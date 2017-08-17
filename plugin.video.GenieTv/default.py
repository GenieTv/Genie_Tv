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
IiiIII111iI = "3.6.0"
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
  o0OIiII ( 'Change Log 17/8/17 - v3.6.2' , '[COLORorangered]New Section Added To Tv Shows[/COLOR],[CR][COLORsteelblue]Nice Upgrade To Top Rated Section[/COLOR],[CR][COLORsteelblue]ThunderStruck Joins GenieTv[/COLOR],[CR][COLORsteelblue]RaizRadio Added To Music[/COLOR],[CR][COLORsteelblue]Adult Gallerys Added[/COLOR],[CR][COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 17/8/17 - v3.6.2' , '[COLORorangered]New Section Added To Tv Shows[/COLOR],[CR][COLORsteelblue]Nice Upgrade To Top Rated Section[/COLOR],[CR][COLORsteelblue]ThunderStruck Joins GenieTv[/COLOR],[CR][COLORsteelblue]RaizRadio Added To Music[/COLOR],[CR][COLORsteelblue]Adult Gallerys Added[/COLOR],[CR][COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
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
   I1I1II1I11 ( '[COLORorangered]Adult Content[/COLOR]' , '' , 19999999 , iiIi1IIiIi + 'AG.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'tools.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if OO ( ) == 'android' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
   if 37 - 37: i1iIi % i1i1I1IIii1II . Ii % o0ii1I . I1ii11iIi11i
   if 39 - 39: oooOo0oo0oo - I1ii11iIi11i * Ii1I % I11i
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def I1I1i1I ( ) :
 if 92 - 92: III1iiIii . III1iiIii + oO0o
 if 9 - 9: oOo0O0Ooo * o0o00Oo0O + III1iiIii - Iii * i1IiiiI1iI
 if 64 - 64: iI11I1II1I1I - iI11I1II1I1I / Ii % I1ii11iIi11i - IiI1i11I
 if 56 - 56: oOo0O0Ooo . Iii * o0ii1I - IiI1i11I
 if 8 - 8: oO0o - oOo0O0Ooo % o0ii1I * ii - oO0o * i1IiiiI1iI
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  if 6 - 6: ii
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if O0o0Oo == '5knuckleshuffle' :
  I1I1II1I11 ( '[COLORorangered]Adult Content[/COLOR]' , '' , 19999999 , iiIi1IIiIi + 'AG.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def tools ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']Change Log[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  ii1iII1II ( )
 if O0oO == 1 :
  oo0OOo0 ( )
 if O0oO == 2 :
  OO0ooOOO0OOO ( )
 if O0oO == 3 :
  oO00oooOOoOo0 ( OoOOoOooooOOo )
 if O0oO == 4 :
  iIii1 . ok ( i1 , i1111 )
 if O0oO == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if O0oO == 6 :
  oOo0O ( )
  if 52 - 52: Ii / I11i * i1iIi
def iI ( ) :
 I1I1II1I11 ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 I1I1II1I11 ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 I1I1II1I11 ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def OO0O000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in iiIiI1i1 :
  Ii1I1i ( IiIi11iI , url , 21999992 , 'http://www.virtual-fireplace.net/' + oO0O00oOOoooO , 'http://www.virtual-fireplace.net/' + oO0O00oOOoooO , IiIi11iI )
def Oo0O00O000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in iiIiI1i1 :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def i11I1IiII1i1i ( url ) :
 I1I1II1I11 ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 I1I1II1I11 ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 I1I1II1I11 ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def ooI1111i ( url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in iiIiI1i1 :
  Ii1I1i ( IiIi11iI , 'http:' + url , 21999992 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
def iIIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , url , o00O0O in iiIiI1i1 :
  I1I1II1I11 ( IiIi11iI , url , 21999996 , oO0O00oOOoooO , oO0O00oOOoooO , ( o00O0O ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def ii1iii1i ( url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , o00O0O in iiIiI1i1 :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR] - Audio' , url , 21999997 , oO0O00oOOoooO , oO0O00oOOoooO , ( o00O0O ) . replace ( ' - Text' , '' ) , ( story ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR] - Text' , url , 21999998 , oO0O00oOOoooO , oO0O00oOOoooO , ( o00O0O ) . replace ( ' - Text' , '' ) , ( story ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def Iii1I1111ii ( url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( II11iIiIIIiI )
 for url in iiIiI1i1 :
  ooOoO00 ( url )
def Ii1IIiI1io0O00Oo0 ( name , url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiII111i1i11 in iiIiI1i1 :
  o0OIiII ( ( name ) . replace ( ' - Text' , '' ) , ( IiII111i1i11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 40 - 40: i1iIi * III1iiIii * Ii
  if 57 - 57: i1iIi
def II11Iiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , o00O0O , i11I , IiIi11iI in iiIiI1i1 :
  Ii1I1i ( IiIi11iI , url , 21009 , oO0O00oOOoooO , i11I , o00O0O )
  if 76 - 76: III1iiIii * IiI1i11I
def ooooooo00o ( url ) :
 url = url
 o0oooOO00 = OO ( )
 if o0oooOO00 ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif o0oooOO00 ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 32 - 32: i1IiiiI1iI
  if 30 - 30: iI11I1II1I1I / Iii . oO0o - I11i
def Iii11iI1i ( ) :
 OoOOoOooooOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( OoOOoOooooOOo , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( OoOOoOooooOOo )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOO0o ( )
def i1II1 ( ) :
 i11i1 = IiiiiI1i1Iii ( )
 oo00oO0o = i11i1 . replace ( II11iiii1Ii , "" )
 if os . path . exists ( i11i1 ) or not i11i1 == False :
  iiii111II = open ( i11i1 , mode = 'r' ) ; I11iIiI1I1i11 = iiii111II . read ( ) ; iiii111II . close ( )
  o0OIiII ( "%s - %s" % ( i1 , oo00oO0o ) , I11iIiI1I1i11 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def Iii11iI1i ( ) :
 OoOOoOooooOOo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( OoOOoOooooOOo , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( OoOOoOooooOOo )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOO0o ( )
def OOoooO00o0oo0 ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 61 - 61: o0ii1I / Ii1I % III1iiIii + i1iIi / i1IiiiI1iI . i1iIi
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 12 - 12: ooOoO0O00 + ooOoO0O00 - Ii1I * I1ii11iIi11i % I1ii11iIi11i - IIiIiII11i
def o0OOOOooo ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def OooO0OO ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 o0OOo0o0O0O = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0OO0o0oOOO0O = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in o0OOo0o0O0O :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 900302 , oO0O00oOOoooO , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for iII1i11 in o0OO0o0oOOO0O :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , iII1i11 , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def OooIiIIII1i11I ( url ) :
 OOOiII1 = OooOoooOo ( url )
 o0OOo0o0O0O = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( OOOiII1 )
 OOo = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( OOOiII1 )
 for url , IiIi11iI in o0OOo0o0O0O :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , IiIi11iI in OOo :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def IIii11Ii1i1I ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for oo00O0oO0O0 , ooo0OO0O0Oo in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + oo00O0oO0O0 , ooo0OO0O0Oo )
def Ooo0O0oooo ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def iiI ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( Oooo0O )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , oO0O00oOOoooO , Oo00OOOOO , '' )
 for url in next :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def oOIIiIi ( url ) :
 Oooo0O = OooOoooOo ( url )
 OOoOooOoOOOoo = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 Iiii1iI1i = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for IiIi11iI , url in i1Iii1i1I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for IiIi11iI , url in Iiii1iI1i :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in OOoOooOoOOOoo :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 34 - 34: i1iIi * oOo0O0Ooo . ooOoO0O00 * i1iIi / i1iIi
def IIiI1Ii ( url ) :
 if 'drive' in url :
  ooOoO00 ( url )
 else :
  Oooo0O = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( Oooo0O )
  for url in IIi :
   ooOoO00 ( url )
def O0O0O0Oo ( url ) :
 OOOOoO00o0O = liveresolver . resolve ( url )
 I1I1I1IIi1III = xbmcgui . ListItem ( path = OOOOoO00o0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1I1IIi1III )
def II11IiiIII ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 o0OOOo = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OOOo )
def IiiiiI1i1Iii ( ) :
 ii1iiIiIII1ii = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  ii1iiIiIII1ii = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  ii1iiIiIII1ii = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  ii1iiIiIII1ii = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  ii1iiIiIII1ii = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return ii1iiIiIII1ii
 if 82 - 82: IiI1i11I
def O0o ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , i1iIiIIi :
  return i1iIiIIi
 return True
def oO0o00oo0 ( ) :
 if 19 - 19: IIiIiII11i + III1iiIii
 if 53 - 53: i1i1I1IIii1II - oOo0O0Ooo - i1i1I1IIii1II * IiI1i11I
 if 71 - 71: o0o00Oo0O - iI11I1II1I1I
 if 12 - 12: oooOo0oo0oo / I11i
 if 42 - 42: I1ii11iIi11i
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def II1IIiiIiI ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   i1II1I1Iii1 ( )
  if O0oO == 1 :
   iiI11Iii ( )
  if O0oO == 2 :
   O0o0O0 ( Ii1II1I11i1 )
  if O0oO == 3 :
   oOoooooOoO ( OoOOoOooooOOo )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 33 - 33: IIiIiII11i / i1iIi * o0o00Oo0O % o0ii1I * i1IiiiI1iI
def O0oO0OOoOOO0oO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 28 - 28: i1iIi + Ii / Iii % OOooOOo % I1ii11iIi11i - o0o00Oo0O
  if 54 - 54: ooOoO0O00 + IIiIiII11i
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
  if 83 - 83: Ii1I - oOo0O0Ooo + oooOo0oo0oo
  if 5 - 5: o0ii1I
  if 46 - 46: III1iiIii
 else :
  if 45 - 45: i1iIi
  if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
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
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COZY CORNER[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 21999990 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
   if 17 - 17: oooOo0oo0oo / oooOo0oo0oo / Iii
   if 1 - 1: ooOoO0O00 . Ii % oooOo0oo0oo
   if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % III1iiIii / o0ii1I . o0ii1I
   if 14 - 14: I11i . oooOo0oo0oo . Iii + ii - oooOo0oo0oo + III1iiIii
   if 9 - 9: o0ii1I
   if 59 - 59: oOo0O0Ooo * IIiIiII11i . o0o00Oo0O
   if 56 - 56: o0ii1I - IiI1i11I % oOo0O0Ooo - I11i
   if 51 - 51: o0o00Oo0O / i1iIi * iI11I1II1I1I + Ii1I + I11i
   if 98 - 98: iI11I1II1I1I * Ii1I * oooOo0oo0oo + i1iIi % Ii % o0o00Oo0O
   if 27 - 27: o0o00Oo0O
   if 79 - 79: I11i - Iii + I11i . i1i1I1IIii1II
   if 28 - 28: ooOoO0O00 - IiI1i11I
   if 54 - 54: IiI1i11I - o0o00Oo0O % oooOo0oo0oo
   if 73 - 73: o0o00Oo0O . OOooOOo + oOo0O0Ooo - Iii % Iii . Iii
   if 17 - 17: o0ii1I - ii % o0ii1I . III1iiIii / Ii % IiI1i11I
   if 28 - 28: Iii
   if 58 - 58: OOooOOo
   if 37 - 37: I1ii11iIi11i - iI11I1II1I1I / Ii1I
   if 73 - 73: Ii - III1iiIii
   if 25 - 25: ii + III1iiIii * Ii1I
   if 92 - 92: oOo0O0Ooo + Iii + o0o00Oo0O / I11i + i1IiiiI1iI
   if 18 - 18: i1iIi * OOooOOo . IiI1i11I / Ii1I / Ii
   if 21 - 21: i1i1I1IIii1II / Ii1I + o0ii1I + ii
   if 91 - 91: Ii / ooOoO0O00 + IiI1i11I + i1iIi * Ii
   if 66 - 66: iI11I1II1I1I % ooOoO0O00 - o0o00Oo0O + Iii * i1IiiiI1iI . III1iiIii
   if 52 - 52: i1iIi + o0o00Oo0O . IiI1i11I . Ii1I . oO0o
   if 97 - 97: oOo0O0Ooo / IiI1i11I
   if 71 - 71: IIiIiII11i / ooOoO0O00 . Ii1I % ii . OOooOOo
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def Iiiiii111i1ii ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  i1i1iII1 ( )
 if O0oO == 1 :
  iii11i1IIII ( )
 if O0oO == 2 :
  Iio00 ( )
 if O0oO == 3 :
  iiI1Ii1 ( )
 if O0oO == 4 :
  ii1i ( )
 if O0oO == 5 :
  oOOoo ( )
  if 14 - 14: I11i * i1i1I1IIii1II
  if 81 - 81: o0ii1I * I11i + i1IiiiI1iI + I1ii11iIi11i - ii
def i1i1I111iIi1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   oo00O00oO000o ( )
  if O0oO == 1 :
   OOo00OoO ( )
  if O0oO == 2 :
   iIi1 ( OoOOoOooooOOo )
  if O0oO == 3 :
   i11iiI1111 ( )
  if O0oO == 4 :
   oOoooo000Oo00 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0oO == 5 :
   OOoo ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 69 - 69: Iii
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def O00oO0 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 97 - 97: i1IiiiI1iI - iI11I1II1I1I
 if 75 - 75: ii * III1iiIii
 if 9 - 9: III1iiIii - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
 if 39 - 39: III1iiIii * I1ii11iIi11i + iI11I1II1I1I - III1iiIii + oooOo0oo0oo
 if 69 - 69: o0o00Oo0O
def o0ooO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Dans Scrapes[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   OoOOOo0o0ooo ( )
  if O0oO == 1 :
   I1iiiiI1iI ( 'http://www.tvmaze.com/shows' )
  if O0oO == 2 :
   iIiiiii1i ( )
  if O0oO == 3 :
   iiIi1IIiI ( )
  if O0oO == 4 :
   i1oO0OO0 ( )
  if O0oO == 5 :
   o0O0Oo00 ( )
  if O0oO == 6 :
   O0Oo0o000oO ( )
  if O0oO == 7 :
   oO0o00oOOooO0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Dans Scrapes[/COLOR]' , 'http://www.tvmaze.com/shows' , 9110001 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def Ii1ii111i1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   i1i1i1I = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 83 - 83: i1i1I1IIii1II + ii
   if 22 - 22: o0ii1I % IiI1i11I * ii - I11i / iI11I1II1I1I
   if 86 - 86: ii . IiI1i11I % OOooOOo / Iii * IiI1i11I / I11i
   if 64 - 64: Ii
  iI111iIIii = [ i1i1i1I , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   I1II ( )
  if O0oO == 1 :
   I1iIiI11I1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , i1oOOoo0o0OOOO , IiIi11iI )
  if O0oO == 2 :
   i1IiII1III ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0oO == 3 :
   I1iIiI11I1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , i1oOOoo0o0OOOO , IiIi11iI )
 else :
  if 30 - 30: o0o00Oo0O
  if 99 - 99: IIiIiII11i * III1iiIii % iI11I1II1I1I / o0ii1I
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 90 - 90: i1i1I1IIii1II % oooOo0oo0oo - oooOo0oo0oo % IIiIiII11i * oO0o
  if 39 - 39: Iii
  if 58 - 58: ooOoO0O00 % I11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 79 - 79: I11i % IiI1i11I * ii * iI11I1II1I1I . IiI1i11I / o0ii1I
  if 19 - 19: o0o00Oo0O + Iii + o0ii1I / IIiIiII11i / IIiIiII11i
  if 86 - 86: Ii1I * o0o00Oo0O * III1iiIii
  if 51 - 51: IIiIiII11i + III1iiIii . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
  if 72 - 72: i1i1I1IIii1II + i1i1I1IIii1II / IIiIiII11i . ii % o0ii1I
  if 49 - 49: i1i1I1IIii1II . oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
  if 2 - 2: ii % oooOo0oo0oo
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def I1ii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def i1IiII1III ( url ) :
 Oooo0O = OooOoooOo ( url )
 O00O0O = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O00O0O ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00O0O ) )
 Iiii1iI1i = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00O0O ) )
 for IiIi11iI , oO0O00oOOoooO , url in IIi :
  if '247ch' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 10190 , oO0O00oOOoooO )
  elif '.m3u' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 1019 , oO0O00oOOoooO )
  elif '.xml' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 1018 , oO0O00oOOoooO )
  else :
   oOOo0OOOOo0Oo ( IiIi11iI , url , 222 , oO0O00oOOoooO )
 for IiIi11iI , url , oO0O00oOOoooO in i1Iii1i1I :
  if '.xml' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 1018 , oO0O00oOOoooO )
  elif '.m3u' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 1019 , oO0O00oOOoooO )
  else :
   oOOo0OOOOo0Oo ( IiIi11iI , url , 222 , oO0O00oOOoooO )
 for IiIi11iI , url , oO0O00oOOoooO in Iiii1iI1i :
  oOOo0OOOOo0Oo ( IiIi11iI , url , 8043 , oO0O00oOOoooO )
def OOo0o ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def ii1iiIi1 ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url , oO0O00oOOoooO in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , oO0O00oOOoooO )
  if 34 - 34: oooOo0oo0oo
def OooO0ooo0o ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 47 - 47: ii
def ii1i1i1IiII ( url ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url , oo0oOO00oO , i11i1iIiii , i11I , o00O0O in IIi :
  if i11i1iIiii == '123' :
   i11i1iIiii = iiIi1IIiIi + 'appstreams.png'
  if i11I == '123' :
   i11I = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( IiIi11iI , url , 100010 , i11i1iIiii , i11I , o00O0O )
  elif 'playlist' in url :
   I1I1II1I11 ( IiIi11iI , url , 100007 , i11i1iIiii , i11I , o00O0O )
  elif 'watchseries' in url :
   I1I1II1I11 ( IiIi11iI , url , 100100 , i11i1iIiii , i11I , o00O0O )
  elif not 'http' in url :
   OOO00OO0oOo ( IiIi11iI , url , 100009 , i11i1iIiii , i11I , o00O0O , '' )
  else :
   OOO00OO0oOo ( IiIi11iI , url , 100005 , i11i1iIiii , i11I , o00O0O , '' )
   if 35 - 35: IiI1i11I + i1iIi - i1i1I1IIii1II . IiI1i11I . III1iiIii
def oo0ooOO ( url ) :
 II11iIiIIIiI = O0oII11I ( url )
 iiIiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , o00O0O , i11I , IiIi11iI in iiIiI1i1 :
  if oO0O00oOOoooO == '123' :
   oO0O00oOOoooO = iiIi1IIiIi + 'appstreams.png'
  if i11I == '123' :
   i11I = Oo00OOOOO
  if 'php' in url :
   I1I1II1I11 ( IiIi11iI , url , 100004 , oO0O00oOOoooO , i11I , o00O0O )
  elif 'playlist' in url :
   I1I1II1I11 ( IiIi11iI , url , 100007 , oO0O00oOOoooO , i11I , o00O0O )
  elif 'watchseries' in url :
   I1I1II1I11 ( IiIi11iI , url , 100100 , oO0O00oOOoooO , i11I , o00O0O )
  elif not 'http' in url :
   OOO00OO0oOo ( IiIi11iI , url , 100009 , oO0O00oOOoooO , i11I , o00O0O , '' )
  else :
   OOO00OO0oOo ( IiIi11iI , url , 100005 , oO0O00oOOoooO , i11I , o00O0O , '' )
   if 24 - 24: oO0o % oO0o * iI11I1II1I1I
def III ( url ) :
 if 1 - 1: i1i1I1IIii1II
 II11iIiIIIiI = O0oII11I ( url )
 oo00OooO = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00O0O in oo00OooO :
  i11i1iIiii = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O00O0O ) )
  for i11i1iIiii in i11i1iIiii :
   i11i1iIiii = i11i1iIiii
  IiIi11iI = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O00O0O ) )
  for IiIi11iI in IiIi11iI :
   if 'elete' in IiIi11iI :
    pass
   elif 'rivate Vid' in IiIi11iI :
    pass
   else :
    IiIi11iI = ( IiIi11iI ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  OO0o0oO = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O00O0O ) )
  for OO0o0oO in OO0o0oO :
   OO0o0oO = OO0o0oO
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O00O0O ) )
  for url in url :
   url = url
  OOO00OO0oOo ( '[COLORred]' + str ( OO0o0oO ) + '[/COLOR] : ' + str ( IiIi11iI ) , str ( url ) , 100009 , str ( i11i1iIiii ) , Oo00OOOOO , '' , '' )
  Ii1IIiI1i ( 'movies' , '' )
  if 83 - 83: I11i / Ii % iI11I1II1I1I . Iii % i1i1I1IIii1II . ii
def o00oO00 ( ) :
 OO0oOOo = iIii1 . input ( 'Search Dans Scrapes' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://www.tvmaze.com/search?q=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 II11iIiIIIiI = OooOoooOo ( III111i11IiI )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  O0000 = 'http://www.tvmaze.com' + OoOOoOooooOOo . replace ( '"' , '' )
  ooO00O0O0 = requests . get ( O0000 ) . content
  IIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( ooO00O0O0 )
  for o00O0O in IIi :
   if not '<div>' in o00O0O :
    iII1I1 = o00O0O . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   oO0O00oOOoooO = 'http:' + oO0O00oOOoooO
   IiIi11iI = IiIi11iI . replace ( '&#039;' , '' )
   if IiIi11iI == '' :
    o0Ooo0o0ooo0 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( OoOOoOooooOOo ) )
    for IiIi11iI in o0Ooo0o0ooo0 :
     IiIi11iI = IiIi11iI . replace ( '-' , ' ' )
  oo0o0000Oo0 ( IiIi11iI , O0000 , 9110002 , oO0O00oOOoooO , Oo00OOOOO , iII1I1 , '' )
  if 80 - 80: i1IiiiI1iI - I1ii11iIi11i
def I1iiiiI1iI ( url ) :
 IIi1i1IiIIi1i ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 9110004 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
 Oooo0O = requests . get ( url ) . content
 IIi = re . compile ( '<div class="img">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( Oooo0O )
 iII1i11 = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  O0000 = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  ooO00O0O0 = requests . get ( O0000 ) . content
  IIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( ooO00O0O0 )
  for o00O0O in IIi :
   if not '<div>' in o00O0O :
    iII1I1 = o00O0O . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   oO0O00oOOoooO = 'http:' + oO0O00oOOoooO
   IiIi11iI = IiIi11iI . replace ( '&#039;' , '' )
   if IiIi11iI == '' :
    o0Ooo0o0ooo0 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for IiIi11iI in o0Ooo0o0ooo0 :
     IiIi11iI = IiIi11iI . replace ( '-' , ' ' )
  oo0o0000Oo0 ( IiIi11iI , O0000 , 9110002 , oO0O00oOOoooO , Oo00OOOOO , iII1I1 , '' )
  if 96 - 96: Ii1I / IIiIiII11i . o0ii1I - IiI1i11I * Iii * i1i1I1IIii1II
 for o0OO0o0oOOO0O in iII1i11 :
  url = 'http://www.tvmaze.com' + o0OO0o0oOOO0O
  oo0o0000Oo0 ( 'NEXT' , url , 9110001 , oO0O00oOOoooO , Oo00OOOOO , '' , '' )
def O00oo0ooO ( url ) :
 Oooo0O = requests . get ( url ) . content
 IIi = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( Oooo0O )
 for o00O0O in IIi :
  iII1I1 = o00O0O . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
 return iII1I1
def iiIii1ii ( url , name , iconimage ) :
 iIIIII1iiiiII = name
 oO0O00oOOoooO = iconimage
 Oooo0O = requests . get ( url + '/episodes' ) . content
 ooO00O0O0 = requests . get ( url ) . content
 O00O0O = re . compile ( "<h2 data-magellan-destination='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( ooO00O0O0 )
 for oooO in IIi :
  oooO = oooO . replace ( ' ' , '' )
 for I111i1I1 , O0o00OOo00O0O in O00O0O :
  if not 'special' in I111i1I1 . lower ( ) :
   I111i1I1 = I111i1I1 . replace ( 'S' , '' ) . replace ( 's' , '' )
  II1i = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( O0o00OOo00O0O ) )
  for Oo , OOoO000O00oO , i1OoOO in II1i :
   if not 'special' in Oo . lower ( ) :
    oo0o0000Oo0 ( iIIIII1iiiiII + ' - SEASON -' + I111i1I1 + '- EPISODE-' + Oo + '-' + oooO , '' , 9110003 , oO0O00oOOoooO , Oo00OOOOO , '' , iIIIII1iiiiII )
    if 44 - 44: oooOo0oo0oo
    if 54 - 54: o0ii1I - Iii - i1IiiiI1iI . iI11I1II1I1I
    if 79 - 79: o0ii1I . oO0o
def IIiI1I1 ( name , extra ) :
 if 15 - 15: o0ii1I * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Checking for stream' )
 from imports import Scrape_Nan
 Oo00OOOOoo0oo = name + '<>'
 O00OOooo0Ooo = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( Oo00OOOOoo0oo ) )
 for iIIIII1iiiiII , o0oOOoOOO , iiI1i11II , oooO in O00OOooo0Ooo :
  iIIIII1iiiiII = iIIIII1iiiiII
  o0oOOoOOO = o0oOOoOOO
  iiI1i11II = iiI1i11II
  II11 = ''
  Scrape_Nan . scrape_episode ( iIIIII1iiiiII , oooO , '' , o0oOOoOOO , iiI1i11II , '' )
if 15 - 15: III1iiIii / o0o00Oo0O . I11i . Ii
if 59 - 59: i1IiiiI1iI - I11i - i1iIi
if 48 - 48: ooOoO0O00 + Iii % OOooOOo / I1ii11iIi11i - I11i
if 67 - 67: i1i1I1IIii1II % I11i . ii + oooOo0oo0oo * Iii * OOooOOo
if 36 - 36: o0o00Oo0O + I1ii11iIi11i
if 5 - 5: I1ii11iIi11i * OOooOOo
if 46 - 46: i1iIi
if 33 - 33: IiI1i11I - IIiIiII11i * ii - I1ii11iIi11i - oooOo0oo0oo
if 84 - 84: i1IiiiI1iI + I1ii11iIi11i - OOooOOo * OOooOOo
if 61 - 61: ii . i1i1I1IIii1II . ii / I1ii11iIi11i
if 72 - 72: ooOoO0O00
def OOoo0oo ( ) :
 oo0o0000Oo0 ( 'Featured 24/7' , '' , 9070000 , iiIi1IIiIi + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 oo0o0000Oo0 ( '24/7 Tv Shows' , '' , 9080000 , iiIi1IIiIi + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 oo0o0000Oo0 ( '24/7 Movies' , '' , 9090000 , iiIi1IIiIi + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 oo0o0000Oo0 ( '24/7 Cable' , '' , 9100000 , iiIi1IIiIi + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 oo0o0000Oo0 ( '24/7 Random Stream' , '' , 9110000 , iiIi1IIiIi + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 58 - 58: i1i1I1IIii1II
def IiIIi1IiiI1 ( ) :
 OoOOoOooooOOo = 'http://arconaitv.me/'
 oO00oOo0OOO = 'index.php#shows'
 Oooo0O = BeautifulSoup ( requests . get ( OoOOoOooooOOo + oO00oOo0OOO ) . content )
 ii1 = Oooo0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for ooO in ii1 :
  oOoOoO000OO = ooO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in oOoOoO000OO :
   ii11II11 = iiI111I1iIiI . text
  oOo = ooO . findAll ( 'a' )
  for iiI111I1iIiI in oOo :
   if iiI111I1iIiI . has_key ( 'href' ) :
    oOo00OooO0oO = OoOOoOooooOOo + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    IiIi11iI = iiI111I1iIiI [ 'title' ]
   ooO00O0O0 = BeautifulSoup ( requests . get ( oOo00OooO0oO ) . content )
   I1IIi = ooO00O0O0 . findAll ( 'source' )
   for O0OOOo in I1IIi :
    i11I1I1iiI = O0OOOo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOO00OO0oOo ( IiIi11iI , i11I1I1iiI , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 34 - 34: Iii % i1iIi . o0o00Oo0O . iI11I1II1I1I
    if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
def O0O00OOo ( ) :
 OoOOoOooooOOo = 'http://arconaitv.me/'
 oO00oOo0OOO = 'index.php#movies'
 Oooo0O = BeautifulSoup ( requests . get ( OoOOoOooooOOo + oO00oOo0OOO ) . content )
 ii1 = Oooo0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for ooO in ii1 :
  oOoOoO000OO = ooO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in oOoOoO000OO :
   ii11II11 = iiI111I1iIiI . text
  oOo = ooO . findAll ( 'a' )
  for iiI111I1iIiI in oOo :
   if iiI111I1iIiI . has_key ( 'href' ) :
    oOo00OooO0oO = OoOOoOooooOOo + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    IiIi11iI = iiI111I1iIiI [ 'title' ]
   ooO00O0O0 = BeautifulSoup ( requests . get ( oOo00OooO0oO ) . content )
   I1IIi = ooO00O0O0 . findAll ( 'source' )
   for O0OOOo in I1IIi :
    i11I1I1iiI = O0OOOo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOO00OO0oOo ( IiIi11iI , i11I1I1iiI , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 66 - 66: Ii / I11i - ii / ooOoO0O00 . Ii
    if 16 - 16: I1ii11iIi11i % Ii1I + Iii - o0o00Oo0O . IiI1i11I / i1IiiiI1iI
def IIi1I ( ) :
 OoOOoOooooOOo = 'http://arconaitv.me/'
 oO00oOo0OOO = 'index.php#cable'
 Oooo0O = BeautifulSoup ( requests . get ( OoOOoOooooOOo + oO00oOo0OOO ) . content )
 ii1 = Oooo0O . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for ooO in ii1 :
  oOoOoO000OO = ooO . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in oOoOoO000OO :
   ii11II11 = iiI111I1iIiI . text
  oOo = ooO . findAll ( 'a' )
  for iiI111I1iIiI in oOo :
   if iiI111I1iIiI . has_key ( 'href' ) :
    oOo00OooO0oO = OoOOoOooooOOo + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    IiIi11iI = iiI111I1iIiI [ 'title' ]
   ooO00O0O0 = BeautifulSoup ( requests . get ( oOo00OooO0oO ) . content )
   I1IIi = ooO00O0O0 . findAll ( 'source' )
   for O0OOOo in I1IIi :
    i11I1I1iiI = O0OOOo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOO00OO0oOo ( IiIi11iI , i11I1I1iiI , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 27 - 27: o0o00Oo0O . i1IiiiI1iI / IiI1i11I
def OO00O000OOO ( ) :
 ooO00O0O0 = BeautifulSoup ( requests . get ( 'http://arconaitv.me/stream.php?id=random' ) . content )
 I1IIi = ooO00O0O0 . findAll ( 'source' )
 for O0OOOo in I1IIi :
  i11I1I1iiI = O0OOOo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  OOO00OO0oOo ( 'Random Pick' , i11I1I1iiI , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 3 - 3: o0o00Oo0O
def Ooo0Oo0oo0 ( ) :
 OoOOoOooooOOo = 'http://arconaitv.me/'
 oO00oOo0OOO = 'index.php#shows'
 if 83 - 83: i1IiiiI1iI
 Oooo0O = BeautifulSoup ( requests . get ( OoOOoOooooOOo + oO00oOo0OOO ) . content )
 ii1 = Oooo0O . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for ooO in ii1 :
  oOoOoO000OO = ooO . findAll ( 'a' )
  for iiI111I1iIiI in oOoOoO000OO :
   if iiI111I1iIiI . has_key ( 'href' ) :
    oOo00OooO0oO = OoOOoOooooOOo + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    IiIi11iI = iiI111I1iIiI [ 'title' ]
   ii111Ii11iii = iiI111I1iIiI . findAll ( 'img' )
   for o00OOoOOO000O0 in ii111Ii11iii :
    oO0O00oOOoooO = OoOOoOooooOOo + o00OOoOOO000O0 [ 'src' ]
    ooO00O0O0 = BeautifulSoup ( requests . get ( oOo00OooO0oO ) . content )
    I1IIi = ooO00O0O0 . findAll ( 'source' )
    for O0OOOo in I1IIi :
     i11I1I1iiI = O0OOOo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     OOO00OO0oOo ( IiIi11iI , i11I1I1iiI , 9060000 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
     if 92 - 92: Ii1I / o0o00Oo0O
def oOO0o00O ( name , url ) :
 import urlresolver
 try :
  oOoO = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( oOoO , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + Iii
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , o00O0O , i11I , IiIi11iI in iiIiI1i1 :
  if '.php' in url :
   I1I1II1I11 ( IiIi11iI , url , 100210 , oO0O00oOOoooO , i11I , o00O0O )
  else :
   Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , i11I , o00O0O )
   if 40 - 40: IiI1i11I . i1i1I1IIii1II + oOo0O0Ooo + Ii1I + i1IiiiI1iI
   if 26 - 26: iI11I1II1I1I
   if 87 - 87: Ii1I / ii - I1ii11iIi11i % OOooOOo % III1iiIii % I1ii11iIi11i
def Ii1 ( iconimage , url , extra ) :
 i11i1iIiii = ' '
 I1iiiiii = ' '
 i11I = ' '
 o0oOOoOOO = ' '
 o0OO0Oo = O0oII11I ( url )
 i11i1iIiii = re . compile ( '<img src="(.+?)">' ) . findall ( o0OO0Oo )
 for i11i1iIiii in i11i1iIiii :
  i11i1iIiii = i11i1iIiii
 I11iiii1I = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( o0OO0Oo )
 for i11I in I11iiii1I :
  i11I = i11I
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( o0OO0Oo )
 for url , o0oOOoOOO in IIi :
  o0oOOoOOO = 'S' + ( o0oOOoOOO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  oo0o0000Oo0 ( ( o0oOOoOOO ) . replace ( '  ' , '' ) , url , 100101 , i11i1iIiii , i11I , I1iiiiii , '' )
  Ii1IIiI1i ( 'Movies' , 'info' )
  if 3 - 3: o0o00Oo0O % ii / oooOo0oo0oo
def ooOo ( url , name , fanart , extra , iconimage ) :
 o0oO0OoO0 = extra
 o0oOOoOOO = name
 o0OO0Oo = O0oII11I ( url )
 i11i1iIiii = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( o0OO0Oo )
 for url , name , oOOOOOoOO in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  oOOOOOoOO = oOOOOOoOO
  oooo00 = name + ' - [COLORred]' + oOOOOOoOO + '[/COLOR]'
  oo0o0000Oo0 ( oooo00 , url , 100102 , i11i1iIiii , fanart , 'Aired : ' + oOOOOOoOO , oooo00 )
  if 35 - 35: i1IiiiI1iI . OOooOOo * Ii
def iiII ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = O0oII11I ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , name in IIi :
  for I1I1I1IIi1III in o00OO00OoO :
   if I1I1I1IIi1III in OoOOoOooooOOo :
    URL = 'http://www.watchseriesgo.to/link/' + OoOOoOooooOOo
    OOO00OO0oOo ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  oo0o0000Oo0 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 57 - 57: Iii . I1ii11iIi11i + IIiIiII11i
  if 43 - 43: i1IiiiI1iI % IiI1i11I
def o0O0ooOOoO ( url , name ) :
 iIi11ii = name
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 Iiii1iI1i = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  i11I1 ( url , iIi11ii )
 for url in i1Iii1i1I :
  i11I1 ( url , iIi11ii )
 for url in Iiii1iI1i :
  i11I1 ( url , iIi11ii )
  if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
def i11I1 ( url , season_name ) :
 if 'daclips.in' in url :
  I1iI1I1 ( url , season_name )
 elif 'filehoot.com' in url :
  IiIi1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  oo00ooOoo ( url , season_name )
 elif 'vidspot.net' in url :
  iii1IIIiiiI ( url , season_name )
 elif 'vodlocker' in url :
  OoO00oo00 ( url , season_name )
 elif 'vidto' in url :
  Oo0Oo0O ( url , season_name )
  if 44 - 44: ii % ii
  if 35 - 35: IiI1i11I / Ii1I * ii . IIiIiII11i / I1ii11iIi11i
def Oo0Oo0O ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Iii11i , IiIi11iI in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 12 - 12: IiI1i11I . III1iiIii . OOooOOo / o0o00Oo0O
  if 58 - 58: I11i - IIiIiII11i % i1i1I1IIii1II + i1IiiiI1iI . OOooOOo / III1iiIii
def oo00ooOoo ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Iii11i , IiIi11iI in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 8 - 8: Ii1I . oO0o * Iii + IIiIiII11i % Ii
def iii1IIIiiiI ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for Iii11i , IiIi11iI in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 8 - 8: i1iIi * o0o00Oo0O
def OoO00oo00 ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Iii11i in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 73 - 73: I11i / i1i1I1IIii1II / Iii / oO0o
def I1iI1I1 ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for Iii11i in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 11 - 11: OOooOOo + III1iiIii - ii / oO0o
def IiIi1 ( url , season_name ) :
 II11iIiIIIiI = O0oII11I ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Iii11i in IIi :
  OOOOOOoO ( Iii11i , season_name )
  if 34 - 34: i1iIi
def OOOOOOoO ( Link , season_name ) :
 if 'http:/' in Link :
  i1iI1 ( Link )
  if 44 - 44: Ii1I - o0ii1I / IIiIiII11i * oO0o * I1ii11iIi11i
  if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * oooOo0oo0oo % IIiIiII11i
def OooOoOOo0oO00 ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 O00O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in O00O :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 91 - 91: Iii / o0o00Oo0O - o0ii1I . oOo0O0Ooo
def oo0o0000Oo0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = True )
 return o0iIiiIiiIi
 if 62 - 62: o0o00Oo0O / oOo0O0Ooo % o0o00Oo0O * oO0o % oOo0O0Ooo
 if 33 - 33: oOo0O0Ooo . i1i1I1IIii1II * oO0o * iI11I1II1I1I
def OOO00OO0oOo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  II11i111i1iIiiIiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = False )
 return o0iIiiIiiIi
 if 26 - 26: iI11I1II1I1I % Ii % Ii1I
def oo0O ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 6 - 6: I1ii11iIi11i . III1iiIii / III1iiIii - Ii
def OO0oIiII1iiI ( url ) :
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iII . play ( url ) . strip ( )
 except : pass
 if 9 - 9: i1i1I1IIii1II * ooOoO0O00 - ooOoO0O00
def i1iI1 ( url ) :
 iII = xbmc . Player ( )
 import urlresolver
 try : iII . play ( url )
 except : pass
 if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . III1iiIii % Iii / I11i
def O0oII11I ( url ) :
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
  if 14 - 14: iI11I1II1I1I * i1IiiiI1iI * Ii1I / iI11I1II1I1I * III1iiIii / Iii
  if 77 - 77: oO0o + i1IiiiI1iI + i1IiiiI1iI * o0ii1I / ii . o0ii1I
  if 62 - 62: ooOoO0O00 - ooOoO0O00
def iii11i1IIII ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   oOOO0O0Ooo ( )
  if O0oO == 1 :
   IiI1i111IiIiIi1 ( )
  if O0oO == 2 :
   i1II11II1 ( )
  if O0oO == 3 :
   II1IIIii ( )
  if O0oO == 4 :
   iIIIiIi1I1i ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def iiI1Ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiIi1IIiIi + 'Fitness.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Go Fishing[/COLOR]' , str ( oO0000OOo00 ) , 8090 , iiIi1IIiIi + 'GoFishing.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiIi1IIiIi + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
 if 91 - 91: iI11I1II1I1I % oO0o . I11i + o0ii1I + I11i
 if 95 - 95: o0ii1I + Ii1I * oooOo0oo0oo
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   I1Ii = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + I1Ii + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO == 0 :
    ooooOoO0O ( II1I )
    OoOO0o ( )
   elif O0oO == 1 :
    IIII ( II1I )
  else :
   pass
   if 8 - 8: I11i / Ii1I - Ii % iI11I1II1I1I
def IIII ( addon ) :
 I1Ii = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 66 - 66: III1iiIii
def ooooOoO0O ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 O0oOo = os . path . join ( IIIII , 'default.py' )
 OO0oOO0ooO = open ( O0oOo , "w+" )
 if 38 - 38: oO0o
 OO0oOO0ooO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OO0oOO0ooO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OO0oOO0ooO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 56 - 56: oooOo0oo0oo . IIiIiII11i
 if 53 - 53: i1i1I1IIii1II % Iii . i1iIi - OOooOOo
 if 69 - 69: IIiIiII11i * oOo0O0Ooo - i1iIi - iI11I1II1I1I + I11i - i1i1I1IIii1II
 if 50 - 50: Iii - i1iIi
def ii111IIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1iIiI1Iiii = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1III1II1I11 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Iiii1iI1i = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOoOooOoOOOoo = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi11 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url , ooo0O0OOO000o , i11I , o00O0O in i1iIiI1Iiii :
  if 'php' in url :
   I1I1II1I11 ( IiIi11iI , url , 90037 , ooo0O0OOO000o , i11I , o00O0O )
  elif IiIi11iI == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , ooo0O0OOO000o , i11I , o00O0O )
  else :
   Ii1I1i ( IiIi11iI , url , 222 , ooo0O0OOO000o , i11I , o00O0O )
 for IiIi11iI , oO0O00oOOoooO , url , iiI1iii in I1III1II1I11 :
  I1I1II1I11 ( IiIi11iI , url , 90037 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , oO0O00oOOoooO , url , iiI1iii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 90037 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , url , oO0O00oOOoooO , iiI1iii in i1Iii1i1I :
  Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , url , oO0O00oOOoooO , iiI1iii in Iiii1iI1i :
  Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , url , oO0O00oOOoooO , iiI1iii in OOoOooOoOOOoo :
  Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , url , oO0O00oOOoooO in IIi11 :
  Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , '' , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def OOoOOo00O0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , oO0O00oOOoooO , url , iiI1iii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 90037 , oO0O00oOOoooO , iiI1iii , '' )
 for IiIi11iI , url , oO0O00oOOoooO , iiI1iii in i1Iii1i1I :
  Ii1I1i ( IiIi11iI , url , 222 , oO0O00oOOoooO , iiI1iii , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % i1IiiiI1iI . Ii1I % o0o00Oo0O
def iIiIi1ii ( ) :
 iiiiiII = [ 'serialsearch' , 'moviesearch' ]
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 if III111i11IiI == '' :
  pass
 else :
  for ii1ii in iiiiiII :
   IIiI1i = Oo0o0000o0o0 + ii1ii + '.php'
   o0OO0Oo = OooOoooOo ( IIiI1i )
   if o0OO0Oo != 'Opened' :
    iiIiI1i1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( o0OO0Oo )
    for IiIi11iI , OoOOoOooooOOo , ooo0O0OOO000o , i11I , o00O0O in iiIiI1i1 :
     if III111i11IiI in IiIi11iI . lower ( ) :
      iII1 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for I1I1I1IIi1III in iII1 :
       if I1I1I1IIi1III == OoOOoOooooOOo :
        IiIi11iI = '[COLORred]* [/COLOR]' + ( IiIi11iI ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        O000O = open ( OOOO0OOoO0O0 , "a" )
        O000O . write ( 'item="' + IiIi11iI + '"\n' )
        O000O . close
      if 'php' in OoOOoOooooOOo :
       I1I1II1I11 ( IiIi11iI , OoOOoOooooOOo , 90037 , ooo0O0OOO000o , i11I , o00O0O )
      else :
       Ii1I1i ( IiIi11iI , OoOOoOooooOOo , 222 , ooo0O0OOO000o , i11I , o00O0O )
       if 98 - 98: iI11I1II1I1I + i1IiiiI1iI % OOooOOo + Iii % OOooOOo
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   if 24 - 24: i1i1I1IIii1II * i1IiiiI1iI
def I11IiIIIi ( ) :
 if 77 - 77: iI11I1II1I1I . o0ii1I % i1i1I1IIii1II / o0ii1I
 if 54 - 54: i1i1I1IIii1II + i1iIi - I1ii11iIi11i
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
 if 49 - 49: Iii . i1iIi * OOooOOo % III1iiIii . o0o00Oo0O
 if 48 - 48: o0o00Oo0O * o0ii1I - o0o00Oo0O / o0ii1I + OOooOOo
 if 52 - 52: oO0o % o0ii1I * IIiIiII11i
 if 4 - 4: Iii % o0o00Oo0O - ii + i1iIi . i1i1I1IIii1II % IIiIiII11i
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
 Oooo0O = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 ooO00O0O0 = requests . get ( 'http://www.djing.com/' ) . content
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( ooO00O0O0 )
 ii1 = Oooo0O . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for ooO in ii1 :
  oOoOoO000OO = ooO . findAll ( 'a' )
  for iiI111I1iIiI in oOoOoO000OO :
   if iiI111I1iIiI . has_attr ( 'href' ) :
    oOo00OooO0oO = 'https://tvcatchup.com' + iiI111I1iIiI [ 'href' ]
   ii111Ii11iii = iiI111I1iIiI . findAll ( 'img' )
   for o00OOoOOO000O0 in ii111Ii11iii :
    oO0O00oOOoooO = o00OOoOOO000O0 [ 'src' ]
    oo0 = o00OOoOOO000O0 [ 'alt' ]
   IIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( iiI111I1iIiI ) )
   for i1iIIi1II1iiI in IIi :
    oOOo0OOOOo0Oo ( ( '[COLORgold]' + oo0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + i1iIIi1II1iiI + '[/COLOR]' ) , oOo00OooO0oO , 90024 , oO0O00oOOoooO )
    if 31 - 31: I11i % Iii + iI11I1II1I1I + Ii * i1IiiiI1iI
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in i1Iii1i1I :
  if 'Submit' in IiIi11iI :
   pass
  elif '&lt;' in IiIi11iI :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 90025 , 'http://www.djing.com' + oO0O00oOOoooO , Oo00OOOOO , '' )
   if 45 - 45: oooOo0oo0oo * i1IiiiI1iI . i1iIi - i1IiiiI1iI + III1iiIii
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def iIIOOoO0oO00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 10 - 10: oO0o
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OO0o0oO0O000o ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 47 - 47: i1IiiiI1iI - oO0o / o0ii1I * ii / o0ii1I . I1ii11iIi11i
def iiII1IiIi1iI1 ( ) :
 II11iIiIIIiI = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 oOiiI1Ii11II1I = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1Ii11II1I1 , IiI1iI1IiiIi1 , OoO0oo in oOiiI1Ii11II1I :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + I1Ii11II1I1 + IiI1iI1IiiIi1 + OoO0oo + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OoOOoOooooOOo , 10201 , iiIi1IIiIi + 'rated.png' )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'yr' in OoOOoOooooOOo :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OoOOoOooooOOo , 10201 , iiIi1IIiIi + 'rated.png' )
   if 72 - 72: o0o00Oo0O + oOo0O0Ooo - IiI1i11I - oO0o
def OOo00OoO ( ) :
 if 100 - 100: o0o00Oo0O
 if 79 - 79: iI11I1II1I1I
 if 81 - 81: oooOo0oo0oo + iI11I1II1I1I * i1IiiiI1iI - iI11I1II1I1I . oooOo0oo0oo
 if 48 - 48: Iii . ii . oOo0O0Ooo . OOooOOo % Ii1I / IiI1i11I
 if 11 - 11: ooOoO0O00 % oO0o % IiI1i11I
 if 99 - 99: i1iIi / iI11I1II1I1I - o0ii1I * Ii1I % oOo0O0Ooo
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'yr' in OoOOoOooooOOo :
   oo0o0000Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OoOOoOooooOOo , 10201 , iiIi1IIiIi + 'rated.png' , '' , IiIi11iI , '' )
   if 13 - 13: oO0o
def O0oo0O0 ( name , url , description ) :
 iII1I1 = description
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iiII111iIII1Ii , url , name in IIi :
  if 'id' in url :
   iI1IiiiIiI1Ii = name
   oo0o0000Oo0 ( ( '[COLORred]RANK [COLORblue]' + iiII111iIII1Ii + '[COLORred] - [COLORblue]' + name + '[/COLOR]' ) , name , 9110005 , iiIi1IIiIi + 'rated.png' , '' , iII1I1 , iI1IiiiIiI1Ii )
   if 78 - 78: ii / oooOo0oo0oo % OOooOOo * ii
   if 68 - 68: i1i1I1IIii1II
def i11i11 ( description , url ) :
 if 18 - 18: iI11I1II1I1I + Iii * oOo0O0Ooo - oooOo0oo0oo / oOo0O0Ooo
 o00iI1i1II = ( str ( description ) )
 iIIIII1iiiiII = ( str ( url ) )
 xbmc . log ( 'title:' + iIIIII1iiiiII + '# year:' + o00iI1i1II , xbmc . LOGNOTICE )
 from imports import Scrape_Nan
 Scrape_Nan . scrape_movie ( iIIIII1iiiiII , o00iI1i1II , '' )
 if 14 - 14: i1iIi - iI11I1II1I1I / o0o00Oo0O % III1iiIii . OOooOOo
 if 18 - 18: i1i1I1IIii1II * i1i1I1IIii1II % i1i1I1IIii1II
 if 17 - 17: o0o00Oo0O * OOooOOo * Ii1I * IIiIiII11i * Iii % ooOoO0O00
 if 33 - 33: Ii1I * Ii1I . i1iIi . Ii
 if 48 - 48: I11i . o0ii1I + OOooOOo % Ii1I / Ii
 if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + III1iiIii % Ii % OOooOOo
 if 78 - 78: o0ii1I + OOooOOo + III1iiIii - III1iiIii . Ii / oO0o
def I11i11i1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OOOii1i1iiI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0oOOo = ( url )
 III111i11IiI = OO0oOOo . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 O0000 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 Oo0oOo0ooOOOo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO0000o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 o0Ii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IIi1IiII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0IIIIiI11I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OO0oOOo
 iiiI11iIIi1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 o00OoooooooOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 32 - 32: I11i + oOo0O0Ooo . i1IiiiI1iI
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1Ii11IiI1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 74 - 74: Ii1I . oO0o / oO0o * o0o00Oo0O . Ii1I - ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( O0000 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0oOo0ooOOOo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO0000o )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oOIIi = O00O0oOO00O00 ( o0Ii1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 I1Ii1IIiI11i1 = O00O0oOO00O00 ( o0IIIIiI11I )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 Ii11I1iIiiI = O00O0oOO00O00 ( iiiI11iIIi1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0o0OO00 = O00O0oOO00O00 ( o00OoooooooOo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 14 - 14: Ii1I + Ii
 if 83 - 83: Ii1I / Ii + IIiIiII11i . IiI1i11I * oooOo0oo0oo + III1iiIii
 iiii1i1II1 = O00O0oOO00O00 ( iIi )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ooOO0ooo0o = O00O0oOO00O00 ( Ii1Ii11IiI1I1 )
 if 17 - 17: i1IiiiI1iI + I1ii11iIi11i
 if 29 - 29: I11i * ii % o0ii1I . I11i
 if 88 - 88: oOo0O0Ooo % oooOo0oo0oo % Ii1I . Ii % I11i
 if 38 - 38: i1IiiiI1iI + ii . ooOoO0O00
 if 19 - 19: IiI1i11I - I11i - o0ii1I - OOooOOo . IiI1i11I . i1IiiiI1iI
 if 48 - 48: IiI1i11I + III1iiIii
 if 60 - 60: Iii + IiI1i11I . III1iiIii / ooOoO0O00 . iI11I1II1I1I
 if 14 - 14: oooOo0oo0oo
 if 79 - 79: o0ii1I
 if 76 - 76: iI11I1II1I1I
 if 80 - 80: iI11I1II1I1I . o0o00Oo0O / o0ii1I % o0ii1I
 if 93 - 93: ii * I1ii11iIi11i
 if 10 - 10: i1IiiiI1iI * ii + Iii - Ii1I / Ii1I . Ii
 if O0o0OO00 != 'Failed' :
  i1I1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0o0OO00 )
  for url , IiIi11iI in i1I1i :
   IIII1iIIii = O00O0oOO00O00 ( url )
   IiiOooooOo0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIII1iIIii )
   for I1ii1 , I1IiIiI in IiiOooooOo0 :
    I1IiIiI = ( I1IiIiI . replace ( '.' , ' ' ) )
    if III111i11IiI in I1IiIiI . lower ( ) :
     if '.mkv' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 222 , '' , '' , '' )
     elif '.mp4' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 222 , '' , '' , '' )
     elif '.avi' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 222 , '' , '' , '' )
     elif '.wav' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 60 - 60: i1IiiiI1iI
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i1Iii1i1I :
   if OO0oOOo in IiIi11iI . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 98 - 98: i1iIi
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: iI11I1II1I1I * Iii * Iii / Ii1I
 if o00OooOO000 != 'Failed' :
  Iiii1iI1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for IIIIIIi1i , IiIi11iI in Iiii1iI1i :
   if OO0oOOo in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Oo0oOo0ooOOOo + IIIIIIi1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in OOoOooOoOOOoo :
   if OO0oOOo in IiIi11iI . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if oOIIi != 'Failed' :
  O0oOoo = [ ]
  IIi11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOIIi )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in IIi11 :
   if OO0oOOo in IiIi11iI . lower ( ) :
    if IiIi11iI in O0oOoo :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
     O0oOoo . append ( IiIi11iI )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if I1Ii1IIiI11i1 != 'Failed' :
  OoOOoO0O0oO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I1Ii1IIiI11i1 )
  for url , oO0O00oOOoooO , IiIi11iI in OoOOoO0O0oO :
   if OO0oOOo in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , oO0O00oOOoooO )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 92 - 92: I1ii11iIi11i / Ii + Ii1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 87 - 87: OOooOOo % iI11I1II1I1I
    if 72 - 72: oooOo0oo0oo . oooOo0oo0oo - Ii1I
    if 48 - 48: I1ii11iIi11i - i1iIi + I1ii11iIi11i - oOo0O0Ooo * Ii . IiI1i11I
    if 35 - 35: III1iiIii . o0o00Oo0O + I1ii11iIi11i + oooOo0oo0oo + ooOoO0O00
    if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
    if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
    if 58 - 58: oooOo0oo0oo . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
    if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
    if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
    if 66 - 66: oO0o % I11i
    if 21 - 21: OOooOOo - ii % Ii
    if 71 - 71: ooOoO0O00 - Iii * i1IiiiI1iI + i1i1I1IIii1II - oO0o % Ii1I
    if 63 - 63: iI11I1II1I1I + oooOo0oo0oo . oO0o / oOo0O0Ooo
    if 84 - 84: ooOoO0O00
    if 42 - 42: IIiIiII11i - oO0o - ii . IiI1i11I / OOooOOo
    if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
    if 81 - 81: III1iiIii / OOooOOo * III1iiIii . o0o00Oo0O
    if 61 - 61: oO0o * oooOo0oo0oo + i1IiiiI1iI . iI11I1II1I1I % Iii . i1IiiiI1iI
 if iiii1i1II1 != 'Failed' :
  O0o0oo0oOO0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiii1i1II1 )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in O0o0oo0oOO0oO :
   if OO0oOOo in IiIi11iI . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 15 - 15: oO0o * IIiIiII11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: i1IiiiI1iI + oO0o / oooOo0oo0oo
    if 97 - 97: I1ii11iIi11i * IiI1i11I % i1iIi . IiI1i11I - i1IiiiI1iI - oooOo0oo0oo
    if 79 - 79: oOo0O0Ooo - i1iIi
    if 37 - 37: III1iiIii . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
    if 83 - 83: III1iiIii / i1IiiiI1iI
    if 64 - 64: oO0o % III1iiIii . i1IiiiI1iI % oO0o + Iii * III1iiIii
    if 83 - 83: I11i % i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
    if 65 - 65: iI11I1II1I1I % i1i1I1IIii1II + o0o00Oo0O / ii
    if 52 - 52: o0ii1I % oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
    if 80 - 80: ii + III1iiIii
 O00OOo0oOOooO0o0O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 92 - 92: iI11I1II1I1I % ii % III1iiIii
 for ii1ii in O00OOo0oOOooO0o0O :
  IIiI1i = oO0 + ii1ii + oOoOooOo0o0
  O0o0OO00 = O00O0oOO00O00 ( IIiI1i )
  if O0o0OO00 != 'Failed' :
   i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0OO00 )
   for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i1I1i :
    if OO0oOOo in IiIi11iI . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 79 - 79: iI11I1II1I1I + III1iiIii
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 61 - 61: oooOo0oo0oo / oO0o + IIiIiII11i . i1i1I1IIii1II / I1ii11iIi11i * oooOo0oo0oo
 O00OOo0oOOooO0o0O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 46 - 46: iI11I1II1I1I
 if 33 - 33: Iii % Iii % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
 for ii1ii in O00OOo0oOOooO0o0O :
  IIiI1i = OOOii1i1iiI + ii1ii
  O0O0ooOoOO0OO = O00O0oOO00O00 ( IIiI1i )
  if O0O0ooOoOO0OO != 'Failed' :
   I1iiIiiii1111 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0O0ooOoOO0OO )
   for IIIIIIi1i , IiIi11iI in I1iiIiiii1111 :
    if OO0oOOo in IiIi11iI . lower ( ) :
     oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOOii1i1iiI + ii1ii + IIIIIIi1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 29 - 29: o0ii1I - oOo0O0Ooo / oOo0O0Ooo * o0ii1I * III1iiIii . oooOo0oo0oo
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: iI11I1II1I1I
def o0O0Oo00 ( ) :
 IIi1i1IiIIi1i ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 IIi1i1IiIIi1i ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 IIi1i1IiIIi1i ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 IIi1i1IiIIi1i ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 23 - 23: IIiIiII11i
def o0oO0OO00oo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , o0oOOoOOO , I1II1 , oOOOOOoOO , Oo000o in IIi :
  IIi1i1IiIIi1i ( ( '[COLORblue]' + IiIi11iI + '[/COLOR] [COLORred]Season[/COLOR]-' + o0oOOoOOO + ' [COLORred]Returns [/COLOR]- ' + Oo000o + ' ' + oOOOOOoOO ) , IiIi11iI , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 69 - 69: Ii1I + IiI1i11I * o0o00Oo0O . oooOo0oo0oo % OOooOOo
def O0O000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , o0oOOoOOO , I1II1 in IIi :
  IIi1i1IiIIi1i ( ( '[COLORblue]' + IiIi11iI + '[/COLOR] [COLORred]Season[/COLOR]-' + o0oOOoOOO + ' [COLORred] Status Unknown[/COLOR] ' ) , IiIi11iI , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 22 - 22: i1i1I1IIii1II
def i1i11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , o0oOOoOOO , I1II1 , oOOOOOoOO in IIi :
  IIi1i1IiIIi1i ( ( '[COLORblue]' + IiIi11iI + ' [COLORred] Cancelled On[/COLOR] ' + oOOOOOoOO ) , IiIi11iI , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 86 - 86: o0ii1I
def IiII1i1iI ( url ) :
 OO0oOOo = ( url )
 III111i11IiI = OO0oOOo . lower ( )
 if 84 - 84: III1iiIii + Ii1I + o0ii1I + IiI1i11I
 if 62 - 62: Ii + OOooOOo + ooOoO0O00
 I1ii1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OO0oOOo ) . replace ( ' ' , '+' )
 O0000 = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 Oo0oOo0ooOOOo = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OoO0000o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 IIi1IiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 69 - 69: OOooOOo
 iiiI11iIIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 o00OoooooooOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OO0Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 13 - 13: I11i * Ii / Ii . oO0o . oooOo0oo0oo . Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 26 - 26: I11i . iI11I1II1I1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 67 - 67: I1ii11iIi11i / o0o00Oo0O
 if 88 - 88: OOooOOo - oooOo0oo0oo
 OOOiII1 = O00O0oOO00O00 ( I1ii1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( O0000 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0oOo0ooOOOo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO0000o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 O0O0ooOoOO0OO = O00O0oOO00O00 ( IIi1IiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 63 - 63: III1iiIii * ii
 if 19 - 19: III1iiIii - I11i . iI11I1II1I1I . OOooOOo / oooOo0oo0oo
 Ii11I1iIiiI = O00O0oOO00O00 ( iiiI11iIIi1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0o0OO00 = O00O0oOO00O00 ( o00OoooooooOo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 OOO0O00Oo = O00O0oOO00O00 ( OO0Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 13 - 13: iI11I1II1I1I
 if O0o0OO00 != 'Failed' :
  i1I1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0o0OO00 )
  for url , IiIi11iI in i1I1i :
   IIII1iIIii = O00O0oOO00O00 ( url )
   IiiOooooOo0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIII1iIIii )
   for I1ii1 , I1IiIiI in IiiOooooOo0 :
    if III111i11IiI in I1IiIiI . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , url + I1ii1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 2 - 2: ooOoO0O00 * i1i1I1IIii1II - i1i1I1IIii1II + ii % OOooOOo / OOooOOo
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if Ii11I1iIiiI != 'Failed' :
  i11IiI1iiI11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii11I1iIiiI )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i11IiI1iiI11 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 85 - 85: Ii1I - OOooOOo / Ii1I + oooOo0oo0oo - IiI1i11I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + i1IiiiI1iI
    if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * i1i1I1IIii1II
    if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
    if 80 - 80: i1i1I1IIii1II * Iii / iI11I1II1I1I % i1i1I1IIii1II / iI11I1II1I1I
    if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * IiI1i11I . Ii * o0o00Oo0O
    if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
    if 27 - 27: oooOo0oo0oo
    if 52 - 52: i1IiiiI1iI % OOooOOo + iI11I1II1I1I * i1i1I1IIii1II . o0ii1I
    if 95 - 95: iI11I1II1I1I . III1iiIii - ii * oO0o / I11i
    if 74 - 74: i1i1I1IIii1II
    if 34 - 34: IiI1i11I
 if OOO0O00Oo != 'Failed' :
  ii1IIiI1IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO0O00Oo )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in ii1IIiI1IIi :
   if III111i11IiI in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , i1oOOoo0o0OOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 76 - 76: IiI1i11I / oO0o + OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  Oooo00 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , oO0O00oOOoooO , IiIi11iI , iii1II1iI1IIi in i1Iii1i1I :
   if III111i11IiI in IiIi11iI . lower ( ) :
    if 'season' in iii1II1iI1IIi :
     IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
    if 'episodes' in iii1II1iI1IIi :
     IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
  for url in Oooo00 :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 41 - 41: oOo0O0Ooo - i1IiiiI1iI % IIiIiII11i . i1IiiiI1iI - Iii
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOOiII1 != 'Failed' :
  I1III1II1I11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOOiII1 )
  for url , IiIi11iI , oO0O00oOOoooO in I1III1II1I11 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( IiIi11iI ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , oO0O00oOOoooO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 45 - 45: o0ii1I - oooOo0oo0oo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . Iii % i1iIi . IIiIiII11i
    if 10 - 10: o0ii1I - Ii . Ii1I % ooOoO0O00
    if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - oooOo0oo0oo . iI11I1II1I1I
    if 30 - 30: i1iIi + i1iIi % III1iiIii - I11i - Ii1I
    if 36 - 36: Iii % oooOo0oo0oo
    if 72 - 72: oOo0O0Ooo / IiI1i11I - o0o00Oo0O + Iii
    if 83 - 83: o0o00Oo0O
    if 89 - 89: I1ii11iIi11i + Ii1I - I11i
    if 40 - 40: oO0o + oO0o
 if o00OooOO000 != 'Failed' :
  Iiii1iI1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for IiIi11iI in Iiii1iI1i :
   if III111i11IiI in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Oo0oOo0ooOOOo + IiIi11iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 94 - 94: IiI1i11I * iI11I1II1I1I . Iii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for IiIi11iI in OOoOooOoOOOoo :
   if III111i11IiI in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OoO0000o + IiIi11iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 13 - 13: iI11I1II1I1I * OOooOOo / i1IiiiI1iI % i1iIi + i1i1I1IIii1II
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if O0O0ooOoOO0OO != 'Failed' :
  I1iiIiiii1111 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0O0ooOoOO0OO )
  for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in I1iiIiiii1111 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 41 - 41: Ii1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: I1ii11iIi11i
 o0oOo00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii1ii in o0oOo00 :
  IIiI1i = oO0 + ii1ii + oOoOooOo0o0
  iiii1i1II1 = O00O0oOO00O00 ( IIiI1i )
  if iiii1i1II1 != 'Failed' :
   O0o0oo0oOO0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiii1i1II1 )
   for IiIi11iI , o00O0O , url , oO0O00oOOoooO , i11I , oo0oOO00oO in O0o0oo0oOO0oO :
    if III111i11IiI in IiIi11iI . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] - Source Pandoras[/COLOR]' , url , oo0oOO00oO , oO0O00oOOoooO , i11I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 22 - 22: iI11I1II1I1I + III1iiIii + Ii1I + i1IiiiI1iI - o0ii1I
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 48 - 48: o0ii1I - OOooOOo - oO0o + oOo0O0Ooo * o0ii1I
     if 67 - 67: I1ii11iIi11i / i1iIi - III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: Iii * o0ii1I - Ii1I % iI11I1II1I1I
def oOoOoO0o0 ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']Adult Gallery[/COLOR]' , '[COLOR' + ooOoOoo0O + ']JizBox[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Adult Channels[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  ii11I1IIi1i ( )
 if O0oO == 1 :
  iiiiiiiiiiIi ( )
 if O0oO == 2 :
  ooiiI1ii ( )
  if 76 - 76: o0ii1I + iI11I1II1I1I + OOooOOo . oO0o
  if 49 - 49: III1iiIii / i1iIi / oooOo0oo0oo
  if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - i1iIi
def ii11I1IIi1i ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']YOLOselfies[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HotNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MyNudeBabes[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TeenNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADULTmeme[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GIRLSmeme[/COLOR]' , ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  III1IiI1i1i ( 'http://www.yoloselfie.com/' )
 if O0oO == 1 :
  o0OOOOOo0 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if O0oO == 2 :
  oooOoO ( 'http://www.teennudegirls.com/' )
 if O0oO == 3 :
  oooOoO ( 'http://www.teennudegirls.com/' )
 if O0oO == 4 :
  O0Oo0 ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if O0oO == 5 :
  O0Oo0 ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 46 - 46: oOo0O0Ooo * OOooOOo
def III1IiI1i1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 100111 , oO0O00oOOoooO )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 100110 , oO0O00oOOoooO )
def oOoO00O000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  Ooo000O00 = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( Ooo000O00 )
  sys . exit ( 1 )
def O0Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + oO0O00oOOoooO , 100113 , 'http:' + oO0O00oOOoooO )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http:' + url , 100112 , oO0O00oOOoooO )
def o0OOOOOo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , oO0O00oOOoooO )
def i1iI1Iiii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , oO0O00oOOoooO , 100113 , oO0O00oOOoooO )
def I1iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , oO0O00oOOoooO )
def Iii1I1IIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , oO0O00oOOoooO , 100113 , oO0O00oOOoooO )
def oooOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , oO0O00oOOoooO )
def OooooOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , oO0O00oOOoooO , 100113 , oO0O00oOOoooO )
def o00OoOO0O0 ( url ) :
 Ooo000O00 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( Ooo000O00 )
 sys . exit ( 1 )
 if 6 - 6: i1iIi + oooOo0oo0oo / I1ii11iIi11i + III1iiIii % IIiIiII11i / oO0o
def iiIi ( ) :
 if 74 - 74: o0o00Oo0O + ii / i1i1I1IIii1II / OOooOOo . Ii1I % i1i1I1IIii1II
 if 34 - 34: ooOoO0O00 . oOo0O0Ooo
 if 6 - 6: i1IiiiI1iI % i1i1I1IIii1II % o0ii1I
 if 63 - 63: o0o00Oo0O . oOo0O0Ooo . o0o00Oo0O * iI11I1II1I1I
 if 92 - 92: i1i1I1IIii1II / oooOo0oo0oo . Ii1I
 if 30 - 30: o0ii1I . Ii1I / oooOo0oo0oo
 if 2 - 2: III1iiIii % oOo0O0Ooo - i1IiiiI1iI
 if 79 - 79: ii / Ii1I . o0o00Oo0O
 if 79 - 79: i1i1I1IIii1II - IIiIiII11i
 if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / o0ii1I * oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
 IIi1i1IiIIi1i ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 IIi1i1IiIIi1i ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 IIi1i1IiIIi1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 84 - 84: ii + i1IiiiI1iI / oOo0O0Ooo % oooOo0oo0oo % Ii1I * oOo0O0Ooo
def OOoO0oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , I11io0Oo in IIi :
  IIi1i1IiIIi1i ( ( IiIi11iI + ' - ' + I11io0Oo ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 4 - 4: IIiIiII11i
def Iiiii11IIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 85 - 85: oooOo0oo0oo . o0ii1I + i1IiiiI1iI . ooOoO0O00 / oooOo0oo0oo % i1IiiiI1iI
def O0oo00oOOO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , url in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , url , 90054 , oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: I11i / oOo0O0Ooo % o0ii1I . III1iiIii
def OooOOoO0OOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , I11io0Oo , url , IiIi11iI , i1IiI1Iiii in IIi :
  I1I1II1I11 ( I11io0Oo + ' - ' + IiIi11iI + ' - ' + i1IiI1Iiii , url , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 for oO0O00oOOoooO , IiIi11iI , url in i1Iii1i1I :
  IIi1i1IiIIi1i ( IiIi11iI , url , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 87 - 87: III1iiIii / i1IiiiI1iI - I1ii11iIi11i
def oOO ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 II11iIiIIIiI = OooOoooOo ( III111i11IiI )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , iii1II1iI1IIi in IIi :
  if 'season' in iii1II1iI1IIi :
   IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 90054 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
  if 'episodes' in iii1II1iI1IIi :
   IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 for OoOOoOooooOOo in next :
  IIi1i1IiIIi1i ( 'NEXT' , OoOOoOooooOOo , 90053 , iiIi1IIiIi + 'Next.png' )
  if 59 - 59: oO0o - oO0o + IiI1i11I
def iiIIII11iiii ( ) :
 if 20 - 20: IiI1i11I / oooOo0oo0oo
 if 28 - 28: i1iIi * Iii % Ii * IiI1i11I / o0ii1I
 if 41 - 41: oooOo0oo0oo - I11i + o0ii1I
 if 15 - 15: Iii / I11i + o0ii1I
 if 76 - 76: o0ii1I + ii / oooOo0oo0oo % oO0o / Ii1I
 if 38 - 38: i1IiiiI1iI . IiI1i11I . oOo0O0Ooo * oO0o
 if 69 - 69: I11i % Ii / o0ii1I
 if 93 - 93: i1iIi
 if 34 - 34: i1i1I1IIii1II - i1iIi * I1ii11iIi11i / I11i
 if 19 - 19: Ii1I
 IIi1i1IiIIi1i ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 IIi1i1IiIIi1i ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 IIi1i1IiIIi1i ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 IIi1i1IiIIi1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
def oOIiiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , I11io0Oo in IIi :
  if 'genre' in url :
   IIi1i1IiIIi1i ( ( IiIi11iI + ' - ' + I11io0Oo ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 96 - 96: ooOoO0O00 . Iii + i1i1I1IIii1II + Ii1I * oooOo0oo0oo - IIiIiII11i
def iIO0OO0o0O00oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  if 'release' in url :
   IIi1i1IiIIi1i ( IiIi11iI , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 81 - 81: III1iiIii / Iii
def III1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , IIi11o0O0oo0 , url , o00O0O in IIi :
  I1I1II1I11 ( IiIi11iI + ' ' + IIi11o0O0oo0 , url , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , o00O0O )
 for oO0O00oOOoooO , IiIi11iI , iii1II1iI1IIi , url , iIIi1 , o00O0O in i1Iii1i1I :
  if 'movies' in iii1II1iI1IIi :
   I1I1II1I11 ( IiIi11iI + ' - ' + iIIi1 , url , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , o00O0O )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 75 - 75: III1iiIii % Ii + iI11I1II1I1I
def oOoOo0o00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIIi1ooo0o0 ( 'http:' + url )
  if 84 - 84: Iii - I1ii11iIi11i * o0o00Oo0O / o0ii1I . o0ii1I
def iIIi1ooo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( IiIi11iI ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def ooO0 ( ) :
 if 34 - 34: ooOoO0O00 % III1iiIii
 if 80 - 80: ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
 if 94 - 94: ooOoO0O00
 if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
 if 46 - 46: IiI1i11I
 if 65 - 65: ooOoO0O00 . Ii1I / i1iIi
 if 11 - 11: III1iiIii * i1iIi / i1iIi - oooOo0oo0oo
 if 68 - 68: oOo0O0Ooo % III1iiIii - III1iiIii / oOo0O0Ooo + Ii1I - I1ii11iIi11i
 if 65 - 65: i1iIi - ooOoO0O00
 if 62 - 62: Iii / i1i1I1IIii1II % I1ii11iIi11i . ii / Ii / i1IiiiI1iI
 if 60 - 60: oOo0O0Ooo % i1i1I1IIii1II / I11i % i1i1I1IIii1II * Ii / IiI1i11I
 if 34 - 34: i1IiiiI1iI - oooOo0oo0oo
 if 25 - 25: i1i1I1IIii1II % oOo0O0Ooo + Ii + o0o00Oo0O * ii
 if 64 - 64: ooOoO0O00
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 II11iIiIIIiI = OooOoooOo ( III111i11IiI )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , I1ii1i1iiii in IIi :
  if 'movies' in I1ii1i1iiii :
   IIi1i1IiIIi1i ( I1ii1i1iiii + '-' + IiIi11iI , OoOOoOooooOOo , 90044 , oO0O00oOOoooO )
 for OoOOoOooooOOo in next :
  III1 ( OoOOoOooooOOo )
  if 45 - 45: o0ii1I / i1iIi . ii + oO0o
def i11iiI1111 ( ) :
 IIi1i1IiIIi1i ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 80006 , iiIi1IIiIi + 'Desi.png' )
def O00oO000Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , url , 80007 , oO0O00oOOoooO )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def iIIiiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  ooOoO00 ( url )
def i1I111II ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://www.join4films.com/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' ) + '&search_type=1'
 III111i11IiI = OO0oO0o . lower ( )
 O00oO000Oo0 ( III111i11IiI )
 if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
 if 26 - 26: I11i % oooOo0oo0oo + oooOo0oo0oo % Iii * Ii / IiI1i11I
 if 64 - 64: i1i1I1IIii1II % OOooOOo / IIiIiII11i % i1iIi - IiI1i11I
 if 2 - 2: i1IiiiI1iI - Ii1I + I11i * oO0o / IiI1i11I
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
 if 89 - 89: i1i1I1IIii1II
def o0OOOOOo00 ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 82 - 82: I1ii11iIi11i
def IIIIIi11111iiiII1I ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://imoviemax.se/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 I1I1i ( III111i11IiI )
def iii1IiI1i ( url ) :
 OooO0ooO0o0 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , OOOO00OOO00 in IIi :
  if IiIi11iI in OooO0ooO0o0 :
   pass
  else :
   I1I1II1I11 ( IiIi11iI + ' - ' + OOOO00OOO00 + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   OooO0ooO0o0 . append ( IiIi11iI )
   if 23 - 23: o0o00Oo0O
def I1iI11IiiI11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , IIIiIIIi11I in IIi :
  I1I1II1I11 ( IiIi11iI + ' - Views:' + IIIiIIIi11I , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 46 - 46: oooOo0oo0oo . Iii % oOo0O0Ooo - i1iIi
  if 13 - 13: OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * ooOoO0O00 % Iii
def I1I1i ( url ) :
 O0i1I11I = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , url in IIi :
  I1I1II1I11 ( IiIi11iI , url , 10075 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
  O0i1I11I . append ( IiIi11iI )
  if 34 - 34: o0ii1I * I11i + oooOo0oo0oo / III1iiIii / I1ii11iIi11i
def I111Iii1 ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for i11i , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  O0o0O00o0o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + O0o0O00o0o
  II1IIiiI1 = ( i11i ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( II1IIiiI1 , O0o0O00o0o , 10076 , img , img , '' )
  if 96 - 96: oooOo0oo0oo + oooOo0oo0oo % III1iiIii % oooOo0oo0oo
def IiiI1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for O0000 in IIi :
  if '=m' in O0000 :
   Ii11iIII ( O0000 )
  elif 'php' in O0000 :
   IiiI1I ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( O0000 )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for Oo0oOo0ooOOOo in IIi :
    Ii11iIII ( O0000 )
    if 58 - 58: o0o00Oo0O
    if 91 - 91: IiI1i11I / Ii1I . IiI1i11I - I11i + Ii1I
    if 72 - 72: o0ii1I . III1iiIii * Ii1I / Ii1I / IiI1i11I
def iiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIII1ii1 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOOOOoOO , OOO0O0OOo in IIII1ii1 :
  print 'there ><><><><><><><><><><><><'
  oOOOOOoOO = oOOOOOoOO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOO0O0OOo ) )
  for IiIi11iI , iiI1i11II in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + oOOOOOoOO + '[/COLOR] - ' + IiIi11iI + ' - [COLOR' + ooOoOoo0O + ']' + iiI1i11II + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 O00O0O = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOOOOoOO , Iii1 in O00O0O :
  print 'there ><><><><><><><><><><><><'
  oOOOOOoOO = oOOOOOoOO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Iii1 ) )
  for IiIi11iI , iiI1i11II in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + oOOOOOoOO + '[/COLOR] - ' + IiIi11iI + ' - [COLOR' + ooOoOoo0O + ']' + iiI1i11II + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 96 - 96: I1ii11iIi11i / i1i1I1IIii1II . IIiIiII11i . I1ii11iIi11i
   if 91 - 91: IIiIiII11i . oooOo0oo0oo + I11i
   if 8 - 8: oooOo0oo0oo * I1ii11iIi11i / IiI1i11I - oO0o - ii
def oO0o00oOOooO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00O0O = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00O0O in O00O0O :
  IiIi11iI = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00O0O ) )
  for IiIi11iI in IiIi11iI :
   IiIi11iI = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00O0O ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i11i1iIiii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00O0O ) )
  for i11i1iIiii in i11i1iIiii :
   i11i1iIiii = 'http:' + i11i1iIiii
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , '' , '' )
  if 100 - 100: i1i1I1IIii1II . iI11I1II1I1I . iI11I1II1I1I
  if 55 - 55: i1i1I1IIii1II
  if 37 - 37: III1iiIii / Ii / I1ii11iIi11i
  if 97 - 97: i1IiiiI1iI . Iii / oOo0O0Ooo
def oOoooo000Oo00 ( url ) :
 if 83 - 83: Iii - Ii1I * i1i1I1IIii1II
 oOO00OO0OooOo = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0000 , oO0O00oOOoooO , IiIi11iI , ii111iI1i1 in IIi :
  IiIi11iI = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( O0000 )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for O00O , I1iiiiii in i1Iii1i1I :
   OO000 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1iiiiii ) )
   for o00O0O in OO000 :
    if IiIi11iI in oOO00OO0OooOo :
     pass
    else :
     Ii1I1i ( IiIi11iI , O00O , 8043 , oO0O00oOOoooO , oO0O00oOOoooO , o00O0O )
     Ii1IIiI1i ( 'movies' , 'INFO' )
     oOO00OO0OooOo . append ( IiIi11iI )
     if 31 - 31: oO0o * o0o00Oo0O / Iii . ii * Iii . Ii1I
     if 50 - 50: oO0o * Iii - I11i + III1iiIii * oO0o % i1i1I1IIii1II
def O00o0000OO ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , i1oOOoo0o0OOOO , o00O0O , i11I , IiIi11iI in IIi :
  I1I1II1I11 ( IiIi11iI , url , 10065 , i1oOOoo0o0OOOO , i11I , o00O0O )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 61 - 61: III1iiIii % ooOoO0O00 - IiI1i11I . i1iIi - I1ii11iIi11i + I1ii11iIi11i
def II1ii1Ii ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'https://www.youtube.com/results?search_query=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 II11iIiIIIiI = OooOoooOo ( III111i11IiI )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo in next :
  OoOOoOooooOOo = 'https://www.youtube.com' + OoOOoOooooOOo
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , OoOOoOooooOOo , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oO0O00oOOoooO , OoOOoOooooOOo , IiIi11iI , I1iIIIIIi , I1iiiiii in IIi :
  OOO00 . append ( IiIi11iI )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  i11i1iIiii = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11i1iIiii
  OoOOoOooooOOo = 'http://www.youtube.com' + OoOOoOooooOOo
  Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , i11i1iIiii , I1iiiiii )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oO0O00oOOoooO , OoOOoOooooOOo , IiIi11iI , I1iIIIIIi in IIi :
   print 'im doing it'
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   i11i1iIiii = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
   OoOOoOooooOOo = 'http://www.youtube.com' + OoOOoOooooOOo
   if '&' in OoOOoOooooOOo :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( OoOOoOooooOOo )
    O00O0O = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00O0O in O00O0O :
     IiIi11iI = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00O0O ) )
     for IiIi11iI in IiIi11iI :
      IiIi11iI = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OoOOoOooooOOo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00O0O ) )
     for OoOOoOooooOOo in OoOOoOooooOOo :
      OoOOoOooooOOo = 'https://www.youtube.com/w' + OoOOoOooooOOo
     i11i1iIiii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00O0O ) )
     for i11i1iIiii in i11i1iIiii :
      i11i1iIiii = 'http:' + i11i1iIiii
     Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , Oo00OOOOO , '' )
   elif IiIi11iI in OOO00 :
    pass
   elif 'user' in OoOOoOooooOOo or 'elete' in IiIi11iI :
    pass
   elif 'hannel' in OoOOoOooooOOo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OoOOoOooooOOo
    II11iIiIIIiI = OooOoooOo ( OoOOoOooooOOo )
    iiIiIiIiiIiI = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oO0O00oOOoooO , OoOOoOooooOOo , IiIi11iI in iiIiIiIiiIiI :
     if 'outube' in OoOOoOooooOOo or 'list' in OoOOoOooooOOo :
      pass
     elif 'atch' in OoOOoOooooOOo :
      OoOOoOooooOOo = ( OoOOoOooooOOo ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oO0O00oOOoooO , 'http:' + oO0O00oOOoooO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , i11i1iIiii , '' )
    if 23 - 23: oO0o / IiI1i11I / iI11I1II1I1I
def IIIIiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oO0O00oOOoooO , url , IiIi11iI , I1iIIIIIi , I1iiiiii in IIi :
  OOO00 . append ( IiIi11iI )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  i11i1iIiii = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11i1iIiii
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , i11i1iIiii , I1iiiiii )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oO0O00oOOoooO , url , IiIi11iI , I1iIIIIIi in IIi :
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   i11i1iIiii = 'http:' + ( oO0O00oOOoooO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    O00O0O = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00O0O in O00O0O :
     IiIi11iI = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00O0O ) )
     for IiIi11iI in IiIi11iI :
      IiIi11iI = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00O0O ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i11i1iIiii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00O0O ) )
     for i11i1iIiii in i11i1iIiii :
      i11i1iIiii = 'http:' + i11i1iIiii
     Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , Oo00OOOOO , '' )
   elif IiIi11iI in OOO00 :
    pass
   elif 'user' in url or 'elete' in IiIi11iI :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    iiIiIiIiiIiI = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oO0O00oOOoooO , url , IiIi11iI in iiIiIiIiiIiI :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oO0O00oOOoooO , 'http:' + oO0O00oOOoooO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + I1iIIIIIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii , i11i1iIiii , '' )
    if 75 - 75: ii . oooOo0oo0oo + oO0o / o0ii1I - oOo0O0Ooo % o0ii1I
    if 89 - 89: IiI1i11I * iI11I1II1I1I + Ii . ii
    if 51 - 51: oooOo0oo0oo / i1iIi + oO0o % OOooOOo / o0ii1I
def ii111i1i ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 71 - 71: I11i % i1iIi / i1i1I1IIii1II - iI11I1II1I1I / Ii
def OOooOoO ( ) :
 ivuesetup . iVueInt ( )
 if 24 - 24: I11i + oOo0O0Ooo - IIiIiII11i
def iiiii1i ( ) :
 Ii1iiI ( )
 return
 if 87 - 87: I1ii11iIi11i % o0ii1I
def Ii1iiI ( ) :
 if 53 - 53: ooOoO0O00 - III1iiIii + iI11I1II1I1I
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 o0Oo00oOO = II1I . getSetting ( id = 'User' )
 O0oo = II1I . getSetting ( id = 'Pass' )
 o0000O00oO0O = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 IiiI111I11 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 oO0Ooooo000 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 Iii1Iiii = "http://piesustv.net:8000/get.php?username=" + o0Oo00oOO + "&password=" + O0oo + "&type=m3u_plus&output=ts"
 i1i1Ii1IiIII = "http://piesustv.net:8000/xmltv.php?username=" + o0Oo00oOO + "&password=" + O0oo + "&type=m3u_plus&output=ts"
 if 9 - 9: Iii - i1i1I1IIii1II + o0o00Oo0O / IiI1i11I % ooOoO0O00
 xbmc . executeJSONRPC ( o0000O00oO0O )
 xbmc . executeJSONRPC ( IiiI111I11 )
 xbmc . executeJSONRPC ( oO0Ooooo000 )
 if 97 - 97: I11i * i1iIi
 O0OOO0ooO00o = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 O0OOO0ooO00o . setSetting ( id = 'm3uUrl' , value = Iii1Iiii )
 O0OOO0ooO00o . setSetting ( id = 'epgUrl' , value = i1i1Ii1IiIII )
 O0OOO0ooO00o . setSetting ( id = 'm3uCache' , value = "false" )
 O0OOO0ooO00o . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def I1iii1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 19 - 19: i1i1I1IIii1II % ii . ii
if 40 - 40: o0o00Oo0O . i1IiiiI1iI / iI11I1II1I1I * I11i
if 73 - 73: I1ii11iIi11i - IiI1i11I . i1i1I1IIii1II % ooOoO0O00 . o0o00Oo0O
def I1 ( ) :
 if 96 - 96: Iii
 if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . oooOo0oo0oo
 if 63 - 63: IiI1i11I
 if 11 - 11: IiI1i11I - iI11I1II1I1I
 if 92 - 92: oO0o
 if 15 - 15: III1iiIii / III1iiIii + iI11I1II1I1I % ii
 if 12 - 12: i1iIi
 if 36 - 36: i1IiiiI1iI . III1iiIii * ii - I11i
 if 60 - 60: oooOo0oo0oo . IiI1i11I / iI11I1II1I1I + oooOo0oo0oo * i1IiiiI1iI
 if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - Iii + o0ii1I
 if 48 - 48: Ii1I
 if 96 - 96: i1iIi . ii
 if OO0o == "insert_username" :
  i1I1I1I = iII1III ( )
  O0oo0oO00o = I1ii111i1ii1 ( )
  I11 ( 'User' , i1I1I1I )
  I11 ( 'Pass' , O0oo0oO00o )
  xbmc . executebuiltin ( 'Container.Refresh' )
  o0Ii11iIiiI = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( i1I1I1I , O0oo0oO00o )
  o0Ii11iIiiI = OooOoooOo ( o0Ii11iIiiI )
  if o0Ii11iIiiI == "" :
   o000 = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   i11ii1 = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   Ii111I11 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , o000 , i11ii1 , Ii111I11 )
   I1 ( )
  else :
   o000 = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   i11ii1 = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   Ii111I11 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % i1I1I1I )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , o000 , i11ii1 , Ii111I11 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   Oo0O0oo ( )
 else :
  Oo0O0oo ( )
def iII1III ( ) :
 o0O0 = xbmc . Keyboard ( '' , 'heading' , True )
 o0O0 . setHeading ( 'Enter Username' )
 o0O0 . setHiddenInput ( False )
 o0O0 . doModal ( )
 if ( o0O0 . isConfirmed ( ) ) :
  oO0o0 = o0O0 . getText ( )
  return oO0o0
 else :
  return False
  if 65 - 65: o0o00Oo0O . i1i1I1IIii1II
  if 85 - 85: IIiIiII11i
def I1ii111i1ii1 ( ) :
 o0O0 = xbmc . Keyboard ( '' , 'heading' , True )
 o0O0 . setHeading ( 'Enter Password' )
 o0O0 . setHiddenInput ( False )
 o0O0 . doModal ( )
 if ( o0O0 . isConfirmed ( ) ) :
  oO0o0 = o0O0 . getText ( )
  return oO0o0
 else :
  return False
def o0oOOoo0O ( ) :
 Iii1Iiii = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  OoooOo00 = urllib2 . urlopen ( Iii1Iiii )
  print OoooOo00 . getcode ( )
  OoooOo00 . close ( )
  if 98 - 98: oO0o . iI11I1II1I1I % ii % I1ii11iIi11i - Ii1I
  pass
  if 86 - 86: OOooOOo . III1iiIii
 except urllib2 . HTTPError , i1iIiIIi :
  print i1iIiIIi . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def Oo0O0oo ( ) :
 iii ( )
 if 10 - 10: IiI1i11I * o0ii1I - i1iIi . Iii - oooOo0oo0oo
 if 94 - 94: oOo0O0Ooo % III1iiIii + oO0o
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 90 - 90: ooOoO0O00 + o0o00Oo0O - i1i1I1IIii1II . IiI1i11I + iI11I1II1I1I
 if 88 - 88: o0ii1I * o0o00Oo0O . i1IiiiI1iI / ii
 if 29 - 29: ii . IIiIiII11i % OOooOOo
 if 26 - 26: iI11I1II1I1I - Ii1I . III1iiIii . III1iiIii + iI11I1II1I1I * I1ii11iIi11i
def O0Oo00 ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 I1IIi = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 Oo0o0ooOoO = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 o0Ii11iIiiI = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 o0Ii11iIiiI = OooOoooOo ( o0Ii11iIiiI )
 if not o0Ii11iIiiI == "" :
  iI1Ii11 = 'https://tinyurl.com/create.php?source=indexpage&url=' + I1IIi + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( iI1Ii11 ) )
  Ooo0 = 'https://tinyurl.com/create.php?source=indexpage&url=' + Oo0o0ooOoO + '&submit=Make+TinyURL%21&alias='
  I1IIi = OooOoooOo ( iI1Ii11 )
  Oo0o0ooOoO = OooOoooOo ( Ooo0 )
  xbmc . log ( str ( Oo0o0ooOoO ) )
  IiiiIIi = I1IIIi ( I1IIi , '<div class="indent"><b>' , '</b>' )
  OoOooOo00O = I1IIIi ( Oo0o0ooOoO , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % IiiiIIi , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % OoOooOo00O )
 else :
  return
def oo0O0oOOO0o ( ) :
 o0oOOoo0O ( )
 oOo0Oo0Oo0 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , OooOo0o0OO + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( iiI1ii1IIiI )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + IiIi11iI + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , OoOOoOooooOOo , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def IIi1i1I11IIII ( url ) :
 open = OooOoooOo ( OooOoOOO00O + url )
 I111iIIII11iI = oOoOO ( open , '<channel>' , '</channel>' )
 for i11I1iIii1i11 in I111iIIII11iI :
  if '<playlist_url>' in open :
   IiIi11iI = I1IIIi ( i11I1iIii1i11 , '<title>' , '</title>' )
   I1ii1 = I1IIIi ( i11I1iIii1i11 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( IiIi11iI ) ) . replace ( '?' , '' ) , I1ii1 , 3 , icon , i11I , '' )
  else :
   IiIi11iI = I1IIIi ( i11I1iIii1i11 , '<title>' , '</title>' )
   IiIi11iI = base64 . b64decode ( IiIi11iI )
   iIiiI11II11i = I1IIIi ( i11I1iIii1i11 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = I1IIIi ( i11I1iIii1i11 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00O0O = I1IIIi ( i11I1iIii1i11 , '<description>' , '</description>' )
   o00O0O = base64 . b64decode ( o00O0O )
   o00OoO0o0 = I1IIIi ( o00O0O , 'PLOT:' , '\n' )
   o0OOOoO0ooOOOo0 = I1IIIi ( o00O0O , 'CAST:' , '\n' )
   o0oOOO = I1IIIi ( o00O0O , 'RATING:' , '\n' )
   o00iI1i1II = I1IIIi ( o00O0O , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   o00iI1i1II = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( o00iI1i1II )
   IIi11O0OOO = I1IIIi ( o00O0O , 'DURATION_SECS:' , '\n' )
   iii1iII1I = I1IIIi ( o00O0O , 'GENRE:' , '\n' )
   i1Ii11ii ( str ( IiIi11iI ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , iIiiI11II11i , i11I , o00OoO0o0 , str ( o00iI1i1II ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( o0OOOoO0ooOOOo0 ) . split ( ) , o0oOOO , IIi11O0OOO , iii1iII1I )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 18 - 18: Ii - i1iIi * i1i1I1IIii1II + I11i
IiiiIi1iiii11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
iIIi1IIIii11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 40 - 40: oOo0O0Ooo % i1iIi % III1iiIii + oO0o
def OOOOOOooo ( ) :
 Iii1Iiii = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  OoooOo00 = urllib2 . urlopen ( Iii1Iiii )
  print OoooOo00 . getcode ( )
  OoooOo00 . close ( )
  if 52 - 52: IiI1i11I / i1iIi - Ii + ii
  pass
  if 33 - 33: o0o00Oo0O + I1ii11iIi11i - iI11I1II1I1I % Ii / oOo0O0Ooo
 except urllib2 . HTTPError , i1iIiIIi :
  print i1iIiIIi . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 47 - 47: Ii1I * i1i1I1IIii1II + iI11I1II1I1I - i1i1I1IIii1II / III1iiIii
 OoOOoOooooOOo = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 oO0ooo0O0Ooo ( OoOOoOooooOOo , iIIi1IIIii11i + "uide.xml" )
 if 33 - 33: IIiIiII11i - III1iiIii - i1iIi
 iiii111II = open ( IiiiIi1iiii11 , 'r+' )
 input = open ( IiiiIi1iiii11 ) . read ( ) . decode ( 'UTF-8' )
 oO00oOoo00o0 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 iiii111II . write ( oO00oOoo00o0 )
 iiii111II . truncate ( )
 iiii111II . close ( )
 III1I ( )
 if 85 - 85: I1ii11iIi11i . Ii - Ii . oOo0O0Ooo . oO0o % ii
def III1I ( ) :
 open = OooOoooOo ( I1111i )
 all = oOoOO ( open , '{"num' , 'direct' )
 for i11I1iIii1i11 in all :
  if '"tv_archive":1' in i11I1iIii1i11 :
   IiIi11iI = I1IIIi ( i11I1iIii1i11 , '"epg_channel_id":"' , '"' )
   iIiiI11II11i = I1IIIi ( i11I1iIii1i11 , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = I1IIIi ( i11I1iIii1i11 , 'stream_id":"' , '"' )
   IiIi11iI = IiIi11iI . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( IiIi11iI , id , 90027 , iIiiI11II11i , i11I , IiIi11iI )
   if 79 - 79: i1IiiiI1iI
   if 8 - 8: IiI1i11I - IIiIiII11i
def ii1111I ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 iII1i1ii = open ( IiiiIi1iiii11 )
 i1I1ii1i = ElementTree . parse ( iII1i1ii )
 iiiiII11iIi = "apples"
 import datetime as dt
 from datetime import time
 OO00 = datetime . now ( ) - timedelta ( days = 5 )
 oOOOOOoOO = str ( OO00 )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 Oooo = i1I1ii1i . findall ( "programme" )
 for O00 in Oooo :
  if name in O00 . attrib . get ( 'channel' ) :
   IiIIIIi = O00 . attrib . get ( 'start' )
   OoIIiIIIII1I , ooiiI , o00iIiI1iI1Ii1 = IiIIIIi . partition ( ' +' )
   oOOOOOoOO = str ( oOOOOOoOO ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   o00iI1i1II , iioO , Oo000o = IiIIIIi . partition ( '2017' )
   ii11I = O00 . find ( 'title' ) . text + IiIIIIi
   Oo000o = Oo000o [ : - 6 ]
   if OoIIiIIIII1I > oOOOOOoOO :
    if OoIIiIIIII1I < I1IIIii :
     Ooo0O00 = OoIIiIIIII1I
     Ooo0O00 = Ooo0O00 [ : 4 ] + '/' + Ooo0O00 [ 4 : ]
     OoIIiIIIII1I = OoIIiIIIII1I [ : 4 ] + '-' + OoIIiIIIII1I [ 4 : ]
     Ooo0O00 = Ooo0O00 [ : 7 ] + '/' + Ooo0O00 [ 7 : ]
     OoIIiIIIII1I = OoIIiIIIII1I [ : 7 ] + '-' + OoIIiIIIII1I [ 7 : ]
     Ooo0O00 = Ooo0O00 [ : 10 ] + ' - ' + Ooo0O00 [ 10 : ]
     OoIIiIIIII1I = OoIIiIIIII1I [ : 10 ] + ':' + OoIIiIIIII1I [ 10 : ]
     Ooo0O00 = Ooo0O00 [ : 15 ] + ':' + Ooo0O00 [ 15 : ]
     OoIIiIIIII1I = OoIIiIIIII1I [ : 13 ] + '-' + OoIIiIIIII1I [ 13 : ]
     Ooo0O00 = Ooo0O00 [ : - 2 ]
     OoIIiIIIII1I = OoIIiIIIII1I [ : - 2 ]
     oooo0oOOoO000 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( OoIIiIIIII1I ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     iiiiII11iIi = oooo0oOOoO000 + str ( OoIIiIIIII1I ) + "&duration=240"
     Ooo0O00 = '[COLOR blue]%s - [/COLOR]' % Ooo0O00
     ii11I = str ( Ooo0O00 ) + O00 . find ( 'title' ) . text
     o00O0O = O00 . find ( 'desc' ) . text
     Ii1I1i ( ii11I , oooo0oOOoO000 , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , o00O0O )
def Oo00o00Oo ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 i1iiIIIi = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 i1iiIIIi . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 i1iiIIIi . setProperty ( 'IsPlayable' , 'true' )
 i1iiIIIi . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iiIIIi )
def oO0ooo0O0Ooo ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 i1I1i1I111 = time . time ( )
 urllib . urlretrieve ( url , dest , lambda oOo00OO0ooOOO , i1i1I1Ii1IIii , oooOOoo : iI1iii1iIiiI ( oOo00OO0ooOOO , i1i1I1Ii1IIii , oooOOoo , o0oOoO00o , i1I1i1I111 ) )
def iI1iii1iIiiI ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  II1iiiiI1 = min ( numblocks * blocksize * 100 / filesize , 100 )
  IiiIiiIIII = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  oOoOOOOoO0 = numblocks * blocksize / ( time . time ( ) - start_time )
  if oOoOOOOoO0 > 0 :
   IiiIiIIi1 = ( filesize - numblocks * blocksize ) / oOoOOOOoO0
  else :
   IiiIiIIi1 = 0
  oOoOOOOoO0 = oOoOOOOoO0 / 1024
  i1oo = oOoOOOOoO0 / 1024
  OooOoo = float ( filesize ) / ( 1024 * 1024 )
  Oooo0Oo00o = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( IiiIiiIIII )
  i1iIiIIi = '[COLOR white]Speed:  %.02f Mb/s ' % i1oo + '[/COLOR]'
  dp . update ( II1iiiiI1 , Oooo0Oo00o , i1iIiIIi )
 except :
  II1iiiiI1 = 100
  dp . update ( II1iiiiI1 )
 if dp . iscanceled ( ) :
  IIoO = xbmcgui . Dialog ( )
  IIoO . ok ( "GenieTv" , 'The download was cancelled.' )
  if 13 - 13: ooOoO0O00
  sys . exit ( )
  dp . close ( )
  if 48 - 48: o0o00Oo0O + oO0o . IiI1i11I * I11i * IiI1i11I
def OOOo0Oo0O ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  i1I1I1iIIi ( )
  if 46 - 46: oOo0O0Ooo . III1iiIii - Ii - i1IiiiI1iI
  if 97 - 97: IIiIiII11i % I1ii11iIi11i * III1iiIii
  if 51 - 51: I1ii11iIi11i % oooOo0oo0oo . I1ii11iIi11i
  if 72 - 72: o0ii1I % o0ii1I / oOo0O0Ooo
  if 40 - 40: I1ii11iIi11i - oooOo0oo0oo + i1IiiiI1iI - I11i % oOo0O0Ooo . i1iIi
  if 35 - 35: Ii + ii * iI11I1II1I1I . i1IiiiI1iI
  if 48 - 48: IiI1i11I * ooOoO0O00 % ii * o0ii1I * oO0o
  if 7 - 7: IiI1i11I . o0ii1I . IiI1i11I - i1IiiiI1iI
def i1I1I1iIIi ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for OoOOoOooooOOo in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def I1IiiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i11I1i11IIIi = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1III1II1I11 = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 Iiii1iI1i = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOoOooOoOOOoo = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IIi11 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1iiIiiii1111 = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 OoOOoO0O0oO = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 III1IIIIIiiI = i1iIii ( )
 O0o00 = I1IIi1iI1iiI ( )
 for url in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i11I1i11IIIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1III1II1I11 :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOoOooOoOOOoo :
  dt = datetime . fromtimestamp ( float ( OOoOooOoOOOoo [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   oOOo0OOOOo0Oo ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Iiii1iI1i :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IIi11 :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1iiIiiii1111 :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OoOOoO0O0oO :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + III1IIIIIiiI , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + O0o00 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 27 - 27: iI11I1II1I1I % Iii - i1IiiiI1iI
 oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 67 - 67: o0o00Oo0O / i1IiiiI1iI * o0ii1I % i1iIi . Ii1I * i1i1I1IIii1II
def IiiiIIIi11ii1 ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 O00Oo00OOoO0 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 99 - 99: oO0o / ooOoO0O00 . Ii1I
def I1I1i11iiiiI ( data ) :
 oOOooI1I1i11 = len ( data ) % 4
 if 79 - 79: I11i - IIiIiII11i
 if 70 - 70: i1IiiiI1iI . i1i1I1IIii1II % ooOoO0O00 / iI11I1II1I1I
 if 98 - 98: ooOoO0O00 % I1ii11iIi11i
 if 82 - 82: i1iIi
 if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / IiI1i11I
 if 9 - 9: OOooOOo - III1iiIii
 if oOOooI1I1i11 != 0 :
  data += b'=' * ( 4 - oOOooI1I1i11 )
 return base64 . decodestring ( data )
def I1IIIi ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : iiIiIiI111 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : iiIiIiI111 = ''
 else :
  try : iiIiIiI111 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : iiIiIiI111 = ''
 return iiIiIiI111
 if 82 - 82: oOo0O0Ooo % oO0o % Iii + Iii
 if 6 - 6: I1ii11iIi11i
def oOoOO ( text , start_with , end_with ) :
 iiIiIiI111 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return iiIiIiI111
def i1iIii ( ) :
 O0OOOOoO00oo = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 O0OOOOoO00oo . connect ( ( '8.8.8.8' , 0 ) )
 O0OOOOoO00oo = O0OOOOoO00oo . getsockname ( ) [ 0 ]
 return O0OOOOoO00oo
 if 80 - 80: ooOoO0O00 . oOo0O0Ooo - i1i1I1IIii1II + oooOo0oo0oo + IiI1i11I % i1i1I1IIii1II
def I1IIi1iI1iiI ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 III1IIIIIiiI = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( III1IIIIIiiI . group ( ) )
OooOo0o0OO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
I1111i = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
IiiII = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
I1ii1iI = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
i1i1 = '&action=get_live_categories'
IIii1Ii1i1ii1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
iiI1ii1IIiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 86 - 86: i1i1I1IIii1II % o0o00Oo0O + oO0o
OooOoOOO00O = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
oO0OO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
o0OOO = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
Iii11iI1I = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 79 - 79: oOo0O0Ooo - IiI1i11I / Iii . I1ii11iIi11i
def o0III11IiI ( ) :
 o0oOOoo0O ( )
 open = OooOoooOo ( o0OOO )
 I111iIIII11iI = oOoOO ( open , '<channel>' , '</channel>' )
 for i11I1iIii1i11 in I111iIIII11iI :
  IiIi11iI = I1IIIi ( i11I1iIii1i11 , '<title>' , '</title>' )
  IiIi11iI = base64 . b64decode ( IiIi11iI )
  I1ii1 = I1IIIi ( i11I1iIii1i11 , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + IiIi11iI + '[/COLOR]' , I1ii1 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 53 - 53: IiI1i11I / ooOoO0O00 / ooOoO0O00
def o0oo00O ( url ) :
 open = OooOoooOo ( Iii11iI1I + url )
 I111iIIII11iI = oOoOO ( open , '<channel>' , '</channel>' )
 for i11I1iIii1i11 in I111iIIII11iI :
  IiIi11iI = I1IIIi ( i11I1iIii1i11 , '<title>' , '</title>' )
  IiIi11iI = base64 . b64decode ( IiIi11iI )
  xbmc . log ( str ( IiIi11iI ) )
  iIiiI11II11i = I1IIIi ( i11I1iIii1i11 , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1ii1 = I1IIIi ( i11I1iIii1i11 , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00O0O = I1IIIi ( i11I1iIii1i11 , '<description>' , '</description>' )
  o00O0O = base64 . b64decode ( o00O0O )
  IIIIII1iI1II = '('
  iiiI1 = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , I1ii1 , 222 , iIiiI11II11i , i11I , ( '[COLOR' + ooOoOoo0O + ']' + o00O0O + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( iiiI1 , '[COLORsteelblue]' ) . replace ( IIIIII1iI1II , '[COLORorangered]' ) )
  if 58 - 58: III1iiIii % Ii * IIiIiII11i . Ii1I
def OoO ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( IIii1Ii1i1ii1 + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , type , O0000 , ooo0O0OOO000o in IIi :
  Oo0oOo0ooOOOo = ( I1ii1iI + O0000 + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , Oo0oOo0ooOOOo , 222 , ( ooo0O0OOO000o ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def O00oO0o00 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1IiIiI , Oo0OOOO0oOoo0 in IIi :
  if name == I1IiIiI :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + Oo0OOOO0oOoo0 , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def O0OIIII1i ( name ) :
 i1I1Iiii = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , oO0O00oOOoooO , OoOOoOooooOOo in IIi :
  OoOOoOooooOOo = ( OoOOoOooooOOo ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( OoOOoOooooOOo ) . strip ( ) , 222 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 15 - 15: i1iIi % I11i / i1i1I1IIii1II - IIiIiII11i . iI11I1II1I1I
  if 28 - 28: IIiIiII11i * i1iIi * o0ii1I
  if 93 - 93: ooOoO0O00 . o0ii1I * i1IiiiI1iI . i1iIi
  if 54 - 54: IiI1i11I . ooOoO0O00 . Ii1I * I11i % IiI1i11I
  if 30 - 30: Iii
  if 85 - 85: IIiIiII11i + i1iIi * Iii
  if 12 - 12: o0ii1I . oOo0O0Ooo % I11i
  if 28 - 28: o0ii1I - oOo0O0Ooo % oO0o * i1IiiiI1iI
  if 80 - 80: oooOo0oo0oo * III1iiIii
  if 4 - 4: iI11I1II1I1I . i1IiiiI1iI + IIiIiII11i % ii
  if 82 - 82: ii / i1iIi * Iii * o0o00Oo0O . Ii1I
  if 21 - 21: IIiIiII11i + I1ii11iIi11i
def i1II1I1Iii1 ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , OoOOoOooooOOo , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 59 - 59: oooOo0oo0oo + oOo0O0Ooo / IIiIiII11i / OOooOOo
  if 80 - 80: OOooOOo + iI11I1II1I1I . III1iiIii
  if 76 - 76: oOo0O0Ooo * oooOo0oo0oo
zip = oo00 . getSetting ( 'zip' )
ii111 = xbmc . translatePath ( os . path . join ( zip ) )
def IIiiI11 ( ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 7 - 7: oOo0O0Ooo / oO0o + i1IiiiI1iI + Iii / oOo0O0Ooo
  if 82 - 82: Ii1I + ii
  if 21 - 21: i1i1I1IIii1II * i1i1I1IIii1II / Iii . IiI1i11I
def I1IIIIiiI1i1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  IIiiI11 ( )
  o00o = open ( url ) . read ( )
  IIIi1ii = os . path . join ( ii111 , description . split ( 'Your ' ) [ 1 ] )
  iiii111II = open ( IIIi1ii , mode = 'w' )
  iiii111II . write ( o00o )
  iiii111II . close ( )
 else :
  if 'guisettings.xml' in description :
   i11I1iIii1i11 = open ( os . path . join ( ii111 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iiIiIiI111 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( iiIiIiI111 ) . findall ( i11I1iIii1i11 )
   for type , Ii1iii11I , Ii11iIiiI in IIi :
    Ii11iIiiI = Ii11iIiiI . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , Ii1iii11I , Ii11iIiiI ) )
  else :
   IIIi1ii = os . path . join ( url )
   o00o = open ( os . path . join ( ii111 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iiii111II = open ( IIIi1ii , mode = 'w' )
   iiii111II . write ( o00o )
   iiii111II . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 3 - 3: IIiIiII11i / oooOo0oo0oo
 if 48 - 48: i1iIi . Ii1I
 if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - i1iIi / I1ii11iIi11i
 if 24 - 24: i1i1I1IIii1II - IiI1i11I / i1iIi
def iIiiII1Ii1ii ( ) :
 iIIi1OoOo0O00 = 1
 IIiiI11 ( )
 iI1i1iI1iI = xbmc . translatePath ( os . path . join ( ii111 , 'Build Backup' , 'Full Backup' , '' ) )
 I1IIiIi = xbmc . translatePath ( os . path . join ( ii111 , 'Build Backup' , 'my_full_backup.zip' ) )
 OOOOoOoO = xbmc . translatePath ( os . path . join ( ii111 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iI1i1iI1iI ) :
  os . makedirs ( iI1i1iI1iI )
 OO000o0oOoo0o = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OO000o0oOoo0o ) : return False , 0
 iIIIII1iiiiII = OO000o0oOoo0o
 IiiIiIIi = xbmc . translatePath ( os . path . join ( iI1i1iI1iI , iIIIII1iiiiII + '.zip' ) )
 O00Oo = [ 'plugin.video.GenieTv' ]
 oOOoooo0O0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Ii111Ii11 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 Ii1II = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 IIiII = "Creating full backup of existing build"
 iII11 = "Creating Community Build"
 O00OO00OOOoO = "Archiving..."
 IiI11Ii1iI = ""
 ooOo0 = "Please Wait"
 oOo0o ( oOo0oooo00o , IiiIiIIi , iII11 , O00OO00OOOoO , IiI11Ii1iI , ooOo0 , Ii111Ii11 , Ii1II )
 time . sleep ( 1 )
 O000OOO000o = xbmc . translatePath ( os . path . join ( iI1i1iI1iI , iIIIII1iiiiII + '_guisettings.zip' ) )
 I11iiIiiI1iIi11 = zipfile . ZipFile ( O000OOO000o , mode = 'w' )
 try :
  I11iiIiiI1iIi11 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I11iiIiiI1iIi11 . close ( )
 if iIIi1OoOo0O00 == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1IIiIi , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IiiIiIIi + '[/COLOR]' )
  if 32 - 32: Ii1I * I11i * oO0o * oooOo0oo0oo * o0o00Oo0O
def oOo0o ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OoOooOo00o = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iI1IIi = len ( sourcefile )
 II11oo0o0O = [ ]
 ooo0ooooo0o = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for IIIIIIi1IIi1I11i , O0o0oOooOoo , oOo0O0 in os . walk ( sourcefile ) :
  for file in oOo0O0 :
   ooo0ooooo0o . append ( file )
 iIi1iI = len ( ooo0ooooo0o )
 for IIIIIIi1IIi1I11i , O0o0oOooOoo , oOo0O0 in os . walk ( sourcefile ) :
  O0o0oOooOoo [ : ] = [ iIIII1iII1i for iIIII1iII1i in O0o0oOooOoo if iIIII1iII1i not in exclude_dirs ]
  oOo0O0 [ : ] = [ iiii111II for iiii111II in oOo0O0 if iiii111II not in exclude_files ]
  for file in oOo0O0 :
   II11oo0o0O . append ( file )
   O0OO00OoO00 = len ( II11oo0o0O ) / float ( iIi1iI ) * 100
   o0oOoO00o . update ( int ( O0OO00OoO00 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O00o = os . path . join ( IIIIIIi1IIi1I11i , file )
   if not 'temp' in O0o0oOooOoo :
    if not 'plugin.program.originwizard' in O0o0oOooOoo :
     import time
     Ii11Iiii1iiii = '01/01/1980'
     i1IIII1111 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O00o ) ) )
     if i1IIII1111 > Ii11Iiii1iiii :
      OoOooOo00o . write ( O00o , O00o [ iI1IIi : ] )
 OoOooOo00o . close ( )
 o0oOoO00o . close ( )
 if 84 - 84: o0o00Oo0O % o0ii1I . o0ii1I . IiI1i11I * Iii
 if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
def OO0O00 ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 65 - 65: ii
 if 22 - 22: oooOo0oo0oo + IIiIiII11i + I1ii11iIi11i
def oOo00Oo0o00oo ( ) :
 iii ( )
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  oo00O00oO000o ( )
 if O0oO == 1 :
  OoOOOo0o0ooo ( )
 if O0oO == 2 :
  oOOO0O0Ooo ( )
 if O0oO == 3 :
  II1ii1Ii ( )
  if 58 - 58: OOooOOo + oO0o * o0ii1I
  if 31 - 31: i1i1I1IIii1II - IiI1i11I
  if 46 - 46: oOo0O0Ooo + I1ii11iIi11i - o0ii1I
  if 99 - 99: oooOo0oo0oo + oOo0O0Ooo . Ii1I * ii
  if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + oooOo0oo0oo * IIiIiII11i
  if 34 - 34: I11i % ii
  if 36 - 36: oOo0O0Ooo
  if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Iii
  if 64 - 64: i1iIi / ooOoO0O00 % IiI1i11I
def OOoOo0O0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0oO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0oO == 2 :
   I1o0 ( )
  if O0oO == 3 :
   I1IiiiiI1i1I ( )
  if O0oO == 4 :
   I11i1I1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO == 5 :
   ooOooO ( )
  if O0oO == 6 :
   oooo ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO == 7 :
   IIIiI1iIIII ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO == 8 :
   o0oo00OOOo ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO == 9 :
   oo0oO ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , iiIi1IIiIi + 'Thunder.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
   if 17 - 17: i1iIi + i1iIi . Ii1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 50 - 50: iI11I1II1I1I * i1i1I1IIii1II
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 85 - 85: ooOoO0O00
  if 100 - 100: ii / Iii % oO0o + o0ii1I
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 42 - 42: I1ii11iIi11i / III1iiIii . o0ii1I * oOo0O0Ooo
def oOO0O0ooOOOo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   o0OOOoO0O ( )
  if O0oO == 1 :
   oO0o00oo0 ( )
  if O0oO == 2 :
   i1II1 ( )
  if O0oO == 3 :
   OoOOo ( OoOOoOooooOOo )
  if O0oO == 4 :
   III11iI1i11i ( OoOOoOooooOOo )
  if O0oO == 5 :
   OoOO0o ( )
  if O0oO == 6 :
   IIiI ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO == 7 :
   OOoOo0oO0oo00 ( )
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
  if 100 - 100: oO0o . Iii / o0ii1I . I11i - OOooOOo . Iii
  if 30 - 30: o0ii1I % Iii + I11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 65 - 65: iI11I1II1I1I . IiI1i11I / o0ii1I
 if 12 - 12: oOo0O0Ooo + i1IiiiI1iI
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
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 80 - 80: i1i1I1IIii1II . o0o00Oo0O
 if 90 - 90: IIiIiII11i / oO0o / o0ii1I
def O0oooOOo0 ( ) :
 iii ( )
 Ii1I1i ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 16 - 16: oO0o + Iii / iI11I1II1I1I % IIiIiII11i
def iiI11Iii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 39 - 39: ooOoO0O00 . Ii1I / Iii / Iii
def ooOo0oO0O ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 17 - 17: III1iiIii / i1IiiiI1iI . oOo0O0Ooo + ooOoO0O00
 if 28 - 28: i1i1I1IIii1II % OOooOOo + i1IiiiI1iI * IiI1i11I * o0ii1I
 if 53 - 53: oooOo0oo0oo / I1ii11iIi11i
def iIO0oOoo00Oo0O ( ) :
 iii ( )
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  Iii1i1Ii ( )
 if O0oO == 0 :
  III1iIii ( OoOOoOooooOOo )
 if O0oO == 0 :
  iiIII1i1 ( OoOOoOooooOOo )
  if 78 - 78: i1i1I1IIii1II % OOooOOo
  if 1 - 1: OOooOOo - I11i / i1iIi - III1iiIii / ooOoO0O00
  if 28 - 28: oO0o / i1IiiiI1iI * oOo0O0Ooo + i1iIi
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 48 - 48: o0o00Oo0O
def iIIIi11iIiIii ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for oO0O00oOOoooO , IiIi11iI in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 61 - 61: ii . o0ii1I % i1i1I1IIii1II * ii
def O00o0O0oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( iIIII1I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 5 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 98 - 98: Iii . Iii / I1ii11iIi11i / o0ii1I / oOo0O0Ooo
def Iii1i1Ii ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 56 - 56: I11i / III1iiIii
def iI1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiI1iI1IiiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 5 - 5: i1IiiiI1iI % IIiIiII11i + I1ii11iIi11i - iI11I1II1I1I
def o0oo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oooiI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 54 - 54: o0ii1I . o0o00Oo0O
def O00O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ii11i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 12 - 12: OOooOOo + I11i . i1IiiiI1iI
def ooO00OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 64 - 64: i1iIi - I11i % IiI1i11I % i1IiiiI1iI . i1i1I1IIii1II
def III1iIii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOoO00OoOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 40 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 70 - 70: Ii + Ii - Ii % oO0o / IIiIiII11i
def III1IIi1iiiI11I1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiIioo0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 5 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
def OO0ooOOO0OOO ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  O0oIii11IiiIi ( )
 if O0oO == 1 :
  oO00O0o0oOOO ( )
 if O0oO == 2 :
  ooooOoo00 ( )
  if 7 - 7: oooOo0oo0oo * oO0o + ii . i1iIi * Iii
  if 82 - 82: iI11I1II1I1I * ii
  if 50 - 50: i1IiiiI1iI - IIiIiII11i
  if 33 - 33: III1iiIii / III1iiIii . Ii * Ii1I + I11i
def oO00O0o0oOOO ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , ii1iI11IiIIi in IIi :
  IIi1i1IiIIi1i ( 'Android Apps' + ii1iI11IiIIi , 'https://www.apkfiles.com' + OoOOoOooooOOo , 30035 , iiIi1IIiIi + 'apps.png' )
 for OoOOoOooooOOo , ii1iI11IiIIi in i1Iii1i1I :
  IIi1i1IiIIi1i ( 'Android Games' + ii1iI11IiIIi , 'https://www.apkfiles.com' + OoOOoOooooOOo , 30035 , iiIi1IIiIi + 'GAMES.png' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def IIIO00ooo0 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if '/cat' in url :
   IIi1i1IiIIi1i ( ( IiIi11iI ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def iI1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if '/app' in url :
   IIi1i1IiIIi1i ( ( IiIi11iI ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def iIi1O00oOOO0 ( url ) :
 Oooo0O = OooOoooOo ( url )
 I1ii1 = url
 if "page=" in str ( url ) :
  I1ii1 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  if 'apk' in url :
   Ii1I1i ( ( IiIi11iI ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oO0O00oOOoooO )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , I1ii1 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def Iiiiii ( name , url ) :
 Oooo0O = ooo ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( Oooo0O )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  oOOOO ( name , url , 'Brackets' )
def ooooOoo00 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'https://www.apkfiles.com/search?q=' + ( OO0oOOo ) . replace ( ' ' , '+' ) + '&search_type=1'
 III111i11IiI = OO0oO0o . lower ( )
 iIi1O00oOOO0 ( III111i11IiI )
 if 82 - 82: ooOoO0O00 + I11i - IIiIiII11i . o0ii1I
def oo0OOO0OOoOO ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( oOoOII1i1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , IiIi11iI + '.apk' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 51 - 51: i1iIi * IiI1i11I / ooOoO0O00
def IIi1I1 ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , IiIi11iI + '.mp4' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 37 - 37: I11i * I1ii11iIi11i
 if 11 - 11: i1i1I1IIii1II
def Oo0O0o00o00 ( name , url , description ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , name )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o0oI1I1i = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0oI1I1i
 print '======================================='
 extract . all ( o0OOOoO0 , o0oI1I1i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 42 - 42: IiI1i11I
 if 77 - 77: ooOoO0O00 * i1i1I1IIii1II % ii + o0o00Oo0O * i1iIi
 if 28 - 28: Iii . ii * oooOo0oo0oo + Ii % oOo0O0Ooo . iI11I1II1I1I
 if 63 - 63: IIiIiII11i - Iii . OOooOOo
 if 8 - 8: oOo0O0Ooo * i1iIi / III1iiIii + OOooOOo . III1iiIii - oooOo0oo0oo
def O0oIii11IiiIi ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , OoOOoOooooOOo , ooo0O0OOO000o , i11I , Oo0O in IIi :
  Ii1I1i ( IiIi11iI , OoOOoOooooOOo , 80003 , ooo0O0OOO000o , iiIi1IIiIi + 'APKToolsB.png' , Oo0O )
def oO00OO0o0ooO ( apk , ret = None ) :
 if apk == "kodi" :
  Iii1iIIIi11I1 = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( Iii1iIIIi11I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   IIII11Ii1I11I = IIi [ 0 ] [ 0 ]
   iIIIII1iiiiII = IIi [ 0 ] [ 1 ]
   I11II1 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( IIII11Ii1I11I , iIIIII1iiiiII )
  if ret == 'version' : return IIII11Ii1I11I
  else : return I11II1
 elif apk == "spmc" :
  O0oOo0o0000 = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( O0oOo0o0000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  IIII11Ii1I11I = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  I11II1 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( IIII11Ii1I11I , IIII11Ii1I11I )
  if ret == 'version' : return IIII11Ii1I11I
  else : return I11II1
def oOOOO ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  I1iIiI = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not I1iIiI : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  Oo0o0OoOoOo0 = name
  if I1iIiI :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not O0o ( url ) == True : oo0OoOO000O ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % Oo0o0OoOoOo0 , '' , 'Please Wait' )
   o0OOOoO0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( o0OOOoO0 )
   except : pass
   downloader . download ( url , o0OOOoO0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    I11iiIiiI1iIi11 = zipfile . ZipFile ( o0OOOoO0 )
    for file in I11iiIiiI1iIi11 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as iiii111II :
       I11iiI11I1II = file . split ( '/' ) [ 1 ]
       iiii111II . write ( I11iiIiiI1iIi11 . read ( file ) )
       xbmc . sleep ( 500 )
       iiii111II . close ( )
       try :
        os . remove ( o0OOOoO0 )
       except :
        pass
       o0OOOoO0 = os . path . join ( i1iIIi1 , I11iiI11I1II )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o0OOOoO0 + '")' )
  else : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 70 - 70: Ii1I . III1iiIii
 if 41 - 41: I11i % I1ii11iIi11i
 if 93 - 93: i1iIi
 if 82 - 82: Ii1I / i1iIi . Ii + oooOo0oo0oo - OOooOOo / IiI1i11I
def oOoo ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  OoOOoOooooOOo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + OoOOoOooooOOo )
  i1IIII1II ( ( IiIi11iI ) . replace ( '_' , ' ' ) , OoOOoOooooOOo )
  if 89 - 89: Iii % IiI1i11I * I1ii11iIi11i / i1IiiiI1iI * I1ii11iIi11i / i1iIi
def i1IIII1II ( name , url ) :
 if OO ( ) == 'android' :
  I1iIiI = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not I1iIiI : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  Oo0o0OoOoOo0 = name
  if I1iIiI :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not O0o ( url ) == True : oo0OoOO000O ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % Oo0o0OoOoOo0 , '' , 'Please Wait' )
   o0OOOoO0 = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( o0OOOoO0 )
   except : pass
   downloader . download ( url , o0OOOoO0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o0OOOoO0 + '")' )
  else : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oo0OoOO000O ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 14 - 14: ooOoO0O00 * iI11I1II1I1I - o0ii1I * OOooOOo - IiI1i11I / i1i1I1IIii1II
 if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
def oOoO0o0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 5 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 72 - 72: Iii * OOooOOo % i1IiiiI1iI % i1iIi
 if 22 - 22: oooOo0oo0oo - Ii1I / III1iiIii
def oOoooooOoO ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 30015 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 95 - 95: I11i
def oOo0OOoO0ooOOoo ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 O0o0O00o0o = url
 oO0O00oOOoooO = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for O0000 , IiIi11iI in IIi :
  if '.mp4' in IiIi11iI :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + O0000 , 222 , oO0O00oOOoooO , fanart , '' )
  if 'description' in IiIi11iI :
   Ii1I1i ( 'Read Description' , url + '/' + O0000 , 30017 , oO0O00oOOoooO , fanart , '' )
  if 'images' in IiIi11iI :
   I1I1II1I11 ( 'View Images' , url + '/' + O0000 , 30018 , oO0O00oOOoooO , fanart , '' )
  if 'url' in IiIi11iI :
   Ii1I1i ( 'Install Build On Android' , url + '/' + O0000 , 30016 , oO0O00oOOoooO , fanart , '' )
  if 'url' in IiIi11iI :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + O0000 , 30019 , oO0O00oOOoooO , fanart , '' )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 95 - 95: I1ii11iIi11i * oooOo0oo0oo + oOo0O0Ooo . o0o00Oo0O
def IIiIi1II1IiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oo0OoO ( url )
  if 3 - 3: III1iiIii - ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I
def O0oo0ooO00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oOoO0 ( url )
  if 50 - 50: i1IiiiI1iI * i1IiiiI1iI * I1ii11iIi11i - oO0o
def IIi1iI ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for oO0o0 in IIi :
  o0OIiII ( 'Description:' , oO0o0 )
  if 36 - 36: IiI1i11I * Iii * o0o00Oo0O * oooOo0oo0oo - I11i / Ii1I
def oooOo0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for O0000 , IiIi11iI in IIi :
  if 'png' in IiIi11iI :
   Ii1I1i ( 'image' , '' , '' , url + '/' + O0000 , url + '/' + O0000 , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 9 - 9: iI11I1II1I1I
def O0000ooO0OO0Oooo0o ( name , url , description ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , name + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOO0o ( )
 if 83 - 83: I11i % I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . Iii * o0o00Oo0O
 if 21 - 21: Ii - i1IiiiI1iI
def oOoO0 ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0OOOoO0O ( )
 if 21 - 21: Ii * IiI1i11I / i1iIi % IiI1i11I * I1ii11iIi11i
def oo0OoO ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0OOOoO0O ( )
 if 84 - 84: iI11I1II1I1I
def III1Ii11i1II ( name , url , description ) :
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0OOOoO0 = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0OOOoO0O ( )
 if 28 - 28: OOooOOo % i1i1I1IIii1II - oooOo0oo0oo + oooOo0oo0oo + i1i1I1IIii1II / iI11I1II1I1I
def OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def i11i1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : iiii111II = open ( oO , 'w' ) ; iiii111II . close ( )
 with open ( oO , 'a' ) as iiii111II :
  oo0o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  iiii111II . write ( oo0o . rstrip ( '\r\n' ) + '\n' )
def o0OOOoO0O ( ) :
 O0oO = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO == 0 : return
 elif O0oO == 1 : pass
 o0oooOO00 = OO ( )
 i11i1 ( "Platform: " + str ( o0oooOO00 ) )
 os . _exit ( 1 )
 i11i1 ( "Force close failed!  Trying alternate methods." )
 if o0oooOO00 == 'osx' :
  i11i1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0oooOO00 == 'linux' :
  i11i1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0oooOO00 == 'android' :
  i11i1 ( "############ try android force close #################" )
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
 elif o0oooOO00 == 'windows' :
  i11i1 ( "############ try windows force close #################" )
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
  i11i1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  i11i1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 69 - 69: I11i + Ii1I / iI11I1II1I1I . III1iiIii % Ii1I * OOooOOo
  if 13 - 13: iI11I1II1I1I + IiI1i11I / o0ii1I / ooOoO0O00 % oO0o - iI11I1II1I1I
  if 60 - 60: i1IiiiI1iI
def iiIII1i1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( url ) :
  for file in oOo0O0 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    i11I1iIii1i11 = open ( ( os . path . join ( ooO0IIiIIiiiiiII1 , file ) ) ) . read ( )
    iIi1i1II = i11I1iIii1i11 . replace ( oOo0oooo00o , 'special://home/' )
    iiii111II = open ( ( os . path . join ( ooO0IIiIIiiiiiII1 , file ) ) , mode = 'w' )
    iiii111II . write ( str ( iIi1i1II ) )
    iiii111II . close ( )
 o0OOOoO0O ( )
 if 62 - 62: I1ii11iIi11i * iI11I1II1I1I
def I1o0 ( ) :
 IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 11 - 11: Ii1I + IiI1i11I
def oOOo ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def OOoOO00OO0O0o ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def oOoOOo0oO0OoO0O ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in i1Iii1i1I :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + IiIi11iI + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + IiIi11iI + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oO0O00oOOoooO )
def o0OOOoO ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( Oooo0O )
 for url in IIi :
  ooOoO00 ( url )
def ooo0 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo
 OO0OOoooOo00 = 'https://www.radionomy.com/en/search/index?query=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( OO0OOoooOo00 )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + IiIi11iI + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OoOOoOooooOOo , 70005 , oO0O00oOOoooO )
  if 63 - 63: ooOoO0O00
  if 56 - 56: I1ii11iIi11i
def ooOooO ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.listenlive.eu/' + OoOOoOooooOOo , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def I11i1I1 ( url ) :
 Oooo0O = ooo ( url )
 if 52 - 52: oooOo0oo0oo + I1ii11iIi11i
 if 67 - 67: Ii1I % ii
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , III1I1I11 , url , Oo0 in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' [COLORorangered] ' + Oo0 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[CR]' + III1I1I11 + '[CR]' + Oo0 + '[/COLOR]' )
  if 6 - 6: i1IiiiI1iI / ii / IiI1i11I / i1IiiiI1iI + IiI1i11I - OOooOOo
def oO0iIiII111 ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.toonjet.com/' + OoOOoOooooOOo , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO in IIi :
  if 'ol.gif' in oO0O00oOOoooO :
   pass
  elif 'link_block_' in oO0O00oOOoooO :
   pass
  elif '.png' in oO0O00oOOoooO :
   pass
  else :
   IIi1i1IiIIi1i ( ( oO0O00oOOoooO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iii111 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( Oooo0O )
 for url in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 59 - 59: i1iIi * i1IiiiI1iI
  if 57 - 57: III1iiIii * iI11I1II1I1I . I1ii11iIi11i / i1iIi . oooOo0oo0oo % i1iIi
def IiI1i1Ii1iiI1 ( ) :
 oOo0Oo0Oo0 ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 oOo0Oo0Oo0 ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 49 - 49: ooOoO0O00 . oO0o / Ii + o0ii1I % o0o00Oo0O + Ii1I
def I1iI1Ii11 ( ) :
 oOo0Oo0Oo0 ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 oOo0Oo0Oo0 ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 oOo0Oo0Oo0 ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 34 - 34: o0ii1I * oOo0O0Ooo + Iii * OOooOOo - IIiIiII11i
def OOoo0ooOo000oo ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for IiIi11iI , OoOOoOooooOOo , OoO0O00oo in IIi :
  if 'Parent' in IiIi11iI :
   pass
  elif '2' in OoO0O00oo :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 71 - 71: o0o00Oo0O % o0o00Oo0O
def oooooOOo0Oo ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for IiIi11iI , OoOOoOooooOOo , OoO0O00oo in IIi :
  if OO0oOOo in IiIi11iI . lower ( ) :
   if '1' in OoO0O00oo :
    oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in OoO0O00oo :
    oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in OoO0O00oo :
    oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 29 - 29: o0o00Oo0O * Ii / ii / I11i . i1iIi
    if 70 - 70: ii . i1iIi / i1i1I1IIii1II . i1i1I1IIii1II - I11i
def i1II1i1iiI1 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for IiIi11iI , OoOOoOooooOOo , OoO0O00oo in IIi :
  if '1' in OoO0O00oo :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in OoO0O00oo :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in OoO0O00oo :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoOOoOooooOOo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: o0ii1I . Ii % o0o00Oo0O % i1IiiiI1iI - I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % o0ii1I + oOo0O0Ooo
def ooOOO000O ( url ) :
 O0000 = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in i1Iii1i1I :
  if 'mp3' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0000 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0000 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0000 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in IiIi11iI :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0000 + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 90 - 90: o0ii1I . Ii + iI11I1II1I1I
   if 32 - 32: I1ii11iIi11i - o0ii1I . ii - ii - I1ii11iIi11i . iI11I1II1I1I
   if 34 - 34: I1ii11iIi11i
def IiI1I1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0000 = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  if 'Parent' in IiIi11iI :
   pass
  elif '.db' in IiIi11iI :
   pass
  elif '.jpg' in IiIi11iI :
   pass
  elif '.html' in IiIi11iI :
   pass
  elif '.doc' in IiIi11iI :
   pass
  elif 'mp3' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0000 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0000 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0000 + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: oOo0O0Ooo . IIiIiII11i + i1IiiiI1iI / oO0o % oOo0O0Ooo . ii
   if 64 - 64: iI11I1II1I1I + IIiIiII11i . IiI1i11I % I1ii11iIi11i * i1iIi
def iiii1i1 ( ) :
 oOo0Oo0Oo0 ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 oOo0Oo0Oo0 ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 oOo0Oo0Oo0 ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . i1iIi - ooOoO0O00
def oOOoOo0OoOO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OoOOoOooooOOo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oO0O00oOOoooO :
   pass
  else :
   oOo0Oo0Oo0 ( oO0O00oOOoooO , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OoOOoOooooOOo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oO0O00oOOoooO + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 90 - 90: oO0o / o0ii1I % iI11I1II1I1I / o0o00Oo0O * i1i1I1IIii1II / oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: IIiIiII11i . i1iIi / i1i1I1IIii1II
 if 54 - 54: i1iIi - iI11I1II1I1I - Iii % o0ii1I / IIiIiII11i
def oooooO0oO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  if '</a>' in IiIi11iI :
   pass
  elif '(' in IiIi11iI :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: o0ii1I - IIiIiII11i . Iii / OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: i1iIi
def IIi1IIII ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if OO0oOOo in IiIi11iI . lower ( ) :
   if '</a>' in IiIi11iI :
    pass
   elif '(' in IiIi11iI :
    oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoOOoOooooOOo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoOOoOooooOOo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 33 - 33: IIiIiII11i . Ii1I - o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
    if 53 - 53: o0ii1I / oOo0O0Ooo * o0ii1I + I11i + i1i1I1IIii1II - I1ii11iIi11i
def IIi1iiIIi1i ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if '</a>' in IiIi11iI :
   pass
  elif '(' in IiIi11iI :
   oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoOOoOooooOOo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoOOoOooooOOo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 5 - 5: ii / III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: oooOo0oo0oo % Ii
 if 77 - 77: oooOo0oo0oo % Ii - Ii1I
def I1oooO00oOOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0000 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( O0000 )
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IIIii111i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in IIi :
  if '<p align' in IiIi11iI :
   pass
  elif '&nbsp;' in IiIi11iI :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 58 - 58: oooOo0oo0oo % IiI1i11I * o0o00Oo0O + Ii1I - III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Iii + Iii
 if 46 - 46: i1IiiiI1iI % Ii1I + o0ii1I
def IiI1i111IiIiIi1 ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'ongoing' in OoOOoOooooOOo :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in OoOOoOooooOOo :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in OoOOoOooooOOo :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in OoOOoOooooOOo :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in OoOOoOooooOOo :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def Ooii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iii1iII1I = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oO0O00oOOoooO , oO0O00oOOoooO , IiIi11iI )
 for url , IiIi11iI in iii1iII1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def i11iII1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iII = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOooo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 i11iI1111ii1I = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in oOooo :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , IiIi11iI in iII :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def OoOo0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 22 - 22: Ii + OOooOOo + ii
def II1IIIii ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if '9cart' in OoOOoOooooOOo :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 2 - 2: i1iIi - Iii * ooOoO0O00 % oooOo0oo0oo / ii * oooOo0oo0oo
def OOO000ooO0OO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Iiii1iI1i = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , IiIi11iI in Iiii1iI1i :
  if '9cart' in url :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - o0ii1I * iI11I1II1I1I
def OO0ooo0OOO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 20003 , oO0O00oOOoooO )
 for url , IiIi11iI in i1Iii1i1I :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 69 - 69: i1IiiiI1iI + iI11I1II1I1I * i1i1I1IIii1II + III1iiIii % i1iIi - o0ii1I
def o00OOOoO000 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   IIi1i1IiIIi1i ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 79 - 79: IiI1i11I / i1IiiiI1iI + I11i
def oO0oOO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 84 - 84: Ii / I11i % iI11I1II1I1I . i1iIi . oO0o / IiI1i11I
def ooooo0oo0OO ( url ) :
 url = cloudflare . source ( url )
 Ii11iIII ( url )
 if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
def i1oo0OO0Oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  Ii11iIII ( url )
  if 4 - 4: OOooOOo * o0o00Oo0O - Iii
  if 72 - 72: Iii + i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
def i1II11II1 ( ) :
 if 13 - 13: i1IiiiI1iI % I11i + oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def oOOO0O0Ooo ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 11 - 11: IiI1i11I
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if OO0oOOo in IiIi11iI . lower ( ) :
   if 'Dad!' in IiIi11iI :
    pass
   elif 'Family Guy' in IiIi11iI :
    pass
   elif '2 Stupid' in IiIi11iI :
    pass
   elif 'The Zelfs' in IiIi11iI :
    pass
   elif 'A Clone' in IiIi11iI :
    pass
   elif 'A.T.O.M' in IiIi11iI :
    pass
   elif 'Almost Naked' in IiIi11iI :
    pass
   elif 'Angry Kid' in IiIi11iI :
    pass
   elif 'Annoying Orange' in IiIi11iI :
    pass
   elif 'Aqua Teen' in IiIi11iI :
    pass
   elif 'Assy Mcgee' in IiIi11iI :
    pass
   elif 'Astroblast' in IiIi11iI :
    pass
   elif 'Atomic Betty' in IiIi11iI :
    pass
   elif 'Axe Cop' in IiIi11iI :
    pass
   elif 'Baby Playpen' in IiIi11iI :
    pass
   elif 'Beavis and Butt' in IiIi11iI :
    pass
   elif 'Celebrity Deathmatch' in IiIi11iI :
    pass
   elif 'Clerks The' in IiIi11iI :
    pass
   elif 'Crapston Villas' in IiIi11iI :
    pass
   elif 'Duckman:' in IiIi11iI :
    pass
   elif 'Stripperella' in IiIi11iI :
    pass
   elif 'Vixen' in IiIi11iI :
    pass
   else :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 5 - 5: oooOo0oo0oo + IiI1i11I
    if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
def iIIIiIi1I1i ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if 'Dad!' in IiIi11iI :
   pass
  elif 'Family Guy' in IiIi11iI :
   pass
  elif '2 Stupid' in IiIi11iI :
   pass
  elif 'The Zelfs' in IiIi11iI :
   pass
  elif 'A Clone' in IiIi11iI :
   pass
  elif 'A.T.O.M' in IiIi11iI :
   pass
  elif 'Almost Naked' in IiIi11iI :
   pass
  elif 'Angry Kid' in IiIi11iI :
   pass
  elif 'Annoying Orange' in IiIi11iI :
   pass
  elif 'Aqua Teen' in IiIi11iI :
   pass
  elif 'Assy Mcgee' in IiIi11iI :
   pass
  elif 'Astroblast' in IiIi11iI :
   pass
  elif 'Atomic Betty' in IiIi11iI :
   pass
  elif 'Axe Cop' in IiIi11iI :
   pass
  elif 'Baby Playpen' in IiIi11iI :
   pass
  elif 'Beavis and Butt' in IiIi11iI :
   pass
  elif 'Celebrity Deathmatch' in IiIi11iI :
   pass
  elif 'Clerks The' in IiIi11iI :
   pass
  elif 'Crapston Villas' in IiIi11iI :
   pass
  elif 'Duckman:' in IiIi11iI :
   pass
  elif 'Stripperella' in IiIi11iI :
   pass
  elif 'Vixen' in IiIi11iI :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( url ) :
 Oooo0O = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Oooo0O )
 for oO0O00oOOoooO in i1Iii1i1I :
  O0Ooo0o = oO0O00oOOoooO
 Iiii1iI1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( Oooo0O )
 for url in Iiii1iI1i :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 10007 , O0Ooo0o )
  if 42 - 42: iI11I1II1I1I / Iii . o0o00Oo0O . o0ii1I
  if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: o0o00Oo0O + i1i1I1IIii1II + I11i
def oO0IIi11IiiiI11i ( url , IMAGE ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  print IiIi11iI + '     ' + url
  if 'easy' in url :
   OO00oO ( url )
   if 80 - 80: o0ii1I - Ii1I . o0ii1I / Ii + o0o00Oo0O . III1iiIii
   if 15 - 15: I1ii11iIi11i + IiI1i11I + oOo0O0Ooo * I11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 33 - 33: I11i * I1ii11iIi11i
def OO00oO ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( Oooo0O )
 for url in IIi :
  ooOoO00 ( url )
  if 88 - 88: i1IiiiI1iI % oooOo0oo0oo - OOooOOo - OOooOOo . oOo0O0Ooo
  if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - i1IiiiI1iI
  if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
def Oo0o0OOo0Oo0 ( ) :
 if 88 - 88: o0ii1I / ii % OOooOOo - ooOoO0O00
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 49 - 49: I11i - iI11I1II1I1I
def o00oo00O0OoOo ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  if 'elete' in IiIi11iI :
   pass
  else :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 222 , oO0O00oOOoooO )
   if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
def ii1iIi111i1 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOoOoO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , o0oOoo00 , i1iII1IiiIiI1 in oOoOoO :
  for OO0oOOo in o0oOoo00 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ii11iIi1iIiii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OoOOoOooooOOo , IiIi11iI in Ii11iIi1iIiii :
    if 'tube' in OoOOoOooooOOo :
     pass
    elif 'stage' in OoOOoOooooOOo :
     oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + o0oOoo00 + '   -   ' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oO0O00oOOoooO , )
    elif 'vee' in OoOOoOooooOOo :
     pass
     if 11 - 11: Ii1I / Ii1I
def ii1IIIIi1 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOoOoO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , o0oOoo00 , i1iII1IiiIiI1 in oOoOoO :
  Ii11iIi1iIiii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OoOOoOooooOOo , IiIi11iI in Ii11iIi1iIiii :
   if 'tube' in OoOOoOooooOOo :
    pass
   elif 'stage' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + o0oOoo00 + '   -   ' + IiIi11iI + '[/COLOR]' , ( OoOOoOooooOOo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oO0O00oOOoooO )
   elif 'vee' in OoOOoOooooOOo :
    pass
    if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
    if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: OOooOOo - Ii
def OooOoOOo0oO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O00O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O00O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O00O :
  OO0o0oO0O000o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 94 - 94: OOooOOo % IiI1i11I
  if 39 - 39: OOooOOo + i1IiiiI1iI % o0o00Oo0O
  if 26 - 26: i1iIi + OOooOOo
  if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
  if 6 - 6: i1IiiiI1iI
  if 46 - 46: IIiIiII11i * i1IiiiI1iI
  if 23 - 23: ooOoO0O00 - o0o00Oo0O
def I1II ( ) :
 if 6 - 6: i1iIi % ii * i1IiiiI1iI - III1iiIii
 I1iioO0 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 I1iioO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 73 - 73: i1IiiiI1iI
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 25 - 25: III1iiIii
def OOii ( ) :
 I1iioO0 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 I1iioO0 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 14 - 14: Ii1I * ooOoO0O00 / iI11I1II1I1I / i1i1I1IIii1II / o0o00Oo0O % I1ii11iIi11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def i1IIII11II1 ( ) :
 if 75 - 75: oO0o - OOooOOo - ooOoO0O00 % I1ii11iIi11i - IIiIiII11i
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 O00OOo0oOOooO0o0O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 61 - 61: I1ii11iIi11i + ii / Ii
 for ii1ii in O00OOo0oOOooO0o0O :
  IIiI1i = oO0 + ii1ii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( IIiI1i )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , i11I , IiIi11iI in IIi :
   if OO0oOOo in IiIi11iI . lower ( ) :
    I11OoooO ( IiIi11iI , OoOOoOooooOOo , 222 , i1oOOoo0o0OOOO , i11I , o00O0O )
    if 49 - 49: III1iiIii + oO0o + o0o00Oo0O
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 95 - 95: IIiIiII11i * OOooOOo . oooOo0oo0oo + Ii1I + I11i + OOooOOo
    if 94 - 94: I1ii11iIi11i + i1IiiiI1iI / i1iIi . Iii . Ii / ooOoO0O00
def o0OOoo ( ) :
 if 52 - 52: oO0o
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 O00OOo0oOOooO0o0O = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 49 - 49: o0ii1I . Ii1I % i1iIi . I1ii11iIi11i * oooOo0oo0oo
 for ii1ii in O00OOo0oOOooO0o0O :
  Ii1iI = oO0 + ii1ii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( Ii1iI )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for IiIi11iI , o00O0O , OoOOoOooooOOo , oO0O00oOOoooO , i11I , oo0oOO00oO in IIi :
   if OO0oOOo in IiIi11iI . lower ( ) :
    I1iioO0 ( IiIi11iI , OoOOoOooooOOo , oo0oOO00oO , oO0O00oOOoooO , i11I , o00O0O )
    if 40 - 40: oOo0O0Ooo
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 96 - 96: oO0o - IiI1i11I
    if 16 - 16: i1IiiiI1iI / o0o00Oo0O . IIiIiII11i * OOooOOo
def i1IiI1I111iI1 ( ) :
 if 82 - 82: I11i - oooOo0oo0oo
 Oooo0O = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , o00O0O , OoOOoOooooOOo , oO0O00oOOoooO , i11I , oo0oOO00oO in IIi :
  I1iioO0 ( IiIi11iI , OoOOoOooooOOo , oo0oOO00oO , oO0O00oOOoooO , i11I , o00O0O )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def O00o0Oo0o0 ( url ) :
 if 100 - 100: Ii1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oO0o0OooOO0 = ( '%s%s' % ( iiIiooOo0oo0O0O , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in IIi :
  iII1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for I1I1I1IIi1III in iII1 :
   if I1I1I1IIi1III == url :
    IiIi11iI = ( '[COLORred]Watched - [/COLOR]' + IiIi11iI ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I11OoooO ( IiIi11iI , url , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
  if 41 - 41: i1i1I1IIii1II / ii . I1ii11iIi11i / o0o00Oo0O . Ii % I11i
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 50 - 50: i1iIi
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
  if 83 - 83: Ii - oOo0O0Ooo * Ii
def O0ooO0oOO ( url ) :
 if 53 - 53: o0o00Oo0O / IIiIiII11i - oooOo0oo0oo - i1i1I1IIii1II . oooOo0oo0oo
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , o00O0O , url , oO0O00oOOoooO , i11I , oo0oOO00oO in IIi :
  I1iioO0 ( IiIi11iI , url , oo0oOO00oO , oO0O00oOOoooO , i11I , o00O0O )
  if 4 - 4: oooOo0oo0oo - I1ii11iIi11i % IIiIiII11i - oO0o % ooOoO0O00 % i1iIi
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 31 - 31: iI11I1II1I1I / ii
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + o0ii1I . oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: iI11I1II1I1I + i1IiiiI1iI - Ii1I - ooOoO0O00 * OOooOOo
def I11OoooO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 4 - 4: ii
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  II11i111i1iIiiIiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = False )
 return o0iIiiIiiIi
 if 7 - 7: III1iiIii
def I1iioO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 26 - 26: oooOo0oo0oo + I1ii11iIi11i
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  II11i111i1iIiiIiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = True )
 return o0iIiiIiiIi
if 71 - 71: oOo0O0Ooo . i1iIi
if 43 - 43: Ii1I * oooOo0oo0oo
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
if 42 - 42: ii / i1IiiiI1iI . I11i / o0o00Oo0O - III1iiIii * III1iiIii
def i111iIi11Ii ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 67 - 67: o0ii1I . I1ii11iIi11i
def i11I111iII1i1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oO0oO0 = [ ]
 try :
  if 22 - 22: o0ii1I - Iii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  i111iIi11Ii ( 'Making Favorites File' )
  oO0oO0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i11I1iIii1i11 = open ( i1I1iI , "w" )
  i11I1iIii1i11 . write ( json . dumps ( oO0oO0 ) )
  i11I1iIii1i11 . close ( )
 else :
  i111iIi11Ii ( 'Appending Favorites' )
  i11I1iIii1i11 = open ( i1I1iI ) . read ( )
  II1IoooOoO00O = json . loads ( i11I1iIii1i11 )
  II1IoooOoO00O . append ( ( name , url , iconimage , fanart , mode ) )
  iIi1i1II = open ( i1I1iI , "w" )
  iIi1i1II . write ( json . dumps ( II1IoooOoO00O ) )
  iIi1i1II . close ( )
  if 42 - 42: III1iiIii * IiI1i11I . Ii1I - iI11I1II1I1I . i1iIi + Iii
  if 35 - 35: IiI1i11I . oOo0O0Ooo / IIiIiII11i % III1iiIii
def iiiIiIIiIiiii ( ) :
 if os . path . exists ( i1I1iI ) == False :
  oO0oO0 = [ ]
  i111iIi11Ii ( 'Making Favorites File' )
  oO0oO0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  i11I1iIii1i11 = open ( i1I1iI , "w" )
  i11I1iIii1i11 . write ( json . dumps ( oO0oO0 ) )
  i11I1iIii1i11 . close ( )
 else :
  o00O0OooO0 = json . loads ( open ( i1I1iI ) . read ( ) )
  OooOoo = len ( o00O0OooO0 )
  for iii1II11II1 in o00O0OooO0 :
   IiIi11iI = iii1II11II1 [ 0 ]
   OoOOoOooooOOo = iii1II11II1 [ 1 ]
   i1oOOoo0o0OOOO = iii1II11II1 [ 2 ]
   try :
    I11i1Iii1I = iii1II11II1 [ 3 ]
    if I11i1Iii1I == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     I11i1Iii1I = i1oOOoo0o0OOOO
    else :
     I11i1Iii1I = i11I
   try : iIIiII1 = iii1II11II1 [ 5 ]
   except : iIIiII1 = None
   try : iI1Iii1i1 = iii1II11II1 [ 6 ]
   except : iI1Iii1i1 = None
   if 87 - 87: Ii * IIiIiII11i - o0ii1I % ii
   if iii1II11II1 [ 4 ] == 0 :
    I1I1II1I11 ( IiIi11iI , OoOOoOooooOOo , '' , i1oOOoo0o0OOOO , i11I , '' , 'fav' )
   else :
    I1I1II1I11 ( IiIi11iI , OoOOoOooooOOo , iii1II11II1 [ 4 ] , i1oOOoo0o0OOOO , i11I , '' , 'fav' )
    if 55 - 55: ooOoO0O00
def oOOO0oo0 ( name ) :
 II1IoooOoO00O = json . loads ( open ( i1I1iI ) . read ( ) )
 for oO00oOo0OOO in range ( len ( II1IoooOoO00O ) ) :
  if II1IoooOoO00O [ oO00oOo0OOO ] [ 0 ] == name :
   del II1IoooOoO00O [ oO00oOo0OOO ]
   iIi1i1II = open ( i1I1iI , "w" )
   iIi1i1II . write ( json . dumps ( II1IoooOoO00O ) )
   iIi1i1II . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 13 - 13: OOooOOo - oO0o * ii
 if 26 - 26: ii
def O00Oo00OOoO0 ( ) :
 ooo0000oo0 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 O0oooo000o = open ( ooo0000oo0 , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 O0oooo000o . write ( r'[' + IiII + ']' + '\n' )
 for IiIi11iI , oO0O00oOOoooO , IIiIiI11II , OoOOoOooooOOo in IIi :
  OoOOoOooooOOo = ( OoOOoOooooOOo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  oOo00 = ( IiIi11iI + '=plugin://' + IiII + '/?url=' + OoOOoOooooOOo + '&mode=10012&name=' + ( IiIi11iI ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oO0O00oOOoooO ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oO0O00oOOoooO ) . replace ( ' ' , '' ) + '+&amp;description=' )
  O0oooo000o . write ( oOo00 + '\n' )
  if 75 - 75: iI11I1II1I1I / IIiIiII11i / o0ii1I / OOooOOo
  if 77 - 77: OOooOOo
def i111 ( ) :
 Oooo0O = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo in IIi :
  IIi1i1IiIIi1i ( '24/7' , OoOOoOooooOOo , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 27 - 27: iI11I1II1I1I + i1i1I1IIii1II % I1ii11iIi11i
def OooOoo0Oo ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  Ii1I1i ( IiIi11iI , ( OoOOoOooooOOo ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def I1IiiiiI1i1I ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  Ii1I1i ( IiIi11iI , ( OoOOoOooooOOo ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def Iio00 ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  Ii1I1i ( IiIi11iI , ( OoOOoOooooOOo ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def ooiiI1ii ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  Ii1I1i ( IiIi11iI , ( OoOOoOooooOOo ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def ii1ii111I11I1 ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  Ii1I1i ( IiIi11iI , OoOOoOooooOOo , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 1 - 1: oooOo0oo0oo / Ii1I - ii . oOo0O0Ooo . IIiIiII11i % IiI1i11I
  if 59 - 59: i1iIi % I1ii11iIi11i - i1i1I1IIii1II + III1iiIii
def I1IIII ( ) :
 if 69 - 69: III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 24 - 24: oO0o / o0o00Oo0O * i1iIi % iI11I1II1I1I + ooOoO0O00 % o0o00Oo0O
def I1I11i ( ) :
 if 93 - 93: IIiIiII11i . Iii - ooOoO0O00 * OOooOOo
 Oooo0O = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , iiI1i11II in IIi :
  I1I1II1I11 ( IiIi11iI + '  -  ' + ( iiI1i11II ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoOOoOooooOOo , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 28 - 28: Iii % i1IiiiI1iI
  if 49 - 49: III1iiIii % I11i . Ii1I / oooOo0oo0oo . o0ii1I * Ii1I
  if 17 - 17: Ii1I * ii % ooOoO0O00 % ii . IiI1i11I
def iIo0O000O00o ( ) :
 if 38 - 38: ii . IiI1i11I
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
 if 43 - 43: ii
def i1i111I ( url ) :
 O0o0O00o0o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( O0o0O00o0o )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 91 - 91: Ii1I * OOooOOo / Ii1I % oooOo0oo0oo
  if 22 - 22: IiI1i11I / oOo0O0Ooo + i1i1I1IIii1II
  if 93 - 93: ii * o0ii1I / o0o00Oo0O + o0ii1I - iI11I1II1I1I
  if 6 - 6: III1iiIii - I1ii11iIi11i - Iii - o0o00Oo0O % ii
def Oo0OIIi ( ) :
 if 27 - 27: Ii % IiI1i11I + o0ii1I . oooOo0oo0oo
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 OoOOoOooooOOo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OO0oOOo ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( OoOOoOooooOOo )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  if OO0oOOo in IiIi11iI . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 9 - 9: oO0o
   if 43 - 43: o0ii1I . oooOo0oo0oo + oOo0O0Ooo * Ii
   if 2 - 2: oooOo0oo0oo
def IiOoo0o0OO0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0000 , o0oOOoOOO , Oo , IiIi11iI in IIi :
  O0o00OoooO = ( Oo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IiI1i1iI = ( o0oOOoOOO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iIIi = 'Season ' + IiI1i1iI + 'Episode ' + O0o00OoooO + IiIi11iI
  iIIIII ( iIIi , O0000 )
  if 24 - 24: IIiIiII11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 23 - 23: I1ii11iIi11i - IiI1i11I
  if 79 - 79: Iii . o0o00Oo0O - ooOoO0O00
def iIIIII ( name , url ) :
 O0000 = url
 II1iII11 = name
 o0o = cloudflare . source ( O0000 )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for O00O , iiiI1IiIi1i1I in i1Iii1i1I :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + II1iII11 + iiiI1IiIi1i1I + '[/COLOR]' , O00O , 222 , iiIi1IIiIi + 'dtv.png' )
  if 94 - 94: o0ii1I + o0o00Oo0O - ii / o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: ii / oooOo0oo0oo - oO0o % ii
 if 25 - 25: I1ii11iIi11i % I11i % ooOoO0O00
def iIiiiii1i ( ) :
 if 31 - 31: III1iiIii . IIiIiII11i % I1ii11iIi11i * o0ii1I + o0ii1I
 if 87 - 87: oO0o
 if 23 - 23: oooOo0oo0oo + i1iIi / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: IiI1i11I - I11i
 if 92 - 92: I1ii11iIi11i % I11i - i1iIi / i1iIi / OOooOOo
 if 84 - 84: oooOo0oo0oo
 if 4 - 4: III1iiIii . i1IiiiI1iI / o0ii1I / IiI1i11I + IIiIiII11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . Iii - o0ii1I
def OOOo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii111OO0oOOOOO = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oO0O00oOOoooO , '' , '' )
 for url in ii111OO0oOOOOO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 87 - 87: ii . i1iIi % iI11I1II1I1I . iI11I1II1I1I % Ii1I . i1IiiiI1iI
def i1ii1i1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii111OO0oOOOOO = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  oO0O00oOOoooO = 'http://watchepisodes.cc/' + oO0O00oOOoooO
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 10093 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
 for url in ii111OO0oOOOOO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 42 - 42: i1i1I1IIii1II
def iiiiiiI1iIi ( url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Oo , url , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + Oo + ' - ' + IiIi11iI + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oO0O00oOOoooO , '' , '' )
  if 40 - 40: Ii1I * oO0o % ii
def OOoOOOo00 ( url , iconimage ) :
 oO0O00oOOoooO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in IIi :
  if 'player' in IiIi11iI :
   pass
  elif 'vod' in IiIi11iI :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , oO0O00oOOoooO , '' , '' )
   if 86 - 86: oO0o - Iii
   if 83 - 83: oOo0O0Ooo % I1ii11iIi11i + o0ii1I + Ii
   if 70 - 70: iI11I1II1I1I
   if 79 - 79: Ii
   if 20 - 20: ooOoO0O00 - III1iiIii + III1iiIii . ii . oOo0O0Ooo + Iii
   if 10 - 10: III1iiIii / I1ii11iIi11i
def iiIi1IIiI ( ) :
 if 82 - 82: Ii1I / IiI1i11I + Ii1I + i1IiiiI1iI
 if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / i1iIi % oOo0O0Ooo % ooOoO0O00
 if 87 - 87: I11i % ooOoO0O00 + i1i1I1IIii1II - iI11I1II1I1I . oooOo0oo0oo + Ii
 if 83 - 83: Ii1I * IIiIiII11i . i1IiiiI1iI - Iii
 if 46 - 46: oO0o % Ii1I
 if 58 - 58: i1i1I1IIii1II + III1iiIii % IiI1i11I - o0ii1I - oooOo0oo0oo % o0ii1I
 if 86 - 86: I11i
 if 15 - 15: i1i1I1IIii1II - iI11I1II1I1I - IIiIiII11i - III1iiIii % Ii1I
 if 80 - 80: III1iiIii * IiI1i11I . ooOoO0O00 % o0ii1I % Ii1I + i1iIi
 if 6 - 6: Ii1I . i1i1I1IIii1II . oO0o + III1iiIii
 if 65 - 65: Ii1I / i1iIi
 if 23 - 23: oooOo0oo0oo / oooOo0oo0oo * I11i * oooOo0oo0oo
 if 57 - 57: IiI1i11I
 if 29 - 29: oOo0O0Ooo
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 41 - 41: i1IiiiI1iI * oO0o - IiI1i11I . o0ii1I
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - i1i1I1IIii1II + i1IiiiI1iI
def Ii1111iI1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00O0O = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O00O0O ) )
 for url , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 78 - 78: Ii1I . IiI1i11I % IIiIiII11i
def Oo0o0OO0O0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 98 - 98: o0o00Oo0O / i1i1I1IIii1II / IiI1i11I
def oOoOoOo0oOoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  if 'episode' in url :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
  if 2 - 2: IIiIiII11i + Iii . oO0o
def i1IIIi111111 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ii1iIii1I1 = 'http://www.watchseriesgo.to/search/' + OO0oOOo . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( O0Ii1iIii1I1 )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , OoOOoOooooOOo , IiIi11iI in IIi :
  if 'watch online' in IiIi11iI :
   pass
  else :
   print OoOOoOooooOOo
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.watchseriesgo.to' + OoOOoOooooOOo , 10044 , oO0O00oOOoooO , '' , '' )
   if 21 - 21: OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * ii . I1ii11iIi11i
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 22 - 22: i1iIi % OOooOOo / I11i
def oO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI , Oo , o00O0O in IIi :
  iIi11ii = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( Oo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIi11ii + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oO0O00oOOoooO , '' , o00O0O )
  if 31 - 31: ii % Ii - IIiIiII11i * Ii
def ooO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  iIi11ii = ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIi11ii + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 40 - 40: i1IiiiI1iI * OOooOOo % i1IiiiI1iI - o0o00Oo0O
def O0O0ooO0oO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oO0O00oOOoooO , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 74 - 74: oO0o / III1iiIii % III1iiIii - IiI1i11I
def Iii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O00O0O = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o0oOOoOOO , oOoOoO in O00O0O :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oOoOoO ) )
  for url , IiIi11iI in IIi :
   iIi11ii = ( o0oOOoOOO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIi11ii + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 3 - 3: Iii - oooOo0oo0oo + OOooOOo * oO0o % i1IiiiI1iI
class ii1IiIi1iIi ( ) :
 if 16 - 16: oooOo0oo0oo % oOo0O0Ooo . i1IiiiI1iI * oO0o % o0o00Oo0O . oooOo0oo0oo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 94 - 94: Ii1I
  iIi11ii = name
  self . Get_Sources ( OoOOoOooooOOo , iIi11ii )
  if 33 - 33: Ii1I + Ii1I . o0ii1I
  if 27 - 27: IIiIiII11i - Ii - ii
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OoOOoOooooOOo , IiIi11iI in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + OoOOoOooooOOo
   self . Get_site_link ( URL , season_name )
   if 90 - 90: oOo0O0Ooo
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  Iiii1iI1i = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in Iiii1iI1i :
   self . main ( url , season_name )
   if 4 - 4: oooOo0oo0oo % i1iIi - oooOo0oo0oo - I11i
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iI1IIIiIII11 = 'DACLIPS'
   if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
    pass
   else :
    self . daclips ( url , season_name , iI1IIIiIII11 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    iI1IIIiIII11 = 'THEVIDEO'
    if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
     pass
    else :
     self . thevideo ( url , season_name , iI1IIIiIII11 )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     iI1IIIiIII11 = 'ALLMYVIDEOS'
     if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , iI1IIIiIII11 )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      iI1IIIiIII11 = 'VIDSPOT'
      if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
       pass
      else :
       self . vidspot ( url , season_name , iI1IIIiIII11 )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       iI1IIIiIII11 = 'VODLOCKER'
       if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , iI1IIIiIII11 )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        iI1IIIiIII11 = 'VIDTO'
        if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
         pass
        else :
         self . vidto ( url , season_name , iI1IIIiIII11 )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 70 - 70: ii + oO0o * I1ii11iIi11i
       else :
        if 'youwatch' in url :
         iI1IIIiIII11 = 'YouWatch'
         if iI1IIIiIII11 in ii1IiIi1iIi . source_list :
          pass
         else :
          self . youwatch ( url , season_name , iI1IIIiIII11 )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 20 - 20: Ii - IIiIiII11i - i1iIi % i1i1I1IIii1II . i1iIi
          if 50 - 50: iI11I1II1I1I + i1IiiiI1iI - Iii - ii
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for Iii11i , IiIi11iI in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 84 - 84: OOooOOo - Iii
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i , IiIi11iI in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 80 - 80: Ii % oooOo0oo0oo - I1ii11iIi11i % oooOo0oo0oo
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 89 - 89: o0ii1I * Iii + OOooOOo / Ii
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 68 - 68: ii * Iii
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 86 - 86: I11i / OOooOOo
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . youplay ( Iii11i , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for Iii11i in IIi :
   self . Printer ( Iii11i , season_name , source_name )
   if 40 - 40: IiI1i11I
 def Printer ( self , Link , season_name , source_name ) :
  if 62 - 62: i1iIi / oooOo0oo0oo
  if Link in ii1IiIi1iIi . List :
   pass
  elif source_name in ii1IiIi1iIi . source_list :
   pass
  else :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   ii1IiIi1iIi . List . append ( Link )
   ii1IiIi1iIi . source_list . append ( source_name )
   if 74 - 74: IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i + oooOo0oo0oo
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 92 - 92: Iii % i1IiiiI1iI
   if 18 - 18: i1iIi + i1IiiiI1iI / oooOo0oo0oo / i1i1I1IIii1II + iI11I1II1I1I % III1iiIii
   if 94 - 94: Iii
   if 37 - 37: i1i1I1IIii1II
   if 52 - 52: Ii1I * oOo0O0Ooo . oooOo0oo0oo + ooOoO0O00 % i1i1I1IIii1II / iI11I1II1I1I
def i1i1iII1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 68 - 68: i1IiiiI1iI - OOooOOo . Ii + I11i
def Oo0oo ( url ) :
 iii1I = '20'
 O0OoO0o = [ ]
 o0Oo00oOOO0o = '                                                    '
 o0ii1I1 = '        '
 I1I1II1I11 ( o0Oo00oOOO0o + 'pl' + o0ii1I1 + 'w' + o0ii1I1 + 'd' + o0ii1I1 + 'l' + o0ii1I1 + 'f' + o0ii1I1 + 'a' + o0ii1I1 + 'pts' , '' , '' , '' , '' , '' )
 Oooo0O = O0oII11I ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( Oooo0O )
 for ii1oo , OOOooOOO00O , I1i1Iii1111Ii , iIIII1iII1i , Ii1IiIi1i111 , iiii111II , i11I1iIii1i11 , OoiIIi , iIII1II11iII in IIi :
  IiiII1iIi = OoO00oooo0o ( OOOooOOO00O )
  iiiiii = OoO00oooo0o ( I1i1Iii1111Ii )
  ooII1 = OoO00oooo0o ( iIIII1iII1i )
  o0OOOIiII11I1I1IIi = OoO00oooo0o ( Ii1IiIi1i111 )
  ii1i111 = OoO00oooo0o ( iiii111II )
  O0ooOOO00000O = OoO00oooo0o ( i11I1iIii1i11 )
  O0OoO0o . append ( ii1oo [ 0 ] )
  OOooOO0o = len ( O0OoO0o )
  oOO00o0 = int ( len ( o0Oo00oOOO0o ) - len ( ii1oo ) - 2 )
  if len ( O0OoO0o ) >= 10 :
   oOO00o0 = oOO00o0 - 1
  if len ( O0OoO0o ) <= int ( iii1I ) :
   Ii1I1i ( str ( OOooOO0o ) + ' ' + ii1oo + o0Oo00oOOO0o [ 0 : oOO00o0 ] + OOOooOOO00O + IiiII1iIi + I1i1Iii1111Ii + iiiiii + iIIII1iII1i + ooII1 + Ii1IiIi1i111 + o0OOOIiII11I1I1IIi + iiii111II + ii1i111 + i11I1iIii1i11 + O0ooOOO00000O + ' ' + iIII1II11iII , '' , '' , '' , '' , '' )
   if 29 - 29: IIiIiII11i - IiI1i11I / i1i1I1IIii1II % ii % IiI1i11I + III1iiIii
   if 44 - 44: o0o00Oo0O / o0o00Oo0O
def OoO00oooo0o ( space ) :
 if len ( space ) > 1 :
  OOOO00OOO00 = len ( '        ' ) - len ( space ) + 1
  space = int ( OOOO00OOO00 ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 25 - 25: I11i + iI11I1II1I1I + III1iiIii + Ii1I / i1IiiiI1iI - ooOoO0O00
def Ii1I11Ii1iI ( ) :
 if 61 - 61: I11i * Ii1I - ooOoO0O00 + Iii % I11i + ii
 if 64 - 64: IiI1i11I . i1iIi % o0ii1I
 if 21 - 21: i1IiiiI1iI / i1i1I1IIii1II
 if 82 - 82: iI11I1II1I1I - IiI1i11I . ooOoO0O00 . III1iiIii % Ii * iI11I1II1I1I
 if 58 - 58: Ii1I % Ii + OOooOOo / Iii - ii
 if 62 - 62: oO0o . OOooOOo
 if 22 - 22: i1iIi . Ii . ii . ooOoO0O00
 if 12 - 12: OOooOOo % oooOo0oo0oo + i1i1I1IIii1II . o0o00Oo0O % iI11I1II1I1I
 if 41 - 41: ii
 if 13 - 13: Iii + i1IiiiI1iI - i1IiiiI1iI % i1i1I1IIii1II / Iii
 if 4 - 4: oOo0O0Ooo + oooOo0oo0oo - III1iiIii + IiI1i11I
 if 78 - 78: o0ii1I
 if 29 - 29: IIiIiII11i
 if 79 - 79: iI11I1II1I1I - Ii + i1iIi - IIiIiII11i . iI11I1II1I1I
 if 84 - 84: I1ii11iIi11i % Iii * o0o00Oo0O * Iii
 if 66 - 66: oooOo0oo0oo / iI11I1II1I1I - OOooOOo % o0o00Oo0O . i1iIi
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
 if 37 - 37: ooOoO0O00 * Ii
 if 95 - 95: Ii % i1IiiiI1iI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / oooOo0oo0oo / i1IiiiI1iI
 if 35 - 35: IiI1i11I * oooOo0oo0oo
 if 65 - 65: IIiIiII11i % ooOoO0O00
 if 13 - 13: oO0o * i1IiiiI1iI + I1ii11iIi11i - III1iiIii
 if 31 - 31: oO0o
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - i1IiiiI1iI . Ii1I % I1ii11iIi11i . o0ii1I
 if 9 - 9: I11i
 if 55 - 55: oooOo0oo0oo % iI11I1II1I1I + Iii . i1iIi
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
 if 23 - 23: Ii
 if 88 - 88: IIiIiII11i - IiI1i11I / ii
 if 71 - 71: Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
 if 1 - 1: III1iiIii % ooOoO0O00
 if 41 - 41: oO0o * oO0o / IiI1i11I + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / o0ii1I
 if 80 - 80: Ii1I
 if 67 - 67: IIiIiII11i
 if 2 - 2: I11i - o0o00Oo0O * o0ii1I % III1iiIii
 if 64 - 64: ooOoO0O00 . i1iIi
 if 7 - 7: i1i1I1IIii1II . IiI1i11I - IiI1i11I / i1IiiiI1iI % I1ii11iIi11i
 if 61 - 61: i1i1I1IIii1II - Ii1I / IiI1i11I % Ii1I + oO0o / I1ii11iIi11i
 if 10 - 10: Ii / OOooOOo
 if 27 - 27: oOo0O0Ooo / ii
 if 74 - 74: Ii1I % i1IiiiI1iI - oO0o * Iii . ii * oO0o
 if 99 - 99: OOooOOo . IiI1i11I - ii - o0o00Oo0O
 if 6 - 6: oooOo0oo0oo
 if 3 - 3: o0o00Oo0O - i1IiiiI1iI * o0ii1I * oooOo0oo0oo / o0ii1I
 if 58 - 58: o0ii1I * iI11I1II1I1I + i1iIi . i1iIi
 if 74 - 74: i1iIi - I11i * III1iiIii % i1iIi
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * i1IiiiI1iI - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . i1i1I1IIii1II . ii . oooOo0oo0oo * Ii1I
 if 80 - 80: i1IiiiI1iI + Iii . i1IiiiI1iI + oooOo0oo0oo
 if 85 - 85: Ii . Iii + o0ii1I / o0ii1I
 if 43 - 43: III1iiIii . ii - IIiIiII11i
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * oooOo0oo0oo * i1i1I1IIii1II
 if 19 - 19: i1IiiiI1iI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
 if 15 - 15: o0ii1I + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
 if 54 - 54: III1iiIii - IIiIiII11i . i1iIi + o0ii1I
 if 45 - 45: i1i1I1IIii1II + IIiIiII11i . IiI1i11I / Ii1I
 if 76 - 76: o0ii1I + IiI1i11I - III1iiIii * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: i1iIi + IIiIiII11i . o0o00Oo0O - IiI1i11I / ii . i1IiiiI1iI
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
 if 29 - 29: Ii1I
 if 41 - 41: o0ii1I
 if 49 - 49: o0ii1I % IIiIiII11i . o0ii1I - I11i - Iii * III1iiIii
 if 47 - 47: o0o00Oo0O . I11i / o0ii1I * IiI1i11I
 if 63 - 63: i1IiiiI1iI - i1i1I1IIii1II - IiI1i11I - i1iIi / i1i1I1IIii1II + oO0o
 if 94 - 94: III1iiIii / oOo0O0Ooo . IIiIiII11i
 if 32 - 32: i1i1I1IIii1II . oooOo0oo0oo % oooOo0oo0oo . OOooOOo
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OoOOoOooooOOo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0O00oOOoooO , Oo00OOOOO , '' )
  if 37 - 37: oooOo0oo0oo + o0o00Oo0O + oooOo0oo0oo . IiI1i11I . I11i
def OoO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00O0O = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00O0O in O00O0O :
  Oo000o = re . compile ( '(.*?)</h2>' ) . findall ( str ( O00O0O ) )
  for IIiIi in Oo000o :
   IIiIi = IIiIi
  OoOOoi111II = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O00O0O ) )
  for iii1iII1I1I , oO0O00oOOoooO , time , oo00o in OoOOoi111II :
   iiIiIiIiiIiI = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oo00o )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIiIi + ' - ' + iii1iII1I1I + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oO0O00oOOoooO , Oo00OOOOO , ( str ( iiIiIiIiiIiI ) ) )
   if 14 - 14: o0ii1I + o0ii1I * ii * Iii + I1ii11iIi11i . oOo0O0Ooo
 Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if 61 - 61: oooOo0oo0oo . oooOo0oo0oo
def ii11 ( ) :
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
 if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  II1IoO0Ooo0o00o = IiIi11iI . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiIi11iI :
   pass
  else :
   II1IoO0Ooo0o00o = IiIi11iI . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + II1IoO0Ooo0o00o + '[/COLOR]' , url , 10013 , oO0O00oOOoooO )
 for url , oO0O00oOOoooO , IiIi11iI in i1Iii1i1I :
  II1IoO0Ooo0o00o = IiIi11iI . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiIi11iI :
   pass
  else :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + II1IoO0Ooo0o00o + '[/COLOR]' , url , 10013 , oO0O00oOOoooO )
def oOoOOO0oO0O ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 37 - 37: oOo0O0Ooo - iI11I1II1I1I
 if 56 - 56: III1iiIii - o0ii1I + Ii * oO0o % oOo0O0Ooo
 if 37 - 37: iI11I1II1I1I + III1iiIii / i1IiiiI1iI . ii
 if 72 - 72: i1i1I1IIii1II % i1iIi % oooOo0oo0oo
 if 63 - 63: oO0o . o0ii1I % IIiIiII11i / Iii - OOooOOo
 if 4 - 4: I1ii11iIi11i - o0o00Oo0O / Iii + o0o00Oo0O - i1i1I1IIii1II * I1ii11iIi11i
 if 25 - 25: oOo0O0Ooo
 for url , oO0O00oOOoooO , IiIi11iI in i1Iii1i1I :
  II1IoO0Ooo0o00o = IiIi11iI . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiIi11iI :
   pass
  else :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + II1IoO0Ooo0o00o + '[/COLOR]' , url , 10013 , oO0O00oOOoooO )
   if 64 - 64: i1i1I1IIii1II
def oOoOo00o00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for O00O in IIi :
  O0OOo00O = ( O00O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OO0o0oO0O000o ( 'http:' + O0OOo00O )
  if 18 - 18: i1iIi * IIiIiII11i
  if 43 - 43: I11i / o0o00Oo0O + ooOoO0O00 - Ii1I % Ii
  if 69 - 69: oooOo0oo0oo % Ii1I / OOooOOo . oooOo0oo0oo - III1iiIii
  if 74 - 74: oO0o - I11i - III1iiIii . o0o00Oo0O % i1iIi
def IIiiii1I1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , url , 8046 , oO0O00oOOoooO )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def i11II ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  OO0o0oO0O000o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 17 - 17: iI11I1II1I1I - i1iIi
def OO00O0O ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( Oooo0O )
 for url in IIi :
  yt . PlayVideo ( url )
  if 52 - 52: Ii1I
def ii1i ( ) :
 IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 Oooo0O = ooo ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oI1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( Oooo0O )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 39 - 39: i1IiiiI1iI . i1i1I1IIii1II - oooOo0oo0oo
  if 56 - 56: I1ii11iIi11i + o0o00Oo0O . I1ii11iIi11i / IIiIiII11i % i1IiiiI1iI
def IIIiIiII11Iii ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( Oooo0O )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def O0oo0o0OoO0 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , '' )
  if 95 - 95: oO0o - Ii . oO0o % oooOo0oo0oo * o0o00Oo0O + Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooo00 ( name , url ) :
 iIiI1I1IIi1 = 0
 name = name
 url = url
 iI111iIIii = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  ooOoO00 ( url )
  if 77 - 77: IIiIiII11i - I11i . Ii1I
  if 63 - 63: i1i1I1IIii1II
  if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
  if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
  if 60 - 60: i1IiiiI1iI
  if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
  if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
  if 14 - 14: o0ii1I - o0o00Oo0O
def OoOO0Ooo ( ) :
 Oooo0O = ooo ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  if 'genre' in OoOOoOooooOOo :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , OoOOoOooooOOo , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO000o0oo ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( Oooo0O )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 83 - 83: OOooOOo / oOo0O0Ooo * o0ii1I
def I1I ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( Oooo0O )
 for url in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  O0oo0o0OoO0 ( url )
  if 84 - 84: Iii . I1ii11iIi11i . III1iiIii * i1iIi + OOooOOo
def iIiiIi11iiI1 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0oO0o = 'http://documentarylovers.com/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 III111i11IiI = OO0oO0o . lower ( )
 oO000o0oo ( III111i11IiI )
 if 82 - 82: Iii % ooOoO0O00
def i111II ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if 'films' in url :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def i11iI1I1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( Oooo0O )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  if 'films' in url :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oO0O00oOOoooO )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def oooo00o00oO ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( Oooo0O )
 for url in IIi :
  if 'rtd' in url :
   iIii11iI1Iii1iI ( url )
   if 47 - 47: III1iiIii - iI11I1II1I1I + i1iIi / o0ii1I
def iIii11iI1Iii1iI ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( Oooo0O )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  ooOoO00 ( url )
  if 42 - 42: o0ii1I * iI11I1II1I1I - IiI1i11I + o0o00Oo0O % i1IiiiI1iI
  if 73 - 73: IIiIiII11i
def iIiiIi11 ( ) :
 II11iIiIIIiI = ooo ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , I1IiIiI in IIi :
  IIi1i1IiIIi1i ( ( IiIi11iI + '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '[/COLOR]' ) , OoOOoOooooOOo , 8086 , oO0O00oOOoooO )
  if 73 - 73: III1iiIii - III1iiIii / ii
def oOoOo ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 8087 , oO0O00oOOoooO )
  if 55 - 55: III1iiIii * I11i * i1iIi - ooOoO0O00 / o0ii1I * i1i1I1IIii1II
def ooOiiIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  ii1I ( url , IiIi11iI )
  if 55 - 55: iI11I1II1I1I % OOooOOo
def ii1I ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 70 - 70: i1i1I1IIii1II - o0o00Oo0O * iI11I1II1I1I . i1IiiiI1iI % o0o00Oo0O
def oo00oo0 ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OoOOoOooooOOo , 3002 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def i11iiiiiIi1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def OoIiii1i11I1iII ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 iI111II11IIii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( Oooo0O )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , IiIi11iI in iI111II11IIii :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']Season- ' + IiIi11iI + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , oO0O00oOOoooO , IiIi11iI in i1Iii1i1I :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oO0O00oOOoooO )
def oOO0o0OoO00OO00 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( Oooo0O )
 for url in IIi :
  I111II11I ( url )
def I111II11I ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( Oooo0O )
 for url in IIi :
  ooOoO00 ( url )
  if 76 - 76: Ii1I + iI11I1II1I1I
def OOoo ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoOOoOooooOOo , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def i1OOO00oO0O ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( Oooo0O )
 for url in IIi :
  Ii11iIII ( url )
  if 5 - 5: OOooOOo / oooOo0oo0oo / i1iIi % Ii1I - IIiIiII11i
def O0Oo0o000oO ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoOOoOooooOOo , 8065 , iiIi1IIiIi + 'classictv.png' )
def OooOO0 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  if 'mp4' in url :
   ooOoO00 ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 16 - 16: i1i1I1IIii1II / IiI1i11I
def ii1iiI ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OoOOoOooooOOo , 8071 , iiIi1IIiIi + 'streams.png' )
def i11ioo0oo0O0Oo0O ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11iI , url in IIi :
  if '(Free Access)' in IiIi11iI :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def Oo0o ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , oO0O00oOOoooO , i11I , '' )
  if 40 - 40: i1IiiiI1iI . IIiIiII11i
def iiiiiiiiiiIi ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  OO00O0O00oOOO ( 'http://watchxxxfree.com/categories' )
 if O0oO == 1 :
  ii1111iIIiIIi ( 'http://www.perfectgirls.net' )
 if O0oO == 2 :
  ooOo0Oo ( 'http://www.xvideos.com/best' )
 if O0oO == 3 :
  I11i1I111II1IiI ( 'http://www.xvideos.com/best' )
 if O0oO == 4 :
  ooOo0Oo ( 'http://www.xvideos.com/best' )
 if O0oO == 5 :
  ooOo0Oo ( 'http://www.xvideos.com/verified/videos' )
 if O0oO == 6 :
  oo00O0oOo ( 'http://www.xvideos.com/tags' )
 if O0oO == 7 :
  IiI1Ii ( 'http://www.xvideos.com/porn' )
 if O0oO == 8 :
  oOO00o0oooOo0 ( )
  if 17 - 17: Ii1I
  if 62 - 62: IiI1i11I - oooOo0oo0oo / IIiIiII11i . IIiIiII11i
  if 49 - 49: iI11I1II1I1I / Iii
  if 53 - 53: oO0o
  if 96 - 96: ii - iI11I1II1I1I . i1i1I1IIii1II
  if 2 - 2: ooOoO0O00
  if 6 - 6: ooOoO0O00 % Iii . III1iiIii + III1iiIii . Iii / Ii
  if 78 - 78: o0o00Oo0O
  if 34 - 34: IIiIiII11i
def II1i1II1iIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  if 'ch' in url :
   oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def iIIOOOO0o0Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIiI1iiI = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for IiIi11iI , url in I1iIiI1iiI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def oO000O00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   IiIIIii1iIII1 ( url )
def OoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def OO00O0O00oOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI , OOOO00OOO00 in IIi :
  if 'category' in url :
   oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORorange]   ' + OOOO00OOO00 + '[/COLOR]' , url , 90006 , oO0O00oOOoooO , iiIi1IIiIi + 'Jizbox.png' , '' )
def oooo0oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIiI1iiI = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oO0O00oOOoooO , '' , '' )
 for url in I1iIiI1iiI :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def ii1II1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   IiIIIii1iIII1 ( url )
def IiIIIii1iIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def ii1111iIIiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , OOOO00OOO00 in IIi :
  if 'category' in url :
   oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORorange]' + OOOO00OOO00 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def i1I1II11I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0000 = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIiI1iiI = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oO0O00oOOoooO , '' , '' )
 for url in I1iIiI1iiI :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , O0000 + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def oo0oOoOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0oOoOooo00oo ( 'http://www.perfectgirls.net' + url )
def O0oOoOooo00oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OO0o0oO0O000o ( 'http://' + url )
def IiI1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , OOOO00OOO00 in IIi :
  oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgreen] - No of Videos : [COLORorange]' + OOOO00OOO00 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oo00O0oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIiI1iiI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in I1iIiI1iiI :
  oOo0Oo0Oo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , OOOO00OOO00 in IIi :
  oOo0Oo0Oo0 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgreen] - No of Videos : [COLORorange]' + ( OOOO00OOO00 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 84 - 84: oO0o - Iii + OOooOOo + i1IiiiI1iI % IIiIiII11i - oOo0O0Ooo
def I1i11I1IiII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIiI1iiI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in I1iIiI1iiI :
  oOo0Oo0Oo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI , ii1iI11IiIIi in IIi :
  oOo0Oo0Oo0 ( IiIi11iI + '--' + ( ii1iI11IiIIi ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oO0O00oOOoooO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + i1IiiiI1iI
  if 58 - 58: i1IiiiI1iI * o0o00Oo0O / o0ii1I + oOo0O0Ooo - Ii1I * I1ii11iIi11i
def ooOo0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , url , IiIi11iI , I1iIIIIIi , ooO0oO00oO0o in IIi :
  oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgreen] - Porn Quality : [COLORorange]' + ooO0oO00oO0o + ' - [COLORred]' + I1iIIIIIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oO0O00oOOoooO , oO0O00oOOoooO , ooO0oO00oO0o + ' - ' + I1iIIIIIi )
 OOo000ooo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in OOo000ooo :
  oOo0Oo0Oo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 72 - 72: Ii1I
def I11i1I111II1IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00O0O = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIiI1iiI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in I1iIiI1iiI :
  oOo0Oo0Oo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O00O0O ) )
 for url , IiIi11iI in IIi :
  if '/c/' in url :
   oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 23 - 23: i1iIi / Ii % oooOo0oo0oo - i1IiiiI1iI . IiI1i11I
   if 92 - 92: iI11I1II1I1I
def oOO00o0oooOo0 ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i = ( OO0oOOo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 III111i11IiI = I1i . lower ( )
 OO0OOoooOo00 = 'http://www.xvideos.com/?k=' + III111i11IiI
 print OO0OOoooOo00 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( OO0OOoooOo00 )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , OoOOoOooooOOo , IiIi11iI , I1iIIIIIi , ooO0oO00oO0o in IIi :
  oOo0Oo0Oo0 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgreen] - Porn Quality : [COLORorange]' + ooO0oO00oO0o + ' - [COLORred]' + I1iIIIIIi + '[/COLOR]' , 'http://www.xvideos.com' + OoOOoOooooOOo , 10108 , oO0O00oOOoooO , oO0O00oOOoooO , ooO0oO00oO0o + ' - ' + I1iIIIIIi )
 OOo000ooo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo in OOo000ooo :
  oOo0Oo0Oo0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OoOOoOooooOOo , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 16 - 16: IIiIiII11i * oO0o * i1IiiiI1iI
if 80 - 80: oooOo0oo0oo * oooOo0oo0oo
if 5 - 5: ii - IiI1i11I - Ii
if 53 - 53: IiI1i11I * oO0o / Ii1I + oOo0O0Ooo + ii
if 47 - 47: i1IiiiI1iI
if 65 - 65: o0ii1I
if 71 - 71: i1IiiiI1iI % i1IiiiI1iI . i1i1I1IIii1II + Ii - Ii
if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / i1IiiiI1iI - Ii . i1iIi / oooOo0oo0oo
if 13 - 13: I11i % o0o00Oo0O - i1IiiiI1iI * ii / I1ii11iIi11i - ii
if 78 - 78: i1i1I1IIii1II % ii
if 73 - 73: oOo0O0Ooo % i1iIi % III1iiIii + ooOoO0O00 - ii / i1i1I1IIii1II
if 78 - 78: ii % i1i1I1IIii1II - Ii
if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
if 23 - 23: i1iIi - o0o00Oo0O + Ii
if 98 - 98: ii
if 61 - 61: I11i . III1iiIii . o0o00Oo0O + ii + o0o00Oo0O
if 65 - 65: ooOoO0O00 * oooOo0oo0oo * ii - III1iiIii . IiI1i11I - oO0o
if 71 - 71: o0ii1I * OOooOOo
if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % i1IiiiI1iI * I11i
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
def oo0i11Iiiiii11II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 Iiii1iI1i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in Iiii1iI1i :
  if 'http' in url :
   oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 100 - 100: i1IiiiI1iI + Iii + oO0o . Ii1I
def iIIII11i1 ( url ) :
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 import urlresolver
 try : iII . play ( url )
 except : pass
 if 39 - 39: Ii % Ii * oO0o
 if 36 - 36: Ii + i1iIi % i1i1I1IIii1II - oO0o * iI11I1II1I1I
def O0oI1iIiiIii ( ) :
 if 99 - 99: i1IiiiI1iI - Ii1I - oOo0O0Ooo - i1IiiiI1iI + oO0o + IIiIiII11i
 if 34 - 34: i1IiiiI1iI * Iii
 if 31 - 31: III1iiIii . i1i1I1IIii1II
 if 40 - 40: o0ii1I - Iii / IIiIiII11i * ooOoO0O00 + III1iiIii * IIiIiII11i
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - i1IiiiI1iI
 if 99 - 99: o0ii1I - III1iiIii - ooOoO0O00 / Ii . III1iiIii
 if 58 - 58: oooOo0oo0oo
 if 12 - 12: oOo0O0Ooo . I11i * ii
 if 64 - 64: OOooOOo + III1iiIii - ooOoO0O00 . IIiIiII11i . oO0o
 if 31 - 31: i1i1I1IIii1II . IiI1i11I - Iii . iI11I1II1I1I + Iii . OOooOOo
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 8091 , iiIi1IIiIi + 'gofish.png' )
def OOoOO00O ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 8092 , oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def II1iIiiiIiiII ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0o0 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO in o0o0 :
  oO0O00oOOoooO = oO0O00oOOoooO
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 8092 , oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - oooOo0oo0oo
def o0o00O00Oo0 ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 96 - 96: IiI1i11I
  if 9 - 9: III1iiIii + IIiIiII11i . oOo0O0Ooo * IiI1i11I
  if 6 - 6: IiI1i11I % i1IiiiI1iI
  if 17 - 17: IIiIiII11i - ii + Iii % o0ii1I % ii
IiiiI1i1i = '{PQ},' ; ii11II1 = '{SC},' ; IIIoooOo0ooO00o = '{XG},' ; i1iII11111iIi = '{JP},' ; I1i11 = '{HW},' ; oO0o0O0ooo0O = '{RT},'
def oo00O00oO000o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OOOii1i1iiI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 OoOOoOooooOOo = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 O0000 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 Oo0oOo0ooOOOo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO0000o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 o0Ii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IIi1IiII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0IIIIiI11I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OO0oOOo
 iiiI11iIIi1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 o00OoooooooOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 87 - 87: I1ii11iIi11i . I11i - ii * i1i1I1IIii1II % III1iiIii + o0o00Oo0O
 iIi = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 Ii1Ii11IiI1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 16 - 16: Ii1I % I1ii11iIi11i % IIiIiII11i % IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( O0000 )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 Ii11I1iIiiI = O00O0oOO00O00 ( O0000 )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( Oo0oOo0ooOOOo )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( OoO0000o )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 O0o0OO00 = O00O0oOO00O00 ( o00OoooooooOo )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 51 - 51: OOooOOo * OOooOOo - o0o00Oo0O % iI11I1II1I1I / o0o00Oo0O
 if 5 - 5: Ii * i1iIi % IiI1i11I - Iii
 if 5 - 5: o0o00Oo0O * III1iiIii * oooOo0oo0oo + i1IiiiI1iI % I1ii11iIi11i - Ii1I
 if 62 - 62: Ii1I + Iii
 if 90 - 90: iI11I1II1I1I
 if 18 - 18: Iii * Ii1I / Ii / iI11I1II1I1I * ii . oooOo0oo0oo
 if 69 - 69: I1ii11iIi11i * i1iIi
 if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
 ooOO0ooo0o = O00O0oOO00O00 ( Ii1Ii11IiI1I1 )
 if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
 if O0o0OO00 != 'Failed' :
  i1I1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0o0OO00 )
  for OoOOoOooooOOo , IiIi11iI in i1I1i :
   IIII1iIIii = O00O0oOO00O00 ( OoOOoOooooOOo )
   IiiOooooOo0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIII1iIIii )
   for I1ii1 , I1IiIiI in IiiOooooOo0 :
    I1IiIiI = ( I1IiIiI . replace ( '.' , ' ' ) )
    if III111i11IiI in I1IiIiI . lower ( ) :
     if '.mkv' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 222 , '' , '' , '' )
     elif '.mp4' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 222 , '' , '' , '' )
     elif '.avi' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 222 , '' , '' , '' )
     elif '.wav' in I1ii1 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 38 - 38: i1i1I1IIii1II + ii * OOooOOo % i1i1I1IIii1II
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i1Iii1i1I :
   if OO0oOOo in IiIi11iI . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORred] source Technica[/COLOR]' ) , OoOOoOooooOOo , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 24 - 24: OOooOOo * o0ii1I
 if o00OooOO000 != 'Failed' :
  Iiii1iI1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for IIIIIIi1i , IiIi11iI in Iiii1iI1i :
   if OO0oOOo in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Oo0oOo0ooOOOo + IIIIIIi1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in OOoOooOoOOOoo :
   if OO0oOOo in IiIi11iI . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORred] source RaizTv[/COLOR]' ) , OoOOoOooooOOo , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 81 - 81: oooOo0oo0oo
    if 58 - 58: IIiIiII11i . i1IiiiI1iI . o0ii1I * ii / o0ii1I / Iii
    if 41 - 41: Iii + oO0o . IiI1i11I
    if 73 - 73: Ii * oOo0O0Ooo + I11i / i1i1I1IIii1II
    if 56 - 56: ooOoO0O00
    if 11 - 11: Ii % I11i / Iii * ii
    if 82 - 82: III1iiIii
    if 10 - 10: I1ii11iIi11i % oooOo0oo0oo / Iii * III1iiIii - I11i
    if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / IiI1i11I
    if 1 - 1: i1IiiiI1iI / OOooOOo * OOooOOo - I11i % o0ii1I
    if 96 - 96: III1iiIii / o0ii1I % oO0o . iI11I1II1I1I
    if 30 - 30: Iii - oO0o
    if 15 - 15: ii
    if 31 - 31: IIiIiII11i
    if 62 - 62: iI11I1II1I1I % i1IiiiI1iI % Ii1I * III1iiIii
    if 87 - 87: III1iiIii
    if 45 - 45: i1i1I1IIii1II + IIiIiII11i * o0o00Oo0O % oooOo0oo0oo . iI11I1II1I1I
    if 55 - 55: III1iiIii
    if 43 - 43: oooOo0oo0oo
    if 17 - 17: Ii
    if 94 - 94: ii - III1iiIii + i1i1I1IIii1II . ii / ooOoO0O00
    if 53 - 53: i1IiiiI1iI % Ii1I
    if 17 - 17: ii % o0ii1I % o0o00Oo0O
    if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
    if 89 - 89: III1iiIii - III1iiIii % IiI1i11I / Iii + i1i1I1IIii1II - III1iiIii
    if 97 - 97: o0ii1I % OOooOOo / Ii1I / iI11I1II1I1I * ii * oooOo0oo0oo
    if 80 - 80: i1i1I1IIii1II / o0o00Oo0O
    if 55 - 55: oOo0O0Ooo * Iii / o0o00Oo0O % OOooOOo
    if 71 - 71: Ii * OOooOOo * oooOo0oo0oo + i1i1I1IIii1II + I1ii11iIi11i
    if 59 - 59: III1iiIii
    if 54 - 54: oooOo0oo0oo
    if 27 - 27: OOooOOo - oO0o + I11i + i1iIi . oO0o
    if 86 - 86: IIiIiII11i - ii - i1iIi % IiI1i11I
    if 16 - 16: i1iIi + I1ii11iIi11i + ii
    if 87 - 87: oOo0O0Ooo . i1i1I1IIii1II / III1iiIii - ii
    if 33 - 33: i1i1I1IIii1II % oO0o . iI11I1II1I1I / III1iiIii
    if 3 - 3: o0ii1I + oO0o
    if 60 - 60: oO0o . OOooOOo - Ii1I - oOo0O0Ooo - IIiIiII11i % I1ii11iIi11i
    if 62 - 62: o0o00Oo0O + IiI1i11I - IiI1i11I % iI11I1II1I1I
    if 47 - 47: i1IiiiI1iI + oOo0O0Ooo
 O00OOo0oOOooO0o0O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 40 - 40: iI11I1II1I1I % o0ii1I + IIiIiII11i - oOo0O0Ooo
 for ii1ii in O00OOo0oOOooO0o0O :
  IIiI1i = oO0 + ii1ii + oOoOooOo0o0
  O0o0OO00 = O00O0oOO00O00 ( IIiI1i )
  if O0o0OO00 != 'Failed' :
   i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0OO00 )
   for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i1I1i :
    if OO0oOOo in IiIi11iI . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] - Source Pandoras[/COLOR]' , OoOOoOooooOOo , 222 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 80 - 80: i1i1I1IIii1II
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 81 - 81: ii / i1iIi * iI11I1II1I1I . I1ii11iIi11i + i1i1I1IIii1II / o0o00Oo0O
 O00OOo0oOOooO0o0O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 84 - 84: IIiIiII11i - I11i
 if 78 - 78: III1iiIii
 for ii1ii in O00OOo0oOOooO0o0O :
  IIiI1i = OOOii1i1iiI + ii1ii
  O0O0ooOoOO0OO = O00O0oOO00O00 ( IIiI1i )
  if O0O0ooOoOO0OO != 'Failed' :
   I1iiIiiii1111 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0O0ooOoOO0OO )
   for IIIIIIi1i , IiIi11iI in I1iiIiiii1111 :
    if OO0oOOo in IiIi11iI . lower ( ) :
     oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOOii1i1iiI + ii1ii + IIIIIIi1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 58 - 58: Ii - OOooOOo
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: Ii1I / IiI1i11I + iI11I1II1I1I % oOo0O0Ooo
def OoOOOo0o0ooo ( ) :
 if 99 - 99: i1iIi . o0ii1I
 if 92 - 92: ooOoO0O00
 if 68 - 68: oO0o % III1iiIii - i1i1I1IIii1II - i1iIi . I1ii11iIi11i
 if 30 - 30: ii % I11i + i1iIi * oO0o
 if 57 - 57: Iii + iI11I1II1I1I . oO0o + i1i1I1IIii1II
 if 4 - 4: o0ii1I
 if 43 - 43: ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii - oooOo0oo0oo + i1iIi
 if 56 - 56: I1ii11iIi11i % Ii / o0ii1I . i1IiiiI1iI . oO0o - OOooOOo
 if 32 - 32: i1IiiiI1iI / i1i1I1IIii1II / oOo0O0Ooo
 if 22 - 22: oO0o - OOooOOo . I1ii11iIi11i + I11i
 if 69 - 69: i1i1I1IIii1II - oOo0O0Ooo
 if 10 - 10: ooOoO0O00 / IiI1i11I . IIiIiII11i * ooOoO0O00 % ii
 if 83 - 83: Iii . oooOo0oo0oo + i1IiiiI1iI * Iii . i1IiiiI1iI + i1i1I1IIii1II
 if 64 - 64: o0ii1I . I11i - ooOoO0O00
 if 35 - 35: Ii1I % ii
 if 59 - 59: oOo0O0Ooo % Iii
 if 32 - 32: oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 if 34 - 34: III1iiIii
 if 5 - 5: oO0o . oOo0O0Ooo
 I1ii1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OO0oOOo ) . replace ( ' ' , '+' )
 O0000 = 'http://onlinemovies.tube/?s=' + ( OO0oOOo ) . replace ( ' ' , '+' )
 Oo0oOo0ooOOOo = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OoO0000o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 IIi1IiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 48 - 48: I1ii11iIi11i - oO0o . Iii - iI11I1II1I1I % o0ii1I
 iiiI11iIIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 o00OoooooooOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 47 - 47: IiI1i11I / ii - IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 91 - 91: OOooOOo + I11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 23 - 23: ooOoO0O00
 if 9 - 9: ooOoO0O00 % i1IiiiI1iI - oO0o * OOooOOo . I11i
 OOOiII1 = O00O0oOO00O00 ( I1ii1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( O0000 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( Oo0oOo0ooOOOo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO0000o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 O0O0ooOoOO0OO = O00O0oOO00O00 ( IIi1IiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 18 - 18: o0ii1I . OOooOOo + IiI1i11I . oOo0O0Ooo + ii . oO0o
 if 31 - 31: i1IiiiI1iI - Iii
 Ii11I1iIiiI = O00O0oOO00O00 ( iiiI11iIIi1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0o0OO00 = O00O0oOO00O00 ( o00OoooooooOo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 49 - 49: iI11I1II1I1I - iI11I1II1I1I - OOooOOo + III1iiIii / OOooOOo
 if 74 - 74: ii + Ii1I % o0o00Oo0O
 if O0o0OO00 != 'Failed' :
  i1I1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0o0OO00 )
  for OoOOoOooooOOo , IiIi11iI in i1I1i :
   IIII1iIIii = O00O0oOO00O00 ( OoOOoOooooOOo )
   IiiOooooOo0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIII1iIIii )
   for I1ii1 , I1IiIiI in IiiOooooOo0 :
    if III111i11IiI in I1IiIiI . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + I1IiIiI + '-[COLORgold] source ' + IiIi11iI + '[/COLOR]' ) , OoOOoOooooOOo + I1ii1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 32 - 32: Ii1I + Ii1I
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if Ii11I1iIiiI != 'Failed' :
  i11IiI1iiI11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii11I1iIiiI )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in i11IiI1iiI11 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] source HeroVision[/COLOR]' ) , OoOOoOooooOOo , 1016 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 89 - 89: i1iIi + i1i1I1IIii1II + o0ii1I - oooOo0oo0oo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 12 - 12: OOooOOo - I11i - i1IiiiI1iI / Iii
    if 17 - 17: oO0o - i1IiiiI1iI - IIiIiII11i / i1IiiiI1iI / o0ii1I
    if 30 - 30: oooOo0oo0oo * Ii1I % Ii1I + IiI1i11I * III1iiIii
    if 33 - 33: I11i + Iii * o0o00Oo0O * oO0o . Ii1I
    if 74 - 74: IiI1i11I * IiI1i11I * I11i / i1i1I1IIii1II
    if 91 - 91: Ii . Ii1I / IIiIiII11i
    if 97 - 97: o0ii1I % ooOoO0O00 % III1iiIii + I1ii11iIi11i - o0o00Oo0O - Iii
    if 64 - 64: o0ii1I - IiI1i11I
    if 12 - 12: ooOoO0O00
    if 99 - 99: IIiIiII11i - Ii1I * III1iiIii
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  Oooo00 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , iii1II1iI1IIi in i1Iii1i1I :
   if III111i11IiI in IiIi11iI . lower ( ) :
    if 'season' in iii1II1iI1IIi :
     IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoOOoOooooOOo , 90054 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
    if 'episodes' in iii1II1iI1IIi :
     IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoOOoOooooOOo , 90044 , oO0O00oOOoooO , oO0O00oOOoooO , '' )
  for OoOOoOooooOOo in Oooo00 :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , OoOOoOooooOOo , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 3 - 3: III1iiIii - Ii1I * IiI1i11I * Ii1I + I1ii11iIi11i
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOOiII1 != 'Failed' :
  I1III1II1I11 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOOiII1 )
  for OoOOoOooooOOo , IiIi11iI , oO0O00oOOoooO in I1III1II1I11 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( IiIi11iI ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , OoOOoOooooOOo , 8022 , oO0O00oOOoooO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 15 - 15: Ii1I * o0ii1I / IiI1i11I . I11i / o0ii1I % OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
    if 96 - 96: i1iIi * i1i1I1IIii1II / iI11I1II1I1I / Iii
    if 5 - 5: I11i
    if 83 - 83: Iii * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
    if 35 - 35: OOooOOo % oO0o + o0o00Oo0O * I11i % Ii1I
    if 57 - 57: i1i1I1IIii1II / Iii
    if 63 - 63: i1iIi * oO0o * i1iIi + OOooOOo
    if 25 - 25: IiI1i11I * OOooOOo / oOo0O0Ooo / III1iiIii
    if 11 - 11: oooOo0oo0oo + Ii
 if o00OooOO000 != 'Failed' :
  Iiii1iI1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for IiIi11iI in Iiii1iI1i :
   if III111i11IiI in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( Oo0oOo0ooOOOo + IiIi11iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 14 - 14: OOooOOo / III1iiIii + oO0o - o0ii1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for IiIi11iI in OOoOooOoOOOoo :
   if III111i11IiI in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OoO0000o + IiIi11iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 38 - 38: i1IiiiI1iI
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if O0O0ooOoOO0OO != 'Failed' :
  I1iiIiiii1111 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0O0ooOoOO0OO )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in I1iiIiiii1111 :
   if III111i11IiI in IiIi11iI . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '-[COLORgold] Source Scooby[/COLOR]' ) , OoOOoOooooOOo , 1016 , i1oOOoo0o0OOOO , I11iiii1I , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 30 - 30: IIiIiII11i + Iii . Ii + iI11I1II1I1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 100 - 100: i1i1I1IIii1II * I11i / IiI1i11I
 o0oOo00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii1ii in o0oOo00 :
  IIiI1i = oO0 + ii1ii + oOoOooOo0o0
  iiii1i1II1 = O00O0oOO00O00 ( IIiI1i )
  if iiii1i1II1 != 'Failed' :
   O0o0oo0oOO0oO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iiii1i1II1 )
   for IiIi11iI , o00O0O , OoOOoOooooOOo , oO0O00oOOoooO , i11I , oo0oOO00oO in O0o0oo0oOO0oO :
    if III111i11IiI in IiIi11iI . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] - Source Pandoras[/COLOR]' , OoOOoOooooOOo , oo0oOO00oO , oO0O00oOOoooO , i11I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 92 - 92: i1iIi / Ii * oooOo0oo0oo
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 55 - 55: i1iIi
     if 1 - 1: oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiI1IIII ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOOoOooooOOo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( OO0oOOo ) . replace ( ' ' , '+' )
 if 80 - 80: Ii1I - OOooOOo . o0ii1I / III1iiIii * oooOo0oo0oo - Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( OoOOoOooooOOo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 18 - 18: IIiIiII11i % OOooOOo - oOo0O0Ooo / i1iIi
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OoOOoOooooOOo , IiIi11iI in i1Iii1i1I :
   if OO0oOOo in IiIi11iI . lower ( ) :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + OoOOoOooooOOo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 12 - 12: o0ii1I % III1iiIii - OOooOOo . III1iiIii + Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
O0000000oooOO = '{ZH},' ; iI11iiI1 = '{IX},' ; I1Ioo000oooooooO = '{LM},'
if 18 - 18: i1i1I1IIii1II * I1ii11iIi11i % Ii + o0o00Oo0O % oooOo0oo0oo . oooOo0oo0oo
def ooO00OoO ( url ) :
 oo0OOO0O0 = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oo0OOO0O0 )
 for url , o0oOOoOOO , iiI1i11II , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( o0oOOoOOO ) . replace ( 'Sezon' , ' Season ' ) + ( iiI1i11II ) . replace ( 'Bölüm' , ' Episode ' ) + IiIi11iI , url , 8063 , '' )
  if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . III1iiIii / i1i1I1IIii1II
  if 22 - 22: IiI1i11I . ii . I1ii11iIi11i
  if 44 - 44: OOooOOo / I1ii11iIi11i . ii % ii * Ii
  if 60 - 60: III1iiIii / iI11I1II1I1I + ii - Ii1I * Ii
def Iii1iIIi1iIii ( url ) :
 oo0OOO0O0 = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oo0OOO0O0 )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , url , 222 , '' )
  if 55 - 55: I11i . oooOo0oo0oo * OOooOOo
  if 19 - 19: IiI1i11I
  if 32 - 32: Iii % i1iIi % ii . i1iIi % Ii + IIiIiII11i
  if 25 - 25: i1iIi
def O00oo ( ) :
 if 65 - 65: oOo0O0Ooo
 oo0OOO0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oo0OOO0O0 )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI , iiI1i11II in IIi :
  IIi1i1IiIIi1i ( IiIi11iI + '  -  ' + ( iiI1i11II ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoOOoOooooOOo , 8063 , oO0O00oOOoooO )
  if 22 - 22: iI11I1II1I1I % i1IiiiI1iI % Ii1I % oOo0O0Ooo
def OoOooOO ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI , oO0O00oOOoooO in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 8002 , oO0O00oOOoooO )
def IiI11i1 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( Oooo0O )
 for oO0O00oOOoooO , time , url , IiIi11iI , Oo0O in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , time ) , url , 1015 , oO0O00oOOoooO , Oo0O )
  if 14 - 14: I1ii11iIi11i % iI11I1II1I1I - iI11I1II1I1I . iI11I1II1I1I - I11i * i1IiiiI1iI
def II1iIIII ( ) :
 if 43 - 43: oooOo0oo0oo * OOooOOo . i1IiiiI1iI * IIiIiII11i - Ii + Iii
 IIi1i1IiIIi1i ( 'Coronation Street' , '' , 8001 , '' )
 IIi1i1IiIIi1i ( 'Eastenders' , '' , 8002 , '' )
 IIi1i1IiIIi1i ( 'Emmerdale' , '' , 8003 , '' )
 IIi1i1IiIIi1i ( 'Hollyoaks' , '' , 8004 , '' )
 IIi1i1IiIIi1i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 44 - 44: i1iIi * Ii . IiI1i11I / iI11I1II1I1I
 if 44 - 44: oO0o
 if 74 - 74: o0ii1I * ooOoO0O00 * Iii - ii . oOo0O0Ooo
 if 24 - 24: IIiIiII11i - Ii * ooOoO0O00 . i1iIi
def i1ii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Holly' in IiIi11iI :
   oO0O00oOOoooO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoOOoOooooOOo . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 17 - 17: i1IiiiI1iI + Ii . Ii * ooOoO0O00 / o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 2 - 2: IIiIiII11i / oO0o % iI11I1II1I1I / Ii
def O0oo0o00O0O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'East' in IiIi11iI :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoOOoOooooOOo . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 83 - 83: OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: I11i - Iii % i1i1I1IIii1II % I11i + Iii
def I11IIiii111I1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Emmer' in IiIi11iI :
   oO0O00oOOoooO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoOOoOooooOOo . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 25 - 25: o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: o0o00Oo0O . oOo0O0Ooo * Ii1I - IIiIiII11i + o0ii1I - i1iIi
def Ii1i ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Coro' in IiIi11iI :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoOOoOooooOOo . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 37 - 37: oO0o / Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: IIiIiII11i - Iii - oO0o * o0o00Oo0O . iI11I1II1I1I . III1iiIii
def OOoO0OOO00 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Celeb' in IiIi11iI :
   oO0O00oOOoooO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OoOOoOooooOOo :
    oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoOOoOooooOOo . replace ( '\\/' , '/' ) , 8006 , oO0O00oOOoooO )
   else :
    pass
    if 15 - 15: I11i . o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . i1i1I1IIii1II * ii
def I1iii1IiI11I11I ( name , url ) :
 IiiIiiIiiIII = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiiIiiIiiIII :
  Ii1i11IIiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  Oooo0O = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( Oooo0O ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  Oooo0O = open_url ( url )
  III1i1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( Oooo0O ) [ - 1 ]
  Ii1i11IIiI = III1i1 . replace ( '\\/' , '/' )
 i1iiIIIi = xbmcgui . ListItem ( name , '' , '' )
 i1iiIIIi . setPath ( Ii1i11IIiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iiIIIi )
 if 90 - 90: oOo0O0Ooo % i1iIi % ii / oO0o . III1iiIii * IIiIiII11i
 if 83 - 83: i1i1I1IIii1II
def i1Ii1Ii ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OoOOoOooooOOo , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for OoOOoOooooOOo , IiIi11iI in i1Iii1i1I :
  IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OoOOoOooooOOo , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 24 - 24: OOooOOo + ii + o0ii1I * Iii
def iI1I11II1Iii1 ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Movies' in IiIi11iI :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.snagfilms.com' + ( OoOOoOooooOOo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def O00O0oO ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oO0O00oOOoooO )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 48 - 48: Ii1I - I1ii11iIi11i - i1iIi . I11i . I11i
  if 49 - 49: ooOoO0O00 . III1iiIii
def iIi1 ( url ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url , oO0O00oOOoooO in IIi :
  if '{{' in IiIi11iI :
   pass
  else :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oO0O00oOOoooO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
oO0OoiIi1IIIi1Ii = '{UJ},' ; Ii1IiIIIi1i = '{WE},' ; II111Ii1I1I = '{WP},' ; o00oo0oOo0o0 = '{PP},'
def i1Ii1 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url , oO0O00oOOoooO in IIi :
  if '{{' in IiIi11iI :
   pass
  else :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oO0O00oOOoooO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1I1ii1iI1 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  OoI1Ii ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoI1Ii ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: Ii1I % oooOo0oo0oo + o0ii1I + i1i1I1IIii1II . I1ii11iIi11i
 if 93 - 93: oooOo0oo0oo * o0ii1I - I11i . i1i1I1IIii1II . IiI1i11I
 if 64 - 64: I1ii11iIi11i / iI11I1II1I1I . oO0o / I11i / Iii
def I11IiiI1 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if '(cooltvseries.com)' in IiIi11iI :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , IiIi11iI in i1Iii1i1I :
  if '(cooltvseries.com)' in IiIi11iI :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def ooo0oO0o000O0 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( Oooo0O )
 for url in IIi :
  OO0o0oO0O000o ( ( url ) . replace ( ' ' , '%20' ) )
iiIi11i1I1 = '{XX},' ; o0OoO0 = '{UD},' ; I11Ii1I1I = '{YT},' ; oo00OO0o0 = '{JS},' ; o0oo0000Oo = '{PF},'
if 93 - 93: i1iIi + i1iIi
def Oo000O0Oo0Oo ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI , oO0O00oOOoooO in IIi :
  oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( OoOOoOooooOOo ) ) , 222 , oO0O00oOOoooO )
  if 2 - 2: i1i1I1IIii1II % IiI1i11I % ooOoO0O00 / I1ii11iIi11i . OOooOOo . I1ii11iIi11i
def oooo ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( Oooo0O )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( Oooo0O )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  if 'youtu' in url :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 81 - 81: IIiIiII11i + ooOoO0O00 % i1IiiiI1iI % III1iiIii
def Ii1oo0O0OO ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 96 - 96: oOo0O0Ooo / Iii
def ooOO0oO0 ( url ) :
 Oooo0O = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 222 , oO0O00oOOoooO )
  if 50 - 50: I1ii11iIi11i
  if 16 - 16: o0ii1I - OOooOOo % I1ii11iIi11i / o0ii1I . Iii + i1iIi
  if 78 - 78: iI11I1II1I1I + oO0o + Ii
  if 21 - 21: I1ii11iIi11i + o0ii1I % i1iIi + OOooOOo % Iii
  if 22 - 22: ooOoO0O00 / ii . oO0o
def OoOooOo0 ( ) :
 if 40 - 40: III1iiIii * I11i / Ii / oO0o
 IIi1i1IiIIi1i ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IIi1i1IiIIi1i ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 26 - 26: oooOo0oo0oo
 if 38 - 38: o0o00Oo0O + IiI1i11I
def i1IIiIiI11 ( Cat_Name ) :
 if 61 - 61: Ii % i1IiiiI1iI / I11i
 I111 = False
 iIOO00o0O = '0'
 if Cat_Name == 'All Channels' : I111 = True
 if Cat_Name == 'Entertainment' : iIOO00o0O = '1'
 if Cat_Name == 'Movies' : iIOO00o0O = '2'
 if Cat_Name == 'Music' : iIOO00o0O = '3'
 if Cat_Name == 'News' : iIOO00o0O = '4'
 if Cat_Name == 'Sports' : iIOO00o0O = '5'
 if Cat_Name == 'Documentary' : iIOO00o0O = '6'
 if Cat_Name == 'Kids' : iIOO00o0O = '7'
 if Cat_Name == 'Food' : iIOO00o0O = '8'
 if Cat_Name == 'Religious' : iIOO00o0O = '9'
 if Cat_Name == 'USA Channels' : iIOO00o0O = '10'
 if Cat_Name == 'Other' : iIOO00o0O = '11'
 if 26 - 26: ii
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( Oooo0O )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for IiIi11iI , oO0O00oOOoooO , o0O0OOo in IIi :
  ii1IiiiI1I = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oO0O00oOOoooO ) . replace ( '\\' , '' )
  if o0O0OOo == iIOO00o0O :
   IIi1i1IiIIi1i ( IiIi11iI , '' , 7022 , ii1IiiiI1I )
  elif I111 == True :
   IIi1i1IiIIi1i ( IiIi11iI , '' , 7022 , ii1IiiiI1I )
  else : pass
  if 21 - 21: ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: iI11I1II1I1I
def OOOO0oo0o0O ( Search_Name ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( Oooo0O )
 for oO0O00oOOoooO , OoOOoOooooOOo , O0000 , Oo0oOo0ooOOOo in IIi :
  ii1IiiiI1I = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oO0O00oOOoooO ) . replace ( '\\' , '' )
  oOOo0OOOOo0Oo ( Search_Name + ': Link 1' , ( OoOOoOooooOOo ) . replace ( '\\' , '' ) , 222 , ii1IiiiI1I )
  oOOo0OOOOo0Oo ( Search_Name + ': Link 2' , ( O0000 ) . replace ( '\\' , '' ) , 222 , ii1IiiiI1I )
  oOOo0OOOOo0Oo ( Search_Name + ': Link 3' , ( Oo0oOo0ooOOOo ) . replace ( '\\' , '' ) , 222 , ii1IiiiI1I )
  if 29 - 29: Ii1I + ii . oO0o . ooOoO0O00 - ii * Ii
def iIIi1i1i1iI1I ( ) :
 Oooo0O = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , ( OoOOoOooooOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def O0o0O0000ooo0 ( ) :
 Oooo0O = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , ( OoOOoOooooOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def Iii1ii ( ) :
 Oooo0O = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( Oooo0O )
 for IiIi11iI , OoOOoOooooOOo in IIi :
  oOOo0OOOOo0Oo ( IiIi11iI , ( OoOOoOooooOOo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 45 - 45: Ii * Ii1I / o0ii1I % o0o00Oo0O / i1i1I1IIii1II * i1i1I1IIii1II
def ooOo00OOo0 ( url ) :
 url
 I1I1I1IIi1III = xbmcgui . ListItem ( IiIi11iI , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1I1IIi1III )
 return
 if 12 - 12: Ii + Ii1I * oO0o
 if 13 - 13: I1ii11iIi11i + ii / III1iiIii
def oOo0Oo0OOoo00 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( Oooo0O )
 for url , o00O0O , oO0O00oOOoooO , IiIi11iI in IIi :
  I1I1II1I11 ( IiIi11iI , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , ( o00O0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  IIi1i1IiIIi1i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 76 - 76: Ii . Iii . i1iIi . Ii1I * o0ii1I . i1IiiiI1iI
def OoooOoo0Oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o00O0O , oO0O00oOOoooO in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , o00O0O )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 oOoOoO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1O0o0oO in oOoOoO :
  ooo0OO0O0Oo = ( i1O0o0oO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oO0O00oOOoooO , '' , ooo0OO0O0Oo )
  if 33 - 33: ooOoO0O00 * I11i + Ii1I - ooOoO0O00 % ii
def o0OiI ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 35 - 35: i1i1I1IIii1II - IiI1i11I . o0ii1I % III1iiIii . o0o00Oo0O
 if 79 - 79: i1IiiiI1iI + i1i1I1IIii1II - iI11I1II1I1I * OOooOOo / ii
 if 49 - 49: ii + i1IiiiI1iI
def III1I1iiIiiI ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( ( IiIi11iI ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def i1ii1I1ii111I ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , url , 9032 , iiIi1IIiIi + 'icon.png' )
def IIIi1ii1i1 ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  if '=' in IiIi11iI :
   pass
  else :
   oOOo0OOOOo0Oo ( ( IiIi11iI ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def oo0oOiII1IiI1I11i ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  if '=' in IiIi11iI :
   pass
  else :
   oOOo0OOOOo0Oo ( IiIi11iI , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 10 - 10: IIiIiII11i % oOo0O0Ooo % o0ii1I * Ii1I
   if 74 - 74: I11i / oO0o + IiI1i11I - ooOoO0O00 / ii / Ii1I
   if 56 - 56: i1i1I1IIii1II + oOo0O0Ooo . Iii
def O0OO0 ( url ) :
 oo0o0000Oo0 ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , oO0O00oOOoooO , url in IIi :
  if 'music' in url :
   oo0o0000Oo0 ( IiIi11iI , url , 90036 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   oo0o0000Oo0 ( IiIi11iI , url , 90039 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
def OO0oO0o0oOO ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( Oooo0O )
 for IiIi11iI , url , oO0O00oOOoooO in IIi :
  OOO00OO0oOo ( IiIi11iI , url , 100009 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
  if 13 - 13: oOo0O0Ooo / o0ii1I / Iii * o0o00Oo0O
def ooOO00O00 ( url ) :
 oo0o0000Oo0 ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 Oooo0O = requests . get ( url ) . text
 iII1i11 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( Oooo0O )
 O00O0O = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00O0O ) )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  ooO00O0O0 = requests . get ( url ) . text
  I11I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( ooO00O0O0 )
  for O0OOOo in I11I :
   IiiiII1III1 = requests . get ( O0OOOo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( IiiiII1III1 )
   for i11I1iIii1i11 , iIi1i1II , i1iII1IiiIiI1 , iIIII1iII1i , iiI111I1iIiI in IIi :
    if i11I1iIii1i11 == 'xyz' :
     ii1I11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( IiIi11iI , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
    else :
     ii1I11 = 'http://' + iIIII1iII1i + '.' + i1iII1IiiIiI1 + '.' + iIi1i1II + '.' + i11I1iIii1i11 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( IiIi11iI , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
 for o0OO0o0oOOO0O in iII1i11 :
  oo0o0000Oo0 ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1000111 , '' , '' , '' , '' )
  if 37 - 37: IiI1i11I . i1i1I1IIii1II
  if 2 - 2: Iii . o0o00Oo0O
  if 22 - 22: i1i1I1IIii1II / IIiIiII11i . OOooOOo
def Iii11iiI111i ( ) :
 oo0o0000Oo0 ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 98 - 98: ooOoO0O00 + i1IiiiI1iI - Ii1I . ii / o0o00Oo0O / IiI1i11I
 if 66 - 66: ooOoO0O00 % ii * Ii + i1i1I1IIii1II * o0o00Oo0O / oO0o
def iI1IiI1 ( url , name ) :
 oo0o0000Oo0 ( name , '' , '' , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 Oooo0O = requests . get ( url ) . text
 iII1i11 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( Oooo0O )
 O00O0O = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00O0O ) )
 for url , oO0O00oOOoooO , name in IIi :
  ooO00O0O0 = requests . get ( url ) . text
  I11I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( ooO00O0O0 )
  for O0OOOo in I11I :
   IiiiII1III1 = requests . get ( O0OOOo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( IiiiII1III1 )
   for i11I1iIii1i11 , iIi1i1II , i1iII1IiiIiI1 , iIIII1iII1i , iiI111I1iIiI in IIi :
    if i11I1iIii1i11 == 'xyz' :
     ii1I11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( name , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
    else :
     ii1I11 = 'http://' + iIIII1iII1i + '.' + i1iII1IiiIiI1 + '.' + iIi1i1II + '.' + i11I1iIii1i11 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( name , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
     if 53 - 53: i1IiiiI1iI + III1iiIii . ooOoO0O00
 for o0OO0o0oOOO0O in iII1i11 :
  oo0o0000Oo0 ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1003111 , '' , '' , '' , '' )
  if 26 - 26: Ii - IIiIiII11i
  if 43 - 43: oOo0O0Ooo
def I11IIii ( ) :
 oo0o0000Oo0 ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 19 - 19: ooOoO0O00 / o0ii1I / OOooOOo . oOo0O0Ooo / o0ii1I % I11i
 if 39 - 39: i1iIi - ii
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
def o0oOOO0O0 ( url , name ) :
 oo0o0000Oo0 ( name , '' , '' , '' , '' , '' , '' )
 oo0o0000Oo0 ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 Oooo0O = requests . get ( url ) . text
 iII1i11 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( Oooo0O )
 O00O0O = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( Oooo0O )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00O0O ) )
 for url , oO0O00oOOoooO , name in IIi :
  ooO00O0O0 = requests . get ( url ) . text
  I11I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( ooO00O0O0 )
  for O0OOOo in I11I :
   IiiiII1III1 = requests . get ( O0OOOo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( IiiiII1III1 )
   for i11I1iIii1i11 , iIi1i1II , i1iII1IiiIiI1 , iIIII1iII1i , iiI111I1iIiI in IIi :
    if i11I1iIii1i11 == 'xyz' :
     ii1I11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( name , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
    else :
     ii1I11 = 'http://' + iIIII1iII1i + '.' + i1iII1IiiIiI1 + '.' + iIi1i1II + '.' + i11I1iIii1i11 + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOO00OO0oOo ( name , ii1I11 , 1001111 , oO0O00oOOoooO , oO0O00oOOoooO , '' , '' )
     if 18 - 18: oOo0O0Ooo / Ii - o0ii1I
 for o0OO0o0oOOO0O in iII1i11 :
  oo0o0000Oo0 ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1005111 , '' , '' , '' , '' )
def oOO0o00O ( name , url ) :
 import urlresolver
 try :
  oOoO = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( oOoO , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 59 - 59: IIiIiII11i - oO0o
 if 31 - 31: Iii - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
 if 46 - 46: III1iiIii * oO0o / oooOo0oo0oo + I1ii11iIi11i
def I1iI1iIIIii ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'Daily' in IiIi11iI :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 9008 , O0O )
def I1iI ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def I1IiiI1i1 ( url ) :
 oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 oOOo0OOOOo0Oo ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  oOOo0OOOOo0Oo ( ( IiIi11iI ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 23 - 23: oO0o / I11i
def iIiI11i1i ( ) :
 Oooo0O = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if '.m3u' in OoOOoOooooOOo :
   IIi1i1IiIIi1i ( ( IiIi11iI ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + OoOOoOooooOOo ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def i1I1I1IIIi11 ( url ) :
 Oooo0O = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  oOOo0OOOOo0Oo ( ( IiIi11iI ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 81 - 81: OOooOOo
def oOOoo ( ) :
 Oooo0O = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  if 'category' in OoOOoOooooOOo :
   IIi1i1IiIIi1i ( IiIi11iI , 'http://www.disclose.tv/' + OoOOoOooooOOo , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 21 - 21: IiI1i11I / oooOo0oo0oo % III1iiIii
   if 51 - 51: Iii + i1iIi / oOo0O0Ooo
def Ii11i ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( Oooo0O )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( Oooo0O )
 for url , IiIi11iI , oO0O00oOOoooO in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , 'http://www.disclose.tv/' + url , 7011 , oO0O00oOOoooO )
 for url in next :
  IIi1i1IiIIi1i ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 65 - 65: o0ii1I % oO0o - Ii % I1ii11iIi11i
  if 19 - 19: o0o00Oo0O
def O0oo0O0OO0OOo ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( Oooo0O )
 Iiii1iI1i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  if 'http' in url :
   oOOo0OOOOo0Oo ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , IiIi11iI in i1Iii1i1I :
  oOOo0OOOOo0Oo ( IiIi11iI , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in Iiii1iI1i :
  oOOo0OOOOo0Oo ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 12 - 12: Iii
  if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
def i1O0o00o0Oo ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 29 - 29: oO0o - I1ii11iIi11i . i1i1I1IIii1II / oO0o % Ii
def I1iO0000 ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0iiI1iii1I111 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I11I1 = len ( O0iiI1iii1I111 )
 if 66 - 66: Ii
 if 94 - 94: o0o00Oo0O . ii - Ii - ooOoO0O00 * I11i
 if I11I1 == 1 :
  for O0oooo0OO000 in O0iiI1iii1I111 :
   O0oooo0OO000 = O0oooo0OO000 . replace ( 'player' , 'watch' )
   IiiIIIIII = O0oooo0OO000 + '&fv=&sou='
   iIIiI11i = OooOoooOo ( IiiIIIIII )
   iiiII11I11i = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iIIiI11i )
   for Iii11i in iiiII11I11i :
    IIIII1 = False
    Resolve ( Iii11i )
    if 49 - 49: ii
 elif I11I1 > 1 :
  if 74 - 74: oooOo0oo0oo - IIiIiII11i
  for O0oooo0OO000 in O0iiI1iii1I111 :
   ooo00O = OooOoooOo ( O0oooo0OO000 )
   iII11iI1i1iI = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( ooo00O )
   IiI1IIiIII = iII11iI1i1iI
   IiI1IIiIII = ( str ( IiI1IIiIII ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IiI1IIiIII
   oOOo0OOOOo0Oo ( 'DOUBLE LINK' , IiI1IIiIII , 424 , '' )
   if 95 - 95: III1iiIii * IIiIiII11i % I11i * I1ii11iIi11i . Iii
   for url in iII11iI1i1iI :
    IIi1i1IiIIi1i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O0000 = Google . resolve ( url )
    except :
     pass
    try :
     ii1I11ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O0000 ) )
     for i1IIiIII111 , iIIiI in ii1I11ii :
      if 62 - 62: oO0o
      HD_URLS . append ( i1IIiIII111 )
      SD_URLS . append ( iIIiI )
    except :
     pass
 else :
  pass
  if 8 - 8: Ii1I * III1iiIii / I1ii11iIi11i
def OOo0O0Oo000OO ( ) :
 if 72 - 72: i1IiiiI1iI / oOo0O0Ooo + ooOoO0O00
 if 53 - 53: i1IiiiI1iI
 IIi1i1IiIIi1i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 81 - 81: o0o00Oo0O % I11i / o0ii1I / i1iIi . Ii + III1iiIii
 IIi1i1IiIIi1i ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 29 - 29: i1iIi
 if 70 - 70: i1i1I1IIii1II . o0o00Oo0O % Iii % III1iiIii - Iii * Ii1I
def i1IiOOO ( ) :
 Oooo0O = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , 'http://cnfstudio.com/genre/' + OoOOoOooooOOo , 7003 , iiIi1IIiIi + 'icon.png' )
  if 65 - 65: ii + i1IiiiI1iI % i1IiiiI1iI . i1iIi / i1i1I1IIii1II
iIii1 = xbmcgui . Dialog ( )
if 6 - 6: ooOoO0O00 + Ii1I
i1Ii1I1I1 = '{UN},' ; Oo0OO0oOo0OOo = '{IG},' ; Oo00O00oo0Ooo = '{PL},' ; iIiI = '{LO},' ; iIi1Iii = '{LP},' ; OoOO0OooOoooo = '{HA},' ; IIIii = '{XD},' ; iIii1111Ii1I1 = '{TA},' ; O00o00oOOo = '{DP},' ; I1oO = '{JT},' ; Oo0o0O0oO0o = '{JJ},' ; iiIioo0O0 = '{MM},' ; oooO000oO0O = '{FQ},' ; I1iIIiiII = '{HH},'
if 98 - 98: Iii % ooOoO0O00 / ooOoO0O00
def oooOOo0Oo0OO0O ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( Oooo0O )
 I1iO00oo0oOo = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( Oooo0O )
 for oO0O00oOOoooO , url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oO0O00oOOoooO )
 I1iO00oo0oOo = I1iO00oo0oOo
 for url in I1iO00oo0oOo :
  IIi1i1IiIIi1i ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 34 - 34: Ii + ii
def iIIi1iiIIiIi1 ( url ) :
 if 30 - 30: o0o00Oo0O * III1iiIii - i1IiiiI1iI % o0o00Oo0O * o0ii1I
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  II1II111iIi = OO0oO0ooOOOoO ( iiI111I1iIiI )
  iIiIIii11iI = OO0oO0ooOOOoO ( url )
  if 27 - 27: I11i
  if 13 - 13: Ii1I - o0o00Oo0O * i1i1I1IIii1II % iI11I1II1I1I . oOo0O0Ooo - oooOo0oo0oo
def OO0oO0ooOOOoO ( url ) :
 if 77 - 77: OOooOOo + ooOoO0O00 - iI11I1II1I1I
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( Oooo0O )
 for url in IIi :
  Ii11iIII ( url )
  if 65 - 65: Ii + Iii
  if 44 - 44: i1iIi
def Iii11Ii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 32 - 32: IIiIiII11i * oOo0O0Ooo / iI11I1II1I1I - Ii1I . Iii
def oo000O ( ) :
 if os . path . exists ( II ) :
  I1iIIiIi1 = open ( II , 'r' )
  for I1I1I1IIi1III in I1iIIiIi1 :
   IiIIi1iI1ii1 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1I1I1IIi1III )
   for IiIi11iI , OoOOoOooooOOo in IiIIi1iI1ii1 :
    oOOo0OOOOo0Oo ( IiIi11iI , OoOOoOooooOOo , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 7 - 7: I1ii11iIi11i . Ii / oooOo0oo0oo + i1i1I1IIii1II
def iIIiii ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = ooo ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for IiIi11iI , url in IIi :
   url = ( url ) . strip ( )
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 25 - 25: IIiIiII11i + Iii
  if 97 - 97: o0o00Oo0O + oooOo0oo0oo % OOooOOo * Iii . iI11I1II1I1I
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo in IIi :
  OoOOoOooooOOo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OoOOoOooooOOo
 IiIi11iI = 'plugin.video.GenieTv'
 if 94 - 94: i1i1I1IIii1II
 O000Oo ( OoOOoOooooOOo , IiIi11iI )
 if 34 - 34: ii - i1i1I1IIii1II / oooOo0oo0oo / I11i + oooOo0oo0oo . Ii
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo in IIi :
  OoOOoOooooOOo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OoOOoOooooOOo
 IiIi11iI = 'repository.GenieTv'
 if 19 - 19: OOooOOo % OOooOOo
 O000Oo ( OoOOoOooooOOo , IiIi11iI )
 if 74 - 74: Ii / Ii1I - i1i1I1IIii1II . oO0o
 if 25 - 25: oooOo0oo0oo % i1i1I1IIii1II
def II1 ( ) :
 iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iI111iIIii )
 if O0oO == 0 :
  i1i1111IIIii ( )
 if O0oO == 1 :
  ii11IiiiIi1iI ( )
  if 23 - 23: IIiIiII11i - IIiIiII11i / i1i1I1IIii1II - III1iiIii - Ii
  if 68 - 68: o0o00Oo0O / IiI1i11I
  if 70 - 70: I1ii11iIi11i
  if 92 - 92: oooOo0oo0oo + ooOoO0O00 - i1iIi
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
i11ii1II11I = 'https://addons.tvaddons.ag/'
if 47 - 47: oO0o * Iii
def ii11IiiiIi1iI ( ) :
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 OO0OOoooOo00 = 'https://addons.tvaddons.ag/search/?keyword=' + III111i11IiI
 II11iIiIIIiI = OooOoooOo ( OO0OOoooOo00 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , i11i1iIiii , IiIi11iI in IIi :
  I1I1II1I11 ( IiIi11iI , OoOOoOooooOOo , 10054 , 'https://addons.tvaddons.ag/' + i11i1iIiii , Oo00OOOOO , '' )
  if 70 - 70: I1ii11iIi11i
  if 93 - 93: IiI1i11I . Ii1I . I1ii11iIi11i . i1i1I1IIii1II . ii
def i1i1111IIIii ( ) :
 II11iIiIIIiI = OooOoooOo ( i11ii1II11I )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  if 'Repositories' in IiIi11iI :
   pass
  elif 'Services' in IiIi11iI :
   pass
  elif 'International' in IiIi11iI :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , OoOOoOooooOOo , 10053 , 'https://addons.tvaddons.ag/' + oO0O00oOOoooO , Oo00OOOOO , '' )
   if 51 - 51: o0o00Oo0O - IiI1i11I
   if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iII1i11 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  if 'Please' in IiIi11iI :
   pass
  else :
   Ii1I1i ( IiIi11iI , url , 10054 , 'https://addons.tvaddons.ag/' + oO0O00oOOoooO , Oo00OOOOO , '' )
 for url in iII1i11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 43 - 43: i1IiiiI1iI + oO0o * ii
  if 85 - 85: IiI1i11I + oooOo0oo0oo
def II1iIiIiIIi ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   o0OOOoO0 = os . path . join ( oOOooOoo , name + '.zip' )
   try :
    os . remove ( o0OOOoO0 )
   except :
    pass
   downloader . download ( url , o0OOOoO0 , o0oOoO00o )
   o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print o0OoOo00o0o
   print '======================================='
   extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
   OoOO0o ( )
   if 53 - 53: o0ii1I - oooOo0oo0oo
def O000Oo ( url , name ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , name + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 OoOO0o ( )
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
def OoOO0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
 if 23 - 23: iI11I1II1I1I * Iii . i1IiiiI1iI - I11i
def Ooo0oo0oO000 ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , i11i1iIiii , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , url , 1007 , i11i1iIiii )
def iI11i11iI ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , i11i1iIiii , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 1006 , i11i1iIiii )
  if 47 - 47: IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
def OOoo00o0 ( ) :
 Oooo0O = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , i11I , IiIi11iI in IIi :
  o0OO0 ( IiIi11iI , 100109 , OoOOoOooooOOo , image = i1oOOoo0o0OOOO , isFolder = True )
  if 28 - 28: oooOo0oo0oo
def OO0o0ooO0 ( url ) :
 import random
 i1ioooo00 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 i1ioooo00 . clear ( )
 oO00o = [ ]
 oo0oOoo = [ ]
 II1IoO0Ooo0o00o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0000 , i1oOOoo0o0OOOO , o00O0O , i11I , IiIi11iI in IIi :
  oO00o . append ( [ O0000 , IiIi11iI ] )
  if len ( oO00o ) == len ( IIi ) :
   for I1I1I1IIi1III in oO00o :
    oOOo0OOOoo0 = random . randint ( 1 , len ( oO00o ) )
    try :
     oOOoo0oO00o = oO00o [ int ( oOOo0OOOoo0 ) ]
    except :
     pass
    if len ( oo0oOoo ) <= 20 :
     if oOOoo0oO00o [ 1 ] not in II1IoO0Ooo0o00o :
      o0o = OooOoooOo ( oOOoo0oO00o [ 0 ] )
      Iiii1iI1i = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for O00O0OoO0o0 , o0oo in Iiii1iI1i :
       OOoOoo = OooOoooOo ( O00O0OoO0o0 )
       OOoOooOoOOOoo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for OOO0o0 , iiI111I1iIiI in OOoOooOoOOOoo :
        if 'panda' in iiI111I1iIiI :
         oOIIi = OooOoooOo ( iiI111I1iIiI )
         IIi11 = re . compile ( "url: '(.+?)'" ) . findall ( oOIIi )
         for OO00OO0 in IIi11 :
          if 'http' in OO00OO0 :
           i1iiIIIi = xbmcgui . ListItem ( oOOoo0oO00o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : oOOoo0oO00o [ 1 ] } )
           i1iiIIIi . setProperty ( "IsPlayable" , "true" )
           i1ioooo00 . add ( OO00OO0 , i1iiIIIi )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iiIIIi )
           if 34 - 34: IIiIiII11i
def o0OO0 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 o0oOOo0OooOo = sys . argv [ 0 ]
 o0oOOo0OooOo += '?mode=' + str ( mode )
 o0oOOo0OooOo += '&title=' + urllib . quote_plus ( name )
 o0oOOo0OooOo += '&image=' + urllib . quote_plus ( image )
 o0oOOo0OooOo += '&page=' + str ( page )
 if url != '' :
  o0oOOo0OooOo += '&url=' + urllib . quote_plus ( url )
 if keyword :
  o0oOOo0OooOo += '&keyword=' + urllib . quote_plus ( keyword )
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  i1iiIIIi . addContextMenuItems ( contextMenu )
 if infoLabels :
  i1iiIIIi . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  i1iiIIIi . setProperty ( "IsPlayable" , "true" )
 i1iiIIIi . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = isFolder )
 if 21 - 21: Ii / Ii / ooOoO0O00
 if 76 - 76: IIiIiII11i % i1iIi - Ii1I
def I1iIiI11I1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , iconimage , o00O0O , i11I , name in IIi :
  if 'http' in url :
   if '.php' in url :
    iII1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for I1I1I1IIi1III in iII1 :
     if I1I1I1IIi1III == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I1iioO0 ( name , url , 1016 , iconimage , i11I , o00O0O )
   else :
    if 'youtube' in url :
     iII1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for I1I1I1IIi1III in iII1 :
      if I1I1I1IIi1III == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11OoooO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , i11I , o00O0O )
    else :
     iII1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for I1I1I1IIi1III in iII1 :
      if I1I1I1IIi1III == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11OoooO ( name , url , 222 , iconimage , i11I , o00O0O )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  else :
   IiiI ( url , iconimage , name )
   if 83 - 83: oooOo0oo0oo . ii + IIiIiII11i - IiI1i11I - Ii
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
  for url , i11i1iIiii , name in IIi :
   if 'http' in url :
    if '.php' in url :
     IIi1i1IiIIi1i ( name , url , 1016 , i11i1iIiii )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOOo0OOOOo0Oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1iIiii )
     else :
      iII1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for I1I1I1IIi1III in iII1 :
       if I1I1I1IIi1III == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOOo0OOOOo0Oo ( name , url , 222 , i11i1iIiii )
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   else :
    IiiI ( url , i11i1iIiii , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 24 - 24: i1IiiiI1iI
def IiiI ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Oo0ooi1I = ( url ) . replace ( iI11iiI1 , 'http' ) . replace ( o0OoO0 , '.com' ) ;
 II1iiII = ( Oo0ooi1I ) . replace ( I1Ioo000oooooooO , 'a' ) . replace ( IIIoooOo0ooO00o , 'b' ) . replace ( i1iII11111iIi , 'c' ) . replace ( Ii1IiIIIi1i , 'd' ) . replace ( Oo00O00oo0Ooo , 'e' ) . replace ( I1oO , 'f' ) ;
 IiiI11iI = ( II1iiII ) . replace ( iiIi11i1I1 , 'g' ) . replace ( OoOO0OooOoooo , 'h' ) . replace ( I11Ii1I1I , 'i' ) . replace ( o0oo0000Oo , 'j' ) . replace ( I1i11 , 'k' ) . replace ( oO0o0O0ooo0O , 'l' ) ;
 OoOoOo0O0OO = ( IiiI11iI ) . replace ( OOOoO0OoOOO0O0O , 'm' ) . replace ( OOooOOO , 'n' ) . replace ( IiIii1iII , 'o' ) . replace ( O0o0Oo00O000O , 'p' ) . replace ( I11I1i1I , 'q' ) . replace ( i11IIiIi , 'r' ) ;
 oOI11Ii1 = ( OoOoOo0O0OO ) . replace ( iII111Ii , 's' ) . replace ( II111Ii1I1I , 't' ) . replace ( O00Oo0O , 'u' ) . replace ( IIII1Ii1II1 , 'v' ) . replace ( IiiIiIiIIIii1 , 'w' ) . replace ( OOOo0oOOO , 'x' ) ;
 O0oOO0O000O0 = ( oOI11Ii1 ) . replace ( i11I1IIII , 'y' ) . replace ( O0ooOOo0 , 'z' ) . replace ( i1Ii1I1I1 , '.' ) . replace ( Oo0OO0oOo0OOo , '(' ) . replace ( iIiI , ')' ) . replace ( iIi1Iii , '/' ) ;
 ii1iiiI = ( O0oOO0O000O0 ) . replace ( O0000000oooOO , '1' ) . replace ( o00oo0oOo0o0 , '2' ) . replace ( i1iII1 , '3' ) . replace ( iIii1111Ii1I1 , '4' ) . replace ( O00o00oOOo , '5' ) . replace ( oo00OO0o0 , '6' ) ;
 oOoo0o00O = ( ii1iiiI ) . replace ( Oo0o0O0oO0o , '7' ) . replace ( iiIioo0O0 , '8' ) . replace ( oooO000oO0O , '9' ) . replace ( I1iIIiiII , '0' ) . replace ( IiiiI1i1i , ':' ) . replace ( ii11II1 , '%' ) ;
 url = ( oOoo0o00O ) . replace ( oO0OoiIi1IIIi1Ii , '-' ) . replace ( IIIii , '_' ) ;
 oOOo0OOOOo0Oo ( name , url , 222 , iconimage ) ;
 if 36 - 36: i1iIi / IIiIiII11i - i1iIi * IiI1i11I
 if 43 - 43: IiI1i11I * ooOoO0O00 . oOo0O0Ooo . OOooOOo / III1iiIii - I1ii11iIi11i
def oo00OoO00o ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , i11i1iIiii , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 1007 , i11i1iIiii )
def II1Oooo00oO0OO0o ( url ) :
 if 47 - 47: I1ii11iIi11i / OOooOOo
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , i11i1iIiii , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 1006 , i11i1iIiii )
  if 26 - 26: Iii . Ii1I
def OO00OOOO00oOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 o0OOOo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 o0OOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0OOOo )
 if 56 - 56: III1iiIii * o0ii1I . IIiIiII11i / OOooOOo
 if 70 - 70: Ii1I
def o0oo00OOOo ( url ) :
 Oooo0O = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oooo0O )
 for url , oO0O00oOOoooO , IiIi11iI in IIi :
  if '-dir-' in IiIi11iI :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oO0O00oOOoooO )
  else :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' , url , 1006 , oO0O00oOOoooO )
   if 82 - 82: oO0o + Ii
def OoOO000oo0 ( url ) :
 Oooo0O = ooo ( url )
 OOOO0o0OOo = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if '[To Parent Directory]' in IiIi11iI :
   IiIi11iI = 'HOME'
   pass
  elif 'HOME' in IiIi11iI :
   pass
  elif '.m3u' in IiIi11iI :
   IIi1i1IiIIi1i ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , OOOO0o0OOo + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in IiIi11iI :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OOOO0o0OOo + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in IiIi11iI :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OOOO0o0OOo + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) , OOOO0o0OOo + url , 1012 , iiIi1IIiIi + 'music.png' )
def O0o000 ( url ) :
 II11iIiIIIiI = ooo ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O00oOOoooO , IiIi11iI , url in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 28 - 28: iI11I1II1I1I * iI11I1II1I1I * i1iIi % Ii1I / Ii
def oOoOO0o ( url ) :
 Oooo0O = ooo ( url )
 OOOO0o0OOo = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  if '.mp3' in IiIi11iI :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '/' , '' ) , OOOO0o0OOo + url , 1011 , iiIi1IIiIi + 'music.png' )
def OOoOo ( ) :
 Oooo0O = ooo ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oooo0O )
 for OoOOoOooooOOo , oO0O00oOOoooO , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , ( 'http://www.cyn.net/music/' + OoOOoOooooOOo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oO0O00oOOoooO ) . replace ( ' ' , '%20' ) )
def i1iiii11iIIiiI1I ( url , img ) :
 Oooo0O = ooo ( url )
 O0000 = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( O0000 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 91 - 91: oOo0O0Ooo - ii - ii
def IIIiI1iIIII ( url ) :
 Oooo0O = ooo ( url )
 O0000 = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( Oooo0O )
 for type , url , IiIi11iI in IIi :
  if '[VID]' in type :
   oOOo0OOOOo0Oo ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , O0000 + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   IIIiI1iIIII ( O0000 + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: IiI1i11I * Ii / ooOoO0O00
 if 86 - 86: oOo0O0Ooo % Iii * o0o00Oo0O + ooOoO0O00 % i1IiiiI1iI
def oo0oO ( ) :
 OOOii1i1iiI = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 OO0oOOo = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III111i11IiI = OO0oOOo . lower ( )
 OoOOoOooooOOo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 I1ii1 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O0000 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 97 - 97: IIiIiII11i * OOooOOo - i1IiiiI1iI / Ii / OOooOOo
 II11iIiIIIiI = O00O0oOO00O00 ( OoOOoOooooOOo )
 OOOiII1 = O00O0oOO00O00 ( I1ii1 )
 o0o = O00O0oOO00O00 ( O0000 )
 if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoOOoOooooOOo , i1oOOoo0o0OOOO , o00O0O , I11iiii1I , IiIi11iI in IIi :
   if OO0oOOo in IiIi11iI . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , OoOOoOooooOOo , 1016 , i1oOOoo0o0OOOO , i11I , o00O0O )
    if 74 - 74: oooOo0oo0oo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOOiII1 != 'Failed' :
  I1III1II1I11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOOiII1 )
  for OoOOoOooooOOo , IiIi11iI in I1III1II1I11 :
   if OO0oOOo in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + OoOOoOooooOOo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 30 - 30: o0o00Oo0O . o0ii1I / I11i + oOo0O0Ooo - o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for OoOOoOooooOOo , IiIi11iI in i1Iii1i1I :
   if OO0oOOo in IiIi11iI . lower ( ) :
    IIi1i1IiIIi1i ( ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + OoOOoOooooOOo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 88 - 88: Ii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: oO0o + o0o00Oo0O
    if 20 - 20: I11i % Iii . i1iIi - ooOoO0O00 . o0o00Oo0O
    if 10 - 10: ooOoO0O00
    if 49 - 49: i1IiiiI1iI - o0ii1I . o0o00Oo0O
    if 46 - 46: oooOo0oo0oo
    if 64 - 64: oOo0O0Ooo / OOooOOo
OOOoO0OoOOO0O0O = '{SF},' ; OOooOOO = '{IF},' ; IiIii1iII = '{PW},' ; i1iII1 = '{AM},' ; O0o0Oo00O000O = '{GF},' ; I11I1i1I = '{DD},' ; i11IIiIi = '{UO},' ; iII111Ii = '{LE},' ; O00Oo0O = '{ZY},' ; IIII1Ii1II1 = '{UE},' ; IiiIiIiIIIii1 = '{PE},' ; OOOo0oOOO = '{JE},' ; i11I1IIII = '{TH},' ; O0ooOOo0 = '{LK},'
if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
def i1oO0OO0 ( ) :
 Oooo0O = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 8021 , iiIi1IIiIi + 'iwatch.png' )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def o0o0o ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( Oooo0O )
 for url , IiIi11iI , iIIIII1iiiiII in IIi :
  IIi1i1IiIIi1i ( IiIi11iI + iIIIII1iiiiII , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def oooo0O ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( Oooo0O )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1i1ii ( url )
def I1i1ii ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( Oooo0O )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( Oooo0O )
 Iiii1iI1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( Oooo0O )
 OOoOooOoOOOoo = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( 'VidSpot - ' + IiIi11iI , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  oOOo0OOOOo0Oo ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , IiIi11iI in OOoOooOoOOOoo :
  oOOo0OOOOo0Oo ( 'VidUp' + IiIi11iI , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for IiIi11iI , url in Iiii1iI1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOOo0OOOOo0Oo ( 'TheVideo - ' + IiIi11iI , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 14 - 14: i1iIi
def IIiIII ( ) :
 Oooo0O = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 1021 , iiIi1IIiIi + 'anime.png' )
  if 5 - 5: o0ii1I
  if 26 - 26: iI11I1II1I1I / ooOoO0O00
def i11i1i ( ) :
 Oooo0O = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( Oooo0O )
 for OoOOoOooooOOo , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , OoOOoOooooOOo , 1002 , iiIi1IIiIi + 'anime.png' )
  if 84 - 84: iI11I1II1I1I / I11i / IIiIiII11i
  if 81 - 81: Ii + I11i / IIiIiII11i + Iii
  if 73 - 73: oO0o + oooOo0oo0oo + III1iiIii - ooOoO0O00
def OoOoO0OoO ( url ) :
 Oooo0O = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( Oooo0O )
 for oO0O00oOOoooO in i1Iii1i1I :
  O0Ooo0o = oO0O00oOOoooO
 Iiii1iI1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( Oooo0O )
 for url in Iiii1iI1i :
  IIi1i1IiIIi1i ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( Oooo0O )
 for url , IiIi11iI in IIi :
  IIi1i1IiIIi1i ( IiIi11iI , url , 1003 , O0Ooo0o )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0O ( url , IMAGE ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( Oooo0O )
 for IiIi11iI , url in IIi :
  print IiIi11iI + '     ' + url
  if 'easy' in url :
   IIIIii1Ii11i ( url )
  elif 'playpanda' in url :
   IIIIii1Ii11i ( url )
   if 88 - 88: i1IiiiI1iI * Iii + oOo0O0Ooo % oooOo0oo0oo - oooOo0oo0oo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIIii1Ii11i ( url ) :
 Oooo0O = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( Oooo0O )
 for url in IIi :
  oOOo0OOOOo0Oo ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 41 - 41: Ii1I * Iii * ooOoO0O00 . o0ii1I * I1ii11iIi11i
  if 93 - 93: iI11I1II1I1I
def iI111Ii ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 28 - 28: I11i / oO0o - Ii % I1ii11iIi11i % IIiIiII11i - OOooOOo
def ooo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 64 - 64: o0ii1I % o0o00Oo0O % III1iiIii . oooOo0oo0oo
def oOoOoo0OOOo0 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oO0o0OooOO0 = ( '%s%s' % ( iiIiooOo0oo0O0O , url ) )
 iiI111I1iIiI = ooo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , i11i1iIiii , IiIi11iI in IIi :
  oOOo0OOOOo0Oo ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + IiIi11iI + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i11i1iIiii )
  if 1 - 1: I11i
def i1Ii1Ii1 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  o00O ( url , IiIi11iI )
 else :
  ooOoO00 ( url )
def ooOoO00 ( url ) :
 import urlresolver
 try :
  oOoO = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( oOoO , xbmcgui . ListItem ( IiIi11iI ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( IiIi11iI ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def Ii11iIII ( url ) :
 if 19 - 19: Iii * i1i1I1IIii1II * Iii + oOo0O0Ooo
 O000O = open ( OOOO0OOoO0O0 , "a" )
 O000O . write ( 'url="' + url + '"\n' )
 O000O . close
 if 41 - 41: iI11I1II1I1I / i1IiiiI1iI . Ii1I * Ii * Ii1I + I11i
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 import urlresolver
 try : iII . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( IiIi11iI ) )
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iII . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def o00O ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OoO0O00oo = '.mp4'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.mkv' in url :
  OoO0O00oo = '.mkv'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.mp3' in url :
  OoO0O00oo = '.mp3'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.avi' in url :
  OoO0O00oo = '.avi'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.mov' in url :
  OoO0O00oo = '.mov'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.mpeg' in url :
  OoO0O00oo = '.mpeg'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.mpg' in url :
  OoO0O00oo = '.mpg'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.flv' in url :
  OoO0O00oo = '.flv'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 elif '.wmv' in url :
  OoO0O00oo = '.wmv'
  iI111iIIii = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0oO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iI111iIIii )
  if O0oO == 0 :
   ooOoO00 ( url )
  if O0oO == 1 :
   OO0iII1I1i ( url , name , OoO0O00oo )
 else :
  ooOoO00 ( url )
def OO0iII1I1i ( url , name , cat ) :
 I1iiI1IiI1iii ( )
 oOOooOoo = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , file )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def I1iiI1IiI1iii ( ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def i1Ii1IiiI ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % IiIi11iI )
 xbmc . sleep ( 1 )
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 o0oOoO00o . update ( 100 , '%s' % IiIi11iI )
 xbmc . sleep ( 1 )
 iII . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 80 - 80: i1iIi % III1iiIii
def OO0o0oO0O000o ( url ) :
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iII . play ( url ) . strip ( )
 except : pass
 if 50 - 50: IIiIiII11i . I11i
def iIII1 ( url ) :
 iII = xbmc . Player ( oO0O000oOoo0O ( ) )
 import urlresolver
 ii1iI111IIi1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iII . play ( ii1iI111IIi1 )
 xbmc . sleep ( 1 )
 iII . play ( url )
 if 88 - 88: iI11I1II1I1I / o0ii1I * III1iiIii / i1IiiiI1iI
 if 31 - 31: o0o00Oo0O . oOo0O0Ooo
def oO0O000oOoo0O ( ) :
 try :
  i1i11i1 = getSet ( "core-player" )
  if ( i1i11i1 == 'DVDPLAYER' ) : ii1iIii1Ii1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( i1i11i1 == 'MPLAYER' ) : ii1iIii1Ii1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( i1i11i1 == 'PAPLAYER' ) : ii1iIii1Ii1 = xbmc . PLAYER_CORE_PAPLAYER
  else : ii1iIii1Ii1 = xbmc . PLAYER_CORE_AUTO
 except : ii1iIii1Ii1 = xbmc . PLAYER_CORE_AUTO
 return ii1iIii1Ii1
 return True
 if 2 - 2: i1IiiiI1iI
def IIi1i1IiIIi1i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  II11i111i1iIiiIiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = True )
 return o0iIiiIiiIi
 if 67 - 67: i1iIi
def oOo0Oo0Oo0 ( name , url , mode , iconimage , fanart , description ) :
 if 53 - 53: o0o00Oo0O . I11i . IIiIiII11i * OOooOOo . oooOo0oo0oo
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = True )
 return o0iIiiIiiIi
 if 78 - 78: OOooOOo * OOooOOo - oO0o / i1i1I1IIii1II
def oOOo0OOOOo0Oo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  II11i111i1iIiiIiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = False )
 return o0iIiiIiiIi
 if 24 - 24: i1IiiiI1iI . i1i1I1IIii1II + i1iIi . Ii1I . IIiIiII11i
 if 25 - 25: oOo0O0Ooo
 if 88 - 88: ooOoO0O00
 if 93 - 93: Ii1I . oO0o
 if 67 - 67: IIiIiII11i + ii + oOo0O0Ooo
 if 76 - 76: o0o00Oo0O / I1ii11iIi11i . OOooOOo
def OO0oO0O ( url , heading , announce ) :
 class OO0oo00OO00oO ( ) :
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
   try : iiii111II = open ( announce ) ; oO0o0 = iiii111II . read ( )
   except : oO0o0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oO0o0 ) )
   return
 OO0oo00OO00oO ( )
 OO0oo00OO00oO ( )
def o0OIiII ( heading , announce ) :
 class OO0oo00OO00oO ( ) :
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
   try : iiii111II = open ( announce ) ; oO0o0 = iiii111II . read ( )
   except : oO0o0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oO0o0 ) )
   return
 OO0oo00OO00oO ( )
 OO0oo00OO00oO ( )
def oOo0O ( ) :
 OO0oO0O ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 51 - 51: ii * o0o00Oo0O - oO0o . I1ii11iIi11i % IIiIiII11i + III1iiIii
 if 48 - 48: III1iiIii . IIiIiII11i - Ii * IiI1i11I
 if 51 - 51: ii + Iii . IiI1i11I + Ii * IiI1i11I - oO0o
 if 60 - 60: IiI1i11I * iI11I1II1I1I . OOooOOo . I11i / iI11I1II1I1I
 if 36 - 36: ooOoO0O00 . ii - IIiIiII11i - OOooOOo - III1iiIii
def OoOO0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 53 - 53: Ii1I - IIiIiII11i . Ii
 if 76 - 76: iI11I1II1I1I - I1ii11iIi11i
 if 79 - 79: oOo0O0Ooo * III1iiIii . ii % i1IiiiI1iI * i1IiiiI1iI
 if 17 - 17: i1IiiiI1iI - i1IiiiI1iI . i1i1I1IIii1II / i1IiiiI1iI
 if 36 - 36: Ii1I * ooOoO0O00 + iI11I1II1I1I
 if 55 - 55: oOo0O0Ooo . i1IiiiI1iI - oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I * o0ii1I
 if 77 - 77: oooOo0oo0oo
 if 29 - 29: IIiIiII11i % iI11I1II1I1I * o0o00Oo0O . I11i
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
 if 9 - 9: Iii / i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo - IIiIiII11i
 if 96 - 96: IiI1i11I + I1ii11iIi11i - ii . ooOoO0O00 + ooOoO0O00 % iI11I1II1I1I
 if 80 - 80: ii / o0o00Oo0O / i1IiiiI1iI - I1ii11iIi11i . Ii
 if 3 - 3: I1ii11iIi11i - oooOo0oo0oo * oO0o - IIiIiII11i . ii
 if 14 - 14: oOo0O0Ooo
 if 41 - 41: i1IiiiI1iI % ooOoO0O00 + oO0o / i1i1I1IIii1II
def Iiii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo00ooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 5 - 5: ooOoO0O00 - OOooOOo - i1i1I1IIii1II + Ii
def oOoo0O0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 90 - 90: o0ii1I / Iii
def o0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoII1ii1iI1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 43 - 43: o0o00Oo0O + OOooOOo / III1iiIii
def iii1iIIi1ii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1iIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 34 - 34: ii
def Iii1IiII1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiiII1II1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
def OOoo0OoOooo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoOoO000O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 100 - 100: i1iIi + i1IiiiI1iI
def Ii1I1iIiIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0oOooOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 54 - 54: IiI1i11I . oO0o . iI11I1II1I1I
def iIiiiI1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIi1I1i1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 86 - 86: Iii % i1IiiiI1iI . Iii * III1iiIii + III1iiIii + IIiIiII11i
def oOOoI1iiI1iiI1i1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiO00Oooo0o000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 42 , i1oOOoo0o0OOOO , i11I , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 73 - 73: IIiIiII11i - IIiIiII11i + I11i * ooOoO0O00
def oO00oooOOoOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOo0o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for IiIi11iI , url , i1oOOoo0o0OOOO , i11I , I1iiiiii in IIi :
  I1I1II1I11 ( IiIi11iI , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , I1iiiiii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 41 - 41: oooOo0oo0oo - III1iiIii + IIiIiII11i - III1iiIii * III1iiIii
 if 60 - 60: i1iIi
 if 92 - 92: o0o00Oo0O % III1iiIii
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
 if 1 - 1: oOo0O0Ooo
 if 40 - 40: I11i % Iii % o0o00Oo0O
 if 88 - 88: I11i - i1i1I1IIii1II
 if 73 - 73: IIiIiII11i
 if 7 - 7: o0o00Oo0O / oO0o
def OOoOo0oO0oo00 ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( o0 ) :
     o0oOoOoooO = 0
     o0oOoOoooO += len ( oOo0O0 )
     if o0oOoOoooO > 0 :
      for iiii111II in oOo0O0 :
       os . unlink ( os . path . join ( ooO0IIiIIiiiiiII1 , iiii111II ) )
  I1oo0Oo = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( I1oo0Oo )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 10 - 10: III1iiIii . oooOo0oo0oo % i1i1I1IIii1II + i1i1I1IIii1II % Iii / oO0o
 if 11 - 11: i1iIi + oO0o - Ii1I . IiI1i11I
 if 39 - 39: I11i % ii - o0o00Oo0O
 if 87 - 87: oOo0O0Ooo * ooOoO0O00 * I1ii11iIi11i / Ii1I - oO0o
 if 44 - 44: I1ii11iIi11i
 if 37 - 37: oooOo0oo0oo / o0ii1I
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
def oo0OoOO000O ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
def OoOOo ( url ) :
 oOo0Ooo = os . path . join ( oooOOOOO , 'addon_data' )
 Ii1III1 = [
 ( oOo0Ooo ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOo0Ooo , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0Ooo , 'plugin.video.itv' , 'Images' ) ) ]
 if 85 - 85: ooOoO0O00 % IiI1i11I * o0ii1I * OOooOOo
 O0OiI1i1iIii1 = 0
 if 72 - 72: oooOo0oo0oo / OOooOOo
 for I1I1I1IIi1III in Ii1III1 :
  if os . path . exists ( I1I1I1IIi1III ) and not I1I1I1IIi1III in [ oo0o0O00 , oOo0Ooo ] :
   for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( I1I1I1IIi1III ) :
    o0oOoOoooO = 0
    o0oOoOoooO += len ( oOo0O0 )
    if o0oOoOoooO > 0 :
     for iiii111II in oOo0O0 :
      if not iiii111II in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( ooO0IIiIIiiiiiII1 , iiii111II ) )
       except :
        pass
      else : i11i1 ( 'Ignore Log File: %s' % iiii111II )
     for iIIII1iII1i in O0o0oOooOoo :
      try :
       shutil . rmtree ( os . path . join ( ooO0IIiIIiiiiiII1 , iIIII1iII1i ) )
       O0OiI1i1iIii1 += 1
       i11i1 ( "[Success] cleared %s files from %s" % ( str ( o0oOoOoooO ) , os . path . join ( I1I1I1IIi1III , iIIII1iII1i ) ) )
      except :
       i11i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I1I1I1IIi1III , iIIII1iII1i ) )
  else :
   for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( I1I1I1IIi1III ) :
    for iIIII1iII1i in O0o0oOooOoo :
     if 'cache' in iIIII1iII1i . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooO0IIiIIiiiiiII1 , iIIII1iII1i ) )
       O0OiI1i1iIii1 += 1
       i11i1 ( "[Success] wiped %s " % os . path . join ( I1I1I1IIi1III , iIIII1iII1i ) )
      except :
       i11i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I1I1I1IIi1III , iIIII1iII1i ) )
       if 89 - 89: oooOo0oo0oo + oooOo0oo0oo * OOooOOo + IiI1i11I % i1IiiiI1iI % i1IiiiI1iI
 oo0OoOO000O ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % O0OiI1i1iIii1 )
 if 68 - 68: I1ii11iIi11i + oO0o % oO0o % OOooOOo
 if 30 - 30: I1ii11iIi11i % ii * Ii % i1i1I1IIii1II
 if 37 - 37: IiI1i11I
 if 29 - 29: oooOo0oo0oo
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
def III11iI1i11i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 ooI111I11iiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( ooI111I11iiI ) :
   o0oOoOoooO = 0
   o0oOoOoooO += len ( oOo0O0 )
   if 72 - 72: i1i1I1IIii1II * Ii1I . OOooOOo
   if 10 - 10: III1iiIii / I11i
   if o0oOoOoooO > 0 :
    if 42 - 42: oooOo0oo0oo * ii / o0o00Oo0O * i1iIi
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o0oOoOoooO ) + " files found" , "Do you want to delete them?" ) :
     if 50 - 50: oooOo0oo0oo
     for iiii111II in oOo0O0 :
      os . unlink ( os . path . join ( ooO0IIiIIiiiiiII1 , iiii111II ) )
     for iIIII1iII1i in O0o0oOooOoo :
      shutil . rmtree ( os . path . join ( ooO0IIiIIiiiiiII1 , iIIII1iII1i ) )
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
 if 43 - 43: I11i
 if 32 - 32: III1iiIii / i1iIi * iI11I1II1I1I + Ii
 if 82 - 82: oooOo0oo0oo % I1ii11iIi11i . oOo0O0Ooo . o0ii1I % oOo0O0Ooo
 if 59 - 59: ooOoO0O00 + III1iiIii . oooOo0oo0oo + Iii
 if 88 - 88: ooOoO0O00 / IiI1i11I * I1ii11iIi11i * IiI1i11I % ooOoO0O00
 if 2 - 2: Ii . IiI1i11I . o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . III1iiIii
 if 54 - 54: I11i
 if 99 - 99: IIiIiII11i % oOo0O0Ooo
 if 89 - 89: oooOo0oo0oo / ooOoO0O00 - Iii * i1i1I1IIii1II
def I1II1I11I1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 ooI111I11iiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( ooI111I11iiI ) :
   o0oOoOoooO = 0
   o0oOoOoooO += len ( oOo0O0 )
   if 42 - 42: o0ii1I
   if 40 - 40: I11i - iI11I1II1I1I % i1i1I1IIii1II . I11i
   if o0oOoOoooO > 0 :
    if 35 - 35: oOo0O0Ooo % oooOo0oo0oo + OOooOOo / oOo0O0Ooo . o0o00Oo0O % IiI1i11I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o0oOoOoooO ) + " files found" , "Do you want to delete them?" ) :
     if 100 - 100: oOo0O0Ooo
     for iiii111II in oOo0O0 :
      os . unlink ( os . path . join ( ooO0IIiIIiiiiiII1 , iiii111II ) )
     for iIIII1iII1i in O0o0oOooOoo :
      shutil . rmtree ( os . path . join ( ooO0IIiIIiiiiiII1 , iIIII1iII1i ) )
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
 OoOOo ( url )
 return
 if 55 - 55: ooOoO0O00 % III1iiIii
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
 if 74 - 74: Iii . OOooOOo + OOooOOo
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
 if 93 - 93: oO0o . oO0o
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
 if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
 if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
 if 55 - 55: i1iIi - I11i
def I1i1i1IIII1i1 ( url , name ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0 = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 oOo0oo0o0O0O = os . path . join ( oOOooOoo , 'advancedsettings.xml.bak' )
 if os . path . exists ( oOo0oo0o0O0O ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoOoo0 = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
   try :
    os . remove ( OoOoo0 )
    print '=== GenieTv - REMOVING    ' + str ( OoOoo0 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   i11I1iIii1i11 = open ( OoOoo0 , "w" )
   i11I1iIii1i11 . write ( iiI111I1iIiI )
   i11I1iIii1i11 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoOoo0 = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
  try :
   os . remove ( OoOoo0 )
   print '=== GenieTv - REMOVING    ' + str ( OoOoo0 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i11I1iIii1i11 = open ( OoOoo0 , "w" )
  i11I1iIii1i11 . write ( iiI111I1iIiI )
  i11I1iIii1i11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 47 - 47: ooOoO0O00
def ii1io0ooO0OO ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0 = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 try :
  i11I1iIii1i11 = open ( OoOoo0 ) . read ( )
  if 'zero' in i11I1iIii1i11 :
   name = '0CACHE'
  elif 'tuxen' in i11I1iIii1i11 :
   name = 'TUXENS'
  elif 'muckys' in i11I1iIii1i11 :
   name = 'MUCKYS'
  elif 'p2p1' in i11I1iIii1i11 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i11I1iIii1i11 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i11I1iIii1i11 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 35 - 35: III1iiIii . ooOoO0O00 + Ii1I . III1iiIii + i1iIi . i1i1I1IIii1II
def iiI1i ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0 = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 try :
  os . remove ( OoOoo0 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoOoo0 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 71 - 71: OOooOOo + i1i1I1IIii1II % oooOo0oo0oo * oOo0O0Ooo
 if 89 - 89: o0ii1I % i1IiiiI1iI / I1ii11iIi11i * o0ii1I + OOooOOo
 if 5 - 5: o0ii1I * oOo0O0Ooo + i1IiiiI1iI
 if 22 - 22: I1ii11iIi11i . oO0o
 if 55 - 55: I1ii11iIi11i % ii * IIiIiII11i % ii
 if 30 - 30: i1IiiiI1iI / I11i + ii + OOooOOo + oO0o
 if 40 - 40: ii / III1iiIii
 if 82 - 82: Ii - i1i1I1IIii1II - ooOoO0O00
 if 78 - 78: i1i1I1IIii1II % IiI1i11I / ooOoO0O00 / i1iIi
 if 44 - 44: I11i + o0ii1I + oOo0O0Ooo % o0o00Oo0O
def IIiI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for III1IIIIIiiI , ooO0i111I , oOo0oO000oOo , iiii1i1iiIiI1 in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % III1IIIIIiiI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOo0oO000oOo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iiii1i1iiIiI1 )
  inc = inc + 1
  if 14 - 14: oooOo0oo0oo / ooOoO0O00 % ooOoO0O00
  if 50 - 50: ii % Iii % iI11I1II1I1I . Ii1I - III1iiIii / oO0o
  if 19 - 19: Ii1I / I1ii11iIi11i * ii
  if 67 - 67: o0o00Oo0O
  if 37 - 37: Iii / I1ii11iIi11i
  if 30 - 30: o0ii1I / o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
  if 35 - 35: ooOoO0O00 % Ii + o0ii1I
  if 14 - 14: oO0o * ii
  if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
def O00oo0ooo0O ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoo0 = os . path . join ( oOOooOoo , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i11I1iIii1i11 = open ( OoOoo0 , "w" )
  i11I1iIii1i11 . write ( iiI111I1iIiI )
  i11I1iIii1i11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 40 - 40: i1i1I1IIii1II
def I1ioOo00oooO ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoo0 = os . path . join ( oOOooOoo , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i11I1iIii1i11 = open ( OoOoo0 , "w" )
  i11I1iIii1i11 . write ( iiI111I1iIiI )
  i11I1iIii1i11 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 60 - 60: IiI1i11I
 if 92 - 92: ooOoO0O00 + i1IiiiI1iI % ooOoO0O00 * IiI1i11I % I11i
def OO0OO ( ) :
 try :
  iII1ii1iiI1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iII1ii1iiI1 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ii1iiii1I = os . path . join ( iII1ii1iiI1 , "source.db" )
    os . unlink ( ii1iiii1I )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 71 - 71: III1iiIii / i1IiiiI1iI + Ii . oooOo0oo0oo
 if 16 - 16: iI11I1II1I1I + oOo0O0Ooo - oooOo0oo0oo + oooOo0oo0oo . iI11I1II1I1I + i1IiiiI1iI
 if 96 - 96: ooOoO0O00 * iI11I1II1I1I . oooOo0oo0oo + o0o00Oo0O . I11i
 if 23 - 23: Ii1I . Ii1I / oOo0O0Ooo . ooOoO0O00
 if 47 - 47: Ii . I11i . Ii + oOo0O0Ooo - Ii1I
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 62 - 62: ii + oOo0O0Ooo / i1iIi . o0ii1I . I1ii11iIi11i
 if 81 - 81: i1i1I1IIii1II + III1iiIii
 if 75 - 75: o0o00Oo0O + Ii1I
 if 51 - 51: ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
 if 30 - 30: Iii
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
def O0o0O0 ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; iiiiiI = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iiiiiI :
  ooOoOO0Oo0oO0o = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; ooOoOO0Oo0oO0o = xbmc . translatePath ( ooOoOO0Oo0oO0o ) ;
  oOo0 = os . path . join ( ooOoOO0Oo0oO0o , ".." , ".." ) ; oOo0 = os . path . abspath ( oOo0 ) ; pluginlog ( "freshstart.main_list xbmcPath=" + oOo0 ) ; oOoooo0 = False
  try :
   for ooO0IIiIIiiiiiII1 , O0o0oOooOoo , oOo0O0 in os . walk ( oOo0 , topdown = True ) :
    O0o0oOooOoo [ : ] = [ iIIII1iII1i for iIIII1iII1i in O0o0oOooOoo if iIIII1iII1i not in o0oO0 ]
    for IiIi11iI in oOo0O0 :
     try : os . remove ( os . path . join ( ooO0IIiIIiiiiiII1 , IiIi11iI ) )
     except :
      if IiIi11iI not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oOoooo0 = True
      pluginlog ( "Error removing " + ooO0IIiIIiiiiiII1 + " " + IiIi11iI )
    for IiIi11iI in O0o0oOooOoo :
     try : os . rmdir ( os . path . join ( ooO0IIiIIiiiiiII1 , IiIi11iI ) )
     except :
      if IiIi11iI not in [ "Database" , "userdata" ] : oOoooo0 = True
      pluginlog ( "Error removing " + ooO0IIiIIiiiiiII1 + " " + IiIi11iI )
   if not oOoooo0 : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 o0OOOoO0O ( )
 if 79 - 79: OOooOOo * IIiIiII11i + o0ii1I + oooOo0oo0oo % oOo0O0Ooo * ii
 if 46 - 46: iI11I1II1I1I . o0ii1I % o0ii1I - oOo0O0Ooo
 if 26 - 26: iI11I1II1I1I - oOo0O0Ooo + IiI1i11I
def ooO0o0O ( ) :
 iIIiI11 = [ ]
 iIi1Ii1ii1 = sys . argv [ 2 ]
 if len ( iIi1Ii1ii1 ) >= 2 :
  Ii1II1I11i1 = sys . argv [ 2 ]
  OOooO = Ii1II1I11i1 . replace ( '?' , '' )
  if ( Ii1II1I11i1 [ len ( Ii1II1I11i1 ) - 1 ] == '/' ) :
   Ii1II1I11i1 = Ii1II1I11i1 [ 0 : len ( Ii1II1I11i1 ) - 2 ]
  iii1i1i1IiiI11i = OOooO . split ( '&' )
  iIIiI11 = { }
  for iii1II11II1 in range ( len ( iii1i1i1IiiI11i ) ) :
   ooII11iI1i = { }
   ooII11iI1i = iii1i1i1IiiI11i [ iii1II11II1 ] . split ( '=' )
   if ( len ( ooII11iI1i ) ) == 2 :
    iIIiI11 [ ooII11iI1i [ 0 ] ] = ooII11iI1i [ 1 ]
    if 3 - 3: i1i1I1IIii1II + oO0o - IiI1i11I / o0ii1I
 return iIIiI11
 if 58 - 58: o0ii1I * Iii
oOoooo0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
oOoOII1i1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIIIII1iI1II = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOiIiIII1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iIIII1I1I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iIII11I1IiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
Oo00ooO0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o0oi11I1IIi11II = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1i1II = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OoII1ii1iI1111 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iI1iIII = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iiiII1II1i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OoOoO000O0O = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0oOooOoOo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IiIi1I1i1iII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiO00Oooo0o000 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iiIioo0O0O = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
O0Oo0ooO0OO00 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOoO00OoOOO = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IiI1iI1IiiIi1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oooiI1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
ii11i1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oOo0o0O = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iiIiooOo0oo0O0O = base64 . decodestring ( 'Q1VOVA==' )
def i1Ii11ii ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 i1iiIIIi . setProperty ( 'fanart_image' , fanart )
 i1iiIIIi . setProperty ( "IsPlayable" , "true" )
 oOo0Oo0o0 = [ ]
 oOo0Oo0o0 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 oOo0Oo0o0 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i1iiIIIi . addContextMenuItems ( oOo0Oo0o0 , replaceItems = True )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = False )
 return o0iIiiIiiIi
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = True )
 return o0iIiiIiiIi
 if 72 - 72: o0o00Oo0O * i1IiiiI1iI - iI11I1II1I1I % ooOoO0O00
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 o0oOOo0OooOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0iIiiIiiIi = True
 i1iiIIIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1iiIIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1iiIIIi . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II11i111i1iIiiIiI = [ ]
  if showcontext == 'fav' :
   II11i111i1iIiiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II11i111i1iIiiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1iiIIIi . addContextMenuItems ( II11i111i1iIiiIiI )
 o0iIiiIiiIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0oOOo0OooOo , listitem = i1iiIIIi , isFolder = False )
 return o0iIiiIiiIi
 if 83 - 83: OOooOOo + oooOo0oo0oo / ii
 if 39 - 39: oO0o % IiI1i11I . i1i1I1IIii1II . IIiIiII11i - Ii
Ii1II1I11i1 = ooO0o0O ( )
OoOOoOooooOOo = None
IiIi11iI = None
oo0oOO00oO = None
i1oOOoo0o0OOOO = None
i11I = None
I1iiiiii = None
iI1IiiiIiI1Ii = None
ooOoOoOoo = None
if 70 - 70: ooOoO0O00 % Ii1I - iI11I1II1I1I % IIiIiII11i + i1i1I1IIii1II % ii
if 92 - 92: iI11I1II1I1I * o0o00Oo0O % Iii - III1iiIii / o0o00Oo0O
try :
 ooOoOoOoo = int ( Ii1II1I11i1 [ "fav_mode" ] )
except :
 pass
 if 74 - 74: IIiIiII11i * oO0o + i1IiiiI1iI / i1iIi % oO0o % Ii
try :
 OoOOoOooooOOo = urllib . unquote_plus ( Ii1II1I11i1 [ "url" ] )
except :
 pass
try :
 IiIi11iI = urllib . unquote_plus ( Ii1II1I11i1 [ "name" ] )
except :
 pass
try :
 i1oOOoo0o0OOOO = urllib . unquote_plus ( Ii1II1I11i1 [ "iconimage" ] )
except :
 pass
try :
 oo0oOO00oO = int ( Ii1II1I11i1 [ "mode" ] )
except :
 pass
try :
 i11I = urllib . unquote_plus ( Ii1II1I11i1 [ "fanart" ] )
except :
 pass
try :
 I1iiiiii = urllib . unquote_plus ( Ii1II1I11i1 [ "description" ] )
except :
 pass
 if 70 - 70: IIiIiII11i - IiI1i11I / Iii
 if 56 - 56: I1ii11iIi11i . o0ii1I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oo0oOO00oO )
print "URL: " + str ( OoOOoOooooOOo )
print "Name: " + str ( IiIi11iI )
print "IconImage: " + str ( i1oOOoo0o0OOOO )
if 61 - 61: o0ii1I
if 48 - 48: oOo0O0Ooo - Ii * Ii1I
def Ii1IIiI1i ( content , viewType ) :
 if 70 - 70: Ii1I * OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 63 - 63: i1iIi . III1iiIii - OOooOOo % III1iiIii - i1IiiiI1iI / i1IiiiI1iI
if i1oOOoo0o0OOOO == None : i1oOOoo0o0OOOO = O0O
if i11I == None : i11I = Oo00OOOOO
if oo0oOO00oO == None :
 Iii1I1I11iiI1 ( )
 if 42 - 42: ooOoO0O00 . OOooOOo * OOooOOo * OOooOOo
elif oo0oOO00oO == 1 :
 oOoO0o0o ( OoOOoOooooOOo )
 if 14 - 14: IIiIiII11i / i1IiiiI1iI . oOo0O0Ooo
elif oo0oOO00oO == 44 :
 oOoooooOoO ( OoOOoOooooOOo )
 if 66 - 66: i1IiiiI1iI % i1i1I1IIii1II . IiI1i11I * ooOoO0O00
elif oo0oOO00oO == 2 :
 oO00O0o0oOOO ( )
 if 81 - 81: ii * oOo0O0Ooo / i1IiiiI1iI
elif oo0oOO00oO == 3 :
 oOO0O0ooOOOo ( )
 if 10 - 10: oOo0O0Ooo - IIiIiII11i / III1iiIii * IIiIiII11i
elif oo0oOO00oO == 21 :
 i1i1II ( )
 if 67 - 67: IIiIiII11i . o0ii1I % i1i1I1IIii1II . I1ii11iIi11i + III1iiIii
elif oo0oOO00oO == 4 :
 O0oooOOo0 ( )
 if 10 - 10: oooOo0oo0oo - oO0o * i1i1I1IIii1II / iI11I1II1I1I - OOooOOo
elif oo0oOO00oO == 5 :
 oOoO0 ( OoOOoOooooOOo )
 if 20 - 20: III1iiIii % oOo0O0Ooo + iI11I1II1I1I % IiI1i11I
elif oo0oOO00oO == 6 :
 III11iI1i11i ( OoOOoOooooOOo )
 if 100 - 100: I11i - I1ii11iIi11i % i1IiiiI1iI . Ii % ii
elif oo0oOO00oO == 7 :
 I1i1i1IIII1i1 ( OoOOoOooooOOo , IiIi11iI )
 if 39 - 39: Ii1I / Ii * ooOoO0O00 * I1ii11iIi11i
elif oo0oOO00oO == 8 :
 ii1io0ooO0OO ( OoOOoOooooOOo , IiIi11iI )
 if 39 - 39: oO0o * ii / ooOoO0O00 + I1ii11iIi11i
elif oo0oOO00oO == 9 :
 FIXREPOSADDONS ( OoOOoOooooOOo )
 if 57 - 57: o0o00Oo0O
elif oo0oOO00oO == 10 :
 OoOO0o ( )
 if 83 - 83: oooOo0oo0oo / o0ii1I * oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I
elif oo0oOO00oO == 11 :
 iiI1i ( OoOOoOooooOOo )
 if 1 - 1: Iii / ii / IiI1i11I
elif oo0oOO00oO == 12 :
 IIiI ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / Iii * I1ii11iIi11i
elif oo0oOO00oO == 13 :
 OOoOo0oO0oo00 ( )
 if 91 - 91: oO0o . IiI1i11I
elif oo0oOO00oO == 14 :
 OoOOo ( OoOOoOooooOOo )
 if 82 - 82: Ii1I / I1ii11iIi11i
elif oo0oOO00oO == 15 :
 ooOo0oO0O ( )
 if 63 - 63: oOo0O0Ooo
elif oo0oOO00oO == 16 :
 O00oo0ooo0O ( OoOOoOooooOOo , IiIi11iI )
 if 3 - 3: IiI1i11I + Ii1I
elif oo0oOO00oO == 17 :
 I1ioOo00oooO ( OoOOoOooooOOo , IiIi11iI )
 if 35 - 35: i1i1I1IIii1II * IiI1i11I * i1i1I1IIii1II * i1IiiiI1iI * III1iiIii * ooOoO0O00
elif oo0oOO00oO == 18 :
 OO0OO ( )
 if 43 - 43: oO0o * oOo0O0Ooo / III1iiIii . Ii + IiI1i11I + I11i
elif oo0oOO00oO == 19 :
 oo0OOO0OOoOO ( OoOOoOooooOOo )
 if 1 - 1: oOo0O0Ooo % I11i . i1IiiiI1iI + Iii * i1i1I1IIii1II
elif oo0oOO00oO == 40 :
 Oo0O0o00o00 ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
 if 41 - 41: oO0o * i1i1I1IIii1II - IIiIiII11i
elif oo0oOO00oO == 42 :
 O0000ooO0OO0Oooo0o ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
 if 2 - 2: III1iiIii + III1iiIii - oO0o * IiI1i11I . i1i1I1IIii1II
elif oo0oOO00oO == 43 :
 oo0OoO ( OoOOoOooooOOo )
 if 91 - 91: i1iIi
elif oo0oOO00oO == 20 :
 O00o0O0oo ( OoOOoOooooOOo )
 if 22 - 22: i1iIi % oO0o * OOooOOo + I1ii11iIi11i
elif oo0oOO00oO == 22 :
 Iiii ( OoOOoOooooOOo )
 if 44 - 44: o0o00Oo0O - Iii
elif oo0oOO00oO == 23 :
 oOoo0O0o ( OoOOoOooooOOo )
 if 43 - 43: o0o00Oo0O
elif oo0oOO00oO == 24 :
 o0OO ( OoOOoOooooOOo )
 if 50 - 50: Iii - ii
elif oo0oOO00oO == 25 :
 iii1iIIi1ii ( OoOOoOooooOOo )
 if 29 - 29: i1i1I1IIii1II * i1i1I1IIii1II
elif oo0oOO00oO == 26 :
 Iii1IiII1 ( OoOOoOooooOOo )
 if 44 - 44: i1iIi . oOo0O0Ooo * i1i1I1IIii1II * o0ii1I
elif oo0oOO00oO == 27 :
 OOoo0OoOooo ( OoOOoOooooOOo )
 if 41 - 41: ooOoO0O00 % Ii + Iii % ii / Ii1I
elif oo0oOO00oO == 28 :
 Ii1I1iIiIi ( OoOOoOooooOOo )
 if 8 - 8: ii - oO0o / Ii / o0o00Oo0O . III1iiIii
elif oo0oOO00oO == 29 :
 iIiiiI1 ( OoOOoOooooOOo )
 if 86 - 86: i1iIi * ii + IiI1i11I + I11i
elif oo0oOO00oO == 30 :
 III1IIi1iiiI11I1i ( OoOOoOooooOOo )
 if 79 - 79: ooOoO0O00 % Ii1I - oO0o % Ii1I
elif oo0oOO00oO == 31 :
 oOOoI1iiI1iiI1i1I ( OoOOoOooooOOo )
 if 6 - 6: I1ii11iIi11i / IiI1i11I . Ii
elif oo0oOO00oO == 32 :
 iIO0oOoo00Oo0O ( )
 if 8 - 8: Ii1I + o0o00Oo0O - i1i1I1IIii1II % IIiIiII11i . i1IiiiI1iI
elif oo0oOO00oO == 33 :
 Iii1i1Ii ( )
 if 86 - 86: III1iiIii
elif oo0oOO00oO == 35 :
 iiIII1i1 ( OoOOoOooooOOo )
 if 71 - 71: o0ii1I - ooOoO0O00 . oOo0O0Ooo
elif oo0oOO00oO == 34 :
 III1iIii ( OoOOoOooooOOo )
 if 15 - 15: ooOoO0O00 % IIiIiII11i / IIiIiII11i - Ii1I - Iii % ooOoO0O00
elif oo0oOO00oO == 36 :
 iI1I1 ( OoOOoOooooOOo )
 if 54 - 54: ooOoO0O00 . oO0o + IiI1i11I + oO0o * ooOoO0O00
elif oo0oOO00oO == 37 :
 o0oo0o ( OoOOoOooooOOo )
 if 13 - 13: I1ii11iIi11i / oO0o + oooOo0oo0oo
elif oo0oOO00oO == 38 :
 O00O0 ( OoOOoOooooOOo )
 if 90 - 90: oO0o * Ii / i1i1I1IIii1II
elif oo0oOO00oO == 41 :
 O0o0O0 ( Ii1II1I11i1 )
 if 91 - 91: IiI1i11I - OOooOOo / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / I11i
elif oo0oOO00oO == 39 :
 oO00oooOOoOo0 ( OoOOoOooooOOo )
 if 34 - 34: oO0o * IIiIiII11i + Ii % o0ii1I
elif oo0oOO00oO == 45 :
 TEXTS ( )
 if 25 - 25: OOooOOo + III1iiIii . Ii
elif oo0oOO00oO == 46 :
 oOo0O ( )
 if 87 - 87: oOo0O0Ooo + ii + o0o00Oo0O
elif oo0oOO00oO == 47 :
 GEVID ( )
 if 32 - 32: o0ii1I / Ii1I . o0ii1I
elif oo0oOO00oO == 48 :
 III1Ii11i1II ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
 if 65 - 65: III1iiIii
elif oo0oOO00oO == 49 :
 iiI11Iii ( )
 if 74 - 74: I1ii11iIi11i + ooOoO0O00 - IIiIiII11i / i1iIi / IiI1i11I
elif oo0oOO00oO == 22222 :
 Ii11iIII ( OoOOoOooooOOo )
 if 66 - 66: i1iIi / III1iiIii * iI11I1II1I1I
elif oo0oOO00oO == 222225 :
 i1iI1 ( OoOOoOooooOOo )
 if 42 - 42: i1IiiiI1iI - Ii % IIiIiII11i * i1iIi . o0o00Oo0O % Iii
elif oo0oOO00oO == 222 :
 i1Ii1Ii1 ( OoOOoOooooOOo )
 if 82 - 82: I1ii11iIi11i % o0o00Oo0O + Ii1I % Ii1I
elif oo0oOO00oO == 2222222 :
 ooOoO00 ( OoOOoOooooOOo )
 if 74 - 74: o0o00Oo0O * III1iiIii . Iii - i1IiiiI1iI + o0o00Oo0O + Iii
elif oo0oOO00oO == 222222 :
 o00O ( OoOOoOooooOOo , IiIi11iI )
 if 48 - 48: i1i1I1IIii1II . I11i - oooOo0oo0oo
elif oo0oOO00oO == 333 :
 oOoOoo0OOOo0 ( OoOOoOooooOOo )
 if 29 - 29: I1ii11iIi11i - o0ii1I - I1ii11iIi11i
 if 89 - 89: I1ii11iIi11i . oO0o . Ii1I * i1i1I1IIii1II . o0o00Oo0O
elif oo0oOO00oO == 1020 :
 IIiIII ( )
 if 72 - 72: Ii % Iii / i1IiiiI1iI + oOo0O0Ooo * IiI1i11I
elif oo0oOO00oO == 1021 :
 ANIMEEP ( )
 if 69 - 69: i1IiiiI1iI + o0o00Oo0O . III1iiIii . I11i
elif oo0oOO00oO == 1022 :
 ANIMEPLAY ( OoOOoOooooOOo )
 if 38 - 38: III1iiIii / ooOoO0O00
elif oo0oOO00oO == 1001 :
 i11i1i ( )
 if 60 - 60: OOooOOo
elif oo0oOO00oO == 1005 :
 oo00OoO00o ( )
 if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
elif oo0oOO00oO == 1007 :
 II1Oooo00oO0OO0o ( OoOOoOooooOOo )
 if 61 - 61: III1iiIii . III1iiIii
elif oo0oOO00oO == 1010 :
 o0oo00OOOo ( OoOOoOooooOOo )
 if 17 - 17: OOooOOo % I1ii11iIi11i / i1IiiiI1iI . o0ii1I % oO0o
elif oo0oOO00oO == 1011 :
 oOoOO0o ( OoOOoOooooOOo )
 if 32 - 32: oOo0O0Ooo + i1iIi / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
elif oo0oOO00oO == 1012 :
 OoOO000oo0 ( OoOOoOooooOOo )
 if 95 - 95: IiI1i11I / i1iIi + i1IiiiI1iI
elif oo0oOO00oO == 1030 :
 OOoOo ( )
 if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - III1iiIii
elif oo0oOO00oO == 1031 :
 i1iiii11iIIiiI1I ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
 if 81 - 81: Ii1I
elif oo0oOO00oO == 1032 :
 IIIiI1iIIII ( OoOOoOooooOOo )
 if 31 - 31: o0o00Oo0O % i1iIi / oOo0O0Ooo * IiI1i11I % iI11I1II1I1I * OOooOOo
elif oo0oOO00oO == 1006 :
 Parse . ParseURL ( OoOOoOooooOOo )
 if 76 - 76: i1IiiiI1iI - o0o00Oo0O
elif oo0oOO00oO == 2030 :
 Parse . addonParseURL ( OoOOoOooooOOo )
 if 23 - 23: o0o00Oo0O * o0ii1I * i1iIi % i1iIi
elif oo0oOO00oO == 2031 :
 Parse . apkParseURL ( OoOOoOooooOOo )
 if 7 - 7: IIiIiII11i + Iii
elif oo0oOO00oO == 2032 :
 Parse . ParseBOSS ( OoOOoOooooOOo )
 if 99 - 99: iI11I1II1I1I * i1i1I1IIii1II
elif oo0oOO00oO == 1002 :
 OoOoO0OoO ( OoOOoOooooOOo )
 if 37 - 37: i1iIi * IiI1i11I * Iii
elif oo0oOO00oO == 1003 :
 o0o0O ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
 if 11 - 11: oOo0O0Ooo
elif oo0oOO00oO == 1004 :
 IIIIii1Ii11i ( OoOOoOooooOOo )
 if 48 - 48: o0o00Oo0O . Iii
elif oo0oOO00oO == 1008 :
 Oo000O0Oo0Oo ( )
 if 9 - 9: i1i1I1IIii1II / I1ii11iIi11i
elif oo0oOO00oO == 1009 :
 iIIiii ( OoOOoOooooOOo )
 if 85 - 85: Ii / oOo0O0Ooo . oO0o . Iii . i1i1I1IIii1II * III1iiIii
elif oo0oOO00oO == 2001 :
 oo000O ( )
 if 41 - 41: o0ii1I / oO0o / oO0o * Iii
elif oo0oOO00oO == 2002 :
 O0o000 ( OoOOoOooooOOo )
 if 31 - 31: o0ii1I / ii % iI11I1II1I1I - III1iiIii * oOo0O0Ooo - o0o00Oo0O
elif oo0oOO00oO == 1013 :
 ooOooO ( )
elif oo0oOO00oO == 10111113 :
 I11i1I1 ( OoOOoOooooOOo )
 if 31 - 31: i1i1I1IIii1II
elif oo0oOO00oO == 1014 :
 OoOooOO ( )
 if 74 - 74: oO0o
elif oo0oOO00oO == 1015 :
 IiI11i1 ( OoOOoOooooOOo )
 if 11 - 11: i1i1I1IIii1II + o0o00Oo0O % o0ii1I . Iii * I11i
elif oo0oOO00oO == 1016 :
 I1iIiI11I1 ( OoOOoOooooOOo , i1oOOoo0o0OOOO , IiIi11iI )
 if 14 - 14: Iii . iI11I1II1I1I + i1IiiiI1iI % ii
elif oo0oOO00oO == 1017 :
 OooO0ooo0o ( )
 if 9 - 9: i1i1I1IIii1II + o0ii1I / Ii1I * iI11I1II1I1I + I11i
elif oo0oOO00oO == 1018 :
 i1IiII1III ( OoOOoOooooOOo )
 if 64 - 64: Iii % Ii % Ii1I
elif oo0oOO00oO == 1019 :
 OOo0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 10190 :
 ii1iiIi1 ( OoOOoOooooOOo )
 if 14 - 14: i1IiiiI1iI - OOooOOo - Ii1I % Iii + ii
elif oo0oOO00oO == 1023 :
 OO0O00 ( )
 if 4 - 4: i1IiiiI1iI - oOo0O0Ooo / iI11I1II1I1I + Ii1I % iI11I1II1I1I * oOo0O0Ooo
elif oo0oOO00oO == 1024 :
 Ooo0oo0oO000 ( OoOOoOooooOOo )
 if 30 - 30: Ii % oooOo0oo0oo
elif oo0oOO00oO == 1025 :
 iI11i11iI ( OoOOoOooooOOo )
 if 52 - 52: Iii - i1i1I1IIii1II . Ii - IIiIiII11i + o0ii1I . IiI1i11I
elif oo0oOO00oO == 4001 :
 II1IIiiIiI ( )
 if 27 - 27: oOo0O0Ooo + OOooOOo + IiI1i11I
elif oo0oOO00oO == 4002 :
 O0oO0OOoOOO0oO ( )
 if 70 - 70: Iii + III1iiIii . i1iIi - Ii1I
elif oo0oOO00oO == 4003 :
 OOoOo0O0 ( )
 if 34 - 34: ooOoO0O00 % I1ii11iIi11i . i1i1I1IIii1II
elif oo0oOO00oO == 4004 :
 i1i1I111iIi1 ( )
 if 36 - 36: Ii1I / i1IiiiI1iI - III1iiIii + oooOo0oo0oo + i1IiiiI1iI
elif oo0oOO00oO == 4005 :
 o0ooO ( )
 if 62 - 62: I1ii11iIi11i . oO0o * i1IiiiI1iI . Ii * o0o00Oo0O
elif oo0oOO00oO == 4006 :
 Ii1ii111i1 ( )
 if 10 - 10: I1ii11iIi11i / OOooOOo * oooOo0oo0oo - III1iiIii + o0ii1I
elif oo0oOO00oO == 4007 :
 iii11i1IIII ( )
 if 62 - 62: oOo0O0Ooo . o0ii1I
elif oo0oOO00oO == 4008 :
 iiI1Ii1 ( )
 if 74 - 74: o0ii1I - Iii % i1iIi - oOo0O0Ooo - o0ii1I - IIiIiII11i
elif oo0oOO00oO == 40099 : I1 ( )
elif oo0oOO00oO == 4009 : Oo0O0oo ( )
elif oo0oOO00oO == 4010 : IiiiIIIi11ii1 ( )
elif oo0oOO00oO == 3000 :
 Iii11Ii ( )
 if 81 - 81: ooOoO0O00 * Ii1I + III1iiIii - oO0o * ooOoO0O00
elif oo0oOO00oO == 3001 :
 oo00oo0 ( )
 if 6 - 6: iI11I1II1I1I % OOooOOo % IIiIiII11i % I11i
elif oo0oOO00oO == 3002 :
 i11iiiiiIi1 ( OoOOoOooooOOo )
 if 52 - 52: o0ii1I - oOo0O0Ooo * iI11I1II1I1I % I1ii11iIi11i * oooOo0oo0oo
elif oo0oOO00oO == 3003 :
 OoIiii1i11I1iII ( OoOOoOooooOOo )
 if 67 - 67: ii * Iii * o0ii1I * iI11I1II1I1I
elif oo0oOO00oO == 3004 :
 oOO0o0OoO00OO00 ( OoOOoOooooOOo )
 if 22 - 22: oO0o / I11i
elif oo0oOO00oO == 404 :
 OO00OOOO00oOO ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO )
 if 35 - 35: i1IiiiI1iI / i1IiiiI1iI + I11i - i1i1I1IIii1II
elif oo0oOO00oO == 405 :
 i1Ii1IiiI ( OoOOoOooooOOo )
 if 40 - 40: OOooOOo - IIiIiII11i
elif oo0oOO00oO == 7030 :
 OoOooOo0 ( )
 if 29 - 29: oOo0O0Ooo - o0o00Oo0O
elif oo0oOO00oO == 7021 :
 i1IIiIiI11 ( IiIi11iI )
 if 36 - 36: oOo0O0Ooo * oOo0O0Ooo
elif oo0oOO00oO == 7022 :
 OOOO0oo0o0O ( IiIi11iI )
 if 79 - 79: i1IiiiI1iI - Iii
elif oo0oOO00oO == 7000 :
 I1iO0000 ( IiIi11iI , OoOOoOooooOOo , img )
 if 49 - 49: IIiIiII11i + o0o00Oo0O * i1iIi - I1ii11iIi11i
elif oo0oOO00oO == 7050 :
 oooo ( OoOOoOooooOOo )
 if 89 - 89: oOo0O0Ooo + Iii . i1i1I1IIii1II . IIiIiII11i + i1i1I1IIii1II / I1ii11iIi11i
elif oo0oOO00oO == 7051 :
 Ii1oo0O0OO ( OoOOoOooooOOo )
 if 32 - 32: oO0o % i1i1I1IIii1II * Ii1I + Iii / i1IiiiI1iI
elif oo0oOO00oO == 7052 :
 I11IiiI1 ( OoOOoOooooOOo )
 if 5 - 5: I11i + IiI1i11I / ii + o0ii1I . OOooOOo / i1i1I1IIii1II
elif oo0oOO00oO == 7053 :
 ooo0oO0o000O0 ( OoOOoOooooOOo )
 if 18 - 18: IIiIiII11i . I11i
elif oo0oOO00oO == 7054 :
 CoolPlay ( OoOOoOooooOOo )
 if 75 - 75: ii - I1ii11iIi11i
elif oo0oOO00oO == 7060 :
 iI1I11II1Iii1 ( )
 if 56 - 56: IIiIiII11i - Ii - i1i1I1IIii1II . I11i
elif oo0oOO00oO == 7061 :
 iIi1 ( OoOOoOooooOOo )
 if 4 - 4: ooOoO0O00
elif oo0oOO00oO == 7063 :
 O00O0oO ( OoOOoOooooOOo )
 if 91 - 91: III1iiIii . oO0o * o0ii1I / I11i
elif oo0oOO00oO == 7062 :
 i1Ii1 ( OoOOoOooooOOo )
 if 41 - 41: oOo0O0Ooo . oO0o / ooOoO0O00 . I1ii11iIi11i . i1i1I1IIii1II
elif oo0oOO00oO == 7064 :
 NATatozcat ( )
 if 44 - 44: IiI1i11I * Iii + Ii + ooOoO0O00 / III1iiIii * IIiIiII11i
elif oo0oOO00oO == 7067 :
 i1I1ii1iI1 ( OoOOoOooooOOo )
 if 58 - 58: oooOo0oo0oo
elif oo0oOO00oO == 7066 :
 NATatozA ( OoOOoOooooOOo )
 if 72 - 72: oO0o + oooOo0oo0oo - I1ii11iIi11i % i1iIi . III1iiIii
elif oo0oOO00oO == 7065 :
 OoI1Ii ( OoOOoOooooOOo )
 if 95 - 95: IiI1i11I % oooOo0oo0oo - III1iiIii - OOooOOo % I11i * o0o00Oo0O
elif oo0oOO00oO == 7070 :
 i1Ii1Ii ( )
 if 16 - 16: i1IiiiI1iI / I1ii11iIi11i
elif oo0oOO00oO == 7071 :
 DIZIlist ( OoOOoOooooOOo )
 if 48 - 48: I1ii11iIi11i / i1i1I1IIii1II + IiI1i11I % IiI1i11I
elif oo0oOO00oO == 7072 :
 DIZIpull ( OoOOoOooooOOo )
 if 9 - 9: Ii1I - I11i . I1ii11iIi11i + Ii1I . oooOo0oo0oo
elif oo0oOO00oO == 7073 :
 WATCHDIZI ( OoOOoOooooOOo )
 if 30 - 30: ii - iI11I1II1I1I / i1i1I1IIii1II * o0ii1I / o0ii1I
elif oo0oOO00oO == 7002 :
 i1IiOOO ( )
 if 52 - 52: OOooOOo - oO0o + oOo0O0Ooo + III1iiIii
elif oo0oOO00oO == 7003 :
 oooOOo0Oo0OO0O ( OoOOoOooooOOo )
 if 49 - 49: i1i1I1IIii1II / Iii - i1i1I1IIii1II
elif oo0oOO00oO == 7004 :
 iIIi1iiIIiIi1 ( OoOOoOooooOOo )
 if 31 - 31: OOooOOo + oOo0O0Ooo + Ii1I + Iii * IIiIiII11i % i1i1I1IIii1II
elif oo0oOO00oO == 7020 :
 OO0oO0ooOOOoO ( OoOOoOooooOOo )
 if 90 - 90: oooOo0oo0oo * iI11I1II1I1I / ooOoO0O00
elif oo0oOO00oO == 7001 :
 oOOoo ( )
 if 60 - 60: oooOo0oo0oo * i1IiiiI1iI . i1i1I1IIii1II
elif oo0oOO00oO == 7010 :
 Ii11i ( OoOOoOooooOOo )
 if 47 - 47: i1i1I1IIii1II % oooOo0oo0oo / oooOo0oo0oo % OOooOOo % i1IiiiI1iI / OOooOOo
elif oo0oOO00oO == 7011 :
 O0oo0O0OO0OOo ( OoOOoOooooOOo )
 if 51 - 51: oOo0O0Ooo . Iii - OOooOOo
elif oo0oOO00oO == 7012 :
 i1O0o00o0Oo ( OoOOoOooooOOo )
 if 10 - 10: I1ii11iIi11i * oooOo0oo0oo / III1iiIii . I11i
elif oo0oOO00oO == 7013 :
 cnfTVPlay2 ( OoOOoOooooOOo )
elif oo0oOO00oO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OoOOoOooooOOo )
elif oo0oOO00oO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OoOOoOooooOOo )
elif oo0oOO00oO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oo0oOO00oO == 7018 :
 OOo0O0Oo000OO ( )
elif oo0oOO00oO == 7019 :
 CNF_Studio_Indexer . List_Movies ( OoOOoOooooOOo )
elif oo0oOO00oO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OoOOoOooooOOo )
elif oo0oOO00oO == 7024 :
 CNF_Studio_Indexer . Box_Office ( OoOOoOooooOOo )
 if 97 - 97: o0ii1I . o0ii1I % IiI1i11I
elif oo0oOO00oO == 8000 :
 II1iIIII ( )
elif oo0oOO00oO == 8001 :
 Ii1i ( )
elif oo0oOO00oO == 8002 :
 O0oo0o00O0O ( )
elif oo0oOO00oO == 8003 :
 I11IIiii111I1 ( )
elif oo0oOO00oO == 8004 :
 i1ii ( )
elif oo0oOO00oO == 8005 :
 OOoO0OOO00 ( )
elif oo0oOO00oO == 8006 :
 I1iii1IiI11I11I ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 8030 :
 ooO00OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 8045 :
 IIiiii1I1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8046 :
 i11II ( OoOOoOooooOOo )
elif oo0oOO00oO == 8047 :
 OO00O0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 8048 :
 i111II ( OoOOoOooooOOo )
elif oo0oOO00oO == 8049 :
 i11iI1I1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 804900 :
 oooo00o00oO ( OoOOoOooooOOo )
elif oo0oOO00oO == 8020 :
 i1oO0OO0 ( )
elif oo0oOO00oO == 8021 :
 o0o0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 8022 :
 oooo0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 8023 :
 I1i1ii ( OoOOoOooooOOo )
elif oo0oOO00oO == 8040 :
 ii1i ( )
elif oo0oOO00oO == 8041 :
 o0oI1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8042 :
 IIIiIiII11Iii ( OoOOoOooooOOo )
elif oo0oOO00oO == 8043 :
 yt . PlayVideo ( OoOOoOooooOOo )
elif oo0oOO00oO == 8044 :
 O0oo0o0OoO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8060 :
 OOoo ( )
elif oo0oOO00oO == 8061 :
 i1OOO00oO0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 8064 :
 O0Oo0o000oO ( )
elif oo0oOO00oO == 8065 :
 OooOO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8070 :
 ii1iiI ( )
elif oo0oOO00oO == 8071 :
 i11ioo0oo0O0Oo0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 7080 :
 Oo0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 8090 :
 O0oI1iIiiIii ( )
elif oo0oOO00oO == 8091 :
 OOoOO00O ( OoOOoOooooOOo )
elif oo0oOO00oO == 8092 :
 o0o00O00Oo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8093 :
 II1iIiiiIiiII ( OoOOoOooooOOo )
elif oo0oOO00oO == 8081 :
 O00oo ( )
elif oo0oOO00oO == 8062 :
 ooO00OoO ( OoOOoOooooOOo )
elif oo0oOO00oO == 8063 :
 Iii1iIIi1iIii ( OoOOoOooooOOo )
elif oo0oOO00oO == 8050 :
 oO0iIiII111 ( )
elif oo0oOO00oO == 8051 :
 OO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8052 :
 iii111 ( OoOOoOooooOOo )
elif oo0oOO00oO == 8085 :
 iIiiIi11 ( )
elif oo0oOO00oO == 8086 :
 oOoOo ( OoOOoOooooOOo )
elif oo0oOO00oO == 8087 :
 ooOiiIII ( OoOOoOooooOOo )
elif oo0oOO00oO == 8088 :
 ii1I ( OoOOoOooooOOo , IiIi11iI )
elif oo0oOO00oO == 9000 :
 oOo00Oo0o00oo ( )
elif oo0oOO00oO == 1111 :
 oo0oO ( )
elif oo0oOO00oO == 9001 :
 oo00O00oO000o ( )
elif oo0oOO00oO == 9002 :
 OoOOOo0o0ooo ( )
elif oo0oOO00oO == 9003 :
 IiI1IIII ( )
elif oo0oOO00oO == 9004 :
 World1 ( )
elif oo0oOO00oO == 9005 :
 World2 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9006 :
 World3 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9007 :
 I1iI1iIIIii ( )
elif oo0oOO00oO == 9008 :
 I1iI ( OoOOoOooooOOo )
elif oo0oOO00oO == 9009 :
 I1IiiI1i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9010 :
 iIiI11i1i ( )
elif oo0oOO00oO == 9011 :
 i1I1I1IIIi11 ( OoOOoOooooOOo )
elif oo0oOO00oO == 50 :
 IIi1I1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9020 :
 champlist ( )
elif oo0oOO00oO == 9021 :
 iIIi1i1i1iI1I ( )
elif oo0oOO00oO == 9022 :
 O0o0O0000ooo0 ( )
elif oo0oOO00oO == 9023 :
 Iii1ii ( )
elif oo0oOO00oO == 9024 :
 ooOo00OOo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9030 :
 III1I1iiIiiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 9031 :
 i1ii1I1ii111I ( OoOOoOooooOOo )
elif oo0oOO00oO == 9032 :
 IIIi1ii1i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 9033 :
 oo0oOiII1IiI1I11i ( OoOOoOooooOOo )
elif oo0oOO00oO == 9034 :
 O00oO0 ( )
elif oo0oOO00oO == 7085 :
 oOo0Oo0OOoo00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 7086 :
 OoooOoo0Oooo ( OoOOoOooooOOo )
elif oo0oOO00oO == 7087 :
 o0OiI ( I1iiiiii )
elif oo0oOO00oO == 9666 :
 I1II1I11I1I ( OoOOoOooooOOo )
elif oo0oOO00oO == 10100 : iiiiiiiiiiIi ( )
elif oo0oOO00oO == 101001 : IiI1Ii ( OoOOoOooooOOo )
elif oo0oOO00oO == 10105 : ooOo0Oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 10106 : I11i1I111II1IiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 10104 : I1i11I1IiII1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10107 : oOO00o0oooOo0 ( )
elif oo0oOO00oO == 10103 : oo00O0oOo ( OoOOoOooooOOo )
elif oo0oOO00oO == 10108 : oo0i11Iiiiii11II ( OoOOoOooooOOo )
elif oo0oOO00oO == 10000 : Origin_Menu ( )
elif oo0oOO00oO == 10001 : i1II11II1 ( )
elif oo0oOO00oO == 10002 : i1i1iII1 ( )
elif oo0oOO00oO == 10003 : Oo0o0OOo0Oo0 ( )
elif oo0oOO00oO == 10004 : iIIIiIi1I1i ( OoOOoOooooOOo )
elif oo0oOO00oO == 10005 : oOOO0O0Ooo ( )
elif oo0oOO00oO == 10006 : o000oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 10007 : oO0IIi11IiiiI11i ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 10008 : ii11 ( )
elif oo0oOO00oO == 10009 : Ii1I11Ii1iI ( )
elif oo0oOO00oO == 10010 : OoO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10011 : OOOOo00oOOO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10012 : ooOoO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10113 : GRABG ( OoOOoOooooOOo , IiIi11iI )
elif oo0oOO00oO == 10109 : iIII1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10013 : oOoOo00o00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10014 : ii1IIIIi1 ( )
elif oo0oOO00oO == 10015 : ii1iIi111i1 ( )
elif oo0oOO00oO == 10016 : OooOoOOo0oO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10017 : o00oo00O0OoOo ( )
elif oo0oOO00oO == 10018 : I1IIII ( )
elif oo0oOO00oO == 10019 : I1I11i ( )
elif oo0oOO00oO == 10020 : iIo0O000O00o ( )
elif oo0oOO00oO == 10021 : Oo0OIIi ( )
elif oo0oOO00oO == 10022 : IiOoo0o0OO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10023 : iIIIII ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 10024 : i1i111I ( OoOOoOooooOOo )
elif oo0oOO00oO == 10025 : I1II ( )
elif oo0oOO00oO == 10026 : OOii ( )
elif oo0oOO00oO == 10027 : i1IIII11II1 ( )
elif oo0oOO00oO == 10028 : o0OOoo ( )
elif oo0oOO00oO == 10029 : i1IiI1I111iI1 ( )
elif oo0oOO00oO == 423 : O0ooO0oOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 426 : O00o0Oo0o0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10030 : Izle_Films ( )
elif oo0oOO00oO == 10031 : Latest_Izle_Movies ( )
elif oo0oOO00oO == 10032 : Izle_Genres ( )
elif oo0oOO00oO == 10033 : Izle_Pop_Movies ( )
elif oo0oOO00oO == 10034 : Izle_Boxsets ( )
elif oo0oOO00oO == 10035 : Izle_Search ( )
elif oo0oOO00oO == 10036 : Izle_Genres_Movie ( OoOOoOooooOOo )
elif oo0oOO00oO == 10037 : Izle_Boxset_single ( OoOOoOooooOOo )
elif oo0oOO00oO == 10038 : Izle_IFRAME ( )
elif oo0oOO00oO == 10039 : Izle_Boxsets_Next ( OoOOoOooooOOo )
elif oo0oOO00oO == 10040 : iiIi1IIiI ( )
elif oo0oOO00oO == 10041 : O0O0ooO0oO0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 10042 : oO0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 10043 : i1IIIi111111 ( )
elif oo0oOO00oO == 10044 : Iii11 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10045 : ii1IiIi1iIi ( IiIi11iI )
elif oo0oOO00oO == 10046 : ooO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10047 : Ii1111iI1i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10048 : Oo0o0OO0O0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 10049 : oOoOoOo0oOoOo ( OoOOoOooooOOo )
elif oo0oOO00oO == 10050 : II1 ( )
elif oo0oOO00oO == 10051 : i1i1111IIIii ( )
elif oo0oOO00oO == 10052 : ii11IiiiIi1iI ( )
elif oo0oOO00oO == 10053 : Addon ( OoOOoOooooOOo )
elif oo0oOO00oO == 10054 : II1iIiIiIIi ( OoOOoOooooOOo , IiIi11iI )
elif oo0oOO00oO == 10055 :
 i111iIi11Ii ( "addFavorite" )
 try :
  IiIi11iI = IiIi11iI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiIi11iI = IiIi11iI . split ( '  - ' ) [ 0 ]
 except :
  pass
 i11I111iII1i1 ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I , ooOoOoOoo )
elif oo0oOO00oO == 10056 :
 i111iIi11Ii ( "rmFavorite" )
 try :
  IiIi11iI = IiIi11iI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiIi11iI = IiIi11iI . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOO0oo0 ( IiIi11iI )
elif oo0oOO00oO == 10057 :
 i111iIi11Ii ( "getFavorites" )
 iiiIiIIiIiiii ( )
elif oo0oOO00oO == 10058 : OOOo0Oo0O ( )
elif oo0oOO00oO == 10059 : Donators_Guide ( )
elif oo0oOO00oO == 10060 : i1II1I1Iii1 ( )
elif oo0oOO00oO == 10061 : iIiiII1Ii1ii ( )
elif oo0oOO00oO == 10062 : I1IIIIiiI1i1 ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
elif oo0oOO00oO == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif oo0oOO00oO == 10064 : II1ii1Ii ( )
elif oo0oOO00oO == 10065 : IIIIiiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 10066 : O00o0000OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 10068 : oOoooo000Oo00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10069 : oO0o00oOOooO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10070 : iiI1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10071 : Genie_Watch ( )
elif oo0oOO00oO == 10072 : o0OOOOOo00 ( )
elif oo0oOO00oO == 10073 : iii1IiI1i ( OoOOoOooooOOo )
elif oo0oOO00oO == 10074 : I1I1i ( OoOOoOooooOOo )
elif oo0oOO00oO == 10075 : I111Iii1 ( i1oOOoo0o0OOOO , IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 10076 : IiiI1I ( OoOOoOooooOOo )
elif oo0oOO00oO == 10077 : I1iI11IiiI11i ( OoOOoOooooOOo )
elif oo0oOO00oO == 10078 : IIIIIi11111iiiII1I ( )
elif oo0oOO00oO == 10079 : Genie_Watch_Tv_Shows ( )
elif oo0oOO00oO == 10080 : Genie_Watch_Tv_Genre ( OoOOoOooooOOo )
elif oo0oOO00oO == 10081 : Genie_Watch_TV_PlayRun ( OoOOoOooooOOo )
elif oo0oOO00oO == 10082 : Genie_Watch_TV_Episodes ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 10083 : Genie_Watch_Tv_Recent ( OoOOoOooooOOo )
elif oo0oOO00oO == 10084 : I1ii ( )
elif oo0oOO00oO == 10085 : oo0OOo0 ( )
elif oo0oOO00oO == 10086 : O0 ( )
elif oo0oOO00oO == 20000 : II1IIIii ( )
elif oo0oOO00oO == 20001 : OOO000ooO0OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 20002 : OO0ooo0OOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 20003 : o00OOOoO000 ( OoOOoOooooOOo )
elif oo0oOO00oO == 20004 : oO0oOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 20005 : ooooo0oo0OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 21004 : IiI1i111IiIiIi1 ( )
elif oo0oOO00oO == 21005 : Ooii ( OoOOoOooooOOo )
elif oo0oOO00oO == 21006 : i11iII1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 21007 : OoOo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 21008 : II11Iiii ( OoOOoOooooOOo )
elif oo0oOO00oO == 21009 : ooooooo00o ( OoOOoOooooOOo )
elif oo0oOO00oO == 30000 : IiI1i1Ii1iiI1 ( )
elif oo0oOO00oO == 30001 : i1II1i1iiI1 ( )
elif oo0oOO00oO == 100121 : Resolve ( OoOOoOooooOOo )
elif oo0oOO00oO == 30003 : IIi1iiIIi1i ( )
elif oo0oOO00oO == 30004 : I1oooO00oOOooO ( OoOOoOooooOOo )
elif oo0oOO00oO == 30005 : IIIii111i ( OoOOoOooooOOo )
elif oo0oOO00oO == 30006 : iiii1i1 ( )
elif oo0oOO00oO == 30007 : oOOoOo0OoOO ( )
elif oo0oOO00oO == 30008 : oooooO0oO0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 30009 : ooOOO000O ( OoOOoOooooOOo )
elif oo0oOO00oO == 30010 : IiI1I1i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 30011 : I1iI1Ii11 ( )
elif oo0oOO00oO == 30012 : OOoo0ooOo000oo ( )
elif oo0oOO00oO == 30013 : oooooOOo0Oo ( )
elif oo0oOO00oO == 30014 : IIi1IIII ( )
elif oo0oOO00oO == 30015 : oOo0OOoO0ooOOoo ( OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I )
elif oo0oOO00oO == 30016 : IIiIi1II1IiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 30019 : O0oo0ooO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 30017 : IIi1iI ( OoOOoOooooOOo )
elif oo0oOO00oO == 30018 : oooOo0OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 30030 : OooOoo0Oo ( )
elif oo0oOO00oO == 30031 : I1IiiiiI1i1I ( )
elif oo0oOO00oO == 30032 : Iio00 ( )
elif oo0oOO00oO == 30033 : ooiiI1ii ( )
elif oo0oOO00oO == 30034 : ii1ii111I11I1 ( )
elif oo0oOO00oO == 30035 : IIIO00ooo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 30036 : iI1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 30037 : iIi1O00oOOO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 30038 : ooooOoo00 ( )
elif oo0oOO00oO == 30039 : OO0ooOOO0OOO ( )
elif oo0oOO00oO == 50000 : i1II1 ( )
elif oo0oOO00oO == 50001 : iIIIi11iIiIii ( )
elif oo0oOO00oO == 50002 : Oo0oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 50003 : Table_Menu ( I1iiiiii )
elif oo0oOO00oO == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oo0oOO00oO == 60001 : o0III11IiI ( )
elif oo0oOO00oO == 60002 : O0OIIII1i ( IiIi11iI )
elif oo0oOO00oO == 60003 : o0oo00O ( OoOOoOooooOOo )
elif oo0oOO00oO == 600033 : OoO ( OoOOoOooooOOo )
elif oo0oOO00oO == 60004 : I1IiiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 50004 : oO0o00oo0 ( )
elif oo0oOO00oO == 50005 : speedtest . runtest ( OoOOoOooooOOo )
elif oo0oOO00oO == 70001 : I1o0 ( )
elif oo0oOO00oO == 70002 : oOOo ( OoOOoOooooOOo )
elif oo0oOO00oO == 70003 : OOoOO00OO0O0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 70004 : oOoOOo0oO0OoO0O ( OoOOoOooooOOo )
elif oo0oOO00oO == 70005 : o0OOOoO ( OoOOoOooooOOo )
elif oo0oOO00oO == 70006 : ooo0 ( )
elif oo0oOO00oO == 50006 : o0OIiII ( i1 , i1111 )
elif oo0oOO00oO == 80000 : o0OOOoO0O ( )
elif oo0oOO00oO == 80001 : resolvefilmon ( OoOOoOooooOOo )
elif oo0oOO00oO == 80002 : O0oIii11IiiIi ( )
elif oo0oOO00oO == 80003 : oOOOO ( IiIi11iI , OoOOoOooooOOo , "None" )
elif oo0oOO00oO == 80004 : Iiiiii ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 80005 : i11iiI1111 ( )
elif oo0oOO00oO == 80006 : O00oO000Oo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 80007 : iIIiiIi ( OoOOoOooooOOo )
elif oo0oOO00oO == 80008 : i1I111II ( )
elif oo0oOO00oO == 80009 : OoOO0Ooo ( )
elif oo0oOO00oO == 80010 : oO000o0oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 80011 : I1I ( OoOOoOooooOOo )
elif oo0oOO00oO == 80012 : iIiiIi11iiI1 ( )
elif oo0oOO00oO == 90000 : Ooo00 ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 90001 : tools ( )
elif oo0oOO00oO == 90002 : Iiiiii111i1ii ( )
elif oo0oOO00oO == 90003 : i1I1II11I1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90004 : oo0oOoOoo ( OoOOoOooooOOo )
elif oo0oOO00oO == 90005 : O0oOoOooo00oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 90006 : oooo0oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 90007 : ii1II1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90008 : iIIOOOO0o0Oo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90009 : oO000O00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90010 : OOoooO00o0oo0 ( )
elif oo0oOO00oO == 90020 : i111 ( )
elif oo0oOO00oO == 90021 : hellyeah2 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90022 : hellyeah3 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90023 : I11IiIIIi ( )
elif oo0oOO00oO == 90024 : iIIOOoO0oO00o ( OoOOoOooooOOo )
elif oo0oOO00oO == 90025 : iii1 ( OoOOoOooooOOo )
if 49 - 49: I1ii11iIi11i % oooOo0oo0oo - ii + III1iiIii
elif oo0oOO00oO == 90026 : OOOOOOooo ( )
elif oo0oOO00oO == 90027 : ii1111I ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
elif oo0oOO00oO == 90028 : Oo00o00Oo ( OoOOoOooooOOo )
if 54 - 54: iI11I1II1I1I - ii / Iii / i1i1I1IIii1II % oOo0O0Ooo + OOooOOo
elif oo0oOO00oO == 900300 : o0OOOOooo ( )
elif oo0oOO00oO == 900301 : OooO0OO ( OoOOoOooooOOo )
elif oo0oOO00oO == 900302 : OooIiIIII1i11I ( OoOOoOooooOOo )
elif oo0oOO00oO == 90030 : IIii11Ii1i1I ( )
elif oo0oOO00oO == 90031 : Ooo0O0oooo ( )
elif oo0oOO00oO == 90032 : iiI ( OoOOoOooooOOo )
elif oo0oOO00oO == 90033 : oOIIiIi ( OoOOoOooooOOo )
elif oo0oOO00oO == 90034 : IIiI1Ii ( OoOOoOooooOOo )
elif oo0oOO00oO == 90035 : O0O0O0Oo ( OoOOoOooooOOo )
elif oo0oOO00oO == 90036 : O0OO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90039 : OO0oO0o0oOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 90037 : ii111IIII ( OoOOoOooooOOo )
elif oo0oOO00oO == 900377 : OOoOOo00O0o0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90038 : iIiIi1ii ( )
if 26 - 26: oO0o * IIiIiII11i % oooOo0oo0oo * IiI1i11I + IiI1i11I
elif oo0oOO00oO == 10090 : iIiiiii1i ( )
elif oo0oOO00oO == 10091 : OOOo ( OoOOoOooooOOo )
elif oo0oOO00oO == 10092 : i1ii1i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10093 : iiiiiiI1iIi ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 10094 : OOoOOOo00 ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
if 25 - 25: Iii - Ii1I
elif oo0oOO00oO == 10095 : o0O0Oo00 ( )
elif oo0oOO00oO == 10096 : o0oO0OO00oo0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 10097 : O0O000O ( OoOOoOooooOOo )
elif oo0oOO00oO == 10098 : i1i11i ( OoOOoOooooOOo )
elif oo0oOO00oO == 10099 : IiII1i1iI ( OoOOoOooooOOo )
if 100 - 100: i1IiiiI1iI / o0ii1I + OOooOOo . ii
elif oo0oOO00oO == 10200 : OOo00OoO ( )
elif oo0oOO00oO == 10201 : O0oo0O0 ( IiIi11iI , OoOOoOooooOOo , I1iiiiii )
elif oo0oOO00oO == 10202 : I11i11i1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 10203 : RT4 ( OoOOoOooooOOo )
if 83 - 83: o0o00Oo0O
elif oo0oOO00oO == 90040 : iiIIII11iiii ( )
elif oo0oOO00oO == 90041 : oOIiiIIi ( OoOOoOooooOOo )
elif oo0oOO00oO == 90042 : iIO0OO0o0O00oO ( OoOOoOooooOOo )
elif oo0oOO00oO == 90043 : III1 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90044 : oOoOo0o00o ( OoOOoOooooOOo )
elif oo0oOO00oO == 90045 : ooO0 ( )
elif oo0oOO00oO == 90046 : iIIi1ooo0o0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 90050 : iiIi ( )
elif oo0oOO00oO == 90051 : OOoO0oooo ( OoOOoOooooOOo )
elif oo0oOO00oO == 90052 : Iiiii11IIii ( OoOOoOooooOOo )
elif oo0oOO00oO == 90053 : O0oo00oOOO0o ( OoOOoOooooOOo )
elif oo0oOO00oO == 90054 : OooOOoO0OOOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 90055 : oOO ( )
if 35 - 35: Ii - Iii . OOooOOo * IIiIiII11i % Ii
elif oo0oOO00oO == 100001 : Stand_up ( )
if 55 - 55: I11i / o0o00Oo0O / ii * I1ii11iIi11i % IiI1i11I
elif oo0oOO00oO == 100003 : OooOoOOo0oO00 ( OoOOoOooooOOo )
elif oo0oOO00oO == 100004 : oo0ooOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 100005 : Resolve ( OoOOoOooooOOo )
elif oo0oOO00oO == 100008 : Search ( )
elif oo0oOO00oO == 100007 : III ( OoOOoOooooOOo )
elif oo0oOO00oO == 100009 : yt . PlayVideo ( OoOOoOooooOOo )
elif oo0oOO00oO == 100010 : ii1i1i1IiII ( OoOOoOooooOOo )
elif oo0oOO00oO == 100100 : Ii1 ( i1oOOoo0o0OOOO , OoOOoOooooOOo , iI1IiiiIiI1Ii )
elif oo0oOO00oO == 100101 : ooOo ( OoOOoOooooOOo , IiIi11iI , i11I , iI1IiiiIiI1Ii , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 100102 : iiII ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I )
elif oo0oOO00oO == 100106 : o0O0ooOOoO ( OoOOoOooooOOo , IiIi11iI )
elif oo0oOO00oO == 100107 : oo0O ( )
elif oo0oOO00oO == 100108 : OOoo00o0 ( )
elif oo0oOO00oO == 100109 : OO0o0ooO0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 40000 : oo0O0oOOO0o ( )
elif oo0oOO00oO == 40001 : IIi1i1I11IIII ( OoOOoOooooOOo )
elif oo0oOO00oO == 100110 : III1IiI1i1i ( OoOOoOooooOOo )
elif oo0oOO00oO == 100111 : oOoO00O000 ( OoOOoOooooOOo )
elif oo0oOO00oO == 100112 : O0Oo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 100113 : o00OoOO0O0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 100114 : o0OOOOOo0 ( OoOOoOooooOOo )
elif oo0oOO00oO == 100115 : i1iI1Iiii1I ( OoOOoOooooOOo )
elif oo0oOO00oO == 100117 : oooOoO ( OoOOoOooooOOo )
elif oo0oOO00oO == 100118 : OooooOoO ( OoOOoOooooOOo )
elif oo0oOO00oO == 100120 : I1iII ( OoOOoOooooOOo )
elif oo0oOO00oO == 1001200 : Iii1I1IIII ( OoOOoOooooOOo )
elif oo0oOO00oO == 100210 : ooO00O00oOO ( OoOOoOooooOOo )
elif oo0oOO00oO == 100211 : ii111i1i ( )
elif oo0oOO00oO == 100212 : iiiii1i ( )
elif oo0oOO00oO == 100213 : I1iii1 ( )
elif oo0oOO00oO == 100214 : O0Oo00 ( )
elif oo0oOO00oO == 1000111 :
 ooOO00O00 ( OoOOoOooooOOo )
 if 24 - 24: Ii1I % oooOo0oo0oo + ii + oO0o
elif oo0oOO00oO == 1001111 :
 oOO0o00O ( IiIi11iI , OoOOoOooooOOo )
 if 100 - 100: I1ii11iIi11i % oO0o - OOooOOo
elif oo0oOO00oO == 1002111 :
 Iii11iiI111i ( )
 if 46 - 46: I11i
elif oo0oOO00oO == 1003111 :
 iI1IiI1 ( OoOOoOooooOOo , IiIi11iI )
 if 28 - 28: ooOoO0O00
elif oo0oOO00oO == 1004111 :
 I11IIii ( )
 if 81 - 81: i1i1I1IIii1II % ii . i1IiiiI1iI - OOooOOo / oOo0O0Ooo
elif oo0oOO00oO == 1005111 :
 o0oOOO0O0 ( OoOOoOooooOOo , IiIi11iI )
elif oo0oOO00oO == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( OoOOoOooooOOo , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( IiIi11iI , OoOOoOooooOOo , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( IiIi11iI , OoOOoOooooOOo , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1105000 :
 try :
  IiIi11iI = IiIi11iI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiIi11iI = IiIi11iI . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I , ooOoOoOoo )
elif oo0oOO00oO == 1106000 :
 try :
  IiIi11iI = IiIi11iI . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiIi11iI = IiIi11iI . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( IiIi11iI )
elif oo0oOO00oO == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( OoOOoOooooOOo )
elif oo0oOO00oO == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( IiIi11iI )
elif oo0oOO00oO == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif oo0oOO00oO == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( OoOOoOooooOOo )
elif oo0oOO00oO == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in OoOOoOooooOOo :
  import urlresolver
  OOOOoO00o0O = urlresolver . resolve ( OoOOoOooooOOo )
  I1I1I1IIi1III = xbmcgui . ListItem ( path = OOOOoO00o0O )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1I1IIi1III )
 elif not OoOOoOooooOOo . startswith ( "plugin://plugin" ) or not any ( x in OoOOoOooooOOo for x in pyramid . g_ignoreSetResolved ) :
  I1I1I1IIi1III = xbmcgui . ListItem ( path = OoOOoOooooOOo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1I1IIi1III )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + OoOOoOooooOOo + ')' )
elif oo0oOO00oO == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( IiIi11iI , playlist )
elif oo0oOO00oO == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OoOOoOooooOOo , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1117000 :
 OoOOoOooooOOo , o0o00O000o0o = getRegexParsed ( regexs , OoOOoOooooOOo )
 if OoOOoOooooOOo :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( OoOOoOooooOOo , IiIi11iI , i1oOOoo0o0OOOO , o0o00O000o0o )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif oo0oOO00oO == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 OO00oOO0Oo = youtubedl . single_YD ( OoOOoOooooOOo )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( OO00oOO0Oo , IiIi11iI , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( OoOOoOooooOOo ) , IiIi11iI , i1oOOoo0o0OOOO , True )
elif oo0oOO00oO == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , IiIi11iI , 'video' )
elif oo0oOO00oO == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OoOOoOooooOOo , IiIi11iI , 'video' )
elif oo0oOO00oO == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OoOOoOooooOOo , IiIi11iI , 'audio' )
elif oo0oOO00oO == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1126000 :
 IiIi11iI = IiIi11iI . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( OoOOoOooooOOo , search_term = IiIi11iI [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( OoOOoOooooOOo )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif oo0oOO00oO == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif oo0oOO00oO == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif oo0oOO00oO == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I )
elif oo0oOO00oO == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( OoOOoOooooOOo , i1oOOoo0o0OOOO , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( IiIi11iI , OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( OoOOoOooooOOo )
elif oo0oOO00oO == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( OoOOoOooooOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif oo0oOO00oO == 9050000 : OOoo0oo ( )
elif oo0oOO00oO == 9060000 : oOO0o00O ( IiIi11iI , OoOOoOooooOOo )
elif oo0oOO00oO == 9080000 : IiIIi1IiiI1 ( )
elif oo0oOO00oO == 9070000 : Ooo0Oo0oo0 ( )
elif oo0oOO00oO == 9090000 : O0O00OOo ( )
elif oo0oOO00oO == 9100000 : IIi1I ( )
elif oo0oOO00oO == 9110000 : OO00O000OOO ( )
elif oo0oOO00oO == 9110001 : I1iiiiI1iI ( OoOOoOooooOOo )
elif oo0oOO00oO == 9110002 : iiIii1ii ( OoOOoOooooOOo , IiIi11iI , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 9110003 : IIiI1I1 ( IiIi11iI , iI1IiiiIiI1Ii )
elif oo0oOO00oO == 9110005 : i11i11 ( I1iiiiii , OoOOoOooooOOo )
elif oo0oOO00oO == 9110004 : o00oO00 ( )
elif oo0oOO00oO == 9999999 : ii11I1IIi1i ( )
elif oo0oOO00oO == 19999999 : oOoOoO0o0 ( )
elif oo0oOO00oO == 1999990 : iiII1IiIi1iI1 ( )
elif oo0oOO00oO == 21999990 : iI ( )
elif oo0oOO00oO == 21999991 : OO0O000 ( OoOOoOooooOOo )
elif oo0oOO00oO == 21999992 : Oo0O00O000 ( OoOOoOooooOOo )
elif oo0oOO00oO == 21999993 : i11I1IiII1i1i ( OoOOoOooooOOo )
elif oo0oOO00oO == 21999994 : ooI1111i ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 21999995 : iIIii ( OoOOoOooooOOo )
elif oo0oOO00oO == 21999996 : ii1iii1i ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 21999997 : Iii1I1111ii ( OoOOoOooooOOo , i1oOOoo0o0OOOO )
elif oo0oOO00oO == 21999998 : Ii1IIiI1io0O00Oo0 ( IiIi11iI , OoOOoOooooOOo , i1oOOoo0o0OOOO )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
