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
IiiIII111iI = "3.2.9"
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
I11 = xbmc . translatePath ( 'special://home/' )
Oo0o0000o0o0 = os . path . join ( I11 , 'userdata' )
oOo0oooo00o = os . path . join ( Oo0o0000o0o0 , 'addon_data' , IiII )
oO0o0o0ooO0oO = os . path . join ( oOo0oooo00o , 'wizard.log' )
oo0o0O00 = uservar . ADDONTITLE
oO = xbmc . translatePath ( 'special://profile/' )
i1iiIIiiI111 = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1i1II = os . path . join ( I11 , 'addons' )
oooOOOOO = os . path . join ( i1i1II , 'packages' )
i1iiIII111ii = os . path . join ( i1i1II , 'HUB' )
i1iIIi1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
ii11iIi1I = Net ( )
iI111I11I1I1 = xbmcgui . Dialog ( )
OOooO0OOoo = oo00 . getSetting ( 'Build' )
iIii1 = oo00 . getSetting ( 'Local' )
oOOoO0 = oo00 . getSetting ( 'Remote' )
O0OoO000O0OO = oo00 . getSetting ( 'LocalM3u' )
iiI1IiI = oo00 . getSetting ( 'TEXTCOL' )
II = oo00 . getSetting ( 'Downloads' )
ooOoOoo0O = xbmc . translatePath ( 'special://logpath/' )
OooO0 = oo00 . getSetting ( 'User' )
II11iiii1Ii = oo00 . getSetting ( 'Pass' )
OO0o = oo00 . getSetting ( 'AdultPass' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
O0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
Oo00OOOOO = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
O0O = xbmc . translatePath ( 'special://database' )
O00o0OO = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
I11i1 = xbmc . translatePath ( 'special://thumbnails' ) ;
iIi1ii1I1 = "GenieTv"
o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
I11II1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
IIIII = 'http://'
ooooooO0oo = base64 . decodestring ( 'LnBocA==' )
IIiiiiiiIi1I1 = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
I1IIIii = [ ]
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
OOO00 = oo00 . getLocalizedString
iiiiiIIii = CookieJar ( )
O000OO0 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( iiiiiIIii ) )
O000OO0 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
I11iii1Ii = int ( sys . argv [ 1 ] )
I1IIiiIiii = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
O000oo0O = os . path . join ( O00o0OO , 'favorites' )
OOOOi11i1 = O00o0OO + '/addons.ini'
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/userdata/' )
IIIii1II1II = xbmc . translatePath ( 'special://home/userdatabroke/' )
i1I1iI = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
oo0OooOOo0 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
o0O = oo0OooOOo0 + 'GenieTvWatched'
O00oO = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
I11i1I1I = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( o0O ) :
 os . makedirs ( o0O )
oO0Oo = o0O + 'watched.txt'
if not os . path . exists ( oO0Oo ) :
 open ( oO0Oo , 'w+' )
oOOoo0Oo = open ( oO0Oo ) . read ( )
o00OO00OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
OOOO0OOoO0O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( O000oo0O ) == True :
 Oo0oOOo = open ( O000oo0O ) . read ( )
else : Oo0oOOo = [ ]
Oo0OoO00oOO0o = oo00 . getSetting ( 'debug' )
if os . path . exists ( O00o0OO ) == False :
 os . makedirs ( O00o0OO )
def OOO00O ( url ) :
 OOoOO0oo0ooO = urllib2 . Request ( url )
 OOoOO0oo0ooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0o0O00Oo0o0 = ''
 O00O0oOO00O00 = ''
 try :
  O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
  O00O0oOO00O00 = O0o0O00Oo0o0 . read ( )
  O0o0O00Oo0o0 . close ( )
 except : pass
 if O00O0oOO00O00 != '' :
  return O00O0oOO00O00
 else :
  O00O0oOO00O00 = 'Failed'
  return O00O0oOO00O00
  if 11 - 11: Ooo00oOo0oOo . o000O0o
iI1iII1 = [ ]
oO0OOoo0OO = OOO00O ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if oO0OOoo0OO != 'Failed' :
 iI1iII1 . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not oO0OOoo0OO != 'Failed' :
 O0 = OOO00O ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if O0 != 'Failed' :
  iI1iII1 . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not O0 != 'Failed' :
  ii1ii1ii = OOO00O ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if ii1ii1ii != 'Failed' :
   iI1iII1 . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not ii1ii1ii != 'Failed' :
   oooooOoo0ooo = OOO00O ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
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
  iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIiIi1iI = 'genie tv repo not being installed '
  i1IiiiI1iI ( )
 else :
  i1iIi ( )
  if 68 - 68: iiiiiiii1 % I1ii11iIi11i / Ii1IIIi1
def i1iIi ( ) :
 if 51 - 51: o0o00Oo0O % Ii * I1111IIi . Ii1I * Ii1IIIi1 - oO0o
 i1I11 = IIII ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 iiIiI = open ( Ii1iIiII1ii1 ) . read ( )
 o00oooO0Oo = open ( ooOooo000oOO ) . read ( )
 if 78 - 78: ooOOOoO % I1111IIi + Ii1I
 OOooOoooOoOo = re . compile ( 'version="([^"]*)" provider' ) . findall ( iiIiI )
 o0OOOO00O0Oo = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( o00oooO0Oo )
 iioOooOOOoOo = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( i1I11 )
 i1Iii1i1I = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( i1I11 )
 for OOoO00 in OOooOoooOoOo :
  IiI111111IIII = OOoO00
  for i1Ii in iioOooOOOoOo :
   if not i1Ii == IiI111111IIII :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    ii111iI1iIi1 ( )
   if i1Ii == IiI111111IIII :
    OOO
 for oo0OOo0 in o0OOOO00O0Oo :
  I11IiI = oo0OOo0
  for O0ooO0Oo00o in i1Iii1i1I :
   if not O0ooO0Oo00o == I11IiI :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    i1IiiiI1iI ( )
   if O0ooO0Oo00o == I11IiI :
    xbmc . sleep ( 100 )
    OOO
def ooO0oOOooOo0 ( ) :
 Oo0oO ( )
 i1I1ii11i1Iii ( )
 I1IiiiiI ( o0OIiII )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1iII1II ( )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , Ooo , '' )
  I1I1i1I ( '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '' , 50006 , III1iII1I1ii + 'Contact-Us.png' , Ooo , '' )
  I1I1i1I ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , III1iII1I1ii + 'settings.png' , Ooo , '' )
  I1I1i1I ( '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , III1iII1I1ii + 'GenieUpdate.png' , Ooo , '' )
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , Ooo , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , III1iII1I1ii + 'tommys.png' , Ooo , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , Ooo , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1I1IiI1 ) , 32 , III1iII1I1ii + 'BuildersToolbox.png' , Ooo , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   I1I1i1I ( '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , str ( I1I1IiI1 ) , 46 , III1iII1I1ii + 'SoruceList.png' , Ooo , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , Ooo , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '' , 10050 , III1iII1I1ii + 'Addons.png' , Ooo , '' )
  if ii1I ( ) == 'android' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( I1I1IiI1 ) , 30039 , III1iII1I1ii + 'APKTools.png' , Ooo , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , str ( I1I1IiI1 ) , 39 , III1iII1I1ii + 'GenieTVRSSFeed.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def ii1iII1II ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , Ooo , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , Ooo , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , Ooo , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , III1iII1I1ii + 'tommys.png' , Ooo , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def oO0O0OO0O ( ) :
 OO = [ '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , '[COLOR' + iiI1IiI + ']GUIDE SKINS[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OO )
 if OoOoO == 0 :
  ii111iI1iIi1 ( )
 if OoOoO == 1 :
  Ii1I1i ( )
 if OoOoO == 2 :
  OOI1iI1ii1II ( )
 if OoOoO == 3 :
  O0O0OOOOoo ( )
 if OoOoO == 4 :
  oOooO0 ( o0OIiII )
 if OoOoO == 5 :
  iI111I11I1I1 . ok ( i1 , i1111 )
 if OoOoO == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if OoOoO == 7 :
  Ii1I1Ii ( )
 if OoOoO == 8 :
  OOoO0 ( )
def OOoO0 ( ) :
 o0OIiII = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( o0OIiII , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( o0OIiII )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
def O0O0ooOOO ( ) :
 oOOo0O00o = iIiIi11 ( )
 OOOiiiiI = oOOo0O00o . replace ( ooOoOoo0O , "" )
 if os . path . exists ( oOOo0O00o ) or not oOOo0O00o == False :
  oooOo0OOOoo0 = open ( oOOo0O00o , mode = 'r' ) ; OOoO = oooOo0OOOoo0 . read ( ) ; oooOo0OOOoo0 . close ( )
  OO0O000 ( "%s - %s" % ( i1 , OOOiiiiI ) , OOoO )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OOoO0 ( ) :
 o0OIiII = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( o0OIiII , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( o0OIiII )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
def iiIiI1i1 ( ) :
 I1I1i1I ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , str ( I1I1IiI1 ) , 90030 , III1iII1I1ii + 'tgames.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , str ( I1I1IiI1 ) , 90031 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , Ooo , '' )
 if 69 - 69: iiiiiiii1
def I11iII ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 OOooOoooOoOo = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I11iI1i1I11I11 , o000O0O in OOooOoooOoOo :
  OO0O000 ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]  ' + I11iI1i1I11I11 , o000O0O )
def I1i1i1iii ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
 iIIII = IIII ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 OOooOoooOoOo = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 90032 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
def iIIii ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , o00O0O , Ooo , '' )
 for url in next :
  Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , III1iII1I1ii + 'NEXT.png' , Ooo , '' )
def ii1iii1i ( url ) :
 iIIII = IIII ( url )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 OOooOoooOoOo = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
 for I1111i , url in o0OOOO00O0Oo :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
 for I1111i , url in ooOoO00 :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
 for url in Iii1I1111ii :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , III1iII1I1ii + 'tommysreplays.png' , Ooo , '' )
  if 14 - 14: ooOoO0O00 - I11i % o0o00Oo0O - oO0o
def ooO0O00Oo0o ( url ) :
 if 'drive' in url :
  OOOOo0o00OO0000 ( url )
 else :
  iIIII = IIII ( url )
  OOooOoooOoOo = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( iIIII )
  for url in OOooOoooOoOo :
   OOOOo0o00OO0000 ( url )
def I1i ( url ) :
 O00Oooo = liveresolver . resolve ( url )
 i11I = xbmcgui . ListItem ( path = O00Oooo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
def o00Oo0oooooo ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 O0oO0iII11 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0iII11 )
def iIiIi11 ( ) :
 iiIiii1IIIII = False
 if os . path . exists ( os . path . join ( ooOoOoo0O , 'xbmc.log' ) ) :
  iiIiii1IIIII = os . path . join ( ooOoOoo0O , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'kodi.log' ) ) :
  iiIiii1IIIII = os . path . join ( ooOoOoo0O , 'kodi.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'spmc.log' ) ) :
  iiIiii1IIIII = os . path . join ( ooOoOoo0O , 'spmc.log' )
 elif os . path . exists ( os . path . join ( ooOoOoo0O , 'tvmc.log' ) ) :
  iiIiii1IIIII = os . path . join ( ooOoOoo0O , 'tvmc.log' )
 return iiIiii1IIIII
 if 67 - 67: ooOOOoO / O0OOOoOoo0
def iiIiIIIiiI ( url ) :
 if url == 'http://' : return False
 try :
  OOoOO0oo0ooO = urllib2 . Request ( url )
  OOoOO0oo0ooO . add_header ( 'User-Agent' , I1i1iiI1 )
  O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
  O0o0O00Oo0o0 . close ( )
 except Exception , iiI1IIIi :
  return iiI1IIIi
 return True
 if 47 - 47: I1ii11iIi11i % Ii1IIIi1 % Ii - o0o00Oo0O + iiiiiiii1
def ooO000OO0O00O ( ) :
 O00O0oOO00O00 = IIII ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 if len ( OOooOoooOoOo ) > 0 :
  for I1111i , o0OIiII , OOOoOO0o , i1II1 in OOooOoooOoOo :
   I1I1i1I ( I1111i , o0OIiII , 50005 , OOOoOO0o , i1II1 , '' )
def i11i1 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , OO )
  if OoOoO == 0 :
   IiiiiI1i1Iii ( )
  if OoOoO == 1 :
   oo00oO0o ( )
  if OoOoO == 2 :
   iiii111II ( I11iIiI1I1i11 )
  if OoOoO == 3 :
   OOoooO00o0oo0 ( o0OIiII )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WISHES PC[/COLOR]' , str ( I1I1IiI1 ) , 1 , III1iII1I1ii + 'WISHESPC.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 61 - 61: ooOOOoO / Ii1I % O0OOOoOoo0 + iiiiiiii1 / I1111IIi . iiiiiiii1
def IiIi1I1 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if OO0o == '5knuckleshuffle' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , Ooo , '' )
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , Ooo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , Ooo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   I1I1i1I ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STREAM CATEGORIES[/COLOR]' , str ( I1I1IiI1 ) , 90002 , III1iII1I1ii + 'cats.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , Ooo , '' )
 else :
  if OO0o == '5knuckleshuffle' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , Ooo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , Ooo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   I1I1i1I ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 4004 , III1iII1I1ii + 'Movies.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( I1I1IiI1 ) , 4005 , III1iII1I1ii + 'TVShows.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 4007 , III1iII1I1ii + 'Kids.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , str ( I1I1IiI1 ) , 30032 , III1iII1I1ii + 'News.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'GenieTVTutorials.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , str ( I1I1IiI1 ) , 4008 , III1iII1I1ii + 'Hobbies.png' , Ooo , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '' , 10003 , III1iII1I1ii + 'StandUp.png' , Ooo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , str ( I1I1IiI1 ) , 8040 , III1iII1I1ii + 'documentaries.png' , Ooo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , str ( I1I1IiI1 ) , 7001 , III1iII1I1ii + 'DiscloseTV.png' , Ooo , '' )
   if 39 - 39: IIiIiII11i + OOooOOo - iiiiiiii1 . OOooOOo
   if 84 - 84: oO0o + ooOoO0O00 - IIiIiII11i . Ii1I * ii + oOo0O0Ooo
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']24/7 STREAMS[/COLOR]' , '' , 30030 , III1iII1I1ii + '247Streams.png' , Ooo , '' )
  if 38 - 38: o000O0o + IIiIiII11i % iiiiiiii1 % OOooOOo - ooOOOoO / ii
  if 73 - 73: I11i * o0o00Oo0O - Ii
  if 85 - 85: ooOOOoO % ii1ii11IIIiiI + Ii1IIIi1 / I11i . Ooo00oOo0oOo + o000O0o
  if 62 - 62: Ii + Ii - I11i
  if 28 - 28: ii1ii11IIIiiI . ii1ii11IIIiiI % iI11I1II1I1I * iI11I1II1I1I . I11i / ii1ii11IIIiiI
  if 27 - 27: oO0o + iiiiiiii1 - ooOoO0O00
  if 69 - 69: O0OOOoOoo0 - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
  if 79 - 79: o0o00Oo0O * Ii - O0OOOoOoo0 / O0OOOoOoo0
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , Ooo , '' )
  if 48 - 48: o0o00Oo0O
  if 93 - 93: Ii - oOo0O0Ooo * Ii1I * Ii1IIIi1 % o0o00Oo0O + ii
  if 25 - 25: O0OOOoOoo0 + ooOOOoO / iiiiiiii1 . I11i % o0o00Oo0O * oO0o
  if 84 - 84: iiiiiiii1 % ooOOOoO + Ii
  if 28 - 28: I1ii11iIi11i + oO0o * o000O0o % Ooo00oOo0oOo . Ii1IIIi1 % o0o00Oo0O
  if 16 - 16: Ii1IIIi1 - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
 O0oO0 ( 'movies' , 'MAIN' )
def iIiIiIiI ( ) :
 OO = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , OO )
 if OoOoO == 0 :
  i11OOoo ( )
 if OoOoO == 1 :
  iIIiiiI ( )
 if OoOoO == 2 :
  oo0 ( )
 if OoOoO == 3 :
  IiI111ii1ii ( )
 if OoOoO == 4 :
  O0OOo ( )
 if OoOoO == 5 :
  IiIII1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , O0Oo000 , I1111i )
 if OoOoO == 6 :
  iiI11i1II ( )
 if OoOoO == 7 :
  OO0O0OOo0O ( )
 if OoOoO == 8 :
  I1 ( )
 if OoOoO == 9 :
  o0OooOOOOOO ( )
 if OoOoO == 10 :
  OOooO0o0 ( )
  if 15 - 15: ooOoO0O00 + OOooOOo
  if 48 - 48: oOo0O0Ooo % ii1ii11IIIiiI / iI11I1II1I1I
def i1I1ii11i1Iii ( ) :
 if not os . path . exists ( I11II1i ) :
  OO0O000 ( 'Change Log 21/11/16 - v3.2.9' , 'Download option added, Search series fixed, Watch series under maintenance but back up, Scooby streams back up and running' )
  os . makedirs ( I11II1i )
  if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
  if 96 - 96: ii + Ooo00oOo0oOo
def i11OOoo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , OO )
  if OoOoO == 0 :
   iiII1i11i ( )
  if OoOoO == 1 :
   IiIi ( o0OIiII )
  if OoOoO == 2 :
   OOOOO0O00 ( )
  if OoOoO == 3 :
   Iii ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if OoOoO == 4 :
   iIIiIiI1I1 ( )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , Ooo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , Ooo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def ooO ( ) :
 Oo0oO ( )
 iiOO0O0Ooo ( )
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . ii1ii11IIIiiI % ii1ii11IIIiiI + Ii
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , Ooo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I1i1I ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , Ooo , '' )
 I1I1i1I ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , III1iII1I1ii + 'linkchannels.png' , Ooo , '' )
def OOooO0o0 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0o0Oo , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0o0Oo , Ooo , '' )
 if 72 - 72: iI11I1II1I1I * ooOOOoO % iiiiiiii1 / oO0o
 if 35 - 35: iiiiiiii1 + ooOoO0O00 % Ii1I % Ii1IIIi1 + Ooo00oOo0oOo
 if 17 - 17: ooOoO0O00
 if 21 - 21: I1ii11iIi11i
 if 29 - 29: Ii1IIIi1 / IIiIiII11i / iiiiiiii1 * o000O0o
def iIIiiiI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , OO )
  if OoOoO == 0 :
   I111i1i1111 ( )
  if OoOoO == 1 :
   IIII1 ( )
  if OoOoO == 2 :
   I1I1i ( )
  if OoOoO == 3 :
   I1IIIiIiIi ( )
  if OoOoO == 4 :
   IIIII1 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , Ooo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , III1iII1I1ii + 'WatchSeries.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , Ooo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def iIi1Ii1i1iI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   IIiI1 = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   i1iI1 = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   ii1I1IiiI1ii1i = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   O0o = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   oO0OoO00o = '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]'
  OO = [ IIiI1 , i1iI1 , ii1I1IiiI1ii1i , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , oO0OoO00o , '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , O0o ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , OO )
  if OoOoO == 0 :
   IiIII1 ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , O0Oo000 , I1111i )
  if OoOoO == 1 :
   IiIII1 ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , O0Oo000 , I1111i )
  if OoOoO == 2 :
   II1iiiiII ( )
  if OoOoO == 3 :
   IiIII1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , O0Oo000 , I1111i )
  if OoOoO == 4 :
   O0OoOO0oo0 ( )
  if OoOoO == 5 :
   IiIII1 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , O0Oo000 , I1111i )
  if OoOoO == 6 :
   oOO ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , Ooo , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , 1016 , III1iII1I1ii + 'TheReaper.png' , Ooo , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , Ooo , '' )
   if 53 - 53: I1111IIi * O0OOOoOoo0 . I1ii11iIi11i - ooOOOoO % ooOOOoO * Ii
   if 7 - 7: o0o00Oo0O . ooOOOoO
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , Ooo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , III1iII1I1ii + 'appstreams.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , III1iII1I1ii + 'raiztv.png' , Ooo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 1023 , III1iII1I1ii + 'ScoobyStreams.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'ITVStreams.png' , Ooo , '' )
  if 51 - 51: oO0o - o0o00Oo0O % Ooo00oOo0oOo - IIiIiII11i
 O0oO0 ( 'movies' , 'MAIN' )
 if 31 - 31: ii1ii11IIIiiI / I1ii11iIi11i - ii1ii11IIIiiI - o000O0o
def I1iiIIIi11 ( ) :
 Oo0oO ( )
 I1I1i1I ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , Ooo , '' )
def Ii1I11ii1i ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 url = url
 OOooOoooOoOo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
 for OOo0 , ii11I1 in OOooOoooOoOo :
  if '[DIR]' in OOo0 :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + ii11I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii11I1 , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in ii11I1 :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + ii11I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii11I1 , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in ii11I1 :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + ii11I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii11I1 , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 21 - 21: Ooo00oOo0oOo / Ii1I + ooOOOoO + ii
def O0OoOO0oo0 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , Ooo , '' )
 if 91 - 91: Ii / ooOoO0O00 + ii1ii11IIIiiI + iiiiiiii1 * Ii
def OoOoOo00o0 ( url ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1111i , url , oo000ii , OoO , i1II1 , Iiiiii111i1ii in OOooOoooOoOo :
  if OoO == '123' :
   OoO = III1iII1I1ii + 'appstreams.png'
  if i1II1 == '123' :
   i1II1 = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100010 , OoO , i1II1 , Iiiiii111i1ii )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100007 , OoO , i1II1 , Iiiiii111i1ii )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100100 , OoO , i1II1 , Iiiiii111i1ii )
  elif not 'http' in url :
   i1i1iII1 ( I1111i , url , 100009 , OoO , i1II1 , Iiiiii111i1ii , '' )
  else :
   i1i1iII1 ( I1111i , url , 100005 , OoO , i1II1 , Iiiiii111i1ii , '' )
   if 25 - 25: iI11I1II1I1I % ii1ii11IIIiiI . iiiiiiii1
def IIIIi1 ( url ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 iIi11iiIiI1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , Iiiiii111i1ii , i1II1 , I1111i in iIi11iiIiI1I :
  if o00O0O == '123' :
   o00O0O = III1iII1I1ii + 'appstreams.png'
  if i1II1 == '123' :
   i1II1 = Ooo
  if 'php' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100004 , o00O0O , i1II1 , Iiiiii111i1ii )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100007 , o00O0O , i1II1 , Iiiiii111i1ii )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( I1111i , url , 100100 , o00O0O , i1II1 , Iiiiii111i1ii )
  elif not 'http' in url :
   i1i1iII1 ( I1111i , url , 100009 , o00O0O , i1II1 , Iiiiii111i1ii , '' )
  else :
   i1i1iII1 ( I1111i , url , 100005 , o00O0O , i1II1 , Iiiiii111i1ii , '' )
   if 3 - 3: ooOoO0O00 / IIiIiII11i / Ii * ooOoO0O00 - IIiIiII11i
def IiiII1111III1I ( url ) :
 if 39 - 39: ooOoO0O00 / O0OOOoOoo0
 oO0OOoo0OO = OO0ooo0oOO ( url )
 oO000oOo00o0o = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in oO000oOo00o0o :
  OoO = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for OoO in OoO :
   OoO = OoO
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  O0Oo00OoOo = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O00oO0 ) )
  for O0Oo00OoOo in O0Oo00OoOo :
   O0Oo00OoOo = O0Oo00OoOo
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for url in url :
   url = url
  i1i1iII1 ( '[COLORred]' + str ( O0Oo00OoOo ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( OoO ) , Ooo , '' , '' )
  O0oO0 ( 'movies' , '' )
  if 24 - 24: Ii - I1111IIi
  if 21 - 21: Ii1IIIi1
  if 92 - 92: Ii / I1111IIi - ii1ii11IIIiiI % iiiiiiii1 * I1111IIi + I1ii11iIi11i
  if 11 - 11: ii . I1111IIi
  if 80 - 80: ii - o000O0o * ooOOOoO * Ii1I / oOo0O0Ooo / o000O0o
def I1I11iI11iI1i ( iconimage , url , extra ) :
 OoO = ' '
 oo0o0O0Oooooo = ' '
 i1II1 = ' '
 i11IIIiI1I = ' '
 o0iiiI1I1iIIIi1 = OO0ooo0oOO ( url )
 OoO = re . compile ( '<img src="(.+?)">' ) . findall ( o0iiiI1I1iIIIi1 )
 for OoO in OoO :
  OoO = OoO
 IiiI1iiiiI1iI = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( o0iiiI1I1iIIIi1 )
 for i1II1 in IiiI1iiiiI1iI :
  i1II1 = i1II1
 OOooOoooOoOo = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( o0iiiI1I1iIIIi1 )
 for url , i11IIIiI1I in OOooOoooOoOo :
  i11IIIiI1I = 'S' + ( i11IIIiI1I ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = O00oO + url
  iIiiiii1i ( ( i11IIIiI1I ) . replace ( '  ' , '' ) , url , 100101 , OoO , i1II1 , oo0o0O0Oooooo , '' )
  O0oO0 ( 'Movies' , 'info' )
  if 40 - 40: o0o00Oo0O - ii - O0OOOoOoo0
def iIiii ( url , name , fanart , extra , iconimage ) :
 OOOO00OO0O0 = extra
 i11IIIiI1I = name
 o0iiiI1I1iIIIi1 = OO0ooo0oOO ( url )
 OoO = iconimage
 OOooOoooOoOo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( o0iiiI1I1iIIIi1 )
 for url , name , i1I111Ii1i11 in OOooOoooOoOo :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = O00oO + url
  i1I111Ii1i11 = i1I111Ii1i11
  o0O0O0o = name + ' - [COLORred]' + i1I111Ii1i11 + '[/COLOR]'
  iIiiiii1i ( o0O0O0o , url , 100102 , OoO , fanart , 'Aired : ' + i1I111Ii1i11 , o0O0O0o )
  if 92 - 92: I1ii11iIi11i . oOo0O0Ooo + OOooOOo / ooOOOoO * I11i - oO0o
def i111IiiII ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = OO0ooo0oOO ( URL )
 OOooOoooOoOo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , name in OOooOoooOoOo :
  for i11I in I11i1I1I :
   if i11I in o0OIiII :
    URL = 'http://www.watchseriesgo.to/link/' + o0OIiII
    i1i1iII1 ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , Ooo , '' , '' )
 if len ( OOooOoooOoOo ) <= 0 :
  iIiiiii1i ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 42 - 42: Ooo00oOo0oOo + IIiIiII11i . iI11I1II1I1I
  if 61 - 61: O0OOOoOoo0 . ooOoO0O00 / I1111IIi % Ii * ii1ii11IIIiiI
def i1i1i1I ( url , name ) :
 oOoo000 = name
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OooOo00o ( url , oOoo000 )
 for url in o0OOOO00O0Oo :
  OooOo00o ( url , oOoo000 )
 for url in ooOoO00 :
  OooOo00o ( url , oOoo000 )
  if 20 - 20: ooOoO0O00 * I1111IIi + IIiIiII11i % I11i % Ooo00oOo0oOo
def OooOo00o ( url , season_name ) :
 if 'daclips.in' in url :
  iIi1II ( url , season_name )
 elif 'filehoot.com' in url :
  I1iIiI11I1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  i1oOOoo0o0OOOO ( url , season_name )
 elif 'vidspot.net' in url :
  i1IiII1III ( url , season_name )
 elif 'vodlocker' in url :
  i1O00oo ( url , season_name )
 elif 'vidto' in url :
  O0OO00O0oOO ( url , season_name )
  if 4 - 4: ii - ooOoO0O00 % ooOOOoO - o000O0o * I11i
  if 85 - 85: ii * iI11I1II1I1I . ii1ii11IIIiiI / ii % oOo0O0Ooo % o0o00Oo0O
def O0OO00O0oOO ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii , I1111i in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 21 - 21: I1111IIi - oOo0O0Ooo + Ii1IIIi1
  if 78 - 78: ii - Ii - IIiIiII11i
def i1oOOoo0o0OOOO ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii , I1111i in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 77 - 77: OOooOOo % ooOOOoO
def i1IiII1III ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1iii , I1111i in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def i1O00oo ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 2 - 2: ii % o000O0o
def iIi1II ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for I1iii in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def I1iIiI11I1 ( url , season_name ) :
 oO0OOoo0OO = OO0ooo0oOO ( url )
 OOooOoooOoOo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii in OOooOoooOoOo :
  oO0o0O0Ooo0o ( I1iii , season_name )
  if 39 - 39: ii1ii11IIIiiI / IIiIiII11i / Ii1I % oOo0O0Ooo
def oO0o0O0Ooo0o ( Link , season_name ) :
 if 'http:/' in Link :
  O0Oo00 ( Link )
  if 41 - 41: iI11I1II1I1I % Ii1IIIi1
def oOo0oO ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 IIi1IIIIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in IIi1IIIIi :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 70 - 70: o000O0o / IIiIiII11i - iI11I1II1I1I - ii1ii11IIIiiI
def iIiiiii1i ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  if 88 - 88: ii1ii11IIIiiI
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = True )
 return i1ii
 if 19 - 19: IIiIiII11i * O0OOOoOoo0 + ooOOOoO
 if 65 - 65: o000O0o . I1111IIi . oO0o . ii1ii11IIIiiI - o000O0o
def i1i1iII1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  iioo0o0OoOOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = False )
 return i1ii
 if 19 - 19: Ii + ii1ii11IIIiiI % iiiiiiii1
def IIi ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 27 - 27: o000O0o % ooOOOoO
def O0OO0oOoO0O0O ( url ) :
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oo000oOo0 . play ( url ) . strip ( )
 except : pass
 if 50 - 50: oO0o . Ii - Ooo00oOo0oOo . Ooo00oOo0oOo
def O0Oo00 ( url ) :
 oo000oOo0 = xbmc . Player ( )
 import urlresolver
 try : oo000oOo0 . play ( url )
 except : pass
 if 31 - 31: o000O0o / I1ii11iIi11i * ooOoO0O00 . OOooOOo
def OO0ooo0oOO ( url ) :
 OOoOO0oo0ooO = urllib2 . Request ( url )
 OOoOO0oo0ooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0o0O00Oo0o0 = ''
 O00O0oOO00O00 = ''
 try :
  O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
  O00O0oOO00O00 = O0o0O00Oo0o0 . read ( )
  O0o0O00Oo0o0 . close ( )
 except : pass
 if O00O0oOO00O00 != '' :
  return O00O0oOO00O00
 else :
  O00O0oOO00O00 = 'Opened'
  return O00O0oOO00O00
  if 57 - 57: o000O0o + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
  if 83 - 83: I11i / Ii % iI11I1II1I1I . Ii1IIIi1 % Ooo00oOo0oOo . ii
  if 94 - 94: ooOOOoO + iI11I1II1I1I % oO0o
def IiI111ii1ii ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OO0oOOo ( )
  if OoOoO == 1 :
   OO0oO0o ( )
  if OoOoO == 2 :
   III111i11IiI ( )
  if OoOoO == 3 :
   O0000 ( )
  if OoOoO == 4 :
   ooO00O0O0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'SearchCartoons.png' , Ooo , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1IiI1 ) , 21004 , III1iII1I1ii + 'watchcartoons.png' , Ooo , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , III1iII1I1ii + 'Cartoons.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '' , 20000 , III1iII1I1ii + 'Cartoons.png' , Ooo , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , III1iII1I1ii + 'anime.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def iiI11i1II ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , Ooo , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , III1iII1I1ii + 'Fitness.png' , Ooo , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Go Fishing[/COLOR]' , str ( I1I1IiI1 ) , 8090 , III1iII1I1ii + 'GoFishing.png' , Ooo , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , III1iII1I1ii + 'GenieTVKitchen.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 33 - 33: I1ii11iIi11i
 if 49 - 49: oO0o % ii1ii11IIIiiI % ii1ii11IIIiiI / ii1ii11IIIiiI
 if 53 - 53: iI11I1II1I1I
def OOO ( ) :
 oO0OOoo0OO = IIII ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 OOooOoooOoOo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in OOooOoooOoOo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   oooo00o0o0o = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oooo00o0o0o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OoOoO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OoOoO == 0 :
    O0Oo00oO0O00 ( IIiIi1iI )
    I1iIIiiIIi1i ( )
   elif OoOoO == 1 :
    IiO000O0OO00oo ( IIiIi1iI )
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
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 iIIIII1iiiiII = os . path . join ( o0 , 'default.py' )
 oooO = open ( iIIIII1iiiiII , "w+" )
 if 22 - 22: iiiiiiii1 - iiiiiiii1 % o000O0o . I1111IIi + Ooo00oOo0oOo
 oooO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oooO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oooO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 63 - 63: oOo0O0Ooo % I1111IIi * I11i + I1111IIi / I1ii11iIi11i % ii1ii11IIIiiI
 if 45 - 45: O0OOOoOoo0
 if 20 - 20: ii * I11i * o0o00Oo0O . o000O0o
 if 78 - 78: iI11I1II1I1I + Ii1IIIi1 - ooOOOoO * I1111IIi - ii % OOooOOo
def i1OoOO ( ) :
 oO0OOoo0OO = IIII ( 'http://www.tvcatchup.com/channels/' )
 O0 = IIII ( 'http://www.djing.com/' )
 OOooOoooOoOo = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for iIII1I1i1i , o00O0O , o0OIiII in OOooOoooOoOo :
  Ii111iIi1iIi ( iIII1I1i1i , 'http://www.tvcatchup.com' + o0OIiII , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for o0OIiII , o00O0O , I1111i in o0OOOO00O0Oo :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   I1I1i1I ( 'DJing  ' + I1111i , o0OIiII , 90025 , 'http://www.djing.com' + o00O0O , Ooo , '' )
  O0oO0 ( 'movies' , 'MAIN' )
def o0OIIiI1I1 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'var url = "([^"]*)";' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
def I11I1IIiiII1 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 31 - 31: oOo0O0Ooo * Ooo00oOo0oOo + ii - ii1ii11IIIiiI / ii
def OOOOO0O00 ( ) :
 oO0oo ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = IIII ( 'http://www.join4films.com/' )
 OOooOoooOoOo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 80006 , III1iII1I1ii + 'Desi.png' )
def I111IIiii1Ii ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def II1 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def iiIIIiIii ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://www.join4films.com/?s=' + ( I1i11II ) . replace ( ' ' , '+' ) + '&search_type=1'
 I1iiioOO0OO0O = II11 . lower ( )
 I111IIiii1Ii ( I1iiioOO0OO0O )
 if 78 - 78: ooOOOoO / IIiIiII11i % OOooOOo
 if 52 - 52: o000O0o - ii1ii11IIIiiI * Ooo00oOo0oOo
 if 17 - 17: ii + o000O0o * Ii1IIIi1 * OOooOOo
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
 if 5 - 5: I1ii11iIi11i * OOooOOo
 if 46 - 46: iiiiiiii1
 if 33 - 33: ii1ii11IIIiiI - IIiIiII11i * ii - I1ii11iIi11i - o000O0o
 if 84 - 84: I1111IIi + I1ii11iIi11i - OOooOOo * OOooOOo
 if 61 - 61: ii . Ooo00oOo0oOo . ii / I1ii11iIi11i
 if 72 - 72: ooOoO0O00
 if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
 if 63 - 63: Ii1I
 if 6 - 6: iiiiiiii1 / Ii1I
 if 57 - 57: Ii1IIIi1
 if 67 - 67: oO0o . iiiiiiii1
 if 87 - 87: Ooo00oOo0oOo % ooOOOoO
 if 83 - 83: IIiIiII11i - Ii1IIIi1
def iiIii1IIi ( ) :
 Iii1I1I11iiI1 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
 if 10 - 10: Ii - I11i % iI11I1II1I1I
def i111IIIiI ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://imoviemax.se/?s=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iiioOO0OO0O = II11 . lower ( )
 III111iiIi1 ( I1iiioOO0OO0O )
def Ii11Ii ( url ) :
 IiIiIi1IIi = [ ]
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , O0OOOo in OOooOoooOoOo :
  if I1111i in IiIiIi1IIi :
   pass
  else :
   Iii1I1I11iiI1 ( I1111i + ' - ' + O0OOOo + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
   IiIiIi1IIi . append ( I1111i )
   if 31 - 31: Ii1IIIi1 % o000O0o * Ii1IIIi1
def IiI ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , I1i1iii1Ii in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i + ' - Views:' + I1i1iii1Ii , url , 10075 , III1iII1I1ii + 'genievision.png' , Ooo , '' )
  if 23 - 23: Ii
  if 39 - 39: I11i - Ii1I % ii1ii11IIIiiI * oO0o - o000O0o / ii1ii11IIIiiI
def III111iiIi1 ( url ) :
 iIiiiiii1 = [ ]
 oO0OOoo0OO = IIII ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  Iii1I1I11iiI1 ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , Ooo , '' )
 OOooOoooOoOo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  iIiiiiii1 . append ( I1111i )
  if 78 - 78: Ii1I + Ii1IIIi1 - o0o00Oo0O
def i1I1iIi1IiI ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for i1111O0O000OOOo , url in OOooOoooOoOo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i11ii1Ii1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i11ii1Ii1
  i1i1II1i11 = ( i1111O0O000OOOo ) . replace ( 'play-' , 'Server ' )
  I1I1i1I ( i1i1II1i11 , i11ii1Ii1 , 10076 , img , img , '' )
  if 91 - 91: Ii1IIIi1 / ooOoO0O00 * ooOoO0O00
def Ii1 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for ii11I1 in OOooOoooOoOo :
  if '=m' in ii11I1 :
   O0OoOOO00 ( ii11I1 )
  elif 'php' in ii11I1 :
   Ii1 ( url )
  else :
   oO0OOoo0OO = IIII ( ii11I1 )
   OOooOoooOoOo = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for o0ooOo0OOOO0o in OOooOoooOoOo :
    O0OoOOO00 ( ii11I1 )
    if 98 - 98: o000O0o + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
    if 24 - 24: I1ii11iIi11i - ooOoO0O00 + Ii1IIIi1
    if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( url ) :
 oO0OOoo0OO = IIII ( url )
 I1IIII1ii = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1I111Ii1i11 , IiIIi1I1I11Ii in I1IIII1ii :
  print 'there ><><><><><><><><><><><><'
  i1I111Ii1i11 = i1I111Ii1i11
  OOooOoooOoOo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiIIi1I1I11Ii ) )
  for I1111i , o0OO in OOooOoooOoOo :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + i1I111Ii1i11 + '[/COLOR] - ' + I1111i + ' - [COLOR' + iiI1IiI + ']' + o0OO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , Ooo , '' )
 O00oO0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1I111Ii1i11 , Oo in O00oO0 :
  print 'there ><><><><><><><><><><><><'
  i1I111Ii1i11 = i1I111Ii1i11
  OOooOoooOoOo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo ) )
  for I1111i , o0OO in OOooOoooOoOo :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + i1I111Ii1i11 + '[/COLOR] - ' + I1111i + ' - [COLOR' + iiI1IiI + ']' + o0OO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , Ooo , '' )
   if 23 - 23: IIiIiII11i / Ooo00oOo0oOo
   if 28 - 28: I1ii11iIi11i * iiiiiiii1 - oO0o
   if 19 - 19: Ii1IIIi1
def IIIII1 ( url ) :
 oO0OOoo0OO = IIII ( url )
 O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in O00oO0 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
  for OoO in OoO :
   OoO = 'http:' + OoO
  I1I1i1I ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , '' , '' )
  if 67 - 67: o0o00Oo0O % iI11I1II1I1I / O0OOOoOoo0 . Ii - ooOOOoO + o0o00Oo0O
  if 27 - 27: o000O0o
  if 89 - 89: IIiIiII11i / Ooo00oOo0oOo
  if 14 - 14: o000O0o . oOo0O0Ooo * iiiiiiii1 + IIiIiII11i - iiiiiiii1 + o000O0o
def Iii ( url ) :
 if 18 - 18: Ooo00oOo0oOo - I11i - oOo0O0Ooo - oOo0O0Ooo
 OOooo00 = [ ]
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii11I1 , o00O0O , I1111i , i1oO in OOooOoooOoOo :
  I1111i = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = IIII ( ii11I1 )
  o0OOOO00O0Oo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for IIi1IIIIi , oo0o0O0Oooooo in o0OOOO00O0Oo :
   iI = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oo0o0O0Oooooo ) )
   for Iiiiii111i1ii in iI :
    if I1111i in OOooo00 :
     pass
    else :
     I1I1i1I ( I1111i , IIi1IIIIi , 8043 , o00O0O , o00O0O , Iiiiii111i1ii )
     O0oO0 ( 'movies' , 'INFO' )
     OOooo00 . append ( I1111i )
     if 42 - 42: ii + I1ii11iIi11i % IIiIiII11i + oO0o
     if 24 - 24: ii1ii11IIIiiI * IIiIiII11i % ii1ii11IIIiiI % O0OOOoOoo0 + ii
def IiIiiiIii ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , O0Oo000 , Iiiiii111i1ii , i1II1 , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 10065 , O0Oo000 , i1II1 , Iiiiii111i1ii )
 O0oO0 ( 'movies' , 'INFO' )
 if 27 - 27: ooOoO0O00 % OOooOOo . oOo0O0Ooo + iiiiiiii1 % OOooOOo
def o0o0oOo000o0 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'https://www.youtube.com/results?search_query=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iiioOO0OO0O = II11 . lower ( )
 oO0OOoo0OO = IIII ( I1iiioOO0OO0O )
 OOooOoooOoOo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII in next :
  o0OIiII = 'https://www.youtube.com' + o0OIiII
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , o0OIiII , 10065 , III1iII1I1ii + 'Next.png' , Ooo , '' )
 for o00O0O , o0OIiII , I1111i , I1iI1I1 , oo0o0O0Oooooo in OOooOoooOoOo :
  I1IIIii . append ( I1111i )
  O0oO0 ( 'tvshows' , 'INFO' )
  OoO = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OoO
  o0OIiII = 'http://www.youtube.com' + o0OIiII
  I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , OoO , oo0o0O0Oooooo )
 else :
  OOooOoooOoOo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , o0OIiII , I1111i , I1iI1I1 in OOooOoooOoOo :
   print 'im doing it'
   O0oO0 ( 'tvshows' , 'INFO' )
   OoO = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   o0OIiII = 'http://www.youtube.com' + o0OIiII
   if '&' in o0OIiII :
    print ' i got here'
    oO0OOoo0OO = IIII ( o0OIiII )
    O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for O00oO0 in O00oO0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     o0OIiII = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
     for o0OIiII in o0OIiII :
      o0OIiII = 'https://www.youtube.com/w' + o0OIiII
     OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for OoO in OoO :
      OoO = 'http:' + OoO
     I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , Ooo , '' )
   elif I1111i in I1IIIii :
    pass
   elif 'user' in o0OIiII or 'elete' in I1111i :
    pass
   elif 'hannel' in o0OIiII :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + o0OIiII
    oO0OOoo0OO = IIII ( o0OIiII )
    IiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , o0OIiII , I1111i in IiIi1 :
     if 'outube' in o0OIiII or 'list' in o0OIiII :
      pass
     elif 'atch' in o0OIiII :
      o0OIiII = ( o0OIiII ) . replace ( '/watch?v=' , '' )
      I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , OoO , '' )
    if 53 - 53: ii - O0OOOoOoo0
def oOo ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , Ooo , '' )
 for o00O0O , url , I1111i , I1iI1I1 , oo0o0O0Oooooo in OOooOoooOoOo :
  I1IIIii . append ( I1111i )
  O0oO0 ( 'tvshows' , 'INFO' )
  OoO = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OoO
  url = 'http://www.youtube.com' + url
  I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , OoO , oo0o0O0Oooooo )
 else :
  OOooOoooOoOo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , url , I1111i , I1iI1I1 in OOooOoooOoOo :
   O0oO0 ( 'tvshows' , 'INFO' )
   OoO = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = IIII ( url )
    O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for O00oO0 in O00oO0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for OoO in OoO :
      OoO = 'http:' + OoO
     I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , Ooo , '' )
   elif I1111i in I1IIIii :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = IIII ( url )
    IiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , url , I1111i in IiIi1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    I1I1i1I ( '[COLORred]' + I1iI1I1 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO , OoO , '' )
    if 17 - 17: ooOOOoO . Ii
    if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . I1111IIi - iiiiiiii1
def iiOO0O0Ooo ( ) :
 if II11iiii1Ii == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  o00oo0000 = open ( OOOOi11i1 )
  OOooOoooOoOo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o00oo0000 ) )
  for iIi1IIi1ii , I11Ii in OOooOoooOoOo :
   if iIi1IIi1ii == 'needs replacing' or I11Ii == 'needs replacing' :
    iIiII ( )
    if 19 - 19: O0OOOoOoo0
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
  if 78 - 78: o000O0o % I11i
def IIIiIiI ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
 iIiII ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 7 - 7: O0OOOoOoo0 . OOooOOo / Ii1I . o000O0o * Ii1IIIi1 - IIiIiII11i
def I1ii1iI1II11ii ( ) :
 Iii1I1I11iiI1 ( 'Full List' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'PPV' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Entertainment' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Factual' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Movie Channels' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'US Movie Channels TEST' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Kids' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Music' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'UK Sports' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'International Sports' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'News UK & International' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'German' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'Arabic' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'TV Series Latest' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'VOD Latest' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( 'VOD Bollywood' , '' , 60003 , III1iII1I1ii + 'GTV.png' , Ooo , '' )
 if 8 - 8: iiiiiiii1 * o0o00Oo0O
def OOoOIiIIII ( name ) :
 oOOo = name
 oO0OOoo0OO = IIII ( 'http://piesustv.net:8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , oo0oO0 , o0OIiII in OOooOoooOoOo :
  if oOOo == 'Full List' :
   o0OIiII = ( o0OIiII ) . replace ( '.ts' , '.m3u8' )
   I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OIiII ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
  else :
   oOOo = ( oOOo ) . replace ( 'World' , 'القنوات العربية' )
   if oOOo in oo0oO0 :
    o0OIiII = ( o0OIiII ) . replace ( '.ts' , '.m3u8' )
    print o0OIiII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OIiII ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
   else :
    pass
    if 44 - 44: Ii1I - ooOOOoO / IIiIiII11i * oO0o * I1ii11iIi11i
def OO0ooo0o0 ( name ) :
 oOOo = name
 oO0OOoo0OO = IIII ( 'http://piesustv.net:8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , o0OIiII in OOooOoooOoOo :
  o0OIiII = ( o0OIiII ) . replace ( '.ts' , '.m3u8' )
  I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( o0OIiII ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
 else :
  I1I1i1I ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 69 - 69: Ii1I - I1111IIi
  if 16 - 16: I1ii11iIi11i
  if 14 - 14: ooOoO0O00 - o0o00Oo0O % I1ii11iIi11i
  if 92 - 92: ooOOOoO % ii1ii11IIIiiI / Ii1I % Ii1I * oOo0O0Ooo
  if 74 - 74: o0o00Oo0O . oOo0O0Ooo % oO0o % O0OOOoOoo0
  if 87 - 87: Ooo00oOo0oOo - Ii
  if 78 - 78: Ii / iI11I1II1I1I - I11i
  if 23 - 23: Ii1IIIi1
  if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
  if 14 - 14: Ii1I
  if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
  if 56 - 56: ii - Ii1IIIi1 - ooOoO0O00
def IiiiiI1i1Iii ( ) :
 Iii1I1I11iiI1 ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , Ooo , 'Back Up Your Full System' )
 if os . path . exists ( oO0 ) :
  Iii1I1I11iiI1 ( 'Backup Genie Favourites' , o0OIiII , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , Ooo , 'Back Up Your favourites' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  Iii1I1I11iiI1 ( 'Backup Ivue Config' , OOOO0OOoO0O0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , Ooo , 'Back Up Your master.db' )
 if os . path . exists ( O0Oo000ooO00 ) :
  Iii1I1I11iiI1 ( 'Backup Kodi Favourites' , O0Oo000ooO00 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , Ooo , 'Back Up Your favourites.xml' )
  if 8 - 8: I1111IIi / o000O0o . oOo0O0Ooo + Ii1I / Ii
  if 31 - 31: iiiiiiii1 - iI11I1II1I1I + ii1ii11IIIiiI . I1ii11iIi11i / O0OOOoOoo0 % iI11I1II1I1I
  if 6 - 6: O0OOOoOoo0 * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
zip = oo00 . getSetting ( 'zip' )
o0o0oOO = xbmc . translatePath ( os . path . join ( zip ) )
def i1IiI ( ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 1 - 1: O0OOOoOoo0 / O0OOOoOoo0 - Ii
  if 87 - 87: I1ii11iIi11i / o0o00Oo0O * O0OOOoOoo0 / I11i
  if 19 - 19: I1111IIi + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
def iIi1I1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oO0
  elif 'Ivue' in name :
   url = OOOO0OOoO0O0
  elif 'Kodi' in name :
   url = O0Oo000ooO00
  i1IiI ( )
  O0oOoo0OoO0O = open ( url ) . read ( )
  oo00IiI1 = os . path . join ( o0o0oOO , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( oo00IiI1 , mode = 'w' )
  oooOo0OOOoo0 . write ( O0oOoo0OoO0O )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   oOo00o00oO = open ( os . path . join ( o0o0oOO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0000 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   OOooOoooOoOo = re . compile ( o0000 ) . findall ( oOo00o00oO )
   for type , i111i1i , IiIii1I1I in OOooOoooOoOo :
    IiIii1I1I = IiIii1I1I . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , i111i1i , IiIii1I1I ) )
  else :
   oo00IiI1 = os . path . join ( url )
   O0oOoo0OoO0O = open ( os . path . join ( o0o0oOO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( oo00IiI1 , mode = 'w' )
   oooOo0OOOoo0 . write ( O0oOoo0OoO0O )
   oooOo0OOOoo0 . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 51 - 51: I1ii11iIi11i % OOooOOo * ii . Ii
 if 77 - 77: IIiIiII11i
 if 42 - 42: ooOOOoO * I1111IIi . O0OOOoOoo0 * oOo0O0Ooo + OOooOOo
 if 25 - 25: Ii1IIIi1 . oOo0O0Ooo + Ooo00oOo0oOo
def O00OO0o0 ( ) :
 oOOOooOo0O = 1
 i1IiI ( )
 III1i111i = xbmc . translatePath ( os . path . join ( o0o0oOO , 'Build Backup' , 'Full Backup' , '' ) )
 iI1i = xbmc . translatePath ( os . path . join ( o0o0oOO , 'Build Backup' , 'my_full_backup.zip' ) )
 i111iiIIII = xbmc . translatePath ( os . path . join ( o0o0oOO , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( III1i111i ) :
  os . makedirs ( III1i111i )
 OOO00OOo0o0Oo = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OOO00OOo0o0Oo ) : return False , 0
 ooooOoO0O = OOO00OOo0o0Oo
 IIIIIIII = xbmc . translatePath ( os . path . join ( III1i111i , ooooOoO0O + '.zip' ) )
 oOoOo0oOo0O0O0o = [ 'plugin.video.GenieTv' ]
 IiiIIiIIii1iI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Oo0O0O000 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 II1Ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OOoO00ooO = "Creating full backup of existing build"
 I1IIIIiii1i = "Creating Community Build"
 o0IiiiI111I = "Archiving..."
 III1I11i1iIi = ""
 OO0oo0O0OOO0 = "Please Wait"
 OoOOo ( I11 , IIIIIIII , I1IIIIiii1i , o0IiiiI111I , III1I11i1iIi , OO0oo0O0OOO0 , Oo0O0O000 , II1Ii )
 time . sleep ( 1 )
 Iii1 = xbmc . translatePath ( os . path . join ( III1i111i , ooooOoO0O + '_guisettings.zip' ) )
 OoOOo00 = zipfile . ZipFile ( Iii1 , mode = 'w' )
 try :
  OoOOo00 . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 OoOOo00 . close ( )
 if oOOOooOo0O == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iI1i , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IIIIIIII + '[/COLOR]' )
  if 53 - 53: O0OOOoOoo0 . I1111IIi % iI11I1II1I1I % OOooOOo % Ii1IIIi1
def OoOOo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0OoOoOOoOo0o = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIiiiIiIii1ii = len ( sourcefile )
 IIiI1i = [ ]
 iII1 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for O000O , Oo00OO0 , oo0O in os . walk ( sourcefile ) :
  for file in oo0O :
   iII1 . append ( file )
 oO00OoOOOo = len ( iII1 )
 for O000O , Oo00OO0 , oo0O in os . walk ( sourcefile ) :
  Oo00OO0 [ : ] = [ Oo0 for Oo0 in Oo00OO0 if Oo0 not in exclude_dirs ]
  oo0O [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in oo0O if oooOo0OOOoo0 not in exclude_files ]
  for file in oo0O :
   IIiI1i . append ( file )
   o0OOOOO0O = len ( IIiI1i ) / float ( oO00OoOOOo ) * 100
   o0oOoO00o . update ( int ( o0OOOOO0O ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1I1IiIi1 = os . path . join ( O000O , file )
   if not 'temp' in Oo00OO0 :
    if not 'plugin.program.originwizard' in Oo00OO0 :
     import time
     oOO0o0oo0 = '01/01/1980'
     oOo000O = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1I1IiIi1 ) ) )
     if oOo000O > oOO0o0oo0 :
      o0OoOoOOoOo0o . write ( I1I1IiIi1 , I1I1IiIi1 [ iIiiiIiIii1ii : ] )
 o0OoOoOOoOo0o . close ( )
 o0oOoO00o . close ( )
 if 1 - 1: iI11I1II1I1I
 if 54 - 54: ii - oOo0O0Ooo % Ii1I
def oOO ( ) :
 Oo0oO ( )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , Ooo , '' )
 if 92 - 92: oO0o * iiiiiiii1
 if 35 - 35: Ii
def ooOo0O00o0OoO ( ) :
 Oo0oO ( )
 OO = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , OO )
 if OoOoO == 0 :
  iiII1i11i ( )
 if OoOoO == 1 :
  I111i1i1111 ( )
 if OoOoO == 2 :
  O0OO0oOOo ( )
 if OoOoO == 3 :
  o0o0oOo000o0 ( )
  if 39 - 39: OOooOOo - I1ii11iIi11i / ii1ii11IIIiiI * ii
  if 100 - 100: o0o00Oo0O . Ii1IIIi1 . oO0o + o0o00Oo0O * Ooo00oOo0oOo
  if 42 - 42: Ooo00oOo0oOo % ii + I11i
  if 56 - 56: ii + Ii1I - ii1ii11IIIiiI
  if 24 - 24: I11i + iiiiiiii1 + Ii1IIIi1 - iI11I1II1I1I
  if 49 - 49: Ii1IIIi1 . iiiiiiii1 * OOooOOo % O0OOOoOoo0 . o0o00Oo0O
  if 48 - 48: o0o00Oo0O * ooOOOoO - o0o00Oo0O / ooOOOoO + OOooOOo
  if 52 - 52: oO0o % ooOOOoO * IIiIiII11i
  if 4 - 4: Ii1IIIi1 % o0o00Oo0O - ii + iiiiiiii1 . Ooo00oOo0oOo % IIiIiII11i
def Iiii1iiiIiI1 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , OO )
  if OoOoO == 0 :
   IiIII1 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , O0Oo000 , I1111i )
  if OoOoO == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if OoOoO == 2 :
   I11Iii1 ( )
  if OoOoO == 3 :
   i1iIIi1II1iiI ( )
  if OoOoO == 4 :
   III1Ii1i1I1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if OoOoO == 5 :
   O0O00OooO ( )
  if OoOoO == 6 :
   I1IiI1iI11 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if OoOoO == 7 :
   iIi ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if OoOoO == 8 :
   iiO0O0o0oO0O00 ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if OoOoO == 9 :
   o0O0oO0 ( )
  if OoOoO == 10 :
   oo0i1 ( )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , III1iII1I1ii + 'Quicksilver.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , Ooo , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 1030 , III1iII1I1ii + 'MUSIC.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , Ooo , '' )
  if 27 - 27: I1111IIi + ii - OOooOOo
 O0oO0 ( 'movies' , 'MAIN' )
 if 15 - 15: Ooo00oOo0oOo / Ii1IIIi1 * o0o00Oo0O . IIiIiII11i - oO0o
def o0Oo00OO0 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OO = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , OO )
  if OoOoO == 0 :
   i11Ii11II1I1 ( )
  if OoOoO == 1 :
   ooO000OO0O00O ( )
  if OoOoO == 2 :
   O0O0ooOOO ( )
  if OoOoO == 3 :
   I1IiiiiI ( o0OIiII )
  if OoOoO == 4 :
   IiI1iI1IiiIi1 ( o0OIiII )
  if OoOoO == 5 :
   I1iIIiiIIi1i ( )
  if OoOoO == 6 :
   OoO0oo ( url = 'http://www.iplocation.net/' , inc = 1 )
  if OoOoO == 7 :
   OoOoO0O ( )
 else :
  I1I1i1I ( 'CLLEANUP' , 'url' , 9666 , III1iII1I1ii + 'MAIN5.png' , Ooo , '' )
  I1I1i1I ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , Ooo , '' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , Ooo , '' )
  I1I1i1I ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , Ooo , '' )
  I1I1i1I ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , Ooo , '' )
  I1I1i1I ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , Ooo , '' )
  I1I1i1I ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , Ooo , 'Force Refresh All Repos' )
  Iii1I1I11iiI1 ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , III1iII1I1ii + '1.jpg' , Ooo , 'Fix Corrupt Database' )
  I1I1i1I ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , Ooo , '' )
  I1I1i1I ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Ooo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 100 - 100: o0o00Oo0O
  if 79 - 79: iI11I1II1I1I
 O0oO0 ( 'movies' , 'MAIN' )
 if 81 - 81: o000O0o + iI11I1II1I1I * I1111IIi - iI11I1II1I1I . o000O0o
 if 48 - 48: Ii1IIIi1 . ii . oOo0O0Ooo . OOooOOo % Ii1I / ii1ii11IIIiiI
def i1i1II ( ) :
 Oo0oO ( )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , III1iII1I1ii + 'repos.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NEW[/COLOR]' , str ( I1I1IiI1 ) , 22 , III1iII1I1ii + 'NEW.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']IPTV[/COLOR]' , str ( I1I1IiI1 ) , 23 , III1iII1I1ii + 'IPTV.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']VIDEO[/COLOR]' , str ( I1I1IiI1 ) , 24 , III1iII1I1ii + 'VIDEO.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']SPORTS[/COLOR]' , str ( I1I1IiI1 ) , 25 , III1iII1I1ii + 'SPORTS.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 26 , III1iII1I1ii + 'KIDS.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 27 , III1iII1I1ii + 'MUSIC.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']PROGRAMS[/COLOR]' , str ( I1I1IiI1 ) , 28 , III1iII1I1ii + 'PROGRAMS.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']XXX[/COLOR]' , 'URL' , 29 , III1iII1I1ii + 'XXX.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 11 - 11: ooOoO0O00 % oO0o % ii1ii11IIIiiI
 if 99 - 99: iiiiiiii1 / iI11I1II1I1I - ooOOOoO * Ii1I % oOo0O0Ooo
def i1II1i ( ) :
 Oo0oO ( )
 I1I1i1I ( 'CHECK ADVANCED XML' , str ( I1I1IiI1 ) , 8 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'MUCKYS XML' , str ( I1I1IiI1 ) + '/wizard/muckys.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( '0CACHE XML' , str ( I1I1IiI1 ) + '/wizard/0cache.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'MIKEY1234 XML' , str ( I1I1IiI1 ) + '/wizard/mikey.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'TUXENS XML' , str ( I1I1IiI1 ) + '/wizard/tuxens.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'P2P RECOMMENDED XML1' , str ( I1I1IiI1 ) + '/wizard/p2p1.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'P2P RECOMMENDED XML2' , str ( I1I1IiI1 ) + '/wizard/p2p2.xml' , 7 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 I1I1i1I ( 'DELETE XML' , str ( I1I1IiI1 ) , 11 , III1iII1I1ii + 'XML.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 10 - 10: ooOOOoO - OOooOOo . ii . o000O0o . oO0o * ii1ii11IIIiiI
def oo00oO0o ( ) :
 Oo0oO ( )
 I1I1i1I ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , Ooo , '' )
 I1I1i1I ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , III1iII1I1ii + 'MyOnlineZip.png' , Ooo , '' )
 if 78 - 78: Ooo00oOo0oOo / oO0o - Ooo00oOo0oOo * ii . OOooOOo
def OOoooOoO0Oo ( ) :
 Oo0oO ( )
 I1I1i1I ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , Ooo , '' )
 I1I1i1I ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , Ooo , '' )
 I1I1i1I ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , Ooo , '' )
 I1I1i1I ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , Ooo , '' )
 if 78 - 78: ii / o000O0o % OOooOOo * ii
 if 68 - 68: Ooo00oOo0oOo
 if 29 - 29: ii1ii11IIIiiI + Ii % Ii1IIIi1
def O0O0OOOOoo ( ) :
 Oo0oO ( )
 OO = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OO )
 if OoOoO == 0 :
  oOo00Ooo0o0 ( )
 if OoOoO == 0 :
  i1IiII1i1I ( o0OIiII )
 if OoOoO == 0 :
  iI1ii1ii1I ( o0OIiII )
  if 18 - 18: Ooo00oOo0oOo * Ooo00oOo0oOo % Ooo00oOo0oOo
  if 17 - 17: o0o00Oo0O * OOooOOo * Ii1I * IIiIiII11i * Ii1IIIi1 % ooOoO0O00
  if 33 - 33: Ii1I * Ii1I . iiiiiiii1 . Ii
 O0oO0 ( 'movies' , 'MAIN' )
 if 48 - 48: I11i . ooOOOoO + OOooOOo % Ii1I / Ii
def OoOi111i ( ) :
 O00O0oOO00O00 = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 OOooOoooOoOo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O00O0oOO00O00 )
 for o00O0O , I1111i in OOooOoooOoOo :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 O0oO0 ( 'tvshows' , 'INFO' )
 if 46 - 46: oO0o * I1ii11iIi11i % Ooo00oOo0oOo + o0o00Oo0O * O0OOOoOoo0
def ii1I11i ( url ) :
 O00O0oOO00O00 = IIII ( O0OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 5 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 37 - 37: o0o00Oo0O - Ii1IIIi1
def oOo00Ooo0o0 ( ) :
 Oo0oO ( )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , Ooo , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 21 - 21: iI11I1II1I1I / I1111IIi + iiiiiiii1 - Ii1IIIi1 / I1ii11iIi11i / IIiIiII11i
def oOI11 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + o0000o0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 90 - 90: iI11I1II1I1I * IIiIiII11i
def oOOo0OoOOOoo ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + oOOOOoO00Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 18 - 18: iiiiiiii1 + ooOOOoO
def ii11i11 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + OooiiIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 35 - 35: ii - I1111IIi / oO0o
def iii11i1 ( url ) :
 O00O0oOO00O00 = IIII ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 48 - 48: iiiiiiii1 * Ii1I
def i1IiII1i1I ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + II111iIiI1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 40 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
def oooO00Oo ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + ooO00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 5 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 73 - 73: ii1ii11IIIiiI * ii1ii11IIIiiI / iiiiiiii1
def Ii1I1i ( ) :
 OO = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , OO )
 if OoOoO == 0 :
  IIii1i11iI1II11 ( )
 if OoOoO == 1 :
  iIi11i ( )
 if OoOoO == 2 :
  ooIII1II1iii1i ( )
  if 75 - 75: O0OOOoOoo0 - OOooOOo - iI11I1II1I1I % I11i
  if 58 - 58: o0o00Oo0O . O0OOOoOoo0 / ii . oO0o / I1ii11iIi11i * IIiIiII11i
  if 53 - 53: ooOOOoO - o0o00Oo0O / I11i % ii1ii11IIIiiI * oOo0O0Ooo % o000O0o
  if 69 - 69: Ii1I
def iIi11i ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for o0OIiII , oOOO0ooo in OOooOoooOoOo :
  oO0oo ( 'Android Apps' + oOOO0ooo , 'https://www.apkfiles.com' + o0OIiII , 30035 , III1iII1I1ii + 'apps.png' )
 for o0OIiII , oOOO0ooo in o0OOOO00O0Oo :
  oO0oo ( 'Android Games' + oOOO0ooo , 'https://www.apkfiles.com' + o0OIiII , 30035 , III1iII1I1ii + 'GAMES.png' )
 O0oO0 ( 'movies' , 'MAIN' )
def I1III1iIi ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if '/cat' in url :
   oO0oo ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def OoO00O0 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if '/app' in url :
   oO0oo ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , III1iII1I1ii + 'APK.png' )
def I1Iii ( url ) :
 iIIII = IIII ( url )
 i1i11ii1Ii = url
 if "page=" in str ( url ) :
  i1i11ii1Ii = url . split ( '?' ) [ 0 ]
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  if 'apk' in url :
   I1I1i1I ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( o0OOOO00O0Oo ) > 1 :
  o0OOOO00O0Oo = str ( o0OOOO00O0Oo [ len ( o0OOOO00O0Oo ) - 1 ] )
 I1I1i1I ( 'Next Page' , i1i11ii1Ii + str ( o0OOOO00O0Oo ) , 30037 , III1iII1I1ii + 'Next.png' )
def i1Oo0oOo000OoO0 ( name , url ) :
 iIIII = O0iIiIIIIIii ( url )
 name = name
 OOooOoooOoOo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  url = 'https://www.apkfiles.com' + url
  IIii1I1i ( name , url , 'Brackets' )
def ooIII1II1iii1i ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'https://www.apkfiles.com/search?q=' + ( I1i11II ) . replace ( ' ' , '+' ) + '&search_type=1'
 I1iiioOO0OO0O = II11 . lower ( )
 I1Iii ( I1iiioOO0OO0O )
 if 22 - 22: I1ii11iIi11i % oO0o - ii * I1ii11iIi11i
def ii1i ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( i1IiiiiIi1I , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , I1111i + '.apk' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 56 - 56: ii * o0o00Oo0O
def oo0OoOOooO ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , I1111i + '.mp4' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 60 - 60: I1111IIi
 if 98 - 98: iiiiiiii1
def Ii11i1Ii1IIII ( name , url , description ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 i1iiI = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1iiI
 print '======================================='
 extract . all ( o00O0 , i1iiI , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 63 - 63: o0o00Oo0O
 if 6 - 6: o000O0o
 if 98 - 98: ii % o0o00Oo0O - o0o00Oo0O
 if 76 - 76: ooOoO0O00 % OOooOOo - oOo0O0Ooo / I11i * iiiiiiii1
 if 4 - 4: I1ii11iIi11i * I1ii11iIi11i / OOooOOo
def IIii1i11iI1II11 ( ) :
 O00O0oOO00O00 = IIII ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOooOoooOoOo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , o0OIiII , OOOoOO0o , i1II1 , Ii1Ii1Ii1I1I in OOooOoooOoOo :
  I1I1i1I ( I1111i , o0OIiII , 80003 , OOOoOO0o , III1iII1I1ii + 'APKToolsB.png' , Ii1Ii1Ii1I1I )
def III1II1i ( apk , ret = None ) :
 if apk == "kodi" :
  iI1i1IiIIIIi = "https://kodi.tv/download/"
  O00O0oOO00O00 = IIII ( iI1i1IiIIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OOooOoooOoOo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O00O0oOO00O00 )
  if len ( OOooOoooOoOo ) == 1 :
   OooOooO0O0o0 = OOooOoooOoOo [ 0 ] [ 0 ]
   ooooOoO0O = OOooOoooOoOo [ 0 ] [ 1 ]
   OOO0o0 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( OooOooO0O0o0 , ooooOoO0O )
  if ret == 'version' : return OooOooO0O0o0
  else : return OOO0o0
 elif apk == "spmc" :
  IIIIII111Ii = 'https://github.com/koying/SPMC/releases/latest/'
  O00O0oOO00O00 = IIII ( IIIIII111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OOooOoooOoOo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O00O0oOO00O00 )
  OooOooO0O0o0 = re . sub ( '<[^<]+?>' , '' , OOooOoooOoOo [ 0 ] ) . replace ( ' ' , '' )
  OOO0o0 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( OooOooO0O0o0 , OooOooO0O0o0 )
  if ret == 'version' : return OooOooO0O0o0
  else : return OOO0o0
def IIii1I1i ( name , url ) :
 if ii1I ( ) == 'android' :
  Ii1i1i = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ii1i1i : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  ooo00Oo00O0 = name
  if Ii1i1i :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not iiIiIIIiiI ( url ) == True : iIi1Ii1IIiI ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % ooo00Oo00O0 , '' , 'Please Wait' )
   o00O0 = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( o00O0 )
   except : pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    OoOOo00 = zipfile . ZipFile ( o00O0 )
    for file in OoOOo00 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       OOOOOOoo0oO = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( OoOOo00 . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( o00O0 )
       except :
        pass
       o00O0 = os . path . join ( oooOOOOO , OOOOOOoo0oO )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o00O0 + '")' )
  else : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 32 - 32: ooOoO0O00 . ii1ii11IIIiiI + IIiIiII11i - oO0o - iI11I1II1I1I
 if 20 - 20: OOooOOo % Ii1I
 if 44 - 44: ii . IIiIiII11i . o000O0o % ii
 if 86 - 86: Ii + o0o00Oo0O * O0OOOoOoo0 - oO0o * o000O0o + o0o00Oo0O
def Oo0O00o0oo0oOO ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O00O0oOO00O00 = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O00O0oOO00O00 )
 for o0OIiII , I1111i in OOooOoooOoOo :
  o0OIiII = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + o0OIiII )
  ooo0OoO ( ( I1111i ) . replace ( '_' , ' ' ) , o0OIiII )
  if 50 - 50: oOo0O0Ooo * o000O0o + iiiiiiii1
def ooo0OoO ( name , url ) :
 if ii1I ( ) == 'android' :
  Ii1i1i = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ii1i1i : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  ooo00Oo00O0 = name
  if Ii1i1i :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not iiIiIIIiiI ( url ) == True : iIi1Ii1IIiI ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % ooo00Oo00O0 , '' , 'Please Wait' )
   o00O0 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( o00O0 )
   except : pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o00O0 + '")' )
  else : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIi1Ii1IIiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 88 - 88: Ii1IIIi1 + Ii % Ooo00oOo0oOo * o000O0o * o000O0o * ooOOOoO
 if 24 - 24: iiiiiiii1 / ii1ii11IIIiiI + O0OOOoOoo0 . O0OOOoOoo0
def I1ii1i ( url ) :
 O00O0oOO00O00 = IIII ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 5 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'INFO' )
 if 22 - 22: Ooo00oOo0oOo * ooOOOoO * Ii + ii1ii11IIIiiI * OOooOOo * oO0o
 if 85 - 85: ii1ii11IIIiiI * o000O0o % I1ii11iIi11i - ii1ii11IIIiiI - Ii1IIIi1
def OOoooO00o0oo0 ( url ) :
 O00O0oOO00O00 = IIII ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 30015 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 46 - 46: o0o00Oo0O
def OoOOoooO000 ( url , iconimage , fanart ) :
 O00O0oOO00O00 = IIII ( url )
 i11ii1Ii1 = url
 o00O0O = iconimage
 fanart = fanart
 OOooOoooOoOo = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( O00O0oOO00O00 )
 for ii11I1 , I1111i in OOooOoooOoOo :
  if '.mp4' in I1111i :
   I1I1i1I ( 'Watch VIDEO' , url + '/' + ii11I1 , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   I1I1i1I ( 'Read Description' , url + '/' + ii11I1 , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   Iii1I1I11iiI1 ( 'View Images' , url + '/' + ii11I1 , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   I1I1i1I ( 'Install Build On Android' , url + '/' + ii11I1 , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   I1I1i1I ( 'Install Build On Pc' , url + '/' + ii11I1 , 30019 , o00O0O , fanart , '' )
 O0oO0 ( 'movies' , 'INFO' )
 if 85 - 85: oOo0O0Ooo % Ii1IIIi1 + o000O0o / ooOOOoO % ii
def i11i11II11i1 ( url ) :
 O00O0oOO00O00 = IIII ( url )
 OOooOoooOoOo = re . compile ( 'url="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for url in OOooOoooOoOo :
  iiiI1i1 ( url )
  if 44 - 44: o000O0o + Ii1IIIi1 . O0OOOoOoo0 / IIiIiII11i % iI11I1II1I1I + O0OOOoOoo0
def O0OOoi1I1Iiii1 ( url ) :
 O00O0oOO00O00 = IIII ( url )
 OOooOoooOoOo = re . compile ( 'url="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for url in OOooOoooOoOo :
  O0ooooo000 ( url )
  if 97 - 97: Ii % Ooo00oOo0oOo / I1ii11iIi11i / I1ii11iIi11i
def OoO00ooO ( url ) :
 O00O0oOO00O00 = IIII ( url )
 OOooOoooOoOo = re . compile ( 'desc="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for iiO0o0O0oo0o in OOooOoooOoOo :
  OO0O000 ( 'Description:' , iiO0o0O0oo0o )
  if 100 - 100: O0OOOoOoo0 . ooOOOoO - iI11I1II1I1I . Ii / IIiIiII11i
def o0oO0OO00oo0o ( url ) :
 O00O0oOO00O00 = IIII ( url )
 url = url
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O00O0oOO00O00 )
 for ii11I1 , I1111i in OOooOoooOoOo :
  if 'png' in I1111i :
   I1I1i1I ( 'image' , '' , '' , url + '/' + ii11I1 , url + '/' + ii11I1 , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 17 - 17: O0OOOoOoo0 / Ii1I - I11i * Ii1I
def i11i11II11i ( name , url , description ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
 if 9 - 9: OOooOOo - Ii1I * iiiiiiii1 . iiiiiiii1 - oOo0O0Ooo
 if 74 - 74: Ii1I * Ii / oOo0O0Ooo - o0o00Oo0O . iiiiiiii1
def O0ooooo000 ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i11Ii11II1I1 ( )
 if 39 - 39: iiiiiiii1 / o0o00Oo0O * O0OOOoOoo0
def iiiI1i1 ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i11Ii11II1I1 ( )
 if 17 - 17: ooOOOoO / iI11I1II1I1I - oO0o + oOo0O0Ooo % o000O0o
def III1III11II ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o00O0 = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i11Ii11II1I1 ( )
 if 43 - 43: oOo0O0Ooo
def ii1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def oOOo0O00o ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo0o0O00 , log ) )
 if not os . path . exists ( oOo0oooo00o ) : os . makedirs ( oOo0oooo00o )
 if not os . path . exists ( oO0o0o0ooO0oO ) : oooOo0OOOoo0 = open ( oO0o0o0ooO0oO , 'w' ) ; oooOo0OOOoo0 . close ( )
 with open ( oO0o0o0ooO0oO , 'a' ) as oooOo0OOOoo0 :
  iiIIIiI1Ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( iiIIIiI1Ii . rstrip ( '\r\n' ) + '\n' )
def i11Ii11II1I1 ( ) :
 OoOoO = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OoOoO == 0 : return
 elif OoOoO == 1 : pass
 IIiiiiiIiIIi = ii1I ( )
 oOOo0O00o ( "Platform: " + str ( IIiiiiiIiIIi ) )
 os . _exit ( 1 )
 oOOo0O00o ( "Force close failed!  Trying alternate methods." )
 if IIiiiiiIiIIi == 'osx' :
  oOOo0O00o ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IIiiiiiIiIIi == 'linux' :
  oOOo0O00o ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IIiiiiiIiIIi == 'android' :
  oOOo0O00o ( "############ try android force close #################" )
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
  iI111I11I1I1 . ok ( oo0o0O00 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif IIiiiiiIiIIi == 'windows' :
  oOOo0O00o ( "############ try windows force close #################" )
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
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  oOOo0O00o ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oOOo0O00o ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 26 - 26: I11i
  if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
  if 46 - 46: IIiIiII11i - O0OOOoOoo0 * ii / Ooo00oOo0oOo % O0OOOoOoo0
def iI1ii1ii1I ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( url ) :
  for file in oo0O :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oOo00o00oO = open ( ( os . path . join ( Iii11III1I11 , file ) ) ) . read ( )
    iii = oOo00o00oO . replace ( I11 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( Iii11III1I11 , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( iii ) )
    oooOo0OOOoo0 . close ( )
 i11Ii11II1I1 ( )
 if 2 - 2: ooOoO0O00 * Ooo00oOo0oOo - Ooo00oOo0oOo + ii % OOooOOo / OOooOOo
def I11Iii1 ( ) :
 oO0oo ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 oO0oo ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 oO0oo ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 3 - 3: ii
def O0OoO0o ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def I111IIiIII ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def OO0OOoo0OOO ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in o0OOOO00O0Oo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def ooooOoo0OO ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
def Oo0O0000Oo00o ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II
 II1ii = 'https://www.radionomy.com/en/search/index?query=' + ( I1i11II ) . replace ( ' ' , '+' )
 oO0OOoo0OO = IIII ( II1ii )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + o0OIiII , 70005 , o00O0O )
  if 89 - 89: ii1ii11IIIiiI . Ii * o0o00Oo0O
  if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + O0OOOoOoo0
def O0O00OooO ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , 'http://www.listenlive.eu/' + o0OIiII , 10111113 , III1iII1I1ii + 'radio.png' )
def III1Ii1i1I1 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , url , 222 , III1iII1I1ii + 'radio.png' )
  if 27 - 27: o000O0o
def O0OO0ooO00 ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + o0OIiII , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0oOO0o ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( iIIII )
 for url , o00O0O in OOooOoooOoOo :
  if 'ol.gif' in o00O0O :
   pass
  elif 'link_block_' in o00O0O :
   pass
  elif '.png' in o00O0O :
   pass
  else :
   oO0oo ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in o0OOOO00O0Oo :
  oO0oo ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0OI1II ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 9 - 9: I1ii11iIi11i % ii - ooOOOoO
  if 43 - 43: oO0o % oO0o
def oo0i1 ( ) :
 IIiii11ii1i ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 IIiii11ii1i ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 7 - 7: Ooo00oOo0oOo - o0o00Oo0O * Ii1IIIi1 - I11i - IIiIiII11i
def Ii11iiI1 ( ) :
 IIiii11ii1i ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 71 - 71: I11i / o000O0o % o000O0o
def OoooO0 ( ) :
 oO0OOoo0OO = IIII ( IIiiiiiiIi1I1 + 'books' + ooooooO0oo )
 OOooOoooOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , o0OIiII , oooOO0oo0Oo00 in OOooOoooOoOo :
  if 'Parent' in I1111i :
   pass
  elif '2' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 99 - 99: o0o00Oo0O
def IiIii1 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 oO0OOoo0OO = IIII ( IIiiiiiiIi1I1 + 'books' + ooooooO0oo )
 OOooOoooOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , o0OIiII , oooOO0oo0Oo00 in OOooOoooOoOo :
  if I1i11II in I1111i . lower ( ) :
   if '1' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 46 - 46: iiiiiiii1 % O0OOOoOoo0 - I11i - I1ii11iIi11i - ooOOOoO / Ii1IIIi1
    if 68 - 68: ooOoO0O00 - Ii1I / I1ii11iIi11i % Ii1IIIi1 . ii1ii11IIIiiI
def iIIIIIIIiIII ( ) :
 oO0OOoo0OO = IIII ( IIiiiiiiIi1I1 + 'books' + ooooooO0oo )
 OOooOoooOoOo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , o0OIiII , oooOO0oo0Oo00 in OOooOoooOoOo :
  if '1' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o0OIiII , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: ii1ii11IIIiiI * iI11I1II1I1I . Ii1IIIi1
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iI11I1II1I1I * OOooOOo / I1111IIi % iiiiiiii1 + Ooo00oOo0oOo
def iiiI1iI1 ( url ) :
 ii11I1 = url
 oO0OOoo0OO = IIII ( url )
 o0OOOO00O0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in o0OOOO00O0Oo :
  if 'mp3' in I1111i :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii11I1 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii11I1 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii11I1 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii11I1 + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 15 - 15: O0OOOoOoo0 . ooOoO0O00 * OOooOOo % iI11I1II1I1I
   if 35 - 35: Ii1I + I1111IIi - OOooOOo % Ooo00oOo0oOo % I11i % OOooOOo
   if 45 - 45: oOo0O0Ooo * o000O0o % oO0o
def i111I11I ( url ) :
 oO0OOoo0OO = IIII ( url )
 ii11I1 = url
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  if 'Parent' in I1111i :
   pass
  elif '.db' in I1111i :
   pass
  elif '.jpg' in I1111i :
   pass
  elif '.html' in I1111i :
   pass
  elif '.doc' in I1111i :
   pass
  elif 'mp3' in I1111i :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii11I1 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii11I1 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii11I1 + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
   if 48 - 48: I1111IIi . Ii / ooOoO0O00 % O0OOOoOoo0 % ii1ii11IIIiiI + Ooo00oOo0oOo
def iiII1iiiiiii ( ) :
 IIiii11ii1i ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 9 - 9: ii + Ooo00oOo0oOo
def iIiI1ii ( ) :
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 OOooOoooOoOo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O in OOooOoooOoOo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + o0OIiII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   IIiii11ii1i ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( o0OIiII ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 76 - 76: ooOOOoO + iI11I1II1I1I + OOooOOo . oO0o
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: O0OOOoOoo0 / iiiiiiii1 / o000O0o
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - iiiiiiii1
def III1IiI1i1i ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: ii1ii11IIIiiI - I1ii11iIi11i + Ooo00oOo0oOo
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: Ii1IIIi1 . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
def oO0o0Oo ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OOooOoooOoOo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if I1i11II in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0OIiII , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0OIiII , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 76 - 76: iiiiiiii1 / OOooOOo + Ii1I
    if 2 - 2: Ii - I1111IIi + oO0o % Ii1IIIi1 * ooOOOoO
def Ooo000O00 ( ) :
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OOooOoooOoOo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0OIiII , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o0OIiII , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: o000O0o % Ii
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * Ooo00oOo0oOo . Ii1IIIi1 / ooOoO0O00
 if 50 - 50: I1111IIi / ooOoO0O00 % ii
def oOOOOO0Ooooo ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  ii11I1 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ii11I1 )
  if 57 - 57: ooOOOoO - ii
def OOoOO0O0o0 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in OOooOoooOoOo :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 44 - 44: o000O0o / I1ii11iIi11i + O0OOOoOoo0 % IIiIiII11i / oO0o + Ii
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: Ii1I
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
def OO0oO0o ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 OOooOoooOoOo = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'ongoing' in o0OIiII :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in o0OIiII :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in o0OIiII :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in o0OIiII :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in o0OIiII :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def OOoooOoO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 O0OOoooo0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in O0OOoooo0 :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def iIiIi1IiIi1iI ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo000oOo0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o00OO0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 oooOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in o00OO0 :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , I1111i in oo000oOo0 :
  I1I1i1I ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def oOoO0Oo0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  I1I1i1I ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 7 - 7: iiiiiiii1 + ooOOOoO
def O0000 ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 OOooOoooOoOo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if '9cart' in o0OIiII :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 32 - 32: iI11I1II1I1I % oOo0O0Ooo / Ii + o000O0o - I11i . ii1ii11IIIiiI
def oo00I1IiI1IIiI ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if '9cart' in url :
   oO0oo ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in o0OOOO00O0Oo :
  if '9cart' in url :
   oO0oo ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 79 - 79: ooOoO0O00
def iIi1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in o0OOOO00O0Oo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 96 - 96: ooOoO0O00 % ii
def ooiI1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if 'Watch' in url :
   oO0oo ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 3 - 3: O0OOOoOoo0 / Ii1IIIi1
def Ii11 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 3 - 3: ooOOOoO + I1111IIi . ooOoO0O00 / o000O0o % I1111IIi
def O0oo00oOOO0o ( url ) :
 url = cloudflare . source ( url )
 O0OoOOO00 ( url )
 if 5 - 5: I11i / oOo0O0Ooo % ooOOOoO . O0OOOoOoo0
def OooOOoO0OOOO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . recompile ( 'src="([^"]*)"' )
 for url in OOooOoooOoOo :
  O0OoOOO00 ( url )
  if 33 - 33: Ii1IIIi1 % IIiIiII11i + oO0o
  if 93 - 93: ooOoO0O00 . O0OOOoOoo0 / oOo0O0Ooo + O0OOOoOoo0
def III111i11IiI ( ) :
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , Ooo , '' )
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - ii1ii11IIIiiI . I11i
def O0OO0oOOo ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 65 - 65: o0o00Oo0O * Ii . ii / oOo0O0Ooo / ii1ii11IIIiiI
 OOooOoooOoOo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 69 - 69: iiiiiiii1 % iiiiiiii1
 for o0OIiII , I1111i in OOooOoooOoOo :
  if I1i11II in I1111i . lower ( ) :
   if 'Dad!' in I1111i :
    pass
   elif 'Family Guy' in I1111i :
    pass
   elif '2 Stupid' in I1111i :
    pass
   elif 'The Zelfs' in I1111i :
    pass
   elif 'A Clone' in I1111i :
    pass
   elif 'A.T.O.M' in I1111i :
    pass
   elif 'Almost Naked' in I1111i :
    pass
   elif 'Angry Kid' in I1111i :
    pass
   elif 'Annoying Orange' in I1111i :
    pass
   elif 'Aqua Teen' in I1111i :
    pass
   elif 'Assy Mcgee' in I1111i :
    pass
   elif 'Astroblast' in I1111i :
    pass
   elif 'Atomic Betty' in I1111i :
    pass
   elif 'Axe Cop' in I1111i :
    pass
   elif 'Baby Playpen' in I1111i :
    pass
   elif 'Beavis and Butt' in I1111i :
    pass
   elif 'Celebrity Deathmatch' in I1111i :
    pass
   elif 'Clerks The' in I1111i :
    pass
   elif 'Crapston Villas' in I1111i :
    pass
   elif 'Duckman:' in I1111i :
    pass
   elif 'Stripperella' in I1111i :
    pass
   elif 'Vixen' in I1111i :
    pass
   else :
    Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , Ooo , '' )
    if 76 - 76: Ii * ii1ii11IIIiiI / oO0o % Ii1I + o000O0o
    if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 79 - 79: OOooOOo % oOo0O0Ooo % ooOOOoO / ooOoO0O00 % oO0o
def ooO00O0O0 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if 'Dad!' in I1111i :
   pass
  elif 'Family Guy' in I1111i :
   pass
  elif '2 Stupid' in I1111i :
   pass
  elif 'The Zelfs' in I1111i :
   pass
  elif 'A Clone' in I1111i :
   pass
  elif 'A.T.O.M' in I1111i :
   pass
  elif 'Almost Naked' in I1111i :
   pass
  elif 'Angry Kid' in I1111i :
   pass
  elif 'Annoying Orange' in I1111i :
   pass
  elif 'Aqua Teen' in I1111i :
   pass
  elif 'Assy Mcgee' in I1111i :
   pass
  elif 'Astroblast' in I1111i :
   pass
  elif 'Atomic Betty' in I1111i :
   pass
  elif 'Axe Cop' in I1111i :
   pass
  elif 'Baby Playpen' in I1111i :
   pass
  elif 'Beavis and Butt' in I1111i :
   pass
  elif 'Celebrity Deathmatch' in I1111i :
   pass
  elif 'Clerks The' in I1111i :
   pass
  elif 'Crapston Villas' in I1111i :
   pass
  elif 'Duckman:' in I1111i :
   pass
  elif 'Stripperella' in I1111i :
   pass
  elif 'Vixen' in I1111i :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , Ooo , '' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: iI11I1II1I1I - Ii * ii1ii11IIIiiI
def o0O0Ooo ( url ) :
 iIIII = IIII ( url )
 o0OOOO00O0Oo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in o0OOOO00O0Oo :
  O0oO00oOOooO = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , Ooo , '' )
 OOooOoooOoOo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 10007 , O0oO00oOOooO )
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
  if 66 - 66: o0o00Oo0O
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: oO0o * ii
def Ii11iiI ( url , IMAGE ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  print I1111i + '     ' + url
  if 'easy' in url :
   o0OO0oooo ( url )
   if 40 - 40: I1111IIi - OOooOOo * Ii1IIIi1 - O0OOOoOoo0 / OOooOOo
   if 71 - 71: Ooo00oOo0oOo / ii % O0OOOoOoo0 / OOooOOo % I1111IIi
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 19 - 19: I1111IIi + O0OOOoOoo0 / Ooo00oOo0oOo / IIiIiII11i
def o0OO0oooo ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
  if 92 - 92: ooOoO0O00 % iiiiiiii1 + iiiiiiii1 - iI11I1II1I1I . ooOOOoO
  if 33 - 33: I11i / o0o00Oo0O + o000O0o
  if 75 - 75: O0OOOoOoo0 % Ii + iI11I1II1I1I
def OO0O0OOo0O ( ) :
 if 92 - 92: OOooOOo % o0o00Oo0O
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , Ooo , '' )
 if 55 - 55: iI11I1II1I1I * ii1ii11IIIiiI
def ooIi11iI ( ) :
 oO0OOoo0OO = IIII ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  if 'elete' in I1111i :
   pass
  else :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 222 , o00O0O )
   if 22 - 22: o000O0o
def I1I11Iiii111 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 oO0OOoo0OO = IIII ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iI1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , ii111iiIii , i1iII1IiiIiI1 in iI1 :
  for I1i11II in ii111iiIii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oO0oiIiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for o0OIiII , I1111i in oO0oiIiI :
    if 'tube' in o0OIiII :
     pass
    elif 'stage' in o0OIiII :
     Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + ii111iiIii + '   -   ' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in o0OIiII :
     pass
     if 46 - 46: ii1ii11IIIiiI
def ooIiI11i1I11111 ( ) :
 oO0OOoo0OO = IIII ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iI1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , ii111iiIii , i1iII1IiiIiI1 in iI1 :
  oO0oiIiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for o0OIiII , I1111i in oO0oiIiI :
   if 'tube' in o0OIiII :
    pass
   elif 'stage' in o0OIiII :
    Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + ii111iiIii + '   -   ' + I1111i + '[/COLOR]' , ( o0OIiII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in o0OIiII :
    pass
    if 34 - 34: oOo0O0Ooo * OOooOOo * Ooo00oOo0oOo + Ii1I
    if 39 - 39: Ii1I / ooOoO0O00 * O0OOOoOoo0 - oOo0O0Ooo
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: o0o00Oo0O - IIiIiII11i + ooOoO0O00 . I1111IIi . Ii1I
def oOo0oO ( url ) :
 oO0OOoo0OO = IIII ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi1IIIIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIi1IIIIi ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIi1IIIIi :
  OOOOo0o00OO0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 95 - 95: IIiIiII11i / ooOOOoO - iiiiiiii1 - IIiIiII11i - Ii
  if 85 - 85: I11i / I1111IIi
  if 67 - 67: Ii1IIIi1 % Ooo00oOo0oOo
  if 39 - 39: Ii + O0OOOoOoo0
  if 7 - 7: iI11I1II1I1I - ooOoO0O00
  if 10 - 10: I1111IIi % o0o00Oo0O / oOo0O0Ooo % Ii1IIIi1
  if 25 - 25: IIiIiII11i / oO0o
def II1iiiiII ( ) :
 if 64 - 64: o0o00Oo0O % iiiiiiii1
 iI1111i ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Ooo , '' )
 iI1111i ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Ooo , '' )
 if 39 - 39: I1111IIi % ii - IIiIiII11i % OOooOOo + Ooo00oOo0oOo + o0o00Oo0O
 O0oO0 ( 'movies' , 'MAIN' )
 if 14 - 14: ii . I11i . Ii1IIIi1
def I1IIIIIi1IIiI ( ) :
 iI1111i ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Ooo , '' )
 iI1111i ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Ooo , '' )
 if 26 - 26: I11i % o000O0o + o000O0o % Ii1IIIi1 * Ii / ii1ii11IIIiiI
 O0oO0 ( 'movies' , 'MAIN' )
def OOoO0oO00o ( ) :
 if 78 - 78: I1ii11iIi11i * I1111IIi - ii - oO0o
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 o0OOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 42 - 42: o0o00Oo0O % ooOOOoO - iI11I1II1I1I + I1111IIi % oOo0O0Ooo + iiiiiiii1
 for o0OoO0oo0O0o in o0OOo :
  ii1III1iiIi = o00OO00OoO + o0OoO0oo0O0o + ooooooO0oo
  oO0OOoo0OO = OOO00O ( ii1III1iiIi )
  OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , i1II1 , I1111i in OOooOoooOoOo :
   if I1i11II in I1111i . lower ( ) :
    I1ii1iI ( I1111i , o0OIiII , 222 , O0Oo000 , i1II1 , Iiiiii111i1ii )
    if 99 - 99: I11i
    O0oO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 1 - 1: ooOOOoO * OOooOOo * oO0o + I1ii11iIi11i
    if 90 - 90: I1111IIi % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / o000O0o + Ii1IIIi1
def o0o00OOOO ( ) :
 if 42 - 42: iiiiiiii1 * ii1ii11IIIiiI
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 o0OOo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 2 - 2: ii1ii11IIIiiI . oO0o / Ooo00oOo0oOo
 for o0OoO0oo0O0o in o0OOo :
  IIO000oooOO0Oo0 = o00OO00OoO + o0OoO0oo0O0o + ooooooO0oo
  oO0OOoo0OO = OOO00O ( IIO000oooOO0Oo0 )
  OOooOoooOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , Iiiiii111i1ii , o0OIiII , o00O0O , i1II1 , oo000ii in OOooOoooOoOo :
   if I1i11II in I1111i . lower ( ) :
    iI1111i ( I1111i , o0OIiII , oo000ii , o00O0O , i1II1 , Iiiiii111i1ii )
    if 31 - 31: O0OOOoOoo0 - oO0o / o000O0o . ooOoO0O00 / ooOOOoO
    O0oO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 66 - 66: oO0o
    if 72 - 72: I1111IIi
def OoO0 ( ) :
 if 13 - 13: I11i
 iIIII = IIII ( o00OO00OoO + 'spongemain.php' )
 OOooOoooOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Iiiiii111i1ii , o0OIiII , o00O0O , i1II1 , oo000ii in OOooOoooOoOo :
  iI1111i ( I1111i , o0OIiII , oo000ii , o00O0O , i1II1 , Iiiiii111i1ii )
  O0oO0 ( 'movies' , 'MAIN' )
def o000OOO00O ( url ) :
 if 65 - 65: ii1ii11IIIiiI * iI11I1II1I1I / o0o00Oo0O . Ii1IIIi1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OO0 = ( '%s%s' % ( OoOoO00OOoOOOo0 , url ) )
 O00O0oOO00O00 = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00O0oOO00O00 )
 for url , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in OOooOoooOoOo :
  oOoO00O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oOOoo0Oo ) )
  for i11I in oOoO00O :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I1ii1iI ( I1111i , url , 222 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
  if 31 - 31: iiiiiiii1 . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * ii1ii11IIIiiI
  O0oO0 ( 'movies' , 'MAIN' )
  if 22 - 22: Ii1IIIi1 % O0OOOoOoo0 . OOooOOo / iiiiiiii1 + o000O0o
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 85 - 85: oOo0O0Ooo - iiiiiiii1 % I1ii11iIi11i % IIiIiII11i - ii % O0OOOoOoo0
  if 40 - 40: ooOOOoO
def O0Ooo0ooo00o ( url ) :
 if 73 - 73: iiiiiiii1 % iiiiiiii1 . ii1ii11IIIiiI + I1111IIi
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Iiiiii111i1ii , url , o00O0O , i1II1 , oo000ii in OOooOoooOoOo :
  iI1111i ( I1111i , url , oo000ii , o00O0O , i1II1 , Iiiiii111i1ii )
  if 10 - 10: o0o00Oo0O / o000O0o * iiiiiiii1 - oO0o - ooOoO0O00 . OOooOOo
  O0oO0 ( 'movies' , 'MAIN' )
  if 69 - 69: I1ii11iIi11i - ooOOOoO % ooOOOoO - o000O0o * o000O0o / I1ii11iIi11i
  if 13 - 13: OOooOOo
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: Ii1I . IIiIiII11i - ooOOOoO % ii
def I1ii1iI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 49 - 49: Ii1I + o0o00Oo0O . ooOOOoO * ii
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  iioo0o0OoOOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = False )
 return i1ii
 if 82 - 82: Ii1I
def iI1111i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 54 - 54: I11i + Ii1IIIi1 - iI11I1II1I1I % iiiiiiii1 % O0OOOoOoo0
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  iioo0o0OoOOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = True )
 return i1ii
if 19 - 19: Ii1I / iI11I1II1I1I % ooOoO0O00 . ii
if 57 - 57: iiiiiiii1 . I1ii11iIi11i - oO0o - Ii * I1111IIi / I11i
if 79 - 79: Ii1I + I11i % I1ii11iIi11i * I11i
if 21 - 21: ii1ii11IIIiiI
if 24 - 24: ii1ii11IIIiiI / iiiiiiii1
if 61 - 61: iI11I1II1I1I + Ooo00oOo0oOo
if 8 - 8: I1111IIi + oO0o
if 9 - 9: o000O0o + I11i
if 8 - 8: o000O0o * I1ii11iIi11i / ii1ii11IIIiiI - oO0o - ii
if 100 - 100: Ooo00oOo0oOo . iI11I1II1I1I . iI11I1II1I1I
if 55 - 55: Ooo00oOo0oOo
if 37 - 37: O0OOOoOoo0 / Ii / I1ii11iIi11i
if 97 - 97: I1111IIi . Ii1IIIi1 / oOo0O0Ooo
if 83 - 83: Ii1IIIi1 - Ii1I * Ooo00oOo0oOo
if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
def OO0OooOo ( string ) :
 if Oo0OoO00oOO0o == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 13 - 13: o0o00Oo0O % iiiiiiii1 % Ii1IIIi1
def Ii11IiI111 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 IIiii11ii1II1 = [ ]
 try :
  if 97 - 97: Ii1IIIi1 - I11i + iiiiiiii1
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( O000oo0O ) == False :
  OO0OooOo ( 'Making Favorites File' )
  IIiii11ii1II1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oOo00o00oO = open ( O000oo0O , "w" )
  oOo00o00oO . write ( json . dumps ( IIiii11ii1II1 ) )
  oOo00o00oO . close ( )
 else :
  OO0OooOo ( 'Appending Favorites' )
  oOo00o00oO = open ( O000oo0O ) . read ( )
  OO0000 = json . loads ( oOo00o00oO )
  OO0000 . append ( ( name , url , iconimage , fanart , mode ) )
  iii = open ( O000oo0O , "w" )
  iii . write ( json . dumps ( OO0000 ) )
  iii . close ( )
  if 75 - 75: iiiiiiii1 % ii1ii11IIIiiI
  if 89 - 89: Ooo00oOo0oOo - o000O0o * I11i * ooOoO0O00
def I1IIIi1i ( ) :
 if os . path . exists ( O000oo0O ) == False :
  IIiii11ii1II1 = [ ]
  OO0OooOo ( 'Making Favorites File' )
  IIiii11ii1II1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oOo00o00oO = open ( O000oo0O , "w" )
  oOo00o00oO . write ( json . dumps ( IIiii11ii1II1 ) )
  oOo00o00oO . close ( )
 else :
  OooIii1I1iI = json . loads ( open ( O000oo0O ) . read ( ) )
  oOoOo0 = len ( OooIii1I1iI )
  for iIioOo in OooIii1I1iI :
   I1111i = iIioOo [ 0 ]
   o0OIiII = iIioOo [ 1 ]
   O0Oo000 = iIioOo [ 2 ]
   try :
    ooOo0o = iIioOo [ 3 ]
    if ooOo0o == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     ooOo0o = O0Oo000
    else :
     ooOo0o = i1II1
   try : III = iIioOo [ 5 ]
   except : III = None
   try : IiiI = iIioOo [ 6 ]
   except : IiiI = None
   if 75 - 75: ii . o000O0o + oO0o / ooOOOoO - oOo0O0Ooo % ooOOOoO
   if iIioOo [ 4 ] == 0 :
    Iii1I1I11iiI1 ( I1111i , o0OIiII , '' , O0Oo000 , i1II1 , '' , 'fav' )
   else :
    Iii1I1I11iiI1 ( I1111i , o0OIiII , iIioOo [ 4 ] , O0Oo000 , i1II1 , '' , 'fav' )
    if 89 - 89: ii1ii11IIIiiI * iI11I1II1I1I + Ii . ii
def O0O0 ( name ) :
 OO0000 = json . loads ( open ( O000oo0O ) . read ( ) )
 for oO0ooo00o0o000Oo in range ( len ( OO0000 ) ) :
  if OO0000 [ oO0ooo00o0o000Oo ] [ 0 ] == name :
   del OO0000 [ oO0ooo00o0o000Oo ]
   iii = open ( O000oo0O , "w" )
   iii . write ( json . dumps ( OO0000 ) )
   iii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 100 - 100: ooOoO0O00 - Ii . I1111IIi * oO0o
 if 62 - 62: o0o00Oo0O
def iIiII ( ) :
 iiIIIIiii = os . path . join ( O00o0OO , 'addons.ini' )
 iiii1 = open ( iiIIIIiii , "w+" )
 oO0OOoo0OO = IIII ( 'http://piesustv.net:8000/get.php?username=' + OooO0 + '&password=' + II11iiii1Ii + '&type=m3u_plus&output=mpegts' )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 iiii1 . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , oo0oO0 , o0OIiII in OOooOoooOoOo :
  o0OIiII = ( o0OIiII + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iii1IiiiI1i1 = ( I1111i + '=plugin://' + IiII + '/?url=' + o0OIiII + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iiii1 . write ( iii1IiiiI1i1 + '\n' )
  if 37 - 37: I1ii11iIi11i - ooOoO0O00 - O0OOOoOoo0 + Ii1IIIi1 . iI11I1II1I1I
  if 59 - 59: ii - I1111IIi % I11i . Ii1IIIi1 + ooOoO0O00 * Ii1IIIi1
def ii11111I ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 OOooOoooOoOo = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII in OOooOoooOoOo :
  oO0oo ( '24/7' , o0OIiII , 90021 , III1iII1I1ii + '247Streams.png' )
  if 72 - 72: oO0o . I11i * Ii1I . iI11I1II1I1I % Ii1I . ooOOOoO
def O000o0 ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  I1I1i1I ( I1111i , ( o0OIiII ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def i1iIIi1II1iiI ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  I1I1i1I ( I1111i , ( o0OIiII ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def O0OOo ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  I1I1i1I ( I1111i , ( o0OIiII ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def Iiiii1 ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  I1I1i1I ( I1111i , ( o0OIiII ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def O0Ooo0O ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 OOooOoooOoOo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  I1I1i1I ( I1111i , o0OIiII , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 18 - 18: ooOoO0O00
  if 4 - 4: O0OOOoOoo0
def oOo0OoOOOo0 ( ) :
 if 55 - 55: Ooo00oOo0oOo + o0o00Oo0O / ii1ii11IIIiiI % iiiiiiii1 / ii
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 if 98 - 98: ooOOOoO * iI11I1II1I1I % I1ii11iIi11i % o000O0o
def O0ooO00o ( ) :
 if 24 - 24: I1111IIi + ii . O0OOOoOoo0 / OOooOOo / Ii1IIIi1
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOooOoooOoOo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , o00O0O , I1111i , o0OO in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i + '  -  ' + ( o0OO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0OIiII , 10023 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
  if 65 - 65: ii
  if 18 - 18: o0o00Oo0O - ooOoO0O00 . I1111IIi
  if 98 - 98: I11i
def OOo00Oooo ( ) :
 if 15 - 15: iiiiiiii1 . iI11I1II1I1I * oOo0O0Ooo % Ii1IIIi1
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Action[/COLOR]' , 'Aksiyon' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Adventure[/COLOR]' , 'Macera' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Animation[/COLOR]' , 'Animasyon' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Anime[/COLOR]' , 'Anime' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Biography[/COLOR]' , 'Biyografi' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Comedy[/COLOR]' , 'Komedi' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Drama[/COLOR]' , 'Dram' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Family[/COLOR]' , 'Aile' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']History[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Horror[/COLOR]' , 'Korku' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Mystery[/COLOR]' , 'Gizem' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Romance[/COLOR]' , 'Romantik' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Sport[/COLOR]' , 'Spor' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Western[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
 if 21 - 21: oO0o - oOo0O0Ooo . ii
def Ii1iiI1i1 ( url ) :
 i11ii1Ii1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( i11ii1Ii1 )
 OOooOoooOoOo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , Ooo , '' )
  if 3 - 3: o000O0o . O0OOOoOoo0 / I1ii11iIi11i
  if 89 - 89: ii . iI11I1II1I1I . I1ii11iIi11i * iI11I1II1I1I - I1111IIi
  if 92 - 92: ii - Ii1I - ii % oOo0O0Ooo % oOo0O0Ooo % iI11I1II1I1I
  if 92 - 92: ii1ii11IIIiiI * o0o00Oo0O % I1111IIi . iI11I1II1I1I
def o00OoO ( ) :
 if 96 - 96: iiiiiiii1 . ii
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 o0OIiII = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1i11II ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( o0OIiII )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  if I1i11II in I1111i . lower ( ) :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 10022 , III1iII1I1ii + 'dtv.png' )
   if 39 - 39: o000O0o + oO0o
   if 80 - 80: o000O0o % oO0o / OOooOOo
   if 54 - 54: I1ii11iIi11i % oO0o - o000O0o - Ii1IIIi1
def o0I1iI111ii111i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii11I1 , i11IIIiI1I , o00iI1Ii11iIiiI1 , I1111i in OOooOoooOoOo :
  i11iII11ii = ( o00iI1Ii11iIiiI1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOo000O00O0 = ( i11IIIiI1I ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iI1iiIii1I11I = 'Season ' + oOo000O00O0 + 'Episode ' + i11iII11ii + I1111i
  Ii1IiiiI1ii ( iI1iiIii1I11I , ii11I1 )
  if 55 - 55: Ii1I
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: Ooo00oOo0oOo - Ii
  if 27 - 27: Ii1I - Ii % I1111IIi / I1ii11iIi11i . I1ii11iIi11i / ii
def Ii1IiiiI1ii ( name , url ) :
 ii11I1 = url
 O0oO0o0oOOO0o = name
 O0 = cloudflare . source ( ii11I1 )
 o0OOOO00O0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for IIi1IIIIi , ii111I1i1I1I in o0OOOO00O0Oo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + O0oO0o0oOOO0o + ii111I1i1I1I + '[/COLOR]' , IIi1IIIIi , 10012 , III1iII1I1ii + 'dtv.png' )
  if 94 - 94: oOo0O0Ooo % O0OOOoOoo0 + oO0o
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: ooOoO0O00 + o0o00Oo0O - Ooo00oOo0oOo . ii1ii11IIIiiI + iI11I1II1I1I
 if 88 - 88: ooOOOoO * o0o00Oo0O . I1111IIi / ii
def IIII1 ( ) :
 if 29 - 29: ii . IIiIiII11i % OOooOOo
 if 26 - 26: iI11I1II1I1I - Ii1I . O0OOOoOoo0 . O0OOOoOoo0 + iI11I1II1I1I * I1ii11iIi11i
 if 85 - 85: o000O0o + IIiIiII11i - o000O0o * Ooo00oOo0oOo - ooOoO0O00 % ii1ii11IIIiiI
 if 1 - 1: ii / o0o00Oo0O + OOooOOo + OOooOOo . I1111IIi - OOooOOo
 if 9 - 9: I1111IIi * ii % oOo0O0Ooo / OOooOOo * Ii1IIIi1
 if 48 - 48: ii . OOooOOo
 if 65 - 65: Ooo00oOo0oOo . I1ii11iIi11i
 if 94 - 94: OOooOOo + O0OOOoOoo0 . iiiiiiii1
 if 69 - 69: o0o00Oo0O - o0o00Oo0O
 if 41 - 41: O0OOOoOoo0 % I11i
 if 67 - 67: o0o00Oo0O % I1111IIi
 if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % o000O0o
 if 39 - 39: ooOOOoO
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 60 - 60: o000O0o
 if 62 - 62: I1111IIi * Ii1IIIi1
def oOooOOoO0oO0oo0O ( url ) :
 oO0OOoo0OO = IIII ( url )
 O00oO0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOooOoooOoOo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O00oO0 ) )
 for url , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 55 - 55: I1ii11iIi11i
def IIi1i1I11IIII ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 55 - 55: iI11I1II1I1I % oO0o / Ii1I / I11i
def IIiI1111iI ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  if 'episode' in url :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in o0OOOO00O0Oo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 62 - 62: ooOOOoO + o0o00Oo0O * oO0o
  if 59 - 59: IIiIiII11i
def iIiIi11I1iIii1i11 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiiI11II11i = 'http://www.watchseriesgo.to/search/' + I1i11II . replace ( ' ' , '%20' )
 oO0OOoo0OO = IIII ( iIiiI11II11i )
 OOooOoooOoOo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , o0OIiII , I1111i in OOooOoooOoOo :
  if 'watch online' in I1111i :
   pass
  else :
   print o0OIiII
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + o0OIiII , 10044 , o00O0O , '' , '' )
   if 98 - 98: ii1ii11IIIiiI - ii1ii11IIIiiI
   xbmcplugin . setContent ( I11iii1Ii , 'movies' )
   if 58 - 58: Ooo00oOo0oOo
def oOOo0OO00OoO ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , o00iI1Ii11iIiiI1 , Iiiiii111i1ii in OOooOoooOoOo :
  oOoo000 = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( o00iI1Ii11iIiiI1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + oOoo000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , Iiiiii111i1ii )
  if 95 - 95: oO0o . Ooo00oOo0oOo
def o0oO0oOOOo ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  oOoo000 = ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + oOoo000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in o0OOOO00O0Oo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 90 - 90: ooOoO0O00 - ooOOOoO
def Oo0OOOoOO ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in o0OOOO00O0Oo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 11 - 11: o0o00Oo0O * OOooOOo
def IIii1i ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 O00oO0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11IIIiI1I , iI1 in O00oO0 :
  OOooOoooOoOo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iI1 ) )
  for url , I1111i in OOooOoooOoOo :
   oOoo000 = ( i11IIIiI1I ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + oOoo000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in OOooOoooOoOo :
  Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in o0OOOO00O0Oo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 69 - 69: I1111IIi / ii % Ii
class Ii11IIIi1 ( ) :
 if 93 - 93: Ii . I11i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 16 - 16: ooOoO0O00 . ooOoO0O00 / I1111IIi % OOooOOo / oOo0O0Ooo * Ii1I
  oOoo000 = name
  self . Get_Sources ( o0OIiII , oOoo000 )
  if 30 - 30: I11i + ii + o000O0o / IIiIiII11i * I1ii11iIi11i
  if 59 - 59: ooOOOoO / OOooOOo * oO0o * ii1ii11IIIiiI % Ooo00oOo0oOo
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = IIII ( URL )
  OOooOoooOoOo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o0OIiII , I1111i in OOooOoooOoOo :
   URL = 'http://www.watchseriesgo.to/link/' + o0OIiII
   self . Get_site_link ( URL , season_name )
   if 61 - 61: I1ii11iIi11i - o0o00Oo0O - ii
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  o0OOOO00O0Oo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for url in OOooOoooOoOo :
   self . main ( url , season_name )
  for url in o0OOOO00O0Oo :
   self . main ( url , season_name )
  for url in ooOoO00 :
   self . main ( url , season_name )
   if 4 - 4: IIiIiII11i - Ooo00oOo0oOo % I1ii11iIi11i * Ii
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iIiII1iiiiI = 'DACLIPS'
   if iIiII1iiiiI in Ii11IIIi1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , iIiII1iiiiI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    iIiII1iiiiI = 'FILEHOOT'
    if iIiII1iiiiI in Ii11IIIi1 . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , iIiII1iiiiI )
   else :
    if 'thevideo.me' in url :
     iIiII1iiiiI = 'THEVIDEO'
     if iIiII1iiiiI in Ii11IIIi1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , iIiII1iiiiI )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      iIiII1iiiiI = 'ALLMYVIDEOS'
      if iIiII1iiiiI in Ii11IIIi1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , iIiII1iiiiI )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       iIiII1iiiiI = 'VIDSPOT'
       if iIiII1iiiiI in Ii11IIIi1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , iIiII1iiiiI )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        iIiII1iiiiI = 'VODLOCKER'
        if iIiII1iiiiI in Ii11IIIi1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , iIiII1iiiiI )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 80 - 80: I1ii11iIi11i - I11i - IIiIiII11i . O0OOOoOoo0 - o0o00Oo0O * O0OOOoOoo0
         if 43 - 43: oOo0O0Ooo / ii1ii11IIIiiI / iiiiiiii1 + iI11I1II1I1I + ii
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1iii , I1111i in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 33 - 33: IIiIiII11i - O0OOOoOoo0 - iiiiiiii1
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iii , I1111i in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 92 - 92: oO0o * O0OOOoOoo0
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( oO0OOoo0OO )
  for I1iii in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 92 - 92: Ooo00oOo0oOo
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1iii in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 7 - 7: ii1ii11IIIiiI
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for I1iii in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 73 - 73: oO0o % Ii1I
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = IIII ( url )
  OOooOoooOoOo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1iii in OOooOoooOoOo :
   self . Printer ( I1iii , season_name , source_name )
   if 32 - 32: o000O0o + ii1ii11IIIiiI + iI11I1II1I1I * I1ii11iIi11i
 def Printer ( self , Link , season_name , source_name ) :
  if 62 - 62: Ii
  if Link in Ii11IIIi1 . List :
   pass
  elif source_name in Ii11IIIi1 . source_list :
   pass
  else :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   Ii11IIIi1 . List . append ( Link )
   Ii11IIIi1 . source_list . append ( source_name )
   if 2 - 2: oOo0O0Ooo
   xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 69 - 69: ii / I1ii11iIi11i * I1111IIi
   if 99 - 99: IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * Ooo00oOo0oOo / IIiIiII11i % ii
   if 14 - 14: O0OOOoOoo0 . O0OOOoOoo0 % iiiiiiii1
   if 42 - 42: I11i . o000O0o - iiiiiiii1
   if 33 - 33: IIiIiII11i / o0o00Oo0O / O0OOOoOoo0 - Ii1IIIi1 - ooOoO0O00
def oo0 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , Ooo , '' )
 if 8 - 8: Ii . ii1ii11IIIiiI / iI11I1II1I1I / Ii1I / O0OOOoOoo0 - ooOOOoO
def iI1i1I1iiii1Ii11 ( url ) :
 Iii1I1I11iiI1 ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for IiIIIIi , url , OoIIiIIIII1I , ooiiI , o00iIiI1iI1Ii1 , Oo0 , iioO , oooOo0OOOoo0 , oOo00o00oO , ii11I , Ooo0O00 in OOooOoooOoOo :
  OoIIiIIIII1I = OoIIiIIIII1I
  if 'Arsenal' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'arsenal-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                                  ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Bournemouth' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'afc-bournemouth.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                       ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Burnley' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'KEGnQWW.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                                   ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Chelsea' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'chelsea.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                                  ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Crystal' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                       ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Everton' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'Everton.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                                   ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Hull' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'hull-city-afc.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                                 ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Leicester' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                       ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Liverpool' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'liverpool-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                               ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Manchester City' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'city-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '               ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Manchester United' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + '91.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '          ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Middlesbrough' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                 ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Southampton' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                   ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Stoke City' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'stoke-city.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                          ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Sunderland' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'sunderland-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                        ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Swansea' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'swansea-city-afc.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                    ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Tottenham' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '        ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Watford' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '                              ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'Bromwich' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '   ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  elif 'West Ham' in OoIIiIIIII1I :
   OoO = III1iII1I1ii + 'west-ham.png'
   I1111i = '[COLOR' + iiI1IiI + ']' + IiIIIIi + ' - ' + OoIIiIIIII1I + '             ' + ooiiI + '        ' + o00iIiI1iI1Ii1 + '        ' + Oo0 + '        ' + iioO + '        ' + oooOo0OOOoo0 + '        ' + oOo00o00oO + '        ' + ii11I + '[/COLOR]'
  Iii1I1I11iiI1 ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , OoO , OoO , OoIIiIIIII1I )
  if 53 - 53: o0o00Oo0O . oOo0O0Ooo
def o0oOOoO000 ( description ) :
 OoIIiIIIII1I = description
 o0OIiII = ( 'http://www.fullmatchesandshows.com/?s=' + OoIIiIIIII1I ) . replace ( ' ' , '%20' )
 Oo00o00Oo ( o0OIiII )
 if 50 - 50: iiiiiiii1 % I1ii11iIi11i
def oO0000O0Oo00O ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 OOooOoooOoOo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o0OIiII , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , Ooo , '' )
  if 42 - 42: Ii / oOo0O0Ooo - oO0o - iiiiiiii1 + IIiIiII11i % iiiiiiii1
def Ii1IIii ( url ) :
 oO0OOoo0OO = IIII ( url )
 O00oO0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in O00oO0 :
  oooOOoo = re . compile ( '(.*?)</h2>' ) . findall ( str ( O00oO0 ) )
  for iI1iii1iIiiI in oooOOoo :
   iI1iii1iIiiI = iI1iii1iIiiI
  II1iiiiI1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O00oO0 ) )
  for IiiIiiIIII , o00O0O , time , oOoOOOOoO0 in II1iiiiI1 :
   IiIi1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oOoOOOOoO0 )
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + iI1iii1iIiiI + ' - ' + IiiIiiIIII + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , Ooo , ( str ( IiIi1 ) ) )
   if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - ooOOOoO
 O0oO0 ( 'tvshows' , 'Media Info 3' )
 if 40 - 40: ii1ii11IIIiiI . OOooOOo * o0o00Oo0O
def IIiiIii11 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 if 74 - 74: ooOoO0O00
def Ii11ii1 ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , Ooo , '' )
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  iiiIiiiI1I = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   iiiIiiiI1I = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + iiiIiiiI1I + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in o0OOOO00O0Oo :
  iiiIiiiI1I = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + iiiIiiiI1I + '[/COLOR]' , url , 10013 , o00O0O )
def Oo00o00Oo ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , Ooo , '' )
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 6 - 6: oO0o
 if 99 - 99: I11i * o000O0o % Ooo00oOo0oOo * Ooo00oOo0oOo + ii
 if 82 - 82: Ii1IIIi1 / OOooOOo - o000O0o / iiiiiiii1
 if 50 - 50: o000O0o + oO0o . Ii + Ii1I + Ii
 if 31 - 31: Ooo00oOo0oOo * I1111IIi . OOooOOo * Ii1IIIi1
 if 28 - 28: O0OOOoOoo0 + oOo0O0Ooo - I1ii11iIi11i % o000O0o . Ii1IIIi1 + oOo0O0Ooo
 if 72 - 72: ooOOOoO / I1ii11iIi11i / Ooo00oOo0oOo * OOooOOo + o000O0o
 for url , o00O0O , I1111i in o0OOOO00O0Oo :
  iiiIiiiI1I = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + iiiIiiiI1I + '[/COLOR]' , url , 10013 , o00O0O )
   if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - O0OOOoOoo0 . ii
def iI1111i1i11Ii ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for IIi1IIIIi in OOooOoooOoOo :
  oo0O00o0O0Oo = ( IIi1IIIIi ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOOo0o00OO0000 ( 'http:' + oo0O00o0O0Oo )
  if 26 - 26: ooOoO0O00 / ii1ii11IIIiiI . ii1ii11IIIiiI
  if 20 - 20: o000O0o - ii1ii11IIIiiI / I1ii11iIi11i * oO0o
  if 55 - 55: ii
  if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
def i1iIii ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , url , 8046 , o00O0O )
 for url in o0OOOO00O0Oo :
  oO0oo ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def O0o00 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  OOOOo0o00OO0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 8 - 8: I1111IIi * I1ii11iIi11i - o000O0o . iI11I1II1I1I
def IiIiI ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  yt . PlayVideo ( url )
  if 77 - 77: I11i
def I1 ( ) :
 oO0oo ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 oO0oo ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 oO0oo ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oo0000o ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  oO0oo ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 99 - 99: Ooo00oOo0oOo - Ii1I . IIiIiII11i * Ii . o000O0o - oO0o
  if 31 - 31: Ii * ooOOOoO . I11i % o000O0o * Ii1I % o0o00Oo0O
def OOoO00O ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   oO0oo ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def iio00O0o00oo ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  url = ( url ) . replace ( '\/' , '/' )
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 10012 , '' )
  if 19 - 19: oOo0O0Ooo
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOoo ( name , url ) :
 I1I1i11 = 0
 name = name
 url = url
 OO = [ '144' , '240' , '380' , '480' , '720' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , OO )
 if OoOoO == 0 :
  OOOOo0o00OO0000 ( url )
  if 79 - 79: I11i - IIiIiII11i
  if 70 - 70: I1111IIi . Ooo00oOo0oOo % ooOoO0O00 / iI11I1II1I1I
  if 98 - 98: ooOoO0O00 % I1ii11iIi11i
  if 82 - 82: iiiiiiii1
  if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / ii1ii11IIIiiI
  if 9 - 9: OOooOOo - O0OOOoOoo0
  if 39 - 39: ooOoO0O00
  if 19 - 19: oOo0O0Ooo . oOo0O0Ooo - Ii
def O00O0O0OO00oo ( ) :
 iIIII = O0iIiIIIIIii ( 'http://documentarylovers.com/' )
 OOooOoooOoOo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  if 'genre' in o0OIiII :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , o0OIiII , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11IIIIiI1 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  oO0oo ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 93 - 93: Ii
def OoOiII11IiIi ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in o0OOOO00O0Oo :
  iio00O0o00oo ( url )
  if 27 - 27: oO0o + OOooOOo
def ooo0oOooo0o0 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://documentarylovers.com/?s=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iiioOO0OO0O = II11 . lower ( )
 I11IIIIiI1 ( I1iiioOO0OO0O )
 if 13 - 13: Ooo00oOo0oOo . iI11I1II1I1I . o000O0o . O0OOOoOoo0
def oo0oo00O0O ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if 'films' in url :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def iIiiI1I ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  if 'films' in url :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in o0OOOO00O0Oo :
  oO0oo ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def Oo0iI1Iii11i ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  if 'rtd' in url :
   O0OOOo0o ( url )
   if 73 - 73: o0o00Oo0O * I1111IIi . ooOoO0O00
def O0OOOo0o ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for O00O0oOO00O00 , file in OOooOoooOoOo :
  url = ( 'https://rtd.rt.com' + O00O0oOO00O00 + file )
  OOOOo0o00OO0000 ( url )
  if 51 - 51: oO0o - ii1ii11IIIiiI % o0o00Oo0O - OOooOOo
  if 53 - 53: ii1ii11IIIiiI / ooOoO0O00 / ooOoO0O00
def o0oo00O ( ) :
 oO0OOoo0OO = O0iIiIIIIIii ( 'http://www.stream2watch.co/live-tv' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O , I1111i , IIIIII1iI1II in OOooOoooOoOo :
  oO0oo ( ( I1111i + '[COLOR' + iiI1IiI + ']' + IIIIII1iI1II + '[/COLOR]' ) , o0OIiII , 8086 , o00O0O )
  if 14 - 14: oOo0O0Ooo / o0o00Oo0O
def II111iii ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 56 - 56: iI11I1II1I1I % oO0o . iiiiiiii1 % O0OOOoOoo0 . I1111IIi * I1ii11iIi11i
def Ii11II1i1I ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  i1iIii1 ( url , I1111i )
  if 92 - 92: O0OOOoOoo0 . I1ii11iIi11i - I1ii11iIi11i - I11i + I1111IIi - o0o00Oo0O
def i1iIii1 ( url , name ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  print url
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 30 - 30: O0OOOoOoo0 - ii1ii11IIIiiI - oO0o
def ii11 ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 OOooOoooOoOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + o0OIiII , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def oOOooooO ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def o000Ooo00o00O ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 ooo0O0O0oo0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , I1111i in ooo0O0O0oo0 :
  oO0oo ( '[COLOR' + iiI1IiI + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  oO0oo ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , o00O0O , I1111i in o0OOOO00O0Oo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def oo000oO ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  IiIiII11i1 ( url )
def IiIiII11i1 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
  if 44 - 44: oOo0O0Ooo % o000O0o * Ii * Ii - I1ii11iIi11i . I1111IIi
def iIIiIiI1I1 ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o0OIiII , 8065 , III1iII1I1ii + 'classicmovies.png' )
def o00i111iiIiiIiI ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  O0OoOOO00 ( url )
  if 59 - 59: o000O0o + oOo0O0Ooo / IIiIiII11i / OOooOOo
def I1IIIiIiIi ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o0OIiII , 8065 , III1iII1I1ii + 'classictv.png' )
def oOoo00 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in o0OOOO00O0Oo :
  yt . PlayVideo ( url )
  if 29 - 29: o000O0o / OOooOOo . iI11I1II1I1I / Ii1IIIi1 % OOooOOo % ii1ii11IIIiiI
def iiI1 ( ) :
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + o0OIiII , 8071 , III1iII1I1ii + 'streams.png' )
def oooOOO0o0O0 ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in OOooOoooOoOo :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def iiiI1IiI ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in OOooOoooOoOo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OooO0 + '/' + II11iiii1Ii + url ) . strip ( )
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o00O0O , i1II1 , '' )
  if 2 - 2: o0o00Oo0O % I1111IIi % Ii1I % I11i - I1ii11iIi11i
def i1i11ii1 ( ) :
 OO = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OO )
 if OoOoO == 0 :
  o0iiii1ii ( 'http://watchxxxfree.com/categories' )
 if OoOoO == 1 :
  Ii1iii11I ( 'http://www.perfectgirls.net' )
 if OoOoO == 2 :
  Ii11iIiiI ( 'http://www.xvideos.com/best' )
 if OoOoO == 3 :
  iiII ( 'http://www.xvideos.com/best' )
 if OoOoO == 4 :
  Ii11iIiiI ( 'http://www.xvideos.com/best' )
 if OoOoO == 5 :
  Ii11iIiiI ( 'http://www.xvideos.com/verified/videos' )
 if OoOoO == 6 :
  iII1IiiIIIIii ( 'http://www.xvideos.com/tags' )
 if OoOoO == 7 :
  oOOO ( 'http://www.xvideos.com/porn' )
 if OoOoO == 8 :
  Iii1IiiII1Ii1 ( )
  if 26 - 26: ii + oOo0O0Ooo
  if 57 - 57: o000O0o . ooOOOoO % I11i
  if 32 - 32: Ii1IIIi1 / O0OOOoOoo0 - o0o00Oo0O * iI11I1II1I1I
  if 70 - 70: ii % ii % oO0o
  if 98 - 98: oO0o
  if 18 - 18: Ii1IIIi1 + I1ii11iIi11i - oO0o / I1111IIi / o000O0o
  if 53 - 53: o000O0o + I11i . Ooo00oOo0oOo / Ii1IIIi1
  if 52 - 52: I1111IIi + I1111IIi
  if 73 - 73: I11i . Ii % ii + iiiiiiii1 . ii / o000O0o
def oOiiI1i11I ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  if 'ch' in url :
   IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def IiIIii ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo0O0 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , I1111i in OOooOoooOoOo :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for I1111i , url in oo0O0 :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def Ii111Ii11 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if 'jetload' in url :
   Ii1II ( url )
def IIiII ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
def o0iiii1ii ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , O0OOOo in OOooOoooOoOo :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORorange]   ' + O0OOOo + '[/COLOR]' , url , 90006 , o00O0O , III1iII1I1ii + 'Jizbox.png' , '' )
def iII11 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo0O0 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in oo0O0 :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def O00OO00OOOoO ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if 'jetload' in url :
   Ii1II ( url )
def Ii1II ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( url )
def Ii1iii11I ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , O0OOOo in OOooOoooOoOo :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORorange]' + O0OOOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def IiI11Ii1iI ( url ) :
 oO0OOoo0OO = IIII ( url )
 ii11I1 = url
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo0O0 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  I1I1i1I ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in oo0O0 :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , ii11I1 + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def ooOo0 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  oOo0o ( 'http://www.perfectgirls.net' + url )
def oOo0o ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( 'http://' + url )
def oOOO ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , O0OOOo in OOooOoooOoOo :
  IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + O0OOOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def iII1IiiIIIIii ( url ) :
 oO0OOoo0OO = IIII ( url )
 oo0O0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in oo0O0 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , O0OOOo in OOooOoooOoOo :
  IIiii11ii1i ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( O0OOOo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 63 - 63: O0OOOoOoo0 % iiiiiiii1 * OOooOOo - O0OOOoOoo0 + ii1ii11IIIiiI % Ii
def I11iiIiiI1iIi11 ( url ) :
 oO0OOoo0OO = IIII ( url )
 oo0O0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in oo0O0 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 OOooOoooOoOo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , oOOO0ooo in OOooOoooOoOo :
  IIiii11ii1i ( I1111i + '--' + ( oOOO0ooo ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 32 - 32: Ii1I * I11i * oO0o * o000O0o * o0o00Oo0O
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ii11iIiiI ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , I1iI1I1 , Ooi1IIii1i in OOooOoooOoOo :
  IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + Ooi1IIii1i + ' - [COLORred]' + I1iI1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , Ooi1IIii1i + ' - ' + I1iI1I1 )
 O0oOo0o0O0o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in O0oOo0o0O0o :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 76 - 76: o0o00Oo0O
def iiII ( url ) :
 oO0OOoo0OO = IIII ( url )
 O00oO0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo0O0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in oo0O0 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O00oO0 ) )
 for url , I1111i in OOooOoooOoOo :
  if '/c/' in url :
   IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 71 - 71: oOo0O0Ooo . ooOoO0O00
   if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + Ooo00oOo0oOo + Ooo00oOo0oOo + ii1ii11IIIiiI
def Iii1IiiII1Ii1 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1I1 = ( I1i11II ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 I1iiioOO0OO0O = IIi1I1 . lower ( )
 II1ii = 'http://www.xvideos.com/?k=' + I1iiioOO0OO0O
 print II1ii + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = IIII ( II1ii )
 OOooOoooOoOo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , o0OIiII , I1111i , I1iI1I1 , Ooi1IIii1i in OOooOoooOoOo :
  IIiii11ii1i ( '[COLOR' + iiI1IiI + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + Ooi1IIii1i + ' - [COLORred]' + I1iI1I1 + '[/COLOR]' , 'http://www.xvideos.com' + o0OIiII , 10108 , o00O0O , o00O0O , Ooi1IIii1i + ' - ' + I1iI1I1 )
 O0oOo0o0O0o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for o0OIiII in O0oOo0o0O0o :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + o0OIiII , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 80 - 80: I11i % ii1ii11IIIiiI
def ooOooOooOOO ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 o0OOOO00O0Oo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if 'http' in url :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in o0OOOO00O0Oo :
  if 'http' in url :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 59 - 59: Ii1IIIi1
def OOI1i ( url ) :
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 import urlresolver
 try : oo000oOo0 . play ( url )
 except : pass
 if 47 - 47: ii1ii11IIIiiI . OOooOOo
 if 58 - 58: ii1ii11IIIiiI + I1ii11iIi11i / oOo0O0Ooo
def o000OO00OoO00 ( ) :
 if 97 - 97: iiiiiiii1 / iI11I1II1I1I % iiiiiiii1 / oOo0O0Ooo * ii1ii11IIIiiI % OOooOOo
 if 17 - 17: iI11I1II1I1I
 if 89 - 89: ooOoO0O00 . ooOoO0O00
 if 10 - 10: ii1ii11IIIiiI % I1ii11iIi11i
 if 48 - 48: o000O0o + I1111IIi % o000O0o
 if 84 - 84: o0o00Oo0O % ooOOOoO . ooOOOoO . ii1ii11IIIiiI * Ii1IIIi1
 if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
 if 61 - 61: oOo0O0Ooo + Ooo00oOo0oOo % I1111IIi % iI11I1II1I1I - ii
 if 22 - 22: o000O0o + IIiIiII11i + I1ii11iIi11i
 if 83 - 83: iiiiiiii1
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 8091 , III1iII1I1ii + 'gofish.png' )
def i1Ii1i11ii ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  oO0oo ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def oO0O0oo ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOOOOOO00OO = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O in OOOOOOO00OO :
  o00O0O = o00O0O
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  oO0oo ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 68 - 68: oOo0O0Ooo
def O00O ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  yt . PlayVideo ( url )
  if 5 - 5: OOooOOo . I1ii11iIi11i
  if 89 - 89: oOo0O0Ooo / ii1ii11IIIiiI / ii - Ii + oOo0O0Ooo
  if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Ii1IIIi1
  if 64 - 64: iiiiiiii1 / ooOoO0O00 % ii1ii11IIIiiI
OOoOo0O0 = '{PQ},' ; I1o0 = '{SC},' ; I1IiiiiI1i1I = '{XG},' ; I11i1I1 = '{JP},' ; ooOooO = '{HW},' ; oooo = '{RT},'
def iiII1i11i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IIIiI1iIIII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 o0OIiII = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 75 - 75: o000O0o % IIiIiII11i
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 IIIIi1Iii1iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 ii1IIi1iI1ii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o00iIIiIi111iI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 II1I1ii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1i11II
 oo0OO0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OO0OooOOoO00OO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 ii11ii1iIiI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 OoOo0oO0 = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 1 - 1: o000O0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = OOO00O ( o0OIiII )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 87 - 87: o0o00Oo0O * IIiIiII11i + iI11I1II1I1I % Ooo00oOo0oOo % Ii - OOooOOo
 if 73 - 73: ii1ii11IIIiiI + ooOOOoO
 ii1ii1ii = OOO00O ( o0ooOo0OOOO0o )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = OOO00O ( IIIIi1Iii1iIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IIIiii11 = OOO00O ( ii1IIi1iI1ii1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iI11ii = OOO00O ( II1I1ii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOoooO00OO0o = OOO00O ( oo0OO0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIi1iI = OOO00O ( OO0OooOOoO00OO00 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 i11ii = OOO00O ( ii11ii1iIiI1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IiI111I = OOO00O ( OoOo0oO0 )
 if 62 - 62: ii + O0OOOoOoo0
 if 32 - 32: OOooOOo * I11i / ii
 if oO0OOoo0OO != 'Failed' :
  OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
  for oOooo00OOO000 , I1111i in OOooOoooOoOo :
   if I1i11II in I1111i . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0OIiII + oOooo00OOO000 ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 85 - 85: ooOoO0O00 - o000O0o / o0o00Oo0O + o0o00Oo0O / Ii1I
    if 54 - 54: iiiiiiii1 * Ii1I . IIiIiII11i / o000O0o % o000O0o
    if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % I1111IIi
    if 53 - 53: ooOoO0O00
    if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
    if 9 - 9: ooOoO0O00 - OOooOOo
    if 57 - 57: iI11I1II1I1I * ooOOOoO * ii1ii11IIIiiI / Ooo00oOo0oOo
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for oOooo00OOO000 , I1111i in ooOoO00 :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o0ooOo0OOOO0o + oOooo00OOO000 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in Iii1I1111ii :
   if I1i11II in I1111i . lower ( ) :
    I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Silent Hunter[/COLOR]' ) , o0OIiII , 222 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 46 - 46: ooOOOoO
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if IIIiii11 != 'Failed' :
  oOO0 = [ ]
  IiIiIIi1IiiIi1III = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIiii11 )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in IiIiIIi1IiiIi1III :
   if I1i11II in I1111i . lower ( ) :
    if I1111i in oOO0 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , o0OIiII , 1016 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
     oOO0 . append ( I1111i )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 if iI11ii != 'Failed' :
  IiIiIiiIIii = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iI11ii )
  for o0OIiII , o00O0O , I1111i in IiIiIiiIIii :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + o0OIiII , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 77 - 77: Ooo00oOo0oOo * iiiiiiii1 . o000O0o * ooOOOoO % IIiIiII11i
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
    if 75 - 75: I1ii11iIi11i + ooOOOoO + oO0o
    if 97 - 97: iiiiiiii1 % Ii % Ii1IIIi1
    if 21 - 21: I1ii11iIi11i / ooOOOoO / Ii1I / ooOoO0O00 / I11i
    if 86 - 86: ooOoO0O00
    if 33 - 33: OOooOOo % Ii * o000O0o
    if 69 - 69: IIiIiII11i + I1ii11iIi11i - Ooo00oOo0oOo . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
    if 75 - 75: oO0o % ii
    if 16 - 16: o0o00Oo0O / ooOoO0O00
 if iIi1iI != 'Failed' :
  OOoo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi1iI )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in OOoo0 :
   if I1i11II in I1111i . lower ( ) :
    I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Reaper[/COLOR]' ) , o0OIiII , 222 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 7 - 7: oOo0O0Ooo % I1111IIi * O0OOOoOoo0 + OOooOOo / OOooOOo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if i11ii != 'Failed' :
  Ii1iiIIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11ii )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in Ii1iiIIIiI :
   if I1i11II in I1111i . lower ( ) :
    I1I1i1I ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source APPRENTICE[/COLOR]' ) , o0OIiII , 222 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 92 - 92: oO0o . I11i . ooOOOoO % OOooOOo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 58 - 58: Ii1I % ooOOOoO * ooOOOoO - ii1ii11IIIiiI
 if IiI111I != 'Failed' :
  I111IiI11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI111I )
  for o0OIiII , O0Oo000 , I1111i in I111IiI11 :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Silent Hunter[/COLOR]' ) , o0OIiII , 222 , O0Oo000 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 66 - 66: Ooo00oOo0oOo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 o0OOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 34 - 34: ii1ii11IIIiiI % Ii + Ii - ii1ii11IIIiiI
 for o0OoO0oo0O0o in o0OOo :
  ii1III1iiIi = o00OO00OoO + o0OoO0oo0O0o + ooooooO0oo
  iii1iII = OOO00O ( ii1III1iiIi )
  if iii1iII != 'Failed' :
   O00o0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1iII )
   for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in O00o0o :
    if I1i11II in I1111i . lower ( ) :
     I1I1i1I ( '[COLOR' + iiI1IiI + ']' + I1111i + ' - Source Pandoras[/COLOR]' , o0OIiII , 222 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 19 - 19: Ooo00oOo0oOo
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 85 - 85: iiiiiiii1 - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
 o0OOo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 94 - 94: iI11I1II1I1I + O0OOOoOoo0
 if 44 - 44: oO0o + Ii1IIIi1 % oO0o + ooOoO0O00 + ii1ii11IIIiiI + o0o00Oo0O
 for o0OoO0oo0O0o in o0OOo :
  ii1III1iiIi = IIIiI1iIIII + o0OoO0oo0O0o
  Ii1iII1ii1 = OOO00O ( ii1III1iiIi )
  if Ii1iII1ii1 != 'Failed' :
   ooOo0I11I1i = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( Ii1iII1ii1 )
   for oOooo00OOO000 , I1111i in ooOo0I11I1i :
    if I1i11II in I1111i . lower ( ) :
     Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IIIiI1iIIII + o0OoO0oo0O0o + oOooo00OOO000 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 100 - 100: Ooo00oOo0oOo
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
     if 25 - 25: ii . ooOOOoO % ii1ii11IIIiiI . O0OOOoOoo0
def I111i1i1111 ( ) :
 if 67 - 67: ii + I1111IIi / iiiiiiii1
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 if 75 - 75: O0OOOoOoo0 / ii . oOo0O0Ooo + I1111IIi - IIiIiII11i
 o0OIiII = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( I1i11II ) . replace ( ' ' , '%20' )
 ii11I1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 IIIIi1Iii1iIi = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ii1IIi1iI1ii1 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1iiioOO0OO0O ) . replace ( ' ' , '+' )
 o00iIIiIi111iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 II1I1ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oo0OO0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 33 - 33: O0OOOoOoo0 / O0OOOoOoo0 . Ii * Ii1I + I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 16 - 16: O0OOOoOoo0
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 oO0OOoo0OO = OOO00O ( o0OIiII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0 = OOO00O ( ii11I1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ii1ii1ii = OOO00O ( o0ooOo0OOOO0o )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oooooOoo0ooo = OOO00O ( IIIIi1Iii1iIi )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIIiii11 = cloudflare . source ( ii1IIi1iI1ii1 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 Ii1iII1ii1 = OOO00O ( o00iIIiIi111iI )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iI11ii = OOO00O ( II1I1ii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOoooO00OO0o = OOO00O ( oo0OO0O )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 10 - 10: OOooOOo . O0OOOoOoo0 * iI11I1II1I1I - Ooo00oOo0oOo - OOooOOo / I1111IIi
 if oOoooO00OO0o != 'Failed' :
  II1I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoooO00OO0o )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in II1I11 :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source HeroVision[/COLOR]' ) , o0OIiII , 1016 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 20 - 20: I1111IIi . ooOoO0O00
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: oO0o
 if iI11ii != 'Failed' :
  IiIiIiiIIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI11ii )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in IiIiIiiIIii :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- source Reaper[/COLOR]' ) , o0OIiII , 1016 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 89 - 89: ooOoO0O00
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: iiiiiiii1 / I11i % O0OOOoOoo0 - ooOOOoO
    if 14 - 14: Ii1I - Ii * I1111IIi
    if 39 - 39: ii
    if 19 - 19: Ii
    if 80 - 80: oOo0O0Ooo
    if 58 - 58: Ooo00oOo0oOo + Ii1I % OOooOOo
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 22 - 22: iI11I1II1I1I - ooOOOoO / oOo0O0Ooo * O0OOOoOoo0
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if oO0OOoo0OO != 'Failed' :
  OOooOoooOoOo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , o0OIiII , I1111i in OOooOoooOoOo :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + ' - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + o0OIiII , 10044 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 26 - 26: I11i + o000O0o - I11i + I1ii11iIi11i . Ooo00oOo0oOo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 97 - 97: ooOoO0O00
    if 46 - 46: Ii1I
    if 30 - 30: oO0o / o0o00Oo0O * I11i * I1111IIi + ii * ii1ii11IIIiiI
    if 23 - 23: Ii1IIIi1
    if 36 - 36: O0OOOoOoo0 . ii1ii11IIIiiI - ooOoO0O00 + I1111IIi
    if 54 - 54: ii . Ooo00oOo0oOo - ii1ii11IIIiiI
    if 76 - 76: I1111IIi
    if 61 - 61: iiiiiiii1 / IIiIiII11i * iiiiiiii1 * OOooOOo * I1111IIi . Ii
    if 26 - 26: I1111IIi / iiiiiiii1 - oO0o . iI11I1II1I1I
    if 83 - 83: iiiiiiii1 % ooOOOoO / I1ii11iIi11i - ii1ii11IIIiiI / o0o00Oo0O
 if O0 != 'Failed' :
  o0OOOO00O0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in o0OOOO00O0Oo :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    oO0oo ( ( I1111i + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , o0OIiII , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 97 - 97: iI11I1II1I1I * Ii1IIIi1
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    oO0oo ( ( I1111i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0ooOo0OOOO0o + I1111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 95 - 95: oO0o
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    oO0oo ( ( I1111i + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IIIIi1Iii1iIi + I1111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 68 - 68: iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIiIiII11i - iI11I1II1I1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if IIIiii11 != 'Failed' :
  IiIiIIi1IiiIi1III = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIiii11 )
  for o0OIiII , o00O0O , I1111i in IiIiIIi1IiiIi1III :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + ' - Source - Dizi[/COLOR]' , o0OIiII , 8062 , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 75 - 75: iiiiiiii1 . oOo0O0Ooo * IIiIiII11i
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if Ii1iII1ii1 != 'Failed' :
  ooOo0I11I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1iII1ii1 )
  for o0OIiII , O0Oo000 , Iiiiii111i1ii , IiiI1iiiiI1iI , I1111i in ooOo0I11I1i :
   if I1iiioOO0OO0O in I1111i . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '- Source Scooby[/COLOR]' ) , o0OIiII , 1016 , O0Oo000 , IiiI1iiiiI1iI , Iiiiii111i1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 99 - 99: iI11I1II1I1I * Ii1I + O0OOOoOoo0
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: ooOoO0O00 % iiiiiiii1 . Ii1I - O0OOOoOoo0 + o000O0o
 OO0o0oo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for o0OoO0oo0O0o in OO0o0oo :
  ii1III1iiIi = o00OO00OoO + o0OoO0oo0O0o + ooooooO0oo
  i11ii = OOO00O ( ii1III1iiIi )
  if i11ii != 'Failed' :
   Ii1iiIIIiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i11ii )
   for I1111i , Iiiiii111i1ii , o0OIiII , o00O0O , i1II1 , oo000ii in Ii1iiIIIiI :
    if I1iiioOO0OO0O in I1111i . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + ' - Source Pandoras[/COLOR]' , o0OIiII , oo000ii , o00O0O , i1II1 , Iiiiii111i1ii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 51 - 51: iiiiiiii1 * iI11I1II1I1I . ii1ii11IIIiiI
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 25 - 25: o000O0o - ooOOOoO . Ii1IIIi1
     if 57 - 57: I11i + I1ii11iIi11i * Ii1I - iiiiiiii1 % iI11I1II1I1I - ooOOOoO
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def III1I11II11I ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OIiII = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( I1i11II ) . replace ( ' ' , '+' )
 if 78 - 78: Ii1I . I1111IIi . I1111IIi . Ii1IIIi1 % ii1ii11IIIiiI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = OOO00O ( o0OIiII )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 26 - 26: iiiiiiii1 + oO0o / OOooOOo . IIiIiII11i * ooOOOoO
 if oO0OOoo0OO != 'Failed' :
  o0OOOO00O0Oo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o0OIiII , I1111i in o0OOOO00O0Oo :
   if I1i11II in I1111i . lower ( ) :
    Ii111iIi1iIi ( ( I1111i + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + o0OIiII ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + ii1ii11IIIiiI % oOo0O0Ooo * Ooo00oOo0oOo
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
O0o0 = '{ZH},' ; ooOo0O0 = '{IX},' ; OooO00O0OO0oo = '{LM},'
if 60 - 60: IIiIiII11i + I11i % I1111IIi + iiiiiiii1 . O0OOOoOoo0 % IIiIiII11i
def oOoO0oO00ooOo ( url ) :
 iIoOO0OO00 = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIoOO0OO00 )
 for url , i11IIIiI1I , o0OO , I1111i in OOooOoooOoOo :
  oO0oo ( ( i11IIIiI1I ) . replace ( 'Sezon' , ' Season ' ) + ( o0OO ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 75 - 75: ii1ii11IIIiiI * I1ii11iIi11i / I1111IIi * I1ii11iIi11i / iiiiiiii1
  if 14 - 14: ooOoO0O00 * iI11I1II1I1I - ooOOOoO * OOooOOo - ii1ii11IIIiiI / Ooo00oOo0oOo
  if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
  if 96 - 96: Ii1I - o0o00Oo0O
def I1iO00O000oOO0oO ( url ) :
 iIoOO0OO00 = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iIoOO0OO00 )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , url , 222 , '' )
  if 88 - 88: I11i . oOo0O0Ooo % Ooo00oOo0oOo . I1ii11iIi11i % iiiiiiii1 . Ooo00oOo0oOo
  if 53 - 53: ooOoO0O00 % ooOOOoO - ii / OOooOOo - iI11I1II1I1I
  if 9 - 9: I1111IIi - oO0o + iI11I1II1I1I % o0o00Oo0O + Ii1IIIi1 + O0OOOoOoo0
  if 50 - 50: ooOoO0O00 + iiiiiiii1
def oOoO0oOo0Oo ( ) :
 if 39 - 39: I1111IIi
 iIoOO0OO00 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OOooOoooOoOo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIoOO0OO00 )
 for o0OIiII , o00O0O , I1111i , o0OO in OOooOoooOoOo :
  oO0oo ( I1111i + '  -  ' + ( o0OO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o0OIiII , 8063 , o00O0O )
  if 57 - 57: ii * ii - oOo0O0Ooo / I1111IIi * Ii1I - O0OOOoOoo0
def Oo0o ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , I1111i , o00O0O in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 8002 , o00O0O )
def I11iiIiI1II11 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , Ii1Ii1Ii1I1I in OOooOoooOoOo :
  Iii1I1I11iiI1 ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , Ii1Ii1Ii1I1I )
  if 94 - 94: I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + ii % oO0o
def I1111iIIiIIII ( ) :
 if 55 - 55: oO0o / ii
 oO0oo ( 'Coronation Street' , '' , 8001 , '' )
 oO0oo ( 'Eastenders' , '' , 8002 , '' )
 oO0oo ( 'Emmerdale' , '' , 8003 , '' )
 oO0oo ( 'Hollyoaks' , '' , 8004 , '' )
 oO0oo ( 'Im a Celebrity' , '' , 8005 , '' )
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
 if 61 - 61: ooOOOoO * ooOOOoO
 if 70 - 70: I1111IIi . Ii1I / I11i * Ooo00oOo0oOo
 if 74 - 74: oOo0O0Ooo . iiiiiiii1 / ii1ii11IIIiiI . O0OOOoOoo0
def OO00 ( ) :
 oO0OOoo0OO = IIII ( 'http://uksoapshare.blogspot.co.uk/' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in o0OIiII :
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0OIiII . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 10 - 10: Ii1IIIi1 * ooOoO0O00 . Ooo00oOo0oOo / I1111IIi . o000O0o / I1111IIi
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 1 - 1: ii1ii11IIIiiI % iiiiiiii1
def O0ooo0 ( ) :
 oO0OOoo0OO = IIII ( 'http://uksoapshare.blogspot.co.uk/' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in o0OIiII :
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0OIiII . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 89 - 89: O0OOOoOoo0 - ooOoO0O00 - O0OOOoOoo0
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: oO0o % oO0o
def IIIII1IIiIi ( ) :
 oO0OOoo0OO = IIII ( 'http://uksoapshare.blogspot.co.uk/' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in o0OIiII :
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0OIiII . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 91 - 91: oOo0O0Ooo / IIiIiII11i * o000O0o
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( ) :
 oO0OOoo0OO = IIII ( 'http://uksoapshare.blogspot.co.uk/' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in o0OIiII :
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0OIiII . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 62 - 62: Ii1I . I1111IIi . ooOOOoO
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: Ii1I / I1111IIi
def IIiIIiiiiiII1 ( ) :
 oO0OOoo0OO = IIII ( 'http://uksoapshare.blogspot.co.uk/' )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in o0OIiII :
    Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o0OIiII . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 7 - 7: Ii1I - iI11I1II1I1I
def oOOOo0Oooo ( name , url ) :
 I1iiIIiI11I = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if I1iiIIiI11I :
  I11II1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  oOoOo000 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  I11II1I = oOoOo000 . replace ( '\\/' , '/' )
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , '' , '' )
 O0ooO0ooo0oO . setPath ( I11II1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0ooO0ooo0oO )
 if 37 - 37: ii1ii11IIIiiI
 if 15 - 15: I11i % oO0o / ii1ii11IIIiiI
def II1IIIi ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 OOooOoooOoOo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , o0OIiII , 7071 , III1iII1I1ii + 'popcorn.png' )
 for o0OIiII , I1111i in o0OOOO00O0Oo :
  oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , o0OIiII , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 40 - 40: ooOoO0O00 / ii / o000O0o * I1111IIi - I11i
def ooooOo00O ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOooOoooOoOo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Movies' in I1111i :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( o0OIiII ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def iiIIiI1I ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 OOooOoooOoOo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in o0OOOO00O0Oo :
  oO0oo ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 67 - 67: Ii1I % ii
  if 41 - 41: oO0o / O0OOOoOoo0 + I1111IIi . I1111IIi / Ooo00oOo0oOo
def IiIi ( url ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OOooOoooOoOo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in OOooOoooOoOo :
  if '{{' in I1111i :
   pass
  else :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
O0oo0o0o0o = '{UJ},' ; iI1I1I1iiI1i = '{WE},' ; IiII1111I = '{WP},' ; iiIIii111Ii = '{PP},'
def OO000oooOo000 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in OOooOoooOoOo :
  if '{{' in I1111i :
   pass
  else :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oO0o0Oo0 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  i1I1iiiI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1I1iiiI ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 44 - 44: Ii1IIIi1
 if 76 - 76: Ii1I . iiiiiiii1 . Ooo00oOo0oOo
 if 74 - 74: I1ii11iIi11i
def o0o00OO00OOo0 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if '(cooltvseries.com)' in I1111i :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , I1111i in o0OOOO00O0Oo :
  if '(cooltvseries.com)' in I1111i :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def ooOo00ooO ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  OOOOo0o00OO0000 ( ( url ) . replace ( ' ' , '%20' ) )
I1ii11IiI1I = '{XX},' ; Oo0Ii = '{UD},' ; oooooOOo0Oo = '{YT},' ; IiiiiiiI111i = '{JS},' ; iiIIIIiI11II1 = '{PF},'
if 26 - 26: o0o00Oo0O . Ii1IIIi1 + ii1ii11IIIiiI - ooOOOoO . Ii1IIIi1
def II1Iii1I1II1i ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 OOooOoooOoOo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , I1111i , o00O0O in OOooOoooOoOo :
  Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( o0OIiII ) ) , 222 , o00O0O )
  if 100 - 100: Ii - I1ii11iIi11i
def I1IiI1iI11 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  if 'youtu' in url :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  oO0oo ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 47 - 47: ii1ii11IIIiiI * OOooOOo * O0OOOoOoo0
def iIiii1IIi1I ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def IiI1I1i1 ( url ) :
 iIIII = IIII
 OOooOoooOoOo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 6 - 6: oOo0O0Ooo . IIiIiII11i + I1111IIi / oO0o % oOo0O0Ooo . ii
  if 64 - 64: iI11I1II1I1I + IIiIiII11i . ii1ii11IIIiiI % I1ii11iIi11i * iiiiiiii1
  if 7 - 7: ooOoO0O00 + ooOoO0O00 / O0OOOoOoo0
  if 32 - 32: ooOOOoO * Ii1I - ii / oOo0O0Ooo . iiiiiiii1 - ooOoO0O00
  if 60 - 60: OOooOOo % OOooOOo
def I1I ( ) :
 if 9 - 9: O0OOOoOoo0 - IIiIiII11i * oO0o
 oO0oo ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oO0oo ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * Ooo00oOo0oOo / ii1ii11IIIiiI / OOooOOo
 if 15 - 15: iiiiiiii1 / Ooo00oOo0oOo
def O0Oo00o0o ( Cat_Name ) :
 if 80 - 80: Ii % iI11I1II1I1I / Ii
 OOoOO0ooo0O = False
 ii1IIi1IIIIi1 = '0'
 if Cat_Name == 'All Channels' : OOoOO0ooo0O = True
 if Cat_Name == 'Entertainment' : ii1IIi1IIIIi1 = '1'
 if Cat_Name == 'Movies' : ii1IIi1IIIIi1 = '2'
 if Cat_Name == 'Music' : ii1IIi1IIIIi1 = '3'
 if Cat_Name == 'News' : ii1IIi1IIIIi1 = '4'
 if Cat_Name == 'Sports' : ii1IIi1IIIIi1 = '5'
 if Cat_Name == 'Documentary' : ii1IIi1IIIIi1 = '6'
 if Cat_Name == 'Kids' : ii1IIi1IIIIi1 = '7'
 if Cat_Name == 'Food' : ii1IIi1IIIIi1 = '8'
 if Cat_Name == 'Religious' : ii1IIi1IIIIi1 = '9'
 if Cat_Name == 'USA Channels' : ii1IIi1IIIIi1 = '10'
 if Cat_Name == 'Other' : ii1IIi1IIIIi1 = '11'
 if 4 - 4: Ii1I - O0OOOoOoo0
 iIIII = IIII ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOooOoooOoOo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( OOooOoooOoOo ) )
 for I1111i , o00O0O , IiiIi11II1IIIIIi in OOooOoooOoOo :
  Oo0ooOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if IiiIi11II1IIIIIi == ii1IIi1IIIIi1 :
   oO0oo ( I1111i , '' , 7022 , Oo0ooOO )
  elif OOoOO0ooo0O == True :
   oO0oo ( I1111i , '' , 7022 , Oo0ooOO )
  else : pass
  if 6 - 6: Ii / ooOoO0O00 / O0OOOoOoo0 . oOo0O0Ooo - o000O0o % Ii
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: o000O0o % Ii - Ii1I
def I1oooO00oOOooO ( Search_Name ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OOooOoooOoOo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 OOooOoooOoOo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , o0OIiII , ii11I1 , o0ooOo0OOOO0o in OOooOoooOoOo :
  Oo0ooOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  Ii111iIi1iIi ( Search_Name + ': Link 1' , ( o0OIiII ) . replace ( '\\' , '' ) , 222 , Oo0ooOO )
  Ii111iIi1iIi ( Search_Name + ': Link 2' , ( ii11I1 ) . replace ( '\\' , '' ) , 222 , Oo0ooOO )
  Ii111iIi1iIi ( Search_Name + ': Link 3' , ( o0ooOo0OOOO0o ) . replace ( '\\' , '' ) , 222 , Oo0ooOO )
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IIIii111i ( ) :
 iIIII = IIII ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOooOoooOoOo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , ( o0OIiII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def O000OoOO0oO ( ) :
 iIIII = IIII ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OOooOoooOoOo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , ( o0OIiII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def iII1o00OO0 ( ) :
 iIIII = IIII ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , o0OIiII in OOooOoooOoOo :
  Ii111iIi1iIi ( I1111i , ( o0OIiII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / Ii1IIIi1 + iiiiiiii1
def i11IiIiii ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 15 - 15: iiiiiiii1 * iI11I1II1I1I * Ooo00oOo0oOo
 if 96 - 96: I1111IIi * iI11I1II1I1I / OOooOOo % o000O0o * IIiIiII11i
def I1iiIIii ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , Iiiiii111i1ii , o00O0O , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( Iiiiii111i1ii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
 for url in o0OOOO00O0Oo :
  oO0oo ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 90 - 90: O0OOOoOoo0 * Ii1IIIi1 % IIiIiII11i / o000O0o
def o00oO0O000 ( url ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iiiiii111i1ii , o00O0O in OOooOoooOoOo :
  I1I1i1I ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , Iiiiii111i1ii )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
 iI1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0OoOOOO00o0 in iI1 :
  o000O0O = ( oO0o0OoOOOO00o0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  Iii1I1I11iiI1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 89 - 89: iiiiiiii1 + IIiIiII11i . I1111IIi . OOooOOo - I11i
def O00oOO ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 75 - 75: iiiiiiii1 - ii1ii11IIIiiI % ii1ii11IIIiiI + iiiiiiii1 * I11i - Ii1I
 if 26 - 26: Ii1IIIi1 * ooOOOoO % oOo0O0Ooo + ii1ii11IIIiiI
 if 38 - 38: ii1ii11IIIiiI - I1ii11iIi11i / ooOOOoO + Ooo00oOo0oOo . ii1ii11IIIiiI + O0OOOoOoo0
def iIiii1iI1Ii ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def ooIi ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , url , 9032 , III1iII1I1ii + 'icon.png' )
def oO0oOo ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  if '=' in I1111i :
   pass
  else :
   Ii111iIi1iIi ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def IIiIiii ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  if '=' in I1111i :
   pass
  else :
   Ii111iIi1iIi ( I1111i , url , 222 , III1iII1I1ii + 'icon.png' )
   if 71 - 71: I11i + o000O0o . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
   if 91 - 91: o0o00Oo0O - Ii1IIIi1 % I1111IIi
   if 46 - 46: iiiiiiii1 / oOo0O0Ooo . O0OOOoOoo0 % oO0o / Ii
   if 13 - 13: I1111IIi % I11i + o000O0o + I1111IIi + Ii - Ii1I
   if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def iiIi1111iiI1 ( ) :
 iIIII = IIII ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 OOooOoooOoOo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'Daily' in I1111i :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 9008 , O0o0Oo )
def o00oo00 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0o0Oo )
def o0oO0O ( url ) :
 Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 Ii111iIi1iIi ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  Ii111iIi1iIi ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , O0o0Oo )
  if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if '.m3u' in o0OIiII :
   oO0oo ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + o0OIiII ) , 9011 , III1iII1I1ii + 'disclose.png' )
def O0Ooo0o ( url ) :
 iIIII = cloudflare . source ( url )
 OOooOoooOoOo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  Ii111iIi1iIi ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 42 - 42: iI11I1II1I1I / Ii1IIIi1 . o0o00Oo0O . ooOOOoO
def o0OooOOOOOO ( ) :
 iIIII = IIII ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  if 'category' in o0OIiII :
   oO0oo ( I1111i , 'http://www.disclose.tv/' + o0OIiII , 7010 , III1iII1I1ii + 'disclose.png' )
   if 12 - 12: Ii - iI11I1II1I1I * O0OOOoOoo0 * ii1ii11IIIiiI
   if 19 - 19: o0o00Oo0O + Ooo00oOo0oOo + I11i
def oO0IIi11IiiiI11i ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in OOooOoooOoOo :
  oO0oo ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  oO0oo ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 68 - 68: Ooo00oOo0oOo + Ii1IIIi1 * Ooo00oOo0oOo . O0OOOoOoo0 % ooOOOoO - ii
  if 60 - 60: oO0o % Ii
def iiIIII11iIii ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  if 'http' in url :
   Ii111iIi1iIi ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , I1111i in o0OOOO00O0Oo :
  Ii111iIi1iIi ( I1111i , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in ooOoO00 :
  Ii111iIi1iIi ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 95 - 95: O0OOOoOoo0 + o000O0o % Ooo00oOo0oOo * o000O0o
  if 58 - 58: OOooOOo . I11i + Ooo00oOo0oOo
def iiIi1 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
def Oo0o0OOo0Oo0 ( name , url , img ) :
 oO0OOoo0OO = IIII ( url )
 O00o = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOoO = len ( O00o )
 if 54 - 54: Ooo00oOo0oOo
 if 26 - 26: iiiiiiii1 % ii . I1111IIi * iiiiiiii1 + IIiIiII11i - Ii1I
 if oOoO == 1 :
  for i1IIIii in O00o :
   i1IIIii = i1IIIii . replace ( 'player' , 'watch' )
   I1I111i = i1IIIii + '&fv=&sou='
   OOooOOoO0 = IIII ( I1I111i )
   Ii11i = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( OOooOOoO0 )
   for I1iii in Ii11i :
    O00 = False
    Resolve ( I1iii )
    if 27 - 27: ii1ii11IIIiiI . OOooOOo / ii
 elif oOoO > 1 :
  if 18 - 18: ooOoO0O00 . oOo0O0Ooo
  for i1IIIii in O00o :
   Oooo0O = IIII ( i1IIIii )
   oOOo0O0Oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oooo0O )
   III1I1I1iiIi = oOOo0O0Oo
   III1I1I1iiIi = ( str ( III1I1I1iiIi ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + III1I1I1iiIi
   Ii111iIi1iIi ( 'DOUBLE LINK' , III1I1I1iiIi , 424 , '' )
   if 30 - 30: OOooOOo - Ii
   for url in oOOo0O0Oo :
    oO0oo ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ii11I1 = Google . resolve ( url )
    except :
     pass
    try :
     oO0OOOO00o = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ii11I1 ) )
     for i1Ii1I , O0O0o0o0oo0O in oO0OOOO00o :
      if 30 - 30: I1111IIi / oOo0O0Ooo / ooOoO0O00 - o0o00Oo0O . ooOOOoO - iiiiiiii1
      HD_URLS . append ( i1Ii1I )
      SD_URLS . append ( O0O0o0o0oo0O )
    except :
     pass
 else :
  pass
  if 95 - 95: I1111IIi - O0OOOoOoo0
def I1ii ( ) :
 if 82 - 82: OOooOOo . ooOOOoO
 if 73 - 73: I1111IIi
 oO0oo ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 25 - 25: O0OOOoOoo0
 oO0oo ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . ooOOOoO - I1ii11iIi11i . Ii
def IIIII11II1 ( ) :
 iIIII = IIII ( 'http://cnfstudio.com/' )
 OOooOoooOoOo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , 'http://cnfstudio.com/genre/' + o0OIiII , 7003 , III1iII1I1ii + 'icon.png' )
  if 75 - 75: oO0o - OOooOOo - ooOoO0O00 % I1ii11iIi11i - IIiIiII11i
iI111I11I1I1 = xbmcgui . Dialog ( )
if 61 - 61: I1ii11iIi11i + ii / Ii
I11OoooO = '{UN},' ; i1IIi11 = '{IG},' ; oOIIIII11 = '{PL},' ; i1i1 = '{LO},' ; IiiIi = '{LP},' ; IIiiIiI = '{HA},' ; I1O0 = '{XD},' ; oO0oo0oOO = '{TA},' ; iiII1iIi1ii1i = '{DP},' ; i11IiI1 = '{JT},' ; O0oO00oOO00O = '{JJ},' ; Oo0Oo0o00oO = '{MM},' ; oO0o0OooOO0 = '{FQ},' ; iiIi = '{HH},'
if 89 - 89: ii % Ii + I1111IIi
def iI1II1iIiiiI ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 iiIIi11I1ii = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 iiIIi11I1ii = iiIIi11I1ii
 for url in iiIIi11I1ii :
  oO0oo ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 14 - 14: o000O0o + I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . iiiiiiii1
def OoO0II1iiIiI1 ( url ) :
 if 10 - 10: Ii % o000O0o * ii1ii11IIIiiI % I1ii11iIi11i
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  O00O0oOO00O00 = url + '&fv=&sou='
  O00O0oOO00O00 = O00O0oOO00O00 . replace ( 'player' , 'watch' )
  oO0o0ooooo = IiIi1I1IiI1II1 ( O00O0oOO00O00 )
  iii1 = IiIi1I1IiI1II1 ( url )
  if 26 - 26: o000O0o + I1ii11iIi11i
  if 71 - 71: oOo0O0Ooo . iiiiiiii1
def IiIi1I1IiI1II1 ( url ) :
 if 43 - 43: Ii1I * o000O0o
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  O0OoOOO00 ( url )
  if 1 - 1: oO0o * iiiiiiii1 + O0OOOoOoo0 . Ooo00oOo0oOo / iiiiiiii1
  if 91 - 91: ooOOOoO + Ii1IIIi1 - I1ii11iIi11i % OOooOOo . ii1ii11IIIiiI
def oO0OO ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , III1iII1I1ii + 'LocalM3U.png' , Ooo , '' )
 Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , III1iII1I1ii + 'RemoteM3U.png' , Ooo , '' )
 if 89 - 89: Ooo00oOo0oOo - I1111IIi + OOooOOo % I11i % ooOOOoO - Ii
def i1I111Iii ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  oOoo0 = open ( O0OoO000O0OO , 'r' )
  for i11I in oOoo0 :
   ii1III11 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , o0OIiII in ii1III11 :
    Ii111iIi1iIi ( I1111i , o0OIiII , 222 , III1iII1I1ii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 28 - 28: oO0o - iiiiiiii1 - Ooo00oOo0oOo % Ooo00oOo0oOo / o0o00Oo0O
def oooo0OoOo ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = O0iIiIIIIIii ( url )
  OOooOoooOoOo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , url in OOooOoooOoOo :
   url = ( url ) . strip ( )
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 69 - 69: Ooo00oOo0oOo
  if 95 - 95: iI11I1II1I1I
def ii111iI1iIi1 ( ) :
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 OOooOoooOoOo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for o0OIiII in OOooOoooOoOo :
  o0OIiII = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + o0OIiII
 I1111i = 'plugin.video.GenieTv'
 if 75 - 75: o000O0o - oO0o
 oo0Ii111ii1 ( o0OIiII , I1111i )
 if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + ooOOOoO % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = IIII ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 OOooOoooOoOo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for o0OIiII in OOooOoooOoOo :
  o0OIiII = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + o0OIiII
 I1111i = 'repository.GenieTv'
 if 79 - 79: ii + Ii1IIIi1 * I1111IIi
 oo0Ii111ii1 ( o0OIiII , I1111i )
 if 63 - 63: iiiiiiii1 % oOo0O0Ooo . o000O0o - iiiiiiii1 / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % Ooo00oOo0oOo / Ii1IIIi1 % o0o00Oo0O
def OOI1iI1ii1II ( ) :
 OO = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , OO )
 if OoOoO == 0 :
  o0O0OOooO ( )
 if OoOoO == 1 :
  i1II111i1IIii ( )
  if 50 - 50: oOo0O0Ooo % Ii - oOo0O0Ooo * ii1ii11IIIiiI / O0OOOoOoo0 / o0o00Oo0O
  if 31 - 31: IIiIiII11i . ii + oO0o + I11i . oOo0O0Ooo . IIiIiII11i
  if 3 - 3: Ii1IIIi1 / I1111IIi * O0OOOoOoo0 - o0o00Oo0O + oOo0O0Ooo / O0OOOoOoo0
  if 19 - 19: ooOoO0O00 % IIiIiII11i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
O00OO0oO = 'https://addons.tvaddons.ag/'
if 30 - 30: Ii % oO0o * IIiIiII11i - o0o00Oo0O . Ii1I * iI11I1II1I1I
def i1II111i1IIii ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 II1ii = 'https://addons.tvaddons.ag/search/?keyword=' + I1iiioOO0OO0O
 oO0OOoo0OO = IIII ( II1ii )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , OoO , I1111i in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , o0OIiII , 10054 , 'https://addons.tvaddons.ag/' + OoO , Ooo , '' )
  if 48 - 48: I11i + Ii1I / Ii1I
  if 80 - 80: ii
def o0O0OOooO ( ) :
 oO0OOoo0OO = IIII ( O00OO0oO )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  if 'Repositories' in I1111i :
   pass
  elif 'Services' in I1111i :
   pass
  elif 'International' in I1111i :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , o0OIiII , 10053 , 'https://addons.tvaddons.ag/' + o00O0O , Ooo , '' )
   if 65 - 65: Ooo00oOo0oOo * ooOoO0O00 . ii % iiiiiiii1
   if 87 - 87: Ii * IIiIiII11i - ooOOOoO % ii
def Addon ( url ) :
 oO0OOoo0OO = IIII ( url )
 o0oO = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 OOooOoooOoOo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  if 'Please' in I1111i :
   pass
  else :
   I1I1i1I ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , Ooo , '' )
 for url in o0oO :
  Iii1I1I11iiI1 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , Ooo , '' )
  if 35 - 35: I1111IIi - ooOoO0O00 / O0OOOoOoo0
  if 13 - 13: OOooOOo - oO0o * ii
def iIi1i111ii1II11ii ( url , name ) :
 oO0OOoo0OO = IIII ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in OOooOoooOoOo :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
   try :
    os . remove ( o00O0 )
   except :
    pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oOO0O00Oo0O0o
   print '======================================='
   extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
   I1iIIiiIIi1i ( )
   if 21 - 21: Ii1IIIi1
def oo0Ii111ii1 ( url , name ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 I1iIIiiIIi1i ( )
 if 79 - 79: oO0o / o000O0o - ooOoO0O00 + ooOoO0O00 - O0OOOoOoo0 + O0OOOoOoo0
def I1iIIiiIIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 67 - 67: oO0o * oO0o / ii
 if 79 - 79: I11i % iI11I1II1I1I / IIiIiII11i / ooOOOoO / ooOOOoO + o0o00Oo0O
def ii11oOo0OO0 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , OoO , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , url , 1007 , OoO )
def OoOiIiIi1i1ii11 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , OoO , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 1006 , OoO )
  if 86 - 86: I1111IIi * iiiiiiii1 - iiiiiiii1 . oOo0O0Ooo
  if 69 - 69: Ii - iI11I1II1I1I / ooOOOoO / IIiIiII11i
def IiIII1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , Iiiiii111i1ii , i1II1 , name in OOooOoooOoOo :
  if 'http' in url :
   if '.php' in url :
    oOoO00O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oOOoo0Oo ) )
    for i11I in oOoO00O :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iI1111i ( name , url , 1016 , iconimage , i1II1 , Iiiiii111i1ii )
   else :
    if 'youtube' in url :
     oOoO00O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oOOoo0Oo ) )
     for i11I in oOoO00O :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I1ii1iI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , i1II1 , Iiiiii111i1ii )
    else :
     oOoO00O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oOOoo0Oo ) )
     for i11I in oOoO00O :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I1ii1iI ( name , url , 222 , iconimage , i1II1 , Iiiiii111i1ii )
     O0oO0 ( 'movies' , 'INFO' )
  else :
   O00OOOO0o ( url , iconimage , name )
   if 86 - 86: I11i % oO0o + Ii1I
 else :
  OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , OoO , name in OOooOoooOoOo :
   if 'http' in url :
    if '.php' in url :
     oO0oo ( name , url , 1016 , OoO )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      Ii111iIi1iIi ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OoO )
     else :
      oOoO00O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oOOoo0Oo ) )
      for i11I in oOoO00O :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      Ii111iIi1iIi ( name , url , 222 , OoO )
      O0oO0 ( 'movies' , 'INFO' )
   else :
    O00OOOO0o ( url , OoO , name )
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 69 - 69: O0OOOoOoo0
def O00OOOO0o ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 II1i = ( url ) . replace ( ooOo0O0 , 'http' ) . replace ( Oo0Ii , '.com' ) ;
 Oo0ooo0 = ( II1i ) . replace ( OooO00O0OO0oo , 'a' ) . replace ( I1IiiiiI1i1I , 'b' ) . replace ( I11i1I1 , 'c' ) . replace ( iI1I1I1iiI1i , 'd' ) . replace ( oOIIIII11 , 'e' ) . replace ( i11IiI1 , 'f' ) ;
 I11i1IiiI = ( Oo0ooo0 ) . replace ( I1ii11IiI1I , 'g' ) . replace ( IIiiIiI , 'h' ) . replace ( oooooOOo0Oo , 'i' ) . replace ( iiIIIIiI11II1 , 'j' ) . replace ( ooOooO , 'k' ) . replace ( oooo , 'l' ) ;
 OOoo = ( I11i1IiiI ) . replace ( OO000oOoOo000 , 'm' ) . replace ( o0O0o0ooo0 , 'n' ) . replace ( iIo0O000O00o , 'o' ) . replace ( iiooo , 'p' ) . replace ( ii111I1I1I , 'q' ) . replace ( iIIiIi1IiI1 , 'r' ) ;
 Oo0O = ( OOoo ) . replace ( Iii1I1III11 , 's' ) . replace ( IiII1111I , 't' ) . replace ( i1ii1IiIiIii , 'u' ) . replace ( OOo0ooOOOo0O0 , 'v' ) . replace ( ooI1 , 'w' ) . replace ( i1Iii1i1II1 , 'x' ) ;
 O0o00OoooO = ( Oo0O ) . replace ( IiI1i1iI , 'y' ) . replace ( iIIi , 'z' ) . replace ( I11OoooO , '.' ) . replace ( i1IIi11 , '(' ) . replace ( i1i1 , ')' ) . replace ( IiiIi , '/' ) ;
 iIIIII = ( O0o00OoooO ) . replace ( O0o0 , '1' ) . replace ( iiIIii111Ii , '2' ) . replace ( iiiII , '3' ) . replace ( oO0oo0oOO , '4' ) . replace ( iiII1iIi1ii1i , '5' ) . replace ( IiiiiiiI111i , '6' ) ;
 Oo0Ooo = ( iIIIII ) . replace ( O0oO00oOO00O , '7' ) . replace ( Oo0Oo0o00oO , '8' ) . replace ( oO0o0OooOO0 , '9' ) . replace ( iiIi , '0' ) . replace ( OOoOo0O0 , ':' ) . replace ( I1o0 , '%' ) ;
 url = ( Oo0Ooo ) . replace ( O0oo0o0o0o , '-' ) . replace ( I1O0 , '_' ) ;
 Ii111iIi1iIi ( name , url , 222 , iconimage ) ;
 if 42 - 42: Ooo00oOo0oOo - Ii % Ooo00oOo0oOo - I1111IIi * o0o00Oo0O / IIiIiII11i
 if 5 - 5: I1ii11iIi11i
def oOoOo0o0 ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for o0OIiII , OoO , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 1007 , OoO )
def II1Iiiii ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , OoO , I1111i in OOooOoooOoOo :
  oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 1006 , OoO )
  if 70 - 70: ii / o000O0o - oO0o % ii
def iI1Iii1i11 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0iII11 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0iII11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0iII11 )
 if 30 - 30: I1ii11iIi11i + ooOOOoO % Ii * ooOoO0O00 + oOo0O0Ooo % o000O0o
 if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % I1111IIi
def iiO0O0o0oO0O00 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in OOooOoooOoOo :
  if '-dir-' in I1111i :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   oO0oo ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 78 - 78: Ii1I + ii - oOo0O0Ooo * OOooOOo * ii1ii11IIIiiI
def I1I1i1 ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 Ii1Ii = ( 'http://afewbitsmore.com/' )
 OOooOoooOoOo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   oO0oo ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , Ii1Ii + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in I1111i :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Ii1Ii + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in I1111i :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Ii1Ii + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) , Ii1Ii + url , 1012 , III1iII1I1ii + 'music.png' )
def iII ( url ) :
 oO0OOoo0OO = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 73 - 73: Ooo00oOo0oOo - Ii1I / ii - oO0o / oOo0O0Ooo
def I111II1iIIII ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 Ii1Ii = url
 OOooOoooOoOo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oO0oo ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , Ii1Ii + url , 1011 , III1iII1I1ii + 'music.png' )
def Ooo00oo0ooO0 ( ) :
 iIIII = O0iIiIIIIIii ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 OOooOoooOoOo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for o0OIiII , o00O0O , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , ( 'http://www.cyn.net/music/' + o0OIiII ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def i1ii1i1 ( url , img ) :
 iIIII = O0iIiIIIIIii ( url )
 ii11I1 = url
 img = img
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( ii11I1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 42 - 42: Ooo00oOo0oOo
def iIi ( url ) :
 iIIII = O0iIiIIIIIii ( url )
 ii11I1 = url
 OOooOoooOoOo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in OOooOoooOoOo :
  if '[VID]' in type :
   Ii111iIi1iIi ( ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , ii11I1 + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   iIi ( ii11I1 + url )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: iI11I1II1I1I % oOo0O0Ooo . o0o00Oo0O
 if 13 - 13: IIiIiII11i % ooOoO0O00 - OOooOOo + ii1ii11IIIiiI
def o0O0oO0 ( ) :
 IIIiI1iIIII = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iiioOO0OO0O = I1i11II . lower ( )
 o0OIiII = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ii11I1 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 59 - 59: ii + I1111IIi % I11i - OOooOOo . oOo0O0Ooo
 oO0OOoo0OO = OOO00O ( o0OIiII )
 O0 = OOO00O ( ii11I1 )
 ii1ii1ii = OOO00O ( o0ooOo0OOOO0o )
 if 42 - 42: I1111IIi
 if oO0OOoo0OO != 'Failed' :
  OOooOoooOoOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0OOoo0OO )
  for I1111i in OOooOoooOoOo :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( I1111i + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OIiII + I1111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 70 - 70: I11i / Ii1IIIi1 + Ooo00oOo0oOo % oOo0O0Ooo % I1ii11iIi11i + oO0o
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  o0OOOO00O0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oO0OOoo0OO )
  for I1111i in o0OOOO00O0Oo :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( I1111i + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ii11I1 + I1111i ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 80 - 80: o000O0o
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if I1i11II in I1111i . lower ( ) :
    oO0oo ( ( I1111i + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0ooOo0OOOO0o + I1111i ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 12 - 12: ooOOOoO
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: ii
    if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
    if 46 - 46: o0o00Oo0O % ii
    if 22 - 22: ii1ii11IIIiiI + ii - OOooOOo - oO0o * I1111IIi - Ooo00oOo0oOo
    if 99 - 99: iiiiiiii1 / oOo0O0Ooo . ooOOOoO - ooOOOoO * oOo0O0Ooo
    if 24 - 24: Ii1IIIi1 * oO0o - Ooo00oOo0oOo / iI11I1II1I1I - I1ii11iIi11i . o000O0o
OO000oOoOo000 = '{SF},' ; o0O0o0ooo0 = '{IF},' ; iIo0O000O00o = '{PW},' ; iiiII = '{AM},' ; iiooo = '{GF},' ; ii111I1I1I = '{DD},' ; iIIiIi1IiI1 = '{UO},' ; Iii1I1III11 = '{LE},' ; i1ii1IiIiIii = '{ZY},' ; OOo0ooOOOo0O0 = '{UE},' ; ooI1 = '{PE},' ; i1Iii1i1II1 = '{JE},' ; IiI1i1iI = '{TH},' ; iIIi = '{LK},'
if 2 - 2: iiiiiiii1 - o0o00Oo0O - Ii1I / Ii1IIIi1 * OOooOOo
if 26 - 26: Ii1I + I1111IIi - Ooo00oOo0oOo + O0OOOoOoo0 % o000O0o
def I1I1i ( ) :
 iIIII = IIII ( 'http://www.iwatchseries.me/tv-list/' )
 OOooOoooOoOo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 8021 , III1iII1I1ii + 'iwatch.png' )
def O0000oOo0OO ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , ooooOoO0O in OOooOoooOoOo :
  oO0oo ( I1111i + ooooOoO0O , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def oo00O000 ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o0o00OO0oOoO ( url )
def o0o00OO0oOoO ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 o0OOOO00O0Oo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( 'VidSpot - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in o0OOOO00O0Oo :
  Ii111iIi1iIi ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   Ii111iIi1iIi ( 'TheVideo - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 16 - 16: oO0o + Ooo00oOo0oOo * ooOoO0O00 / Ii1I
def ooO0O0OOO ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 OOooOoooOoOo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 1021 , III1iII1I1ii + 'anime.png' )
  if 2 - 2: Ii / oO0o + iiiiiiii1 - Ii1I * oO0o
  if 3 - 3: oO0o % I11i % o000O0o . Ii1I . Ii1I
def IiI1i1111iI1i ( ) :
 iIIII = IIII ( 'http://www.animetoon.org/cartoon' )
 OOooOoooOoOo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for o0OIiII , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , o0OIiII , 1002 , III1iII1I1ii + 'anime.png' )
  if 85 - 85: iI11I1II1I1I + ooOOOoO - IIiIiII11i * O0OOOoOoo0 * ii1ii11IIIiiI
  if 17 - 17: o000O0o . Ooo00oOo0oOo - I1ii11iIi11i * iI11I1II1I1I * iiiiiiii1
  if 39 - 39: ii . Ooo00oOo0oOo
def O0iiIi1iIiI ( url ) :
 iIIII = IIII ( url )
 o0OOOO00O0Oo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in o0OOOO00O0Oo :
  O0oO00oOOooO = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  oO0oo ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 OOooOoooOoOo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in OOooOoooOoOo :
  oO0oo ( I1111i , url , 1003 , O0oO00oOOooO )
 xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIi1iii ( url , IMAGE ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in OOooOoooOoOo :
  print I1111i + '     ' + url
  if 'easy' in url :
   ii1Ii ( url )
  elif 'playpanda' in url :
   ii1Ii ( url )
   if 41 - 41: Ii1I % Ii1I + O0OOOoOoo0 . ii1ii11IIIiiI % I1111IIi * iiiiiiii1
  xbmcplugin . addSortMethod ( I11iii1Ii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1Ii ( url ) :
 iIIII = IIII ( url )
 OOooOoooOoOo = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in OOooOoooOoOo :
  Ii111iIi1iIi ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 57 - 57: ooOOOoO . I1111IIi . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
  if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
def o000 ( url ) :
 OOoOO0oo0ooO = urllib2 . Request ( url )
 OOoOO0oo0ooO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO . add_header ( 'referer' , url )
 O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
 O00O0oOO00O00 = O0o0O00Oo0o0 . read ( )
 O0o0O00Oo0o0 . close ( )
 return O00O0oOO00O00
 if 8 - 8: I1ii11iIi11i
def O0iIiIIIIIii ( url ) :
 OOoOO0oo0ooO = urllib2 . Request ( url )
 OOoOO0oo0ooO . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
 O00O0oOO00O00 = O0o0O00Oo0o0 . read ( )
 O0o0O00Oo0o0 . close ( )
 return O00O0oOO00O00
 if 22 - 22: iiiiiiii1 % OOooOOo / I11i
def oO0O ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OO0 = ( '%s%s' % ( OoOoO00OOoOOOo0 , url ) )
 O00O0oOO00O00 = O0iIiIIIIIii ( url )
 OOooOoooOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00O0oOO00O00 )
 for url , OoO , I1111i in OOooOoooOoOo :
  Ii111iIi1iIi ( '%s' % ( '[COLOR' + iiI1IiI + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , OoO )
  if 31 - 31: ii % Ii - IIiIiII11i * Ii
def O0OoOOO00 ( url ) :
 if 82 - 82: o0o00Oo0O / o000O0o + ii1ii11IIIiiI
 I11II1i1I11I1 = open ( oO0Oo , "a" )
 I11II1i1I11I1 . write ( 'url="' + url + '"\n' )
 I11II1i1I11I1 . close
 if 11 - 11: iiiiiiii1 - ii
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 import urlresolver
 try : oo000oOo0 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1111i ) )
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oo000oOo0 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def O0OoO00 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  oooOO0oo0Oo00 = '.mp4'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.mkv' in url :
  oooOO0oo0Oo00 = '.mkv'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.mp3' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.avi' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.mov' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.mpeg' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.mpg' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 elif '.flv' in url :
  oooOO0oo0Oo00 = '.mp3'
  OO = [ '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , '[COLOR' + iiI1IiI + ']DOWNLOAD[/COLOR]' ]
  OoOoO = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Play/Download[/COLOR]' , OO )
  if OoOoO == 0 :
   O0OoOOO00 ( url )
  if OoOoO == 1 :
   Oo0ooo00o0O0 ( url , name , oooOO0oo0Oo00 )
 else :
  O0OoOOO00 ( url )
def Oo0ooo00o0O0 ( url , name , cat ) :
 II1I1iI1i1IiI ( )
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( II ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , file )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def II1I1iI1i1IiI ( ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( II ) )
 if not os . path . exists ( II ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def IIii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oo000oOo0 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 100 - 100: Ii - iiiiiiii1 + o000O0o * ii + o0o00Oo0O
def OOOOo0o00OO0000 ( url ) :
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oo000oOo0 . play ( url ) . strip ( )
 except : pass
 if 66 - 66: Ii1I . I1ii11iIi11i / Ii1I + Ii1I . IIiIiII11i % oO0o
def ooo0oooO ( url ) :
 oo000oOo0 = xbmc . Player ( iIiI1I1Ii ( ) )
 import urlresolver
 O0O0Ooo0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oo000oOo0 . play ( O0O0Ooo0 )
 xbmc . sleep ( 1 )
 oo000oOo0 . play ( url )
 if 34 - 34: Ooo00oOo0oOo - IIiIiII11i - I11i + ii1ii11IIIiiI + I1111IIi
 if 70 - 70: ii + oO0o * I1ii11iIi11i
def iIiI1I1Ii ( ) :
 try :
  IiIi11iI1 = getSet ( "core-player" )
  if ( IiIi11iI1 == 'DVDPLAYER' ) : IiI1I1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiIi11iI1 == 'MPLAYER' ) : IiI1I1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiIi11iI1 == 'PAPLAYER' ) : IiI1I1 = xbmc . PLAYER_CORE_PAPLAYER
  else : IiI1I1 = xbmc . PLAYER_CORE_AUTO
 except : IiI1I1 = xbmc . PLAYER_CORE_AUTO
 return IiI1I1
 return True
 if 16 - 16: Ii1I / Ii1IIIi1 + I11i % Ii % o000O0o - ooOOOoO
def oO0oo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iioo0o0OoOOO = [ ]
  iioo0o0OoOOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = True )
 return i1ii
 if 37 - 37: o000O0o * ooOOOoO * Ii1IIIi1 + OOooOOo / Ii
def IIiii11ii1i ( name , url , mode , iconimage , fanart , description ) :
 if 68 - 68: ii * Ii1IIIi1
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = True )
 return i1ii
 if 86 - 86: I11i / OOooOOo
def Ii111iIi1iIi ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iioo0o0OoOOO = [ ]
  iioo0o0OoOOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = False )
 return i1ii
 if 40 - 40: ii1ii11IIIiiI
 if 62 - 62: iiiiiiii1 / o000O0o
 if 74 - 74: ii1ii11IIIiiI % I1111IIi / I1111IIi - iI11I1II1I1I - IIiIiII11i + o000O0o
 if 92 - 92: Ii1IIIi1 % I1111IIi
 if 18 - 18: iiiiiiii1 + I1111IIi / o000O0o / Ooo00oOo0oOo + iI11I1II1I1I % O0OOOoOoo0
 if 94 - 94: Ii1IIIi1
def OO0O000 ( heading , announce ) :
 class iI11IiiI1 ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; iiO0o0O0oo0o = oooOo0OOOoo0 . read ( )
   except : iiO0o0O0oo0o = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iiO0o0O0oo0o ) )
   return
 iI11IiiI1 ( )
 iI11IiiI1 ( )
 if 83 - 83: Ooo00oOo0oOo / iI11I1II1I1I
def Ii1I1Ii ( ) :
 OO0O000 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 68 - 68: I1111IIi - OOooOOo . Ii + I11i
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
 if 33 - 33: Ii1IIIi1 . I1ii11iIi11i
 if 89 - 89: ii1ii11IIIiiI + ooOoO0O00 - O0OOOoOoo0 + iiiiiiii1 . IIiIiII11i
 if 85 - 85: iI11I1II1I1I - ooOOOoO * I1ii11iIi11i . Ooo00oOo0oOo + I1111IIi
def I1iIIiiIIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . ii1ii11IIIiiI / ii1ii11IIIiiI
 if 43 - 43: oOo0O0Ooo
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + ooOOOoO * Ii1IIIi1 / Ooo00oOo0oOo
 if 18 - 18: iiiiiiii1
 if 92 - 92: oO0o % iI11I1II1I1I / O0OOOoOoo0 * ii1ii11IIIiiI . ooOoO0O00 + Ooo00oOo0oOo
 if 24 - 24: O0OOOoOoo0 . ii1ii11IIIiiI * O0OOOoOoo0 % Ii . Ii + ooOoO0O00
 if 64 - 64: iI11I1II1I1I / O0OOOoOoo0 / I1ii11iIi11i - Ii1I
 if 100 - 100: O0OOOoOoo0 + ooOoO0O00 * oO0o
 if 64 - 64: Ooo00oOo0oOo * Ii . I1ii11iIi11i
 if 52 - 52: I1ii11iIi11i / iiiiiiii1 / ii1ii11IIIiiI - I11i / ii1ii11IIIiiI
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
 if 72 - 72: ii . I11i + o0o00Oo0O
 if 46 - 46: OOooOOo * Ii1IIIi1 / Ooo00oOo0oOo + I1ii11iIi11i + O0OOOoOoo0
 if 95 - 95: I11i - ooOOOoO
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
 if 19 - 19: OOooOOo . o000O0o . ii
 if 79 - 79: o000O0o * iiiiiiii1 * oOo0O0Ooo * Ii1I / Ii1I
 if 62 - 62: iiiiiiii1 * ooOOOoO % Ii1I - ooOoO0O00 - Ii1I
 if 24 - 24: o000O0o
 if 71 - 71: O0OOOoOoo0 - ooOoO0O00
def oOO00o0 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + Iii11I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 45 - 45: oO0o * ii / o0o00Oo0O . I1111IIi / OOooOOo
def oO0I1ii11i1 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + IIi1iII11III ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 35 - 35: Ii1IIIi1 % I1ii11iIi11i
def oOo0000oo ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + I11Iii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 73 - 73: Ii * Ii1I . Ii1IIIi1 % oOo0O0Ooo - oOo0O0Ooo . OOooOOo
def OOooiIi1 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + iiiIIIIiI1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 13 - 13: Ii1IIIi1 . oO0o
def O00oO0oOOOOOO ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + Oo0ooo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 1 - 1: ii * iI11I1II1I1I / Ii1I * Ii1IIIi1
def I1i1I1i1Ii ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + oooOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 31 - 31: Ii / O0OOOoOoo0 * Ii % I1111IIi * I1ii11iIi11i + ii
def iIII1iiiiI1Ii11 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + O0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 13 - 13: oO0o * I1111IIi + I1ii11iIi11i - O0OOOoOoo0
def i11IIii ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + iiIiI11Iii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 56 - 56: I1ii11iIi11i
def oOOOOoo000Ooo ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + iiii1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 42 , O0Oo000 , i1II1 , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 28 - 28: ii % Ii1IIIi1
def oOooO0 ( url ) :
 O00O0oOO00O00 = IIII ( str ( I1I1IiI1 ) + IIIIiiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOooOoooOoOo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O00O0oOO00O00 )
 for I1111i , url , O0Oo000 , i1II1 , oo0o0O0Oooooo in OOooOoooOoOo :
  Iii1I1I11iiI1 ( I1111i , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , oo0o0O0Oooooo )
 O0oO0 ( 'movies' , 'MAIN' )
 if 68 - 68: oO0o / I1111IIi % IIiIiII11i + I1ii11iIi11i + o0o00Oo0O % Ii1I
 if 53 - 53: OOooOOo % iiiiiiii1 . oO0o + oOo0O0Ooo / Ii1I
 if 76 - 76: Ii1I . iI11I1II1I1I - Ii / Ii1I - I11i
 if 95 - 95: Ii1IIIi1
 if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - ii1ii11IIIiiI
 if 30 - 30: I1111IIi % Ooo00oOo0oOo + Ooo00oOo0oOo * ii - Ii1I
 if 69 - 69: Ii1I + oO0o / o0o00Oo0O + IIiIiII11i / Ii
 if 48 - 48: ii / oOo0O0Ooo
 if 19 - 19: o000O0o * Ii1I - iiiiiiii1 * Ii + Ii1IIIi1
def OoOoO0O ( ) :
 try :
  if os . path . exists ( I11i1 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( I11i1 ) :
     o0OoOO0 = 0
     o0OoOO0 += len ( oo0O )
     if o0OoOO0 > 0 :
      for oooOo0OOOoo0 in oo0O :
       os . unlink ( os . path . join ( Iii11III1I11 , oooOo0OOOoo0 ) )
  ooo = os . path . join ( O0O , "Textures13.db" )
  os . unlink ( ooo )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 67 - 67: ii1ii11IIIiiI
 if 63 - 63: I1111IIi
 if 94 - 94: ooOoO0O00 % ooOOOoO % Ii1I - ooOOOoO * iI11I1II1I1I + iI11I1II1I1I
 if 98 - 98: I11i % iiiiiiii1 - I11i * O0OOOoOoo0 % I1111IIi * O0OOOoOoo0
 if 31 - 31: ooOOOoO
 if 46 - 46: I11i + Ii1I * I11i + Ii + ii1ii11IIIiiI / IIiIiII11i
 if 5 - 5: o0o00Oo0O + ii1ii11IIIiiI * I1ii11iIi11i
 if 9 - 9: Ooo00oOo0oOo . ii . o000O0o * Ii1I
def iIi1Ii1IIiI ( title , message , times = 2000 , icon = O0o0Oo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 80 - 80: I1111IIi + Ii1IIIi1 . I1111IIi + o000O0o
def I1IiiiiI ( url ) :
 OoI11II = os . path . join ( oO , 'addon_data' )
 Iii11IiIi = [
 ( OoI11II ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OoI11II , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OoI11II , 'plugin.video.itv' , 'Images' ) ) ]
 if 94 - 94: o000O0o * ii - O0OOOoOoo0 - I1111IIi
 oOooOoOoo = 0
 if 2 - 2: iI11I1II1I1I . I1ii11iIi11i * ii1ii11IIIiiI % oO0o
 for i11I in Iii11IiIi :
  if os . path . exists ( i11I ) and not i11I in [ oOo0oooo00o , OoI11II ] :
   for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( i11I ) :
    o0OoOO0 = 0
    o0OoOO0 += len ( oo0O )
    if o0OoOO0 > 0 :
     for oooOo0OOOoo0 in oo0O :
      if not oooOo0OOOoo0 in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( Iii11III1I11 , oooOo0OOOoo0 ) )
       except :
        pass
      else : oOOo0O00o ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for Oo0 in Oo00OO0 :
      try :
       shutil . rmtree ( os . path . join ( Iii11III1I11 , Oo0 ) )
       oOooOoOoo += 1
       oOOo0O00o ( "[Success] cleared %s files from %s" % ( str ( o0OoOO0 ) , os . path . join ( i11I , Oo0 ) ) )
      except :
       oOOo0O00o ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , Oo0 ) )
  else :
   for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( i11I ) :
    for Oo0 in Oo00OO0 :
     if 'cache' in Oo0 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Iii11III1I11 , Oo0 ) )
       oOooOoOoo += 1
       oOOo0O00o ( "[Success] wiped %s " % os . path . join ( i11I , Oo0 ) )
      except :
       oOOo0O00o ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , Oo0 ) )
       if 55 - 55: I11i
 iIi1Ii1IIiI ( oo0o0O00 , 'Clear Cache: Removed %s Files' % oOooOoOoo )
 if 58 - 58: I11i / I11i - O0OOOoOoo0 - IIiIiII11i . OOooOOo
 if 100 - 100: Ii1I + Ooo00oOo0oOo + IIiIiII11i . ii1ii11IIIiiI / Ii1I
 if 76 - 76: ooOOOoO + ii1ii11IIIiiI - O0OOOoOoo0 * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: iiiiiiii1 + IIiIiII11i . o0o00Oo0O - ii1ii11IIIiiI / ii . I1111IIi
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
 if 29 - 29: Ii1I
def IiI1iI1IiiIi1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI111iiI1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( iI111iiI1II ) :
   o0OoOO0 = 0
   o0OoOO0 += len ( oo0O )
   if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . iiiiiiii1 - ooOOOoO
   if 84 - 84: Ooo00oOo0oOo * I11i * I11i - ii1ii11IIIiiI
   if o0OoOO0 > 0 :
    if 25 - 25: Ooo00oOo0oOo + I1111IIi + oOo0O0Ooo + o0o00Oo0O * IIiIiII11i + oOo0O0Ooo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0OoOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 66 - 66: Ooo00oOo0oOo
     for oooOo0OOOoo0 in oo0O :
      os . unlink ( os . path . join ( Iii11III1I11 , oooOo0OOOoo0 ) )
     for Oo0 in Oo00OO0 :
      shutil . rmtree ( os . path . join ( Iii11III1I11 , Oo0 ) )
     iI111I11I1I1 = xbmcgui . Dialog ( )
     iI111I11I1I1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iI111I11I1I1 = xbmcgui . Dialog ( )
    iI111I11I1I1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 73 - 73: o000O0o . I1ii11iIi11i + I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
 if 8 - 8: ii1ii11IIIiiI . ooOOOoO - ooOoO0O00 % oO0o / Ii1IIIi1
 if 13 - 13: I1ii11iIi11i / OOooOOo . Ii1I . o000O0o
 if 31 - 31: I11i
 if 59 - 59: I1ii11iIi11i / I1ii11iIi11i
 if 87 - 87: Ii1I % OOooOOo + ooOOOoO . Ii / ooOOOoO
 if 32 - 32: ooOOOoO + O0OOOoOoo0 + Ii1I
 if 79 - 79: ooOoO0O00 / ooOOOoO
 if 81 - 81: iI11I1II1I1I
def ii1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI111iiI1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( iI111iiI1II ) :
   o0OoOO0 = 0
   o0OoOO0 += len ( oo0O )
   if 86 - 86: O0OOOoOoo0 % O0OOOoOoo0 % ii
   if 42 - 42: I1ii11iIi11i . Ooo00oOo0oOo + o0o00Oo0O / o000O0o % ii
   if o0OoOO0 > 0 :
    if 19 - 19: iiiiiiii1 / ooOOOoO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0OoOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 43 - 43: OOooOOo % ooOOOoO + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
     for oooOo0OOOoo0 in oo0O :
      os . unlink ( os . path . join ( Iii11III1I11 , oooOo0OOOoo0 ) )
     for Oo0 in Oo00OO0 :
      shutil . rmtree ( os . path . join ( Iii11III1I11 , Oo0 ) )
     iI111I11I1I1 = xbmcgui . Dialog ( )
     iI111I11I1I1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iI111I11I1I1 = xbmcgui . Dialog ( )
    iI111I11I1I1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 I1IiiiiI ( url )
 return
 if 98 - 98: I11i * I1ii11iIi11i - ooOOOoO . iiiiiiii1
 if 2 - 2: I1ii11iIi11i - iiiiiiii1 % iI11I1II1I1I
 if 88 - 88: I1111IIi - oO0o
 if 79 - 79: ii1ii11IIIiiI
 if 45 - 45: IIiIiII11i + ii1ii11IIIiiI . Ii1IIIi1 . o0o00Oo0O * ooOoO0O00 - ooOOOoO
 if 48 - 48: Ii1I + I1ii11iIi11i
 if 76 - 76: Ii1I
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . ooOOOoO
 if 51 - 51: ooOOOoO + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
 if 20 - 20: I1111IIi . Ii1IIIi1 . ooOOOoO + Ii1IIIi1 - o000O0o * Ooo00oOo0oOo
def o00ooO0 ( url , name ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iIiI1 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml.bak' )
 if os . path . exists ( iIiI1 ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
   try :
    os . remove ( iIIiiI1Ii1II )
    print '=== GenieTv - REMOVING    ' + str ( iIIiiI1Ii1II ) + '    ==='
   except :
    pass
   O00O0oOO00O00 = ii11iIi1I . http_GET ( url ) . content
   oOo00o00oO = open ( iIIiiI1Ii1II , "w" )
   oOo00o00oO . write ( O00O0oOO00O00 )
   oOo00o00oO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iIIiiI1Ii1II ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
  try :
   os . remove ( iIIiiI1Ii1II )
   print '=== GenieTv - REMOVING    ' + str ( iIIiiI1Ii1II ) + '    ==='
  except :
   pass
  O00O0oOO00O00 = ii11iIi1I . http_GET ( url ) . content
  oOo00o00oO = open ( iIIiiI1Ii1II , "w" )
  oOo00o00oO . write ( O00O0oOO00O00 )
  oOo00o00oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIIiiI1Ii1II ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 23 - 23: iI11I1II1I1I - ooOoO0O00 - O0OOOoOoo0 * O0OOOoOoo0 . O0OOOoOoo0
def O0OOo00O ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 try :
  oOo00o00oO = open ( iIIiiI1Ii1II ) . read ( )
  if 'zero' in oOo00o00oO :
   name = '0CACHE'
  elif 'tuxen' in oOo00o00oO :
   name = 'TUXENS'
  elif 'muckys' in oOo00o00oO :
   name = 'MUCKYS'
  elif 'p2p1' in oOo00o00oO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oOo00o00oO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oOo00o00oO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 18 - 18: iiiiiiii1 * IIiIiII11i
def IIIi ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 try :
  os . remove ( iIIiiI1Ii1II )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iIIiiI1Ii1II ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 61 - 61: Ii1I % Ii
 if 69 - 69: o000O0o % Ii1I / OOooOOo . o000O0o - O0OOOoOoo0
 if 74 - 74: oO0o - I11i - O0OOOoOoo0 . o0o00Oo0O % iiiiiiii1
 if 32 - 32: OOooOOo . oO0o / I1ii11iIi11i . Ii
 if 9 - 9: Ii1IIIi1 - IIiIiII11i + I1111IIi / Ooo00oOo0oOo % Ii1I
 if 17 - 17: iI11I1II1I1I - iiiiiiii1
 if 99 - 99: I1ii11iIi11i + I1111IIi % iiiiiiii1 - I11i
 if 52 - 52: Ii1I
 if 93 - 93: ii1ii11IIIiiI . Ii
 if 24 - 24: o000O0o . oO0o + I1111IIi . Ooo00oOo0oOo - Ii1I % ii1ii11IIIiiI
def OoO0oo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 OOooOoooOoOo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for iiii1iI1IIiIi , i1Iii1I11ii , oOoO000OOoo0 , IIiiI1iii1 in OOooOoooOoOo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iiii1iI1IIiIi , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOoO000OOoo0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % IIiiI1iii1 )
  inc = inc + 1
  if 100 - 100: ii1ii11IIIiiI / I11i
  if 11 - 11: Ii1I * OOooOOo % Ii - ooOOOoO
  if 77 - 77: IIiIiII11i - I11i . Ii1I
  if 63 - 63: Ooo00oOo0oOo
  if 79 - 79: Ii1I - Ooo00oOo0oOo - I11i . o000O0o
  if 65 - 65: Ii . oO0o % ii1ii11IIIiiI + O0OOOoOoo0 - Ii
  if 60 - 60: I1111IIi
  if 14 - 14: I1ii11iIi11i % Ooo00oOo0oOo * ii1ii11IIIiiI - Ii / Ii1I * Ii
  if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Ii1IIIi1 + o000O0o
def i1i11IiII ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'addons2.ini' )
  O00O0oOO00O00 = ii11iIi1I . http_GET ( url ) . content
  oOo00o00oO = open ( iIIiiI1Ii1II , "w" )
  oOo00o00oO . write ( O00O0oOO00O00 )
  oOo00o00oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIIiiI1Ii1II ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 94 - 94: iI11I1II1I1I / oOo0O0Ooo * Ii1I
def I1i1ii1IiI1i ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iIIiiI1Ii1II = os . path . join ( OO0Oooo0oOO0O , 'settings.xml' )
  O00O0oOO00O00 = ii11iIi1I . http_GET ( url ) . content
  oOo00o00oO = open ( iIIiiI1Ii1II , "w" )
  oOo00o00oO . write ( O00O0oOO00O00 )
  oOo00o00oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIIiiI1Ii1II ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 78 - 78: ii1ii11IIIiiI
 if 15 - 15: ii1ii11IIIiiI + Ii % o0o00Oo0O % I1111IIi + oO0o * iiiiiiii1
def i1I ( ) :
 try :
  ii11iiI1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ii11iiI1 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o0ooOO000O = os . path . join ( ii11iiI1 , "source.db" )
    os . unlink ( o0ooOO000O )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 49 - 49: I1ii11iIi11i
 if 57 - 57: o0o00Oo0O * iiiiiiii1 - ii1ii11IIIiiI - iI11I1II1I1I * ii1ii11IIIiiI
 if 9 - 9: O0OOOoOoo0 . Ii1IIIi1
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
 if 96 - 96: iiiiiiii1 % o0o00Oo0O
def IIII ( url ) :
 OOoOO0oo0ooO = urllib2 . Request ( url )
 OOoOO0oo0ooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O0o0O00Oo0o0 = urllib2 . urlopen ( OOoOO0oo0ooO )
 O00O0oOO00O00 = O0o0O00Oo0o0 . read ( )
 O0o0O00Oo0o0 . close ( )
 return O00O0oOO00O00
 if 51 - 51: oOo0O0Ooo - ii1ii11IIIiiI / Ii1I . Ii1I + Ii1I
 if 87 - 87: IIiIiII11i . ooOOOoO * oO0o
 if 74 - 74: I11i % OOooOOo . ii1ii11IIIiiI % I1111IIi . o0o00Oo0O % IIiIiII11i
 if 5 - 5: Ooo00oOo0oOo - ii / OOooOOo
 if 30 - 30: Ii1IIIi1 % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
 if 55 - 55: oO0o
 if 20 - 20: iiiiiiii1 * I1111IIi * I11i - iiiiiiii1
def iiii111II ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i1I1IiiIIIiiI = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i1I1IiiIIIiiI :
  oOoo0O = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oOoo0O = xbmc . translatePath ( oOoo0O ) ;
  ooO00OO0ooo = os . path . join ( oOoo0O , ".." , ".." ) ; ooO00OO0ooo = os . path . abspath ( ooO00OO0ooo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + ooO00OO0ooo ) ; O0oi1i1ii1Ii111i = False
  try :
   for Iii11III1I11 , Oo00OO0 , oo0O in os . walk ( ooO00OO0ooo , topdown = True ) :
    Oo00OO0 [ : ] = [ Oo0 for Oo0 in Oo00OO0 if Oo0 not in o0oO0 ]
    for I1111i in oo0O :
     try : os . remove ( os . path . join ( Iii11III1I11 , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0oi1i1ii1Ii111i = True
      plugintools . log ( "Error removing " + Iii11III1I11 + " " + I1111i )
    for I1111i in Oo00OO0 :
     try : os . rmdir ( os . path . join ( Iii11III1I11 , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : O0oi1i1ii1Ii111i = True
      plugintools . log ( "Error removing " + Iii11III1I11 + " " + I1111i )
   if not O0oi1i1ii1Ii111i : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 i11Ii11II1I1 ( )
 if 18 - 18: o0o00Oo0O
 if 14 - 14: ooOOOoO / O0OOOoOoo0 - o0o00Oo0O
 if 16 - 16: I1111IIi % iI11I1II1I1I . ooOoO0O00
def o0O0oOOoo0O0 ( ) :
 OO00OOo = [ ]
 IiI11i1IiI1 = sys . argv [ 2 ]
 if len ( IiI11i1IiI1 ) >= 2 :
  I11iIiI1I1i11 = sys . argv [ 2 ]
  o00oOO00 = I11iIiI1I1i11 . replace ( '?' , '' )
  if ( I11iIiI1I1i11 [ len ( I11iIiI1I1i11 ) - 1 ] == '/' ) :
   I11iIiI1I1i11 = I11iIiI1I1i11 [ 0 : len ( I11iIiI1I1i11 ) - 2 ]
  o00O0oOOo = o00oOO00 . split ( '&' )
  OO00OOo = { }
  for iIioOo in range ( len ( o00O0oOOo ) ) :
   i1OOO00oO0O = { }
   i1OOO00oO0O = o00O0oOOo [ iIioOo ] . split ( '=' )
   if ( len ( i1OOO00oO0O ) ) == 2 :
    OO00OOo [ i1OOO00oO0O [ 0 ] ] = i1OOO00oO0O [ 1 ]
    if 5 - 5: OOooOOo / o000O0o / iiiiiiii1 % Ii1I - IIiIiII11i
 return OO00OOo
 if 59 - 59: ooOoO0O00 + OOooOOo . ii1ii11IIIiiI + oOo0O0Ooo . Ooo00oOo0oOo / ii1ii11IIIiiI
ii1iiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1IiiiiIi1I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i11i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oo0oo0O0Oo0O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
O0OOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo0oi1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
Iii11I1i = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OO00O0O00oOOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IIi1iII11III = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I11Iii1ii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iiiIIIIiI1iiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
Oo0ooo00OoO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oooOOoO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0oo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiIiI11Iii11 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iiii1II = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooO00o = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
ii1111iIIiIIi = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
II111iIiI1Ii = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o0000o0Oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOOOOoO00Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OooiiIii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IIIIiiiii = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OoOoO00OOoOOOo0 = base64 . decodestring ( 'Q1VOVA==' )
def Iii1I1I11iiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = True )
 return i1ii
 if 60 - 60: oO0o
def I1I1i1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IiiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1ii = True
 O0ooO0ooo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O0ooO0ooo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O0ooO0ooo0oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iioo0o0OoOOO = [ ]
  if showcontext == 'fav' :
   iioo0o0OoOOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0oOOo :
   iioo0o0OoOOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O0ooO0ooo0oO . addContextMenuItems ( iioo0o0OoOOO )
 i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiiiIi1i , listitem = O0ooO0ooo0oO , isFolder = False )
 return i1ii
 if 10 - 10: Ii1IIIi1 . ii - oO0o
 if 96 - 96: ooOOOoO
I11iIiI1I1i11 = o0O0oOOoo0O0 ( )
o0OIiII = None
I1111i = None
oo000ii = None
O0Oo000 = None
i1II1 = None
oo0o0O0Oooooo = None
o00O00 = None
O0OoOOo = None
if 59 - 59: o000O0o % OOooOOo
if 71 - 71: Ii1I
try :
 O0OoOOo = int ( I11iIiI1I1i11 [ "fav_mode" ] )
except :
 pass
 if 5 - 5: iiiiiiii1
try :
 o0OIiII = urllib . unquote_plus ( I11iIiI1I1i11 [ "url" ] )
except :
 pass
try :
 I1111i = urllib . unquote_plus ( I11iIiI1I1i11 [ "name" ] )
except :
 pass
try :
 O0Oo000 = urllib . unquote_plus ( I11iIiI1I1i11 [ "iconimage" ] )
except :
 pass
try :
 oo000ii = int ( I11iIiI1I1i11 [ "mode" ] )
except :
 pass
try :
 i1II1 = urllib . unquote_plus ( I11iIiI1I1i11 [ "fanart" ] )
except :
 pass
try :
 oo0o0O0Oooooo = urllib . unquote_plus ( I11iIiI1I1i11 [ "description" ] )
except :
 pass
 if 34 - 34: ii1ii11IIIiiI - Ooo00oOo0oOo
 if 22 - 22: I1111IIi + Ii1I - ii1ii11IIIiiI * IIiIiII11i
print str ( iIi1ii1I1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oo000ii )
print "URL: " + str ( o0OIiII )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( O0Oo000 )
if 97 - 97: o0o00Oo0O . I11i
if 17 - 17: o0o00Oo0O . Ooo00oOo0oOo - Ooo00oOo0oOo - ooOoO0O00 * o000O0o
def O0oO0 ( content , viewType ) :
 if 16 - 16: OOooOOo / IIiIiII11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 22 - 22: Ii1IIIi1
if O0Oo000 == None : O0Oo000 = O0o0Oo
if i1II1 == None : i1II1 = Ooo
if oo000ii == None :
 ooO0oOOooOo0 ( )
 if 53 - 53: oO0o
elif oo000ii == 1 :
 I1ii1i ( o0OIiII )
 if 96 - 96: ii - iI11I1II1I1I . Ooo00oOo0oOo
elif oo000ii == 44 :
 OOoooO00o0oo0 ( o0OIiII )
 if 2 - 2: ooOoO0O00
elif oo000ii == 2 :
 iIi11i ( )
 if 6 - 6: ooOoO0O00 % Ii1IIIi1 . O0OOOoOoo0 + O0OOOoOoo0 . Ii1IIIi1 / Ii
elif oo000ii == 3 :
 o0Oo00OO0 ( )
 if 78 - 78: o0o00Oo0O
elif oo000ii == 21 :
 i1i1II ( )
 if 34 - 34: IIiIiII11i
elif oo000ii == 4 :
 i1II1i ( )
 if 20 - 20: oOo0O0Ooo % ooOoO0O00 % OOooOOo % I1111IIi + o0o00Oo0O
elif oo000ii == 5 :
 O0ooooo000 ( o0OIiII )
 if 54 - 54: o0o00Oo0O
elif oo000ii == 6 :
 IiI1iI1IiiIi1 ( o0OIiII )
 if 3 - 3: Ii1I
elif oo000ii == 7 :
 o00ooO0 ( o0OIiII , I1111i )
 if 42 - 42: Ii1IIIi1 % I1ii11iIi11i + O0OOOoOoo0 - Ii1IIIi1 . iI11I1II1I1I - ooOOOoO
elif oo000ii == 8 :
 O0OOo00O ( o0OIiII , I1111i )
 if 27 - 27: ii1ii11IIIiiI % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif oo000ii == 9 :
 FIXREPOSADDONS ( o0OIiII )
 if 37 - 37: ii1ii11IIIiiI + I1111IIi * ooOOOoO + O0OOOoOoo0
elif oo000ii == 10 :
 I1iIIiiIIi1i ( )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + ooOOOoO / IIiIiII11i
elif oo000ii == 11 :
 IIIi ( o0OIiII )
 if 66 - 66: iiiiiiii1 + Ooo00oOo0oOo % ii
elif oo000ii == 12 :
 OoO0oo ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 23 - 23: Ooo00oOo0oOo . OOooOOo + iI11I1II1I1I
elif oo000ii == 13 :
 OoOoO0O ( )
 if 17 - 17: O0OOOoOoo0
elif oo000ii == 14 :
 I1IiiiiI ( o0OIiII )
 if 12 - 12: ooOoO0O00 . oO0o
elif oo000ii == 15 :
 OOoooOoO0Oo ( )
 if 14 - 14: o000O0o + IIiIiII11i % o000O0o . Ooo00oOo0oOo * iiiiiiii1
elif oo000ii == 16 :
 i1i11IiII ( o0OIiII , I1111i )
 if 54 - 54: iiiiiiii1 * Ii1IIIi1 - I1111IIi
elif oo000ii == 17 :
 I1i1ii1IiI1i ( o0OIiII , I1111i )
 if 15 - 15: ii1ii11IIIiiI / o0o00Oo0O
elif oo000ii == 18 :
 i1I ( )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + iiiiiiii1 . I1111IIi * iiiiiiii1
elif oo000ii == 19 :
 ii1i ( o0OIiII )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif oo000ii == 40 :
 Ii11i1Ii1IIII ( I1111i , o0OIiII , oo0o0O0Oooooo )
 if 82 - 82: o0o00Oo0O / ii1ii11IIIiiI * oO0o - Ii1IIIi1 + I1ii11iIi11i
elif oo000ii == 42 :
 i11i11II11i ( I1111i , o0OIiII , oo0o0O0Oooooo )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + ooOOOoO * IIiIiII11i
elif oo000ii == 43 :
 iiiI1i1 ( o0OIiII )
 if 78 - 78: I1111IIi - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif oo000ii == 20 :
 ii1I11i ( o0OIiII )
 if 97 - 97: ooOoO0O00
elif oo000ii == 22 :
 oOO00o0 ( o0OIiII )
 if 29 - 29: oOo0O0Ooo
elif oo000ii == 23 :
 oO0I1ii11i1 ( o0OIiII )
 if 37 - 37: Ii1I * I1111IIi * oOo0O0Ooo * o0o00Oo0O
elif oo000ii == 24 :
 oOo0000oo ( o0OIiII )
 if 35 - 35: oOo0O0Ooo - Ii1I * ii1ii11IIIiiI + O0OOOoOoo0 / ooOoO0O00
elif oo000ii == 25 :
 OOooiIi1 ( o0OIiII )
 if 46 - 46: I1ii11iIi11i . iiiiiiii1 % I1ii11iIi11i / IIiIiII11i * iiiiiiii1 * o000O0o
elif oo000ii == 26 :
 O00oO0oOOOOOO ( o0OIiII )
 if 59 - 59: I1111IIi * ii1ii11IIIiiI
elif oo000ii == 27 :
 I1i1I1i1Ii ( o0OIiII )
 if 31 - 31: Ii1IIIi1 / o0o00Oo0O
elif oo000ii == 28 :
 iIII1iiiiI1Ii11 ( o0OIiII )
 if 57 - 57: ooOoO0O00 % iiiiiiii1
elif oo000ii == 29 :
 i11IIii ( o0OIiII )
 if 69 - 69: I11i
elif oo000ii == 30 :
 oooO00Oo ( o0OIiII )
 if 69 - 69: I1111IIi
elif oo000ii == 31 :
 oOOOOoo000Ooo ( o0OIiII )
 if 83 - 83: iI11I1II1I1I . I11i + I1111IIi . ii / iiiiiiii1 + IIiIiII11i
elif oo000ii == 32 :
 O0O0OOOOoo ( )
 if 90 - 90: ooOOOoO * ii1ii11IIIiiI / o000O0o
elif oo000ii == 33 :
 oOo00Ooo0o0 ( )
 if 68 - 68: OOooOOo
elif oo000ii == 35 :
 iI1ii1ii1I ( o0OIiII )
 if 65 - 65: Ooo00oOo0oOo
elif oo000ii == 34 :
 i1IiII1i1I ( o0OIiII )
 if 82 - 82: I11i
elif oo000ii == 36 :
 oOI11 ( o0OIiII )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + I1111IIi
elif oo000ii == 37 :
 oOOo0OoOOOoo ( o0OIiII )
 if 65 - 65: ooOOOoO
elif oo000ii == 38 :
 ii11i11 ( o0OIiII )
 if 71 - 71: I1111IIi % I1111IIi . Ooo00oOo0oOo + Ii - Ii
elif oo000ii == 41 :
 iiii111II ( I11iIiI1I1i11 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / I1111IIi - Ii . iiiiiiii1 / o000O0o
elif oo000ii == 39 :
 oOooO0 ( o0OIiII )
 if 13 - 13: I11i % o0o00Oo0O - I1111IIi * ii / I1ii11iIi11i - ii
elif oo000ii == 45 :
 TEXTS ( )
 if 78 - 78: Ooo00oOo0oOo % ii
elif oo000ii == 46 :
 Ii1I1Ii ( )
 if 73 - 73: oOo0O0Ooo % iiiiiiii1 % O0OOOoOoo0 + ooOoO0O00 - ii / Ooo00oOo0oOo
elif oo000ii == 47 :
 GEVID ( )
 if 78 - 78: ii % Ooo00oOo0oOo - Ii
elif oo000ii == 48 :
 III1III11II ( I1111i , o0OIiII , oo0o0O0Oooooo )
 if 37 - 37: O0OOOoOoo0 % ooOOOoO % ooOoO0O00
elif oo000ii == 49 :
 oo00oO0o ( )
 if 23 - 23: iiiiiiii1 - o0o00Oo0O + Ii
elif oo000ii == 22222 :
 O0OoOOO00 ( o0OIiII )
 if 98 - 98: ii
elif oo000ii == 222 :
 O0OoO00 ( o0OIiII , I1111i )
 if 61 - 61: I11i . O0OOOoOoo0 . o0o00Oo0O + ii + o0o00Oo0O
elif oo000ii == 333 :
 oO0O ( o0OIiII )
 if 65 - 65: ooOoO0O00 * o000O0o * ii - O0OOOoOoo0 . ii1ii11IIIiiI - oO0o
 if 71 - 71: ooOOOoO * OOooOOo
elif oo000ii == 1020 :
 ooO0O0OOO ( )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % I1111IIi * I11i
elif oo000ii == 1021 :
 ANIMEEP ( )
 if 64 - 64: iiiiiiii1 / iiiiiiii1 + Ii1I * o000O0o % o000O0o
elif oo000ii == 1022 :
 ANIMEPLAY ( o0OIiII )
 if 87 - 87: oO0o * I1ii11iIi11i
elif oo000ii == 1001 :
 IiI1i1111iI1i ( )
 if 83 - 83: ooOoO0O00 * I1111IIi - O0OOOoOoo0 / ooOOOoO
elif oo000ii == 1005 :
 oOoOo0o0 ( )
 if 48 - 48: Ooo00oOo0oOo . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif oo000ii == 1007 :
 II1Iiiii ( o0OIiII )
 if 32 - 32: ooOOOoO * oOo0O0Ooo - o000O0o . I1ii11iIi11i / o0o00Oo0O + ooOOOoO
elif oo000ii == 1010 :
 iiO0O0o0oO0O00 ( o0OIiII )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif oo000ii == 1011 :
 I111II1iIIII ( o0OIiII )
 if 7 - 7: Ii % Ii1I / I1111IIi % I1ii11iIi11i - oO0o
elif oo000ii == 1012 :
 I1I1i1 ( o0OIiII )
 if 73 - 73: Ii1I
elif oo000ii == 1030 :
 Ooo00oo0ooO0 ( )
 if 92 - 92: Ii + o0o00Oo0O * Ii1IIIi1
elif oo000ii == 1031 :
 i1ii1i1 ( o0OIiII , O0Oo000 )
 if 60 - 60: I11i / I1ii11iIi11i
elif oo000ii == 1032 :
 iIi ( o0OIiII )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif oo000ii == 1006 :
 Parse . ParseURL ( o0OIiII )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % I1111IIi / Ii1I
elif oo000ii == 2030 :
 Parse . addonParseURL ( o0OIiII )
 if 76 - 76: oO0o * Ooo00oOo0oOo - oO0o
elif oo000ii == 2031 :
 Parse . apkParseURL ( o0OIiII )
 if 57 - 57: ii / OOooOOo + Ooo00oOo0oOo . ooOOOoO
elif oo000ii == 1002 :
 O0iiIi1iIiI ( o0OIiII )
 if 14 - 14: Ii % o000O0o * I11i * OOooOOo
elif oo000ii == 1003 :
 IIi1iii ( o0OIiII , O0Oo000 )
 if 55 - 55: I1111IIi * o000O0o * I1111IIi
elif oo000ii == 1004 :
 ii1Ii ( o0OIiII )
 if 70 - 70: o0o00Oo0O . ooOOOoO
elif oo000ii == 1008 :
 II1Iii1I1II1i ( )
 if 33 - 33: o000O0o * ooOOOoO
elif oo000ii == 1009 :
 oooo0OoOo ( o0OIiII )
 if 64 - 64: Ii . iI11I1II1I1I
elif oo000ii == 2001 :
 i1I111Iii ( )
 if 7 - 7: OOooOOo % iiiiiiii1 + OOooOOo - OOooOOo * Ii % oO0o
elif oo000ii == 2002 :
 iII ( o0OIiII )
 if 57 - 57: o000O0o / oO0o + Ii1I
elif oo000ii == 1013 :
 O0O00OooO ( )
elif oo000ii == 10111113 :
 III1Ii1i1I1 ( o0OIiII )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % o000O0o + O0OOOoOoo0 . oO0o . I1ii11iIi11i
elif oo000ii == 1014 :
 Oo0o ( )
 if 70 - 70: Ii1IIIi1 . Ii1I * Ooo00oOo0oOo
elif oo000ii == 1015 :
 I11iiIiI1II11 ( o0OIiII )
 if 97 - 97: Ooo00oOo0oOo . iI11I1II1I1I - o000O0o
elif oo000ii == 1016 :
 IiIII1 ( o0OIiII , O0Oo000 , I1111i )
 if 23 - 23: Ii1I % Ii1IIIi1
elif oo000ii == 1017 :
 O0OoOO0oo0 ( )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif oo000ii == 1018 :
 Ii1I11ii1i ( o0OIiII )
 if 99 - 99: I1111IIi - Ii1I - oOo0O0Ooo - I1111IIi + oO0o + IIiIiII11i
elif oo000ii == 1023 :
 oOO ( )
 if 34 - 34: I1111IIi * Ii1IIIi1
elif oo000ii == 1024 :
 ii11oOo0OO0 ( o0OIiII )
 if 31 - 31: O0OOOoOoo0 . Ooo00oOo0oOo
elif oo000ii == 1025 :
 OoOiIiIi1i1ii11 ( o0OIiII )
 if 40 - 40: ooOOOoO - Ii1IIIi1 / IIiIiII11i * ooOoO0O00 + O0OOOoOoo0 * IIiIiII11i
elif oo000ii == 4001 :
 i11i1 ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - I1111IIi
elif oo000ii == 4002 :
 IiIi1I1 ( )
 if 99 - 99: ooOOOoO - O0OOOoOoo0 - ooOoO0O00 / Ii . O0OOOoOoo0
elif oo000ii == 4003 :
 Iiii1iiiIiI1 ( )
 if 58 - 58: o000O0o
elif oo000ii == 4004 :
 i11OOoo ( )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif oo000ii == 4005 :
 iIIiiiI ( )
 if 64 - 64: OOooOOo + O0OOOoOoo0 - ooOoO0O00 . IIiIiII11i . oO0o
elif oo000ii == 4006 :
 iIi1Ii1i1iI ( )
 if 31 - 31: Ooo00oOo0oOo . ii1ii11IIIiiI - Ii1IIIi1 . iI11I1II1I1I + Ii1IIIi1 . OOooOOo
elif oo000ii == 4007 :
 IiI111ii1ii ( )
 if 86 - 86: Ii1I - Ii1I / ii1ii11IIIiiI - Ii1I * ii1ii11IIIiiI + I1111IIi
elif oo000ii == 4008 :
 iiI11i1II ( )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - O0OOOoOoo0
elif oo000ii == 4009 : ooO ( )
elif oo000ii == 4010 : IIIiIiI ( )
elif oo000ii == 3000 :
 oO0OO ( )
 if 30 - 30: ii % o000O0o
elif oo000ii == 3001 :
 ii11 ( )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - o000O0o
elif oo000ii == 3002 :
 oOOooooO ( o0OIiII )
 if 81 - 81: ii1ii11IIIiiI % ooOOOoO . iiiiiiii1
elif oo000ii == 3003 :
 o000Ooo00o00O ( o0OIiII )
 if 66 - 66: Ii1I * ooOOOoO / ii * o0o00Oo0O % o000O0o
elif oo000ii == 3004 :
 oo000oO ( o0OIiII )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * ooOOOoO / I1111IIi * ii
elif oo000ii == 404 :
 iI1Iii1i11 ( I1111i , o0OIiII , O0Oo000 )
 if 82 - 82: I1ii11iIi11i / ooOOOoO / ooOOOoO % ooOOOoO
elif oo000ii == 405 :
 IIii ( o0OIiII )
 if 20 - 20: iiiiiiii1
elif oo000ii == 7030 :
 I1I ( )
 if 63 - 63: iI11I1II1I1I . oO0o
elif oo000ii == 7021 :
 O0Oo00o0o ( I1111i )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif oo000ii == 7022 :
 I1oooO00oOOooO ( I1111i )
 if 26 - 26: o000O0o . oO0o % OOooOOo
elif oo000ii == 7000 :
 Oo0o0OOo0Oo0 ( I1111i , o0OIiII , img )
 if 94 - 94: O0OOOoOoo0
elif oo000ii == 7050 :
 I1IiI1iI11 ( o0OIiII )
 if 15 - 15: ooOOOoO - O0OOOoOoo0 / o0o00Oo0O
elif oo000ii == 7051 :
 iIiii1IIi1I ( o0OIiII )
 if 28 - 28: I1111IIi . ooOoO0O00 / Ii1I
elif oo000ii == 7052 :
 o0o00OO00OOo0 ( o0OIiII )
 if 77 - 77: Ii / I1111IIi / Ii % OOooOOo - I1111IIi
elif oo000ii == 7053 :
 ooOo00ooO ( o0OIiII )
 if 80 - 80: I1111IIi % OOooOOo . ii . IIiIiII11i % O0OOOoOoo0
elif oo000ii == 7054 :
 CoolPlay ( o0OIiII )
 if 6 - 6: I1111IIi % O0OOOoOoo0 / ooOOOoO + I1111IIi . Ooo00oOo0oOo
elif oo000ii == 7060 :
 ooooOo00O ( )
 if 70 - 70: iI11I1II1I1I / ooOOOoO
elif oo000ii == 7061 :
 IiIi ( o0OIiII )
 if 61 - 61: o0o00Oo0O * I11i + I1111IIi - o000O0o . oOo0O0Ooo - O0OOOoOoo0
elif oo000ii == 7063 :
 iiIIiI1I ( o0OIiII )
 if 7 - 7: Ii1I
elif oo000ii == 7062 :
 OO000oooOo000 ( o0OIiII )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / Ii1IIIi1
elif oo000ii == 7064 :
 NATatozcat ( )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif oo000ii == 7067 :
 o0oO0o0Oo0 ( o0OIiII )
 if 13 - 13: Ii
elif oo000ii == 7066 :
 NATatozA ( o0OIiII )
 if 54 - 54: o000O0o . Ii1I * Ii1IIIi1 % I1111IIi . o0o00Oo0O * O0OOOoOoo0
elif oo000ii == 7065 :
 i1I1iiiI ( o0OIiII )
 if 87 - 87: ooOOOoO % Ii1I * I1ii11iIi11i
elif oo000ii == 7070 :
 II1IIIi ( )
 if 59 - 59: I1ii11iIi11i / Ii1IIIi1 - iI11I1II1I1I * iI11I1II1I1I
elif oo000ii == 7071 :
 DIZIlist ( o0OIiII )
 if 18 - 18: Ii1IIIi1 * Ii1I / Ii / iI11I1II1I1I * ii . o000O0o
elif oo000ii == 7072 :
 DIZIpull ( o0OIiII )
 if 69 - 69: I1ii11iIi11i * iiiiiiii1
elif oo000ii == 7073 :
 WATCHDIZI ( o0OIiII )
 if 91 - 91: I11i . iiiiiiii1 / oO0o / Ii * I11i
elif oo000ii == 7002 :
 IIIII11II1 ( )
 if 52 - 52: oOo0O0Ooo - Ii / O0OOOoOoo0 . Ooo00oOo0oOo
elif oo000ii == 7003 :
 iI1II1iIiiiI ( o0OIiII )
 if 38 - 38: Ooo00oOo0oOo + ii * OOooOOo % Ooo00oOo0oOo
elif oo000ii == 7004 :
 OoO0II1iiIiI1 ( o0OIiII )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif oo000ii == 7020 :
 IiIi1I1IiI1II1 ( o0OIiII )
 if 24 - 24: OOooOOo * ooOOOoO
elif oo000ii == 7001 :
 o0OooOOOOOO ( )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif oo000ii == 7010 :
 oO0IIi11IiiiI11i ( o0OIiII )
 if 81 - 81: o000O0o
elif oo000ii == 7011 :
 iiIIII11iIii ( o0OIiII )
 if 58 - 58: IIiIiII11i . I1111IIi . ooOOOoO * ii / ooOOOoO / Ii1IIIi1
elif oo000ii == 7012 :
 iiIi1 ( o0OIiII )
 if 41 - 41: Ii1IIIi1 + oO0o . ii1ii11IIIiiI
elif oo000ii == 7013 :
 cnfTVPlay2 ( o0OIiII )
elif oo000ii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( o0OIiII )
elif oo000ii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( o0OIiII )
elif oo000ii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , o0OIiII , O0Oo000 )
elif oo000ii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oo000ii == 7018 :
 I1ii ( )
elif oo000ii == 7019 :
 CNF_Studio_Indexer . List_Movies ( o0OIiII )
elif oo000ii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( o0OIiII )
elif oo000ii == 7024 :
 CNF_Studio_Indexer . Box_Office ( o0OIiII )
 if 73 - 73: Ii * oOo0O0Ooo + I11i / Ooo00oOo0oOo
elif oo000ii == 8000 :
 I1111iIIiIIII ( )
elif oo000ii == 8001 :
 OOOo0Ooo0o00o ( )
elif oo000ii == 8002 :
 O0ooo0 ( )
elif oo000ii == 8003 :
 IIIII1IIiIi ( )
elif oo000ii == 8004 :
 OO00 ( )
elif oo000ii == 8005 :
 IIiIIiiiiiII1 ( )
elif oo000ii == 8006 :
 oOOOo0Oooo ( I1111i , o0OIiII )
elif oo000ii == 8030 :
 iii11i1 ( o0OIiII )
elif oo000ii == 8045 :
 i1iIii ( o0OIiII )
elif oo000ii == 8046 :
 O0o00 ( o0OIiII )
elif oo000ii == 8047 :
 IiIiI ( o0OIiII )
elif oo000ii == 8048 :
 oo0oo00O0O ( o0OIiII )
elif oo000ii == 8049 :
 iIiiI1I ( o0OIiII )
elif oo000ii == 804900 :
 Oo0iI1Iii11i ( o0OIiII )
elif oo000ii == 8020 :
 I1I1i ( )
elif oo000ii == 8021 :
 O0000oOo0OO ( o0OIiII )
elif oo000ii == 8022 :
 oo00O000 ( o0OIiII )
elif oo000ii == 8023 :
 o0o00OO0oOoO ( o0OIiII )
elif oo000ii == 8040 :
 I1 ( )
elif oo000ii == 8041 :
 O0oo0000o ( o0OIiII )
elif oo000ii == 8042 :
 OOoO00O ( o0OIiII )
elif oo000ii == 8043 :
 yt . PlayVideo ( o0OIiII )
elif oo000ii == 8044 :
 iio00O0o00oo ( o0OIiII )
elif oo000ii == 8060 :
 iIIiIiI1I1 ( )
elif oo000ii == 8061 :
 o00i111iiIiiIiI ( o0OIiII )
elif oo000ii == 8064 :
 I1IIIiIiIi ( )
elif oo000ii == 8065 :
 oOoo00 ( o0OIiII )
elif oo000ii == 8070 :
 iiI1 ( )
elif oo000ii == 8071 :
 oooOOO0o0O0 ( o0OIiII )
elif oo000ii == 7080 :
 iiiI1IiI ( o0OIiII )
elif oo000ii == 8090 :
 o000OO00OoO00 ( )
elif oo000ii == 8091 :
 i1Ii1i11ii ( o0OIiII )
elif oo000ii == 8092 :
 O00O ( o0OIiII )
elif oo000ii == 8093 :
 oO0O0oo ( o0OIiII )
elif oo000ii == 8081 :
 oOoO0oOo0Oo ( )
elif oo000ii == 8062 :
 oOoO0oO00ooOo ( o0OIiII )
elif oo000ii == 8063 :
 I1iO00O000oOO0oO ( o0OIiII )
elif oo000ii == 8050 :
 O0OO0ooO00 ( )
elif oo000ii == 8051 :
 oO0oOO0o ( o0OIiII )
elif oo000ii == 8052 :
 o0OI1II ( o0OIiII )
elif oo000ii == 8085 :
 o0oo00O ( )
elif oo000ii == 8086 :
 II111iii ( o0OIiII )
elif oo000ii == 8087 :
 Ii11II1i1I ( o0OIiII )
elif oo000ii == 8088 :
 i1iIii1 ( o0OIiII , I1111i )
elif oo000ii == 9000 :
 ooOo0O00o0OoO ( )
elif oo000ii == 1111 :
 o0O0oO0 ( )
elif oo000ii == 9001 :
 iiII1i11i ( )
elif oo000ii == 9002 :
 I111i1i1111 ( )
elif oo000ii == 9003 :
 III1I11II11I ( )
elif oo000ii == 9004 :
 World1 ( )
elif oo000ii == 9005 :
 World2 ( o0OIiII )
elif oo000ii == 9006 :
 World3 ( o0OIiII )
elif oo000ii == 9007 :
 iiIi1111iiI1 ( )
elif oo000ii == 9008 :
 o00oo00 ( o0OIiII )
elif oo000ii == 9009 :
 o0oO0O ( o0OIiII )
elif oo000ii == 9010 :
 o000oo ( )
elif oo000ii == 9011 :
 O0Ooo0o ( o0OIiII )
elif oo000ii == 50 :
 oo0OoOOooO ( o0OIiII )
elif oo000ii == 9020 :
 champlist ( )
elif oo000ii == 9021 :
 IIIii111i ( )
elif oo000ii == 9022 :
 O000OoOO0oO ( )
elif oo000ii == 9023 :
 iII1o00OO0 ( )
elif oo000ii == 9024 :
 i11IiIiii ( o0OIiII )
elif oo000ii == 9030 :
 iIiii1iI1Ii ( o0OIiII )
elif oo000ii == 9031 :
 ooIi ( o0OIiII )
elif oo000ii == 9032 :
 oO0oOo ( o0OIiII )
elif oo000ii == 9033 :
 IIiIiii ( o0OIiII )
elif oo000ii == 9034 :
 OOooO0o0 ( )
elif oo000ii == 7085 :
 I1iiIIii ( o0OIiII )
elif oo000ii == 7086 :
 o00oO0O000 ( o0OIiII )
elif oo000ii == 7087 :
 O00oOO ( oo0o0O0Oooooo )
elif oo000ii == 9666 :
 ii1 ( o0OIiII )
elif oo000ii == 10100 : i1i11ii1 ( )
elif oo000ii == 101001 : oOOO ( o0OIiII )
elif oo000ii == 10105 : Ii11iIiiI ( o0OIiII )
elif oo000ii == 10106 : iiII ( o0OIiII )
elif oo000ii == 10104 : I11iiIiiI1iIi11 ( o0OIiII )
elif oo000ii == 10107 : Iii1IiiII1Ii1 ( )
elif oo000ii == 10103 : iII1IiiIIIIii ( o0OIiII )
elif oo000ii == 10108 : ooOooOooOOO ( o0OIiII )
elif oo000ii == 10000 : Origin_Menu ( )
elif oo000ii == 10001 : III111i11IiI ( )
elif oo000ii == 10002 : oo0 ( )
elif oo000ii == 10003 : OO0O0OOo0O ( )
elif oo000ii == 10004 : ooO00O0O0 ( o0OIiII )
elif oo000ii == 10005 : O0OO0oOOo ( )
elif oo000ii == 10006 : o0O0Ooo ( o0OIiII )
elif oo000ii == 10007 : Ii11iiI ( o0OIiII , O0Oo000 )
elif oo000ii == 10008 : IIiiIii11 ( )
elif oo000ii == 10009 : oO0000O0Oo00O ( )
elif oo000ii == 10010 : Ii1IIii ( o0OIiII )
elif oo000ii == 10011 : Ii11ii1 ( o0OIiII )
elif oo000ii == 10012 : OOOOo0o00OO0000 ( o0OIiII )
elif oo000ii == 10109 : ooo0oooO ( o0OIiII )
elif oo000ii == 10013 : iI1111i1i11Ii ( o0OIiII )
elif oo000ii == 10014 : ooIiI11i1I11111 ( )
elif oo000ii == 10015 : I1I11Iiii111 ( )
elif oo000ii == 10016 : oOo0oO ( o0OIiII )
elif oo000ii == 10017 : ooIi11iI ( )
elif oo000ii == 10018 : oOo0OoOOOo0 ( )
elif oo000ii == 10019 : O0ooO00o ( )
elif oo000ii == 10020 : OOo00Oooo ( )
elif oo000ii == 10021 : o00OoO ( )
elif oo000ii == 10022 : o0I1iI111ii111i ( o0OIiII )
elif oo000ii == 10023 : Ii1IiiiI1ii ( I1111i , o0OIiII )
elif oo000ii == 10024 : Ii1iiI1i1 ( o0OIiII )
elif oo000ii == 10025 : II1iiiiII ( )
elif oo000ii == 10026 : I1IIIIIi1IIiI ( )
elif oo000ii == 10027 : OOoO0oO00o ( )
elif oo000ii == 10028 : o0o00OOOO ( )
elif oo000ii == 10029 : OoO0 ( )
elif oo000ii == 423 : O0Ooo0ooo00o ( o0OIiII )
elif oo000ii == 426 : o000OOO00O ( o0OIiII )
elif oo000ii == 10030 : Izle_Films ( )
elif oo000ii == 10031 : Latest_Izle_Movies ( )
elif oo000ii == 10032 : Izle_Genres ( )
elif oo000ii == 10033 : Izle_Pop_Movies ( )
elif oo000ii == 10034 : Izle_Boxsets ( )
elif oo000ii == 10035 : Izle_Search ( )
elif oo000ii == 10036 : Izle_Genres_Movie ( o0OIiII )
elif oo000ii == 10037 : Izle_Boxset_single ( o0OIiII )
elif oo000ii == 10038 : Izle_IFRAME ( )
elif oo000ii == 10039 : Izle_Boxsets_Next ( o0OIiII )
elif oo000ii == 10040 : IIII1 ( )
elif oo000ii == 10041 : Oo0OOOoOO ( o0OIiII )
elif oo000ii == 10042 : oOOo0OO00OoO ( o0OIiII )
elif oo000ii == 10043 : iIiIi11I1iIii1i11 ( )
elif oo000ii == 10044 : IIii1i ( o0OIiII )
elif oo000ii == 10045 : Ii11IIIi1 ( I1111i )
elif oo000ii == 10046 : o0oO0oOOOo ( o0OIiII )
elif oo000ii == 10047 : oOooOOoO0oO0oo0O ( o0OIiII )
elif oo000ii == 10048 : IIi1i1I11IIII ( o0OIiII )
elif oo000ii == 10049 : IIiI1111iI ( o0OIiII )
elif oo000ii == 10050 : OOI1iI1ii1II ( )
elif oo000ii == 10051 : o0O0OOooO ( )
elif oo000ii == 10052 : i1II111i1IIii ( )
elif oo000ii == 10053 : Addon ( o0OIiII )
elif oo000ii == 10054 : iIi1i111ii1II11ii ( o0OIiII , I1111i )
elif oo000ii == 10055 :
 OO0OooOo ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 Ii11IiI111 ( I1111i , o0OIiII , O0Oo000 , i1II1 , O0OoOOo )
elif oo000ii == 10056 :
 OO0OooOo ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0O0 ( I1111i )
elif oo000ii == 10057 :
 OO0OooOo ( "getFavorites" )
 I1IIIi1i ( )
elif oo000ii == 10058 : iiOO0O0Ooo ( )
elif oo000ii == 10059 : Donators_Guide ( )
elif oo000ii == 10060 : IiiiiI1i1Iii ( )
elif oo000ii == 10061 : O00OO0o0 ( )
elif oo000ii == 10062 : iIi1I1 ( I1111i , o0OIiII , oo0o0O0Oooooo )
elif oo000ii == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
elif oo000ii == 10064 : o0o0oOo000o0 ( )
elif oo000ii == 10065 : oOo ( o0OIiII )
elif oo000ii == 10066 : IiIiiiIii ( o0OIiII )
elif oo000ii == 10068 : Iii ( o0OIiII )
elif oo000ii == 10069 : IIIII1 ( o0OIiII )
elif oo000ii == 10070 : ooO00O00oOO ( o0OIiII )
elif oo000ii == 10071 : Genie_Watch ( )
elif oo000ii == 10072 : iiIii1IIi ( )
elif oo000ii == 10073 : Ii11Ii ( o0OIiII )
elif oo000ii == 10074 : III111iiIi1 ( o0OIiII )
elif oo000ii == 10075 : i1I1iIi1IiI ( O0Oo000 , I1111i , o0OIiII )
elif oo000ii == 10076 : Ii1 ( o0OIiII )
elif oo000ii == 10077 : IiI ( o0OIiII )
elif oo000ii == 10078 : i111IIIiI ( )
elif oo000ii == 10079 : Genie_Watch_Tv_Shows ( )
elif oo000ii == 10080 : Genie_Watch_Tv_Genre ( o0OIiII )
elif oo000ii == 10081 : Genie_Watch_TV_PlayRun ( o0OIiII )
elif oo000ii == 10082 : Genie_Watch_TV_Episodes ( o0OIiII , O0Oo000 )
elif oo000ii == 10083 : Genie_Watch_Tv_Recent ( o0OIiII )
elif oo000ii == 10084 : I1iiIIIi11 ( )
elif oo000ii == 10085 : ii111iI1iIi1 ( )
elif oo000ii == 10086 : i1IiiiI1iI ( )
elif oo000ii == 20000 : O0000 ( )
elif oo000ii == 20001 : oo00I1IiI1IIiI ( o0OIiII )
elif oo000ii == 20002 : iIi1 ( o0OIiII )
elif oo000ii == 20003 : ooiI1i ( o0OIiII )
elif oo000ii == 20004 : Ii11 ( o0OIiII )
elif oo000ii == 20005 : O0oo00oOOO0o ( o0OIiII )
elif oo000ii == 21004 : OO0oO0o ( )
elif oo000ii == 21005 : OOoooOoO0 ( o0OIiII )
elif oo000ii == 21006 : iIiIi1IiIi1iI ( o0OIiII )
elif oo000ii == 21007 : oOoO0Oo0 ( o0OIiII )
elif oo000ii == 30000 : oo0i1 ( )
elif oo000ii == 30001 : iIIIIIIIiIII ( )
elif oo000ii == 10012 : Resolve ( o0OIiII )
elif oo000ii == 30003 : Ooo000O00 ( )
elif oo000ii == 30004 : oOOOOO0Ooooo ( o0OIiII )
elif oo000ii == 30005 : OOoOO0O0o0 ( o0OIiII )
elif oo000ii == 30006 : iiII1iiiiiii ( )
elif oo000ii == 30007 : iIiI1ii ( )
elif oo000ii == 30008 : III1IiI1i1i ( o0OIiII )
elif oo000ii == 30009 : iiiI1iI1 ( o0OIiII )
elif oo000ii == 30010 : i111I11I ( o0OIiII )
elif oo000ii == 30011 : Ii11iiI1 ( )
elif oo000ii == 30012 : OoooO0 ( )
elif oo000ii == 30013 : IiIii1 ( )
elif oo000ii == 30014 : oO0o0Oo ( )
elif oo000ii == 30015 : OoOOoooO000 ( o0OIiII , O0Oo000 , i1II1 )
elif oo000ii == 30016 : i11i11II11i1 ( o0OIiII )
elif oo000ii == 30019 : O0OOoi1I1Iiii1 ( o0OIiII )
elif oo000ii == 30017 : OoO00ooO ( o0OIiII )
elif oo000ii == 30018 : o0oO0OO00oo0o ( o0OIiII )
elif oo000ii == 30030 : O000o0 ( )
elif oo000ii == 30031 : i1iIIi1II1iiI ( )
elif oo000ii == 30032 : O0OOo ( )
elif oo000ii == 30033 : Iiiii1 ( )
elif oo000ii == 30034 : O0Ooo0O ( )
elif oo000ii == 30035 : I1III1iIi ( o0OIiII )
elif oo000ii == 30036 : OoO00O0 ( o0OIiII )
elif oo000ii == 30037 : I1Iii ( o0OIiII )
elif oo000ii == 30038 : ooIII1II1iii1i ( )
elif oo000ii == 30039 : Ii1I1i ( )
elif oo000ii == 50000 : O0O0ooOOO ( )
elif oo000ii == 50001 : OoOi111i ( )
elif oo000ii == 50002 : iI1i1I1iiii1Ii11 ( o0OIiII )
elif oo000ii == 50003 : o0oOOoO000 ( oo0o0O0Oooooo )
elif oo000ii == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oo000ii == 60001 : I1ii1iI1II11ii ( )
elif oo000ii == 60002 : OO0ooo0o0 ( I1111i )
elif oo000ii == 60003 : OOoOIiIIII ( I1111i )
elif oo000ii == 50004 : ooO000OO0O00O ( )
elif oo000ii == 50005 : speedtest . runtest ( o0OIiII )
elif oo000ii == 70001 : I11Iii1 ( )
elif oo000ii == 70002 : O0OoO0o ( o0OIiII )
elif oo000ii == 70003 : I111IIiIII ( o0OIiII )
elif oo000ii == 70004 : OO0OOoo0OOO ( o0OIiII )
elif oo000ii == 70005 : ooooOoo0OO ( o0OIiII )
elif oo000ii == 70006 : Oo0O0000Oo00o ( )
elif oo000ii == 50006 : OO0O000 ( i1 , i1111 )
elif oo000ii == 80000 : i11Ii11II1I1 ( )
elif oo000ii == 80001 : resolvefilmon ( o0OIiII )
elif oo000ii == 80002 : IIii1i11iI1II11 ( )
elif oo000ii == 80003 : IIii1I1i ( I1111i , o0OIiII )
elif oo000ii == 80004 : i1Oo0oOo000OoO0 ( I1111i , o0OIiII )
elif oo000ii == 80005 : OOOOO0O00 ( )
elif oo000ii == 80006 : I111IIiii1Ii ( o0OIiII )
elif oo000ii == 80007 : II1 ( o0OIiII )
elif oo000ii == 80008 : iiIIIiIii ( )
elif oo000ii == 80009 : O00O0O0OO00oo ( )
elif oo000ii == 80010 : I11IIIIiI1 ( o0OIiII )
elif oo000ii == 80011 : OoOiII11IiIi ( o0OIiII )
elif oo000ii == 80012 : ooo0oOooo0o0 ( )
elif oo000ii == 90000 : oOOoo ( I1111i , o0OIiII )
elif oo000ii == 90001 : oO0O0OO0O ( )
elif oo000ii == 90002 : iIiIiIiI ( )
elif oo000ii == 90003 : IiI11Ii1iI ( o0OIiII )
elif oo000ii == 90004 : ooOo0 ( o0OIiII )
elif oo000ii == 90005 : oOo0o ( o0OIiII )
elif oo000ii == 90006 : iII11 ( o0OIiII )
elif oo000ii == 90007 : O00OO00OOOoO ( o0OIiII )
elif oo000ii == 90008 : IiIIii ( o0OIiII )
elif oo000ii == 90009 : Ii111Ii11 ( o0OIiII )
elif oo000ii == 90010 : iiIiI1i1 ( )
elif oo000ii == 90020 : ii11111I ( )
elif oo000ii == 90021 : hellyeah2 ( o0OIiII )
elif oo000ii == 90022 : hellyeah3 ( o0OIiII )
elif oo000ii == 90023 : i1OoOO ( )
elif oo000ii == 90024 : o0OIIiI1I1 ( o0OIiII )
elif oo000ii == 90025 : I11I1IIiiII1 ( o0OIiII )
if 56 - 56: ooOoO0O00
elif oo000ii == 90030 : I11iII ( )
elif oo000ii == 90031 : I1i1i1iii ( )
elif oo000ii == 90032 : iIIii ( o0OIiII )
elif oo000ii == 90033 : ii1iii1i ( o0OIiII )
elif oo000ii == 90034 : ooO0O00Oo0o ( o0OIiII )
elif oo000ii == 90035 : I1i ( o0OIiII )
if 11 - 11: Ii % I11i / Ii1IIIi1 * ii
if 82 - 82: O0OOOoOoo0
elif oo000ii == 100001 : Stand_up ( )
if 10 - 10: I1ii11iIi11i % o000O0o / Ii1IIIi1 * O0OOOoOoo0 - I11i
elif oo000ii == 100003 : oOo0oO ( o0OIiII )
elif oo000ii == 100004 : IIIIi1 ( o0OIiII )
elif oo000ii == 100005 : Resolve ( o0OIiII )
elif oo000ii == 100008 : Search ( )
elif oo000ii == 100007 : IiiII1111III1I ( o0OIiII )
elif oo000ii == 100009 : yt . PlayVideo ( o0OIiII )
elif oo000ii == 100010 : OoOoOo00o0 ( o0OIiII )
elif oo000ii == 100100 : I1I11iI11iI1i ( O0Oo000 , o0OIiII , o00O00 )
elif oo000ii == 100101 : iIiii ( o0OIiII , I1111i , i1II1 , o00O00 , O0Oo000 )
elif oo000ii == 100102 : i111IiiII ( I1111i , o0OIiII , O0Oo000 , i1II1 )
elif oo000ii == 100106 : i1i1i1I ( o0OIiII , I1111i )
elif oo000ii == 100107 : IIi ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
