# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata , socket
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
from imports import Parse , CNF_Studio_Indexer , speedtest , uservar , tools
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
import webbrowser
import SimpleDownloader
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
IiiIII111iI = "3.5.9"
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
I11 = xbmcaddon . Addon ( ) . setSetting
Oo0o0000o0o0 = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv' ) )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
oO0o0o0ooO0oO = os . path . join ( oOo0oooo00o , 'userdata' )
oo0o0O00 = os . path . join ( oO0o0o0ooO0oO , 'addon_data' , IiII )
oO = os . path . join ( oo0o0O00 , 'wizard.log' )
i1iiIIiiI111 = uservar . ADDONTITLE
oooOOOOO = xbmc . translatePath ( 'special://profile/' )
i1iiIII111ii = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1i1II = os . path . join ( oOo0oooo00o , 'addons' )
i1iIIi1 = os . path . join ( i1i1II , 'packages' )
ii11iIi1I = os . path . join ( i1i1II , 'HUB' )
iI111I11I1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
OOooO0OOoo = Net ( )
iIii1 = xbmcgui . Dialog ( )
oOOoO0 = oo00 . getSetting ( 'Build' )
O0OoO000O0OO = oo00 . getSetting ( 'Local' )
iiI1IiI = oo00 . getSetting ( 'Remote' )
II = oo00 . getSetting ( 'LocalM3u' )
ooOoOoo0O = oo00 . getSetting ( 'TEXTCOL' )
OooO0 = oo00 . getSetting ( 'Downloads' )
II11iiii1Ii = xbmc . translatePath ( 'special://logpath/' )
OO0o = oo00 . getSetting ( 'User' )
Ooo = oo00 . getSetting ( 'Pass' )
O0o0Oo = oo00 . getSetting ( 'AdultPass' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
O00o0OO = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
I11i1 = xbmc . translatePath ( 'special://database' )
iIi1ii1I1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
o0 = xbmc . translatePath ( 'special://thumbnails' ) ;
I11II1i = "GenieTv"
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
IIiiiiiiIi1I1 = 'http://'
I1IIIii = datetime . now ( )
oOoOooOo0o0 = base64 . decodestring ( 'LnBocA==' )
OOOO = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OOO00 = [ ]
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
I11iii1Ii = oo00 . getLocalizedString
I1IIiiIiii = CookieJar ( )
O000oo0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( I1IIiiIiii ) )
O000oo0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOOOi11i1 = int ( sys . argv [ 1 ] )
IIIii1II1II = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i1I1iI = os . path . join ( iIi1ii1I1 , 'favorites' )
oo0OooOOo0 = iIi1ii1I1 + '/addons.ini'
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/' )
o0O = xbmc . translatePath ( 'special://home/userdatabroke/' )
O00oO = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
I11i1I1I = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oO0Oo = I11i1I1I + 'GenieTvWatched'
oOOoo0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
o00OO00OoO = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( oO0Oo ) :
 os . makedirs ( oO0Oo )
OOOO0OOoO0O0 = oO0Oo + 'watched.txt'
if not os . path . exists ( OOOO0OOoO0O0 ) :
 open ( OOOO0OOoO0O0 , 'w+' )
O0Oo000ooO00 = open ( OOOO0OOoO0O0 ) . read ( )
oO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlNvbGQv' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOO00O = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( i1I1iI ) == True :
 OOoOO0oo0ooO = open ( i1I1iI ) . read ( )
else : OOoOO0oo0ooO = [ ]
O0o0O00Oo0o0 = oo00 . getSetting ( 'debug' )
if os . path . exists ( iIi1ii1I1 ) == False :
 os . makedirs ( iIi1ii1I1 )
def O00O0oOO00O00 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = ''
 iiI111I1iIiI = ''
 try :
  i1i = urllib2 . urlopen ( i1Oo00 )
  iiI111I1iIiI = i1i . read ( )
  i1i . close ( )
 except : pass
 if iiI111I1iIiI != '' :
  return iiI111I1iIiI
 else :
  iiI111I1iIiI = 'Failed'
  return iiI111I1iIiI
  if 41 - 41: i1i1I1IIii1II . oooOo0oo0oo - Iii * o0ii1I / IiI1i11I % III1iiIii
O0OOO = [ ]
II11iIiIIIiI = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if II11iIiIIIiI != 'Failed' :
 O0OOO . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not II11iIiIIIiI != 'Failed' :
 o0o = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if o0o != 'Failed' :
  O0OOO . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not o0o != 'Failed' :
  o00OooOO000 = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if o00OooOO000 != 'Failed' :
   O0OOO . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not o00OooOO000 != 'Failed' :
   OOoOoo = O00O0oOO00O00 ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if OOoOoo != 'Failed' :
    O0OOO . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
oO0000OOo00 = ( str ( O0OOO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
iiIi1IIiIi = oO0000OOo00 + 'GenieArt/NEW/'
if 75 - 75: i1IiiiI1iI + i1iIi
if 68 - 68: Ii % Ii1I + Ii
def iii ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  II1I = 'genie tv repo not being installed '
  O0 ( )
 else :
  i1II1Iiii1I11 ( )
  if 9 - 9: Ii1I / I1ii11iIi11i - oOo0O0Ooo / ii / iI11I1II1I1I - I11i
def i1II1Iiii1I11 ( ) :
 if 91 - 91: IiI1i11I % ooOoO0O00 % iI11I1II1I1I
 IIi1I11I1II = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 ii11IIII11I = open ( Oo0OoO00oOO0o ) . read ( )
 OOooo = open ( OOO00O ) . read ( )
 if 90 - 90: I11i % ooOoO0O00 / oO0o
 IIi = re . compile ( 'version="([^"]*)" provider' ) . findall ( ii11IIII11I )
 i1Iii1i1I = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( OOooo )
 OOoO00 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( IIi1I11I1II )
 IiI111111IIII = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( IIi1I11I1II )
 for i1Ii in IIi :
  ii111iI1iIi1 = i1Ii
  for OOO in OOoO00 :
   if not OOO == ii111iI1iIi1 :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    oo0OOo0 ( )
   if OOO == ii111iI1iIi1 :
    I11IiI
 for O0ooO0Oo00o in i1Iii1i1I :
  ooO0oOOooOo0 = O0ooO0Oo00o
  for i1I1ii11i1Iii in IiI111111IIII :
   if not i1I1ii11i1Iii == ooO0oOOooOo0 :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    O0 ( )
   if i1I1ii11i1Iii == ooO0oOOooOo0 :
    xbmc . sleep ( 100 )
    I11IiI
def I1IiiiiI ( ) :
 if not os . path . exists ( ooooooO0oo ) :
  o0OIiII ( 'Change Log 27/7/17 - v3.5.9' , '[COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 29/7/17 - v3.5.9' , '[COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
def Iii1I1I11iiI1 ( ) :
 iii ( )
 I1IiiiiI ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I1I1i1I ( )
 else :
  if 30 - 30: ii
  if 5 - 5: i1iIi - IIiIiII11i - ii % o0ii1I + oOo0O0Ooo * iI11I1II1I1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 4009 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
   if 8 - 8: I11i % o0o00Oo0O / oOo0O0Ooo - i1i1I1IIii1II
  if oo00 . getSetting ( 'Music' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Adult Gallery[/COLOR]' , '' , 9999999 , iiIi1IIiIi + 'AG.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'tools.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if OO ( ) == 'android' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '' , 10050 , iiIi1IIiIi + 'Addons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def I1I1i1I ( ) :
 if 57 - 57: i1IiiiI1iI % o0ii1I + I11i - I1ii11iIi11i
 if 65 - 65: Iii . OOooOOo
 if 39 - 39: IIiIiII11i / i1iIi + i1IiiiI1iI / OOooOOo
 if 13 - 13: III1iiIii + o0o00Oo0O + IiI1i11I % oOo0O0Ooo / I11i . III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  if 86 - 86: i1i1I1IIii1II * I11i % ooOoO0O00 . o0ii1I . Ii
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if O0o0Oo == '5knuckleshuffle' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Adult Gallery[/COLOR]' , '' , 9999999 , iiIi1IIiIi + 'AG.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def tools ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']Change Log[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  ii1iII1II ( )
 if O0O00Oo == 1 :
  oo0OOo0 ( )
 if O0O00Oo == 2 :
  oooooo0O000o ( )
 if O0O00Oo == 3 :
  OoO ( )
 if O0O00Oo == 4 :
  ooO0O0O0ooOOO ( oOOo0O00o )
 if O0O00Oo == 5 :
  iIii1 . ok ( i1 , i1111 )
 if O0O00Oo == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if O0O00Oo == 7 :
  iIiIi11 ( )
  if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / i1i1I1IIii1II
def IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  Ii1I1i ( iIIIiIi , url , 21009 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  if 100 - 100: oOo0O0Ooo / I11i % IIiIiII11i % I1ii11iIi11i % oooOo0oo0oo
def O00oO000O0O ( url ) :
 url = url
 I1i1i1iii = OO ( )
 if I1i1i1iii ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif I1i1i1iii ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 16 - 16: o0ii1I + III1iiIii * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
  if 67 - 67: ii / oOo0O0Ooo * o0ii1I + Iii
def OooOo0ooo ( ) :
 oOOo0O00o = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( oOOo0O00o , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( oOOo0O00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
def I1i ( ) :
 O00Oooo = i11I ( )
 o00Oo0oooooo = O00Oooo . replace ( II11iiii1Ii , "" )
 if os . path . exists ( O00Oooo ) or not O00Oooo == False :
  O0oO0 = open ( O00Oooo , mode = 'r' ) ; iII11 = O0oO0 . read ( ) ; O0oO0 . close ( )
  o0OIiII ( "%s - %s" % ( i1 , o00Oo0oooooo ) , iII11 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OooOo0ooo ( ) :
 oOOo0O00o = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( oOOo0O00o , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( oOOo0O00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
def iiIiii1IIIII ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 67 - 67: o0ii1I / III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 9 - 9: o0o00Oo0O % o0o00Oo0O - I11i
def OoOiiI1IIIi ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def II11IiIi11 ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIOOO0O00O0OOOO = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iiii1I = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIOOO0O00O0OOOO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 900302 , ooO0OO , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for OOo0 in I1iiii1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , OOo0 , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def oO00ooooO0o ( url ) :
 oo0o = OooOoooOo ( url )
 IIOOO0O00O0OOOO = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( oo0o )
 o0oO0oooOoo = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( oo0o )
 for url , iIIIiIi in IIOOO0O00O0OOOO :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , iIIIiIi in o0oO0oooOoo :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def I1III1111iIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for OooOo0oo0O0o00O , I1i11 in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + OooOo0oo0O0o00O , I1i11 )
def IiIi1I1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def IiIIi1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , ooO0OO , Oo00OOOOO , '' )
 for url in next :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def IIIIiii1IIii ( url ) :
 I1i111I = OooOoooOo ( url )
 II1i11I = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIIIiIi , url in i1Iii1i1I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIIIiIi , url in ii1I1IIii11 :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in II1i11I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 67 - 67: IiI1i11I + Iii / I11i . i1i1I1IIii1II + oooOo0oo0oo
def ooOoOo0 ( url ) :
 if 'drive' in url :
  I11iiiiI1i ( url )
 else :
  I1i111I = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( I1i111I )
  for url in IIi :
   I11iiiiI1i ( url )
def iI1i11 ( url ) :
 OoOOoooOO0O = liveresolver . resolve ( url )
 ooo00Ooo = xbmcgui . ListItem ( path = OoOOoooOO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
def Oo0o0O00 ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 ii1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
def i11I ( ) :
 I1i11OO = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return I1i11OO
 if 84 - 84: i1iIi % o0ii1I + Ii
def II1I1Ii ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , Ooo0O0oooo :
  return Ooo0O0oooo
 return True
def iiI ( ) :
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 if 39 - 39: o0o00Oo0O + i1IiiiI1iI
 if 91 - 91: ii - iI11I1II1I1I + OOooOOo / oO0o . OOooOOo + o0o00Oo0O
 if 26 - 26: Ii1I - ii
 if 11 - 11: oOo0O0Ooo * i1i1I1IIii1II
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def o000oo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   o00o0 ( )
  if O0O00Oo == 1 :
   II1III1I1I1Ii ( )
  if O0O00Oo == 2 :
   OOOOoO00o0O ( I1I1I1IIi1III )
  if O0O00Oo == 3 :
   II11IiiIII ( oOOo0O00o )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 58 - 58: o0ii1I + I11i - oOo0O0Ooo
def i1i1ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 46 - 46: OOooOOo + oO0o
  if 70 - 70: IiI1i11I / iI11I1II1I1I
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Supremacy[/COLOR]' , '' , 1131000 , iiIi1IIiIi + 'supremacy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']24/7 STREAMS[/COLOR]' , '' , 9050000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
   if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
   if 96 - 96: ii + i1i1I1IIii1II
   if 44 - 44: i1i1I1IIii1II
 else :
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: OOooOOo / IIiIiII11i
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Supremacy[/COLOR]' , '' , 1131000 , iiIi1IIiIi + 'supremacy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']24/7 STREAMS[/COLOR]' , '' , 9050000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
   if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
   if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
   if 42 - 42: I1ii11iIi11i
   if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
   if 46 - 46: I1ii11iIi11i
   if 1 - 1: IiI1i11I
   if 97 - 97: oooOo0oo0oo + IiI1i11I + o0o00Oo0O + Ii
   if 77 - 77: I11i / ii
   if 46 - 46: I11i % iI11I1II1I1I . IiI1i11I % IiI1i11I + Ii
   if 72 - 72: iI11I1II1I1I * o0ii1I % i1iIi / oO0o
   if 35 - 35: i1iIi + ooOoO0O00 % Ii1I % Iii + i1i1I1IIii1II
   if 17 - 17: ooOoO0O00
   if 21 - 21: I1ii11iIi11i
   if 29 - 29: Iii / IIiIiII11i / i1iIi * oooOo0oo0oo
   if 10 - 10: i1IiiiI1iI % III1iiIii * III1iiIii . Iii / o0ii1I % oooOo0oo0oo
   if 49 - 49: oO0o / i1i1I1IIii1II + o0o00Oo0O * I11i
   if 28 - 28: i1iIi + Ii / Iii % OOooOOo % I1ii11iIi11i - o0o00Oo0O
   if 54 - 54: ooOoO0O00 + IIiIiII11i
   if 83 - 83: Ii1I - oOo0O0Ooo + oooOo0oo0oo
   if 5 - 5: o0ii1I
   if 46 - 46: III1iiIii
   if 45 - 45: i1iIi
   if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
   if 17 - 17: oooOo0oo0oo / oooOo0oo0oo / Iii
   if 1 - 1: ooOoO0O00 . Ii % oooOo0oo0oo
   if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % III1iiIii / o0ii1I . o0ii1I
   if 14 - 14: I11i . oooOo0oo0oo . Iii + ii - oooOo0oo0oo + III1iiIii
   if 9 - 9: o0ii1I
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oooooOOO000Oo ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  Ooo00OoOOO ( )
 if O0O00Oo == 1 :
  Oo0OO0000oooo ( )
 if O0O00Oo == 2 :
  IIII1iII ( )
 if O0O00Oo == 3 :
  ii1III11 ( )
 if O0O00Oo == 4 :
  I1iiIIIi11 ( )
 if O0O00Oo == 5 :
  Ii1I11ii1i ( )
  if 89 - 89: IiI1i11I . o0o00Oo0O / Ii1I % OOooOOo . I1ii11iIi11i
  if 50 - 50: IIiIiII11i + Ii1I . ooOoO0O00 % I11i
def IIIi ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   O00OoO0o ( )
  if O0O00Oo == 1 :
   i1i111iI ( )
  if O0O00Oo == 2 :
   IIiiI ( oOOo0O00o )
  if O0O00Oo == 3 :
   III1i11 ( )
  if O0O00Oo == 4 :
   iiI111 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0O00Oo == 5 :
   I1iIiIi11i11 ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 52 - 52: i1iIi + o0o00Oo0O . IiI1i11I . Ii1I . oO0o
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oo000ii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 78 - 78: ii . oO0o + i1iIi - ooOoO0O00
 if 31 - 31: ii . oooOo0oo0oo
 if 83 - 83: IiI1i11I . o0o00Oo0O / I1ii11iIi11i / oooOo0oo0oo - IIiIiII11i
 if 100 - 100: oO0o
 if 46 - 46: OOooOOo / iI11I1II1I1I % IiI1i11I . iI11I1II1I1I * IiI1i11I
def IIi1ii1Ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   OoOoO ( )
  if O0O00Oo == 1 :
   o0ii1i ( )
  if O0O00Oo == 2 :
   oOOoo ( )
  if O0O00Oo == 3 :
   iII1111III1I ( )
  if O0O00Oo == 4 :
   ii11i ( )
  if O0O00Oo == 5 :
   O00oOo00o0o ( )
  if O0O00Oo == 6 :
   O00oO0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 70 - 70: Iii . Ii1I * ii - III1iiIii * oOo0O0Ooo + OOooOOo
  if 10 - 10: I11i / Ii
  if 92 - 92: Iii . i1IiiiI1iI
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oOO00O0Ooooo00 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   O000 = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 79 - 79: ii - oOo0O0Ooo
   if 69 - 69: Iii
   if 95 - 95: i1iIi + Ii * i1IiiiI1iI - ooOoO0O00 * i1IiiiI1iI - iI11I1II1I1I
   if 75 - 75: ii * III1iiIii
  oOOoo00O00o = [ O000 , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I1Iiiiiii ( )
  if O0O00Oo == 1 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , iIIIiIi )
  if O0O00Oo == 2 :
   IiiI1iiiiI1iI ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0O00Oo == 3 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , iIIIiIi )
 else :
  if 43 - 43: i1i1I1IIii1II - ii
  if 3 - 3: o0o00Oo0O / IiI1i11I
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 31 - 31: oooOo0oo0oo + I11i . ii
  if 89 - 89: IIiIiII11i + ooOoO0O00 + IIiIiII11i
  if 7 - 7: o0o00Oo0O % I11i + Ii1I * IiI1i11I - IiI1i11I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 42 - 42: OOooOOo * OOooOOo * i1IiiiI1iI . Iii
  if 51 - 51: oooOo0oo0oo % iI11I1II1I1I - ii % i1iIi * iI11I1II1I1I % oO0o
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / III1iiIii
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: IIiIiII11i
def Ii1ii111i1 ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def IiiI1iiiiI1iI ( url ) :
 I1i111I = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 ii1I1IIii11 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for iIIIiIi , ooO0OO , url in IIi :
  if '247ch' in url :
   oOoo000 ( iIIIiIi , url , 10190 , ooO0OO )
  elif '.m3u' in url :
   oOoo000 ( iIIIiIi , url , 1019 , ooO0OO )
  elif '.xml' in url :
   oOoo000 ( iIIIiIi , url , 1018 , ooO0OO )
  else :
   OooOo00o ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in i1Iii1i1I :
  if '.xml' in url :
   oOoo000 ( iIIIiIi , url , 1018 , ooO0OO )
  elif '.m3u' in url :
   oOoo000 ( iIIIiIi , url , 1019 , ooO0OO )
  else :
   OooOo00o ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in ii1I1IIii11 :
  OooOo00o ( iIIIiIi , url , 8043 , ooO0OO )
def IiI11i1IIiiI ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def OoOo00o0OO ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 1 - 1: oOo0O0Ooo % i1iIi
def oOoO00 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 40 - 40: I11i
def OOOooo ( url ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , O0oOOo0Oo , o000O000 , IIo0o0O0O00oOOo , O000OOO in IIi :
  if o000O000 == '123' :
   o000O000 = iiIi1IIiIi + 'appstreams.png'
  if IIo0o0O0O00oOOo == '123' :
   IIo0o0O0O00oOOo = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100010 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif 'playlist' in url :
   I1I1II1I11 ( iIIIiIi , url , 100007 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif 'watchseries' in url :
   I1I1II1I11 ( iIIIiIi , url , 100100 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif not 'http' in url :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , o000O000 , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100005 , o000O000 , IIo0o0O0O00oOOo , O000OOO , '' )
   if 86 - 86: Ii1I * o0o00Oo0O * III1iiIii
def Ooo0oo ( url ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if ooO0OO == '123' :
   ooO0OO = iiIi1IIiIi + 'appstreams.png'
  if IIo0o0O0O00oOOo == '123' :
   IIo0o0O0O00oOOo = Oo00OOOOO
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100004 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif 'playlist' in url :
   I1I1II1I11 ( iIIIiIi , url , 100007 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif 'watchseries' in url :
   I1I1II1I11 ( iIIIiIi , url , 100100 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif not 'http' in url :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100005 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
   if 41 - 41: OOooOOo * Iii / OOooOOo % i1i1I1IIii1II
def IioO0oOOO0Ooo ( url ) :
 if 38 - 38: oOo0O0Ooo
 II11iIiIIIiI = Oo00oo0000OO ( url )
 oOo0OoOOo0 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in oOo0OoOOo0 :
  o000O000 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for o000O000 in o000O000 :
   o000O000 = o000O000
  iIIIiIi = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for iIIIiIi in iIIIiIi :
   if 'elete' in iIIIiIi :
    pass
   elif 'rivate Vid' in iIIIiIi :
    pass
   else :
    iIIIiIi = ( iIIIiIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iII11I1Ii1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( i1i1i1I ) )
  for iII11I1Ii1 in iII11I1Ii1 :
   iII11I1Ii1 = iII11I1Ii1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = url
  ii1oOoO0o0ooo ( '[COLORred]' + str ( iII11I1Ii1 ) + '[/COLOR] : ' + str ( iIIIiIi ) , str ( url ) , 100009 , str ( o000O000 ) , Oo00OOOOO , '' , '' )
  I1iI1ii1II ( 'movies' , '' )
  if 92 - 92: Iii / Iii . Ii1I
def ii1iIi1II ( ) :
 IIIIi1I ( 'Featured 24/7' , '' , 9070000 , iiIi1IIiIi + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 IIIIi1I ( '24/7 Tv Thows' , '' , 9080000 , iiIi1IIiIi + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 IIIIi1I ( '24/7 Movies' , '' , 9090000 , iiIi1IIiIi + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 IIIIi1I ( '24/7 Cable' , '' , 9100000 , iiIi1IIiIi + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 IIIIi1I ( '24/7 Random Stream' , '' , 9110000 , iiIi1IIiIi + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % Iii
def iiiI1ii ( ) :
 oOOo0O00o = 'http://arconaitv.me/'
 iii1111iiI1ii = 'index.php#shows'
 I1i111I = BeautifulSoup ( requests . get ( oOOo0O00o + iii1111iiI1ii ) . content )
 IIiii = I1i111I . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for I1i1i in IIiii :
  OOOOooO0oO00O0o = I1i1i . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OOOOooO0oO00O0o :
   ooOO00oOOo000 = iiI111I1iIiI . text
  IIii11II11II1 = I1i1i . findAll ( 'a' )
  for iiI111I1iIiI in IIii11II11II1 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    II1IOoOo000oOo0oo = oOOo0O00o + iiI111I1iIiI [ 'href' ]
   iIIIiIi = iiI111I1iIiI [ 'title' ]
   oO0O = BeautifulSoup ( requests . get ( II1IOoOo000oOo0oo ) . content )
   oOO = oO0O . findAll ( 'source' )
   for iiiIIiIi in oOO :
    OooOOO = iiiIIiIi [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ii1oOoO0o0ooo ( iIIIiIi , OooOOO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 48 - 48: iI11I1II1I1I % ooOoO0O00 % IiI1i11I + i1iIi
    if 30 - 30: Ii % iI11I1II1I1I . Iii % iI11I1II1I1I
def oOO00oO00O0OO ( ) :
 oOOo0O00o = 'http://arconaitv.me/'
 iii1111iiI1ii = 'index.php#movies'
 I1i111I = BeautifulSoup ( requests . get ( oOOo0O00o + iii1111iiI1ii ) . content )
 IIiii = I1i111I . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for I1i1i in IIiii :
  OOOOooO0oO00O0o = I1i1i . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OOOOooO0oO00O0o :
   ooOO00oOOo000 = iiI111I1iIiI . text
  IIii11II11II1 = I1i1i . findAll ( 'a' )
  for iiI111I1iIiI in IIii11II11II1 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    II1IOoOo000oOo0oo = oOOo0O00o + iiI111I1iIiI [ 'href' ]
   iIIIiIi = iiI111I1iIiI [ 'title' ]
   oO0O = BeautifulSoup ( requests . get ( II1IOoOo000oOo0oo ) . content )
   oOO = oO0O . findAll ( 'source' )
   for iiiIIiIi in oOO :
    OooOOO = iiiIIiIi [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ii1oOoO0o0ooo ( iIIIiIi , OooOOO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 96 - 96: OOooOOo
    if 54 - 54: i1IiiiI1iI
def o0oO0oOO ( ) :
 oOOo0O00o = 'http://arconaitv.me/'
 iii1111iiI1ii = 'index.php#cable'
 I1i111I = BeautifulSoup ( requests . get ( oOOo0O00o + iii1111iiI1ii ) . content )
 IIiii = I1i111I . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for I1i1i in IIiii :
  OOOOooO0oO00O0o = I1i1i . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OOOOooO0oO00O0o :
   ooOO00oOOo000 = iiI111I1iIiI . text
  IIii11II11II1 = I1i1i . findAll ( 'a' )
  for iiI111I1iIiI in IIii11II11II1 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    II1IOoOo000oOo0oo = oOOo0O00o + iiI111I1iIiI [ 'href' ]
   iIIIiIi = iiI111I1iIiI [ 'title' ]
   oO0O = BeautifulSoup ( requests . get ( II1IOoOo000oOo0oo ) . content )
   oOO = oO0O . findAll ( 'source' )
   for iiiIIiIi in oOO :
    OooOOO = iiiIIiIi [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ii1oOoO0o0ooo ( iIIIiIi , OooOOO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 89 - 89: i1iIi + o0ii1I * i1iIi / i1iIi
def i11i11 ( ) :
 oO0O = BeautifulSoup ( requests . get ( 'http://arconaitv.me/stream.php?id=random' ) . content )
 oOO = oO0O . findAll ( 'source' )
 for iiiIIiIi in oOO :
  OooOOO = iiiIIiIi [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  ii1oOoO0o0ooo ( 'Random Pick' , OooOOO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 72 - 72: ooOoO0O00 - IIiIiII11i - oooOo0oo0oo + oooOo0oo0oo * I11i * oooOo0oo0oo
def iII1I1 ( ) :
 oOOo0O00o = 'http://arconaitv.me/'
 iii1111iiI1ii = 'index.php#shows'
 if 85 - 85: IiI1i11I * I11i
 I1i111I = BeautifulSoup ( requests . get ( oOOo0O00o + iii1111iiI1ii ) . content )
 IIiii = I1i111I . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for I1i1i in IIiii :
  OOOOooO0oO00O0o = I1i1i . findAll ( 'a' )
  for iiI111I1iIiI in OOOOooO0oO00O0o :
   if iiI111I1iIiI . has_key ( 'href' ) :
    II1IOoOo000oOo0oo = oOOo0O00o + iiI111I1iIiI [ 'href' ]
   iIIIiIi = iiI111I1iIiI [ 'title' ]
   ii1iii11i1 = iiI111I1iIiI . findAll ( 'img' )
   for I11Oo00oO0O in ii1iii11i1 :
    ooO0OO = oOOo0O00o + I11Oo00oO0O [ 'src' ]
    oO0O = BeautifulSoup ( requests . get ( II1IOoOo000oOo0oo ) . content )
    oOO = oO0O . findAll ( 'source' )
    for iiiIIiIi in oOO :
     OooOOO = iiiIIiIi [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     ii1oOoO0o0ooo ( iIIIiIi , OooOOO , 9060000 , ooO0OO , ooO0OO , '' , '' )
     if 96 - 96: Ii1I / IIiIiII11i . o0ii1I - IiI1i11I * Iii * i1i1I1IIii1II
def O00oo0ooO ( name , url ) :
 import urlresolver
 try :
  iiIii1ii = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIii1ii , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 33 - 33: i1IiiiI1iI
 if 62 - 62: Ii1I + o0ii1I + ooOoO0O00 / ii
def IIiiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if '.php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100210 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
   if 37 - 37: I11i % i1iIi
   if 83 - 83: oooOo0oo0oo . i1IiiiI1iI + i1i1I1IIii1II - oooOo0oo0oo * i1IiiiI1iI / i1IiiiI1iI
   if 39 - 39: i1IiiiI1iI / I1ii11iIi11i % oO0o % Ii
def o0o0Ooo0 ( iconimage , url , extra ) :
 o000O000 = ' '
 OoO000O = ' '
 IIo0o0O0O00oOOo = ' '
 OOo = ' '
 iIIiiIIIi1I = Oo00oo0000OO ( url )
 o000O000 = re . compile ( '<img src="(.+?)">' ) . findall ( iIIiiIIIi1I )
 for o000O000 in o000O000 :
  o000O000 = o000O000
 OO0o0o0oo0O = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( iIIiiIIIi1I )
 for IIo0o0O0O00oOOo in OO0o0o0oo0O :
  IIo0o0O0O00oOOo = IIo0o0O0O00oOOo
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( iIIiiIIIi1I )
 for url , OOo in IIi :
  OOo = 'S' + ( OOo ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  IIIIi1I ( ( OOo ) . replace ( '  ' , '' ) , url , 100101 , o000O000 , IIo0o0O0O00oOOo , OoO000O , '' )
  I1iI1ii1II ( 'Movies' , 'info' )
  if 40 - 40: I11i + I1ii11iIi11i . I11i % i1iIi
def I11I1IIiiII1 ( url , name , fanart , extra , iconimage ) :
 IIIIIii1ii11 = extra
 OOo = name
 iIIiiIIIi1I = Oo00oo0000OO ( url )
 o000O000 = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( iIIiiIIIi1I )
 for url , name , OOOooo0OooOoO in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  OOOooo0OooOoO = OOOooo0OooOoO
  oOoOOOo = name + ' - [COLORred]' + OOOooo0OooOoO + '[/COLOR]'
  IIIIi1I ( oOoOOOo , url , 100102 , o000O000 , fanart , 'Aired : ' + OOOooo0OooOoO , oOoOOOo )
  if 43 - 43: ooOoO0O00
def I1i11II ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = Oo00oo0000OO ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , name in IIi :
  for ooo00Ooo in o00OO00OoO :
   if ooo00Ooo in oOOo0O00o :
    URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
    ii1oOoO0o0ooo ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  IIIIi1I ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 31 - 31: i1i1I1IIii1II / III1iiIii * I11i . IIiIiII11i
  if 89 - 89: o0o00Oo0O
def IIIII1I1Ii11iI ( url , name ) :
 oO00OoOO = name
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11IIiIiI ( url , oO00OoOO )
 for url in i1Iii1i1I :
  I11IIiIiI ( url , oO00OoOO )
 for url in ii1I1IIii11 :
  I11IIiIiI ( url , oO00OoOO )
  if 5 - 5: I1ii11iIi11i * OOooOOo
def I11IIiIiI ( url , season_name ) :
 if 'daclips.in' in url :
  ii1I11iIiIII1 ( url , season_name )
 elif 'filehoot.com' in url :
  oOO0OOOOoooO ( url , season_name )
 elif 'allmyvideos.net' in url :
  i1ii11 ( url , season_name )
 elif 'vidspot.net' in url :
  ii1i ( url , season_name )
 elif 'vodlocker' in url :
  IIioo0OO ( url , season_name )
 elif 'vidto' in url :
  IiiI11i1I ( url , season_name )
  if 80 - 80: oooOo0oo0oo / Iii / OOooOOo + ooOoO0O00 - I1ii11iIi11i
  if 11 - 11: I11i * oO0o
def IiiI11i1I ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIi1IiI , iIIIiIi in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 39 - 39: o0ii1I % o0o00Oo0O % OOooOOo . ooOoO0O00
  if 86 - 86: oO0o * ii
def i1ii11 ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIi1IiI , iIIIiIi in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 71 - 71: iI11I1II1I1I - oooOo0oo0oo . oOo0O0Ooo % ii + oooOo0oo0oo
def ii1i ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIi1IiI , iIIIiIi in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 26 - 26: I1ii11iIi11i + oooOo0oo0oo / oO0o % OOooOOo % Ii1I + IIiIiII11i
def IIioo0OO ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIi1IiI in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 31 - 31: Iii % oooOo0oo0oo * Iii
def ii1I11iIiIII1 ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for iIi1IiI in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 45 - 45: ooOoO0O00 . oOo0O0Ooo + oooOo0oo0oo - ii % i1iIi
def oOO0OOOOoooO ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIi1IiI in IIi :
  I11IIIiIi11 ( iIi1IiI , season_name )
  if 1 - 1: iI11I1II1I1I
def I11IIIiIi11 ( Link , season_name ) :
 if 'http:/' in Link :
  ooi1II1I ( Link )
  if 95 - 95: oO0o - oooOo0oo0oo / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 oo0OoOooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in oo0OoOooo :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 95 - 95: III1iiIii * Ii1I % i1iIi % o0ii1I - o0ii1I
def IIIIi1I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = True )
 return o0Oo0
 if 91 - 91: Iii / ooOoO0O00 * ooOoO0O00
 if 25 - 25: iI11I1II1I1I . oooOo0oo0oo * i1i1I1IIii1II - o0ii1I
def ii1oOoO0o0ooo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOO000O = [ ]
  oOO000O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = False )
 return o0Oo0
 if 99 - 99: ooOoO0O00 / o0o00Oo0O - OOooOOo % I11i - oooOo0oo0oo + ii
def O0ooOoO ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + Iii
def IiiIi ( url ) :
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIi . play ( url ) . strip ( )
 except : pass
 if 40 - 40: IiI1i11I . i1i1I1IIii1II + oOo0O0Ooo + Ii1I + i1IiiiI1iI
def ooi1II1I ( url ) :
 iIIi = xbmc . Player ( )
 import urlresolver
 try : iIIi . play ( url )
 except : pass
 if 26 - 26: iI11I1II1I1I
def Oo00oo0000OO ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = ''
 iiI111I1iIiI = ''
 try :
  i1i = urllib2 . urlopen ( i1Oo00 )
  iiI111I1iIiI = i1i . read ( )
  i1i . close ( )
 except : pass
 if iiI111I1iIiI != '' :
  return iiI111I1iIiI
 else :
  iiI111I1iIiI = 'Opened'
  return iiI111I1iIiI
  if 87 - 87: Ii1I / ii - I1ii11iIi11i % OOooOOo % III1iiIii % I1ii11iIi11i
  if 29 - 29: ii . oOo0O0Ooo % Ii1I - IiI1i11I
  if 8 - 8: ooOoO0O00
def Oo0OO0000oooo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   iIiI1 ( )
  if O0O00Oo == 1 :
   IIii1I11iiii1 ( )
  if O0O00Oo == 2 :
   o0oooO ( )
  if O0O00Oo == 3 :
   ooOo ( )
  if O0O00Oo == 4 :
   o0oO0OoO0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def ii1III11 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiIi1IIiIi + 'Fitness.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Go Fishing[/COLOR]' , str ( oO0000OOo00 ) , 8090 , iiIi1IIiIi + 'GoFishing.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiIi1IIiIi + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 70 - 70: i1i1I1IIii1II - i1i1I1IIii1II
 if 57 - 57: oOo0O0Ooo - I11i + oO0o % I1ii11iIi11i
 if 26 - 26: IiI1i11I . IiI1i11I
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   i1oO = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1oO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O00Oo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O00Oo == 0 :
    iI ( II1I )
    OOOOo0o00OO0000 ( )
   elif O0O00Oo == 1 :
    Ii1IIi ( II1I )
  else :
   pass
   if 43 - 43: i1IiiiI1iI % IiI1i11I
def Ii1IIi ( addon ) :
 i1oO = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 69 - 69: IiI1i11I % oO0o
def iI ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOOoO = os . path . join ( IIIII , 'default.py' )
 iIi11ii = open ( oOOoO , "w+" )
 if 50 - 50: o0ii1I / OOooOOo * o0ii1I
 iIi11ii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iIi11ii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iIi11ii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
 if 25 - 25: Iii + OOooOOo . I11i % OOooOOo * oooOo0oo0oo
 if 32 - 32: Ii - i1IiiiI1iI
 if 53 - 53: ii - III1iiIii
def oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1iIIIiiiI = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoO00oo00 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1i11I = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Oo0Oo0O = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO in i1iIIIiiiI :
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 90037 , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO )
  elif iIIIiIi == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO )
 for iIIIiIi , ooO0OO , url , iIiII in OoO00oo00 :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , iIiII , '' )
 for iIIIiIi , ooO0OO , url , iIiII in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , iIiII , '' )
 for iIIIiIi , url , ooO0OO , iIiII in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , iIiII , '' )
 for iIIIiIi , url , ooO0OO , iIiII in ii1I1IIii11 :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , iIiII , '' )
 for iIIIiIi , url , ooO0OO , iIiII in II1i11I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , iIiII , '' )
 for iIIIiIi , url , ooO0OO in Oo0Oo0O :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , '' , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def i1i1IIIIIIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , ooO0OO , url , iIiII in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , iIiII , '' )
 for iIIIiIi , url , ooO0OO , iIiII in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , iIiII , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  if 65 - 65: I11i
def I1ii1II1iII ( ) :
 II1i = [ 'serialsearch' , 'moviesearch' ]
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 if i1i1IiIiIi1Ii == '' :
  pass
 else :
  for oO0ooOO in II1i :
   IIi1iI1 = Oo0o0000o0o0 + oO0ooOO + '.php'
   iIIiiIIIi1I = OooOoooOo ( IIi1iI1 )
   if iIIiiIIIi1I != 'Opened' :
    IIIii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( iIIiiIIIi1I )
    for iIIIiIi , oOOo0O00o , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO in IIIii1I :
     if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
      IIi11i1II = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in IIi11i1II :
       if ooo00Ooo == oOOo0O00o :
        iIIIiIi = '[COLORred]* [/COLOR]' + ( iIIIiIi ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OO0ooo0o0 = open ( OOOO0OOoO0O0 , "a" )
        OO0ooo0o0 . write ( 'item="' + iIIIiIi + '"\n' )
        OO0ooo0o0 . close
      if 'php' in oOOo0O00o :
       I1I1II1I11 ( iIIIiIi , oOOo0O00o , 90037 , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO )
      else :
       Ii1I1i ( iIIIiIi , oOOo0O00o , 222 , iiiI1i11Ii , IIo0o0O0O00oOOo , O000OOO )
       if 69 - 69: Ii1I - i1IiiiI1iI
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   if 16 - 16: I1ii11iIi11i
def ii1iI111 ( ) :
 if 80 - 80: oooOo0oo0oo % Ii1I
 if 91 - 91: Iii / o0o00Oo0O - o0ii1I . oOo0O0Ooo
 if 82 - 82: III1iiIii * oooOo0oo0oo / i1i1I1IIii1II
 if 2 - 2: oOo0O0Ooo + I11i . I11i . o0o00Oo0O / Iii
 if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
 if 14 - 14: Ii1I
 if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
 if 56 - 56: ii - Iii - ooOoO0O00
 if 8 - 8: i1IiiiI1iI / oooOo0oo0oo . oOo0O0Ooo + Ii1I / Ii
 if 31 - 31: i1iIi - iI11I1II1I1I + IiI1i11I . I1ii11iIi11i / III1iiIii % iI11I1II1I1I
 if 6 - 6: III1iiIii * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
 if 53 - 53: Iii + iI11I1II1I1I
 if 70 - 70: Ii1I
 if 67 - 67: ii
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + oooOo0oo0oo * III1iiIii
 if 2 - 2: ooOoO0O00 - i1iIi + oOo0O0Ooo . I11i * I11i / OOooOOo
 if 93 - 93: ooOoO0O00
 if 53 - 53: ii + I1ii11iIi11i + i1i1I1IIii1II
 if 24 - 24: IiI1i11I - III1iiIii - IiI1i11I * Ii1I . ii / III1iiIii
 if 66 - 66: I1ii11iIi11i
 if 97 - 97: ooOoO0O00 - ii / i1IiiiI1iI * oOo0O0Ooo
 I1i111I = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 oO0O = requests . get ( 'http://www.djing.com/' ) . content
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( oO0O )
 IIiii = I1i111I . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for I1i1i in IIiii :
  OOOOooO0oO00O0o = I1i1i . findAll ( 'a' )
  for iiI111I1iIiI in OOOOooO0oO00O0o :
   if iiI111I1iIiI . has_attr ( 'href' ) :
    II1IOoOo000oOo0oo = 'https://tvcatchup.com' + iiI111I1iIiI [ 'href' ]
   ii1iii11i1 = iiI111I1iIiI . findAll ( 'img' )
   for I11Oo00oO0O in ii1iii11i1 :
    ooO0OO = I11Oo00oO0O [ 'src' ]
    oO0oOo00o00oO = I11Oo00oO0O [ 'alt' ]
   IIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( iiI111I1iIiI ) )
   for o0000 in IIi :
    OooOo00o ( ( '[COLORgold]' + oO0oOo00o00oO + '[/COLOR][COLORwhite] - [COLORsteelblue]' + o0000 + '[/COLOR]' ) , II1IOoOo000oOo0oo , 90024 , ooO0OO )
    if 42 - 42: i1IiiiI1iI + i1IiiiI1iI * IIiIiII11i
 for oOOo0O00o , ooO0OO , iIIIiIi in i1Iii1i1I :
  if 'Submit' in iIIIiIi :
   pass
  elif '&lt;' in iIIIiIi :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 90025 , 'http://www.djing.com' + ooO0OO , Oo00OOOOO , '' )
   if 78 - 78: ii
 I1iI1ii1II ( 'movies' , 'MAIN' )
def OOoo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 36 - 36: I11i + Iii - III1iiIii + iI11I1II1I1I + ii
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def IiI1i111IiIiIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  i1II11II1 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 5 - 5: I1ii11iIi11i - Ii1I % i1i1I1IIii1II - IIiIiII11i . oOo0O0Ooo + IiI1i11I
def i1i111iI ( ) :
 if 47 - 47: o0o00Oo0O - iI11I1II1I1I - IiI1i11I
 if 46 - 46: o0ii1I . oooOo0oo0oo * oO0o . ii + Ii1I
 if 72 - 72: IIiIiII11i + oooOo0oo0oo
 if 91 - 91: iI11I1II1I1I % oO0o . I11i + o0ii1I + I11i
 if 95 - 95: o0ii1I + Ii1I * oooOo0oo0oo
 if 16 - 16: Iii / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'yr' in oOOo0O00o :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOOo0O00o , 10201 , iiIi1IIiIi + 'rated.png' )
   if 26 - 26: I11i * III1iiIii . ooOoO0O00
def ooOoOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Oo , url , iIIIiIi in IIi :
  if 'id' in url :
   oOoo000 ( ( '[COLORred]RANK [COLORblue]' + Oo + '[COLORred] - [COLORblue]' + iIIIiIi + '[/COLOR]' ) , iIIIiIi , 10202 , iiIi1IIiIi + 'rated.png' )
   if 66 - 66: III1iiIii
def O0oOo ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OO0oOO0ooO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OO00oo = ( url )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 iIii1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 Oo0O0O000 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoO00ooO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1IIIIiii1i = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0IiiiI111I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0OO00oo
 III1I11i1iIi = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0oo0O0OOO0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 76 - 76: Ii / OOooOOo + OOooOOo / ooOoO0O00 * oOo0O0Ooo
 I1IiIIi11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I11i1I1Ii11 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 60 - 60: OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( iIii1iI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0O0O000 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( II1Ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IiIi1iiii = O00O0oOO00O00 ( OOoO00ooO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iiiOOoo = O00O0oOO00O00 ( o0IiiiI111I )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOO = O00O0oOO00O00 ( III1I11i1iIi )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1iiIiI = O00O0oOO00O00 ( OO0oo0O0OOO0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 60 - 60: i1i1I1IIii1II % IiI1i11I / oooOo0oo0oo % i1iIi - OOooOOo % iI11I1II1I1I
 if 82 - 82: OOooOOo + Iii % ooOoO0O00 + III1iiIii / i1IiiiI1iI - I1ii11iIi11i
 O0OoOOOo0Oo = O00O0oOO00O00 ( I1IiIIi11I1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IiI1IIIII1I = O00O0oOO00O00 ( I11i1I1Ii11 )
 if 35 - 35: o0ii1I - o0ii1I + ooOoO0O00 - o0o00Oo0O - i1IiiiI1iI
 if 58 - 58: OOooOOo - IiI1i11I - ii
 if 96 - 96: iI11I1II1I1I
 if 82 - 82: OOooOOo + o0o00Oo0O - III1iiIii % i1i1I1IIii1II * Ii
 if 15 - 15: I11i
 if 39 - 39: oooOo0oo0oo / Ii1I / oOo0O0Ooo * i1IiiiI1iI
 if 44 - 44: o0o00Oo0O + i1iIi . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - Iii
 if 83 - 83: III1iiIii * Iii / I1ii11iIi11i
 if 32 - 32: I11i + OOooOOo - ii
 if 39 - 39: ii * oooOo0oo0oo * o0o00Oo0O . Iii . oO0o + i1iIi
 if 9 - 9: OOooOOo + i1i1I1IIii1II % ii + I11i
 if 56 - 56: ii + Ii1I - IiI1i11I
 if 24 - 24: I11i + i1iIi + Iii - iI11I1II1I1I
 if i1iiIiI != 'Failed' :
  I11Oo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iiIiI )
  for url , iIIIiIi in I11Oo0oO00 :
   IiiI1III1I1 = O00O0oOO00O00 ( url )
   o0OoOoo00O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiiI1III1I1 )
   for i1iii1ii , II1 in o0OoOoo00O :
    II1 = ( II1 . replace ( '.' , ' ' ) )
    if i1i1IiIiIi1Ii in II1 . lower ( ) :
     if '.mkv' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 222 , '' , '' , '' )
     elif '.mp4' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 222 , '' , '' , '' )
     elif '.avi' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 222 , '' , '' , '' )
     elif '.wav' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 27 - 27: o0ii1I + oOo0O0Ooo * iI11I1II1I1I . ii * OOooOOo
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in i1Iii1i1I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: Iii / I11i % I1ii11iIi11i
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for o0oo00o0O0O00 , iIIIiIi in ii1I1IIii11 :
   if o0OO00oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Oo0O0O000 + o0oo00o0O0O00 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in II1i11I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 34 - 34: oooOo0oo0oo . I1ii11iIi11i
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if IiIi1iiii != 'Failed' :
  OOoO0oO00o = [ ]
  Oo0Oo0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIi1iiii )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in Oo0Oo0O :
   if o0OO00oo in iIIIiIi . lower ( ) :
    if iIIIiIi in OOoO0oO00o :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
     OOoO0oO00o . append ( iIIIiIi )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if iiiOOoo != 'Failed' :
  iiiiii1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iiiOOoo )
  for url , ooO0OO , iIIIiIi in iiiiii1 :
   if o0OO00oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , ooO0OO )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 66 - 66: i1i1I1IIii1II * iI11I1II1I1I % iI11I1II1I1I * III1iiIii - i1iIi - III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: i1IiiiI1iI + i1i1I1IIii1II
    if 93 - 93: i1IiiiI1iI + o0ii1I
    if 33 - 33: o0o00Oo0O
    if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
    if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % i1IiiiI1iI - iI11I1II1I1I % o0o00Oo0O
    if 58 - 58: III1iiIii + iI11I1II1I1I
    if 65 - 65: IIiIiII11i - i1IiiiI1iI % I11i - OOooOOo * IiI1i11I + o0ii1I
    if 79 - 79: i1iIi . OOooOOo % i1IiiiI1iI - I1ii11iIi11i
    if 69 - 69: i1iIi - I11i . i1iIi
    if 9 - 9: i1i1I1IIii1II % Ii / I1ii11iIi11i
    if 20 - 20: i1i1I1IIii1II * o0o00Oo0O + Iii - ii . Iii
    if 60 - 60: I11i . I11i / IiI1i11I
    if 45 - 45: o0o00Oo0O . Ii % IiI1i11I . OOooOOo % III1iiIii % iI11I1II1I1I
    if 58 - 58: iI11I1II1I1I . OOooOOo - Ii * iI11I1II1I1I % Ii / oOo0O0Ooo
    if 80 - 80: Ii1I / iI11I1II1I1I % OOooOOo
    if 80 - 80: oO0o % IiI1i11I
    if 99 - 99: i1iIi / iI11I1II1I1I - o0ii1I * Ii1I % oOo0O0Ooo
    if 13 - 13: oO0o
 if O0OoOOOo0Oo != 'Failed' :
  O0oo0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OoOOOo0Oo )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in O0oo0O0 :
   if o0OO00oo in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 2 - 2: ii . oooOo0oo0oo . III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 42 - 42: oooOo0oo0oo % i1i1I1IIii1II / oO0o - i1i1I1IIii1II * Ii
    if 19 - 19: i1i1I1IIii1II * oOo0O0Ooo % Ii
    if 24 - 24: I11i
    if 10 - 10: I11i % o0ii1I / oooOo0oo0oo
    if 28 - 28: oooOo0oo0oo % i1iIi
    if 48 - 48: Ii % i1i1I1IIii1II
    if 29 - 29: IiI1i11I + Ii % Iii
    if 93 - 93: OOooOOo % iI11I1II1I1I
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
 oo0O0o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 13 - 13: iI11I1II1I1I . OOooOOo * oOo0O0Ooo / i1i1I1IIii1II * o0ii1I
 for oO0ooOO in oo0O0o :
  IIi1iI1 = oO0 + oO0ooOO + oOoOooOo0o0
  i1iiIiI = O00O0oOO00O00 ( IIi1iI1 )
  if i1iiIiI != 'Failed' :
   I11Oo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iiIiI )
   for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in I11Oo0oO00 :
    if o0OO00oo in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 64 - 64: i1iIi / o0o00Oo0O * OOooOOo * i1iIi
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 60 - 60: Iii / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
 oo0O0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 99 - 99: OOooOOo
 if 77 - 77: I11i
 for oO0ooOO in oo0O0o :
  IIi1iI1 = OO0oOO0ooO + oO0ooOO
  IIiIi11iiIi = O00O0oOO00O00 ( IIi1iI1 )
  if IIiIi11iiIi != 'Failed' :
   i11iI11I1I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( IIiIi11iiIi )
   for o0oo00o0O0O00 , iIIIiIi in i11iI11I1I :
    if o0OO00oo in iIIIiIi . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO0oOO0ooO + oO0ooOO + o0oo00o0O0O00 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: o0ii1I % III1iiIii . o0o00Oo0O % i1IiiiI1iI
def ii11i ( ) :
 oOoo000 ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 oOoo000 ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 oOoo000 ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 oOoo000 ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / Iii . i1iIi / ooOoO0O00
def iI1i1iIi1iiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , OOo , o0OoO0000o , OOOooo0OooOoO , o0Ii1 in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + OOo + ' [COLORred]Returns [/COLOR]- ' + o0Ii1 + ' ' + OOOooo0OooOoO ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 50 - 50: i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oO0o + IIiIiII11i - o0o00Oo0O
def oOOOOoO00Ooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , OOo , o0OoO0000o in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + OOo + ' [COLORred] Status Unknown[/COLOR] ' ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 18 - 18: i1iIi + o0ii1I
def ii11i11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , OOo , o0OoO0000o , OOOooo0OooOoO in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + ' [COLORred] Cancelled On[/COLOR] ' + OOOooo0OooOoO ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 70 - 70: ooOoO0O00 . oOo0O0Ooo . IIiIiII11i . ii
def oOOOo ( url ) :
 o0OO00oo = ( url )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 if 31 - 31: OOooOOo + OOooOOo . Ii / i1iIi % Iii / OOooOOo
 if 29 - 29: Ii1I * Ii1I . oO0o * Iii % iI11I1II1I1I * Ii1I
 i1iii1ii = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o0OO00oo ) . replace ( ' ' , '+' )
 iIii1iI = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 Oo0O0O000 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1IIIIiii1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 31 - 31: oO0o * o0o00Oo0O . i1i1I1IIii1II
 III1I11i1iIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OO0oo0O0OOO0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 oooOO0oOooO00 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 37 - 37: III1iiIii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 37 - 37: I1ii11iIi11i / III1iiIii * o0o00Oo0O
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 73 - 73: IiI1i11I * IiI1i11I / i1iIi
 if 43 - 43: Ii1I . ooOoO0O00 . III1iiIii + o0o00Oo0O * o0ii1I * o0o00Oo0O
 oo0o = O00O0oOO00O00 ( i1iii1ii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iIii1iI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0O0O000 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( II1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 IIiIi11iiIi = O00O0oOO00O00 ( I1IIIIiii1i )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 41 - 41: Ii1I + o0ii1I % ii . Ii1I + IiI1i11I . IiI1i11I
 if 31 - 31: Ii + IIiIiII11i . IiI1i11I * OOooOOo
 ooOO = O00O0oOO00O00 ( III1I11i1iIi )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iiIiI = O00O0oOO00O00 ( OO0oo0O0OOO0 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 OO0ooo0 = O00O0oOO00O00 ( oooOO0oOooO00 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 7 - 7: Ii1I - i1i1I1IIii1II * oooOo0oo0oo + I11i . Ii1I
 if i1iiIiI != 'Failed' :
  I11Oo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iiIiI )
  for url , iIIIiIi in I11Oo0oO00 :
   IiiI1III1I1 = O00O0oOO00O00 ( url )
   o0OoOoo00O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiiI1III1I1 )
   for i1iii1ii , II1 in o0OoOoo00O :
    if i1i1IiIiIi1Ii in II1 . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + i1iii1ii , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 85 - 85: o0o00Oo0O
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if ooOO != 'Failed' :
  IiiIiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in IiiIiI1I1 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 19 - 19: o0ii1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
    if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
    if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
    if 8 - 8: OOooOOo * I1ii11iIi11i / III1iiIii % o0ii1I - oOo0O0Ooo
    if 71 - 71: IiI1i11I
    if 23 - 23: ooOoO0O00 . iI11I1II1I1I . oooOo0oo0oo . o0o00Oo0O % o0ii1I % Ii
    if 11 - 11: o0o00Oo0O - IIiIiII11i . oooOo0oo0oo . o0ii1I % i1IiiiI1iI
    if 21 - 21: I1ii11iIi11i / IiI1i11I . i1IiiiI1iI * ii + Iii - ooOoO0O00
    if 58 - 58: Ii1I
    if 2 - 2: IIiIiII11i / i1IiiiI1iI
    if 54 - 54: ooOoO0O00 . Iii - Ii1I + i1iIi + I1ii11iIi11i / I1ii11iIi11i
 if OO0ooo0 != 'Failed' :
  i1ii1IiiiiIi1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0ooo0 )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in i1ii1IiiiiIi1I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    oOoo000 ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , iiiI1I1iIIIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 56 - 56: ii * o0o00Oo0O
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oo0OoOOooO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , ooO0OO , iIIIiIi , o0o0OO0o00o0O in i1Iii1i1I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    if 'season' in o0o0OO0o00o0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in o0o0OO0o00o0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , ooO0OO , ooO0OO , '' )
  for url in oo0OoOOooO :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 28 - 28: oO0o - i1i1I1IIii1II + OOooOOo + o0ii1I / iI11I1II1I1I
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OoO00oo00 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for url , iIIIiIi , ooO0OO in OoO00oo00 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 68 - 68: oooOo0oo0oo + i1i1I1IIii1II . o0o00Oo0O . o0ii1I % ooOoO0O00 % oooOo0oo0oo
    if 50 - 50: III1iiIii + I11i
    if 96 - 96: oO0o
    if 92 - 92: I1ii11iIi11i / Ii + Ii1I
    if 87 - 87: OOooOOo % iI11I1II1I1I
    if 72 - 72: oooOo0oo0oo . oooOo0oo0oo - Ii1I
    if 48 - 48: I1ii11iIi11i - i1iIi + I1ii11iIi11i - oOo0O0Ooo * Ii . IiI1i11I
    if 35 - 35: III1iiIii . o0o00Oo0O + I1ii11iIi11i + oooOo0oo0oo + ooOoO0O00
    if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Oo0O0O000 + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( II1Ii + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 58 - 58: oooOo0oo0oo . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if IIiIi11iiIi != 'Failed' :
  i11iI11I1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiIi11iiIi )
  for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in i11iI11I1I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
 oOOoOOO0oo0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oO0ooOO in oOOoOOO0oo0 :
  IIi1iI1 = oO0 + oO0ooOO + oOoOooOo0o0
  O0OoOOOo0Oo = O00O0oOO00O00 ( IIi1iI1 )
  if O0OoOOOo0Oo != 'Failed' :
   O0oo0O0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OoOOOo0Oo )
   for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in O0oo0O0 :
    if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 87 - 87: i1iIi / OOooOOo % I11i * i1i1I1IIii1II
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 77 - 77: i1i1I1IIii1II - I1ii11iIi11i - iI11I1II1I1I
     if 16 - 16: oO0o / IiI1i11I / ooOoO0O00 . IiI1i11I + i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
def IiiIi11Ii1iI1 ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']YOLOselfies[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HotNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MyNudeBabes[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TeenNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADULTmeme[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GIRLSmeme[/COLOR]' , ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  oOo00o ( 'http://www.yoloselfie.com/' )
 if O0O00Oo == 1 :
  II111i1ii1iII ( 'http://www.hotnudegirls.net/#nudegirls' )
 if O0O00Oo == 2 :
  ooo0OoO ( 'http://www.teennudegirls.com/' )
 if O0O00Oo == 3 :
  ooo0OoO ( 'http://www.teennudegirls.com/' )
 if O0O00Oo == 4 :
  iiI1111I11i1I ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if O0O00Oo == 5 :
  iiI1111I11i1I ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 85 - 85: oooOo0oo0oo * ooOoO0O00 % oOo0O0Ooo - i1iIi
def oOo00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 100111 , ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 100110 , ooO0OO )
def I11I1ii1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  II11Ii111II1 = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( II11Ii111II1 )
  sys . exit ( 1 )
def iiI1111I11i1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + ooO0OO , 100113 , 'http:' + ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http:' + url , 100112 , ooO0OO )
def II111i1ii1iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , ooO0OO )
def O00OOO00Ooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , ooO0OO , 100113 , ooO0OO )
def OoOOoooO000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , ooO0OO )
def OoO0o000oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , ooO0OO , 100113 , ooO0OO )
def ooo0OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , ooO0OO )
def Oo00OO00o0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , ooO0OO , 100113 , ooO0OO )
def iI1 ( url ) :
 II11Ii111II1 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( II11Ii111II1 )
 sys . exit ( 1 )
 if 12 - 12: i1IiiiI1iI + oooOo0oo0oo + Iii . III1iiIii / o0ii1I
def i1I ( ) :
 if 100 - 100: oO0o % oO0o
 if 15 - 15: i1i1I1IIii1II / i1IiiiI1iI
 if 37 - 37: Ii + oOo0O0Ooo . oooOo0oo0oo % Iii % Iii
 if 26 - 26: o0o00Oo0O
 if 34 - 34: i1iIi * i1IiiiI1iI
 if 97 - 97: Ii % i1i1I1IIii1II / I1ii11iIi11i / I1ii11iIi11i
 if 97 - 97: IIiIiII11i - i1IiiiI1iI - iI11I1II1I1I * oOo0O0Ooo
 if 54 - 54: iI11I1II1I1I
 if 5 - 5: III1iiIii
 if 84 - 84: IIiIiII11i * i1i1I1IIii1II * IIiIiII11i % III1iiIii / oOo0O0Ooo
 if 100 - 100: III1iiIii . o0ii1I - iI11I1II1I1I . Ii / IIiIiII11i
 oOoo000 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 oOoo000 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 71 - 71: i1IiiiI1iI * I1ii11iIi11i . Iii
def i1ii1iiIi1II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , OOo000o0 in IIi :
  oOoo000 ( ( iIIIiIi + ' - ' + OOo000o0 ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 69 - 69: i1iIi - ii * o0o00Oo0O
def O0Oo0O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 33 - 33: i1iIi % ooOoO0O00 - i1i1I1IIii1II . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  oOoo000 ( iIIIiIi , url , 90054 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 17 - 17: o0ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % oooOo0oo0oo
def III1III11II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , OOo000o0 , url , iIIIiIi , iIi1iI in IIi :
  I1I1II1I11 ( OOo000o0 + ' - ' + iIIIiIi + ' - ' + iIi1iI , url , 90044 , ooO0OO , ooO0OO , '' )
 for ooO0OO , iIIIiIi , url in i1Iii1i1I :
  oOoo000 ( iIIIiIi , url , 90044 , ooO0OO , ooO0OO , '' )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . i1IiiiI1iI
def Ooooo ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 II11iIiIIIiI = OooOoooOo ( i1i1IiIiIi1Ii )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , o0o0OO0o00o0O in IIi :
  if 'season' in o0o0OO0o00o0O :
   oOoo000 ( iIIIiIi , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
  if 'episodes' in o0o0OO0o00o0O :
   oOoo000 ( iIIIiIi , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
 for oOOo0O00o in next :
  oOoo000 ( 'NEXT' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
  if 19 - 19: III1iiIii . Ii1I / OOooOOo
def O00oo ( ) :
 if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
 if 70 - 70: i1i1I1IIii1II * i1i1I1IIii1II + I1ii11iIi11i * oooOo0oo0oo % oOo0O0Ooo + iI11I1II1I1I
 if 2 - 2: Ii
 if 98 - 98: i1i1I1IIii1II / oO0o - o0ii1I - oOo0O0Ooo / OOooOOo + Ii
 if 17 - 17: Iii
 if 97 - 97: Ii1I * Ii1I / IiI1i11I
 if 6 - 6: i1i1I1IIii1II
 if 72 - 72: Iii * Ii1I - OOooOOo / Ii1I + oooOo0oo0oo - IiI1i11I
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + i1IiiiI1iI
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * i1i1I1IIii1II
 oOoo000 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 oOoo000 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 oOoo000 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
def OOo00ooOoO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , OOo000o0 in IIi :
  if 'genre' in url :
   oOoo000 ( ( iIIIiIi + ' - ' + OOo000o0 ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 21 - 21: Ii
def o00iIiiiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'release' in url :
   oOoo000 ( iIIIiIi , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 5 - 5: ii / I11i % Iii % oO0o * IiI1i11I + iI11I1II1I1I
def I11iiI11iiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , OOOII1i1II , url , O000OOO in IIi :
  I1I1II1I11 ( iIIIiIi + ' ' + OOOII1i1II , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for ooO0OO , iIIIiIi , o0o0OO0o00o0O , url , iIIi1Ii1III , O000OOO in i1Iii1i1I :
  if 'movies' in o0o0OO0o00o0O :
   I1I1II1I11 ( iIIIiIi + ' - ' + iIIi1Ii1III , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 86 - 86: Ii + Ii . i1IiiiI1iI % oOo0O0Ooo . i1iIi
def iII1iI1IIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O00ooOOoO0O000O ( 'http:' + url )
  if 20 - 20: oOo0O0Ooo . Iii
def O00ooOOoO0O000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def oooOO0oo0Oo00 ( ) :
 if 99 - 99: o0o00Oo0O
 if 38 - 38: Ii + iI11I1II1I1I - Iii / OOooOOo
 if 99 - 99: Ii1I * i1i1I1IIii1II * Ii1I - IIiIiII11i + o0ii1I
 if 72 - 72: I11i % oOo0O0Ooo / IiI1i11I - o0o00Oo0O + Iii
 if 83 - 83: o0o00Oo0O
 if 89 - 89: I1ii11iIi11i + Ii1I - I11i
 if 40 - 40: oO0o + oO0o
 if 94 - 94: IiI1i11I * iI11I1II1I1I . Iii
 if 13 - 13: iI11I1II1I1I * OOooOOo / i1IiiiI1iI % i1iIi + i1i1I1IIii1II
 if 41 - 41: Ii1I
 if 5 - 5: I1ii11iIi11i
 if 100 - 100: o0ii1I + iI11I1II1I1I
 if 59 - 59: III1iiIii
 if 89 - 89: OOooOOo % iI11I1II1I1I
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 II11iIiIIIiI = OooOoooOo ( i1i1IiIiIi1Ii )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , III11I1 in IIi :
  if 'movies' in III11I1 :
   oOoo000 ( III11I1 + '-' + iIIIiIi , oOOo0O00o , 90044 , ooO0OO )
 for oOOo0O00o in next :
  I11iiI11iiI ( oOOo0O00o )
  if 61 - 61: OOooOOo - oO0o + oOo0O0Ooo * oooOo0oo0oo % oO0o
def III1i11 ( ) :
 oOoo000 ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 80006 , iiIi1IIiIi + 'Desi.png' )
def i111I11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( iIIIiIi , url , 80007 , ooO0OO )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def OoOoOOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  I11iiiiI1i ( url )
def ii1ii1i11I1I ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'http://www.join4films.com/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 i111I11I ( i1i1IiIiIi1Ii )
 if 41 - 41: III1iiIii
 if 3 - 3: III1iiIii + IIiIiII11i / iI11I1II1I1I
 if 10 - 10: IIiIiII11i . o0o00Oo0O
 if 31 - 31: i1i1I1IIii1II / Ii / o0o00Oo0O
 if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
 if 83 - 83: ooOoO0O00
 if 76 - 76: o0ii1I + iI11I1II1I1I + OOooOOo . oO0o
 if 49 - 49: III1iiIii / i1iIi / oooOo0oo0oo
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - i1iIi
 if 38 - 38: I11i % i1IiiiI1iI + Ii + IiI1i11I + i1iIi / Ii
 if 94 - 94: IiI1i11I - I1ii11iIi11i + i1i1I1IIii1II
 if 59 - 59: Iii . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 if 56 - 56: i1i1I1IIii1II + i1iIi
 if 32 - 32: IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
 if 2 - 2: Ii - i1IiiiI1iI + oO0o % Iii * o0ii1I
 if 54 - 54: o0o00Oo0O - IiI1i11I . oooOo0oo0oo % IiI1i11I + IiI1i11I
 if 36 - 36: oooOo0oo0oo % Ii
def Iiii1Ii ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 62 - 62: ooOoO0O00 % OOooOOo
def i1ii1I1IIIII ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'http://imoviemax.se/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 OoiiI1i111 ( i1i1IiIiIi1Ii )
def oO0O0o0O ( url ) :
 oOO00ooOOo = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii11Iiii in IIi :
  if iIIIiIi in oOO00ooOOo :
   pass
  else :
   I1I1II1I11 ( iIIIiIi + ' - ' + ii11Iiii + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   oOO00ooOOo . append ( iIIIiIi )
   if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
def iiI111OOoooo0oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , oOo0O in IIi :
  I1I1II1I11 ( iIIIiIi + ' - Views:' + oOo0O , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 30 - 30: o0ii1I . Ii1I / oooOo0oo0oo
  if 2 - 2: III1iiIii % oOo0O0Ooo - i1IiiiI1iI
def OoiiI1i111 ( url ) :
 oooOo = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10075 , ooO0OO , ooO0OO , '' )
  oooOo . append ( iIIIiIi )
  if 79 - 79: i1i1I1IIii1II - IIiIiII11i
def Ii1iiI1 ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for o0ooOOoO0oO0 , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oo00I1IiI1IIiI = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oo00I1IiI1IIiI
  oooo = ( o0ooOOoO0oO0 ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( oooo , oo00I1IiI1IIiI , 10076 , img , img , '' )
  if 63 - 63: i1iIi % oOo0O0Ooo
def o0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for iIii1iI in IIi :
  if '=m' in iIii1iI :
   iiI1i ( iIii1iI )
  elif 'php' in iIii1iI :
   o0Oo ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( iIii1iI )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for Oo0O0O000 in IIi :
    iiI1i ( iIii1iI )
    if 3 - 3: III1iiIii / Iii
    if 34 - 34: Ii / i1IiiiI1iI * oooOo0oo0oo . I1ii11iIi11i
    if 79 - 79: i1IiiiI1iI
def iI11111ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iI1iiI = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOooo0OooOoO , Iii11111iiI in iI1iiI :
  print 'there ><><><><><><><><><><><><'
  OOOooo0OooOoO = OOOooo0OooOoO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Iii11111iiI ) )
  for iIIIiIi , o0OOOOoO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + OOOooo0OooOoO + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + o0OOOOoO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 i1i1i1I = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOooo0OooOoO , OoO0Ooo in i1i1i1I :
  print 'there ><><><><><><><><><><><><'
  OOOooo0OooOoO = OOOooo0OooOoO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OoO0Ooo ) )
  for iIIIiIi , o0OOOOoO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + OOOooo0OooOoO + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + o0OOOOoO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 21 - 21: oOo0O0Ooo + Ii1I * I1ii11iIi11i * iI11I1II1I1I - oO0o . I1ii11iIi11i
   if 59 - 59: oO0o - oO0o + IiI1i11I
   if 32 - 32: ooOoO0O00 / I1ii11iIi11i - o0o00Oo0O
def O00oO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for iIIIiIi in iIIIiIi :
   iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for o000O000 in o000O000 :
   o000O000 = 'http:' + o000O000
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , '' , '' )
  if 85 - 85: o0ii1I - o0o00Oo0O * Ii . ooOoO0O00
  if 20 - 20: IiI1i11I / oooOo0oo0oo
  if 28 - 28: i1iIi * Iii % Ii * IiI1i11I / o0ii1I
  if 41 - 41: oooOo0oo0oo - I11i + o0ii1I
def iiI111 ( url ) :
 if 15 - 15: Iii / I11i + o0ii1I
 O0oo00o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIii1iI , ooO0OO , iIIIiIi , IIi1i1 in IIi :
  iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( iIii1iI )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for oo0OoOooo , OoO000O in i1Iii1i1I :
   o0O0Ooo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OoO000O ) )
   for O000OOO in o0O0Ooo :
    if iIIIiIi in O0oo00o :
     pass
    else :
     Ii1I1i ( iIIIiIi , oo0OoOooo , 8043 , ooO0OO , ooO0OO , O000OOO )
     I1iI1ii1II ( 'movies' , 'INFO' )
     O0oo00o . append ( iIIIiIi )
     if 79 - 79: i1iIi . i1i1I1IIii1II / i1i1I1IIii1II - i1iIi * I1ii11iIi11i / I11i
     if 19 - 19: Ii1I
def IiIIii1iiI ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10065 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 7 - 7: I11i
def IiiIIi ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'https://www.youtube.com/results?search_query=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 II11iIiIIIiI = OooOoooOo ( i1i1IiIiIi1Ii )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in next :
  oOOo0O00o = 'https://www.youtube.com' + oOOo0O00o
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , oOOo0O00o , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , oOOo0O00o , iIIIiIi , OoOo0OO0oooo , OoO000O in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o000O000
  oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
  Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , OoO000O )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , oOOo0O00o , iIIIiIi , OoOo0OO0oooo in IIi :
   print 'im doing it'
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
   if '&' in oOOo0O00o :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOOo0O00o = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for oOOo0O00o in oOOo0O00o :
      oOOo0O00o = 'https://www.youtube.com/w' + oOOo0O00o
     o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for o000O000 in o000O000 :
      o000O000 = 'http:' + o000O000
     Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in oOOo0O00o or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in oOOo0O00o :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOOo0O00o
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    I11II1i1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , oOOo0O00o , iIIIiIi in I11II1i1 :
     if 'outube' in oOOo0O00o or 'list' in oOOo0O00o :
      pass
     elif 'atch' in oOOo0O00o :
      oOOo0O00o = ( oOOo0O00o ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , '' )
    if 46 - 46: IIiIiII11i % IiI1i11I - ooOoO0O00 / Iii * OOooOOo
def oO0o0oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , url , iIIIiIi , OoOo0OO0oooo , OoO000O in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o000O000
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , OoO000O )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , url , iIIIiIi , OoOo0OO0oooo in IIi :
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for o000O000 in o000O000 :
      o000O000 = 'http:' + o000O000
     Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in url or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    I11II1i1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , url , iIIIiIi in I11II1i1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + OoOo0OO0oooo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , '' )
    if 92 - 92: ooOoO0O00 % i1iIi + i1iIi - iI11I1II1I1I . o0ii1I
    if 33 - 33: I11i / o0o00Oo0O + oooOo0oo0oo
    if 75 - 75: III1iiIii % Ii + iI11I1II1I1I
def oOoOo0o00o ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 2 - 2: IIiIiII11i
def o0ooo0o0 ( ) :
 ivuesetup . iVueInt ( )
 if 84 - 84: Iii - I1ii11iIi11i * o0o00Oo0O / o0ii1I . o0ii1I
def ooO0 ( ) :
 ii111iiIii ( )
 return
 if 57 - 57: I11i / i1IiiiI1iI
def ii111iiIii ( ) :
 if 13 - 13: ii + oO0o
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 ii1IIii = II1I . getSetting ( id = 'User' )
 IiI11i1I11111 = II1I . getSetting ( id = 'Pass' )
 Ii1IIIIIIiI1 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Ii11IiIiiii1 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 OooO0O0Ooo = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 oO0OIIIiIi1iiI = "http://piesustv.net:8000/get.php?username=" + ii1IIii + "&password=" + IiI11i1I11111 + "&type=m3u_plus&output=ts"
 iI1o0 = "http://piesustv.net:8000/xmltv.php?username=" + ii1IIii + "&password=" + IiI11i1I11111 + "&type=m3u_plus&output=ts"
 if 32 - 32: ii / IIiIiII11i / i1i1I1IIii1II + o0ii1I / o0o00Oo0O
 xbmc . executeJSONRPC ( Ii1IIIIIIiI1 )
 xbmc . executeJSONRPC ( Ii11IiIiiii1 )
 xbmc . executeJSONRPC ( OooO0O0Ooo )
 if 98 - 98: oO0o / Iii - o0ii1I
 OOOOo0oOOOOooOo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 OOOOo0oOOOOooOo . setSetting ( id = 'm3uUrl' , value = oO0OIIIiIi1iiI )
 OOOOo0oOOOOooOo . setSetting ( id = 'epgUrl' , value = iI1o0 )
 OOOOo0oOOOOooOo . setSetting ( id = 'm3uCache' , value = "false" )
 OOOOo0oOOOOooOo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def i1I111II ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
if 26 - 26: I11i % oooOo0oo0oo + oooOo0oo0oo % Iii * Ii / IiI1i11I
if 64 - 64: i1i1I1IIii1II % OOooOOo / IIiIiII11i % i1iIi - IiI1i11I
def I1II1IiI1 ( ) :
 if 26 - 26: oooOo0oo0oo * I1ii11iIi11i
 if 31 - 31: Iii * i1i1I1IIii1II . o0ii1I
 if 35 - 35: Iii
 if 94 - 94: i1iIi / Ii % o0o00Oo0O
 if 70 - 70: Iii - I1ii11iIi11i / ii % ii
 if 95 - 95: ii % ii . o0ii1I
 if 26 - 26: i1i1I1IIii1II + III1iiIii - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
 if 68 - 68: o0o00Oo0O
 if 76 - 76: Ii1I
 if 99 - 99: I11i
 if 1 - 1: o0ii1I * OOooOOo * oO0o + I1ii11iIi11i
 if 90 - 90: i1IiiiI1iI % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / oooOo0oo0oo + Iii
 if OO0o == "insert_username" :
  o0o00OOOO = i11iIi1iIIIIi ( )
  I1111iiiII1Ii = oO0oOoOoo0 ( )
  I11 ( 'User' , o0o00OOOO )
  I11 ( 'Pass' , I1111iiiII1Ii )
  xbmc . executebuiltin ( 'Container.Refresh' )
  o0o000o = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( o0o00OOOO , I1111iiiII1Ii )
  o0o000o = OooOoooOo ( o0o000o )
  if o0o000o == "" :
   iiiI1i1111II = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   IIII11iiii = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   OoO00OooO0 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , iiiI1i1111II , IIII11iiii , OoO00OooO0 )
   I1II1IiI1 ( )
  else :
   iiiI1i1111II = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   IIII11iiii = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   OoO00OooO0 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % o0o00OOOO )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , iiiI1i1111II , IIII11iiii , OoO00OooO0 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   o00OOo ( )
 else :
  o00OOo ( )
def i11iIi1iIIIIi ( ) :
 Ii11III = xbmc . Keyboard ( '' , 'heading' , True )
 Ii11III . setHeading ( 'Enter Username' )
 Ii11III . setHiddenInput ( False )
 Ii11III . doModal ( )
 if ( Ii11III . isConfirmed ( ) ) :
  I1Ii1i11I1I = Ii11III . getText ( )
  return I1Ii1i11I1I
 else :
  return False
  if 71 - 71: oOo0O0Ooo * ooOoO0O00 % Iii
  if 82 - 82: III1iiIii . OOooOOo / i1iIi + IiI1i11I - i1iIi
def oO0oOoOoo0 ( ) :
 Ii11III = xbmc . Keyboard ( '' , 'heading' , True )
 Ii11III . setHeading ( 'Enter Password' )
 Ii11III . setHiddenInput ( False )
 Ii11III . doModal ( )
 if ( Ii11III . isConfirmed ( ) ) :
  I1Ii1i11I1I = Ii11III . getText ( )
  return I1Ii1i11I1I
 else :
  return False
def o00OOo0o0O ( ) :
 oO0OIIIiIi1iiI = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  I111Iii1 = urllib2 . urlopen ( oO0OIIIiIi1iiI )
  print I111Iii1 . getcode ( )
  I111Iii1 . close ( )
  if 30 - 30: ooOoO0O00
  pass
  if 75 - 75: Iii . oooOo0oo0oo - iI11I1II1I1I * oO0o * IiI1i11I
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def o00OOo ( ) :
 iii ( )
 if 93 - 93: i1iIi
 if 18 - 18: i1iIi
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 66 - 66: i1i1I1IIii1II * Ii + OOooOOo / oooOo0oo0oo
 if 96 - 96: oooOo0oo0oo + oooOo0oo0oo % III1iiIii % oooOo0oo0oo
 if 28 - 28: iI11I1II1I1I + OOooOOo . I11i % Ii
 if 58 - 58: Iii / ii % i1i1I1IIii1II + oO0o
def o0ooOO0OOO00o ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 oOO = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 OoOoO0ooooO0 = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 o0o000o = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 o0o000o = OooOoooOo ( o0o000o )
 if not o0o000o == "" :
  IIII1ii1 = 'https://tinyurl.com/create.php?source=indexpage&url=' + oOO + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( IIII1ii1 ) )
  OOO0O0OOo = 'https://tinyurl.com/create.php?source=indexpage&url=' + OoOoO0ooooO0 + '&submit=Make+TinyURL%21&alias='
  oOO = OooOoooOo ( IIII1ii1 )
  OoOoO0ooooO0 = OooOoooOo ( OOO0O0OOo )
  xbmc . log ( str ( OoOoO0ooooO0 ) )
  Iii1 = OOoO ( oOO , '<div class="indent"><b>' , '</b>' )
  i1IiiI = OOoO ( OoOoO0ooooO0 , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % Iii1 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % i1IiiI )
 else :
  return
def O0OOO0 ( ) :
 o00OOo0o0O ( )
 o0OIi ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIi1iiI + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( o0ooOO00OO0o0O )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOOo0O00o , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def III1IiiIiiI1i ( url ) :
 open = OooOoooOo ( OoO0o00OoO + url )
 Oo00Oooo00o = II11II1I ( open , '<channel>' , '</channel>' )
 for O0OO00000o00 in Oo00Oooo00o :
  if '<playlist_url>' in open :
   iIIIiIi = OOoO ( O0OO00000o00 , '<title>' , '</title>' )
   i1iii1ii = OOoO ( O0OO00000o00 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( iIIIiIi ) ) . replace ( '?' , '' ) , i1iii1ii , 3 , icon , IIo0o0O0O00oOOo , '' )
  else :
   iIIIiIi = OOoO ( O0OO00000o00 , '<title>' , '</title>' )
   iIIIiIi = base64 . b64decode ( iIIIiIi )
   OOO000Oo = OOoO ( O0OO00000o00 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = OOoO ( O0OO00000o00 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   O000OOO = OOoO ( O0OO00000o00 , '<description>' , '</description>' )
   O000OOO = base64 . b64decode ( O000OOO )
   I1IIIi1i = OOoO ( O000OOO , 'PLOT:' , '\n' )
   OooIii1I1iI = OOoO ( O000OOO , 'CAST:' , '\n' )
   oOoOo0 = OOoO ( O000OOO , 'RATING:' , '\n' )
   iIi = OOoO ( O000OOO , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   iIi = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( iIi )
   oOoooOo0o = OOoO ( O000OOO , 'DURATION_SECS:' , '\n' )
   III = OOoO ( O000OOO , 'GENRE:' , '\n' )
   IiiI ( str ( iIIIiIi ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , OOO000Oo , IIo0o0O0O00oOOo , I1IIIi1i , str ( iIi ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( OooIii1I1iI ) . split ( ) , oOoOo0 , oOoooOo0o , III )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 75 - 75: ii . oooOo0oo0oo + oO0o / o0ii1I - oOo0O0Ooo % o0ii1I
O0OooooO0o0O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
oO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 52 - 52: III1iiIii % i1iIi
def I111 ( ) :
 oO0OIIIiIi1iiI = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  I111Iii1 = urllib2 . urlopen ( oO0OIIIiIi1iiI )
  print I111Iii1 . getcode ( )
  I111Iii1 . close ( )
  if 51 - 51: Ii1I * i1i1I1IIii1II
  pass
  if 23 - 23: Ii
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 100 - 100: i1i1I1IIii1II + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
 oOOo0O00o = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 ooOOo ( oOOo0O00o , oO0oo + "uide.xml" )
 if 5 - 5: o0o00Oo0O
 O0oO0 = open ( O0OooooO0o0O0 , 'r+' )
 input = open ( O0OooooO0o0O0 ) . read ( ) . decode ( 'UTF-8' )
 o0oo0Oo = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 O0oO0 . write ( o0oo0Oo )
 O0oO0 . truncate ( )
 O0oO0 . close ( )
 i1i1I1II ( )
 if 66 - 66: III1iiIii + iI11I1II1I1I
def i1i1I1II ( ) :
 open = OooOoooOo ( o0Oo00oOO )
 all = II11II1I ( open , '{"num' , 'direct' )
 for O0OO00000o00 in all :
  if '"tv_archive":1' in O0OO00000o00 :
   iIIIiIi = OOoO ( O0OO00000o00 , '"epg_channel_id":"' , '"' )
   OOO000Oo = OOoO ( O0OO00000o00 , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = OOoO ( O0OO00000o00 , 'stream_id":"' , '"' )
   iIIIiIi = iIIIiIi . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( iIIIiIi , id , 90027 , OOO000Oo , IIo0o0O0O00oOOo , iIIIiIi )
   if 73 - 73: Iii / ii . IIiIiII11i - III1iiIii * i1iIi * III1iiIii
   if 45 - 45: o0o00Oo0O * i1IiiiI1iI + Ii - oooOo0oo0oo - iI11I1II1I1I
def I11I111i1I1 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 iii1 = open ( O0OooooO0o0O0 )
 O0Ooo0O = ElementTree . parse ( iii1 )
 iii1oOo0OoOOOo0 = "apples"
 import datetime as dt
 from datetime import time
 OOoo00 = datetime . now ( ) - timedelta ( days = 5 )
 OOOooo0OooOoO = str ( OOoo00 )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 I1I1 = O0Ooo0O . findall ( "programme" )
 for O0OOO0ooO00o in I1I1 :
  if name in O0OOO0ooO00o . attrib . get ( 'channel' ) :
   I1iii1 = O0OOO0ooO00o . attrib . get ( 'start' )
   iIiiiIIiii , OO0 , Oo00Oo = I1iii1 . partition ( ' +' )
   OOOooo0OooOoO = str ( OOOooo0OooOoO ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   iIi , iIiO0O , o0Ii1 = I1iii1 . partition ( '2017' )
   oOOoooo = O0OOO0ooO00o . find ( 'title' ) . text + I1iii1
   o0Ii1 = o0Ii1 [ : - 6 ]
   if iIiiiIIiii > OOOooo0OooOoO :
    if iIiiiIIiii < I1IIIii :
     O0o = iIiiiIIiii
     O0o = O0o [ : 4 ] + '/' + O0o [ 4 : ]
     iIiiiIIiii = iIiiiIIiii [ : 4 ] + '-' + iIiiiIIiii [ 4 : ]
     O0o = O0o [ : 7 ] + '/' + O0o [ 7 : ]
     iIiiiIIiii = iIiiiIIiii [ : 7 ] + '-' + iIiiiIIiii [ 7 : ]
     O0o = O0o [ : 10 ] + ' - ' + O0o [ 10 : ]
     iIiiiIIiii = iIiiiIIiii [ : 10 ] + ':' + iIiiiIIiii [ 10 : ]
     O0o = O0o [ : 15 ] + ':' + O0o [ 15 : ]
     iIiiiIIiii = iIiiiIIiii [ : 13 ] + '-' + iIiiiIIiii [ 13 : ]
     O0o = O0o [ : - 2 ]
     iIiiiIIiii = iIiiiIIiii [ : - 2 ]
     Ii1iIiIi1I11 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( iIiiiIIiii ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     iii1oOo0OoOOOo0 = Ii1iIiIi1I11 + str ( iIiiiIIiii ) + "&duration=240"
     O0o = '[COLOR blue]%s - [/COLOR]' % O0o
     oOOoooo = str ( O0o ) + O0OOO0ooO00o . find ( 'title' ) . text
     O000OOO = O0OOO0ooO00o . find ( 'desc' ) . text
     Ii1I1i ( oOOoooo , Ii1iIiIi1I11 , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , O000OOO )
def ii1I11 ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 i1i1II1i11 = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 i1i1II1i11 . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 i1i1II1i11 . setProperty ( 'IsPlayable' , 'true' )
 i1i1II1i11 . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i1II1i11 )
def ooOOo ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 OOO0 = time . time ( )
 urllib . urlretrieve ( url , dest , lambda I1Ii1 , O0oo0oOoO00 , i1ii1iIi : I1I1Ii ( I1Ii1 , O0oo0oOoO00 , i1ii1iIi , o0oOoO00o , OOO0 ) )
def I1I1Ii ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  iI1IIII1 = min ( numblocks * blocksize * 100 / filesize , 100 )
  Oo0o = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  OoO000oo000o0 = numblocks * blocksize / ( time . time ( ) - start_time )
  if OoO000oo000o0 > 0 :
   i1Ii1I1Ii11iI = ( filesize - numblocks * blocksize ) / OoO000oo000o0
  else :
   i1Ii1I1Ii11iI = 0
  OoO000oo000o0 = OoO000oo000o0 / 1024
  i1ii111i = OoO000oo000o0 / 1024
  i1ii1i1Ii11 = float ( filesize ) / ( 1024 * 1024 )
  O0O0Oo0O0oo = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( Oo0o )
  Ooo0O0oooo = '[COLOR white]Speed:  %.02f Mb/s ' % i1ii111i + '[/COLOR]'
  dp . update ( iI1IIII1 , O0O0Oo0O0oo , Ooo0O0oooo )
 except :
  iI1IIII1 = 100
  dp . update ( iI1IIII1 )
 if dp . iscanceled ( ) :
  o0O0 = xbmcgui . Dialog ( )
  o0O0 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 82 - 82: i1i1I1IIii1II / ii % IiI1i11I
  sys . exit ( )
  dp . close ( )
  if 65 - 65: o0o00Oo0O . i1i1I1IIii1II
def oOoO0 ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  Iii1II1ii ( )
  if 95 - 95: I1ii11iIi11i
  if 29 - 29: o0ii1I / i1iIi % Iii
  if 10 - 10: iI11I1II1I1I % ii % Ii1I
  if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * Iii
  if 89 - 89: o0ii1I - i1iIi . Iii - i1IiiiI1iI - oOo0O0Ooo
  if 79 - 79: III1iiIii + III1iiIii + o0ii1I
  if 39 - 39: o0o00Oo0O - ii
  if 63 - 63: iI11I1II1I1I % I11i * i1iIi
def Iii1II1ii ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def oo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iii1iI = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OoO00oo00 = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 ii1I1IIii11 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 II1i11I = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 Oo0Oo0O = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i11iI11I1I = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 iiiiii1 = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 IiiIi1I11 = i1I1Ii11II1i ( )
 oooOoOOoOO0O = I11iii1I1Iiii ( )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iii1iI :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OoO00oo00 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in II1i11I :
  dt = datetime . fromtimestamp ( float ( II1i11I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   OooOo00o ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in ii1I1IIii11 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Oo0Oo0O :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i11iI11I1I :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iiiiii1 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + IiiIi1I11 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + oooOoOOoOO0O , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 48 - 48: III1iiIii
def OOooO ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 II1i1i1I1iII ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 48 - 48: oooOo0oo0oo . oooOo0oo0oo + Ii + Ii1I % o0o00Oo0O
def O0000 ( data ) :
 ii1i1II = len ( data ) % 4
 if 1 - 1: iI11I1II1I1I % i1iIi + o0o00Oo0O
 if 22 - 22: I11i + I1ii11iIi11i . i1iIi + Ii1I * IiI1i11I . Ii
 if 90 - 90: oooOo0oo0oo * OOooOOo - I1ii11iIi11i + I11i
 if 53 - 53: ii . ii + I11i - IiI1i11I + oooOo0oo0oo
 if 44 - 44: i1IiiiI1iI - III1iiIii
 if 100 - 100: i1i1I1IIii1II . oO0o - o0ii1I + o0o00Oo0O * oO0o
 if ii1i1II != 0 :
  data += b'=' * ( 4 - ii1i1II )
 return base64 . decodestring ( data )
def OOoO ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : oOoOO = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : oOoOO = ''
 else :
  try : oOoOO = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : oOoOO = ''
 return oOoOO
 if 20 - 20: i1iIi . oO0o * IiI1i11I
 if 71 - 71: I1ii11iIi11i . IIiIiII11i / IIiIiII11i * o0ii1I * oO0o
def II11II1I ( text , start_with , end_with ) :
 oOoOO = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return oOoOO
def i1I1Ii11II1i ( ) :
 IiiI11 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 IiiI11 . connect ( ( '8.8.8.8' , 0 ) )
 IiiI11 = IiiI11 . getsockname ( ) [ 0 ]
 return IiiI11
 if 60 - 60: i1iIi * i1iIi / ii
def I11iii1I1Iiii ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 IiiIi1I11 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( IiiIi1I11 . group ( ) )
IIi1iiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
o0Oo00oOO = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
OOoO0o0OOo0 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
O0OoO0ooOOO = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
IiI1iIIIi1iIi = '&action=get_live_categories'
OOo0OOOoOOo = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
o0ooOO00OO0o0O = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 29 - 29: OOooOOo . IiI1i11I + OOooOOo + o0o00Oo0O . o0o00Oo0O * oooOo0oo0oo
OoO0o00OoO = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
i1iiiIIi11II = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
o0oooOo0oo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
i1iI1IIi1I = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 52 - 52: ii / III1iiIii % IIiIiII11i
def Ii11I1I11II ( ) :
 o00OOo0o0O ( )
 open = OooOoooOo ( o0oooOo0oo )
 Oo00Oooo00o = II11II1I ( open , '<channel>' , '</channel>' )
 for O0OO00000o00 in Oo00Oooo00o :
  iIIIiIi = OOoO ( O0OO00000o00 , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  i1iii1ii = OOoO ( O0OO00000o00 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' , i1iii1ii , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 43 - 43: i1i1I1IIii1II + ii . I11i . Ii1I
def I1Iiii1Ii ( url ) :
 open = OooOoooOo ( i1iI1IIi1I + url )
 Oo00Oooo00o = II11II1I ( open , '<channel>' , '</channel>' )
 for O0OO00000o00 in Oo00Oooo00o :
  iIIIiIi = OOoO ( O0OO00000o00 , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  xbmc . log ( str ( iIIIiIi ) )
  OOO000Oo = OOoO ( O0OO00000o00 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  i1iii1ii = OOoO ( O0OO00000o00 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  O000OOO = OOoO ( O0OO00000o00 , '<description>' , '</description>' )
  O000OOO = base64 . b64decode ( O000OOO )
  oooooO00OOO = '('
  oO00o = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , i1iii1ii , 222 , OOO000Oo , IIo0o0O0O00oOOo , ( '[COLOR' + ooOoOoo0O + ']' + O000OOO + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oO00o , '[COLORsteelblue]' ) . replace ( oooooO00OOO , '[COLORorangered]' ) )
  if 90 - 90: oOo0O0Ooo % ii / IiI1i11I
def IiiiIIi ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( OOo0OOOoOOo + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , type , iIii1iI , iiiI1i11Ii in IIi :
  Oo0O0O000 = ( O0OoO0ooOOO + iIii1iI + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , Oo0O0O000 , 222 , ( iiiI1i11Ii ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def O0o0O00oOoo00 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1 , IIiII1 in IIi :
  if name == II1 :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + IIiII1 , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def IiIIiiiii1Iii ( name ) :
 o000o0o0ooO0 = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , ooO0OO , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOOo0O00o ) . strip ( ) , 222 , ooO0OO , ooO0OO , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 27 - 27: OOooOOo . iI11I1II1I1I
  if 87 - 87: i1iIi * oO0o + I11i . oooOo0oo0oo - i1iIi
  if 33 - 33: IIiIiII11i / o0o00Oo0O / III1iiIii - Iii - ooOoO0O00
  if 8 - 8: Ii . IiI1i11I / iI11I1II1I1I / Ii1I / III1iiIii - o0ii1I
  if 32 - 32: I11i . ooOoO0O00 * I1ii11iIi11i
  if 98 - 98: o0ii1I - IIiIiII11i / oOo0O0Ooo . i1i1I1IIii1II * III1iiIii . Iii
  if 25 - 25: Ii / OOooOOo - i1IiiiI1iI / oO0o . I11i . I11i
  if 6 - 6: i1i1I1IIii1II . Iii
  if 43 - 43: Ii1I + I11i
  if 50 - 50: i1i1I1IIii1II % ooOoO0O00 * o0o00Oo0O
  if 4 - 4: iI11I1II1I1I . ooOoO0O00
  if 63 - 63: iI11I1II1I1I + III1iiIii % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def o00o0 ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , oOOo0O00o , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 60 - 60: I11i . OOooOOo % i1IiiiI1iI / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / oooOo0oo0oo . Ii1I * i1iIi
  if 59 - 59: iI11I1II1I1I / Ii1I % i1iIi
zip = oo00 . getSetting ( 'zip' )
Oooo = xbmc . translatePath ( os . path . join ( zip ) )
def o0oOOoO000 ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 86 - 86: iI11I1II1I1I - Iii % i1iIi . oooOo0oo0oo * OOooOOo . ooOoO0O00
  if 75 - 75: Iii + i1iIi / i1iIi - oooOo0oo0oo * oO0o * i1iIi
  if 53 - 53: III1iiIii % I1ii11iIi11i
def IiIII ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  o0oOOoO000 ( )
  i1i1I1Ii1IIii = open ( url ) . read ( )
  oooOOoo = os . path . join ( Oooo , description . split ( 'Your ' ) [ 1 ] )
  O0oO0 = open ( oooOOoo , mode = 'w' )
  O0oO0 . write ( i1i1I1Ii1IIii )
  O0oO0 . close ( )
 else :
  if 'guisettings.xml' in description :
   O0OO00000o00 = open ( os . path . join ( Oooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOoOO = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( oOoOO ) . findall ( O0OO00000o00 )
   for type , iI1iii1iIiiI , II1iiiiI1 in IIi :
    II1iiiiI1 = II1iiiiI1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iI1iii1iIiiI , II1iiiiI1 ) )
  else :
   oooOOoo = os . path . join ( url )
   i1i1I1Ii1IIii = open ( os . path . join ( Oooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0oO0 = open ( oooOOoo , mode = 'w' )
   O0oO0 . write ( i1i1I1Ii1IIii )
   O0oO0 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: III1iiIii + iI11I1II1I1I + oOo0O0Ooo + i1IiiiI1iI
 if 72 - 72: oO0o + Ii + Ii1I
 if 96 - 96: i1i1I1IIii1II % ooOoO0O00 / I11i
def Ii1IIi11 ( ) :
 i1ooO = 1
 o0oOOoO000 ( )
 i11iii1Ii1 = xbmc . translatePath ( os . path . join ( Oooo , 'Build Backup' , 'Full Backup' , '' ) )
 o0oO0iiiiI1Iii = xbmc . translatePath ( os . path . join ( Oooo , 'Build Backup' , 'my_full_backup.zip' ) )
 I1I111IIIi1 = xbmc . translatePath ( os . path . join ( Oooo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( i11iii1Ii1 ) :
  os . makedirs ( i11iii1Ii1 )
 oOOo00O0O0 = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oOOo00O0O0 ) : return False , 0
 iiIIiiI = oOOo00O0O0
 O0oo0O0OO0Oo = xbmc . translatePath ( os . path . join ( i11iii1Ii1 , iiIIiiI + '.zip' ) )
 oO00o0oO0O = [ 'plugin.video.GenieTv' ]
 iI11Iii1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0i1I = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 O0o0o00OoOo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oO00o0O0Ooo = "Creating full backup of existing build"
 ii11 = "Creating Community Build"
 I1i11IIIi = "Archiving..."
 III1IIIIIiiI = ""
 i1iIii = "Please Wait"
 O0o00 ( oOo0oooo00o , O0oo0O0OO0Oo , ii11 , I1i11IIIi , III1IIIIIiiI , i1iIii , o0i1I , O0o0o00OoOo )
 time . sleep ( 1 )
 I1IIi1iI1iiI = xbmc . translatePath ( os . path . join ( i11iii1Ii1 , iiIIiiI + '_guisettings.zip' ) )
 iiI11I1ii11 = zipfile . ZipFile ( I1IIi1iI1iiI , mode = 'w' )
 try :
  iiI11I1ii11 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iiI11I1ii11 . close ( )
 if i1ooO == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + o0oO0iiiiI1Iii , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O0oo0O0OO0Oo + '[/COLOR]' )
  if 71 - 71: i1iIi . Ii1I * o0o00Oo0O - i1IiiiI1iI - IIiIiII11i
def O0o00 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iIIi11ii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O000Oo00 = len ( sourcefile )
 iI1oOoo = [ ]
 o00O0o00oo = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for iIiiII , iII1I , o00oOOo0Oo in os . walk ( sourcefile ) :
  for file in o00oOOo0Oo :
   o00O0o00oo . append ( file )
 Oooo0o0oO = len ( o00O0o00oo )
 for iIiiII , iII1I , o00oOOo0Oo in os . walk ( sourcefile ) :
  iII1I [ : ] = [ o0OOoOooO0ooO for o0OOoOooO0ooO in iII1I if o0OOoOooO0ooO not in exclude_dirs ]
  o00oOOo0Oo [ : ] = [ O0oO0 for O0oO0 in o00oOOo0Oo if O0oO0 not in exclude_files ]
  for file in o00oOOo0Oo :
   iI1oOoo . append ( file )
   IiiiIi = len ( iI1oOoo ) / float ( Oooo0o0oO ) * 100
   o0oOoO00o . update ( int ( IiiiIi ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IiI111 = os . path . join ( iIiiII , file )
   if not 'temp' in iII1I :
    if not 'plugin.program.originwizard' in iII1I :
     import time
     OO0OO00ooO0 = '01/01/1980'
     OOOOOoO00oo00 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IiI111 ) ) )
     if OOOOOoO00oo00 > OO0OO00ooO0 :
      iIIi11ii . write ( IiI111 , IiI111 [ O000Oo00 : ] )
 iIIi11ii . close ( )
 o0oOoO00o . close ( )
 if 9 - 9: oOo0O0Ooo - I1ii11iIi11i
 if 62 - 62: o0ii1I - i1i1I1IIii1II % iI11I1II1I1I
def ooOOO ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 97 - 97: ooOoO0O00 * i1IiiiI1iI . IIiIiII11i
 if 62 - 62: ii . o0ii1I
def IIioo0 ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  O00OoO0o ( )
 if O0O00Oo == 1 :
  OoOoO ( )
 if O0O00Oo == 2 :
  iIiI1 ( )
 if O0O00Oo == 3 :
  IiiIIi ( )
  if 87 - 87: Iii . Iii . IIiIiII11i / oooOo0oo0oo
  if 86 - 86: i1i1I1IIii1II % o0o00Oo0O + oO0o
  if 52 - 52: I1ii11iIi11i / IiI1i11I
  if 42 - 42: iI11I1II1I1I * o0ii1I / oO0o + oooOo0oo0oo
  if 48 - 48: ii - i1IiiiI1iI . Ii * IiI1i11I - o0ii1I - I11i
  if 59 - 59: IiI1i11I / Iii . I1ii11iIi11i
  if 100 - 100: o0o00Oo0O
  if 94 - 94: Ii1I - I11i
  if 42 - 42: I11i * OOooOOo . oO0o - IiI1i11I / IIiIiII11i
def iII1ii11III ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   oOo ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if O0O00Oo == 1 :
   oOo ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if O0O00Oo == 2 :
   OOOO0oO0O ( )
  if O0O00Oo == 3 :
   ooooO ( )
  if O0O00Oo == 4 :
   O000oooO0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0O00Oo == 5 :
   oOO00 ( )
  if O0O00Oo == 6 :
   oO0o00 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0O00Oo == 7 :
   Oo0OOOO0oOoo0 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0O00Oo == 8 :
   O0OIIII1i ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0O00Oo == 9 :
   i1I1Iiii ( )
  if O0O00Oo == 10 :
   I1iIIIiiii ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Quicksilver.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 1030 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , iiIi1IIiIi + 'KodibleAudioBooks.png' , Oo00OOOOO , '' )
  if 44 - 44: i1IiiiI1iI / o0ii1I * oooOo0oo0oo * ooOoO0O00 . o0ii1I * Ii
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 91 - 91: o0ii1I - IiI1i11I . ooOoO0O00 . Ii1I * I11i % IiI1i11I
def i1IIi111iI ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   IiIiII11i1 ( )
  if O0O00Oo == 1 :
   iiI ( )
  if O0O00Oo == 2 :
   I1i ( )
  if O0O00Oo == 3 :
   Ii1I1iIiiI1 ( oOOo0O00o )
  if O0O00Oo == 4 :
   o00i111iiIiiIiI ( oOOo0O00o )
  if O0O00Oo == 5 :
   OOOOo0o00OO0000 ( )
  if O0O00Oo == 6 :
   OOooooO ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0O00Oo == 7 :
   oOoo00 ( )
 else :
  Ii1I1i ( 'CLLEANUP' , 'url' , 9666 , iiIi1IIiIi + 'MAIN5.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '' , 80000 , iiIi1IIiIi + 'KillKodi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiIi1IIiIi + 'Speedtest.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiIi1IIiIi + 'View-Log-File.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'DELETE CACHE' , 'url' , 14 , iiIi1IIiIi + 'DeleteCache.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'DELETE PACKAGES' , 'url' , 6 , iiIi1IIiIi + 'DeletePackages.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'FORCE REFRESH' , 'url' , 10 , iiIi1IIiIi + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
  I1I1II1I11 ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , iiIi1IIiIi + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
  Ii1I1i ( 'CHECK MY IP' , 'url' , 12 , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iiIi1IIiIi + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 29 - 29: oooOo0oo0oo / OOooOOo . iI11I1II1I1I / Iii % OOooOOo % IiI1i11I
  if 49 - 49: IIiIiII11i / III1iiIii - o0ii1I
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 7 - 7: oOo0O0Ooo / oO0o + i1IiiiI1iI + Iii / oOo0O0Ooo
 if 82 - 82: Ii1I + ii
def i1i1II ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iiIi1IIiIi + 'repos.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEW[/COLOR]' , str ( oO0000OOo00 ) , 22 , iiIi1IIiIi + 'NEW.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']IPTV[/COLOR]' , str ( oO0000OOo00 ) , 23 , iiIi1IIiIi + 'IPTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VIDEO[/COLOR]' , str ( oO0000OOo00 ) , 24 , iiIi1IIiIi + 'VIDEO.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SPORTS[/COLOR]' , str ( oO0000OOo00 ) , 25 , iiIi1IIiIi + 'SPORTS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 26 , iiIi1IIiIi + 'KIDS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 27 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PROGRAMS[/COLOR]' , str ( oO0000OOo00 ) , 28 , iiIi1IIiIi + 'PROGRAMS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XXX[/COLOR]' , 'URL' , 29 , iiIi1IIiIi + 'XXX.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 21 - 21: i1i1I1IIii1II * i1i1I1IIii1II / Iii . IiI1i11I
 if 10 - 10: o0ii1I * oooOo0oo0oo - I1ii11iIi11i - ii / I11i
def o0oo00oo0oO ( ) :
 iii ( )
 Ii1I1i ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 49 - 49: oOo0O0Ooo
def II1III1I1I1Ii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 24 - 24: IIiIiII11i / o0ii1I . iI11I1II1I1I - IIiIiII11i % o0o00Oo0O
def IIi1Ii11iIi ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 33 - 33: IIiIiII11i . IIiIiII11i / OOooOOo - IIiIiII11i
 if 10 - 10: OOooOOo - I11i * Ii / I1ii11iIi11i + I11i + iI11I1II1I1I
 if 23 - 23: ooOoO0O00 + Ii1I + oOo0O0Ooo - i1iIi % ii . III1iiIii
def iII ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  O0oo ( )
 if O0O00Oo == 0 :
  iIIi1 ( oOOo0O00o )
 if O0O00Oo == 0 :
  OoOo0O00 ( oOOo0O00o )
  if 9 - 9: oooOo0oo0oo
  if 38 - 38: Iii . oO0o . Ii * ii + IiI1i11I
  if 49 - 49: I1ii11iIi11i - oO0o / i1IiiiI1iI / I11i % i1i1I1IIii1II
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 38 - 38: I11i . i1i1I1IIii1II / I11i % IIiIiII11i
def I11iI1iIii1ii ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for ooO0OO , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , ooO0OO , ooO0OO , '' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 70 - 70: o0o00Oo0O / ii + Ii1I + ooOoO0O00
def O00Oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( oOOoooo0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 34 - 34: IIiIiII11i - III1iiIii % OOooOOo % o0ii1I / i1iIi
def O0oo ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - oooOo0oo0oo
def IIIiII11 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O00OO00OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 47 - 47: ooOoO0O00 % i1iIi - I1ii11iIi11i * Iii / Ii
def Iii1Iii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiI11111II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 48 - 48: IiI1i11I % Ii . ii * III1iiIii % oO0o . IiI1i11I
def IiOOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0O0O0O00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ooi1IIii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 60 - 60: o0ii1I % I1ii11iIi11i / Iii . IiI1i11I / i1IiiiI1iI - ii
def iIIi1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0iii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 40 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - IiI1i11I - Ii
def oo0O00o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo0oOooOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 38 - 38: Ii - i1i1I1IIii1II % III1iiIii
def oooooo0O000o ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  iIi1iIiIIII1iII1i ( )
 if O0O00Oo == 1 :
  O0OO00OoO00 ( )
 if O0O00Oo == 2 :
  O00o ( )
  if 34 - 34: oOo0O0Ooo * IiI1i11I % ii + iI11I1II1I1I . oOo0O0Ooo * o0o00Oo0O
  if 24 - 24: ooOoO0O00 . oooOo0oo0oo
  if 85 - 85: oOo0O0Ooo + oooOo0oo0oo + oooOo0oo0oo
  if 92 - 92: Iii % o0o00Oo0O % o0ii1I . o0ii1I . III1iiIii
def O0OO00OoO00 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , OOoO0Oo in IIi :
  oOoo000 ( 'Android Apps' + OOoO0Oo , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'apps.png' )
 for oOOo0O00o , OOoO0Oo in i1Iii1i1I :
  oOoo000 ( 'Android Games' + OOoO0Oo , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'GAMES.png' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def OO0O00 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/cat' in url :
   oOoo000 ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def ooOOoO0o0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/app' in url :
   oOoo000 ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def i1Ii1i11ii ( url ) :
 I1i111I = OooOoooOo ( url )
 i1iii1ii = url
 if "page=" in str ( url ) :
  i1iii1ii = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if 'apk' in url :
   Ii1I1i ( ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + ooO0OO )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , i1iii1ii + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def oO0O0oo ( name , url ) :
 I1i111I = oOOo000oOoO0 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I1i111I )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  OOOOOOO00OO ( name , url , 'Brackets' )
def O00o ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'https://www.apkfiles.com/search?q=' + ( o0OO00oo ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 i1Ii1i11ii ( i1i1IiIiIi1Ii )
 if 68 - 68: oOo0O0Ooo
def O00O ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( iIIOOo0O , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , iIIIiIi + '.apk' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 18 - 18: oOo0O0Ooo . Ii1I - I1ii11iIi11i
def Iii1o00o0 ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , iIIIiIi + '.mp4' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 84 - 84: OOooOOo - I1ii11iIi11i . i1iIi . III1iiIii - I1ii11iIi11i
 if 99 - 99: i1IiiiI1iI
def o0I1IiiiiI1i1I ( name , url , description ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 I11i1I1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print I11i1I1
 print '======================================='
 extract . all ( I11ii1IIiIi , I11i1I1 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 68 - 68: Ii + oO0o
 if 13 - 13: i1iIi - oOo0O0Ooo
 if 23 - 23: oOo0O0Ooo
 if 7 - 7: IiI1i11I % Ii1I
 if 64 - 64: i1IiiiI1iI + Ii
def iIi1iIiIIII1iII1i ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , oOOo0O00o , iiiI1i11Ii , IIo0o0O0O00oOOo , iI1i11i in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 80003 , iiiI1i11Ii , iiIi1IIiIi + 'APKToolsB.png' , iI1i11i )
def IIIIi1Iii1iIi ( apk , ret = None ) :
 if apk == "kodi" :
  ii1IIi1iI1ii1 = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( ii1IIi1iI1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   o00iIIiIi111iI = IIi [ 0 ] [ 0 ]
   iiIIiiI = IIi [ 0 ] [ 1 ]
   II1I1ii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( o00iIIiIi111iI , iiIIiiI )
  if ret == 'version' : return o00iIIiIi111iI
  else : return II1I1ii
 elif apk == "spmc" :
  oo0OO0O = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( oo0OO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  o00iIIiIi111iI = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  II1I1ii = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( o00iIIiIi111iI , o00iIIiIi111iI )
  if ret == 'version' : return o00iIIiIi111iI
  else : return II1I1ii
def OOOOOOO00OO ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  OO0OooOOoO00OO00 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OO0OooOOoO00OO00 : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  OoOo0oO0 = name
  if OO0OooOOoO00OO00 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not II1I1Ii ( url ) == True : ii11ii1iIiI1 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % OoOo0oO0 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iiI11I1ii11 = zipfile . ZipFile ( I11ii1IIiIi )
    for file in iiI11I1ii11 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as O0oO0 :
       i111iIi1i1 = file . split ( '/' ) [ 1 ]
       O0oO0 . write ( iiI11I1ii11 . read ( file ) )
       xbmc . sleep ( 500 )
       O0oO0 . close ( )
       try :
        os . remove ( I11ii1IIiIi )
       except :
        pass
       I11ii1IIiIi = os . path . join ( i1iIIi1 , i111iIi1i1 )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 65 - 65: OOooOOo . IIiIiII11i % IiI1i11I + o0ii1I
 if 37 - 37: i1i1I1IIii1II - iI11I1II1I1I + IIiIiII11i . o0ii1I % iI11I1II1I1I
 if 17 - 17: i1IiiiI1iI + ooOoO0O00 % o0o00Oo0O
 if 65 - 65: III1iiIii
def iiI11 ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOOo0O00o = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOOo0O00o )
  OoooOOo0oOO ( ( iIIIiIi ) . replace ( '_' , ' ' ) , oOOo0O00o )
  if 44 - 44: oooOo0oo0oo % iI11I1II1I1I
def OoooOOo0oOO ( name , url ) :
 if OO ( ) == 'android' :
  OO0OooOOoO00OO00 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OO0OooOOoO00OO00 : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  OoOo0oO0 = name
  if OO0OooOOoO00OO00 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not II1I1Ii ( url ) == True : ii11ii1iIiI1 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % OoOo0oO0 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : ii11ii1iIiI1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 30 - 30: Ii - oOo0O0Ooo / Ii1I
 if 26 - 26: i1iIi % i1i1I1IIii1II + oOo0O0Ooo / III1iiIii . oOo0O0Ooo
def IiIi1i1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 35 - 35: IIiIiII11i / o0ii1I
 if 79 - 79: OOooOOo + i1IiiiI1iI * IiI1i11I * o0ii1I
def II11IiiIII ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 30015 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 53 - 53: oooOo0oo0oo / I1ii11iIi11i
def iIO0oOoo00Oo0O ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 oo00I1IiI1IIiI = url
 ooO0OO = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iIii1iI , iIIIiIi in IIi :
  if '.mp4' in iIIIiIi :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + iIii1iI , 222 , ooO0OO , fanart , '' )
  if 'description' in iIIIiIi :
   Ii1I1i ( 'Read Description' , url + '/' + iIii1iI , 30017 , ooO0OO , fanart , '' )
  if 'images' in iIIIiIi :
   I1I1II1I11 ( 'View Images' , url + '/' + iIii1iI , 30018 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Android' , url + '/' + iIii1iI , 30016 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + iIii1iI , 30019 , ooO0OO , fanart , '' )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 5 - 5: o0o00Oo0O - IiI1i11I / i1IiiiI1iI . I11i
def iIII1iIii ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  iiIII1i1 ( url )
  if 78 - 78: i1i1I1IIii1II % OOooOOo
def IIiII1i1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  II11I ( url )
  if 32 - 32: ii + oO0o . i1IiiiI1iI / i1i1I1IIii1II + ii - o0ii1I
def ooOooOOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I1Ii1i11I1I in IIi :
  o0OIiII ( 'Description:' , I1Ii1i11I1I )
  if 16 - 16: III1iiIii % ii - i1iIi * o0ii1I - o0ii1I
def I1iiII1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iIii1iI , iIIIiIi in IIi :
  if 'png' in iIIIiIi :
   Ii1I1i ( 'image' , '' , '' , url + '/' + iIii1iI , url + '/' + iIii1iI , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 45 - 45: oO0o + oO0o % i1iIi
def I1i1i1iIi1iIi ( name , url , description ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
 if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / Iii + OOooOOo
 if 98 - 98: oooOo0oo0oo
def II11I ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIiII11i1 ( )
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - i1i1I1IIii1II . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
def iiIII1i1 ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIiII11i1 ( )
 if 75 - 75: oO0o % ii
def iiiI ( name , url , description ) :
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 I11ii1IIiIi = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIiII11i1 ( )
 if 77 - 77: IIiIiII11i - Ii
def OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def O00Oooo ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : O0oO0 = open ( oO , 'w' ) ; O0oO0 . close ( )
 with open ( oO , 'a' ) as O0oO0 :
  o0o00O0oOOo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  O0oO0 . write ( o0o00O0oOOo . rstrip ( '\r\n' ) + '\n' )
def IiIiII11i1 ( ) :
 O0O00Oo = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0O00Oo == 0 : return
 elif O0O00Oo == 1 : pass
 I1i1i1iii = OO ( )
 O00Oooo ( "Platform: " + str ( I1i1i1iii ) )
 os . _exit ( 1 )
 O00Oooo ( "Force close failed!  Trying alternate methods." )
 if I1i1i1iii == 'osx' :
  O00Oooo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1i1iii == 'linux' :
  O00Oooo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1i1iii == 'android' :
  O00Oooo ( "############ try android force close #################" )
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
  iIii1 . ok ( i1iiIIiiI111 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif I1i1i1iii == 'windows' :
  O00Oooo ( "############ try windows force close #################" )
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
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  O00Oooo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  O00Oooo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 68 - 68: Iii / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
  if 92 - 92: oO0o . I11i . o0ii1I % OOooOOo
  if 58 - 58: Ii1I % o0ii1I * o0ii1I - IiI1i11I
def OoOo0O00 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( url ) :
  for file in o00oOOo0Oo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    O0OO00000o00 = open ( ( os . path . join ( I111IiI11 , file ) ) ) . read ( )
    oOO00OoOo = O0OO00000o00 . replace ( oOo0oooo00o , 'special://home/' )
    O0oO0 = open ( ( os . path . join ( I111IiI11 , file ) ) , mode = 'w' )
    O0oO0 . write ( str ( oOO00OoOo ) )
    O0oO0 . close ( )
 IiIiII11i1 ( )
 if 83 - 83: ooOoO0O00
def OOOO0oO0O ( ) :
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 43 - 43: oooOo0oo0oo / oOo0O0Ooo
def III11i1iiiI ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def O0oooooO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def IIi1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , ooO0OO )
def II11II ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
def i1ii11III ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo
 o00O = 'https://www.radionomy.com/en/search/index?query=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( o00O )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOOo0O00o , 70005 , ooO0OO )
  if 26 - 26: OOooOOo
  if 1 - 1: III1iiIii + i1IiiiI1iI + oO0o * oOo0O0Ooo * i1iIi
def oOO00 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.listenlive.eu/' + oOOo0O00o , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def O000oooO0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 if 9 - 9: OOooOOo + IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
 if 25 - 25: ii . o0ii1I % IiI1i11I . III1iiIii
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , ooo000 , url , oooOoO0oo0o0 in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' [COLORorangered] ' + oooOoO0oo0o0 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[CR]' + ooo000 + '[CR]' + oooOoO0oo0o0 + '[/COLOR]' )
  if 4 - 4: Ii * Ii1I + ii - III1iiIii . i1iIi . iI11I1II1I1I
def IIiIIiI1iIII ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.toonjet.com/' + oOOo0O00o , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0ooo0oooO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I1i111I )
 for url , ooO0OO in IIi :
  if 'ol.gif' in ooO0OO :
   pass
  elif 'link_block_' in ooO0OO :
   pass
  elif '.png' in ooO0OO :
   pass
  else :
   oOoo000 ( ( ooO0OO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOoOO00oOOO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 94 - 94: i1IiiiI1iI
  if 39 - 39: ii
def I1iIIIiiii ( ) :
 o0OIi ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 o0OIi ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 19 - 19: Ii
def oOOOO ( ) :
 o0OIi ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 o0OIi ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 o0OIi ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 82 - 82: ooOoO0O00 + I11i - IIiIiII11i . o0ii1I
def oo0OOO0OOoOO ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , oOoO in IIi :
  if 'Parent' in iIIIiIi :
   pass
  elif '2' in oOoO :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: oO0o / o0o00Oo0O * I11i * i1IiiiI1iI + ii * IiI1i11I
def iIIi1I1Ii1 ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , oOoO in IIi :
  if o0OO00oo in iIIIiIi . lower ( ) :
   if '1' in oOoO :
    o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in oOoO :
    o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in oOoO :
    o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 54 - 54: ii . i1i1I1IIii1II - IiI1i11I
    if 76 - 76: i1IiiiI1iI
def O00o0 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , oOoO in IIi :
  if '1' in oOoO :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in oOoO :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in oOoO :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 98 - 98: iI11I1II1I1I + Ii * Ii1I / i1IiiiI1iI / i1iIi - o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: IiI1i11I
def Oo0OOo0o0o0o0 ( url ) :
 iIii1iI = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in i1Iii1i1I :
  if 'mp3' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in iIIIiIi :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIii1iI + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 95 - 95: oO0o
   if 68 - 68: iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIiIiII11i - iI11I1II1I1I
   if 75 - 75: i1iIi . oOo0O0Ooo * IIiIiII11i
def ooOO0000oo0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIii1iI = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'Parent' in iIIIiIi :
   pass
  elif '.db' in iIIIiIi :
   pass
  elif '.jpg' in iIIIiIi :
   pass
  elif '.html' in iIIIiIi :
   pass
  elif '.doc' in iIIIiIi :
   pass
  elif 'mp3' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIii1iI + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 60 - 60: oooOo0oo0oo * i1iIi * oO0o
   if 64 - 64: Iii / IIiIiII11i / oO0o - i1iIi * iI11I1II1I1I . IiI1i11I
def iIi11I1II ( ) :
 o0OIi ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 o0OIi ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 o0OIi ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 93 - 93: Ii1I - i1iIi % Ii1I
def I11II1 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOOo0O00o + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in ooO0OO :
   pass
  else :
   o0OIi ( ooO0OO , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOOo0O00o ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + ooO0OO + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: Ii1I * i1IiiiI1iI - i1i1I1IIii1II % oooOo0oo0oo % Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: i1IiiiI1iI
 if 10 - 10: Iii % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
def oo0OoOO000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: ooOoO0O00 * iI11I1II1I1I % i1i1I1IIii1II % OOooOOo / ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: I1ii11iIi11i % IiI1i11I
def OooO00O0OO0oo ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if o0OO00oo in iIIIiIi . lower ( ) :
   if '</a>' in iIIIiIi :
    pass
   elif '(' in iIIIiIi :
    o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 60 - 60: IIiIiII11i + I11i % i1IiiiI1iI + i1iIi . III1iiIii % IIiIiII11i
    if 58 - 58: i1iIi
def i1iI11ii ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 65 - 65: ooOoO0O00 . Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: Ii1I + oO0o - Ii1I * III1iiIii - Iii * Iii
 if 99 - 99: I1ii11iIi11i / i1IiiiI1iI * I1ii11iIi11i / iI11I1II1I1I * III1iiIii
def oo00OOo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIii1iI = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iIii1iI )
  if 61 - 61: i1i1I1IIii1II % i1iIi - Ii1I + i1i1I1IIii1II . OOooOOo
def IIIiI1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '<p align' in iIIIiIi :
   pass
  elif '&nbsp;' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 72 - 72: Iii * OOooOOo % i1IiiiI1iI % i1iIi
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: oooOo0oo0oo - Ii1I / III1iiIii
 if 95 - 95: I11i
def IIii1I11iiii1 ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'ongoing' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def oOo0OOoO0ooOOoo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , ooO0OO , ooO0OO , iIIIiIi )
 for url , iIIIiIi in III :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OOO0oOoO00OoO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1IiI1iI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 IiIi1I11 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in II1IiI1iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , iIIIiIi in iIIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def IiI1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 92 - 92: III1iiIii - III1iiIii % iI11I1II1I1I / IiI1i11I
def ooOo ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '9cart' in oOOo0O00o :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 4 - 4: I11i
def OooOoO0OO00 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , iIIIiIi in ii1I1IIii11 :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 94 - 94: I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + ii % oO0o
def I1111iIIiIIII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20003 , ooO0OO )
 for url , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 55 - 55: oO0o / ii
def ooooOOo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   oOoo000 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 100 - 100: oooOo0oo0oo % Ii - oOo0O0Ooo * i1IiiiI1iI - I11i
def Oooo0o00 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 74 - 74: I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . III1iiIii
def ooOoo0oo00000O ( url ) :
 url = cloudflare . source ( url )
 iiI1i ( url )
 if 84 - 84: iI11I1II1I1I
def III1Ii11i1II ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  iiI1i ( url )
  if 28 - 28: OOooOOo % i1i1I1IIii1II - oooOo0oo0oo + oooOo0oo0oo + i1i1I1IIii1II / iI11I1II1I1I
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
def o0oooO ( ) :
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % o0ii1I
def iIiI1 ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 81 - 81: oO0o - iI11I1II1I1I
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 60 - 60: i1IiiiI1iI
 for oOOo0O00o , iIIIiIi in IIi :
  if o0OO00oo in iIIIiIi . lower ( ) :
   if 'Dad!' in iIIIiIi :
    pass
   elif 'Family Guy' in iIIIiIi :
    pass
   elif '2 Stupid' in iIIIiIi :
    pass
   elif 'The Zelfs' in iIIIiIi :
    pass
   elif 'A Clone' in iIIIiIi :
    pass
   elif 'A.T.O.M' in iIIIiIi :
    pass
   elif 'Almost Naked' in iIIIiIi :
    pass
   elif 'Angry Kid' in iIIIiIi :
    pass
   elif 'Annoying Orange' in iIIIiIi :
    pass
   elif 'Aqua Teen' in iIIIiIi :
    pass
   elif 'Assy Mcgee' in iIIIiIi :
    pass
   elif 'Astroblast' in iIIIiIi :
    pass
   elif 'Atomic Betty' in iIIIiIi :
    pass
   elif 'Axe Cop' in iIIIiIi :
    pass
   elif 'Baby Playpen' in iIIIiIi :
    pass
   elif 'Beavis and Butt' in iIIIiIi :
    pass
   elif 'Celebrity Deathmatch' in iIIIiIi :
    pass
   elif 'Clerks The' in iIIIiIi :
    pass
   elif 'Crapston Villas' in iIIIiIi :
    pass
   elif 'Duckman:' in iIIIiIi :
    pass
   elif 'Stripperella' in iIIIiIi :
    pass
   elif 'Vixen' in iIIIiIi :
    pass
   else :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 77 - 77: oOo0O0Ooo / Ii1I
    if 95 - 95: i1IiiiI1iI * ooOoO0O00 + i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 40 - 40: IIiIiII11i
def o0oO0OoO0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if 'Dad!' in iIIIiIi :
   pass
  elif 'Family Guy' in iIIIiIi :
   pass
  elif '2 Stupid' in iIIIiIi :
   pass
  elif 'The Zelfs' in iIIIiIi :
   pass
  elif 'A Clone' in iIIIiIi :
   pass
  elif 'A.T.O.M' in iIIIiIi :
   pass
  elif 'Almost Naked' in iIIIiIi :
   pass
  elif 'Angry Kid' in iIIIiIi :
   pass
  elif 'Annoying Orange' in iIIIiIi :
   pass
  elif 'Aqua Teen' in iIIIiIi :
   pass
  elif 'Assy Mcgee' in iIIIiIi :
   pass
  elif 'Astroblast' in iIIIiIi :
   pass
  elif 'Atomic Betty' in iIIIiIi :
   pass
  elif 'Axe Cop' in iIIIiIi :
   pass
  elif 'Baby Playpen' in iIIIiIi :
   pass
  elif 'Beavis and Butt' in iIIIiIi :
   pass
  elif 'Celebrity Deathmatch' in iIIIiIi :
   pass
  elif 'Clerks The' in iIIIiIi :
   pass
  elif 'Crapston Villas' in iIIIiIi :
   pass
  elif 'Duckman:' in iIIIiIi :
   pass
  elif 'Stripperella' in iIIIiIi :
   pass
  elif 'Vixen' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: oooOo0oo0oo / oO0o
def oOOo ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  oOOOo0Oooo = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10007 , oOOOo0Oooo )
  if 39 - 39: o0ii1I % ooOoO0O00 . Ii1I - o0o00Oo0O
  if 65 - 65: i1i1I1IIii1II * i1i1I1IIii1II / Iii + i1i1I1IIii1II % i1iIi + OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: I11i
def ii111Ii1i ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   IiI1I1II ( url )
   if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / Iii
   if 21 - 21: ii / III1iiIii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 66 - 66: I11i * oO0o % ooOoO0O00 - iI11I1II1I1I
def IiI1I1II ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 11 - 11: IiI1i11I / i1i1I1IIii1II % ooOoO0O00 . Ii1I
  if 16 - 16: ii - oooOo0oo0oo + I1ii11iIi11i
  if 67 - 67: Ii1I % ii
def III1 ( ) :
 if 14 - 14: i1IiiiI1iI / Iii - oooOo0oo0oo * o0o00Oo0O % III1iiIii . o0o00Oo0O
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 86 - 86: ooOoO0O00 * ii
def I1I1I1 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if 'elete' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 222 , ooO0OO )
   if 29 - 29: Ii1I
def oOOoOO ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OoO0oOOoo0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , Oo000O000 , i1iII1IiiIiI1 in O0OoO0oOOoo0 :
  for o0OO00oo in Oo000O000 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOOo0O00o , iIIIiIi in iIi11 :
    if 'tube' in oOOo0O00o :
     pass
    elif 'stage' in oOOo0O00o :
     OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + Oo000O000 + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO , )
    elif 'vee' in oOOo0O00o :
     pass
     if 67 - 67: Iii / o0o00Oo0O * o0ii1I - III1iiIii . ii + III1iiIii
def i1I1iiiI ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OoO0oOOoo0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , Oo000O000 , i1iII1IiiIiI1 in O0OoO0oOOoo0 :
  iIi11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOOo0O00o , iIIIiIi in iIi11 :
   if 'tube' in oOOo0O00o :
    pass
   elif 'stage' in oOOo0O00o :
    OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + Oo000O000 + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO )
   elif 'vee' in oOOo0O00o :
    pass
    if 44 - 44: Iii
    if 76 - 76: Ii1I . i1iIi . i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I1ii11iIi11i
def iii1IIII1iii11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oo0OoOooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oo0OoOooo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oo0OoOooo :
  i1II11II1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 91 - 91: oooOo0oo0oo . oOo0O0Ooo % IiI1i11I
  if 86 - 86: oOo0O0Ooo + Iii * OOooOOo - i1IiiiI1iI / i1IiiiI1iI
  if 9 - 9: I11i / IiI1i11I . iI11I1II1I1I % o0o00Oo0O
  if 38 - 38: IiI1i11I
  if 78 - 78: Ii . III1iiIii % ii - III1iiIii - III1iiIii + o0ii1I
  if 11 - 11: Iii
  if 20 - 20: o0o00Oo0O . Ii * ooOoO0O00 % o0o00Oo0O . oOo0O0Ooo
def I1Iiiiiii ( ) :
 if 53 - 53: i1iIi / ii - IIiIiII11i
 OoiiI1 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 OoiiI1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 70 - 70: ii . i1iIi / i1i1I1IIii1II . i1i1I1IIii1II - I11i
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 29 - 29: Iii % oooOo0oo0oo - i1iIi
def IiI1i11i1iI ( ) :
 OoiiI1 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 OoiiI1 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 92 - 92: oooOo0oo0oo % IIiIiII11i . IiI1i11I
 I1iI1ii1II ( 'movies' , 'MAIN' )
def II1i1iI ( ) :
 if 5 - 5: OOooOOo + IiI1i11I * i1iIi
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 oo0O0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . i1iIi / I1ii11iIi11i - Ii
 for oO0ooOO in oo0O0o :
  IIi1iI1 = oO0 + oO0ooOO + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( IIi1iI1 )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
   if o0OO00oo in iIIIiIi . lower ( ) :
    OOoo ( iIIIiIi , oOOo0O00o , 222 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
    if 40 - 40: oOo0O0Ooo
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 3 - 3: i1iIi / ooOoO0O00 - OOooOOo
    if 73 - 73: ii * o0o00Oo0O * i1iIi
def iii11Ii ( ) :
 if 31 - 31: i1i1I1IIii1II
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 oo0O0o = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 69 - 69: iI11I1II1I1I . Iii / IiI1i11I
 for oO0ooOO in oo0O0o :
  ooOOooo0o000O = oO0 + oO0ooOO + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( ooOOooo0o000O )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
   if o0OO00oo in iIIIiIi . lower ( ) :
    OoiiI1 ( iIIIiIi , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
    if 58 - 58: iI11I1II1I1I / oOo0O0Ooo
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 64 - 64: Ii1I / IiI1i11I / OOooOOo + I11i . o0ii1I . i1i1I1IIii1II
    if 9 - 9: III1iiIii - IIiIiII11i * oO0o
def Oo0oo ( ) :
 if 64 - 64: OOooOOo % iI11I1II1I1I
 I1i111I = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
  OoiiI1 ( iIIIiIi , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def iII1I1Ii11i1i ( url ) :
 if 80 - 80: Ii % iI11I1II1I1I / Ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoOO0ooo0O = ( '%s%s' % ( ii1IIi1IIIIi1 , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in IIi :
  IIi11i1II = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for ooo00Ooo in IIi11i1II :
   if ooo00Ooo == url :
    iIIIiIi = ( '[COLORred]Watched - [/COLOR]' + iIIIiIi ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  OOoo ( iIIIiIi , url , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
  if 4 - 4: Ii1I - III1iiIii
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 6 - 6: o0o00Oo0O . ii . i1IiiiI1iI - o0ii1I / i1iIi
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: OOooOOo % I11i - i1i1I1IIii1II
  if 40 - 40: IiI1i11I
def o0oIi1iiiii ( url ) :
 if 88 - 88: o0ii1I / Ii % OOooOOo % oooOo0oo0oo
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
  OoiiI1 ( iIIIiIi , url , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  if 70 - 70: Ii1I . Ii1I / Iii . Ii1I
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: I11i - ii + IiI1i11I . Iii
def OOoo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 88 - 88: Iii - IiI1i11I
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOO000O = [ ]
  oOO000O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = False )
 return o0Oo0
 if 68 - 68: I1ii11iIi11i % i1i1I1IIii1II . III1iiIii - I11i / ooOoO0O00 / ii
def OoiiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 34 - 34: Iii % I1ii11iIi11i + o0ii1I
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOO000O = [ ]
  oOO000O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = True )
 return o0Oo0
if 93 - 93: o0ii1I - i1IiiiI1iI % o0o00Oo0O
if 11 - 11: Ii
if 6 - 6: IIiIiII11i
if 1 - 1: i1iIi % I1ii11iIi11i . i1i1I1IIii1II
if 98 - 98: IIiIiII11i + IIiIiII11i - iI11I1II1I1I . OOooOOo . i1IiiiI1iI
if 99 - 99: i1i1I1IIii1II . o0ii1I * i1IiiiI1iI * iI11I1II1I1I / OOooOOo % III1iiIii
if 70 - 70: Ii1I . o0o00Oo0O
if 70 - 70: I1ii11iIi11i + Ii
if 44 - 44: Ii / oooOo0oo0oo * i1iIi
if 88 - 88: ooOoO0O00 % oooOo0oo0oo / ii * IiI1i11I % i1iIi
if 5 - 5: Ii1I * o0ii1I % Iii % IIiIiII11i
if 9 - 9: I11i % i1IiiiI1iI + Iii
if 55 - 55: oO0o - Ii1I
if 38 - 38: iI11I1II1I1I % III1iiIii % oO0o % o0o00Oo0O * iI11I1II1I1I / i1IiiiI1iI
if 65 - 65: oooOo0oo0oo - oOo0O0Ooo * i1IiiiI1iI
def oO00O0 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 80 - 80: IiI1i11I + i1iIi * I11i - IIiIiII11i - Ii1I
def O0Oo0O0O0o ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iiII11ii1Ii = [ ]
 try :
  if 15 - 15: i1iIi
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  oO00O0 ( 'Making Favorites File' )
  iiII11ii1Ii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  O0OO00000o00 = open ( i1I1iI , "w" )
  O0OO00000o00 . write ( json . dumps ( iiII11ii1Ii ) )
  O0OO00000o00 . close ( )
 else :
  oO00O0 ( 'Appending Favorites' )
  O0OO00000o00 = open ( i1I1iI ) . read ( )
  iIi1iiii1ii = json . loads ( O0OO00000o00 )
  iIi1iiii1ii . append ( ( name , url , iconimage , fanart , mode ) )
  oOO00OoOo = open ( i1I1iI , "w" )
  oOO00OoOo . write ( json . dumps ( iIi1iiii1ii ) )
  oOO00OoOo . close ( )
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
  if 21 - 21: OOooOOo - Ii - OOooOOo
def i1oo0OO0Oo ( ) :
 if os . path . exists ( i1I1iI ) == False :
  iiII11ii1Ii = [ ]
  oO00O0 ( 'Making Favorites File' )
  iiII11ii1Ii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  O0OO00000o00 = open ( i1I1iI , "w" )
  O0OO00000o00 . write ( json . dumps ( iiII11ii1Ii ) )
  O0OO00000o00 . close ( )
 else :
  iIIi111I1i1i = json . loads ( open ( i1I1iI ) . read ( ) )
  i1ii1i1Ii11 = len ( iIIi111I1i1i )
  for IiIii111III1 in iIIi111I1i1i :
   iIIIiIi = IiIii111III1 [ 0 ]
   oOOo0O00o = IiIii111III1 [ 1 ]
   iiiI1I1iIIIi1 = IiIii111III1 [ 2 ]
   try :
    IiI1I1iii = IiIii111III1 [ 3 ]
    if IiI1I1iii == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     IiI1I1iii = iiiI1I1iIIIi1
    else :
     IiI1I1iii = IIo0o0O0O00oOOo
   try : i1ii111iiI11iI = IiIii111III1 [ 5 ]
   except : i1ii111iiI11iI = None
   try : Oo0 = IiIii111III1 [ 6 ]
   except : Oo0 = None
   if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
   if IiIii111III1 [ 4 ] == 0 :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , '' , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , '' , 'fav' )
   else :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , IiIii111III1 [ 4 ] , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , '' , 'fav' )
    if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000ooO0Ooo0o ( name ) :
 iIi1iiii1ii = json . loads ( open ( i1I1iI ) . read ( ) )
 for iii1111iiI1ii in range ( len ( iIi1iiii1ii ) ) :
  if iIi1iiii1ii [ iii1111iiI1ii ] [ 0 ] == name :
   del iIi1iiii1ii [ iii1111iiI1ii ]
   oOO00OoOo = open ( i1I1iI , "w" )
   oOO00OoOo . write ( json . dumps ( iIi1iiii1ii ) )
   oOO00OoOo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 42 - 42: iI11I1II1I1I / Iii . o0o00Oo0O . o0ii1I
 if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
def II1i1i1I1iII ( ) :
 iiIII1i = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 IiI1Ii11Iiii = open ( iiIII1i , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 IiI1Ii11Iiii . write ( r'[' + IiII + ']' + '\n' )
 for iIIIiIi , ooO0OO , Ii11II11iI1 , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OoOo0Oooo0o = ( iIIIiIi + '=plugin://' + IiII + '/?url=' + oOOo0O00o + '&mode=10012&name=' + ( iIIIiIi ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IiI1Ii11Iiii . write ( OoOo0Oooo0o + '\n' )
  if 65 - 65: OOooOOo + i1IiiiI1iI % oOo0O0Ooo
  if 54 - 54: i1IiiiI1iI / I11i
def I11IIIIiII ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o in IIi :
  oOoo000 ( '24/7' , oOOo0O00o , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - i1IiiiI1iI
def Oo0OOo ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def ooooO ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def IIII1iII ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def I1i1i1IIi1I ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def IIi11iIIiIiI ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 54 - 54: i1i1I1IIii1II
  if 26 - 26: i1iIi % ii . i1IiiiI1iI * i1iIi + IIiIiII11i - Ii1I
def i1IIIii ( ) :
 if 37 - 37: IiI1i11I . I11i / o0ii1I / oooOo0oo0oo * ooOoO0O00
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + i1i1I1IIii1II
def o0oOoo00 ( ) :
 if 21 - 21: o0o00Oo0O * i1iIi % OOooOOo / o0o00Oo0O
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi , o0OOOOoO in IIi :
  I1I1II1I11 ( iIIIiIi + '  -  ' + ( o0OOOOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 85 - 85: ii + ii
  if 23 - 23: ooOoO0O00
  if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Iii . oO0o
def oOOo0O0Oo ( ) :
 if 50 - 50: i1i1I1IIii1II * Iii + oooOo0oo0oo - I1ii11iIi11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Adventure[/COLOR]' , 'Macera' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Anime[/COLOR]' , 'Anime' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Drama[/COLOR]' , 'Dram' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Family[/COLOR]' , 'Aile' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']History[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Horror[/COLOR]' , 'Korku' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Romance[/COLOR]' , 'Romantik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sport[/COLOR]' , 'Spor' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Western[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 79 - 79: oO0o / ooOoO0O00
def iIi1i1I1I ( url ) :
 oo00I1IiI1IIiI = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( oo00I1IiI1IIiI )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 35 - 35: Iii + o0o00Oo0O * IIiIiII11i
  if 23 - 23: OOooOOo * III1iiIii / i1i1I1IIii1II
  if 60 - 60: i1iIi * o0ii1I + i1IiiiI1iI . oooOo0oo0oo . o0o00Oo0O
  if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
def O0oO00o0o0oo0 ( ) :
 if 18 - 18: OOooOOo
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0OO00oo ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( oOOo0O00o )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if o0OO00oo in iIIIiIi . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 77 - 77: i1IiiiI1iI . Ii / o0ii1I * Ii - I11i
   if 6 - 6: Ii
   if 16 - 16: III1iiIii
def OooooOO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIii1iI , OOo , i1IIII11II1 , iIIIiIi in IIi :
  OOOO0oOO = ( i1IIII11II1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIIiii = ( OOo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I11OoooO = 'Season ' + IIIiii + 'Episode ' + OOOO0oOO + iIIIiIi
  i1IIi11 ( I11OoooO , iIii1iI )
  if 93 - 93: OOooOOo . I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 66 - 66: I1ii11iIi11i - OOooOOo - i1IiiiI1iI
  if 87 - 87: ii + ii * i1iIi
def i1IIi11 ( name , url ) :
 iIii1iI = url
 IiiIiIIiiIiI = name
 o0o = cloudflare . source ( iIii1iI )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for oo0OoOooo , I1 in i1Iii1i1I :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IiiIiIIiiIiI + I1 + '[/COLOR]' , oo0OoOooo , 222 , iiIi1IIiIi + 'dtv.png' )
  if 73 - 73: i1iIi . I1ii11iIi11i * oO0o - Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: i1IiiiI1iI
 if 10 - 10: Ii + i1iIi / ii
def o0ii1i ( ) :
 if 57 - 57: ii % IIiIiII11i - i1IiiiI1iI
 if 1 - 1: III1iiIii
 if 27 - 27: OOooOOo . i1IiiiI1iI * OOooOOo
 if 8 - 8: i1i1I1IIii1II * III1iiIii * i1iIi
 if 26 - 26: IiI1i11I * oooOo0oo0oo / oooOo0oo0oo - IiI1i11I
 if 59 - 59: o0ii1I % IiI1i11I / IIiIiII11i + oOo0O0Ooo * i1iIi
 if 100 - 100: Ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 81 - 81: Ii1I % IiI1i11I
def IiiII1I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iI1iI1iIi1ii1I1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + ooO0OO , '' , '' )
 for url in iI1iI1iIi1ii1I1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 59 - 59: IIiIiII11i * ii - ii
def iioOo00O0o ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iI1iI1iIi1ii1I1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  ooO0OO = 'http://watchepisodes.cc/' + ooO0OO
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10093 , ooO0OO , ooO0OO , '' )
 for url in iI1iI1iIi1ii1I1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 18 - 18: i1iIi
def IIIi1iiI1I1 ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1IIII11II1 , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + i1IIII11II1 + ' - ' + iIIIiIi + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , ooO0OO , '' , '' )
  if 20 - 20: i1iIi + iI11I1II1I1I
def O0ooOoO0 ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if 'player' in iIIIiIi :
   pass
  elif 'vod' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , ooO0OO , '' , '' )
   if 10 - 10: Ii % oooOo0oo0oo * IiI1i11I % I1ii11iIi11i
   if 51 - 51: oO0o % IiI1i11I
   if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
   if 8 - 8: Ii1I % oO0o % i1i1I1IIii1II . Ii1I * Ii1I
   if 94 - 94: Ii + ii
   if 20 - 20: Ii
def oOOoo ( ) :
 if 86 - 86: OOooOOo / oooOo0oo0oo
 if 40 - 40: iI11I1II1I1I / i1iIi / oOo0O0Ooo + Ii1I * oooOo0oo0oo
 if 1 - 1: oO0o * i1iIi + III1iiIii . i1i1I1IIii1II / i1iIi
 if 91 - 91: o0ii1I + Iii - I1ii11iIi11i % OOooOOo . IiI1i11I
 if 51 - 51: oooOo0oo0oo / Iii
 if 51 - 51: i1iIi * i1i1I1IIii1II - i1IiiiI1iI + IiI1i11I
 if 46 - 46: I11i - Ii % oO0o / o0ii1I - OOooOOo
 if 88 - 88: i1i1I1IIii1II * oOo0O0Ooo / oO0o - oooOo0oo0oo / ooOoO0O00 . i1IiiiI1iI
 if 26 - 26: Ii - i1iIi
 if 45 - 45: i1iIi + IIiIiII11i % IiI1i11I
 if 55 - 55: i1iIi - i1i1I1IIii1II % oOo0O0Ooo
 if 61 - 61: i1iIi
 if 22 - 22: iI11I1II1I1I / i1iIi / oOo0O0Ooo - I11i
 if 21 - 21: i1i1I1IIii1II . Ii * Iii . oooOo0oo0oo / oooOo0oo0oo
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 42 - 42: ii / i1IiiiI1iI . I11i / o0o00Oo0O - III1iiIii * III1iiIii
 if 1 - 1: o0ii1I % i1IiiiI1iI
def oo00Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1i1i1I ) )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 28 - 28: o0ii1I
def i111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 63 - 63: i1iIi % oOo0O0Ooo . oooOo0oo0oo - i1iIi / I1ii11iIi11i % oOo0O0Ooo
def II1i11i1iI1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'episode' in url :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 78 - 78: ii - OOooOOo . Ii
  if 36 - 36: i1i1I1IIii1II * IiI1i11I + III1iiIii * IiI1i11I . Ii1I - iI11I1II1I1I
def i1IIi1ii1i1ii ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoOOIi = 'http://www.watchseriesgo.to/search/' + o0OO00oo . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( oOoOOIi )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi in IIi :
  if 'watch online' in iIIIiIi :
   pass
  else :
   print oOOo0O00o
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOOo0O00o , 10044 , ooO0OO , '' , '' )
   if 30 - 30: i1iIi
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 33 - 33: i1IiiiI1iI * III1iiIii - o0o00Oo0O + oOo0O0Ooo / III1iiIii
def iii1II11II1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , i1IIII11II1 , O000OOO in IIi :
  oO00OoOO = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1IIII11II1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oO00OoOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , ooO0OO , '' , O000OOO )
  if 30 - 30: III1iiIii / Ii % oO0o * oooOo0oo0oo
def i1oOOOoOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oO00OoOO = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oO00OoOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 80 - 80: ii
def OOoo0o00O0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , ooO0OO , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 28 - 28: ii % o0o00Oo0O - oooOo0oo0oo / I11i / oOo0O0Ooo
def Iii1iIII1Iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1i1i1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOo , O0OoO0oOOoo0 in i1i1i1I :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0OoO0oOOoo0 ) )
  for url , iIIIiIi in IIi :
   oO00OoOO = ( OOo ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oO00OoOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 13 - 13: iI11I1II1I1I - oooOo0oo0oo
class i111ii1II11ii ( ) :
 if 21 - 21: Iii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 79 - 79: oO0o / oooOo0oo0oo - ooOoO0O00 + ooOoO0O00 - III1iiIii + III1iiIii
  oO00OoOO = name
  self . Get_Sources ( oOOo0O00o , oO00OoOO )
  if 67 - 67: oO0o * oO0o / ii
  if 79 - 79: I11i % iI11I1II1I1I / IIiIiII11i / o0ii1I / o0ii1I + o0o00Oo0O
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
   self . Get_site_link ( URL , season_name )
   if 46 - 46: ooOoO0O00 / III1iiIii
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  ii1I1IIii11 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in ii1I1IIii11 :
   self . main ( url , season_name )
   if 84 - 84: OOooOOo / iI11I1II1I1I + i1i1I1IIii1II % i1iIi + i1i1I1IIii1II - iI11I1II1I1I
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ii1Ii = 'DACLIPS'
   if ii1Ii in i111ii1II11ii . source_list :
    pass
   else :
    self . daclips ( url , season_name , ii1Ii )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    ii1Ii = 'THEVIDEO'
    if ii1Ii in i111ii1II11ii . source_list :
     pass
    else :
     self . thevideo ( url , season_name , ii1Ii )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     ii1Ii = 'ALLMYVIDEOS'
     if ii1Ii in i111ii1II11ii . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , ii1Ii )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      ii1Ii = 'VIDSPOT'
      if ii1Ii in i111ii1II11ii . source_list :
       pass
      else :
       self . vidspot ( url , season_name , ii1Ii )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       ii1Ii = 'VODLOCKER'
       if ii1Ii in i111ii1II11ii . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , ii1Ii )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        ii1Ii = 'VIDTO'
        if ii1Ii in i111ii1II11ii . source_list :
         pass
        else :
         self . vidto ( url , season_name , ii1Ii )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 41 - 41: i1iIi
       else :
        if 'youwatch' in url :
         ii1Ii = 'YouWatch'
         if ii1Ii in i111ii1II11ii . source_list :
          pass
         else :
          self . youwatch ( url , season_name , ii1Ii )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 11 - 11: ooOoO0O00 / i1IiiiI1iI * Ii1I * i1IiiiI1iI * i1iIi - Ii
          if 96 - 96: Ii1I % Ii1I
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIi1IiI , iIIIiIi in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 1 - 1: oOo0O0Ooo . o0ii1I
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI , iIIIiIi in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 26 - 26: i1i1I1IIii1II - i1iIi % I1ii11iIi11i - i1i1I1IIii1II + III1iiIii
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 33 - 33: o0ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * III1iiIii
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 21 - 21: o0o00Oo0O * i1iIi % oO0o
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 14 - 14: o0o00Oo0O / i1IiiiI1iI / i1iIi + III1iiIii - III1iiIii
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . youplay ( iIi1IiI , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIi1IiI in IIi :
   self . Printer ( iIi1IiI , season_name , source_name )
   if 10 - 10: o0o00Oo0O - Ii1I / i1IiiiI1iI % OOooOOo / ii / o0ii1I
 def Printer ( self , Link , season_name , source_name ) :
  if 73 - 73: i1iIi + III1iiIii % I11i . Ii1I / oooOo0oo0oo . i1IiiiI1iI
  if Link in i111ii1II11ii . List :
   pass
  elif source_name in i111ii1II11ii . source_list :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   i111ii1II11ii . List . append ( Link )
   i111ii1II11ii . source_list . append ( source_name )
   if 76 - 76: Iii . Ii1I * ii % IiI1i11I
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 24 - 24: ii
   if 83 - 83: o0o00Oo0O / oO0o
   if 62 - 62: Iii
   if 73 - 73: o0ii1I % oO0o * oooOo0oo0oo
   if 84 - 84: I1ii11iIi11i
def Ooo00OoOOO ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 18 - 18: ii
def ooo ( url ) :
 ii111I1I1I = '20'
 iIIiIi1IiI1 = [ ]
 Oo0O = '                                                    '
 Iii1I1III11 = '        '
 I1I1II1I11 ( Oo0O + 'pl' + Iii1I1III11 + 'w' + Iii1I1III11 + 'd' + Iii1I1III11 + 'l' + Iii1I1III11 + 'f' + Iii1I1III11 + 'a' + Iii1I1III11 + 'pts' , '' , '' , '' , '' , '' )
 I1i111I = Oo00oo0000OO ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I1i111I )
 for i1ii1IiIiIii , OOo0ooOOOo0O0 , ooI1 , o0OOoOooO0ooO , i1Iii1i1II1 , O0oO0 , O0OO00000o00 , O0o00OoooO , IiI1i1iI in IIi :
  iIIiiIIIII = iiiII ( OOo0ooOOOo0O0 )
  Oo0Ooo = iiiII ( ooI1 )
  II1iII11 = iiiII ( o0OOoOooO0ooO )
  iiiI1 = iiiII ( i1Iii1i1II1 )
  IiIi1i1I = iiiII ( O0oO0 )
  O0Oooo = iiiII ( O0OO00000o00 )
  iIIiIi1IiI1 . append ( i1ii1IiIiIii [ 0 ] )
  IiiI11Iii = len ( iIIiIi1IiI1 )
  I1Iii1 = int ( len ( Oo0O ) - len ( i1ii1IiIiIii ) - 2 )
  if len ( iIIiIi1IiI1 ) >= 10 :
   I1Iii1 = I1Iii1 - 1
  if len ( iIIiIi1IiI1 ) <= int ( ii111I1I1I ) :
   Ii1I1i ( str ( IiiI11Iii ) + ' ' + i1ii1IiIiIii + Oo0O [ 0 : I1Iii1 ] + OOo0ooOOOo0O0 + iIIiiIIIII + ooI1 + Oo0Ooo + o0OOoOooO0ooO + II1iII11 + i1Iii1i1II1 + iiiI1 + O0oO0 + IiIi1i1I + O0OO00000o00 + O0Oooo + ' ' + IiI1i1iI , '' , '' , '' , '' , '' )
   if 9 - 9: IIiIiII11i % I1ii11iIi11i * o0ii1I + III1iiIii % oO0o . ooOoO0O00
   if 68 - 68: IIiIiII11i % i1IiiiI1iI * Ii
def iiiII ( space ) :
 if len ( space ) > 1 :
  ii11Iiii = len ( '        ' ) - len ( space ) + 1
  space = int ( ii11Iiii ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 9 - 9: IIiIiII11i + Ii1I / IiI1i11I
def O0OOOo0o0O0 ( ) :
 if 7 - 7: oooOo0oo0oo . III1iiIii . i1IiiiI1iI / o0ii1I / I1ii11iIi11i
 if 83 - 83: Iii / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
 if 10 - 10: Iii - I11i % ii - Ii1I
 if 64 - 64: oO0o / oOo0O0Ooo
 if 23 - 23: Iii * i1IiiiI1iI * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: III1iiIii * ii . i1iIi % Ii
 if 11 - 11: iI11I1II1I1I . i1IiiiI1iI - I1ii11iIi11i / Iii + IIiIiII11i
 if 29 - 29: Iii . Ii + ooOoO0O00 - o0ii1I + o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: o0ii1I - ii + i1IiiiI1iI % I11i - OOooOOo . oOo0O0Ooo
 if 42 - 42: i1IiiiI1iI
 if 70 - 70: I11i / Iii + i1i1I1IIii1II % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: oooOo0oo0oo
 if 12 - 12: o0ii1I
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
 if 22 - 22: IiI1i11I + ii - OOooOOo - oO0o * i1IiiiI1iI - i1i1I1IIii1II
 if 99 - 99: i1iIi / oOo0O0Ooo . o0ii1I - o0ii1I * oOo0O0Ooo
 if 24 - 24: Iii * oO0o - i1i1I1IIii1II / iI11I1II1I1I - I1ii11iIi11i . oooOo0oo0oo
 if 2 - 2: i1iIi - o0o00Oo0O - Ii1I / Iii * OOooOOo
 if 26 - 26: Ii1I + i1IiiiI1iI - i1i1I1IIii1II + III1iiIii % oooOo0oo0oo
 if 84 - 84: Iii % o0ii1I % o0o00Oo0O * I11i
 if 15 - 15: i1i1I1IIii1II - iI11I1II1I1I - IIiIiII11i - III1iiIii % Ii1I
 if 80 - 80: III1iiIii * IiI1i11I . ooOoO0O00 % o0ii1I % Ii1I + i1iIi
 if 6 - 6: Ii1I . i1i1I1IIii1II . oO0o + III1iiIii
 if 65 - 65: Ii1I / i1iIi
 if 23 - 23: oooOo0oo0oo / oooOo0oo0oo * I11i * oooOo0oo0oo
 if 57 - 57: IiI1i11I
 if 29 - 29: oOo0O0Ooo
 if 41 - 41: i1IiiiI1iI * oO0o - IiI1i11I . o0ii1I
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - i1i1I1IIii1II + i1IiiiI1iI
 if 22 - 22: o0o00Oo0O % III1iiIii % IiI1i11I % oOo0O0Ooo
 if 34 - 34: IiI1i11I . I1ii11iIi11i % Ii1I . IiI1i11I % III1iiIii / III1iiIii
 if 84 - 84: o0ii1I
 if 1 - 1: i1i1I1IIii1II - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
 if 9 - 9: IiI1i11I - IiI1i11I
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + i1i1I1IIii1II
 if 20 - 20: oO0o + Iii . IIiIiII11i / Ii
 if 50 - 50: ii / oO0o % iI11I1II1I1I
 if 41 - 41: Ii1I % Ii1I + III1iiIii . IiI1i11I % i1IiiiI1iI * i1iIi
 if 57 - 57: o0ii1I . i1IiiiI1iI . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: i1iIi / oooOo0oo0oo * o0o00Oo0O
 if 17 - 17: oO0o / i1iIi % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / III1iiIii . Ii / oO0o % IIiIiII11i
 if 6 - 6: IiI1i11I % I11i + i1IiiiI1iI
 if 91 - 91: I11i + o0o00Oo0O * i1i1I1IIii1II * III1iiIii * Ii1I
 if 83 - 83: ii
 if 52 - 52: I11i / OOooOOo % i1i1I1IIii1II % oO0o / III1iiIii % I11i
 if 88 - 88: oooOo0oo0oo / Ii / o0ii1I / Ii * Ii1I % Iii
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * o0ii1I + iI11I1II1I1I
 if 80 - 80: I11i . IiI1i11I . ii
 if 63 - 63: i1iIi . oooOo0oo0oo
 if 66 - 66: oOo0O0Ooo
 if 99 - 99: oO0o % o0o00Oo0O . i1IiiiI1iI - Ii1I . I1ii11iIi11i / OOooOOo
 if 60 - 60: Ii1I
 if 78 - 78: i1i1I1IIii1II + IIiIiII11i
 if 55 - 55: ii
 if 90 - 90: oOo0O0Ooo
 if 4 - 4: oooOo0oo0oo % i1iIi - oooOo0oo0oo - I11i
 if 30 - 30: III1iiIii
 if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
 if 70 - 70: ii + oO0o * I1ii11iIi11i
 if 20 - 20: Ii - IIiIiII11i - i1iIi % i1i1I1IIii1II . i1iIi
 if 50 - 50: iI11I1II1I1I + i1IiiiI1iI - Iii - ii
 if 84 - 84: OOooOOo - Iii
 if 80 - 80: Ii % oooOo0oo0oo - I1ii11iIi11i % oooOo0oo0oo
 if 89 - 89: o0ii1I * Iii + OOooOOo / Ii
 if 68 - 68: ii * Iii
 if 86 - 86: I11i / OOooOOo
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOOo0O00o , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0OO , Oo00OOOOO , '' )
  if 40 - 40: IiI1i11I
def o000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  o0Ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1i1i1I ) )
  for Oo0O0OoOo00 in o0Ii1 :
   Oo0O0OoOo00 = Oo0O0OoOo00
  I1i1I1i1i1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
  for Ii11i1IiII , ooO0OO , time , OooO00oo in I1i1I1i1i1 :
   I11II1i1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OooO00oo )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + Oo0O0OoOo00 + ' - ' + Ii11i1IiII + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + ooO0OO , Oo00OOOOO , ( str ( I11II1i1 ) ) )
   if 63 - 63: oooOo0oo0oo
 I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . Iii
def o0iIiii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 if 73 - 73: IiI1i11I * IiI1i11I + I11i
def ii1i11Ii11iI ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  IiIIi1iIii1I1 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   IiIIi1iIii1I1 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IiIIi1iIii1I1 + '[/COLOR]' , url , 10013 , ooO0OO )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  IiIIi1iIii1I1 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IiIIi1iIii1I1 + '[/COLOR]' , url , 10013 , ooO0OO )
def ii1oo ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + o0ii1I * Iii / i1i1I1IIii1II
 if 18 - 18: i1iIi
 if 92 - 92: oO0o % iI11I1II1I1I / III1iiIii * IiI1i11I . ooOoO0O00 + i1i1I1IIii1II
 if 24 - 24: III1iiIii . IiI1i11I * III1iiIii % Ii . Ii + ooOoO0O00
 if 64 - 64: iI11I1II1I1I / III1iiIii / I1ii11iIi11i - Ii1I
 if 100 - 100: III1iiIii + ooOoO0O00 * oO0o
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  IiIIi1iIii1I1 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IiIIi1iIii1I1 + '[/COLOR]' , url , 10013 , ooO0OO )
   if 64 - 64: i1i1I1IIii1II * Ii . I1ii11iIi11i
def OOo0OO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for oo0OoOooo in IIi :
  ii1iiiiiii = ( oo0OoOooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  i1II11II1 ( 'http:' + ii1iiiiiii )
  if 72 - 72: ii . I11i + o0o00Oo0O
  if 46 - 46: OOooOOo * Iii / i1i1I1IIii1II + I1ii11iIi11i + III1iiIii
  if 95 - 95: I11i - o0ii1I
  if 67 - 67: Ii1I * I1ii11iIi11i % I11i
def iIio00O000ooOO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( iIIIiIi , url , 8046 , ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def O000OOOoOooO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  i1II11II1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 71 - 71: III1iiIii - ooOoO0O00
def oOO00o0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( url )
  if 29 - 29: IIiIiII11i - IiI1i11I / i1i1I1IIii1II % ii % IiI1i11I + III1iiIii
def I1iiIIIi11 ( ) :
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 91 - 91: OOooOOo - OOooOOo . III1iiIii
  if 33 - 33: i1IiiiI1iI - iI11I1II1I1I / o0ii1I % o0o00Oo0O
def o0Oo0oOO00O ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def Oo00OO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , '' )
  if 19 - 19: o0o00Oo0O + o0ii1I * o0ii1I * ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI11Iii1ii111 ( name , url ) :
 i11IIiiI = 0
 name = name
 url = url
 oOOoo00O00o = [ '144' , '240' , '380' , '480' , '720' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  I11iiiiI1i ( url )
  if 66 - 66: i1i1I1IIii1II / Ii / OOooOOo + Ii1I / o0o00Oo0O
  if 97 - 97: Ii
  if 16 - 16: ooOoO0O00
  if 12 - 12: OOooOOo % oooOo0oo0oo + i1i1I1IIii1II . o0o00Oo0O % iI11I1II1I1I
  if 41 - 41: ii
  if 13 - 13: Iii + i1IiiiI1iI - i1IiiiI1iI % i1i1I1IIii1II / Iii
  if 4 - 4: oOo0O0Ooo + oooOo0oo0oo - III1iiIii + IiI1i11I
  if 78 - 78: o0ii1I
def i11Ii ( ) :
 I1i111I = oOOo000oOoO0 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  if 'genre' in oOOo0O00o :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOOo0O00o , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iii1I1I ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 97 - 97: o0o00Oo0O * oooOo0oo0oo % ooOoO0O00 % Ii1I % iI11I1II1I1I
def oooOOoO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  Oo00OO ( url )
  if 31 - 31: Ii / III1iiIii * Ii % i1IiiiI1iI * I1ii11iIi11i + ii
def iIII1iiiiI1Ii11 ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiiIiIi = 'http://documentarylovers.com/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 i1i1IiIiIi1Ii = iIiiiIiIi . lower ( )
 i1iii1I1I ( i1i1IiIiIi1Ii )
 if 69 - 69: Iii / ooOoO0O00 / i1i1I1IIii1II . i1IiiiI1iI
def iII1iiI11IIi ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if 'films' in url :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def i1ii11Iii11 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'films' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def o0ooOO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1i111I )
 for url in IIi :
  if 'rtd' in url :
   OOoo000Ooo ( url )
   if 46 - 46: ooOoO0O00 + o0o00Oo0O
def OOoo000Ooo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I1i111I )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  I11iiiiI1i ( url )
  if 5 - 5: I11i + oOo0O0Ooo / ii % Ii % ii - I11i
  if 53 - 53: oO0o + Ii / iI11I1II1I1I
def i1iI11IiII ( ) :
 II11iIiIIIiI = oOOo000oOoO0 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , II1 in IIi :
  oOoo000 ( ( iIIIiIi + '[COLOR' + ooOoOoo0O + ']' + II1 + '[/COLOR]' ) , oOOo0O00o , 8086 , ooO0OO )
  if 83 - 83: Ii1I
def OOo0OOooO0 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8087 , ooO0OO )
  if 80 - 80: Ii1I
def ooOOOo00Oooo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1i111II ( url , iIIIiIi )
  if 99 - 99: ii - oooOo0oo0oo - I1ii11iIi11i % Ii1I
def I1i111II ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 30 - 30: o0o00Oo0O + IIiIiII11i / Ii
def iiiiOOO00Oo00o ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOOo0O00o , 3002 , 'http://www.solie.org/alibrary/' + ooO0OO )
def IiII1Iiii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def I1o000o00OO00Oo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 I1II11I11111i = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , iIIIiIi in I1II11I11111i :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Season- ' + iIIIiIi + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def I1II1II ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  oooO ( url )
def oooO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 48 - 48: IiI1i11I
def I1iIiIi11i11 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def oOoo00OO0o0O000 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i111I )
 for url in IIi :
  iiI1i ( url )
  if 67 - 67: Ii
def O00oOo00o0o ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classictv.png' )
def I11II ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'mp4' in url :
   I11iiiiI1i ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 5 - 5: ii - III1iiIii / Ii1I % I1ii11iIi11i / i1IiiiI1iI . Ii1I
def OoO000oOO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOOo0O00o , 8071 , iiIi1IIiIi + 'streams.png' )
def iiIiiiIii ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '(Free Access)' in iIIIiIi :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def o0OOoOO0oOO ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , ooO0OO , IIo0o0O0O00oOOo , '' )
  if 51 - 51: iI11I1II1I1I * OOooOOo / o0ii1I * oO0o
def oooo0O00O ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  O000oo00O0o ( 'http://watchxxxfree.com/categories' )
 if O0O00Oo == 1 :
  Ii1 ( 'http://www.perfectgirls.net' )
 if O0O00Oo == 2 :
  iiiiiiiiiiiI ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 3 :
  iI111iiI1II ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 4 :
  iiiiiiiiiiiI ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 5 :
  iiiiiiiiiiiI ( 'http://www.xvideos.com/verified/videos' )
 if O0O00Oo == 6 :
  OOOoooO000O0 ( 'http://www.xvideos.com/tags' )
 if O0O00Oo == 7 :
  OOO0o0OO ( 'http://www.xvideos.com/porn' )
 if O0O00Oo == 8 :
  Ii1iIi ( )
  if 32 - 32: i1i1I1IIii1II . oooOo0oo0oo % oooOo0oo0oo . OOooOOo
  if 37 - 37: oooOo0oo0oo + o0o00Oo0O + oooOo0oo0oo . IiI1i11I . I11i
  if 78 - 78: oOo0O0Ooo / Iii + I11i . I1ii11iIi11i / o0o00Oo0O
  if 49 - 49: Ii1I
  if 66 - 66: I11i . Ii1I
  if 18 - 18: I1ii11iIi11i + III1iiIii
  if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % o0ii1I . oOo0O0Ooo
  if 43 - 43: oOo0O0Ooo % Ii1I * o0ii1I
  if 31 - 31: o0ii1I / IiI1i11I
def iI1111iI1iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'ch' in url :
   o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def o0ooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0OO0OOoo0oO = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for iIIIiIi , url in o0OO0OOoo0oO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OOOOo00oOOO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   II1IoO0Ooo0o00o ( url )
def oOoOOO0oO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def O000oo00O0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , ii11Iiii in IIi :
  if 'category' in url :
   o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   ' + ii11Iiii + '[/COLOR]' , url , 90006 , ooO0OO , iiIi1IIiIi + 'Jizbox.png' , '' )
def iiiI1I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0OO0OOoo0oO = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , ooO0OO , '' , '' )
 for url in o0OO0OOoo0oO :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def O0iIIii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   II1IoO0Ooo0o00o ( url )
def II1IoO0Ooo0o00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def Ii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii11Iiii in IIi :
  if 'category' in url :
   o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]' + ii11Iiii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIii1iI = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0OO0OOoo0oO = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , ooO0OO , '' , '' )
 for url in o0OO0OOoo0oO :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , iIii1iI + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def O00O0oO00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IIi1IIiiI1 ( 'http://www.perfectgirls.net' + url )
def IIi1IIiiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  i1II11II1 ( 'http://' + url )
def OOO0o0OO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii11Iiii in IIi :
  o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + ii11Iiii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def OOOoooO000O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 o0OO0OOoo0oO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in o0OO0OOoo0oO :
  o0OIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii11Iiii in IIi :
  o0OIi ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + ( ii11Iiii + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 66 - 66: IiI1i11I
def oooOIi1IiIi11i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 o0OO0OOoo0oO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in o0OO0OOoo0oO :
  o0OIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , OOoO0Oo in IIi :
  o0OIi ( iIIIiIi + '--' + ( OOoO0Oo ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( ooO0OO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 87 - 87: I11i % I1ii11iIi11i % IIiIiII11i + IiI1i11I * oOo0O0Ooo
  if 18 - 18: i1iIi * IIiIiII11i
def iiiiiiiiiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , OoOo0OO0oooo , IIIioOo0000oOo in IIi :
  o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIioOo0000oOo + ' - [COLORred]' + OoOo0OO0oooo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , ooO0OO , ooO0OO , IIIioOo0000oOo + ' - ' + OoOo0OO0oooo )
 I111IIIIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in I111IIIIi :
  o0OIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 89 - 89: i1iIi . Ii1I / OOooOOo . oO0o / iI11I1II1I1I
def iI111iiI1II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0OO0OOoo0oO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in o0OO0OOoo0oO :
  o0OIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1i1i1I ) )
 for url , iIIIiIi in IIi :
  if '/c/' in url :
   o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 38 - 38: o0o00Oo0O
   if 73 - 73: I1ii11iIi11i % IIiIiII11i / IiI1i11I * i1i1I1IIii1II
def Ii1iIi ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOo0 = ( o0OO00oo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1i1IiIiIi1Ii = oOo0 . lower ( )
 o00O = 'http://www.xvideos.com/?k=' + i1i1IiIiIi1Ii
 print o00O + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( o00O )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi , OoOo0OO0oooo , IIIioOo0000oOo in IIi :
  o0OIi ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIioOo0000oOo + ' - [COLORred]' + OoOo0OO0oooo + '[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10108 , ooO0OO , ooO0OO , IIIioOo0000oOo + ' - ' + OoOo0OO0oooo )
 I111IIIIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in I111IIIIi :
  o0OIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 99 - 99: I1ii11iIi11i + i1IiiiI1iI % i1iIi - I11i
if 52 - 52: Ii1I
if 93 - 93: IiI1i11I . Ii
if 24 - 24: oooOo0oo0oo . oO0o + i1IiiiI1iI . i1i1I1IIii1II - Ii1I % IiI1i11I
if 49 - 49: o0o00Oo0O . I1ii11iIi11i / o0ii1I
if 29 - 29: Ii1I / i1i1I1IIii1II * o0o00Oo0O - Ii - oO0o + o0ii1I
if 86 - 86: oOo0O0Ooo / Ii1I * o0ii1I % Ii
if 20 - 20: IiI1i11I . ii + IiI1i11I + i1iIi * Ii1I
if 44 - 44: Ii
if 69 - 69: oooOo0oo0oo * o0o00Oo0O + Ii
if 65 - 65: o0o00Oo0O / IiI1i11I . ooOoO0O00 * IiI1i11I / iI11I1II1I1I - i1i1I1IIii1II
if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
if 55 - 55: I11i . Ii1I
if 63 - 63: i1i1I1IIii1II
if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
if 60 - 60: i1IiiiI1iI
if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
if 14 - 14: o0ii1I - o0o00Oo0O
if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
if 7 - 7: III1iiIii * i1iIi + OOooOOo
if 22 - 22: IiI1i11I
if 48 - 48: Ii1I . oOo0O0Ooo
if 73 - 73: o0o00Oo0O . i1IiiiI1iI - ii % Iii % ooOoO0O00
if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
if 49 - 49: I1ii11iIi11i
if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
if 9 - 9: III1iiIii . Iii
if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
if 96 - 96: i1iIi % o0o00Oo0O
if 51 - 51: oOo0O0Ooo - IiI1i11I / Ii1I . Ii1I + Ii1I
if 87 - 87: IIiIiII11i . o0ii1I * oO0o
def OOoO00o00oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in ii1I1IIii11 :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
def I1II1i1iIIi ( url ) :
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 import urlresolver
 try : iIIi . play ( url )
 except : pass
 if 55 - 55: oO0o
 if 20 - 20: i1iIi * i1IiiiI1iI * I11i - i1iIi
def i1I1IiiIIIiiI ( ) :
 if 62 - 62: I1ii11iIi11i + ii / IiI1i11I
 if 60 - 60: o0ii1I / OOooOOo . Iii % oooOo0oo0oo
 if 61 - 61: o0o00Oo0O . o0ii1I . o0o00Oo0O * Ii * IIiIiII11i / i1IiiiI1iI
 if 69 - 69: Iii
 if 17 - 17: Iii
 if 38 - 38: i1IiiiI1iI % oooOo0oo0oo
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
 if 44 - 44: Ii1I % III1iiIii
 if 6 - 6: oO0o
 if 82 - 82: iI11I1II1I1I . Iii / III1iiIii / oooOo0oo0oo * IIiIiII11i % i1i1I1IIii1II
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8091 , iiIi1IIiIi + 'gofish.png' )
def o0O00 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def o00OOoo0 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1I11i = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO in i1I11i :
  ooO0OO = ooO0OO
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 70 - 70: oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
def oO000OO0 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 96 - 96: ooOoO0O00 % Ii1I + iI11I1II1I1I
  if 37 - 37: o0o00Oo0O
  if 97 - 97: i1i1I1IIii1II - oO0o + IiI1i11I * o0o00Oo0O
  if 55 - 55: Ii + ooOoO0O00 % IIiIiII11i + Iii % i1iIi
OO0Oo = '{PQ},' ; i1iiiI = '{SC},' ; oOo0iiii11i1 = '{XG},' ; I1iI1Ii1I1Iii1 = '{JP},' ; ii1iOO00O0O00oOOO = '{HW},' ; ii1111iIIiIIi = '{RT},'
def O00OoO0o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OO0oOO0ooO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 oOOo0O00o = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 iIii1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 Oo0O0O000 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoO00ooO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1IIIIiii1i = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0IiiiI111I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0OO00oo
 III1I11i1iIi = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0oo0O0OOO0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 60 - 60: oO0o
 I1IiIIi11I1 = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 I11i1I1Ii11 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 10 - 10: Iii . ii - oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( iIii1iI )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 ooOO = O00O0oOO00O00 ( iIii1iI )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( Oo0O0O000 )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( II1Ii )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 i1iiIiI = O00O0oOO00O00 ( OO0oo0O0OOO0 )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 96 - 96: o0ii1I
 if 73 - 73: i1IiiiI1iI + o0ii1I
 if 53 - 53: oooOo0oo0oo % oO0o - I11i % I1ii11iIi11i / o0o00Oo0O - Ii1I
 if 32 - 32: OOooOOo % o0o00Oo0O % Ii - i1iIi . oOo0O0Ooo
 if 24 - 24: i1i1I1IIii1II % I11i / i1IiiiI1iI + I11i
 if 59 - 59: IIiIiII11i % oOo0O0Ooo * o0o00Oo0O . ii - ii % o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
 if 28 - 28: ooOoO0O00 / Iii . I11i
 IiI1IIIII1I = O00O0oOO00O00 ( I11i1I1Ii11 )
 if 11 - 11: I1ii11iIi11i * ii - Ii
 if i1iiIiI != 'Failed' :
  I11Oo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iiIiI )
  for oOOo0O00o , iIIIiIi in I11Oo0oO00 :
   IiiI1III1I1 = O00O0oOO00O00 ( oOOo0O00o )
   o0OoOoo00O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiiI1III1I1 )
   for i1iii1ii , II1 in o0OoOoo00O :
    II1 = ( II1 . replace ( '.' , ' ' ) )
    if i1i1IiIiIi1Ii in II1 . lower ( ) :
     if '.mkv' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 222 , '' , '' , '' )
     elif '.mp4' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 222 , '' , '' , '' )
     elif '.avi' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 222 , '' , '' , '' )
     elif '.wav' in i1iii1ii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in i1Iii1i1I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , oOOo0O00o , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for o0oo00o0O0O00 , iIIIiIi in ii1I1IIii11 :
   if o0OO00oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Oo0O0O000 + o0oo00o0O0O00 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in II1i11I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , oOOo0O00o , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 3 - 3: Ii1I
    if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
    if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
    if 37 - 37: IiI1i11I + i1IiiiI1iI * o0ii1I + III1iiIii
    if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + o0ii1I / IIiIiII11i
    if 66 - 66: i1iIi + i1i1I1IIii1II % ii
    if 23 - 23: i1i1I1IIii1II . OOooOOo + iI11I1II1I1I
    if 17 - 17: III1iiIii
    if 12 - 12: ooOoO0O00 . oO0o
    if 14 - 14: oooOo0oo0oo + IIiIiII11i % oooOo0oo0oo . i1i1I1IIii1II * i1iIi
    if 54 - 54: i1iIi * Iii - i1IiiiI1iI
    if 15 - 15: IiI1i11I / o0o00Oo0O
    if 61 - 61: ooOoO0O00 / ooOoO0O00 + i1iIi . i1IiiiI1iI * i1iIi
    if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
    if 82 - 82: o0o00Oo0O / IiI1i11I * oO0o - Iii + I1ii11iIi11i
    if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + o0ii1I * IIiIiII11i
    if 78 - 78: i1IiiiI1iI - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
    if 97 - 97: ooOoO0O00
    if 29 - 29: oOo0O0Ooo
    if 37 - 37: Ii1I * i1IiiiI1iI * oOo0O0Ooo * o0o00Oo0O
    if 35 - 35: oOo0O0Ooo - Ii1I * IiI1i11I + III1iiIii / ooOoO0O00
    if 46 - 46: I1ii11iIi11i . i1iIi % I1ii11iIi11i / IIiIiII11i * i1iIi * oooOo0oo0oo
    if 59 - 59: i1IiiiI1iI * IiI1i11I
    if 31 - 31: Iii / o0o00Oo0O
    if 57 - 57: ooOoO0O00 % i1iIi
    if 69 - 69: I11i
    if 69 - 69: i1IiiiI1iI
    if 83 - 83: iI11I1II1I1I . I11i + i1IiiiI1iI . ii / i1iIi + IIiIiII11i
    if 90 - 90: o0ii1I * IiI1i11I / oooOo0oo0oo
    if 68 - 68: OOooOOo
    if 65 - 65: i1i1I1IIii1II
    if 82 - 82: I11i
    if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + i1IiiiI1iI
    if 65 - 65: o0ii1I
    if 71 - 71: i1IiiiI1iI % i1IiiiI1iI . i1i1I1IIii1II + Ii - Ii
    if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / i1IiiiI1iI - Ii . i1iIi / oooOo0oo0oo
    if 13 - 13: I11i % o0o00Oo0O - i1IiiiI1iI * ii / I1ii11iIi11i - ii
    if 78 - 78: i1i1I1IIii1II % ii
    if 73 - 73: oOo0O0Ooo % i1iIi % III1iiIii + ooOoO0O00 - ii / i1i1I1IIii1II
    if 78 - 78: ii % i1i1I1IIii1II - Ii
 oo0O0o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
 for oO0ooOO in oo0O0o :
  IIi1iI1 = oO0 + oO0ooOO + oOoOooOo0o0
  i1iiIiI = O00O0oOO00O00 ( IIi1iI1 )
  if i1iiIiI != 'Failed' :
   I11Oo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iiIiI )
   for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in I11Oo0oO00 :
    if o0OO00oo in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , 222 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 23 - 23: i1iIi - o0o00Oo0O + Ii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 98 - 98: ii
 oo0O0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 61 - 61: I11i . III1iiIii . o0o00Oo0O + ii + o0o00Oo0O
 if 65 - 65: ooOoO0O00 * oooOo0oo0oo * ii - III1iiIii . IiI1i11I - oO0o
 for oO0ooOO in oo0O0o :
  IIi1iI1 = OO0oOO0ooO + oO0ooOO
  IIiIi11iiIi = O00O0oOO00O00 ( IIi1iI1 )
  if IIiIi11iiIi != 'Failed' :
   i11iI11I1I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( IIiIi11iiIi )
   for o0oo00o0O0O00 , iIIIiIi in i11iI11I1I :
    if o0OO00oo in iIIIiIi . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO0oOO0ooO + oO0ooOO + o0oo00o0O0O00 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 71 - 71: o0ii1I * OOooOOo
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % i1IiiiI1iI * I11i
def OoOoO ( ) :
 if 64 - 64: i1iIi / i1iIi + Ii1I * oooOo0oo0oo % oooOo0oo0oo
 if 87 - 87: oO0o * I1ii11iIi11i
 if 83 - 83: ooOoO0O00 * i1IiiiI1iI - III1iiIii / o0ii1I
 if 48 - 48: i1i1I1IIii1II . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
 if 32 - 32: o0ii1I * oOo0O0Ooo - oooOo0oo0oo . I1ii11iIi11i / o0o00Oo0O + o0ii1I
 if 67 - 67: OOooOOo % I1ii11iIi11i
 if 7 - 7: Ii % Ii1I / i1IiiiI1iI % I1ii11iIi11i - oO0o
 if 73 - 73: Ii1I
 if 92 - 92: Ii + o0o00Oo0O * Iii
 if 60 - 60: I11i / I1ii11iIi11i
 if 19 - 19: iI11I1II1I1I . oO0o / ii
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % i1IiiiI1iI / Ii1I
 if 76 - 76: oO0o * i1i1I1IIii1II - oO0o
 if 57 - 57: ii / OOooOOo + i1i1I1IIii1II . o0ii1I
 if 14 - 14: Ii % oooOo0oo0oo * I11i * OOooOOo
 if 55 - 55: i1IiiiI1iI * oooOo0oo0oo * i1IiiiI1iI
 if 70 - 70: o0o00Oo0O . o0ii1I
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 if 33 - 33: oooOo0oo0oo * o0ii1I
 if 64 - 64: Ii . iI11I1II1I1I
 i1iii1ii = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o0OO00oo ) . replace ( ' ' , '+' )
 iIii1iI = 'http://onlinemovies.tube/?s=' + ( o0OO00oo ) . replace ( ' ' , '+' )
 Oo0O0O000 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1IIIIiii1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 7 - 7: OOooOOo % i1iIi + OOooOOo - OOooOOo * Ii % oO0o
 III1I11i1iIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OO0oo0O0OOO0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 57 - 57: oooOo0oo0oo / oO0o + Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % oooOo0oo0oo + III1iiIii . oO0o . I1ii11iIi11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 70 - 70: Iii . Ii1I * i1i1I1IIii1II
 if 97 - 97: i1i1I1IIii1II . iI11I1II1I1I - oooOo0oo0oo
 oo0o = O00O0oOO00O00 ( i1iii1ii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iIii1iI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0O0O000 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( II1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 IIiIi11iiIi = O00O0oOO00O00 ( I1IIIIiii1i )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 23 - 23: Ii1I % Iii
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 ooOO = O00O0oOO00O00 ( III1I11i1iIi )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iiIiI = O00O0oOO00O00 ( OO0oo0O0OOO0 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 99 - 99: i1IiiiI1iI - Ii1I - oOo0O0Ooo - i1IiiiI1iI + oO0o + IIiIiII11i
 if 34 - 34: i1IiiiI1iI * Iii
 if i1iiIiI != 'Failed' :
  I11Oo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iiIiI )
  for oOOo0O00o , iIIIiIi in I11Oo0oO00 :
   IiiI1III1I1 = O00O0oOO00O00 ( oOOo0O00o )
   o0OoOoo00O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiiI1III1I1 )
   for i1iii1ii , II1 in o0OoOoo00O :
    if i1i1IiIiIi1Ii in II1 . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + II1 + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + i1iii1ii , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 31 - 31: III1iiIii . i1i1I1IIii1II
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if ooOO != 'Failed' :
  IiiIiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in IiiIiI1I1 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 40 - 40: o0ii1I - Iii / IIiIiII11i * ooOoO0O00 + III1iiIii * IIiIiII11i
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - i1IiiiI1iI
    if 99 - 99: o0ii1I - III1iiIii - ooOoO0O00 / Ii . III1iiIii
    if 58 - 58: oooOo0oo0oo
    if 12 - 12: oOo0O0Ooo . I11i * ii
    if 64 - 64: OOooOOo + III1iiIii - ooOoO0O00 . IIiIiII11i . oO0o
    if 31 - 31: i1i1I1IIii1II . IiI1i11I - Iii . iI11I1II1I1I + Iii . OOooOOo
    if 86 - 86: Ii1I - Ii1I / IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
    if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - III1iiIii
    if 30 - 30: ii % oooOo0oo0oo
    if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - oooOo0oo0oo
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oo0OoOOooO = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for oOOo0O00o , ooO0OO , iIIIiIi , o0o0OO0o00o0O in i1Iii1i1I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    if 'season' in o0o0OO0o00o0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in o0o0OO0o00o0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
  for oOOo0O00o in oo0OoOOooO :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 81 - 81: IiI1i11I % o0ii1I . i1iIi
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OoO00oo00 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi , ooO0OO in OoO00oo00 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOOo0O00o , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 66 - 66: Ii1I * o0ii1I / ii * o0o00Oo0O % oooOo0oo0oo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * o0ii1I / i1IiiiI1iI * ii
    if 82 - 82: I1ii11iIi11i / o0ii1I / o0ii1I % o0ii1I
    if 20 - 20: i1iIi
    if 63 - 63: iI11I1II1I1I . oO0o
    if 100 - 100: ooOoO0O00 * ooOoO0O00
    if 26 - 26: oooOo0oo0oo . oO0o % OOooOOo
    if 94 - 94: III1iiIii
    if 15 - 15: o0ii1I - III1iiIii / o0o00Oo0O
    if 28 - 28: i1IiiiI1iI . ooOoO0O00 / Ii1I
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Oo0O0O000 + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 77 - 77: Ii / i1IiiiI1iI / Ii % OOooOOo - i1IiiiI1iI
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( II1Ii + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 80 - 80: i1IiiiI1iI % OOooOOo . ii . IIiIiII11i % III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if IIiIi11iiIi != 'Failed' :
  i11iI11I1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiIi11iiIi )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in i11iI11I1I :
   if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , OO0o0o0oo0O , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 6 - 6: i1IiiiI1iI % III1iiIii / o0ii1I + i1IiiiI1iI . i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: iI11I1II1I1I / o0ii1I
 oOOoOOO0oo0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oO0ooOO in oOOoOOO0oo0 :
  IIi1iI1 = oO0 + oO0ooOO + oOoOooOo0o0
  O0OoOOOo0Oo = O00O0oOO00O00 ( IIi1iI1 )
  if O0OoOOOo0Oo != 'Failed' :
   O0oo0O0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OoOOOo0Oo )
   for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in O0oo0O0 :
    if i1i1IiIiIi1Ii in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 61 - 61: o0o00Oo0O * I11i + i1IiiiI1iI - oooOo0oo0oo . oOo0O0Ooo - III1iiIii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 7 - 7: Ii1I
     if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0oooooO ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o0OO00oo ) . replace ( ' ' , '+' )
 if 97 - 97: oooOo0oo0oo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 99 - 99: Iii % i1IiiiI1iI . o0o00Oo0O * III1iiIii
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOOo0O00o ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 87 - 87: o0ii1I % Ii1I * I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
OOO00i111 = '{ZH},' ; Ii1i = '{IX},' ; i1i1I111iI = '{LM},'
if 20 - 20: oO0o / Ii * I11i - Ii1I - IIiIiII11i / Ii
def IIIII1i1I ( url ) :
 OOo0Oo = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OOo0Oo )
 for url , OOo , o0OOOOoO , iIIIiIi in IIi :
  oOoo000 ( ( OOo ) . replace ( 'Sezon' , ' Season ' ) + ( o0OOOOoO ) . replace ( 'Bölüm' , ' Episode ' ) + iIIIiIi , url , 8063 , '' )
  if 24 - 24: OOooOOo * o0ii1I
  if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
  if 81 - 81: oooOo0oo0oo
  if 58 - 58: IIiIiII11i . i1IiiiI1iI . o0ii1I * ii / o0ii1I / Iii
def i1iI11I ( url ) :
 OOo0Oo = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( OOo0Oo )
 for url , iIIIiIi in IIi :
  OooOo00o ( iIIIiIi , url , 222 , '' )
  if 96 - 96: I1ii11iIi11i
  if 34 - 34: i1i1I1IIii1II - Ii1I
  if 10 - 10: oooOo0oo0oo . o0ii1I
  if 5 - 5: III1iiIii - Iii
def I1iOoO00O ( ) :
 if 87 - 87: i1iIi - Ii / iI11I1II1I1I % oOo0O0Ooo
 OOo0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOo0Oo )
 for oOOo0O00o , ooO0OO , iIIIiIi , o0OOOOoO in IIi :
  oOoo000 ( iIIIiIi + '  -  ' + ( o0OOOOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 8063 , ooO0OO )
  if 56 - 56: oOo0O0Ooo
def ii1i11III1I1 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8002 , ooO0OO )
def O000o ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , time , url , iIIIiIi , iI1i11i in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , time ) , url , 1015 , ooO0OO , iI1i11i )
  if 44 - 44: IIiIiII11i
def IIiiiiiiII ( ) :
 if 80 - 80: Iii
 oOoo000 ( 'Coronation Street' , '' , 8001 , '' )
 oOoo000 ( 'Eastenders' , '' , 8002 , '' )
 oOoo000 ( 'Emmerdale' , '' , 8003 , '' )
 oOoo000 ( 'Hollyoaks' , '' , 8004 , '' )
 oOoo000 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 94 - 94: III1iiIii - o0o00Oo0O * oO0o * oO0o % i1iIi - IIiIiII11i
 if 70 - 70: ii
 if 70 - 70: I11i
 if 6 - 6: Ii + ii % Ii . Iii * ii - I1ii11iIi11i
def ooooOo00O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Holly' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 17 - 17: ii % o0ii1I % o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
def O000o0O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'East' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 51 - 51: i1iIi * o0ii1I * ii % OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: iI11I1II1I1I * ii * o0ii1I - ooOoO0O00
def IIIo00o ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Emmer' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 48 - 48: i1IiiiI1iI % i1iIi . I1ii11iIi11i + oO0o - i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: III1iiIii . iI11I1II1I1I - IIiIiII11i - o0ii1I
def oOOOo0O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Coro' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 86 - 86: IIiIiII11i - ii - i1iIi % IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: i1iIi + I1ii11iIi11i + ii
def OooOooO0OoOoo0o ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Celeb' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 27 - 27: oO0o % i1iIi - o0o00Oo0O
def IIIIi1i ( name , url ) :
 IIiI111i = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIiI111i :
  i1III1i = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i111I = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I1i111I ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i111I = open_url ( url )
  Iii1iI11 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I1i111I ) [ - 1 ]
  i1III1i = Iii1iI11 . replace ( '\\/' , '/' )
 i1i1II1i11 = xbmcgui . ListItem ( name , '' , '' )
 i1i1II1i11 . setPath ( i1III1i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i1II1i11 )
 if 33 - 33: i1iIi * ii
 if 14 - 14: IIiIiII11i + o0o00Oo0O - IiI1i11I
def II1i1 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for oOOo0O00o , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 58 - 58: Ii - OOooOOo
def OOO0o0oo00 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Movies' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOOo0O00o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def o000IIIi1IiI1iII ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . i1i1I1IIii1II + Ii
  if 12 - 12: III1iiIii + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
def IIiiI ( url ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
i1I11Iiii = '{UJ},' ; oOOOoOo0oOoo = '{WE},' ; OoOOOO0 = '{WP},' ; Iii1iii11 = '{PP},'
def Ii11 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II11i1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  IIIi1IIiI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIi1IIiI ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: ii - oOo0O0Ooo - oOo0O0Ooo % oOo0O0Ooo % oO0o
 if 98 - 98: o0o00Oo0O + o0o00Oo0O
 if 34 - 34: III1iiIii
def iIiIIiII11i1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '(cooltvseries.com)' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , iIIIiIi in i1Iii1i1I :
  if '(cooltvseries.com)' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def i1Iii ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  i1II11II1 ( ( url ) . replace ( ' ' , '%20' ) )
oOOooo = '{XX},' ; IiI11IiIIi = '{UD},' ; oOOo0OoooOo = '{YT},' ; I1I1IiIiIIi1I = '{JS},' ; oo0Ooo = '{PF},'
if 21 - 21: Ii1I - i1i1I1IIii1II * oO0o
def oO00oOOOO ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOOo0O00o ) ) , 222 , ooO0OO )
  if 54 - 54: Iii * ii
def oO0o00 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'youtu' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 71 - 71: I11i + ii * IIiIiII11i / i1IiiiI1iI
def o000OOO000o ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 71 - 71: i1IiiiI1iI - IiI1i11I % o0o00Oo0O
def i1I1111iI ( url ) :
 I1i111I = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 64 - 64: o0o00Oo0O + oOo0O0Ooo . IIiIiII11i - i1IiiiI1iI * o0ii1I % o0ii1I
  if 21 - 21: I11i * I11i + o0o00Oo0O
  if 73 - 73: I11i / IiI1i11I % o0o00Oo0O . ooOoO0O00
  if 99 - 99: IIiIiII11i - Ii1I * III1iiIii
  if 3 - 3: III1iiIii - Ii1I * IiI1i11I * Ii1I + I1ii11iIi11i
def IIi1i1iI11I11 ( ) :
 if 67 - 67: Ii % Iii
 oOoo000 ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 13 - 13: Ii - i1iIi
 if 54 - 54: oOo0O0Ooo * oOo0O0Ooo - Iii . o0o00Oo0O . IiI1i11I - o0ii1I
def OooooO00OOO0 ( Cat_Name ) :
 if 8 - 8: Ii1I - ooOoO0O00 - i1i1I1IIii1II / i1i1I1IIii1II % I11i
 OOO0OoO00oOo = False
 IiIoOo = '0'
 if Cat_Name == 'All Channels' : OOO0OoO00oOo = True
 if Cat_Name == 'Entertainment' : IiIoOo = '1'
 if Cat_Name == 'Movies' : IiIoOo = '2'
 if Cat_Name == 'Music' : IiIoOo = '3'
 if Cat_Name == 'News' : IiIoOo = '4'
 if Cat_Name == 'Sports' : IiIoOo = '5'
 if Cat_Name == 'Documentary' : IiIoOo = '6'
 if Cat_Name == 'Kids' : IiIoOo = '7'
 if Cat_Name == 'Food' : IiIoOo = '8'
 if Cat_Name == 'Religious' : IiIoOo = '9'
 if Cat_Name == 'USA Channels' : IiIoOo = '10'
 if Cat_Name == 'Other' : IiIoOo = '11'
 if 49 - 49: I11i * o0ii1I + I1ii11iIi11i
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i111I )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for iIIIiIi , ooO0OO , IIIii in IIi :
  oooOoO00Oo00o0O = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  if IIIii == IiIoOo :
   oOoo000 ( iIIIiIi , '' , 7022 , oooOoO00Oo00o0O )
  elif OOO0OoO00oOo == True :
   oOoo000 ( iIIIiIi , '' , 7022 , oooOoO00Oo00o0O )
  else : pass
  if 14 - 14: iI11I1II1I1I . oO0o + I11i * i1i1I1IIii1II . OOooOOo % I11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 58 - 58: i1IiiiI1iI % Ii1I - OOooOOo . IIiIiII11i
def OO0ooO0oOOoo ( Search_Name ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , oOOo0O00o , iIii1iI , Oo0O0O000 in IIi :
  oooOoO00Oo00o0O = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  OooOo00o ( Search_Name + ': Link 1' , ( oOOo0O00o ) . replace ( '\\' , '' ) , 222 , oooOoO00Oo00o0O )
  OooOo00o ( Search_Name + ': Link 2' , ( iIii1iI ) . replace ( '\\' , '' ) , 222 , oooOoO00Oo00o0O )
  OooOo00o ( Search_Name + ': Link 3' , ( Oo0O0O000 ) . replace ( '\\' , '' ) , 222 , oooOoO00Oo00o0O )
  if 97 - 97: Iii
def O0oOO0o0 ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def O000000oooOOo ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def I11iiI1 ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 45 - 45: Iii . i1i1I1IIii1II - i1iIi . IiI1i11I / III1iiIii
def oooiIi11 ( url ) :
 url
 ooo00Ooo = xbmcgui . ListItem ( iIIIiIi , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 return
 if 62 - 62: OOooOOo + o0ii1I . o0o00Oo0O . oooOo0oo0oo % IiI1i11I
 if 28 - 28: I1ii11iIi11i . IiI1i11I % o0o00Oo0O - OOooOOo
def oo0OOO0O0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i111I )
 for url , O000OOO , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + ooO0OO , '' , ( O000OOO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . III1iiIii / i1i1I1IIii1II
def i1ii1iIiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , O000OOO , ooO0OO in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + ooO0OO , '' , O000OOO )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 O0OoO0oOOoo0 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIoOoOo0OoOOoo in O0OoO0oOOoo0 :
  I1i11 = ( IiIoOoOo0OoOOoo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + ooO0OO , '' , I1i11 )
  if 25 - 25: i1iIi % OOooOOo . i1i1I1IIii1II
def IIiIiI1IIi ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 3 - 3: i1IiiiI1iI / Iii % i1iIi % ii . IiI1i11I
 if 97 - 97: IIiIiII11i . o0o00Oo0O / i1iIi
 if 83 - 83: o0ii1I / ii * i1i1I1IIii1II . oOo0O0Ooo . ooOoO0O00
def O00 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( iIIIiIi ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def O00OooOOo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 9032 , iiIi1IIiIi + 'icon.png' )
def oOO0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   OooOo00o ( ( iIIIiIi ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def IIIiiiIi1I1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   OooOo00o ( iIIIiIi , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 10 - 10: oO0o - IIiIiII11i % I11i - OOooOOo + oO0o
   if 88 - 88: iI11I1II1I1I % i1iIi + I11i * OOooOOo / Iii . oO0o
   if 66 - 66: iI11I1II1I1I * IIiIiII11i . iI11I1II1I1I * Ii + Iii + o0ii1I
def OoO0ooooOOo0o ( url ) :
 IIIIi1I ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , ooO0OO , url in IIi :
  if 'music' in url :
   IIIIi1I ( iIIIiIi , url , 90036 , ooO0OO , ooO0OO , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   IIIIi1I ( iIIIiIi , url , 90039 , ooO0OO , ooO0OO , '' , '' )
def iIii1iii1I1ii ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , ooO0OO , ooO0OO , '' , '' )
  if 91 - 91: ooOoO0O00
def iIiIiiiII11i ( url ) :
 IIIIi1I ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , iIIIiIi in IIi :
  oO0O = requests . get ( url ) . text
  I1oO0oO00OO00 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO0O )
  for iiiIIiIi in I1oO0oO00OO00 :
   OO0o00 = requests . get ( iiiIIiIi ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0o00 )
   for O0OO00000o00 , oOO00OoOo , i1iII1IiiIiI1 , o0OOoOooO0ooO , iiI111I1iIiI in IIi :
    if O0OO00000o00 == 'xyz' :
     OOooo000 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( iIIIiIi , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     OOooo000 = 'http://' + o0OOoOooO0ooO + '.' + i1iII1IiiIiI1 + '.' + oOO00OoOo + '.' + O0OO00000o00 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( iIIIiIi , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
 for I1iiii1I in OOo0 :
  IIIIi1I ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1000111 , '' , '' , '' , '' )
  if 52 - 52: iI11I1II1I1I / IiI1i11I . o0o00Oo0O * III1iiIii . oOo0O0Ooo
  if 67 - 67: IIiIiII11i + o0ii1I - oOo0O0Ooo * i1iIi
  if 19 - 19: Ii * I1ii11iIi11i
def iii1Ii ( ) :
 IIIIi1I ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 59 - 59: oO0o * o0o00Oo0O . iI11I1II1I1I . Iii * IiI1i11I
 if 71 - 71: I11i . oooOo0oo0oo * Ii1I - o0ii1I
def ooOOooooo0Oo ( url , name ) :
 IIIIi1I ( name , '' , '' , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , name in IIi :
  oO0O = requests . get ( url ) . text
  I1oO0oO00OO00 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO0O )
  for iiiIIiIi in I1oO0oO00OO00 :
   OO0o00 = requests . get ( iiiIIiIi ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0o00 )
   for O0OO00000o00 , oOO00OoOo , i1iII1IiiIiI1 , o0OOoOooO0ooO , iiI111I1iIiI in IIi :
    if O0OO00000o00 == 'xyz' :
     OOooo000 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     OOooo000 = 'http://' + o0OOoOooO0ooO + '.' + i1iII1IiiIiI1 + '.' + oOO00OoOo + '.' + O0OO00000o00 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
     if 32 - 32: i1iIi / IIiIiII11i . o0o00Oo0O . i1iIi % oOo0O0Ooo - I11i
 for I1iiii1I in OOo0 :
  IIIIi1I ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1003111 , '' , '' , '' , '' )
  if 69 - 69: o0ii1I - oOo0O0Ooo * oooOo0oo0oo . iI11I1II1I1I * OOooOOo . ii
  if 6 - 6: o0o00Oo0O . I11i - OOooOOo
def Ii1i11IIiI ( ) :
 IIIIi1I ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 27 - 27: OOooOOo + o0ii1I + IiI1i11I / III1iiIii
 if 92 - 92: Iii / oOo0O0Ooo * iI11I1II1I1I / i1iIi + III1iiIii
 if 30 - 30: i1i1I1IIii1II . Ii / Iii + ooOoO0O00 - Iii
def iIII ( url , name ) :
 IIIIi1I ( name , '' , '' , '' , '' , '' , '' )
 IIIIi1I ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , name in IIi :
  oO0O = requests . get ( url ) . text
  I1oO0oO00OO00 = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( oO0O )
  for iiiIIiIi in I1oO0oO00OO00 :
   OO0o00 = requests . get ( iiiIIiIi ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OO0o00 )
   for O0OO00000o00 , oOO00OoOo , i1iII1IiiIiI1 , o0OOoOooO0ooO , iiI111I1iIiI in IIi :
    if O0OO00000o00 == 'xyz' :
     OOooo000 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     OOooo000 = 'http://' + o0OOoOooO0ooO + '.' + i1iII1IiiIiI1 + '.' + oOO00OoOo + '.' + O0OO00000o00 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , OOooo000 , 1001111 , ooO0OO , ooO0OO , '' , '' )
     if 41 - 41: o0ii1I * Iii
 for I1iiii1I in OOo0 :
  IIIIi1I ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1005111 , '' , '' , '' , '' )
def O00oo0ooO ( name , url ) :
 import urlresolver
 try :
  iiIii1ii = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iiIii1ii , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 13 - 13: I1ii11iIi11i * I11i * IiI1i11I
 if 71 - 71: oooOo0oo0oo + ii + iI11I1II1I1I
 if 99 - 99: oO0o - III1iiIii * III1iiIii + i1i1I1IIii1II / IiI1i11I + oooOo0oo0oo
def Oo0oOO ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Daily' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 9008 , O0O )
def ii1oO0Oo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iIi1IIIi1Ii ( url ) :
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 29 - 29: iI11I1II1I1I % OOooOOo % Ii1I / OOooOOo - Ii
def o00OOOo0O0O0o0 ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if '.m3u' in oOOo0O00o :
   oOoo000 ( ( iIIIiIi ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOOo0O00o ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def Oo0ooo0oOo0Oo0O ( url ) :
 I1i111I = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 11 - 11: I1ii11iIi11i * ooOoO0O00 * oooOo0oo0oo . oO0o . IiI1i11I
def Ii1I11ii1i ( ) :
 I1i111I = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'category' in oOOo0O00o :
   oOoo000 ( iIIIiIi , 'http://www.disclose.tv/' + oOOo0O00o , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 63 - 63: o0o00Oo0O . i1IiiiI1iI / i1IiiiI1iI / iI11I1II1I1I + oooOo0oo0oo . Iii
   if 59 - 59: oO0o - iI11I1II1I1I % i1i1I1IIii1II
def I11I1iIiI1I ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( iIIIiIi , 'http://www.disclose.tv/' + url , 7011 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 83 - 83: Ii + iI11I1II1I1I
  if 21 - 21: I11i / Ii % i1IiiiI1iI
def OOooO00O0oo0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'http' in url :
   OooOo00o ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , iIIIiIi in i1Iii1i1I :
  OooOo00o ( iIIIiIi , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in ii1I1IIii11 :
  OooOo00o ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 12 - 12: ii * oooOo0oo0oo * Ii1I * i1iIi
  if 26 - 26: ii . ooOoO0O00 + oO0o
def Ii1I11II1IiI ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 67 - 67: iI11I1II1I1I % III1iiIii
def oOo0O0O0oOo ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OO0o00Iii1111Ii1iI = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O00o000O0 = len ( OO0o00Iii1111Ii1iI )
 if 58 - 58: I11i * ooOoO0O00
 if 2 - 2: i1i1I1IIii1II % IiI1i11I % ooOoO0O00 / I1ii11iIi11i . OOooOOo . I1ii11iIi11i
 if O00o000O0 == 1 :
  for Oo0o00 in OO0o00Iii1111Ii1iI :
   Oo0o00 = Oo0o00 . replace ( 'player' , 'watch' )
   ooo00oOo = Oo0o00 + '&fv=&sou='
   oOO0ooO00oO = OooOoooOo ( ooo00oOo )
   i1iI1Ii = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( oOO0ooO00oO )
   for iIi1IiI in i1iI1Ii :
    iI11IiIi1I11 = False
    Resolve ( iIi1IiI )
    if 78 - 78: iI11I1II1I1I + oO0o + Ii
 elif O00o000O0 > 1 :
  if 21 - 21: I1ii11iIi11i + o0ii1I % i1iIi + OOooOOo % Iii
  for Oo0o00 in OO0o00Iii1111Ii1iI :
   iiiiI = OooOoooOo ( Oo0o00 )
   OoOooOo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iiiiI )
   I1iIiiIiiIIiI = OoOooOo0
   I1iIiiIiiIIiI = ( str ( I1iIiiIiiIIiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + I1iIiiIiiIIiI
   OooOo00o ( 'DOUBLE LINK' , I1iIiiIiiIIiI , 424 , '' )
   if 7 - 7: oOo0O0Ooo / i1iIi % oO0o + i1i1I1IIii1II . I11i / Iii
   for url in OoOooOo0 :
    oOoo000 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iIii1iI = Google . resolve ( url )
    except :
     pass
    try :
     O0oo0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iIii1iI ) )
     for I111iI , OO00o0O in O0oo0O :
      if 26 - 26: ii
      HD_URLS . append ( I111iI )
      SD_URLS . append ( OO00o0O )
    except :
     pass
 else :
  pass
  if 66 - 66: Iii + I11i
def ooOo0o ( ) :
 if 84 - 84: ii . oO0o / OOooOOo * ooOoO0O00
 if 6 - 6: iI11I1II1I1I * iI11I1II1I1I
 oOoo000 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 77 - 77: oooOo0oo0oo % i1i1I1IIii1II + iI11I1II1I1I * o0ii1I . III1iiIii . I1ii11iIi11i
 oOoo000 ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 29 - 29: Ii1I + ii . oO0o . ooOoO0O00 - ii * Ii
 if 19 - 19: Ii1I * o0o00Oo0O - i1iIi
def I1iI1 ( ) :
 I1i111I = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , 'http://cnfstudio.com/genre/' + oOOo0O00o , 7003 , iiIi1IIiIi + 'icon.png' )
  if 46 - 46: i1IiiiI1iI % o0o00Oo0O % oO0o * III1iiIii % i1IiiiI1iI % IIiIiII11i
iIii1 = xbmcgui . Dialog ( )
if 20 - 20: ii * i1IiiiI1iI
i1ii1iiI11ii1II1 = '{UN},' ; IIi1oo0oOOo0 = '{IG},' ; oOOi1Ii = '{PL},' ; O0Oo0 = '{LO},' ; Oo000 = '{LP},' ; ooo0Oo00000oooO = '{HA},' ; iIiiiiIi111I = '{XD},' ; ooOo00oOOOO0 = '{TA},' ; iii1IiIiII1 = '{DP},' ; O00oo00O0OO0ooO = '{JT},' ; iIi1I = '{JJ},' ; OO0O0ooOo = '{MM},' ; iI11 = '{FQ},' ; iI1ii111II = '{HH},'
if 77 - 77: Ii1I
def Ii1ii1i1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i111I )
 oo0oO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , ooO0OO )
 oo0oO = oo0oO
 for url in oo0oO :
  oOoo000 ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 11 - 11: I11i * oO0o
def oO0IiiI1i1i11I1 ( url ) :
 if 97 - 97: OOooOOo - oO0o
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  OoooOOOoO0 = O0OO0 ( iiI111I1iIiI )
  OO0oO0o0oOO = O0OO0 ( url )
  if 13 - 13: oOo0O0Ooo / o0ii1I / Iii * o0o00Oo0O
  if 59 - 59: ii . I1ii11iIi11i
def O0OO0 ( url ) :
 if 76 - 76: o0ii1I + oO0o * i1iIi % oO0o
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  iiI1i ( url )
  if 56 - 56: III1iiIii % i1i1I1IIii1II
  if 10 - 10: ooOoO0O00 % IIiIiII11i / Ii1I - i1i1I1IIii1II % I1ii11iIi11i - IiI1i11I
def ii1I11i1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 65 - 65: ooOoO0O00
def IiIIiI ( ) :
 if os . path . exists ( II ) :
  Iii11i = open ( II , 'r' )
  for ooo00Ooo in Iii11i :
   iI111i = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooo00Ooo )
   for iIIIiIi , oOOo0O00o in iI111i :
    OooOo00o ( iIIIiIi , oOOo0O00o , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 98 - 98: ooOoO0O00 + i1IiiiI1iI - Ii1I . ii / o0o00Oo0O / IiI1i11I
def Oo0oOo0Ooo ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = oOOo000oOoO0 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , url in IIi :
   url = ( url ) . strip ( )
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 44 - 44: ooOoO0O00
  if 10 - 10: IIiIiII11i * ii * ii
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOOo0O00o
 iIIIiIi = 'plugin.video.GenieTv'
 if 47 - 47: OOooOOo - i1IiiiI1iI + III1iiIii . IIiIiII11i / i1i1I1IIii1II / Ii
 iiI11IIii ( oOOo0O00o , iIIIiIi )
 if 19 - 19: ooOoO0O00 / o0ii1I / OOooOOo . oOo0O0Ooo / o0ii1I % I11i
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOOo0O00o
 iIIIiIi = 'repository.GenieTv'
 if 39 - 39: i1iIi - ii
 iiI11IIii ( oOOo0O00o , iIIIiIi )
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
 if 74 - 74: i1iIi - Ii
def OoO ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  I1I1iI ( )
 if O0O00Oo == 1 :
  ii1IiIiIi ( )
  if 85 - 85: IIiIiII11i % i1iIi + IIiIiII11i - OOooOOo
  if 40 - 40: OOooOOo - III1iiIii - III1iiIii
  if 26 - 26: oooOo0oo0oo + ooOoO0O00 + Ii1I
  if 81 - 81: oooOo0oo0oo . o0o00Oo0O * I11i + Ii - OOooOOo . i1IiiiI1iI
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
III1IiiI1i1 = 'https://addons.tvaddons.ag/'
if 23 - 23: oO0o / I11i
def ii1IiIiIi ( ) :
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 o00O = 'https://addons.tvaddons.ag/search/?keyword=' + i1i1IiIiIi1Ii
 II11iIiIIIiI = OooOoooOo ( o00O )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , o000O000 , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , oOOo0O00o , 10054 , 'https://addons.tvaddons.ag/' + o000O000 , Oo00OOOOO , '' )
  if 22 - 22: oooOo0oo0oo - oO0o . Iii
  if 89 - 89: i1IiiiI1iI
def I1I1iI ( ) :
 II11iIiIIIiI = OooOoooOo ( III1IiiI1i1 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if 'Repositories' in iIIIiIi :
   pass
  elif 'Services' in iIIIiIi :
   pass
  elif 'International' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10053 , 'https://addons.tvaddons.ag/' + ooO0OO , Oo00OOOOO , '' )
   if 19 - 19: III1iiIii + i1IiiiI1iI
   if 65 - 65: o0ii1I - i1i1I1IIii1II + ooOoO0O00 + oooOo0oo0oo % IiI1i11I
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOo0 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  if 'Please' in iIIIiIi :
   pass
  else :
   Ii1I1i ( iIIIiIi , url , 10054 , 'https://addons.tvaddons.ag/' + ooO0OO , Oo00OOOOO , '' )
 for url in OOo0 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 5 - 5: oO0o / IiI1i11I / oooOo0oo0oo
  if 70 - 70: OOooOOo - Iii + i1iIi / Ii / oOo0O0Ooo % iI11I1II1I1I
def OOOOO0oOooo0O ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
   try :
    os . remove ( I11ii1IIiIi )
   except :
    pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OoOOo0OOoO
   print '======================================='
   extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
   OOOOo0o00OO0000 ( )
   if 97 - 97: ii . Ii1I % I11i % oooOo0oo0oo - I11i - ii
def iiI11IIii ( url , name ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 OOOOo0o00OO0000 ( )
 if 12 - 12: Iii
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
 if 41 - 41: Iii . Ii1I
def Oo00o0Ooo0OOo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 1007 , o000O000 )
def i1IiiIi1i ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , o000O000 )
  if 92 - 92: o0ii1I / oooOo0oo0oo % oooOo0oo0oo % o0o00Oo0O % Iii
def iiI1iii1I111 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  I11I1 ( iIIIiIi , 100109 , oOOo0O00o , image = iiiI1I1iIIIi1 , isFolder = True )
  if 66 - 66: Ii
def OoOI1 ( url ) :
 import random
 II11iiii = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 II11iiii . clear ( )
 O000o0Ooo = [ ]
 OOOOoo = [ ]
 IiIIi1iIii1I1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIii1iI , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  O000o0Ooo . append ( [ iIii1iI , iIIIiIi ] )
  if len ( O000o0Ooo ) == len ( IIi ) :
   for ooo00Ooo in O000o0Ooo :
    ooO00oOOo = random . randint ( 1 , len ( O000o0Ooo ) )
    try :
     iII1I11ii1III = O000o0Ooo [ int ( ooO00oOOo ) ]
    except :
     pass
    if len ( OOOOoo ) <= 20 :
     if iII1I11ii1III [ 1 ] not in IiIIi1iIii1I1 :
      o0o = OooOoooOo ( iII1I11ii1III [ 0 ] )
      ii1I1IIii11 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for IIii1iIIiII , i11i1II in ii1I1IIii11 :
       OOoOoo = OooOoooOo ( IIii1iIIiII )
       II1i11I = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for OO0ooo00oO , iiI111I1iIiI in II1i11I :
        if 'panda' in iiI111I1iIiI :
         IiIi1iiii = OooOoooOo ( iiI111I1iIiI )
         Oo0Oo0O = re . compile ( "url: '(.+?)'" ) . findall ( IiIi1iiii )
         for ooOOO000 in Oo0Oo0O :
          if 'http' in ooOOO000 :
           i1i1II1i11 = xbmcgui . ListItem ( iII1I11ii1III [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : iII1I11ii1III [ 1 ] } )
           i1i1II1i11 . setProperty ( "IsPlayable" , "true" )
           II11iiii . add ( ooOOO000 , i1i1II1i11 )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1i1II1i11 )
           if 88 - 88: III1iiIii / iI11I1II1I1I - Iii + OOooOOo + I11i
def I11I1 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 oOoooO0 = sys . argv [ 0 ]
 oOoooO0 += '?mode=' + str ( mode )
 oOoooO0 += '&title=' + urllib . quote_plus ( name )
 oOoooO0 += '&image=' + urllib . quote_plus ( image )
 oOoooO0 += '&page=' + str ( page )
 if url != '' :
  oOoooO0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  oOoooO0 += '&keyword=' + urllib . quote_plus ( keyword )
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  i1i1II1i11 . addContextMenuItems ( contextMenu )
 if infoLabels :
  i1i1II1i11 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  i1i1II1i11 . setProperty ( "IsPlayable" , "true" )
 i1i1II1i11 . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = isFolder )
 if 28 - 28: i1iIi + ooOoO0O00 * oO0o . o0ii1I + i1iIi
 if 41 - 41: Ii1I . OOooOOo - III1iiIii * i1IiiiI1iI
def I1IIIiI1I1ii1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iconimage , O000OOO , IIo0o0O0O00oOOo , name in IIi :
  if 'http' in url :
   if '.php' in url :
    IIi11i1II = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for ooo00Ooo in IIi11i1II :
     if ooo00Ooo == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoiiI1 ( name , url , 1016 , iconimage , IIo0o0O0O00oOOo , O000OOO )
   else :
    if 'youtube' in url :
     IIi11i1II = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in IIi11i1II :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OOoo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , IIo0o0O0O00oOOo , O000OOO )
    else :
     IIi11i1II = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in IIi11i1II :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OOoo ( name , url , 222 , iconimage , IIo0o0O0O00oOOo , O000OOO )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  else :
   iIIiI ( url , iconimage , name )
   if 62 - 62: oO0o
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
  for url , o000O000 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     oOoo000 ( name , url , 1016 , o000O000 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OooOo00o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 )
     else :
      IIi11i1II = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in IIi11i1II :
       if ooo00Ooo == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OooOo00o ( name , url , 222 , o000O000 )
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   else :
    iIIiI ( url , o000O000 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 8 - 8: Ii1I * III1iiIii / I1ii11iIi11i
def iIIiI ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OOo0O0Oo000OO = ( url ) . replace ( Ii1i , 'http' ) . replace ( IiI11IiIIi , '.com' ) ;
 o0OoI1 = ( OOo0O0Oo000OO ) . replace ( i1i1I111iI , 'a' ) . replace ( oOo0iiii11i1 , 'b' ) . replace ( I1iI1Ii1I1Iii1 , 'c' ) . replace ( oOOOoOo0oOoo , 'd' ) . replace ( oOOi1Ii , 'e' ) . replace ( O00oo00O0OO0ooO , 'f' ) ;
 OooOo0o0Oo0 = ( o0OoI1 ) . replace ( oOOooo , 'g' ) . replace ( ooo0Oo00000oooO , 'h' ) . replace ( oOOo0OoooOo , 'i' ) . replace ( oo0Ooo , 'j' ) . replace ( ii1iOO00O0O00oOOO , 'k' ) . replace ( ii1111iIIiIIi , 'l' ) ;
 i11iI1i11I111 = ( OooOo0o0Oo0 ) . replace ( oo0iIiIII1Ii , 'm' ) . replace ( O0oOoiIII1Ii1 , 'n' ) . replace ( I1111i1I , 'o' ) . replace ( OOoooOO0o , 'p' ) . replace ( O00oo0Ooo , 'q' ) . replace ( iIiI , 'r' ) ;
 iIi1Iii = ( i11iI1i11I111 ) . replace ( OoOO0OooOoooo , 's' ) . replace ( OoOOOO0 , 't' ) . replace ( IIIiiiIii1111Ii1I1 , 'u' ) . replace ( O00o00oOOo , 'v' ) . replace ( I1oO , 'w' ) . replace ( Oo0o0O0oO0o , 'x' ) ;
 iiIi = ( iIi1Iii ) . replace ( oo0O0 , 'y' ) . replace ( oooO000oO0O , 'z' ) . replace ( i1ii1iiI11ii1II1 , '.' ) . replace ( IIi1oo0oOOo0 , '(' ) . replace ( O0Oo0 , ')' ) . replace ( Oo000 , '/' ) ;
 I1iIIiiII = ( iiIi ) . replace ( OOO00i111 , '1' ) . replace ( Iii1iii11 , '2' ) . replace ( o0ooo0ooo0 , '3' ) . replace ( ooOo00oOOOO0 , '4' ) . replace ( iii1IiIiII1 , '5' ) . replace ( I1I1IiIiIIi1I , '6' ) ;
 IIi1Ii1I = ( I1iIIiiII ) . replace ( iIi1I , '7' ) . replace ( OO0O0ooOo , '8' ) . replace ( iI11 , '9' ) . replace ( iI1ii111II , '0' ) . replace ( OO0Oo , ':' ) . replace ( i1iiiI , '%' ) ;
 url = ( IIi1Ii1I ) . replace ( i1I11Iiii , '-' ) . replace ( iIiiiiIi111I , '_' ) ;
 OooOo00o ( name , url , 222 , iconimage ) ;
 if 49 - 49: Ii - iI11I1II1I1I % o0o00Oo0O % IiI1i11I * i1iIi - III1iiIii
 if 8 - 8: iI11I1II1I1I * I1ii11iIi11i
def iIiiI ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for oOOo0O00o , o000O000 , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1007 , o000O000 )
def iIiI11iiI ( url ) :
 if 48 - 48: OOooOOo
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , o000O000 )
  if 28 - 28: Iii / o0o00Oo0O * III1iiIii - i1IiiiI1iI % III1iiIii
def I11I1o00oOo0O0O0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ii1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 if 14 - 14: oOo0O0Ooo % OOooOOo . Ii1I
 if 45 - 45: oO0o + oOo0O0Ooo
def O0OIIII1i ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if '-dir-' in iIIIiIi :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , ooO0OO )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , ooO0OO )
   if 82 - 82: I1ii11iIi11i . Ii + Ii
def OOoI1I ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 O0oOO = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '[To Parent Directory]' in iIIIiIi :
   iIIIiIi = 'HOME'
   pass
  elif 'HOME' in iIIIiIi :
   pass
  elif '.m3u' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , O0oOO + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , O0oOO + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , O0oOO + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , O0oOO + url , 1012 , iiIi1IIiIi + 'music.png' )
def OOOOooO ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 19 - 19: Iii . iI11I1II1I1I + i1iIi
def Iii11Ii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 O0oOO = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '.mp3' in iIIIiIi :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/' , '' ) , O0oOO + url , 1011 , iiIi1IIiIi + 'music.png' )
def IiiiIiiI1IIIi ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , ( 'http://www.cyn.net/music/' + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + ooO0OO ) . replace ( ' ' , '%20' ) )
def OOO0O0oOOoO ( url , img ) :
 I1i111I = oOOo000oOoO0 ( url )
 iIii1iI = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( iIii1iI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 2 - 2: IiI1i11I + oOo0O0Ooo * oO0o + III1iiIii / oO0o . i1IiiiI1iI
def Oo0OOOO0oOoo0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 iIii1iI = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for type , url , iIIIiIi in IIi :
  if '[VID]' in type :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iIii1iI + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   Oo0OOOO0oOoo0 ( iIii1iI + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: o0o00Oo0O % I11i
 if 3 - 3: Ii / oooOo0oo0oo + i1i1I1IIii1II
def i1I1Iiii ( ) :
 OO0oOO0ooO = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o0OO00oo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1IiIiIi1Ii = o0OO00oo . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 i1iii1ii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iIii1iI = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 10 - 10: oO0o . oO0o + o0o00Oo0O
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 oo0o = O00O0oOO00O00 ( i1iii1ii )
 o0o = O00O0oOO00O00 ( iIii1iI )
 if 13 - 13: ooOoO0O00 . oOo0O0Ooo
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , OO0o0o0oo0O , iIIIiIi in IIi :
   if o0OO00oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
    if 45 - 45: i1iIi % Iii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OoO00oo00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi in OoO00oo00 :
   if o0OO00oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 37 - 37: IiI1i11I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if o0OO00oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 70 - 70: o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * I11i - I1ii11iIi11i - i1iIi
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: ooOoO0O00 + III1iiIii / ii - i1i1I1IIii1II / oooOo0oo0oo / OOooOOo
    if 55 - 55: oooOo0oo0oo
    if 5 - 5: Iii / OOooOOo
    if 48 - 48: ooOoO0O00 - i1i1I1IIii1II . ii - oO0o - ooOoO0O00
    if 19 - 19: i1i1I1IIii1II % o0ii1I + Ii1I . IIiIiII11i * Ii
    if 87 - 87: o0ii1I / i1IiiiI1iI % OOooOOo * Ii1I - ii / OOooOOo
oo0iIiIII1Ii = '{SF},' ; O0oOoiIII1Ii1 = '{IF},' ; I1111i1I = '{PW},' ; o0ooo0ooo0 = '{AM},' ; OOoooOO0o = '{GF},' ; O00oo0Ooo = '{DD},' ; iIiI = '{UO},' ; OoOO0OooOoooo = '{LE},' ; IIIiiiIii1111Ii1I1 = '{ZY},' ; O00o00oOOo = '{UE},' ; I1oO = '{PE},' ; Oo0o0O0oO0o = '{JE},' ; oo0O0 = '{TH},' ; oooO000oO0O = '{LK},'
if 24 - 24: Iii . oooOo0oo0oo * ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
if 62 - 62: I11i % IIiIiII11i
def iII1111III1I ( ) :
 I1i111I = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 8021 , iiIi1IIiIi + 'iwatch.png' )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def iII1i1iii ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i111I )
 for url , iIIIiIi , iiIIiiI in IIi :
  oOoo000 ( iIIIiIi + iiIIiiI , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def OO0iIi1ii111i ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  II11IIi ( url )
def II11IIi ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i111I )
 II1i11I = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( 'VidSpot - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  OooOo00o ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , iIIIiIi in II1i11I :
  OooOo00o ( 'VidUp' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for iIIIiIi , url in ii1I1IIii11 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OooOo00o ( 'TheVideo - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 94 - 94: oooOo0oo0oo % I1ii11iIi11i . i1IiiiI1iI
def ooOoOoOoOoO ( ) :
 I1i111I = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1021 , iiIi1IIiIi + 'anime.png' )
  if 9 - 9: o0ii1I - o0o00Oo0O / IIiIiII11i * III1iiIii % OOooOOo
  if 76 - 76: oO0o + i1IiiiI1iI + oO0o * ii
def o0OO00IIiIi ( ) :
 I1i111I = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1002 , iiIi1IIiIi + 'anime.png' )
  if 60 - 60: I11i / Ii1I / oooOo0oo0oo % Iii
  if 84 - 84: Ii1I * Ii1I . oO0o % i1i1I1IIii1II - oOo0O0Ooo
  if 32 - 32: IiI1i11I - IiI1i11I / oO0o % iI11I1II1I1I / Ii1I / III1iiIii
def iI1III1ii1 ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  oOOOo0Oooo = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  oOoo000 ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 1003 , oOOOo0Oooo )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiI111iiII ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   O00oOI11I1iI ( url )
  elif 'playpanda' in url :
   O00oOI11I1iI ( url )
   if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00oOI11I1iI ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 99 - 99: Ii1I % I1ii11iIi11i
  if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
def O0ooOOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 84 - 84: III1iiIii
def oOOo000oOoO0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 42 - 42: o0o00Oo0O . i1IiiiI1iI / Iii
def oO00ooo0oOoo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoOO0ooo0O = ( '%s%s' % ( ii1IIi1IIIIi1 , url ) )
 iiI111I1iIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , o000O000 , iIIIiIi in IIi :
  OooOo00o ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , o000O000 )
  if 53 - 53: oO0o % iI11I1II1I1I - oooOo0oo0oo
def iii11i ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  Ooo0oO0 ( url , iIIIiIi )
 else :
  I11iiiiI1i ( url )
def I11iiiiI1i ( url ) :
 import urlresolver
 try :
  iiIii1ii = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( iiIii1ii , xbmcgui . ListItem ( iIIIiIi ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iIIIiIi ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def iiI1i ( url ) :
 if 100 - 100: o0ii1I
 OO0ooo0o0 = open ( OOOO0OOoO0O0 , "a" )
 OO0ooo0o0 . write ( 'url="' + url + '"\n' )
 OO0ooo0o0 . close
 if 84 - 84: Iii * i1iIi + Ii + IiI1i11I - IIiIiII11i
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 import urlresolver
 try : iIIi . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iIIIiIi ) )
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIIi . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def Ooo0oO0 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  oOoO = '.mp4'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.mkv' in url :
  oOoO = '.mkv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.mp3' in url :
  oOoO = '.mp3'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.avi' in url :
  oOoO = '.avi'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.mov' in url :
  oOoO = '.mov'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.mpeg' in url :
  oOoO = '.mpeg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.mpg' in url :
  oOoO = '.mpg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.flv' in url :
  oOoO = '.flv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 elif '.wmv' in url :
  oOoO = '.wmv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   Oo0ooO ( url , name , oOoO )
 else :
  I11iiiiI1i ( url )
def Oo0ooO ( url , name , cat ) :
 o00o0o0O0 ( )
 o00oo0 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , file )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def o00o0o0O0 ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def i1II1IiiiIii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 o0oOoO00o . update ( 100 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 iIIi . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 32 - 32: ooOoO0O00
def i1II11II1 ( url ) :
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIi . play ( url ) . strip ( )
 except : pass
 if 76 - 76: IIiIiII11i % i1iIi - Ii1I
def IiiIOO ( url ) :
 iIIi = xbmc . Player ( ooO00O00oOO ( ) )
 import urlresolver
 iiI1iii1I = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iIIi . play ( iiI1iii1I )
 xbmc . sleep ( 1 )
 iIIi . play ( url )
 if 77 - 77: IiI1i11I / Ii
 if 20 - 20: o0o00Oo0O . Iii
def ooO00O00oOO ( ) :
 try :
  oOO0ooOO = getSet ( "core-player" )
  if ( oOO0ooOO == 'DVDPLAYER' ) : IiiI11iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOO0ooOO == 'MPLAYER' ) : IiiI11iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOO0ooOO == 'PAPLAYER' ) : IiiI11iI = xbmc . PLAYER_CORE_PAPLAYER
  else : IiiI11iI = xbmc . PLAYER_CORE_AUTO
 except : IiiI11iI = xbmc . PLAYER_CORE_AUTO
 return IiiI11iI
 return True
 if 88 - 88: IIiIiII11i % ii - ooOoO0O00 - oO0o * Iii
def oOoo000 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOO000O = [ ]
  oOO000O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = True )
 return o0Oo0
 if 37 - 37: o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
def o0OIi ( name , url , mode , iconimage , fanart , description ) :
 if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = True )
 return o0Oo0
 if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
def OooOo00o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOO000O = [ ]
  oOO000O . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = False )
 return o0Oo0
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
 if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
 if 63 - 63: Ii1I % i1iIi % Ii1I
 if 71 - 71: o0ii1I
def iI11OO ( url , heading , announce ) :
 class IiIiII ( ) :
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
   try : O0oO0 = open ( announce ) ; I1Ii1i11I1I = O0oO0 . read ( )
   except : I1Ii1i11I1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1Ii1i11I1I ) )
   return
 IiIiII ( )
 IiIiII ( )
def o0OIiII ( heading , announce ) :
 class IiIiII ( ) :
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
   try : O0oO0 = open ( announce ) ; I1Ii1i11I1I = O0oO0 . read ( )
   except : I1Ii1i11I1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1Ii1i11I1I ) )
   return
 IiIiII ( )
 IiIiII ( )
def iIiIi11 ( ) :
 iI11OO ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 99 - 99: ii - ooOoO0O00 % I11i / I11i + III1iiIii
 if 96 - 96: ii + oooOo0oo0oo - i1IiiiI1iI / i1i1I1IIii1II % i1i1I1IIii1II
 if 34 - 34: III1iiIii
 if 55 - 55: Ii1I
 if 79 - 79: oooOo0oo0oo + I11i % IiI1i11I . i1i1I1IIii1II
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 49 - 49: o0ii1I + Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
 if 61 - 61: Iii / oooOo0oo0oo
 if 85 - 85: OOooOOo - Iii . OOooOOo . OOooOOo
 if 62 - 62: III1iiIii % ii * oO0o + oO0o % o0ii1I % IiI1i11I
 if 66 - 66: oOo0O0Ooo . oooOo0oo0oo - oO0o % I1ii11iIi11i * I11i - i1i1I1IIii1II
 if 68 - 68: Iii - Ii / I11i + i1iIi / oOo0O0Ooo
 if 31 - 31: i1IiiiI1iI . ii . ooOoO0O00
 if 65 - 65: oO0o . i1iIi
 if 12 - 12: i1IiiiI1iI + o0o00Oo0O - i1i1I1IIii1II . III1iiIii
 if 46 - 46: III1iiIii . i1iIi / IiI1i11I
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
 if 92 - 92: oO0o % i1iIi * o0o00Oo0O % iI11I1II1I1I / ooOoO0O00 / OOooOOo
 if 67 - 67: i1IiiiI1iI + Iii + i1IiiiI1iI . oooOo0oo0oo % I11i / i1iIi
 if 78 - 78: Ii1I . o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * o0o00Oo0O / Iii * oOo0O0Ooo . Iii
 if 54 - 54: Ii % ooOoO0O00 + I1ii11iIi11i / OOooOOo
 if 26 - 26: Iii . Ii1I
 if 55 - 55: OOooOOo * i1IiiiI1iI % oO0o - oO0o
 if 34 - 34: o0o00Oo0O * oO0o - i1i1I1IIii1II - III1iiIii * o0ii1I . IIiIiII11i
 if 28 - 28: o0o00Oo0O % IiI1i11I - ooOoO0O00
 if 49 - 49: i1iIi . Iii - iI11I1II1I1I
 if 41 - 41: i1iIi * Ii % i1iIi . i1i1I1IIii1II
 if 97 - 97: i1i1I1IIii1II - IiI1i11I + III1iiIii . OOooOOo + iI11I1II1I1I
 if 75 - 75: i1iIi + i1iIi . i1IiiiI1iI % IiI1i11I / iI11I1II1I1I * IiI1i11I
def IiIi1iIIiII1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 3 - 3: ooOoO0O00
def oOO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOOi1I1IIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 16 - 16: I1ii11iIi11i % III1iiIii
def ooOo00Oo0o000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOo0ooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 24 - 24: I1ii11iIi11i + Iii
def I1iii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOoo0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 25 - 25: o0o00Oo0O + oooOo0oo0oo / IiI1i11I
def oO0ooooooO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Ii1iIi1IiiiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 65 - 65: III1iiIii . oooOo0oo0oo % IiI1i11I / o0o00Oo0O
def ooooo0OOO0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 79 - 79: oO0o
def i1Ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 14 - 14: i1iIi
def IIiIII ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiiiiiiiI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 16 - 16: IiI1i11I / IIiIiII11i + oOo0O0Ooo . IIiIiII11i - IiI1i11I
def ooo00OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1iIIIiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 41 - 41: ii + i1iIi + oOo0O0Ooo + IIiIiII11i * o0ii1I
def ooO0O0O0ooOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + i1IIIii1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , OoO000O in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , OoO000O )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 70 - 70: III1iiIii
 if 78 - 78: I1ii11iIi11i * oooOo0oo0oo % Ii1I + oooOo0oo0oo % o0ii1I + III1iiIii
 if 58 - 58: ii % i1IiiiI1iI / I1ii11iIi11i % ii * OOooOOo . ii
 if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
 if 30 - 30: i1i1I1IIii1II - o0ii1I % o0ii1I
 if 8 - 8: III1iiIii
 if 68 - 68: III1iiIii . ii - Ii + Ii
 if 81 - 81: OOooOOo + IiI1i11I . Ii
def oOoo00 ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( o0 ) :
     III1Ii1 = 0
     III1Ii1 += len ( o00oOOo0Oo )
     if III1Ii1 > 0 :
      for O0oO0 in o00oOOo0Oo :
       os . unlink ( os . path . join ( I111IiI11 , O0oO0 ) )
  o0Oo00OoO000O = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( o0Oo00OoO000O )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 39 - 39: oO0o + ii * iI11I1II1I1I . III1iiIii * Ii1I
 if 90 - 90: I1ii11iIi11i
 if 58 - 58: i1iIi - i1i1I1IIii1II . I1ii11iIi11i % IIiIiII11i
 if 47 - 47: oooOo0oo0oo + III1iiIii + oOo0O0Ooo / i1i1I1IIii1II
 if 4 - 4: oOo0O0Ooo . Ii % Iii + IIiIiII11i - o0ii1I - o0o00Oo0O
 if 23 - 23: OOooOOo / oooOo0oo0oo
 if 84 - 84: oooOo0oo0oo / iI11I1II1I1I - Ii1I . o0ii1I
 if 27 - 27: III1iiIii * ooOoO0O00 + IIiIiII11i . iI11I1II1I1I - Ii
def ii11ii1iIiI1 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 29 - 29: oooOo0oo0oo - Ii % III1iiIii / ii
def Ii1I1iIiiI1 ( url ) :
 o000OOo0 = os . path . join ( oooOOOOO , 'addon_data' )
 Oo00 = [
 ( o000OOo0 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( o000OOo0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o000OOo0 , 'plugin.video.itv' , 'Images' ) ) ]
 if 26 - 26: oOo0O0Ooo * ii / oOo0O0Ooo . o0o00Oo0O . i1iIi + o0o00Oo0O
 O0OI1i = 0
 if 50 - 50: Iii . Ii1I
 for ooo00Ooo in Oo00 :
  if os . path . exists ( ooo00Ooo ) and not ooo00Ooo in [ oo0o0O00 , o000OOo0 ] :
   for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( ooo00Ooo ) :
    III1Ii1 = 0
    III1Ii1 += len ( o00oOOo0Oo )
    if III1Ii1 > 0 :
     for O0oO0 in o00oOOo0Oo :
      if not O0oO0 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( I111IiI11 , O0oO0 ) )
       except :
        pass
      else : O00Oooo ( 'Ignore Log File: %s' % O0oO0 )
     for o0OOoOooO0ooO in iII1I :
      try :
       shutil . rmtree ( os . path . join ( I111IiI11 , o0OOoOooO0ooO ) )
       O0OI1i += 1
       O00Oooo ( "[Success] cleared %s files from %s" % ( str ( III1Ii1 ) , os . path . join ( ooo00Ooo , o0OOoOooO0ooO ) ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , o0OOoOooO0ooO ) )
  else :
   for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( ooo00Ooo ) :
    for o0OOoOooO0ooO in iII1I :
     if 'cache' in o0OOoOooO0ooO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I111IiI11 , o0OOoOooO0ooO ) )
       O0OI1i += 1
       O00Oooo ( "[Success] wiped %s " % os . path . join ( ooo00Ooo , o0OOoOooO0ooO ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , o0OOoOooO0ooO ) )
       if 31 - 31: iI11I1II1I1I . oooOo0oo0oo * i1iIi . IiI1i11I - o0o00Oo0O . iI11I1II1I1I
 ii11ii1iIiI1 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % O0OI1i )
 if 54 - 54: iI11I1II1I1I / oooOo0oo0oo + i1i1I1IIii1II % OOooOOo * OOooOOo - IIiIiII11i
 if 43 - 43: o0ii1I / i1IiiiI1iI . i1i1I1IIii1II + iI11I1II1I1I
 if 99 - 99: Ii1I
 if 29 - 29: oOo0O0Ooo . III1iiIii
 if 8 - 8: ooOoO0O00 * o0o00Oo0O
 if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
 if 17 - 17: OOooOOo % oOo0O0Ooo
def o00i111iiIiiIiI ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( iI11II ) :
   III1Ii1 = 0
   III1Ii1 += len ( o00oOOo0Oo )
   if 71 - 71: i1IiiiI1iI - oO0o
   if 61 - 61: Ii1I * Ii * i1iIi . Iii
   if III1Ii1 > 0 :
    if 35 - 35: i1IiiiI1iI * I1ii11iIi11i / I11i
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( III1Ii1 ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: i1i1I1IIii1II / ii . o0ii1I + I1ii11iIi11i + III1iiIii / OOooOOo
     for O0oO0 in o00oOOo0Oo :
      os . unlink ( os . path . join ( I111IiI11 , O0oO0 ) )
     for o0OOoOooO0ooO in iII1I :
      shutil . rmtree ( os . path . join ( I111IiI11 , o0OOoOooO0ooO ) )
     iIii1 = xbmcgui . Dialog ( )
     iIii1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iIii1 = xbmcgui . Dialog ( )
    iIii1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 67 - 67: III1iiIii
 if 66 - 66: Ii * IiI1i11I
 if 51 - 51: ii + Iii . IiI1i11I + Ii * IiI1i11I - oO0o
 if 60 - 60: IiI1i11I * iI11I1II1I1I . OOooOOo . I11i / iI11I1II1I1I
 if 36 - 36: ooOoO0O00 . ii - IIiIiII11i - OOooOOo - III1iiIii
 if 53 - 53: Ii1I - IIiIiII11i . Ii
 if 76 - 76: iI11I1II1I1I - I1ii11iIi11i
 if 79 - 79: oOo0O0Ooo * III1iiIii . ii % i1IiiiI1iI * i1IiiiI1iI
 if 17 - 17: i1IiiiI1iI - i1IiiiI1iI . i1i1I1IIii1II / i1IiiiI1iI
def ooO0O00Oo0o ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( iI11II ) :
   III1Ii1 = 0
   III1Ii1 += len ( o00oOOo0Oo )
   if 36 - 36: Ii1I * ooOoO0O00 + iI11I1II1I1I
   if 55 - 55: oOo0O0Ooo . i1IiiiI1iI - oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I * o0ii1I
   if III1Ii1 > 0 :
    if 77 - 77: oooOo0oo0oo
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( III1Ii1 ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: IIiIiII11i % iI11I1II1I1I * o0o00Oo0O . I11i
     for O0oO0 in o00oOOo0Oo :
      os . unlink ( os . path . join ( I111IiI11 , O0oO0 ) )
     for o0OOoOooO0ooO in iII1I :
      shutil . rmtree ( os . path . join ( I111IiI11 , o0OOoOooO0ooO ) )
     iIii1 = xbmcgui . Dialog ( )
     iIii1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iIii1 = xbmcgui . Dialog ( )
    iIii1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 Ii1I1iIiiI1 ( url )
 return
 if 56 - 56: ooOoO0O00 . i1iIi + Iii - Ii
 if 100 - 100: iI11I1II1I1I - ooOoO0O00 . oooOo0oo0oo
 if 73 - 73: i1IiiiI1iI / Iii / Ii - Ii1I % i1iIi
 if 92 - 92: oOo0O0Ooo - I11i % Ii1I / IiI1i11I % i1i1I1IIii1II
 if 43 - 43: I1ii11iIi11i % i1i1I1IIii1II . Ii - o0o00Oo0O
 if 5 - 5: ooOoO0O00 + o0ii1I
 if 38 - 38: oOo0O0Ooo . o0o00Oo0O + oooOo0oo0oo / Ii1I . iI11I1II1I1I - ooOoO0O00
 if 3 - 3: I1ii11iIi11i + i1i1I1IIii1II
 if 65 - 65: oOo0O0Ooo / OOooOOo % oOo0O0Ooo * Ii * ii / Iii
 if 91 - 91: Ii / Ii
def I1I1I ( url , name ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ii11I = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 OooOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OooOo0 ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Ii11I = os . path . join ( o00oo0 , 'advancedsettings.xml' )
   try :
    os . remove ( Ii11I )
    print '=== GenieTv - REMOVING    ' + str ( Ii11I ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   O0OO00000o00 = open ( Ii11I , "w" )
   O0OO00000o00 . write ( iiI111I1iIiI )
   O0OO00000o00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Ii11I ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Ii11I = os . path . join ( o00oo0 , 'advancedsettings.xml' )
  try :
   os . remove ( Ii11I )
   print '=== GenieTv - REMOVING    ' + str ( Ii11I ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  O0OO00000o00 = open ( Ii11I , "w" )
  O0OO00000o00 . write ( iiI111I1iIiI )
  O0OO00000o00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ii11I ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 23 - 23: o0ii1I
def oooOooo0OO ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ii11I = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  O0OO00000o00 = open ( Ii11I ) . read ( )
  if 'zero' in O0OO00000o00 :
   name = '0CACHE'
  elif 'tuxen' in O0OO00000o00 :
   name = 'TUXENS'
  elif 'muckys' in O0OO00000o00 :
   name = 'MUCKYS'
  elif 'p2p1' in O0OO00000o00 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in O0OO00000o00 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in O0OO00000o00 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 91 - 91: oO0o - IIiIiII11i . iI11I1II1I1I . oOo0O0Ooo . oO0o
def OOooOOO0oooO ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ii11I = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  os . remove ( Ii11I )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Ii11I ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 4 - 4: Ii1I * I11i
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
 if 12 - 12: ii % i1i1I1IIii1II
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
 if 79 - 79: o0o00Oo0O
def OOooooO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for IiiIi1I11 , oOo0oooo , IiIIIIiiIIIii , OOO0o in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IiiIi1I11 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IiIIIIiiIIIii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OOO0o )
  inc = inc + 1
  if 29 - 29: oOo0O0Ooo
  if 3 - 3: Iii
  if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
  if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
  if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
  if 53 - 53: o0o00Oo0O
  if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
  if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
  if 27 - 27: oO0o / IiI1i11I . Ii1I
def OOiiIiII ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Ii11I = os . path . join ( o00oo0 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  O0OO00000o00 = open ( Ii11I , "w" )
  O0OO00000o00 . write ( iiI111I1iIiI )
  O0OO00000o00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ii11I ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 11 - 11: oO0o . oO0o . OOooOOo + ooOoO0O00 - oOo0O0Ooo
def ii11iIi1I1i ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Ii11I = os . path . join ( o00oo0 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  O0OO00000o00 = open ( Ii11I , "w" )
  O0OO00000o00 . write ( iiI111I1iIiI )
  O0OO00000o00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ii11I ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 79 - 79: Ii1I + III1iiIii
 if 94 - 94: Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
def IiIIiI1 ( ) :
 try :
  OoOoOoOO0ooO000 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OoOoOoOO0ooO000 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ooI11 = os . path . join ( OoOoOoOO0ooO000 , "source.db" )
    os . unlink ( ooI11 )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 90 - 90: I11i - I1ii11iIi11i / i1iIi / ooOoO0O00 - o0ii1I
 if 43 - 43: Ii - ii % i1iIi
 if 55 - 55: i1i1I1IIii1II % I1ii11iIi11i % III1iiIii
 if 65 - 65: III1iiIii * III1iiIii
 if 60 - 60: i1iIi
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 92 - 92: o0o00Oo0O % III1iiIii
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
 if 1 - 1: oOo0O0Ooo
 if 40 - 40: I11i % Iii % o0o00Oo0O
 if 88 - 88: I11i - i1i1I1IIii1II
 if 73 - 73: IIiIiII11i
 if 7 - 7: o0o00Oo0O / oO0o
def OOOOoO00o0O ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; o0oOoOoooO = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if o0oOoOoooO :
  I1oo0Oo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; I1oo0Oo = xbmc . translatePath ( I1oo0Oo ) ;
  I1OO0Oo0 = os . path . join ( I1oo0Oo , ".." , ".." ) ; I1OO0Oo0 = os . path . abspath ( I1OO0Oo0 ) ; pluginlog ( "freshstart.main_list xbmcPath=" + I1OO0Oo0 ) ; iI1IIiI1 = False
  try :
   for I111IiI11 , iII1I , o00oOOo0Oo in os . walk ( I1OO0Oo0 , topdown = True ) :
    iII1I [ : ] = [ o0OOoOooO0ooO for o0OOoOooO0ooO in iII1I if o0OOoOooO0ooO not in o0oO0 ]
    for iIIIiIi in o00oOOo0Oo :
     try : os . remove ( os . path . join ( I111IiI11 , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iI1IIiI1 = True
      pluginlog ( "Error removing " + I111IiI11 + " " + iIIIiIi )
    for iIIIiIi in iII1I :
     try : os . rmdir ( os . path . join ( I111IiI11 , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Database" , "userdata" ] : iI1IIiI1 = True
      pluginlog ( "Error removing " + I111IiI11 + " " + iIIIiIi )
   if not iI1IIiI1 : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 IiIiII11i1 ( )
 if 39 - 39: I11i % ii - o0o00Oo0O
 if 87 - 87: oOo0O0Ooo * ooOoO0O00 * I1ii11iIi11i / Ii1I - oO0o
 if 44 - 44: I1ii11iIi11i
def iI1I ( ) :
 ii11Ii1Ii = [ ]
 Ii11i1Ii1 = sys . argv [ 2 ]
 if len ( Ii11i1Ii1 ) >= 2 :
  I1I1I1IIi1III = sys . argv [ 2 ]
  IIIiiI1 = I1I1I1IIi1III . replace ( '?' , '' )
  if ( I1I1I1IIi1III [ len ( I1I1I1IIi1III ) - 1 ] == '/' ) :
   I1I1I1IIi1III = I1I1I1IIi1III [ 0 : len ( I1I1I1IIi1III ) - 2 ]
  iIiii1Ii1III = IIIiiI1 . split ( '&' )
  ii11Ii1Ii = { }
  for IiIii111III1 in range ( len ( iIiii1Ii1III ) ) :
   O0o0000O0 = { }
   O0o0000O0 = iIiii1Ii1III [ IiIii111III1 ] . split ( '=' )
   if ( len ( O0o0000O0 ) ) == 2 :
    ii11Ii1Ii [ O0o0000O0 [ 0 ] ] = O0o0000O0 [ 1 ]
    if 96 - 96: III1iiIii
 return ii11Ii1Ii
 if 51 - 51: iI11I1II1I1I
Oo0oOoo00oo0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iIIOOo0O = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oooooO00OOO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OO00OO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oOOoooo0O0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
O000OOO0O0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OOoOo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i1I1i1iII = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOOi1I1IIII = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOo0ooOo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOoo0ooo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Ii1iIi1IiiiIi = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o0o0o = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
I1ii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiiiiiiiI11 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iI1iIIIiIi = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
Oo0oOooOooO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii11IOo0O0oOoo0Ooo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0iii1i = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O00OO00OOOoO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iiI11111II = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
o0O0O0O00o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i1IIIii1Ii1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
ii1IIi1IIIIi1 = base64 . decodestring ( 'Q1VOVA==' )
def IiiI ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 i1i1II1i11 . setProperty ( 'fanart_image' , fanart )
 i1i1II1i11 . setProperty ( "IsPlayable" , "true" )
 ii1i1ii11 = [ ]
 ii1i1ii11 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 ii1i1ii11 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i1i1II1i11 . addContextMenuItems ( ii1i1ii11 , replaceItems = True )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = False )
 return o0Oo0
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOO000O = [ ]
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = True )
 return o0Oo0
 if 42 - 42: Ii
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOoooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0Oo0 = True
 i1i1II1i11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1II1i11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1i1II1i11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOO000O = [ ]
  if showcontext == 'fav' :
   oOO000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oOO000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1i1II1i11 . addContextMenuItems ( oOO000O )
 o0Oo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoooO0 , listitem = i1i1II1i11 , isFolder = False )
 return o0Oo0
 if 41 - 41: oooOo0oo0oo % i1IiiiI1iI * III1iiIii - i1IiiiI1iI
 if 21 - 21: Iii - I1ii11iIi11i
I1I1I1IIi1III = iI1I ( )
oOOo0O00o = None
iIIIiIi = None
O0oOOo0Oo = None
iiiI1I1iIIIi1 = None
IIo0o0O0O00oOOo = None
OoO000O = None
OOOi1II = None
Ooo0o0OoOO = None
if 15 - 15: I11i / III1iiIii / i1iIi * OOooOOo
if 13 - 13: IiI1i11I
try :
 Ooo0o0OoOO = int ( I1I1I1IIi1III [ "fav_mode" ] )
except :
 pass
 if 69 - 69: Ii - Ii + Iii / oOo0O0Ooo % Ii1I
try :
 oOOo0O00o = urllib . unquote_plus ( I1I1I1IIi1III [ "url" ] )
except :
 pass
try :
 iIIIiIi = urllib . unquote_plus ( I1I1I1IIi1III [ "name" ] )
except :
 pass
try :
 iiiI1I1iIIIi1 = urllib . unquote_plus ( I1I1I1IIi1III [ "iconimage" ] )
except :
 pass
try :
 O0oOOo0Oo = int ( I1I1I1IIi1III [ "mode" ] )
except :
 pass
try :
 IIo0o0O0O00oOOo = urllib . unquote_plus ( I1I1I1IIi1III [ "fanart" ] )
except :
 pass
try :
 OoO000O = urllib . unquote_plus ( I1I1I1IIi1III [ "description" ] )
except :
 pass
 if 56 - 56: iI11I1II1I1I / oO0o * oooOo0oo0oo
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O0oOOo0Oo )
print "URL: " + str ( oOOo0O00o )
print "Name: " + str ( iIIIiIi )
print "IconImage: " + str ( iiiI1I1iIIIi1 )
if 91 - 91: Ii
if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
def I1iI1ii1II ( content , viewType ) :
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
if iiiI1I1iIIIi1 == None : iiiI1I1iIIIi1 = O0O
if IIo0o0O0O00oOOo == None : IIo0o0O0O00oOOo = Oo00OOOOO
if O0oOOo0Oo == None :
 Iii1I1I11iiI1 ( )
 if 82 - 82: iI11I1II1I1I
elif O0oOOo0Oo == 1 :
 IiIi1i1 ( oOOo0O00o )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif O0oOOo0Oo == 44 :
 II11IiiIII ( oOOo0O00o )
 if 46 - 46: oOo0O0Ooo
elif O0oOOo0Oo == 2 :
 O0OO00OoO00 ( )
 if 72 - 72: IiI1i11I
elif O0oOOo0Oo == 3 :
 i1IIi111iI ( )
 if 100 - 100: oOo0O0Ooo
elif O0oOOo0Oo == 21 :
 i1i1II ( )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif O0oOOo0Oo == 4 :
 o0oo00oo0oO ( )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
elif O0oOOo0Oo == 5 :
 II11I ( oOOo0O00o )
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif O0oOOo0Oo == 6 :
 o00i111iiIiiIiI ( oOOo0O00o )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif O0oOOo0Oo == 7 :
 I1I1I ( oOOo0O00o , iIIIiIi )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif O0oOOo0Oo == 8 :
 oooOooo0OO ( oOOo0O00o , iIIIiIi )
 if 93 - 93: oO0o . oO0o
elif O0oOOo0Oo == 9 :
 FIXREPOSADDONS ( oOOo0O00o )
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif O0oOOo0Oo == 10 :
 OOOOo0o00OO0000 ( )
 if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif O0oOOo0Oo == 11 :
 OOooOOO0oooO ( oOOo0O00o )
 if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif O0oOOo0Oo == 12 :
 OOooooO ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 55 - 55: i1iIi - I11i
elif O0oOOo0Oo == 13 :
 oOoo00 ( )
 if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif O0oOOo0Oo == 14 :
 Ii1I1iIiiI1 ( oOOo0O00o )
 if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif O0oOOo0Oo == 15 :
 IIi1Ii11iIi ( )
 if 37 - 37: Iii
elif O0oOOo0Oo == 16 :
 OOiiIiII ( oOOo0O00o , iIIIiIi )
 if 19 - 19: ii % i1IiiiI1iI
elif O0oOOo0Oo == 17 :
 ii11iIi1I1i ( oOOo0O00o , iIIIiIi )
 if 57 - 57: OOooOOo + ooOoO0O00 . iI11I1II1I1I . iI11I1II1I1I / iI11I1II1I1I % i1i1I1IIii1II
elif O0oOOo0Oo == 18 :
 IiIIiI1 ( )
 if 7 - 7: Ii * Ii1I / oO0o * i1i1I1IIii1II
elif O0oOOo0Oo == 19 :
 O00O ( oOOo0O00o )
 if 35 - 35: III1iiIii . ooOoO0O00 + Ii1I . III1iiIii + i1iIi . i1i1I1IIii1II
elif O0oOOo0Oo == 40 :
 o0I1IiiiiI1i1I ( iIIIiIi , oOOo0O00o , OoO000O )
 if 2 - 2: IIiIiII11i
elif O0oOOo0Oo == 42 :
 I1i1i1iIi1iIi ( iIIIiIi , oOOo0O00o , OoO000O )
 if 18 - 18: iI11I1II1I1I % Ii1I % I1ii11iIi11i
elif O0oOOo0Oo == 43 :
 iiIII1i1 ( oOOo0O00o )
 if 47 - 47: i1iIi - oOo0O0Ooo % oooOo0oo0oo * o0ii1I % oOo0O0Ooo
elif O0oOOo0Oo == 20 :
 O00Oo ( oOOo0O00o )
 if 95 - 95: oO0o + OOooOOo % I1ii11iIi11i . o0ii1I * oOo0O0Ooo + i1IiiiI1iI
elif O0oOOo0Oo == 22 :
 IiIi1iIIiII1i ( oOOo0O00o )
 if 22 - 22: I1ii11iIi11i . oO0o
elif O0oOOo0Oo == 23 :
 oOO0o ( oOOo0O00o )
 if 55 - 55: I1ii11iIi11i % ii * IIiIiII11i % ii
elif O0oOOo0Oo == 24 :
 ooOo00Oo0o000 ( oOOo0O00o )
 if 30 - 30: i1IiiiI1iI / I11i + ii + OOooOOo + oO0o
elif O0oOOo0Oo == 25 :
 I1iii ( oOOo0O00o )
 if 40 - 40: ii / III1iiIii
elif O0oOOo0Oo == 26 :
 oO0ooooooO ( oOOo0O00o )
 if 82 - 82: Ii - i1i1I1IIii1II - ooOoO0O00
elif O0oOOo0Oo == 27 :
 ooooo0OOO0 ( oOOo0O00o )
 if 78 - 78: i1i1I1IIii1II % IiI1i11I / ooOoO0O00 / i1iIi
elif O0oOOo0Oo == 28 :
 i1Ii1 ( oOOo0O00o )
 if 44 - 44: I11i + o0ii1I + oOo0O0Ooo % o0o00Oo0O
elif O0oOOo0Oo == 29 :
 IIiIII ( oOOo0O00o )
 if 100 - 100: ii
elif O0oOOo0Oo == 30 :
 oo0O00o0 ( oOOo0O00o )
 if 27 - 27: Ii % IIiIiII11i + i1IiiiI1iI
elif O0oOOo0Oo == 31 :
 ooo00OO ( oOOo0O00o )
 if 76 - 76: oooOo0oo0oo - i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo * i1i1I1IIii1II
elif O0oOOo0Oo == 32 :
 iII ( )
 if 93 - 93: Ii * Ii - oOo0O0Ooo + iI11I1II1I1I * Ii
elif O0oOOo0Oo == 33 :
 O0oo ( )
 if 14 - 14: i1iIi . ii . oOo0O0Ooo - III1iiIii + iI11I1II1I1I
elif O0oOOo0Oo == 35 :
 OoOo0O00 ( oOOo0O00o )
 if 47 - 47: oooOo0oo0oo % ooOoO0O00
elif O0oOOo0Oo == 34 :
 iIIi1 ( oOOo0O00o )
 if 23 - 23: o0ii1I * o0ii1I / Iii
elif O0oOOo0Oo == 36 :
 IIIiII11 ( oOOo0O00o )
 if 11 - 11: oooOo0oo0oo
elif O0oOOo0Oo == 37 :
 Iii1Iii ( oOOo0O00o )
 if 58 - 58: oO0o * ii
elif O0oOOo0Oo == 38 :
 IiOOo0 ( oOOo0O00o )
 if 47 - 47: IiI1i11I - I1ii11iIi11i
elif O0oOOo0Oo == 41 :
 OOOOoO00o0O ( I1I1I1IIi1III )
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + Iii / IIiIiII11i + i1iIi
elif O0oOOo0Oo == 39 :
 ooO0O0O0ooOOO ( oOOo0O00o )
 if 26 - 26: o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
elif O0oOOo0Oo == 45 :
 TEXTS ( )
 if 35 - 35: ooOoO0O00 % Ii + o0ii1I
elif O0oOOo0Oo == 46 :
 iIiIi11 ( )
 if 14 - 14: oO0o * ii
elif O0oOOo0Oo == 47 :
 GEVID ( )
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
elif O0oOOo0Oo == 48 :
 iiiI ( iIIIiIi , oOOo0O00o , OoO000O )
 if 97 - 97: Iii % IIiIiII11i % o0ii1I . IIiIiII11i . iI11I1II1I1I
elif O0oOOo0Oo == 49 :
 II1III1I1I1Ii ( )
 if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IiI1i11I
elif O0oOOo0Oo == 22222 :
 iiI1i ( oOOo0O00o )
 if 25 - 25: i1i1I1IIii1II / o0o00Oo0O + i1IiiiI1iI % Ii / oOo0O0Ooo
elif O0oOOo0Oo == 222225 :
 ooi1II1I ( oOOo0O00o )
 if 62 - 62: IiI1i11I . Iii * ooOoO0O00 + IiI1i11I
elif O0oOOo0Oo == 222 :
 iii11i ( oOOo0O00o )
 if 95 - 95: o0ii1I / I11i % i1iIi - oOo0O0Ooo / oooOo0oo0oo * oooOo0oo0oo
elif O0oOOo0Oo == 2222222 :
 I11iiiiI1i ( oOOo0O00o )
 if 6 - 6: oO0o % III1iiIii + iI11I1II1I1I
elif O0oOOo0Oo == 222222 :
 Ooo0oO0 ( oOOo0O00o , iIIIiIi )
 if 18 - 18: IIiIiII11i . o0ii1I + OOooOOo + o0o00Oo0O - Iii
elif O0oOOo0Oo == 333 :
 oO00ooo0oOoo ( oOOo0O00o )
 if 30 - 30: IIiIiII11i
 if 26 - 26: Iii - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * oooOo0oo0oo . ii
elif O0oOOo0Oo == 1020 :
 ooOoOoOoOoO ( )
 if 99 - 99: i1i1I1IIii1II . oO0o / oooOo0oo0oo
elif O0oOOo0Oo == 1021 :
 ANIMEEP ( )
 if 12 - 12: iI11I1II1I1I + i1iIi * i1IiiiI1iI % ii / iI11I1II1I1I
elif O0oOOo0Oo == 1022 :
 ANIMEPLAY ( oOOo0O00o )
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - Ii1I
elif O0oOOo0Oo == 1001 :
 o0OO00IIiIi ( )
 if 8 - 8: OOooOOo / o0ii1I
elif O0oOOo0Oo == 1005 :
 iIiiI ( )
 if 12 - 12: iI11I1II1I1I
elif O0oOOo0Oo == 1007 :
 iIiI11iiI ( oOOo0O00o )
 if 52 - 52: i1i1I1IIii1II . Ii1I + i1i1I1IIii1II
elif O0oOOo0Oo == 1010 :
 O0OIIII1i ( oOOo0O00o )
 if 73 - 73: IIiIiII11i / Ii / i1iIi
elif O0oOOo0Oo == 1011 :
 Iii11Ii ( oOOo0O00o )
 if 1 - 1: IiI1i11I + OOooOOo / III1iiIii - oOo0O0Ooo % oOo0O0Ooo
elif O0oOOo0Oo == 1012 :
 OOoI1I ( oOOo0O00o )
 if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
elif O0oOOo0Oo == 1030 :
 IiiiIiiI1IIIi ( )
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
elif O0oOOo0Oo == 1031 :
 OOO0O0oOOoO ( oOOo0O00o , iiiI1I1iIIIi1 )
 if 30 - 30: Iii
elif O0oOOo0Oo == 1032 :
 Oo0OOOO0oOoo0 ( oOOo0O00o )
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
elif O0oOOo0Oo == 1006 :
 Parse . ParseURL ( oOOo0O00o )
 if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
elif O0oOOo0Oo == 2030 :
 Parse . addonParseURL ( oOOo0O00o )
 if 15 - 15: I11i
elif O0oOOo0Oo == 2031 :
 Parse . apkParseURL ( oOOo0O00o )
 if 55 - 55: Ii / ii - Iii
elif O0oOOo0Oo == 2032 :
 Parse . ParseBOSS ( oOOo0O00o )
 if 89 - 89: Iii - ooOoO0O00 - ooOoO0O00 * oooOo0oo0oo - o0o00Oo0O
elif O0oOOo0Oo == 1002 :
 iI1III1ii1 ( oOOo0O00o )
 if 94 - 94: I1ii11iIi11i / Iii . Ii1I
elif O0oOOo0Oo == 1003 :
 iiI111iiII ( oOOo0O00o , iiiI1I1iIIIi1 )
 if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
elif O0oOOo0Oo == 1004 :
 O00oOI11I1iI ( oOOo0O00o )
 if 72 - 72: i1IiiiI1iI * oO0o + I1ii11iIi11i / o0ii1I % oooOo0oo0oo
elif O0oOOo0Oo == 1008 :
 oO00oOOOO ( )
 if 84 - 84: OOooOOo / I11i
elif O0oOOo0Oo == 1009 :
 Oo0oOo0Ooo ( oOOo0O00o )
 if 9 - 9: o0ii1I
elif O0oOOo0Oo == 2001 :
 IiIIiI ( )
 if 76 - 76: oOo0O0Ooo % I1ii11iIi11i / iI11I1II1I1I - I1ii11iIi11i
elif O0oOOo0Oo == 2002 :
 OOOOooO ( oOOo0O00o )
 if 34 - 34: OOooOOo - ooOoO0O00 + oooOo0oo0oo + o0ii1I . I11i
elif O0oOOo0Oo == 1013 :
 oOO00 ( )
elif O0oOOo0Oo == 10111113 :
 O000oooO0 ( oOOo0O00o )
 if 42 - 42: oO0o
elif O0oOOo0Oo == 1014 :
 ii1i11III1I1 ( )
 if 59 - 59: oO0o . i1IiiiI1iI % oO0o
elif O0oOOo0Oo == 1015 :
 O000o ( oOOo0O00o )
 if 22 - 22: I1ii11iIi11i
elif O0oOOo0Oo == 1016 :
 I1IIIiI1I1ii1 ( oOOo0O00o , iiiI1I1iIIIi1 , iIIIiIi )
 if 21 - 21: I11i
elif O0oOOo0Oo == 1017 :
 oOoO00 ( )
 if 86 - 86: i1iIi / iI11I1II1I1I . oooOo0oo0oo
elif O0oOOo0Oo == 1018 :
 IiiI1iiiiI1iI ( oOOo0O00o )
 if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
elif O0oOOo0Oo == 1019 :
 IiI11i1IIiiI ( oOOo0O00o )
elif O0oOOo0Oo == 10190 :
 OoOo00o0OO ( oOOo0O00o )
 if 30 - 30: OOooOOo . oooOo0oo0oo % oooOo0oo0oo / IIiIiII11i + ooOoO0O00
elif O0oOOo0Oo == 1023 :
 ooOOO ( )
 if 61 - 61: ooOoO0O00 % IIiIiII11i * IIiIiII11i . I11i / Ii1I - i1IiiiI1iI
elif O0oOOo0Oo == 1024 :
 Oo00o0Ooo0OOo ( oOOo0O00o )
 if 93 - 93: o0ii1I - ooOoO0O00
elif O0oOOo0Oo == 1025 :
 i1IiiIi1i ( oOOo0O00o )
 if 3 - 3: i1i1I1IIii1II + oO0o - IiI1i11I / o0ii1I
elif O0oOOo0Oo == 4001 :
 o000oo ( )
 if 58 - 58: o0ii1I * Iii
elif O0oOOo0Oo == 4002 :
 i1i1ii ( )
 if 95 - 95: i1i1I1IIii1II
elif O0oOOo0Oo == 4003 :
 iII1ii11III ( )
 if 49 - 49: oOo0O0Ooo
elif O0oOOo0Oo == 4004 :
 IIIi ( )
 if 23 - 23: i1IiiiI1iI
elif O0oOOo0Oo == 4005 :
 IIi1ii1Ii ( )
 if 5 - 5: Ii1I % OOooOOo . ii . I11i + Ii
elif O0oOOo0Oo == 4006 :
 oOO00O0Ooooo00 ( )
 if 54 - 54: i1iIi - o0o00Oo0O + IiI1i11I
elif O0oOOo0Oo == 4007 :
 Oo0OO0000oooo ( )
 if 34 - 34: o0ii1I - oooOo0oo0oo % IiI1i11I
elif O0oOOo0Oo == 4008 :
 ii1III11 ( )
 if 48 - 48: i1i1I1IIii1II - o0o00Oo0O
elif O0oOOo0Oo == 40099 : I1II1IiI1 ( )
elif O0oOOo0Oo == 4009 : o00OOo ( )
elif O0oOOo0Oo == 4010 : OOooO ( )
elif O0oOOo0Oo == 3000 :
 ii1I11i1 ( )
 if 17 - 17: iI11I1II1I1I . III1iiIii / i1iIi % Iii + I11i - iI11I1II1I1I
elif O0oOOo0Oo == 3001 :
 iiiiOOO00Oo00o ( )
 if 95 - 95: OOooOOo + oooOo0oo0oo - Iii * ooOoO0O00 + ooOoO0O00 * o0o00Oo0O
elif O0oOOo0Oo == 3002 :
 IiII1Iiii ( oOOo0O00o )
 if 60 - 60: I1ii11iIi11i + Iii % iI11I1II1I1I % i1i1I1IIii1II - i1IiiiI1iI / I11i
elif O0oOOo0Oo == 3003 :
 I1o000o00OO00Oo ( oOOo0O00o )
 if 9 - 9: III1iiIii / i1i1I1IIii1II % o0o00Oo0O * i1IiiiI1iI - iI11I1II1I1I % ooOoO0O00
elif O0oOOo0Oo == 3004 :
 I1II1II ( oOOo0O00o )
 if 83 - 83: OOooOOo + oooOo0oo0oo / ii
elif O0oOOo0Oo == 404 :
 I11I1o00oOo0O0O0 ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 )
 if 39 - 39: oO0o % IiI1i11I . i1i1I1IIii1II . IIiIiII11i - Ii
elif O0oOOo0Oo == 405 :
 i1II1IiiiIii ( oOOo0O00o )
 if 85 - 85: o0o00Oo0O - OOooOOo
elif O0oOOo0Oo == 7030 :
 IIi1i1iI11I11 ( )
 if 17 - 17: I11i / ooOoO0O00 / oooOo0oo0oo
elif O0oOOo0Oo == 7021 :
 OooooO00OOO0 ( iIIIiIi )
 if 91 - 91: Ii1I / o0ii1I - OOooOOo . Iii / i1i1I1IIii1II
elif O0oOOo0Oo == 7022 :
 OO0ooO0oOOoo ( iIIIiIi )
 if 16 - 16: III1iiIii % IiI1i11I . i1i1I1IIii1II . oOo0O0Ooo % o0o00Oo0O * Iii
elif O0oOOo0Oo == 7000 :
 oOo0O0O0oOo ( iIIIiIi , oOOo0O00o , img )
 if 99 - 99: OOooOOo / ii + IiI1i11I * Iii * Ii + oooOo0oo0oo
elif O0oOOo0Oo == 7050 :
 oO0o00 ( oOOo0O00o )
 if 40 - 40: IIiIiII11i / Iii % oOo0O0Ooo - o0o00Oo0O
elif O0oOOo0Oo == 7051 :
 o000OOO000o ( oOOo0O00o )
 if 39 - 39: Ii - OOooOOo % oooOo0oo0oo + i1iIi + Ii
elif O0oOOo0Oo == 7052 :
 iIiIIiII11i1 ( oOOo0O00o )
 if 59 - 59: III1iiIii / OOooOOo - i1IiiiI1iI - i1iIi . i1i1I1IIii1II
elif O0oOOo0Oo == 7053 :
 i1Iii ( oOOo0O00o )
 if 87 - 87: i1i1I1IIii1II + oOo0O0Ooo * i1IiiiI1iI * I11i + o0o00Oo0O
elif O0oOOo0Oo == 7054 :
 CoolPlay ( oOOo0O00o )
 if 21 - 21: i1IiiiI1iI + OOooOOo + OOooOOo . IIiIiII11i / i1IiiiI1iI . oOo0O0Ooo
elif O0oOOo0Oo == 7060 :
 OOO0o0oo00 ( )
 if 66 - 66: i1IiiiI1iI % i1i1I1IIii1II . IiI1i11I * ooOoO0O00
elif O0oOOo0Oo == 7061 :
 IIiiI ( oOOo0O00o )
 if 81 - 81: ii * oOo0O0Ooo / i1IiiiI1iI
elif O0oOOo0Oo == 7063 :
 o000IIIi1IiI1iII ( oOOo0O00o )
 if 10 - 10: oOo0O0Ooo - IIiIiII11i / III1iiIii * IIiIiII11i
elif O0oOOo0Oo == 7062 :
 Ii11 ( oOOo0O00o )
 if 67 - 67: IIiIiII11i . o0ii1I % i1i1I1IIii1II . I1ii11iIi11i + III1iiIii
elif O0oOOo0Oo == 7064 :
 NATatozcat ( )
 if 10 - 10: oooOo0oo0oo - oO0o * i1i1I1IIii1II / iI11I1II1I1I - OOooOOo
elif O0oOOo0Oo == 7067 :
 II11i1 ( oOOo0O00o )
 if 20 - 20: III1iiIii % oOo0O0Ooo + iI11I1II1I1I % IiI1i11I
elif O0oOOo0Oo == 7066 :
 NATatozA ( oOOo0O00o )
 if 100 - 100: I11i - I1ii11iIi11i % i1IiiiI1iI . Ii % ii
elif O0oOOo0Oo == 7065 :
 IIIi1IIiI ( oOOo0O00o )
 if 39 - 39: Ii1I / Ii * ooOoO0O00 * I1ii11iIi11i
elif O0oOOo0Oo == 7070 :
 II1i1 ( )
 if 39 - 39: oO0o * ii / ooOoO0O00 + I1ii11iIi11i
elif O0oOOo0Oo == 7071 :
 DIZIlist ( oOOo0O00o )
 if 57 - 57: o0o00Oo0O
elif O0oOOo0Oo == 7072 :
 DIZIpull ( oOOo0O00o )
 if 83 - 83: oooOo0oo0oo / o0ii1I * oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I
elif O0oOOo0Oo == 7073 :
 WATCHDIZI ( oOOo0O00o )
 if 1 - 1: Iii / ii / IiI1i11I
elif O0oOOo0Oo == 7002 :
 I1iI1 ( )
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / Iii * I1ii11iIi11i
elif O0oOOo0Oo == 7003 :
 Ii1ii1i1 ( oOOo0O00o )
 if 91 - 91: oO0o . IiI1i11I
elif O0oOOo0Oo == 7004 :
 oO0IiiI1i1i11I1 ( oOOo0O00o )
 if 82 - 82: Ii1I / I1ii11iIi11i
elif O0oOOo0Oo == 7020 :
 O0OO0 ( oOOo0O00o )
 if 63 - 63: oOo0O0Ooo
elif O0oOOo0Oo == 7001 :
 Ii1I11ii1i ( )
 if 3 - 3: IiI1i11I + Ii1I
elif O0oOOo0Oo == 7010 :
 I11I1iIiI1I ( oOOo0O00o )
 if 35 - 35: i1i1I1IIii1II * IiI1i11I * i1i1I1IIii1II * i1IiiiI1iI * III1iiIii * ooOoO0O00
elif O0oOOo0Oo == 7011 :
 OOooO00O0oo0 ( oOOo0O00o )
 if 43 - 43: oO0o * oOo0O0Ooo / III1iiIii . Ii + IiI1i11I + I11i
elif O0oOOo0Oo == 7012 :
 Ii1I11II1IiI ( oOOo0O00o )
 if 1 - 1: oOo0O0Ooo % I11i . i1IiiiI1iI + Iii * i1i1I1IIii1II
elif O0oOOo0Oo == 7013 :
 cnfTVPlay2 ( oOOo0O00o )
elif O0oOOo0Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOOo0O00o )
elif O0oOOo0Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOOo0O00o )
elif O0oOOo0Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O0oOOo0Oo == 7018 :
 ooOo0o ( )
elif O0oOOo0Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOOo0O00o )
elif O0oOOo0Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOOo0O00o )
elif O0oOOo0Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOOo0O00o )
 if 41 - 41: oO0o * i1i1I1IIii1II - IIiIiII11i
elif O0oOOo0Oo == 8000 :
 IIiiiiiiII ( )
elif O0oOOo0Oo == 8001 :
 oOOOo0O ( )
elif O0oOOo0Oo == 8002 :
 O000o0O0 ( )
elif O0oOOo0Oo == 8003 :
 IIIo00o ( )
elif O0oOOo0Oo == 8004 :
 ooooOo00O ( )
elif O0oOOo0Oo == 8005 :
 OooOooO0OoOoo0o ( )
elif O0oOOo0Oo == 8006 :
 IIIIi1i ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 8030 :
 Ooi1IIii1i ( oOOo0O00o )
elif O0oOOo0Oo == 8045 :
 iIio00O000ooOO ( oOOo0O00o )
elif O0oOOo0Oo == 8046 :
 O000OOOoOooO ( oOOo0O00o )
elif O0oOOo0Oo == 8047 :
 oOO00o0 ( oOOo0O00o )
elif O0oOOo0Oo == 8048 :
 iII1iiI11IIi ( oOOo0O00o )
elif O0oOOo0Oo == 8049 :
 i1ii11Iii11 ( oOOo0O00o )
elif O0oOOo0Oo == 804900 :
 o0ooOO ( oOOo0O00o )
elif O0oOOo0Oo == 8020 :
 iII1111III1I ( )
elif O0oOOo0Oo == 8021 :
 iII1i1iii ( oOOo0O00o )
elif O0oOOo0Oo == 8022 :
 OO0iIi1ii111i ( oOOo0O00o )
elif O0oOOo0Oo == 8023 :
 II11IIi ( oOOo0O00o )
elif O0oOOo0Oo == 8040 :
 I1iiIIIi11 ( )
elif O0oOOo0Oo == 8041 :
 iiii ( oOOo0O00o )
elif O0oOOo0Oo == 8042 :
 o0Oo0oOO00O ( oOOo0O00o )
elif O0oOOo0Oo == 8043 :
 yt . PlayVideo ( oOOo0O00o )
elif O0oOOo0Oo == 8044 :
 Oo00OO ( oOOo0O00o )
elif O0oOOo0Oo == 8060 :
 I1iIiIi11i11 ( )
elif O0oOOo0Oo == 8061 :
 oOoo00OO0o0O000 ( oOOo0O00o )
elif O0oOOo0Oo == 8064 :
 O00oOo00o0o ( )
elif O0oOOo0Oo == 8065 :
 I11II ( oOOo0O00o )
elif O0oOOo0Oo == 8070 :
 OoO000oOO ( )
elif O0oOOo0Oo == 8071 :
 iiIiiiIii ( oOOo0O00o )
elif O0oOOo0Oo == 7080 :
 o0OOoOO0oOO ( oOOo0O00o )
elif O0oOOo0Oo == 8090 :
 i1I1IiiIIIiiI ( )
elif O0oOOo0Oo == 8091 :
 o0O00 ( oOOo0O00o )
elif O0oOOo0Oo == 8092 :
 oO000OO0 ( oOOo0O00o )
elif O0oOOo0Oo == 8093 :
 o00OOoo0 ( oOOo0O00o )
elif O0oOOo0Oo == 8081 :
 I1iOoO00O ( )
elif O0oOOo0Oo == 8062 :
 IIIII1i1I ( oOOo0O00o )
elif O0oOOo0Oo == 8063 :
 i1iI11I ( oOOo0O00o )
elif O0oOOo0Oo == 8050 :
 IIiIIiI1iIII ( )
elif O0oOOo0Oo == 8051 :
 o0ooo0oooO ( oOOo0O00o )
elif O0oOOo0Oo == 8052 :
 ooOoOO00oOOO ( oOOo0O00o )
elif O0oOOo0Oo == 8085 :
 i1iI11IiII ( )
elif O0oOOo0Oo == 8086 :
 OOo0OOooO0 ( oOOo0O00o )
elif O0oOOo0Oo == 8087 :
 ooOOOo00Oooo0o0 ( oOOo0O00o )
elif O0oOOo0Oo == 8088 :
 I1i111II ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 9000 :
 IIioo0 ( )
elif O0oOOo0Oo == 1111 :
 i1I1Iiii ( )
elif O0oOOo0Oo == 9001 :
 O00OoO0o ( )
elif O0oOOo0Oo == 9002 :
 OoOoO ( )
elif O0oOOo0Oo == 9003 :
 oO0oooooO ( )
elif O0oOOo0Oo == 9004 :
 World1 ( )
elif O0oOOo0Oo == 9005 :
 World2 ( oOOo0O00o )
elif O0oOOo0Oo == 9006 :
 World3 ( oOOo0O00o )
elif O0oOOo0Oo == 9007 :
 Oo0oOO ( )
elif O0oOOo0Oo == 9008 :
 ii1oO0Oo ( oOOo0O00o )
elif O0oOOo0Oo == 9009 :
 iIi1IIIi1Ii ( oOOo0O00o )
elif O0oOOo0Oo == 9010 :
 o00OOOo0O0O0o0 ( )
elif O0oOOo0Oo == 9011 :
 Oo0ooo0oOo0Oo0O ( oOOo0O00o )
elif O0oOOo0Oo == 50 :
 Iii1o00o0 ( oOOo0O00o )
elif O0oOOo0Oo == 9020 :
 champlist ( )
elif O0oOOo0Oo == 9021 :
 O0oOO0o0 ( )
elif O0oOOo0Oo == 9022 :
 O000000oooOOo ( )
elif O0oOOo0Oo == 9023 :
 I11iiI1 ( )
elif O0oOOo0Oo == 9024 :
 oooiIi11 ( oOOo0O00o )
elif O0oOOo0Oo == 9030 :
 O00 ( oOOo0O00o )
elif O0oOOo0Oo == 9031 :
 O00OooOOo ( oOOo0O00o )
elif O0oOOo0Oo == 9032 :
 oOO0 ( oOOo0O00o )
elif O0oOOo0Oo == 9033 :
 IIIiiiIi1I1 ( oOOo0O00o )
elif O0oOOo0Oo == 9034 :
 oo000ii ( )
elif O0oOOo0Oo == 7085 :
 oo0OOO0O0 ( oOOo0O00o )
elif O0oOOo0Oo == 7086 :
 i1ii1iIiI1 ( oOOo0O00o )
elif O0oOOo0Oo == 7087 :
 IIiIiI1IIi ( OoO000O )
elif O0oOOo0Oo == 9666 :
 ooO0O00Oo0o ( oOOo0O00o )
elif O0oOOo0Oo == 10100 : oooo0O00O ( )
elif O0oOOo0Oo == 101001 : OOO0o0OO ( oOOo0O00o )
elif O0oOOo0Oo == 10105 : iiiiiiiiiiiI ( oOOo0O00o )
elif O0oOOo0Oo == 10106 : iI111iiI1II ( oOOo0O00o )
elif O0oOOo0Oo == 10104 : oooOIi1IiIi11i1 ( oOOo0O00o )
elif O0oOOo0Oo == 10107 : Ii1iIi ( )
elif O0oOOo0Oo == 10103 : OOOoooO000O0 ( oOOo0O00o )
elif O0oOOo0Oo == 10108 : OOoO00o00oo ( oOOo0O00o )
elif O0oOOo0Oo == 10000 : Origin_Menu ( )
elif O0oOOo0Oo == 10001 : o0oooO ( )
elif O0oOOo0Oo == 10002 : Ooo00OoOOO ( )
elif O0oOOo0Oo == 10003 : III1 ( )
elif O0oOOo0Oo == 10004 : o0oO0OoO0 ( oOOo0O00o )
elif O0oOOo0Oo == 10005 : iIiI1 ( )
elif O0oOOo0Oo == 10006 : oOOo ( oOOo0O00o )
elif O0oOOo0Oo == 10007 : ii111Ii1i ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10008 : o0iIiii ( )
elif O0oOOo0Oo == 10009 : O0OOOo0o0O0 ( )
elif O0oOOo0Oo == 10010 : o000 ( oOOo0O00o )
elif O0oOOo0Oo == 10011 : ii1i11Ii11iI ( oOOo0O00o )
elif O0oOOo0Oo == 10012 : I11iiiiI1i ( oOOo0O00o )
elif O0oOOo0Oo == 10113 : GRABG ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 10109 : IiiIOO ( oOOo0O00o )
elif O0oOOo0Oo == 10013 : OOo0OO00 ( oOOo0O00o )
elif O0oOOo0Oo == 10014 : i1I1iiiI ( )
elif O0oOOo0Oo == 10015 : oOOoOO ( )
elif O0oOOo0Oo == 10016 : iii1IIII1iii11I ( oOOo0O00o )
elif O0oOOo0Oo == 10017 : I1I1I1 ( )
elif O0oOOo0Oo == 10018 : i1IIIii ( )
elif O0oOOo0Oo == 10019 : o0oOoo00 ( )
elif O0oOOo0Oo == 10020 : oOOo0O0Oo ( )
elif O0oOOo0Oo == 10021 : O0oO00o0o0oo0 ( )
elif O0oOOo0Oo == 10022 : OooooOO ( oOOo0O00o )
elif O0oOOo0Oo == 10023 : i1IIi11 ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 10024 : iIi1i1I1I ( oOOo0O00o )
elif O0oOOo0Oo == 10025 : I1Iiiiiii ( )
elif O0oOOo0Oo == 10026 : IiI1i11i1iI ( )
elif O0oOOo0Oo == 10027 : II1i1iI ( )
elif O0oOOo0Oo == 10028 : iii11Ii ( )
elif O0oOOo0Oo == 10029 : Oo0oo ( )
elif O0oOOo0Oo == 423 : o0oIi1iiiii ( oOOo0O00o )
elif O0oOOo0Oo == 426 : iII1I1Ii11i1i ( oOOo0O00o )
elif O0oOOo0Oo == 10030 : Izle_Films ( )
elif O0oOOo0Oo == 10031 : Latest_Izle_Movies ( )
elif O0oOOo0Oo == 10032 : Izle_Genres ( )
elif O0oOOo0Oo == 10033 : Izle_Pop_Movies ( )
elif O0oOOo0Oo == 10034 : Izle_Boxsets ( )
elif O0oOOo0Oo == 10035 : Izle_Search ( )
elif O0oOOo0Oo == 10036 : Izle_Genres_Movie ( oOOo0O00o )
elif O0oOOo0Oo == 10037 : Izle_Boxset_single ( oOOo0O00o )
elif O0oOOo0Oo == 10038 : Izle_IFRAME ( )
elif O0oOOo0Oo == 10039 : Izle_Boxsets_Next ( oOOo0O00o )
elif O0oOOo0Oo == 10040 : oOOoo ( )
elif O0oOOo0Oo == 10041 : OOoo0o00O0oO ( oOOo0O00o )
elif O0oOOo0Oo == 10042 : iii1II11II1 ( oOOo0O00o )
elif O0oOOo0Oo == 10043 : i1IIi1ii1i1ii ( )
elif O0oOOo0Oo == 10044 : Iii1iIII1Iii ( oOOo0O00o )
elif O0oOOo0Oo == 10045 : i111ii1II11ii ( iIIIiIi )
elif O0oOOo0Oo == 10046 : i1oOOOoOO ( oOOo0O00o )
elif O0oOOo0Oo == 10047 : oo00Oo0 ( oOOo0O00o )
elif O0oOOo0Oo == 10048 : i111 ( oOOo0O00o )
elif O0oOOo0Oo == 10049 : II1i11i1iI1I ( oOOo0O00o )
elif O0oOOo0Oo == 10050 : OoO ( )
elif O0oOOo0Oo == 10051 : I1I1iI ( )
elif O0oOOo0Oo == 10052 : ii1IiIiIi ( )
elif O0oOOo0Oo == 10053 : Addon ( oOOo0O00o )
elif O0oOOo0Oo == 10054 : OOOOO0oOooo0O ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 10055 :
 oO00O0 ( "addFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0Oo0O0O0o ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , Ooo0o0OoOO )
elif O0oOOo0Oo == 10056 :
 oO00O0 ( "rmFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 o000ooO0Ooo0o ( iIIIiIi )
elif O0oOOo0Oo == 10057 :
 oO00O0 ( "getFavorites" )
 i1oo0OO0Oo ( )
elif O0oOOo0Oo == 10058 : oOoO0 ( )
elif O0oOOo0Oo == 10059 : Donators_Guide ( )
elif O0oOOo0Oo == 10060 : o00o0 ( )
elif O0oOOo0Oo == 10061 : Ii1IIi11 ( )
elif O0oOOo0Oo == 10062 : IiIII ( iIIIiIi , oOOo0O00o , OoO000O )
elif O0oOOo0Oo == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif O0oOOo0Oo == 10064 : IiiIIi ( )
elif O0oOOo0Oo == 10065 : oO0o0oOo ( oOOo0O00o )
elif O0oOOo0Oo == 10066 : IiIIii1iiI ( oOOo0O00o )
elif O0oOOo0Oo == 10068 : iiI111 ( oOOo0O00o )
elif O0oOOo0Oo == 10069 : O00oO0 ( oOOo0O00o )
elif O0oOOo0Oo == 10070 : iI11111ii11 ( oOOo0O00o )
elif O0oOOo0Oo == 10071 : Genie_Watch ( )
elif O0oOOo0Oo == 10072 : Iiii1Ii ( )
elif O0oOOo0Oo == 10073 : oO0O0o0O ( oOOo0O00o )
elif O0oOOo0Oo == 10074 : OoiiI1i111 ( oOOo0O00o )
elif O0oOOo0Oo == 10075 : Ii1iiI1 ( iiiI1I1iIIIi1 , iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 10076 : o0Oo ( oOOo0O00o )
elif O0oOOo0Oo == 10077 : iiI111OOoooo0oo ( oOOo0O00o )
elif O0oOOo0Oo == 10078 : i1ii1I1IIIII ( )
elif O0oOOo0Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif O0oOOo0Oo == 10080 : Genie_Watch_Tv_Genre ( oOOo0O00o )
elif O0oOOo0Oo == 10081 : Genie_Watch_TV_PlayRun ( oOOo0O00o )
elif O0oOOo0Oo == 10082 : Genie_Watch_TV_Episodes ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10083 : Genie_Watch_Tv_Recent ( oOOo0O00o )
elif O0oOOo0Oo == 10084 : Ii1ii111i1 ( )
elif O0oOOo0Oo == 10085 : oo0OOo0 ( )
elif O0oOOo0Oo == 10086 : O0 ( )
elif O0oOOo0Oo == 20000 : ooOo ( )
elif O0oOOo0Oo == 20001 : OooOoO0OO00 ( oOOo0O00o )
elif O0oOOo0Oo == 20002 : I1111iIIiIIII ( oOOo0O00o )
elif O0oOOo0Oo == 20003 : ooooOOo ( oOOo0O00o )
elif O0oOOo0Oo == 20004 : Oooo0o00 ( oOOo0O00o )
elif O0oOOo0Oo == 20005 : ooOoo0oo00000O ( oOOo0O00o )
elif O0oOOo0Oo == 21004 : IIii1I11iiii1 ( )
elif O0oOOo0Oo == 21005 : oOo0OOoO0ooOOoo ( oOOo0O00o )
elif O0oOOo0Oo == 21006 : OOO0oOoO00OoO ( oOOo0O00o )
elif O0oOOo0Oo == 21007 : IiI1 ( oOOo0O00o )
elif O0oOOo0Oo == 21008 : IiI ( oOOo0O00o )
elif O0oOOo0Oo == 21009 : O00oO000O0O ( oOOo0O00o )
elif O0oOOo0Oo == 30000 : I1iIIIiiii ( )
elif O0oOOo0Oo == 30001 : O00o0 ( )
elif O0oOOo0Oo == 100121 : Resolve ( oOOo0O00o )
elif O0oOOo0Oo == 30003 : i1iI11ii ( )
elif O0oOOo0Oo == 30004 : oo00OOo0 ( oOOo0O00o )
elif O0oOOo0Oo == 30005 : IIIiI1i ( oOOo0O00o )
elif O0oOOo0Oo == 30006 : iIi11I1II ( )
elif O0oOOo0Oo == 30007 : I11II1 ( )
elif O0oOOo0Oo == 30008 : oo0OoOO000O ( oOOo0O00o )
elif O0oOOo0Oo == 30009 : Oo0OOo0o0o0o0 ( oOOo0O00o )
elif O0oOOo0Oo == 30010 : ooOO0000oo0O ( oOOo0O00o )
elif O0oOOo0Oo == 30011 : oOOOO ( )
elif O0oOOo0Oo == 30012 : oo0OOO0OOoOO ( )
elif O0oOOo0Oo == 30013 : iIIi1I1Ii1 ( )
elif O0oOOo0Oo == 30014 : OooO00O0OO0oo ( )
elif O0oOOo0Oo == 30015 : iIO0oOoo00Oo0O ( oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 30016 : iIII1iIii ( oOOo0O00o )
elif O0oOOo0Oo == 30019 : IIiII1i1i ( oOOo0O00o )
elif O0oOOo0Oo == 30017 : ooOooOOo ( oOOo0O00o )
elif O0oOOo0Oo == 30018 : I1iiII1 ( oOOo0O00o )
elif O0oOOo0Oo == 30030 : Oo0OOo ( )
elif O0oOOo0Oo == 30031 : ooooO ( )
elif O0oOOo0Oo == 30032 : IIII1iII ( )
elif O0oOOo0Oo == 30033 : I1i1i1IIi1I ( )
elif O0oOOo0Oo == 30034 : IIi11iIIiIiI ( )
elif O0oOOo0Oo == 30035 : OO0O00 ( oOOo0O00o )
elif O0oOOo0Oo == 30036 : ooOOoO0o0 ( oOOo0O00o )
elif O0oOOo0Oo == 30037 : i1Ii1i11ii ( oOOo0O00o )
elif O0oOOo0Oo == 30038 : O00o ( )
elif O0oOOo0Oo == 30039 : oooooo0O000o ( )
elif O0oOOo0Oo == 50000 : I1i ( )
elif O0oOOo0Oo == 50001 : I11iI1iIii1ii ( )
elif O0oOOo0Oo == 50002 : ooo ( oOOo0O00o )
elif O0oOOo0Oo == 50003 : Table_Menu ( OoO000O )
elif O0oOOo0Oo == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif O0oOOo0Oo == 60001 : Ii11I1I11II ( )
elif O0oOOo0Oo == 60002 : IiIIiiiii1Iii ( iIIIiIi )
elif O0oOOo0Oo == 60003 : I1Iiii1Ii ( oOOo0O00o )
elif O0oOOo0Oo == 600033 : IiiiIIi ( oOOo0O00o )
elif O0oOOo0Oo == 60004 : oo0 ( oOOo0O00o )
elif O0oOOo0Oo == 50004 : iiI ( )
elif O0oOOo0Oo == 50005 : speedtest . runtest ( oOOo0O00o )
elif O0oOOo0Oo == 70001 : OOOO0oO0O ( )
elif O0oOOo0Oo == 70002 : III11i1iiiI ( oOOo0O00o )
elif O0oOOo0Oo == 70003 : O0oooooO ( oOOo0O00o )
elif O0oOOo0Oo == 70004 : IIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 70005 : II11II ( oOOo0O00o )
elif O0oOOo0Oo == 70006 : i1ii11III ( )
elif O0oOOo0Oo == 50006 : o0OIiII ( i1 , i1111 )
elif O0oOOo0Oo == 80000 : IiIiII11i1 ( )
elif O0oOOo0Oo == 80001 : resolvefilmon ( oOOo0O00o )
elif O0oOOo0Oo == 80002 : iIi1iIiIIII1iII1i ( )
elif O0oOOo0Oo == 80003 : OOOOOOO00OO ( iIIIiIi , oOOo0O00o , "None" )
elif O0oOOo0Oo == 80004 : oO0O0oo ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 80005 : III1i11 ( )
elif O0oOOo0Oo == 80006 : i111I11I ( oOOo0O00o )
elif O0oOOo0Oo == 80007 : OoOoOOoO ( oOOo0O00o )
elif O0oOOo0Oo == 80008 : ii1ii1i11I1I ( )
elif O0oOOo0Oo == 80009 : i11Ii ( )
elif O0oOOo0Oo == 80010 : i1iii1I1I ( oOOo0O00o )
elif O0oOOo0Oo == 80011 : oooOOoO ( oOOo0O00o )
elif O0oOOo0Oo == 80012 : iIII1iiiiI1Ii11 ( )
elif O0oOOo0Oo == 90000 : iI11Iii1ii111 ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 90001 : tools ( )
elif O0oOOo0Oo == 90002 : oooooOOO000Oo ( )
elif O0oOOo0Oo == 90003 : I1I ( oOOo0O00o )
elif O0oOOo0Oo == 90004 : O00O0oO00o ( oOOo0O00o )
elif O0oOOo0Oo == 90005 : IIi1IIiiI1 ( oOOo0O00o )
elif O0oOOo0Oo == 90006 : iiiI1I1I ( oOOo0O00o )
elif O0oOOo0Oo == 90007 : O0iIIii1 ( oOOo0O00o )
elif O0oOOo0Oo == 90008 : o0ooo0 ( oOOo0O00o )
elif O0oOOo0Oo == 90009 : OOOOo00oOOO00 ( oOOo0O00o )
elif O0oOOo0Oo == 90010 : iiIiii1IIIII ( )
elif O0oOOo0Oo == 90020 : I11IIIIiII ( )
elif O0oOOo0Oo == 90021 : hellyeah2 ( oOOo0O00o )
elif O0oOOo0Oo == 90022 : hellyeah3 ( oOOo0O00o )
elif O0oOOo0Oo == 90023 : ii1iI111 ( )
elif O0oOOo0Oo == 90024 : OOoo0 ( oOOo0O00o )
elif O0oOOo0Oo == 90025 : IiI1i111IiIiIi1 ( oOOo0O00o )
if 2 - 2: III1iiIii + III1iiIii - oO0o * IiI1i11I . i1i1I1IIii1II
elif O0oOOo0Oo == 90026 : I111 ( )
elif O0oOOo0Oo == 90027 : I11I111i1I1 ( iIIIiIi , oOOo0O00o , OoO000O )
elif O0oOOo0Oo == 90028 : ii1I11 ( oOOo0O00o )
if 91 - 91: i1iIi
elif O0oOOo0Oo == 900300 : OoOiiI1IIIi ( )
elif O0oOOo0Oo == 900301 : II11IiIi11 ( oOOo0O00o )
elif O0oOOo0Oo == 900302 : oO00ooooO0o ( oOOo0O00o )
elif O0oOOo0Oo == 90030 : I1III1111iIi ( )
elif O0oOOo0Oo == 90031 : IiIi1I1 ( )
elif O0oOOo0Oo == 90032 : IiIIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 90033 : IIIIiii1IIii ( oOOo0O00o )
elif O0oOOo0Oo == 90034 : ooOoOo0 ( oOOo0O00o )
elif O0oOOo0Oo == 90035 : iI1i11 ( oOOo0O00o )
elif O0oOOo0Oo == 90036 : OoO0ooooOOo0o ( oOOo0O00o )
elif O0oOOo0Oo == 90039 : iIii1iii1I1ii ( oOOo0O00o )
elif O0oOOo0Oo == 90037 : oOo ( oOOo0O00o )
elif O0oOOo0Oo == 900377 : i1i1IIIIIIIi ( oOOo0O00o )
elif O0oOOo0Oo == 90038 : I1ii1II1iII ( )
if 22 - 22: i1iIi % oO0o * OOooOOo + I1ii11iIi11i
elif O0oOOo0Oo == 10090 : o0ii1i ( )
elif O0oOOo0Oo == 10091 : IiiII1I ( oOOo0O00o )
elif O0oOOo0Oo == 10092 : iioOo00O0o ( oOOo0O00o )
elif O0oOOo0Oo == 10093 : IIIi1iiI1I1 ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10094 : O0ooOoO0 ( oOOo0O00o , iiiI1I1iIIIi1 )
if 44 - 44: o0o00Oo0O - Iii
elif O0oOOo0Oo == 10095 : ii11i ( )
elif O0oOOo0Oo == 10096 : iI1i1iIi1iiII ( oOOo0O00o )
elif O0oOOo0Oo == 10097 : oOOOOoO00Ooo0 ( oOOo0O00o )
elif O0oOOo0Oo == 10098 : ii11i11 ( oOOo0O00o )
elif O0oOOo0Oo == 10099 : oOOOo ( oOOo0O00o )
if 43 - 43: o0o00Oo0O
elif O0oOOo0Oo == 10200 : i1i111iI ( )
elif O0oOOo0Oo == 10201 : ooOoOO ( oOOo0O00o )
elif O0oOOo0Oo == 10202 : O0oOo ( oOOo0O00o )
elif O0oOOo0Oo == 10203 : RT4 ( oOOo0O00o )
if 50 - 50: Iii - ii
elif O0oOOo0Oo == 90040 : O00oo ( )
elif O0oOOo0Oo == 90041 : OOo00ooOoO0o ( oOOo0O00o )
elif O0oOOo0Oo == 90042 : o00iIiiiII ( oOOo0O00o )
elif O0oOOo0Oo == 90043 : I11iiI11iiI ( oOOo0O00o )
elif O0oOOo0Oo == 90044 : iII1iI1IIiI ( oOOo0O00o )
elif O0oOOo0Oo == 90045 : oooOO0oo0Oo00 ( )
elif O0oOOo0Oo == 90046 : O00ooOOoO0O000O ( oOOo0O00o )
elif O0oOOo0Oo == 90050 : i1I ( )
elif O0oOOo0Oo == 90051 : i1ii1iiIi1II ( oOOo0O00o )
elif O0oOOo0Oo == 90052 : O0Oo0O0 ( oOOo0O00o )
elif O0oOOo0Oo == 90053 : oo00o0 ( oOOo0O00o )
elif O0oOOo0Oo == 90054 : III1III11II ( oOOo0O00o )
elif O0oOOo0Oo == 90055 : Ooooo ( )
if 29 - 29: i1i1I1IIii1II * i1i1I1IIii1II
elif O0oOOo0Oo == 100001 : Stand_up ( )
if 44 - 44: i1iIi . oOo0O0Ooo * i1i1I1IIii1II * o0ii1I
elif O0oOOo0Oo == 100003 : iii1IIII1iii11I ( oOOo0O00o )
elif O0oOOo0Oo == 100004 : Ooo0oo ( oOOo0O00o )
elif O0oOOo0Oo == 100005 : Resolve ( oOOo0O00o )
elif O0oOOo0Oo == 100008 : Search ( )
elif O0oOOo0Oo == 100007 : IioO0oOOO0Ooo ( oOOo0O00o )
elif O0oOOo0Oo == 100009 : yt . PlayVideo ( oOOo0O00o )
elif O0oOOo0Oo == 100010 : OOOooo ( oOOo0O00o )
elif O0oOOo0Oo == 100100 : o0o0Ooo0 ( iiiI1I1iIIIi1 , oOOo0O00o , OOOi1II )
elif O0oOOo0Oo == 100101 : I11I1IIiiII1 ( oOOo0O00o , iIIIiIi , IIo0o0O0O00oOOo , OOOi1II , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 100102 : I1i11II ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 100106 : IIIII1I1Ii11iI ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 100107 : O0ooOoO ( )
elif O0oOOo0Oo == 100108 : iiI1iii1I111 ( )
elif O0oOOo0Oo == 100109 : OoOI1 ( oOOo0O00o )
elif O0oOOo0Oo == 40000 : O0OOO0 ( )
elif O0oOOo0Oo == 40001 : III1IiiIiiI1i ( oOOo0O00o )
elif O0oOOo0Oo == 100110 : oOo00o ( oOOo0O00o )
elif O0oOOo0Oo == 100111 : I11I1ii1i ( oOOo0O00o )
elif O0oOOo0Oo == 100112 : iiI1111I11i1I ( oOOo0O00o )
elif O0oOOo0Oo == 100113 : iI1 ( oOOo0O00o )
elif O0oOOo0Oo == 100114 : II111i1ii1iII ( oOOo0O00o )
elif O0oOOo0Oo == 100115 : O00OOO00Ooo ( oOOo0O00o )
elif O0oOOo0Oo == 100117 : ooo0OoO ( oOOo0O00o )
elif O0oOOo0Oo == 100118 : Oo00OO00o0oO ( oOOo0O00o )
elif O0oOOo0Oo == 100120 : OoOOoooO000 ( oOOo0O00o )
elif O0oOOo0Oo == 1001200 : OoO0o000oOo ( oOOo0O00o )
elif O0oOOo0Oo == 100210 : IIiiii ( oOOo0O00o )
elif O0oOOo0Oo == 100211 : oOoOo0o00o ( )
elif O0oOOo0Oo == 100212 : ooO0 ( )
elif O0oOOo0Oo == 100213 : i1I111II ( )
elif O0oOOo0Oo == 100214 : o0ooOO0OOO00o ( )
elif O0oOOo0Oo == 1000111 :
 iIiIiiiII11i ( oOOo0O00o )
 if 41 - 41: ooOoO0O00 % Ii + Iii % ii / Ii1I
elif O0oOOo0Oo == 1001111 :
 O00oo0ooO ( iIIIiIi , oOOo0O00o )
 if 8 - 8: ii - oO0o / Ii / o0o00Oo0O . III1iiIii
elif O0oOOo0Oo == 1002111 :
 iii1Ii ( )
 if 86 - 86: i1iIi * ii + IiI1i11I + I11i
elif O0oOOo0Oo == 1003111 :
 ooOOooooo0Oo ( oOOo0O00o , iIIIiIi )
 if 79 - 79: ooOoO0O00 % Ii1I - oO0o % Ii1I
elif O0oOOo0Oo == 1004111 :
 Ii1i11IIiI ( )
 if 6 - 6: I1ii11iIi11i / IiI1i11I . Ii
elif O0oOOo0Oo == 1005111 :
 iIII ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( iIIIiIi , oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( iIIIiIi , oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1105000 :
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , Ooo0o0OoOO )
elif O0oOOo0Oo == 1106000 :
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( iIIIiIi )
elif O0oOOo0Oo == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( oOOo0O00o )
elif O0oOOo0Oo == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( iIIIiIi )
elif O0oOOo0Oo == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif O0oOOo0Oo == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( oOOo0O00o )
elif O0oOOo0Oo == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in oOOo0O00o :
  import urlresolver
  OoOOoooOO0O = urlresolver . resolve ( oOOo0O00o )
  ooo00Ooo = xbmcgui . ListItem ( path = OoOOoooOO0O )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 elif not oOOo0O00o . startswith ( "plugin://plugin" ) or not any ( x in oOOo0O00o for x in pyramid . g_ignoreSetResolved ) :
  ooo00Ooo = xbmcgui . ListItem ( path = oOOo0O00o )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + oOOo0O00o + ')' )
elif O0oOOo0Oo == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( iIIIiIi , playlist )
elif O0oOOo0Oo == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( oOOo0O00o , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1117000 :
 oOOo0O00o , IIIi1Ii = getRegexParsed ( regexs , oOOo0O00o )
 if oOOo0O00o :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( oOOo0O00o , iIIIiIi , iiiI1I1iIIIi1 , IIIi1Ii )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif O0oOOo0Oo == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 Ii11II1iiii1 = youtubedl . single_YD ( oOOo0O00o )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( Ii11II1iiii1 , iIIIiIi , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( oOOo0O00o ) , iIIIiIi , iiiI1I1iIIIi1 , True )
elif O0oOOo0Oo == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , iIIIiIi , 'video' )
elif O0oOOo0Oo == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( oOOo0O00o , iIIIiIi , 'video' )
elif O0oOOo0Oo == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( oOOo0O00o , iIIIiIi , 'audio' )
elif O0oOOo0Oo == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1126000 :
 iIIIiIi = iIIIiIi . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( oOOo0O00o , search_term = iIIIiIi [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( oOOo0O00o )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif O0oOOo0Oo == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( iIIIiIi , oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( oOOo0O00o )
elif O0oOOo0Oo == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 9050000 : ii1iIi1II ( )
elif O0oOOo0Oo == 9060000 : O00oo0ooO ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 9080000 : iiiI1ii ( )
elif O0oOOo0Oo == 9070000 : iII1I1 ( )
elif O0oOOo0Oo == 9090000 : oOO00oO00O0OO ( )
elif O0oOOo0Oo == 9100000 : o0oO0oOO ( )
elif O0oOOo0Oo == 9110000 : i11i11 ( )
elif O0oOOo0Oo == 9999999 : IiiIi11Ii1iI1 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
