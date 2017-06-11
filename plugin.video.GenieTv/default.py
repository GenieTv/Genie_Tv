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
IiiIII111iI = "3.5.3"
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
oO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
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
  o0OIiII ( 'Change Log 11/6/17 - v3.5.3' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORred]Following recent server issues some items are temporarily offline[/COLOR],[CR][COLORorangered]This is being worked on at top priority and will be back ASAP[/COLOR],[CR][COLORsteelblue]Items Affected[/COLOR],[CR][COLORsteelblue] StreamTeam[/COLOR],[CR][COLORsteelblue] G.O.D.S[/COLOR],[CR][COLORsteelblue]Boss Docs[/COLOR],[CR][COLORsteelblue]Search Lists[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 11/6/17 - v3.5.3' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORred]Following recent server issues some items are temporarily offline[/COLOR],[CR][COLORorangered]This is being worked on at top priority and will be back ASAP[/COLOR],[CR][COLORsteelblue]Items Affected[/COLOR],[CR][COLORsteelblue] StreamTeam[/COLOR],[CR][COLORsteelblue] G.O.D.S[/COLOR],[CR][COLORsteelblue]Boss Docs[/COLOR],[CR][COLORsteelblue]Search Lists[/COLOR],[CR]General Maintence' )
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
  if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
  if 96 - 96: ii + i1i1I1IIii1II
  if 44 - 44: i1i1I1IIii1II
  ii1I ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: OOooOOo / IIiIiII11i
  ii1I ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   ii1I ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
 else :
  if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
  if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
  if 42 - 42: I1ii11iIi11i
  if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
  if 46 - 46: I1ii11iIi11i
  if 1 - 1: IiI1i11I
  if 97 - 97: oooOo0oo0oo + IiI1i11I + o0o00Oo0O + Ii
  if 77 - 77: I11i / ii
  ii1I ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL2RvY3Mv' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  if 46 - 46: I11i % iI11I1II1I1I . IiI1i11I % IiI1i11I + Ii
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
 iI1i11iII111 ( 'movies' , 'MAIN' )
def oooooOOO000Oo ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  Ooo00OoOOO ( )
 if I111I1Iiii1i == 1 :
  Oo0OO0000oooo ( )
 if I111I1Iiii1i == 2 :
  IIII1iII ( )
 if I111I1Iiii1i == 3 :
  ii1III11 ( )
 if I111I1Iiii1i == 4 :
  I1iiIIIi11 ( )
 if I111I1Iiii1i == 5 :
  Ii1I11ii1i ( )
  if 89 - 89: IiI1i11I . o0o00Oo0O / Ii1I % OOooOOo . I1ii11iIi11i
  if 50 - 50: IIiIiII11i + Ii1I . ooOoO0O00 % I11i
def IIIi ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   O00OoO0o ( )
  if I111I1Iiii1i == 1 :
   i1i111iI ( )
  if I111I1Iiii1i == 2 :
   IIiiI ( OoO )
  if I111I1Iiii1i == 3 :
   III1i11 ( )
  if I111I1Iiii1i == 4 :
   iiI111 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if I111I1Iiii1i == 5 :
   I1iIiIi11i11 ( )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 52 - 52: i1iIi + o0o00Oo0O . IiI1i11I . Ii1I . oO0o
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def oo000ii ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 78 - 78: ii . oO0o + i1iIi - ooOoO0O00
 if 31 - 31: ii . oooOo0oo0oo
 if 83 - 83: IiI1i11I . o0o00Oo0O / I1ii11iIi11i / oooOo0oo0oo - IIiIiII11i
 if 100 - 100: oO0o
 if 46 - 46: OOooOOo / iI11I1II1I1I % IiI1i11I . iI11I1II1I1I * IiI1i11I
def IIi1ii1Ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OoOoO ( )
  if I111I1Iiii1i == 1 :
   o0ii1i ( )
  if I111I1Iiii1i == 2 :
   oOOoo ( )
  if I111I1Iiii1i == 3 :
   iII1111III1I ( )
  if I111I1Iiii1i == 4 :
   ii11i ( )
  if I111I1Iiii1i == 5 :
   O00oOo00o0o ( )
  if I111I1Iiii1i == 6 :
   O00oO0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 70 - 70: Iii . Ii1I * ii - III1iiIii * oOo0O0Ooo + OOooOOo
  if 10 - 10: I11i / Ii
  if 92 - 92: Iii . i1IiiiI1iI
  ii1I ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def oOO00O0Ooooo00 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   O000 = '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]'
   if 79 - 79: ii - oOo0O0Ooo
   if 69 - 69: Iii
   if 95 - 95: i1iIi + Ii * i1IiiiI1iI - ooOoO0O00 * i1IiiiI1iI - iI11I1II1I1I
   if 75 - 75: ii * III1iiIii
  oOo0O0Oo00oO = [ O000 , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RAIZ TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   I1Iiiiiii ( )
  if I111I1Iiii1i == 1 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , OO0O000 )
  if I111I1Iiii1i == 2 :
   IiiI1iiiiI1iI ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) )
  if I111I1Iiii1i == 3 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , iiiI1I1iIIIi1 , OO0O000 )
   if 43 - 43: i1i1I1IIii1II - ii
  if I111I1Iiii1i == 4 :
   ii1iI ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if I111I1Iiii1i == 5 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , OO0O000 )
 else :
  if 49 - 49: I11i . III1iiIii / oO0o + IIiIiII11i
  if 47 - 47: o0o00Oo0O / o0ii1I
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   ii1I ( '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'Roadrunner-Streams.png' , Oo00OOOOO , '' )
  if 67 - 67: oOo0O0Ooo
  if 55 - 55: Ii1I - IiI1i11I * I11i + OOooOOo * OOooOOo * o0o00Oo0O
  ii1I ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'pirate.png' , Oo00OOOOO , '' )
  if 91 - 91: i1IiiiI1iI - oooOo0oo0oo % iI11I1II1I1I - ii % i1iIi
  if 98 - 98: oO0o . oO0o * i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / III1iiIii
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 61 - 61: IIiIiII11i
def Ii1ii111i1 ( ) :
 iii ( )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def ii1iI ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 IiIi1I1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for OO0O000 , oOo0O , url in IIi :
  if '247ch' in url :
   oOoo000 ( OO0O000 , url , 10190 , oOo0O )
  elif '.m3u' in url :
   oOoo000 ( OO0O000 , url , 1019 , oOo0O )
  elif '.xml' in url :
   oOoo000 ( OO0O000 , url , 1018 , oOo0O )
  else :
   OooOo00o ( OO0O000 , url , 222 , oOo0O )
 for OO0O000 , url , oOo0O in i1Iii1i1I :
  if '.xml' in url :
   oOoo000 ( OO0O000 , url , 1018 , oOo0O )
  elif '.m3u' in url :
   oOoo000 ( OO0O000 , url , 1019 , oOo0O )
  else :
   OooOo00o ( OO0O000 , url , 222 , oOo0O )
 for OO0O000 , url , oOo0O in IiIi1I1 :
  OooOo00o ( OO0O000 , url , 8043 , oOo0O )
def IiI11i1IIiiI ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def OoOo00o0OO ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , oOo0O in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , oOo0O )
  if 1 - 1: oOo0O0Ooo % i1iIi
def oOoO00 ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 ii1I ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 ii1I ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 40 - 40: I11i
def OOOoooOo00oo0000OO ( url ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , o000O000 , ii1 , iI , oo0O0 in IIi :
  if ii1 == '123' :
   ii1 = iiIi1IIiIi + 'appstreams.png'
  if iI == '123' :
   iI = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   ii1I ( OO0O000 , url , 100010 , ii1 , iI , oo0O0 )
  elif 'playlist' in url :
   ii1I ( OO0O000 , url , 100007 , ii1 , iI , oo0O0 )
  elif 'watchseries' in url :
   ii1I ( OO0O000 , url , 100100 , ii1 , iI , oo0O0 )
  elif not 'http' in url :
   oOoO0o0ooo ( OO0O000 , url , 100009 , ii1 , iI , oo0O0 , '' )
  else :
   oOoO0o0ooo ( OO0O000 , url , 100005 , ii1 , iI , oo0O0 , '' )
   if 86 - 86: Ii1I * o0o00Oo0O * III1iiIii
def Ooo0oo ( url ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
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
   oOoO0o0ooo ( OO0O000 , url , 100009 , oOo0O , iI , oo0O0 , '' )
  else :
   oOoO0o0ooo ( OO0O000 , url , 100005 , oOo0O , iI , oo0O0 , '' )
   if 41 - 41: OOooOOo * Iii / OOooOOo % i1i1I1IIii1II
def IioO0oOOO0Ooo ( url ) :
 if 38 - 38: oOo0O0Ooo
 II11iIiIIIiI = O0oOOo0Oo ( url )
 oOo0OoOOo0 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in oOo0OoOOo0 :
  ii1 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for ii1 in ii1 :
   ii1 = ii1
  OO0O000 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for OO0O000 in OO0O000 :
   if 'elete' in OO0O000 :
    pass
   elif 'rivate Vid' in OO0O000 :
    pass
   else :
    OO0O000 = ( OO0O000 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iII11I1Ii1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( i1i1i1I ) )
  for iII11I1Ii1 in iII11I1Ii1 :
   iII11I1Ii1 = iII11I1Ii1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = url
  oOoO0o0ooo ( '[COLORred]' + str ( iII11I1Ii1 ) + '[/COLOR] : ' + str ( OO0O000 ) , str ( url ) , 100009 , str ( ii1 ) , Oo00OOOOO , '' , '' )
  iI1i11iII111 ( 'movies' , '' )
  if 92 - 92: Iii / Iii . Ii1I
  if 17 - 17: Ii - IIiIiII11i * I11i
  if 5 - 5: oooOo0oo0oo - oooOo0oo0oo . I1ii11iIi11i + OOooOOo - oooOo0oo0oo . i1i1I1IIii1II
  if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % Iii
def iiiI1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OoOOoOooooOOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , oo0O0 , iI , OO0O000 in OoOOoOooooOOo :
  if '.php' in url :
   ii1I ( OO0O000 , url , 100210 , oOo0O , iI , oo0O0 )
  else :
   i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iI , oo0O0 )
   if 50 - 50: oOo0O0Ooo * Ii
   if 68 - 68: oooOo0oo0oo * o0o00Oo0O . Iii - IIiIiII11i . i1iIi / IIiIiII11i
   if 47 - 47: ii
def ii1i1i1IiII ( iconimage , url , extra ) :
 ii1 = ' '
 O0o = ' '
 iI = ' '
 II11I = ' '
 oo0oOO00oO = O0oOOo0Oo ( url )
 ii1 = re . compile ( '<img src="(.+?)">' ) . findall ( oo0oOO00oO )
 for ii1 in ii1 :
  ii1 = ii1
 i11i1iIiii = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oo0oOO00oO )
 for iI in i11i1iIiii :
  iI = iI
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oo0oOO00oO )
 for url , II11I in IIi :
  II11I = 'S' + ( II11I ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  OOO00OO0oOo ( ( II11I ) . replace ( '  ' , '' ) , url , 100101 , ii1 , iI , O0o , '' )
  iI1i11iII111 ( 'Movies' , 'info' )
  if 35 - 35: IiI1i11I + i1iIi - i1i1I1IIii1II . IiI1i11I . III1iiIii
def oo0ooOO ( url , name , fanart , extra , iconimage ) :
 iI1IiIIiIIi = extra
 II11I = name
 oo0oOO00oO = O0oOOo0Oo ( url )
 ii1 = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oo0oOO00oO )
 for url , name , IiIi11Iii in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  IiIi11Iii = IiIi11Iii
  III1i1iI1 = name + ' - [COLORred]' + IiIi11Iii + '[/COLOR]'
  OOO00OO0oOo ( III1i1iI1 , url , 100102 , ii1 , fanart , 'Aired : ' + IiIi11Iii , III1i1iI1 )
  if 97 - 97: Iii - Ii
def i1iIi1II11 ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = O0oOOo0Oo ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , name in IIi :
  for iII1i11 in o00OO00OoO :
   if iII1i11 in OoO :
    URL = 'http://www.watchseriesgo.to/link/' + OoO
    oOoO0o0ooo ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  OOO00OO0oOo ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 11 - 11: IiI1i11I * o0ii1I - OOooOOo
  if 66 - 66: OOooOOo . Ii - IiI1i11I * I11i + ii * Ii1I
def oO0OO0 ( url , name ) :
 O00Oo = name
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  Ii1111IiIi ( url , O00Oo )
 for url in i1Iii1i1I :
  Ii1111IiIi ( url , O00Oo )
 for url in IiIi1I1 :
  Ii1111IiIi ( url , O00Oo )
  if 35 - 35: oooOo0oo0oo * I11i * oOo0O0Ooo % I1ii11iIi11i . OOooOOo
def Ii1111IiIi ( url , season_name ) :
 if 'daclips.in' in url :
  O00o00O ( url , season_name )
 elif 'filehoot.com' in url :
  ii1iii11i1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  I11Oo00oO0O ( url , season_name )
 elif 'vidspot.net' in url :
  OOooO ( url , season_name )
 elif 'vodlocker' in url :
  O00O0OO00oo ( url , season_name )
 elif 'vidto' in url :
  oOOO ( url , season_name )
  if 56 - 56: Ii1I
  if 26 - 26: ii % ii
def oOOO ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , OO0O000 in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 62 - 62: oooOo0oo0oo * i1IiiiI1iI / I1ii11iIi11i * I11i
  if 29 - 29: I1ii11iIi11i % oO0o % III1iiIii . I11i / ii * i1iIi
def I11Oo00oO0O ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , OO0O000 in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 54 - 54: o0o00Oo0O
def OOooO ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , OO0O000 in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 68 - 68: oO0o * I11i . i1iIi % i1i1I1IIii1II % i1IiiiI1iI
def O00O0OO00oo ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 75 - 75: OOooOOo
def O00o00O ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 34 - 34: o0o00Oo0O
def ii1iii11i1 ( url , season_name ) :
 II11iIiIIIiI = O0oOOo0Oo ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooOI111i1I1 ( iIIIII1iiiiII , season_name )
  if 80 - 80: ooOoO0O00 - I1ii11iIi11i / oO0o - Ii
def oooOI111i1I1 ( Link , season_name ) :
 if 'http:/' in Link :
  OO0O0o0o0 ( Link )
  if 31 - 31: o0ii1I
def iIIiI1I1i ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 O0O0OOooOO0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in O0O0OOooOO0 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 31 - 31: oOo0O0Ooo * i1i1I1IIii1II + ii - IiI1i11I / ii
def OOO00OO0oOo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if 31 - 31: i1i1I1IIii1II / III1iiIii * I11i . IIiIiII11i
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 89 - 89: o0o00Oo0O
 if 2 - 2: Ii1I . Ii1I + Ii1I * I11i
def oOoO0o0ooo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 100 - 100: I1ii11iIi11i % o0ii1I / Iii
def iIII11Ii ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 52 - 52: i1IiiiI1iI / i1iIi - Iii
def iIiI ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIIi1i1I11i . play ( url ) . strip ( )
 except : pass
 if 87 - 87: i1i1I1IIii1II + iI11I1II1I1I - ii
def OO0O0o0o0 ( url ) :
 iIIIi1i1I11i = xbmc . Player ( )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
 except : pass
 if 8 - 8: ii / Iii + ooOoO0O00 . IiI1i11I
def O0oOOo0Oo ( url ) :
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
  if 73 - 73: ooOoO0O00 + IiI1i11I . Ii
  if 5 - 5: i1i1I1IIii1II . Ii1I . IIiIiII11i . ii
  if 96 - 96: Ii - oooOo0oo0oo % o0o00Oo0O / oO0o
def Oo0OO0000oooo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   O0O0 ( )
  if I111I1Iiii1i == 1 :
   oo0OOOoOo ( )
  if I111I1Iiii1i == 2 :
   IIiiIIi1 ( )
  if I111I1Iiii1i == 3 :
   ooO000O ( )
  if I111I1Iiii1i == 4 :
   oOIII111iiIi1 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def ii1III11 ( ) :
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
 if 29 - 29: ii + o0ii1I % iI11I1II1I1I - oooOo0oo0oo . oOo0O0Ooo % I1ii11iIi11i
 if 16 - 16: III1iiIii / I1ii11iIi11i + oooOo0oo0oo / o0ii1I
 if 42 - 42: I1ii11iIi11i + IIiIiII11i - oOo0O0Ooo / Iii % III1iiIii
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   O0ooOOO = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + O0ooOOO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   I111I1Iiii1i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if I111I1Iiii1i == 0 :
    O0oiIiiiiI1II1I1 ( II1I )
    Ooo0OOoOoO0 ( )
   elif I111I1Iiii1i == 1 :
    OoO0ooO ( II1I )
  else :
   pass
   if 52 - 52: Ii / ooOoO0O00
def OoO0ooO ( addon ) :
 O0ooOOO = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 1 - 1: i1iIi
def O0oiIiiiiI1II1I1 ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOO0oo = os . path . join ( IIIII , 'default.py' )
 II1iIi1IiIii = open ( oOO0oo , "w+" )
 if 30 - 30: i1iIi % IiI1i11I * oooOo0oo0oo - Ii1I * o0ii1I % i1iIi
 II1iIi1IiIii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 II1iIi1IiIii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 II1iIi1IiIii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 46 - 46: Ii - o0o00Oo0O . i1i1I1IIii1II
 if 100 - 100: oOo0O0Ooo / I11i * IiI1i11I . o0o00Oo0O / oooOo0oo0oo
 if 83 - 83: i1IiiiI1iI
 if 48 - 48: IIiIiII11i * oooOo0oo0oo * i1IiiiI1iI
def IiiI1iiiiI1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1iiiIii11 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOoOOO000O0 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOo0 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url , II1i11I1 , iI , oo0O0 in i1iiiIii11 :
  if 'php' in url :
   ii1I ( OO0O000 , url , 90037 , II1i11I1 , iI , oo0O0 )
  elif OO0O000 == 'Search' :
   ii1I ( 'Search' , url , 90038 , II1i11I1 , iI , oo0O0 )
  else :
   i11I1II1I11i ( OO0O000 , url , 222 , II1i11I1 , iI , oo0O0 )
 for OO0O000 , oOo0O , url , iiIiIiII in OOoOOO000O0 :
  ii1I ( OO0O000 , url , 90037 , oOo0O , iiIiIiII , '' )
 for OO0O000 , oOo0O , url , iiIiIiII in IIi :
  ii1I ( OO0O000 , url , 90037 , oOo0O , iiIiIiII , '' )
 for OO0O000 , url , oOo0O , iiIiIiII in i1Iii1i1I :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iiIiIiII , '' )
 for OO0O000 , url , oOo0O , iiIiIiII in IiIi1I1 :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iiIiIiII , '' )
 for OO0O000 , url , oOo0O , iiIiIiII in I1i11 :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iiIiIiII , '' )
 for OO0O000 , url , oOo0O in oOo0 :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , '' , '' )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
def i1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , oOo0O , url , iiIiIiII in IIi :
  ii1I ( OO0O000 , url , 90037 , oOo0O , iiIiIiII , '' )
 for OO0O000 , url , oOo0O , iiIiIiII in i1Iii1i1I :
  i11I1II1I11i ( OO0O000 , url , 222 , oOo0O , iiIiIiII , '' )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
  if 28 - 28: Ii1I . ooOoO0O00
def iIIi ( ) :
 ooO00O00oOO = [ 'serialsearch' , 'moviesearch' ]
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 if IIII1ii == '' :
  pass
 else :
  for IiIIi1I1I11Ii in ooO00O00oOO :
   o0OO = Oo0o0000o0o0 + IiIIi1I1I11Ii + '.php'
   oo0oOO00oO = OooOoooOo ( o0OO )
   if oo0oOO00oO != 'Opened' :
    OoOOoOooooOOo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oo0oOO00oO )
    for OO0O000 , OoO , II1i11I1 , iI , oo0O0 in OoOOoOooooOOo :
     if IIII1ii in OO0O000 . lower ( ) :
      Oo = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in Oo :
       if iII1i11 == OoO :
        OO0O000 = '[COLORred]* [/COLOR]' + ( OO0O000 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        iiIiI = open ( OOOO0OOoO0O0 , "a" )
        iiIiI . write ( 'item="' + OO0O000 + '"\n' )
        iiIiI . close
      if 'php' in OoO :
       ii1I ( OO0O000 , OoO , 90037 , II1i11I1 , iI , oo0O0 )
      else :
       i11I1II1I11i ( OO0O000 , OoO , 222 , II1i11I1 , iI , oo0O0 )
       if 87 - 87: i1iIi - ii + Ii
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
   if 73 - 73: Iii * ii . o0o00Oo0O . III1iiIii
def o0oooO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ooOo = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for OoO , oOo0O , o0oO0OoO0 , OO0O000 in IIi :
  OooOo00o ( ( '[COLORgold]' + o0oO0OoO0 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + OoO , 90024 , oOo0O )
 for I1IIIii , OoO , oOo0O in ooOo :
  OooOo00o ( I1IIIii , 'http://www.tvcatchup.com' + OoO , 90024 , oOo0O )
 for OoO , oOo0O , OO0O000 in i1Iii1i1I :
  if 'Submit' in OO0O000 :
   pass
  elif '&lt;' in OO0O000 :
   pass
  else :
   i11I1II1I11i ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + OO0O000 + '[/COLOR]' , OoO , 90025 , 'http://www.djing.com' + oOo0O , Oo00OOOOO , '' )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def oOOOOOoOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 81 - 81: IIiIiII11i + Ii / IiI1i11I
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def oo00OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIIi1IIi ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 43 - 43: i1IiiiI1iI % IiI1i11I
def i1i111iI ( ) :
 if 69 - 69: IiI1i11I % oO0o
 if 86 - 86: i1i1I1IIii1II / i1i1I1IIii1II
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
 if 72 - 72: ii / oOo0O0Ooo + o0ii1I / OOooOOo * o0ii1I
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
 if 25 - 25: Iii + OOooOOo . I11i % OOooOOo * oooOo0oo0oo
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if 'yr' in OoO :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + OoO , 10201 , iiIi1IIiIi + 'rated.png' )
   if 32 - 32: Ii - i1IiiiI1iI
def oo00ooOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iii1IIIiiiI , url , OO0O000 in IIi :
  if 'id' in url :
   oOoo000 ( ( '[COLORred]RANK [COLORblue]' + iii1IIIiiiI + '[COLORred] - [COLORblue]' + OO0O000 + '[/COLOR]' ) , OO0O000 , 10202 , iiIi1IIiIi + 'rated.png' )
   if 94 - 94: o0o00Oo0O - Iii - iI11I1II1I1I % i1iIi / o0ii1I % IiI1i11I
def iIi1IIi1ii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 I11Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1 = ( url )
 IIII1ii = I1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1
 i1iiIIi1I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 45 - 45: i1iIi % I11i - i1iIi
 i1i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oO0ooOoO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 59 - 59: o0o00Oo0O % I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 O0o00O0Oo0 = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0I11iII = O00O0oOO00O00 ( ooOo0OoO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiIiI = O00O0oOO00O00 ( i1iiIIi1I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIIIIiiIii = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 58 - 58: I1ii11iIi11i
 if 9 - 9: iI11I1II1I1I % Ii1I . oooOo0oo0oo + ii
 Oo0o = O00O0oOO00O00 ( i1i1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 oOOoOoo0O0 = O00O0oOO00O00 ( oO0ooOoO )
 if 45 - 45: Ii
 if 82 - 82: o0ii1I + III1iiIii
 if 12 - 12: i1IiiiI1iI
 if 93 - 93: Ii % iI11I1II1I1I % Ii + I11i / I11i / IIiIiII11i
 if 49 - 49: oooOo0oo0oo . Ii1I . Ii - IIiIiII11i / o0ii1I
 if 62 - 62: oooOo0oo0oo
 if 1 - 1: III1iiIii / III1iiIii - Ii
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * III1iiIii / I11i
 if 19 - 19: i1IiiiI1iI + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
 if 16 - 16: i1i1I1IIii1II + i1iIi / I11i
 if 82 - 82: III1iiIii * Ii % IIiIiII11i - ii
 if 90 - 90: I1ii11iIi11i . i1i1I1IIii1II * ooOoO0O00 - ooOoO0O00
 if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . III1iiIii % Iii / I11i
 if iIIIIiiIii != 'Failed' :
  Ii11iI1ii1111 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIiiIii )
  for url , OO0O000 in Ii11iI1ii1111 :
   i111i1i = O00O0oOO00O00 ( url )
   IiIii1I1I = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i111i1i )
   for OO0Oooo0oo , I1i111IiIiIi1 in IiIii1I1I :
    I1i111IiIiIi1 = ( I1i111IiIiIi1 . replace ( '.' , ' ' ) )
    if IIII1ii in I1i111IiIiIi1 . lower ( ) :
     if '.mkv' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.mp4' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.avi' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.wav' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 222 , '' , '' , '' )
     else :
      ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 39 - 39: Iii - Ii1I
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 53 - 53: I11i % IiI1i11I + i1iIi . I1ii11iIi11i - Ii1I % I11i
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 64 - 64: IIiIiII11i
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi1I1i , OO0O000 in IiIi1I1 :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1i1IIIIIIIi + iIIIiIi1I1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in I1i11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if O0o00O0Oo0 != 'Failed' :
  OooOOOO0O0 = [ ]
  oOo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o00O0Oo0 )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in oOo0 :
   if I1 in OO0O000 . lower ( ) :
    if OO0O000 in OooOOOO0O0 :
     pass
    else :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
     OooOOOO0O0 . append ( OO0O000 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0I11iII != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0I11iII )
  for url , oOo0O , OO0O000 in i1IIi1i1Ii1 :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , oOo0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 45 - 45: iI11I1II1I1I . i1i1I1IIii1II / OOooOOo / III1iiIii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: III1iiIii
    if 24 - 24: oO0o + i1i1I1IIii1II . I11i / i1i1I1IIii1II
    if 56 - 56: iI11I1II1I1I . Ii - oooOo0oo0oo * IIiIiII11i * i1IiiiI1iI
    if 5 - 5: oooOo0oo0oo / oooOo0oo0oo - Ii1I
    if 79 - 79: Ii1I + i1IiiiI1iI
    if 10 - 10: I1ii11iIi11i + o0o00Oo0O
    if 43 - 43: iI11I1II1I1I / IIiIiII11i % I11i - oooOo0oo0oo
    if 62 - 62: Iii
    if 63 - 63: oooOo0oo0oo + i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
    if 3 - 3: IiI1i11I . i1iIi % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
    if 29 - 29: I11i / Ii / oOo0O0Ooo % i1i1I1IIii1II % Ii
    if 18 - 18: oooOo0oo0oo + i1IiiiI1iI
    if 80 - 80: i1i1I1IIii1II + I11i * o0ii1I + oO0o
    if 75 - 75: Iii / I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
    if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
    if 50 - 50: i1iIi + ooOoO0O00
 if Oo0o != 'Failed' :
  i11IiIIi11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0o )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in i11IiIIi11I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 78 - 78: III1iiIii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % i1IiiiI1iI . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - III1iiIii
    if 33 - 33: oOo0O0Ooo / oO0o
    if 12 - 12: IIiIiII11i
    if 2 - 2: ooOoO0O00 - oOo0O0Ooo + Iii . IIiIiII11i
    if 25 - 25: i1i1I1IIii1II
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: Ii1I - IiI1i11I
    if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
 i1II11Iii1I = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 92 - 92: oooOo0oo0oo % III1iiIii % OOooOOo
 for IiIIi1I1I11Ii in i1II11Iii1I :
  o0OO = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  iIIIIiiIii = O00O0oOO00O00 ( o0OO )
  if iIIIIiiIii != 'Failed' :
   Ii11iI1ii1111 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIiiIii )
   for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in Ii11iI1ii1111 :
    if I1 in OO0O000 . lower ( ) :
     i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 4 - 4: OOooOOo + o0ii1I / i1i1I1IIii1II
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 13 - 13: IiI1i11I
 i1II11Iii1I = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 80 - 80: o0ii1I - I11i
 if 41 - 41: I11i - I1ii11iIi11i * oOo0O0Ooo
 for IiIIi1I1I11Ii in i1II11Iii1I :
  o0OO = I11Ii + IiIIi1I1I11Ii
  OO0OoOo0OOO = O00O0oOO00O00 ( o0OO )
  if OO0OoOo0OOO != 'Failed' :
   Ii1ii11IIIi = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OO0OoOo0OOO )
   for iIIIiIi1I1i , OO0O000 in Ii1ii11IIIi :
    if I1 in OO0O000 . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( I11Ii + IiIIi1I1I11Ii + iIIIiIi1I1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 82 - 82: i1i1I1IIii1II * iI11I1II1I1I . I11i . Ii1I + oooOo0oo0oo / oOo0O0Ooo
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: i1IiiiI1iI / i1iIi + o0o00Oo0O + i1iIi . iI11I1II1I1I + IIiIiII11i
def ii11i ( ) :
 oOoo000 ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 oOoo000 ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 oOoo000 ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 oOoo000 ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 37 - 37: Iii . I1ii11iIi11i % III1iiIii * ooOoO0O00
def oOOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , II11I , i11i11 , IiIi11Iii , i1iiIII1IIiIIII in IIi :
  oOoo000 ( ( '[COLORblue]' + OO0O000 + '[/COLOR] [COLORred]Season[/COLOR]-' + II11I + ' [COLORred]Returns [/COLOR]- ' + i1iiIII1IIiIIII + ' ' + IiIi11Iii ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 19 - 19: IiI1i11I - I11i / I11i + I1ii11iIi11i
def OoO0o0000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , II11I , i11i11 in IIi :
  oOoo000 ( ( '[COLORblue]' + OO0O000 + '[/COLOR] [COLORred]Season[/COLOR]-' + II11I + ' [COLORred] Status Unknown[/COLOR] ' ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 8 - 8: OOooOOo . i1iIi % i1i1I1IIii1II . oOo0O0Ooo % oOo0O0Ooo . o0ii1I
def I1I11ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , II11I , i11i11 , IiIi11Iii in IIi :
  oOoo000 ( ( '[COLORblue]' + OO0O000 + ' [COLORred] Cancelled On[/COLOR] ' + IiIi11Iii ) , OO0O000 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / IiI1i11I * i1i1I1IIii1II
def i1iii1ii ( url ) :
 I1 = ( url )
 IIII1ii = I1 . lower ( )
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 OO0Oooo0oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I1 ) . replace ( ' ' , '+' )
 iIiII = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
 i1iiIIi1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 i11II = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 71 - 71: III1iiIii . i1IiiiI1iI . oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 68 - 68: Ii % i1i1I1IIii1II * oO0o * III1iiIii * IIiIiII11i + o0o00Oo0O
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 66 - 66: Iii % Ii1I % ii
 if 34 - 34: I11i / IiI1i11I % o0o00Oo0O . oO0o . ooOoO0O00
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( OO0Oooo0oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 OO0OoOo0OOO = O00O0oOO00O00 ( I1III11iiii11i1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 29 - 29: o0o00Oo0O . i1IiiiI1iI
 if 66 - 66: i1i1I1IIii1II * iI11I1II1I1I % iI11I1II1I1I * III1iiIii - i1iIi - III1iiIii
 IiiIiI = O00O0oOO00O00 ( i1iiIIi1I )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 iIIIIiiIii = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 o0O0oO0 = O00O0oOO00O00 ( i11II )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 77 - 77: o0o00Oo0O . o0ii1I
 if iIIIIiiIii != 'Failed' :
  Ii11iI1ii1111 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIiiIii )
  for url , OO0O000 in Ii11iI1ii1111 :
   i111i1i = O00O0oOO00O00 ( url )
   IiIii1I1I = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i111i1i )
   for OO0Oooo0oo , I1i111IiIiIi1 in IiIii1I1I :
    if IIII1ii in I1i111IiIiIi1 . lower ( ) :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , url + OO0Oooo0oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 39 - 39: i1iIi . IIiIiII11i
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IiiIiI != 'Failed' :
  iIiIi1iI11iiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIiI )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in iIiIi1iI11iiI :
   if IIII1ii in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 26 - 26: iI11I1II1I1I * i1IiiiI1iI - oooOo0oo0oo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
    if 55 - 55: i1iIi
    if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
    if 64 - 64: I11i . o0o00Oo0O * o0ii1I + ii - I1ii11iIi11i . ii
    if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
    if 55 - 55: IiI1i11I - oO0o
    if 100 - 100: o0o00Oo0O
    if 79 - 79: iI11I1II1I1I
    if 81 - 81: oooOo0oo0oo + iI11I1II1I1I * i1IiiiI1iI - iI11I1II1I1I . oooOo0oo0oo
    if 48 - 48: Iii . ii . oOo0O0Ooo . OOooOOo % Ii1I / IiI1i11I
    if 11 - 11: ooOoO0O00 % oO0o % IiI1i11I
 if o0O0oO0 != 'Failed' :
  O0Oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0O0oO0 )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in O0Oo0 :
   if IIII1ii in OO0O000 . lower ( ) :
    oOoo000 ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , iiiI1I1iIIIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . oooOo0oo0oo + oO0o - i1IiiiI1iI
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  iI1iIiiiI1I1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , oOo0O , OO0O000 , OOOOOo in i1Iii1i1I :
   if IIII1ii in OO0O000 . lower ( ) :
    if 'season' in OOOOOo :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , oOo0O , oOo0O , '' )
    if 'episodes' in OOOOOo :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , oOo0O , oOo0O , '' )
  for url in iI1iIiiiI1I1 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 50 - 50: o0ii1I - Ii + iI11I1II1I1I / o0o00Oo0O - o0ii1I + I11i
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
  for url , OO0O000 , oOo0O in OOoOOO000O0 :
   if IIII1ii in OO0O000 . lower ( ) :
    ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( OO0O000 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , oOo0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 22 - 22: IIiIiII11i - o0ii1I / i1iIi % ii + oooOo0oo0oo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: oO0o / IiI1i11I + Ii % Iii
    if 93 - 93: OOooOOo % iI11I1II1I1I
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
    if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
    if 21 - 21: oooOo0oo0oo
    if 6 - 6: III1iiIii
    if 46 - 46: III1iiIii + i1i1I1IIii1II
    if 79 - 79: ii - III1iiIii * III1iiIii . OOooOOo
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OO0O000 in IiIi1I1 :
   if IIII1ii in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i1i1IIIIIIIi + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 100 - 100: IIiIiII11i * Iii % oOo0O0Ooo / Ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OO0O000 in I1i11 :
   if IIII1ii in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oo0o0oOo + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 90 - 90: Ii1I . i1iIi . OOooOOo . o0ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OO0OoOo0OOO != 'Failed' :
  Ii1ii11IIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoOo0OOO )
  for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in Ii1ii11IIIi :
   if IIII1ii in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 4 - 4: o0ii1I + OOooOOo % Ii1I / Ii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + III1iiIii % Ii % OOooOOo
 O0OOO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IiIIi1I1I11Ii in O0OOO0 :
  o0OO = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  Oo0o = O00O0oOO00O00 ( o0OO )
  if Oo0o != 'Failed' :
   i11IiIIi11I = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo0o )
   for OO0O000 , oo0O0 , url , oOo0O , iI , o000O000 in i11IiIIi11I :
    if IIII1ii in OO0O000 . lower ( ) :
     ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , url , o000O000 , oOo0O , iI , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 8 - 8: Ii / IIiIiII11i + I11i * o0ii1I % III1iiIii . Iii
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 6 - 6: III1iiIii % I1ii11iIi11i . I1ii11iIi11i - Ii1I / Iii . ooOoO0O00
     if 99 - 99: OOooOOo . i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: Iii / I1ii11iIi11i / oooOo0oo0oo / o0o00Oo0O / OOooOOo + I11i
def IIiI1111i1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  oOoo000 ( ( OO0O000 ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + OoO , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + OoO )
def ii1ii1I1IIi1 ( url ) :
 oOOoo0 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( oOOoo0 )
 sys . exit ( 1 )
 if 24 - 24: oO0o - i1i1I1IIii1II + Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
def oO00o ( ) :
 if 36 - 36: i1IiiiI1iI . IIiIiII11i % i1iIi
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
 oOoo000 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 oOoo000 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 37 - 37: I1ii11iIi11i / III1iiIii * o0o00Oo0O
def o0o00O0oOooO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , o0oO0OO00ooOO in IIi :
  oOoo000 ( ( OO0O000 + ' - ' + o0oO0OO00ooOO ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 5 - 5: oOo0O0Ooo * OOooOOo - Ii . i1iIi / IiI1i11I
def III1iii1i1II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  oOoo000 ( OO0O000 , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 87 - 87: oooOo0oo0oo + I11i . IiI1i11I - ii
def iiiiI1IiI1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  oOoo000 ( OO0O000 , url , 90054 , oOo0O )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 19 - 19: o0ii1I
def O0o00oO0oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , o0oO0OO00ooOO , url , OO0O000 , iiiii1I1III1 in IIi :
  ii1I ( o0oO0OO00ooOO + ' - ' + OO0O000 + ' - ' + iiiii1I1III1 , url , 90044 , oOo0O , oOo0O , '' )
 for oOo0O , OO0O000 , url in i1Iii1i1I :
  oOoo000 ( OO0O000 , url , 90044 , oOo0O , oOo0O , '' )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 12 - 12: IiI1i11I . OOooOOo * oOo0O0Ooo
def II1I1i1i1iii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 IIII1ii = i1i11ii1Ii . lower ( )
 II11iIiIIIiI = OooOoooOo ( IIII1ii )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , OOOOOo in IIi :
  if 'season' in OOOOOo :
   oOoo000 ( OO0O000 , OoO , 90054 , oOo0O , oOo0O , '' )
  if 'episodes' in OOOOOo :
   oOoo000 ( OO0O000 , OoO , 90044 , oOo0O , oOo0O , '' )
 for OoO in next :
  oOoo000 ( 'NEXT' , OoO , 90053 , iiIi1IIiIi + 'Next.png' )
  if 12 - 12: oooOo0oo0oo . o0ii1I
def O0oO ( ) :
 if 10 - 10: i1IiiiI1iI * ii + Iii - Ii1I / Ii1I . Ii
 if 22 - 22: i1IiiiI1iI / I11i
 if 98 - 98: ooOoO0O00
 if 51 - 51: Ii1I + i1iIi + I1ii11iIi11i / ooOoO0O00 + ooOoO0O00
 if 12 - 12: iI11I1II1I1I . o0ii1I . Ii1I % oOo0O0Ooo . IIiIiII11i . i1i1I1IIii1II
 if 32 - 32: Ii1I + III1iiIii / o0o00Oo0O / OOooOOo * ii % i1iIi
 if 50 - 50: oO0o
 if 66 - 66: iI11I1II1I1I
 if 41 - 41: i1IiiiI1iI . o0o00Oo0O * oOo0O0Ooo * Ii1I
 if 100 - 100: IiI1i11I
 oOoo000 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 oOoo000 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 oOoo000 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 73 - 73: Ii1I % IIiIiII11i
def OOOOOooOOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , o0oO0OO00ooOO in IIi :
  if 'genre' in url :
   oOoo000 ( ( OO0O000 + ' - ' + o0oO0OO00ooOO ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 6 - 6: oooOo0oo0oo
def ooOoo000oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if 'release' in url :
   oOoo000 ( OO0O000 , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 50 - 50: III1iiIii + I11i
def o0OoOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , O0Oo0iI1II1III1 , url , oo0O0 in IIi :
  ii1I ( OO0O000 + ' ' + O0Oo0iI1II1III1 , url , 90044 , oOo0O , oOo0O , oo0O0 )
 for oOo0O , OO0O000 , OOOOOo , url , oooo0O0o0OoOO , oo0O0 in i1Iii1i1I :
  if 'movies' in OOOOOo :
   ii1I ( OO0O000 + ' - ' + oooo0O0o0OoOO , url , 90044 , oOo0O , oOo0O , oo0O0 )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 36 - 36: i1i1I1IIii1II / i1IiiiI1iI - oOo0O0Ooo . oOo0O0Ooo
def i1I1i1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oO0o0O ( 'http:' + url )
  if 51 - 51: i1i1I1IIii1II + oO0o + IiI1i11I + IiI1i11I % I11i
def oO0o0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  OooOo00o ( ( OO0O000 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def iIi1i1iIi1Ii1 ( ) :
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - Iii * i1IiiiI1iI + i1i1I1IIii1II - oO0o % Ii1I
 if 63 - 63: iI11I1II1I1I + oooOo0oo0oo . oO0o / oOo0O0Ooo
 if 84 - 84: ooOoO0O00
 if 42 - 42: IIiIiII11i - oO0o - ii . IiI1i11I / OOooOOo
 if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
 if 81 - 81: III1iiIii / OOooOOo * III1iiIii . o0o00Oo0O
 if 61 - 61: oO0o * oooOo0oo0oo + i1IiiiI1iI . iI11I1II1I1I % Iii . i1IiiiI1iI
 if 53 - 53: i1IiiiI1iI * III1iiIii / iI11I1II1I1I / oOo0O0Ooo % Ii1I
 if 39 - 39: oO0o / ii . oO0o * Ii1I / OOooOOo
 if 38 - 38: oO0o / i1iIi % i1IiiiI1iI * Iii + Ii % i1iIi
 if 61 - 61: i1IiiiI1iI - o0ii1I % Ii1I / i1iIi / IiI1i11I + iI11I1II1I1I
 if 87 - 87: i1IiiiI1iI + i1iIi + o0o00Oo0O / ooOoO0O00 % III1iiIii / i1IiiiI1iI
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 IIII1ii = i1i11ii1Ii . lower ( )
 II11iIiIIIiI = OooOoooOo ( IIII1ii )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , OOo000OO000 in IIi :
  if 'movies' in OOo000OO000 :
   oOoo000 ( OOo000OO000 + '-' + OO0O000 , OoO , 90044 , oOo0O )
 for OoO in next :
  o0OoOOo ( OoO )
  if 83 - 83: I11i % i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
def III1i11 ( ) :
 oOoo000 ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 80006 , iiIi1IIiIi + 'Desi.png' )
def OoOOoooO000 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  OooOo00o ( OO0O000 , url , 80007 , oOo0O )
 for url , oOo0O , OO0O000 in IIi :
  oOoo000 ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def OoO0o000oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  OooO0OO ( url )
def Oo00OO00o0oO ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'http://www.join4films.com/?s=' + ( I1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 IIII1ii = i1i11ii1Ii . lower ( )
 OoOOoooO000 ( IIII1ii )
 if 43 - 43: I1ii11iIi11i . i1IiiiI1iI
 if 12 - 12: i1IiiiI1iI + oooOo0oo0oo + Iii . III1iiIii / o0ii1I
 if 29 - 29: III1iiIii . i1iIi - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / i1i1I1IIii1II
 if 91 - 91: OOooOOo % iI11I1II1I1I . oOo0O0Ooo
 if 70 - 70: Iii % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / i1IiiiI1iI
 if 100 - 100: Ii1I * Ii % i1i1I1IIii1II / I1ii11iIi11i / i1iIi + Ii1I
 if 59 - 59: i1IiiiI1iI - III1iiIii
 if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
 if 5 - 5: III1iiIii
 if 84 - 84: IIiIiII11i * i1i1I1IIii1II * IIiIiII11i % III1iiIii / oOo0O0Ooo
 if 100 - 100: III1iiIii . o0ii1I - iI11I1II1I1I . Ii / IIiIiII11i
 if 71 - 71: i1IiiiI1iI * I1ii11iIi11i . Iii
 if 49 - 49: III1iiIii * o0o00Oo0O . III1iiIii
 if 19 - 19: IIiIiII11i - III1iiIii
 if 59 - 59: I11i * oO0o - o0ii1I . oooOo0oo0oo
 if 89 - 89: oooOo0oo0oo
def o00oo0OO0 ( ) :
 ii1I ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 ii1I ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 60 - 60: i1iIi
def O000O ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'http://imoviemax.se/?s=' + ( I1 ) . replace ( ' ' , '+' )
 IIII1ii = i1i11ii1Ii . lower ( )
 iiii1IIi1 ( IIII1ii )
def oo0o0OoOO0o0 ( url ) :
 III1III11II = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , iIi1iI in IIi :
  if OO0O000 in III1III11II :
   pass
  else :
   ii1I ( OO0O000 + ' - ' + iIi1iI + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   III1III11II . append ( OO0O000 )
   if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . i1IiiiI1iI
def Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , iIiiiIiIi in IIi :
  ii1I ( OO0O000 + ' - Views:' + iIiiiIiIi , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 19 - 19: III1iiIii . Ii1I / OOooOOo
  if 68 - 68: i1iIi / ii * Iii / i1i1I1IIii1II
def iiii1IIi1 ( url ) :
 ooooO000 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  ii1I ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  ii1I ( OO0O000 , url , 10075 , oOo0O , oOo0O , '' )
  ooooO000 . append ( OO0O000 )
  if 61 - 61: i1iIi - oooOo0oo0oo + oooOo0oo0oo
def iiiIiIIII1iiIIi ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for i1I1IiI1ii , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  O00OOoOOOO00O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + O00OOoOOOO00O
  Ooo0OOO = ( i1I1IiI1ii ) . replace ( 'play-' , 'Server ' )
  i11I1II1I11i ( Ooo0OOO , O00OOoOOOO00O , 10076 , img , img , '' )
  if 94 - 94: Ii % ii / oOo0O0Ooo
def iII1Iii11111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for iIiII in IIi :
  if '=m' in iIiII :
   OOo00ooOoO0o ( iIiII )
  elif 'php' in iIiII :
   iII1Iii11111 ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( iIiII )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for i1i1IIIIIIIi in IIi :
    OOo00ooOoO0o ( iIiII )
    if 21 - 21: Ii
    if 89 - 89: IiI1i11I . Ii * o0o00Oo0O
    if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
def iI111II1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0ooO00ooOO0o = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11Iii , o0OI1II in O0ooO00ooOO0o :
  print 'there ><><><><><><><><><><><><'
  IiIi11Iii = IiIi11Iii
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OI1II ) )
  for OO0O000 , iIIi1Ii1III in IIi :
   print 'here <><><><><><><><><><><><>'
   ii1I ( '[COLORred]' + IiIi11Iii + '[/COLOR] - ' + OO0O000 + ' - [COLOR' + ooOoOoo0O + ']' + iIIi1Ii1III + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 i1i1i1I = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11Iii , Oooo00 in i1i1i1I :
  print 'there ><><><><><><><><><><><><'
  IiIi11Iii = IiIi11Iii
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oooo00 ) )
  for OO0O000 , iIIi1Ii1III in IIi :
   print 'here <><><><><><><><><><><><>'
   ii1I ( '[COLORred]' + IiIi11Iii + '[/COLOR] - ' + OO0O000 + ' - [COLOR' + ooOoOoo0O + ']' + iIIi1Ii1III + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 9 - 9: ii * o0o00Oo0O
   if 76 - 76: i1IiiiI1iI - i1i1I1IIii1II . oooOo0oo0oo % I11i
   if 30 - 30: Ii1I % Iii / i1IiiiI1iI
def O00oO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for OO0O000 in OO0O000 :
   OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for ii1 in ii1 :
   ii1 = 'http:' + ii1
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , '' , '' )
  if 1 - 1: i1IiiiI1iI - Iii
  if 45 - 45: o0ii1I - oooOo0oo0oo
  if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . Iii % i1iIi . IIiIiII11i
  if 10 - 10: o0ii1I - Ii . Ii1I % ooOoO0O00
def iiI111 ( url ) :
 if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - oooOo0oo0oo . iI11I1II1I1I
 I111I1I = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiII , oOo0O , OO0O000 , Oo0000 in IIi :
  OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( iIiII )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for O0O0OOooOO0 , O0o in i1Iii1i1I :
   oO0OoOo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( O0o ) )
   for oo0O0 in oO0OoOo :
    if OO0O000 in I111I1I :
     pass
    else :
     i11I1II1I11i ( OO0O000 , O0O0OOooOO0 , 8043 , oOo0O , oOo0O , oo0O0 )
     iI1i11iII111 ( 'movies' , 'INFO' )
     I111I1I . append ( OO0O000 )
     if 89 - 89: I1ii11iIi11i + Ii1I - I11i
     if 40 - 40: oO0o + oO0o
def o0oo0o00ooO00 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , iiiI1I1iIIIi1 , oo0O0 , iI , OO0O000 in IIi :
  ii1I ( OO0O000 , url , 10065 , iiiI1I1iIIIi1 , iI , oo0O0 )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 37 - 37: oO0o - Ii1I . ii . i1iIi + OOooOOo / o0ii1I
def I1oOoO0OOO00O ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'https://www.youtube.com/results?search_query=' + ( I1 ) . replace ( ' ' , '+' )
 IIII1ii = i1i11ii1Ii . lower ( )
 II11iIiIIIiI = OooOoooOo ( IIII1ii )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for OoO in next :
  OoO = 'https://www.youtube.com' + OoO
  ii1I ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , OoO , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oOo0O , OoO , OO0O000 , OOOOO0o0OOo , O0o in IIi :
  OOO00 . append ( OO0O000 )
  iI1i11iII111 ( 'tvshows' , 'INFO' )
  ii1 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ii1
  OoO = 'http://www.youtube.com' + OoO
  i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , ii1 , O0o )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOo0O , OoO , OO0O000 , OOOOO0o0OOo in IIi :
   print 'im doing it'
   iI1i11iII111 ( 'tvshows' , 'INFO' )
   ii1 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
   OoO = 'http://www.youtube.com' + OoO
   if '&' in OoO :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( OoO )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for OO0O000 in OO0O000 :
      OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     OoO = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for OoO in OoO :
      OoO = 'https://www.youtube.com/w' + OoO
     ii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for ii1 in ii1 :
      ii1 = 'http:' + ii1
     i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , Oo00OOOOO , '' )
   elif OO0O000 in OOO00 :
    pass
   elif 'user' in OoO or 'elete' in OO0O000 :
    pass
   elif 'hannel' in OoO :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + OoO
    II11iIiIIIiI = OooOoooOo ( OoO )
    I11I11I11IiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oOo0O , OoO , OO0O000 in I11I11I11IiIi :
     if 'outube' in OoO or 'list' in OoO :
      pass
     elif 'atch' in OoO :
      OoO = ( OoO ) . replace ( '/watch?v=' , '' )
      i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0O , 'http:' + oOo0O , '' )
     else :
      pass
   else :
    i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , ii1 , '' )
    if 62 - 62: Ii1I . OOooOOo / iI11I1II1I1I * i1IiiiI1iI
def ii11I1IIi1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  ii1I ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for oOo0O , url , OO0O000 , OOOOO0o0OOo , O0o in IIi :
  OOO00 . append ( OO0O000 )
  iI1i11iII111 ( 'tvshows' , 'INFO' )
  ii1 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ii1
  url = 'http://www.youtube.com' + url
  i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , ii1 , O0o )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOo0O , url , OO0O000 , OOOOO0o0OOo in IIi :
   iI1i11iII111 ( 'tvshows' , 'INFO' )
   ii1 = 'http:' + ( oOo0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     OO0O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for OO0O000 in OO0O000 :
      OO0O000 = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for ii1 in ii1 :
      ii1 = 'http:' + ii1
     i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , Oo00OOOOO , '' )
   elif OO0O000 in OOO00 :
    pass
   elif 'user' in url or 'elete' in OO0O000 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    I11I11I11IiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for oOo0O , url , OO0O000 in I11I11I11IiIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0O , 'http:' + oOo0O , '' )
     else :
      pass
   else :
    i11I1II1I11i ( '[COLORred]' + OOOOO0o0OOo + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 , ii1 , '' )
    if 44 - 44: oOo0O0Ooo * iI11I1II1I1I / o0o00Oo0O
    if 17 - 17: IIiIiII11i
    if 9 - 9: ii + i1i1I1IIii1II
def iIiI1ii ( ) :
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 76 - 76: o0ii1I + iI11I1II1I1I + OOooOOo . oO0o
def i1i1o0oOoOo0 ( ) :
 ivuesetup . iVueInt ( )
 if 38 - 38: I11i % i1IiiiI1iI + Ii + IiI1i11I + i1iIi / Ii
def o0OOOOOo0 ( ) :
 oooOoO ( )
 return
 if 62 - 62: oooOo0oo0oo / IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
def oooOoO ( ) :
 if 2 - 2: Ii - i1IiiiI1iI + oO0o % Iii * o0ii1I
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 Ooo000O00 = II1I . getSetting ( id = 'User' )
 i1iI1Iiii1I = II1I . getSetting ( id = 'Pass' )
 I1iII = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 Iii1I1IIII = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 OooooOoO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 o00OoOO0O0 = "http://piesustv.net:8000/get.php?username=" + Ooo000O00 + "&password=" + i1iI1Iiii1I + "&type=m3u_plus&output=ts"
 I1i1II1 = "http://piesustv.net:8000/xmltv.php?username=" + Ooo000O00 + "&password=" + i1iI1Iiii1I + "&type=m3u_plus&output=ts"
 if 89 - 89: oO0o / oO0o
 xbmc . executeJSONRPC ( I1iII )
 xbmc . executeJSONRPC ( Iii1I1IIII )
 xbmc . executeJSONRPC ( OooooOoO )
 if 1 - 1: Ii1I . Ii
 OooooOo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 OooooOo . setSetting ( id = 'm3uUrl' , value = o00OoOO0O0 )
 OooooOo . setSetting ( id = 'epgUrl' , value = I1i1II1 )
 OooooOo . setSetting ( id = 'm3uCache' , value = "false" )
 OooooOo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def IIIiiiIiI ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 80 - 80: i1i1I1IIii1II % i1i1I1IIii1II % o0o00Oo0O - Ii . IiI1i11I / o0o00Oo0O
if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / o0ii1I . ooOoO0O00
if 60 - 60: I1ii11iIi11i . III1iiIii % oOo0O0Ooo - i1IiiiI1iI
def oooOo ( ) :
 if 79 - 79: i1i1I1IIii1II - IIiIiII11i
 if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / o0ii1I * oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
 if 84 - 84: ii + i1IiiiI1iI / oOo0O0Ooo % oooOo0oo0oo % Ii1I * oOo0O0Ooo
 if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / i1i1I1IIii1II
 if 24 - 24: oOo0O0Ooo * ooOoO0O00 % i1iIi / o0o00Oo0O + Ii
 if 12 - 12: Ii1I / o0ii1I
 if 5 - 5: ii
 if 18 - 18: oOo0O0Ooo % ii - IiI1i11I . Ii * I1ii11iIi11i % o0ii1I
 if 12 - 12: ooOoO0O00 / oooOo0oo0oo % i1iIi * III1iiIii * o0o00Oo0O * iI11I1II1I1I
 if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * i1i1I1IIii1II . ii
 if 54 - 54: o0o00Oo0O / III1iiIii % i1iIi * ooOoO0O00 * o0o00Oo0O
 if OO0o == "insert_username" :
  IIOOOoO00O = iIiii1Ii1I1II ( )
  iIIIIII = IIiiIiII11iiiiiii ( )
  I11 ( 'User' , IIOOOoO00O )
  I11 ( 'Pass' , iIIIIII )
  xbmc . executebuiltin ( 'Container.Refresh' )
  O0000 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( IIOOOoO00O , iIIIIII )
  O0000 = OooOoooOo ( O0000 )
  if O0000 == "" :
   OoOOOOOO = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   oo0OO0 = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   O0oo00o = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , OoOOOOOO , oo0OO0 , O0oo00o )
   oooOo ( )
  else :
   OoOOOOOO = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   oo0OO0 = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   O0oo00o = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % IIOOOoO00O )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , OoOOOOOO , oo0OO0 , O0oo00o )
   xbmc . executebuiltin ( 'Container.Refresh' )
   IIi1i1 ( )
 else :
  IIi1i1 ( )
def iIiii1Ii1I1II ( ) :
 o0O0Ooo = xbmc . Keyboard ( '' , 'heading' , True )
 o0O0Ooo . setHeading ( 'Enter Username' )
 o0O0Ooo . setHiddenInput ( False )
 o0O0Ooo . doModal ( )
 if ( o0O0Ooo . isConfirmed ( ) ) :
  O0oO00oOOooO = o0O0Ooo . getText ( )
  return O0oO00oOOooO
 else :
  return False
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
  if 66 - 66: o0o00Oo0O
def IIiiIiII11iiiiiii ( ) :
 o0O0Ooo = xbmc . Keyboard ( '' , 'heading' , True )
 o0O0Ooo . setHeading ( 'Enter Password' )
 o0O0Ooo . setHiddenInput ( False )
 o0O0Ooo . doModal ( )
 if ( o0O0Ooo . isConfirmed ( ) ) :
  O0oO00oOOooO = o0O0Ooo . getText ( )
  return O0oO00oOOooO
 else :
  return False
def oOooOOo00ooO ( ) :
 o00OoOO0O0 = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  o0OO0oooo = urllib2 . urlopen ( o00OoOO0O0 )
  print o0OO0oooo . getcode ( )
  o0OO0oooo . close ( )
  if 40 - 40: i1IiiiI1iI - OOooOOo * Iii - III1iiIii / OOooOOo
  pass
  if 71 - 71: i1i1I1IIii1II / ii % III1iiIii / OOooOOo % i1IiiiI1iI
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def IIi1i1 ( ) :
 iii ( )
 if 19 - 19: i1IiiiI1iI + III1iiIii / i1i1I1IIii1II / IIiIiII11i
 if 92 - 92: ooOoO0O00 % i1iIi + i1iIi - iI11I1II1I1I . o0ii1I
 ii1I ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 33 - 33: I11i / o0o00Oo0O + oooOo0oo0oo
 if 75 - 75: III1iiIii % Ii + iI11I1II1I1I
 if 92 - 92: OOooOOo % o0o00Oo0O
 if 55 - 55: iI11I1II1I1I * IiI1i11I
def ooIi11iI ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 ii111I11Ii = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 i11IiiI1Ii1 = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 O0000 = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 O0000 = OooOoooOo ( O0000 )
 if not O0000 == "" :
  I1iiIiiIiiI = 'https://tinyurl.com/create.php?source=indexpage&url=' + ii111I11Ii + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( I1iiIiiIiiI ) )
  oOoO = 'https://tinyurl.com/create.php?source=indexpage&url=' + i11IiiI1Ii1 + '&submit=Make+TinyURL%21&alias='
  ii111I11Ii = OooOoooOo ( I1iiIiiIiiI )
  i11IiiI1Ii1 = OooOoooOo ( oOoO )
  xbmc . log ( str ( i11IiiI1Ii1 ) )
  ii1IIii = IiI11i1I11111 ( ii111I11Ii , '<div class="indent"><b>' , '</b>' )
  Ii1IIIIIIiI1 = IiI11i1I11111 ( i11IiiI1Ii1 , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % ii1IIii , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % Ii1IIIIIIiI1 )
 else :
  return
def Ii11IiIiiii1 ( ) :
 oOooOOo00ooO ( )
 OooO0O0Ooo ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , oO0O + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( IIIiIi1iiI )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  ii1I ( ( '[COLORsteelblue]' + OO0O000 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , OoO , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def iI1 ( url ) :
 open = OooOoooOo ( o0Iiii + url )
 I1i1I = i1111iI1 ( open , '<channel>' , '</channel>' )
 for Oo0oOOOOo in I1i1I :
  if '<playlist_url>' in open :
   OO0O000 = IiI11i1I11111 ( Oo0oOOOOo , '<title>' , '</title>' )
   OO0Oooo0oo = IiI11i1I11111 ( Oo0oOOOOo , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   ii1I ( str ( base64 . b64decode ( OO0O000 ) ) . replace ( '?' , '' ) , OO0Oooo0oo , 3 , icon , iI , '' )
  else :
   OO0O000 = IiI11i1I11111 ( Oo0oOOOOo , '<title>' , '</title>' )
   OO0O000 = base64 . b64decode ( OO0O000 )
   iiiO000OOO = IiI11i1I11111 ( Oo0oOOOOo , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = IiI11i1I11111 ( Oo0oOOOOo , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   oo0O0 = IiI11i1I11111 ( Oo0oOOOOo , '<description>' , '</description>' )
   oo0O0 = base64 . b64decode ( oo0O0 )
   o0IIi1 = IiI11i1I11111 ( oo0O0 , 'PLOT:' , '\n' )
   O00O00o = IiI11i1I11111 ( oo0O0 , 'CAST:' , '\n' )
   I11IiI1iI = IiI11i1I11111 ( oo0O0 , 'RATING:' , '\n' )
   O0OO0OoO = IiI11i1I11111 ( oo0O0 , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   O0OO0OoO = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( O0OO0OoO )
   o0OOo = IiI11i1I11111 ( oo0O0 , 'DURATION_SECS:' , '\n' )
   IiI1Ii11Ii = IiI11i1I11111 ( oo0O0 , 'GENRE:' , '\n' )
   OoO0oO0oo0O ( str ( OO0O000 ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , iiiO000OOO , iI , o0IIi1 , str ( O0OO0OoO ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( O00O00o ) . split ( ) , I11IiI1iI , o0OOo , IiI1Ii11Ii )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 82 - 82: ii . o0ii1I
III1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
iII1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 76 - 76: Ii1I
def ooO000OO ( ) :
 o00OoOO0O0 = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  o0OO0oooo = urllib2 . urlopen ( o00OoOO0O0 )
  print o0OO0oooo . getcode ( )
  o0OO0oooo . close ( )
  if 43 - 43: i1iIi * i1IiiiI1iI % oooOo0oo0oo
  pass
  if 38 - 38: I1ii11iIi11i
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 34 - 34: OOooOOo
 OoO = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 OoO0o00OOOOO ( OoO , iII1ii + "uide.xml" )
 if 19 - 19: IiI1i11I * I1ii11iIi11i . IiI1i11I . oO0o / oO0o - i1i1I1IIii1II
 oooO = open ( III1ii , 'r+' )
 input = open ( III1ii ) . read ( ) . decode ( 'UTF-8' )
 i11111iiiII1I = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 oooO . write ( i11111iiiII1I )
 oooO . truncate ( )
 oooO . close ( )
 I1I1i ( )
 if 45 - 45: oooOo0oo0oo
def I1I1i ( ) :
 open = OooOoooOo ( iIiI1i111ii )
 all = i1111iI1 ( open , '{"num' , 'direct' )
 for Oo0oOOOOo in all :
  if '"tv_archive":1' in Oo0oOOOOo :
   OO0O000 = IiI11i1I11111 ( Oo0oOOOOo , '"epg_channel_id":"' , '"' )
   iiiO000OOO = IiI11i1I11111 ( Oo0oOOOOo , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = IiI11i1I11111 ( Oo0oOOOOo , 'stream_id":"' , '"' )
   OO0O000 = OO0O000 . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   ii1I ( OO0O000 , id , 90027 , iiiO000OOO , iI , OO0O000 )
   if 48 - 48: iI11I1II1I1I . Iii - oooOo0oo0oo . i1IiiiI1iI * i1i1I1IIii1II % i1i1I1IIii1II
   if 38 - 38: I1ii11iIi11i % Ii1I - IiI1i11I * iI11I1II1I1I / o0o00Oo0O
def I1iI11IiiI11i ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 IIIiIIIi11I = open ( III1ii )
 II1O0o00 = ElementTree . parse ( IIIiIIIi11I )
 I1I1i1i = "apples"
 import datetime as dt
 from datetime import time
 Oo0oOO0O00 = datetime . now ( ) - timedelta ( days = 5 )
 IiIi11Iii = str ( Oo0oOO0O00 )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 o00OOo0o0O = II1O0o00 . findall ( "programme" )
 for I111Iii1 in o00OOo0o0O :
  if name in I111Iii1 . attrib . get ( 'channel' ) :
   i11i = I111Iii1 . attrib . get ( 'start' )
   O0o0O00o0o , II1IIiiI1 , O00O00 = i11i . partition ( ' +' )
   IiIi11Iii = str ( IiIi11Iii ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   O0OO0OoO , oOooO0OoO , i1iiIII1IIiIIII = i11i . partition ( '2017' )
   o0oOOOOoo0 = I111Iii1 . find ( 'title' ) . text + i11i
   i1iiIII1IIiIIII = i1iiIII1IIiIIII [ : - 6 ]
   if O0o0O00o0o > IiIi11Iii :
    if O0o0O00o0o < I1IIIii :
     ooOO0OOO00o = O0o0O00o0o
     ooOO0OOO00o = ooOO0OOO00o [ : 4 ] + '/' + ooOO0OOO00o [ 4 : ]
     O0o0O00o0o = O0o0O00o0o [ : 4 ] + '-' + O0o0O00o0o [ 4 : ]
     ooOO0OOO00o = ooOO0OOO00o [ : 7 ] + '/' + ooOO0OOO00o [ 7 : ]
     O0o0O00o0o = O0o0O00o0o [ : 7 ] + '-' + O0o0O00o0o [ 7 : ]
     ooOO0OOO00o = ooOO0OOO00o [ : 10 ] + ' - ' + ooOO0OOO00o [ 10 : ]
     O0o0O00o0o = O0o0O00o0o [ : 10 ] + ':' + O0o0O00o0o [ 10 : ]
     ooOO0OOO00o = ooOO0OOO00o [ : 15 ] + ':' + ooOO0OOO00o [ 15 : ]
     O0o0O00o0o = O0o0O00o0o [ : 13 ] + '-' + O0o0O00o0o [ 13 : ]
     ooOO0OOO00o = ooOO0OOO00o [ : - 2 ]
     O0o0O00o0o = O0o0O00o0o [ : - 2 ]
     OoOoO0ooooO0 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( O0o0O00o0o ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     I1I1i1i = OoOoO0ooooO0 + str ( O0o0O00o0o ) + "&duration=240"
     ooOO0OOO00o = '[COLOR blue]%s - [/COLOR]' % ooOO0OOO00o
     o0oOOOOoo0 = str ( ooOO0OOO00o ) + I111Iii1 . find ( 'title' ) . text
     oo0O0 = I111Iii1 . find ( 'desc' ) . text
     i11I1II1I11i ( o0oOOOOoo0 , OoOoO0ooooO0 , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , oo0O0 )
def IIII1ii1 ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 iiIIIiIii = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 iiIIIiIii . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 iiIIIiIii . setProperty ( 'IsPlayable' , 'true' )
 iiIIIiIii . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
def OoO0o00OOOOO ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 OOO0O0OOo = time . time ( )
 urllib . urlretrieve ( url , dest , lambda Iii1 , OOoO , i1IiiI : O0OOO0o0O ( Iii1 , OOoO , i1IiiI , o0oOoO00o , OOO0O0OOo ) )
def O0OOO0o0O ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  IiIIi1iiI = min ( numblocks * blocksize * 100 / filesize , 100 )
  o0ooOO00OO0o0O = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  III1IiiIiiI1i = numblocks * blocksize / ( time . time ( ) - start_time )
  if III1IiiIiiI1i > 0 :
   OoO0o00OoO = ( filesize - numblocks * blocksize ) / III1IiiIiiI1i
  else :
   OoO0o00OoO = 0
  III1IiiIiiI1i = III1IiiIiiI1i / 1024
  Oo00Oooo00o = III1IiiIiiI1i / 1024
  II11II1I = float ( filesize ) / ( 1024 * 1024 )
  O0OO00000o00 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( o0ooOO00OO0o0O )
  II1iI1I11I = '[COLOR white]Speed:  %.02f Mb/s ' % Oo00Oooo00o + '[/COLOR]'
  dp . update ( IiIIi1iiI , O0OO00000o00 , II1iI1I11I )
 except :
  IiIIi1iiI = 100
  dp . update ( IiIIi1iiI )
 if dp . iscanceled ( ) :
  OOO000Oo = xbmcgui . Dialog ( )
  OOO000Oo . ok ( "GenieTv" , 'The download was cancelled.' )
  if 8 - 8: i1iIi - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * o0ii1I - iI11I1II1I1I
  sys . exit ( )
  dp . close ( )
  if 30 - 30: Iii / Ii1I
def iI1iIIIIIiIi1 ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iIi ( )
  if 52 - 52: iI11I1II1I1I
  if 49 - 49: oooOo0oo0oo
  if 23 - 23: oO0o / IiI1i11I / iI11I1II1I1I
  if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / Iii + i1IiiiI1iI
  if 17 - 17: oooOo0oo0oo + IIiIiII11i
  if 43 - 43: Iii % o0ii1I / I11i * i1IiiiI1iI
  if 85 - 85: iI11I1II1I1I . ii . I11i
  if 77 - 77: oOo0O0Ooo % i1iIi
def iIi ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for OoO in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def oO0oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 o00o0o000Oo = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOoOOO000O0 = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiIi1I1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1i11 = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOo0 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 Ii1ii11IIIi = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 i1IIi1i1Ii1 = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 Oooo00OOo = iIiIIOooOO ( )
 iio0oo0Oo = i1i1I1II ( )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in o00o0o000Oo :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOoOOO000O0 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1i11 :
  dt = datetime . fromtimestamp ( float ( I1i11 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   OooOo00o ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiIi1I1 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOo0 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Ii1ii11IIIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1IIi1i1Ii1 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + Oooo00OOo , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + iio0oo0Oo , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 66 - 66: III1iiIii + iI11I1II1I1I
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 75 - 75: Ii1I
def O00o ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 o0o0ooOo00 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 91 - 91: oO0o * i1IiiiI1iI % oO0o . I11i * Ii1I . oooOo0oo0oo
def i111I111 ( data ) :
 I1Iiii = len ( data ) % 4
 if 22 - 22: o0ii1I * Iii + oOo0O0Ooo - Iii / Ii1I
 if 18 - 18: ooOoO0O00
 if 4 - 4: III1iiIii
 if 93 - 93: i1i1I1IIii1II % ooOoO0O00
 if 83 - 83: oOo0O0Ooo . I1ii11iIi11i - Iii . I11i
 if 73 - 73: oOo0O0Ooo - IiI1i11I . IiI1i11I
 if I1Iiii != 0 :
  data += b'=' * ( 4 - I1Iiii )
 return base64 . decodestring ( data )
def IiI11i1I11111 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : I1I1 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : I1I1 = ''
 else :
  try : I1I1 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : I1I1 = ''
 return I1I1
 if 78 - 78: Iii . oooOo0oo0oo + i1i1I1IIii1II * IiI1i11I - ooOoO0O00
 if 27 - 27: o0ii1I % ooOoO0O00 . I1ii11iIi11i % i1IiiiI1iI
def i1111iI1 ( text , start_with , end_with ) :
 I1I1 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return I1I1
def iIiIIOooOO ( ) :
 i1iI = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 i1iI . connect ( ( '8.8.8.8' , 0 ) )
 i1iI = i1iI . getsockname ( ) [ 0 ]
 return i1iI
 if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
def i1i1I1II ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 Oooo00OOo = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( Oooo00OOo . group ( ) )
oO0O = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
iIiI1i111ii = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
IiI11IIi11Iii = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
ii11i1I1i = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
Iiiii1I = '&action=get_live_categories'
IiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
IIIiIi1iiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 84 - 84: i1IiiiI1iI
o0Iiii = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
iIio0oooo0OOo00 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
OOO0 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
I1Ii1 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 67 - 67: Iii % Ii . iI11I1II1I1I * oOo0O0Ooo - Iii + o0ii1I
def i1ii1iIi ( ) :
 oOooOOo00ooO ( )
 open = OooOoooOo ( OOO0 )
 I1i1I = i1111iI1 ( open , '<channel>' , '</channel>' )
 for Oo0oOOOOo in I1i1I :
  OO0O000 = IiI11i1I11111 ( Oo0oOOOOo , '<title>' , '</title>' )
  OO0O000 = base64 . b64decode ( OO0O000 )
  OO0Oooo0oo = IiI11i1I11111 ( Oo0oOOOOo , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ii1I ( '[COLORsteelblue]' + OO0O000 + '[/COLOR]' , OO0Oooo0oo , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 43 - 43: o0ii1I + IiI1i11I + ooOoO0O00 - OOooOOo + I11i
def OOOO00 ( url ) :
 open = OooOoooOo ( I1Ii1 + url )
 I1i1I = i1111iI1 ( open , '<channel>' , '</channel>' )
 for Oo0oOOOOo in I1i1I :
  OO0O000 = IiI11i1I11111 ( Oo0oOOOOo , '<title>' , '</title>' )
  OO0O000 = base64 . b64decode ( OO0O000 )
  xbmc . log ( str ( OO0O000 ) )
  iiiO000OOO = IiI11i1I11111 ( Oo0oOOOOo , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OO0Oooo0oo = IiI11i1I11111 ( Oo0oOOOOo , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oo0O0 = IiI11i1I11111 ( Oo0oOOOOo , '<description>' , '</description>' )
  oo0O0 = base64 . b64decode ( oo0O0 )
  o0I1iI111ii111i = '('
  o00iI1Ii11iIiiI1 = ')'
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , OO0Oooo0oo , 222 , iiiO000OOO , iI , ( '[COLOR' + ooOoOoo0O + ']' + oo0O0 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( o00iI1Ii11iIiiI1 , '[COLORsteelblue]' ) . replace ( o0I1iI111ii111i , '[COLORorangered]' ) )
  if 15 - 15: Iii % oooOo0oo0oo
def i11ii1 ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( IiI + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , type , iIiII , II1i11I1 in IIi :
  i1i1IIIIIIIi = ( ii11i1I1i + iIiII + '.m3u8' ) . strip ( )
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , i1i1IIIIIIIi , 222 , ( II1i11I1 ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
def Ii111I11 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i111IiIiIi1 , Oo0O0oo in IIi :
  if name == I1i111IiIiIi1 :
   i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + Oo0O0oo , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def o0O0 ( name ) :
 oO0o0 = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , oOo0O , OoO in IIi :
  OoO = ( OoO ) . replace ( '.ts' , '.m3u8' )
  i11I1II1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( OoO ) . strip ( ) , 222 , oOo0O , oOo0O , '' )
 else :
  i11I1II1I11i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 65 - 65: o0o00Oo0O . i1i1I1IIii1II
  if 85 - 85: IIiIiII11i
  if 55 - 55: Ii1I
  if 76 - 76: i1i1I1IIii1II - Ii
  if 27 - 27: Ii1I - Ii % i1IiiiI1iI / I1ii11iIi11i . I1ii11iIi11i / ii
  if 76 - 76: Iii * oO0o . iI11I1II1I1I % ii % Ii1I
  if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * Iii
  if 89 - 89: o0ii1I - i1iIi . Iii - i1IiiiI1iI - oOo0O0Ooo
  if 79 - 79: III1iiIii + III1iiIii + o0ii1I
  if 39 - 39: o0o00Oo0O - ii
  if 63 - 63: iI11I1II1I1I % I11i * i1iIi
  if 79 - 79: o0o00Oo0O
def iiIiii1iI1i ( ) :
 ii1I ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  ii1I ( 'Backup Genie Favourites' , OoO , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  ii1I ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  ii1I ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 32 - 32: IIiIiII11i . o0o00Oo0O + o0ii1I / OOooOOo / III1iiIii / oooOo0oo0oo
  if 15 - 15: Ii1I
  if 4 - 4: III1iiIii + iI11I1II1I1I * IiI1i11I + I1ii11iIi11i * I11i % IIiIiII11i
zip = oo00 . getSetting ( 'zip' )
OO0o0o0oo = xbmc . translatePath ( os . path . join ( zip ) )
def iIiII1 ( ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 47 - 47: Iii
  if 92 - 92: ii % oOo0O0Ooo / OOooOOo * OOooOOo % Ii / ii
  if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
def i11iIiiIi11I ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  iIiII1 ( )
  oo0O0oOOO0o = open ( url ) . read ( )
  oOo0Oo0Oo0 = os . path . join ( OO0o0o0oo , description . split ( 'Your ' ) [ 1 ] )
  oooO = open ( oOo0Oo0Oo0 , mode = 'w' )
  oooO . write ( oo0O0oOOO0o )
  oooO . close ( )
 else :
  if 'guisettings.xml' in description :
   Oo0oOOOOo = open ( os . path . join ( OO0o0o0oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1I1 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( I1I1 ) . findall ( Oo0oOOOOo )
   for type , OooOo0o0OO , iiI1ii1IIiI in IIi :
    iiI1ii1IIiI = iiI1ii1IIiI . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OooOo0o0OO , iiI1ii1IIiI ) )
  else :
   oOo0Oo0Oo0 = os . path . join ( url )
   oo0O0oOOO0o = open ( os . path . join ( OO0o0o0oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooO = open ( oOo0Oo0Oo0 , mode = 'w' )
   oooO . write ( oo0O0oOOO0o )
   oooO . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 35 - 35: Ii1I * IiI1i11I . III1iiIii . III1iiIii - i1i1I1IIii1II % OOooOOo
 if 42 - 42: I11i - iI11I1II1I1I % ii
 if 43 - 43: I11i - I1ii11iIi11i
 if 85 - 85: IIiIiII11i + i1IiiiI1iI - i1iIi * iI11I1II1I1I % i1i1I1IIii1II
def o00oOOo ( ) :
 iIIii1I111iIii1i1 = 1
 iIiII1 ( )
 o0Oo = xbmc . translatePath ( os . path . join ( OO0o0o0oo , 'Build Backup' , 'Full Backup' , '' ) )
 i1II11i1iI1 = xbmc . translatePath ( os . path . join ( OO0o0o0oo , 'Build Backup' , 'my_full_backup.zip' ) )
 OO0 = xbmc . translatePath ( os . path . join ( OO0o0o0oo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( o0Oo ) :
  os . makedirs ( o0Oo )
 IIi1II11 = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IIi1II11 ) : return False , 0
 o0ooOOOo = IIi1II11
 OO = xbmc . translatePath ( os . path . join ( o0Oo , o0ooOOOo + '.zip' ) )
 oOOo0oO = [ 'plugin.video.GenieTv' ]
 I1Ii1IIIiII = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iiII1IIii1i1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i1iiiIIi11II = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0oooOo0oo = "Creating full backup of existing build"
 i1iI1IIi1I = "Creating Community Build"
 oo00i1i11I1I1 = "Archiving..."
 OOOOOoooO = ""
 oO0Oooo0OoO = "Please Wait"
 Iiii1IIIIiiI11 ( oOo0oooo00o , OO , i1iI1IIi1I , oo00i1i11I1I1 , OOOOOoooO , oO0Oooo0OoO , iiII1IIii1i1 , i1iiiIIi11II )
 time . sleep ( 1 )
 I1iii1I = xbmc . translatePath ( os . path . join ( o0Oo , o0ooOOOo + '_guisettings.zip' ) )
 oooII111 = zipfile . ZipFile ( I1iii1I , mode = 'w' )
 try :
  oooII111 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oooII111 . close ( )
 if iIIii1I111iIii1i1 == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i1II11i1iI1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OO + '[/COLOR]' )
  if 29 - 29: III1iiIii + Ii * o0o00Oo0O - IiI1i11I . IIiIiII11i % o0ii1I
def Iiii1IIIIiiI11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 III1I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OOOii = len ( sourcefile )
 Iii1I11 = [ ]
 O0o0o = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for IiiiIi1111I , iII1i1ii , i1I1ii1i in os . walk ( sourcefile ) :
  for file in i1I1ii1i :
   O0o0o . append ( file )
 iiiiII11iIi = len ( O0o0o )
 for IiiiIi1111I , iII1i1ii , i1I1ii1i in os . walk ( sourcefile ) :
  iII1i1ii [ : ] = [ OO00 for OO00 in iII1i1ii if OO00 not in exclude_dirs ]
  i1I1ii1i [ : ] = [ oooO for oooO in i1I1ii1i if oooO not in exclude_files ]
  for file in i1I1ii1i :
   Iii1I11 . append ( file )
   Oooo = len ( Iii1I11 ) / float ( iiiiII11iIi ) * 100
   o0oOoO00o . update ( int ( Oooo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O00 = os . path . join ( IiiiIi1111I , file )
   if not 'temp' in iII1i1ii :
    if not 'plugin.program.originwizard' in iII1i1ii :
     import time
     IiIIIIi = '01/01/1980'
     OoIIiIIIII1I = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O00 ) ) )
     if OoIIiIIIII1I > IiIIIIi :
      III1I . write ( O00 , O00 [ OOOii : ] )
 III1I . close ( )
 o0oOoO00o . close ( )
 if 96 - 96: Ii . IIiIiII11i
 if 7 - 7: ooOoO0O00
def Oo00oo ( ) :
 iii ( )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 79 - 79: Ii1I / o0o00Oo0O % I11i
 if 71 - 71: i1IiiiI1iI / oOo0O0Ooo / o0o00Oo0O
def IiIii11I ( ) :
 iii ( )
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  O00OoO0o ( )
 if I111I1Iiii1i == 1 :
  OoOoO ( )
 if I111I1Iiii1i == 2 :
  O0O0 ( )
 if I111I1Iiii1i == 3 :
  I1oOoO0OOO00O ( )
  if 97 - 97: ooOoO0O00 + IiI1i11I . i1iIi - IiI1i11I
  if 53 - 53: o0o00Oo0O . oOo0O0Ooo
  if 74 - 74: i1iIi % OOooOOo / I1ii11iIi11i
  if 2 - 2: III1iiIii % III1iiIii % i1IiiiI1iI
  if 60 - 60: oooOo0oo0oo
  if 73 - 73: i1iIi
  if 86 - 86: OOooOOo . Iii / I1ii11iIi11i * Iii
  if 20 - 20: i1iIi - oooOo0oo0oo * oO0o * I11i * oooOo0oo0oo / III1iiIii
  if 40 - 40: oOo0O0Ooo * I11i . oOo0O0Ooo
def o00o0O0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   IiiI1iiiiI1iI ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if I111I1Iiii1i == 1 :
   IiiI1iiiiI1iI ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if I111I1Iiii1i == 2 :
   iIIii1iiiIiiI ( )
  if I111I1Iiii1i == 3 :
   oOo0Ooo0 ( )
  if I111I1Iiii1i == 4 :
   IiiII1iiiiI1i ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if I111I1Iiii1i == 5 :
   OoOo ( )
  if I111I1Iiii1i == 6 :
   III1IiIi1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if I111I1Iiii1i == 7 :
   oOOoO0O ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if I111I1Iiii1i == 8 :
   OoOoOoOOo00Ooo0O ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if I111I1Iiii1i == 9 :
   iIii1Oo ( )
  if I111I1Iiii1i == 10 :
   Ii11ii1 ( )
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
  if 1 - 1: iI11I1II1I1I % i1i1I1IIii1II . iI11I1II1I1I
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 10 - 10: IiI1i11I + oO0o
def i111I1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OOOo0Oo0O ( )
  if I111I1Iiii1i == 1 :
   o0OO0 ( )
  if I111I1Iiii1i == 2 :
   oOo0OOoO0 ( )
  if I111I1Iiii1i == 3 :
   i1I1I1iIIi ( OoO )
  if I111I1Iiii1i == 4 :
   IiOo00O0o0O ( OoO )
  if I111I1Iiii1i == 5 :
   Ooo0OOoOoO0 ( )
  if I111I1Iiii1i == 6 :
   O0OoOO ( url = 'http://www.iplocation.net/' , inc = 1 )
  if I111I1Iiii1i == 7 :
   o0o0oO0OOO ( )
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
  if 66 - 66: o0ii1I * iI11I1II1I1I - i1iIi / oOo0O0Ooo
  if 62 - 62: III1iiIii . o0o00Oo0O . iI11I1II1I1I
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi % Iii % ooOoO0O00
 if 90 - 90: o0ii1I * oO0o
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
 if 7 - 7: IiI1i11I . o0ii1I . IiI1i11I - i1IiiiI1iI
 if 33 - 33: i1iIi + ii - oO0o / ooOoO0O00 / ii
def OOO0IIIIii11II1I ( ) :
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
 if 48 - 48: Ii1I - o0o00Oo0O . oO0o
def I1ii1ii11i1I ( ) :
 iii ( )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 38 - 38: o0o00Oo0O
def ooOi1i1i11iI11II ( ) :
 iii ( )
 i11I1II1I11i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 i11I1II1I11i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / o0ii1I
 if 14 - 14: i1IiiiI1iI % III1iiIii - o0o00Oo0O / i1IiiiI1iI
 if 91 - 91: Ii % i1IiiiI1iI * i1i1I1IIii1II - Ii1I . i1IiiiI1iI
def iIo00oo ( ) :
 iii ( )
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  O000Oo00 ( )
 if I111I1Iiii1i == 0 :
  iI1oOoo ( OoO )
 if I111I1Iiii1i == 0 :
  o00O0o00oo ( OoO )
  if 19 - 19: oOo0O0Ooo
  if 66 - 66: i1i1I1IIii1II / OOooOOo
  if 13 - 13: IIiIiII11i
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 55 - 55: I1ii11iIi11i % ooOoO0O00 * Iii
def OOOo0 ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for oOo0O , OO0O000 in IIi :
  i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0O , oOo0O , '' )
 iI1i11iII111 ( 'tvshows' , 'INFO' )
 if 51 - 51: i1IiiiI1iI
def Ooo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( o0o00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 5 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 46 - 46: OOooOOo
def O000Oo00 ( ) :
 iii ( )
 ii1I ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 4 - 4: IiI1i11I + o0o00Oo0O
def I1IiiiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iIiI1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 60 - 60: IiI1i11I + oO0o + Iii % iI11I1II1I1I . I1ii11iIi11i
def O0OOOOoO00oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoOiII11IiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 27 - 27: oO0o + OOooOOo
def ooo0oOooo0o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIii1Ii1i1ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 86 - 86: i1i1I1IIii1II % o0o00Oo0O + oO0o
def oO0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 88 - 88: oOo0O0Ooo
def iI1oOoo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 40 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 5 - 5: Ii * IiI1i11I - o0ii1I - Ii1I - ooOoO0O00 + IiI1i11I
def I1ii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OO00OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 5 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 45 - 45: IIiIiII11i * ooOoO0O00
def oOOoo00O00o ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  II1ii1 ( )
 if I111I1Iiii1i == 1 :
  oO0OOO ( )
 if I111I1Iiii1i == 2 :
  IiI1IIiiiii ( )
  if 43 - 43: i1i1I1IIii1II - III1iiIii % Ii * IIiIiII11i . i1IiiiI1iI - Iii
  if 13 - 13: oO0o
  if 70 - 70: III1iiIii . i1IiiiI1iI * oO0o + Iii - III1iiIii . III1iiIii
  if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def oO0OOO ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , ooo000o in IIi :
  oOoo000 ( 'Android Apps' + ooo000o , 'https://www.apkfiles.com' + OoO , 30035 , iiIi1IIiIi + 'apps.png' )
 for OoO , ooo000o in i1Iii1i1I :
  oOoo000 ( 'Android Games' + ooo000o , 'https://www.apkfiles.com' + OoO , 30035 , iiIi1IIiIi + 'GAMES.png' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
def OOOOOO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '/cat' in url :
   oOoo000 ( ( OO0O000 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def oOO0O ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '/app' in url :
   oOoo000 ( ( OO0O000 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def oooo0 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 OO0Oooo0oo = url
 if "page=" in str ( url ) :
  OO0Oooo0oo = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  if 'apk' in url :
   i11I1II1I11i ( ( OO0O000 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0O )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 i11I1II1I11i ( 'Next Page' , OO0Oooo0oo + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def OOOOiiI ( name , url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( oO00ooooO0o )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  o000Ooo00o00O ( name , url , 'Brackets' )
def IiI1IIiiiii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'https://www.apkfiles.com/search?q=' + ( I1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 IIII1ii = i1i11ii1Ii . lower ( )
 oooo0 ( IIII1ii )
 if 80 - 80: IiI1i11I
def iI1I1ii11IIi1 ( url ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( OOoOOoOO , 'Download' ) )
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
 if 78 - 78: i1IiiiI1iI / i1IiiiI1iI + oOo0O0Ooo % oooOo0oo0oo * III1iiIii
def IiIii11ii111 ( url ) :
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
 if 75 - 75: o0o00Oo0O
 if 56 - 56: oO0o / IIiIiII11i
def IIIiiiiI1 ( name , url , description ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 OooooOOoo0 = os . path . join ( ii1I1 , name )
 try :
  os . remove ( OooooOOoo0 )
 except :
  pass
 downloader . download ( url , OooooOOoo0 , o0oOoO00o )
 iii11i1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iii11i1
 print '======================================='
 extract . all ( OooooOOoo0 , iii11i1 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 33 - 33: OOooOOo . iI11I1II1I1I / Iii % o0ii1I
 if 49 - 49: oO0o + IIiIiII11i / III1iiIii - o0o00Oo0O % o0ii1I
 if 27 - 27: oO0o + I1ii11iIi11i
 if 92 - 92: oOo0O0Ooo % IiI1i11I
 if 31 - 31: ii - i1i1I1IIii1II / i1IiiiI1iI
def II1ii1 ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , OoO , II1i11I1 , iI , oo00o000O in IIi :
  i11I1II1I11i ( OO0O000 , OoO , 80003 , II1i11I1 , iiIi1IIiIi + 'APKToolsB.png' , oo00o000O )
def OooO0o ( apk , ret = None ) :
 if apk == "kodi" :
  Oo00o = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( Oo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   III = IIi [ 0 ] [ 0 ]
   o0ooOOOo = IIi [ 0 ] [ 1 ]
   i1ii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( III , o0ooOOOo )
  if ret == 'version' : return III
  else : return i1ii
 elif apk == "spmc" :
  Ii1iii11I = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( Ii1iii11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  III = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  i1ii = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( III , III )
  if ret == 'version' : return III
  else : return i1ii
def o000Ooo00o00O ( name , url , Brackets ) :
 if OooOoOO0 ( ) == 'android' :
  Ii11iIiiI = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not Ii11iIiiI : iiII ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iII1IiiIIIIii = name
  if Ii11iIiiI :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OOooo0O0o0 ( url ) == True : iiII ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iII1IiiIIIIii , '' , 'Please Wait' )
   OooooOOoo0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( OooooOOoo0 )
   except : pass
   downloader . download ( url , OooooOOoo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oooII111 = zipfile . ZipFile ( OooooOOoo0 )
    for file in oooII111 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as oooO :
       oOOOIii1IiiII1Ii1 = file . split ( '/' ) [ 1 ]
       oooO . write ( oooII111 . read ( file ) )
       xbmc . sleep ( 500 )
       oooO . close ( )
       try :
        os . remove ( OooooOOoo0 )
       except :
        pass
       OooooOOoo0 = os . path . join ( i1iIIi1 , oOOOIii1IiiII1Ii1 )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + OooooOOoo0 + '")' )
  else : iiII ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiII ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 26 - 26: ii + oOo0O0Ooo
 if 57 - 57: oooOo0oo0oo . o0ii1I % I11i
 if 32 - 32: Iii / III1iiIii - o0o00Oo0O * iI11I1II1I1I
 if 70 - 70: ii % ii % oO0o
def oo0O0OO ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for OoO , OO0O000 in IIi :
  OoO = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + OoO )
  i11IIIIi ( ( OO0O000 ) . replace ( '_' , ' ' ) , OoO )
  if 62 - 62: IIiIiII11i - i1IiiiI1iI + Iii * iI11I1II1I1I * I11i
def i11IIIIi ( name , url ) :
 if OooOoOO0 ( ) == 'android' :
  Ii11iIiiI = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not Ii11iIiiI : iiII ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iII1IiiIIIIii = name
  if Ii11iIiiI :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OOooo0O0o0 ( url ) == True : iiII ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iII1IiiIIIIii , '' , 'Please Wait' )
   OooooOOoo0 = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( OooooOOoo0 )
   except : pass
   downloader . download ( url , OooooOOoo0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + OooooOOoo0 + '")' )
  else : iiII ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiII ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 83 - 83: oO0o
 if 16 - 16: i1iIi
def iIiiIiIIiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 5 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 93 - 93: III1iiIii % Ii1I
 if 31 - 31: IIiIiII11i + oooOo0oo0oo - ii . Iii
def oOoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 30015 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 28 - 28: o0ii1I . Ii1I
def oOo000Oo00o ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 O00OOoOOOO00O = url
 oOo0O = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iIiII , OO0O000 in IIi :
  if '.mp4' in OO0O000 :
   i11I1II1I11i ( 'Watch VIDEO' , url + '/' + iIiII , 222 , oOo0O , fanart , '' )
  if 'description' in OO0O000 :
   i11I1II1I11i ( 'Read Description' , url + '/' + iIiII , 30017 , oOo0O , fanart , '' )
  if 'images' in OO0O000 :
   ii1I ( 'View Images' , url + '/' + iIiII , 30018 , oOo0O , fanart , '' )
  if 'url' in OO0O000 :
   i11I1II1I11i ( 'Install Build On Android' , url + '/' + iIiII , 30016 , oOo0O , fanart , '' )
  if 'url' in OO0O000 :
   i11I1II1I11i ( 'Install Build On Pc' , url + '/' + iIiII , 30019 , oOo0O , fanart , '' )
 iI1i11iII111 ( 'movies' , 'INFO' )
 if 81 - 81: ii
def ooOOOoOoOOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  I1111111 ( url )
  if 57 - 57: oooOo0oo0oo % oO0o - oOo0O0Ooo
def i11iI11 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  iiIIiiiIi1 ( url )
  if 61 - 61: IIiIiII11i
def iiI11111II ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for O0oO00oOOooO in IIi :
  o0OIiII ( 'Description:' , O0oO00oOOooO )
  if 48 - 48: IiI1i11I % Ii . ii * III1iiIii % oO0o . IiI1i11I
def IiOOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for iIiII , OO0O000 in IIi :
  if 'png' in OO0O000 :
   i11I1II1I11i ( 'image' , '' , '' , url + '/' + iIiII , url + '/' + iIiII , '' )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 85 - 85: i1IiiiI1iI % Ii1I
def OO00o0O0oOooO ( name , url , description ) :
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
 if 18 - 18: Ii * I1ii11iIi11i / Ii1I + Ii1I % OOooOOo
 if 12 - 12: Iii
def iiIIiiiIi1 ( url ) :
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
 OOOo0Oo0O ( )
 if 19 - 19: o0ii1I * ooOoO0O00 % o0o00Oo0O + Iii
def I1111111 ( url ) :
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
 OOOo0Oo0O ( )
 if 25 - 25: i1IiiiI1iI - o0ii1I / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
def Ii1i ( name , url , description ) :
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
 OOOo0Oo0O ( )
 if 49 - 49: i1i1I1IIii1II + i1i1I1IIii1II + Ii % IiI1i11I
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
  I1I1oO00o0oOoo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooO . write ( I1I1oO00o0oOoo . rstrip ( '\r\n' ) + '\n' )
def OOOo0Oo0O ( ) :
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
  if 66 - 66: Ii1I . I1ii11iIi11i
  if 38 - 38: Iii . III1iiIii - oO0o . oOo0O0Ooo
  if 65 - 65: i1IiiiI1iI
def o00O0o00oo ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( url ) :
  for file in i1I1ii1i :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    Oo0oOOOOo = open ( ( os . path . join ( ii1Io0oOO0 , file ) ) ) . read ( )
    I11II11IiI11 = Oo0oOOOOo . replace ( oOo0oooo00o , 'special://home/' )
    oooO = open ( ( os . path . join ( ii1Io0oOO0 , file ) ) , mode = 'w' )
    oooO . write ( str ( I11II11IiI11 ) )
    oooO . close ( )
 OOOo0Oo0O ( )
 if 97 - 97: i1iIi / iI11I1II1I1I % i1iIi / oOo0O0Ooo * IiI1i11I % OOooOOo
def iIIii1iiiIiiI ( ) :
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 17 - 17: iI11I1II1I1I
def ooi11I ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def i111111 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def o0oO0OOoO0OoO0 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , oOo0O , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0O )
def iI11IiiiIII ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooO0OO ( url )
def i1i1Ii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1
 Oo0o00o = 'https://www.radionomy.com/en/search/index?query=' + ( I1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( Oo0o00o )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OO0O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + OoO , 70005 , oOo0O )
  if 32 - 32: OOooOOo + i1iIi + o0ii1I + oOo0O0Ooo
  if 26 - 26: IiI1i11I - I1ii11iIi11i + oOo0O0Ooo + I11i
def OoOo ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.listenlive.eu/' + OoO , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def IiiII1iiiiI1i ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 if 37 - 37: I11i * oooOo0oo0oo + oOo0O0Ooo . Ii1I * ii
 if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + oooOo0oo0oo * IIiIiII11i
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , iIiIiiIIIi1 , url , i1I in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' [COLORorangered] ' + i1I + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[CR]' + iIiIiiIIIi1 + '[CR]' + i1I + '[/COLOR]' )
  if 44 - 44: oooOo0oo0oo * ooOoO0O00
def OOOoOo0O0O ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.toonjet.com/' + OoO , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0Oo0oO00Oooo ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
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
   oOoo000 ( ( oOo0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1II1I11i1I ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 91 - 91: oO0o / oO0o . IIiIiII11i . i1iIi - oOo0O0Ooo
  if 23 - 23: oOo0O0Ooo
def Ii11ii1 ( ) :
 OooO0O0Ooo ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 OooO0O0Ooo ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 7 - 7: IiI1i11I % Ii1I
def o0oOOO ( ) :
 OooO0O0Ooo ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 OooO0O0Ooo ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 OooO0O0Ooo ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 47 - 47: oooOo0oo0oo / IIiIiII11i % III1iiIii . i1i1I1IIii1II * Ii1I
def iIii1iIiII1i1 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , o0oO in IIi :
  if 'Parent' in OO0O000 :
   pass
  elif '2' in o0oO :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: ooOoO0O00
def Oo00 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , o0oO in IIi :
  if I1 in OO0O000 . lower ( ) :
   if '1' in o0oO :
    OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in o0oO :
    OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in o0oO :
    OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 41 - 41: oO0o % oOo0O0Ooo - I1ii11iIi11i
    if 11 - 11: o0ii1I * I11i / III1iiIii + OOooOOo + oO0o % i1IiiiI1iI
def iIIi1II1 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OO0O000 , OoO , o0oO in IIi :
  if '1' in o0oO :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in o0oO :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in o0oO :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , OoO , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 42 - 42: iI11I1II1I1I - i1iIi - Iii - i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: OOooOOo - o0o00Oo0O
def III11iI1i11i ( url ) :
 iIiII = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in i1Iii1i1I :
  if 'mp3' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIiII + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIiII + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iIiII + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in OO0O000 :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIiII + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: OOooOOo / i1i1I1IIii1II / o0ii1I * I11i * i1i1I1IIii1II . oOo0O0Ooo
   if 93 - 93: OOooOOo
   if 97 - 97: Ii
def O0oOo0o0OOoO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIiII = url
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
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIiII + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in OO0O000 :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIiII + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iIiII + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: o0ii1I % Iii + I11i
   if 65 - 65: iI11I1II1I1I . IiI1i11I / o0ii1I
def iI11ii ( ) :
 OooO0O0Ooo ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 OooO0O0Ooo ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 OooO0O0Ooo ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 65 - 65: III1iiIii
def iiI11 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + OoO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0O :
   pass
  else :
   OooO0O0Ooo ( oOo0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( OoO ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0O + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: i1i1I1IIii1II
 if 48 - 48: Iii / iI11I1II1I1I % IIiIiII11i
def IiI111I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  if '</a>' in OO0O000 :
   pass
  elif '(' in OO0O000 :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: ii + III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: OOooOOo * I11i / ii
def oOooo00OOO000 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if I1 in OO0O000 . lower ( ) :
   if '</a>' in OO0O000 :
    pass
   elif '(' in OO0O000 :
    OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 85 - 85: ooOoO0O00 - oooOo0oo0oo / o0o00Oo0O + o0o00Oo0O / Ii1I
    if 54 - 54: i1iIi * Ii1I . IIiIiII11i / oooOo0oo0oo % oooOo0oo0oo
def IiIIii1 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if '</a>' in OO0O000 :
   pass
  elif '(' in OO0O000 :
   OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + OoO , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 7 - 7: o0o00Oo0O - Ii1I / OOooOOo - o0ii1I - i1i1I1IIii1II / ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: ii
 if 55 - 55: Ii1I + Ii1I
def o0o0OOo0OOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIiII = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iIiII )
  if 52 - 52: III1iiIii / IIiIiII11i / oOo0O0Ooo - i1iIi + OOooOOo * oOo0O0Ooo
def ooOIIIi11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  if '<p align' in OO0O000 :
   pass
  elif '&nbsp;' in OO0O000 :
   pass
  else :
   ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: ii . o0ii1I % i1i1I1IIii1II * ii
 if 96 - 96: o0ii1I - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
def oo0OOOoOo ( ) :
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
def oOO0O0O ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiI1Ii11Ii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0O , oOo0O , OO0O000 )
 for url , OO0O000 in IiI1Ii11Ii :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def Oo0o0oOo0oO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIIIi1i1I11i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1iiiI1I = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 o00OoOOoO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in i1iiiI1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , OO0O000 in iIIIi1i1I11i :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  ii1I ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def iii1i1Iiiiiii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 58 - 58: I11i / Ii / o0o00Oo0O % Iii % oOo0O0Ooo
def ooO000O ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , OO0O000 in IIi :
  if '9cart' in OoO :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 86 - 86: III1iiIii + OOooOOo / oOo0O0Ooo + Iii % Iii / Ii
def iIiI1I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , OO0O000 in IiIi1I1 :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 2 - 2: I11i . o0ii1I % OOooOOo
def OO00O00o0O ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20003 , oOo0O )
 for url , OO0O000 in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 100 - 100: oO0o % OOooOOo / Iii * o0o00Oo0O - i1i1I1IIii1II
def I1IiIi1iiI ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   oOoo000 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 26 - 26: oOo0O0Ooo % OOooOOo
def OO00o0oo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 3 - 3: o0ii1I * i1iIi - oOo0O0Ooo / ooOoO0O00
def ii1iIi1 ( url ) :
 url = cloudflare . source ( url )
 OOo00ooOoO0o ( url )
 if 44 - 44: oO0o + Iii % oO0o + ooOoO0O00 + IiI1i11I + o0o00Oo0O
def Ii1iII1ii1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  OOo00ooOoO0o ( url )
  if 80 - 80: iI11I1II1I1I / Ii + IiI1i11I
  if 41 - 41: i1IiiiI1iI + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def IIiiIIi1 ( ) :
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
 ii1I ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 25 - 25: ii . o0ii1I % IiI1i11I . III1iiIii
def O0O0 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
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
def oOIII111iiIi1 ( url ) :
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
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10007 , O0oOOO0o0Ooo )
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
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 222 , oOo0O )
   if 16 - 16: o0ii1I % iI11I1II1I1I . oOo0O0Ooo
def IIii1Ii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
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
     OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + I111ii1III1I + '   -   ' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0O , )
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
    OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + I111ii1III1I + '   -   ' + OO0O000 + '[/COLOR]' , ( OoO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0O )
   elif 'vee' in OoO :
    pass
    if 93 - 93: Ii1I - i1iIi % Ii1I
    if 12 - 12: oooOo0oo0oo + oO0o * Iii + o0ii1I + III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: IiI1i11I * o0ii1I - Ii % Ii1I
def iIIiI1I1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0O0OOooOO0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O0O0OOooOO0 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O0O0OOooOO0 :
  iIIi1IIi ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 3 - 3: i1IiiiI1iI . Iii % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
  if 5 - 5: IIiIiII11i * ooOoO0O00 % o0ii1I
  if 55 - 55: oOo0O0Ooo + IiI1i11I
  if 85 - 85: i1i1I1IIii1II + IiI1i11I % IiI1i11I / Iii . oOo0O0Ooo - OOooOOo
  if 19 - 19: Iii / IiI1i11I + III1iiIii
  if 76 - 76: iI11I1II1I1I / i1IiiiI1iI - Ii1I % I11i % oooOo0oo0oo + ii
  if 10 - 10: oO0o * Iii / I1ii11iIi11i - i1IiiiI1iI
def I1Iiiiiii ( ) :
 if 11 - 11: III1iiIii % Ii1I / i1iIi . Ii + oooOo0oo0oo - IIiIiII11i
 IiiIiiiiI1III ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 IiiIiiiiI1III ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 42 - 42: i1i1I1IIii1II - i1iIi * Iii % IiI1i11I * I1ii11iIi11i / i1IiiiI1iI
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi + iI11I1II1I1I
def OOo0Oo0O00O ( ) :
 IiiIiiiiI1III ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 IiiIiiiiI1III ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 56 - 56: Ii1I + i1i1I1IIii1II . oO0o + ii * Ii1I - o0o00Oo0O
 iI1i11iII111 ( 'movies' , 'MAIN' )
def I1i ( ) :
 if 72 - 72: Iii * OOooOOo % i1IiiiI1iI % i1iIi
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 i1II11Iii1I = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 22 - 22: oooOo0oo0oo - Ii1I / III1iiIii
 for IiIIi1I1I11Ii in i1II11Iii1I :
  o0OO = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( o0OO )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , iI , OO0O000 in IIi :
   if I1 in OO0O000 . lower ( ) :
    o0ooO0Oo ( OO0O000 , OoO , 222 , iiiI1I1iIIIi1 , iI , oo0O0 )
    if 98 - 98: Iii - ooOoO0O00 % o0ii1I - ii
    iI1i11iII111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 19 - 19: iI11I1II1I1I + i1IiiiI1iI . i1IiiiI1iI - I1ii11iIi11i
    if 41 - 41: oOo0O0Ooo . I1ii11iIi11i . III1iiIii % ii + oO0o
def II1IiI1iI ( ) :
 if 17 - 17: Ii - Ii + Ii1I * i1iIi * i1i1I1IIii1II / ii
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 i1II11Iii1I = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 22 - 22: i1IiiiI1iI * Ii1I - III1iiIii
 for IiIIi1I1I11Ii in i1II11Iii1I :
  Oo0oI11iiIiI1II11 = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( Oo0oI11iiIiI1II11 )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OO0O000 , oo0O0 , OoO , oOo0O , iI , o000O000 in IIi :
   if I1 in OO0O000 . lower ( ) :
    IiiIiiiiI1III ( OO0O000 , OoO , o000O000 , oOo0O , iI , oo0O0 )
    if 94 - 94: I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + ii % oO0o
    iI1i11iII111 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 36 - 36: IiI1i11I * Iii * o0o00Oo0O * oooOo0oo0oo - I11i / Ii1I
    if 54 - 54: ooOoO0O00 - oO0o / ii
def ooooOOo ( ) :
 if 100 - 100: oooOo0oo0oo % Ii - oOo0O0Ooo * i1IiiiI1iI - I11i
 oO00ooooO0o = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , oo0O0 , OoO , oOo0O , iI , o000O000 in IIi :
  IiiIiiiiI1III ( OO0O000 , OoO , o000O000 , oOo0O , iI , oo0O0 )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def Oooo0o00 ( url ) :
 if 74 - 74: I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . III1iiIii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOoo0oo00000O = ( '%s%s' % ( oo0 , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in IIi :
  Oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for iII1i11 in Oo :
   if iII1i11 == url :
    OO0O000 = ( '[COLORred]Watched - [/COLOR]' + OO0O000 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o0ooO0Oo ( OO0O000 , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
  if 89 - 89: III1iiIii - ooOoO0O00 - III1iiIii
  iI1i11iII111 ( 'movies' , 'MAIN' )
  if 74 - 74: oO0o % oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: OOooOOo % i1i1I1IIii1II - oooOo0oo0oo + oooOo0oo0oo + i1i1I1IIii1II / iI11I1II1I1I
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
def ooOoo000 ( url ) :
 if 56 - 56: i1iIi . iI11I1II1I1I + ooOoO0O00
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , oo0O0 , url , oOo0O , iI , o000O000 in IIi :
  IiiIiiiiI1III ( OO0O000 , url , o000O000 , oOo0O , iI , oo0O0 )
  if 84 - 84: IiI1i11I % ooOoO0O00
  iI1i11iII111 ( 'movies' , 'MAIN' )
  if 62 - 62: Ii1I . i1IiiiI1iI . o0ii1I
  if 19 - 19: Ii1I / i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: I1ii11iIi11i * i1i1I1IIii1II / ii + o0o00Oo0O / ii / oooOo0oo0oo
def o0ooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 44 - 44: ooOoO0O00 . Ii1I - i1iIi . oooOo0oo0oo . I11i + i1i1I1IIii1II
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + o0ii1I % ooOoO0O00 . i1i1I1IIii1II
def IiiIiiiiI1III ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 57 - 57: i1i1I1IIii1II
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
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
if 37 - 37: IiI1i11I - Iii + iI11I1II1I1I / i1IiiiI1iI - oO0o . I11i
if 62 - 62: Ii1I
if 47 - 47: i1IiiiI1iI % oooOo0oo0oo * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 7 - 7: oOo0O0Ooo
def i111i11iI1i1I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 IiI1 = [ ]
 try :
  if 49 - 49: ooOoO0O00 . oO0o / Ii + o0ii1I % o0o00Oo0O + Ii1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  I1Ii111I111 ( 'Making Favorites File' )
  IiI1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Oo0oOOOOo = open ( i1I1iI , "w" )
  Oo0oOOOOo . write ( json . dumps ( IiI1 ) )
  Oo0oOOOOo . close ( )
 else :
  I1Ii111I111 ( 'Appending Favorites' )
  Oo0oOOOOo = open ( i1I1iI ) . read ( )
  I1iI1Ii11 = json . loads ( Oo0oOOOOo )
  I1iI1Ii11 . append ( ( name , url , iconimage , fanart , mode ) )
  I11II11IiI11 = open ( i1I1iI , "w" )
  I11II11IiI11 . write ( json . dumps ( I1iI1Ii11 ) )
  I11II11IiI11 . close ( )
  if 34 - 34: o0ii1I * oOo0O0Ooo + Iii * OOooOOo - IIiIiII11i
  if 92 - 92: oooOo0oo0oo . I11i / IiI1i11I . iI11I1II1I1I % I1ii11iIi11i . ii
def Ooo00OoO0O00 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  IiI1 = [ ]
  I1Ii111I111 ( 'Making Favorites File' )
  IiI1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Oo0oOOOOo = open ( i1I1iI , "w" )
  Oo0oOOOOo . write ( json . dumps ( IiI1 ) )
  Oo0oOOOOo . close ( )
 else :
  ii1ii1i1ii = json . loads ( open ( i1I1iI ) . read ( ) )
  II11II1I = len ( ii1ii1i1ii )
  for iIi1Iii1 in ii1ii1i1ii :
   OO0O000 = iIi1Iii1 [ 0 ]
   OoO = iIi1Iii1 [ 1 ]
   iiiI1I1iIIIi1 = iIi1Iii1 [ 2 ]
   try :
    oooo = iIi1Iii1 [ 3 ]
    if oooo == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oooo = iiiI1I1iIIIi1
    else :
     oooo = iI
   try : I11iii1iIIIIi = iIi1Iii1 [ 5 ]
   except : I11iii1iIIIIi = None
   try : III1i1iiI1 = iIi1Iii1 [ 6 ]
   except : III1i1iiI1 = None
   if 62 - 62: o0ii1I . Ii % o0o00Oo0O % i1IiiiI1iI - I1ii11iIi11i
   if iIi1Iii1 [ 4 ] == 0 :
    ii1I ( OO0O000 , OoO , '' , iiiI1I1iIIIi1 , iI , '' , 'fav' )
   else :
    ii1I ( OO0O000 , OoO , iIi1Iii1 [ 4 ] , iiiI1I1iIIIi1 , iI , '' , 'fav' )
    if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % o0ii1I + oOo0O0Ooo
def ooOOO000O ( name ) :
 I1iI1Ii11 = json . loads ( open ( i1I1iI ) . read ( ) )
 for o0Oi1IIi in range ( len ( I1iI1Ii11 ) ) :
  if I1iI1Ii11 [ o0Oi1IIi ] [ 0 ] == name :
   del I1iI1Ii11 [ o0Oi1IIi ]
   I11II11IiI11 = open ( i1I1iI , "w" )
   I11II11IiI11 . write ( json . dumps ( I1iI1Ii11 ) )
   I11II11IiI11 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
 if 3 - 3: i1iIi / ooOoO0O00 - OOooOOo
def o0o0ooOo00 ( ) :
 oo0o0ooOoo00O = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 iI1ii1 = open ( oo0o0ooOoo00O , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 iI1ii1 . write ( r'[' + IiII + ']' + '\n' )
 for OO0O000 , oOo0O , O0oOOo , OoO in IIi :
  OoO = ( OoO + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  ii111IIiiiiI = ( OO0O000 + '=plugin://' + IiII + '/?url=' + OoO + '&mode=10012&name=' + ( OO0O000 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iI1ii1 . write ( ii111IIiiiiI + '\n' )
  if 98 - 98: ooOoO0O00 - IiI1i11I
  if 49 - 49: I11i . o0ii1I . i1i1I1IIii1II
def i11iI11ii ( ) :
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO in IIi :
  oOoo000 ( '24/7' , OoO , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 85 - 85: ooOoO0O00
def oOooo0OO0O0 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def oOo0Ooo0 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def IIII1iII ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def o0o0o0O0oo ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  i11I1II1I11i ( OO0O000 , ( OoO ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def i1iI1iIII ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  i11I1II1I11i ( OO0O000 , OoO , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 76 - 76: IIiIiII11i
  if 28 - 28: ii + i1iIi . III1iiIii . I1ii11iIi11i - oOo0O0Ooo
def OOOo0ooOO ( ) :
 if 89 - 89: Iii
 ii1I ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 14 - 14: o0o00Oo0O
def Ii11II1IIIIIi ( ) :
 if 83 - 83: iI11I1II1I1I + IIiIiII11i * i1i1I1IIii1II / o0o00Oo0O - IiI1i11I
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 , iIIi1Ii1III in IIi :
  ii1I ( OO0O000 + '  -  ' + ( iIIi1Ii1III ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoO , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 23 - 23: ooOoO0O00
  if 24 - 24: III1iiIii
  if 51 - 51: oooOo0oo0oo % Ii
def o0OoOoOo0O ( ) :
 if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
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
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IIIii111i ( url ) :
 O00OOoOOOO00O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( O00OOoOOOO00O )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 58 - 58: oooOo0oo0oo % IiI1i11I * o0o00Oo0O + Ii1I - III1iiIii
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Iii + Iii
  if 46 - 46: i1IiiiI1iI % Ii1I + o0ii1I
  if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / Iii + i1iIi
def i11IiIiii ( ) :
 if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 OoO = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( OoO )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 in IIi :
  if I1 in OO0O000 . lower ( ) :
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
   if 3 - 3: oooOo0oo0oo . I1ii11iIi11i / Ii + oO0o
   if 47 - 47: III1iiIii . oooOo0oo0oo
def O0oo00o000 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiII , II11I , II1111iiI1II , OO0O000 in IIi :
  OoOOOO00 = ( II1111iiI1II ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1I1iii1III1 = ( II11I ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0oOO00O000O0 = 'Season ' + I1I1iii1III1 + 'Episode ' + OoOOOO00 + OO0O000
  OOOoO000 ( o0oOO00O000O0 , iIiII )
  if 79 - 79: IiI1i11I / i1IiiiI1iI + I11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: oO0o + o0ii1I
  if 11 - 11: IiI1i11I + ii * o0ii1I . I11i
def OOOoO000 ( name , url ) :
 iIiII = url
 i1iIi1iiii1ii = name
 o0o = cloudflare . source ( iIiII )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for O0O0OOooOO0 , oO0oOo in i1Iii1i1I :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + i1iIi1iiii1ii + oO0oOo + '[/COLOR]' , O0O0OOooOO0 , 222 , iiIi1IIiIi + 'dtv.png' )
  if 43 - 43: i1i1I1IIii1II + OOooOOo . oOo0O0Ooo . Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: I11i + oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
 if 91 - 91: o0o00Oo0O - Iii % i1IiiiI1iI
def o0ii1i ( ) :
 if 46 - 46: i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
 if 13 - 13: i1IiiiI1iI % I11i + oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: IiI1i11I
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
 if 5 - 5: oooOo0oo0oo + IiI1i11I
 if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
 ii1I ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
def iIIii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o000oo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oOo0O , '' , '' )
 for url in o000oo :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 58 - 58: i1iIi + IIiIiII11i + o0ii1I . ii
def Iii1iiIIi1i111i ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o000oo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 in IIi :
  oOo0O = 'http://watchepisodes.cc/' + oOo0O
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 10093 , oOo0O , oOo0O , '' )
 for url in o000oo :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 48 - 48: I1ii11iIi11i . I11i - IiI1i11I
def i1iI1Ii1 ( url , iconimage ) :
 oOo0O = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II1111iiI1II , url , OO0O000 in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + II1111iiI1II + ' - ' + OO0O000 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oOo0O , '' , '' )
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
def oOOoo ( ) :
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
 i1i1i1I = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1i1i1I ) )
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
 for oOo0O , url , OO0O000 , II1111iiI1II , oo0O0 in IIi :
  O00Oo = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( II1111iiI1II ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0O , '' , oo0O0 )
  if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 in IIi :
  O00Oo = ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
def iIIIIIIIIIi1i1i1iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0O , '' , '' )
 for url in i1Iii1i1I :
  ii1I ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 53 - 53: oO0o
def oooOoOO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1i1i1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II11I , Oo0O0o in i1i1i1I :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Oo0O0o ) )
  for url , OO0O000 in IIi :
   O00Oo = ( II11I ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
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
  O00Oo = name
  self . Get_Sources ( OoO , O00Oo )
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
  for iIIIII1iiiiII , OO0O000 in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 50 - 50: i1iIi
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII , OO0O000 in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 83 - 83: Ii - oOo0O0Ooo * Ii
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 59 - 59: IiI1i11I - ii / i1iIi + Ii1I . I11i - IiI1i11I
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 29 - 29: i1i1I1IIii1II
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . youplay ( iIIIII1iiiiII , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 26 - 26: o0o00Oo0O % oooOo0oo0oo - III1iiIii . oooOo0oo0oo
 def Printer ( self , Link , season_name , source_name ) :
  if 70 - 70: I11i + Iii / IiI1i11I + i1iIi / oOo0O0Ooo
  if Link in IIIiiII1iIi1ii1i . List :
   pass
  elif source_name in IIIiiII1iIi1ii1i . source_list :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
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
def Ooo00OoOOO ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 40 - 40: iI11I1II1I1I / i1iIi / oOo0O0Ooo + Ii1I * oooOo0oo0oo
def III1i1iI111I1 ( url ) :
 OOoO0OooO0O = '20'
 OOOO00O0OO0oo = [ ]
 II111IiiIIi = '                                                    '
 o0oo = '        '
 ii1I ( II111IiiIIi + 'pl' + o0oo + 'w' + o0oo + 'd' + o0oo + 'l' + o0oo + 'f' + o0oo + 'a' + o0oo + 'pts' , '' , '' , '' , '' , '' )
 oO00ooooO0o = O0oOOo0Oo ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOOO00o0OOO00 , oo0oOooo0 , oo0oO0oo , OO00 , o0O0ooo0o , oooO , Oo0oOOOOo , O0Oo , O0oOo00Oo0oo0 in IIi :
  i111 = O0oOO0o00OO ( oo0oOooo0 )
  II1i11i1iI1I = O0oOO0o00OO ( oo0oO0oo )
  oooOoO00O = O0oOO0o00OO ( OO00 )
  I1i1IIiiI11II = O0oOO0o00OO ( o0O0ooo0o )
  Ii1i1 = O0oOO0o00OO ( oooO )
  iiiIiIIiIiiii = O0oOO0o00OO ( Oo0oOOOOo )
  OOOO00O0OO0oo . append ( oOOO00o0OOO00 [ 0 ] )
  o00O0OooO0 = len ( OOOO00O0OO0oo )
  iii1II11II1 = int ( len ( II111IiiIIi ) - len ( oOOO00o0OOO00 ) - 2 )
  if len ( OOOO00O0OO0oo ) >= 10 :
   iii1II11II1 = iii1II11II1 - 1
  if len ( OOOO00O0OO0oo ) <= int ( OOoO0OooO0O ) :
   i11I1II1I11i ( str ( o00O0OooO0 ) + ' ' + oOOO00o0OOO00 + II111IiiIIi [ 0 : iii1II11II1 ] + oo0oOooo0 + i111 + oo0oO0oo + II1i11i1iI1I + OO00 + oooOoO00O + o0O0ooo0o + I1i1IIiiI11II + oooO + Ii1i1 + Oo0oOOOOo + iiiIiIIiIiiii + ' ' + O0oOo00Oo0oo0 , '' , '' , '' , '' , '' )
   if 30 - 30: III1iiIii / Ii % oO0o * oooOo0oo0oo
   if 27 - 27: o0o00Oo0O
def O0oOO0o00OO ( space ) :
 if len ( space ) > 1 :
  iIi1iI = len ( '        ' ) - len ( space ) + 1
  space = int ( iIi1iI ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 95 - 95: OOooOOo . I1ii11iIi11i + IIiIiII11i - Ii1I
def OoOOoo0o00O0oO ( ) :
 if 28 - 28: ii % o0o00Oo0O - oooOo0oo0oo / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * III1iiIii / oO0o . i1i1I1IIii1II
 if 50 - 50: ii + iI11I1II1I1I / i1i1I1IIii1II / oooOo0oo0oo . Ii . i1iIi
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
 i1i1i1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  i1iiIII1IIiIIII = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1i1i1I ) )
  for i1iii in i1iiIII1IIiIIII :
   i1iii = i1iii
  oOoOO0OO0O0 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
  for oooO000Oo000O , oOo0O , time , o0oO0OoO0 in oOoOO0OO0O0 :
   I11I11I11IiIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0oO0OoO0 )
   ii1I ( '[COLOR' + ooOoOoo0O + ']' + i1iii + ' - ' + oooO000Oo000O + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0O , Oo00OOOOO , ( str ( I11I11I11IiIi ) ) )
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
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
 for url , oOo0O , OO0O000 in i1Iii1i1I :
  oo00O000 = OO0O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OO0O000 :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
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
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oo00O000 + '[/COLOR]' , url , 10013 , oOo0O )
   if 84 - 84: IiI1i11I % oOo0O0Ooo / iI11I1II1I1I * o0ii1I * iI11I1II1I1I + Ii1I
def O000o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for O0O0OOooOO0 in IIi :
  oOO0O0o0Oo = ( O0O0OOooOO0 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iIIi1IIi ( 'http:' + oOO0O0o0Oo )
  if 9 - 9: IiI1i11I - IiI1i11I
  if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + i1i1I1IIii1II
  if 20 - 20: oO0o + Iii . IIiIiII11i / Ii
  if 50 - 50: ii / oO0o % iI11I1II1I1I
def IIIIi11111 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  OooOo00o ( OO0O000 , url , 8046 , oOo0O )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def Oo0o00o0oOoo0 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  iIIi1IIi ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 36 - 36: i1IiiiI1iI / OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * o0o00Oo0O
def iI11 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oO00ooooO0o )
 for url in IIi :
  yt . PlayVideo ( url )
  if 32 - 32: i1iIi - ii + oO0o
def I1iiIIIi11 ( ) :
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0oO ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0O )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: Ii / oO0o % o0o00Oo0O / oooOo0oo0oo + I1ii11iIi11i % I11i
  if 93 - 93: OOooOOo % i1IiiiI1iI - IiI1i11I . III1iiIii - Ii1I * IiI1i11I
def i1iI1I1I ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def i1I11i1iii1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , '' )
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
 oO00ooooO0o = oOOo000oOoO0 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  if 'genre' in OoO :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , OoO , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOIiI1IIIiI1I1i ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0O )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 84 - 84: OOooOOo - Iii
def OoO00O00O0 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  i1I11i1iii1 ( url )
  if 76 - 76: oOo0O0Ooo % Ii + oooOo0oo0oo
def I11iIIi1Iii ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i11ii1Ii = 'http://documentarylovers.com/?s=' + ( I1 ) . replace ( ' ' , '+' )
 IIII1ii = i1i11ii1Ii . lower ( )
 OOIiI1IIIiI1I1i ( IIII1ii )
 if 96 - 96: IiI1i11I % IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - Ii1I
def i11i1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if 'films' in url :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def O0O0I1II ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  if 'films' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0O )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def o0o0OoOO00Oo ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'rtd' in url :
   i1iiIi1II1 ( url )
   if 12 - 12: Ii + Iii - Ii1I
def i1iiIi1II1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oO00ooooO0o )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  OooO0OO ( url )
  if 27 - 27: IiI1i11I
  if 22 - 22: OOooOOo / oOo0O0Ooo
def iI11I1IiI1 ( ) :
 II11iIiIIIiI = oOOo000oOoO0 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO , oOo0O , OO0O000 , I1i111IiIiIi1 in IIi :
  oOoo000 ( ( OO0O000 + '[COLOR' + ooOoOoo0O + ']' + I1i111IiIiIi1 + '[/COLOR]' ) , OoO , 8086 , oOo0O )
  if 5 - 5: IiI1i11I / i1i1I1IIii1II % i1iIi . Ii % OOooOOo + i1i1I1IIii1II
def oOo0oOoo0 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oOo0O , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8087 , oOo0O )
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
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 97 - 97: oOo0O0Ooo + III1iiIii . Ii * I1ii11iIi11i % ooOoO0O00
def oo00000ooOooO ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + OoO , 3002 , 'http://www.solie.org/alibrary/' + oOo0O )
def oo0o0OO00oOO ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0O )
def IiiII1iIi ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 OoO00oooo0o = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , OO0O000 in OoO00oooo0o :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Season- ' + OO0O000 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , oOo0O , OO0O000 in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0O )
def iiiiii ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oO00ooooO0o )
 for url in IIi :
  ooII1 ( url )
def ooII1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  OooO0OO ( url )
  if 90 - 90: Iii / i1i1I1IIii1II + OOooOOo
def I1iIiIi11i11 ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoO , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def IiII11I1I1IIi ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( oO00ooooO0o )
 for url in IIi :
  OOo00ooOoO0o ( url )
  if 44 - 44: OOooOOo
def O00oOo00o0o ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , OoO , 8065 , iiIi1IIiIi + 'classictv.png' )
def I111 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
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
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + OoO , 8071 , iiIi1IIiIi + 'streams.png' )
def OOoOI1i1i1Iii1 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO0O000 , url in IIi :
  if '(Free Access)' in OO0O000 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def OoO00Ooooo ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
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
   OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
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
 for oOo0O , url , OO0O000 , iIi1iI in IIi :
  if 'category' in url :
   OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]   ' + iIi1iI + '[/COLOR]' , url , 90006 , oOo0O , iiIi1IIiIi + 'Jizbox.png' , '' )
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
 for url , OO0O000 , iIi1iI in IIi :
  if 'category' in url :
   OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORorange]' + iIi1iI + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIiII = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0O , '' , '' )
 for url in III1II1iiI11 :
  ii1I ( '[COLORred]NEXT[/COLOR]' , iIiII + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OO00iI1iII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  o0iiI11 ( 'http://www.perfectgirls.net' + url )
def o0iiI11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIIi1IIi ( 'http://' + url )
def OOOoO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , iIi1iI in IIi :
  OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - No of Videos : [COLORorange]' + iIi1iI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOii1iiiiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  OooO0O0Ooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , iIi1iI in IIi :
  OooO0O0Ooo ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - No of Videos : [COLORorange]' + ( iIi1iI + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 6 - 6: iI11I1II1I1I - Ii / Ii1I - I11i
def o00Oooo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  OooO0O0Ooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , ooo000o in IIi :
  OooO0O0Ooo ( OO0O000 + '--' + ( ooo000o ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 5 - 5: IiI1i11I - IiI1i11I / i1IiiiI1iI % I1ii11iIi11i
  if 61 - 61: i1i1I1IIii1II - Ii1I / IiI1i11I % Ii1I + oO0o / I1ii11iIi11i
def iii111iiI11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , url , OO0O000 , OOOOO0o0OOo , iiIii in IIi :
  OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + iiIii + ' - [COLORred]' + OOOOO0o0OOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0O , oOo0O , iiIii + ' - ' + OOOOO0o0OOo )
 i111O0Oo00oO0OoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in i111O0Oo00oO0OoO :
  OooO0O0Ooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 52 - 52: ii - o0o00Oo0O . oooOo0oo0oo . IiI1i11I . i1i1I1IIii1II
def iII1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  OooO0O0Ooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1i1i1I ) )
 for url , OO0O000 in IIi :
  if '/c/' in url :
   OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 10 - 10: i1IiiiI1iI * ooOoO0O00 % o0ii1I % Ii1I - o0ii1I * oO0o
   if 15 - 15: i1iIi
def iiioO000oO0oO ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO00O000 = ( I1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIII1ii = OO00O000 . lower ( )
 Oo0o00o = 'http://www.xvideos.com/?k=' + IIII1ii
 print Oo0o00o + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( Oo0o00o )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OoO , OO0O000 , OOOOO0o0OOo , iiIii in IIi :
  OooO0O0Ooo ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + iiIii + ' - [COLORred]' + OOOOO0o0OOo + '[/COLOR]' , 'http://www.xvideos.com' + OoO , 10108 , oOo0O , oOo0O , iiIii + ' - ' + OOOOO0o0OOo )
 i111O0Oo00oO0OoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for OoO in i111O0Oo00oO0OoO :
  OooO0O0Ooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + OoO , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
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
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in IiIi1I1 :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
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
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0O0OOo00Oo ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OO0O000 , oOo0O in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8092 , oOo0O )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI1iIIiIi1Ii ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0oOoOOO000 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O in O0oOoOOO000 :
  oOo0O = oOo0O
 for url , OO0O000 in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 8092 , oOo0O )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 57 - 57: I11i - III1iiIii . oooOo0oo0oo
def IIiIi ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 45 - 45: I1ii11iIi11i
  if 4 - 4: Iii
  if 60 - 60: IIiIiII11i + i1IiiiI1iI / i1i1I1IIii1II % ii - ooOoO0O00
  if 57 - 57: i1iIi
OO00O0O = '{PQ},' ; o0oo0oo0 = '{SC},' ; IIi1II = '{XG},' ; OOOoooO0o0o = '{JP},' ; OOoOoOO00 = '{HW},' ; o0O00 = '{RT},'
def O00OoO0o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 I11Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 OoO = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1
 i1iiIIi1I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 4 - 4: Ii % IiI1i11I
 i1i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oO0ooOoO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 41 - 41: IiI1i11I + i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( OoO )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 O0o00O0Oo0 = O00O0oOO00O00 ( OO0oOOo0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0I11iII = O00O0oOO00O00 ( ooOo0OoO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiIiI = O00O0oOO00O00 ( i1iiIIi1I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIIIIiiIii = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 96 - 96: o0o00Oo0O + oooOo0oo0oo . i1iIi + oooOo0oo0oo
 if 43 - 43: Ii
 Oo0o = O00O0oOO00O00 ( i1i1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 oOOoOoo0O0 = O00O0oOO00O00 ( oO0ooOoO )
 if 65 - 65: o0o00Oo0O / IiI1i11I . ooOoO0O00 * IiI1i11I / iI11I1II1I1I - i1i1I1IIii1II
 if iIIIIiiIii != 'Failed' :
  Ii11iI1ii1111 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIiiIii )
  for OoO , OO0O000 in Ii11iI1ii1111 :
   i111i1i = O00O0oOO00O00 ( OoO )
   IiIii1I1I = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i111i1i )
   for OO0Oooo0oo , I1i111IiIiIi1 in IiIii1I1I :
    I1i111IiIiIi1 = ( I1i111IiIiIi1 . replace ( '.' , ' ' ) )
    if IIII1ii in I1i111IiIiIi1 . lower ( ) :
     if '.mkv' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.mp4' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.avi' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 222 , '' , '' , '' )
     elif '.wav' in OO0Oooo0oo :
      i11I1II1I11i ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 222 , '' , '' , '' )
     else :
      ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source Technica[/COLOR]' ) , OoO , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 55 - 55: I11i . Ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: i1i1I1IIii1II
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi1I1i , OO0O000 in IiIi1I1 :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1i1IIIIIIIi + iIIIiIi1I1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in I1i11 :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORred] source RaizTv[/COLOR]' ) , OoO , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if O0o00O0Oo0 != 'Failed' :
  OooOOOO0O0 = [ ]
  oOo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o00O0Oo0 )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in oOo0 :
   if I1 in OO0O000 . lower ( ) :
    if OO0O000 in OooOOOO0O0 :
     pass
    else :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , OoO , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
     OooOOOO0O0 . append ( OO0O000 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0I11iII != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0I11iII )
  for OoO , oOo0O , OO0O000 in i1IIi1i1Ii1 :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + OoO , 7067 , oOo0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if Oo0o != 'Failed' :
  i11IiIIi11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0o )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in i11IiIIi11I :
   if I1 in OO0O000 . lower ( ) :
    i11I1II1I11i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , OoO , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
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
 i1II11Iii1I = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
 for IiIIi1I1I11Ii in i1II11Iii1I :
  o0OO = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  iIIIIiiIii = O00O0oOO00O00 ( o0OO )
  if iIIIIiiIii != 'Failed' :
   Ii11iI1ii1111 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIiiIii )
   for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in Ii11iI1ii1111 :
    if I1 in OO0O000 . lower ( ) :
     i11I1II1I11i ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , OoO , 222 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 49 - 49: I1ii11iIi11i
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
     if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
 i1II11Iii1I = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 9 - 9: III1iiIii . Iii
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
 for IiIIi1I1I11Ii in i1II11Iii1I :
  o0OO = I11Ii + IiIIi1I1I11Ii
  OO0OoOo0OOO = O00O0oOO00O00 ( o0OO )
  if OO0OoOo0OOO != 'Failed' :
   Ii1ii11IIIi = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OO0OoOo0OOO )
   for iIIIiIi1I1i , OO0O000 in Ii1ii11IIIi :
    if I1 in OO0O000 . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( I11Ii + IiIIi1I1I11Ii + iIIIiIi1I1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 96 - 96: i1iIi % o0o00Oo0O
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: oOo0O0Ooo - IiI1i11I / Ii1I . Ii1I + Ii1I
def OoOoO ( ) :
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
 IIII1ii = I1 . lower ( )
 if 6 - 6: oO0o
 if 82 - 82: iI11I1II1I1I . Iii / III1iiIii / oooOo0oo0oo * IIiIiII11i % i1i1I1IIii1II
 OO0Oooo0oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I1 ) . replace ( ' ' , '+' )
 iIiII = 'http://onlinemovies.tube/?s=' + ( I1 ) . replace ( ' ' , '+' )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 62 - 62: IIiIiII11i
 i1iiIIi1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 96 - 96: Iii % OOooOOo * Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . i1iIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
 if 77 - 77: I11i
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( OO0Oooo0oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 OO0OoOo0OOO = O00O0oOO00O00 ( I1III11iiii11i1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 63 - 63: i1iIi * i1i1I1IIii1II + i1iIi * o0ii1I + I1ii11iIi11i / Ii1I
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
 IiiIiI = O00O0oOO00O00 ( i1iiIIi1I )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 iIIIIiiIii = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
 if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
 if iIIIIiiIii != 'Failed' :
  Ii11iI1ii1111 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( iIIIIiiIii )
  for OoO , OO0O000 in Ii11iI1ii1111 :
   i111i1i = O00O0oOO00O00 ( OoO )
   IiIii1I1I = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i111i1i )
   for OO0Oooo0oo , I1i111IiIiIi1 in IiIii1I1I :
    if IIII1ii in I1i111IiIiIi1 . lower ( ) :
     ii1I ( ( '[COLOR' + ooOoOoo0O + ']*' + I1i111IiIiIi1 + '-[COLORgold] source ' + OO0O000 + '[/COLOR]' ) , OoO + OO0Oooo0oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IiiIiI != 'Failed' :
  iIiIi1iI11iiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIiI )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in iIiIi1iI11iiI :
   if IIII1ii in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] source HeroVision[/COLOR]' ) , OoO , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
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
  iI1iIiiiI1I1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for OoO , oOo0O , OO0O000 , OOOOOo in i1Iii1i1I :
   if IIII1ii in OO0O000 . lower ( ) :
    if 'season' in OOOOOo :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90054 , oOo0O , oOo0O , '' )
    if 'episodes' in OOOOOo :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90044 , oOo0O , oOo0O , '' )
  for OoO in iI1iIiiiI1I1 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , OoO , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 45 - 45: oOo0O0Ooo
   iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( IIOOO0O00O0OOOO )
  for OoO , OO0O000 , oOo0O in OOoOOO000O0 :
   if IIII1ii in OO0O000 . lower ( ) :
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
   if IIII1ii in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i1i1IIIIIIIi + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OO0O000 in I1i11 :
   if IIII1ii in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oo0o0oOo + OO0O000 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if OO0OoOo0OOO != 'Failed' :
  Ii1ii11IIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoOo0OOO )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in Ii1ii11IIIi :
   if IIII1ii in OO0O000 . lower ( ) :
    ii1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OO0O000 + '-[COLORgold] Source Scooby[/COLOR]' ) , OoO , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , oo0O0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
 O0OOO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IiIIi1I1I11Ii in O0OOO0 :
  o0OO = oO0 + IiIIi1I1I11Ii + oOoOooOo0o0
  Oo0o = O00O0oOO00O00 ( o0OO )
  if Oo0o != 'Failed' :
   i11IiIIi11I = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo0o )
   for OO0O000 , oo0O0 , OoO , oOo0O , iI , o000O000 in i11IiIIi11I :
    if IIII1ii in OO0O000 . lower ( ) :
     ii1I ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - Source Pandoras[/COLOR]' , OoO , o000O000 , oOo0O , iI , oo0O0 )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + OoO ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iIiii = '{ZH},' ; oooOoo0oo00O0O = '{IX},' ; II11iii1iI1ii = '{LM},'
if 34 - 34: i1iIi . i1iIi
def OOoOi11i ( url ) :
 IIII1II11Iii = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IIII1II11Iii )
 for url , II11I , iIIi1Ii1III , OO0O000 in IIi :
  oOoo000 ( ( II11I ) . replace ( 'Sezon' , ' Season ' ) + ( iIIi1Ii1III ) . replace ( 'Bölüm' , ' Episode ' ) + OO0O000 , url , 8063 , '' )
  if 46 - 46: o0ii1I * o0ii1I / i1i1I1IIii1II * i1IiiiI1iI
  if 37 - 37: OOooOOo + III1iiIii
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + i1IiiiI1iI
  if 58 - 58: i1IiiiI1iI * o0o00Oo0O / o0ii1I + oOo0O0Ooo - Ii1I * I1ii11iIi11i
def ooO0oO00oO0o ( url ) :
 IIII1II11Iii = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IIII1II11Iii )
 for url , OO0O000 in IIi :
  OooOo00o ( OO0O000 , url , 222 , '' )
  if 100 - 100: Ii1I - III1iiIii / IiI1i11I * oOo0O0Ooo / Iii / o0o00Oo0O
  if 57 - 57: ooOoO0O00 % i1iIi
  if 69 - 69: I11i
  if 69 - 69: i1IiiiI1iI
def OoOoooO0o0O00o0O ( ) :
 if 68 - 68: OOooOOo
 IIII1II11Iii = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIII1II11Iii )
 for OoO , oOo0O , OO0O000 , iIIi1Ii1III in IIi :
  oOoo000 ( OO0O000 + '  -  ' + ( iIIi1Ii1III ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , OoO , 8063 , oOo0O )
  if 65 - 65: i1i1I1IIii1II
def o000oOOO ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 , oOo0O in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 8002 , oOo0O )
def iIi1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , time , url , OO0O000 , oo00o000O in IIi :
  ii1I ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , time ) , url , 1015 , oOo0O , oo00o000O )
  if 65 - 65: o0ii1I
def O0o0OOOooo0 ( ) :
 if 18 - 18: oOo0O0Ooo
 oOoo000 ( 'Coronation Street' , '' , 8001 , '' )
 oOoo000 ( 'Eastenders' , '' , 8002 , '' )
 oOoo000 ( 'Emmerdale' , '' , 8003 , '' )
 oOoo000 ( 'Hollyoaks' , '' , 8004 , '' )
 oOoo000 ( 'Im a Celebrity' , '' , 8005 , '' )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
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
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , OoO . replace ( '\\/' , '/' ) , 8006 , oOo0O )
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
 iiIIIiIii = xbmcgui . ListItem ( name , '' , '' )
 iiIIIiIii . setPath ( iiiiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
 if 65 - 65: I11i - ii / OOooOOo
 if 49 - 49: i1i1I1IIii1II
def o0o000OOO ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , OoO , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for OoO , OO0O000 in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , OoO , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 36 - 36: i1IiiiI1iI * i1IiiiI1iI % oOo0O0Ooo % o0o00Oo0O . oOo0O0Ooo % ii
def OOooooo00OO ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'Movies' in OO0O000 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( OoO ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def O0O0oOO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0O )
 for url in i1Iii1i1I :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 40 - 40: oO0o - oO0o
  if 58 - 58: III1iiIii * IiI1i11I . oOo0O0Ooo + oooOo0oo0oo
def IIiiI ( url ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url , oOo0O in IIi :
  if '{{' in OO0O000 :
   pass
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0O )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IIIi11II1 = '{UJ},' ; iIi1ii1I1iiI = '{WE},' ; i1I1IIIII1IIi = '{WP},' ; i11iii1II1I1 = '{PP},'
def IiIi11iI1IIi ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url , oOo0O in IIi :
  if '{{' in OO0O000 :
   pass
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0O )
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
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
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
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , OO0O000 in i1Iii1i1I :
  if '(cooltvseries.com)' in OO0O000 :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def II1iIiiiIiiII ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oO00ooooO0o )
 for url in IIi :
  iIIi1IIi ( ( url ) . replace ( ' ' , '%20' ) )
o0o0 = '{XX},' ; IIiI = '{UD},' ; oOOOO00o00 = '{YT},' ; OOo00o0oOO0o = '{JS},' ; I1ii1 = '{PF},'
if 84 - 84: IiI1i11I . IIiIiII11i - ii + Iii % o0ii1I % ii
def IiiiI1i1i ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 , oOo0O in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( OoO ) ) , 222 , oOo0O )
  if 22 - 22: o0o00Oo0O + oooOo0oo0oo
def III1IiIi1 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  if 'youtu' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0O )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 68 - 68: i1IiiiI1iI + III1iiIii . iI11I1II1I1I
def Ii1iiIi1iiI ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 77 - 77: Ii / i1IiiiI1iI / Ii % OOooOOo - i1IiiiI1iI
def O0oOoo0o0o0 ( url ) :
 oO00ooooO0o = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 222 , oOo0O )
  if 73 - 73: III1iiIii / o0ii1I + i1IiiiI1iI . oooOo0oo0oo - IIiIiII11i / iI11I1II1I1I
  if 79 - 79: i1IiiiI1iI * I1ii11iIi11i . I11i - i1IiiiI1iI
  if 16 - 16: oOo0O0Ooo - o0o00Oo0O * Ii1I . Ii1I % oooOo0oo0oo
  if 39 - 39: IIiIiII11i / Iii - OOooOOo * OOooOOo - o0ii1I
  if 8 - 8: o0o00Oo0O . Ii
def O0O0o00o00O00 ( ) :
 if 94 - 94: Ii1I + IIiIiII11i - Ii1I + Iii
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
 if 90 - 90: iI11I1II1I1I
 if 18 - 18: Iii * Ii1I / Ii / iI11I1II1I1I * ii . oooOo0oo0oo
def oO000oOo0oO0 ( Cat_Name ) :
 if 2 - 2: I11i - oOo0O0Ooo - Ii / ii
 OOOO0o = False
 o0OOo0Ooo = '0'
 if Cat_Name == 'All Channels' : OOOO0o = True
 if Cat_Name == 'Entertainment' : o0OOo0Ooo = '1'
 if Cat_Name == 'Movies' : o0OOo0Ooo = '2'
 if Cat_Name == 'Music' : o0OOo0Ooo = '3'
 if Cat_Name == 'News' : o0OOo0Ooo = '4'
 if Cat_Name == 'Sports' : o0OOo0Ooo = '5'
 if Cat_Name == 'Documentary' : o0OOo0Ooo = '6'
 if Cat_Name == 'Kids' : o0OOo0Ooo = '7'
 if Cat_Name == 'Food' : o0OOo0Ooo = '8'
 if Cat_Name == 'Religious' : o0OOo0Ooo = '9'
 if Cat_Name == 'USA Channels' : o0OOo0Ooo = '10'
 if Cat_Name == 'Other' : o0OOo0Ooo = '11'
 if 19 - 19: o0ii1I + I1ii11iIi11i . oO0o . oOo0O0Ooo * IiI1i11I . iI11I1II1I1I
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for OO0O000 , oOo0O , Oooo000ooo00O in IIi :
  iiI11I1iII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0O ) . replace ( '\\' , '' )
  if Oooo000ooo00O == o0OOo0Ooo :
   oOoo000 ( OO0O000 , '' , 7022 , iiI11I1iII )
  elif OOOO0o == True :
   oOoo000 ( OO0O000 , '' , 7022 , iiI11I1iII )
  else : pass
  if 26 - 26: Ii1I - ooOoO0O00 . oooOo0oo0oo . o0ii1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: III1iiIii - Iii
def I1iOoO00O ( Search_Name ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oO00ooooO0o )
 for oOo0O , OoO , iIiII , i1i1IIIIIIIi in IIi :
  iiI11I1iII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0O ) . replace ( '\\' , '' )
  OooOo00o ( Search_Name + ': Link 1' , ( OoO ) . replace ( '\\' , '' ) , 222 , iiI11I1iII )
  OooOo00o ( Search_Name + ': Link 2' , ( iIiII ) . replace ( '\\' , '' ) , 222 , iiI11I1iII )
  OooOo00o ( Search_Name + ': Link 3' , ( i1i1IIIIIIIi ) . replace ( '\\' , '' ) , 222 , iiI11I1iII )
  if 87 - 87: i1iIi - Ii / iI11I1II1I1I % oOo0O0Ooo
def ooo0o ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OooOo00o ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def o0OOO0O00Oo00 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OooOo00o ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def ooooO0O ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oO00ooooO0o )
 for OO0O000 , OoO in IIi :
  OooOo00o ( OO0O000 , ( OoO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 15 - 15: ii
def iII1iOO00o0O0OO0o0 ( url ) :
 url
 iII1i11 = xbmcgui . ListItem ( OO0O000 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
 return
 if 10 - 10: oooOo0oo0oo
 if 12 - 12: III1iiIii . Ii + ii % Ii
def IIiI1iIiii ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oO00ooooO0o )
 for url , oo0O0 , oOo0O , OO0O000 in IIi :
  ii1I ( OO0O000 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0O , '' , ( oo0O0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 53 - 53: i1IiiiI1iI % Ii1I
def ii11iIII111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , oo0O0 , oOo0O in IIi :
  i11I1II1I11i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0O , '' , oo0O0 )
  iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 Oo0O0o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00O000o in Oo0O0o :
  o0oO0oooOoo = ( o00O000o ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  ii1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0O , '' , o0oO0oooOoo )
  if 82 - 82: I11i % III1iiIii - i1iIi
def OoOoO0o0oO0 ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 21 - 21: o0o00Oo0O - I11i
 if 51 - 51: ii + Iii % OOooOOo . o0ii1I % Ii * i1iIi
 if 49 - 49: oO0o - I1ii11iIi11i - Ii1I
def IiIi1III ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( ( OO0O000 ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def ii1I1IIi ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( OO0O000 , url , 9032 , iiIi1IIiIi + 'icon.png' )
def o00oOO0OOo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if '=' in OO0O000 :
   pass
  else :
   OooOo00o ( ( OO0O000 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def OooOooO0OoOoo0o ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if '=' in OO0O000 :
   pass
  else :
   OooOo00o ( OO0O000 , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 27 - 27: oO0o % i1iIi - o0o00Oo0O
   if 44 - 44: Ii1I + Ii1I - oooOo0oo0oo / IIiIiII11i
   if 36 - 36: oO0o - I11i . IiI1i11I % IiI1i11I
def iI1II ( url ) :
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if 'mp4' in url :
   pass
  else :
   OooOo00o ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0o0oO0 ( url ) :
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  if 'mp4' in url :
   OooOo00o ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: IiI1i11I / i1iIi
 if 17 - 17: OOooOOo
 if 40 - 40: o0o00Oo0O - IiI1i11I
def II1i1 ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'Daily' in OO0O000 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , OoO , 9008 , O0O )
def ooO0OoOO0 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def o0oo00 ( url ) :
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  OooOo00o ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 92 - 92: ooOoO0O00
def OOO0OOo0OoO ( ) :
 oO00ooooO0o = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if '.m3u' in OoO :
   oOoo000 ( ( OO0O000 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + OoO ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def oO00OOO ( url ) :
 oO00ooooO0o = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oO00ooooO0o )
 for OO0O000 , url in IIi :
  OooOo00o ( ( OO0O000 ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 48 - 48: iI11I1II1I1I . oO0o + Ii - o0ii1I . oO0o
def Ii1I11ii1i ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  if 'category' in OoO :
   oOoo000 ( OO0O000 , 'http://www.disclose.tv/' + OoO , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 89 - 89: ooOoO0O00
   if 92 - 92: iI11I1II1I1I * Ii1I
def i1I11Iiii ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oO00ooooO0o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , oOo0O in IIi :
  oOoo000 ( OO0O000 , 'http://www.disclose.tv/' + url , 7011 , oOo0O )
 for url in next :
  oOoo000 ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 78 - 78: i1IiiiI1iI
  if 62 - 62: oOo0O0Ooo + ii + i1IiiiI1iI
def IiIII ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oO00ooooO0o )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oO00ooooO0o )
 IiIi1I1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  if 'http' in url :
   OooOo00o ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , OO0O000 in i1Iii1i1I :
  OooOo00o ( OO0O000 , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in IiIi1I1 :
  OooOo00o ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 3 - 3: I1ii11iIi11i + oooOo0oo0oo - oOo0O0Ooo
  if 60 - 60: o0o00Oo0O / ooOoO0O00 % Ii / IiI1i11I
def ooo00o0OO0 ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( OO0O000 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 94 - 94: Iii
def IIIi1IIiI ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IiIi1I1i = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiiIIi = len ( IiIi1I1i )
 if 10 - 10: OOooOOo / i1i1I1IIii1II % I1ii11iIi11i
 if 15 - 15: Iii - iI11I1II1I1I % o0ii1I
 if IIiiIIi == 1 :
  for i1Iii in IiIi1I1i :
   i1Iii = i1Iii . replace ( 'player' , 'watch' )
   oOOooo = i1Iii + '&fv=&sou='
   IiI11IiIIi = OooOoooOo ( oOOooo )
   oOOo0OoooOo = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( IiI11IiIIi )
   for iIIIII1iiiiII in oOOo0OoooOo :
    I1I1IiIiIIi1I = False
    Resolve ( iIIIII1iiiiII )
    if 74 - 74: ii + Ii1I % o0o00Oo0O
 elif IIiiIIi > 1 :
  if 32 - 32: Ii1I + Ii1I
  for i1Iii in IiIi1I1i :
   O0OOO00 = OooOoooOo ( i1Iii )
   IIIIi11i = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( O0OOO00 )
   OO0ooo = IIIIi11i
   OO0ooo = ( str ( OO0ooo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OO0ooo
   OooOo00o ( 'DOUBLE LINK' , OO0ooo , 424 , '' )
   if 94 - 94: o0ii1I / oooOo0oo0oo * Ii1I % Ii1I + III1iiIii
   for url in IIIIi11i :
    oOoo000 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iIiII = Google . resolve ( url )
    except :
     pass
    try :
     O0OO0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iIiII ) )
     for OoII1111iII1 , iio0000oO0OOOo0 in O0OO0 :
      if 64 - 64: o0ii1I - IiI1i11I
      HD_URLS . append ( OoII1111iII1 )
      SD_URLS . append ( iio0000oO0OOOo0 )
    except :
     pass
 else :
  pass
  if 12 - 12: ooOoO0O00
def oo0O0o0O ( ) :
 if 87 - 87: IiI1i11I - oO0o * I1ii11iIi11i - III1iiIii . Ii1I * ooOoO0O00
 if 79 - 79: IiI1i11I
 oOoo000 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 32 - 32: o0ii1I % Iii + oooOo0oo0oo % ii
 oOoo000 ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 68 - 68: Iii
 if 13 - 13: Ii - i1iIi
def OoOoo0ooO0000 ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , 'http://cnfstudio.com/genre/' + OoO , 7003 , iiIi1IIiIi + 'icon.png' )
  if 5 - 5: IIiIiII11i * Iii
iIii1 = xbmcgui . Dialog ( )
if 21 - 21: oOo0O0Ooo
OOO0o0O = '{UN},' ; OoO0 = '{IG},' ; O00OO0OoO00oO = '{PL},' ; iiiI1iiIiII1 = '{LO},' ; oOo0oOOoo0O = '{LP},' ; iI1IiI11Ii11i = '{HA},' ; O0oi1IiI1I = '{XD},' ; O00OOoOo0 = '{TA},' ; O0ooO0oOO = '{DP},' ; ii111I1iII1i1 = '{JT},' ; O000000oooOOo = '{JJ},' ; I11iiI1 = '{MM},' ; I1I = '{FQ},' ; oo000oooooooO = '{HH},'
if 18 - 18: i1i1I1IIii1II * I1ii11iIi11i % Ii + o0o00Oo0O % oooOo0oo0oo . oooOo0oo0oo
def ooO00OoO ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oO00ooooO0o )
 oo0OOO0O0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oO00ooooO0o )
 for oOo0O , url , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0O )
 oo0OOO0O0 = oo0OOO0O0
 for url in oo0OOO0O0 :
  oOoo000 ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . III1iiIii / i1i1I1IIii1II
def i1ii1iIiI1 ( url ) :
 if 17 - 17: Ii . o0ii1I - III1iiIii / iI11I1II1I1I + ii - i1iIi
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  oOoooO0 = oOo0oOo ( iiI111I1iIiI )
  IiI1II = oOo0oOo ( url )
  if 19 - 19: IiI1i11I
  if 32 - 32: Iii % i1iIi % ii . i1iIi % Ii + IIiIiII11i
def oOo0oOo ( url ) :
 if 25 - 25: i1iIi
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url in IIi :
  OOo00ooOoO0o ( url )
  if 83 - 83: o0ii1I / ii * i1i1I1IIii1II . oOo0O0Ooo . ooOoO0O00
  if 59 - 59: Iii . Iii * oOo0O0Ooo - o0ii1I % OOooOOo
def IiIIIiI11i1 ( ) :
 ii1I ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 ii1I ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 14 - 14: I1ii11iIi11i % iI11I1II1I1I - iI11I1II1I1I . iI11I1II1I1I - I11i * i1IiiiI1iI
def II1iIIII ( ) :
 if os . path . exists ( II ) :
  I1iI11IiIi1II = open ( II , 'r' )
  for iII1i11 in I1iI11IiIi1II :
   OooooO0000 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1i11 )
   for OO0O000 , OoO in OooooO0000 :
    OooOo00o ( OO0O000 , OoO , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 95 - 95: Iii - iI11I1II1I1I
def iIIioo0 ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = oOOo000oOoO0 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OO0O000 , url in IIi :
   url = ( url ) . strip ( )
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 42 - 42: Iii / Ii
  if 7 - 7: Iii
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoO in IIi :
  OoO = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + OoO
 OO0O000 = 'plugin.video.GenieTv'
 if 50 - 50: Ii . Ii * ooOoO0O00 / Ii . ooOoO0O00 - IIiIiII11i
 oooOOoo0o00O0O0oO ( OoO , OO0O000 )
 if 94 - 94: I11i - Iii % i1i1I1IIii1II % I11i + Iii
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for OoO in IIi :
  OoO = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + OoO
 OO0O000 = 'repository.GenieTv'
 if 31 - 31: i1IiiiI1iI * I11i * IIiIiII11i + o0o00Oo0O / IiI1i11I * i1iIi
 oooOOoo0o00O0O0oO ( OoO , OO0O000 )
 if 52 - 52: iI11I1II1I1I / IiI1i11I . o0o00Oo0O * III1iiIii . oOo0O0Ooo
 if 67 - 67: IIiIiII11i + o0ii1I - oOo0O0Ooo * i1iIi
def O0O00Oo ( ) :
 oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOo0O0Oo00oO )
 if I111I1Iiii1i == 0 :
  iiIiiIii1IiI ( )
 if I111I1Iiii1i == 1 :
  Ooooo00 ( )
  if 82 - 82: o0o00Oo0O - i1IiiiI1iI - I11i - o0ii1I - i1iIi
  if 15 - 15: I11i . o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . i1i1I1IIii1II * ii
  if 32 - 32: i1iIi / IIiIiII11i . o0o00Oo0O . i1iIi % oOo0O0Ooo - I11i
  if 69 - 69: o0ii1I - oOo0O0Ooo * oooOo0oo0oo . iI11I1II1I1I * OOooOOo . ii
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
iiOo00o0o = 'https://addons.tvaddons.ag/'
if 74 - 74: I1ii11iIi11i + oooOo0oo0oo . I11i / OOooOOo + o0ii1I + ooOoO0O00
def Ooooo00 ( ) :
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 Oo0o00o = 'https://addons.tvaddons.ag/search/?keyword=' + IIII1ii
 II11iIiIIIiI = OooOoooOo ( Oo0o00o )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for OoO , ii1 , OO0O000 in IIi :
  ii1I ( OO0O000 , OoO , 10054 , 'https://addons.tvaddons.ag/' + ii1 , Oo00OOOOO , '' )
  if 82 - 82: o0ii1I * Iii / oOo0O0Ooo * iI11I1II1I1I / i1iIi + III1iiIii
  if 30 - 30: i1i1I1IIii1II . Ii / Iii + ooOoO0O00 - Iii
def iiIiiIii1IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( iiOo00o0o )
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
def oooOOoo0o00O0O0oO ( url , name ) :
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
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , ii1 , OO0O000 in IIi :
  oOoo000 ( OO0O000 , url , 1007 , ii1 )
def i1I111Ii1I ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , ii1 , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , ii1 )
  if 100 - 100: Ii * IiI1i11I * i1iIi
def iiIi1i1iIi1I ( ) :
 oO00ooooO0o = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , iiiI1I1iIIIi1 , oo0O0 , iI , OO0O000 in IIi :
  Ii11I1i ( OO0O000 , 100109 , OoO , image = iiiI1I1iIIIi1 , isFolder = True )
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
 for iIiII , iiiI1I1iIIIi1 , oo0O0 , iI , OO0O000 in IIi :
  o0O0oOooo . append ( [ iIiII , OO0O000 ] )
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
      for iIiIIi1I11II1IiI , oo00o0Oo0O0 in IiIi1I1 :
       OOoOoo = OooOoooOo ( iIiIIi1I11II1IiI )
       I1i11 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for OOo00 , iiI111I1iIiI in I1i11 :
        if 'panda' in iiI111I1iIiI :
         O0o00O0Oo0 = OooOoooOo ( iiI111I1iIiI )
         oOo0 = re . compile ( "url: '(.+?)'" ) . findall ( O0o00O0Oo0 )
         for ii11I11ii1 in oOo0 :
          if 'http' in ii11I11ii1 :
           iiIIIiIii = xbmcgui . ListItem ( o0o000O0o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : o0o000O0o [ 1 ] } )
           iiIIIiIii . setProperty ( "IsPlayable" , "true" )
           ooOO0000O0o . add ( ii11I11ii1 , iiIIIiIii )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
           if 84 - 84: I1ii11iIi11i % i1IiiiI1iI . I1ii11iIi11i / i1iIi * o0ii1I - III1iiIii
def Ii11I1i ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 I111IIiii1Ii = sys . argv [ 0 ]
 I111IIiii1Ii += '?mode=' + str ( mode )
 I111IIiii1Ii += '&title=' + urllib . quote_plus ( name )
 I111IIiii1Ii += '&image=' + urllib . quote_plus ( image )
 I111IIiii1Ii += '&page=' + str ( page )
 if url != '' :
  I111IIiii1Ii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  I111IIiii1Ii += '&keyword=' + urllib . quote_plus ( keyword )
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  iiIIIiIii . addContextMenuItems ( contextMenu )
 if infoLabels :
  iiIIIiIii . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  iiIIIiIii . setProperty ( "IsPlayable" , "true" )
 iiIIIiIii . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = isFolder )
 if 16 - 16: oooOo0oo0oo % III1iiIii - IIiIiII11i - I11i * Ii / i1IiiiI1iI
 if 74 - 74: IiI1i11I % ooOoO0O00 / I1ii11iIi11i . o0o00Oo0O
def I1IIIiI1I1ii1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , iconimage , oo0O0 , iI , name in IIi :
  if 'http' in url :
   if '.php' in url :
    Oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for iII1i11 in Oo :
     if iII1i11 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    IiiIiiiiI1III ( name , url , 1016 , iconimage , iI , oo0O0 )
   else :
    if 'youtube' in url :
     Oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in Oo :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0ooO0Oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iI , oo0O0 )
    else :
     Oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in Oo :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0ooO0Oo ( name , url , 222 , iconimage , iI , oo0O0 )
     iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
  else :
   iIIi1i111iI ( url , iconimage , name )
   if 10 - 10: III1iiIii % IIiIiII11i
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
  for url , ii1 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     oOoo000 ( name , url , 1016 , ii1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OooOo00o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ii1 )
     else :
      Oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in Oo :
       if iII1i11 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OooOo00o ( name , url , 222 , ii1 )
      iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
   else :
    iIIi1i111iI ( url , ii1 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 50 - 50: OOooOOo * IiI1i11I
def iIIi1i111iI ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oooO00oOoOO0o = ( url ) . replace ( oooOoo0oo00O0O , 'http' ) . replace ( IIiI , '.com' ) ;
 OoOo0O0 = ( oooO00oOoOO0o ) . replace ( II11iii1iI1ii , 'a' ) . replace ( IIi1II , 'b' ) . replace ( OOOoooO0o0o , 'c' ) . replace ( iIi1ii1I1iiI , 'd' ) . replace ( O00OO0OoO00oO , 'e' ) . replace ( ii111I1iII1i1 , 'f' ) ;
 oOo0I1IIiIIii1II1 = ( OoOo0O0 ) . replace ( o0o0 , 'g' ) . replace ( iI1IiI11Ii11i , 'h' ) . replace ( oOOOO00o00 , 'i' ) . replace ( I1ii1 , 'j' ) . replace ( OOoOoOO00 , 'k' ) . replace ( o0O00 , 'l' ) ;
 o0O0oOooooO00 = ( oOo0I1IIiIIii1II1 ) . replace ( oooOo0O , 'm' ) . replace ( OoOooOooOOoO , 'n' ) . replace ( II11 , 'o' ) . replace ( iIiOOO0oo0OO0o0 , 'p' ) . replace ( OOoO0 , 'q' ) . replace ( o00o0Ooo , 'r' ) ;
 II1I1 = ( o0O0oOooooO00 ) . replace ( iIi1i , 's' ) . replace ( i1I1IIIII1IIi , 't' ) . replace ( OooIiii1ii , 'u' ) . replace ( OOOO0oo0o0O , 'v' ) . replace ( IIiiiI , 'w' ) . replace ( ooooO0OOo0o0 , 'x' ) ;
 IIo000o0O0000o = ( II1I1 ) . replace ( ii1Iii1iiI11 , 'y' ) . replace ( i11ii1II , 'z' ) . replace ( OOO0o0O , '.' ) . replace ( OoO0 , '(' ) . replace ( iiiI1iiIiII1 , ')' ) . replace ( oOo0oOOoo0O , '/' ) ;
 ooOo00OOo0 = ( IIo000o0O0000o ) . replace ( iIiii , '1' ) . replace ( i11iii1II1I1 , '2' ) . replace ( ii1IIi , '3' ) . replace ( O00OOoOo0 , '4' ) . replace ( O0ooO0oOO , '5' ) . replace ( OOo00o0oOO0o , '6' ) ;
 iii1Ii = ( ooOo00OOo0 ) . replace ( O000000oooOOo , '7' ) . replace ( I11iiI1 , '8' ) . replace ( I1I , '9' ) . replace ( oo000oooooooO , '0' ) . replace ( OO00O0O , ':' ) . replace ( o0oo0oo0 , '%' ) ;
 url = ( iii1Ii ) . replace ( IIIi11II1 , '-' ) . replace ( O0oi1IiI1I , '_' ) ;
 OooOo00o ( name , url , 222 , iconimage ) ;
 if 98 - 98: Iii / Ii - I11i % I11i
 if 31 - 31: Iii
def Oooo0o00Oo00 ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for OoO , ii1 , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 1007 , ii1 )
def OoooOoo0Oooo ( url ) :
 if 17 - 17: IiI1i11I . IiI1i11I * oOo0O0Ooo
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , ii1 , OO0O000 in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , ii1 )
  if 98 - 98: III1iiIii
def i11iI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOiII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOiII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
 if 51 - 51: oooOo0oo0oo - ii / ii % ii
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
def OoOoOoOOo00Ooo0O ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO00ooooO0o )
 for url , oOo0O , OO0O000 in IIi :
  if '-dir-' in OO0O000 :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0O )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' , url , 1006 , oOo0O )
   if 75 - 75: iI11I1II1I1I - o0ii1I % o0o00Oo0O % III1iiIii
def II1II1iiIiI ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 i1IOO0O0ooOo = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '[To Parent Directory]' in OO0O000 :
   OO0O000 = 'HOME'
   pass
  elif 'HOME' in OO0O000 :
   pass
  elif '.m3u' in OO0O000 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , i1IOO0O0ooOo + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in OO0O000 :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , i1IOO0O0ooOo + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in OO0O000 :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , i1IOO0O0ooOo + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) , i1IOO0O0ooOo + url , 1012 , iiIi1IIiIi + 'music.png' )
def iI11iI1ii111II ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo0O , OO0O000 , url in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 77 - 77: Ii1I
def Ii1ii1i1 ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 i1IOO0O0ooOo = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  if '.mp3' in OO0O000 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '/' , '' ) , i1IOO0O0ooOo + url , 1011 , iiIi1IIiIi + 'music.png' )
def oo0oO ( ) :
 oO00ooooO0o = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for OoO , oOo0O , OO0O000 in IIi :
  oOoo000 ( OO0O000 , ( 'http://www.cyn.net/music/' + OoO ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0O ) . replace ( ' ' , '%20' ) )
def iII1IiI1I11i ( url , img ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 iIiII = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( iIiII + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 10 - 10: IIiIiII11i % oOo0O0Ooo % o0ii1I * Ii1I
def oOOoO0O ( url ) :
 oO00ooooO0o = oOOo000oOoO0 ( url )
 iIiII = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO00ooooO0o )
 for type , url , OO0O000 in IIi :
  if '[VID]' in type :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iIiII + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   oOOoO0O ( iIiII + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I11i / oO0o + IiI1i11I - ooOoO0O00 / ii / Ii1I
 if 56 - 56: i1i1I1IIii1II + oOo0O0Ooo . Iii
def iIii1Oo ( ) :
 I11Ii = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1ii = I1 . lower ( )
 OoO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 OO0Oooo0oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iIiII = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 67 - 67: III1iiIii / I11i + Iii % IiI1i11I - i1iIi - oOo0O0Ooo
 II11iIiIIIiI = O00O0oOO00O00 ( OoO )
 IIOOO0O00O0OOOO = O00O0oOO00O00 ( OO0Oooo0oo )
 o0o = O00O0oOO00O00 ( iIiII )
 if 44 - 44: o0ii1I . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for OoO , iiiI1I1iIIIi1 , oo0O0 , i11i1iIiii , OO0O000 in IIi :
   if I1 in OO0O000 . lower ( ) :
    ii1I ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , OoO , 1016 , iiiI1I1iIIIi1 , iI , oo0O0 )
    if 22 - 22: Iii * Ii1I . ii / I1ii11iIi11i / o0ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if IIOOO0O00O0OOOO != 'Failed' :
  OOoOOO000O0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIOOO0O00O0OOOO )
  for OoO , OO0O000 in OOoOOO000O0 :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + OoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 54 - 54: i1IiiiI1iI % o0ii1I + i1iIi
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for OoO , OO0O000 in i1Iii1i1I :
   if I1 in OO0O000 . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + OoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 45 - 45: o0ii1I / i1i1I1IIii1II * i1IiiiI1iI . o0ii1I
    iI1i11iII111 ( 'tvshows' , 'Media Info 3' )
    if 25 - 25: Ii1I / Ii1I
    if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
    if 84 - 84: i1iIi * ii + o0o00Oo0O
    if 84 - 84: ooOoO0O00 . Iii . ooOoO0O00 . I1ii11iIi11i
    if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
    if 5 - 5: iI11I1II1I1I * Ii + oO0o + Iii * o0o00Oo0O % i1iIi
oooOo0O = '{SF},' ; OoOooOooOOoO = '{IF},' ; II11 = '{PW},' ; ii1IIi = '{AM},' ; iIiOOO0oo0OO0o0 = '{GF},' ; OOoO0 = '{DD},' ; o00o0Ooo = '{UO},' ; iIi1i = '{LE},' ; OooIiii1ii = '{ZY},' ; OOOO0oo0o0O = '{UE},' ; IIiiiI = '{PE},' ; ooooO0OOo0o0 = '{JE},' ; ii1Iii1iiI11 = '{TH},' ; i11ii1II = '{LK},'
if 88 - 88: I11i / Ii * Ii1I
if 23 - 23: o0o00Oo0O / IiI1i11I
def iII1111III1I ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 8021 , iiIi1IIiIi + 'iwatch.png' )
  iI1i11iII111 ( 'movies' , 'MAIN' )
def Oo0oOo0Ooo ( url ) :
 oO00ooooO0o = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 , o0ooOOOo in IIi :
  oOoo000 ( OO0O000 + o0ooOOOo , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
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
  OooOo00o ( 'VidSpot - ' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  OooOo00o ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , OO0O000 in I1i11 :
  OooOo00o ( 'VidUp' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for OO0O000 , url in IiIi1I1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OooOo00o ( 'TheVideo - ' + OO0O000 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 63 - 63: IIiIiII11i
def iIII1 ( ) :
 oO00ooooO0o = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 1021 , iiIi1IIiIi + 'anime.png' )
  if 84 - 84: ii - ii / III1iiIii
  if 29 - 29: o0ii1I / o0o00Oo0O
def i11IIi ( ) :
 oO00ooooO0o = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO00ooooO0o )
 for OoO , OO0O000 in IIi :
  oOoo000 ( OO0O000 , OoO , 1002 , iiIi1IIiIi + 'anime.png' )
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
  oOoo000 ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oO00ooooO0o )
 for url , OO0O000 in IIi :
  oOoo000 ( OO0O000 , url , 1003 , O0oOOO0o0Ooo )
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
  OooOo00o ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
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
def oOOo000oOoO0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 19 - 19: i1IiiiI1iI * o0ii1I - i1i1I1IIii1II
def oOo000oOo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOoo0oo00000O = ( '%s%s' % ( oo0 , url ) )
 iiI111I1iIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , ii1 , OO0O000 in IIi :
  OooOo00o ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + OO0O000 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ii1 )
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
def OOo00ooOoO0o ( url ) :
 if 12 - 12: Iii
 iiIiI = open ( OOOO0OOoO0O0 , "a" )
 iiIiI . write ( 'url="' + url + '"\n' )
 iiIiI . close
 if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( OO0O000 ) )
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIIIi1i1I11i . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def I11II1iI ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  o0oO = '.mp4'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.mkv' in url :
  o0oO = '.mkv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.mp3' in url :
  o0oO = '.mp3'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.avi' in url :
  o0oO = '.avi'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.mov' in url :
  o0oO = '.mov'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.mpeg' in url :
  o0oO = '.mpeg'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.mpg' in url :
  o0oO = '.mpg'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.flv' in url :
  o0oO = '.flv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
 elif '.wmv' in url :
  o0oO = '.wmv'
  oOo0O0Oo00oO = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  I111I1Iiii1i = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOo0O0Oo00oO )
  if I111I1Iiii1i == 0 :
   OooO0OO ( url )
  if I111I1Iiii1i == 1 :
   i1O0o00o0Oo ( url , name , o0oO )
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
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 o0oOoO00o . update ( 100 , '%s' % OO0O000 )
 xbmc . sleep ( 1 )
 iIIIi1i1I11i . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 70 - 70: Iii . OOooOOo . Ii * i1iIi - IIiIiII11i
def iIIi1IIi ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIIi1i1I11i . play ( url ) . strip ( )
 except : pass
 if 23 - 23: III1iiIii
def O0oOo00O0Oo ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 IiiIiIi1iII = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iIIIi1i1I11i . play ( IiiIiIi1iII )
 xbmc . sleep ( 1 )
 iIIIi1i1I11i . play ( url )
 if 52 - 52: o0o00Oo0O * ii . i1IiiiI1iI . oooOo0oo0oo - IiI1i11I % IiI1i11I
 if 33 - 33: Ii - I11i . oOo0O0Ooo - i1i1I1IIii1II - IIiIiII11i + o0o00Oo0O
def oOO0OO0OO ( ) :
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
def oOoo000 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 66 - 66: I1ii11iIi11i - oO0o
def OooO0O0Ooo ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: i1IiiiI1iI
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 96 - 96: ii / Ii1I * oO0o
def OooOo00o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
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
   try : oooO = open ( announce ) ; O0oO00oOOooO = oooO . read ( )
   except : O0oO00oOOooO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0oO00oOOooO ) )
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
   try : oooO = open ( announce ) ; O0oO00oOOooO = oooO . read ( )
   except : O0oO00oOOooO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0oO00oOOooO ) )
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
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOO0OOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 14 - 14: ii
def oOOo0Oo0OO0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1iO00oo0oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 34 - 34: Ii + ii
def iII ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + i1iiIIiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 30 - 30: o0o00Oo0O * III1iiIii - i1IiiiI1iI % o0o00Oo0O * o0ii1I
def II1II111iIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OO0oO0ooOOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 41 - 41: I1ii11iIi11i % Ii
def iiOOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1IO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 64 - 64: iI11I1II1I1I
def o0OOOOooOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iIi1I1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 99 - 99: oOo0O0Ooo . i1iIi % IIiIiII11i / oOo0O0Ooo
def oOOOo000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1iIIiIi1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 85 - 85: oO0o + IIiIiII11i
def o0oo0oO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiI1ooOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 26 - 26: ooOoO0O00
def i111I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1Ii1i1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 42 , iiiI1I1iIIIi1 , iI , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 58 - 58: i1IiiiI1iI * oO0o * ooOoO0O00
def oooooo0O000o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiiIi1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OO0O000 , url , iiiI1I1iIIIi1 , iI , O0o in IIi :
  ii1I ( OO0O000 , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , O0o )
 iI1i11iII111 ( 'movies' , 'MAIN' )
 if 1 - 1: ii . Iii / OOooOOo + I11i % ooOoO0O00
 if 1 - 1: ii - oO0o - ii / IiI1i11I
 if 70 - 70: o0ii1I + Ii1I . IIiIiII11i * Ii
 if 87 - 87: o0ii1I / i1IiiiI1iI % OOooOOo * Ii1I - ii / OOooOOo
 if 24 - 24: Iii . oooOo0oo0oo * ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
 if 62 - 62: I11i % IIiIiII11i
 if 22 - 22: i1i1I1IIii1II - I11i
 if 89 - 89: oooOo0oo0oo
 if 34 - 34: IiI1i11I . oooOo0oo0oo
def o0o0oO0OOO ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( o0 ) :
     iII1Ii1ii111 = 0
     iII1Ii1ii111 += len ( i1I1ii1i )
     if iII1Ii1ii111 > 0 :
      for oooO in i1I1ii1i :
       os . unlink ( os . path . join ( ii1Io0oOO0 , oooO ) )
  iII11IIi1I1 = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( iII11IIi1I1 )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 70 - 70: I1ii11iIi11i
 if 93 - 93: IiI1i11I . Ii1I . I1ii11iIi11i . i1i1I1IIii1II . ii
 if 51 - 51: o0o00Oo0O - IiI1i11I
 if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
 if 43 - 43: i1IiiiI1iI + oO0o * ii
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
 if 53 - 53: o0ii1I - oooOo0oo0oo
def iiII ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
def i1I1I1iIIi ( url ) :
 Oo00OoooO0o = os . path . join ( oooOOOOO , 'addon_data' )
 I1III1ii1 = [
 ( Oo00OoooO0o ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( Oo00OoooO0o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Oo00OoooO0o , 'plugin.video.itv' , 'Images' ) ) ]
 if 23 - 23: oooOo0oo0oo
 i11iiII11i = 0
 if 83 - 83: I1ii11iIi11i . I11i + IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
 for iII1i11 in I1III1ii1 :
  if os . path . exists ( iII1i11 ) and not iII1i11 in [ oo0o0O00 , Oo00OoooO0o ] :
   for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( iII1i11 ) :
    iII1Ii1ii111 = 0
    iII1Ii1ii111 += len ( i1I1ii1i )
    if iII1Ii1ii111 > 0 :
     for oooO in i1I1ii1i :
      if not oooO in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( ii1Io0oOO0 , oooO ) )
       except :
        pass
      else : IIo0Oo0oO0oOO00 ( 'Ignore Log File: %s' % oooO )
     for OO00 in iII1i1ii :
      try :
       shutil . rmtree ( os . path . join ( ii1Io0oOO0 , OO00 ) )
       i11iiII11i += 1
       IIo0Oo0oO0oOO00 ( "[Success] cleared %s files from %s" % ( str ( iII1Ii1ii111 ) , os . path . join ( iII1i11 , OO00 ) ) )
      except :
       IIo0Oo0oO0oOO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , OO00 ) )
  else :
   for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( iII1i11 ) :
    for OO00 in iII1i1ii :
     if 'cache' in OO00 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ii1Io0oOO0 , OO00 ) )
       i11iiII11i += 1
       IIo0Oo0oO0oOO00 ( "[Success] wiped %s " % os . path . join ( iII1i11 , OO00 ) )
      except :
       IIo0Oo0oO0oOO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , OO00 ) )
       if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
 iiII ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % i11iiII11i )
 if 99 - 99: Ii1I % I1ii11iIi11i
 if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
 if 57 - 57: oooOo0oo0oo / Ii / i1IiiiI1iI - I1ii11iIi11i . iI11I1II1I1I
 if 84 - 84: III1iiIii
 if 42 - 42: o0o00Oo0O . i1IiiiI1iI / Iii
 if 69 - 69: OOooOOo / i1IiiiI1iI * oOo0O0Ooo
 if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
def IiOo00O0o0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( iI1IIi1I ) :
   iII1Ii1ii111 = 0
   iII1Ii1ii111 += len ( i1I1ii1i )
   if 42 - 42: ii / III1iiIii * IIiIiII11i
   if 77 - 77: IIiIiII11i + IiI1i11I . I11i / i1IiiiI1iI
   if iII1Ii1ii111 > 0 :
    if 100 - 100: o0ii1I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( iII1Ii1ii111 ) + " files found" , "Do you want to delete them?" ) :
     if 84 - 84: Iii * i1iIi + Ii + IiI1i11I - IIiIiII11i
     for oooO in i1I1ii1i :
      os . unlink ( os . path . join ( ii1Io0oOO0 , oooO ) )
     for OO00 in iII1i1ii :
      shutil . rmtree ( os . path . join ( ii1Io0oOO0 , OO00 ) )
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
 if 92 - 92: ii + oOo0O0Ooo % i1i1I1IIii1II . I11i
 if 4 - 4: Iii * oooOo0oo0oo / o0ii1I . i1i1I1IIii1II
 if 83 - 83: IiI1i11I + Ii1I % OOooOOo
 if 85 - 85: IIiIiII11i . I1ii11iIi11i / IIiIiII11i
 if 2 - 2: ooOoO0O00 . o0ii1I
 if 38 - 38: I11i / Ii1I * i1i1I1IIii1II + IIiIiII11i / Ii
 if 34 - 34: Ii % oO0o - i1i1I1IIii1II / oooOo0oo0oo / IiI1i11I
 if 5 - 5: i1IiiiI1iI . i1i1I1IIii1II
 if 77 - 77: IiI1i11I / Ii
def iiI11ii1I1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI1IIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( iI1IIi1I ) :
   iII1Ii1ii111 = 0
   iII1Ii1ii111 += len ( i1I1ii1i )
   if 20 - 20: o0o00Oo0O . Iii
   if 67 - 67: OOooOOo - i1iIi - iI11I1II1I1I
   if iII1Ii1ii111 > 0 :
    if 31 - 31: IIiIiII11i + I11i * Ii . I11i
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( iII1Ii1ii111 ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: i1i1I1IIii1II / oooOo0oo0oo * IIiIiII11i % ii - ooOoO0O00 - i1iIi
     for oooO in i1I1ii1i :
      os . unlink ( os . path . join ( ii1Io0oOO0 , oooO ) )
     for OO00 in iII1i1ii :
      shutil . rmtree ( os . path . join ( ii1Io0oOO0 , OO00 ) )
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
 i1I1I1iIIi ( url )
 return
 if 43 - 43: I11i + o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
 if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
 if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
 if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
 if 63 - 63: Ii1I % i1iIi % Ii1I
 if 71 - 71: o0ii1I
 if 43 - 43: I11i / i1iIi
def OoOoOOoOo ( url , name ) :
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 i1i11IIIi = os . path . join ( ii1I1 , 'advancedsettings.xml.bak' )
 if os . path . exists ( i1i11IIIi ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'advancedsettings.xml' )
   try :
    os . remove ( o0Oo0ooOOO000 )
    print '=== GenieTv - REMOVING    ' + str ( o0Oo0ooOOO000 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   Oo0oOOOOo = open ( o0Oo0ooOOO000 , "w" )
   Oo0oOOOOo . write ( iiI111I1iIiI )
   Oo0oOOOOo . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0ooOOO000 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'advancedsettings.xml' )
  try :
   os . remove ( o0Oo0ooOOO000 )
   print '=== GenieTv - REMOVING    ' + str ( o0Oo0ooOOO000 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  Oo0oOOOOo = open ( o0Oo0ooOOO000 , "w" )
  Oo0oOOOOo . write ( iiI111I1iIiI )
  Oo0oOOOOo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0ooOOO000 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 88 - 88: Ii1I . I11i % oooOo0oo0oo + o0ii1I
def oOO0O00ooOo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 try :
  Oo0oOOOOo = open ( o0Oo0ooOOO000 ) . read ( )
  if 'zero' in Oo0oOOOOo :
   name = '0CACHE'
  elif 'tuxen' in Oo0oOOOOo :
   name = 'TUXENS'
  elif 'muckys' in Oo0oOOOOo :
   name = 'MUCKYS'
  elif 'p2p1' in Oo0oOOOOo :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Oo0oOOOOo :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Oo0oOOOOo :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 49 - 49: Ii1I
def Ii1IOOo0oOOO0 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'advancedsettings.xml' )
 try :
  os . remove ( o0Oo0ooOOO000 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0Oo0ooOOO000 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 79 - 79: ii * oO0o + oO0o % o0ii1I % oooOo0oo0oo * III1iiIii
 if 11 - 11: oooOo0oo0oo - o0ii1I
 if 44 - 44: i1i1I1IIii1II + i1i1I1IIii1II - Iii % Iii - Ii / I1ii11iIi11i
 if 51 - 51: oOo0O0Ooo * oOo0O0Ooo
 if 49 - 49: i1IiiiI1iI
 if 11 - 11: ooOoO0O00
 if 65 - 65: oO0o . i1iIi
 if 12 - 12: i1IiiiI1iI + o0o00Oo0O - i1i1I1IIii1II . III1iiIii
 if 46 - 46: III1iiIii . i1iIi / IiI1i11I
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
def O0OoOO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for Oooo00OOo , OO000oooooO , O0O0o0 , OO00iiI1II1i in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Oooo00OOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0O0o0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OO00iiI1II1i )
  inc = inc + 1
  if 18 - 18: III1iiIii
  if 74 - 74: oOo0O0Ooo
  if 74 - 74: o0ii1I - OOooOOo . IIiIiII11i / I1ii11iIi11i
  if 48 - 48: iI11I1II1I1I / Iii
  if 58 - 58: i1IiiiI1iI - Iii + i1i1I1IIii1II * oO0o
  if 45 - 45: III1iiIii * oooOo0oo0oo . oO0o
  if 56 - 56: III1iiIii * o0ii1I . IIiIiII11i / OOooOOo
  if 70 - 70: Ii1I
  if 82 - 82: oO0o + Ii
def OoOO000oo0 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  Oo0oOOOOo = open ( o0Oo0ooOOO000 , "w" )
  Oo0oOOOOo . write ( iiI111I1iIiI )
  Oo0oOOOOo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0ooOOO000 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 64 - 64: Ii1I % I1ii11iIi11i - iI11I1II1I1I % oO0o * iI11I1II1I1I + Iii
def oo000o00o0o00 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  ii1I1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0Oo0ooOOO000 = os . path . join ( ii1I1 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  Oo0oOOOOo = open ( o0Oo0ooOOO000 , "w" )
  Oo0oOOOOo . write ( iiI111I1iIiI )
  Oo0oOOOOo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0Oo0ooOOO000 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 27 - 27: III1iiIii . oO0o / ooOoO0O00 + oO0o
 if 36 - 36: III1iiIii . oOo0O0Ooo - IIiIiII11i - IIiIiII11i + Ii
def iiiII1i11iII ( ) :
 try :
  i1I1IIII = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( i1I1IIII ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iI11iii111 = os . path . join ( i1I1IIII , "source.db" )
    os . unlink ( iI11iii111 )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 33 - 33: oOo0O0Ooo % Iii . i1IiiiI1iI / o0ii1I * IIiIiII11i * I11i
 if 49 - 49: ooOoO0O00 * Ii
 if 47 - 47: IIiIiII11i / I1ii11iIi11i
 if 38 - 38: oooOo0oo0oo . IiI1i11I / o0o00Oo0O . o0ii1I / OOooOOo
 if 52 - 52: o0o00Oo0O / Ii * oOo0O0Ooo . ooOoO0O00
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 50 - 50: ii . IiI1i11I % I11i
 if 6 - 6: i1iIi - ooOoO0O00 . o0o00Oo0O . ooOoO0O00 . OOooOOo
 if 42 - 42: Ii * o0o00Oo0O % Ii + oooOo0oo0oo
 if 64 - 64: oOo0O0Ooo / OOooOOo
 if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
 if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
 if 91 - 91: oOo0O0Ooo
def o0OoOO ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; oo0oOooo0O = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oo0oOooo0O :
  I1i1ii = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; I1i1ii = xbmc . translatePath ( I1i1ii ) ;
  ii1iIiIIiIIii = os . path . join ( I1i1ii , ".." , ".." ) ; ii1iIiIIiIIii = os . path . abspath ( ii1iIiIIiIIii ) ; pluginlog ( "freshstart.main_list xbmcPath=" + ii1iIiIIiIIii ) ; ooooo = False
  try :
   for ii1Io0oOO0 , iII1i1ii , i1I1ii1i in os . walk ( ii1iIiIIiIIii , topdown = True ) :
    iII1i1ii [ : ] = [ OO00 for OO00 in iII1i1ii if OO00 not in o0oO0 ]
    for OO0O000 in i1I1ii1i :
     try : os . remove ( os . path . join ( ii1Io0oOO0 , OO0O000 ) )
     except :
      if OO0O000 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : ooooo = True
      pluginlog ( "Error removing " + ii1Io0oOO0 + " " + OO0O000 )
    for OO0O000 in iII1i1ii :
     try : os . rmdir ( os . path . join ( ii1Io0oOO0 , OO0O000 ) )
     except :
      if OO0O000 not in [ "Database" , "userdata" ] : ooooo = True
      pluginlog ( "Error removing " + ii1Io0oOO0 + " " + OO0O000 )
   if not ooooo : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 OOOo0Oo0O ( )
 if 19 - 19: o0ii1I * Iii . IIiIiII11i
 if 84 - 84: iI11I1II1I1I / I11i / IIiIiII11i
 if 81 - 81: Ii + I11i / IIiIiII11i + Iii
def OOO0O0 ( ) :
 IIiIiI1I = [ ]
 iIi1i1Ii11III = sys . argv [ 2 ]
 if len ( iIi1i1Ii11III ) >= 2 :
  O0O0Oo00 = sys . argv [ 2 ]
  iIi11i1111I = O0O0Oo00 . replace ( '?' , '' )
  if ( O0O0Oo00 [ len ( O0O0Oo00 ) - 1 ] == '/' ) :
   O0O0Oo00 = O0O0Oo00 [ 0 : len ( O0O0Oo00 ) - 2 ]
  OO00O0 = iIi11i1111I . split ( '&' )
  IIiIiI1I = { }
  for iIi1Iii1 in range ( len ( OO00O0 ) ) :
   O0oo00O0ooOo = { }
   O0oo00O0ooOo = OO00O0 [ iIi1Iii1 ] . split ( '=' )
   if ( len ( O0oo00O0ooOo ) ) == 2 :
    IIiIiI1I [ O0oo00O0ooOo [ 0 ] ] = O0oo00O0ooOo [ 1 ]
    if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
 return IIiIiI1I
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
iI111ii11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OOoOOoOO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o0I1iI111ii111i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oOoOoo0OOOo0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
o0o00O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iIII1Ii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oOO0OOoo0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o0Oo00OoO000O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1iO00oo0oOo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1iiIIiIi1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OO0oO0ooOOOoO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
I1IO0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIi1I1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iI1iIIiIi1I1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiI1ooOOOoo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
I1Ii1i1iII = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OO00OoOO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
II1iii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oOO0Oo = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iIiI1111 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OoOiII11IiIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IIii1Ii1i1ii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiiIi1II = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oo0 = base64 . decodestring ( 'Q1VOVA==' )
def OoO0oO0oo0O ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 iiIIIiIii . setProperty ( 'fanart_image' , fanart )
 iiIIIiIii . setProperty ( "IsPlayable" , "true" )
 O0oOOOO0o = [ ]
 O0oOOOO0o . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 O0oOOOO0o . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 iiIIIiIii . addContextMenuItems ( O0oOOOO0o , replaceItems = True )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
def ii1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 65 - 65: IIiIiII11i + i1i1I1IIii1II + oooOo0oo0oo + III1iiIii + ooOoO0O00
def i11I1II1I11i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 33 - 33: i1iIi . oOo0O0Ooo . Ii % oO0o
 if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
O0O0Oo00 = OOO0O0 ( )
OoO = None
OO0O000 = None
o000O000 = None
iiiI1I1iIIIi1 = None
iI = None
O0o = None
IIi1IiiI1i1 = None
OoooOoo = None
if 29 - 29: oooOo0oo0oo - Ii % III1iiIii / ii
if 92 - 92: Ii1I
try :
 OoooOoo = int ( O0O0Oo00 [ "fav_mode" ] )
except :
 pass
 if 89 - 89: oO0o * Ii - III1iiIii * ooOoO0O00 - i1iIi . o0ii1I
try :
 OoO = urllib . unquote_plus ( O0O0Oo00 [ "url" ] )
except :
 pass
try :
 OO0O000 = urllib . unquote_plus ( O0O0Oo00 [ "name" ] )
except :
 pass
try :
 iiiI1I1iIIIi1 = urllib . unquote_plus ( O0O0Oo00 [ "iconimage" ] )
except :
 pass
try :
 o000O000 = int ( O0O0Oo00 [ "mode" ] )
except :
 pass
try :
 iI = urllib . unquote_plus ( O0O0Oo00 [ "fanart" ] )
except :
 pass
try :
 O0o = urllib . unquote_plus ( O0O0Oo00 [ "description" ] )
except :
 pass
 if 26 - 26: oOo0O0Ooo * ii / oOo0O0Ooo . o0o00Oo0O . i1iIi + o0o00Oo0O
 if 84 - 84: i1IiiiI1iI . o0o00Oo0O + o0o00Oo0O % o0o00Oo0O % ooOoO0O00 + iI11I1II1I1I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( o000O000 )
print "URL: " + str ( OoO )
print "Name: " + str ( OO0O000 )
print "IconImage: " + str ( iiiI1I1iIIIi1 )
if 71 - 71: IiI1i11I / iI11I1II1I1I . oooOo0oo0oo * Ii
if 98 - 98: o0o00Oo0O % iI11I1II1I1I . III1iiIii - IIiIiII11i
def iI1i11iII111 ( content , viewType ) :
 if 14 - 14: o0ii1I % i1iIi - OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 52 - 52: oO0o / ooOoO0O00 - o0ii1I
if iiiI1I1iIIIi1 == None : iiiI1I1iIIIi1 = O0O
if iI == None : iI = Oo00OOOOO
if o000O000 == None :
 Iii1I1I11iiI1 ( )
 if 8 - 8: i1i1I1IIii1II + i1iIi . Ii1I . ooOoO0O00 / oOo0O0Ooo . III1iiIii
elif o000O000 == 1 :
 iIiiIiIIiI ( OoO )
 if 8 - 8: ooOoO0O00 * o0o00Oo0O
elif o000O000 == 44 :
 oOoO00o ( OoO )
 if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
elif o000O000 == 2 :
 oO0OOO ( )
 if 17 - 17: OOooOOo % oOo0O0Ooo
elif o000O000 == 3 :
 i111I1 ( )
 if 8 - 8: I1ii11iIi11i
elif o000O000 == 21 :
 i1i1II ( )
 if 49 - 49: OOooOOo * Iii - I11i / oO0o * i1i1I1IIii1II
elif o000O000 == 4 :
 OOO0IIIIii11II1I ( )
 if 51 - 51: i1iIi - iI11I1II1I1I . Iii * OOooOOo + i1IiiiI1iI * ooOoO0O00
elif o000O000 == 5 :
 iiIIiiiIi1 ( OoO )
 if 37 - 37: III1iiIii * i1i1I1IIii1II / ii . oO0o
elif o000O000 == 6 :
 IiOo00O0o0O ( OoO )
 if 77 - 77: IIiIiII11i + OOooOOo * oooOo0oo0oo
elif o000O000 == 7 :
 OoOoOOoOo ( OoO , OO0O000 )
 if 9 - 9: IIiIiII11i - Ii * I11i % oO0o * Ii / Iii
elif o000O000 == 8 :
 oOO0O00ooOo ( OoO , OO0O000 )
 if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
elif o000O000 == 9 :
 FIXREPOSADDONS ( OoO )
 if 11 - 11: iI11I1II1I1I
elif o000O000 == 10 :
 Ooo0OOoOoO0 ( )
 if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
elif o000O000 == 11 :
 Ii1IOOo0oOOO0 ( OoO )
 if 80 - 80: ooOoO0O00
elif o000O000 == 12 :
 O0OoOO ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 56 - 56: IIiIiII11i - I11i
elif o000O000 == 13 :
 o0o0oO0OOO ( )
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
elif o000O000 == 14 :
 i1I1I1iIIi ( OoO )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
elif o000O000 == 15 :
 ooOi1i1i11iI11II ( )
 if 93 - 93: i1i1I1IIii1II
elif o000O000 == 16 :
 OoOO000oo0 ( OoO , OO0O000 )
 if 60 - 60: i1IiiiI1iI . i1i1I1IIii1II / I1ii11iIi11i * i1iIi + OOooOOo - ooOoO0O00
elif o000O000 == 17 :
 oo000o00o0o00 ( OoO , OO0O000 )
 if 13 - 13: Ii * i1i1I1IIii1II / Iii * oOo0O0Ooo
elif o000O000 == 18 :
 iiiII1i11iII ( )
 if 31 - 31: iI11I1II1I1I * o0ii1I % oooOo0oo0oo . IIiIiII11i
elif o000O000 == 19 :
 iI1I1ii11IIi1 ( OoO )
 if 56 - 56: III1iiIii / Ii . I11i . i1i1I1IIii1II - Ii
elif o000O000 == 40 :
 IIIiiiiI1 ( OO0O000 , OoO , O0o )
 if 23 - 23: Ii1I * Ii % i1iIi
elif o000O000 == 42 :
 OO00o0O0oOooO ( OO0O000 , OoO , O0o )
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
elif o000O000 == 43 :
 I1111111 ( OoO )
 if 92 - 92: Ii1I % Ii
elif o000O000 == 20 :
 Ooo0o ( OoO )
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
elif o000O000 == 22 :
 OOO0O0oO ( OoO )
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
elif o000O000 == 23 :
 oOOo0Oo0OO0O ( OoO )
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
elif o000O000 == 24 :
 iII ( OoO )
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
elif o000O000 == 25 :
 II1II111iIi ( OoO )
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
elif o000O000 == 26 :
 iiOOo ( OoO )
 if 48 - 48: i1i1I1IIii1II - IIiIiII11i * oOo0O0Ooo
elif o000O000 == 27 :
 o0OOOOooOo ( OoO )
 if 78 - 78: oOo0O0Ooo * Ii * IIiIiII11i
elif o000O000 == 28 :
 oOOOo000 ( OoO )
 if 19 - 19: ii * Ii / o0o00Oo0O . oOo0O0Ooo % Iii
elif o000O000 == 29 :
 o0oo0oO ( OoO )
 if 35 - 35: iI11I1II1I1I + oOo0O0Ooo - i1iIi / I1ii11iIi11i * Ii1I * I1ii11iIi11i
elif o000O000 == 30 :
 I1ii1i ( OoO )
 if 17 - 17: OOooOOo
elif o000O000 == 31 :
 i111I ( OoO )
 if 24 - 24: iI11I1II1I1I / oooOo0oo0oo % ii / o0o00Oo0O / i1i1I1IIii1II
elif o000O000 == 32 :
 iIo00oo ( )
 if 93 - 93: I1ii11iIi11i
elif o000O000 == 33 :
 O000Oo00 ( )
 if 5 - 5: IiI1i11I
elif o000O000 == 35 :
 o00O0o00oo ( OoO )
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
elif o000O000 == 34 :
 iI1oOoo ( OoO )
 if 30 - 30: iI11I1II1I1I
elif o000O000 == 36 :
 I1IiiiI ( OoO )
 if 14 - 14: I11i + o0ii1I
elif o000O000 == 37 :
 O0OOOOoO00oo ( OoO )
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
elif o000O000 == 38 :
 ooo0oOooo0o0 ( OoO )
 if 100 - 100: ooOoO0O00
elif o000O000 == 41 :
 o0OoOO ( O0O0Oo00 )
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
elif o000O000 == 39 :
 oooooo0O000o ( OoO )
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
elif o000O000 == 45 :
 TEXTS ( )
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
elif o000O000 == 46 :
 ooO0O0O0ooOOO ( )
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
elif o000O000 == 47 :
 GEVID ( )
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
elif o000O000 == 48 :
 Ii1i ( OO0O000 , OoO , O0o )
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
elif o000O000 == 49 :
 I1ii1ii11i1I ( )
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
elif o000O000 == 22222 :
 OOo00ooOoO0o ( OoO )
 if 12 - 12: ii % i1i1I1IIii1II
elif o000O000 == 222225 :
 OO0O0o0o0 ( OoO )
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
elif o000O000 == 222 :
 OO0o0ooo00 ( OoO )
 if 79 - 79: o0o00Oo0O
elif o000O000 == 2222222 :
 OooO0OO ( OoO )
 if 71 - 71: oO0o - o0o00Oo0O
elif o000O000 == 222222 :
 I11II1iI ( OoO , OO0O000 )
 if 73 - 73: iI11I1II1I1I
elif o000O000 == 333 :
 oOo000oOo ( OoO )
 if 7 - 7: OOooOOo
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
elif o000O000 == 1020 :
 iIII1 ( )
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
elif o000O000 == 1021 :
 ANIMEEP ( )
 if 3 - 3: Iii
elif o000O000 == 1022 :
 ANIMEPLAY ( OoO )
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
elif o000O000 == 1001 :
 i11IIi ( )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
elif o000O000 == 1005 :
 Oooo0o00Oo00 ( )
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
elif o000O000 == 1007 :
 OoooOoo0Oooo ( OoO )
 if 53 - 53: o0o00Oo0O
elif o000O000 == 1010 :
 OoOoOoOOo00Ooo0O ( OoO )
 if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
elif o000O000 == 1011 :
 Ii1ii1i1 ( OoO )
 if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
elif o000O000 == 1012 :
 II1II1iiIiI ( OoO )
 if 27 - 27: oO0o / IiI1i11I . Ii1I
elif o000O000 == 1030 :
 oo0oO ( )
 if 71 - 71: oO0o . Ii . iI11I1II1I1I + oOo0O0Ooo - I11i
elif o000O000 == 1031 :
 iII1IiI1I11i ( OoO , iiiI1I1iIIIi1 )
 if 34 - 34: IiI1i11I
elif o000O000 == 1032 :
 oOOoO0O ( OoO )
 if 6 - 6: oO0o . OOooOOo + Ii1I
elif o000O000 == 1006 :
 Parse . ParseURL ( OoO )
 if 24 - 24: oO0o . o0ii1I
elif o000O000 == 2030 :
 Parse . addonParseURL ( OoO )
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
elif o000O000 == 2031 :
 Parse . apkParseURL ( OoO )
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
elif o000O000 == 2032 :
 Parse . ParseBOSS ( OoO )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
elif o000O000 == 1002 :
 oOoOoOo0O0o ( OoO )
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
elif o000O000 == 1003 :
 IiIIIIII ( OoO , iiiI1I1iIIIi1 )
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
elif o000O000 == 1004 :
 OOO0O ( OoO )
 if 7 - 7: o0ii1I
elif o000O000 == 1008 :
 IiiiI1i1i ( )
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
elif o000O000 == 1009 :
 iIIioo0 ( OoO )
 if 55 - 55: oO0o % OOooOOo
elif o000O000 == 2001 :
 II1iIIII ( )
 if 58 - 58: o0ii1I
elif o000O000 == 2002 :
 iI11iI1ii111II ( OoO )
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
elif o000O000 == 1013 :
 OoOo ( )
elif o000O000 == 10111113 :
 IiiII1iiiiI1i ( OoO )
 if 88 - 88: i1iIi . IIiIiII11i * o0o00Oo0O % III1iiIii
elif o000O000 == 1014 :
 o000oOOO ( )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif o000O000 == 1015 :
 iIi1 ( OoO )
 if 1 - 1: oOo0O0Ooo
elif o000O000 == 1016 :
 I1IIIiI1I1ii1 ( OoO , iiiI1I1iIIIi1 , OO0O000 )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif o000O000 == 1017 :
 oOoO00 ( )
 if 88 - 88: I11i - i1i1I1IIii1II
elif o000O000 == 1018 :
 ii1iI ( OoO )
 if 73 - 73: IIiIiII11i
elif o000O000 == 1019 :
 IiI11i1IIiiI ( OoO )
elif o000O000 == 10190 :
 OoOo00o0OO ( OoO )
 if 7 - 7: o0o00Oo0O / oO0o
elif o000O000 == 1023 :
 Oo00oo ( )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif o000O000 == 1024 :
 IiIIIi1 ( OoO )
 if 52 - 52: oOo0O0Ooo / I11i
elif o000O000 == 1025 :
 i1I111Ii1I ( OoO )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif o000O000 == 4001 :
 OoOooOoO ( )
 if 46 - 46: i1IiiiI1iI . Ii
elif o000O000 == 4002 :
 oOOo0OOOo00O ( )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif o000O000 == 4003 :
 o00o0O0 ( )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif o000O000 == 4004 :
 IIIi ( )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif o000O000 == 4005 :
 IIi1ii1Ii ( )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif o000O000 == 4006 :
 oOO00O0Ooooo00 ( )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif o000O000 == 4007 :
 Oo0OO0000oooo ( )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif o000O000 == 4008 :
 ii1III11 ( )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif o000O000 == 40099 : oooOo ( )
elif o000O000 == 4009 : IIi1i1 ( )
elif o000O000 == 4010 : O00o ( )
elif o000O000 == 3000 :
 IiIIIiI11i1 ( )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif o000O000 == 3001 :
 oo00000ooOooO ( )
 if 65 - 65: I1ii11iIi11i . Iii
elif o000O000 == 3002 :
 oo0o0OO00oOO ( OoO )
 if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif o000O000 == 3003 :
 IiiII1iIi ( OoO )
 if 11 - 11: OOooOOo % ii
elif o000O000 == 3004 :
 iiiiii ( OoO )
 if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif o000O000 == 404 :
 i11iI ( OO0O000 , OoO , iiiI1I1iIIIi1 )
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif o000O000 == 405 :
 I1iO0000 ( OoO )
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif o000O000 == 7030 :
 O0O0o00o00O00 ( )
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif o000O000 == 7021 :
 oO000oOo0oO0 ( OO0O000 )
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif o000O000 == 7022 :
 I1iOoO00O ( OO0O000 )
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif o000O000 == 7000 :
 IIIi1IIiI ( OO0O000 , OoO , img )
 if 29 - 29: oooOo0oo0oo
elif o000O000 == 7050 :
 III1IiIi1 ( OoO )
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
elif o000O000 == 7051 :
 Ii1iiIi1iiI ( OoO )
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
elif o000O000 == 7052 :
 i1IOOoOO00O ( OoO )
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
elif o000O000 == 7053 :
 II1iIiiiIiiII ( OoO )
 if 91 - 91: Ii . Ii1I + Iii
elif o000O000 == 7054 :
 CoolPlay ( OoO )
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
elif o000O000 == 7060 :
 OOooooo00OO ( )
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
elif o000O000 == 7061 :
 IIiiI ( OoO )
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
elif o000O000 == 7063 :
 O0O0oOO ( OoO )
 if 52 - 52: IIiIiII11i - III1iiIii
elif o000O000 == 7062 :
 IiIi11iI1IIi ( OoO )
 if 91 - 91: iI11I1II1I1I + IiI1i11I . Iii % Ii - Ii + oOo0O0Ooo
elif o000O000 == 7064 :
 NATatozcat ( )
 if 75 - 75: Ii1I / oOo0O0Ooo - iI11I1II1I1I / oO0o * oooOo0oo0oo
elif o000O000 == 7067 :
 iII111I ( OoO )
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
elif o000O000 == 7066 :
 NATatozA ( OoO )
 if 91 - 91: Ii
elif o000O000 == 7065 :
 Ooooo0Oo0oOo ( OoO )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
elif o000O000 == 7070 :
 o0o000OOO ( )
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
elif o000O000 == 7071 :
 DIZIlist ( OoO )
 if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
elif o000O000 == 7072 :
 DIZIpull ( OoO )
 if 82 - 82: iI11I1II1I1I
elif o000O000 == 7073 :
 WATCHDIZI ( OoO )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif o000O000 == 7002 :
 OoOoo0ooO0000 ( )
 if 46 - 46: oOo0O0Ooo
elif o000O000 == 7003 :
 ooO00OoO ( OoO )
 if 72 - 72: IiI1i11I
elif o000O000 == 7004 :
 i1ii1iIiI1 ( OoO )
 if 100 - 100: oOo0O0Ooo
elif o000O000 == 7020 :
 oOo0oOo ( OoO )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif o000O000 == 7001 :
 Ii1I11ii1i ( )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
elif o000O000 == 7010 :
 i1I11Iiii ( OoO )
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif o000O000 == 7011 :
 IiIII ( OoO )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif o000O000 == 7012 :
 ooo00o0OO0 ( OoO )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif o000O000 == 7013 :
 cnfTVPlay2 ( OoO )
elif o000O000 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( OoO )
elif o000O000 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( OoO )
elif o000O000 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OO0O000 , OoO , iiiI1I1iIIIi1 )
elif o000O000 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif o000O000 == 7018 :
 oo0O0o0O ( )
elif o000O000 == 7019 :
 CNF_Studio_Indexer . List_Movies ( OoO )
elif o000O000 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( OoO )
elif o000O000 == 7024 :
 CNF_Studio_Indexer . Box_Office ( OoO )
 if 93 - 93: oO0o . oO0o
elif o000O000 == 8000 :
 O0o0OOOooo0 ( )
elif o000O000 == 8001 :
 o0o00O0oO ( )
elif o000O000 == 8002 :
 i1iIi1IiI ( )
elif o000O000 == 8003 :
 IIi1ii1i1i1 ( )
elif o000O000 == 8004 :
 O0oOOoO ( )
elif o000O000 == 8005 :
 iiIIi1Ii1 ( )
elif o000O000 == 8006 :
 OOOO0oO0OOo0o ( OO0O000 , OoO )
elif o000O000 == 8030 :
 oO0OO ( OoO )
elif o000O000 == 8045 :
 IIIIi11111 ( OoO )
elif o000O000 == 8046 :
 Oo0o00o0oOoo0 ( OoO )
elif o000O000 == 8047 :
 iI11 ( OoO )
elif o000O000 == 8048 :
 i11i1 ( OoO )
elif o000O000 == 8049 :
 O0O0I1II ( OoO )
elif o000O000 == 804900 :
 o0o0OoOO00Oo ( OoO )
elif o000O000 == 8020 :
 iII1111III1I ( )
elif o000O000 == 8021 :
 Oo0oOo0Ooo ( OoO )
elif o000O000 == 8022 :
 iiI1 ( OoO )
elif o000O000 == 8023 :
 IiI1o0o0ooo ( OoO )
elif o000O000 == 8040 :
 I1iiIIIi11 ( )
elif o000O000 == 8041 :
 OO0oO ( OoO )
elif o000O000 == 8042 :
 i1iI1I1I ( OoO )
elif o000O000 == 8043 :
 yt . PlayVideo ( OoO )
elif o000O000 == 8044 :
 i1I11i1iii1 ( OoO )
elif o000O000 == 8060 :
 I1iIiIi11i11 ( )
elif o000O000 == 8061 :
 IiII11I1I1IIi ( OoO )
elif o000O000 == 8064 :
 O00oOo00o0o ( )
elif o000O000 == 8065 :
 I111 ( OoO )
elif o000O000 == 8070 :
 OOoOooO0o ( )
elif o000O000 == 8071 :
 OOoOI1i1i1Iii1 ( OoO )
elif o000O000 == 7080 :
 OoO00Ooooo ( OoO )
elif o000O000 == 8090 :
 I1iI1I ( )
elif o000O000 == 8091 :
 O0O0OOo00Oo ( OoO )
elif o000O000 == 8092 :
 IIiIi ( OoO )
elif o000O000 == 8093 :
 IiI1iIIiIi1Ii ( OoO )
elif o000O000 == 8081 :
 OoOoooO0o0O00o0O ( )
elif o000O000 == 8062 :
 OOoOi11i ( OoO )
elif o000O000 == 8063 :
 ooO0oO00oO0o ( OoO )
elif o000O000 == 8050 :
 OOOoOo0O0O ( )
elif o000O000 == 8051 :
 o0Oo0oO00Oooo ( OoO )
elif o000O000 == 8052 :
 Ii1II1I11i1I ( OoO )
elif o000O000 == 8085 :
 iI11I1IiI1 ( )
elif o000O000 == 8086 :
 oOo0oOoo0 ( OoO )
elif o000O000 == 8087 :
 oooOOO0 ( OoO )
elif o000O000 == 8088 :
 OO00o0 ( OoO , OO0O000 )
elif o000O000 == 9000 :
 IiIii11I ( )
elif o000O000 == 1111 :
 iIii1Oo ( )
elif o000O000 == 9001 :
 O00OoO0o ( )
elif o000O000 == 9002 :
 OoOoO ( )
elif o000O000 == 9003 :
 I111I1 ( )
elif o000O000 == 9004 :
 World1 ( )
elif o000O000 == 9005 :
 World2 ( OoO )
elif o000O000 == 9006 :
 World3 ( OoO )
elif o000O000 == 9007 :
 II1i1 ( )
elif o000O000 == 9008 :
 ooO0OoOO0 ( OoO )
elif o000O000 == 9009 :
 o0oo00 ( OoO )
elif o000O000 == 9010 :
 OOO0OOo0OoO ( )
elif o000O000 == 9011 :
 oO00OOO ( OoO )
elif o000O000 == 50 :
 IiIii11ii111 ( OoO )
elif o000O000 == 9020 :
 champlist ( )
elif o000O000 == 9021 :
 ooo0o ( )
elif o000O000 == 9022 :
 o0OOO0O00Oo00 ( )
elif o000O000 == 9023 :
 ooooO0O ( )
elif o000O000 == 9024 :
 iII1iOO00o0O0OO0o0 ( OoO )
elif o000O000 == 9030 :
 IiIi1III ( OoO )
elif o000O000 == 9031 :
 ii1I1IIi ( OoO )
elif o000O000 == 9032 :
 o00oOO0OOo ( OoO )
elif o000O000 == 9033 :
 OooOooO0OoOoo0o ( OoO )
elif o000O000 == 9034 :
 oo000ii ( )
elif o000O000 == 7085 :
 IIiI1iIiii ( OoO )
elif o000O000 == 7086 :
 ii11iIII111 ( OoO )
elif o000O000 == 7087 :
 OoOoO0o0oO0 ( O0o )
elif o000O000 == 9666 :
 iiI11ii1I1 ( OoO )
elif o000O000 == 10100 : Ii1I11Ii1iI ( )
elif o000O000 == 101001 : OOOoO0o ( OoO )
elif o000O000 == 10105 : iii111iiI11I ( OoO )
elif o000O000 == 10106 : iII1i ( OoO )
elif o000O000 == 10104 : o00Oooo0o0 ( OoO )
elif o000O000 == 10107 : iiioO000oO0oO ( )
elif o000O000 == 10103 : oOii1iiiiii ( OoO )
elif o000O000 == 10108 : ii11 ( OoO )
elif o000O000 == 10000 : Origin_Menu ( )
elif o000O000 == 10001 : IIiiIIi1 ( )
elif o000O000 == 10002 : Ooo00OoOOO ( )
elif o000O000 == 10003 : oO0o00o000Oo0 ( )
elif o000O000 == 10004 : oOIII111iiIi1 ( OoO )
elif o000O000 == 10005 : O0O0 ( )
elif o000O000 == 10006 : iiiiI1iiiIi11 ( OoO )
elif o000O000 == 10007 : Iii11I1i ( OoO , iiiI1I1iIIIi1 )
elif o000O000 == 10008 : oO00O ( )
elif o000O000 == 10009 : OoOOoo0o00O0oO ( )
elif o000O000 == 10010 : i1IiI1i ( OoO )
elif o000O000 == 10011 : O0000oOo0OO ( OoO )
elif o000O000 == 10012 : OooO0OO ( OoO )
elif o000O000 == 10113 : GRABG ( OoO , OO0O000 )
elif o000O000 == 10109 : O0oOo00O0Oo ( OoO )
elif o000O000 == 10013 : O000o ( OoO )
elif o000O000 == 10014 : iIi11I1II ( )
elif o000O000 == 10015 : IIii1Ii ( )
elif o000O000 == 10016 : iIIiI1I1i ( OoO )
elif o000O000 == 10017 : I1I11 ( )
elif o000O000 == 10018 : OOOo0ooOO ( )
elif o000O000 == 10019 : Ii11II1IIIIIi ( )
elif o000O000 == 10020 : o0OoOoOo0O ( )
elif o000O000 == 10021 : i11IiIiii ( )
elif o000O000 == 10022 : O0oo00o000 ( OoO )
elif o000O000 == 10023 : OOOoO000 ( OO0O000 , OoO )
elif o000O000 == 10024 : IIIii111i ( OoO )
elif o000O000 == 10025 : I1Iiiiiii ( )
elif o000O000 == 10026 : OOo0Oo0O00O ( )
elif o000O000 == 10027 : I1i ( )
elif o000O000 == 10028 : II1IiI1iI ( )
elif o000O000 == 10029 : ooooOOo ( )
elif o000O000 == 423 : ooOoo000 ( OoO )
elif o000O000 == 426 : Oooo0o00 ( OoO )
elif o000O000 == 10030 : Izle_Films ( )
elif o000O000 == 10031 : Latest_Izle_Movies ( )
elif o000O000 == 10032 : Izle_Genres ( )
elif o000O000 == 10033 : Izle_Pop_Movies ( )
elif o000O000 == 10034 : Izle_Boxsets ( )
elif o000O000 == 10035 : Izle_Search ( )
elif o000O000 == 10036 : Izle_Genres_Movie ( OoO )
elif o000O000 == 10037 : Izle_Boxset_single ( OoO )
elif o000O000 == 10038 : Izle_IFRAME ( )
elif o000O000 == 10039 : Izle_Boxsets_Next ( OoO )
elif o000O000 == 10040 : oOOoo ( )
elif o000O000 == 10041 : iIIIIIIIIIi1i1i1iii ( OoO )
elif o000O000 == 10042 : OOOOO0oOOoO ( OoO )
elif o000O000 == 10043 : ooo00OoOooooo ( )
elif o000O000 == 10044 : oooOoOO0o ( OoO )
elif o000O000 == 10045 : IIIiiII1iIi1ii1i ( OO0O000 )
elif o000O000 == 10046 : o00OooooOOOO ( OoO )
elif o000O000 == 10047 : iIi1i1I1I ( OoO )
elif o000O000 == 10048 : iIi1II111I1i1 ( OoO )
elif o000O000 == 10049 : IiiI ( OoO )
elif o000O000 == 10050 : O0O00Oo ( )
elif o000O000 == 10051 : iiIiiIii1IiI ( )
elif o000O000 == 10052 : Ooooo00 ( )
elif o000O000 == 10053 : Addon ( OoO )
elif o000O000 == 10054 : Iii11I ( OoO , OO0O000 )
elif o000O000 == 10055 :
 I1Ii111I111 ( "addFavorite" )
 try :
  OO0O000 = OO0O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0O000 = OO0O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 i111i11iI1i1I ( OO0O000 , OoO , iiiI1I1iIIIi1 , iI , OoooOoo )
elif o000O000 == 10056 :
 I1Ii111I111 ( "rmFavorite" )
 try :
  OO0O000 = OO0O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0O000 = OO0O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 ooOOO000O ( OO0O000 )
elif o000O000 == 10057 :
 I1Ii111I111 ( "getFavorites" )
 Ooo00OoO0O00 ( )
elif o000O000 == 10058 : iI1iIIIIIiIi1 ( )
elif o000O000 == 10059 : Donators_Guide ( )
elif o000O000 == 10060 : iiIiii1iI1i ( )
elif o000O000 == 10061 : o00oOOo ( )
elif o000O000 == 10062 : i11iIiiIi11I ( OO0O000 , OoO , O0o )
elif o000O000 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif o000O000 == 10064 : I1oOoO0OOO00O ( )
elif o000O000 == 10065 : ii11I1IIi1i ( OoO )
elif o000O000 == 10066 : o0oo0o00ooO00 ( OoO )
elif o000O000 == 10068 : iiI111 ( OoO )
elif o000O000 == 10069 : O00oO0 ( OoO )
elif o000O000 == 10070 : iI111II1ii ( OoO )
elif o000O000 == 10071 : Genie_Watch ( )
elif o000O000 == 10072 : o00oo0OO0 ( )
elif o000O000 == 10073 : oo0o0OoOO0o0 ( OoO )
elif o000O000 == 10074 : iiii1IIi1 ( OoO )
elif o000O000 == 10075 : iiiIiIIII1iiIIi ( iiiI1I1iIIIi1 , OO0O000 , OoO )
elif o000O000 == 10076 : iII1Iii11111 ( OoO )
elif o000O000 == 10077 : Ooooo ( OoO )
elif o000O000 == 10078 : O000O ( )
elif o000O000 == 10079 : Genie_Watch_Tv_Shows ( )
elif o000O000 == 10080 : Genie_Watch_Tv_Genre ( OoO )
elif o000O000 == 10081 : Genie_Watch_TV_PlayRun ( OoO )
elif o000O000 == 10082 : Genie_Watch_TV_Episodes ( OoO , iiiI1I1iIIIi1 )
elif o000O000 == 10083 : Genie_Watch_Tv_Recent ( OoO )
elif o000O000 == 10084 : Ii1ii111i1 ( )
elif o000O000 == 10085 : oo0OOo0 ( )
elif o000O000 == 10086 : O0 ( )
elif o000O000 == 20000 : ooO000O ( )
elif o000O000 == 20001 : iIiI1I ( OoO )
elif o000O000 == 20002 : OO00O00o0O ( OoO )
elif o000O000 == 20003 : I1IiIi1iiI ( OoO )
elif o000O000 == 20004 : OO00o0oo ( OoO )
elif o000O000 == 20005 : ii1iIi1 ( OoO )
elif o000O000 == 21004 : oo0OOOoOo ( )
elif o000O000 == 21005 : oOO0O0O ( OoO )
elif o000O000 == 21006 : Oo0o0oOo0oO ( OoO )
elif o000O000 == 21007 : iii1i1Iiiiiii ( OoO )
elif o000O000 == 21008 : IiiiIIiIi1 ( OoO )
elif o000O000 == 21009 : o0o0O0O00oOOo ( OoO )
elif o000O000 == 30000 : Ii11ii1 ( )
elif o000O000 == 30001 : iIIi1II1 ( )
elif o000O000 == 100121 : Resolve ( OoO )
elif o000O000 == 30003 : IiIIii1 ( )
elif o000O000 == 30004 : o0o0OOo0OOoO ( OoO )
elif o000O000 == 30005 : ooOIIIi11i ( OoO )
elif o000O000 == 30006 : iI11ii ( )
elif o000O000 == 30007 : iiI11 ( )
elif o000O000 == 30008 : IiI111I ( OoO )
elif o000O000 == 30009 : III11iI1i11i ( OoO )
elif o000O000 == 30010 : O0oOo0o0OOoO0 ( OoO )
elif o000O000 == 30011 : o0oOOO ( )
elif o000O000 == 30012 : iIii1iIiII1i1 ( )
elif o000O000 == 30013 : Oo00 ( )
elif o000O000 == 30014 : oOooo00OOO000 ( )
elif o000O000 == 30015 : oOo000Oo00o ( OoO , iiiI1I1iIIIi1 , iI )
elif o000O000 == 30016 : ooOOOoOoOOOO ( OoO )
elif o000O000 == 30019 : i11iI11 ( OoO )
elif o000O000 == 30017 : iiI11111II ( OoO )
elif o000O000 == 30018 : IiOOo0 ( OoO )
elif o000O000 == 30030 : oOooo0OO0O0 ( )
elif o000O000 == 30031 : oOo0Ooo0 ( )
elif o000O000 == 30032 : IIII1iII ( )
elif o000O000 == 30033 : o0o0o0O0oo ( )
elif o000O000 == 30034 : i1iI1iIII ( )
elif o000O000 == 30035 : OOOOOO ( OoO )
elif o000O000 == 30036 : oOO0O ( OoO )
elif o000O000 == 30037 : oooo0 ( OoO )
elif o000O000 == 30038 : IiI1IIiiiii ( )
elif o000O000 == 30039 : oOOoo00O00o ( )
elif o000O000 == 50000 : oOo0OOoO0 ( )
elif o000O000 == 50001 : OOOo0 ( )
elif o000O000 == 50002 : III1i1iI111I1 ( OoO )
elif o000O000 == 50003 : Table_Menu ( O0o )
elif o000O000 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif o000O000 == 60001 : i1ii1iIi ( )
elif o000O000 == 60002 : o0O0 ( OO0O000 )
elif o000O000 == 60003 : OOOO00 ( OoO )
elif o000O000 == 600033 : i11ii1 ( OoO )
elif o000O000 == 60004 : oO0oo ( OoO )
elif o000O000 == 50004 : o0OO0 ( )
elif o000O000 == 50005 : speedtest . runtest ( OoO )
elif o000O000 == 70001 : iIIii1iiiIiiI ( )
elif o000O000 == 70002 : ooi11I ( OoO )
elif o000O000 == 70003 : i111111 ( OoO )
elif o000O000 == 70004 : o0oO0OOoO0OoO0 ( OoO )
elif o000O000 == 70005 : iI11IiiiIII ( OoO )
elif o000O000 == 70006 : i1i1Ii ( )
elif o000O000 == 50006 : o0OIiII ( i1 , i1111 )
elif o000O000 == 80000 : OOOo0Oo0O ( )
elif o000O000 == 80001 : resolvefilmon ( OoO )
elif o000O000 == 80002 : II1ii1 ( )
elif o000O000 == 80003 : o000Ooo00o00O ( OO0O000 , OoO , "None" )
elif o000O000 == 80004 : OOOOiiI ( OO0O000 , OoO )
elif o000O000 == 80005 : III1i11 ( )
elif o000O000 == 80006 : OoOOoooO000 ( OoO )
elif o000O000 == 80007 : OoO0o000oOo ( OoO )
elif o000O000 == 80008 : Oo00OO00o0oO ( )
elif o000O000 == 80009 : oo0OOo ( )
elif o000O000 == 80010 : OOIiI1IIIiI1I1i ( OoO )
elif o000O000 == 80011 : OoO00O00O0 ( OoO )
elif o000O000 == 80012 : I11iIIi1Iii ( )
elif o000O000 == 90000 : O00O0O0 ( OO0O000 , OoO )
elif o000O000 == 90001 : tools ( )
elif o000O000 == 90002 : oooooOOO000Oo ( )
elif o000O000 == 90003 : oOooooo ( OoO )
elif o000O000 == 90004 : OO00iI1iII1 ( OoO )
elif o000O000 == 90005 : o0iiI11 ( OoO )
elif o000O000 == 90006 : oo0OooOoOo ( OoO )
elif o000O000 == 90007 : iIIii1i1iIiI ( OoO )
elif o000O000 == 90008 : O0oo ( OoO )
elif o000O000 == 90009 : iiIi ( OoO )
elif o000O000 == 90010 : ooo ( )
elif o000O000 == 90020 : i11iI11ii ( )
elif o000O000 == 90021 : hellyeah2 ( OoO )
elif o000O000 == 90022 : hellyeah3 ( OoO )
elif o000O000 == 90023 : o0oooO ( )
elif o000O000 == 90024 : oOOOOOoOO ( OoO )
elif o000O000 == 90025 : oo00OoO ( OoO )
if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif o000O000 == 90026 : ooO000OO ( )
elif o000O000 == 90027 : I1iI11IiiI11i ( OO0O000 , OoO , O0o )
elif o000O000 == 90028 : IIII1ii1 ( OoO )
if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif o000O000 == 900300 : ooO ( )
elif o000O000 == 900301 : Ooo0oOooo0 ( OoO )
elif o000O000 == 900302 : II11IiIi11 ( OoO )
elif o000O000 == 90030 : OOo0 ( )
elif o000O000 == 90031 : I1III1111iIi ( )
elif o000O000 == 90032 : I1i111I ( OoO )
elif o000O000 == 90033 : OooOo0oo0O0o00O ( OoO )
elif o000O000 == 90034 : OOOooo ( OoO )
elif o000O000 == 90035 : o0OOo0o0O0O ( OoO )
elif o000O000 == 90036 : iI1II ( OoO )
elif o000O000 == 90039 : OO0o0oO0 ( OoO )
elif o000O000 == 90037 : IiiI1iiiiI1iI ( OoO )
elif o000O000 == 900377 : i1I1 ( OoO )
elif o000O000 == 90038 : iIIi ( )
if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif o000O000 == 10090 : o0ii1i ( )
elif o000O000 == 10091 : iIIii ( OoO )
elif o000O000 == 10092 : Iii1iiIIi1i111i ( OoO )
elif o000O000 == 10093 : i1iI1Ii1 ( OoO , iiiI1I1iIIIi1 )
elif o000O000 == 10094 : o0OO00oO00 ( OoO , iiiI1I1iIIIi1 )
if 55 - 55: i1iIi - I11i
elif o000O000 == 10095 : ii11i ( )
elif o000O000 == 10096 : oOOOO ( OoO )
elif o000O000 == 10097 : OoO0o0000O ( OoO )
elif o000O000 == 10098 : I1I11ii ( OoO )
elif o000O000 == 10099 : i1iii1ii ( OoO )
if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif o000O000 == 10200 : i1i111iI ( )
elif o000O000 == 10201 : oo00ooOoo ( OoO )
elif o000O000 == 10202 : iIi1IIi1ii ( OoO )
elif o000O000 == 10203 : RT4 ( OoO )
if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif o000O000 == 90040 : O0oO ( )
elif o000O000 == 90041 : OOOOOooOOoo ( OoO )
elif o000O000 == 90042 : ooOoo000oO ( OoO )
elif o000O000 == 90043 : o0OoOOo ( OoO )
elif o000O000 == 90044 : i1I1i1I ( OoO )
elif o000O000 == 90045 : iIi1i1iIi1Ii1 ( )
elif o000O000 == 90046 : oO0o0O ( OoO )
elif o000O000 == 90050 : oO00o ( )
elif o000O000 == 90051 : o0o00O0oOooO0 ( OoO )
elif o000O000 == 90052 : III1iii1i1II ( OoO )
elif o000O000 == 90053 : iiiiI1IiI1I1 ( OoO )
elif o000O000 == 90054 : O0o00oO0oOO ( OoO )
elif o000O000 == 90055 : II1I1i1i1iii ( )
if 37 - 37: Iii
elif o000O000 == 100001 : Stand_up ( )
if 19 - 19: ii % i1IiiiI1iI
elif o000O000 == 100003 : iIIiI1I1i ( OoO )
elif o000O000 == 100004 : Ooo0oo ( OoO )
elif o000O000 == 100005 : Resolve ( OoO )
elif o000O000 == 100008 : Search ( )
elif o000O000 == 100007 : IioO0oOOO0Ooo ( OoO )
elif o000O000 == 100009 : yt . PlayVideo ( OoO )
elif o000O000 == 100010 : OOOoooOo00oo0000OO ( OoO )
elif o000O000 == 100100 : ii1i1i1IiII ( iiiI1I1iIIIi1 , OoO , IIi1IiiI1i1 )
elif o000O000 == 100101 : oo0ooOO ( OoO , OO0O000 , iI , IIi1IiiI1i1 , iiiI1I1iIIIi1 )
elif o000O000 == 100102 : i1iIi1II11 ( OO0O000 , OoO , iiiI1I1iIIIi1 , iI )
elif o000O000 == 100106 : oO0OO0 ( OoO , OO0O000 )
elif o000O000 == 100107 : iIII11Ii ( )
elif o000O000 == 100108 : iiIi1i1iIi1I ( )
elif o000O000 == 100109 : Iii11II ( OoO )
elif o000O000 == 40000 : Ii11IiIiiii1 ( )
elif o000O000 == 40001 : iI1 ( OoO )
elif o000O000 == 100110 : IIiI1111i1 ( )
elif o000O000 == 100111 : ii1ii1I1IIi1 ( OoO )
elif o000O000 == 100110 : IIiI1111i1 ( )
elif o000O000 == 100210 : iiiI1ii ( OoO )
elif o000O000 == 100211 : iIiI1ii ( )
elif o000O000 == 100212 : o0OOOOOo0 ( )
elif o000O000 == 100213 : IIIiiiIiI ( )
elif o000O000 == 100214 : ooIi11iI ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
