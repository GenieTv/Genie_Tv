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
IiiIII111iI = "3.2.3"
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
  OOOiiiiI ( 'Change Log 22/10/16 - v3.2.2' , 'Guide skins install button added, tommys football list added, Adult section fixed and new categories added, Complete overhaul of menus, New section added who can find it first???' )
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
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 60 - 60: Ii1I * oOo0O0Ooo
 if 17 - 17: Oooo0O0oo00oO % I1ii11iIi11i / Ii1I . iIi1i1ii1 * Oooo0O0oo00oO - IIiIiII11i
def i1ii1II1ii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 41 - 41: IIi
def oOOoo0o0OOOO ( url ) :
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : i1IiII1III . play ( url ) . strip ( )
 except : pass
 if 77 - 77: iiII11i1I1IIi % Oooo0O0oo00oO - oo0oO00 % OOoOoo - oO0o / I1ii11iIi11i
def iI11I ( url ) :
 i1IiII1III = xbmc . Player ( )
 import urlresolver
 try : i1IiII1III . play ( url )
 except : pass
 if 4 - 4: ii - ooOoO0O00 % IIi - Oooo0O0oo00oO * I11i
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
  if 85 - 85: ii * iI11I1II1I1I . iiII11i1I1IIi / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: IIi / IIiIiII11i / iIi1i1ii1 / iIi1i1ii1 + Ii1I
  if 95 - 95: iIi1i1ii1
def oOo0 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   Ooo0oo ( )
  if O0oO0 == 1 :
   IIi11IIiIii1 ( )
  if O0oO0 == 2 :
   I1iIII1 ( )
  if O0oO0 == 3 :
   iIii ( )
  if O0oO0 == 4 :
   oOo0OoOOo0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
 if 30 - 30: Ii1I % oOo0O0Ooo
 if 89 - 89: OooOO000 + ii + OooOO000 * ooOoO0O00 + iI11I1II1I1I % oo0oO00
 if 59 - 59: Oooo0O0oo00oO + Ii
def IiI111111IIII ( ) :
 I1 = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o00oooO0Oo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiIi1iI in o00oooO0Oo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   oo0OOo0O = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOOiiiiI ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oo0OOo0O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO0 == 0 :
    Ii1IiII ( IIiIi1iI )
    o00O0 ( )
   elif O0oO0 == 1 :
    I1i ( IIiIi1iI )
  else :
   pass
   if 72 - 72: iI11I1II1I1I
def I1i ( addon ) :
 oo0OOo0O = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 11 - 11: IIiIiII11i / I11i
def Ii1IiII ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 IiIi1 = os . path . join ( iIi1ii1I1 , 'default.py' )
 i111iiI1ii = open ( IiIi1 , "w+" )
 if 24 - 24: OOooOOo / ii . IIiIiII11i . oOo0O0Ooo % o0o00Oo0O % IIi
 i111iiI1ii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 i111iiI1ii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 i111iiI1ii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 5 - 5: ii - oO0o + iIi1i1ii1 - iiII11i1I1IIi . oO0o / OOoOoo
 if 28 - 28: IIi * IIi - iI11I1II1I1I
 if 70 - 70: OooOO000
 if 16 - 16: iiII11i1I1IIi - ii % I1ii11iIi11i
def II1iI1I11I ( ) :
 I1i11111i1i11 ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O0 ( 'http://www.join4films.com/' )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def i11i1iIiii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 80007 , O0o0OO0000ooo )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def OOO00OO0oOo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  url = ( url ) . replace ( ' ' , '%20' )
  I1I1iI ( url )
def I1iIi1iiIIiI ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11I = 'http://www.join4films.com/?s=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 iIIII1i = I11I . lower ( )
 i11i1iIiii ( iIIII1i )
 if 76 - 76: iiII11i1I1IIi + OOoOoo
 if 30 - 30: Ii % iI11I1II1I1I . oo0oO00 % iI11I1II1I1I
 if 62 - 62: I1ii11iIi11i * OOooOOo
 if 79 - 79: oO0o . iiII11i1I1IIi * IIi - Oooo0O0oo00oO + OOoOoo
 if 14 - 14: Ii - iiII11i1I1IIi * OOooOOo
 if 51 - 51: Ii1I / iI11I1II1I1I % O0oOO0 + I11i * OOoOoo + OooOO000
 if 77 - 77: OOoOoo * OOooOOo
 if 14 - 14: oo0oO00 % oo0oO00 / iIi1i1ii1
 if 72 - 72: ooOoO0O00 - IIiIiII11i - Oooo0O0oo00oO + Oooo0O0oo00oO * I11i * Oooo0O0oo00oO
 if 33 - 33: I1ii11iIi11i
 if 49 - 49: oO0o % iiII11i1I1IIi % iiII11i1I1IIi / iiII11i1I1IIi
 if 53 - 53: iI11I1II1I1I
 if 68 - 68: ii % IIiIiII11i
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % oo0oO00 * oo0oO00 * Ii1I
 if 24 - 24: IIiIiII11i % OooOO000 - OOoOoo + oOo0O0Ooo * Ii1I
 if 2 - 2: IIi - iIi1i1ii1
 if 83 - 83: O0oOO0 % I11i % IIi - IIiIiII11i * Oooo0O0oo00oO / ii
def IIIiIi ( ) :
 I1IiiiiI ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 if 34 - 34: ii . o0o00Oo0O / O0oOO0 * OOooOOo - Ii1I
def IiiiI ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11I = 'http://imoviemax.se/?s=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 iIIII1i = I11I . lower ( )
 Iii ( iIIII1i )
def i1I1 ( url ) :
 O0II11i11II = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , Oo0OO , II1Ii1iI1i1 in o00oooO0Oo :
  if Oo0OO in O0II11i11II :
   pass
  else :
   I1IiiiiI ( Oo0OO + ' - ' + II1Ii1iI1i1 + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
   O0II11i11II . append ( Oo0OO )
   if 54 - 54: o0o00Oo0O
def OOoO000O00oO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , i1OoOO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + ' - Views:' + i1OoOO , url , 10075 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
  if 44 - 44: Oooo0O0oo00oO
  if 54 - 54: IIi - oo0oO00 - OooOO000 . iI11I1II1I1I
def Iii ( url ) :
 o0OIIiI1I1 = [ ]
 I1 = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IiiiiI ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10075 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
  o0OIIiI1I1 . append ( Oo0OO )
  if 15 - 15: IIi * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
def Oo00OOOOoo0oo ( img , name , url ) :
 img = img
 name = name
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for O00OOooo0Ooo , url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o0oOOoOOO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o0oOOoOOO
  iiI1i11II = ( O00OOooo0Ooo ) . replace ( 'play-' , 'Server ' )
  o0OIiII ( iiI1i11II , o0oOOoOOO , 10076 , img , img , '' )
  if 31 - 31: O0oOO0 / iIi1i1ii1 * I11i . IIiIiII11i
def oooOO0OO0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for OooiiIi1i in o00oooO0Oo :
  if '=m' in OooiiIi1i :
   o00o ( OooiiIi1i )
  elif 'php' in OooiiIi1i :
   oooOO0OO0O ( url )
  else :
   I1 = O0 ( OooiiIi1i )
   o00oooO0Oo = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for III11I in o00oooO0Oo :
    o00o ( OooiiIi1i )
    if 17 - 17: ii + Oooo0O0oo00oO * oo0oO00 * OOooOOo
    if 36 - 36: o0o00Oo0O + I1ii11iIi11i
    if 5 - 5: I1ii11iIi11i * OOooOOo
def ii1I11iIiIII1 ( url ) :
 I1 = O0 ( url )
 oOO0OOOOoooO = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for Ii1IIIIi1ii1I , i1ii11 in oOO0OOOOoooO :
  print 'there ><><><><><><><><><><><><'
  Ii1IIIIi1ii1I = Ii1IIIIi1ii1I
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1ii11 ) )
  for Oo0OO , ii1i in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + Ii1IIIIi1ii1I + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + ii1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
 Ii11i1I11i = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for Ii1IIIIi1ii1I , IIioo0OO in Ii11i1I11i :
  print 'there ><><><><><><><><><><><><'
  Ii1IIIIi1ii1I = Ii1IIIIi1ii1I
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIioo0OO ) )
  for Oo0OO , ii1i in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + Ii1IIIIi1ii1I + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + ii1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
   if 2 - 2: IIiIiII11i - oO0o . iIi1i1ii1 * iiII11i1I1IIi / O0oOO0
   if 80 - 80: Oooo0O0oo00oO / oo0oO00 / OOooOOo + ooOoO0O00 - I1ii11iIi11i
   if 11 - 11: I11i * oO0o
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
  if 15 - 15: OOooOOo
  if 62 - 62: IIi
  if 51 - 51: OOooOOo
  if 14 - 14: iIi1i1ii1 % O0oOO0 % I1ii11iIi11i - Ii
def o0OO0 ( url ) :
 if 53 - 53: IIi % I1ii11iIi11i
 O0ooOo0o0Oo = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for OooiiIi1i , O0o0OO0000ooo , Oo0OO , OooO0oOo in o00oooO0Oo :
  Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O0 ( OooiiIi1i )
  o0O0OOO0Ooo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for iIIiii , OOo in o0O0OOO0Ooo :
   oOOo00O0OOOo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOo ) )
   for o0o0oOoOO0O in oOOo00O0OOOo :
    if Oo0OO in O0ooOo0o0Oo :
     pass
    else :
     o0OIiII ( Oo0OO , iIIiii , 8043 , O0o0OO0000ooo , O0o0OO0000ooo , o0o0oOoOO0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
     O0ooOo0o0Oo . append ( Oo0OO )
     if 31 - 31: oo0oO00 % Oooo0O0oo00oO * oo0oO00
     if 45 - 45: ooOoO0O00 . oOo0O0Ooo + Oooo0O0oo00oO - ii % OOoOoo
def i1I ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , iIIiiI1II1i11 , o0o0oOoOO0O , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10065 , iIIiiI1II1i11 , iiI11ii1I1 , o0o0oOoOO0O )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 7 - 7: Ii . I1ii11iIi11i
def O0O00OOo ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11I = 'https://www.youtube.com/results?search_query=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 iIIII1i = I11I . lower ( )
 I1 = O0 ( iIIII1i )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for ooO0oOOooOo0 in next :
  ooO0oOOooOo0 = 'https://www.youtube.com' + ooO0oOOooOo0
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , ooO0oOOooOo0 , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , OoOOo , OOo in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o00OooO0oo
  ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
  o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , OOo )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , OoOOo in o00oooO0Oo :
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
     o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in ooO0oOOooOo0 or 'elete' in Oo0OO :
    pass
   elif 'hannel' in ooO0oOOooOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooO0oOOooOo0
    I1 = O0 ( ooO0oOOooOo0 )
    iii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in iii1 :
     if 'outube' in ooO0oOOooOo0 or 'list' in ooO0oOOooOo0 :
      pass
     elif 'atch' in ooO0oOOooOo0 :
      ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0o0OO0000ooo , 'http:' + O0o0OO0000ooo , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , '' )
    if 78 - 78: Ii1I + oo0oO00 - o0o00Oo0O
def i1I1iIi1IiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for O0o0OO0000ooo , url , Oo0OO , OoOOo , OOo in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  o00OooO0oo = 'http:' + ( O0o0OO0000ooo ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o00OooO0oo
  url = 'http://www.youtube.com' + url
  o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , OOo )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , url , Oo0OO , OoOOo in o00oooO0Oo :
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
     o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in Oo0OO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O0 ( url )
    iii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for O0o0OO0000ooo , url , Oo0OO in iii1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0o0OO0000ooo , 'http:' + O0o0OO0000ooo , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + OoOOo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o00OooO0oo , o00OooO0oo , '' )
    if 11 - 11: IIiIiII11i
    if 95 - 95: iIi1i1ii1 * Ii1I % OOoOoo % IIi - IIi
def iiI ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  oOoooO0 = open ( O000oo0O )
  o00oooO0Oo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( oOoooO0 ) )
  for o0Oo0 , i1i1II1i11 in o00oooO0Oo :
   if o0Oo0 == 'needs replacing' or i1i1II1i11 == 'needs replacing' :
    o00oiii11II1I ( )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv PRIVATE LIST[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'PrivateList.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv ULTIMATE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
  if 5 - 5: OOooOOo - iIi1i1ii1 * iIi1i1ii1
def IiiIi1IIII1i ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 o00oiii11II1I ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 98 - 98: Oooo0O0oo00oO + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
def iIIi1I1ii ( ) :
 I1IiiiiI ( 'Full List' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'PPV' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Entertainment' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Factual' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Movie Channels' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'US Movie Channels TEST' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Kids' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Music' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'UK Sports' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'International Sports' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'News UK & International' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'German' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'Arabic' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'TV Series Latest' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'VOD Latest' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 I1IiiiiI ( 'VOD Bollywood' , '' , 60003 , oOOOo00O00oOo + 'UltimateList.png' , OO0o , '' )
 if 14 - 14: o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( name ) :
 I1IIII1ii = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , O0o0OO0000ooo , IiIIi1I1I11Ii , ooO0oOOooOo0 in o00oooO0Oo :
  if I1IIII1ii == 'Full List' :
   ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
   o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
  else :
   I1IIII1ii = ( I1IIII1ii ) . replace ( 'World' , 'القنوات العربية' )
   if I1IIII1ii in IiIIi1I1I11Ii :
    ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
    print ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
   else :
    pass
    if 64 - 64: ii
def oO0oooooo ( name ) :
 I1IIII1ii = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , O0o0OO0000ooo , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
  o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , O0o0OO0000ooo , O0o0OO0000ooo , '' )
 else :
  o0OIiII ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 65 - 65: iIi1i1ii1 + I1ii11iIi11i
  if 59 - 59: ii + oo0oO00 . OooOO000 - o0o00Oo0O % iI11I1II1I1I / o0o00Oo0O
  if 88 - 88: I1ii11iIi11i . o0o00Oo0O % ii / Oooo0O0oo00oO
  if 89 - 89: IIiIiII11i / O0oOO0
  if 14 - 14: Oooo0O0oo00oO . oOo0O0Ooo * OOoOoo + IIiIiII11i - OOoOoo + Oooo0O0oo00oO
  if 18 - 18: O0oOO0 - I11i - oOo0O0Ooo - oOo0O0Ooo
  if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / iiII11i1I1IIi . oOo0O0Ooo * OOooOOo
  if 1 - 1: OOooOOo * oO0o . ooOoO0O00 / I1ii11iIi11i . Ii1I + I1ii11iIi11i
  if 17 - 17: I1ii11iIi11i + oO0o / IIi / iiII11i1I1IIi * Oooo0O0oo00oO
  if 29 - 29: oO0o % ii * O0oOO0 / IIiIiII11i - O0oOO0
  if 19 - 19: Ii
  if 54 - 54: IIiIiII11i . oo0oO00
def oOo0OOoO0 ( ) :
 I1IiiiiI ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IiiiiI ( 'Backup Genie Favourites' , ooO0oOOooOo0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( o00OO00OoO ) :
  I1IiiiiI ( 'Backup Ivue Config' , o00OO00OoO , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  I1IiiiiI ( 'Backup Kodi Favourites' , OOOO0OOoO0O0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 73 - 73: OOooOOo . oOo0O0Ooo
  if 32 - 32: OOooOOo * oOo0O0Ooo % OOoOoo * IIi . o0o00Oo0O
  if 48 - 48: iiII11i1I1IIi * iiII11i1I1IIi
zip = oo00 . getSetting ( 'zip' )
I1I1 = xbmc . translatePath ( os . path . join ( zip ) )
def iI1I1iiIi1I ( ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 26 - 26: iIi1i1ii1 / ooOoO0O00 * O0oOO0 . oOo0O0Ooo
  if 17 - 17: IIi . Ii
  if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . OooOO000 - OOoOoo
def o00oo0000 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O0Oo000ooO00
  elif 'Ivue' in name :
   url = o00OO00OoO
  elif 'Kodi' in name :
   url = OOOO0OOoO0O0
  iI1I1iiIi1I ( )
  iIi1IIi1ii = open ( url ) . read ( )
  I11Ii = os . path . join ( I1I1 , description . split ( 'Your ' ) [ 1 ] )
  oOOo0O00o = open ( I11Ii , mode = 'w' )
  oOOo0O00o . write ( iIi1IIi1ii )
  oOOo0O00o . close ( )
 else :
  if 'guisettings.xml' in description :
   iIiII = open ( os . path . join ( I1I1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1i1IIIIIIIi = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   o00oooO0Oo = re . compile ( i1i1IIIIIIIi ) . findall ( iIiII )
   for type , oo0o0oOo , OO0oOOo0o in o00oooO0Oo :
    OO0oOOo0o = OO0oOOo0o . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oo0o0oOo , OO0oOOo0o ) )
  else :
   I11Ii = os . path . join ( url )
   iIi1IIi1ii = open ( os . path . join ( I1I1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0O00o = open ( I11Ii , mode = 'w' )
   oOOo0O00o . write ( iIi1IIi1ii )
   oOOo0O00o . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 50 - 50: iiII11i1I1IIi . Ii1I . oO0o * oo0oO00 + IIiIiII11i % Ii
 if 8 - 8: OOoOoo * o0o00Oo0O
 if 73 - 73: I11i / O0oOO0 / oo0oO00 / oO0o
 if 11 - 11: OOooOOo + iIi1i1ii1 - ii / oO0o
def iIIi1iI1I1IIi ( ) :
 O0OO0 = 1
 iI1I1iiIi1I ( )
 O0ooo0o0 = xbmc . translatePath ( os . path . join ( I1I1 , 'Build Backup' , 'Full Backup' , '' ) )
 oO0ooOoO = xbmc . translatePath ( os . path . join ( I1I1 , 'Build Backup' , 'my_full_backup.zip' ) )
 ooO0000o00O = xbmc . translatePath ( os . path . join ( I1I1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( O0ooo0o0 ) :
  os . makedirs ( O0ooo0o0 )
 O0Ooo = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not O0Ooo ) : return False , 0
 oO00oOOo0Oo = O0Ooo
 IIiIIIIii = xbmc . translatePath ( os . path . join ( O0ooo0o0 , oO00oOOo0Oo + '.zip' ) )
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
 oO0O000oOoo0O = xbmc . translatePath ( os . path . join ( O0ooo0o0 , oO00oOOo0Oo + '_guisettings.zip' ) )
 iIIiii11iIiiI = zipfile . ZipFile ( oO0O000oOoo0O , mode = 'w' )
 try :
  iIIiii11iIiiI . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iIIiii11iIiiI . close ( )
 if O0OO0 == 0 :
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
     Iiio0Oo0oO = '01/01/1980'
     iIII1iiIi11 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1IIi1i1Ii1 ) ) )
     if iIII1iiIi11 > Iiio0Oo0oO :
      o0000 . write ( i1IIi1i1Ii1 , i1IIi1i1Ii1 [ i111i1i : ] )
 o0000 . close ( )
 o0oOoO00o . close ( )
 if 84 - 84: Ii * oO0o
 if 18 - 18: Oooo0O0oo00oO - IIi - OOooOOo / OooOO000 - o0o00Oo0O
def OooOoOo ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
 if 14 - 14: I11i / Oooo0O0oo00oO - iI11I1II1I1I - O0oOO0 % OOoOoo
def I1iIiI1IiIIII ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ooo00Oo ( )
 if O0oO0 == 1 :
  o00o0 ( )
 if O0oO0 == 2 :
  Ooo0oo ( )
 if O0oO0 == 3 :
  O0O00OOo ( )
  if 18 - 18: OOoOoo % Ii . iI11I1II1I1I - iiII11i1I1IIi
  if 80 - 80: oOo0O0Ooo + O0oOO0 - ooOoO0O00 . IIi / I11i / oOo0O0Ooo
  if 1 - 1: oo0oO00 + Ii - oOo0O0Ooo / Oooo0O0oo00oO + OooOO000
  if 80 - 80: O0oOO0 + I11i * IIi + oO0o
  if 75 - 75: oo0oO00 / I11i / Oooo0O0oo00oO / iIi1i1ii1 % OOoOoo + IIiIiII11i
  if 4 - 4: iiII11i1I1IIi - I1ii11iIi11i - iIi1i1ii1 - oo0oO00 % Ii / oO0o
  if 50 - 50: OOoOoo + ooOoO0O00
  if 31 - 31: IIi
  if 78 - 78: Ii + I11i + OooOO000 / I11i % iI11I1II1I1I % iIi1i1ii1
def Oo0O0Oo00O ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I11IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , iIIiiI1II1i11 , Oo0OO )
  if O0oO0 == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if O0oO0 == 2 :
   iIoo0ooooO ( )
  if O0oO0 == 3 :
   iiIIi ( )
  if O0oO0 == 4 :
   i1i ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO0 == 5 :
   iIIiI1iiI ( )
  if O0oO0 == 6 :
   I11Ii111I ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO0 == 7 :
   Oo00OO0 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO0 == 8 :
   oo0O ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO0 == 9 :
   oO00OoOOOo ( )
  if O0oO0 == 10 :
   Oo0o0OOOOO0O ( )
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
  if 35 - 35: IIi - IIi + ooOoO0O00 - o0o00Oo0O - OooOO000
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 58 - 58: OOooOOo - iiII11i1I1IIi - ii
def o00ii111Iiii ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   oo0oO0o0 ( )
  if O0oO0 == 1 :
   iI1111iiii ( )
  if O0oO0 == 2 :
   oOO0O00Oo0O0o ( )
  if O0oO0 == 3 :
   O0ooO0Oo00o ( ooO0oOOooOo0 )
  if O0oO0 == 4 :
   Iii1Ii ( ooO0oOOooOo0 )
  if O0oO0 == 5 :
   o00O0 ( )
  if O0oO0 == 6 :
   ii11I11i ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO0 == 7 :
   oOOOO ( )
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
  if 48 - 48: OooOO000 + iiII11i1I1IIi
  if 16 - 16: iI11I1II1I1I % Ii . OOooOOo % OOoOoo + O0oOO0 . oO0o
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 46 - 46: oO0o - I11i / OOooOOo - ii + O0oOO0
 if 58 - 58: I11i / I11i + OOoOoo + oo0oO00 - OOooOOo . Oooo0O0oo00oO
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
 if 15 - 15: OOoOoo * OOooOOo % iIi1i1ii1 . OOooOOo . oo0oO00
 if 97 - 97: O0oOO0
def oOoO0O00oo ( ) :
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
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / iiII11i1I1IIi * O0oOO0
def IIo0Oo0oO0oOO00 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , OO0o , '' )
 if 29 - 29: I11i
def oo0 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , OO0o , '' )
 o0OIiII ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , OO0o , '' )
 if 2 - 2: ii
 if 60 - 60: oO0o
 if 81 - 81: OOooOOo % IIi
def OoOoO ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  oo0i1iIIi1II1iiI ( )
 if O0oO0 == 0 :
  III1Ii1i1I1 ( ooO0oOOooOo0 )
 if O0oO0 == 0 :
  O0O00OooO ( ooO0oOOooOo0 )
  if 40 - 40: oo0oO00 % ii - Oooo0O0oo00oO + I11i / Oooo0O0oo00oO
  if 84 - 84: o0o00Oo0O
  if 11 - 11: IIiIiII11i / Ii / o0o00Oo0O
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 94 - 94: OOoOoo * oo0oO00 - iIi1i1ii1 . iI11I1II1I1I
def O000oO0O ( ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o00oooO0Oo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O0o0O00Oo0o0 )
 for O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , O0o0OO0000ooo , O0o0OO0000ooo , '' )
 Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
 if 93 - 93: OooOO000 + IIi
def i1i1 ( url ) :
 O0o0O00Oo0o0 = O0 ( i1IiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 22 - 22: oo0oO00 * o0o00Oo0O . IIiIiII11i - oO0o
def oo0i1iIIi1II1iiI ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 90 - 90: O0oOO0
def O00OO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o000Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 82 - 82: OooOO000 - Oooo0O0oo00oO + oO0o
def OO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iIiiIi11IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 64 - 64: ii . Ii1I % o0o00Oo0O + oOo0O0Ooo - I11i
def ooo0oo00O00oO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oOOooooo0OoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 11 - 11: ooOoO0O00 % oO0o % iiII11i1I1IIi
def O0Oo0 ( url ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . Oooo0O0oo00oO + oO0o - OooOO000
def III1Ii1i1I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iI1iIiiiI1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 40 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 78 - 78: O0oOO0 / oO0o - O0oOO0 * ii . OOooOOo
def OOoooOoO0Oo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + Oo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 48 - 48: Ii % O0oOO0
def oO0O0OO0O ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  i11i11 ( )
 if O0oO0 == 1 :
  Ii11Iii ( )
 if O0oO0 == 2 :
  ooo00OoOO0o ( )
  if 93 - 93: iI11I1II1I1I + O0oOO0 % OOoOoo
  if 21 - 21: Oooo0O0oo00oO
  if 6 - 6: iIi1i1ii1
  if 46 - 46: iIi1i1ii1 + O0oOO0
def Ii11Iii ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo00o0O0O in o00oooO0Oo :
  I1i11111i1i11 ( 'Android Apps' + Oo00o0O0O , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for ooO0oOOooOo0 , Oo00o0O0O in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'Android Games' + Oo00o0O0O , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o0ooO0OoOo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/cat' in url :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def o0oOO00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/app' in url :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def ii11iiIi ( url ) :
 OOoO = O0 ( url )
 i11iI11I1I = url
 if "page=" in str ( url ) :
  i11iI11I1I = url . split ( '?' ) [ 0 ]
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'apk' in url :
   o0OIiII ( ( Oo0OO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + O0o0OO0000ooo )
 if len ( o0O0OOO0Ooo ) > 1 :
  o0O0OOO0Ooo = str ( o0O0OOO0Ooo [ len ( o0O0OOO0Ooo ) - 1 ] )
 o0OIiII ( 'Next Page' , i11iI11I1I + str ( o0O0OOO0Ooo ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def Ii1iiIi1I11i ( name , url ) :
 OOoO = oo0O0o00o0O ( url )
 name = name
 o00oooO0Oo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  url = 'https://www.apkfiles.com' + url
  O0OOO ( name , url , 'Brackets' )
def ooo00OoOO0o ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11I = 'https://www.apkfiles.com/search?q=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 iIIII1i = I11I . lower ( )
 ii11iiIi ( iIIII1i )
 if 37 - 37: o0o00Oo0O - oo0oO00
def IiI1 ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( O0oO , 'Download' ) )
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
 if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - Oooo0O0oo00oO % I11i
def I111i1Ii1i1 ( url ) :
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
 if 11 - 11: OOooOOo % iIi1i1ii1
 if 53 - 53: OOoOoo / iI11I1II1I1I - oO0o + O0oOO0
def ii1IIIIiI11I ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , name )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iiiI11iIIi1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iiiI11iIIi1
 print '======================================='
 extract . all ( Ii1I1Ii , iiiI11iIIi1 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 72 - 72: iiII11i1I1IIi * Oooo0O0oo00oO
 if 67 - 67: ooOoO0O00
 if 5 - 5: IIiIiII11i . ii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: ii - OooOO000 / oO0o
def i11i11 ( ) :
 O0o0O00Oo0o0 = O0 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , ooO0oOOooOo0 , O0OooOo0o , iiI11ii1I1 , iii11i1 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 80003 , O0OooOo0o , oOOOo00O00oOo + 'APKToolsB.png' , iii11i1 )
def i1IiI1I111iIi ( apk , ret = None ) :
 if apk == "kodi" :
  IiiIIi1 = "https://kodi.tv/download/"
  O0o0O00Oo0o0 = O0 ( IiiIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O0o0O00Oo0o0 )
  if len ( o00oooO0Oo ) == 1 :
   iI1iIiiI = o00oooO0Oo [ 0 ] [ 0 ]
   oO00oOOo0Oo = o00oooO0Oo [ 0 ] [ 1 ]
   Oo0OOo = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( iI1iIiiI , oO00oOOo0Oo )
  if ret == 'version' : return iI1iIiiI
  else : return Oo0OOo
 elif apk == "spmc" :
  Ii1I11i11I1i = 'https://github.com/koying/SPMC/releases/latest/'
  O0o0O00Oo0o0 = O0 ( Ii1I11i11I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O0o0O00Oo0o0 )
  iI1iIiiI = re . sub ( '<[^<]+?>' , '' , o00oooO0Oo [ 0 ] ) . replace ( ' ' , '' )
  Oo0OOo = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( iI1iIiiI , iI1iIiiI )
  if ret == 'version' : return iI1iIiiI
  else : return Oo0OOo
def O0OOO ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  oO00 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not oO00 : IiI1II11iiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  o0oOOooo00O = name
  if oO00 :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not I1i1I11I ( url ) == True : IiI1II11iiI ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % o0oOOooo00O , '' , 'Please Wait' )
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
       OO0ooo0 = file . split ( '/' ) [ 1 ]
       oOOo0O00o . write ( iIIiii11iIiiI . read ( file ) )
       xbmc . sleep ( 500 )
       oOOo0O00o . close ( )
       try :
        os . remove ( Ii1I1Ii )
       except :
        pass
       Ii1I1Ii = os . path . join ( oooOOOOO , OO0ooo0 )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : IiI1II11iiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : IiI1II11iiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 7 - 7: Ii1I - O0oOO0 * Oooo0O0oo00oO + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * IIi
 if 19 - 19: IIi
def O0o00oO0oOO ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O0o0O00Oo0o0 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  ooO0oOOooOo0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + ooO0oOOooOo0 )
  iiiii1I1III1 ( ( Oo0OO ) . replace ( '_' , ' ' ) , ooO0oOOooOo0 )
  if 12 - 12: iiII11i1I1IIi . OOooOOo * oOo0O0Ooo
def iiiii1I1III1 ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  oO00 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not oO00 : IiI1II11iiI ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  o0oOOooo00O = name
  if oO00 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not I1i1I11I ( url ) == True : IiI1II11iiI ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % o0oOOooo00O , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : IiI1II11iiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : IiI1II11iiI ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 37 - 37: Ii1I * oOo0O0Ooo % Ii % ooOoO0O00 % iIi1i1ii1
 if 15 - 15: iI11I1II1I1I . o0o00Oo0O
def O0o0O ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 6 - 6: IIiIiII11i
 if 7 - 7: IIi % ooOoO0O00 * ii * o0o00Oo0O + iiII11i1I1IIi
def oooO ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 30015 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 95 - 95: ii + oo0oO00 - Ii1I / Ii1I . ooOoO0O00 . ii
def I1iiI1II ( url , iconimage , fanart ) :
 O0o0O00Oo0o0 = O0 ( url )
 o0oOOoOOO = url
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
 if 44 - 44: I1ii11iIi11i / ooOoO0O00 + iI11I1II1I1I / iI11I1II1I1I * iI11I1II1I1I . IIi
def Oo ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  ii1IIi1ii ( url )
  if 85 - 85: ii % OOooOOo * iI11I1II1I1I
def IiI ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  o0o0OO0o00o0O ( url )
  if 28 - 28: oO0o - O0oOO0 + OOooOOo + IIi / iI11I1II1I1I
def iiiii11I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'desc="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Ii1 in o00oooO0Oo :
  OOOiiiiI ( 'Description:' , Ii1 )
  if 77 - 77: Oooo0O0oo00oO / IIiIiII11i + iIi1i1ii1 + OOoOoo - Ii
def IiIIiI ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 url = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for OooiiIi1i , Oo0OO in o00oooO0Oo :
  if 'png' in Oo0OO :
   o0OIiII ( 'image' , '' , '' , url + '/' + OooiiIi1i , url + '/' + OooiiIi1i , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 87 - 87: OOooOOo % iI11I1II1I1I
def o0OO0OOO0O ( name , url , description ) :
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
 if 36 - 36: Ii / iiII11i1I1IIi . oo0oO00 + iIi1i1ii1 . o0o00Oo0O + oOo0O0Ooo
 if 36 - 36: ooOoO0O00 - Ii1I - OooOO000
def o0o0OO0o00o0O ( url ) :
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
 oo0oO0o0 ( )
 if 7 - 7: Ii + oOo0O0Ooo
def ii1IIi1ii ( url ) :
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
 oo0oO0o0 ( )
 if 47 - 47: OooOO000 - Oooo0O0oo00oO / OOoOoo - I1ii11iIi11i + iiII11i1I1IIi - iI11I1II1I1I
def o0OOOOO0 ( name , url , description ) :
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
 oo0oO0o0 ( )
 if 79 - 79: IIiIiII11i - OOoOoo . ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * oOo0O0Ooo
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
  Ii1Ii1I = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOo0O00o . write ( Ii1Ii1I . rstrip ( '\r\n' ) + '\n' )
def oo0oO0o0 ( ) :
 O0oO0 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO0 == 0 : return
 elif O0oO0 == 1 : pass
 oOO0oo = ii1iII1II ( )
 ii1 ( "Platform: " + str ( oOO0oo ) )
 os . _exit ( 1 )
 ii1 ( "Force close failed!  Trying alternate methods." )
 if oOO0oo == 'osx' :
  ii1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOO0oo == 'linux' :
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
 elif oOO0oo == 'android' :
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
 elif oOO0oo == 'windows' :
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
  if 71 - 71: ooOoO0O00 - oo0oO00 * OooOO000 + O0oOO0 - oO0o % Ii1I
  if 63 - 63: iI11I1II1I1I + Oooo0O0oo00oO . oO0o / oOo0O0Ooo
  if 84 - 84: ooOoO0O00
def O0O00OooO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( url ) :
  for file in II1IIIii :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    iIiII = open ( ( os . path . join ( IiIIiii1I , file ) ) ) . read ( )
    ooooo0Oo0 = iIiII . replace ( I11 , 'special://home/' )
    oOOo0O00o = open ( ( os . path . join ( IiIIiii1I , file ) ) , mode = 'w' )
    oOOo0O00o . write ( str ( ooooo0Oo0 ) )
    oOOo0O00o . close ( )
 oo0oO0o0 ( )
 if 97 - 97: iIi1i1ii1 . O0oOO0 . iIi1i1ii1
def iIoo0ooooO ( ) :
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 91 - 91: Oooo0O0oo00oO + OooOO000 . oo0oO00
def i1I111i1ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def oO0oOoo0O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def II1iI11 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , O0o0OO0000ooo )
def O00o0O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1I1iI ( url )
def O00oOo0O0o00O ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO
 ooo0oo00O00Oo = 'https://www.radionomy.com/en/search/index?query=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 I1 = O0 ( ooo0oo00O00Oo )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + ooO0oOOooOo0 , 70005 , O0o0OO0000ooo )
  if 87 - 87: OOooOOo * iiII11i1I1IIi + iIi1i1ii1 % iiII11i1I1IIi % Oooo0O0oo00oO
  if 51 - 51: iiII11i1I1IIi - OOooOOo % Ii
def iIIiI1iiI ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://www.listenlive.eu/' + ooO0oOOooOo0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def i1i ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 6 - 6: IIi - oO0o . oOo0O0Ooo - o0o00Oo0O
def I11111iI1i111 ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.toonjet.com/' + ooO0oOOooOo0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i111 ( url ) :
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
def III11i1iIIiiI ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 95 - 95: oo0oO00
  if 44 - 44: Oooo0O0oo00oO + oo0oO00 . iIi1i1ii1 / IIiIiII11i % iI11I1II1I1I + iIi1i1ii1
def Oo0o0OOOOO0O ( ) :
 O0OOo ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 O0OOo ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 30 - 30: OooOO000 - I1ii11iIi11i
def ooI111iiiii1 ( ) :
 O0OOo ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 O0OOo ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 O0OOo ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 100 - 100: Ii1I * Ii % O0oOO0 / I1ii11iIi11i / OOoOoo + Ii1I
def o00ooOoo ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , i111i1I1ii1i in o00oooO0Oo :
  if 'Parent' in Oo0OO :
   pass
  elif '2' in i111i1I1ii1i :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 100 - 100: iIi1i1ii1 . IIi - iI11I1II1I1I . Ii / IIiIiII11i
def o0oO0OO00oo0o ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , i111i1I1ii1i in o00oooO0Oo :
  if oOoOOoOOooOO in Oo0OO . lower ( ) :
   if '1' in i111i1I1ii1i :
    O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in i111i1I1ii1i :
    O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in i111i1I1ii1i :
    O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 17 - 17: iIi1i1ii1 / Ii1I - I11i * Ii1I
    if 42 - 42: IIi
def O0o00oo0OO0 ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , i111i1I1ii1i in o00oooO0Oo :
  if '1' in i111i1I1ii1i :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in i111i1I1ii1i :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in i111i1I1ii1i :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 60 - 60: OOoOoo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: oo0oO00 / OOoOoo % ooOoO0O00 - O0oOO0 . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( url ) :
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
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 17 - 17: IIi / iI11I1II1I1I - oO0o + oOo0O0Ooo % Oooo0O0oo00oO
   if 14 - 14: I11i % iIi1i1ii1 + Ii1I + oO0o
   if 76 - 76: oO0o - Ii + OOooOOo + Oooo0O0oo00oO / ii
def IiI1Iii1 ( url ) :
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
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OooiiIi1i + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
   if 67 - 67: IIiIiII11i / I11i . Oooo0O0oo00oO . ii
def i1I1Ii11i ( ) :
 O0OOo ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 O0OOo ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 O0OOo ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 19 - 19: iIi1i1ii1 - I11i . iI11I1II1I1I . OOooOOo / Oooo0O0oo00oO
def OOO0O00Oo ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo in o00oooO0Oo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in O0o0OO0000ooo :
   pass
  else :
   O0OOo ( O0o0OO0000ooo , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooO0oOOooOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + O0o0OO0000ooo + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 13 - 13: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: ooOoO0O00 * O0oOO0 - O0oOO0 + ii % OOooOOo / OOooOOo
 if 3 - 3: ii
def O0OoO0o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 1 - 1: OOoOoo % oo0oO00 * Ii1I - IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: O0oOO0 - iiII11i1I1IIi % OOooOOo
def Ooo0OOO ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if oOoOOoOOooOO in Oo0OO . lower ( ) :
   if '</a>' in Oo0OO :
    pass
   elif '(' in Oo0OO :
    O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 94 - 94: Ii % ii / oOo0O0Ooo
    if 24 - 24: oOo0O0Ooo * O0oOO0
def Oo0O0000Oo00o ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: iiII11i1I1IIi . Ii * o0o00Oo0O
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + iIi1i1ii1
def iI111II1ii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in o00oooO0Oo :
  OooiiIi1i = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OooiiIi1i )
  if 62 - 62: iiII11i1I1IIi * iI11I1II1I1I . iIi1i1ii1 - ii * IIiIiII11i
def IiIIi1II1i ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '<p align' in Oo0OO :
   pass
  elif '&nbsp;' in Oo0OO :
   pass
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 81 - 81: o0o00Oo0O - IIi + I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: IIi
 if 43 - 43: oO0o % oO0o
def IIi11IIiIii1 ( ) :
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
def IIiii11ii1i ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 II1iI1IIi = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , O0o0OO0000ooo , O0o0OO0000ooo , Oo0OO )
 for url , Oo0OO in II1iI1IIi :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def Ii11iiI1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 i1IiII1III = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 oO0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 OOoooO00o0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in oO0O :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , Oo0OO in i1IiII1III :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def I1ii1Ii1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 73 - 73: o0o00Oo0O . O0oOO0 + Ii + iI11I1II1I1I - oo0oO00 / OOooOOo
def iIii ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 o00oooO0Oo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '9cart' in ooO0oOOooOo0 :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 99 - 99: Ii1I * O0oOO0 * Ii1I - IIiIiII11i + IIi
def OOooO0Oo00 ( url ) :
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
   if 9 - 9: iIi1i1ii1
def iIIIIi ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20003 , O0o0OO0000ooo )
 for url , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 50 - 50: OooOO000 + OOoOoo + iiII11i1I1IIi
def ii11iiI11I ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'Watch' in url :
   I1i11111i1i11 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 96 - 96: iI11I1II1I1I + Ii - I1ii11iIi11i . OOoOoo
def iiIi11i1IiI ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 88 - 88: Ii1I - IIi * OOooOOo
def OOOOO0o0OOo ( url ) :
 url = cloudflare . source ( url )
 o00o ( url )
 if 40 - 40: iIi1i1ii1 * O0oOO0 % oo0oO00 * Ii1I
def OoOoOOoO ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . recompile ( 'src="([^"]*)"' )
 for url in o00oooO0Oo :
  o00o ( url )
  if 19 - 19: iI11I1II1I1I * ii * Ii
  if 79 - 79: iIi1i1ii1 % oO0o
def I1iIII1 ( ) :
 if 81 - 81: Ii + Ii * oO0o + iIi1i1ii1
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 if 32 - 32: o0o00Oo0O . ii
def Ooo0oo ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 15 - 15: oOo0O0Ooo . oO0o
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 17 - 17: Ii / I1ii11iIi11i . oO0o / oOo0O0Ooo
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if oOoOOoOOooOO in Oo0OO . lower ( ) :
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
    if 38 - 38: ooOoO0O00 . Ii1I % IIi + iI11I1II1I1I + o0o00Oo0O
    if 47 - 47: oO0o + iIi1i1ii1 / IIiIiII11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: Ii1I / oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - OOoOoo
def oOo0OoOOo0 ( url ) :
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
 if 38 - 38: I11i % OooOO000 + Ii + iiII11i1I1IIi + OOoOoo / Ii
def o0OOOOOo0 ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for O0o0OO0000ooo in o0O0OOO0Ooo :
  oooOoO = O0o0OO0000ooo
 o0OOo00OoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in o0OOo00OoO :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10007 , oooOoO )
  if 62 - 62: Oooo0O0oo00oO / IIiIiII11i + OOooOOo % OOoOoo / OOooOOo + Ii1I
  if 2 - 2: Ii - OooOO000 + oO0o % oo0oO00 * IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: o0o00Oo0O - iiII11i1I1IIi . Oooo0O0oo00oO % iiII11i1I1IIi + iiII11i1I1IIi
def i1iI1Iiii1I ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   I1iII ( url )
   if 29 - 29: ooOoO0O00 % iiII11i1I1IIi / iIi1i1ii1 + OOooOOo - Oooo0O0oo00oO - Ii1I
   if 69 - 69: iI11I1II1I1I . IIiIiII11i . ooOoO0O00 - I11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 79 - 79: OOoOoo % Oooo0O0oo00oO
def I1iII ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1I1iI ( url )
  if 54 - 54: OOooOOo - OooOO000
  if 65 - 65: OooOO000 . OOoOoo + Oooo0O0oo00oO / I1ii11iIi11i + iIi1i1ii1 % ooOoO0O00
  if 28 - 28: Ii + o0o00Oo0O / Ii1I
def IIii1111 ( ) :
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , OO0o , '' )
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
def I1I1IIiiii1ii ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'elete' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 222 , O0o0OO0000ooo )
   if 92 - 92: O0oOO0 / Oooo0O0oo00oO . Ii1I
def i1iOO ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO00OoooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , IIIi , i1iII1IiiIiI1 in OO00OoooO :
  for oOoOOoOOooOO in IIIi :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ii1iiI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for ooO0oOOooOo0 , Oo0OO in Ii1iiI1 :
    if 'tube' in ooO0oOOooOo0 :
     pass
    elif 'stage' in ooO0oOOooOo0 :
     OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + IIIi + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0o0OO0000ooo , )
    elif 'vee' in ooO0oOOooOo0 :
     pass
     if 76 - 76: IIi * iI11I1II1I1I
def iiI1iI ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO00OoooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , IIIi , i1iII1IiiIiI1 in OO00OoooO :
  Ii1iiI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for ooO0oOOooOo0 , Oo0OO in Ii1iiI1 :
   if 'tube' in ooO0oOOooOo0 :
    pass
   elif 'stage' in ooO0oOOooOo0 :
    OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + IIIi + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0o0OO0000ooo )
   elif 'vee' in ooO0oOOooOo0 :
    pass
    if 84 - 84: ii + OooOO000 / oOo0O0Ooo % Oooo0O0oo00oO % Ii1I * oOo0O0Ooo
    if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / O0oOO0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: oOo0O0Ooo * ooOoO0O00 % OOoOoo / o0o00Oo0O + Ii
def OoO ( url ) :
 I1 = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 iIIiii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( iIIiii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in iIIiii :
  I1I1iI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 12 - 12: Ii1I / IIi
  if 5 - 5: ii
  if 18 - 18: oOo0O0Ooo % ii - iiII11i1I1IIi . Ii * I1ii11iIi11i % IIi
  if 12 - 12: ooOoO0O00 / Oooo0O0oo00oO % OOoOoo * iIi1i1ii1 * o0o00Oo0O * iI11I1II1I1I
  if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * O0oOO0 . ii
  if 54 - 54: o0o00Oo0O / iIi1i1ii1 % OOoOoo * ooOoO0O00 * o0o00Oo0O
  if 48 - 48: I11i . O0oOO0 % OOooOOo - OOooOOo
def ii1II ( ) :
 if 33 - 33: oo0oO00 % IIiIiII11i + oO0o
 OoIi1I1I ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 OoIi1I1I ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 56 - 56: o0o00Oo0O
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 45 - 45: OOooOOo - oO0o - OOooOOo
def IIiiI ( ) :
 OoIi1I1I ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 OoIi1I1I ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 36 - 36: iiII11i1I1IIi
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def O0ooooooo00 ( ) :
 if 28 - 28: OOoOoo * oo0oO00 % Ii * iiII11i1I1IIi / IIi
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 iIII1iIi = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 75 - 75: IIi - oo0oO00 % OOooOOo
 for o00oIIi1i1 in iIII1iIi :
  o0O0Ooo = oOOoo0Oo + o00oIIi1i1 + IIIII
  I1 = Oo0OoO00oOO0o ( o0O0Ooo )
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    O0o ( Oo0OO , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , iiI11ii1I1 , o0o0oOoOO0O )
    if 63 - 63: iIi1i1ii1 - ooOoO0O00 * I11i + ii
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 11 - 11: iIi1i1ii1 + iI11I1II1I1I . Ii - Oooo0O0oo00oO
    if 49 - 49: OOoOoo . IIiIiII11i
def IioOooOOo00ooO ( ) :
 if 71 - 71: OooOO000 - I11i - Oooo0O0oo00oO
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 iIII1iIi = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 28 - 28: iI11I1II1I1I
 for o00oIIi1i1 in iIII1iIi :
  iI11II1i1I1 = oOOoo0Oo + o00oIIi1i1 + IIIII
  I1 = Oo0OoO00oOO0o ( iI11II1i1I1 )
  o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    OoIi1I1I ( Oo0OO , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
    if 72 - 72: iiII11i1I1IIi - ii
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * O0oOO0
    if 30 - 30: oo0oO00 % OOooOOo / Ii1I * o0o00Oo0O * IIi . oOo0O0Ooo
def iIi11I11 ( ) :
 if 40 - 40: iI11I1II1I1I
 OOoO = O0 ( oOOoo0Oo + 'spongemain.php' )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
  OoIi1I1I ( Oo0OO , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def oOoOo0o00o ( url ) :
 if 2 - 2: IIiIiII11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0ooo0o0 = ( '%s%s' % ( O00Oooo00 , url ) )
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in o00oooO0Oo :
  ooO0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
  for iII1111III1I in ooO0 :
   if iII1111III1I == url :
    Oo0OO = ( '[COLORred]Watched - [/COLOR]' + Oo0OO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  O0o ( Oo0OO , url , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
  if 34 - 34: ooOoO0O00 % iIi1i1ii1
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 80 - 80: ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 94 - 94: ooOoO0O00
  if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
def iIIiiiI1iI1 ( url ) :
 if 86 - 86: Ii1I * OOoOoo
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , o0o0oOoOO0O , url , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in o00oooO0Oo :
  OoIi1I1I ( Oo0OO , url , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
  if 70 - 70: Oooo0O0oo00oO * O0oOO0 / oOo0O0Ooo * OOooOOo * oOo0O0Ooo
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 61 - 61: O0oOO0 + Ii1I / ooOoO0O00 * O0oOO0
  if 90 - 90: IIi % O0oOO0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: ii / Ii / OooOO000
def O0o ( name , url , mode , iconimage , fanart , description ) :
 if 60 - 60: oOo0O0Ooo % O0oOO0 / I11i % O0oOO0 * Ii / iiII11i1I1IIi
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 34 - 34: OooOO000 - Oooo0O0oo00oO
def OoIi1I1I ( name , url , mode , iconimage , fanart , description ) :
 if 25 - 25: O0oOO0 % oOo0O0Ooo + Ii + o0o00Oo0O * ii
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
if 64 - 64: ooOoO0O00
if 10 - 10: OooOO000 % o0o00Oo0O / oOo0O0Ooo % oo0oO00
if 25 - 25: IIiIiII11i / oO0o
if 64 - 64: o0o00Oo0O % OOoOoo
if 40 - 40: I11i + oo0oO00
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
def i1Ii11ii1I ( string ) :
 if Oo0oOOo == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 66 - 66: I1ii11iIi11i / ii % OooOO000 / iiII11i1I1IIi + ii
def ii1III1iiIi ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1ii1iI = [ ]
 try :
  if 99 - 99: I11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  i1Ii11ii1I ( 'Making Favorites File' )
  I1ii1iI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iIiII = open ( I1IIiiIiii , "w" )
  iIiII . write ( json . dumps ( I1ii1iI ) )
  iIiII . close ( )
 else :
  i1Ii11ii1I ( 'Appending Favorites' )
  iIiII = open ( I1IIiiIiii ) . read ( )
  I11IIII1111II = json . loads ( iIiII )
  I11IIII1111II . append ( ( name , url , iconimage , fanart , mode ) )
  ooooo0Oo0 = open ( I1IIiiIiii , "w" )
  ooooo0Oo0 . write ( json . dumps ( I11IIII1111II ) )
  ooooo0Oo0 . close ( )
  if 6 - 6: iI11I1II1I1I / Oooo0O0oo00oO + oo0oO00
  if 89 - 89: O0oOO0
def o0OOOOOo00 ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  I1ii1iI = [ ]
  i1Ii11ii1I ( 'Making Favorites File' )
  I1ii1iI . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iIiII = open ( I1IIiiIiii , "w" )
  iIiII . write ( json . dumps ( I1ii1iI ) )
  iIiII . close ( )
 else :
  oo0oOO = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  IIO000oooOO0Oo0 = len ( oo0oOO )
  for I1iIiIii in oo0oOO :
   Oo0OO = I1iIiIii [ 0 ]
   ooO0oOOooOo0 = I1iIiIii [ 1 ]
   iIIiiI1II1i11 = I1iIiIii [ 2 ]
   try :
    OO0I1iiI1iiI1i1 = I1iIiIii [ 3 ]
    if OO0I1iiI1iiI1i1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     OO0I1iiI1iiI1i1 = iIIiiI1II1i11
    else :
     OO0I1iiI1iiI1i1 = iiI11ii1I1
   try : OOOO00OOO00 = I1iIiIii [ 5 ]
   except : OOOO00OOO00 = None
   try : ii1OO0 = I1iIiIii [ 6 ]
   except : ii1OO0 = None
   if 96 - 96: o0o00Oo0O . iiII11i1I1IIi - oOo0O0Ooo * I1ii11iIi11i
   if I1iIiIii [ 4 ] == 0 :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , '' , iIIiiI1II1i11 , iiI11ii1I1 , '' , 'fav' )
   else :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , I1iIiIii [ 4 ] , iIIiiI1II1i11 , iiI11ii1I1 , '' , 'fav' )
    if 68 - 68: O0oOO0 - I1ii11iIi11i / OOooOOo - OooOO000 . iiII11i1I1IIi
def iiI11Ii1i ( name ) :
 I11IIII1111II = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for O0O0O0o in range ( len ( I11IIII1111II ) ) :
  if I11IIII1111II [ O0O0O0o ] [ 0 ] == name :
   del I11IIII1111II [ O0O0O0o ]
   ooooo0Oo0 = open ( I1IIiiIiii , "w" )
   ooooo0Oo0 . write ( json . dumps ( I11IIII1111II ) )
   ooooo0Oo0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 83 - 83: iiII11i1I1IIi % oo0oO00
 if 6 - 6: OOooOOo / OOoOoo + iiII11i1I1IIi - I11i * Oooo0O0oo00oO + OOoOoo
def o00oiii11II1I ( ) :
 oo0o0Oo0 = os . path . join ( O0O , 'addons.ini' )
 O0Ooo0ooo00o = open ( oo0o0Oo0 , "w+" )
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 O0Ooo0ooo00o . write ( r'[' + IiII + ']' + '\n' )
 for Oo0OO , O0o0OO0000ooo , IiIIi1I1I11Ii , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  O0o0O00o0o = ( Oo0OO + '=plugin://' + IiII + '/?url=' + ooO0oOOooOo0 + '&mode=10012&name=' + ( Oo0OO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( O0o0OO0000ooo ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( O0o0OO0000ooo ) . replace ( ' ' , '' ) + '+&amp;description=' )
  O0Ooo0ooo00o . write ( O0o0O00o0o + '\n' )
  if 6 - 6: Ii1I - O0oOO0 * Ii + OOooOOo / OOoOoo % Oooo0O0oo00oO
  if 38 - 38: Oooo0O0oo00oO % iIi1i1ii1 % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
def iIiIIi11iI ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247.png' , oOOOo00O00oOo + '247.png' , '' )
def iiIIi ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def OOOoOO ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def ooo00o0o ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def OOOO00o000o ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o00oooO0Oo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 60 - 60: iiII11i1I1IIi - iI11I1II1I1I
  if 13 - 13: Ii1I . iIi1i1ii1
def IIII1ii1 ( ) :
 if 52 - 52: oO0o - Oooo0O0oo00oO - OOoOoo - I11i + ooOoO0O00
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 10 - 10: ii / iiII11i1I1IIi / O0oOO0 * I1ii11iIi11i / iI11I1II1I1I
def oO0OoiIi111iII1 ( ) :
 if 61 - 61: OOoOoo . Ii + O0oOO0
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , ii1i in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + '  -  ' + ( ii1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 10023 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 8 - 8: iI11I1II1I1I
  if 55 - 55: O0oOO0
  if 37 - 37: iIi1i1ii1 / Ii / I1ii11iIi11i
def o0o ( ) :
 if 73 - 73: OOooOOo % I11i
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
 if 71 - 71: O0oOO0 - ii * I1ii11iIi11i * oo0oO00 + I11i * Ii1I
def ooO ( url ) :
 o0oOOoOOO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( o0oOOoOOO )
 o00oooO0Oo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 16 - 16: I1ii11iIi11i
  if 74 - 74: oo0oO00
  if 98 - 98: O0oOO0 / ii % IIi * IIiIiII11i - oO0o
  if 95 - 95: oOo0O0Ooo % OooOO000 * oOo0O0Ooo + o0o00Oo0O . OooOO000 % ii
def II11II1I ( ) :
 if 52 - 52: Oooo0O0oo00oO * O0oOO0 + oo0oO00 * oo0oO00 % ooOoO0O00 % oo0oO00
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( ooO0oOOooOo0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if oOoOOoOOooOO in Oo0OO . lower ( ) :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 96 - 96: I11i * O0oOO0 - Oooo0O0oo00oO * I11i * ooOoO0O00
   if 8 - 8: OOoOoo - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * IIi - iI11I1II1I1I
   if 30 - 30: oo0oO00 / Ii1I
def iI1iIIIIIiIi1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for OooiiIi1i , i1i11I1I1iii1 , iIi , Oo0OO in o00oooO0Oo :
  oOo = ( iIi ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ooOo0o = ( i1i11I1I1iii1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  III = 'Season ' + ooOo0o + 'Episode ' + oOo + Oo0OO
  IiiI ( III , OooiiIi1i )
  if 75 - 75: ii . Oooo0O0oo00oO + oO0o / IIi - oOo0O0Ooo % IIi
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 89 - 89: iiII11i1I1IIi * iI11I1II1I1I + Ii . ii
  if 51 - 51: Oooo0O0oo00oO / OOoOoo + oO0o % OOooOOo / IIi
def IiiI ( name , url ) :
 OooiiIi1i = url
 ii111i1i = name
 iii1i1iiiiIi = cloudflare . source ( OooiiIi1i )
 o0O0OOO0Ooo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for iIIiii , OOo0OOooo0 in o0O0OOO0Ooo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + ii111i1i + OOo0OOooo0 + '[/COLOR]' , iIIiii , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 93 - 93: o0o00Oo0O - oO0o . oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: OOooOOo + I11i
 if 65 - 65: IIiIiII11i / I1ii11iIi11i
def II1III1I1I1Ii ( ) :
 if 42 - 42: Ii . o0o00Oo0O
 if 75 - 75: OooOO000 + iI11I1II1I1I
 if 19 - 19: oOo0O0Ooo + Ii . iIi1i1ii1 - oo0oO00 / IIi + I11i
 if 38 - 38: I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I % Ii1I
 if 92 - 92: oo0oO00 / o0o00Oo0O * oOo0O0Ooo - oo0oO00
 if 99 - 99: Ii % ii
 if 56 - 56: iIi1i1ii1 * OooOO000
 if 98 - 98: oo0oO00 + o0o00Oo0O * OooOO000 + Ii - Oooo0O0oo00oO - iI11I1II1I1I
 if 5 - 5: Oooo0O0oo00oO % I1ii11iIi11i % iIi1i1ii1 % OOoOoo
 if 17 - 17: IIi + IIiIiII11i + ii / Oooo0O0oo00oO / iIi1i1ii1
 if 80 - 80: I11i % ooOoO0O00 / oo0oO00
 if 56 - 56: ooOoO0O00 . Ii
 if 15 - 15: IIiIiII11i * O0oOO0 % iiII11i1I1IIi / Ii - O0oOO0 + I1ii11iIi11i
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 9 - 9: oo0oO00 - O0oOO0 + o0o00Oo0O / iiII11i1I1IIi % ooOoO0O00
 if 97 - 97: I11i * OOoOoo
def O0OOO0ooO00o ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Ii11i1I11i ) )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 24 - 24: OooOO000 + ii . iIi1i1ii1 / OOooOOo / oo0oO00
def ooOoo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 91 - 91: I11i . iiII11i1I1IIi % I1ii11iIi11i - iiII11i1I1IIi . O0oOO0 % Ii
def iIiO0O ( url ) :
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
  if 71 - 71: Ii1I + oO0o
  if 17 - 17: o0o00Oo0O . Oooo0O0oo00oO
def oooO0o0oOoO ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11iii = 'http://www.watchseries.ac/search/' + oOoOOoOOooOO . replace ( ' ' , '%20' )
 I1 = O0 ( I11iii )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'watch online' in Oo0OO :
   pass
  else :
   print ooO0oOOooOo0
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , O0o0OO0000ooo , '' , '' )
   if 11 - 11: O0oOO0 + OooOO000 . iIi1i1ii1 * ii - Ii1I - Oooo0O0oo00oO
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 16 - 16: iiII11i1I1IIi / iI11I1II1I1I + Oooo0O0oo00oO * iiII11i1I1IIi * oo0oO00
def iiIiI11IiI1ii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , iIi , o0o0oOoOO0O in o00oooO0Oo :
  OO00 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iIi ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , O0o0OO0000ooo , '' , o0o0oOoOO0O )
  if 100 - 100: oOo0O0Ooo + oO0o
def oO0OoOOOO0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  OO00 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 59 - 59: Oooo0O0oo00oO - oo0oO00 % ooOoO0O00
def IIOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , O0o0OO0000ooo , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 85 - 85: IIiIiII11i % iIi1i1ii1 . OooOO000 * iiII11i1I1IIi / iI11I1II1I1I . OOoOoo
def o0Ii11iIiiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 Ii11i1I11i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for i1i11I1I1iii1 , OO00OoooO in Ii11i1I11i :
  o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OO00OoooO ) )
  for url , Oo0OO in o00oooO0Oo :
   OO00 = ( i1i11I1I1iii1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: ii
class OoOO00oo0o ( ) :
 if 76 - 76: iiII11i1I1IIi . iIi1i1ii1 % iiII11i1I1IIi - OooOO000
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 51 - 51: ii + I11i * iI11I1II1I1I * O0oOO0 / ooOoO0O00
  OO00 = name
  self . Get_Sources ( ooO0oOOooOo0 , OO00 )
  if 19 - 19: iiII11i1I1IIi - OOooOOo % O0oOO0 / ii % iiII11i1I1IIi
  if 65 - 65: o0o00Oo0O . O0oOO0
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O0 ( URL )
  o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
   self . Get_site_link ( URL , season_name )
   if 85 - 85: IIiIiII11i
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
   if 55 - 55: Ii1I
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oOoo0OO0 = 'DACLIPS'
   if oOoo0OO0 in OoOO00oo0o . source_list :
    pass
   else :
    self . daclips ( url , season_name , oOoo0OO0 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    oOoo0OO0 = 'FILEHOOT'
    if oOoo0OO0 in OoOO00oo0o . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , oOoo0OO0 )
   else :
    if 'thevideo.me' in url :
     oOoo0OO0 = 'THEVIDEO'
     if oOoo0OO0 in OoOO00oo0o . source_list :
      pass
     else :
      self . thevideo ( url , season_name , oOoo0OO0 )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      oOoo0OO0 = 'ALLMYVIDEOS'
      if oOoo0OO0 in OoOO00oo0o . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , oOoo0OO0 )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       oOoo0OO0 = 'VIDSPOT'
       if oOoo0OO0 in OoOO00oo0o . source_list :
        pass
       else :
        self . vidspot ( url , season_name , oOoo0OO0 )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        oOoo0OO0 = 'VODLOCKER'
        if oOoo0OO0 in OoOO00oo0o . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , oOoo0OO0 )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 5 - 5: Ii * I1ii11iIi11i
         if 29 - 29: IIi / OOoOoo % oo0oO00
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 10 - 10: iI11I1II1I1I % ii % Ii1I
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for oooOooooO0oOO , Oo0OO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * oo0oO00
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 89 - 89: IIi - OOoOoo . oo0oO00 - OooOO000 - oOo0O0Ooo
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 79 - 79: iIi1i1ii1 + iIi1i1ii1 + IIi
 def daclips ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 39 - 39: o0o00Oo0O - ii
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oooOooooO0oOO in o00oooO0Oo :
   self . Printer ( oooOooooO0oOO , season_name , source_name )
   if 63 - 63: iI11I1II1I1I % I11i * OOoOoo
 def Printer ( self , Link , season_name , source_name ) :
  if 79 - 79: o0o00Oo0O
  if Link in OoOO00oo0o . List :
   pass
  elif source_name in OoOO00oo0o . source_list :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   OoOO00oo0o . List . append ( Link )
   OoOO00oo0o . source_list . append ( source_name )
   if 32 - 32: IIiIiII11i . o0o00Oo0O + IIi / OOooOOo / iIi1i1ii1 / Oooo0O0oo00oO
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 15 - 15: Ii1I
   if 4 - 4: iIi1i1ii1 + iI11I1II1I1I * iiII11i1I1IIi + I1ii11iIi11i * I11i % IIiIiII11i
   if 88 - 88: O0oOO0 - ooOoO0O00 % Ii % IIiIiII11i * ii
   if 40 - 40: I1ii11iIi11i
   if 47 - 47: OOooOOo
def o0OO0o0o00o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 65 - 65: o0o00Oo0O + OooOO000 % IIi * oOo0O0Ooo / OOoOoo / OOooOOo
def oooOO ( url ) :
 I1IiiiiI ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OOoO )
 for iI1IIIi11 , url , oooOo00O0 , I1I , oOO0o0 , OoOOoO0oOo , Ii1Ii1 , oOOo0O00o , iIiII , o000ooOo0o0OO , iiI1ii1IIiI in o00oooO0Oo :
  oooOo00O0 = oooOo00O0
  if 'Arsenal' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'arsenal-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                                  ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Bournemouth' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'afc-bournemouth.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                       ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Burnley' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'KEGnQWW.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                                   ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Chelsea' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'chelsea.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                                  ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Crystal' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'CrystalPalace.0.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                       ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Everton' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'Everton.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                                   ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Hull' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'hull-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                                 ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Leicester' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                       ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Liverpool' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'liverpool-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                               ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Manchester City' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'city-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '               ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Manchester United' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + '91.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '          ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Middlesbrough' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                 ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Southampton' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'southampton-fc-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                   ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Stoke City' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'stoke-city.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                          ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Sunderland' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'sunderland-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                        ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Swansea' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'swansea-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                    ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Tottenham' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '        ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Watford' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '                              ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'Bromwich' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '   ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  elif 'West Ham' in oooOo00O0 :
   o00OooO0oo = oOOOo00O00oOo + 'west-ham.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iI1IIIi11 + ' - ' + oooOo00O0 + '             ' + I1I + '        ' + oOO0o0 + '        ' + OoOOoO0oOo + '        ' + Ii1Ii1 + '        ' + oOOo0O00o + '        ' + iIiII + '        ' + o000ooOo0o0OO + '[/COLOR]'
  I1IiiiiI ( str ( Oo0OO ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , o00OooO0oo , o00OooO0oo , oooOo00O0 )
  if 35 - 35: Ii1I * iiII11i1I1IIi . iIi1i1ii1 . iIi1i1ii1 - O0oOO0 % OOooOOo
def iI1iiIiI ( description ) :
 oooOo00O0 = description
 ooO0oOOooOo0 = ( 'http://www.fullmatchesandshows.com/?s=' + oooOo00O0 ) . replace ( ' ' , '%20' )
 o0OoO0000oOO ( ooO0oOOooOo0 )
 if 42 - 42: OooOO000 % oO0o . Ii1I
def iiIIiIi ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o00oooO0Oo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0oOOooOo0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0o0OO0000ooo , OO0o , '' )
  if 97 - 97: iiII11i1I1IIi + oo0oO00 % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * iiII11i1I1IIi
def o0Oo ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for Ii11i1I11i in Ii11i1I11i :
  i1II11i1iI1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( Ii11i1I11i ) )
  for OO0IIi1II11 in i1II11i1iI1 :
   OO0IIi1II11 = OO0IIi1II11
  o0ooOOOo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Ii11i1I11i ) )
  for OOoOOo0oO , O0o0OO0000ooo , time , I1Ii1IIIiII in o0ooOOOo :
   iii1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1Ii1IIIiII )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OO0IIi1II11 + ' - ' + OOoOOo0oO + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + O0o0OO0000ooo , OO0o , ( str ( iii1 ) ) )
   if 11 - 11: o0o00Oo0O * OOooOOo
 Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % OooOO000 / iiII11i1I1IIi
def iIIi ( ) :
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
 if 98 - 98: O0oOO0 + ii - OooOO000 % Ii / I11i . ii
def ooo0 ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  o0OOo0O = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   o0OOo0O = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0OOo0O + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  o0OOo0O = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0OOo0O + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
def o0OoO0000oOO ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 52 - 52: ii / iIi1i1ii1 % IIiIiII11i
 if 40 - 40: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + oO0o
 if 75 - 75: O0oOO0 - Ii1I + O0oOO0 + ii . Ii
 if 52 - 52: iiII11i1I1IIi / OOoOoo - Ii + ii
 if 33 - 33: o0o00Oo0O + I1ii11iIi11i - iI11I1II1I1I % Ii / oOo0O0Ooo
 if 47 - 47: Ii1I * O0oOO0 + iI11I1II1I1I - O0oOO0 / iIi1i1ii1
 if 86 - 86: iIi1i1ii1
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  o0OOo0O = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + o0OOo0O + '[/COLOR]' , url , 10013 , O0o0OO0000ooo )
   if 43 - 43: oOo0O0Ooo / iiII11i1I1IIi / OOoOoo + iI11I1II1I1I + ii
def iiI111i1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for iIIiii in o00oooO0Oo :
  IiIii11i1IIiI = ( iIIiii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I1I1iI ( 'http:' + IiIii11i1IIiI )
  if 40 - 40: iiII11i1I1IIi + iI11I1II1I1I * O0oOO0 + Ii . Ii
  if 11 - 11: oO0o % ii
  if 20 - 20: OooOO000 + OooOO000 * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
  if 62 - 62: ii / OOooOOo . iIi1i1ii1 . iIi1i1ii1 % OOoOoo
def iIIO0ooo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 8046 , O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def II1ii1iii1ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1I1iI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 21 - 21: iIi1i1ii1 - oOo0O0Ooo % ii + I11i
def o00O0o ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 28 - 28: oOo0O0Ooo
def I1iI ( ) :
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 25 - 25: Ii / OOooOOo - OooOO000 / oO0o . I11i . I11i
  if 6 - 6: O0oOO0 . oo0oO00
def iIIII1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   OOoOOO0 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def Oooo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  url = ( url ) . replace ( '\/' , '/' )
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , '' )
  if 7 - 7: ooOoO0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo00oo ( name , url ) :
 oO0oO = 0
 name = name
 url = url
 ii1I = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  I1I1iI ( url )
  if 71 - 71: OooOO000 / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / Oooo0O0oo00oO . Ii1I * OOoOoo
  if 59 - 59: iI11I1II1I1I / Ii1I % OOoOoo
  if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % oo0oO00
  if 99 - 99: I1ii11iIi11i + Ii
  if 36 - 36: IIi * OooOO000 * iI11I1II1I1I - oo0oO00 % Ii
  if 98 - 98: iI11I1II1I1I - ooOoO0O00 + OOoOoo % oo0oO00 + OOoOoo / O0oOO0
  if 97 - 97: iIi1i1ii1 % OOoOoo + IIiIiII11i - iIi1i1ii1 % oO0o + OOoOoo
def iIIII11i ( ) :
 OOoO = oo0O0o00o0O ( 'http://documentarylovers.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  if 'genre' in ooO0oOOooOo0 :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , ooO0oOOooOo0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOo0OOoo0o ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 5 - 5: o0o00Oo0O - oOo0O0Ooo
def IiiI1iii1iIiiI ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in o0O0OOO0Ooo :
  Oooo ( url )
  if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / Oooo0O0oo00oO
def IiiIiiIIII ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I11I = 'http://documentarylovers.com/?s=' + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 iIIII1i = I11I . lower ( )
 oOo0OOoo0o ( iIIII1i )
 if 88 - 88: oO0o . OooOO000 / oo0oO00
def iIiI1I1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def oOoO ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def oOOo00Ooo0O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'rtd' in url :
   iIii1Oo ( url )
   if 15 - 15: ooOoO0O00 + iIi1i1ii1 % oOo0O0Ooo / Ii * OOooOOo
def iIii1Oo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OOoO )
 for O0o0O00Oo0o0 , file in o00oooO0Oo :
  url = ( 'https://rtd.rt.com' + O0o0O00Oo0o0 + file )
  I1I1iI ( url )
  if 69 - 69: Ii
  if 61 - 61: o0o00Oo0O
def iIiiI111I11 ( ) :
 I1 = oo0O0o00o0O ( 'http://www.stream2watch.co/live-tv' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , OOo0Oo0 in o00oooO0Oo :
  I1i11111i1i11 ( ( Oo0OO + '[COLOR' + iiI1IiI + ']' + OOo0Oo0 + '[/COLOR]' ) , ooO0oOOooOo0 , 8086 , O0o0OO0000ooo )
  if 55 - 55: Oooo0O0oo00oO / OOooOOo * Oooo0O0oo00oO
def IIIiiiI1Ii1 ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8087 , O0o0OO0000ooo )
  if 97 - 97: IIiIiII11i % I1ii11iIi11i * iIi1i1ii1
def oOoOO0O00o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OOOO ( url , Oo0OO )
  if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - iIi1i1ii1 . ii
def o0OOOO ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  print url
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 10 - 10: OooOO000
def I11i1i11IiIi1 ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooO0oOOooOo0 , 3002 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def I11i1I1Ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def iii11 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 I1i11IIIi = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , Oo0OO in I1i11IIIi :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']Season- ' + Oo0OO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , O0o0OO0000ooo , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0o0OO0000ooo )
def III1IIIIIiiI ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  i1iIii ( url )
def i1iIii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1I1iI ( url )
  if 95 - 95: oo0oO00 / iIi1i1ii1 . o0o00Oo0O * iIi1i1ii1 - I11i * I1ii11iIi11i
def IiI11ii1I ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def II1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "v.src = '([^']*)';" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  o00o ( url )
  if 27 - 27: oOo0O0Ooo
def I1I1I1IIi1III ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def iiI11I1ii11 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'mp4' in url :
   I1I1iI ( url )
 for url in o0O0OOO0Ooo :
  yt . PlayVideo ( url )
  if 71 - 71: OOoOoo . Ii1I * o0o00Oo0O - OooOO000 - IIiIiII11i
def iIIi11ii ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooO0oOOooOo0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def O000Oo00 ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '(Free Access)' in Oo0OO :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def iI1oOoo ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , O0o0OO0000ooo , iiI11ii1I1 , '' )
  if 59 - 59: iIi1i1ii1 % IIi
def O0ooo ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  IiIIiII1I ( 'http://watchxxxfree.com/categories' )
 if O0oO0 == 1 :
  o00oOOo0Oo ( 'http://www.perfectgirls.net' )
 if O0oO0 == 2 :
  Oooo0o0oO ( 'http://www.xvideos.com/best' )
 if O0oO0 == 3 :
  o0OOoOooO0ooO ( 'http://www.xvideos.com/best' )
 if O0oO0 == 4 :
  Oooo0o0oO ( 'http://www.xvideos.com/best' )
 if O0oO0 == 5 :
  Oooo0o0oO ( 'http://www.xvideos.com/verified/videos' )
 if O0oO0 == 6 :
  IiiiIi ( 'http://www.xvideos.com/tags' )
 if O0oO0 == 7 :
  IiI111 ( 'http://www.xvideos.com/porn' )
 if O0oO0 == 8 :
  OO0OO00ooO0 ( )
  if 68 - 68: OOooOOo * Ii1I - ii - oo0oO00 + iI11I1II1I1I * Ii
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - O0oOO0 + Oooo0O0oo00oO + iiII11i1I1IIi % O0oOO0
  if 13 - 13: IIiIiII11i / OOooOOo / OOooOOo + OOoOoo
  if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % iIi1i1ii1
  if 13 - 13: O0oOO0 . iI11I1II1I1I . Oooo0O0oo00oO . iIi1i1ii1
  if 58 - 58: oo0oO00
  if 7 - 7: IIiIiII11i / iIi1i1ii1 % oo0oO00 + oOo0O0Ooo - o0o00Oo0O
  if 45 - 45: oOo0O0Ooo / iiII11i1I1IIi + O0oOO0 + iIi1i1ii1
  if 15 - 15: oOo0O0Ooo % oO0o
def oOoo00oO0O0OO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if 'ch' in url :
   O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def ii1I1ii1iII ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 o0OoOOOo0o = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for Oo0OO , url in o0OoOOOo0o :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iII1ii11III ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   OOOO0oO0O ( url )
def ooooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I1I1iI ( url )
def IiIIiII1I ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , II1Ii1iI1i1 in o00oooO0Oo :
  if 'category' in url :
   O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   ' + II1Ii1iI1i1 + '[/COLOR]' , url , 90006 , O0o0OO0000ooo , oOOOo00O00oOo + 'Jizbox.png' , '' )
def O000oooO0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 o0OoOOOo0o = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , O0o0OO0000ooo , '' , '' )
 for url in o0OoOOOo0o :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oOO00 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   OOOO0oO0O ( url )
def OOOO0oO0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I1I1iI ( url )
def o00oOOo0Oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , II1Ii1iI1i1 in o00oooO0Oo :
  if 'category' in url :
   O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]' + II1Ii1iI1i1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oO0o00 ( url ) :
 I1 = O0 ( url )
 OooiiIi1i = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0OoOOOo0o = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , O0o0OO0000ooo , '' , '' )
 for url in o0OoOOOo0o :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , OooiiIi1i + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def Oo0OOOO0oOoo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in o00oooO0Oo :
  O0OIIII1i ( 'http://www.perfectgirls.net' + url )
def O0OIIII1i ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in o00oooO0Oo :
  I1I1iI ( 'http://' + url )
def IiI111 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , II1Ii1iI1i1 in o00oooO0Oo :
  O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + II1Ii1iI1i1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiiiIi ( url ) :
 I1 = O0 ( url )
 o0OoOOOo0o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in o0OoOOOo0o :
  O0OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , II1Ii1iI1i1 in o00oooO0Oo :
  O0OOo ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + ( II1Ii1iI1i1 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 30 - 30: iIi1i1ii1 - iiII11i1I1IIi - oO0o
def ii11 ( url ) :
 I1 = O0 ( url )
 o0OoOOOo0o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in o0OoOOOo0o :
  O0OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , Oo00o0O0O in o00oooO0Oo :
  O0OOo ( Oo0OO + '--' + ( Oo00o0O0O ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( O0o0OO0000ooo ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 99 - 99: Ii1I - O0oOO0
  if 10 - 10: IIiIiII11i . oO0o
def Oooo0o0oO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , url , Oo0OO , OoOOo , o000Ooo00o00O in o00oooO0Oo :
  O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + o000Ooo00o00O + ' - [COLORred]' + OoOOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , O0o0OO0000ooo , O0o0OO0000ooo , o000Ooo00o00O + ' - ' + OoOOo )
 ooo0O0O0oo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in ooo0O0O0oo0 :
  O0OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 85 - 85: IIiIiII11i + OOoOoo * oo0oO00
def o0OOoOooO0ooO ( url ) :
 I1 = O0 ( url )
 Ii11i1I11i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 o0OoOOOo0o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in o0OoOOOo0o :
  O0OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Ii11i1I11i ) )
 for url , Oo0OO in o00oooO0Oo :
  if '/c/' in url :
   O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 12 - 12: IIi . oOo0O0Ooo % I11i
   if 28 - 28: IIi - oOo0O0Ooo % oO0o * OooOO000
def OO0OO00ooO0 ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0oOooO00oo = ( oOoOOoOOooOO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 iIIII1i = oO0oOooO00oo . lower ( )
 ooo0oo00O00Oo = 'http://www.xvideos.com/?k=' + iIIII1i
 print ooo0oo00O00Oo + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O0 ( ooo0oo00O00Oo )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO , OoOOo , o000Ooo00o00O in o00oooO0Oo :
  O0OOo ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + o000Ooo00o00O + ' - [COLORred]' + OoOOo + '[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10108 , O0o0OO0000ooo , O0o0OO0000ooo , o000Ooo00o00O + ' - ' + OoOOo )
 ooo0O0O0oo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for ooO0oOOooOo0 in ooo0O0O0oo0 :
  O0OOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 82 - 82: ii / OOoOoo * oo0oO00 * o0o00Oo0O . Ii1I
def iiIIIII ( url ) :
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
   if 19 - 19: IIiIiII11i / OOooOOo
def oOoo00 ( url ) :
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 import urlresolver
 try : i1IiII1III . play ( url )
 except : pass
 if 29 - 29: Oooo0O0oo00oO / OOooOOo . iI11I1II1I1I / oo0oO00 % OOooOOo % iiII11i1I1IIi
 if 49 - 49: IIiIiII11i / iIi1i1ii1 - IIi
def IiIII ( ) :
 if 92 - 92: oOo0O0Ooo % iiII11i1I1IIi
 if 31 - 31: ii - O0oOO0 / OooOO000
 if 62 - 62: Ii - oo0oO00
 if 81 - 81: oo0oO00
 if 92 - 92: Oooo0O0oo00oO - I1ii11iIi11i - ii / iIi1i1ii1 - ooOoO0O00
 if 81 - 81: ooOoO0O00 / OooOO000 % Ii . iI11I1II1I1I * OOooOOo + ii
 if 31 - 31: ooOoO0O00 % IIiIiII11i
 if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . IIi % oO0o
 if 2 - 2: ii - IIi % O0oOO0 / oOo0O0Ooo / I11i
 if 3 - 3: IIiIiII11i / Oooo0O0oo00oO
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def i1IIiiIIIIi ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def IiIIIi ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 Oo0iII = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo in Oo0iII :
  O0o0OO0000ooo = O0o0OO0000ooo
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 73 - 73: IIi / oOo0O0Ooo / ii + oOo0O0Ooo
def o0OoOo0O00 ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 9 - 9: Oooo0O0oo00oO
  if 38 - 38: oo0oO00 . oO0o . Ii * ii + iiII11i1I1IIi
  if 49 - 49: I1ii11iIi11i - oO0o / OooOO000 / I11i % O0oOO0
  if 38 - 38: I11i . O0oOO0 / I11i % IIiIiII11i
I11iI1iIii1ii = '{PQ},' ; OoOoOo0o00OoOO = '{SC},' ; Iii1iii1I = '{XG},' ; oOo000Oo00o = '{JP},' ; o0ooOOoOoOO = '{HW},' ; iII11 = '{RT},'
def Ooo00Oo ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 O00OO00OOOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 47 - 47: ooOoO0O00 % OOoOoo - I1ii11iIi11i * oo0oO00 / Ii
 III11I = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Iii1Iii = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 iiI11111II = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1ii1i11iI1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiOOo0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOoOOoOOooOO
 o0O0O0O00o = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OoOooOo00o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 iI1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II11 = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 79 - 79: o0o00Oo0O + oo0oO00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 25 - 25: OooOO000 - IIi / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
 if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + O0oOO0 + O0oOO0 + iiII11i1I1IIi
 Iiii = Oo0OoO00oOO0o ( III11I )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( Iii1Iii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IIi1I1 = Oo0OoO00oOO0o ( iiI11111II )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 oO00o0oOoo = Oo0OoO00oOO0o ( IiOOo0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOOI1 = Oo0OoO00oOO0o ( o0O0O0O00o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OOI1i = Oo0OoO00oOO0o ( OoOooOo00o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 i1II1iII1 = Oo0OoO00oOO0o ( iI1IIi )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 I11II11IiI11 = Oo0OoO00oOO0o ( II11 )
 if 97 - 97: OOoOoo / iI11I1II1I1I % OOoOoo / oOo0O0Ooo * iiII11i1I1IIi % OOooOOo
 if 17 - 17: iI11I1II1I1I
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for ooi11I , Oo0OO in o00oooO0Oo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooO0oOOooOo0 + ooi11I ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 48 - 48: Oooo0O0oo00oO + OooOO000 % Oooo0O0oo00oO
    if 84 - 84: o0o00Oo0O % IIi . IIi . iiII11i1I1IIi * oo0oO00
    if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
    if 61 - 61: oOo0O0Ooo + O0oOO0 % OooOO000 % iI11I1II1I1I - ii
    if 22 - 22: Oooo0O0oo00oO + IIiIiII11i + I1ii11iIi11i
    if 83 - 83: OOoOoo
    if 43 - 43: Oooo0O0oo00oO
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for ooi11I , Oo0OO in o0OOo00OoO :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( III11I + ooi11I ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  o0IiiIIII1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in o0IiiIIII1I1i :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 26 - 26: iiII11i1I1IIi - I1ii11iIi11i + oOo0O0Ooo + I11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if IIi1I1 != 'Failed' :
  III1iI1Ii11Ii = [ ]
  iI11iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1I1 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in iI11iIi :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    if Oo0OO in III1iI1Ii11Ii :
     pass
    else :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
     III1iI1Ii11Ii . append ( Oo0OO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if oO00o0oOoo != 'Failed' :
  OOoo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oO00o0oOoo )
  for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in OOoo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooO0oOOooOo0 , 7067 , O0o0OO0000ooo )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . oo0oO00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 64 - 64: OOoOoo / ooOoO0O00 % iiII11i1I1IIi
    if 84 - 84: OOooOOo - I1ii11iIi11i . OOoOoo . iIi1i1ii1 - I1ii11iIi11i
    if 99 - 99: OooOO000
    if 75 - 75: OOoOoo . Oooo0O0oo00oO / iIi1i1ii1
    if 84 - 84: ii . oOo0O0Ooo / I11i
    if 86 - 86: I1ii11iIi11i % OOooOOo
    if 77 - 77: IIi % Oooo0O0oo00oO / O0oOO0
    if 91 - 91: oO0o / oO0o . IIiIiII11i . OOoOoo - oOo0O0Ooo
    if 23 - 23: oOo0O0Ooo
 if OOI1i != 'Failed' :
  i1IIiI1iII = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOI1i )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in i1IIiI1iII :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 45 - 45: ooOoO0O00 % Oooo0O0oo00oO % IIiIiII11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if i1II1iII1 != 'Failed' :
  IIIIi1Iii1iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1II1iII1 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in IIIIi1Iii1iIi :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 36 - 36: Ii * Ii1I * OOooOOo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 24 - 24: O0oOO0 . o0o00Oo0O * OOoOoo / ii - IIi . oo0oO00
 if I11II11IiI11 != 'Failed' :
  iIIiIi111iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11II11IiI11 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , Oo0OO in iIIiIi111iI :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 40 - 40: OOooOOo + oO0o % ii * I11i / OOooOOo + ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 iIII1iIi = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 91 - 91: OOoOoo - O0oOO0 + O0oOO0
 for o00oIIi1i1 in iIII1iIi :
  o0O0Ooo = oOOoo0Oo + o00oIIi1i1 + IIIII
  II11iiIIiI11I = Oo0OoO00oOO0o ( o0O0Ooo )
  if II11iiIIiI11I != 'Failed' :
   OoO0o00oo0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iiIIiI11I )
   for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in OoO0o00oo0oO :
    if oOoOOoOOooOO in Oo0OO . lower ( ) :
     o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , 222 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 25 - 25: IIi * I11i * O0oOO0 . oOo0O0Ooo
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 93 - 93: OOooOOo
 iIII1iIi = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 97 - 97: Ii
 if 68 - 68: iIi1i1ii1 * oO0o . oo0oO00 / IIi . I11i - Ii
 for o00oIIi1i1 in iIII1iIi :
  o0O0Ooo = O00OO00OOOoO + o00oIIi1i1
  II11I = Oo0OoO00oOO0o ( o0O0Ooo )
  if II11I != 'Failed' :
   OOooo00oo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( II11I )
   for ooi11I , Oo0OO in OOooo00oo :
    if oOoOOoOOooOO in Oo0OO . lower ( ) :
     OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O00OO00OOOoO + o00oIIi1i1 + ooi11I ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 42 - 42: IIi * o0o00Oo0O / O0oOO0
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 8 - 8: ooOoO0O00 + IIiIiII11i / IIi + Ii1I % IIi - iI11I1II1I1I
     if 29 - 29: I1ii11iIi11i + IIiIiII11i
def o00o0 ( ) :
 if 95 - 95: O0oOO0
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 if 48 - 48: oo0oO00 / iI11I1II1I1I % IIiIiII11i
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( oOoOOoOOooOO ) . replace ( ' ' , '%20' )
 OooiiIi1i = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 III11I = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Iii1Iii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iiI11111II = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIIII1i ) . replace ( ' ' , '+' )
 I1ii1i11iI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IiOOo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 o0O0O0O00o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 39 - 39: ooOoO0O00 . Ii1I / oo0oO00 / oo0oO00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 100 - 100: ii - ii + iIi1i1ii1
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( OooiiIi1i )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = Oo0OoO00oOO0o ( III11I )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( Iii1Iii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIi1I1 = cloudflare . source ( iiI11111II )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 II11I = Oo0OoO00oOO0o ( I1ii1i11iI1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oO00o0oOoo = Oo0OoO00oOO0o ( IiOOo0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOOI1 = Oo0OoO00oOO0o ( o0O0O0O00o )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 32 - 32: OOooOOo * I11i / ii
 if oOOI1 != 'Failed' :
  oOooo00OOO000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOI1 )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in oOooo00OOO000 :
   if iIIII1i in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
    if 85 - 85: ooOoO0O00 - Oooo0O0oo00oO / o0o00Oo0O + o0o00Oo0O / Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 54 - 54: OOoOoo * Ii1I . IIiIiII11i / Oooo0O0oo00oO % Oooo0O0oo00oO
 if oO00o0oOoo != 'Failed' :
  OOoo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO00o0oOoo )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in OOoo :
   if iIIII1i in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % OooOO000
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: ooOoO0O00
    if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
    if 9 - 9: ooOoO0O00 - OOooOOo
    if 57 - 57: iI11I1II1I1I * IIi * iiII11i1I1IIi / O0oOO0
    if 46 - 46: IIi
    if 61 - 61: I11i / OOoOoo - IIiIiII11i
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 87 - 87: Ii1I / oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for O0o0OO0000ooo , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   if iIIII1i in Oo0OO . lower ( ) :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , O0o0OO0000ooo , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 45 - 45: OOooOOo * OOoOoo / ii + oO0o . OooOO000 / oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 64 - 64: IIi / ooOoO0O00 % oOo0O0Ooo - I11i
    if 11 - 11: Ii1I - ii
    if 16 - 16: iIi1i1ii1 % ii - OOoOoo * IIi - IIi
    if 27 - 27: iIi1i1ii1 + iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + oO0o
    if 77 - 77: I1ii11iIi11i * OOoOoo % IIi
    if 2 - 2: oo0oO00 / I1ii11iIi11i / IIi / Ii1I / ii
    if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / oo0oO00 + OOooOOo
    if 98 - 98: Oooo0O0oo00oO
    if 69 - 69: IIiIiII11i + I1ii11iIi11i - O0oOO0 . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
    if 75 - 75: oO0o % ii
    if 16 - 16: o0o00Oo0O / ooOoO0O00
    if 58 - 58: I11i / Ii / o0o00Oo0O % oo0oO00 % oOo0O0Ooo
    if 86 - 86: iIi1i1ii1 + OOooOOo / oOo0O0Ooo + oo0oO00 % oo0oO00 / Ii
    if 12 - 12: OOooOOo + I11i . OooOO000
    if 52 - 52: oO0o
    if 4 - 4: IIi % Ii1I + oo0oO00 - Ii1I
    if 98 - 98: IIi - o0o00Oo0O * O0oOO0 * IIi * IIi
    if 44 - 44: iIi1i1ii1 + oo0oO00
    if 66 - 66: O0oOO0
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for Oo0OO in o0OOo00OoO :
   if iIIII1i in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( III11I + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 34 - 34: iiII11i1I1IIi % Ii + Ii - iiII11i1I1IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  o0IiiIIII1I1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for Oo0OO in o0IiiIIII1I1i :
   if iIIII1i in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Iii1Iii + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 2 - 2: IIiIiII11i + ooOoO0O00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if IIi1I1 != 'Failed' :
  iI11iIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIi1I1 )
  for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in iI11iIi :
   if iIIII1i in Oo0OO . lower ( ) :
    I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source - Dizi[/COLOR]' , ooO0oOOooOo0 , 8062 , O0o0OO0000ooo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 68 - 68: Oooo0O0oo00oO + IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if II11I != 'Failed' :
  OOooo00oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11I )
  for ooO0oOOooOo0 , iIIiiI1II1i11 , o0o0oOoOO0O , ooo0O , Oo0OO in OOooo00oo :
   if iIIII1i in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- Source Scooby[/COLOR]' ) , ooO0oOOooOo0 , 1016 , iIIiiI1II1i11 , ooo0O , o0o0oOoOO0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 58 - 58: iIi1i1ii1 * IIi . ooOoO0O00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: O0oOO0
 O0oooooO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if II11I != 'Failed' :
  for o00oIIi1i1 in O0oooooO :
   o0O0Ooo = oOOoo0Oo + o00oIIi1i1 + IIIII
   i1II1iII1 = O0 ( o0O0Ooo )
   if i1II1iII1 != 'Failed' :
    IIIIi1Iii1iIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1II1iII1 )
    for Oo0OO , o0o0oOoOO0O , ooO0oOOooOo0 , O0o0OO0000ooo , iiI11ii1I1 , iiIi1iI1iIii in IIIIi1Iii1iIi :
     if iIIII1i in Oo0OO . lower ( ) :
      I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , iiIi1iI1iIii , O0o0OO0000ooo , iiI11ii1I1 , o0o0oOoOO0O )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 28 - 28: I1ii11iIi11i / iIi1i1ii1 . iiII11i1I1IIi + oO0o + oo0oO00 % I1ii11iIi11i
      Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
      if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
      if 92 - 92: IIi . OOooOOo . oo0oO00 - ii / OOoOoo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOo0 ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oOoOOoOOooOO ) . replace ( ' ' , '+' )
 if 41 - 41: OooOO000 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
 if I1 != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    OOoOOO0 ( ( Oo0OO + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + ooO0oOOooOo0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 25 - 25: ii . IIi % iiII11i1I1IIi . iIi1i1ii1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
ooo000 = '{ZH},' ; oooOoO0oo0o0 = '{IX},' ; IiIIIii1i1iI = '{LM},'
if 99 - 99: iI11I1II1I1I - O0oOO0 - OOooOOo / iI11I1II1I1I * I1ii11iIi11i - O0oOO0
def o0ooo0oooO ( url ) :
 ooOo = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooOo )
 for url , i1i11I1I1iii1 , ii1i , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( i1i11I1I1iii1 ) . replace ( 'Sezon' , ' Season ' ) + ( ii1i ) . replace ( 'Bölüm' , ' Episode ' ) + Oo0OO , url , 8063 , '' )
  if 98 - 98: Ii1I - IIi * oO0o . Ii1I - OooOO000
  if 4 - 4: Ii + ii / Ii . ii % Ii1I / OOooOOo
  if 35 - 35: Ii1I % ooOoO0O00 + I11i - iI11I1II1I1I
  if 28 - 28: oOo0O0Ooo * IIiIiII11i * OOooOOo % Oooo0O0oo00oO - Oooo0O0oo00oO
def IIOoO ( url ) :
 ooOo = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( ooOo )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , url , 222 , '' )
  if 12 - 12: iIi1i1ii1 / oO0o / o0o00Oo0O * iIi1i1ii1
  if 51 - 51: OOoOoo * iiII11i1I1IIi / ooOoO0O00
  if 2 - 2: O0oOO0 + iIi1i1ii1 . iiII11i1I1IIi - ooOoO0O00 + OooOO000
  if 54 - 54: ii . O0oOO0 - iiII11i1I1IIi
def oO0o00o000Oo0 ( ) :
 if 1 - 1: oOo0O0Ooo - OooOO000
 ooOo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooOo )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO , ii1i in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO + '  -  ' + ( ii1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 8063 , O0o0OO0000ooo )
  if 62 - 62: oO0o . iiII11i1I1IIi . iiII11i1I1IIi % ooOoO0O00 * O0oOO0 % I1ii11iIi11i
def I1I11 ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8002 , O0o0OO0000ooo )
def i1iiiiIIIi ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , time , url , Oo0OO , iii11i1 in o00oooO0Oo :
  I1IiiiiI ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , time ) , url , 1015 , O0o0OO0000ooo , iii11i1 )
  if 13 - 13: o0o00Oo0O + OooOO000 * IIiIiII11i + I1ii11iIi11i * iIi1i1ii1
def i1111ii1I ( ) :
 if 60 - 60: Oooo0O0oo00oO * OOoOoo * oO0o
 I1i11111i1i11 ( 'Coronation Street' , '' , 8001 , '' )
 I1i11111i1i11 ( 'Eastenders' , '' , 8002 , '' )
 I1i11111i1i11 ( 'Emmerdale' , '' , 8003 , '' )
 I1i11111i1i11 ( 'Hollyoaks' , '' , 8004 , '' )
 I1i11111i1i11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 64 - 64: oo0oO00 / IIiIiII11i / oO0o - OOoOoo * iI11I1II1I1I . iiII11i1I1IIi
 if 25 - 25: Oooo0O0oo00oO - IIi . oo0oO00
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - OOoOoo % iI11I1II1I1I - IIi
 if 37 - 37: oO0o * oo0oO00 + IIi + Ii1I * I11i
def O00oOo0o0 ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Holly' in Oo0OO :
   O0o0OO0000ooo = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 100 - 100: ooOoO0O00 % IIi
def oO000O ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'East' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 62 - 62: ooOoO0O00 * iI11I1II1I1I % O0oOO0 % OOooOOo / ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: I1ii11iIi11i % iiII11i1I1IIi
def OooO00O0OO0oo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Emmer' in Oo0OO :
   O0o0OO0000ooo = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 60 - 60: IIiIiII11i + I11i % OooOO000 + OOoOoo . iIi1i1ii1 % IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: OOoOoo
def i1iI11ii ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Coro' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 65 - 65: ooOoO0O00 . Ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: Ii1I + oO0o - Ii1I * iIi1i1ii1 - oo0oO00 * oo0oO00
def OO00o ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Celeb' in Oo0OO :
   O0o0OO0000ooo = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooO0oOOooOo0 :
    OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , O0o0OO0000ooo )
   else :
    pass
    if 36 - 36: iIi1i1ii1 . ooOoO0O00 * iI11I1II1I1I - IIi * OOooOOo - oOo0O0Ooo
def O0OO0OOoOO ( name , url ) :
 IIIiI1i = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIIiI1i :
  O00O000oOO0oO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOoO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OOoO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOoO = open_url ( url )
  OO0i1Ii1II11 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OOoO ) [ - 1 ]
  O00O000oOO0oO = OO0i1Ii1II11 . replace ( '\\/' , '/' )
 OooOo00o = xbmcgui . ListItem ( name , '' , '' )
 OooOo00o . setPath ( O00O000oOO0oO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OooOo00o )
 if 25 - 25: ii % O0oOO0 / iI11I1II1I1I + o0o00Oo0O
 if 95 - 95: I1ii11iIi11i * Oooo0O0oo00oO + oOo0O0Ooo . o0o00Oo0O
def IIiIi1II1IiI ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
  I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 99 - 99: I1ii11iIi11i
def IiIi1I11 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Movies' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooO0oOOooOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def IiI1O000oo0o ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0o0OO0000ooo )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 4 - 4: OooOO000 * oOo0O0Ooo % oOo0O0Ooo / ii
  if 52 - 52: O0oOO0 + OooOO000 * OooOO000 * I1ii11iIi11i - iI11I1II1I1I + Ii1I
def oO00Oooo0O0o0 ( url ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , O0o0OO0000ooo in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , O0o0OO0000ooo )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
i1iI = '{UJ},' ; I1111iIIiIIII = '{WE},' ; oOo0O = '{WP},' ; iiO0000 = '{PP},'
def ooO0OO0Oooo0o ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , O0o0OO0000ooo in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0o0OO0000ooo )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoO00o000 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  iIi1Iii11111I1iii ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIi1Iii11111I1iii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: Ii1I + O0oOO0 * iIi1i1ii1 / IIiIiII11i % oO0o % oO0o
 if 28 - 28: OOooOOo % O0oOO0 - Oooo0O0oo00oO + Oooo0O0oo00oO + O0oOO0 / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * Oooo0O0oo00oO
def ooOoo000 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '(cooltvseries.com)' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , Oo0OO in o0O0OOO0Ooo :
  if '(cooltvseries.com)' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def o0Oii11iIIiIi1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1I1iI ( ( url ) . replace ( ' ' , '%20' ) )
ooO0IIiIIiiiiiII1 = '{XX},' ; iIi1i1II = '{UD},' ; oOoooOO00ooOO = '{YT},' ; I1IiII11II1I = '{JS},' ; oOoOo000 = '{PF},'
if 37 - 37: iiII11i1I1IIi
def iIiI1I1II1 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  OOoOOO0 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( ooO0oOOooOo0 ) ) , 222 , O0o0OO0000ooo )
  if 45 - 45: oOo0O0Ooo + oo0oO00 + ooOoO0O00
def I11Ii111I ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  if 'youtu' in url :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 22 - 22: iIi1i1ii1 / Oooo0O0oo00oO
def O0OOoooO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 31 - 31: O0oOO0 % ooOoO0O00 . ii - I11i + ii
def I1i1Ii ( url ) :
 OOoO = O0
 o00oooO0Oo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , O0o0OO0000ooo )
  if 41 - 41: oO0o / iIi1i1ii1 + OooOO000 . OooOO000 / O0oOO0
  if 74 - 74: IIi % Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
  if 22 - 22: OooOO000 + iiII11i1I1IIi - oo0oO00 + iI11I1II1I1I / OooOO000 - ii
  if 42 - 42: ii - OOooOOo - Oooo0O0oo00oO * OooOO000
  if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( ) :
 if 7 - 7: oOo0O0Ooo
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
 if 40 - 40: OOoOoo
 if 80 - 80: oOo0O0Ooo * OooOO000 % O0oOO0 . Ii % iIi1i1ii1
def iiiI1I1iiiII ( Cat_Name ) :
 if 5 - 5: OOooOOo % Ii1I . OOoOoo . oo0oO00 - Ii
 Ii11I1 = False
 OO00OO = '0'
 if Cat_Name == 'All Channels' : Ii11I1 = True
 if Cat_Name == 'Entertainment' : OO00OO = '1'
 if Cat_Name == 'Movies' : OO00OO = '2'
 if Cat_Name == 'Music' : OO00OO = '3'
 if Cat_Name == 'News' : OO00OO = '4'
 if Cat_Name == 'Sports' : OO00OO = '5'
 if Cat_Name == 'Documentary' : OO00OO = '6'
 if Cat_Name == 'Kids' : OO00OO = '7'
 if Cat_Name == 'Food' : OO00OO = '8'
 if Cat_Name == 'Religious' : OO00OO = '9'
 if Cat_Name == 'USA Channels' : OO00OO = '10'
 if Cat_Name == 'Other' : OO00OO = '11'
 if 27 - 27: o0o00Oo0O * oOo0O0Ooo - iI11I1II1I1I - iiII11i1I1IIi % o0o00Oo0O . I1ii11iIi11i
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoO )
 print 'Len Match: >>>' + str ( len ( o00oooO0Oo ) )
 for Oo0OO , O0o0OO0000ooo , I1ii11IiI1I in o00oooO0Oo :
  Oo0Ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0o0OO0000ooo ) . replace ( '\\' , '' )
  if I1ii11IiI1I == OO00OO :
   I1i11111i1i11 ( Oo0OO , '' , 7022 , Oo0Ii )
  elif Ii11I1 == True :
   I1i11111i1i11 ( Oo0OO , '' , 7022 , Oo0Ii )
  else : pass
  if 96 - 96: IIi
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 24 - 24: o0o00Oo0O
def Ii1Iii1 ( Search_Name ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 for O0o0OO0000ooo , ooO0oOOooOo0 , OooiiIi1i , III11I in o00oooO0Oo :
  Oo0Ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0o0OO0000ooo ) . replace ( '\\' , '' )
  OOoOOO0 ( Search_Name + ': Link 1' , ( ooO0oOOooOo0 ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  OOoOOO0 ( Search_Name + ': Link 2' , ( OooiiIi1i ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  OOoOOO0 ( Search_Name + ': Link 3' , ( III11I ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  if 87 - 87: ii
def iiI1 ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def OoIII ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def OO00O ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  OOoOOO0 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 66 - 66: IIi / o0o00Oo0O . oo0oO00 + iiII11i1I1IIi - IIi . oo0oO00
def II1Iii1I1II1i ( url ) :
 url
 iII1111III1I = xbmcgui . ListItem ( Oo0OO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1111III1I )
 return
 if 100 - 100: Ii - I1ii11iIi11i
 if 47 - 47: iiII11i1I1IIi * OOooOOo * iIi1i1ii1
def iIiii1IIi1I ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOoO )
 for url , o0o0oOoOO0O , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , ( o0o0oOoOO0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 for url in o0O0OOO0Ooo :
  I1i11111i1i11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def IiI1I1i1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , o0o0oOoOO0O , O0o0OO0000ooo in o00oooO0Oo :
  o0OIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , o0o0oOoOO0O )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 OO00OoooO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for Iii11I in OO00OoooO :
  iiIiI1i1 = ( Iii11I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IiiiiI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + O0o0OO0000ooo , '' , iiIiI1i1 )
  if 2 - 2: O0oOO0 . Oooo0O0oo00oO
def ii1O0oOOo ( INFO ) :
 OOOiiiiI ( 'info for workout' , INFO )
 if 33 - 33: oOo0O0Ooo * OooOO000
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . OOoOoo - ooOoO0O00
 if 60 - 60: OOooOOo % OOooOOo
def I1Ii11iI11ii ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( ( Oo0OO ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def oOo0ii1II ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def OOo00o0o0O0oo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   OOoOOO0 ( ( Oo0OO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def i1iI1iIII ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   OOoOOO0 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 76 - 76: IIiIiII11i
   if 28 - 28: ii + OOoOoo . iIi1i1ii1 . I1ii11iIi11i - oOo0O0Ooo
   if 73 - 73: O0oOO0 - oOo0O0Ooo + Ii * IIiIiII11i
   if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
   if 53 - 53: IIi / oOo0O0Ooo * IIi + I11i + O0oOO0 - I1ii11iIi11i
def IIi1iiIIi1i ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 o00oooO0Oo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Daily' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 9008 , Ooo )
def ii1IIi1I11IiIi ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def oOO0ooO00o ( url ) :
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OOoOOO0 ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 56 - 56: ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
def iIIIii111 ( ) :
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '.m3u' in ooO0oOOooOo0 :
   I1i11111i1i11 ( ( Oo0OO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + ooO0oOOooOo0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def I1111IiII1 ( url ) :
 OOoO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / oo0oO00 + oo0oO00
def IIIIiIiIi1 ( ) :
 OOoO = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'category' in ooO0oOOooOo0 :
   I1i11111i1i11 ( Oo0OO , 'http://www.disclose.tv/' + ooO0oOOooOo0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 46 - 46: OooOO000 % Ii1I + IIi
   if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / oo0oO00 + OOoOoo
def i11IiIiii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOoO )
 for url , Oo0OO , O0o0OO0000ooo in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://www.disclose.tv/' + url , 7011 , O0o0OO0000ooo )
 for url in next :
  I1i11111i1i11 ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 15 - 15: OOoOoo * iI11I1II1I1I * O0oOO0
  if 96 - 96: OooOO000 * iI11I1II1I1I / OOooOOo % Oooo0O0oo00oO * IIiIiII11i
def I1iiIIii ( url ) :
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
  if 90 - 90: iIi1i1ii1 * oo0oO00 % IIiIiII11i / Oooo0O0oo00oO
  if 97 - 97: iiII11i1I1IIi % OOoOoo
def II1111iiI1II ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - IIi * iI11I1II1I1I
def OO0ooo0OOO ( name , url , img ) :
 I1 = O0 ( url )
 O00oOO = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 O000O000 = len ( O00oOO )
 if 55 - 55: IIiIiII11i - OooOO000 - Oooo0O0oo00oO % IIi
 if 49 - 49: I1ii11iIi11i * OooOO000
 if O000O000 == 1 :
  for OOO0 in O00oOO :
   OOO0 = OOO0 . replace ( 'player' , 'watch' )
   I11ii1I = OOO0 + '&fv=&sou='
   i1iIi1iiii1ii = O0 ( I11ii1I )
   oO0oOo = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( i1iIi1iiii1ii )
   for oooOooooO0oOO in oO0oOo :
    IIiIiii = False
    Resolve ( oooOooooO0oOO )
    if 71 - 71: I11i + Oooo0O0oo00oO . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
 elif O000O000 > 1 :
  if 91 - 91: o0o00Oo0O - oo0oO00 % OooOO000
  for OOO0 in O00oOO :
   I1ii = O0 ( OOO0 )
   OOooOOOO0O0OoO0O0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( I1ii )
   iiii1 = OOooOOOO0O0OoO0O0
   iiii1 = ( str ( iiii1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iiii1
   OOoOOO0 ( 'DOUBLE LINK' , iiii1 , 424 , '' )
   if 20 - 20: IIi . OooOO000 % IIi
   for url in OOooOOOO0O0OoO0O0 :
    I1i11111i1i11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OooiiIi1i = Google . resolve ( url )
    except :
     pass
    try :
     i11iI1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OooiiIi1i ) )
     for o00o0oO0O , iIIii in i11iI1 :
      if 95 - 95: OooOO000 + iIi1i1ii1 * iI11I1II1I1I
      HD_URLS . append ( o00o0oO0O )
      SD_URLS . append ( iIIii )
    except :
     pass
 else :
  pass
  if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / IIi
def iiii1ii1 ( ) :
 if 12 - 12: Ii - iI11I1II1I1I * iIi1i1ii1 * iiII11i1I1IIi
 if 19 - 19: o0o00Oo0O + O0oOO0 + I11i
 I1i11111i1i11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 81 - 81: iI11I1II1I1I
 I1i11111i1i11 ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 51 - 51: I11i . Ii1I * IIi / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % OooOO000 % O0oOO0 + oo0oO00 * O0oOO0 . IIi
def OoOo0Oooo0o ( ) :
 OOoO = O0 ( 'http://cnfstudio.com/' )
 o00oooO0Oo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , 'http://cnfstudio.com/genre/' + ooO0oOOooOo0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 65 - 65: OOooOOo + OooOO000 % oOo0O0Ooo
iI111I11I1I1 = xbmcgui . Dialog ( )
if 54 - 54: OooOO000 / I11i
I11IIIIiII = '{UN},' ; OoooO = '{IG},' ; IIIi1IIiII11 = '{PL},' ; I1IIi = '{LO},' ; O00O = '{LP},' ; IiIIiIiIIiI = '{HA},' ; I1ii11I1IiI = '{XD},' ; i1IIIii = '{TA},' ; I1I111i = '{DP},' ; OOooOOoO0 = '{JT},' ; Ii11i = '{JJ},' ; O00i1i = '{MM},' ; iiii = '{FQ},' ; IIiii1I1I = '{HH},'
if 62 - 62: IIiIiII11i - OOooOOo * IIi
def oO0OO0O ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOoO )
 oooOoooOOo0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOoO )
 for O0o0OO0000ooo , url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , O0o0OO0000ooo )
 oooOoooOOo0 = oooOoooOOo0
 for url in oooOoooOOo0 :
  I1i11111i1i11 ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 25 - 25: iiII11i1I1IIi + oOo0O0Ooo + OOooOOo + OooOO000 % o0o00Oo0O
def i1Ii1I ( url ) :
 if 60 - 60: OOoOoo * IIi + OooOO000 . Oooo0O0oo00oO . o0o00Oo0O
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  O0o0O00Oo0o0 = url + '&fv=&sou='
  O0o0O00Oo0o0 = O0o0O00Oo0o0 . replace ( 'player' , 'watch' )
  Ii1i1ii = ooOOoO00o0o0oo0o ( O0o0O00Oo0o0 )
  i1i1ii11IiI = ooOOoO00o0o0oo0o ( url )
  if 6 - 6: Ii
  if 16 - 16: iIi1i1ii1
def ooOOoO00o0o0oo0o ( url ) :
 if 84 - 84: ooOoO0O00 / iI11I1II1I1I / O0oOO0 / IIi
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  o00o ( url )
  if 7 - 7: OOooOOo . Oooo0O0oo00oO % I1ii11iIi11i
  if 55 - 55: OOoOoo - I1ii11iIi11i * O0oOO0
def OOOOO0oOOoO ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , OO0o , '' )
 if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  oo000o = open ( O0OoO000O0OO , 'r' )
  for iII1111III1I in oo000o :
   iIIIII = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1111III1I )
   for Oo0OO , ooO0oOOooOo0 in iIIIII :
    OOoOOO0 ( Oo0OO , ooO0oOOooOo0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 if os . path . exists ( Remote ) :
  I1 = oo0O0o00o0O ( url )
  o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , url in o00oooO0Oo :
   url = ( url ) . strip ( )
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 78 - 78: o0o00Oo0O - OooOO000 * Oooo0O0oo00oO + oo0oO00 + IIiIiII11i
  if 15 - 15: I1ii11iIi11i . Ii + OOoOoo / Ii1I / iiII11i1I1IIi + ii
def OOoO00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + ooO0oOOooOo0
 Oo0OO = 'plugin.video.GenieTv'
 if 55 - 55: Ii * o0o00Oo0O
 ooO00Oo ( ooO0oOOooOo0 , Oo0OO )
 if 46 - 46: OOoOoo - OOoOoo * Ii1I / iiII11i1I1IIi * Oooo0O0oo00oO / I11i
def i1IiiiI1iI ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooO0oOOooOo0
 Oo0OO = 'repository.GenieTv'
 if 67 - 67: Oooo0O0oo00oO - IIi % iiII11i1I1IIi / IIiIiII11i + oOo0O0Ooo * OOoOoo
 ooO00Oo ( ooO0oOOooOo0 , Oo0OO )
 if 100 - 100: Ii1I
 if 81 - 81: Ii1I % iiII11i1I1IIi
def OO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  IiiII1I ( )
 if O0oO0 == 1 :
  iI1iI1iIi1ii1I1 ( )
  if 59 - 59: IIiIiII11i * ii - ii
  if 33 - 33: o0o00Oo0O . Ii % I11i
  if 50 - 50: OOoOoo
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Oooo0O0oo00oO
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oo0ooO0O = 'https://addons.tvaddons.ag/'
if 83 - 83: I1ii11iIi11i / OOoOoo
def iI1iI1iIi1ii1I1 ( ) :
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 ooo0oo00O00Oo = 'https://addons.tvaddons.ag/search/?keyword=' + iIIII1i
 I1 = O0 ( ooo0oo00O00Oo )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , 10054 , 'https://addons.tvaddons.ag/' + o00OooO0oo , OO0o , '' )
  if 11 - 11: I11i - IIiIiII11i % O0oOO0 . IIiIiII11i
  if 65 - 65: O0oOO0 . Ii % Oooo0O0oo00oO * iiII11i1I1IIi % I1ii11iIi11i
def IiiII1I ( ) :
 I1 = O0 ( oo0ooO0O )
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
   if 51 - 51: oO0o % iiII11i1I1IIi
   if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
def Addon ( url ) :
 I1 = O0 ( url )
 II1IiI1II1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if 'Please' in Oo0OO :
   pass
  else :
   o0OIiII ( Oo0OO , url , 10054 , 'https://addons.tvaddons.ag/' + O0o0OO0000ooo , OO0o , '' )
 for url in II1IiI1II1 :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
  if 21 - 21: ii . o0o00Oo0O / Ii
  if 86 - 86: OOooOOo / Oooo0O0oo00oO
def Iii1I ( url , name ) :
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
   if 32 - 32: Oooo0O0oo00oO - IIi . oO0o * OOoOoo + iIi1i1ii1 . ooOoO0O00
def ooO00Oo ( url , name ) :
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
 if 61 - 61: oo0oO00 * IIi + oo0oO00 - I1ii11iIi11i % OOooOOo . iiII11i1I1IIi
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 51 - 51: Oooo0O0oo00oO / oo0oO00
 if 51 - 51: OOoOoo * O0oOO0 - OooOO000 + iiII11i1I1IIi
def II1iiII1 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 1007 , o00OooO0oo )
def I1IiiIIiIii1i ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , o00OooO0oo )
  if 27 - 27: OOoOoo . I1ii11iIi11i + OOoOoo + iiII11i1I1IIi
  if 28 - 28: oO0o - OOoOoo - O0oOO0 % O0oOO0 / o0o00Oo0O
def I11IIIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , iconimage , o0o0oOoOO0O , iiI11ii1I1 , name in o00oooO0Oo :
  if 'http' in url :
   if '.php' in url :
    ooO0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
    for iII1111III1I in ooO0 :
     if iII1111III1I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoIi1I1I ( name , url , 1016 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
   else :
    if 'youtube' in url :
     ooO0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for iII1111III1I in ooO0 :
      if iII1111III1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
    else :
     ooO0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for iII1111III1I in ooO0 :
      if iII1111III1I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0o ( name , url , 222 , iconimage , iiI11ii1I1 , o0o0oOoOO0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
  else :
   oooo0OoOo ( url , iconimage , name )
   if 69 - 69: O0oOO0
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
      ooO0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
      for iII1111III1I in ooO0 :
       if iII1111III1I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOoOOO0 ( name , url , 222 , o00OooO0oo )
      Iii1I1I11iiI1 ( 'movies' , 'INFO' )
   else :
    oooo0OoOo ( url , o00OooO0oo , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 95 - 95: iI11I1II1I1I
def oooo0OoOo ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o0O0ooo0o = ( url ) . replace ( oooOoO0oo0o0 , 'http' ) . replace ( iIi1i1II , '.com' ) ;
 O0Oo = ( o0O0ooo0o ) . replace ( IiIIIii1i1iI , 'a' ) . replace ( Iii1iii1I , 'b' ) . replace ( oOo000Oo00o , 'c' ) . replace ( I1111iIIiIIII , 'd' ) . replace ( IIIi1IIiII11 , 'e' ) . replace ( OOooOOoO0 , 'f' ) ;
 O0oOo00Oo0oo0 = ( O0Oo ) . replace ( ooO0IIiIIiiiiiII1 , 'g' ) . replace ( IiIIiIiIIiI , 'h' ) . replace ( oOoooOO00ooOO , 'i' ) . replace ( oOoOo000 , 'j' ) . replace ( o0ooOOoOoOO , 'k' ) . replace ( iII11 , 'l' ) ;
 i111O0oOO0o00OO = ( O0oOo00Oo0oo0 ) . replace ( II1i11i1iI1I , 'm' ) . replace ( oooOoO00O , 'n' ) . replace ( I1i1IIiiI11II , 'o' ) . replace ( Ii1i1 , 'p' ) . replace ( iiiIiIIiIiiii , 'q' ) . replace ( o00O0OooO0 , 'r' ) ;
 iii1II11II1 = ( i111O0oOO0o00OO ) . replace ( I11i1Iii1I , 's' ) . replace ( oOo0O , 't' ) . replace ( iIIiII1 , 'u' ) . replace ( iI1Iii1i1 , 'v' ) . replace ( OoOo00oOoo0oO , 'w' ) . replace ( i1ii1iIII , 'x' ) ;
 oooo = ( iii1II11II1 ) . replace ( ooo0000oo0 , 'y' ) . replace ( O0oooo000o , 'z' ) . replace ( I11IIIIiII , '.' ) . replace ( OoooO , '(' ) . replace ( I1IIi , ')' ) . replace ( O00O , '/' ) ;
 IIiIiI11II = ( oooo ) . replace ( ooo000 , '1' ) . replace ( iiO0000 , '2' ) . replace ( oOo00 , '3' ) . replace ( i1IIIii , '4' ) . replace ( I1I111i , '5' ) . replace ( I1IiII11II1I , '6' ) ;
 OoooI1iIiii = ( IIiIiI11II ) . replace ( Ii11i , '7' ) . replace ( O00i1i , '8' ) . replace ( iiii , '9' ) . replace ( IIiii1I1I , '0' ) . replace ( I11iI1iIii1ii , ':' ) . replace ( OoOoOo0o00OoOO , '%' ) ;
 url = ( OoooI1iIiii ) . replace ( i1iI , '-' ) . replace ( I1ii11I1IiI , '_' ) ;
 OOoOOO0 ( name , url , 222 , iconimage ) ;
 if 87 - 87: IIiIiII11i * oO0o + IIi . I1ii11iIi11i - Ii1I * O0oOO0
 if 15 - 15: IIiIiII11i + o0o00Oo0O
def OOo0o ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1007 , o00OooO0oo )
def o000 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , o00OooO0oo )
  if 58 - 58: O0oOO0 * Ii * oOo0O0Ooo * Ii1I % Ii - ii
def ii1II11IIII ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 oO0OOOO0o0o0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 oO0OOOO0o0o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oO0OOOO0o0o0 )
 if 21 - 21: o0o00Oo0O * OOoOoo % oO0o
 if 14 - 14: o0o00Oo0O / OooOO000 / OOoOoo + iIi1i1ii1 - iIi1i1ii1
def oo0O ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  if '-dir-' in Oo0OO :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , O0o0OO0000ooo )
  else :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , O0o0OO0000ooo )
   if 10 - 10: o0o00Oo0O - Ii1I / OooOO000 % OOooOOo / ii / IIi
def O000oOo ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00Oo00O0o = ( 'http://afewbitsmore.com/' )
 o00oooO0Oo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '[To Parent Directory]' in Oo0OO :
   Oo0OO = 'HOME'
   pass
  elif 'HOME' in Oo0OO :
   pass
  elif '.m3u' in Oo0OO :
   I1i11111i1i11 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , o00Oo00O0o + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , o00Oo00O0o + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in Oo0OO :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , o00Oo00O0o + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , o00Oo00O0o + url , 1012 , oOOOo00O00oOo + 'music.png' )
def ooooOOo ( url ) :
 I1 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , Oo0OO , url in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 73 - 73: IIi + iiII11i1I1IIi % Oooo0O0oo00oO + ii * I1ii11iIi11i
def i1IiiI1i11 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 o00Oo00O0o = url
 o00oooO0Oo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '.mp3' in Oo0OO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   I1i11111i1i11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/' , '' ) , o00Oo00O0o + url , 1011 , oOOOo00O00oOo + 'music.png' )
def OO0OoO0OOoOo ( ) :
 OOoO = oo0O0o00o0O ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , O0o0OO0000ooo , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ( 'http://www.cyn.net/music/' + ooO0oOOooOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + O0o0OO0000ooo ) . replace ( ' ' , '%20' ) )
def oO000 ( url , img ) :
 OOoO = oo0O0o00o0O ( url )
 OooiiIi1i = url
 img = img
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OooiiIi1i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 20 - 20: OOooOOo % o0o00Oo0O
def Oo00OO0 ( url ) :
 OOoO = oo0O0o00o0O ( url )
 OooiiIi1i = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for type , url , Oo0OO in o00oooO0Oo :
  if '[VID]' in type :
   OOoOOO0 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OooiiIi1i + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   Oo00OO0 ( OooiiIi1i + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: o0o00Oo0O . I11i % Ii1I * O0oOO0 + oo0oO00
 if 82 - 82: ii
def oO00OoOOOo ( ) :
 O00OO00OOOoO = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOoOOoOOooOO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIII1i = oOoOOoOOooOO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OooiiIi1i = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 III11I = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( OooiiIi1i )
 Iiii = Oo0OoO00oOO0o ( III11I )
 if 27 - 27: Ii % iiII11i1I1IIi + IIi . Oooo0O0oo00oO
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o00oooO0Oo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooO0oOOooOo0 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 9 - 9: oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o0O0OOO0Ooo :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OooiiIi1i + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 43 - 43: IIi . Oooo0O0oo00oO + oOo0O0Ooo * Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  o0OOo00OoO = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for Oo0OO in o0OOo00OoO :
   if oOoOOoOOooOO in Oo0OO . lower ( ) :
    I1i11111i1i11 ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( III11I + Oo0OO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 2 - 2: Oooo0O0oo00oO
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 3 - 3: oOo0O0Ooo . iiII11i1I1IIi % o0o00Oo0O - OOoOoo / o0o00Oo0O
    if 79 - 79: IIi + O0oOO0 % OOoOoo % oOo0O0Ooo
    if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
    if 53 - 53: iiII11i1I1IIi . O0oOO0 / I1ii11iIi11i . oO0o . Ii
    if 60 - 60: IIiIiII11i
    if 25 - 25: I1ii11iIi11i + I11i - oO0o
II1i11i1iI1I = '{SF},' ; oooOoO00O = '{IF},' ; I1i1IIiiI11II = '{PW},' ; oOo00 = '{AM},' ; Ii1i1 = '{GF},' ; iiiIiIIiIiiii = '{DD},' ; o00O0OooO0 = '{UO},' ; I11i1Iii1I = '{LE},' ; iIIiII1 = '{ZY},' ; iI1Iii1i1 = '{UE},' ; OoOo00oOoo0oO = '{PE},' ; i1ii1iIII = '{JE},' ; ooo0000oo0 = '{TH},' ; O0oooo000o = '{LK},'
if 57 - 57: IIiIiII11i . ooOoO0O00
if 33 - 33: iiII11i1I1IIi + I1ii11iIi11i % oo0oO00 . O0oOO0
def OOOOoO00o0O ( ) :
 OOoO = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 o00oooO0Oo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def i1II1i ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OOoO )
 for url , Oo0OO , oO00oOOo0Oo in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO + oO00oOOo0Oo , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def O0oooooO0oOOo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oo0O0OO0Oooo ( url )
def oo0O0OO0Oooo ( url ) :
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
   if 7 - 7: IIiIiII11i - Ii1I / oo0oO00 % ii + ooOoO0O00
def I1Iii1 ( ) :
 OOoO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o00oooO0Oo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 9 - 9: IIiIiII11i % I1ii11iIi11i * IIi + iIi1i1ii1 % oO0o . ooOoO0O00
  if 68 - 68: IIiIiII11i % OooOO000 * Ii
def iiiI1I ( ) :
 OOoO = O0 ( 'http://www.animetoon.org/cartoon' )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , ooO0oOOooOo0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 92 - 92: I1ii11iIi11i % I11i - OOoOoo / OOoOoo / OOooOOo
  if 84 - 84: Oooo0O0oo00oO
  if 4 - 4: iIi1i1ii1 . OooOO000 / IIi / iiII11i1I1IIi + IIiIiII11i
def IiiiiI ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for O0o0OO0000ooo in o0O0OOO0Ooo :
  oooOoO = O0o0OO0000ooo
 o0OOo00OoO = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in o0OOo00OoO :
  I1i11111i1i11 ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  I1i11111i1i11 ( Oo0OO , url , 1003 , oooOoO )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoOOooOoo ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   O00OO0oOOO ( url )
  elif 'playpanda' in url :
   O00OO0oOOO ( url )
   if 41 - 41: iIi1i1ii1 * ii . OOoOoo % Ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00OO0oOOO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  OOoOOO0 ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 11 - 11: iI11I1II1I1I . OooOO000 - I1ii11iIi11i / oo0oO00 + IIiIiII11i
  if 29 - 29: oo0oO00 . Ii + ooOoO0O00 - IIi + o0o00Oo0O . oOo0O0Ooo
def i1iIiII1 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOO00O . add_header ( 'referer' , url )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 59 - 59: ii + OooOO000 % I11i - OOooOOo . oOo0O0Ooo
def oo0O0o00o0O ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 42 - 42: OooOO000
def OOO00OOOO0o ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0ooo0o0 = ( '%s%s' % ( O00Oooo00 , url ) )
 O0o0O00Oo0o0 = oo0O0o00o0O ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , o00OooO0oo , Oo0OO in o00oooO0Oo :
  OOoOOO0 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , o00OooO0oo )
  if 70 - 70: iI11I1II1I1I
def o00o ( url ) :
 if 79 - 79: Ii
 IiI1i1ii = open ( I11i1I1I , "a" )
 IiI1i1ii . write ( 'url="' + url + '"\n' )
 IiI1i1ii . close
 if 46 - 46: o0o00Oo0O % ii
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 import urlresolver
 try : i1IiII1III . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Oo0OO ) )
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : i1IiII1III . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 22 - 22: iiII11i1I1IIi + ii - OOooOOo - oO0o * OooOO000 - O0oOO0
def O0ooO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 o0oOoO00o . update ( 100 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 i1IiII1III . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 80 - 80: oOo0O0Ooo % iIi1i1ii1 / oo0oO00 * oO0o - O0oOO0 / O0oOO0
def I1I1iI ( url ) :
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : i1IiII1III . play ( url ) . strip ( )
 except : pass
 if 13 - 13: I1ii11iIi11i
def oO0OooO00Oo ( url ) :
 i1IiII1III = xbmc . Player ( i1O00oo ( ) )
 import urlresolver
 oO0OO00O0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 i1IiII1III . play ( oO0OO00O0 )
 xbmc . sleep ( 1 )
 i1IiII1III . play ( url )
 if 65 - 65: Oooo0O0oo00oO % iIi1i1ii1 % I11i . IIi . Ii1I
 if 64 - 64: Ii1I . IIi / Ii1I * IIi
def i1O00oo ( ) :
 try :
  Oo00o00OO0oO = getSet ( "core-player" )
  if ( Oo00o00OO0oO == 'DVDPLAYER' ) : IIIIiiI1iIiI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( Oo00o00OO0oO == 'MPLAYER' ) : IIIIiiI1iIiI = xbmc . PLAYER_CORE_MPLAYER
  elif ( Oo00o00OO0oO == 'PAPLAYER' ) : IIIIiiI1iIiI = xbmc . PLAYER_CORE_PAPLAYER
  else : IIIIiiI1iIiI = xbmc . PLAYER_CORE_AUTO
 except : IIIIiiI1iIiI = xbmc . PLAYER_CORE_AUTO
 return IIIIiiI1iIiI
 return True
 if 91 - 91: I11i * Ii1I - iiII11i1I1IIi . IIiIiII11i
def I1i11111i1i11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 1 - 1: Oooo0O0oo00oO + OooOO000 * Ii1I
def O0OOo ( name , url , mode , iconimage , fanart , description ) :
 if 44 - 44: iiII11i1I1IIi
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = True )
 return oOoo000
 if 79 - 79: I11i % Oooo0O0oo00oO . o0o00Oo0O
def OOoOOO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiI11i1IIiiI = [ ]
  if showcontext == 'fav' :
   IiI11i1IIiiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IiI11i1IIiiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OooOo00o . addContextMenuItems ( IiI11i1IIiiI )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 56 - 56: O0oOO0 + ooOoO0O00 * iiII11i1I1IIi - o0o00Oo0O
 if 84 - 84: iiII11i1I1IIi % oOo0O0Ooo / iI11I1II1I1I * IIi * iI11I1II1I1I + Ii1I
 if 78 - 78: iIi1i1ii1 / iiII11i1I1IIi * IIi . Oooo0O0oo00oO . O0oOO0 - OooOO000
 if 39 - 39: OOoOoo . ooOoO0O00 + ii . iiII11i1I1IIi - Ii % OooOO000
 if 38 - 38: O0oOO0
 if 9 - 9: oo0oO00 . oO0o . O0oOO0 / ii
def OOOiiiiI ( heading , announce ) :
 class oo0ooo ( ) :
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
   try : oOOo0O00o = open ( announce ) ; Ii1 = oOOo0O00o . read ( )
   except : Ii1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ii1 ) )
   return
 oo0ooo ( )
 oo0ooo ( )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
def OOI1iI1ii1II ( ) :
 OOOiiiiI ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 41 - 41: Ii1I % Ii1I + iIi1i1ii1 . iiII11i1I1IIi % OooOO000 * OOoOoo
 if 57 - 57: IIi . OooOO000 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: OOoOoo / Oooo0O0oo00oO * o0o00Oo0O
 if 17 - 17: oO0o / OOoOoo % oOo0O0Ooo
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / iIi1i1ii1 . Ii / oO0o % IIiIiII11i
 if 6 - 6: iiII11i1I1IIi % I11i + OooOO000
 if 91 - 91: I11i + o0o00Oo0O * O0oOO0 * iIi1i1ii1 * Ii1I
 if 83 - 83: ii
 if 52 - 52: I11i / OOooOOo % O0oOO0 % oO0o / iIi1i1ii1 % I11i
 if 88 - 88: Oooo0O0oo00oO / Ii / IIi / Ii * Ii1I % oo0oO00
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * IIi + iI11I1II1I1I
 if 80 - 80: I11i . iiII11i1I1IIi . ii
 if 63 - 63: OOoOoo . Oooo0O0oo00oO
 if 66 - 66: oOo0O0Ooo
 if 99 - 99: oO0o % o0o00Oo0O . OooOO000 - Ii1I . I1ii11iIi11i / OOooOOo
 if 60 - 60: Ii1I
 if 78 - 78: O0oOO0 + IIiIiII11i
 if 55 - 55: ii
 if 90 - 90: oOo0O0Ooo
 if 4 - 4: Oooo0O0oo00oO % OOoOoo - Oooo0O0oo00oO - I11i
 if 30 - 30: iIi1i1ii1
 if 34 - 34: O0oOO0 - IIiIiII11i - I11i + iiII11i1I1IIi + OooOO000
 if 70 - 70: ii + oO0o * I1ii11iIi11i
 if 20 - 20: Ii - IIiIiII11i - OOoOoo % O0oOO0 . OOoOoo
 if 50 - 50: iI11I1II1I1I + OooOO000 - oo0oO00 - ii
 if 84 - 84: OOooOOo - oo0oO00
 if 80 - 80: Ii % Oooo0O0oo00oO - I1ii11iIi11i % Oooo0O0oo00oO
def O0O0oOo0o0o0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 15 - 15: ii - OOoOoo / oo0oO00 % IIi * iiII11i1I1IIi
def I1IiIi11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i1I1i1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 35 - 35: iI11I1II1I1I % OooOO000 * oo0oO00 . I1ii11iIi11i
def I11IiiI1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oOo0OoOOoO0Ooo0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 33 - 33: oOo0O0Ooo / oo0oO00 . I1ii11iIi11i
def O0OoO0oo0Oo00oOOO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o0ii1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 35 - 35: iI11I1II1I1I
def IIii1I1IIii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i11III ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 97 - 97: oo0oO00 / ii - OOoOoo . OOoOoo * iiII11i1I1IIi
def i11IiIi1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + O00ooOooOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 11 - 11: I11i * I1ii11iIi11i
def OO00oOO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + IiiII1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , iIIiiI1II1i11 , iiI11ii1I1 , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 96 - 96: ii % iiII11i1I1IIi - ii % o0o00Oo0O
def iiiiIiiiii1I ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iIiI11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
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
def Ii1I1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOoOooO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , iIIiiI1II1i11 , iiI11ii1I1 , OOo in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , OOo )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 58 - 58: Ii1I / oO0o / O0oOO0 + iIi1i1ii1 % iiII11i1I1IIi / IIiIiII11i
 if 95 - 95: IIiIiII11i / IIi % oo0oO00 - ii
 if 45 - 45: oO0o * ii / o0o00Oo0O . OooOO000 / OOooOOo
 if 53 - 53: OOooOOo . oOo0O0Ooo * Ii1I
 if 56 - 56: iI11I1II1I1I / IIi % IIi . IIi + I11i * ii
 if 89 - 89: O0oOO0 - OooOO000
 if 89 - 89: Ii1I - ooOoO0O00 + oo0oO00 % I1ii11iIi11i
 if 52 - 52: I1ii11iIi11i - o0o00Oo0O
 if 84 - 84: IIi * IIiIiII11i / OooOO000 / iiII11i1I1IIi - iIi1i1ii1
def oOOOO ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( O00o0OO ) :
     o0i11iiI11II = 0
     o0i11iiI11II += len ( II1IIIii )
     if o0i11iiI11II > 0 :
      for oOOo0O00o in II1IIIii :
       os . unlink ( os . path . join ( IiIIiii1I , oOOo0O00o ) )
  iI1iIii = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( iI1iIii )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 42 - 42: Ii1I / OOoOoo . iI11I1II1I1I
 if 5 - 5: ii
 if 21 - 21: Oooo0O0oo00oO
 if 71 - 71: Oooo0O0oo00oO + O0oOO0 . oo0oO00
 if 9 - 9: oO0o
 if 13 - 13: oo0oO00 . oO0o
 if 73 - 73: IIi * ii * oo0oO00 - Ii
 if 58 - 58: I11i + OOooOOo - iIi1i1ii1
def IiI1II11iiI ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 82 - 82: IIi . iI11I1II1I1I / IIi / O0oOO0 % iI11I1II1I1I
def O0ooO0Oo00o ( url ) :
 i1iii1I1I = os . path . join ( oO , 'addon_data' )
 Oo0O0o0Oo0Oo = [
 ( i1iii1I1I ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( i1iii1I1I , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i1iii1I1I , 'plugin.video.itv' , 'Images' ) ) ]
 if 10 - 10: IIiIiII11i . I1ii11iIi11i + I1ii11iIi11i / OooOO000 / Ii / OooOO000
 O0oooOoO = 0
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / Oooo0O0oo00oO / OooOO000
 for iII1111III1I in Oo0O0o0Oo0Oo :
  if os . path . exists ( iII1111III1I ) and not iII1111III1I in [ oOo0oooo00o , i1iii1I1I ] :
   for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( iII1111III1I ) :
    o0i11iiI11II = 0
    o0i11iiI11II += len ( II1IIIii )
    if o0i11iiI11II > 0 :
     for oOOo0O00o in II1IIIii :
      if not oOOo0O00o in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( IiIIiii1I , oOOo0O00o ) )
       except :
        pass
      else : ii1 ( 'Ignore Log File: %s' % oOOo0O00o )
     for OoOOoO0oOo in i1II11II1 :
      try :
       shutil . rmtree ( os . path . join ( IiIIiii1I , OoOOoO0oOo ) )
       O0oooOoO += 1
       ii1 ( "[Success] cleared %s files from %s" % ( str ( o0i11iiI11II ) , os . path . join ( iII1111III1I , OoOOoO0oOo ) ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
  else :
   for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( iII1111III1I ) :
    for OoOOoO0oOo in i1II11II1 :
     if 'cache' in OoOOoO0oOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( IiIIiii1I , OoOOoO0oOo ) )
       O0oooOoO += 1
       ii1 ( "[Success] wiped %s " % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1111III1I , OoOOoO0oOo ) )
       if 35 - 35: iiII11i1I1IIi * Oooo0O0oo00oO
 IiI1II11iiI ( oo0o0O00 , 'Clear Cache: Removed %s Files' % O0oooOoO )
 if 65 - 65: IIiIiII11i % ooOoO0O00
 if 13 - 13: oO0o * OooOO000 + I1ii11iIi11i - iIi1i1ii1
 if 31 - 31: oO0o
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - OooOO000 . Ii1I % I1ii11iIi11i . IIi
 if 9 - 9: I11i
 if 55 - 55: Oooo0O0oo00oO % iI11I1II1I1I + oo0oO00 . OOoOoo
def Iii1Ii ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 ooOoii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( ooOoii ) :
   o0i11iiI11II = 0
   o0i11iiI11II += len ( II1IIIii )
   if 88 - 88: IIiIiII11i - iiII11i1I1IIi / ii
   if 71 - 71: Ii1I
   if o0i11iiI11II > 0 :
    if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0i11iiI11II ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: iIi1i1ii1 % ooOoO0O00
     for oOOo0O00o in II1IIIii :
      os . unlink ( os . path . join ( IiIIiii1I , oOOo0O00o ) )
     for OoOOoO0oOo in i1II11II1 :
      shutil . rmtree ( os . path . join ( IiIIiii1I , OoOOoO0oOo ) )
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
 if 41 - 41: oO0o * oO0o / iiII11i1I1IIi + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / IIi
 if 80 - 80: Ii1I
 if 67 - 67: IIiIiII11i
 if 2 - 2: I11i - o0o00Oo0O * IIi % iIi1i1ii1
 if 64 - 64: ooOoO0O00 . OOoOoo
 if 7 - 7: O0oOO0 . iiII11i1I1IIi - iiII11i1I1IIi / OooOO000 % I1ii11iIi11i
 if 61 - 61: O0oOO0 - Ii1I / iiII11i1I1IIi % Ii1I + oO0o / I1ii11iIi11i
 if 10 - 10: Ii / OOooOOo
def OO0Oooo0oOO0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 ooOoii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( ooOoii ) :
   o0i11iiI11II = 0
   o0i11iiI11II += len ( II1IIIii )
   if 27 - 27: oOo0O0Ooo / ii
   if 74 - 74: Ii1I % OooOO000 - oO0o * oo0oO00 . ii * oO0o
   if o0i11iiI11II > 0 :
    if 99 - 99: OOooOOo . iiII11i1I1IIi - ii - o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( o0i11iiI11II ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: Oooo0O0oo00oO
     for oOOo0O00o in II1IIIii :
      os . unlink ( os . path . join ( IiIIiii1I , oOOo0O00o ) )
     for OoOOoO0oOo in i1II11II1 :
      shutil . rmtree ( os . path . join ( IiIIiii1I , OoOOoO0oOo ) )
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
 if 3 - 3: o0o00Oo0O - OooOO000 * IIi * Oooo0O0oo00oO / IIi
 if 58 - 58: IIi * iI11I1II1I1I + OOoOoo . OOoOoo
 if 74 - 74: OOoOoo - I11i * iIi1i1ii1 % OOoOoo
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * OooOO000 - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . O0oOO0 . ii . Oooo0O0oo00oO * Ii1I
 if 80 - 80: OooOO000 + oo0oO00 . OooOO000 + Oooo0O0oo00oO
 if 85 - 85: Ii . oo0oO00 + IIi / IIi
 if 43 - 43: iIi1i1ii1 . ii - IIiIiII11i
def OoOo0O0O ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o000oOOoo = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 ooooOoo = os . path . join ( oOooO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( ooooOoo ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o000oOOoo = os . path . join ( oOooO0 , 'advancedsettings.xml' )
   try :
    os . remove ( o000oOOoo )
    print '=== GenieTv - REMOVING    ' + str ( o000oOOoo ) + '    ==='
   except :
    pass
   O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
   iIiII = open ( o000oOOoo , "w" )
   iIiII . write ( O0o0O00Oo0o0 )
   iIiII . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o000oOOoo ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o000oOOoo = os . path . join ( oOooO0 , 'advancedsettings.xml' )
  try :
   os . remove ( o000oOOoo )
   print '=== GenieTv - REMOVING    ' + str ( o000oOOoo ) + '    ==='
  except :
   pass
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  iIiII = open ( o000oOOoo , "w" )
  iIiII . write ( O0o0O00Oo0o0 )
  iIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o000oOOoo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 99 - 99: iiII11i1I1IIi % I11i + iI11I1II1I1I
def OoOOOO0ooO0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o000oOOoo = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  iIiII = open ( o000oOOoo ) . read ( )
  if 'zero' in iIiII :
   name = '0CACHE'
  elif 'tuxen' in iIiII :
   name = 'TUXENS'
  elif 'muckys' in iIiII :
   name = 'MUCKYS'
  elif 'p2p1' in iIiII :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iIiII :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iIiII :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 76 - 76: oO0o - o0o00Oo0O - IIiIiII11i
def I11I1I111 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o000oOOoo = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  os . remove ( o000oOOoo )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o000oOOoo ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 72 - 72: ooOoO0O00
 if 72 - 72: OOoOoo + IIiIiII11i . o0o00Oo0O - iiII11i1I1IIi / ii . OooOO000
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
 if 29 - 29: Ii1I
 if 41 - 41: IIi
 if 49 - 49: IIi % IIiIiII11i . IIi - I11i - oo0oO00 * iIi1i1ii1
 if 47 - 47: o0o00Oo0O . I11i / IIi * iiII11i1I1IIi
 if 63 - 63: OooOO000 - O0oOO0 - iiII11i1I1IIi - OOoOoo / O0oOO0 + oO0o
 if 94 - 94: iIi1i1ii1 / oOo0O0Ooo . IIiIiII11i
def ii11I11i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o00oooO0Oo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for II1oOO0O0Ooo0 , I11iiI1i , ooOoOO , iIiiII11 in o00oooO0Oo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % II1oOO0O0Ooo0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ooOoOO , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iIiiII11 )
  inc = inc + 1
  if 75 - 75: OOooOOo + IIi . Ii / IIi
  if 32 - 32: IIi + iIi1i1ii1 + Ii1I
  if 79 - 79: ooOoO0O00 / IIi
  if 81 - 81: iI11I1II1I1I
  if 86 - 86: iIi1i1ii1 % iIi1i1ii1 % ii
  if 42 - 42: I1ii11iIi11i . O0oOO0 + o0o00Oo0O / Oooo0O0oo00oO % ii
  if 19 - 19: OOoOoo / IIi
  if 43 - 43: OOooOOo % IIi + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
  if 98 - 98: I11i * I1ii11iIi11i - IIi . OOoOoo
def iI11i1iI ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o000oOOoo = os . path . join ( oOooO0 , 'addons2.ini' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  iIiII = open ( o000oOOoo , "w" )
  iIiII . write ( O0o0O00Oo0o0 )
  iIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o000oOOoo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 95 - 95: Ii % oO0o % OOoOoo
def i1iOOIiIII1i ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o000oOOoo = os . path . join ( oOooO0 , 'settings.xml' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  iIiII = open ( o000oOOoo , "w" )
  iIiII . write ( O0o0O00Oo0o0 )
  iIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o000oOOoo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 56 - 56: I1ii11iIi11i - I11i / iI11I1II1I1I / IIi - iIi1i1ii1 - I1ii11iIi11i
 if 76 - 76: Oooo0O0oo00oO . oOo0O0Ooo + Oooo0O0oo00oO + iI11I1II1I1I + iIi1i1ii1 / iI11I1II1I1I
def oO0O000O0o ( ) :
 try :
  IiiI1Ii1IIi = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IiiI1Ii1IIi ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iIi1IIiiiI = os . path . join ( IiiI1Ii1IIi , "source.db" )
    os . unlink ( iIi1IIiiiI )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 4 - 4: ooOoO0O00 % I11i % O0oOO0 . ooOoO0O00
 if 85 - 85: iIi1i1ii1 . IIi * I11i % I1ii11iIi11i % IIiIiII11i + OooOO000
 if 85 - 85: IIiIiII11i / OOoOoo * IIiIiII11i
 if 43 - 43: I11i / o0o00Oo0O + ooOoO0O00 - Ii1I % Ii
 if 69 - 69: Oooo0O0oo00oO % Ii1I / OOooOOo . Oooo0O0oo00oO - iIi1i1ii1
def O0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 74 - 74: oO0o - I11i - iIi1i1ii1 . o0o00Oo0O % OOoOoo
 if 32 - 32: OOooOOo . oO0o / I1ii11iIi11i . Ii
 if 9 - 9: oo0oO00 - IIiIiII11i + OooOO000 / O0oOO0 % Ii1I
 if 17 - 17: iI11I1II1I1I - OOoOoo
 if 99 - 99: I1ii11iIi11i + OooOO000 % OOoOoo - I11i
 if 52 - 52: Ii1I
 if 93 - 93: iiII11i1I1IIi . Ii
def oo00OO0000oO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; I1i1I = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if I1i1I :
  O0OOoooOooO0OOoOoOO00 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; O0OOoooOooO0OOoOoOO00 = xbmc . translatePath ( O0OOoooOooO0OOoOoOO00 ) ;
  o0O00 = os . path . join ( O0OOoooOooO0OOoOoOO00 , ".." , ".." ) ; o0O00 = os . path . abspath ( o0O00 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o0O00 ) ; ii1IiI111II = False
  try :
   for IiIIiii1I , i1II11II1 , II1IIIii in os . walk ( o0O00 , topdown = True ) :
    i1II11II1 [ : ] = [ OoOOoO0oOo for OoOOoO0oOo in i1II11II1 if OoOOoO0oOo not in o0oO0 ]
    for Oo0OO in II1IIIii :
     try : os . remove ( os . path . join ( IiIIiii1I , Oo0OO ) )
     except :
      if Oo0OO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : ii1IiI111II = True
      plugintools . log ( "Error removing " + IiIIiii1I + " " + Oo0OO )
    for Oo0OO in i1II11II1 :
     try : os . rmdir ( os . path . join ( IiIIiii1I , Oo0OO ) )
     except :
      if Oo0OO not in [ "Database" , "userdata" ] : ii1IiI111II = True
      plugintools . log ( "Error removing " + IiIIiii1I + " " + Oo0OO )
   if not ii1IiI111II : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oo0oO0o0 ( )
 if 8 - 8: Oooo0O0oo00oO
 if 44 - 44: oO0o % Ii . OooOO000 - o0o00Oo0O / iiII11i1I1IIi . OOoOoo
 if 23 - 23: I11i % iI11I1II1I1I
def O0OOo00OO ( ) :
 iIIiI1II = [ ]
 OoO0O0oo0 = sys . argv [ 2 ]
 if len ( OoO0O0oo0 ) >= 2 :
  I1II1 = sys . argv [ 2 ]
  iI1iIi1i11I1 = I1II1 . replace ( '?' , '' )
  if ( I1II1 [ len ( I1II1 ) - 1 ] == '/' ) :
   I1II1 = I1II1 [ 0 : len ( I1II1 ) - 2 ]
  Ooo0Oo00Ooo = iI1iIi1i11I1 . split ( '&' )
  iIIiI1II = { }
  for I1iIiIii in range ( len ( Ooo0Oo00Ooo ) ) :
   i1II1 = { }
   i1II1 = Ooo0Oo00Ooo [ I1iIiIii ] . split ( '=' )
   if ( len ( i1II1 ) ) == 2 :
    iIIiI1II [ i1II1 [ 0 ] ] = i1II1 [ 1 ]
    if 68 - 68: IIiIiII11i
 return iIIiI1II
 if 61 - 61: Oooo0O0oo00oO . Ii1I * O0oOO0 / OooOO000 - oO0o
iIII111i1ii1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
O0oO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii1i1i1I11i1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i1I1Iii1IiiIi = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1IiIi1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OoOo00ooOO000 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oOOO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iIOoO0O00o0ooo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1i1I1i1i1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOo0OoOOoO0Ooo0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0ii1I1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i11III = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
O00ooOooOOo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IiiII1iIi = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iIiI11I = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
ii1i111 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
Oo000 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0oOoooOoo0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iI1iIiiiI1I1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o000Oo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iIiiIi11IIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oOOooooo0OoO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OOoOooO0o = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O00Oooo00 = base64 . decodestring ( 'Q1VOVA==' )
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
 if 26 - 26: o0o00Oo0O * IIi - oOo0O0Ooo - iiII11i1I1IIi / iI11I1II1I1I
def o0OIiII ( name , url , mode , iconimage , fanart , description ) :
 i1i1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOoo000 = True
 OooOo00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OooOo00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OooOo00o . setProperty ( "Fanart_Image" , fanart )
 oOoo000 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = OooOo00o , isFolder = False )
 return oOoo000
 if 57 - 57: Ii1I - oO0o * iI11I1II1I1I
 if 26 - 26: oO0o % OOoOoo % I11i % OOooOOo . iiII11i1I1IIi % o0o00Oo0O
I1II1 = O0OOo00OO ( )
ooO0oOOooOo0 = None
Oo0OO = None
iiIi1iI1iIii = None
iIIiiI1II1i11 = None
iiI11ii1I1 = None
OOo = None
OoiIiiIi11 = None
o0o0oOOo = None
if 55 - 55: oO0o
if 20 - 20: OOoOoo * OooOO000 * I11i - OOoOoo
try :
 o0o0oOOo = int ( I1II1 [ "fav_mode" ] )
except :
 pass
 if 32 - 32: IIi * O0oOO0
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
 if 85 - 85: Ii . oO0o + oO0o
 if 28 - 28: I1ii11iIi11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( iiIi1iI1iIii )
print "URL: " + str ( ooO0oOOooOo0 )
print "Name: " + str ( Oo0OO )
print "IconImage: " + str ( iIIiiI1II1i11 )
if 62 - 62: I1ii11iIi11i + ii / iiII11i1I1IIi
if 60 - 60: IIi / OOooOOo . oo0oO00 % Oooo0O0oo00oO
def Iii1I1I11iiI1 ( content , viewType ) :
 if 61 - 61: o0o00Oo0O . IIi . o0o00Oo0O * Ii * IIiIiII11i / OooOO000
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 69 - 69: oo0oO00
if iIIiiI1II1i11 == None : iIIiiI1II1i11 = Ooo
if iiI11ii1I1 == None : iiI11ii1I1 = OO0o
if iiIi1iI1iIii == None :
 oo0OOo0 ( )
 if 17 - 17: oo0oO00
elif iiIi1iI1iIii == 1 :
 O0o0O ( ooO0oOOooOo0 )
 if 38 - 38: OooOO000 % Oooo0O0oo00oO
elif iiIi1iI1iIii == 44 :
 oooO ( ooO0oOOooOo0 )
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
elif iiIi1iI1iIii == 2 :
 Ii11Iii ( )
 if 44 - 44: Ii1I % iIi1i1ii1
elif iiIi1iI1iIii == 3 :
 o00ii111Iiii ( )
 if 6 - 6: oO0o
elif iiIi1iI1iIii == 21 :
 i1i1II ( )
 if 82 - 82: iI11I1II1I1I . oo0oO00 / iIi1i1ii1 / Oooo0O0oo00oO * IIiIiII11i % O0oOO0
elif iiIi1iI1iIii == 4 :
 oOoO0O00oo ( )
 if 62 - 62: IIiIiII11i
elif iiIi1iI1iIii == 5 :
 o0o0OO0o00o0O ( ooO0oOOooOo0 )
 if 96 - 96: oo0oO00 % OOooOOo * Ii1I
elif iiIi1iI1iIii == 6 :
 Iii1Ii ( ooO0oOOooOo0 )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . OOoOoo
elif iiIi1iI1iIii == 7 :
 OoOo0O0O ( ooO0oOOooOo0 , Oo0OO )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . iIi1i1ii1 * I11i + Oooo0O0oo00oO
elif iiIi1iI1iIii == 8 :
 OoOOOO0ooO0 ( ooO0oOOooOo0 , Oo0OO )
 if 77 - 77: I11i
elif iiIi1iI1iIii == 9 :
 FIXREPOSADDONS ( ooO0oOOooOo0 )
 if 63 - 63: OOoOoo * O0oOO0 + OOoOoo * IIi + I1ii11iIi11i / Ii1I
elif iiIi1iI1iIii == 10 :
 o00O0 ( )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
elif iiIi1iI1iIii == 11 :
 I11I1I111 ( ooO0oOOooOo0 )
 if 65 - 65: OooOO000 + o0o00Oo0O % I11i
elif iiIi1iI1iIii == 12 :
 ii11I11i ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 72 - 72: Oooo0O0oo00oO . OOooOOo / IIiIiII11i
elif iiIi1iI1iIii == 13 :
 oOOOO ( )
 if 69 - 69: Oooo0O0oo00oO * IIiIiII11i - OOoOoo - ooOoO0O00 + Ii
elif iiIi1iI1iIii == 14 :
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if 50 - 50: ii * ooOoO0O00 / O0oOO0
elif iiIi1iI1iIii == 15 :
 oo0 ( )
 if 83 - 83: ooOoO0O00
elif iiIi1iI1iIii == 16 :
 iI11i1iI ( ooO0oOOooOo0 , Oo0OO )
 if 38 - 38: ii * iI11I1II1I1I
elif iiIi1iI1iIii == 17 :
 i1iOOIiIII1i ( ooO0oOOooOo0 , Oo0OO )
 if 54 - 54: ii . OooOO000
elif iiIi1iI1iIii == 18 :
 oO0O000O0o ( )
 if 71 - 71: IIi
elif iiIi1iI1iIii == 19 :
 IiI1 ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 . Ii . oO0o * I1ii11iIi11i % IIi . I11i
elif iiIi1iI1iIii == 40 :
 ii1IIIIiI11I ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
elif iiIi1iI1iIii == 42 :
 o0OO0OOO0O ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 93 - 93: OOoOoo % OooOO000
elif iiIi1iI1iIii == 43 :
 ii1IIi1ii ( ooO0oOOooOo0 )
 if 46 - 46: Ii1I * OOooOOo * iIi1i1ii1 * Ii1I . Ii1I
elif iiIi1iI1iIii == 20 :
 i1i1 ( ooO0oOOooOo0 )
 if 43 - 43: OOoOoo . ooOoO0O00
elif iiIi1iI1iIii == 22 :
 O0O0oOo0o0o0 ( ooO0oOOooOo0 )
 if 68 - 68: iIi1i1ii1 % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
elif iiIi1iI1iIii == 23 :
 I1IiIi11 ( ooO0oOOooOo0 )
 if 45 - 45: oOo0O0Ooo
elif iiIi1iI1iIii == 24 :
 I11IiiI1 ( ooO0oOOooOo0 )
 if 17 - 17: ii - OOoOoo + IIi . ii % I1ii11iIi11i
elif iiIi1iI1iIii == 25 :
 O0OoO0oo0Oo00oOOO0o ( ooO0oOOooOo0 )
 if 92 - 92: OooOO000 - Oooo0O0oo00oO % oO0o - I11i % ooOoO0O00
elif iiIi1iI1iIii == 26 :
 IIii1I1IIii ( ooO0oOOooOo0 )
 if 38 - 38: Ii1I . oo0oO00 / OOooOOo % oo0oO00
elif iiIi1iI1iIii == 27 :
 i11IiIi1i ( ooO0oOOooOo0 )
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / iiII11i1I1IIi
elif iiIi1iI1iIii == 28 :
 OO00oOO ( ooO0oOOooOo0 )
 if 61 - 61: I1ii11iIi11i - OooOO000
elif iiIi1iI1iIii == 29 :
 iiiiIiiiii1I ( ooO0oOOooOo0 )
 if 51 - 51: iiII11i1I1IIi * OOoOoo / o0o00Oo0O / o0o00Oo0O
elif iiIi1iI1iIii == 30 :
 OOoooOoO0Oo ( ooO0oOOooOo0 )
 if 52 - 52: ii % o0o00Oo0O
elif iiIi1iI1iIii == 31 :
 O0O0OOo ( ooO0oOOooOo0 )
 if 56 - 56: O0oOO0 - ooOoO0O00 * ii - IIiIiII11i
elif iiIi1iI1iIii == 32 :
 OoOoO ( )
 if 28 - 28: ooOoO0O00 / oo0oO00 . I11i
elif iiIi1iI1iIii == 33 :
 oo0i1iIIi1II1iiI ( )
 if 11 - 11: I1ii11iIi11i * ii - Ii
elif iiIi1iI1iIii == 35 :
 O0O00OooO ( ooO0oOOooOo0 )
 if 13 - 13: Ii . o0o00Oo0O / Oooo0O0oo00oO * ooOoO0O00
elif iiIi1iI1iIii == 34 :
 III1Ii1i1I1 ( ooO0oOOooOo0 )
 if 14 - 14: iIi1i1ii1 + iIi1i1ii1 . oo0oO00 / IIi . iI11I1II1I1I
elif iiIi1iI1iIii == 36 :
 O00OO ( ooO0oOOooOo0 )
 if 10 - 10: IIiIiII11i . Oooo0O0oo00oO / iiII11i1I1IIi
elif iiIi1iI1iIii == 37 :
 OO0 ( ooO0oOOooOo0 )
 if 35 - 35: iiII11i1I1IIi / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif iiIi1iI1iIii == 38 :
 ooo0oo00O00oO ( ooO0oOOooOo0 )
 if 3 - 3: Ii1I
elif iiIi1iI1iIii == 41 :
 oo00OO0000oO ( I1II1 )
 if 42 - 42: oo0oO00 % I1ii11iIi11i + iIi1i1ii1 - oo0oO00 . iI11I1II1I1I - IIi
elif iiIi1iI1iIii == 39 :
 Ii1I1i ( ooO0oOOooOo0 )
 if 27 - 27: iiII11i1I1IIi % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif iiIi1iI1iIii == 45 :
 TEXTS ( )
 if 37 - 37: iiII11i1I1IIi + OooOO000 * IIi + iIi1i1ii1
elif iiIi1iI1iIii == 46 :
 OOI1iI1ii1II ( )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + IIi / IIiIiII11i
elif iiIi1iI1iIii == 47 :
 GEVID ( )
 if 66 - 66: OOoOoo + O0oOO0 % ii
elif iiIi1iI1iIii == 48 :
 o0OOOOO0 ( Oo0OO , ooO0oOOooOo0 , OOo )
 if 23 - 23: O0oOO0 . OOooOOo + iI11I1II1I1I
elif iiIi1iI1iIii == 49 :
 IIo0Oo0oO0oOO00 ( )
 if 17 - 17: iIi1i1ii1
elif iiIi1iI1iIii == 222 :
 o00o ( ooO0oOOooOo0 )
 if 12 - 12: ooOoO0O00 . oO0o
elif iiIi1iI1iIii == 333 :
 OOO00OOOO0o ( ooO0oOOooOo0 )
 if 14 - 14: Oooo0O0oo00oO + IIiIiII11i % Oooo0O0oo00oO . O0oOO0 * OOoOoo
 if 54 - 54: OOoOoo * oo0oO00 - OooOO000
elif iiIi1iI1iIii == 1020 :
 I1Iii1 ( )
 if 15 - 15: iiII11i1I1IIi / o0o00Oo0O
elif iiIi1iI1iIii == 1021 :
 ANIMEEP ( )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + OOoOoo . OooOO000 * OOoOoo
elif iiIi1iI1iIii == 1022 :
 ANIMEPLAY ( ooO0oOOooOo0 )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif iiIi1iI1iIii == 1001 :
 iiiI1I ( )
 if 82 - 82: o0o00Oo0O / iiII11i1I1IIi * oO0o - oo0oO00 + I1ii11iIi11i
elif iiIi1iI1iIii == 1005 :
 OOo0o ( )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + IIi * IIiIiII11i
elif iiIi1iI1iIii == 1007 :
 o000 ( ooO0oOOooOo0 )
 if 78 - 78: OooOO000 - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif iiIi1iI1iIii == 1010 :
 oo0O ( ooO0oOOooOo0 )
 if 97 - 97: ooOoO0O00
elif iiIi1iI1iIii == 1011 :
 i1IiiI1i11 ( ooO0oOOooOo0 )
 if 29 - 29: oOo0O0Ooo
elif iiIi1iI1iIii == 1012 :
 O000oOo ( ooO0oOOooOo0 )
 if 37 - 37: Ii1I * OooOO000 * oOo0O0Ooo * o0o00Oo0O
elif iiIi1iI1iIii == 1030 :
 OO0OoO0OOoOo ( )
 if 35 - 35: oOo0O0Ooo - Ii1I * iiII11i1I1IIi + iIi1i1ii1 / ooOoO0O00
elif iiIi1iI1iIii == 1031 :
 oO000 ( ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 46 - 46: I1ii11iIi11i . OOoOoo % I1ii11iIi11i / IIiIiII11i * OOoOoo * Oooo0O0oo00oO
elif iiIi1iI1iIii == 1032 :
 Oo00OO0 ( ooO0oOOooOo0 )
 if 59 - 59: OooOO000 * iiII11i1I1IIi
elif iiIi1iI1iIii == 1006 :
 Parse . ParseURL ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 / o0o00Oo0O
elif iiIi1iI1iIii == 2030 :
 Parse . addonParseURL ( ooO0oOOooOo0 )
 if 57 - 57: ooOoO0O00 % OOoOoo
elif iiIi1iI1iIii == 2031 :
 Parse . apkParseURL ( ooO0oOOooOo0 )
 if 69 - 69: I11i
elif iiIi1iI1iIii == 1002 :
 IiiiiI ( ooO0oOOooOo0 )
 if 69 - 69: OooOO000
elif iiIi1iI1iIii == 1003 :
 OOOoOOooOoo ( ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 83 - 83: iI11I1II1I1I . I11i + OooOO000 . ii / OOoOoo + IIiIiII11i
elif iiIi1iI1iIii == 1004 :
 O00OO0oOOO ( ooO0oOOooOo0 )
 if 90 - 90: IIi * iiII11i1I1IIi / Oooo0O0oo00oO
elif iiIi1iI1iIii == 1008 :
 iIiI1I1II1 ( )
 if 68 - 68: OOooOOo
elif iiIi1iI1iIii == 1009 :
 IIoooOoOO0o ( ooO0oOOooOo0 )
 if 65 - 65: O0oOO0
elif iiIi1iI1iIii == 2001 :
 o00OooooOOOO ( )
 if 82 - 82: I11i
elif iiIi1iI1iIii == 2002 :
 ooooOOo ( ooO0oOOooOo0 )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + OooOO000
elif iiIi1iI1iIii == 1013 :
 iIIiI1iiI ( )
elif iiIi1iI1iIii == 10111113 :
 i1i ( ooO0oOOooOo0 )
 if 65 - 65: IIi
elif iiIi1iI1iIii == 1014 :
 I1I11 ( )
 if 71 - 71: OooOO000 % OooOO000 . O0oOO0 + Ii - Ii
elif iiIi1iI1iIii == 1015 :
 i1iiiiIIIi ( ooO0oOOooOo0 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / OooOO000 - Ii . OOoOoo / Oooo0O0oo00oO
elif iiIi1iI1iIii == 1016 :
 I11IIIi ( ooO0oOOooOo0 , iIIiiI1II1i11 , Oo0OO )
 if 13 - 13: I11i % o0o00Oo0O - OooOO000 * ii / I1ii11iIi11i - ii
elif iiIi1iI1iIii == 1017 :
 iI1I ( )
 if 78 - 78: O0oOO0 % ii
elif iiIi1iI1iIii == 1018 :
 Oo0 ( ooO0oOOooOo0 )
 if 73 - 73: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + ooOoO0O00 - ii / O0oOO0
elif iiIi1iI1iIii == 1023 :
 OooOoOo ( )
 if 78 - 78: ii % O0oOO0 - Ii
elif iiIi1iI1iIii == 1024 :
 II1iiII1 ( ooO0oOOooOo0 )
 if 37 - 37: iIi1i1ii1 % IIi % ooOoO0O00
elif iiIi1iI1iIii == 1025 :
 I1IiiIIiIii1i ( ooO0oOOooOo0 )
 if 23 - 23: OOoOoo - o0o00Oo0O + Ii
elif iiIi1iI1iIii == 4001 :
 Ooo0OOoOoO0 ( )
 if 98 - 98: ii
elif iiIi1iI1iIii == 4002 :
 o00Oo0oooooo ( )
 if 61 - 61: I11i . iIi1i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
elif iiIi1iI1iIii == 4003 :
 Oo0O0Oo00O ( )
 if 65 - 65: ooOoO0O00 * Oooo0O0oo00oO * ii - iIi1i1ii1 . iiII11i1I1IIi - oO0o
elif iiIi1iI1iIii == 4004 :
 iI1i111I1Ii ( )
 if 71 - 71: IIi * OOooOOo
elif iiIi1iI1iIii == 4005 :
 i11i1ii1I ( )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % OooOO000 * I11i
elif iiIi1iI1iIii == 4006 :
 o0OOOo ( )
 if 64 - 64: OOoOoo / OOoOoo + Ii1I * Oooo0O0oo00oO % Oooo0O0oo00oO
elif iiIi1iI1iIii == 4007 :
 oOo0 ( )
 if 87 - 87: oO0o * I1ii11iIi11i
elif iiIi1iI1iIii == 4008 :
 o0o0 ( )
 if 83 - 83: ooOoO0O00 * OooOO000 - iIi1i1ii1 / IIi
elif iiIi1iI1iIii == 4009 : ooo ( )
elif iiIi1iI1iIii == 4010 : IiiIi1IIII1i ( )
elif iiIi1iI1iIii == 3000 :
 OOOOO0oOOoO ( )
 if 48 - 48: O0oOO0 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif iiIi1iI1iIii == 3001 :
 I11i1i11IiIi1 ( )
 if 32 - 32: IIi * oOo0O0Ooo - Oooo0O0oo00oO . I1ii11iIi11i / o0o00Oo0O + IIi
elif iiIi1iI1iIii == 3002 :
 I11i1I1Ii ( ooO0oOOooOo0 )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif iiIi1iI1iIii == 3003 :
 iii11 ( ooO0oOOooOo0 )
 if 7 - 7: Ii % Ii1I / OooOO000 % I1ii11iIi11i - oO0o
elif iiIi1iI1iIii == 3004 :
 III1IIIIIiiI ( ooO0oOOooOo0 )
 if 73 - 73: Ii1I
elif iiIi1iI1iIii == 404 :
 ii1II11IIII ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 )
 if 92 - 92: Ii + o0o00Oo0O * oo0oO00
elif iiIi1iI1iIii == 405 :
 O0ooO ( ooO0oOOooOo0 )
 if 60 - 60: I11i / I1ii11iIi11i
elif iiIi1iI1iIii == 7030 :
 I1Ii111I111 ( )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif iiIi1iI1iIii == 7021 :
 iiiI1I1iiiII ( Oo0OO )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % OooOO000 / Ii1I
elif iiIi1iI1iIii == 7022 :
 Ii1Iii1 ( Oo0OO )
 if 76 - 76: oO0o * O0oOO0 - oO0o
elif iiIi1iI1iIii == 7000 :
 OO0ooo0OOO ( Oo0OO , ooO0oOOooOo0 , img )
 if 57 - 57: ii / OOooOOo + O0oOO0 . IIi
elif iiIi1iI1iIii == 7050 :
 I11Ii111I ( ooO0oOOooOo0 )
 if 14 - 14: Ii % Oooo0O0oo00oO * I11i * OOooOOo
elif iiIi1iI1iIii == 7051 :
 O0OOoooO ( ooO0oOOooOo0 )
 if 55 - 55: OooOO000 * Oooo0O0oo00oO * OooOO000
elif iiIi1iI1iIii == 7052 :
 ooOoo000 ( ooO0oOOooOo0 )
 if 70 - 70: o0o00Oo0O . IIi
elif iiIi1iI1iIii == 7053 :
 o0Oii11iIIiIi1 ( ooO0oOOooOo0 )
 if 33 - 33: Oooo0O0oo00oO * IIi
elif iiIi1iI1iIii == 7054 :
 CoolPlay ( ooO0oOOooOo0 )
 if 64 - 64: Ii . iI11I1II1I1I
elif iiIi1iI1iIii == 7060 :
 IiIi1I11 ( )
 if 7 - 7: OOooOOo % OOoOoo + OOooOOo - OOooOOo * Ii % oO0o
elif iiIi1iI1iIii == 7061 :
 oO00Oooo0O0o0 ( ooO0oOOooOo0 )
 if 57 - 57: Oooo0O0oo00oO / oO0o + Ii1I
elif iiIi1iI1iIii == 7063 :
 IiI1O000oo0o ( ooO0oOOooOo0 )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % Oooo0O0oo00oO + iIi1i1ii1 . oO0o . I1ii11iIi11i
elif iiIi1iI1iIii == 7062 :
 ooO0OO0Oooo0o ( ooO0oOOooOo0 )
 if 70 - 70: oo0oO00 . Ii1I * O0oOO0
elif iiIi1iI1iIii == 7064 :
 NATatozcat ( )
 if 97 - 97: O0oOO0 . iI11I1II1I1I - Oooo0O0oo00oO
elif iiIi1iI1iIii == 7067 :
 OOoO00o000 ( ooO0oOOooOo0 )
 if 23 - 23: Ii1I % oo0oO00
elif iiIi1iI1iIii == 7066 :
 NATatozA ( ooO0oOOooOo0 )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif iiIi1iI1iIii == 7065 :
 iIi1Iii11111I1iii ( ooO0oOOooOo0 )
 if 99 - 99: OooOO000 - Ii1I - oOo0O0Ooo - OooOO000 + oO0o + IIiIiII11i
elif iiIi1iI1iIii == 7070 :
 IIiIi1II1IiI ( )
 if 34 - 34: OooOO000 * oo0oO00
elif iiIi1iI1iIii == 7071 :
 DIZIlist ( ooO0oOOooOo0 )
 if 31 - 31: iIi1i1ii1 . O0oOO0
elif iiIi1iI1iIii == 7072 :
 DIZIpull ( ooO0oOOooOo0 )
 if 40 - 40: IIi - oo0oO00 / IIiIiII11i * ooOoO0O00 + iIi1i1ii1 * IIiIiII11i
elif iiIi1iI1iIii == 7073 :
 WATCHDIZI ( ooO0oOOooOo0 )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - OooOO000
elif iiIi1iI1iIii == 7002 :
 OoOo0Oooo0o ( )
 if 99 - 99: IIi - iIi1i1ii1 - ooOoO0O00 / Ii . iIi1i1ii1
elif iiIi1iI1iIii == 7003 :
 oO0OO0O ( ooO0oOOooOo0 )
 if 58 - 58: Oooo0O0oo00oO
elif iiIi1iI1iIii == 7004 :
 i1Ii1I ( ooO0oOOooOo0 )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif iiIi1iI1iIii == 7020 :
 ooOOoO00o0o0oo0o ( ooO0oOOooOo0 )
 if 64 - 64: OOooOOo + iIi1i1ii1 - ooOoO0O00 . IIiIiII11i . oO0o
elif iiIi1iI1iIii == 7001 :
 IIIIiIiIi1 ( )
 if 31 - 31: O0oOO0 . iiII11i1I1IIi - oo0oO00 . iI11I1II1I1I + oo0oO00 . OOooOOo
elif iiIi1iI1iIii == 7010 :
 i11IiIiii ( ooO0oOOooOo0 )
 if 86 - 86: Ii1I - Ii1I / iiII11i1I1IIi - Ii1I * iiII11i1I1IIi + OooOO000
elif iiIi1iI1iIii == 7011 :
 I1iiIIii ( ooO0oOOooOo0 )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - iIi1i1ii1
elif iiIi1iI1iIii == 7012 :
 II1111iiI1II ( ooO0oOOooOo0 )
 if 30 - 30: ii % Oooo0O0oo00oO
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
 iiii1ii1 ( )
elif iiIi1iI1iIii == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooO0oOOooOo0 )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - Oooo0O0oo00oO
elif iiIi1iI1iIii == 8000 :
 i1111ii1I ( )
elif iiIi1iI1iIii == 8001 :
 i1iI11ii ( )
elif iiIi1iI1iIii == 8002 :
 oO000O ( )
elif iiIi1iI1iIii == 8003 :
 OooO00O0OO0oo ( )
elif iiIi1iI1iIii == 8004 :
 O00oOo0o0 ( )
elif iiIi1iI1iIii == 8005 :
 OO00o ( )
elif iiIi1iI1iIii == 8006 :
 O0OO0OOoOO ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8030 :
 O0Oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8045 :
 iIIO0ooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8046 :
 II1ii1iii1ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8047 :
 o00O0o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8048 :
 iIiI1I1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8049 :
 oOoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 804900 :
 oOOo00Ooo0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8020 :
 OOOOoO00o0O ( )
elif iiIi1iI1iIii == 8021 :
 i1II1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8022 :
 O0oooooO0oOOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8023 :
 oo0O0OO0Oooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8040 :
 I1iI ( )
elif iiIi1iI1iIii == 8041 :
 O00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8042 :
 iIIII1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8043 :
 yt . PlayVideo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8044 :
 Oooo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8060 :
 IiI11ii1I ( )
elif iiIi1iI1iIii == 8061 :
 II1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8064 :
 I1I1I1IIi1III ( )
elif iiIi1iI1iIii == 8065 :
 iiI11I1ii11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8070 :
 iIIi11ii ( )
elif iiIi1iI1iIii == 8071 :
 O000Oo00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7080 :
 iI1oOoo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8090 :
 IiIII ( )
elif iiIi1iI1iIii == 8091 :
 i1IIiiIIIIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8092 :
 o0OoOo0O00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8093 :
 IiIIIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8081 :
 oO0o00o000Oo0 ( )
elif iiIi1iI1iIii == 8062 :
 o0ooo0oooO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8063 :
 IIOoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8050 :
 I11111iI1i111 ( )
elif iiIi1iI1iIii == 8051 :
 i111 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8052 :
 III11i1iIIiiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8085 :
 iIiiI111I11 ( )
elif iiIi1iI1iIii == 8086 :
 IIIiiiI1Ii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8087 :
 oOoOO0O00o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 8088 :
 o0OOOO ( ooO0oOOooOo0 , Oo0OO )
elif iiIi1iI1iIii == 9000 :
 I1iIiI1IiIIII ( )
elif iiIi1iI1iIii == 1111 :
 oO00OoOOOo ( )
elif iiIi1iI1iIii == 9001 :
 Ooo00Oo ( )
elif iiIi1iI1iIii == 9002 :
 o00o0 ( )
elif iiIi1iI1iIii == 9003 :
 ooOo0 ( )
elif iiIi1iI1iIii == 9004 :
 World1 ( )
elif iiIi1iI1iIii == 9005 :
 World2 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9006 :
 World3 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9007 :
 IIi1iiIIi1i ( )
elif iiIi1iI1iIii == 9008 :
 ii1IIi1I11IiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9009 :
 oOO0ooO00o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9010 :
 iIIIii111 ( )
elif iiIi1iI1iIii == 9011 :
 I1111IiII1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 50 :
 I111i1Ii1i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9020 :
 champlist ( )
elif iiIi1iI1iIii == 9021 :
 iiI1 ( )
elif iiIi1iI1iIii == 9022 :
 OoIII ( )
elif iiIi1iI1iIii == 9023 :
 OO00O ( )
elif iiIi1iI1iIii == 9024 :
 II1Iii1I1II1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9030 :
 I1Ii11iI11ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9031 :
 oOo0ii1II ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9032 :
 OOo00o0o0O0oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9033 :
 i1iI1iIII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 9034 :
 I11iiiiI1i ( )
elif iiIi1iI1iIii == 7085 :
 iIiii1IIi1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7086 :
 IiI1I1i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 7087 :
 ii1O0oOOo ( OOo )
elif iiIi1iI1iIii == 9666 :
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10100 : O0ooo ( )
elif iiIi1iI1iIii == 101001 : IiI111 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10105 : Oooo0o0oO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10106 : o0OOoOooO0ooO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10104 : ii11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10107 : OO0OO00ooO0 ( )
elif iiIi1iI1iIii == 10103 : IiiiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10108 : iiIIIII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10000 : Origin_Menu ( )
elif iiIi1iI1iIii == 10001 : I1iIII1 ( )
elif iiIi1iI1iIii == 10002 : o0OO0o0o00o ( )
elif iiIi1iI1iIii == 10003 : IIii1111 ( )
elif iiIi1iI1iIii == 10004 : oOo0OoOOo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10005 : Ooo0oo ( )
elif iiIi1iI1iIii == 10006 : o0OOOOOo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10007 : i1iI1Iiii1I ( ooO0oOOooOo0 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 10008 : iIIi ( )
elif iiIi1iI1iIii == 10009 : iiIIiIi ( )
elif iiIi1iI1iIii == 10010 : o0Oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10011 : ooo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10012 : I1I1iI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10109 : oO0OooO00Oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10013 : iiI111i1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10014 : iiI1iI ( )
elif iiIi1iI1iIii == 10015 : i1iOO ( )
elif iiIi1iI1iIii == 10016 : OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10017 : I1I1IIiiii1ii ( )
elif iiIi1iI1iIii == 10018 : IIII1ii1 ( )
elif iiIi1iI1iIii == 10019 : oO0OoiIi111iII1 ( )
elif iiIi1iI1iIii == 10020 : o0o ( )
elif iiIi1iI1iIii == 10021 : II11II1I ( )
elif iiIi1iI1iIii == 10022 : iI1iIIIIIiIi1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10023 : IiiI ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10024 : ooO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10025 : ii1II ( )
elif iiIi1iI1iIii == 10026 : IIiiI ( )
elif iiIi1iI1iIii == 10027 : O0ooooooo00 ( )
elif iiIi1iI1iIii == 10028 : IioOooOOo00ooO ( )
elif iiIi1iI1iIii == 10029 : iIi11I11 ( )
elif iiIi1iI1iIii == 423 : iIIiiiI1iI1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 426 : oOoOo0o00o ( ooO0oOOooOo0 )
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
elif iiIi1iI1iIii == 10041 : IIOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10042 : iiIiI11IiI1ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10043 : oooO0o0oOoO ( )
elif iiIi1iI1iIii == 10044 : o0Ii11iIiiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10045 : OoOO00oo0o ( Oo0OO )
elif iiIi1iI1iIii == 10046 : oO0OoOOOO0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10047 : O0OOO0ooO00o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10048 : ooOoo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10049 : iIiO0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10050 : OO ( )
elif iiIi1iI1iIii == 10051 : IiiII1I ( )
elif iiIi1iI1iIii == 10052 : iI1iI1iIi1ii1I1 ( )
elif iiIi1iI1iIii == 10053 : Addon ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10054 : Iii1I ( ooO0oOOooOo0 , Oo0OO )
elif iiIi1iI1iIii == 10055 :
 i1Ii11ii1I ( "addFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii1III1iiIi ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 , o0o0oOOo )
elif iiIi1iI1iIii == 10056 :
 i1Ii11ii1I ( "rmFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiI11Ii1i ( Oo0OO )
elif iiIi1iI1iIii == 10057 :
 i1Ii11ii1I ( "getFavorites" )
 o0OOOOOo00 ( )
elif iiIi1iI1iIii == 10058 : iiI ( )
elif iiIi1iI1iIii == 10059 : Donators_Guide ( )
elif iiIi1iI1iIii == 10060 : oOo0OOoO0 ( )
elif iiIi1iI1iIii == 10061 : iIIi1iI1I1IIi ( )
elif iiIi1iI1iIii == 10062 : o00oo0000 ( Oo0OO , ooO0oOOooOo0 , OOo )
elif iiIi1iI1iIii == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif iiIi1iI1iIii == 10064 : O0O00OOo ( )
elif iiIi1iI1iIii == 10065 : i1I1iIi1IiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10066 : i1I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10068 : o0OO0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10069 : II11IiiIII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10070 : ii1I11iIiIII1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10071 : Genie_Watch ( )
elif iiIi1iI1iIii == 10072 : IIIiIi ( )
elif iiIi1iI1iIii == 10073 : i1I1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10074 : Iii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10075 : Oo00OOOOoo0oo ( iIIiiI1II1i11 , Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10076 : oooOO0OO0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10077 : OOoO000O00oO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10078 : IiiiI ( )
elif iiIi1iI1iIii == 10079 : Genie_Watch_Tv_Shows ( )
elif iiIi1iI1iIii == 10080 : Genie_Watch_Tv_Genre ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10081 : Genie_Watch_TV_PlayRun ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10082 : Genie_Watch_TV_Episodes ( ooO0oOOooOo0 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 10083 : Genie_Watch_Tv_Recent ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 10084 : oOoO0 ( )
elif iiIi1iI1iIii == 10085 : OOoO00 ( )
elif iiIi1iI1iIii == 10086 : i1IiiiI1iI ( )
elif iiIi1iI1iIii == 20000 : iIii ( )
elif iiIi1iI1iIii == 20001 : OOooO0Oo00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20002 : iIIIIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20003 : ii11iiI11I ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20004 : iiIi11i1IiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 20005 : OOOOO0o0OOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21004 : IIi11IIiIii1 ( )
elif iiIi1iI1iIii == 21005 : IIiii11ii1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21006 : Ii11iiI1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 21007 : I1ii1Ii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30000 : Oo0o0OOOOO0O ( )
elif iiIi1iI1iIii == 30001 : O0o00oo0OO0 ( )
elif iiIi1iI1iIii == 10012 : Resolve ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30003 : Oo0O0000Oo00o ( )
elif iiIi1iI1iIii == 30004 : iI111II1ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30005 : IiIIi1II1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30006 : i1I1Ii11i ( )
elif iiIi1iI1iIii == 30007 : OOO0O00Oo ( )
elif iiIi1iI1iIii == 30008 : O0OoO0o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30009 : oo00o0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30010 : IiI1Iii1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30011 : ooI111iiiii1 ( )
elif iiIi1iI1iIii == 30012 : o00ooOoo ( )
elif iiIi1iI1iIii == 30013 : o0oO0OO00oo0o ( )
elif iiIi1iI1iIii == 30014 : Ooo0OOO ( )
elif iiIi1iI1iIii == 30015 : I1iiI1II ( ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 )
elif iiIi1iI1iIii == 30016 : Oo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30019 : IiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30017 : iiiii11I1 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30018 : IiIIiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30030 : iIiIIi11iI ( )
elif iiIi1iI1iIii == 30031 : iiIIi ( )
elif iiIi1iI1iIii == 30032 : OOOoOO ( )
elif iiIi1iI1iIii == 30033 : ooo00o0o ( )
elif iiIi1iI1iIii == 30034 : OOOO00o000o ( )
elif iiIi1iI1iIii == 30035 : o0ooO0OoOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30036 : o0oOO00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30037 : ii11iiIi ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 30038 : ooo00OoOO0o ( )
elif iiIi1iI1iIii == 30039 : oO0O0OO0O ( )
elif iiIi1iI1iIii == 50000 : oOO0O00Oo0O0o ( )
elif iiIi1iI1iIii == 50001 : O000oO0O ( )
elif iiIi1iI1iIii == 50002 : oooOO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 50003 : iI1iiIiI ( OOo )
elif iiIi1iI1iIii == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif iiIi1iI1iIii == 60001 : iIIi1I1ii ( )
elif iiIi1iI1iIii == 60002 : oO0oooooo ( Oo0OO )
elif iiIi1iI1iIii == 60003 : ooO00O00oOO ( Oo0OO )
elif iiIi1iI1iIii == 50004 : iI1111iiii ( )
elif iiIi1iI1iIii == 50005 : speedtest . runtest ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70001 : iIoo0ooooO ( )
elif iiIi1iI1iIii == 70002 : i1I111i1ii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70003 : oO0oOoo0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70004 : II1iI11 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70005 : O00o0O ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 70006 : O00oOo0O0o00O ( )
elif iiIi1iI1iIii == 50006 : OOOiiiiI ( i1 , i1111 )
elif iiIi1iI1iIii == 80000 : oo0oO0o0 ( )
elif iiIi1iI1iIii == 80001 : resolvefilmon ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80002 : i11i11 ( )
elif iiIi1iI1iIii == 80003 : O0OOO ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80004 : Ii1iiIi1I11i ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80005 : II1iI1I11I ( )
elif iiIi1iI1iIii == 80006 : i11i1iIiii ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80007 : OOO00OO0oOo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80008 : I1iIi1iiIIiI ( )
elif iiIi1iI1iIii == 80009 : iIIII11i ( )
elif iiIi1iI1iIii == 80010 : oOo0OOoo0o ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80011 : IiiI1iii1iIiiI ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 80012 : IiiIiiIIII ( )
elif iiIi1iI1iIii == 90000 : Oo00oo ( Oo0OO , ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90001 : I1I1i1I ( )
elif iiIi1iI1iIii == 90002 : i1OOO0000oO ( )
elif iiIi1iI1iIii == 90003 : oO0o00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90004 : Oo0OOOO0oOoo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90005 : O0OIIII1i ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90006 : O000oooO0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90007 : oOO00 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90008 : ii1I1ii1iII ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90009 : iII1ii11III ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 90010 : oooOo0OOOoo0 ( )
if 81 - 81: iiII11i1I1IIi % IIi . OOoOoo
if 66 - 66: Ii1I * IIi / ii * o0o00Oo0O % Oooo0O0oo00oO
elif iiIi1iI1iIii == 100001 : Stand_up ( )
if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * IIi / OooOO000 * ii
elif iiIi1iI1iIii == 100003 : OoO ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100004 : O00OoOO0oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100005 : Resolve ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100008 : Search ( )
elif iiIi1iI1iIii == 100007 : OO0oOOoo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100009 : yt . PlayVideo ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100010 : oOOO0oo0 ( ooO0oOOooOo0 )
elif iiIi1iI1iIii == 100100 : IiiIiI111iI ( iIIiiI1II1i11 , ooO0oOOooOo0 , OoiIiiIi11 )
elif iiIi1iI1iIii == 100101 : O0iII1 ( ooO0oOOooOo0 , Oo0OO , iiI11ii1I1 , OoiIiiIi11 , iIIiiI1II1i11 )
elif iiIi1iI1iIii == 100102 : oOOoo ( Oo0OO , ooO0oOOooOo0 , iIIiiI1II1i11 , iiI11ii1I1 )
elif iiIi1iI1iIii == 100106 : O0oOo00o0o00O ( ooO0oOOooOo0 , Oo0OO )
if 82 - 82: I1ii11iIi11i / IIi / IIi % IIi
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
