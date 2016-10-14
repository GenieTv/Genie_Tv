# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
import httplib
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
IiiIII111iI = "3.1.9"
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
II = xbmc . translatePath ( 'special://logpath/' )
ooOoOoo0O = oo00 . getSetting ( 'User' )
OooO0 = oo00 . getSetting ( 'Pass' )
II11iiii1Ii = oo00 . getSetting ( 'AdultPass' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
OO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
O0o0Oo = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
Oo00OOOOO = xbmc . translatePath ( 'special://database' )
O0O = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
O00o0OO = xbmc . translatePath ( 'special://thumbnails' ) ;
I11i1 = "GenieTv"
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
I11II1i = 'http://'
IIIII = base64 . decodestring ( 'LnBocA==' )
ooooooO0oo = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
IIiiiiiiIi1I1 = [ ]
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
OOOO = oo00 . getLocalizedString
OOO00 = CookieJar ( )
iiiiiIIii = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( OOO00 ) )
iiiiiIIii . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O000OO0 = int ( sys . argv [ 1 ] )
I11iii1Ii = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
I1IIiiIiii = os . path . join ( O0O , 'favorites' )
O000oo0O = O0O + '/addons.ini'
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/userdata/' )
OOOOi11i1 = xbmc . translatePath ( 'special://home/userdatabroke/' )
IIIii1II1II = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
i1I1iI = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oo0OooOOo0 = i1I1iI + 'GenieTvWatched'
if not os . path . exists ( oo0OooOOo0 ) :
 os . makedirs ( oo0OooOOo0 )
o0O = oo0OooOOo0 + 'watched.txt'
if not os . path . exists ( o0O ) :
 open ( o0O , 'w+' )
O00oO = open ( o0O ) . read ( )
I11i1I1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
oO0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
oOOoo0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
o00OO00OoO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
OOOO0OOoO0O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( I1IIiiIiii ) == True :
 oO0 = open ( I1IIiiIiii ) . read ( )
else : oO0 = [ ]
Ii1iIiII1ii1 = oo00 . getSetting ( 'debug' )
if os . path . exists ( O0O ) == False :
 os . makedirs ( O0O )
def ooOooo000oOO ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0OoO00oOO0o = ''
 OOO00O = ''
 try :
  Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
  OOO00O = Oo0OoO00oOO0o . read ( )
  Oo0OoO00oOO0o . close ( )
 except : pass
 if OOO00O != '' :
  return OOO00O
 else :
  OOO00O = 'Failed'
  return OOO00O
  if 84 - 84: oO0oo0o * O00o0O00 . I11O0O0oOO00O00o + iI1ii11iIi1i
iiI111I1iIiI = [ ]
IIIi1I1IIii1II = ooOooo000oOO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if IIIi1I1IIii1II != 'Failed' :
 iiI111I1iIiI . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not IIIi1I1IIii1II != 'Failed' :
 O0 = ooOooo000oOO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if O0 != 'Failed' :
  iiI111I1iIiI . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not O0 != 'Failed' :
  ii1ii1ii = ooOooo000oOO ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if ii1ii1ii != 'Failed' :
   iiI111I1iIiI . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not ii1ii1ii != 'Failed' :
   oooooOoo0ooo = ooOooo000oOO ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if oooooOoo0ooo != 'Failed' :
    iiI111I1iIiI . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
I1I1IiI1 = ( str ( iiI111I1iIiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
III1iII1I1ii = I1I1IiI1 + 'GenieArt/NEW/'
if 61 - 61: Ii1IIIi1
if 86 - 86: ooOOOoO % ii1ii11IIIiiI - O0OOOoOoo0 - I1ii11iIi11i
def O000OOo00oo ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  oo0OOo = 'genie tv repo not being installed '
  ooOOO00Ooo ( )
 else :
  IiIIIi1iIi ( )
  if 68 - 68: Ii % Ii1I + Ii
def IiIIIi1iIi ( ) :
 if 31 - 31: IIiIiII11i . oOo0O0Ooo
 II1I = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 IIII = open ( OOOO0OOoO0O0 ) . read ( )
 iiIiI = open ( O0Oo000ooO00 ) . read ( )
 if 91 - 91: Ii1IIIi1 % ooOoO0O00 % iI11I1II1I1I
 IIi1I11I1II = re . compile ( 'version="([^"]*)" provider' ) . findall ( IIII )
 OooOoooOo = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( iiIiI )
 ii11IIII11I = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( II1I )
 OOooo = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( II1I )
 for oOooOOOoOo in IIi1I11I1II :
  i1Iii1i1I = oOooOOOoOo
  for OOoO00 in ii11IIII11I :
   if not OOoO00 == i1Iii1i1I :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    IiI111111IIII ( )
   if OOoO00 == i1Iii1i1I :
    i1Ii
 for ii111iI1iIi1 in OooOoooOo :
  OOO = ii111iI1iIi1
  for oo0OOo0 in OOooo :
   if not oo0OOo0 == OOO :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    ooOOO00Ooo ( )
   if oo0OOo0 == OOO :
    xbmc . sleep ( 100 )
    i1Ii
def I11IiI ( ) :
 O000OOo00oo ( )
 O0ooO0Oo00o ( )
 ooO0oOOooOo0 ( i1I1ii11i1Iii )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I1IiiiiI ( )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , OO0o , '' )
  ii1iII1II ( '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '' , 50006 , III1iII1I1ii + 'Contact-Us.png' , OO0o , '' )
  ii1iII1II ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , III1iII1I1ii + 'settings.png' , OO0o , '' )
  ii1iII1II ( '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , III1iII1I1ii + 'GenieUpdate.png' , OO0o , '' )
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , OO0o , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , OO0o , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , OO0o , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1I1IiI1 ) , 32 , III1iII1I1ii + 'BuildersToolbox.png' , OO0o , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   ii1iII1II ( '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , str ( I1I1IiI1 ) , 46 , III1iII1I1ii + 'SoruceList.png' , OO0o , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , OO0o , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '' , 10050 , III1iII1I1ii + 'Addons.png' , OO0o , '' )
  if Iii1I1I11iiI1 ( ) == 'android' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( I1I1IiI1 ) , 30039 , III1iII1I1ii + 'APKTools.png' , OO0o , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , str ( I1I1IiI1 ) , 39 , III1iII1I1ii + 'GenieTVRSSFeed.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
def I1IiiiiI ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , OO0o , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , OO0o , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , OO0o , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , OO0o , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
def ii1I ( ) :
 O0oO0 = [ '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  IiI111111IIII ( )
 if oO0O0OO0O == 1 :
  OO ( )
 if oO0O0OO0O == 2 :
  OoOoO ( )
 if oO0O0OO0O == 3 :
  Ii1I1i ( )
 if oO0O0OO0O == 4 :
  OOI1iI1ii1II ( i1I1ii11i1Iii )
 if oO0O0OO0O == 5 :
  iI111I11I1I1 . ok ( i1 , i1111 )
 if oO0O0OO0O == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if oO0O0OO0O == 7 :
  O0O0OOOOoo ( )
def oOooO0 ( ) :
 Ii1I1Ii = OOoO0 ( )
 OO0Oooo0oOO0O = Ii1I1Ii . replace ( II , "" )
 if os . path . exists ( Ii1I1Ii ) or not Ii1I1Ii == False :
  o00O0 = open ( Ii1I1Ii , mode = 'r' ) ; oOO0O00Oo0O0o = o00O0 . read ( ) ; o00O0 . close ( )
  ii1 ( "%s - %s" % ( i1 , OO0Oooo0oOO0O ) , oOO0O00Oo0O0o )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OOoO0 ( ) :
 I1iIIiiIIi1i = False
 if os . path . exists ( os . path . join ( II , 'xbmc.log' ) ) :
  I1iIIiiIIi1i = os . path . join ( II , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II , 'kodi.log' ) ) :
  I1iIIiiIIi1i = os . path . join ( II , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II , 'spmc.log' ) ) :
  I1iIIiiIIi1i = os . path . join ( II , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II , 'tvmc.log' ) ) :
  I1iIIiiIIi1i = os . path . join ( II , 'tvmc.log' )
 return I1iIIiiIIi1i
 if 66 - 66: Ii1IIIi1 - Ii1IIIi1 - Ii . Ii1I - O00o0O00
def oOOo0O00o ( url ) :
 if url == 'http://' : return False
 try :
  Oo0oOOo = urllib2 . Request ( url )
  Oo0oOOo . add_header ( 'User-Agent' , I1i1iiI1 )
  Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
  Oo0OoO00oOO0o . close ( )
 except Exception , iIiIi11 :
  return iIiIi11
 return True
 if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / oO0oo0o
def IiI ( ) :
 OOO00O = O0i1II1Iiii1I11 ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( OOO00O )
 if len ( IIi1I11I1II ) > 0 :
  for IIIii1I , i1I1ii11i1Iii , ooO0OO , O000OOO in IIi1I11I1II :
   ii1iII1II ( IIIii1I , i1I1ii11i1Iii , 50005 , ooO0OO , O000OOO , '' )
def IIo0o0O0O00oOOo ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   iIIIiIi ( )
  if oO0O0OO0O == 1 :
   OO0O0 ( )
  if oO0O0OO0O == 2 :
   I11I11 ( o000O0O )
  if oO0O0OO0O == 3 :
   I1i1i1iii ( i1I1ii11i1Iii )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']WISHES PC[/COLOR]' , str ( I1I1IiI1 ) , 1 , III1iII1I1ii + 'WISHESPC.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 16 - 16: iI1ii11iIi1i + ooOOOoO * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
def Oo0OO ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if II11iiii1Ii == '5knuckleshuffle' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , OO0o , '' )
   o0OIiII ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , OO0o , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , OO0o , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   ii1iII1II ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']STREAM CATEGORIES[/COLOR]' , str ( I1I1IiI1 ) , 90002 , III1iII1I1ii + 'cats.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , OO0o , '' )
 else :
  if II11iiii1Ii == '5knuckleshuffle' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , OO0o , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , OO0o , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   ii1iII1II ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 4004 , III1iII1I1ii + 'Movies.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( I1I1IiI1 ) , 4005 , III1iII1I1ii + 'TVShows.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , III1iII1I1ii + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 4007 , III1iII1I1ii + 'Kids.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , str ( I1I1IiI1 ) , 30032 , III1iII1I1ii + 'News.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'GenieTVTutorials.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , str ( I1I1IiI1 ) , 4008 , III1iII1I1ii + 'Hobbies.png' , OO0o , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '' , 10003 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , str ( I1I1IiI1 ) , 8040 , III1iII1I1ii + 'documentaries.png' , OO0o , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , str ( I1I1IiI1 ) , 7001 , III1iII1I1ii + 'DiscloseTV.png' , OO0o , '' )
   if 78 - 78: O00o0O00 - ii - Ii1I / O0OOOoOoo0 / IIiIiII11i
   if 29 - 29: oOo0O0Ooo % oOo0O0Ooo
   if 94 - 94: iI11I1II1I1I / I1ii11iIi11i % Ii1IIIi1 * Ii1IIIi1 * IIiIiII11i
   if 29 - 29: oO0o + OOooOOo / I11i / O00o0O00 * iI11I1II1I1I
   if 62 - 62: O00o0O00 / oO0oo0o - oO0o . I11O0O0oOO00O00o
   if 11 - 11: Ii1I . oO0o * ooOOOoO * ii + O0OOOoOoo0
   if 33 - 33: o0o00Oo0O * I11i - ii1ii11IIIiiI % ii1ii11IIIiiI
   if 18 - 18: ii1ii11IIIiiI / I1ii11iIi11i * ii1ii11IIIiiI + ii1ii11IIIiiI * Ii * Ii1I
   if 11 - 11: O0OOOoOoo0 / OOooOOo - ooOOOoO * ii + ii . OOooOOo
   if 26 - 26: iI1ii11iIi1i % Ii1I
   if 76 - 76: ooOOOoO * Ii1IIIi1
   if 52 - 52: O00o0O00
   if 19 - 19: oOo0O0Ooo
   if 25 - 25: iI1ii11iIi1i / O0OOOoOoo0
   if 31 - 31: O00o0O00 . o0o00Oo0O % oOo0O0Ooo . I11i + ooOOOoO
   if 71 - 71: ii1ii11IIIiiI . IIiIiII11i
   if 62 - 62: ii . I11O0O0oOO00O00o
   if 61 - 61: OOooOOo - O00o0O00 - ooOoO0O00
 I1I1i1I ( 'movies' , 'MAIN' )
def IiI1iIiIIIii ( ) :
 O0oO0 = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  oOoO ( )
 if oO0O0OO0O == 1 :
  oOoO00O0 ( )
 if oO0O0OO0O == 2 :
  OOIi1iI111II1I1 ( )
 if oO0O0OO0O == 3 :
  oOOOOoOO0o ( )
 if oO0O0OO0O == 4 :
  i1II1 ( )
 if oO0O0OO0O == 5 :
  i11i1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , IiiiiI1i1Iii , IIIii1I )
 if oO0O0OO0O == 6 :
  oo00oO0o ( )
 if oO0O0OO0O == 7 :
  iiii111II ( )
 if oO0O0OO0O == 8 :
  I11iIiI1I1i11 ( )
 if oO0O0OO0O == 9 :
  OOoooO00o0oo0 ( )
 if oO0O0OO0O == 10 :
  O00O ( )
  if 48 - 48: O0OOOoOoo0 / ii1ii11IIIiiI . iI11I1II1I1I * OOooOOo * oO0oo0o / ooOoO0O00
  if 92 - 92: I1ii11iIi11i % I1ii11iIi11i - I11i / OOooOOo
def O0ooO0Oo00o ( ) :
 if not os . path . exists ( o0 ) :
  ii1 ( 'Change Log 14/10/16 - v3.1.9' , 'Adult section fixed and new categories added, Complete overhaul of menus, New section added who can find it first???' )
  os . makedirs ( o0 )
  if 10 - 10: Ii1IIIi1 + I1ii11iIi11i * Ii1I + iI11I1II1I1I / ii1ii11IIIiiI / Ii1I
  if 42 - 42: oOo0O0Ooo
def oOoO ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   II1i11I ( )
  if oO0O0OO0O == 1 :
   ii1I1IIii11 ( i1I1ii11i1Iii )
  if oO0O0OO0O == 2 :
   O0o0oO ( )
  if oO0O0OO0O == 3 :
   IIIIiIiIi1 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if oO0O0OO0O == 4 :
   I11iiiiI1i ( )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
def iI1i11 ( ) :
 O000OOo00oo ( )
 OoOOoooOO0O ( )
 if 86 - 86: I11i
 if 5 - 5: ooOOOoO * OOooOOo
 o0OIiII ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  ii1iII1II ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , OO0o , '' )
 ii1iII1II ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , III1iII1I1ii + 'linkchannels.png' , OO0o , '' )
def O00O ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , Ooo , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Ooo , OO0o , '' )
 if 5 - 5: ii1ii11IIIiiI
 if 90 - 90: ii1ii11IIIiiI . O0OOOoOoo0 / iI1ii11iIi1i - I11O0O0oOO00O00o
 if 40 - 40: ii
 if 25 - 25: ooOOOoO + iI1ii11iIi1i / O0OOOoOoo0 . I11i % o0o00Oo0O * oO0o
 if 84 - 84: O0OOOoOoo0 % iI1ii11iIi1i + Ii
def oOoO00O0 ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   II1I1Ii ( )
  if oO0O0OO0O == 1 :
   Ooo0O0oooo ( )
  if oO0O0OO0O == 2 :
   iiI ( )
  if oO0O0OO0O == 3 :
   oOIIiIi ( )
  if oO0O0OO0O == 4 :
   OOoOooOoOOOoo ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , III1iII1I1ii + 'WatchSeries.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
def Iiii1iI1i ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1ii1ii11i1I = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   o0OoOO = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   O0O0Oo00 = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   oOoO00o = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   oO00O0 = '[COLOR' + iiI1IiI + ']HERO VISION[/COLOR]'
  O0oO0 = [ I1ii1ii11i1I , o0OoOO , O0O0Oo00 , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , oOoO00o , oO00O0 ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   i11i1 ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , IiiiiI1i1Iii , IIIii1I )
  if oO0O0OO0O == 1 :
   i11i1 ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLm5ldC9yZWFwZXIvbWFpbm1lbnUucGhw' ) ) , IiiiiI1i1Iii , IIIii1I )
  if oO0O0OO0O == 2 :
   IIi1IIIi ( )
  if oO0O0OO0O == 3 :
   i11i1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , IiiiiI1i1Iii , IIIii1I )
  if oO0O0OO0O == 4 :
   O00Ooo ( )
  if oO0O0OO0O == 5 :
   OOOO0OOO ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'TheReaper.png' , OO0o , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , OO0o , '' )
  if oo00 . getSetting ( 'Redemption Streams' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']Redemption Streams[/COLOR]' , ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'RedemptionStreams.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 1023 , III1iII1I1ii + 'ScoobyStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , '' , 1017 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'ITVStreams.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Test[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvdGVzdC5waHA=' ) ) , 1016 , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 3 - 3: oO0o
def oooOoOOO0oo0o ( ) :
 O000OOo00oo ( )
 ii1iII1II ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
def Oo0oooO0oO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 url = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( IiIiII1 )
 for OO0O00oOo , ii1II in IIi1I11I1II :
  if '[DIR]' in OO0O00oOo :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + ii1II + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii1II , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in ii1II :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + ii1II + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii1II , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in ii1II :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + ii1II + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ii1II , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 14 - 14: I11i * O00o0O00 + Ii1IIIi1 + o0o00Oo0O + Ii
def OOOO0OOO ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']HEROVISION SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 if 77 - 77: I11i / ii
def oOOOOoOO0o ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   IIii11I1i1I ( )
  if oO0O0OO0O == 1 :
   o0o0OO0O00o ( )
  if oO0O0OO0O == 2 :
   O0Oooo ( )
  if oO0O0OO0O == 3 :
   iiIi1i ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'SearchCartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1IiI1 ) , 21004 , III1iII1I1ii + 'watchcartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , III1iII1I1ii + 'Cartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , III1iII1I1ii + 'anime.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
def oo00oO0o ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , OO0o , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , III1iII1I1ii + 'Fitness.png' , OO0o , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']Go Fishing[/COLOR]' , str ( I1I1IiI1 ) , 8090 , III1iII1I1ii + 'GoFishing.png' , OO0o , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , III1iII1I1ii + 'GenieTVKitchen.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 27 - 27: O00o0O00 * O0OOOoOoo0 . ii1ii11IIIiiI % ooOOOoO * ooOOOoO . ooOoO0O00
 if 72 - 72: O00o0O00 % Ii1I + oO0o / oO0oo0o + ooOOOoO
 if 10 - 10: ii1ii11IIIiiI / O0OOOoOoo0 + Ii / iI1ii11iIi1i
def i1Ii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi1I11I1II = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIIi1I1IIii1II )
 for oo0OOo in IIi1I11I1II :
  oo0OOo = ( str ( oo0OOo ) )
  if os . path . exists ( xbmc . translatePath ( oo0OOo ) ) :
   OOOoOoO = ( oo0OOo ) . replace ( 'special://home/addons/' , '' )
   ii1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OOOoOoO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   oO0O0OO0O = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if oO0O0OO0O == 0 :
    iIIIII1ii1I ( oo0OOo )
    Ii1i1iI ( )
   elif oO0O0OO0O == 1 :
    IIiI1 ( oo0OOo )
  else :
   pass
   if 17 - 17: O00o0O00 / O00o0O00 / I11O0O0oOO00O00o
def IIiI1 ( addon ) :
 OOOoOoO = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 1 - 1: ooOoO0O00 . Ii % O00o0O00
def iIIIII1ii1I ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OooO0oo = os . path . join ( iIi1ii1I1 , 'default.py' )
 o0o0oOoOO0O = open ( OooO0oo , "w+" )
 if 16 - 16: ooOOOoO % iI11I1II1I1I . iI1ii11iIi1i
 o0o0oOoOO0O . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o0o0oOoOO0O . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o0o0oOoOO0O . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 59 - 59: oOo0O0Ooo * IIiIiII11i . o0o00Oo0O
 if 56 - 56: iI1ii11iIi1i - Ii1IIIi1 % oOo0O0Ooo - I11i
 if 51 - 51: o0o00Oo0O / O0OOOoOoo0 * iI11I1II1I1I + Ii1I + I11i
 if 98 - 98: iI11I1II1I1I * Ii1I * O00o0O00 + O0OOOoOoo0 % Ii % o0o00Oo0O
def O0o0oO ( ) :
 iI1I ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://www.join4films.com/' )
 IIi1I11I1II = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 80006 , III1iII1I1ii + 'Desi.png' )
def i1OO0oOOoo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  OooOoOo ( IIIii1I , url , 80007 , oOOO00o000o )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def iIi11i1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  url = ( url ) . replace ( ' ' , '%20' )
  oO00oo0o00o0o ( url )
def IiIIIIIi ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OoO0ooOO0o = 'http://www.join4films.com/?s=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 i1OO0oOOoo ( OoOo0oOooOoOO )
 if 60 - 60: ii % iI1ii11iIi1i * ooOoO0O00
 if 1 - 1: oOo0O0Ooo / ooOOOoO * O0OOOoOoo0
 if 1 - 1: I11O0O0oOO00O00o * I11i . OOooOOo / o0o00Oo0O
 if 100 - 100: ii1ii11IIIiiI . I11i * I1ii11iIi11i % o0o00Oo0O * o0o00Oo0O
 if 14 - 14: Ii1I . O0OOOoOoo0 + IIiIiII11i / Ii1IIIi1 / I11O0O0oOO00O00o
 if 74 - 74: o0o00Oo0O / ooOoO0O00
 if 78 - 78: ii . oO0o + O0OOOoOoo0 - ooOoO0O00
 if 31 - 31: ii . O00o0O00
 if 83 - 83: Ii1IIIi1 . o0o00Oo0O / I1ii11iIi11i / O00o0O00 - IIiIiII11i
 if 100 - 100: oO0o
 if 46 - 46: OOooOOo / iI11I1II1I1I % Ii1IIIi1 . iI11I1II1I1I * Ii1IIIi1
 if 38 - 38: Ii1I - Ii1IIIi1 / o0o00Oo0O . ii1ii11IIIiiI
 if 45 - 45: ii1ii11IIIiiI
 if 83 - 83: OOooOOo . ii
 if 58 - 58: Ii + ii % ii / ooOOOoO / Ii
 if 62 - 62: oO0o / Ii1I
 if 7 - 7: ii . ooOOOoO
def O000OOO0OOo ( ) :
 o0OIiII ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 o0OIiII ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 o0OIiII ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 o0OIiII ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 if 32 - 32: iI1ii11iIi1i * o0o00Oo0O
def O00oOo00o0o ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OoO0ooOO0o = 'http://imoviemax.se/?s=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 O00oO0 ( OoOo0oOooOoOO )
def O0Oo00OoOo ( url ) :
 ii1ii111 = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , i11111I1I in IIi1I11I1II :
  if IIIii1I in ii1ii111 :
   pass
  else :
   o0OIiII ( IIIii1I + ' - ' + i11111I1I + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
   ii1ii111 . append ( IIIii1I )
   if 11 - 11: ii . ii1ii11IIIiiI
def Oo0000oOo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , I11o0oO00oO0o0o0 in IIi1I11I1II :
  o0OIiII ( IIIii1I + ' - Views:' + I11o0oO00oO0o0o0 , url , 10075 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
  if 17 - 17: I11O0O0oOO00O00o . ooOOOoO - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
  if 39 - 39: ooOOOoO * I1ii11iIi11i + iI11I1II1I1I - ooOOOoO + O00o0O00
def O00oO0 ( url ) :
 o0iiiI1I1iIIIi1 = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIIi1I1IIii1II )
 for next in next :
  o0OIiII ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , IIIii1I , url in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 10075 , oOOO00o000o , oOOO00o000o , '' )
  o0iiiI1I1iIIIi1 . append ( IIIii1I )
  if 17 - 17: iI11I1II1I1I . ii / I11O0O0oOO00O00o % IIiIiII11i % ooOoO0O00 / Ii
def OOOIiiiii1iI ( img , name , url ) :
 img = img
 name = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIIi1I1IIii1II )
 for IIi , url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  ooOooo0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + ooOooo0
  oO0OO0 = ( IIi ) . replace ( 'play-' , 'Server ' )
  ii1iII1II ( oO0OO0 , ooOooo0 , 10076 , img , img , '' )
  if 82 - 82: ooOOOoO - ooOOOoO + OOooOOo
def II111Ii1i1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIIi1I1IIii1II )
 for ii1II in IIi1I11I1II :
  if '=m' in ii1II :
   OO0 ( ii1II )
  elif 'php' in ii1II :
   II111Ii1i1 ( url )
  else :
   IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ii1II )
   IIi1I11I1II = re . compile ( 'content="([^"]*)">' ) . findall ( IIIi1I1IIii1II )
   for I1i11iIIi in IIi1I11I1II :
    OO0 ( ii1II )
    if 28 - 28: iI1ii11iIi1i * I11i - oO0o
    if 42 - 42: Ii1I
    if 76 - 76: Ii1I * IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + oO0oo0o + Ii
def i1i1ii111 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IiI1i = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO0oOOoo00000 , oOo00 in IiI1i :
  print 'there ><><><><><><><><><><><><'
  oO0oOOoo00000 = oO0oOOoo00000
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oOo00 ) )
  for IIIii1I , i1iI11i1IIi in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   o0OIiII ( '[COLORred]' + oO0oOOoo00000 + '[/COLOR] - ' + IIIii1I + ' - [COLOR' + iiI1IiI + ']' + i1iI11i1IIi + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
 ii1IIi111 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO0oOOoo00000 , iI1 in ii1IIi111 :
  print 'there ><><><><><><><><><><><><'
  oO0oOOoo00000 = oO0oOOoo00000
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iI1 ) )
  for IIIii1I , i1iI11i1IIi in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   o0OIiII ( '[COLORred]' + oO0oOOoo00000 + '[/COLOR] - ' + IIIii1I + ' - [COLOR' + iiI1IiI + ']' + i1iI11i1IIi + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
   if 86 - 86: IIiIiII11i % Ii + iI1ii11iIi1i % Ii
   if 92 - 92: Ii - Ii1IIIi1 / O0OOOoOoo0 / oO0oo0o
   if 43 - 43: IIiIiII11i + O00o0O00 + Ii1IIIi1
def OOoOooOoOOOoo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii1IIi111 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii1IIi111 in ii1IIi111 :
  IIIii1I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
  for IIIii1I in IIIii1I :
   IIIii1I = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1IIi111 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iI1IIIii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
  for iI1IIIii in iI1IIIii :
   iI1IIIii = 'http:' + iI1IIIii
  ii1iII1II ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , '' , '' )
  if 7 - 7: ooOOOoO - I11O0O0oOO00O00o / IIiIiII11i * iI1ii11iIi1i . Ii1IIIi1 * Ii1IIIi1
  if 61 - 61: I11O0O0oOO00O00o % O0OOOoOoo0 - oO0o / I1ii11iIi11i
  if 4 - 4: ii - ooOoO0O00 % iI1ii11iIi1i - O00o0O00 * I11i
  if 85 - 85: ii * iI11I1II1I1I . Ii1IIIi1 / ii % oOo0O0Ooo % o0o00Oo0O
def IIIIiIiIi1 ( url ) :
 if 36 - 36: iI1ii11iIi1i / IIiIiII11i / ooOOOoO / ooOOOoO + Ii1I
 oO0Ooo0ooOO0 = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii1II , oOOO00o000o , IIIii1I , i1IIiIii1i in IIi1I11I1II :
  IIIii1I = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = O0i1II1Iiii1I11 ( ii1II )
  OooOoooOo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for ooOOO0OooOo , I1Ii in OooOoooOo :
   oOO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1Ii ) )
   for Ii1II in oOO :
    if IIIii1I in oO0Ooo0ooOO0 :
     pass
    else :
     ii1iII1II ( IIIii1I , ooOOO0OooOo , 8043 , oOOO00o000o , oOOO00o000o , Ii1II )
     I1I1i1I ( 'movies' , 'INFO' )
     oO0Ooo0ooOO0 . append ( IIIii1I )
     if 89 - 89: ii1ii11IIIiiI + ii + ii1ii11IIIiiI * ooOoO0O00 + iI11I1II1I1I % I11O0O0oOO00O00o
     if 59 - 59: O00o0O00 + Ii
def oo0OOo0O ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , IiiiiI1i1Iii , Ii1II , O000OOO , IIIii1I in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 10065 , IiiiiI1i1Iii , O000OOO , Ii1II )
 I1I1i1I ( 'movies' , 'INFO' )
 if 39 - 39: ii + oO0oo0o % O00o0O00 / O00o0O00
def I1i ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OoO0ooOO0o = 'https://www.youtube.com/results?search_query=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( OoOo0oOooOoOO )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in next :
  i1I1ii11i1Iii = 'https://www.youtube.com' + i1I1ii11i1Iii
  o0OIiII ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , i1I1ii11i1Iii , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for oOOO00o000o , i1I1ii11i1Iii , IIIii1I , ooo , I1Ii in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( IIIii1I )
  I1I1i1I ( 'tvshows' , 'INFO' )
  iI1IIIii = 'http:' + ( oOOO00o000o ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iI1IIIii
  i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
  ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , iI1IIIii , I1Ii )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oOOO00o000o , i1I1ii11i1Iii , IIIii1I , ooo in IIi1I11I1II :
   print 'im doing it'
   I1I1i1I ( 'tvshows' , 'INFO' )
   iI1IIIii = 'http:' + ( oOOO00o000o ) . replace ( 'https:' , '' )
   i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
   if '&' in i1I1ii11i1Iii :
    print ' i got here'
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    ii1IIi111 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for ii1IIi111 in ii1IIi111 :
     IIIii1I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
     for IIIii1I in IIIii1I :
      IIIii1I = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     i1I1ii11i1Iii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1IIi111 ) )
     for i1I1ii11i1Iii in i1I1ii11i1Iii :
      i1I1ii11i1Iii = 'https://www.youtube.com/w' + i1I1ii11i1Iii
     iI1IIIii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
     for iI1IIIii in iI1IIIii :
      iI1IIIii = 'http:' + iI1IIIii
     ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , OO0o , '' )
   elif IIIii1I in IIiiiiiiIi1I1 :
    pass
   elif 'user' in i1I1ii11i1Iii or 'elete' in IIIii1I :
    pass
   elif 'hannel' in i1I1ii11i1Iii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i1I1ii11i1Iii
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    ii1iiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for oOOO00o000o , i1I1ii11i1Iii , IIIii1I in ii1iiIi1 :
     if 'outube' in i1I1ii11i1Iii or 'list' in i1I1ii11i1Iii :
      pass
     elif 'atch' in i1I1ii11i1Iii :
      i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '/watch?v=' , '' )
      ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOOO00o000o , 'http:' + oOOO00o000o , '' )
     else :
      pass
   else :
    ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , iI1IIIii , '' )
    if 34 - 34: O00o0O00
def OooO0ooo0o ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for url in next :
  url = 'https://www.youtube.com' + url
  o0OIiII ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for oOOO00o000o , url , IIIii1I , ooo , I1Ii in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( IIIii1I )
  I1I1i1I ( 'tvshows' , 'INFO' )
  iI1IIIii = 'http:' + ( oOOO00o000o ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iI1IIIii
  url = 'http://www.youtube.com' + url
  ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , iI1IIIii , I1Ii )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oOOO00o000o , url , IIIii1I , ooo in IIi1I11I1II :
   I1I1i1I ( 'tvshows' , 'INFO' )
   iI1IIIii = 'http:' + ( oOOO00o000o ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    ii1IIi111 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for ii1IIi111 in ii1IIi111 :
     IIIii1I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
     for IIIii1I in IIIii1I :
      IIIii1I = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii1IIi111 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iI1IIIii = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii1IIi111 ) )
     for iI1IIIii in iI1IIIii :
      iI1IIIii = 'http:' + iI1IIIii
     ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , OO0o , '' )
   elif IIIii1I in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in IIIii1I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    ii1iiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for oOOO00o000o , url , IIIii1I in ii1iiIi1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOOO00o000o , 'http:' + oOOO00o000o , '' )
     else :
      pass
   else :
    ii1iII1II ( '[COLORred]' + ooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii , iI1IIIii , '' )
    if 47 - 47: ii
    if 4 - 4: oOo0O0Ooo % I11O0O0oOO00O00o
def OoOOoooOO0O ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  I1 = open ( O000oo0O )
  IIi1I11I1II = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( I1 ) )
  for oOO0o0 , iiI11I1i1i1iI in IIi1I11I1II :
   if oOO0o0 == 'needs replacing' or iiI11I1i1i1iI == 'needs replacing' :
    OoOOo000o0 ( )
  o0OIiII ( '[COLOR' + iiI1IiI + ']G-Tv PRIVATE LIST[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , III1iII1I1ii + 'PrivateList.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']G-Tv ULTIMATE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
  if 12 - 12: IIiIiII11i . I11O0O0oOO00O00o / O00o0O00
def O00OO0oO ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 OoOOo000o0 ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 25 - 25: I1ii11iIi11i % Ii1I * O0OOOoOoo0
def I11oo0ooOO ( ) :
 o0OIiII ( 'Full List' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'PPV' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Entertainment' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Factual' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Movie Channels' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'US Movie Channels TEST' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Kids' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Music' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'UK Sports' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'International Sports' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'News UK & International' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'German' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'Arabic' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'TV Series Latest' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'VOD Latest' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 o0OIiII ( 'VOD Bollywood' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 if 24 - 24: oO0o % oO0o * iI11I1II1I1I
def III ( name ) :
 iIiIi11Ii = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , oOOO00o000o , iIII1i1i , i1I1ii11i1Iii in IIi1I11I1II :
  if iIiIi11Ii == 'Full List' :
   i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
   ii1iII1II ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , oOOO00o000o , oOOO00o000o , '' )
  else :
   iIiIi11Ii = ( iIiIi11Ii ) . replace ( 'World' , 'القنوات العربية' )
   if iIiIi11Ii in iIII1i1i :
    i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
    print i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    ii1iII1II ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , oOOO00o000o , oOOO00o000o , '' )
   else :
    pass
    if 35 - 35: IIiIiII11i * I11O0O0oOO00O00o - ii . I11O0O0oOO00O00o . I11O0O0oOO00O00o
def I1II ( name ) :
 iIiIi11Ii = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , oOOO00o000o , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
  ii1iII1II ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , oOOO00o000o , oOOO00o000o , '' )
 else :
  ii1iII1II ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 79 - 79: oO0o . Ii1IIIi1 * iI1ii11iIi1i - O00o0O00 + O0OOOoOoo0
  if 14 - 14: Ii - Ii1IIIi1 * OOooOOo
  if 51 - 51: Ii1I / iI11I1II1I1I % oO0oo0o + I11i * O0OOOoOoo0 + ii1ii11IIIiiI
  if 77 - 77: O0OOOoOoo0 * OOooOOo
  if 14 - 14: I11O0O0oOO00O00o % I11O0O0oOO00O00o / ooOOOoO
  if 72 - 72: ooOoO0O00 - IIiIiII11i - O00o0O00 + O00o0O00 * I11i * O00o0O00
  if 33 - 33: I1ii11iIi11i
  if 49 - 49: oO0o % Ii1IIIi1 % Ii1IIIi1 / Ii1IIIi1
  if 53 - 53: iI11I1II1I1I
  if 68 - 68: ii % IIiIiII11i
  if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % I11O0O0oOO00O00o * I11O0O0oOO00O00o * Ii1I
  if 24 - 24: IIiIiII11i % ii1ii11IIIiiI - O0OOOoOoo0 + oOo0O0Ooo * Ii1I
def iIIIiIi ( ) :
 o0OIiII ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( o00OO00OoO ) :
  o0OIiII ( 'Backup Genie Favourites' , i1I1ii11i1Iii , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( oO0Oo ) :
  o0OIiII ( 'Backup Ivue Config' , oO0Oo , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( oOOoo0Oo ) :
  o0OIiII ( 'Backup Kodi Favourites' , oOOoo0Oo , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 2 - 2: iI1ii11iIi1i - ooOOOoO
  if 83 - 83: oO0oo0o % I11i % iI1ii11iIi1i - IIiIiII11i * O00o0O00 / ii
  if 18 - 18: oO0o + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
zip = oo00 . getSetting ( 'zip' )
oooOOOO0oooo = xbmc . translatePath ( os . path . join ( zip ) )
def oooooOo0 ( ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 92 - 92: I11i + ii1ii11IIIiiI / I1ii11iIi11i % oO0o % ooOOOoO . ii
  if 52 - 52: O0OOOoOoo0 / Ii - O00o0O00 . ooOOOoO % iI11I1II1I1I + I11i
  if 71 - 71: oO0oo0o % I11O0O0oOO00O00o * OOooOOo . o0o00Oo0O / iI1ii11iIi1i . Ii1I
def oOOOo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = o00OO00OoO
  elif 'Ivue' in name :
   url = oO0Oo
  elif 'Kodi' in name :
   url = oOOoo0Oo
  oooooOo0 ( )
  OO0O0o0o0 = open ( url ) . read ( )
  iIIIIIiI1I1 = os . path . join ( oooOOOO0oooo , description . split ( 'Your ' ) [ 1 ] )
  o00O0 = open ( iIIIIIiI1I1 , mode = 'w' )
  o00O0 . write ( OO0O0o0o0 )
  o00O0 . close ( )
 else :
  if 'guisettings.xml' in description :
   I11I1IIiiII1 = open ( os . path . join ( oooOOOO0oooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IIIIIii1ii11 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi1I11I1II = re . compile ( IIIIIii1ii11 ) . findall ( I11I1IIiiII1 )
   for type , OOOooo0OooOoO , oOoOOOo in IIi1I11I1II :
    oOoOOOo = oOoOOOo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OOOooo0OooOoO , oOoOOOo ) )
  else :
   iIIIIIiI1I1 = os . path . join ( url )
   OO0O0o0o0 = open ( os . path . join ( oooOOOO0oooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o00O0 = open ( iIIIIIiI1I1 , mode = 'w' )
   o00O0 . write ( OO0O0o0o0 )
   o00O0 . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 43 - 43: ooOoO0O00
 if 23 - 23: Ii1IIIi1 + I11O0O0oOO00O00o . OOooOOo * oOo0O0Ooo + Ii1I
 if 18 - 18: ooOOOoO * I11i . ooOOOoO / o0o00Oo0O
 if 8 - 8: I11i
def II1II1 ( ) :
 Ii11iI = 1
 oooooOo0 ( )
 oO00OoOO = xbmc . translatePath ( os . path . join ( oooOOOO0oooo , 'Build Backup' , 'Full Backup' , '' ) )
 I11IIiIiI = xbmc . translatePath ( os . path . join ( oooOOOO0oooo , 'Build Backup' , 'my_full_backup.zip' ) )
 iIIIi1i1I11i = xbmc . translatePath ( os . path . join ( oooOOOO0oooo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oO00OoOO ) :
  os . makedirs ( oO00OoOO )
 oOO0OO0OO = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oOO0OO0OO ) : return False , 0
 oOOoooO = oOO0OO0OO
 i1ii11 = xbmc . translatePath ( os . path . join ( oO00OoOO , oOOoooO + '.zip' ) )
 ii1i = [ 'plugin.video.GenieTv' ]
 IIioo0OO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 IiiI11i1I = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iiIii1IIi = "Creating full backup of existing build"
 ii1IiIiI1 = "Creating Community Build"
 OOOoOo00O = "Archiving..."
 O0ooOo0o0Oo = ""
 OooO0oOo = "Please Wait"
 oOOo00O0OOOo ( I11 , i1ii11 , ii1IiIiI1 , OOOoOo00O , O0ooOo0o0Oo , OooO0oOo , IiiI11i1I , OOo0 )
 time . sleep ( 1 )
 i11I1I1iiI = xbmc . translatePath ( os . path . join ( oO00OoOO , oOOoooO + '_guisettings.zip' ) )
 I1i1iii1Ii = zipfile . ZipFile ( i11I1I1iiI , mode = 'w' )
 try :
  I1i1iii1Ii . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1i1iii1Ii . close ( )
 if Ii11iI == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I11IIiIiI , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + i1ii11 + '[/COLOR]' )
  if 23 - 23: Ii
def oOOo00O0OOOo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 II1I11IIi = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OoOOo = len ( sourcefile )
 iii1 = [ ]
 oOO0oo = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for II1iIi1IiIii , I111I11I111 , iiiiI11ii in os . walk ( sourcefile ) :
  for file in iiiiI11ii :
   oOO0oo . append ( file )
 O0i1i1II1i11 = len ( oOO0oo )
 for II1iIi1IiIii , I111I11I111 , iiiiI11ii in os . walk ( sourcefile ) :
  I111I11I111 [ : ] = [ o00o for o00o in I111I11I111 if o00o not in exclude_dirs ]
  iiiiI11ii [ : ] = [ o00O0 for o00O0 in iiiiI11ii if o00O0 not in exclude_files ]
  for file in iiiiI11ii :
   iii1 . append ( file )
   iii11II1I = len ( iii1 ) / float ( O0i1i1II1i11 ) * 100
   o0oOoO00o . update ( int ( iii11II1I ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iI111I11i = os . path . join ( II1iIi1IiIii , file )
   if not 'temp' in I111I11I111 :
    if not 'plugin.program.originwizard' in I111I11I111 :
     import time
     I1II1i11I1 = '01/01/1980'
     iiIiIiII = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iI111I11i ) ) )
     if iiIiIiII > I1II1i11I1 :
      II1I11IIi . write ( iI111I11i , iI111I11i [ OoOOo : ] )
 II1I11IIi . close ( )
 o0oOoO00o . close ( )
 if 37 - 37: I11O0O0oOO00O00o / ooOOOoO + IIiIiII11i
 if 18 - 18: Ii1I
def O00Ooo ( ) :
 O000OOo00oo ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 if 23 - 23: IIiIiII11i
 if 24 - 24: iI11I1II1I1I + iI11I1II1I1I * Ii1IIIi1
def i1I11iIII1i1I ( ) :
 O000OOo00oo ( )
 O0oO0 = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  II1i11I ( )
 if oO0O0OO0O == 1 :
  II1I1Ii ( )
 if oO0O0OO0O == 2 :
  IIii11I1i1I ( )
 if oO0O0OO0O == 3 :
  I1i ( )
  if 63 - 63: I1ii11iIi11i + ii1ii11IIIiiI - IIiIiII11i
  if 2 - 2: ooOOOoO
  if 97 - 97: oO0oo0o - ii
  if 79 - 79: OOooOOo % ooOOOoO % I1ii11iIi11i
  if 29 - 29: ii . oOo0O0Ooo % Ii1I - Ii1IIIi1
  if 8 - 8: ooOoO0O00
  if 32 - 32: oO0oo0o / IIiIiII11i
  if 45 - 45: Ii1I + oO0o * Ii / O00o0O00 % I11O0O0oOO00O00o * o0o00Oo0O
  if 17 - 17: o0o00Oo0O
def OOooO0o ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   i11i1 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , IiiiiI1i1Iii , IIIii1I )
  if oO0O0OO0O == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if oO0O0OO0O == 2 :
   ii1iI1iI1 ( )
  if oO0O0OO0O == 3 :
   o00oOOO ( )
  if oO0O0OO0O == 4 :
   OoOO0OOoo ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if oO0O0OO0O == 5 :
   IIIi11IiIiii ( )
  if oO0O0OO0O == 6 :
   iIi1IIiI ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if oO0O0OO0O == 7 :
   I11i11I1iiII ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if oO0O0OO0O == 8 :
   IiiI ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if oO0O0OO0O == 9 :
   i11ii ( )
  if oO0O0OO0O == 10 :
   i11I1 ( )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , III1iII1I1ii + 'Quicksilver.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , OO0o , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 1030 , III1iII1I1ii + 'MUSIC.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , OO0o , '' )
  if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + Ii1IIIi1 * iI11I1II1I1I % iI1ii11iIi1i
 I1I1i1I ( 'movies' , 'MAIN' )
 if 25 - 25: I11O0O0oOO00O00o + OOooOOo . I11i % OOooOOo * O00o0O00
def ii1IiIi11 ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   iiiii1ii1 ( )
  if oO0O0OO0O == 1 :
   IiI ( )
  if oO0O0OO0O == 2 :
   oOooO0 ( )
  if oO0O0OO0O == 3 :
   ooO0oOOooOo0 ( i1I1ii11i1Iii )
  if oO0O0OO0O == 4 :
   IiiiI1 ( i1I1ii11i1Iii )
  if oO0O0OO0O == 5 :
   Ii1i1iI ( )
  if oO0O0OO0O == 6 :
   OOOo0 ( )
  if oO0O0OO0O == 7 :
   OOo0Oo0OOo0 ( )
 else :
  ii1iII1II ( 'CLLEANUP' , 'url' , 9666 , III1iII1I1ii + 'MAIN5.png' , OO0o , '' )
  ii1iII1II ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , OO0o , '' )
  ii1iII1II ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , OO0o , '' )
  ii1iII1II ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , OO0o , '' )
  ii1iII1II ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , OO0o , '' )
  ii1iII1II ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , OO0o , 'Force Refresh All Repos' )
  o0OIiII ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , III1iII1I1ii + '1.jpg' , OO0o , 'Fix Corrupt Database' )
  ii1iII1II ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , OO0o , '' )
  ii1iII1II ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , OO0o , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 19 - 19: I11O0O0oOO00O00o + IIiIiII11i
  if 84 - 84: o0o00Oo0O - IIiIiII11i . I1ii11iIi11i / oO0oo0o . ii + Ii
 I1I1i1I ( 'movies' , 'MAIN' )
 if 86 - 86: I11O0O0oOO00O00o / I11i - I11i + Ii1I + oO0oo0o
 if 33 - 33: I11i . Ii1IIIi1 . ooOOOoO . ooOoO0O00
def i1i1II ( ) :
 O000OOo00oo ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , III1iII1I1ii + 'repos.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']NEW[/COLOR]' , str ( I1I1IiI1 ) , 22 , III1iII1I1ii + 'NEW.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']IPTV[/COLOR]' , str ( I1I1IiI1 ) , 23 , III1iII1I1ii + 'IPTV.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']VIDEO[/COLOR]' , str ( I1I1IiI1 ) , 24 , III1iII1I1ii + 'VIDEO.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SPORTS[/COLOR]' , str ( I1I1IiI1 ) , 25 , III1iII1I1ii + 'SPORTS.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 26 , III1iII1I1ii + 'KIDS.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 27 , III1iII1I1ii + 'MUSIC.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']PROGRAMS[/COLOR]' , str ( I1I1IiI1 ) , 28 , III1iII1I1ii + 'PROGRAMS.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']XXX[/COLOR]' , 'URL' , 29 , III1iII1I1ii + 'XXX.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 49 - 49: Ii1I
 if 84 - 84: I11O0O0oOO00O00o - I1ii11iIi11i / o0o00Oo0O - ii1ii11IIIiiI
def ii1iI1II11ii ( ) :
 O000OOo00oo ( )
 ii1iII1II ( 'CHECK ADVANCED XML' , str ( I1I1IiI1 ) , 8 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'MUCKYS XML' , str ( I1I1IiI1 ) + '/wizard/muckys.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( '0CACHE XML' , str ( I1I1IiI1 ) + '/wizard/0cache.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'MIKEY1234 XML' , str ( I1I1IiI1 ) + '/wizard/mikey.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'TUXENS XML' , str ( I1I1IiI1 ) + '/wizard/tuxens.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'P2P RECOMMENDED XML1' , str ( I1I1IiI1 ) + '/wizard/p2p1.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'P2P RECOMMENDED XML2' , str ( I1I1IiI1 ) + '/wizard/p2p2.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 ii1iII1II ( 'DELETE XML' , str ( I1I1IiI1 ) , 11 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 8 - 8: O0OOOoOoo0 * o0o00Oo0O
def OO0O0 ( ) :
 O000OOo00oo ( )
 ii1iII1II ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , OO0o , '' )
 ii1iII1II ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , III1iII1I1ii + 'MyOnlineZip.png' , OO0o , '' )
 if 73 - 73: I11i / oO0oo0o / I11O0O0oOO00O00o / oO0o
def III1ii ( ) :
 O000OOo00oo ( )
 ii1iII1II ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , OO0o , '' )
 ii1iII1II ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , OO0o , '' )
 ii1iII1II ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , OO0o , '' )
 ii1iII1II ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , OO0o , '' )
 if 41 - 41: O0OOOoOoo0 . I1ii11iIi11i + oOo0O0Ooo
 if 100 - 100: iI1ii11iIi1i + oO0o
 if 73 - 73: ooOoO0O00 - ii1ii11IIIiiI % O0OOOoOoo0 / oO0o
def Ii1I1i ( ) :
 O000OOo00oo ( )
 O0oO0 = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  III1iii1i11iI ( )
 if oO0O0OO0O == 0 :
  OoO ( i1I1ii11i1Iii )
 if oO0O0OO0O == 0 :
  ii1iI111 ( i1I1ii11i1Iii )
  if 80 - 80: O00o0O00 % Ii1I
  if 91 - 91: I11O0O0oOO00O00o / o0o00Oo0O - iI1ii11iIi1i . oOo0O0Ooo
  if 82 - 82: ooOOOoO * O00o0O00 / oO0oo0o
 I1I1i1I ( 'movies' , 'MAIN' )
 if 2 - 2: oOo0O0Ooo + I11i . I11i . o0o00Oo0O / I11O0O0oOO00O00o
def iIiiIiiIi ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi1I11I1II = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( OOO00O )
 for oOOO00o000o , IIIii1I in IIi1I11I1II :
  ii1iII1II ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOOO00o000o , oOOO00o000o , '' )
 I1I1i1I ( 'tvshows' , 'INFO' )
 if 40 - 40: I11i
def oOOo0oo0o0o0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( iIii1Ooo0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 5 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 86 - 86: o0o00Oo0O
def III1iii1i11iI ( ) :
 O000OOo00oo ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , OO0o , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 95 - 95: Ii1IIIi1 * O00o0O00 . OOooOOo . ooOoO0O00 . ooOoO0O00 - I11i
def ii1iIIiii1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + ooOo0O0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 65 - 65: O0OOOoOoo0 + o0o00Oo0O
def IiII1iiI ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 63 - 63: I11i * Ii1IIIi1
def O0oOoo0OoO0O ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oo00IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 87 - 87: I11i % iI11I1II1I1I
def O00 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 32 - 32: iI11I1II1I1I * ooOOOoO / iI1ii11iIi1i % ooOOOoO
def OoO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + i111i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 40 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 19 - 19: IIiIiII11i - ooOoO0O00 - O00o0O00 / O00o0O00 + OOooOOo
def OO0Oooo0oo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + I1i111IiIiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 5 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 39 - 39: I11O0O0oOO00O00o - Ii1I
def OO ( ) :
 O0oO0 = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  OOO0o0OO0OO ( )
 if oO0O0OO0O == 1 :
  oOo0O ( )
 if oO0O0OO0O == 2 :
  III1i111i ( )
  if 42 - 42: Ii1I / ooOoO0O00 % OOooOOo
  if 26 - 26: iI1ii11iIi1i * iI11I1II1I1I % oO0o . I11i + I1ii11iIi11i
  if 80 - 80: I1ii11iIi11i * iI1ii11iIi1i + Ii1I * O00o0O00
  if 16 - 16: I11O0O0oOO00O00o / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . oO0oo0o
def oOo0O ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , iIi1iIIIiIiI in IIi1I11I1II :
  iI1I ( 'Android Apps' + iIi1iIIIiIiI , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'apps.png' )
 for i1I1ii11i1Iii , iIi1iIIIiIiI in OooOoooOo :
  iI1I ( 'Android Games' + iIi1iIIIiIiI , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I1i1I ( 'movies' , 'MAIN' )
def OooOo000o0o ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if '/cat' in url :
   iI1I ( ( IIIii1I ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def iI1I1iII1i ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if '/app' in url :
   iI1I ( ( IIIii1I ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , III1iII1I1ii + 'APK.png' )
def iiIIii ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 oO0Oo0O0 = url
 if "page=" in str ( url ) :
  oO0Oo0O0 = url . split ( '?' ) [ 0 ]
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if 'apk' in url :
   ii1iII1II ( ( IIIii1I ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOOO00o000o )
 if len ( OooOoooOo ) > 1 :
  OooOoooOo = str ( OooOoooOo [ len ( OooOoooOo ) - 1 ] )
 ii1iII1II ( 'Next Page' , oO0Oo0O0 + str ( OooOoooOo ) , 30037 , III1iII1I1ii + 'Next.png' )
def I1iIiI1IiIIII ( name , url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 name = name
 IIi1I11I1II = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  url = 'https://www.apkfiles.com' + url
  I1iiIi111I ( name , url , 'Brackets' )
def III1i111i ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OoO0ooOO0o = 'https://www.apkfiles.com/search?q=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 iiIIii ( OoOo0oOooOoOO )
 if 34 - 34: Ii - IIiIiII11i / oOo0O0Ooo % I11i
def iI1IiiiI11 ( url ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( OO0OO0O , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 O0oOo = os . path . join ( O0o0O0OO00o , IIIii1I + '.apk' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 69 - 69: I1ii11iIi11i * IIiIiII11i * O0OOOoOoo0 . Ii1IIIi1 - Ii1I
def I11iiIIiI1ii ( url ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 O0oOo = os . path . join ( O0o0O0OO00o , IIIii1I + '.mp4' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 12 - 12: ii1ii11IIIiiI % Ii + I11i + ii1ii11IIIiiI / I11O0O0oOO00O00o
 if 53 - 53: ooOOOoO . ii1ii11IIIiiI % iI11I1II1I1I % OOooOOo % I11O0O0oOO00O00o
def o0OoOoOOoOo0o ( name , url , description ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 O0oOo = os . path . join ( O0o0O0OO00o , name )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 iIiii = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIiii
 print '======================================='
 extract . all ( O0oOo , iIiii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 2 - 2: ooOoO0O00 - oOo0O0Ooo + I11O0O0oOO00O00o . IIiIiII11i
 if 25 - 25: oO0oo0o
 if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
 if 43 - 43: Ii1I - Ii1IIIi1
 if 70 - 70: Ii1IIIi1 / O00o0O00 % O0OOOoOoo0 - iI1ii11iIi1i
def OOO0o0OO0OO ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1I11I1II = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOO00O )
 for IIIii1I , i1I1ii11i1Iii , ooO0OO , O000OOO , i1II11Iii1I in IIi1I11I1II :
  ii1iII1II ( IIIii1I , i1I1ii11i1Iii , 80003 , ooO0OO , III1iII1I1ii + 'APKToolsB.png' , i1II11Iii1I )
def oO00OoOOOo ( apk , ret = None ) :
 if apk == "kodi" :
  Oo0 = "https://kodi.tv/download/"
  OOO00O = O0i1II1Iiii1I11 ( Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( OOO00O )
  if len ( IIi1I11I1II ) == 1 :
   o0OOOOO0O = IIi1I11I1II [ 0 ] [ 0 ]
   oOOoooO = IIi1I11I1II [ 0 ] [ 1 ]
   I1I1IiIi1 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( o0OOOOO0O , oOOoooO )
  if ret == 'version' : return o0OOOOO0O
  else : return I1I1IiIi1
 elif apk == "spmc" :
  oOO0o0oo0 = 'https://github.com/koying/SPMC/releases/latest/'
  OOO00O = O0i1II1Iiii1I11 ( oOO0o0oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( OOO00O )
  o0OOOOO0O = re . sub ( '<[^<]+?>' , '' , IIi1I11I1II [ 0 ] ) . replace ( ' ' , '' )
  I1I1IiIi1 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( o0OOOOO0O , o0OOOOO0O )
  if ret == 'version' : return o0OOOOO0O
  else : return I1I1IiIi1
def I1iiIi111I ( name , url ) :
 if Iii1I1I11iiI1 ( ) == 'android' :
  oOo000O = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not oOo000O : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  IiiIIi = name
  if oOo000O :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not oOOo0O00o ( url ) == True : iIIooO0o0O0Oo ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % IiiIIi , '' , 'Please Wait' )
   O0oOo = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( O0oOo )
   except : pass
   downloader . download ( url , O0oOo , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    I1i1iii1Ii = zipfile . ZipFile ( O0oOo )
    for file in I1i1iii1Ii . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as o00O0 :
       O00o0O = file . split ( '/' ) [ 1 ]
       o00O0 . write ( I1i1iii1Ii . read ( file ) )
       xbmc . sleep ( 500 )
       o00O0 . close ( )
       try :
        os . remove ( O0oOo )
       except :
        pass
       O0oOo = os . path . join ( oooOOOOO , O00o0O )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + O0oOo + '")' )
  else : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 32 - 32: I11i + OOooOOo - ii
 if 39 - 39: ii * O00o0O00 * o0o00Oo0O . I11O0O0oOO00O00o . oO0o + O0OOOoOoo0
 if 9 - 9: OOooOOo + oO0oo0o % ii + I11i
 if 56 - 56: ii + Ii1I - Ii1IIIi1
def III1I1 ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( OOO00O )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  i1I1ii11i1Iii = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + i1I1ii11i1Iii )
  ii1111Ii1i ( ( IIIii1I ) . replace ( '_' , ' ' ) , i1I1ii11i1Iii )
  if 48 - 48: o0o00Oo0O * iI1ii11iIi1i - o0o00Oo0O / iI1ii11iIi1i + OOooOOo
def ii1111Ii1i ( name , url ) :
 if Iii1I1I11iiI1 ( ) == 'android' :
  oOo000O = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not oOo000O : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  IiiIIi = name
  if oOo000O :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not oOOo0O00o ( url ) == True : iIIooO0o0O0Oo ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % IiiIIi , '' , 'Please Wait' )
   O0oOo = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( O0oOo )
   except : pass
   downloader . download ( url , O0oOo , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + O0oOo + '")' )
  else : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIIooO0o0O0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 52 - 52: oO0o % iI1ii11iIi1i * IIiIiII11i
 if 4 - 4: I11O0O0oOO00O00o % o0o00Oo0O - ii + O0OOOoOoo0 . oO0oo0o % IIiIiII11i
def Iiii1iiiIiI1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 5 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'INFO' )
 if 27 - 27: iI1ii11iIi1i + oOo0O0Ooo * iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % iI1ii11iIi1i - iI11I1II1I1I
def I1i1i1iii ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 30015 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 17 - 17: I11O0O0oOO00O00o / I11i % I1ii11iIi11i
def o0o ( url , iconimage , fanart ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 ooOooo0 = url
 oOOO00o000o = iconimage
 fanart = fanart
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for ii1II , IIIii1I in IIi1I11I1II :
  if '.mp4' in IIIii1I :
   ii1iII1II ( 'Watch VIDEO' , url + '/' + ii1II , 222 , oOOO00o000o , fanart , '' )
  if 'description' in IIIii1I :
   ii1iII1II ( 'Read Description' , url + '/' + ii1II , 30017 , oOOO00o000o , fanart , '' )
  if 'images' in IIIii1I :
   o0OIiII ( 'View Images' , url + '/' + ii1II , 30018 , oOOO00o000o , fanart , '' )
  if 'url' in IIIii1I :
   ii1iII1II ( 'Install Build On Android' , url + '/' + ii1II , 30016 , oOOO00o000o , fanart , '' )
  if 'url' in IIIii1I :
   ii1iII1II ( 'Install Build On Pc' , url + '/' + ii1II , 30019 , oOOO00o000o , fanart , '' )
 I1I1i1I ( 'movies' , 'INFO' )
 if 93 - 93: O0OOOoOoo0 % Ii % ii1ii11IIIiiI
def O00OooO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  I1IiI1iI11 ( url )
  if 2 - 2: iI11I1II1I1I
def iiii1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  OO0o0oO0O000o ( url )
  if 47 - 47: ii1ii11IIIiiI - oO0o / iI1ii11iIi1i * ii / iI1ii11iIi1i . I1ii11iIi11i
def iiII1IiIi1iI1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'desc="([^"]*)"' ) . findall ( OOO00O )
 for oOiiI1Ii11II1I in IIi1I11I1II :
  ii1 ( 'Description:' , oOiiI1Ii11II1I )
  if 44 - 44: iI1ii11iIi1i % Ii - Ii1IIIi1 * Ii1I + I1ii11iIi11i * O00o0O00
def IiI1iI1IiiIi1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 url = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for ii1II , IIIii1I in IIi1I11I1II :
  if 'png' in IIIii1I :
   ii1iII1II ( 'image' , '' , '' , url + '/' + ii1II , url + '/' + ii1II , '' )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 90 - 90: o0o00Oo0O + I11O0O0oOO00O00o - ii . I11O0O0oOO00O00o
def oOII1ii1ii11I1 ( name , url , description ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 O0oOo = os . path . join ( O0o0O0OO00o , name + '.zip' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0ooOO0o
 print '======================================='
 extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ii1i1iI ( )
 if 71 - 71: ii
 if 5 - 5: OOooOOo % ii
def OO0o0oO0O000o ( url ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0oOo = os . path . join ( O0o0O0OO00o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0ooOO0o
 print '======================================='
 extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
 OO0I111i1I ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iiiii1ii1 ( )
 if 14 - 14: iI1ii11iIi1i % oOo0O0Ooo - iI11I1II1I1I . O00o0O00 + oO0o - ii1ii11IIIiiI
def I1IiI1iI11 ( url ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 O0oOo = os . path . join ( O0o0O0OO00o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0ooOO0o
 print '======================================='
 extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
 OO0I111i1I ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iiiii1ii1 ( )
 if 5 - 5: Ii1IIIi1
def OOiI1 ( name , url , description ) :
 o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 O0oOo = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print o0ooOO0o
 print '======================================='
 extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iiiii1ii1 ( )
 if 42 - 42: O00o0O00 % oO0oo0o / oO0o - oO0oo0o * Ii
def Iii1I1I11iiI1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def Ii1I1Ii ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo0o0O00 , log ) )
 if not os . path . exists ( oOo0oooo00o ) : os . makedirs ( oOo0oooo00o )
 if not os . path . exists ( oO0o0o0ooO0oO ) : o00O0 = open ( oO0o0o0ooO0oO , 'w' ) ; o00O0 . close ( )
 with open ( oO0o0o0ooO0oO , 'a' ) as o00O0 :
  iI1IiiiIiI1Ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  o00O0 . write ( iI1IiiiIiI1Ii . rstrip ( '\r\n' ) + '\n' )
def iiiii1ii1 ( ) :
 oO0O0OO0O = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oO0O0OO0O == 0 : return
 elif oO0O0OO0O == 1 : pass
 Oo000 = Iii1I1I11iiI1 ( )
 Ii1I1Ii ( "Platform: " + str ( Oo000 ) )
 os . _exit ( 1 )
 Ii1I1Ii ( "Force close failed!  Trying alternate methods." )
 if Oo000 == 'osx' :
  Ii1I1Ii ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Oo000 == 'linux' :
  Ii1I1Ii ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Oo000 == 'android' :
  Ii1I1Ii ( "############ try android force close #################" )
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
 elif Oo000 == 'windows' :
  Ii1I1Ii ( "############ try windows force close #################" )
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
  Ii1I1Ii ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  Ii1I1Ii ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 48 - 48: Ii % oO0oo0o
  if 29 - 29: Ii1IIIi1 + Ii % I11O0O0oOO00O00o
  if 93 - 93: OOooOOo % iI11I1II1I1I
def ii1iI111 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( url ) :
  for file in iiiiI11ii :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    I11I1IIiiII1 = open ( ( os . path . join ( Ooo0o0oo0 , file ) ) ) . read ( )
    oOO0 = I11I1IIiiII1 . replace ( I11 , 'special://home/' )
    o00O0 = open ( ( os . path . join ( Ooo0o0oo0 , file ) ) , mode = 'w' )
    o00O0 . write ( str ( oOO0 ) )
    o00O0 . close ( )
 iiiii1ii1 ( )
 if 15 - 15: I1ii11iIi11i + I11O0O0oOO00O00o . O0OOOoOoo0 - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
def ii1iI1iI1 ( ) :
 iI1I ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 iI1I ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 iI1I ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 86 - 86: oOo0O0Ooo / oO0oo0o * iI1ii11iIi1i
def O00o ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def oO0o00ooO0OoO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def IIoO00OoOo ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in OooOoooOo :
  iI1I ( ( '[COLOR' + iiI1IiI + ']Filter - ' + IIIii1I + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']Stream - ' + IIIii1I + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOOO00o000o )
def OoOi111i ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  oO00oo0o00o0o ( url )
def II1III1i1iiI ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1
 I11i11i1 = 'https://www.radionomy.com/en/search/index?query=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( I11i11i1 )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']Stream - ' + IIIii1I + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + i1I1ii11i1Iii , 70005 , oOOO00o000o )
  if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / I11O0O0oOO00O00o . O0OOOoOoo0 / ooOoO0O00
  if 12 - 12: Ii1I * ooOoO0O00 * I11O0O0oOO00O00o
def IIIi11IiIiii ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , 'http://www.listenlive.eu/' + i1I1ii11i1Iii , 10111113 , III1iII1I1ii + 'radio.png' )
def OoOO0OOoo ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  OooOoOo ( IIIii1I , url , 222 , III1iII1I1ii + 'radio.png' )
  if 23 - 23: O00o0O00 / o0o00Oo0O / oOo0O0Ooo
def I11o0000o0Oo ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.toonjet.com/' + i1I1ii11i1Iii , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0O0OOo0OoO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( IiIiII1 )
 for url , oOOO00o000o in IIi1I11I1II :
  if 'ol.gif' in oOOO00o000o :
   pass
  elif 'link_block_' in oOOO00o000o :
   pass
  elif '.png' in oOOO00o000o :
   pass
  else :
   iI1I ( ( oOOO00o000o ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in OooOoooOo :
  iI1I ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1i1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 65 - 65: oO0oo0o + Ii1I / O00o0O00
  if 85 - 85: iI11I1II1I1I / ii % IIiIiII11i
def i11I1 ( ) :
 IiIIi11i111 ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 IiIIi11i111 ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 67 - 67: ooOoO0O00
def iii ( ) :
 IiIIi11i111 ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IiIIi11i111 ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 IiIIi11i111 ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 57 - 57: oOo0O0Ooo
def iii1IIiI ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , i1I1ii11i1Iii , i1i1Ii11Ii in IIi1I11I1II :
  if 'Parent' in IIIii1I :
   pass
  elif '2' in i1i1Ii11Ii :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: O00o0O00 + ii1ii11IIIiiI % Ii1I . oO0o / oO0o * o0o00Oo0O
def Ii1iiII1i ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , i1I1ii11i1Iii , i1i1Ii11Ii in IIi1I11I1II :
  if IiIi1iIIi1 in IIIii1I . lower ( ) :
   if '1' in i1i1Ii11Ii :
    IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in i1i1Ii11Ii :
    IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in i1i1Ii11Ii :
    IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 52 - 52: oO0oo0o / ii1ii11IIIiiI
    if 91 - 91: ooOOOoO . I1ii11iIi11i + IIiIiII11i
def Ii1I11i11I1i ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , i1I1ii11i1Iii , i1i1Ii11Ii in IIi1I11I1II :
  if '1' in i1i1Ii11Ii :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in i1i1Ii11Ii :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in i1i1Ii11Ii :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 59 - 59: ooOoO0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: o0o00Oo0O * iI1ii11iIi1i * oO0o . oO0o * I11O0O0oOO00O00o - iI1ii11iIi1i
def iIi11i ( url ) :
 ii1II = url
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in OooOoooOo :
  if 'mp3' in IIIii1I :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii1II + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in IIIii1I :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii1II + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in IIIii1I :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ii1II + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in IIIii1I :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii1II + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 56 - 56: Ii . O0OOOoOoo0 / Ii1IIIi1
   if 48 - 48: oO0o * O00o0O00 + iI11I1II1I1I / IIiIiII11i
   if 100 - 100: I11O0O0oOO00O00o
def OOO0oOO0ooo0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii1II = url
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  if 'Parent' in IIIii1I :
   pass
  elif '.db' in IIIii1I :
   pass
  elif '.jpg' in IIIii1I :
   pass
  elif '.html' in IIIii1I :
   pass
  elif '.doc' in IIIii1I :
   pass
  elif 'mp3' in IIIii1I :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii1II + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in IIIii1I :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii1II + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ii1II + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 14 - 14: IIiIiII11i
   if 42 - 42: IIiIiII11i + ii1ii11IIIiiI - iI1ii11iIi1i - o0o00Oo0O / I11i % ooOOOoO
def O00oOoOOO0ooo ( ) :
 IiIIi11i111 ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IiIIi11i111 ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IiIIi11i111 ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 19 - 19: Ii1IIIi1 - I11i - iI1ii11iIi1i - OOooOOo . Ii1IIIi1 . ii1ii11IIIiiI
def i11I1I ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o in IIi1I11I1II :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOOO00o000o :
   pass
  else :
   IiIIi11i111 ( oOOO00o000o , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i1I1ii11i1Iii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOOO00o000o + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 71 - 71: Ii1IIIi1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . O00o0O00 . o0o00Oo0O % iI1ii11iIi1i % Ii
 if 11 - 11: o0o00Oo0O - IIiIiII11i . O00o0O00 . iI1ii11iIi1i % ii1ii11IIIiiI
def IIi1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  if '</a>' in IIIii1I :
   pass
  elif '(' in IIIii1I :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 95 - 95: ii + I11O0O0oOO00O00o - Ii1I / Ii1I . ooOoO0O00 . ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: O0OOOoOoo0 - ooOoO0O00 . I11O0O0oOO00O00o - Ii1I + O0OOOoOoo0 + ii
def iii1i11 ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if IiIi1iIIi1 in IIIii1I . lower ( ) :
   if '</a>' in IIIii1I :
    pass
   elif '(' in IIIii1I :
    IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 56 - 56: oOo0O0Ooo
    if 12 - 12: oOo0O0Ooo - O0OOOoOoo0
def I1ii1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if '</a>' in IIIii1I :
   pass
  elif '(' in IIIii1I :
   IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 48 - 48: O0OOOoOoo0 / iI11I1II1I1I + O00o0O00 + iI11I1II1I1I . oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: ii1ii11IIIiiI
 if 98 - 98: O0OOOoOoo0
def Ii11i1Ii1IIII ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  ii1II = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ii1II )
  if 41 - 41: iI1ii11iIi1i / IIiIiII11i . OOooOOo
def oooO0oOoo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , url in IIi1I11I1II :
  if '<p align' in IIIii1I :
   pass
  elif '&nbsp;' in IIIii1I :
   pass
  else :
   o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 76 - 76: ooOoO0O00 % OOooOOo - oOo0O0Ooo / I11i * O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: I1ii11iIi11i * I1ii11iIi11i / OOooOOo
 if 4 - 4: oOo0O0Ooo * OOooOOo % I11O0O0oOO00O00o . OOooOOo
def o0o0OO0O00o ( ) :
 IIIi1I1IIii1II = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi1I11I1II = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'ongoing' in i1I1ii11i1Iii :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in i1I1ii11i1Iii :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in i1I1ii11i1Iii :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in i1I1ii11i1Iii :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in i1I1ii11i1Iii :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def I1II1III1 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 oooo0O0o0OoOO = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOOO00o000o , oOOO00o000o , IIIii1I )
 for url , IIIii1I in oooo0O0o0OoOO :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  o0OIiII ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def III1 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 iiiI1I = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 oO0OOO0o0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIIi1I1IIii1II )
 OOOOO0 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in oO0OOO0o0O :
  o0OIiII ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , IIIii1I in iiiI1I :
  ii1iII1II ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  o0OIiII ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def Ooo0Oo0o ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  ii1iII1II ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 85 - 85: oOo0O0Ooo
def Ii1Ii1I ( ) :
 iI1I ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 iI1I ( '[COLOR' + iiI1IiI + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 54 - 54: oO0oo0o + OOooOOo
def o0O00O ( ) :
 iI1I ( '[COLOR' + iiI1IiI + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 iI1I ( '[COLOR' + iiI1IiI + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 94 - 94: iI1ii11iIi1i - Ii1I + I11i - I1ii11iIi11i
def iiIi1iiI1I ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  if '?c=' in url :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
def IiiIi11Ii1iI1 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , i1II11Iii1I , IIIii1I in IIi1I11I1II :
  if 'Genre' in url :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 91 - 91: O00o0O00 + ii1ii11IIIiiI . I11O0O0oOO00O00o
def i1I111i1ii ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , i1II11Iii1I , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i1II11Iii1I )
  if 81 - 81: I1ii11iIi11i - I11O0O0oOO00O00o
def ii1iII1iI111 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , i1II11Iii1I , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , i1II11Iii1I )
  if 94 - 94: Ii1IIIi1 % O0OOOoOoo0 . oO0oo0o
  if 85 - 85: O00o0O00 * ooOoO0O00 % oOo0O0Ooo - O0OOOoOoo0
  if 37 - 37: ooOOOoO . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
  if 83 - 83: ooOOOoO / ii1ii11IIIiiI
  if 64 - 64: oO0o % ooOOOoO . ii1ii11IIIiiI % oO0o + I11O0O0oOO00O00o * ooOOOoO
def O0Oooo ( ) :
 if 83 - 83: I11i % oO0oo0o + I11O0O0oOO00O00o % Ii + o0o00Oo0O
 o0OIiII ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 if 65 - 65: iI11I1II1I1I % oO0oo0o + o0o00Oo0O / ii
def IIii11I1i1I ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 52 - 52: iI1ii11iIi1i % O00o0O00 * oOo0O0Ooo % I11O0O0oOO00O00o + O00o0O00 / Ii1IIIi1
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIIi1I1IIii1II )
 if 80 - 80: ii + ooOOOoO
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if IiIi1iIIi1 in IIIii1I . lower ( ) :
   if 'Dad!' in IIIii1I :
    pass
   elif 'Family Guy' in IIIii1I :
    pass
   elif '2 Stupid' in IIIii1I :
    pass
   elif 'The Zelfs' in IIIii1I :
    pass
   elif 'A Clone' in IIIii1I :
    pass
   elif 'A.T.O.M' in IIIii1I :
    pass
   elif 'Almost Naked' in IIIii1I :
    pass
   elif 'Angry Kid' in IIIii1I :
    pass
   elif 'Annoying Orange' in IIIii1I :
    pass
   elif 'Aqua Teen' in IIIii1I :
    pass
   elif 'Assy Mcgee' in IIIii1I :
    pass
   elif 'Astroblast' in IIIii1I :
    pass
   elif 'Atomic Betty' in IIIii1I :
    pass
   elif 'Axe Cop' in IIIii1I :
    pass
   elif 'Baby Playpen' in IIIii1I :
    pass
   elif 'Beavis and Butt' in IIIii1I :
    pass
   elif 'Celebrity Deathmatch' in IIIii1I :
    pass
   elif 'Clerks The' in IIIii1I :
    pass
   elif 'Crapston Villas' in IIIii1I :
    pass
   elif 'Duckman:' in IIIii1I :
    pass
   elif 'Stripperella' in IIIii1I :
    pass
   elif 'Vixen' in IIIii1I :
    pass
   else :
    o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
    if 95 - 95: ii1ii11IIIiiI / oO0oo0o * ii1ii11IIIiiI - ii * ii % oO0o
    if 43 - 43: I1ii11iIi11i . ii1ii11IIIiiI
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 12 - 12: ii1ii11IIIiiI + O00o0O00 + I11O0O0oOO00O00o . ooOOOoO / iI1ii11iIi1i
def iiIi1i ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if 'Dad!' in IIIii1I :
   pass
  elif 'Family Guy' in IIIii1I :
   pass
  elif '2 Stupid' in IIIii1I :
   pass
  elif 'The Zelfs' in IIIii1I :
   pass
  elif 'A Clone' in IIIii1I :
   pass
  elif 'A.T.O.M' in IIIii1I :
   pass
  elif 'Almost Naked' in IIIii1I :
   pass
  elif 'Angry Kid' in IIIii1I :
   pass
  elif 'Annoying Orange' in IIIii1I :
   pass
  elif 'Aqua Teen' in IIIii1I :
   pass
  elif 'Assy Mcgee' in IIIii1I :
   pass
  elif 'Astroblast' in IIIii1I :
   pass
  elif 'Atomic Betty' in IIIii1I :
   pass
  elif 'Axe Cop' in IIIii1I :
   pass
  elif 'Baby Playpen' in IIIii1I :
   pass
  elif 'Beavis and Butt' in IIIii1I :
   pass
  elif 'Celebrity Deathmatch' in IIIii1I :
   pass
  elif 'Clerks The' in IIIii1I :
   pass
  elif 'Crapston Villas' in IIIii1I :
   pass
  elif 'Duckman:' in IIIii1I :
   pass
  elif 'Stripperella' in IIIii1I :
   pass
  elif 'Vixen' in IIIii1I :
   pass
  else :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: ooOOOoO . O0OOOoOoo0 - IIiIiII11i
def ooooO0 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IiIiII1 )
 for oOOO00o000o in OooOoooOo :
  Iiii111 = oOOO00o000o
 Ooooo = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IiIiII1 )
 for url in Ooooo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 10007 , Iiii111 )
  if 91 - 91: O0OOOoOoo0 * I11O0O0oOO00O00o - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + O0OOOoOoo0
  if 56 - 56: I11i / ooOOOoO * oOo0O0Ooo . I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: Ii
def I11i1I1ii1i1 ( url , IMAGE ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  print IIIii1I + '     ' + url
  if 'easy' in url :
   oO0ooooo0O00 ( url )
   if 5 - 5: OOooOOo % Ii1IIIi1 + ooOOOoO
   if 13 - 13: ooOOOoO
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 19 - 19: IIiIiII11i - ooOOOoO
def oO0ooooo0O00 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  oO00oo0o00o0o ( url )
  if 59 - 59: I11i * oO0o - iI1ii11iIi1i . O00o0O00
  if 89 - 89: O00o0O00
  if 69 - 69: O0OOOoOoo0 - ii * o0o00Oo0O
def iiii111II ( ) :
 if 84 - 84: O0OOOoOoo0 + Ii - O00o0O00 * O0OOOoOoo0
 o0OIiII ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , OO0o , '' )
 if 33 - 33: O0OOOoOoo0 % ooOoO0O00 - oO0oo0o . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if 'elete' in IIIii1I :
   pass
  else :
   OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 222 , oOOO00o000o )
   if 17 - 17: iI1ii11iIi1i / iI11I1II1I1I - oO0o + oOo0O0Ooo % O00o0O00
def III1III11II ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iIi1iI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , OO0Oo , i1iII1IiiIiI1 in iIi1iI :
  for IiIi1iIIi1 in OO0Oo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIiiiiiIiIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for i1I1ii11i1Iii , IIIii1I in IIiiiiiIiIIi :
    if 'tube' in i1I1ii11i1Iii :
     pass
    elif 'stage' in i1I1ii11i1Iii :
     OooOoOo ( '[COLOR' + iiI1IiI + ']' + OO0Oo + '   -   ' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOOO00o000o , )
    elif 'vee' in i1I1ii11i1Iii :
     pass
     if 26 - 26: I11i
def IiIi ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iIi1iI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , OO0Oo , i1iII1IiiIiI1 in iIi1iI :
  IIiiiiiIiIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for i1I1ii11i1Iii , IIIii1I in IIiiiiiIiIIi :
   if 'tube' in i1I1ii11i1Iii :
    pass
   elif 'stage' in i1I1ii11i1Iii :
    OooOoOo ( '[COLOR' + iiI1IiI + ']' + OO0Oo + '   -   ' + IIIii1I + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOOO00o000o )
   elif 'vee' in i1I1ii11i1Iii :
    pass
    if 88 - 88: OOooOOo - O00o0O00
    if 63 - 63: ooOOOoO * ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: ooOOOoO - I11i . iI11I1II1I1I . OOooOOo / O00o0O00
def OOO0O00Oo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ooOOO0OooOo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIIi1I1IIii1II )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( ooOOO0OooOo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in ooOOO0OooOo :
  oO00oo0o00o0o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 13 - 13: iI11I1II1I1I
  if 2 - 2: ooOoO0O00 * oO0oo0o - oO0oo0o + ii % OOooOOo / OOooOOo
  if 3 - 3: ii
  if 71 - 71: ooOOOoO + ooOoO0O00 - Ii1IIIi1 - Ii . I11O0O0oOO00O00o - O0OOOoOoo0
  if 85 - 85: Ii1I - OOooOOo / Ii1I + O00o0O00 - Ii1IIIi1
  if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + ii1ii11IIIiiI
  if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * oO0oo0o
def IIi1IIIi ( ) :
 if 85 - 85: IIiIiII11i . O0OOOoOoo0 % O00o0O00 % I11O0O0oOO00O00o
 OOo00ooOoO0o ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 OOo00ooOoO0o ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 21 - 21: Ii
 I1I1i1I ( 'movies' , 'MAIN' )
 if 89 - 89: Ii1IIIi1 . Ii * o0o00Oo0O
def Iii ( ) :
 OOo00ooOoO0o ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 OOo00ooOoO0o ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 35 - 35: ooOOOoO . ii / O00o0O00
 I1I1i1I ( 'movies' , 'MAIN' )
def O0OO0ooO00 ( ) :
 if 83 - 83: iI11I1II1I1I
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 OooOO0oOOo0O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 42 - 42: Ii1IIIi1 / I11i + I1ii11iIi11i . I1ii11iIi11i % O00o0O00
 for Ii1III1 in OooOO0oOOo0O :
  ooIii1ii1II1iI1 = I11i1I1I + Ii1III1 + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( ooIii1ii1II1iI1 )
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , O000OOO , IIIii1I in IIi1I11I1II :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    OO0OoOo ( IIIii1I , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii , O000OOO , Ii1II )
    if 53 - 53: oO0o % I11i / O00o0O00 % ooOOOoO % oO0o % ii
    I1I1i1I ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 31 - 31: oOo0O0Ooo
    if 73 - 73: O0OOOoOoo0 . o0o00Oo0O / I11i - ii % Ii
def O000 ( ) :
 if 12 - 12: I1ii11iIi11i
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 OooOO0oOOo0O = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 63 - 63: O00o0O00 . IIiIiII11i . I11O0O0oOO00O00o
 for Ii1III1 in OooOO0oOOo0O :
  I1I1IIIIi11 = I11i1I1I + Ii1III1 + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( I1I1IIIIi11 )
  IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for IIIii1I , Ii1II , i1I1ii11i1Iii , oOOO00o000o , O000OOO , OooO0Oo0 in IIi1I11I1II :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    OOo00ooOoO0o ( IIIii1I , i1I1ii11i1Iii , OooO0Oo0 , oOOO00o000o , O000OOO , Ii1II )
    if 83 - 83: o0o00Oo0O
    I1I1i1I ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 89 - 89: I1ii11iIi11i + Ii1I - I11i
    if 40 - 40: oO0o + oO0o
def o0oo0o00ooO00 ( ) :
 if 37 - 37: oO0o - Ii1I . ii . O0OOOoOoo0 + OOooOOo / iI1ii11iIi1i
 IiIiII1 = O0i1II1Iiii1I11 ( I11i1I1I + 'spongemain.php' )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , Ii1II , i1I1ii11i1Iii , oOOO00o000o , O000OOO , OooO0Oo0 in IIi1I11I1II :
  OOo00ooOoO0o ( IIIii1I , i1I1ii11i1Iii , OooO0Oo0 , oOOO00o000o , O000OOO , Ii1II )
  I1I1i1I ( 'movies' , 'MAIN' )
def I1oOoO0OOO00O ( url ) :
 if 73 - 73: I11i % oO0o + ooOOOoO + oOo0O0Ooo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OoOO00 = ( '%s%s' % ( O0O00OoOoOOo , url ) )
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in IIi1I11I1II :
  II1IIi1iII1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
  for iiiiIiIi in II1IIi1iII1i :
   if iiiiIiIi == url :
    IIIii1I = ( '[COLORred]Watched - [/COLOR]' + IIIii1I ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  OO0OoOo ( IIIii1I , url , 222 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
  if 3 - 3: I1ii11iIi11i
  I1I1i1I ( 'movies' , 'MAIN' )
  if 33 - 33: I1ii11iIi11i / iI11I1II1I1I % ooOoO0O00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: iI1ii11iIi1i + iI11I1II1I1I + OOooOOo . oO0o
  if 49 - 49: ooOOOoO / O0OOOoOoo0 / O00o0O00
def IiIiIi1I11I ( url ) :
 if 43 - 43: Ii + Ii1IIIi1 + O0OOOoOoo0 / ii1ii11IIIiiI . Ii1I + Ii1IIIi1
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , Ii1II , url , oOOO00o000o , O000OOO , OooO0Oo0 in IIi1I11I1II :
  OOo00ooOoO0o ( IIIii1I , url , OooO0Oo0 , oOOO00o000o , O000OOO , Ii1II )
  if 39 - 39: Ii1I - Ii - I11O0O0oOO00O00o
  I1I1i1I ( 'movies' , 'MAIN' )
  if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
  if 56 - 56: oO0oo0o + O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: IIiIiII11i + OOooOOo % O0OOOoOoo0 / OOooOOo + Ii1I
def OO0OoOo ( name , url , mode , iconimage , fanart , description ) :
 if 2 - 2: Ii - ii1ii11IIIiiI + oO0o % I11O0O0oOO00O00o * iI1ii11iIi1i
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iII . setProperty ( "Fanart_Image" , fanart )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = False )
 return i1iI1Iiii1I
 if 29 - 29: ooOoO0O00 % Ii1IIIi1 / ooOOOoO + OOooOOo - O00o0O00 - Ii1I
def OOo00ooOoO0o ( name , url , mode , iconimage , fanart , description ) :
 if 69 - 69: iI11I1II1I1I . IIiIiII11i . ooOoO0O00 - I11i
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iII . setProperty ( "Fanart_Image" , fanart )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = True )
 return i1iI1Iiii1I
if 79 - 79: O0OOOoOoo0 % O00o0O00
if 54 - 54: OOooOOo - ii1ii11IIIiiI
if 65 - 65: ii1ii11IIIiiI . O0OOOoOoo0 + O00o0O00 / I1ii11iIi11i + ooOOOoO % ooOoO0O00
if 28 - 28: Ii + o0o00Oo0O / Ii1I
if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
if 34 - 34: iI1ii11iIi1i * iI1ii11iIi1i - Ii1I - o0o00Oo0O . Ii
if 32 - 32: iI11I1II1I1I . oO0o * oO0oo0o / O00o0O00 . IIiIiII11i - I1ii11iIi11i
if 10 - 10: Ii1I / Ii - iI1ii11iIi1i + oO0oo0o * oOo0O0Ooo
if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
if 64 - 64: I11O0O0oOO00O00o + oO0o
if 25 - 25: oOo0O0Ooo . O0OOOoOoo0 + oOo0O0Ooo % iI1ii11iIi1i * iI11I1II1I1I
if 31 - 31: Ii + O00o0O00 - o0o00Oo0O
if 51 - 51: oO0o * ooOoO0O00 / iI1ii11iIi1i * O00o0O00 + O0OOOoOoo0 % Ii1I
if 34 - 34: oO0oo0o * ii + iI1ii11iIi1i + Ii
def iiIi ( string ) :
 if Ii1iIiII1ii1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 74 - 74: I11O0O0oOO00O00o / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
def Oo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1IIii11i1I1 = [ ]
 try :
  if 12 - 12: ooOoO0O00 / O00o0O00 % O0OOOoOoo0 * ooOOOoO * o0o00Oo0O * iI11I1II1I1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  iiIi ( 'Making Favorites File' )
  i1IIii11i1I1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  I11I1IIiiII1 = open ( I1IIiiIiii , "w" )
  I11I1IIiiII1 . write ( json . dumps ( i1IIii11i1I1 ) )
  I11I1IIiiII1 . close ( )
 else :
  iiIi ( 'Appending Favorites' )
  I11I1IIiiII1 = open ( I1IIiiIiii ) . read ( )
  OOOOoO = json . loads ( I11I1IIiiII1 )
  OOOOoO . append ( ( name , url , iconimage , fanart , mode ) )
  oOO0 = open ( I1IIiiIiii , "w" )
  oOO0 . write ( json . dumps ( OOOOoO ) )
  oOO0 . close ( )
  if 19 - 19: oOo0O0Ooo % iI1ii11iIi1i . ooOOOoO * O0OOOoOoo0
  if 89 - 89: OOooOOo . O00o0O00
def IIIIIiI11Ii ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  i1IIii11i1I1 = [ ]
  iiIi ( 'Making Favorites File' )
  i1IIii11i1I1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  I11I1IIiiII1 = open ( I1IIiiIiii , "w" )
  I11I1IIiiII1 . write ( json . dumps ( i1IIii11i1I1 ) )
  I11I1IIiiII1 . close ( )
 else :
  Iiii1Ii1I = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  oooOOOOOi1iIii = len ( Iiii1Ii1I )
  for o0O0ooooooo00 in Iiii1Ii1I :
   IIIii1I = o0O0ooooooo00 [ 0 ]
   i1I1ii11i1Iii = o0O0ooooooo00 [ 1 ]
   IiiiiI1i1Iii = o0O0ooooooo00 [ 2 ]
   try :
    I1111ii11IIII = o0O0ooooooo00 [ 3 ]
    if I1111ii11IIII == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     I1111ii11IIII = IiiiiI1i1Iii
    else :
     I1111ii11IIII = O000OOO
   try : IiIi1II111I = o0O0ooooooo00 [ 5 ]
   except : IiIi1II111I = None
   try : o00oIIi1i1 = o0O0ooooooo00 [ 6 ]
   except : o00oIIi1i1 = None
   if 84 - 84: O00o0O00 + iI1ii11iIi1i + I11i
   if o0O0ooooooo00 [ 4 ] == 0 :
    o0OIiII ( IIIii1I , i1I1ii11i1Iii , '' , IiiiiI1i1Iii , O000OOO , '' , 'fav' )
   else :
    o0OIiII ( IIIii1I , i1I1ii11i1Iii , o0O0ooooooo00 [ 4 ] , IiiiiI1i1Iii , O000OOO , '' , 'fav' )
    if 33 - 33: iI1ii11iIi1i
def ooOOO00oOOooO ( name ) :
 OOOOoO = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for IiIIii1iiI in range ( len ( OOOOoO ) ) :
  if OOOOoO [ IiIIii1iiI ] [ 0 ] == name :
   del OOOOoO [ IiIIii1iiI ]
   oOO0 = open ( I1IIiiIiii , "w" )
   oOO0 . write ( json . dumps ( OOOOoO ) )
   oOO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 7 - 7: I11i
 if 18 - 18: ii + I11i . o0o00Oo0O + ooOOOoO * ooOoO0O00 . oO0o
def OoOOo000o0 ( ) :
 o0OO0oooo = os . path . join ( O0O , 'addons.ini' )
 I11II1i1 = open ( o0OO0oooo , "w+" )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIIi1I1IIii1II )
 I11II1i1 . write ( r'[' + IiII + ']' + '\n' )
 for IIIii1I , oOOO00o000o , iIII1i1i , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  IiI1ii11I1 = ( IIIii1I + '=plugin://' + IiII + '/?url=' + i1I1ii11i1Iii + '&mode=10012&name=' + ( IIIii1I ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOOO00o000o ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOOO00o000o ) . replace ( ' ' , '' ) + '+&amp;description=' )
  I11II1i1 . write ( IiI1ii11I1 + '\n' )
  if 19 - 19: ii1ii11IIIiiI + ooOOOoO / oO0oo0o / IIiIiII11i
  if 92 - 92: ooOoO0O00 % O0OOOoOoo0 + O0OOOoOoo0 - iI11I1II1I1I . iI1ii11iIi1i
def iIIi1 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  ii1iII1II ( IIIii1I , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + '247.png' , III1iII1I1ii + '247.png' , '' )
def o00oOOO ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  ii1iII1II ( IIIii1I , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def i1II1 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  ii1iII1II ( IIIii1I , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def o0Ooo0o0Oo ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  ii1iII1II ( IIIii1I , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def oo00ooooOOo00 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi1I11I1II = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  ii1iII1II ( IIIii1I , i1I1ii11i1Iii , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 16 - 16: Ii / ooOoO0O00 % O00o0O00
  if 84 - 84: I11O0O0oOO00O00o - I1ii11iIi11i * o0o00Oo0O / iI1ii11iIi1i . iI1ii11iIi1i
def ooO0 ( ) :
 if 34 - 34: ooOoO0O00 % ooOOOoO
 o0OIiII ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 80 - 80: ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
def oOoOii1IIii ( ) :
 if 31 - 31: iI11I1II1I1I * O0OOOoOoo0 - ii * O0OOOoOoo0
 IiIiII1 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I , i1iI11i1IIi in IIi1I11I1II :
  o0OIiII ( IIIii1I + '  -  ' + ( i1iI11i1IIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 10023 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 60 - 60: O00o0O00 % O00o0O00 * oO0oo0o / oOo0O0Ooo * OOooOOo * oOo0O0Ooo
  if 61 - 61: oO0oo0o + Ii1I / ooOoO0O00 * oO0oo0o
  if 90 - 90: iI1ii11iIi1i % oO0oo0o
def iiii1OooO0O0Ooo ( ) :
 if 85 - 85: I11i / ii1ii11IIIiiI
 o0OIiII ( '[COLOR' + iiI1IiI + ']Action[/COLOR]' , 'Aksiyon' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Adventure[/COLOR]' , 'Macera' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Animation[/COLOR]' , 'Animasyon' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Anime[/COLOR]' , 'Anime' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Biography[/COLOR]' , 'Biyografi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Comedy[/COLOR]' , 'Komedi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Drama[/COLOR]' , 'Dram' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Family[/COLOR]' , 'Aile' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']History[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Horror[/COLOR]' , 'Korku' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Mystery[/COLOR]' , 'Gizem' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Romance[/COLOR]' , 'Romantik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Sport[/COLOR]' , 'Spor' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Western[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 67 - 67: I11O0O0oOO00O00o % oO0oo0o
def ii1iiIi ( url ) :
 ooOooo0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIIi1I1IIii1II = cloudflare . source ( ooOooo0 )
 IIi1I11I1II = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 21 - 21: Ii1I
  if 84 - 84: o0o00Oo0O / oOo0O0Ooo % ooOoO0O00 % ooOoO0O00 / oO0o / oO0oo0o
  if 28 - 28: O0OOOoOoo0 . ii + I11i + iI1ii11iIi1i % Ii1IIIi1
  if 80 - 80: I1ii11iIi11i
def OOo0oOOOOooOo ( ) :
 if 19 - 19: I11i
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = cloudflare . source ( i1I1ii11i1Iii )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if IiIi1iIIi1 in IIIii1I . lower ( ) :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 10022 , III1iII1I1ii + 'dtv.png' )
   if 73 - 73: ii1ii11IIIiiI * I1ii11iIi11i * OOooOOo
   if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
   if 26 - 26: I11i % O00o0O00 + O00o0O00 % I11O0O0oOO00O00o * Ii / Ii1IIIi1
def OOoO0oO00o ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii1II , OOO0OoO0oo0OO , i1iI1Ii11Ii1 , IIIii1I in IIi1I11I1II :
  o0OoO0oo0O0o = ( i1iI1Ii11Ii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii1III1iiIi = ( OOO0OoO0oo0OO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1ii1iI = 'Season ' + ii1III1iiIi + 'Episode ' + o0OoO0oo0O0o + IIIii1I
  ooO000OO ( I1ii1iI , ii1II )
  if 43 - 43: O0OOOoOoo0 * ii1ii11IIIiiI % O00o0O00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 38 - 38: I1ii11iIi11i
  if 34 - 34: OOooOOo
def ooO000OO ( name , url ) :
 ii1II = url
 OoO0o00OOOOO = name
 O0 = cloudflare . source ( ii1II )
 OooOoooOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for ooOOO0OooOo , I1iIi1iIIIIiI in OooOoooOo :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + OoO0o00OOOOO + I1iIi1iIIIIiI + '[/COLOR]' , ooOOO0OooOo , 10012 , III1iII1I1ii + 'dtv.png' )
  if 94 - 94: ooOOOoO * I11O0O0oOO00O00o * ii / I11i . ooOOOoO - I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: O00o0O00 / ooOOOoO - oO0o / O00o0O00 . ooOoO0O00
 if 22 - 22: o0o00Oo0O - I11O0O0oOO00O00o + ii1ii11IIIiiI . iI1ii11iIi1i * ooOoO0O00
def Ooo0O0oooo ( ) :
 if 26 - 26: iI11I1II1I1I * I11i . I11O0O0oOO00O00o
 if 10 - 10: ii1ii11IIIiiI * oO0oo0o % I1ii11iIi11i - I11O0O0oOO00O00o % I1ii11iIi11i
 if 65 - 65: Ii1IIIi1 * iI11I1II1I1I / o0o00Oo0O . I11O0O0oOO00O00o
 if 94 - 94: I1ii11iIi11i . O0OOOoOoo0 * Ii - I11i . Ii1IIIi1
 if 98 - 98: O00o0O00 + iI1ii11iIi1i
 if 52 - 52: I1ii11iIi11i / OOooOOo - ii1ii11IIIiiI . Ii1IIIi1
 if 50 - 50: iI11I1II1I1I - Ii1IIIi1 - I11O0O0oOO00O00o
 if 60 - 60: iI11I1II1I1I * O0OOOoOoo0
 if 71 - 71: OOooOOo % I1ii11iIi11i % O0OOOoOoo0
 if 34 - 34: I11O0O0oOO00O00o / I11O0O0oOO00O00o % ooOOOoO . OOooOOo / I1ii11iIi11i
 if 99 - 99: O0OOOoOoo0 * oOo0O0Ooo - O0OOOoOoo0 % iI1ii11iIi1i
 if 40 - 40: O00o0O00 / ooOOOoO / iI11I1II1I1I + iI1ii11iIi1i
 if 59 - 59: I11O0O0oOO00O00o * ii + O00o0O00 . iI11I1II1I1I / ooOoO0O00
 o0OIiII ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 75 - 75: I11O0O0oOO00O00o . O00o0O00 - iI11I1II1I1I * oO0o * Ii1IIIi1
 if 93 - 93: O0OOOoOoo0
def iII1IIiiI11II ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii1IIi111 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii1IIi111 ) )
 for url , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 70 - 70: iI1ii11iIi1i - O00o0O00 * O00o0O00 / iI11I1II1I1I + o0o00Oo0O
def IiIIi11i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 49 - 49: Ii1I + o0o00Oo0O . iI1ii11iIi1i * ii
def oO0OOO00 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  if 'episode' in url :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 13 - 13: ooOOOoO * Ii1I / Ii1I / iI11I1II1I1I % iI11I1II1I1I
  if 21 - 21: Ii1I
def oOOOO0oo0O0OO ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OOoo0o = 'http://www.watchseries.ac/search/' + IiIi1iIIi1 . replace ( ' ' , '%20' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( O0OOoo0o )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'watch online' in IIIii1I :
   pass
  else :
   print i1I1ii11i1Iii
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , oOOO00o000o , '' , '' )
   if 19 - 19: O0OOOoOoo0 % oO0oo0o
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 22 - 22: oO0oo0o . IIiIiII11i . I1ii11iIi11i
def ooIi111iII ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , url , IIIii1I , i1iI1Ii11Ii1 , Ii1II in IIi1I11I1II :
  Oo0OoOo = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1iI1Ii11Ii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OoOo + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOO00o000o , '' , Ii1II )
  if 13 - 13: I11i
def IIi1ii ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  Oo0OoOo = ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OoOo + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 38 - 38: iI11I1II1I1I + ii * oOo0O0Ooo % OOooOOo % I11O0O0oOO00O00o - ooOOOoO
def Oo0OO00OO0Oo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOO00o000o , '' , '' )
 for url in OooOoooOo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 1 - 1: iI11I1II1I1I . I11O0O0oOO00O00o + I11O0O0oOO00O00o . O0OOOoOoo0
def o0o00OoO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 ii1IIi111 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for OOO0OoO0oo0OO , iIi1iI in ii1IIi111 :
  IIi1I11I1II = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iIi1iI ) )
  for url , IIIii1I in IIi1I11I1II :
   Oo0OoOo = ( OOO0OoO0oo0OO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OoOo + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , url in IIi1I11I1II :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 89 - 89: ooOOOoO / oO0o * o0o00Oo0O / I11O0O0oOO00O00o . ii1ii11IIIiiI
class iII11II1II ( ) :
 if 100 - 100: oO0o % ii1ii11IIIiiI - I11O0O0oOO00O00o % I11O0O0oOO00O00o % I11O0O0oOO00O00o / O0OOOoOoo0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 83 - 83: oO0oo0o - O0OOOoOoo0 - ooOOOoO % ooOoO0O00 - Ii1IIIi1 . I11i
  Oo0OoOo = name
  self . Get_Sources ( i1I1ii11i1Iii , Oo0OoOo )
  if 96 - 96: I1ii11iIi11i + ii1ii11IIIiiI . ooOoO0O00
  if 54 - 54: IIiIiII11i . ooOoO0O00 / Ii1I % oOo0O0Ooo / ii1ii11IIIiiI
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( URL )
  IIi1I11I1II = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
   URL = 'http://www.watchseries.ac/link/' + i1I1ii11i1Iii
   self . Get_site_link ( URL , season_name )
   if 65 - 65: OOooOOo . OOooOOo - oO0oo0o + I1ii11iIi11i / Ii
 def Get_site_link ( self , url , season_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  OooOoooOo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  Ooooo = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for url in IIi1I11I1II :
   self . main ( url , season_name )
  for url in OooOoooOo :
   self . main ( url , season_name )
  for url in Ooooo :
   self . main ( url , season_name )
   if 90 - 90: iI11I1II1I1I + OOooOOo
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IiIIIiI = 'DACLIPS'
   if IiIIIiI in iII11II1II . source_list :
    pass
   else :
    self . daclips ( url , season_name , IiIIIiI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    IiIIIiI = 'FILEHOOT'
    if IiIIIiI in iII11II1II . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , IiIIIiI )
   else :
    if 'thevideo.me' in url :
     IiIIIiI = 'THEVIDEO'
     if IiIIIiI in iII11II1II . source_list :
      pass
     else :
      self . thevideo ( url , season_name , IiIIIiI )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      IiIIIiI = 'ALLMYVIDEOS'
      if IiIIIiI in iII11II1II . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , IiIIIiI )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       IiIIIiI = 'VIDSPOT'
       if IiIIIiI in iII11II1II . source_list :
        pass
       else :
        self . vidspot ( url , season_name , IiIIIiI )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        IiIIIiI = 'VODLOCKER'
        if IiIIIiI in iII11II1II . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , IiIIIiI )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 19 - 19: oO0o . ii * oO0o + ooOOOoO + ii
         if 19 - 19: I1ii11iIi11i
 def allmyvid ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 , IIIii1I in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . iI1ii11iIi1i - O00o0O00 / oOo0O0Ooo
 def vidspot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 , IIIii1I in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 98 - 98: IIiIiII11i + iI1ii11iIi1i + ii / ooOoO0O00 - iI1ii11iIi1i
 def thevideo ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 87 - 87: Ii1IIIi1 / I11O0O0oOO00O00o / I11O0O0oOO00O00o % ii - Ii1I * oO0oo0o
 def vodlocker ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 23 - 23: Ii
 def daclips ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 100 - 100: oO0oo0o + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
 def filehoot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OoOoO00o00 in IIi1I11I1II :
   self . Printer ( OoOoO00o00 , season_name , source_name )
   if 65 - 65: IIiIiII11i / I1ii11iIi11i
 def Printer ( self , Link , season_name , source_name ) :
  if 42 - 42: Ii . o0o00Oo0O
  if Link in iII11II1II . List :
   pass
  elif source_name in iII11II1II . source_list :
   pass
  else :
   OooOoOo ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   iII11II1II . List . append ( Link )
   iII11II1II . source_list . append ( source_name )
   if 75 - 75: ii1ii11IIIiiI + iI11I1II1I1I
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 19 - 19: oOo0O0Ooo + Ii . ooOOOoO - I11O0O0oOO00O00o / iI1ii11iIi1i + I11i
   if 38 - 38: I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I % Ii1I
   if 92 - 92: I11O0O0oOO00O00o / o0o00Oo0O * oOo0O0Ooo - I11O0O0oOO00O00o
   if 99 - 99: Ii % ii
   if 56 - 56: ooOOOoO * ii1ii11IIIiiI
def OOIi1iI111II1I1 ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , OO0o , '' )
 if 98 - 98: I11O0O0oOO00O00o + o0o00Oo0O * ii1ii11IIIiiI + Ii - O00o0O00 - iI11I1II1I1I
def I11I111i1I1 ( url ) :
 o0OIiII ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( IiIiII1 )
 for iii1O0Ooo0O , url , iii1oOo0OoOOOo0 , OOoo00 , I1I1 , o00o , O0OOO0ooO00o , o00O0 , I11I1IIiiII1 , I1iii1 , iIiiiIIiii in IIi1I11I1II :
  iii1oOo0OoOOOo0 = iii1oOo0OoOOOo0
  if 'Arsenal' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'arsenal-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                                  ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Bournemouth' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'afc-bournemouth.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                       ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Burnley' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'KEGnQWW.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                                   ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Chelsea' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'chelsea.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                                  ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Crystal' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'CrystalPalace.0.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                       ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Everton' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'Everton.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                                   ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Hull' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'hull-city-afc.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                                 ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Leicester' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                       ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Liverpool' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'liverpool-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                               ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Manchester City' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'city-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '               ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Manchester United' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + '91.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '          ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Middlesbrough' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                 ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Southampton' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'southampton-fc-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                   ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Stoke City' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'stoke-city.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                          ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Sunderland' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'sunderland-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                        ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Swansea' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'swansea-city-afc.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                    ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Tottenham' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '        ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Watford' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'watford-fc-hd-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '                              ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'Bromwich' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '   ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  elif 'West Ham' in iii1oOo0OoOOOo0 :
   iI1IIIii = III1iII1I1ii + 'west-ham.png'
   IIIii1I = '[COLOR' + iiI1IiI + ']' + iii1O0Ooo0O + ' - ' + iii1oOo0OoOOOo0 + '             ' + OOoo00 + '        ' + I1I1 + '        ' + o00o + '        ' + O0OOO0ooO00o + '        ' + o00O0 + '        ' + I11I1IIiiII1 + '        ' + I1iii1 + '[/COLOR]'
  o0OIiII ( str ( IIIii1I ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , iI1IIIii , iI1IIIii , iii1oOo0OoOOOo0 )
  if 91 - 91: I11i . Ii1IIIi1 % I1ii11iIi11i - Ii1IIIi1 . oO0oo0o % Ii
def iIi ( description ) :
 iii1oOo0OoOOOo0 = description
 i1I1ii11i1Iii = ( 'http://www.fullmatchesandshows.com/?s=' + iii1oOo0OoOOOo0 ) . replace ( ' ' , '%20' )
 O0OoOOoooo ( i1I1ii11i1Iii )
 if 70 - 70: Ii1IIIi1 . IIiIiII11i . Ii1IIIi1 - iI11I1II1I1I
def ooOo0O0 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi1I11I1II = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1I1ii11i1Iii , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOOO00o000o , OO0o , '' )
  if 83 - 83: ii
def iIIi111IiII1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii1IIi111 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii1IIi111 in ii1IIi111 :
  oOo0O000oo0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii1IIi111 ) )
  for II11I in oOo0O000oo0 :
   II11I = II11I
  Iii1iIiI1I1I1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii1IIi111 ) )
  for oOOO0OO , oOOO00o000o , time , I11ii1iI11 in Iii1iIiI1I1I1 :
   ii1iiIi1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I11ii1iI11 )
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + II11I + ' - ' + oOOO0OO + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOOO00o000o , OO0o , ( str ( ii1iiIi1 ) ) )
   if 6 - 6: ooOOOoO * IIiIiII11i % iI11I1II1I1I
 I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if 86 - 86: ooOoO0O00 * o0o00Oo0O % O0OOOoOoo0 . I1ii11iIi11i % O0OOOoOoo0 . I1ii11iIi11i
def O0oooO0o ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 if 19 - 19: O00o0O00 % oO0o / iI1ii11iIi1i + IIiIiII11i % ii
def oOo000O00O0 ( url ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , url , IIIii1I in IIi1I11I1II :
  iI1iiIii1I11I = IIIii1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IIIii1I :
   pass
  else :
   iI1iiIii1I11I = IIIii1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OooOoOo ( '[COLOR' + iiI1IiI + ']' + iI1iiIii1I11I + '[/COLOR]' , url , 10013 , oOOO00o000o )
 for url , oOOO00o000o , IIIii1I in OooOoooOo :
  iI1iiIii1I11I = IIIii1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IIIii1I :
   pass
  else :
   OooOoOo ( '[COLOR' + iiI1IiI + ']' + iI1iiIii1I11I + '[/COLOR]' , url , 10013 , oOOO00o000o )
def O0OoOOoooo ( url ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 if 32 - 32: ii % oO0oo0o % iI11I1II1I1I / o0o00Oo0O
 if 61 - 61: IIiIiII11i . o0o00Oo0O - iI1ii11iIi1i - Ii1I / Ii - IIiIiII11i
 if 98 - 98: iI1ii11iIi1i - oOo0O0Ooo . Ii * I1ii11iIi11i
 if 29 - 29: iI1ii11iIi1i / O0OOOoOoo0 % I11O0O0oOO00O00o
 if 10 - 10: iI11I1II1I1I % ii % Ii1I
 if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * I11O0O0oOO00O00o
 if 89 - 89: iI1ii11iIi1i - O0OOOoOoo0 . I11O0O0oOO00O00o - ii1ii11IIIiiI - oOo0O0Ooo
 for url , oOOO00o000o , IIIii1I in OooOoooOo :
  iI1iiIii1I11I = IIIii1I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IIIii1I :
   pass
  else :
   OooOoOo ( '[COLOR' + iiI1IiI + ']' + iI1iiIii1I11I + '[/COLOR]' , url , 10013 , oOOO00o000o )
   if 79 - 79: ooOOOoO + ooOOOoO + iI1ii11iIi1i
def iiiII1i1I ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIIi1I1IIii1II )
 for ooOOO0OooOo in IIi1I11I1II :
  OoooOoo0 = ( ooOOO0OooOo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  oO00oo0o00o0o ( 'http:' + OoooOoo0 )
  if 26 - 26: ooOOOoO / iI11I1II1I1I - iI11I1II1I1I
  if 57 - 57: ooOOOoO
  if 41 - 41: iI11I1II1I1I * Ii1IIIi1 + I1ii11iIi11i * I11i % ooOOOoO / O00o0O00
  if 63 - 63: ooOoO0O00 % Ii % IIiIiII11i * ii
def iIiII1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  OooOoOo ( IIIii1I , url , 8046 , oOOO00o000o )
 for url in OooOoooOo :
  iI1I ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def i111iii1I1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  oO00oo0o00o0o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 48 - 48: ii . OOooOOo
def oOIIIi11 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 69 - 69: o0o00Oo0O - o0o00Oo0O
def I11iIiI1I1i11 ( ) :
 iI1I ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 iI1I ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 iI1I ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1I1i1i1I1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( IiIiII1 )
 for oOOO00o000o , url , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOOO00o000o )
 for url in next :
  iI1I ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 17 - 17: OOooOOo + ii % O00o0O00
  if 36 - 36: Ii + Ii1I % O00o0O00 . oOo0O0Ooo - O0OOOoOoo0
def OooOo0o0OO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OooOoOo ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   OooOoOo ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def iiI1ii1IIiI ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  url = ( url ) . replace ( '\/' , '/' )
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 222 , '' )
  if 35 - 35: Ii1I * Ii1IIIi1 . ooOOOoO . ooOOOoO - oO0oo0o % OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1iiIiI ( name , url ) :
 o0OoO0000oOO = 0
 name = name
 url = url
 O0oO0 = [ '144' , '240' , '380' , '480' , '720' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  oO00oo0o00o0o ( url )
  if 42 - 42: ii1ii11IIIiiI % oO0o . Ii1I
  if 4 - 4: ooOoO0O00 + OOooOOo
  if 39 - 39: iI11I1II1I1I + O0OOOoOoo0
  if 92 - 92: I11O0O0oOO00O00o % Ii % I1ii11iIi11i
  if 23 - 23: IIiIiII11i * Ii1IIIi1
  if 80 - 80: ii1ii11IIIiiI / Ii + ii
  if 38 - 38: Ii1I % O0OOOoOoo0 + ooOoO0O00 * ii * oO0oo0o
  if 83 - 83: iI11I1II1I1I - O0OOOoOoo0 - ii1ii11IIIiiI / oO0o - o0o00Oo0O
def O00OoO0oo ( ) :
 IiIiII1 = Iii1iiIi1II ( 'http://documentarylovers.com/' )
 IIi1I11I1II = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  if 'genre' in i1I1ii11i1Iii :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , i1I1ii11i1Iii , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii11iI1iI ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( IiIiII1 )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOOO00o000o )
 for url in next :
  iI1I ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 64 - 64: ooOOOoO / I11i / ooOoO0O00
def OOo0OOOoOOo ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in OooOoooOo :
  iiI1ii1IIiI ( url )
  if 29 - 29: OOooOOo . Ii1IIIi1 + OOooOOo + o0o00Oo0O . o0o00Oo0O * O00o0O00
def i1iiiIIi11II ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0OoO0ooOO0o = 'http://documentarylovers.com/?s=' + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 OoOo0oOooOoOO = O0OoO0ooOO0o . lower ( )
 Ii11iI1iI ( OoOo0oOooOoOO )
 if 55 - 55: I11O0O0oOO00O00o
def ooooooo00oO0OO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if 'films' in url :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def IIIii11 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( IiIiII1 )
 for oOOO00o000o , url , IIIii1I in IIi1I11I1II :
  if 'films' in url :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOOO00o000o )
 for url in OooOoooOo :
  iI1I ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def i1i11I1I1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  if 'rtd' in url :
   OOOOOoooO ( url )
   if 59 - 59: oO0oo0o % O0OOOoOoo0
def OOOOOoooO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( IiIiII1 )
 for OOO00O , file in IIi1I11I1II :
  url = ( 'https://rtd.rt.com' + OOO00O + file )
  oO00oo0o00o0o ( url )
  if 36 - 36: ii
  if 33 - 33: o0o00Oo0O + I1ii11iIi11i - iI11I1II1I1I % Ii / oOo0O0Ooo
def IIIIIiiI11i1 ( ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( 'http://www.stream2watch.co/live-tv' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I , Iii1I in IIi1I11I1II :
  iI1I ( ( IIIii1I + '[COLOR' + iiI1IiI + ']' + Iii1I + '[/COLOR]' ) , i1I1ii11i1Iii , 8086 , oOOO00o000o )
  if 100 - 100: ii . I1ii11iIi11i / Ii1I
def I11i1I11iIii ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 8087 , oOOO00o000o )
  if 81 - 81: iI1ii11iIi1i / Ii1I + oO0oo0o / O00o0O00 + OOooOOo
def OOOii ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I in IIi1I11I1II :
  Iii1I11 ( url , IIIii1I )
  if 94 - 94: iI1ii11iIi1i / ii1ii11IIIiiI . oOo0O0Ooo . Ii1IIIi1 - ii / iI11I1II1I1I
def Iii1I11 ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  print url
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 47 - 47: ooOOOoO
def OOOoOOO0o0ooo ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i1I1ii11i1Iii , 3002 , 'http://www.solie.org/alibrary/' + oOOO00o000o )
def II1ii1iii1ii ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOOO00o000o )
def I11iIiI1 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 i1I1iiii1Ii11 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( IiIiII1 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , IIIii1I in i1I1iiii1Ii11 :
  iI1I ( '[COLOR' + iiI1IiI + ']Season- ' + IIIii1I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  iI1I ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , oOOO00o000o , IIIii1I in OooOoooOo :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOOO00o000o )
def IiIIIIi ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OoIIiIIIII1I ( url )
def OoIIiIIIII1I ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  oO00oo0o00o0o ( url )
  if 96 - 96: Ii . IIiIiII11i
def I11iiiiI1i ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classicmovies.png' )
def iI1IIii1IiI1iI1I ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "v.src = '([^']*)';" ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OO0 ( url )
  if 31 - 31: oOo0O0Ooo / ii . iI11I1II1I1I * OOooOOo . ii + IIiIiII11i
def oOIIiIi ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classictv.png' )
def II1IIii1I11I ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  if 'mp4' in url :
   oO00oo0o00o0o ( url )
 for url in OooOoooOo :
  yt . PlayVideo ( url )
  if 17 - 17: o0o00Oo0O
def I11iIIi ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1I1ii11i1Iii , 8071 , III1iII1I1ii + 'streams.png' )
def I111Ii11i11I ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for IIIii1I , url in IIi1I11I1II :
  if '(Free Access)' in IIIii1I :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def i11I ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , IIIii1I , url in IIi1I11I1II :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  ii1iII1II ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOO00o000o , O000OOO , '' )
  if 75 - 75: oO0oo0o * O0OOOoOoo0
def OO0Oo00OO0oo ( ) :
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , 'http://www.xvideos.com/best' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.xvideos.com' , 10106 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , 'http://xvideos.com' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , 'http://www.xvideos.com/verified/videos' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , 'http://www.xvideos.com/tags' , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 if 53 - 53: oO0o - O0OOOoOoo0 + iI1ii11iIi1i
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , 'http://www.xvideos.com/porn' , 101001 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IiIIi11i111 ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10107 , III1iII1I1ii + 'Jizbox.png' , '' , '' , )
 if 29 - 29: O00o0O00 + ii + oO0oo0o * oOo0O0Ooo - iI1ii11iIi1i / Ii
def iiiIIiiIi ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , i11111I1I in IIi1I11I1II :
  IiIIi11i111 ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[COLORgreen] - No of Videos : [COLORorange]' + i11111I1I + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def Oooo0oOooOO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 O0ooooO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in O0ooooO :
  IiIIi11i111 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , i11111I1I in IIi1I11I1II :
  IiIIi11i111 ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[COLORgreen] - No of Videos : [COLORorange]' + ( i11111I1I + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 68 - 68: O00o0O00 - ii
def IiIII ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 O0ooooO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for url in O0ooooO :
  IiIIi11i111 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , url , IIIii1I , iIi1iIIIiIiI in IIi1I11I1II :
  IiIIi11i111 ( IIIii1I + '--' + ( iIi1iIIIiIiI ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOOO00o000o ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 38 - 38: iI11I1II1I1I + oOo0O0Ooo + I11O0O0oOO00O00o * oO0o + oO0o + Ii
  if 56 - 56: iI1ii11iIi1i + oOo0O0Ooo - I11i / I11i . IIiIiII11i - iI1ii11iIi1i
def i1oo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , url , IIIii1I , ooo , OooOoo in IIi1I11I1II :
  IiIIi11i111 ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[COLORgreen] - Porn Quality : [COLORorange]' + OooOoo + ' - [COLORred]' + ooo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOOO00o000o , oOOO00o000o , OooOoo + ' - ' + ooo )
 Oooo0Oo00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for url in Oooo0Oo00o :
  IiIIi11i111 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 32 - 32: OOooOOo . iI11I1II1I1I % oO0oo0o . o0o00Oo0O . OOooOOo / Ii1IIIi1
def iI1O000OOOo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii1IIi111 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 O0ooooO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in O0ooooO :
  IiIIi11i111 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii1IIi111 ) )
 for url , IIIii1I in IIi1I11I1II :
  if '/c/' in url :
   IiIIi11i111 ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 82 - 82: I11O0O0oOO00O00o / OOooOOo - O00o0O00 / O0OOOoOoo0
   if 50 - 50: O00o0O00 + oO0o . Ii + Ii1I + Ii
def IIi11I1i1I1I ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiII1I = ( IiIi1iIIi1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OoOo0oOooOoOO = IiII1I . lower ( )
 I11i11i1 = 'http://www.xvideos.com/?k=' + OoOo0oOooOoOO
 print I11i11i1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( I11i11i1 )
 IIi1I11I1II = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , i1I1ii11i1Iii , IIIii1I , ooo , OooOoo in IIi1I11I1II :
  IiIIi11i111 ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[COLORgreen] - Porn Quality : [COLORorange]' + OooOoo + ' - [COLORred]' + ooo + '[/COLOR]' , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10108 , oOOO00o000o , oOOO00o000o , OooOoo + ' - ' + ooo )
 Oooo0Oo00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in Oooo0Oo00o :
  IiIIi11i111 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 72 - 72: iI1ii11iIi1i / I1ii11iIi11i / oO0oo0o * OOooOOo + O00o0O00
def OOoo0OOOo0o ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 Ooooo = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'http' in url :
   OooOoOo ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in OooOoooOo :
  if 'http' in url :
   OooOoOo ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in Ooooo :
  if 'http' in url :
   OooOoOo ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 10 - 10: ii1ii11IIIiiI
def I11i1i11IiIi1 ( url ) :
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 import urlresolver
 try : iiiI1I . play ( url )
 except : pass
 if 26 - 26: ooOoO0O00 / Ii1IIIi1 . Ii1IIIi1
 if 20 - 20: O00o0O00 - Ii1IIIi1 / I1ii11iIi11i * oO0o
def o00O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 8091 , III1iII1I1ii + 'gofish.png' )
def IIIIIiiI ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 1092 , oOOO00o000o )
 for url in next :
  iI1I ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def i1iIii ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 8092 , oOOO00o000o )
 for url in next :
  iI1I ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def O0o00 ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "videoId: '([^']*)'," ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 8 - 8: ii1ii11IIIiiI * I1ii11iIi11i - O00o0O00 . iI11I1II1I1I
  if 48 - 48: Ii / IIiIiII11i + iI1ii11iIi1i + I11i . ii1ii11IIIiiI % O00o0O00
  if 88 - 88: ii1ii11IIIiiI . ii1ii11IIIiiI
O0OoO0oooOO = '{PQ},' ; i1ii11I111Ii = '{SC},' ; OOoO00O = '{XG},' ; iio00O0o00oo = '{JP},' ; iIiiII = '{HW},' ; iII1I = '{RT},'
def II1i11I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o00oOOo0Oo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 91 - 91: IIiIiII11i - iI11I1II1I1I / ooOoO0O00 * ooOoO0O00 % I1ii11iIi11i
 I1i11iIIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0OOoOooO0ooO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 IiiiIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IiI111 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0OO00ooO0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiIi1iIIi1
 OOOOOoO00oo00 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIIIII11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 ooooOOO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1i = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 62 - 62: ii . iI1ii11iIi1i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 28 - 28: oO0oo0o . oO0oo0o . iI11I1II1I1I . O00o0O00 . Ii1I * Ii
 if 72 - 72: I11O0O0oOO00O00o
 ii1ii1ii = ooOooo000oOO ( I1i11iIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( o0OOoOooO0ooO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1I1IIiIIi = ooOooo000oOO ( IiiiIi )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iII1ii1IIII = ooOooo000oOO ( OO0OO00ooO0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 Oo0o0O0OOOo0 = ooOooo000oOO ( OOOOOoO00oo00 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 I1ii1i = ooOooo000oOO ( iIIIII11 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 OO00OoOO = ooOooo000oOO ( ooooOOO0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iiii1II1ii11 = ooOooo000oOO ( Ii1i )
 if 37 - 37: ii1ii11IIIiiI - oO0oo0o - oO0o
 if 42 - 42: iI11I1II1I1I % iI1ii11iIi1i - Ii1I + iI11I1II1I1I
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
  for iiI1I , IIIii1I in IIi1I11I1II :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1I1ii11i1Iii + iiI1I ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 64 - 64: ooOOOoO * iI11I1II1I1I . Ii1I / I11O0O0oOO00O00o * iI11I1II1I1I
    if 4 - 4: O0OOOoOoo0 % ooOOOoO . ii1ii11IIIiiI
    if 91 - 91: Ii1I + iI11I1II1I1I % ooOOOoO
    if 90 - 90: O0OOOoOoo0 - I11O0O0oOO00O00o . oO0o + oO0o
    if 45 - 45: OOooOOo / ii . ii1ii11IIIiiI % o0o00Oo0O * Ii1I * I1ii11iIi11i
    if 65 - 65: I11i + ii1ii11IIIiiI - o0o00Oo0O
    if 30 - 30: ooOOOoO - Ii1IIIi1 - oO0o
 if ii1ii1ii != 'Failed' :
  Ooooo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for iiI1I , IIIii1I in Ooooo :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i11iIIi + iiI1I ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  ii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in ii11 :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    ii1iII1II ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 99 - 99: Ii1I - oO0oo0o
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if i1I1IIiIIi != 'Failed' :
  iiIo000Ooo00o00O = [ ]
  ooo0O0O0oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1IIiIIi )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in ooo0O0O0oo0 :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    if IIIii1I in iiIo000Ooo00o00O :
     pass
    else :
     o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i1I1ii11i1Iii , 1016 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
     iiIo000Ooo00o00O . append ( IIIii1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if iII1ii1IIII != 'Failed' :
  oo000oO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iII1ii1IIII )
  for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in oo000oO :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1I1ii11i1Iii , 7067 , oOOO00o000o )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 8 - 8: oOo0O0Ooo % IIiIiII11i - I11i - I11O0O0oOO00O00o % oOo0O0Ooo
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 93 - 93: iI1ii11iIi1i * Ii1IIIi1 / O00o0O00
    if 88 - 88: oO0oo0o
    if 1 - 1: I1ii11iIi11i
    if 95 - 95: ii / I11O0O0oOO00O00o % ii / O0OOOoOoo0 * ooOOOoO
    if 75 - 75: o0o00Oo0O
    if 56 - 56: oO0o / IIiIiII11i
    if 39 - 39: OOooOOo - ii - ooOoO0O00 / IIiIiII11i
    if 49 - 49: I1ii11iIi11i + o0o00Oo0O + ooOOOoO . IIiIiII11i % O0OOOoOoo0
    if 33 - 33: OOooOOo . iI11I1II1I1I / I11O0O0oOO00O00o % iI1ii11iIi1i
 if I1ii1i != 'Failed' :
  IIiiI11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1ii1i )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in IIiiI11 :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    ii1iII1II ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 7 - 7: oOo0O0Ooo / oO0o + ii1ii11IIIiiI + I11O0O0oOO00O00o / oOo0O0Ooo
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if OO00OoOO != 'Failed' :
  oOooO0oo00o000O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO00OoOO )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in oOooO0oo00o000O :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    ii1iII1II ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Herovision[/COLOR]' ) , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 66 - 66: ii + I11i . ooOoO0O00 * Ii1IIIi1
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: I11O0O0oOO00O00o / ii1ii11IIIiiI
 if iiii1II1ii11 != 'Failed' :
  iiIIiii1iii1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiii1II1ii11 )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , IIIii1I in iiIIiii1iii1I :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 14 - 14: o0o00Oo0O / I11O0O0oOO00O00o . oO0o % Ii1IIIi1 . oO0oo0o
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 OooOO0oOOo0O = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
 for Ii1III1 in OooOO0oOOo0O :
  ooIii1ii1II1iI1 = I11i1I1I + Ii1III1 + IIIII
  Iii1II1 = ooOooo000oOO ( ooIii1ii1II1iI1 )
  if Iii1II1 != 'Failed' :
   oOiii1IiII = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Iii1II1 )
   for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in oOiii1IiII :
    if IiIi1iIIi1 in IIIii1I . lower ( ) :
     ii1iII1II ( '[COLOR' + iiI1IiI + ']' + IIIii1I + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , 222 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 65 - 65: O0OOOoOoo0 % o0o00Oo0O
     I1I1i1I ( 'tvshows' , 'Media Info 3' )
     if 17 - 17: ooOoO0O00 + oO0oo0o . I11O0O0oOO00O00o + ooOoO0O00 - IIiIiII11i % oOo0O0Ooo
 OooOO0oOOo0O = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 34 - 34: oOo0O0Ooo
 if 57 - 57: O00o0O00 . iI1ii11iIi1i % I11i
 for Ii1III1 in OooOO0oOOo0O :
  ooIii1ii1II1iI1 = o00oOOo0Oo + Ii1III1
  I1I11 = ooOooo000oOO ( ooIii1ii1II1iI1 )
  if I1I11 != 'Failed' :
   iI1i1iI1iI = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1I11 )
   for iiI1I , IIIii1I in iI1i1iI1iI :
    if IiIi1iIIi1 in IIIii1I . lower ( ) :
     OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o00oOOo0Oo + Ii1III1 + iiI1I ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 18 - 18: I11O0O0oOO00O00o + I1ii11iIi11i - oO0o / ii1ii11IIIiiI / O00o0O00
     I1I1i1I ( 'tvshows' , 'Media Info 3' )
     if 53 - 53: O00o0O00 + I11i . oO0oo0o / I11O0O0oOO00O00o
     if 52 - 52: ii1ii11IIIiiI + ii1ii11IIIiiI
def II1I1Ii ( ) :
 if 73 - 73: I11i . Ii % ii + O0OOOoOoo0 . ii / O00o0O00
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 if 54 - 54: OOooOOo . ii
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( IiIi1iIIi1 ) . replace ( ' ' , '%20' )
 ii1II = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I1i11iIIi = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0OOoOooO0ooO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IiiiIi = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OoOo0oOooOoOO ) . replace ( ' ' , '+' )
 IiI111 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OO0OO00ooO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OOOOOoO00oo00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 36 - 36: oO0oo0o / IIiIiII11i * ooOOOoO % Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 31 - 31: IIiIiII11i + O00o0O00 - ii . I11O0O0oOO00O00o
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0 = ooOooo000oOO ( ii1II )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ii1ii1ii = ooOooo000oOO ( I1i11iIIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( o0OOoOooO0ooO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1I1IIiIIi = cloudflare . source ( IiiiIi )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 I1I11 = ooOooo000oOO ( IiI111 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iII1ii1IIII = ooOooo000oOO ( OO0OO00ooO0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 Oo0o0O0OOOo0 = ooOooo000oOO ( OOOOOoO00oo00 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 28 - 28: iI1ii11iIi1i . Ii1I
 if Oo0o0O0OOOo0 != 'Failed' :
  oOo000Oo00o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0o0O0OOOo0 )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in oOo000Oo00o :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source HeroVision[/COLOR]' ) , i1I1ii11i1Iii , 1016 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 81 - 81: ii
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 88 - 88: o0o00Oo0O * I11i
 if iII1ii1IIII != 'Failed' :
  oo000oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1ii1IIII )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in oo000oO :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 1016 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: ooOOOoO - O0OOOoOoo0 * Ii1IIIi1 * I11O0O0oOO00O00o
    if 84 - 84: iI1ii11iIi1i + Ii1I % oOo0O0Ooo + Ii
    if 37 - 37: I11O0O0oOO00O00o % Ii1I / O0OOOoOoo0
    if 94 - 94: I11O0O0oOO00O00o / oO0o . I11i
    if 1 - 1: I1ii11iIi11i . IIiIiII11i
    if 93 - 93: IIiIiII11i . Ii + IIiIiII11i % oO0oo0o
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 98 - 98: ii1ii11IIIiiI * oO0oo0o * OOooOOo + iI1ii11iIi1i * Ii1IIIi1
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oOOO00o000o , i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , oOOO00o000o , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 4 - 4: ooOOOoO
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 16 - 16: iI11I1II1I1I * Ii1IIIi1 + oO0oo0o . o0o00Oo0O . I11i
    if 99 - 99: Ii - Ii1IIIi1
    if 85 - 85: ii1ii11IIIiiI % Ii1I
    if 95 - 95: oO0o * O00o0O00 * Ii1IIIi1 . I11i
    if 73 - 73: oO0o
    if 28 - 28: ii - I11O0O0oOO00O00o
    if 84 - 84: IIiIiII11i
    if 36 - 36: O00o0O00 - OOooOOo - iI11I1II1I1I
    if 10 - 10: Ii1I / iI1ii11iIi1i * ooOoO0O00 % o0o00Oo0O + I11O0O0oOO00O00o
    if 25 - 25: ii1ii11IIIiiI - iI1ii11iIi1i / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
    if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + oO0oo0o + oO0oo0o + Ii1IIIi1
    if 4 - 4: I11i + I11O0O0oOO00O00o / Ii1IIIi1 + ooOoO0O00 % I11i % Ii1IIIi1
    if 80 - 80: iI1ii11iIi1i
    if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
    if 59 - 59: Ii1I + I11O0O0oOO00O00o . oO0oo0o
    if 87 - 87: oO0o
    if 34 - 34: ii1ii11IIIiiI . OOooOOo / Ii / Ii1IIIi1
    if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + O00o0O00
    if 31 - 31: iI1ii11iIi1i * I11i * iI1ii11iIi1i + oO0o * I11i . ii1ii11IIIiiI
 if ii1ii1ii != 'Failed' :
  Ooooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for IIIii1I in Ooooo :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    iI1I ( ( IIIii1I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11iIIi + IIIii1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 89 - 89: ii * iI1ii11iIi1i * oOo0O0Ooo . O0OOOoOoo0 * iI1ii11iIi1i / Ii1IIIi1
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  ii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for IIIii1I in ii11 :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    iI1I ( ( IIIii1I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OOoOooO0ooO + IIIii1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 46 - 46: Ii
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if i1I1IIiIIi != 'Failed' :
  ooo0O0O0oo0 = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( i1I1IIiIIi )
  for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in ooo0O0O0oo0 :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + ' - Source - Dizi[/COLOR]' , i1I1ii11i1Iii , 8062 , oOOO00o000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . Ii1IIIi1 % OOooOOo + oOo0O0Ooo
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if I1I11 != 'Failed' :
  iI1i1iI1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I11 )
  for i1I1ii11i1Iii , IiiiiI1i1Iii , Ii1II , o0o0oo0 , IIIii1I in iI1i1iI1iI :
   if OoOo0oOooOoOO in IIIii1I . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '- Source Scooby[/COLOR]' ) , i1I1ii11i1Iii , 1016 , IiiiiI1i1Iii , o0o0oo0 , Ii1II )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 48 - 48: ii1ii11IIIiiI % Ii1IIIi1 % iI1ii11iIi1i % iI11I1II1I1I . iI1ii11iIi1i
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: Ii1IIIi1 * oO0o % o0o00Oo0O + I11O0O0oOO00O00o + Ii1I
 III1I11Iiii = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if I1I11 != 'Failed' :
  for Ii1III1 in III1I11Iiii :
   ooIii1ii1II1iI1 = I11i1I1I + Ii1III1 + IIIII
   OO00OoOO = O0i1II1Iiii1I11 ( ooIii1ii1II1iI1 )
   if OO00OoOO != 'Failed' :
    oOooO0oo00o000O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO00OoOO )
    for IIIii1I , Ii1II , i1I1ii11i1Iii , oOOO00o000o , O000OOO , OooO0Oo0 in oOooO0oo00o000O :
     if OoOo0oOooOoOO in IIIii1I . lower ( ) :
      o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , OooO0Oo0 , oOOO00o000o , O000OOO , Ii1II )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 44 - 44: oO0o - I1ii11iIi11i / Ii1IIIi1
      I1I1i1I ( 'tvshows' , 'Media Info 3' )
      if 4 - 4: ii + Ii1IIIi1 % o0o00Oo0O + iI11I1II1I1I % Ii1IIIi1 * Ii
      if 32 - 32: OOooOOo + O0OOOoOoo0 + iI1ii11iIi1i + oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IIIIII1 ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IiIi1iIIi1 ) . replace ( ' ' , '+' )
 if 99 - 99: O00o0O00 + oOo0O0Ooo . Ii1I * ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + O00o0O00 * IIiIiII11i
 if IIIi1I1IIii1II != 'Failed' :
  OooOoooOo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , IIIii1I in OooOoooOo :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    OooOoOo ( ( IIIii1I + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + i1I1ii11i1Iii ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 34 - 34: I11i % ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
iIIIi = '{ZH},' ; oo0 = '{IX},' ; o00o0 = '{LM},'
if 84 - 84: OOooOOo - I1ii11iIi11i . O0OOOoOoo0 . ooOOOoO - I1ii11iIi11i
def o0Oo0oO00Oooo ( url ) :
 Ii1II1I11i1I = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Ii1II1I11i1I )
 for url , OOO0OoO0oo0OO , i1iI11i1IIi , IIIii1I in IIi1I11I1II :
  iI1I ( ( OOO0OoO0oo0OO ) . replace ( 'Sezon' , ' Season ' ) + ( i1iI11i1IIi ) . replace ( 'Bölüm' , ' Episode ' ) + IIIii1I , url , 8063 , '' )
  if 91 - 91: oO0o / oO0o . IIiIiII11i . O0OOOoOoo0 - oOo0O0Ooo
  if 23 - 23: oOo0O0Ooo
  if 7 - 7: Ii1IIIi1 % Ii1I
  if 64 - 64: ii1ii11IIIiiI + Ii
def iI1i11i ( url ) :
 Ii1II1I11i1I = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Ii1II1I11i1I )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( IIIii1I , url , 222 , '' )
  if 4 - 4: oO0oo0o * oOo0O0Ooo - O0OOOoOoo0 / IIiIiII11i + O00o0O00 / Ii
  if 63 - 63: oO0o + O0OOOoOoo0
  if 3 - 3: OOooOOo - ii1ii11IIIiiI / oO0oo0o . o0o00Oo0O * O0OOOoOoo0 / Ii1I
  if 18 - 18: iI1ii11iIi1i
def o0OOoO ( ) :
 if 11 - 11: iI1ii11iIi1i * I11i / ooOOOoO + OOooOOo + oO0o % ii1ii11IIIiiI
 Ii1II1I11i1I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Ii1II1I11i1I )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I , i1iI11i1IIi in IIi1I11I1II :
  iI1I ( IIIii1I + '  -  ' + ( i1iI11i1IIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 8063 , oOOO00o000o )
  if 18 - 18: oOo0O0Ooo - OOooOOo
def II1III ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I , oOOO00o000o in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 8002 , oOOO00o000o )
def II11iiIIiI11I ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( IiIiII1 )
 for oOOO00o000o , time , url , IIIii1I , i1II11Iii1I in IIi1I11I1II :
  o0OIiII ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , time ) , url , 1015 , oOOO00o000o , i1II11Iii1I )
  if 56 - 56: ii * ooOOOoO + ii1ii11IIIiiI / oOo0O0Ooo * ooOOOoO / ooOoO0O00
def i111IiIi1 ( ) :
 if 16 - 16: Ii * O00o0O00 . ooOOOoO
 iI1I ( 'Coronation Street' , '' , 8001 , '' )
 iI1I ( 'Eastenders' , '' , 8002 , '' )
 iI1I ( 'Emmerdale' , '' , 8003 , '' )
 iI1I ( 'Hollyoaks' , '' , 8004 , '' )
 iI1I ( 'Im a Celebrity' , '' , 8005 , '' )
 if 100 - 100: oO0o . I11O0O0oOO00O00o / iI1ii11iIi1i . I11i - OOooOOo . I11O0O0oOO00O00o
 if 30 - 30: iI1ii11iIi1i % I11O0O0oOO00O00o + I11i
 if 65 - 65: iI11I1II1I1I . Ii1IIIi1 / iI1ii11iIi1i
 if 12 - 12: oOo0O0Ooo + ii1ii11IIIiiI
def oOo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Holly' in IIIii1I :
   oOOO00o000o = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1I1ii11i1Iii :
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , oOOO00o000o )
   else :
    pass
    if 90 - 90: IIiIiII11i / oO0o / iI1ii11iIi1i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 70 - 70: iI1ii11iIi1i - IIiIiII11i . I1ii11iIi11i / I1ii11iIi11i
def IIIi1iiIIiiiI ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'East' in IIIii1I :
   oOOO00o000o = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , oOOO00o000o )
   else :
    pass
    if 26 - 26: O0OOOoOoo0 % oO0oo0o + oOo0O0Ooo / ooOOOoO . oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: ii + ii - Ii * oOo0O0Ooo * ooOoO0O00 / IIiIiII11i
def OOO00000O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Emmer' in IIIii1I :
   oOOO00o000o = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , oOOO00o000o )
   else :
    pass
    if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: Ii1I
def O0oOoo00Oo0O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Coro' in IIIii1I :
   oOOO00o000o = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , oOOO00o000o )
   else :
    pass
    if 5 - 5: o0o00Oo0O - Ii1IIIi1 / ii1ii11IIIiiI . I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: Ii1I - OOooOOo
def OOoooIIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Celeb' in IIIii1I :
   oOOO00o000o = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , oOOO00o000o )
   else :
    pass
    if 87 - 87: ooOOOoO
def oOOo0OOoOO0 ( name , url ) :
 IiIiIIi1IiiIi1III = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiIiIIi1IiiIi1III :
  IiIiIiiIIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  IiIiII1 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( IiIiII1 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  IiIiII1 = open_url ( url )
  OOo00O00o0O0 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( IiIiII1 ) [ - 1 ]
  IiIiIiiIIii = OOo00O00o0O0 . replace ( '\\/' , '/' )
 I1iII = xbmcgui . ListItem ( name , '' , '' )
 I1iII . setPath ( IiIiIiiIIii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iII )
 if 31 - 31: oOo0O0Ooo
 if 36 - 36: oO0o + oO0o + oO0o % I1ii11iIi11i * Ii1IIIi1
def O0IIi1i ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
 for i1I1ii11i1Iii , IIIii1I in OooOoooOo :
  iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 56 - 56: I11i / ooOOOoO
def iI1I1 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Movies' in IIIii1I :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( i1I1ii11i1Iii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def I1IiIIiIiI ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IiIiII1 )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOOO00o000o )
 for url in OooOoooOo :
  iI1I ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 93 - 93: iI11I1II1I1I
  if 75 - 75: oO0o % ii
def ii1I1IIii11 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , url , oOOO00o000o in IIi1I11I1II :
  if '{{' in IIIii1I :
   pass
  else :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOOO00o000o )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
iiiI = '{UJ},' ; ooo0o00o = '{WE},' ; O0oOOo0 = '{WP},' ; oooOOOoO0O = '{PP},'
def iI ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , url , oOOO00o000o in IIi1I11I1II :
  if '{{' in IIIii1I :
   pass
  else :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOOO00o000o )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOO0O00 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  Oo0O000OoO00 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0O000OoO00 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: oO0oo0o
 if 34 - 34: Ii1IIIi1 % Ii + Ii - Ii1IIIi1
 if 2 - 2: IIiIiII11i + ooOoO0O00
def oO0OO00 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if '(cooltvseries.com)' in IIIii1I :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , IIIii1I in OooOoooOo :
  if '(cooltvseries.com)' in IIIii1I :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def IiiIO0oooooO ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  oO00oo0o00o0o ( ( url ) . replace ( ' ' , '%20' ) )
IIi1II11II = '{XX},' ; i1ii11III = '{UD},' ; o00Oii1I1I1 = '{YT},' ; oo0oOOO0oOoo = '{JS},' ; Ii1 = '{PF},'
if 77 - 77: Ii1IIIi1
def OOoo00O0oo ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I , oOOO00o000o in IIi1I11I1II :
  OooOoOo ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( i1I1ii11i1Iii ) ) , 222 , oOOO00o000o )
  if 50 - 50: ii1ii11IIIiiI - IIiIiII11i
def iIi1IIiI ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( IiIiII1 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( IiIiII1 )
 for oOOO00o000o , url , IIIii1I in IIi1I11I1II :
  if 'youtu' in url :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOOO00o000o )
 for url in next :
  iI1I ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 33 - 33: ooOOOoO / ooOOOoO . Ii * Ii1I + I11i
def ii1iI11IiIIi ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 47 - 47: O00o0O00 . oO0oo0o + OOooOOo % ooOOOoO % ooOoO0O00 / iI11I1II1I1I
def ooIii ( url ) :
 IiIiII1 = O0i1II1Iiii1I11
 IIi1I11I1II = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 222 , oOOO00o000o )
  if 66 - 66: O00o0O00 * I11i
  if 58 - 58: iI11I1II1I1I % O00o0O00 + ii1ii11IIIiiI - ii1ii11IIIiiI . Ii + ii
  if 19 - 19: Ii
  if 80 - 80: oOo0O0Ooo
  if 58 - 58: oO0oo0o + Ii1I % OOooOOo
def Iii11I1i ( ) :
 if 81 - 81: O00o0O00 - oOo0O0Ooo % I11i
 iI1I ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 iI1I ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 7 - 7: O0OOOoOoo0 - ooOoO0O00 . OOooOOo
 if 12 - 12: ooOOOoO / oO0o / o0o00Oo0O * ooOOOoO
def o0o0oo0OOo0O0 ( Cat_Name ) :
 if 37 - 37: I11i * I1ii11iIi11i
 iI11i1I1i = False
 O000O = '0'
 if Cat_Name == 'All Channels' : iI11i1I1i = True
 if Cat_Name == 'Entertainment' : O000O = '1'
 if Cat_Name == 'Movies' : O000O = '2'
 if Cat_Name == 'Music' : O000O = '3'
 if Cat_Name == 'News' : O000O = '4'
 if Cat_Name == 'Sports' : O000O = '5'
 if Cat_Name == 'Documentary' : O000O = '6'
 if Cat_Name == 'Kids' : O000O = '7'
 if Cat_Name == 'Food' : O000O = '8'
 if Cat_Name == 'Religious' : O000O = '9'
 if Cat_Name == 'USA Channels' : O000O = '10'
 if Cat_Name == 'Other' : O000O = '11'
 if 14 - 14: IIiIiII11i . oOo0O0Ooo - oO0oo0o * o0o00Oo0O * iI11I1II1I1I + Ii1IIIi1
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IiIiII1 )
 print 'Len Match: >>>' + str ( len ( IIi1I11I1II ) )
 for IIIii1I , oOOO00o000o , Oo0OOo0o0o0o0 in IIi1I11I1II :
  o00oooo = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOOO00o000o ) . replace ( '\\' , '' )
  if Oo0OOo0o0o0o0 == O000O :
   iI1I ( IIIii1I , '' , 7022 , o00oooo )
  elif iI11i1I1i == True :
   iI1I ( IIIii1I , '' , 7022 , o00oooo )
  else : pass
  if 63 - 63: IIiIiII11i - I11O0O0oOO00O00o . OOooOOo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 8 - 8: oOo0O0Ooo * O0OOOoOoo0 / ooOOOoO + OOooOOo . ooOOOoO - O00o0O00
def Oo0O ( Search_Name ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IiIiII1 )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( IiIiII1 )
 for oOOO00o000o , i1I1ii11i1Iii , ii1II , I1i11iIIi in IIi1I11I1II :
  o00oooo = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOOO00o000o ) . replace ( '\\' , '' )
  OooOoOo ( Search_Name + ': Link 1' , ( i1I1ii11i1Iii ) . replace ( '\\' , '' ) , 222 , o00oooo )
  OooOoOo ( Search_Name + ': Link 2' , ( ii1II ) . replace ( '\\' , '' ) , 222 , o00oooo )
  OooOoOo ( Search_Name + ': Link 3' , ( I1i11iIIi ) . replace ( '\\' , '' ) , 222 , o00oooo )
  if 60 - 60: O00o0O00 * O0OOOoOoo0 * oO0o
def O0ooO ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  OooOoOo ( IIIii1I , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def Iii1iIIIi11I1 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  OooOoOo ( IIIii1I , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def IIII11Ii1I11I ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( IiIiII1 )
 for IIIii1I , i1I1ii11i1Iii in IIi1I11I1II :
  OooOoOo ( IIIii1I , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 40 - 40: iI1ii11iIi1i + Ii1I * ii1ii11IIIiiI - oO0oo0o % iI1ii11iIi1i
def oo0o0000 ( url ) :
 url
 iiiiIiIi = xbmcgui . ListItem ( IIIii1I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiiIiIi )
 return
 if 26 - 26: O0OOOoOoo0 + oO0o / OOooOOo . IIiIiII11i * iI1ii11iIi1i
 if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + Ii1IIIi1 % oOo0O0Ooo * oO0oo0o
def O0o0 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( IiIiII1 )
 for url , Ii1II , oOOO00o000o , IIIii1I in IIi1I11I1II :
  o0OIiII ( IIIii1I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOOO00o000o , '' , ( Ii1II ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I1i1I ( 'tvshows' , 'Media Info 3' )
 for url in OooOoooOo :
  iI1I ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 64 - 64: ii + I1ii11iIi11i
def I1111i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , Ii1II , oOOO00o000o in IIi1I11I1II :
  ii1iII1II ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOOO00o000o , '' , Ii1II )
  I1I1i1I ( 'tvshows' , 'Media Info 3' )
 iIi1iI = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for I1I1II1iiI1I in iIi1iI :
  II1i111i = ( I1I1II1iiI1I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o0OIiII ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOOO00o000o , '' , II1i111i )
  if 58 - 58: O0OOOoOoo0
def i1iI11ii ( INFO ) :
 ii1 ( 'info for workout' , INFO )
 if 65 - 65: ooOoO0O00 . Ii
 if 62 - 62: Ii1I + oO0o - Ii1I * ooOOOoO - I11O0O0oOO00O00o * I11O0O0oOO00O00o
 if 99 - 99: I1ii11iIi11i / ii1ii11IIIiiI * I1ii11iIi11i / iI11I1II1I1I * ooOOOoO
def oo00OOo0 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( ( IIIii1I ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def OOO0OOoOOO ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , url , 9032 , III1iII1I1ii + 'icon.png' )
def oOoO0o0o ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  if '=' in IIIii1I :
   pass
  else :
   OooOoOo ( ( IIIii1I ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def O00O000oOO0oO ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  if '=' in IIIii1I :
   pass
  else :
   OooOoOo ( IIIii1I , url , 222 , III1iII1I1ii + 'icon.png' )
   if 88 - 88: I11i . oOo0O0Ooo % oO0oo0o . I1ii11iIi11i % O0OOOoOoo0 . oO0oo0o
   if 53 - 53: ooOoO0O00 % iI1ii11iIi1i - ii / OOooOOo - iI11I1II1I1I
   if 9 - 9: ii1ii11IIIiiI - oO0o + iI11I1II1I1I % o0o00Oo0O + I11O0O0oOO00O00o + ooOOOoO
   if 50 - 50: ooOoO0O00 + O0OOOoOoo0
   if 64 - 64: I11i % oO0oo0o . O0OOOoOoo0
def i1IiiI11iIiiI11I ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi1I11I1II = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'Daily' in IIIii1I :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 9008 , Ooo )
def O0oo0ooO00 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def oOoO0 ( url ) :
 OooOoOo ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OooOoOo ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OooOoOo ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  OooOoOo ( ( IIIii1I ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 50 - 50: ii1ii11IIIiiI * ii1ii11IIIiiI * I1ii11iIi11i - oO0o
def IIi1iI ( ) :
 IiIiII1 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if '.m3u' in i1I1ii11i1Iii :
   iI1I ( ( IIIii1I ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + i1I1ii11i1Iii ) , 9011 , III1iII1I1ii + 'disclose.png' )
def I1111iIIiIIII ( url ) :
 IiIiII1 = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  OooOoOo ( ( IIIii1I ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 55 - 55: oO0o / ii
def OOoooO00o0oo0 ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  if 'category' in i1I1ii11i1Iii :
   iI1I ( IIIii1I , 'http://www.disclose.tv/' + i1I1ii11i1Iii , 7010 , III1iII1I1ii + 'disclose.png' )
   if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
   if 61 - 61: iI1ii11iIi1i * iI1ii11iIi1i
def O0III1Iiii1i11 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( IiIiII1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IiIiII1 )
 for url , IIIii1I , oOOO00o000o in IIi1I11I1II :
  iI1I ( IIIii1I , 'http://www.disclose.tv/' + url , 7011 , oOOO00o000o )
 for url in next :
  iI1I ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 74 - 74: I1ii11iIi11i / ii1ii11IIIiiI % ii1ii11IIIiiI . ooOOOoO
  if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( IiIiII1 )
 Ooooo = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  if 'http' in url :
   OooOoOo ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , IIIii1I in OooOoooOo :
  OooOoOo ( IIIii1I , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in Ooooo :
  OooOoOo ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 67 - 67: Ii1I + oO0oo0o * ooOOOoO / IIiIiII11i % oO0o % oO0o
  if 28 - 28: OOooOOo % oO0oo0o - O00o0O00 + O00o0O00 + oO0oo0o / iI11I1II1I1I
def oo0o ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 69 - 69: I11i + Ii1I / iI11I1II1I1I . ooOOOoO % Ii1I * OOooOOo
def Iii1i11 ( name , url , img ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IiIi11i = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 i1I11IiI = len ( IiIi11i )
 if 40 - 40: IIiIiII11i
 if 7 - 7: O00o0O00 / oO0o
 if i1I11IiI == 1 :
  for oOOo in IiIi11i :
   oOOo = oOOo . replace ( 'player' , 'watch' )
   oOOOo0Oooo = oOOo + '&fv=&sou='
   I1iiIIiI11I = O0i1II1Iiii1I11 ( oOOOo0Oooo )
   I11II1I = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( I1iiIIiI11I )
   for OoOoO00o00 in I11II1I :
    oOoOo000 = False
    Resolve ( OoOoO00o00 )
    if 37 - 37: Ii1IIIi1
 elif i1I11IiI > 1 :
  if 15 - 15: I11i % oO0o / Ii1IIIi1
  for oOOo in IiIi11i :
   II1IIIi = O0i1II1Iiii1I11 ( oOOo )
   Iiii = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( II1IIIi )
   O0O0OOooo = Iiii
   O0O0OOooo = ( str ( O0O0OOooo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0O0OOooo
   OooOoOo ( 'DOUBLE LINK' , O0O0OOooo , 424 , '' )
   if 66 - 66: iI1ii11iIi1i % oO0oo0o
   for url in Iiii :
    iI1I ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ii1II = Google . resolve ( url )
    except :
     pass
    try :
     iiIIiI1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ii1II ) )
     for oOoO0oOO0o , oO0000oo0o0o0 in iiIIiI1I :
      if 21 - 21: ooOoO0O00
      HD_URLS . append ( oOoO0oOO0o )
      SD_URLS . append ( oO0000oo0o0o0 )
    except :
     pass
 else :
  pass
  if 85 - 85: Ii1I * OOooOOo % I11O0O0oOO00O00o
def i1iIIIiI ( ) :
 if 47 - 47: ii1ii11IIIiiI % O00o0O00 * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
 if 2 - 2: ii1ii11IIIiiI % ii - O0OOOoOoo0 * Ii1I * ooOOOoO
 iI1I ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / O0OOOoOoo0 . O00o0O00 % oOo0O0Ooo * I11O0O0oOO00O00o
 iI1I ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 95 - 95: oO0oo0o
 if 80 - 80: ooOOOoO
def iiiI1I1iiiII ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( 'http://cnfstudio.com/' )
 IIi1I11I1II = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , 'http://cnfstudio.com/genre/' + i1I1ii11i1Iii , 7003 , III1iII1I1ii + 'icon.png' )
  if 5 - 5: OOooOOo % Ii1I . O0OOOoOoo0 . I11O0O0oOO00O00o - Ii
iI111I11I1I1 = xbmcgui . Dialog ( )
if 39 - 39: Ii + O00o0O00 % Ii1IIIi1 + iI1ii11iIi1i * oOo0O0Ooo + ii1ii11IIIiiI
Oo00oOo = '{UN},' ; o0ooOo000oo = '{IG},' ; OoO0O00oo = '{PL},' ; ooo0o0oooo = '{LO},' ; o0Oo = '{LP},' ; IiiiiiiI111i = '{HA},' ; iiIIIIiI11II1 = '{XD},' ; IiI1i11i1iI = '{TA},' ; o0oo0O0OO0 = '{DP},' ; IIiI = '{JT},' ; i11I1Ii1Iiii1 = '{JJ},' ; o0oooOoOoOo = '{MM},' ; OO0O = '{FQ},' ; oo0ooOoo00Ooo = '{HH},'
if 16 - 16: oO0o % iI11I1II1I1I . I11O0O0oOO00O00o / Ii1IIIi1
def ooOOooo0o000O ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( IiIiII1 )
 oooO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( IiIiII1 )
 for oOOO00o000o , url , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOOO00o000o )
 oooO = oooO
 for url in oooO :
  iI1I ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 98 - 98: ooOoO0O00 - Ii1IIIi1
def iIIiII11iI1 ( url ) :
 if 80 - 80: Ii1IIIi1 . o0o00Oo0O
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OOO00O = url + '&fv=&sou='
  OOO00O = OOO00O . replace ( 'player' , 'watch' )
  I1Iii = II1I1Ii11 ( OOO00O )
  I1I1i = II1I1Ii11 ( url )
  if 27 - 27: Ii
  if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - iI1ii11iIi1i - iI11I1II1I1I
def II1I1Ii11 ( url ) :
 if 28 - 28: OOooOOo % ii
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OO0 ( url )
  if 13 - 13: ooOOOoO . I1ii11iIi11i - I11O0O0oOO00O00o / oO0oo0o - I1ii11iIi11i - oOo0O0Ooo
  if 84 - 84: IIiIiII11i
def Oo0ooooO0o00 ( ) :
 o0OIiII ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , III1iII1I1ii + 'LocalM3U.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , III1iII1I1ii + 'RemoteM3U.png' , OO0o , '' )
 if 34 - 34: OOooOOo % I11i - oO0oo0o
def i1Ii1iiIIi1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  iii1o0o0O00OoOo = open ( O0OoO000O0OO , 'r' )
  for iiiiIiIi in iii1o0o0O00OoOo :
   oOO0ooO00o = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iiiiIiIi )
   for IIIii1I , i1I1ii11i1Iii in oOO0ooO00o :
    OooOoOo ( IIIii1I , i1I1ii11i1Iii , 222 , III1iII1I1ii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 56 - 56: ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
def iIIIii111 ( url ) :
 if os . path . exists ( Remote ) :
  IIIi1I1IIii1II = Iii1iiIi1II ( url )
  IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for IIIii1I , url in IIi1I11I1II :
   url = ( url ) . strip ( )
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 21 - 21: Ii1IIIi1 % ooOOOoO % I1ii11iIi11i % o0o00Oo0O
  if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
def IiI111111IIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + i1I1ii11i1Iii
 IIIii1I = 'plugin.video.GenieTv'
 if 50 - 50: OOooOOo % iI1ii11iIi1i + OOooOOo * iI1ii11iIi1i - O00o0O00
 oooiiI11 ( i1I1ii11i1Iii , IIIii1I )
 if 10 - 10: O0OOOoOoo0 - I1ii11iIi11i % IIiIiII11i
def ooOOO00Ooo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + i1I1ii11i1Iii
 IIIii1I = 'repository.GenieTv'
 if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 oooiiI11 ( i1I1ii11i1Iii , IIIii1I )
 if 46 - 46: ii1ii11IIIiiI * oO0oo0o . iI1ii11iIi1i * ii1ii11IIIiiI * iI11I1II1I1I / I11O0O0oOO00O00o
 if 46 - 46: IIiIiII11i % Ii1I . O00o0O00 . I1ii11iIi11i / Ii + oO0o
def OoOoO ( ) :
 O0oO0 = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  i1O00oo00o000o ( )
 if oO0O0OO0O == 1 :
  O0000ooO ( )
  if 83 - 83: ii1ii11IIIiiI + I11i % oO0oo0o / oO0o
  if 59 - 59: iI1ii11iIi1i * O00o0O00 . ooOOOoO
  if 68 - 68: o0o00Oo0O * iI11I1II1I1I / ii1ii11IIIiiI
  if 65 - 65: O00o0O00 - oOo0O0Ooo * ii1ii11IIIiiI
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oO00O0O000OO = 'https://addons.tvaddons.ag/'
if 58 - 58: ii1ii11IIIiiI - I11O0O0oOO00O00o
def O0000ooO ( ) :
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 I11i11i1 = 'https://addons.tvaddons.ag/search/?keyword=' + OoOo0oOooOoOO
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( I11i11i1 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , iI1IIIii , IIIii1I in IIi1I11I1II :
  o0OIiII ( IIIii1I , i1I1ii11i1Iii , 10054 , 'https://addons.tvaddons.ag/' + iI1IIIii , OO0o , '' )
  if 69 - 69: oOo0O0Ooo + I1ii11iIi11i * I11i * ooOoO0O00 % I1ii11iIi11i
  if 41 - 41: oO0oo0o . Ii1IIIi1 + ii * iI1ii11iIi1i . I11i
def i1O00oo00o000o ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oO00O0O000OO )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if 'Repositories' in IIIii1I :
   pass
  elif 'Services' in IIIii1I :
   pass
  elif 'International' in IIIii1I :
   pass
  else :
   o0OIiII ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , i1I1ii11i1Iii , 10053 , 'https://addons.tvaddons.ag/' + oOOO00o000o , OO0o , '' )
   if 11 - 11: o0o00Oo0O
   if 96 - 96: Ii1IIIi1 + I11i
def Addon ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 Iiiii1III1iIi = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if 'Please' in IIIii1I :
   pass
  else :
   ii1iII1II ( IIIii1I , url , 10054 , 'https://addons.tvaddons.ag/' + oOOO00o000o , OO0o , '' )
 for url in Iiiii1III1iIi :
  o0OIiII ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , OO0o , '' )
  if 43 - 43: oO0oo0o + OOooOOo . oOo0O0Ooo . Ii
  if 71 - 71: I11i + O00o0O00 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
def oo000O0o ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   O0oOo = os . path . join ( O0o0O0OO00o , name + '.zip' )
   try :
    os . remove ( O0oOo )
   except :
    pass
   downloader . download ( url , O0oOo , o0oOoO00o )
   o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print o0ooOO0o
   print '======================================='
   extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
   Ii1i1iI ( )
   if 99 - 99: oOo0O0Ooo
def oooiiI11 ( url , name ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 O0oOo = os . path . join ( O0o0O0OO00o , name + '.zip' )
 try :
  os . remove ( O0oOo )
 except :
  pass
 downloader . download ( url , O0oOo , o0oOoO00o )
 o0ooOO0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print o0ooOO0o
 print '======================================='
 extract . all ( O0oOo , o0ooOO0o , o0oOoO00o )
 Ii1i1iI ( )
 if 78 - 78: oO0o / iI11I1II1I1I . iI1ii11iIi1i * oO0o * OOooOOo - O00o0O00
def Ii1i1iI ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 39 - 39: Ii - O00o0O00 - ii1ii11IIIiiI + ii / oOo0O0Ooo / iI11I1II1I1I
 if 16 - 16: OOooOOo / iI1ii11iIi1i . ii1ii11IIIiiI % Ii % oOo0O0Ooo / O00o0O00
def o00oo00 ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , iI1IIIii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , url , 1007 , iI1IIIii )
def o0oO0O ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , iI1IIIii , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 1006 , iI1IIIii )
  if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
  if 95 - 95: ii1ii11IIIiiI + ooOOOoO * iI11I1II1I1I
def i11i1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , iconimage , Ii1II , O000OOO , name in IIi1I11I1II :
  if 'http' in url :
   if '.php' in url :
    II1IIi1iII1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
    for iiiiIiIi in II1IIi1iII1i :
     if iiiiIiIi == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OOo00ooOoO0o ( name , url , 1016 , iconimage , O000OOO , Ii1II )
   else :
    if 'youtube' in url :
     II1IIi1iII1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for iiiiIiIi in II1IIi1iII1i :
      if iiiiIiIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OO0OoOo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , O000OOO , Ii1II )
    else :
     II1IIi1iII1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for iiiiIiIi in II1IIi1iII1i :
      if iiiiIiIi == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OO0OoOo ( name , url , 222 , iconimage , O000OOO , Ii1II )
     I1I1i1I ( 'movies' , 'INFO' )
  else :
   II1Iii1iI ( url , iconimage , name )
   if 56 - 56: iI11I1II1I1I . I11O0O0oOO00O00o
 else :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
  for url , iI1IIIii , name in IIi1I11I1II :
   if 'http' in url :
    if '.php' in url :
     iI1I ( name , url , 1016 , iI1IIIii )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OooOoOo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iI1IIIii )
     else :
      II1IIi1iII1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
      for iiiiIiIi in II1IIi1iII1i :
       if iiiiIiIi == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OooOoOo ( name , url , 222 , iI1IIIii )
      I1I1i1I ( 'movies' , 'INFO' )
   else :
    II1Iii1iI ( url , iI1IIIii , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 2 - 2: iI1ii11iIi1i
def II1Iii1iI ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Ii1i111iI = ( url ) . replace ( oo0 , 'http' ) . replace ( i1ii11III , '.com' ) ;
 iII1ii = ( Ii1i111iI ) . replace ( o00o0 , 'a' ) . replace ( OOoO00O , 'b' ) . replace ( iio00O0o00oo , 'c' ) . replace ( ooo0o00o , 'd' ) . replace ( OoO0O00oo , 'e' ) . replace ( IIiI , 'f' ) ;
 OOO00OiI = ( iII1ii ) . replace ( IIi1II11II , 'g' ) . replace ( IiiiiiiI111i , 'h' ) . replace ( o00Oii1I1I1 , 'i' ) . replace ( Ii1 , 'j' ) . replace ( iIiiII , 'k' ) . replace ( iII1I , 'l' ) ;
 O0o00oO00O0 = ( OOO00OiI ) . replace ( I1IiiIII , 'm' ) . replace ( i1iIii1II11 , 'n' ) . replace ( OOOOoOOOO , 'o' ) . replace ( iiIi1 , 'p' ) . replace ( Oo0OOo , 'q' ) . replace ( I1i1i1IIi1I , 'r' ) ;
 IIi11iIIiIiI = ( O0o00oO00O0 ) . replace ( oo000oo00 , 's' ) . replace ( O0oOOo0 , 't' ) . replace ( IiIiiI1II , 'u' ) . replace ( iI1i , 'v' ) . replace ( oo000o0O , 'w' ) . replace ( iiIiIIiI1 , 'x' ) ;
 Ii11i = ( IIi11iIIiIiI ) . replace ( O00i1i , 'y' ) . replace ( iiii , 'z' ) . replace ( Oo00oOo , '.' ) . replace ( o0ooOo000oo , '(' ) . replace ( ooo0o0oooo , ')' ) . replace ( o0Oo , '/' ) ;
 IIiii1I1I = ( Ii11i ) . replace ( iIIIi , '1' ) . replace ( oooOOOoO0O , '2' ) . replace ( oo0O0OoO , '3' ) . replace ( IiI1i11i1iI , '4' ) . replace ( o0oo0O0OO0 , '5' ) . replace ( oo0oOOO0oOoo , '6' ) ;
 OO0O0O0oo = ( IIiii1I1I ) . replace ( i11I1Ii1Iiii1 , '7' ) . replace ( o0oooOoOoOo , '8' ) . replace ( OO0O , '9' ) . replace ( oo0ooOoo00Ooo , '0' ) . replace ( O0OoO0oooOO , ':' ) . replace ( i1ii11I111Ii , '%' ) ;
 url = ( OO0O0O0oo ) . replace ( iiiI , '-' ) . replace ( iiIIIIiI11II1 , '_' ) ;
 OooOoOo ( name , url , 222 , iconimage ) ;
 if 41 - 41: ooOoO0O00 / oO0oo0o
 if 47 - 47: ii1ii11IIIiiI
def I1IIII1 ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , iI1IIIii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 1007 , iI1IIIii )
def ooO0O ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , iI1IIIii , IIIii1I in IIi1I11I1II :
  iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 1006 , iI1IIIii )
  if 17 - 17: Ii1I - Ii1IIIi1 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * O00o0O00
def iIi1i1iiIiiiI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OoO00o0o0oo0o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OoO00o0o0oo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO00o0o0oo0o )
 if 13 - 13: I11O0O0oOO00O00o % ii1ii11IIIiiI . ooOoO0O00
 if 1 - 1: I11i % I11i . iI11I1II1I1I . ii . ooOOOoO . Ii1IIIi1
def IiiI ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIiII1 )
 for url , oOOO00o000o , IIIii1I in IIi1I11I1II :
  if '-dir-' in IIIii1I :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOOO00o000o )
  else :
   iI1I ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' , url , 1006 , oOOO00o000o )
   if 58 - 58: ii / iI11I1II1I1I
def IiIiI11IIII ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 OO000O = ( 'http://afewbitsmore.com/' )
 IIi1I11I1II = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if '[To Parent Directory]' in IIIii1I :
   IIIii1I = 'HOME'
   pass
  elif 'HOME' in IIIii1I :
   pass
  elif '.m3u' in IIIii1I :
   iI1I ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , OO000O + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in IIIii1I :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OO000O + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in IIIii1I :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OO000O + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) , OO000O + url , 1012 , III1iII1I1ii + 'music.png' )
def I1iIIiI ( url ) :
 IIIi1I1IIii1II = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oOOO00o000o , IIIii1I , url in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 OO000O = url
 IIi1I11I1II = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  if '.mp3' in IIIii1I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   iI1I ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '/' , '' ) , OO000O + url , 1011 , III1iII1I1ii + 'music.png' )
def oo000o ( ) :
 IiIiII1 = Iii1iiIi1II ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , oOOO00o000o , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , ( 'http://www.cyn.net/music/' + i1I1ii11i1Iii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOOO00o000o ) . replace ( ' ' , '%20' ) )
def iIIIII ( url , img ) :
 IiIiII1 = Iii1iiIi1II ( url )
 ii1II = url
 img = img
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( ii1II + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def I11i11I1iiII ( url ) :
 IiIiII1 = Iii1iiIi1II ( url )
 ii1II = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IiIiII1 )
 for type , url , IIIii1I in IIi1I11I1II :
  if '[VID]' in type :
   OooOoOo ( ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , ii1II + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   I11i11I1iiII ( ii1II + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: oO0o . OOooOOo % IIiIiII11i - o0o00Oo0O
 if 52 - 52: oO0o
def i11ii ( ) :
 o00oOOo0Oo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IiIi1iIIi1 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oOooOoOO = IiIi1iIIi1 . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ii1II = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1i11iIIi = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 49 - 49: iI1ii11iIi1i . Ii1I % O0OOOoOoo0 . I1ii11iIi11i * O00o0O00
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 O0 = ooOooo000oOO ( ii1II )
 ii1ii1ii = ooOooo000oOO ( I1i11iIIi )
 if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OOOoOoo0
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for IIIii1I in IIi1I11I1II :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( IIIii1I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1ii11i1Iii + IIIii1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 20 - 20: Ii1IIIi1 + I11i . ii1ii11IIIiiI / Ii
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for IIIii1I in OooOoooOo :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( IIIii1I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ii1II + IIIii1I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 7 - 7: OOooOOo / OOooOOo . ii1ii11IIIiiI * o0o00Oo0O + ooOOOoO + oO0oo0o
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  Ooooo = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ii1ii1ii )
  for IIIii1I in Ooooo :
   if IiIi1iIIi1 in IIIii1I . lower ( ) :
    iI1I ( ( IIIii1I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11iIIi + IIIii1I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 98 - 98: IIiIiII11i * ooOOOoO - oOo0O0Ooo % I11i - Ii1IIIi1 % Ii1I
    I1I1i1I ( 'tvshows' , 'Media Info 3' )
    if 69 - 69: ooOoO0O00 % oO0o % ii1ii11IIIiiI / O0OOOoOoo0 / O0OOOoOoo0
    if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0OOOoOoo0
    if 47 - 47: o0o00Oo0O
    if 55 - 55: oO0o % o0o00Oo0O / ii
    if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
    if 88 - 88: Ii1I * Ii1IIIi1 + IIiIiII11i
I1IiiIII = '{SF},' ; i1iIii1II11 = '{IF},' ; OOOOoOOOO = '{PW},' ; oo0O0OoO = '{AM},' ; iiIi1 = '{GF},' ; Oo0OOo = '{DD},' ; I1i1i1IIi1I = '{UO},' ; oo000oo00 = '{LE},' ; IiIiiI1II = '{ZY},' ; iI1i = '{UE},' ; oo000o0O = '{PE},' ; iiIiIIiI1 = '{JE},' ; O00i1i = '{TH},' ; iiii = '{LK},'
if 62 - 62: ii
if 33 - 33: o0o00Oo0O . Ii % I11i
def iiI ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( 'http://www.iwatchseries.me/tv-list/' )
 IIi1I11I1II = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 8021 , III1iII1I1ii + 'iwatch.png' )
def i1I1iii1I11II ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( IiIiII1 )
 for url , IIIii1I , oOOoooO in IIi1I11I1II :
  iI1I ( IIIii1I + oOOoooO , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def IiI1I ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oO0oO0ooOoO0 ( url )
def oO0oO0ooOoO0 ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IiIiII1 )
 OooOoooOo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IiIiII1 )
 Ooooo = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  OooOoOo ( 'VidSpot - ' + IIIii1I , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in OooOoooOo :
  OooOoOo ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for IIIii1I , url in Ooooo :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OooOoOo ( 'TheVideo - ' + IIIii1I , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 10 - 10: Ii % O00o0O00 * Ii1IIIi1 % I1ii11iIi11i
def oO0o0ooooo ( ) :
 IiIiII1 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi1I11I1II = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 1021 , III1iII1I1ii + 'anime.png' )
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + iI1ii11iIi1i . O00o0O00
  if 58 - 58: iI11I1II1I1I + ii1ii11IIIiiI - Ii1I - ooOoO0O00 * OOooOOo
def iii1iII1iii ( ) :
 IiIiII1 = O0i1II1Iiii1I11 ( 'http://www.animetoon.org/cartoon' )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IiIiII1 )
 for i1I1ii11i1Iii , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , i1I1ii11i1Iii , 1002 , III1iII1I1ii + 'anime.png' )
  if 97 - 97: ii1ii11IIIiiI / O00o0O00 - Ii
  if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * O0OOOoOoo0 - I11O0O0oOO00O00o * oO0o
  if 78 - 78: Ii1IIIi1 % Ii + Ii1IIIi1 + I11i
def i1II11III ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( IiIiII1 )
 for oOOO00o000o in OooOoooOo :
  Iiii111 = oOOO00o000o
 Ooooo = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( IiIiII1 )
 for url in Ooooo :
  iI1I ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( IiIiII1 )
 for url , IIIii1I in IIi1I11I1II :
  iI1I ( IIIii1I , url , 1003 , Iiii111 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0OO0oo ( url , IMAGE ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( IiIiII1 )
 for IIIii1I , url in IIi1I11I1II :
  print IIIii1I + '     ' + url
  if 'easy' in url :
   II111IiiIIi ( url )
  elif 'playpanda' in url :
   II111IiiIIi ( url )
   if 66 - 66: ooOoO0O00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II111IiiIIi ( url ) :
 IiIiII1 = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( IiIiII1 )
 for url in IIi1I11I1II :
  OooOoOo ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 91 - 91: I11i / Ii
  if 96 - 96: oO0o + Ii1IIIi1 * IIiIiII11i
def OO00OoO ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0oOOo . add_header ( 'referer' , url )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 6 - 6: O00o0O00 / iI11I1II1I1I / O0OOOoOoo0 / oOo0O0Ooo - ooOoO0O00 - O00o0O00
def Iii1iiIi1II ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 8 - 8: Ii * I11O0O0oOO00O00o . O00o0O00 / O00o0O00
def Iii1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OoOO00 = ( '%s%s' % ( O0O00OoOoOOo , url ) )
 OOO00O = Iii1iiIi1II ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , iI1IIIii , IIIii1I in IIi1I11I1II :
  OooOoOo ( '%s' % ( '[COLOR' + iiI1IiI + ']' + IIIii1I + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iI1IIIii )
  if 31 - 31: o0o00Oo0O - ooOOOoO * Ii * ooOoO0O00
def OO0 ( url ) :
 if 78 - 78: O0OOOoOoo0 * OOooOOo . iI1ii11iIi1i . OOooOOo % iI11I1II1I1I
 o0i111 = open ( o0O , "a" )
 o0i111 . write ( 'url="' + url + '"\n' )
 o0i111 . close
 if 63 - 63: O0OOOoOoo0 % oOo0O0Ooo . O00o0O00 - O0OOOoOoo0 / I1ii11iIi11i % oOo0O0Ooo
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 import urlresolver
 try : iiiI1I . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( IIIii1I ) )
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iiiI1I . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 39 - 39: I11i . ooOoO0O00 % oO0oo0o / I11O0O0oOO00O00o % o0o00Oo0O
def o0O0OOooO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % IIIii1I )
 xbmc . sleep ( 1 )
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 o0oOoO00o . update ( 100 , '%s' % IIIii1I )
 xbmc . sleep ( 1 )
 iiiI1I . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 1 - 1: ii1ii11IIIiiI * oO0o - Ii1IIIi1
def oO00oo0o00o0o ( url ) :
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iiiI1I . play ( url ) . strip ( )
 except : pass
 if 97 - 97: Ii1IIIi1 . Ii1I - iI11I1II1I1I . O0OOOoOoo0 + oOo0O0Ooo % oO0oo0o
def Ii1i1iiiIiIIiIiiii ( url ) :
 iiiI1I = xbmc . Player ( I11i1I1Ii ( ) )
 import urlresolver
 o00O0OooO0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iiiI1I . play ( o00O0OooO0 )
 xbmc . sleep ( 1 )
 iiiI1I . play ( url )
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: ooOOOoO - I11i % O00o0O00 - IIiIiII11i
def I11i1I1Ii ( ) :
 try :
  o0o0OOooo0Oo = getSet ( "core-player" )
  if ( o0o0OOooo0Oo == 'DVDPLAYER' ) : iIiII1iI1Iii1i1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0o0OOooo0Oo == 'MPLAYER' ) : iIiII1iI1Iii1i1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0o0OOooo0Oo == 'PAPLAYER' ) : iIiII1iI1Iii1i1 = xbmc . PLAYER_CORE_PAPLAYER
  else : iIiII1iI1Iii1i1 = xbmc . PLAYER_CORE_AUTO
 except : iIiII1iI1Iii1i1 = xbmc . PLAYER_CORE_AUTO
 return iIiII1iI1Iii1i1
 return True
 if 87 - 87: Ii * IIiIiII11i - iI1ii11iIi1i % ii
def iI1I ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o0oO = [ ]
  if showcontext == 'fav' :
   o0oO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   o0oO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iII . addContextMenuItems ( o0oO )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = True )
 return i1iI1Iiii1I
 if 35 - 35: ii1ii11IIIiiI - ooOoO0O00 / ooOOOoO
def IiIIi11i111 ( name , url , mode , iconimage , fanart , description ) :
 if 13 - 13: OOooOOo - oO0o * ii
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iII . setProperty ( "Fanart_Image" , fanart )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = True )
 return i1iI1Iiii1I
 if 26 - 26: ii
def OooOoOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o0oO = [ ]
  if showcontext == 'fav' :
   o0oO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   o0oO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iII . addContextMenuItems ( o0oO )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = False )
 return i1iI1Iiii1I
 if 65 - 65: O00o0O00
 if 14 - 14: O0OOOoOoo0
 if 75 - 75: iI11I1II1I1I % O0OOOoOoo0 / O00o0O00 - Ii1IIIi1 % Ii
 if 11 - 11: I11O0O0oOO00O00o . iI1ii11iIi1i
 if 87 - 87: O00o0O00 + O00o0O00
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
def ii1 ( heading , announce ) :
 class OO0OoOo00 ( ) :
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
   try : o00O0 = open ( announce ) ; oOiiI1Ii11II1I = o00O0 . read ( )
   except : oOiiI1Ii11II1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( oOiiI1Ii11II1I ) )
   return
 OO0OoOo00 ( )
 OO0OoOo00 ( )
 if 75 - 75: iI11I1II1I1I / IIiIiII11i / iI1ii11iIi1i / OOooOOo
def O0O0OOOOoo ( ) :
 ii1 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 77 - 77: OOooOOo
 if 31 - 31: ooOOOoO / Ii1IIIi1
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: O0OOOoOoo0 + oO0oo0o - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: ooOOOoO
def Ii1i1iI ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 52 - 52: o0o00Oo0O + O0OOOoOoo0
 if 11 - 11: ooOoO0O00 / ii1ii11IIIiiI * Ii1I * ii1ii11IIIiiI * O0OOOoOoo0 - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . iI1ii11iIi1i
 if 26 - 26: oO0oo0o - O0OOOoOoo0 % I1ii11iIi11i - oO0oo0o + ooOOOoO
 if 33 - 33: iI1ii11iIi1i + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * ooOOOoO
 if 21 - 21: o0o00Oo0O * O0OOOoOoo0 % oO0o
 if 14 - 14: o0o00Oo0O / ii1ii11IIIiiI / O0OOOoOoo0 + ooOOOoO - ooOOOoO
 if 10 - 10: o0o00Oo0O - Ii1I / ii1ii11IIIiiI % OOooOOo / ii / iI1ii11iIi1i
 if 73 - 73: O0OOOoOoo0 + ooOOOoO % I11i . Ii1I / O00o0O00 . ii1ii11IIIiiI
 if 76 - 76: I11O0O0oOO00O00o . Ii1I * ii % Ii1IIIi1
 if 24 - 24: ii
 if 83 - 83: o0o00Oo0O / oO0o
 if 62 - 62: I11O0O0oOO00O00o
 if 73 - 73: iI1ii11iIi1i % oO0o * O00o0O00
 if 84 - 84: I1ii11iIi11i
 if 18 - 18: ii
 if 85 - 85: ii . oO0o . oO0o
 if 70 - 70: I11O0O0oOO00O00o
 if 72 - 72: ii1ii11IIIiiI - O0OOOoOoo0 - oOo0O0Ooo - Ii1IIIi1 + O00o0O00 - ooOoO0O00
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: Ii1IIIi1 % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * oO0oo0o + Ii1IIIi1 % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % ooOOOoO . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
def OOo0ooOOOo0O0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + ooI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 4 - 4: Ii1IIIi1 % Ii1I
def ii1II11I11i11 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + ooOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 55 - 55: iI1ii11iIi1i - ii
def ooOoOoOoo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIIIIIiiiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 83 - 83: Ii + oO0oo0o % ooOoO0O00 . ooOOOoO + Ii1I
def OOOoooooO0oOOoO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + I1I1oOoooo0OooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 67 - 67: ii + oO0o / I1ii11iIi11i % I11i % ooOoO0O00
def I1oOO000oOo0O0o ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + OoiiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 92 - 92: I1ii11iIi11i % I11i - O0OOOoOoo0 / O0OOOoOoo0 / OOooOOo
def oo0o0o0o0O ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 11 - 11: Ii1I
def OOOoOOooOoo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + O00OO0oOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 41 - 41: ooOOOoO * ii . O0OOOoOoo0 % Ii
def IiIoO0oo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + IiIiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 14 - 14: oOo0O0Ooo
def i1iIiII1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Oo00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 42 , IiiiiI1i1Iii , O000OOO , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 8 - 8: oO0o + ii1ii11IIIiiI . O00o0O00
def OOI1iI1ii1II ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oO00O0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for IIIii1I , url , IiiiiI1i1Iii , O000OOO , I1Ii in IIi1I11I1II :
  o0OIiII ( IIIii1I , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , I1Ii )
 I1I1i1I ( 'movies' , 'MAIN' )
 if 40 - 40: Ii % iI11I1II1I1I % iI11I1II1I1I
 if 79 - 79: Ii
 if 20 - 20: ooOoO0O00 - ooOOOoO + ooOOOoO . ii . oOo0O0Ooo + I11O0O0oOO00O00o
 if 10 - 10: ooOOOoO / I1ii11iIi11i
 if 82 - 82: Ii1I / Ii1IIIi1 + Ii1I + ii1ii11IIIiiI
 if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / O0OOOoOoo0 % oOo0O0Ooo % ooOoO0O00
 if 87 - 87: I11i % ooOoO0O00 + oO0oo0o - iI11I1II1I1I . O00o0O00 + Ii
 if 83 - 83: Ii1I * IIiIiII11i . ii1ii11IIIiiI - I11O0O0oOO00O00o
 if 46 - 46: oO0o % Ii1I
def OOo0Oo0OOo0 ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( O00o0OO ) :
     OO00O0O = 0
     OO00O0O += len ( iiiiI11ii )
     if OO00O0O > 0 :
      for o00O0 in iiiiI11ii :
       os . unlink ( os . path . join ( Ooo0o0oo0 , o00O0 ) )
  O00oOo0OOO = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( O00oOo0OOO )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 15 - 15: iI1ii11iIi1i / Ii1I * ooOOOoO % O0OOOoOoo0
 if 90 - 90: Ii1IIIi1
 if 81 - 81: iI1ii11iIi1i % oO0o
 if 57 - 57: oO0oo0o . Ii1I . oO0oo0o . oO0o + oO0oo0o * ii
 if 22 - 22: ooOoO0O00 * oOo0O0Ooo - ii1ii11IIIiiI - O00o0O00
 if 90 - 90: Ii1I - Ii1IIIi1 . Ii / oOo0O0Ooo
 if 41 - 41: ii1ii11IIIiiI * oO0o - Ii1IIIi1 . iI1ii11iIi1i
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - oO0oo0o + ii1ii11IIIiiI
def iIIooO0o0O0Oo ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 22 - 22: o0o00Oo0O % ooOOOoO % Ii1IIIi1 % oOo0O0Ooo
def ooO0oOOooOo0 ( url ) :
 I11i11i111i1 = os . path . join ( oO , 'addon_data' )
 II1I1i1I = [
 ( I11i11i111i1 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I11i11i111i1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I11i11i111i1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 21 - 21: ii
 Oo0OoOoOo0o = 0
 if 41 - 41: ii - Ii1I
 for iiiiIiIi in II1I1i1I :
  if os . path . exists ( iiiiIiIi ) and not iiiiIiIi in [ oOo0oooo00o , I11i11i111i1 ] :
   for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( iiiiIiIi ) :
    OO00O0O = 0
    OO00O0O += len ( iiiiI11ii )
    if OO00O0O > 0 :
     for o00O0 in iiiiI11ii :
      if not o00O0 in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( Ooo0o0oo0 , o00O0 ) )
       except :
        pass
      else : Ii1I1Ii ( 'Ignore Log File: %s' % o00O0 )
     for o00o in I111I11I111 :
      try :
       shutil . rmtree ( os . path . join ( Ooo0o0oo0 , o00o ) )
       Oo0OoOoOo0o += 1
       Ii1I1Ii ( "[Success] cleared %s files from %s" % ( str ( OO00O0O ) , os . path . join ( iiiiIiIi , o00o ) ) )
      except :
       Ii1I1Ii ( "[Failed] to wipe cache in: %s" % os . path . join ( iiiiIiIi , o00o ) )
  else :
   for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( iiiiIiIi ) :
    for o00o in I111I11I111 :
     if 'cache' in o00o . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Ooo0o0oo0 , o00o ) )
       Oo0OoOoOo0o += 1
       Ii1I1Ii ( "[Success] wiped %s " % os . path . join ( iiiiIiIi , o00o ) )
      except :
       Ii1I1Ii ( "[Failed] to wipe cache in: %s" % os . path . join ( iiiiIiIi , o00o ) )
       if 45 - 45: I11O0O0oOO00O00o . IIiIiII11i / Ii
 iIIooO0o0O0Oo ( oo0o0O00 , 'Clear Cache: Removed %s Files' % Oo0OoOoOo0o )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
 if 41 - 41: Ii1I % Ii1I + ooOOOoO . Ii1IIIi1 % ii1ii11IIIiiI * O0OOOoOoo0
 if 57 - 57: iI1ii11iIi1i . ii1ii11IIIiiI . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: O0OOOoOoo0 / O00o0O00 * o0o00Oo0O
 if 17 - 17: oO0o / O0OOOoOoo0 % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def IiiiI1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OOo0iIiiI11II11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( OOo0iIiiI11II11 ) :
   OO00O0O = 0
   OO00O0O += len ( iiiiI11ii )
   if 75 - 75: ii1ii11IIIiiI - Ii1IIIi1 . oO0oo0o
   if 88 - 88: Ii1IIIi1 - ii . O0OOOoOoo0 - I11i / OOooOOo % I11O0O0oOO00O00o
   if OO00O0O > 0 :
    if 61 - 61: Ii1IIIi1 + ooOOOoO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( OO00O0O ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: ii * oOo0O0Ooo % ooOoO0O00 . O0OOOoOoo0 % iI1ii11iIi1i . Ii1I
     for o00O0 in iiiiI11ii :
      os . unlink ( os . path . join ( Ooo0o0oo0 , o00O0 ) )
     for o00o in I111I11I111 :
      shutil . rmtree ( os . path . join ( Ooo0o0oo0 , o00o ) )
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
 if 72 - 72: O0OOOoOoo0 % I11O0O0oOO00O00o + oO0o
 if 94 - 94: iI1ii11iIi1i + iI11I1II1I1I
 if 80 - 80: I11i . Ii1IIIi1 . ii
 if 63 - 63: O0OOOoOoo0 . O00o0O00
 if 66 - 66: oOo0O0Ooo
 if 99 - 99: oO0o % o0o00Oo0O . ii1ii11IIIiiI - Ii1I . I1ii11iIi11i / OOooOOo
 if 60 - 60: Ii1I
 if 78 - 78: oO0oo0o + IIiIiII11i
 if 55 - 55: ii
def OO0I111i1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OOo0iIiiI11II11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( OOo0iIiiI11II11 ) :
   OO00O0O = 0
   OO00O0O += len ( iiiiI11ii )
   if 90 - 90: oOo0O0Ooo
   if 4 - 4: O00o0O00 % O0OOOoOoo0 - O00o0O00 - I11i
   if OO00O0O > 0 :
    if 30 - 30: ooOOOoO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( OO00O0O ) + " files found" , "Do you want to delete them?" ) :
     if 34 - 34: oO0oo0o - IIiIiII11i - I11i + Ii1IIIi1 + ii1ii11IIIiiI
     for o00O0 in iiiiI11ii :
      os . unlink ( os . path . join ( Ooo0o0oo0 , o00O0 ) )
     for o00o in I111I11I111 :
      shutil . rmtree ( os . path . join ( Ooo0o0oo0 , o00o ) )
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
 ooO0oOOooOo0 ( url )
 return
 if 70 - 70: ii + oO0o * I1ii11iIi11i
 if 20 - 20: Ii - IIiIiII11i - O0OOOoOoo0 % oO0oo0o . O0OOOoOoo0
 if 50 - 50: iI11I1II1I1I + ii1ii11IIIiiI - I11O0O0oOO00O00o - ii
 if 84 - 84: OOooOOo - I11O0O0oOO00O00o
 if 80 - 80: Ii % O00o0O00 - I1ii11iIi11i % O00o0O00
 if 89 - 89: iI1ii11iIi1i * I11O0O0oOO00O00o + OOooOOo / Ii
 if 68 - 68: ii * I11O0O0oOO00O00o
 if 86 - 86: I11i / OOooOOo
 if 40 - 40: Ii1IIIi1
 if 62 - 62: O0OOOoOoo0 / O00o0O00
def O0o0O0OoOo0 ( url , name ) :
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 Ii11i1IiII = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml.bak' )
 if os . path . exists ( Ii11i1IiII ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml' )
   try :
    os . remove ( o00o0O0o0o0 )
    print '=== GenieTv - REMOVING    ' + str ( o00o0O0o0o0 ) + '    ==='
   except :
    pass
   OOO00O = ii11iIi1I . http_GET ( url ) . content
   I11I1IIiiII1 = open ( o00o0O0o0o0 , "w" )
   I11I1IIiiII1 . write ( OOO00O )
   I11I1IIiiII1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o00o0O0o0o0 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml' )
  try :
   os . remove ( o00o0O0o0o0 )
   print '=== GenieTv - REMOVING    ' + str ( o00o0O0o0o0 ) + '    ==='
  except :
   pass
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I11I1IIiiII1 = open ( o00o0O0o0o0 , "w" )
  I11I1IIiiII1 . write ( OOO00O )
  I11I1IIiiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00o0O0o0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 96 - 96: Ii - OOooOOo / Ii1IIIi1 % ii / iI11I1II1I1I - O00o0O00
def OoOOoO0Ooo0oo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml' )
 try :
  I11I1IIiiII1 = open ( o00o0O0o0o0 ) . read ( )
  if 'zero' in I11I1IIiiII1 :
   name = '0CACHE'
  elif 'tuxen' in I11I1IIiiII1 :
   name = 'TUXENS'
  elif 'muckys' in I11I1IIiiII1 :
   name = 'MUCKYS'
  elif 'p2p1' in I11I1IIiiII1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in I11I1IIiiII1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in I11I1IIiiII1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 33 - 33: oOo0O0Ooo / I11O0O0oOO00O00o . I1ii11iIi11i
def O0OoO0o ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'advancedsettings.xml' )
 try :
  os . remove ( o00o0O0o0o0 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o00o0O0o0o0 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 96 - 96: O00o0O00 * oO0oo0o
 if 11 - 11: Ii % OOooOOo + ii1ii11IIIiiI - Ii1I . o0o00Oo0O + I11O0O0oOO00O00o
 if 14 - 14: iI11I1II1I1I / I11i * ooOOOoO
 if 35 - 35: iI11I1II1I1I
 if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
 if 75 - 75: oOo0O0Ooo - O0OOOoOoo0 - oOo0O0Ooo % oO0oo0o % ii
 if 13 - 13: O0OOOoOoo0 * oO0o % iI11I1II1I1I / ooOOOoO * Ii1IIIi1 . I1ii11iIi11i
 if 23 - 23: O0OOOoOoo0 / ooOOOoO . Ii1IIIi1 * iI1ii11iIi1i
 if 87 - 87: Ii
def OOOo0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi1I11I1II = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for iIIi , iIII1II11iII , IiiII1iIi , OoO00oooo0o in IIi1I11I1II :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iIIi , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IiiII1iIi , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OoO00oooo0o )
  inc = inc + 1
  if 31 - 31: I1ii11iIi11i
  if 1 - 1: ooOoO0O00
  if 27 - 27: I11O0O0oOO00O00o
  if 47 - 47: ii
  if 48 - 48: OOooOOo . ooOOOoO % oOo0O0Ooo + I11O0O0oOO00O00o
  if 37 - 37: I1ii11iIi11i + ii1ii11IIIiiI * oO0oo0o / I11i
  if 78 - 78: ooOOOoO + I11O0O0oOO00O00o - I11i + oO0o / iI11I1II1I1I
  if 47 - 47: O00o0O00
  if 20 - 20: ii1ii11IIIiiI % O0OOOoOoo0 - ii1ii11IIIiiI * ii / Ii1I
def O0000OOOoO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'addons2.ini' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I11I1IIiiII1 = open ( o00o0O0o0o0 , "w" )
  I11I1IIiiII1 . write ( OOO00O )
  I11I1IIiiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00o0O0o0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 24 - 24: O00o0O00
def o0oOoOOO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  O0o0O0OO00o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o00o0O0o0o0 = os . path . join ( O0o0O0OO00o , 'settings.xml' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I11I1IIiiII1 = open ( o00o0O0o0o0 , "w" )
  I11I1IIiiII1 . write ( OOO00O )
  I11I1IIiiII1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00o0O0o0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 74 - 74: Ii1IIIi1 / ii1ii11IIIiiI / IIiIiII11i - Ii1IIIi1 / oO0oo0o % I11O0O0oOO00O00o
 if 19 - 19: ooOOOoO % ii + ii
def i1II ( ) :
 try :
  i1iII1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( i1iII1i ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Ii1I11Ii1iI = os . path . join ( i1iII1i , "source.db" )
    os . unlink ( Ii1I11Ii1iI )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 61 - 61: I11i * Ii1I - ooOoO0O00 + I11O0O0oOO00O00o % I11i + ii
 if 64 - 64: Ii1IIIi1 . O0OOOoOoo0 % iI1ii11iIi1i
 if 21 - 21: ii1ii11IIIiiI / oO0oo0o
 if 82 - 82: iI11I1II1I1I - Ii1IIIi1 . ooOoO0O00 . ooOOOoO % Ii * iI11I1II1I1I
 if 58 - 58: Ii1I % Ii + OOooOOo / I11O0O0oOO00O00o - ii
def O0i1II1Iiii1I11 ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 62 - 62: oO0o . OOooOOo
 if 22 - 22: O0OOOoOoo0 . Ii . ii . ooOoO0O00
 if 12 - 12: OOooOOo % O00o0O00 + oO0oo0o . o0o00Oo0O % iI11I1II1I1I
 if 41 - 41: ii
 if 13 - 13: I11O0O0oOO00O00o + ii1ii11IIIiiI - ii1ii11IIIiiI % oO0oo0o / I11O0O0oOO00O00o
 if 4 - 4: oOo0O0Ooo + O00o0O00 - ooOOOoO + Ii1IIIi1
 if 78 - 78: iI1ii11iIi1i
def I11I11 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i11Ii = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i11Ii :
  i1iii1I1I = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; i1iii1I1I = xbmc . translatePath ( i1iii1I1I ) ;
  Oo0O0o0Oo0Oo = os . path . join ( i1iii1I1I , ".." , ".." ) ; Oo0O0o0Oo0Oo = os . path . abspath ( Oo0O0o0Oo0Oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + Oo0O0o0Oo0Oo ) ; IiIii1ii1 = False
  try :
   for Ooo0o0oo0 , I111I11I111 , iiiiI11ii in os . walk ( Oo0O0o0Oo0Oo , topdown = True ) :
    I111I11I111 [ : ] = [ o00o for o00o in I111I11I111 if o00o not in o0oO0 ]
    for IIIii1I in iiiiI11ii :
     try : os . remove ( os . path . join ( Ooo0o0oo0 , IIIii1I ) )
     except :
      if IIIii1I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiIii1ii1 = True
      plugintools . log ( "Error removing " + Ooo0o0oo0 + " " + IIIii1I )
    for IIIii1I in I111I11I111 :
     try : os . rmdir ( os . path . join ( Ooo0o0oo0 , IIIii1I ) )
     except :
      if IIIii1I not in [ "Database" , "userdata" ] : IiIii1ii1 = True
      plugintools . log ( "Error removing " + Ooo0o0oo0 + " " + IIIii1I )
   if not IiIii1ii1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iiiii1ii1 ( )
 if 89 - 89: O0OOOoOoo0 . oO0o * ii + OOooOOo / o0o00Oo0O
 if 60 - 60: I11O0O0oOO00O00o
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
def Oo000O ( ) :
 IiiI1 = [ ]
 iII1iiI11IIi = sys . argv [ 2 ]
 if len ( iII1iiI11IIi ) >= 2 :
  o000O0O = sys . argv [ 2 ]
  i1i = o000O0O . replace ( '?' , '' )
  if ( o000O0O [ len ( o000O0O ) - 1 ] == '/' ) :
   o000O0O = o000O0O [ 0 : len ( o000O0O ) - 2 ]
  i11Iii11 = i1i . split ( '&' )
  IiiI1 = { }
  for o0O0ooooooo00 in range ( len ( i11Iii11 ) ) :
   o0ooOO = { }
   o0ooOO = i11Iii11 [ o0O0ooooooo00 ] . split ( '=' )
   if ( len ( o0ooOO ) ) == 2 :
    IiiI1 [ o0ooOO [ 0 ] ] = o0ooOO [ 1 ]
    if 52 - 52: oO0o % Ii . O0OOOoOoo0 % OOooOOo % ii
 return IiiI1
 if 5 - 5: OOooOOo / o0o00Oo0O / Ii
ooo0o0oO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OO0OO0O = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIIIiiii = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
IiI11IiII1iI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iIii1Ooo0oO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OOo0OOooO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
ooI1 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oOoooOOO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ooOo0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iIIIIIiiiII = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1I1oOoooo0OooO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OoiiI1I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o0Ooo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O00OO0oOOO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IiIiI1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
Oo00OO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
I1i111IiIiIi1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1Iiii1i1iI = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i111i1i = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ooOo0O0o0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iII = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo00IiI1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oO00O0OO = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O0O00OoOoOOo = base64 . decodestring ( 'Q1VOVA==' )
def o0OIiII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO = [ ]
  if showcontext == 'fav' :
   o0oO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   o0oO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1iII . addContextMenuItems ( o0oO )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = True )
 return i1iI1Iiii1I
 if 51 - 51: Ii1IIIi1 / ii1ii11IIIiiI % oO0oo0o + oO0oo0o * oO0oo0o
def ii1iII1II ( name , url , mode , iconimage , fanart , description ) :
 Ooo000O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1iI1Iiii1I = True
 I1iII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iII . setProperty ( "Fanart_Image" , fanart )
 i1iI1Iiii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooo000O00 , listitem = I1iII , isFolder = False )
 return i1iI1Iiii1I
 if 20 - 20: Ii1IIIi1 % Ii1I + oO0o / I1ii11iIi11i
 if 10 - 10: Ii / OOooOOo
o000O0O = Oo000O ( )
i1I1ii11i1Iii = None
IIIii1I = None
OooO0Oo0 = None
IiiiiI1i1Iii = None
O000OOO = None
I1Ii = None
iii1OO00Oo00o = None
if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . O00o0O00
if 3 - 3: o0o00Oo0O - ii1ii11IIIiiI * iI1ii11iIi1i * O00o0O00 / iI1ii11iIi1i
try :
 iii1OO00Oo00o = int ( o000O0O [ "fav_mode" ] )
except :
 pass
 if 58 - 58: iI1ii11iIi1i * iI11I1II1I1I + O0OOOoOoo0 . O0OOOoOoo0
try :
 i1I1ii11i1Iii = urllib . unquote_plus ( o000O0O [ "url" ] )
except :
 pass
try :
 IIIii1I = urllib . unquote_plus ( o000O0O [ "name" ] )
except :
 pass
try :
 IiiiiI1i1Iii = urllib . unquote_plus ( o000O0O [ "iconimage" ] )
except :
 pass
try :
 OooO0Oo0 = int ( o000O0O [ "mode" ] )
except :
 pass
try :
 O000OOO = urllib . unquote_plus ( o000O0O [ "fanart" ] )
except :
 pass
try :
 I1Ii = urllib . unquote_plus ( o000O0O [ "description" ] )
except :
 pass
 if 74 - 74: O0OOOoOoo0 - I11i * ooOOOoO % O0OOOoOoo0
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * ii1ii11IIIiiI - oO0o - I11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OooO0Oo0 )
print "URL: " + str ( i1I1ii11i1Iii )
print "Name: " + str ( IIIii1I )
print "IconImage: " + str ( IiiiiI1i1Iii )
if 44 - 44: ii
if 82 - 82: OOooOOo . OOooOOo
def I1I1i1I ( content , viewType ) :
 if 10 - 10: I1ii11iIi11i * Ii1I . oO0oo0o . ii . O00o0O00 * Ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 80 - 80: ii1ii11IIIiiI + I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00
if IiiiiI1i1Iii == None : IiiiiI1i1Iii = Ooo
if O000OOO == None : O000OOO = OO0o
if OooO0Oo0 == None :
 I11IiI ( )
 if 85 - 85: Ii . I11O0O0oOO00O00o + iI1ii11iIi1i / iI1ii11iIi1i
elif OooO0Oo0 == 1 :
 Iiii1iiiIiI1 ( i1I1ii11i1Iii )
 if 43 - 43: ooOOOoO . ii - IIiIiII11i
elif OooO0Oo0 == 44 :
 I1i1i1iii ( i1I1ii11i1Iii )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O00o0O00 * oO0oo0o
elif OooO0Oo0 == 2 :
 oOo0O ( )
 if 19 - 19: ii1ii11IIIiiI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OooO0Oo0 == 3 :
 ii1IiIi11 ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OooO0Oo0 == 21 :
 i1i1II ( )
 if 15 - 15: iI1ii11iIi1i + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OooO0Oo0 == 4 :
 ii1iI1II11ii ( )
 if 54 - 54: ooOOOoO - IIiIiII11i . O0OOOoOoo0 + iI1ii11iIi1i
elif OooO0Oo0 == 5 :
 OO0o0oO0O000o ( i1I1ii11i1Iii )
 if 45 - 45: oO0oo0o + IIiIiII11i . Ii1IIIi1 / Ii1I
elif OooO0Oo0 == 6 :
 IiiiI1 ( i1I1ii11i1Iii )
 if 76 - 76: iI1ii11iIi1i + Ii1IIIi1 - ooOOOoO * iI11I1II1I1I % ooOoO0O00
elif OooO0Oo0 == 7 :
 O0o0O0OoOo0 ( i1I1ii11i1Iii , IIIii1I )
 if 72 - 72: O0OOOoOoo0 + IIiIiII11i . o0o00Oo0O - Ii1IIIi1 / ii . ii1ii11IIIiiI
elif OooO0Oo0 == 8 :
 OoOOoO0Ooo0oo ( i1I1ii11i1Iii , IIIii1I )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OooO0Oo0 == 9 :
 FIXREPOSADDONS ( i1I1ii11i1Iii )
 if 32 - 32: ii
elif OooO0Oo0 == 10 :
 Ii1i1iI ( )
 if 29 - 29: Ii1I
elif OooO0Oo0 == 11 :
 O0OoO0o ( i1I1ii11i1Iii )
 if 41 - 41: iI1ii11iIi1i
elif OooO0Oo0 == 12 :
 OOOo0 ( )
 if 49 - 49: iI1ii11iIi1i % IIiIiII11i . iI1ii11iIi1i - I11i - I11O0O0oOO00O00o * ooOOOoO
elif OooO0Oo0 == 13 :
 OOo0Oo0OOo0 ( )
 if 47 - 47: o0o00Oo0O . I11i / iI1ii11iIi1i * Ii1IIIi1
elif OooO0Oo0 == 14 :
 ooO0oOOooOo0 ( i1I1ii11i1Iii )
 if 63 - 63: ii1ii11IIIiiI - oO0oo0o - Ii1IIIi1 - O0OOOoOoo0 / oO0oo0o + oO0o
elif OooO0Oo0 == 15 :
 III1ii ( )
 if 94 - 94: ooOOOoO / oOo0O0Ooo . IIiIiII11i
elif OooO0Oo0 == 16 :
 O0000OOOoO ( i1I1ii11i1Iii , IIIii1I )
 if 32 - 32: oO0oo0o . O00o0O00 % O00o0O00 . OOooOOo
elif OooO0Oo0 == 17 :
 o0oOoOOO ( i1I1ii11i1Iii , IIIii1I )
 if 37 - 37: O00o0O00 + o0o00Oo0O + O00o0O00 . Ii1IIIi1 . I11i
elif OooO0Oo0 == 18 :
 i1II ( )
 if 78 - 78: oOo0O0Ooo / I11O0O0oOO00O00o + I11i . I1ii11iIi11i / o0o00Oo0O
elif OooO0Oo0 == 19 :
 iI1IiiiI11 ( i1I1ii11i1Iii )
 if 49 - 49: Ii1I
elif OooO0Oo0 == 40 :
 o0OoOoOOoOo0o ( IIIii1I , i1I1ii11i1Iii , I1Ii )
 if 66 - 66: I11i . Ii1I
elif OooO0Oo0 == 42 :
 oOII1ii1ii11I1 ( IIIii1I , i1I1ii11i1Iii , I1Ii )
 if 18 - 18: I1ii11iIi11i + ooOOOoO
elif OooO0Oo0 == 43 :
 I1IiI1iI11 ( i1I1ii11i1Iii )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % iI1ii11iIi1i . oOo0O0Ooo
elif OooO0Oo0 == 20 :
 oOOo0oo0o0o0 ( i1I1ii11i1Iii )
 if 43 - 43: oOo0O0Ooo % Ii1I * iI1ii11iIi1i
elif OooO0Oo0 == 22 :
 OOo0ooOOOo0O0 ( i1I1ii11i1Iii )
 if 31 - 31: iI1ii11iIi1i / Ii1IIIi1
elif OooO0Oo0 == 23 :
 ii1II11I11i11 ( i1I1ii11i1Iii )
 if 3 - 3: ooOOOoO
elif OooO0Oo0 == 24 :
 ooOoOoOoo ( i1I1ii11i1Iii )
 if 37 - 37: iI1ii11iIi1i * ii * I11O0O0oOO00O00o + I1ii11iIi11i . oOo0O0Ooo
elif OooO0Oo0 == 25 :
 OOOoooooO0oOOoO ( i1I1ii11i1Iii )
 if 61 - 61: O00o0O00 . O00o0O00
elif OooO0Oo0 == 26 :
 I1oOO000oOo0O0o ( i1I1ii11i1Iii )
 if 17 - 17: IIiIiII11i / O0OOOoOoo0
elif OooO0Oo0 == 27 :
 oo0o0o0o0O ( i1I1ii11i1Iii )
 if 80 - 80: O00o0O00 * oO0o + iI1ii11iIi1i
elif OooO0Oo0 == 28 :
 OOOoOOooOoo ( i1I1ii11i1Iii )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif OooO0Oo0 == 29 :
 IiIoO0oo0 ( i1I1ii11i1Iii )
 if 98 - 98: I11i * I1ii11iIi11i - iI1ii11iIi1i . O0OOOoOoo0
elif OooO0Oo0 == 30 :
 OO0Oooo0oo ( i1I1ii11i1Iii )
 if 2 - 2: I1ii11iIi11i - O0OOOoOoo0 % iI11I1II1I1I
elif OooO0Oo0 == 31 :
 i1iIiII1 ( i1I1ii11i1Iii )
 if 88 - 88: ii1ii11IIIiiI - oO0o
elif OooO0Oo0 == 32 :
 Ii1I1i ( )
 if 79 - 79: Ii1IIIi1
elif OooO0Oo0 == 33 :
 III1iii1i11iI ( )
 if 45 - 45: IIiIiII11i + Ii1IIIi1 . I11O0O0oOO00O00o . o0o00Oo0O * ooOoO0O00 - iI1ii11iIi1i
elif OooO0Oo0 == 35 :
 ii1iI111 ( i1I1ii11i1Iii )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif OooO0Oo0 == 34 :
 OoO ( i1I1ii11i1Iii )
 if 76 - 76: Ii1I
elif OooO0Oo0 == 36 :
 ii1iIIiii1 ( i1I1ii11i1Iii )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . iI1ii11iIi1i
elif OooO0Oo0 == 37 :
 IiII1iiI ( i1I1ii11i1Iii )
 if 51 - 51: iI1ii11iIi1i + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OooO0Oo0 == 38 :
 O0oOoo0OoO0O ( i1I1ii11i1Iii )
 if 20 - 20: ii1ii11IIIiiI . I11O0O0oOO00O00o . iI1ii11iIi1i + I11O0O0oOO00O00o - O00o0O00 * oO0oo0o
elif OooO0Oo0 == 41 :
 I11I11 ( o000O0O )
 if 82 - 82: oO0o
elif OooO0Oo0 == 39 :
 OOI1iI1ii1II ( i1I1ii11i1Iii )
 if 78 - 78: IIiIiII11i / I11O0O0oOO00O00o - Ii + Ii1I * I1ii11iIi11i
elif OooO0Oo0 == 45 :
 TEXTS ( )
 if 17 - 17: OOooOOo
elif OooO0Oo0 == 46 :
 O0O0OOOOoo ( )
 if 72 - 72: Ii1IIIi1 . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OooO0Oo0 == 47 :
 GEVID ( )
 if 64 - 64: oO0oo0o
elif OooO0Oo0 == 48 :
 OOiI1 ( IIIii1I , i1I1ii11i1Iii , I1Ii )
 if 80 - 80: I11i % iI11I1II1I1I
elif OooO0Oo0 == 49 :
 OO0O0 ( )
 if 63 - 63: ooOOOoO * Ii
elif OooO0Oo0 == 222 :
 OO0 ( i1I1ii11i1Iii )
 if 86 - 86: I11O0O0oOO00O00o % I11O0O0oOO00O00o - OOooOOo + ii1ii11IIIiiI / oOo0O0Ooo * ii
elif OooO0Oo0 == 333 :
 Iii1 ( i1I1ii11i1Iii )
 if 26 - 26: IIiIiII11i * Ii1IIIi1 + I11i / o0o00Oo0O + ooOoO0O00 - I11O0O0oOO00O00o
 if 56 - 56: O00o0O00
elif OooO0Oo0 == 1020 :
 oO0o0ooooo ( )
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + ooOOOoO - I11O0O0oOO00O00o
elif OooO0Oo0 == 1021 :
 ANIMEEP ( )
 if 81 - 81: Ii1I + ii - O00o0O00 * o0o00Oo0O
elif OooO0Oo0 == 1022 :
 ANIMEPLAY ( i1I1ii11i1Iii )
 if 100 - 100: iI11I1II1I1I - OOooOOo
elif OooO0Oo0 == 1001 :
 iii1iII1iii ( )
 if 28 - 28: I1ii11iIi11i . o0o00Oo0O . I11O0O0oOO00O00o
elif OooO0Oo0 == 1005 :
 I1IIII1 ( )
 if 60 - 60: IIiIiII11i + ii1ii11IIIiiI / oO0oo0o % ii - ooOoO0O00
elif OooO0Oo0 == 1007 :
 ooO0O ( i1I1ii11i1Iii )
 if 57 - 57: O0OOOoOoo0
elif OooO0Oo0 == 1010 :
 IiiI ( i1I1ii11i1Iii )
 if 99 - 99: I1ii11iIi11i + ii1ii11IIIiiI % O0OOOoOoo0 - I11i
elif OooO0Oo0 == 1011 :
 o00OooooOOOO ( i1I1ii11i1Iii )
 if 52 - 52: Ii1I
elif OooO0Oo0 == 1012 :
 IiIiI11IIII ( i1I1ii11i1Iii )
 if 93 - 93: Ii1IIIi1 . Ii
elif OooO0Oo0 == 1030 :
 oo000o ( )
 if 24 - 24: O00o0O00 . oO0o + ii1ii11IIIiiI . oO0oo0o - Ii1I % Ii1IIIi1
elif OooO0Oo0 == 1031 :
 iIIIII ( i1I1ii11i1Iii , IiiiiI1i1Iii )
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / iI1ii11iIi1i
elif OooO0Oo0 == 1032 :
 I11i11I1iiII ( i1I1ii11i1Iii )
 if 29 - 29: Ii1I / oO0oo0o * o0o00Oo0O - Ii - oO0o + iI1ii11iIi1i
elif OooO0Oo0 == 1006 :
 Parse . ParseURL ( i1I1ii11i1Iii )
 if 86 - 86: oOo0O0Ooo / Ii1I * iI1ii11iIi1i % Ii
elif OooO0Oo0 == 2030 :
 Parse . addonParseURL ( i1I1ii11i1Iii )
 if 20 - 20: Ii1IIIi1 . ii + Ii1IIIi1 + O0OOOoOoo0 * Ii1I
elif OooO0Oo0 == 2031 :
 Parse . apkParseURL ( i1I1ii11i1Iii )
 if 44 - 44: Ii
elif OooO0Oo0 == 1002 :
 i1II11III ( i1I1ii11i1Iii )
 if 69 - 69: O00o0O00 * o0o00Oo0O + Ii
elif OooO0Oo0 == 1003 :
 O0OO0oo ( i1I1ii11i1Iii , IiiiiI1i1Iii )
 if 65 - 65: o0o00Oo0O / Ii1IIIi1 . ooOoO0O00 * Ii1IIIi1 / iI11I1II1I1I - oO0oo0o
elif OooO0Oo0 == 1004 :
 II111IiiIIi ( i1I1ii11i1Iii )
 if 93 - 93: OOooOOo % Ii - iI1ii11iIi1i % oO0o
elif OooO0Oo0 == 1008 :
 OOoo00O0oo ( )
 if 55 - 55: I11i . Ii1I
elif OooO0Oo0 == 1009 :
 iIIIii111 ( i1I1ii11i1Iii )
 if 63 - 63: oO0oo0o
elif OooO0Oo0 == 2001 :
 i1Ii1iiIIi1 ( )
 if 79 - 79: Ii1I - oO0oo0o - I11i . O00o0O00
elif OooO0Oo0 == 2002 :
 I1iIIiI ( i1I1ii11i1Iii )
 if 65 - 65: Ii . oO0o % Ii1IIIi1 + ooOOOoO - Ii
elif OooO0Oo0 == 1013 :
 IIIi11IiIiii ( )
elif OooO0Oo0 == 10111113 :
 OoOO0OOoo ( i1I1ii11i1Iii )
 if 60 - 60: ii1ii11IIIiiI
elif OooO0Oo0 == 1014 :
 II1III ( )
 if 14 - 14: I1ii11iIi11i % oO0oo0o * Ii1IIIi1 - Ii / Ii1I * Ii
elif OooO0Oo0 == 1015 :
 II11iiIIiI11I ( i1I1ii11i1Iii )
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * I11O0O0oOO00O00o + O00o0O00
elif OooO0Oo0 == 1016 :
 i11i1 ( i1I1ii11i1Iii , IiiiiI1i1Iii , IIIii1I )
 if 14 - 14: iI1ii11iIi1i - o0o00Oo0O
elif OooO0Oo0 == 1017 :
 OOOO0OOO ( )
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
elif OooO0Oo0 == 1018 :
 Oo0oooO0oO ( i1I1ii11i1Iii )
 if 45 - 45: ii1ii11IIIiiI * I11O0O0oOO00O00o / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
elif OooO0Oo0 == 1023 :
 O00Ooo ( )
 if 49 - 49: iI1ii11iIi1i / Ii1IIIi1 . Ii1IIIi1 . Ii1IIIi1 + Ii % I11O0O0oOO00O00o
elif OooO0Oo0 == 1024 :
 o00oo00 ( i1I1ii11i1Iii )
 if 7 - 7: ooOOOoO * O0OOOoOoo0 + OOooOOo
elif OooO0Oo0 == 1025 :
 o0oO0O ( i1I1ii11i1Iii )
 if 22 - 22: Ii1IIIi1
elif OooO0Oo0 == 4001 :
 IIo0o0O0O00oOOo ( )
 if 48 - 48: Ii1I . oOo0O0Ooo
elif OooO0Oo0 == 4002 :
 Oo0OO ( )
 if 73 - 73: o0o00Oo0O . ii1ii11IIIiiI - ii % I11O0O0oOO00O00o % ooOoO0O00
elif OooO0Oo0 == 4003 :
 OOooO0o ( )
 if 14 - 14: ii1ii11IIIiiI + iI1ii11iIi1i * I1ii11iIi11i
elif OooO0Oo0 == 4004 :
 oOoO ( )
 if 49 - 49: I1ii11iIi11i
elif OooO0Oo0 == 4005 :
 oOoO00O0 ( )
 if 57 - 57: o0o00Oo0O * O0OOOoOoo0 - Ii1IIIi1 - iI11I1II1I1I * Ii1IIIi1
elif OooO0Oo0 == 4006 :
 Iiii1iI1i ( )
 if 9 - 9: ooOOOoO . I11O0O0oOO00O00o
elif OooO0Oo0 == 4007 :
 oOOOOoOO0o ( )
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
elif OooO0Oo0 == 4008 :
 oo00oO0o ( )
 if 96 - 96: O0OOOoOoo0 % o0o00Oo0O
elif OooO0Oo0 == 4009 : iI1i11 ( )
elif OooO0Oo0 == 4010 : O00OO0oO ( )
elif OooO0Oo0 == 3000 :
 Oo0ooooO0o00 ( )
 if 51 - 51: oOo0O0Ooo - Ii1IIIi1 / Ii1I . Ii1I + Ii1I
elif OooO0Oo0 == 3001 :
 OOOoOOO0o0ooo ( )
 if 87 - 87: IIiIiII11i . iI1ii11iIi1i * oO0o
elif OooO0Oo0 == 3002 :
 II1ii1iii1ii ( i1I1ii11i1Iii )
 if 74 - 74: I11i % OOooOOo . Ii1IIIi1 % ii1ii11IIIiiI . o0o00Oo0O % IIiIiII11i
elif OooO0Oo0 == 3003 :
 I11iIiI1 ( i1I1ii11i1Iii )
 if 5 - 5: oO0oo0o - ii / OOooOOo
elif OooO0Oo0 == 3004 :
 IiIIIIi ( i1I1ii11i1Iii )
 if 30 - 30: I11O0O0oOO00O00o % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
elif OooO0Oo0 == 404 :
 iIi1i1iiIiiiI ( IIIii1I , i1I1ii11i1Iii , IiiiiI1i1Iii )
 if 55 - 55: oO0o
elif OooO0Oo0 == 405 :
 o0O0OOooO ( i1I1ii11i1Iii )
 if 20 - 20: O0OOOoOoo0 * ii1ii11IIIiiI * I11i - O0OOOoOoo0
elif OooO0Oo0 == 7030 :
 Iii11I1i ( )
 if 32 - 32: iI1ii11iIi1i * oO0oo0o
elif OooO0Oo0 == 7021 :
 o0o0oo0OOo0O0 ( IIIii1I )
 if 85 - 85: Ii . oO0o + oO0o
elif OooO0Oo0 == 7022 :
 Oo0O ( IIIii1I )
 if 28 - 28: I1ii11iIi11i
elif OooO0Oo0 == 7000 :
 Iii1i11 ( IIIii1I , i1I1ii11i1Iii , img )
 if 62 - 62: I1ii11iIi11i + ii / Ii1IIIi1
elif OooO0Oo0 == 7050 :
 iIi1IIiI ( i1I1ii11i1Iii )
 if 60 - 60: iI1ii11iIi1i / OOooOOo . I11O0O0oOO00O00o % O00o0O00
elif OooO0Oo0 == 7051 :
 ii1iI11IiIIi ( i1I1ii11i1Iii )
 if 61 - 61: o0o00Oo0O . iI1ii11iIi1i . o0o00Oo0O * Ii * IIiIiII11i / ii1ii11IIIiiI
elif OooO0Oo0 == 7052 :
 oO0OO00 ( i1I1ii11i1Iii )
 if 69 - 69: I11O0O0oOO00O00o
elif OooO0Oo0 == 7053 :
 IiiIO0oooooO ( i1I1ii11i1Iii )
 if 17 - 17: I11O0O0oOO00O00o
elif OooO0Oo0 == 7054 :
 CoolPlay ( i1I1ii11i1Iii )
 if 38 - 38: ii1ii11IIIiiI % O00o0O00
elif OooO0Oo0 == 7060 :
 iI1I1 ( )
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
elif OooO0Oo0 == 7061 :
 ii1I1IIii11 ( i1I1ii11i1Iii )
 if 44 - 44: Ii1I % ooOOOoO
elif OooO0Oo0 == 7063 :
 I1IiIIiIiI ( i1I1ii11i1Iii )
 if 6 - 6: oO0o
elif OooO0Oo0 == 7062 :
 iI ( i1I1ii11i1Iii )
 if 82 - 82: iI11I1II1I1I . I11O0O0oOO00O00o / ooOOOoO / O00o0O00 * IIiIiII11i % oO0oo0o
elif OooO0Oo0 == 7064 :
 NATatozcat ( )
 if 62 - 62: IIiIiII11i
elif OooO0Oo0 == 7067 :
 OOO0O00 ( i1I1ii11i1Iii )
 if 96 - 96: I11O0O0oOO00O00o % OOooOOo * Ii1I
elif OooO0Oo0 == 7066 :
 NATatozA ( i1I1ii11i1Iii )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . O0OOOoOoo0
elif OooO0Oo0 == 7065 :
 Oo0O000OoO00 ( i1I1ii11i1Iii )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . ooOOOoO * I11i + O00o0O00
elif OooO0Oo0 == 7070 :
 O0IIi1i ( )
 if 77 - 77: I11i
elif OooO0Oo0 == 7071 :
 DIZIlist ( i1I1ii11i1Iii )
 if 63 - 63: O0OOOoOoo0 * oO0oo0o + O0OOOoOoo0 * iI1ii11iIi1i + I1ii11iIi11i / Ii1I
elif OooO0Oo0 == 7072 :
 DIZIpull ( i1I1ii11i1Iii )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
elif OooO0Oo0 == 7073 :
 WATCHDIZI ( i1I1ii11i1Iii )
 if 65 - 65: ii1ii11IIIiiI + o0o00Oo0O % I11i
elif OooO0Oo0 == 7002 :
 iiiI1I1iiiII ( )
 if 72 - 72: O00o0O00 . OOooOOo / IIiIiII11i
elif OooO0Oo0 == 7003 :
 ooOOooo0o000O ( i1I1ii11i1Iii )
 if 69 - 69: O00o0O00 * IIiIiII11i - O0OOOoOoo0 - ooOoO0O00 + Ii
elif OooO0Oo0 == 7004 :
 iIIiII11iI1 ( i1I1ii11i1Iii )
 if 50 - 50: ii * ooOoO0O00 / oO0oo0o
elif OooO0Oo0 == 7020 :
 II1I1Ii11 ( i1I1ii11i1Iii )
 if 83 - 83: ooOoO0O00
elif OooO0Oo0 == 7001 :
 OOoooO00o0oo0 ( )
 if 38 - 38: ii * iI11I1II1I1I
elif OooO0Oo0 == 7010 :
 O0III1Iiii1i11 ( i1I1ii11i1Iii )
 if 54 - 54: ii . ii1ii11IIIiiI
elif OooO0Oo0 == 7011 :
 I1Iii11111I1iii ( i1I1ii11i1Iii )
 if 71 - 71: iI1ii11iIi1i
elif OooO0Oo0 == 7012 :
 oo0o ( i1I1ii11i1Iii )
 if 31 - 31: I11O0O0oOO00O00o . Ii . oO0o * I1ii11iIi11i % iI1ii11iIi1i . I11i
elif OooO0Oo0 == 7013 :
 cnfTVPlay2 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IIIii1I , i1I1ii11i1Iii , IiiiiI1i1Iii )
elif OooO0Oo0 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OooO0Oo0 == 7018 :
 i1iIIIiI ( )
elif OooO0Oo0 == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1I1ii11i1Iii )
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
elif OooO0Oo0 == 8000 :
 i111IiIi1 ( )
elif OooO0Oo0 == 8001 :
 O0oOoo00Oo0O ( )
elif OooO0Oo0 == 8002 :
 IIIi1iiIIiiiI ( )
elif OooO0Oo0 == 8003 :
 OOO00000O ( )
elif OooO0Oo0 == 8004 :
 oOo ( )
elif OooO0Oo0 == 8005 :
 OOoooIIII ( )
elif OooO0Oo0 == 8006 :
 oOOo0OOoOO0 ( IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 8030 :
 O00 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8045 :
 iIiII1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8046 :
 i111iii1I1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8047 :
 oOIIIi11 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8048 :
 ooooooo00oO0OO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8049 :
 IIIii11 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 804900 :
 i1i11I1I1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8020 :
 iiI ( )
elif OooO0Oo0 == 8021 :
 i1I1iii1I11II ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8022 :
 IiI1I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8023 :
 oO0oO0ooOoO0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8040 :
 I11iIiI1I1i11 ( )
elif OooO0Oo0 == 8041 :
 i1I1i1i1I1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8042 :
 OooOo0o0OO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8043 :
 yt . PlayVideo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8044 :
 iiI1ii1IIiI ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8060 :
 I11iiiiI1i ( )
elif OooO0Oo0 == 8061 :
 iI1IIii1IiI1iI1I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8064 :
 oOIIiIi ( )
elif OooO0Oo0 == 8065 :
 II1IIii1I11I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8070 :
 I11iIIi ( )
elif OooO0Oo0 == 8071 :
 I111Ii11i11I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7080 :
 i11I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8090 :
 o00O ( )
elif OooO0Oo0 == 8091 :
 IIIIIiiI ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8092 :
 O0o00 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8093 :
 i1iIii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8081 :
 o0OOoO ( )
elif OooO0Oo0 == 8062 :
 o0Oo0oO00Oooo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8063 :
 iI1i11i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8050 :
 I11o0000o0Oo ( )
elif OooO0Oo0 == 8051 :
 ooo0O0OOo0OoO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8052 :
 Ii1i1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8085 :
 IIIIIiiI11i1 ( )
elif OooO0Oo0 == 8086 :
 I11i1I11iIii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8087 :
 OOOii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 8088 :
 Iii1I11 ( i1I1ii11i1Iii , IIIii1I )
elif OooO0Oo0 == 9000 :
 i1I11iIII1i1I ( )
elif OooO0Oo0 == 1111 :
 i11ii ( )
elif OooO0Oo0 == 9001 :
 II1i11I ( )
elif OooO0Oo0 == 9002 :
 II1I1Ii ( )
elif OooO0Oo0 == 9003 :
 I1IIIIII1 ( )
elif OooO0Oo0 == 9004 :
 World1 ( )
elif OooO0Oo0 == 9005 :
 World2 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9006 :
 World3 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9007 :
 i1IiiI11iIiiI11I ( )
elif OooO0Oo0 == 9008 :
 O0oo0ooO00 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9009 :
 oOoO0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9010 :
 IIi1iI ( )
elif OooO0Oo0 == 9011 :
 I1111iIIiIIII ( i1I1ii11i1Iii )
elif OooO0Oo0 == 50 :
 I11iiIIiI1ii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9020 :
 champlist ( )
elif OooO0Oo0 == 9021 :
 O0ooO ( )
elif OooO0Oo0 == 9022 :
 Iii1iIIIi11I1 ( )
elif OooO0Oo0 == 9023 :
 IIII11Ii1I11I ( )
elif OooO0Oo0 == 9024 :
 oo0o0000 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9030 :
 oo00OOo0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9031 :
 OOO0OOoOOO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9032 :
 oOoO0o0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9033 :
 O00O000oOO0oO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 9034 :
 O00O ( )
elif OooO0Oo0 == 7085 :
 O0o0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7086 :
 I1111i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 7087 :
 i1iI11ii ( I1Ii )
elif OooO0Oo0 == 9666 :
 OO0I111i1I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10100 : OO0Oo00OO0oo ( )
elif OooO0Oo0 == 101001 : iiiIIiiIi ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10105 : i1oo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10106 : iI1O000OOOo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10104 : IiIII ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10107 : IIi11I1i1I1I ( )
elif OooO0Oo0 == 10103 : Oooo0oOooOO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10108 : OOoo0OOOo0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10107 : IIi11I1i1I1I ( )
elif OooO0Oo0 == 10000 : Origin_Menu ( )
elif OooO0Oo0 == 10001 : O0Oooo ( )
elif OooO0Oo0 == 10002 : OOIi1iI111II1I1 ( )
elif OooO0Oo0 == 10003 : iiii111II ( )
elif OooO0Oo0 == 10004 : iiIi1i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10005 : IIii11I1i1I ( )
elif OooO0Oo0 == 10006 : ooooO0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10007 : I11i1I1ii1i1 ( i1I1ii11i1Iii , IiiiiI1i1Iii )
elif OooO0Oo0 == 10008 : O0oooO0o ( )
elif OooO0Oo0 == 10009 : ooOo0O0 ( )
elif OooO0Oo0 == 10010 : iIIi111IiII1i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10011 : oOo000O00O0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10012 : oO00oo0o00o0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10109 : Ii1i1iiiIiIIiIiiii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10013 : iiiII1i1I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10014 : IiIi ( )
elif OooO0Oo0 == 10015 : III1III11II ( )
elif OooO0Oo0 == 10016 : OOO0O00Oo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10017 : oo00o0 ( )
elif OooO0Oo0 == 10018 : ooO0 ( )
elif OooO0Oo0 == 10019 : oOoOii1IIii ( )
elif OooO0Oo0 == 10020 : iiii1OooO0O0Ooo ( )
elif OooO0Oo0 == 10021 : OOo0oOOOOooOo ( )
elif OooO0Oo0 == 10022 : OOoO0oO00o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10023 : ooO000OO ( IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 10024 : ii1iiIi ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10025 : IIi1IIIi ( )
elif OooO0Oo0 == 10026 : Iii ( )
elif OooO0Oo0 == 10027 : O0OO0ooO00 ( )
elif OooO0Oo0 == 10028 : O000 ( )
elif OooO0Oo0 == 10029 : o0oo0o00ooO00 ( )
elif OooO0Oo0 == 423 : IiIiIi1I11I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 426 : I1oOoO0OOO00O ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10030 : Izle_Films ( )
elif OooO0Oo0 == 10031 : Latest_Izle_Movies ( )
elif OooO0Oo0 == 10032 : Izle_Genres ( )
elif OooO0Oo0 == 10033 : Izle_Pop_Movies ( )
elif OooO0Oo0 == 10034 : Izle_Boxsets ( )
elif OooO0Oo0 == 10035 : Izle_Search ( )
elif OooO0Oo0 == 10036 : Izle_Genres_Movie ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10037 : Izle_Boxset_single ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10038 : Izle_IFRAME ( )
elif OooO0Oo0 == 10039 : Izle_Boxsets_Next ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10040 : Ooo0O0oooo ( )
elif OooO0Oo0 == 10041 : Oo0OO00OO0Oo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10042 : ooIi111iII ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10043 : oOOOO0oo0O0OO ( )
elif OooO0Oo0 == 10044 : o0o00OoO0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10045 : iII11II1II ( IIIii1I )
elif OooO0Oo0 == 10046 : IIi1ii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10047 : iII1IIiiI11II ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10048 : IiIIi11i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10049 : oO0OOO00 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10050 : OoOoO ( )
elif OooO0Oo0 == 10051 : i1O00oo00o000o ( )
elif OooO0Oo0 == 10052 : O0000ooO ( )
elif OooO0Oo0 == 10053 : Addon ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10054 : oo000O0o ( i1I1ii11i1Iii , IIIii1I )
elif OooO0Oo0 == 10055 :
 iiIi ( "addFavorite" )
 try :
  IIIii1I = IIIii1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IIIii1I = IIIii1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oo ( IIIii1I , i1I1ii11i1Iii , IiiiiI1i1Iii , O000OOO , iii1OO00Oo00o )
elif OooO0Oo0 == 10056 :
 iiIi ( "rmFavorite" )
 try :
  IIIii1I = IIIii1I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IIIii1I = IIIii1I . split ( '  - ' ) [ 0 ]
 except :
  pass
 ooOOO00oOOooO ( IIIii1I )
elif OooO0Oo0 == 10057 :
 iiIi ( "getFavorites" )
 IIIIIiI11Ii ( )
elif OooO0Oo0 == 10058 : OoOOoooOO0O ( )
elif OooO0Oo0 == 10059 : Donators_Guide ( )
elif OooO0Oo0 == 10060 : iIIIiIi ( )
elif OooO0Oo0 == 10061 : II1II1 ( )
elif OooO0Oo0 == 10062 : oOOOo ( IIIii1I , i1I1ii11i1Iii , I1Ii )
elif OooO0Oo0 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif OooO0Oo0 == 10064 : I1i ( )
elif OooO0Oo0 == 10065 : OooO0ooo0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10066 : oo0OOo0O ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10068 : IIIIiIiIi1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10069 : OOoOooOoOOOoo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10070 : i1i1ii111 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10071 : Genie_Watch ( )
elif OooO0Oo0 == 10072 : O000OOO0OOo ( )
elif OooO0Oo0 == 10073 : O0Oo00OoOo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10074 : O00oO0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10075 : OOOIiiiii1iI ( IiiiiI1i1Iii , IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 10076 : II111Ii1i1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10077 : Oo0000oOo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10078 : O00oOo00o0o ( )
elif OooO0Oo0 == 10079 : Genie_Watch_Tv_Shows ( )
elif OooO0Oo0 == 10080 : Genie_Watch_Tv_Genre ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10081 : Genie_Watch_TV_PlayRun ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10082 : Genie_Watch_TV_Episodes ( i1I1ii11i1Iii , IiiiiI1i1Iii )
elif OooO0Oo0 == 10083 : Genie_Watch_Tv_Recent ( i1I1ii11i1Iii )
elif OooO0Oo0 == 10084 : oooOoOOO0oo0o ( )
elif OooO0Oo0 == 10085 : IiI111111IIII ( )
elif OooO0Oo0 == 10086 : ooOOO00Ooo ( )
elif OooO0Oo0 == 20000 : Ii1Ii1I ( )
elif OooO0Oo0 == 20001 : o0O00O ( )
elif OooO0Oo0 == 20002 : iiIi1iiI1I ( i1I1ii11i1Iii )
elif OooO0Oo0 == 20003 : IiiIi11Ii1iI1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 20004 : i1I111i1ii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 21004 : o0o0OO0O00o ( )
elif OooO0Oo0 == 21005 : I1II1III1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 21006 : III1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 21007 : Ooo0Oo0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30000 : i11I1 ( )
elif OooO0Oo0 == 30001 : Ii1I11i11I1i ( )
elif OooO0Oo0 == 10012 : Resolve ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30003 : I1ii1 ( )
elif OooO0Oo0 == 30004 : Ii11i1Ii1IIII ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30005 : oooO0oOoo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30006 : O00oOoOOO0ooo ( )
elif OooO0Oo0 == 30007 : i11I1I ( )
elif OooO0Oo0 == 30008 : IIi1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30009 : iIi11i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30010 : OOO0oOO0ooo0 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30011 : iii ( )
elif OooO0Oo0 == 30012 : iii1IIiI ( )
elif OooO0Oo0 == 30013 : Ii1iiII1i ( )
elif OooO0Oo0 == 30014 : iii1i11 ( )
elif OooO0Oo0 == 30015 : o0o ( i1I1ii11i1Iii , IiiiiI1i1Iii , O000OOO )
elif OooO0Oo0 == 30016 : O00OooO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30019 : iiii1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30017 : iiII1IiIi1iI1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30018 : IiI1iI1IiiIi1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30030 : iIIi1 ( )
elif OooO0Oo0 == 30031 : o00oOOO ( )
elif OooO0Oo0 == 30032 : i1II1 ( )
elif OooO0Oo0 == 30033 : o0Ooo0o0Oo ( )
elif OooO0Oo0 == 30034 : oo00ooooOOo00 ( )
elif OooO0Oo0 == 30035 : OooOo000o0o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30036 : iI1I1iII1i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30037 : iiIIii ( i1I1ii11i1Iii )
elif OooO0Oo0 == 30038 : III1i111i ( )
elif OooO0Oo0 == 30039 : OO ( )
elif OooO0Oo0 == 50000 : oOooO0 ( )
elif OooO0Oo0 == 50001 : iIiiIiiIi ( )
elif OooO0Oo0 == 50002 : I11I111i1I1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 50003 : iIi ( I1Ii )
elif OooO0Oo0 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OooO0Oo0 == 60001 : I11oo0ooOO ( )
elif OooO0Oo0 == 60002 : I1II ( IIIii1I )
elif OooO0Oo0 == 60003 : III ( IIIii1I )
elif OooO0Oo0 == 50004 : IiI ( )
elif OooO0Oo0 == 50005 : speedtest . runtest ( i1I1ii11i1Iii )
elif OooO0Oo0 == 70001 : ii1iI1iI1 ( )
elif OooO0Oo0 == 70002 : O00o ( i1I1ii11i1Iii )
elif OooO0Oo0 == 70003 : oO0o00ooO0OoO ( i1I1ii11i1Iii )
elif OooO0Oo0 == 70004 : IIoO00OoOo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 70005 : OoOi111i ( i1I1ii11i1Iii )
elif OooO0Oo0 == 70006 : II1III1i1iiI ( )
elif OooO0Oo0 == 50006 : ii1 ( i1 , i1111 )
elif OooO0Oo0 == 80000 : iiiii1ii1 ( )
elif OooO0Oo0 == 80001 : resolvefilmon ( i1I1ii11i1Iii )
elif OooO0Oo0 == 80002 : OOO0o0OO0OO ( )
elif OooO0Oo0 == 80003 : I1iiIi111I ( IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 80004 : I1iIiI1IiIIII ( IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 80005 : O0o0oO ( )
elif OooO0Oo0 == 80006 : i1OO0oOOoo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 80007 : iIi11i1 ( i1I1ii11i1Iii )
elif OooO0Oo0 == 80008 : IiIIIIIi ( )
elif OooO0Oo0 == 80009 : O00OoO0oo ( )
elif OooO0Oo0 == 80010 : Ii11iI1iI ( i1I1ii11i1Iii )
elif OooO0Oo0 == 80011 : OOo0OOOoOOo ( i1I1ii11i1Iii )
elif OooO0Oo0 == 80012 : i1iiiIIi11II ( )
elif OooO0Oo0 == 90000 : iI1iiIiI ( IIIii1I , i1I1ii11i1Iii )
elif OooO0Oo0 == 90001 : ii1I ( )
elif OooO0Oo0 == 90002 : IiI1iIiIIIii ( )
if 93 - 93: O0OOOoOoo0 % ii1ii11IIIiiI
if 46 - 46: Ii1I * OOooOOo * ooOOOoO * Ii1I . Ii1I
if 43 - 43: O0OOOoOoo0 . ooOoO0O00
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
