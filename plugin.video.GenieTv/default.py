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
def OOOoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00o0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , I11iII , iIIII , I11iI1i1I11I11 , o000O0O in O00o0 :
  Ii1I1i ( o000O0O , url , 21009 , I11iII , I11iI1i1I11I11 , iIIII )
  if 18 - 18: IiI1i11I - oooOo0oo0oo . i1IiiiI1iI . iI11I1II1I1I
def i1I ( url ) :
 url = url
 O0ooooOOoo0O = OO ( )
 if O0ooooOOoo0O ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif O0ooooOOoo0O ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 36 - 36: i1i1I1IIii1II % i1i1I1IIii1II % ooOoO0O00 / ooOoO0O00 - i1iIi
  if 30 - 30: Iii / oOo0O0Ooo
def Iii1I1111ii ( ) :
 OOOiiiiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( OOOiiiiI , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 i111iIi1i1II1 ( OOOiiiiI )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooO ( )
def i1I1i111Ii ( ) :
 ooo = i1i1iI1iiiI ( )
 Ooo0oOooo0 = ooo . replace ( II11iiii1Ii , "" )
 if os . path . exists ( ooo ) or not ooo == False :
  oOOOoo00 = open ( ooo , mode = 'r' ) ; iiIiIIIiiI = oOOOoo00 . read ( ) ; oOOOoo00 . close ( )
  o0OIiII ( "%s - %s" % ( i1 , Ooo0oOooo0 ) , iiIiIIIiiI )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def Iii1I1111ii ( ) :
 OOOiiiiI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( OOOiiiiI , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 i111iIi1i1II1 ( OOOiiiiI )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooO ( )
def iiI1IIIi ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 47 - 47: I1ii11iIi11i % Iii % Ii - o0o00Oo0O + i1iIi
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 94 - 94: i1IiiiI1iI
def i11II1I11I1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def OOoOO0ooo ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 II1iIi11 = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I11iiii = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , I11iII , o000O0O in II1iIi11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 900302 , I11iII , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for O0i1iI in I11iiii :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , O0i1iI , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def IiI1iiiIii ( url ) :
 I1III1111iIi = OooOoooOo ( url )
 II1iIi11 = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( I1III1111iIi )
 I1i111I = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( I1III1111iIi )
 for url , o000O0O in II1iIi11 :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , o000O0O in I1i111I :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def OooOo0oo0O0o00O ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for IiIi1I1 , IiIIi1 in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + IiIi1I1 , IiIIi1 )
def IIIIiii1IIii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def II1i11I ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( I1i11 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O , I11iII in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , I11iII , Oo00OOOOO , '' )
 for url in next :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def ii1I1IIii11 ( url ) :
 I1i11 = OooOoooOo ( url )
 O0o0oO = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 IIIIiIiIi1 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for o000O0O , url in i1Iii1i1I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for o000O0O , url in IIIIiIiIi1 :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in O0o0oO :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 2 - 2: IiI1i11I % iI11I1II1I1I * iI11I1II1I1I . I11i / IiI1i11I
def iII1i1 ( url ) :
 if 'drive' in url :
  O0oOOoooOO0O ( url )
 else :
  I1i11 = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( I1i11 )
  for url in IIi :
   O0oOOoooOO0O ( url )
def ooo00Ooo ( url ) :
 Oo0o0O00 = liveresolver . resolve ( url )
 ii1 = xbmcgui . ListItem ( path = Oo0o0O00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
def I1i11OO ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 o0O0oo0OO0O = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0O0oo0OO0O )
def i1i1iI1iiiI ( ) :
 OO0 = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  OO0 = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  OO0 = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  OO0 = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  OO0 = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return OO0
 if 72 - 72: ii
def OooooOoooO ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , oOIIiIi :
  return oOIIiIi
 return True
def OOoOooOoOOOoo ( ) :
 if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * i1i1I1IIii1II
 if 81 - 81: IiI1i11I + III1iiIii
 if 98 - 98: oOo0O0Ooo
 if 95 - 95: i1iIi / i1iIi
 if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def O0O0Oo00 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   oOoO00o ( )
  if O0O0ooOOO == 1 :
   oO00O0 ( )
  if O0O0ooOOO == 2 :
   IIi1IIIi ( O00Ooo )
  if O0O0ooOOO == 3 :
   OOOO0OOO ( OOOiiiiI )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 3 - 3: oO0o
def oooOoOOO0oo0o ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
  if 96 - 96: ii + i1i1I1IIii1II
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
  if 44 - 44: i1i1I1IIii1II
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: OOooOOo / IIiIiII11i
 else :
  if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
  if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
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
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
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
   if 59 - 59: oOo0O0Ooo * IIiIiII11i . o0o00Oo0O
   if 56 - 56: o0ii1I - IiI1i11I % oOo0O0Ooo - I11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def Oo00O ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  iI111i1II ( )
 if O0O0ooOOO == 1 :
  O0ooooo0OOOO0 ( )
 if O0O0ooOOO == 2 :
  IiiIi1III ( )
 if O0O0ooOOO == 3 :
  O0Oo ( )
 if O0O0ooOOO == 4 :
  ii11i11i1 ( )
 if O0O0ooOOO == 5 :
  Ooo0o00o0o ( )
  if 7 - 7: o0o00Oo0O - I1ii11iIi11i + Ii1I + IIiIiII11i + iI11I1II1I1I
  if 58 - 58: I11i / III1iiIii . OOooOOo / ii + i1IiiiI1iI
def O0OoO0ooOO0o ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   OoOo0oOooOoOO ( )
  if O0O0ooOOO == 1 :
   oo00ooOoO00 ( )
  if O0O0ooOOO == 2 :
   o00oOoOo0 ( OOOiiiiI )
  if O0O0ooOOO == 3 :
   o0O0O0ooo0oOO ( )
  if O0O0ooOOO == 4 :
   oo000ii ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0O0ooOOO == 5 :
   OoO ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . oooOo0oo0oo
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def O0iII1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 27 - 27: oO0o . Iii + OOooOOo / iI11I1II1I1I % IiI1i11I . i1iIi
 if 14 - 14: i1i1I1IIii1II + Ii1I - IiI1i11I / o0o00Oo0O . i1IiiiI1iI
 if 45 - 45: i1IiiiI1iI
 if 83 - 83: OOooOOo . ii
 if 58 - 58: Ii + ii % ii / III1iiIii / Ii
def oOOoo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   iII1111III1I ( )
  if O0O0ooOOO == 1 :
   ii11i ( )
  if O0O0ooOOO == 2 :
   O00oOo00o0o ( )
  if O0O0ooOOO == 3 :
   O00oO0 ( )
  if O0O0ooOOO == 4 :
   O0Oo00OoOo ( )
  if O0O0ooOOO == 5 :
   ii1ii111 ( )
  if O0O0ooOOO == 6 :
   i11111I1I ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 11 - 11: ii . i1IiiiI1iI
  if 80 - 80: ii - oooOo0oo0oo * o0ii1I * Ii1I / oOo0O0Ooo / oooOo0oo0oo
  if 13 - 13: i1IiiiI1iI * i1iIi + Ii * i1IiiiI1iI - i1iIi
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def Ii1i1i1i1I1Ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiiI1 = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 97 - 97: I1ii11iIi11i + iI11I1II1I1I - III1iiIii + oooOo0oo0oo - o0o00Oo0O . IiI1i11I
   if 30 - 30: o0o00Oo0O * ii
   if 38 - 38: III1iiIii - Ii1I . OOooOOo - i1IiiiI1iI . ii
   if 89 - 89: iI11I1II1I1I
  iiio00oOOooOOo0o = [ iiiI1 , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   i11iiiiI1i ( )
  if O0O0ooOOO == 1 :
   iIIii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , i1iIiIi1I , o000O0O )
  if O0O0ooOOO == 2 :
   iiii11i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0O0ooOOO == 3 :
   iIIii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , i1iIiIi1I , o000O0O )
 else :
  if 35 - 35: Ii1I * IiI1i11I - oO0o % I11i
  if 87 - 87: OOooOOo * i1IiiiI1iI . Iii
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 51 - 51: oooOo0oo0oo % iI11I1II1I1I - ii % i1iIi * iI11I1II1I1I % oO0o
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 40 - 40: OOooOOo / III1iiIii
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
  if 15 - 15: Ii % oOo0O0Ooo * Iii / i1IiiiI1iI
  if 90 - 90: IiI1i11I
  if 31 - 31: oooOo0oo0oo + o0o00Oo0O
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 87 - 87: i1iIi
def IIIii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def iiii11i ( url ) :
 I1i11 = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 IIIIiIiIi1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 for o000O0O , I11iII , url in IIi :
  if '247ch' in url :
   IiI11i1IIiiI ( o000O0O , url , 10190 , I11iII )
  elif '.m3u' in url :
   IiI11i1IIiiI ( o000O0O , url , 1019 , I11iII )
  elif '.xml' in url :
   IiI11i1IIiiI ( o000O0O , url , 1018 , I11iII )
  else :
   oOOo000oOoO0 ( o000O0O , url , 222 , I11iII )
 for o000O0O , url , I11iII in i1Iii1i1I :
  if '.xml' in url :
   IiI11i1IIiiI ( o000O0O , url , 1018 , I11iII )
  elif '.m3u' in url :
   IiI11i1IIiiI ( o000O0O , url , 1019 , I11iII )
  else :
   oOOo000oOoO0 ( o000O0O , url , 222 , I11iII )
 for o000O0O , url , I11iII in IIIIiIiIi1 :
  oOOo000oOoO0 ( o000O0O , url , 8043 , I11iII )
def OoOo00o0OO ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def iI1IIIii ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url , I11iII in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , I11iII )
  if 7 - 7: III1iiIii - Iii / IIiIiII11i * o0ii1I . IiI1i11I * IiI1i11I
def O0O0oOOo0O ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 19 - 19: I11i / i1IiiiI1iI % I11i % IiI1i11I * III1iiIii
def ii1oOoO0o0ooo ( url ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for o000O0O , url , i1Ii11II , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII in IIi :
  if IioO0oOOO0Ooo == '123' :
   IioO0oOOO0Ooo = iiIi1IIiIi + 'appstreams.png'
  if I11iI1i1I11I11 == '123' :
   I11iI1i1I11I11 = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( o000O0O , url , 100010 , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII )
  elif 'playlist' in url :
   I1I1II1I11 ( o000O0O , url , 100007 , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII )
  elif 'watchseries' in url :
   I1I1II1I11 ( o000O0O , url , 100100 , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII )
  elif not 'http' in url :
   i1i1I ( o000O0O , url , 100009 , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII , '' )
  else :
   i1i1I ( o000O0O , url , 100005 , IioO0oOOO0Ooo , I11iI1i1I11I11 , iIIII , '' )
   if 25 - 25: iI11I1II1I1I + Ii1I + IiI1i11I / IIiIiII11i / Iii
def o0O0Oo00Oo0o ( url ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 O00o0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , I11iII , iIIII , I11iI1i1I11I11 , o000O0O in O00o0 :
  if I11iII == '123' :
   I11iII = iiIi1IIiIi + 'appstreams.png'
  if I11iI1i1I11I11 == '123' :
   I11iI1i1I11I11 = Oo00OOOOO
  if 'php' in url :
   I1I1II1I11 ( o000O0O , url , 100004 , I11iII , I11iI1i1I11I11 , iIIII )
  elif 'playlist' in url :
   I1I1II1I11 ( o000O0O , url , 100007 , I11iII , I11iI1i1I11I11 , iIIII )
  elif 'watchseries' in url :
   I1I1II1I11 ( o000O0O , url , 100100 , I11iII , I11iI1i1I11I11 , iIIII )
  elif not 'http' in url :
   i1i1I ( o000O0O , url , 100009 , I11iII , I11iI1i1I11I11 , iIIII , '' )
  else :
   i1i1I ( o000O0O , url , 100005 , I11iII , I11iI1i1I11I11 , iIIII , '' )
   if 74 - 74: I1ii11iIi11i / Ii - IIiIiII11i * I11i
def IIi1IIIIi ( url ) :
 if 70 - 70: oooOo0oo0oo / IIiIiII11i - iI11I1II1I1I - IiI1i11I
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IiiiIi1i = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in IiiiIi1i :
  IioO0oOOO0Ooo = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
   IioO0oOOO0Ooo = IioO0oOOO0Ooo
  o000O0O = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for o000O0O in o000O0O :
   if 'elete' in o000O0O :
    pass
   elif 'rivate Vid' in o000O0O :
    pass
   else :
    o000O0O = ( o000O0O ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  i1ii = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O00OooOo00o ) )
  for i1ii in i1ii :
   i1ii = i1ii
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for url in url :
   url = url
  i1i1I ( '[COLORred]' + str ( i1ii ) + '[/COLOR] : ' + str ( o000O0O ) , str ( url ) , 100009 , str ( IioO0oOOO0Ooo ) , Oo00OOOOO , '' , '' )
  Ii1IIiI1i ( 'movies' , '' )
  if 68 - 68: oooOo0oo0oo * o0o00Oo0O . Iii - IIiIiII11i . i1iIi / IIiIiII11i
def iii1 ( ) :
 I1i ( 'Featured 24/7' , '' , 9070000 , iiIi1IIiIi + 'arconai/feat.png' , Oo00OOOOO , '' , '' )
 I1i ( '24/7 Tv Thows' , '' , 9080000 , iiIi1IIiIi + 'arconai/247shows.png' , Oo00OOOOO , '' , '' )
 I1i ( '24/7 Movies' , '' , 9090000 , iiIi1IIiIi + 'arconai/247movies.png' , Oo00OOOOO , '' , '' )
 I1i ( '24/7 Cable' , '' , 9100000 , iiIi1IIiIi + 'arconai/247cable.png' , Oo00OOOOO , '' , '' )
 I1i ( '24/7 Random Stream' , '' , 9110000 , iiIi1IIiIi + 'arconai/random.png' , Oo00OOOOO , '' , '' )
 if 86 - 86: I1ii11iIi11i / i1i1I1IIii1II + o0o00Oo0O * IiI1i11I
def iiI11I1i1i1iI ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 OoOOo000o0 = 'index.php#shows'
 I1i11 = BeautifulSoup ( requests . get ( OOOiiiiI + OoOOo000o0 ) . content )
 iiI1II11II1i = I1i11 . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for o0O0O0 in iiI1II11II1i :
  I11oo0ooOO = o0O0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in I11oo0ooOO :
   iI1IiIIiIIi = iiI111I1iIiI . text
  IiIi11Iii = o0O0O0 . findAll ( 'a' )
  for iiI111I1iIiI in IiIi11Iii :
   if iiI111I1iIiI . has_key ( 'href' ) :
    III1i1iI1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   o000O0O = iiI111I1iIiI [ 'title' ]
   o0ooo00o = BeautifulSoup ( requests . get ( III1i1iI1 ) . content )
   oOO00oO00O0OO = o0ooo00o . findAll ( 'source' )
   for oOo00OO in oOO00oO00O0OO :
    o0oOO0OO = oOo00OO [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    i1i1I ( o000O0O , o0oOO0OO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 98 - 98: IIiIiII11i % i1iIi * iI11I1II1I1I + Iii + IIiIiII11i % Iii
    if 87 - 87: i1i1I1IIii1II * i1i1I1IIii1II / oOo0O0Ooo / i1iIi % oooOo0oo0oo
def OooOOO0O00 ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 OoOOo000o0 = 'index.php#movies'
 I1i11 = BeautifulSoup ( requests . get ( OOOiiiiI + OoOOo000o0 ) . content )
 iiI1II11II1i = I1i11 . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for o0O0O0 in iiI1II11II1i :
  I11oo0ooOO = o0O0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in I11oo0ooOO :
   iI1IiIIiIIi = iiI111I1iIiI . text
  IiIi11Iii = o0O0O0 . findAll ( 'a' )
  for iiI111I1iIiI in IiIi11Iii :
   if iiI111I1iIiI . has_key ( 'href' ) :
    III1i1iI1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   o000O0O = iiI111I1iIiI [ 'title' ]
   o0ooo00o = BeautifulSoup ( requests . get ( III1i1iI1 ) . content )
   oOO00oO00O0OO = o0ooo00o . findAll ( 'source' )
   for oOo00OO in oOO00oO00O0OO :
    o0oOO0OO = oOo00OO [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    i1i1I ( o000O0O , o0oOO0OO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 29 - 29: I11i % iI11I1II1I1I . ii % ii % IIiIiII11i / IiI1i11I
    if 70 - 70: Ii % IiI1i11I
def I11Ii11iI1 ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 OoOOo000o0 = 'index.php#cable'
 I1i11 = BeautifulSoup ( requests . get ( OOOiiiiI + OoOOo000o0 ) . content )
 iiI1II11II1i = I1i11 . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for o0O0O0 in iiI1II11II1i :
  I11oo0ooOO = o0O0O0 . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for iiI111I1iIiI in I11oo0ooOO :
   iI1IiIIiIIi = iiI111I1iIiI . text
  IiIi11Iii = o0O0O0 . findAll ( 'a' )
  for iiI111I1iIiI in IiIi11Iii :
   if iiI111I1iIiI . has_key ( 'href' ) :
    III1i1iI1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   o000O0O = iiI111I1iIiI [ 'title' ]
   o0ooo00o = BeautifulSoup ( requests . get ( III1i1iI1 ) . content )
   oOO00oO00O0OO = o0ooo00o . findAll ( 'source' )
   for oOo00OO in oOO00oO00O0OO :
    o0oOO0OO = oOo00OO [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    i1i1I ( o000O0O , o0oOO0OO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
    if 39 - 39: oOo0O0Ooo * Ii - i1i1I1IIii1II / III1iiIii % i1IiiiI1iI % Iii
def OO00oo0o ( ) :
 o0ooo00o = BeautifulSoup ( requests . get ( 'http://arconaitv.me/stream.php?id=random' ) . content )
 oOO00oO00O0OO = o0ooo00o . findAll ( 'source' )
 for oOo00OO in oOO00oO00O0OO :
  o0oOO0OO = oOo00OO [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  i1i1I ( 'Random Pick' , o0oOO0OO , 9060000 , iiIi1IIiIi + '247Streams.png' , Oo00OOOOO , '' , '' )
  if 18 - 18: oO0o + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
def oooOOOO0oooo ( ) :
 OOOiiiiI = 'http://arconaitv.me/'
 OoOOo000o0 = 'index.php#shows'
 if 51 - 51: o0o00Oo0O - ooOoO0O00 / oOo0O0Ooo
 I1i11 = BeautifulSoup ( requests . get ( OOOiiiiI + OoOOo000o0 ) . content )
 iiI1II11II1i = I1i11 . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for o0O0O0 in iiI1II11II1i :
  I11oo0ooOO = o0O0O0 . findAll ( 'a' )
  for iiI111I1iIiI in I11oo0ooOO :
   if iiI111I1iIiI . has_key ( 'href' ) :
    III1i1iI1 = OOOiiiiI + iiI111I1iIiI [ 'href' ]
   o000O0O = iiI111I1iIiI [ 'title' ]
   iI111i1I1II = iiI111I1iIiI . findAll ( 'img' )
   for O00OO in iI111i1I1II :
    I11iII = OOOiiiiI + O00OO [ 'src' ]
    o0ooo00o = BeautifulSoup ( requests . get ( III1i1iI1 ) . content )
    oOO00oO00O0OO = o0ooo00o . findAll ( 'source' )
    for oOo00OO in oOO00oO00O0OO :
     o0oOO0OO = oOo00OO [ 'src' ] + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     i1i1I ( o000O0O , o0oOO0OO , 9060000 , I11iII , I11iII , '' , '' )
     if 29 - 29: I1ii11iIi11i % oO0o % III1iiIii . I11i / ii * i1iIi
def o0OoO000O ( name , url ) :
 import urlresolver
 try :
  OOo = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOo , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 9 - 9: o0ii1I
 if 56 - 56: IIiIiII11i / i1i1I1IIii1II + Ii + oooOo0oo0oo
def O0O0o0o0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00o0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , I11iII , iIIII , I11iI1i1I11I11 , o000O0O in O00o0 :
  if '.php' in url :
   I1I1II1I11 ( o000O0O , url , 100210 , I11iII , I11iI1i1I11I11 , iIIII )
  else :
   Ii1I1i ( o000O0O , url , 222 , I11iII , I11iI1i1I11I11 , iIIII )
   if 9 - 9: I1ii11iIi11i + OOooOOo - iI11I1II1I1I - o0ii1I + I11i
   if 97 - 97: oooOo0oo0oo
   if 92 - 92: I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii1I . I11i
def o0OOOOoo0o ( iconimage , url , extra ) :
 IioO0oOOO0Ooo = ' '
 I111IIiii1Ii = ' '
 I11iI1i1I11I11 = ' '
 II1 = ' '
 iiIIIiIii = oO0o0O0Ooo0o ( url )
 IioO0oOOO0Ooo = re . compile ( '<img src="(.+?)">' ) . findall ( iiIIIiIii )
 for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
  IioO0oOOO0Ooo = IioO0oOOO0Ooo
 I1i11II = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( iiIIIiIii )
 for I11iI1i1I11I11 in I1i11II :
  I11iI1i1I11I11 = I11iI1i1I11I11
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( iiIIIiIii )
 for url , II1 in IIi :
  II1 = 'S' + ( II1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  I1i ( ( II1 ) . replace ( '  ' , '' ) , url , 100101 , IioO0oOOO0Ooo , I11iI1i1I11I11 , I111IIiii1Ii , '' )
  Ii1IIiI1i ( 'Movies' , 'info' )
  if 31 - 31: i1i1I1IIii1II / III1iiIii * I11i . IIiIiII11i
def oooOO0OO0O ( url , name , fanart , extra , iconimage ) :
 o00o = extra
 II1 = name
 iiIIIiIii = oO0o0O0Ooo0o ( url )
 IioO0oOOO0Ooo = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( iiIIIiIii )
 for url , name , III11I in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  III11I = III11I
  Ii1I11I = name + ' - [COLORred]' + III11I + '[/COLOR]'
  I1i ( Ii1I11I , url , 100102 , IioO0oOOO0Ooo , fanart , 'Aired : ' + III11I , Ii1I11I )
  if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , name in IIi :
  for ii1 in o00OO00OoO :
   if ii1 in OOOiiiiI :
    URL = 'http://www.watchseriesgo.to/link/' + OOOiiiiI
    i1i1I ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  I1i ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 55 - 55: I1ii11iIi11i - oooOo0oo0oo
  if 84 - 84: i1IiiiI1iI + I1ii11iIi11i - OOooOOo * OOooOOo
def OoooO0o ( url , name ) :
 IIIii1iiIi = name
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 IIIIiIiIi1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oooo0OOo ( url , IIIii1iiIi )
 for url in i1Iii1i1I :
  oooo0OOo ( url , IIIii1iiIi )
 for url in IIIIiIiIi1 :
  oooo0OOo ( url , IIIii1iiIi )
  if 72 - 72: o0o00Oo0O / i1iIi + ii * IiI1i11I
def oooo0OOo ( url , season_name ) :
 if 'daclips.in' in url :
  OoOo0OOOoOo ( url , season_name )
 elif 'filehoot.com' in url :
  IIiiIIi1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  ooO000O ( url , season_name )
 elif 'vidspot.net' in url :
  oOIII111iiIi1 ( url , season_name )
 elif 'vodlocker' in url :
  Ii11Ii ( url , season_name )
 elif 'vidto' in url :
  IiIiIi1IIi ( url , season_name )
  if 69 - 69: o0ii1I + I1ii11iIi11i + IIiIiII11i - oOo0O0Ooo / Iii
  if 74 - 74: Iii - oooOo0oo0oo + ooOoO0O00 . oOo0O0Ooo + oooOo0oo0oo - Iii
def IiIiIi1IIi ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 , o000O0O in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 4 - 4: ooOoO0O00 - Ii / Ii / ii
  if 100 - 100: I1ii11iIi11i + I11i - o0o00Oo0O % IIiIiII11i . IiI1i11I
def ooO000O ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 , o000O0O in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 92 - 92: IIiIiII11i * ii - i1IiiiI1iI
def oOIII111iiIi1 ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 , o000O0O in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 58 - 58: iI11I1II1I1I + o0o00Oo0O
def Ii11Ii ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 30 - 30: i1iIi % IiI1i11I * oooOo0oo0oo - Ii1I * o0ii1I % i1iIi
def OoOo0OOOoOo ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 46 - 46: Ii - o0o00Oo0O . i1i1I1IIii1II
def IIiiIIi1 ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIiiiiI1 in IIi :
  OO00OOoO0o ( IiIiiiiI1 , season_name )
  if 100 - 100: oOo0O0Ooo / I11i * IiI1i11I . o0o00Oo0O / oooOo0oo0oo
def OO00OOoO0o ( Link , season_name ) :
 if 'http:/' in Link :
  oOO0o000Oo00o ( Link )
  if 21 - 21: ii - iI11I1II1I1I
def OO0OoOOO0 ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 O00ooOo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in O00ooOo :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 80 - 80: I11i - oooOo0oo0oo + ii
def I1i ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = True )
 return IIII
 if 24 - 24: iI11I1II1I1I + iI11I1II1I1I * IiI1i11I
 if 18 - 18: IiI1i11I * Iii - o0ii1I
def i1i1I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1i1III = [ ]
  II1i1III . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = False )
 return IIII
 if 34 - 34: i1IiiiI1iI - Ii / iI11I1II1I1I
def OOOo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 79 - 79: OOooOOo % III1iiIii % I1ii11iIi11i
def Ii1 ( url ) :
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iiiiii . play ( url ) . strip ( )
 except : pass
 if 3 - 3: i1IiiiI1iI - o0o00Oo0O % iI11I1II1I1I / III1iiIii . I11i
def oOO0o000Oo00o ( url ) :
 I1iiiiii = xbmc . Player ( )
 import urlresolver
 try : I1iiiiii . play ( url )
 except : pass
 if 3 - 3: o0o00Oo0O % ii / oooOo0oo0oo
def oO0o0O0Ooo0o ( url ) :
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
  if 89 - 89: IIiIiII11i / i1i1I1IIii1II
  if 14 - 14: oooOo0oo0oo . oOo0O0Ooo * i1iIi + IIiIiII11i - i1iIi + oooOo0oo0oo
  if 18 - 18: i1i1I1IIii1II - I11i - oOo0O0Ooo - oOo0O0Ooo
def O0ooooo0OOOO0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   OOooo00 ( )
  if O0O0ooOOO == 1 :
   i1oO ( )
  if O0O0ooOOO == 2 :
   iI ( )
  if O0O0ooOOO == 3 :
   Ii1IIi ( )
  if O0O0ooOOO == 4 :
   i111i11I1ii ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def O0Oo ( ) :
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
 if 64 - 64: i1i1I1IIii1II / Ii / I11i . ii
 if 11 - 11: Iii % ooOoO0O00
 if 16 - 16: oOo0O0Ooo + i1iIi % OOooOOo
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   o0o0oOo000o0 = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + o0o0oOo000o0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O0ooOOO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O0ooOOO == 0 :
    I1iI1I1 ( II1I )
    oooO ( )
   elif O0O0ooOOO == 1 :
    IiIi1 ( II1I )
  else :
   pass
   if 53 - 53: ii - III1iiIii
def IiIi1 ( addon ) :
 o0o0oOo000o0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 87 - 87: i1i1I1IIii1II . oOo0O0Ooo
def I1iI1I1 ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 i1iIIIiiiI = os . path . join ( IIIII , 'default.py' )
 OoO00oo00 = open ( i1iIIIiiiI , "w+" )
 if 76 - 76: ii + I1ii11iIi11i % III1iiIii . oO0o + IIiIiII11i
 OoO00oo00 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OoO00oo00 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OoO00oo00 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 70 - 70: oOo0O0Ooo / Iii
 if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + i1i1I1IIii1II
 if 38 - 38: III1iiIii . o0ii1I
 if 24 - 24: I11i - I11i + Ii1I + oOo0O0Ooo - i1i1I1IIii1II
def I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIiI = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0oOOo0o = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIIIiIiIi1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0o0oO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1III11iiii11i1 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url , ooOo0OoO , I11iI1i1I11I11 , iIIII in IIiI :
  if 'php' in url :
   I1I1II1I11 ( o000O0O , url , 90037 , ooOo0OoO , I11iI1i1I11I11 , iIIII )
  elif o000O0O == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , ooOo0OoO , I11iI1i1I11I11 , iIIII )
  else :
   Ii1I1i ( o000O0O , url , 222 , ooOo0OoO , I11iI1i1I11I11 , iIIII )
 for o000O0O , I11iII , url , i1iiIIi1I in O0oOOo0o :
  I1I1II1I11 ( o000O0O , url , 90037 , I11iII , i1iiIIi1I , '' )
 for o000O0O , I11iII , url , i1iiIIi1I in IIi :
  I1I1II1I11 ( o000O0O , url , 90037 , I11iII , i1iiIIi1I , '' )
 for o000O0O , url , I11iII , i1iiIIi1I in i1Iii1i1I :
  Ii1I1i ( o000O0O , url , 222 , I11iII , i1iiIIi1I , '' )
 for o000O0O , url , I11iII , i1iiIIi1I in IIIIiIiIi1 :
  Ii1I1i ( o000O0O , url , 222 , I11iII , i1iiIIi1I , '' )
 for o000O0O , url , I11iII , i1iiIIi1I in O0o0oO :
  Ii1I1i ( o000O0O , url , 222 , I11iII , i1iiIIi1I , '' )
 for o000O0O , url , I11iII in I1III11iiii11i1 :
  Ii1I1i ( o000O0O , url , 222 , I11iII , '' , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def iiI1I1IIi11i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , I11iII , url , i1iiIIi1I in IIi :
  I1I1II1I11 ( o000O0O , url , 90037 , I11iII , i1iiIIi1I , '' )
 for o000O0O , url , I11iII , i1iiIIi1I in i1Iii1i1I :
  Ii1I1i ( o000O0O , url , 222 , I11iII , i1iiIIi1I , '' )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  if 45 - 45: i1iIi % I11i - i1iIi
def i1i1 ( ) :
 oO0ooOoO = [ 'serialsearch' , 'moviesearch' ]
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 if O0Ooo == '' :
  pass
 else :
  for oO00oOOo0Oo in oO0ooOoO :
   IIiIIIIii = Oo0o0000o0o0 + oO00oOOo0Oo + '.php'
   iiIIIiIii = OooOoooOo ( IIiIIIIii )
   if iiIIIiIii != 'Opened' :
    O00o0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( iiIIIiIii )
    for o000O0O , OOOiiiiI , ooOo0OoO , I11iI1i1I11I11 , iIIII in O00o0 :
     if O0Ooo in o000O0O . lower ( ) :
      iIiI1 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ii1 in iIiI1 :
       if ii1 == OOOiiiiI :
        o000O0O = '[COLORred]* [/COLOR]' + ( o000O0O ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        iIIiI1ii = open ( OOOO0OOoO0O0 , "a" )
        iIIiI1ii . write ( 'item="' + o000O0O + '"\n' )
        iIIiI1ii . close
      if 'php' in OOOiiiiI :
       I1I1II1I11 ( o000O0O , OOOiiiiI , 90037 , ooOo0OoO , I11iI1i1I11I11 , iIIII )
      else :
       Ii1I1i ( o000O0O , OOOiiiiI , 222 , ooOo0OoO , I11iI1i1I11I11 , iIIII )
       if 78 - 78: o0o00Oo0O * oooOo0oo0oo
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   if 43 - 43: Ii1I / oOo0O0Ooo . i1iIi
def Ooo0oO0 ( ) :
 if 86 - 86: o0o00Oo0O
 if 95 - 95: IiI1i11I * oooOo0oo0oo . OOooOOo . ooOoO0O00 . ooOoO0O00 - I11i
 if 26 - 26: iI11I1II1I1I % Ii % Ii1I
 if 67 - 67: ii
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + oooOo0oo0oo * III1iiIii
 if 2 - 2: ooOoO0O00 - i1iIi + oOo0O0Ooo . I11i * I11i / OOooOOo
 if 93 - 93: ooOoO0O00
 if 53 - 53: ii + I1ii11iIi11i + i1i1I1IIii1II
 if 24 - 24: IiI1i11I - III1iiIii - IiI1i11I * Ii1I . ii / III1iiIii
 if 66 - 66: I1ii11iIi11i
 if 97 - 97: ooOoO0O00 - ii / i1IiiiI1iI * oOo0O0Ooo
 if 55 - 55: I11i . IiI1i11I
 if 87 - 87: I11i % iI11I1II1I1I
 if 100 - 100: i1IiiiI1iI . oOo0O0Ooo * i1IiiiI1iI - oOo0O0Ooo . Iii * o0ii1I
 if 89 - 89: oO0o + III1iiIii * i1IiiiI1iI
 if 28 - 28: ii . i1i1I1IIii1II % Ii1I / ooOoO0O00 / oooOo0oo0oo
 if 36 - 36: I11i + Iii - III1iiIii + iI11I1II1I1I + ii
 if 4 - 4: IIiIiII11i . Iii + o0ii1I * i1IiiiI1iI . i1iIi
 if 87 - 87: OOooOOo / oO0o / Ii
 if 74 - 74: i1i1I1IIii1II / Ii1I % I11i
 if 88 - 88: OOooOOo - Ii % I11i * Iii + Ii1I
 I1i11 = BeautifulSoup ( requests . get ( 'https://tvcatchup.com/channels' ) . content )
 o0ooo00o = requests . get ( 'http://www.djing.com/' ) . content
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0ooo00o )
 iiI1II11II1i = I1i11 . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for o0O0O0 in iiI1II11II1i :
  I11oo0ooOO = o0O0O0 . findAll ( 'a' )
  for iiI111I1iIiI in I11oo0ooOO :
   if iiI111I1iIiI . has_attr ( 'href' ) :
    III1i1iI1 = 'https://tvcatchup.com' + iiI111I1iIiI [ 'href' ]
   iI111i1I1II = iiI111I1iIiI . findAll ( 'img' )
   for O00OO in iI111i1I1II :
    I11iII = O00OO [ 'src' ]
    Oo = O00OO [ 'alt' ]
   IIi = re . compile ( '<br/>(.+?)</a>' ) . findall ( str ( iiI111I1iIiI ) )
   for iIIIiIi1I1i in IIi :
    oOOo000oOoO0 ( ( '[COLORgold]' + Oo + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iIIIiIi1I1i + '[/COLOR]' ) , III1i1iI1 , 90024 , I11iII )
    if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
 for OOOiiiiI , I11iII , o000O0O in i1Iii1i1I :
  if 'Submit' in o000O0O :
   pass
  elif '&lt;' in o000O0O :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]' + o000O0O + '[/COLOR]' , OOOiiiiI , 90025 , 'http://www.djing.com' + I11iII , Oo00OOOOO , '' )
   if 91 - 91: iI11I1II1I1I % oO0o . I11i + o0ii1I + I11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def o00OOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 87 - 87: oO0o % oOo0O0Ooo
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0oOOoooOO0O ( url )
def ooooOoO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IIIIIIII ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 83 - 83: iI11I1II1I1I
def o00o0oOo0O0O ( ) :
 II11iIiIIIiI = cloudflare . source ( 'view-source:http://fightnights.com/match/6894' )
 oO0ooOO = re . compile ( '<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iii1iII1 , oO0O000oOo , OoOOOO in oO0ooOO :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iii1iII1 + oO0O000oOo + OoOOOO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
 for OOOiiiiI , o000O0O in IIi :
  if 'yr' in OOOiiiiI :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
   if 18 - 18: i1iIi % Ii . iI11I1II1I1I - IiI1i11I
def oo00ooOoO00 ( ) :
 if 80 - 80: oOo0O0Ooo + i1i1I1IIii1II - ooOoO0O00 . o0ii1I / I11i / oOo0O0Ooo
 if 1 - 1: Iii + Ii - oOo0O0Ooo / oooOo0oo0oo + i1IiiiI1iI
 if 80 - 80: i1i1I1IIii1II + I11i * o0ii1I + oO0o
 if 75 - 75: Iii / I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
 if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
 if 50 - 50: i1iIi + ooOoO0O00
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'yr' in OOOiiiiI :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OOOiiiiI , 10201 , iiIi1IIiIi + 'rated.png' )
   if 31 - 31: o0ii1I
def OoOOo00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00 , url , o000O0O in IIi :
  if 'id' in url :
   IiI11i1IIiiI ( ( '[COLORred]RANK [COLORblue]' + O00 + '[COLORred] - [COLORblue]' + o000O0O + '[/COLOR]' ) , o000O0O , 10202 , iiIi1IIiIi + 'rated.png' )
   if 94 - 94: Iii . Iii + Ii - oooOo0oo0oo * Ii1I
def iIoo0ooooO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiIIi = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooO0000o00O = ( url )
 O0Ooo = ooO0000o00O . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 i1iiIIiI1iiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 I11Ii111I = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Oo00OO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oO00OoOOOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Oo0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ooO0000o00O
 o0OOOOO0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I1I1IiIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 58 - 58: OOooOOo - IiI1i11I - ii
 o00ii111Iiii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oo0oO0o0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 44 - 44: o0o00Oo0O + i1iIi . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - Iii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( i1iiIIiI1iiI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( I11Ii111I )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo00OO0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 o0o0OoOOOOOo = O00O0oOO00O00 ( oo0O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 Ii11iii1II1i = O00O0oOO00O00 ( Oo0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o0OOoOO = O00O0oOO00O00 ( o0OOOOO0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iII1 = O00O0oOO00O00 ( I1I1IiIi1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 24 - 24: I11i + i1iIi + Iii - iI11I1II1I1I
 if 49 - 49: Iii . i1iIi * OOooOOo % III1iiIii . o0o00Oo0O
 IiI1iiI1III1I = O00O0oOO00O00 ( o00ii111Iiii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 Oo000 = O00O0oOO00O00 ( oo0oO0o0 )
 if 57 - 57: OOooOOo
 if 17 - 17: i1iIi
 if 81 - 81: o0o00Oo0O / III1iiIii - iI11I1II1I1I / IIiIiII11i
 if 86 - 86: iI11I1II1I1I
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
 if 17 - 17: Iii / I11i % I1ii11iIi11i
 if 71 - 71: III1iiIii . i1IiiiI1iI . oO0o
 if 68 - 68: Ii % i1i1I1IIii1II * oO0o * III1iiIii * IIiIiII11i + o0o00Oo0O
 if 66 - 66: Iii % Ii1I % ii
 if 34 - 34: I11i / IiI1i11I % o0o00Oo0O . oO0o . ooOoO0O00
 if 29 - 29: o0o00Oo0O . i1IiiiI1iI
 if iII1 != 'Failed' :
  OO0o0oO0O000o = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iII1 )
  for url , o000O0O in OO0o0oO0O000o :
   I1iI11iii = O00O0oOO00O00 ( url )
   oo0oO = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1iI11iii )
   for IiIi1iI11 , iiI1iI1I in oo0oO :
    iiI1iI1I = ( iiI1iI1I . replace ( '.' , ' ' ) )
    if O0Ooo in iiI1iI1I . lower ( ) :
     if '.mkv' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.mp4' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.avi' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.wav' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in i1Iii1i1I :
   if ooO0000o00O in o000O0O . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 55 - 55: i1iIi
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
 if o00OooOO000 != 'Failed' :
  IIIIiIiIi1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OO0iIiiIi11IIi , o000O0O in IIIIiIiIi1 :
   if ooO0000o00O in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I11Ii111I + OO0iIiiIi11IIi ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  O0o0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in O0o0oO :
   if ooO0000o00O in o000O0O . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 64 - 64: ii . Ii1I % o0o00Oo0O + oOo0O0Ooo - I11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o0OoOOOOOo != 'Failed' :
  ooo0oo00O00oO = [ ]
  I1III11iiii11i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o0OoOOOOOo )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in I1III11iiii11i1 :
   if ooO0000o00O in o000O0O . lower ( ) :
    if o000O0O in ooo0oo00O00oO :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , i1iIiIi1I , I1i11II , iIIII )
     ooo0oo00O00oO . append ( o000O0O )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if Ii11iii1II1i != 'Failed' :
  oOO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Ii11iii1II1i )
  for url , I11iII , o000O0O in oOO :
   if ooO0000o00O in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , I11iII )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 92 - 92: Iii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: oOo0O0Ooo . o0ii1I
    if 46 - 46: IiI1i11I - iI11I1II1I1I
    if 50 - 50: IiI1i11I / IiI1i11I + oooOo0oo0oo * i1iIi / Ii1I
    if 14 - 14: o0ii1I % oOo0O0Ooo - iI11I1II1I1I . oooOo0oo0oo + oO0o - i1IiiiI1iI
    if 5 - 5: IiI1i11I
    if 62 - 62: OOooOOo . ii . oooOo0oo0oo . oO0o * IiI1i11I
    if 78 - 78: i1i1I1IIii1II / oO0o - i1i1I1IIii1II * ii . OOooOOo
    if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
    if 37 - 37: ooOoO0O00 - oooOo0oo0oo % ii / oooOo0oo0oo % i1iIi
    if 48 - 48: Ii % i1i1I1IIii1II
    if 29 - 29: IiI1i11I + Ii % Iii
    if 93 - 93: OOooOOo % iI11I1II1I1I
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
    if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
    if 21 - 21: oooOo0oo0oo
    if 6 - 6: III1iiIii
    if 46 - 46: III1iiIii + i1i1I1IIii1II
 if IiI1iiI1III1I != 'Failed' :
  Oo00o0O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1iiI1III1I )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in Oo00o0O0O :
   if ooO0000o00O in o000O0O . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 84 - 84: Iii % ooOoO0O00
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: Ii1I * Ii1I . i1iIi . Ii
    if 48 - 48: I11i . o0ii1I + OOooOOo % Ii1I / Ii
    if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + III1iiIii % Ii % OOooOOo
    if 78 - 78: o0ii1I + OOooOOo + III1iiIii - III1iiIii . Ii / oO0o
    if 27 - 27: o0ii1I - o0o00Oo0O % Iii * i1IiiiI1iI . III1iiIii % iI11I1II1I1I
    if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % i1iIi
    if 24 - 24: OOooOOo
    if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
    if 28 - 28: oOo0O0Ooo
    if 49 - 49: Iii . I11i % i1i1I1IIii1II / o0ii1I
 Oo0Oo0o0oo0O0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 53 - 53: i1iIi / iI11I1II1I1I - oO0o + i1i1I1IIii1II
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  IIiIIIIii = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  iII1 = O00O0oOO00O00 ( IIiIIIIii )
  if iII1 != 'Failed' :
   OO0o0oO0O000o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1 )
   for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in OO0o0oO0O000o :
    if ooO0000o00O in o000O0O . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , i1iIiIi1I , I1i11II , iIIII )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 30 - 30: III1iiIii
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 24 - 24: oO0o - i1i1I1IIii1II + Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
 Oo0Oo0o0oo0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 79 - 79: OOooOOo / i1iIi
 if 77 - 77: I1ii11iIi11i
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  IIiIIIIii = iiIIi + oO00oOOo0Oo
  i1i111Iiiiiii = O00O0oOO00O00 ( IIiIIIIii )
  if i1i111Iiiiiii != 'Failed' :
   Iiiii1IIiI = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( i1i111Iiiiiii )
   for OO0iIiiIi11IIi , o000O0O in Iiiii1IIiI :
    if ooO0000o00O in o000O0O . lower ( ) :
     oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiIIi + oO00oOOo0Oo + OO0iIiiIi11IIi ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 33 - 33: Iii
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: OOooOOo % IIiIiII11i
def O0Oo00OoOo ( ) :
 IiI11i1IIiiI ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 IiI11i1IIiiI ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 IiI11i1IIiiI ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 IiI11i1IIiiI ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 95 - 95: iI11I1II1I1I - i1IiiiI1iI - oooOo0oo0oo + i1IiiiI1iI % Ii1I . oOo0O0Ooo
def IiiIIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , II1 , iI1iIiiI , III11I , Oo0OOo in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + o000O0O + '[/COLOR] [COLORred]Season[/COLOR]-' + II1 + ' [COLORred]Returns [/COLOR]- ' + Oo0OOo + ' ' + III11I ) , o000O0O , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 36 - 36: o0o00Oo0O * oO0o % IiI1i11I * IiI1i11I / oO0o * III1iiIii
def IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , II1 , iI1iIiiI in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + o000O0O + '[/COLOR] [COLORred]Season[/COLOR]-' + II1 + ' [COLORred] Status Unknown[/COLOR] ' ) , o000O0O , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 87 - 87: i1iIi . o0o00Oo0O % i1IiiiI1iI + Ii1I + o0ii1I % iI11I1II1I1I
def ii11iIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , II1 , iI1iIiiI , III11I in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + o000O0O + ' [COLORred] Cancelled On[/COLOR] ' + III11I ) , o000O0O , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 1 - 1: IiI1i11I * OOooOOo
def OO0ooo0 ( url ) :
 ooO0000o00O = ( url )
 O0Ooo = ooO0000o00O . lower ( )
 if 7 - 7: Ii1I - i1i1I1IIii1II * oooOo0oo0oo + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
 IiIi1iI11 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ooO0000o00O ) . replace ( ' ' , '+' )
 i1iiIIiI1iiI = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 I11Ii111I = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 Oo00OO0 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oO00OoOOOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * o0ii1I
 o0OOOOO0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 I1I1IiIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iI111i11iI1 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 2 - 2: OOooOOo + i1IiiiI1iI + ii . ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 19 - 19: IiI1i11I - I11i - o0ii1I - OOooOOo . IiI1i11I . i1IiiiI1iI
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 48 - 48: IiI1i11I + III1iiIii
 if 60 - 60: Iii + IiI1i11I . III1iiIii / ooOoO0O00 . iI11I1II1I1I
 I1III1111iIi = O00O0oOO00O00 ( IiIi1iI11 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( i1iiIIiI1iiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( I11Ii111I )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo00OO0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 i1i111Iiiiiii = O00O0oOO00O00 ( oO00OoOOOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 14 - 14: oooOo0oo0oo
 if 79 - 79: o0ii1I
 o0OOoOO = O00O0oOO00O00 ( o0OOOOO0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 iII1 = O00O0oOO00O00 ( I1I1IiIi1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 o0Oii111 = O00O0oOO00O00 ( iI111i11iI1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 93 - 93: ii * I1ii11iIi11i
 if iII1 != 'Failed' :
  OO0o0oO0O000o = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iII1 )
  for url , o000O0O in OO0o0oO0O000o :
   I1iI11iii = O00O0oOO00O00 ( url )
   oo0oO = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1iI11iii )
   for IiIi1iI11 , iiI1iI1I in oo0oO :
    if O0Ooo in iiI1iI1I . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , url + IiIi1iI11 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 10 - 10: i1IiiiI1iI * ii + Iii - Ii1I / Ii1I . Ii
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0OOoOO != 'Failed' :
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOoOO )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in i1I1i :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 22 - 22: I1ii11iIi11i % oO0o - ii * I1ii11iIi11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 38 - 38: iI11I1II1I1I / i1iIi
    if 13 - 13: iI11I1II1I1I
    if 77 - 77: Ii - iI11I1II1I1I / i1i1I1IIii1II / i1iIi / oO0o
    if 56 - 56: ii * o0o00Oo0O
    if 85 - 85: ii % OOooOOo * iI11I1II1I1I
    if 44 - 44: iI11I1II1I1I . Ii1I + i1IiiiI1iI . i1iIi
    if 7 - 7: Ii1I + iI11I1II1I1I * Iii * Iii / IIiIiII11i - o0ii1I
    if 65 - 65: i1i1I1IIii1II + OOooOOo + IIiIiII11i
    if 77 - 77: IIiIiII11i
    if 50 - 50: o0o00Oo0O . o0o00Oo0O . i1iIi % I1ii11iIi11i
    if 68 - 68: i1i1I1IIii1II
 if o0Oii111 != 'Failed' :
  i11iIIiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0Oii111 )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in i11iIIiI1I1 :
   if O0Ooo in o000O0O . lower ( ) :
    IiI11i1IIiiI ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , i1iIiIi1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 4 - 4: I1ii11iIi11i * I1ii11iIi11i / OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  Ii1Ii1Ii1I1I = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , I11iII , o000O0O , III1II1i in i1Iii1i1I :
   if O0Ooo in o000O0O . lower ( ) :
    if 'season' in III1II1i :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , I11iII , I11iII , '' )
    if 'episodes' in III1II1i :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , I11iII , I11iII , '' )
  for url in Ii1Ii1Ii1I1I :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 3 - 3: IiI1i11I
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if I1III1111iIi != 'Failed' :
  O0oOOo0o = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
  for url , o000O0O , I11iII in O0oOOo0o :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( o000O0O ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , I11iII , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 35 - 35: III1iiIii . o0o00Oo0O + I1ii11iIi11i + oooOo0oo0oo + ooOoO0O00
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
    if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
    if 58 - 58: oooOo0oo0oo . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
    if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
    if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
    if 66 - 66: oO0o % I11i
    if 21 - 21: OOooOOo - ii % Ii
    if 71 - 71: ooOoO0O00 - Iii * i1IiiiI1iI + i1i1I1IIii1II - oO0o % Ii1I
    if 63 - 63: iI11I1II1I1I + oooOo0oo0oo . oO0o / oOo0O0Ooo
 if o00OooOO000 != 'Failed' :
  IIIIiIiIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for o000O0O in IIIIiIiIi1 :
   if O0Ooo in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( I11Ii111I + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 84 - 84: ooOoO0O00
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  O0o0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for o000O0O in O0o0oO :
   if O0Ooo in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( Oo00OO0 + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 42 - 42: IIiIiII11i - oO0o - ii . IiI1i11I / OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if i1i111Iiiiiii != 'Failed' :
  Iiiii1IIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i111Iiiiiii )
  for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in Iiiii1IIiI :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 81 - 81: III1iiIii / OOooOOo * III1iiIii . o0o00Oo0O
 OOOOo00oo00O = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oO00oOOo0Oo in OOOOo00oo00O :
  IIiIIIIii = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  IiI1iiI1III1I = O00O0oOO00O00 ( IIiIIIIii )
  if IiI1iiI1III1I != 'Failed' :
   Oo00o0O0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiI1iiI1III1I )
   for o000O0O , iIIII , url , I11iII , I11iI1i1I11I11 , i1Ii11II in Oo00o0O0O :
    if O0Ooo in o000O0O . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] - Source Pandoras[/COLOR]' , url , i1Ii11II , I11iII , I11iI1i1I11I11 , iIIII )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 83 - 83: IIiIiII11i * ooOoO0O00 * IiI1i11I . Ii1I / Iii + ooOoO0O00
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 43 - 43: ii
     if 97 - 97: Ii1I / I1ii11iIi11i + i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: i1iIi % i1IiiiI1iI * I1ii11iIi11i
def O0O000oOo0O ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']Adult Gallery[/COLOR]' , '[COLOR' + ooOoOoo0O + ']JizBox[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Adult Channels[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  o0O0O0oo0oo0 ( )
 if O0O0ooOOO == 1 :
  O0Oo000OO000 ( )
 if O0O0ooOOO == 2 :
  OOOO00OooO ( )
  if 64 - 64: oO0o . oOo0O0Ooo - ii . i1iIi - IiI1i11I
  if 77 - 77: o0ii1I % OOooOOo / IIiIiII11i % IiI1i11I % ii % oO0o
  if 19 - 19: III1iiIii * i1IiiiI1iI / i1i1I1IIii1II * i1IiiiI1iI - ii * Iii
def o0O0O0oo0oo0 ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']YOLOselfies[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HotNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MyNudeBabes[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TeenNudeGirls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADULTmeme[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GIRLSmeme[/COLOR]' , ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  iiiI1i1 ( 'http://www.yoloselfie.com/' )
 if O0O0ooOOO == 1 :
  I1i1i11 ( 'http://www.hotnudegirls.net/#nudegirls' )
 if O0O0ooOOO == 2 :
  i1IoOOoooO0O0 ( 'http://www.teennudegirls.com/' )
 if O0O0ooOOO == 3 :
  i1IoOOoooO0O0 ( 'http://www.teennudegirls.com/' )
 if O0O0ooOOO == 4 :
  ii1O0ooooo000 ( 'https://jokideo.com/category/funny-dirty-rude-jokes/' )
 if O0O0ooOOO == 5 :
  ii1O0ooooo000 ( 'https://jokideo.com/category/hot-and-sexy/' )
  if 97 - 97: Ii % i1i1I1IIii1II / I1ii11iIi11i / I1ii11iIi11i
def iiiI1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "<a href='([^']*)' class='btn' title='next 100" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 100111 , I11iII )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 100110 , I11iII )
def OoO00ooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "/><link rel='image_src' href='([^']*)'/>" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiO0o0O0oo0o = "ShowPicture(" + url + ')'
  xbmc . executebuiltin ( iiO0o0O0oo0o )
  sys . exit ( 1 )
def ii1O0ooooo000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http:' + I11iII , 100113 , 'http:' + I11iII )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http:' + url , 100112 , I11iII )
def I1i1i11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.hotnudegirls.net/' + url , 100115 , I11iII )
def O0Oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class='rosalind' href='([^']*)' ><img src='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iII in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , I11iII , 100113 , I11iII )
def I11iI1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://mynudebabes.com' + url , 100118 , I11iII )
def Iii1iiIi1II1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iII in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , I11iII , 100113 , I11iII )
def i1IoOOoooO0O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '' , '' ) . replace ( '' , '' ) . replace ( '' , '' ) , 'http://www.teennudegirls.com' + url , 100118 , I11iII )
def Oo000o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Next &raquo;</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iII in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Click To Enlarge[/COLOR]' , I11iII , 100113 , I11iII )
def OO00oo ( url ) :
 iiO0o0O0oo0o = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iiO0o0O0oo0o )
 sys . exit ( 1 )
 if 84 - 84: i1iIi + Ii - oooOo0oo0oo * i1iIi
def I1IiiIiii1 ( ) :
 if 39 - 39: i1iIi / o0o00Oo0O * III1iiIii
 if 17 - 17: o0ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % oooOo0oo0oo
 if 14 - 14: I11i % III1iiIii + Ii1I + oO0o
 if 76 - 76: oO0o - Ii + OOooOOo + oooOo0oo0oo / ii
 if 50 - 50: IIiIiII11i - i1IiiiI1iI + iI11I1II1I1I + iI11I1II1I1I
 if 91 - 91: IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
 if 26 - 26: I11i
 if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
 if 46 - 46: IIiIiII11i - III1iiIii * ii / i1i1I1IIii1II % III1iiIii
 if 11 - 11: iI11I1II1I1I . OOooOOo / III1iiIii % i1iIi
 if 61 - 61: i1iIi - oooOo0oo0oo + oooOo0oo0oo
 IiI11i1IIiiI ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 IiI11i1IIiiI ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 IiI11i1IIiiI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 40 - 40: Ii . iI11I1II1I1I
def IiIIII1iiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , i1I1IiI1ii in IIi :
  IiI11i1IIiiI ( ( o000O0O + ' - ' + i1I1IiI1ii ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 64 - 64: IiI1i11I * Ii1I % IIiIiII11i - OOooOOo + Ii1I
def OO0OOoo0OOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 94 - 94: Ii % ii / oOo0O0Ooo
def iII1Iii11111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for I11iII , o000O0O , url in IIi :
  IiI11i1IIiiI ( o000O0O , url , 90054 , I11iII )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 80 - 80: i1i1I1IIii1II * Iii / iI11I1II1I1I % i1i1I1IIii1II / iI11I1II1I1I
def Iiii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for I11iII , i1I1IiI1ii , url , o000O0O , i1iiIIiiiII in IIi :
  I1I1II1I11 ( i1I1IiI1ii + ' - ' + o000O0O + ' - ' + i1iiIIiiiII , url , 90044 , I11iII , I11iII , '' )
 for I11iII , o000O0O , url in i1Iii1i1I :
  IiI11i1IIiiI ( o000O0O , url , 90044 , I11iII , I11iII , '' )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: ii / I11i % Iii % oO0o * IiI1i11I + iI11I1II1I1I
def I11iiI11iiI ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 O0Ooo = OOOII1i1II . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0Ooo )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O , III1II1i in IIi :
  if 'season' in III1II1i :
   IiI11i1IIiiI ( o000O0O , OOOiiiiI , 90054 , I11iII , I11iII , '' )
  if 'episodes' in III1II1i :
   IiI11i1IIiiI ( o000O0O , OOOiiiiI , 90044 , I11iII , I11iII , '' )
 for OOOiiiiI in next :
  IiI11i1IIiiI ( 'NEXT' , OOOiiiiI , 90053 , iiIi1IIiIi + 'Next.png' )
  if 9 - 9: I1ii11iIi11i % ii - o0ii1I
def iIII11Iiii1 ( ) :
 if 95 - 95: oOo0O0Ooo
 if 99 - 99: o0o00Oo0O
 if 76 - 76: i1IiiiI1iI - i1i1I1IIii1II . oooOo0oo0oo % I11i
 if 30 - 30: Ii1I % Iii / i1IiiiI1iI
 if 1 - 1: i1IiiiI1iI - Iii
 if 45 - 45: o0ii1I - oooOo0oo0oo
 if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . Iii % i1iIi . IIiIiII11i
 if 10 - 10: o0ii1I - Ii . Ii1I % ooOoO0O00
 if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - oooOo0oo0oo . iI11I1II1I1I
 if 30 - 30: i1iIi + i1iIi % III1iiIii - I11i - Ii1I
 IiI11i1IIiiI ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 IiI11i1IIiiI ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 IiI11i1IIiiI ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 IiI11i1IIiiI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 36 - 36: Iii % oooOo0oo0oo
def OoO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , i1I1IiI1ii in IIi :
  if 'genre' in url :
   IiI11i1IIiiI ( ( o000O0O + ' - ' + i1I1IiI1ii ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 37 - 37: Iii
def o0iIIIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  if 'release' in url :
   IiI11i1IIiiI ( o000O0O , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 50 - 50: i1IiiiI1iI + i1iIi + IiI1i11I
def ii11iiI11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for I11iII , o000O0O , OoOooO , url , iIIII in IIi :
  I1I1II1I11 ( o000O0O + ' ' + OoOooO , url , 90044 , I11iII , I11iII , iIIII )
 for I11iII , o000O0O , III1II1i , url , o0oOo00 , iIIII in i1Iii1i1I :
  if 'movies' in III1II1i :
   I1I1II1I11 ( o000O0O + ' - ' + o0oOo00 , url , 90044 , I11iII , I11iII , iIIII )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 22 - 22: iI11I1II1I1I + III1iiIii + Ii1I + i1IiiiI1iI - o0ii1I
def I1IIII1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oOO0 ( 'http:' + url )
  if 90 - 90: III1iiIii - Ii1I % Iii % iI11I1II1I1I - Ii1I
def oOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( ( o000O0O ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def IiIiI1i1 ( ) :
 if 18 - 18: o0ii1I
 if 25 - 25: oO0o * i1i1I1IIii1II % Ii + Ii * oO0o
 if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
 if 62 - 62: o0o00Oo0O . I1ii11iIi11i
 if 33 - 33: I1ii11iIi11i / iI11I1II1I1I % ooOoO0O00
 if 76 - 76: o0ii1I + iI11I1II1I1I + OOooOOo . oO0o
 if 49 - 49: III1iiIii / i1iIi / oooOo0oo0oo
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - i1iIi
 if 38 - 38: I11i % i1IiiiI1iI + Ii + IiI1i11I + i1iIi / Ii
 if 94 - 94: IiI1i11I - I1ii11iIi11i + i1i1I1IIii1II
 if 59 - 59: Iii . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 if 56 - 56: i1i1I1IIii1II + i1iIi
 if 32 - 32: IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
 if 2 - 2: Ii - i1IiiiI1iI + oO0o % Iii * o0ii1I
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 O0Ooo = OOOII1i1II . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0Ooo )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O , Ooo000O00 in IIi :
  if 'movies' in Ooo000O00 :
   IiI11i1IIiiI ( Ooo000O00 + '-' + o000O0O , OOOiiiiI , 90044 , I11iII )
 for OOOiiiiI in next :
  ii11iiI11I ( OOOiiiiI )
  if 36 - 36: oooOo0oo0oo % Ii
def o0O0O0ooo0oOO ( ) :
 IiI11i1IIiiI ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 80006 , iiIi1IIiIi + 'Desi.png' )
def Iiii1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , I11iII , o000O0O in IIi :
  oOOo000oOoO0 ( o000O0O , url , 80007 , I11iII )
 for url , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def ooOOo00oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  O0oOOoooOO0O ( url )
def IIIII1Ii ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'http://www.join4films.com/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0Ooo = OOOII1i1II . lower ( )
 Iiii1Ii ( O0Ooo )
 if 13 - 13: IIiIiII11i
 if 57 - 57: o0ii1I - ii
 if 68 - 68: I11i % Ii1I / i1IiiiI1iI + i1IiiiI1iI - i1IiiiI1iI . oO0o
 if 100 - 100: OOooOOo % I1ii11iIi11i
 if 76 - 76: IIiIiII11i / oO0o + ii . Ii1I . Iii . i1iIi
 if 43 - 43: ooOoO0O00
 if 17 - 17: o0o00Oo0O - OOooOOo
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 if 34 - 34: o0ii1I * o0ii1I - Ii1I - o0o00Oo0O . Ii
 if 32 - 32: iI11I1II1I1I . oO0o * i1i1I1IIii1II / oooOo0oo0oo . IIiIiII11i - I1ii11iIi11i
 if 10 - 10: Ii1I / Ii - o0ii1I + i1i1I1IIii1II * oOo0O0Ooo
 if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
 if 64 - 64: Iii + oO0o
 if 25 - 25: oOo0O0Ooo . i1iIi + oOo0O0Ooo % o0ii1I * iI11I1II1I1I
 if 31 - 31: Ii + oooOo0oo0oo - o0o00Oo0O
 if 51 - 51: oO0o * ooOoO0O00 / o0ii1I * oooOo0oo0oo + i1iIi % Ii1I
 if 34 - 34: i1i1I1IIii1II * ii + o0ii1I + Ii
def iiIi ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 74 - 74: Iii / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
def Ooi1IIii11i1I1 ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'http://imoviemax.se/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 O0Ooo = OOOII1i1II . lower ( )
 Ii1I1 ( O0Ooo )
def O0oo00oOOO0o ( url ) :
 II1i = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I111iiIIiI1I in IIi :
  if o000O0O in II1i :
   pass
  else :
   I1I1II1I11 ( o000O0O + ' - ' + I111iiIIiI1I + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   II1i . append ( o000O0O )
   if 51 - 51: oOo0O0Ooo + oooOo0oo0oo + Iii
def i1Iiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , o0O0O in IIi :
  I1I1II1I11 ( o000O0O + ' - Views:' + o0O0O , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 56 - 56: o0o00Oo0O
  if 45 - 45: OOooOOo - oO0o - OOooOOo
def Ii1I1 ( url ) :
 IIiiI = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , o000O0O , url in IIi :
  I1I1II1I11 ( o000O0O , url , 10075 , I11iII , I11iII , '' )
  IIiiI . append ( o000O0O )
  if 36 - 36: IiI1i11I
def O0ooooooo00 ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for I1111ii11IIII , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  IiIi1II111I = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + IiIi1II111I
  o00oIIi1i1 = ( I1111ii11IIII ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( o00oIIi1i1 , IiIi1II111I , 10076 , img , img , '' )
  if 84 - 84: oooOo0oo0oo + o0ii1I + I11i
def i1i1iIII11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for i1iiIIiI1iiI in IIi :
  if '=m' in i1iiIIiI1iiI :
   IiIIoOo ( i1iiIIiI1iiI )
  elif 'php' in i1iiIIiI1iiI :
   i1i1iIII11i ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( i1iiIIiI1iiI )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for I11Ii111I in IIi :
    IiIIoOo ( i1iiIIiI1iiI )
    if 69 - 69: o0o00Oo0O / IIiIiII11i * ooOoO0O00
    if 66 - 66: o0o00Oo0O
    if 52 - 52: oO0o * ii
def Ii11iiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 o0OO0oooo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for III11I , I11II1i1 in o0OO0oooo :
  print 'there ><><><><><><><><><><><><'
  III11I = III11I
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11II1i1 ) )
  for o000O0O , IiI1ii11I1 in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + III11I + '[/COLOR] - ' + o000O0O + ' - [COLOR' + ooOoOoo0O + ']' + IiI1ii11I1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 O00OooOo00o = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for III11I , I1i1iI in O00OooOo00o :
  print 'there ><><><><><><><><><><><><'
  III11I = III11I
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1i1iI ) )
  for o000O0O , IiI1ii11I1 in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + III11I + '[/COLOR] - ' + o000O0O + ' - [COLOR' + ooOoOoo0O + ']' + IiI1ii11I1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 30 - 30: Iii % OOooOOo / Ii1I * o0o00Oo0O * o0ii1I . oOo0O0Ooo
   if 46 - 46: OOooOOo - o0o00Oo0O
   if 70 - 70: Iii + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * Iii
def i11111I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in O00OooOo00o :
  o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
  for o000O0O in o000O0O :
   o000O0O = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
  for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
   IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , '' , '' )
  if 49 - 49: I11i
  if 25 - 25: IiI1i11I . ii * iI11I1II1I1I . I11i / o0o00Oo0O + o0ii1I
  if 68 - 68: I1ii11iIi11i
  if 22 - 22: oooOo0oo0oo
def oo000ii ( url ) :
 if 22 - 22: IiI1i11I * Iii - I1ii11iIi11i * o0o00Oo0O / Ii
 OOooO0Oo0o000 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1iiIIiI1iiI , I11iII , o000O0O , iiiIii in IIi :
  o000O0O = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( i1iiIIiI1iiI )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for O00ooOo , I111IIiii1Ii in i1Iii1i1I :
   OoOiIIi1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I111IIiii1Ii ) )
   for iIIII in OoOiIIi1 :
    if o000O0O in OOooO0Oo0o000 :
     pass
    else :
     Ii1I1i ( o000O0O , O00ooOo , 8043 , I11iII , I11iII , iIIII )
     Ii1IIiI1i ( 'movies' , 'INFO' )
     OOooO0Oo0o000 . append ( o000O0O )
     if 65 - 65: ooOoO0O00 . Ii1I / i1iIi
     if 11 - 11: III1iiIii * i1iIi / i1iIi - oooOo0oo0oo
def OoO0o0OOOO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , i1iIiIi1I , iIIII , I11iI1i1I11I11 , o000O0O in IIi :
  I1I1II1I11 ( o000O0O , url , 10065 , i1iIiIi1I , I11iI1i1I11I11 , iIIII )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 39 - 39: Ii1I / ooOoO0O00 * III1iiIii - oOo0O0Ooo
def OoOoooo0O ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'https://www.youtube.com/results?search_query=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 O0Ooo = OOOII1i1II . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0Ooo )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in next :
  OOOiiiiI = 'https://www.youtube.com' + OOOiiiiI
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , OOOiiiiI , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for I11iII , OOOiiiiI , o000O0O , OoO0O , I111IIiii1Ii in IIi :
  OOO00 . append ( o000O0O )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  IioO0oOOO0Ooo = 'http:' + ( I11iII ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IioO0oOOO0Ooo
  OOOiiiiI = 'http://www.youtube.com' + OOOiiiiI
  Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , I111IIiii1Ii )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for I11iII , OOOiiiiI , o000O0O , OoO0O in IIi :
   print 'im doing it'
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   IioO0oOOO0Ooo = 'http:' + ( I11iII ) . replace ( 'https:' , '' )
   OOOiiiiI = 'http://www.youtube.com' + OOOiiiiI
   if '&' in OOOiiiiI :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( OOOiiiiI )
    O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00OooOo00o in O00OooOo00o :
     o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for o000O0O in o000O0O :
      o000O0O = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OOOiiiiI = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
     for OOOiiiiI in OOOiiiiI :
      OOOiiiiI = 'https://www.youtube.com/w' + OOOiiiiI
     IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
      IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
     Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , Oo00OOOOO , '' )
   elif o000O0O in OOO00 :
    pass
   elif 'user' in OOOiiiiI or 'elete' in o000O0O :
    pass
   elif 'hannel' in OOOiiiiI :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OOOiiiiI
    II11iIiIIIiI = OooOoooOo ( OOOiiiiI )
    Oo0oo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I11iII , OOOiiiiI , o000O0O in Oo0oo :
     if 'outube' in OOOiiiiI or 'list' in OOOiiiiI :
      pass
     elif 'atch' in OOOiiiiI :
      OOOiiiiI = ( OOOiiiiI ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I11iII , 'http:' + I11iII , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , '' )
    if 54 - 54: ooOoO0O00 - Iii % I1ii11iIi11i - oO0o / III1iiIii . o0o00Oo0O
def IiiOoo0o0ooooOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for I11iII , url , o000O0O , OoO0O , I111IIiii1Ii in IIi :
  OOO00 . append ( o000O0O )
  Ii1IIiI1i ( 'tvshows' , 'INFO' )
  IioO0oOOO0Ooo = 'http:' + ( I11iII ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IioO0oOOO0Ooo
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , I111IIiii1Ii )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for I11iII , url , o000O0O , OoO0O in IIi :
   Ii1IIiI1i ( 'tvshows' , 'INFO' )
   IioO0oOOO0Ooo = 'http:' + ( I11iII ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00OooOo00o in O00OooOo00o :
     o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for o000O0O in o000O0O :
      o000O0O = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
      IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
     Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , Oo00OOOOO , '' )
   elif o000O0O in OOO00 :
    pass
   elif 'user' in url or 'elete' in o000O0O :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    Oo0oo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I11iII , url , o000O0O in Oo0oo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I11iII , 'http:' + I11iII , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + OoO0O + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , '' )
    if 79 - 79: i1iIi
    if 40 - 40: I11i + Iii
    if 77 - 77: Ii % III1iiIii + i1IiiiI1iI % ii - Iii
def iIIiiIi ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 19 - 19: I11i
def o00OOOOOo0OOo ( ) :
 ivuesetup . iVueInt ( )
 if 44 - 44: Iii * I11i
def II11ii1I11 ( ) :
 o0oO00o ( )
 return
 if 78 - 78: I1ii11iIi11i * i1IiiiI1iI - ii - oO0o
def o0oO00o ( ) :
 if 83 - 83: i1iIi / oooOo0oo0oo
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 i11iI1 = II1I . getSetting ( id = 'User' )
 i1Ii11ii1I = II1I . getSetting ( id = 'Pass' )
 OO0oI1iii1i = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 oO0ooOoOO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 Ii1IiIiI111IIII1 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 OOOoOooO000oO = "http://piesustv.net:8000/get.php?username=" + i11iI1 + "&password=" + i1Ii11ii1I + "&type=m3u_plus&output=ts"
 o0OOOOOo00 = "http://piesustv.net:8000/xmltv.php?username=" + i11iI1 + "&password=" + i1Ii11ii1I + "&type=m3u_plus&output=ts"
 if 82 - 82: I1ii11iIi11i
 xbmc . executeJSONRPC ( OO0oI1iii1i )
 xbmc . executeJSONRPC ( oO0ooOoOO )
 xbmc . executeJSONRPC ( Ii1IiIiI111IIII1 )
 if 5 - 5: oO0o / oO0o - o0o00Oo0O - i1IiiiI1iI + i1IiiiI1iI
 O0oooOO0Oo0o = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 O0oooOO0Oo0o . setSetting ( id = 'm3uUrl' , value = OOOoOooO000oO )
 O0oooOO0Oo0o . setSetting ( id = 'epgUrl' , value = o0OOOOOo00 )
 O0oooOO0Oo0o . setSetting ( id = 'm3uCache' , value = "false" )
 O0oooOO0Oo0o . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def OoOoOoo0OoO0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 17 - 17: o0ii1I * IIiIiII11i / III1iiIii + iI11I1II1I1I . Iii - o0o00Oo0O
if 70 - 70: o0ii1I * i1i1I1IIii1II - Iii + I1ii11iIi11i % Ii1I - III1iiIii
if 81 - 81: o0o00Oo0O . o0o00Oo0O
def OoO00OooO0 ( ) :
 if 98 - 98: oooOo0oo0oo + o0ii1I
 if 52 - 52: I1ii11iIi11i / OOooOOo - i1IiiiI1iI . IiI1i11I
 if 50 - 50: iI11I1II1I1I - IiI1i11I - Iii
 if 60 - 60: iI11I1II1I1I * i1iIi
 if 71 - 71: OOooOOo % I1ii11iIi11i % i1iIi
 if 34 - 34: Iii / Iii % III1iiIii . OOooOOo / I1ii11iIi11i
 if 99 - 99: i1iIi * oOo0O0Ooo - i1iIi % o0ii1I
 if 40 - 40: oooOo0oo0oo / III1iiIii / iI11I1II1I1I + o0ii1I
 if 59 - 59: Iii * ii + oooOo0oo0oo . iI11I1II1I1I / ooOoO0O00
 if 75 - 75: Iii . oooOo0oo0oo - iI11I1II1I1I * oO0o * IiI1i11I
 if 93 - 93: i1iIi
 if 18 - 18: i1iIi
 if OO0o == "insert_username" :
  OOOooO00OO00O = OoOOooO0O ( )
  Ii11iIII = o0ooOO0OOO00o ( )
  I11 ( 'User' , OOOooO00OO00O )
  I11 ( 'Pass' , Ii11iIII )
  xbmc . executebuiltin ( 'Container.Refresh' )
  OoOoO0ooooO0 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OOOooO00OO00O , Ii11iIII )
  OoOoO0ooooO0 = OooOoooOo ( OoOoO0ooooO0 )
  if OoOoO0ooooO0 == "" :
   IIII1ii1 = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   OOO0O0OOo = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   Iii1 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , IIII1ii1 , OOO0O0OOo , Iii1 )
   OoO00OooO0 ( )
  else :
   IIII1ii1 = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   OOO0O0OOo = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   Iii1 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % OOOooO00OO00O )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , IIII1ii1 , OOO0O0OOo , Iii1 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   OOoO ( )
 else :
  OOoO ( )
def OoOOooO0O ( ) :
 i1IiiI = xbmc . Keyboard ( '' , 'heading' , True )
 i1IiiI . setHeading ( 'Enter Username' )
 i1IiiI . setHiddenInput ( False )
 i1IiiI . doModal ( )
 if ( i1IiiI . isConfirmed ( ) ) :
  O0OOO0 = i1IiiI . getText ( )
  return O0OOO0
 else :
  return False
  if 61 - 61: i1iIi . Ii + i1i1I1IIii1II
  if 8 - 8: iI11I1II1I1I
def o0ooOO0OOO00o ( ) :
 i1IiiI = xbmc . Keyboard ( '' , 'heading' , True )
 i1IiiI . setHeading ( 'Enter Password' )
 i1IiiI . setHiddenInput ( False )
 i1IiiI . doModal ( )
 if ( i1IiiI . isConfirmed ( ) ) :
  O0OOO0 = i1IiiI . getText ( )
  return O0OOO0
 else :
  return False
def oOOo0ooO0 ( ) :
 OOOoOooO000oO = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  ii1i1II11II1i = urllib2 . urlopen ( OOOoOooO000oO )
  print ii1i1II11II1i . getcode ( )
  ii1i1II11II1i . close ( )
  if 95 - 95: Iii + I11i * Ii1I
  pass
  if 85 - 85: Ii . ii - iI11I1II1I1I
 except urllib2 . HTTPError , oOIIiIi :
  print oOIIiIi . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def OOoO ( ) :
 iii ( )
 if 38 - 38: Iii . Iii * i1i1I1IIii1II / ii % i1iIi
 if 80 - 80: oO0o / III1iiIii * oOo0O0Ooo % III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 95 - 95: o0o00Oo0O / Iii . i1IiiiI1iI
 if 17 - 17: Iii
 if 56 - 56: i1iIi * I11i + Iii
 if 48 - 48: III1iiIii * oO0o % i1IiiiI1iI - Iii
def Oo0000OOO0 ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 oOO00oO00O0OO = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 Ooo0O0OO = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 OoOoO0ooooO0 = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 OoOoO0ooooO0 = OooOoooOo ( OoOoO0ooooO0 )
 if not OoOoO0ooooO0 == "" :
  iiI1iiii1Iii = 'https://tinyurl.com/create.php?source=indexpage&url=' + oOO00oO00O0OO + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( iiI1iiii1Iii ) )
  OoOOOOOoOo0 = 'https://tinyurl.com/create.php?source=indexpage&url=' + Ooo0O0OO + '&submit=Make+TinyURL%21&alias='
  oOO00oO00O0OO = OooOoooOo ( iiI1iiii1Iii )
  Ooo0O0OO = OooOoooOo ( OoOOOOOoOo0 )
  xbmc . log ( str ( Ooo0O0OO ) )
  iIi = oOo ( oOO00oO00O0OO , '<div class="indent"><b>' , '</b>' )
  ooOo0o = oOo ( Ooo0O0OO , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % iIi , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % ooOo0o )
 else :
  return
def III ( ) :
 oOOo0ooO0 ( )
 IiiI ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , OoOoO00o00 + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( OOooooO0o0O0 )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + o000O0O + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , OOOiiiiI , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def oO0oo ( url ) :
 open = OooOoooOo ( o00o0o000Oo + url )
 Oooo00OOo = iIiII ( open , '<channel>' , '</channel>' )
 for OooOO in Oooo00OOo :
  if '<playlist_url>' in open :
   o000O0O = oOo ( OooOO , '<title>' , '</title>' )
   IiIi1iI11 = oOo ( OooOO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( o000O0O ) ) . replace ( '?' , '' ) , IiIi1iI11 , 3 , icon , I11iI1i1I11I11 , '' )
  else :
   o000O0O = oOo ( OooOO , '<title>' , '</title>' )
   o000O0O = base64 . b64decode ( o000O0O )
   iio0oo0Oo = oOo ( OooOO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = oOo ( OooOO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   iIIII = oOo ( OooOO , '<description>' , '</description>' )
   iIIII = base64 . b64decode ( iIIII )
   i1i1I1II = oOo ( iIIII , 'PLOT:' , '\n' )
   o0o0oO = oOo ( iIIII , 'CAST:' , '\n' )
   O00o = oOo ( iIIII , 'RATING:' , '\n' )
   o0o0ooOo00 = oOo ( iIIII , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   o0o0ooOo00 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( o0o0ooOo00 )
   OO00oO0OoO0o = oOo ( iIIII , 'DURATION_SECS:' , '\n' )
   I11I111i1I1 = oOo ( iIIII , 'GENRE:' , '\n' )
   iii1O0Ooo0O ( str ( o000O0O ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , iio0oo0Oo , I11iI1i1I11I11 , i1i1I1II , str ( o0o0ooOo00 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( o0o0oO ) . split ( ) , O00o , OO00oO0OoO0o , I11I111i1I1 )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 18 - 18: ooOoO0O00
i1i1Ii1IiIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
I1IIii11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 22 - 22: i1iIi / i1iIi - o0ii1I % Iii . oooOo0oo0oo + III1iiIii
def OooO00oo0O0 ( ) :
 OOOoOooO000oO = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  ii1i1II11II1i = urllib2 . urlopen ( OOOoOooO000oO )
  print ii1i1II11II1i . getcode ( )
  ii1i1II11II1i . close ( )
  if 10 - 10: III1iiIii / ii
  pass
  if 50 - 50: Ii - ii . i1i1I1IIii1II + o0o00Oo0O . ooOoO0O00
 except urllib2 . HTTPError , oOIIiIi :
  print oOIIiIi . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 91 - 91: I11i . IiI1i11I % I1ii11iIi11i - IiI1i11I . i1i1I1IIii1II % Ii
 OOOiiiiI = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 iIiO0O ( OOOiiiiI , I1IIii11 + "uide.xml" )
 if 71 - 71: Ii1I + oO0o
 oOOOoo00 = open ( i1i1Ii1IiIII , 'r+' )
 input = open ( i1i1Ii1IiIII ) . read ( ) . decode ( 'UTF-8' )
 ii1oooO0o0oOoO = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 oOOOoo00 . write ( ii1oooO0o0oOoO )
 oOOOoo00 . truncate ( )
 oOOOoo00 . close ( )
 I11iii ( )
 if 11 - 11: i1i1I1IIii1II + i1IiiiI1iI . III1iiIii * ii - Ii1I - oooOo0oo0oo
def I11iii ( ) :
 open = OooOoooOo ( I1Ii1 )
 all = iIiII ( open , '{"num' , 'direct' )
 for OooOO in all :
  if '"tv_archive":1' in OooOO :
   o000O0O = oOo ( OooOO , '"epg_channel_id":"' , '"' )
   iio0oo0Oo = oOo ( OooOO , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = oOo ( OooOO , 'stream_id":"' , '"' )
   o000O0O = o000O0O . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( o000O0O , id , 90027 , iio0oo0Oo , I11iI1i1I11I11 , o000O0O )
   if 67 - 67: Iii % Ii . iI11I1II1I1I * oOo0O0Ooo - Iii + o0ii1I
   if 48 - 48: Ii1I
def o0oi1I1I1I ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 iII1III = open ( i1i1Ii1IiIII )
 O0oo0oO00o = ElementTree . parse ( iII1III )
 I1ii111i1ii1 = "apples"
 import datetime as dt
 from datetime import time
 o0Ii11iIiiI = datetime . now ( ) - timedelta ( days = 5 )
 III11I = str ( o0Ii11iIiiI )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 o000 = O0oo0oO00o . findall ( "programme" )
 for i11ii1 in o000 :
  if name in i11ii1 . attrib . get ( 'channel' ) :
   Ii111I11 = i11ii1 . attrib . get ( 'start' )
   Oo0O0oo , o0O0 , oO0o0 = Ii111I11 . partition ( ' +' )
   III11I = str ( III11I ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   o0o0ooOo00 , ooO , Oo0OOo = Ii111I11 . partition ( '2017' )
   oOoO0 = i11ii1 . find ( 'title' ) . text + Ii111I11
   Oo0OOo = Oo0OOo [ : - 6 ]
   if Oo0O0oo > III11I :
    if Oo0O0oo < I1IIIii :
     Iii1II1ii = Oo0O0oo
     Iii1II1ii = Iii1II1ii [ : 4 ] + '/' + Iii1II1ii [ 4 : ]
     Oo0O0oo = Oo0O0oo [ : 4 ] + '-' + Oo0O0oo [ 4 : ]
     Iii1II1ii = Iii1II1ii [ : 7 ] + '/' + Iii1II1ii [ 7 : ]
     Oo0O0oo = Oo0O0oo [ : 7 ] + '-' + Oo0O0oo [ 7 : ]
     Iii1II1ii = Iii1II1ii [ : 10 ] + ' - ' + Iii1II1ii [ 10 : ]
     Oo0O0oo = Oo0O0oo [ : 10 ] + ':' + Oo0O0oo [ 10 : ]
     Iii1II1ii = Iii1II1ii [ : 15 ] + ':' + Iii1II1ii [ 15 : ]
     Oo0O0oo = Oo0O0oo [ : 13 ] + '-' + Oo0O0oo [ 13 : ]
     Iii1II1ii = Iii1II1ii [ : - 2 ]
     Oo0O0oo = Oo0O0oo [ : - 2 ]
     ooOo00 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( Oo0O0oo ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     I1ii111i1ii1 = ooOo00 + str ( Oo0O0oo ) + "&duration=240"
     Iii1II1ii = '[COLOR blue]%s - [/COLOR]' % Iii1II1ii
     oOoO0 = str ( Iii1II1ii ) + i11ii1 . find ( 'title' ) . text
     iIIII = i11ii1 . find ( 'desc' ) . text
     Ii1I1i ( oOoO0 , ooOo00 , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , iIIII )
def OO0III ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 iI1iiiIiii = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 iI1iiiIiii . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 iI1iiiIiii . setProperty ( 'IsPlayable' , 'true' )
 iI1iiiIiii . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1iiiIiii )
def iIiO0O ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 OoO0o = time . time ( )
 urllib . urlretrieve ( url , dest , lambda OO0o0O0O0O0 , iI11IiIiiII1 , I11iii1i : ii1i1Iii ( OO0o0O0O0O0 , iI11IiIiiII1 , I11iii1i , o0oOoO00o , OoO0o ) )
def ii1i1Iii ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  oO00oO00O0Oo = min ( numblocks * blocksize * 100 / filesize , 100 )
  OO0o0o0oo = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  iIiII1 = numblocks * blocksize / ( time . time ( ) - start_time )
  if iIiII1 > 0 :
   i111iii1I1 = ( filesize - numblocks * blocksize ) / iIiII1
  else :
   i111iii1I1 = 0
  iIiII1 = iIiII1 / 1024
  iiIiII1 = iIiII1 / 1024
  ii111iI = float ( filesize ) / ( 1024 * 1024 )
  ii11I1 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( OO0o0o0oo )
  oOIIiIi = '[COLOR white]Speed:  %.02f Mb/s ' % iiIiII1 + '[/COLOR]'
  dp . update ( oO00oO00O0Oo , ii11I1 , oOIIiIi )
 except :
  oO00oO00O0Oo = 100
  dp . update ( oO00oO00O0Oo )
 if dp . iscanceled ( ) :
  I1I = xbmcgui . Dialog ( )
  I1I . ok ( "GenieTv" , 'The download was cancelled.' )
  if 76 - 76: oOo0O0Ooo
  sys . exit ( )
  dp . close ( )
  if 42 - 42: ii % I1ii11iIi11i % oooOo0oo0oo
def iIi1Ii1111i ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  i1iooO0oO0o ( )
  if 22 - 22: I11i + I1ii11iIi11i . i1iIi + Ii1I * IiI1i11I . Ii
  if 90 - 90: oooOo0oo0oo * OOooOOo - I1ii11iIi11i + I11i
  if 53 - 53: ii . ii + I11i - IiI1i11I + oooOo0oo0oo
  if 44 - 44: i1IiiiI1iI - III1iiIii
  if 100 - 100: i1i1I1IIii1II . oO0o - o0ii1I + o0o00Oo0O * oO0o
  if 59 - 59: IIiIiII11i
  if 43 - 43: I1ii11iIi11i + ii
  if 47 - 47: i1iIi
def i1iooO0oO0o ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for OOOiiiiI in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def o00oOoo0o00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iIiiI11II11i = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 O0oOOo0o = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IIIIiIiIi1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 O0o0oO = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1III11iiii11i1 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 Iiiii1IIiI = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 oOO = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 o00OoO0o0 = o0OOOoO0ooOOOo0 ( )
 o0oOOO = IIi11 ( )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iIiiI11II11i :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in O0oOOo0o :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in O0o0oO :
  dt = datetime . fromtimestamp ( float ( O0o0oO [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   oOOo000oOoO0 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IIIIiIiIi1 :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1III11iiii11i1 :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Iiiii1IIiI :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOO :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + o00OoO0o0 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + o0oOOO , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 78 - 78: i1IiiiI1iI / i1i1I1IIii1II - iI11I1II1I1I - OOooOOo
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 60 - 60: IIiIiII11i
def oO0OOoo ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 oOo00oooOO ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 4 - 4: OOooOOo * I11i - Iii . ii * Ii . I11i
def IiiIiI1IIi1IIIii ( data ) :
 OOO0o = len ( data ) % 4
 if 80 - 80: III1iiIii + Iii + i1i1I1IIii1II % oO0o - I1ii11iIi11i - i1i1I1IIii1II
 if 7 - 7: I11i . Ii1I
 if 30 - 30: i1iIi - Ii + oOo0O0Ooo / I1ii11iIi11i % o0o00Oo0O
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 if 47 - 47: Ii1I * i1i1I1IIii1II + iI11I1II1I1I - i1i1I1IIii1II / III1iiIii
 if 86 - 86: III1iiIii
 if OOO0o != 0 :
  data += b'=' * ( 4 - OOO0o )
 return base64 . decodestring ( data )
def oOo ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : Iii1I = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : Iii1I = ''
 else :
  try : Iii1I = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : Iii1I = ''
 return Iii1I
 if 100 - 100: ii . I1ii11iIi11i / Ii1I
 if 29 - 29: i1iIi * IIiIiII11i * oO0o * III1iiIii
def iIiII ( text , start_with , end_with ) :
 Iii1I = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return Iii1I
def o0OOOoO0ooOOOo0 ( ) :
 ooo00o0OO = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 ooo00o0OO . connect ( ( '8.8.8.8' , 0 ) )
 ooo00o0OO = ooo00o0OO . getsockname ( ) [ 0 ]
 return ooo00o0OO
 if 32 - 32: oooOo0oo0oo + IiI1i11I + iI11I1II1I1I * I1ii11iIi11i
def IIi11 ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 o00OoO0o0 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( o00OoO0o0 . group ( ) )
OoOoO00o00 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
I1Ii1 = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
ooiIii1I1111 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
I1iIiiiIi1111I = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
iII1i1ii = '&action=get_live_categories'
i1I1ii1i = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
OOooooO0o0O0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 2 - 2: ii % iI11I1II1I1I
o00o0o000Oo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
I11iIiI1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
i1I1iiii1Ii11 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
IiIIIIi = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 51 - 51: IIiIiII11i . i1i1I1IIii1II . oO0o % IIiIiII11i
def III1I1ii ( ) :
 oOOo0ooO0 ( )
 open = OooOoooOo ( i1I1iiii1Ii11 )
 Oooo00OOo = iIiII ( open , '<channel>' , '</channel>' )
 for OooOO in Oooo00OOo :
  o000O0O = oOo ( OooOO , '<title>' , '</title>' )
  o000O0O = base64 . b64decode ( o000O0O )
  IiIi1iI11 = oOo ( OooOO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + o000O0O + '[/COLOR]' , IiIi1iI11 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 4 - 4: iI11I1II1I1I . ooOoO0O00
def Oo00oo ( url ) :
 open = OooOoooOo ( IiIIIIi + url )
 Oooo00OOo = iIiII ( open , '<channel>' , '</channel>' )
 for OooOO in Oooo00OOo :
  o000O0O = oOo ( OooOO , '<title>' , '</title>' )
  o000O0O = base64 . b64decode ( o000O0O )
  xbmc . log ( str ( o000O0O ) )
  iio0oo0Oo = oOo ( OooOO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  IiIi1iI11 = oOo ( OooOO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  iIIII = oOo ( OooOO , '<description>' , '</description>' )
  iIIII = base64 . b64decode ( iIIII )
  oO0oO = '('
  o0ooo = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , IiIi1iI11 , 222 , iio0oo0Oo , I11iI1i1I11I11 , ( '[COLOR' + ooOoOoo0O + ']' + iIIII + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o0ooo , '[COLORsteelblue]' ) . replace ( oO0oO , '[COLORorangered]' ) )
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / oooOo0oo0oo . Ii1I * i1iIi
def oo0OOoooo0O0 ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( i1I1ii1i + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , type , i1iiIIiI1iiI , ooOo0OoO in IIi :
  I11Ii111I = ( I1iIiiiIi1111I + i1iiIIiI1iiI + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , I11Ii111I , 222 , ( ooOo0OoO ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
def oOoO000 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iiI1iI1I , Oo00o00Oo in IIi :
  if name == iiI1iI1I :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + Oo00o00Oo , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def i1I1i1I111 ( name ) :
 oOo00OO0ooOOO = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , I11iII , OOOiiiiI in IIi :
  OOOiiiiI = ( OOOiiiiI ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( OOOiiiiI ) . strip ( ) , 222 , I11iII , I11iII , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 44 - 44: o0ii1I * i1iIi / OOooOOo
  if 69 - 69: i1iIi . oooOo0oo0oo - oOo0O0Ooo
  if 29 - 29: Ii . Ii1I / oOo0O0Ooo . oooOo0oo0oo + Ii
  if 26 - 26: III1iiIii / o0ii1I - ii
  if 9 - 9: ii * Ii1I
  if 9 - 9: I1ii11iIi11i + IiI1i11I
  if 64 - 64: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo
  if 57 - 57: Ii1I / ii % Ii1I . o0o00Oo0O / Ii1I
  if 63 - 63: III1iiIii + iI11I1II1I1I + oOo0O0Ooo + i1IiiiI1iI
  if 72 - 72: oO0o + Ii + Ii1I
  if 96 - 96: i1i1I1IIii1II % ooOoO0O00 / I11i
  if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + IiI1i11I
def oOoO00o ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , OOOiiiiI , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 88 - 88: o0o00Oo0O . i1i1I1IIii1II % oOo0O0Ooo
  if 10 - 10: oOo0O0Ooo + o0o00Oo0O
  if 75 - 75: o0o00Oo0O % iI11I1II1I1I / OOooOOo % oooOo0oo0oo / III1iiIii
zip = oo00 . getSetting ( 'zip' )
iiI1iiIiiiI1I = xbmc . translatePath ( os . path . join ( zip ) )
def i111I1 ( ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 69 - 69: oO0o - ii - oooOo0oo0oo % Iii / OOooOOo - IIiIiII11i
  if 67 - 67: oooOo0oo0oo + oooOo0oo0oo + oO0o . Ii + Ii1I + Ii
  if 31 - 31: i1i1I1IIii1II * i1IiiiI1iI . OOooOOo * Iii
def I1II1I ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  i111I1 ( )
  I1I11i = open ( url ) . read ( )
  o0OOOO = os . path . join ( iiI1iiIiiiI1I , description . split ( 'Your ' ) [ 1 ] )
  oOOOoo00 = open ( o0OOOO , mode = 'w' )
  oOOOoo00 . write ( I1I11i )
  oOOOoo00 . close ( )
 else :
  if 'guisettings.xml' in description :
   OooOO = open ( os . path . join ( iiI1iiIiiiI1I , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii1I = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( Iii1I ) . findall ( OooOO )
   for type , OOoo0OOOo0o , iI1111i1i11Ii in IIi :
    iI1111i1i11Ii = iI1111i1i11Ii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OOoo0OOOo0o , iI1111i1i11Ii ) )
  else :
   o0OOOO = os . path . join ( url )
   I1I11i = open ( os . path . join ( iiI1iiIiiiI1I , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOOoo00 = open ( o0OOOO , mode = 'w' )
   oOOOoo00 . write ( I1I11i )
   oOOOoo00 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 62 - 62: IiI1i11I
 if 8 - 8: IiI1i11I - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
 if 26 - 26: ooOoO0O00 / IiI1i11I . IiI1i11I
 if 20 - 20: oooOo0oo0oo - IiI1i11I / I1ii11iIi11i * oO0o
def o00O ( ) :
 IIIIIiiI = 1
 i111I1 ( )
 i1iIii = xbmc . translatePath ( os . path . join ( iiI1iiIiiiI1I , 'Build Backup' , 'Full Backup' , '' ) )
 O0o00 = xbmc . translatePath ( os . path . join ( iiI1iiIiiiI1I , 'Build Backup' , 'my_full_backup.zip' ) )
 I1IIi1iI1iiI = xbmc . translatePath ( os . path . join ( iiI1iiIiiiI1I , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( i1iIii ) :
  os . makedirs ( i1iIii )
 iiI11I1ii11 = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iiI11I1ii11 ) : return False , 0
 O0OoO0oooOO = iiI11I1ii11
 i1ii11I111Ii = xbmc . translatePath ( os . path . join ( i1iIii , O0OoO0oooOO + '.zip' ) )
 OOoO00O = [ 'plugin.video.GenieTv' ]
 iio00O0o00oo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iIiiII = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 iII1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o00oOOo0Oo = "Creating full backup of existing build"
 Oooo0o0oO = "Creating Community Build"
 o0OOoOooO0ooO = "Archiving..."
 IiiiIi = ""
 IiI111 = "Please Wait"
 OO0OO00ooO0 ( oOo0oooo00o , i1ii11I111Ii , Oooo0o0oO , o0OOoOooO0ooO , IiiiIi , IiI111 , iIiiII , iII1I )
 time . sleep ( 1 )
 OOOOOoO00oo00 = xbmc . translatePath ( os . path . join ( i1iIii , O0OoO0oooOO + '_guisettings.zip' ) )
 iIIIII11 = zipfile . ZipFile ( OOOOOoO00oo00 , mode = 'w' )
 try :
  iIIIII11 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iIIIII11 . close ( )
 if IIIIIiiI == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + O0o00 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + i1ii11I111Ii + '[/COLOR]' )
  if 61 - 61: Ii1I
def OO0OO00ooO0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iIII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 ooo0oOooo0o0 = len ( sourcefile )
 IIii1Ii1i1ii1 = [ ]
 oOOoOOooO0 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for Iii1IIII1Iii , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( sourcefile ) :
  for file in IIIIIIiIIIi1iii1 :
   oOOoOOooO0 . append ( file )
 iii11III1I = len ( oOOoOOooO0 )
 for Iii1IIII1Iii , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( sourcefile ) :
  OOOOOOo0o0O0o [ : ] = [ oO0oO0O for oO0oO0O in OOOOOOo0o0O0o if oO0oO0O not in exclude_dirs ]
  IIIIIIiIIIi1iii1 [ : ] = [ oOOOoo00 for oOOOoo00 in IIIIIIiIIIi1iii1 if oOOOoo00 not in exclude_files ]
  for file in IIIIIIiIIIi1iii1 :
   IIii1Ii1i1ii1 . append ( file )
   ooooO = len ( IIii1Ii1i1ii1 ) / float ( iii11III1I ) * 100
   o0oOoO00o . update ( int ( ooooO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O000oooO0 = os . path . join ( Iii1IIII1Iii , file )
   if not 'temp' in OOOOOOo0o0O0o :
    if not 'plugin.program.originwizard' in OOOOOOo0o0O0o :
     import time
     oOO00 = '01/01/1980'
     oO0o00 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O000oooO0 ) ) )
     if oO0o00 > oOO00 :
      iIII . write ( O000oooO0 , O000oooO0 [ ooo0oOooo0o0 : ] )
 iIII . close ( )
 o0oOoO00o . close ( )
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
 if 84 - 84: iI11I1II1I1I + ii
def Oo0OOOOOOO0oo ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 if 15 - 15: i1iIi % I11i / i1i1I1IIii1II - IIiIiII11i . iI11I1II1I1I
def ii1111Iii11i ( ) :
 iii ( )
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  OoOo0oOooOoOO ( )
 if O0O0ooOOO == 1 :
  iII1111III1I ( )
 if O0O0ooOOO == 2 :
  OOooo00 ( )
 if O0O0ooOOO == 3 :
  OoOoooo0O ( )
  if 91 - 91: o0ii1I - IiI1i11I . ooOoO0O00 . Ii1I * I11i % IiI1i11I
  if 30 - 30: Iii
  if 85 - 85: IIiIiII11i + i1iIi * Iii
  if 12 - 12: o0ii1I . oOo0O0Ooo % I11i
  if 28 - 28: o0ii1I - oOo0O0Ooo % oO0o * i1IiiiI1iI
  if 80 - 80: oooOo0oo0oo * III1iiIii
  if 4 - 4: iI11I1II1I1I . i1IiiiI1iI + IIiIiII11i % ii
  if 82 - 82: ii / i1iIi * Iii * o0o00Oo0O . Ii1I
  if 21 - 21: IIiIiII11i + I1ii11iIi11i
def OOooooO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0O0ooOOO == 1 :
   from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if O0O0ooOOO == 2 :
   oOoo00 ( )
  if O0O0ooOOO == 3 :
   IIiIi ( )
  if O0O0ooOOO == 4 :
   I1I1IIiiI1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0O0ooOOO == 5 :
   oooOOO0o0O0 ( )
  if O0O0ooOOO == 6 :
   iiiI1IiI ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0O0ooOOO == 7 :
   Ii111IIIIii ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0O0ooOOO == 8 :
   O00oIii1iIIiii1ii ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0O0ooOOO == 9 :
   Ii1iii11I ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RaysRavers Radio[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 1125 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ThunderStruck[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 1127 , iiIi1IIiIi + 'Thunder.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
   if 2 - 2: ii - o0ii1I % i1i1I1IIii1II / oOo0O0Ooo / I11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  if 3 - 3: IIiIiII11i / oooOo0oo0oo
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  if 48 - 48: i1iIi . Ii1I
  if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - i1iIi / I1ii11iIi11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 24 - 24: i1i1I1IIii1II - IiI1i11I / i1iIi
def iIiiII1Ii1ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   iIIi1 ( )
  if O0O0ooOOO == 1 :
   OOoOooOoOOOoo ( )
  if O0O0ooOOO == 2 :
   i1I1i111Ii ( )
  if O0O0ooOOO == 3 :
   OoOo0O00 ( OOOiiiiI )
  if O0O0ooOOO == 4 :
   iI1i1iI1iI ( OOOiiiiI )
  if O0O0ooOOO == 5 :
   oooO ( )
  if O0O0ooOOO == 6 :
   I1IIiIi ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0O0ooOOO == 7 :
   OOOOoOoO ( )
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
  if 72 - 72: OOooOOo / i1IiiiI1iI * III1iiIii % iI11I1II1I1I
  if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * oooOo0oo0oo / I11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 34 - 34: OOooOOo
 if 16 - 16: ooOoO0O00 - i1IiiiI1iI - IIiIiII11i
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
 if 83 - 83: oOo0O0Ooo - oO0o - I11i / o0o00Oo0O - Iii . IIiIiII11i
 if 27 - 27: o0ii1I
def O0Oo0 ( ) :
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
 if 88 - 88: ii + i1iIi % IiI1i11I . ii . III1iiIii
def oO00O0 ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 33 - 33: I11i . oooOo0oo0oo + I11i / Ii1I . I1ii11iIi11i + OOooOOo
def I1111111 ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 57 - 57: oooOo0oo0oo % oO0o - oOo0O0Ooo
 if 3 - 3: oooOo0oo0oo + ooOoO0O00 % Ii1I
 if 100 - 100: ii + Ii % I11i + oOo0O0Ooo . I1ii11iIi11i . IIiIiII11i
def OoiiI11111II ( ) :
 iii ( )
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  I1ii1i11iI1 ( )
 if O0O0ooOOO == 0 :
  IiOOo0 ( OOOiiiiI )
 if O0O0ooOOO == 0 :
  o0O0O0O00o ( OOOiiiiI )
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
  if 75 - 75: IIiIiII11i . oOo0O0Ooo + oooOo0oo0oo - OOooOOo - o0o00Oo0O . Iii
  if 19 - 19: o0ii1I * ooOoO0O00 % o0o00Oo0O + Iii
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 25 - 25: i1IiiiI1iI - o0ii1I / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
def Ii1i ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for I11iII , o000O0O in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , I11iII , I11iII , '' )
 Ii1IIiI1i ( 'tvshows' , 'INFO' )
 if 49 - 49: i1i1I1IIii1II + i1i1I1IIii1II + Ii % IiI1i11I
def I1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO00o0oOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 5 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 66 - 66: Ii1I . I1ii11iIi11i
def I1ii1i11iI1 ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 38 - 38: Iii . III1iiIii - oO0o . oOo0O0Ooo
def ooOoo0OOOO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oO0O000oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 38 - 38: oOo0O0Ooo % III1iiIii * o0ii1I
def O00OoO0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo00oo00o00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 1 - 1: III1iiIii
def iiii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 92 - 92: Iii % o0o00Oo0O % o0ii1I . o0ii1I . III1iiIii
def OOoO0Oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 61 - 61: oOo0O0Ooo + i1i1I1IIii1II % i1IiiiI1iI % iI11I1II1I1I - ii
def IiOOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iIIiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 40 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 4 - 4: ii + IiI1i11I % o0o00Oo0O + iI11I1II1I1I % IiI1i11I * Ii
def III1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1IIIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 5 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 79 - 79: I1ii11iIi11i - ii % i1IiiiI1iI + ii - Iii % OOooOOo
def oOOo0O00o ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  iII ( )
 if O0O0ooOOO == 1 :
  OOo0O ( )
 if O0O0ooOOO == 2 :
  iiOo0ooo ( )
  if 73 - 73: IIiIiII11i + oooOo0oo0oo * IiI1i11I / IiI1i11I
  if 74 - 74: o0o00Oo0O + iI11I1II1I1I + i1i1I1IIii1II * III1iiIii
  if 39 - 39: i1IiiiI1iI . oO0o % i1iIi . oooOo0oo0oo / IiI1i11I * oO0o
  if 12 - 12: oOo0O0Ooo / I11i
def OOo0O ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I1i11 )
 for OOOiiiiI , oOO0O00o0O0 in IIi :
  IiI11i1IIiiI ( 'Android Apps' + oOO0O00o0O0 , 'https://www.apkfiles.com' + OOOiiiiI , 30035 , iiIi1IIiIi + 'apps.png' )
 for OOOiiiiI , oOO0O00o0O0 in i1Iii1i1I :
  IiI11i1IIiiI ( 'Android Games' + oOO0O00o0O0 , 'https://www.apkfiles.com' + OOOiiiiI , 30035 , iiIi1IIiIi + 'GAMES.png' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def ooOooO ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if '/cat' in url :
   IiI11i1IIiiI ( ( o000O0O ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def oooo ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if '/app' in url :
   IiI11i1IIiiI ( ( o000O0O ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def IIIiI1iIIII ( url ) :
 I1i11 = OooOoooOo ( url )
 IiIi1iI11 = url
 if "page=" in str ( url ) :
  IiIi1iI11 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  if 'apk' in url :
   Ii1I1i ( ( o000O0O ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + I11iII )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , IiIi1iI11 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def o0oo00OOOo ( name , url ) :
 I1i11 = ii1IIIIiI11 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I1i11 )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  oo0oOi1i1IIi ( name , url , 'Brackets' )
def iiOo0ooo ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'https://www.apkfiles.com/search?q=' + ( ooO0000o00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0Ooo = OOOII1i1II . lower ( )
 IIIiI1iIIII ( O0Ooo )
 if 93 - 93: i1i1I1IIii1II
def o0Oo ( url ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( III1IIiIi1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , o000O0O + '.apk' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 97 - 97: I11i / III1iiIii + OOooOOo + oO0o % i1IiiiI1iI
def iIIi1II1 ( url ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , o000O0O + '.mp4' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 42 - 42: iI11I1II1I1I - i1iIi - Iii - i1IiiiI1iI
 if 33 - 33: OOooOOo - o0o00Oo0O
def III11iI1i11i ( name , url , description ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , name )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IIiIOOoOo0oO0oo00 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIiIOOoOo0oO0oo00
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IIiIOOoOo0oO0oo00 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 100 - 100: oO0o . Iii / o0ii1I . I11i - OOooOOo . Iii
 if 30 - 30: o0ii1I % Iii + I11i
 if 65 - 65: iI11I1II1I1I . IiI1i11I / o0ii1I
 if 12 - 12: oOo0O0Ooo + i1IiiiI1iI
 if 80 - 80: i1i1I1IIii1II . o0o00Oo0O
def iII ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , OOOiiiiI , ooOo0OoO , I11iI1i1I11I11 , oooOOO0oooOO in IIi :
  Ii1I1i ( o000O0O , OOOiiiiI , 80003 , ooOo0OoO , iiIi1IIiIi + 'APKToolsB.png' , oooOOO0oooOO )
def IIIi1iiIIiiiI ( apk , ret = None ) :
 if apk == "kodi" :
  I1IIiIi1iI = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( I1IIiIi1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   oOo0 = IIi [ 0 ] [ 0 ]
   O0OoO0oooOO = IIi [ 0 ] [ 1 ]
   Iiii11 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oOo0 , O0OoO0oooOO )
  if ret == 'version' : return oOo0
  else : return Iiii11
 elif apk == "spmc" :
  o00000O = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( o00000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  oOo0 = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  Iiii11 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oOo0 , oOo0 )
  if ret == 'version' : return oOo0
  else : return Iiii11
def oo0oOi1i1IIi ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  iIiiiII11 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iIiiiII11 : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iIii1i1Ii = name
  if iIiiiII11 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OooooOoooO ( url ) == True : ooo00Oo0 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iIii1i1Ii , '' , 'Please Wait' )
   Ii1IIiI1io0O00Oo0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( Ii1IIiI1io0O00Oo0 )
   except : pass
   downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iIIIII11 = zipfile . ZipFile ( Ii1IIiI1io0O00Oo0 )
    for file in iIIIII11 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as oOOOoo00 :
       III1iIii = file . split ( '/' ) [ 1 ]
       oOOOoo00 . write ( iIIIII11 . read ( file ) )
       xbmc . sleep ( 500 )
       oOOOoo00 . close ( )
       try :
        os . remove ( Ii1IIiI1io0O00Oo0 )
       except :
        pass
       Ii1IIiI1io0O00Oo0 = os . path . join ( i1iIIi1 , III1iIii )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1IIiI1io0O00Oo0 + '")' )
  else : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 9 - 9: ooOoO0O00 - OOooOOo
 if 57 - 57: iI11I1II1I1I * o0ii1I * IiI1i11I / i1i1I1IIii1II
 if 46 - 46: o0ii1I
 if 61 - 61: I11i / i1iIi - IIiIiII11i
def oOoO0o0Ooo ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for OOOiiiiI , o000O0O in IIi :
  OOOiiiiI = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + OOOiiiiI )
  iIIIi11iIiIii ( ( o000O0O ) . replace ( '_' , ' ' ) , OOOiiiiI )
  if 61 - 61: ii . o0ii1I % i1i1I1IIii1II * ii
def iIIIi11iIiIii ( name , url ) :
 if OO ( ) == 'android' :
  iIiiiII11 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iIiiiII11 : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iIii1i1Ii = name
  if iIiiiII11 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OooooOoooO ( url ) == True : ooo00Oo0 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iIii1i1Ii , '' , 'Please Wait' )
   Ii1IIiI1io0O00Oo0 = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( Ii1IIiI1io0O00Oo0 )
   except : pass
   downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1IIiI1io0O00Oo0 + '")' )
  else : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : ooo00Oo0 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 96 - 96: o0ii1I - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if 75 - 75: I1ii11iIi11i + o0ii1I + oO0o
def o00o0o0oOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 5 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 33 - 33: ooOoO0O00 / III1iiIii - ooOoO0O00 . oOo0O0Ooo
 if 48 - 48: i1iIi + oooOo0oo0oo . i1IiiiI1iI % IIiIiII11i + i1i1I1IIii1II
def OOOO0OOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 30015 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 38 - 38: i1i1I1IIii1II
def iii1i1Iiiiiii ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IiIi1II111I = url
 I11iII = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for i1iiIIiI1iiI , o000O0O in IIi :
  if '.mp4' in o000O0O :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + i1iiIIiI1iiI , 222 , I11iII , fanart , '' )
  if 'description' in o000O0O :
   Ii1I1i ( 'Read Description' , url + '/' + i1iiIIiI1iiI , 30017 , I11iII , fanart , '' )
  if 'images' in o000O0O :
   I1I1II1I11 ( 'View Images' , url + '/' + i1iiIIiI1iiI , 30018 , I11iII , fanart , '' )
  if 'url' in o000O0O :
   Ii1I1i ( 'Install Build On Android' , url + '/' + i1iiIIiI1iiI , 30016 , I11iII , fanart , '' )
  if 'url' in o000O0O :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + i1iiIIiI1iiI , 30019 , I11iII , fanart , '' )
 Ii1IIiI1i ( 'movies' , 'INFO' )
 if 58 - 58: I11i / Ii / o0o00Oo0O % Iii % oOo0O0Ooo
def O0oOOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oooOOOoO0O ( url )
  if 2 - 2: I11i . o0ii1I % OOooOOo
def OO00O00o0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  OOoO00OoOOO ( url )
  if 70 - 70: Ii + Ii - Ii % oO0o / IIiIiII11i
def III1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for O0OOO0 in IIi :
  o0OIiII ( 'Description:' , O0OOO0 )
  if 36 - 36: ii * ooOoO0O00 % Ii / IiI1i11I - I11i % i1iIi
def iiiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for i1iiIIiI1iiI , o000O0O in IIi :
  if 'png' in o000O0O :
   Ii1I1i ( 'image' , '' , '' , url + '/' + i1iiIIiI1iiI , url + '/' + i1iiIIiI1iiI , '' )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 28 - 28: I1ii11iIi11i / III1iiIii . IiI1i11I + oO0o + Iii % I1ii11iIi11i
def iI1i ( name , url , description ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , name + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oooO ( )
 if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % i1i1I1IIii1II + oOo0O0Ooo % i1iIi / o0ii1I
 if 36 - 36: OOooOOo . Ii
def OOoO00OoOOO ( url ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 i111iIi1i1II1 ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIi1 ( )
 if 81 - 81: I1ii11iIi11i * IiI1i11I * oO0o
def oooOOOoO0O ( url ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 i111iIi1i1II1 ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIi1 ( )
 if 85 - 85: o0o00Oo0O * i1i1I1IIii1II
def iiIiiiIii11i1 ( name , url , description ) :
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii1IIiI1io0O00Oo0 = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIIi1 ( )
 if 87 - 87: oO0o + ii . i1iIi * Iii
def OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def ooo ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : oOOOoo00 = open ( oO , 'w' ) ; oOOOoo00 . close ( )
 with open ( oO , 'a' ) as oOOOoo00 :
  oooOoO0oo0o0 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOOoo00 . write ( oooOoO0oo0o0 . rstrip ( '\r\n' ) + '\n' )
def iIIi1 ( ) :
 O0O0ooOOO = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0O0ooOOO == 0 : return
 elif O0O0ooOOO == 1 : pass
 O0ooooOOoo0O = OO ( )
 ooo ( "Platform: " + str ( O0ooooOOoo0O ) )
 os . _exit ( 1 )
 ooo ( "Force close failed!  Trying alternate methods." )
 if O0ooooOOoo0O == 'osx' :
  ooo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0ooooOOoo0O == 'linux' :
  ooo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0ooooOOoo0O == 'android' :
  ooo ( "############ try android force close #################" )
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
 elif O0ooooOOoo0O == 'windows' :
  ooo ( "############ try windows force close #################" )
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
  ooo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  ooo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 4 - 4: Ii * Ii1I + ii - III1iiIii . i1iIi . iI11I1II1I1I
  if 48 - 48: I11i * i1i1I1IIii1II . oOo0O0Ooo - i1IiiiI1iI + oooOo0oo0oo . I1ii11iIi11i
  if 62 - 62: Iii + ii * iI11I1II1I1I / ooOoO0O00 * o0o00Oo0O
def o0O0O0O00o ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( url ) :
  for file in IIIIIIiIIIi1iii1 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OooOO = open ( ( os . path . join ( iiiiIi11II11 , file ) ) ) . read ( )
    iI1i1Iiii = OooOO . replace ( oOo0oooo00o , 'special://home/' )
    oOOOoo00 = open ( ( os . path . join ( iiiiIi11II11 , file ) ) , mode = 'w' )
    oOOOoo00 . write ( str ( iI1i1Iiii ) )
    oOOOoo00 . close ( )
 iIIi1 ( )
 if 15 - 15: o0ii1I
def oOoo00 ( ) :
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 17 - 17: OOooOOo - oOo0O0Ooo
def OOoOOoo0 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def oo0OOO0OOoOO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def oOoO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , I11iII , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , I11iII )
def II1i1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I1i11 )
 for url in IIi :
  O0oOOoooOO0O ( url )
def o0o0oo0OOo0O0 ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O
 iIIiiII11i1I1 = 'https://www.radionomy.com/en/search/index?query=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( iIIiiII11i1I1 )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OOOiiiiI , 70005 , I11iII )
  if 28 - 28: IIiIiII11i * i1iIi * OOooOOo * i1IiiiI1iI . IIiIiII11i . Ii1I
  if 32 - 32: i1iIi - oO0o . IiI1i11I . IiI1i11I % ooOoO0O00 * o0ii1I
def oooOOO0o0O0 ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.listenlive.eu/' + OOOiiiiI , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def I1I1IIiiI1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 if 65 - 65: IiI1i11I / i1iIi . IIiIiII11i
 if 90 - 90: Iii
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , o00oooo , url , ooo0Oo00O in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' [COLORorangered] ' + ooo0Oo00O + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[CR]' + o00oooo + '[CR]' + ooo0Oo00O + '[/COLOR]' )
  if 28 - 28: III1iiIii + OOooOOo . III1iiIii - o0ii1I % ooOoO0O00 % iI11I1II1I1I
def OO0O00OO0 ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.toonjet.com/' + OOOiiiiI , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiII1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I1i11 )
 for url , I11iII in IIi :
  if 'ol.gif' in I11iII :
   pass
  elif 'link_block_' in I11iII :
   pass
  elif '.png' in I11iII :
   pass
  else :
   IiI11i1IIiiI ( ( I11iII ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oIi11I1II1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i11 )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 39 - 39: o0ii1I - Ii1I * o0ii1I . I1ii11iIi11i
  if 68 - 68: I1ii11iIi11i + oOo0O0Ooo % III1iiIii % I11i - IiI1i11I * i1i1I1IIii1II
def OOI11 ( ) :
 IiiI ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 IiiI ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 73 - 73: IiI1i11I / i1iIi + oO0o / OOooOOo . IIiIiII11i * o0ii1I
def IiII111I ( ) :
 IiiI ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiiI ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 IiiI ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 62 - 62: ooOoO0O00 * iI11I1II1I1I % i1i1I1IIii1II % OOooOOo / ii
def iI1111iiI1 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for o000O0O , OOOiiiiI , OOO0ooO0Oo0 in IIi :
  if 'Parent' in o000O0O :
   pass
  elif '2' in OOO0ooO0Oo0 :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 54 - 54: iI11I1II1I1I * IiI1i11I * III1iiIii
def I1i1iI11ii ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for o000O0O , OOOiiiiI , OOO0ooO0Oo0 in IIi :
  if ooO0000o00O in o000O0O . lower ( ) :
   if '1' in OOO0ooO0Oo0 :
    IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOO0ooO0Oo0 :
    IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOO0ooO0Oo0 :
    IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 65 - 65: ooOoO0O00 . Ii
    if 62 - 62: Ii1I + oO0o - Ii1I * III1iiIii - Iii * Iii
def OO00o ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for o000O0O , OOOiiiiI , OOO0ooO0Oo0 in IIi :
  if '1' in OOO0ooO0Oo0 :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOO0ooO0Oo0 :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOO0ooO0Oo0 :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OOOiiiiI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: III1iiIii . ooOoO0O00 * iI11I1II1I1I - o0ii1I * OOooOOo - oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: Iii % Ii1I - OOooOOo * Ii1I
def II1iIIi ( url ) :
 i1iiIIiI1iiI = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in i1Iii1i1I :
  if 'mp3' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in o000O0O :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iiIIiI1iiI + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: oooOo0oo0oo . Iii . i1IiiiI1iI - Iii % Iii + i1IiiiI1iI
   if 99 - 99: I11i + oooOo0oo0oo
   if 34 - 34: i1IiiiI1iI * I11i . oOo0O0Ooo % Ii
def Oo0OO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1iiIIiI1iiI = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  if 'Parent' in o000O0O :
   pass
  elif '.db' in o000O0O :
   pass
  elif '.jpg' in o000O0O :
   pass
  elif '.html' in o000O0O :
   pass
  elif '.doc' in o000O0O :
   pass
  elif 'mp3' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1iiIIiI1iiI + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 74 - 74: o0ii1I - ii
   if 19 - 19: iI11I1II1I1I + i1IiiiI1iI . i1IiiiI1iI - I1ii11iIi11i
def IIiIIiIi1II1IiI ( ) :
 IiiI ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiiI ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiiI ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 99 - 99: I1ii11iIi11i
def IiIi1I11 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OOOiiiiI + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I11iII :
   pass
  else :
   IiiI ( I11iII , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OOOiiiiI ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I11iII + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 19 - 19: ooOoO0O00 / III1iiIii + Ii1I * Ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: ii * IiI1i11I . Ii . i1iIi - i1IiiiI1iI
 if 81 - 81: oOo0O0Ooo / ii
def OO0000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  if '</a>' in o000O0O :
   pass
  elif '(' in o000O0O :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 39 - 39: Ii1I . I1ii11iIi11i + ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: I1ii11iIi11i + i1IiiiI1iI
def O00oOOoOOOOO ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if ooO0000o00O in o000O0O . lower ( ) :
   if '</a>' in o000O0O :
    pass
   elif '(' in o000O0O :
    IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 21 - 21: ii + i1IiiiI1iI
    if 43 - 43: Ii . Ii1I . i1i1I1IIii1II
def I11Ii1iI1II ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if '</a>' in o000O0O :
   pass
  elif '(' in o000O0O :
   IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OOOiiiiI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 74 - 74: oOo0O0Ooo . i1iIi / IiI1i11I . III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . III1iiIii
 if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  i1iiIIiI1iiI = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i1iiIIiI1iiI )
  if 67 - 67: Ii1I + i1i1I1IIii1II * III1iiIii / IIiIiII11i % oO0o % oO0o
def IIIII1IIiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url in IIi :
  if '<p align' in o000O0O :
   pass
  elif '&nbsp;' in o000O0O :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % o0ii1I
def i1oO ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'ongoing' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in OOOiiiiI :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def oOoOo00oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I11I111i1I1 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , I11iII , I11iII , o000O0O )
 for url , o000O0O in I11I111i1I1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def II11IiIIiiiii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iiiiii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oooOOo0o0OOO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 IiiiII = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in oooOOo0o0OOO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , o000O0O in I1iiiiii :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def OoOo00OoOO00 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 62 - 62: OOooOOo * ii * I11i
def Ii1IIi ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if '9cart' in OOOiiiiI :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 37 - 37: i1i1I1IIii1II
def I1Ii1iI1IiI1I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIIIiIiIi1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , o000O0O in IIIIiIiIi1 :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 95 - 95: Iii + I1ii11iIi11i + I1ii11iIi11i
def iiiii1II1I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 20003 , I11iII )
 for url , o000O0O in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 77 - 77: ooOoO0O00 - iI11I1II1I1I . oooOo0oo0oo
def IIiiIiIIiI1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   IiI11i1IIiiI ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 39 - 39: Iii / ii - o0ii1I + oO0o / OOooOOo
def oo0O0000oo0o0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 32 - 32: ii / IiI1i11I / i1IiiiI1iI + IiI1i11I - Iii + IIiIiII11i
def IiIIIiII1111 ( url ) :
 url = cloudflare . source ( url )
 IiIIoOo ( url )
 if 67 - 67: oO0o
def oOoo00O000 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  IiIIoOo ( url )
  if 57 - 57: III1iiIii * iI11I1II1I1I . I1ii11iIi11i / i1iIi . oooOo0oo0oo % i1iIi
  if 33 - 33: o0o00Oo0O * o0ii1I - III1iiIii . ii + III1iiIii
def iI ( ) :
 if 20 - 20: i1IiiiI1iI - OOooOOo
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 91 - 91: ooOoO0O00
def OOooo00 ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 31 - 31: Ii + o0ii1I % OOooOOo
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 9 - 9: i1iIi . Iii - I1ii11iIi11i . i1IiiiI1iI
 for OOOiiiiI , o000O0O in IIi :
  if ooO0000o00O in o000O0O . lower ( ) :
   if 'Dad!' in o000O0O :
    pass
   elif 'Family Guy' in o000O0O :
    pass
   elif '2 Stupid' in o000O0O :
    pass
   elif 'The Zelfs' in o000O0O :
    pass
   elif 'A Clone' in o000O0O :
    pass
   elif 'A.T.O.M' in o000O0O :
    pass
   elif 'Almost Naked' in o000O0O :
    pass
   elif 'Angry Kid' in o000O0O :
    pass
   elif 'Annoying Orange' in o000O0O :
    pass
   elif 'Aqua Teen' in o000O0O :
    pass
   elif 'Assy Mcgee' in o000O0O :
    pass
   elif 'Astroblast' in o000O0O :
    pass
   elif 'Atomic Betty' in o000O0O :
    pass
   elif 'Axe Cop' in o000O0O :
    pass
   elif 'Baby Playpen' in o000O0O :
    pass
   elif 'Beavis and Butt' in o000O0O :
    pass
   elif 'Celebrity Deathmatch' in o000O0O :
    pass
   elif 'Clerks The' in o000O0O :
    pass
   elif 'Crapston Villas' in o000O0O :
    pass
   elif 'Duckman:' in o000O0O :
    pass
   elif 'Stripperella' in o000O0O :
    pass
   elif 'Vixen' in o000O0O :
    pass
   else :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 39 - 39: oooOo0oo0oo
    if 70 - 70: III1iiIii % oO0o % oOo0O0Ooo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: OOooOOo - i1IiiiI1iI / o0o00Oo0O * oOo0O0Ooo - I11i
def i111i11I1ii ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if 'Dad!' in o000O0O :
   pass
  elif 'Family Guy' in o000O0O :
   pass
  elif '2 Stupid' in o000O0O :
   pass
  elif 'The Zelfs' in o000O0O :
   pass
  elif 'A Clone' in o000O0O :
   pass
  elif 'A.T.O.M' in o000O0O :
   pass
  elif 'Almost Naked' in o000O0O :
   pass
  elif 'Angry Kid' in o000O0O :
   pass
  elif 'Annoying Orange' in o000O0O :
   pass
  elif 'Aqua Teen' in o000O0O :
   pass
  elif 'Assy Mcgee' in o000O0O :
   pass
  elif 'Astroblast' in o000O0O :
   pass
  elif 'Atomic Betty' in o000O0O :
   pass
  elif 'Axe Cop' in o000O0O :
   pass
  elif 'Baby Playpen' in o000O0O :
   pass
  elif 'Beavis and Butt' in o000O0O :
   pass
  elif 'Celebrity Deathmatch' in o000O0O :
   pass
  elif 'Clerks The' in o000O0O :
   pass
  elif 'Crapston Villas' in o000O0O :
   pass
  elif 'Duckman:' in o000O0O :
   pass
  elif 'Stripperella' in o000O0O :
   pass
  elif 'Vixen' in o000O0O :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: iI11I1II1I1I % I1ii11iIi11i . IiI1i11I . III1iiIii % Ii
def IIiI1I11ii1i ( url ) :
 I1i11 = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11 )
 for I11iII in i1Iii1i1I :
  o0oooIi1Iii1 = I11iII
 IIIIiIiIi1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i11 )
 for url in IIIIiIiIi1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 10007 , o0oooIi1Iii1 )
  if 87 - 87: ii
  if 1 - 1: iI11I1II1I1I / I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: o0o00Oo0O % oOo0O0Ooo / ii * Ii1I - i1i1I1IIii1II
def o00OO0o ( url , IMAGE ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  print o000O0O + '     ' + url
  if 'easy' in url :
   oOOo00o0oO0O0 ( url )
   if 68 - 68: IIiIiII11i
   if 84 - 84: OOooOOo % o0ii1I + oOo0O0Ooo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: Ii - I1ii11iIi11i
def oOOo00o0oO0O0 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i11 )
 for url in IIi :
  O0oOOoooOO0O ( url )
  if 47 - 47: IiI1i11I * OOooOOo * III1iiIii
  if 46 - 46: o0ii1I
  if 42 - 42: iI11I1II1I1I
def IIi1IiIii ( ) :
 if 40 - 40: oOo0O0Ooo
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 3 - 3: i1iIi / ooOoO0O00 - OOooOOo
def oo0o0ooOoo00O ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  if 'elete' in o000O0O :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 222 , I11iII )
   if 2 - 2: i1i1I1IIii1II . oooOo0oo0oo
def ii1O0oOOo ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ii111IIiiiiI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , oo0OOoOo0 , i1iII1IiiIiI1 in ii111IIiiiiI :
  for ooO0000o00O in oo0OOoOo0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oO00oO0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OOOiiiiI , o000O0O in oO00oO0 :
    if 'tube' in OOOiiiiI :
     pass
    elif 'stage' in OOOiiiiI :
     oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + oo0OOoOo0 + '   -   ' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iII , )
    elif 'vee' in OOOiiiiI :
     pass
     if 80 - 80: IiI1i11I . o0o00Oo0O
def I1Iii ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ii111IIiiiiI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , oo0OOoOo0 , i1iII1IiiIiI1 in ii111IIiiiiI :
  oO00oO0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OOOiiiiI , o000O0O in oO00oO0 :
   if 'tube' in OOOiiiiI :
    pass
   elif 'stage' in OOOiiiiI :
    oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + oo0OOoOo0 + '   -   ' + o000O0O + '[/COLOR]' , ( OOOiiiiI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iII )
   elif 'vee' in OOOiiiiI :
    pass
    if 33 - 33: I11i - i1i1I1IIii1II % Ii1I * Iii . ii % o0ii1I
    if 29 - 29: IiI1i11I + IIiIiII11i . Ii . o0ii1I - o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: i1i1I1IIii1II . Ii1I - iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
def OO0OoOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O00ooOo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O00ooOo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O00ooOo :
  IIIIIIII ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 13 - 13: III1iiIii . I1ii11iIi11i - Iii / i1i1I1IIii1II - I1ii11iIi11i - oOo0O0Ooo
  if 84 - 84: IIiIiII11i
  if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
  if 53 - 53: o0ii1I / oOo0O0Ooo * o0ii1I + I11i + i1i1I1IIii1II - I1ii11iIi11i
  if 16 - 16: oO0o % i1IiiiI1iI . ooOoO0O00 / Ii1I - o0o00Oo0O
  if 85 - 85: ooOoO0O00 . ooOoO0O00
  if 16 - 16: oOo0O0Ooo - oooOo0oo0oo % o0ii1I . oooOo0oo0oo + Ii1I % Ii
def i11iiiiI1i ( ) :
 if 59 - 59: Ii - Iii
 oooO00oOOooO ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 oooO00oOOooO ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 3 - 3: I11i - ii + IiI1i11I . Iii
def o00000Oo ( ) :
 oooO00oOOooO ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 oooO00oOOooO ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
 Ii1IIiI1i ( 'movies' , 'MAIN' )
def III11II111 ( ) :
 if 8 - 8: Ii
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 Oo0Oo0o0oo0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 4 - 4: Ii
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  IIiIIIIii = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( IIiIIIIii )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , i1iIiIi1I , iIIII , I11iI1i1I11I11 , o000O0O in IIi :
   if ooO0000o00O in o000O0O . lower ( ) :
    i11iII1 ( o000O0O , OOOiiiiI , 222 , i1iIiIi1I , I11iI1i1I11I11 , iIIII )
    if 75 - 75: oooOo0oo0oo / Ii / iI11I1II1I1I
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
    if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
def I1iiIIii ( ) :
 if 90 - 90: III1iiIii * Iii % IIiIiII11i / oooOo0oo0oo
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 Oo0Oo0o0oo0O0 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 97 - 97: IiI1i11I % i1iIi
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  II1111iiI1II = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( II1111iiI1II )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for o000O0O , iIIII , OOOiiiiI , I11iII , I11iI1i1I11I11 , i1Ii11II in IIi :
   if ooO0000o00O in o000O0O . lower ( ) :
    oooO00oOOooO ( o000O0O , OOOiiiiI , i1Ii11II , I11iII , I11iI1i1I11I11 , iIIII )
    if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - o0ii1I * iI11I1II1I1I
    Ii1IIiI1i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / i1i1I1IIii1II * I11i + oooOo0oo0oo
    if 89 - 89: i1iIi * oOo0O0Ooo . i1i1I1IIii1II
def O000O000 ( ) :
 if 55 - 55: IIiIiII11i - i1IiiiI1iI - oooOo0oo0oo % o0ii1I
 I1i11 = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , iIIII , OOOiiiiI , I11iII , I11iI1i1I11I11 , i1Ii11II in IIi :
  oooO00oOOooO ( o000O0O , OOOiiiiI , i1Ii11II , I11iII , I11iI1i1I11I11 , iIIII )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def iI1I1iII1iII ( url ) :
 if 84 - 84: Ii / I11i % iI11I1II1I1I . i1iIi . oO0o / IiI1i11I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooooo0oo0OO = ( '%s%s' % ( IIiII , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , i1iIiIi1I , iIIII , I1i11II , o000O0O in IIi :
  iIiI1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for ii1 in iIiI1 :
   if ii1 == url :
    o000O0O = ( '[COLORred]Watched - [/COLOR]' + o000O0O ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  i11iII1 ( o000O0O , url , 222 , i1iIiIi1I , I1i11II , iIIII )
  if 48 - 48: OOooOOo . oOo0O0Ooo . Iii . III1iiIii
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 39 - 39: oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 4 - 4: OOooOOo * o0o00Oo0O - Iii
  if 72 - 72: Iii + i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
def I1III1I1IiI ( url ) :
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , iIIII , url , I11iII , I11iI1i1I11I11 , i1Ii11II in IIi :
  oooO00oOOooO ( o000O0O , url , i1Ii11II , I11iII , I11iI1i1I11I11 , iIIII )
  if 11 - 11: IiI1i11I
  Ii1IIiI1i ( 'movies' , 'MAIN' )
  if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
  if 5 - 5: oooOo0oo0oo + IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
def i11iII1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1i1III = [ ]
  II1i1III . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = False )
 return IIII
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def oooO00oOOooO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 95 - 95: i1IiiiI1iI + III1iiIii * iI11I1II1I1I
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1i1III = [ ]
  II1i1III . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = True )
 return IIII
if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0ii1I
if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Iii
if 2 - 2: o0ii1I
if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
if 19 - 19: o0o00Oo0O + i1i1I1IIii1II + I11i
if 81 - 81: iI11I1II1I1I
if 51 - 51: I11i . Ii1I * o0ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
if 44 - 44: Ii % i1IiiiI1iI % i1i1I1IIii1II + Iii * i1i1I1IIii1II . o0ii1I
if 89 - 89: ii % IIiIiII11i - oO0o % Ii
if 7 - 7: III1iiIii
if 15 - 15: I1ii11iIi11i + IiI1i11I + oOo0O0Ooo * I11i
if 33 - 33: I11i * I1ii11iIi11i
if 88 - 88: i1IiiiI1iI % oooOo0oo0oo - OOooOOo - OOooOOo . oOo0O0Ooo
if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - i1IiiiI1iI
if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
def Oo0o0OOo0Oo0 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 88 - 88: o0ii1I / ii % OOooOOo - ooOoO0O00
def iIiIi111 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1I1IiIiiI1II = [ ]
 try :
  if 39 - 39: ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  Oo0o0OOo0Oo0 ( 'Making Favorites File' )
  i1I1IiIiiI1II . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OooOO = open ( i1I1iI , "w" )
  OooOO . write ( json . dumps ( i1I1IiIiiI1II ) )
  OooOO . close ( )
 else :
  Oo0o0OOo0Oo0 ( 'Appending Favorites' )
  OooOO = open ( i1I1iI ) . read ( )
  I1I111i = json . loads ( OooOO )
  I1I111i . append ( ( name , url , iconimage , fanart , mode ) )
  iI1i1Iiii = open ( i1I1iI , "w" )
  iI1i1Iiii . write ( json . dumps ( I1I111i ) )
  iI1i1Iiii . close ( )
  if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + i1i1I1IIii1II
  if 58 - 58: IiI1i11I - ii
def o00oO00 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  i1I1IiIiiI1II = [ ]
  Oo0o0OOo0Oo0 ( 'Making Favorites File' )
  i1I1IiIiiI1II . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OooOO = open ( i1I1iI , "w" )
  OooOO . write ( json . dumps ( i1I1IiIiiI1II ) )
  OooOO . close ( )
 else :
  i1iiiii = json . loads ( open ( i1I1iI ) . read ( ) )
  ii111iI = len ( i1iiiii )
  for IIiii1I1I in i1iiiii :
   o000O0O = IIiii1I1I [ 0 ]
   OOOiiiiI = IIiii1I1I [ 1 ]
   i1iIiIi1I = IIiii1I1I [ 2 ]
   try :
    oo0O0OoO = IIiii1I1I [ 3 ]
    if oo0O0OoO == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oo0O0OoO = i1iIiIi1I
    else :
     oo0O0OoO = I11iI1i1I11I11
   try : OO0O0O0oo = IIiii1I1I [ 5 ]
   except : OO0O0O0oo = None
   try : iiIIioO0OOOO00o = IIiii1I1I [ 6 ]
   except : iiIIioO0OOOO00o = None
   if 26 - 26: i1iIi + OOooOOo
   if IIiii1I1I [ 4 ] == 0 :
    I1I1II1I11 ( o000O0O , OOOiiiiI , '' , i1iIiIi1I , I11iI1i1I11I11 , '' , 'fav' )
   else :
    I1I1II1I11 ( o000O0O , OOOiiiiI , IIiii1I1I [ 4 ] , i1iIiIi1I , I11iI1i1I11I11 , '' , 'fav' )
    if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
def iIi1i1iiIiiiI ( name ) :
 I1I111i = json . loads ( open ( i1I1iI ) . read ( ) )
 for OoOOo000o0 in range ( len ( I1I111i ) ) :
  if I1I111i [ OoOOo000o0 ] [ 0 ] == name :
   del I1I111i [ OoOOo000o0 ]
   iI1i1Iiii = open ( i1I1iI , "w" )
   iI1i1Iiii . write ( json . dumps ( I1I111i ) )
   iI1i1Iiii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 79 - 79: ii * i1IiiiI1iI - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
 if 82 - 82: OOooOOo . o0ii1I
def oOo00oooOO ( ) :
 ooo00OoOooooo = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 OoooooO0 = open ( ooo00OoOooooo , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 OoooooO0 . write ( r'[' + IiII + ']' + '\n' )
 for o000O0O , I11iII , iIOOOO00 , OOOiiiiI in IIi :
  OOOiiiiI = ( OOOiiiiI + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I11IIII1iI = ( o000O0O + '=plugin://' + IiII + '/?url=' + OOOiiiiI + '&mode=10012&name=' + ( o000O0O ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( I11iII ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( I11iII ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OoooooO0 . write ( I11IIII1iI + '\n' )
  if 37 - 37: oO0o - I1ii11iIi11i
  if 38 - 38: Ii / oO0o
def o00OooooOOOO ( ) :
 I1i11 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI in IIi :
  IiI11i1IIiiI ( '24/7' , OOOiiiiI , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
def iIIIIII ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  Ii1I1i ( o000O0O , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def IIiIi ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  Ii1I1i ( o000O0O , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def IiiIi1III ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  Ii1I1i ( o000O0O , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def OOOO00OooO ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  Ii1I1i ( o000O0O , ( OOOiiiiI ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def IIIi1i1i1iii ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  Ii1I1i ( o000O0O , OOOiiiiI , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 53 - 53: oO0o
  if 80 - 80: IIiIiII11i - I11i . iI11I1II1I1I
def ii11Ii11III ( ) :
 if 73 - 73: i1IiiiI1iI . o0o00Oo0O
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 39 - 39: oOo0O0Ooo . ii * Ii1I
def IIio0 ( ) :
 if 27 - 27: OOooOOo . i1IiiiI1iI * OOooOOo
 I1i11 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , I11iII , o000O0O , IiI1ii11I1 in IIi :
  I1I1II1I11 ( o000O0O + '  -  ' + ( IiI1ii11I1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOiiiiI , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 8 - 8: i1i1I1IIii1II * III1iiIii * i1iIi
  if 26 - 26: IiI1i11I * oooOo0oo0oo / oooOo0oo0oo - IiI1i11I
  if 59 - 59: o0ii1I % IiI1i11I / IIiIiII11i + oOo0O0Ooo * i1iIi
def o0o0O0o0O ( ) :
 if 16 - 16: I11i
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
 if 37 - 37: oOo0O0Ooo + ii . i1IiiiI1iI + oOo0O0Ooo . III1iiIii
def IIio0O0 ( url ) :
 IiIi1II111I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( IiIi1II111I )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iII , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 59 - 59: IIiIiII11i * ii - ii
  if 33 - 33: o0o00Oo0O . Ii % I11i
  if 50 - 50: i1iIi
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
def oo0ooO0O ( ) :
 if 83 - 83: I1ii11iIi11i / i1iIi
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 OOOiiiiI = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( ooO0000o00O ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( OOOiiiiI )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  if ooO0000o00O in o000O0O . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 11 - 11: I11i - IIiIiII11i % i1i1I1IIii1II . IIiIiII11i
   if 65 - 65: i1i1I1IIii1II . Ii % oooOo0oo0oo * IiI1i11I % I1ii11iIi11i
   if 51 - 51: oO0o % IiI1i11I
def Iiiii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1iiIIiI1iiI , II1 , IiIi1I1IiI1II1 , o000O0O in IIi :
  iii1iII1iii = ( IiIi1I1IiI1II1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0O0o = ( II1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OO0o0o = 'Season ' + o0O0o + 'Episode ' + iii1iII1iii + o000O0O
  O0O0O00OoO0O ( OO0o0o , i1iiIIiI1iiI )
  if 22 - 22: Iii - I11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 54 - 54: i1i1I1IIii1II * oO0o - IiI1i11I * Iii + I11i - o0ii1I
  if 5 - 5: i1i1I1IIii1II + o0ii1I
def O0O0O00OoO0O ( name , url ) :
 i1iiIIiI1iiI = url
 I1IiiIIiIii1i = name
 o0o = cloudflare . source ( i1iiIIiI1iiI )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for O00ooOo , I1i11i1II in i1Iii1i1I :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + I1IiiIIiIii1i + I1i11i1II + '[/COLOR]' , O00ooOo , 222 , iiIi1IIiIi + 'dtv.png' )
  if 51 - 51: i1i1I1IIii1II % i1i1I1IIii1II / i1iIi . oooOo0oo0oo / iI11I1II1I1I / ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: I11i / oooOo0oo0oo / i1i1I1IIii1II . i1IiiiI1iI
 if 3 - 3: Iii
def ii11i ( ) :
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . i1IiiiI1iI
 if 31 - 31: o0o00Oo0O - III1iiIii * Ii * ooOoO0O00
 if 78 - 78: i1iIi * OOooOOo . o0ii1I . OOooOOo % iI11I1II1I1I
 if 67 - 67: o0ii1I . I1ii11iIi11i
 if 39 - 39: Iii * i1IiiiI1iI
 if 63 - 63: i1iIi % oOo0O0Ooo . oooOo0oo0oo - i1iIi / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % i1i1I1IIii1II / Iii % o0o00Oo0O
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 100 - 100: i1IiiiI1iI - OOooOOo
def oooOoO00O ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i1IIiiI11II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + I11iII , '' , '' )
 for url in I1i1IIiiI11II :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 4 - 4: oOo0O0Ooo / IIiIiII11i % o0o00Oo0O * i1iIi / IIiIiII11i . I1ii11iIi11i
def iiIiii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i1IIiiI11II = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O in IIi :
  I11iII = 'http://watchepisodes.cc/' + I11iII
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 10093 , I11iII , I11iII , '' )
 for url in I1i1IIiiI11II :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 3 - 3: Iii / i1IiiiI1iI * III1iiIii - o0o00Oo0O + oOo0O0Ooo / III1iiIii
def iii1II11II1 ( url , iconimage ) :
 I11iII = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1I1IiI1II1 , url , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IiIi1I1IiI1II1 + ' - ' + o000O0O + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , I11iII , '' , '' )
  if 30 - 30: III1iiIii / Ii % oO0o * oooOo0oo0oo
def i1oOOOoOO ( url , iconimage ) :
 I11iII = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url in IIi :
  if 'player' in o000O0O :
   pass
  elif 'vod' in o000O0O :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , I11iII , '' , '' )
   if 80 - 80: ii
   if 65 - 65: i1i1I1IIii1II * ooOoO0O00 . ii % i1iIi
   if 87 - 87: Ii * IIiIiII11i - o0ii1I % ii
   if 55 - 55: ooOoO0O00
   if 67 - 67: oOo0O0Ooo - oO0o
   if 60 - 60: ooOoO0O00 / iI11I1II1I1I * i1i1I1IIii1II + i1iIi + ii + IIiIiII11i
def O00oOo00o0o ( ) :
 if 13 - 13: iI11I1II1I1I - oooOo0oo0oo
 if 14 - 14: i1iIi
 if 75 - 75: iI11I1II1I1I % i1iIi / oooOo0oo0oo - IiI1i11I % Ii
 if 11 - 11: Iii . o0ii1I
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
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 11 - 11: ooOoO0O00 / i1IiiiI1iI * Ii1I * i1IiiiI1iI * i1iIi - Ii
 if 96 - 96: Ii1I % Ii1I
def ii1II11IIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O00OooOo00o ) )
 for url , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 33 - 33: o0ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * III1iiIii
def ii11Ii1iii1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 65 - 65: o0o00Oo0O * i1i1I1IIii1II * IIiIiII11i . Iii - ooOoO0O00 * OOooOOo
def i11I111iIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  if 'episode' in url :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 1 - 1: o0ii1I * ii - i1iIi % oooOo0oo0oo - ii
  if 83 - 83: ii . IiI1i11I
def iIo0O000O00o ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiooo = 'http://www.watchseriesgo.to/search/' + ooO0000o00O . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( iiooo )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , OOOiiiiI , o000O0O in IIi :
  if 'watch online' in o000O0O :
   pass
  else :
   print OOOiiiiI
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseriesgo.to' + OOOiiiiI , 10044 , I11iII , '' , '' )
   if 42 - 42: ii % Iii % III1iiIii
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 54 - 54: i1iIi - oOo0O0Ooo - IiI1i11I + oooOo0oo0oo - oO0o / ii
def oO000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O , IiIi1I1IiI1II1 , iIIII in IIi :
  IIIii1iiIi = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IiIi1I1IiI1II1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIIii1iiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , I11iII , '' , iIIII )
  if 20 - 20: OOooOOo % o0o00Oo0O
def Oo0OOO00oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  IIIii1iiIi = ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIIii1iiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 80 - 80: III1iiIii . I11i
def IIiIiI1i11iiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , I11iII , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 64 - 64: o0ii1I
def IIiiiIi1ii11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O00OooOo00o = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1 , ii111IIiiiiI in O00OooOo00o :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( ii111IIiiiiI ) )
  for url , o000O0O in IIi :
   IIIii1iiIi = ( II1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIIii1iiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: o0o00Oo0O * o0ii1I
class o0O00o00Ooo ( ) :
 if 16 - 16: oooOo0oo0oo . IIiIiII11i - o0ii1I - ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 83 - 83: Ii - I1ii11iIi11i
  IIIii1iiIi = name
  self . Get_Sources ( OOOiiiiI , IIIii1iiIi )
  if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
  if 35 - 35: I11i + oO0o - Ii1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , o000O0O in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + OOOiiiiI
   self . Get_site_link ( URL , season_name )
   if 24 - 24: IIiIiII11i
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  IIIIiIiIi1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in IIIIiIiIi1 :
   self . main ( url , season_name )
   if 23 - 23: I1ii11iIi11i - IiI1i11I
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0oO0O = 'DACLIPS'
   if o0oO0O in o0O00o00Ooo . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0oO0O )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    o0oO0O = 'THEVIDEO'
    if o0oO0O in o0O00o00Ooo . source_list :
     pass
    else :
     self . thevideo ( url , season_name , o0oO0O )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     o0oO0O = 'ALLMYVIDEOS'
     if o0oO0O in o0O00o00Ooo . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , o0oO0O )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      o0oO0O = 'VIDSPOT'
      if o0oO0O in o0O00o00Ooo . source_list :
       pass
      else :
       self . vidspot ( url , season_name , o0oO0O )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       o0oO0O = 'VODLOCKER'
       if o0oO0O in o0O00o00Ooo . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , o0oO0O )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        o0oO0O = 'VIDTO'
        if o0oO0O in o0O00o00Ooo . source_list :
         pass
        else :
         self . vidto ( url , season_name , o0oO0O )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
       else :
        if 'youwatch' in url :
         o0oO0O = 'YouWatch'
         if o0oO0O in o0O00o00Ooo . source_list :
          pass
         else :
          self . youwatch ( url , season_name , o0oO0O )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 13 - 13: iI11I1II1I1I * I11i - Ii
          if 63 - 63: ii * i1IiiiI1iI
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 , o000O0O in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . i1i1I1IIii1II % IIiIiII11i
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 , o000O0O in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 18 - 18: Iii % ii + oO0o / Iii
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 37 - 37: ooOoO0O00 - o0ii1I / III1iiIii . IIiIiII11i % i1iIi
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 39 - 39: o0ii1I % Ii * oO0o
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 23 - 23: oooOo0oo0oo + i1iIi / Ii * I1ii11iIi11i . oO0o
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . youplay ( IiIiiiiI1 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIiiiiI1 in IIi :
   self . Printer ( IiIiiiiI1 , season_name , source_name )
   if 28 - 28: IiI1i11I - I11i
 def Printer ( self , Link , season_name , source_name ) :
  if 92 - 92: I1ii11iIi11i % I11i - i1iIi / i1iIi / OOooOOo
  if Link in o0O00o00Ooo . List :
   pass
  elif source_name in o0O00o00Ooo . source_list :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   o0O00o00Ooo . List . append ( Link )
   o0O00o00Ooo . source_list . append ( source_name )
   if 84 - 84: oooOo0oo0oo
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 4 - 4: III1iiIii . i1IiiiI1iI / o0ii1I / IiI1i11I + IIiIiII11i
   if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . Iii - o0ii1I
   if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
   if 23 - 23: Iii * i1IiiiI1iI * I11i - oOo0O0Ooo % OOooOOo + I11i
   if 41 - 41: III1iiIii * ii . i1iIi % Ii
def iI111i1II ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 11 - 11: iI11I1II1I1I . i1IiiiI1iI - I1ii11iIi11i / Iii + IIiIiII11i
def I1III1i ( url ) :
 iiOOoOO = '20'
 OOo00OOoOOO = [ ]
 I1iII11I1I = '                                                    '
 i1i1ii1 = '        '
 I1I1II1I11 ( I1iII11I1I + 'pl' + i1i1ii1 + 'w' + i1i1ii1 + 'd' + i1i1ii1 + 'l' + i1i1ii1 + 'f' + i1i1ii1 + 'a' + i1i1ii1 + 'pts' , '' , '' , '' , '' , '' )
 I1i11 = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I1i11 )
 for i1IiI1i , i1iii , oOoOO0OO0O0 , oO0oO0O , oooO000Oo000O , oOOOoo00 , OooOO , iIiiI1i1I , OoOOo0OOO0OO in IIi :
  O0O00000o = oOOOoOo00O0 ( i1iii )
  Oo00o00OO0oO = oOOOoOo00O0 ( oOoOO0OO0O0 )
  IIIIiiI1iIiI = oOOOoOo00O0 ( oO0oO0O )
  OOOOo0ooOOO0 = oOOOoOo00O0 ( oooO000Oo000O )
  Oo00O0O = oOOOoOo00O0 ( oOOOoo00 )
  IIIIiI1i1111iI1i = oOOOoOo00O0 ( OooOO )
  OOo00OOoOOO . append ( i1IiI1i [ 0 ] )
  OoO00o = len ( OOo00OOoOOO )
  Oo0o0OO0O0o = int ( len ( I1iII11I1I ) - len ( i1IiI1i ) - 2 )
  if len ( OOo00OOoOOO ) >= 10 :
   Oo0o0OO0O0o = Oo0o0OO0O0o - 1
  if len ( OOo00OOoOOO ) <= int ( iiOOoOO ) :
   Ii1I1i ( str ( OoO00o ) + ' ' + i1IiI1i + I1iII11I1I [ 0 : Oo0o0OO0O0o ] + i1iii + O0O00000o + oOoOO0OO0O0 + Oo00o00OO0oO + oO0oO0O + IIIIiiI1iIiI + oooO000Oo000O + OOOOo0ooOOO0 + oOOOoo00 + Oo00O0O + OooOO + IIIIiI1i1111iI1i + ' ' + OoOOo0OOO0OO , '' , '' , '' , '' , '' )
   if 98 - 98: o0o00Oo0O / i1i1I1IIii1II / IiI1i11I
   if 83 - 83: i1IiiiI1iI
def oOOOoOo00O0 ( space ) :
 if len ( space ) > 1 :
  I111iiIIiI1I = len ( '        ' ) - len ( space ) + 1
  space = int ( I111iiIIiI1I ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 38 - 38: i1i1I1IIii1II
def I1iIiI ( ) :
 if 45 - 45: Iii . IIiIiII11i / Ii
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
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OOOiiiiI , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I11iII , Oo00OOOOO , '' )
  if 7 - 7: ooOoO0O00
def oOoO0oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in O00OooOo00o :
  Oo0OOo = re . compile ( '(.*?)</h2>' ) . findall ( str ( O00OooOo00o ) )
  for o00I11Ii1 in Oo0OOo :
   o00I11Ii1 = o00I11Ii1
  I11IIIIi1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
  for ooOOo000 , I11iII , time , oo0O0 in I11IIIIi1 :
   Oo0oo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oo0O0 )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o00I11Ii1 + ' - ' + ooOOo000 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I11iII , Oo00OOOOO , ( str ( Oo0oo ) ) )
   if 86 - 86: o0o00Oo0O . ii * Iii / III1iiIii
 Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if 87 - 87: iI11I1II1I1I
def OOOooOO0oO ( ) :
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
 if 20 - 20: oO0o
def ii1iiiiii ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O in IIi :
  OOOoO0o = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   OOOoO0o = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + OOOoO0o + '[/COLOR]' , url , 10013 , I11iII )
 for url , I11iII , o000O0O in i1Iii1i1I :
  OOOoO0o = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + OOOoO0o + '[/COLOR]' , url , 10013 , I11iII )
def iiioO000oO0oO ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 44 - 44: oooOo0oo0oo - III1iiIii + IiI1i11I
 if 78 - 78: o0ii1I
 if 29 - 29: IIiIiII11i
 if 79 - 79: iI11I1II1I1I - Ii + i1iIi - IIiIiII11i . iI11I1II1I1I
 if 84 - 84: I1ii11iIi11i % Iii * o0o00Oo0O * Iii
 if 66 - 66: oooOo0oo0oo / iI11I1II1I1I - OOooOOo % o0o00Oo0O . i1iIi
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
 for url , I11iII , o000O0O in i1Iii1i1I :
  OOOoO0o = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + OOOoO0o + '[/COLOR]' , url , 10013 , I11iII )
   if 37 - 37: ooOoO0O00 * Ii
def Oo00OOooOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for O00ooOo in IIi :
  II1iiiiI1Ii11 = ( O00ooOo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  IIIIIIII ( 'http:' + II1iiiiI1Ii11 )
  if 69 - 69: Iii / ooOoO0O00 / i1i1I1IIii1II . i1IiiiI1iI
  if 41 - 41: i1i1I1IIii1II * III1iiIii + oOo0O0Ooo
  if 7 - 7: i1iIi % oO0o + ii
  if 25 - 25: IiI1i11I . oO0o / iI11I1II1I1I
def OOoo00OoO0o ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O , I11iII in IIi :
  oOOo000oOoO0 ( o000O0O , url , 8046 , I11iII )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def II11Iii1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  IIIIIIII ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 98 - 98: ii + OOooOOo . OOooOOo / o0o00Oo0O / Ii
def ooo0o0oO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i11 )
 for url in IIi :
  yt . PlayVideo ( url )
  if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
def ii11i11i1 ( ) :
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iI11IiII ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I1i11 )
 for I11iII , url , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + I11iII )
 for url in next :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 83 - 83: Ii1I
  if 53 - 53: OOooOOo % i1iIi . oO0o + oOo0O0Ooo / Ii1I
def OOooOOO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i11 )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o00Oooo0o0 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , '' )
  if 5 - 5: IiI1i11I - IiI1i11I / i1IiiiI1iI % I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoO00OOo ( name , url ) :
 iiiiiiii = 0
 name = name
 url = url
 iiio00oOOooOOo0o = [ '144' , '240' , '380' , '480' , '720' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  O0oOOoooOO0O ( url )
  if 74 - 74: Ii1I % i1IiiiI1iI - oO0o * Iii . ii * oO0o
  if 99 - 99: OOooOOo . IiI1i11I - ii - o0o00Oo0O
  if 6 - 6: oooOo0oo0oo
  if 3 - 3: o0o00Oo0O - i1IiiiI1iI * o0ii1I * oooOo0oo0oo / o0ii1I
  if 58 - 58: o0ii1I * iI11I1II1I1I + i1iIi . i1iIi
  if 74 - 74: i1iIi - I11i * III1iiIii % i1iIi
  if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * i1IiiiI1iI - oO0o - I11i
  if 44 - 44: ii
def oOi1IiIiIii11I ( ) :
 I1i11 = ii1IIIIiI11 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  if 'genre' in OOOiiiiI :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , OOOiiiiI , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0o0O00 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I1i11 )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , I11iII )
 for url in next :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 85 - 85: Ii . Iii + o0ii1I / o0ii1I
def i1o00Oo ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I1i11 )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  o00Oooo0o0 ( url )
  if 38 - 38: i1IiiiI1iI
def OOoO000oO ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOII1i1II = 'http://documentarylovers.com/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 O0Ooo = OOOII1i1II . lower ( )
 O0o0O00 ( O0Ooo )
 if 39 - 39: i1i1I1IIii1II / Ii
def iio0O ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if 'films' in url :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def OOoOO0 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i11 )
 for I11iII , url , o000O0O in IIi :
  if 'films' in url :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + I11iII )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def III1iiI1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1i11 )
 for url in IIi :
  if 'rtd' in url :
   oOOooo0O ( url )
   if 76 - 76: o0ii1I + IiI1i11I - III1iiIii * iI11I1II1I1I % ooOoO0O00
def oOOooo0O ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I1i11 )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  O0oOOoooOO0O ( url )
  if 72 - 72: i1iIi + IIiIiII11i . o0o00Oo0O - IiI1i11I / ii . i1IiiiI1iI
  if 28 - 28: iI11I1II1I1I . o0o00Oo0O
def iiiIiI111iiI1II ( ) :
 II11iIiIIIiI = ii1IIIIiI11 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O , iiI1iI1I in IIi :
  IiI11i1IIiiI ( ( o000O0O + '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '[/COLOR]' ) , OOOiiiiI , 8086 , I11iII )
  if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . i1iIi - o0ii1I
def OO0OOO0o0OOO0 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 8087 , I11iII )
  if 39 - 39: o0o00Oo0O * oOo0O0Ooo
def iiI11i1II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  oOoo0o0O00 ( url , o000O0O )
  if 21 - 21: Iii + iI11I1II1I1I
def oOoo0o0O00 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 52 - 52: o0o00Oo0O + OOooOOo
def IiiIIiiII ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OOOiiiiI , 3002 , 'http://www.solie.org/alibrary/' + I11iII )
def OOOOo0oo0o ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I11iII )
def iI1I1iii11i ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 I1111i = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i11 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , o000O0O in I1111i :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Season- ' + o000O0O + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , I11iII , o000O0O in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I11iII )
def IIIi11 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i11 )
 for url in IIi :
  ii11 ( url )
def ii11 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i11 )
 for url in IIi :
  O0oOOoooOO0O ( url )
  if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OoO ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOiiiiI , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def OOOOo00oOOO00 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i11 )
 for url in IIi :
  IiIIoOo ( url )
  if 13 - 13: Ii1I / oO0o * Ii % oO0o % oO0o * IIiIiII11i
def ii1ii111 ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OOOiiiiI , 8065 , iiIi1IIiIi + 'classictv.png' )
def I1oo0OoOOO ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  if 'mp4' in url :
   O0oOOoooOO0O ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 76 - 76: Ii1I
def OoOooOOO00o0OoOOOo ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OOOiiiiI , 8071 , iiIi1IIiIi + 'streams.png' )
def I1ioO000O0oO00 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o000O0O , url in IIi :
  if '(Free Access)' in o000O0O :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def i1Ii1IIii ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , o000O0O , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , I11iII , I11iI1i1I11I11 , '' )
  if 48 - 48: o0o00Oo0O - i1i1I1IIii1II * ooOoO0O00 + oOo0O0Ooo . i1i1I1IIii1II
def O0Oo000OO000 ( ) :
 iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , iiio00oOOooOOo0o )
 if O0O0ooOOO == 0 :
  Ii1IiIi11i1 ( 'http://watchxxxfree.com/categories' )
 if O0O0ooOOO == 1 :
  OO0OOo00Oo ( 'http://www.perfectgirls.net' )
 if O0O0ooOOO == 2 :
  IiI1iIIiIi1Ii ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 3 :
  O0oOoOOO000 ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 4 :
  IiI1iIIiIi1Ii ( 'http://www.xvideos.com/best' )
 if O0O0ooOOO == 5 :
  IiI1iIIiIi1Ii ( 'http://www.xvideos.com/verified/videos' )
 if O0O0ooOOO == 6 :
  oOo00o0oO ( 'http://www.xvideos.com/tags' )
 if O0O0ooOOO == 7 :
  iIiIi ( 'http://www.xvideos.com/porn' )
 if O0O0ooOOO == 8 :
  I1Iii11II ( )
  if 17 - 17: iI11I1II1I1I - i1iIi
  if 99 - 99: I1ii11iIi11i + i1IiiiI1iI % i1iIi - I11i
  if 52 - 52: Ii1I
  if 93 - 93: IiI1i11I . Ii
  if 24 - 24: oooOo0oo0oo . oO0o + i1IiiiI1iI . i1i1I1IIii1II - Ii1I % IiI1i11I
  if 49 - 49: o0o00Oo0O . I1ii11iIi11i / o0ii1I
  if 29 - 29: Ii1I / i1i1I1IIii1II * o0o00Oo0O - Ii - oO0o + o0ii1I
  if 86 - 86: oOo0O0Ooo / Ii1I * o0ii1I % Ii
  if 20 - 20: IiI1i11I . ii + IiI1i11I + i1iIi * Ii1I
def i1IIiiI1iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  if 'ch' in url :
   IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def o0OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOo00OOooO = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , o000O0O in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for o000O0O , url in OOOo00OOooO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OO0OOOoO0O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iII1I1iIi1i ( url )
def O0OO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0oOOoooOO0O ( url )
def Ii1IiIi11i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O , I111iiIIiI1I in IIi :
  if 'category' in url :
   IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORorange]   ' + I111iiIIiI1I + '[/COLOR]' , url , 90006 , I11iII , iiIi1IIiIi + 'Jizbox.png' , '' )
def Ii11IiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOo00OOooO = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , I11iII , '' , '' )
 for url in OOOo00OOooO :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iII11iiI1i11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iII1I1iIi1i ( url )
def iII1I1iIi1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0oOOoooOO0O ( url )
def OO0OOo00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I111iiIIiI1I in IIi :
  if 'category' in url :
   IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORorange]' + I111iiIIiI1I + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def I1Iii1III ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1iiIIiI1iiI = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOo00OOooO = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , I11iII , '' , '' )
 for url in OOOo00OOooO :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , i1iiIIiI1iiI + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def Oo0oo0OoO0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I1IO0 ( 'http://www.perfectgirls.net' + url )
def I1IO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IIIIIIII ( 'http://' + url )
def iIiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I111iiIIiI1I in IIi :
  IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgreen] - No of Videos : [COLORorange]' + I111iiIIiI1I + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOo00o0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOOo00OOooO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in OOOo00OOooO :
  IiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I111iiIIiI1I in IIi :
  IiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgreen] - No of Videos : [COLORorange]' + ( I111iiIIiI1I + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 7 - 7: III1iiIii * i1iIi + OOooOOo
def iIiiIi11iiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOOo00OOooO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in OOOo00OOooO :
  IiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O , oOO0O00o0O0 in IIi :
  IiiI ( o000O0O + '--' + ( oOO0O00o0O0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I11iII ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 82 - 82: Iii % ooOoO0O00
  if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
def IiI1iIIiIi1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , url , o000O0O , OoO0O , iI11iI in IIi :
  IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgreen] - Porn Quality : [COLORorange]' + iI11iI + ' - [COLORred]' + OoO0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , I11iII , I11iII , iI11iI + ' - ' + OoO0O )
 O0o0ooo00o00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in O0o0ooo00o00 :
  IiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 6 - 6: Ii / oO0o . Ii / i1iIi
def O0oOoOOO000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOo00OOooO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in OOOo00OOooO :
  IiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O00OooOo00o ) )
 for url , o000O0O in IIi :
  if '/c/' in url :
   IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 26 - 26: o0o00Oo0O * o0ii1I - oOo0O0Ooo - IiI1i11I / iI11I1II1I1I
   if 57 - 57: Ii1I - oO0o * iI11I1II1I1I
def I1Iii11II ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II111IiI11i = ( ooO0000o00O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 O0Ooo = II111IiI11i . lower ( )
 iIIiiII11i1I1 = 'http://www.xvideos.com/?k=' + O0Ooo
 print iIIiiII11i1I1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( iIIiiII11i1I1 )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , OOOiiiiI , o000O0O , OoO0O , iI11iI in IIi :
  IiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgreen] - Porn Quality : [COLORorange]' + iI11iI + ' - [COLORred]' + OoO0O + '[/COLOR]' , 'http://www.xvideos.com' + OOOiiiiI , 10108 , I11iII , I11iII , iI11iI + ' - ' + OoO0O )
 O0o0ooo00o00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in O0o0ooo00o00 :
  IiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OOOiiiiI , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 91 - 91: IIiIiII11i . I1ii11iIi11i . i1i1I1IIii1II - ii / OOooOOo
if 30 - 30: Iii % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
if 55 - 55: oO0o
if 20 - 20: i1iIi * i1IiiiI1iI * I11i - i1iIi
if 32 - 32: o0ii1I * i1i1I1IIii1II
if 85 - 85: Ii . oO0o + oO0o
if 28 - 28: I1ii11iIi11i
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
if 62 - 62: IIiIiII11i
if 96 - 96: Iii % OOooOOo * Ii1I
if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . i1iIi
if 63 - 63: Ii % Ii1I % oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
if 77 - 77: I11i
if 63 - 63: i1iIi * i1i1I1IIii1II + i1iIi * o0ii1I + I1ii11iIi11i / Ii1I
if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
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
def II1I11iIIIii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 IIIIiIiIi1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in IIIIiIiIi1 :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 25 - 25: o0ii1I * iI11I1II1I1I * I11i + OOooOOo . OOooOOo
def IIi1I ( url ) :
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 try : I1iiiiii . play ( url )
 except : pass
 if 19 - 19: o0o00Oo0O * Iii % ii
 if 36 - 36: I11i % Iii * Ii1I % o0ii1I + ooOoO0O00 - I1ii11iIi11i
def oo00O0oOo ( ) :
 if 6 - 6: ooOoO0O00 + IiI1i11I - ooOoO0O00 - I1ii11iIi11i - I11i * Ii1I
 if 90 - 90: i1iIi / o0o00Oo0O / I11i . o0ii1I / ii
 if 6 - 6: I11i - IiI1i11I - oooOo0oo0oo / ii
 if 26 - 26: IIiIiII11i + ooOoO0O00
 if 14 - 14: iI11I1II1I1I - i1iIi + i1i1I1IIii1II + Ii / iI11I1II1I1I
 if 63 - 63: Ii
 if 21 - 21: i1IiiiI1iI
 if 70 - 70: Iii . OOooOOo
 if 86 - 86: III1iiIii
 if 25 - 25: o0ii1I . o0o00Oo0O . Ii + ii / oooOo0oo0oo
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 8091 , iiIi1IIiIi + 'gofish.png' )
def oo0OO0oOooo ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o000O0O , I11iII in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 8092 , I11iII )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def I111II ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0OI111i = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII in O0OI111i :
  I11iII = I11iII
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 8092 , I11iII )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 39 - 39: Ii1I
def oOOI111I1 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 90 - 90: i1IiiiI1iI % I11i . I1ii11iIi11i
  if 37 - 37: o0ii1I / IIiIiII11i
  if 66 - 66: i1iIi + i1i1I1IIii1II % ii
  if 23 - 23: i1i1I1IIii1II . OOooOOo + iI11I1II1I1I
iiiiiIi1II1i = '{PQ},' ; II1II11I11ii = '{SC},' ; II1iii111 = '{XG},' ; ooOooo = '{JP},' ; Oo00 = '{HW},' ; o0OO00oOO00 = '{RT},'
def OoOo0oOooOoOO ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiIIi = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 OOOiiiiI = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 i1iiIIiI1iiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 I11Ii111I = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Oo00OO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oO00OoOOOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Oo0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ooO0000o00O
 o0OOOOO0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I1I1IiIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 27 - 27: i1i1I1IIii1II * I1ii11iIi11i * I1ii11iIi11i / III1iiIii + I1ii11iIi11i
 o00ii111Iiii = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 oo0oO0o0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 94 - 94: i1iIi - ooOoO0O00 . o0o00Oo0O / oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( i1iiIIiI1iiI )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 o0OOoOO = O00O0oOO00O00 ( i1iiIIiI1iiI )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( I11Ii111I )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( Oo00OO0 )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 iII1 = O00O0oOO00O00 ( I1I1IiIi1 )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 37 - 37: Ii1I * i1IiiiI1iI * oOo0O0Ooo * o0o00Oo0O
 if 35 - 35: oOo0O0Ooo - Ii1I * IiI1i11I + III1iiIii / ooOoO0O00
 if 46 - 46: I1ii11iIi11i . i1iIi % I1ii11iIi11i / IIiIiII11i * i1iIi * oooOo0oo0oo
 if 59 - 59: i1IiiiI1iI * IiI1i11I
 if 31 - 31: Iii / o0o00Oo0O
 if 57 - 57: ooOoO0O00 % i1iIi
 if 69 - 69: I11i
 if 69 - 69: i1IiiiI1iI
 Oo000 = O00O0oOO00O00 ( oo0oO0o0 )
 if 83 - 83: iI11I1II1I1I . I11i + i1IiiiI1iI . ii / i1iIi + IIiIiII11i
 if iII1 != 'Failed' :
  OO0o0oO0O000o = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iII1 )
  for OOOiiiiI , o000O0O in OO0o0oO0O000o :
   I1iI11iii = O00O0oOO00O00 ( OOOiiiiI )
   oo0oO = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1iI11iii )
   for IiIi1iI11 , iiI1iI1I in oo0oO :
    iiI1iI1I = ( iiI1iI1I . replace ( '.' , ' ' ) )
    if O0Ooo in iiI1iI1I . lower ( ) :
     if '.mkv' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.mp4' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.avi' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 222 , '' , '' , '' )
     elif '.wav' in IiIi1iI11 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 90 - 90: o0ii1I * IiI1i11I / oooOo0oo0oo
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in i1Iii1i1I :
   if ooO0000o00O in o000O0O . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORred] source Technica[/COLOR]' ) , OOOiiiiI , 222 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 68 - 68: OOooOOo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: i1i1I1IIii1II
 if o00OooOO000 != 'Failed' :
  IIIIiIiIi1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OO0iIiiIi11IIi , o000O0O in IIIIiIiIi1 :
   if ooO0000o00O in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I11Ii111I + OO0iIiiIi11IIi ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  O0o0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in O0o0oO :
   if ooO0000o00O in o000O0O . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORred] source RaizTv[/COLOR]' ) , OOOiiiiI , 222 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 82 - 82: I11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + i1IiiiI1iI
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
    if 70 - 70: o0o00Oo0O . o0ii1I
    if 33 - 33: oooOo0oo0oo * o0ii1I
    if 64 - 64: Ii . iI11I1II1I1I
    if 7 - 7: OOooOOo % i1iIi + OOooOOo - OOooOOo * Ii % oO0o
    if 57 - 57: oooOo0oo0oo / oO0o + Ii1I
    if 60 - 60: o0o00Oo0O * I1ii11iIi11i % oooOo0oo0oo + III1iiIii . oO0o . I1ii11iIi11i
    if 70 - 70: Iii . Ii1I * i1i1I1IIii1II
    if 97 - 97: i1i1I1IIii1II . iI11I1II1I1I - oooOo0oo0oo
    if 23 - 23: Ii1I % Iii
 Oo0Oo0o0oo0O0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  IIiIIIIii = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  iII1 = O00O0oOO00O00 ( IIiIIIIii )
  if iII1 != 'Failed' :
   OO0o0oO0O000o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1 )
   for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in OO0o0oO0O000o :
    if ooO0000o00O in o000O0O . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] - Source Pandoras[/COLOR]' , OOOiiiiI , 222 , i1iIiIi1I , I1i11II , iIIII )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 99 - 99: i1IiiiI1iI - Ii1I - oOo0O0Ooo - i1IiiiI1iI + oO0o + IIiIiII11i
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 34 - 34: i1IiiiI1iI * Iii
 Oo0Oo0o0oo0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 31 - 31: III1iiIii . i1i1I1IIii1II
 if 40 - 40: o0ii1I - Iii / IIiIiII11i * ooOoO0O00 + III1iiIii * IIiIiII11i
 for oO00oOOo0Oo in Oo0Oo0o0oo0O0 :
  IIiIIIIii = iiIIi + oO00oOOo0Oo
  i1i111Iiiiiii = O00O0oOO00O00 ( IIiIIIIii )
  if i1i111Iiiiiii != 'Failed' :
   Iiiii1IIiI = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( i1i111Iiiiiii )
   for OO0iIiiIi11IIi , o000O0O in Iiiii1IIiI :
    if ooO0000o00O in o000O0O . lower ( ) :
     oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiIIi + oO00oOOo0Oo + OO0iIiiIi11IIi ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - i1IiiiI1iI
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: o0ii1I - III1iiIii - ooOoO0O00 / Ii . III1iiIii
def iII1111III1I ( ) :
 if 58 - 58: oooOo0oo0oo
 if 12 - 12: oOo0O0Ooo . I11i * ii
 if 64 - 64: OOooOOo + III1iiIii - ooOoO0O00 . IIiIiII11i . oO0o
 if 31 - 31: i1i1I1IIii1II . IiI1i11I - Iii . iI11I1II1I1I + Iii . OOooOOo
 if 86 - 86: Ii1I - Ii1I / IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - III1iiIii
 if 30 - 30: ii % oooOo0oo0oo
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - oooOo0oo0oo
 if 81 - 81: IiI1i11I % o0ii1I . i1iIi
 if 66 - 66: Ii1I * o0ii1I / ii * o0o00Oo0O % oooOo0oo0oo
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * o0ii1I / i1IiiiI1iI * ii
 if 82 - 82: I1ii11iIi11i / o0ii1I / o0ii1I % o0ii1I
 if 20 - 20: i1iIi
 if 63 - 63: iI11I1II1I1I . oO0o
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 if 26 - 26: oooOo0oo0oo . oO0o % OOooOOo
 if 94 - 94: III1iiIii
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 if 15 - 15: o0ii1I - III1iiIii / o0o00Oo0O
 if 28 - 28: i1IiiiI1iI . ooOoO0O00 / Ii1I
 IiIi1iI11 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ooO0000o00O ) . replace ( ' ' , '+' )
 i1iiIIiI1iiI = 'http://onlinemovies.tube/?s=' + ( ooO0000o00O ) . replace ( ' ' , '+' )
 I11Ii111I = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 Oo00OO0 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oO00OoOOOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 77 - 77: Ii / i1IiiiI1iI / Ii % OOooOOo - i1IiiiI1iI
 o0OOOOO0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 I1I1IiIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 80 - 80: i1IiiiI1iI % OOooOOo . ii . IIiIiII11i % III1iiIii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 6 - 6: i1IiiiI1iI % III1iiIii / o0ii1I + i1IiiiI1iI . i1i1I1IIii1II
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 70 - 70: iI11I1II1I1I / o0ii1I
 if 61 - 61: o0o00Oo0O * I11i + i1IiiiI1iI - oooOo0oo0oo . oOo0O0Ooo - III1iiIii
 I1III1111iIi = O00O0oOO00O00 ( IiIi1iI11 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( i1iiIIiI1iiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( I11Ii111I )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo00OO0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 i1i111Iiiiiii = O00O0oOO00O00 ( oO00OoOOOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 7 - 7: Ii1I
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / Iii
 o0OOoOO = O00O0oOO00O00 ( o0OOOOO0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 iII1 = O00O0oOO00O00 ( I1I1IiIi1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
 if 13 - 13: Ii
 if iII1 != 'Failed' :
  OO0o0oO0O000o = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iII1 )
  for OOOiiiiI , o000O0O in OO0o0oO0O000o :
   I1iI11iii = O00O0oOO00O00 ( OOOiiiiI )
   oo0oO = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1iI11iii )
   for IiIi1iI11 , iiI1iI1I in oo0oO :
    if O0Ooo in iiI1iI1I . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iiI1iI1I + '-[COLORgold] source ' + o000O0O + '[/COLOR]' ) , OOOiiiiI + IiIi1iI11 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 54 - 54: oooOo0oo0oo . Ii1I * Iii % i1IiiiI1iI . o0o00Oo0O * III1iiIii
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0OOoOO != 'Failed' :
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOoOO )
  for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in i1I1i :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] source HeroVision[/COLOR]' ) , OOOiiiiI , 1016 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 87 - 87: o0ii1I % Ii1I * I1ii11iIi11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: I1ii11iIi11i / Iii - iI11I1II1I1I * iI11I1II1I1I
    if 18 - 18: Iii * Ii1I / Ii / iI11I1II1I1I * ii . oooOo0oo0oo
    if 69 - 69: I1ii11iIi11i * i1iIi
    if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
    if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
    if 38 - 38: i1i1I1IIii1II + ii * OOooOOo % i1i1I1IIii1II
    if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
    if 24 - 24: OOooOOo * o0ii1I
    if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
    if 81 - 81: oooOo0oo0oo
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  Ii1Ii1Ii1I1I = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for OOOiiiiI , I11iII , o000O0O , III1II1i in i1Iii1i1I :
   if O0Ooo in o000O0O . lower ( ) :
    if 'season' in III1II1i :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90054 , I11iII , I11iII , '' )
    if 'episodes' in III1II1i :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90044 , I11iII , I11iII , '' )
  for OOOiiiiI in Ii1Ii1Ii1I1I :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , OOOiiiiI , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 58 - 58: IIiIiII11i . i1IiiiI1iI . o0ii1I * ii / o0ii1I / Iii
   Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if I1III1111iIi != 'Failed' :
  O0oOOo0o = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
  for OOOiiiiI , o000O0O , I11iII in O0oOOo0o :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( o000O0O ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , OOOiiiiI , 8022 , I11iII , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 41 - 41: Iii + oO0o . IiI1i11I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 73 - 73: Ii * oOo0O0Ooo + I11i / i1i1I1IIii1II
    if 56 - 56: ooOoO0O00
    if 11 - 11: Ii % I11i / Iii * ii
    if 82 - 82: III1iiIii
    if 10 - 10: I1ii11iIi11i % oooOo0oo0oo / Iii * III1iiIii - I11i
    if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / IiI1i11I
    if 1 - 1: i1IiiiI1iI / OOooOOo * OOooOOo - I11i % o0ii1I
    if 96 - 96: III1iiIii / o0ii1I % oO0o . iI11I1II1I1I
    if 30 - 30: Iii - oO0o
 if o00OooOO000 != 'Failed' :
  IIIIiIiIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for o000O0O in IIIIiIiIi1 :
   if O0Ooo in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( I11Ii111I + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 15 - 15: ii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  O0o0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for o000O0O in O0o0oO :
   if O0Ooo in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( Oo00OO0 + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 31 - 31: IIiIiII11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if i1i111Iiiiiii != 'Failed' :
  Iiiii1IIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i111Iiiiiii )
  for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in Iiiii1IIiI :
   if O0Ooo in o000O0O . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + o000O0O + '-[COLORgold] Source Scooby[/COLOR]' ) , OOOiiiiI , 1016 , i1iIiIi1I , I1i11II , iIIII )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 62 - 62: iI11I1II1I1I % i1IiiiI1iI % Ii1I * III1iiIii
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 87 - 87: III1iiIii
 OOOOo00oo00O = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oO00oOOo0Oo in OOOOo00oo00O :
  IIiIIIIii = oO0 + oO00oOOo0Oo + oOoOooOo0o0
  IiI1iiI1III1I = O00O0oOO00O00 ( IIiIIIIii )
  if IiI1iiI1III1I != 'Failed' :
   Oo00o0O0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiI1iiI1III1I )
   for o000O0O , iIIII , OOOiiiiI , I11iII , I11iI1i1I11I11 , i1Ii11II in Oo00o0O0O :
    if O0Ooo in o000O0O . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] - Source Pandoras[/COLOR]' , OOOiiiiI , i1Ii11II , I11iII , I11iI1i1I11I11 , iIIII )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 45 - 45: i1i1I1IIii1II + IIiIiII11i * o0o00Oo0O % oooOo0oo0oo . iI11I1II1I1I
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
     if 55 - 55: III1iiIii
     if 43 - 43: oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1OO0o ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOiiiiI = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( ooO0000o00O ) . replace ( ' ' , '+' )
 if 64 - 64: ooOoO0O00 / I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( OOOiiiiI )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 24 - 24: Ii1I * oO0o . ii % o0ii1I % o0o00Oo0O
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , o000O0O in i1Iii1i1I :
   if ooO0000o00O in o000O0O . lower ( ) :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + OOOiiiiI ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
O000o0O0 = '{ZH},' ; O0000oOoO0o0 = '{IX},' ; IiiIiII1Ii1 = '{LM},'
if 73 - 73: OOooOOo
def Oo0OOOOOOOo0O ( url ) :
 I1III = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( I1III )
 for url , II1 , IiI1ii11I1 , o000O0O in IIi :
  IiI11i1IIiiI ( ( II1 ) . replace ( 'Sezon' , ' Season ' ) + ( IiI1ii11I1 ) . replace ( 'Bölüm' , ' Episode ' ) + o000O0O , url , 8063 , '' )
  if 41 - 41: iI11I1II1I1I - oO0o * III1iiIii
  if 65 - 65: oooOo0oo0oo / oooOo0oo0oo / IiI1i11I * ii
  if 40 - 40: I1ii11iIi11i * ii + III1iiIii
  if 58 - 58: oOo0O0Ooo
def I1iiI1IiI ( url ) :
 I1III = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( I1III )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( o000O0O , url , 222 , '' )
  if 30 - 30: III1iiIii
  if 3 - 3: o0ii1I + oO0o
  if 60 - 60: oO0o . OOooOOo - Ii1I - oOo0O0Ooo - IIiIiII11i % I1ii11iIi11i
  if 62 - 62: o0o00Oo0O + IiI1i11I - IiI1i11I % iI11I1II1I1I
def i1III1i ( ) :
 if 39 - 39: IIiIiII11i - o0ii1I / i1i1I1IIii1II . III1iiIii % oOo0O0Ooo
 I1III = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1III )
 for OOOiiiiI , I11iII , o000O0O , IiI1ii11I1 in IIi :
  IiI11i1IIiiI ( o000O0O + '  -  ' + ( IiI1ii11I1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OOOiiiiI , 8063 , I11iII )
  if 18 - 18: ii * OOooOOo . IIiIiII11i + o0o00Oo0O - ii * I11i
def Ii1IiIiI1Ii ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O , I11iII in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 8002 , I11iII )
def o0oO0oo000oo ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i11 )
 for I11iII , time , url , o000O0O , oooOOO0oooOO in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , time ) , url , 1015 , I11iII , oooOOO0oooOO )
  if 68 - 68: oO0o % III1iiIii - i1i1I1IIii1II - i1iIi . I1ii11iIi11i
def IiII11IIII1 ( ) :
 if 2 - 2: OOooOOo
 IiI11i1IIiiI ( 'Coronation Street' , '' , 8001 , '' )
 IiI11i1IIiiI ( 'Eastenders' , '' , 8002 , '' )
 IiI11i1IIiiI ( 'Emmerdale' , '' , 8003 , '' )
 IiI11i1IIiiI ( 'Hollyoaks' , '' , 8004 , '' )
 IiI11i1IIiiI ( 'Im a Celebrity' , '' , 8005 , '' )
 if 42 - 42: iI11I1II1I1I . oO0o % iI11I1II1I1I * ooOoO0O00
 if 92 - 92: iI11I1II1I1I * Ii1I
 if 5 - 5: i1iIi - i1IiiiI1iI - IiI1i11I
 if 38 - 38: iI11I1II1I1I . o0ii1I
def IIIiIi1iI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'Holly' in o000O0O :
   I11iII = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OOOiiiiI :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , I11iII )
   else :
    pass
    if 34 - 34: oooOo0oo0oo - oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 3 - 3: I1ii11iIi11i + oooOo0oo0oo - oOo0O0Ooo
def Oo0ooIi1ii11i1II11 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'East' in o000O0O :
   I11iII = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OOOiiiiI :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , I11iII )
   else :
    pass
    if 7 - 7: i1IiiiI1iI + i1i1I1IIii1II - ii + I11i % I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: oooOo0oo0oo / ii - Ii1I
def I1iI1i ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'Emmer' in o000O0O :
   I11iII = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OOOiiiiI :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , I11iII )
   else :
    pass
    if 37 - 37: o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: III1iiIii
def iIiIIiII11i1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'Coro' in o000O0O :
   I11iII = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OOOiiiiI :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , I11iII )
   else :
    pass
    if 47 - 47: IiI1i11I / ii - IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: OOooOOo + I11i
def ii11I1IiIIi1i1IIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , o000O0O in IIi :
  if 'Celeb' in o000O0O :
   I11iII = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OOOiiiiI :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OOOiiiiI . replace ( '\\/' , '/' ) , 8006 , I11iII )
   else :
    pass
    if 83 - 83: o0o00Oo0O / oO0o / oOo0O0Ooo
def I1I1IiIiIIi1I ( name , url ) :
 oo0Ooo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oo0Ooo :
  iI1II1III = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i11 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I1i11 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i11 = open_url ( url )
  OOOIi11i1II = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I1i11 ) [ - 1 ]
  iI1II1III = OOOIi11i1II . replace ( '\\/' , '/' )
 iI1iiiIiii = xbmcgui . ListItem ( name , '' , '' )
 iI1iiiIiii . setPath ( iI1II1III )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1iiiIiii )
 if 53 - 53: IIiIiII11i / i1IiiiI1iI / IIiIiII11i % i1IiiiI1iI % Iii % Ii1I
 if 44 - 44: IiI1i11I * oOo0O0Ooo * oOo0O0Ooo % I11i
def OooOO0O0000o ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OOOiiiiI , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for OOOiiiiI , o000O0O in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OOOiiiiI , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 55 - 55: OOooOOo * Ii . Ii1I / IIiIiII11i
def O00oO0OOOo0 ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  if 'Movies' in o000O0O :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( OOOiiiiI ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def o00ooo0O ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iII )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 54 - 54: Ii1I * III1iiIii
  if 3 - 3: III1iiIii - Ii1I * IiI1i11I * Ii1I + I1ii11iIi11i
def o00oOoOo0 ( url ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url , I11iII in IIi :
  if '{{' in o000O0O :
   pass
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I11iII )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IIi1i1iI11I11 = '{UJ},' ; oo0ooOo0O0 = '{WE},' ; ooo0ooO00 = '{WP},' ; OooooO00OOO0 = '{PP},'
def IIIiiI1I ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url , I11iII in IIi :
  if '{{' in o000O0O :
   pass
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iII )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0OO0OoO00oOo ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  IiIoOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIoOo ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: I11i * o0ii1I + I1ii11iIi11i
 if 1 - 1: I11i / IIiIiII11i + Iii . Ii + i1iIi . OOooOOo
 if 95 - 95: I11i / i1IiiiI1iI % IIiIiII11i + i1iIi
def oOo0ooOO0O ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if '(cooltvseries.com)' in o000O0O :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , o000O0O in i1Iii1i1I :
  if '(cooltvseries.com)' in o000O0O :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def IIIII11IIi ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i11 )
 for url in IIi :
  IIIIIIII ( ( url ) . replace ( ' ' , '%20' ) )
i11I1iiI1iI = '{XX},' ; i1i11 = '{UD},' ; OoOO0o000000 = '{YT},' ; O0oooOOoOOO = '{JS},' ; OoO0I1I = '{PF},'
if 63 - 63: i1iIi
def I1iiiiiiiIi1 ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O , I11iII in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( OOOiiiiI ) ) , 222 , I11iII )
  if 90 - 90: I1ii11iIi11i % Ii + o0o00Oo0O % o0o00Oo0O
def iiiI1IiI ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?' , re . DOTALL ) . findall ( I1i11 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i11 )
 for I11iII , url , o000O0O in IIi :
  if 'youtu' in url :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I11iII )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 70 - 70: IIiIiII11i * ii - o0ii1I + i1i1I1IIii1II * o0o00Oo0O
def IIiOO0O000 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 58 - 58: o0o00Oo0O / OOooOOo
def ii1Ii ( url ) :
 I1i11 = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 222 , I11iII )
  if 42 - 42: IiI1i11I
  if 6 - 6: oO0o + oooOo0oo0oo
  if 22 - 22: I1ii11iIi11i . ii % i1IiiiI1iI
  if 16 - 16: Ii1I
  if 78 - 78: oO0o * iI11I1II1I1I
def oOoOOoooO00oO ( ) :
 if 62 - 62: o0ii1I
 IiI11i1IIiiI ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 4 - 4: iI11I1II1I1I . I1ii11iIi11i - Ii
 if 51 - 51: OOooOOo - Ii / oOo0O0Ooo % o0ii1I * o0ii1I % i1iIi
def i1Iiiii111i ( Cat_Name ) :
 if 79 - 79: iI11I1II1I1I / Ii - ooOoO0O00 + o0ii1I - Iii . i1IiiiI1iI
 O00Oo = False
 oOOo = '0'
 if Cat_Name == 'All Channels' : O00Oo = True
 if Cat_Name == 'Entertainment' : oOOo = '1'
 if Cat_Name == 'Movies' : oOOo = '2'
 if Cat_Name == 'Music' : oOOo = '3'
 if Cat_Name == 'News' : oOOo = '4'
 if Cat_Name == 'Sports' : oOOo = '5'
 if Cat_Name == 'Documentary' : oOOo = '6'
 if Cat_Name == 'Kids' : oOOo = '7'
 if Cat_Name == 'Food' : oOOo = '8'
 if Cat_Name == 'Religious' : oOOo = '9'
 if Cat_Name == 'USA Channels' : oOOo = '10'
 if Cat_Name == 'Other' : oOOo = '11'
 if 93 - 93: OOooOOo . Iii % Ii
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i11 )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for o000O0O , I11iII , o0OOoooOo0O0o in IIi :
  O0oOOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iII ) . replace ( '\\' , '' )
  if o0OOoooOo0O0o == oOOo :
   IiI11i1IIiiI ( o000O0O , '' , 7022 , O0oOOO )
  elif O00Oo == True :
   IiI11i1IIiiI ( o000O0O , '' , 7022 , O0oOOO )
  else : pass
  if 48 - 48: i1iIi * iI11I1II1I1I % OOooOOo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: IIiIiII11i - Ii + oO0o % i1iIi - iI11I1II1I1I * Ii
def IIiI111iI1iiii ( Search_Name ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i11 )
 for I11iII , OOOiiiiI , i1iiIIiI1iiI , I11Ii111I in IIi :
  O0oOOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iII ) . replace ( '\\' , '' )
  oOOo000oOoO0 ( Search_Name + ': Link 1' , ( OOOiiiiI ) . replace ( '\\' , '' ) , 222 , O0oOOO )
  oOOo000oOoO0 ( Search_Name + ': Link 2' , ( i1iiIIiI1iiI ) . replace ( '\\' , '' ) , 222 , O0oOOO )
  oOOo000oOoO0 ( Search_Name + ': Link 3' , ( I11Ii111I ) . replace ( '\\' , '' ) , 222 , O0oOOO )
  if 55 - 55: i1IiiiI1iI / ii . i1iIi / oO0o
def iiii1I1ii1 ( ) :
 I1i11 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  oOOo000oOoO0 ( o000O0O , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def iiiIiIiiiII11i ( ) :
 I1i11 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  oOOo000oOoO0 ( o000O0O , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def I1oO0oO00OO00 ( ) :
 I1i11 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i11 )
 for o000O0O , OOOiiiiI in IIi :
  oOOo000oOoO0 ( o000O0O , ( OOOiiiiI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 75 - 75: I11i + oOo0O0Ooo % i1iIi * i1IiiiI1iI
def Oooo000 ( url ) :
 url
 ii1 = xbmcgui . ListItem ( o000O0O , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 return
 if 52 - 52: iI11I1II1I1I / IiI1i11I . o0o00Oo0O * III1iiIii . oOo0O0Ooo
 if 67 - 67: IIiIiII11i + o0ii1I - oOo0O0Ooo * i1iIi
def iiIiiIii1IiI ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i11 )
 for url , iIIII , I11iII , o000O0O in IIi :
  I1I1II1I11 ( o000O0O , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I11iII , '' , ( iIIII ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 71 - 71: iI11I1II1I1I + o0o00Oo0O . III1iiIii . IiI1i11I % I11i % o0o00Oo0O
def OOO00o0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIII , I11iII in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I11iII , '' , iIIII )
  Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 ii111IIiiiiI = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oooo0 in ii111IIiiiiI :
  IiIIi1 = ( oooo0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I11iII , '' , IiIIi1 )
  if 64 - 64: i1iIi / ooOoO0O00
def ooo00 ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 56 - 56: oooOo0oo0oo - i1IiiiI1iI
 if 63 - 63: oOo0O0Ooo * oooOo0oo0oo . iI11I1II1I1I * OOooOOo . ii
 if 6 - 6: o0o00Oo0O . I11i - OOooOOo
def Ii1i11IIiI ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( ( o000O0O ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def III1i1 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , url , 9032 , iiIi1IIiIi + 'icon.png' )
def Oo00oooO00o ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  if '=' in o000O0O :
   pass
  else :
   oOOo000oOoO0 ( ( o000O0O ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def oooO0Oo0O ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  if '=' in o000O0O :
   pass
  else :
   oOOo000oOoO0 ( o000O0O , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 15 - 15: oO0o - OOooOOo
   if 41 - 41: o0ii1I * Iii
   if 13 - 13: I1ii11iIi11i * I11i * IiI1i11I
def o0Ooo0 ( url ) :
 I1i ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , I11iII , url in IIi :
  if 'music' in url :
   I1i ( o000O0O , url , 90036 , I11iII , I11iII , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   I1i ( o000O0O , url , 90039 , I11iII , I11iII , '' , '' )
def O00O0oO ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( I1i11 )
 for o000O0O , url , I11iII in IIi :
  i1i1I ( o000O0O , url , 100009 , I11iII , I11iII , '' , '' )
  if 48 - 48: Ii1I - I1ii11iIi11i - i1iIi . I11i . I11i
def ii1oO0Oo ( url ) :
 I1i ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I1i ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 I1i11 = requests . get ( url ) . text
 O0i1iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i11 )
 O00OooOo00o = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 for url , I11iII , o000O0O in IIi :
  o0ooo00o = requests . get ( url ) . text
  iIi1IIIi1Ii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0ooo00o )
  for oOo00OO in iIi1IIIi1Ii :
   Ii1IiIIIi1i = requests . get ( oOo00OO ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii1IiIIIi1i )
   for OooOO , iI1i1Iiii , i1iII1IiiIiI1 , oO0oO0O , iiI111I1iIiI in IIi :
    if OooOO == 'xyz' :
     II111Ii1I1I = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( o000O0O , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
    else :
     II111Ii1I1I = 'http://' + oO0oO0O + '.' + i1iII1IiiIiI1 + '.' + iI1i1Iiii + '.' + OooOO + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( o000O0O , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
 for I11iiii in O0i1iI :
  I1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , I11iiii , 1000111 , '' , '' , '' , '' )
  if 87 - 87: IiI1i11I
  if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oO0o
  if 32 - 32: Ii - OOooOOo * Iii . I1ii11iIi11i * i1iIi
def iiI1I1iii1 ( ) :
 I1i ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 21 - 21: iI11I1II1I1I + oooOo0oo0oo . Ii1I % oooOo0oo0oo + o0ii1I + iI11I1II1I1I
 if 64 - 64: o0ii1I * oooOo0oo0oo * i1i1I1IIii1II
def ooO0O0oO ( url , name ) :
 I1i ( name , '' , '' , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I1i11 = requests . get ( url ) . text
 O0i1iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i11 )
 O00OooOo00o = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 for url , I11iII , name in IIi :
  o0ooo00o = requests . get ( url ) . text
  iIi1IIIi1Ii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0ooo00o )
  for oOo00OO in iIi1IIIi1Ii :
   Ii1IiIIIi1i = requests . get ( oOo00OO ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii1IiIIIi1i )
   for OooOO , iI1i1Iiii , i1iII1IiiIiI1 , oO0oO0O , iiI111I1iIiI in IIi :
    if OooOO == 'xyz' :
     II111Ii1I1I = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( name , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
    else :
     II111Ii1I1I = 'http://' + oO0oO0O + '.' + i1iII1IiiIiI1 + '.' + iI1i1Iiii + '.' + OooOO + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( name , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
     if 1 - 1: ooOoO0O00
 for I11iiii in O0i1iI :
  I1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , I11iiii , 1003111 , '' , '' , '' , '' )
  if 44 - 44: Iii - Ii
  if 93 - 93: IiI1i11I % Ii - OOooOOo . o0ii1I
def ooo0oO0o000O0 ( ) :
 I1i ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 26 - 26: ii . ooOoO0O00 + oO0o
 if 42 - 42: Ii * I11i % Iii % I1ii11iIi11i + I11i * Ii
 if 66 - 66: o0ii1I / III1iiIii . ii * I1ii11iIi11i % Ii
def OO0oOo00OO0 ( url , name ) :
 I1i ( name , '' , '' , '' , '' , '' , '' )
 I1i ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 I1i11 = requests . get ( url ) . text
 O0i1iI = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i11 )
 O00OooOo00o = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( I1i11 )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 for url , I11iII , name in IIi :
  o0ooo00o = requests . get ( url ) . text
  iIi1IIIi1Ii = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0ooo00o )
  for oOo00OO in iIi1IIIi1Ii :
   Ii1IiIIIi1i = requests . get ( oOo00OO ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( Ii1IiIIIi1i )
   for OooOO , iI1i1Iiii , i1iII1IiiIiI1 , oO0oO0O , iiI111I1iIiI in IIi :
    if OooOO == 'xyz' :
     II111Ii1I1I = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( name , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
    else :
     II111Ii1I1I = 'http://' + oO0oO0O + '.' + i1iII1IiiIiI1 + '.' + iI1i1Iiii + '.' + OooOO + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     i1i1I ( name , II111Ii1I1I , 1001111 , I11iII , I11iII , '' , '' )
     if 25 - 25: I1ii11iIi11i * III1iiIii % oOo0O0Ooo . IiI1i11I % IiI1i11I * I1ii11iIi11i
 for I11iiii in O0i1iI :
  I1i ( '[COLORblue][B]NEXT[/B][/COLOR]' , I11iiii , 1005111 , '' , '' , '' , '' )
def o0OoO000O ( name , url ) :
 import urlresolver
 try :
  OOo = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( OOo , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 1 - 1: I1ii11iIi11i / i1iIi * o0ii1I - ii * Iii * oooOo0oo0oo
 if 63 - 63: IIiIiII11i - I11i * Ii / Iii * IiI1i11I - IiI1i11I
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
def iIIi1i111iI ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  if 'Daily' in o000O0O :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 9008 , O0O )
def i1iIi1I1II1 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def i11iIi ( url ) :
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  oOOo000oOoO0 ( ( o000O0O ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 45 - 45: iI11I1II1I1I % o0ii1I - OOooOOo
def i1IOoOo0O0 ( ) :
 I1i11 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  if '.m3u' in OOOiiiiI :
   IiI11i1IIiiI ( ( o000O0O ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + OOOiiiiI ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def OOoOOoo ( url ) :
 I1i11 = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  oOOo000oOoO0 ( ( o000O0O ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 83 - 83: IiI1i11I + OOooOOo % i1iIi
def Ooo0o00o0o ( ) :
 I1i11 = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  if 'category' in OOOiiiiI :
   IiI11i1IIiiI ( o000O0O , 'http://www.disclose.tv/' + OOOiiiiI , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 76 - 76: ooOoO0O00 % oOo0O0Ooo + ooOoO0O00
   if 2 - 2: IiI1i11I + IiI1i11I
def oooOo0O ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i11 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i11 )
 for url , o000O0O , I11iII in IIi :
  IiI11i1IIiiI ( o000O0O , 'http://www.disclose.tv/' + url , 7011 , I11iII )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 53 - 53: ii * oOo0O0Ooo - oO0o . Ii / I1ii11iIi11i - ooOoO0O00
  if 48 - 48: IiI1i11I
def i1IIiIiI11 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i11 )
 IIIIiIiIi1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  if 'http' in url :
   oOOo000oOoO0 ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , o000O0O in i1Iii1i1I :
  oOOo000oOoO0 ( o000O0O , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in IIIIiIiIi1 :
  oOOo000oOoO0 ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 61 - 61: Ii % i1IiiiI1iI / I11i
  if 40 - 40: oooOo0oo0oo / o0ii1I % oOo0O0Ooo / I11i . IiI1i11I
def o00o0Ooo ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 20 - 20: OOooOOo / I11i % OOooOOo * oOo0O0Ooo
def i1IiiiI1Ii ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iii111III1ii1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Ii1IIiiIi1iii = len ( iii111III1ii1 )
 if 42 - 42: I11i - i1iIi . oooOo0oo0oo / IiI1i11I / I11i . III1iiIii
 if 46 - 46: i1IiiiI1iI % o0o00Oo0O % oO0o * III1iiIii % i1IiiiI1iI % IIiIiII11i
 if Ii1IIiiIi1iii == 1 :
  for ii1Iii1iiI11 in iii111III1ii1 :
   ii1Iii1iiI11 = ii1Iii1iiI11 . replace ( 'player' , 'watch' )
   i11ii1II = ii1Iii1iiI11 + '&fv=&sou='
   ooOo00OOo0 = OooOoooOo ( i11ii1II )
   ii1IIi = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( ooOo00OOo0 )
   for IiIiiiiI1 in ii1IIi :
    iii1Ii = False
    Resolve ( IiIiiiiI1 )
    if 98 - 98: Iii / Ii - I11i % I11i
 elif Ii1IIiiIi1iii > 1 :
  if 31 - 31: Iii
  for ii1Iii1iiI11 in iii111III1ii1 :
   Oooo0o00Oo00 = OooOoooOo ( ii1Iii1iiI11 )
   OoooOoo0Oooo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oooo0o00Oo00 )
   i1O0o0oO = OoooOoo0Oooo
   i1O0o0oO = ( str ( i1O0o0oO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i1O0o0oO
   oOOo000oOoO0 ( 'DOUBLE LINK' , i1O0o0oO , 424 , '' )
   if 33 - 33: ooOoO0O00 * I11i + Ii1I - ooOoO0O00 % ii
   for url in OoooOoo0Oooo :
    IiI11i1IIiiI ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i1iiIIiI1iiI = Google . resolve ( url )
    except :
     pass
    try :
     o0OiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i1iiIIiI1iiI ) )
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
 IiI11i1IIiiI ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 71 - 71: oO0o + Ii % ii - I11i % III1iiIii / IIiIiII11i
 IiI11i1IIiiI ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 20 - 20: oooOo0oo0oo . I1ii11iIi11i * IIiIiII11i / iI11I1II1I1I % Ii1I
 if 11 - 11: I11i * oO0o
def oO0IiiI1i1i11I1 ( ) :
 I1i11 = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , 'http://cnfstudio.com/genre/' + OOOiiiiI , 7003 , iiIi1IIiIi + 'icon.png' )
  if 97 - 97: OOooOOo - oO0o
iIii1 = xbmcgui . Dialog ( )
if 64 - 64: ooOoO0O00 / ii / Ii1I - I1ii11iIi11i + i1i1I1IIii1II
iI1i1II11I = '{UN},' ; OoO0o0oOOoOoo = '{IG},' ; I1iIiiiI1II1 = '{PL},' ; o0OOo00Oo00 = '{LO},' ; iII1IoOoOo0O00Oo = '{LP},' ; Iiii1iiIi = '{HA},' ; oOoOO = '{XD},' ; i1iIiII111i11 = '{TA},' ; i1iIiiii = '{DP},' ; O0o0oOo0OooO = '{JT},' ; iI1 = '{JJ},' ; IiI1 = '{MM},' ; o0o0ooo = '{FQ},' ; oOooO = '{HH},'
if 52 - 52: IiI1i11I * i1i1I1IIii1II + ii
def iiii1iIiI11I ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i11 )
 i1i11Ii1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i11 )
 for I11iII , url , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I11iII )
 i1i11Ii1 = i1i11Ii1
 for url in i1i11Ii1 :
  IiI11i1IIiiI ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 14 - 14: oooOo0oo0oo . I11i / IIiIiII11i % oooOo0oo0oo
def oOO0O0 ( url ) :
 if 18 - 18: oOo0O0Ooo / Ii - o0ii1I
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  ooOo0O0o = IiIIIIII ( iiI111I1iIiI )
  OOO0O = IiIIIIII ( url )
  if 24 - 24: i1iIi % oooOo0oo0oo . o0o00Oo0O * I1ii11iIi11i
  if 52 - 52: o0o00Oo0O . i1IiiiI1iI + IiI1i11I / Ii
def IiIIIIII ( url ) :
 if 52 - 52: i1i1I1IIii1II % I1ii11iIi11i * IIiIiII11i
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I1i11 )
 for url in IIi :
  IiIIoOo ( url )
  if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
  if 27 - 27: ooOoO0O00 - i1i1I1IIii1II + oooOo0oo0oo
def i1i1iiI11I ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 78 - 78: OOooOOo % oO0o - o0ii1I / oooOo0oo0oo
def ooOo000 ( ) :
 if os . path . exists ( II ) :
  OO0o0oo = open ( II , 'r' )
  for ii1 in OO0o0oo :
   o00I11II1iI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ii1 )
   for o000O0O , OOOiiiiI in o00I11II1iI :
    oOOo000oOoO0 ( o000O0O , OOOiiiiI , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 19 - 19: o0o00Oo0O
def O0oo0O0OO0OOo ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = ii1IIIIiI11 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for o000O0O , url in IIi :
   url = ( url ) . strip ( )
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
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
 o000O0O = 'plugin.video.GenieTv'
 if 41 - 41: Iii . Ii1I
 Oo00o0Ooo0OOo ( OOOiiiiI , o000O0O )
 if 39 - 39: IiI1i11I - oO0o
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI in IIi :
  OOOiiiiI = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OOOiiiiI
 o000O0O = 'repository.GenieTv'
 if 1 - 1: ii - i1iIi
 Oo00o0Ooo0OOo ( OOOiiiiI , o000O0O )
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
iiiiiI = 'https://addons.tvaddons.ag/'
if 46 - 46: i1iIi % oooOo0oo0oo + IIiIiII11i * ooOoO0O00
def I1II11iiii ( ) :
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 iIIiiII11i1I1 = 'https://addons.tvaddons.ag/search/?keyword=' + O0Ooo
 II11iIiIIIiI = OooOoooOo ( iIIiiII11i1I1 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , IioO0oOOO0Ooo , o000O0O in IIi :
  I1I1II1I11 ( o000O0O , OOOiiiiI , 10054 , 'https://addons.tvaddons.ag/' + IioO0oOOO0Ooo , Oo00OOOOO , '' )
  if 81 - 81: i1i1I1IIii1II - I11i + IiI1i11I
  if 49 - 49: ii
def o0oO ( ) :
 II11iIiIIIiI = OooOoooOo ( iiiiiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  if 'Repositories' in o000O0O :
   pass
  elif 'Services' in o000O0O :
   pass
  elif 'International' in o000O0O :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , OOOiiiiI , 10053 , 'https://addons.tvaddons.ag/' + I11iII , Oo00OOOOO , '' )
   if 74 - 74: oooOo0oo0oo - IIiIiII11i
   if 66 - 66: Ii + i1IiiiI1iI . i1iIi
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0i1iI = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , I11iII , o000O0O in IIi :
  if 'Please' in o000O0O :
   pass
  else :
   Ii1I1i ( o000O0O , url , 10054 , 'https://addons.tvaddons.ag/' + I11iII , Oo00OOOOO , '' )
 for url in O0i1iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 46 - 46: i1IiiiI1iI / Ii1I
  if 41 - 41: ooOoO0O00 % o0ii1I + i1IiiiI1iI . I1ii11iIi11i / iI11I1II1I1I
def OOooOOO000 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , name + '.zip' )
   try :
    os . remove ( Ii1IIiI1io0O00Oo0 )
   except :
    pass
   downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
   IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print IiII111i1i11
   print '======================================='
   extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
   oooO ( )
   if 88 - 88: III1iiIii / iI11I1II1I1I - Iii + OOooOOo + I11i
def Oo00o0Ooo0OOo ( url , name ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , name + '.zip' )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 IiII111i1i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiII111i1i11
 print '======================================='
 extract . all ( Ii1IIiI1io0O00Oo0 , IiII111i1i11 , o0oOoO00o )
 oooO ( )
 if 28 - 28: i1iIi + ooOoO0O00 * oO0o . o0ii1I + i1iIi
def oooO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 41 - 41: Ii1I . OOooOOo - III1iiIii * i1IiiiI1iI
 if 14 - 14: IIiIiII11i
def oOOiI ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , IioO0oOOO0Ooo , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , url , 1007 , IioO0oOOO0Ooo )
def O0O0 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , IioO0oOOO0Ooo , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 1006 , IioO0oOOO0Ooo )
  if 91 - 91: ii - i1i1I1IIii1II * I11i * o0ii1I / III1iiIii % I1ii11iIi11i
def Oo0OooO ( ) :
 I1i11 = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , i1iIiIi1I , iIIII , I11iI1i1I11I11 , o000O0O in IIi :
  I11iiIi1i1I ( o000O0O , 100109 , OOOiiiiI , image = i1iIiIi1I , isFolder = True )
  if 3 - 3: Ii / oooOo0oo0oo * iI11I1II1I1I * Iii - o0ii1I . Iii
def O0Oooo0OoOOo ( url ) :
 import random
 O0Oo00o0o = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 O0Oo00o0o . clear ( )
 OoiIII1Ii1 = [ ]
 I1111i1I = [ ]
 OOOoO0o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1iiIIiI1iiI , i1iIiIi1I , iIIII , I11iI1i1I11I11 , o000O0O in IIi :
  OoiIII1Ii1 . append ( [ i1iiIIiI1iiI , o000O0O ] )
  if len ( OoiIII1Ii1 ) == len ( IIi ) :
   for ii1 in OoiIII1Ii1 :
    OOoooOO0o = random . randint ( 1 , len ( OoiIII1Ii1 ) )
    try :
     O00oo0Ooo = OoiIII1Ii1 [ int ( OOoooOO0o ) ]
    except :
     pass
    if len ( I1111i1I ) <= 20 :
     if O00oo0Ooo [ 1 ] not in OOOoO0o :
      o0o = OooOoooOo ( O00oo0Ooo [ 0 ] )
      IIIIiIiIi1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for iIiI , iIi1Iii in IIIIiIiIi1 :
       OOoOoo = OooOoooOo ( iIiI )
       O0o0oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for OoOO0OooOoooo , iiI111I1iIiI in O0o0oO :
        if 'panda' in iiI111I1iIiI :
         o0o0OoOOOOOo = OooOoooOo ( iiI111I1iIiI )
         I1III11iiii11i1 = re . compile ( "url: '(.+?)'" ) . findall ( o0o0OoOOOOOo )
         for IIIiiiIii1111Ii1I1 in I1III11iiii11i1 :
          if 'http' in IIIiiiIii1111Ii1I1 :
           iI1iiiIiii = xbmcgui . ListItem ( O00oo0Ooo [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : O00oo0Ooo [ 1 ] } )
           iI1iiiIiii . setProperty ( "IsPlayable" , "true" )
           O0Oo00o0o . add ( IIIiiiIii1111Ii1I1 , iI1iiiIiii )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iI1iiiIiii )
           if 63 - 63: III1iiIii % o0o00Oo0O * i1iIi % I11i . IIiIiII11i + I1ii11iIi11i
def I11iiIi1i1I ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 O0ooOoO = sys . argv [ 0 ]
 O0ooOoO += '?mode=' + str ( mode )
 O0ooOoO += '&title=' + urllib . quote_plus ( name )
 O0ooOoO += '&image=' + urllib . quote_plus ( image )
 O0ooOoO += '&page=' + str ( page )
 if url != '' :
  O0ooOoO += '&url=' + urllib . quote_plus ( url )
 if keyword :
  O0ooOoO += '&keyword=' + urllib . quote_plus ( keyword )
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  iI1iiiIiii . addContextMenuItems ( contextMenu )
 if infoLabels :
  iI1iiiIiii . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  iI1iiiIiii . setProperty ( "IsPlayable" , "true" )
 iI1iiiIiii . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = isFolder )
 if 98 - 98: IiI1i11I
 if 56 - 56: oOo0O0Ooo . Iii % IiI1i11I
def iIIii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , iconimage , iIIII , I11iI1i1I11I11 , name in IIi :
  if 'http' in url :
   if '.php' in url :
    iIiI1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for ii1 in iIiI1 :
     if ii1 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oooO00oOOooO ( name , url , 1016 , iconimage , I11iI1i1I11I11 , iIIII )
   else :
    if 'youtube' in url :
     iIiI1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ii1 in iIiI1 :
      if ii1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i11iII1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , I11iI1i1I11I11 , iIIII )
    else :
     iIiI1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ii1 in iIiI1 :
      if ii1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i11iII1 ( name , url , 222 , iconimage , I11iI1i1I11I11 , iIIII )
     Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
  else :
   I1I1i ( url , iconimage , name )
   if 67 - 67: OOooOOo . o0o00Oo0O + ooOoO0O00 . Ii % III1iiIii / iI11I1II1I1I
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
  for url , IioO0oOOO0Ooo , name in IIi :
   if 'http' in url :
    if '.php' in url :
     IiI11i1IIiiI ( name , url , 1016 , IioO0oOOO0Ooo )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOOo000oOoO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo )
     else :
      iIiI1 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ii1 in iIiI1 :
       if ii1 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOOo000oOoO0 ( name , url , 222 , IioO0oOOO0Ooo )
      Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
   else :
    I1I1i ( url , IioO0oOOO0Ooo , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 28 - 28: o0ii1I
def I1I1i ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Oo0ooO00 = ( url ) . replace ( O0000oOoO0o0 , 'http' ) . replace ( i1i11 , '.com' ) ;
 o0OO0O0o = ( Oo0ooO00 ) . replace ( IiiIiII1Ii1 , 'a' ) . replace ( II1iii111 , 'b' ) . replace ( ooOooo , 'c' ) . replace ( oo0ooOo0O0 , 'd' ) . replace ( I1iIiiiI1II1 , 'e' ) . replace ( O0o0oOo0OooO , 'f' ) ;
 IiII11iii = ( o0OO0O0o ) . replace ( i11I1iiI1iI , 'g' ) . replace ( Iiii1iiIi , 'h' ) . replace ( OoOO0o000000 , 'i' ) . replace ( OoO0I1I , 'j' ) . replace ( Oo00 , 'k' ) . replace ( o0OO00oOO00 , 'l' ) ;
 oooOOo0Oo0OO0O = ( IiII11iii ) . replace ( I1iO00oo0oOo , 'm' ) . replace ( iiiIiioO00o , 'n' ) . replace ( IiIi1i1 , 'o' ) . replace ( o0000o0o , 'p' ) . replace ( O0OO000o , 'q' ) . replace ( iI1I1iI1ii , 'r' ) ;
 IiIIi1I = ( oooOOo0Oo0OO0O ) . replace ( iii11iI , 's' ) . replace ( ooo0ooO00 , 't' ) . replace ( ii1II1i1 , 'u' ) . replace ( oOOOOOOooO , 'v' ) . replace ( i1iI1Iii11Iii11 , 'w' ) . replace ( iIiiI , 'x' ) ;
 OOo000 = ( IiIIi1I ) . replace ( iI1iIIiIi1I1 , 'y' ) . replace ( oOo0oO0 , 'z' ) . replace ( iI1i1II11I , '.' ) . replace ( OoO0o0oOOoOoo , '(' ) . replace ( o0OOo00Oo00 , ')' ) . replace ( iII1IoOoOo0O00Oo , '/' ) ;
 iiIiIiiI1Ii = ( OOo000 ) . replace ( O000o0O0 , '1' ) . replace ( OooooO00OOO0 , '2' ) . replace ( iIIiiii , '3' ) . replace ( i1iIiII111i11 , '4' ) . replace ( i1iIiiii , '5' ) . replace ( O0oooOOoOOO , '6' ) ;
 ii111Ii = ( iiIiIiiI1Ii ) . replace ( iI1 , '7' ) . replace ( IiI1 , '8' ) . replace ( o0o0ooo , '9' ) . replace ( oOooO , '0' ) . replace ( iiiiiIi1II1i , ':' ) . replace ( II1II11I11ii , '%' ) ;
 url = ( ii111Ii ) . replace ( IIi1i1iI11I11 , '-' ) . replace ( oOoOO , '_' ) ;
 oOOo000oOoO0 ( name , url , 222 , iconimage ) ;
 if 82 - 82: OOooOOo * Iii . i1IiiiI1iI . i1i1I1IIii1II . I11i
 if 58 - 58: i1IiiiI1iI * oO0o * ooOoO0O00
def IiiIi1II ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for OOOiiiiI , IioO0oOOO0Ooo , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 1007 , IioO0oOOO0Ooo )
def IiII1IiiI ( url ) :
 if 57 - 57: i1i1I1IIii1II
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , IioO0oOOO0Ooo , o000O0O in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 1006 , IioO0oOOO0Ooo )
  if 44 - 44: IiI1i11I / oooOo0oo0oo
def ooO0oo00o00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 o0O0oo0OO0O = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 o0O0oo0OO0O . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0O0oo0OO0O )
 if 94 - 94: i1i1I1IIii1II + ii - OOooOOo . i1IiiiI1iI / Iii . III1iiIii
 if 66 - 66: ooOoO0O00
def O00oIii1iIIiii1ii ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i11 )
 for url , I11iII , o000O0O in IIi :
  if '-dir-' in o000O0O :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , I11iII )
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' , url , 1006 , I11iII )
   if 19 - 19: i1iIi / i1i1I1IIii1II . o0ii1I / I11i
def iIII1 ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 Iii11 = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if '[To Parent Directory]' in o000O0O :
   o000O0O = 'HOME'
   pass
  elif 'HOME' in o000O0O :
   pass
  elif '.m3u' in o000O0O :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , Iii11 + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in o000O0O :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Iii11 + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in o000O0O :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Iii11 + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) , Iii11 + url , 1012 , iiIi1IIiIi + 'music.png' )
def iII1Ii1ii111 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I11iII , o000O0O , url in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 22 - 22: o0ii1I
def I1IIi1I11iI ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 Iii11 = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  if '.mp3' in o000O0O :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '/' , '' ) , Iii11 + url , 1011 , iiIi1IIiIi + 'music.png' )
def O0II ( ) :
 I1i11 = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i11 )
 for OOOiiiiI , I11iII , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , ( 'http://www.cyn.net/music/' + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I11iII ) . replace ( ' ' , '%20' ) )
def IIiII1ii1i11I ( url , img ) :
 I1i11 = ii1IIIIiI11 ( url )
 i1iiIIiI1iiI = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i1iiIIiI1iiI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 76 - 76: oO0o + i1IiiiI1iI + oO0o * ii
def Ii111IIIIii ( url ) :
 I1i11 = ii1IIIIiI11 ( url )
 i1iiIIiI1iiI = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i11 )
 for type , url , o000O0O in IIi :
  if '[VID]' in type :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i1iiIIiI1iiI + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   Ii111IIIIii ( i1iiIIiI1iiI + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
def Ii1iii11I ( ) :
 iiIIi = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 ooO0000o00O = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo = ooO0000o00O . lower ( )
 OOOiiiiI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 IiIi1iI11 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i1iiIIiI1iiI = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 53 - 53: o0ii1I - oooOo0oo0oo
 II11iIiIIIiI = O00O0oOO00O00 ( OOOiiiiI )
 I1III1111iIi = O00O0oOO00O00 ( IiIi1iI11 )
 o0o = O00O0oOO00O00 ( i1iiIIiI1iiI )
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OOOiiiiI , i1iIiIi1I , iIIII , I1i11II , o000O0O in IIi :
   if ooO0000o00O in o000O0O . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , OOOiiiiI , 1016 , i1iIiIi1I , I11iI1i1I11I11 , iIIII )
    if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if I1III1111iIi != 'Failed' :
  O0oOOo0o = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
  for OOOiiiiI , o000O0O in O0oOOo0o :
   if ooO0000o00O in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 23 - 23: iI11I1II1I1I * Iii . i1IiiiI1iI - I11i
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for OOOiiiiI , o000O0O in i1Iii1i1I :
   if ooO0000o00O in o000O0O . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + OOOiiiiI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 66 - 66: oOo0O0Ooo * i1IiiiI1iI / Ii / oooOo0oo0oo
    Ii1IIiI1i ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: i1iIi % iI11I1II1I1I * ii
    if 60 - 60: i1IiiiI1iI * IiI1i11I / ii * I1ii11iIi11i
    if 47 - 47: IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
    if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
    if 99 - 99: Ii1I % I1ii11iIi11i
    if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
I1iO00oo0oOo = '{SF},' ; iiiIiioO00o = '{IF},' ; IiIi1i1 = '{PW},' ; iIIiiii = '{AM},' ; o0000o0o = '{GF},' ; O0OO000o = '{DD},' ; iI1I1iI1ii = '{UO},' ; iii11iI = '{LE},' ; ii1II1i1 = '{ZY},' ; oOOOOOOooO = '{UE},' ; i1iI1Iii11Iii11 = '{PE},' ; iIiiI = '{JE},' ; iI1iIIiIi1I1 = '{TH},' ; oOo0oO0 = '{LK},'
if 57 - 57: oooOo0oo0oo / Ii / i1IiiiI1iI - I1ii11iIi11i . iI11I1II1I1I
if 84 - 84: III1iiIii
def O00oO0 ( ) :
 I1i11 = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 8021 , iiIi1IIiIi + 'iwatch.png' )
  Ii1IIiI1i ( 'movies' , 'MAIN' )
def iiiOOoO00o0OO ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i11 )
 for url , o000O0O , O0OoO0oooOO in IIi :
  IiI11i1IIiiI ( o000O0O + O0OoO0oooOO , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def IIiiIIIi1II ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i11 )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  i11IIii1iI11 ( url )
def i11IIii1iI11 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1i11 )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1i11 )
 IIIIiIiIi1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i11 )
 O0o0oO = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  oOOo000oOoO0 ( 'VidSpot - ' + o000O0O , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  oOOo000oOoO0 ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , o000O0O in O0o0oO :
  oOOo000oOoO0 ( 'VidUp' + o000O0O , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for o000O0O , url in IIIIiIiIi1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOOo000oOoO0 ( 'TheVideo - ' + o000O0O , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 2 - 2: IiI1i11I * Iii * i1iIi + Ii + i1i1I1IIii1II
def oOOo0ooOOoO0 ( ) :
 I1i11 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 1021 , iiIi1IIiIi + 'anime.png' )
  if 75 - 75: Ii % o0ii1I
  if 64 - 64: OOooOOo + IiI1i11I * OOooOOo - oOo0O0Ooo * ii
def iiiiii ( ) :
 I1i11 = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i11 )
 for OOOiiiiI , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , OOOiiiiI , 1002 , iiIi1IIiIi + 'anime.png' )
  if 76 - 76: IIiIiII11i % i1iIi - Ii1I
  if 50 - 50: IIiIiII11i / oOo0O0Ooo . o0ii1I % Ii
  if 66 - 66: i1i1I1IIii1II / oooOo0oo0oo / IiI1i11I
def i1Io0ooo ( url ) :
 I1i11 = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i11 )
 for I11iII in i1Iii1i1I :
  o0oooIi1Iii1 = I11iII
 IIIIiIiIi1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i11 )
 for url in IIIIiIiIi1 :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i11 )
 for url , o000O0O in IIi :
  IiI11i1IIiiI ( o000O0O , url , 1003 , o0oooIi1Iii1 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIIIII1iiI ( url , IMAGE ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i11 )
 for o000O0O , url in IIi :
  print o000O0O + '     ' + url
  if 'easy' in url :
   iIiiI11iI111 ( url )
  elif 'playpanda' in url :
   iIiiI11iI111 ( url )
   if 28 - 28: i1i1I1IIii1II . i1iIi / Iii + I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIiiI11iI111 ( url ) :
 I1i11 = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i11 )
 for url in IIi :
  oOOo000oOoO0 ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 55 - 55: ii % OOooOOo + ooOoO0O00 * oO0o * oooOo0oo0oo
  if 39 - 39: oooOo0oo0oo - i1i1I1IIii1II
def oO00OOooOOOoO ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 60 - 60: oO0o
def ii1IIIIiI11 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 16 - 16: Iii
def iII11i1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooooo0oo0OO = ( '%s%s' % ( IIiII , url ) )
 iiI111I1iIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , IioO0oOOO0Ooo , o000O0O in IIi :
  oOOo000oOoO0 ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + o000O0O + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IioO0oOOO0Ooo )
  if 58 - 58: IiI1i11I
def o00OO0O00O0 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  IiiI11I ( url , o000O0O )
 else :
  O0oOOoooOO0O ( url )
def O0oOOoooOO0O ( url ) :
 import urlresolver
 try :
  OOo = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOo , xbmcgui . ListItem ( o000O0O ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( o000O0O ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def IiIIoOo ( url ) :
 if 63 - 63: OOooOOo
 iIIiI1ii = open ( OOOO0OOoO0O0 , "a" )
 iIIiI1ii . write ( 'url="' + url + '"\n' )
 iIIiI1ii . close
 if 22 - 22: o0o00Oo0O + o0o00Oo0O + I1ii11iIi11i - i1iIi
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 try : I1iiiiii . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( o000O0O ) )
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1iiiiii . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def IiiI11I ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OOO0ooO0Oo0 = '.mp4'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.mkv' in url :
  OOO0ooO0Oo0 = '.mkv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.mp3' in url :
  OOO0ooO0Oo0 = '.mp3'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.avi' in url :
  OOO0ooO0Oo0 = '.avi'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.mov' in url :
  OOO0ooO0Oo0 = '.mov'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.mpeg' in url :
  OOO0ooO0Oo0 = '.mpeg'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.mpg' in url :
  OOO0ooO0Oo0 = '.mpg'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.flv' in url :
  OOO0ooO0Oo0 = '.flv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 elif '.wmv' in url :
  OOO0ooO0Oo0 = '.wmv'
  iiio00oOOooOOo0o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O0ooOOO = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , iiio00oOOooOOo0o )
  if O0O0ooOOO == 0 :
   O0oOOoooOO0O ( url )
  if O0O0ooOOO == 1 :
   O0oo ( url , name , OOO0ooO0Oo0 )
 else :
  O0oOOoooOO0O ( url )
def O0oo ( url , name , cat ) :
 o000OoO0 ( )
 ooOoO00 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 Ii1IIiI1io0O00Oo0 = os . path . join ( ooOoO00 , file )
 try :
  os . remove ( Ii1IIiI1io0O00Oo0 )
 except :
  pass
 downloader . download ( url , Ii1IIiI1io0O00Oo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def o000OoO0 ( ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def IIIIi1IiI1I ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % o000O0O )
 xbmc . sleep ( 1 )
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 o0oOoO00o . update ( 100 , '%s' % o000O0O )
 xbmc . sleep ( 1 )
 I1iiiiii . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 39 - 39: I11i % IiI1i11I . OOooOOo - i1IiiiI1iI
def IIIIIIII ( url ) :
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iiiiii . play ( url ) . strip ( )
 except : pass
 if 39 - 39: Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
def o0O0Oo0 ( url ) :
 I1iiiiii = xbmc . Player ( o0OO0Oo ( ) )
 import urlresolver
 iI1111i = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 I1iiiiii . play ( iI1111i )
 xbmc . sleep ( 1 )
 I1iiiiii . play ( url )
 if 36 - 36: oO0o % o0ii1I % IiI1i11I
 if 66 - 66: oOo0O0Ooo . oooOo0oo0oo - oO0o % I1ii11iIi11i * I11i - i1i1I1IIii1II
def o0OO0Oo ( ) :
 try :
  O0ooOOo0 = getSet ( "core-player" )
  if ( O0ooOOo0 == 'DVDPLAYER' ) : ii1iiiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0ooOOo0 == 'MPLAYER' ) : ii1iiiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0ooOOo0 == 'PAPLAYER' ) : ii1iiiI = xbmc . PLAYER_CORE_PAPLAYER
  else : ii1iiiI = xbmc . PLAYER_CORE_AUTO
 except : ii1iiiI = xbmc . PLAYER_CORE_AUTO
 return ii1iiiI
 return True
 if 33 - 33: oO0o
def IiI11i1IIiiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1i1III = [ ]
  II1i1III . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = True )
 return IIII
 if 100 - 100: i1i1I1IIii1II
def IiiI ( name , url , mode , iconimage , fanart , description ) :
 if 40 - 40: o0o00Oo0O - i1i1I1IIii1II . OOooOOo * o0o00Oo0O + ooOoO0O00 * i1iIi
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = True )
 return IIII
 if 81 - 81: I11i + i1iIi / IIiIiII11i - i1IiiiI1iI
def oOOo000oOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  II1i1III = [ ]
  II1i1III . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = False )
 return IIII
 if 99 - 99: III1iiIii + IiI1i11I * ooOoO0O00 . oOo0O0Ooo . ooOoO0O00
 if 50 - 50: I1ii11iIi11i * I1ii11iIi11i * ii % i1IiiiI1iI
 if 67 - 67: I11i / o0ii1I * Ii / Ii1I
 if 9 - 9: oooOo0oo0oo * i1iIi - ii / o0o00Oo0O
 if 86 - 86: oOo0O0Ooo . I11i % o0ii1I - OOooOOo . ooOoO0O00
 if 30 - 30: IIiIiII11i + iI11I1II1I1I / Iii
def O0O00OOOO ( url , heading , announce ) :
 class OOI11i1iiI1 ( ) :
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
   try : oOOOoo00 = open ( announce ) ; O0OOO0 = oOOOoo00 . read ( )
   except : O0OOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0OOO0 ) )
   return
 OOI11i1iiI1 ( )
 OOI11i1iiI1 ( )
def o0OIiII ( heading , announce ) :
 class OOI11i1iiI1 ( ) :
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
   try : oOOOoo00 = open ( announce ) ; O0OOO0 = oOOOoo00 . read ( )
   except : O0OOO0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0OOO0 ) )
   return
 OOI11i1iiI1 ( )
 OOI11i1iiI1 ( )
def oooOo0OOOoo0 ( ) :
 O0O00OOOO ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 6 - 6: ooOoO0O00 % oO0o + i1iIi . Ii1I
 if 72 - 72: oO0o
 if 67 - 67: o0ii1I * ii . i1i1I1IIii1II * Iii * i1i1I1IIii1II - I1ii11iIi11i
 if 82 - 82: III1iiIii
 if 42 - 42: Iii . oO0o * i1iIi
def oooO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 1 - 1: i1IiiiI1iI % IiI1i11I / iI11I1II1I1I * iI11I1II1I1I * i1iIi % IIiIiII11i
 if 59 - 59: III1iiIii
 if 21 - 21: ooOoO0O00 + I1ii11iIi11i + Iii
 if 10 - 10: oOo0O0Ooo - IIiIiII11i - IIiIiII11i + ii . III1iiIii / o0o00Oo0O
 if 31 - 31: III1iiIii + IiI1i11I . IiI1i11I
 if 12 - 12: iI11I1II1I1I + Ii1I / o0ii1I
 if 36 - 36: i1i1I1IIii1II + Ii1I + ii . I1ii11iIi11i % IiI1i11I * IIiIiII11i
 if 5 - 5: o0ii1I * IiI1i11I
 if 33 - 33: oOo0O0Ooo % Iii . i1IiiiI1iI / o0ii1I * IIiIiII11i * I11i
 if 49 - 49: ooOoO0O00 * Ii
 if 47 - 47: IIiIiII11i / I1ii11iIi11i
 if 38 - 38: oooOo0oo0oo . IiI1i11I / o0o00Oo0O . o0ii1I / OOooOOo
 if 52 - 52: o0o00Oo0O / Ii * oOo0O0Ooo . ooOoO0O00
 if 50 - 50: ii . IiI1i11I % I11i
 if 6 - 6: i1iIi - ooOoO0O00 . o0o00Oo0O . ooOoO0O00 . OOooOOo
 if 42 - 42: Ii * o0o00Oo0O % Ii + oooOo0oo0oo
 if 64 - 64: oOo0O0Ooo / OOooOOo
 if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
 if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
 if 91 - 91: oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % o0ii1I
 if 3 - 3: oOo0O0Ooo . Iii / Ii1I
 if 2 - 2: III1iiIii + Iii / iI11I1II1I1I . Ii . ooOoO0O00 * i1iIi
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - i1i1I1IIii1II - Ii
def Iiiiii11i1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 81 - 81: Ii + I11i / IIiIiII11i + Iii
def OOO0O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIiIiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 18 - 18: I1ii11iIi11i * IiI1i11I / IIiIiII11i
def o00Ooo0Oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O00O00OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 70 - 70: III1iiIii % III1iiIii - Iii
def i1I1iiIiII11 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 55 - 55: oooOo0oo0oo + o0ii1I . I11i + IIiIiII11i
def I111ii11I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 48 - 48: IiI1i11I
def iIII1Ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0Oo00OoO000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 39 - 39: oO0o + ii * iI11I1II1I1I . III1iiIii * Ii1I
def oOOO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 42 - 42: oOo0O0Ooo / Ii - iI11I1II1I1I * o0ii1I + oO0o . Iii
def o0ooooOO0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOooO0o000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 50 - 50: IIiIiII11i . I11i
def iIII1ii1iI111IIi1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo00IiiiiiiiI1i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 42 , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii )
 Ii1IIiI1i ( 'movies' , 'MAIN' )
 if 10 - 10: o0o00Oo0O + o0o00Oo0O % o0o00Oo0O % ooOoO0O00 + Iii . Ii1I
def iIiIi11 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o000O0O , url , i1iIiIi1I , I11iI1i1I11I11 , I111IIiii1Ii in IIi :
  I1I1II1I11 ( o000O0O , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , I111IIiii1Ii )
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
def OOOOoOoO ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( o0 ) :
     o00i1iII11iIiiI1 = 0
     o00i1iII11iIiiI1 += len ( IIIIIIiIIIi1iii1 )
     if o00i1iII11iIiiI1 > 0 :
      for oOOOoo00 in IIIIIIiIIIi1iii1 :
       os . unlink ( os . path . join ( iiiiIi11II11 , oOOOoo00 ) )
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
def ooo00Oo0 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
def OoOo0O00 ( url ) :
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
 for ii1 in IIiiI1iiI :
  if os . path . exists ( ii1 ) and not ii1 in [ oo0o0O00 , oO0o0oO0O ] :
   for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( ii1 ) :
    o00i1iII11iIiiI1 = 0
    o00i1iII11iIiiI1 += len ( IIIIIIiIIIi1iii1 )
    if o00i1iII11iIiiI1 > 0 :
     for oOOOoo00 in IIIIIIiIIIi1iii1 :
      if not oOOOoo00 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( iiiiIi11II11 , oOOOoo00 ) )
       except :
        pass
      else : ooo ( 'Ignore Log File: %s' % oOOOoo00 )
     for oO0oO0O in OOOOOOo0o0O0o :
      try :
       shutil . rmtree ( os . path . join ( iiiiIi11II11 , oO0oO0O ) )
       Ii1iiiIIIii += 1
       ooo ( "[Success] cleared %s files from %s" % ( str ( o00i1iII11iIiiI1 ) , os . path . join ( ii1 , oO0oO0O ) ) )
      except :
       ooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ii1 , oO0oO0O ) )
  else :
   for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( ii1 ) :
    for oO0oO0O in OOOOOOo0o0O0o :
     if 'cache' in oO0oO0O . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iiiiIi11II11 , oO0oO0O ) )
       Ii1iiiIIIii += 1
       ooo ( "[Success] wiped %s " % os . path . join ( ii1 , oO0oO0O ) )
      except :
       ooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ii1 , oO0oO0O ) )
       if 72 - 72: ooOoO0O00 * Iii
 ooo00Oo0 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % Ii1iiiIIIii )
 if 60 - 60: IiI1i11I
 if 56 - 56: o0ii1I * oOo0O0Ooo - I11i % Ii1I / IiI1i11I % i1i1I1IIii1II
 if 43 - 43: I1ii11iIi11i % i1i1I1IIii1II . Ii - o0o00Oo0O
 if 5 - 5: ooOoO0O00 + o0ii1I
 if 38 - 38: oOo0O0Ooo . o0o00Oo0O + oooOo0oo0oo / Ii1I . iI11I1II1I1I - ooOoO0O00
 if 3 - 3: I1ii11iIi11i + i1i1I1IIii1II
 if 65 - 65: oOo0O0Ooo / OOooOOo % oOo0O0Ooo * Ii * ii / Iii
def iI1i1iI1iI ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oooo0I1IiIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( oooo0I1IiIi ) :
   o00i1iII11iIiiI1 = 0
   o00i1iII11iIiiI1 += len ( IIIIIIiIIIi1iii1 )
   if 29 - 29: I1ii11iIi11i * Ii1I * ii + OOooOOo . o0ii1I / ooOoO0O00
   if 15 - 15: IIiIiII11i % ooOoO0O00 / i1i1I1IIii1II . iI11I1II1I1I * I1ii11iIi11i
   if o00i1iII11iIiiI1 > 0 :
    if 5 - 5: IiI1i11I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o00i1iII11iIiiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
     for oOOOoo00 in IIIIIIiIIIi1iii1 :
      os . unlink ( os . path . join ( iiiiIi11II11 , oOOOoo00 ) )
     for oO0oO0O in OOOOOOo0o0O0o :
      shutil . rmtree ( os . path . join ( iiiiIi11II11 , oO0oO0O ) )
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
 if 30 - 30: iI11I1II1I1I
 if 14 - 14: I11i + o0ii1I
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
 if 100 - 100: ooOoO0O00
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
def i111iIi1i1II1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oooo0I1IiIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( oooo0I1IiIi ) :
   o00i1iII11iIiiI1 = 0
   o00i1iII11iIiiI1 += len ( IIIIIIiIIIi1iii1 )
   if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
   if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
   if o00i1iII11iIiiI1 > 0 :
    if 12 - 12: ii % i1i1I1IIii1II
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( o00i1iII11iIiiI1 ) + " files found" , "Do you want to delete them?" ) :
     if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
     for oOOOoo00 in IIIIIIiIIIi1iii1 :
      os . unlink ( os . path . join ( iiiiIi11II11 , oOOOoo00 ) )
     for oO0oO0O in OOOOOOo0o0O0o :
      shutil . rmtree ( os . path . join ( iiiiIi11II11 , oO0oO0O ) )
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
 OoOo0O00 ( url )
 return
 if 79 - 79: o0o00Oo0O
 if 71 - 71: oO0o - o0o00Oo0O
 if 73 - 73: iI11I1II1I1I
 if 7 - 7: OOooOOo
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
 if 3 - 3: Iii
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
def oo0 ( url , name ) :
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 oO0oOoOo0O0 = os . path . join ( ooOoO00 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oO0oOoOo0O0 ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'advancedsettings.xml' )
   try :
    os . remove ( OOoI1I1I1iI11I1 )
    print '=== GenieTv - REMOVING    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   OooOO = open ( OOoI1I1I1iI11I1 , "w" )
   OooOO . write ( iiI111I1iIiI )
   OooOO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'advancedsettings.xml' )
  try :
   os . remove ( OOoI1I1I1iI11I1 )
   print '=== GenieTv - REMOVING    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OooOO = open ( OOoI1I1I1iI11I1 , "w" )
  OooOO . write ( iiI111I1iIiI )
  OooOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 84 - 84: oO0o
def iiIiII ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'advancedsettings.xml' )
 try :
  OooOO = open ( OOoI1I1I1iI11I1 ) . read ( )
  if 'zero' in OooOO :
   name = '0CACHE'
  elif 'tuxen' in OooOO :
   name = 'TUXENS'
  elif 'muckys' in OooOO :
   name = 'MUCKYS'
  elif 'p2p1' in OooOO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OooOO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OooOO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 11 - 11: oO0o . oO0o . OOooOOo + ooOoO0O00 - oOo0O0Ooo
def ii11iIi1I1i ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'advancedsettings.xml' )
 try :
  os . remove ( OOoI1I1I1iI11I1 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 79 - 79: Ii1I + III1iiIii
 if 94 - 94: Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
 if 7 - 7: o0ii1I
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
 if 55 - 55: oO0o % OOooOOo
 if 58 - 58: o0ii1I
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
def I1IIiIi ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for o00OoO0o0 , O0oo0oO0oOoo , Ooi1I11i1 , II1iiiii in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o00OoO0o0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Ooi1I11i1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1iiiii )
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
  ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OooOO = open ( OOoI1I1I1iI11I1 , "w" )
  OooOO . write ( iiI111I1iIiI )
  OooOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 44 - 44: I1ii11iIi11i
def iI1I ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  ooOoO00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoI1I1I1iI11I1 = os . path . join ( ooOoO00 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OooOO = open ( OOoI1I1I1iI11I1 , "w" )
  OooOO . write ( iiI111I1iIiI )
  OooOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoI1I1I1iI11I1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 29 - 29: o0o00Oo0O - Iii * oOo0O0Ooo
 if 5 - 5: IIiIiII11i - I11i + ooOoO0O00 - o0ii1I % Ii
def o0ooOooO0oo ( ) :
 try :
  ooo0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ooo0O ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    III11I1i = os . path . join ( ooo0O , "source.db" )
    os . unlink ( III11I1i )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 29 - 29: oooOo0oo0oo
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
 if 91 - 91: Ii . Ii1I + Iii
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
def IIi1IIIi ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; Ooo0o0OoOO = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if Ooo0o0OoOO :
  IIi11oo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; IIi11oo0 = xbmc . translatePath ( IIi11oo0 ) ;
  OoOoo00oO = os . path . join ( IIi11oo0 , ".." , ".." ) ; OoOoo00oO = os . path . abspath ( OoOoo00oO ) ; pluginlog ( "freshstart.main_list xbmcPath=" + OoOoo00oO ) ; oo0OO0oo000O00oo = False
  try :
   for iiiiIi11II11 , OOOOOOo0o0O0o , IIIIIIiIIIi1iii1 in os . walk ( OoOoo00oO , topdown = True ) :
    OOOOOOo0o0O0o [ : ] = [ oO0oO0O for oO0oO0O in OOOOOOo0o0O0o if oO0oO0O not in o0oO0 ]
    for o000O0O in IIIIIIiIIIi1iii1 :
     try : os . remove ( os . path . join ( iiiiIi11II11 , o000O0O ) )
     except :
      if o000O0O not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oo0OO0oo000O00oo = True
      pluginlog ( "Error removing " + iiiiIi11II11 + " " + o000O0O )
    for o000O0O in OOOOOOo0o0O0o :
     try : os . rmdir ( os . path . join ( iiiiIi11II11 , o000O0O ) )
     except :
      if o000O0O not in [ "Database" , "userdata" ] : oo0OO0oo000O00oo = True
      pluginlog ( "Error removing " + iiiiIi11II11 + " " + o000O0O )
   if not oo0OO0oo000O00oo : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 iIIi1 ( )
 if 91 - 91: Ii
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
def Oo0OOOO ( ) :
 oOOIiI1iIiI1i1 = [ ]
 oOo0o0 = sys . argv [ 2 ]
 if len ( oOo0o0 ) >= 2 :
  O00Ooo = sys . argv [ 2 ]
  IIiiI11iI = O00Ooo . replace ( '?' , '' )
  if ( O00Ooo [ len ( O00Ooo ) - 1 ] == '/' ) :
   O00Ooo = O00Ooo [ 0 : len ( O00Ooo ) - 2 ]
  IIi1III1II = IIiiI11iI . split ( '&' )
  oOOIiI1iIiI1i1 = { }
  for IIiii1I1I in range ( len ( IIi1III1II ) ) :
   o0o0OOOO = { }
   o0o0OOOO = IIi1III1II [ IIiii1I1I ] . split ( '=' )
   if ( len ( o0o0OOOO ) ) == 2 :
    oOOIiI1iIiI1i1 [ o0o0OOOO [ 0 ] ] = o0o0OOOO [ 1 ]
    if 9 - 9: o0ii1I * i1IiiiI1iI . ii / oO0o
 return oOOIiI1iIiI1i1
 if 44 - 44: Ii % ii % o0o00Oo0O - I1ii11iIi11i
oO000ooO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
III1IIiIi1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oO0oO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OoOiIIiI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oO00o0oOoo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IIi111i1i1III = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oooOo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
O00oOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IIiIiI1I = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O00O00OO0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Oo0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
IiIii1II = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o0Oo00OoO000O = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OoOOO0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOooO0o000 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
Oo00IiiiiiiiI1i11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iI1IIIIII = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii1Ii1ii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iIIiI1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oO0O000oOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
Oo00oo00o00Oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OOOO00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IIiII = base64 . decodestring ( 'Q1VOVA==' )
def iii1O0Ooo0O ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 iI1iiiIiii . setProperty ( 'fanart_image' , fanart )
 iI1iiiIiii . setProperty ( "IsPlayable" , "true" )
 oO0OOoooooo0o = [ ]
 oO0OOoooooo0o . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 oO0OOoooooo0o . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 iI1iiiIiii . addContextMenuItems ( oO0OOoooooo0o , replaceItems = True )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = False )
 return IIII
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1i1III = [ ]
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = True )
 return IIII
 if 64 - 64: I11i
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooOoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIII = True
 iI1iiiIiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iI1iiiIiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iI1iiiIiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  II1i1III = [ ]
  if showcontext == 'fav' :
   II1i1III . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   II1i1III . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iI1iiiIiii . addContextMenuItems ( II1i1III )
 IIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOoO , listitem = iI1iiiIiii , isFolder = False )
 return IIII
 if 84 - 84: IIiIiII11i
 if 58 - 58: i1i1I1IIii1II + i1iIi + III1iiIii . ooOoO0O00 + Ii1I . I1ii11iIi11i
O00Ooo = Oo0OOOO ( )
OOOiiiiI = None
o000O0O = None
i1Ii11II = None
i1iIiIi1I = None
I11iI1i1I11I11 = None
I111IIiii1Ii = None
oOooooO0o0OOO = None
O0o0000o00OO0 = None
if 50 - 50: I1ii11iIi11i
if 91 - 91: oOo0O0Ooo + ooOoO0O00 * o0o00Oo0O / oO0o + I11i
try :
 O0o0000o00OO0 = int ( O00Ooo [ "fav_mode" ] )
except :
 pass
 if 54 - 54: III1iiIii + Iii / ii / Iii / ooOoO0O00
try :
 OOOiiiiI = urllib . unquote_plus ( O00Ooo [ "url" ] )
except :
 pass
try :
 o000O0O = urllib . unquote_plus ( O00Ooo [ "name" ] )
except :
 pass
try :
 i1iIiIi1I = urllib . unquote_plus ( O00Ooo [ "iconimage" ] )
except :
 pass
try :
 i1Ii11II = int ( O00Ooo [ "mode" ] )
except :
 pass
try :
 I11iI1i1I11I11 = urllib . unquote_plus ( O00Ooo [ "fanart" ] )
except :
 pass
try :
 I111IIiii1Ii = urllib . unquote_plus ( O00Ooo [ "description" ] )
except :
 pass
 if 94 - 94: oO0o - oO0o . OOooOOo
 if 44 - 44: oOo0O0Ooo / III1iiIii . IiI1i11I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( i1Ii11II )
print "URL: " + str ( OOOiiiiI )
print "Name: " + str ( o000O0O )
print "IconImage: " + str ( i1iIiIi1I )
if 48 - 48: I11i . ooOoO0O00 - oooOo0oo0oo % o0ii1I
if 62 - 62: IIiIiII11i % ooOoO0O00
def Ii1IIiI1i ( content , viewType ) :
 if 98 - 98: oOo0O0Ooo - I1ii11iIi11i - o0ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 80 - 80: i1iIi . Ii
if i1iIiIi1I == None : i1iIiIi1I = O0O
if I11iI1i1I11I11 == None : I11iI1i1I11I11 = Oo00OOOOO
if i1Ii11II == None :
 Iii1I1I11iiI1 ( )
 if 18 - 18: Iii + Ii
elif i1Ii11II == 1 :
 o00o0o0oOo0 ( OOOiiiiI )
 if 46 - 46: o0ii1I * o0ii1I
elif i1Ii11II == 44 :
 OOOO0OOO ( OOOiiiiI )
 if 57 - 57: i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo * i1IiiiI1iI - oooOo0oo0oo
elif i1Ii11II == 2 :
 OOo0O ( )
 if 97 - 97: Ii1I
elif i1Ii11II == 3 :
 iIiiII1Ii1ii ( )
 if 3 - 3: i1iIi + Ii . iI11I1II1I1I
elif i1Ii11II == 21 :
 i1i1II ( )
 if 70 - 70: i1iIi
elif i1Ii11II == 4 :
 O0Oo0 ( )
 if 3 - 3: oOo0O0Ooo - oOo0O0Ooo
elif i1Ii11II == 5 :
 OOoO00OoOOO ( OOOiiiiI )
 if 89 - 89: OOooOOo
elif i1Ii11II == 6 :
 iI1i1iI1iI ( OOOiiiiI )
 if 27 - 27: ooOoO0O00 % OOooOOo / o0ii1I * o0ii1I / Iii
elif i1Ii11II == 7 :
 oo0 ( OOOiiiiI , o000O0O )
 if 11 - 11: oooOo0oo0oo
elif i1Ii11II == 8 :
 iiIiII ( OOOiiiiI , o000O0O )
 if 58 - 58: oO0o * ii
elif i1Ii11II == 9 :
 FIXREPOSADDONS ( OOOiiiiI )
 if 47 - 47: IiI1i11I - I1ii11iIi11i
elif i1Ii11II == 10 :
 oooO ( )
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + Iii / IIiIiII11i + i1iIi
elif i1Ii11II == 11 :
 ii11iIi1I1i ( OOOiiiiI )
 if 26 - 26: o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
elif i1Ii11II == 12 :
 I1IIiIi ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 35 - 35: ooOoO0O00 % Ii + o0ii1I
elif i1Ii11II == 13 :
 OOOOoOoO ( )
 if 14 - 14: oO0o * ii
elif i1Ii11II == 14 :
 OoOo0O00 ( OOOiiiiI )
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
elif i1Ii11II == 15 :
 I1111111 ( )
 if 97 - 97: Iii % IIiIiII11i % o0ii1I . IIiIiII11i . iI11I1II1I1I
elif i1Ii11II == 16 :
 I1i1iiIIII ( OOOiiiiI , o000O0O )
 if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IiI1i11I
elif i1Ii11II == 17 :
 iI1I ( OOOiiiiI , o000O0O )
 if 25 - 25: i1i1I1IIii1II / o0o00Oo0O + i1IiiiI1iI % Ii / oOo0O0Ooo
elif i1Ii11II == 18 :
 o0ooOooO0oo ( )
 if 62 - 62: IiI1i11I . Iii * ooOoO0O00 + IiI1i11I
elif i1Ii11II == 19 :
 o0Oo ( OOOiiiiI )
 if 95 - 95: o0ii1I / I11i % i1iIi - oOo0O0Ooo / oooOo0oo0oo * oooOo0oo0oo
elif i1Ii11II == 40 :
 III11iI1i11i ( o000O0O , OOOiiiiI , I111IIiii1Ii )
 if 6 - 6: oO0o % III1iiIii + iI11I1II1I1I
elif i1Ii11II == 42 :
 iI1i ( o000O0O , OOOiiiiI , I111IIiii1Ii )
 if 18 - 18: IIiIiII11i . o0ii1I + OOooOOo + o0o00Oo0O - Iii
elif i1Ii11II == 43 :
 oooOOOoO0O ( OOOiiiiI )
 if 30 - 30: IIiIiII11i
elif i1Ii11II == 20 :
 I1I1 ( OOOiiiiI )
 if 26 - 26: Iii - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * oooOo0oo0oo . ii
elif i1Ii11II == 22 :
 Iiiiii11i1i ( OOOiiiiI )
 if 99 - 99: i1i1I1IIii1II . oO0o / oooOo0oo0oo
elif i1Ii11II == 23 :
 OOO0O0 ( OOOiiiiI )
 if 12 - 12: iI11I1II1I1I + i1iIi * i1IiiiI1iI % ii / iI11I1II1I1I
elif i1Ii11II == 24 :
 o00Ooo0Oo ( OOOiiiiI )
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - Ii1I
elif i1Ii11II == 25 :
 i1I1iiIiII11 ( OOOiiiiI )
 if 8 - 8: OOooOOo / o0ii1I
elif i1Ii11II == 26 :
 I111ii11I ( OOOiiiiI )
 if 12 - 12: iI11I1II1I1I
elif i1Ii11II == 27 :
 iIII1Ii1 ( OOOiiiiI )
 if 52 - 52: i1i1I1IIii1II . Ii1I + i1i1I1IIii1II
elif i1Ii11II == 28 :
 oOOO0o ( OOOiiiiI )
 if 73 - 73: IIiIiII11i / Ii / i1iIi
elif i1Ii11II == 29 :
 o0ooooOO0 ( OOOiiiiI )
 if 1 - 1: IiI1i11I + OOooOOo / III1iiIii - oOo0O0Ooo % oOo0O0Ooo
elif i1Ii11II == 30 :
 III1I1 ( OOOiiiiI )
 if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
elif i1Ii11II == 31 :
 iIII1ii1iI111IIi1 ( OOOiiiiI )
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
elif i1Ii11II == 32 :
 OoiiI11111II ( )
 if 30 - 30: Iii
elif i1Ii11II == 33 :
 I1ii1i11iI1 ( )
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
elif i1Ii11II == 35 :
 o0O0O0O00o ( OOOiiiiI )
 if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
elif i1Ii11II == 34 :
 IiOOo0 ( OOOiiiiI )
 if 15 - 15: I11i
elif i1Ii11II == 36 :
 ooOoo0OOOO0o ( OOOiiiiI )
 if 55 - 55: Ii / ii - Iii
elif i1Ii11II == 37 :
 O00OoO0 ( OOOiiiiI )
 if 89 - 89: Iii - ooOoO0O00 - ooOoO0O00 * oooOo0oo0oo - o0o00Oo0O
elif i1Ii11II == 38 :
 iiii ( OOOiiiiI )
 if 94 - 94: I1ii11iIi11i / Iii . Ii1I
elif i1Ii11II == 41 :
 IIi1IIIi ( O00Ooo )
 if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
elif i1Ii11II == 39 :
 iIiIi11 ( OOOiiiiI )
 if 72 - 72: i1IiiiI1iI * oO0o + I1ii11iIi11i / o0ii1I % oooOo0oo0oo
elif i1Ii11II == 45 :
 TEXTS ( )
 if 84 - 84: OOooOOo / I11i
elif i1Ii11II == 46 :
 oooOo0OOOoo0 ( )
 if 9 - 9: o0ii1I
elif i1Ii11II == 47 :
 GEVID ( )
 if 76 - 76: oOo0O0Ooo % I1ii11iIi11i / iI11I1II1I1I - I1ii11iIi11i
elif i1Ii11II == 48 :
 iiIiiiIii11i1 ( o000O0O , OOOiiiiI , I111IIiii1Ii )
 if 34 - 34: OOooOOo - ooOoO0O00 + oooOo0oo0oo + o0ii1I . I11i
elif i1Ii11II == 49 :
 oO00O0 ( )
 if 42 - 42: oO0o
elif i1Ii11II == 22222 :
 IiIIoOo ( OOOiiiiI )
 if 59 - 59: oO0o . i1IiiiI1iI % oO0o
elif i1Ii11II == 222225 :
 oOO0o000Oo00o ( OOOiiiiI )
 if 22 - 22: I1ii11iIi11i
elif i1Ii11II == 222 :
 o00OO0O00O0 ( OOOiiiiI )
 if 21 - 21: I11i
elif i1Ii11II == 2222222 :
 O0oOOoooOO0O ( OOOiiiiI )
 if 86 - 86: i1iIi / iI11I1II1I1I . oooOo0oo0oo
elif i1Ii11II == 222222 :
 IiiI11I ( OOOiiiiI , o000O0O )
 if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
elif i1Ii11II == 333 :
 iII11i1 ( OOOiiiiI )
 if 30 - 30: OOooOOo . oooOo0oo0oo % oooOo0oo0oo / IIiIiII11i + ooOoO0O00
 if 61 - 61: ooOoO0O00 % IIiIiII11i * IIiIiII11i . I11i / Ii1I - i1IiiiI1iI
elif i1Ii11II == 1020 :
 oOOo0ooOOoO0 ( )
 if 93 - 93: o0ii1I - ooOoO0O00
elif i1Ii11II == 1021 :
 ANIMEEP ( )
 if 3 - 3: i1i1I1IIii1II + oO0o - IiI1i11I / o0ii1I
elif i1Ii11II == 1022 :
 ANIMEPLAY ( OOOiiiiI )
 if 58 - 58: o0ii1I * Iii
elif i1Ii11II == 1001 :
 iiiiii ( )
 if 95 - 95: i1i1I1IIii1II
elif i1Ii11II == 1005 :
 IiiIi1II ( )
 if 49 - 49: oOo0O0Ooo
elif i1Ii11II == 1007 :
 IiII1IiiI ( OOOiiiiI )
 if 23 - 23: i1IiiiI1iI
elif i1Ii11II == 1010 :
 O00oIii1iIIiii1ii ( OOOiiiiI )
 if 5 - 5: Ii1I % OOooOOo . ii . I11i + Ii
elif i1Ii11II == 1011 :
 I1IIi1I11iI ( OOOiiiiI )
 if 54 - 54: i1iIi - o0o00Oo0O + IiI1i11I
elif i1Ii11II == 1012 :
 iIII1 ( OOOiiiiI )
 if 34 - 34: o0ii1I - oooOo0oo0oo % IiI1i11I
elif i1Ii11II == 1030 :
 O0II ( )
 if 48 - 48: i1i1I1IIii1II - o0o00Oo0O
elif i1Ii11II == 1031 :
 IIiII1ii1i11I ( OOOiiiiI , i1iIiIi1I )
 if 17 - 17: iI11I1II1I1I . III1iiIii / i1iIi % Iii + I11i - iI11I1II1I1I
elif i1Ii11II == 1032 :
 Ii111IIIIii ( OOOiiiiI )
 if 95 - 95: OOooOOo + oooOo0oo0oo - Iii * ooOoO0O00 + ooOoO0O00 * o0o00Oo0O
elif i1Ii11II == 1006 :
 Parse . ParseURL ( OOOiiiiI )
 if 60 - 60: I1ii11iIi11i + Iii % iI11I1II1I1I % i1i1I1IIii1II - i1IiiiI1iI / I11i
elif i1Ii11II == 2030 :
 Parse . addonParseURL ( OOOiiiiI )
 if 9 - 9: III1iiIii / i1i1I1IIii1II % o0o00Oo0O * i1IiiiI1iI - iI11I1II1I1I % ooOoO0O00
elif i1Ii11II == 2031 :
 Parse . apkParseURL ( OOOiiiiI )
 if 83 - 83: OOooOOo + oooOo0oo0oo / ii
elif i1Ii11II == 2032 :
 Parse . ParseBOSS ( OOOiiiiI )
 if 39 - 39: oO0o % IiI1i11I . i1i1I1IIii1II . IIiIiII11i - Ii
elif i1Ii11II == 1002 :
 i1Io0ooo ( OOOiiiiI )
 if 85 - 85: o0o00Oo0O - OOooOOo
elif i1Ii11II == 1003 :
 iIIIII1iiI ( OOOiiiiI , i1iIiIi1I )
 if 17 - 17: I11i / ooOoO0O00 / oooOo0oo0oo
elif i1Ii11II == 1004 :
 iIiiI11iI111 ( OOOiiiiI )
 if 91 - 91: Ii1I / o0ii1I - OOooOOo . Iii / i1i1I1IIii1II
elif i1Ii11II == 1008 :
 I1iiiiiiiIi1 ( )
 if 16 - 16: III1iiIii % IiI1i11I . i1i1I1IIii1II . oOo0O0Ooo % o0o00Oo0O * Iii
elif i1Ii11II == 1009 :
 O0oo0O0OO0OOo ( OOOiiiiI )
 if 99 - 99: OOooOOo / ii + IiI1i11I * Iii * Ii + oooOo0oo0oo
elif i1Ii11II == 2001 :
 ooOo000 ( )
 if 40 - 40: IIiIiII11i / Iii % oOo0O0Ooo - o0o00Oo0O
elif i1Ii11II == 2002 :
 iII1Ii1ii111 ( OOOiiiiI )
 if 39 - 39: Ii - OOooOOo % oooOo0oo0oo + i1iIi + Ii
elif i1Ii11II == 1013 :
 oooOOO0o0O0 ( )
elif i1Ii11II == 10111113 :
 I1I1IIiiI1 ( OOOiiiiI )
 if 59 - 59: III1iiIii / OOooOOo - i1IiiiI1iI - i1iIi . i1i1I1IIii1II
elif i1Ii11II == 1014 :
 Ii1IiIiI1Ii ( )
 if 87 - 87: i1i1I1IIii1II + oOo0O0Ooo * i1IiiiI1iI * I11i + o0o00Oo0O
elif i1Ii11II == 1015 :
 o0oO0oo000oo ( OOOiiiiI )
 if 21 - 21: i1IiiiI1iI + OOooOOo + OOooOOo . IIiIiII11i / i1IiiiI1iI . oOo0O0Ooo
elif i1Ii11II == 1016 :
 iIIii ( OOOiiiiI , i1iIiIi1I , o000O0O )
 if 66 - 66: i1IiiiI1iI % i1i1I1IIii1II . IiI1i11I * ooOoO0O00
elif i1Ii11II == 1017 :
 O0O0oOOo0O ( )
 if 81 - 81: ii * oOo0O0Ooo / i1IiiiI1iI
elif i1Ii11II == 1018 :
 iiii11i ( OOOiiiiI )
 if 10 - 10: oOo0O0Ooo - IIiIiII11i / III1iiIii * IIiIiII11i
elif i1Ii11II == 1019 :
 OoOo00o0OO ( OOOiiiiI )
elif i1Ii11II == 10190 :
 iI1IIIii ( OOOiiiiI )
 if 67 - 67: IIiIiII11i . o0ii1I % i1i1I1IIii1II . I1ii11iIi11i + III1iiIii
elif i1Ii11II == 1023 :
 Oo0OOOOOOO0oo ( )
 if 10 - 10: oooOo0oo0oo - oO0o * i1i1I1IIii1II / iI11I1II1I1I - OOooOOo
elif i1Ii11II == 1024 :
 oOOiI ( OOOiiiiI )
 if 20 - 20: III1iiIii % oOo0O0Ooo + iI11I1II1I1I % IiI1i11I
elif i1Ii11II == 1025 :
 O0O0 ( OOOiiiiI )
 if 100 - 100: I11i - I1ii11iIi11i % i1IiiiI1iI . Ii % ii
elif i1Ii11II == 4001 :
 O0O0Oo00 ( )
 if 39 - 39: Ii1I / Ii * ooOoO0O00 * I1ii11iIi11i
elif i1Ii11II == 4002 :
 oooOoOOO0oo0o ( )
 if 39 - 39: oO0o * ii / ooOoO0O00 + I1ii11iIi11i
elif i1Ii11II == 4003 :
 OOooooO ( )
 if 57 - 57: o0o00Oo0O
elif i1Ii11II == 4004 :
 O0OoO0ooOO0o ( )
 if 83 - 83: oooOo0oo0oo / o0ii1I * oOo0O0Ooo % i1i1I1IIii1II / iI11I1II1I1I
elif i1Ii11II == 4005 :
 oOOoo ( )
 if 1 - 1: Iii / ii / IiI1i11I
elif i1Ii11II == 4006 :
 Ii1i1i1i1I1Ii ( )
 if 68 - 68: ooOoO0O00 / I1ii11iIi11i / Iii * I1ii11iIi11i
elif i1Ii11II == 4007 :
 O0ooooo0OOOO0 ( )
 if 91 - 91: oO0o . IiI1i11I
elif i1Ii11II == 4008 :
 O0Oo ( )
 if 82 - 82: Ii1I / I1ii11iIi11i
elif i1Ii11II == 40099 : OoO00OooO0 ( )
elif i1Ii11II == 4009 : OOoO ( )
elif i1Ii11II == 4010 : oO0OOoo ( )
elif i1Ii11II == 3000 :
 i1i1iiI11I ( )
 if 63 - 63: oOo0O0Ooo
elif i1Ii11II == 3001 :
 IiiIIiiII ( )
 if 3 - 3: IiI1i11I + Ii1I
elif i1Ii11II == 3002 :
 OOOOo0oo0o ( OOOiiiiI )
 if 35 - 35: i1i1I1IIii1II * IiI1i11I * i1i1I1IIii1II * i1IiiiI1iI * III1iiIii * ooOoO0O00
elif i1Ii11II == 3003 :
 iI1I1iii11i ( OOOiiiiI )
 if 43 - 43: oO0o * oOo0O0Ooo / III1iiIii . Ii + IiI1i11I + I11i
elif i1Ii11II == 3004 :
 IIIi11 ( OOOiiiiI )
 if 1 - 1: oOo0O0Ooo % I11i . i1IiiiI1iI + Iii * i1i1I1IIii1II
elif i1Ii11II == 404 :
 ooO0oo00o00 ( o000O0O , OOOiiiiI , i1iIiIi1I )
 if 41 - 41: oO0o * i1i1I1IIii1II - IIiIiII11i
elif i1Ii11II == 405 :
 IIIIi1IiI1I ( OOOiiiiI )
 if 2 - 2: III1iiIii + III1iiIii - oO0o * IiI1i11I . i1i1I1IIii1II
elif i1Ii11II == 7030 :
 oOoOOoooO00oO ( )
 if 91 - 91: i1iIi
elif i1Ii11II == 7021 :
 i1Iiiii111i ( o000O0O )
 if 22 - 22: i1iIi % oO0o * OOooOOo + I1ii11iIi11i
elif i1Ii11II == 7022 :
 IIiI111iI1iiii ( o000O0O )
 if 44 - 44: o0o00Oo0O - Iii
elif i1Ii11II == 7000 :
 i1IiiiI1Ii ( o000O0O , OOOiiiiI , img )
 if 43 - 43: o0o00Oo0O
elif i1Ii11II == 7050 :
 iiiI1IiI ( OOOiiiiI )
 if 50 - 50: Iii - ii
elif i1Ii11II == 7051 :
 IIiOO0O000 ( OOOiiiiI )
 if 29 - 29: i1i1I1IIii1II * i1i1I1IIii1II
elif i1Ii11II == 7052 :
 oOo0ooOO0O ( OOOiiiiI )
 if 44 - 44: i1iIi . oOo0O0Ooo * i1i1I1IIii1II * o0ii1I
elif i1Ii11II == 7053 :
 IIIII11IIi ( OOOiiiiI )
 if 41 - 41: ooOoO0O00 % Ii + Iii % ii / Ii1I
elif i1Ii11II == 7054 :
 CoolPlay ( OOOiiiiI )
 if 8 - 8: ii - oO0o / Ii / o0o00Oo0O . III1iiIii
elif i1Ii11II == 7060 :
 O00oO0OOOo0 ( )
 if 86 - 86: i1iIi * ii + IiI1i11I + I11i
elif i1Ii11II == 7061 :
 o00oOoOo0 ( OOOiiiiI )
 if 79 - 79: ooOoO0O00 % Ii1I - oO0o % Ii1I
elif i1Ii11II == 7063 :
 o00ooo0O ( OOOiiiiI )
 if 6 - 6: I1ii11iIi11i / IiI1i11I . Ii
elif i1Ii11II == 7062 :
 IIIiiI1I ( OOOiiiiI )
 if 8 - 8: Ii1I + o0o00Oo0O - i1i1I1IIii1II % IIiIiII11i . i1IiiiI1iI
elif i1Ii11II == 7064 :
 NATatozcat ( )
 if 86 - 86: III1iiIii
elif i1Ii11II == 7067 :
 O0OO0OoO00oOo ( OOOiiiiI )
 if 71 - 71: o0ii1I - ooOoO0O00 . oOo0O0Ooo
elif i1Ii11II == 7066 :
 NATatozA ( OOOiiiiI )
 if 15 - 15: ooOoO0O00 % IIiIiII11i / IIiIiII11i - Ii1I - Iii % ooOoO0O00
elif i1Ii11II == 7065 :
 IiIoOo ( OOOiiiiI )
 if 54 - 54: ooOoO0O00 . oO0o + IiI1i11I + oO0o * ooOoO0O00
elif i1Ii11II == 7070 :
 OooOO0O0000o ( )
 if 13 - 13: I1ii11iIi11i / oO0o + oooOo0oo0oo
elif i1Ii11II == 7071 :
 DIZIlist ( OOOiiiiI )
 if 90 - 90: oO0o * Ii / i1i1I1IIii1II
elif i1Ii11II == 7072 :
 DIZIpull ( OOOiiiiI )
 if 91 - 91: IiI1i11I - OOooOOo / I1ii11iIi11i % IIiIiII11i / IIiIiII11i / I11i
elif i1Ii11II == 7073 :
 WATCHDIZI ( OOOiiiiI )
 if 34 - 34: oO0o * IIiIiII11i + Ii % o0ii1I
elif i1Ii11II == 7002 :
 oO0IiiI1i1i11I1 ( )
 if 25 - 25: OOooOOo + III1iiIii . Ii
elif i1Ii11II == 7003 :
 iiii1iIiI11I ( OOOiiiiI )
 if 87 - 87: oOo0O0Ooo + ii + o0o00Oo0O
elif i1Ii11II == 7004 :
 oOO0O0 ( OOOiiiiI )
 if 32 - 32: o0ii1I / Ii1I . o0ii1I
elif i1Ii11II == 7020 :
 IiIIIIII ( OOOiiiiI )
 if 65 - 65: III1iiIii
elif i1Ii11II == 7001 :
 Ooo0o00o0o ( )
 if 74 - 74: I1ii11iIi11i + ooOoO0O00 - IIiIiII11i / i1iIi / IiI1i11I
elif i1Ii11II == 7010 :
 oooOo0O ( OOOiiiiI )
 if 66 - 66: i1iIi / III1iiIii * iI11I1II1I1I
elif i1Ii11II == 7011 :
 i1IIiIiI11 ( OOOiiiiI )
 if 42 - 42: i1IiiiI1iI - Ii % IIiIiII11i * i1iIi . o0o00Oo0O % Iii
elif i1Ii11II == 7012 :
 o00o0Ooo ( OOOiiiiI )
 if 82 - 82: I1ii11iIi11i % o0o00Oo0O + Ii1I % Ii1I
elif i1Ii11II == 7013 :
 cnfTVPlay2 ( OOOiiiiI )
elif i1Ii11II == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OOOiiiiI )
elif i1Ii11II == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OOOiiiiI )
elif i1Ii11II == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( o000O0O , OOOiiiiI , i1iIiIi1I )
elif i1Ii11II == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i1Ii11II == 7018 :
 iI11 ( )
elif i1Ii11II == 7019 :
 CNF_Studio_Indexer . List_Movies ( OOOiiiiI )
elif i1Ii11II == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OOOiiiiI )
elif i1Ii11II == 7024 :
 CNF_Studio_Indexer . Box_Office ( OOOiiiiI )
 if 74 - 74: o0o00Oo0O * III1iiIii . Iii - i1IiiiI1iI + o0o00Oo0O + Iii
elif i1Ii11II == 8000 :
 IiII11IIII1 ( )
elif i1Ii11II == 8001 :
 iIiIIiII11i1 ( )
elif i1Ii11II == 8002 :
 Oo0ooIi1ii11i1II11 ( )
elif i1Ii11II == 8003 :
 I1iI1i ( )
elif i1Ii11II == 8004 :
 IIIiIi1iI ( )
elif i1Ii11II == 8005 :
 ii11I1IiIIi1i1IIi ( )
elif i1Ii11II == 8006 :
 I1I1IiIiIIi1I ( o000O0O , OOOiiiiI )
elif i1Ii11II == 8030 :
 OOoO0Oo ( OOOiiiiI )
elif i1Ii11II == 8045 :
 OOoo00OoO0o ( OOOiiiiI )
elif i1Ii11II == 8046 :
 II11Iii1 ( OOOiiiiI )
elif i1Ii11II == 8047 :
 ooo0o0oO ( OOOiiiiI )
elif i1Ii11II == 8048 :
 iio0O ( OOOiiiiI )
elif i1Ii11II == 8049 :
 OOoOO0 ( OOOiiiiI )
elif i1Ii11II == 804900 :
 III1iiI1 ( OOOiiiiI )
elif i1Ii11II == 8020 :
 O00oO0 ( )
elif i1Ii11II == 8021 :
 iiiOOoO00o0OO ( OOOiiiiI )
elif i1Ii11II == 8022 :
 IIiiIIIi1II ( OOOiiiiI )
elif i1Ii11II == 8023 :
 i11IIii1iI11 ( OOOiiiiI )
elif i1Ii11II == 8040 :
 ii11i11i1 ( )
elif i1Ii11II == 8041 :
 i1iI11IiII ( OOOiiiiI )
elif i1Ii11II == 8042 :
 OOooOOO ( OOOiiiiI )
elif i1Ii11II == 8043 :
 yt . PlayVideo ( OOOiiiiI )
elif i1Ii11II == 8044 :
 o00Oooo0o0 ( OOOiiiiI )
elif i1Ii11II == 8060 :
 OoO ( )
elif i1Ii11II == 8061 :
 OOOOo00oOOO00 ( OOOiiiiI )
elif i1Ii11II == 8064 :
 ii1ii111 ( )
elif i1Ii11II == 8065 :
 I1oo0OoOOO ( OOOiiiiI )
elif i1Ii11II == 8070 :
 OoOooOOO00o0OoOOOo ( )
elif i1Ii11II == 8071 :
 I1ioO000O0oO00 ( OOOiiiiI )
elif i1Ii11II == 7080 :
 i1Ii1IIii ( OOOiiiiI )
elif i1Ii11II == 8090 :
 oo00O0oOo ( )
elif i1Ii11II == 8091 :
 oo0OO0oOooo ( OOOiiiiI )
elif i1Ii11II == 8092 :
 oOOI111I1 ( OOOiiiiI )
elif i1Ii11II == 8093 :
 I111II ( OOOiiiiI )
elif i1Ii11II == 8081 :
 i1III1i ( )
elif i1Ii11II == 8062 :
 Oo0OOOOOOOo0O ( OOOiiiiI )
elif i1Ii11II == 8063 :
 I1iiI1IiI ( OOOiiiiI )
elif i1Ii11II == 8050 :
 OO0O00OO0 ( )
elif i1Ii11II == 8051 :
 IiII1 ( OOOiiiiI )
elif i1Ii11II == 8052 :
 o0oIi11I1II1 ( OOOiiiiI )
elif i1Ii11II == 8085 :
 iiiIiI111iiI1II ( )
elif i1Ii11II == 8086 :
 OO0OOO0o0OOO0 ( OOOiiiiI )
elif i1Ii11II == 8087 :
 iiI11i1II ( OOOiiiiI )
elif i1Ii11II == 8088 :
 oOoo0o0O00 ( OOOiiiiI , o000O0O )
elif i1Ii11II == 9000 :
 ii1111Iii11i ( )
elif i1Ii11II == 1111 :
 Ii1iii11I ( )
elif i1Ii11II == 9001 :
 OoOo0oOooOoOO ( )
elif i1Ii11II == 9002 :
 iII1111III1I ( )
elif i1Ii11II == 9003 :
 i1OO0o ( )
elif i1Ii11II == 9004 :
 World1 ( )
elif i1Ii11II == 9005 :
 World2 ( OOOiiiiI )
elif i1Ii11II == 9006 :
 World3 ( OOOiiiiI )
elif i1Ii11II == 9007 :
 iIIi1i111iI ( )
elif i1Ii11II == 9008 :
 i1iIi1I1II1 ( OOOiiiiI )
elif i1Ii11II == 9009 :
 i11iIi ( OOOiiiiI )
elif i1Ii11II == 9010 :
 i1IOoOo0O0 ( )
elif i1Ii11II == 9011 :
 OOoOOoo ( OOOiiiiI )
elif i1Ii11II == 50 :
 iIIi1II1 ( OOOiiiiI )
elif i1Ii11II == 9020 :
 champlist ( )
elif i1Ii11II == 9021 :
 iiii1I1ii1 ( )
elif i1Ii11II == 9022 :
 iiiIiIiiiII11i ( )
elif i1Ii11II == 9023 :
 I1oO0oO00OO00 ( )
elif i1Ii11II == 9024 :
 Oooo000 ( OOOiiiiI )
elif i1Ii11II == 9030 :
 Ii1i11IIiI ( OOOiiiiI )
elif i1Ii11II == 9031 :
 III1i1 ( OOOiiiiI )
elif i1Ii11II == 9032 :
 Oo00oooO00o ( OOOiiiiI )
elif i1Ii11II == 9033 :
 oooO0Oo0O ( OOOiiiiI )
elif i1Ii11II == 9034 :
 O0iII1 ( )
elif i1Ii11II == 7085 :
 iiIiiIii1IiI ( OOOiiiiI )
elif i1Ii11II == 7086 :
 OOO00o0oO ( OOOiiiiI )
elif i1Ii11II == 7087 :
 ooo00 ( I111IIiii1Ii )
elif i1Ii11II == 9666 :
 i111iIi1i1II1 ( OOOiiiiI )
elif i1Ii11II == 10100 : O0Oo000OO000 ( )
elif i1Ii11II == 101001 : iIiIi ( OOOiiiiI )
elif i1Ii11II == 10105 : IiI1iIIiIi1Ii ( OOOiiiiI )
elif i1Ii11II == 10106 : O0oOoOOO000 ( OOOiiiiI )
elif i1Ii11II == 10104 : iIiiIi11iiI1 ( OOOiiiiI )
elif i1Ii11II == 10107 : I1Iii11II ( )
elif i1Ii11II == 10103 : oOo00o0oO ( OOOiiiiI )
elif i1Ii11II == 10108 : II1I11iIIIii1 ( OOOiiiiI )
elif i1Ii11II == 10000 : Origin_Menu ( )
elif i1Ii11II == 10001 : iI ( )
elif i1Ii11II == 10002 : iI111i1II ( )
elif i1Ii11II == 10003 : IIi1IiIii ( )
elif i1Ii11II == 10004 : i111i11I1ii ( OOOiiiiI )
elif i1Ii11II == 10005 : OOooo00 ( )
elif i1Ii11II == 10006 : IIiI1I11ii1i ( OOOiiiiI )
elif i1Ii11II == 10007 : o00OO0o ( OOOiiiiI , i1iIiIi1I )
elif i1Ii11II == 10008 : OOOooOO0oO ( )
elif i1Ii11II == 10009 : I1iIiI ( )
elif i1Ii11II == 10010 : oOoO0oOO ( OOOiiiiI )
elif i1Ii11II == 10011 : ii1iiiiii ( OOOiiiiI )
elif i1Ii11II == 10012 : O0oOOoooOO0O ( OOOiiiiI )
elif i1Ii11II == 10113 : GRABG ( OOOiiiiI , o000O0O )
elif i1Ii11II == 10109 : o0O0Oo0 ( OOOiiiiI )
elif i1Ii11II == 10013 : Oo00OOooOoO ( OOOiiiiI )
elif i1Ii11II == 10014 : I1Iii ( )
elif i1Ii11II == 10015 : ii1O0oOOo ( )
elif i1Ii11II == 10016 : OO0OoOOO0 ( OOOiiiiI )
elif i1Ii11II == 10017 : oo0o0ooOoo00O ( )
elif i1Ii11II == 10018 : ii11Ii11III ( )
elif i1Ii11II == 10019 : IIio0 ( )
elif i1Ii11II == 10020 : o0o0O0o0O ( )
elif i1Ii11II == 10021 : oo0ooO0O ( )
elif i1Ii11II == 10022 : Iiiii ( OOOiiiiI )
elif i1Ii11II == 10023 : O0O0O00OoO0O ( o000O0O , OOOiiiiI )
elif i1Ii11II == 10024 : IIio0O0 ( OOOiiiiI )
elif i1Ii11II == 10025 : i11iiiiI1i ( )
elif i1Ii11II == 10026 : o00000Oo ( )
elif i1Ii11II == 10027 : III11II111 ( )
elif i1Ii11II == 10028 : I1iiIIii ( )
elif i1Ii11II == 10029 : O000O000 ( )
elif i1Ii11II == 423 : I1III1I1IiI ( OOOiiiiI )
elif i1Ii11II == 426 : iI1I1iII1iII ( OOOiiiiI )
elif i1Ii11II == 10030 : Izle_Films ( )
elif i1Ii11II == 10031 : Latest_Izle_Movies ( )
elif i1Ii11II == 10032 : Izle_Genres ( )
elif i1Ii11II == 10033 : Izle_Pop_Movies ( )
elif i1Ii11II == 10034 : Izle_Boxsets ( )
elif i1Ii11II == 10035 : Izle_Search ( )
elif i1Ii11II == 10036 : Izle_Genres_Movie ( OOOiiiiI )
elif i1Ii11II == 10037 : Izle_Boxset_single ( OOOiiiiI )
elif i1Ii11II == 10038 : Izle_IFRAME ( )
elif i1Ii11II == 10039 : Izle_Boxsets_Next ( OOOiiiiI )
elif i1Ii11II == 10040 : O00oOo00o0o ( )
elif i1Ii11II == 10041 : IIiIiI1i11iiII ( OOOiiiiI )
elif i1Ii11II == 10042 : oO000 ( OOOiiiiI )
elif i1Ii11II == 10043 : iIo0O000O00o ( )
elif i1Ii11II == 10044 : IIiiiIi1ii11I ( OOOiiiiI )
elif i1Ii11II == 10045 : o0O00o00Ooo ( o000O0O )
elif i1Ii11II == 10046 : Oo0OOO00oo0 ( OOOiiiiI )
elif i1Ii11II == 10047 : ii1II11IIII1 ( OOOiiiiI )
elif i1Ii11II == 10048 : ii11Ii1iii1I1 ( OOOiiiiI )
elif i1Ii11II == 10049 : i11I111iIiI ( OOOiiiiI )
elif i1Ii11II == 10050 : I11I1 ( )
elif i1Ii11II == 10051 : o0oO ( )
elif i1Ii11II == 10052 : I1II11iiii ( )
elif i1Ii11II == 10053 : Addon ( OOOiiiiI )
elif i1Ii11II == 10054 : OOooOOO000 ( OOOiiiiI , o000O0O )
elif i1Ii11II == 10055 :
 Oo0o0OOo0Oo0 ( "addFavorite" )
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 iIiIi111 ( o000O0O , OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 , O0o0000o00OO0 )
elif i1Ii11II == 10056 :
 Oo0o0OOo0Oo0 ( "rmFavorite" )
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 iIi1i1iiIiiiI ( o000O0O )
elif i1Ii11II == 10057 :
 Oo0o0OOo0Oo0 ( "getFavorites" )
 o00oO00 ( )
elif i1Ii11II == 10058 : iIi1Ii1111i ( )
elif i1Ii11II == 10059 : Donators_Guide ( )
elif i1Ii11II == 10060 : oOoO00o ( )
elif i1Ii11II == 10061 : o00O ( )
elif i1Ii11II == 10062 : I1II1I ( o000O0O , OOOiiiiI , I111IIiii1Ii )
elif i1Ii11II == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif i1Ii11II == 10064 : OoOoooo0O ( )
elif i1Ii11II == 10065 : IiiOoo0o0ooooOOo ( OOOiiiiI )
elif i1Ii11II == 10066 : OoO0o0OOOO ( OOOiiiiI )
elif i1Ii11II == 10068 : oo000ii ( OOOiiiiI )
elif i1Ii11II == 10069 : i11111I1I ( OOOiiiiI )
elif i1Ii11II == 10070 : Ii11iiI ( OOOiiiiI )
elif i1Ii11II == 10071 : Genie_Watch ( )
elif i1Ii11II == 10072 : iiIi ( )
elif i1Ii11II == 10073 : O0oo00oOOO0o ( OOOiiiiI )
elif i1Ii11II == 10074 : Ii1I1 ( OOOiiiiI )
elif i1Ii11II == 10075 : O0ooooooo00 ( i1iIiIi1I , o000O0O , OOOiiiiI )
elif i1Ii11II == 10076 : i1i1iIII11i ( OOOiiiiI )
elif i1Ii11II == 10077 : i1Iiii ( OOOiiiiI )
elif i1Ii11II == 10078 : Ooi1IIii11i1I1 ( )
elif i1Ii11II == 10079 : Genie_Watch_Tv_Shows ( )
elif i1Ii11II == 10080 : Genie_Watch_Tv_Genre ( OOOiiiiI )
elif i1Ii11II == 10081 : Genie_Watch_TV_PlayRun ( OOOiiiiI )
elif i1Ii11II == 10082 : Genie_Watch_TV_Episodes ( OOOiiiiI , i1iIiIi1I )
elif i1Ii11II == 10083 : Genie_Watch_Tv_Recent ( OOOiiiiI )
elif i1Ii11II == 10084 : IIIii ( )
elif i1Ii11II == 10085 : oo0OOo0 ( )
elif i1Ii11II == 10086 : O0 ( )
elif i1Ii11II == 20000 : Ii1IIi ( )
elif i1Ii11II == 20001 : I1Ii1iI1IiI1I ( OOOiiiiI )
elif i1Ii11II == 20002 : iiiii1II1I ( OOOiiiiI )
elif i1Ii11II == 20003 : IIiiIiIIiI1 ( OOOiiiiI )
elif i1Ii11II == 20004 : oo0O0000oo0o0 ( OOOiiiiI )
elif i1Ii11II == 20005 : IiIIIiII1111 ( OOOiiiiI )
elif i1Ii11II == 21004 : i1oO ( )
elif i1Ii11II == 21005 : oOoOo00oo ( OOOiiiiI )
elif i1Ii11II == 21006 : II11IiIIiiiii ( OOOiiiiI )
elif i1Ii11II == 21007 : OoOo00OoOO00 ( OOOiiiiI )
elif i1Ii11II == 21008 : OOOoOo ( OOOiiiiI )
elif i1Ii11II == 21009 : i1I ( OOOiiiiI )
elif i1Ii11II == 30000 : OOI11 ( )
elif i1Ii11II == 30001 : OO00o ( )
elif i1Ii11II == 100121 : Resolve ( OOOiiiiI )
elif i1Ii11II == 30003 : I11Ii1iI1II ( )
elif i1Ii11II == 30004 : I1Iii11111I1iii ( OOOiiiiI )
elif i1Ii11II == 30005 : IIIII1IIiIi ( OOOiiiiI )
elif i1Ii11II == 30006 : IIiIIiIi1II1IiI ( )
elif i1Ii11II == 30007 : IiIi1I11 ( )
elif i1Ii11II == 30008 : OO0000O ( OOOiiiiI )
elif i1Ii11II == 30009 : II1iIIi ( OOOiiiiI )
elif i1Ii11II == 30010 : Oo0OO0 ( OOOiiiiI )
elif i1Ii11II == 30011 : IiII111I ( )
elif i1Ii11II == 30012 : iI1111iiI1 ( )
elif i1Ii11II == 30013 : I1i1iI11ii ( )
elif i1Ii11II == 30014 : O00oOOoOOOOO ( )
elif i1Ii11II == 30015 : iii1i1Iiiiiii ( OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 )
elif i1Ii11II == 30016 : O0oOOo0 ( OOOiiiiI )
elif i1Ii11II == 30019 : OO00O00o0O ( OOOiiiiI )
elif i1Ii11II == 30017 : III1I ( OOOiiiiI )
elif i1Ii11II == 30018 : iiiI ( OOOiiiiI )
elif i1Ii11II == 30030 : iIIIIII ( )
elif i1Ii11II == 30031 : IIiIi ( )
elif i1Ii11II == 30032 : IiiIi1III ( )
elif i1Ii11II == 30033 : OOOO00OooO ( )
elif i1Ii11II == 30034 : IIIi1i1i1iii ( )
elif i1Ii11II == 30035 : ooOooO ( OOOiiiiI )
elif i1Ii11II == 30036 : oooo ( OOOiiiiI )
elif i1Ii11II == 30037 : IIIiI1iIIII ( OOOiiiiI )
elif i1Ii11II == 30038 : iiOo0ooo ( )
elif i1Ii11II == 30039 : oOOo0O00o ( )
elif i1Ii11II == 50000 : i1I1i111Ii ( )
elif i1Ii11II == 50001 : Ii1i ( )
elif i1Ii11II == 50002 : I1III1i ( OOOiiiiI )
elif i1Ii11II == 50003 : Table_Menu ( I111IIiii1Ii )
elif i1Ii11II == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif i1Ii11II == 60001 : III1I1ii ( )
elif i1Ii11II == 60002 : i1I1i1I111 ( o000O0O )
elif i1Ii11II == 60003 : Oo00oo ( OOOiiiiI )
elif i1Ii11II == 600033 : oo0OOoooo0O0 ( OOOiiiiI )
elif i1Ii11II == 60004 : o00oOoo0o00 ( OOOiiiiI )
elif i1Ii11II == 50004 : OOoOooOoOOOoo ( )
elif i1Ii11II == 50005 : speedtest . runtest ( OOOiiiiI )
elif i1Ii11II == 70001 : oOoo00 ( )
elif i1Ii11II == 70002 : OOoOOoo0 ( OOOiiiiI )
elif i1Ii11II == 70003 : oo0OOO0OOoOO ( OOOiiiiI )
elif i1Ii11II == 70004 : oOoO ( OOOiiiiI )
elif i1Ii11II == 70005 : II1i1 ( OOOiiiiI )
elif i1Ii11II == 70006 : o0o0oo0OOo0O0 ( )
elif i1Ii11II == 50006 : o0OIiII ( i1 , i1111 )
elif i1Ii11II == 80000 : iIIi1 ( )
elif i1Ii11II == 80001 : resolvefilmon ( OOOiiiiI )
elif i1Ii11II == 80002 : iII ( )
elif i1Ii11II == 80003 : oo0oOi1i1IIi ( o000O0O , OOOiiiiI , "None" )
elif i1Ii11II == 80004 : o0oo00OOOo ( o000O0O , OOOiiiiI )
elif i1Ii11II == 80005 : o0O0O0ooo0oOO ( )
elif i1Ii11II == 80006 : Iiii1Ii ( OOOiiiiI )
elif i1Ii11II == 80007 : ooOOo00oo0 ( OOOiiiiI )
elif i1Ii11II == 80008 : IIIII1Ii ( )
elif i1Ii11II == 80009 : oOi1IiIiIii11I ( )
elif i1Ii11II == 80010 : O0o0O00 ( OOOiiiiI )
elif i1Ii11II == 80011 : i1o00Oo ( OOOiiiiI )
elif i1Ii11II == 80012 : OOoO000oO ( )
elif i1Ii11II == 90000 : OOoO00OOo ( o000O0O , OOOiiiiI )
elif i1Ii11II == 90001 : tools ( )
elif i1Ii11II == 90002 : Oo00O ( )
elif i1Ii11II == 90003 : I1Iii1III ( OOOiiiiI )
elif i1Ii11II == 90004 : Oo0oo0OoO0o0 ( OOOiiiiI )
elif i1Ii11II == 90005 : I1IO0 ( OOOiiiiI )
elif i1Ii11II == 90006 : Ii11IiiI ( OOOiiiiI )
elif i1Ii11II == 90007 : iII11iiI1i11I ( OOOiiiiI )
elif i1Ii11II == 90008 : o0OoO ( OOOiiiiI )
elif i1Ii11II == 90009 : OO0OOOoO0O0 ( OOOiiiiI )
elif i1Ii11II == 90010 : iiI1IIIi ( )
elif i1Ii11II == 90020 : o00OooooOOOO ( )
elif i1Ii11II == 90021 : hellyeah2 ( OOOiiiiI )
elif i1Ii11II == 90022 : hellyeah3 ( OOOiiiiI )
elif i1Ii11II == 90023 : Ooo0oO0 ( )
elif i1Ii11II == 90024 : o00OOo ( OOOiiiiI )
elif i1Ii11II == 90025 : ooooOoO0O ( OOOiiiiI )
if 48 - 48: i1i1I1IIii1II . I11i - oooOo0oo0oo
elif i1Ii11II == 90026 : OooO00oo0O0 ( )
elif i1Ii11II == 90027 : o0oi1I1I1I ( o000O0O , OOOiiiiI , I111IIiii1Ii )
elif i1Ii11II == 90028 : OO0III ( OOOiiiiI )
if 29 - 29: I1ii11iIi11i - o0ii1I - I1ii11iIi11i
elif i1Ii11II == 900300 : i11II1I11I1 ( )
elif i1Ii11II == 900301 : OOoOO0ooo ( OOOiiiiI )
elif i1Ii11II == 900302 : IiI1iiiIii ( OOOiiiiI )
elif i1Ii11II == 90030 : OooOo0oo0O0o00O ( )
elif i1Ii11II == 90031 : IIIIiii1IIii ( )
elif i1Ii11II == 90032 : II1i11I ( OOOiiiiI )
elif i1Ii11II == 90033 : ii1I1IIii11 ( OOOiiiiI )
elif i1Ii11II == 90034 : iII1i1 ( OOOiiiiI )
elif i1Ii11II == 90035 : ooo00Ooo ( OOOiiiiI )
elif i1Ii11II == 90036 : o0Ooo0 ( OOOiiiiI )
elif i1Ii11II == 90039 : O00O0oO ( OOOiiiiI )
elif i1Ii11II == 90037 : I1 ( OOOiiiiI )
elif i1Ii11II == 900377 : iiI1I1IIi11i1 ( OOOiiiiI )
elif i1Ii11II == 90038 : i1i1 ( )
if 89 - 89: I1ii11iIi11i . oO0o . Ii1I * i1i1I1IIii1II . o0o00Oo0O
elif i1Ii11II == 10090 : ii11i ( )
elif i1Ii11II == 10091 : oooOoO00O ( OOOiiiiI )
elif i1Ii11II == 10092 : iiIiii ( OOOiiiiI )
elif i1Ii11II == 10093 : iii1II11II1 ( OOOiiiiI , i1iIiIi1I )
elif i1Ii11II == 10094 : i1oOOOoOO ( OOOiiiiI , i1iIiIi1I )
if 72 - 72: Ii % Iii / i1IiiiI1iI + oOo0O0Ooo * IiI1i11I
elif i1Ii11II == 10095 : O0Oo00OoOo ( )
elif i1Ii11II == 10096 : IiiIIi1 ( OOOiiiiI )
elif i1Ii11II == 10097 : IiI ( OOOiiiiI )
elif i1Ii11II == 10098 : ii11iIIi ( OOOiiiiI )
elif i1Ii11II == 10099 : OO0ooo0 ( OOOiiiiI )
if 69 - 69: i1IiiiI1iI + o0o00Oo0O . III1iiIii . I11i
elif i1Ii11II == 10200 : oo00ooOoO00 ( )
elif i1Ii11II == 10201 : OoOOo00 ( OOOiiiiI )
elif i1Ii11II == 10202 : iIoo0ooooO ( OOOiiiiI )
elif i1Ii11II == 10203 : RT4 ( OOOiiiiI )
if 38 - 38: III1iiIii / ooOoO0O00
elif i1Ii11II == 90040 : iIII11Iiii1 ( )
elif i1Ii11II == 90041 : OoO0 ( OOOiiiiI )
elif i1Ii11II == 90042 : o0iIIIIi ( OOOiiiiI )
elif i1Ii11II == 90043 : ii11iiI11I ( OOOiiiiI )
elif i1Ii11II == 90044 : I1IIII1i1 ( OOOiiiiI )
elif i1Ii11II == 90045 : IiIiI1i1 ( )
elif i1Ii11II == 90046 : oOO0 ( OOOiiiiI )
elif i1Ii11II == 90050 : I1IiiIiii1 ( )
elif i1Ii11II == 90051 : IiIIII1iiIIi ( OOOiiiiI )
elif i1Ii11II == 90052 : OO0OOoo0OOO ( OOOiiiiI )
elif i1Ii11II == 90053 : iII1Iii11111 ( OOOiiiiI )
elif i1Ii11II == 90054 : Iiii1 ( OOOiiiiI )
elif i1Ii11II == 90055 : I11iiI11iiI ( )
if 60 - 60: OOooOOo
elif i1Ii11II == 100001 : Stand_up ( )
if 75 - 75: IIiIiII11i / iI11I1II1I1I / ii
elif i1Ii11II == 100003 : OO0OoOOO0 ( OOOiiiiI )
elif i1Ii11II == 100004 : o0O0Oo00Oo0o ( OOOiiiiI )
elif i1Ii11II == 100005 : Resolve ( OOOiiiiI )
elif i1Ii11II == 100008 : Search ( )
elif i1Ii11II == 100007 : IIi1IIIIi ( OOOiiiiI )
elif i1Ii11II == 100009 : yt . PlayVideo ( OOOiiiiI )
elif i1Ii11II == 100010 : ii1oOoO0o0ooo ( OOOiiiiI )
elif i1Ii11II == 100100 : o0OOOOoo0o ( i1iIiIi1I , OOOiiiiI , oOooooO0o0OOO )
elif i1Ii11II == 100101 : oooOO0OO0O ( OOOiiiiI , o000O0O , I11iI1i1I11I11 , oOooooO0o0OOO , i1iIiIi1I )
elif i1Ii11II == 100102 : iIIIi1i1I11i ( o000O0O , OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 )
elif i1Ii11II == 100106 : OoooO0o ( OOOiiiiI , o000O0O )
elif i1Ii11II == 100107 : OOOo ( )
elif i1Ii11II == 100108 : Oo0OooO ( )
elif i1Ii11II == 100109 : O0Oooo0OoOOo ( OOOiiiiI )
elif i1Ii11II == 40000 : III ( )
elif i1Ii11II == 40001 : oO0oo ( OOOiiiiI )
elif i1Ii11II == 100110 : iiiI1i1 ( OOOiiiiI )
elif i1Ii11II == 100111 : OoO00ooO ( OOOiiiiI )
elif i1Ii11II == 100112 : ii1O0ooooo000 ( OOOiiiiI )
elif i1Ii11II == 100113 : OO00oo ( OOOiiiiI )
elif i1Ii11II == 100114 : I1i1i11 ( OOOiiiiI )
elif i1Ii11II == 100115 : O0Oooo ( OOOiiiiI )
elif i1Ii11II == 100117 : i1IoOOoooO0O0 ( OOOiiiiI )
elif i1Ii11II == 100118 : Oo000o ( OOOiiiiI )
elif i1Ii11II == 100120 : I11iI1I ( OOOiiiiI )
elif i1Ii11II == 1001200 : Iii1iiIi1II1 ( OOOiiiiI )
elif i1Ii11II == 100210 : O0O0o0o0o ( OOOiiiiI )
elif i1Ii11II == 100211 : iIIiiIi ( )
elif i1Ii11II == 100212 : II11ii1I11 ( )
elif i1Ii11II == 100213 : OoOoOoo0OoO0 ( )
elif i1Ii11II == 100214 : Oo0000OOO0 ( )
elif i1Ii11II == 1000111 :
 ii1oO0Oo ( OOOiiiiI )
 if 61 - 61: III1iiIii . III1iiIii
elif i1Ii11II == 1001111 :
 o0OoO000O ( o000O0O , OOOiiiiI )
 if 17 - 17: OOooOOo % I1ii11iIi11i / i1IiiiI1iI . o0ii1I % oO0o
elif i1Ii11II == 1002111 :
 iiI1I1iii1 ( )
 if 32 - 32: oOo0O0Ooo + i1iIi / o0o00Oo0O * Ii % I1ii11iIi11i + IIiIiII11i
elif i1Ii11II == 1003111 :
 ooO0O0oO ( OOOiiiiI , o000O0O )
 if 95 - 95: IiI1i11I / i1iIi + i1IiiiI1iI
elif i1Ii11II == 1004111 :
 ooo0oO0o000O0 ( )
 if 78 - 78: iI11I1II1I1I / oOo0O0Ooo - III1iiIii
elif i1Ii11II == 1005111 :
 OO0oOo00OO0 ( OOOiiiiI , o000O0O )
elif i1Ii11II == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( OOOiiiiI , I11iI1i1I11I11 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( o000O0O , OOOiiiiI , I11iI1i1I11I11 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( o000O0O , OOOiiiiI , I11iI1i1I11I11 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1105000 :
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( o000O0O , OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 , O0o0000o00OO0 )
elif i1Ii11II == 1106000 :
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( o000O0O )
elif i1Ii11II == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( OOOiiiiI )
elif i1Ii11II == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( o000O0O )
elif i1Ii11II == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( o000O0O , OOOiiiiI )
elif i1Ii11II == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif i1Ii11II == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( OOOiiiiI )
elif i1Ii11II == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in OOOiiiiI :
  import urlresolver
  Oo0o0O00 = urlresolver . resolve ( OOOiiiiI )
  ii1 = xbmcgui . ListItem ( path = Oo0o0O00 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 elif not OOOiiiiI . startswith ( "plugin://plugin" ) or not any ( x in OOOiiiiI for x in pyramid . g_ignoreSetResolved ) :
  ii1 = xbmcgui . ListItem ( path = OOOiiiiI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + OOOiiiiI + ')' )
elif i1Ii11II == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( o000O0O , playlist )
elif i1Ii11II == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( OOOiiiiI , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1117000 :
 OOOiiiiI , oo00oo00 = getRegexParsed ( regexs , OOOiiiiI )
 if OOOiiiiI :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( OOOiiiiI , o000O0O , i1iIiIi1I , oo00oo00 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif i1Ii11II == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 I1iI1iI1iiI1 = youtubedl . single_YD ( OOOiiiiI )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( I1iI1iI1iiI1 , o000O0O , i1iIiIi1I )
elif i1Ii11II == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( OOOiiiiI ) , o000O0O , i1iIiIi1I , True )
elif i1Ii11II == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , o000O0O , 'video' )
elif i1Ii11II == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OOOiiiiI , o000O0O , 'video' )
elif i1Ii11II == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( OOOiiiiI , o000O0O , 'audio' )
elif i1Ii11II == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1126000 :
 o000O0O = o000O0O . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( OOOiiiiI , search_term = o000O0O [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( OOOiiiiI )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif i1Ii11II == 1124 : from imports . pyramid import pyramid ; pyramid . Search_Raiz ( )
elif i1Ii11II == 1125 : from imports . pyramid import pyramid ; pyramid . SKindex_Raiz ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1126 : from imports . pyramid import pyramid ; pyramid . Search_Thunder ( )
elif i1Ii11II == 1127 : from imports . pyramid import pyramid ; pyramid . SKindex_thunderstruck ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( o000O0O , OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 )
elif i1Ii11II == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( OOOiiiiI , i1iIiIi1I , I11iI1i1I11I11 ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( o000O0O , OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( OOOiiiiI )
elif i1Ii11II == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( OOOiiiiI ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i1Ii11II == 9050000 : iii1 ( )
elif i1Ii11II == 9060000 : o0OoO000O ( o000O0O , OOOiiiiI )
elif i1Ii11II == 9080000 : iiI11I1i1i1iI ( )
elif i1Ii11II == 9070000 : oooOOOO0oooo ( )
elif i1Ii11II == 9090000 : OooOOO0O00 ( )
elif i1Ii11II == 9100000 : I11Ii11iI1 ( )
elif i1Ii11II == 9110000 : OO00oo0o ( )
elif i1Ii11II == 9999999 : o0O0O0oo0oo0 ( )
elif i1Ii11II == 19999999 : O0O000oOo0O ( )
elif i1Ii11II == 1999990 : o00o0oOo0O0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
