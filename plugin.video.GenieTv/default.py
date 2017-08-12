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
  o0OIiII ( 'Change Log 9/8/17 - v3.6.0' , '[COLORsteelblue]ThunderStruck Joins GenieTv[/COLOR],[CR][COLORsteelblue]RaizRadio Added To Music[/COLOR],[CR][COLORsteelblue]Adult Gallerys Added[/COLOR],[CR][COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 9/8/17 - v3.6.0' , '[COLORsteelblue]ThunderStruck Joins GenieTv[/COLOR],[CR][COLORsteelblue]RaizRadio Added To Music[/COLOR],[CR][COLORsteelblue]Adult Gallerys Added[/COLOR],[CR][COLORsteelblue]24/7 Streams Now In Stream Section, A Large Selection Coutesy Of Mr Perry[/COLOR],[CR][COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
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
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 1999990 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  if 8 - 8: oO0o - oOo0O0Ooo % o0ii1I * ii - oO0o * i1IiiiI1iI
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if O0o0Oo == '5knuckleshuffle' :
  I1I1II1I11 ( '[COLORorangered]Adult Content[/COLOR]' , '' , 19999999 , iiIi1IIiIi + 'AG.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def tools ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']Change Log[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  ii1iII1II ( )
 if O0O0ooOOO == 1 :
  oo0OOo0 ( )
 if O0O0ooOOO == 2 :
  oOOo0O00o ( )
 if O0O0ooOOO == 3 :
  iIiIi11 ( OOOiiiiI )
 if O0O0ooOOO == 4 :
  iIii1 . ok ( i1 , i1111 )
 if O0O0ooOOO == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if O0O0ooOOO == 6 :
  oooOo0OOOoo0 ( )
  if 51 - 51: I1ii11iIi11i / OOooOOo . oooOo0oo0oo * I11i + oO0o * III1iiIii
def OOOoOo ( ) :
 I1I1II1I11 ( 'Stories' , 'http://etc.usf.edu/lit2go/books/' , 21999995 , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , 'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg' , '' )
 I1I1II1I11 ( 'Virtual FirePlaces' , 'http://www.virtual-fireplace.net/fireplaces.html' , 21999991 , 'http://www.virtual-fireplace.net/files/theme/burning-log.gif' , 'http://www.virtual-fireplace.net/files/theme/burning-log1.gif' , '' )
 I1I1II1I11 ( 'Nature Sounds' , 'http://www.virtual-fireplace.net/sounds.html' , 21999993 , 'http://www.virtual-fireplace.net/files/theme/sound.gif' , 'http://www.virtual-fireplace.net/files/theme/sound-bw.gif' , '' )
def O00o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iI1i1I11I11 in I11iII :
  Ii1I1i ( I11iI1i1I11I11 , url , 21999992 , 'http://www.virtual-fireplace.net/' + iIIII , 'http://www.virtual-fireplace.net/' + iIIII , I11iI1i1I11I11 )
def o000O0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( 'rel="canonical" href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in I11iII :
  url = ( url ) . replace ( '//www.youtube.com/embed/' , '' ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' )
  yt . PlayVideo ( url )
def I1i1i1iii ( url ) :
 I1I1II1I11 ( 'Rain And Thunder' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg' , '' )
 I1I1II1I11 ( 'Water And Forests' , 'http://www.virtual-fireplace.net/water-and-forest.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg' , '' )
 I1I1II1I11 ( 'Beach And Ocean' , 'http://www.virtual-fireplace.net/rain-and-thunder.html' , 21999994 , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , 'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg' , '' )
def I1111i ( url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in I11iII :
  Ii1I1i ( I11iI1i1I11I11 , 'http:' + url , 21999992 , iIIII , iIIII , '' )
def iIIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( 'data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , url , o00O0O in I11iII :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 21999996 , iIIII , iIIII , ( o00O0O ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def ii1iii1i ( url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , o00O0O in I11iII :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR] - Audio' , url , 21999997 , iIIII , iIIII , ( o00O0O ) . replace ( ' - Text' , '' ) , ( story ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR] - Text' , url , 21999998 , iIIII , iIIII , ( o00O0O ) . replace ( ' - Text' , '' ) , ( story ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
def Iii1I1111ii ( url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<a href="([^"]*)">Audio</a>' ) . findall ( II11iIiIIIiI )
 for url in I11iII :
  ooOoO00 ( url )
def Ii1IIiI1io0O00Oo0 ( name , url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '</audio>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiII111i1i11 in I11iII :
  o0OIiII ( ( name ) . replace ( ' - Text' , '' ) , ( IiII111i1i11 ) . replace ( '&#8230' , '' ) . replace ( '&mdash;' , '-' ) . replace ( '&ndash;' , '-' ) . replace ( '&quot;' , '"' ) . replace ( '&rsquo;' , '' ) . replace ( '&#39;' , '' ) . replace ( '&quo' , '' ) . replace ( '<br />' , '' ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) )
  if 40 - 40: i1iIi * III1iiIii * Ii
  if 57 - 57: i1iIi
def II11Iiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIIII , o00O0O , i11I , I11iI1i1I11I11 in I11iII :
  Ii1I1i ( I11iI1i1I11I11 , url , 21009 , iIIII , i11I , o00O0O )
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
 OOOiiiiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( OOOiiiiI , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( OOOiiiiI )
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
 OOOiiiiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o0OOOoO0 = os . path . join ( oOOooOoo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( OOOiiiiI , o0OOOoO0 , o0oOoO00o )
 o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0OoOo00o0o
 print '======================================='
 extract . all ( o0OOOoO0 , o0OoOo00o0o , o0oOoO00o )
 I1II1I11I1I ( OOOiiiiI )
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
 for url , iIIII , I11iI1i1I11I11 in o0OOo0o0O0O :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 900302 , iIIII , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for iI in o0OO0o0oOOO0O :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , iI , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def I1i11 ( url ) :
 OooIiIIII1i11I = OooOoooOo ( url )
 o0OOo0o0O0O = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( OooIiIIII1i11I )
 OOOiII1 = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( OooIiIIII1i11I )
 for url , I11iI1i1I11I11 in o0OOo0o0O0O :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , I11iI1i1I11I11 in OOOiII1 :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def OOo ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for Oooo0O , oo00O0oO0O0 in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + Oooo0O , oo00O0oO0O0 )
def ooo0OO0O0Oo ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def Ooo0O0oooo ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , iIIII , Oo00OOOOO , '' )
 for url in next :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def iiI ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 oOIIiIi = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 OOoOooOoOOOoo = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for I11iI1i1I11I11 , url in i1Iii1i1I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for I11iI1i1I11I11 , url in OOoOooOoOOOoo :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in oOIIiIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * i1i1I1IIii1II
def o000oo ( url ) :
 if 'drive' in url :
  ooOoO00 ( url )
 else :
  IIii11Ii1i1I = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( IIii11Ii1i1I )
  for url in IIi :
   ooOoO00 ( url )
def o00o0 ( url ) :
 II1III1I1I1Ii = liveresolver . resolve ( url )
 OOOOoO00o0O = xbmcgui . ListItem ( path = II1III1I1I1Ii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoO00o0O )
def I1I1I1IIi1III ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 II11IiiIII = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II11IiiIII )
def IiiiiI1i1Iii ( ) :
 o0OOOo = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  o0OOOo = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  o0OOOo = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  o0OOOo = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  o0OOOo = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return o0OOOo
 if 11 - 11: iI11I1II1I1I * iI11I1II1I1I * oOo0O0Ooo
def iII1ii1 ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , I1i1iiiI1 :
  return I1i1iiiI1
 return True
def iIIi ( ) :
 if 62 - 62: I1ii11iIi11i - Iii
 if 21 - 21: o0o00Oo0O % III1iiIii . oOo0O0Ooo / IIiIiII11i + III1iiIii
 if 53 - 53: i1i1I1IIii1II - oOo0O0Ooo - i1i1I1IIii1II * IiI1i11I
 if 71 - 71: o0o00Oo0O - iI11I1II1I1I
 if 12 - 12: oooOo0oo0oo / I11i
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def iiI1I1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooO ( )
  if O0O0ooOOO == 1 :
   iiOO0O0Ooo ( )
  if O0O0ooOOO == 2 :
   oOoO0 ( Oo0 )
  if O0O0ooOOO == 3 :
   oo0O0o00o0O ( OOOiiiiI )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 35 - 35: i1iIi + ooOoO0O00 % Ii1I % Iii + i1i1I1IIii1II
def iiiI ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 29 - 29: Iii / IIiIiII11i / i1iIi * oooOo0oo0oo
  if 10 - 10: i1IiiiI1iI % III1iiIii * III1iiIii . Iii / o0ii1I % oooOo0oo0oo
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
  if 49 - 49: oO0o / i1i1I1IIii1II + o0o00Oo0O * I11i
  if 28 - 28: i1iIi + Ii / Iii % OOooOOo % I1ii11iIi11i - o0o00Oo0O
  if 54 - 54: ooOoO0O00 + IIiIiII11i
 else :
  if 83 - 83: Ii1I - oOo0O0Ooo + oooOo0oo0oo
  if 5 - 5: o0ii1I
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
   if 46 - 46: III1iiIii
   if 45 - 45: i1iIi
   if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
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
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def O0ooo0 ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  I1iii11 ( )
 if O0O0ooOOO == 1 :
  ooo0O ( )
 if O0O0ooOOO == 2 :
  iII1iii ( )
 if O0O0ooOOO == 3 :
  i11i1iiiII ( )
 if O0O0ooOOO == 4 :
  ooOO0oO0oo00o ( )
 if O0O0ooOOO == 5 :
  oOOo0oo0O ( )
  if 13 - 13: oOo0O0Ooo % OOooOOo . Ii1I / I1ii11iIi11i % oooOo0oo0oo . ii
  if 22 - 22: III1iiIii / Ii
def oOOoo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   iII1111III1I ( )
  if O0O0ooOOO == 1 :
   ii11i ( )
  if O0O0ooOOO == 2 :
   O00oOo00o0o ( OOOiiiiI )
  if O0O0ooOOO == 3 :
   O00oO0 ( )
  if O0O0ooOOO == 4 :
   O0Oo00OoOo ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0O0ooOOO == 5 :
   ii1ii111 ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 33 - 33: Ii1I
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def O00O0Ooooo00 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 97 - 97: i1iIi / i1IiiiI1iI % ooOoO0O00 % Ii1I
 if 18 - 18: iI11I1II1I1I % Iii
 if 95 - 95: i1iIi + Ii * i1IiiiI1iI - ooOoO0O00 * i1IiiiI1iI - iI11I1II1I1I
 if 75 - 75: ii * III1iiIii
 if 9 - 9: III1iiIii - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
def I1IIIiI1I1ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   iiiI1I1iIIIi1 ( )
  if O0O0ooOOO == 1 :
   IiiI1iiiiI1iI ( )
  if O0O0ooOOO == 2 :
   iIiiiii1i ( )
  if O0O0ooOOO == 3 :
   iiIi1IIiI ( )
  if O0O0ooOOO == 4 :
   i1oO0OO0 ( )
  if O0O0ooOOO == 5 :
   o0O0Oo00 ( )
  if O0O0ooOOO == 6 :
   O0Oo0o000oO ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / III1iiIii
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def OOOoO000 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   oOOOO = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 49 - 49: IIiIiII11i . i1i1I1IIii1II . Ii % III1iiIii
   if 34 - 34: i1IiiiI1iI % III1iiIii
   if 3 - 3: IIiIiII11i / oooOo0oo0oo + III1iiIii . i1iIi . oO0o
   if 83 - 83: i1i1I1IIii1II + ii
  iiio00oOOooOOo0o = [ oOOOO , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   I111IiiIi1 ( )
  if O0O0ooOOO == 1 :
   o00o ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , Ii1IIiiIIi , I11iI1i1I11I11 )
  if O0O0ooOOO == 2 :
   Oo000o ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0O0ooOOO == 3 :
   o00o ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , Ii1IIiiIIi , I11iI1i1I11I11 )
 else :
  if 39 - 39: Ii1I
  if 97 - 97: oooOo0oo0oo - oO0o / o0ii1I . Ii % i1i1I1IIii1II * i1i1I1IIii1II
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 1 - 1: oOo0O0Ooo % i1iIi
  if 65 - 65: oOo0O0Ooo + OOooOOo / oooOo0oo0oo
  if 83 - 83: I11i . IiI1i11I - I1ii11iIi11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 65 - 65: iI11I1II1I1I / i1iIi . III1iiIii - IIiIiII11i
  if 72 - 72: iI11I1II1I1I / III1iiIii % IiI1i11I % oooOo0oo0oo - Iii % oooOo0oo0oo
  if 100 - 100: I1ii11iIi11i + Ii
  if 71 - 71: Iii / I11i / i1IiiiI1iI % oooOo0oo0oo
  if 51 - 51: III1iiIii * o0o00Oo0O / IIiIiII11i . o0ii1I % oooOo0oo0oo / oOo0O0Ooo
  if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
  if 30 - 30: III1iiIii + i1IiiiI1iI - III1iiIii . III1iiIii - IIiIiII11i + o0o00Oo0O
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 86 - 86: ooOoO0O00
def IIi11IIiIii1 ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def Oo000o ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 I1iIII1 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 OOoOooOoOOOoo = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 for I11iI1i1I11I11 , iIIII , url in IIi :
  if '247ch' in url :
   iIii ( I11iI1i1I11I11 , url , 10190 , iIIII )
  elif '.m3u' in url :
   iIii ( I11iI1i1I11I11 , url , 1019 , iIIII )
  elif '.xml' in url :
   iIii ( I11iI1i1I11I11 , url , 1018 , iIIII )
  else :
   oOo0OoOOo0 ( I11iI1i1I11I11 , url , 222 , iIIII )
 for I11iI1i1I11I11 , url , iIIII in i1Iii1i1I :
  if '.xml' in url :
   iIii ( I11iI1i1I11I11 , url , 1018 , iIIII )
  elif '.m3u' in url :
   iIii ( I11iI1i1I11I11 , url , 1019 , iIIII )
  else :
   oOo0OoOOo0 ( I11iI1i1I11I11 , url , 222 , iIIII )
 for I11iI1i1I11I11 , url , iIIII in OOoOooOoOOOoo :
  oOo0OoOOo0 ( I11iI1i1I11I11 , url , 8043 , iIIII )
def iII11I1Ii1 ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def oOo0oO ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url , iIIII in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iIIII )
  if 5 - 5: oooOo0oo0oo - oooOo0oo0oo . I1ii11iIi11i + OOooOOo - oooOo0oo0oo . i1i1I1IIii1II
def IiIi1i1ii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 11 - 11: IIiIiII11i / I11i
def IiIi1 ( url ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url , IIiii , I1i1i , i11I , o00O0O in IIi :
  if I1i1i == '123' :
   I1i1i = iiIi1IIiIi + 'appstreams.png'
  if i11I == '123' :
   i11I = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100010 , I1i1i , i11I , o00O0O )
  elif 'playlist' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100007 , I1i1i , i11I , o00O0O )
  elif 'watchseries' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100100 , I1i1i , i11I , o00O0O )
  elif not 'http' in url :
   OOOOooO0oO00O0o ( I11iI1i1I11I11 , url , 100009 , I1i1i , i11I , o00O0O , '' )
  else :
   OOOOooO0oO00O0o ( I11iI1i1I11I11 , url , 100005 , I1i1i , i11I , o00O0O , '' )
   if 70 - 70: i1IiiiI1iI
def i11iIIi11 ( url ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 I11iII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIIII , o00O0O , i11I , I11iI1i1I11I11 in I11iII :
  if iIIII == '123' :
   iIIII = iiIi1IIiIi + 'appstreams.png'
  if i11I == '123' :
   i11I = Oo00OOOOO
  if 'php' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100004 , iIIII , i11I , o00O0O )
  elif 'playlist' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100007 , iIIII , i11I , o00O0O )
  elif 'watchseries' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100100 , iIIII , i11I , o00O0O )
  elif not 'http' in url :
   OOOOooO0oO00O0o ( I11iI1i1I11I11 , url , 100009 , iIIII , i11I , o00O0O , '' )
  else :
   OOOOooO0oO00O0o ( I11iI1i1I11I11 , url , 100005 , iIIII , i11I , o00O0O , '' )
   if 98 - 98: i1IiiiI1iI
def iiI1II11II1i ( url ) :
 if 67 - 67: oooOo0oo0oo + I1ii11iIi11i
 II11iIiIIIiI = i111iiI1ii ( url )
 OoOo000oOo0oo = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iIII1 in OoOo000oOo0oo :
  I1i1i = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1iIII1 ) )
  for I1i1i in I1i1i :
   I1i1i = I1i1i
  I11iI1i1I11I11 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1iIII1 ) )
  for I11iI1i1I11I11 in I11iI1i1I11I11 :
   if 'elete' in I11iI1i1I11I11 :
    pass
   elif 'rivate Vid' in I11iI1i1I11I11 :
    pass
   else :
    I11iI1i1I11I11 = ( I11iI1i1I11I11 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  oO0O = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1iIII1 ) )
  for oO0O in oO0O :
   oO0O = oO0O
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1iIII1 ) )
  for url in url :
   url = url
  OOOOooO0oO00O0o ( '[COLORred]' + str ( oO0O ) + '[/COLOR] : ' + str ( I11iI1i1I11I11 ) , str ( url ) , 100009 , str ( I1i1i ) , Oo00OOOOO , '' , '' )
  Ii1IIiI1i ( 'movies' , '' )
  if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
def oOO ( ) :
 I11I ( 'Featured 24/7' , '' , 9070000 , iiIi1IIiIi + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 I11I ( '24/7 Tv Thows' , '' , 9080000 , iiIi1IIiIi + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 I11I ( '24/7 Movies' , '' , 9090000 , iiIi1IIiIi + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 I11I ( '24/7 Cable' , '' , 9100000 , iiIi1IIiIi + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 I11I ( '24/7 Random Stream' , '' , 9110000 , iiIi1IIiIi + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 6 - 6: Ii1I + i1i1I1IIii1II
def Ii1iI11iI1 ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 i11I1II = 'index.php#shows'
 IIii11Ii1i1I = BeautifulSoup ( requests . get ( OOOiiiiI + i11I1II ) . content )
 OO0 = IIii11Ii1i1I . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for OOO0oOOo00O in OO0 :
  OO0oIII111i11IiI = OOO0oOOo00O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OO0oIII111i11IiI :
   O0000 = iiI111I1iIiI . text
  ooO00O0O0 = OOO0oOOo00O . findAll ( 'a' )
  for iiI111I1iIiI in ooO00O0O0 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    iII1I1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    I11iI1i1I11I11 = iiI111I1iIiI [ 'title' ]
   o0Ooo0o0ooo0 = BeautifulSoup ( requests . get ( iII1I1 ) . content )
   oo0o0000Oo0 = o0Ooo0o0ooo0 . findAll ( 'source' )
   for o0O00oOoo in oo0o0000Oo0 :
    O000O0OO00oo = o0O00oOoo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOOOooO0oO00O0o ( I11iI1i1I11I11 , O000O0OO00oo , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 69 - 69: I11i / I1ii11iIi11i
    if 43 - 43: Ii1I . oOo0O0Ooo / ii % ii
def iIIIII1iiiiII ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 i11I1II = 'index.php#movies'
 IIii11Ii1i1I = BeautifulSoup ( requests . get ( OOOiiiiI + i11I1II ) . content )
 OO0 = IIii11Ii1i1I . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for OOO0oOOo00O in OO0 :
  OO0oIII111i11IiI = OOO0oOOo00O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OO0oIII111i11IiI :
   O0000 = iiI111I1iIiI . text
  ooO00O0O0 = OOO0oOOo00O . findAll ( 'a' )
  for iiI111I1iIiI in ooO00O0O0 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    iII1I1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    I11iI1i1I11I11 = iiI111I1iIiI [ 'title' ]
   o0Ooo0o0ooo0 = BeautifulSoup ( requests . get ( iII1I1 ) . content )
   oo0o0000Oo0 = o0Ooo0o0ooo0 . findAll ( 'source' )
   for o0O00oOoo in oo0o0000Oo0 :
    O000O0OO00oo = o0O00oOoo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOOOooO0oO00O0o ( I11iI1i1I11I11 , O000O0OO00oo , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 54 - 54: ooOoO0O00
    if 22 - 22: ooOoO0O00 + o0ii1I
def O0o0O0OO00o ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 i11I1II = 'index.php#cable'
 IIii11Ii1i1I = BeautifulSoup ( requests . get ( OOOiiiiI + i11I1II ) . content )
 OO0 = IIii11Ii1i1I . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for OOO0oOOo00O in OO0 :
  OO0oIII111i11IiI = OOO0oOOo00O . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in OO0oIII111i11IiI :
   O0000 = iiI111I1iIiI . text
  ooO00O0O0 = OOO0oOOo00O . findAll ( 'a' )
  for iiI111I1iIiI in ooO00O0O0 :
   if iiI111I1iIiI . has_key ( 'href' ) :
    iII1I1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    I11iI1i1I11I11 = iiI111I1iIiI [ 'title' ]
   o0Ooo0o0ooo0 = BeautifulSoup ( requests . get ( iII1I1 ) . content )
   oo0o0000Oo0 = o0Ooo0o0ooo0 . findAll ( 'source' )
   for o0O00oOoo in oo0o0000Oo0 :
    O000O0OO00oo = o0O00oOoo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    OOOOooO0oO00O0o ( I11iI1i1I11I11 , O000O0OO00oo , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 92 - 92: I11i + i1IiiiI1iI / I1ii11iIi11i % oO0o % III1iiIii . ii
def O0Oo ( ) :
 o0Ooo0o0ooo0 = BeautifulSoup ( requests . get ( 'http://arconaitv.me/stream.php?id=random' ) . content )
 oo0o0000Oo0 = o0Ooo0o0ooo0 . findAll ( 'source' )
 for o0O00oOoo in oo0o0000Oo0 :
  O000O0OO00oo = o0O00oOoo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  OOOOooO0oO00O0o ( 'Random Pick' , O000O0OO00oo , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 7 - 7: III1iiIii % iI11I1II1I1I + Iii - o0ii1I * i1i1I1IIii1II
def OOoiIIiiIIIi1I ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 i11I1II = 'index.php#shows'
 if 65 - 65: Ii1I % o0o00Oo0O % iI11I1II1I1I * o0ii1I
 IIii11Ii1i1I = BeautifulSoup ( requests . get ( OOOiiiiI + i11I1II ) . content )
 OO0 = IIii11Ii1i1I . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for OOO0oOOo00O in OO0 :
  OO0oIII111i11IiI = OOO0oOOo00O . findAll ( 'a' )
  for iiI111I1iIiI in OO0oIII111i11IiI :
   if iiI111I1iIiI . has_key ( 'href' ) :
    iII1I1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   if iiI111I1iIiI . has_key ( 'title' ) :
    I11iI1i1I11I11 = iiI111I1iIiI [ 'title' ]
   iIIIIIiI1I1 = iiI111I1iIiI . findAll ( 'img' )
   for I11I1IIiiII1 in iIIIIIiI1I1 :
    iIIII = OOOiiiiI + I11I1IIiiII1 [ 'src' ]
    o0Ooo0o0ooo0 = BeautifulSoup ( requests . get ( iII1I1 ) . content )
    oo0o0000Oo0 = o0Ooo0o0ooo0 . findAll ( 'source' )
    for o0O00oOoo in oo0o0000Oo0 :
     O000O0OO00oo = o0O00oOoo [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     OOOOooO0oO00O0o ( I11iI1i1I11I11 , O000O0OO00oo , 9060000 , iIIII , iIIII , '' , '' )
     if 31 - 31: oOo0O0Ooo * i1i1I1IIii1II + ii - IiI1i11I / ii
def I111IIiii1Ii ( name , url ) :
 import urlresolver
 try :
  II1 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( II1 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 32 - 32: oOo0O0Ooo - Ii1I - I1ii11iIi11i
 if 32 - 32: ooOoO0O00 . Iii / oO0o
def o0OOoOoO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I11iII = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIIII , o00O0O , i11I , I11iI1i1I11I11 in I11iII :
  if '.php' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 100210 , iIIII , i11I , o00O0O )
  else :
   Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , i11I , o00O0O )
   if 15 - 15: III1iiIii / o0o00Oo0O . I11i . Ii
   if 59 - 59: i1IiiiI1iI - I11i - i1iIi
   if 48 - 48: ooOoO0O00 + Iii % OOooOOo / I1ii11iIi11i - I11i
def OOoOOo0O00O ( iconimage , url , extra ) :
 I1i1i = ' '
 iiIii1I = ' '
 i11I = ' '
 i1I11iIiII = ' '
 OO0OO0OO = i111iiI1ii ( url )
 I1i1i = re . compile ( '<img src="(.+?)">' ) . findall ( OO0OO0OO )
 for I1i1i in I1i1i :
  I1i1i = I1i1i
 OoooO0o = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( OO0OO0OO )
 for i11I in OoooO0o :
  i11I = i11I
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( OO0OO0OO )
 for url , i1I11iIiII in IIi :
  i1I11iIiII = 'S' + ( i1I11iIiII ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  I11I ( ( i1I11iIiII ) . replace ( '  ' , '' ) , url , 100101 , I1i1i , i11I , iiIii1I , '' )
  Ii1IIiI1i ( 'Movies' , 'info' )
  if 24 - 24: OOooOOo % ooOoO0O00 + IiI1i11I . Ii . Ii1I
def IIi1II ( url , name , fanart , extra , iconimage ) :
 IiiI11i1I = extra
 i1I11iIiII = name
 OO0OO0OO = i111iiI1ii ( url )
 I1i1i = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( OO0OO0OO )
 for url , name , OOo0 in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  OOo0 = OOo0
  iiIii1IIi = name + ' - [COLORred]' + OOo0 + '[/COLOR]'
  I11I ( iiIii1IIi , url , 100102 , I1i1i , fanart , 'Aired : ' + OOo0 , iiIii1IIi )
  if 10 - 10: Ii - I11i % iI11I1II1I1I
def i111IIIiI ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = i111iiI1ii ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , name in IIi :
  for OOOOoO00o0O in o00OO00OoO :
   if OOOOoO00o0O in OOOiiiiI :
    URL = 'http://www.watchseriesgo.to/link/' + OOOiiiiI
    OOOOooO0oO00O0o ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  I11I ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 23 - 23: I1ii11iIi11i % Iii - oooOo0oo0oo % iI11I1II1I1I . OOooOOo
  if 24 - 24: III1iiIii / ii + o0ii1I % iI11I1II1I1I - oooOo0oo0oo . oooOo0oo0oo
def iIi ( url , name ) :
 oo00O0 = name
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 OOoOooOoOOOoo = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiiI111I ( url , oo00O0 )
 for url in i1Iii1i1I :
  iiiI111I ( url , oo00O0 )
 for url in OOoOooOoOOOoo :
  iiiI111I ( url , oo00O0 )
  if 75 - 75: ii % oO0o / oOo0O0Ooo
def iiiI111I ( url , season_name ) :
 if 'daclips.in' in url :
  Oo0ooo0Ooo ( url , season_name )
 elif 'filehoot.com' in url :
  i1II1I ( url , season_name )
 elif 'allmyvideos.net' in url :
  OOoO0ooOO ( url , season_name )
 elif 'vidspot.net' in url :
  iii1IIII1iii11I ( url , season_name )
 elif 'vodlocker' in url :
  oo0OoOooo ( url , season_name )
 elif 'vidto' in url :
  O00O00O000OOO ( url , season_name )
  if 3 - 3: o0o00Oo0O
  if 64 - 64: ooOoO0O00 % i1iIi / Ii - ooOoO0O00 % oooOo0oo0oo . IiI1i11I
def O00O00O000OOO ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1i111 , I11iI1i1I11I11 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 67 - 67: I11i % OOooOOo . OOooOOo - i1iIi
  if 90 - 90: i1iIi + IIiIiII11i * Ii1I / o0ii1I . I11i + I11i
def OOoO0ooOO ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1i111 , I11iI1i1I11I11 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 40 - 40: i1iIi / OOooOOo % Ii % Ii1I / oOo0O0Ooo
def iii1IIII1iii11I ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for II1i111 , I11iI1i1I11I11 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 62 - 62: ooOoO0O00 - OOooOOo
def oo0OoOooo ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1i111 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 62 - 62: ooOoO0O00 + I1ii11iIi11i % III1iiIii
def Oo0ooo0Ooo ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for II1i111 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 28 - 28: Ii1I . ooOoO0O00
def i1II1I ( url , season_name ) :
 II11iIiIIIiI = i111iiI1ii ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1i111 in IIi :
  i1iiiIii11 ( II1i111 , season_name )
  if 10 - 10: oO0o / I1ii11iIi11i
def i1iiiIii11 ( Link , season_name ) :
 if 'http:/' in Link :
  I1i ( Link )
  if 50 - 50: I11i * o0ii1I % Ii1I / I1ii11iIi11i - o0o00Oo0O % IiI1i11I
  if 48 - 48: oOo0O0Ooo + Ii1I + IIiIiII11i * Ii
def IiIIi1I1I11Ii ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 o0OO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in o0OO :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 58 - 58: ii . oOo0O0Ooo / IIiIiII11i / IIiIiII11i - III1iiIii + I1ii11iIi11i
def I11I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = True )
 return ooo0
 if 89 - 89: IIiIiII11i / i1i1I1IIii1II
 if 14 - 14: oooOo0oo0oo . oOo0O0Ooo * i1iIi + IIiIiII11i - i1iIi + oooOo0oo0oo
def OOOOooO0oO00O0o ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIiII1 = [ ]
  IIIIIiII1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = False )
 return ooo0
 if 45 - 45: oOo0O0Ooo / IiI1i11I . IiI1i11I
def i1oO ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 30 - 30: I1ii11iIi11i . oO0o
def o0Oii1111i ( url ) :
 O0ooOO = xbmc . Player ( IiiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0ooOO . play ( url ) . strip ( )
 except : pass
 if 19 - 19: IIiIiII11i
def I1i ( url ) :
 O0ooOO = xbmc . Player ( )
 import urlresolver
 try : O0ooOO . play ( url )
 except : pass
 if 72 - 72: ii / oOo0O0Ooo + o0ii1I / OOooOOo * o0ii1I
def i111iiI1ii ( url ) :
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
  if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
  if 25 - 25: Iii + OOooOOo . I11i % OOooOOo * oooOo0oo0oo
  if 32 - 32: Ii - i1IiiiI1iI
def ooo0O ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   oo00ooOoo ( )
  if O0O0ooOOO == 1 :
   iii1IIIiiiI ( )
  if O0O0ooOOO == 2 :
   OoO00oo00 ( )
  if O0O0ooOOO == 3 :
   Oo0Oo0O ( )
  if O0O0ooOOO == 4 :
   iiiI1i11Ii ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def i11i1iiiII ( ) :
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
 if 16 - 16: I1ii11iIi11i / Ii
 if 64 - 64: Ii / o0ii1I * ooOoO0O00
 if 73 - 73: I1ii11iIi11i - OOooOOo - i1i1I1IIii1II - oOo0O0Ooo
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   oo0o0oOo = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oo0o0oOo + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O0ooOOO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O0ooOOO == 0 :
    OO0oOOo0o ( II1I )
    OoOO0o ( )
   elif O0O0ooOOO == 1 :
    I1 ( II1I )
  else :
   pass
   if 7 - 7: oO0o * Iii + IIiIiII11i % Ii
def I1 ( addon ) :
 oo0o0oOo = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 8 - 8: i1iIi * o0o00Oo0O
def OO0oOOo0o ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOoO = os . path . join ( IIIII , 'default.py' )
 IiIIII = open ( OOoO , "w+" )
 if 89 - 89: oO0o / oOo0O0Ooo
 IiIIII . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 IiIIII . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 IiIIII . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 16 - 16: I1ii11iIi11i + i1iIi / I1ii11iIi11i / oO0o % i1i1I1IIii1II % Ii1I
 if 22 - 22: IIiIiII11i * oO0o * Iii + Ii1I * I11i
 if 100 - 100: ooOoO0O00 / III1iiIii
 if 3 - 3: IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
def I1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0o00O0Oo0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0I11iII = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOoOooOoOOOoo = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOIIiIi = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiiIiI = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url , iIIIIiiIii , i11I , o00O0O in O0o00O0Oo0 :
  if 'php' in url :
   I1I1II1I11 ( I11iI1i1I11I11 , url , 90037 , iIIIIiiIii , i11I , o00O0O )
  elif I11iI1i1I11I11 == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , iIIIIiiIii , i11I , o00O0O )
  else :
   Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIIIiiIii , i11I , o00O0O )
 for I11iI1i1I11I11 , iIIII , url , ooO0oo in o0I11iII :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 90037 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , iIIII , url , ooO0oo in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 90037 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , url , iIIII , ooO0oo in i1Iii1i1I :
  Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , url , iIIII , ooO0oo in OOoOooOoOOOoo :
  Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , url , iIIII , ooO0oo in oOIIiIi :
  Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , url , iIIII in IiiIiI :
  Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , '' , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def ooO0oo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , iIIII , url , ooO0oo in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 90037 , iIIII , ooO0oo , '' )
 for I11iI1i1I11I11 , url , iIIII , ooO0oo in i1Iii1i1I :
  Ii1I1i ( I11iI1i1I11I11 , url , 222 , iIIII , ooO0oo , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  if 9 - 9: oOo0O0Ooo + Ii1I / oOo0O0Ooo . i1i1I1IIii1II * i1iIi
def i1i1ii1111i1i ( ) :
 iIiI = [ 'serialsearch' , 'moviesearch' ]
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 if ooOo0O0o0 == '' :
  pass
 else :
  for o0oo0O in iIiI :
   I1iiIII = Oo0o0000o0o0 + o0oo0O + '.php'
   OO0OO0OO = OooOoooOo ( I1iiIII )
   if OO0OO0OO != 'Opened' :
    I11iII = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( OO0OO0OO )
    for I11iI1i1I11I11 , OOOiiiiI , iIIIIiiIii , i11I , o00O0O in I11iII :
     if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
      iIi1I1 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for OOOOoO00o0O in iIi1I1 :
       if OOOOoO00o0O == OOOiiiiI :
        I11iI1i1I11I11 = '[COLORred]* [/COLOR]' + ( I11iI1i1I11I11 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        O0oOoo0OoO0O = open ( OOOO0OOoO0O0 , "a" )
        O0oOoo0OoO0O . write ( 'item="' + I11iI1i1I11I11 + '"\n' )
        O0oOoo0OoO0O . close
      if 'php' in OOOiiiiI :
       I1I1II1I11 ( I11iI1i1I11I11 , OOOiiiiI , 90037 , iIIIIiiIii , i11I , o00O0O )
      else :
       Ii1I1i ( I11iI1i1I11I11 , OOOiiiiI , 222 , iIIIIiiIii , i11I , o00O0O )
       if 63 - 63: ii / i1iIi
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   if 91 - 91: ooOoO0O00 - iI11I1II1I1I
def Oo0Oo00o00oO ( ) :
 if 95 - 95: oOo0O0Ooo
 if 88 - 88: III1iiIii % oO0o + i1IiiiI1iI + i1IiiiI1iI * IIiIiII11i
 if 78 - 78: ii
 if 77 - 77: Ii1I / ooOoO0O00 / I1ii11iIi11i % oooOo0oo0oo
 if 48 - 48: Iii - III1iiIii + iI11I1II1I1I + ii
 if 4 - 4: IIiIiII11i . Iii + o0ii1I * i1IiiiI1iI . i1iIi
 if 87 - 87: OOooOOo / oO0o / Ii
 if 74 - 74: i1i1I1IIii1II / Ii1I % I11i
 if 88 - 88: OOooOOo - Ii % I11i * Iii + Ii1I
 if 52 - 52: IIiIiII11i . oOo0O0Ooo + OOooOOo % oO0o
 if 62 - 62: I11i
 if 15 - 15: Iii + o0ii1I . oooOo0oo0oo * oO0o . OOooOOo
 if 18 - 18: ooOoO0O00 % IIiIiII11i + i1IiiiI1iI % o0ii1I
 if 72 - 72: iI11I1II1I1I
 if 45 - 45: I1ii11iIi11i - I11i % i1IiiiI1iI
 if 38 - 38: i1IiiiI1iI % oooOo0oo0oo - ii
 if 87 - 87: oO0o % oOo0O0Ooo
 if 77 - 77: iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
 if 26 - 26: I11i * III1iiIii . ooOoO0O00
 if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
 if 62 - 62: Ii % oooOo0oo0oo . III1iiIii . oooOo0oo0oo
 IIii11Ii1i1I = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 o0Ooo0o0ooo0 = requests . get ( 'http://www.djing.com/' ) . content
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0Ooo0o0ooo0 )
 OO0 = IIii11Ii1i1I . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for OOO0oOOo00O in OO0 :
  OO0oIII111i11IiI = OOO0oOOo00O . findAll ( 'a' )
  for iiI111I1iIiI in OO0oIII111i11IiI :
   if iiI111I1iIiI . has_attr ( 'href' ) :
    iII1I1 = 'https://tvcatchup.com' + iiI111I1iIiI [ 'href' ]
   iIIIIIiI1I1 = iiI111I1iIiI . findAll ( 'img' )
   for I11I1IIiiII1 in iIIIIIiI1I1 :
    iIIII = I11I1IIiiII1 [ 'src' ]
    ooOo0O0O0oOO0 = I11I1IIiiII1 [ 'alt' ]
   IIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( iiI111I1iIiI ) )
   for iIiIIi in IIi :
    oOo0OoOOo0 ( ( '[COLORgold]' + ooOo0O0O0oOO0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iIiIIi + '[/COLOR]' ) , iII1I1 , 90024 , iIIII )
    if 14 - 14: I11i / oooOo0oo0oo - iI11I1II1I1I - i1i1I1IIii1II % i1iIi
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in i1Iii1i1I :
  if 'Submit' in I11iI1i1I11I11 :
   pass
  elif '&lt;' in I11iI1i1I11I11 :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 90025 , 'http://www.djing.com' + iIIII , Oo00OOOOO , '' )
   if 49 - 49: i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def OOoO00ooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 12 - 12: i1iIi % oOo0O0Ooo + i1i1I1IIii1II - ooOoO0O00 . o0ii1I / oOo0O0Ooo
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def o0IiiiI111I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  III1I11i1iIi ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 69 - 69: I1ii11iIi11i * IIiIiII11i * i1iIi . IiI1i11I - Ii1I
def I11iiIIiI1ii ( ) :
 II11iIiIIIiI = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 I1IiIIi11I1 = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11i1I1Ii11 , ooOOoOo , oooO in I1IiIIi11I1 :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11i1I1Ii11 + ooOOoOo + oooO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'yr' in OOOiiiiI :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
   if 12 - 12: IIiIiII11i
def ii11i ( ) :
 if 2 - 2: ooOoO0O00 - oOo0O0Ooo + Iii . IIiIiII11i
 if 25 - 25: i1i1I1IIii1II
 if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
 if 43 - 43: Ii1I - IiI1i11I
 if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
 if 47 - 47: IiI1i11I
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'yr' in OOOiiiiI :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
   if 92 - 92: oooOo0oo0oo + OOooOOo % ooOoO0O00
def I1I1I11Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1Iii1 , url , I11iI1i1I11I11 in IIi :
  if 'id' in url :
   iIii ( ( '[COLORred]RANK [COLORblue]' + ii1Iii1 + '[COLORred] - [COLORblue]' + I11iI1i1I11I11 + '[/COLOR]' ) , I11iI1i1I11I11 , 10202 , iiIi1IIiIi + 'rated.png' )
   if 80 - 80: o0ii1I - I11i
def iI1II1I1I ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OOo0oOO0o0oo0 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1iIIiii1 = ( url )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 oOo000O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iII = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 ooO0o0O0Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IiiIIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O00o0O = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIIiI = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ii1iIIiii1
 O00 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1iiIII1IIiIIII = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 19 - 19: IiI1i11I - I11i / I11i + I1ii11iIi11i
 OoO0o0000O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II1o0ooO0OOO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 74 - 74: o0ii1I * Ii / i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( oOo000O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iII )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( ooO0o0O0Oo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OoOoo00O = O00O0oOO00O00 ( IiiIIi )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1iii1ii = O00O0oOO00O00 ( iIIIiI )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 II1I11Iii1 = O00O0oOO00O00 ( O00 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1iIIi1II1iiI = O00O0oOO00O00 ( i1iiIII1IIiIIII )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 31 - 31: I11i % Iii + iI11I1II1I1I + Ii * i1IiiiI1iI
 if 45 - 45: oooOo0oo0oo * i1IiiiI1iI . i1iIi - i1IiiiI1iI + III1iiIii
 iIIOOoO0oO00o = O00O0oOO00O00 ( OoO0o0000O )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iiiiii1 = O00O0oOO00O00 ( II1o0ooO0OOO )
 if 66 - 66: i1i1I1IIii1II * iI11I1II1I1I % iI11I1II1I1I * III1iiIii - i1iIi - III1iiIii
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
 if i1iIIi1II1iiI != 'Failed' :
  Iio00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIi1II1iiI )
  for url , I11iI1i1I11I11 in Iio00 :
   IiI1iiII1i1i = O00O0oOO00O00 ( url )
   i1IiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1iiII1i1i )
   for o0o0O00 , oOo000OOooO0O in i1IiI :
    oOo000OOooO0O = ( oOo000OOooO0O . replace ( '.' , ' ' ) )
    if ooOo0O0o0 in oOo000OOooO0O . lower ( ) :
     if '.mkv' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 222 , '' , '' , '' )
     elif '.mp4' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 222 , '' , '' , '' )
     elif '.avi' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 222 , '' , '' , '' )
     elif '.wav' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 44 - 44: o0o00Oo0O . i1i1I1IIii1II * Ii % Ii + o0o00Oo0O / oooOo0oo0oo
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in i1Iii1i1I :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 89 - 89: o0ii1I % ooOoO0O00 % i1i1I1IIii1II
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: i1i1I1IIii1II * ii . OOooOOo
 if o00OooOO000 != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OOoooOoO0Oo , I11iI1i1I11I11 in OOoOooOoOOOoo :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iII + OOoooOoO0Oo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  oOIIiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in oOIIiIi :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 78 - 78: ii / oooOo0oo0oo % OOooOOo * ii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OoOoo00O != 'Failed' :
  ooOO00o00 = [ ]
  IiiIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOoo00O )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in IiiIiI :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    if I11iI1i1I11I11 in ooOO00o00 :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , Ii1IIiiIIi , OoooO0o , o00O0O )
     ooOO00o00 . append ( I11iI1i1I11I11 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if i1iii1ii != 'Failed' :
  Ii11Iii = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1iii1ii )
  for url , iIIII , I11iI1i1I11I11 in Ii11Iii :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iIIII )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 68 - 68: oOo0O0Ooo % o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: ooOoO0O00 + OOooOOo + iI11I1II1I1I * OOooOOo * iI11I1II1I1I + Iii
    if 64 - 64: iI11I1II1I1I / o0o00Oo0O % III1iiIii . ii + III1iiIii + i1i1I1IIii1II
    if 79 - 79: ii - III1iiIii * III1iiIii . OOooOOo
    if 100 - 100: IIiIiII11i * Iii % oOo0O0Ooo / Ii1I
    if 90 - 90: Ii1I . i1iIi . OOooOOo . o0ii1I
    if 4 - 4: o0ii1I + OOooOOo % Ii1I / Ii
    if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + III1iiIii % Ii % OOooOOo
    if 78 - 78: o0ii1I + OOooOOo + III1iiIii - III1iiIii . Ii / oO0o
    if 27 - 27: o0ii1I - o0o00Oo0O % Iii * i1IiiiI1iI . III1iiIii % iI11I1II1I1I
    if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % i1iIi
    if 24 - 24: OOooOOo
    if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
    if 28 - 28: oOo0O0Ooo
    if 49 - 49: Iii . I11i % i1i1I1IIii1II / o0ii1I
    if 95 - 95: o0o00Oo0O * OOooOOo * III1iiIii . i1iIi / iI11I1II1I1I
    if 28 - 28: III1iiIii + i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oOo0O0Ooo
    if 45 - 45: o0o00Oo0O / ooOoO0O00 * i1i1I1IIii1II * oO0o
    if 35 - 35: Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
 if iIIOOoO0oO00o != 'Failed' :
  oO00o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIOOoO0oO00o )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in oO00o :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 36 - 36: i1IiiiI1iI . IIiIiII11i % i1iIi
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 84 - 84: ii - Ii / iI11I1II1I1I / ii / Ii1I
    if 4 - 4: I1ii11iIi11i + I11i
    if 17 - 17: oO0o * OOooOOo
    if 15 - 15: Ii / i1iIi % oOo0O0Ooo
    if 71 - 71: i1IiiiI1iI / Ii1I * iI11I1II1I1I
    if 57 - 57: oooOo0oo0oo + i1IiiiI1iI % Ii1I . oO0o / oO0o * o0o00Oo0O
    if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
    if 68 - 68: I11i
    if 20 - 20: i1IiiiI1iI - i1IiiiI1iI
    if 37 - 37: III1iiIii
 iI11i = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 73 - 73: IiI1i11I * IiI1i11I / i1iIi
 for o0oo0O in iI11i :
  I1iiIII = oO0 + o0oo0O + oOoOooOo0o0
  i1iIIi1II1iiI = O00O0oOO00O00 ( I1iiIII )
  if i1iIIi1II1iiI != 'Failed' :
   Iio00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIi1II1iiI )
   for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in Iio00 :
    if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 43 - 43: Ii1I . ooOoO0O00 . III1iiIii + o0o00Oo0O * o0ii1I * o0o00Oo0O
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 41 - 41: Ii1I + o0ii1I % ii . Ii1I + IiI1i11I . IiI1i11I
 iI11i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 31 - 31: Ii + IIiIiII11i . IiI1i11I * OOooOOo
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 for o0oo0O in iI11i :
  I1iiIII = OOo0oOO0o0oo0 + o0oo0O
  O0oOO0o = O00O0oOO00O00 ( I1iiIII )
  if O0oOO0o != 'Failed' :
   iiiiI1IiI1I1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0oOO0o )
   for OOoooOoO0Oo , I11iI1i1I11I11 in iiiiI1IiI1I1 :
    if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
     oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOo0oOO0o0oo0 + o0oo0O + OOoooOoO0Oo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 19 - 19: o0ii1I
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
def i1oO0OO0 ( ) :
 iIii ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 iIii ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 iIii ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 iIii ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def OOOO0oOo00O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , i1I11iIiII , i1I1I1i1i1i , OOo0 , ii1 in IIi :
  iIii ( ( '[COLORblue]' + I11iI1i1I11I11 + '[/COLOR] [COLORred]Season[/COLOR]-' + i1I11iIiII + ' [COLORred]Returns [/COLOR]- ' + ii1 + ' ' + OOo0 ) , I11iI1i1I11I11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 79 - 79: o0ii1I
def o0Oii111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , i1I11iIiII , i1I1I1i1i1i in IIi :
  iIii ( ( '[COLORblue]' + I11iI1i1I11I11 + '[/COLOR] [COLORred]Season[/COLOR]-' + i1I11iIiII + ' [COLORred] Status Unknown[/COLOR] ' ) , I11iI1i1I11I11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 93 - 93: ii * I1ii11iIi11i
def I1IiI1iIiIiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , i1I11iIiII , i1I1I1i1i1i , OOo0 in IIi :
  iIii ( ( '[COLORblue]' + I11iI1i1I11I11 + ' [COLORred] Cancelled On[/COLOR] ' + OOo0 ) , I11iI1i1I11I11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 29 - 29: i1iIi - ooOoO0O00 . Iii - Ii1I + i1iIi + ii
def iii1 ( url ) :
 ii1iIIiii1 = ( url )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 if 13 - 13: iI11I1II1I1I
 if 77 - 77: Ii - iI11I1II1I1I / i1i1I1IIii1II / i1iIi / oO0o
 o0o0O00 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 oOo000O = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 iII = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 ooO0o0O0Oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O00o0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 56 - 56: ii * o0o00Oo0O
 O00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1iiIII1IIiIIII = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 oo0OoOOooO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 60 - 60: i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 98 - 98: i1iIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 34 - 34: iI11I1II1I1I * Iii * Iii / Ii1I
 if 28 - 28: oO0o - i1i1I1IIii1II + OOooOOo + o0ii1I / iI11I1II1I1I
 OooIiIIII1i11I = O00O0oOO00O00 ( o0o0O00 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oOo000O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iII )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( ooO0o0O0Oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 O0oOO0o = O00O0oOO00O00 ( O00o0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
 if 68 - 68: oooOo0oo0oo + i1i1I1IIii1II . o0o00Oo0O . o0ii1I % ooOoO0O00 % oooOo0oo0oo
 II1I11Iii1 = O00O0oOO00O00 ( O00 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iIIi1II1iiI = O00O0oOO00O00 ( i1iiIII1IIiIIII )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 i1I1iIoOOoO = O00O0oOO00O00 ( oo0OoOOooO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 87 - 87: OOooOOo % iI11I1II1I1I
 if i1iIIi1II1iiI != 'Failed' :
  Iio00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIi1II1iiI )
  for url , I11iI1i1I11I11 in Iio00 :
   IiI1iiII1i1i = O00O0oOO00O00 ( url )
   i1IiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1iiII1i1i )
   for o0o0O00 , oOo000OOooO0O in i1IiI :
    if ooOo0O0o0 in oOo000OOooO0O . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , url + o0o0O00 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 72 - 72: oooOo0oo0oo . oooOo0oo0oo - Ii1I
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if II1I11Iii1 != 'Failed' :
  III1II1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1I11Iii1 )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in III1II1i :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 3 - 3: IiI1i11I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
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
 if i1I1iIoOOoO != 'Failed' :
  IiIIiii1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1iIoOOoO )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in IiIIiii1I :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    iIii ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , Ii1IIiiIIi )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  O00O = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , iIIII , I11iI1i1I11I11 , II1oOo00o in i1Iii1i1I :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    if 'season' in II1oOo00o :
     iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iIIII , iIIII , '' )
    if 'episodes' in II1oOo00o :
     iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iIIII , iIIII , '' )
  for url in O00O :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 12 - 12: I11i * i1IiiiI1iI % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OooIiIIII1i11I != 'Failed' :
  o0I11iII = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for url , I11iI1i1I11I11 , iIIII in o0I11iII :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( I11iI1i1I11I11 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iIIII , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 81 - 81: I1ii11iIi11i - Iii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 24 - 24: ii . oO0o * IIiIiII11i
    if 59 - 59: i1IiiiI1iI + oO0o / oooOo0oo0oo
    if 97 - 97: I1ii11iIi11i * IiI1i11I % i1iIi . IiI1i11I - i1IiiiI1iI - oooOo0oo0oo
    if 79 - 79: oOo0O0Ooo - i1iIi
    if 37 - 37: III1iiIii . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
    if 83 - 83: III1iiIii / i1IiiiI1iI
    if 64 - 64: oO0o % III1iiIii . i1IiiiI1iI % oO0o + Iii * III1iiIii
    if 83 - 83: I11i % i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
    if 65 - 65: iI11I1II1I1I % i1i1I1IIii1II + o0o00Oo0O / ii
 if o00OooOO000 != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for I11iI1i1I11I11 in OOoOooOoOOOoo :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iII + I11iI1i1I11I11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 52 - 52: o0ii1I % oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  oOIIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for I11iI1i1I11I11 in oOIIiIi :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( ooO0o0O0Oo + I11iI1i1I11I11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 80 - 80: ii + III1iiIii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if O0oOO0o != 'Failed' :
  iiiiI1IiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oOO0o )
  for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in iiiiI1IiI1I1 :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 95 - 95: i1IiiiI1iI / i1i1I1IIii1II * i1IiiiI1iI - ii * ii % oO0o
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 43 - 43: I1ii11iIi11i . i1IiiiI1iI
 I1I1i1i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for o0oo0O in I1I1i1i :
  I1iiIII = oO0 + o0oo0O + oOoOooOo0o0
  iIIOOoO0oO00o = O00O0oOO00O00 ( I1iiIII )
  if iIIOOoO0oO00o != 'Failed' :
   oO00o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIOOoO0oO00o )
   for I11iI1i1I11I11 , o00O0O , url , iIIII , i11I , IIiii in oO00o :
    if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] - Source Pandoras[/COLOR]' , url , IIiii , iIIII , i11I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 87 - 87: OOooOOo / III1iiIii . i1iIi - oooOo0oo0oo / oO0o
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 41 - 41: IIiIiII11i
     if 27 - 27: I1ii11iIi11i * OOooOOo % iI11I1II1I1I . oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: Iii % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / i1IiiiI1iI
def OO0ooOoOO0OOo ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']Adult Gallery[/COLOR]' , '[COLOR' + ooOoOoo0O + ']JizBox[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Adult Channels[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  OooOoooo0000 ( )
 if O0O0ooOOO == 1 :
  I1ii1i11i ( )
 if O0O0ooOOO == 2 :
  Oooooo0O00o ( )
  if 36 - 36: OOooOOo + III1iiIii * o0o00Oo0O . ii * ii
  if 51 - 51: Ii1I * Ii1I
  if 98 - 98: oO0o - o0ii1I . III1iiIii % Ii
def OooOoooo0000 ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']YOLOselfies[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HotNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MyNudeBabes[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TeenNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADULTmeme[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GIRLSmeme[/COLOR]' , ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  OO00oo ( 'http://www.yoloselfie.com/' )
 if O0O0ooOOO == 1 :
  O0Oo0O0 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if O0O0ooOOO == 2 :
  I1IiiIiii1 ( 'http://www.teennudegirls.com/' )
 if O0O0ooOOO == 3 :
  I1IiiIiii1 ( 'http://www.teennudegirls.com/' )
 if O0O0ooOOO == 4 :
  i11i ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if O0O0ooOOO == 5 :
  i11i ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 86 - 86: o0ii1I
def OO00oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 100111 , iIIII )
 for url in i1Iii1i1I :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 100110 , iIIII )
def IiII1i1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0OOO00 = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( O0OOO00 )
  sys . exit ( 1 )
def i11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , iIIII in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + iIIII , 100113 , 'http:' + iIIII )
 for url in i1Iii1i1I :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http:' + url , 100112 , iIIII )
def O0Oo0O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , iIIII )
def ooOOo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , iIIII , 100113 , iIIII )
def IiI1Iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , iIIII )
def Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , iIIII , 100113 , iIIII )
def I1IiiIiii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , iIIII )
def iIiiiIiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , iIIII , 100113 , iIIII )
def i1I1Ii11i ( url ) :
 O0OOO00 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( O0OOO00 )
 sys . exit ( 1 )
 if 19 - 19: III1iiIii - I11i . iI11I1II1I1I . OOooOOo / oooOo0oo0oo
def OOO0O00Oo ( ) :
 if 13 - 13: iI11I1II1I1I
 if 2 - 2: ooOoO0O00 * i1i1I1IIii1II - i1i1I1IIii1II + ii % OOooOOo / OOooOOo
 if 3 - 3: ii
 if 71 - 71: III1iiIii + ooOoO0O00 - IiI1i11I - Ii . Iii - i1iIi
 if 85 - 85: Ii1I - OOooOOo / Ii1I + oooOo0oo0oo - IiI1i11I
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + i1IiiiI1iI
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * i1i1I1IIii1II
 if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
 if 80 - 80: i1i1I1IIii1II * Iii / iI11I1II1I1I % i1i1I1IIii1II / iI11I1II1I1I
 if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * IiI1i11I . Ii * o0o00Oo0O
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
 iIii ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 iIii ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 iIii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 27 - 27: oooOo0oo0oo
def O0OO0ooO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , oO0oOO0o in IIi :
  iIii ( ( I11iI1i1I11I11 + ' - ' + oO0oOO0o ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 65 - 65: IiI1i11I . oO0o + o0ii1I
def IIiI1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 67 - 67: o0ii1I
def iIII11Iiii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , url in IIi :
  iIii ( I11iI1i1I11I11 , url , 90054 , iIIII )
 for url in next :
  iIii ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 95 - 95: oOo0O0Ooo
def o0OoO0OOoO0Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIIII , oO0oOO0o , url , I11iI1i1I11I11 , oO00O in IIi :
  I1I1II1I11 ( oO0oOO0o + ' - ' + I11iI1i1I11I11 + ' - ' + oO00O , url , 90044 , iIIII , iIIII , '' )
 for iIIII , I11iI1i1I11I11 , url in i1Iii1i1I :
  iIii ( I11iI1i1I11I11 , url , 90044 , iIIII , iIIII , '' )
 for url in next :
  iIii ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 21 - 21: oooOo0oo0oo % III1iiIii % oO0o % ii
def i11i1i ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ooOo0O0o0 )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 , II1oOo00o in IIi :
  if 'season' in II1oOo00o :
   iIii ( I11iI1i1I11I11 , OOOiiiiI , 90054 , iIIII , iIIII , '' )
  if 'episodes' in II1oOo00o :
   iIii ( I11iI1i1I11I11 , OOOiiiiI , 90044 , iIIII , iIIII , '' )
 for OOOiiiiI in next :
  iIii ( 'NEXT' , OOOiiiiI , 90053 , iiIi1IIiIi + 'Next.png' )
  if 73 - 73: o0o00Oo0O . i1i1I1IIii1II + Ii + iI11I1II1I1I - Iii / OOooOOo
def OO0OOOOo0000O ( ) :
 if 25 - 25: IiI1i11I - I1ii11iIi11i
 if 10 - 10: o0o00Oo0O % III1iiIii . oO0o + I11i + Ii1I
 if 52 - 52: OOooOOo / oO0o + i1IiiiI1iI
 if 49 - 49: iI11I1II1I1I % Iii . Iii . iI11I1II1I1I * OOooOOo / Iii
 if 95 - 95: i1i1I1IIii1II * iI11I1II1I1I + Ii1I
 if 5 - 5: I1ii11iIi11i
 if 100 - 100: o0ii1I + iI11I1II1I1I
 if 59 - 59: III1iiIii
 if 89 - 89: OOooOOo % iI11I1II1I1I
 if 35 - 35: Ii1I + i1IiiiI1iI - OOooOOo % i1i1I1IIii1II % I11i % OOooOOo
 iIii ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 iIii ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 iIii ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 iIii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 45 - 45: oOo0O0Ooo * oooOo0oo0oo % oO0o
def i111I11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , oO0oOO0o in IIi :
  if 'genre' in url :
   iIii ( ( I11iI1i1I11I11 + ' - ' + oO0oOO0o ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
def I1iI11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  if 'release' in url :
   iIii ( I11iI1i1I11I11 , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 81 - 81: Ii + Ii * oO0o + III1iiIii
def iiiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , IiiIi , url , o00O0O in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 + ' ' + IiiIi , url , 90044 , iIIII , iIIII , o00O0O )
 for iIIII , I11iI1i1I11I11 , II1oOo00o , url , i1ii1I , o00O0O in i1Iii1i1I :
  if 'movies' in II1oOo00o :
   I1I1II1I11 ( I11iI1i1I11I11 + ' - ' + i1ii1I , url , 90044 , iIIII , iIIII , o00O0O )
 for url in next :
  iIii ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 50 - 50: iI11I1II1I1I + OOooOOo . OOooOOo + ooOoO0O00 + III1iiIii
def IiI1iIiIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  III1IiI1i1i ( 'http:' + url )
  if 94 - 94: IiI1i11I - I1ii11iIi11i + i1i1I1IIii1II
def III1IiI1i1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( I11iI1i1I11I11 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def O0oooOoO ( ) :
 if 62 - 62: oooOo0oo0oo / IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
 if 2 - 2: Ii - i1IiiiI1iI + oO0o % Iii * o0ii1I
 if 54 - 54: o0o00Oo0O - IiI1i11I . oooOo0oo0oo % IiI1i11I + IiI1i11I
 if 36 - 36: oooOo0oo0oo % Ii
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * i1i1I1IIii1II . Iii / ooOoO0O00
 if 50 - 50: i1IiiiI1iI / ooOoO0O00 % ii
 if 83 - 83: Ii1I * Ii1I + oooOo0oo0oo
 if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / o0ii1I
 if 20 - 20: oooOo0oo0oo * IIiIiII11i - OOooOOo - i1i1I1IIii1II * i1IiiiI1iI
 if 6 - 6: i1iIi + oooOo0oo0oo / I1ii11iIi11i + III1iiIii % IIiIiII11i / oO0o
 if 45 - 45: ii
 if 9 - 9: Iii . oO0o * ooOoO0O00 . ii
 if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
 if 11 - 11: o0o00Oo0O + oOo0O0Ooo
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ooOo0O0o0 )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 , OO0OOoooo0o in IIi :
  if 'movies' in OO0OOoooo0o :
   iIii ( OO0OOoooo0o + '-' + I11iI1i1I11I11 , OOOiiiiI , 90044 , iIIII )
 for OOOiiiiI in next :
  iiiiiI ( OOOiiiiI )
  if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / o0ii1I . ooOoO0O00
def O00oO0 ( ) :
 iIii ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 80006 , iiIi1IIiIi + 'Desi.png' )
def OOOO00OoooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , url , 80007 , iIIII )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def IIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  ooOoO00 ( url )
def Ii1iiI1 ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://www.join4films.com/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 OOOO00OoooO ( ooOo0O0o0 )
 if 76 - 76: o0ii1I * iI11I1II1I1I
 if 31 - 31: Ii + oooOo0oo0oo - o0o00Oo0O
 if 51 - 51: oO0o * ooOoO0O00 / o0ii1I * oooOo0oo0oo + i1iIi % Ii1I
 if 34 - 34: i1i1I1IIii1II * ii + o0ii1I + Ii
 if 22 - 22: ooOoO0O00
 if 24 - 24: Iii / oOo0O0Ooo * ooOoO0O00 % ii
 if 99 - 99: Ii . IIiIiII11i . ii
 if 59 - 59: Ii . ii / Iii * Ii1I + ii
 if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * IiI1i11I / oooOo0oo0oo
 if 95 - 95: III1iiIii * o0o00Oo0O * i1IiiiI1iI . ii % I1ii11iIi11i + Ii1I
 if 98 - 98: i1i1I1IIii1II . ii
 if 54 - 54: o0o00Oo0O / III1iiIii % i1iIi * ooOoO0O00 * o0o00Oo0O
 if 48 - 48: I11i . i1i1I1IIii1II % OOooOOo - OOooOOo
 if 33 - 33: Iii % IIiIiII11i + oO0o
 if 93 - 93: ooOoO0O00 . III1iiIii / oOo0O0Ooo + III1iiIii
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - IiI1i11I . I11i
def Oooooooo00o00 ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 100 - 100: i1IiiiI1iI % IIiIiII11i . o0ii1I % oO0o + Ii1I
def o0oOo0OO ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://imoviemax.se/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 OO0oo00oOO ( ooOo0O0o0 )
def I1iOO0O0O ( url ) :
 i1i1iIII11i = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , IiIIoOo in IIi :
  if I11iI1i1I11I11 in i1i1iIII11i :
   pass
  else :
   I1I1II1I11 ( I11iI1i1I11I11 + ' - ' + IiIIoOo + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   i1i1iIII11i . append ( I11iI1i1I11I11 )
   if 69 - 69: o0o00Oo0O / IIiIiII11i * ooOoO0O00
def oOIiiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , OoO in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 + ' - Views:' + OoO , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 71 - 71: i1IiiiI1iI - I11i - oooOo0oo0oo
  if 28 - 28: iI11I1II1I1I
def OO0oo00oOO ( url ) :
 iI11II1i1I1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , url in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 10075 , iIIII , iIIII , '' )
  iI11II1i1I1 . append ( I11iI1i1I11I11 )
  if 72 - 72: IiI1i11I - ii
def II1iII1i1i ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for o00oO0O0oo0o , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIi11I11 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIi11I11
  i1ioO = ( o00oO0O0oo0o ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( i1ioO , iIi11I11 , 10076 , img , img , '' )
  if 25 - 25: IiI1i11I . ii * iI11I1II1I1I . I11i / o0o00Oo0O + o0ii1I
def ooo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for oOo000O in IIi :
  if '=m' in oOo000O :
   O00Oooo00 ( oOo000O )
  elif 'php' in oOo000O :
   ooo0o0 ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( oOo000O )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for iII in IIi :
    O00Oooo00 ( oOo000O )
    if 93 - 93: o0o00Oo0O / i1iIi + oOo0O0Ooo
    if 20 - 20: III1iiIii / IiI1i11I % ii / iI11I1II1I1I + oOo0O0Ooo
    if 57 - 57: I11i / i1IiiiI1iI
def iiIiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIiiiI1iI = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOo0 , O0O0 in IIiiiI1iI :
  print 'there ><><><><><><><><><><><><'
  OOo0 = OOo0
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0O0 ) )
  for I11iI1i1I11I11 , O0oO0o0OOOOOO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + OOo0 + '[/COLOR] - ' + I11iI1i1I11I11 + ' - [COLOR' + ooOoOoo0O + ']' + O0oO0o0OOOOOO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 I1iIII1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOo0 , IiI1i11IiIiii in I1iIII1 :
  print 'there ><><><><><><><><><><><><'
  OOo0 = OOo0
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiI1i11IiIiii ) )
  for I11iI1i1I11I11 , O0oO0o0OOOOOO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + OOo0 + '[/COLOR] - ' + I11iI1i1I11I11 + ' - [COLOR' + ooOoOoo0O + ']' + O0oO0o0OOOOOO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 4 - 4: i1IiiiI1iI - oOo0O0Ooo % i1i1I1IIii1II / I11i % i1i1I1IIii1II * IIiIiII11i
   if 3 - 3: ooOoO0O00 / i1IiiiI1iI - ooOoO0O00 - Iii % I1ii11iIi11i - oOo0O0Ooo
   if 45 - 45: III1iiIii
def O0Oo0o000oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iIII1 in I1iIII1 :
  I11iI1i1I11I11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
  for I11iI1i1I11I11 in I11iI1i1I11I11 :
   I11iI1i1I11I11 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iIII1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I1i1i = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
  for I1i1i in I1i1i :
   I1i1i = 'http:' + I1i1i
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , '' , '' )
  if 7 - 7: iI11I1II1I1I - ooOoO0O00
  if 10 - 10: i1IiiiI1iI % o0o00Oo0O / oOo0O0Ooo % Iii
  if 25 - 25: IIiIiII11i / oO0o
  if 64 - 64: o0o00Oo0O % i1iIi
def O0Oo00OoOo ( url ) :
 if 40 - 40: I11i + Iii
 OoO000Oo0oO = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo000O , iIIII , I11iI1i1I11I11 , iiiIiiiI1 in IIi :
  I11iI1i1I11I11 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( oOo000O )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for o0OO , iiIii1I in i1Iii1i1I :
   I1IIIIIi1IIiI = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iiIii1I ) )
   for o00O0O in I1IIIIIi1IIiI :
    if I11iI1i1I11I11 in OoO000Oo0oO :
     pass
    else :
     Ii1I1i ( I11iI1i1I11I11 , o0OO , 8043 , iIIII , iIIII , o00O0O )
     Ii1IIiI1i ( 'movies' , 'INFO' )
     OoO000Oo0oO . append ( I11iI1i1I11I11 )
     if 26 - 26: I11i % oooOo0oo0oo + oooOo0oo0oo % Iii * Ii / IiI1i11I
     if 64 - 64: i1i1I1IIii1II % OOooOOo / IIiIiII11i % i1iIi - IiI1i11I
def I1II1IiI1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , Ii1IIiiIIi , o00O0O , i11I , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 10065 , Ii1IIiiIIi , i11I , o00O0O )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 26 - 26: oooOo0oo0oo * I1ii11iIi11i
def i1iI1Ii11Ii1 ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'https://www.youtube.com/results?search_query=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ooOo0O0o0 )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in next :
  OOOiiiiI = 'https://www.youtube.com' + OOOiiiiI
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , OOOiiiiI , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIIII , OOOiiiiI , I11iI1i1I11I11 , o0OoO0oo0O0o , iiIii1I in IIi :
  OOO00 . append ( I11iI1i1I11I11 )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  I1i1i = 'http:' + ( iIIII ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1i1i
  OOOiiiiI = 'http://www.youtube.com' + OOOiiiiI
  Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , I1i1i , iiIii1I )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIII , OOOiiiiI , I11iI1i1I11I11 , o0OoO0oo0O0o in IIi :
   print 'im doing it'
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   I1i1i = 'http:' + ( iIIII ) . replace ( 'https:' , '' )
   OOOiiiiI = 'http://www.youtube.com' + OOOiiiiI
   if '&' in OOOiiiiI :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( OOOiiiiI )
    I1iIII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iIII1 in I1iIII1 :
     I11iI1i1I11I11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
     for I11iI1i1I11I11 in I11iI1i1I11I11 :
      I11iI1i1I11I11 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OOOiiiiI = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iIII1 ) )
     for OOOiiiiI in OOOiiiiI :
      OOOiiiiI = 'https://www.youtube.com/w' + OOOiiiiI
     I1i1i = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
     for I1i1i in I1i1i :
      I1i1i = 'http:' + I1i1i
     Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , Oo00OOOOO , '' )
   elif I11iI1i1I11I11 in OOO00 :
    pass
   elif 'user' in OOOiiiiI or 'elete' in I11iI1i1I11I11 :
    pass
   elif 'hannel' in OOOiiiiI :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OOOiiiiI
    II11iIiIIIiI = OooOoooOo ( OOOiiiiI )
    ii1III1iiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIIII , OOOiiiiI , I11iI1i1I11I11 in ii1III1iiIi :
     if 'outube' in OOOiiiiI or 'list' in OOOiiiiI :
      pass
     elif 'atch' in OOOiiiiI :
      OOOiiiiI = ( OOOiiiiI ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIIII , 'http:' + iIIII , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , I1i1i , '' )
    if 35 - 35: oooOo0oo0oo + o0o00Oo0O . Ii % Ii1I
def ooO000OO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIIII , url , I11iI1i1I11I11 , o0OoO0oo0O0o , iiIii1I in IIi :
  OOO00 . append ( I11iI1i1I11I11 )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  I1i1i = 'http:' + ( iIIII ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1i1i
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , I1i1i , iiIii1I )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIII , url , I11iI1i1I11I11 , o0OoO0oo0O0o in IIi :
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   I1i1i = 'http:' + ( iIIII ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    I1iIII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iIII1 in I1iIII1 :
     I11iI1i1I11I11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
     for I11iI1i1I11I11 in I11iI1i1I11I11 :
      I11iI1i1I11I11 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iIII1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I1i1i = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iIII1 ) )
     for I1i1i in I1i1i :
      I1i1i = 'http:' + I1i1i
     Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , Oo00OOOOO , '' )
   elif I11iI1i1I11I11 in OOO00 :
    pass
   elif 'user' in url or 'elete' in I11iI1i1I11I11 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    ii1III1iiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIIII , url , I11iI1i1I11I11 in ii1III1iiIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIIII , 'http:' + iIIII , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + o0OoO0oo0O0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i , I1i1i , '' )
    if 43 - 43: i1iIi * i1IiiiI1iI % oooOo0oo0oo
    if 38 - 38: I1ii11iIi11i
    if 34 - 34: OOooOOo
def OoO0o00OOOOO ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 19 - 19: IiI1i11I * I1ii11iIi11i . IiI1i11I . oO0o / oO0o - i1i1I1IIii1II
def i11111iiiII1I ( ) :
 ivuesetup . iVueInt ( )
 if 13 - 13: oooOo0oo0oo / III1iiIii - oO0o / oooOo0oo0oo . ooOoO0O00
def IiI1i111i ( ) :
 iiiI1i1111II ( )
 return
 if 38 - 38: I1ii11iIi11i % Ii1I - IiI1i11I * iI11I1II1I1I / o0o00Oo0O
def iiiI1i1111II ( ) :
 if 9 - 9: Iii * I1ii11iIi11i . i1iIi * Ii - o0o00Oo0O
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 OoO00OOoOOOo0 = II1I . getSetting ( id = 'User' )
 oOoO00O = II1I . getSetting ( id = 'Pass' )
 I11I1I1i1i = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Oo0oOO0O00 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 o00OOo0o0O = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 I111Iii1 = "http://piesustv.net:8000/get.php?username=" + OoO00OOoOOOo0 + "&password=" + oOoO00O + "&type=m3u_plus&output=ts"
 i11iO0o0O00o0o = "http://piesustv.net:8000/xmltv.php?username=" + OoO00OOoOOOo0 + "&password=" + oOoO00O + "&type=m3u_plus&output=ts"
 if 6 - 6: Ii1I - i1i1I1IIii1II * Ii + OOooOOo / i1iIi % oooOo0oo0oo
 xbmc . executeJSONRPC ( I11I1I1i1i )
 xbmc . executeJSONRPC ( Oo0oOO0O00 )
 xbmc . executeJSONRPC ( o00OOo0o0O )
 if 38 - 38: oooOo0oo0oo % III1iiIii % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
 iIiIIi11iI = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 iIiIIi11iI . setSetting ( id = 'm3uUrl' , value = I111Iii1 )
 iIiIIi11iI . setSetting ( id = 'epgUrl' , value = i11iO0o0O00o0o )
 iIiIIi11iI . setSetting ( id = 'm3uCache' , value = "false" )
 iIiIIi11iI . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def ooo00o0o ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 56 - 56: OOooOOo % Ii1I - o0ii1I % iI11I1II1I1I
if 76 - 76: ii * ii - IiI1i11I - iI11I1II1I1I . ii / Ii1I
if 86 - 86: i1iIi
def oO0oo0O0 ( ) :
 if 66 - 66: oooOo0oo0oo - i1iIi - I1ii11iIi11i
 if 54 - 54: IiI1i11I . ooOoO0O00
 if 19 - 19: i1iIi % i1i1I1IIii1II
 if 22 - 22: i1i1I1IIii1II . IIiIiII11i . I1ii11iIi11i
 if 91 - 91: IIiIiII11i . oooOo0oo0oo + I11i
 if 8 - 8: oooOo0oo0oo * I1ii11iIi11i / IiI1i11I - oO0o - ii
 if 100 - 100: i1i1I1IIii1II . iI11I1II1I1I . iI11I1II1I1I
 if 55 - 55: i1i1I1IIii1II
 if 37 - 37: III1iiIii / Ii / I1ii11iIi11i
 if 97 - 97: i1IiiiI1iI . Iii / oOo0O0Ooo
 if 83 - 83: Iii - Ii1I * i1i1I1IIii1II
 if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
 if OO0o == "insert_username" :
  OO0OooOo = ii111iI1i1 ( )
  OO000 = IIiii11ii1II1 ( )
  I11 ( 'User' , OO0OooOo )
  I11 ( 'Pass' , OO000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  o0OO000O = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OO0OooOo , OO000 )
  o0OO000O = OooOoooOo ( o0OO000O )
  if o0OO000O == "" :
   O000o0000O = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   O00Ooo0O0OOOo = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   o0oooo0O = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , O000o0000O , O00Ooo0O0OOOo , o0oooo0O )
   oO0oo0O0 ( )
  else :
   O000o0000O = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   O00Ooo0O0OOOo = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   o0oooo0O = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % OO0OooOo )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , O000o0000O , O00Ooo0O0OOOo , o0oooo0O )
   xbmc . executebuiltin ( 'Container.Refresh' )
   iI1iIIIIIiIi1 ( )
 else :
  iI1iIIIIIiIi1 ( )
def ii111iI1i1 ( ) :
 iIioOo = xbmc . Keyboard ( '' , 'heading' , True )
 iIioOo . setHeading ( 'Enter Username' )
 iIioOo . setHiddenInput ( False )
 iIioOo . doModal ( )
 if ( iIioOo . isConfirmed ( ) ) :
  ooOo0o = iIioOo . getText ( )
  return ooOo0o
 else :
  return False
  if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / Iii + i1IiiiI1iI
  if 17 - 17: oooOo0oo0oo + IIiIiII11i
def IIiii11ii1II1 ( ) :
 iIioOo = xbmc . Keyboard ( '' , 'heading' , True )
 iIioOo . setHeading ( 'Enter Password' )
 iIioOo . setHiddenInput ( False )
 iIioOo . doModal ( )
 if ( iIioOo . isConfirmed ( ) ) :
  ooOo0o = iIioOo . getText ( )
  return ooOo0o
 else :
  return False
def I1i11I11Iii ( ) :
 I111Iii1 = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  i1i1I11I = urllib2 . urlopen ( I111Iii1 )
  print i1i1I11I . getcode ( )
  i1i1I11I . close ( )
  if 29 - 29: ooOoO0O00 % I11i . ooOoO0O00
  pass
  if 77 - 77: ooOoO0O00 * ii % IiI1i11I % I11i % i1iIi / Ii1I
 except urllib2 . HTTPError , I1i1iiiI1 :
  print I1i1iiiI1 . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def iI1iIIIIIiIi1 ( ) :
 iii ( )
 if 64 - 64: Ii . i1iIi
 if 93 - 93: o0o00Oo0O - oO0o . oOo0O0Ooo
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 64 - 64: OOooOOo + I11i
 if 65 - 65: IIiIiII11i / I1ii11iIi11i
 if 42 - 42: Ii . o0o00Oo0O
 if 75 - 75: i1IiiiI1iI + iI11I1II1I1I
def IiiiI1 ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 oo0o0000Oo0 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 I1IIIi = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 o0OO000O = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 o0OO000O = OooOoooOo ( o0OO000O )
 if not o0OO000O == "" :
  I1iOo00oOO00 = 'https://tinyurl.com/create.php?source=indexpage&url=' + oo0o0000Oo0 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( I1iOo00oOO00 ) )
  Iio0000O00oO0O = 'https://tinyurl.com/create.php?source=indexpage&url=' + I1IIIi + '&submit=Make+TinyURL%21&alias='
  oo0o0000Oo0 = OooOoooOo ( I1iOo00oOO00 )
  I1IIIi = OooOoooOo ( Iio0000O00oO0O )
  xbmc . log ( str ( I1IIIi ) )
  IiiI111I11 = oO0Ooooo000 ( oo0o0000Oo0 , '<div class="indent"><b>' , '</b>' )
  Iii1Iiii = oO0Ooooo000 ( I1IIIi , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % IiiI111I11 , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % Iii1Iiii )
 else :
  return
def i1i1Ii1IiIII ( ) :
 I1i11I11Iii ( )
 I1IIii11 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1I1 + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( O0OOO0ooO00o )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , OOOiiiiI , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def I1iii1 ( url ) :
 open = OooOoooOo ( iIiiiIIiii + url )
 OO0Oo00Oo = iIiO0O ( open , '<channel>' , '</channel>' )
 for oOOoooo in OO0Oo00Oo :
  if '<playlist_url>' in open :
   I11iI1i1I11I11 = oO0Ooooo000 ( oOOoooo , '<title>' , '</title>' )
   o0o0O00 = oO0Ooooo000 ( oOOoooo , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( I11iI1i1I11I11 ) ) . replace ( '?' , '' ) , o0o0O00 , 3 , icon , i11I , '' )
  else :
   I11iI1i1I11I11 = oO0Ooooo000 ( oOOoooo , '<title>' , '</title>' )
   I11iI1i1I11I11 = base64 . b64decode ( I11iI1i1I11I11 )
   O0o = oO0Ooooo000 ( oOOoooo , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = oO0Ooooo000 ( oOOoooo , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   o00O0O = oO0Ooooo000 ( oOOoooo , '<description>' , '</description>' )
   o00O0O = base64 . b64decode ( o00O0O )
   Ii1iIiIi1I11 = oO0Ooooo000 ( o00O0O , 'PLOT:' , '\n' )
   ii1I11 = oO0Ooooo000 ( o00O0O , 'CAST:' , '\n' )
   OOO0 = oO0Ooooo000 ( o00O0O , 'RATING:' , '\n' )
   I1Ii1 = oO0Ooooo000 ( o00O0O , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   I1Ii1 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( I1Ii1 )
   O0oo0oOoO00 = oO0Ooooo000 ( o00O0O , 'DURATION_SECS:' , '\n' )
   i1ii1iIi = oO0Ooooo000 ( o00O0O , 'GENRE:' , '\n' )
   I1I1Ii ( str ( I11iI1i1I11I11 ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , O0o , i11I , Ii1iIiIi1I11 , str ( I1Ii1 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( ii1I11 ) . split ( ) , OOO0 , O0oo0oOoO00 , i1ii1iIi )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 42 - 42: I11i - I1ii11iIi11i % Ii1I
I11ii1iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
i11ii111i1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 97 - 97: Ii + I1ii11iIi11i * oooOo0oo0oo % IiI1i11I . III1iiIii
def iiOo0 ( ) :
 I111Iii1 = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  i1i1I11I = urllib2 . urlopen ( I111Iii1 )
  print i1i1I11I . getcode ( )
  i1i1I11I . close ( )
  if 75 - 75: oO0o / o0ii1I + IIiIiII11i % III1iiIii . Ii
  pass
  if 76 - 76: IiI1i11I . III1iiIii % IiI1i11I - i1IiiiI1iI
 except urllib2 . HTTPError , I1i1iiiI1 :
  print I1i1iiiI1 . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 51 - 51: ii + I11i * iI11I1II1I1I * i1i1I1IIii1II / ooOoO0O00
 OOOiiiiI = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 I11IiI1i ( OOOiiiiI , i11ii111i1ii + "uide.xml" )
 if 81 - 81: iI11I1II1I1I / i1i1I1IIii1II . Ii * IIiIiII11i
 iiii111II = open ( I11ii1iI11 , 'r+' )
 input = open ( I11ii1iI11 ) . read ( ) . decode ( 'UTF-8' )
 o0oOOoo0O = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 iiii111II . write ( o0oOOoo0O )
 iiii111II . truncate ( )
 iiii111II . close ( )
 Oo ( )
 if 95 - 95: I1ii11iIi11i
def Oo ( ) :
 open = OooOoooOo ( i111 )
 all = iIiO0O ( open , '{"num' , 'direct' )
 for oOOoooo in all :
  if '"tv_archive":1' in oOOoooo :
   I11iI1i1I11I11 = oO0Ooooo000 ( oOOoooo , '"epg_channel_id":"' , '"' )
   O0o = oO0Ooooo000 ( oOOoooo , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = oO0Ooooo000 ( oOOoooo , 'stream_id":"' , '"' )
   I11iI1i1I11I11 = I11iI1i1I11I11 . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( I11iI1i1I11I11 , id , 90027 , O0o , i11I , I11iI1i1I11I11 )
   if 71 - 71: oO0o
   if 75 - 75: IiI1i11I
def II1iiI ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 o00O0o0O0O = open ( I11ii1iI11 )
 oOO0O00OoOo = ElementTree . parse ( o00O0o0O0O )
 I1i1I11 = "apples"
 import datetime as dt
 from datetime import time
 i1iiI = datetime . now ( ) - timedelta ( days = 5 )
 OOo0 = str ( i1iiI )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 iiIi1IiiIi1 = oOO0O00OoOo . findall ( "programme" )
 for IiI11I1Ii11II in iiIi1IiiIi1 :
  if name in IiI11I1Ii11II . attrib . get ( 'channel' ) :
   oo0ooOoOOoO = IiI11I1Ii11II . attrib . get ( 'start' )
   Oo0000o , iI1IiiiIIiiII , oOo000o = oo0ooOoOOoO . partition ( ' +' )
   OOo0 = str ( OOo0 ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   I1Ii1 , oOII1i1i1I1iII , ii1 = oo0ooOoOOoO . partition ( '2017' )
   I1I = IiI11I1Ii11II . find ( 'title' ) . text + oo0ooOoOOoO
   ii1 = ii1 [ : - 6 ]
   if Oo0000o > OOo0 :
    if Oo0000o < I1IIIii :
     o0oOo0000ooO = Oo0000o
     o0oOo0000ooO = o0oOo0000ooO [ : 4 ] + '/' + o0oOo0000ooO [ 4 : ]
     Oo0000o = Oo0000o [ : 4 ] + '-' + Oo0000o [ 4 : ]
     o0oOo0000ooO = o0oOo0000ooO [ : 7 ] + '/' + o0oOo0000ooO [ 7 : ]
     Oo0000o = Oo0000o [ : 7 ] + '-' + Oo0000o [ 7 : ]
     o0oOo0000ooO = o0oOo0000ooO [ : 10 ] + ' - ' + o0oOo0000ooO [ 10 : ]
     Oo0000o = Oo0000o [ : 10 ] + ':' + Oo0000o [ 10 : ]
     o0oOo0000ooO = o0oOo0000ooO [ : 15 ] + ':' + o0oOo0000ooO [ 15 : ]
     Oo0000o = Oo0000o [ : 13 ] + '-' + Oo0000o [ 13 : ]
     o0oOo0000ooO = o0oOo0000ooO [ : - 2 ]
     Oo0000o = Oo0000o [ : - 2 ]
     I1Io0oO0oo = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( Oo0000o ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     I1i1I11 = I1Io0oO0oo + str ( Oo0000o ) + "&duration=240"
     o0oOo0000ooO = '[COLOR blue]%s - [/COLOR]' % o0oOo0000ooO
     I1I = str ( o0oOo0000ooO ) + IiI11I1Ii11II . find ( 'title' ) . text
     o00O0O = IiI11I1Ii11II . find ( 'desc' ) . text
     Ii1I1i ( I1I , I1Io0oO0oo , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , o00O0O )
def ooOO00Oo ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 o0oooO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 o0oooO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 o0oooO . setProperty ( 'IsPlayable' , 'true' )
 o0oooO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0oooO )
def I11IiI1i ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 oO00OOOOOO0o = time . time ( )
 urllib . urlretrieve ( url , dest , lambda iIII , OoO0000 , III11iIIi : iIIii1I111iIii1i1 ( iIII , OoO0000 , III11iIIi , o0oOoO00o , oO00OOOOOO0o ) )
def iIIii1I111iIii1i1 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  o0Oo = min ( numblocks * blocksize * 100 / filesize , 100 )
  i1II11i1iI1 = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  OO0IIi1II11 = numblocks * blocksize / ( time . time ( ) - start_time )
  if OO0IIi1II11 > 0 :
   o0ooOOOo = ( filesize - numblocks * blocksize ) / OO0IIi1II11
  else :
   o0ooOOOo = 0
  OO0IIi1II11 = OO0IIi1II11 / 1024
  OOoOOo0oO = OO0IIi1II11 / 1024
  I1Ii1IIIiII = float ( filesize ) / ( 1024 * 1024 )
  iiII1IIii1i1 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( i1II11i1iI1 )
  I1i1iiiI1 = '[COLOR white]Speed:  %.02f Mb/s ' % OOoOOo0oO + '[/COLOR]'
  dp . update ( o0Oo , iiII1IIii1i1 , I1i1iiiI1 )
 except :
  o0Oo = 100
  dp . update ( o0Oo )
 if dp . iscanceled ( ) :
  i1iiiIIi11II = xbmcgui . Dialog ( )
  i1iiiIIi11II . ok ( "GenieTv" , 'The download was cancelled.' )
  if 55 - 55: Iii
  sys . exit ( )
  dp . close ( )
  if 93 - 93: Ii . I11i
def IiiIiI1IIi1IIIii ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OOO0o ( )
  if 80 - 80: III1iiIii + Iii + i1i1I1IIii1II % oO0o - I1ii11iIi11i - i1i1I1IIii1II
  if 7 - 7: I11i . Ii1I
  if 30 - 30: i1iIi - Ii + oOo0O0Ooo / I1ii11iIi11i % o0o00Oo0O
  if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
  if 47 - 47: Ii1I * i1i1I1IIii1II + iI11I1II1I1I - i1i1I1IIii1II / III1iiIii
  if 86 - 86: III1iiIii
  if 43 - 43: oOo0O0Ooo / IiI1i11I / i1iIi + iI11I1II1I1I + ii
  if 33 - 33: IIiIiII11i - III1iiIii - i1iIi
def OOO0o ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for OOOiiiiI in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def oO00oOoo00o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 III1I = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 o0I11iII = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOoOooOoOOOoo = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOIIiIi = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiiIiI = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iiiiI1IiI1I1 = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 Ii11Iii = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 OOOii = Iii1I11 ( )
 O0o0o = IiiiIi1111I ( )
 for url in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in III1I :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in o0I11iII :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOIIiIi :
  dt = datetime . fromtimestamp ( float ( oOIIiIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   oOo0OoOOo0 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOoOooOoOOOoo :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiiIiI :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iiiiI1IiI1I1 :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Ii11Iii :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + OOOii , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + O0o0o , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 45 - 45: I11i
 oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 58 - 58: oOo0O0Ooo * ooOoO0O00 % IIiIiII11i / o0o00Oo0O
def O0oo0ooo0 ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 iII1 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 77 - 77: ii + I11i
def o00O0o ( data ) :
 i1Ii1 = len ( data ) % 4
 if 75 - 75: ii * Ii
 if 67 - 67: i1IiiiI1iI / oO0o . ii
 if 51 - 51: IIiIiII11i . i1i1I1IIii1II . oO0o % IIiIiII11i
 if 41 - 41: OOooOOo - oooOo0oo0oo + i1iIi - ooOoO0O00
 if 6 - 6: IIiIiII11i
 if 7 - 7: ooOoO0O00
 if i1Ii1 != 0 :
  data += b'=' * ( 4 - i1Ii1 )
 return base64 . decodestring ( data )
def oO0Ooooo000 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : Oo00oo = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : Oo00oo = ''
 else :
  try : Oo00oo = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : Oo00oo = ''
 return Oo00oo
 if 79 - 79: Ii1I / o0o00Oo0O % I11i
 if 71 - 71: i1IiiiI1iI / oOo0O0Ooo / o0o00Oo0O
def iIiO0O ( text , start_with , end_with ) :
 Oo00oo = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return Oo00oo
def Iii1I11 ( ) :
 IiI = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 IiI . connect ( ( '8.8.8.8' , 0 ) )
 IiI = IiI . getsockname ( ) [ 0 ]
 return IiI
 if 34 - 34: o0o00Oo0O / oooOo0oo0oo
def IiiiIi1111I ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 OOOii = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( OOOii . group ( ) )
I1I1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
i111 = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
OOOoo0O00Oooo = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
I11iIIi = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
I111Ii11i11I = '&action=get_live_categories'
i11IoO0000O0Oo00O = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
O0OOO0ooO00o = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 42 - 42: Ii / oOo0O0Ooo - oO0o - i1iIi + IIiIiII11i % i1iIi
iIiiiIIiii = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
Ii1IIii = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
oooOOoo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
iI1iii1iIiiI = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / oooOo0oo0oo
def IiiIiiIIII ( ) :
 I1i11I11Iii ( )
 open = OooOoooOo ( oooOOoo )
 OO0Oo00Oo = iIiO0O ( open , '<channel>' , '</channel>' )
 for oOOoooo in OO0Oo00Oo :
  I11iI1i1I11I11 = oO0Ooooo000 ( oOOoooo , '<title>' , '</title>' )
  I11iI1i1I11I11 = base64 . b64decode ( I11iI1i1I11I11 )
  o0o0O00 = oO0Ooooo000 ( oOOoooo , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + I11iI1i1I11I11 + '[/COLOR]' , o0o0O00 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 88 - 88: oO0o . i1IiiiI1iI / Iii
def iIiI1I1 ( url ) :
 open = OooOoooOo ( iI1iii1iIiiI + url )
 OO0Oo00Oo = iIiO0O ( open , '<channel>' , '</channel>' )
 for oOOoooo in OO0Oo00Oo :
  I11iI1i1I11I11 = oO0Ooooo000 ( oOOoooo , '<title>' , '</title>' )
  I11iI1i1I11I11 = base64 . b64decode ( I11iI1i1I11I11 )
  xbmc . log ( str ( I11iI1i1I11I11 ) )
  O0o = oO0Ooooo000 ( oOOoooo , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o0o0O00 = oO0Ooooo000 ( oOOoooo , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  o00O0O = oO0Ooooo000 ( oOOoooo , '<description>' , '</description>' )
  o00O0O = base64 . b64decode ( o00O0O )
  oOoO = '('
  oOOo00Ooo0O = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , o0o0O00 , 222 , O0o , i11I , ( '[COLOR' + ooOoOoo0O + ']' + o00O0O + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oOOo00Ooo0O , '[COLORsteelblue]' ) . replace ( oOoO , '[COLORorangered]' ) )
  if 34 - 34: IIiIiII11i
def i1Oo ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( i11IoO0000O0Oo00O + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , type , oOo000O , iIIIIiiIii in IIi :
  iII = ( I11iIIi + oOo000O + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , iII , 222 , ( iIIIIiiIii ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def Ii11ii1 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo000OOooO0O , iiiIiiiI1I in IIi :
  if name == oOo000OOooO0O :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + iiiIiiiI1I , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def i111I1 ( name ) :
 OOOo0Oo0O = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , iIIII , OOOiiiiI in IIi :
  OOOiiiiI = ( OOOiiiiI ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( OOOiiiiI ) . strip ( ) , 222 , iIIII , iIIII , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 48 - 48: i1iIi % OOooOOo
  if 67 - 67: iI11I1II1I1I % oO0o + Ii
  if 46 - 46: oOo0O0Ooo . III1iiIii - Ii - i1IiiiI1iI
  if 97 - 97: IIiIiII11i % I1ii11iIi11i * III1iiIii
  if 51 - 51: I1ii11iIi11i % oooOo0oo0oo . I1ii11iIi11i
  if 72 - 72: o0ii1I % o0ii1I / oOo0O0Ooo
  if 40 - 40: I1ii11iIi11i - oooOo0oo0oo + i1IiiiI1iI - I11i % oOo0O0Ooo . i1iIi
  if 35 - 35: Ii + ii * iI11I1II1I1I . i1IiiiI1iI
  if 48 - 48: IiI1i11I * ooOoO0O00 % ii * o0ii1I * oO0o
  if 7 - 7: IiI1i11I . o0ii1I . IiI1i11I - i1IiiiI1iI
  if 33 - 33: i1iIi + ii - oO0o / ooOoO0O00 / ii
  if 82 - 82: Ii1I / oooOo0oo0oo - IiI1i11I / I1ii11iIi11i * oO0o
def ooO ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , OOOiiiiI , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 55 - 55: ii
  if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
  if 38 - 38: o0o00Oo0O
zip = oo00 . getSetting ( 'zip' )
ooOi1i1i11iI11II = xbmc . translatePath ( os . path . join ( zip ) )
def II1iiI1iI ( ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 74 - 74: III1iiIii - o0o00Oo0O / i1IiiiI1iI * o0ii1I % i1iIi . i1IiiiI1iI
  if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
  if 66 - 66: IiI1i11I / Ii * o0o00Oo0O
def O000Oo00 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  II1iiI1iI ( )
  iI1 = open ( url ) . read ( )
  oOoo = os . path . join ( ooOi1i1i11iI11II , description . split ( 'Your ' ) [ 1 ] )
  iiii111II = open ( oOoo , mode = 'w' )
  iiii111II . write ( iI1 )
  iiii111II . close ( )
 else :
  if 'guisettings.xml' in description :
   oOOoooo = open ( os . path . join ( ooOi1i1i11iI11II , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Oo00oo = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( Oo00oo ) . findall ( oOOoooo )
   for type , o00O0o00oo , iIiiII in IIi :
    iIiiII = iIiiII . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o00O0o00oo , iIiiII ) )
  else :
   oOoo = os . path . join ( url )
   iI1 = open ( os . path . join ( ooOi1i1i11iI11II , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iiii111II = open ( oOoo , mode = 'w' )
   iiii111II . write ( iI1 )
   iiii111II . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 13 - 13: IIiIiII11i
 if 55 - 55: I1ii11iIi11i % ooOoO0O00 * Iii
 if 95 - 95: oooOo0oo0oo / IIiIiII11i - I11i % i1IiiiI1iI . Iii
 if 63 - 63: iI11I1II1I1I / i1iIi
def II1i ( ) :
 OOoOooO0o = 1
 II1iiI1iI ( )
 I1IiiiI = xbmc . translatePath ( os . path . join ( ooOi1i1i11iI11II , 'Build Backup' , 'Full Backup' , '' ) )
 iIiI1111 = xbmc . translatePath ( os . path . join ( ooOi1i1i11iI11II , 'Build Backup' , 'my_full_backup.zip' ) )
 O0OO00 = xbmc . translatePath ( os . path . join ( ooOi1i1i11iI11II , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1IiiiI ) :
  os . makedirs ( I1IiiiI )
 i1111I = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i1111I ) : return False , 0
 OoO00oo0 = i1111I
 oOOO = xbmc . translatePath ( os . path . join ( I1IiiiI , OoO00oo0 + '.zip' ) )
 o00OoOooo = [ 'plugin.video.GenieTv' ]
 i1I1ii1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Iii1i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 ooOooo00O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 I1i1I1IIiIIi = "Creating full backup of existing build"
 iII1ii1IIII = "Creating Community Build"
 Oo0o0O0OOOo0 = "Archiving..."
 I1ii1i = ""
 OO00OoOO = "Please Wait"
 iiii1II1ii11 ( oOo0oooo00o , oOOO , iII1ii1IIII , Oo0o0O0OOOo0 , I1ii1i , OO00OoOO , Iii1i , ooOooo00O )
 time . sleep ( 1 )
 i1IIIII1 = xbmc . translatePath ( os . path . join ( I1IiiiI , OoO00oo0 + '_guisettings.zip' ) )
 IIIiiiiiI1I = zipfile . ZipFile ( i1IIIII1 , mode = 'w' )
 try :
  IIIiiiiiI1I . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 IIIiiiiiI1I . close ( )
 if OOoOooO0o == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iIiI1111 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oOOO + '[/COLOR]' )
  if 64 - 64: III1iiIii * iI11I1II1I1I . Ii1I / Iii * iI11I1II1I1I
def iiii1II1ii11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i1i111III1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 III1i1IIII1i = len ( sourcefile )
 i111IIIIIII1i = [ ]
 i1I1Iiii = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for I1iIIIiiii , I1111 , o00oO0o0oo0O in os . walk ( sourcefile ) :
  for file in o00oO0o0oo0O :
   i1I1Iiii . append ( file )
 Ooo00OOo000 = len ( i1I1Iiii )
 for I1iIIIiiii , I1111 , o00oO0o0oo0O in os . walk ( sourcefile ) :
  I1111 [ : ] = [ i1ooOO00o0 for i1ooOO00o0 in I1111 if i1ooOO00o0 not in exclude_dirs ]
  o00oO0o0oo0O [ : ] = [ iiii111II for iiii111II in o00oO0o0oo0O if iiii111II not in exclude_files ]
  for file in o00oO0o0oo0O :
   i111IIIIIII1i . append ( file )
   Ii1I1iIiiI1 = len ( i111IIIIIII1i ) / float ( Ooo00OOo000 ) * 100
   o0oOoO00o . update ( int ( Ii1I1iIiiI1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o00i111iiIiiIiI = os . path . join ( I1iIIIiiii , file )
   if not 'temp' in I1111 :
    if not 'plugin.program.originwizard' in I1111 :
     import time
     OOooooO = '01/01/1980'
     oOoo00 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o00i111iiIiiIiI ) ) )
     if oOoo00 > OOooooO :
      i1i111III1 . write ( o00i111iiIiiIiI , o00i111iiIiiIiI [ III1i1IIII1i : ] )
 i1i111III1 . close ( )
 o0oOoO00o . close ( )
 if 29 - 29: oooOo0oo0oo / OOooOOo . iI11I1II1I1I / Iii % OOooOOo % IiI1i11I
 if 49 - 49: IIiIiII11i / III1iiIii - o0ii1I
def IiIII ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 92 - 92: oOo0O0Ooo % IiI1i11I
 if 31 - 31: ii - i1i1I1IIii1II / i1IiiiI1iI
def oo00o000O ( ) :
 iii ( )
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  iII1111III1I ( )
 if O0O0ooOOO == 1 :
  iiiI1I1iIIIi1 ( )
 if O0O0ooOOO == 2 :
  oo00ooOoo ( )
 if O0O0ooOOO == 3 :
  i1iI1Ii11Ii1 ( )
  if 66 - 66: ii + I11i . ooOoO0O00 * IiI1i11I
  if 92 - 92: Iii / i1IiiiI1iI
  if 4 - 4: i1IiiiI1iI
  if 11 - 11: ii + ooOoO0O00 / o0ii1I
  if 25 - 25: o0ii1I . oooOo0oo0oo
  if 14 - 14: o0o00Oo0O / Iii . oO0o % IiI1i11I . i1i1I1IIii1II
  if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
  if 27 - 27: IIiIiII11i + i1iIi . OOooOOo - i1IiiiI1iI
  if 54 - 54: OOooOOo . I1ii11iIi11i
def Ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0O0ooOOO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0O0ooOOO == 2 :
   iIIi11 ( )
  if O0O0ooOOO == 3 :
   iIiiII1Ii1ii ( )
  if O0O0ooOOO == 4 :
   iIIi1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0O0ooOOO == 5 :
   OoOo0O00 ( )
  if O0O0ooOOO == 6 :
   iI1i1iI1iI ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0O0ooOOO == 7 :
   I1IIiIi ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0O0ooOOO == 8 :
   OOOOoOoO ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0O0ooOOO == 9 :
   OO000o0oOoo0o ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , iiIi1IIiIi + 'Thunder.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
   if 19 - 19: oOo0O0Ooo - OOooOOo . I1ii11iIi11i . ooOoO0O00 - i1i1I1IIii1II
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 93 - 93: III1iiIii % Ii1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 31 - 31: IIiIiII11i + oooOo0oo0oo - ii . Iii
  if 28 - 28: o0ii1I . Ii1I
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 77 - 77: Ii1I % IIiIiII11i
def OOo00o0oo0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   IIIIiII ( )
  if O0O0ooOOO == 1 :
   iIIi ( )
  if O0O0ooOOO == 2 :
   i1II1 ( )
  if O0O0ooOOO == 3 :
   iII11 ( OOOiiiiI )
  if O0O0ooOOO == 4 :
   O00OO00OOOoO ( OOOiiiiI )
  if O0O0ooOOO == 5 :
   OoOO0o ( )
  if O0O0ooOOO == 6 :
   IiI11Ii1iI ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0O0ooOOO == 7 :
   ooOo0 ( )
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
  if 61 - 61: IIiIiII11i
  if 48 - 48: oooOo0oo0oo
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 26 - 26: IiI1i11I * i1IiiiI1iI * i1i1I1IIii1II * OOooOOo
 if 48 - 48: IiI1i11I % Ii . ii * III1iiIii % oO0o . IiI1i11I
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
 if 6 - 6: o0o00Oo0O . i1iIi - i1i1I1IIii1II / Ii
 if 84 - 84: Iii / Ii1I * I11i * oO0o * oooOo0oo0oo * o0o00Oo0O
def OoOooOo00o ( ) :
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
 if 28 - 28: Ii1I + Ii1I % OOooOOo
def iiOO0O0Ooo ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 12 - 12: Iii
def I11iIi1i1I1i1 ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 14 - 14: Iii
 if 18 - 18: oOo0O0Ooo
 if 23 - 23: ii * IIiIiII11i
def oOOOOO0 ( ) :
 iii ( )
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  IIi1I1 ( )
 if O0O0ooOOO == 0 :
  oO00o0oOoo ( OOOiiiiI )
 if O0O0ooOOO == 0 :
  oOOI1 ( OOOiiiiI )
  if 63 - 63: oO0o . i1i1I1IIii1II + i1IiiiI1iI . OOooOOo / Ii / IiI1i11I
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + oooOo0oo0oo
  if 31 - 31: o0ii1I * I11i * o0ii1I + oO0o * I11i . i1IiiiI1iI
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 89 - 89: ii * o0ii1I * oOo0O0Ooo . i1iIi * o0ii1I / IiI1i11I
def iioo ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for iIIII , I11iI1i1I11I11 in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iIIII , iIIII , '' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 21 - 21: ooOoO0O00
def OOOO00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( O00oo0o0000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 5 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
def IIi1I1 ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 61 - 61: oOo0O0Ooo + i1i1I1IIii1II % i1IiiiI1iI % iI11I1II1I1I - ii
def iIIiI1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ooOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 4 - 4: ii + IiI1i11I % o0o00Oo0O + iI11I1II1I1I % IiI1i11I * Ii
def III1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1IIIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 79 - 79: I1ii11iIi11i - ii % i1IiiiI1iI + ii - Iii % OOooOOo
def iIIOOo0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiOo0ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 73 - 73: IIiIiII11i + oooOo0oo0oo * IiI1i11I / IiI1i11I
def OoOo0O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 39 - 39: i1IiiiI1iI . oO0o % i1iIi . oooOo0oo0oo / IiI1i11I * oO0o
def oO00o0oOoo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 40 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 80 - 80: o0ii1I + Iii + o0ii1I
def I11iIiIii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OooooIIIiI1iIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 5 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 75 - 75: oooOo0oo0oo % IIiIiII11i
def oOOo0O00o ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  IIIIi1Iii1iIi ( )
 if O0O0ooOOO == 1 :
  ii1IIi1iI1ii1 ( )
 if O0O0ooOOO == 2 :
  o00iIIiIi111iI ( )
  if 40 - 40: OOooOOo + oO0o % ii * I11i / OOooOOo + ii
  if 91 - 91: i1iIi - i1i1I1IIii1II + i1i1I1IIii1II
  if 14 - 14: Ii1I * i1IiiiI1iI % ooOoO0O00 / Ii1I
  if 48 - 48: I1ii11iIi11i
def ii1IIi1iI1ii1 ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , OO00oO0o0 in IIi :
  iIii ( 'Android Apps' + OO00oO0o0 , 'https://www.apkfiles.com' + OOOiiiiI , 30035 , iiIi1IIiIi + 'apps.png' )
 for OOOiiiiI , OO00oO0o0 in i1Iii1i1I :
  iIii ( 'Android Games' + OO00oO0o0 , 'https://www.apkfiles.com' + OOOiiiiI , 30035 , iiIi1IIiIi + 'GAMES.png' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def o0oOo ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if '/cat' in url :
   iIii ( ( I11iI1i1I11I11 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def O0OoOo0oO0o ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if '/app' in url :
   iIii ( ( I11iI1i1I11I11 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def I11iIi1i1IIi ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 o0o0O00 = url
 if "page=" in str ( url ) :
  o0o0O00 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  if 'apk' in url :
   Ii1I1i ( ( I11iI1i1I11I11 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iIIII )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , o0o0O00 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def II11I ( name , url ) :
 IIii11Ii1i1I = o0o0 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  OOooo00oo ( name , url , 'Brackets' )
def o00iIIiIi111iI ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'https://www.apkfiles.com/search?q=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 I11iIi1i1IIi ( ooOo0O0o0 )
 if 42 - 42: o0ii1I * o0o00Oo0O / i1i1I1IIii1II
def IiiiI11 ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( OoooOOo0oOO , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , I11iI1i1I11I11 + '.apk' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 44 - 44: oooOo0oo0oo % iI11I1II1I1I
def iiiiIi111 ( url ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , I11iI1i1I11I11 + '.mp4' )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 41 - 41: oOo0O0Ooo / III1iiIii . I1ii11iIi11i / III1iiIii
 if 49 - 49: ii - III1iiIii
def Iiii11 ( name , url , description ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o0OOOoO0 = os . path . join ( oOOooOoo , name )
 try :
  os . remove ( o0OOOoO0 )
 except :
  pass
 downloader . download ( url , o0OOOoO0 , o0oOoO00o )
 o00000O = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o00000O
 print '======================================='
 extract . all ( o0OOOoO0 , o00000O , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 if 33 - 33: Ii1I
 if 54 - 54: i1iIi * Ii1I . IIiIiII11i / oooOo0oo0oo % oooOo0oo0oo
 if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % i1IiiiI1iI
 if 53 - 53: ooOoO0O00
def IIIIi1Iii1iIi ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , OOOiiiiI , iIIIIiiIii , i11I , OO0oOoo in IIi :
  Ii1I1i ( I11iI1i1I11I11 , OOOiiiiI , 80003 , iIIIIiiIii , iiIi1IIiIi + 'APKToolsB.png' , OO0oOoo )
def iiIII1i1 ( apk , ret = None ) :
 if apk == "kodi" :
  oOOo0OOoOO0 = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( oOOo0OOoOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   IiIi = IIi [ 0 ] [ 0 ]
   OoO00oo0 = IIi [ 0 ] [ 1 ]
   IIi1IiiIi1III = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( IiIi , OoO00oo0 )
  if ret == 'version' : return IiIi
  else : return IIi1IiiIi1III
 elif apk == "spmc" :
  IiIiIiiIIii = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( IiIiIiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  IiIi = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  IIi1IiiIi1III = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( IiIi , IiIi )
  if ret == 'version' : return IiIi
  else : return IIi1IiiIi1III
def OOooo00oo ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  OOo00O00o0O0 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOo00O00o0O0 : iI1III ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I1I111 = name
  if OOo00O00o0O0 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not iII1ii1 ( url ) == True : iI1III ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % I1I111 , '' , 'Please Wait' )
   o0OOOoO0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( o0OOOoO0 )
   except : pass
   downloader . download ( url , o0OOOoO0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    IIIiiiiiI1I = zipfile . ZipFile ( o0OOOoO0 )
    for file in IIIiiiiiI1I . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as iiii111II :
       I1iIIIiiI = file . split ( '/' ) [ 1 ]
       iiii111II . write ( IIIiiiiiI1I . read ( file ) )
       xbmc . sleep ( 500 )
       iiii111II . close ( )
       try :
        os . remove ( o0OOOoO0 )
       except :
        pass
       o0OOOoO0 = os . path . join ( i1iIIi1 , I1iIIIiiI )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o0OOOoO0 + '")' )
  else : iI1III ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iI1III ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 86 - 86: ooOoO0O00
 if 33 - 33: OOooOOo % Ii * oooOo0oo0oo
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - i1i1I1IIii1II . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
 if 75 - 75: oO0o % ii
def iiiIooo0o00o ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  OOOiiiiI = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + OOOiiiiI )
  O0oOOo0 ( ( I11iI1i1I11I11 ) . replace ( '_' , ' ' ) , OOOiiiiI )
  if 71 - 71: Ii % iI11I1II1I1I
def O0oOOo0 ( name , url ) :
 if OO ( ) == 'android' :
  OOo00O00o0O0 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOo00O00o0O0 : iI1III ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1I111 = name
  if OOo00O00o0O0 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not iII1ii1 ( url ) == True : iI1III ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % I1I111 , '' , 'Please Wait' )
   o0OOOoO0 = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( o0OOOoO0 )
   except : pass
   downloader . download ( url , o0OOOoO0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o0OOOoO0 + '")' )
  else : iI1III ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iI1III ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 42 - 42: Ii + i1IiiiI1iI - I11i
 if 2 - 2: I11i . o0ii1I % OOooOOo
def OO00O00o0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 5 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 100 - 100: oO0o % OOooOOo / Iii * o0o00Oo0O - i1i1I1IIii1II
 if 34 - 34: IiI1i11I % Ii + Ii - IiI1i11I
def oo0O0o00o0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 30015 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 2 - 2: IIiIiII11i + ooOoO0O00
def oO0OO00 ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 iIi11I11 = url
 iIIII = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oOo000O , I11iI1i1I11I11 in IIi :
  if '.mp4' in I11iI1i1I11I11 :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + oOo000O , 222 , iIIII , fanart , '' )
  if 'description' in I11iI1i1I11I11 :
   Ii1I1i ( 'Read Description' , url + '/' + oOo000O , 30017 , iIIII , fanart , '' )
  if 'images' in I11iI1i1I11I11 :
   I1I1II1I11 ( 'View Images' , url + '/' + oOo000O , 30018 , iIIII , fanart , '' )
  if 'url' in I11iI1i1I11I11 :
   Ii1I1i ( 'Install Build On Android' , url + '/' + oOo000O , 30016 , iIIII , fanart , '' )
  if 'url' in I11iI1i1I11I11 :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + oOo000O , 30019 , iIIII , fanart , '' )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 16 - 16: ii / i1i1I1IIii1II . o0ii1I * i1iIi - oOo0O0Ooo
def iiIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oo0O0O ( url )
  if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
def O0oIii11IiiIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oO00O0o0oOOO ( url )
  if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
def Ii1o0OOOoo0000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for ooOo0o in IIi :
  o0OIiII ( 'Description:' , ooOo0o )
  if 19 - 19: ii . oOo0O0Ooo + i1IiiiI1iI - oOo0O0Ooo / oOo0O0Ooo % III1iiIii
def IiIIIii1i1iI ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oOo000O , I11iI1i1I11I11 in IIi :
  if 'png' in I11iI1i1I11I11 :
   Ii1I1i ( 'image' , '' , '' , url + '/' + oOo000O , url + '/' + oOo000O , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 99 - 99: iI11I1II1I1I - i1i1I1IIii1II - OOooOOo / iI11I1II1I1I * I1ii11iIi11i - i1i1I1IIii1II
def o0ooo0oooO ( name , url , description ) :
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
 if 89 - 89: ooOoO0O00
 if 19 - 19: i1iIi / I11i % III1iiIii - o0ii1I
def oO00O0o0oOOO ( url ) :
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
 IIIIiII ( )
 if 14 - 14: Ii1I - Ii * i1IiiiI1iI
def oo0O0O ( url ) :
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
 IIIIiII ( )
 if 39 - 39: ii
def i1iIII1IIi ( name , url , description ) :
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
 IIIIiII ( )
 if 63 - 63: IIiIiII11i . i1IiiiI1iI % III1iiIii + IIiIiII11i
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
  oO0OOoOO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  iiii111II . write ( oO0OOoOO . rstrip ( '\r\n' ) + '\n' )
def IIIIiII ( ) :
 O0O0ooOOO = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0O0ooOOO == 0 : return
 elif O0O0ooOOO == 1 : pass
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
  if 97 - 97: ooOoO0O00
  if 46 - 46: Ii1I
  if 30 - 30: oO0o / o0o00Oo0O * I11i * i1IiiiI1iI + ii * IiI1i11I
def oOOI1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( url ) :
  for file in o00oO0o0oo0O :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOOoooo = open ( ( os . path . join ( iIIi1I1Ii1 , file ) ) ) . read ( )
    ooOOo0O0o00o00 = oOOoooo . replace ( oOo0oooo00o , 'special://home/' )
    iiii111II = open ( ( os . path . join ( iIIi1I1Ii1 , file ) ) , mode = 'w' )
    iiii111II . write ( str ( ooOOo0O0o00o00 ) )
    iiii111II . close ( )
 IIIIiII ( )
 if 90 - 90: i1IiiiI1iI . IIiIiII11i . Ii1I
def iIIi11 ( ) :
 iIii ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 iIii ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 iIii ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 32 - 32: i1iIi - oO0o . IiI1i11I . IiI1i11I % ooOoO0O00 * o0ii1I
def o0o0I11 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def i1iiiiIIIi ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def Ii11Ii1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in i1Iii1i1I :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + I11iI1i1I11I11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + I11iI1i1I11I11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iIIII )
def III ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  ooOoO00 ( url )
def O0oo0OOO0O0 ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1
 o0o0ooOO0 = 'https://www.radionomy.com/en/search/index?query=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( o0o0ooOO0 )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + I11iI1i1I11I11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OOOiiiiI , 70005 , iIIII )
  if 99 - 99: iI11I1II1I1I
  if 81 - 81: Ii1I + oooOo0oo0oo
def OoOo0O00 ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.listenlive.eu/' + OOOiiiiI , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def iIIi1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 if 11 - 11: Ii1I % I1ii11iIi11i * i1IiiiI1iI - i1i1I1IIii1II + Ii1I
 if 80 - 80: iI11I1II1I1I - I1ii11iIi11i % i1IiiiI1iI % I1ii11iIi11i + oOo0O0Ooo % o0ii1I
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , O00O00oO , url , I11O0O0o in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' [COLORorangered] ' + I11O0O0o + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[CR]' + O00O00oO + '[CR]' + I11O0O0o + '[/COLOR]' )
  if 45 - 45: OOooOOo
def oo0OoOO000O ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.toonjet.com/' + OOOiiiiI , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0o0OoOoOo0 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( IIii11Ii1i1I )
 for url , iIIII in IIi :
  if 'ol.gif' in iIIII :
   pass
  elif 'link_block_' in iIIII :
   pass
  elif '.png' in iIIII :
   pass
  else :
   iIii ( ( iIIII ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  iIii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11iiI11I1II ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 70 - 70: Ii1I . III1iiIii
  if 41 - 41: I11i % I1ii11iIi11i
def o00oOo0OoO0oO ( ) :
 I1IIii11 ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 I1IIii11 ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 84 - 84: ooOoO0O00 / ooOoO0O00 - ooOoO0O00 . i1i1I1IIii1II . oO0o * Ii1I
def oOO000000oO0 ( ) :
 I1IIii11 ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 I1IIii11 ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 I1IIii11 ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 94 - 94: i1iIi + iI11I1II1I1I
def OOo0Oo0O00O ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , OOOiiiiI , OOoOOO0 in IIi :
  if 'Parent' in I11iI1i1I11I11 :
   pass
  elif '2' in OOoOOO0 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 18 - 18: o0o00Oo0O - III1iiIii + oooOo0oo0oo . o0o00Oo0O
def O00O000oOO0oO ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , OOOiiiiI , OOoOOO0 in IIi :
  if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
   if '1' in OOoOOO0 :
    I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOoOOO0 :
    I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOoOOO0 :
    I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 88 - 88: I11i . oOo0O0Ooo % i1i1I1IIii1II . I1ii11iIi11i % i1iIi . i1i1I1IIii1II
    if 53 - 53: ooOoO0O00 % o0ii1I - ii / OOooOOo - iI11I1II1I1I
def I1II1iIi ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , OOOiiiiI , OOoOOO0 in IIi :
  if '1' in OOoOOO0 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOoOOO0 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOoOOO0 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: OOooOOo * oO0o / i1iIi / oOo0O0Ooo - o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: i1i1I1IIii1II
def oo0OoO ( url ) :
 oOo000O = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in i1Iii1i1I :
  if 'mp3' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOo000O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOo000O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOo000O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in I11iI1i1I11I11 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOo000O + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 3 - 3: III1iiIii - ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I
   if 58 - 58: III1iiIii % iI11I1II1I1I / Ii % I11i . i1IiiiI1iI * IiI1i11I
   if 32 - 32: ii + I11i
def o0000OOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOo000O = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  if 'Parent' in I11iI1i1I11I11 :
   pass
  elif '.db' in I11iI1i1I11I11 :
   pass
  elif '.jpg' in I11iI1i1I11I11 :
   pass
  elif '.html' in I11iI1i1I11I11 :
   pass
  elif '.doc' in I11iI1i1I11I11 :
   pass
  elif 'mp3' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOo000O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOo000O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOo000O + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 56 - 56: ooOoO0O00 + ii % oO0o
   if 36 - 36: IiI1i11I * Iii * o0o00Oo0O * oooOo0oo0oo - I11i / Ii1I
def oooOo0OO ( ) :
 I1IIii11 ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 I1IIii11 ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 I1IIii11 ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 9 - 9: iI11I1II1I1I
def O0000ooO0OO0Oooo0o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OOOiiiiI + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iIIII :
   pass
  else :
   I1IIii11 ( iIIII , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OOOiiiiI ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iIIII + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 83 - 83: I11i % I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . Iii * o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: Ii - i1IiiiI1iI
 if 21 - 21: Ii * IiI1i11I / i1iIi % IiI1i11I * I1ii11iIi11i
def oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  if '</a>' in I11iI1i1I11I11 :
   pass
  elif '(' in I11iI1i1I11I11 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 89 - 89: III1iiIii - ooOoO0O00 - III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: oO0o % oO0o
def IIIII1IIiIi ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
   if '</a>' in I11iI1i1I11I11 :
    pass
   elif '(' in I11iI1i1I11I11 :
    I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
    if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if '</a>' in I11iI1i1I11I11 :
   pass
  elif '(' in I11iI1i1I11I11 :
   I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: Ii1I . i1IiiiI1iI . o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: Ii1I / i1IiiiI1iI
 if 35 - 35: I1ii11iIi11i * i1i1I1IIii1II / ii + o0o00Oo0O / ii / oooOo0oo0oo
def IiO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oOo000O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oOo000O )
  if 69 - 69: i1i1I1IIii1II - i1IiiiI1iI / I1ii11iIi11i
def iII1oOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in IIi :
  if '<p align' in I11iI1i1I11I11 :
   pass
  elif '&nbsp;' in I11iI1i1I11I11 :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 65 - 65: i1i1I1IIii1II * i1i1I1IIii1II / Iii + i1i1I1IIii1II % i1iIi + OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: I11i
 if 37 - 37: i1i1I1IIii1II
def iii1IIIiiiI ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'ongoing' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def I1Ii1iI1IiI1I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1ii1iIi = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iIIII , iIIII , I11iI1i1I11I11 )
 for url , I11iI1i1I11I11 in i1ii1iIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def o0OOOoO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0ooOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ooo0OO0OOoooOo00 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 oOoOo0O0o0O = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in ooo0OO0OOoooOo00 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , I11iI1i1I11I11 in O0ooOO :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def iiII1i1i1I1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 88 - 88: o0o00Oo0O % III1iiIii . III1iiIii . i1IiiiI1iI / ooOoO0O00
def Oo0Oo0O ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if '9cart' in OOOiiiiI :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 16 - 16: I1ii11iIi11i * i1IiiiI1iI
def O0ooO0o ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOoOooOoOOOoo = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   iIii ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   iIii ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , I11iI1i1I11I11 in OOoOooOoOOOoo :
  if '9cart' in url :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 42 - 42: ii - OOooOOo - oooOo0oo0oo * i1IiiiI1iI
def OO0iii111 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 20003 , iIIII )
 for url , I11iI1i1I11I11 in i1Iii1i1I :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 59 - 59: i1iIi * i1IiiiI1iI
def O0oooOo0000o0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   iIii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 95 - 95: i1i1I1IIii1II
def oOo0ooO0O0oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 31 - 31: Ii + o0ii1I % OOooOOo
def I1Io0Oo00 ( url ) :
 url = cloudflare . source ( url )
 O00Oooo00 ( url )
 if 34 - 34: o0ii1I * oOo0O0Ooo + Iii * OOooOOo - IIiIiII11i
def OOoo0ooOo000oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  O00Oooo00 ( url )
  if 81 - 81: ii - III1iiIii - III1iiIii + iI11I1II1I1I % Iii . ii
  if 75 - 75: o0o00Oo0O
def OoO00oo00 ( ) :
 if 96 - 96: o0ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 24 - 24: o0o00Oo0O
def oo00ooOoo ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 33 - 33: ii + i1i1I1IIii1II * IIiIiII11i / oooOo0oo0oo
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 87 - 87: ii
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
   if 'Dad!' in I11iI1i1I11I11 :
    pass
   elif 'Family Guy' in I11iI1i1I11I11 :
    pass
   elif '2 Stupid' in I11iI1i1I11I11 :
    pass
   elif 'The Zelfs' in I11iI1i1I11I11 :
    pass
   elif 'A Clone' in I11iI1i1I11I11 :
    pass
   elif 'A.T.O.M' in I11iI1i1I11I11 :
    pass
   elif 'Almost Naked' in I11iI1i1I11I11 :
    pass
   elif 'Angry Kid' in I11iI1i1I11I11 :
    pass
   elif 'Annoying Orange' in I11iI1i1I11I11 :
    pass
   elif 'Aqua Teen' in I11iI1i1I11I11 :
    pass
   elif 'Assy Mcgee' in I11iI1i1I11I11 :
    pass
   elif 'Astroblast' in I11iI1i1I11I11 :
    pass
   elif 'Atomic Betty' in I11iI1i1I11I11 :
    pass
   elif 'Axe Cop' in I11iI1i1I11I11 :
    pass
   elif 'Baby Playpen' in I11iI1i1I11I11 :
    pass
   elif 'Beavis and Butt' in I11iI1i1I11I11 :
    pass
   elif 'Celebrity Deathmatch' in I11iI1i1I11I11 :
    pass
   elif 'Clerks The' in I11iI1i1I11I11 :
    pass
   elif 'Crapston Villas' in I11iI1i1I11I11 :
    pass
   elif 'Duckman:' in I11iI1i1I11I11 :
    pass
   elif 'Stripperella' in I11iI1i1I11I11 :
    pass
   elif 'Vixen' in I11iI1i1I11I11 :
    pass
   else :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 1 - 1: iI11I1II1I1I / I11i
    if 98 - 98: o0o00Oo0O % oOo0O0Ooo / ii * Ii1I - i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 51 - 51: IiI1i11I + Iii
def iiiI1i11Ii ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if 'Dad!' in I11iI1i1I11I11 :
   pass
  elif 'Family Guy' in I11iI1i1I11I11 :
   pass
  elif '2 Stupid' in I11iI1i1I11I11 :
   pass
  elif 'The Zelfs' in I11iI1i1I11I11 :
   pass
  elif 'A Clone' in I11iI1i1I11I11 :
   pass
  elif 'A.T.O.M' in I11iI1i1I11I11 :
   pass
  elif 'Almost Naked' in I11iI1i1I11I11 :
   pass
  elif 'Angry Kid' in I11iI1i1I11I11 :
   pass
  elif 'Annoying Orange' in I11iI1i1I11I11 :
   pass
  elif 'Aqua Teen' in I11iI1i1I11I11 :
   pass
  elif 'Assy Mcgee' in I11iI1i1I11I11 :
   pass
  elif 'Astroblast' in I11iI1i1I11I11 :
   pass
  elif 'Atomic Betty' in I11iI1i1I11I11 :
   pass
  elif 'Axe Cop' in I11iI1i1I11I11 :
   pass
  elif 'Baby Playpen' in I11iI1i1I11I11 :
   pass
  elif 'Beavis and Butt' in I11iI1i1I11I11 :
   pass
  elif 'Celebrity Deathmatch' in I11iI1i1I11I11 :
   pass
  elif 'Clerks The' in I11iI1i1I11I11 :
   pass
  elif 'Crapston Villas' in I11iI1i1I11I11 :
   pass
  elif 'Duckman:' in I11iI1i1I11I11 :
   pass
  elif 'Stripperella' in I11iI1i1I11I11 :
   pass
  elif 'Vixen' in I11iI1i1I11I11 :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: IIiIiII11i * o0o00Oo0O % oOo0O0Ooo . Iii
def O0ooO0O00oo0 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIii11Ii1i1I )
 for iIIII in i1Iii1i1I :
  II1i1iI = iIIII
 OOoOooOoOOOoo = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IIii11Ii1i1I )
 for url in OOoOooOoOOOoo :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 10007 , II1i1iI )
  if 5 - 5: OOooOOo + IiI1i11I * i1iIi
  if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . i1iIi / I1ii11iIi11i - Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
def i1IiIoo0o0ooOoo00O ( url , IMAGE ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  print I11iI1i1I11I11 + '     ' + url
  if 'easy' in url :
   iI1ii1 ( url )
   if 81 - 81: i1iIi + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * i1IiiiI1iI
   if 98 - 98: Ii1I - ii / oOo0O0Ooo . i1iIi - ooOoO0O00
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 60 - 60: OOooOOo % OOooOOo
def iI1ii1 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  ooOoO00 ( url )
  if 2 - 2: o0ii1I . o0o00Oo0O - i1i1I1IIii1II + III1iiIii
  if 96 - 96: o0ii1I + o0ii1I
  if 28 - 28: IiI1i11I
def ii1Iiii1I ( ) :
 if 54 - 54: i1iIi - iI11I1II1I1I - Iii % o0ii1I / IIiIiII11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 80 - 80: Ii % iI11I1II1I1I / Ii
def OOoOO0ooo0O ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  if 'elete' in I11iI1i1I11I11 :
   pass
  else :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 222 , iIIII )
   if 17 - 17: i1iIi
def IIi1IIII ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiOo0ooooO0o00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , iIIIIIi11Ii , i1iII1IiiIiI1 in IiOo0ooooO0o00 :
  for ii1iIIiii1 in iIIIIIi11Ii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OOOiiiiI , I11iI1i1I11I11 in oOOo :
    if 'tube' in OOOiiiiI :
     pass
    elif 'stage' in OOOiiiiI :
     oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIIIi11Ii + '   -   ' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIIII , )
    elif 'vee' in OOOiiiiI :
     pass
     if 85 - 85: ooOoO0O00 . ooOoO0O00
def Ii11i1I1 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiOo0ooooO0o00 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , iIIIIIi11Ii , i1iII1IiiIiI1 in IiOo0ooooO0o00 :
  oOOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OOOiiiiI , I11iI1i1I11I11 in oOOo :
   if 'tube' in OOOiiiiI :
    pass
   elif 'stage' in OOOiiiiI :
    oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIIIi11Ii + '   -   ' + I11iI1i1I11I11 + '[/COLOR]' , ( OOOiiiiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIIII )
   elif 'vee' in OOOiiiiI :
    pass
    if 70 - 70: Ii1I . Ii1I / Iii . Ii1I
    if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IiIIi1I1I11Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o0OO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( o0OO ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in o0OO :
  III1I11i1iIi ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 3 - 3: I11i - ii + IiI1i11I . Iii
  if 88 - 88: Iii - IiI1i11I
  if 68 - 68: I1ii11iIi11i % i1i1I1IIii1II . III1iiIii - I11i / ooOoO0O00 / ii
  if 34 - 34: Iii % I1ii11iIi11i + o0ii1I
  if 93 - 93: o0ii1I - i1IiiiI1iI % o0o00Oo0O
  if 11 - 11: Ii
  if 6 - 6: IIiIiII11i
def I111IiiIi1 ( ) :
 if 1 - 1: i1iIi % I1ii11iIi11i . i1i1I1IIii1II
 OoOooo ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 OoOooo ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
def I1iiIIii ( ) :
 OoOooo ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 OoOooo ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 90 - 90: III1iiIii * Iii % IIiIiII11i / oooOo0oo0oo
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def o00oO0O000 ( ) :
 if 75 - 75: I1ii11iIi11i . IiI1i11I
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 iI11i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 55 - 55: Iii * oOo0O0Ooo - i1i1I1IIii1II
 for o0oo0O in iI11i :
  I1iiIII = oO0 + o0oo0O + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( I1iiIII )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , i11I , I11iI1i1I11I11 in IIi :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    I11i11 ( I11iI1i1I11I11 , OOOiiiiI , 222 , Ii1IIiiIIi , i11I , o00O0O )
    if 68 - 68: o0o00Oo0O * iI11I1II1I1I / i1IiiiI1iI
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 65 - 65: oooOo0oo0oo - oOo0O0Ooo * i1IiiiI1iI
    if 99 - 99: oOo0O0Ooo
def OO000O000OOO ( ) :
 if 26 - 26: Iii * o0ii1I % oOo0O0Ooo + IiI1i11I
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 iI11i = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 38 - 38: IiI1i11I - I1ii11iIi11i / o0ii1I + i1i1I1IIii1II . IiI1i11I + III1iiIii
 for o0oo0O in iI11i :
  iIiii1iI1Ii = oO0 + o0oo0O + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( iIiii1iI1Ii )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for I11iI1i1I11I11 , o00O0O , OOOiiiiI , iIIII , i11I , IIiii in IIi :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    OoOooo ( I11iI1i1I11I11 , OOOiiiiI , IIiii , iIIII , i11I , o00O0O )
    if 82 - 82: Ii
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 13 - 13: o0o00Oo0O % IIiIiII11i
    if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
def iIIiIiii1 ( ) :
 if 87 - 87: o0o00Oo0O - i1i1I1IIii1II % I1ii11iIi11i
 IIii11Ii1i1I = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , o00O0O , OOOiiiiI , iIIII , i11I , IIiii in IIi :
  OoOooo ( I11iI1i1I11I11 , OOOiiiiI , IIiii , iIIII , i11I , o00O0O )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def ooIIi111I ( url ) :
 if 75 - 75: Ii * oOo0O0Ooo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoo = ( '%s%s' % ( OOOO0O0OoO0O0 , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in IIi :
  iIi1I1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for OOOOoO00o0O in iIi1I1 :
   if OOOOoO00o0O == url :
    I11iI1i1I11I11 = ( '[COLORred]Watched - [/COLOR]' + I11iI1i1I11I11 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I11i11 ( I11iI1i1I11I11 , url , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
  if 30 - 30: IIiIiII11i
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 34 - 34: ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: Ii + o0ii1I
  if 81 - 81: Ii % oOo0O0Ooo / IiI1i11I % oO0o / i1IiiiI1iI % iI11I1II1I1I
def IIII1iI1IiIiI ( url ) :
 if 43 - 43: IIiIiII11i
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , o00O0O , url , iIIII , i11I , IIiii in IIi :
  OoOooo ( I11iI1i1I11I11 , url , IIiii , iIIII , i11I , o00O0O )
  if 95 - 95: i1IiiiI1iI + III1iiIii * iI11I1II1I1I
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0ii1I
  if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: o0ii1I
def I11i11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIiII1 = [ ]
  IIIIIiII1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = False )
 return ooo0
 if 19 - 19: o0o00Oo0O + i1i1I1IIii1II + I11i
def OoOooo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 81 - 81: iI11I1II1I1I
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIiII1 = [ ]
  IIIIIiII1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = True )
 return ooo0
if 51 - 51: I11i . Ii1I * o0ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
if 44 - 44: Ii % i1IiiiI1iI % i1i1I1IIii1II + Iii * i1i1I1IIii1II . o0ii1I
if 89 - 89: ii % IIiIiII11i - oO0o % Ii
if 7 - 7: III1iiIii
if 15 - 15: I1ii11iIi11i + IiI1i11I + oOo0O0Ooo * I11i
if 33 - 33: I11i * I1ii11iIi11i
if 88 - 88: i1IiiiI1iI % oooOo0oo0oo - OOooOOo - OOooOOo . oOo0O0Ooo
if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - i1IiiiI1iI
if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - o0ii1I
if 59 - 59: III1iiIii % i1i1I1IIii1II
if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
if 15 - 15: i1iIi / i1iIi % ii . i1IiiiI1iI
if 93 - 93: Ii1I * Ii1I / ii
if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
def ii1iIi111i1 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 57 - 57: oOo0O0Ooo
def ooOOoO0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Ii11i = [ ]
 try :
  if 62 - 62: Iii . IIiIiII11i * o0o00Oo0O + ooOoO0O00 * ii + ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  ii1iIi111i1 ( 'Making Favorites File' )
  Ii11i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOOoooo = open ( i1I1iI , "w" )
  oOOoooo . write ( json . dumps ( Ii11i ) )
  oOOoooo . close ( )
 else :
  ii1iIi111i1 ( 'Appending Favorites' )
  oOOoooo = open ( i1I1iI ) . read ( )
  iiII = json . loads ( oOOoooo )
  iiII . append ( ( name , url , iconimage , fanart , mode ) )
  ooOOo0O0o00o00 = open ( i1I1iI , "w" )
  ooOOo0O0o00o00 . write ( json . dumps ( iiII ) )
  ooOOo0O0o00o00 . close ( )
  if 39 - 39: o0o00Oo0O . Iii
  if 45 - 45: i1i1I1IIii1II + I11i + III1iiIii / o0ii1I + I11i
def i1II1I1I1 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  Ii11i = [ ]
  ii1iIi111i1 ( 'Making Favorites File' )
  Ii11i . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oOOoooo = open ( i1I1iI , "w" )
  oOOoooo . write ( json . dumps ( Ii11i ) )
  oOOoooo . close ( )
 else :
  iiiiII = json . loads ( open ( i1I1iI ) . read ( ) )
  I1Ii1IIIiII = len ( iiiiII )
  for I1I1iI11ii in iiiiII :
   I11iI1i1I11I11 = I1I1iI11ii [ 0 ]
   OOOiiiiI = I1I1iI11ii [ 1 ]
   Ii1IIiiIIi = I1I1iI11ii [ 2 ]
   try :
    iIi1II111I1i1 = I1I1iI11ii [ 3 ]
    if iIi1II111I1i1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     iIi1II111I1i1 = Ii1IIiiIIi
    else :
     iIi1II111I1i1 = i11I
   try : Iio0o0o = I1I1iI11ii [ 5 ]
   except : Iio0o0o = None
   try : IiiIOoO00o0o0oo0o = I1I1iI11ii [ 6 ]
   except : IiiIOoO00o0o0oo0o = None
   if 13 - 13: Iii % i1IiiiI1iI . ooOoO0O00
   if I1I1iI11ii [ 4 ] == 0 :
    I1I1II1I11 ( I11iI1i1I11I11 , OOOiiiiI , '' , Ii1IIiiIIi , i11I , '' , 'fav' )
   else :
    I1I1II1I11 ( I11iI1i1I11I11 , OOOiiiiI , I1I1iI11ii [ 4 ] , Ii1IIiiIIi , i11I , '' , 'fav' )
    if 1 - 1: I11i % I11i . iI11I1II1I1I . ii . III1iiIii . IiI1i11I
def oooo ( name ) :
 iiII = json . loads ( open ( i1I1iI ) . read ( ) )
 for i11I1II in range ( len ( iiII ) ) :
  if iiII [ i11I1II ] [ 0 ] == name :
   del iiII [ i11I1II ]
   ooOOo0O0o00o00 = open ( i1I1iI , "w" )
   ooOOo0O0o00o00 . write ( json . dumps ( iiII ) )
   ooOOo0O0o00o00 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 65 - 65: I1ii11iIi11i . OOooOOo . oooOo0oo0oo % I11i + oO0o
 if 53 - 53: I1ii11iIi11i * Iii - o0ii1I % oO0o - OOooOOo - IiI1i11I
def iII1 ( ) :
 IiIIIIiI = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 o00OooooOOOO = open ( IiIIIIiI , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 o00OooooOOOO . write ( r'[' + IiII + ']' + '\n' )
 for I11iI1i1I11I11 , iIIII , oo000o , OOOiiiiI in IIi :
  OOOiiiiI = ( OOOiiiiI + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iIIIII = ( I11iI1i1I11I11 + '=plugin://' + IiII + '/?url=' + OOOiiiiI + '&mode=10012&name=' + ( I11iI1i1I11I11 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iIIII ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iIIII ) . replace ( ' ' , '' ) + '+&amp;description=' )
  o00OooooOOOO . write ( iIIIII + '\n' )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
  if 22 - 22: oO0o . OOooOOo % IIiIiII11i - o0o00Oo0O
def oO0o00O ( ) :
 IIii11Ii1i1I = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI in IIi :
  iIii ( '24/7' , OOOiiiiI , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 7 - 7: I1ii11iIi11i * oO0o - IIiIiII11i % i1IiiiI1iI . I1ii11iIi11i . I1ii11iIi11i
def iiII1iIi1ii1i ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  Ii1I1i ( I11iI1i1I11I11 , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def iIiiII1Ii1ii ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  Ii1I1i ( I11iI1i1I11I11 , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def iII1iii ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  Ii1I1i ( I11iI1i1I11I11 , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def Oooooo0O00o ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  Ii1I1i ( I11iI1i1I11I11 , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def i11IiI1 ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  Ii1I1i ( I11iI1i1I11I11 , OOOiiiiI , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 62 - 62: i1iIi * Ii1I / IiI1i11I * oooOo0oo0oo / oooOo0oo0oo - IiI1i11I
  if 59 - 59: o0ii1I % IiI1i11I / IIiIiII11i + oOo0O0Ooo * i1iIi
def o0o0O0o0O ( ) :
 if 16 - 16: I11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 37 - 37: oOo0O0Ooo + ii . i1IiiiI1iI + oOo0O0Ooo . III1iiIii
def IIio0O0 ( ) :
 if 59 - 59: IIiIiII11i * ii - ii
 IIii11Ii1i1I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 , O0oO0o0OOOOOO in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 + '  -  ' + ( O0oO0o0OOOOOO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOiiiiI , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 33 - 33: o0o00Oo0O . Ii % I11i
  if 50 - 50: i1iIi
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
def oo0ooO0O ( ) :
 if 83 - 83: I1ii11iIi11i / i1iIi
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
 if 11 - 11: I11i - IIiIiII11i % i1i1I1IIii1II . IIiIiII11i
def OO0I11IIi1I1 ( url ) :
 iIi11I11 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( iIi11I11 )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
  if 8 - 8: Ii1I % oO0o % i1i1I1IIii1II . Ii1I * Ii1I
  if 94 - 94: Ii + ii
  if 20 - 20: Ii
def oOOOoo0 ( ) :
 if 43 - 43: Ii1I * oooOo0oo0oo
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 OOOiiiiI = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( OOOiiiiI )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 1 - 1: oO0o * i1iIi + III1iiIii . i1i1I1IIii1II / i1iIi
   if 91 - 91: o0ii1I + Iii - I1ii11iIi11i % OOooOOo . IiI1i11I
   if 51 - 51: oooOo0oo0oo / Iii
def O0OOO00O0OO0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo000O , i1I11iIiII , iI1I11 , I11iI1i1I11I11 in IIi :
  OoOO = ( iI1I11 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IioOo0O = ( i1I11iIiII ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1i1III11IiIi = 'Season ' + IioOo0O + 'Episode ' + OoOO + I11iI1i1I11I11
  oooo0OoOo ( i1i1III11IiIi , oOo000O )
  if 69 - 69: i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: iI11I1II1I1I
  if 75 - 75: oooOo0oo0oo - oO0o
def oooo0OoOo ( name , url ) :
 oOo000O = url
 oo0Ii111ii1 = name
 o0o = cloudflare . source ( oOo000O )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for o0OO , OoOo00Oo0oo0O in i1Iii1i1I :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + oo0Ii111ii1 + OoOo00Oo0oo0O + '[/COLOR]' , o0OO , 222 , iiIi1IIiIi + 'dtv.png' )
  if 39 - 39: Iii * i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: i1iIi % oOo0O0Ooo . oooOo0oo0oo - i1iIi / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % i1i1I1IIii1II / Iii % o0o00Oo0O
def IiiI1iiiiI1iI ( ) :
 if 100 - 100: i1IiiiI1iI - OOooOOo
 if 78 - 78: ii - OOooOOo . Ii
 if 36 - 36: i1i1I1IIii1II * IiI1i11I + III1iiIii * IiI1i11I . Ii1I - iI11I1II1I1I
 if 14 - 14: Iii * i1i1I1IIii1II + Ii
 if 84 - 84: IiI1i11I / IIiIiII11i
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 38 - 38: oOo0O0Ooo
def iiiii1i1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0OooO0oo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iIIII , '' , '' )
 for url in O0OooO0oo :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 81 - 81: IiI1i11I / Ii1I
def OOO0oOo00o0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0OooO0oo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  iIIII = 'http://watchepisodes.cc/' + iIIII
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 10093 , iIIII , iIIII , '' )
 for url in O0OooO0oo :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 43 - 43: o0o00Oo0O / i1IiiiI1iI . iI11I1II1I1I - OOooOOo
def iiII1iiI ( url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI1I11 , url , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iI1I11 + ' - ' + I11iI1i1I11I11 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iIIII , '' , '' )
  if 57 - 57: Ii - Iii / i1iIi / I11i * Ii * I11i
def IiIii1iIIII ( url , iconimage ) :
 iIIII = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in IIi :
  if 'player' in I11iI1i1I11I11 :
   pass
  elif 'vod' in I11iI1i1I11I11 :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iIIII , '' , '' )
   if 92 - 92: III1iiIii / iI11I1II1I1I
   if 43 - 43: i1iIi + ii + iI11I1II1I1I / ii
   if 65 - 65: oooOo0oo0oo
   if 14 - 14: i1iIi
   if 75 - 75: iI11I1II1I1I % i1iIi / oooOo0oo0oo - IiI1i11I % Ii
   if 11 - 11: Iii . o0ii1I
def iIiiiii1i ( ) :
 if 87 - 87: oooOo0oo0oo + oooOo0oo0oo
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / o0ii1I . Iii * I11i
 if 21 - 21: IIiIiII11i
 if 29 - 29: OOooOOo % o0ii1I
 if 7 - 7: ooOoO0O00 / III1iiIii / IiI1i11I
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: i1iIi + i1i1I1IIii1II - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: III1iiIii
 if 52 - 52: o0o00Oo0O + i1iIi
 if 11 - 11: ooOoO0O00 / i1IiiiI1iI * Ii1I * i1IiiiI1iI * i1iIi - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . o0ii1I
 if 26 - 26: i1i1I1IIii1II - i1iIi % I1ii11iIi11i - i1i1I1IIii1II + III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 33 - 33: o0ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * III1iiIii
 if 21 - 21: o0o00Oo0O * i1iIi % oO0o
def Iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIII1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1iIII1 ) )
 for url , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 41 - 41: III1iiIii - o0o00Oo0O * i1i1I1IIii1II * IIiIiII11i . Iii - i1IiiiI1iI
def ii111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 49 - 49: III1iiIii % I11i . Ii1I / oooOo0oo0oo . o0ii1I * Ii1I
def II1i1iii1iiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  if 'episode' in url :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 62 - 62: Iii
  if 73 - 73: o0ii1I % oO0o * oooOo0oo0oo
def oooo0O ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iII11OO0OoO0OOoOo = 'http://www.watchseriesgo.to/search/' + ii1iIIiii1 . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( iII11OO0OoO0OOoOo )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'watch online' in I11iI1i1I11I11 :
   pass
  else :
   print OOOiiiiI
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.watchseriesgo.to' + OOOiiiiI , 10044 , iIIII , '' , '' )
   if 84 - 84: i1i1I1IIii1II / o0ii1I * IiI1i11I
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 20 - 20: OOooOOo % o0o00Oo0O
def Oo0OOO00oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 , iI1I11 , o00O0O in IIi :
  oo00O0 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iI1I11 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo00O0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iIIII , '' , o00O0O )
  if 80 - 80: III1iiIii . I11i
def IIiIiI1i11iiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  oo00O0 = ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo00O0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 64 - 64: o0ii1I
def IIiiiIi1ii11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iIIII , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 9 - 9: o0o00Oo0O * o0ii1I
def o0O00o00Ooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIII1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1I11iIiII , IiOo0ooooO0o00 in I1iIII1 :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IiOo0ooooO0o00 ) )
  for url , I11iI1i1I11I11 in IIi :
   oo00O0 = ( i1I11iIiII ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo00O0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: oooOo0oo0oo . IIiIiII11i - o0ii1I - ii
class ooOoOoOoo ( ) :
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 57 - 57: IIiIiII11i . ooOoO0O00
  oo00O0 = name
  self . Get_Sources ( OOOiiiiI , oo00O0 )
  if 33 - 33: IiI1i11I + I1ii11iIi11i % Iii . i1i1I1IIii1II
  if 6 - 6: III1iiIii + Ii1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , I11iI1i1I11I11 in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + OOOiiiiI
   self . Get_site_link ( URL , season_name )
   if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  OOoOooOoOOOoo = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in OOoOooOoOOOoo :
   self . main ( url , season_name )
   if 13 - 13: iI11I1II1I1I * I11i - Ii
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oo0O0OO0Oooo = 'DACLIPS'
   if oo0O0OO0Oooo in ooOoOoOoo . source_list :
    pass
   else :
    self . daclips ( url , season_name , oo0O0OO0Oooo )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    oo0O0OO0Oooo = 'THEVIDEO'
    if oo0O0OO0Oooo in ooOoOoOoo . source_list :
     pass
    else :
     self . thevideo ( url , season_name , oo0O0OO0Oooo )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     oo0O0OO0Oooo = 'ALLMYVIDEOS'
     if oo0O0OO0Oooo in ooOoOoOoo . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , oo0O0OO0Oooo )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      oo0O0OO0Oooo = 'VIDSPOT'
      if oo0O0OO0Oooo in ooOoOoOoo . source_list :
       pass
      else :
       self . vidspot ( url , season_name , oo0O0OO0Oooo )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       oo0O0OO0Oooo = 'VODLOCKER'
       if oo0O0OO0Oooo in ooOoOoOoo . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , oo0O0OO0Oooo )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        oo0O0OO0Oooo = 'VIDTO'
        if oo0O0OO0Oooo in ooOoOoOoo . source_list :
         pass
        else :
         self . vidto ( url , season_name , oo0O0OO0Oooo )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 7 - 7: IIiIiII11i - Ii1I / Iii % ii + ooOoO0O00
       else :
        if 'youwatch' in url :
         oo0O0OO0Oooo = 'YouWatch'
         if oo0O0OO0Oooo in ooOoOoOoo . source_list :
          pass
         else :
          self . youwatch ( url , season_name , oo0O0OO0Oooo )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 42 - 42: Iii + ooOoO0O00 - o0ii1I / III1iiIii . IiI1i11I
          if 30 - 30: I1ii11iIi11i + o0ii1I % Ii * ooOoO0O00 + oOo0O0Ooo % oooOo0oo0oo
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for II1i111 , I11iI1i1I11I11 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % i1IiiiI1iI
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 , I11iI1i1I11I11 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 78 - 78: Ii1I + ii - oOo0O0Ooo * OOooOOo * IiI1i11I
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 7 - 7: oooOo0oo0oo . III1iiIii . i1IiiiI1iI / o0ii1I / I1ii11iIi11i
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 83 - 83: Iii / I1ii11iIi11i
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 23 - 23: iI11I1II1I1I
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . youplay ( II1i111 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for II1i111 in IIi :
   self . Printer ( II1i111 , season_name , source_name )
   if 10 - 10: Iii - I11i % ii - Ii1I
 def Printer ( self , Link , season_name , source_name ) :
  if 64 - 64: oO0o / oOo0O0Ooo
  if Link in ooOoOoOoo . List :
   pass
  elif source_name in ooOoOoOoo . source_list :
   pass
  else :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   ooOoOoOoo . List . append ( Link )
   ooOoOoOoo . source_list . append ( source_name )
   if 23 - 23: Iii * i1IiiiI1iI * I11i - oOo0O0Ooo % OOooOOo + I11i
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 41 - 41: III1iiIii * ii . i1iIi % Ii
   if 11 - 11: iI11I1II1I1I . i1IiiiI1iI - I1ii11iIi11i / Iii + IIiIiII11i
   if 29 - 29: Iii . Ii + ooOoO0O00 - o0ii1I + o0o00Oo0O . oOo0O0Ooo
   if 8 - 8: I11i
   if 78 - 78: ooOoO0O00 - I1ii11iIi11i
def I1iii11 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 48 - 48: o0ii1I - ii + i1IiiiI1iI % I11i - OOooOOo . oOo0O0Ooo
def i11iII11I1III ( url ) :
 I1iiii1IiI1i1 = '20'
 ii1iii1 = [ ]
 IiII1II1 = '                                                    '
 Oo0ooO000Oo = '        '
 I1I1II1I11 ( IiII1II1 + 'pl' + Oo0ooO000Oo + 'w' + Oo0ooO000Oo + 'd' + Oo0ooO000Oo + 'l' + Oo0ooO000Oo + 'f' + Oo0ooO000Oo + 'a' + Oo0ooO000Oo + 'pts' , '' , '' , '' , '' , '' )
 IIii11Ii1i1I = i111iiI1ii ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOoOOooO0 , I1IiiI11 , iIII1II11I1 , i1ooOO00o0 , O000oOo0OO , iiii111II , oOOoooo , oo00O000 , o0o00OO0oOoO in IIi :
  II1IiiI = ooO0O0OOO ( I1IiiI11 )
  IiIIIOOo00O0O = ooO0O0OOO ( iIII1II11I1 )
  IIIIiI1i1111iI1i = ooO0O0OOO ( i1ooOO00o0 )
  OoO00o = ooO0O0OOO ( O000oOo0OO )
  Oo0o0OO0O0o = ooO0O0OOO ( iiii111II )
  oooOO0 = ooO0O0OOO ( oOOoooo )
  ii1iii1 . append ( OOOoOOooO0 [ 0 ] )
  iiIi1iIiI = len ( ii1iii1 )
  IIi1iii = int ( len ( IiII1II1 ) - len ( OOOoOOooO0 ) - 2 )
  if len ( ii1iii1 ) >= 10 :
   IIi1iii = IIi1iii - 1
  if len ( ii1iii1 ) <= int ( I1iiii1IiI1i1 ) :
   Ii1I1i ( str ( iiIi1iIiI ) + ' ' + OOOoOOooO0 + IiII1II1 [ 0 : IIi1iii ] + I1IiiI11 + II1IiiI + iIII1II11I1 + IiIIIOOo00O0O + i1ooOO00o0 + IIIIiI1i1111iI1i + O000oOo0OO + OoO00o + iiii111II + Oo0o0OO0O0o + oOOoooo + oooOO0 + ' ' + o0o00OO0oOoO , '' , '' , '' , '' , '' )
   if 50 - 50: ii / oO0o % iI11I1II1I1I
   if 41 - 41: Ii1I % Ii1I + III1iiIii . IiI1i11I % i1IiiiI1iI * i1iIi
def ooO0O0OOO ( space ) :
 if len ( space ) > 1 :
  IiIIoOo = len ( '        ' ) - len ( space ) + 1
  space = int ( IiIIoOo ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 57 - 57: o0ii1I . i1IiiiI1iI . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
def oo0OO0Oo000oo ( ) :
 if 38 - 38: IiI1i11I + i1iIi
 if 32 - 32: i1iIi - ii + oO0o
 if 90 - 90: Ii1I / ii % Ii - III1iiIii
 if 30 - 30: IiI1i11I
 if 44 - 44: OOooOOo . oooOo0oo0oo
 if 84 - 84: i1IiiiI1iI - Iii * OOooOOo
 if 52 - 52: IiI1i11I . III1iiIii - Ii1I * iI11I1II1I1I % I11i / i1iIi
 if 18 - 18: OOooOOo % i1i1I1IIii1II % oO0o / IiI1i11I
 if 88 - 88: IiI1i11I * oooOo0oo0oo / Ii / ooOoO0O00
 if 76 - 76: o0ii1I . Iii - oooOo0oo0oo + OOooOOo * oO0o % i1IiiiI1iI
 if 24 - 24: iI11I1II1I1I % I1ii11iIi11i % Ii
 if 55 - 55: IiI1i11I
 if 19 - 19: ii / oooOo0oo0oo * Ii - oOo0O0Ooo
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
 if 40 - 40: IiI1i11I
 if 62 - 62: i1iIi / oooOo0oo0oo
 if 74 - 74: IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i + oooOo0oo0oo
 if 92 - 92: Iii % i1IiiiI1iI
 if 18 - 18: i1iIi + i1IiiiI1iI / oooOo0oo0oo / i1i1I1IIii1II + iI11I1II1I1I % III1iiIii
 if 94 - 94: Iii
 if 37 - 37: i1i1I1IIii1II
 if 52 - 52: Ii1I * oOo0O0Ooo . oooOo0oo0oo + ooOoO0O00 % i1i1I1IIii1II / iI11I1II1I1I
 if 68 - 68: i1IiiiI1iI - OOooOOo . Ii + I11i
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
 if 33 - 33: Iii . I1ii11iIi11i
 if 89 - 89: IiI1i11I + ooOoO0O00 - III1iiIii + i1iIi . IIiIiII11i
 if 85 - 85: iI11I1II1I1I - o0ii1I * I1ii11iIi11i . i1i1I1IIii1II + i1IiiiI1iI
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IiI1i11I / IiI1i11I
 if 43 - 43: oOo0O0Ooo
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + o0ii1I * Iii / i1i1I1IIii1II
 if 18 - 18: i1iIi
 if 92 - 92: oO0o % iI11I1II1I1I / III1iiIii * IiI1i11I . ooOoO0O00 + i1i1I1IIii1II
 if 24 - 24: III1iiIii . IiI1i11I * III1iiIii % Ii . Ii + ooOoO0O00
 if 64 - 64: iI11I1II1I1I / III1iiIii / I1ii11iIi11i - Ii1I
 if 100 - 100: III1iiIii + ooOoO0O00 * oO0o
 if 64 - 64: i1i1I1IIii1II * Ii . I1ii11iIi11i
 if 52 - 52: I1ii11iIi11i / i1iIi / IiI1i11I - I11i / IiI1i11I
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
 if 72 - 72: ii . I11i + o0o00Oo0O
 if 46 - 46: OOooOOo * Iii / i1i1I1IIii1II + I1ii11iIi11i + III1iiIii
 if 95 - 95: I11i - o0ii1I
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
 if 19 - 19: OOooOOo . oooOo0oo0oo . ii
 if 79 - 79: oooOo0oo0oo * i1iIi * oOo0O0Ooo * Ii1I / Ii1I
 if 62 - 62: i1iIi * o0ii1I % Ii1I - ooOoO0O00 - Ii1I
 if 24 - 24: oooOo0oo0oo
 if 71 - 71: III1iiIii - ooOoO0O00
 if 56 - 56: OOooOOo + i1i1I1IIii1II
 if 74 - 74: IiI1i11I / i1IiiiI1iI / IIiIiII11i - IiI1i11I / i1i1I1IIii1II % Iii
 if 19 - 19: III1iiIii % ii + ii
 if 7 - 7: ooOoO0O00
 if 91 - 91: OOooOOo - OOooOOo . III1iiIii
 if 33 - 33: i1IiiiI1iI - iI11I1II1I1I / o0ii1I % o0o00Oo0O
 if 80 - 80: III1iiIii % ii - III1iiIii
 if 27 - 27: i1IiiiI1iI - I11i * Ii1I - oOo0O0Ooo
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OOOiiiiI , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIIII , Oo00OOOOO , '' )
  if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IiI1i11I . o0ii1I
def Ooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIII1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iIII1 in I1iIII1 :
  ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1iIII1 ) )
  for OOoo0oo000oo in ii1 :
   OOoo0oo000oo = OOoo0oo000oo
  OOOooOO0oO = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
  for iIiIi1 , iIIII , time , iiiIIIIiI1iiI in OOOooOO0oO :
   ii1III1iiIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iiiIIIIiI1iiI )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoo0oo000oo + ' - ' + iIiIi1 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iIIII , Oo00OOOOO , ( str ( ii1III1iiIi ) ) )
   if 13 - 13: Iii . oO0o
 Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if 73 - 73: o0ii1I * ii * Iii - Ii
def oOOO00 ( ) :
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
 if 78 - 78: o0ii1I
def i11Ii ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  i1iii1I1I = I11iI1i1I11I11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I11iI1i1I11I11 :
   pass
  else :
   i1iii1I1I = I11iI1i1I11I11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + i1iii1I1I + '[/COLOR]' , url , 10013 , iIIII )
 for url , iIIII , I11iI1i1I11I11 in i1Iii1i1I :
  i1iii1I1I = I11iI1i1I11I11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I11iI1i1I11I11 :
   pass
  else :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + i1iii1I1I + '[/COLOR]' , url , 10013 , iIIII )
def Oo0O0o0Oo0Oo ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 10 - 10: IIiIiII11i . I1ii11iIi11i + I1ii11iIi11i / i1IiiiI1iI / Ii / i1IiiiI1iI
 if 89 - 89: i1iIi . oO0o * ii + OOooOOo / o0o00Oo0O
 if 60 - 60: Iii
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
 if 66 - 66: IIiIiII11i + IiI1i11I * i1i1I1IIii1II % Iii / ooOoO0O00 / iI11I1II1I1I
 if 62 - 62: OOooOOo + i1i1I1IIii1II * III1iiIii + o0o00Oo0O / oooOo0oo0oo + i1iIi
 if 38 - 38: ooOoO0O00 / iI11I1II1I1I + IiI1i11I
 for url , iIIII , I11iI1i1I11I11 in i1Iii1i1I :
  i1iii1I1I = I11iI1i1I11I11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I11iI1i1I11I11 :
   pass
  else :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + i1iii1I1I + '[/COLOR]' , url , 10013 , iIIII )
   if 26 - 26: Ii1I . o0ii1I % I11i
def i1IiI1iiIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for o0OO in IIi :
  oo0OooOoOo = ( o0OO ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  III1I11i1iIi ( 'http:' + oo0OooOoOo )
  if 8 - 8: III1iiIii
  if 37 - 37: oOo0O0Ooo / ii % Ii % Ii1I
  if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
  if 1 - 1: III1iiIii % ooOoO0O00
def IIiII1iII11Ii ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , url , 8046 , iIIII )
 for url in i1Iii1i1I :
  iIii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def oooO00o ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  III1I11i1iIi ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 59 - 59: IIiIiII11i . oooOo0oo0oo . I11i - i1IiiiI1iI
def I1Iiii1i1iI ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  yt . PlayVideo ( url )
  if 51 - 51: IiI1i11I / i1IiiiI1iI % i1i1I1IIii1II + i1i1I1IIii1II * i1i1I1IIii1II
def ooOO0oO0oo00o ( ) :
 iIii ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 iIii ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 iIii ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IIiIIiii ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iIIII )
 for url in next :
  iIii ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: ooOoO0O00 / oOo0O0Ooo / ii
  if 74 - 74: Ii1I % i1IiiiI1iI - oO0o * Iii . ii * oO0o
def OOOooooOo0 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   iIii ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o000o00OO00Oo ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , '' )
  if 12 - 12: Iii * i1i1I1IIii1II - i1IiiiI1iI * IiI1i11I - i1iIi * i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0Oo0OOOOoo ( name , url ) :
 oOi1IiIiIii11I = 0
 name = name
 url = url
 iiio00oOOooOOo0o = [ '144' , '240' , '380' , '480' , '720' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  ooOoO00 ( url )
  if 80 - 80: i1IiiiI1iI + Iii . i1IiiiI1iI + oooOo0oo0oo
  if 85 - 85: Ii . Iii + o0ii1I / o0ii1I
  if 43 - 43: III1iiIii . ii - IIiIiII11i
  if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * oooOo0oo0oo * i1i1I1IIii1II
  if 19 - 19: i1IiiiI1iI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
  if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
  if 15 - 15: o0ii1I + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
  if 54 - 54: III1iiIii - IIiIiII11i . i1iIi + o0ii1I
def IIiii1I ( ) :
 IIii11Ii1i1I = o0o0 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  if 'genre' in OOOiiiiI :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , OOOiiiiI , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0O000 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iIIII )
 for url in next :
  iIii ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 72 - 72: ooOoO0O00
def O0ooOo ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  o000o00OO00Oo ( url )
  if 34 - 34: ii . IIiIiII11i * iI11I1II1I1I / o0o00Oo0O . oOo0O0Ooo
def iiIIi ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1Ii1 = 'http://documentarylovers.com/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 ooOo0O0o0 = I1ii1Ii1 . lower ( )
 O0O000 ( ooOo0O0o0 )
 if 76 - 76: Iii * iI11I1II1I1I % IIiIiII11i
def OO000OOoo ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if 'films' in url :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def I11I1I1III1i1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IIii11Ii1i1I )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  if 'films' in url :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iIIII )
 for url in i1Iii1i1I :
  iIii ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def I1Ii1iI ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  if 'rtd' in url :
   iiI11i1II ( url )
   if 70 - 70: I1ii11iIi11i % o0o00Oo0O . oooOo0oo0oo
def iiI11i1II ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( IIii11Ii1i1I )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  ooOoO00 ( url )
  if 7 - 7: o0ii1I - ooOoO0O00 % oO0o / iI11I1II1I1I % I11i
  if 26 - 26: OOooOOo . Ii1I . oooOo0oo0oo
def iIiiII11 ( ) :
 II11iIiIIIiI = o0o0 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 , oOo000OOooO0O in IIi :
  iIii ( ( I11iI1i1I11I11 + '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '[/COLOR]' ) , OOOiiiiI , 8086 , iIIII )
  if 75 - 75: OOooOOo + o0ii1I . Ii / o0ii1I
def i1I1I1 ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 8087 , iIIII )
  if 31 - 31: o0ii1I / IiI1i11I
def iI1111iI1iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  o0ooo0 ( url , I11iI1i1I11I11 )
  if 80 - 80: oooOo0oo0oo * oO0o + o0ii1I
def o0ooo0 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OOOiiiiI , 3002 , 'http://www.solie.org/alibrary/' + iIIII )
def II1IoO0Ooo0o00o ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIIII )
def oOoOOO0oO0O ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 iiiI1I1I = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , I11iI1i1I11I11 in iiiI1I1I :
  iIii ( '[COLOR' + ooOoOoo0O + ']Season- ' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , iIIII , I11iI1i1I11I11 in i1Iii1i1I :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIIII )
def O0iIIii1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  I1IO00O0oO00o ( url )
def I1IO00O0oO00o ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  ooOoO00 ( url )
  if 30 - 30: OOooOOo % III1iiIii . I1ii11iIi11i - ii
def ii1ii111 ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOiiiiI , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def iIi1IIiiiI ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  O00Oooo00 ( url )
  if 4 - 4: ooOoO0O00 % I11i % i1i1I1IIii1II . ooOoO0O00
def o0O0Oo00 ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOiiiiI , 8065 , iiIi1IIiIi + 'classictv.png' )
def O0OO0OOo00Oo ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  if 'mp4' in url :
   ooOoO00 ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 26 - 26: IIiIiII11i * IiI1i11I + I11i / o0o00Oo0O + ooOoO0O00 - Iii
def o000oOoOOO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OOOiiiiI , 8071 , iiIi1IIiIi + 'streams.png' )
def OOOOOo00o0o ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iI1i1I11I11 , url in IIi :
  if '(Free Access)' in I11iI1i1I11I11 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def ooOoOoo ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iIIII , i11I , '' )
  if 73 - 73: I1ii11iIi11i % IIiIiII11i / IiI1i11I * i1i1I1IIii1II
def I1ii1i11i ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  oOo0 ( 'http://watchxxxfree.com/categories' )
 if O0O0ooOOO == 1 :
  OO00O0O ( 'http://www.perfectgirls.net' )
 if O0O0ooOOO == 2 :
  o0oo0oo0 ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 3 :
  IIi1IIOOOoooO0o0o ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 4 :
  o0oo0oo0 ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 5 :
  o0oo0oo0 ( 'http://www.xvideos.com/verified/videos' )
 if O0O0ooOOO == 6 :
  OOoOoOO00 ( 'http://www.xvideos.com/tags' )
 if O0O0ooOOO == 7 :
  o0O00 ( 'http://www.xvideos.com/porn' )
 if O0O0ooOOO == 8 :
  ii1IiI111II ( )
  if 8 - 8: oooOo0oo0oo
  if 44 - 44: oO0o % Ii . i1IiiiI1iI - o0o00Oo0O / IiI1i11I . i1iIi
  if 23 - 23: I11i % iI11I1II1I1I
  if 62 - 62: o0ii1I - I11i + o0ii1I . oO0o % IIiIiII11i - iI11I1II1I1I
  if 54 - 54: ii - o0ii1I - I11i - Ii1I
  if 53 - 53: I11i . i1i1I1IIii1II % o0o00Oo0O % Ii
  if 81 - 81: IiI1i11I + III1iiIii - Ii
  if 60 - 60: i1IiiiI1iI
  if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
def OooOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  if 'ch' in url :
   I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def o00ooO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiII1Iii1II = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for I11iI1i1I11I11 , url in IIiII1Iii1II :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def I1i1ii1IiI1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   oo0O00o0oO00 ( url )
def Iii1Iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def oOo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 , IiIIoOo in IIi :
  if 'category' in url :
   I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORorange]   ' + IiIIoOo + '[/COLOR]' , url , 90006 , iIIII , iiIi1IIiIi + 'Jizbox.png' , '' )
def o0ooO00o00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiII1Iii1II = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iIIII , '' , '' )
 for url in IIiII1Iii1II :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iI111II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   oo0O00o0oO00 ( url )
def oo0O00o0oO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooOoO00 ( url )
def OO00O0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , IiIIoOo in IIi :
  if 'category' in url :
   I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORorange]' + IiIIoOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def i11iI1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOo000O = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiII1Iii1II = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iIIII , '' , '' )
 for url in IIiII1Iii1II :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , oOo000O + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def oooo00o00oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIii11iI1Iii1iI ( 'http://www.perfectgirls.net' + url )
def iIii11iI1Iii1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  III1I11i1iIi ( 'http://' + url )
def o0O00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , IiIIoOo in IIi :
  I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgreen] - No of Videos : [COLORorange]' + IiIIoOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def OOoOoOO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIiII1Iii1II = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in IIiII1Iii1II :
  I1IIii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , IiIIoOo in IIi :
  I1IIii11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgreen] - No of Videos : [COLORorange]' + ( IiIIoOo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 47 - 47: III1iiIii - iI11I1II1I1I + i1iIi / o0ii1I
def I1IiI11i11iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIiII1Iii1II = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in IIiII1Iii1II :
  I1IIii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 , OO00oO0o0 in IIi :
  I1IIii11 ( I11iI1i1I11I11 + '--' + ( OO00oO0o0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iIIII ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 36 - 36: ooOoO0O00 - OOooOOo / i1iIi / o0ii1I
  if 73 - 73: III1iiIii - III1iiIii / ii
def o0oo0oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , url , I11iI1i1I11I11 , o0OoO0oo0O0o , oOoOo in IIi :
  I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgreen] - Porn Quality : [COLORorange]' + oOoOo + ' - [COLORred]' + o0OoO0oo0O0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iIIII , iIIII , oOoOo + ' - ' + o0OoO0oo0O0o )
 O00OO0oo00O0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in O00OO0oo00O0O :
  I1IIii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 14 - 14: oOo0O0Ooo
def IIi1IIOOOoooO0o0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iIII1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiII1Iii1II = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in IIiII1Iii1II :
  I1IIii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1iIII1 ) )
 for url , I11iI1i1I11I11 in IIi :
  if '/c/' in url :
   I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 45 - 45: o0o00Oo0O / i1i1I1IIii1II + I1ii11iIi11i
   if 37 - 37: ii / Ii1I % I11i
def ii1IiI111II ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1O0ooo00o0 = ( ii1iIIiii1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 ooOo0O0o0 = II1O0ooo00o0 . lower ( )
 o0o0ooOO0 = 'http://www.xvideos.com/?k=' + ooOo0O0o0
 print o0o0ooOO0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( o0o0ooOO0 )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , OOOiiiiI , I11iI1i1I11I11 , o0OoO0oo0O0o , oOoOo in IIi :
  I1IIii11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgreen] - Porn Quality : [COLORorange]' + oOoOo + ' - [COLORred]' + o0OoO0oo0O0o + '[/COLOR]' , 'http://www.xvideos.com' + OOOiiiiI , 10108 , iIIII , iIIII , oOoOo + ' - ' + o0OoO0oo0O0o )
 O00OO0oo00O0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in O00OO0oo00O0O :
  I1IIii11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OOOiiiiI , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 2 - 2: i1IiiiI1iI / oooOo0oo0oo
if 6 - 6: Ii / I1ii11iIi11i % IiI1i11I / oooOo0oo0oo * o0o00Oo0O
if 18 - 18: o0o00Oo0O
if 14 - 14: o0ii1I / III1iiIii - o0o00Oo0O
if 16 - 16: i1IiiiI1iI % iI11I1II1I1I . ooOoO0O00
if 72 - 72: i1iIi * oooOo0oo0oo
if 69 - 69: i1i1I1IIii1II - Ii
if 29 - 29: o0ii1I + IiI1i11I % Ii1I + Iii * I1ii11iIi11i - Ii
if 24 - 24: Ii . i1iIi + i1iIi - Ii % oooOo0oo0oo
if 58 - 58: oOo0O0Ooo
if 94 - 94: I11i + o0ii1I % I11i . i1IiiiI1iI - i1iIi * oOo0O0Ooo
if 62 - 62: I1ii11iIi11i * ooOoO0O00 % Ii1I + I1ii11iIi11i . o0o00Oo0O . i1iIi
if 57 - 57: I1ii11iIi11i - i1IiiiI1iI + o0o00Oo0O % I11i
if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
if 50 - 50: ii * ooOoO0O00 / i1i1I1IIii1II
if 83 - 83: ooOoO0O00
if 38 - 38: ii * iI11I1II1I1I
if 54 - 54: ii . i1IiiiI1iI
if 71 - 71: o0ii1I
if 31 - 31: Iii . Ii . oO0o * I1ii11iIi11i % o0ii1I . I11i
if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
if 93 - 93: i1iIi % i1IiiiI1iI
if 46 - 46: Ii1I * OOooOOo * III1iiIii * Ii1I . Ii1I
if 43 - 43: i1iIi . ooOoO0O00
if 68 - 68: III1iiIii % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
if 45 - 45: oOo0O0Ooo
if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
if 92 - 92: i1IiiiI1iI - oooOo0oo0oo % oO0o - I11i % ooOoO0O00
if 38 - 38: Ii1I . Iii / OOooOOo % Iii
if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
if 61 - 61: I1ii11iIi11i - i1IiiiI1iI
if 51 - 51: IiI1i11I * i1iIi / o0o00Oo0O / o0o00Oo0O
if 52 - 52: ii % o0o00Oo0O
if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
def iii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 OOoOooOoOOOoo = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in OOoOooOoOOOoo :
  if 'http' in url :
   oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 11 - 11: I1ii11iIi11i * ii - Ii
def Iii1ii1I1i1i1i1 ( url ) :
 O0ooOO = xbmc . Player ( IiiI ( ) )
 import urlresolver
 try : O0ooOO . play ( url )
 except : pass
 if 14 - 14: oOo0O0Ooo
 if 5 - 5: oooOo0oo0oo / IiI1i11I
def I1II ( ) :
 if 91 - 91: I11i
 if 14 - 14: Ii
 if 17 - 17: III1iiIii + Iii % I1ii11iIi11i + i1i1I1IIii1II
 if 87 - 87: Iii
 if 54 - 54: o0ii1I
 if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
 if 37 - 37: IiI1i11I + i1IiiiI1iI * o0ii1I + III1iiIii
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + o0ii1I / IIiIiII11i
 if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 if 23 - 23: i1i1I1IIii1II . OOooOOo + iI11I1II1I1I
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 8091 , iiIi1IIiIi + 'gofish.png' )
def iiiiiIi1II1i ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 8092 , iIIII )
 for url in next :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def II1II11I11ii ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1iii111 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII in II1iii111 :
  iIIII = iIIII
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 8092 , iIIII )
 for url in next :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 98 - 98: o0o00Oo0O + I11i
def i11iIIII1II11Iii ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 46 - 46: o0ii1I * o0ii1I / i1i1I1IIii1II * i1IiiiI1iI
  if 37 - 37: OOooOOo + III1iiIii
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + i1IiiiI1iI
  if 58 - 58: i1IiiiI1iI * o0o00Oo0O / o0ii1I + oOo0O0Ooo - Ii1I * I1ii11iIi11i
ooO0oO00oO0o = '{PQ},' ; OOo000ooo = '{SC},' ; oo0o00oO = '{XG},' ; o00ooOOo0ooO0 = '{JP},' ; I11i1I1 = '{HW},' ; iiI1iI111 = '{RT},'
def iII1111III1I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OOo0oOO0o0oo0 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 OOOiiiiI = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 oOo000O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 iII = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 ooO0o0O0Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IiiIIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O00o0O = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIIiI = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ii1iIIiii1
 O00 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1iiIII1IIiIIII = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 23 - 23: Ii1I + oOo0O0Ooo + ii
 OoO0o0000O = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 II1o0ooO0OOO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 47 - 47: i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( oOo000O )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 II1I11Iii1 = O00O0oOO00O00 ( oOo000O )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( iII )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( ooO0o0O0Oo )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 i1iIIi1II1iiI = O00O0oOO00O00 ( i1iiIII1IIiIIII )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 65 - 65: o0ii1I
 if 71 - 71: i1IiiiI1iI % i1IiiiI1iI . i1i1I1IIii1II + Ii - Ii
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / i1IiiiI1iI - Ii . i1iIi / oooOo0oo0oo
 if 13 - 13: I11i % o0o00Oo0O - i1IiiiI1iI * ii / I1ii11iIi11i - ii
 if 78 - 78: i1i1I1IIii1II % ii
 if 73 - 73: oOo0O0Ooo % i1iIi % III1iiIii + ooOoO0O00 - ii / i1i1I1IIii1II
 if 78 - 78: ii % i1i1I1IIii1II - Ii
 if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
 iiiiii1 = O00O0oOO00O00 ( II1o0ooO0OOO )
 if 23 - 23: i1iIi - o0o00Oo0O + Ii
 if i1iIIi1II1iiI != 'Failed' :
  Iio00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIi1II1iiI )
  for OOOiiiiI , I11iI1i1I11I11 in Iio00 :
   IiI1iiII1i1i = O00O0oOO00O00 ( OOOiiiiI )
   i1IiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1iiII1i1i )
   for o0o0O00 , oOo000OOooO0O in i1IiI :
    oOo000OOooO0O = ( oOo000OOooO0O . replace ( '.' , ' ' ) )
    if ooOo0O0o0 in oOo000OOooO0O . lower ( ) :
     if '.mkv' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 222 , '' , '' , '' )
     elif '.mp4' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 222 , '' , '' , '' )
     elif '.avi' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 222 , '' , '' , '' )
     elif '.wav' in o0o0O00 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 98 - 98: ii
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in i1Iii1i1I :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORred] source Technica[/COLOR]' ) , OOOiiiiI , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 61 - 61: I11i . III1iiIii . o0o00Oo0O + ii + o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: ooOoO0O00 * oooOo0oo0oo * ii - III1iiIii . IiI1i11I - oO0o
 if o00OooOO000 != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OOoooOoO0Oo , I11iI1i1I11I11 in OOoOooOoOOOoo :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iII + OOoooOoO0Oo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  oOIIiIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in oOIIiIi :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORred] source RaizTv[/COLOR]' ) , OOOiiiiI , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 71 - 71: o0ii1I * OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
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
    if 70 - 70: o0o00Oo0O . o0ii1I
    if 33 - 33: oooOo0oo0oo * o0ii1I
    if 64 - 64: Ii . iI11I1II1I1I
    if 7 - 7: OOooOOo % i1iIi + OOooOOo - OOooOOo * Ii % oO0o
    if 57 - 57: oooOo0oo0oo / oO0o + Ii1I
    if 60 - 60: o0o00Oo0O * I1ii11iIi11i % oooOo0oo0oo + III1iiIii . oO0o . I1ii11iIi11i
    if 70 - 70: Iii . Ii1I * i1i1I1IIii1II
    if 97 - 97: i1i1I1IIii1II . iI11I1II1I1I - oooOo0oo0oo
    if 23 - 23: Ii1I % Iii
    if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
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
    if 86 - 86: Ii1I - Ii1I / IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
    if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - III1iiIii
    if 30 - 30: ii % oooOo0oo0oo
 iI11i = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - oooOo0oo0oo
 for o0oo0O in iI11i :
  I1iiIII = oO0 + o0oo0O + oOoOooOo0o0
  i1iIIi1II1iiI = O00O0oOO00O00 ( I1iiIII )
  if i1iIIi1II1iiI != 'Failed' :
   Iio00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIi1II1iiI )
   for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in Iio00 :
    if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] - Source Pandoras[/COLOR]' , OOOiiiiI , 222 , Ii1IIiiIIi , OoooO0o , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 81 - 81: IiI1i11I % o0ii1I . i1iIi
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: Ii1I * o0ii1I / ii * o0o00Oo0O % oooOo0oo0oo
 iI11i = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * o0ii1I / i1IiiiI1iI * ii
 if 82 - 82: I1ii11iIi11i / o0ii1I / o0ii1I % o0ii1I
 for o0oo0O in iI11i :
  I1iiIII = OOo0oOO0o0oo0 + o0oo0O
  O0oOO0o = O00O0oOO00O00 ( I1iiIII )
  if O0oOO0o != 'Failed' :
   iiiiI1IiI1I1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0oOO0o )
   for OOoooOoO0Oo , I11iI1i1I11I11 in iiiiI1IiI1I1 :
    if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
     oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OOo0oOO0o0oo0 + o0oo0O + OOoooOoO0Oo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 20 - 20: i1iIi
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: iI11I1II1I1I . oO0o
def iiiI1I1iIIIi1 ( ) :
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 if 26 - 26: oooOo0oo0oo . oO0o % OOooOOo
 if 94 - 94: III1iiIii
 if 15 - 15: o0ii1I - III1iiIii / o0o00Oo0O
 if 28 - 28: i1IiiiI1iI . ooOoO0O00 / Ii1I
 if 77 - 77: Ii / i1IiiiI1iI / Ii % OOooOOo - i1IiiiI1iI
 if 80 - 80: i1IiiiI1iI % OOooOOo . ii . IIiIiII11i % III1iiIii
 if 6 - 6: i1IiiiI1iI % III1iiIii / o0ii1I + i1IiiiI1iI . i1i1I1IIii1II
 if 70 - 70: iI11I1II1I1I / o0ii1I
 if 61 - 61: o0o00Oo0O * I11i + i1IiiiI1iI - oooOo0oo0oo . oOo0O0Ooo - III1iiIii
 if 7 - 7: Ii1I
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / Iii
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
 if 13 - 13: Ii
 if 54 - 54: oooOo0oo0oo . Ii1I * Iii % i1IiiiI1iI . o0o00Oo0O * III1iiIii
 if 87 - 87: o0ii1I % Ii1I * I1ii11iIi11i
 if 59 - 59: I1ii11iIi11i / Iii - iI11I1II1I1I * iI11I1II1I1I
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 if 18 - 18: Iii * Ii1I / Ii / iI11I1II1I1I * ii . oooOo0oo0oo
 if 69 - 69: I1ii11iIi11i * i1iIi
 o0o0O00 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 oOo000O = 'http://onlinemovies.tube/?s=' + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 iII = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 ooO0o0O0Oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O00o0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
 O00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1iiIII1IIiIIII = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 38 - 38: i1i1I1IIii1II + ii * OOooOOo % i1i1I1IIii1II
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
 if 24 - 24: OOooOOo * o0ii1I
 OooIiIIII1i11I = O00O0oOO00O00 ( o0o0O00 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oOo000O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iII )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( ooO0o0O0Oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 O0oOO0o = O00O0oOO00O00 ( O00o0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
 if 81 - 81: oooOo0oo0oo
 II1I11Iii1 = O00O0oOO00O00 ( O00 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iIIi1II1iiI = O00O0oOO00O00 ( i1iiIII1IIiIIII )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 58 - 58: IIiIiII11i . i1IiiiI1iI . o0ii1I * ii / o0ii1I / Iii
 if 41 - 41: Iii + oO0o . IiI1i11I
 if i1iIIi1II1iiI != 'Failed' :
  Iio00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIi1II1iiI )
  for OOOiiiiI , I11iI1i1I11I11 in Iio00 :
   IiI1iiII1i1i = O00O0oOO00O00 ( OOOiiiiI )
   i1IiI = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1iiII1i1i )
   for o0o0O00 , oOo000OOooO0O in i1IiI :
    if ooOo0O0o0 in oOo000OOooO0O . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo000OOooO0O + '-[COLORgold] source ' + I11iI1i1I11I11 + '[/COLOR]' ) , OOOiiiiI + o0o0O00 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 73 - 73: Ii * oOo0O0Ooo + I11i / i1i1I1IIii1II
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if II1I11Iii1 != 'Failed' :
  III1II1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1I11Iii1 )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in III1II1i :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] source HeroVision[/COLOR]' ) , OOOiiiiI , 1016 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 56 - 56: ooOoO0O00
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
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
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  O00O = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for OOOiiiiI , iIIII , I11iI1i1I11I11 , II1oOo00o in i1Iii1i1I :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    if 'season' in II1oOo00o :
     iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90054 , iIIII , iIIII , '' )
    if 'episodes' in II1oOo00o :
     iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90044 , iIIII , iIIII , '' )
  for OOOiiiiI in O00O :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 87 - 87: III1iiIii
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OooIiIIII1i11I != 'Failed' :
  o0I11iII = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( OooIiIIII1i11I )
  for OOOiiiiI , I11iI1i1I11I11 , iIIII in o0I11iII :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( I11iI1i1I11I11 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , OOOiiiiI , 8022 , iIIII , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 45 - 45: i1i1I1IIii1II + IIiIiII11i * o0o00Oo0O % oooOo0oo0oo . iI11I1II1I1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: III1iiIii
    if 43 - 43: oooOo0oo0oo
    if 17 - 17: Ii
    if 94 - 94: ii - III1iiIii + i1i1I1IIii1II . ii / ooOoO0O00
    if 53 - 53: i1IiiiI1iI % Ii1I
    if 17 - 17: ii % o0ii1I % o0o00Oo0O
    if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
    if 89 - 89: III1iiIii - III1iiIii % IiI1i11I / Iii + i1i1I1IIii1II - III1iiIii
    if 97 - 97: o0ii1I % OOooOOo / Ii1I / iI11I1II1I1I * ii * oooOo0oo0oo
 if o00OooOO000 != 'Failed' :
  OOoOooOoOOOoo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for I11iI1i1I11I11 in OOoOooOoOOOoo :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iII + I11iI1i1I11I11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 80 - 80: i1i1I1IIii1II / o0o00Oo0O
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  oOIIiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for I11iI1i1I11I11 in oOIIiIi :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( ooO0o0O0Oo + I11iI1i1I11I11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 55 - 55: oOo0O0Ooo * Iii / o0o00Oo0O % OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if O0oOO0o != 'Failed' :
  iiiiI1IiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oOO0o )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in iiiiI1IiI1I1 :
   if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '-[COLORgold] Source Scooby[/COLOR]' ) , OOOiiiiI , 1016 , Ii1IIiiIIi , OoooO0o , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 71 - 71: Ii * OOooOOo * oooOo0oo0oo + i1i1I1IIii1II + I1ii11iIi11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: III1iiIii
 I1I1i1i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for o0oo0O in I1I1i1i :
  I1iiIII = oO0 + o0oo0O + oOoOooOo0o0
  iIIOOoO0oO00o = O00O0oOO00O00 ( I1iiIII )
  if iIIOOoO0oO00o != 'Failed' :
   oO00o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIOOoO0oO00o )
   for I11iI1i1I11I11 , o00O0O , OOOiiiiI , iIIII , i11I , IIiii in oO00o :
    if ooOo0O0o0 in I11iI1i1I11I11 . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] - Source Pandoras[/COLOR]' , OOOiiiiI , IIiii , iIIII , i11I , o00O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 54 - 54: oooOo0oo0oo
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 27 - 27: OOooOOo - oO0o + I11i + i1iIi . oO0o
     if 86 - 86: IIiIiII11i - ii - i1iIi % IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1IIi1 ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOiiiiI = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( ii1iIIiii1 ) . replace ( ' ' , '+' )
 if 58 - 58: oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( OOOiiiiI )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 21 - 21: III1iiIii - oOo0O0Ooo . oooOo0oo0oo - i1i1I1IIii1II
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , I11iI1i1I11I11 in i1Iii1i1I :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + OOOiiiiI ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 1 - 1: iI11I1II1I1I / Ii * IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
II1iII = '{ZH},' ; IIi1iIII = '{IX},' ; i111iIiI = '{LM},'
if 95 - 95: Ii1I + iI11I1II1I1I % I1ii11iIi11i
def Oo0oO ( url ) :
 Oo00o = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo00o )
 for url , i1I11iIiII , O0oO0o0OOOOOO , I11iI1i1I11I11 in IIi :
  iIii ( ( i1I11iIiII ) . replace ( 'Sezon' , ' Season ' ) + ( O0oO0o0OOOOOO ) . replace ( 'Bölüm' , ' Episode ' ) + I11iI1i1I11I11 , url , 8063 , '' )
  if 14 - 14: IIiIiII11i + o0o00Oo0O - IiI1i11I
  if 18 - 18: I11i / Ii % Ii1I * ii
  if 67 - 67: OOooOOo
  if 67 - 67: Ii1I / IiI1i11I + iI11I1II1I1I % oOo0O0Ooo
def o00o000 ( url ) :
 Oo00o = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Oo00o )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , url , 222 , '' )
  if 41 - 41: Ii1I * Ii - I1ii11iIi11i * IIiIiII11i
  if 56 - 56: oO0o / IiI1i11I - oO0o * I11i - OOooOOo
  if 73 - 73: iI11I1II1I1I
  if 48 - 48: Ii - o0ii1I . oO0o
def o0o0II ( ) :
 if 67 - 67: i1IiiiI1iI - I1ii11iIi11i % Ii / o0ii1I . i1IiiiI1iI . i1i1I1IIii1II
 Oo00o = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo00o )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 , O0oO0o0OOOOOO in IIi :
  iIii ( I11iI1i1I11I11 + '  -  ' + ( O0oO0o0OOOOOO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOiiiiI , 8063 , iIIII )
  if 44 - 44: oO0o / i1IiiiI1iI / ii
def oOOOiII1iII ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 , iIIII in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 8002 , iIIII )
def iiii11i1ii1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for iIIII , time , url , I11iI1i1I11I11 , OO0oOoo in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , time ) , url , 1015 , iIIII , OO0oOoo )
  if 90 - 90: Iii
def I1i1I1IIIi1II ( ) :
 if 25 - 25: oooOo0oo0oo / ii - Ii1I
 iIii ( 'Coronation Street' , '' , 8001 , '' )
 iIii ( 'Eastenders' , '' , 8002 , '' )
 iIii ( 'Emmerdale' , '' , 8003 , '' )
 iIii ( 'Hollyoaks' , '' , 8004 , '' )
 iIii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 31 - 31: Iii + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
 if 34 - 34: III1iiIii
 if 5 - 5: oO0o . oOo0O0Ooo
 if 48 - 48: I1ii11iIi11i - oO0o . Iii - iI11I1II1I1I % o0ii1I
def i1Iii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Holly' in I11iI1i1I11I11 :
   iIIII = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OOOiiiiI :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , iIIII )
   else :
    pass
    if 91 - 91: OOooOOo + I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 23 - 23: ooOoO0O00
def IiI11IiIIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'East' in I11iI1i1I11I11 :
   iIIII = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OOOiiiiI :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , iIIII )
   else :
    pass
    if 92 - 92: o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: IiI1i11I . oOo0O0Ooo + o0o00Oo0O
def iiI11 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Emmer' in I11iI1i1I11I11 :
   iIIII = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OOOiiiiI :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , iIIII )
   else :
    pass
    if 49 - 49: iI11I1II1I1I - iI11I1II1I1I - OOooOOo + III1iiIii / OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: ii + Ii1I % o0o00Oo0O
def iII1II ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Coro' in I11iI1i1I11I11 :
   iIIII = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OOOiiiiI :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , iIIII )
   else :
    pass
    if 98 - 98: Ii1I - oooOo0oo0oo % iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: Ii1I + ooOoO0O00 - Iii * ii
def OO0ooo ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Celeb' in I11iI1i1I11I11 :
   iIIII = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OOOiiiiI :
    oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , iIIII )
   else :
    pass
    if 94 - 94: o0ii1I / oooOo0oo0oo * Ii1I % Ii1I + III1iiIii
def O0OO0 ( name , url ) :
 OoII1111iII1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OoII1111iII1 :
  iio0000oO0OOOo0 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IIii11Ii1i1I = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( IIii11Ii1i1I ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IIii11Ii1i1I = open_url ( url )
  o00ooo0O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( IIii11Ii1i1I ) [ - 1 ]
  iio0000oO0OOOo0 = o00ooo0O . replace ( '\\/' , '/' )
 o0oooO = xbmcgui . ListItem ( name , '' , '' )
 o0oooO . setPath ( iio0000oO0OOOo0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0oooO )
 if 54 - 54: Ii1I * III1iiIii
 if 3 - 3: III1iiIii - Ii1I * IiI1i11I * Ii1I + I1ii11iIi11i
def IIi1i1iI11I11 ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OOOiiiiI , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for OOOiiiiI , I11iI1i1I11I11 in i1Iii1i1I :
  iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OOOiiiiI , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 67 - 67: Ii % Iii
def ii1I11iIi ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Movies' in I11iI1i1I11I11 :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( OOOiiiiI ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def IiO00oo0o0ooO ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIIII )
 for url in i1Iii1i1I :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 70 - 70: I1ii11iIi11i + i1IiiiI1iI + oooOo0oo0oo . Ii1I - Ii1I
  if 21 - 21: Iii - i1i1I1IIii1II
def O00oOo00o0o ( url ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url , iIIII in IIi :
  if '{{' in I11iI1i1I11I11 :
   pass
  else :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iIIII )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
O0OO0OoO00oOo = '{UJ},' ; IiIoOo = '{WE},' ; iII1Ii1iIIii = '{WP},' ; oooOoO00Oo00o0O = '{PP},'
def IiiIiI1IIII11II ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url , iIIII in IIi :
  if '{{' in I11iI1i1I11I11 :
   pass
  else :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIIII )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i111I ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  oO0ooo0o0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0ooo0o0 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: III1iiIii - OOooOOo . III1iiIii + i1iIi . IiI1i11I
 if 96 - 96: o0ii1I % IiI1i11I * o0ii1I % oOo0O0Ooo . I11i / I11i
 if 7 - 7: oO0o - i1iIi % ooOoO0O00
def iI1i1IIi1i1 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if '(cooltvseries.com)' in I11iI1i1I11I11 :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , I11iI1i1I11I11 in i1Iii1i1I :
  if '(cooltvseries.com)' in I11iI1i1I11I11 :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def Oooo ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  III1I11i1iIi ( ( url ) . replace ( ' ' , '%20' ) )
iIi11 = '{XX},' ; OOo0oo = '{UD},' ; OoOoO00OoOOo = '{YT},' ; oOOO0O000Oo = '{JS},' ; iiiii1I = '{PF},'
if 22 - 22: IiI1i11I . ii . I1ii11iIi11i
def IIiI ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 , iIIII in IIi :
  oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( OOOiiiiI ) ) , 222 , iIIII )
  if 70 - 70: ii * Ii
def iI1i1iI1iI ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  if 'youtu' in url :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iIIII )
 for url in next :
  iIii ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 60 - 60: III1iiIii / iI11I1II1I1I + ii - Ii1I * Ii
def Iii1iIIi1iIii ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 55 - 55: I11i . oooOo0oo0oo * OOooOOo
def ii11111ii11 ( url ) :
 IIii11Ii1i1I = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 222 , iIIII )
  if 48 - 48: IIiIiII11i
  if 25 - 25: i1iIi
  if 83 - 83: o0ii1I / ii * i1i1I1IIii1II . oOo0O0Ooo . ooOoO0O00
  if 59 - 59: Iii . Iii * oOo0O0Ooo - o0ii1I % OOooOOo
  if 19 - 19: ii / I1ii11iIi11i - i1IiiiI1iI . OOooOOo
def i1i1i11IIii ( ) :
 if 11 - 11: i1iIi . i1IiiiI1iI - IiI1i11I . I11i
 iIii ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIii ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 41 - 41: i1i1I1IIii1II / oO0o - oO0o + i1iIi * oooOo0oo0oo
 if 13 - 13: i1IiiiI1iI * IIiIiII11i - OOooOOo
def II11iii ( Cat_Name ) :
 if 85 - 85: oO0o
 i1111iI1ii = False
 iIi1iii1 = '0'
 if Cat_Name == 'All Channels' : i1111iI1ii = True
 if Cat_Name == 'Entertainment' : iIi1iii1 = '1'
 if Cat_Name == 'Movies' : iIi1iii1 = '2'
 if Cat_Name == 'Music' : iIi1iii1 = '3'
 if Cat_Name == 'News' : iIi1iii1 = '4'
 if Cat_Name == 'Sports' : iIi1iii1 = '5'
 if Cat_Name == 'Documentary' : iIi1iii1 = '6'
 if Cat_Name == 'Kids' : iIi1iii1 = '7'
 if Cat_Name == 'Food' : iIi1iii1 = '8'
 if Cat_Name == 'Religious' : iIi1iii1 = '9'
 if Cat_Name == 'USA Channels' : iIi1iii1 = '10'
 if Cat_Name == 'Other' : iIi1iii1 = '11'
 if 42 - 42: Iii / Ii
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for I11iI1i1I11I11 , iIIII , iI1ii1iiii in IIi :
  Ii1IiI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIIII ) . replace ( '\\' , '' )
  if iI1ii1iiii == iIi1iii1 :
   iIii ( I11iI1i1I11I11 , '' , 7022 , Ii1IiI )
  elif i1111iI1ii == True :
   iIii ( I11iI1i1I11I11 , '' , 7022 , Ii1IiI )
  else : pass
  if 58 - 58: iI11I1II1I1I * o0ii1I . i1iIi . I1ii11iIi11i * o0ii1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: OOooOOo . Iii * I11i - Iii % Iii
def o0o0000O ( Search_Name ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for iIIII , OOOiiiiI , oOo000O , iII in IIi :
  Ii1IiI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIIII ) . replace ( '\\' , '' )
  oOo0OoOOo0 ( Search_Name + ': Link 1' , ( OOOiiiiI ) . replace ( '\\' , '' ) , 222 , Ii1IiI )
  oOo0OoOOo0 ( Search_Name + ': Link 2' , ( oOo000O ) . replace ( '\\' , '' ) , 222 , Ii1IiI )
  oOo0OoOOo0 ( Search_Name + ': Link 3' , ( iII ) . replace ( '\\' , '' ) , 222 , Ii1IiI )
  if 49 - 49: o0o00Oo0O / i1IiiiI1iI
def O0ooo00o ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def IIIIi ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def Oo0oo0oOooOoo ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , OOOiiiiI in IIi :
  oOo0OoOOo0 ( I11iI1i1I11I11 , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 95 - 95: Ii1I / III1iiIii % iI11I1II1I1I + o0o00Oo0O
def i111IiI1III1 ( url ) :
 url
 OOOOoO00o0O = xbmcgui . ListItem ( I11iI1i1I11I11 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoO00o0O )
 return
 if 97 - 97: III1iiIii
 if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . i1IiiiI1iI
def o0o0o ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IIii11Ii1i1I )
 for url , o00O0O , iIIII , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iIIII , '' , ( o00O0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  iIii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 30 - 30: o0o00Oo0O
def OoO00O00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o00O0O , iIIII in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iIIII , '' , o00O0O )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 IiOo0ooooO0o00 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1iiIiiIi in IiOo0ooooO0o00 :
  oo00O0oO0O0 = ( i1iiIiiIi ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iIIII , '' , oo00O0oO0O0 )
  if 9 - 9: OOooOOo - Iii . ii % i1iIi
def IIIiIiIIII1i1 ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 90 - 90: oOo0O0Ooo % i1iIi % ii / oO0o . III1iiIii * IIiIiII11i
 if 83 - 83: i1i1I1IIii1II
 if 34 - 34: OOooOOo
def O0OoIIIi111 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( ( I11iI1i1I11I11 ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def iI1I11II1Iii1 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , url , 9032 , iiIi1IIiIi + 'icon.png' )
def O00O0oO ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  if '=' in I11iI1i1I11I11 :
   pass
  else :
   oOo0OoOOo0 ( ( I11iI1i1I11I11 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def IIIIi1iII ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  if '=' in I11iI1i1I11I11 :
   pass
  else :
   oOo0OoOOo0 ( I11iI1i1I11I11 , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 49 - 49: ooOoO0O00 . III1iiIii
   if 82 - 82: oO0o / Iii
   if 38 - 38: iI11I1II1I1I
def Ii1IIIi ( url ) :
 I11I ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , iIIII , url in IIi :
  if 'music' in url :
   I11I ( I11iI1i1I11I11 , url , 90036 , iIIII , iIIII , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   I11I ( I11iI1i1I11I11 , url , 90039 , iIIII , iIIII , '' , '' )
def Oo00ooOOO ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url , iIIII in IIi :
  OOOOooO0oO00O0o ( I11iI1i1I11I11 , url , 100009 , iIIII , iIIII , '' , '' )
  if 1 - 1: ooOoO0O00 / o0ii1I % III1iiIii - Iii % I11i
def I1I1i111 ( url ) :
 I11I ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I11I ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 IIii11Ii1i1I = requests . get ( url ) . text
 iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 I1iIII1 = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  o0Ooo0o0ooo0 = requests . get ( url ) . text
  iiIi1i1iIi1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0Ooo0o0ooo0 )
  for o0O00oOoo in iiIi1i1iIi1I :
   Ii11I1i = requests . get ( o0O00oOoo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii11I1i )
   for oOOoooo , ooOOo0O0o00o00 , i1iII1IiiIiI1 , i1ooOO00o0 , iiI111I1iIiI in IIi :
    if oOOoooo == 'xyz' :
     II1Oo = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( I11iI1i1I11I11 , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
    else :
     II1Oo = 'http://' + i1ooOO00o0 + '.' + i1iII1IiiIiI1 + '.' + ooOOo0O0o00o00 + '.' + oOOoooo + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( I11iI1i1I11I11 , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
 for o0OO0o0oOOO0O in iI :
  I11I ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1000111 , '' , '' , '' , '' )
  if 28 - 28: i1IiiiI1iI / iI11I1II1I1I + oooOo0oo0oo . Ii1I % oooOo0oo0oo + oO0o
  if 79 - 79: i1i1I1IIii1II
  if 39 - 39: i1IiiiI1iI % i1i1I1IIii1II % o0o00Oo0O % o0o00Oo0O - IiI1i11I - i1i1I1IIii1II
def ooooOo ( ) :
 I11I ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 54 - 54: i1IiiiI1iI . oooOo0oo0oo - I11i * iI11I1II1I1I . OOooOOo
 if 77 - 77: i1IiiiI1iI + Ii . iI11I1II1I1I % i1iIi - ii
def OO0oOooOoOO0 ( url , name ) :
 I11I ( name , '' , '' , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 IIii11Ii1i1I = requests . get ( url ) . text
 iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 I1iIII1 = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 for url , iIIII , name in IIi :
  o0Ooo0o0ooo0 = requests . get ( url ) . text
  iiIi1i1iIi1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0Ooo0o0ooo0 )
  for o0O00oOoo in iiIi1i1iIi1I :
   Ii11I1i = requests . get ( o0O00oOoo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii11I1i )
   for oOOoooo , ooOOo0O0o00o00 , i1iII1IiiIiI1 , i1ooOO00o0 , iiI111I1iIiI in IIi :
    if oOOoooo == 'xyz' :
     II1Oo = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( name , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
    else :
     II1Oo = 'http://' + i1ooOO00o0 + '.' + i1iII1IiiIiI1 + '.' + ooOOo0O0o00o00 + '.' + oOOoooo + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( name , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
     if 90 - 90: o0ii1I
 for o0OO0o0oOOO0O in iI :
  I11I ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1003111 , '' , '' , '' , '' )
  if 55 - 55: I1ii11iIi11i % III1iiIii + Ii - oooOo0oo0oo - IIiIiII11i
  if 80 - 80: III1iiIii
def oOo0O0O0oOo ( ) :
 I11I ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 81 - 81: oO0o + ooOoO0O00 % i1IiiiI1iI * Iii + III1iiIii
 if 15 - 15: IiI1i11I % III1iiIii
 if 83 - 83: i1IiiiI1iI . I1ii11iIi11i / i1iIi
def O0o000O0Oo0 ( url , name ) :
 I11I ( name , '' , '' , '' , '' , '' , '' )
 I11I ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 IIii11Ii1i1I = requests . get ( url ) . text
 iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 I1iIII1 = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
 for url , iIIII , name in IIi :
  o0Ooo0o0ooo0 = requests . get ( url ) . text
  iiIi1i1iIi1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0Ooo0o0ooo0 )
  for o0O00oOoo in iiIi1i1iIi1I :
   Ii11I1i = requests . get ( o0O00oOoo ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii11I1i )
   for oOOoooo , ooOOo0O0o00o00 , i1iII1IiiIiI1 , i1ooOO00o0 , iiI111I1iIiI in IIi :
    if oOOoooo == 'xyz' :
     II1Oo = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( name , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
    else :
     II1Oo = 'http://' + i1ooOO00o0 + '.' + i1iII1IiiIiI1 + '.' + ooOOo0O0o00o00 + '.' + oOOoooo + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     OOOOooO0oO00O0o ( name , II1Oo , 1001111 , iIIII , iIIII , '' , '' )
     if 51 - 51: i1IiiiI1iI . Iii
 for o0OO0o0oOOO0O in iI :
  I11I ( '[COLORblue][B]NEXT[/B][/COLOR]' , o0OO0o0oOOO0O , 1005111 , '' , '' , '' , '' )
def I111IIiii1Ii ( name , url ) :
 import urlresolver
 try :
  II1 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( II1 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 61 - 61: oOo0O0Ooo % iI11I1II1I1I / o0o00Oo0O + I1ii11iIi11i + IiI1i11I
 if 56 - 56: Iii / oooOo0oo0oo / i1IiiiI1iI
 if 87 - 87: o0o00Oo0O - oOo0O0Ooo
def OOo0O ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'Daily' in I11iI1i1I11I11 :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 9008 , O0O )
def O0ooO00 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def IIII1 ( url ) :
 oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 oOo0OoOOo0 ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  oOo0OoOOo0 ( ( I11iI1i1I11I11 ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 50 - 50: I1ii11iIi11i
def I11IiIi1I ( ) :
 IIii11Ii1i1I = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if '.m3u' in OOOiiiiI :
   iIii ( ( I11iI1i1I11I11 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + OOOiiiiI ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def OOOoOOoo0OO ( url ) :
 IIii11Ii1i1I = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  oOo0OoOOo0 ( ( I11iI1i1I11I11 ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 81 - 81: i1iIi + OOooOOo % ooOoO0O00 % oOo0O0Ooo + ooOoO0O00
def oOOo0oo0O ( ) :
 IIii11Ii1i1I = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  if 'category' in OOOiiiiI :
   iIii ( I11iI1i1I11I11 , 'http://www.disclose.tv/' + OOOiiiiI , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 2 - 2: IiI1i11I + IiI1i11I
   if 51 - 51: ii + Ii
def oOO00oOooOo ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 , iIIII in IIi :
  iIii ( I11iI1i1I11I11 , 'http://www.disclose.tv/' + url , 7011 , iIIII )
 for url in next :
  iIii ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 2 - 2: ooOoO0O00 + o0o00Oo0O + ooOoO0O00 * oOo0O0Ooo
  if 73 - 73: oO0o + i1i1I1IIii1II . I11i / IiI1i11I % oO0o - oooOo0oo0oo
def iII1i111iIiI1 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IIii11Ii1i1I )
 OOoOooOoOOOoo = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  if 'http' in url :
   oOo0OoOOo0 ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , I11iI1i1I11I11 in i1Iii1i1I :
  oOo0OoOOo0 ( I11iI1i1I11I11 , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in OOoOooOoOOOoo :
  oOo0OoOOo0 ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 78 - 78: Iii - oOo0O0Ooo * III1iiIii
  if 43 - 43: ii . oooOo0oo0oo
def iI1IIiIi1i ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 84 - 84: ii . oO0o / OOooOOo * ooOoO0O00
def iii111III1ii1 ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 Ii1IIi = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIi1iii = len ( Ii1IIi )
 if 42 - 42: I11i - i1iIi . oooOo0oo0oo / IiI1i11I / I11i . III1iiIii
 if 46 - 46: i1IiiiI1iI % o0o00Oo0O % oO0o * III1iiIii % i1IiiiI1iI % IIiIiII11i
 if iIi1iii == 1 :
  for ii1Iii1iiI11 in Ii1IIi :
   ii1Iii1iiI11 = ii1Iii1iiI11 . replace ( 'player' , 'watch' )
   i11ii1II = ii1Iii1iiI11 + '&fv=&sou='
   ooOo00OOo0 = OooOoooOo ( i11ii1II )
   ii1IIi = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( ooOo00OOo0 )
   for II1i111 in ii1IIi :
    iii1Ii = False
    Resolve ( II1i111 )
    if 98 - 98: Iii / Ii - I11i % I11i
 elif iIi1iii > 1 :
  if 31 - 31: Iii
  for ii1Iii1iiI11 in Ii1IIi :
   Oooo0o00Oo00 = OooOoooOo ( ii1Iii1iiI11 )
   OoooOoo0Oooo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oooo0o00Oo00 )
   i1O0o0oO = OoooOoo0Oooo
   i1O0o0oO = ( str ( i1O0o0oO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i1O0o0oO
   oOo0OoOOo0 ( 'DOUBLE LINK' , i1O0o0oO , 424 , '' )
   if 33 - 33: ooOoO0O00 * I11i + Ii1I - ooOoO0O00 % ii
   for url in OoooOoo0Oooo :
    iIii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oOo000O = Google . resolve ( url )
    except :
     pass
    try :
     o0OiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oOo000O ) )
     for IIi111i1 , II1II1iiIiI in o0OiI :
      if 31 - 31: i1IiiiI1iI . Ii1I + III1iiIii
      HD_URLS . append ( IIi111i1 )
      SD_URLS . append ( II1II1iiIiI )
    except :
     pass
 else :
  pass
  if 65 - 65: oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . o0o00Oo0O
def iI11 ( ) :
 if 28 - 28: I11i % i1IiiiI1iI
 if 26 - 26: i1IiiiI1iI
 iIii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 71 - 71: oO0o + Ii % ii - I11i % III1iiIii / IIiIiII11i
 iIii ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 20 - 20: oooOo0oo0oo . I1ii11iIi11i * IIiIiII11i / iI11I1II1I1I % Ii1I
 if 11 - 11: I11i * oO0o
def oO0IiiI1i1i11I1 ( ) :
 IIii11Ii1i1I = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , 'http://cnfstudio.com/genre/' + OOOiiiiI , 7003 , iiIi1IIiIi + 'icon.png' )
  if 97 - 97: OOooOOo - oO0o
iIii1 = xbmcgui . Dialog ( )
if 64 - 64: ooOoO0O00 / ii / Ii1I - I1ii11iIi11i + i1i1I1IIii1II
iI1i1II11I = '{UN},' ; OoO0o0oOOoOoo = '{IG},' ; I1iIiiiI1II1 = '{PL},' ; o0OOo00Oo00 = '{LO},' ; iII1I = '{LP},' ; oOoOo0O00Oo = '{HA},' ; Iiii1iiIi = '{XD},' ; oOoOO = '{TA},' ; i1iIiII111i11 = '{DP},' ; i1iIiiii = '{JT},' ; O0o0oOo0OooO = '{JJ},' ; iI1IiI1 = '{MM},' ; o0o0ooo = '{FQ},' ; oOooO = '{HH},'
if 52 - 52: IiI1i11I * i1i1I1IIii1II + ii
def iiii1iIiI11I ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1i11Ii1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IIii11Ii1i1I )
 for iIIII , url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iIIII )
 i1i11Ii1 = i1i11Ii1
 for url in i1i11Ii1 :
  iIii ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 14 - 14: oooOo0oo0oo . I11i / IIiIiII11i % oooOo0oo0oo
def oOO0O0 ( url ) :
 if 18 - 18: oOo0O0Ooo / Ii - o0ii1I
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  ooOo0O0o = IiIIIIII ( iiI111I1iIiI )
  OOO0O = IiIIIIII ( url )
  if 24 - 24: i1iIi % oooOo0oo0oo . o0o00Oo0O * I1ii11iIi11i
  if 52 - 52: o0o00Oo0O . i1IiiiI1iI + IiI1i11I / Ii
def IiIIIIII ( url ) :
 if 52 - 52: i1i1I1IIii1II % I1ii11iIi11i * IIiIiII11i
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  O00Oooo00 ( url )
  if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
  if 27 - 27: ooOoO0O00 - i1i1I1IIii1II + oooOo0oo0oo
def i1i1iiI11I ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 78 - 78: OOooOOo % oO0o - o0ii1I / oooOo0oo0oo
def ooOo000 ( ) :
 if os . path . exists ( II ) :
  OO0o0oo = open ( II , 'r' )
  for OOOOoO00o0O in OO0o0oo :
   o00I11II1iI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOOOoO00o0O )
   for I11iI1i1I11I11 , OOOiiiiI in o00I11II1iI :
    oOo0OoOOo0 ( I11iI1i1I11I11 , OOOiiiiI , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 19 - 19: o0o00Oo0O
def O0oo0O0OO0OOo ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = o0o0 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for I11iI1i1I11I11 , url in IIi :
   url = ( url ) . strip ( )
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 12 - 12: Iii
  if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in IIi :
  OOOiiiiI = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OOOiiiiI
 I11iI1i1I11I11 = 'plugin.video.GenieTv'
 if 41 - 41: Iii . Ii1I
 Oo00o0Ooo0OOo ( OOOiiiiI , I11iI1i1I11I11 )
 if 39 - 39: IiI1i11I - oO0o
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in IIi :
  OOOiiiiI = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OOOiiiiI
 I11iI1i1I11I11 = 'repository.GenieTv'
 if 1 - 1: ii - i1iIi
 Oo00o0Ooo0OOo ( OOOiiiiI , I11iI1i1I11I11 )
 if 24 - 24: IIiIiII11i % IiI1i11I % o0ii1I % IiI1i11I % Iii . iI11I1II1I1I
 if 48 - 48: i1i1I1IIii1II . IIiIiII11i * iI11I1II1I1I / I11i * o0ii1I * i1IiiiI1iI
def I11I1 ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  o0oO ( )
 if O0O0ooOOO == 1 :
  I1II11iiii ( )
  if 95 - 95: o0ii1I - IiI1i11I % i1IiiiI1iI / oooOo0oo0oo
  if 2 - 2: I11i
  if 58 - 58: i1i1I1IIii1II - IIiIiII11i + o0o00Oo0O
  if 54 - 54: iI11I1II1I1I - III1iiIii - III1iiIii
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
iiiiiII1I11ii1III = 'https://addons.tvaddons.ag/'
if 34 - 34: OOooOOo % ii . IIiIiII11i % oooOo0oo0oo
def I1II11iiii ( ) :
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 o0o0ooOO0 = 'https://addons.tvaddons.ag/search/?keyword=' + ooOo0O0o0
 II11iIiIIIiI = OooOoooOo ( o0o0ooOO0 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I1i1i , I11iI1i1I11I11 in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , OOOiiiiI , 10054 , 'https://addons.tvaddons.ag/' + I1i1i , Oo00OOOOO , '' )
  if 66 - 66: I1ii11iIi11i - oO0o
  if 2 - 2: i1IiiiI1iI
def o0oO ( ) :
 II11iIiIIIiI = OooOoooOo ( iiiiiII1I11ii1III )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  if 'Repositories' in I11iI1i1I11I11 :
   pass
  elif 'Services' in I11iI1i1I11I11 :
   pass
  elif 'International' in I11iI1i1I11I11 :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , OOOiiiiI , 10053 , 'https://addons.tvaddons.ag/' + iIIII , Oo00OOOOO , '' )
   if 96 - 96: ii / Ii1I * oO0o
   if 82 - 82: I1ii11iIi11i / Ii % IIiIiII11i * iI11I1II1I1I + o0ii1I
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iI = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  if 'Please' in I11iI1i1I11I11 :
   pass
  else :
   Ii1I1i ( I11iI1i1I11I11 , url , 10054 , 'https://addons.tvaddons.ag/' + iIIII , Oo00OOOOO , '' )
 for url in iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 69 - 69: I1ii11iIi11i
  if 70 - 70: o0o00Oo0O - oO0o - I1ii11iIi11i
def O00o0OoO0OOOo ( url , name ) :
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
   if 72 - 72: i1iIi * Ii / oO0o
def Oo00o0Ooo0OOo ( url , name ) :
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
 if 47 - 47: oO0o * iI11I1II1I1I - Ii1I - i1IiiiI1iI + III1iiIii
def OoOO0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 91 - 91: o0o00Oo0O
 if 26 - 26: ii + i1i1I1IIii1II + oO0o . o0o00Oo0O
def Ii1I111Ii ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , I1i1i , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , url , 1007 , I1i1i )
def OOo000OO0Oo0O ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , I1i1i , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 1006 , I1i1i )
  if 31 - 31: Ii - i1IiiiI1iI
def OooOo0o0Oo0 ( ) :
 IIii11Ii1i1I = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , Ii1IIiiIIi , o00O0O , i11I , I11iI1i1I11I11 in IIi :
  i11iI1i11I111 ( I11iI1i1I11I11 , 100109 , OOOiiiiI , image = Ii1IIiiIIi , isFolder = True )
  if 57 - 57: ooOoO0O00 . IiI1i11I
def iIiIII1Ii ( url ) :
 import random
 O0oOo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 O0oOo . clear ( )
 iIII1Ii1 = [ ]
 I1111i1I = [ ]
 i1iii1I1I = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo000O , Ii1IIiiIIi , o00O0O , i11I , I11iI1i1I11I11 in IIi :
  iIII1Ii1 . append ( [ oOo000O , I11iI1i1I11I11 ] )
  if len ( iIII1Ii1 ) == len ( IIi ) :
   for OOOOoO00o0O in iIII1Ii1 :
    OOoooOO0o = random . randint ( 1 , len ( iIII1Ii1 ) )
    try :
     O00oo0Ooo = iIII1Ii1 [ int ( OOoooOO0o ) ]
    except :
     pass
    if len ( I1111i1I ) <= 20 :
     if O00oo0Ooo [ 1 ] not in i1iii1I1I :
      o0o = OooOoooOo ( O00oo0Ooo [ 0 ] )
      OOoOooOoOOOoo = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for iIiIiIi1Iii , OoOO0OooOoooo in OOoOooOoOOOoo :
       OOoOoo = OooOoooOo ( iIiIiIi1Iii )
       oOIIiIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for IIIii , iiI111I1iIiI in oOIIiIi :
        if 'panda' in iiI111I1iIiI :
         OoOoo00O = OooOoooOo ( iiI111I1iIiI )
         IiiIiI = re . compile ( "url: '(.+?)'" ) . findall ( OoOoo00O )
         for iIii1111Ii1I1 in IiiIiI :
          if 'http' in iIii1111Ii1I1 :
           o0oooO = xbmcgui . ListItem ( O00oo0Ooo [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : O00oo0Ooo [ 1 ] } )
           o0oooO . setProperty ( "IsPlayable" , "true" )
           O0oOo . add ( iIii1111Ii1I1 , o0oooO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0oooO )
           if 63 - 63: III1iiIii % o0o00Oo0O * i1iIi % I11i . IIiIiII11i + I1ii11iIi11i
def i11iI1i11I111 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 Ooo0O0 = sys . argv [ 0 ]
 Ooo0O0 += '?mode=' + str ( mode )
 Ooo0O0 += '&title=' + urllib . quote_plus ( name )
 Ooo0O0 += '&image=' + urllib . quote_plus ( image )
 Ooo0O0 += '&page=' + str ( page )
 if url != '' :
  Ooo0O0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  Ooo0O0 += '&keyword=' + urllib . quote_plus ( keyword )
 o0oooO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  o0oooO . addContextMenuItems ( contextMenu )
 if infoLabels :
  o0oooO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  o0oooO . setProperty ( "IsPlayable" , "true" )
 o0oooO . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = isFolder )
 if 98 - 98: IiI1i11I
 if 56 - 56: oOo0O0Ooo . Iii % IiI1i11I
def o00o ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , iconimage , o00O0O , i11I , name in IIi :
  if 'http' in url :
   if '.php' in url :
    iIi1I1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for OOOOoO00o0O in iIi1I1 :
     if OOOOoO00o0O == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoOooo ( name , url , 1016 , iconimage , i11I , o00O0O )
   else :
    if 'youtube' in url :
     iIi1I1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for OOOOoO00o0O in iIi1I1 :
      if OOOOoO00o0O == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11i11 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , i11I , o00O0O )
    else :
     iIi1I1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for OOOOoO00o0O in iIi1I1 :
      if OOOOoO00o0O == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11i11 ( name , url , 222 , iconimage , i11I , o00O0O )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  else :
   I1I1i ( url , iconimage , name )
   if 67 - 67: OOooOOo . o0o00Oo0O + ooOoO0O00 . Ii % III1iiIii / iI11I1II1I1I
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
  for url , I1i1i , name in IIi :
   if 'http' in url :
    if '.php' in url :
     iIii ( name , url , 1016 , I1i1i )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOo0OoOOo0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1i1i )
     else :
      iIi1I1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for OOOOoO00o0O in iIi1I1 :
       if OOOOoO00o0O == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOo0OoOOo0 ( name , url , 222 , I1i1i )
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   else :
    I1I1i ( url , I1i1i , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 28 - 28: o0ii1I
def I1I1i ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Oo0ooO00 = ( url ) . replace ( IIi1iIII , 'http' ) . replace ( OOo0oo , '.com' ) ;
 o0OO0O0o = ( Oo0ooO00 ) . replace ( i111iIiI , 'a' ) . replace ( oo0o00oO , 'b' ) . replace ( o00ooOOo0ooO0 , 'c' ) . replace ( IiIoOo , 'd' ) . replace ( I1iIiiiI1II1 , 'e' ) . replace ( i1iIiiii , 'f' ) ;
 IiII11iii = ( o0OO0O0o ) . replace ( iIi11 , 'g' ) . replace ( oOoOo0O00Oo , 'h' ) . replace ( OoOoO00OoOOo , 'i' ) . replace ( iiiii1I , 'j' ) . replace ( I11i1I1 , 'k' ) . replace ( iiI1iI111 , 'l' ) ;
 oooOOo0Oo0OO0O = ( IiII11iii ) . replace ( I1iO00oo0oOo , 'm' ) . replace ( iiiIii , 'n' ) . replace ( oO00oIiIi1i1 , 'o' ) . replace ( o0000o0o , 'p' ) . replace ( O0OO000o , 'q' ) . replace ( iI1I1iI1ii , 'r' ) ;
 IiIIi1I = ( oooOOo0Oo0OO0O ) . replace ( iii11iI , 's' ) . replace ( iII1Ii1iIIii , 't' ) . replace ( ii1II1i1 , 'u' ) . replace ( oOOOOOOooO , 'v' ) . replace ( i1iI1Iii11Iii11 , 'w' ) . replace ( iIiiI , 'x' ) ;
 OOo000 = ( IiIIi1I ) . replace ( iI1iIIiIi1I1 , 'y' ) . replace ( oOo0oO0 , 'z' ) . replace ( iI1i1II11I , '.' ) . replace ( OoO0o0oOOoOoo , '(' ) . replace ( o0OOo00Oo00 , ')' ) . replace ( iII1I , '/' ) ;
 iiIiIiiI1Ii = ( OOo000 ) . replace ( II1iII , '1' ) . replace ( oooOoO00Oo00o0O , '2' ) . replace ( iIIiiii , '3' ) . replace ( oOoOO , '4' ) . replace ( i1iIiII111i11 , '5' ) . replace ( oOOO0O000Oo , '6' ) ;
 ii111Ii = ( iiIiIiiI1Ii ) . replace ( O0o0oOo0OooO , '7' ) . replace ( iI1IiI1 , '8' ) . replace ( o0o0ooo , '9' ) . replace ( oOooO , '0' ) . replace ( ooO0oO00oO0o , ':' ) . replace ( OOo000ooo , '%' ) ;
 url = ( ii111Ii ) . replace ( O0OO0OoO00oOo , '-' ) . replace ( Iiii1iiIi , '_' ) ;
 oOo0OoOOo0 ( name , url , 222 , iconimage ) ;
 if 82 - 82: OOooOOo * Iii . i1IiiiI1iI . i1i1I1IIii1II . I11i
 if 58 - 58: i1IiiiI1iI * oO0o * ooOoO0O00
def IiiIi1II ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I1i1i , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 1007 , I1i1i )
def IiII1IiiI ( url ) :
 if 57 - 57: i1i1I1IIii1II
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , I1i1i , I11iI1i1I11I11 in IIi :
  iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 1006 , I1i1i )
  if 44 - 44: IiI1i11I / oooOo0oo0oo
def ooO0oo00o00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 II11IiiIII = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 II11IiiIII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , II11IiiIII )
 if 94 - 94: i1i1I1IIii1II + ii - OOooOOo . i1IiiiI1iI / Iii . III1iiIii
 if 66 - 66: ooOoO0O00
def OOOOoOoO ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii11Ii1i1I )
 for url , iIIII , I11iI1i1I11I11 in IIi :
  if '-dir-' in I11iI1i1I11I11 :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iIIII )
  else :
   iIii ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' , url , 1006 , iIIII )
   if 19 - 19: i1iIi / i1i1I1IIii1II . o0ii1I / I11i
def iIII1 ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 Iii11 = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if '[To Parent Directory]' in I11iI1i1I11I11 :
   I11iI1i1I11I11 = 'HOME'
   pass
  elif 'HOME' in I11iI1i1I11I11 :
   pass
  elif '.m3u' in I11iI1i1I11I11 :
   iIii ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , Iii11 + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in I11iI1i1I11I11 :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Iii11 + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in I11iI1i1I11I11 :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Iii11 + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) , Iii11 + url , 1012 , iiIi1IIiIi + 'music.png' )
def iII1Ii1ii111 ( url ) :
 II11iIiIIIiI = o0o0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIII , I11iI1i1I11I11 , url in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 22 - 22: o0ii1I
def I1IIi1I11iI ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 Iii11 = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  if '.mp3' in I11iI1i1I11I11 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '/' , '' ) , Iii11 + url , 1011 , iiIi1IIiIi + 'music.png' )
def O0II ( ) :
 IIii11Ii1i1I = o0o0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , iIIII , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , ( 'http://www.cyn.net/music/' + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iIIII ) . replace ( ' ' , '%20' ) )
def IIiII1ii1i11I ( url , img ) :
 IIii11Ii1i1I = o0o0 ( url )
 oOo000O = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oOo000O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 76 - 76: oO0o + i1IiiiI1iI + oO0o * ii
def I1IIiIi ( url ) :
 IIii11Ii1i1I = o0o0 ( url )
 oOo000O = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 for type , url , I11iI1i1I11I11 in IIi :
  if '[VID]' in type :
   oOo0OoOOo0 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oOo000O + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   I1IIiIi ( oOo000O + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
def OO000o0oOoo0o ( ) :
 OOo0oOO0o0oo0 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 ii1iIIiii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooOo0O0o0 = ii1iIIiii1 . lower ( )
 OOOiiiiI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 o0o0O00 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oOo000O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 53 - 53: o0ii1I - oooOo0oo0oo
 II11iIiIIIiI = O00O0oOO00O00 ( OOOiiiiI )
 OooIiIIII1i11I = O00O0oOO00O00 ( o0o0O00 )
 o0o = O00O0oOO00O00 ( oOo000O )
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , Ii1IIiiIIi , o00O0O , OoooO0o , I11iI1i1I11I11 in IIi :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , OOOiiiiI , 1016 , Ii1IIiiIIi , i11I , o00O0O )
    if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OooIiIIII1i11I != 'Failed' :
  o0I11iII = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OooIiIIII1i11I )
  for OOOiiiiI , I11iI1i1I11I11 in o0I11iII :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 23 - 23: iI11I1II1I1I * Iii . i1IiiiI1iI - I11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for OOOiiiiI , I11iI1i1I11I11 in i1Iii1i1I :
   if ii1iIIiii1 in I11iI1i1I11I11 . lower ( ) :
    iIii ( ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 66 - 66: oOo0O0Ooo * i1IiiiI1iI / Ii / oooOo0oo0oo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: i1iIi % iI11I1II1I1I * ii
    if 60 - 60: i1IiiiI1iI * IiI1i11I / ii * I1ii11iIi11i
    if 47 - 47: IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
    if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
    if 99 - 99: Ii1I % I1ii11iIi11i
    if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
I1iO00oo0oOo = '{SF},' ; iiiIii = '{IF},' ; oO00oIiIi1i1 = '{PW},' ; iIIiiii = '{AM},' ; o0000o0o = '{GF},' ; O0OO000o = '{DD},' ; iI1I1iI1ii = '{UO},' ; iii11iI = '{LE},' ; ii1II1i1 = '{ZY},' ; oOOOOOOooO = '{UE},' ; i1iI1Iii11Iii11 = '{PE},' ; iIiiI = '{JE},' ; iI1iIIiIi1I1 = '{TH},' ; oOo0oO0 = '{LK},'
if 57 - 57: oooOo0oo0oo / Ii / i1IiiiI1iI - I1ii11iIi11i . iI11I1II1I1I
if 84 - 84: III1iiIii
def iiIi1IIiI ( ) :
 IIii11Ii1i1I = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 8021 , iiIi1IIiIi + 'iwatch.png' )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def iiiOOoO00o0OO ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 , OoO00oo0 in IIi :
  iIii ( I11iI1i1I11I11 + OoO00oo0 , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def IIiiI ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IIi1IIi11 ( url )
def IIi1IIi11 ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIii11Ii1i1I )
 OOoOooOoOOOoo = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IIii11Ii1i1I )
 oOIIiIi = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( 'VidSpot - ' + I11iI1i1I11I11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  oOo0OoOOo0 ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , I11iI1i1I11I11 in oOIIiIi :
  oOo0OoOOo0 ( 'VidUp' + I11iI1i1I11I11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for I11iI1i1I11I11 , url in OOoOooOoOOOoo :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOo0OoOOo0 ( 'TheVideo - ' + I11iI1i1I11I11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 27 - 27: OOooOOo - iI11I1II1I1I / ooOoO0O00 * i1IiiiI1iI - i1iIi
def I111I1IiI1i1 ( ) :
 IIii11Ii1i1I = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 1021 , iiIi1IIiIi + 'anime.png' )
  if 52 - 52: o0ii1I / Ii / i1i1I1IIii1II
  if 54 - 54: i1i1I1IIii1II
def O0o0 ( ) :
 IIii11Ii1i1I = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIii11Ii1i1I )
 for OOOiiiiI , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , OOOiiiiI , 1002 , iiIi1IIiIi + 'anime.png' )
  if 64 - 64: OOooOOo + IiI1i11I * OOooOOo - oOo0O0Ooo * ii
  if 27 - 27: IIiIiII11i + Ii
  if 32 - 32: ooOoO0O00
def ooO0OOOooo ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IIii11Ii1i1I )
 for iIIII in i1Iii1i1I :
  II1i1iI = iIIII
 OOoOooOoOOOoo = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IIii11Ii1i1I )
 for url in OOoOooOoOOOoo :
  iIii ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IIii11Ii1i1I )
 for url , I11iI1i1I11I11 in IIi :
  iIii ( I11iI1i1I11I11 , url , 1003 , II1i1iI )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIiIiI1ii ( url , IMAGE ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( IIii11Ii1i1I )
 for I11iI1i1I11I11 , url in IIi :
  print I11iI1i1I11I11 + '     ' + url
  if 'easy' in url :
   I1ii1iiii ( url )
  elif 'playpanda' in url :
   I1ii1iiii ( url )
   if 10 - 10: OOooOOo - OOooOOo - i1iIi - oOo0O0Ooo . I11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1ii1iiii ( url ) :
 IIii11Ii1i1I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( IIii11Ii1i1I )
 for url in IIi :
  oOo0OoOOo0 ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 43 - 43: I11i * ii
  if 1 - 1: IiI1i11I % i1i1I1IIii1II / oooOo0oo0oo * IiI1i11I
def IIioOO00oOO0o ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
def o0o0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
def iiIIiI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoo = ( '%s%s' % ( OOOO0O0OoO0O0 , url ) )
 iiI111I1iIiI = o0o0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , I1i1i , I11iI1i1I11I11 in IIi :
  oOo0OoOOo0 ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + I11iI1i1I11I11 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1i1i )
  if 16 - 16: Iii
def iII11i1 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  o0O000OO0O0 ( url , I11iI1i1I11I11 )
 else :
  ooOoO00 ( url )
def ooOoO00 ( url ) :
 import urlresolver
 try :
  II1 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( II1 , xbmcgui . ListItem ( I11iI1i1I11I11 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I11iI1i1I11I11 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def O00Oooo00 ( url ) :
 if 99 - 99: o0o00Oo0O % oO0o % ooOoO0O00 / I11i
 O0oOoo0OoO0O = open ( OOOO0OOoO0O0 , "a" )
 O0oOoo0OoO0O . write ( 'url="' + url + '"\n' )
 O0oOoo0OoO0O . close
 if 99 - 99: i1i1I1IIii1II - OOooOOo . I11i / o0o00Oo0O + o0o00Oo0O + Ii1I
 O0ooOO = xbmc . Player ( IiiI ( ) )
 import urlresolver
 try : O0ooOO . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I11iI1i1I11I11 ) )
 O0ooOO = xbmc . Player ( IiiI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O0ooOO . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def o0O000OO0O0 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OOoOOO0 = '.mp4'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.mkv' in url :
  OOoOOO0 = '.mkv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.mp3' in url :
  OOoOOO0 = '.mp3'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.avi' in url :
  OOoOOO0 = '.avi'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.mov' in url :
  OOoOOO0 = '.mov'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.mpeg' in url :
  OOoOOO0 = '.mpeg'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.mpg' in url :
  OOoOOO0 = '.mpg'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.flv' in url :
  OOoOOO0 = '.flv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 elif '.wmv' in url :
  OOoOOO0 = '.wmv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   ooOoO00 ( url )
  if O0O0ooOOO == 1 :
   IIi1iiIII11 ( url , name , OOoOOO0 )
 else :
  ooOoO00 ( url )
def IIi1iiIII11 ( url , name , cat ) :
 oO0IIIIi1IiI1I ( )
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
def oO0IIIIi1IiI1I ( ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def IIi1II1I11i ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I11iI1i1I11I11 )
 xbmc . sleep ( 1 )
 O0ooOO = xbmc . Player ( IiiI ( ) )
 o0oOoO00o . update ( 100 , '%s' % I11iI1i1I11I11 )
 xbmc . sleep ( 1 )
 O0ooOO . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 12 - 12: OOooOOo . Ii1I . I1ii11iIi11i
def III1I11i1iIi ( url ) :
 O0ooOO = xbmc . Player ( IiiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0ooOO . play ( url ) . strip ( )
 except : pass
 if 61 - 61: Iii / oooOo0oo0oo
def OOo0oOOO0 ( url ) :
 O0ooOO = xbmc . Player ( IiiI ( ) )
 import urlresolver
 OoOO0O000O0oo = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 O0ooOO . play ( OoOO0O000O0oo )
 xbmc . sleep ( 1 )
 O0ooOO . play ( url )
 if 64 - 64: oO0o % I1ii11iIi11i * I11i - oooOo0oo0oo - Iii
 if 52 - 52: Ii / I11i + i1iIi / oOo0O0Ooo / OOooOOo
def IiiI ( ) :
 try :
  IiioO = getSet ( "core-player" )
  if ( IiioO == 'DVDPLAYER' ) : oO0OooO0O = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiioO == 'MPLAYER' ) : oO0OooO0O = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiioO == 'PAPLAYER' ) : oO0OooO0O = xbmc . PLAYER_CORE_PAPLAYER
  else : oO0OooO0O = xbmc . PLAYER_CORE_AUTO
 except : oO0OooO0O = xbmc . PLAYER_CORE_AUTO
 return oO0OooO0O
 return True
 if 45 - 45: III1iiIii
def iIii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIIIIiII1 = [ ]
  IIIIIiII1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = True )
 return ooo0
 if 24 - 24: i1i1I1IIii1II % I11i + i1iIi / IIiIiII11i - i1iIi * IiI1i11I
def I1IIii11 ( name , url , mode , iconimage , fanart , description ) :
 if 43 - 43: IiI1i11I * ooOoO0O00 . oOo0O0Ooo . OOooOOo / III1iiIii - I1ii11iIi11i
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = True )
 return ooo0
 if 95 - 95: ii % oooOo0oo0oo * oooOo0oo0oo
def oOo0OoOOo0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIIIIiII1 = [ ]
  IIIIIiII1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = False )
 return ooo0
 if 24 - 24: o0ii1I * Ii / o0o00Oo0O - Ii1I
 if 93 - 93: i1iIi - ii / III1iiIii . Iii
 if 7 - 7: I11i % o0ii1I - Ii
 if 47 - 47: I1ii11iIi11i / OOooOOo
 if 26 - 26: Iii . Ii1I
 if 55 - 55: OOooOOo * i1IiiiI1iI % oO0o - oO0o
def IiIIII11i1ii ( url , heading , announce ) :
 class IIoOo0O0o ( ) :
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
   try : iiii111II = open ( announce ) ; ooOo0o = iiii111II . read ( )
   except : ooOo0o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooOo0o ) )
   return
 IIoOo0O0o ( )
 IIoOo0O0o ( )
def o0OIiII ( heading , announce ) :
 class IIoOo0O0o ( ) :
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
   try : iiii111II = open ( announce ) ; ooOo0o = iiii111II . read ( )
   except : ooOo0o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooOo0o ) )
   return
 IIoOo0O0o ( )
 IIoOo0O0o ( )
def oooOo0OOOoo0 ( ) :
 IiIIII11i1ii ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 41 - 41: i1iIi * Ii % i1iIi . i1i1I1IIii1II
 if 97 - 97: i1i1I1IIii1II - IiI1i11I + III1iiIii . OOooOOo + iI11I1II1I1I
 if 75 - 75: i1iIi + i1iIi . i1IiiiI1iI % IiI1i11I / iI11I1II1I1I * IiI1i11I
 if 13 - 13: IIiIiII11i * Ii - ooOoO0O00 * oO0o + ooOoO0O00
 if 43 - 43: o0o00Oo0O % i1i1I1IIii1II * oOo0O0Ooo
def OoOO0o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 64 - 64: IIiIiII11i + Ii
 if 17 - 17: o0o00Oo0O * oOo0O0Ooo
 if 40 - 40: iI11I1II1I1I * IiI1i11I % iI11I1II1I1I
 if 39 - 39: ooOoO0O00 . o0ii1I - I1ii11iIi11i
 if 91 - 91: oOo0O0Ooo - ii - ii
 if 69 - 69: IiI1i11I * Ii / ooOoO0O00
 if 86 - 86: oOo0O0Ooo % Iii * o0o00Oo0O + ooOoO0O00 % i1IiiiI1iI
 if 97 - 97: IIiIiII11i * OOooOOo - i1IiiiI1iI / Ii / OOooOOo
 if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
 if 74 - 74: oooOo0oo0oo
 if 30 - 30: o0o00Oo0O . o0ii1I / I11i + oOo0O0Ooo - o0o00Oo0O
 if 88 - 88: Ii
 if 33 - 33: oO0o + o0o00Oo0O
 if 20 - 20: I11i % Iii . i1iIi - ooOoO0O00 . o0o00Oo0O
 if 10 - 10: ooOoO0O00
 if 49 - 49: i1IiiiI1iI - o0ii1I . o0o00Oo0O
 if 46 - 46: oooOo0oo0oo
 if 64 - 64: oOo0O0Ooo / OOooOOo
 if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
 if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
 if 91 - 91: oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % o0ii1I
 if 3 - 3: oOo0O0Ooo . Iii / Ii1I
 if 2 - 2: III1iiIii + Iii / iI11I1II1I1I . Ii . ooOoO0O00 * i1iIi
def IIoOoo0oooo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI11I1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 31 - 31: IiI1i11I / oO0o - IIiIiII11i . I11i
def i1IIII1I1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoOoO0OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 96 - 96: IiI1i11I / o0ii1I / I1ii11iIi11i
def IIIIii1Ii11i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0O00OO00O00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 89 - 89: ooOoO0O00 . o0ii1I * i1IiiiI1iI + iI11I1II1I1I . OOooOOo
def i111Iii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0o0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 48 - 48: o0ii1I - o0ii1I % o0o00Oo0O . III1iiIii
def O0Oii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOo0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 54 - 54: Ii1I + Ii1I % iI11I1II1I1I
def O00i1IiI111II1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiii11I1iIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 100 - 100: i1i1I1IIii1II
def oOOO0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIio0oO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 28 - 28: o0o00Oo0O % IIiIiII11i / OOooOOo / oooOo0oo0oo
def O0OoIi111IiiiIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iII1ii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 16 - 16: III1iiIii * oO0o * Ii - i1iIi
def Oo00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiiiiiiiI1i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 42 , Ii1IIiiIIi , i11I , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 10 - 10: o0o00Oo0O + o0o00Oo0O % o0o00Oo0O % ooOoO0O00 + Iii . Ii1I
def iIiIi11 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I11iI1i1I11I11 , url , Ii1IIiiIIi , i11I , iiIii1I in IIi :
  I1I1II1I11 ( I11iI1i1I11I11 , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIii1I )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 53 - 53: o0o00Oo0O . I11i . IIiIiII11i * OOooOOo . oooOo0oo0oo
 if 78 - 78: OOooOOo * OOooOOo - oO0o / i1i1I1IIii1II
 if 24 - 24: i1IiiiI1iI . i1i1I1IIii1II + i1iIi . Ii1I . IIiIiII11i
 if 25 - 25: oOo0O0Ooo
 if 88 - 88: ooOoO0O00
 if 93 - 93: Ii1I . oO0o
 if 67 - 67: IIiIiII11i + ii + oOo0O0Ooo
 if 76 - 76: o0o00Oo0O / I1ii11iIi11i . OOooOOo
 if 81 - 81: I11i + IIiIiII11i % i1IiiiI1iI - i1i1I1IIii1II + i1iIi - Ii1I
def ooOo0 ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( o0 ) :
     o00i1iII11iIiiI1 = 0
     o00i1iII11iIiiI1 += len ( o00oO0o0oo0O )
     if o00i1iII11iIiiI1 > 0 :
      for iiii111II in o00oO0o0oo0O :
       os . unlink ( os . path . join ( iIIi1I1Ii1 , iiii111II ) )
  i1IIi = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( i1IIi )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 86 - 86: IiI1i11I / IiI1i11I . i1iIi - oO0o
 if 19 - 19: Iii
 if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
 if 11 - 11: iI11I1II1I1I
 if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
 if 80 - 80: ooOoO0O00
 if 56 - 56: IIiIiII11i - I11i
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
def iI1III ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
def iII11 ( url ) :
 oO0o0oO0O = os . path . join ( oooOOOOO , 'addon_data' )
 IIiiI1iiI = [
 ( oO0o0oO0O ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oO0o0oO0O , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0oO0O , 'plugin.video.itv' , 'Images' ) ) ]
 if 92 - 92: oOo0O0Ooo / III1iiIii - o0ii1I . o0o00Oo0O % oooOo0oo0oo
 Ii1iiiIIIii = 0
 if 35 - 35: Iii - i1iIi . Ii1I + iI11I1II1I1I . oooOo0oo0oo / Iii
 for OOOOoO00o0O in IIiiI1iiI :
  if os . path . exists ( OOOOoO00o0O ) and not OOOOoO00o0O in [ oo0o0O00 , oO0o0oO0O ] :
   for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( OOOOoO00o0O ) :
    o00i1iII11iIiiI1 = 0
    o00i1iII11iIiiI1 += len ( o00oO0o0oo0O )
    if o00i1iII11iIiiI1 > 0 :
     for iiii111II in o00oO0o0oo0O :
      if not iiii111II in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( iIIi1I1Ii1 , iiii111II ) )
       except :
        pass
      else : i11i1 ( 'Ignore Log File: %s' % iiii111II )
     for i1ooOO00o0 in I1111 :
      try :
       shutil . rmtree ( os . path . join ( iIIi1I1Ii1 , i1ooOO00o0 ) )
       Ii1iiiIIIii += 1
       i11i1 ( "[Success] cleared %s files from %s" % ( str ( o00i1iII11iIiiI1 ) , os . path . join ( OOOOoO00o0O , i1ooOO00o0 ) ) )
      except :
       i11i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOOoO00o0O , i1ooOO00o0 ) )
  else :
   for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( OOOOoO00o0O ) :
    for i1ooOO00o0 in I1111 :
     if 'cache' in i1ooOO00o0 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIIi1I1Ii1 , i1ooOO00o0 ) )
       Ii1iiiIIIii += 1
       i11i1 ( "[Success] wiped %s " % os . path . join ( OOOOoO00o0O , i1ooOO00o0 ) )
      except :
       i11i1 ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOOoO00o0O , i1ooOO00o0 ) )
       if 72 - 72: ooOoO0O00 * Iii
 iI1III ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % Ii1iiiIIIii )
 if 60 - 60: IiI1i11I
 if 56 - 56: o0ii1I * oOo0O0Ooo - I11i % Ii1I / IiI1i11I % i1i1I1IIii1II
 if 43 - 43: I1ii11iIi11i % i1i1I1IIii1II . Ii - o0o00Oo0O
 if 5 - 5: ooOoO0O00 + o0ii1I
 if 38 - 38: oOo0O0Ooo . o0o00Oo0O + oooOo0oo0oo / Ii1I . iI11I1II1I1I - ooOoO0O00
 if 3 - 3: I1ii11iIi11i + i1i1I1IIii1II
 if 65 - 65: oOo0O0Ooo / OOooOOo % oOo0O0Ooo * Ii * ii / Iii
def O00OO00OOOoO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( oooo0 ) :
   o00i1iII11iIiiI1 = 0
   o00i1iII11iIiiI1 += len ( o00oO0o0oo0O )
   if 31 - 31: i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo - i1iIi / i1IiiiI1iI
   if 39 - 39: I1ii11iIi11i - ii . ooOoO0O00 + ooOoO0O00 % o0ii1I . oooOo0oo0oo
   if o00i1iII11iIiiI1 > 0 :
    if 30 - 30: o0o00Oo0O / i1i1I1IIii1II
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o00i1iII11iIiiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: I1ii11iIi11i
     for iiii111II in o00oO0o0oo0O :
      os . unlink ( os . path . join ( iIIi1I1Ii1 , iiii111II ) )
     for i1ooOO00o0 in I1111 :
      shutil . rmtree ( os . path . join ( iIIi1I1Ii1 , i1ooOO00o0 ) )
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
 if 5 - 5: IiI1i11I
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
 if 30 - 30: iI11I1II1I1I
 if 14 - 14: I11i + o0ii1I
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
 if 100 - 100: ooOoO0O00
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
def I1II1I11I1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oooo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( oooo0 ) :
   o00i1iII11iIiiI1 = 0
   o00i1iII11iIiiI1 += len ( o00oO0o0oo0O )
   if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
   if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
   if o00i1iII11iIiiI1 > 0 :
    if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o00i1iII11iIiiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
     for iiii111II in o00oO0o0oo0O :
      os . unlink ( os . path . join ( iIIi1I1Ii1 , iiii111II ) )
     for i1ooOO00o0 in I1111 :
      shutil . rmtree ( os . path . join ( iIIi1I1Ii1 , i1ooOO00o0 ) )
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
 iII11 ( url )
 return
 if 12 - 12: ii % i1i1I1IIii1II
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
 if 79 - 79: o0o00Oo0O
 if 71 - 71: oO0o - o0o00Oo0O
 if 73 - 73: iI11I1II1I1I
 if 7 - 7: OOooOOo
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
 if 3 - 3: Iii
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
def IiIIooO00oOo0 ( url , name ) :
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIiIiii111iI = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 i11I1I1iI11I = os . path . join ( oOOooOoo , 'advancedsettings.xml.bak' )
 if os . path . exists ( i11I1I1iI11I ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IIiIiii111iI = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
   try :
    os . remove ( IIiIiii111iI )
    print '=== GenieTv - REMOVING    ' + str ( IIiIiii111iI ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   oOOoooo = open ( IIiIiii111iI , "w" )
   oOOoooo . write ( iiI111I1iIiI )
   oOOoooo . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IIiIiii111iI ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IIiIiii111iI = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
  try :
   os . remove ( IIiIiii111iI )
   print '=== GenieTv - REMOVING    ' + str ( IIiIiii111iI ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  oOOoooo = open ( IIiIiii111iI , "w" )
  oOOoooo . write ( iiI111I1iIiI )
  oOOoooo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIiIiii111iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 84 - 84: o0ii1I / i1iIi - oO0o / oO0o / ii
def O0oOooOoOo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIiIiii111iI = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 try :
  oOOoooo = open ( IIiIiii111iI ) . read ( )
  if 'zero' in oOOoooo :
   name = '0CACHE'
  elif 'tuxen' in oOOoooo :
   name = 'TUXENS'
  elif 'muckys' in oOOoooo :
   name = 'MUCKYS'
  elif 'p2p1' in oOOoooo :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOOoooo :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOOoooo :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 54 - 54: IiI1i11I . oO0o . iI11I1II1I1I
def iIiiiI1 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIiIiii111iI = os . path . join ( oOOooOoo , 'advancedsettings.xml' )
 try :
  os . remove ( IIiIiii111iI )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IIiIiii111iI ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
 if 7 - 7: o0ii1I
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
 if 55 - 55: oO0o % OOooOOo
 if 58 - 58: o0ii1I
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
def IiI11Ii1iI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for OOOii , O0oo0oO0oOoo , Ooi1I11i1 , II1iiiii in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOOii , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Ooi1I11i1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1iiiii )
  inc = inc + 1
  if 7 - 7: oOo0O0Ooo * IiI1i11I % ii
  if 64 - 64: I11i
  if 22 - 22: I11i / ii
  if 63 - 63: i1IiiiI1iI
  if 52 - 52: iI11I1II1I1I / IiI1i11I
  if 46 - 46: i1IiiiI1iI . Ii
  if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
  if 52 - 52: I11i * o0o00Oo0O + Ii1I
  if 83 - 83: Iii + oooOo0oo0oo - ii
def I1i1iiIIII ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IIiIiii111iI = os . path . join ( oOOooOoo , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  oOOoooo = open ( IIiIiii111iI , "w" )
  oOOoooo . write ( iiI111I1iIiI )
  oOOoooo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIiIiii111iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 44 - 44: I1ii11iIi11i
def iI1I ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOOooOoo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IIiIiii111iI = os . path . join ( oOOooOoo , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  oOOoooo = open ( IIiIiii111iI , "w" )
  oOOoooo . write ( iiI111I1iIiI )
  oOOoooo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIiIiii111iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 29 - 29: o0o00Oo0O - Iii * oOo0O0Ooo
 if 5 - 5: IIiIiII11i - I11i + ooOoO0O00 - o0ii1I % Ii
def o0ooOooO0oo ( ) :
 try :
  ooo0OIII11I1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ooo0OIII11I1i ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    O0O00o0Ooo0O0 = os . path . join ( ooo0OIII11I1i , "source.db" )
    os . unlink ( O0O00o0Ooo0O0 )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 20 - 20: oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
 if 29 - 29: oooOo0oo0oo
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
 if 91 - 91: Ii . Ii1I + Iii
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
def oOoO0 ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; oo000Ooo = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oo000Ooo :
  OOoOoo00oO = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; OOoOoo00oO = xbmc . translatePath ( OOoOoo00oO ) ;
  oo0O = os . path . join ( OOoOoo00oO , ".." , ".." ) ; oo0O = os . path . abspath ( oo0O ) ; pluginlog ( "freshstart.main_list xbmcPath=" + oo0O ) ; O0oo000O00oo = False
  try :
   for iIIi1I1Ii1 , I1111 , o00oO0o0oo0O in os . walk ( oo0O , topdown = True ) :
    I1111 [ : ] = [ i1ooOO00o0 for i1ooOO00o0 in I1111 if i1ooOO00o0 not in o0oO0 ]
    for I11iI1i1I11I11 in o00oO0o0oo0O :
     try : os . remove ( os . path . join ( iIIi1I1Ii1 , I11iI1i1I11I11 ) )
     except :
      if I11iI1i1I11I11 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0oo000O00oo = True
      pluginlog ( "Error removing " + iIIi1I1Ii1 + " " + I11iI1i1I11I11 )
    for I11iI1i1I11I11 in I1111 :
     try : os . rmdir ( os . path . join ( iIIi1I1Ii1 , I11iI1i1I11I11 ) )
     except :
      if I11iI1i1I11I11 not in [ "Database" , "userdata" ] : O0oo000O00oo = True
      pluginlog ( "Error removing " + iIIi1I1Ii1 + " " + I11iI1i1I11I11 )
   if not O0oo000O00oo : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 IIIIiII ( )
 if 91 - 91: Ii
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
def Oo0OOOO ( ) :
 oOOIiI1iIiI1i1 = [ ]
 oOo0o0 = sys . argv [ 2 ]
 if len ( oOo0o0 ) >= 2 :
  Oo0 = sys . argv [ 2 ]
  IIiiI11iI = Oo0 . replace ( '?' , '' )
  if ( Oo0 [ len ( Oo0 ) - 1 ] == '/' ) :
   Oo0 = Oo0 [ 0 : len ( Oo0 ) - 2 ]
  IIi1III1II = IIiiI11iI . split ( '&' )
  oOOIiI1iIiI1i1 = { }
  for I1I1iI11ii in range ( len ( IIi1III1II ) ) :
   o0o0OOOO = { }
   o0o0OOOO = IIi1III1II [ I1I1iI11ii ] . split ( '=' )
   if ( len ( o0o0OOOO ) ) == 2 :
    oOOIiI1iIiI1i1 [ o0o0OOOO [ 0 ] ] = o0o0OOOO [ 1 ]
    if 9 - 9: o0ii1I * i1IiiiI1iI . ii / oO0o
 return oOOIiI1iIiI1i1
 if 44 - 44: Ii % ii % o0o00Oo0O - I1ii11iIi11i
oO000ooO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OoooOOo0oOO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oOoO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OoOiIIiI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
O00oo0o0000 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IIi111i1i1III = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iI11I1Iii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
O00oOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OoOoO0OoO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O0O00OO00O00O = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
O0o0OOo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oOo0oo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iiii11I1iIIII = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IiIio0oO0O = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iII1ii1i1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiiiiiiiI1i11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OooooIIIiI1iIIII = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii1Ii1ii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiI1i = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ooOOoOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iI1IIIIII = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iiOo0ooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOOO0O0OoO0O0 = base64 . decodestring ( 'Q1VOVA==' )
def I1I1Ii ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 o0oooO . setProperty ( 'fanart_image' , fanart )
 o0oooO . setProperty ( "IsPlayable" , "true" )
 oO0OOoooooo0o = [ ]
 oO0OOoooooo0o . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 oO0OOoooooo0o . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 o0oooO . addContextMenuItems ( oO0OOoooooo0o , replaceItems = True )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = False )
 return ooo0
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIiII1 = [ ]
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = True )
 return ooo0
 if 64 - 64: I11i
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooo0O0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooo0 = True
 o0oooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0oooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0oooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIiII1 = [ ]
  if showcontext == 'fav' :
   IIIIIiII1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   IIIIIiII1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0oooO . addContextMenuItems ( IIIIIiII1 )
 ooo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo0O0 , listitem = o0oooO , isFolder = False )
 return ooo0
 if 84 - 84: IIiIiII11i
 if 58 - 58: i1i1I1IIii1II + i1iIi + III1iiIii . ooOoO0O00 + Ii1I . I1ii11iIi11i
Oo0 = Oo0OOOO ( )
OOOiiiiI = None
I11iI1i1I11I11 = None
IIiii = None
Ii1IIiiIIi = None
i11I = None
iiIii1I = None
oOooooO0o0OOO = None
O0o0000o00OO0 = None
if 50 - 50: I1ii11iIi11i
if 91 - 91: oOo0O0Ooo + ooOoO0O00 * o0o00Oo0O / oO0o + I11i
try :
 O0o0000o00OO0 = int ( Oo0 [ "fav_mode" ] )
except :
 pass
 if 54 - 54: III1iiIii + Iii / ii / Iii / ooOoO0O00
try :
 OOOiiiiI = urllib . unquote_plus ( Oo0 [ "url" ] )
except :
 pass
try :
 I11iI1i1I11I11 = urllib . unquote_plus ( Oo0 [ "name" ] )
except :
 pass
try :
 Ii1IIiiIIi = urllib . unquote_plus ( Oo0 [ "iconimage" ] )
except :
 pass
try :
 IIiii = int ( Oo0 [ "mode" ] )
except :
 pass
try :
 i11I = urllib . unquote_plus ( Oo0 [ "fanart" ] )
except :
 pass
try :
 iiIii1I = urllib . unquote_plus ( Oo0 [ "description" ] )
except :
 pass
 if 94 - 94: oO0o - oO0o . OOooOOo
 if 44 - 44: oOo0O0Ooo / III1iiIii . IiI1i11I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( IIiii )
print "URL: " + str ( OOOiiiiI )
print "Name: " + str ( I11iI1i1I11I11 )
print "IconImage: " + str ( Ii1IIiiIIi )
if 48 - 48: I11i . ooOoO0O00 - oooOo0oo0oo % o0ii1I
if 62 - 62: IIiIiII11i % ooOoO0O00
def Ii1IIiI1i ( content , viewType ) :
 if 98 - 98: oOo0O0Ooo - I1ii11iIi11i - o0ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 80 - 80: i1iIi . Ii
if Ii1IIiiIIi == None : Ii1IIiiIIi = O0O
if i11I == None : i11I = Oo00OOOOO
if IIiii == None :
 Iii1I1I11iiI1 ( )
 if 18 - 18: Iii + Ii
elif IIiii == 1 :
 OO00O00o0O ( OOOiiiiI )
 if 46 - 46: o0ii1I * o0ii1I
elif IIiii == 44 :
 oo0O0o00o0O ( OOOiiiiI )
 if 57 - 57: i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo * i1IiiiI1iI - oooOo0oo0oo
elif IIiii == 2 :
 ii1IIi1iI1ii1 ( )
 if 97 - 97: Ii1I
elif IIiii == 3 :
 OOo00o0oo0 ( )
 if 3 - 3: i1iIi + Ii . iI11I1II1I1I
elif IIiii == 21 :
 i1i1II ( )
 if 70 - 70: i1iIi
elif IIiii == 4 :
 OoOooOo00o ( )
 if 3 - 3: oOo0O0Ooo - oOo0O0Ooo
elif IIiii == 5 :
 oO00O0o0oOOO ( OOOiiiiI )
 if 89 - 89: OOooOOo
elif IIiii == 6 :
 O00OO00OOOoO ( OOOiiiiI )
 if 27 - 27: ooOoO0O00 % OOooOOo / o0ii1I * o0ii1I / Iii
elif IIiii == 7 :
 IiIIooO00oOo0 ( OOOiiiiI , I11iI1i1I11I11 )
 if 11 - 11: oooOo0oo0oo
elif IIiii == 8 :
 O0oOooOoOo ( OOOiiiiI , I11iI1i1I11I11 )
 if 58 - 58: oO0o * ii
elif IIiii == 9 :
 FIXREPOSADDONS ( OOOiiiiI )
 if 47 - 47: IiI1i11I - I1ii11iIi11i
elif IIiii == 10 :
 OoOO0o ( )
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + Iii / IIiIiII11i + i1iIi
elif IIiii == 11 :
 iIiiiI1 ( OOOiiiiI )
 if 26 - 26: o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
elif IIiii == 12 :
 IiI11Ii1iI ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 35 - 35: ooOoO0O00 % Ii + o0ii1I
elif IIiii == 13 :
 ooOo0 ( )
 if 14 - 14: oO0o * ii
elif IIiii == 14 :
 iII11 ( OOOiiiiI )
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
elif IIiii == 15 :
 I11iIi1i1I1i1 ( )
 if 97 - 97: Iii % IIiIiII11i % o0ii1I . IIiIiII11i . iI11I1II1I1I
elif IIiii == 16 :
 I1i1iiIIII ( OOOiiiiI , I11iI1i1I11I11 )
 if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IiI1i11I
elif IIiii == 17 :
 iI1I ( OOOiiiiI , I11iI1i1I11I11 )
 if 25 - 25: i1i1I1IIii1II / o0o00Oo0O + i1IiiiI1iI % Ii / oOo0O0Ooo
elif IIiii == 18 :
 o0ooOooO0oo ( )
 if 62 - 62: IiI1i11I . Iii * ooOoO0O00 + IiI1i11I
elif IIiii == 19 :
 IiiiI11 ( OOOiiiiI )
 if 95 - 95: o0ii1I / I11i % i1iIi - oOo0O0Ooo / oooOo0oo0oo * oooOo0oo0oo
elif IIiii == 40 :
 Iiii11 ( I11iI1i1I11I11 , OOOiiiiI , iiIii1I )
 if 6 - 6: oO0o % III1iiIii + iI11I1II1I1I
elif IIiii == 42 :
 o0ooo0oooO ( I11iI1i1I11I11 , OOOiiiiI , iiIii1I )
 if 18 - 18: IIiIiII11i . o0ii1I + OOooOOo + o0o00Oo0O - Iii
elif IIiii == 43 :
 oo0O0O ( OOOiiiiI )
 if 30 - 30: IIiIiII11i
elif IIiii == 20 :
 OOOO00 ( OOOiiiiI )
 if 26 - 26: Iii - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * oooOo0oo0oo . ii
elif IIiii == 22 :
 IIoOoo0oooo ( OOOiiiiI )
 if 99 - 99: i1i1I1IIii1II . oO0o / oooOo0oo0oo
elif IIiii == 23 :
 i1IIII1I1i ( OOOiiiiI )
 if 12 - 12: iI11I1II1I1I + i1iIi * i1IiiiI1iI % ii / iI11I1II1I1I
elif IIiii == 24 :
 IIIIii1Ii11i ( OOOiiiiI )
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - Ii1I
elif IIiii == 25 :
 i111Iii1i ( OOOiiiiI )
 if 8 - 8: OOooOOo / o0ii1I
elif IIiii == 26 :
 O0Oii ( OOOiiiiI )
 if 12 - 12: iI11I1II1I1I
elif IIiii == 27 :
 O00i1IiI111II1 ( OOOiiiiI )
 if 52 - 52: i1i1I1IIii1II . Ii1I + i1i1I1IIii1II
elif IIiii == 28 :
 oOOO0 ( OOOiiiiI )
 if 73 - 73: IIiIiII11i / Ii / i1iIi
elif IIiii == 29 :
 O0OoIi111IiiiIi ( OOOiiiiI )
 if 1 - 1: IiI1i11I + OOooOOo / III1iiIii - oOo0O0Ooo % oOo0O0Ooo
elif IIiii == 30 :
 I11iIiIii ( OOOiiiiI )
 if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
elif IIiii == 31 :
 Oo00 ( OOOiiiiI )
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
elif IIiii == 32 :
 oOOOOO0 ( )
 if 30 - 30: Iii
elif IIiii == 33 :
 IIi1I1 ( )
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
elif IIiii == 35 :
 oOOI1 ( OOOiiiiI )
 if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
elif IIiii == 34 :
 oO00o0oOoo ( OOOiiiiI )
 if 15 - 15: I11i
elif IIiii == 36 :
 iIIiI1 ( OOOiiiiI )
 if 55 - 55: Ii / ii - Iii
elif IIiii == 37 :
 III1I1 ( OOOiiiiI )
 if 89 - 89: Iii - ooOoO0O00 - ooOoO0O00 * oooOo0oo0oo - o0o00Oo0O
elif IIiii == 38 :
 iIIOOo0O ( OOOiiiiI )
 if 94 - 94: I1ii11iIi11i / Iii . Ii1I
elif IIiii == 41 :
 oOoO0 ( Oo0 )
 if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
elif IIiii == 39 :
 iIiIi11 ( OOOiiiiI )
 if 72 - 72: i1IiiiI1iI * oO0o + I1ii11iIi11i / o0ii1I % oooOo0oo0oo
elif IIiii == 45 :
 TEXTS ( )
 if 84 - 84: OOooOOo / I11i
elif IIiii == 46 :
 oooOo0OOOoo0 ( )
 if 9 - 9: o0ii1I
elif IIiii == 47 :
 GEVID ( )
 if 76 - 76: oOo0O0Ooo % I1ii11iIi11i / iI11I1II1I1I - I1ii11iIi11i
elif IIiii == 48 :
 i1iIII1IIi ( I11iI1i1I11I11 , OOOiiiiI , iiIii1I )
 if 34 - 34: OOooOOo - ooOoO0O00 + oooOo0oo0oo + o0ii1I . I11i
elif IIiii == 49 :
 iiOO0O0Ooo ( )
 if 42 - 42: oO0o
elif IIiii == 22222 :
 O00Oooo00 ( OOOiiiiI )
 if 59 - 59: oO0o . i1IiiiI1iI % oO0o
elif IIiii == 222225 :
 I1i ( OOOiiiiI )
 if 22 - 22: I1ii11iIi11i
elif IIiii == 222 :
 iII11i1 ( OOOiiiiI )
 if 21 - 21: I11i
elif IIiii == 2222222 :
 ooOoO00 ( OOOiiiiI )
 if 86 - 86: i1iIi / iI11I1II1I1I . oooOo0oo0oo
elif IIiii == 222222 :
 o0O000OO0O0 ( OOOiiiiI , I11iI1i1I11I11 )
 if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
elif IIiii == 333 :
 iiIIiI ( OOOiiiiI )
 if 30 - 30: OOooOOo . oooOo0oo0oo % oooOo0oo0oo / IIiIiII11i + ooOoO0O00
 if 61 - 61: ooOoO0O00 % IIiIiII11i * IIiIiII11i . I11i / Ii1I - i1IiiiI1iI
elif IIiii == 1020 :
 I111I1IiI1i1 ( )
 if 93 - 93: o0ii1I - ooOoO0O00
elif IIiii == 1021 :
 ANIMEEP ( )
 if 3 - 3: i1i1I1IIii1II + oO0o - IiI1i11I / o0ii1I
elif IIiii == 1022 :
 ANIMEPLAY ( OOOiiiiI )
 if 58 - 58: o0ii1I * Iii
elif IIiii == 1001 :
 O0o0 ( )
 if 95 - 95: i1i1I1IIii1II
elif IIiii == 1005 :
 IiiIi1II ( )
 if 49 - 49: oOo0O0Ooo
elif IIiii == 1007 :
 IiII1IiiI ( OOOiiiiI )
 if 23 - 23: i1IiiiI1iI
elif IIiii == 1010 :
 OOOOoOoO ( OOOiiiiI )
 if 5 - 5: Ii1I % OOooOOo . ii . I11i + Ii
elif IIiii == 1011 :
 I1IIi1I11iI ( OOOiiiiI )
 if 54 - 54: i1iIi - o0o00Oo0O + IiI1i11I
elif IIiii == 1012 :
 iIII1 ( OOOiiiiI )
 if 34 - 34: o0ii1I - oooOo0oo0oo % IiI1i11I
elif IIiii == 1030 :
 O0II ( )
 if 48 - 48: i1i1I1IIii1II - o0o00Oo0O
elif IIiii == 1031 :
 IIiII1ii1i11I ( OOOiiiiI , Ii1IIiiIIi )
 if 17 - 17: iI11I1II1I1I . III1iiIii / i1iIi % Iii + I11i - iI11I1II1I1I
elif IIiii == 1032 :
 I1IIiIi ( OOOiiiiI )
 if 95 - 95: OOooOOo + oooOo0oo0oo - Iii * ooOoO0O00 + ooOoO0O00 * o0o00Oo0O
elif IIiii == 1006 :
 Parse . ParseURL ( OOOiiiiI )
 if 60 - 60: I1ii11iIi11i + Iii % iI11I1II1I1I % i1i1I1IIii1II - i1IiiiI1iI / I11i
elif IIiii == 2030 :
 Parse . addonParseURL ( OOOiiiiI )
 if 9 - 9: III1iiIii / i1i1I1IIii1II % o0o00Oo0O * i1IiiiI1iI - iI11I1II1I1I % ooOoO0O00
elif IIiii == 2031 :
 Parse . apkParseURL ( OOOiiiiI )
 if 83 - 83: OOooOOo + oooOo0oo0oo / ii
elif IIiii == 2032 :
 Parse . ParseBOSS ( OOOiiiiI )
 if 39 - 39: oO0o % IiI1i11I . i1i1I1IIii1II . IIiIiII11i - Ii
elif IIiii == 1002 :
 ooO0OOOooo ( OOOiiiiI )
 if 85 - 85: o0o00Oo0O - OOooOOo
elif IIiii == 1003 :
 IiIIiIiI1ii ( OOOiiiiI , Ii1IIiiIIi )
 if 17 - 17: I11i / ooOoO0O00 / oooOo0oo0oo
elif IIiii == 1004 :
 I1ii1iiii ( OOOiiiiI )
 if 91 - 91: Ii1I / o0ii1I - OOooOOo . Iii / i1i1I1IIii1II
elif IIiii == 1008 :
 IIiI ( )
 if 16 - 16: III1iiIii % IiI1i11I . i1i1I1IIii1II . oOo0O0Ooo % o0o00Oo0O * Iii
elif IIiii == 1009 :
 O0oo0O0OO0OOo ( OOOiiiiI )
 if 99 - 99: OOooOOo / ii + IiI1i11I * Iii * Ii + oooOo0oo0oo
elif IIiii == 2001 :
 ooOo000 ( )
 if 40 - 40: IIiIiII11i / Iii % oOo0O0Ooo - o0o00Oo0O
elif IIiii == 2002 :
 iII1Ii1ii111 ( OOOiiiiI )
 if 39 - 39: Ii - OOooOOo % oooOo0oo0oo + i1iIi + Ii
elif IIiii == 1013 :
 OoOo0O00 ( )
elif IIiii == 10111113 :
 iIIi1 ( OOOiiiiI )
 if 59 - 59: III1iiIii / OOooOOo - i1IiiiI1iI - i1iIi . i1i1I1IIii1II
elif IIiii == 1014 :
 oOOOiII1iII ( )
 if 87 - 87: i1i1I1IIii1II + oOo0O0Ooo * i1IiiiI1iI * I11i + o0o00Oo0O
elif IIiii == 1015 :
 iiii11i1ii1 ( OOOiiiiI )
 if 21 - 21: i1IiiiI1iI + OOooOOo + OOooOOo . IIiIiII11i / i1IiiiI1iI . oOo0O0Ooo
elif IIiii == 1016 :
 o00o ( OOOiiiiI , Ii1IIiiIIi , I11iI1i1I11I11 )
 if 66 - 66: i1IiiiI1iI % i1i1I1IIii1II . IiI1i11I * ooOoO0O00
elif IIiii == 1017 :
 IiIi1i1ii ( )
 if 81 - 81: ii * oOo0O0Ooo / i1IiiiI1iI
elif IIiii == 1018 :
 Oo000o ( OOOiiiiI )
 if 10 - 10: oOo0O0Ooo - IIiIiII11i / III1iiIii * IIiIiII11i
elif IIiii == 1019 :
 iII11I1Ii1 ( OOOiiiiI )
elif IIiii == 10190 :
 oOo0oO ( OOOiiiiI )
 if 67 - 67: IIiIiII11i . o0ii1I % i1i1I1IIii1II . I1ii11iIi11i + III1iiIii
elif IIiii == 1023 :
 IiIII ( )
 if 10 - 10: oooOo0oo0oo - oO0o * i1i1I1IIii1II / iI11I1II1I1I - OOooOOo
elif IIiii == 1024 :
 Ii1I111Ii ( OOOiiiiI )
 if 20 - 20: III1iiIii % oOo0O0Ooo + iI11I1II1I1I % IiI1i11I
elif IIiii == 1025 :
 OOo000OO0Oo0O ( OOOiiiiI )
 if 100 - 100: I11i - I1ii11iIi11i % i1IiiiI1iI . Ii % ii
elif IIiii == 4001 :
 iiI1I1 ( )
 if 39 - 39: Ii1I / Ii * ooOoO0O00 * I1ii11iIi11i
elif IIiii == 4002 :
 iiiI ( )
 if 39 - 39: oO0o * ii / ooOoO0O00 + I1ii11iIi11i
elif IIiii == 4003 :
 Ii1 ( )
 if 57 - 57: o0o00Oo0O
elif IIiii == 4004 :
 oOOoo ( )
 if 83 - 83: oooOo0oo0oo / o0ii1I * oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I
elif IIiii == 4005 :
 I1IIIiI1I1ii1 ( )
 if 1 - 1: Iii / ii / IiI1i11I
elif IIiii == 4006 :
 OOOoO000 ( )
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / Iii * I1ii11iIi11i
elif IIiii == 4007 :
 ooo0O ( )
 if 91 - 91: oO0o . IiI1i11I
elif IIiii == 4008 :
 i11i1iiiII ( )
 if 82 - 82: Ii1I / I1ii11iIi11i
elif IIiii == 40099 : oO0oo0O0 ( )
elif IIiii == 4009 : iI1iIIIIIiIi1 ( )
elif IIiii == 4010 : O0oo0ooo0 ( )
elif IIiii == 3000 :
 i1i1iiI11I ( )
 if 63 - 63: oOo0O0Ooo
elif IIiii == 3001 :
 OOOOo00oOOO00 ( )
 if 3 - 3: IiI1i11I + Ii1I
elif IIiii == 3002 :
 II1IoO0Ooo0o00o ( OOOiiiiI )
 if 35 - 35: i1i1I1IIii1II * IiI1i11I * i1i1I1IIii1II * i1IiiiI1iI * III1iiIii * ooOoO0O00
elif IIiii == 3003 :
 oOoOOO0oO0O ( OOOiiiiI )
 if 43 - 43: oO0o * oOo0O0Ooo / III1iiIii . Ii + IiI1i11I + I11i
elif IIiii == 3004 :
 O0iIIii1 ( OOOiiiiI )
 if 1 - 1: oOo0O0Ooo % I11i . i1IiiiI1iI + Iii * i1i1I1IIii1II
elif IIiii == 404 :
 ooO0oo00o00 ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi )
 if 41 - 41: oO0o * i1i1I1IIii1II - IIiIiII11i
elif IIiii == 405 :
 IIi1II1I11i ( OOOiiiiI )
 if 2 - 2: III1iiIii + III1iiIii - oO0o * IiI1i11I . i1i1I1IIii1II
elif IIiii == 7030 :
 i1i1i11IIii ( )
 if 91 - 91: i1iIi
elif IIiii == 7021 :
 II11iii ( I11iI1i1I11I11 )
 if 22 - 22: i1iIi % oO0o * OOooOOo + I1ii11iIi11i
elif IIiii == 7022 :
 o0o0000O ( I11iI1i1I11I11 )
 if 44 - 44: o0o00Oo0O - Iii
elif IIiii == 7000 :
 iii111III1ii1 ( I11iI1i1I11I11 , OOOiiiiI , img )
 if 43 - 43: o0o00Oo0O
elif IIiii == 7050 :
 iI1i1iI1iI ( OOOiiiiI )
 if 50 - 50: Iii - ii
elif IIiii == 7051 :
 Iii1iIIi1iIii ( OOOiiiiI )
 if 29 - 29: i1i1I1IIii1II * i1i1I1IIii1II
elif IIiii == 7052 :
 iI1i1IIi1i1 ( OOOiiiiI )
 if 44 - 44: i1iIi . oOo0O0Ooo * i1i1I1IIii1II * o0ii1I
elif IIiii == 7053 :
 Oooo ( OOOiiiiI )
 if 41 - 41: ooOoO0O00 % Ii + Iii % ii / Ii1I
elif IIiii == 7054 :
 CoolPlay ( OOOiiiiI )
 if 8 - 8: ii - oO0o / Ii / o0o00Oo0O . III1iiIii
elif IIiii == 7060 :
 ii1I11iIi ( )
 if 86 - 86: i1iIi * ii + IiI1i11I + I11i
elif IIiii == 7061 :
 O00oOo00o0o ( OOOiiiiI )
 if 79 - 79: ooOoO0O00 % Ii1I - oO0o % Ii1I
elif IIiii == 7063 :
 IiO00oo0o0ooO ( OOOiiiiI )
 if 6 - 6: I1ii11iIi11i / IiI1i11I . Ii
elif IIiii == 7062 :
 IiiIiI1IIII11II ( OOOiiiiI )
 if 8 - 8: Ii1I + o0o00Oo0O - i1i1I1IIii1II % IIiIiII11i . i1IiiiI1iI
elif IIiii == 7064 :
 NATatozcat ( )
 if 86 - 86: III1iiIii
elif IIiii == 7067 :
 i111I ( OOOiiiiI )
 if 71 - 71: o0ii1I - ooOoO0O00 . oOo0O0Ooo
elif IIiii == 7066 :
 NATatozA ( OOOiiiiI )
 if 15 - 15: ooOoO0O00 % IIiIiII11i / IIiIiII11i - Ii1I - Iii % ooOoO0O00
elif IIiii == 7065 :
 oO0ooo0o0 ( OOOiiiiI )
 if 54 - 54: ooOoO0O00 . oO0o + IiI1i11I + oO0o * ooOoO0O00
elif IIiii == 7070 :
 IIi1i1iI11I11 ( )
 if 13 - 13: I1ii11iIi11i / oO0o + oooOo0oo0oo
elif IIiii == 7071 :
 DIZIlist ( OOOiiiiI )
 if 90 - 90: oO0o * Ii / i1i1I1IIii1II
elif IIiii == 7072 :
 DIZIpull ( OOOiiiiI )
 if 91 - 91: IiI1i11I - OOooOOo / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / I11i
elif IIiii == 7073 :
 WATCHDIZI ( OOOiiiiI )
 if 34 - 34: oO0o * IIiIiII11i + Ii % o0ii1I
elif IIiii == 7002 :
 oO0IiiI1i1i11I1 ( )
 if 25 - 25: OOooOOo + III1iiIii . Ii
elif IIiii == 7003 :
 iiii1iIiI11I ( OOOiiiiI )
 if 87 - 87: oOo0O0Ooo + ii + o0o00Oo0O
elif IIiii == 7004 :
 oOO0O0 ( OOOiiiiI )
 if 32 - 32: o0ii1I / Ii1I . o0ii1I
elif IIiii == 7020 :
 IiIIIIII ( OOOiiiiI )
 if 65 - 65: III1iiIii
elif IIiii == 7001 :
 oOOo0oo0O ( )
 if 74 - 74: I1ii11iIi11i + ooOoO0O00 - IIiIiII11i / i1iIi / IiI1i11I
elif IIiii == 7010 :
 oOO00oOooOo ( OOOiiiiI )
 if 66 - 66: i1iIi / III1iiIii * iI11I1II1I1I
elif IIiii == 7011 :
 iII1i111iIiI1 ( OOOiiiiI )
 if 42 - 42: i1IiiiI1iI - Ii % IIiIiII11i * i1iIi . o0o00Oo0O % Iii
elif IIiii == 7012 :
 iI1IIiIi1i ( OOOiiiiI )
 if 82 - 82: I1ii11iIi11i % o0o00Oo0O + Ii1I % Ii1I
elif IIiii == 7013 :
 cnfTVPlay2 ( OOOiiiiI )
elif IIiii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OOOiiiiI )
elif IIiii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OOOiiiiI )
elif IIiii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IIiii == 7018 :
 iI11 ( )
elif IIiii == 7019 :
 CNF_Studio_Indexer . List_Movies ( OOOiiiiI )
elif IIiii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OOOiiiiI )
elif IIiii == 7024 :
 CNF_Studio_Indexer . Box_Office ( OOOiiiiI )
 if 74 - 74: o0o00Oo0O * III1iiIii . Iii - i1IiiiI1iI + o0o00Oo0O + Iii
elif IIiii == 8000 :
 I1i1I1IIIi1II ( )
elif IIiii == 8001 :
 iII1II ( )
elif IIiii == 8002 :
 IiI11IiIIi ( )
elif IIiii == 8003 :
 iiI11 ( )
elif IIiii == 8004 :
 i1Iii ( )
elif IIiii == 8005 :
 OO0ooo ( )
elif IIiii == 8006 :
 O0OO0 ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 8030 :
 OoOo0O0 ( OOOiiiiI )
elif IIiii == 8045 :
 IIiII1iII11Ii ( OOOiiiiI )
elif IIiii == 8046 :
 oooO00o ( OOOiiiiI )
elif IIiii == 8047 :
 I1Iiii1i1iI ( OOOiiiiI )
elif IIiii == 8048 :
 OO000OOoo ( OOOiiiiI )
elif IIiii == 8049 :
 I11I1I1III1i1 ( OOOiiiiI )
elif IIiii == 804900 :
 I1Ii1iI ( OOOiiiiI )
elif IIiii == 8020 :
 iiIi1IIiI ( )
elif IIiii == 8021 :
 iiiOOoO00o0OO ( OOOiiiiI )
elif IIiii == 8022 :
 IIiiI ( OOOiiiiI )
elif IIiii == 8023 :
 IIi1IIi11 ( OOOiiiiI )
elif IIiii == 8040 :
 ooOO0oO0oo00o ( )
elif IIiii == 8041 :
 I1IIiIIiii ( OOOiiiiI )
elif IIiii == 8042 :
 OOOooooOo0 ( OOOiiiiI )
elif IIiii == 8043 :
 yt . PlayVideo ( OOOiiiiI )
elif IIiii == 8044 :
 o000o00OO00Oo ( OOOiiiiI )
elif IIiii == 8060 :
 ii1ii111 ( )
elif IIiii == 8061 :
 iIi1IIiiiI ( OOOiiiiI )
elif IIiii == 8064 :
 o0O0Oo00 ( )
elif IIiii == 8065 :
 O0OO0OOo00Oo ( OOOiiiiI )
elif IIiii == 8070 :
 o000oOoOOO ( )
elif IIiii == 8071 :
 OOOOOo00o0o ( OOOiiiiI )
elif IIiii == 7080 :
 ooOoOoo ( OOOiiiiI )
elif IIiii == 8090 :
 I1II ( )
elif IIiii == 8091 :
 iiiiiIi1II1i ( OOOiiiiI )
elif IIiii == 8092 :
 i11iIIII1II11Iii ( OOOiiiiI )
elif IIiii == 8093 :
 II1II11I11ii ( OOOiiiiI )
elif IIiii == 8081 :
 o0o0II ( )
elif IIiii == 8062 :
 Oo0oO ( OOOiiiiI )
elif IIiii == 8063 :
 o00o000 ( OOOiiiiI )
elif IIiii == 8050 :
 oo0OoOO000O ( )
elif IIiii == 8051 :
 Oo0o0OoOoOo0 ( OOOiiiiI )
elif IIiii == 8052 :
 I11iiI11I1II ( OOOiiiiI )
elif IIiii == 8085 :
 iIiiII11 ( )
elif IIiii == 8086 :
 i1I1I1 ( OOOiiiiI )
elif IIiii == 8087 :
 iI1111iI1iII ( OOOiiiiI )
elif IIiii == 8088 :
 o0ooo0 ( OOOiiiiI , I11iI1i1I11I11 )
elif IIiii == 9000 :
 oo00o000O ( )
elif IIiii == 1111 :
 OO000o0oOoo0o ( )
elif IIiii == 9001 :
 iII1111III1I ( )
elif IIiii == 9002 :
 iiiI1I1iIIIi1 ( )
elif IIiii == 9003 :
 i1IIi1 ( )
elif IIiii == 9004 :
 World1 ( )
elif IIiii == 9005 :
 World2 ( OOOiiiiI )
elif IIiii == 9006 :
 World3 ( OOOiiiiI )
elif IIiii == 9007 :
 OOo0O ( )
elif IIiii == 9008 :
 O0ooO00 ( OOOiiiiI )
elif IIiii == 9009 :
 IIII1 ( OOOiiiiI )
elif IIiii == 9010 :
 I11IiIi1I ( )
elif IIiii == 9011 :
 OOOoOOoo0OO ( OOOiiiiI )
elif IIiii == 50 :
 iiiiIi111 ( OOOiiiiI )
elif IIiii == 9020 :
 champlist ( )
elif IIiii == 9021 :
 O0ooo00o ( )
elif IIiii == 9022 :
 IIIIi ( )
elif IIiii == 9023 :
 Oo0oo0oOooOoo ( )
elif IIiii == 9024 :
 i111IiI1III1 ( OOOiiiiI )
elif IIiii == 9030 :
 O0OoIIIi111 ( OOOiiiiI )
elif IIiii == 9031 :
 iI1I11II1Iii1 ( OOOiiiiI )
elif IIiii == 9032 :
 O00O0oO ( OOOiiiiI )
elif IIiii == 9033 :
 IIIIi1iII ( OOOiiiiI )
elif IIiii == 9034 :
 O00O0Ooooo00 ( )
elif IIiii == 7085 :
 o0o0o ( OOOiiiiI )
elif IIiii == 7086 :
 OoO00O00 ( OOOiiiiI )
elif IIiii == 7087 :
 IIIiIiIIII1i1 ( iiIii1I )
elif IIiii == 9666 :
 I1II1I11I1I ( OOOiiiiI )
elif IIiii == 10100 : I1ii1i11i ( )
elif IIiii == 101001 : o0O00 ( OOOiiiiI )
elif IIiii == 10105 : o0oo0oo0 ( OOOiiiiI )
elif IIiii == 10106 : IIi1IIOOOoooO0o0o ( OOOiiiiI )
elif IIiii == 10104 : I1IiI11i11iii ( OOOiiiiI )
elif IIiii == 10107 : ii1IiI111II ( )
elif IIiii == 10103 : OOoOoOO00 ( OOOiiiiI )
elif IIiii == 10108 : iii1I ( OOOiiiiI )
elif IIiii == 10000 : Origin_Menu ( )
elif IIiii == 10001 : OoO00oo00 ( )
elif IIiii == 10002 : I1iii11 ( )
elif IIiii == 10003 : ii1Iiii1I ( )
elif IIiii == 10004 : iiiI1i11Ii ( OOOiiiiI )
elif IIiii == 10005 : oo00ooOoo ( )
elif IIiii == 10006 : O0ooO0O00oo0 ( OOOiiiiI )
elif IIiii == 10007 : i1IiIoo0o0ooOoo00O ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 10008 : oOOO00 ( )
elif IIiii == 10009 : oo0OO0Oo000oo ( )
elif IIiii == 10010 : Ooo0 ( OOOiiiiI )
elif IIiii == 10011 : i11Ii ( OOOiiiiI )
elif IIiii == 10012 : ooOoO00 ( OOOiiiiI )
elif IIiii == 10113 : GRABG ( OOOiiiiI , I11iI1i1I11I11 )
elif IIiii == 10109 : OOo0oOOO0 ( OOOiiiiI )
elif IIiii == 10013 : i1IiI1iiIII1 ( OOOiiiiI )
elif IIiii == 10014 : Ii11i1I1 ( )
elif IIiii == 10015 : IIi1IIII ( )
elif IIiii == 10016 : IiIIi1I1I11Ii ( OOOiiiiI )
elif IIiii == 10017 : OOoOO0ooo0O ( )
elif IIiii == 10018 : o0o0O0o0O ( )
elif IIiii == 10019 : IIio0O0 ( )
elif IIiii == 10020 : oo0ooO0O ( )
elif IIiii == 10021 : oOOOoo0 ( )
elif IIiii == 10022 : O0OOO00O0OO0 ( OOOiiiiI )
elif IIiii == 10023 : oooo0OoOo ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 10024 : OO0I11IIi1I1 ( OOOiiiiI )
elif IIiii == 10025 : I111IiiIi1 ( )
elif IIiii == 10026 : I1iiIIii ( )
elif IIiii == 10027 : o00oO0O000 ( )
elif IIiii == 10028 : OO000O000OOO ( )
elif IIiii == 10029 : iIIiIiii1 ( )
elif IIiii == 423 : IIII1iI1IiIiI ( OOOiiiiI )
elif IIiii == 426 : ooIIi111I ( OOOiiiiI )
elif IIiii == 10030 : Izle_Films ( )
elif IIiii == 10031 : Latest_Izle_Movies ( )
elif IIiii == 10032 : Izle_Genres ( )
elif IIiii == 10033 : Izle_Pop_Movies ( )
elif IIiii == 10034 : Izle_Boxsets ( )
elif IIiii == 10035 : Izle_Search ( )
elif IIiii == 10036 : Izle_Genres_Movie ( OOOiiiiI )
elif IIiii == 10037 : Izle_Boxset_single ( OOOiiiiI )
elif IIiii == 10038 : Izle_IFRAME ( )
elif IIiii == 10039 : Izle_Boxsets_Next ( OOOiiiiI )
elif IIiii == 10040 : iIiiiii1i ( )
elif IIiii == 10041 : IIiiiIi1ii11I ( OOOiiiiI )
elif IIiii == 10042 : Oo0OOO00oo0 ( OOOiiiiI )
elif IIiii == 10043 : oooo0O ( )
elif IIiii == 10044 : o0O00o00Ooo ( OOOiiiiI )
elif IIiii == 10045 : ooOoOoOoo ( I11iI1i1I11I11 )
elif IIiii == 10046 : IIiIiI1i11iiII ( OOOiiiiI )
elif IIiii == 10047 : Iii1 ( OOOiiiiI )
elif IIiii == 10048 : ii111 ( OOOiiiiI )
elif IIiii == 10049 : II1i1iii1iiiI ( OOOiiiiI )
elif IIiii == 10050 : I11I1 ( )
elif IIiii == 10051 : o0oO ( )
elif IIiii == 10052 : I1II11iiii ( )
elif IIiii == 10053 : Addon ( OOOiiiiI )
elif IIiii == 10054 : O00o0OoO0OOOo ( OOOiiiiI , I11iI1i1I11I11 )
elif IIiii == 10055 :
 ii1iIi111i1 ( "addFavorite" )
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 ooOOoO0 ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi , i11I , O0o0000o00OO0 )
elif IIiii == 10056 :
 ii1iIi111i1 ( "rmFavorite" )
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oooo ( I11iI1i1I11I11 )
elif IIiii == 10057 :
 ii1iIi111i1 ( "getFavorites" )
 i1II1I1I1 ( )
elif IIiii == 10058 : IiiIiI1IIi1IIIii ( )
elif IIiii == 10059 : Donators_Guide ( )
elif IIiii == 10060 : ooO ( )
elif IIiii == 10061 : II1i ( )
elif IIiii == 10062 : O000Oo00 ( I11iI1i1I11I11 , OOOiiiiI , iiIii1I )
elif IIiii == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif IIiii == 10064 : i1iI1Ii11Ii1 ( )
elif IIiii == 10065 : ooO000OO ( OOOiiiiI )
elif IIiii == 10066 : I1II1IiI1 ( OOOiiiiI )
elif IIiii == 10068 : O0Oo00OoOo ( OOOiiiiI )
elif IIiii == 10069 : O0Oo0o000oO ( OOOiiiiI )
elif IIiii == 10070 : iiIiII ( OOOiiiiI )
elif IIiii == 10071 : Genie_Watch ( )
elif IIiii == 10072 : Oooooooo00o00 ( )
elif IIiii == 10073 : I1iOO0O0O ( OOOiiiiI )
elif IIiii == 10074 : OO0oo00oOO ( OOOiiiiI )
elif IIiii == 10075 : II1iII1i1i ( Ii1IIiiIIi , I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 10076 : ooo0o0 ( OOOiiiiI )
elif IIiii == 10077 : oOIiiIIi ( OOOiiiiI )
elif IIiii == 10078 : o0oOo0OO ( )
elif IIiii == 10079 : Genie_Watch_Tv_Shows ( )
elif IIiii == 10080 : Genie_Watch_Tv_Genre ( OOOiiiiI )
elif IIiii == 10081 : Genie_Watch_TV_PlayRun ( OOOiiiiI )
elif IIiii == 10082 : Genie_Watch_TV_Episodes ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 10083 : Genie_Watch_Tv_Recent ( OOOiiiiI )
elif IIiii == 10084 : IIi11IIiIii1 ( )
elif IIiii == 10085 : oo0OOo0 ( )
elif IIiii == 10086 : O0 ( )
elif IIiii == 20000 : Oo0Oo0O ( )
elif IIiii == 20001 : O0ooO0o ( OOOiiiiI )
elif IIiii == 20002 : OO0iii111 ( OOOiiiiI )
elif IIiii == 20003 : O0oooOo0000o0 ( OOOiiiiI )
elif IIiii == 20004 : oOo0ooO0O0oo ( OOOiiiiI )
elif IIiii == 20005 : I1Io0Oo00 ( OOOiiiiI )
elif IIiii == 21004 : iii1IIIiiiI ( )
elif IIiii == 21005 : I1Ii1iI1IiI1I ( OOOiiiiI )
elif IIiii == 21006 : o0OOOoO ( OOOiiiiI )
elif IIiii == 21007 : iiII1i1i1I1 ( OOOiiiiI )
elif IIiii == 21008 : II11Iiii ( OOOiiiiI )
elif IIiii == 21009 : ooooooo00o ( OOOiiiiI )
elif IIiii == 30000 : o00oOo0OoO0oO ( )
elif IIiii == 30001 : I1II1iIi ( )
elif IIiii == 100121 : Resolve ( OOOiiiiI )
elif IIiii == 30003 : OOOo0Ooo0o00o ( )
elif IIiii == 30004 : IiO0o ( OOOiiiiI )
elif IIiii == 30005 : iII1oOOo ( OOOiiiiI )
elif IIiii == 30006 : oooOo0OO ( )
elif IIiii == 30007 : O0000ooO0OO0Oooo0o ( )
elif IIiii == 30008 : oo0 ( OOOiiiiI )
elif IIiii == 30009 : oo0OoO ( OOOiiiiI )
elif IIiii == 30010 : o0000OOOo ( OOOiiiiI )
elif IIiii == 30011 : oOO000000oO0 ( )
elif IIiii == 30012 : OOo0Oo0O00O ( )
elif IIiii == 30013 : O00O000oOO0oO ( )
elif IIiii == 30014 : IIIII1IIiIi ( )
elif IIiii == 30015 : oO0OO00 ( OOOiiiiI , Ii1IIiiIIi , i11I )
elif IIiii == 30016 : iiIi ( OOOiiiiI )
elif IIiii == 30019 : O0oIii11IiiIi ( OOOiiiiI )
elif IIiii == 30017 : Ii1o0OOOoo0000 ( OOOiiiiI )
elif IIiii == 30018 : IiIIIii1i1iI ( OOOiiiiI )
elif IIiii == 30030 : iiII1iIi1ii1i ( )
elif IIiii == 30031 : iIiiII1Ii1ii ( )
elif IIiii == 30032 : iII1iii ( )
elif IIiii == 30033 : Oooooo0O00o ( )
elif IIiii == 30034 : i11IiI1 ( )
elif IIiii == 30035 : o0oOo ( OOOiiiiI )
elif IIiii == 30036 : O0OoOo0oO0o ( OOOiiiiI )
elif IIiii == 30037 : I11iIi1i1IIi ( OOOiiiiI )
elif IIiii == 30038 : o00iIIiIi111iI ( )
elif IIiii == 30039 : oOOo0O00o ( )
elif IIiii == 50000 : i1II1 ( )
elif IIiii == 50001 : iioo ( )
elif IIiii == 50002 : i11iII11I1III ( OOOiiiiI )
elif IIiii == 50003 : Table_Menu ( iiIii1I )
elif IIiii == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif IIiii == 60001 : IiiIiiIIII ( )
elif IIiii == 60002 : i111I1 ( I11iI1i1I11I11 )
elif IIiii == 60003 : iIiI1I1 ( OOOiiiiI )
elif IIiii == 600033 : i1Oo ( OOOiiiiI )
elif IIiii == 60004 : oO00oOoo00o0 ( OOOiiiiI )
elif IIiii == 50004 : iIIi ( )
elif IIiii == 50005 : speedtest . runtest ( OOOiiiiI )
elif IIiii == 70001 : iIIi11 ( )
elif IIiii == 70002 : o0o0I11 ( OOOiiiiI )
elif IIiii == 70003 : i1iiiiIIIi ( OOOiiiiI )
elif IIiii == 70004 : Ii11Ii1 ( OOOiiiiI )
elif IIiii == 70005 : III ( OOOiiiiI )
elif IIiii == 70006 : O0oo0OOO0O0 ( )
elif IIiii == 50006 : o0OIiII ( i1 , i1111 )
elif IIiii == 80000 : IIIIiII ( )
elif IIiii == 80001 : resolvefilmon ( OOOiiiiI )
elif IIiii == 80002 : IIIIi1Iii1iIi ( )
elif IIiii == 80003 : OOooo00oo ( I11iI1i1I11I11 , OOOiiiiI , "None" )
elif IIiii == 80004 : II11I ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 80005 : O00oO0 ( )
elif IIiii == 80006 : OOOO00OoooO ( OOOiiiiI )
elif IIiii == 80007 : IIIi ( OOOiiiiI )
elif IIiii == 80008 : Ii1iiI1 ( )
elif IIiii == 80009 : IIiii1I ( )
elif IIiii == 80010 : O0O000 ( OOOiiiiI )
elif IIiii == 80011 : O0ooOo ( OOOiiiiI )
elif IIiii == 80012 : iiIIi ( )
elif IIiii == 90000 : o0Oo0OOOOoo ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 90001 : tools ( )
elif IIiii == 90002 : O0ooo0 ( )
elif IIiii == 90003 : i11iI1I1 ( OOOiiiiI )
elif IIiii == 90004 : oooo00o00oO ( OOOiiiiI )
elif IIiii == 90005 : iIii11iI1Iii1iI ( OOOiiiiI )
elif IIiii == 90006 : o0ooO00o00 ( OOOiiiiI )
elif IIiii == 90007 : iI111II ( OOOiiiiI )
elif IIiii == 90008 : o00ooO0 ( OOOiiiiI )
elif IIiii == 90009 : I1i1ii1IiI1i ( OOOiiiiI )
elif IIiii == 90010 : OOoooO00o0oo0 ( )
elif IIiii == 90020 : oO0o00O ( )
elif IIiii == 90021 : hellyeah2 ( OOOiiiiI )
elif IIiii == 90022 : hellyeah3 ( OOOiiiiI )
elif IIiii == 90023 : Oo0Oo00o00oO ( )
elif IIiii == 90024 : OOoO00ooO ( OOOiiiiI )
elif IIiii == 90025 : o0IiiiI111I ( OOOiiiiI )
if 48 - 48: i1i1I1IIii1II . I11i - oooOo0oo0oo
elif IIiii == 90026 : iiOo0 ( )
elif IIiii == 90027 : II1iiI ( I11iI1i1I11I11 , OOOiiiiI , iiIii1I )
elif IIiii == 90028 : ooOO00Oo ( OOOiiiiI )
if 29 - 29: I1ii11iIi11i - o0ii1I - I1ii11iIi11i
elif IIiii == 900300 : o0OOOOooo ( )
elif IIiii == 900301 : OooO0OO ( OOOiiiiI )
elif IIiii == 900302 : I1i11 ( OOOiiiiI )
elif IIiii == 90030 : OOo ( )
elif IIiii == 90031 : ooo0OO0O0Oo ( )
elif IIiii == 90032 : Ooo0O0oooo ( OOOiiiiI )
elif IIiii == 90033 : iiI ( OOOiiiiI )
elif IIiii == 90034 : o000oo ( OOOiiiiI )
elif IIiii == 90035 : o00o0 ( OOOiiiiI )
elif IIiii == 90036 : Ii1IIIi ( OOOiiiiI )
elif IIiii == 90039 : Oo00ooOOO ( OOOiiiiI )
elif IIiii == 90037 : I1iI ( OOOiiiiI )
elif IIiii == 900377 : ooO0oo0o0 ( OOOiiiiI )
elif IIiii == 90038 : i1i1ii1111i1i ( )
if 89 - 89: I1ii11iIi11i . oO0o . Ii1I * i1i1I1IIii1II . o0o00Oo0O
elif IIiii == 10090 : IiiI1iiiiI1iI ( )
elif IIiii == 10091 : iiiii1i1 ( OOOiiiiI )
elif IIiii == 10092 : OOO0oOo00o0 ( OOOiiiiI )
elif IIiii == 10093 : iiII1iiI ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 10094 : IiIii1iIIII ( OOOiiiiI , Ii1IIiiIIi )
if 72 - 72: Ii % Iii / i1IiiiI1iI + oOo0O0Ooo * IiI1i11I
elif IIiii == 10095 : i1oO0OO0 ( )
elif IIiii == 10096 : OOOO0oOo00O ( OOOiiiiI )
elif IIiii == 10097 : o0Oii111 ( OOOiiiiI )
elif IIiii == 10098 : I1IiI1iIiIiii ( OOOiiiiI )
elif IIiii == 10099 : iii1 ( OOOiiiiI )
if 69 - 69: i1IiiiI1iI + o0o00Oo0O . III1iiIii . I11i
elif IIiii == 10200 : ii11i ( )
elif IIiii == 10201 : I1I1I11Ii ( OOOiiiiI )
elif IIiii == 10202 : iI1II1I1I ( OOOiiiiI )
elif IIiii == 10203 : RT4 ( OOOiiiiI )
if 38 - 38: III1iiIii / ooOoO0O00
elif IIiii == 90040 : OO0OOOOo0000O ( )
elif IIiii == 90041 : i111I11I ( OOOiiiiI )
elif IIiii == 90042 : I1iI11I ( OOOiiiiI )
elif IIiii == 90043 : iiiiiI ( OOOiiiiI )
elif IIiii == 90044 : IiI1iIiIi1 ( OOOiiiiI )
elif IIiii == 90045 : O0oooOoO ( )
elif IIiii == 90046 : III1IiI1i1i ( OOOiiiiI )
elif IIiii == 90050 : OOO0O00Oo ( )
elif IIiii == 90051 : O0OO0ooO00 ( OOOiiiiI )
elif IIiii == 90052 : IIiI1I ( OOOiiiiI )
elif IIiii == 90053 : iIII11Iiii1 ( OOOiiiiI )
elif IIiii == 90054 : o0OoO0OOoO0Oo0 ( OOOiiiiI )
elif IIiii == 90055 : i11i1i ( )
if 60 - 60: OOooOOo
elif IIiii == 100001 : Stand_up ( )
if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
elif IIiii == 100003 : IiIIi1I1I11Ii ( OOOiiiiI )
elif IIiii == 100004 : i11iIIi11 ( OOOiiiiI )
elif IIiii == 100005 : Resolve ( OOOiiiiI )
elif IIiii == 100008 : Search ( )
elif IIiii == 100007 : iiI1II11II1i ( OOOiiiiI )
elif IIiii == 100009 : yt . PlayVideo ( OOOiiiiI )
elif IIiii == 100010 : IiIi1 ( OOOiiiiI )
elif IIiii == 100100 : OOoOOo0O00O ( Ii1IIiiIIi , OOOiiiiI , oOooooO0o0OOO )
elif IIiii == 100101 : IIi1II ( OOOiiiiI , I11iI1i1I11I11 , i11I , oOooooO0o0OOO , Ii1IIiiIIi )
elif IIiii == 100102 : i111IIIiI ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi , i11I )
elif IIiii == 100106 : iIi ( OOOiiiiI , I11iI1i1I11I11 )
elif IIiii == 100107 : i1oO ( )
elif IIiii == 100108 : OooOo0o0Oo0 ( )
elif IIiii == 100109 : iIiIII1Ii ( OOOiiiiI )
elif IIiii == 40000 : i1i1Ii1IiIII ( )
elif IIiii == 40001 : I1iii1 ( OOOiiiiI )
elif IIiii == 100110 : OO00oo ( OOOiiiiI )
elif IIiii == 100111 : IiII1i1iI ( OOOiiiiI )
elif IIiii == 100112 : i11i ( OOOiiiiI )
elif IIiii == 100113 : i1I1Ii11i ( OOOiiiiI )
elif IIiii == 100114 : O0Oo0O0 ( OOOiiiiI )
elif IIiii == 100115 : ooOOo0o ( OOOiiiiI )
elif IIiii == 100117 : I1IiiIiii1 ( OOOiiiiI )
elif IIiii == 100118 : iIiiiIiIi ( OOOiiiiI )
elif IIiii == 100120 : IiI1Iii1 ( OOOiiiiI )
elif IIiii == 1001200 : Ooooo ( OOOiiiiI )
elif IIiii == 100210 : o0OOoOoO00 ( OOOiiiiI )
elif IIiii == 100211 : OoO0o00OOOOO ( )
elif IIiii == 100212 : IiI1i111i ( )
elif IIiii == 100213 : ooo00o0o ( )
elif IIiii == 100214 : IiiiI1 ( )
elif IIiii == 1000111 :
 I1I1i111 ( OOOiiiiI )
 if 61 - 61: III1iiIii . III1iiIii
elif IIiii == 1001111 :
 I111IIiii1Ii ( I11iI1i1I11I11 , OOOiiiiI )
 if 17 - 17: OOooOOo % I1ii11iIi11i / i1IiiiI1iI . o0ii1I % oO0o
elif IIiii == 1002111 :
 ooooOo ( )
 if 32 - 32: oOo0O0Ooo + i1iIi / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
elif IIiii == 1003111 :
 OO0oOooOoOO0 ( OOOiiiiI , I11iI1i1I11I11 )
 if 95 - 95: IiI1i11I / i1iIi + i1IiiiI1iI
elif IIiii == 1004111 :
 oOo0O0O0oOo ( )
 if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - III1iiIii
elif IIiii == 1005111 :
 O0o000O0Oo0 ( OOOiiiiI , I11iI1i1I11I11 )
elif IIiii == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( OOOiiiiI , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( I11iI1i1I11I11 , OOOiiiiI , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( I11iI1i1I11I11 , OOOiiiiI , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1105000 :
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi , i11I , O0o0000o00OO0 )
elif IIiii == 1106000 :
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I11iI1i1I11I11 = I11iI1i1I11I11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( I11iI1i1I11I11 )
elif IIiii == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( OOOiiiiI )
elif IIiii == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( I11iI1i1I11I11 )
elif IIiii == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif IIiii == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( OOOiiiiI )
elif IIiii == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in OOOiiiiI :
  import urlresolver
  II1III1I1I1Ii = urlresolver . resolve ( OOOiiiiI )
  OOOOoO00o0O = xbmcgui . ListItem ( path = II1III1I1I1Ii )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoO00o0O )
 elif not OOOiiiiI . startswith ( "plugin://plugin" ) or not any ( x in OOOiiiiI for x in pyramid . g_ignoreSetResolved ) :
  OOOOoO00o0O = xbmcgui . ListItem ( path = OOOiiiiI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOOoO00o0O )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + OOOiiiiI + ')' )
elif IIiii == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( I11iI1i1I11I11 , playlist )
elif IIiii == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OOOiiiiI , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1117000 :
 OOOiiiiI , oo00oo00 = getRegexParsed ( regexs , OOOiiiiI )
 if OOOiiiiI :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( OOOiiiiI , I11iI1i1I11I11 , Ii1IIiiIIi , oo00oo00 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif IIiii == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 I1iI1iI1iiI1 = youtubedl . single_YD ( OOOiiiiI )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( I1iI1iI1iiI1 , I11iI1i1I11I11 , Ii1IIiiIIi )
elif IIiii == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( OOOiiiiI ) , I11iI1i1I11I11 , Ii1IIiiIIi , True )
elif IIiii == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , I11iI1i1I11I11 , 'video' )
elif IIiii == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OOOiiiiI , I11iI1i1I11I11 , 'video' )
elif IIiii == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OOOiiiiI , I11iI1i1I11I11 , 'audio' )
elif IIiii == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1126000 :
 I11iI1i1I11I11 = I11iI1i1I11I11 . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( OOOiiiiI , search_term = I11iI1i1I11I11 [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( OOOiiiiI )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif IIiii == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif IIiii == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif IIiii == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi , i11I )
elif IIiii == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( OOOiiiiI , Ii1IIiiIIi , i11I ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( I11iI1i1I11I11 , OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( OOOiiiiI )
elif IIiii == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif IIiii == 9050000 : oOO ( )
elif IIiii == 9060000 : I111IIiii1Ii ( I11iI1i1I11I11 , OOOiiiiI )
elif IIiii == 9080000 : Ii1iI11iI1 ( )
elif IIiii == 9070000 : OOoiIIiiIIIi1I ( )
elif IIiii == 9090000 : iIIIII1iiiiII ( )
elif IIiii == 9100000 : O0o0O0OO00o ( )
elif IIiii == 9110000 : O0Oo ( )
elif IIiii == 9999999 : OooOoooo0000 ( )
elif IIiii == 19999999 : OO0ooOoOO0OOo ( )
elif IIiii == 1999990 : I11iiIIiI1ii ( )
elif IIiii == 21999990 : OOOoOo ( )
elif IIiii == 21999991 : O00o0 ( OOOiiiiI )
elif IIiii == 21999992 : o000O0O ( OOOiiiiI )
elif IIiii == 21999993 : I1i1i1iii ( OOOiiiiI )
elif IIiii == 21999994 : I1111i ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 21999995 : iIIii ( OOOiiiiI )
elif IIiii == 21999996 : ii1iii1i ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 21999997 : Iii1I1111ii ( OOOiiiiI , Ii1IIiiIIi )
elif IIiii == 21999998 : Ii1IIiI1io0O00Oo0 ( I11iI1i1I11I11 , OOOiiiiI , Ii1IIiiIIi )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
