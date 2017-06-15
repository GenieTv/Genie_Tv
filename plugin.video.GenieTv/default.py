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
IiiIII111iI = "3.5.4"
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
  o0OIiII ( 'Change Log 11/6/17 - v3.5.4' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORred]Following recent server issues some items are temporarily offline[/COLOR],[CR][COLORorangered]This is being worked on at top priority and will be back ASAP[/COLOR],[CR][COLORsteelblue]Items Affected[/COLOR],[CR][COLORsteelblue] StreamTeam[/COLOR],[CR][COLORsteelblue] G.O.D.S[/COLOR],[CR][COLORsteelblue]Boss Docs[/COLOR],[CR][COLORsteelblue]Search Lists[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 11/6/17 - v3.5.4' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORred]Following recent server issues some items are temporarily offline[/COLOR],[CR][COLORorangered]This is being worked on at top priority and will be back ASAP[/COLOR],[CR][COLORsteelblue]Items Affected[/COLOR],[CR][COLORsteelblue] StreamTeam[/COLOR],[CR][COLORsteelblue] G.O.D.S[/COLOR],[CR][COLORsteelblue]Boss Docs[/COLOR],[CR][COLORsteelblue]Search Lists[/COLOR],[CR]General Maintence' )
def Iii1I1I11iiI1 ( ) :
 iii ( )
 I1IiiiiI ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I1I1i1I ( )
 else :
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']WIZARD[/COLOR]' , str ( oO0000OOo00 ) , 4001 , iiIi1IIiIi + 'Wizard.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 4009 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 99 - 99: o0ii1I / I1ii11iIi11i / III1iiIii % oOo0O0Ooo
  if oo00 . getSetting ( 'Music' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if OooOoOO0 ( ) == 'android' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '' , 10050 , iiIi1IIiIi + 'Addons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def I1I1i1I ( ) :
 if 15 - 15: Ii % o0ii1I . I1ii11iIi11i + Ii1I
 if 61 - 61: I1ii11iIi11i * Ii1I % I1ii11iIi11i - ooOoO0O00 - iI11I1II1I1I
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']WIZARD[/COLOR]' , str ( oO0000OOo00 ) , 4001 , iiIi1IIiIi + 'Wizard.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 if 74 - 74: Ii1I + IIiIiII11i / oO0o
 if oo00 . getSetting ( 'Music' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def tools ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']Change Log[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  ii1iII1II ( )
 if I111I1Iiii1i == 1 :
  oo0OOo0 ( )
 if I111I1Iiii1i == 2 :
  oOOoo00O00o ( )
 if I111I1Iiii1i == 3 :
  O0O00Oo ( )
 if I111I1Iiii1i == 4 :
  oooooo0O000o ( OoO )
 if I111I1Iiii1i == 5 :
  iIii1 . ok ( i1 , i1111 )
 if I111I1Iiii1i == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if I111I1Iiii1i == 7 :
  ooO0O0O0ooOOO ( )
  if 77 - 77: OOooOOo - IIiIiII11i - i1iIi
def IiiiIIiIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OoOOoOooooOOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , oo0O0 , iI , OO0O000 in OoOOoOooooOOo :
  i11I1II1I11i ( OO0O000 , url , 21009 , oOo0O , iI , oo0O0 )
  if 37 - 37: ii - o0o00Oo0O - I11i
def o0o0O0O00oOOo ( url ) :
 url = url
 iIIIiIi = OooOoOO0 ( )
 if iIIIiIi ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif iIIIiIi ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 100 - 100: oOo0O0Ooo / I11i % IIiIiII11i % I1ii11iIi11i % oooOo0oo0oo
  if 98 - 98: Iii % Ii % i1iIi + o0ii1I
def OOoOO0o0o0 ( ) :
 OoO = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( OoO , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iiI11ii1I1 ( OoO )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOoOoO0 ( )
def oOo0OOoO0 ( ) :
 IIo0Oo0oO0oOO00 = oo00OO0000oO ( )
 I1II1 = IIo0Oo0oO0oOO00 . replace ( II11iiii1Ii , "" )
 if os . path . exists ( IIo0Oo0oO0oOO00 ) or not IIo0Oo0oO0oOO00 == False :
  oooO = open ( IIo0Oo0oO0oOO00 , mode = 'r' ) ; i1I1i111Ii = oooO . read ( ) ; oooO . close ( )
  o0OIiII ( "%s - %s" % ( i1 , I1II1 ) , i1I1i111Ii )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OOoOO0o0o0 ( ) :
 OoO = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( OoO , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iiI11ii1I1 ( OoO )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOoOoO0 ( )
def ooo ( ) :
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 27 - 27: i1iIi % oOo0O0Ooo
 ii1I ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 73 - 73: oooOo0oo0oo
def ooO ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def Ooo0oOooo0 ( url ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 oOOOoo00 = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iiIiIIIiiI = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in oOOOoo00 :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 900302 , oOo0O , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for iiI1IIIi in iiIiIIIiiI :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , iiI1IIIi , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def II11IiIi11 ( url ) :
 IIOOO0O00O0OOOO = OooOoooOo ( url )
 oOOOoo00 = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
 I1iiii1I = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
 for url , OO0O000 in oOOOoo00 :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , OO0O000 in I1iiii1I :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def OOo0 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oo0o , o0oO0oooOoo in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + oo0o , o0oO0oooOoo )
def I1III1111iIi ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def I1i111I ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , oOo0O , Oo00OOOOO , '' )
 for url in next :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def OooOo0oo0O0o00O ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 I1i11 = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 IiIi1I1 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for OO0O000 , url in i1Iii1i1I :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for OO0O000 , url in IiIi1I1 :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in I1i11 :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 39 - 39: IIiIiII11i + OOooOOo - i1iIi . OOooOOo
def OOOooo ( url ) :
 if 'drive' in url :
  OooO0OO ( url )
 else :
  oO00ooooO0o = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( oO00ooooO0o )
  for url in IIi :
   OooO0OO ( url )
def o0OOo0o0O0O ( url ) :
 o0OO0o0oOOO0O = liveresolver . resolve ( url )
 iII1i11 = xbmcgui . ListItem ( path = o0OO0o0oOOO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
def OooIiIIII1i11I ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 OOOiII1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
def oo00OO0000oO ( ) :
 OOo = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return OOo
 if 22 - 22: OOooOOo * o0o00Oo0O . III1iiIii * Ii - oOo0O0Ooo * i1iIi
def OOooo0O0o0 ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , II1iI1I11I :
  return II1iI1I11I
 return True
def o0OO0 ( ) :
 if 44 - 44: o0o00Oo0O - o0ii1I - o0o00Oo0O % Iii . i1i1I1IIii1II
 if 74 - 74: Ii . oOo0O0Ooo
 if 36 - 36: ii . oO0o
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 if 39 - 39: o0o00Oo0O + i1IiiiI1iI
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def OoOooOoO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   iiIiii1iI1i ( )
  if I111I1Iiii1i == 1 :
   I1ii1ii11i1I ( )
  if I111I1Iiii1i == 2 :
   o0OoOO ( O0O0Oo00 )
  if I111I1Iiii1i == 3 :
   oOoO00o ( OoO )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 100 - 100: I11i + oooOo0oo0oo * I11i
def oOOo0OOOo00O ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 76 - 76: Ii + I11i / Ii1I - oO0o - o0ii1I + Ii1I
  if 51 - 51: iI11I1II1I1I . i1iIi + iI11I1II1I1I
  if 95 - 95: oOo0O0Ooo
  if 46 - 46: OOooOOo + oO0o
  if 70 - 70: IiI1i11I / iI11I1II1I1I
  ii1I ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
  ii1I ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Series[/COLOR]' , ( i11 ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3BsZXgvZG93bmxvYWRzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  if 96 - 96: ii + i1i1I1IIii1II
  ii1I ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   ii1I ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
 else :
  if 44 - 44: i1i1I1IIii1II
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: OOooOOo / IIiIiII11i
  if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
  ii1I ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
  if 42 - 42: I1ii11iIi11i
  ii1I ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Series[/COLOR]' , ( i11 ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3BsZXgvZG93bmxvYWRzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
  ii1I ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   ii1I ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , str ( oO0000OOo00 ) , 30032 , iiIi1IIiIi + 'News.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , str ( oO0000OOo00 ) , 4008 , iiIi1IIiIi + 'Hobbies.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , str ( oO0000OOo00 ) , 8040 , iiIi1IIiIi + 'documentaries.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' , str ( oO0000OOo00 ) , 7001 , iiIi1IIiIi + 'DiscloseTV.png' , Oo00OOOOO , '' )
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
 iI1i11iII111 ( 'movies' , 'MAIN' )
def i1iI1 ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  ii1 ( )
 if I111I1Iiii1i == 1 :
  I1IiiI1ii1i ( )
 if I111I1Iiii1i == 2 :
  O0o ( )
 if I111I1Iiii1i == 3 :
  oO0OoO00o ( )
 if I111I1Iiii1i == 4 :
  II1iiiiII ( )
 if I111I1Iiii1i == 5 :
  O0OoOO0oo0 ( )
  if 96 - 96: OOooOOo . I11i - i1iIi
  if 99 - 99: III1iiIii . I1ii11iIi11i - o0ii1I % o0ii1I * o0o00Oo0O . IIiIiII11i
def iIIII1iIIii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   oOOO00o000o ( )
  if I111I1Iiii1i == 1 :
   iIi11i1 ( )
  if I111I1Iiii1i == 2 :
   oO00oo0o00o0o ( OoO )
  if I111I1Iiii1i == 3 :
   IiIIIIIi ( )
  if I111I1Iiii1i == 4 :
   IiIi1iIIi1 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if I111I1Iiii1i == 5 :
   O0OoO0ooOO0o ( )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def oO0o00ooO ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 24 - 24: III1iiIii * Ii * oooOo0oo0oo
 if 85 - 85: I11i . OOooOOo / i1iIi . o0o00Oo0O % i1IiiiI1iI
 if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . IiI1i11I
 if 8 - 8: i1iIi + IIiIiII11i / IiI1i11I / Iii
 if 74 - 74: o0o00Oo0O / ooOoO0O00
def OoOIiiiii111i1ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   i1i1iII1 ( )
  if I111I1Iiii1i == 1 :
   iii11i1IIII ( )
  if I111I1Iiii1i == 2 :
   Iio00 ( )
  if I111I1Iiii1i == 3 :
   iiI1Ii1 ( )
  if I111I1Iiii1i == 4 :
   ii1i ( )
  if I111I1Iiii1i == 5 :
   oOOoo ( )
  if I111I1Iiii1i == 6 :
   iII1111III1I ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 39 - 39: ooOoO0O00 / III1iiIii
  if 78 - 78: i1iIi
  if 53 - 53: i1iIi * oooOo0oo0oo . IiI1i11I / o0o00Oo0O * i1iIi
  ii1I ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def II11iI111i1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Oo00OoOo = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 24 - 24: Ii - i1IiiiI1iI
   if 21 - 21: Iii
   if 92 - 92: Ii / i1IiiiI1iI - IiI1i11I % i1iIi * i1IiiiI1iI + I1ii11iIi11i
   if 11 - 11: ii . i1IiiiI1iI
  oOo0O0Oo00oO = [ Oo00OoOo , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   Oo0000oOo ( )
  if I111I1Iiii1i == 1 :
   I11o0oO00oO0o0o0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , I1I , OO0O000 )
  if I111I1Iiii1i == 2 :
   ooooo ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if I111I1Iiii1i == 3 :
   I11o0oO00oO0o0o0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , I1I , OO0O000 )
 else :
  if 1 - 1: i1iIi % OOooOOo * I1ii11iIi11i
  if 55 - 55: OOooOOo
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 87 - 87: ii % IiI1i11I . oOo0O0Ooo / i1iIi
  if 8 - 8: Iii + I11i
  if 90 - 90: Ii1I
  ii1I ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 62 - 62: i1IiiiI1iI . III1iiIii . ii
  if 11 - 11: oooOo0oo0oo / Iii
  if 73 - 73: ooOoO0O00 / Ii
  if 58 - 58: I1ii11iIi11i . IIiIiII11i + i1i1I1IIii1II - Ii / IIiIiII11i / o0o00Oo0O
  if 85 - 85: OOooOOo + oooOo0oo0oo
  if 10 - 10: III1iiIii / oO0o + OOooOOo / ooOoO0O00
  if 27 - 27: o0ii1I
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 67 - 67: oOo0O0Ooo
def OO00OO0O0 ( ) :
 iii ( )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def ooooo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 i1I111Ii1i11 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( i1I111Ii1i11 ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1I111Ii1i11 ) )
 IiIi1I1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1I111Ii1i11 ) )
 for OO0O000 , oOo0O , url in IIi :
  if '247ch' in url :
   o0O0O0o ( OO0O000 , url , 10190 , oOo0O )
  elif '.m3u' in url :
   o0O0O0o ( OO0O000 , url , 1019 , oOo0O )
  elif '.xml' in url :
   o0O0O0o ( OO0O000 , url , 1018 , oOo0O )
  else :
   OO ( OO0O000 , url , 222 , oOo0O )
 for OO0O000 , url , oOo0O in i1Iii1i1I :
  if '.xml' in url :
   o0O0O0o ( OO0O000 , url , 1018 , oOo0O )
  elif '.m3u' in url :
   o0O0O0o ( OO0O000 , url , 1019 , oOo0O )
  else :
   OO ( OO0O000 , url , 222 , oOo0O )
 for OO0O000 , url , oOo0O in IiIi1I1 :
  OO ( OO0O000 , url , 8043 , oOo0O )
def iI11I ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def oOOOO ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , oOo0O in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , oOo0O )
  if 49 - 49: IIiIiII11i . i1i1I1IIii1II . Ii % III1iiIii
def i11i1iiI1i ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 ii1I ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 ii1I ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 87 - 87: i1iIi
def IIIii ( url ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , IiI11i1IIiiI , oOOo000oOoO0 , iI , oo0O0 in IIi :
  if oOOo000oOoO0 == '123' :
   oOOo000oOoO0 = iiIi1IIiIi + 'appstreams.png'
  if iI == '123' :
   iI = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   ii1I ( OO0O000 , url , 100010 , oOOo000oOoO0 , iI , oo0O0 )
  elif 'playlist' in url :
   ii1I ( OO0O000 , url , 100007 , oOOo000oOoO0 , iI , oo0O0 )
  elif 'watchseries' in url :
   ii1I ( OO0O000 , url , 100100 , oOOo000oOoO0 , iI , oo0O0 )
  elif not 'http' in url :
   OoOo00o0OO ( OO0O000 , url , 100009 , oOOo000oOoO0 , iI , oo0O0 , '' )
  else :
   OoOo00o0OO ( OO0O000 , url , 100005 , oOOo000oOoO0 , iI , oo0O0 , '' )
   if 1 - 1: oOo0O0Ooo % i1iIi
def oOoO00 ( url ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 OoOOoOooooOOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , oo0O0 , iI , OO0O000 in OoOOoOooooOOo :
  if oOo0O == '123' :
   oOo0O = iiIi1IIiIi + 'appstreams.png'
  if iI == '123' :
   iI = Oo00OOOOO
  if 'php' in url :
   ii1I ( OO0O000 , url , 100004 , oOo0O , iI , oo0O0 )
  elif 'playlist' in url :
   ii1I ( OO0O000 , url , 100007 , oOo0O , iI , oo0O0 )
  elif 'watchseries' in url :
   ii1I ( OO0O000 , url , 100100 , oOo0O , iI , oo0O0 )
  elif not 'http' in url :
   OoOo00o0OO ( OO0O000 , url , 100009 , oOo0O , iI , oo0O0 , '' )
  else :
   OoOo00o0OO ( OO0O000 , url , 100005 , oOo0O , iI , oo0O0 , '' )
   if 40 - 40: I11i
def OOOoooOo00oo0000OO ( url ) :
 if 69 - 69: i1iIi - oO0o / Ii + Ii1I % ii
 II11iIiIIIiI = O00OooOo00o ( url )
 o000O000 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1I111Ii1i11 in o000O000 :
  oOOo000oOoO0 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( i1I111Ii1i11 ) )
  for oOOo000oOoO0 in oOOo000oOoO0 :
   oOOo000oOoO0 = oOOo000oOoO0
  OO0O000 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( i1I111Ii1i11 ) )
  for OO0O000 in OO0O000 :
   if 'elete' in OO0O000 :
    pass
   elif 'rivate Vid' in OO0O000 :
    pass
   else :
    OO0O000 = ( OO0O000 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  ii1oOoO0o0ooo = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( i1I111Ii1i11 ) )
  for ii1oOoO0o0ooo in ii1oOoO0o0ooo :
   ii1oOoO0o0ooo = ii1oOoO0o0ooo
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( i1I111Ii1i11 ) )
  for url in url :
   url = url
  OoOo00o0OO ( '[COLORred]' + str ( ii1oOoO0o0ooo ) + '[/COLOR] : ' + str ( OO0O000 ) , str ( url ) , 100009 , str ( oOOo000oOoO0 ) , Oo00OOOOO , '' , '' )
  iI1i11iII111 ( 'movies' , '' )
  if 86 - 86: Ii1I * o0o00Oo0O * III1iiIii
  if 51 - 51: IIiIiII11i + III1iiIii . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
  if 72 - 72: i1i1I1IIii1II + i1i1I1IIii1II / IIiIiII11i . ii % o0ii1I
  if 49 - 49: i1i1I1IIii1II . oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OoOOoOooooOOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , oo0O0 , iI , OO0O000 in OoOOoOooooOOo :
  if '.php' in url :
   ii1I ( OO0O000 , url , 100210 , oOo0O , iI , oo0O0 )
  else :
   i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iI , oo0O0 )
   if 83 - 83: Iii / Ii1I
   if 34 - 34: oOo0O0Ooo * I1ii11iIi11i * i1IiiiI1iI / oO0o * Iii / iI11I1II1I1I
   if 74 - 74: I1ii11iIi11i / Ii - IIiIiII11i * I11i
def IIi1IIIIi ( iconimage , url , extra ) :
 oOOo000oOoO0 = ' '
 OOOoO = ' '
 iI = ' '
 I1i = ' '
 iiiI = O00OooOo00o ( url )
 oOOo000oOoO0 = re . compile ( '<img src="(.+?)">' ) . findall ( iiiI )
 for oOOo000oOoO0 in oOOo000oOoO0 :
  oOOo000oOoO0 = oOOo000oOoO0
 IiIi1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( iiiI )
 for iI in IiIi1 :
  iI = iI
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( iiiI )
 for url , I1i in IIi :
  I1i = 'S' + ( I1i ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  i111iiI1ii ( ( I1i ) . replace ( '  ' , '' ) , url , 100101 , oOOo000oOoO0 , iI , OOOoO , '' )
  iI1i11iII111 ( 'Movies' , 'info' )
  if 24 - 24: OOooOOo / ii . IIiIiII11i . oOo0O0Ooo % o0o00Oo0O % o0ii1I
def IiIII1i1i ( url , name , fanart , extra , iconimage ) :
 II11I = extra
 I1i = name
 iiiI = O00OooOo00o ( url )
 oOOo000oOoO0 = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( iiiI )
 for url , name , oo0oOO00oO in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  oo0oOO00oO = oo0oOO00oO
  i11i1iIiii = name + ' - [COLORred]' + oo0oOO00oO + '[/COLOR]'
  i111iiI1ii ( i11i1iIiii , url , 100102 , oOOo000oOoO0 , fanart , 'Aired : ' + oo0oOO00oO , i11i1iIiii )
  if 71 - 71: Ii1I % i1iIi - oOo0O0Ooo % Iii - o0o00Oo0O
def o0O0O0 ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = O00OooOo00o ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , name in IIi :
  for iII1i11 in o00OO00OoO :
   if iII1i11 in OoO :
    URL = 'http://www.watchseriesgo.to/link/' + OoO
    OoOo00o0OO ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  i111iiI1ii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 6 - 6: IiI1i11I . III1iiIii * OOooOOo . ooOoO0O00
  if 98 - 98: ooOoO0O00
def oO0O ( url , name ) :
 oOO = name
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiiIIiIi ( url , oOO )
 for url in i1Iii1i1I :
  iiiIIiIi ( url , oOO )
 for url in IiIi1I1 :
  iiiIIiIi ( url , oOO )
  if 68 - 68: o0o00Oo0O + OOooOOo / i1i1I1IIii1II - oooOo0oo0oo + iI11I1II1I1I % o0ii1I
def iiiIIiIi ( url , season_name ) :
 if 'daclips.in' in url :
  i1iI1iii11i ( url , season_name )
 elif 'filehoot.com' in url :
  oOO00oO00O0OO ( url , season_name )
 elif 'allmyvideos.net' in url :
  oOo00OO ( url , season_name )
 elif 'vidspot.net' in url :
  o0oOO0OO ( url , season_name )
 elif 'vodlocker' in url :
  Oo00OoO00o0 ( url , season_name )
 elif 'vidto' in url :
  OOoOoO00O0O0o ( url , season_name )
  if 12 - 12: Ii1I + oO0o % Iii
  if 85 - 85: IiI1i11I * I11i
def OOoOoO00O0O0o ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 , OO0O000 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 96 - 96: Ii1I / IIiIiII11i . o0ii1I - IiI1i11I * Iii * i1i1I1IIii1II
  if 76 - 76: o0ii1I - IIiIiII11i * oooOo0oo0oo / ii
def oOo00OO ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 , OO0O000 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 18 - 18: oO0o + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
def o0oOO0OO ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 , OO0O000 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 71 - 71: ii
def Oo00OoO00o0 ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 33 - 33: i1IiiiI1iI
def i1iI1iii11i ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 62 - 62: Ii1I + o0ii1I + ooOoO0O00 / ii
def oOO00oO00O0OO ( url , season_name ) :
 II11iIiIIIiI = O00OooOo00o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1iii11i1 in IIi :
  I11Oo00oO0O ( ii1iii11i1 , season_name )
  if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
def I11Oo00oO0O ( Link , season_name ) :
 if 'http:/' in Link :
  I111i1I1 ( Link )
  if 62 - 62: oooOo0oo0oo * i1IiiiI1iI / I1ii11iIi11i * I11i
def II1Ii1iI1i1 ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 o0OoO000O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in o0OoO000O :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 94 - 94: OOooOOo . o0o00Oo0O / o0ii1I . Ii1I - ooOoO0O00
def i111iiI1ii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  if 65 - 65: ooOoO0O00 . ii * o0ii1I / III1iiIii
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = True )
 return oo0oo0OOOOOoO
 if 86 - 86: OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % iI11I1II1I1I / oooOo0oo0oo
 if 11 - 11: oOo0O0Ooo * i1i1I1IIii1II + Ii1I / Ii1I
def OoOo00o0OO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  O00OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = False )
 return oo0oo0OOOOOoO
 if 37 - 37: Ii + ooOoO0O00
def I1i11II ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 31 - 31: i1i1I1IIii1II / III1iiIii * I11i . IIiIiII11i
def oooOO0OO0O ( url ) :
 o00o = xbmc . Player ( III11I ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o00o . play ( url ) . strip ( )
 except : pass
 if 17 - 17: ii + oooOo0oo0oo * Iii * OOooOOo
def I111i1I1 ( url ) :
 o00o = xbmc . Player ( )
 import urlresolver
 try : o00o . play ( url )
 except : pass
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def O00OooOo00o ( url ) :
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
  if 5 - 5: I1ii11iIi11i * OOooOOo
  if 46 - 46: i1iIi
  if 33 - 33: IiI1i11I - IIiIiII11i * ii - I1ii11iIi11i - oooOo0oo0oo
def I1IiiI1ii1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   O0OO0O ( )
  if I111I1Iiii1i == 1 :
   IiiiIiiI ( )
  if I111I1Iiii1i == 2 :
   o00O ( )
  if I111I1Iiii1i == 3 :
   i1iIIi ( )
  if I111I1Iiii1i == 4 :
   oo0OO ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def oO0OoO00o ( ) :
 iii ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiIi1IIiIi + 'Fitness.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']Go Fishing[/COLOR]' , str ( oO0000OOo00 ) , 8090 , iiIi1IIiIi + 'GoFishing.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  ii1I ( '[COLOR' + ooOoOoo0O + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiIi1IIiIi + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 2 - 2: IIiIiII11i - oO0o . III1iiIii * IiI1i11I / i1i1I1IIii1II
 if 80 - 80: oooOo0oo0oo / Iii / OOooOOo + ooOoO0O00 - I1ii11iIi11i
 if 11 - 11: I11i * oO0o
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   iIi1IiI = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iIi1IiI + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   I111I1Iiii1i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if I111I1Iiii1i == 0 :
    I11IIIiIi11 ( II1I )
    Ooo0OOoOoO0 ( )
   elif I111I1Iiii1i == 1 :
    I11iiIi1i1 ( II1I )
  else :
   pass
   if 41 - 41: o0ii1I % Ii1I
def I11iiIi1i1 ( addon ) :
 iIi1IiI = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 12 - 12: oooOo0oo0oo
def I11IIIiIi11 ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 ooOo0O = os . path . join ( IIIII , 'default.py' )
 i1I1IIIiiI = open ( ooOo0O , "w+" )
 if 71 - 71: oooOo0oo0oo * oO0o % ii % oO0o / oOo0O0Ooo
 i1I1IIIiiI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 i1I1IIIiiI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 i1I1IIIiiI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 56 - 56: ii % Ii * iI11I1II1I1I . oO0o * o0o00Oo0O
 if 23 - 23: Ii
 if 39 - 39: I11i - Ii1I % IiI1i11I * oO0o - oooOo0oo0oo / IiI1i11I
 if 29 - 29: Ii1I
def oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIII1iii11 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi1I = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iiiO00O00O000OOO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , iIOo0O , iI , oo0O0 in IIIII1iii11 :
  if 'php' in url :
   ii1I ( OO0O000 , url , 90037 , iIOo0O , iI , oo0O0 )
  elif OO0O000 == 'Search' :
   ii1I ( 'Search' , url , 90038 , iIOo0O , iI , oo0O0 )
  else :
   i11I1II1I11i ( OO0O000 , url , 222 , iIOo0O , iI , oo0O0 )
 for OO0O000 , oOo0O , url , Ii11 in IIi1I :
  ii1I ( OO0O000 , url , 90037 , oOo0O , Ii11 , '' )
 for OO0O000 , oOo0O , url , Ii11 in IIi :
  ii1I ( OO0O000 , url , 90037 , oOo0O , Ii11 , '' )
 for OO0O000 , url , oOo0O , Ii11 in i1Iii1i1I :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , Ii11 , '' )
 for OO0O000 , url , oOo0O , Ii11 in IiIi1I1 :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , Ii11 , '' )
 for OO0O000 , url , oOo0O , Ii11 in I1i11 :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , Ii11 , '' )
 for OO0O000 , url , oOo0O in iiiO00O00O000OOO :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , '' , '' )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
def II1i111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , oOo0O , url , Ii11 in IIi :
  ii1I ( OO0O000 , url , 90037 , oOo0O , Ii11 , '' )
 for OO0O000 , url , oOo0O , Ii11 in i1Iii1i1I :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , Ii11 , '' )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
  if 50 - 50: III1iiIii % ooOoO0O00
def iii11II1I ( ) :
 iI111I11i = [ 'serialsearch' , 'moviesearch' ]
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 if II1i11I1 == '' :
  pass
 else :
  for iiIiIiII in iI111I11i :
   i1I1 = Oo0o0000o0o0 + iiIiIiII + '.php'
   iiiI = OooOoooOo ( i1I1 )
   if iiiI != 'Opened' :
    OoOOoOooooOOo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( iiiI )
    for OO0O000 , OoO , iIOo0O , iI , oo0O0 in OoOOoOooooOOo :
     if II1i11I1 in OO0O000 . lower ( ) :
      iIi = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in iIi :
       if iII1i11 == OoO :
        OO0O000 = '[COLORred]* [/COLOR]' + ( OO0O000 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        iIIi = open ( OOOO0OOoO0O0 , "a" )
        iIIi . write ( 'item="' + OO0O000 + '"\n' )
        iIIi . close
      if 'php' in OoO :
       ii1I ( OO0O000 , OoO , 90037 , iIOo0O , iI , oo0O0 )
      else :
       i11I1II1I11i ( OO0O000 , OoO , 222 , iIOo0O , iI , oo0O0 )
       if 96 - 96: IiI1i11I
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
   if 18 - 18: IiI1i11I * Iii - o0ii1I
def II1i1III ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1iii11i = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for OoO , oOo0O , O0O0 , OO0O000 in IIi :
  OO ( ( '[COLORgold]' + O0O0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + OoO , 90024 , oOo0O )
 for I1IIIii , OoO , oOo0O in i1iii11i :
  OO ( I1IIIii , 'http://www.tvcatchup.com' + OoO , 90024 , oOo0O )
 for OoO , oOo0O , OO0O000 in i1Iii1i1I :
  if 'Submit' in OO0O000 :
   pass
  elif '&lt;' in OO0O000 :
   pass
  else :
   i11I1II1I11i ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + OO0O000 + '[/COLOR]' , OoO , 90025 , 'http://www.djing.com' + oOo0O , Oo00OOOOO , '' )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def IIiIii1III1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 17 - 17: IIiIiII11i / IIiIiII11i
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def o0OO0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiii1I ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 3 - 3: o0o00Oo0O % ii / oooOo0oo0oo
def iIi11i1 ( ) :
 if 89 - 89: IIiIiII11i / i1i1I1IIii1II
 if 14 - 14: oooOo0oo0oo . oOo0O0Ooo * i1iIi + IIiIiII11i - i1iIi + oooOo0oo0oo
 if 18 - 18: i1i1I1IIii1II - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / IiI1i11I . oOo0O0Ooo * OOooOOo
 if 1 - 1: OOooOOo * oO0o . ooOoO0O00 / I1ii11iIi11i . Ii1I + I1ii11iIi11i
 if 17 - 17: I1ii11iIi11i + oO0o / o0ii1I / IiI1i11I * oooOo0oo0oo
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'yr' in OoO :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OoO , 10201 , iiIi1IIiIi + 'rated.png' )
   if 29 - 29: oO0o % ii * i1i1I1IIii1II / IIiIiII11i - i1i1I1IIii1II
def iIi11ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i11I1 , url , OO0O000 in IIi :
  if 'id' in url :
   o0O0O0o ( ( '[COLORred]RANK [COLORblue]' + i11I1 + '[COLORred] - [COLORblue]' + OO0O000 + '[/COLOR]' ) , OO0O000 , 10202 , iiIi1IIiIi + 'rated.png' )
   if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
def I1iI1I1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IiIi1oo00ooOoo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1 = ( url )
 II1i11I1 = I1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iIiII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1
 oo0o0oOo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 50 - 50: IiI1i11I . Ii1I . oO0o * Iii + IIiIiII11i % Ii
 i1i1IiIiIi1Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oO0ooOO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 16 - 16: I1ii11iIi11i + i1iIi / I1ii11iIi11i / oO0o % i1i1I1IIii1II % Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 Ii1II11II1iii = O00O0oOO00O00 ( iiiI1i11Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0oOO0ooOoO = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooO0000o00O = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0Ooo = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 78 - 78: oO0o % III1iiIii * ooOoO0O00
 if 66 - 66: o0ii1I . oOo0O0Ooo + I11i . iI11I1II1I1I
 o0iIiiIiiIi = O00O0oOO00O00 ( i1i1IiIiIi1Ii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 i1iiIIIi = O00O0oOO00O00 ( oO0ooOO )
 if 62 - 62: o0o00Oo0O / oOo0O0Ooo % o0o00Oo0O * oO0o % oOo0O0Ooo
 if 33 - 33: oOo0O0Ooo . i1i1I1IIii1II * oO0o * iI11I1II1I1I
 if 5 - 5: I1ii11iIi11i / III1iiIii % o0o00Oo0O . i1IiiiI1iI * III1iiIii
 if 83 - 83: oooOo0oo0oo
 if 12 - 12: ooOoO0O00 . ooOoO0O00 - I11i
 if 26 - 26: iI11I1II1I1I % Ii % Ii1I
 if 67 - 67: ii
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + oooOo0oo0oo * III1iiIii
 if 2 - 2: ooOoO0O00 - i1iIi + oOo0O0Ooo . I11i * I11i / OOooOOo
 if 93 - 93: ooOoO0O00
 if 53 - 53: ii + I1ii11iIi11i + i1i1I1IIii1II
 if 24 - 24: IiI1i11I - III1iiIii - IiI1i11I * Ii1I . ii / III1iiIii
 if 66 - 66: I1ii11iIi11i
 if O0Ooo != 'Failed' :
  Oooo00oOo = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0Ooo )
  for url , OO0O000 in Oooo00oOo :
   I1i1Ii11i11 = O00O0oOO00O00 ( url )
   Iii1111III111 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i1Ii11i11 )
   for Ii1 , ooo0O0OO in Iii1111III111 :
    ooo0O0OO = ( ooo0O0OO . replace ( '.' , ' ' ) )
    if II1i11I1 in ooo0O0OO . lower ( ) :
     if '.mkv' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 222 , '' , '' , '' )
     elif '.mp4' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 222 , '' , '' , '' )
     elif '.avi' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 222 , '' , '' , '' )
     elif '.wav' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 222 , '' , '' , '' )
     else :
      ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 61 - 61: III1iiIii + iI11I1II1I1I + Ii / Ii % IIiIiII11i
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 42 - 42: o0ii1I * i1IiiiI1iI . III1iiIii * oOo0O0Ooo + OOooOOo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: Iii . oOo0O0Ooo + i1i1I1IIii1II
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for O00OO0o0 , OO0O000 in IiIi1I1 :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OoO00oo00 + O00OO0o0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in I1i11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 52 - 52: Ii1I % i1i1I1IIii1II - Ii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if Ii1II11II1iii != 'Failed' :
  i1III = [ ]
  iiiO00O00O000OOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1II11II1iii )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in iiiO00O00O000OOO :
   if I1 in OO0O000 . lower ( ) :
    if OO0O000 in i1III :
     pass
    else :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , I1I , IiIi1 , oo0O0 )
     i1III . append ( OO0O000 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0oOO0ooOoO != 'Failed' :
  I1Io00oOOoO0oO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0oOO0ooOoO )
  for url , oOo0O , OO0O000 in I1Io00oOOoO0oO :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , oOo0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 26 - 26: o0ii1I * iI11I1II1I1I % oO0o . I11i + I1ii11iIi11i
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: I1ii11iIi11i * o0ii1I + Ii1I * oooOo0oo0oo
    if 16 - 16: Iii / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
    if 26 - 26: I11i * III1iiIii . ooOoO0O00
    if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
    if 62 - 62: Ii % oooOo0oo0oo . III1iiIii . oooOo0oo0oo
    if 84 - 84: Ii * oO0o
    if 18 - 18: oooOo0oo0oo - o0ii1I - OOooOOo / i1IiiiI1iI - o0o00Oo0O
    if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
    if 14 - 14: I11i / oooOo0oo0oo - iI11I1II1I1I - i1i1I1IIii1II % i1iIi
    if 49 - 49: i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
    if 3 - 3: IiI1i11I . i1iIi % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
    if 29 - 29: I11i / Ii / oOo0O0Ooo % i1i1I1IIii1II % Ii
    if 18 - 18: oooOo0oo0oo + i1IiiiI1iI
    if 80 - 80: i1i1I1IIii1II + I11i * o0ii1I + oO0o
    if 75 - 75: Iii / I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
    if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
 if o0iIiiIiiIi != 'Failed' :
  i1iii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0iIiiIiiIi )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in i1iii11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 92 - 92: OOooOOo . ii - i1IiiiI1iI
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: iI11I1II1I1I % IiI1i11I * oooOo0oo0oo * iI11I1II1I1I
    if 73 - 73: I11i % i1IiiiI1iI . oooOo0oo0oo
    if 60 - 60: OOooOOo
    if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
    if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
    if 28 - 28: i1i1I1IIii1II
    if 52 - 52: oOo0O0Ooo + iI11I1II1I1I
    if 71 - 71: o0o00Oo0O / i1i1I1IIii1II
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: Ii1I - IiI1i11I
 O000O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 98 - 98: iI11I1II1I1I + i1IiiiI1iI % OOooOOo + Iii % OOooOOo
 for iiIiIiII in O000O :
  i1I1 = oO0 + iiIiIiII + oOoOooOo0o0
  O0Ooo = O00O0oOO00O00 ( i1I1 )
  if O0Ooo != 'Failed' :
   Oooo00oOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0Ooo )
   for url , I1I , oo0O0 , IiIi1 , OO0O000 in Oooo00oOo :
    if I1 in OO0O000 . lower ( ) :
     i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , I1I , IiIi1 , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 24 - 24: i1i1I1IIii1II * i1IiiiI1iI
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 40 - 40: o0ii1I - OOooOOo * OOooOOo . OOooOOo + ii
 O000O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 77 - 77: iI11I1II1I1I . o0ii1I % i1i1I1IIii1II / o0ii1I
 if 54 - 54: i1i1I1IIii1II + i1iIi - I1ii11iIi11i
 for iiIiIiII in O000O :
  i1I1 = IiIi1oo00ooOoo + iiIiIiII
  I1I1IiIi1 = O00O0oOO00O00 ( i1I1 )
  if I1I1IiIi1 != 'Failed' :
   oOO0o0oo0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1I1IiIi1 )
   for O00OO0o0 , OO0O000 in oOO0o0oo0 :
    if I1 in OO0O000 . lower ( ) :
     OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IiIi1oo00ooOoo + iiIiIiII + O00OO0o0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 78 - 78: oooOo0oo0oo + IiI1i11I . III1iiIii
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
def ii1i ( ) :
 o0O0O0o ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 o0O0O0o ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 o0O0O0o ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 o0O0O0o ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 69 - 69: i1IiiiI1iI - oOo0O0Ooo
def oOoo0OooOOo00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , I1i , Ii1IiIIIIIiI , oo0oOO00oO , O00 in IIi :
  o0O0O0o ( ( '[COLORblue]' + OO0O000 + '[/COLOR] [COLORred]Season[/COLOR]-' + I1i + ' [COLORred]Returns [/COLOR]- ' + O00 + ' ' + oo0oOO00oO ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 14 - 14: Ii
def o0oOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , I1i , Ii1IiIIIIIiI in IIi :
  o0O0O0o ( ( '[COLORblue]' + OO0O000 + '[/COLOR] [COLORred]Season[/COLOR]-' + I1i + ' [COLORred] Status Unknown[/COLOR] ' ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 61 - 61: I11i / OOooOOo - I1ii11iIi11i
def I1iIIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , I1i , Ii1IiIIIIIiI , oo0oOO00oO in IIi :
  o0O0O0o ( ( '[COLORblue]' + OO0O000 + ' [COLORred] Cancelled On[/COLOR] ' + oo0oOO00oO ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 57 - 57: OOooOOo . iI11I1II1I1I % i1iIi % o0ii1I * OOooOOo
def II1 ( url ) :
 I1 = ( url )
 II1i11I1 = I1 . lower ( )
 if 97 - 97: i1i1I1IIii1II
 if 80 - 80: oOo0O0Ooo . o0ii1I
 Ii1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I1 ) . replace ( ' ' , '+' )
 iii1IIIiiiI = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 OoO00oo00 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 47 - 47: Iii + i1iIi + IIiIiII11i % Ii
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOoOoo00Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( Ii1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1I1IiIi1 = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 17 - 17: Iii / I11i % I1ii11iIi11i
 if 71 - 71: III1iiIii . i1IiiiI1iI . oO0o
 ooO0000o00O = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0Ooo = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 Oo0O0O00Oo = O00O0oOO00O00 ( OOoOoo00Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 10 - 10: o0ii1I + Iii % ii - oOo0O0Ooo
 if O0Ooo != 'Failed' :
  Oooo00oOo = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0Ooo )
  for url , OO0O000 in Oooo00oOo :
   I1i1Ii11i11 = O00O0oOO00O00 ( url )
   Iii1111III111 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i1Ii11i11 )
   for Ii1 , ooo0O0OO in Iii1111III111 :
    if II1i11I1 in ooo0O0OO . lower ( ) :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + Ii1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 70 - 70: oooOo0oo0oo - IiI1i11I
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if ooO0000o00O != 'Failed' :
  iIiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0000o00O )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in iIiii :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 94 - 94: i1iIi * Iii - III1iiIii . iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: i1iIi - oooOo0oo0oo * OOooOOo / i1i1I1IIii1II * IIiIiII11i * oO0o
    if 91 - 91: ii / o0ii1I . oOo0O0Ooo + i1iIi . IIiIiII11i
    if 45 - 45: i1i1I1IIii1II * OOooOOo / iI11I1II1I1I
    if 77 - 77: i1IiiiI1iI - Iii
    if 11 - 11: Ii1I
    if 26 - 26: iI11I1II1I1I * i1IiiiI1iI - oooOo0oo0oo
    if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
    if 55 - 55: i1iIi
    if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
    if 64 - 64: I11i . o0o00Oo0O * o0ii1I + ii - I1ii11iIi11i . ii
    if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
 if Oo0O0O00Oo != 'Failed' :
  o0O0oo0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0O0O00Oo )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in o0O0oo0o :
   if II1i11I1 in OO0O000 . lower ( ) :
    o0O0O0o ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 12 - 12: OOooOOo % III1iiIii % Ii1I . Ii * iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oo0oooo0OoO0o = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , oOo0O , OO0O000 , I1I1 in i1Iii1i1I :
   if II1i11I1 in OO0O000 . lower ( ) :
    if 'season' in I1I1 :
     o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , oOo0O , oOo0O , '' )
    if 'episodes' in I1I1 :
     o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , oOo0O , oOo0O , '' )
  for url in oo0oooo0OoO0o :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 99 - 99: i1iIi / iI11I1II1I1I - o0ii1I * Ii1I % oOo0O0Ooo
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  IIi1I = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
  for url , OO0O000 , oOo0O in IIi1I :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( OO0O000 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , oOo0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 13 - 13: oO0o
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: i1IiiiI1iI + o0o00Oo0O . i1i1I1IIii1II * o0ii1I
    if 2 - 2: ii . oooOo0oo0oo . III1iiIii
    if 42 - 42: oooOo0oo0oo % i1i1I1IIii1II / oO0o - i1i1I1IIii1II * Ii
    if 19 - 19: i1i1I1IIii1II * oOo0O0Ooo % Ii
    if 24 - 24: I11i
    if 10 - 10: I11i % o0ii1I / oooOo0oo0oo
    if 28 - 28: oooOo0oo0oo % i1iIi
    if 48 - 48: Ii % i1i1I1IIii1II
    if 29 - 29: IiI1i11I + Ii % Iii
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OO0O000 in IiIi1I1 :
   if II1i11I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( OoO00oo00 + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 93 - 93: OOooOOo % iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OO0O000 in I1i11 :
   if II1i11I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( Oo0Oo0O + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if I1I1IiIi1 != 'Failed' :
  oOO0o0oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I1IiIi1 )
  for url , I1I , oo0O0 , IiIi1 , OO0O000 in oOO0o0oo0 :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
 iii1IiI1I1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for iiIiIiII in iii1IiI1I1 :
  i1I1 = oO0 + iiIiIiII + oOoOooOo0o0
  o0iIiiIiiIi = O00O0oOO00O00 ( i1I1 )
  if o0iIiiIiiIi != 'Failed' :
   i1iii11 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0iIiiIiiIi )
   for OO0O000 , oo0O0 , url , oOo0O , iI , IiI11i1IIiiI in i1iii11 :
    if II1i11I1 in OO0O000 . lower ( ) :
     ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , url , IiI11i1IIiiI , oOo0O , iI , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 64 - 64: i1iIi / o0o00Oo0O * OOooOOo * i1iIi
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 60 - 60: Iii / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
     if 99 - 99: OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: I11i
def IIiIi11iiIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( ( OO0O000 ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + OoO , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + OoO )
def i11iI11I1I ( url ) :
 Ii1iiIi1I11i = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( Ii1iiIi1I11i )
 sys . exit ( 1 )
 if 89 - 89: i1IiiiI1iI . III1iiIii % I1ii11iIi11i . I1ii11iIi11i - ii
def oo0ooO0O0o ( ) :
 if 75 - 75: IIiIiII11i + oooOo0oo0oo
 if 28 - 28: oOo0O0Ooo
 if 49 - 49: Iii . I11i % i1i1I1IIii1II / o0ii1I
 if 95 - 95: o0o00Oo0O * OOooOOo * III1iiIii . i1iIi / iI11I1II1I1I
 if 28 - 28: III1iiIii + i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oOo0O0Ooo
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * i1i1I1IIii1II * oO0o
 if 35 - 35: Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / i1iIi
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: i1IiiiI1iI
 if 72 - 72: IiI1i11I * oooOo0oo0oo
 o0O0O0o ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 o0O0O0o ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 o0O0O0o ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 67 - 67: ooOoO0O00
def iiioOOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , IIiIii in IIi :
  o0O0O0o ( ( OO0O000 + ' - ' + IIiIii ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 74 - 74: Iii / IIiIiII11i + i1iIi * iI11I1II1I1I - i1IiiiI1iI - oO0o
def OoOoO0OooOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 94 - 94: I11i . oO0o
def oooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  o0O0O0o ( OO0O000 , url , 90054 , oOo0O )
 for url in next :
  o0O0O0o ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 86 - 86: IIiIiII11i + i1iIi + III1iiIii
def I11i11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , IIiIii , url , OO0O000 , oooO00o00 in IIi :
  ii1I ( IIiIii + ' - ' + OO0O000 + ' - ' + oooO00o00 , url , 90044 , oOo0O , oOo0O , '' )
 for oOo0O , OO0O000 , url in i1Iii1i1I :
  o0O0O0o ( OO0O000 , url , 90044 , oOo0O , oOo0O , '' )
 for url in next :
  o0O0O0o ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 9 - 9: oO0o * Iii - o0ii1I
def iIi11i ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 II1i11I1 = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i11I1 )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , I1I1 in IIi :
  if 'season' in I1I1 :
   o0O0O0o ( OO0O000 , OoO , 90054 , oOo0O , oOo0O , '' )
  if 'episodes' in I1I1 :
   o0O0O0o ( OO0O000 , OoO , 90044 , oOo0O , oOo0O , '' )
 for OoO in next :
  o0O0O0o ( 'NEXT' , OoO , 90053 , iiIi1IIiIi + 'Next.png' )
  if 75 - 75: III1iiIii - OOooOOo - iI11I1II1I1I % I11i
def OooooO ( ) :
 if 92 - 92: I11i / I11i * o0ii1I
 if 19 - 19: o0ii1I
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
 if 8 - 8: OOooOOo * I1ii11iIi11i / III1iiIii % o0ii1I - oOo0O0Ooo
 if 71 - 71: IiI1i11I
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . oooOo0oo0oo . o0o00Oo0O % o0ii1I % Ii
 if 11 - 11: o0o00Oo0O - IIiIiII11i . oooOo0oo0oo . o0ii1I % i1IiiiI1iI
 if 21 - 21: I1ii11iIi11i / IiI1i11I . i1IiiiI1iI * ii + Iii - ooOoO0O00
 o0O0O0o ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 o0O0O0o ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 o0O0O0o ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 o0O0O0o ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 58 - 58: Ii1I
def ii1IoO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , IIiIii in IIi :
  if 'genre' in url :
   o0O0O0o ( ( OO0O000 + ' - ' + IIiIii ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 59 - 59: ii * I1ii11iIi11i + ooOoO0O00
def iiii11IiiiiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if 'release' in url :
   o0O0O0o ( OO0O000 , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 98 - 98: IIiIiII11i - ii * o0o00Oo0O
def oo0OoOOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , o0o0OO0o00o0O , url , oo0O0 in IIi :
  ii1I ( OO0O000 + ' ' + o0o0OO0o00o0O , url , 90044 , oOo0O , oOo0O , oo0O0 )
 for oOo0O , OO0O000 , I1I1 , url , IIIIIIi1i , oo0O0 in i1Iii1i1I :
  if 'movies' in I1I1 :
   ii1I ( OO0O000 + ' - ' + IIIIIIi1i , url , 90044 , oOo0O , oOo0O , oo0O0 )
 for url in next :
  o0O0O0o ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
def O0oOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OoOOoO0O0oO ( 'http:' + url )
  if 92 - 92: I1ii11iIi11i / Ii + Ii1I
def OoOOoO0O0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  OO ( ( OO0O000 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def oOo0Oo0O0O ( ) :
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
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 II1i11I1 = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i11I1 )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , O00O in IIi :
  if 'movies' in O00O :
   o0O0O0o ( O00O + '-' + OO0O000 , OoO , 90044 , oOo0O )
 for OoO in next :
  oo0OoOOooO ( OoO )
  if 2 - 2: i1i1I1IIii1II . i1IiiiI1iI * I1ii11iIi11i + o0o00Oo0O - Iii * iI11I1II1I1I
def IiIIIIIi ( ) :
 o0O0O0o ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 80006 , iiIi1IIiIi + 'Desi.png' )
def II111i1ii1iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  OO ( OO0O000 , url , 80007 , oOo0O )
 for url , oOo0O , OO0O000 in IIi :
  o0O0O0o ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def ooo0OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  OooO0OO ( url )
def iiI1111I11i1I ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://www.join4films.com/?s=' + ( I1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 II1i11I1 = ooIII1II1iii1i . lower ( )
 II111i1ii1iII ( II1i11I1 )
 if 85 - 85: oooOo0oo0oo * ooOoO0O00 % oOo0O0Ooo - i1iIi
 if 37 - 37: III1iiIii . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
 if 83 - 83: III1iiIii / i1IiiiI1iI
 if 64 - 64: oO0o % III1iiIii . i1IiiiI1iI % oO0o + Iii * III1iiIii
 if 83 - 83: I11i % i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % i1i1I1IIii1II + o0o00Oo0O / ii
 if 52 - 52: o0ii1I % oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
 if 80 - 80: ii + III1iiIii
 if 95 - 95: i1IiiiI1iI / i1i1I1IIii1II * i1IiiiI1iI - ii * ii % oO0o
 if 43 - 43: I1ii11iIi11i . i1IiiiI1iI
 if 12 - 12: i1IiiiI1iI + oooOo0oo0oo + Iii . III1iiIii / o0ii1I
 if 29 - 29: III1iiIii . i1iIi - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / i1i1I1IIii1II
 if 91 - 91: OOooOOo % iI11I1II1I1I . oOo0O0Ooo
 if 70 - 70: Iii % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / i1IiiiI1iI
 if 100 - 100: Ii1I * Ii % i1i1I1IIii1II / I1ii11iIi11i / i1iIi + Ii1I
 if 59 - 59: i1IiiiI1iI - III1iiIii
def iiiii111 ( ) :
 ii1I ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 93 - 93: i1i1I1IIii1II * o0ii1I
def ii11i1I1iiii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://imoviemax.se/?s=' + ( I1 ) . replace ( ' ' , '+' )
 II1i11I1 = ooIII1II1iii1i . lower ( )
 I11iI1I ( II1i11I1 )
def Iii1iiIi1II1 ( url ) :
 Oo000o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , OO00oo in IIi :
  if OO0O000 in Oo000o :
   pass
  else :
   ii1I ( OO0O000 + ' - ' + OO00oo + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   Oo000o . append ( OO0O000 )
   if 84 - 84: i1iIi + Ii - oooOo0oo0oo * i1iIi
def I1IiiIiii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , i11i in IIi :
  ii1I ( OO0O000 + ' - Views:' + i11i , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 86 - 86: o0ii1I
  if 29 - 29: iI11I1II1I1I - oO0o + oOo0O0Ooo % iI11I1II1I1I % oooOo0oo0oo
def I11iI1I ( url ) :
 O0OOO00 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  ii1I ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  ii1I ( OO0O000 , url , 10075 , oOo0O , oOo0O , '' )
  O0OOO00 . append ( OO0O000 )
  if 62 - 62: Ii + OOooOOo + ooOoO0O00
def oOOoO0O ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for i1IiiiiiIiII , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIIiIi = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIIiIi
  oO0Oo00oo = ( i1IiiiiiIiII ) . replace ( 'play-' , 'Server ' )
  i11I1II1I11i ( oO0Oo00oo , iIIiIi , 10076 , img , img , '' )
  if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
def OOOO0O00Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for iii1IIIiiiI in IIi :
  if '=m' in iii1IIIiiiI :
   IiIIII1iiIIi ( iii1IIIiiiI )
  elif 'php' in iii1IIIiiiI :
   OOOO0O00Ooooo ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( iii1IIIiiiI )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for OoO00oo00 in IIi :
    IiIIII1iiIIi ( iii1IIIiiiI )
    if 17 - 17: Iii
    if 97 - 97: Ii1I * Ii1I / IiI1i11I
    if 6 - 6: i1i1I1IIii1II
def O0OOoOOOO00O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 Ooo0OOO = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0oOO00oO , ooooOoo0OO in Ooo0OOO :
  print 'there ><><><><><><><><><><><><'
  oo0oOO00oO = oo0oOO00oO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooooOoo0OO ) )
  for OO0O000 , Oo0 in IIi :
   print 'here <><><><><><><><><><><><>'
   ii1I ( '[COLORred]' + oo0oOO00oO + '[/COLOR] - ' + OO0O000 + ' - [COLOR' + ooOoOoo0O + ']' + Oo0 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 i1I111Ii1i11 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0oOO00oO , O0000Oo00o in i1I111Ii1i11 :
  print 'there ><><><><><><><><><><><><'
  oo0oOO00oO = oo0oOO00oO
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0000Oo00o ) )
  for OO0O000 , Oo0 in IIi :
   print 'here <><><><><><><><><><><><>'
   ii1I ( '[COLORred]' + oo0oOO00oO + '[/COLOR] - ' + OO0O000 + ' - [COLOR' + ooOoOoo0O + ']' + Oo0 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
   if 89 - 89: IiI1i11I . Ii * o0o00Oo0O
   if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
def iII1111III1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1I111Ii1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1I111Ii1i11 in i1I111Ii1i11 :
  OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
  for OO0O000 in OO0O000 :
   OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I111Ii1i11 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oOOo000oOoO0 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
  for oOOo000oOoO0 in oOOo000oOoO0 :
   oOOo000oOoO0 = 'http:' + oOOo000oOoO0
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , '' , '' )
  if 27 - 27: oooOo0oo0oo
  if 52 - 52: i1IiiiI1iI % OOooOOo + iI11I1II1I1I * i1i1I1IIii1II . o0ii1I
  if 95 - 95: iI11I1II1I1I . III1iiIii - ii * oO0o / I11i
  if 74 - 74: i1i1I1IIii1II
def IiIi1iIIi1 ( url ) :
 if 34 - 34: IiI1i11I
 ii1IIiI1IIi = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iii1IIIiiiI , oOo0O , OO0O000 , o0OO in IIi :
  OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( iii1IIIiiiI )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for o0OoO000O , OOOoO in i1Iii1i1I :
   IIiii11ii1i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOOoO ) )
   for oo0O0 in IIiii11ii1i :
    if OO0O000 in ii1IIiI1IIi :
     pass
    else :
     i11I1II1I11i ( OO0O000 , o0OoO000O , 8043 , oOo0O , oOo0O , oo0O0 )
     iI1i11iII111 ( 'movies' , 'INFO' )
     ii1IIiI1IIi . append ( OO0O000 )
     if 7 - 7: i1i1I1IIii1II - o0o00Oo0O * Iii - I11i - IIiIiII11i
     if 41 - 41: oOo0O0Ooo - i1IiiiI1iI % IIiIiII11i . i1IiiiI1iI - Iii
def i1I111Ii ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , I1I , oo0O0 , iI , OO0O000 in IIi :
  ii1I ( OO0O000 , url , 10065 , I1I , iI , oo0O0 )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 31 - 31: oOo0O0Ooo
def O0oI1ii1Ii1 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'https://www.youtube.com/results?search_query=' + ( I1 ) . replace ( ' ' , '+' )
 II1i11I1 = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i11I1 )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for OoO in next :
  OoO = 'https://www.youtube.com' + OoO
  ii1I ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , OoO , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oOo0O , OoO , OO0O000 , OoOoO , OOOoO in IIi :
  OOO00 . append ( OO0O000 )
  iI1i11iII111 ( 'tvshows' , 'INFO' )
  oOOo000oOoO0 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOo000oOoO0
  OoO = 'http://www.youtube.com' + OoO
  i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , oOOo000oOoO0 , OOOoO )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOo0O , OoO , OO0O000 , OoOoO in IIi :
   print 'im doing it'
   iI1i11iII111 ( 'tvshows' , 'INFO' )
   oOOo000oOoO0 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
   OoO = 'http://www.youtube.com' + OoO
   if '&' in OoO :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( OoO )
    i1I111Ii1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1I111Ii1i11 in i1I111Ii1i11 :
     OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
     for OO0O000 in OO0O000 :
      OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OoO = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I111Ii1i11 ) )
     for OoO in OoO :
      OoO = 'https://www.youtube.com/w' + OoO
     oOOo000oOoO0 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
     for oOOo000oOoO0 in oOOo000oOoO0 :
      oOOo000oOoO0 = 'http:' + oOOo000oOoO0
     i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , Oo00OOOOO , '' )
   elif OO0O000 in OOO00 :
    pass
   elif 'user' in OoO or 'elete' in OO0O000 :
    pass
   elif 'hannel' in OoO :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OoO
    II11iIiIIIiI = OooOoooOo ( OoO )
    iI111I1III = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oOo0O , OoO , OO0O000 in iI111I1III :
     if 'outube' in OoO or 'list' in OoO :
      pass
     elif 'atch' in OoO :
      OoO = ( OoO ) . replace ( '/watch?v=' , '' )
      i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0O , 'http:' + oOo0O , '' )
     else :
      pass
   else :
    i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , oOOo000oOoO0 , '' )
    if 36 - 36: Iii % oooOo0oo0oo
def OoO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  ii1I ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oOo0O , url , OO0O000 , OoOoO , OOOoO in IIi :
  OOO00 . append ( OO0O000 )
  iI1i11iII111 ( 'tvshows' , 'INFO' )
  oOOo000oOoO0 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOo000oOoO0
  url = 'http://www.youtube.com' + url
  i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , oOOo000oOoO0 , OOOoO )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOo0O , url , OO0O000 , OoOoO in IIi :
   iI1i11iII111 ( 'tvshows' , 'INFO' )
   oOOo000oOoO0 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    i1I111Ii1i11 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1I111Ii1i11 in i1I111Ii1i11 :
     OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
     for OO0O000 in OO0O000 :
      OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1I111Ii1i11 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oOOo000oOoO0 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1I111Ii1i11 ) )
     for oOOo000oOoO0 in oOOo000oOoO0 :
      oOOo000oOoO0 = 'http:' + oOOo000oOoO0
     i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , Oo00OOOOO , '' )
   elif OO0O000 in OOO00 :
    pass
   elif 'user' in url or 'elete' in OO0O000 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    iI111I1III = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oOo0O , url , OO0O000 in iI111I1III :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0O , 'http:' + oOo0O , '' )
     else :
      pass
   else :
    i11I1II1I11i ( '[COLORred]' + OoOoO + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 , oOOo000oOoO0 , '' )
    if 37 - 37: Iii
    if 83 - 83: o0o00Oo0O
    if 89 - 89: I1ii11iIi11i + Ii1I - I11i
def iII1I11 ( ) :
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 15 - 15: Iii
def IiiI11I1IIiI ( ) :
 ivuesetup . iVueInt ( )
 if 5 - 5: I1ii11iIi11i
def o0oOo00 ( ) :
 IiI1III ( )
 return
 if 91 - 91: Iii + o0ii1I - OOooOOo - oO0o + III1iiIii
def IiI1III ( ) :
 if 33 - 33: oO0o - I1ii11iIi11i / i1iIi - Iii * i1i1I1IIii1II
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 O00OoOoO = II1I . getSetting ( id = 'User' )
 ooO0o0oo = II1I . getSetting ( id = 'Pass' )
 o0O0OOo0oO = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Iiiii = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 iiI = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 IiiIi = "http://piesustv.net:8000/get.php?username=" + O00OoOoO + "&password=" + ooO0o0oo + "&type=m3u_plus&output=ts"
 i1ii1I = "http://piesustv.net:8000/xmltv.php?username=" + O00OoOoO + "&password=" + ooO0o0oo + "&type=m3u_plus&output=ts"
 if 50 - 50: iI11I1II1I1I + OOooOOo . OOooOOo + ooOoO0O00 + III1iiIii
 xbmc . executeJSONRPC ( o0O0OOo0oO )
 xbmc . executeJSONRPC ( Iiiii )
 xbmc . executeJSONRPC ( iiI )
 if 27 - 27: ooOoO0O00 % o0ii1I - oO0o / i1i1I1IIii1II . i1iIi / I1ii11iIi11i
 OO0OoO0o = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 OO0OoO0o . setSetting ( id = 'm3uUrl' , value = IiiIi )
 OO0OoO0o . setSetting ( id = 'epgUrl' , value = i1ii1I )
 OO0OoO0o . setSetting ( id = 'm3uCache' , value = "false" )
 OO0OoO0o . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def oOO0OOOOOo0Oo ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 40 - 40: iI11I1II1I1I
if 56 - 56: i1i1I1IIii1II + i1iIi
if 32 - 32: IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
def IiI11I111 ( ) :
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
 if OO0o == "insert_username" :
  OO0OOoooo0o = IiIi1Ii ( )
  iiIIiI11II1 = oooOo ( )
  I11 ( 'User' , OO0OOoooo0o )
  I11 ( 'Pass' , iiIIiI11II1 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  oOoO0Oo0 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OO0OOoooo0o , iiIIiI11II1 )
  oOoO0Oo0 = OooOoooOo ( oOoO0Oo0 )
  if oOoO0Oo0 == "" :
   i11i11i = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   iiI1iI = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   Ooo00O0 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , i11i11i , iiI1iI , Ooo00O0 )
   IiI11I111 ( )
  else :
   i11i11i = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   iiI1iI = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   Ooo00O0 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % OO0OOoooo0o )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , i11i11i , iiI1iI , Ooo00O0 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   OoO0OOoO0 ( )
 else :
  OoO0OOoO0 ( )
def IiIi1Ii ( ) :
 iiI11i = xbmc . Keyboard ( '' , 'heading' , True )
 iiI11i . setHeading ( 'Enter Username' )
 iiI11i . setHiddenInput ( False )
 iiI11i . doModal ( )
 if ( iiI11i . isConfirmed ( ) ) :
  o0Oo = iiI11i . getText ( )
  return o0Oo
 else :
  return False
  if 4 - 4: IIiIiII11i
  if 20 - 20: Ii % ii . III1iiIii / Iii
def oooOo ( ) :
 iiI11i = xbmc . Keyboard ( '' , 'heading' , True )
 iiI11i . setHeading ( 'Enter Password' )
 iiI11i . setHiddenInput ( False )
 iiI11i . doModal ( )
 if ( iiI11i . isConfirmed ( ) ) :
  o0Oo = iiI11i . getText ( )
  return o0Oo
 else :
  return False
def Ii11I1i1ii ( ) :
 IiiIi = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  O0000oo00oOOO = urllib2 . urlopen ( IiiIi )
  print O0000oo00oOOO . getcode ( )
  O0000oo00oOOO . close ( )
  if 98 - 98: i1i1I1IIii1II . ii
  pass
  if 54 - 54: o0o00Oo0O / III1iiIii % i1iIi * ooOoO0O00 * o0o00Oo0O
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def OoO0OOoO0 ( ) :
 iii ( )
 if 48 - 48: I11i . i1i1I1IIii1II % OOooOOo - OOooOOo
 if 33 - 33: Iii % IIiIiII11i + oO0o
 ii1I ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 93 - 93: ooOoO0O00 . III1iiIii / oOo0O0Ooo + III1iiIii
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - IiI1i11I . I11i
 if 65 - 65: o0o00Oo0O * Ii . ii / oOo0O0Ooo / IiI1i11I
def o00000oo00 ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 iIII1iIi = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 o000O0oo = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 oOoO0Oo0 = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 oOoO0Oo0 = OooOoooOo ( oOoO0Oo0 )
 if not oOoO0Oo0 == "" :
  OOOOoo00OO0O0Ooo0 = 'https://tinyurl.com/create.php?source=indexpage&url=' + iIII1iIi + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( OOOOoo00OO0O0Ooo0 ) )
  ooOOO00oOOooO = 'https://tinyurl.com/create.php?source=indexpage&url=' + o000O0oo + '&submit=Make+TinyURL%21&alias='
  iIII1iIi = OooOoooOo ( OOOOoo00OO0O0Ooo0 )
  o000O0oo = OooOoooOo ( ooOOO00oOOooO )
  xbmc . log ( str ( o000O0oo ) )
  IiI = Iii1iiI ( iIII1iIi , '<div class="indent"><b>' , '</b>' )
  ii1IiiII = Iii1iiI ( o000O0oo , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % IiI , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % ii1IiiII )
 else :
  return
def IiiI1II1II1i ( ) :
 Ii11I1i1ii ( )
 iIO0OO0o0O00oO ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , o00OoO0o0oOo + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( OoO0O0oo0o )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  ii1I ( ( '[COLORsteelblue]' + OO0O000 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , OoO , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def iIi11I11 ( url ) :
 open = OooOoooOo ( i1ioO + url )
 I11iiI = i1iIii1i111 ( open , '<channel>' , '</channel>' )
 for OOooo000OooO in I11iiI :
  if '<playlist_url>' in open :
   OO0O000 = Iii1iiI ( OOooo000OooO , '<title>' , '</title>' )
   Ii1 = Iii1iiI ( OOooo000OooO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   ii1I ( str ( base64 . b64decode ( OO0O000 ) ) . replace ( '?' , '' ) , Ii1 , 3 , icon , iI , '' )
  else :
   OO0O000 = Iii1iiI ( OOooo000OooO , '<title>' , '</title>' )
   OO0O000 = base64 . b64decode ( OO0O000 )
   o0o0 = Iii1iiI ( OOooo000OooO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = Iii1iiI ( OOooo000OooO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   oo0O0 = Iii1iiI ( OOooo000OooO , '<description>' , '</description>' )
   oo0O0 = base64 . b64decode ( oo0O0 )
   OoOo = Iii1iiI ( oo0O0 , 'PLOT:' , '\n' )
   IiI1 = Iii1iiI ( oo0O0 , 'CAST:' , '\n' )
   iiIiII = Iii1iiI ( oo0O0 , 'RATING:' , '\n' )
   IIiiiI1iI = Iii1iiI ( oo0O0 , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   IIiiiI1iI = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( IIiiiI1iI )
   O0O0O0oO0o0OOOOOO = Iii1iiI ( oo0O0 , 'DURATION_SECS:' , '\n' )
   IiI1i11IiIiii = Iii1iiI ( oo0O0 , 'GENRE:' , '\n' )
   I11iiI1I1 ( str ( OO0O000 ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , o0o0 , iI , OoOo , str ( IIiiiI1iI ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( IiI1 ) . split ( ) , iiIiII , O0O0O0oO0o0OOOOOO , IiI1i11IiIiii )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 65 - 65: IiI1i11I . oOo0O0Ooo
IIi11IIiIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
IiiOoo0o0ooooOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 79 - 79: i1iIi
def iI1111i ( ) :
 IiiIi = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  O0000oo00oOOO = urllib2 . urlopen ( IiiIi )
  print O0000oo00oOOO . getcode ( )
  O0000oo00oOOO . close ( )
  if 39 - 39: i1IiiiI1iI % ii - IIiIiII11i % OOooOOo + i1i1I1IIii1II + o0o00Oo0O
  pass
  if 14 - 14: ii . I11i . Iii
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 50 - 50: i1iIi * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
 OoO = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 i11II ( OoO , IiiOoo0o0ooooOOo + "uide.xml" )
 if 69 - 69: i1IiiiI1iI - ooOoO0O00 % IiI1i11I . oooOo0oo0oo - oooOo0oo0oo
 oooO = open ( IIi11IIiIi1i , 'r+' )
 input = open ( IIi11IIiIi1i ) . read ( ) . decode ( 'UTF-8' )
 o0oO00o = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 oooO . write ( o0oO00o )
 oooO . truncate ( )
 oooO . close ( )
 OOO0OoO0oo0OO ( )
 if 31 - 31: Iii * i1i1I1IIii1II . o0ii1I
def OOO0OoO0oo0OO ( ) :
 open = OooOoooOo ( i1Ii11ii1I )
 all = i1iIii1i111 ( open , '{"num' , 'direct' )
 for OOooo000OooO in all :
  if '"tv_archive":1' in OOooo000OooO :
   OO0O000 = Iii1iiI ( OOooo000OooO , '"epg_channel_id":"' , '"' )
   o0o0 = Iii1iiI ( OOooo000OooO , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = Iii1iiI ( OOooo000OooO , 'stream_id":"' , '"' )
   OO0O000 = OO0O000 . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   ii1I ( OO0O000 , id , 90027 , o0o0 , iI , OO0O000 )
   if 66 - 66: I1ii11iIi11i / ii % i1IiiiI1iI / IiI1i11I + ii
   if 6 - 6: IIiIiII11i % i1IiiiI1iI
def I1iiIiIII ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 o0IiIiI111IIII1 = open ( IIi11IIiIi1i )
 OOOoOooO000oO = ElementTree . parse ( o0IiIiI111IIII1 )
 o0OOOOOo00 = "apples"
 import datetime as dt
 from datetime import time
 oo0oOO = datetime . now ( ) - timedelta ( days = 5 )
 oo0oOO00oO = str ( oo0oOO )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 IIO000oooOO0Oo0 = OOOoOooO000oO . findall ( "programme" )
 for I1iIiIii in IIO000oooOO0Oo0 :
  if name in I1iIiIii . attrib . get ( 'channel' ) :
   OO0 = I1iIiIii . attrib . get ( 'start' )
   I1iiI1iiI1i1 , OOOO00OOO00 , ii1OO0 = OO0 . partition ( ' +' )
   oo0oOO00oO = str ( oo0oOO00oO ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   IIiiiI1iI , Oo , O00 = OO0 . partition ( '2017' )
   OoO00OOoOOOo0 = I1iIiIii . find ( 'title' ) . text + OO0
   O00 = O00 [ : - 6 ]
   if I1iiI1iiI1i1 > oo0oOO00oO :
    if I1iiI1iiI1i1 < I1IIIii :
     oOoO00O = I1iiI1iiI1i1
     oOoO00O = oOoO00O [ : 4 ] + '/' + oOoO00O [ 4 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 4 ] + '-' + I1iiI1iiI1i1 [ 4 : ]
     oOoO00O = oOoO00O [ : 7 ] + '/' + oOoO00O [ 7 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 7 ] + '-' + I1iiI1iiI1i1 [ 7 : ]
     oOoO00O = oOoO00O [ : 10 ] + ' - ' + oOoO00O [ 10 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 10 ] + ':' + I1iiI1iiI1i1 [ 10 : ]
     oOoO00O = oOoO00O [ : 15 ] + ':' + oOoO00O [ 15 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 13 ] + '-' + I1iiI1iiI1i1 [ 13 : ]
     oOoO00O = oOoO00O [ : - 2 ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : - 2 ]
     I11I1I1i1i = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( I1iiI1iiI1i1 ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     o0OOOOOo00 = I11I1I1i1i + str ( I1iiI1iiI1i1 ) + "&duration=240"
     oOoO00O = '[COLOR blue]%s - [/COLOR]' % oOoO00O
     OoO00OOoOOOo0 = str ( oOoO00O ) + I1iIiIii . find ( 'title' ) . text
     oo0O0 = I1iIiIii . find ( 'desc' ) . text
     i11I1II1I11i ( OoO00OOoOOOo0 , I11I1I1i1i , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , oo0O0 )
def Oo0oOO0O00 ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 Oo0000O0OOooO = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 Oo0000O0OOooO . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 Oo0000O0OOooO . setProperty ( 'IsPlayable' , 'true' )
 Oo0000O0OOooO . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0000O0OOooO )
def i11II ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 o00OOo0o0O = time . time ( )
 urllib . urlretrieve ( url , dest , lambda I111Iii1 , i11iO0o0O00o0o , II1IIiiI1 : O00O00 ( I111Iii1 , i11iO0o0O00o0o , II1IIiiI1 , o0oOoO00o , o00OOo0o0O ) )
def O00O00 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  oOooO0OoO = min ( numblocks * blocksize * 100 / filesize , 100 )
  o0oOOOOoo0 = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  ooOO0OOO00o = numblocks * blocksize / ( time . time ( ) - start_time )
  if ooOO0OOO00o > 0 :
   OoOoO0ooooO0 = ( filesize - numblocks * blocksize ) / ooOO0OOO00o
  else :
   OoOoO0ooooO0 = 0
  ooOO0OOO00o = ooOO0OOO00o / 1024
  IIII1ii1 = ooOO0OOO00o / 1024
  OOO0O0OOo = float ( filesize ) / ( 1024 * 1024 )
  Iii1 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( o0oOOOOoo0 )
  II1iI1I11I = '[COLOR white]Speed:  %.02f Mb/s ' % IIII1ii1 + '[/COLOR]'
  dp . update ( oOooO0OoO , Iii1 , II1iI1I11I )
 except :
  oOooO0OoO = 100
  dp . update ( oOooO0OoO )
 if dp . iscanceled ( ) :
  OOoO = xbmcgui . Dialog ( )
  OOoO . ok ( "GenieTv" , 'The download was cancelled.' )
  if 8 - 8: i1IiiiI1iI + oO0o
  sys . exit ( )
  dp . close ( )
  if 9 - 9: oooOo0oo0oo + I11i
def I1iII1IIi1IiI ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iIioo0ooO ( )
  if 97 - 97: i1IiiiI1iI . Iii / oOo0O0Ooo
  if 83 - 83: Iii - Ii1I * i1i1I1IIii1II
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
  if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . Iii
  if 6 - 6: Iii * i1i1I1IIii1II / ii % o0ii1I * I11i
  if 28 - 28: III1iiIii * oOo0O0Ooo % III1iiIii
  if 95 - 95: o0o00Oo0O / Iii . i1IiiiI1iI
  if 17 - 17: Iii
def iIioo0ooO ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for OoO in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def o0OO0OO000OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 O00o0000OO = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IIi1I = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiIi1I1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1i11 = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iiiO00O00O000OOO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOO0o0oo0 = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 I1Io00oOOoO0oO = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 O0Ooo0O0OO = iiI1iiii1Iii ( )
 OoOOOOOoOo0 = iIioOo ( )
 for url in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OO ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in O00o0000OO :
  OO ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IIi1I :
  OO ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1i11 :
  dt = datetime . fromtimestamp ( float ( I1i11 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  OO ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   OO ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OO ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiIi1I1 :
  OO ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iiiO00O00O000OOO :
  OO ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOO0o0oo0 :
  OO ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1Io00oOOoO0oO :
  OO ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + O0Ooo0O0OO , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + OoOOOOOoOo0 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 66 - 66: IIiIiII11i + oO0o
 OO ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 19 - 19: oO0o . ii * oO0o + III1iiIii + ii
def i11iiI ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 oO00o00 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . o0ii1I - oooOo0oo0oo / oOo0O0Ooo
def OoO0ooO ( data ) :
 I1i1i111Ii1I = len ( data ) % 4
 if 64 - 64: Ii . i1iIi
 if 93 - 93: o0o00Oo0O - oO0o . oOo0O0Ooo
 if 64 - 64: OOooOOo + I11i
 if 65 - 65: IIiIiII11i / I1ii11iIi11i
 if 42 - 42: Ii . o0o00Oo0O
 if 75 - 75: i1IiiiI1iI + iI11I1II1I1I
 if I1i1i111Ii1I != 0 :
  data += b'=' * ( 4 - I1i1i111Ii1I )
 return base64 . decodestring ( data )
def Iii1iiI ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : IiiiI1 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : IiiiI1 = ''
 else :
  try : IiiiI1 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : IiiiI1 = ''
 return IiiiI1
 if 34 - 34: o0ii1I + I1ii11iIi11i - ooOoO0O00 - III1iiIii + iI11I1II1I1I
 if 75 - 75: Ii1I
def i1iIii1i111 ( text , start_with , end_with ) :
 IiiiI1 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return IiiiI1
def iiI1iiii1Iii ( ) :
 O00o = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 O00o . connect ( ( '8.8.8.8' , 0 ) )
 O00o = O00o . getsockname ( ) [ 0 ]
 return O00o
 if 55 - 55: i1iIi % Iii / Ii
def iIioOo ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 O0Ooo0O0OO = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O0Ooo0O0OO . group ( ) )
o00OoO0o0oOo = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
i1Ii11ii1I = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
I1111 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
o0oO0OoO0o = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
I11I111i1I1 = '&action=get_live_categories'
iii1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
OoO0O0oo0o = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 88 - 88: Iii + oOo0O0Ooo - Iii / ii - Ii
i1ioO = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
i11Ii1IiIIIi = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
OOOoo00o0o = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
O00o0OO0OO0oo = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 59 - 59: ii % Iii / i1IiiiI1iI + ii . ii
def o0OoooO ( ) :
 Ii11I1i1ii ( )
 open = OooOoooOo ( OOOoo00o0o )
 I11iiI = i1iIii1i111 ( open , '<channel>' , '</channel>' )
 for OOooo000OooO in I11iiI :
  OO0O000 = Iii1iiI ( OOooo000OooO , '<title>' , '</title>' )
  OO0O000 = base64 . b64decode ( OO0O000 )
  Ii1 = Iii1iiI ( OOooo000OooO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ii1I ( '[COLORsteelblue]' + OO0O000 + '[/COLOR]' , Ii1 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 61 - 61: o0o00Oo0O
def IiI11IIi11Iii ( url ) :
 open = OooOoooOo ( O00o0OO0OO0oo + url )
 I11iiI = i1iIii1i111 ( open , '<channel>' , '</channel>' )
 for OOooo000OooO in I11iiI :
  OO0O000 = Iii1iiI ( OOooo000OooO , '<title>' , '</title>' )
  OO0O000 = base64 . b64decode ( OO0O000 )
  xbmc . log ( str ( OO0O000 ) )
  o0o0 = Iii1iiI ( OOooo000OooO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  Ii1 = Iii1iiI ( OOooo000OooO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oo0O0 = Iii1iiI ( OOooo000OooO , '<description>' , '</description>' )
  oo0O0 = base64 . b64decode ( oo0O0 )
  ii11i1I1i = '('
  Iiiii1I = ')'
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , Ii1 , 222 , o0o0 , iI , ( '[COLOR' + ooOoOoo0O + ']' + oo0O0 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( Iiiii1I , '[COLORsteelblue]' ) . replace ( ii11i1I1i , '[COLORorangered]' ) )
  if 13 - 13: IIiIiII11i . IiI1i11I - i1IiiiI1iI . oO0o . iI11I1II1I1I
def oO00oooo0OOo ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( iii1 + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , type , iii1IIIiiiI , iIOo0O in IIi :
  OoO00oo00 = ( o0oO0OoO0o + iii1IIIiiiI + '.m3u8' ) . strip ( )
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO00oo00 , 222 , ( iIOo0O ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
def OOoOO0o0o0Oo ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooo0O0OO , O00oo0oOoO00O in IIi :
  if name == ooo0O0OO :
   i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + O00oo0oOoO00O , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def Iii1iIiI1I1I1 ( name ) :
 oOOO0OO = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , oOo0O , OoO in IIi :
  OoO = ( OoO ) . replace ( '.ts' , '.m3u8' )
  i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( OoO ) . strip ( ) , 222 , oOo0O , oOo0O , '' )
 else :
  i11I1II1I11i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 43 - 43: Iii % ooOoO0O00 % i1iIi . Ii
  if 56 - 56: o0o00Oo0O * IiI1i11I + IiI1i11I * iI11I1II1I1I / i1iIi * i1IiiiI1iI
  if 25 - 25: iI11I1II1I1I . Iii * Ii + I1ii11iIi11i * Iii
  if 67 - 67: IiI1i11I
  if 88 - 88: I1ii11iIi11i
  if 8 - 8: Ii1I
  if 82 - 82: ii
  if 75 - 75: IIiIiII11i % oOo0O0Ooo + oooOo0oo0oo % ii / III1iiIii
  if 4 - 4: Ii - oooOo0oo0oo % Ii1I * i1IiiiI1iI % I11i
  if 71 - 71: i1iIi . i1iIi - iI11I1II1I1I
  if 22 - 22: ii / Ii1I % IiI1i11I * OOooOOo
  if 32 - 32: ii % i1i1I1IIii1II % iI11I1II1I1I / o0o00Oo0O
def iiIiii1iI1i ( ) :
 ii1I ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  ii1I ( 'Backup Genie Favourites' , OoO , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  ii1I ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  ii1I ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 61 - 61: IIiIiII11i . o0o00Oo0O - o0ii1I - Ii1I / Ii - IIiIiII11i
  if 98 - 98: o0ii1I - oOo0O0Ooo . Ii * I1ii11iIi11i
  if 29 - 29: o0ii1I / i1iIi % Iii
zip = oo00 . getSetting ( 'zip' )
ii1iIII1ii = xbmc . translatePath ( os . path . join ( zip ) )
def I11Oo0O0O0O0OO ( ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 86 - 86: o0ii1I * ooOoO0O00 + i1i1I1IIii1II
  if 8 - 8: i1i1I1IIii1II
  if 50 - 50: III1iiIii . i1iIi - o0o00Oo0O % oOo0O0Ooo . i1IiiiI1iI
def iii1iI ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  I11Oo0O0O0O0OO ( )
  IiiIi1I11 = open ( url ) . read ( )
  i1I1Ii11II1i = os . path . join ( ii1iIII1ii , description . split ( 'Your ' ) [ 1 ] )
  oooO = open ( i1I1Ii11II1i , mode = 'w' )
  oooO . write ( IiiIi1I11 )
  oooO . close ( )
 else :
  if 'guisettings.xml' in description :
   OOooo000OooO = open ( os . path . join ( ii1iIII1ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiiiI1 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( IiiiI1 ) . findall ( OOooo000OooO )
   for type , oooOoOOoOO0O , I11iii1I1Iiii in IIi :
    I11iii1I1Iiii = I11iii1I1Iiii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oooOoOOoOO0O , I11iii1I1Iiii ) )
  else :
   i1I1Ii11II1i = os . path . join ( url )
   IiiIi1I11 = open ( os . path . join ( ii1iIII1ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooO = open ( i1I1Ii11II1i , mode = 'w' )
   oooO . write ( IiiIi1I11 )
   oooO . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
 if 48 - 48: III1iiIii
 if 96 - 96: i1i1I1IIii1II / o0o00Oo0O . IIiIiII11i + III1iiIii % I11i
 if 67 - 67: o0o00Oo0O % i1IiiiI1iI
def III ( ) :
 I1Io0 = 1
 I11Oo0O0O0O0OO ( )
 oOo0000ooO = xbmc . translatePath ( os . path . join ( ii1iIII1ii , 'Build Backup' , 'Full Backup' , '' ) )
 I1Io0oO0oo = xbmc . translatePath ( os . path . join ( ii1iIII1ii , 'Build Backup' , 'my_full_backup.zip' ) )
 ooOO00Oo = xbmc . translatePath ( os . path . join ( ii1iIII1ii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOo0000ooO ) :
  os . makedirs ( oOo0000ooO )
 oO00OOOOOO0o = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oO00OOOOOO0o ) : return False , 0
 iIII = oO00OOOOOO0o
 OoO0000 = xbmc . translatePath ( os . path . join ( oOo0000ooO , iIII + '.zip' ) )
 III11iIIi = [ 'plugin.video.GenieTv' ]
 iIIii1I111iIii1i1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0Ooi1II11i1iI1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OO0IIi1II11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0ooOOOo = "Creating full backup of existing build"
 OOoOOo0oO = "Creating Community Build"
 I1Ii1IIIiII = "Archiving..."
 iiII1IIii1i1 = ""
 i1iiiIIi11II = "Please Wait"
 o0oooOo0oo ( oOo0oooo00o , OoO0000 , OOoOOo0oO , I1Ii1IIIiII , iiII1IIii1i1 , i1iiiIIi11II , o0Ooi1II11i1iI1 , OO0IIi1II11 )
 time . sleep ( 1 )
 i1iI1IIi1I = xbmc . translatePath ( os . path . join ( oOo0000ooO , iIII + '_guisettings.zip' ) )
 oo00i1i11I1I1 = zipfile . ZipFile ( i1iI1IIi1I , mode = 'w' )
 try :
  oo00i1i11I1I1 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oo00i1i11I1I1 . close ( )
 if I1Io0 == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1Io0oO0oo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OoO0000 + '[/COLOR]' )
  if 82 - 82: oO0o - I1ii11iIi11i - o0o00Oo0O - ii
def o0oooOo0oo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Ii1I1Iiii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oOIii = len ( sourcefile )
 i1IIIIiiI11 = [ ]
 I1iii1I = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for oooII111 , I11iIi , Ii1IIiII1I in os . walk ( sourcefile ) :
  for file in Ii1IIiII1I :
   I1iii1I . append ( file )
 OOOii = len ( I1iii1I )
 for oooII111 , I11iIi , Ii1IIiII1I in os . walk ( sourcefile ) :
  I11iIi [ : ] = [ Iii1I11 for Iii1I11 in I11iIi if Iii1I11 not in exclude_dirs ]
  Ii1IIiII1I [ : ] = [ oooO for oooO in Ii1IIiII1I if oooO not in exclude_files ]
  for file in Ii1IIiII1I :
   i1IIIIiiI11 . append ( file )
   O0o0o = len ( i1IIIIiiI11 ) / float ( OOOii ) * 100
   o0oOoO00o . update ( int ( O0o0o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IiiiIi1111I = os . path . join ( oooII111 , file )
   if not 'temp' in I11iIi :
    if not 'plugin.program.originwizard' in I11iIi :
     import time
     iII1i1ii = '01/01/1980'
     i1I1ii1i = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IiiiIi1111I ) ) )
     if i1I1ii1i > iII1i1ii :
      Ii1I1Iiii . write ( IiiiIi1111I , IiiiIi1111I [ oOIii : ] )
 Ii1I1Iiii . close ( )
 o0oOoO00o . close ( )
 if 2 - 2: ii % iI11I1II1I1I
 if 21 - 21: III1iiIii - oOo0O0Ooo % ii + I11i
def o00O0o ( ) :
 iii ( )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 28 - 28: oOo0O0Ooo
 if 87 - 87: III1iiIii . ooOoO0O00 % ii * Ii
def o0oOo ( ) :
 iii ( )
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  oOOO00o000o ( )
 if I111I1Iiii1i == 1 :
  i1i1iII1 ( )
 if I111I1Iiii1i == 2 :
  O0OO0O ( )
 if I111I1Iiii1i == 3 :
  O0oI1ii1Ii1 ( )
  if 51 - 51: IIiIiII11i . i1i1I1IIii1II . oO0o % IIiIiII11i
  if 41 - 41: OOooOOo - oooOo0oo0oo + i1iIi - ooOoO0O00
  if 6 - 6: IIiIiII11i
  if 7 - 7: ooOoO0O00
  if 63 - 63: iI11I1II1I1I + III1iiIii % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
  if 60 - 60: I11i . OOooOOo % i1IiiiI1iI / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / oooOo0oo0oo . Ii1I * i1iIi
  if 59 - 59: iI11I1II1I1I / Ii1I % i1iIi
  if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % Iii
def oOoO000 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   oooo ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if I111I1Iiii1i == 1 :
   oooo ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if I111I1Iiii1i == 2 :
   Oo00o00Oo ( )
  if I111I1Iiii1i == 3 :
   i1I1i1I111 ( )
  if I111I1Iiii1i == 4 :
   oOo00OO0ooOOO ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if I111I1Iiii1i == 5 :
   i1i1I1Ii1IIii ( )
  if I111I1Iiii1i == 6 :
   oooOOoo ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if I111I1Iiii1i == 7 :
   iI1iii1iIiiI ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if I111I1Iiii1i == 8 :
   II1iiiiI1 ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if I111I1Iiii1i == 9 :
   IiiIiiIIII ( )
  if I111I1Iiii1i == 10 :
   oOo ( )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Quicksilver.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 1030 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , iiIi1IIiIi + 'KodibleAudioBooks.png' , Oo00OOOOO , '' )
  if 94 - 94: oO0o + oO0o + Ii1I . oO0o * o0ii1I
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 62 - 62: I11i / iI11I1II1I1I
def O0OOo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   Ooo0OOo ( )
  if I111I1Iiii1i == 1 :
   o0OO0 ( )
  if I111I1Iiii1i == 2 :
   oOo0OOoO0 ( )
  if I111I1Iiii1i == 3 :
   ii111 ( OoO )
  if I111I1Iiii1i == 4 :
   i1I ( OoO )
  if I111I1Iiii1i == 5 :
   Ooo0OOoOoO0 ( )
  if I111I1Iiii1i == 6 :
   Iii1iI1iiIii ( url = 'http://www.iplocation.net/' , inc = 1 )
  if I111I1Iiii1i == 7 :
   iIiiI111I11 ( )
 else :
  i11I1II1I11i ( 'CLLEANUP' , 'url' , 9666 , iiIi1IIiIi + 'MAIN5.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '' , 80000 , iiIi1IIiIi + 'KillKodi.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiIi1IIiIi + 'Speedtest.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiIi1IIiIi + 'View-Log-File.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( 'DELETE CACHE' , 'url' , 14 , iiIi1IIiIi + 'DeleteCache.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( 'DELETE PACKAGES' , 'url' , 6 , iiIi1IIiIi + 'DeletePackages.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( 'FORCE REFRESH' , 'url' , 10 , iiIi1IIiIi + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
  ii1I ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , iiIi1IIiIi + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
  i11I1II1I11i ( 'CHECK MY IP' , 'url' , 12 , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
  i11I1II1I11i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iiIi1IIiIi + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 86 - 86: i1i1I1IIii1II + IiI1i11I / ii - Iii
  if 55 - 55: oooOo0oo0oo / OOooOOo * oooOo0oo0oo
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 40 - 40: oO0o . Ii + Ii1I + oOo0O0Ooo . i1i1I1IIii1II
 if 90 - 90: i1IiiiI1iI . OOooOOo * IIiIiII11i % i1iIi
def i1i1II ( ) :
 iii ( )
 ii1I ( '[COLOR' + ooOoOoo0O + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iiIi1IIiIi + 'repos.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']NEW[/COLOR]' , str ( oO0000OOo00 ) , 22 , iiIi1IIiIi + 'NEW.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']IPTV[/COLOR]' , str ( oO0000OOo00 ) , 23 , iiIi1IIiIi + 'IPTV.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']VIDEO[/COLOR]' , str ( oO0000OOo00 ) , 24 , iiIi1IIiIi + 'VIDEO.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SPORTS[/COLOR]' , str ( oO0000OOo00 ) , 25 , iiIi1IIiIi + 'SPORTS.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 26 , iiIi1IIiIi + 'KIDS.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 27 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']PROGRAMS[/COLOR]' , str ( oO0000OOo00 ) , 28 , iiIi1IIiIi + 'PROGRAMS.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']XXX[/COLOR]' , 'URL' , 29 , iiIi1IIiIi + 'XXX.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 36 - 36: oOo0O0Ooo - I1ii11iIi11i % oooOo0oo0oo . Iii + Iii + o0ii1I
 if 28 - 28: I1ii11iIi11i / i1i1I1IIii1II * OOooOOo + Ii1I - i1IiiiI1iI
def Oo0Ii1iii ( ) :
 iii ( )
 i11I1II1I11i ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi % Iii % ooOoO0O00
def I1ii1ii11i1I ( ) :
 iii ( )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 90 - 90: o0ii1I * oO0o
def I1iO0o0O0OooOoo ( ) :
 iii ( )
 i11I1II1I11i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 17 - 17: ii % i1i1I1IIii1II - ooOoO0O00 % III1iiIii % I1ii11iIi11i
 if 41 - 41: ii . i1IiiiI1iI % OOooOOo - IiI1i11I
 if 58 - 58: i1i1I1IIii1II + iI11I1II1I1I - o0o00Oo0O
def iiooO ( ) :
 iii ( )
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  i1i1i11iI11II ( )
 if I111I1Iiii1i == 0 :
  II1iiI1iI ( OoO )
 if I111I1Iiii1i == 0 :
  O0oo0000o ( OoO )
  if 99 - 99: i1i1I1IIii1II - Ii1I . IIiIiII11i * Ii . oooOo0oo0oo - oO0o
  if 31 - 31: Ii * o0ii1I . I11i % oooOo0oo0oo * Ii1I % o0o00Oo0O
  if 77 - 77: oO0o + oO0o . i1iIi * ii + oO0o
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 6 - 6: ooOoO0O00 - Iii
def O0o00ooo ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for oOo0O , OO0O000 in IIi :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0O , oOo0O , '' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 5 - 5: ooOoO0O00 - i1i1I1IIii1II / OOooOOo
def iII1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( o00oOOo0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 5 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 91 - 91: IIiIiII11i - iI11I1II1I1I / ooOoO0O00 * ooOoO0O00 % I1ii11iIi11i
def i1i1i11iI11II ( ) :
 iii ( )
 ii1I ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 82 - 82: i1iIi
def OoOooO0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1IiiiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 31 - 31: Ii + III1iiIii - i1IiiiI1iI * IiI1i11I
def O0OO00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + i1111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 58 - 58: ii - Iii + iI11I1II1I1I * Ii
def OoOiII11IiIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iII1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 6 - 6: i1i1I1IIii1II / o0o00Oo0O / o0ii1I / III1iiIii / i1i1I1IIii1II . iI11I1II1I1I
def oo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 87 - 87: Iii . Iii . IIiIiII11i / oooOo0oo0oo
def II1iiI1iI ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOOoOOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 40 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 42 - 42: iI11I1II1I1I * o0ii1I / oO0o + oooOo0oo0oo
def Iii11iI1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOo0o0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 5 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 8 - 8: i1IiiiI1iI
def oOOoo00O00o ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  III11IiI ( )
 if I111I1Iiii1i == 1 :
  o0ooo ( )
 if I111I1Iiii1i == 2 :
  o0oo00O ( )
  if 36 - 36: oooOo0oo0oo * oO0o - Ii1I + IiI1i11I
  if 13 - 13: oO0o % iI11I1II1I1I - IIiIiII11i / oOo0O0Ooo
  if 9 - 9: Ii1I * o0ii1I - III1iiIii
  if 88 - 88: iI11I1II1I1I
def o0ooo ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , I1iiI11i111II in IIi :
  o0O0O0o ( 'Android Apps' + I1iiI11i111II , 'https://www.apkfiles.com' + OoO , 30035 , iiIi1IIiIi + 'apps.png' )
 for OoO , I1iiI11i111II in i1Iii1i1I :
  o0O0O0o ( 'Android Games' + I1iiI11i111II , 'https://www.apkfiles.com' + OoO , 30035 , iiIi1IIiIi + 'GAMES.png' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def O00Oo0OOOO0oOoo0 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '/cat' in url :
   o0O0O0o ( ( OO0O000 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def O0OIIII1i ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '/app' in url :
   o0O0O0o ( ( OO0O000 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def i1I1Iiii ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 Ii1 = url
 if "page=" in str ( url ) :
  Ii1 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  if 'apk' in url :
   i11I1II1I11i ( ( OO0O000 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0O )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 i11I1II1I11i ( 'Next Page' , Ii1 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def I1iIIIiiii ( name , url ) :
 oO00ooooO0o = ooO000 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( oO00ooooO0o )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  I1111o00o ( name , url , 'Brackets' )
def o0oo00O ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'https://www.apkfiles.com/search?q=' + ( I1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 II1i11I1 = ooIII1II1iii1i . lower ( )
 i1I1Iiii ( II1i11I1 )
 if 91 - 91: o0ii1I - IiI1i11I . ooOoO0O00 . Ii1I * I11i % IiI1i11I
def i1IIi111iI ( url ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( IiIiII11i1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 OooooOOoo0 = os . path . join ( ii1I1 , OO0O000 + '.apk' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 44 - 44: oOo0O0Ooo % oooOo0oo0oo * Ii * Ii - I1ii11iIi11i . i1IiiiI1iI
def o00i111iiIiiIiI ( url ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 OooooOOoo0 = os . path . join ( ii1I1 , OO0O000 + '.mp4' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 59 - 59: oooOo0oo0oo + oOo0O0Ooo / IIiIiII11i / OOooOOo
 if 80 - 80: OOooOOo + iI11I1II1I1I . III1iiIii
def ooOoOoo000O0O ( name , url , description ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 OooooOOoo0 = os . path . join ( ii1I1 , name )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 iI11i = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iI11i
 print '======================================='
 extract . all ( OooooOOoo0 , iI11i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 78 - 78: I1ii11iIi11i / oO0o
 if 40 - 40: Iii / IiI1i11I + oO0o / ii - i1i1I1IIii1II / i1IiiiI1iI
 if 62 - 62: Ii - Iii
 if 81 - 81: Iii
 if 92 - 92: oooOo0oo0oo - I1ii11iIi11i - ii / III1iiIii - ooOoO0O00
def III11IiI ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , OoO , iIOo0O , iI , Oo00o in IIi :
  i11I1II1I11i ( OO0O000 , OoO , 80003 , iIOo0O , iiIi1IIiIi + 'APKToolsB.png' , Oo00o )
def IIIi1ii ( apk , ret = None ) :
 if apk == "kodi" :
  Ii1iii11I = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( Ii1iii11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   Ii11iIiiI = IIi [ 0 ] [ 0 ]
   iIII = IIi [ 0 ] [ 1 ]
   iiII = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( Ii11iIiiI , iIII )
  if ret == 'version' : return Ii11iIiiI
  else : return iiII
 elif apk == "spmc" :
  iII1IiiIIIIii = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( iII1IiiIIIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  Ii11iIiiI = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  iiII = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( Ii11iIiiI , Ii11iIiiI )
  if ret == 'version' : return Ii11iIiiI
  else : return iiII
def I1111o00o ( name , url , Brackets ) :
 if OooOoOO0 ( ) == 'android' :
  oOOO = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not oOOO : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iiiIIi = name
  if oOOO :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OOooo0O0o0 ( url ) == True : Iii1IiiII1Ii1 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiiIIi , '' , 'Please Wait' )
   OooooOOoo0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( OooooOOoo0 )
   except : pass
   downloader . download ( url , OooooOOoo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oo00i1i11I1I1 = zipfile . ZipFile ( OooooOOoo0 )
    for file in oo00i1i11I1I1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as oooO :
       OOoOo0O00oo = file . split ( '/' ) [ 1 ]
       oooO . write ( oo00i1i11I1I1 . read ( file ) )
       xbmc . sleep ( 500 )
       oooO . close ( )
       try :
        os . remove ( OooooOOoo0 )
       except :
        pass
       OooooOOoo0 = os . path . join ( i1iIIi1 , OOoOo0O00oo )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + OooooOOoo0 + '")' )
  else : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 70 - 70: ii % ii % oO0o
 if 98 - 98: oO0o
 if 18 - 18: Iii + I1ii11iIi11i - oO0o / i1IiiiI1iI / oooOo0oo0oo
 if 53 - 53: oooOo0oo0oo + I11i . i1i1I1IIii1II / Iii
def o0000oO ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for OoO , OO0O000 in IIi :
  OoO = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + OoO )
  ooo0oo ( ( OO0O000 ) . replace ( '_' , ' ' ) , OoO )
  if 70 - 70: o0o00Oo0O / ii + Ii1I + ooOoO0O00
def ooo0oo ( name , url ) :
 if OooOoOO0 ( ) == 'android' :
  oOOO = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not oOOO : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iiiIIi = name
  if oOOO :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OOooo0O0o0 ( url ) == True : Iii1IiiII1Ii1 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iiiIIi , '' , 'Please Wait' )
   OooooOOoo0 = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( OooooOOoo0 )
   except : pass
   downloader . download ( url , OooooOOoo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + OooooOOoo0 + '")' )
  else : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Iii1IiiII1Ii1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 63 - 63: IiI1i11I / Ii1I * i1i1I1IIii1II / IIiIiII11i + oooOo0oo0oo - o0o00Oo0O
 if 16 - 16: IIiIiII11i / o0ii1I . o0ii1I - o0ii1I / Ii1I
def I1Ii11i1ii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 5 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 90 - 90: I11i
 if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
def oOoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 30015 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 32 - 32: III1iiIii - i1iIi * IiI1i11I * Iii
def O00OOOo ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 iIIiIi = url
 oOo0O = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iii1IIIiiiI , OO0O000 in IIi :
  if '.mp4' in OO0O000 :
   i11I1II1I11i ( 'Watch VIDEO' , url + '/' + iii1IIIiiiI , 222 , oOo0O , fanart , '' )
  if 'description' in OO0O000 :
   i11I1II1I11i ( 'Read Description' , url + '/' + iii1IIIiiiI , 30017 , oOo0O , fanart , '' )
  if 'images' in OO0O000 :
   ii1I ( 'View Images' , url + '/' + iii1IIIiiiI , 30018 , oOo0O , fanart , '' )
  if 'url' in OO0O000 :
   i11I1II1I11i ( 'Install Build On Android' , url + '/' + iii1IIIiiiI , 30016 , oOo0O , fanart , '' )
  if 'url' in OO0O000 :
   i11I1II1I11i ( 'Install Build On Pc' , url + '/' + iii1IIIiiiI , 30019 , oOo0O , fanart , '' )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 37 - 37: Iii % Ii1I / i1iIi
def o0oO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  ooOo0 ( url )
  if 61 - 61: IIiIiII11i
def iiI11111II ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  I1ii1i11iI1 ( url )
  if 6 - 6: o0o00Oo0O . i1iIi - i1i1I1IIii1II / Ii
def O00O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o0Oo in IIi :
  o0OIiII ( 'Description:' , o0Oo )
  if 52 - 52: IiI1i11I + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
def o0ooOOO0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iii1IIIiiiI , OO0O000 in IIi :
  if 'png' in OO0O000 :
   i11I1II1I11i ( 'image' , '' , '' , url + '/' + iii1IIIiiiI , url + '/' + iii1IIIiiiI , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 12 - 12: Iii
def I11iIi1i1I1i1 ( name , url , description ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , name + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOoOoO0 ( )
 if 14 - 14: Iii
 if 18 - 18: oOo0O0Ooo
def I1ii1i11iI1 ( url ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iiI11ii1I1 ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOo ( )
 if 23 - 23: ii * IIiIiII11i
def ooOo0 ( url ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iiI11ii1I1 ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOo ( )
 if 70 - 70: Ii1I + oOo0O0Ooo
def o0o0OOo0O ( name , url , description ) :
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OooooOOoo0 = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ooo0OOo ( )
 if 82 - 82: oooOo0oo0oo / IiI1i11I - o0o00Oo0O % IIiIiII11i % OOooOOo
def OooOoOO0 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def IIo0Oo0oO0oOO00 ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : oooO = open ( oO , 'w' ) ; oooO . close ( )
 with open ( oO , 'a' ) as oooO :
  iiiIIIIi1 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooO . write ( iiiIIIIi1 . rstrip ( '\r\n' ) + '\n' )
def Ooo0OOo ( ) :
 I111I1Iiii1i = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if I111I1Iiii1i == 0 : return
 elif I111I1Iiii1i == 1 : pass
 iIIIiIi = OooOoOO0 ( )
 IIo0Oo0oO0oOO00 ( "Platform: " + str ( iIIIiIi ) )
 os . _exit ( 1 )
 IIo0Oo0oO0oOO00 ( "Force close failed!  Trying alternate methods." )
 if iIIIiIi == 'osx' :
  IIo0Oo0oO0oOO00 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIIIiIi == 'linux' :
  IIo0Oo0oO0oOO00 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIIIiIi == 'android' :
  IIo0Oo0oO0oOO00 ( "############ try android force close #################" )
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
 elif iIIIiIi == 'windows' :
  IIo0Oo0oO0oOO00 ( "############ try windows force close #################" )
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
  IIo0Oo0oO0oOO00 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  IIo0Oo0oO0oOO00 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 63 - 63: oO0o . i1i1I1IIii1II + i1IiiiI1iI . OOooOOo / Ii / IiI1i11I
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + oooOo0oo0oo
  if 31 - 31: o0ii1I * I11i * o0ii1I + oO0o * I11i . i1IiiiI1iI
def O0oo0000o ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( url ) :
  for file in Ii1IIiII1I :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OOooo000OooO = open ( ( os . path . join ( Oo00oo00o00Oo , file ) ) ) . read ( )
    iiiiiii11III = OOooo000OooO . replace ( oOo0oooo00o , 'special://home/' )
    oooO = open ( ( os . path . join ( Oo00oo00o00Oo , file ) ) , mode = 'w' )
    oooO . write ( str ( iiiiiii11III ) )
    oooO . close ( )
 Ooo0OOo ( )
 if 48 - 48: i1IiiiI1iI % IiI1i11I % o0ii1I % iI11I1II1I1I . o0ii1I
def Oo00o00Oo ( ) :
 o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 14 - 14: IiI1i11I * oO0o % o0o00Oo0O + Iii + Ii1I
def III1I11Iiii ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def iIiI1i1Ii ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def Oo0o00o ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in i1Iii1i1I :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , oOo0O , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0O )
def III1I1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooO0OO ( url )
def iI1IIIIII ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1
 OO0oO0Oo = 'https://www.radionomy.com/en/search/index?query=' + ( I1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( OO0oO0Oo )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OoO , 70005 , oOo0O )
  if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + oooOo0oo0oo * IIiIiII11i
  if 34 - 34: I11i % ii
def i1i1I1Ii1IIii ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.listenlive.eu/' + OoO , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def oOo00OO0ooOOO ( url ) :
 oO00ooooO0o = ooO000 ( url )
 if 36 - 36: oOo0O0Ooo
 if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Iii
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , o00o0 , url , OOoOo0O0 in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' [COLORorangered] ' + OOoOo0O0 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[CR]' + o00o0 + '[CR]' + OOoOo0O0 + '[/COLOR]' )
  if 39 - 39: i1IiiiI1iI . oO0o % i1iIi . oooOo0oo0oo / IiI1i11I * oO0o
def iiI1i ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.toonjet.com/' + OoO , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00o0 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( oO00ooooO0o )
 for url , oOo0O in IIi :
  if 'ol.gif' in oOo0O :
   pass
  elif 'link_block_' in oOo0O :
   pass
  elif '.png' in oOo0O :
   pass
  else :
   o0O0O0o ( ( oOo0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  o0O0O0o ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOoOooO0o ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 23 - 23: oOo0O0Ooo
  if 7 - 7: IiI1i11I % Ii1I
def oOo ( ) :
 iIO0OO0o0O00oO ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 iIO0OO0o0O00oO ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 64 - 64: i1IiiiI1iI + Ii
def iI1i11i ( ) :
 iIO0OO0o0O00oO ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIO0OO0o0O00oO ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 iIO0OO0o0O00oO ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 4 - 4: i1i1I1IIii1II * oOo0O0Ooo - i1iIi / IIiIiII11i + oooOo0oo0oo / Ii
def oO0o0O ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , iiI1ii1Iii11I in IIi :
  if 'Parent' in OO0O000 :
   pass
  elif '2' in iiI1ii1Iii11I :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 41 - 41: Ii1I + I1ii11iIi11i / III1iiIii . o0ii1I * oOo0O0Ooo
def oOO0O0ooOOOo ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , iiI1ii1Iii11I in IIi :
  if I1 in OO0O000 . lower ( ) :
   if '1' in iiI1ii1Iii11I :
    iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in iiI1ii1Iii11I :
    iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in iiI1ii1Iii11I :
    iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 91 - 91: i1iIi - i1i1I1IIii1II + i1i1I1IIii1II
    if 14 - 14: Ii1I * i1IiiiI1iI % ooOoO0O00 / Ii1I
def i11II1 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , iiI1ii1Iii11I in IIi :
  if '1' in iiI1ii1Iii11I :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in iiI1ii1Iii11I :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in iiI1ii1Iii11I :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: i1IiiiI1iI * oOo0O0Ooo
def IIiI ( url ) :
 iii1IIIiiiI = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in i1Iii1i1I :
  if 'mp3' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in OO0O000 :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iii1IIIiiiI + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 99 - 99: I11i * i1i1I1IIii1II . i1IiiiI1iI / OOooOOo . i1iIi
   if 1 - 1: oooOo0oo0oo
   if 87 - 87: o0o00Oo0O * IIiIiII11i + iI11I1II1I1I % i1i1I1IIii1II % Ii - OOooOOo
def o00O0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iii1IIIiiiI = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if 'Parent' in OO0O000 :
   pass
  elif '.db' in OO0O000 :
   pass
  elif '.jpg' in OO0O000 :
   pass
  elif '.html' in OO0O000 :
   pass
  elif '.doc' in OO0O000 :
   pass
  elif 'mp3' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iii1IIIiiiI + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 65 - 65: iI11I1II1I1I . IiI1i11I / o0ii1I
   if 12 - 12: oOo0O0Ooo + i1IiiiI1iI
def oOooooO ( ) :
 iIO0OO0o0O00oO ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIO0OO0o0O00oO ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIO0OO0o0O00oO ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OoO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0O :
   pass
  else :
   iIO0OO0o0O00oO ( oOo0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OoO ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0O + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 64 - 64: ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: Iii / i1iIi % i1i1I1IIii1II + ii
 if 35 - 35: III1iiIii
def iIiIi1i1Iiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if '</a>' in OO0O000 :
   pass
  elif '(' in OO0O000 :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 78 - 78: I1ii11iIi11i - i1IiiiI1iI + IiI1i11I * o0ii1I * I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: I1ii11iIi11i - o0o00Oo0O
def iI111iIi ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if I1 in OO0O000 . lower ( ) :
   if '</a>' in OO0O000 :
    pass
   elif '(' in OO0O000 :
    iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 26 - 26: oooOo0oo0oo % oooOo0oo0oo / Ii + Ii1I - o0o00Oo0O
    if 20 - 20: i1IiiiI1iI . o0o00Oo0O - Ii1I / OOooOOo - I11i
def oooooOoOO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if '</a>' in OO0O000 :
   pass
  elif '(' in OO0O000 :
   iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 59 - 59: III1iiIii . ii % i1i1I1IIii1II % Ii + i1i1I1IIii1II % OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: i1iIi - III1iiIii / IIiIiII11i / Ii1I
 if 31 - 31: i1IiiiI1iI * oOo0O0Ooo + i1iIi
def iIIIIi11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iii1IIIiiiI = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iii1IIIiiiI )
  if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
def Oo0Oo00O00o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  if '<p align' in OO0O000 :
   pass
  elif '&nbsp;' in OO0O000 :
   pass
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + o0ii1I + oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97: i1iIi % Ii % Iii
 if 21 - 21: I1ii11iIi11i / o0ii1I / Ii1I / ooOoO0O00 / I11i
def IiiiIiiI ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'ongoing' in OoO :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in OoO :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in OoO :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in OoO :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in OoO :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def ooO0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiI1i11IiIiii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0O , oOo0O , OO0O000 )
 for url , OO0O000 in IiI1i11IiIiii :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def IIOoOOoOo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o00o = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Ii1Iiiiii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 IiIii1i11i1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in Ii1Iiiiii :
  ii1I ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , OO0O000 in o00o :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def ooOOo00o0ooO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 40 - 40: I11i . I11i * Ii
def i1iIIi ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if '9cart' in OoO :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 44 - 44: I11i
def OOO0O00 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , OO0O000 in IiIi1I1 :
  if '9cart' in url :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 54 - 54: o0o00Oo0O * i1i1I1IIii1II * o0ii1I * oO0o % IIiIiII11i
def IIiIII11Ii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20003 , oOo0O )
 for url , OO0O000 in i1Iii1i1I :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 58 - 58: IiI1i11I
def iii1iII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   o0O0O0o ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 77 - 77: III1iiIii + ii * ooOoO0O00 % ii
def I1I1iiiiiIi1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 22 - 22: III1iiIii . IiI1i11I + I1ii11iIi11i
def IIIIiI1ii1 ( url ) :
 url = cloudflare . source ( url )
 IiIIII1iiIIi ( url )
 if 73 - 73: o0ii1I
def i1ii11Iii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  IiIIII1iiIIi ( url )
  if 46 - 46: IiI1i11I
  if 41 - 41: i1IiiiI1iI + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def o00O ( ) :
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
 ii1I ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 25 - 25: ii . o0ii1I % IiI1i11I . III1iiIii
def O0OO0O ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 67 - 67: ii + i1IiiiI1iI / i1iIi
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 75 - 75: III1iiIii / ii . oOo0O0Ooo + i1IiiiI1iI - IIiIiII11i
 for OoO , OO0O000 in IIi :
  if I1 in OO0O000 . lower ( ) :
   if 'Dad!' in OO0O000 :
    pass
   elif 'Family Guy' in OO0O000 :
    pass
   elif '2 Stupid' in OO0O000 :
    pass
   elif 'The Zelfs' in OO0O000 :
    pass
   elif 'A Clone' in OO0O000 :
    pass
   elif 'A.T.O.M' in OO0O000 :
    pass
   elif 'Almost Naked' in OO0O000 :
    pass
   elif 'Angry Kid' in OO0O000 :
    pass
   elif 'Annoying Orange' in OO0O000 :
    pass
   elif 'Aqua Teen' in OO0O000 :
    pass
   elif 'Assy Mcgee' in OO0O000 :
    pass
   elif 'Astroblast' in OO0O000 :
    pass
   elif 'Atomic Betty' in OO0O000 :
    pass
   elif 'Axe Cop' in OO0O000 :
    pass
   elif 'Baby Playpen' in OO0O000 :
    pass
   elif 'Beavis and Butt' in OO0O000 :
    pass
   elif 'Celebrity Deathmatch' in OO0O000 :
    pass
   elif 'Clerks The' in OO0O000 :
    pass
   elif 'Crapston Villas' in OO0O000 :
    pass
   elif 'Duckman:' in OO0O000 :
    pass
   elif 'Stripperella' in OO0O000 :
    pass
   elif 'Vixen' in OO0O000 :
    pass
   else :
    ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 33 - 33: III1iiIii / III1iiIii . Ii * Ii1I + I11i
    if 16 - 16: III1iiIii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 10 - 10: OOooOOo . III1iiIii * iI11I1II1I1I - i1i1I1IIii1II - OOooOOo / i1IiiiI1iI
def oo0OO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if 'Dad!' in OO0O000 :
   pass
  elif 'Family Guy' in OO0O000 :
   pass
  elif '2 Stupid' in OO0O000 :
   pass
  elif 'The Zelfs' in OO0O000 :
   pass
  elif 'A Clone' in OO0O000 :
   pass
  elif 'A.T.O.M' in OO0O000 :
   pass
  elif 'Almost Naked' in OO0O000 :
   pass
  elif 'Angry Kid' in OO0O000 :
   pass
  elif 'Annoying Orange' in OO0O000 :
   pass
  elif 'Aqua Teen' in OO0O000 :
   pass
  elif 'Assy Mcgee' in OO0O000 :
   pass
  elif 'Astroblast' in OO0O000 :
   pass
  elif 'Atomic Betty' in OO0O000 :
   pass
  elif 'Axe Cop' in OO0O000 :
   pass
  elif 'Baby Playpen' in OO0O000 :
   pass
  elif 'Beavis and Butt' in OO0O000 :
   pass
  elif 'Celebrity Deathmatch' in OO0O000 :
   pass
  elif 'Clerks The' in OO0O000 :
   pass
  elif 'Crapston Villas' in OO0O000 :
   pass
  elif 'Duckman:' in OO0O000 :
   pass
  elif 'Stripperella' in OO0O000 :
   pass
  elif 'Vixen' in OO0O000 :
   pass
  else :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: i1i1I1IIii1II + OOooOOo % III1iiIii % ii
def iiiiI1iiiIi11 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oO00ooooO0o )
 for oOo0O in i1Iii1i1I :
  O0oOOO0o0Ooo = oOo0O
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oO00ooooO0o )
 for url in IiIi1I1 :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10007 , O0oOOO0o0Ooo )
  if 19 - 19: Ii
  if 80 - 80: oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: i1i1I1IIii1II + Ii1I % OOooOOo
def Iii11I1i ( url , IMAGE ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  print OO0O000 + '     ' + url
  if 'easy' in url :
   oO0OOoOO ( url )
   if 97 - 97: ooOoO0O00
   if 46 - 46: Ii1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 30 - 30: oO0o / o0o00Oo0O * I11i * i1IiiiI1iI + ii * IiI1i11I
def oO0OOoOO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooO0OO ( url )
  if 23 - 23: Iii
  if 36 - 36: III1iiIii . IiI1i11I - ooOoO0O00 + i1IiiiI1iI
  if 54 - 54: ii . i1i1I1IIii1II - IiI1i11I
def oO0o00o000Oo0 ( ) :
 if 1 - 1: oOo0O0Ooo - i1IiiiI1iI
 ii1I ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 62 - 62: oO0o . IiI1i11I . IiI1i11I % ooOoO0O00 * i1i1I1IIii1II % I1ii11iIi11i
def I1I11 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  if 'elete' in OO0O000 :
   pass
  else :
   OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 222 , oOo0O )
   if 16 - 16: o0ii1I % iI11I1II1I1I . oOo0O0Ooo
def IIii1Ii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Oo0O0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , I111ii1III1I , i1iII1IiiIiI1 in Oo0O0o :
  for I1 in I111ii1III1I :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   OO0o0oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for OoO , OO0O000 in OO0o0oo :
    if 'tube' in OoO :
     pass
    elif 'stage' in OoO :
     OO ( '[COLOR' + ooOoOoo0O + ']' + I111ii1III1I + '   -   ' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0O , )
    elif 'vee' in OoO :
     pass
     if 51 - 51: i1iIi * iI11I1II1I1I . IiI1i11I
def iIi11I1II ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Oo0O0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , I111ii1III1I , i1iII1IiiIiI1 in Oo0O0o :
  OO0o0oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for OoO , OO0O000 in OO0o0oo :
   if 'tube' in OoO :
    pass
   elif 'stage' in OoO :
    OO ( '[COLOR' + ooOoOoo0O + ']' + I111ii1III1I + '   -   ' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0O )
   elif 'vee' in OoO :
    pass
    if 93 - 93: Ii1I - i1iIi % Ii1I
    if 12 - 12: oooOo0oo0oo + oO0o * Iii + o0ii1I + III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: IiI1i11I * o0ii1I - Ii % Ii1I
def II1Ii1iI1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o0OoO000O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( o0OoO000O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in o0OoO000O :
  I11iiii1I ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 3 - 3: i1IiiiI1iI . Iii % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
  if 5 - 5: IIiIiII11i * ooOoO0O00 % o0ii1I
  if 55 - 55: oOo0O0Ooo + IiI1i11I
  if 85 - 85: i1i1I1IIii1II + IiI1i11I % IiI1i11I / Iii . oOo0O0Ooo - OOooOOo
  if 19 - 19: Iii / IiI1i11I + III1iiIii
  if 76 - 76: iI11I1II1I1I / i1IiiiI1iI - Ii1I % I11i % oooOo0oo0oo + ii
  if 10 - 10: oO0o * Iii / I1ii11iIi11i - i1IiiiI1iI
def Oo0000oOo ( ) :
 if 11 - 11: III1iiIii % Ii1I / i1iIi . Ii + oooOo0oo0oo - IIiIiII11i
 IiiIiiiiI1III ( '[COLOR darkgoldenrod]Open Murrays Mints[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 IiiIiiiiI1III ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 42 - 42: i1i1I1IIii1II - i1iIi * Iii % IiI1i11I * I1ii11iIi11i / i1IiiiI1iI
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi + iI11I1II1I1I
def OOo0Oo0O00O ( ) :
 IiiIiiiiI1III ( 'Search Murrays Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 IiiIiiiiI1III ( 'Search Murrays TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 56 - 56: Ii1I + i1i1I1IIii1II . oO0o + ii * Ii1I - o0o00Oo0O
 iI1i11iII111 ( 'movies' , 'MAIN' )
def I1iO00O000oOO0oO ( ) :
 if 88 - 88: I11i . oOo0O0Ooo % i1i1I1IIii1II . I1ii11iIi11i % i1iIi . i1i1I1IIii1II
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 O000O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 53 - 53: ooOoO0O00 % o0ii1I - ii / OOooOOo - iI11I1II1I1I
 for iiIiIiII in O000O :
  i1I1 = oO0 + iiIiIiII + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( i1I1 )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoO , I1I , oo0O0 , iI , OO0O000 in IIi :
   if I1 in OO0O000 . lower ( ) :
    I1II1iIi ( OO0O000 , OoO , 222 , I1I , iI , oo0O0 )
    if 36 - 36: OOooOOo * oO0o / i1iIi / oOo0O0Ooo - o0ii1I
    iI1i11iII111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 53 - 53: i1i1I1IIii1II
    if 99 - 99: I1ii11iIi11i
def IiIi1I11 ( ) :
 if 19 - 19: ooOoO0O00 / III1iiIii + Ii1I * Ii1I
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 O000O = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 90 - 90: ii * IiI1i11I . Ii . i1iIi - i1IiiiI1iI
 for iiIiIiII in O000O :
  oOoO0 = oO0 + iiIiIiII + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( oOoO0 )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OO0O000 , oo0O0 , OoO , oOo0O , iI , IiI11i1IIiiI in IIi :
   if I1 in OO0O000 . lower ( ) :
    IiiIiiiiI1III ( OO0O000 , OoO , IiI11i1IIiiI , oOo0O , iI , oo0O0 )
    if 50 - 50: i1IiiiI1iI * i1IiiiI1iI * I1ii11iIi11i - oO0o
    iI1i11iII111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 12 - 12: I1ii11iIi11i + IiI1i11I / oO0o / I1ii11iIi11i
    if 92 - 92: i1IiiiI1iI % IiI1i11I % I11i . oOo0O0Ooo - Ii1I - I11i
def IiIi ( ) :
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
 oO00ooooO0o = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , oo0O0 , OoO , oOo0O , iI , IiI11i1IIiiI in IIi :
  IiiIiiiiI1III ( OO0O000 , OoO , IiI11i1IIiiI , oOo0O , iI , oo0O0 )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def o000Oo0oO0OO0 ( url ) :
 if 54 - 54: oOo0O0Ooo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1OoO00o00 = ( '%s%s' % ( ooOo , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , I1I , oo0O0 , IiIi1 , OO0O000 in IIi :
  iIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for iII1i11 in iIi :
   if iII1i11 == url :
    OO0O000 = ( '[COLORred]Watched - [/COLOR]' + OO0O000 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I1II1iIi ( OO0O000 , url , 222 , I1I , IiIi1 , oo0O0 )
  if 93 - 93: i1IiiiI1iI % Ii
  iI1i11iII111 ( 'movies' , 'MAIN' )
  if 25 - 25: i1iIi % IiI1i11I * IiI1i11I + iI11I1II1I1I . ooOoO0O00
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 67 - 67: Ii1I + i1i1I1IIii1II * III1iiIii / IIiIiII11i % oO0o % oO0o
  if 28 - 28: OOooOOo % i1i1I1IIii1II - oooOo0oo0oo + oooOo0oo0oo + i1i1I1IIii1II / iI11I1II1I1I
def oo0oOOoOoo ( url ) :
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % o0ii1I
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , oo0O0 , url , oOo0O , iI , IiI11i1IIiiI in IIi :
  IiiIiiiiI1III ( OO0O000 , url , IiI11i1IIiiI , oOo0O , iI , oo0O0 )
  if 81 - 81: oO0o - iI11I1II1I1I
  iI1i11iII111 ( 'movies' , 'MAIN' )
  if 60 - 60: i1IiiiI1iI
  if 77 - 77: oOo0O0Ooo / Ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: i1IiiiI1iI * ooOoO0O00 + i1i1I1IIii1II
def I1II1iIi ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 40 - 40: IIiIiII11i
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  O00OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = False )
 return oo0oo0OOOOOoO
 if 7 - 7: oooOo0oo0oo / oO0o
def IiiIiiiiI1III ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 88 - 88: ooOoO0O00
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  O00OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = True )
 return oo0oo0OOOOOoO
if 53 - 53: i1iIi . oooOo0oo0oo . I11i + i1i1I1IIii1II
if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + o0ii1I % ooOoO0O00 . i1i1I1IIii1II
if 57 - 57: i1i1I1IIii1II
if 92 - 92: IIiIiII11i - oO0o - oooOo0oo0oo % oOo0O0Ooo - OOooOOo * i1IiiiI1iI
if 16 - 16: iI11I1II1I1I + ii - i1iIi * III1iiIii
if 37 - 37: IiI1i11I
if 15 - 15: I11i % oO0o / IiI1i11I
if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
if 20 - 20: oooOo0oo0oo * i1i1I1IIii1II
if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . oooOo0oo0oo
if 31 - 31: i1i1I1IIii1II % ooOoO0O00 . ii - I11i + ii
if 45 - 45: oooOo0oo0oo + Iii / ii - o0ii1I + ii
if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * i1IiiiI1iI
if 62 - 62: oooOo0oo0oo * o0o00Oo0O % III1iiIii . III1iiIii . oOo0O0Ooo
if 91 - 91: ooOoO0O00 . IiI1i11I
def I1I1iiI1i ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 42 - 42: ii - OOooOOo - oooOo0oo0oo * i1IiiiI1iI
def OO0iii111 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o00O000oooOo = [ ]
 try :
  if 100 - 100: i1iIi % Iii / o0o00Oo0O * o0ii1I - Ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  I1I1iiI1i ( 'Making Favorites File' )
  o00O000oooOo . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OOooo000OooO = open ( i1I1iI , "w" )
  OOooo000OooO . write ( json . dumps ( o00O000oooOo ) )
  OOooo000OooO . close ( )
 else :
  I1I1iiI1i ( 'Appending Favorites' )
  OOooo000OooO = open ( i1I1iI ) . read ( )
  o0oo = json . loads ( OOooo000OooO )
  o0oo . append ( ( name , url , iconimage , fanart , mode ) )
  iiiiiii11III = open ( i1I1iI , "w" )
  iiiiiii11III . write ( json . dumps ( o0oo ) )
  iiiiiii11III . close ( )
  if 53 - 53: i1IiiiI1iI + ooOoO0O00 . oO0o / Ii + o0ii1I % OOooOOo
  if 9 - 9: i1iIi . Iii - I1ii11iIi11i . i1IiiiI1iI
def i1I111II11 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  o00O000oooOo = [ ]
  I1I1iiI1i ( 'Making Favorites File' )
  o00O000oooOo . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OOooo000OooO = open ( i1I1iI , "w" )
  OOooo000OooO . write ( json . dumps ( o00O000oooOo ) )
  OOooo000OooO . close ( )
 else :
  o00oO = json . loads ( open ( i1I1iI ) . read ( ) )
  OOO0O0OOo = len ( o00oO )
  for I11ii111i in o00oO :
   OO0O000 = I11ii111i [ 0 ]
   OoO = I11ii111i [ 1 ]
   I1I = I11ii111i [ 2 ]
   try :
    IIiI1I11ii1i = I11ii111i [ 3 ]
    if IIiI1I11ii1i == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     IIiI1I11ii1i = I1I
    else :
     IIiI1I11ii1i = iI
   try : o0oooIi1Iii1 = I11ii111i [ 5 ]
   except : o0oooIi1Iii1 = None
   try : ooooI11iii1iIIIIi = I11ii111i [ 6 ]
   except : ooooI11iii1iIIIIi = None
   if 43 - 43: I11i % i1iIi - o0ii1I / o0o00Oo0O . oOo0O0Ooo
   if I11ii111i [ 4 ] == 0 :
    ii1I ( OO0O000 , OoO , '' , I1I , iI , '' , 'fav' )
   else :
    ii1I ( OO0O000 , OoO , I11ii111i [ 4 ] , I1I , iI , '' , 'fav' )
    if 74 - 74: o0o00Oo0O % Iii % Iii . o0o00Oo0O
def O00oo0 ( name ) :
 o0oo = json . loads ( open ( i1I1iI ) . read ( ) )
 for II1i1iI in range ( len ( o0oo ) ) :
  if o0oo [ II1i1iI ] [ 0 ] == name :
   del o0oo [ II1i1iI ]
   iiiiiii11III = open ( i1I1iI , "w" )
   iiiiiii11III . write ( json . dumps ( o0oo ) )
   iiiiiii11III . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 5 - 5: OOooOOo + IiI1i11I * i1iIi
 if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . i1iIi / I1ii11iIi11i - Ii
def oO00o00 ( ) :
 OOoo = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 iiIi1I = open ( OOoo , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 iiIi1I . write ( r'[' + IiII + ']' + '\n' )
 for OO0O000 , oOo0O , iI1i1i1iiI , OoO in IIi :
  OoO = ( OoO + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  i1IiiiI1Iiii1 = ( OO0O000 + '=plugin://' + IiII + '/?url=' + OoO + '&mode=10012&name=' + ( OO0O000 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iiIi1I . write ( i1IiiiI1Iiii1 + '\n' )
  if 81 - 81: i1iIi + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * i1IiiiI1iI
  if 98 - 98: Ii1I - ii / oOo0O0Ooo . i1iIi - ooOoO0O00
def oOOoOo0OoOO ( ) :
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO in IIi :
  o0O0O0o ( '24/7' , OoO , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 90 - 90: oO0o / o0ii1I % iI11I1II1I1I / o0o00Oo0O * i1i1I1IIii1II / oOo0O0Ooo
def oooO0O0Oo00 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def i1I1i1I111 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def O0o ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def I1I1i ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def iIo0oOOO0 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  i11I1II1I11i ( OO0O000 , OoO , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 11 - 11: Iii / OOooOOo
  if 17 - 17: i1iIi
def IIi1IIII ( ) :
 if 33 - 33: IIiIiII11i . Ii1I - o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
 ii1I ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 53 - 53: o0ii1I / oOo0O0Ooo * o0ii1I + I11i + i1i1I1IIii1II - I1ii11iIi11i
def IIi1iiIIi1i ( ) :
 if 5 - 5: ii / III1iiIii
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 , Oo0 in IIi :
  ii1I ( OO0O000 + '  -  ' + ( Oo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoO , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 51 - 51: oooOo0oo0oo % Ii
  if 77 - 77: oooOo0oo0oo % Ii - Ii1I
  if 21 - 21: Iii . I1ii11iIi11i - ii * ooOoO0O00
def OoOOooOOoo ( ) :
 if 12 - 12: i1i1I1IIii1II . oooOo0oo0oo
 ii1I ( '[COLOR' + ooOoOoo0O + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Adventure[/COLOR]' , 'Macera' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Anime[/COLOR]' , 'Anime' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Drama[/COLOR]' , 'Dram' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Family[/COLOR]' , 'Aile' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']History[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Horror[/COLOR]' , 'Korku' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Romance[/COLOR]' , 'Romantik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Sport[/COLOR]' , 'Spor' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Western[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 52 - 52: Ii / Iii % III1iiIii
def I1111IiII1 ( url ) :
 iIIiIi = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( iIIiIi )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Iii + Iii
  if 46 - 46: i1IiiiI1iI % Ii1I + o0ii1I
  if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / Iii + i1iIi
  if 10 - 10: i1iIi - I1ii11iIi11i % IIiIiII11i
def ooi11iI1111ii1I ( ) :
 if 89 - 89: Ii / o0o00Oo0O - ooOoO0O00 % I1ii11iIi11i + Ii
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 OoO = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( OoO )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  if I1 in OO0O000 . lower ( ) :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 44 - 44: Ii / oooOo0oo0oo * i1iIi
   if 88 - 88: ooOoO0O00 % oooOo0oo0oo / ii * IiI1i11I % i1iIi
   if 5 - 5: Ii1I * o0ii1I % Iii % IIiIiII11i
def iII11IiIIII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iii1IIIiiiI , I1i , O00oooo0OOO00O00 , OO0O000 in IIi :
  i11I111I1 = ( O00oooo0OOO00O00 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OOOoO000 = ( I1i ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0O0O = 'Season ' + OOOoO000 + 'Episode ' + i11I111I1 + OO0O000
  oO0oOO ( o0O0O , iii1IIIiiiI )
  if 84 - 84: Ii / I11i % iI11I1II1I1I . i1iIi . oO0o / IiI1i11I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: IiI1i11I
  if 3 - 3: iI11I1II1I1I
def oO0oOO ( name , url ) :
 iii1IIIiiiI = url
 IioO0oOo = name
 o0o = cloudflare . source ( iii1IIIiiiI )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for o0OoO000O , IIiIiii in i1Iii1i1I :
  OO ( '[COLOR' + ooOoOoo0O + ']' + IioO0oOo + IIiIiii + '[/COLOR]' , o0OoO000O , 222 , iiIi1IIiIi + 'dtv.png' )
  if 71 - 71: I11i + oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: o0o00Oo0O - Iii % i1IiiiI1iI
 if 46 - 46: i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
def iii11i1IIII ( ) :
 if 13 - 13: i1IiiiI1iI % I11i + oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: IiI1i11I
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
 if 5 - 5: oooOo0oo0oo + IiI1i11I
 if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
 if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
 ii1I ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0Ooo0o = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oOo0O , '' , '' )
 for url in O0Ooo0o :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 42 - 42: iI11I1II1I1I / Iii . o0o00Oo0O . o0ii1I
def Ii1i111iI ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0Ooo0o = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  oOo0O = 'http://watchepisodes.cc/' + oOo0O
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10093 , oOo0O , oOo0O , '' )
 for url in O0Ooo0o :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 48 - 48: I1ii11iIi11i
def OooO0oO0Oo0 ( url , iconimage ) :
 oOo0O = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00oooo0OOO00O00 , url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + O00oooo0OOO00O00 + ' - ' + OO0O000 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oOo0O , '' , '' )
  if 84 - 84: IIiIiII11i / oO0o . III1iiIii
def o0OO00oO00 ( url , iconimage ) :
 oOo0O = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  if 'player' in OO0O000 :
   pass
  elif 'vod' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , oOo0O , '' , '' )
   if 65 - 65: Ii1I . o0ii1I / Ii + o0o00Oo0O . III1iiIii
   if 15 - 15: I1ii11iIi11i + IiI1i11I + oOo0O0Ooo * I11i
   if 33 - 33: I11i * I1ii11iIi11i
   if 88 - 88: i1IiiiI1iI % oooOo0oo0oo - OOooOOo - OOooOOo . oOo0O0Ooo
   if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - i1IiiiI1iI
   if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
def Iio00 ( ) :
 if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - o0ii1I
 if 59 - 59: III1iiIii % i1i1I1IIii1II
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 if 15 - 15: i1iIi / i1iIi % ii . i1IiiiI1iI
 if 93 - 93: Ii1I * Ii1I / ii
 if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
 if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
 if 27 - 27: oooOo0oo0oo * III1iiIii / Ii - i1i1I1IIii1II + IIiIiII11i
 if 43 - 43: Ii1I - IIiIiII11i
 if 56 - 56: Ii1I . ooOoO0O00 / IiI1i11I % i1i1I1IIii1II / o0o00Oo0O * Iii
 if 98 - 98: o0o00Oo0O + IiI1i11I
 if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Iii . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - III1iiIii
 ii1I ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
def iIi1i1I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1I111Ii1i11 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1I111Ii1i11 ) )
 for url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 35 - 35: Iii + o0o00Oo0O * IIiIiII11i
def iIi1II111I1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 10 - 10: o0o00Oo0O . OOooOOo * III1iiIii / i1IiiiI1iI / ooOoO0O00
def IiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if 'episode' in url :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 79 - 79: ii * i1IiiiI1iI - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
  if 82 - 82: OOooOOo . o0ii1I
def ooo00OoOooooo ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoooooO0 = 'http://www.watchseriesgo.to/search/' + I1 . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( OoooooO0 )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OoO , OO0O000 in IIi :
  if 'watch online' in OO0O000 :
   pass
  else :
   print OoO
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + OoO , 10044 , oOo0O , '' , '' )
   if 7 - 7: OOooOOo . oooOo0oo0oo % I1ii11iIi11i
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 55 - 55: i1iIi - I1ii11iIi11i * i1i1I1IIii1II
def OOOOO0oOOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , O00oooo0OOO00O00 , oo0O0 in IIi :
  oOO = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O00oooo0OOO00O00 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + oOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0O , '' , oo0O0 )
  if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  oOO = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + oOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
def iIIIIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0O , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1I111Ii1i11 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i , Oo0O0o in i1I111Ii1i11 :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Oo0O0o ) )
  for url , OO0O000 in IIi :
   oOO = ( I1i ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + oOO + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 78 - 78: o0o00Oo0O - i1IiiiI1iI * oooOo0oo0oo + Iii + IIiIiII11i
class IIIiiII1iIi1ii1i ( ) :
 if 49 - 49: OOooOOo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 99 - 99: o0o00Oo0O + III1iiIii + i1iIi - i1iIi * Ii1I / III1iiIii
  oOO = name
  self . Get_Sources ( OoO , oOO )
  if 82 - 82: I11i - oooOo0oo0oo
  if 84 - 84: IiI1i11I % ooOoO0O00 % oO0o % IIiIiII11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OoO , OO0O000 in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + OoO
   self . Get_site_link ( URL , season_name )
   if 94 - 94: i1iIi * o0o00Oo0O
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in IiIi1I1 :
   self . main ( url , season_name )
   if 60 - 60: IiI1i11I / IiI1i11I - i1iIi / ii + o0o00Oo0O
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oOoooO0oo0 = 'DACLIPS'
   if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
    pass
   else :
    self . daclips ( url , season_name , oOoooO0oo0 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    oOoooO0oo0 = 'THEVIDEO'
    if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
     pass
    else :
     self . thevideo ( url , season_name , oOoooO0oo0 )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     oOoooO0oo0 = 'ALLMYVIDEOS'
     if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , oOoooO0oo0 )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      oOoooO0oo0 = 'VIDSPOT'
      if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
       pass
      else :
       self . vidspot ( url , season_name , oOoooO0oo0 )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       oOoooO0oo0 = 'VODLOCKER'
       if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , oOoooO0oo0 )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        oOoooO0oo0 = 'VIDTO'
        if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
         pass
        else :
         self . vidto ( url , season_name , oOoooO0oo0 )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 44 - 44: OOooOOo . i1IiiiI1iI . ooOoO0O00 . OOooOOo * i1iIi
       else :
        if 'youwatch' in url :
         oOoooO0oo0 = 'YouWatch'
         if oOoooO0oo0 in IIIiiII1iIi1ii1i . source_list :
          pass
         else :
          self . youwatch ( url , season_name , oOoooO0oo0 )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 59 - 59: IIiIiII11i * ii - ii
          if 33 - 33: o0o00Oo0O . Ii % I11i
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 , OO0O000 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 50 - 50: i1iIi
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 , OO0O000 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 83 - 83: Ii - oOo0O0Ooo * Ii
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 59 - 59: IiI1i11I - ii / i1iIi + Ii1I . I11i - IiI1i11I
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 29 - 29: i1i1I1IIii1II
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . youplay ( ii1iii11i1 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for ii1iii11i1 in IIi :
   self . Printer ( ii1iii11i1 , season_name , source_name )
   if 26 - 26: o0o00Oo0O % oooOo0oo0oo - III1iiIii . oooOo0oo0oo
 def Printer ( self , Link , season_name , source_name ) :
  if 70 - 70: I11i + Iii / IiI1i11I + i1iIi / oOo0O0Ooo
  if Link in IIIiiII1iIi1ii1i . List :
   pass
  elif source_name in IIIiiII1iIi1ii1i . source_list :
   pass
  else :
   OO ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IIIiiII1iIi1ii1i . List . append ( Link )
   IIIiiII1iIi1ii1i . source_list . append ( source_name )
   if 33 - 33: ii . o0o00Oo0O
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 59 - 59: iI11I1II1I1I
   if 45 - 45: o0o00Oo0O
   if 78 - 78: Iii - iI11I1II1I1I + i1IiiiI1iI - Ii1I - i1IiiiI1iI
   if 21 - 21: ii . o0o00Oo0O / Ii
   if 86 - 86: OOooOOo / oooOo0oo0oo
def ii1 ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 40 - 40: iI11I1II1I1I / i1iIi / oOo0O0Ooo + Ii1I * oooOo0oo0oo
def III1i1iI111I1 ( url ) :
 OOoO0OooO0O = '20'
 OOOO00O0OO0oo = [ ]
 II111IiiIIi = '                                                    '
 o0oooOOO00o0OOO00 = '        '
 ii1I ( II111IiiIIi + 'pl' + o0oooOOO00o0OOO00 + 'w' + o0oooOOO00o0OOO00 + 'd' + o0oooOOO00o0OOO00 + 'l' + o0oooOOO00o0OOO00 + 'f' + o0oooOOO00o0OOO00 + 'a' + o0oooOOO00o0OOO00 + 'pts' , '' , '' , '' , '' , '' )
 oO00ooooO0o = O00OooOo00o ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oo0oOooo0 , oo0oO0oo , o0O0ooo0o , Iii1I11 , O0Oo , oooO , OOooo000OooO , O0oOo00Oo0oo0 , i111 in IIi :
  O0oOO0o00OO = II1i11i1iI1I ( oo0oO0oo )
  oooOoO00O = II1i11i1iI1I ( o0O0ooo0o )
  I1i1IIiiI11II = II1i11i1iI1I ( Iii1I11 )
  Ii1i1 = II1i11i1iI1I ( O0Oo )
  iiiIiIIiIiiii = II1i11i1iI1I ( oooO )
  o00O0OooO0 = II1i11i1iI1I ( OOooo000OooO )
  OOOO00O0OO0oo . append ( oo0oOooo0 [ 0 ] )
  iii1II11II1 = len ( OOOO00O0OO0oo )
  I11i1Iii1I = int ( len ( II111IiiIIi ) - len ( oo0oOooo0 ) - 2 )
  if len ( OOOO00O0OO0oo ) >= 10 :
   I11i1Iii1I = I11i1Iii1I - 1
  if len ( OOOO00O0OO0oo ) <= int ( OOoO0OooO0O ) :
   i11I1II1I11i ( str ( iii1II11II1 ) + ' ' + oo0oOooo0 + II111IiiIIi [ 0 : I11i1Iii1I ] + oo0oO0oo + O0oOO0o00OO + o0O0ooo0o + oooOoO00O + Iii1I11 + I1i1IIiiI11II + O0Oo + Ii1i1 + oooO + iiiIiIIiIiiii + OOooo000OooO + o00O0OooO0 + ' ' + i111 , '' , '' , '' , '' , '' )
   if 11 - 11: I1ii11iIi11i + IIiIiII11i - Ii1I
   if 57 - 57: ii . Ii1I - i1i1I1IIii1II * ooOoO0O00 . Iii
def II1i11i1iI1I ( space ) :
 if len ( space ) > 1 :
  OO00oo = len ( '        ' ) - len ( space ) + 1
  space = int ( OO00oo ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 17 - 17: I11i * Ii * IIiIiII11i - o0ii1I % I11i / o0o00Oo0O
def IIII ( ) :
 if 60 - 60: ooOoO0O00 / iI11I1II1I1I * i1i1I1IIii1II + i1iIi + ii + IIiIiII11i
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
 if 11 - 11: ooOoO0O00 / i1IiiiI1iI * Ii1I * i1IiiiI1iI * i1iIi - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . o0ii1I
 if 26 - 26: i1i1I1IIii1II - i1iIi % I1ii11iIi11i - i1i1I1IIii1II + III1iiIii
 if 33 - 33: o0ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * III1iiIii
 if 21 - 21: o0o00Oo0O * i1iIi % oO0o
 if 14 - 14: o0o00Oo0O / i1IiiiI1iI / i1iIi + III1iiIii - III1iiIii
 if 10 - 10: o0o00Oo0O - Ii1I / i1IiiiI1iI % OOooOOo / ii / o0ii1I
 if 73 - 73: i1iIi + III1iiIii % I11i . Ii1I / oooOo0oo0oo . i1IiiiI1iI
 if 76 - 76: Iii . Ii1I * ii % IiI1i11I
 if 24 - 24: ii
 if 83 - 83: o0o00Oo0O / oO0o
 if 62 - 62: Iii
 if 73 - 73: o0ii1I % oO0o * oooOo0oo0oo
 if 84 - 84: I1ii11iIi11i
 if 18 - 18: ii
 if 85 - 85: ii . oO0o . oO0o
 if 70 - 70: Iii
 if 72 - 72: i1IiiiI1iI - i1iIi - oOo0O0Ooo - IiI1i11I + oooOo0oo0oo - ooOoO0O00
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: IiI1i11I % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * i1i1I1IIii1II + IiI1i11I % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % III1iiIii . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
 if 55 - 55: OOooOOo . iI11I1II1I1I * oooOo0oo0oo % iI11I1II1I1I . oO0o
 if 43 - 43: o0ii1I . oooOo0oo0oo + oOo0O0Ooo * Ii
 if 2 - 2: oooOo0oo0oo
 if 3 - 3: oOo0O0Ooo . IiI1i11I % o0o00Oo0O - i1iIi / o0o00Oo0O
 if 79 - 79: o0ii1I + i1i1I1IIii1II % i1iIi % oOo0O0Ooo
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: IiI1i11I . i1i1I1IIii1II / I1ii11iIi11i . oO0o . Ii
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: IiI1i11I + I1ii11iIi11i % Iii . i1i1I1IIii1II
 if 6 - 6: III1iiIii + Ii1I
 if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
 if 63 - 63: ii * i1IiiiI1iI
 if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . i1i1I1IIii1II % IIiIiII11i
 if 18 - 18: Iii % ii + oO0o / Iii
 if 37 - 37: ooOoO0O00 - o0ii1I / III1iiIii . IIiIiII11i % i1iIi
 if 39 - 39: o0ii1I % Ii * oO0o
 if 23 - 23: oooOo0oo0oo + i1iIi / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: IiI1i11I - I11i
 if 92 - 92: I1ii11iIi11i % I11i - i1iIi / i1iIi / OOooOOo
 if 84 - 84: oooOo0oo0oo
 if 4 - 4: III1iiIii . i1IiiiI1iI / o0ii1I / IiI1i11I + IIiIiII11i
 if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . Iii - o0ii1I
 if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
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
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + OoO , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0O , Oo00OOOOO , '' )
  if 12 - 12: o0ii1I
def i1IiI1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1I111Ii1i11 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1I111Ii1i11 in i1I111Ii1i11 :
  O00 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1I111Ii1i11 ) )
  for i1iii in O00 :
   i1iii = i1iii
  oOoOO0OO0O0 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1I111Ii1i11 ) )
  for oooO000Oo000O , oOo0O , time , O0O0 in oOoOO0OO0O0 :
   iI111I1III = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( O0O0 )
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + i1iii + ' - ' + oooO000Oo000O + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0O , Oo00OOOOO , ( str ( iI111I1III ) ) )
   if 41 - 41: i1i1I1IIii1II - iI11I1II1I1I
 iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if 11 - 11: Ii % I11i % i1iIi
def oO00O ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 if 26 - 26: Ii1I + i1IiiiI1iI - i1i1I1IIii1II + III1iiIii % oooOo0oo0oo
def O0000oOo0OO ( url ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  oo00O000 = OO0O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OO0O000 :
   pass
  else :
   oo00O000 = OO0O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OO ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
 for url , oOo0O , OO0O000 in i1Iii1i1I :
  oo00O000 = OO0O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OO0O000 :
   pass
  else :
   OO ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
def o0o00OO0oOoO ( url ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 16 - 16: oO0o + i1i1I1IIii1II * ooOoO0O00 / Ii1I
 if 100 - 100: oOo0O0Ooo - oooOo0oo0oo
 if 91 - 91: I11i * Ii1I - IiI1i11I . IIiIiII11i
 if 1 - 1: oooOo0oo0oo + i1IiiiI1iI * Ii1I
 if 44 - 44: IiI1i11I
 if 79 - 79: I11i % oooOo0oo0oo . o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II + ooOoO0O00 * IiI1i11I - o0o00Oo0O
 for url , oOo0O , OO0O000 in i1Iii1i1I :
  oo00O000 = OO0O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OO0O000 :
   pass
  else :
   OO ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
   if 84 - 84: IiI1i11I % oOo0O0Ooo / iI11I1II1I1I * o0ii1I * iI11I1II1I1I + Ii1I
def O000o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for o0OoO000O in IIi :
  oOO0O0o0Oo = ( o0OoO000O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I11iiii1I ( 'http:' + oOO0O0o0Oo )
  if 9 - 9: IiI1i11I - IiI1i11I
  if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + i1i1I1IIii1II
  if 20 - 20: oO0o + Iii . IIiIiII11i / Ii
  if 50 - 50: ii / oO0o % iI11I1II1I1I
def IIIIi11111 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  OO ( OO0O000 , url , 8046 , oOo0O )
 for url in i1Iii1i1I :
  o0O0O0o ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def Oo0o00o0oOoo0 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  I11iiii1I ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 36 - 36: i1IiiiI1iI / OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * o0o00Oo0O
def iI11 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oO00ooooO0o )
 for url in IIi :
  yt . PlayVideo ( url )
  if 32 - 32: i1iIi - ii + oO0o
def II1iiiiII ( ) :
 o0O0O0o ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 o0O0O0o ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 o0O0O0o ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0oO ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0O )
 for url in next :
  o0O0O0o ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: Ii / oO0o % o0o00Oo0O / oooOo0oo0oo + I1ii11iIi11i % I11i
  if 93 - 93: OOooOOo % i1IiiiI1iI - IiI1i11I . III1iiIii - Ii1I * IiI1i11I
def i1iI1I1I ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OO ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def i1I11i1iii1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , '' )
  if 96 - 96: o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00O0O0 ( name , url ) :
 ii1IiIi1iIi = 0
 name = name
 url = url
 oOo0O0Oo00oO = [ '144' , '240' , '380' , '480' , '720' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  OooO0OO ( url )
  if 16 - 16: oooOo0oo0oo % oOo0O0Ooo . i1IiiiI1iI * oO0o % o0o00Oo0O . oooOo0oo0oo
  if 94 - 94: Ii1I
  if 33 - 33: Ii1I + Ii1I . o0ii1I
  if 27 - 27: IIiIiII11i - Ii - ii
  if 90 - 90: oOo0O0Ooo
  if 4 - 4: oooOo0oo0oo % i1iIi - oooOo0oo0oo - I11i
  if 30 - 30: III1iiIii
  if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
def oo0OOo ( ) :
 oO00ooooO0o = ooO000 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  if 'genre' in OoO :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , OoO , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOIiI1IIIiI1I1i ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0O )
 for url in next :
  o0O0O0o ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 84 - 84: OOooOOo - Iii
def OoO00O00O0 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  i1I11i1iii1 ( url )
  if 76 - 76: oOo0O0Ooo % Ii + oooOo0oo0oo
def I11iIIi1Iii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://documentarylovers.com/?s=' + ( I1 ) . replace ( ' ' , '+' )
 II1i11I1 = ooIII1II1iii1i . lower ( )
 OOIiI1IIIiI1I1i ( II1i11I1 )
 if 96 - 96: IiI1i11I % IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - Ii1I
def i11i1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if 'films' in url :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def O0O0I1II ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  if 'films' in url :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0O )
 for url in i1Iii1i1I :
  o0O0O0o ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def o0o0OoOO00Oo ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'rtd' in url :
   i1iiIi1II1 ( url )
   if 12 - 12: Ii + Iii - Ii1I
def i1iiIi1II1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oO00ooooO0o )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  OooO0OO ( url )
  if 27 - 27: IiI1i11I
  if 22 - 22: OOooOOo / oOo0O0Ooo
def iI11I1IiI1 ( ) :
 II11iIiIIIiI = ooO000 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , ooo0O0OO in IIi :
  o0O0O0o ( ( OO0O000 + '[COLOR' + ooOoOoo0O + ']' + ooo0O0OO + '[/COLOR]' ) , OoO , 8086 , oOo0O )
  if 5 - 5: IiI1i11I / i1i1I1IIii1II % i1iIi . Ii % OOooOOo + i1i1I1IIii1II
def oOo0oOoo0 ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8087 , oOo0O )
  if 53 - 53: ii + oOo0O0Ooo . IiI1i11I % o0o00Oo0O + o0ii1I / I11i
def oooOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  OO00o0 ( url , OO0O000 )
  if 62 - 62: i1iIi . i1IiiiI1iI
def OO00o0 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  OO ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 97 - 97: oOo0O0Ooo + III1iiIii . Ii * I1ii11iIi11i % ooOoO0O00
def oo00000ooOooO ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OoO , 3002 , 'http://www.solie.org/alibrary/' + oOo0O )
def oo0o0OO00oOO ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0O )
def IiiII1iIi ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 OoO00oooo0o = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , OO0O000 in OoO00oooo0o :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']Season- ' + OO0O000 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , oOo0O , OO0O000 in i1Iii1i1I :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0O )
def iiiiii ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url in IIi :
  ooII1 ( url )
def ooII1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooO0OO ( url )
  if 90 - 90: Iii / i1i1I1IIii1II + OOooOOo
def O0OoO0ooOO0o ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoO , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def IiII11I1I1IIi ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( oO00ooooO0o )
 for url in IIi :
  IiIIII1iiIIi ( url )
  if 44 - 44: OOooOOo
def oOOoo ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoO , 8065 , iiIi1IIiIi + 'classictv.png' )
def I111 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'mp4' in url :
   OooO0OO ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 66 - 66: i1IiiiI1iI * ii / Ii1I - Iii - i1iIi * Iii
def OOoOooO0o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OoO , 8071 , iiIi1IIiIi + 'streams.png' )
def OOoOI1i1i1Iii1 ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  if '(Free Access)' in OO0O000 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def OoO00Ooooo ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , oOo0O , iI , '' )
  if 25 - 25: I11i + iI11I1II1I1I + III1iiIii + Ii1I / i1IiiiI1iI - ooOoO0O00
def Ii1I11Ii1iI ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  OOOOOo00OOoO ( 'http://watchxxxfree.com/categories' )
 if I111I1Iiii1i == 1 :
  i111iii1I11I ( 'http://www.perfectgirls.net' )
 if I111I1Iiii1i == 2 :
  iii111iiI11I ( 'http://www.xvideos.com/best' )
 if I111I1Iiii1i == 3 :
  iII1i ( 'http://www.xvideos.com/best' )
 if I111I1Iiii1i == 4 :
  iii111iiI11I ( 'http://www.xvideos.com/best' )
 if I111I1Iiii1i == 5 :
  iii111iiI11I ( 'http://www.xvideos.com/verified/videos' )
 if I111I1Iiii1i == 6 :
  oOii1iiiiii ( 'http://www.xvideos.com/tags' )
 if I111I1Iiii1i == 7 :
  OOOoO0o ( 'http://www.xvideos.com/porn' )
 if I111I1Iiii1i == 8 :
  iiioO000oO0oO ( )
  if 44 - 44: oooOo0oo0oo - III1iiIii + IiI1i11I
  if 78 - 78: o0ii1I
  if 29 - 29: IIiIiII11i
  if 79 - 79: iI11I1II1I1I - Ii + i1iIi - IIiIiII11i . iI11I1II1I1I
  if 84 - 84: I1ii11iIi11i % Iii * o0o00Oo0O * Iii
  if 66 - 66: oooOo0oo0oo / iI11I1II1I1I - OOooOOo % o0o00Oo0O . i1iIi
  if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
  if 37 - 37: ooOoO0O00 * Ii
  if 95 - 95: Ii % i1IiiiI1iI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
def II1iiiiI1Ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if 'ch' in url :
   iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def O0oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for OO0O000 , url in III1II1iiI11 :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   ooO00Oo ( url )
def IIiI1iiIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def OOOOOo00OOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , OO00oo in IIi :
  if 'category' in url :
   iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]   ' + OO00oo + '[/COLOR]' , url , 90006 , oOo0O , iiIi1IIiIi + 'Jizbox.png' , '' )
def oo0OooOoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOo0O , '' , '' )
 for url in III1II1iiI11 :
  ii1I ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iIIii1i1iIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   ooO00Oo ( url )
def ooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def i111iii1I11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , OO00oo in IIi :
  if 'category' in url :
   iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]' + OO00oo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iii1IIIiiiI = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0O , '' , '' )
 for url in III1II1iiI11 :
  ii1I ( '[COLORred]NEXT[/COLOR]' , iii1IIIiiiI + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iI1iII1 ( 'http://www.perfectgirls.net' + url )
def iI1iII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiii1I ( 'http://' + url )
def OOOoO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , OO00oo in IIi :
  iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - No of Videos : [COLORorange]' + OO00oo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOii1iiiiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  iIO0OO0o0O00oO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , OO00oo in IIi :
  iIO0OO0o0O00oO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - No of Videos : [COLORorange]' + ( OO00oo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 70 - 70: i1iIi . oO0o + oOo0O0Ooo
def I1iIIiiiIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  iIO0OO0o0O00oO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , I1iiI11i111II in IIi :
  iIO0OO0o0O00oO ( OO0O000 + '--' + ( I1iiI11i111II ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 95 - 95: Iii
  if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - IiI1i11I
def iii111iiI11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , OoOoO , I1II1IIiI11 in IIi :
  iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + I1II1IIiI11 + ' - [COLORred]' + OoOoO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0O , oOo0O , I1II1IIiI11 + ' - ' + OoOoO )
 IIIiiiiiiii1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in IIIiiiiiiii1 :
  iIO0OO0o0O00oO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 97 - 97: Ii1I - i1iIi * Ii + i1IiiiI1iI % ii
def iII1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1I111Ii1i11 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  iIO0OO0o0O00oO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1I111Ii1i11 ) )
 for url , OO0O000 in IIi :
  if '/c/' in url :
   iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . oooOo0oo0oo
   if 3 - 3: o0o00Oo0O - i1IiiiI1iI * o0ii1I * oooOo0oo0oo / o0ii1I
def iiioO000oO0oO ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo000OO00 = ( I1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 II1i11I1 = O0Ooo000OO00 . lower ( )
 OO0oO0Oo = 'http://www.xvideos.com/?k=' + II1i11I1
 print OO0oO0Oo + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( OO0oO0Oo )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OoO , OO0O000 , OoOoO , I1II1IIiI11 in IIi :
  iIO0OO0o0O00oO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + I1II1IIiI11 + ' - [COLORred]' + OoOoO + '[/COLOR]' , 'http://www.xvideos.com' + OoO , 10108 , oOo0O , oOo0O , I1II1IIiI11 + ' - ' + OoOoO )
 IIIiiiiiiii1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for OoO in IIIiiiiiiii1 :
  iIO0OO0o0O00oO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OoO , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 51 - 51: i1iIi * III1iiIii * iI11I1II1I1I / OOooOOo % III1iiIii
if 36 - 36: Ii1I * I11i + Ii + ii
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
if 37 - 37: oooOo0oo0oo + o0o00Oo0O + oooOo0oo0oo . IiI1i11I . I11i
if 78 - 78: oOo0O0Ooo / Iii + I11i . I1ii11iIi11i / o0o00Oo0O
if 49 - 49: Ii1I
if 66 - 66: I11i . Ii1I
if 18 - 18: I1ii11iIi11i + III1iiIii
if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % o0ii1I . oOo0O0Ooo
if 43 - 43: oOo0O0Ooo % Ii1I * o0ii1I
if 31 - 31: o0ii1I / IiI1i11I
if 3 - 3: III1iiIii
if 37 - 37: o0ii1I * ii * Iii + I1ii11iIi11i . oOo0O0Ooo
if 61 - 61: oooOo0oo0oo . oooOo0oo0oo
def ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   OO ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   OO ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in IiIi1I1 :
  if 'http' in url :
   OO ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( url ) :
 o00o = xbmc . Player ( III11I ( ) )
 import urlresolver
 try : o00o . play ( url )
 except : pass
 if 13 - 13: Ii1I / oO0o * Ii % oO0o % oO0o * IIiIiII11i
 if 17 - 17: Iii . o0o00Oo0O * ooOoO0O00 - OOooOOo % ooOoO0O00
def I1iI1I ( ) :
 if 37 - 37: oOo0O0Ooo - iI11I1II1I1I
 if 56 - 56: III1iiIii - o0ii1I + Ii * oO0o % oOo0O0Ooo
 if 37 - 37: iI11I1II1I1I + III1iiIii / i1IiiiI1iI . ii
 if 72 - 72: i1i1I1IIii1II % i1iIi % oooOo0oo0oo
 if 63 - 63: oO0o . o0ii1I % IIiIiII11i / Iii - OOooOOo
 if 4 - 4: I1ii11iIi11i - o0o00Oo0O / Iii + o0o00Oo0O - i1i1I1IIii1II * I1ii11iIi11i
 if 25 - 25: oOo0O0Ooo
 if 64 - 64: i1i1I1IIii1II
 if 80 - 80: I11i % iI11I1II1I1I
 if 63 - 63: III1iiIii * Ii
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0O0OOo00Oo ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8092 , oOo0O )
 for url in next :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI1iIIiIi1Ii ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0oOoOOO000 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O in O0oOoOOO000 :
  oOo0O = oOo0O
 for url , OO0O000 in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8092 , oOo0O )
 for url in next :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 57 - 57: I11i - III1iiIii . oooOo0oo0oo
def IIiIi ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 45 - 45: I1ii11iIi11i
  if 4 - 4: Iii
  if 60 - 60: IIiIiII11i + i1IiiiI1iI / i1i1I1IIii1II % ii - ooOoO0O00
  if 57 - 57: i1iIi
OO00O0O = '{PQ},' ; o0oo0oo0 = '{SC},' ; IIi1II = '{XG},' ; OOOoooO0o0o = '{JP},' ; OOoOoOO00 = '{HW},' ; o0O00 = '{RT},'
def oOOO00o000o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IiIi1oo00ooOoo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 OoO = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iIiII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1
 oo0o0oOo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 4 - 4: Ii % IiI1i11I
 i1i1IiIiIi1Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oO0ooOO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 41 - 41: IiI1i11I + i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( OoO )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 Ii1II11II1iii = O00O0oOO00O00 ( iiiI1i11Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0oOO0ooOoO = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooO0000o00O = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0Ooo = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 96 - 96: o0o00Oo0O + oooOo0oo0oo . i1iIi + oooOo0oo0oo
 if 43 - 43: Ii
 o0iIiiIiiIi = O00O0oOO00O00 ( i1i1IiIiIi1Ii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 i1iiIIIi = O00O0oOO00O00 ( oO0ooOO )
 if 65 - 65: o0o00Oo0O / IiI1i11I . ooOoO0O00 * IiI1i11I / iI11I1II1I1I - i1i1I1IIii1II
 if O0Ooo != 'Failed' :
  Oooo00oOo = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0Ooo )
  for OoO , OO0O000 in Oooo00oOo :
   I1i1Ii11i11 = O00O0oOO00O00 ( OoO )
   Iii1111III111 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i1Ii11i11 )
   for Ii1 , ooo0O0OO in Iii1111III111 :
    ooo0O0OO = ( ooo0O0OO . replace ( '.' , ' ' ) )
    if II1i11I1 in ooo0O0OO . lower ( ) :
     if '.mkv' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 222 , '' , '' , '' )
     elif '.mp4' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 222 , '' , '' , '' )
     elif '.avi' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 222 , '' , '' , '' )
     elif '.wav' in Ii1 :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 222 , '' , '' , '' )
     else :
      ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source Technica[/COLOR]' ) , OoO , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 55 - 55: I11i . Ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: i1i1I1IIii1II
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for O00OO0o0 , OO0O000 in IiIi1I1 :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OoO00oo00 + O00OO0o0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in I1i11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source RaizTv[/COLOR]' ) , OoO , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if Ii1II11II1iii != 'Failed' :
  i1III = [ ]
  iiiO00O00O000OOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1II11II1iii )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in iiiO00O00O000OOO :
   if I1 in OO0O000 . lower ( ) :
    if OO0O000 in i1III :
     pass
    else :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OoO , 1016 , I1I , IiIi1 , oo0O0 )
     i1III . append ( OO0O000 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0oOO0ooOoO != 'Failed' :
  I1Io00oOOoO0oO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0oOO0ooOoO )
  for OoO , oOo0O , OO0O000 in I1Io00oOOoO0oO :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + OoO , 7067 , oOo0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0iIiiIiiIi != 'Failed' :
  i1iii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0iIiiIiiIi )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in i1iii11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , OoO , 222 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 60 - 60: i1IiiiI1iI
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
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
 O000O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
 for iiIiIiII in O000O :
  i1I1 = oO0 + iiIiIiII + oOoOooOo0o0
  O0Ooo = O00O0oOO00O00 ( i1I1 )
  if O0Ooo != 'Failed' :
   Oooo00oOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0Ooo )
   for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in Oooo00oOo :
    if I1 in OO0O000 . lower ( ) :
     i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , OoO , 222 , I1I , IiIi1 , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 49 - 49: I1ii11iIi11i
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
 O000O = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 9 - 9: III1iiIii . Iii
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
 for iiIiIiII in O000O :
  i1I1 = IiIi1oo00ooOoo + iiIiIiII
  I1I1IiIi1 = O00O0oOO00O00 ( i1I1 )
  if I1I1IiIi1 != 'Failed' :
   oOO0o0oo0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1I1IiIi1 )
   for O00OO0o0 , OO0O000 in oOO0o0oo0 :
    if I1 in OO0O000 . lower ( ) :
     OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IiIi1oo00ooOoo + iiIiIiII + O00OO0o0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 96 - 96: i1iIi % o0o00Oo0O
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: oOo0O0Ooo - IiI1i11I / Ii1I . Ii1I + Ii1I
def i1i1iII1 ( ) :
 if 87 - 87: IIiIiII11i . o0ii1I * oO0o
 if 74 - 74: I11i % OOooOOo . IiI1i11I % i1IiiiI1iI . o0o00Oo0O % IIiIiII11i
 if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
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
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 if 6 - 6: oO0o
 if 82 - 82: iI11I1II1I1I . Iii / III1iiIii / oooOo0oo0oo * IIiIiII11i % i1i1I1IIii1II
 Ii1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I1 ) . replace ( ' ' , '+' )
 iii1IIIiiiI = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 OoO00oo00 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 62 - 62: IIiIiII11i
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 96 - 96: Iii % OOooOOo * Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . i1iIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
 if 77 - 77: I11i
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( Ii1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1I1IiIi1 = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 63 - 63: i1iIi * i1i1I1IIii1II + i1iIi * o0ii1I + I1ii11iIi11i / Ii1I
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
 ooO0000o00O = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0Ooo = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
 if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
 if O0Ooo != 'Failed' :
  Oooo00oOo = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0Ooo )
  for OoO , OO0O000 in Oooo00oOo :
   I1i1Ii11i11 = O00O0oOO00O00 ( OoO )
   Iii1111III111 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i1Ii11i11 )
   for Ii1 , ooo0O0OO in Iii1111III111 :
    if II1i11I1 in ooo0O0OO . lower ( ) :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + ooo0O0OO + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + Ii1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if ooO0000o00O != 'Failed' :
  iIiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0000o00O )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in iIiii :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source HeroVision[/COLOR]' ) , OoO , 1016 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 50 - 50: ii * ooOoO0O00 / i1i1I1IIii1II
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
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
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oo0oooo0OoO0o = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for OoO , oOo0O , OO0O000 , I1I1 in i1Iii1i1I :
   if II1i11I1 in OO0O000 . lower ( ) :
    if 'season' in I1I1 :
     o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90054 , oOo0O , oOo0O , '' )
    if 'episodes' in I1I1 :
     o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90044 , oOo0O , oOo0O , '' )
  for OoO in oo0oooo0OoO0o :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 45 - 45: oOo0O0Ooo
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  IIi1I = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
  for OoO , OO0O000 , oOo0O in IIi1I :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( OO0O000 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , OoO , 8022 , oOo0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: i1IiiiI1iI - oooOo0oo0oo % oO0o - I11i % ooOoO0O00
    if 38 - 38: Ii1I . Iii / OOooOOo % Iii
    if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
    if 61 - 61: I1ii11iIi11i - i1IiiiI1iI
    if 51 - 51: IiI1i11I * i1iIi / o0o00Oo0O / o0o00Oo0O
    if 52 - 52: ii % o0o00Oo0O
    if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
    if 28 - 28: ooOoO0O00 / Iii . I11i
    if 11 - 11: I1ii11iIi11i * ii - Ii
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OO0O000 in IiIi1I1 :
   if II1i11I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( OoO00oo00 + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OO0O000 in I1i11 :
   if II1i11I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( Oo0Oo0O + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if I1I1IiIi1 != 'Failed' :
  oOO0o0oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I1IiIi1 )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in oOO0o0oo0 :
   if II1i11I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] Source Scooby[/COLOR]' ) , OoO , 1016 , I1I , IiIi1 , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
 iii1IiI1I1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for iiIiIiII in iii1IiI1I1 :
  i1I1 = oO0 + iiIiIiII + oOoOooOo0o0
  o0iIiiIiiIi = O00O0oOO00O00 ( i1I1 )
  if o0iIiiIiiIi != 'Failed' :
   i1iii11 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0iIiiIiiIi )
   for OO0O000 , oo0O0 , OoO , oOo0O , iI , IiI11i1IIiiI in i1iii11 :
    if II1i11I1 in OO0O000 . lower ( ) :
     ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , OoO , IiI11i1IIiiI , oOo0O , iI , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 3 - 3: Ii1I
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
     if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I111I1 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( I1 ) . replace ( ' ' , '+' )
 if 90 - 90: i1IiiiI1iI % I11i . I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( OoO )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 37 - 37: o0ii1I / IIiIiII11i
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OoO , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + OoO ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iIiiioooOo = '{ZH},' ; o0oo00O0O = '{IX},' ; II11iii1iI1ii = '{LM},'
if 34 - 34: i1iIi . i1iIi
def OOoOi11i ( url ) :
 IIII1II11Iii = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IIII1II11Iii )
 for url , I1i , Oo0 , OO0O000 in IIi :
  o0O0O0o ( ( I1i ) . replace ( 'Sezon' , ' Season ' ) + ( Oo0 ) . replace ( 'Bölüm' , ' Episode ' ) + OO0O000 , url , 8063 , '' )
  if 46 - 46: o0ii1I * o0ii1I / i1i1I1IIii1II * i1IiiiI1iI
  if 37 - 37: OOooOOo + III1iiIii
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + i1IiiiI1iI
  if 58 - 58: i1IiiiI1iI * o0o00Oo0O / o0ii1I + oOo0O0Ooo - Ii1I * I1ii11iIi11i
def ooO0oO00oO0o ( url ) :
 IIII1II11Iii = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IIII1II11Iii )
 for url , OO0O000 in IIi :
  OO ( OO0O000 , url , 222 , '' )
  if 100 - 100: Ii1I - III1iiIii / IiI1i11I * oOo0O0Ooo / Iii / o0o00Oo0O
  if 57 - 57: ooOoO0O00 % i1iIi
  if 69 - 69: I11i
  if 69 - 69: i1IiiiI1iI
def OoOoooO0o0O00o0O ( ) :
 if 68 - 68: OOooOOo
 IIII1II11Iii = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIII1II11Iii )
 for OoO , oOo0O , OO0O000 , Oo0 in IIi :
  o0O0O0o ( OO0O000 + '  -  ' + ( Oo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoO , 8063 , oOo0O )
  if 65 - 65: i1i1I1IIii1II
def o000oOOO ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 , oOo0O in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 8002 , oOo0O )
def iIi1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , time , url , OO0O000 , Oo00o in IIi :
  ii1I ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , time ) , url , 1015 , oOo0O , Oo00o )
  if 65 - 65: o0ii1I
def O0o0OOOooo0 ( ) :
 if 18 - 18: oOo0O0Ooo
 o0O0O0o ( 'Coronation Street' , '' , 8001 , '' )
 o0O0O0o ( 'Eastenders' , '' , 8002 , '' )
 o0O0O0o ( 'Emmerdale' , '' , 8003 , '' )
 o0O0O0o ( 'Hollyoaks' , '' , 8004 , '' )
 o0O0O0o ( 'Im a Celebrity' , '' , 8005 , '' )
 if 32 - 32: iI11I1II1I1I * oOo0O0Ooo . oooOo0oo0oo * iI11I1II1I1I
 if 92 - 92: i1i1I1IIii1II - i1iIi . ii * i1i1I1IIii1II / I1ii11iIi11i
 if 16 - 16: Iii / ii - III1iiIii % oOo0O0Ooo % Iii
 if 97 - 97: oooOo0oo0oo * ooOoO0O00 / ii
def O0oOOoO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'Holly' in OO0O000 :
   oOo0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in OoO :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
   else :
    pass
    if 48 - 48: IiI1i11I * ooOoO0O00 % oO0o / i1iIi - OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 10 - 10: i1iIi
def i1iIi1IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'East' in OO0O000 :
   oOo0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in OoO :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
   else :
    pass
    if 16 - 16: i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: i1iIi / i1i1I1IIii1II % o0o00Oo0O / oooOo0oo0oo * oO0o * Iii
def IIi1ii1i1i1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'Emmer' in OO0O000 :
   oOo0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in OoO :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
   else :
    pass
    if 92 - 92: o0ii1I - i1iIi / i1iIi + III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: oooOo0oo0oo - ii * oO0o * IiI1i11I + i1i1I1IIii1II
def o0o00O0oO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'Coro' in OO0O000 :
   oOo0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in OoO :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
   else :
    pass
    if 54 - 54: OOooOOo % iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: III1iiIii / o0ii1I * oooOo0oo0oo
def iiIIi1Ii1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'Celeb' in OO0O000 :
   oOo0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in OoO :
    OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
   else :
    pass
    if 48 - 48: Iii . Ii % oOo0O0Ooo
def OOOO0oO0OOo0o ( name , url ) :
 OoOO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OoOO :
  iiiiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oO00ooooO0o = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( oO00ooooO0o ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oO00ooooO0o = open_url ( url )
  ooo0O0O0OO = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( oO00ooooO0o ) [ - 1 ]
  iiiiI = ooo0O0O0OO . replace ( '\\/' , '/' )
 Oo0000O0OOooO = xbmcgui . ListItem ( name , '' , '' )
 Oo0000O0OOooO . setPath ( iiiiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0000O0OOooO )
 if 65 - 65: I11i - ii / OOooOOo
 if 49 - 49: i1i1I1IIii1II
def o0o000OOO ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OoO , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for OoO , OO0O000 in i1Iii1i1I :
  o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OoO , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 36 - 36: i1IiiiI1iI * i1IiiiI1iI % oOo0O0Ooo % o0o00Oo0O . oOo0O0Ooo % ii
def OOooooo00OO ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'Movies' in OO0O000 :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( OoO ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def O0O0oOO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0O )
 for url in i1Iii1i1I :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 40 - 40: oO0o - oO0o
  if 58 - 58: III1iiIii * IiI1i11I . oOo0O0Ooo + oooOo0oo0oo
def oO00oo0o00o0o ( url ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url , oOo0O in IIi :
  if '{{' in OO0O000 :
   pass
  else :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0O )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IIIi11II1 = '{UJ},' ; iIi1ii1I1iiI = '{WE},' ; i1I1IIIII1IIi = '{WP},' ; i11iii1II1I1 = '{PP},'
def IiIi11iI1IIi ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url , oOo0O in IIi :
  if '{{' in OO0O000 :
   pass
  else :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0O )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII111I ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  Ooooo0Oo0oOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooooo0Oo0oOo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: ii - o0ii1I - OOooOOo + III1iiIii - ooOoO0O00 . Ii
 if 28 - 28: i1IiiiI1iI / i1i1I1IIii1II . Ii1I
 if 83 - 83: Iii
def i1IOOoOO00O ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '(cooltvseries.com)' in OO0O000 :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , OO0O000 in i1Iii1i1I :
  if '(cooltvseries.com)' in OO0O000 :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def II1iIiiiIiiII ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  I11iiii1I ( ( url ) . replace ( ' ' , '%20' ) )
o0o0IIiI = '{XX},' ; oOOOO00o00 = '{UD},' ; OOo00o0oOO0o = '{YT},' ; I1ii1 = '{JS},' ; O0Oi111 = '{PF},'
if 76 - 76: i1iIi . i1i1I1IIii1II
def iI1 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 , oOo0O in IIi :
  OO ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( OoO ) ) , 222 , oOo0O )
  if 22 - 22: ooOoO0O00 / OOooOOo / oooOo0oo0oo . oO0o % i1IiiiI1iI + Ii
def oooOOoo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  if 'youtu' in url :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0O )
 for url in next :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 86 - 86: OOooOOo
def O0ooO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 6 - 6: ooOoO0O00 / o0ii1I - ii % IIiIiII11i . o0ii1I * Ii
def o0000oOoo0o0o ( url ) :
 oO00ooooO0o = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , oOo0O )
  if 82 - 82: IIiIiII11i * OOooOOo * iI11I1II1I1I % i1i1I1IIii1II * oooOo0oo0oo
  if 33 - 33: o0ii1I . i1i1I1IIii1II
  if 87 - 87: I1ii11iIi11i . I11i - ii * i1i1I1IIii1II % III1iiIii + o0o00Oo0O
  if 16 - 16: Ii1I % I1ii11iIi11i % IIiIiII11i % IIiIiII11i
  if 51 - 51: OOooOOo * OOooOOo - o0o00Oo0O % iI11I1II1I1I / o0o00Oo0O
def Ii11I11i11i11 ( ) :
 if 49 - 49: i1IiiiI1iI % I1ii11iIi11i - i1i1I1IIii1II - I1ii11iIi11i / Ii1I
 o0O0O0o ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 o0O0O0o ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 74 - 74: iI11I1II1I1I . i1IiiiI1iI / Iii * Ii1I / Ii / III1iiIii
 if 15 - 15: ii
def O0O00 ( Cat_Name ) :
 if 75 - 75: I11i
 II1iI = False
 Ooooo0OO = '0'
 if Cat_Name == 'All Channels' : II1iI = True
 if Cat_Name == 'Entertainment' : Ooooo0OO = '1'
 if Cat_Name == 'Movies' : Ooooo0OO = '2'
 if Cat_Name == 'Music' : Ooooo0OO = '3'
 if Cat_Name == 'News' : Ooooo0OO = '4'
 if Cat_Name == 'Sports' : Ooooo0OO = '5'
 if Cat_Name == 'Documentary' : Ooooo0OO = '6'
 if Cat_Name == 'Kids' : Ooooo0OO = '7'
 if Cat_Name == 'Food' : Ooooo0OO = '8'
 if Cat_Name == 'Religious' : Ooooo0OO = '9'
 if Cat_Name == 'USA Channels' : Ooooo0OO = '10'
 if Cat_Name == 'Other' : Ooooo0OO = '11'
 if 51 - 51: III1iiIii - oooOo0oo0oo / OOooOOo
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for OO0O000 , oOo0O , OOo0Oo in IIi :
  iI1iIiI1Ii1iI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0O ) . replace ( '\\' , '' )
  if OOo0Oo == Ooooo0OO :
   o0O0O0o ( OO0O000 , '' , 7022 , iI1iIiI1Ii1iI )
  elif II1iI == True :
   o0O0O0o ( OO0O000 , '' , 7022 , iI1iIiI1Ii1iI )
  else : pass
  if 58 - 58: IIiIiII11i . i1IiiiI1iI . o0ii1I * ii / o0ii1I / Iii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 41 - 41: Iii + oO0o . IiI1i11I
def OoOOoOOOoooO0 ( Search_Name ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , OoO , iii1IIIiiiI , OoO00oo00 in IIi :
  iI1iIiI1Ii1iI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0O ) . replace ( '\\' , '' )
  OO ( Search_Name + ': Link 1' , ( OoO ) . replace ( '\\' , '' ) , 222 , iI1iIiI1Ii1iI )
  OO ( Search_Name + ': Link 2' , ( iii1IIIiiiI ) . replace ( '\\' , '' ) , 222 , iI1iIiI1Ii1iI )
  OO ( Search_Name + ': Link 3' , ( OoO00oo00 ) . replace ( '\\' , '' ) , 222 , iI1iIiI1Ii1iI )
  if 5 - 5: III1iiIii - Iii
def I1iOoO00O ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OO ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def O0oo0ooO ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OO ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def ii1i1 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OO ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 18 - 18: OOooOOo * OOooOOo - I11i % i1iIi % IIiIiII11i - III1iiIii
def OOoi1Iiiiiii ( url ) :
 url
 iII1i11 = xbmcgui . ListItem ( OO0O000 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
 return
 if 62 - 62: iI11I1II1I1I % i1IiiiI1iI % Ii1I * III1iiIii
 if 87 - 87: III1iiIii
def II1i1i ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oO00ooooO0o )
 for url , oo0O0 , oOo0O , OO0O000 in IIi :
  ii1I ( OO0O000 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0O , '' , ( oo0O0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  o0O0O0o ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 17 - 17: I11i . III1iiIii . Ii + ii % Ii
def IIiI1iIiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oo0O0 , oOo0O in IIi :
  i11I1II1I11i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0O , '' , oo0O0 )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 Oo0O0o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o0OoO0o00o in Oo0O0o :
  o0oO0oooOoo = ( o0OoO0o00o ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  ii1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0O , '' , o0oO0oooOoo )
  if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
def O000o0O0 ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 51 - 51: i1iIi * o0ii1I * ii % OOooOOo
 if 25 - 25: iI11I1II1I1I * ii * o0ii1I - ooOoO0O00
 if 23 - 23: I11i . i1iIi - ii + Iii
def o000o0O ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( ( OO0O000 ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def IIIIi1I ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , url , 9032 , iiIi1IIiIi + 'icon.png' )
def I1III ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if '=' in OO0O000 :
   pass
  else :
   OO ( ( OO0O000 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def ii1I1IIi ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if '=' in OO0O000 :
   pass
  else :
   OO ( OO0O000 , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 67 - 67: i1iIi % IiI1i11I
   if 16 - 16: i1iIi + I1ii11iIi11i + ii
   if 87 - 87: oOo0O0Ooo . i1i1I1IIii1II / III1iiIii - ii
def IIiIii1iiI ( url ) :
 OO ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 OO ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 o0O0O0o ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if 'mp4' in url :
   pass
  else :
   OO ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oOOOOOO ( url ) :
 OO ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 OO ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 o0O0O0o ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if 'mp4' in url :
   OO ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: I1ii11iIi11i / Ii1I - o0o00Oo0O + IiI1i11I - IiI1i11I
 if 85 - 85: OOooOOo
 if 29 - 29: oOo0O0Ooo * Ii1I + IiI1i11I
def iIii1iI11ii ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'Daily' in OO0O000 :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 9008 , O0O )
def OoOii1iIiI1i ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def OOoOOOO0 ( url ) :
 OO ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OO ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OO ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  OO ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 75 - 75: oOo0O0Ooo
def o00o000 ( ) :
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if '.m3u' in OoO :
   o0O0O0o ( ( OO0O000 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + OoO ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def IIIi1IiI1iII ( url ) :
 oO00ooooO0o = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  OO ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . i1i1I1IIii1II + Ii
def O0OoOO0oo0 ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'category' in OoO :
   o0O0O0o ( OO0O000 , 'http://www.disclose.tv/' + OoO , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 12 - 12: III1iiIii + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
   if 5 - 5: i1iIi - i1IiiiI1iI - IiI1i11I
def iioOOOoOo0oOoo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  o0O0O0o ( OO0O000 , 'http://www.disclose.tv/' + url , 7011 , oOo0O )
 for url in next :
  o0O0O0o ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 64 - 64: Ii + OOooOOo + I11i + oooOo0oo0oo
  if 33 - 33: oOo0O0Ooo - IiI1i11I . ooOoO0O00 / Ii
def O0oo0 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oO00ooooO0o )
 IiIi1I1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'http' in url :
   OO ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , OO0O000 in i1Iii1i1I :
  OO ( OO0O000 , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in IiIi1I1 :
  OO ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 90 - 90: Iii
  if 40 - 40: i1IiiiI1iI * Iii . i1IiiiI1iI + i1i1I1IIii1II
def o0Ooo0OoO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 31 - 31: Iii + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def iiiiIiI1IIiI ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 Oo0OOo0Ooo = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOOooo = len ( Oo0OOo0Ooo )
 if 9 - 9: ooOoO0O00 % i1IiiiI1iI - oO0o * OOooOOo . I11i
 if 18 - 18: o0ii1I . OOooOOo + IiI1i11I . oOo0O0Ooo + ii . oO0o
 if oOOooo == 1 :
  for i11I1IiIi in Oo0OOo0Ooo :
   i11I1IiIi = i11I1IiIi . replace ( 'player' , 'watch' )
   i1I1I = i11I1IiIi + '&fv=&sou='
   iIiiiIII1II = OooOoooOo ( i1I1I )
   oO00oOOOO = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iIiiiIII1II )
   for ii1iii11i1 in oO00oOOOO :
    o0o0OOO0ooo00 = False
    Resolve ( ii1iii11i1 )
    if 30 - 30: oooOo0oo0oo * Ii1I % Ii1I + IiI1i11I * III1iiIii
 elif oOOooo > 1 :
  if 33 - 33: I11i + Iii * o0o00Oo0O * oO0o . Ii1I
  for i11I1IiIi in Oo0OOo0Ooo :
   O000oOO0Oooo = OooOoooOo ( i11I1IiIi )
   o0000oO0OOOo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( O000oOO0Oooo )
   o00ooo0O = o0000oO0OOOo0
   o00ooo0O = ( str ( o00ooo0O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o00ooo0O
   OO ( 'DOUBLE LINK' , o00ooo0O , 424 , '' )
   if 54 - 54: Ii1I * III1iiIii
   for url in o0000oO0OOOo0 :
    o0O0O0o ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iii1IIIiiiI = Google . resolve ( url )
    except :
     pass
    try :
     I11I11III = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iii1IIIiiiI ) )
     for IIi1i1iI11I11 , oo0ooOo0O0 in I11I11III :
      if 99 - 99: oOo0O0Ooo - iI11I1II1I1I
      HD_URLS . append ( IIi1i1iI11I11 )
      SD_URLS . append ( oo0ooOo0O0 )
    except :
     pass
 else :
  pass
  if 73 - 73: o0o00Oo0O
def O00oo0o0ooO ( ) :
 if 70 - 70: I1ii11iIi11i + i1IiiiI1iI + oooOo0oo0oo . Ii1I - Ii1I
 if 21 - 21: Iii - i1i1I1IIii1II
 o0O0O0o ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 55 - 55: IiI1i11I * I1ii11iIi11i + OOooOOo * oooOo0oo0oo / IiI1i11I * ooOoO0O00
 o0O0O0o ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 49 - 49: III1iiIii + iI11I1II1I1I
 if 30 - 30: Ii % I11i . ooOoO0O00
def iII1Ii1iIIii ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , 'http://cnfstudio.com/genre/' + OoO , 7003 , iiIi1IIiIi + 'icon.png' )
  if 71 - 71: iI11I1II1I1I . OOooOOo * i1IiiiI1iI
iIii1 = xbmcgui . Dialog ( )
if 64 - 64: IiI1i11I - i1IiiiI1iI
i1i1Ii1iiII1I = '{UN},' ; IIIII11IIi = '{IG},' ; i11I1iiI1iI = '{PL},' ; i1i11 = '{LO},' ; OoOO0o000000 = '{LP},' ; O0oooOOoOOO = '{HA},' ; OoO0I1I = '{XD},' ; oo000oooooooO = '{TA},' ; II1IIi1ii111 = '{DP},' ; II1OO = '{JT},' ; oo0OOO0O0 = '{JJ},' ; OoooOooo = '{MM},' ; IiIi1iiII = '{FQ},' ; ooO0o0o = '{HH},'
if 4 - 4: ooOoO0O00 % oO0o * Ii1I . ii
def OOooO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oO00ooooO0o )
 OOooOooOOoO0O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0O )
 OOooOooOOoO0O = OOooOooOOoO0O
 for url in OOooOooOOoO0O :
  o0O0O0o ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 50 - 50: IiI1i11I . oOo0O0Ooo
def O00oo00Ooo ( url ) :
 if 25 - 25: i1iIi
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  O00oo = ooO0o0 ( iiI111I1iIiI )
  Oo00OoOoo = ooO0o0 ( url )
  if 65 - 65: i1IiiiI1iI . o0o00Oo0O + OOooOOo
  if 82 - 82: i1iIi . i1IiiiI1iI . I1ii11iIi11i % iI11I1II1I1I - Ii
def ooO0o0 ( url ) :
 if 11 - 11: i1iIi . i1IiiiI1iI - IiI1i11I . I11i
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  IiIIII1iiIIi ( url )
  if 41 - 41: i1i1I1IIii1II / oO0o - oO0o + i1iIi * oooOo0oo0oo
  if 13 - 13: i1IiiiI1iI * IIiIiII11i - OOooOOo
def II11iii ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 85 - 85: oO0o
def i1111iI1ii ( ) :
 if os . path . exists ( II ) :
  iIi1iii1 = open ( II , 'r' )
  for iII1i11 in iIi1iii1 :
   i1ii = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1i11 )
   for OO0O000 , OoO in i1ii :
    OO ( OO0O000 , OoO , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 17 - 17: i1IiiiI1iI + Ii . Ii * ooOoO0O00 / o0o00Oo0O
def Ii1IiI ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = ooO000 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OO0O000 , url in IIi :
   url = ( url ) . strip ( )
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 58 - 58: iI11I1II1I1I * o0ii1I . i1iIi . I1ii11iIi11i * o0ii1I
  if 63 - 63: OOooOOo . Iii * I11i - Iii % Iii
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoO in IIi :
  OoO = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OoO
 OO0O000 = 'plugin.video.GenieTv'
 if 62 - 62: Iii - i1iIi / i1iIi
 OOooo000 ( OoO , OO0O000 )
 if 52 - 52: iI11I1II1I1I / IiI1i11I . o0o00Oo0O * III1iiIii . oOo0O0Ooo
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoO in IIi :
  OoO = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OoO
 OO0O000 = 'repository.GenieTv'
 if 67 - 67: IIiIiII11i + o0ii1I - oOo0O0Ooo * i1iIi
 OOooo000 ( OoO , OO0O000 )
 if 19 - 19: Ii * I1ii11iIi11i
 if 33 - 33: Ii + oOo0O0Ooo
def O0O00Oo ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  OO00O ( )
 if I111I1Iiii1i == 1 :
  iiO0OoO0OOO00 ( )
  if 15 - 15: I11i . o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . i1i1I1IIii1II * ii
  if 32 - 32: i1iIi / IIiIiII11i . o0o00Oo0O . i1iIi % oOo0O0Ooo - I11i
  if 69 - 69: o0ii1I - oOo0O0Ooo * oooOo0oo0oo . iI11I1II1I1I * OOooOOo . ii
  if 6 - 6: o0o00Oo0O . I11i - OOooOOo
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
Ii1i11IIiI = 'https://addons.tvaddons.ag/'
if 27 - 27: OOooOOo + o0ii1I + IiI1i11I / III1iiIii
def iiO0OoO0OOO00 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 OO0oO0Oo = 'https://addons.tvaddons.ag/search/?keyword=' + II1i11I1
 II11iIiIIIiI = OooOoooOo ( OO0oO0Oo )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , oOOo000oOoO0 , OO0O000 in IIi :
  ii1I ( OO0O000 , OoO , 10054 , 'https://addons.tvaddons.ag/' + oOOo000oOoO0 , Oo00OOOOO , '' )
  if 92 - 92: Iii / oOo0O0Ooo * iI11I1II1I1I / i1iIi + III1iiIii
  if 30 - 30: i1i1I1IIii1II . Ii / Iii + ooOoO0O00 - Iii
def OO00O ( ) :
 II11iIiIIIiI = OooOoooOo ( Ii1i11IIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  if 'Repositories' in OO0O000 :
   pass
  elif 'Services' in OO0O000 :
   pass
  elif 'International' in OO0O000 :
   pass
  else :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 10053 , 'https://addons.tvaddons.ag/' + oOo0O , Oo00OOOOO , '' )
   if 50 - 50: ooOoO0O00
   if 56 - 56: oO0o + i1IiiiI1iI / o0ii1I
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiI1IIIi = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  if 'Please' in OO0O000 :
   pass
  else :
   i11I1II1I11i ( OO0O000 , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0O , Oo00OOOOO , '' )
 for url in iiI1IIIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 75 - 75: OOooOOo
  if 96 - 96: I11i * Iii * I1ii11iIi11i
def Iii11I ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   OooooOOoo0 = os . path . join ( ii1I1 , name + '.zip' )
   try :
    os . remove ( OooooOOoo0 )
   except :
    pass
   downloader . download ( url , OooooOOoo0 , o0oOoO00o )
   i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print i1I1IiiIi1i
   print '======================================='
   extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
   Ooo0OOoOoO0 ( )
   if 45 - 45: oO0o * IIiIiII11i * OOooOOo - oooOo0oo0oo % i1i1I1IIii1II - I1ii11iIi11i
def OOooo000 ( url , name ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OooooOOoo0 = os . path . join ( ii1I1 , name + '.zip' )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 i1I1IiiIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I1IiiIi1i
 print '======================================='
 extract . all ( OooooOOoo0 , i1I1IiiIi1i , o0oOoO00o )
 Ooo0OOoOoO0 ( )
 if 4 - 4: I11i . OOooOOo - iI11I1II1I1I / III1iiIii / oOo0O0Ooo % oOo0O0Ooo
def Ooo0OOoOoO0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 42 - 42: ii + o0o00Oo0O . oO0o % Iii / I1ii11iIi11i
 if 36 - 36: i1iIi / IIiIiII11i - IiI1i11I / o0ii1I
def IiIIIi1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , oOOo000oOoO0 , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , url , 1007 , oOOo000oOoO0 )
def i1I111Ii1I ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , oOOo000oOoO0 , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , oOOo000oOoO0 )
  if 100 - 100: Ii * IiI1i11I * i1iIi
def iiIi1i1iIi1I ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , I1I , oo0O0 , iI , OO0O000 in IIi :
  Ii11I1i ( OO0O000 , 100109 , OoO , image = I1I , isFolder = True )
  if 7 - 7: oO0o . i1i1I1IIii1II % Ii * IIiIiII11i . i1IiiiI1iI
def Iii11II ( url ) :
 import random
 ooOO0000O0o = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 ooOO0000O0o . clear ( )
 o0O0oOooo = [ ]
 i1i1I11I = [ ]
 oo00O000 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iii1IIIiiiI , I1I , oo0O0 , iI , OO0O000 in IIi :
  o0O0oOooo . append ( [ iii1IIIiiiI , OO0O000 ] )
  if len ( o0O0oOooo ) == len ( IIi ) :
   for iII1i11 in o0O0oOooo :
    i11I1ii = random . randint ( 1 , len ( o0O0oOooo ) )
    try :
     o0o000O0o = o0O0oOooo [ int ( i11I1ii ) ]
    except :
     pass
    if len ( i1i1I11I ) <= 20 :
     if o0o000O0o [ 1 ] not in oo00O000 :
      o0o = OooOoooOo ( o0o000O0o [ 0 ] )
      IiIi1I1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for iIiI , Ii1I11II1IiI in IiIi1I1 :
       OOoOoo = OooOoooOo ( iIiI )
       I1i11 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for oo00o0Oo0O0 , iiI111I1iIiI in I1i11 :
        if 'panda' in iiI111I1iIiI :
         Ii1II11II1iii = OooOoooOo ( iiI111I1iIiI )
         iiiO00O00O000OOO = re . compile ( "url: '(.+?)'" ) . findall ( Ii1II11II1iii )
         for OOo00 in iiiO00O00O000OOO :
          if 'http' in OOo00 :
           Oo0000O0OOooO = xbmcgui . ListItem ( o0o000O0o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : o0o000O0o [ 1 ] } )
           Oo0000O0OOooO . setProperty ( "IsPlayable" , "true" )
           ooOO0000O0o . add ( OOo00 , Oo0000O0OOooO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0000O0OOooO )
           if 36 - 36: ooOoO0O00 % i1IiiiI1iI * I1ii11iIi11i
def Ii11I1i ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 iIi1III1I = sys . argv [ 0 ]
 iIi1III1I += '?mode=' + str ( mode )
 iIi1III1I += '&title=' + urllib . quote_plus ( name )
 iIi1III1I += '&image=' + urllib . quote_plus ( image )
 iIi1III1I += '&page=' + str ( page )
 if url != '' :
  iIi1III1I += '&url=' + urllib . quote_plus ( url )
 if keyword :
  iIi1III1I += '&keyword=' + urllib . quote_plus ( keyword )
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  Oo0000O0OOooO . addContextMenuItems ( contextMenu )
 if infoLabels :
  Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  Oo0000O0OOooO . setProperty ( "IsPlayable" , "true" )
 Oo0000O0OOooO . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = isFolder )
 if 75 - 75: oOo0O0Ooo . IiI1i11I % IiI1i11I * Ii + ooOoO0O00 * I1ii11iIi11i
 if 98 - 98: o0ii1I - ii * Iii * i1i1I1IIii1II % Ii1I * IIiIiII11i
def I11o0oO00oO0o0o0 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , iconimage , oo0O0 , iI , name in IIi :
  if 'http' in url :
   if '.php' in url :
    iIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for iII1i11 in iIi :
     if iII1i11 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    IiiIiiiiI1III ( name , url , 1016 , iconimage , iI , oo0O0 )
   else :
    if 'youtube' in url :
     iIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in iIi :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I1II1iIi ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iI , oo0O0 )
    else :
     iIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in iIi :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I1II1iIi ( name , url , 222 , iconimage , iI , oo0O0 )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
  else :
   Oo00 ( url , iconimage , name )
   if 61 - 61: oOo0O0Ooo % iI11I1II1I1I / o0o00Oo0O + I1ii11iIi11i + IiI1i11I
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
  for url , oOOo000oOoO0 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     o0O0O0o ( name , url , 1016 , oOOo000oOoO0 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOo000oOoO0 )
     else :
      iIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in iIi :
       if iII1i11 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OO ( name , url , 222 , oOOo000oOoO0 )
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
   else :
    Oo00 ( url , oOOo000oOoO0 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 56 - 56: Iii / oooOo0oo0oo / i1IiiiI1iI
def Oo00 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooo00oOo = ( url ) . replace ( o0oo00O0O , 'http' ) . replace ( oOOOO00o00 , '.com' ) ;
 oOO0ooO00oO = ( ooo00oOo ) . replace ( II11iii1iI1ii , 'a' ) . replace ( IIi1II , 'b' ) . replace ( OOOoooO0o0o , 'c' ) . replace ( iIi1ii1I1iiI , 'd' ) . replace ( i11I1iiI1iI , 'e' ) . replace ( II1OO , 'f' ) ;
 i1iI1Ii = ( oOO0ooO00oO ) . replace ( o0o0IIiI , 'g' ) . replace ( O0oooOOoOOO , 'h' ) . replace ( OOo00o0oOO0o , 'i' ) . replace ( O0Oi111 , 'j' ) . replace ( OOoOoOO00 , 'k' ) . replace ( o0O00 , 'l' ) ;
 iI11IiIi1I11 = ( i1iI1Ii ) . replace ( ooOOoo0 , 'm' ) . replace ( i1I11I1iIii , 'n' ) . replace ( i11IiIi , 'o' ) . replace ( I1II1oooOooOO , 'p' ) . replace ( i1i1IIiIiI11 , 'q' ) . replace ( ooo0OO0o00 , 'r' ) ;
 ooO00O = ( iI11IiIi1I11 ) . replace ( Oo0OoooOoO0O0 , 's' ) . replace ( i1I1IIIII1IIi , 't' ) . replace ( iIi1i , 'u' ) . replace ( OooIiii1ii , 'v' ) . replace ( OOOO0oo0o0O , 'w' ) . replace ( IIiiiI , 'x' ) ;
 ooooO0OOo0o0 = ( ooO00O ) . replace ( IIo000o0O0000o , 'y' ) . replace ( ii1Iii1iiI11 , 'z' ) . replace ( i1i1Ii1iiII1I , '.' ) . replace ( IIIII11IIi , '(' ) . replace ( i1i11 , ')' ) . replace ( OoOO0o000000 , '/' ) ;
 i11ii1II = ( ooooO0OOo0o0 ) . replace ( iIiiioooOo , '1' ) . replace ( i11iii1II1I1 , '2' ) . replace ( ooOo00OOo0 , '3' ) . replace ( oo000oooooooO , '4' ) . replace ( II1IIi1ii111 , '5' ) . replace ( I1ii1 , '6' ) ;
 ii1IIi = ( i11ii1II ) . replace ( oo0OOO0O0 , '7' ) . replace ( OoooOooo , '8' ) . replace ( IiIi1iiII , '9' ) . replace ( ooO0o0o , '0' ) . replace ( OO00O0O , ':' ) . replace ( o0oo0oo0 , '%' ) ;
 url = ( ii1IIi ) . replace ( IIIi11II1 , '-' ) . replace ( OoO0I1I , '_' ) ;
 OO ( name , url , 222 , iconimage ) ;
 if 44 - 44: oOo0O0Ooo + III1iiIii / Ii1I
 if 31 - 31: IIiIiII11i - Ii1I % Iii . I11i - Ii / Iii
def Oooo0o00Oo00 ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for OoO , oOOo000oOoO0 , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 1007 , oOOo000oOoO0 )
def OoooOoo0Oooo ( url ) :
 if 17 - 17: IiI1i11I . IiI1i11I * oOo0O0Ooo
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , oOOo000oOoO0 , OO0O000 in IIi :
  o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , oOOo000oOoO0 )
  if 98 - 98: III1iiIii
def i11iI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOiII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOiII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
 if 51 - 51: oooOo0oo0oo - ii / ii % ii
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
def II1iiiiI1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  if '-dir-' in OO0O000 :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0O )
  else :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , oOo0O )
   if 75 - 75: iI11I1II1I1I - o0ii1I % o0o00Oo0O % III1iiIii
def II1II1iiIiI ( url ) :
 oO00ooooO0o = ooO000 ( url )
 i1IOO0O0ooOo = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '[To Parent Directory]' in OO0O000 :
   OO0O000 = 'HOME'
   pass
  elif 'HOME' in OO0O000 :
   pass
  elif '.m3u' in OO0O000 :
   o0O0O0o ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , i1IOO0O0ooOo + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in OO0O000 :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , i1IOO0O0ooOo + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in OO0O000 :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , i1IOO0O0ooOo + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , i1IOO0O0ooOo + url , 1012 , iiIi1IIiIi + 'music.png' )
def iI11iI1ii111II ( url ) :
 II11iIiIIIiI = ooO000 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 77 - 77: Ii1I
def Ii1ii1i1 ( url ) :
 oO00ooooO0o = ooO000 ( url )
 i1IOO0O0ooOo = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '.mp3' in OO0O000 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '/' , '' ) , i1IOO0O0ooOo + url , 1011 , iiIi1IIiIi + 'music.png' )
def oo0oO ( ) :
 oO00ooooO0o = ooO000 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , ( 'http://www.cyn.net/music/' + OoO ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0O ) . replace ( ' ' , '%20' ) )
def iII1IiI1I11i ( url , img ) :
 oO00ooooO0o = ooO000 ( url )
 iii1IIIiiiI = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( iii1IIIiiiI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 10 - 10: IIiIiII11i % oOo0O0Ooo % o0ii1I * Ii1I
def iI1iii1iIiiI ( url ) :
 oO00ooooO0o = ooO000 ( url )
 iii1IIIiiiI = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for type , url , OO0O000 in IIi :
  if '[VID]' in type :
   OO ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iii1IIIiiiI + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   iI1iii1iIiiI ( iii1IIIiiiI + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I11i / oO0o + IiI1i11I - ooOoO0O00 / ii / Ii1I
 if 56 - 56: i1i1I1IIii1II + oOo0O0Ooo . Iii
def IiiIiiIIII ( ) :
 IiIi1oo00ooOoo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i11I1 = I1 . lower ( )
 OoO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 Ii1 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 67 - 67: III1iiIii / I11i + Iii % IiI1i11I - i1iIi - oOo0O0Ooo
 II11iIiIIIiI = O00O0oOO00O00 ( OoO )
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( Ii1 )
 o0o = O00O0oOO00O00 ( iii1IIIiiiI )
 if 44 - 44: o0ii1I . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoO , I1I , oo0O0 , IiIi1 , OO0O000 in IIi :
   if I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , OoO , 1016 , I1I , iI , oo0O0 )
    if 22 - 22: Iii * Ii1I . ii / I1ii11iIi11i / o0ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  IIi1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIOOO0O00O0OOOO )
  for OoO , OO0O000 in IIi1I :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + OoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 54 - 54: i1IiiiI1iI % o0ii1I + i1iIi
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for OoO , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    o0O0O0o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + OoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 45 - 45: o0ii1I / i1i1I1IIii1II * i1IiiiI1iI . o0ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: Ii1I / Ii1I
    if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
    if 84 - 84: i1iIi * ii + o0o00Oo0O
    if 84 - 84: ooOoO0O00 . Iii . ooOoO0O00 . I1ii11iIi11i
    if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
    if 5 - 5: iI11I1II1I1I * Ii + oO0o + Iii * o0o00Oo0O % i1iIi
ooOOoo0 = '{SF},' ; i1I11I1iIii = '{IF},' ; i11IiIi = '{PW},' ; ooOo00OOo0 = '{AM},' ; I1II1oooOooOO = '{GF},' ; i1i1IIiIiI11 = '{DD},' ; ooo0OO0o00 = '{UO},' ; Oo0OoooOoO0O0 = '{LE},' ; iIi1i = '{ZY},' ; OooIiii1ii = '{UE},' ; OOOO0oo0o0O = '{PE},' ; IIiiiI = '{JE},' ; IIo000o0O0000o = '{TH},' ; ii1Iii1iiI11 = '{LK},'
if 88 - 88: I11i / Ii * Ii1I
if 23 - 23: o0o00Oo0O / IiI1i11I
def iiI1Ii1 ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 8021 , iiIi1IIiIi + 'iwatch.png' )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def Oo0oOo0Ooo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , iIII in IIi :
  o0O0O0o ( OO0O000 + iIII , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def iiI1 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IiI1o0o0ooo ( url )
def IiI1o0o0ooo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oO00ooooO0o )
 IiIi1I1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oO00ooooO0o )
 I1i11 = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OO ( 'VidSpot - ' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  OO ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , OO0O000 in I1i11 :
  OO ( 'VidUp' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for OO0O000 , url in IiIi1I1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OO ( 'TheVideo - ' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 63 - 63: IIiIiII11i
def iIII1 ( ) :
 oO00ooooO0o = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 1021 , iiIi1IIiIi + 'anime.png' )
  if 84 - 84: ii - ii / III1iiIii
  if 29 - 29: o0ii1I / o0o00Oo0O
def i11IIi ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , OoO , 1002 , iiIi1IIiIi + 'anime.png' )
  if 58 - 58: III1iiIii . I1ii11iIi11i % IiI1i11I / Ii1I . oooOo0oo0oo . ii
  if 52 - 52: oooOo0oo0oo / Ii * I11i + III1iiIii + OOooOOo
  if 95 - 95: IIiIiII11i + oOo0O0Ooo
def oOoOoOo0O0o ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oO00ooooO0o )
 for oOo0O in i1Iii1i1I :
  O0oOOO0o0Ooo = oOo0O
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oO00ooooO0o )
 for url in IiIi1I1 :
  o0O0O0o ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  o0O0O0o ( OO0O000 , url , 1003 , O0oOOO0o0Ooo )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIIIII ( url , IMAGE ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  print OO0O000 + '     ' + url
  if 'easy' in url :
   OOO0O ( url )
  elif 'playpanda' in url :
   OOO0O ( url )
   if 24 - 24: i1iIi % oooOo0oo0oo . o0o00Oo0O * I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOO0O ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( oO00ooooO0o )
 for url in IIi :
  OO ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 52 - 52: o0o00Oo0O . i1IiiiI1iI + IiI1i11I / Ii
  if 52 - 52: i1i1I1IIii1II % I1ii11iIi11i * IIiIiII11i
def ii1iiiIIiIII ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 3 - 3: III1iiIii % i1IiiiI1iI . ii
def ooO000 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 19 - 19: i1IiiiI1iI * o0ii1I - i1i1I1IIii1II
def oOo000oOo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1OoO00o00 = ( '%s%s' % ( ooOo , url ) )
 iiI111I1iIiI = ooO000 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oOOo000oOoO0 , OO0O000 in IIi :
  OO ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOOo000oOoO0 )
  if 42 - 42: oooOo0oo0oo % oooOo0oo0oo
def OO0o0ooo00 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  I11II1iI ( url , OO0O000 )
 else :
  OooO0OO ( url )
def OooO0OO ( url ) :
 import urlresolver
 try :
  i1Ooo0O0OO0OOo = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( i1Ooo0O0OO0OOo , xbmcgui . ListItem ( OO0O000 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( OO0O000 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def IiIIII1iiIIi ( url ) :
 if 12 - 12: Iii
 iIIi = open ( OOOO0OOoO0O0 , "a" )
 iIIi . write ( 'url="' + url + '"\n' )
 iIIi . close
 if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
 o00o = xbmc . Player ( III11I ( ) )
 import urlresolver
 try : o00o . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( OO0O000 ) )
 o00o = xbmc . Player ( III11I ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : o00o . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def I11II1iI ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  iiI1ii1Iii11I = '.mp4'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.mkv' in url :
  iiI1ii1Iii11I = '.mkv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.mp3' in url :
  iiI1ii1Iii11I = '.mp3'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.avi' in url :
  iiI1ii1Iii11I = '.avi'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.mov' in url :
  iiI1ii1Iii11I = '.mov'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.mpeg' in url :
  iiI1ii1Iii11I = '.mpeg'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.mpg' in url :
  iiI1ii1Iii11I = '.mpg'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.flv' in url :
  iiI1ii1Iii11I = '.flv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 elif '.wmv' in url :
  iiI1ii1Iii11I = '.wmv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , iiI1ii1Iii11I )
 else :
  OooO0OO ( url )
def i1O0o00o0Oo ( url , name , cat ) :
 IIiIiI1Ii ( )
 ii1I1 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 OooooOOoo0 = os . path . join ( ii1I1 , file )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def IIiIiI1Ii ( ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def I1iO0000 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % OO0O000 )
 xbmc . sleep ( 1 )
 o00o = xbmc . Player ( III11I ( ) )
 o0oOoO00o . update ( 100 , '%s' % OO0O000 )
 xbmc . sleep ( 1 )
 o00o . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 70 - 70: Iii . OOooOOo . Ii * i1iIi - IIiIiII11i
def I11iiii1I ( url ) :
 o00o = xbmc . Player ( III11I ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : o00o . play ( url ) . strip ( )
 except : pass
 if 23 - 23: III1iiIii
def O0oOo00O0Oo ( url ) :
 o00o = xbmc . Player ( III11I ( ) )
 import urlresolver
 IiiIiIi1iII = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 o00o . play ( IiiIiIi1iII )
 xbmc . sleep ( 1 )
 o00o . play ( url )
 if 52 - 52: o0o00Oo0O * ii . i1IiiiI1iI . oooOo0oo0oo - IiI1i11I % IiI1i11I
 if 33 - 33: Ii - I11i . oOo0O0Ooo - i1i1I1IIii1II - IIiIiII11i + o0o00Oo0O
def III11I ( ) :
 try :
  ooO00oOOo = getSet ( "core-player" )
  if ( ooO00oOOo == 'DVDPLAYER' ) : iII1I11ii1III = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooO00oOOo == 'MPLAYER' ) : iII1I11ii1III = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooO00oOOo == 'PAPLAYER' ) : iII1I11ii1III = xbmc . PLAYER_CORE_PAPLAYER
  else : iII1I11ii1III = xbmc . PLAYER_CORE_AUTO
 except : iII1I11ii1III = xbmc . PLAYER_CORE_AUTO
 return iII1I11ii1III
 return True
 if 34 - 34: OOooOOo % ii . IIiIiII11i % oooOo0oo0oo
def o0O0O0o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O00OO = [ ]
  O00OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = True )
 return oo0oo0OOOOOoO
 if 66 - 66: I1ii11iIi11i - oO0o
def iIO0OO0o0O00oO ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: i1IiiiI1iI
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = True )
 return oo0oo0OOOOOoO
 if 96 - 96: ii / Ii1I * oO0o
def OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O00OO = [ ]
  O00OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = False )
 return oo0oo0OOOOOoO
 if 82 - 82: I1ii11iIi11i / Ii % IIiIiII11i * iI11I1II1I1I + o0ii1I
 if 69 - 69: I1ii11iIi11i
 if 70 - 70: o0o00Oo0O - oO0o - I1ii11iIi11i
 if 95 - 95: III1iiIii * IIiIiII11i % I11i * I1ii11iIi11i . Iii
 if 46 - 46: IIiIiII11i - oO0o % i1iIi
 if 97 - 97: oO0o . OOooOOo
def OOoOOO ( url , heading , announce ) :
 class OoooOOoOOoOo ( ) :
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
   try : oooO = open ( announce ) ; o0Oo = oooO . read ( )
   except : o0Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o0Oo ) )
   return
 OoooOOoOOoOo ( )
 OoooOOoOOoOo ( )
def o0OIiII ( heading , announce ) :
 class OoooOOoOOoOo ( ) :
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
   try : oooO = open ( announce ) ; o0Oo = oooO . read ( )
   except : o0Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o0Oo ) )
   return
 OoooOOoOOoOo ( )
 OoooOOoOOoOo ( )
def ooO0O0O0ooOOO ( ) :
 OOoOOO ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 46 - 46: ii - I1ii11iIi11i * i1IiiiI1iI * oooOo0oo0oo * i1IiiiI1iI . i1i1I1IIii1II
 if 96 - 96: o0ii1I / III1iiIii % I11i + Iii
 if 46 - 46: oO0o * oOo0O0Ooo
 if 25 - 25: i1IiiiI1iI . III1iiIii % o0o00Oo0O % ooOoO0O00
 if 53 - 53: o0o00Oo0O % i1iIi
def Ooo0OOoOoO0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 41 - 41: III1iiIii
 if 29 - 29: i1iIi
 if 70 - 70: i1i1I1IIii1II . o0o00Oo0O % Iii % III1iiIii - Iii * Ii1I
 if 22 - 22: ooOoO0O00
 if 82 - 82: i1i1I1IIii1II . iI11I1II1I1I - Ii1I
 if 55 - 55: I1ii11iIi11i % o0ii1I . iI11I1II1I1I * i1IiiiI1iI
 if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + IiI1i11I - i1i1I1IIii1II
 if 27 - 27: i1IiiiI1iI + i1iIi - i1IiiiI1iI % Ii * I1ii11iIi11i * I11i
 if 88 - 88: oooOo0oo0oo
 if 25 - 25: oO0o + I11i . i1iIi - o0ii1I . i1i1I1IIii1II * o0ii1I
 if 85 - 85: ooOoO0O00
 if 94 - 94: ii . o0o00Oo0O / ii
 if 67 - 67: Ii + OOooOOo
 if 50 - 50: i1iIi . ooOoO0O00 + Ii1I . oooOo0oo0oo
 if 97 - 97: oOo0O0Ooo
 if 63 - 63: o0o00Oo0O - OOooOOo / Ii / ii / i1iIi / IIiIiII11i
 if 45 - 45: IIiIiII11i . oO0o + oO0o * iI11I1II1I1I
 if 23 - 23: III1iiIii * OOooOOo % o0ii1I / o0ii1I - i1iIi - oooOo0oo0oo
 if 86 - 86: oooOo0oo0oo . ii * oOo0O0Ooo - I1ii11iIi11i / Ii * IiI1i11I
 if 56 - 56: oOo0O0Ooo . Iii % IiI1i11I
 if 33 - 33: Iii / oooOo0oo0oo - oooOo0oo0oo / Ii * OOooOOo + o0o00Oo0O
 if 2 - 2: Ii % oOo0O0Ooo
 if 90 - 90: IIiIiII11i
 if 2 - 2: o0ii1I - ii - Ii % I1ii11iIi11i / o0ii1I
def OOO0O0oO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 70 - 70: ooOoO0O00 / Iii / o0o00Oo0O . i1iIi / IIiIiII11i
def Oo0Oo0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 63 - 63: o0o00Oo0O * III1iiIii / I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / Ii
def iiIIi1iiIIiIi1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiI1111i1i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 73 - 73: o0ii1I + i1iIi % oO0o . ooOoO0O00
def OO0oO0ooOOOoO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iIiIIii11iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 27 - 27: I11i
def II1i1IiiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIIIIiiIiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 72 - 72: i1iIi . IiI1i11I + OOooOOo
def i1Iii11iiiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + i1IIIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 77 - 77: III1iiIii + oooOo0oo0oo - iI11I1II1I1I
def iIi1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 16 - 16: Ii * o0ii1I / o0o00Oo0O
def oooO0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 45 - 45: iI11I1II1I1I
def iiIiOOo000Oo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOOO000Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 42 , I1I , iI , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 34 - 34: ii - i1i1I1IIii1II / oooOo0oo0oo / I11i + oooOo0oo0oo . Ii
def oooooo0O000o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iII1IiiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , I1I , iI , OOOoO in IIi :
  ii1I ( OO0O000 , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , OOOoO )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 61 - 61: ii / oooOo0oo0oo % i1i1I1IIii1II
 if 48 - 48: Ii1I . IIiIiII11i * III1iiIii . oOo0O0Ooo * o0ii1I
 if 82 - 82: OOooOOo * Ii1I - ii / ooOoO0O00 + ii * Iii
 if 87 - 87: ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
 if 62 - 62: I11i % IIiIiII11i
 if 22 - 22: i1i1I1IIii1II - I11i
 if 89 - 89: oooOo0oo0oo
 if 34 - 34: IiI1i11I . oooOo0oo0oo
 if 13 - 13: oO0o * oooOo0oo0oo + i1i1I1IIii1II
def iIiiI111I11 ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( o0 ) :
     Ii1Oo0O = 0
     Ii1Oo0O += len ( Ii1IIiII1I )
     if Ii1Oo0O > 0 :
      for oooO in Ii1IIiII1I :
       os . unlink ( os . path . join ( Oo00oo00o00Oo , oooO ) )
  OOOo0O00oO00 = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( OOOo0O00oO00 )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 3 - 3: Ii1I . I1ii11iIi11i . i1i1I1IIii1II . I11i / oOo0O0Ooo
 if 64 - 64: IiI1i11I
 if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
 if 43 - 43: i1IiiiI1iI + oO0o * ii
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
 if 53 - 53: o0ii1I - oooOo0oo0oo
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
def Iii1IiiII1Ii1 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
def ii111 ( url ) :
 Iii1I1III1ii = os . path . join ( oooOOOOO , 'addon_data' )
 o0i11iiII11i = [
 ( Iii1I1III1ii ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( Iii1I1III1ii , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Iii1I1III1ii , 'plugin.video.itv' , 'Images' ) ) ]
 if 83 - 83: I1ii11iIi11i . I11i + IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
 OOoo00o0 = 0
 if 58 - 58: Iii / I11i - III1iiIii
 for iII1i11 in o0i11iiII11i :
  if os . path . exists ( iII1i11 ) and not iII1i11 in [ oo0o0O00 , Iii1I1III1ii ] :
   for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( iII1i11 ) :
    Ii1Oo0O = 0
    Ii1Oo0O += len ( Ii1IIiII1I )
    if Ii1Oo0O > 0 :
     for oooO in Ii1IIiII1I :
      if not oooO in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( Oo00oo00o00Oo , oooO ) )
       except :
        pass
      else : IIo0Oo0oO0oOO00 ( 'Ignore Log File: %s' % oooO )
     for Iii1I11 in I11iIi :
      try :
       shutil . rmtree ( os . path . join ( Oo00oo00o00Oo , Iii1I11 ) )
       OOoo00o0 += 1
       IIo0Oo0oO0oOO00 ( "[Success] cleared %s files from %s" % ( str ( Ii1Oo0O ) , os . path . join ( iII1i11 , Iii1I11 ) ) )
      except :
       IIo0Oo0oO0oOO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , Iii1I11 ) )
  else :
   for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( iII1i11 ) :
    for Iii1I11 in I11iIi :
     if 'cache' in Iii1I11 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Oo00oo00o00Oo , Iii1I11 ) )
       OOoo00o0 += 1
       IIo0Oo0oO0oOO00 ( "[Success] wiped %s " % os . path . join ( iII1i11 , Iii1I11 ) )
      except :
       IIo0Oo0oO0oOO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , Iii1I11 ) )
       if 28 - 28: oooOo0oo0oo
 Iii1IiiII1Ii1 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % OOoo00o0 )
 if 52 - 52: Ii1I - ii % ooOoO0O00 % i1i1I1IIii1II . i1IiiiI1iI
 if 16 - 16: IiI1i11I . III1iiIii . oO0o
 if 39 - 39: o0o00Oo0O
 if 33 - 33: oooOo0oo0oo % IIiIiII11i + i1IiiiI1iI + oOo0O0Ooo * I1ii11iIi11i % OOooOOo
 if 10 - 10: oO0o / o0o00Oo0O . oOo0O0Ooo - oO0o % iI11I1II1I1I - oooOo0oo0oo
 if 36 - 36: oOo0O0Ooo + III1iiIii . III1iiIii
 if 27 - 27: OOooOOo - iI11I1II1I1I / ooOoO0O00 * i1IiiiI1iI - i1iIi
def i1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I111I1IiI1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( I111I1IiI1i1 ) :
   Ii1Oo0O = 0
   Ii1Oo0O += len ( Ii1IIiII1I )
   if 52 - 52: o0ii1I / Ii / i1i1I1IIii1II
   if 54 - 54: i1i1I1IIii1II
   if Ii1Oo0O > 0 :
    if 88 - 88: oooOo0oo0oo / o0ii1I . IiI1i11I - OOooOOo + IiI1i11I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( Ii1Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 83 - 83: IiI1i11I + ii + ooOoO0O00 / I1ii11iIi11i
     for oooO in Ii1IIiII1I :
      os . unlink ( os . path . join ( Oo00oo00o00Oo , oooO ) )
     for Iii1I11 in I11iIi :
      shutil . rmtree ( os . path . join ( Oo00oo00o00Oo , Iii1I11 ) )
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
 if 28 - 28: oOo0O0Ooo
 if 5 - 5: I1ii11iIi11i % oooOo0oo0oo
 if 30 - 30: Ii1I * i1i1I1IIii1II + IIiIiII11i / Ii
 if 34 - 34: Ii % oO0o - i1i1I1IIii1II / oooOo0oo0oo / IiI1i11I
 if 5 - 5: i1IiiiI1iI . i1i1I1IIii1II
 if 77 - 77: IiI1i11I / Ii
 if 20 - 20: o0o00Oo0O . Iii
 if 67 - 67: OOooOOo - i1iIi - iI11I1II1I1I
 if 31 - 31: IIiIiII11i + I11i * Ii . I11i
def iiI11ii1I1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I111I1IiI1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( I111I1IiI1i1 ) :
   Ii1Oo0O = 0
   Ii1Oo0O += len ( Ii1IIiII1I )
   if 73 - 73: i1i1I1IIii1II / oooOo0oo0oo * IIiIiII11i % ii - ooOoO0O00 - i1iIi
   if 43 - 43: I11i + o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
   if Ii1Oo0O > 0 :
    if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( Ii1Oo0O ) + " files found" , "Do you want to delete them?" ) :
     if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
     for oooO in Ii1IIiII1I :
      os . unlink ( os . path . join ( Oo00oo00o00Oo , oooO ) )
     for Iii1I11 in I11iIi :
      shutil . rmtree ( os . path . join ( Oo00oo00o00Oo , Iii1I11 ) )
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
 ii111 ( url )
 return
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
 if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
 if 63 - 63: Ii1I % i1iIi % Ii1I
 if 71 - 71: o0ii1I
 if 43 - 43: I11i / i1iIi
 if 88 - 88: Ii - ooOoO0O00 + I1ii11iIi11i - o0o00Oo0O
 if 50 - 50: Ii1I
 if 37 - 37: i1i1I1IIii1II % IiI1i11I / IIiIiII11i / oO0o - III1iiIii - i1iIi
def oO0IIIIi1IiI1I ( url , name ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1II1I11i = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 iIiooo0O0OOO = os . path . join ( ii1I1 , 'advancedsettings.xml.bak' )
 if os . path . exists ( iIiooo0O0OOO ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IIi1II1I11i = os . path . join ( ii1I1 , 'advancedsettings.xml' )
   try :
    os . remove ( IIi1II1I11i )
    print '=== GenieTv - REMOVING    ' + str ( IIi1II1I11i ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   OOooo000OooO = open ( IIi1II1I11i , "w" )
   OOooo000OooO . write ( iiI111I1iIiI )
   OOooo000OooO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IIi1II1I11i ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IIi1II1I11i = os . path . join ( ii1I1 , 'advancedsettings.xml' )
  try :
   os . remove ( IIi1II1I11i )
   print '=== GenieTv - REMOVING    ' + str ( IIi1II1I11i ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OOooo000OooO = open ( IIi1II1I11i , "w" )
  OOooo000OooO . write ( iiI111I1iIiI )
  OOooo000OooO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1II1I11i ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 5 - 5: OOooOOo . i1i1I1IIii1II + o0ii1I * i1iIi * ii
def iI111I1iiI1 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1II1I11i = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 try :
  OOooo000OooO = open ( IIi1II1I11i ) . read ( )
  if 'zero' in OOooo000OooO :
   name = '0CACHE'
  elif 'tuxen' in OOooo000OooO :
   name = 'TUXENS'
  elif 'muckys' in OOooo000OooO :
   name = 'MUCKYS'
  elif 'p2p1' in OOooo000OooO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OOooo000OooO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OOooo000OooO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 77 - 77: I1ii11iIi11i * I11i - i1i1I1IIii1II
def O0ooOOo0 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IIi1II1I11i = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 try :
  os . remove ( IIi1II1I11i )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IIi1II1I11i ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 32 - 32: o0o00Oo0O + i1IiiiI1iI
 if 11 - 11: ooOoO0O00
 if 65 - 65: oO0o . i1iIi
 if 12 - 12: i1IiiiI1iI + o0o00Oo0O - i1i1I1IIii1II . III1iiIii
 if 46 - 46: III1iiIii . i1iIi / IiI1i11I
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
 if 92 - 92: oO0o % i1iIi * o0o00Oo0O % iI11I1II1I1I / ooOoO0O00 / OOooOOo
 if 67 - 67: i1IiiiI1iI + Iii + i1IiiiI1iI . oooOo0oo0oo % I11i / i1iIi
 if 78 - 78: Ii1I . o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * o0o00Oo0O / Iii * oOo0O0Ooo . Iii
def Iii1iI1iiIii ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for O0Ooo0O0OO , OoOooOOooo0 , O0O00OOOO , OOI11i1iiI1 in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O0Ooo0O0OO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0O00OOOO , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OOI11i1iiI1 )
  inc = inc + 1
  if 6 - 6: ooOoO0O00 % oO0o + i1iIi . Ii1I
  if 72 - 72: oO0o
  if 67 - 67: o0ii1I * ii . i1i1I1IIii1II * Iii * i1i1I1IIii1II - I1ii11iIi11i
  if 82 - 82: III1iiIii
  if 42 - 42: Iii . oO0o * i1iIi
  if 1 - 1: i1IiiiI1iI % IiI1i11I / iI11I1II1I1I * iI11I1II1I1I * i1iIi % IIiIiII11i
  if 59 - 59: III1iiIii
  if 21 - 21: ooOoO0O00 + I1ii11iIi11i + Iii
  if 10 - 10: oOo0O0Ooo - IIiIiII11i - IIiIiII11i + ii . III1iiIii / o0o00Oo0O
def i1i11i ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IIi1II1I11i = os . path . join ( ii1I1 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OOooo000OooO = open ( IIi1II1I11i , "w" )
  OOooo000OooO . write ( iiI111I1iIiI )
  OOooo000OooO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1II1I11i ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 39 - 39: ooOoO0O00 . o0ii1I - I1ii11iIi11i
def oOOoo0O00 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IIi1II1I11i = os . path . join ( ii1I1 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OOooo000OooO = open ( IIi1II1I11i , "w" )
  OOooo000OooO . write ( iiI111I1iIiI )
  OOooo000OooO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IIi1II1I11i ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 30 - 30: ooOoO0O00
 if 86 - 86: oOo0O0Ooo % Iii * o0o00Oo0O + ooOoO0O00 % i1IiiiI1iI
def OoOOo0ooOoooO ( ) :
 try :
  I1ioo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I1ioo0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Iii1iiiiI = os . path . join ( I1ioo0 , "source.db" )
    os . unlink ( Iii1iiiiI )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 44 - 44: ii
 if 70 - 70: o0o00Oo0O - I11i % o0o00Oo0O * o0o00Oo0O / o0o00Oo0O
 if 7 - 7: oO0o + i1i1I1IIii1II
 if 95 - 95: o0ii1I
 if 8 - 8: oooOo0oo0oo . oOo0O0Ooo - oOo0O0Ooo
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 34 - 34: i1i1I1IIii1II . Ii - III1iiIii
 if 83 - 83: IiI1i11I / i1IiiiI1iI . Iii / Ii
 if 4 - 4: i1iIi . oO0o
 if 34 - 34: i1IiiiI1iI * oOo0O0Ooo . ii % Iii
 if 10 - 10: oO0o . oOo0O0Ooo . Iii / Ii - i1iIi
 if 41 - 41: Iii / iI11I1II1I1I . Ii . ooOoO0O00 * iI11I1II1I1I * oooOo0oo0oo
 if 5 - 5: o0o00Oo0O - i1i1I1IIii1II - Ii
def o0OoOO ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; Iiiiii11i1i = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if Iiiiii11i1i :
  oooOoOooOOo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oooOoOooOOo0 = xbmc . translatePath ( oooOoOooOOo0 ) ;
  OOO0O0 = os . path . join ( oooOoOooOOo0 , ".." , ".." ) ; OOO0O0 = os . path . abspath ( OOO0O0 ) ; pluginlog ( "freshstart.main_list xbmcPath=" + OOO0O0 ) ; IIiIiI1I = False
  try :
   for Oo00oo00o00Oo , I11iIi , Ii1IIiII1I in os . walk ( OOO0O0 , topdown = True ) :
    I11iIi [ : ] = [ Iii1I11 for Iii1I11 in I11iIi if Iii1I11 not in o0oO0 ]
    for OO0O000 in Ii1IIiII1I :
     try : os . remove ( os . path . join ( Oo00oo00o00Oo , OO0O000 ) )
     except :
      if OO0O000 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiIiI1I = True
      pluginlog ( "Error removing " + Oo00oo00o00Oo + " " + OO0O000 )
    for OO0O000 in I11iIi :
     try : os . rmdir ( os . path . join ( Oo00oo00o00Oo , OO0O000 ) )
     except :
      if OO0O000 not in [ "Database" , "userdata" ] : IIiIiI1I = True
      pluginlog ( "Error removing " + Oo00oo00o00Oo + " " + OO0O000 )
   if not IIiIiI1I : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 Ooo0OOo ( )
 if 18 - 18: I1ii11iIi11i * IiI1i11I / IIiIiII11i
 if 77 - 77: o0ii1I . I11i * i1i1I1IIii1II
 if 42 - 42: o0ii1I / I1ii11iIi11i
def Ii1111I11I ( ) :
 OO00O00oo0 = [ ]
 oooOoOO000Ooo = sys . argv [ 2 ]
 if len ( oooOoOO000Ooo ) >= 2 :
  O0O0Oo00 = sys . argv [ 2 ]
  oOO0o0OO = O0O0Oo00 . replace ( '?' , '' )
  if ( O0O0Oo00 [ len ( O0O0Oo00 ) - 1 ] == '/' ) :
   O0O0Oo00 = O0O0Oo00 [ 0 : len ( O0O0Oo00 ) - 2 ]
  iI111ii11 = oOO0o0OO . split ( '&' )
  OO00O00oo0 = { }
  for I11ii111i in range ( len ( iI111ii11 ) ) :
   oOoOoo0OOOo0 = { }
   oOoOoo0OOOo0 = iI111ii11 [ I11ii111i ] . split ( '=' )
   if ( len ( oOoOoo0OOOo0 ) ) == 2 :
    OO00O00oo0 [ oOoOoo0OOOo0 [ 0 ] ] = oOoOoo0OOOo0 [ 1 ]
    if 1 - 1: I11i
 return OO00O00oo0
 if 43 - 43: Iii - iI11I1II1I1I - Iii
o0Oo00OoO000O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
IiIiII11i1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii11i1I1i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
II1iii = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
o00oOOo0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
O0oOOOO0o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oOO0O = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OoOOO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
O0I11 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
IiI1111i1i11I = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIiIIii11iI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
IIIIIiiIiIi = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
i1IIIi11 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OOOo0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oOOO000Oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOo0o0O0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
IiIio0oO0O = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOOoOOooO0 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iI1IiiiIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1111I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iII1I1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iII1IiiIIi = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
ooOo = base64 . decodestring ( 'Q1VOVA==' )
def I11iiI1I1 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 Oo0000O0OOooO . setProperty ( 'fanart_image' , fanart )
 Oo0000O0OOooO . setProperty ( "IsPlayable" , "true" )
 IiiiiII1Ii1 = [ ]
 IiiiiII1Ii1 . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 IiiiiII1Ii1 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 Oo0000O0OOooO . addContextMenuItems ( IiiiiII1Ii1 , replaceItems = True )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = False )
 return oo0oo0OOOOOoO
def ii1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = True )
 return oo0oo0OOOOOoO
 if 54 - 54: Ii
def i11I1II1I11i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iIi1III1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oo0oo0OOOOOoO = True
 Oo0000O0OOooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0000O0OOooO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Oo0000O0OOooO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O00OO = [ ]
  if showcontext == 'fav' :
   O00OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   O00OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Oo0000O0OOooO . addContextMenuItems ( O00OO )
 oo0oo0OOOOOoO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIi1III1I , listitem = Oo0000O0OOooO , isFolder = False )
 return oo0oo0OOOOOoO
 if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
 if 11 - 11: IIiIiII11i
O0O0Oo00 = Ii1111I11I ( )
OoO = None
OO0O000 = None
IiI11i1IIiiI = None
I1I = None
iI = None
OOOoO = None
O0oo0o0oO = None
OOOo00Ooo00o0 = None
if 94 - 94: ii / o0o00Oo0O
if 32 - 32: o0o00Oo0O
try :
 OOOo00Ooo00o0 = int ( O0O0Oo00 [ "fav_mode" ] )
except :
 pass
 if 48 - 48: IiI1i11I . o0o00Oo0O * I1ii11iIi11i * o0ii1I . Iii . o0o00Oo0O
try :
 OoO = urllib . unquote_plus ( O0O0Oo00 [ "url" ] )
except :
 pass
try :
 OO0O000 = urllib . unquote_plus ( O0O0Oo00 [ "name" ] )
except :
 pass
try :
 I1I = urllib . unquote_plus ( O0O0Oo00 [ "iconimage" ] )
except :
 pass
try :
 IiI11i1IIiiI = int ( O0O0Oo00 [ "mode" ] )
except :
 pass
try :
 iI = urllib . unquote_plus ( O0O0Oo00 [ "fanart" ] )
except :
 pass
try :
 OOOoO = urllib . unquote_plus ( O0O0Oo00 [ "description" ] )
except :
 pass
 if 50 - 50: Iii . Ii1I
 if 31 - 31: iI11I1II1I1I . oooOo0oo0oo * i1iIi . IiI1i11I - o0o00Oo0O . iI11I1II1I1I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( IiI11i1IIiiI )
print "URL: " + str ( OoO )
print "Name: " + str ( OO0O000 )
print "IconImage: " + str ( I1I )
if 54 - 54: iI11I1II1I1I / oooOo0oo0oo + i1i1I1IIii1II % OOooOOo * OOooOOo - IIiIiII11i
if 43 - 43: o0ii1I / i1IiiiI1iI . i1i1I1IIii1II + iI11I1II1I1I
def iI1i11iII111 ( content , viewType ) :
 if 99 - 99: Ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 29 - 29: oOo0O0Ooo . III1iiIii
if I1I == None : I1I = O0O
if iI == None : iI = Oo00OOOOO
if IiI11i1IIiiI == None :
 Iii1I1I11iiI1 ( )
 if 8 - 8: ooOoO0O00 * o0o00Oo0O
elif IiI11i1IIiiI == 1 :
 I1Ii11i1ii1i ( OoO )
 if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
elif IiI11i1IIiiI == 44 :
 oOoO00o ( OoO )
 if 17 - 17: OOooOOo % oOo0O0Ooo
elif IiI11i1IIiiI == 2 :
 o0ooo ( )
 if 8 - 8: I1ii11iIi11i
elif IiI11i1IIiiI == 3 :
 O0OOo ( )
 if 49 - 49: OOooOOo * Iii - I11i / oO0o * i1i1I1IIii1II
elif IiI11i1IIiiI == 21 :
 i1i1II ( )
 if 51 - 51: i1iIi - iI11I1II1I1I . Iii * OOooOOo + i1IiiiI1iI * ooOoO0O00
elif IiI11i1IIiiI == 4 :
 Oo0Ii1iii ( )
 if 37 - 37: III1iiIii * i1i1I1IIii1II / ii . oO0o
elif IiI11i1IIiiI == 5 :
 I1ii1i11iI1 ( OoO )
 if 77 - 77: IIiIiII11i + OOooOOo * oooOo0oo0oo
elif IiI11i1IIiiI == 6 :
 i1I ( OoO )
 if 9 - 9: IIiIiII11i - Ii * I11i % oO0o * Ii / Iii
elif IiI11i1IIiiI == 7 :
 oO0IIIIi1IiI1I ( OoO , OO0O000 )
 if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
elif IiI11i1IIiiI == 8 :
 iI111I1iiI1 ( OoO , OO0O000 )
 if 11 - 11: iI11I1II1I1I
elif IiI11i1IIiiI == 9 :
 FIXREPOSADDONS ( OoO )
 if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
elif IiI11i1IIiiI == 10 :
 Ooo0OOoOoO0 ( )
 if 80 - 80: ooOoO0O00
elif IiI11i1IIiiI == 11 :
 O0ooOOo0 ( OoO )
 if 56 - 56: IIiIiII11i - I11i
elif IiI11i1IIiiI == 12 :
 Iii1iI1iiIii ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
elif IiI11i1IIiiI == 13 :
 iIiiI111I11 ( )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
elif IiI11i1IIiiI == 14 :
 ii111 ( OoO )
 if 93 - 93: i1i1I1IIii1II
elif IiI11i1IIiiI == 15 :
 I1iO0o0O0OooOoo ( )
 if 60 - 60: i1IiiiI1iI . i1i1I1IIii1II / I1ii11iIi11i * i1iIi + OOooOOo - ooOoO0O00
elif IiI11i1IIiiI == 16 :
 i1i11i ( OoO , OO0O000 )
 if 13 - 13: Ii * i1i1I1IIii1II / Iii * oOo0O0Ooo
elif IiI11i1IIiiI == 17 :
 oOOoo0O00 ( OoO , OO0O000 )
 if 31 - 31: iI11I1II1I1I * o0ii1I % oooOo0oo0oo . IIiIiII11i
elif IiI11i1IIiiI == 18 :
 OoOOo0ooOoooO ( )
 if 56 - 56: III1iiIii / Ii . I11i . i1i1I1IIii1II - Ii
elif IiI11i1IIiiI == 19 :
 i1IIi111iI ( OoO )
 if 23 - 23: Ii1I * Ii % i1iIi
elif IiI11i1IIiiI == 40 :
 ooOoOoo000O0O ( OO0O000 , OoO , OOOoO )
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
elif IiI11i1IIiiI == 42 :
 I11iIi1i1I1i1 ( OO0O000 , OoO , OOOoO )
 if 92 - 92: Ii1I % Ii
elif IiI11i1IIiiI == 43 :
 ooOo0 ( OoO )
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
elif IiI11i1IIiiI == 20 :
 iII1I ( OoO )
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
elif IiI11i1IIiiI == 22 :
 OOO0O0oO ( OoO )
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
elif IiI11i1IIiiI == 23 :
 Oo0Oo0OO ( OoO )
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
elif IiI11i1IIiiI == 24 :
 iiIIi1iiIIiIi1 ( OoO )
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
elif IiI11i1IIiiI == 25 :
 OO0oO0ooOOOoO ( OoO )
 if 48 - 48: i1i1I1IIii1II - IIiIiII11i * oOo0O0Ooo
elif IiI11i1IIiiI == 26 :
 II1i1IiiI ( OoO )
 if 78 - 78: oOo0O0Ooo * Ii * IIiIiII11i
elif IiI11i1IIiiI == 27 :
 i1Iii11iiiI ( OoO )
 if 19 - 19: ii * Ii / o0o00Oo0O . oOo0O0Ooo % Iii
elif IiI11i1IIiiI == 28 :
 iIi1I ( OoO )
 if 35 - 35: iI11I1II1I1I + oOo0O0Ooo - i1iIi / I1ii11iIi11i * Ii1I * I1ii11iIi11i
elif IiI11i1IIiiI == 29 :
 oooO0O ( OoO )
 if 17 - 17: OOooOOo
elif IiI11i1IIiiI == 30 :
 Iii11iI1I ( OoO )
 if 24 - 24: iI11I1II1I1I / oooOo0oo0oo % ii / o0o00Oo0O / i1i1I1IIii1II
elif IiI11i1IIiiI == 31 :
 iiIiOOo000Oo0o ( OoO )
 if 93 - 93: I1ii11iIi11i
elif IiI11i1IIiiI == 32 :
 iiooO ( )
 if 5 - 5: IiI1i11I
elif IiI11i1IIiiI == 33 :
 i1i1i11iI11II ( )
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
elif IiI11i1IIiiI == 35 :
 O0oo0000o ( OoO )
 if 30 - 30: iI11I1II1I1I
elif IiI11i1IIiiI == 34 :
 II1iiI1iI ( OoO )
 if 14 - 14: I11i + o0ii1I
elif IiI11i1IIiiI == 36 :
 OoOooO0 ( OoO )
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
elif IiI11i1IIiiI == 37 :
 O0OO00 ( OoO )
 if 100 - 100: ooOoO0O00
elif IiI11i1IIiiI == 38 :
 OoOiII11IiIi ( OoO )
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
elif IiI11i1IIiiI == 41 :
 o0OoOO ( O0O0Oo00 )
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
elif IiI11i1IIiiI == 39 :
 oooooo0O000o ( OoO )
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
elif IiI11i1IIiiI == 45 :
 TEXTS ( )
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
elif IiI11i1IIiiI == 46 :
 ooO0O0O0ooOOO ( )
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
elif IiI11i1IIiiI == 47 :
 GEVID ( )
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
elif IiI11i1IIiiI == 48 :
 o0o0OOo0O ( OO0O000 , OoO , OOOoO )
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
elif IiI11i1IIiiI == 49 :
 I1ii1ii11i1I ( )
 if 12 - 12: ii % i1i1I1IIii1II
elif IiI11i1IIiiI == 22222 :
 IiIIII1iiIIi ( OoO )
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
elif IiI11i1IIiiI == 222225 :
 I111i1I1 ( OoO )
 if 79 - 79: o0o00Oo0O
elif IiI11i1IIiiI == 222 :
 OO0o0ooo00 ( OoO )
 if 71 - 71: oO0o - o0o00Oo0O
elif IiI11i1IIiiI == 2222222 :
 OooO0OO ( OoO )
 if 73 - 73: iI11I1II1I1I
elif IiI11i1IIiiI == 222222 :
 I11II1iI ( OoO , OO0O000 )
 if 7 - 7: OOooOOo
elif IiI11i1IIiiI == 333 :
 oOo000oOo ( OoO )
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
elif IiI11i1IIiiI == 1020 :
 iIII1 ( )
 if 3 - 3: Iii
elif IiI11i1IIiiI == 1021 :
 ANIMEEP ( )
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
elif IiI11i1IIiiI == 1022 :
 ANIMEPLAY ( OoO )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
elif IiI11i1IIiiI == 1001 :
 i11IIi ( )
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
elif IiI11i1IIiiI == 1005 :
 Oooo0o00Oo00 ( )
 if 53 - 53: o0o00Oo0O
elif IiI11i1IIiiI == 1007 :
 OoooOoo0Oooo ( OoO )
 if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
elif IiI11i1IIiiI == 1010 :
 II1iiiiI1 ( OoO )
 if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
elif IiI11i1IIiiI == 1011 :
 Ii1ii1i1 ( OoO )
 if 27 - 27: oO0o / IiI1i11I . Ii1I
elif IiI11i1IIiiI == 1012 :
 II1II1iiIiI ( OoO )
 if 71 - 71: oO0o . Ii . iI11I1II1I1I + oOo0O0Ooo - I11i
elif IiI11i1IIiiI == 1030 :
 oo0oO ( )
 if 34 - 34: IiI1i11I
elif IiI11i1IIiiI == 1031 :
 iII1IiI1I11i ( OoO , I1I )
 if 6 - 6: oO0o . OOooOOo + Ii1I
elif IiI11i1IIiiI == 1032 :
 iI1iii1iIiiI ( OoO )
 if 24 - 24: oO0o . o0ii1I
elif IiI11i1IIiiI == 1006 :
 Parse . ParseURL ( OoO )
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
elif IiI11i1IIiiI == 2030 :
 Parse . addonParseURL ( OoO )
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
elif IiI11i1IIiiI == 2031 :
 Parse . apkParseURL ( OoO )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
elif IiI11i1IIiiI == 2032 :
 Parse . ParseBOSS ( OoO )
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
elif IiI11i1IIiiI == 1002 :
 oOoOoOo0O0o ( OoO )
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
elif IiI11i1IIiiI == 1003 :
 IiIIIIII ( OoO , I1I )
 if 7 - 7: o0ii1I
elif IiI11i1IIiiI == 1004 :
 OOO0O ( OoO )
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
elif IiI11i1IIiiI == 1008 :
 iI1 ( )
 if 55 - 55: oO0o % OOooOOo
elif IiI11i1IIiiI == 1009 :
 Ii1IiI ( OoO )
 if 58 - 58: o0ii1I
elif IiI11i1IIiiI == 2001 :
 i1111iI1ii ( )
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
elif IiI11i1IIiiI == 2002 :
 iI11iI1ii111II ( OoO )
 if 88 - 88: i1iIi . IIiIiII11i * o0o00Oo0O % III1iiIii
elif IiI11i1IIiiI == 1013 :
 i1i1I1Ii1IIii ( )
elif IiI11i1IIiiI == 10111113 :
 oOo00OO0ooOOO ( OoO )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif IiI11i1IIiiI == 1014 :
 o000oOOO ( )
 if 1 - 1: oOo0O0Ooo
elif IiI11i1IIiiI == 1015 :
 iIi1 ( OoO )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif IiI11i1IIiiI == 1016 :
 I11o0oO00oO0o0o0 ( OoO , I1I , OO0O000 )
 if 88 - 88: I11i - i1i1I1IIii1II
elif IiI11i1IIiiI == 1017 :
 i11i1iiI1i ( )
 if 73 - 73: IIiIiII11i
elif IiI11i1IIiiI == 1018 :
 ooooo ( OoO )
 if 7 - 7: o0o00Oo0O / oO0o
elif IiI11i1IIiiI == 1019 :
 iI11I ( OoO )
elif IiI11i1IIiiI == 10190 :
 oOOOO ( OoO )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif IiI11i1IIiiI == 1023 :
 o00O0o ( )
 if 52 - 52: oOo0O0Ooo / I11i
elif IiI11i1IIiiI == 1024 :
 IiIIIi1 ( OoO )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif IiI11i1IIiiI == 1025 :
 i1I111Ii1I ( OoO )
 if 46 - 46: i1IiiiI1iI . Ii
elif IiI11i1IIiiI == 4001 :
 OoOooOoO ( )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif IiI11i1IIiiI == 4002 :
 oOOo0OOOo00O ( )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif IiI11i1IIiiI == 4003 :
 oOoO000 ( )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif IiI11i1IIiiI == 4004 :
 iIIII1iIIii ( )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif IiI11i1IIiiI == 4005 :
 OoOIiiiii111i1ii ( )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif IiI11i1IIiiI == 4006 :
 II11iI111i1 ( )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif IiI11i1IIiiI == 4007 :
 I1IiiI1ii1i ( )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif IiI11i1IIiiI == 4008 :
 oO0OoO00o ( )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif IiI11i1IIiiI == 40099 : IiI11I111 ( )
elif IiI11i1IIiiI == 4009 : OoO0OOoO0 ( )
elif IiI11i1IIiiI == 4010 : i11iiI ( )
elif IiI11i1IIiiI == 3000 :
 II11iii ( )
 if 65 - 65: I1ii11iIi11i . Iii
elif IiI11i1IIiiI == 3001 :
 oo00000ooOooO ( )
 if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif IiI11i1IIiiI == 3002 :
 oo0o0OO00oOO ( OoO )
 if 11 - 11: OOooOOo % ii
elif IiI11i1IIiiI == 3003 :
 IiiII1iIi ( OoO )
 if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif IiI11i1IIiiI == 3004 :
 iiiiii ( OoO )
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif IiI11i1IIiiI == 404 :
 i11iI ( OO0O000 , OoO , I1I )
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif IiI11i1IIiiI == 405 :
 I1iO0000 ( OoO )
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif IiI11i1IIiiI == 7030 :
 Ii11I11i11i11 ( )
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif IiI11i1IIiiI == 7021 :
 O0O00 ( OO0O000 )
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif IiI11i1IIiiI == 7022 :
 OoOOoOOOoooO0 ( OO0O000 )
 if 29 - 29: oooOo0oo0oo
elif IiI11i1IIiiI == 7000 :
 iiiiIiI1IIiI ( OO0O000 , OoO , img )
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
elif IiI11i1IIiiI == 7050 :
 oooOOoo ( OoO )
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
elif IiI11i1IIiiI == 7051 :
 O0ooO ( OoO )
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
elif IiI11i1IIiiI == 7052 :
 i1IOOoOO00O ( OoO )
 if 91 - 91: Ii . Ii1I + Iii
elif IiI11i1IIiiI == 7053 :
 II1iIiiiIiiII ( OoO )
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
elif IiI11i1IIiiI == 7054 :
 CoolPlay ( OoO )
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
elif IiI11i1IIiiI == 7060 :
 OOooooo00OO ( )
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
elif IiI11i1IIiiI == 7061 :
 oO00oo0o00o0o ( OoO )
 if 52 - 52: IIiIiII11i - III1iiIii
elif IiI11i1IIiiI == 7063 :
 O0O0oOO ( OoO )
 if 91 - 91: iI11I1II1I1I + IiI1i11I . Iii % Ii - Ii + oOo0O0Ooo
elif IiI11i1IIiiI == 7062 :
 IiIi11iI1IIi ( OoO )
 if 75 - 75: Ii1I / oOo0O0Ooo - iI11I1II1I1I / oO0o * oooOo0oo0oo
elif IiI11i1IIiiI == 7064 :
 NATatozcat ( )
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
elif IiI11i1IIiiI == 7067 :
 iII111I ( OoO )
 if 91 - 91: Ii
elif IiI11i1IIiiI == 7066 :
 NATatozA ( OoO )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
elif IiI11i1IIiiI == 7065 :
 Ooooo0Oo0oOo ( OoO )
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
elif IiI11i1IIiiI == 7070 :
 o0o000OOO ( )
 if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
elif IiI11i1IIiiI == 7071 :
 DIZIlist ( OoO )
 if 82 - 82: iI11I1II1I1I
elif IiI11i1IIiiI == 7072 :
 DIZIpull ( OoO )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif IiI11i1IIiiI == 7073 :
 WATCHDIZI ( OoO )
 if 46 - 46: oOo0O0Ooo
elif IiI11i1IIiiI == 7002 :
 iII1Ii1iIIii ( )
 if 72 - 72: IiI1i11I
elif IiI11i1IIiiI == 7003 :
 OOooO ( OoO )
 if 100 - 100: oOo0O0Ooo
elif IiI11i1IIiiI == 7004 :
 O00oo00Ooo ( OoO )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif IiI11i1IIiiI == 7020 :
 ooO0o0 ( OoO )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
elif IiI11i1IIiiI == 7001 :
 O0OoOO0oo0 ( )
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif IiI11i1IIiiI == 7010 :
 iioOOOoOo0oOoo ( OoO )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif IiI11i1IIiiI == 7011 :
 O0oo0 ( OoO )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif IiI11i1IIiiI == 7012 :
 o0Ooo0OoO ( OoO )
 if 93 - 93: oO0o . oO0o
elif IiI11i1IIiiI == 7013 :
 cnfTVPlay2 ( OoO )
elif IiI11i1IIiiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OoO )
elif IiI11i1IIiiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OoO )
elif IiI11i1IIiiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OO0O000 , OoO , I1I )
elif IiI11i1IIiiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IiI11i1IIiiI == 7018 :
 O00oo0o0ooO ( )
elif IiI11i1IIiiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( OoO )
elif IiI11i1IIiiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OoO )
elif IiI11i1IIiiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( OoO )
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif IiI11i1IIiiI == 8000 :
 O0o0OOOooo0 ( )
elif IiI11i1IIiiI == 8001 :
 o0o00O0oO ( )
elif IiI11i1IIiiI == 8002 :
 i1iIi1IiI ( )
elif IiI11i1IIiiI == 8003 :
 IIi1ii1i1i1 ( )
elif IiI11i1IIiiI == 8004 :
 O0oOOoO ( )
elif IiI11i1IIiiI == 8005 :
 iiIIi1Ii1 ( )
elif IiI11i1IIiiI == 8006 :
 OOOO0oO0OOo0o ( OO0O000 , OoO )
elif IiI11i1IIiiI == 8030 :
 oo0 ( OoO )
elif IiI11i1IIiiI == 8045 :
 IIIIi11111 ( OoO )
elif IiI11i1IIiiI == 8046 :
 Oo0o00o0oOoo0 ( OoO )
elif IiI11i1IIiiI == 8047 :
 iI11 ( OoO )
elif IiI11i1IIiiI == 8048 :
 i11i1 ( OoO )
elif IiI11i1IIiiI == 8049 :
 O0O0I1II ( OoO )
elif IiI11i1IIiiI == 804900 :
 o0o0OoOO00Oo ( OoO )
elif IiI11i1IIiiI == 8020 :
 iiI1Ii1 ( )
elif IiI11i1IIiiI == 8021 :
 Oo0oOo0Ooo ( OoO )
elif IiI11i1IIiiI == 8022 :
 iiI1 ( OoO )
elif IiI11i1IIiiI == 8023 :
 IiI1o0o0ooo ( OoO )
elif IiI11i1IIiiI == 8040 :
 II1iiiiII ( )
elif IiI11i1IIiiI == 8041 :
 OO0oO ( OoO )
elif IiI11i1IIiiI == 8042 :
 i1iI1I1I ( OoO )
elif IiI11i1IIiiI == 8043 :
 yt . PlayVideo ( OoO )
elif IiI11i1IIiiI == 8044 :
 i1I11i1iii1 ( OoO )
elif IiI11i1IIiiI == 8060 :
 O0OoO0ooOO0o ( )
elif IiI11i1IIiiI == 8061 :
 IiII11I1I1IIi ( OoO )
elif IiI11i1IIiiI == 8064 :
 oOOoo ( )
elif IiI11i1IIiiI == 8065 :
 I111 ( OoO )
elif IiI11i1IIiiI == 8070 :
 OOoOooO0o ( )
elif IiI11i1IIiiI == 8071 :
 OOoOI1i1i1Iii1 ( OoO )
elif IiI11i1IIiiI == 7080 :
 OoO00Ooooo ( OoO )
elif IiI11i1IIiiI == 8090 :
 I1iI1I ( )
elif IiI11i1IIiiI == 8091 :
 O0O0OOo00Oo ( OoO )
elif IiI11i1IIiiI == 8092 :
 IIiIi ( OoO )
elif IiI11i1IIiiI == 8093 :
 IiI1iIIiIi1Ii ( OoO )
elif IiI11i1IIiiI == 8081 :
 OoOoooO0o0O00o0O ( )
elif IiI11i1IIiiI == 8062 :
 OOoOi11i ( OoO )
elif IiI11i1IIiiI == 8063 :
 ooO0oO00oO0o ( OoO )
elif IiI11i1IIiiI == 8050 :
 iiI1i ( )
elif IiI11i1IIiiI == 8051 :
 o0O00o0 ( OoO )
elif IiI11i1IIiiI == 8052 :
 OoOoOooO0o ( OoO )
elif IiI11i1IIiiI == 8085 :
 iI11I1IiI1 ( )
elif IiI11i1IIiiI == 8086 :
 oOo0oOoo0 ( OoO )
elif IiI11i1IIiiI == 8087 :
 oooOOO0 ( OoO )
elif IiI11i1IIiiI == 8088 :
 OO00o0 ( OoO , OO0O000 )
elif IiI11i1IIiiI == 9000 :
 o0oOo ( )
elif IiI11i1IIiiI == 1111 :
 IiiIiiIIII ( )
elif IiI11i1IIiiI == 9001 :
 oOOO00o000o ( )
elif IiI11i1IIiiI == 9002 :
 i1i1iII1 ( )
elif IiI11i1IIiiI == 9003 :
 I111I1 ( )
elif IiI11i1IIiiI == 9004 :
 World1 ( )
elif IiI11i1IIiiI == 9005 :
 World2 ( OoO )
elif IiI11i1IIiiI == 9006 :
 World3 ( OoO )
elif IiI11i1IIiiI == 9007 :
 iIii1iI11ii ( )
elif IiI11i1IIiiI == 9008 :
 OoOii1iIiI1i ( OoO )
elif IiI11i1IIiiI == 9009 :
 OOoOOOO0 ( OoO )
elif IiI11i1IIiiI == 9010 :
 o00o000 ( )
elif IiI11i1IIiiI == 9011 :
 IIIi1IiI1iII ( OoO )
elif IiI11i1IIiiI == 50 :
 o00i111iiIiiIiI ( OoO )
elif IiI11i1IIiiI == 9020 :
 champlist ( )
elif IiI11i1IIiiI == 9021 :
 I1iOoO00O ( )
elif IiI11i1IIiiI == 9022 :
 O0oo0ooO ( )
elif IiI11i1IIiiI == 9023 :
 ii1i1 ( )
elif IiI11i1IIiiI == 9024 :
 OOoi1Iiiiiii ( OoO )
elif IiI11i1IIiiI == 9030 :
 o000o0O ( OoO )
elif IiI11i1IIiiI == 9031 :
 IIIIi1I ( OoO )
elif IiI11i1IIiiI == 9032 :
 I1III ( OoO )
elif IiI11i1IIiiI == 9033 :
 ii1I1IIi ( OoO )
elif IiI11i1IIiiI == 9034 :
 oO0o00ooO ( )
elif IiI11i1IIiiI == 7085 :
 II1i1i ( OoO )
elif IiI11i1IIiiI == 7086 :
 IIiI1iIiii ( OoO )
elif IiI11i1IIiiI == 7087 :
 O000o0O0 ( OOOoO )
elif IiI11i1IIiiI == 9666 :
 iiI11ii1I1 ( OoO )
elif IiI11i1IIiiI == 10100 : Ii1I11Ii1iI ( )
elif IiI11i1IIiiI == 101001 : OOOoO0o ( OoO )
elif IiI11i1IIiiI == 10105 : iii111iiI11I ( OoO )
elif IiI11i1IIiiI == 10106 : iII1i ( OoO )
elif IiI11i1IIiiI == 10104 : I1iIIiiiIII ( OoO )
elif IiI11i1IIiiI == 10107 : iiioO000oO0oO ( )
elif IiI11i1IIiiI == 10103 : oOii1iiiiii ( OoO )
elif IiI11i1IIiiI == 10108 : ii11 ( OoO )
elif IiI11i1IIiiI == 10000 : Origin_Menu ( )
elif IiI11i1IIiiI == 10001 : o00O ( )
elif IiI11i1IIiiI == 10002 : ii1 ( )
elif IiI11i1IIiiI == 10003 : oO0o00o000Oo0 ( )
elif IiI11i1IIiiI == 10004 : oo0OO ( OoO )
elif IiI11i1IIiiI == 10005 : O0OO0O ( )
elif IiI11i1IIiiI == 10006 : iiiiI1iiiIi11 ( OoO )
elif IiI11i1IIiiI == 10007 : Iii11I1i ( OoO , I1I )
elif IiI11i1IIiiI == 10008 : oO00O ( )
elif IiI11i1IIiiI == 10009 : IIII ( )
elif IiI11i1IIiiI == 10010 : i1IiI1i ( OoO )
elif IiI11i1IIiiI == 10011 : O0000oOo0OO ( OoO )
elif IiI11i1IIiiI == 10012 : OooO0OO ( OoO )
elif IiI11i1IIiiI == 10113 : GRABG ( OoO , OO0O000 )
elif IiI11i1IIiiI == 10109 : O0oOo00O0Oo ( OoO )
elif IiI11i1IIiiI == 10013 : O000o ( OoO )
elif IiI11i1IIiiI == 10014 : iIi11I1II ( )
elif IiI11i1IIiiI == 10015 : IIii1Ii ( )
elif IiI11i1IIiiI == 10016 : II1Ii1iI1i1 ( OoO )
elif IiI11i1IIiiI == 10017 : I1I11 ( )
elif IiI11i1IIiiI == 10018 : IIi1IIII ( )
elif IiI11i1IIiiI == 10019 : IIi1iiIIi1i ( )
elif IiI11i1IIiiI == 10020 : OoOOooOOoo ( )
elif IiI11i1IIiiI == 10021 : ooi11iI1111ii1I ( )
elif IiI11i1IIiiI == 10022 : iII11IiIIII ( OoO )
elif IiI11i1IIiiI == 10023 : oO0oOO ( OO0O000 , OoO )
elif IiI11i1IIiiI == 10024 : I1111IiII1 ( OoO )
elif IiI11i1IIiiI == 10025 : Oo0000oOo ( )
elif IiI11i1IIiiI == 10026 : OOo0Oo0O00O ( )
elif IiI11i1IIiiI == 10027 : I1iO00O000oOO0oO ( )
elif IiI11i1IIiiI == 10028 : IiIi1I11 ( )
elif IiI11i1IIiiI == 10029 : IiIi ( )
elif IiI11i1IIiiI == 423 : oo0oOOoOoo ( OoO )
elif IiI11i1IIiiI == 426 : o000Oo0oO0OO0 ( OoO )
elif IiI11i1IIiiI == 10030 : Izle_Films ( )
elif IiI11i1IIiiI == 10031 : Latest_Izle_Movies ( )
elif IiI11i1IIiiI == 10032 : Izle_Genres ( )
elif IiI11i1IIiiI == 10033 : Izle_Pop_Movies ( )
elif IiI11i1IIiiI == 10034 : Izle_Boxsets ( )
elif IiI11i1IIiiI == 10035 : Izle_Search ( )
elif IiI11i1IIiiI == 10036 : Izle_Genres_Movie ( OoO )
elif IiI11i1IIiiI == 10037 : Izle_Boxset_single ( OoO )
elif IiI11i1IIiiI == 10038 : Izle_IFRAME ( )
elif IiI11i1IIiiI == 10039 : Izle_Boxsets_Next ( OoO )
elif IiI11i1IIiiI == 10040 : Iio00 ( )
elif IiI11i1IIiiI == 10041 : iIIIIII ( OoO )
elif IiI11i1IIiiI == 10042 : OOOOO0oOOoO ( OoO )
elif IiI11i1IIiiI == 10043 : ooo00OoOooooo ( )
elif IiI11i1IIiiI == 10044 : IIoooOoOO0o ( OoO )
elif IiI11i1IIiiI == 10045 : IIIiiII1iIi1ii1i ( OO0O000 )
elif IiI11i1IIiiI == 10046 : o00OooooOOOO ( OoO )
elif IiI11i1IIiiI == 10047 : iIi1i1I1I ( OoO )
elif IiI11i1IIiiI == 10048 : iIi1II111I1i1 ( OoO )
elif IiI11i1IIiiI == 10049 : IiiI ( OoO )
elif IiI11i1IIiiI == 10050 : O0O00Oo ( )
elif IiI11i1IIiiI == 10051 : OO00O ( )
elif IiI11i1IIiiI == 10052 : iiO0OoO0OOO00 ( )
elif IiI11i1IIiiI == 10053 : Addon ( OoO )
elif IiI11i1IIiiI == 10054 : Iii11I ( OoO , OO0O000 )
elif IiI11i1IIiiI == 10055 :
 I1I1iiI1i ( "addFavorite" )
 try :
  OO0O000 = OO0O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0O000 = OO0O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO0iii111 ( OO0O000 , OoO , I1I , iI , OOOo00Ooo00o0 )
elif IiI11i1IIiiI == 10056 :
 I1I1iiI1i ( "rmFavorite" )
 try :
  OO0O000 = OO0O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0O000 = OO0O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 O00oo0 ( OO0O000 )
elif IiI11i1IIiiI == 10057 :
 I1I1iiI1i ( "getFavorites" )
 i1I111II11 ( )
elif IiI11i1IIiiI == 10058 : I1iII1IIi1IiI ( )
elif IiI11i1IIiiI == 10059 : Donators_Guide ( )
elif IiI11i1IIiiI == 10060 : iiIiii1iI1i ( )
elif IiI11i1IIiiI == 10061 : III ( )
elif IiI11i1IIiiI == 10062 : iii1iI ( OO0O000 , OoO , OOOoO )
elif IiI11i1IIiiI == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif IiI11i1IIiiI == 10064 : O0oI1ii1Ii1 ( )
elif IiI11i1IIiiI == 10065 : OoO0 ( OoO )
elif IiI11i1IIiiI == 10066 : i1I111Ii ( OoO )
elif IiI11i1IIiiI == 10068 : IiIi1iIIi1 ( OoO )
elif IiI11i1IIiiI == 10069 : iII1111III1I ( OoO )
elif IiI11i1IIiiI == 10070 : O0OOoOOOO00O ( OoO )
elif IiI11i1IIiiI == 10071 : Genie_Watch ( )
elif IiI11i1IIiiI == 10072 : iiiii111 ( )
elif IiI11i1IIiiI == 10073 : Iii1iiIi1II1 ( OoO )
elif IiI11i1IIiiI == 10074 : I11iI1I ( OoO )
elif IiI11i1IIiiI == 10075 : oOOoO0O ( I1I , OO0O000 , OoO )
elif IiI11i1IIiiI == 10076 : OOOO0O00Ooooo ( OoO )
elif IiI11i1IIiiI == 10077 : I1IiiIiii1 ( OoO )
elif IiI11i1IIiiI == 10078 : ii11i1I1iiii ( )
elif IiI11i1IIiiI == 10079 : Genie_Watch_Tv_Shows ( )
elif IiI11i1IIiiI == 10080 : Genie_Watch_Tv_Genre ( OoO )
elif IiI11i1IIiiI == 10081 : Genie_Watch_TV_PlayRun ( OoO )
elif IiI11i1IIiiI == 10082 : Genie_Watch_TV_Episodes ( OoO , I1I )
elif IiI11i1IIiiI == 10083 : Genie_Watch_Tv_Recent ( OoO )
elif IiI11i1IIiiI == 10084 : OO00OO0O0 ( )
elif IiI11i1IIiiI == 10085 : oo0OOo0 ( )
elif IiI11i1IIiiI == 10086 : O0 ( )
elif IiI11i1IIiiI == 20000 : i1iIIi ( )
elif IiI11i1IIiiI == 20001 : OOO0O00 ( OoO )
elif IiI11i1IIiiI == 20002 : IIiIII11Ii ( OoO )
elif IiI11i1IIiiI == 20003 : iii1iII ( OoO )
elif IiI11i1IIiiI == 20004 : I1I1iiiiiIi1 ( OoO )
elif IiI11i1IIiiI == 20005 : IIIIiI1ii1 ( OoO )
elif IiI11i1IIiiI == 21004 : IiiiIiiI ( )
elif IiI11i1IIiiI == 21005 : ooO0 ( OoO )
elif IiI11i1IIiiI == 21006 : IIOoOOoOo ( OoO )
elif IiI11i1IIiiI == 21007 : ooOOo00o0ooO ( OoO )
elif IiI11i1IIiiI == 21008 : IiiiIIiIi1 ( OoO )
elif IiI11i1IIiiI == 21009 : o0o0O0O00oOOo ( OoO )
elif IiI11i1IIiiI == 30000 : oOo ( )
elif IiI11i1IIiiI == 30001 : i11II1 ( )
elif IiI11i1IIiiI == 100121 : Resolve ( OoO )
elif IiI11i1IIiiI == 30003 : oooooOoOO ( )
elif IiI11i1IIiiI == 30004 : iIIIIi11i ( OoO )
elif IiI11i1IIiiI == 30005 : Oo0Oo00O00o0 ( OoO )
elif IiI11i1IIiiI == 30006 : oOooooO ( )
elif IiI11i1IIiiI == 30007 : oOOo00ooO ( )
elif IiI11i1IIiiI == 30008 : iIiIi1i1Iiii ( OoO )
elif IiI11i1IIiiI == 30009 : IIiI ( OoO )
elif IiI11i1IIiiI == 30010 : o00O0O ( OoO )
elif IiI11i1IIiiI == 30011 : iI1i11i ( )
elif IiI11i1IIiiI == 30012 : oO0o0O ( )
elif IiI11i1IIiiI == 30013 : oOO0O0ooOOOo ( )
elif IiI11i1IIiiI == 30014 : iI111iIi ( )
elif IiI11i1IIiiI == 30015 : O00OOOo ( OoO , I1I , iI )
elif IiI11i1IIiiI == 30016 : o0oO ( OoO )
elif IiI11i1IIiiI == 30019 : iiI11111II ( OoO )
elif IiI11i1IIiiI == 30017 : O00O0 ( OoO )
elif IiI11i1IIiiI == 30018 : o0ooOOO0OO ( OoO )
elif IiI11i1IIiiI == 30030 : oooO0O0Oo00 ( )
elif IiI11i1IIiiI == 30031 : i1I1i1I111 ( )
elif IiI11i1IIiiI == 30032 : O0o ( )
elif IiI11i1IIiiI == 30033 : I1I1i ( )
elif IiI11i1IIiiI == 30034 : iIo0oOOO0 ( )
elif IiI11i1IIiiI == 30035 : O00Oo0OOOO0oOoo0 ( OoO )
elif IiI11i1IIiiI == 30036 : O0OIIII1i ( OoO )
elif IiI11i1IIiiI == 30037 : i1I1Iiii ( OoO )
elif IiI11i1IIiiI == 30038 : o0oo00O ( )
elif IiI11i1IIiiI == 30039 : oOOoo00O00o ( )
elif IiI11i1IIiiI == 50000 : oOo0OOoO0 ( )
elif IiI11i1IIiiI == 50001 : O0o00ooo ( )
elif IiI11i1IIiiI == 50002 : III1i1iI111I1 ( OoO )
elif IiI11i1IIiiI == 50003 : Table_Menu ( OOOoO )
elif IiI11i1IIiiI == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif IiI11i1IIiiI == 60001 : o0OoooO ( )
elif IiI11i1IIiiI == 60002 : Iii1iIiI1I1I1 ( OO0O000 )
elif IiI11i1IIiiI == 60003 : IiI11IIi11Iii ( OoO )
elif IiI11i1IIiiI == 600033 : oO00oooo0OOo ( OoO )
elif IiI11i1IIiiI == 60004 : o0OO0OO000OO ( OoO )
elif IiI11i1IIiiI == 50004 : o0OO0 ( )
elif IiI11i1IIiiI == 50005 : speedtest . runtest ( OoO )
elif IiI11i1IIiiI == 70001 : Oo00o00Oo ( )
elif IiI11i1IIiiI == 70002 : III1I11Iiii ( OoO )
elif IiI11i1IIiiI == 70003 : iIiI1i1Ii ( OoO )
elif IiI11i1IIiiI == 70004 : Oo0o00o ( OoO )
elif IiI11i1IIiiI == 70005 : III1I1 ( OoO )
elif IiI11i1IIiiI == 70006 : iI1IIIIII ( )
elif IiI11i1IIiiI == 50006 : o0OIiII ( i1 , i1111 )
elif IiI11i1IIiiI == 80000 : Ooo0OOo ( )
elif IiI11i1IIiiI == 80001 : resolvefilmon ( OoO )
elif IiI11i1IIiiI == 80002 : III11IiI ( )
elif IiI11i1IIiiI == 80003 : I1111o00o ( OO0O000 , OoO , "None" )
elif IiI11i1IIiiI == 80004 : I1iIIIiiii ( OO0O000 , OoO )
elif IiI11i1IIiiI == 80005 : IiIIIIIi ( )
elif IiI11i1IIiiI == 80006 : II111i1ii1iII ( OoO )
elif IiI11i1IIiiI == 80007 : ooo0OoO ( OoO )
elif IiI11i1IIiiI == 80008 : iiI1111I11i1I ( )
elif IiI11i1IIiiI == 80009 : oo0OOo ( )
elif IiI11i1IIiiI == 80010 : OOIiI1IIIiI1I1i ( OoO )
elif IiI11i1IIiiI == 80011 : OoO00O00O0 ( OoO )
elif IiI11i1IIiiI == 80012 : I11iIIi1Iii ( )
elif IiI11i1IIiiI == 90000 : O00O0O0 ( OO0O000 , OoO )
elif IiI11i1IIiiI == 90001 : tools ( )
elif IiI11i1IIiiI == 90002 : i1iI1 ( )
elif IiI11i1IIiiI == 90003 : oOooooo ( OoO )
elif IiI11i1IIiiI == 90004 : OO00 ( OoO )
elif IiI11i1IIiiI == 90005 : iI1iII1 ( OoO )
elif IiI11i1IIiiI == 90006 : oo0OooOoOo ( OoO )
elif IiI11i1IIiiI == 90007 : iIIii1i1iIiI ( OoO )
elif IiI11i1IIiiI == 90008 : O0oo ( OoO )
elif IiI11i1IIiiI == 90009 : iiIi ( OoO )
elif IiI11i1IIiiI == 90010 : ooo ( )
elif IiI11i1IIiiI == 90020 : oOOoOo0OoOO ( )
elif IiI11i1IIiiI == 90021 : hellyeah2 ( OoO )
elif IiI11i1IIiiI == 90022 : hellyeah3 ( OoO )
elif IiI11i1IIiiI == 90023 : II1i1III ( )
elif IiI11i1IIiiI == 90024 : IIiIii1III1i ( OoO )
elif IiI11i1IIiiI == 90025 : o0OO0Oo ( OoO )
if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif IiI11i1IIiiI == 90026 : iI1111i ( )
elif IiI11i1IIiiI == 90027 : I1iiIiIII ( OO0O000 , OoO , OOOoO )
elif IiI11i1IIiiI == 90028 : Oo0oOO0O00 ( OoO )
if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif IiI11i1IIiiI == 900300 : ooO ( )
elif IiI11i1IIiiI == 900301 : Ooo0oOooo0 ( OoO )
elif IiI11i1IIiiI == 900302 : II11IiIi11 ( OoO )
elif IiI11i1IIiiI == 90030 : OOo0 ( )
elif IiI11i1IIiiI == 90031 : I1III1111iIi ( )
elif IiI11i1IIiiI == 90032 : I1i111I ( OoO )
elif IiI11i1IIiiI == 90033 : OooOo0oo0O0o00O ( OoO )
elif IiI11i1IIiiI == 90034 : OOOooo ( OoO )
elif IiI11i1IIiiI == 90035 : o0OOo0o0O0O ( OoO )
elif IiI11i1IIiiI == 90036 : IIiIii1iiI ( OoO )
elif IiI11i1IIiiI == 90039 : o0oOOOOOO ( OoO )
elif IiI11i1IIiiI == 90037 : oooo ( OoO )
elif IiI11i1IIiiI == 900377 : II1i111 ( OoO )
elif IiI11i1IIiiI == 90038 : iii11II1I ( )
if 55 - 55: i1iIi - I11i
elif IiI11i1IIiiI == 10090 : iii11i1IIII ( )
elif IiI11i1IIiiI == 10091 : o000oo ( OoO )
elif IiI11i1IIiiI == 10092 : Ii1i111iI ( OoO )
elif IiI11i1IIiiI == 10093 : OooO0oO0Oo0 ( OoO , I1I )
elif IiI11i1IIiiI == 10094 : o0OO00oO00 ( OoO , I1I )
if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif IiI11i1IIiiI == 10095 : ii1i ( )
elif IiI11i1IIiiI == 10096 : oOoo0OooOOo00 ( OoO )
elif IiI11i1IIiiI == 10097 : o0oOOO0 ( OoO )
elif IiI11i1IIiiI == 10098 : I1iIIII1 ( OoO )
elif IiI11i1IIiiI == 10099 : II1 ( OoO )
if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif IiI11i1IIiiI == 10200 : iIi11i1 ( )
elif IiI11i1IIiiI == 10201 : iIi11ii ( OoO )
elif IiI11i1IIiiI == 10202 : I1iI1I1 ( OoO )
elif IiI11i1IIiiI == 10203 : RT4 ( OoO )
if 37 - 37: Iii
elif IiI11i1IIiiI == 90040 : OooooO ( )
elif IiI11i1IIiiI == 90041 : ii1IoO0O ( OoO )
elif IiI11i1IIiiI == 90042 : iiii11IiiiiIi ( OoO )
elif IiI11i1IIiiI == 90043 : oo0OoOOooO ( OoO )
elif IiI11i1IIiiI == 90044 : O0oOoo ( OoO )
elif IiI11i1IIiiI == 90045 : oOo0Oo0O0O ( )
elif IiI11i1IIiiI == 90046 : OoOOoO0O0oO ( OoO )
elif IiI11i1IIiiI == 90050 : oo0ooO0O0o ( )
elif IiI11i1IIiiI == 90051 : iiioOOOo ( OoO )
elif IiI11i1IIiiI == 90052 : OoOoO0OooOOo ( OoO )
elif IiI11i1IIiiI == 90053 : oooO00Oo ( OoO )
elif IiI11i1IIiiI == 90054 : I11i11I ( OoO )
elif IiI11i1IIiiI == 90055 : iIi11i ( )
if 19 - 19: ii % i1IiiiI1iI
elif IiI11i1IIiiI == 100001 : Stand_up ( )
if 57 - 57: OOooOOo + ooOoO0O00 . iI11I1II1I1I . iI11I1II1I1I / iI11I1II1I1I % i1i1I1IIii1II
elif IiI11i1IIiiI == 100003 : II1Ii1iI1i1 ( OoO )
elif IiI11i1IIiiI == 100004 : oOoO00 ( OoO )
elif IiI11i1IIiiI == 100005 : Resolve ( OoO )
elif IiI11i1IIiiI == 100008 : Search ( )
elif IiI11i1IIiiI == 100007 : OOOoooOo00oo0000OO ( OoO )
elif IiI11i1IIiiI == 100009 : yt . PlayVideo ( OoO )
elif IiI11i1IIiiI == 100010 : IIIii ( OoO )
elif IiI11i1IIiiI == 100100 : IIi1IIIIi ( I1I , OoO , O0oo0o0oO )
elif IiI11i1IIiiI == 100101 : IiIII1i1i ( OoO , OO0O000 , iI , O0oo0o0oO , I1I )
elif IiI11i1IIiiI == 100102 : o0O0O0 ( OO0O000 , OoO , I1I , iI )
elif IiI11i1IIiiI == 100106 : oO0O ( OoO , OO0O000 )
elif IiI11i1IIiiI == 100107 : I1i11II ( )
elif IiI11i1IIiiI == 100108 : iiIi1i1iIi1I ( )
elif IiI11i1IIiiI == 100109 : Iii11II ( OoO )
elif IiI11i1IIiiI == 40000 : IiiI1II1II1i ( )
elif IiI11i1IIiiI == 40001 : iIi11I11 ( OoO )
elif IiI11i1IIiiI == 100110 : IIiIi11iiIi ( )
elif IiI11i1IIiiI == 100111 : i11iI11I1I ( OoO )
elif IiI11i1IIiiI == 100110 : IIiIi11iiIi ( )
elif IiI11i1IIiiI == 100210 : ii1Ii1IiIIi ( OoO )
elif IiI11i1IIiiI == 100211 : iII1I11 ( )
elif IiI11i1IIiiI == 100212 : o0oOo00 ( )
elif IiI11i1IIiiI == 100213 : oOO0OOOOOo0Oo ( )
elif IiI11i1IIiiI == 100214 : o00000oo00 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
