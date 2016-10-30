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
IiiIII111iI = "3.2.4"
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
o0O = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
O00oO = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( oo0OooOOo0 ) :
 os . makedirs ( oo0OooOOo0 )
I11i1I1I = oo0OooOOo0 + 'watched.txt'
if not os . path . exists ( I11i1I1I ) :
 open ( I11i1I1I , 'w+' )
oO0Oo = open ( I11i1I1I ) . read ( )
oOOoo0Oo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
o00OO00OoO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
OOOO0OOoO0O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
oO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( I1IIiiIiii ) == True :
 ooOooo000oOO = open ( I1IIiiIiii ) . read ( )
else : ooOooo000oOO = [ ]
Oo0oOOo = oo00 . getSetting ( 'debug' )
if os . path . exists ( O0O ) == False :
 os . makedirs ( O0O )
def Oo0OoO00oOO0o ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = ''
 O0o0O00Oo0o0 = ''
 try :
  OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
  O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
  OOoOO0oo0ooO . close ( )
 except : pass
 if O0o0O00Oo0o0 != '' :
  return O0o0O00Oo0o0
 else :
  O0o0O00Oo0o0 = 'Failed'
  return O0o0O00Oo0o0
  if 87 - 87: O0oOO0 * Oooo0O0oo00oO % oo0oO00 . IIi * iiII11i1I1IIi
IIIIi1i = [ ]
I1 = Oo0OoO00oOO0o ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if I1 != 'Failed' :
 IIIIi1i . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not I1 != 'Failed' :
 iii1i1iiiiIi = Oo0OoO00oOO0o ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if iii1i1iiiiIi != 'Failed' :
  IIIIi1i . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not iii1i1iiiiIi != 'Failed' :
  Iiii = Oo0OoO00oOO0o ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if Iiii != 'Failed' :
   IIIIi1i . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not Iiii != 'Failed' :
   OO0OoO0o00 = Oo0OoO00oOO0o ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if OO0OoO0o00 != 'Failed' :
    IIIIi1i . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
ooOO0O0ooOooO = ( str ( IIIIi1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
oOOOo00O00oOo = ooOO0O0ooOooO + 'GenieArt/NEW/'
if 34 - 34: iIi1i1ii1 + OooOO000 % OOoOoo
if 85 - 85: Ii1I % iiII11i1I1IIi % OOoOoo
def Oo00oo0oO ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIiIi1iI = 'genie tv repo not being installed '
  i1IiiiI1iI ( )
 else :
  i1iIi ( )
  if 68 - 68: Ii % Ii1I + Ii
def i1iIi ( ) :
 if 31 - 31: IIiIiII11i . oOo0O0Ooo
 II1I = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 i1II1Iiii1I11 = open ( oO0 ) . read ( )
 IIII = open ( Ii1iIiII1ii1 ) . read ( )
 if 32 - 32: ii / iI11I1II1I1I - I11i
 o00oooO0Oo = re . compile ( 'version="([^"]*)" provider' ) . findall ( i1II1Iiii1I11 )
 o0O0OOO0Ooo = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( IIII )
 iiIiI = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( II1I )
 I1OOO00O0O = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( II1I )
 for iii in o00oooO0Oo :
  oOooOOOoOo = iii
  for i1Iii1i1I in iiIiI :
   if not i1Iii1i1I == oOooOOOoOo :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    OOoO00 ( )
   if i1Iii1i1I == oOooOOOoOo :
    IiI111111IIII
 for i1Ii in o0O0OOO0Ooo :
  ii111iI1iIi1 = i1Ii
  for OOO in I1OOO00O0O :
   if not OOO == ii111iI1iIi1 :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    i1IiiiI1iI ( )
   if OOO == ii111iI1iIi1 :
    xbmc . sleep ( 100 )
    IiI111111IIII
def oo0OOo0 ( ) :
 Oo00oo0oO ( )
 I11IiI ( )
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1I1ii11i1Iii ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '' , 50006 , oOOOo00O00oOo + 'Contact-Us.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , oOOOo00O00oOo + 'settings.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , oOOOo00O00oOo + 'GenieUpdate.png' , OO0o , '' )
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , OO0o , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , OO0o , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , OO0o , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 32 , oOOOo00O00oOo + 'BuildersToolbox.png' , OO0o , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , str ( ooOO0O0ooOooO ) , 46 , oOOOo00O00oOo + 'SoruceList.png' , OO0o , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , OO0o , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '' , 10050 , oOOOo00O00oOo + 'Addons.png' , OO0o , '' )
  if ii1iII1II ( ) == 'android' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( ooOO0O0ooOooO ) , 30039 , oOOOo00O00oOo + 'APKTools.png' , OO0o , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , str ( ooOO0O0ooOooO ) , 39 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def i1I1ii11i1Iii ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , OO0o , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , OO0o , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , OO0o , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , OO0o , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I1I1i1I ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , '[COLOR' + iiI1IiI + ']GUIDE SKINS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  OOoO00 ( )
 if O0oO0 == 1 :
  oO0O0OO0O ( )
 if O0oO0 == 2 :
  OO ( )
 if O0oO0 == 3 :
  OoOoO ( )
 if O0oO0 == 4 :
  Ii1I1i ( ooO0oOOooOo0 )
 if O0oO0 == 5 :
  iI111I11I1I1 . ok ( i1 , i1111 )
 if O0oO0 == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if O0oO0 == 7 :
  OOI1iI1ii1II ( )
 if O0oO0 == 8 :
  O0O0OOOOoo ( )
def O0O0OOOOoo ( ) :
 ooO0oOOooOo0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( ooO0oOOooOo0 , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o00O0 ( )
def oOO0O00Oo0O0o ( ) :
 ii1 = I1iIIiiIIi1i ( )
 O0O0ooOOO = ii1 . replace ( II , "" )
 if os . path . exists ( ii1 ) or not ii1 == False :
  oOOo0O00o = open ( ii1 , mode = 'r' ) ; iIiIi11 = oOOo0O00o . read ( ) ; oOOo0O00o . close ( )
  OOOiiiiI ( "%s - %s" % ( i1 , O0O0ooOOO ) , iIiIi11 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def O0O0OOOOoo ( ) :
 ooO0oOOooOo0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( ooO0oOOooOo0 , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o00O0 ( )
def oooOo0OOOoo0 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 o00oooO0Oo = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for OO0O000 , iiIiI1i1 in o00oooO0Oo :
  OOOiiiiI ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]  ' + OO0O000 , iiIiI1i1 )
def I1iIIiiIIi1i ( ) :
 oO0O00oOOoooO = False
 if os . path . exists ( os . path . join ( II , 'xbmc.log' ) ) :
  oO0O00oOOoooO = os . path . join ( II , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II , 'kodi.log' ) ) :
  oO0O00oOOoooO = os . path . join ( II , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II , 'spmc.log' ) ) :
  oO0O00oOOoooO = os . path . join ( II , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II , 'tvmc.log' ) ) :
  oO0O00oOOoooO = os . path . join ( II , 'tvmc.log' )
 return oO0O00oOOoooO
 if 46 - 46: oOo0O0Ooo - ii - oo0oO00 * IIiIiII11i
def I1i1I11I ( url ) :
 if url == 'http://' : return False
 try :
  OOO00O = urllib2 . Request ( url )
  OOO00O . add_header ( 'User-Agent' , I1i1iiI1 )
  OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
  OOoOO0oo0ooO . close ( )
 except Exception , OoO000O0Oo :
  return OoO000O0Oo
 return True
 if 63 - 63: iI11I1II1I1I * Ii % iI11I1II1I1I * Ii
def iI1111iiii ( ) :
 O0o0O00Oo0o0 = O0 ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 if len ( o00oooO0Oo ) > 0 :
  for Oo0OO , ooO0oOOooOo0 , O0OooOo0o , iiI11ii1I1 in o00oooO0Oo :
   o0OIiII ( Oo0OO , ooO0oOOooOo0 , 50005 , O0OooOo0o , iiI11ii1I1 , '' )
def Ooo0OOoOoO0 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   oOo0OOoO0 ( )
  if O0oO0 == 1 :
   IIo0Oo0oO0oOO00 ( )
  if O0oO0 == 2 :
   oo00OO0000oO ( I1II1 )
  if O0oO0 == 3 :
   oooO ( ooO0oOOooOo0 )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 26 - 26: IIi % Ii1I
def o00Oo0oooooo ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if II11iiii1Ii == '5knuckleshuffle' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , OO0o , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , OO0o , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , OO0o , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']STREAM CATEGORIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 90002 , oOOOo00O00oOo + 'cats.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , OO0o , '' )
 else :
  if II11iiii1Ii == '5knuckleshuffle' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , OO0o , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , OO0o , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4004 , oOOOo00O00oOo + 'Movies.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4005 , oOOOo00O00oOo + 'TVShows.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4007 , oOOOo00O00oOo + 'Kids.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30032 , oOOOo00O00oOo + 'News.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'GenieTVTutorials.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4008 , oOOOo00O00oOo + 'Hobbies.png' , OO0o , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '' , 10003 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 8040 , oOOOo00O00oOo + 'documentaries.png' , OO0o , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 7001 , oOOOo00O00oOo + 'DiscloseTV.png' , OO0o , '' )
   if 76 - 76: oo0oO00 / Oooo0O0oo00oO . o0o00Oo0O % oOo0O0Ooo . I11i + iIi1i1ii1
   if 71 - 71: OooOO000 . IIiIiII11i
   if 62 - 62: ii . oo0oO00
   if 61 - 61: OOooOOo - Oooo0O0oo00oO - ooOoO0O00
   if 25 - 25: o0o00Oo0O * oo0oO00 + Ii1I . I11i . I11i
   if 58 - 58: oOo0O0Ooo
   if 53 - 53: ooOoO0O00
   if 59 - 59: I11i
   if 81 - 81: OOooOOo - OOooOOo . iiII11i1I1IIi
   if 73 - 73: oo0oO00 % Ii - oOo0O0Ooo
   if 7 - 7: o0o00Oo0O * Ii * IIi + OOoOoo % oO0o - OOoOoo
   if 39 - 39: I1ii11iIi11i * Oooo0O0oo00oO % Oooo0O0oo00oO - ii + I11i - oo0oO00
   if 23 - 23: Ii
   if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + oo0oO00 * iI11I1II1I1I
   if 81 - 81: iIi1i1ii1 % ooOoO0O00 . iI11I1II1I1I
   if 4 - 4: Ii % oO0o % ooOoO0O00 / iIi1i1ii1
   if 6 - 6: iiII11i1I1IIi / oOo0O0Ooo % Oooo0O0oo00oO - oOo0O0Ooo
   if 31 - 31: Oooo0O0oo00oO
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def i1OOO0000oO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  iI1i111I1Ii ( )
 if O0oO0 == 1 :
  i11i1ii1I ( )
 if O0oO0 == 2 :
  o0OO0o0o00o ( )
 if O0oO0 == 3 :
  oOo0 ( )
 if O0oO0 == 4 :
  OOOoOO ( )
 if O0oO0 == 5 :
  I11IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , iIIiiI1II1i11 , Oo0OO )
 if O0oO0 == 6 :
  o0o0 ( )
 if O0oO0 == 7 :
  IIii1111 ( )
 if O0oO0 == 8 :
  I1iI ( )
 if O0oO0 == 9 :
  IIIIiIiIi1 ( )
 if O0oO0 == 10 :
  I11iiiiI1i ( )
  if 40 - 40: Ii1I + ooOoO0O00 * Oooo0O0oo00oO
  if 85 - 85: IIi * I1ii11iIi11i . o0o00Oo0O - Ii
def I11IiI ( ) :
 if not os . path . exists ( o0 ) :
  OOOiiiiI ( 'Change Log 30/10/16 - v3.2.4' , 'G-Tv lists now from G-Tv channels, private list sectioned off. Queue function added to most sections for continuous play or playlists, thanks to Tony allen and danny perry for their hard work.' )
  os . makedirs ( o0 )
  if 18 - 18: IIi + iIi1i1ii1 - o0o00Oo0O
  if 53 - 53: ooOoO0O00
def iI1i111I1Ii ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   Ooo00Oo ( )
  if O0oO0 == 1 :
   oO00Oooo0O0o0 ( ooO0oOOooOo0 )
  if O0oO0 == 2 :
   II1iI1I11I ( )
  if O0oO0 == 3 :
   o0OO0 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0oO0 == 4 :
   IiI11ii1I ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def ooo ( ) :
 Oo00oo0oO ( )
 iiI ( )
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 if 39 - 39: o0o00Oo0O + OooOO000
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , OO0o , '' )
def I11iiiiI1i ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , Ooo , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Ooo , OO0o , '' )
 if 91 - 91: ii - iI11I1II1I1I + OOooOOo / oO0o . OOooOOo + o0o00Oo0O
 if 26 - 26: Ii1I - ii
 if 11 - 11: oOo0O0Ooo * O0oOO0
 if 81 - 81: iiII11i1I1IIi + iIi1i1ii1
 if 98 - 98: oOo0O0Ooo
def i11i1ii1I ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   o00o0 ( )
  if O0oO0 == 1 :
   II1III1I1I1Ii ( )
  if O0oO0 == 2 :
   OOOOoO00o0O ( )
  if O0oO0 == 3 :
   I1I1I1IIi1III ( )
  if O0oO0 == 4 :
   II11IiiIII ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o0OOOo ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   ii1iiIiIII1ii = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   oO0o0oooO0oO = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   IiIiII1 = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   Iii1iiIi1II = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   OO0O00oOo = '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]'
  ii1I = [ ii1iiIiIII1ii , oO0o0oooO0oO , IiIiII1 , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , OO0O00oOo , '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , Iii1iiIi1II ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I11IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 1 :
   I11IIIi ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLm5ldC9yZWFwZXIvbWFpbm1lbnUucGhw' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 2 :
   ii1II ( )
  if O0oO0 == 3 :
   I11IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 4 :
   iI1I ( )
  if O0oO0 == 5 :
   I11IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 6 :
   OooOoOo ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'TheReaper.png' , OO0o , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , OO0o , '' )
  if oo00 . getSetting ( 'Redemption Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']Redemption Streams[/COLOR]' , ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'RedemptionStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , OO0o , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Test[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvdGVzdC5waHA=' ) ) , 1016 , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==' ) ) , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 14 - 14: I11i * Oooo0O0oo00oO + iiII11i1I1IIi + o0o00Oo0O + Ii
def oOoO0 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
def Oo0 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 url = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OOoO )
 for I11i1II , OooiiIi1i in o00oooO0Oo :
  if '[DIR]' in I11i1II :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + OooiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OooiiIi1i , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in OooiiIi1i :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + OooiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OooiiIi1i , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in OooiiIi1i :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + OooiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OooiiIi1i , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 10 - 10: OooOO000 / OOoOoo + Ii / IIi
def iI1I ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 if 74 - 74: Oooo0O0oo00oO + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
def oOOO0oo0 ( url ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for Oo0OO , url , iiIi1iI1iIii , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O in o00oooO0Oo :
  if o00OooO0oo == '123' :
   o00OooO0oo = oOOOo00O00oOo + 'appstreams.png'
  if iiI11ii1I1 == '123' :
   iiI11ii1I1 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IiiiiI ( Oo0OO , url , 100010 , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0OO , url , 100007 , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0OO , url , 100100 , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O )
  elif not 'http' in url :
   i1ii1II1ii ( Oo0OO , url , 100009 , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O , '' )
  else :
   i1ii1II1ii ( Oo0OO , url , 100005 , o00OooO0oo , iiI11ii1I1 , o0o0oOoOO0O , '' )
   if 28 - 28: Ii1I
def O00OoOO0oo0 ( url ) :
 I1 = iIi1i1iIi1iI ( url )
 oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , O0o0OO0000ooo , o0o0oOoOO0O , iiI11ii1I1 , Oo0OO in oOO :
  if O0o0OO0000ooo == '123' :
   O0o0OO0000ooo = oOOOo00O00oOo + 'appstreams.png'
  if iiI11ii1I1 == '123' :
   iiI11ii1I1 = OO0o
  if 'php' in url :
   I1IiiiiI ( Oo0OO , url , 100004 , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0OO , url , 100007 , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0OO , url , 100100 , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  elif not 'http' in url :
   i1ii1II1ii ( Oo0OO , url , 100009 , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O , '' )
  else :
   i1ii1II1ii ( Oo0OO , url , 100005 , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O , '' )
   if 4 - 4: IIi
def OO0oOOoo ( url ) :
 if 52 - 52: I11i % I1ii11iIi11i
 I1 = iIi1i1iIi1iI ( url )
 Oo000ooOOO = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for Ii11i1I11i in Oo000ooOOO :
  o00OooO0oo = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( Ii11i1I11i ) )
  for o00OooO0oo in o00OooO0oo :
   o00OooO0oo = o00OooO0oo
  Oo0OO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( Ii11i1I11i ) )
  for Oo0OO in Oo0OO :
   if 'elete' in Oo0OO :
    pass
   elif 'rivate Vid' in Oo0OO :
    pass
   else :
    Oo0OO = ( Oo0OO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I11i1iIiIIIIIii = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( Ii11i1I11i ) )
  for I11i1iIiIIIIIii in I11i1iIiIIIIIii :
   I11i1iIiIIIIIii = I11i1iIiIIIIIii
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( Ii11i1I11i ) )
  for url in url :
   url = url
  i1ii1II1ii ( '[COLORred]' + str ( I11i1iIiIIIIIii ) + '[/COLOR] : ' + str ( Oo0OO ) , str ( url ) , 100009 , str ( o00OooO0oo ) , OO0o , '' , '' )
  Iii1I1I11iiI1 ( 'movies' , '' )
  if 58 - 58: I11i / iIi1i1ii1 . OOooOOo / ii + OooOO000
  if 86 - 86: oo0oO00 * oOo0O0Ooo + oo0oO00 + IIiIiII11i
  if 8 - 8: OooOO000 - iiII11i1I1IIi / OOoOoo
  if 96 - 96: OOooOOo
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - IIi
def IiiIiI111iI ( iconimage , url , extra ) :
 o00OooO0oo = ' '
 OOo = ' '
 iiI11ii1I1 = ' '
 i1i11I1I1iii1 = ' '
 I1iii11 = iIi1i1iIi1iI ( url )
 o00OooO0oo = re . compile ( '<img src="(.+?)">' ) . findall ( I1iii11 )
 for o00OooO0oo in o00OooO0oo :
  o00OooO0oo = o00OooO0oo
 ooo0O = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I1iii11 )
 for iiI11ii1I1 in ooo0O :
  iiI11ii1I1 = iiI11ii1I1
 o00oooO0Oo = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I1iii11 )
 for url , i1i11I1I1iii1 in o00oooO0Oo :
  i1i11I1I1iii1 = 'S' + ( i1i11I1I1iii1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o0O + url
  iII1iii ( ( i1i11I1I1iii1 ) . replace ( '  ' , '' ) , url , 100101 , o00OooO0oo , iiI11ii1I1 , OOo , '' )
  Iii1I1I11iiI1 ( 'Movies' , 'info' )
  if 12 - 12: Oooo0O0oo00oO
def O0iII1 ( url , name , fanart , extra , iconimage ) :
 IIII1i = extra
 i1i11I1I1iii1 = name
 I1iii11 = iIi1i1iIi1iI ( url )
 o00OooO0oo = iconimage
 o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I1iii11 )
 for url , name , Ii1IIIIi1ii1I in o00oooO0Oo :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o0O + url
  Ii1IIIIi1ii1I = Ii1IIIIi1ii1I
  IiiIiI1Ii1i = name + ' - [COLORred]' + Ii1IIIIi1ii1I + '[/COLOR]'
  iII1iii ( IiiIiI1Ii1i , url , 100102 , o00OooO0oo , fanart , 'Aired : ' + Ii1IIIIi1ii1I , IiiIiI1Ii1i )
  if 22 - 22: iIi1i1ii1 / Ii
def oOOoo ( name , URL , iconimage , fanart ) :
 I1 = iIi1i1iIi1iI ( URL )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , name in o00oooO0Oo :
  for iII1111III1I in O00oO :
   if iII1111III1I in ooO0oOOooOo0 :
    URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
    i1ii1II1ii ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' , '' )
 if len ( o00oooO0Oo ) <= 0 :
  iII1iii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 39 - 39: ooOoO0O00 / iIi1i1ii1
  if 78 - 78: OOoOoo
def O0oOo00o0o00O ( url , name ) :
 OO00 = name
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 o0OOo00OoO = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  iIi1 ( url , OO00 )
 for url in o0O0OOO0Ooo :
  iIi1 ( url , OO00 )
 for url in o0OOo00OoO :
  iIi1 ( url , OO00 )
  if 21 - 21: oo0oO00
def iIi1 ( url , season_name ) :
 if 'daclips.in' in url :
  OoO00 ( url , season_name )
 elif 'filehoot.com' in url :
  OO0Ooooo000Oo ( url , season_name )
 elif 'allmyvideos.net' in url :
  O0oOoo0o000O0 ( url , season_name )
 elif 'vidspot.net' in url :
  o00oO0o0o ( url , season_name )
 elif 'vodlocker' in url :
  oo0O0Ooooooo ( url , season_name )
 elif 'vidto' in url :
  I1IIIiI1I1ii1 ( url , season_name )
  if 30 - 30: o0o00Oo0O * ii
  if 38 - 38: iIi1i1ii1 - Ii1I . OOooOOo - OooOO000 . ii
def I1IIIiI1I1ii1 ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 49 - 49: I11i . iIi1i1ii1 / oO0o + IIiIiII11i
  if 47 - 47: o0o00Oo0O / IIi
def O0oOoo0o000O0 ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 67 - 67: oOo0O0Ooo
def o00oO0o0o ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 55 - 55: Ii1I - iiII11i1I1IIi * I11i + OOooOOo * OOooOOo * o0o00Oo0O
def oo0O0Ooooooo ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oooOooooO0oOO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 91 - 91: OooOO000 - Oooo0O0oo00oO % iI11I1II1I1I - ii % OOoOoo
def OoO00 ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for oooOooooO0oOO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 98 - 98: oO0o . oO0o * O0oOO0 * IIiIiII11i * OooOO000
def OO0Ooooo000Oo ( url , season_name ) :
 I1 = iIi1i1iIi1iI ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oooOooooO0oOO in o00oooO0Oo :
  Iiiiii1iI ( oooOooooO0oOO , season_name )
  if 92 - 92: I1ii11iIi11i
def Iiiiii1iI ( Link , season_name ) :
 if 'http:/' in Link :
  iI11I ( Link )
  if 53 - 53: iI11I1II1I1I + IIi - OooOO000
def OoO ( url ) :
 I1 = OPEN_URL_1 ( url )
 iIIiii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in iIIiii :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 61 - 61: iIi1i1ii1 . ooOoO0O00 / OooOO000 % Ii * iiII11i1I1IIi
def iII1iii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if 60 - 60: Ii1I * oOo0O0Ooo
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 17 - 17: Oooo0O0oo00oO % I1ii11iIi11i / Ii1I . iIi1i1ii1 * Oooo0O0oo00oO - IIiIiII11i
 if 41 - 41: IIi
def i1ii1II1ii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  IiI11i1IIiiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 77 - 77: OooOO000
def Oo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 81 - 81: O0oOO0 * oO0o
def iI11II1IIIiii1 ( url ) :
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O00oo . play ( url ) . strip ( )
 except : pass
 if 4 - 4: ii - ooOoO0O00 % IIi - Oooo0O0oo00oO * I11i
def iI11I ( url ) :
 O00oo = xbmc . Player ( )
 import urlresolver
 try : O00oo . play ( url )
 except : pass
 if 85 - 85: ii * iI11I1II1I1I . iiII11i1I1IIi / ii % oOo0O0Ooo % o0o00Oo0O
def iIi1i1iIi1iI ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = ''
 O0o0O00Oo0o0 = ''
 try :
  OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
  O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
  OOoOO0oo0ooO . close ( )
 except : pass
 if O0o0O00Oo0o0 != '' :
  return O0o0O00Oo0o0
 else :
  O0o0O00Oo0o0 = 'Opened'
  return O0o0O00Oo0o0
  if 36 - 36: IIi / IIiIiII11i / iIi1i1ii1 / iIi1i1ii1 + Ii1I
  if 95 - 95: iIi1i1ii1
  if 51 - 51: IIiIiII11i + iIi1i1ii1 . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def oOo0 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   OOoOoo0 ( )
  if O0oO0 == 1 :
   I1iIII1 ( )
  if O0oO0 == 2 :
   iIii ( )
  if O0oO0 == 3 :
   oOo0OoOOo0 ( )
  if O0oO0 == 4 :
   iII11I1Ii1 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'SearchCartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( ooOO0O0ooOooO ) , 21004 , oOOOo00O00oOo + 'watchcartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , oOOOo00O00oOo + 'Cartoons.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '' , 20000 , oOOOo00O00oOo + 'Cartoons.png' , OO0o , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , oOOOo00O00oOo + 'anime.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o0o0 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , OO0o , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOOo00O00oOo + 'Fitness.png' , OO0o , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Go Fishing[/COLOR]' , str ( ooOO0O0ooOooO ) , 8090 , oOOOo00O00oOo + 'GoFishing.png' , OO0o , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOOo00O00oOo + 'GenieTVKitchen.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 92 - 92: oo0oO00 / oo0oO00 . Ii1I
 if 17 - 17: Ii - IIiIiII11i * I11i
 if 5 - 5: Oooo0O0oo00oO - Oooo0O0oo00oO . I1ii11iIi11i + OOooOOo - Oooo0O0oo00oO . O0oOO0
def IiI111111IIII ( ) :
 I1 = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o00oooO0Oo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiIi1iI in o00oooO0Oo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   IiIi1i1ii = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOOiiiiI ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + IiIi1i1ii + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO0 == 0 :
    iiIi ( IIiIi1iI )
    o00O0 ( )
   elif O0oO0 == 1 :
    oOIi111 ( IIiIi1iI )
  else :
   pass
   if 67 - 67: o0o00Oo0O
def oOIi111 ( addon ) :
 IiIi1i1ii = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 52 - 52: IIiIiII11i . OOoOoo / OOooOOo / ii . Ii
def iiIi ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1i1i = os . path . join ( iIi1ii1I1 , 'default.py' )
 OOOOooO0oO00O0o = open ( I1i1i , "w+" )
 if 70 - 70: OooOO000
 OOOOooO0oO00O0o . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OOOOooO0oO00O0o . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OOOOooO0oO00O0o . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 16 - 16: iiII11i1I1IIi - ii % I1ii11iIi11i
 if 36 - 36: Oooo0O0oo00oO
 if 84 - 84: OooOO000 . oO0o . IIiIiII11i . oo0oO00 / IIi % Ii1I
 if 57 - 57: oOo0O0Ooo % oo0oO00 - Oooo0O0oo00oO . oOo0O0Ooo / I1ii11iIi11i % iiII11i1I1IIi
def II1iI1I11I ( ) :
 I1i11111i1i11 ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O0 ( 'http://www.join4films.com/' )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def OOI1iIi1iiIIiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 80007 , O0o0OO0000ooo )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def oOoOOoOOooOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  url = ( url ) . replace ( ' ' , '%20' )
  I11I ( url )
def iIIII1i ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11I1II = 'http://www.join4films.com/?s=' + ( o00oO0 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OO0 = i11I1II . lower ( )
 OOI1iIi1iiIIiI ( OO0 )
 if 84 - 84: OOooOOo % OOoOoo - OOooOOo . I11i
 if 5 - 5: OOooOOo * OooOO000 - Ii1I / iI11I1II1I1I % O0oOO0 + iIi1i1ii1
 if 51 - 51: OooOO000 * IIiIiII11i % OOoOoo
 if 98 - 98: oO0o . oo0oO00 % IIiIiII11i
 if 71 - 71: OooOO000 % ooOoO0O00 - IIiIiII11i - Oooo0O0oo00oO + Oooo0O0oo00oO * OOoOoo
 if 51 - 51: iI11I1II1I1I / OOooOOo + Oooo0O0oo00oO - oo0oO00 + iiII11i1I1IIi
 if 29 - 29: I11i % iI11I1II1I1I . ii % ii % IIiIiII11i / iiII11i1I1IIi
 if 70 - 70: Ii % iiII11i1I1IIi
 if 11 - 11: iIi1i1ii1 % Ii1I % IIi / IIiIiII11i % OooOO000 - I1ii11iIi11i
 if 96 - 96: Ii1I / IIiIiII11i . IIi - iiII11i1I1IIi * oo0oO00 * O0oOO0
 if 76 - 76: IIi - IIiIiII11i * Oooo0O0oo00oO / ii
 if 18 - 18: oO0o + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
 if 71 - 71: ii
 if 33 - 33: OooOO000
 if 62 - 62: Ii1I + IIi + ooOoO0O00 / ii
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 if 22 - 22: OOoOoo - OOoOoo % Oooo0O0oo00oO . OooOO000 + O0oOO0
def Oo00OOo00O ( ) :
 I1IiiiiI ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 if 81 - 81: iIi1i1ii1 . I11i / OooOO000
def Iii111Ii ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11I1II = 'http://imoviemax.se/?s=' + ( o00oO0 ) . replace ( ' ' , '+' )
 OO0 = i11I1II . lower ( )
 O0O00oOooo0OO ( OO0 )
def iIIi1I ( url ) :
 OO0o0o0oo0O = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , Oo0OO , IIiI1I1 in o00oooO0Oo :
  if Oo0OO in OO0o0o0oo0O :
   pass
  else :
   I1IiiiiI ( Oo0OO + ' - ' + IIiI1I1 + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
   OO0o0o0oo0O . append ( Oo0OO )
   if 15 - 15: IIi * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
def Oo00OOOOoo0oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , O00OOooo0Ooo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + ' - Views:' + O00OOooo0Ooo , url , 10075 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
  if 66 - 66: O0oOO0
  if 91 - 91: O0oOO0 + oOo0O0Ooo
def O0O00oOooo0OO ( url ) :
 OoOooo = [ ]
 I1 = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IiiiiI ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10075 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
  OoOooo . append ( Oo0OO )
  if 74 - 74: iI11I1II1I1I * iIi1i1ii1 % OOooOOo
def iiI11iIi ( img , name , url ) :
 img = img
 name = name
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for oooOO0OO0O , url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o00o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o00o
  III11I = ( oooOO0OO0O ) . replace ( 'play-' , 'Server ' )
  o0OIiII ( III11I , o00o , 10076 , img , img , '' )
  if 17 - 17: ii + Oooo0O0oo00oO * oo0oO00 * OOooOOo
def iiIii1I ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for OooiiIi1i in o00oooO0Oo :
  if '=m' in OooiiIi1i :
   i1I11iIiII ( OooiiIi1i )
  elif 'php' in OooiiIi1i :
   iiIii1I ( url )
  else :
   I1 = O0 ( OooiiIi1i )
   o00oooO0Oo = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for OO0OO0OO in o00oooO0Oo :
    i1I11iIiII ( OooiiIi1i )
    if 61 - 61: ii . O0oOO0 . ii / I1ii11iIi11i
    if 72 - 72: ooOoO0O00
    if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
def oooo0OOo ( url ) :
 I1 = O0 ( url )
 OoO00I11iIi1II = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for Ii1IIIIi1ii1I , ooo0OO in OoO00I11iIi1II :
  print 'there ><><><><><><><><><><><><'
  Ii1IIIIi1ii1I = Ii1IIIIi1ii1I
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooo0OO ) )
  for Oo0OO , iIi1IiI in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + Ii1IIIIi1ii1I + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + iIi1IiI + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
 Ii11i1I11i = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for Ii1IIIIi1ii1I , I11IIIiIi11 in Ii11i1I11i :
  print 'there ><><><><><><><><><><><><'
  Ii1IIIIi1ii1I = Ii1IIIIi1ii1I
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11IIIiIi11 ) )
  for Oo0OO , iIi1IiI in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + Ii1IIIIi1ii1I + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + iIi1IiI + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
   if 39 - 39: IIi % o0o00Oo0O % OOooOOo . ooOoO0O00
   if 86 - 86: oO0o * ii
   if 71 - 71: iI11I1II1I1I - Oooo0O0oo00oO . oOo0O0Ooo % ii + Oooo0O0oo00oO
def II11IiiIII ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for Ii11i1I11i in Ii11i1I11i :
  Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
  for Oo0OO in Oo0OO :
   Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii11i1I11i ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  o00OooO0oo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
  for o00OooO0oo in o00OooO0oo :
   o00OooO0oo = 'http:' + o00OooO0oo
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , '' , '' )
  if 26 - 26: I1ii11iIi11i + Oooo0O0oo00oO / oO0o % OOooOOo % Ii1I + IIiIiII11i
  if 31 - 31: oo0oO00 % Oooo0O0oo00oO * oo0oO00
  if 45 - 45: ooOoO0O00 . oOo0O0Ooo + Oooo0O0oo00oO - ii % OOoOoo
  if 1 - 1: iI11I1II1I1I
def o0OO0 ( url ) :
 if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
 O0O00OOo = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for OooiiIi1i , O0o0OO0000ooo , Oo0OO , OoOOo in o00oooO0Oo :
  Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O0 ( OooiiIi1i )
  o0O0OOO0Ooo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for iIIiii , OOo in o0O0OOO0Ooo :
   iii1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOo ) )
   for o0o0oOoOO0O in iii1 :
    if Oo0OO in O0O00OOo :
     pass
    else :
     o0OIiII ( Oo0OO , iIIiii , 8043 , O0o0OO0000ooo , O0o0OO0000ooo , o0o0oOoOO0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
     O0O00OOo . append ( Oo0OO )
     if 78 - 78: Ii1I + oo0oO00 - o0o00Oo0O
     if 10 - 10: OooOO000 % oOo0O0Ooo
def oo0OoOooo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , iIIiiI1II1i11 , o0o0oOoOO0O , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10065 , iIIiiI1II1i11 , iiI11ii1I1 , o0o0oOoOO0O )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 95 - 95: iIi1i1ii1 * Ii1I % OOoOoo % IIi - IIi
def oOoooO0 ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11I1II = 'https://www.youtube.com/results?search_query=' + ( o00oO0 ) . replace ( ' ' , '+' )
 OO0 = i11I1II . lower ( )
 I1 = O0 ( OO0 )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for ooO0oOOooOo0 in next :
  ooO0oOOooOo0 = 'https://www.youtube.com' + ooO0oOOooOo0
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , ooO0oOOooOo0 , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , o0Oo0 , OOo in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o00OooO0oo
  ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
  o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , OOo )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , o0Oo0 in o00oooO0Oo :
   print 'im doing it'
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
   ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
   if '&' in ooO0oOOooOo0 :
    print ' i got here'
    I1 = O0 ( ooO0oOOooOo0 )
    Ii11i1I11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for Ii11i1I11i in Ii11i1I11i :
     Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
     for Oo0OO in Oo0OO :
      Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     ooO0oOOooOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii11i1I11i ) )
     for ooO0oOOooOo0 in ooO0oOOooOo0 :
      ooO0oOOooOo0 = 'https://www.youtube.com/w' + ooO0oOOooOo0
     o00OooO0oo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
     for o00OooO0oo in o00OooO0oo :
      o00OooO0oo = 'http:' + o00OooO0oo
     o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in ooO0oOOooOo0 or 'elete' in Oo0OO :
    pass
   elif 'hannel' in ooO0oOOooOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooO0oOOooOo0
    I1 = O0 ( ooO0oOOooOo0 )
    i1i1II1i11 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in i1i1II1i11 :
     if 'outube' in ooO0oOOooOo0 or 'list' in ooO0oOOooOo0 :
      pass
     elif 'atch' in ooO0oOOooOo0 :
      ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0o0OO0000ooo , 'http:' + O0o0OO0000ooo , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , '' )
    if 91 - 91: oo0oO00 / ooOoO0O00 * ooOoO0O00
def Ii1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for O0o0OO0000ooo , url , Oo0OO , o0Oo0 , OOo in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o00OooO0oo
  url = 'http://www.youtube.com' + url
  o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , OOo )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , url , Oo0OO , o0Oo0 in o00oooO0Oo :
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O0 ( url )
    Ii11i1I11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for Ii11i1I11i in Ii11i1I11i :
     Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
     for Oo0OO in Oo0OO :
      Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Ii11i1I11i ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o00OooO0oo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Ii11i1I11i ) )
     for o00OooO0oo in o00OooO0oo :
      o00OooO0oo = 'http:' + o00OooO0oo
     o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in Oo0OO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O0 ( url )
    i1i1II1i11 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for O0o0OO0000ooo , url , Oo0OO in i1i1II1i11 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0o0OO0000ooo , 'http:' + O0o0OO0000ooo , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + o0Oo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , '' )
    if 68 - 68: IIi - Ii - O0oOO0 + OOooOOo
    if 99 - 99: OOooOOo * OooOO000 * ooOoO0O00 / o0o00Oo0O - OOooOOo % I11i
def iiI ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  oo00O0ooOo = open ( O000oo0O )
  o00oooO0Oo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( oo00O0ooOo ) )
  for ooOOOOo0 , IiiIi in o00oooO0Oo :
   if ooOOOOo0 == 'needs replacing' or IiiIi == 'needs replacing' :
    iIIi ( )
    if 96 - 96: iiII11i1I1IIi
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if 18 - 18: iiII11i1I1IIi * oo0oO00 - IIi
def II1i1III ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 iIIi ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 34 - 34: OooOO000 - Ii / iI11I1II1I1I
def OOOo ( ) :
 I1IiiiiI ( 'Full List' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'PPV' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Entertainment' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Factual' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Movie Channels' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'US Movie Channels TEST' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Kids' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Music' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'UK Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'International Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'News UK & International' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'German' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'Arabic' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'TV Series Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'VOD Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 I1IiiiiI ( 'VOD Bollywood' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
 if 79 - 79: OOooOOo % iIi1i1ii1 % I1ii11iIi11i
def Ii1I1iiiiii ( name ) :
 o0OO0Oo = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , O0o0OO0000ooo , I11iiii1I , ooO0oOOooOo0 in o00oooO0Oo :
  if o0OO0Oo == 'Full List' :
   ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
   o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
  else :
   o0OO0Oo = ( o0OO0Oo ) . replace ( 'World' , 'القنوات العربية' )
   if o0OO0Oo in I11iiii1I :
    ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
    print ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
   else :
    pass
    if 3 - 3: o0o00Oo0O % ii / Oooo0O0oo00oO
def ooOo ( name ) :
 o0OO0Oo = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , O0o0OO0000ooo , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
  o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
 else :
  o0OIiII ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 84 - 84: Oooo0O0oo00oO
  if 87 - 87: OOoOoo + I11i
  if 28 - 28: Oooo0O0oo00oO * Ii1I / O0oOO0
  if 64 - 64: O0oOO0 - oOo0O0Ooo / iiII11i1I1IIi - oO0o
  if 37 - 37: Ii / iiII11i1I1IIi
  if 85 - 85: Ii + OooOO000 * OOooOOo
  if 1 - 1: ooOoO0O00 / I1ii11iIi11i . oO0o
  if 57 - 57: oo0oO00 . I1ii11iIi11i + IIiIiII11i
  if 43 - 43: OooOO000 % iiII11i1I1IIi
  if 69 - 69: iiII11i1I1IIi % oO0o
  if 86 - 86: O0oOO0 / O0oOO0
  if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
def oOo0OOoO0 ( ) :
 I1IiiiiI ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IiiiiI ( 'Backup Genie Favourites' , ooO0oOOooOo0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( o00OO00OoO ) :
  I1IiiiiI ( 'Backup Ivue Config' , o00OO00OoO , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  I1IiiiiI ( 'Backup Kodi Favourites' , OOOO0OOoO0O0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 72 - 72: ii / oOo0O0Ooo + IIi / OOooOOo * IIi
  if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + iiII11i1I1IIi * iI11I1II1I1I % IIi
  if 25 - 25: oo0oO00 + OOooOOo . I11i % OOooOOo * Oooo0O0oo00oO
zip = oo00 . getSetting ( 'zip' )
ii1IiIi11 = xbmc . translatePath ( os . path . join ( zip ) )
def iiiii1ii1 ( ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: o0o00Oo0O + o0o00Oo0O . OooOO000 - OOoOoo
  if 63 - 63: O0oOO0
  if 71 - 71: ooOoO0O00 . IIi * iiII11i1I1IIi % ii + Oooo0O0oo00oO
def iIIi1iiI1i11 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O0Oo000ooO00
  elif 'Ivue' in name :
   url = o00OO00OoO
  elif 'Kodi' in name :
   url = OOOO0OOoO0O0
  iiiii1ii1 ( )
  oooiIii11i1I = open ( url ) . read ( )
  oOOOoOoO = os . path . join ( ii1IiIi11 , description . split ( 'Your ' ) [ 1 ] )
  oOOo0O00o = open ( oOOOoOoO , mode = 'w' )
  oOOo0O00o . write ( oooiIii11i1I )
  oOOo0O00o . close ( )
 else :
  if 'guisettings.xml' in description :
   I1i = open ( os . path . join ( ii1IiIi11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1II1iII = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   o00oooO0Oo = re . compile ( i1II1iII ) . findall ( I1i )
   for type , II1i , o0OO00oo in o00oooO0Oo :
    o0OO00oo = o0OO00oo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , II1i , o0OO00oo ) )
  else :
   oOOOoOoO = os . path . join ( url )
   oooiIii11i1I = open ( os . path . join ( ii1IiIi11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0O00o = open ( oOOOoOoO , mode = 'w' )
   oOOo0O00o . write ( oooiIii11i1I )
   oOOo0O00o . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 8 - 8: OOoOoo * o0o00Oo0O
 if 73 - 73: I11i / O0oOO0 / oo0oO00 / oO0o
 if 11 - 11: OOooOOo + iIi1i1ii1 - ii / oO0o
 if 34 - 34: OOoOoo
def i1iI1 ( ) :
 IIi11i1II = 1
 iiiii1ii1 ( )
 OO0ooo0o0 = xbmc . translatePath ( os . path . join ( ii1IiIi11 , 'Build Backup' , 'Full Backup' , '' ) )
 oO0ooOoO = xbmc . translatePath ( os . path . join ( ii1IiIi11 , 'Build Backup' , 'my_full_backup.zip' ) )
 ooO0000o00O = xbmc . translatePath ( os . path . join ( ii1IiIi11 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( OO0ooo0o0 ) :
  os . makedirs ( OO0ooo0o0 )
 O0Ooo = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not O0Ooo ) : return False , 0
 oO00oOOo0Oo = O0Ooo
 IIiIIIIii = xbmc . translatePath ( os . path . join ( OO0ooo0o0 , oO00oOOo0Oo + '.zip' ) )
 iI = [ 'plugin.video.GenieTv' ]
 iI1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iIIiI1ii = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oo0OOoOoo0O0O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iiI11ii1111 = "Creating full backup of existing build"
 IIiIIiI = "Creating Community Build"
 ooOOooo0Oo = "Archiving..."
 oo0O0o = ""
 OO0oIiII1iiI = "Please Wait"
 iII ( I11 , IIiIIIIii , IIiIIiI , ooOOooo0Oo , oo0O0o , OO0oIiII1iiI , iIIiI1ii , oo0OOoOoo0O0O )
 time . sleep ( 1 )
 oO0O000oOoo0O = xbmc . translatePath ( os . path . join ( OO0ooo0o0 , oO00oOOo0Oo + '_guisettings.zip' ) )
 iIIiii11iIiiI = zipfile . ZipFile ( oO0O000oOoo0O , mode = 'w' )
 try :
  iIIiii11iIiiI . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iIIiii11iIiiI . close ( )
 if IIi11i1II == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oO0ooOoO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IIiIIIIii + '[/COLOR]' )
  if 81 - 81: oo0oO00 / iI11I1II1I1I - OOoOoo * OooOO000 . oOo0O0Ooo * Ii1I
def iII ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0000 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 i111i1i = len ( sourcefile )
 IiIii1I1I = [ ]
 OO0Oooo0oo = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for I1i111IiIiIi1 , i1II11II1 , II1IIIii in os . walk ( sourcefile ) :
  for file in II1IIIii :
   OO0Oooo0oo . append ( file )
 iIIIiIi1I1i = len ( OO0Oooo0oo )
 for I1i111IiIiIi1 , i1II11II1 , II1IIIii in os . walk ( sourcefile ) :
  i1II11II1 [ : ] = [ OoOOoO0oOo for OoOOoO0oOo in i1II11II1 if OoOOoO0oOo not in exclude_dirs ]
  II1IIIii [ : ] = [ oOOo0O00o for oOOo0O00o in II1IIIii if oOOo0O00o not in exclude_files ]
  for file in II1IIIii :
   IiIii1I1I . append ( file )
   O0ooOOOO0O0 = len ( IiIii1I1I ) / float ( iIIIiIi1I1i ) * 100
   o0oOoO00o . update ( int ( O0ooOOOO0O0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   i1IIi1i1Ii1 = os . path . join ( I1i111IiIiIi1 , file )
   if not 'temp' in i1II11II1 :
    if not 'plugin.program.originwizard' in i1II11II1 :
     import time
     Iii = '01/01/1980'
     o0Oo0oO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1IIi1i1Ii1 ) ) )
     if o0Oo0oO > Iii :
      o0000 . write ( i1IIi1i1Ii1 , i1IIi1i1Ii1 [ i111i1i : ] )
 o0000 . close ( )
 o0oOoO00o . close ( )
 if 48 - 48: O0oOO0 . I11i / O0oOO0
 if 56 - 56: iI11I1II1I1I . Ii - Oooo0O0oo00oO * IIiIiII11i * OooOO000
def OooOoOo ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 if 5 - 5: Oooo0O0oo00oO / Oooo0O0oo00oO - Ii1I
 if 79 - 79: Ii1I + OooOO000
def iIiIIi ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ooo00Oo ( )
 if O0oO0 == 1 :
  o00o0 ( )
 if O0oO0 == 2 :
  OOoOoo0 ( )
 if O0oO0 == 3 :
  oOoooO0 ( )
  if 14 - 14: I11i / Oooo0O0oo00oO - iI11I1II1I1I - O0oOO0 % OOoOoo
  if 49 - 49: OOoOoo * O0oOO0 / I11i / I1ii11iIi11i * iI11I1II1I1I
  if 57 - 57: OOooOOo - O0oOO0 / OOoOoo % Ii
  if 3 - 3: iiII11i1I1IIi . OOoOoo % oOo0O0Ooo + Ii1I
  if 64 - 64: ooOoO0O00
  if 29 - 29: I11i / Ii / oOo0O0Ooo % O0oOO0 % Ii
  if 18 - 18: Oooo0O0oo00oO + OooOO000
  if 80 - 80: O0oOO0 + I11i * IIi + oO0o
  if 75 - 75: oo0oO00 / I11i / Oooo0O0oo00oO / iIi1i1ii1 % OOoOoo + IIiIiII11i
def I1III111i ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I11IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if O0oO0 == 2 :
   iiI1iii ( )
  if O0oO0 == 3 :
   OOoOOo00O0o0 ( )
  if O0oO0 == 4 :
   Oo0O0Oo00O ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO0 == 5 :
   iIoo0ooooO ( )
  if O0oO0 == 6 :
   iiIIi ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO0 == 7 :
   i1i ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO0 == 8 :
   iIIiI1iiI ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO0 == 9 :
   I11Ii111I ( )
  if O0oO0 == 10 :
   Oo00OO0 ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'Rays-Ravers.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , oOOOo00O00oOo + 'Quicksilver.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , oOOOo00O00oOo + 'RadioNomy.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30031 , oOOOo00O00oOo + 'MusicChannels.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , oOOOo00O00oOo + 'UKRadio.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( ooOO0O0ooOooO ) , 1013 , oOOOo00O00oOo + 'WorldRadio.png' , OO0o , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , oOOOo00O00oOo + 'Concerts.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1030 , oOOOo00O00oOo + 'MUSIC.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , oOOOo00O00oOo + 'MusicVideos.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOOo00O00oOo + 'Music.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 1111 , oOOOo00O00oOo + 'MusicSearch.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , OO0o , '' )
  if 72 - 72: ooOoO0O00 / O0oOO0 * OooOO000
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 40 - 40: IIi - OOooOOo * OOooOOo . OOooOOo + ii
def Oo0o0OOOOO0O ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I1I1IiIi1 ( )
  if O0oO0 == 1 :
   iI1111iiii ( )
  if O0oO0 == 2 :
   oOO0O00Oo0O0o ( )
  if O0oO0 == 3 :
   O0ooO0Oo00o ( ooO0oOOooOo0 )
  if O0oO0 == 4 :
   oOO0o0oo0 ( ooO0oOOooOo0 )
  if O0oO0 == 5 :
   o00O0 ( )
  if O0oO0 == 6 :
   oOo000O ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO0 == 7 :
   iIIooO0o0O0Oo ( )
 else :
  o0OIiII ( 'CLLEANUP' , 'url' , 9666 , oOOOo00O00oOo + 'MAIN5.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , oOOOo00O00oOo + 'KillKodi.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , oOOOo00O00oOo + 'Speedtest.png' , OO0o , '' )
  o0OIiII ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , oOOOo00O00oOo + 'View-Log-File.png' , OO0o , '' )
  o0OIiII ( 'DELETE CACHE' , 'url' , 14 , oOOOo00O00oOo + 'DeleteCache.png' , OO0o , '' )
  o0OIiII ( 'DELETE PACKAGES' , 'url' , 6 , oOOOo00O00oOo + 'DeletePackages.png' , OO0o , '' )
  o0OIiII ( 'FORCE REFRESH' , 'url' , 10 , oOOOo00O00oOo + 'ForceRefresh.png' , OO0o , 'Force Refresh All Repos' )
  I1IiiiiI ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , oOOOo00O00oOo + '1.jpg' , OO0o , 'Fix Corrupt Database' )
  o0OIiII ( 'CHECK MY IP' , 'url' , 12 , oOOOo00O00oOo + 'CheckMyIP.png' , OO0o , '' )
  o0OIiII ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOOo00O00oOo + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , OO0o , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 1 - 1: iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - iiII11i1I1IIi % iIi1i1ii1 + iIi1i1ii1
  if 24 - 24: oOo0O0Ooo + I1ii11iIi11i + Oooo0O0oo00oO - ii + I1ii11iIi11i
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 93 - 93: OOoOoo . iI11I1II1I1I % Ii . OOooOOo % OOoOoo + o0o00Oo0O
 if 65 - 65: IIi + oO0o - ii
def i1i1II ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOOo00O00oOo + 'repos.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEW[/COLOR]' , str ( ooOO0O0ooOooO ) , 22 , oOOOo00O00oOo + 'NEW.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']IPTV[/COLOR]' , str ( ooOO0O0ooOooO ) , 23 , oOOOo00O00oOo + 'IPTV.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']VIDEO[/COLOR]' , str ( ooOO0O0ooOooO ) , 24 , oOOOo00O00oOo + 'VIDEO.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SPORTS[/COLOR]' , str ( ooOO0O0ooOooO ) , 25 , oOOOo00O00oOo + 'SPORTS.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 26 , oOOOo00O00oOo + 'KIDS.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 27 , oOOOo00O00oOo + 'MUSIC.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']PROGRAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 28 , oOOOo00O00oOo + 'PROGRAMS.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']XXX[/COLOR]' , 'URL' , 29 , oOOOo00O00oOo + 'XXX.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 51 - 51: I1ii11iIi11i + O0oOO0 / iiII11i1I1IIi - ooOoO0O00
 if 51 - 51: I1ii11iIi11i - Ii1I * oo0oO00
def ii1111Ii1i ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'CHECK ADVANCED XML' , str ( ooOO0O0ooOooO ) , 8 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'MUCKYS XML' , str ( ooOO0O0ooOooO ) + '/wizard/muckys.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( '0CACHE XML' , str ( ooOO0O0ooOooO ) + '/wizard/0cache.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'MIKEY1234 XML' , str ( ooOO0O0ooOooO ) + '/wizard/mikey.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'TUXENS XML' , str ( ooOO0O0ooOooO ) + '/wizard/tuxens.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'P2P RECOMMENDED XML1' , str ( ooOO0O0ooOooO ) + '/wizard/p2p1.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'P2P RECOMMENDED XML2' , str ( ooOO0O0ooOooO ) + '/wizard/p2p2.xml' , 7 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 o0OIiII ( 'DELETE XML' , str ( ooOO0O0ooOooO ) , 11 , oOOOo00O00oOo + 'XML.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 48 - 48: o0o00Oo0O * IIi - o0o00Oo0O / IIi + OOooOOo
def IIo0Oo0oO0oOO00 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , OO0o , '' )
 if 52 - 52: oO0o % IIi * IIiIiII11i
def I1IiIii11I ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , OO0o , '' )
 o0OIiII ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , OO0o , '' )
 if 29 - 29: I11i
 if 86 - 86: IIiIiII11i . iIi1i1ii1
 if 2 - 2: ii
def OoOoO ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  o0o0O00 ( )
 if O0oO0 == 0 :
  i1iIiIIi1II1ii ( ooO0oOOooOo0 )
 if O0oO0 == 0 :
  i1II1Ii1i1 ( ooO0oOOooOo0 )
  if 45 - 45: Oooo0O0oo00oO * OooOO000 . OOoOoo - OooOO000 + iIi1i1ii1
  if 34 - 34: Oooo0O0oo00oO . I1ii11iIi11i
  if 78 - 78: Ii1I % oOo0O0Ooo / ii % Oooo0O0oo00oO - iiII11i1I1IIi
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 2 - 2: iI11I1II1I1I
def iiii1 ( ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o00oooO0Oo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O0o0O00Oo0o0 )
 for O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , O0o0OO0000ooo , O0o0OO0000ooo , '' )
 Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
 if 66 - 66: O0oOO0 * iI11I1II1I1I % iI11I1II1I1I * iIi1i1ii1 - OOoOoo - iIi1i1ii1
def o0O0oO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 39 - 39: OOoOoo . IIiIiII11i
def o0o0O00 ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 45 - 45: O0oOO0 * OOooOOo / iI11I1II1I1I
def o00ooOoO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + IIi11II1II111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 55 - 55: OOoOoo
def o0O0OO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 70 - 70: I1ii11iIi11i - O0oOO0 . iI11I1II1I1I % oo0oO00 / OOooOOo - o0o00Oo0O
def o0O0oo0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + II11iI1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 48 - 48: oo0oO00 . ii . oOo0O0Ooo . OOooOOo % Ii1I / iiII11i1I1IIi
def ii1I111i1Ii ( url ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 84 - 84: Ii1I % iI11I1II1I1I + oO0o . Ii1I % oO0o
def i1iIiIIi1II1ii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o0OooooO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 40 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 81 - 81: ooOoO0O00 % I11i - OooOO000 + Ii - ii
def I1IiiiIiI ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 20 - 20: OOoOoo % ii + Ii % IIiIiII11i - oO0o
def oO0O0OO0O ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ii11i1Ii11I ( )
 if O0oO0 == 1 :
  ii1ii11IiI ( )
 if O0oO0 == 2 :
  I1I ( )
  if 39 - 39: oo0oO00
  if 64 - 64: iI11I1II1I1I / o0o00Oo0O % iIi1i1ii1 . ii + iIi1i1ii1 + O0oOO0
  if 79 - 79: ii - iIi1i1ii1 * iIi1i1ii1 . OOooOOo
  if 100 - 100: IIiIiII11i * oo0oO00 % oOo0O0Ooo / Ii1I
def ii1ii11IiI ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , OOoo0oOO00 in o00oooO0Oo :
  I1i11111i1i11 ( 'Android Apps' + OOoo0oOO00 , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for ooO0oOOooOo0 , OOoo0oOO00 in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'Android Games' + OOoo0oOO00 , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def ii11iiIi ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/cat' in url :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def i11iI11I1I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/app' in url :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def Ii1iiIi1I11i ( url ) :
 OOoO = O0 ( url )
 O0OOO = url
 if "page=" in str ( url ) :
  O0OOO = url . split ( '?' ) [ 0 ]
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'apk' in url :
   o0OIiII ( ( Oo0OO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + O0o0OO0000ooo )
 if len ( o0O0OOO0Ooo ) > 1 :
  o0O0OOO0Ooo = str ( o0O0OOO0Ooo [ len ( o0O0OOO0Ooo ) - 1 ] )
 o0OIiII ( 'Next Page' , O0OOO + str ( o0O0OOO0Ooo ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def ii1i1iiI ( name , url ) :
 OOoO = oo0O0o00o0O ( url )
 name = name
 o00oooO0Oo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  url = 'https://www.apkfiles.com' + url
  Oo0oOo0ooOOOo ( name , url , 'Brackets' )
def I1I ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11I1II = 'https://www.apkfiles.com/search?q=' + ( o00oO0 ) . replace ( ' ' , '+' ) + '&search_type=1'
 OO0 = i11I1II . lower ( )
 Ii1iiIi1I11i ( OO0 )
 if 71 - 71: IIiIiII11i - IIi - iiII11i1I1IIi * o0o00Oo0O * iIi1i1ii1
def ii1ii1I1IIi1 ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( oOOoo0 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , Oo0OO + '.apk' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 24 - 24: oO0o - O0oOO0 + Ii1I / iiII11i1I1IIi % oOo0O0Ooo + iI11I1II1I1I
def oO00o ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , Oo0OO + '.mp4' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 36 - 36: OooOO000 . IIiIiII11i % OOoOoo
 if 84 - 84: ii - Ii / iI11I1II1I1I / ii / Ii1I
def iIIii1 ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , name )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iIi = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIi
 print '======================================='
 extract . all ( Ii1I1Ii , iIi , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 1 - 1: oOo0O0Ooo * OOooOOo % OooOO000 / Ii1I * iI11I1II1I1I
 if 57 - 57: Oooo0O0oo00oO + OooOO000 % Ii1I . oO0o / oO0o * o0o00Oo0O
 if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
 if 68 - 68: I11i
 if 20 - 20: OooOO000 - OooOO000
def Ii11i1Ii11I ( ) :
 O0o0O00Oo0o0 = O0 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , ooO0oOOooOo0 , O0OooOo0o , iiI11ii1I1 , iIIiI11i1I11 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 80003 , O0OooOo0o , oOOOo00O00oOo + 'APKToolsB.png' , iIIiI11i1I11 )
def II1iIiiI11i11 ( apk , ret = None ) :
 if apk == "kodi" :
  iII11iiIIi11 = "https://kodi.tv/download/"
  O0o0O00Oo0o0 = O0 ( iII11iiIIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O0o0O00Oo0o0 )
  if len ( o00oooO0Oo ) == 1 :
   Iiii11I = o00oooO0Oo [ 0 ] [ 0 ]
   oO00oOOo0Oo = o00oooO0Oo [ 0 ] [ 1 ]
   OO0ooo0 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( Iiii11I , oO00oOOo0Oo )
  if ret == 'version' : return Iiii11I
  else : return OO0ooo0
 elif apk == "spmc" :
  II1II1iI = 'https://github.com/koying/SPMC/releases/latest/'
  O0o0O00Oo0o0 = O0 ( II1II1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O0o0O00Oo0o0 )
  Iiii11I = re . sub ( '<[^<]+?>' , '' , o00oooO0Oo [ 0 ] ) . replace ( ' ' , '' )
  OO0ooo0 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( Iiii11I , Iiii11I )
  if ret == 'version' : return Iiii11I
  else : return OO0ooo0
def Oo0oOo0ooOOOo ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  OooooO = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not OooooO : oO0O0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iI111i11iI1 = name
  if OooooO :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not I1i1I11I ( url ) == True : oO0O0 ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % iI111i11iI1 , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iIIiii11iIiiI = zipfile . ZipFile ( Ii1I1Ii )
    for file in iIIiii11iIiiI . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as oOOo0O00o :
       III1ii = file . split ( '/' ) [ 1 ]
       oOOo0O00o . write ( iIIiii11iIiiI . read ( file ) )
       xbmc . sleep ( 500 )
       oOOo0O00o . close ( )
       try :
        os . remove ( Ii1I1Ii )
       except :
        pass
       Ii1I1Ii = os . path . join ( oooOOOOO , III1ii )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : oO0O0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oO0O0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 23 - 23: O0oOO0 * iiII11i1I1IIi
 if 53 - 53: IIi - OOooOOo . iiII11i1I1IIi . OooOO000
 if 48 - 48: iiII11i1I1IIi + iIi1i1ii1
 if 60 - 60: oo0oO00 + iiII11i1I1IIi . iIi1i1ii1 / ooOoO0O00 . iI11I1II1I1I
def i1i11ii1Ii ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O0o0O00Oo0o0 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  ooO0oOOooOo0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + ooO0oOOooOo0 )
  i1Oo0oOo000OoO0 ( ( Oo0OO ) . replace ( '_' , ' ' ) , ooO0oOOooOo0 )
  if 25 - 25: Ii1I . ooOoO0O00 . IIiIiII11i / OooOO000
def i1Oo0oOo000OoO0 ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  OooooO = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not OooooO : oO0O0 ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iI111i11iI1 = name
  if OooooO :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not I1i1I11I ( url ) == True : oO0O0 ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % iI111i11iI1 , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : oO0O0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oO0O0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 54 - 54: ooOoO0O00 . oo0oO00 - Ii1I + OOoOoo + I1ii11iIi11i / I1ii11iIi11i
 if 22 - 22: OOoOoo . iI11I1II1I1I
def i1IiiiiIi1I ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 56 - 56: ii * o0o00Oo0O
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
def oooO ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 30015 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 44 - 44: iI11I1II1I1I . Ii1I + OooOO000 . OOoOoo
def II1i11 ( url , iconimage , fanart ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00o = url
 O0o0OO0000ooo = iconimage
 fanart = fanart
 o00oooO0Oo = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for OooiiIi1i , Oo0OO in o00oooO0Oo :
  if '.mp4' in Oo0OO :
   o0OIiII ( 'Watch VIDEO' , url + '/' + OooiiIi1i , 222 , O0o0OO0000ooo , fanart , '' )
  if 'description' in Oo0OO :
   o0OIiII ( 'Read Description' , url + '/' + OooiiIi1i , 30017 , O0o0OO0000ooo , fanart , '' )
  if 'images' in Oo0OO :
   I1IiiiiI ( 'View Images' , url + '/' + OooiiIi1i , 30018 , O0o0OO0000ooo , fanart , '' )
  if 'url' in Oo0OO :
   o0OIiII ( 'Install Build On Android' , url + '/' + OooiiIi1i , 30016 , O0o0OO0000ooo , fanart , '' )
  if 'url' in Oo0OO :
   o0OIiII ( 'Install Build On Pc' , url + '/' + OooiiIi1i , 30019 , O0o0OO0000ooo , fanart , '' )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 28 - 28: IIiIiII11i - O0oOO0 % OOooOOo + oO0o - OOooOOo
def IiI ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  oooO0oOoo ( url )
  if 76 - 76: ooOoO0O00 % OOooOOo - oOo0O0Ooo / I11i * OOoOoo
def iIiIIiI1i1Ii ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  o0OO0OOO0O ( url )
  if 36 - 36: Ii / iiII11i1I1IIi . oo0oO00 + iIi1i1ii1 . o0o00Oo0O + oOo0O0Ooo
def iiII1iiIi ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'desc="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for iI1i1I1III1i in o00oooO0Oo :
  OOOiiiiI ( 'Description:' , iI1i1I1III1i )
  if 68 - 68: IIi - O0oOO0 + I1ii11iIi11i
def i11Iii1Ii1i1 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 url = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for OooiiIi1i , Oo0OO in o00oooO0Oo :
  if 'png' in Oo0OO :
   o0OIiII ( 'image' , '' , '' , url + '/' + OooiiIi1i , url + '/' + OooiiIi1i , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 10 - 10: iiII11i1I1IIi . ooOoO0O00 + IIi
def oOOoOOO0oo0 ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , name + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o00O0 ( )
 if 87 - 87: OOoOoo / OOooOOo % I11i * O0oOO0
 if 77 - 77: O0oOO0 - I1ii11iIi11i - iI11I1II1I1I
def o0OO0OOO0O ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 OO0Oooo0oOO0O ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1I1IiIi1 ( )
 if 16 - 16: oO0o / iiII11i1I1IIi / ooOoO0O00 . iiII11i1I1IIi + O0oOO0
def oooO0oOoo ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 OO0Oooo0oOO0O ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1I1IiIi1 ( )
 if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
def IiiIi11Ii1iI1 ( name , url , description ) :
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii1I1Ii = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1I1IiIi1 ( )
 if 91 - 91: Oooo0O0oo00oO + OooOO000 . oo0oO00
def ii1iII1II ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def ii1 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo0o0O00 , log ) )
 if not os . path . exists ( oOo0oooo00o ) : os . makedirs ( oOo0oooo00o )
 if not os . path . exists ( oO0o0o0ooO0oO ) : oOOo0O00o = open ( oO0o0o0ooO0oO , 'w' ) ; oOOo0O00o . close ( )
 with open ( oO0o0o0ooO0oO , 'a' ) as oOOo0O00o :
  i1I111i1ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOo0O00o . write ( i1I111i1ii . rstrip ( '\r\n' ) + '\n' )
def I1I1IiIi1 ( ) :
 O0oO0 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO0 == 0 : return
 elif O0oO0 == 1 : pass
 oO0oOoo0O = ii1iII1II ( )
 ii1 ( "Platform: " + str ( oO0oOoo0O ) )
 os . _exit ( 1 )
 ii1 ( "Force close failed!  Trying alternate methods." )
 if oO0oOoo0O == 'osx' :
  ii1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0oOoo0O == 'linux' :
  ii1 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0oOoo0O == 'android' :
  ii1 ( "############ try android force close #################" )
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
 elif oO0oOoo0O == 'windows' :
  ii1 ( "############ try windows force close #################" )
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
  ii1 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  ii1 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 26 - 26: I1ii11iIi11i + oOo0O0Ooo * Oooo0O0oo00oO + OOoOoo
  if 88 - 88: oo0oO00 + Ii % O0oOO0 * Oooo0O0oo00oO * Oooo0O0oo00oO * IIi
  if 24 - 24: OOoOoo / iiII11i1I1IIi + iIi1i1ii1 . iIi1i1ii1
def i1II1Ii1i1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I1ii1i , i1II11II1 , II1IIIii in os . walk ( url ) :
  for file in II1IIIii :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    I1i = open ( ( os . path . join ( I1ii1i , file ) ) ) . read ( )
    II11Ii111II1 = I1i . replace ( I11 , 'special://home/' )
    oOOo0O00o = open ( ( os . path . join ( I1ii1i , file ) ) , mode = 'w' )
    oOOo0O00o . write ( str ( II11Ii111II1 ) )
    oOOo0O00o . close ( )
 I1I1IiIi1 ( )
 if 72 - 72: iiII11i1I1IIi % I11i % O0oOO0 + oo0oO00 % Ii + o0o00Oo0O
def iiI1iii ( ) :
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 65 - 65: iI11I1II1I1I % O0oOO0 + o0o00Oo0O / ii
def O0000oO0o00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def oo000o ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def OO00o0oOO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , O0o0OO0000ooo )
def i1i1I1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11I ( url )
def I1iOOo0O ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0
 oOOoooO0O0 = 'https://www.radionomy.com/en/search/index?query=' + ( o00oO0 ) . replace ( ' ' , '+' )
 I1 = O0 ( oOOoooO0O0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + ooO0oOOooOo0 , 70005 , O0o0OO0000ooo )
  if 46 - 46: iI11I1II1I1I
  if 33 - 33: oo0oO00 % oo0oO00 % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
def iIoo0ooooO ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://www.listenlive.eu/' + ooO0oOOooOo0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def Oo0O0Oo00O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 91 - 91: OOoOoo * oo0oO00 - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOoOoo
def OO00o ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.toonjet.com/' + ooO0oOOooOo0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiI11i1I1ii1i1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OOoO )
 for url , O0o0OO0000ooo in o00oooO0Oo :
  if 'ol.gif' in O0o0OO0000ooo :
   pass
  elif 'link_block_' in O0o0OO0000ooo :
   pass
  elif '.png' in O0o0OO0000ooo :
   pass
  else :
   I1i11111i1i11 ( ( O0o0OO0000ooo ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0ooooo0O00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 5 - 5: OOooOOo % iiII11i1I1IIi + iIi1i1ii1
  if 13 - 13: iIi1i1ii1
def Oo00OO0 ( ) :
 ii1II1II ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 ii1II1II ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 42 - 42: IIi
def O0o00oo0OO0 ( ) :
 ii1II1II ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 ii1II1II ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 ii1II1II ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 60 - 60: OOoOoo
def O000O ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , iiii1IIi1 in o00oooO0Oo :
  if 'Parent' in Oo0OO :
   pass
  elif '2' in iiii1IIi1 :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: iIi1i1ii1
def I1IiI ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , iiii1IIi1 in o00oooO0Oo :
  if o00oO0 in Oo0OO . lower ( ) :
   if '1' in iiii1IIi1 :
    ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in iiii1IIi1 :
    ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in iiii1IIi1 :
    ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 44 - 44: Oooo0O0oo00oO / Oooo0O0oo00oO . I11i % iIi1i1ii1 + OOooOOo
    if 57 - 57: iiII11i1I1IIi % oO0o - oO0o
def ii1iIII ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , iiii1IIi1 in o00oooO0Oo :
  if '1' in iiii1IIi1 :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in iiii1IIi1 :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in iiii1IIi1 :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: OOooOOo * iI11I1II1I1I . OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def OooOo ( url ) :
 OooiiIi1i = url
 I1 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0OO in o0O0OOO0Ooo :
  if 'mp3' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OooiiIi1i + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OooiiIi1i + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OooiiIi1i + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in Oo0OO :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 67 - 67: I1ii11iIi11i / o0o00Oo0O
   if 88 - 88: OOooOOo - Oooo0O0oo00oO
   if 63 - 63: iIi1i1ii1 * ii
def I1iIiiiI1 ( url ) :
 I1 = O0 ( url )
 OooiiIi1i = url
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if 'Parent' in Oo0OO :
   pass
  elif '.db' in Oo0OO :
   pass
  elif '.jpg' in Oo0OO :
   pass
  elif '.html' in Oo0OO :
   pass
  elif '.doc' in Oo0OO :
   pass
  elif 'mp3' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: OOooOOo - OOoOoo - Oooo0O0oo00oO + I1ii11iIi11i % iI11I1II1I1I / Ii
   if 12 - 12: OOoOoo
def oOOO0ooOO ( ) :
 ii1II1II ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 ii1II1II ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 ii1II1II ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 3 - 3: ii
def O0OoO0o ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo in o00oooO0Oo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in O0o0OO0000ooo :
   pass
  else :
   ii1II1II ( O0o0OO0000ooo , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooO0oOOooOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + O0o0OO0000ooo + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 1 - 1: OOoOoo % oo0oO00 * Ii1I - IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: O0oOO0 - iiII11i1I1IIi % OOooOOo
 if 72 - 72: oOo0O0Ooo + iIi1i1ii1 . OOooOOo + OOooOOo
def ooooOoo0OO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: IIiIiII11i . OOoOoo % Oooo0O0oo00oO % oo0oO00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: O0oOO0 * oo0oO00 / iI11I1II1I1I % O0oOO0 / iI11I1II1I1I
def Iiii1 ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if o00oO0 in Oo0OO . lower ( ) :
   if '</a>' in Oo0OO :
    pass
   elif '(' in Oo0OO :
    ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 36 - 36: iiII11i1I1IIi
    if 90 - 90: o0o00Oo0O
def Iiii1iI111II1ii ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: iiII11i1I1IIi * iI11I1II1I1I . iIi1i1ii1 - ii * IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: o0o00Oo0O % oOo0O0Ooo - iiII11i1I1IIi . oO0o
 if 42 - 42: iiII11i1I1IIi / I11i + I1ii11iIi11i . I1ii11iIi11i % Oooo0O0oo00oO
def Ii1III1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in o00oooO0Oo :
  OooiiIi1i = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OooiiIi1i )
  if 80 - 80: iI11I1II1I1I . iiII11i1I1IIi . OooOO000
def iii1II1iI1IIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '<p align' in Oo0OO :
   pass
  elif '&nbsp;' in Oo0OO :
   pass
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 41 - 41: oOo0O0Ooo - OooOO000 % IIiIiII11i . OooOO000 - oo0oO00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: IIi - Oooo0O0oo00oO
 if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . oo0oO00 % OOoOoo . IIiIiII11i
def I1iIII1 ( ) :
 I1 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'ongoing' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Disney.png' , '' , '' )
  if 'genre' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Genre.png' , '' , '' )
  if 'years' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Years.png' , '' , '' )
def I1ii1Ii1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 OoOoOiI111I1III = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , O0o0OO0000ooo , O0o0OO0000ooo , Oo0OO )
 for url , Oo0OO in OoOoOiI111I1III :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def i111IiiI1Ii ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 O00oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 OooOOOOOo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 i1I11ii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in OooOOOOOo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , Oo0OO in O00oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def o0ooO00O0O ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 41 - 41: Ii1I
def oOo0OoOOo0 ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 o00oooO0Oo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '9cart' in ooO0oOOooOo0 :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 5 - 5: I1ii11iIi11i
def o0oOo00 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 o0OOo00OoO = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if '9cart' in url :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in o0O0OOO0Ooo :
  if '9cart' in url :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , Oo0OO in o0OOo00OoO :
  if '9cart' in url :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 22 - 22: iI11I1II1I1I + iIi1i1ii1 + Ii1I + OooOO000 - IIi
def I1IIII1i1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20003 , O0o0OO0000ooo )
 for url , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 67 - 67: I1ii11iIi11i / OOoOoo - iIi1i1ii1
def O0O00OoOoOOo ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'Watch' in url :
   I1i11111i1i11 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 58 - 58: iIi1i1ii1 + iI11I1II1I1I
def o0II1IIi1iII1i ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 26 - 26: o0o00Oo0O
def iiiIi ( url ) :
 url = cloudflare . source ( url )
 i1I11iIiII ( url )
 if 62 - 62: o0o00Oo0O . I1ii11iIi11i
def iI1ii ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . recompile ( 'src="([^"]*)"' )
 for url in o00oooO0Oo :
  i1I11iIiII ( url )
  if 76 - 76: IIi + iI11I1II1I1I + OOooOOo . oO0o
  if 49 - 49: iIi1i1ii1 / OOoOoo / Oooo0O0oo00oO
def iIii ( ) :
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - OOoOoo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 if 38 - 38: I11i % OooOO000 + Ii + iiII11i1I1IIi + OOoOoo / Ii
def OOoOoo0 ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 94 - 94: iiII11i1I1IIi - I1ii11iIi11i + O0oOO0
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 59 - 59: oo0oO00 . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if o00oO0 in Oo0OO . lower ( ) :
   if 'Dad!' in Oo0OO :
    pass
   elif 'Family Guy' in Oo0OO :
    pass
   elif '2 Stupid' in Oo0OO :
    pass
   elif 'The Zelfs' in Oo0OO :
    pass
   elif 'A Clone' in Oo0OO :
    pass
   elif 'A.T.O.M' in Oo0OO :
    pass
   elif 'Almost Naked' in Oo0OO :
    pass
   elif 'Angry Kid' in Oo0OO :
    pass
   elif 'Annoying Orange' in Oo0OO :
    pass
   elif 'Aqua Teen' in Oo0OO :
    pass
   elif 'Assy Mcgee' in Oo0OO :
    pass
   elif 'Astroblast' in Oo0OO :
    pass
   elif 'Atomic Betty' in Oo0OO :
    pass
   elif 'Axe Cop' in Oo0OO :
    pass
   elif 'Baby Playpen' in Oo0OO :
    pass
   elif 'Beavis and Butt' in Oo0OO :
    pass
   elif 'Celebrity Deathmatch' in Oo0OO :
    pass
   elif 'Clerks The' in Oo0OO :
    pass
   elif 'Crapston Villas' in Oo0OO :
    pass
   elif 'Duckman:' in Oo0OO :
    pass
   elif 'Stripperella' in Oo0OO :
    pass
   elif 'Vixen' in Oo0OO :
    pass
   else :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
    if 56 - 56: O0oOO0 + OOoOoo
    if 32 - 32: IIiIiII11i + OOooOOo % OOoOoo / OOooOOo + Ii1I
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 2 - 2: Ii - OooOO000 + oO0o % oo0oO00 * IIi
def iII11I1Ii1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if 'Dad!' in Oo0OO :
   pass
  elif 'Family Guy' in Oo0OO :
   pass
  elif '2 Stupid' in Oo0OO :
   pass
  elif 'The Zelfs' in Oo0OO :
   pass
  elif 'A Clone' in Oo0OO :
   pass
  elif 'A.T.O.M' in Oo0OO :
   pass
  elif 'Almost Naked' in Oo0OO :
   pass
  elif 'Angry Kid' in Oo0OO :
   pass
  elif 'Annoying Orange' in Oo0OO :
   pass
  elif 'Aqua Teen' in Oo0OO :
   pass
  elif 'Assy Mcgee' in Oo0OO :
   pass
  elif 'Astroblast' in Oo0OO :
   pass
  elif 'Atomic Betty' in Oo0OO :
   pass
  elif 'Axe Cop' in Oo0OO :
   pass
  elif 'Baby Playpen' in Oo0OO :
   pass
  elif 'Beavis and Butt' in Oo0OO :
   pass
  elif 'Celebrity Deathmatch' in Oo0OO :
   pass
  elif 'Clerks The' in Oo0OO :
   pass
  elif 'Crapston Villas' in Oo0OO :
   pass
  elif 'Duckman:' in Oo0OO :
   pass
  elif 'Stripperella' in Oo0OO :
   pass
  elif 'Vixen' in Oo0OO :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: o0o00Oo0O - iiII11i1I1IIi . Oooo0O0oo00oO % iiII11i1I1IIi + iiII11i1I1IIi
def i1iI1Iiii1I ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for O0o0OO0000ooo in o0O0OOO0Ooo :
  I1iII = O0o0OO0000ooo
 o0OOo00OoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in o0OOo00OoO :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10007 , I1iII )
  if 29 - 29: ooOoO0O00 % iiII11i1I1IIi / iIi1i1ii1 + OOooOOo - Oooo0O0oo00oO - Ii1I
  if 69 - 69: iI11I1II1I1I . IIiIiII11i . ooOoO0O00 - I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: OOoOoo % Oooo0O0oo00oO
def oO0O0o0O ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   oOO00ooOOo ( url )
   if 20 - 20: Ii1I
   if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
def oOO00ooOOo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11I ( url )
  if 34 - 34: IIi * IIi - Ii1I - o0o00Oo0O . Ii
  if 32 - 32: iI11I1II1I1I . oO0o * O0oOO0 / Oooo0O0oo00oO . IIiIiII11i - I1ii11iIi11i
  if 10 - 10: Ii1I / Ii - IIi + O0oOO0 * oOo0O0Ooo
def IIii1111 ( ) :
 if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , OO0o , '' )
 if 64 - 64: oo0oO00 + oO0o
def IiIi11iiIIiI1 ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'elete' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 222 , O0o0OO0000ooo )
   if 6 - 6: iIi1i1ii1 * ii + OooOO000 / IIi
def I1IiI1IIiI ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oooo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , o0o0oo0Ooo , i1iII1IiiIiI1 in oooo :
  for o00oO0 in o0o0oo0Ooo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iI1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for ooO0oOOooOo0 , Oo0OO in iI1i :
    if 'tube' in ooO0oOOooOo0 :
     pass
    elif 'stage' in ooO0oOOooOo0 :
     OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0o0oo0Ooo + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0o0OO0000ooo , )
    elif 'vee' in ooO0oOOooOo0 :
     pass
     if 3 - 3: iIi1i1ii1 / oo0oO00
def Ii11 ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oooo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , o0o0oo0Ooo , i1iII1IiiIiI1 in oooo :
  iI1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for ooO0oOOooOo0 , Oo0OO in iI1i :
   if 'tube' in ooO0oOOooOo0 :
    pass
   elif 'stage' in ooO0oOOooOo0 :
    OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0o0oo0Ooo + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0o0OO0000ooo )
   elif 'vee' in ooO0oOOooOo0 :
    pass
    if 3 - 3: IIi + OooOO000 . ooOoO0O00 / Oooo0O0oo00oO % OooOO000
    if 98 - 98: iIi1i1ii1 * iI11I1II1I1I . IIi * I1ii11iIi11i / Ii1I + OOoOoo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: O0oOO0
def OoO ( url ) :
 I1 = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iIIiii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( iIIiii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in iIIiii :
  I11I ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 19 - 19: oOo0O0Ooo % IIi . iIi1i1ii1 * OOoOoo
  if 89 - 89: OOooOOo . Oooo0O0oo00oO
  if 7 - 7: O0oOO0 % OOooOOo - oOo0O0Ooo + I1ii11iIi11i
  if 70 - 70: IIiIiII11i + OooOO000 + Ii - ooOoO0O00 / iIi1i1ii1
  if 40 - 40: Ii1I * OooOO000
  if 38 - 38: o0o00Oo0O . I1ii11iIi11i + OOooOOo - O0oOO0
  if 43 - 43: iiII11i1I1IIi + I1ii11iIi11i / ii
def ii1II ( ) :
 if 24 - 24: o0o00Oo0O + I11i * IIi - OooOO000
 iii11i1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 iii11i1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 100 - 100: oo0oO00 % Ii * iiII11i1I1IIi / oO0o % Ii1I + Oooo0O0oo00oO
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
def OO0oo00oOO ( ) :
 iii11i1 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 iii11i1 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 38 - 38: OooOO000 . iiII11i1I1IIi . oOo0O0Ooo * oO0o
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def oOoo00o0oOO ( ) :
 if 61 - 61: ooOoO0O00 * I11i + iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 oOoo0ooOoo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 52 - 52: oO0o * ii
 for Ii11iiI in oOoo0ooOoo :
  o0OO0oooo = oOOoo0Oo + Ii11iiI + IIIII
  I1 = Oo0OoO00oOO0o ( o0OO0oooo )
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
   if o00oO0 in Oo0OO . lower ( ) :
    I11II1i1 ( Oo0OO , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , iiI11ii1I1 , o0o0oOoOO0O )
    if 46 - 46: IIiIiII11i % iiII11i1I1IIi - ooOoO0O00 / oo0oO00 * OOooOOo
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 92 - 92: I1ii11iIi11i - OooOO000
    if 24 - 24: O0oOO0 / OooOO000 / oo0oO00 % OOooOOo / Ii1I * OOoOoo
def iiIiIIi11I1 ( ) :
 if 86 - 86: iI11I1II1I1I . oOo0O0Ooo * oo0oO00
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 oOoo0ooOoo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 49 - 49: I11i
 for Ii11iiI in oOoo0ooOoo :
  I11iiI = oOOoo0Oo + Ii11iiI + IIIII
  I1 = Oo0OoO00oOO0o ( I11iiI )
  o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
   if o00oO0 in Oo0OO . lower ( ) :
    iii11i1 ( Oo0OO , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
    if 40 - 40: IIi
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: I1ii11iIi11i
    if 22 - 22: Oooo0O0oo00oO
def I1I11Iiii111 ( ) :
 if 38 - 38: oO0o . OOoOoo
 OOoO = O0 ( oOOoo0Oo + 'spongemain.php' )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
  iii11i1 ( Oo0OO , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def ii111iiIii ( url ) :
 if 57 - 57: I11i / OooOO000
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiIiII = ( '%s%s' % ( IIiiiI1iI , url ) )
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in o00oooO0Oo :
  O0O0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
  for iII1111III1I in O0O0 :
   if iII1111III1I == url :
    Oo0OO = ( '[COLORred]Watched - [/COLOR]' + Oo0OO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I11II1i1 ( Oo0OO , url , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
  if 70 - 70: Oooo0O0oo00oO * O0oOO0 / oOo0O0Ooo * OOooOOo * oOo0O0Ooo
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 61 - 61: O0oOO0 + Ii1I / ooOoO0O00 * O0oOO0
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 90 - 90: IIi % O0oOO0
  if 6 - 6: ii / Ii / OooOO000
def OooO0O0Ooo ( url ) :
 if 85 - 85: I11i / OooOO000
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , o0o0oOoOO0O , url , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
  iii11i1 ( Oo0OO , url , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  if 67 - 67: oo0oO00 % O0oOO0
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 39 - 39: Ii + iIi1i1ii1
  if 7 - 7: iI11I1II1I1I - ooOoO0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: OooOO000 % o0o00Oo0O / oOo0O0Ooo % oo0oO00
def I11II1i1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 25 - 25: IIiIiII11i / oO0o
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  IiI11i1IIiiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 64 - 64: o0o00Oo0O % OOoOoo
def iii11i1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 40 - 40: I11i + oo0oO00
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  IiI11i1IIiiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
if 77 - 77: Ii % iIi1i1ii1 + OooOO000 % ii - oo0oO00
if 26 - 26: I1ii11iIi11i + o0o00Oo0O - iI11I1II1I1I
if 47 - 47: ii
if 2 - 2: OOooOOo % OooOO000 * I1ii11iIi11i * OOooOOo
if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
if 26 - 26: I11i % Oooo0O0oo00oO + Oooo0O0oo00oO % oo0oO00 * Ii / iiII11i1I1IIi
if 64 - 64: O0oOO0 % OOooOOo / IIiIiII11i % OOoOoo - iiII11i1I1IIi
if 2 - 2: OooOO000 - Ii1I + I11i * oO0o / iiII11i1I1IIi
if 26 - 26: Oooo0O0oo00oO * I1ii11iIi11i
if 31 - 31: oo0oO00 * O0oOO0 . IIi
if 35 - 35: oo0oO00
if 94 - 94: OOoOoo / Ii % o0o00Oo0O
if 70 - 70: oo0oO00 - I1ii11iIi11i / ii % ii
if 95 - 95: ii % ii . IIi
if 26 - 26: O0oOO0 + iIi1i1ii1 - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
def o0IiIiI111IIII1 ( string ) :
 if Oo0oOOo == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 100 - 100: Oooo0O0oo00oO * o0o00Oo0O + oOo0O0Ooo + OOooOOo . Oooo0O0oo00oO
def OO0IIIIIIi111i ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iiIIIIiI111 = [ ]
 try :
  if 86 - 86: IIiIiII11i % iI11I1II1I1I / Ii1I - I11i * IIi . oOo0O0Ooo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  o0IiIiI111IIII1 ( 'Making Favorites File' )
  iiIIIIiI111 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  I1i = open ( I1IIiiIiii , "w" )
  I1i . write ( json . dumps ( iiIIIIiI111 ) )
  I1i . close ( )
 else :
  o0IiIiI111IIII1 ( 'Appending Favorites' )
  I1i = open ( I1IIiiIiii ) . read ( )
  OoOoOoo0OoO0 = json . loads ( I1i )
  OoOoOoo0OoO0 . append ( ( name , url , iconimage , fanart , mode ) )
  II11Ii111II1 = open ( I1IIiiIiii , "w" )
  II11Ii111II1 . write ( json . dumps ( OoOoOoo0OoO0 ) )
  II11Ii111II1 . close ( )
  if 17 - 17: IIi * IIiIiII11i / iIi1i1ii1 + iI11I1II1I1I . oo0oO00 - o0o00Oo0O
  if 70 - 70: IIi * O0oOO0 - oo0oO00 + I1ii11iIi11i % Ii1I - iIi1i1ii1
def oooOoO00OooO0 ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  iiIIIIiI111 = [ ]
  o0IiIiI111IIII1 ( 'Making Favorites File' )
  iiIIIIiI111 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  I1i = open ( I1IIiiIiii , "w" )
  I1i . write ( json . dumps ( iiIIIIiI111 ) )
  I1i . close ( )
 else :
  o00OOo = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  Ii11III = len ( o00OOo )
  for I1Ii1i11I1I in o00OOo :
   Oo0OO = I1Ii1i11I1I [ 0 ]
   ooO0oOOooOo0 = I1Ii1i11I1I [ 1 ]
   iIIiiI1II1i11 = I1Ii1i11I1I [ 2 ]
   try :
    oo0o000o0oOO0 = I1Ii1i11I1I [ 3 ]
    if oo0o000o0oOO0 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oo0o000o0oOO0 = iIIiiI1II1i11
    else :
     oo0o000o0oOO0 = iiI11ii1I1
   try : OOO000OOo0o0O = I1Ii1i11I1I [ 5 ]
   except : OOO000OOo0o0O = None
   try : I111Iii1 = I1Ii1i11I1I [ 6 ]
   except : I111Iii1 = None
   if 30 - 30: ooOoO0O00
   if I1Ii1i11I1I [ 4 ] == 0 :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , '' , iIIiiI1II1i11 , iiI11ii1I1 , '' , 'fav' )
   else :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , I1Ii1i11I1I [ 4 ] , iIIiiI1II1i11 , iiI11ii1I1 , '' , 'fav' )
    if 75 - 75: oo0oO00 . Oooo0O0oo00oO - iI11I1II1I1I * oO0o * iiII11i1I1IIi
def ooo0OO0OOooO0 ( name ) :
 OoOoOoo0OoO0 = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for O00O00 in range ( len ( OoOoOoo0OoO0 ) ) :
  if OoOoOoo0OoO0 [ O00O00 ] [ 0 ] == name :
   del OoOoOoo0OoO0 [ O00O00 ]
   II11Ii111II1 = open ( I1IIiiIiii , "w" )
   II11Ii111II1 . write ( json . dumps ( OoOoOoo0OoO0 ) )
   II11Ii111II1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 66 - 66: I1ii11iIi11i - iI11I1II1I1I
 if 9 - 9: I11i % Ii1I . Ii1I
def iIIi ( ) :
 IiIIIIii11i = os . path . join ( O0O , 'addons.ini' )
 oO0OOO00 = open ( IiIIIIii11i , "w+" )
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 oO0OOO00 . write ( r'[' + IiII + ']' + '\n' )
 for Oo0OO , O0o0OO0000ooo , I11iiii1I , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I1iIiI1iiiiI1 = ( Oo0OO + '=plugin://' + IiII + '/?url=' + ooO0oOOooOo0 + '&mode=10012&name=' + ( Oo0OO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( O0o0OO0000ooo ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( O0o0OO0000ooo ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oO0OOO00 . write ( I1iIiI1iiiiI1 + '\n' )
  if 4 - 4: I1ii11iIi11i - oO0o - Ii * OooOO000 / IIi - Oooo0O0oo00oO
  if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
def oo00ooOooO ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247.png' , oOOOo00O00oOo + '247.png' , '' )
def OOoOOo00O0o0 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def OOOoOO ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def ooIi111iII ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def Oo0OoOo ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o00oooO0Oo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 13 - 13: I11i
  if 7 - 7: oOo0O0Ooo + iIi1i1ii1 / Ii / I1ii11iIi11i
def o0o ( ) :
 if 73 - 73: OOooOOo % I11i
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 71 - 71: O0oOO0 - ii * I1ii11iIi11i * oo0oO00 + I11i * Ii1I
def ooO ( ) :
 if 16 - 16: I1ii11iIi11i
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , iIi1IiI in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + '  -  ' + ( iIi1IiI ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 10023 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 74 - 74: oo0oO00
  if 98 - 98: O0oOO0 / ii % IIi * IIiIiII11i - oO0o
  if 95 - 95: oOo0O0Ooo % OooOO000 * oOo0O0Ooo + o0o00Oo0O . OooOO000 % ii
def II11II1I ( ) :
 if 52 - 52: Oooo0O0oo00oO * O0oOO0 + oo0oO00 * oo0oO00 % ooOoO0O00 % oo0oO00
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Action[/COLOR]' , 'Aksiyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Adventure[/COLOR]' , 'Macera' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Animation[/COLOR]' , 'Animasyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Anime[/COLOR]' , 'Anime' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Biography[/COLOR]' , 'Biyografi' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Comedy[/COLOR]' , 'Komedi' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Drama[/COLOR]' , 'Dram' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Family[/COLOR]' , 'Aile' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']History[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Horror[/COLOR]' , 'Korku' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Mystery[/COLOR]' , 'Gizem' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Romance[/COLOR]' , 'Romantik' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Sport[/COLOR]' , 'Spor' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Western[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 96 - 96: I11i * O0oOO0 - Oooo0O0oo00oO * I11i * ooOoO0O00
def I1IIIi1i ( url ) :
 o00o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( o00o )
 o00oooO0Oo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 54 - 54: IIiIiII11i . ooOoO0O00 / Ii1I % oOo0O0Ooo / OooOO000
  if 65 - 65: OOooOOo . OOooOOo - O0oOO0 + I1ii11iIi11i / Ii
  if 90 - 90: iI11I1II1I1I + OOooOOo
  if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
def i1iI ( ) :
 if 84 - 84: I1ii11iIi11i
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00oO0 ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( ooO0oOOooOo0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if o00oO0 in Oo0OO . lower ( ) :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 44 - 44: ii * Ii / I1ii11iIi11i
   if 75 - 75: ii . Oooo0O0oo00oO + oO0o / IIi - oOo0O0Ooo % IIi
   if 89 - 89: iiII11i1I1IIi * iI11I1II1I1I + Ii . ii
def O0O0oO0oo ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for OooiiIi1i , i1i11I1I1iii1 , o00o0o000Oo , Oo0OO in o00oooO0Oo :
  Oooo00OOo = ( o00o0o000Oo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iIiII = ( i1i11I1I1iii1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OooOO = 'Season ' + iIiII + 'Episode ' + Oooo00OOo + Oo0OO
  iio0oo0Oo ( OooOO , OooiiIi1i )
  if 10 - 10: Ii1I
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 87 - 87: I1ii11iIi11i % IIi
  if 53 - 53: ooOoO0O00 - iIi1i1ii1 + iI11I1II1I1I
def iio0oo0Oo ( name , url ) :
 OooiiIi1i = url
 o0Oo00oOO = name
 iii1i1iiiiIi = cloudflare . source ( OooiiIi1i )
 o0O0OOO0Ooo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for iIIiii , O0oo in o0O0OOO0Ooo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0Oo00oOO + O0oo + '[/COLOR]' , iIIiii , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 56 - 56: iIi1i1ii1 * OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: oo0oO00 + o0o00Oo0O * OooOO000 + Ii - Oooo0O0oo00oO - iI11I1II1I1I
 if 5 - 5: Oooo0O0oo00oO % I1ii11iIi11i % iIi1i1ii1 % OOoOoo
def II1III1I1I1Ii ( ) :
 if 17 - 17: IIi + IIiIiII11i + ii / Oooo0O0oo00oO / iIi1i1ii1
 if 80 - 80: I11i % ooOoO0O00 / oo0oO00
 if 56 - 56: ooOoO0O00 . Ii
 if 15 - 15: IIiIiII11i * O0oOO0 % iiII11i1I1IIi / Ii - O0oOO0 + I1ii11iIi11i
 if 9 - 9: oo0oO00 - O0oOO0 + o0o00Oo0O / iiII11i1I1IIi % ooOoO0O00
 if 97 - 97: I11i * OOoOoo
 if 78 - 78: oo0oO00 . Oooo0O0oo00oO + O0oOO0 * iiII11i1I1IIi - ooOoO0O00
 if 27 - 27: IIi % ooOoO0O00 . I1ii11iIi11i % OooOO000
 if 10 - 10: iIi1i1ii1 / ii
 if 50 - 50: Ii - ii . O0oOO0 + o0o00Oo0O . ooOoO0O00
 if 91 - 91: I11i . iiII11i1I1IIi % I1ii11iIi11i - iiII11i1I1IIi . O0oOO0 % Ii
 if 25 - 25: iI11I1II1I1I
 if 63 - 63: OOoOoo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 96 - 96: oo0oO00
 if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . Oooo0O0oo00oO
def oooO0o0oOoO ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Ii11i1I11i ) )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 23 - 23: iIi1i1ii1 + iI11I1II1I1I % iI11I1II1I1I / OOoOoo . O0oOO0 + iI11I1II1I1I
def OOoOO0o0o0Oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 92 - 92: iiII11i1I1IIi * o0o00Oo0O % OooOO000 . iI11I1II1I1I
def o00OoO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if 'episode' in url :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 96 - 96: OOoOoo . ii
  if 39 - 39: Oooo0O0oo00oO + oO0o
def oOoOOOO0OOO ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0oo0oO00o = 'http://www.watchseries.ac/search/' + o00oO0 . replace ( ' ' , '%20' )
 I1 = O0 ( O0oo0oO00o )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'watch online' in Oo0OO :
   pass
  else :
   print ooO0oOOooOo0
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , O0o0OO0000ooo , '' , '' )
   if 35 - 35: iiII11i1I1IIi * iI11I1II1I1I / OOoOoo * ooOoO0O00 * o0o00Oo0O % iI11I1II1I1I
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 97 - 97: Ii + I1ii11iIi11i * Oooo0O0oo00oO % iiII11i1I1IIi . iIi1i1ii1
def iiOo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , o00o0o000Oo , o0o0oOoOO0O in o00oooO0Oo :
  OO00 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( o00o0o000Oo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , O0o0OO0000ooo , '' , o0o0oOoOO0O )
  if 75 - 75: oO0o / IIi + IIiIiII11i % iIi1i1ii1 . Ii
def O0O00O0Oo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  OO00 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 53 - 53: ooOoO0O00 . ooOoO0O00 - oo0oO00 / iiII11i1I1IIi - OOooOOo % oOo0O0Ooo
def O0OiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , O0o0OO0000ooo , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 85 - 85: IIiIiII11i
def o0oOOoo0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 Ii11i1I11i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for i1i11I1I1iii1 , oooo in Ii11i1I11i :
  o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oooo ) )
  for url , Oo0OO in o00oooO0Oo :
   OO00 = ( i1i11I1I1iii1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 57 - 57: oOo0O0Ooo . Ii * IIiIiII11i + ii + IIi
class OoO0o0oOOO ( ) :
 if 86 - 86: OOooOOo . iIi1i1ii1
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 10 - 10: iiII11i1I1IIi * IIi - OOoOoo . oo0oO00 - Oooo0O0oo00oO
  OO00 = name
  self . Get_Sources ( ooO0oOOooOo0 , OO00 )
  if 94 - 94: oOo0O0Ooo % iIi1i1ii1 + oO0o
  if 90 - 90: ooOoO0O00 + o0o00Oo0O - O0oOO0 . iiII11i1I1IIi + iI11I1II1I1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O0 ( URL )
  o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
   self . Get_site_link ( URL , season_name )
   if 88 - 88: IIi * o0o00Oo0O . OooOO000 / ii
 def Get_site_link ( self , url , season_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( I1 )
  o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  o0OOo00OoO = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in o00oooO0Oo :
   self . main ( url , season_name )
  for url in o0O0OOO0Ooo :
   self . main ( url , season_name )
  for url in o0OOo00OoO :
   self . main ( url , season_name )
   if 29 - 29: ii . IIiIiII11i % OOooOOo
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IiiIi1I11 = 'DACLIPS'
   if IiiIi1I11 in OoO0o0oOOO . source_list :
    pass
   else :
    self . daclips ( url , season_name , IiiIi1I11 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    IiiIi1I11 = 'FILEHOOT'
    if IiiIi1I11 in OoO0o0oOOO . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , IiiIi1I11 )
   else :
    if 'thevideo.me' in url :
     IiiIi1I11 = 'THEVIDEO'
     if IiiIi1I11 in OoO0o0oOOO . source_list :
      pass
     else :
      self . thevideo ( url , season_name , IiiIi1I11 )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      IiiIi1I11 = 'ALLMYVIDEOS'
      if IiiIi1I11 in OoO0o0oOOO . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , IiiIi1I11 )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       IiiIi1I11 = 'VIDSPOT'
       if IiiIi1I11 in OoO0o0oOOO . source_list :
        pass
       else :
        self . vidspot ( url , season_name , IiiIi1I11 )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        IiiIi1I11 = 'VODLOCKER'
        if IiiIi1I11 in OoO0o0oOOO . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , IiiIi1I11 )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 13 - 13: OOoOoo * Oooo0O0oo00oO + I11i
         if 27 - 27: O0oOO0 % oo0oO00 - iiII11i1I1IIi / iIi1i1ii1 . ii / I1ii11iIi11i
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 8 - 8: o0o00Oo0O + O0oOO0 + OooOO000
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 47 - 47: oo0oO00
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 92 - 92: ii % oOo0O0Ooo / OOooOOo * OOooOOo % Ii / ii
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
 def daclips ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 48 - 48: iIi1i1ii1
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 96 - 96: O0oOO0 / o0o00Oo0O . IIiIiII11i + iIi1i1ii1 % I11i
 def Printer ( self , Link , season_name , source_name ) :
  if 67 - 67: o0o00Oo0O % OooOO000
  if Link in OoO0o0oOOO . List :
   pass
  elif source_name in OoO0o0oOOO . source_list :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   OoO0o0oOOO . List . append ( Link )
   OoO0o0oOOO . source_list . append ( source_name )
   if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % Oooo0O0oo00oO
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 39 - 39: IIi
   if 60 - 60: Oooo0O0oo00oO
   if 62 - 62: OooOO000 * oo0oO00
   if 74 - 74: OOooOOo . iI11I1II1I1I
   if 87 - 87: OOoOoo
def o0OO0o0o00o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 41 - 41: OOooOOo . iI11I1II1I1I % OOoOoo + o0o00Oo0O
def IIiII11 ( url ) :
 I1IiiiiI ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OOoO )
 for oo0O00OOOOO , url , OoOII11IiI1 , OoOOOO00oOO , iiIIiIi , OoOOoO0oOo , O000oO , oOOo0O00o , I1i , ii11Ii1IiiI1 , O00o0o in o00oooO0Oo :
  OoOII11IiI1 = OoOII11IiI1
  if 'Arsenal' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'arsenal-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                                  ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Bournemouth' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'afc-bournemouth.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                       ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Burnley' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'KEGnQWW.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                                   ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Chelsea' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'chelsea.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                                  ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Crystal' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'CrystalPalace.0.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                       ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Everton' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'Everton.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                                   ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Hull' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'hull-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                                 ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Leicester' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                       ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Liverpool' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'liverpool-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                               ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Manchester City' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'city-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '               ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Manchester United' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + '91.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '          ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Middlesbrough' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                 ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Southampton' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'southampton-fc-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                   ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Stoke City' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'stoke-city.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                          ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Sunderland' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'sunderland-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                        ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Swansea' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'swansea-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                    ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Tottenham' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '        ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Watford' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '                              ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'Bromwich' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '   ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  elif 'West Ham' in OoOII11IiI1 :
   o00OooO0oo = oOOOo00O00oOo + 'west-ham.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + oo0O00OOOOO + ' - ' + OoOII11IiI1 + '             ' + OoOOOO00oOO + '        ' + iiIIiIi + '        ' + OoOOoO0oOo + '        ' + O000oO + '        ' + oOOo0O00o + '        ' + I1i + '        ' + ii11Ii1IiiI1 + '[/COLOR]'
  I1IiiiiI ( str ( Oo0OO ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , o00OooO0oo , o00OooO0oo , OoOII11IiI1 )
  if 65 - 65: Ii1I % O0oOO0 . ii * I11i * oO0o
def II11IiI1 ( description ) :
 OoOII11IiI1 = description
 ooO0oOOooOo0 = ( 'http://www.fullmatchesandshows.com/?s=' + OoOII11IiI1 ) . replace ( ' ' , '%20' )
 iIIi11i ( ooO0oOOooOo0 )
 if 39 - 39: OOooOOo . I1ii11iIi11i - iIi1i1ii1 / I11i / ooOoO0O00
def OOo0OOOoOOo ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o00oooO0Oo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0oOOooOo0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0o0OO0000ooo , OO0o , '' )
  if 29 - 29: OOooOOo . iiII11i1I1IIi + OOooOOo + o0o00Oo0O . o0o00Oo0O * Oooo0O0oo00oO
def i1iiiIIi11II ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for Ii11i1I11i in Ii11i1I11i :
  o0oooOo0oo = re . compile ( '(.*?)</h2>' ) . findall ( str ( Ii11i1I11i ) )
  for i1iI1IIi1I in o0oooOo0oo :
   i1iI1IIi1I = i1iI1IIi1I
  oo00i1i11I1I1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Ii11i1I11i ) )
  for OOOOOoooO , O0o0OO0000ooo , time , oO0Oooo0OoO in oo00i1i11I1I1 :
   i1i1II1i11 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oO0Oooo0OoO )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + i1iI1IIi1I + ' - ' + OOOOOoooO + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + O0o0OO0000ooo , OO0o , ( str ( i1i1II1i11 ) ) )
   if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . IIi + Ii1I * I1ii11iIi11i
 Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if 61 - 61: IIiIiII11i . iIi1i1ii1 - o0o00Oo0O * iIi1i1ii1
def Iii1I ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 if 100 - 100: ii . I1ii11iIi11i / Ii1I
def I11i1I11iIii ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  O0OOo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   O0OOo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + O0OOo + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  O0OOo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + O0OOo + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
def iIIi11i ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 62 - 62: OOooOOo % OOoOoo * iI11I1II1I1I
 if 38 - 38: Ii . iI11I1II1I1I . Oooo0O0oo00oO / oO0o
 if 18 - 18: I1ii11iIi11i * OooOO000
 if 99 - 99: IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * O0oOO0 / IIiIiII11i % ii
 if 14 - 14: iIi1i1ii1 . iIi1i1ii1 % OOoOoo
 if 42 - 42: I11i . Oooo0O0oo00oO - OOoOoo
 if 33 - 33: IIiIiII11i / o0o00Oo0O / iIi1i1ii1 - oo0oO00 - ooOoO0O00
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  O0OOo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + O0OOo + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
   if 8 - 8: Ii . iiII11i1I1IIi / iI11I1II1I1I / Ii1I / iIi1i1ii1 - IIi
def iI1i1I1iiii1Ii11 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for iIIiii in o00oooO0Oo :
  IiIIIIi = ( iIIiii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I11I ( 'http:' + IiIIIIi )
  if 51 - 51: IIiIiII11i . O0oOO0 . oO0o % IIiIiII11i
  if 41 - 41: OOooOOo - Oooo0O0oo00oO + OOoOoo - ooOoO0O00
  if 6 - 6: IIiIiII11i
  if 7 - 7: ooOoO0O00
def Oo00oo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 8046 , O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def oO0oO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I11I ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 71 - 71: OooOO000 / oOo0O0Ooo / o0o00Oo0O
def IiIii11I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 97 - 97: ooOoO0O00 + iiII11i1I1IIi . OOoOoo - iiII11i1I1IIi
def I1iI ( ) :
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooo0oOOoO000 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 86 - 86: iI11I1II1I1I - oo0oO00 % OOoOoo . Oooo0O0oo00oO * OOooOOo . ooOoO0O00
  if 75 - 75: oo0oO00 + OOoOoo / OOoOoo - Oooo0O0oo00oO * oO0o * OOoOoo
def o0OO0ooOOO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def i1i1I1Ii1IIii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  url = ( url ) . replace ( '\/' , '/' )
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , '' )
  if 80 - 80: Ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIi ( name , url ) :
 iI1iii1iIiiI = 0
 name = name
 url = url
 ii1I = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  I11I ( url )
  if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / Oooo0O0oo00oO
  if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
  if 63 - 63: iIi1i1ii1 + iI11I1II1I1I + oOo0O0Ooo + OooOO000
  if 72 - 72: oO0o + Ii + Ii1I
  if 96 - 96: O0oOO0 % ooOoO0O00 / I11i
  if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + iiII11i1I1IIi
  if 88 - 88: o0o00Oo0O . O0oOO0 % oOo0O0Ooo
  if 10 - 10: oOo0O0Ooo + o0o00Oo0O
def Oooo0Oo00o ( ) :
 OOoO = oo0O0o00o0O ( 'http://documentarylovers.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  if 'genre' in ooO0oOOooOo0 :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , ooO0oOOooOo0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIoO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 13 - 13: ooOoO0O00
def IiiI111 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in o0O0OOO0Ooo :
  i1i1I1Ii1IIii ( url )
  if 55 - 55: iIi1i1ii1 % oO0o - ii - Oooo0O0oo00oO % ii
def Oo00O0O ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11I1II = 'http://documentarylovers.com/?s=' + ( o00oO0 ) . replace ( ' ' , '+' )
 OO0 = i11I1II . lower ( )
 IIoO ( OO0 )
 if 70 - 70: oO0o
def iIiiI1I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def II1i1I1II1IiI ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def I11i1i ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'rtd' in url :
   IIIII11Ii ( url )
   if 33 - 33: O0oOO0 + Ii + ii * iI11I1II1I1I . OOooOOo * IIi
def IIIII11Ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OOoO )
 for O0o0O00Oo0o0 , file in o00oooO0Oo :
  url = ( 'https://rtd.rt.com' + O0o0O00Oo0o0 + file )
  I11I ( url )
  if 99 - 99: ooOoO0O00 % ii * IIi * o0o00Oo0O + O0oOO0
  if 12 - 12: IIi . iiII11i1I1IIi - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
def iii11 ( ) :
 I1 = oo0O0o00o0O ( 'http://www.stream2watch.co/live-tv' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , I1i11IIIi in o00oooO0Oo :
  I1i11111i1i11 ( ( Oo0OO + '[COLOR' + iiI1IiI + ']' + I1i11IIIi + '[/COLOR]' ) , ooO0oOOooOo0 , 8086 , O0o0OO0000ooo )
  if 19 - 19: O0oOO0 * iiII11i1I1IIi + OOooOOo - O0oOO0 + Ii1I
def iIii1ii ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8087 , O0o0OO0000ooo )
  if 24 - 24: ooOoO0O00 / OooOO000 * oo0oO00 / o0o00Oo0O
def OOOOo0oO0o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  iI1iI ( url , Oo0OO )
  if 74 - 74: iIi1i1ii1 - o0o00Oo0O / OooOO000 * IIi % OOoOoo . OooOO000
def iI1iI ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  print url
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
def o00oo ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooO0oOOooOo0 , 3002 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def O000Oo00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def iI1oOoo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 o00O0o00oo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , Oo0OO in o00O0o00oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Season- ' + Oo0OO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def iIiiII ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  iII1I ( url )
def iII1I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11I ( url )
  if 92 - 92: OooOO000 % IIi
def IiI11ii1I ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def Ii1Ii11I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "v.src = '([^']*)';" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  i1I11iIiII ( url )
  if 28 - 28: OOoOoo . ooOoO0O00
def I1I1I1IIi1III ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def o0o00O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'mp4' in url :
   I11I ( url )
 for url in o0O0OOO0Ooo :
  yt . PlayVideo ( url )
  if 46 - 46: OOooOOo
def i1iiII ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooO0oOOooOo0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def ooii ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '(Free Access)' in Oo0OO :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def oOO0O0O0OO00oo ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , O0o0OO0000ooo , iiI11ii1I1 , '' )
  if 39 - 39: iIi1i1ii1 % OOooOOo * Ii1I - ii - I1ii11iIi11i
def Oo0oOOO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  o00OoOooo ( 'http://watchxxxfree.com/categories' )
 if O0oO0 == 1 :
  i1I1ii1 ( 'http://www.perfectgirls.net' )
 if O0oO0 == 2 :
  Iii1i ( 'http://www.xvideos.com/best' )
 if O0oO0 == 3 :
  ooOooo00O ( 'http://www.xvideos.com/best' )
 if O0oO0 == 4 :
  Iii1i ( 'http://www.xvideos.com/best' )
 if O0oO0 == 5 :
  Iii1i ( 'http://www.xvideos.com/verified/videos' )
 if O0oO0 == 6 :
  I1i1I1IIiIIi ( 'http://www.xvideos.com/tags' )
 if O0oO0 == 7 :
  iII1ii1IIII ( 'http://www.xvideos.com/porn' )
 if O0oO0 == 8 :
  Oo0o0O0OOOo0 ( )
  if 4 - 4: OOoOoo + o0o00Oo0O . ooOoO0O00 * Ii1I - I11i
  if 42 - 42: I11i * OOooOOo . oO0o - iiII11i1I1IIi / IIiIiII11i
  if 25 - 25: I1ii11iIi11i % OOooOOo
  if 75 - 75: ooOoO0O00
  if 74 - 74: I1ii11iIi11i + OooOO000 - O0oOO0 - oO0o + iiII11i1I1IIi - iI11I1II1I1I
  if 54 - 54: Ii1I + IIiIiII11i . oOo0O0Ooo / oO0o . OOoOoo
  if 58 - 58: iIi1i1ii1 % Ii * IIiIiII11i . Ii1I
  if 94 - 94: Ii . Oooo0O0oo00oO + iI11I1II1I1I * OooOO000 * OooOO000
  if 36 - 36: oo0oO00 - iIi1i1ii1 . iIi1i1ii1
def Oo0OOOO0oOoo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if 'ch' in url :
   ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def O0OIIII1i ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 i1I1Iiii = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for Oo0OO , url in i1I1Iiii :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def I1iIIIiiii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   I1111 ( url )
def o00oO0o0oo0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I11I ( url )
def o00OoOooo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , IIiI1I1 in o00oooO0Oo :
  if 'category' in url :
   ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   ' + IIiI1I1 + '[/COLOR]' , url , 90006 , O0o0OO0000ooo , oOOOo00O00oOo + 'Jizbox.png' , '' )
def Ooo00OOo000 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 i1I1Iiii = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , O0o0OO0000ooo , '' , '' )
 for url in i1I1Iiii :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def i1ooOO00o0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   I1111 ( url )
def I1111 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I11I ( url )
def i1I1ii1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , IIiI1I1 in o00oooO0Oo :
  if 'category' in url :
   ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]' + IIiI1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def Ii1I1iIiiI1 ( url ) :
 I1 = O0 ( url )
 OooiiIi1i = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I1Iiii = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , O0o0OO0000ooo , '' , '' )
 for url in i1I1Iiii :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , OooiiIi1i + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def o00i111iiIiiIiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in o00oooO0Oo :
  OOooooO ( 'http://www.perfectgirls.net' + url )
def OOooooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I11I ( 'http://' + url )
def iII1ii1IIII ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , IIiI1I1 in o00oooO0Oo :
  ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + IIiI1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def I1i1I1IIiIIi ( url ) :
 I1 = O0 ( url )
 i1I1Iiii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in i1I1Iiii :
  ii1II1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , IIiI1I1 in o00oooO0Oo :
  ii1II1II ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + ( IIiI1I1 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 80 - 80: OOooOOo + iI11I1II1I1I . iIi1i1ii1
def ooOoOoo000O0O ( url ) :
 I1 = O0 ( url )
 i1I1Iiii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in i1I1Iiii :
  ii1II1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , OOoo0oOO00 in o00oooO0Oo :
  ii1II1II ( Oo0OO + '--' + ( OOoo0oOO00 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( O0o0OO0000ooo ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 42 - 42: I11i / iIi1i1ii1
  if 79 - 79: IIi
def Iii1i ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , o0Oo0 , iII1i1 in o00oooO0Oo :
  ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + iII1i1 + ' - [COLORred]' + o0Oo0 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , O0o0OO0000ooo , O0o0OO0000ooo , iII1i1 + ' - ' + o0Oo0 )
 IIIii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in IIIii :
  ii1II1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 63 - 63: oOo0O0Ooo - Ii - iiII11i1I1IIi % oo0oO00 . IIi * Ii1I
def ooOooo00O ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 i1I1Iiii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in i1I1Iiii :
  ii1II1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Ii11i1I11i ) )
 for url , Oo0OO in o00oooO0Oo :
  if '/c/' in url :
   ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 66 - 66: ii + I11i . ooOoO0O00 * iiII11i1I1IIi
   if 92 - 92: oo0oO00 / OooOO000
def Oo0o0O0OOOo0 ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIIiii1iii1I = ( o00oO0 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OO0 = iiIIiii1iii1I . lower ( )
 oOOoooO0O0 = 'http://www.xvideos.com/?k=' + OO0
 print oOOoooO0O0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O0 ( oOOoooO0O0 )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , o0Oo0 , iII1i1 in o00oooO0Oo :
  ii1II1II ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + iII1i1 + ' - [COLORred]' + o0Oo0 + '[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10108 , O0o0OO0000ooo , O0o0OO0000ooo , iII1i1 + ' - ' + o0Oo0 )
 IIIii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for ooO0oOOooOo0 in IIIii :
  ii1II1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 14 - 14: o0o00Oo0O / oo0oO00 . oO0o % iiII11i1I1IIi . O0oOO0
def IiIiiIiiiiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 o0OOo00OoO = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'http' in url :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in o0O0OOO0Ooo :
  if 'http' in url :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in o0OOo00OoO :
  if 'http' in url :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 48 - 48: OOoOoo . Ii1I
def IiiIIIIi ( url ) :
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 import urlresolver
 try : O00oo . play ( url )
 except : pass
 if 23 - 23: ooOoO0O00 + Ii1I + oOo0O0Ooo - OOoOoo % ii . iIi1i1ii1
 if 49 - 49: O0oOO0 . OOooOOo
def O0ooiIIi1 ( ) :
 if 76 - 76: oOo0O0Ooo - oOo0O0Ooo - I11i % OOoOoo * o0o00Oo0O
 if 11 - 11: IIi + oo0oO00 . oO0o . Ii * oO0o
 if 18 - 18: oo0oO00 + I1ii11iIi11i - oO0o / OooOO000 / Oooo0O0oo00oO
 if 53 - 53: Oooo0O0oo00oO + I11i . O0oOO0 / oo0oO00
 if 52 - 52: OooOO000 + OooOO000
 if 73 - 73: I11i . Ii % ii + OOoOoo . ii / Oooo0O0oo00oO
 if 54 - 54: OOooOOo . ii
 if 36 - 36: O0oOO0 / IIiIiII11i * iIi1i1ii1 % Ii1I
 if 31 - 31: IIiIiII11i + Oooo0O0oo00oO - ii . oo0oO00
 if 28 - 28: IIi . Ii1I
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def oOo000Oo00o ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def o0ooOOoOoOO ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 iII11 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo in iII11 :
  O0o0OO0000ooo = O0o0OO0000ooo
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 96 - 96: oo0oO00 * Ii1I * IIi + Ii1I % oOo0O0Ooo + Ii
def i1iI11Ii1i ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . OooOO000 / O0oOO0
  if 4 - 4: Ii + Oooo0O0oo00oO
  if 26 - 26: iiII11i1I1IIi * OooOO000 * O0oOO0 * OOooOOo
  if 48 - 48: iiII11i1I1IIi % Ii . ii * iIi1i1ii1 % oO0o . iiII11i1I1IIi
IiOOo0 = '{PQ},' ; o0O0O0O00o = '{SC},' ; OoOooOo00o = '{XG},' ; iI1IIi = '{JP},' ; II11 = '{HW},' ; oo0o0O = '{RT},'
def Ooo00Oo ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 ooo0ooooo0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - iiII11i1I1IIi - Ii
 OO0OO0OO = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oo0O00o0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 Oo0oOooOooO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ii1I1iIII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIii1 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o00oO0
 II1iII1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I11II11IiI11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 O00o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii11Iiii1iiii = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 10 - 10: iiII11i1I1IIi % I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 48 - 48: Oooo0O0oo00oO + OooOO000 % Oooo0O0oo00oO
 if 84 - 84: o0o00Oo0O % IIi . IIi . iiII11i1I1IIi * oo0oO00
 Iiii = Oo0OoO00oOO0o ( OO0OO0OO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( oo0O00o0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIOO0O = Oo0OoO00oOO0o ( Oo0oOooOooO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 I11IiiiII = Oo0OoO00oOO0o ( IIii1 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oO0o0 = Oo0OoO00oOO0o ( II1iII1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1Ii1i11ii = Oo0OoO00oOO0o ( I11II11IiI11 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0O0oo = Oo0OoO00oOO0o ( O00o )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 OOOOOOO00OO = Oo0OoO00oOO0o ( Ii11Iiii1iiii )
 if 68 - 68: oOo0O0Ooo
 if 94 - 94: iiII11i1I1IIi / OOooOOo % IIiIiII11i . iI11I1II1I1I
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for i1iIi1IiIiiI , Oo0OO in o00oooO0Oo :
   if o00oO0 in Oo0OO . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooO0oOOooOo0 + i1iIi1IiIiiI ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 60 - 60: oo0oO00 . o0o00Oo0O / o0o00Oo0O
    if 73 - 73: IIiIiII11i + Oooo0O0oo00oO * iiII11i1I1IIi / iiII11i1I1IIi
    if 74 - 74: o0o00Oo0O + iI11I1II1I1I + O0oOO0 * iIi1i1ii1
    if 39 - 39: OooOO000 . oO0o % OOoOoo . Oooo0O0oo00oO / iiII11i1I1IIi * oO0o
    if 12 - 12: oOo0O0Ooo / I11i
    if 86 - 86: I1ii11iIi11i % OOooOOo
    if 77 - 77: IIi % Oooo0O0oo00oO / O0oOO0
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for i1iIi1IiIiiI , Oo0OO in o0OOo00OoO :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OO0OO0OO + i1iIi1IiIiiI ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  OOoOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in OOoOo :
   if o00oO0 in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 27 - 27: oOo0O0Ooo * Ii / o0o00Oo0O / IIiIiII11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iIOO0O != 'Failed' :
  OOoO0oOOO = [ ]
  I11iIIIIi1Iii1iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIOO0O )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in I11iIIIIi1Iii1iIi :
   if o00oO0 in Oo0OO . lower ( ) :
    if Oo0OO in OOoO0oOOO :
     pass
    else :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
     OOoO0oOOO . append ( Oo0OO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I11IiiiII != 'Failed' :
  ii1IIi1iI1ii1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( I11IiiiII )
  for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in ii1IIi1iI1ii1 :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooO0oOOooOo0 , 7067 , O0o0OO0000ooo )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 58 - 58: IIi . oo0oO00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 41 - 41: oO0o % oOo0O0Ooo - I1ii11iIi11i
    if 11 - 11: IIi * I11i / iIi1i1ii1 + OOooOOo + oO0o % OooOO000
    if 18 - 18: oOo0O0Ooo - OOooOOo
    if 18 - 18: Oooo0O0oo00oO + oO0o * O0oOO0 - O0oOO0 . Ii1I * oo0oO00
    if 95 - 95: Ii1I / OOooOOo
    if 10 - 10: iIi1i1ii1 % Ii1I - iIi1i1ii1
    if 86 - 86: I1ii11iIi11i
    if 88 - 88: OooOO000 * oOo0O0Ooo
    if 30 - 30: OOooOOo / O0oOO0 / IIi * I11i * O0oOO0 . oOo0O0Ooo
 if i1Ii1i11ii != 'Failed' :
  o0oo000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Ii1i11ii )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in o0oo000 :
   if o00oO0 in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 87 - 87: oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if oO0O0oo != 'Failed' :
  I1Io0oO00O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0O0oo )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in I1Io0oO00O :
   if o00oO0 in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 72 - 72: oO0o - iI11I1II1I1I . iiII11i1I1IIi / IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 12 - 12: oOo0O0Ooo + OooOO000
 if OOOOOOO00OO != 'Failed' :
  oOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOOOO00OO )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , Oo0OO in oOo :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 90 - 90: IIiIiII11i / oO0o / IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 oOoo0ooOoo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 70 - 70: IIi - IIiIiII11i . I1ii11iIi11i / I1ii11iIi11i
 for Ii11iiI in oOoo0ooOoo :
  o0OO0oooo = oOOoo0Oo + Ii11iiI + IIIII
  III = Oo0OoO00oOO0o ( o0OO0oooo )
  if III != 'Failed' :
   i1iiIIiiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III )
   for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in i1iiIIiiiI :
    if o00oO0 in Oo0OO . lower ( ) :
     o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 26 - 26: OOoOoo % O0oOO0 + oOo0O0Ooo / iIi1i1ii1 . oOo0O0Ooo
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 38 - 38: ii + ii - Ii * oOo0O0Ooo * ooOoO0O00 / IIiIiII11i
 oOoo0ooOoo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 78 - 78: I1ii11iIi11i - OooOO000 + iiII11i1I1IIi * IIi * I11i
 if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 for Ii11iiI in oOoo0ooOoo :
  o0OO0oooo = ooo0ooooo0o + Ii11iiI
  iI111iIi = Oo0OoO00oOO0o ( o0OO0oooo )
  if iI111iIi != 'Failed' :
   IIi1IiIIii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( iI111iIi )
   for i1iIi1IiIiiI , Oo0OO in IIi1IiIIii :
    if o00oO0 in Oo0OO . lower ( ) :
     OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( ooo0ooooo0o + Ii11iiI + i1iIi1IiIiiI ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 84 - 84: OooOO000
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 53 - 53: ooOoO0O00
     if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
def o00o0 ( ) :
 if 9 - 9: ooOoO0O00 - OOooOOo
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 if 57 - 57: iI11I1II1I1I * IIi * iiII11i1I1IIi / O0oOO0
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( o00oO0 ) . replace ( ' ' , '%20' )
 OooiiIi1i = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 OO0OO0OO = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 oo0O00o0 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Oo0oOooOooO = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OO0 ) . replace ( ' ' , '+' )
 ii1I1iIII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IIii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 II1iII1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIIiII1i1ii = ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vY2FycmVyYS9zb3VyY2VfZmlsZTIucGhw' ) )
 if 57 - 57: OOoOoo + OooOO000
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 49 - 49: OOooOOo * ii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( OooiiIi1i )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = Oo0OoO00oOO0o ( OO0OO0OO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( oo0O00o0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iIOO0O = cloudflare . source ( Oo0oOooOooO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 iI111iIi = Oo0OoO00oOO0o ( ii1I1iIII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 I11IiiiII = Oo0OoO00oOO0o ( IIii1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0o0 = Oo0OoO00oOO0o ( II1iII1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 III = Oo0OoO00oOO0o ( iIIiII1i1ii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 10/9 Links" )
 if 7 - 7: OooOO000 / O0oOO0 + I11i
 if oO0o0 != 'Failed' :
  IiIiIiiIIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0o0 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in IiIiIiiIIii :
   if OO0 in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
    if 77 - 77: O0oOO0 * OOoOoo . Oooo0O0oo00oO * IIi % IIiIiII11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if I11IiiiII != 'Failed' :
  ii1IIi1iI1ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11IiiiII )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in ii1IIi1iI1ii1 :
   if OO0 in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 75 - 75: I1ii11iIi11i + IIi + oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 97 - 97: OOoOoo % Ii % oo0oO00
    if 21 - 21: I1ii11iIi11i / IIi / Ii1I / ooOoO0O00 / I11i
    if 86 - 86: ooOoO0O00
    if 33 - 33: OOooOOo % Ii * Oooo0O0oo00oO
    if 69 - 69: IIiIiII11i + I1ii11iIi11i - O0oOO0 . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
    if 75 - 75: oO0o % ii
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 16 - 16: o0o00Oo0O / ooOoO0O00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   if OO0 in Oo0OO . lower ( ) :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , O0o0OO0000ooo , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 58 - 58: I11i / Ii / o0o00Oo0O % oo0oO00 % oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 86 - 86: iIi1i1ii1 + OOooOOo / oOo0O0Ooo + oo0oO00 % oo0oO00 / Ii
    if 12 - 12: OOooOOo + I11i . OooOO000
    if 52 - 52: oO0o
    if 4 - 4: IIi % Ii1I + oo0oO00 - Ii1I
    if 98 - 98: IIi - o0o00Oo0O * O0oOO0 * IIi * IIi
    if 44 - 44: iIi1i1ii1 + oo0oO00
    if 66 - 66: O0oOO0
    if 34 - 34: iiII11i1I1IIi % Ii + Ii - iiII11i1I1IIi
    if 2 - 2: IIiIiII11i + ooOoO0O00
    if 68 - 68: Oooo0O0oo00oO + IIi
    if 58 - 58: iIi1i1ii1 * IIi . ooOoO0O00
    if 19 - 19: O0oOO0
    if 85 - 85: OOoOoo - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
    if 94 - 94: iI11I1II1I1I + iIi1i1ii1
    if 44 - 44: oO0o + oo0oO00 % oO0o + ooOoO0O00 + iiII11i1I1IIi + o0o00Oo0O
    if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % O0oOO0 + oOo0O0Ooo % OOoOoo / IIi
    if 36 - 36: OOooOOo . Ii
    if 81 - 81: I1ii11iIi11i * iiII11i1I1IIi * oO0o
    if 85 - 85: o0o00Oo0O * O0oOO0
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for Oo0OO in o0OOo00OoO :
   if OO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0OO0OO + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  OOoOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for Oo0OO in OOoOo :
   if OO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo0O00o0 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 25 - 25: ii . IIi % iiII11i1I1IIi . iIi1i1ii1
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iIOO0O != 'Failed' :
  I11iIIIIi1Iii1iIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIOO0O )
  for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in I11iIIIIi1Iii1iIi :
   if OO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source - Dizi[/COLOR]' , ooO0oOOooOo0 , 8062 , O0o0OO0000ooo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 67 - 67: ii + OooOO000 / OOoOoo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iI111iIi != 'Failed' :
  IIi1IiIIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI111iIi )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in IIi1IiIIii :
   if OO0 in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- Source Scooby[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 75 - 75: iIi1i1ii1 / ii . oOo0O0Ooo + OooOO000 - IIiIiII11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: iIi1i1ii1 / iIi1i1ii1 . Ii * Ii1I + I11i
 ii1iI11IiIIi = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if iI111iIi != 'Failed' :
  for Ii11iiI in ii1iI11IiIIi :
   o0OO0oooo = oOOoo0Oo + Ii11iiI + IIIII
   oO0O0oo = O0 ( o0OO0oooo )
   if oO0O0oo != 'Failed' :
    I1Io0oO00O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0O0oo )
    for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in I1Io0oO00O :
     if OO0 in Oo0OO . lower ( ) :
      I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 47 - 47: Oooo0O0oo00oO . O0oOO0 + OOooOOo % iIi1i1ii1 % ooOoO0O00 / iI11I1II1I1I
      Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if III != 'Failed' :
  i1iiIIiiiI = re . compile ( 'url="([^"]*)">name=".+?"' ) . findall ( III )
  for ooIii in i1iiIIiiiI :
   o0OO00oOOO0o0 = O0 ( ooIii )
   OooOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0OO00oOOO0o0 )
   for OooiiIi1i , Oo0OO in OooOo :
    OO0OO0OO = ooIii + OooiiIi1i
    if '..' in OO0OO0OO :
     pass
    elif 'rar' in OO0OO0OO :
     pass
    elif 'srt' in OO0OO0OO :
     pass
    elif '../' in OO0OO0OO :
     pass
    elif '.jpg' in OooiiIi1i :
     pass
    elif 'C=' in OooiiIi1i :
     pass
    elif '/' in OooiiIi1i :
     iiii = O0 ( OO0OO0OO )
     oOOOO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiii )
     if 82 - 82: ooOoO0O00 + I11i - IIiIiII11i . IIi
    if OO0 in Oo0OO . lower ( ) :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
     if 93 - 93: IIiIiII11i * OOooOOo % I11i
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 67 - 67: I11i + I1ii11iIi11i . OOoOoo - ooOoO0O00 . OOooOOo
     if 12 - 12: iIi1i1ii1 / oO0o / o0o00Oo0O * iIi1i1ii1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0oo0OOo0O0 ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o00oO0 ) . replace ( ' ' , '+' )
 if 37 - 37: I11i * I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 11 - 11: O0oOO0
 if I1 != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
   if o00oO0 in Oo0OO . lower ( ) :
    OOoOOO0 ( ( Oo0OO + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + ooO0oOOooOo0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 62 - 62: ii % O0oOO0 * IIiIiII11i * OooOO000 * OooOO000 / OOoOoo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
o0oI1I1i = '{ZH},' ; i111i1IIi1i = '{IX},' ; oo00oO00oooo = '{LM},'
if 63 - 63: IIiIiII11i - oo0oO00 . OOooOOo
def IIi1I1iII111 ( url ) :
 o0OoO00OO0o0ooO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( o0OoO00OO0o0ooO )
 for url , i1i11I1I1iii1 , iIi1IiI , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( i1i11I1I1iii1 ) . replace ( 'Sezon' , ' Season ' ) + ( iIi1IiI ) . replace ( 'Bölüm' , ' Episode ' ) + Oo0OO , url , 8063 , '' )
  if 42 - 42: o0o00Oo0O * iiII11i1I1IIi . OOooOOo / Oooo0O0oo00oO - IIi . oo0oO00
  if 57 - 57: I11i + I1ii11iIi11i * Ii1I - OOoOoo % iI11I1II1I1I - IIi
  if 37 - 37: oO0o * oo0oO00 + IIi + Ii1I * I11i
  if 95 - 95: IIi - Ii % Ii - o0o00Oo0O * OooOO000
def Oo0O0oOoO0o0 ( url ) :
 o0OoO00OO0o0ooO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0OoO00OO0o0ooO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 222 , '' )
  if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + iiII11i1I1IIi % oOo0O0Ooo * O0oOO0
  if 74 - 74: iiII11i1I1IIi / oo0oO00 . oOo0O0Ooo - ii + IIiIiII11i + oo0oO00
  if 36 - 36: IIi * oOo0O0Ooo * Ii1I . oo0oO00 * Ii1I
  if 76 - 76: Oooo0O0oo00oO + o0o00Oo0O / iIi1i1ii1 - oO0o
def II1i111i ( ) :
 if 58 - 58: OOoOoo
 o0OoO00OO0o0ooO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o0OoO00OO0o0ooO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , iIi1IiI in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO + '  -  ' + ( iIi1IiI ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 8063 , O0o0OO0000ooo )
  if 45 - 45: I11i
def o00ooOo ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8002 , O0o0OO0000ooo )
def iIoOO0OO00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , time , url , Oo0OO , iIIiI11i1I11 in o00oooO0Oo :
  I1IiiiiI ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , time ) , url , 1015 , O0o0OO0000ooo , iIIiI11i1I11 )
  if 75 - 75: iiII11i1I1IIi * I1ii11iIi11i / OooOO000 * I1ii11iIi11i / OOoOoo
def IiIi11IIi1I11 ( ) :
 if 65 - 65: OOooOOo * o0o00Oo0O - OOooOOo - oO0o
 I1i11111i1i11 ( 'Coronation Street' , '' , 8001 , '' )
 I1i11111i1i11 ( 'Eastenders' , '' , 8002 , '' )
 I1i11111i1i11 ( 'Emmerdale' , '' , 8003 , '' )
 I1i11111i1i11 ( 'Hollyoaks' , '' , 8004 , '' )
 I1i11111i1i11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 96 - 96: Ii1I - o0o00Oo0O
 if 35 - 35: Oooo0O0oo00oO . oo0oO00 . OooOO000 - oo0oO00 % oo0oO00 + OooOO000
 if 99 - 99: I11i + Oooo0O0oo00oO
 if 34 - 34: OooOO000 * I11i . oOo0O0Ooo % Ii
def Oo0OO0 ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Holly' in Oo0OO :
   O0o0OO0000ooo = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 74 - 74: IIi - ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 19 - 19: iI11I1II1I1I + OooOO000 . OooOO000 - I1ii11iIi11i
def IIiIIiIi1II1IiI ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'East' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 99 - 99: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: Ii - Ii + Ii1I * OOoOoo * O0oOO0 / ii
def i1II111ii1ii ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Emmer' in Oo0OO :
   O0o0OO0000ooo = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 54 - 54: iiII11i1I1IIi * IIiIiII11i / ii + OooOO000 - O0oOO0 + OOoOoo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: I11i * oO0o + Ii1I . I1ii11iIi11i + iiII11i1I1IIi / ii
def i11111iIIiII ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Coro' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 54 - 54: ooOoO0O00 - oO0o / ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
def o000Oo0oO0OO0 ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Celeb' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 54 - 54: oOo0O0Ooo
def I1OoO00o00 ( name , url ) :
 ooOoo0oo00000O = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOoo0oo00000O :
  oo0o0Oo00o0 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOoO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OOoO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOoO = open_url ( url )
  i11II = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OOoO ) [ - 1 ]
  oo0o0Oo00o0 = i11II . replace ( '\\/' , '/' )
 OooOo00o = xbmcgui . ListItem ( name , '' , '' )
 OooOo00o . setPath ( oo0o0Oo00o0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooOo00o )
 if 63 - 63: oO0o % ooOoO0O00 - O0oOO0
 if 12 - 12: ii + OooOO000 / Oooo0O0oo00oO / I1ii11iIi11i * IIiIiII11i - Ii1I
def i11IIi1Iii1 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 19 - 19: ooOoO0O00 % oO0o - Ii1I . OooOO000 . IIi
def iI1I1 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Movies' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooO0oOOooOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def oOOo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 30 - 30: ii
  if 20 - 20: iIi1i1ii1 + ooOoO0O00 . Ii1I - iI11I1II1I1I
def oO00Oooo0O0o0 ( url ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , O0o0OO0000ooo in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , O0o0OO0000ooo )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
oOOOo0Oooo = '{UJ},' ; I1iiIIiI11I = '{WE},' ; I11II1I = '{WP},' ; oOoOo000 = '{PP},'
def iiI1IiI1I1I ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , O0o0OO0000ooo in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0o0OO0000ooo )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIiI1i ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  i1II ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1II ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . Oooo0O0oo00oO
 if 31 - 31: O0oOO0 % ooOoO0O00 . ii - I11i + ii
 if 45 - 45: Oooo0O0oo00oO + oo0oO00 / ii - IIi + ii
def ii1i1I1111ii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '(cooltvseries.com)' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , Oo0OO in o0O0OOO0Ooo :
  if '(cooltvseries.com)' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def oo0ooo0O0O0O ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11I ( ( url ) . replace ( ' ' , '%20' ) )
oO0iIiII111 = '{XX},' ; OO0iii111 = '{UD},' ; o00O000oooOo = '{YT},' ; O0o00oO0o0 = '{JS},' ; iiiI1I1iiiII = '{PF},'
if 5 - 5: OOooOOo % Ii1I . OOoOoo . oo0oO00 - Ii
def Ii11I1 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( ooO0oOOooOo0 ) ) , 222 , O0o0OO0000ooo )
  if 86 - 86: oOo0O0Ooo + oo0oO00 * OOooOOo - OooOO000 / OooOO000
def iiIIi ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  if 'youtu' in url :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 9 - 9: I11i / iiII11i1I1IIi . iI11I1II1I1I % o0o00Oo0O
def i11ii11IiI1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 47 - 47: iI11I1II1I1I % oo0oO00 . oo0oO00 / o0o00Oo0O . Ii * IIi
def iio0Oo ( url ) :
 OOoO = O0
 o00oooO0Oo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , O0o0OO0000ooo )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . OOoOoo
  if 70 - 70: ii . OOoOoo / O0oOO0 . O0oOO0 - I11i
  if 29 - 29: oo0oO00 % Oooo0O0oo00oO - OOoOoo
  if 26 - 26: o0o00Oo0O . oo0oO00 + iiII11i1I1IIi - IIi . oo0oO00
  if 2 - 2: Ii1I . I1ii11iIi11i * Oooo0O0oo00oO % IIiIiII11i . iiII11i1I1IIi
def II1i1iI ( ) :
 if 5 - 5: OOooOOo + iiII11i1I1IIi * OOoOoo
 I1i11111i1i11 ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 I1i11111i1i11 ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . OOoOoo / I1ii11iIi11i - Ii
 if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
def i1IiI ( Cat_Name ) :
 if 73 - 73: ii * o0o00Oo0O * OOoOoo
 iii11Ii = False
 i1Iiii111 = '0'
 if Cat_Name == 'All Channels' : iii11Ii = True
 if Cat_Name == 'Entertainment' : i1Iiii111 = '1'
 if Cat_Name == 'Movies' : i1Iiii111 = '2'
 if Cat_Name == 'Music' : i1Iiii111 = '3'
 if Cat_Name == 'News' : i1Iiii111 = '4'
 if Cat_Name == 'Sports' : i1Iiii111 = '5'
 if Cat_Name == 'Documentary' : i1Iiii111 = '6'
 if Cat_Name == 'Kids' : i1Iiii111 = '7'
 if Cat_Name == 'Food' : i1Iiii111 = '8'
 if Cat_Name == 'Religious' : i1Iiii111 = '9'
 if Cat_Name == 'USA Channels' : i1Iiii111 = '10'
 if Cat_Name == 'Other' : i1Iiii111 = '11'
 if 37 - 37: oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * OOoOoo * IIi
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoO )
 print 'Len Match: >>>' + str ( len ( o00oooO0Oo ) )
 for Oo0OO , O0o0OO0000ooo , OoooO in o00oooO0Oo :
  oo0OOoOo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0o0OO0000ooo ) . replace ( '\\' , '' )
  if OoooO == i1Iiii111 :
   I1i11111i1i11 ( Oo0OO , '' , 7022 , oo0OOoOo0 )
  elif iii11Ii == True :
   I1i11111i1i11 ( Oo0OO , '' , 7022 , oo0OOoOo0 )
  else : pass
  if 63 - 63: OOooOOo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: IIiIiII11i * IIi + IIiIiII11i % iiII11i1I1IIi . ooOoO0O00 . O0oOO0
def Iiii1II ( Search_Name ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , ooO0oOOooOo0 , OooiiIi1i , OO0OO0OO in o00oooO0Oo :
  oo0OOoOo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0o0OO0000ooo ) . replace ( '\\' , '' )
  OOoOOO0 ( Search_Name + ': Link 1' , ( ooO0oOOooOo0 ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  OOoOOO0 ( Search_Name + ': Link 2' , ( OooiiIi1i ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  OOoOOO0 ( Search_Name + ': Link 3' , ( OO0OO0OO ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  if 83 - 83: Ii1I * oo0oO00 . ii % IIi
def I1iiiiI ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def o0oOOO0 ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def i1Iii ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 96 - 96: iIi1i1ii1
def o0OOO ( url ) :
 url
 iII1111III1I = xbmcgui . ListItem ( Oo0OO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1111III1I )
 return
 if 40 - 40: Ii * IIiIiII11i
 if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def O00O ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOoO )
 for url , o0o0oOoOO0O , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , ( o0o0oOoOO0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 42 - 42: I11i + O0oOO0 - ii + iiII11i1I1IIi % oO0o
def IiIIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , o0o0oOoOO0O , O0o0OO0000ooo in o00oooO0Oo :
  o0OIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , o0o0oOoOO0O )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 oooo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for ooiIi11i1I11Ii in oooo :
  iiIiI1i1 = ( ooiIi11i1I11Ii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IiiiiI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , iiIiI1i1 )
  if 59 - 59: Ii - oo0oO00
def oooO00oOOooO ( INFO ) :
 OOOiiiiI ( 'info for workout' , INFO )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
 if 3 - 3: I11i - ii + iiII11i1I1IIi . oo0oO00
 if 88 - 88: oo0oO00 - iiII11i1I1IIi
def OOoOO0oOooo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( Oo0OO ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def i1II11II11 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def oooiiI11 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   OOoOOO0 ( ( Oo0OO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def i11IiIiii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   OOoOOO0 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 15 - 15: OOoOoo * iI11I1II1I1I * O0oOO0
   if 96 - 96: OooOO000 * iI11I1II1I1I / OOooOOo % Oooo0O0oo00oO * IIiIiII11i
   if 3 - 3: Oooo0O0oo00oO . I1ii11iIi11i / Ii + oO0o
   if 47 - 47: iIi1i1ii1 . Oooo0O0oo00oO
   if 96 - 96: oo0oO00 % IIiIiII11i / OOoOoo % Oooo0O0oo00oO / OOoOoo % Ii
def O0000ooO ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 o00oooO0Oo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Daily' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 9008 , Ooo )
def O00OoO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def I11i11 ( url ) :
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 68 - 68: o0o00Oo0O * iI11I1II1I1I / OooOO000
def o00O00oO ( ) :
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '.m3u' in ooO0oOOooOo0 :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + ooO0oOOooOo0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def OO000O000OOO ( url ) :
 OOoO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 26 - 26: oo0oO00 * IIi % oOo0O0Ooo + iiII11i1I1IIi
def IIIIiIiIi1 ( ) :
 OOoO = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'category' in ooO0oOOooOo0 :
   I1i11111i1i11 ( Oo0OO , 'http://www.disclose.tv/' + ooO0oOOooOo0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 38 - 38: iiII11i1I1IIi - I1ii11iIi11i / IIi + O0oOO0 . iiII11i1I1IIi + iIi1i1ii1
   if 19 - 19: IIi
def oo0iIi1iiii1ii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://www.disclose.tv/' + url , 7011 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
  if 21 - 21: OOooOOo - Ii - OOooOOo
def i1oo0OO0Oo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OOoO )
 o0OOo00OoO = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'http' in url :
   OOoOOO0 ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , Oo0OO in o0O0OOO0Ooo :
  OOoOOO0 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in o0OOo00OoO :
  OOoOOO0 ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 4 - 4: OOooOOo * o0o00Oo0O - oo0oO00
  if 72 - 72: oo0oO00 + OOoOoo / oOo0O0Ooo . iIi1i1ii1 % oO0o / Ii
def I1III1I1IiI ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def iiIi1111iiI1 ( name , url , img ) :
 I1 = O0 ( url )
 o00oo00 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 o0oO0O = len ( o00oo00 )
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: OooOO000 + iIi1i1ii1 * iI11I1II1I1I
 if o0oO0O == 1 :
  for II1Iii1iI in o00oo00 :
   II1Iii1iI = II1Iii1iI . replace ( 'player' , 'watch' )
   oo0iiIIi1i111i = II1Iii1iI + '&fv=&sou='
   iIIOoO = O0 ( oo0iiIIi1i111i )
   o0Oo00Oo = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iIIOoO )
   for oooOooooO0oOO in o0Oo00Oo :
    i11i11I = False
    Resolve ( oooOooooO0oOO )
    if 61 - 61: iI11I1II1I1I % IIi - O0oOO0 * ii % IIiIiII11i - IIi
 elif o0oO0O > 1 :
  if 44 - 44: o0o00Oo0O
  for II1Iii1iI in o00oo00 :
   IIIi1iIii1II11 = O0 ( II1Iii1iI )
   OOOOoOOOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIIi1iIii1II11 )
   iiIi1 = OOOOoOOOO
   iiIi1 = ( str ( iiIi1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iiIi1
   OOoOOO0 ( 'DOUBLE LINK' , iiIi1 , 424 , '' )
   if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
   for url in OOOOoOOOO :
    I1i11111i1i11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OooiiIi1i = Google . resolve ( url )
    except :
     pass
    try :
     Oo0o0OOo0Oo0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OooiiIi1i ) )
     for O00ooOoO , oo000oo00 in Oo0o0OOo0Oo0 :
      if 46 - 46: IIiIiII11i - ii - oO0o . Ii1I * I1ii11iIi11i + iI11I1II1I1I
      HD_URLS . append ( O00ooOoO )
      SD_URLS . append ( oo000oo00 )
    except :
     pass
 else :
  pass
  if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
def I1i1IiIIiIiII ( ) :
 if 27 - 27: ii * oOo0O0Ooo - iiII11i1I1IIi / iiII11i1I1IIi
 if 21 - 21: o0o00Oo0O * OOoOoo % OOooOOo / o0o00Oo0O
 I1i11111i1i11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 85 - 85: ii + ii
 I1i11111i1i11 ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / oo0oO00 . oO0o
def oOOo0O0Oo ( ) :
 OOoO = O0 ( 'http://cnfstudio.com/' )
 o00oooO0Oo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://cnfstudio.com/genre/' + ooO0oOOooOo0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 50 - 50: O0oOO0 * oo0oO00 + Oooo0O0oo00oO - I1ii11iIi11i
iI111I11I1I1 = xbmcgui . Dialog ( )
if 79 - 79: oO0o / ooOoO0O00
iIi1i1I1I = '{UN},' ; i11iiiI = '{IG},' ; o0OO = '{PL},' ; OO0o0o0oo0Oo0 = '{LO},' ; IiIii111iI11i = '{LP},' ; ooo0ooO00o = '{HA},' ; o0OOii = '{XD},' ; IIiiiiiI1iIi = '{TA},' ; IIIII11II1 = '{DP},' ; OOOO0oOO = '{JT},' ; IIIiii = '{JJ},' ; I11OoooO = '{MM},' ; i1IIi11 = '{FQ},' ; oOIIIII11 = '{HH},'
if 48 - 48: OooOO000 / OOoOoo . iI11I1II1I1I
def ooo0OOoo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOoO )
 oO0o00O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , O0o0OO0000ooo )
 oO0o00O = oO0o00O
 for url in oO0o00O :
  I1i11111i1i11 ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 7 - 7: I1ii11iIi11i * oO0o - IIiIiII11i % OooOO000 . I1ii11iIi11i . I1ii11iIi11i
def iiII1iIi1ii1i ( url ) :
 if 49 - 49: OOooOOo
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  O0o0O00Oo0o0 = url + '&fv=&sou='
  O0o0O00Oo0o0 = O0o0O00Oo0o0 . replace ( 'player' , 'watch' )
  OoO0O00 = o00oOO00 ( O0o0O00Oo0o0 )
  O0o0Oo0o00o = o00oOO00 ( url )
  if 60 - 60: iiII11i1I1IIi / iiII11i1I1IIi - OOoOoo / ii + o0o00Oo0O
  if 55 - 55: oO0o % o0o00Oo0O / ii
def o00oOO00 ( url ) :
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  i1I11iIiII ( url )
  if 88 - 88: Ii1I * iiII11i1I1IIi + IIiIiII11i
  if 62 - 62: ii
def iioOo00O0o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , OO0o , '' )
 if 18 - 18: OOoOoo
def IIIi1iiI1I1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  i1iIII = open ( O0OoO000O0OO , 'r' )
  for iII1111III1I in i1iIII :
   oOIiI1i1I11I = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1111III1I )
   for Oo0OO , ooO0oOOooOo0 in oOIiI1i1I11I :
    OOoOOO0 ( Oo0OO , ooO0oOOooOo0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 51 - 51: oO0o % iiII11i1I1IIi
def Iiiii ( url ) :
 if os . path . exists ( Remote ) :
  I1 = oo0O0o00o0O ( url )
  o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , url in o00oooO0Oo :
   url = ( url ) . strip ( )
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + IIi . Oooo0O0oo00oO
  if 58 - 58: iI11I1II1I1I + OooOO000 - Ii1I - ooOoO0O00 * OOooOOo
def OOoO00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + ooO0oOOooOo0
 Oo0OO = 'plugin.video.GenieTv'
 if 4 - 4: ii
 iiiIII1iii1I ( ooO0oOOooOo0 , Oo0OO )
 if 32 - 32: Oooo0O0oo00oO - IIi . oO0o * OOoOoo + iIi1i1ii1 . ooOoO0O00
def i1IiiiI1iI ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooO0oOOooOo0
 Oo0OO = 'repository.GenieTv'
 if 61 - 61: oo0oO00 * IIi + oo0oO00 - I1ii11iIi11i % OOooOOo . iiII11i1I1IIi
 iiiIII1iii1I ( ooO0oOOooOo0 , Oo0OO )
 if 51 - 51: Oooo0O0oo00oO / oo0oO00
 if 51 - 51: OOoOoo * O0oOO0 - OooOO000 + iiII11i1I1IIi
def OO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  II1iiII1 ( )
 if O0oO0 == 1 :
  I1IiiIIiIii1i ( )
  if 27 - 27: OOoOoo . I1ii11iIi11i + OOoOoo + iiII11i1I1IIi
  if 28 - 28: oO0o - OOoOoo - O0oOO0 % O0oOO0 / o0o00Oo0O
  if 99 - 99: IIiIiII11i - iI11I1II1I1I
  if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % OooOO000 - iI11I1II1I1I . oo0oO00
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
II1iii1iII = 'https://addons.tvaddons.ag/'
if 7 - 7: iIi1i1ii1 * ooOoO0O00 . IIi % OOoOoo * OOooOOo . iI11I1II1I1I
def I1IiiIIiIii1i ( ) :
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 oOOoooO0O0 = 'https://addons.tvaddons.ag/search/?keyword=' + OO0
 I1 = O0 ( oOOoooO0O0 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , 10054 , 'https://addons.tvaddons.ag/' + o00OooO0oo , OO0o , '' )
  if 77 - 77: iI11I1II1I1I + IIiIiII11i % IIi . I1ii11iIi11i + ii
  if 95 - 95: O0oOO0 * IIi * ii * I11i + Oooo0O0oo00oO
def II1iiII1 ( ) :
 I1 = O0 ( II1iii1iII )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'Repositories' in Oo0OO :
   pass
  elif 'Services' in Oo0OO :
   pass
  elif 'International' in Oo0OO :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10053 , 'https://addons.tvaddons.ag/' + O0o0OO0000ooo , OO0o , '' )
   if 20 - 20: I1ii11iIi11i % I1ii11iIi11i + iI11I1II1I1I % iiII11i1I1IIi - ii / O0oOO0
   if 78 - 78: OOoOoo . Oooo0O0oo00oO / OOooOOo * I1ii11iIi11i % O0oOO0
def Addon ( url ) :
 I1 = O0 ( url )
 iiI11II = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'Please' in Oo0OO :
   pass
  else :
   o0OIiII ( Oo0OO , url , 10054 , 'https://addons.tvaddons.ag/' + O0o0OO0000ooo , OO0o , '' )
 for url in iiI11II :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
  if 84 - 84: o0o00Oo0O * Ii1I * iI11I1II1I1I - OOooOOo . oo0oO00 * oOo0O0Ooo
  if 63 - 63: iiII11i1I1IIi
def ii1ii1iiIiI ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( oOooO0 , name + '.zip' )
   try :
    os . remove ( Ii1I1Ii )
   except :
    pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   OOoO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OOoO0
   print '======================================='
   extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
   o00O0 ( )
   if 42 - 42: I11i
def iiiIII1iii1I ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 Ii1I1Ii = os . path . join ( oOooO0 , name + '.zip' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 OOoO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOoO0
 print '======================================='
 extract . all ( Ii1I1Ii , OOoO0 , o0oOoO00o )
 o00O0 ( )
 if 8 - 8: Ii / OOoOoo
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 33 - 33: OooOO000 * iIi1i1ii1 - o0o00Oo0O + oOo0O0Ooo / iIi1i1ii1
 if 19 - 19: ooOoO0O00 % IIiIiII11i
def O00OO0oO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 1007 , o00OooO0oo )
def Ii1IIiii1Ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , o00OooO0oo )
  if 48 - 48: I11i + Ii1I / Ii1I
  if 80 - 80: ii
def I11IIIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , iconimage , o0o0oOoOO0O , iiI11ii1I1 , name in o00oooO0Oo :
  if 'http' in url :
   if '.php' in url :
    O0O0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
    for iII1111III1I in O0O0 :
     if iII1111III1I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iii11i1 ( name , url , 1016 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
   else :
    if 'youtube' in url :
     O0O0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for iII1111III1I in O0O0 :
      if iII1111III1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11II1i1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
    else :
     O0O0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for iII1111III1I in O0O0 :
      if iII1111III1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11II1i1 ( name , url , 222 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
  else :
   OOoo0o00O0oO ( url , iconimage , name )
   if 28 - 28: ii % o0o00Oo0O - Oooo0O0oo00oO / I11i / oOo0O0Ooo
 else :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
  for url , o00OooO0oo , name in o00oooO0Oo :
   if 'http' in url :
    if '.php' in url :
     I1i11111i1i11 ( name , url , 1016 , o00OooO0oo )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OOoOOO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo )
     else :
      O0O0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
      for iII1111III1I in O0O0 :
       if iII1111III1I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOoOOO0 ( name , url , 222 , o00OooO0oo )
      Iii1I1I11iiI1 ( 'movies' , 'INFO' )
   else :
    OOoo0o00O0oO ( url , o00OooO0oo , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 41 - 41: IIiIiII11i * iIi1i1ii1 / oO0o . O0oOO0
def OOoo0o00O0oO ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 IiiiiI = ( url ) . replace ( i111i1IIi1i , 'http' ) . replace ( OO0iii111 , '.com' ) ;
 Ii1Ooo0OO00oo = ( IiiiiI ) . replace ( oo00oO00oooo , 'a' ) . replace ( OoOooOo00o , 'b' ) . replace ( iI1IIi , 'c' ) . replace ( I1iiIIiI11I , 'd' ) . replace ( o0OO , 'e' ) . replace ( OOOO0oOO , 'f' ) ;
 i11iII1IiI = ( Ii1Ooo0OO00oo ) . replace ( oO0iIiII111 , 'g' ) . replace ( ooo0ooO00o , 'h' ) . replace ( o00O000oooOo , 'i' ) . replace ( iiiI1I1iiiII , 'j' ) . replace ( II11 , 'k' ) . replace ( oo0o0O , 'l' ) ;
 i1II1IiIi111 = ( i11iII1IiI ) . replace ( oooI1iIiii , 'm' ) . replace ( OoOOo0OO0OOoo , 'n' ) . replace ( i1I , 'o' ) . replace ( i1Ii111 , 'p' ) . replace ( OO0o0o0OOoooo , 'q' ) . replace ( oOO00OOOO0o , 'r' ) ;
 oOOOO0o0o0o = ( i1II1IiIi111 ) . replace ( I1o0o , 's' ) . replace ( I11II1I , 't' ) . replace ( iI1I11i1IiiI1 , 'u' ) . replace ( ooo000O , 'v' ) . replace ( OoOoOo000Oo0 , 'w' ) . replace ( Oo0ooo0ooo , 'x' ) ;
 I1o00O00oOooo = ( oOOOO0o0o0o ) . replace ( oooii111I1I1I , 'y' ) . replace ( iIIiIi1IiI1 , 'z' ) . replace ( iIi1i1I1I , '.' ) . replace ( i11iiiI , '(' ) . replace ( OO0o0o0oo0Oo0 , ')' ) . replace ( IiIii111iI11i , '/' ) ;
 Oo0O = ( I1o00O00oOooo ) . replace ( o0oI1I1i , '1' ) . replace ( oOoOo000 , '2' ) . replace ( Iii1I1III11 , '3' ) . replace ( IIiiiiiI1iIi , '4' ) . replace ( IIIII11II1 , '5' ) . replace ( O0o00oO0o0 , '6' ) ;
 i1ii1IiIiIii = ( Oo0O ) . replace ( IIIiii , '7' ) . replace ( I11OoooO , '8' ) . replace ( i1IIi11 , '9' ) . replace ( oOIIIII11 , '0' ) . replace ( IiOOo0 , ':' ) . replace ( o0O0O0O00o , '%' ) ;
 url = ( i1ii1IiIiIii ) . replace ( oOOOo0Oooo , '-' ) . replace ( o0OOii , '_' ) ;
 OOoOOO0 ( name , url , 222 , iconimage ) ;
 if 55 - 55: OOooOOo . iI11I1II1I1I * Oooo0O0oo00oO % iI11I1II1I1I . oO0o
 if 43 - 43: IIi . Oooo0O0oo00oO + oOo0O0Ooo * Ii
def ii1ii11Ii ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1007 , o00OooO0oo )
def I1III11i11Iii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , o00OooO0oo )
  if 16 - 16: Oooo0O0oo00oO . IIiIiII11i - IIi - ii
def ooOoOoOoo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iIIIII = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iIIIII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIIII )
 if 24 - 24: IIiIiII11i
 if 23 - 23: I1ii11iIi11i - iiII11i1I1IIi
def iIIiI1iiI ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if '-dir-' in Oo0OO :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , O0o0OO0000ooo )
  else :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , O0o0OO0000ooo )
   if 79 - 79: oo0oO00 . o0o00Oo0O - ooOoO0O00
def II1iII11 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 iiiI1 = ( 'http://afewbitsmore.com/' )
 o00oooO0Oo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '[To Parent Directory]' in Oo0OO :
   Oo0OO = 'HOME'
   pass
  elif 'HOME' in Oo0OO :
   pass
  elif '.m3u' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , iiiI1 + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iiiI1 + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iiiI1 + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , iiiI1 + url , 1012 , oOOOo00O00oOo + 'music.png' )
def IiIi1i1I ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 94 - 94: IIi + o0o00Oo0O - ii / o0o00Oo0O
def OoO00iI1I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 iiiI1 = url
 o00oooO0Oo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '.mp3' in Oo0OO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/' , '' ) , iiiI1 + url , 1011 , oOOOo00O00oOo + 'music.png' )
def Oo0o ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ( 'http://www.cyn.net/music/' + ooO0oOOooOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + O0o0OO0000ooo ) . replace ( ' ' , '%20' ) )
def O0OO0 ( url , img ) :
 OOoO = oo0O0o00o0O ( url )
 OooiiIi1i = url
 img = img
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OooiiIi1i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 76 - 76: oO0o . Oooo0O0oo00oO / Oooo0O0oo00oO + OOoOoo / Ii * o0o00Oo0O
def i1i ( url ) :
 OOoO = oo0O0o00o0O ( url )
 OooiiIi1i = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for type , url , Oo0OO in o00oooO0Oo :
  if '[VID]' in type :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OooiiIi1i + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   i1i ( OooiiIi1i + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: IIiIiII11i / iiII11i1I1IIi - I11i
 if 92 - 92: I1ii11iIi11i % I11i - OOoOoo / OOoOoo / OOooOOo
def I11Ii111I ( ) :
 ooo0ooooo0o = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o00oO0 = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0 = o00oO0 . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OooiiIi1i = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OO0OO0OO = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 84 - 84: Oooo0O0oo00oO
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( OooiiIi1i )
 Iiii = Oo0OoO00oOO0o ( OO0OO0OO )
 if 4 - 4: iIi1i1ii1 . OooOO000 / IIi / iiII11i1I1IIi + IIiIiII11i
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o00oooO0Oo :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooO0oOOooOo0 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . oo0oO00 - IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o0O0OOO0Ooo :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooiiIi1i + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for Oo0OO in o0OOo00OoO :
   if o00oO0 in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0OO0OO + Oo0OO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 23 - 23: oo0oO00 * OooOO000 * I11i - oOo0O0Ooo % OOooOOo + I11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 41 - 41: iIi1i1ii1 * ii . OOoOoo % Ii
    if 11 - 11: iI11I1II1I1I . OooOO000 - I1ii11iIi11i / oo0oO00 + IIiIiII11i
    if 29 - 29: oo0oO00 . Ii + ooOoO0O00 - IIi + o0o00Oo0O . oOo0O0Ooo
    if 8 - 8: I11i
    if 78 - 78: ooOoO0O00 - I1ii11iIi11i
    if 48 - 48: IIi - ii + OooOO000 % I11i - OOooOOo . oOo0O0Ooo
oooI1iIiii = '{SF},' ; OoOOo0OO0OOoo = '{IF},' ; i1I = '{PW},' ; Iii1I1III11 = '{AM},' ; i1Ii111 = '{GF},' ; OO0o0o0OOoooo = '{DD},' ; oOO00OOOO0o = '{UO},' ; I1o0o = '{LE},' ; iI1I11i1IiiI1 = '{ZY},' ; ooo000O = '{UE},' ; OoOoOo000Oo0 = '{PE},' ; Oo0ooo0ooo = '{JE},' ; oooii111I1I1I = '{TH},' ; iIIiIi1IiI1 = '{LK},'
if 42 - 42: OooOO000
if 70 - 70: I11i / oo0oO00 + O0oOO0 % oOo0O0Ooo % I1ii11iIi11i + oO0o
def OOOOoO00o0O ( ) :
 OOoO = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 o00oooO0Oo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def ooo0ooo0Oo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OOoO )
 for url , Oo0OO , oO00oOOo0Oo in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO + oO00oOOo0Oo , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def I1ii1iii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oOoOO0OO0O0 ( url )
def oOoOO0OO0O0 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OOoO )
 o0OOo00OoO = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( 'VidSpot - ' + Oo0OO , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in o0O0OOO0Ooo :
  OOoOOO0 ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for Oo0OO , url in o0OOo00OoO :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OOoOOO0 ( 'TheVideo - ' + Oo0OO , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 84 - 84: iI11I1II1I1I * oOo0O0Ooo
def O0Oo000OOoOOo ( ) :
 OOoO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o00oooO0Oo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 11 - 11: Ii % I11i % OOoOoo
  if 59 - 59: IIiIiII11i
def OOo0OOO0OO ( ) :
 OOoO = O0 ( 'http://www.animetoon.org/cartoon' )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 81 - 81: iiII11i1I1IIi - IIi - Oooo0O0oo00oO % iIi1i1ii1 % I11i . iI11I1II1I1I
  if 79 - 79: Ii1I - Ii1I . IIi / iIi1i1ii1
  if 57 - 57: OOoOoo * iI11I1II1I1I * iiII11i1I1IIi * IIi / IIi
def IiIiIiIII1Iii ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for O0o0OO0000ooo in o0O0OOO0Ooo :
  I1iII = O0o0OO0000ooo
 o0OOo00OoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in o0OOo00OoO :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 1003 , I1iII )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoOOOOOo0ooOOO0 ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   Oo00O0OIII ( url )
  elif 'playpanda' in url :
   Oo00O0OIII ( url )
   if 35 - 35: ooOoO0O00 * iiII11i1I1IIi - iiII11i1I1IIi . iIi1i1ii1
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo00O0OIII ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 77 - 77: oOo0O0Ooo / iI11I1II1I1I * IIi * iI11I1II1I1I + Ii1I
  if 78 - 78: iIi1i1ii1 / iiII11i1I1IIi * IIi . Oooo0O0oo00oO . O0oOO0 - OooOO000
def I1IiI11 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOO00O . add_header ( 'referer' , url )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + O0oOO0
def oo0O0o00o0O ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 20 - 20: oO0o + oo0oO00 . IIiIiII11i / Ii
def ii1Ii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiIiII = ( '%s%s' % ( IIiiiI1iI , url ) )
 O0o0O00Oo0o0 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , o00OooO0oo )
  if 41 - 41: Ii1I % Ii1I + iIi1i1ii1 . iiII11i1I1IIi % OooOO000 * OOoOoo
def i1I11iIiII ( url ) :
 if 57 - 57: IIi . OooOO000 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 oo0OO0Oo000oo = open ( I11i1I1I , "a" )
 oo0OO0Oo000oo . write ( 'url="' + url + '"\n' )
 oo0OO0Oo000oo . close
 if 38 - 38: iiII11i1I1IIi + OOoOoo
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 import urlresolver
 try : O00oo . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Oo0OO ) )
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O00oo . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 32 - 32: OOoOoo - ii + oO0o
def OO0oO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 o0oOoO00o . update ( 100 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 O00oo . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 5 - 5: Ii / oO0o % o0o00Oo0O / Oooo0O0oo00oO + I1ii11iIi11i % I11i
def I11I ( url ) :
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O00oo . play ( url ) . strip ( )
 except : pass
 if 93 - 93: OOooOOo % OooOO000 - iiII11i1I1IIi . iIi1i1ii1 - Ii1I * iiII11i1I1IIi
def i1iI1I1I ( url ) :
 O00oo = xbmc . Player ( O0OO00O0oOO ( ) )
 import urlresolver
 i1I11i1iii1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 O00oo . play ( i1I11i1iii1 )
 xbmc . sleep ( 1 )
 O00oo . play ( url )
 if 96 - 96: IIi
 if 59 - 59: Oooo0O0oo00oO + OOooOOo * oO0o % ooOoO0O00 * oO0o
def O0OO00O0oOO ( ) :
 try :
  oOoOo0oOoo0 = getSet ( "core-player" )
  if ( oOoOo0oOoo0 == 'DVDPLAYER' ) : OOOOooO0oOoO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOoOo0oOoo0 == 'MPLAYER' ) : OOOOooO0oOoO = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOoOo0oOoo0 == 'PAPLAYER' ) : OOOOooO0oOoO = xbmc . PLAYER_CORE_PAPLAYER
  else : OOOOooO0oOoO = xbmc . PLAYER_CORE_AUTO
 except : OOOOooO0oOoO = xbmc . PLAYER_CORE_AUTO
 return OOOOooO0oOoO
 return True
 if 46 - 46: Ii1I . IIiIiII11i % O0oOO0 + IIiIiII11i
def I1i11111i1i11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11i1IIiiI = [ ]
  IiI11i1IIiiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 55 - 55: ii
def ii1II1II ( name , url , mode , iconimage , fanart , description ) :
 if 90 - 90: oOo0O0Ooo
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 4 - 4: Oooo0O0oo00oO % OOoOoo - Oooo0O0oo00oO - I11i
def OOoOOO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11i1IIiiI = [ ]
  IiI11i1IIiiI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 30 - 30: iIi1i1ii1
 if 34 - 34: O0oOO0 - IIiIiII11i - I11i + iiII11i1I1IIi + OooOO000
 if 70 - 70: ii + oO0o * I1ii11iIi11i
 if 20 - 20: Ii - IIiIiII11i - OOoOoo % O0oOO0 . OOoOoo
 if 50 - 50: iI11I1II1I1I + OooOO000 - oo0oO00 - ii
 if 84 - 84: OOooOOo - oo0oO00
def OOOiiiiI ( heading , announce ) :
 class OoO00O00O0 ( ) :
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
   try : oOOo0O00o = open ( announce ) ; iI1i1I1III1i = oOOo0O00o . read ( )
   except : iI1i1I1III1i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iI1i1I1III1i ) )
   return
 OoO00O00O0 ( )
 OoO00O00O0 ( )
 if 76 - 76: oOo0O0Ooo % Ii + Oooo0O0oo00oO
def OOI1iI1ii1II ( ) :
 OOOiiiiI ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 17 - 17: oo0oO00 / IIiIiII11i * I11i / I1ii11iIi11i + iiII11i1I1IIi . O0oOO0
 if 19 - 19: Oooo0O0oo00oO * oo0oO00
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
 if 69 - 69: IIi / OooOO000 % OooOO000 / OOoOoo + OooOO000 / ooOoO0O00
 if 70 - 70: Oooo0O0oo00oO - iIi1i1ii1 . OooOO000
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 11 - 11: Ii + I11i - OooOO000 * Ii - oOo0O0Ooo
 if 49 - 49: ooOoO0O00 % O0oOO0 / Oooo0O0oo00oO . Ii1I - OooOO000
 if 12 - 12: Ii + oo0oO00 - Ii1I
 if 27 - 27: iiII11i1I1IIi
 if 22 - 22: OOooOOo / oOo0O0Ooo
 if 33 - 33: oo0oO00
 if 37 - 37: OOooOOo % I11i * oO0o / Ii * IIiIiII11i * iiII11i1I1IIi
 if 70 - 70: OOoOoo . Ii % OOooOOo + O0oOO0
 if 95 - 95: Ii1I
 if 48 - 48: oo0oO00
 if 14 - 14: iI11I1II1I1I / I11i * iIi1i1ii1
 if 35 - 35: iI11I1II1I1I
 if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
 if 75 - 75: oOo0O0Ooo - OOoOoo - oOo0O0Ooo % O0oOO0 % ii
 if 13 - 13: OOoOoo * oO0o % iI11I1II1I1I / iIi1i1ii1 * iiII11i1I1IIi . I1ii11iIi11i
 if 23 - 23: OOoOoo / iIi1i1ii1 . iiII11i1I1IIi * IIi
 if 87 - 87: Ii
 if 34 - 34: ooOoO0O00
 if 64 - 64: iI11I1II1I1I / iIi1i1ii1 / I1ii11iIi11i - Ii1I
 if 100 - 100: iIi1i1ii1 + ooOoO0O00 * oO0o
 if 64 - 64: O0oOO0 * Ii . I1ii11iIi11i
 if 52 - 52: I1ii11iIi11i / OOoOoo / iiII11i1I1IIi - I11i / iiII11i1I1IIi
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
def ooOoo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i1IiIiI11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 33 - 33: O0oOO0 + I1ii11iIi11i + OooOO000 * O0oOO0 / I11i
def O0O0OOo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ii1i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 66 - 66: OooOO000 * ii / Ii1I - oo0oO00 - OOoOoo * oo0oO00
def OOoOooO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOoOI1i1i1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 78 - 78: ii % iiII11i1I1IIi + oO0o * ii
def iioOoO0oOO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o00I11Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 27 - 27: OooOO000 - I11i * Ii1I - oOo0O0Ooo
def IIIiIIi111 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oo0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 86 - 86: o0o00Oo0O . ii * oo0oO00 / iIi1i1ii1
def oO0OooOO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + IiIII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 5 - 5: ii
def i1IIIiI1ii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ii1IO00oO0oOOOOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 88 - 88: iI11I1II1I1I % IIiIiII11i % IIiIiII11i . Oooo0O0oo00oO % O0oOO0
def iIoo0O0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i1I1i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
def iIi1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i11IIiiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / Oooo0O0oo00oO / OooOO000
def Ii1I1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i11Ii1iiiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 50 - 50: I1ii11iIi11i - oOo0O0Ooo * oO0o . OOoOoo % oO0o + ii
 if 25 - 25: iiII11i1I1IIi . oO0o / iI11I1II1I1I
 if 56 - 56: I11i % Ii . IIi * iI11I1II1I1I - I1ii11iIi11i
 if 77 - 77: ii
 if 52 - 52: iiII11i1I1IIi - oO0o % Ii . oo0oO00
 if 98 - 98: ii + OOooOOo . OOooOOo / o0o00Oo0O / Ii
 if 88 - 88: IIiIiII11i - iiII11i1I1IIi / ii
 if 71 - 71: Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
def iIIooO0o0O0Oo ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1ii1i , i1II11II1 , II1IIIii in os . walk ( O00o0OO ) :
     i1iI11IiII = 0
     i1iI11IiII += len ( II1IIIii )
     if i1iI11IiII > 0 :
      for oOOo0O00o in II1IIIii :
       os . unlink ( os . path . join ( I1ii1i , oOOo0O00o ) )
  oO00Oo0OO = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( oO00Oo0OO )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 32 - 32: IIi - IIi
 if 6 - 6: iI11I1II1I1I - Ii / Ii1I - I11i
 if 95 - 95: oo0oO00
 if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - iiII11i1I1IIi
 if 30 - 30: OooOO000 % O0oOO0 + O0oOO0 * ii - Ii1I
 if 69 - 69: Ii1I + oO0o / o0o00Oo0O + IIiIiII11i / Ii
 if 48 - 48: ii / oOo0O0Ooo
 if 19 - 19: Oooo0O0oo00oO * Ii1I - OOoOoo * Ii + oo0oO00
def oO0O0 ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 92 - 92: oO0o
def O0ooO0Oo00o ( url ) :
 OOOooooOo0 = os . path . join ( oO , 'addon_data' )
 o000o00OO00Oo = [
 ( OOOooooOo0 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OOOooooOo0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OOOooooOo0 , 'plugin.video.itv' , 'Images' ) ) ]
 if 12 - 12: oo0oO00 * O0oOO0 - OooOO000 * iiII11i1I1IIi - OOoOoo * OooOO000
 o0Oo0OOOOoo = 0
 if 82 - 82: OOooOOo . OOooOOo
 for iII1111III1I in o000o00OO00Oo :
  if os . path . exists ( iII1111III1I ) and not iII1111III1I in [ oOo0oooo00o , OOOooooOo0 ] :
   for I1ii1i , i1II11II1 , II1IIIii in os . walk ( iII1111III1I ) :
    i1iI11IiII = 0
    i1iI11IiII += len ( II1IIIii )
    if i1iI11IiII > 0 :
     for oOOo0O00o in II1IIIii :
      if not oOOo0O00o in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( I1ii1i , oOOo0O00o ) )
       except :
        pass
      else : ii1 ( 'Ignore Log File: %s' % oOOo0O00o )
     for OoOOoO0oOo in i1II11II1 :
      try :
       shutil . rmtree ( os . path . join ( I1ii1i , OoOOoO0oOo ) )
       o0Oo0OOOOoo += 1
       ii1 ( "[Success] cleared %s files from %s" % ( str ( i1iI11IiII ) , os . path . join ( iII1111III1I , OoOOoO0oOo ) ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
  else :
   for I1ii1i , i1II11II1 , II1IIIii in os . walk ( iII1111III1I ) :
    for OoOOoO0oOo in i1II11II1 :
     if 'cache' in OoOOoO0oOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1ii1i , OoOOoO0oOo ) )
       o0Oo0OOOOoo += 1
       ii1 ( "[Success] wiped %s " % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
       if 10 - 10: I1ii11iIi11i * Ii1I . O0oOO0 . ii . Oooo0O0oo00oO * Ii1I
 oO0O0 ( oo0o0O00 , 'Clear Cache: Removed %s Files' % o0Oo0OOOOoo )
 if 80 - 80: OooOO000 + oo0oO00 . OooOO000 + Oooo0O0oo00oO
 if 85 - 85: Ii . oo0oO00 + IIi / IIi
 if 43 - 43: iIi1i1ii1 . ii - IIiIiII11i
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * Oooo0O0oo00oO * O0oOO0
 if 19 - 19: OooOO000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
 if 15 - 15: IIi + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
def oOO0o0oo0 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0ooO00OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1ii1i , i1II11II1 , II1IIIii in os . walk ( O0ooO00OO ) :
   i1iI11IiII = 0
   i1iI11IiII += len ( II1IIIii )
   if 43 - 43: IIiIiII11i . iiII11i1I1IIi / IIi - oo0oO00
   if 36 - 36: iiII11i1I1IIi - iIi1i1ii1 * iI11I1II1I1I % oo0oO00 / iIi1i1ii1
   if i1iI11IiII > 0 :
    if 35 - 35: IIiIiII11i . o0o00Oo0O - iiII11i1I1IIi / ii . IIiIiII11i * oOo0O0Ooo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( i1iI11IiII ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: o0o00Oo0O
     for oOOo0O00o in II1IIIii :
      os . unlink ( os . path . join ( I1ii1i , oOOo0O00o ) )
     for OoOOoO0oOo in i1II11II1 :
      shutil . rmtree ( os . path . join ( I1ii1i , OoOOoO0oOo ) )
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
 if 32 - 32: ii
 if 29 - 29: Ii1I
 if 41 - 41: IIi
 if 49 - 49: IIi % IIiIiII11i . IIi - I11i - oo0oO00 * iIi1i1ii1
 if 47 - 47: o0o00Oo0O . I11i / IIi * iiII11i1I1IIi
 if 63 - 63: OooOO000 - O0oOO0 - iiII11i1I1IIi - OOoOoo / O0oOO0 + oO0o
 if 94 - 94: iIi1i1ii1 / oOo0O0Ooo . IIiIiII11i
 if 32 - 32: O0oOO0 . Oooo0O0oo00oO % Oooo0O0oo00oO . OOooOOo
 if 37 - 37: Oooo0O0oo00oO + o0o00Oo0O + Oooo0O0oo00oO . iiII11i1I1IIi . I11i
def OO0Oooo0oOO0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0ooO00OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1ii1i , i1II11II1 , II1IIIii in os . walk ( O0ooO00OO ) :
   i1iI11IiII = 0
   i1iI11IiII += len ( II1IIIii )
   if 78 - 78: oOo0O0Ooo / oo0oO00 + I11i . I1ii11iIi11i / o0o00Oo0O
   if 49 - 49: Ii1I
   if i1iI11IiII > 0 :
    if 66 - 66: I11i . Ii1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( i1iI11IiII ) + " files found" , "Do you want to delete them?" ) :
     if 18 - 18: I1ii11iIi11i + iIi1i1ii1
     for oOOo0O00o in II1IIIii :
      os . unlink ( os . path . join ( I1ii1i , oOOo0O00o ) )
     for OoOOoO0oOo in i1II11II1 :
      shutil . rmtree ( os . path . join ( I1ii1i , OoOOoO0oOo ) )
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
 O0ooO0Oo00o ( url )
 return
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % IIi . oOo0O0Ooo
 if 43 - 43: oOo0O0Ooo % Ii1I * IIi
 if 31 - 31: IIi / iiII11i1I1IIi
 if 3 - 3: iIi1i1ii1
 if 37 - 37: IIi * ii * oo0oO00 + I1ii11iIi11i . oOo0O0Ooo
 if 61 - 61: Oooo0O0oo00oO . Oooo0O0oo00oO
 if 17 - 17: IIiIiII11i / OOoOoo
 if 80 - 80: Oooo0O0oo00oO * oO0o + IIi
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
 if 98 - 98: I11i * I1ii11iIi11i - IIi . OOoOoo
def iI11i1iI ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 oo0OoOOO = os . path . join ( oOooO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oo0OoOOO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
   try :
    os . remove ( oo0O0Ooo0o0 )
    print '=== GenieTv - REMOVING    ' + str ( oo0O0Ooo0o0 ) + '    ==='
   except :
    pass
   O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
   I1i = open ( oo0O0Ooo0o0 , "w" )
   I1i . write ( O0o0O00Oo0o0 )
   I1i . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oo0O0Ooo0o0 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
  try :
   os . remove ( oo0O0Ooo0o0 )
   print '=== GenieTv - REMOVING    ' + str ( oo0O0Ooo0o0 ) + '    ==='
  except :
   pass
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  I1i = open ( oo0O0Ooo0o0 , "w" )
  I1i . write ( O0o0O00Oo0o0 )
  I1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0O0Ooo0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 76 - 76: Ii1I
def OoOooO ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  I1i = open ( oo0O0Ooo0o0 ) . read ( )
  if 'zero' in I1i :
   name = '0CACHE'
  elif 'tuxen' in I1i :
   name = 'TUXENS'
  elif 'muckys' in I1i :
   name = 'MUCKYS'
  elif 'p2p1' in I1i :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in I1i :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in I1i :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 76 - 76: I1ii11iIi11i * OOoOoo % Oooo0O0oo00oO . oO0o
def iIii1i1i1 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  os . remove ( oo0O0Ooo0o0 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oo0O0Ooo0o0 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 45 - 45: oo0oO00 - Oooo0O0oo00oO * iiII11i1I1IIi - oO0o . IIi
 if 77 - 77: O0oOO0 / oo0oO00
 if 49 - 49: iIi1i1ii1
 if 56 - 56: o0o00Oo0O / oo0oO00 + Oooo0O0oo00oO
 if 7 - 7: I1ii11iIi11i - Ii / O0oOO0 / O0oOO0 . ooOoO0O00 % oo0oO00
 if 51 - 51: O0oOO0
 if 23 - 23: Ii * iIi1i1ii1 * oo0oO00 % oo0oO00 - OOooOOo + IIiIiII11i
 if 91 - 91: ii + OooOO000 / IIiIiII11i * iiII11i1I1IIi + I11i / I1ii11iIi11i
 if 7 - 7: oo0oO00 / Ii - IIi % iiII11i1I1IIi
 if 67 - 67: iI11I1II1I1I - OOooOOo
def oOo000O ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o00oooO0Oo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for O00OOOOo00o0 , IIiiii1I1 , i11IIii11III1 , OOOoO0oo0oo0o in o00oooO0Oo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O00OOOOo00o0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i11IIii11III1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OOOoO0oo0oo0o )
  inc = inc + 1
  if 70 - 70: iI11I1II1I1I + I11i * O0oOO0
  if 68 - 68: OOooOOo % Ii + IIiIiII11i . I1ii11iIi11i
  if 80 - 80: ooOoO0O00 * Ii1I
  if 93 - 93: o0o00Oo0O - Ii - oO0o + IIi
  if 86 - 86: oOo0O0Ooo / Ii1I * IIi % Ii
  if 20 - 20: iiII11i1I1IIi . ii + iiII11i1I1IIi + OOoOoo * Ii1I
  if 44 - 44: Ii
  if 69 - 69: Oooo0O0oo00oO * o0o00Oo0O + Ii
  if 65 - 65: o0o00Oo0O / iiII11i1I1IIi . ooOoO0O00 * iiII11i1I1IIi / iI11I1II1I1I - O0oOO0
def OOOo00OOooO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'addons2.ini' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  I1i = open ( oo0O0Ooo0o0 , "w" )
  I1i . write ( O0o0O00Oo0o0 )
  I1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0O0Ooo0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 57 - 57: O0oOO0 . I11i % Ii1I - I11i
def o0O0oo0O ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo0O0Ooo0o0 = os . path . join ( oOooO0 , 'settings.xml' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  I1i = open ( oo0O0Ooo0o0 , "w" )
  I1i . write ( O0o0O00Oo0o0 )
  I1i . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0O0Ooo0o0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 37 - 37: iIi1i1ii1 - Ii1I . OooOO000 . iIi1i1ii1 . I1ii11iIi11i % iiII11i1I1IIi
 if 64 - 64: ii % OOoOoo . Ii - OooOO000
def ooOiII11iiI1i11I ( ) :
 try :
  I1Iii1III = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I1Iii1III ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Oo0oo0OoO0o0 = os . path . join ( I1Iii1III , "source.db" )
    os . unlink ( Oo0oo0OoO0o0 )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 13 - 13: iiII11i1I1IIi . iiII11i1I1IIi + Ii % o0o00Oo0O % OooOO000 + iIi1i1ii1
 if 42 - 42: ooOoO0O00 + iiII11i1I1IIi . ii + Ii1I . oo0oO00 / IIi
 if 1 - 1: I11i
 if 95 - 95: Oooo0O0oo00oO / ooOoO0O00 % oO0o . OooOO000 + OooOO000
 if 80 - 80: o0o00Oo0O + Ii1I + Oooo0O0oo00oO
def O0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 95 - 95: Ii1I
 if 98 - 98: iIi1i1ii1 * iiII11i1I1IIi . ii . o0o00Oo0O
 if 89 - 89: iiII11i1I1IIi / o0o00Oo0O % ii - o0o00Oo0O . oO0o
 if 32 - 32: OOoOoo
 if 26 - 26: o0o00Oo0O * IIi - oOo0O0Ooo - iiII11i1I1IIi / iI11I1II1I1I
 if 57 - 57: Ii1I - oO0o * iI11I1II1I1I
 if 26 - 26: oO0o % OOoOoo % I11i % OOooOOo . iiII11i1I1IIi % o0o00Oo0O
def oo00OO0000oO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OoiIiiIi11 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OoiIiiIi11 :
  o0o0oOOo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; o0o0oOOo = xbmc . translatePath ( o0o0oOOo ) ;
  ooO0000 = os . path . join ( o0o0oOOo , ".." , ".." ) ; ooO0000 = os . path . abspath ( ooO0000 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + ooO0000 ) ; Ooo00O0OooOOO = False
  try :
   for I1ii1i , i1II11II1 , II1IIIii in os . walk ( ooO0000 , topdown = True ) :
    i1II11II1 [ : ] = [ OoOOoO0oOo for OoOOoO0oOo in i1II11II1 if OoOOoO0oOo not in o0oO0 ]
    for Oo0OO in II1IIIii :
     try : os . remove ( os . path . join ( I1ii1i , Oo0OO ) )
     except :
      if Oo0OO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Ooo00O0OooOOO = True
      plugintools . log ( "Error removing " + I1ii1i + " " + Oo0OO )
    for Oo0OO in i1II11II1 :
     try : os . rmdir ( os . path . join ( I1ii1i , Oo0OO ) )
     except :
      if Oo0OO not in [ "Database" , "userdata" ] : Ooo00O0OooOOO = True
      plugintools . log ( "Error removing " + I1ii1i + " " + Oo0OO )
   if not Ooo00O0OooOOO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I1I1IiIi1 ( )
 if 28 - 28: I1ii11iIi11i
 if 62 - 62: I1ii11iIi11i + ii / iiII11i1I1IIi
 if 60 - 60: IIi / OOooOOo . oo0oO00 % Oooo0O0oo00oO
def OooO0o ( ) :
 i1i1ii1Ii111i = [ ]
 iiiI1iiI11iii = sys . argv [ 2 ]
 if len ( iiiI1iiI11iii ) >= 2 :
  I1II1 = sys . argv [ 2 ]
  o0O0oOOoo0O0 = I1II1 . replace ( '?' , '' )
  if ( I1II1 [ len ( I1II1 ) - 1 ] == '/' ) :
   I1II1 = I1II1 [ 0 : len ( I1II1 ) - 2 ]
  OO00OOo = o0O0oOOoo0O0 . split ( '&' )
  i1i1ii1Ii111i = { }
  for I1Ii1i11I1I in range ( len ( OO00OOo ) ) :
   IiI11i1IiI1 = { }
   IiI11i1IiI1 = OO00OOo [ I1Ii1i11I1I ] . split ( '=' )
   if ( len ( IiI11i1IiI1 ) ) == 2 :
    i1i1ii1Ii111i [ IiI11i1IiI1 [ 0 ] ] = IiI11i1IiI1 [ 1 ]
    if 88 - 88: Oooo0O0oo00oO - o0o00Oo0O % I11i
 return i1i1ii1Ii111i
 if 63 - 63: OOoOoo * O0oOO0 + OOoOoo * IIi + I1ii11iIi11i / Ii1I
iiOOOO00oO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
oOOoo0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o0i111I = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
o0OooOO0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iI1ii1iiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
i1IiIiI11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i11i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ii1i111 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OOoOI1i1i1Iii1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o00I11Ii1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oo0O0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IiIII1i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
ii1IO00oO0oOOOOOO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1i1I1i1Ii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
I1i11IIiiIiI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0Oo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oo0oo0O0Oo0O = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0OooooO0O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IIi11II1II111 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOOoOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
II11iI1iiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
i11Ii1iiiI1I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IIiiiI1iI = base64 . decodestring ( 'Q1VOVA==' )
def I1IiiiiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
def o0OIiII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 93 - 93: OOoOoo % OooOO000
 if 46 - 46: Ii1I * OOooOOo * iIi1i1ii1 * Ii1I . Ii1I
I1II1 = OooO0o ( )
ooO0oOOooOo0 = None
Oo0OO = None
iiIi1iI1iIii = None
iIIiiI1II1i11 = None
iiI11ii1I1 = None
OOo = None
i1I11iIIiIIiIi = None
ii1IiI = None
if 96 - 96: IIi
if 73 - 73: OooOO000 + IIi
try :
 ii1IiI = int ( I1II1 [ "fav_mode" ] )
except :
 pass
 if 53 - 53: Oooo0O0oo00oO % oO0o - I11i % I1ii11iIi11i / o0o00Oo0O - Ii1I
try :
 ooO0oOOooOo0 = urllib . unquote_plus ( I1II1 [ "url" ] )
except :
 pass
try :
 Oo0OO = urllib . unquote_plus ( I1II1 [ "name" ] )
except :
 pass
try :
 iIIiiI1II1i11 = urllib . unquote_plus ( I1II1 [ "iconimage" ] )
except :
 pass
try :
 iiIi1iI1iIii = int ( I1II1 [ "mode" ] )
except :
 pass
try :
 iiI11ii1I1 = urllib . unquote_plus ( I1II1 [ "fanart" ] )
except :
 pass
try :
 OOo = urllib . unquote_plus ( I1II1 [ "description" ] )
except :
 pass
 if 32 - 32: OOooOOo % o0o00Oo0O % Ii - OOoOoo . oOo0O0Ooo
 if 24 - 24: O0oOO0 % I11i / OooOO000 + I11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( iiIi1iI1iIii )
print "URL: " + str ( ooO0oOOooOo0 )
print "Name: " + str ( Oo0OO )
print "IconImage: " + str ( iIIiiI1II1i11 )
if 59 - 59: IIiIiII11i % oOo0O0Ooo * o0o00Oo0O . ii - ii % o0o00Oo0O
if 56 - 56: O0oOO0 - ooOoO0O00 * ii - IIiIiII11i
def Iii1I1I11iiI1 ( content , viewType ) :
 if 28 - 28: ooOoO0O00 / oo0oO00 . I11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 11 - 11: I1ii11iIi11i * ii - Ii
if iIIiiI1II1i11 == None : iIIiiI1II1i11 = Ooo
if iiI11ii1I1 == None : iiI11ii1I1 = OO0o
if iiIi1iI1iIii == None :
 oo0OOo0 ( )
 if 13 - 13: Ii . o0o00Oo0O / Oooo0O0oo00oO * ooOoO0O00
elif iiIi1iI1iIii == 1 :
 i1IiiiiIi1I ( ooO0oOOooOo0 )
 if 14 - 14: iIi1i1ii1 + iIi1i1ii1 . oo0oO00 / IIi . iI11I1II1I1I
elif iiIi1iI1iIii == 44 :
 oooO ( ooO0oOOooOo0 )
 if 10 - 10: IIiIiII11i . Oooo0O0oo00oO / iiII11i1I1IIi
elif iiIi1iI1iIii == 2 :
 ii1ii11IiI ( )
 if 35 - 35: iiII11i1I1IIi / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif iiIi1iI1iIii == 3 :
 Oo0o0OOOOO0O ( )
 if 3 - 3: Ii1I
elif iiIi1iI1iIii == 21 :
 i1i1II ( )
 if 42 - 42: oo0oO00 % I1ii11iIi11i + iIi1i1ii1 - oo0oO00 . iI11I1II1I1I - IIi
elif iiIi1iI1iIii == 4 :
 ii1111Ii1i ( )
 if 27 - 27: iiII11i1I1IIi % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif iiIi1iI1iIii == 5 :
 o0OO0OOO0O ( ooO0oOOooOo0 )
 if 37 - 37: iiII11i1I1IIi + OooOO000 * IIi + iIi1i1ii1
elif iiIi1iI1iIii == 6 :
 oOO0o0oo0 ( ooO0oOOooOo0 )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + IIi / IIiIiII11i
elif iiIi1iI1iIii == 7 :
 iI11i1iI ( ooO0oOOooOo0 , Oo0OO )
 if 66 - 66: OOoOoo + O0oOO0 % ii
elif iiIi1iI1iIii == 8 :
 OoOooO ( ooO0oOOooOo0 , Oo0OO )
 if 23 - 23: O0oOO0 . OOooOOo + iI11I1II1I1I
elif iiIi1iI1iIii == 9 :
 FIXREPOSADDONS ( ooO0oOOooOo0 )
 if 17 - 17: iIi1i1ii1
elif iiIi1iI1iIii == 10 :
 o00O0 ( )
 if 12 - 12: ooOoO0O00 . oO0o
elif iiIi1iI1iIii == 11 :
 iIii1i1i1 ( ooO0oOOooOo0 )
 if 14 - 14: Oooo0O0oo00oO + IIiIiII11i % Oooo0O0oo00oO . O0oOO0 * OOoOoo
elif iiIi1iI1iIii == 12 :
 oOo000O ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 54 - 54: OOoOoo * oo0oO00 - OooOO000
elif iiIi1iI1iIii == 13 :
 iIIooO0o0O0Oo ( )
 if 15 - 15: iiII11i1I1IIi / o0o00Oo0O
elif iiIi1iI1iIii == 14 :
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + OOoOoo . OooOO000 * OOoOoo
elif iiIi1iI1iIii == 15 :
 I1IiIii11I ( )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif iiIi1iI1iIii == 16 :
 OOOo00OOooO ( ooO0oOOooOo0 , Oo0OO )
 if 82 - 82: o0o00Oo0O / iiII11i1I1IIi * oO0o - oo0oO00 + I1ii11iIi11i
elif iiIi1iI1iIii == 17 :
 o0O0oo0O ( ooO0oOOooOo0 , Oo0OO )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + IIi * IIiIiII11i
elif iiIi1iI1iIii == 18 :
 ooOiII11iiI1i11I ( )
 if 78 - 78: OooOO000 - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif iiIi1iI1iIii == 19 :
 ii1ii1I1IIi1 ( ooO0oOOooOo0 )
 if 97 - 97: ooOoO0O00
elif iiIi1iI1iIii == 40 :
 iIIii1 ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 29 - 29: oOo0O0Ooo
elif iiIi1iI1iIii == 42 :
 oOOoOOO0oo0 ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 37 - 37: Ii1I * OooOO000 * oOo0O0Ooo * o0o00Oo0O
elif iiIi1iI1iIii == 43 :
 oooO0oOoo ( ooO0oOOooOo0 )
 if 35 - 35: oOo0O0Ooo - Ii1I * iiII11i1I1IIi + iIi1i1ii1 / ooOoO0O00
elif iiIi1iI1iIii == 20 :
 o0O0oO0 ( ooO0oOOooOo0 )
 if 46 - 46: I1ii11iIi11i . OOoOoo % I1ii11iIi11i / IIiIiII11i * OOoOoo * Oooo0O0oo00oO
elif iiIi1iI1iIii == 22 :
 ooOoo ( ooO0oOOooOo0 )
 if 59 - 59: OooOO000 * iiII11i1I1IIi
elif iiIi1iI1iIii == 23 :
 O0O0OOo ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 / o0o00Oo0O
elif iiIi1iI1iIii == 24 :
 OOoOooO0o ( ooO0oOOooOo0 )
 if 57 - 57: ooOoO0O00 % OOoOoo
elif iiIi1iI1iIii == 25 :
 iioOoO0oOO ( ooO0oOOooOo0 )
 if 69 - 69: I11i
elif iiIi1iI1iIii == 26 :
 IIIiIIi111 ( ooO0oOOooOo0 )
 if 69 - 69: OooOO000
elif iiIi1iI1iIii == 27 :
 oO0OooOO0 ( ooO0oOOooOo0 )
 if 83 - 83: iI11I1II1I1I . I11i + OooOO000 . ii / OOoOoo + IIiIiII11i
elif iiIi1iI1iIii == 28 :
 i1IIIiI1ii ( ooO0oOOooOo0 )
 if 90 - 90: IIi * iiII11i1I1IIi / Oooo0O0oo00oO
elif iiIi1iI1iIii == 29 :
 iIoo0O0 ( ooO0oOOooOo0 )
 if 68 - 68: OOooOOo
elif iiIi1iI1iIii == 30 :
 I1IiiiIiI ( ooO0oOOooOo0 )
 if 65 - 65: O0oOO0
elif iiIi1iI1iIii == 31 :
 iIi1i ( ooO0oOOooOo0 )
 if 82 - 82: I11i
elif iiIi1iI1iIii == 32 :
 OoOoO ( )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + OooOO000
elif iiIi1iI1iIii == 33 :
 o0o0O00 ( )
 if 65 - 65: IIi
elif iiIi1iI1iIii == 35 :
 i1II1Ii1i1 ( ooO0oOOooOo0 )
 if 71 - 71: OooOO000 % OooOO000 . O0oOO0 + Ii - Ii
elif iiIi1iI1iIii == 34 :
 i1iIiIIi1II1ii ( ooO0oOOooOo0 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / OooOO000 - Ii . OOoOoo / Oooo0O0oo00oO
elif iiIi1iI1iIii == 36 :
 o00ooOoO0 ( ooO0oOOooOo0 )
 if 13 - 13: I11i % o0o00Oo0O - OooOO000 * ii / I1ii11iIi11i - ii
elif iiIi1iI1iIii == 37 :
 o0O0OO0o ( ooO0oOOooOo0 )
 if 78 - 78: O0oOO0 % ii
elif iiIi1iI1iIii == 38 :
 o0O0oo0o ( ooO0oOOooOo0 )
 if 73 - 73: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + ooOoO0O00 - ii / O0oOO0
elif iiIi1iI1iIii == 41 :
 oo00OO0000oO ( I1II1 )
 if 78 - 78: ii % O0oOO0 - Ii
elif iiIi1iI1iIii == 39 :
 Ii1I1i ( ooO0oOOooOo0 )
 if 37 - 37: iIi1i1ii1 % IIi % ooOoO0O00
elif iiIi1iI1iIii == 45 :
 TEXTS ( )
 if 23 - 23: OOoOoo - o0o00Oo0O + Ii
elif iiIi1iI1iIii == 46 :
 OOI1iI1ii1II ( )
 if 98 - 98: ii
elif iiIi1iI1iIii == 47 :
 GEVID ( )
 if 61 - 61: I11i . iIi1i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
elif iiIi1iI1iIii == 48 :
 IiiIi11Ii1iI1 ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 65 - 65: ooOoO0O00 * Oooo0O0oo00oO * ii - iIi1i1ii1 . iiII11i1I1IIi - oO0o
elif iiIi1iI1iIii == 49 :
 IIo0Oo0oO0oOO00 ( )
 if 71 - 71: IIi * OOooOOo
elif iiIi1iI1iIii == 222 :
 i1I11iIiII ( ooO0oOOooOo0 )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % OooOO000 * I11i
elif iiIi1iI1iIii == 333 :
 ii1Ii ( ooO0oOOooOo0 )
 if 64 - 64: OOoOoo / OOoOoo + Ii1I * Oooo0O0oo00oO % Oooo0O0oo00oO
 if 87 - 87: oO0o * I1ii11iIi11i
elif iiIi1iI1iIii == 1020 :
 O0Oo000OOoOOo ( )
 if 83 - 83: ooOoO0O00 * OooOO000 - iIi1i1ii1 / IIi
elif iiIi1iI1iIii == 1021 :
 ANIMEEP ( )
 if 48 - 48: O0oOO0 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif iiIi1iI1iIii == 1022 :
 ANIMEPLAY ( ooO0oOOooOo0 )
 if 32 - 32: IIi * oOo0O0Ooo - Oooo0O0oo00oO . I1ii11iIi11i / o0o00Oo0O + IIi
elif iiIi1iI1iIii == 1001 :
 OOo0OOO0OO ( )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif iiIi1iI1iIii == 1005 :
 ii1ii11Ii ( )
 if 7 - 7: Ii % Ii1I / OooOO000 % I1ii11iIi11i - oO0o
elif iiIi1iI1iIii == 1007 :
 I1III11i11Iii ( ooO0oOOooOo0 )
 if 73 - 73: Ii1I
elif iiIi1iI1iIii == 1010 :
 iIIiI1iiI ( ooO0oOOooOo0 )
 if 92 - 92: Ii + o0o00Oo0O * oo0oO00
elif iiIi1iI1iIii == 1011 :
 OoO00iI1I ( ooO0oOOooOo0 )
 if 60 - 60: I11i / I1ii11iIi11i
elif iiIi1iI1iIii == 1012 :
 II1iII11 ( ooO0oOOooOo0 )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif iiIi1iI1iIii == 1030 :
 Oo0o ( )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % OooOO000 / Ii1I
elif iiIi1iI1iIii == 1031 :
 O0OO0 ( ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 76 - 76: oO0o * O0oOO0 - oO0o
elif iiIi1iI1iIii == 1032 :
 i1i ( ooO0oOOooOo0 )
 if 57 - 57: ii / OOooOOo + O0oOO0 . IIi
elif iiIi1iI1iIii == 1006 :
 Parse . ParseURL ( ooO0oOOooOo0 )
 if 14 - 14: Ii % Oooo0O0oo00oO * I11i * OOooOOo
elif iiIi1iI1iIii == 2030 :
 Parse . addonParseURL ( ooO0oOOooOo0 )
 if 55 - 55: OooOO000 * Oooo0O0oo00oO * OooOO000
elif iiIi1iI1iIii == 2031 :
 Parse . apkParseURL ( ooO0oOOooOo0 )
 if 70 - 70: o0o00Oo0O . IIi
elif iiIi1iI1iIii == 1002 :
 IiIiIiIII1Iii ( ooO0oOOooOo0 )
 if 33 - 33: Oooo0O0oo00oO * IIi
elif iiIi1iI1iIii == 1003 :
 OOoOOOOOo0ooOOO0 ( ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 64 - 64: Ii . iI11I1II1I1I
elif iiIi1iI1iIii == 1004 :
 Oo00O0OIII ( ooO0oOOooOo0 )
 if 7 - 7: OOooOOo % OOoOoo + OOooOOo - OOooOOo * Ii % oO0o
elif iiIi1iI1iIii == 1008 :
 Ii11I1 ( )
 if 57 - 57: Oooo0O0oo00oO / oO0o + Ii1I
elif iiIi1iI1iIii == 1009 :
 Iiiii ( ooO0oOOooOo0 )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % Oooo0O0oo00oO + iIi1i1ii1 . oO0o . I1ii11iIi11i
elif iiIi1iI1iIii == 2001 :
 IIIi1iiI1I1 ( )
 if 70 - 70: oo0oO00 . Ii1I * O0oOO0
elif iiIi1iI1iIii == 2002 :
 IiIi1i1I ( ooO0oOOooOo0 )
 if 97 - 97: O0oOO0 . iI11I1II1I1I - Oooo0O0oo00oO
elif iiIi1iI1iIii == 1013 :
 iIoo0ooooO ( )
elif iiIi1iI1iIii == 10111113 :
 Oo0O0Oo00O ( ooO0oOOooOo0 )
 if 23 - 23: Ii1I % oo0oO00
elif iiIi1iI1iIii == 1014 :
 o00ooOo ( )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif iiIi1iI1iIii == 1015 :
 iIoOO0OO00 ( ooO0oOOooOo0 )
 if 99 - 99: OooOO000 - Ii1I - oOo0O0Ooo - OooOO000 + oO0o + IIiIiII11i
elif iiIi1iI1iIii == 1016 :
 I11IIIi ( ooO0oOOooOo0 , iIIiiI1II1i11 , Oo0OO )
 if 34 - 34: OooOO000 * oo0oO00
elif iiIi1iI1iIii == 1017 :
 iI1I ( )
 if 31 - 31: iIi1i1ii1 . O0oOO0
elif iiIi1iI1iIii == 1018 :
 Oo0 ( ooO0oOOooOo0 )
 if 40 - 40: IIi - oo0oO00 / IIiIiII11i * ooOoO0O00 + iIi1i1ii1 * IIiIiII11i
elif iiIi1iI1iIii == 1023 :
 OooOoOo ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - OooOO000
elif iiIi1iI1iIii == 1024 :
 O00OO0oO ( ooO0oOOooOo0 )
 if 99 - 99: IIi - iIi1i1ii1 - ooOoO0O00 / Ii . iIi1i1ii1
elif iiIi1iI1iIii == 1025 :
 Ii1IIiii1Ii ( ooO0oOOooOo0 )
 if 58 - 58: Oooo0O0oo00oO
elif iiIi1iI1iIii == 4001 :
 Ooo0OOoOoO0 ( )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif iiIi1iI1iIii == 4002 :
 o00Oo0oooooo ( )
 if 64 - 64: OOooOOo + iIi1i1ii1 - ooOoO0O00 . IIiIiII11i . oO0o
elif iiIi1iI1iIii == 4003 :
 I1III111i ( )
 if 31 - 31: O0oOO0 . iiII11i1I1IIi - oo0oO00 . iI11I1II1I1I + oo0oO00 . OOooOOo
elif iiIi1iI1iIii == 4004 :
 iI1i111I1Ii ( )
 if 86 - 86: Ii1I - Ii1I / iiII11i1I1IIi - Ii1I * iiII11i1I1IIi + OooOO000
elif iiIi1iI1iIii == 4005 :
 i11i1ii1I ( )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - iIi1i1ii1
elif iiIi1iI1iIii == 4006 :
 o0OOOo ( )
 if 30 - 30: ii % Oooo0O0oo00oO
elif iiIi1iI1iIii == 4007 :
 oOo0 ( )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - Oooo0O0oo00oO
elif iiIi1iI1iIii == 4008 :
 o0o0 ( )
 if 81 - 81: iiII11i1I1IIi % IIi . OOoOoo
elif iiIi1iI1iIii == 4009 : ooo ( )
elif iiIi1iI1iIii == 4010 : II1i1III ( )
elif iiIi1iI1iIii == 3000 :
 iioOo00O0o ( )
 if 66 - 66: Ii1I * IIi / ii * o0o00Oo0O % Oooo0O0oo00oO
elif iiIi1iI1iIii == 3001 :
 o00oo ( )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * IIi / OooOO000 * ii
elif iiIi1iI1iIii == 3002 :
 O000Oo00 ( ooO0oOOooOo0 )
 if 82 - 82: I1ii11iIi11i / IIi / IIi % IIi
elif iiIi1iI1iIii == 3003 :
 iI1oOoo ( ooO0oOOooOo0 )
 if 20 - 20: OOoOoo
elif iiIi1iI1iIii == 3004 :
 iIiiII ( ooO0oOOooOo0 )
 if 63 - 63: iI11I1II1I1I . oO0o
elif iiIi1iI1iIii == 404 :
 ooOoOoOoo ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif iiIi1iI1iIii == 405 :
 OO0oO ( ooO0oOOooOo0 )
 if 26 - 26: Oooo0O0oo00oO . oO0o % OOooOOo
elif iiIi1iI1iIii == 7030 :
 II1i1iI ( )
 if 94 - 94: iIi1i1ii1
elif iiIi1iI1iIii == 7021 :
 i1IiI ( Oo0OO )
 if 15 - 15: IIi - iIi1i1ii1 / o0o00Oo0O
elif iiIi1iI1iIii == 7022 :
 Iiii1II ( Oo0OO )
 if 28 - 28: OooOO000 . ooOoO0O00 / Ii1I
elif iiIi1iI1iIii == 7000 :
 iiIi1111iiI1 ( Oo0OO , ooO0oOOooOo0 , img )
 if 77 - 77: Ii / OooOO000 / Ii % OOooOOo - OooOO000
elif iiIi1iI1iIii == 7050 :
 iiIIi ( ooO0oOOooOo0 )
 if 80 - 80: OooOO000 % OOooOOo . ii . IIiIiII11i % iIi1i1ii1
elif iiIi1iI1iIii == 7051 :
 i11ii11IiI1 ( ooO0oOOooOo0 )
 if 6 - 6: OooOO000 % iIi1i1ii1 / IIi + OooOO000 . O0oOO0
elif iiIi1iI1iIii == 7052 :
 ii1i1I1111ii ( ooO0oOOooOo0 )
 if 70 - 70: iI11I1II1I1I / IIi
elif iiIi1iI1iIii == 7053 :
 oo0ooo0O0O0O ( ooO0oOOooOo0 )
 if 61 - 61: o0o00Oo0O * I11i + OooOO000 - Oooo0O0oo00oO . oOo0O0Ooo - iIi1i1ii1
elif iiIi1iI1iIii == 7054 :
 CoolPlay ( ooO0oOOooOo0 )
 if 7 - 7: Ii1I
elif iiIi1iI1iIii == 7060 :
 iI1I1 ( )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / oo0oO00
elif iiIi1iI1iIii == 7061 :
 oO00Oooo0O0o0 ( ooO0oOOooOo0 )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif iiIi1iI1iIii == 7063 :
 oOOo ( ooO0oOOooOo0 )
 if 13 - 13: Ii
elif iiIi1iI1iIii == 7062 :
 iiI1IiI1I1I ( ooO0oOOooOo0 )
 if 54 - 54: Oooo0O0oo00oO . Ii1I * oo0oO00 % OooOO000 . o0o00Oo0O * iIi1i1ii1
elif iiIi1iI1iIii == 7064 :
 NATatozcat ( )
 if 87 - 87: IIi % Ii1I * I1ii11iIi11i
elif iiIi1iI1iIii == 7067 :
 IIIiI1i ( ooO0oOOooOo0 )
 if 59 - 59: I1ii11iIi11i / oo0oO00 - iI11I1II1I1I * iI11I1II1I1I
elif iiIi1iI1iIii == 7066 :
 NATatozA ( ooO0oOOooOo0 )
 if 18 - 18: oo0oO00 * Ii1I / Ii / iI11I1II1I1I * ii . Oooo0O0oo00oO
elif iiIi1iI1iIii == 7065 :
 i1II ( ooO0oOOooOo0 )
 if 69 - 69: I1ii11iIi11i * OOoOoo
elif iiIi1iI1iIii == 7070 :
 i11IIi1Iii1 ( )
 if 91 - 91: I11i . OOoOoo / oO0o / Ii * I11i
elif iiIi1iI1iIii == 7071 :
 DIZIlist ( ooO0oOOooOo0 )
 if 52 - 52: oOo0O0Ooo - Ii / iIi1i1ii1 . O0oOO0
elif iiIi1iI1iIii == 7072 :
 DIZIpull ( ooO0oOOooOo0 )
 if 38 - 38: O0oOO0 + ii * OOooOOo % O0oOO0
elif iiIi1iI1iIii == 7073 :
 WATCHDIZI ( ooO0oOOooOo0 )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif iiIi1iI1iIii == 7002 :
 oOOo0O0Oo ( )
 if 24 - 24: OOooOOo * IIi
elif iiIi1iI1iIii == 7003 :
 ooo0OOoo ( ooO0oOOooOo0 )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif iiIi1iI1iIii == 7004 :
 iiII1iIi1ii1i ( ooO0oOOooOo0 )
 if 81 - 81: Oooo0O0oo00oO
elif iiIi1iI1iIii == 7020 :
 o00oOO00 ( ooO0oOOooOo0 )
 if 58 - 58: IIiIiII11i . OooOO000 . IIi * ii / IIi / oo0oO00
elif iiIi1iI1iIii == 7001 :
 IIIIiIiIi1 ( )
 if 41 - 41: oo0oO00 + oO0o . iiII11i1I1IIi
elif iiIi1iI1iIii == 7010 :
 oo0iIi1iiii1ii ( ooO0oOOooOo0 )
 if 73 - 73: Ii * oOo0O0Ooo + I11i / O0oOO0
elif iiIi1iI1iIii == 7011 :
 i1oo0OO0Oo ( ooO0oOOooOo0 )
 if 56 - 56: ooOoO0O00
elif iiIi1iI1iIii == 7012 :
 I1III1I1IiI ( ooO0oOOooOo0 )
 if 11 - 11: Ii % I11i / oo0oO00 * ii
elif iiIi1iI1iIii == 7013 :
 cnfTVPlay2 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iiIi1iI1iIii == 7018 :
 I1i1IiIIiIiII ( )
elif iiIi1iI1iIii == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooO0oOOooOo0 )
 if 82 - 82: iIi1i1ii1
elif iiIi1iI1iIii == 8000 :
 IiIi11IIi1I11 ( )
elif iiIi1iI1iIii == 8001 :
 i11111iIIiII ( )
elif iiIi1iI1iIii == 8002 :
 IIiIIiIi1II1IiI ( )
elif iiIi1iI1iIii == 8003 :
 i1II111ii1ii ( )
elif iiIi1iI1iIii == 8004 :
 Oo0OO0 ( )
elif iiIi1iI1iIii == 8005 :
 o000Oo0oO0OO0 ( )
elif iiIi1iI1iIii == 8006 :
 I1OoO00o00 ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8030 :
 ii1I111i1Ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8045 :
 Oo00oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8046 :
 oO0oO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8047 :
 IiIii11I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8048 :
 iIiiI1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8049 :
 II1i1I1II1IiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 804900 :
 I11i1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8020 :
 OOOOoO00o0O ( )
elif iiIi1iI1iIii == 8021 :
 ooo0ooo0Oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8022 :
 I1ii1iii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8023 :
 oOoOO0OO0O0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8040 :
 I1iI ( )
elif iiIi1iI1iIii == 8041 :
 oooo0oOOoO000 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8042 :
 o0OO0ooOOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8043 :
 yt . PlayVideo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8044 :
 i1i1I1Ii1IIii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8060 :
 IiI11ii1I ( )
elif iiIi1iI1iIii == 8061 :
 Ii1Ii11I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8064 :
 I1I1I1IIi1III ( )
elif iiIi1iI1iIii == 8065 :
 o0o00O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8070 :
 i1iiII ( )
elif iiIi1iI1iIii == 8071 :
 ooii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7080 :
 oOO0O0O0OO00oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8090 :
 O0ooiIIi1 ( )
elif iiIi1iI1iIii == 8091 :
 oOo000Oo00o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8092 :
 i1iI11Ii1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8093 :
 o0ooOOoOoOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8081 :
 II1i111i ( )
elif iiIi1iI1iIii == 8062 :
 IIi1I1iII111 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8063 :
 Oo0O0oOoO0o0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8050 :
 OO00o ( )
elif iiIi1iI1iIii == 8051 :
 IiiI11i1I1ii1i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8052 :
 oO0ooooo0O00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8085 :
 iii11 ( )
elif iiIi1iI1iIii == 8086 :
 iIii1ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8087 :
 OOOOo0oO0o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8088 :
 iI1iI ( ooO0oOOooOo0 , Oo0OO )
elif iiIi1iI1iIii == 9000 :
 iIiIIi ( )
elif iiIi1iI1iIii == 1111 :
 I11Ii111I ( )
elif iiIi1iI1iIii == 9001 :
 Ooo00Oo ( )
elif iiIi1iI1iIii == 9002 :
 o00o0 ( )
elif iiIi1iI1iIii == 9003 :
 o0o0oo0OOo0O0 ( )
elif iiIi1iI1iIii == 9004 :
 World1 ( )
elif iiIi1iI1iIii == 9005 :
 World2 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9006 :
 World3 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9007 :
 O0000ooO ( )
elif iiIi1iI1iIii == 9008 :
 O00OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9009 :
 I11i11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9010 :
 o00O00oO ( )
elif iiIi1iI1iIii == 9011 :
 OO000O000OOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 50 :
 oO00o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9020 :
 champlist ( )
elif iiIi1iI1iIii == 9021 :
 I1iiiiI ( )
elif iiIi1iI1iIii == 9022 :
 o0oOOO0 ( )
elif iiIi1iI1iIii == 9023 :
 i1Iii ( )
elif iiIi1iI1iIii == 9024 :
 o0OOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9030 :
 OOoOO0oOooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9031 :
 i1II11II11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9032 :
 oooiiI11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9033 :
 i11IiIiii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9034 :
 I11iiiiI1i ( )
elif iiIi1iI1iIii == 7085 :
 O00O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7086 :
 IiIIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7087 :
 oooO00oOOooO ( OOo )
elif iiIi1iI1iIii == 9666 :
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10100 : Oo0oOOO ( )
elif iiIi1iI1iIii == 101001 : iII1ii1IIII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10105 : Iii1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10106 : ooOooo00O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10104 : ooOoOoo000O0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10107 : Oo0o0O0OOOo0 ( )
elif iiIi1iI1iIii == 10103 : I1i1I1IIiIIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10108 : IiIiiIiiiiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10000 : Origin_Menu ( )
elif iiIi1iI1iIii == 10001 : iIii ( )
elif iiIi1iI1iIii == 10002 : o0OO0o0o00o ( )
elif iiIi1iI1iIii == 10003 : IIii1111 ( )
elif iiIi1iI1iIii == 10004 : iII11I1Ii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10005 : OOoOoo0 ( )
elif iiIi1iI1iIii == 10006 : i1iI1Iiii1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10007 : oO0O0o0O ( ooO0oOOooOo0 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 10008 : Iii1I ( )
elif iiIi1iI1iIii == 10009 : OOo0OOOoOOo ( )
elif iiIi1iI1iIii == 10010 : i1iiiIIi11II ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10011 : I11i1I11iIii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10012 : I11I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10109 : i1iI1I1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10013 : iI1i1I1iiii1Ii11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10014 : Ii11 ( )
elif iiIi1iI1iIii == 10015 : I1IiI1IIiI ( )
elif iiIi1iI1iIii == 10016 : OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10017 : IiIi11iiIIiI1 ( )
elif iiIi1iI1iIii == 10018 : o0o ( )
elif iiIi1iI1iIii == 10019 : ooO ( )
elif iiIi1iI1iIii == 10020 : II11II1I ( )
elif iiIi1iI1iIii == 10021 : i1iI ( )
elif iiIi1iI1iIii == 10022 : O0O0oO0oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10023 : iio0oo0Oo ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10024 : I1IIIi1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10025 : ii1II ( )
elif iiIi1iI1iIii == 10026 : OO0oo00oOO ( )
elif iiIi1iI1iIii == 10027 : oOoo00o0oOO ( )
elif iiIi1iI1iIii == 10028 : iiIiIIi11I1 ( )
elif iiIi1iI1iIii == 10029 : I1I11Iiii111 ( )
elif iiIi1iI1iIii == 423 : OooO0O0Ooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 426 : ii111iiIii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10030 : Izle_Films ( )
elif iiIi1iI1iIii == 10031 : Latest_Izle_Movies ( )
elif iiIi1iI1iIii == 10032 : Izle_Genres ( )
elif iiIi1iI1iIii == 10033 : Izle_Pop_Movies ( )
elif iiIi1iI1iIii == 10034 : Izle_Boxsets ( )
elif iiIi1iI1iIii == 10035 : Izle_Search ( )
elif iiIi1iI1iIii == 10036 : Izle_Genres_Movie ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10037 : Izle_Boxset_single ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10038 : Izle_IFRAME ( )
elif iiIi1iI1iIii == 10039 : Izle_Boxsets_Next ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10040 : II1III1I1I1Ii ( )
elif iiIi1iI1iIii == 10041 : O0OiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10042 : iiOo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10043 : oOoOOOO0OOO ( )
elif iiIi1iI1iIii == 10044 : o0oOOoo0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10045 : OoO0o0oOOO ( Oo0OO )
elif iiIi1iI1iIii == 10046 : O0O00O0Oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10047 : oooO0o0oOoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10048 : OOoOO0o0o0Oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10049 : o00OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10050 : OO ( )
elif iiIi1iI1iIii == 10051 : II1iiII1 ( )
elif iiIi1iI1iIii == 10052 : I1IiiIIiIii1i ( )
elif iiIi1iI1iIii == 10053 : Addon ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10054 : ii1ii1iiIiI ( ooO0oOOooOo0 , Oo0OO )
elif iiIi1iI1iIii == 10055 :
 o0IiIiI111IIII1 ( "addFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO0IIIIIIi111i ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 , ii1IiI )
elif iiIi1iI1iIii == 10056 :
 o0IiIiI111IIII1 ( "rmFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 ooo0OO0OOooO0 ( Oo0OO )
elif iiIi1iI1iIii == 10057 :
 o0IiIiI111IIII1 ( "getFavorites" )
 oooOoO00OooO0 ( )
elif iiIi1iI1iIii == 10058 : iiI ( )
elif iiIi1iI1iIii == 10059 : Donators_Guide ( )
elif iiIi1iI1iIii == 10060 : oOo0OOoO0 ( )
elif iiIi1iI1iIii == 10061 : i1iI1 ( )
elif iiIi1iI1iIii == 10062 : iIIi1iiI1i11 ( Oo0OO , ooO0oOOooOo0 , OOo )
elif iiIi1iI1iIii == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif iiIi1iI1iIii == 10064 : oOoooO0 ( )
elif iiIi1iI1iIii == 10065 : Ii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10066 : oo0OoOooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10068 : o0OO0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10069 : II11IiiIII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10070 : oooo0OOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10071 : Genie_Watch ( )
elif iiIi1iI1iIii == 10072 : Oo00OOo00O ( )
elif iiIi1iI1iIii == 10073 : iIIi1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10074 : O0O00oOooo0OO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10075 : iiI11iIi ( iIIiiI1II1i11 , Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10076 : iiIii1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10077 : Oo00OOOOoo0oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10078 : Iii111Ii ( )
elif iiIi1iI1iIii == 10079 : Genie_Watch_Tv_Shows ( )
elif iiIi1iI1iIii == 10080 : Genie_Watch_Tv_Genre ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10081 : Genie_Watch_TV_PlayRun ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10082 : Genie_Watch_TV_Episodes ( ooO0oOOooOo0 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 10083 : Genie_Watch_Tv_Recent ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10084 : oOoO0 ( )
elif iiIi1iI1iIii == 10085 : OOoO00 ( )
elif iiIi1iI1iIii == 10086 : i1IiiiI1iI ( )
elif iiIi1iI1iIii == 20000 : oOo0OoOOo0 ( )
elif iiIi1iI1iIii == 20001 : o0oOo00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20002 : I1IIII1i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20003 : O0O00OoOoOOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20004 : o0II1IIi1iII1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20005 : iiiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21004 : I1iIII1 ( )
elif iiIi1iI1iIii == 21005 : I1ii1Ii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21006 : i111IiiI1Ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21007 : o0ooO00O0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30000 : Oo00OO0 ( )
elif iiIi1iI1iIii == 30001 : ii1iIII ( )
elif iiIi1iI1iIii == 10012 : Resolve ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30003 : Iiii1iI111II1ii ( )
elif iiIi1iI1iIii == 30004 : Ii1III1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30005 : iii1II1iI1IIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30006 : oOOO0ooOO ( )
elif iiIi1iI1iIii == 30007 : O0OoO0o ( )
elif iiIi1iI1iIii == 30008 : ooooOoo0OO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30009 : OooOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30010 : I1iIiiiI1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30011 : O0o00oo0OO0 ( )
elif iiIi1iI1iIii == 30012 : O000O ( )
elif iiIi1iI1iIii == 30013 : I1IiI ( )
elif iiIi1iI1iIii == 30014 : Iiii1 ( )
elif iiIi1iI1iIii == 30015 : II1i11 ( ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 )
elif iiIi1iI1iIii == 30016 : IiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30019 : iIiIIiI1i1Ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30017 : iiII1iiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30018 : i11Iii1Ii1i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30030 : oo00ooOooO ( )
elif iiIi1iI1iIii == 30031 : OOoOOo00O0o0 ( )
elif iiIi1iI1iIii == 30032 : OOOoOO ( )
elif iiIi1iI1iIii == 30033 : ooIi111iII ( )
elif iiIi1iI1iIii == 30034 : Oo0OoOo ( )
elif iiIi1iI1iIii == 30035 : ii11iiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30036 : i11iI11I1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30037 : Ii1iiIi1I11i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30038 : I1I ( )
elif iiIi1iI1iIii == 30039 : oO0O0OO0O ( )
elif iiIi1iI1iIii == 50000 : oOO0O00Oo0O0o ( )
elif iiIi1iI1iIii == 50001 : iiii1 ( )
elif iiIi1iI1iIii == 50002 : IIiII11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 50003 : II11IiI1 ( OOo )
elif iiIi1iI1iIii == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif iiIi1iI1iIii == 60001 : OOOo ( )
elif iiIi1iI1iIii == 60002 : ooOo ( Oo0OO )
elif iiIi1iI1iIii == 60003 : Ii1I1iiiiii ( Oo0OO )
elif iiIi1iI1iIii == 50004 : iI1111iiii ( )
elif iiIi1iI1iIii == 50005 : speedtest . runtest ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70001 : iiI1iii ( )
elif iiIi1iI1iIii == 70002 : O0000oO0o00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70003 : oo000o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70004 : OO00o0oOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70005 : i1i1I1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70006 : I1iOOo0O ( )
elif iiIi1iI1iIii == 50006 : OOOiiiiI ( i1 , i1111 )
elif iiIi1iI1iIii == 80000 : I1I1IiIi1 ( )
elif iiIi1iI1iIii == 80001 : resolvefilmon ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80002 : Ii11i1Ii11I ( )
elif iiIi1iI1iIii == 80003 : Oo0oOo0ooOOOo ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80004 : ii1i1iiI ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80005 : II1iI1I11I ( )
elif iiIi1iI1iIii == 80006 : OOI1iIi1iiIIiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80007 : oOoOOoOOooOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80008 : iIIII1i ( )
elif iiIi1iI1iIii == 80009 : Oooo0Oo00o ( )
elif iiIi1iI1iIii == 80010 : IIoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80011 : IiiI111 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80012 : Oo00O0O ( )
elif iiIi1iI1iIii == 90000 : IiIi ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90001 : I1I1i1I ( )
elif iiIi1iI1iIii == 90002 : i1OOO0000oO ( )
elif iiIi1iI1iIii == 90003 : Ii1I1iIiiI1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90004 : o00i111iiIiiIiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90005 : OOooooO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90006 : Ooo00OOo000 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90007 : i1ooOO00o0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90008 : O0OIIII1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90009 : I1iIIIiiii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90010 : oooOo0OOOoo0 ( )
if 10 - 10: I1ii11iIi11i % Oooo0O0oo00oO / oo0oO00 * iIi1i1ii1 - I11i
if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / iiII11i1I1IIi
elif iiIi1iI1iIii == 100001 : Stand_up ( )
if 1 - 1: OooOO000 / OOooOOo * OOooOOo - I11i % IIi
elif iiIi1iI1iIii == 100003 : OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100004 : O00OoOO0oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100005 : Resolve ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100008 : Search ( )
elif iiIi1iI1iIii == 100007 : OO0oOOoo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100009 : yt . PlayVideo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100010 : oOOO0oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100100 : IiiIiI111iI ( iIIiiI1II1i11 , ooO0oOOooOo0 , i1I11iIIiIIiIi )
elif iiIi1iI1iIii == 100101 : O0iII1 ( ooO0oOOooOo0 , Oo0OO , iiI11ii1I1 , i1I11iIIiIIiIi , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 100102 : oOOoo ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 )
elif iiIi1iI1iIii == 100106 : O0oOo00o0o00O ( ooO0oOOooOo0 , Oo0OO )
elif iiIi1iI1iIii == 100107 : Oo ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
