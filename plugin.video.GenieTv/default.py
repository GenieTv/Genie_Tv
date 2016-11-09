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
IiiIII111iI = "3.2.5"
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
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , OO0o , '' )
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
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , OO0o , '' )
  if 62 - 62: ii . oo0oO00
  if 61 - 61: OOooOOo - Oooo0O0oo00oO - ooOoO0O00
  if 25 - 25: o0o00Oo0O * oo0oO00 + Ii1I . I11i . I11i
  if 58 - 58: oOo0O0Ooo
  if 53 - 53: ooOoO0O00
  if 59 - 59: I11i
  if 81 - 81: OOooOOo - OOooOOo . iiII11i1I1IIi
  if 73 - 73: oo0oO00 % Ii - oOo0O0Ooo
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , OO0o , '' )
  if 7 - 7: o0o00Oo0O * Ii * IIi + OOoOoo % oO0o - OOoOoo
  if 39 - 39: I1ii11iIi11i * Oooo0O0oo00oO % Oooo0O0oo00oO - ii + I11i - oo0oO00
  if 23 - 23: Ii
  if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + oo0oO00 * iI11I1II1I1I
  if 81 - 81: iIi1i1ii1 % ooOoO0O00 . iI11I1II1I1I
  if 4 - 4: Ii % oO0o % ooOoO0O00 / iIi1i1ii1
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I11iI ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  ooOoo ( )
 if O0oO0 == 1 :
  I1III1111iIi ( )
 if O0oO0 == 2 :
  I1i111I ( )
 if O0oO0 == 3 :
  OooOo0oo0O0o00O ( )
 if O0oO0 == 4 :
  I1i11 ( )
 if O0oO0 == 5 :
  IiIi1I1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , IiIIi1 , Oo0OO )
 if O0oO0 == 6 :
  IIIIiii1IIii ( )
 if O0oO0 == 7 :
  II1i11I ( )
 if O0oO0 == 8 :
  ii1I1IIii11 ( )
 if O0oO0 == 9 :
  O0o0oO ( )
 if O0oO0 == 10 :
  IIIIiIiIi1 ( )
  if 2 - 2: iiII11i1I1IIi % iI11I1II1I1I * iI11I1II1I1I . I11i / iiII11i1I1IIi
  if 27 - 27: oO0o + OOoOoo - ooOoO0O00
def I11IiI ( ) :
 if not os . path . exists ( o0 ) :
  OOOiiiiI ( 'Change Log 9/11/16 - v3.2.5' , 'Freeview section added to streams 30+ channels, search series fixed, more movies and music added.' )
  os . makedirs ( o0 )
  if 69 - 69: iIi1i1ii1 - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
  if 79 - 79: o0o00Oo0O * Ii - iIi1i1ii1 / iIi1i1ii1
def ooOoo ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   i1O0 ( )
  if O0oO0 == 1 :
   I11Iiii1I ( ooO0oOOooOo0 )
  if O0oO0 == 2 :
   oo00O0oO0O0 ( )
  if O0oO0 == 3 :
   ooo0OO0O0Oo ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0oO0 == 4 :
   Ooo0O0oooo ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def iiI ( ) :
 Oo00oo0oO ( )
 oOIIiIi ( )
 if 91 - 91: Ii1I * I1ii11iIi11i / oOo0O0Ooo . o0o00Oo0O + oO0o + OOooOOo
 if 8 - 8: O0oOO0 / Ii1I
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , OO0o , '' )
def IIIIiIiIi1 ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , Ooo , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Ooo , OO0o , '' )
 if 20 - 20: oOo0O0Ooo
 if 95 - 95: iiII11i1I1IIi - oOo0O0Ooo
 if 34 - 34: OOoOoo * oOo0O0Ooo . ooOoO0O00 * OOoOoo / OOoOoo
 if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
 if 55 - 55: OOoOoo - oo0oO00 + IIiIiII11i + iiII11i1I1IIi % IIi
def I1III1111iIi ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   iiI11i1II ( )
  if O0oO0 == 1 :
   OO0O0OOo0O ( )
  if O0oO0 == 2 :
   I1o0OooOOOOOO ( )
  if O0oO0 == 3 :
   OOooO0o0 ( )
  if O0oO0 == 4 :
   iiIII1i ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I1I ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   ooooO0oOoOOoO = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1i11i = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   IiIi = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   OOOOO0O00 = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   Iii = '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]'
  ii1I = [ ooooO0oOoOOoO , I1i11i , IiIi , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , Iii , '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , OOOOO0O00 ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   IiIi1I1 ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , IiIIi1 , Oo0OO )
  if O0oO0 == 1 :
   IiIi1I1 ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLm5ldC9yZWFwZXIvbWFpbm1lbnUucGhw' ) ) , IiIIi1 , Oo0OO )
  if O0oO0 == 2 :
   iIIiIiI1I1 ( )
  if O0oO0 == 3 :
   IiIi1I1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , IiIIi1 , Oo0OO )
  if O0oO0 == 4 :
   ooO ( )
  if O0oO0 == 5 :
   IiIi1I1 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , IiIIi1 , Oo0OO )
  if O0oO0 == 6 :
   iiOO0O0Ooo ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'TheReaper.png' , OO0o , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , OO0o , '' )
   if 77 - 77: I11i / ii
   if 46 - 46: I11i % iI11I1II1I1I . iiII11i1I1IIi % iiII11i1I1IIi + Ii
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , OO0o , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , OO0o , '' )
  if 72 - 72: iI11I1II1I1I * IIi % OOoOoo / oO0o
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 35 - 35: OOoOoo + ooOoO0O00 % Ii1I % oo0oO00 + O0oOO0
def iiiI ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
def I1ii1 ( url ) :
 OOoO = O00 ( url )
 url = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OOoO )
 for Oo0o0000OOoO , IiIi1I1ii111 in o00oooO0Oo :
  if '[DIR]' in Oo0o0000OOoO :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + IiIi1I1ii111 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIi1I1ii111 , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in IiIi1I1ii111 :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + IiIi1I1ii111 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIi1I1ii111 , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in IiIi1I1ii111 :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + IiIi1I1ii111 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIi1I1ii111 , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 5 - 5: IIi
def ooO ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 if 46 - 46: iIi1i1ii1
def ii1iIi1iIiI1i ( url ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for Oo0OO , url , OOooO0oo0o00o , ooOO0OoO , iiI11ii1I1 , Oo0 in o00oooO0Oo :
  if ooOO0OoO == '123' :
   ooOO0OoO = oOOOo00O00oOo + 'appstreams.png'
  if iiI11ii1I1 == '123' :
   iiI11ii1I1 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IiiiiI ( Oo0OO , url , 100010 , ooOO0OoO , iiI11ii1I1 , Oo0 )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0OO , url , 100007 , ooOO0OoO , iiI11ii1I1 , Oo0 )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0OO , url , 100100 , ooOO0OoO , iiI11ii1I1 , Oo0 )
  elif not 'http' in url :
   oooooOOO000Oo ( Oo0OO , url , 100009 , ooOO0OoO , iiI11ii1I1 , Oo0 , '' )
  else :
   oooooOOO000Oo ( Oo0OO , url , 100005 , ooOO0OoO , iiI11ii1I1 , Oo0 , '' )
   if 52 - 52: IIiIiII11i % iIi1i1ii1 . OOooOOo * iI11I1II1I1I
def I111i1II ( url ) :
 I1 = iiI1iIii1i ( url )
 O0ooooo0OOOO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , IiiIi1III , Oo0 , iiI11ii1I1 , Oo0OO in O0ooooo0OOOO0 :
  if IiiIi1III == '123' :
   IiiIi1III = oOOOo00O00oOo + 'appstreams.png'
  if iiI11ii1I1 == '123' :
   iiI11ii1I1 = OO0o
  if 'php' in url :
   I1IiiiiI ( Oo0OO , url , 100004 , IiiIi1III , iiI11ii1I1 , Oo0 )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0OO , url , 100007 , IiiIi1III , iiI11ii1I1 , Oo0 )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0OO , url , 100100 , IiiIi1III , iiI11ii1I1 , Oo0 )
  elif not 'http' in url :
   oooooOOO000Oo ( Oo0OO , url , 100009 , IiiIi1III , iiI11ii1I1 , Oo0 , '' )
  else :
   oooooOOO000Oo ( Oo0OO , url , 100005 , IiiIi1III , iiI11ii1I1 , Oo0 , '' )
   if 84 - 84: Oooo0O0oo00oO . iiII11i1I1IIi % o0o00Oo0O . OOooOOo + O0oOO0
def Ii11i1I11i ( url ) :
 if 13 - 13: iIi1i1ii1 / Ii % IIiIiII11i % oo0oO00 . Ii1I
 I1 = iiI1iIii1i ( url )
 iIIIii = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for OOo0 in iIIIii :
  ooOO0OoO = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( OOo0 ) )
  for ooOO0OoO in ooOO0OoO :
   ooOO0OoO = ooOO0OoO
  Oo0OO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( OOo0 ) )
  for Oo0OO in Oo0OO :
   if 'elete' in Oo0OO :
    pass
   elif 'rivate Vid' in Oo0OO :
    pass
   else :
    Oo0OO = ( Oo0OO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  ii11I1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( OOo0 ) )
  for ii11I1 in ii11I1 :
   ii11I1 = ii11I1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( OOo0 ) )
  for url in url :
   url = url
  oooooOOO000Oo ( '[COLORred]' + str ( ii11I1 ) + '[/COLOR] : ' + str ( Oo0OO ) , str ( url ) , 100009 , str ( ooOO0OoO ) , OO0o , '' , '' )
  Iii1I1I11iiI1 ( 'movies' , '' )
  if 75 - 75: oO0o / IIiIiII11i % o0o00Oo0O
  if 38 - 38: ii * OOoOoo % o0o00Oo0O * OOooOOo
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - IIi
  if 20 - 20: ooOoO0O00 % oO0o . oOo0O0Ooo / iIi1i1ii1 * Ii * Oooo0O0oo00oO
  if 85 - 85: I11i . OOooOOo / OOoOoo . o0o00Oo0O % OooOO000
def OO0ooo0oOO ( iconimage , url , extra ) :
 ooOO0OoO = ' '
 oo000ii = ' '
 iiI11ii1I1 = ' '
 OoO = ' '
 Iiiiii111i1ii = iiI1iIii1i ( url )
 ooOO0OoO = re . compile ( '<img src="(.+?)">' ) . findall ( Iiiiii111i1ii )
 for ooOO0OoO in ooOO0OoO :
  ooOO0OoO = ooOO0OoO
 i1i1iII1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( Iiiiii111i1ii )
 for iiI11ii1I1 in i1i1iII1 :
  iiI11ii1I1 = iiI11ii1I1
 o00oooO0Oo = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( Iiiiii111i1ii )
 for url , OoO in o00oooO0Oo :
  OoO = 'S' + ( OoO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o0O + url
  iii11i1IIII ( ( OoO ) . replace ( '  ' , '' ) , url , 100101 , ooOO0OoO , iiI11ii1I1 , oo000ii , '' )
  Iii1I1I11iiI1 ( 'Movies' , 'info' )
  if 26 - 26: o0o00Oo0O . oO0o * OooOO000 . oOo0O0Ooo % Ii
def i1Ii1iii ( url , name , fanart , extra , iconimage ) :
 IIiIiiii = extra
 OoO = name
 Iiiiii111i1ii = iiI1iIii1i ( url )
 ooOO0OoO = iconimage
 o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( Iiiiii111i1ii )
 for url , name , O0000OOO0 in o00oooO0Oo :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o0O + url
  O0000OOO0 = O0000OOO0
  ooo0 = name + ' - [COLORred]' + O0000OOO0 + '[/COLOR]'
  iii11i1IIII ( ooo0 , url , 100102 , ooOO0OoO , fanart , 'Aired : ' + O0000OOO0 , ooo0 )
  if 78 - 78: OOoOoo
def O0oOo00o0o00O ( name , URL , iconimage , fanart ) :
 I1 = iiI1iIii1i ( URL )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , name in o00oooO0Oo :
  for OO00 in O00oO :
   if OO00 in ooO0oOOooOo0 :
    URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
    oooooOOO000Oo ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' , '' )
 if len ( o00oooO0Oo ) <= 0 :
  iii11i1IIII ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 92 - 92: oo0oO00
  if 95 - 95: ii - iIi1i1ii1 * oOo0O0Ooo + OOooOOo
def iIi1 ( url , name ) :
 i11iiI1111 = name
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 oOoooo000Oo00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  OOoo ( url , i11iiI1111 )
 for url in o0O0OOO0Ooo :
  OOoo ( url , i11iiI1111 )
 for url in oOoooo000Oo00 :
  OOoo ( url , i11iiI1111 )
  if 69 - 69: oo0oO00
def OOoo ( url , season_name ) :
 if 'daclips.in' in url :
  O00oO0 ( url , season_name )
 elif 'filehoot.com' in url :
  o0o0o0o0 ( url , season_name )
 elif 'allmyvideos.net' in url :
  I1Iiiiiii ( url , season_name )
 elif 'vidspot.net' in url :
  I1IIIiI1I1ii1 ( url , season_name )
 elif 'vodlocker' in url :
  iiiI1I1iIIIi1 ( url , season_name )
 elif 'vidto' in url :
  IiiI1iiiiI1iI ( url , season_name )
  if 43 - 43: O0oOO0 - ii
  if 3 - 3: o0o00Oo0O / iiII11i1I1IIi
def IiiI1iiiiI1iI ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for iIiIi1I , Oo0OO in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 35 - 35: Ii1I * iiII11i1I1IIi - oO0o % I11i
  if 87 - 87: OOooOOo * OooOO000 . oo0oO00
def I1Iiiiiii ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for iIiIi1I , Oo0OO in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 51 - 51: Oooo0O0oo00oO % iI11I1II1I1I - ii % OOoOoo * iI11I1II1I1I % oO0o
def I1IIIiI1I1ii1 ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for iIiIi1I , Oo0OO in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 99 - 99: O0oOO0 * IIiIiII11i * OooOO000
def iiiI1I1iIIIi1 ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for iIiIi1I in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 92 - 92: I1ii11iIi11i
def O00oO0 ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for iIiIi1I in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 40 - 40: OOooOOo / iIi1i1ii1
def o0o0o0o0 ( url , season_name ) :
 I1 = iiI1iIii1i ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for iIiIi1I in o00oooO0Oo :
  iiii11i ( iIiIi1I , season_name )
  if 79 - 79: oO0o - iI11I1II1I1I + IIi - OooOO000
def iiii11i ( Link , season_name ) :
 if 'http:/' in Link :
  OoOiIIiii ( Link )
  if 61 - 61: iIi1i1ii1 . ooOoO0O00 / OooOO000 % Ii * iiII11i1I1IIi
def i1i1i1I ( url ) :
 I1 = OPEN_URL_1 ( url )
 oOoo000 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in oOoo000 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 87 - 87: ii - I11i / iIi1i1ii1 . Ii * ii
def iii11i1IIII ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  if 81 - 81: O0oOO0 * oO0o
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = True )
 return o00ooO00O
 if 38 - 38: OOooOOo / iiII11i1I1IIi % I1ii11iIi11i
 if 11 - 11: iiII11i1I1IIi - O0oOO0 + IIiIiII11i - iI11I1II1I1I
def oooooOOO000Oo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  Oo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = False )
 return o00ooO00O
 if 7 - 7: iIi1i1ii1 - oo0oO00 / IIiIiII11i * IIi . iiII11i1I1IIi * iiII11i1I1IIi
def O0O0oOOo0O ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 19 - 19: I11i / OooOO000 % I11i % iiII11i1I1IIi * iIi1i1ii1
def ii1oOoO0o0ooo ( url ) :
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0o0O0Ooo0o . play ( url ) . strip ( )
 except : pass
 if 18 - 18: IIiIiII11i . ii % OOooOOo % IIi
def OoOiIIiii ( url ) :
 oO0o0O0Ooo0o = xbmc . Player ( )
 import urlresolver
 try : oO0o0O0Ooo0o . play ( url )
 except : pass
 if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def iiI1iIii1i ( url ) :
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
  if 2 - 2: ii % Oooo0O0oo00oO
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
  if 39 - 39: iiII11i1I1IIi / IIiIiII11i / Ii1I % oOo0O0Ooo
def OooOo0oo0O0o00O ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   O0Oo00 ( )
  if O0oO0 == 1 :
   ii1IiIIi1i ( )
  if O0oO0 == 2 :
   oOOo0OOOOo0Oo ( )
  if O0oO0 == 3 :
   OOo0o ( )
  if O0oO0 == 4 :
   ooo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def IIIIiii1IIii ( ) :
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
 if 20 - 20: ooOoO0O00 - oo0oO00
 if 30 - 30: OOooOOo
 if 21 - 21: Ii / OooOO000 % Oooo0O0oo00oO * o0o00Oo0O . oo0oO00 - iI11I1II1I1I
def IiI111111IIII ( ) :
 I1 = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o00oooO0Oo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiIi1iI in o00oooO0Oo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   iiIiiii1i1i1i = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOOiiiiI ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iiIiiii1i1i1i + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO0 == 0 :
    OOOOooO0oO00O0o ( IIiIi1iI )
    o00O0 ( )
   elif O0oO0 == 1 :
    ooOO00oOOo000 ( IIiIi1iI )
  else :
   pass
   if 14 - 14: oO0o . IIiIiII11i . oo0oO00 / IIi % Ii1I - OOoOoo
def ooOO00oOOo000 ( addon ) :
 iiIiiii1i1i1i = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 67 - 67: oo0oO00 - Oooo0O0oo00oO . ooOoO0O00
def OOOOooO0oO00O0o ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1I1iI = os . path . join ( iIi1ii1I1 , 'default.py' )
 I1iIi1iiIIiI = open ( I1I1iI , "w+" )
 if 81 - 81: oO0o * OOooOOo . Oooo0O0oo00oO
 I1iIi1iiIIiI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1iIi1iiIIiI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1iIi1iiIIiI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 11 - 11: Ii - O0oOO0 . O0oOO0
 if 31 - 31: Oooo0O0oo00oO / I1ii11iIi11i * ooOoO0O00 . OOooOOo
 if 57 - 57: Oooo0O0oo00oO + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
 if 83 - 83: I11i / Ii % iI11I1II1I1I . oo0oO00 % O0oOO0 . ii
def o00oO00 ( ) :
 I1 = O0 ( 'http://www.tvcatchup.com/channels/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for OO0oOOo , IiiIi1III , ooO0oOOooOo0 in o00oooO0Oo :
  IIIII1 ( OO0oOOo , 'http://www.tvcatchup.com' + ooO0oOOooOo0 , 90024 , 'http://www.tvcatchup.com' + IiiIi1III )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def OO0oO0o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
  if 71 - 71: oo0oO00 / oo0oO00 * O0oOO0 * O0oOO0 / IIiIiII11i
def oo00O0oO0O0 ( ) :
 IiIiIi ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O0 ( 'http://www.join4films.com/' )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def II1I1iiIII1I1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IIIII1 ( Oo0OO , url , 80007 , IiiIi1III )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def o0Ooo0o0ooo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  url = ( url ) . replace ( ' ' , '%20' )
  III111i11IiI ( url )
def oo0o0000Oo0 ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000O0OO00oo = 'http://www.join4films.com/?s=' + ( o0O00oOoo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oOOO = O000O0OO00oo . lower ( )
 II1I1iiIII1I1 ( oOOO )
 if 56 - 56: Ii1I
 if 26 - 26: ii % ii
 if 33 - 33: OooOO000
 if 62 - 62: Ii1I + IIi + ooOoO0O00 / ii
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 if 22 - 22: OOoOoo - OOoOoo % Oooo0O0oo00oO . OooOO000 + O0oOO0
 if 63 - 63: oOo0O0Ooo % OooOO000 * I11i + OooOO000 / I1ii11iIi11i % iiII11i1I1IIi
 if 45 - 45: iIi1i1ii1
 if 20 - 20: ii * I11i * o0o00Oo0O . Oooo0O0oo00oO
 if 78 - 78: iI11I1II1I1I + oo0oO00 - IIi * OooOO000 - ii % OOooOOo
 if 34 - 34: o0o00Oo0O
 if 80 - 80: ooOoO0O00 - I1ii11iIi11i / oO0o - Ii
 if 68 - 68: O0oOO0 - Ii1I % o0o00Oo0O % OooOO000
 if 11 - 11: o0o00Oo0O / oO0o % Oooo0O0oo00oO + I11i + iI11I1II1I1I
 if 40 - 40: OOoOoo - Oooo0O0oo00oO . IIi * I1ii11iIi11i % OooOO000
 if 56 - 56: Ii . I11i - oOo0O0Ooo * oo0oO00
 if 91 - 91: O0oOO0 + ii - ooOoO0O00
def o000 ( ) :
 I1IiiiiI ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 if 94 - 94: I11i + o0o00Oo0O / oo0oO00 . oOo0O0Ooo + Oooo0O0oo00oO . iI11I1II1I1I
def OOOoO ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000O0OO00oo = 'http://imoviemax.se/?s=' + ( o0O00oOoo ) . replace ( ' ' , '+' )
 oOOO = O000O0OO00oo . lower ( )
 oOooo ( oOOO )
def oo00OOoOoO00 ( url ) :
 I1iii = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , Oo0OO , oOO0OO0O in o00oooO0Oo :
  if Oo0OO in I1iii :
   pass
  else :
   I1IiiiiI ( Oo0OO + ' - ' + oOO0OO0O + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
   I1iii . append ( Oo0OO )
   if 78 - 78: IIi / IIiIiII11i % OOooOOo
def oO00OoOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , I11IIiIiI in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + ' - Views:' + I11IIiIiI , url , 10075 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
  if 5 - 5: I1ii11iIi11i * OOooOOo
  if 46 - 46: OOoOoo
def oOooo ( url ) :
 I11iIiII = [ ]
 I1 = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IiiiiI ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10075 , IiiIi1III , IiiIi1III , '' )
  I11iIiII . append ( Oo0OO )
  if 66 - 66: I1ii11iIi11i - I11i * iIi1i1ii1 + OOooOOo + I11i - iI11I1II1I1I
def iiiI1ii11 ( img , name , url ) :
 img = img
 name = name
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for ii1i , url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  IIioo0OO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + IIioo0OO
  IiiI11i1I = ( ii1i ) . replace ( 'play-' , 'Server ' )
  o0OIiII ( IiiI11i1I , IIioo0OO , 10076 , img , img , '' )
  if 80 - 80: Oooo0O0oo00oO / oo0oO00 / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def iIIiiIIi1IiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for IiIi1I1ii111 in o00oooO0Oo :
  if '=m' in IiIi1I1ii111 :
   I11IIIiIi11 ( IiIi1I1ii111 )
  elif 'php' in IiIi1I1ii111 :
   iIIiiIIi1IiI ( url )
  else :
   I1 = O0 ( IiIi1I1ii111 )
   o00oooO0Oo = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for I11iiIi1i1 in o00oooO0Oo :
    I11IIIiIi11 ( IiIi1I1ii111 )
    if 41 - 41: IIi % Ii1I
    if 12 - 12: Oooo0O0oo00oO
    if 69 - 69: ii + Oooo0O0oo00oO
def IIi11I1 ( url ) :
 I1 = O0 ( url )
 iiiI111I = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0000OOO0 , oooOOO00o0 in iiiI111I :
  print 'there ><><><><><><><><><><><><'
  O0000OOO0 = O0000OOO0
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oooOOO00o0 ) )
  for Oo0OO , i1I in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + O0000OOO0 + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + i1I + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
 OOo0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for O0000OOO0 , iiII1I11IIi in OOo0 :
  print 'there ><><><><><><><><><><><><'
  O0000OOO0 = O0000OOO0
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiII1I11IIi ) )
  for Oo0OO , i1I in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + O0000OOO0 + '[/COLOR] - ' + Oo0OO + ' - [COLOR' + iiI1IiI + ']' + i1I + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
   if 66 - 66: Ii / I11i - ii / ooOoO0O00 . Ii
   if 16 - 16: I1ii11iIi11i % Ii1I + oo0oO00 - o0o00Oo0O . iiII11i1I1IIi / OooOO000
   if 35 - 35: O0oOO0 / OooOO000 / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . OooOO000
def iiIII1i ( url ) :
 I1 = O0 ( url )
 OOo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for OOo0 in OOo0 :
  Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( OOo0 ) )
  for Oo0OO in Oo0OO :
   Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOo0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooOO0OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( OOo0 ) )
  for ooOO0OoO in ooOO0OoO :
   ooOO0OoO = 'http:' + ooOO0OoO
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , '' , '' )
  if 81 - 81: iiII11i1I1IIi * Oooo0O0oo00oO - Ii1I * IIi % OOooOOo * OOooOOo
  if 59 - 59: iI11I1II1I1I
  if 7 - 7: Oooo0O0oo00oO * oOo0O0Ooo / I11i * Ii
  if 84 - 84: Oooo0O0oo00oO . iiII11i1I1IIi
def ooo0OO0O0Oo ( url ) :
 if 8 - 8: I1ii11iIi11i + IIiIiII11i * Oooo0O0oo00oO * OOooOOo * oo0oO00 / iIi1i1ii1
 iIii = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for IiIi1I1ii111 , IiiIi1III , Oo0OO , OO0OoOOO0 in o00oooO0Oo :
  Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O0 ( IiIi1I1ii111 )
  o0O0OOO0Ooo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for oOoo000 , oo000ii in o0O0OOO0Ooo :
   O00ooOo = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oo000ii ) )
   for Oo0 in O00ooOo :
    if Oo0OO in iIii :
     pass
    else :
     o0OIiII ( Oo0OO , oOoo000 , 8043 , IiiIi1III , IiiIi1III , Oo0 )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
     iIii . append ( Oo0OO )
     if 80 - 80: I11i - Oooo0O0oo00oO + ii
     if 98 - 98: Oooo0O0oo00oO + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
def iIIi1I1ii ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , IiIIi1 , Oo0 , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 10065 , IiIIi1 , iiI11ii1I1 , Oo0 )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 14 - 14: o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000O0OO00oo = 'https://www.youtube.com/results?search_query=' + ( o0O00oOoo ) . replace ( ' ' , '+' )
 oOOO = O000O0OO00oo . lower ( )
 I1 = O0 ( oOOO )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for ooO0oOOooOo0 in next :
  ooO0oOOooOo0 = 'https://www.youtube.com' + ooO0oOOooOo0
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , ooO0oOOooOo0 , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for IiiIi1III , ooO0oOOooOo0 , Oo0OO , I1IIII1ii , oo000ii in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  ooOO0OoO = 'http:' + ( IiiIi1III ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooOO0OoO
  ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
  o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , ooOO0OoO , oo000ii )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for IiiIi1III , ooO0oOOooOo0 , Oo0OO , I1IIII1ii in o00oooO0Oo :
   print 'im doing it'
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   ooOO0OoO = 'http:' + ( IiiIi1III ) . replace ( 'https:' , '' )
   ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
   if '&' in ooO0oOOooOo0 :
    print ' i got here'
    I1 = O0 ( ooO0oOOooOo0 )
    OOo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for OOo0 in OOo0 :
     Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( OOo0 ) )
     for Oo0OO in Oo0OO :
      Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     ooO0oOOooOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOo0 ) )
     for ooO0oOOooOo0 in ooO0oOOooOo0 :
      ooO0oOOooOo0 = 'https://www.youtube.com/w' + ooO0oOOooOo0
     ooOO0OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( OOo0 ) )
     for ooOO0OoO in ooOO0OoO :
      ooOO0OoO = 'http:' + ooOO0OoO
     o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in ooO0oOOooOo0 or 'elete' in Oo0OO :
    pass
   elif 'hannel' in ooO0oOOooOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooO0oOOooOo0
    I1 = O0 ( ooO0oOOooOo0 )
    IiIIi1I1I11Ii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for IiiIi1III , ooO0oOOooOo0 , Oo0OO in IiIIi1I1I11Ii :
     if 'outube' in ooO0oOOooOo0 or 'list' in ooO0oOOooOo0 :
      pass
     elif 'atch' in ooO0oOOooOo0 :
      ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiiIi1III , 'http:' + IiiIi1III , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , ooOO0OoO , '' )
    if 64 - 64: ii
def oO0oooooo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for IiiIi1III , url , Oo0OO , I1IIII1ii , oo000ii in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0OO )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  ooOO0OoO = 'http:' + ( IiiIi1III ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooOO0OoO
  url = 'http://www.youtube.com' + url
  o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , ooOO0OoO , oo000ii )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for IiiIi1III , url , Oo0OO , I1IIII1ii in o00oooO0Oo :
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   ooOO0OoO = 'http:' + ( IiiIi1III ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O0 ( url )
    OOo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for OOo0 in OOo0 :
     Oo0OO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( OOo0 ) )
     for Oo0OO in Oo0OO :
      Oo0OO = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( OOo0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooOO0OoO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( OOo0 ) )
     for ooOO0OoO in ooOO0OoO :
      ooOO0OoO = 'http:' + ooOO0OoO
     o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , OO0o , '' )
   elif Oo0OO in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in Oo0OO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O0 ( url )
    IiIIi1I1I11Ii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for IiiIi1III , url , Oo0OO in IiIIi1I1I11Ii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiiIi1III , 'http:' + IiiIi1III , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + I1IIII1ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO , ooOO0OoO , '' )
    if 65 - 65: iIi1i1ii1 + I1ii11iIi11i
    if 59 - 59: ii + oo0oO00 . OooOO000 - o0o00Oo0O % iI11I1II1I1I / o0o00Oo0O
def oOIIiIi ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OOooO0o = open ( O000oo0O )
  o00oooO0Oo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OOooO0o ) )
  for ii1iI1iI1 , o00oOOO in o00oooO0Oo :
   if ii1iI1iI1 == 'needs replacing' or o00oOOO == 'needs replacing' :
    OoOO0OOoo ( )
    if 1 - 1: oOo0O0Ooo * Ii + OooOO000 * Ii + oO0o
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if 30 - 30: I1ii11iIi11i . oO0o
def o0Oii1111i ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 OoOO0OOoo ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 75 - 75: iIi1i1ii1 + IIiIiII11i / O0oOO0 - O0oOO0 / ii
def iiii11ii ( ) :
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
 if 50 - 50: IIi / OOooOOo * IIi
def Ii1iIi111i1i1 ( name ) :
 IIOO0ooOo0OoOo0 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , IiiIi1III , oOo , ooO0oOOooOo0 in o00oooO0Oo :
  if IIOO0ooOo0OoOo0 == 'Full List' :
   ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
   o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , IiiIi1III , IiiIi1III , '' )
  else :
   IIOO0ooOo0OoOo0 = ( IIOO0ooOo0OoOo0 ) . replace ( 'World' , 'القنوات العربية' )
   if IIOO0ooOo0OoOo0 in oOo :
    ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
    print ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , IiiIi1III , IiiIi1III , '' )
   else :
    pass
    if 17 - 17: IIi . Ii
def IIIiiiI ( name ) :
 IIOO0ooOo0OoOo0 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , IiiIi1III , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
  o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , IiiIi1III , IiiIi1III , '' )
 else :
  o0OIiII ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 94 - 94: o0o00Oo0O - oo0oO00 - iI11I1II1I1I % OOoOoo / IIi % iiII11i1I1IIi
  if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
  if 90 - 90: IIiIiII11i + ii % ii
  if 35 - 35: iiII11i1I1IIi / Ii1I * ii . IIiIiII11i / I1ii11iIi11i
  if 1 - 1: ii + iIi1i1ii1 . ooOoO0O00 % oo0oO00
  if 66 - 66: I11i + Ii1I + oOo0O0Ooo - O0oOO0
  if 12 - 12: iiII11i1I1IIi . iIi1i1ii1 . OOooOOo / o0o00Oo0O
  if 58 - 58: I11i - IIiIiII11i % O0oOO0 + OooOO000 . OOooOOo / iIi1i1ii1
  if 8 - 8: Ii1I . oO0o * oo0oO00 + IIiIiII11i % Ii
  if 8 - 8: OOoOoo * o0o00Oo0O
  if 73 - 73: I11i / O0oOO0 / oo0oO00 / oO0o
  if 11 - 11: OOooOOo + iIi1i1ii1 - ii / oO0o
def oOo0OOoO0 ( ) :
 I1IiiiiI ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IiiiiI ( 'Backup Genie Favourites' , ooO0oOOooOo0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( o00OO00OoO ) :
  I1IiiiiI ( 'Backup Ivue Config' , o00OO00OoO , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  I1IiiiiI ( 'Backup Kodi Favourites' , OOOO0OOoO0O0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 34 - 34: OOoOoo
  if 45 - 45: OOoOoo / I1ii11iIi11i / IIi
  if 44 - 44: Ii1I - IIi / IIiIiII11i * oO0o * I1ii11iIi11i
zip = oo00 . getSetting ( 'zip' )
OO0ooo0o0 = xbmc . translatePath ( os . path . join ( zip ) )
def oO0ooOoO ( ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 59 - 59: o0o00Oo0O % I1ii11iIi11i
  if 92 - 92: IIi % iiII11i1I1IIi / Ii1I % Ii1I * oOo0O0Ooo
  if 74 - 74: o0o00Oo0O . oOo0O0Ooo % oO0o % iIi1i1ii1
def oOo0OooOo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O0Oo000ooO00
  elif 'Ivue' in name :
   url = o00OO00OoO
  elif 'Kodi' in name :
   url = OOOO0OOoO0O0
  oO0ooOoO ( )
  o0iIiiIiiIi = open ( url ) . read ( )
  i1iiIIIi = os . path . join ( OO0ooo0o0 , description . split ( 'Your ' ) [ 1 ] )
  oOOo0O00o = open ( i1iiIIIi , mode = 'w' )
  oOOo0O00o . write ( o0iIiiIiiIi )
  oOOo0O00o . close ( )
 else :
  if 'guisettings.xml' in description :
   Oo0o = open ( os . path . join ( OO0ooo0o0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOoOoo0O0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   o00oooO0Oo = re . compile ( oOOoOoo0O0 ) . findall ( Oo0o )
   for type , i1i1ii1111i1i , iIiI in o00oooO0Oo :
    iIiI = iIiI . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , i1i1ii1111i1i , iIiI ) )
  else :
   i1iiIIIi = os . path . join ( url )
   o0iIiiIiiIi = open ( os . path . join ( OO0ooo0o0 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0O00o = open ( i1iiIIIi , mode = 'w' )
   oOOo0O00o . write ( o0iIiiIiiIi )
   oOOo0O00o . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 26 - 26: iI11I1II1I1I % Ii % Ii1I
 if 67 - 67: ii
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + Oooo0O0oo00oO * iIi1i1ii1
 if 2 - 2: ooOoO0O00 - OOoOoo + oOo0O0Ooo . I11i * I11i / OOooOOo
def oOOOiIi1I1 ( ) :
 O0oOoo0OoO0O = 1
 oO0ooOoO ( )
 oo00IiI1 = xbmc . translatePath ( os . path . join ( OO0ooo0o0 , 'Build Backup' , 'Full Backup' , '' ) )
 oOo00o00oO = xbmc . translatePath ( os . path . join ( OO0ooo0o0 , 'Build Backup' , 'my_full_backup.zip' ) )
 o0000 = xbmc . translatePath ( os . path . join ( OO0ooo0o0 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oo00IiI1 ) :
  os . makedirs ( oo00IiI1 )
 i111i1i = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i111i1i ) : return False , 0
 IiIii1I1I = i111i1i
 OO0Oooo0oo = xbmc . translatePath ( os . path . join ( oo00IiI1 , IiIii1I1I + '.zip' ) )
 I1i111IiIiIi1 = [ 'plugin.video.GenieTv' ]
 i1II11II1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 II1IIIii = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 iIIIiIi1I1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OoOOoO0oOo = "Creating full backup of existing build"
 O0ooOOOO0O0 = "Creating Community Build"
 i1IIi1i1Ii1 = "Archiving..."
 Iiio0Oo0oO = ""
 iI = "Please Wait"
 II1iiIi11 ( I11 , OO0Oooo0oo , O0ooOOOO0O0 , i1IIi1i1Ii1 , Iiio0Oo0oO , iI , II1IIIii , iIIIiIi1I1i )
 time . sleep ( 1 )
 ooOo0O0O0oOO0 = xbmc . translatePath ( os . path . join ( oo00IiI1 , IiIii1I1I + '_guisettings.zip' ) )
 iIiIIi = zipfile . ZipFile ( ooOo0O0O0oOO0 , mode = 'w' )
 try :
  iIiIIi . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iIiIIi . close ( )
 if O0oOoo0OoO0O == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOo00o00oO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OO0Oooo0oo + '[/COLOR]' )
  if 14 - 14: I11i / Oooo0O0oo00oO - iI11I1II1I1I - O0oOO0 % OOoOoo
def II1iiIi11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I1iIiI1IiIIII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 I1iiIi111I = len ( sourcefile )
 Iiii1iIii = [ ]
 oOoooO000O = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for III1I11i1iIi , OO0oo0O0OOO0 , OoOOo in os . walk ( sourcefile ) :
  for file in OoOOo :
   oOoooO000O . append ( file )
 Iii1 = len ( oOoooO000O )
 for III1I11i1iIi , OO0oo0O0OOO0 , OoOOo in os . walk ( sourcefile ) :
  OO0oo0O0OOO0 [ : ] = [ OoOOo00 for OoOOo00 in OO0oo0O0OOO0 if OoOOo00 not in exclude_dirs ]
  OoOOo [ : ] = [ oOOo0O00o for oOOo0O00o in OoOOo if oOOo0O00o not in exclude_files ]
  for file in OoOOo :
   Iiii1iIii . append ( file )
   O00O0O = len ( Iiii1iIii ) / float ( Iii1 ) * 100
   o0oOoO00o . update ( int ( O00O0O ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O0OOo = os . path . join ( III1I11i1iIi , file )
   if not 'temp' in OO0oo0O0OOO0 :
    if not 'plugin.program.originwizard' in OO0oo0O0OOO0 :
     import time
     OOo0oiIiii = '01/01/1980'
     IiIii1ii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O0OOo ) ) )
     if IiIii1ii > OOo0oiIiii :
      I1iIiI1IiIIII . write ( O0OOo , O0OOo [ I1iiIi111I : ] )
 I1iIiI1IiIIII . close ( )
 o0oOoO00o . close ( )
 if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
 if 43 - 43: Ii1I - iiII11i1I1IIi
def iiOO0O0Ooo ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 if 70 - 70: iiII11i1I1IIi / Oooo0O0oo00oO % OOoOoo - IIi
 if 47 - 47: iiII11i1I1IIi
def o00Ooo0 ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  i1O0 ( )
 if O0oO0 == 1 :
  iiI11i1II ( )
 if O0oO0 == 2 :
  O0Oo00 ( )
 if O0oO0 == 3 :
  ooO00O00oOO ( )
  if 62 - 62: Oooo0O0oo00oO + IIi - OOooOOo * OOooOOo . OOooOOo + ii
  if 77 - 77: iI11I1II1I1I . IIi % O0oOO0 / IIi
  if 54 - 54: O0oOO0 + OOoOoo - I1ii11iIi11i
  if 35 - 35: IIi - IIi + ooOoO0O00 - o0o00Oo0O - OooOO000
  if 58 - 58: OOooOOo - iiII11i1I1IIi - ii
  if 96 - 96: iI11I1II1I1I
  if 82 - 82: OOooOOo + o0o00Oo0O - iIi1i1ii1 % O0oOO0 * Ii
  if 15 - 15: I11i
  if 39 - 39: Oooo0O0oo00oO / Ii1I / oOo0O0Ooo * OooOO000
def Iii1Ii ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   IiIi1I1 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , IiIIi1 , Oo0OO )
  if O0oO0 == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if O0oO0 == 2 :
   ii11I11i ( )
  if O0oO0 == 3 :
   oOOOO ( )
  if O0oO0 == 4 :
   i11i11 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO0 == 5 :
   i1iiIII1IIiIIII ( )
  if O0oO0 == 6 :
   I1iIIII1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO0 == 7 :
   OO0 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO0 == 8 :
   I11Ii1iI11iI1 ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO0 == 9 :
   i1III1 ( )
  if O0oO0 == 10 :
   Iii111IiIii ( )
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
  if 100 - 100: IIiIiII11i - I11i . IIiIiII11i * IIiIiII11i . iIi1i1ii1
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 2 - 2: ii
def o0o0O00 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   i1i ( )
  if O0oO0 == 1 :
   iI1111iiii ( )
  if O0oO0 == 2 :
   oOO0O00Oo0O0o ( )
  if O0oO0 == 3 :
   O0ooO0Oo00o ( ooO0oOOooOo0 )
  if O0oO0 == 4 :
   IiIIi1II1ii ( ooO0oOOooOo0 )
  if O0oO0 == 5 :
   o00O0 ( )
  if O0oO0 == 6 :
   i1II1Ii1i1 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO0 == 7 :
   I1i1I1I11IiiI ( )
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
  if 40 - 40: oo0oO00 % ii - Oooo0O0oo00oO + I11i / Oooo0O0oo00oO
  if 84 - 84: o0o00Oo0O
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 11 - 11: IIiIiII11i / Ii / o0o00Oo0O
 if 94 - 94: OOoOoo * oo0oO00 - iIi1i1ii1 . iI11I1II1I1I
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
 if 66 - 66: OOoOoo - Oooo0O0oo00oO * OOooOOo / O0oOO0 * IIiIiII11i * oO0o
 if 91 - 91: ii / IIi . oOo0O0Ooo + OOoOoo . IIiIiII11i
def iIiIi1iI11iiI ( ) :
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
 if 26 - 26: iI11I1II1I1I * OooOO000 - Oooo0O0oo00oO
def IIo0Oo0oO0oOO00 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , OO0o , '' )
 if 27 - 27: Ii1I * OooOO000 - oO0o + IIi * IIi
def o0OO0O0OO0oO0 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , OO0o , '' )
 o0OIiII ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , OO0o , '' )
 if 9 - 9: O0oOO0 % Ii / I1ii11iIi11i
 if 20 - 20: O0oOO0 * o0o00Oo0O + oo0oO00 - ii . oo0oO00
 if 60 - 60: I11i . I11i / iiII11i1I1IIi
def OoOoO ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Iio00 ( )
 if O0oO0 == 0 :
  IiI1iiII1i1i ( ooO0oOOooOo0 )
 if O0oO0 == 0 :
  i1IiI ( ooO0oOOooOo0 )
  if 82 - 82: OOooOOo
  if 80 - 80: oO0o % iiII11i1I1IIi
  if 99 - 99: OOoOoo / iI11I1II1I1I - IIi * Ii1I % oOo0O0Ooo
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 13 - 13: oO0o
def O0oo0O0 ( ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o00oooO0Oo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O0o0O00Oo0o0 )
 for IiiIi1III , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , IiiIi1III , IiiIi1III , '' )
 Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
 if 2 - 2: ii . Oooo0O0oo00oO . iIi1i1ii1
def I1iIII1IiiI ( url ) :
 O0o0O00Oo0o0 = O0 ( OOoooOoO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 78 - 78: ii / Oooo0O0oo00oO % OOooOOo * ii
def Iio00 ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 68 - 68: O0oOO0
def i11i11Ii11Iii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ooo00OoOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 93 - 93: iI11I1II1I1I + O0oOO0 % OOoOoo
def iii1IiI1I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + O00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 86 - 86: Ii1I * IIiIiII11i * oo0oO00
def oO0OoooO0oOO00OoOo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OoOi111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 46 - 46: oO0o * I1ii11iIi11i % O0oOO0 + o0o00Oo0O * iIi1i1ii1
def ii1I11i ( url ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 89 - 89: OooOO000 . iIi1i1ii1 % I1ii11iIi11i . I1ii11iIi11i - ii
def IiI1iiII1i1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oo0ooO0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 40 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 75 - 75: IIiIiII11i + Oooo0O0oo00oO
def iIIi11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o0000o0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 90 - 90: iI11I1II1I1I * IIiIiII11i
def oO0O0OO0O ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  oOOo0OoOOOoo ( )
 if O0oO0 == 1 :
  oOOOOoO00Ooo0 ( )
 if O0oO0 == 2 :
  i11iIIi ( )
  if 93 - 93: OOoOoo / Oooo0O0oo00oO * ii - Ii / oOo0O0Ooo
  if 13 - 13: Ii1I / Ii
  if 32 - 32: I11i + oOo0O0Ooo . OooOO000
  if 41 - 41: OOooOOo . Ii / oo0oO00
def oOOOOoO00Ooo0 ( ) :
 OOoO = O00 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , oOo00OoO0O in o00oooO0Oo :
  IiIiIi ( 'Android Apps' + oOo00OoO0O , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for ooO0oOOooOo0 , oOo00OoO0O in o0O0OOO0Ooo :
  IiIiIi ( 'Android Games' + oOo00OoO0O , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def OoOoO0OooOOo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/cat' in url :
   IiIiIi ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def oOIIi ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '/app' in url :
   IiIiIi ( ( Oo0OO ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def I1Ii1IIiI11i1 ( url ) :
 OOoO = O0 ( url )
 Ii11I1iIiiI = url
 if "page=" in str ( url ) :
  Ii11I1iIiiI = url . split ( '?' ) [ 0 ]
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  if 'apk' in url :
   o0OIiII ( ( Oo0OO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + IiiIi1III )
 if len ( o0O0OOO0Ooo ) > 1 :
  o0O0OOO0Ooo = str ( o0O0OOO0Ooo [ len ( o0O0OOO0Ooo ) - 1 ] )
 o0OIiII ( 'Next Page' , Ii11I1iIiiI + str ( o0O0OOO0Ooo ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def O0o0OO00 ( name , url ) :
 OOoO = O00 ( url )
 name = name
 o00oooO0Oo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  url = 'https://www.apkfiles.com' + url
  iIi11i ( name , url , 'Brackets' )
def i11iIIi ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000O0OO00oo = 'https://www.apkfiles.com/search?q=' + ( o0O00oOoo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oOOO = O000O0OO00oo . lower ( )
 I1Ii1IIiI11i1 ( oOOO )
 if 56 - 56: Ii . OOoOoo / iiII11i1I1IIi
def III1iii1i1II ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( O0oOO0o , 'Download' ) )
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
 if 6 - 6: iI11I1II1I1I * ii
def iIiI1I1ii1I1 ( url ) :
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
 if 83 - 83: Oooo0O0oo00oO / o0o00Oo0O % iiII11i1I1IIi - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def OOOO0oOo00O ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , name )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 i1I1I1i1i1i = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1I1I1i1i1i
 print '======================================='
 extract . all ( Ii1I1Ii , i1I1I1i1i1i , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 23 - 23: iI11I1II1I1I
 if 8 - 8: o0o00Oo0O % IIi % iI11I1II1I1I . I11i % o0o00Oo0O
 if 12 - 12: Oooo0O0oo00oO . IIi
 if 79 - 79: OooOO000 / I1ii11iIi11i / iiII11i1I1IIi . OooOO000 * ii + I11i
 if 73 - 73: o0o00Oo0O - Ii1I
def oOOo0OoOOOoo ( ) :
 O0o0O00Oo0o0 = O0 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , ooO0oOOooOo0 , O0OooOo0o , iiI11ii1I1 , ii1IoO0O in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 80003 , O0OooOo0o , oOOOo00O00oOo + 'APKToolsB.png' , ii1IoO0O )
def ooOOooo0ooo00 ( apk , ret = None ) :
 if apk == "kodi" :
  oooOo = "https://kodi.tv/download/"
  O0o0O00Oo0o0 = O0 ( oooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O0o0O00Oo0o0 )
  if len ( o00oooO0Oo ) == 1 :
   oo0oo0O0 = o00oooO0Oo [ 0 ] [ 0 ]
   IiIii1I1I = o00oooO0Oo [ 0 ] [ 1 ]
   IiIIiiI = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oo0oo0O0 , IiIii1I1I )
  if ret == 'version' : return oo0oo0O0
  else : return IiIIiiI
 elif apk == "spmc" :
  o0o0OO0o00o0O = 'https://github.com/koying/SPMC/releases/latest/'
  O0o0O00Oo0o0 = O0 ( o0o0OO0o00o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O0o0O00Oo0o0 )
  oo0oo0O0 = re . sub ( '<[^<]+?>' , '' , o00oooO0Oo [ 0 ] ) . replace ( ' ' , '' )
  IiIIiiI = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oo0oo0O0 , oo0oo0O0 )
  if ret == 'version' : return oo0oo0O0
  else : return IiIIiiI
def iIi11i ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  IIIIIIi1i = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not IIIIIIi1i : iiiii11I1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  Ii1 = name
  if IIIIIIi1i :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not I1i1I11I ( url ) == True : iiiii11I1 ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % Ii1 , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iIiIIi = zipfile . ZipFile ( Ii1I1Ii )
    for file in iIiIIi . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as oOOo0O00o :
       OOOo = file . split ( '/' ) [ 1 ]
       oOOo0O00o . write ( iIiIIi . read ( file ) )
       xbmc . sleep ( 500 )
       oOOo0O00o . close ( )
       try :
        os . remove ( Ii1I1Ii )
       except :
        pass
       Ii1I1Ii = os . path . join ( oooOOOOO , OOOo )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : iiiii11I1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiiii11I1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 35 - 35: OOoOoo - oO0o . I1ii11iIi11i * I1ii11iIi11i / Ii + Ii1I
 if 87 - 87: OOooOOo % iI11I1II1I1I
 if 72 - 72: Oooo0O0oo00oO . Oooo0O0oo00oO - Ii1I
 if 48 - 48: I1ii11iIi11i - OOoOoo + I1ii11iIi11i - oOo0O0Ooo * Ii . iiII11i1I1IIi
def I1iIIIiI ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O0o0O00Oo0o0 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  ooO0oOOooOo0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + ooO0oOOooOo0 )
  OoiI1I1 ( ( Oo0OO ) . replace ( '_' , ' ' ) , ooO0oOOooOo0 )
  if 27 - 27: OOoOoo - I1ii11iIi11i + iiII11i1I1IIi - Oooo0O0oo00oO . oOo0O0Ooo
def OoiI1I1 ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  IIIIIIi1i = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not IIIIIIi1i : iiiii11I1 ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  Ii1 = name
  if IIIIIIi1i :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not I1i1I11I ( url ) == True : iiiii11I1 ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % Ii1 , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : iiiii11I1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiiii11I1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 51 - 51: O0oOO0 + oO0o + iiII11i1I1IIi + iiII11i1I1IIi % I11i
 if 29 - 29: OOoOoo
def ii1iIi1Ii1 ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
def oooO ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 30015 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 71 - 71: ooOoO0O00 - oo0oO00 * OooOO000 + O0oOO0 - oO0o % Ii1I
def Ooo0oO ( url , iconimage , fanart ) :
 O0o0O00Oo0o0 = O0 ( url )
 IIioo0OO = url
 IiiIi1III = iconimage
 fanart = fanart
 o00oooO0Oo = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for IiIi1I1ii111 , Oo0OO in o00oooO0Oo :
  if '.mp4' in Oo0OO :
   o0OIiII ( 'Watch VIDEO' , url + '/' + IiIi1I1ii111 , 222 , IiiIi1III , fanart , '' )
  if 'description' in Oo0OO :
   o0OIiII ( 'Read Description' , url + '/' + IiIi1I1ii111 , 30017 , IiiIi1III , fanart , '' )
  if 'images' in Oo0OO :
   I1IiiiiI ( 'View Images' , url + '/' + IiIi1I1ii111 , 30018 , IiiIi1III , fanart , '' )
  if 'url' in Oo0OO :
   o0OIiII ( 'Install Build On Android' , url + '/' + IiIi1I1ii111 , 30016 , IiiIi1III , fanart , '' )
  if 'url' in Oo0OO :
   o0OIiII ( 'Install Build On Pc' , url + '/' + IiIi1I1ii111 , 30019 , IiiIi1III , fanart , '' )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 32 - 32: ooOoO0O00 . iiII11i1I1IIi + IIiIiII11i - oO0o - iI11I1II1I1I
def iIIIIiiii1I ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  IIi1iI11IIIi1 ( url )
  if 73 - 73: iI11I1II1I1I
def O000o0oo ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  oO0oOoo0O ( url )
  if 26 - 26: I1ii11iIi11i + oOo0O0Ooo * Oooo0O0oo00oO + OOoOoo
def O00o0O ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'desc="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for O00oOo0O0o00O in o00oooO0Oo :
  OOOiiiiI ( 'Description:' , O00oOo0O0o00O )
  if 91 - 91: IIiIiII11i * iiII11i1I1IIi . ooOoO0O00
def II11Ii111II1 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 url = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for IiIi1I1ii111 , Oo0OO in o00oooO0Oo :
  if 'png' in Oo0OO :
   o0OIiII ( 'image' , '' , '' , url + '/' + IiIi1I1ii111 , url + '/' + IiIi1I1ii111 , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 72 - 72: iiII11i1I1IIi % I11i % O0oOO0 + oo0oO00 % Ii + o0o00Oo0O
def OoOOoooO000 ( name , url , description ) :
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
 if 85 - 85: oOo0O0Ooo % oo0oO00 + Oooo0O0oo00oO / IIi % ii
 if 42 - 42: OooOO000 * iIi1i1ii1
def oO0oOoo0O ( url ) :
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
 i1i ( )
 if 23 - 23: O0oOO0 * OooOO000 - ii * ii % oO0o + IIiIiII11i
def IIi1iI11IIIi1 ( url ) :
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
 i1i ( )
 if 9 - 9: iI11I1II1I1I * oO0o % OooOO000
def I1i ( name , url , description ) :
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
 i1i ( )
 if 87 - 87: OOooOOo / iIi1i1ii1 . OOoOoo - Oooo0O0oo00oO / oO0o
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
  iiI1I = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOo0O00o . write ( iiI1I . rstrip ( '\r\n' ) + '\n' )
def i1i ( ) :
 O0oO0 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO0 == 0 : return
 elif O0oO0 == 1 : pass
 ooI111iiiii1 = ii1iII1II ( )
 ii1 ( "Platform: " + str ( ooI111iiiii1 ) )
 os . _exit ( 1 )
 ii1 ( "Force close failed!  Trying alternate methods." )
 if ooI111iiiii1 == 'osx' :
  ii1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ooI111iiiii1 == 'linux' :
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
 elif ooI111iiiii1 == 'android' :
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
 elif ooI111iiiii1 == 'windows' :
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
  if 100 - 100: Ii1I * Ii % O0oOO0 / I1ii11iIi11i / OOoOoo + Ii1I
  if 59 - 59: OooOO000 - iIi1i1ii1
  if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
def i1IiI ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( url ) :
  for file in OoOOo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    Oo0o = open ( ( os . path . join ( i111i1I1ii1i , file ) ) ) . read ( )
    O0Oooo = Oo0o . replace ( I11 , 'special://home/' )
    oOOo0O00o = open ( ( os . path . join ( i111i1I1ii1i , file ) ) , mode = 'w' )
    oOOo0O00o . write ( str ( O0Oooo ) )
    oOOo0O00o . close ( )
 i1i ( )
 if 27 - 27: OOoOoo + Ii * oo0oO00 + OOooOOo + iiII11i1I1IIi
def ii11I11i ( ) :
 IiIiIi ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIiIi ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIiIi ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 87 - 87: o0o00Oo0O
def oOo0 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def OOOOo000o00OO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def Oo0oOo0O0o000Ooo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o0O0OOO0Ooo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']Filter - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , IiiIi1III )
def oooo00o0 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
def I1IiI ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo
 I1iI1 = 'https://www.radionomy.com/en/search/index?query=' + ( o0O00oOoo ) . replace ( ' ' , '+' )
 I1 = O0 ( I1iI1 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0OO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + ooO0oOOooOo0 , 70005 , IiiIi1III )
  if 52 - 52: OOooOOo * oO0o - IIi
  if 82 - 82: oO0o + oOo0O0Ooo . ooOoO0O00 + Oooo0O0oo00oO
def i1iiIII1IIiIIII ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , 'http://www.listenlive.eu/' + ooO0oOOooOo0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def i11i11 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  IIIII1 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 16 - 16: I11i - oO0o / OooOO000
def i11oo ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.toonjet.com/' + ooO0oOOooOo0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiIIiii ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OOoO )
 for url , IiiIi1III in o00oooO0Oo :
  if 'ol.gif' in IiiIi1III :
   pass
  elif 'link_block_' in IiiIi1III :
   pass
  elif '.png' in IiiIi1III :
   pass
  else :
   IiIiIi ( ( IiiIi1III ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in o0O0OOO0Ooo :
  IiIiIi ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooOo0oOO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 68 - 68: OOoOoo / ii * oo0oO00 / O0oOO0
  if 88 - 88: I11i
def Iii111IiIii ( ) :
 iI11 ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 iI11 ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 97 - 97: O0oOO0 + I1ii11iIi11i * Oooo0O0oo00oO % I1ii11iIi11i
def iiIiIIII1iiIIi ( ) :
 iI11 ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iI11 ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 iI11 ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 17 - 17: oo0oO00
def oOoO0ooO0000 ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , OOOOO in o00oooO0Oo :
  if 'Parent' in Oo0OO :
   pass
  elif '2' in OOOOO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 68 - 68: oo0oO00 + oO0o - o0o00Oo0O / oO0o * OOooOOo
def I1iiiI ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , OOOOO in o00oooO0Oo :
  if o0O00oOoo in Oo0OO . lower ( ) :
   if '1' in OOOOO :
    iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOOOO :
    iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOOOO :
    iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 24 - 24: oOo0O0Ooo * O0oOO0
    if 85 - 85: IIiIiII11i . OOoOoo % Oooo0O0oo00oO % oo0oO00
def OOo00ooOoO0o ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0OO , ooO0oOOooOo0 , OOOOO in o00oooO0Oo :
  if '1' in OOOOO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOOOO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOOOO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 21 - 21: Ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: iiII11i1I1IIi . Ii * o0o00Oo0O
def Iiii1 ( url ) :
 IiIi1I1ii111 = url
 I1 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0OO in o0O0OOO0Ooo :
  if 'mp3' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIi1I1ii111 + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIi1I1ii111 + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIi1I1ii111 + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in Oo0OO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIi1I1ii111 + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 27 - 27: Oooo0O0oo00oO
   if 52 - 52: OooOO000 % OOooOOo + iI11I1II1I1I * O0oOO0 . IIi
   if 95 - 95: iI11I1II1I1I . iIi1i1ii1 - ii * oO0o / I11i
def oOo0OO0o0 ( url ) :
 I1 = O0 ( url )
 IiIi1I1ii111 = url
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
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIi1I1ii111 + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Oo0OO :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIi1I1ii111 + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIi1I1ii111 + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: I1ii11iIi11i . I1ii11iIi11i % ii - IIi
   if 43 - 43: oO0o % oO0o
def IIiii11ii1i ( ) :
 iI11 ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iI11 ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iI11 ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 7 - 7: O0oOO0 - o0o00Oo0O * oo0oO00 - I11i - IIiIiII11i
def Ii11iiI1 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III in o00oooO0Oo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IiiIi1III :
   pass
  else :
   iI11 ( IiiIi1III , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooO0oOOooOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IiiIi1III + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 71 - 71: I11i / Oooo0O0oo00oO % Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: ii + Ii / oo0oO00 + iI11I1II1I1I % OOoOoo
 if 29 - 29: Ii1I
def Oo0o00ooOOOoOo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: OOoOoo + OOoOoo % iIi1i1ii1 - I11i - Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: oo0oO00 % Oooo0O0oo00oO
def OoO0 ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if o0O00oOoo in Oo0OO . lower ( ) :
   if '</a>' in Oo0OO :
    pass
   elif '(' in Oo0OO :
    iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 37 - 37: oo0oO00
    if 83 - 83: o0o00Oo0O
def oOOOOOo ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '</a>' in Oo0OO :
   pass
  elif '(' in Oo0OO :
   iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 50 - 50: OooOO000 + OOoOoo + iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: oo0oO00
 if 13 - 13: iI11I1II1I1I * OOooOOo / OooOO000 % OOoOoo + O0oOO0
def iiiI1iI1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in o00oooO0Oo :
  IiIi1I1ii111 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IiIi1I1ii111 )
  if 15 - 15: iIi1i1ii1 . ooOoO0O00 * OOooOOo % iI11I1II1I1I
def III11I1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '<p align' in Oo0OO :
   pass
  elif '&nbsp;' in Oo0OO :
   pass
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 61 - 61: OOooOOo - oO0o + oOo0O0Ooo * Oooo0O0oo00oO % oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: OOoOoo - oo0oO00 * O0oOO0
 if 87 - 87: IIi - Ii1I % Ii1I . O0oOO0 / Ii1I
def ii1IiIIi1i ( ) :
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
def II1i ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0II1IIi1iII1i = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , IiiIi1III , IiiIi1III , Oo0OO )
 for url , Oo0OO in o0II1IIi1iII1i :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iiiiIiIi ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 oO0o0O0Ooo0o = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 iiIiI1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 iII1IiiIIII = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in iiIiI1 :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , Oo0OO in oO0o0O0Ooo0o :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def I11iIooOo0O ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 99 - 99: oO0o - OOooOOo * OOooOOo . IIiIiII11i % OOoOoo
def OOo0o ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 o00oooO0Oo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '9cart' in ooO0oOOooOo0 :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 1 - 1: Ii1I + I1ii11iIi11i * O0oOO0 + I11i - oo0oO00 . Ii1I
def iiIi1i1Ii1Ii ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 oOoooo000Oo00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if '9cart' in url :
   IiIiIi ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in o0O0OOO0Ooo :
  if '9cart' in url :
   IiIiIi ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , Oo0OO in oOoooo000Oo00 :
  if '9cart' in url :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 99 - 99: Ii1I + Oooo0O0oo00oO . O0oOO0
def i1I111I1Iii1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20003 , IiiIi1III )
 for url , Oo0OO in o0O0OOO0Ooo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 68 - 68: iiII11i1I1IIi + I1ii11iIi11i % IIi / Ii % OOooOOo
def ooo0ii1iIIi11 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'Watch' in url :
   IiIiIi ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 21 - 21: I1ii11iIi11i % iIi1i1ii1
def oOO0Oooo ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 26 - 26: I11i / ii % OOoOoo % Oooo0O0oo00oO
def oO0O0o0O ( url ) :
 url = cloudflare . source ( url )
 I11IIIiIi11 ( url )
 if 100 - 100: OOooOOo % I1ii11iIi11i
def OoOO ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . recompile ( 'src="([^"]*)"' )
 for url in o00oooO0Oo :
  I11IIIiIi11 ( url )
  if 1 - 1: Ii1I . Ii
  if 74 - 74: o0o00Oo0O + ii / O0oOO0 / OOooOOo . Ii1I % O0oOO0
def oOOo0OOOOo0Oo ( ) :
 if 34 - 34: ooOoO0O00 . oOo0O0Ooo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 if 6 - 6: OooOO000 % O0oOO0 % IIi
def O0Oo00 ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 63 - 63: o0o00Oo0O . oOo0O0Ooo . o0o00Oo0O * iI11I1II1I1I
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 92 - 92: O0oOO0 / Oooo0O0oo00oO . Ii1I
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if o0O00oOoo in Oo0OO . lower ( ) :
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
    if 30 - 30: IIi . Ii1I / Oooo0O0oo00oO
    if 2 - 2: iIi1i1ii1 % oOo0O0Ooo - OooOO000
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 79 - 79: ii / Ii1I . o0o00Oo0O
def ooo ( url ) :
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
 if 79 - 79: O0oOO0 - IIiIiII11i
def Ii1iiI1 ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for IiiIi1III in o0O0OOO0Ooo :
  o0ooOOoO0oO0 = IiiIi1III
 oOoooo000Oo00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in oOoooo000Oo00 :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10007 , o0ooOOoO0oO0 )
  if 86 - 86: ooOoO0O00 / IIi * oOo0O0Ooo
  if 67 - 67: Ii1I * Ii1I / O0oOO0 * ii + OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: ooOoO0O00
def iIi1ooo0Oooooo ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   Ooi1IIii11i1I1 ( url )
   if 12 - 12: ooOoO0O00 / Oooo0O0oo00oO % OOoOoo * iIi1i1ii1 * o0o00Oo0O * iI11I1II1I1I
   if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * O0oOO0 . ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 54 - 54: o0o00Oo0O / iIi1i1ii1 % OOoOoo * ooOoO0O00 * o0o00Oo0O
def Ooi1IIii11i1I1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
  if 48 - 48: I11i . O0oOO0 % OOooOOo - OOooOOo
  if 33 - 33: oo0oO00 % IIiIiII11i + oO0o
  if 93 - 93: ooOoO0O00 . iIi1i1ii1 / oOo0O0Ooo + iIi1i1ii1
def II1i11I ( ) :
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , OO0o , '' )
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - iiII11i1I1IIi . I11i
def Oooooooo00o00 ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  if 'elete' in Oo0OO :
   pass
  else :
   IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 222 , IiiIi1III )
   if 100 - 100: OooOO000 % IIiIiII11i . IIi % oO0o + Ii1I
def o0oOo0OO ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0oo00oOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , I1iOO0O0O , i1iII1IiiIiI1 in OO0oo00oOO :
  for o0O00oOoo in I1iOO0O0O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1i1iIII11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for ooO0oOOooOo0 , Oo0OO in i1i1iIII11i :
    if 'tube' in ooO0oOOooOo0 :
     pass
    elif 'stage' in ooO0oOOooOo0 :
     IIIII1 ( '[COLOR' + iiI1IiI + ']' + I1iOO0O0O + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiiIi1III , )
    elif 'vee' in ooO0oOOooOo0 :
     pass
     if 40 - 40: iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
def oOoo0ooOoo ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0oo00oOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , I1iOO0O0O , i1iII1IiiIiI1 in OO0oo00oOO :
  i1i1iIII11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for ooO0oOOooOo0 , Oo0OO in i1i1iIII11i :
   if 'tube' in ooO0oOOooOo0 :
    pass
   elif 'stage' in ooO0oOOooOo0 :
    IIIII1 ( '[COLOR' + iiI1IiI + ']' + I1iOO0O0O + '   -   ' + Oo0OO + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiiIi1III )
   elif 'vee' in ooO0oOOooOo0 :
    pass
    if 52 - 52: oO0o * ii
    if 12 - 12: o0o00Oo0O + iIi1i1ii1 * ooOoO0O00 . oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: OooOO000 - I11i - Oooo0O0oo00oO
def i1i1i1I ( url ) :
 I1 = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOoo000 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOoo000 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOoo000 :
  III111i11IiI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 28 - 28: iI11I1II1I1I
  if 7 - 7: I11i % iIi1i1ii1 * OOooOOo
  if 58 - 58: iIi1i1ii1 / oo0oO00 + IIiIiII11i % iiII11i1I1IIi - ii
  if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * O0oOO0
  if 30 - 30: oo0oO00 % OOooOOo / Ii1I * o0o00Oo0O * IIi . oOo0O0Ooo
  if 46 - 46: OOooOOo - o0o00Oo0O
  if 70 - 70: oo0oO00 + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * oo0oO00
def iIIiIiI1I1 ( ) :
 if 49 - 49: I11i
 I11iiI ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 I11iiI ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 40 - 40: IIi
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 68 - 68: I1ii11iIi11i
def ii111I11Ii ( ) :
 I11iiI ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 I11iiI ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 6 - 6: IIi
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def OooO0O ( ) :
 if 20 - 20: iIi1i1ii1 / iiII11i1I1IIi % ii / iI11I1II1I1I + oOo0O0Ooo
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 oO0oiIiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 46 - 46: iiII11i1I1IIi
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  I1 = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , iiI11ii1I1 , Oo0OO in o00oooO0Oo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    Ii11IiIiiii1 ( Oo0OO , ooO0oOOooOo0 , 222 , IiIIi1 , iiI11ii1I1 , Oo0 )
    if 60 - 60: oOo0O0Ooo % O0oOO0 / I11i % O0oOO0 * Ii / iiII11i1I1IIi
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 34 - 34: OooOO000 - Oooo0O0oo00oO
    if 25 - 25: O0oOO0 % oOo0O0Ooo + Ii + o0o00Oo0O * ii
def ooO0 ( ) :
 if 94 - 94: oo0oO00 . oOo0O0Ooo
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 oO0oiIiI = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 73 - 73: ooOoO0O00 / IIiIiII11i
 for ooIiI11i1I11111 in oO0oiIiI :
  I1i1I = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  I1 = Oo0OoO00oOO0o ( I1i1I )
  o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , Oo0 , ooO0oOOooOo0 , IiiIi1III , iiI11ii1I1 , OOooO0oo0o00o in o00oooO0Oo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    I11iiI ( Oo0OO , ooO0oOOooOo0 , OOooO0oo0o00o , IiiIi1III , iiI11ii1I1 , Oo0 )
    if 17 - 17: oo0oO00 - iiII11i1I1IIi % IIi
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 2 - 2: IIi * Ii1I * ii
    if 73 - 73: OOooOOo + I1ii11iIi11i
def oOoi1I111II ( ) :
 if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
 OOoO = O0 ( oOOoo0Oo + 'spongemain.php' )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , Oo0 , ooO0oOOooOo0 , IiiIi1III , iiI11ii1I1 , OOooO0oo0o00o in o00oooO0Oo :
  I11iiI ( Oo0OO , ooO0oOOooOo0 , OOooO0oo0o00o , IiiIi1III , iiI11ii1I1 , Oo0 )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def III11I11ii ( url ) :
 if 82 - 82: Oooo0O0oo00oO % IIiIiII11i - Oooo0O0oo00oO + IIiIiII11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0O0OO0OoO0 = ( '%s%s' % ( iIIiI11iI1Ii1 , url ) )
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in o00oooO0Oo :
  o00oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
  for OO00 in o00oo :
   if OO00 == url :
    Oo0OO = ( '[COLORred]Watched - [/COLOR]' + Oo0OO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  Ii11IiIiiii1 ( Oo0OO , url , 222 , IiIIi1 , i1i1iII1 , Oo0 )
  if 70 - 70: oo0oO00 - I1ii11iIi11i / ii % ii
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 95 - 95: ii % ii . IIi
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: O0oOO0 + iIi1i1ii1 - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
  if 68 - 68: o0o00Oo0O
def o0oOoO00 ( url ) :
 if 94 - 94: oO0o + iIi1i1ii1 + OOoOoo
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , Oo0 , url , IiiIi1III , iiI11ii1I1 , OOooO0oo0o00o in o00oooO0Oo :
  I11iiI ( Oo0OO , url , OOooO0oo0o00o , IiiIi1III , iiI11ii1I1 , Oo0 )
  if 82 - 82: I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / Oooo0O0oo00oO + iIi1i1ii1 % iI11I1II1I1I
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 61 - 61: Oooo0O0oo00oO / I1ii11iIi11i % Oooo0O0oo00oO - oO0o + OOoOoo / OOoOoo
  if 82 - 82: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: oO0o / oO0o - o0o00Oo0O - OooOO000 + OooOO000
def Ii11IiIiiii1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 99 - 99: oo0oO00 * ii / I11i . iIi1i1ii1 - iI11I1II1I1I - IIi
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  Oo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = False )
 return o00ooO00O
 if 31 - 31: iIi1i1ii1 - oO0o / Oooo0O0oo00oO . ooOoO0O00 / IIi
def I11iiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 66 - 66: oO0o
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  Oo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = True )
 return o00ooO00O
if 72 - 72: OooOO000
if 91 - 91: IIiIiII11i / iIi1i1ii1 + iI11I1II1I1I . oo0oO00 - o0o00Oo0O
if 70 - 70: IIi * O0oOO0 - oo0oO00 + I1ii11iIi11i % Ii1I - iIi1i1ii1
if 81 - 81: o0o00Oo0O . o0o00Oo0O
if 75 - 75: iI11I1II1I1I % iIi1i1ii1 + Ii1I * o0o00Oo0O . iiII11i1I1IIi - OOoOoo
if 32 - 32: IIi % O0oOO0 - ooOoO0O00
if 40 - 40: iI11I1II1I1I + iiII11i1I1IIi * OOooOOo + O0oOO0
if 15 - 15: oo0oO00 % oOo0O0Ooo - iI11I1II1I1I * OOoOoo
if 71 - 71: OOooOOo % I1ii11iIi11i % OOoOoo
if 34 - 34: oo0oO00 / oo0oO00 % iIi1i1ii1 . OOooOOo / I1ii11iIi11i
if 99 - 99: OOoOoo * oOo0O0Ooo - OOoOoo % IIi
if 40 - 40: Oooo0O0oo00oO / iIi1i1ii1 / iI11I1II1I1I + IIi
if 59 - 59: oo0oO00 * ii + Oooo0O0oo00oO . iI11I1II1I1I / ooOoO0O00
if 75 - 75: oo0oO00 . Oooo0O0oo00oO - iI11I1II1I1I * oO0o * iiII11i1I1IIi
if 93 - 93: OOoOoo
def iII1IIiiI11II ( string ) :
 if Oo0oOOo == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 70 - 70: IIi - Oooo0O0oo00oO * Oooo0O0oo00oO / iI11I1II1I1I + o0o00Oo0O
def IiIIi11i ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 IIii11i = [ ]
 try :
  if 82 - 82: Ii1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  iII1IIiiI11II ( 'Making Favorites File' )
  IIii11i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Oo0o = open ( I1IIiiIiii , "w" )
  Oo0o . write ( json . dumps ( IIii11i ) )
  Oo0o . close ( )
 else :
  iII1IIiiI11II ( 'Appending Favorites' )
  Oo0o = open ( I1IIiiIiii ) . read ( )
  OOO00o0 = json . loads ( Oo0o )
  OOO00o0 . append ( ( name , url , iconimage , fanart , mode ) )
  O0Oooo = open ( I1IIiiIiii , "w" )
  O0Oooo . write ( json . dumps ( OOO00o0 ) )
  O0Oooo . close ( )
  if 97 - 97: Ii1I / Ii1I / iI11I1II1I1I % ooOoO0O00 . Ii1I . iIi1i1ii1
  if 4 - 4: I1ii11iIi11i - oO0o - Ii * OooOO000 / IIi - Oooo0O0oo00oO
def II1IIii1ii ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  IIii11i = [ ]
  iII1IIiiI11II ( 'Making Favorites File' )
  IIii11i . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Oo0o = open ( I1IIiiIiii , "w" )
  Oo0o . write ( json . dumps ( IIii11i ) )
  Oo0o . close ( )
 else :
  IIiIiIiiI1Iii = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  Ii111iII = len ( IIiIiIiiI1Iii )
  for Oo0OoOo in IIiIiIiiI1Iii :
   Oo0OO = Oo0OoOo [ 0 ]
   ooO0oOOooOo0 = Oo0OoOo [ 1 ]
   IiIIi1 = Oo0OoOo [ 2 ]
   try :
    iiIIIi1i = Oo0OoOo [ 3 ]
    if iiIIIi1i == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     iiIIIi1i = IiIIi1
    else :
     iiIIIi1i = iiI11ii1I1
   try : iIi1i1i1II11I = Oo0OoOo [ 5 ]
   except : iIi1i1i1II11I = None
   try : O0OO = Oo0OoOo [ 6 ]
   except : O0OO = None
   if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . oo0oO00
   if Oo0OoOo [ 4 ] == 0 :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , '' , IiIIi1 , iiI11ii1I1 , '' , 'fav' )
   else :
    I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , Oo0OoOo [ 4 ] , IiIIi1 , iiI11ii1I1 , '' , 'fav' )
    if 6 - 6: oo0oO00 * O0oOO0 / ii % IIi * I11i
def i11i11Iiii11i ( name ) :
 OOO00o0 = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for II11II1I in range ( len ( OOO00o0 ) ) :
  if OOO00o0 [ II11II1I ] [ 0 ] == name :
   del OOO00o0 [ II11II1I ]
   O0Oooo = open ( I1IIiiIiii , "w" )
   O0Oooo . write ( json . dumps ( OOO00o0 ) )
   O0Oooo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 52 - 52: Oooo0O0oo00oO * O0oOO0 + oo0oO00 * oo0oO00 % ooOoO0O00 % oo0oO00
 if 96 - 96: I11i * O0oOO0 - Oooo0O0oo00oO * I11i * ooOoO0O00
def OoOO0OOoo ( ) :
 I1IIIi1i = os . path . join ( O0O , 'addons.ini' )
 OooIii1I1iI = open ( I1IIIi1i , "w+" )
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 OooIii1I1iI . write ( r'[' + IiII + ']' + '\n' )
 for Oo0OO , IiiIi1III , oOo , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  oOoOo0 = ( Oo0OO + '=plugin://' + IiII + '/?url=' + ooO0oOOooOo0 + '&mode=10012&name=' + ( Oo0OO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( IiiIi1III ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( IiiIi1III ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OooIii1I1iI . write ( oOoOo0 + '\n' )
  if 19 - 19: OOooOOo . I11i . ii
  if 13 - 13: Oooo0O0oo00oO . I1ii11iIi11i / IIiIiII11i
def iiI1iIII1ii ( ) :
 OOoO = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 in o00oooO0Oo :
  IiIiIi ( '24/7' , ooO0oOOooOo0 , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 5 - 5: OooOO000 % ii . OOooOOo
def oO00o00 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def oOOOO ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def I1i11 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def OOooooO0o0O0 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0OO , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def oO0oo ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o00oooO0Oo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  o0OIiII ( Oo0OO , ooO0oOOooOo0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 52 - 52: iIi1i1ii1 % OOoOoo
  if 25 - 25: oo0oO00 / oo0oO00 % ii - Ii1I * O0oOO0
def i1oooOoOoOO ( ) :
 if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 5 - 5: oo0oO00
def iii1IiiiI1i1 ( ) :
 if 37 - 37: I1ii11iIi11i - ooOoO0O00 - iIi1i1ii1 + oo0oO00 . iI11I1II1I1I
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO , i1I in o00oooO0Oo :
  I1IiiiiI ( Oo0OO + '  -  ' + ( i1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 10023 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 59 - 59: ii - OooOO000 % I11i . oo0oO00 + ooOoO0O00 * oo0oO00
  if 5 - 5: IIiIiII11i - iIi1i1ii1
  if 86 - 86: iIi1i1ii1 * oo0oO00 + o0o00Oo0O * OooOO000 + Ii - Ii1I
def oOOO000o0O0O ( ) :
 if 28 - 28: ooOoO0O00 . Oooo0O0oo00oO
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
 if 88 - 88: oo0oO00 + oOo0O0Ooo - oo0oO00 / ii - Ii
def i11Ii1IiIIIi ( url ) :
 IIioo0OO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( IIioo0OO )
 o00oooO0Oo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 71 - 71: oO0o % oOo0O0Ooo - iiII11i1I1IIi . iiII11i1I1IIi
  if 22 - 22: OOoOoo / OOoOoo - IIi % oo0oO00 . Oooo0O0oo00oO + iIi1i1ii1
  if 64 - 64: ooOoO0O00 % Ii1I / IIi % ii
  if 24 - 24: OooOO000 + ii . iIi1i1ii1 / OOooOOo / oo0oO00
def ooOooOO0 ( ) :
 if 81 - 81: Ii + IIi % Ii - ooOoO0O00
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0O00oOoo ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( ooO0oOOooOo0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  if o0O00oOoo in Oo0OO . lower ( ) :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 9 - 9: O0oOO0
   if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
   if 16 - 16: Oooo0O0oo00oO
def oooO0o0oOoO ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for IiIi1I1ii111 , OoO , I11iii , Oo0OO in o00oooO0Oo :
  IIi111 = ( I11iii ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oO0o0o0O = ( OoO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I111ii1iI = 'Season ' + oO0o0o0O + 'Episode ' + IIi111 + Oo0OO
  i1IiI1ii1i ( I111ii1iI , IiIi1I1ii111 )
  if 39 - 39: Oooo0O0oo00oO + oO0o
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: Oooo0O0oo00oO % oO0o / OOooOOo
  if 54 - 54: I1ii11iIi11i % oO0o - Oooo0O0oo00oO - oo0oO00
def i1IiI1ii1i ( name , url ) :
 IiIi1I1ii111 = url
 o0I1iI111ii111i = name
 iii1i1iiiiIi = cloudflare . source ( IiIi1I1ii111 )
 o0O0OOO0Ooo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for oOoo000 , o00iI1Ii11iIiiI1 in o0O0OOO0Ooo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + o0I1iI111ii111i + o00iI1Ii11iIiiI1 + '[/COLOR]' , oOoo000 , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 15 - 15: oo0oO00 % Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: IIi + IIiIiII11i % ii
 if 89 - 89: IIi
def OO0O0OOo0O ( ) :
 if 51 - 51: iiII11i1I1IIi
 if 68 - 68: iiII11i1I1IIi - I11i * oO0o % OOoOoo . OOoOoo - iI11I1II1I1I
 if 22 - 22: ii / Ii1I % iiII11i1I1IIi * OOooOOo
 if 32 - 32: ii % O0oOO0 % iI11I1II1I1I / o0o00Oo0O
 if 61 - 61: IIiIiII11i . o0o00Oo0O - IIi - Ii1I / Ii - IIiIiII11i
 if 98 - 98: IIi - oOo0O0Ooo . Ii * I1ii11iIi11i
 if 29 - 29: IIi / OOoOoo % oo0oO00
 if 10 - 10: iI11I1II1I1I % ii % Ii1I
 if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * oo0oO00
 if 89 - 89: IIi - OOoOoo . oo0oO00 - OooOO000 - oOo0O0Ooo
 if 79 - 79: iIi1i1ii1 + iIi1i1ii1 + IIi
 if 39 - 39: o0o00Oo0O - ii
 if 63 - 63: iI11I1II1I1I % I11i * OOoOoo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 79 - 79: o0o00Oo0O
 if 32 - 32: IIiIiII11i . o0o00Oo0O + IIi / OOooOOo / iIi1i1ii1 / Oooo0O0oo00oO
def ii1I11iI ( url ) :
 I1 = O0 ( url )
 OOo0 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( OOo0 ) )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 85 - 85: Oooo0O0oo00oO + IIiIiII11i - Oooo0O0oo00oO * O0oOO0 - ooOoO0O00 % iiII11i1I1IIi
def IiIiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 47 - 47: OOooOOo
def Oo0000o ( url ) :
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
  if 33 - 33: OOooOOo * oo0oO00
  if 48 - 48: ii . OOooOOo
def oOIIIi11 ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooOo00O0 = 'http://www.watchseries.ac/search/' + o0O00oOoo . replace ( ' ' , '%20' )
 I1 = O0 ( oooOo00O0 )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'watch online' in Oo0OO :
   pass
  else :
   print ooO0oOOooOo0
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , IiiIi1III , '' , '' )
   if 26 - 26: OooOO000 . IIi + oOo0O0Ooo . OOooOOo + Oooo0O0oo00oO
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 17 - 17: Oooo0O0oo00oO + Ii + Ii1I % Oooo0O0oo00oO . O0oOO0
def I11iiIi1i1IIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO , I11iii , Oo0 in o00oooO0Oo :
  i11iiI1111 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( I11iii ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + i11iiI1111 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IiiIi1III , '' , Oo0 )
  if 46 - 46: oO0o . o0o00Oo0O * OOoOoo / I11i + ii
def i1Ii1i1I11III ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  i11iiI1111 = ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + i11iiI1111 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 36 - 36: IIi - ii . ii + Ii1I
def o0OoO0000oOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , IiiIi1III , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 42 - 42: OooOO000 % oO0o . Ii1I
def iiIIiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 OOo0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for OoO , OO0oo00oOO in OOo0 :
  o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OO0oo00oOO ) )
  for url , Oo0OO in o00oooO0Oo :
   i11iiI1111 = ( OoO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + i11iiI1111 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: iiII11i1I1IIi + oo0oO00 % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * iiII11i1I1IIi
class o0Oo ( ) :
 if 16 - 16: iiII11i1I1IIi % oOo0O0Ooo - OOoOoo
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 100 - 100: ii * O0oOO0
  i11iiI1111 = name
  self . Get_Sources ( ooO0oOOooOo0 , i11iiI1111 )
  if 83 - 83: iI11I1II1I1I - OOoOoo - OooOO000 / oO0o - o0o00Oo0O
  if 81 - 81: IIi - O0oOO0 * Ii1I / OooOO000
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O0 ( URL )
  o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
   self . Get_site_link ( URL , season_name )
   if 21 - 21: oO0o
 def Get_site_link ( self , url , season_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( I1 )
  o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  oOoooo000Oo00 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in o00oooO0Oo :
   self . main ( url , season_name )
  for url in o0O0OOO0Ooo :
   self . main ( url , season_name )
  for url in oOoooo000Oo00 :
   self . main ( url , season_name )
   if 63 - 63: oo0oO00 . o0o00Oo0O * oo0oO00 + iI11I1II1I1I
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   Ii1iIi = 'DACLIPS'
   if Ii1iIi in o0Oo . source_list :
    pass
   else :
    self . daclips ( url , season_name , Ii1iIi )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    Ii1iIi = 'FILEHOOT'
    if Ii1iIi in o0Oo . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , Ii1iIi )
   else :
    if 'thevideo.me' in url :
     Ii1iIi = 'THEVIDEO'
     if Ii1iIi in o0Oo . source_list :
      pass
     else :
      self . thevideo ( url , season_name , Ii1iIi )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      Ii1iIi = 'ALLMYVIDEOS'
      if Ii1iIi in o0Oo . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , Ii1iIi )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       Ii1iIi = 'VIDSPOT'
       if Ii1iIi in o0Oo . source_list :
        pass
       else :
        self . vidspot ( url , season_name , Ii1iIi )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        Ii1iIi = 'VODLOCKER'
        if Ii1iIi in o0Oo . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , Ii1iIi )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 79 - 79: Oooo0O0oo00oO % OooOO000 / O0oOO0 - iI11I1II1I1I - OOooOOo
         if 60 - 60: IIiIiII11i
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for iIiIi1I , Oo0OO in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 90 - 90: OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for iIiIi1I , Oo0OO in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % OooOO000 / iiII11i1I1IIi
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for iIiIi1I in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 18 - 18: ii
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for iIiIi1I in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 57 - 57: OOoOoo . OOooOOo * I11i - ii
 def daclips ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for iIiIi1I in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 75 - 75: Ii / I11i . iIi1i1ii1 . ooOoO0O00 . ooOoO0O00 / oo0oO00
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for iIiIi1I in o00oooO0Oo :
   self . Printer ( iIiIi1I , season_name , source_name )
   if 94 - 94: OOoOoo + oOo0O0Ooo
 def Printer ( self , Link , season_name , source_name ) :
  if 56 - 56: OOooOOo % I11i
  if Link in o0Oo . List :
   pass
  elif source_name in o0Oo . source_list :
   pass
  else :
   IIIII1 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   o0Oo . List . append ( Link )
   o0Oo . source_list . append ( source_name )
   if 40 - 40: Oooo0O0oo00oO / iIi1i1ii1
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 29 - 29: IIi - IIi / OOoOoo
   if 49 - 49: oo0oO00 + O0oOO0 % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
   if 4 - 4: IIiIiII11i - O0oOO0 % I1ii11iIi11i * Ii
   if 18 - 18: I1ii11iIi11i % o0o00Oo0O
   if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
def I1i111I ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 47 - 47: Ii1I * O0oOO0 + iI11I1II1I1I - O0oOO0 / iIi1i1ii1
def oO0ooo0O0Ooo ( url ) :
 I1IiiiiI ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OOoO )
 for iiI111i1 , url , IiIii11i1IIiI , I11iIIi , ii1i1I1 , OoOOo00 , Oo0o0ooO0ooo , oOOo0O00o , Oo0o , i111IIiIII1i , oooO0 in o00oooO0Oo :
  IiIii11i1IIiI = IiIii11i1IIiI
  if 'Arsenal' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'arsenal-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                                  ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Bournemouth' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'afc-bournemouth.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                       ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Burnley' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'KEGnQWW.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                                   ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Chelsea' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'chelsea.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                                  ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Crystal' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'CrystalPalace.0.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                       ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Everton' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'Everton.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                                   ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Hull' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'hull-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                                 ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Leicester' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                       ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Liverpool' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'liverpool-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                               ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Manchester City' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'city-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '               ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Manchester United' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + '91.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '          ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Middlesbrough' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                 ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Southampton' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'southampton-fc-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                   ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Stoke City' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'stoke-city.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                          ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Sunderland' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'sunderland-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                        ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Swansea' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'swansea-city-afc.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                    ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Tottenham' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '        ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Watford' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '                              ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'Bromwich' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '   ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  elif 'West Ham' in IiIii11i1IIiI :
   ooOO0OoO = oOOOo00O00oOo + 'west-ham.png'
   Oo0OO = '[COLOR' + iiI1IiI + ']' + iiI111i1 + ' - ' + IiIii11i1IIiI + '             ' + I11iIIi + '        ' + ii1i1I1 + '        ' + OoOOo00 + '        ' + Oo0o0ooO0ooo + '        ' + oOOo0O00o + '        ' + Oo0o + '        ' + i111IIiIII1i + '[/COLOR]'
  I1IiiiiI ( str ( Oo0OO ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , ooOO0OoO , ooOO0OoO , IiIii11i1IIiI )
  if 66 - 66: o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def I11iIiI1 ( description ) :
 IiIii11i1IIiI = description
 ooO0oOOooOo0 = ( 'http://www.fullmatchesandshows.com/?s=' + IiIii11i1IIiI ) . replace ( ' ' , '%20' )
 i1I1iiii1Ii11 ( ooO0oOOooOo0 )
 if 25 - 25: Ii / OOooOOo - OooOO000 / oO0o . I11i . I11i
def iI1 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o00oooO0Oo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0oOOooOo0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiiIi1III , OO0o , '' )
  if 43 - 43: Ii1I + I11i
def iI1iiiiiii ( url ) :
 I1 = O0 ( url )
 OOo0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for OOo0 in OOo0 :
  Oo00oo = re . compile ( '(.*?)</h2>' ) . findall ( str ( OOo0 ) )
  for oO0oO in Oo00oo :
   oO0oO = oO0oO
  o0ooo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( OOo0 ) )
  for IiI , IiiIi1III , time , ii11I in o0ooo :
   IiIIi1I1I11Ii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( ii11I )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + oO0oO + ' - ' + IiI + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IiiIi1III , OO0o , ( str ( IiIIi1I1I11Ii ) ) )
   if 97 - 97: ooOoO0O00 + iiII11i1I1IIi . OOoOoo - iiII11i1I1IIi
 Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if 53 - 53: o0o00Oo0O . oOo0O0Ooo
def o0oOOoO000 ( ) :
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
 if 86 - 86: iI11I1II1I1I - oo0oO00 % OOoOoo . Oooo0O0oo00oO * OOooOOo . ooOoO0O00
def O0o0O0 ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  OO0Oo00OO0oo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   OO0Oo00OO0oo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   IIIII1 ( '[COLOR' + iiI1IiI + ']' + OO0Oo00OO0oo + '[/COLOR]' , url , 10013 , IiiIi1III )
 for url , IiiIi1III , Oo0OO in o0O0OOO0Ooo :
  OO0Oo00OO0oo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   IIIII1 ( '[COLOR' + iiI1IiI + ']' + OO0Oo00OO0oo + '[/COLOR]' , url , 10013 , IiiIi1III )
def i1I1iiii1Ii11 ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 53 - 53: oO0o - OOoOoo + IIi
 if 29 - 29: Oooo0O0oo00oO + ii + O0oOO0 * oOo0O0Ooo - IIi / Ii
 if 5 - 5: o0o00Oo0O - oOo0O0Ooo
 if 44 - 44: IIiIiII11i . IIiIiII11i + Oooo0O0oo00oO * IIi
 if 16 - 16: IIiIiII11i
 if 100 - 100: o0o00Oo0O - ooOoO0O00
 if 48 - 48: O0oOO0 % OOoOoo + o0o00Oo0O
 for url , IiiIi1III , Oo0OO in o0O0OOO0Ooo :
  OO0Oo00OO0oo = Oo0OO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0OO :
   pass
  else :
   IIIII1 ( '[COLOR' + iiI1IiI + ']' + OO0Oo00OO0oo + '[/COLOR]' , url , 10013 , IiiIi1III )
   if 27 - 27: Ii1I / Oooo0O0oo00oO
def IiiIiiIIII ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for oOoo000 in o00oooO0Oo :
  oOoOOOOoO0 = ( oOoo000 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  III111i11IiI ( 'http:' + oOoOOOOoO0 )
  if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - IIi
  if 40 - 40: iiII11i1I1IIi . OOooOOo * o0o00Oo0O
  if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + oo0oO00 . Oooo0O0oo00oO
  if 74 - 74: ooOoO0O00
def Ii11ii1 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  IIIII1 ( Oo0OO , url , 8046 , IiiIi1III )
 for url in o0O0OOO0Ooo :
  IiIiIi ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def iiiIiiiI1I ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  III111i11IiI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 6 - 6: oO0o
def OO000OOOo0Oo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 75 - 75: IIiIiII11i + OOoOoo % Oooo0O0oo00oO + I1ii11iIi11i
def ii1I1IIii11 ( ) :
 IiIiIi ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 IiIiIi ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 IiIiIi ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OOoO = O00 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoOOoo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OOoO )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + IiiIi1III )
 for url in next :
  IiIiIi ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 65 - 65: Ii - OOoOoo * oo0oO00 + OOoOoo / iIi1i1ii1 + I11i
  if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % IIi % IIiIiII11i
def o0OOOO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   IIIII1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   IIIII1 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def OOoo0OOOo0o ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  url = ( url ) . replace ( '\/' , '/' )
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , '' )
  if 10 - 10: OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11i1i11IiIi1 ( name , url ) :
 I11i1I1Ii = 0
 name = name
 url = url
 ii1I = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  III111i11IiI ( url )
  if 26 - 26: ooOoO0O00 / iiII11i1I1IIi . iiII11i1I1IIi
  if 20 - 20: Oooo0O0oo00oO - iiII11i1I1IIi / I1ii11iIi11i * oO0o
  if 55 - 55: ii
  if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
  if 38 - 38: o0o00Oo0O
  if 79 - 79: ooOoO0O00 . O0oOO0
  if 34 - 34: OooOO000 * IIiIiII11i
  if 71 - 71: iIi1i1ii1
def o00OOo0o ( ) :
 OOoO = O00 ( 'http://documentarylovers.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  if 'genre' in ooO0oOOooOo0 :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , ooO0oOOooOo0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIiIo00O0oo0 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OOoO )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , IiiIi1III )
 for url in next :
  IiIiIi ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 91 - 91: Ii % OooOO000 * O0oOO0 - Ii1I . OooOO000
def iIo00oo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in o0O0OOO0Ooo :
  OOoo0OOOo0o ( url )
  if 78 - 78: iIi1i1ii1 - oo0oO00 % o0o00Oo0O - Oooo0O0oo00oO % oO0o
def i11IiIi ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000O0OO00oo = 'http://documentarylovers.com/?s=' + ( o0O00oOoo ) . replace ( ' ' , '+' )
 oOOO = O000O0OO00oo . lower ( )
 IiIiIo00O0oo0 ( oOOO )
 if 24 - 24: oo0oO00 / IIi * OOoOoo - Ii
def OoiIiiII ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def iII1I ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOoO )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  if 'films' in url :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + IiiIi1III )
 for url in o0O0OOO0Ooo :
  IiIiIi ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def o00oOOo0Oo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'rtd' in url :
   Oooo0o0oO ( url )
   if 82 - 82: OOoOoo
def Oooo0o0oO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OOoO )
 for O0o0O00Oo0o0 , file in o00oooO0Oo :
  url = ( 'https://rtd.rt.com' + O0o0O00Oo0o0 + file )
  III111i11IiI ( url )
  if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / iiII11i1I1IIi
  if 9 - 9: OOooOOo - iIi1i1ii1
def iiIi ( ) :
 I1 = O00 ( 'http://www.stream2watch.co/live-tv' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO , IiI111 in o00oooO0Oo :
  IiIiIi ( ( Oo0OO + '[COLOR' + iiI1IiI + ']' + IiI111 + '[/COLOR]' ) , ooO0oOOooOo0 , 8086 , IiiIi1III )
  if 82 - 82: oOo0O0Ooo % oO0o % oo0oO00 + oo0oO00
def i1111I ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8087 , IiiIi1III )
  if 58 - 58: ii - oo0oO00 + iI11I1II1I1I * Ii
def OoOiII11IiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  iII1I1i ( url , Oo0OO )
  if 6 - 6: O0oOO0 / o0o00Oo0O / IIi / iIi1i1ii1 / O0oOO0 . iI11I1II1I1I
def iII1I1i ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  print url
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 62 - 62: iI11I1II1I1I
def IIi1i1ii11I1 ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooO0oOOooOo0 , 3002 , 'http://www.solie.org/alibrary/' + IiiIi1III )
def oOoO0OO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiiIi1III )
def o0OOO ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 Iii11iI1I = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , Oo0OO in Iii11iI1I :
  IiIiIi ( '[COLOR' + iiI1IiI + ']Season- ' + Oo0OO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , IiiIi1III , Oo0OO in o0O0OOO0Ooo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiiIi1III )
def OOo0o0O0 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  iiIIII11IiIII ( url )
def iiIIII11IiIII ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
  if 27 - 27: ooOoO0O00 / IIi / OOooOOo + iI11I1II1I1I % oo0oO00 / iIi1i1ii1
def Ooo0O0oooo ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def i1IIIII1 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( "v.src = '([^']*)';" ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11IIIiIi11 ( url )
  if 13 - 13: oO0o % iI11I1II1I1I - IIiIiII11i / oOo0O0Ooo
def OOooO0o0 ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def iII111iiiI11i ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'mp4' in url :
   III111i11IiI ( url )
 for url in o0O0OOO0Ooo :
  yt . PlayVideo ( url )
  if 4 - 4: OOoOoo % iIi1i1ii1 . OooOO000
def oO0o00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooO0oOOooOo0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def Oo0OOOO0oOoo0 ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for Oo0OO , url in o00oooO0Oo :
  if '(Free Access)' in Oo0OO :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def O0OIIII1i ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , Oo0OO , url in o00oooO0Oo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IiiIi1III , iiI11ii1I1 , '' )
  if 30 - 30: iIi1i1ii1 - iiII11i1I1IIi - oO0o
def ii11 ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  oOOooooO ( 'http://watchxxxfree.com/categories' )
 if O0oO0 == 1 :
  o000Ooo00o00O ( 'http://www.perfectgirls.net' )
 if O0oO0 == 2 :
  ooo0O0O0oo0 ( 'http://www.xvideos.com/best' )
 if O0oO0 == 3 :
  oo000oO ( 'http://www.xvideos.com/best' )
 if O0oO0 == 4 :
  ooo0O0O0oo0 ( 'http://www.xvideos.com/best' )
 if O0oO0 == 5 :
  ooo0O0O0oo0 ( 'http://www.xvideos.com/verified/videos' )
 if O0oO0 == 6 :
  IiIiII11i1 ( 'http://www.xvideos.com/tags' )
 if O0oO0 == 7 :
  Ii1I1iIiiI1 ( 'http://www.xvideos.com/porn' )
 if O0oO0 == 8 :
  o00i111iiIiiIiI ( )
  if 59 - 59: Oooo0O0oo00oO + oOo0O0Ooo / IIiIiII11i / OOooOOo
  if 80 - 80: OOooOOo + iI11I1II1I1I . iIi1i1ii1
  if 76 - 76: oOo0O0Ooo * Oooo0O0oo00oO
  if 12 - 12: iI11I1II1I1I / oo0oO00 % IIi
  if 49 - 49: oO0o + IIiIiII11i / iIi1i1ii1 - o0o00Oo0O % IIi
  if 27 - 27: oO0o + I1ii11iIi11i
  if 92 - 92: oOo0O0Ooo % iiII11i1I1IIi
  if 31 - 31: ii - O0oOO0 / OooOO000
  if 62 - 62: Ii - oo0oO00
def o00OOOOooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  if 'ch' in url :
   iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def o0oo00oo0oO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 ii1ii = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for Oo0OO , url in ii1ii :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def Ii1iii11I ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   Ii11iIiiI ( url )
def iiII ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
def oOOooooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO , oOO0OO0O in o00oooO0Oo :
  if 'category' in url :
   iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]   ' + oOO0OO0O + '[/COLOR]' , url , 90006 , IiiIi1III , oOOOo00O00oOo + 'Jizbox.png' , '' )
def iII1IiiIIIIii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 ii1ii = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , IiiIi1III , '' , '' )
 for url in ii1ii :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oOOOIii1IiiII1Ii1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   Ii11iIiiI ( url )
def Ii11iIiiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  III111i11IiI ( url )
def o000Ooo00o00O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , oOO0OO0O in o00oooO0Oo :
  if 'category' in url :
   iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORorange]' + oOO0OO0O + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def iiiIIi ( url ) :
 I1 = O0 ( url )
 IiIi1I1ii111 = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 ii1ii = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , IiiIi1III , '' , '' )
 for url in ii1ii :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , IiIi1I1ii111 + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OOoOo0O00oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in o00oooO0Oo :
  oo0oO0oOo0O ( 'http://www.perfectgirls.net' + url )
def oo0oO0oOo0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in o00oooO0Oo :
  III111i11IiI ( 'http://' + url )
def Ii1I1iIiiI1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , oOO0OO0O in o00oooO0Oo :
  iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + oOO0OO0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiIiII11i1 ( url ) :
 I1 = O0 ( url )
 ii1ii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in ii1ii :
  iI11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , Oo0OO , oOO0OO0O in o00oooO0Oo :
  iI11 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - No of Videos : [COLORorange]' + ( oOO0OO0O + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 75 - 75: IIiIiII11i + IIiIiII11i + Oooo0O0oo00oO * I11i
def ooOoO0OoO ( url ) :
 I1 = O0 ( url )
 ii1ii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in ii1ii :
  iI11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO , oOo00OoO0O in o00oooO0Oo :
  iI11 ( Oo0OO + '--' + ( oOo00OoO0O ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IiiIi1III ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 94 - 94: iIi1i1ii1 % I11i . Ii % ii + OOoOoo . oOo0O0Ooo
  if 19 - 19: oOo0O0Ooo - OOooOOo . I1ii11iIi11i . ooOoO0O00 - O0oOO0
def ooo0O0O0oo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , url , Oo0OO , I1IIII1ii , o0OoOOoOOoo in o00oooO0Oo :
  iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + o0OoOOoOOoo + ' - [COLORred]' + I1IIII1ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , IiiIi1III , IiiIi1III , o0OoOOoOOoo + ' - ' + I1IIII1ii )
 oo0O0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in oo0O0 :
  iI11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 34 - 34: IIiIiII11i - iIi1i1ii1 % OOooOOo % IIi / OOoOoo
def oo000oO ( url ) :
 I1 = O0 ( url )
 OOo0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 ii1ii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in ii1ii :
  iI11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( OOo0 ) )
 for url , Oo0OO in o00oooO0Oo :
  if '/c/' in url :
   iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - Oooo0O0oo00oO
   if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def o00i111iiIiiIiI ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00000OO00OO = ( o0O00oOoo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 oOOO = O00000OO00OO . lower ( )
 I1iI1 = 'http://www.xvideos.com/?k=' + oOOO
 print I1iI1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O0 ( I1iI1 )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , ooO0oOOooOo0 , Oo0OO , I1IIII1ii , o0OoOOoOOoo in o00oooO0Oo :
  iI11 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[COLORgreen] - Porn Quality : [COLORorange]' + o0OoOOoOOoo + ' - [COLORred]' + I1IIII1ii + '[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10108 , IiiIi1III , IiiIi1III , o0OoOOoOOoo + ' - ' + I1IIII1ii )
 oo0O0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for ooO0oOOooOo0 in oo0O0 :
  iI11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 35 - 35: I1ii11iIi11i
def IiI11Ii1iI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 oOoooo000Oo00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'http' in url :
   IIIII1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in o0O0OOO0Ooo :
  if 'http' in url :
   IIIII1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in oOoooo000Oo00 :
  if 'http' in url :
   IIIII1 ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 53 - 53: oOo0O0Ooo
def i1Iii ( url ) :
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 import urlresolver
 try : oO0o0O0Ooo0o . play ( url )
 except : pass
 if 48 - 48: Oooo0O0oo00oO
 if 26 - 26: iiII11i1I1IIi * OooOO000 * O0oOO0 * OOooOOo
def I1ii1i11iI1 ( ) :
 if 6 - 6: o0o00Oo0O . OOoOoo - O0oOO0 / Ii
 if 84 - 84: oo0oO00 / Ii1I * I11i * oO0o * Oooo0O0oo00oO * o0o00Oo0O
 if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
 if 75 - 75: IIiIiII11i . oOo0O0Ooo + Oooo0O0oo00oO - OOooOOo - o0o00Oo0O . oo0oO00
 if 19 - 19: IIi * ooOoO0O00 % o0o00Oo0O + oo0oO00
 if 25 - 25: OooOO000 - IIi / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
 if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + O0oOO0 + O0oOO0 + iiII11i1I1IIi
 if 4 - 4: I11i + oo0oO00 / iiII11i1I1IIi + ooOoO0O00 % I11i % iiII11i1I1IIi
 if 80 - 80: IIi
 if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def oOo0O0 ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , IiiIi1III )
 for url in next :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def iIi1iI ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 iIIII1iII1i = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III in iIIII1iII1i :
  IiiIi1III = IiiIi1III
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 8092 , IiiIi1III )
 for url in next :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 98 - 98: OooOO000 % oO0o - OOoOoo % Ii + OooOO000 - iIi1i1ii1
def O00oIi11Iiii1iiii ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 10 - 10: iiII11i1I1IIi % I1ii11iIi11i
  if 48 - 48: Oooo0O0oo00oO + OooOO000 % Oooo0O0oo00oO
  if 84 - 84: o0o00Oo0O % IIi . IIi . iiII11i1I1IIi * oo0oO00
  if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
OO0O00 = '{PQ},' ; ooOO = '{SC},' ; oO0o0 = '{XG},' ; i1Ii1i11ii = '{JP},' ; oO0O0oo = '{HW},' ; OOOOOOO00OO = '{RT},'
def i1O0 ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0Oo00 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 46 - 46: IIiIiII11i
 I11iiIi1i1 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i11iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 OOooOo0ooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Oo00o00 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OoOo0O0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0O00oOoo
 I1o0 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I1IiiiiI1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I11i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 ooOooO = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 98 - 98: Ii / oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 7 - 7: iiII11i1I1IIi % Ii1I
 if 64 - 64: OooOO000 + Ii
 Iiii = Oo0OoO00oOO0o ( I11iiIi1i1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( i11iIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iI1i11i = Oo0OoO00oOO0o ( OOooOo0ooo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIIIi1Iii1iIi = Oo0OoO00oOO0o ( OoOo0O0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ii1IIi1iI1ii1 = Oo0OoO00oOO0o ( I1o0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 o00iIIiIi111iI = Oo0OoO00oOO0o ( I1IiiiiI1i1I )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 II1I1ii = Oo0OoO00oOO0o ( I11i1I1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 oo0OO0O = Oo0OoO00oOO0o ( ooOooO )
 if 64 - 64: O0oOO0 . Ii1I * OooOO000 % oOo0O0Ooo
 if 25 - 25: o0o00Oo0O + oo0oO00 + Oooo0O0oo00oO * Ii1I
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for OO0Iii1iIiI111Ii , Oo0OO in o00oooO0Oo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooO0oOOooOo0 + OO0Iii1iIiI111Ii ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 61 - 61: ii * OOooOOo
    if 97 - 97: Ii
    if 68 - 68: iIi1i1ii1 * oO0o . oo0oO00 / IIi . I11i - Ii
    if 49 - 49: I1ii11iIi11i / IIi % oo0oO00 + O0oOO0 - oO0o
    if 13 - 13: IIiIiII11i
    if 83 - 83: ii . oOo0O0Ooo + IIi * o0o00Oo0O / O0oOO0
    if 8 - 8: ooOoO0O00 + IIiIiII11i / IIi + Ii1I % IIi - iI11I1II1I1I
 if Iiii != 'Failed' :
  oOoooo000Oo00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for OO0Iii1iIiI111Ii , Oo0OO in oOoooo000Oo00 :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I11iiIi1i1 + OO0Iii1iIiI111Ii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  iIi1iIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in iIi1iIi11ii :
   if o0O00oOoo in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 39 - 39: ooOoO0O00 . Ii1I / oo0oO00 / oo0oO00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iI1i11i != 'Failed' :
  ooOo0oO0O = [ ]
  I1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1i11i )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in I1i1 :
   if o0O00oOoo in Oo0OO . lower ( ) :
    if Oo0OO in ooOo0oO0O :
     pass
    else :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooO0oOOooOo0 , 1016 , IiIIi1 , i1i1iII1 , Oo0 )
     ooOo0oO0O . append ( Oo0OO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if IIIIi1Iii1iIi != 'Failed' :
  ii11o00000O = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIIIi1Iii1iIi )
  for ooO0oOOooOo0 , IiiIi1III , Oo0OO in ii11o00000O :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooO0oOOooOo0 , 7067 , IiiIi1III )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 23 - 23: I1ii11iIi11i - o0o00Oo0O
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: Ii1I
    if 54 - 54: OOoOoo * Ii1I . IIiIiII11i / Oooo0O0oo00oO % Oooo0O0oo00oO
    if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % OooOO000
    if 53 - 53: ooOoO0O00
    if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
    if 9 - 9: ooOoO0O00 - OOooOOo
    if 57 - 57: iI11I1II1I1I * IIi * iiII11i1I1IIi / O0oOO0
    if 46 - 46: IIi
    if 61 - 61: I11i / OOoOoo - IIiIiII11i
 if o00iIIiIi111iI != 'Failed' :
  oOoO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00iIIiIi111iI )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in oOoO0 :
   if o0O00oOoo in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 222 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 95 - 95: OOoOoo / ii + o0o00Oo0O
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if II1I1ii != 'Failed' :
  iIIIi11iIiIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1I1ii )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in iIIIi11iIiIii :
   if o0O00oOoo in Oo0OO . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 222 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 61 - 61: ii . IIi % O0oOO0 * ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: IIi - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if oo0OO0O != 'Failed' :
  oOO0O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo0OO0O )
  for ooO0oOOooOo0 , IiIIi1 , Oo0OO in oOO0O0O :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , IiIIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 81 - 81: Ii % ooOoO0O00 % IIiIiII11i % oOo0O0Ooo + oOo0O0Ooo % Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 oO0oiIiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 20 - 20: iIi1i1ii1 - iI11I1II1I1I
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  i1I1iI1 = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  if i1I1iI1 != 'Failed' :
   oOOoO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1iI1 )
   for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in oOOoO :
    if o0O00oOoo in Oo0OO . lower ( ) :
     o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , 222 , IiIIi1 , i1i1iII1 , Oo0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 28 - 28: iI11I1II1I1I * oo0oO00 . oOo0O0Ooo
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 78 - 78: ii . ii / o0o00Oo0O
 oO0oiIiI = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 25 - 25: IIiIiII11i % IIiIiII11i - IIi . o0o00Oo0O
 if 79 - 79: iIi1i1ii1 / oO0o * ii * OOooOOo + oOo0O0Ooo
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = o0Oo00 + ooIiI11i1I11111
  O0ooO = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  if O0ooO != 'Failed' :
   iIOO = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0ooO )
   for OO0Iii1iIiI111Ii , Oo0OO in iIOO :
    if o0O00oOoo in Oo0OO . lower ( ) :
     IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0Oo00 + ooIiI11i1I11111 + OO0Iii1iIiI111Ii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 4 - 4: IIi % Ii1I + oo0oO00 - Ii1I
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 98 - 98: IIi - o0o00Oo0O * O0oOO0 * IIi * IIi
     if 44 - 44: iIi1i1ii1 + oo0oO00
def iiI11i1II ( ) :
 if 66 - 66: O0oOO0
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 if 34 - 34: iiII11i1I1IIi % Ii + Ii - iiII11i1I1IIi
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( o0O00oOoo ) . replace ( ' ' , '%20' )
 IiIi1I1ii111 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I11iiIi1i1 = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 i11iIi = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OOooOo0ooo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOOO ) . replace ( ' ' , '+' )
 Oo00o00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OoOo0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 I1o0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 2 - 2: IIiIiII11i + ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 68 - 68: Oooo0O0oo00oO + IIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( IiIi1I1ii111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = Oo0OoO00oOO0o ( I11iiIi1i1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( i11iIi )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iI1i11i = cloudflare . source ( OOooOo0ooo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0ooO = Oo0OoO00oOO0o ( Oo00o00 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIIIi1Iii1iIi = Oo0OoO00oOO0o ( OoOo0O0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 ii1IIi1iI1ii1 = Oo0OoO00oOO0o ( I1o0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 58 - 58: iIi1i1ii1 * IIi . ooOoO0O00
 if ii1IIi1iI1ii1 != 'Failed' :
  i11I1iiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ii1IIi1iI1ii1 )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in i11I1iiii :
   if oOOO in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
    if 31 - 31: OooOO000 / I1ii11iIi11i / iI11I1II1I1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: I1ii11iIi11i * oo0oO00 + oo0oO00
 if IIIIi1Iii1iIi != 'Failed' :
  ii11o00000O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIIi1Iii1iIi )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in ii11o00000O :
   if oOOO in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 1016 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 39 - 39: ooOoO0O00 + iiII11i1I1IIi + o0o00Oo0O
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % O0oOO0 + oOo0O0Ooo % OOoOoo / IIi
    if 36 - 36: OOooOOo . Ii
    if 81 - 81: I1ii11iIi11i * iiII11i1I1IIi * oO0o
    if 85 - 85: o0o00Oo0O * O0oOO0
    if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . IIi % iiII11i1I1IIi . iIi1i1ii1
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 67 - 67: ii + OooOO000 / OOoOoo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for IiiIi1III , ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
   if oOOO in Oo0OO . lower ( ) :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , IiiIi1III , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 75 - 75: iIi1i1ii1 / ii . oOo0O0Ooo + OooOO000 - IIiIiII11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: iIi1i1ii1 / iIi1i1ii1 . Ii * Ii1I + I11i
    if 16 - 16: iIi1i1ii1
    if 10 - 10: OOooOOo . iIi1i1ii1 * iI11I1II1I1I - O0oOO0 - OOooOOo / OooOO000
    if 13 - 13: O0oOO0 + OOooOOo % iIi1i1ii1 % ii
    if 22 - 22: OooOO000
    if 23 - 23: o0o00Oo0O
    if 41 - 41: ooOoO0O00 . Oooo0O0oo00oO / OOoOoo / I11i % iIi1i1ii1 - IIi
    if 14 - 14: Ii1I - Ii * OooOO000
    if 39 - 39: ii
    if 19 - 19: Ii
    if 80 - 80: oOo0O0Ooo
    if 58 - 58: O0oOO0 + Ii1I % OOooOOo
    if 22 - 22: iI11I1II1I1I - IIi / oOo0O0Ooo * iIi1i1ii1
    if 26 - 26: I11i + Oooo0O0oo00oO - I11i + I1ii11iIi11i . O0oOO0
    if 97 - 97: ooOoO0O00
    if 46 - 46: Ii1I
    if 30 - 30: oO0o / o0o00Oo0O * I11i * OooOO000 + ii * iiII11i1I1IIi
    if 23 - 23: oo0oO00
    if 36 - 36: iIi1i1ii1 . iiII11i1I1IIi - ooOoO0O00 + OooOO000
 if Iiii != 'Failed' :
  oOoooo000Oo00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for Oo0OO in oOoooo000Oo00 :
   if oOOO in Oo0OO . lower ( ) :
    IiIiIi ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I11iiIi1i1 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 54 - 54: ii . O0oOO0 - iiII11i1I1IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  iIi1iIi11ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for Oo0OO in iIi1iIi11ii :
   if oOOO in Oo0OO . lower ( ) :
    IiIiIi ( ( Oo0OO + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i11iIi + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 76 - 76: OooOO000
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iI1i11i != 'Failed' :
  I1i1 = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iI1i11i )
  for ooO0oOOooOo0 , IiiIi1III , Oo0OO in I1i1 :
   if oOOO in Oo0OO . lower ( ) :
    IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source - Dizi[/COLOR]' , ooO0oOOooOo0 , 8062 , IiiIi1III )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 61 - 61: OOoOoo / IIiIiII11i * OOoOoo * OOooOOo * OooOO000 . Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if O0ooO != 'Failed' :
  iIOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooO )
  for ooO0oOOooOo0 , IiIIi1 , Oo0 , i1i1iII1 , Oo0OO in iIOO :
   if oOOO in Oo0OO . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '- Source Scooby[/COLOR]' ) , ooO0oOOooOo0 , 1016 , IiIIi1 , i1i1iII1 , Oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 26 - 26: OooOO000 / OOoOoo - oO0o . iI11I1II1I1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: OOoOoo % IIi / I1ii11iIi11i - iiII11i1I1IIi / o0o00Oo0O
 oo00oO00oooo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if O0ooO != 'Failed' :
  for ooIiI11i1I11111 in oo00oO00oooo :
   Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
   II1I1ii = O0 ( Ii1IIIIIIiI1 )
   if II1I1ii != 'Failed' :
    iIIIi11iIiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II1I1ii )
    for Oo0OO , Oo0 , ooO0oOOooOo0 , IiiIi1III , iiI11ii1I1 , OOooO0oo0o00o in iIIIi11iIiIii :
     if oOOO in Oo0OO . lower ( ) :
      I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , OOooO0oo0o00o , IiiIi1III , iiI11ii1I1 , Oo0 )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 63 - 63: IIiIiII11i - oo0oO00 . OOooOOo
      Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
      if 8 - 8: oOo0O0Ooo * OOoOoo / iIi1i1ii1 + OOooOOo . iIi1i1ii1 - Oooo0O0oo00oO
      if 80 - 80: iI11I1II1I1I / O0oOO0 * I1ii11iIi11i - Oooo0O0oo00oO * iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0ooOO0 ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o0O00oOoo ) . replace ( ' ' , '+' )
 if 99 - 99: iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 81 - 81: Ii1I + Oooo0O0oo00oO
 if I1 != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IIIII1 ( ( Oo0OO + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + ooO0oOOooOo0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 11 - 11: Ii1I % I1ii11iIi11i * OooOO000 - O0oOO0 + Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
Oo0O00OO = '{ZH},' ; o0OO00O00oO = '{IX},' ; I11O0O0o = '{LM},'
if 45 - 45: OOooOOo
def oo0OoOO000O ( url ) :
 Oo0o0OoOoOo0 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo0o0OoOoOo0 )
 for url , OoO , i1I , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( OoO ) . replace ( 'Sezon' , ' Season ' ) + ( i1I ) . replace ( 'Bölüm' , ' Episode ' ) + Oo0OO , url , 8063 , '' )
  if 36 - 36: IIi * oOo0O0Ooo * Ii1I . oo0oO00 * Ii1I
  if 76 - 76: Oooo0O0oo00oO + o0o00Oo0O / iIi1i1ii1 - oO0o
  if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * iiII11i1I1IIi * IIiIiII11i * Ii1I
  if 9 - 9: Ii + Oooo0O0oo00oO - OOooOOo / OOoOoo % ooOoO0O00 / O0oOO0
def iiI1 ( url ) :
 Oo0o0OoOoOo0 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Oo0o0OoOoOo0 )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( Oo0OO , url , 222 , '' )
  if 42 - 42: oO0o - Ii1I * iIi1i1ii1 - OOoOoo
  if 75 - 75: iiII11i1I1IIi * I1ii11iIi11i / OooOO000 * I1ii11iIi11i / OOoOoo
  if 14 - 14: ooOoO0O00 * iI11I1II1I1I - IIi * OOooOOo - iiII11i1I1IIi / O0oOO0
  if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
def oOoO0o0o ( ) :
 if 72 - 72: oo0oO00 * OOooOOo % OooOO000 % OOoOoo
 Oo0o0OoOoOo0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo0o0OoOoOo0 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO , i1I in o00oooO0Oo :
  IiIiIi ( Oo0OO + '  -  ' + ( i1I ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 8063 , IiiIi1III )
  if 22 - 22: Oooo0O0oo00oO - Ii1I / iIi1i1ii1
def o0ooO0Oo ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , IiiIi1III in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 8002 , IiiIi1III )
def O00oO0oo ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOoO )
 for IiiIi1III , time , url , Oo0OO , ii1IoO0O in o00oooO0Oo :
  I1IiiiiI ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , time ) , url , 1015 , IiiIi1III , ii1IoO0O )
  if 65 - 65: o0o00Oo0O . Ii1I * OooOO000
def iiIiI11IiI ( ) :
 if 23 - 23: oOo0O0Ooo - I11i % O0oOO0 . o0o00Oo0O * ii + OOoOoo
 IiIiIi ( 'Coronation Street' , '' , 8001 , '' )
 IiIiIi ( 'Eastenders' , '' , 8002 , '' )
 IiIiIi ( 'Emmerdale' , '' , 8003 , '' )
 IiIiIi ( 'Hollyoaks' , '' , 8004 , '' )
 IiIiIi ( 'Im a Celebrity' , '' , 8005 , '' )
 if 53 - 53: I1ii11iIi11i
 if 3 - 3: iIi1i1ii1 - ii * ii - oOo0O0Ooo / OooOO000 * Ii1I
 if 58 - 58: iIi1i1ii1 % iI11I1II1I1I / Ii % I11i . OooOO000 * iiII11i1I1IIi
 if 32 - 32: ii + I11i
def o0000OOOo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Holly' in Oo0OO :
   IiiIi1III = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooO0oOOooOo0 :
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , IiiIi1III )
   else :
    pass
    if 56 - 56: ooOoO0O00 + ii % oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 36 - 36: iiII11i1I1IIi * oo0oO00 * o0o00Oo0O * Oooo0O0oo00oO - I11i / Ii1I
def oooOo0OO ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'East' in Oo0OO :
   IiiIi1III = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooO0oOOooOo0 :
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , IiiIi1III )
   else :
    pass
    if 9 - 9: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: OOoOoo / IIi % I11i % Ii
def o0OO0Oooo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Emmer' in Oo0OO :
   IiiIi1III = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooO0oOOooOo0 :
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , IiiIi1III )
   else :
    pass
    if 97 - 97: iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: ii - Oooo0O0oo00oO + o0o00Oo0O * iIi1i1ii1 * oo0oO00
def iIi1Iii11111I1iii ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Coro' in Oo0OO :
   IiiIi1III = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooO0oOOooOo0 :
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , IiiIi1III )
   else :
    pass
    if 67 - 67: Ii1I + O0oOO0 * iIi1i1ii1 / IIiIiII11i % oO0o % oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: OOooOOo % O0oOO0 - Oooo0O0oo00oO + Oooo0O0oo00oO + O0oOO0 / iI11I1II1I1I
def oo0o ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Celeb' in Oo0OO :
   IiiIi1III = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooO0oOOooOo0 :
    IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , IiiIi1III )
   else :
    pass
    if 69 - 69: I11i + Ii1I / iI11I1II1I1I . iIi1i1ii1 % Ii1I * OOooOOo
def Iii1i11 ( name , url ) :
 IiIi11i = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiIi11i :
  i1I11IiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOoO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OOoO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOoO = open_url ( url )
  iiiiI = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OOoO ) [ - 1 ]
  i1I11IiI = iiiiI . replace ( '\\/' , '/' )
 oo00o0 = xbmcgui . ListItem ( name , '' , '' )
 oo00o0 . setPath ( i1I11IiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo00o0 )
 if 44 - 44: ooOoO0O00 . Ii1I - OOoOoo . Oooo0O0oo00oO . I11i + O0oOO0
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + IIi % ooOoO0O00 . O0oOO0
def o00OoOO00 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for ooO0oOOooOo0 , Oo0OO in o0O0OOO0Ooo :
  IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 62 - 62: OOooOOo * ii * I11i
def ii111Ii1i ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Movies' in Oo0OO :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooO0oOOooOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def IiI1I1II ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiiIi1III )
 for url in o0O0OOO0Ooo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / oo0oO00
  if 21 - 21: ii / iIi1i1ii1
def I11Iiii1I ( url ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , IiiIi1III in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IiiIi1III )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
OO0OOoooOo00 = '{UJ},' ; oOoO = '{WE},' ; o0O0o0O = '{WP},' ; iiII1i1i1I1 = '{PP},'
def Ooo0o0o0ooo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url , IiiIi1III in o00oooO0Oo :
  if '{{' in Oo0OO :
   pass
  else :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiiIi1III )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0O0ooO0oOO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  oO0000Oo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0000Oo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: I1ii11iIi11i . ii + Oooo0O0oo00oO . OooOO000 % Ii1I
 if 19 - 19: OooOO000 * iIi1i1ii1 - iIi1i1ii1 * iI11I1II1I1I . I1ii11iIi11i / iI11I1II1I1I
 if 100 - 100: OOoOoo % oo0oO00 / o0o00Oo0O * IIi - Ii
def o0oo ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '(cooltvseries.com)' in Oo0OO :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , Oo0OO in o0O0OOO0Ooo :
  if '(cooltvseries.com)' in Oo0OO :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def O0oooOO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  III111i11IiI ( ( url ) . replace ( ' ' , '%20' ) )
IIiIi1I1iI1 = '{XX},' ; i1I111II11 = '{UD},' ; o00oO = '{YT},' ; I11ii111i = '{JS},' ; IIiI1I11ii1i = '{PF},'
if 75 - 75: o0o00Oo0O
def oooooOOo0Oo ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO , IiiIi1III in o00oooO0Oo :
  IIIII1 ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( ooO0oOOooOo0 ) ) , 222 , IiiIi1III )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . OOoOoo
def I1iIIII1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OOoO )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  if 'youtu' in url :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IiiIi1III )
 for url in next :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 70 - 70: ii . OOoOoo / O0oOO0 . O0oOO0 - I11i
def i1II1i1iiI1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 62 - 62: IIi . Ii % o0o00Oo0O % OooOO000 - I1ii11iIi11i
def OooOO0o0oOoO ( url ) :
 OOoO = O0
 o00oooO0Oo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 222 , IiiIi1III )
  if 47 - 47: iiII11i1I1IIi * OOooOOo * iIi1i1ii1
  if 46 - 46: IIi
  if 42 - 42: iI11I1II1I1I
  if 32 - 32: I1ii11iIi11i - IIi . ii - ii - I1ii11iIi11i . iI11I1II1I1I
  if 34 - 34: I1ii11iIi11i
def IiI1I1i1 ( ) :
 if 6 - 6: oOo0O0Ooo . IIiIiII11i + OooOO000 / oO0o % oOo0O0Ooo . ii
 IiIiIi ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIiIi ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 64 - 64: iI11I1II1I1I + IIiIiII11i . iiII11i1I1IIi % I1ii11iIi11i * OOoOoo
 if 7 - 7: ooOoO0O00 + ooOoO0O00 / iIi1i1ii1
def I1IIiiiiI1iIi ( Cat_Name ) :
 if 82 - 82: Ii + o0o00Oo0O - IIi
 oO00oO0 = False
 o0o = '0'
 if Cat_Name == 'All Channels' : oO00oO0 = True
 if Cat_Name == 'Entertainment' : o0o = '1'
 if Cat_Name == 'Movies' : o0o = '2'
 if Cat_Name == 'Music' : o0o = '3'
 if Cat_Name == 'News' : o0o = '4'
 if Cat_Name == 'Sports' : o0o = '5'
 if Cat_Name == 'Documentary' : o0o = '6'
 if Cat_Name == 'Kids' : o0o = '7'
 if Cat_Name == 'Food' : o0o = '8'
 if Cat_Name == 'Religious' : o0o = '9'
 if Cat_Name == 'USA Channels' : o0o = '10'
 if Cat_Name == 'Other' : o0o = '11'
 if 25 - 25: iiII11i1I1IIi / iI11I1II1I1I + oOo0O0Ooo / OOoOoo
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOoO )
 print 'Len Match: >>>' + str ( len ( o00oooO0Oo ) )
 for Oo0OO , IiiIi1III , OO0Oo00o0o0 in o00oooO0Oo :
  Iii1iI1iIII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiiIi1III ) . replace ( '\\' , '' )
  if OO0Oo00o0o0 == o0o :
   IiIiIi ( Oo0OO , '' , 7022 , Iii1iI1iIII )
  elif oO00oO0 == True :
   IiIiIi ( Oo0OO , '' , 7022 , Iii1iI1iIII )
  else : pass
  if 76 - 76: IIiIiII11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: ii + OOoOoo . iIi1i1ii1 . I1ii11iIi11i - oOo0O0Ooo
def OOOo0ooOO ( Search_Name ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOoO )
 for IiiIi1III , ooO0oOOooOo0 , IiIi1I1ii111 , I11iiIi1i1 in o00oooO0Oo :
  Iii1iI1iIII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiiIi1III ) . replace ( '\\' , '' )
  IIIII1 ( Search_Name + ': Link 1' , ( ooO0oOOooOo0 ) . replace ( '\\' , '' ) , 222 , Iii1iI1iIII )
  IIIII1 ( Search_Name + ': Link 2' , ( IiIi1I1ii111 ) . replace ( '\\' , '' ) , 222 , Iii1iI1iIII )
  IIIII1 ( Search_Name + ': Link 3' , ( I11iiIi1i1 ) . replace ( '\\' , '' ) , 222 , Iii1iI1iIII )
  if 89 - 89: oo0oO00
def iiO00O ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  IIIII1 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def IIIIIi1 ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  IIIII1 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def o0oIi1iiiii ( ) :
 OOoO = O0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOoO )
 for Oo0OO , ooO0oOOooOo0 in o00oooO0Oo :
  IIIII1 ( Oo0OO , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 88 - 88: IIi / Ii % OOooOOo % Oooo0O0oo00oO
def OOI1 ( url ) :
 url
 OO00 = xbmcgui . ListItem ( Oo0OO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO00 )
 return
 if 59 - 59: ii * I11i / OooOO000
 if 75 - 75: I11i - ii
def Iiiiii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOoO )
 for url , Oo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IiiIi1III , '' , ( Oo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 for url in o0O0OOO0Ooo :
  IiIiIi ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 61 - 61: oO0o - Ii / oo0oO00 % iIi1i1ii1
def I1111IiII1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0 , IiiIi1III in o00oooO0Oo :
  o0OIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IiiIi1III , '' , Oo0 )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 OO0oo00oOO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for IiiII in OO0oo00oOO :
  iiIiI1i1 = ( IiiII ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IiiiiI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IiiIi1III , '' , iiIiI1i1 )
  if 72 - 72: I1ii11iIi11i + OooOO000 % Ii1I + Oooo0O0oo00oO % OooOO000
def iiiiI11 ( INFO ) :
 OOOiiiiI ( 'info for workout' , INFO )
 if 10 - 10: OOoOoo - I1ii11iIi11i % IIiIiII11i
 if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 if 46 - 46: OooOO000 * O0oOO0 . IIi * OooOO000 * iI11I1II1I1I / oo0oO00
def IiiIi1iIIi ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( ( Oo0OO ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def ii1IO0oo00o000 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def II1111iiI1II ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   IIIII1 ( ( Oo0OO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def OoOOOO00 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  if '=' in Oo0OO :
   pass
  else :
   IIIII1 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 15 - 15: Oooo0O0oo00oO * OOoOoo + IIiIiII11i . OooOO000 . O0oOO0
   if 46 - 46: iIi1i1ii1 % OooOO000 + iI11I1II1I1I * oOo0O0Ooo
   if 64 - 64: Ii1I * IIi * I1ii11iIi11i % iIi1i1ii1 % OOoOoo
   if 55 - 55: IIiIiII11i - OooOO000 - Oooo0O0oo00oO % IIi
   if 49 - 49: I1ii11iIi11i * OooOO000
def OOO0 ( ) :
 OOoO = O0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 o00oooO0Oo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'Daily' in Oo0OO :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 9008 , Ooo )
def I11ii1I ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def i1iIi1iiii1ii ( url ) :
 IIIII1 ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 IIIII1 ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 IIIII1 ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  IIIII1 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
def iIIiIiii1 ( ) :
 OOoO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if '.m3u' in ooO0oOOooOo0 :
   IiIiIi ( ( Oo0OO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + ooO0oOOooOo0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def oo0OO0Oo ( url ) :
 OOoO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  IIIII1 ( ( Oo0OO ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 4 - 4: OOooOOo * o0o00Oo0O - oo0oO00
def O0o0oO ( ) :
 OOoO = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  if 'category' in ooO0oOOooOo0 :
   IiIiIi ( Oo0OO , 'http://www.disclose.tv/' + ooO0oOOooOo0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 72 - 72: oo0oO00 + OOoOoo / oOo0O0Ooo . iIi1i1ii1 % oO0o / Ii
   if 13 - 13: OooOO000 % I11i + Oooo0O0oo00oO + OooOO000 + Ii - Ii1I
def ooooooo0oOo0 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOoO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOoO )
 for url , Oo0OO , IiiIi1III in o00oooO0Oo :
  IiIiIi ( Oo0OO , 'http://www.disclose.tv/' + url , 7011 , IiiIi1III )
 for url in next :
  IiIiIi ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 81 - 81: Ii % oOo0O0Ooo / iiII11i1I1IIi % oO0o / OooOO000 % iI11I1II1I1I
  if 14 - 14: Ii1I * I1ii11iIi11i + Ii % Oooo0O0oo00oO - O0oOO0
def iIIii ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OOoO )
 oOoooo000Oo00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  if 'http' in url :
   IIIII1 ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , Oo0OO in o0O0OOO0Ooo :
  IIIII1 ( Oo0OO , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in oOoooo000Oo00 :
  IIIII1 ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 95 - 95: OooOO000 + iIi1i1ii1 * iI11I1II1I1I
  if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / IIi
def iiii1ii1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 12 - 12: Ii - iI11I1II1I1I * iIi1i1ii1 * iiII11i1I1IIi
def iiIII1iIiI1Ii11Iiii ( name , url , img ) :
 I1 = O0 ( url )
 Ii11II11iI1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 OoOo0Oooo0o = len ( Ii11II11iI1 )
 if 65 - 65: OOooOOo + OooOO000 % oOo0O0Ooo
 if 54 - 54: OooOO000 / I11i
 if OoOo0Oooo0o == 1 :
  for I11IIIIiII in Ii11II11iI1 :
   I11IIIIiII = I11IIIIiII . replace ( 'player' , 'watch' )
   OoooO = I11IIIIiII + '&fv=&sou='
   IIIi1IIiII11 = O0 ( OoooO )
   I1IIi = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( IIIi1IIiII11 )
   for iIiIi1I in I1IIi :
    O00O = False
    Resolve ( iIiIi1I )
    if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 elif OoOo0Oooo0o > 1 :
  if 15 - 15: OOoOoo / OOoOoo % ii . OooOO000
  for I11IIIIiII in Ii11II11iI1 :
   oOoOooO0OOOoo = O0 ( I11IIIIiII )
   I1I111i = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oOoOooO0OOOoo )
   OOooOOoO0 = I1I111i
   OOooOOoO0 = ( str ( OOooOOoO0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OOooOOoO0
   IIIII1 ( 'DOUBLE LINK' , OOooOOoO0 , 424 , '' )
   if 16 - 16: ooOoO0O00 / iiII11i1I1IIi % O0oOO0 / OOoOoo
   for url in I1I111i :
    IiIiIi ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiIi1I1ii111 = Google . resolve ( url )
    except :
     pass
    try :
     IiIi1iIiiiiii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiIi1I1ii111 ) )
     for Oooo0O , oOOo0O0Oo in IiIi1iIiiiiii :
      if 50 - 50: O0oOO0 * oo0oO00 + Oooo0O0oo00oO - I1ii11iIi11i
      HD_URLS . append ( Oooo0O )
      SD_URLS . append ( oOOo0O0Oo )
    except :
     pass
 else :
  pass
  if 79 - 79: oO0o / ooOoO0O00
def iIi1i1I1I ( ) :
 if 35 - 35: oo0oO00 + o0o00Oo0O * IIiIiII11i
 if 23 - 23: OOooOOo * iIi1i1ii1 / O0oOO0
 IiIiIi ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 60 - 60: OOoOoo * IIi + OooOO000 . Oooo0O0oo00oO . o0o00Oo0O
 IiIiIi ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
 if 66 - 66: OooOO000 * I11i / iIi1i1ii1 * iiII11i1I1IIi / ii
def o0oi1i1ii11IiI ( ) :
 OOoO = O0 ( 'http://cnfstudio.com/' )
 o00oooO0Oo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , 'http://cnfstudio.com/genre/' + ooO0oOOooOo0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 6 - 6: Ii
iI111I11I1I1 = xbmcgui . Dialog ( )
if 16 - 16: iIi1i1ii1
Ooooo = '{UN},' ; OOi1IIII11II1 = '{IG},' ; OOOO0oOO = '{PL},' ; IIIiii = '{LO},' ; I11OoooO = '{LP},' ; i1IIi11 = '{HA},' ; oOIIIII11 = '{XD},' ; i1i1 = '{TA},' ; IiiIi = '{DP},' ; IIiiIiI = '{JT},' ; I1O0 = '{JJ},' ; oO0oo0oOO = '{MM},' ; iiII1iIi1ii1i = '{FQ},' ; i11IiI1 = '{HH},'
if 62 - 62: OOoOoo * Ii1I / iiII11i1I1IIi * Oooo0O0oo00oO / Oooo0O0oo00oO - iiII11i1I1IIi
def O0o0Oo0o00o ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOoO )
 O0O0o = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOoO )
 for IiiIi1III , url , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IiiIi1III )
 O0O0o = O0O0o
 for url in O0O0o :
  IiIiIi ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 96 - 96: o0o00Oo0O . I1ii11iIi11i - oo0oO00
def iiIiooOo0oo0O0O ( url ) :
 if 41 - 41: O0oOO0 / ii . I1ii11iIi11i / o0o00Oo0O . Ii % I11i
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  O0o0O00Oo0o0 = url + '&fv=&sou='
  O0o0O00Oo0o0 = O0o0O00Oo0o0 . replace ( 'player' , 'watch' )
  i1I1iii1I11II = IiI1I ( O0o0O00Oo0o0 )
  oO0oO0ooOoO0 = IiI1I ( url )
  if 10 - 10: Ii % Oooo0O0oo00oO * iiII11i1I1IIi % I1ii11iIi11i
  if 51 - 51: oO0o % iiII11i1I1IIi
def IiI1I ( url ) :
 if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OOoO )
 for url in o00oooO0Oo :
  I11IIIiIi11 ( url )
  if 8 - 8: Ii1I % oO0o % O0oOO0 . Ii1I * Ii1I
  if 94 - 94: Ii + ii
def i1iII1iii ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , OO0o , '' )
 if 97 - 97: OooOO000 / Oooo0O0oo00oO - Ii
def OO0o0o ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  O0O0O00OoO0O = open ( O0OoO000O0OO , 'r' )
  for OO00 in O0O0O00OoO0O :
   i1II11III = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OO00 )
   for Oo0OO , ooO0oOOooOo0 in i1II11III :
    IIIII1 ( Oo0OO , ooO0oOOooOo0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 95 - 95: oo0oO00 + I11i - Ii % oO0o / O0oOO0
def o00OooOOoOoo ( url ) :
 if os . path . exists ( Remote ) :
  I1 = O00 ( url )
  o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for Oo0OO , url in o00oooO0Oo :
   url = ( url ) . strip ( )
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 91 - 91: I11i / Ii
  if 96 - 96: oO0o + iiII11i1I1IIi * IIiIiII11i
def OOoO00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + ooO0oOOooOo0
 Oo0OO = 'plugin.video.GenieTv'
 if 82 - 82: I11i + IIi * oOo0O0Ooo - O0oOO0
 IIii ( ooO0oOOooOo0 , Oo0OO )
 if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % OooOO000 - iI11I1II1I1I . oo0oO00
def i1IiiiI1iI ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooO0oOOooOo0
 Oo0OO = 'repository.GenieTv'
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . OooOO000
 IIii ( ooO0oOOooOo0 , Oo0OO )
 if 31 - 31: o0o00Oo0O - iIi1i1ii1 * Ii * ooOoO0O00
 if 78 - 78: OOoOoo * OOooOOo . IIi . OOooOOo % iI11I1II1I1I
def OO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  o0i111 ( )
 if O0oO0 == 1 :
  O0oOO0o00OO ( )
  if 39 - 39: I11i . ooOoO0O00 % O0oOO0 / oo0oO00 % o0o00Oo0O
  if 100 - 100: OooOO000 - OOooOOo
  if 78 - 78: ii - OOooOOo . Ii
  if 36 - 36: O0oOO0 * iiII11i1I1IIi + iIi1i1ii1 * iiII11i1I1IIi . Ii1I - iI11I1II1I1I
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
i1IIi1ii1i1ii = 'https://addons.tvaddons.ag/'
if 97 - 97: IIiIiII11i
def O0oOO0o00OO ( ) :
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 I1iI1 = 'https://addons.tvaddons.ag/search/?keyword=' + oOOO
 I1 = O0 ( I1iI1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , ooOO0OoO , Oo0OO in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , ooO0oOOooOo0 , 10054 , 'https://addons.tvaddons.ag/' + ooOO0OoO , OO0o , '' )
  if 38 - 38: oOo0O0Ooo
  if 42 - 42: I11i
def o0i111 ( ) :
 I1 = O0 ( i1IIi1ii1i1ii )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  if 'Repositories' in Oo0OO :
   pass
  elif 'Services' in Oo0OO :
   pass
  elif 'International' in Oo0OO :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , ooO0oOOooOo0 , 10053 , 'https://addons.tvaddons.ag/' + IiiIi1III , OO0o , '' )
   if 8 - 8: Ii / OOoOoo
   if 33 - 33: OooOO000 * iIi1i1ii1 - o0o00Oo0O + oOo0O0Ooo / iIi1i1ii1
def Addon ( url ) :
 I1 = O0 ( url )
 iii1II11II1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  if 'Please' in Oo0OO :
   pass
  else :
   o0OIiII ( Oo0OO , url , 10054 , 'https://addons.tvaddons.ag/' + IiiIi1III , OO0o , '' )
 for url in iii1II11II1 :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
  if 30 - 30: iIi1i1ii1 / Ii % oO0o * Oooo0O0oo00oO
  if 27 - 27: o0o00Oo0O
def OOOIII1i ( url , name ) :
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
   if 17 - 17: iIi1i1ii1 - Ii - oo0oO00 / ii
def IIii ( url , name ) :
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
 if 96 - 96: OOoOoo - I11i . IIi / ii % o0o00Oo0O - ooOoO0O00
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 67 - 67: oOo0O0Ooo - oO0o
 if 60 - 60: ooOoO0O00 / iI11I1II1I1I * O0oOO0 + OOoOoo + ii + IIiIiII11i
def ii1ii1111 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , ooOO0OoO , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , url , 1007 , ooOO0OoO )
def iII11iiii111i ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , ooOO0OoO , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , ooOO0OoO )
  if 42 - 42: oO0o % O0oOO0 / I1ii11iIi11i / iIi1i1ii1
  if 86 - 86: OooOO000 + IIiIiII11i + ii + IIi
def IiIi1I1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , iconimage , Oo0 , iiI11ii1I1 , name in o00oooO0Oo :
  if 'http' in url :
   if '.php' in url :
    o00oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
    for OO00 in o00oo :
     if OO00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I11iiI ( name , url , 1016 , iconimage , iiI11ii1I1 , Oo0 )
   else :
    if 'youtube' in url :
     o00oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for OO00 in o00oo :
      if OO00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Ii11IiIiiii1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iiI11ii1I1 , Oo0 )
    else :
     o00oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for OO00 in o00oo :
      if OO00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Ii11IiIiiii1 ( name , url , 222 , iconimage , iiI11ii1I1 , Oo0 )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
  else :
   Oooooo0O ( url , iconimage , name )
   if 77 - 77: OOooOOo
 else :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
  for url , ooOO0OoO , name in o00oooO0Oo :
   if 'http' in url :
    if '.php' in url :
     IiIiIi ( name , url , 1016 , ooOO0OoO )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      IIIII1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooOO0OoO )
     else :
      o00oo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
      for OO00 in o00oo :
       if OO00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      IIIII1 ( name , url , 222 , ooOO0OoO )
      Iii1I1I11iiI1 ( 'movies' , 'INFO' )
   else :
    Oooooo0O ( url , ooOO0OoO , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 31 - 31: iIi1i1ii1 / iiII11i1I1IIi
def Oooooo0O ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oOo0OO0 = ( url ) . replace ( o0OO00O00oO , 'http' ) . replace ( i1I111II11 , '.com' ) ;
 OoOiIiIi1i1ii11 = ( oOo0OO0 ) . replace ( I11O0O0o , 'a' ) . replace ( oO0o0 , 'b' ) . replace ( i1Ii1i11ii , 'c' ) . replace ( oOoO , 'd' ) . replace ( OOOO0oOO , 'e' ) . replace ( IIiiIiI , 'f' ) ;
 O0O0o0o0OOooo = ( OoOiIiIi1i1ii11 ) . replace ( IIiIi1I1iI1 , 'g' ) . replace ( i1IIi11 , 'h' ) . replace ( o00oO , 'i' ) . replace ( IIiI1I11ii1i , 'j' ) . replace ( oO0O0oo , 'k' ) . replace ( OOOOOOO00OO , 'l' ) ;
 I1II1OOO0o0 = ( O0O0o0o0OOooo ) . replace ( IIII1i1i , 'm' ) . replace ( o0o00O , 'n' ) . replace ( Iii1I11i1IiiI , 'o' ) . replace ( OOooOO000oOoOo000 , 'p' ) . replace ( o0O0o0ooo0 , 'q' ) . replace ( iIo0O000O00o , 'r' ) ;
 iiooo = ( I1II1OOO0o0 ) . replace ( ii111I1I1I , 's' ) . replace ( o0O0o0O , 't' ) . replace ( iIIiIi1IiI1 , 'u' ) . replace ( Oo0O , 'v' ) . replace ( Iii1I1III11 , 'w' ) . replace ( i1ii1IiIiIii , 'x' ) ;
 OOo0ooOOOo0O0 = ( iiooo ) . replace ( ooI1 , 'y' ) . replace ( i1Iii1i1II1 , 'z' ) . replace ( Ooooo , '.' ) . replace ( OOi1IIII11II1 , '(' ) . replace ( IIIiii , ')' ) . replace ( I11OoooO , '/' ) ;
 O0o00OoooO = ( OOo0ooOOOo0O0 ) . replace ( Oo0O00OO , '1' ) . replace ( iiII1i1i1I1 , '2' ) . replace ( IiI1i1iI , '3' ) . replace ( i1i1 , '4' ) . replace ( IiiIi , '5' ) . replace ( I11ii111i , '6' ) ;
 iIIi = ( O0o00OoooO ) . replace ( I1O0 , '7' ) . replace ( oO0oo0oOO , '8' ) . replace ( iiII1iIi1ii1i , '9' ) . replace ( i11IiI1 , '0' ) . replace ( OO0O00 , ':' ) . replace ( ooOO , '%' ) ;
 url = ( iIIi ) . replace ( OO0OOoooOo00 , '-' ) . replace ( oOIIIII11 , '_' ) ;
 IIIII1 ( name , url , 222 , iconimage ) ;
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
def I11Ii1 ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , ooOO0OoO , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 1007 , ooOO0OoO )
def oO0O ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , ooOO0OoO , Oo0OO in o00oooO0Oo :
  IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , ooOO0OoO )
  if 62 - 62: O0oOO0 . OooOO000 - ii * IIiIiII11i . Ii
def iiIIiIi1i1I1 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 oOoooo0OooO = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 oOoooo0OooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoooo0OooO )
 if 67 - 67: ii + oO0o / I1ii11iIi11i % I11i % ooOoO0O00
 if 31 - 31: iIi1i1ii1 . IIiIiII11i % I1ii11iIi11i * IIi + IIi
def I11Ii1iI11iI1 ( url ) :
 OOoO = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOoO )
 for url , IiiIi1III , Oo0OO in o00oooO0Oo :
  if '-dir-' in Oo0OO :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IiiIi1III )
  else :
   IiIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' , url , 1006 , IiiIi1III )
   if 87 - 87: oO0o
def I1i11iiiiI1I ( url ) :
 OOoO = O00 ( url )
 OOOOo0o0O0 = ( 'http://afewbitsmore.com/' )
 o00oooO0Oo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '[To Parent Directory]' in Oo0OO :
   Oo0OO = 'HOME'
   pass
  elif 'HOME' in Oo0OO :
   pass
  elif '.m3u' in Oo0OO :
   IiIiIi ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , OOOOo0o0O0 + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in Oo0OO :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OOOOo0o0O0 + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in Oo0OO :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OOOOo0o0O0 + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) , OOOOo0o0O0 + url , 1012 , oOOOo00O00oOo + 'music.png' )
def I1I1i1 ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for IiiIi1III , Oo0OO , url in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 36 - 36: oOo0O0Ooo / I1ii11iIi11i % iI11I1II1I1I / o0o00Oo0O . Ii1I
def OOOoOOooOoo ( url ) :
 OOoO = O00 ( url )
 OOOOo0o0O0 = url
 o00oooO0Oo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  if '.mp3' in Oo0OO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '/' , '' ) , OOOOo0o0O0 + url , 1011 , oOOOo00O00oOo + 'music.png' )
def O00OO0oOOO ( ) :
 OOoO = O00 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOoO )
 for ooO0oOOooOo0 , IiiIi1III , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ( 'http://www.cyn.net/music/' + ooO0oOOooOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IiiIi1III ) . replace ( ' ' , '%20' ) )
def I1ii11ii1iiI ( url , img ) :
 OOoO = O00 ( url )
 IiIi1I1ii111 = url
 img = img
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( IiIi1I1ii111 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 93 - 93: OOooOOo + oo0oO00
def OO0 ( url ) :
 OOoO = O00 ( url )
 IiIi1I1ii111 = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOoO )
 for type , url , Oo0OO in o00oooO0Oo :
  if '[VID]' in type :
   IIIII1 ( ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , IiIi1I1ii111 + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   OO0 ( IiIi1I1ii111 + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: iI11I1II1I1I * oo0oO00
 if 42 - 42: O0oOO0
def i1III1 ( ) :
 o0Oo00 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o0O00oOoo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOO = o0O00oOoo . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiIi1I1ii111 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I11iiIi1i1 = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 22 - 22: iI11I1II1I1I % oOo0O0Ooo . o0o00Oo0O
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( IiIi1I1ii111 )
 Iiii = Oo0OoO00oOO0o ( I11iiIi1i1 )
 if 13 - 13: IIiIiII11i % ooOoO0O00 - OOooOOo + iiII11i1I1IIi
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o00oooO0Oo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( Oo0OO + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooO0oOOooOo0 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 59 - 59: ii + OooOO000 % I11i - OOooOOo . oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0OO in o0O0OOO0Ooo :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( Oo0OO + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1I1ii111 + Oo0OO ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 42 - 42: OooOO000
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  oOoooo000Oo00 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for Oo0OO in oOoooo000Oo00 :
   if o0O00oOoo in Oo0OO . lower ( ) :
    IiIiIi ( ( Oo0OO + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I11iiIi1i1 + Oo0OO ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 70 - 70: I11i / oo0oO00 + O0oOO0 % oOo0O0Ooo % I1ii11iIi11i + oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: Oooo0O0oo00oO
    if 12 - 12: IIi
    if 2 - 2: ii
    if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
    if 46 - 46: o0o00Oo0O % ii
    if 22 - 22: iiII11i1I1IIi + ii - OOooOOo - oO0o * OooOO000 - O0oOO0
IIII1i1i = '{SF},' ; o0o00O = '{IF},' ; Iii1I11i1IiiI = '{PW},' ; IiI1i1iI = '{AM},' ; OOooOO000oOoOo000 = '{GF},' ; o0O0o0ooo0 = '{DD},' ; iIo0O000O00o = '{UO},' ; ii111I1I1I = '{LE},' ; iIIiIi1IiI1 = '{ZY},' ; Oo0O = '{UE},' ; Iii1I1III11 = '{PE},' ; i1ii1IiIiIii = '{JE},' ; ooI1 = '{TH},' ; i1Iii1i1II1 = '{LK},'
if 99 - 99: OOoOoo / oOo0O0Ooo . IIi - IIi * oOo0O0Ooo
if 24 - 24: oo0oO00 * oO0o - O0oOO0 / iI11I1II1I1I - I1ii11iIi11i . Oooo0O0oo00oO
def I1o0OooOOOOOO ( ) :
 OOoO = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 o00oooO0Oo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def I1IiiI11 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OOoO )
 for url , Oo0OO , IiIii1I1I in o00oooO0Oo :
  IiIiIi ( Oo0OO + IiIii1I1I , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def iIII1II11I1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOoO )
 for url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  O000oOo0OO ( url )
def O000oOo0OO ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OOoO )
 o0O0OOO0Ooo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OOoO )
 oOoooo000Oo00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IIIII1 ( 'VidSpot - ' + Oo0OO , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in o0O0OOO0Ooo :
  IIIII1 ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for Oo0OO , url in oOoooo000Oo00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   IIIII1 ( 'TheVideo - ' + Oo0OO , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 57 - 57: Ii1I
def II1111i11i11 ( ) :
 OOoO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o00oooO0Oo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 43 - 43: o0o00Oo0O * Ii - ii - O0oOO0
  if 46 - 46: O0oOO0 * ooOoO0O00 / Ii1I
def ooO0O0OOO ( ) :
 OOoO = O0 ( 'http://www.animetoon.org/cartoon' )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOoO )
 for ooO0oOOooOo0 , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , ooO0oOOooOo0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 2 - 2: Ii / oO0o + OOoOoo - Ii1I * oO0o
  if 3 - 3: oO0o % I11i % Oooo0O0oo00oO . Ii1I . Ii1I
  if 35 - 35: ooOoO0O00 * iiII11i1I1IIi - iiII11i1I1IIi . iIi1i1ii1
def OO0o0 ( url ) :
 OOoO = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOoO )
 for IiiIi1III in o0O0OOO0Ooo :
  o0ooOOoO0oO0 = IiiIi1III
 oOoooo000Oo00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOoO )
 for url in oOoooo000Oo00 :
  IiIiIi ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOoO )
 for url , Oo0OO in o00oooO0Oo :
  IiIiIi ( Oo0OO , url , 1003 , o0ooOOoO0oO0 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0o00o0o0OO0O0 ( url , IMAGE ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOoO )
 for Oo0OO , url in o00oooO0Oo :
  print Oo0OO + '     ' + url
  if 'easy' in url :
   IiiiI1 ( url )
  elif 'playpanda' in url :
   IiiiI1 ( url )
   if 83 - 83: OooOO000
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiiI1 ( url ) :
 OOoO = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OOoO )
 for url in o00oooO0Oo :
  IIIII1 ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 38 - 38: O0oOO0
  if 9 - 9: oo0oO00 . oO0o . O0oOO0 / ii
def oo0ooo ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOO00O . add_header ( 'referer' , url )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 50 - 50: ii / oO0o % iI11I1II1I1I
def O00 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 41 - 41: Ii1I % Ii1I + iIi1i1ii1 . iiII11i1I1IIi % OooOO000 * OOoOoo
def O0Ii1iIii1I1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Oo0O0OO0OoO0 = ( '%s%s' % ( iIIiI11iI1Ii1 , url ) )
 O0o0O00Oo0o0 = O00 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , ooOO0OoO , Oo0OO in o00oooO0Oo :
  IIIII1 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + Oo0OO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooOO0OoO )
  if 21 - 21: OOooOOo + OOooOOo * OOoOoo / Oooo0O0oo00oO * ii . I1ii11iIi11i
def I11IIIiIi11 ( url ) :
 if 22 - 22: OOoOoo % OOooOOo / I11i
 oO0OIiIi1ii1Ii = open ( I11i1I1I , "a" )
 oO0OIiIi1ii1Ii . write ( 'url="' + url + '"\n' )
 oO0OIiIi1ii1Ii . close
 if 6 - 6: iiII11i1I1IIi % I11i + OooOO000
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 import urlresolver
 try : oO0o0O0Ooo0o . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Oo0OO ) )
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO0o0O0Ooo0o . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 91 - 91: I11i + o0o00Oo0O * O0oOO0 * iIi1i1ii1 * Ii1I
def oO0oO0OoO00 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 o0oOoO00o . update ( 100 , '%s' % Oo0OO )
 xbmc . sleep ( 1 )
 oO0o0O0Ooo0o . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 54 - 54: ii * oOo0O0Ooo % ooOoO0O00 . OOoOoo % IIi . Ii1I
def III111i11IiI ( url ) :
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0o0O0Ooo0o . play ( url ) . strip ( )
 except : pass
 if 72 - 72: OOoOoo % oo0oO00 + oO0o
def o0o0Oo ( url ) :
 oO0o0O0Ooo0o = xbmc . Player ( i1Ii11II ( ) )
 import urlresolver
 ooOoo00OoO00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0o0O0Ooo0o . play ( ooOoo00OoO00 )
 xbmc . sleep ( 1 )
 oO0o0O0Ooo0o . play ( url )
 if 69 - 69: o0o00Oo0O . OooOO000 - o0o00Oo0O
 if 58 - 58: OOooOOo + Ii1I
def i1Ii11II ( ) :
 try :
  IiIIiIii1ii = getSet ( "core-player" )
  if ( IiIIiIii1ii == 'DVDPLAYER' ) : III1I1Iii1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiIIiIii1ii == 'MPLAYER' ) : III1I1Iii1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiIIiIii1ii == 'PAPLAYER' ) : III1I1Iii1 = xbmc . PLAYER_CORE_PAPLAYER
  else : III1I1Iii1 = xbmc . PLAYER_CORE_AUTO
 except : III1I1Iii1 = xbmc . PLAYER_CORE_AUTO
 return III1I1Iii1
 return True
 if 34 - 34: O0oOO0 - IIiIiII11i - I11i + iiII11i1I1IIi + OooOO000
def IiIiIi ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo = [ ]
  Oo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = True )
 return o00ooO00O
 if 70 - 70: ii + oO0o * I1ii11iIi11i
def iI11 ( name , url , mode , iconimage , fanart , description ) :
 if 20 - 20: Ii - IIiIiII11i - OOoOoo % O0oOO0 . OOoOoo
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = True )
 return o00ooO00O
 if 50 - 50: iI11I1II1I1I + OooOO000 - oo0oO00 - ii
def IIIII1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  Oo = [ ]
  Oo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = False )
 return o00ooO00O
 if 84 - 84: OOooOOo - oo0oO00
 if 80 - 80: Ii % Oooo0O0oo00oO - I1ii11iIi11i % Oooo0O0oo00oO
 if 89 - 89: IIi * oo0oO00 + OOooOOo / Ii
 if 68 - 68: ii * oo0oO00
 if 86 - 86: I11i / OOooOOo
 if 40 - 40: iiII11i1I1IIi
def OOOiiiiI ( heading , announce ) :
 class o000Oo0O0OoOo00 ( ) :
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
   try : oOOo0O00o = open ( announce ) ; O00oOo0O0o00O = oOOo0O00o . read ( )
   except : O00oOo0O0o00O = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O00oOo0O0o00O ) )
   return
 o000Oo0O0OoOo00 ( )
 o000Oo0O0OoOo00 ( )
 if 19 - 19: OooOO000 % OooOO000 / OOoOoo + OooOO000 / ooOoO0O00
def OOI1iI1ii1II ( ) :
 OOOiiiiI ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 70 - 70: Oooo0O0oo00oO - iIi1i1ii1 . OooOO000
 if 11 - 11: Ii + I11i - OooOO000 * Ii - oOo0O0Ooo
 if 49 - 49: ooOoO0O00 % O0oOO0 / Oooo0O0oo00oO . Ii1I - OooOO000
 if 12 - 12: Ii + oo0oO00 - Ii1I
 if 27 - 27: iiII11i1I1IIi
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
 if 85 - 85: oOo0O0Ooo
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
 if 72 - 72: ii . I11i + o0o00Oo0O
 if 46 - 46: OOooOOo * oo0oO00 / O0oOO0 + I1ii11iIi11i + iIi1i1ii1
def oO00O0O0O ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ooOo0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 73 - 73: OOoOoo - OooOO000 * ii / Ii1I - oo0oO00 - iIi1i1ii1
def OOOOoOooO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOoOI1i1i1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 78 - 78: ii % iiII11i1I1IIi + oO0o * ii
def iioOoO0oOO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o00I11Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 27 - 27: OooOO000 - I11i * Ii1I - oOo0O0Ooo
def IIIiIIi111 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oo0O0Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 17 - 17: iIi1i1ii1 % iIi1i1ii1
def i11IIiiI ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOooiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 15 - 15: ii
def i11iiI1iiIii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1I111iOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 44 - 44: Oooo0O0oo00oO - iIi1i1ii1 + iiII11i1I1IIi
def oooo00OoOoO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oo0O0I1i1I1i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
def iIi1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i11IIiiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / Oooo0O0oo00oO / OooOO000
def i11Ii1iiiI1I ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + II1iiI11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 42 , IiIIi1 , iiI11ii1I1 , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 43 - 43: OOooOOo / iI11I1II1I1I
def Ii1I1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ooO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0OO , url , IiIIi1 , iiI11ii1I1 , oo000ii in o00oooO0Oo :
  I1IiiiiI ( Oo0OO , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oo000ii )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 3 - 3: Ii1I % I1ii11iIi11i . o0o00Oo0O % I11i . I11i - iiII11i1I1IIi
 if 68 - 68: Ii . OOoOoo % oo0oO00
 if 47 - 47: OOooOOo . ooOoO0O00
 if 47 - 47: Ii . iIi1i1ii1
 if 37 - 37: oOo0O0Ooo / ii % Ii % Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
 if 1 - 1: iIi1i1ii1 % ooOoO0O00
 if 41 - 41: oO0o * oO0o / iiII11i1I1IIi + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / IIi
def I1i1I1I11IiiI ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( O00o0OO ) :
     oOoooOOO0 = 0
     oOoooOOO0 += len ( OoOOo )
     if oOoooOOO0 > 0 :
      for oOOo0O00o in OoOOo :
       os . unlink ( os . path . join ( i111i1I1ii1i , oOOo0O00o ) )
  I1Iiii1i1iI = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( I1Iiii1i1iI )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 51 - 51: iiII11i1I1IIi / OooOO000 % O0oOO0 + O0oOO0 * O0oOO0
 if 20 - 20: iiII11i1I1IIi % Ii1I + oO0o / I1ii11iIi11i
 if 10 - 10: Ii / OOooOOo
 if 27 - 27: oOo0O0Ooo / ii
 if 74 - 74: Ii1I % OooOO000 - oO0o * oo0oO00 . ii * oO0o
 if 99 - 99: OOooOOo . iiII11i1I1IIi - ii - o0o00Oo0O
 if 6 - 6: Oooo0O0oo00oO
 if 3 - 3: o0o00Oo0O - OooOO000 * IIi * Oooo0O0oo00oO / IIi
def iiiii11I1 ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 58 - 58: IIi * iI11I1II1I1I + OOoOoo . OOoOoo
def O0ooO0Oo00o ( url ) :
 O00O00000 = os . path . join ( oO , 'addon_data' )
 iI1II1IIIIi = [
 ( O00O00000 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( O00O00000 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( O00O00000 , 'plugin.video.itv' , 'Images' ) ) ]
 if 18 - 18: Ii / OOooOOo + iiII11i1I1IIi . I1ii11iIi11i * o0o00Oo0O
 ooo00O0OO = 0
 if 91 - 91: oo0oO00
 for OO00 in iI1II1IIIIi :
  if os . path . exists ( OO00 ) and not OO00 in [ oOo0oooo00o , O00O00000 ] :
   for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( OO00 ) :
    oOoooOOO0 = 0
    oOoooOOO0 += len ( OoOOo )
    if oOoooOOO0 > 0 :
     for oOOo0O00o in OoOOo :
      if not oOOo0O00o in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( i111i1I1ii1i , oOOo0O00o ) )
       except :
        pass
      else : ii1 ( 'Ignore Log File: %s' % oOOo0O00o )
     for OoOOo00 in OO0oo0O0OOO0 :
      try :
       shutil . rmtree ( os . path . join ( i111i1I1ii1i , OoOOo00 ) )
       ooo00O0OO += 1
       ii1 ( "[Success] cleared %s files from %s" % ( str ( oOoooOOO0 ) , os . path . join ( OO00 , OoOOo00 ) ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( OO00 , OoOOo00 ) )
  else :
   for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( OO00 ) :
    for OoOOo00 in OO0oo0O0OOO0 :
     if 'cache' in OoOOo00 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( i111i1I1ii1i , OoOOo00 ) )
       ooo00O0OO += 1
       ii1 ( "[Success] wiped %s " % os . path . join ( OO00 , OoOOo00 ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( OO00 , OoOOo00 ) )
       if 40 - 40: iiII11i1I1IIi % o0o00Oo0O - I1ii11iIi11i . IIiIiII11i % IIi % oO0o
 iiiii11I1 ( oo0o0O00 , 'Clear Cache: Removed %s Files' % ooo00O0OO )
 if 36 - 36: iIi1i1ii1
 if 65 - 65: iIi1i1ii1 / Oooo0O0oo00oO
 if 56 - 56: iI11I1II1I1I + OooOO000
 if 59 - 59: O0oOO0 - O0oOO0 / OooOO000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
 if 15 - 15: IIi + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
 if 54 - 54: iIi1i1ii1 - IIiIiII11i . OOoOoo + IIi
def IiIIi1II1ii ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IIiii1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( IIiii1I ) :
   oOoooOOO0 = 0
   oOoooOOO0 += len ( OoOOo )
   if 76 - 76: IIi + iiII11i1I1IIi - iIi1i1ii1 * iI11I1II1I1I % ooOoO0O00
   if 72 - 72: OOoOoo + IIiIiII11i . o0o00Oo0O - iiII11i1I1IIi / ii . OooOO000
   if oOoooOOO0 > 0 :
    if 28 - 28: iI11I1II1I1I . o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( oOoooOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: ii
     for oOOo0O00o in OoOOo :
      os . unlink ( os . path . join ( i111i1I1ii1i , oOOo0O00o ) )
     for OoOOo00 in OO0oo0O0OOO0 :
      shutil . rmtree ( os . path . join ( i111i1I1ii1i , OoOOo00 ) )
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
 if 29 - 29: Ii1I
 if 41 - 41: IIi
 if 49 - 49: IIi % IIiIiII11i . IIi - I11i - oo0oO00 * iIi1i1ii1
 if 47 - 47: o0o00Oo0O . I11i / IIi * iiII11i1I1IIi
 if 63 - 63: OooOO000 - O0oOO0 - iiII11i1I1IIi - OOoOoo / O0oOO0 + oO0o
 if 94 - 94: iIi1i1ii1 / oOo0O0Ooo . IIiIiII11i
 if 32 - 32: O0oOO0 . Oooo0O0oo00oO % Oooo0O0oo00oO . OOooOOo
 if 37 - 37: Oooo0O0oo00oO + o0o00Oo0O + Oooo0O0oo00oO . iiII11i1I1IIi . I11i
 if 78 - 78: oOo0O0Ooo / oo0oO00 + I11i . I1ii11iIi11i / o0o00Oo0O
def OO0Oooo0oOO0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IIiii1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( IIiii1I ) :
   oOoooOOO0 = 0
   oOoooOOO0 += len ( OoOOo )
   if 49 - 49: Ii1I
   if 66 - 66: I11i . Ii1I
   if oOoooOOO0 > 0 :
    if 18 - 18: I1ii11iIi11i + iIi1i1ii1
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( oOoooOOO0 ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % IIi . oOo0O0Ooo
     for oOOo0O00o in OoOOo :
      os . unlink ( os . path . join ( i111i1I1ii1i , oOOo0O00o ) )
     for OoOOo00 in OO0oo0O0OOO0 :
      shutil . rmtree ( os . path . join ( i111i1I1ii1i , OoOOo00 ) )
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
 if 43 - 43: oOo0O0Ooo % Ii1I * IIi
 if 31 - 31: IIi / iiII11i1I1IIi
 if 3 - 3: iIi1i1ii1
 if 37 - 37: IIi * ii * oo0oO00 + I1ii11iIi11i . oOo0O0Ooo
 if 61 - 61: Oooo0O0oo00oO . Oooo0O0oo00oO
 if 17 - 17: IIiIiII11i / OOoOoo
 if 80 - 80: Oooo0O0oo00oO * oO0o + IIi
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
 if 98 - 98: I11i * I1ii11iIi11i - IIi . OOoOoo
 if 2 - 2: I1ii11iIi11i - OOoOoo % iI11I1II1I1I
def o0O0o0O0O ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11iIi1IiI = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 ooO0OOoOooO = os . path . join ( oOooO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( ooO0OOoOooO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   ii11iIi1IiI = os . path . join ( oOooO0 , 'advancedsettings.xml' )
   try :
    os . remove ( ii11iIi1IiI )
    print '=== GenieTv - REMOVING    ' + str ( ii11iIi1IiI ) + '    ==='
   except :
    pass
   O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
   Oo0o = open ( ii11iIi1IiI , "w" )
   Oo0o . write ( O0o0O00Oo0o0 )
   Oo0o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( ii11iIi1IiI ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  ii11iIi1IiI = os . path . join ( oOooO0 , 'advancedsettings.xml' )
  try :
   os . remove ( ii11iIi1IiI )
   print '=== GenieTv - REMOVING    ' + str ( ii11iIi1IiI ) + '    ==='
  except :
   pass
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  Oo0o = open ( ii11iIi1IiI , "w" )
  Oo0o . write ( O0o0O00Oo0o0 )
  Oo0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11iIi1IiI ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 76 - 76: I1ii11iIi11i * OOoOoo % Oooo0O0oo00oO . oO0o
def iIii1i1i1 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11iIi1IiI = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  Oo0o = open ( ii11iIi1IiI ) . read ( )
  if 'zero' in Oo0o :
   name = '0CACHE'
  elif 'tuxen' in Oo0o :
   name = 'TUXENS'
  elif 'muckys' in Oo0o :
   name = 'MUCKYS'
  elif 'p2p1' in Oo0o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Oo0o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Oo0o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 45 - 45: oo0oO00 - Oooo0O0oo00oO * iiII11i1I1IIi - oO0o . IIi
def oO0OoOooO0O ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11iIi1IiI = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  os . remove ( ii11iIi1IiI )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( ii11iIi1IiI ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 7 - 7: I1ii11iIi11i - Ii / O0oOO0 / O0oOO0 . ooOoO0O00 % oo0oO00
 if 51 - 51: O0oOO0
 if 23 - 23: Ii * iIi1i1ii1 * oo0oO00 % oo0oO00 - OOooOOo + IIiIiII11i
 if 91 - 91: ii + OooOO000 / IIiIiII11i * iiII11i1I1IIi + I11i / I1ii11iIi11i
 if 7 - 7: oo0oO00 / Ii - IIi % iiII11i1I1IIi
 if 67 - 67: iI11I1II1I1I - OOooOOo
 if 51 - 51: oo0oO00 * Ii1I % Ii1I + I11i
 if 16 - 16: o0o00Oo0O % oOo0O0Ooo * iI11I1II1I1I - IIiIiII11i + iI11I1II1I1I + I1ii11iIi11i
 if 4 - 4: oo0oO00
 if 60 - 60: IIiIiII11i + OooOO000 / O0oOO0 % ii - ooOoO0O00
def i1II1Ii1i1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o00oooO0Oo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for o0OOO00O0OOoO , o0oI1 , i1IO0OOoooO , ooO0OOoOoOO00 in o00oooO0Oo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0OOO00O0OOoO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i1IO0OOoooO , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ooO0OOoOoOO00 )
  inc = inc + 1
  if 65 - 65: iIi1i1ii1 / Ii1I
  if 84 - 84: ii . Ii % oO0o * I1ii11iIi11i / iiII11i1I1IIi
  if 95 - 95: oO0o - Ii . oO0o % Oooo0O0oo00oO * o0o00Oo0O + Ii
  if 65 - 65: o0o00Oo0O / iiII11i1I1IIi . ooOoO0O00 * iiII11i1I1IIi / iI11I1II1I1I - O0oOO0
  if 93 - 93: OOooOOo % Ii - IIi % oO0o
  if 55 - 55: I11i . Ii1I
  if 63 - 63: O0oOO0
  if 79 - 79: Ii1I - O0oOO0 - I11i . Oooo0O0oo00oO
  if 65 - 65: Ii . oO0o % iiII11i1I1IIi + iIi1i1ii1 - Ii
def oo00O0OO0oo0O ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ii11iIi1IiI = os . path . join ( oOooO0 , 'addons2.ini' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  Oo0o = open ( ii11iIi1IiI , "w" )
  Oo0o . write ( O0o0O00Oo0o0 )
  Oo0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11iIi1IiI ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 1 - 1: I1ii11iIi11i * o0o00Oo0O . oOo0O0Ooo + OOoOoo / OOooOOo + oo0oO00
def oO0o0OOO0O ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ii11iIi1IiI = os . path . join ( oOooO0 , 'settings.xml' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  Oo0o = open ( ii11iIi1IiI , "w" )
  Oo0o . write ( O0o0O00Oo0o0 )
  Oo0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11iIi1IiI ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 18 - 18: OooOO000
 if 34 - 34: iiII11i1I1IIi + OooOO000 * oo0oO00 / IIiIiII11i
def IiI1i1 ( ) :
 try :
  I1IO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I1IO0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i1I1Iii1IiiIi = os . path . join ( I1IO0 , "source.db" )
    os . unlink ( i1I1Iii1IiiIi )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 73 - 73: o0o00Oo0O . OooOO000 - ii % oo0oO00 % ooOoO0O00
 if 14 - 14: OooOO000 + IIi * I1ii11iIi11i
 if 49 - 49: I1ii11iIi11i
 if 57 - 57: o0o00Oo0O * OOoOoo - iiII11i1I1IIi - iI11I1II1I1I * iiII11i1I1IIi
 if 9 - 9: iIi1i1ii1 . oo0oO00
def O0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
 if 96 - 96: OOoOoo % o0o00Oo0O
 if 51 - 51: oOo0O0Ooo - iiII11i1I1IIi / Ii1I . Ii1I + Ii1I
 if 87 - 87: IIiIiII11i . IIi * oO0o
 if 74 - 74: I11i % OOooOOo . iiII11i1I1IIi % OooOO000 . o0o00Oo0O % IIiIiII11i
 if 5 - 5: O0oOO0 - ii / OOooOOo
 if 30 - 30: oo0oO00 % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
def oo00OO0000oO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; ooO0000 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if ooO0000 :
  Ooo00O0OooOOO = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; Ooo00O0OooOOO = xbmc . translatePath ( Ooo00O0OooOOO ) ;
  iIIIIi = os . path . join ( Ooo00O0OooOOO , ".." , ".." ) ; iIIIIi = os . path . abspath ( iIIIIi ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iIIIIi ) ; IIi1iI11I = False
  try :
   for i111i1I1ii1i , OO0oo0O0OOO0 , OoOOo in os . walk ( iIIIIi , topdown = True ) :
    OO0oo0O0OOO0 [ : ] = [ OoOOo00 for OoOOo00 in OO0oo0O0OOO0 if OoOOo00 not in o0oO0 ]
    for Oo0OO in OoOOo :
     try : os . remove ( os . path . join ( i111i1I1ii1i , Oo0OO ) )
     except :
      if Oo0OO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIi1iI11I = True
      plugintools . log ( "Error removing " + i111i1I1ii1i + " " + Oo0OO )
    for Oo0OO in OO0oo0O0OOO0 :
     try : os . rmdir ( os . path . join ( i111i1I1ii1i , Oo0OO ) )
     except :
      if Oo0OO not in [ "Database" , "userdata" ] : IIi1iI11I = True
      plugintools . log ( "Error removing " + i111i1I1ii1i + " " + Oo0OO )
   if not IIi1iI11I : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 i1i ( )
 if 61 - 61: o0o00Oo0O . IIi . o0o00Oo0O * Ii * IIiIiII11i / OooOO000
 if 69 - 69: oo0oO00
 if 17 - 17: oo0oO00
def i11iiiiiIi1 ( ) :
 OoIiii1i11I1iII = [ ]
 iI111II11IIii = sys . argv [ 2 ]
 if len ( iI111II11IIii ) >= 2 :
  I1II1 = sys . argv [ 2 ]
  oOO0o0OoO00OO00 = I1II1 . replace ( '?' , '' )
  if ( I1II1 [ len ( I1II1 ) - 1 ] == '/' ) :
   I1II1 = I1II1 [ 0 : len ( I1II1 ) - 2 ]
  I111II11I = oOO0o0OoO00OO00 . split ( '&' )
  OoIiii1i11I1iII = { }
  for Oo0OoOo in range ( len ( I111II11I ) ) :
   oOoOoo = { }
   oOoOoo = I111II11I [ Oo0OoOo ] . split ( '=' )
   if ( len ( oOoOoo ) ) == 2 :
    OoIiii1i11I1iII [ oOoOoo [ 0 ] ] = oOoOoo [ 1 ]
    if 97 - 97: O0oOO0 - oO0o + iiII11i1I1IIi * o0o00Oo0O
 return OoIiii1i11I1iII
 if 55 - 55: Ii + ooOoO0O00 % IIiIiII11i + oo0oO00 % OOoOoo
OO0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
O0oOO0o = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1iiiI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oOo0iiii11i1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OOoooOoO0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1iI1Ii1I1Iii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
ooOo0o0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
ii1iOO00O0O00oOOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOoOI1i1i1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o00I11Ii1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oo0O0Oo0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OOooiIi1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I1I111iOO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oo0O0I1i1I1i1Ii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1i11IIiiIiI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
II1iiI11I = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0000o0Oo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
ii1111iIIiIIi = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oo0ooO0O0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ooo00OoOO0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O00o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OoOi111i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
ooO00Oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iIIiI11iI1Ii1 = base64 . decodestring ( 'Q1VOVA==' )
def I1IiiiiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = True )
 return o00ooO00O
 if 60 - 60: oO0o
def o0OIiII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OO00IIiiIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o00ooO00O = True
 oo00o0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo00o0 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oo00o0 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Oo = [ ]
  if showcontext == 'fav' :
   Oo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   Oo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oo00o0 . addContextMenuItems ( Oo )
 o00ooO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO00IIiiIIi1 , listitem = oo00o0 , isFolder = False )
 return o00ooO00O
 if 10 - 10: oo0oO00 . ii - oO0o
 if 96 - 96: IIi
I1II1 = i11iiiiiIi1 ( )
ooO0oOOooOo0 = None
Oo0OO = None
OOooO0oo0o00o = None
IiIIi1 = None
iiI11ii1I1 = None
oo000ii = None
o00O00 = None
O0OoOOo = None
if 59 - 59: Oooo0O0oo00oO % OOooOOo
if 71 - 71: Ii1I
try :
 O0OoOOo = int ( I1II1 [ "fav_mode" ] )
except :
 pass
 if 5 - 5: OOoOoo
try :
 ooO0oOOooOo0 = urllib . unquote_plus ( I1II1 [ "url" ] )
except :
 pass
try :
 Oo0OO = urllib . unquote_plus ( I1II1 [ "name" ] )
except :
 pass
try :
 IiIIi1 = urllib . unquote_plus ( I1II1 [ "iconimage" ] )
except :
 pass
try :
 OOooO0oo0o00o = int ( I1II1 [ "mode" ] )
except :
 pass
try :
 iiI11ii1I1 = urllib . unquote_plus ( I1II1 [ "fanart" ] )
except :
 pass
try :
 oo000ii = urllib . unquote_plus ( I1II1 [ "description" ] )
except :
 pass
 if 34 - 34: iiII11i1I1IIi - O0oOO0
 if 22 - 22: OooOO000 + Ii1I - iiII11i1I1IIi * IIiIiII11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OOooO0oo0o00o )
print "URL: " + str ( ooO0oOOooOo0 )
print "Name: " + str ( Oo0OO )
print "IconImage: " + str ( IiIIi1 )
if 97 - 97: o0o00Oo0O . I11i
if 17 - 17: o0o00Oo0O . O0oOO0 - O0oOO0 - ooOoO0O00 * Oooo0O0oo00oO
def Iii1I1I11iiI1 ( content , viewType ) :
 if 16 - 16: OOooOOo / IIiIiII11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 22 - 22: oo0oO00
if IiIIi1 == None : IiIIi1 = Ooo
if iiI11ii1I1 == None : iiI11ii1I1 = OO0o
if OOooO0oo0o00o == None :
 oo0OOo0 ( )
 if 53 - 53: oO0o
elif OOooO0oo0o00o == 1 :
 ii1iIi1Ii1 ( ooO0oOOooOo0 )
 if 96 - 96: ii - iI11I1II1I1I . O0oOO0
elif OOooO0oo0o00o == 44 :
 oooO ( ooO0oOOooOo0 )
 if 2 - 2: ooOoO0O00
elif OOooO0oo0o00o == 2 :
 oOOOOoO00Ooo0 ( )
 if 6 - 6: ooOoO0O00 % oo0oO00 . iIi1i1ii1 + iIi1i1ii1 . oo0oO00 / Ii
elif OOooO0oo0o00o == 3 :
 o0o0O00 ( )
 if 78 - 78: o0o00Oo0O
elif OOooO0oo0o00o == 21 :
 i1i1II ( )
 if 34 - 34: IIiIiII11i
elif OOooO0oo0o00o == 4 :
 iIiIi1iI11iiI ( )
 if 20 - 20: oOo0O0Ooo % ooOoO0O00 % OOooOOo % OooOO000 + o0o00Oo0O
elif OOooO0oo0o00o == 5 :
 oO0oOoo0O ( ooO0oOOooOo0 )
 if 54 - 54: o0o00Oo0O
elif OOooO0oo0o00o == 6 :
 IiIIi1II1ii ( ooO0oOOooOo0 )
 if 3 - 3: Ii1I
elif OOooO0oo0o00o == 7 :
 o0O0o0O0O ( ooO0oOOooOo0 , Oo0OO )
 if 42 - 42: oo0oO00 % I1ii11iIi11i + iIi1i1ii1 - oo0oO00 . iI11I1II1I1I - IIi
elif OOooO0oo0o00o == 8 :
 iIii1i1i1 ( ooO0oOOooOo0 , Oo0OO )
 if 27 - 27: iiII11i1I1IIi % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif OOooO0oo0o00o == 9 :
 FIXREPOSADDONS ( ooO0oOOooOo0 )
 if 37 - 37: iiII11i1I1IIi + OooOO000 * IIi + iIi1i1ii1
elif OOooO0oo0o00o == 10 :
 o00O0 ( )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + IIi / IIiIiII11i
elif OOooO0oo0o00o == 11 :
 oO0OoOooO0O ( ooO0oOOooOo0 )
 if 66 - 66: OOoOoo + O0oOO0 % ii
elif OOooO0oo0o00o == 12 :
 i1II1Ii1i1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 23 - 23: O0oOO0 . OOooOOo + iI11I1II1I1I
elif OOooO0oo0o00o == 13 :
 I1i1I1I11IiiI ( )
 if 17 - 17: iIi1i1ii1
elif OOooO0oo0o00o == 14 :
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if 12 - 12: ooOoO0O00 . oO0o
elif OOooO0oo0o00o == 15 :
 o0OO0O0OO0oO0 ( )
 if 14 - 14: Oooo0O0oo00oO + IIiIiII11i % Oooo0O0oo00oO . O0oOO0 * OOoOoo
elif OOooO0oo0o00o == 16 :
 oo00O0OO0oo0O ( ooO0oOOooOo0 , Oo0OO )
 if 54 - 54: OOoOoo * oo0oO00 - OooOO000
elif OOooO0oo0o00o == 17 :
 oO0o0OOO0O ( ooO0oOOooOo0 , Oo0OO )
 if 15 - 15: iiII11i1I1IIi / o0o00Oo0O
elif OOooO0oo0o00o == 18 :
 IiI1i1 ( )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + OOoOoo . OooOO000 * OOoOoo
elif OOooO0oo0o00o == 19 :
 III1iii1i1II ( ooO0oOOooOo0 )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif OOooO0oo0o00o == 40 :
 OOOO0oOo00O ( Oo0OO , ooO0oOOooOo0 , oo000ii )
 if 82 - 82: o0o00Oo0O / iiII11i1I1IIi * oO0o - oo0oO00 + I1ii11iIi11i
elif OOooO0oo0o00o == 42 :
 OoOOoooO000 ( Oo0OO , ooO0oOOooOo0 , oo000ii )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + IIi * IIiIiII11i
elif OOooO0oo0o00o == 43 :
 IIi1iI11IIIi1 ( ooO0oOOooOo0 )
 if 78 - 78: OooOO000 - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif OOooO0oo0o00o == 20 :
 I1iIII1IiiI ( ooO0oOOooOo0 )
 if 97 - 97: ooOoO0O00
elif OOooO0oo0o00o == 22 :
 oO00O0O0O ( ooO0oOOooOo0 )
 if 29 - 29: oOo0O0Ooo
elif OOooO0oo0o00o == 23 :
 OOOOoOooO0o ( ooO0oOOooOo0 )
 if 37 - 37: Ii1I * OooOO000 * oOo0O0Ooo * o0o00Oo0O
elif OOooO0oo0o00o == 24 :
 iioOoO0oOO ( ooO0oOOooOo0 )
 if 35 - 35: oOo0O0Ooo - Ii1I * iiII11i1I1IIi + iIi1i1ii1 / ooOoO0O00
elif OOooO0oo0o00o == 25 :
 IIIiIIi111 ( ooO0oOOooOo0 )
 if 46 - 46: I1ii11iIi11i . OOoOoo % I1ii11iIi11i / IIiIiII11i * OOoOoo * Oooo0O0oo00oO
elif OOooO0oo0o00o == 26 :
 i11IIiiI ( ooO0oOOooOo0 )
 if 59 - 59: OooOO000 * iiII11i1I1IIi
elif OOooO0oo0o00o == 27 :
 i11iiI1iiIii ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 / o0o00Oo0O
elif OOooO0oo0o00o == 28 :
 oooo00OoOoO ( ooO0oOOooOo0 )
 if 57 - 57: ooOoO0O00 % OOoOoo
elif OOooO0oo0o00o == 29 :
 iIi1i ( ooO0oOOooOo0 )
 if 69 - 69: I11i
elif OOooO0oo0o00o == 30 :
 iIIi11 ( ooO0oOOooOo0 )
 if 69 - 69: OooOO000
elif OOooO0oo0o00o == 31 :
 i11Ii1iiiI1I ( ooO0oOOooOo0 )
 if 83 - 83: iI11I1II1I1I . I11i + OooOO000 . ii / OOoOoo + IIiIiII11i
elif OOooO0oo0o00o == 32 :
 OoOoO ( )
 if 90 - 90: IIi * iiII11i1I1IIi / Oooo0O0oo00oO
elif OOooO0oo0o00o == 33 :
 Iio00 ( )
 if 68 - 68: OOooOOo
elif OOooO0oo0o00o == 35 :
 i1IiI ( ooO0oOOooOo0 )
 if 65 - 65: O0oOO0
elif OOooO0oo0o00o == 34 :
 IiI1iiII1i1i ( ooO0oOOooOo0 )
 if 82 - 82: I11i
elif OOooO0oo0o00o == 36 :
 i11i11Ii11Iii ( ooO0oOOooOo0 )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + OooOO000
elif OOooO0oo0o00o == 37 :
 iii1IiI1I1 ( ooO0oOOooOo0 )
 if 65 - 65: IIi
elif OOooO0oo0o00o == 38 :
 oO0OoooO0oOO00OoOo ( ooO0oOOooOo0 )
 if 71 - 71: OooOO000 % OooOO000 . O0oOO0 + Ii - Ii
elif OOooO0oo0o00o == 41 :
 oo00OO0000oO ( I1II1 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / OooOO000 - Ii . OOoOoo / Oooo0O0oo00oO
elif OOooO0oo0o00o == 39 :
 Ii1I1i ( ooO0oOOooOo0 )
 if 13 - 13: I11i % o0o00Oo0O - OooOO000 * ii / I1ii11iIi11i - ii
elif OOooO0oo0o00o == 45 :
 TEXTS ( )
 if 78 - 78: O0oOO0 % ii
elif OOooO0oo0o00o == 46 :
 OOI1iI1ii1II ( )
 if 73 - 73: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + ooOoO0O00 - ii / O0oOO0
elif OOooO0oo0o00o == 47 :
 GEVID ( )
 if 78 - 78: ii % O0oOO0 - Ii
elif OOooO0oo0o00o == 48 :
 I1i ( Oo0OO , ooO0oOOooOo0 , oo000ii )
 if 37 - 37: iIi1i1ii1 % IIi % ooOoO0O00
elif OOooO0oo0o00o == 49 :
 IIo0Oo0oO0oOO00 ( )
 if 23 - 23: OOoOoo - o0o00Oo0O + Ii
elif OOooO0oo0o00o == 222 :
 I11IIIiIi11 ( ooO0oOOooOo0 )
 if 98 - 98: ii
elif OOooO0oo0o00o == 333 :
 O0Ii1iIii1I1 ( ooO0oOOooOo0 )
 if 61 - 61: I11i . iIi1i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
 if 65 - 65: ooOoO0O00 * Oooo0O0oo00oO * ii - iIi1i1ii1 . iiII11i1I1IIi - oO0o
elif OOooO0oo0o00o == 1020 :
 II1111i11i11 ( )
 if 71 - 71: IIi * OOooOOo
elif OOooO0oo0o00o == 1021 :
 ANIMEEP ( )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % OooOO000 * I11i
elif OOooO0oo0o00o == 1022 :
 ANIMEPLAY ( ooO0oOOooOo0 )
 if 64 - 64: OOoOoo / OOoOoo + Ii1I * Oooo0O0oo00oO % Oooo0O0oo00oO
elif OOooO0oo0o00o == 1001 :
 ooO0O0OOO ( )
 if 87 - 87: oO0o * I1ii11iIi11i
elif OOooO0oo0o00o == 1005 :
 I11Ii1 ( )
 if 83 - 83: ooOoO0O00 * OooOO000 - iIi1i1ii1 / IIi
elif OOooO0oo0o00o == 1007 :
 oO0O ( ooO0oOOooOo0 )
 if 48 - 48: O0oOO0 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif OOooO0oo0o00o == 1010 :
 I11Ii1iI11iI1 ( ooO0oOOooOo0 )
 if 32 - 32: IIi * oOo0O0Ooo - Oooo0O0oo00oO . I1ii11iIi11i / o0o00Oo0O + IIi
elif OOooO0oo0o00o == 1011 :
 OOOoOOooOoo ( ooO0oOOooOo0 )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif OOooO0oo0o00o == 1012 :
 I1i11iiiiI1I ( ooO0oOOooOo0 )
 if 7 - 7: Ii % Ii1I / OooOO000 % I1ii11iIi11i - oO0o
elif OOooO0oo0o00o == 1030 :
 O00OO0oOOO ( )
 if 73 - 73: Ii1I
elif OOooO0oo0o00o == 1031 :
 I1ii11ii1iiI ( ooO0oOOooOo0 , IiIIi1 )
 if 92 - 92: Ii + o0o00Oo0O * oo0oO00
elif OOooO0oo0o00o == 1032 :
 OO0 ( ooO0oOOooOo0 )
 if 60 - 60: I11i / I1ii11iIi11i
elif OOooO0oo0o00o == 1006 :
 Parse . ParseURL ( ooO0oOOooOo0 )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif OOooO0oo0o00o == 2030 :
 Parse . addonParseURL ( ooO0oOOooOo0 )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % OooOO000 / Ii1I
elif OOooO0oo0o00o == 2031 :
 Parse . apkParseURL ( ooO0oOOooOo0 )
 if 76 - 76: oO0o * O0oOO0 - oO0o
elif OOooO0oo0o00o == 1002 :
 OO0o0 ( ooO0oOOooOo0 )
 if 57 - 57: ii / OOooOOo + O0oOO0 . IIi
elif OOooO0oo0o00o == 1003 :
 oO0o00o0o0OO0O0 ( ooO0oOOooOo0 , IiIIi1 )
 if 14 - 14: Ii % Oooo0O0oo00oO * I11i * OOooOOo
elif OOooO0oo0o00o == 1004 :
 IiiiI1 ( ooO0oOOooOo0 )
 if 55 - 55: OooOO000 * Oooo0O0oo00oO * OooOO000
elif OOooO0oo0o00o == 1008 :
 oooooOOo0Oo ( )
 if 70 - 70: o0o00Oo0O . IIi
elif OOooO0oo0o00o == 1009 :
 o00OooOOoOoo ( ooO0oOOooOo0 )
 if 33 - 33: Oooo0O0oo00oO * IIi
elif OOooO0oo0o00o == 2001 :
 OO0o0o ( )
 if 64 - 64: Ii . iI11I1II1I1I
elif OOooO0oo0o00o == 2002 :
 I1I1i1 ( ooO0oOOooOo0 )
 if 7 - 7: OOooOOo % OOoOoo + OOooOOo - OOooOOo * Ii % oO0o
elif OOooO0oo0o00o == 1013 :
 i1iiIII1IIiIIII ( )
elif OOooO0oo0o00o == 10111113 :
 i11i11 ( ooO0oOOooOo0 )
 if 57 - 57: Oooo0O0oo00oO / oO0o + Ii1I
elif OOooO0oo0o00o == 1014 :
 o0ooO0Oo ( )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % Oooo0O0oo00oO + iIi1i1ii1 . oO0o . I1ii11iIi11i
elif OOooO0oo0o00o == 1015 :
 O00oO0oo ( ooO0oOOooOo0 )
 if 70 - 70: oo0oO00 . Ii1I * O0oOO0
elif OOooO0oo0o00o == 1016 :
 IiIi1I1 ( ooO0oOOooOo0 , IiIIi1 , Oo0OO )
 if 97 - 97: O0oOO0 . iI11I1II1I1I - Oooo0O0oo00oO
elif OOooO0oo0o00o == 1017 :
 ooO ( )
 if 23 - 23: Ii1I % oo0oO00
elif OOooO0oo0o00o == 1018 :
 I1ii1 ( ooO0oOOooOo0 )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif OOooO0oo0o00o == 1023 :
 iiOO0O0Ooo ( )
 if 99 - 99: OooOO000 - Ii1I - oOo0O0Ooo - OooOO000 + oO0o + IIiIiII11i
elif OOooO0oo0o00o == 1024 :
 ii1ii1111 ( ooO0oOOooOo0 )
 if 34 - 34: OooOO000 * oo0oO00
elif OOooO0oo0o00o == 1025 :
 iII11iiii111i ( ooO0oOOooOo0 )
 if 31 - 31: iIi1i1ii1 . O0oOO0
elif OOooO0oo0o00o == 4001 :
 Ooo0OOoOoO0 ( )
 if 40 - 40: IIi - oo0oO00 / IIiIiII11i * ooOoO0O00 + iIi1i1ii1 * IIiIiII11i
elif OOooO0oo0o00o == 4002 :
 o00Oo0oooooo ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - OooOO000
elif OOooO0oo0o00o == 4003 :
 Iii1Ii ( )
 if 99 - 99: IIi - iIi1i1ii1 - ooOoO0O00 / Ii . iIi1i1ii1
elif OOooO0oo0o00o == 4004 :
 ooOoo ( )
 if 58 - 58: Oooo0O0oo00oO
elif OOooO0oo0o00o == 4005 :
 I1III1111iIi ( )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif OOooO0oo0o00o == 4006 :
 I1I ( )
 if 64 - 64: OOooOOo + iIi1i1ii1 - ooOoO0O00 . IIiIiII11i . oO0o
elif OOooO0oo0o00o == 4007 :
 OooOo0oo0O0o00O ( )
 if 31 - 31: O0oOO0 . iiII11i1I1IIi - oo0oO00 . iI11I1II1I1I + oo0oO00 . OOooOOo
elif OOooO0oo0o00o == 4008 :
 IIIIiii1IIii ( )
 if 86 - 86: Ii1I - Ii1I / iiII11i1I1IIi - Ii1I * iiII11i1I1IIi + OooOO000
elif OOooO0oo0o00o == 4009 : iiI ( )
elif OOooO0oo0o00o == 4010 : o0Oii1111i ( )
elif OOooO0oo0o00o == 3000 :
 i1iII1iii ( )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - iIi1i1ii1
elif OOooO0oo0o00o == 3001 :
 IIi1i1ii11I1 ( )
 if 30 - 30: ii % Oooo0O0oo00oO
elif OOooO0oo0o00o == 3002 :
 oOoO0OO ( ooO0oOOooOo0 )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - Oooo0O0oo00oO
elif OOooO0oo0o00o == 3003 :
 o0OOO ( ooO0oOOooOo0 )
 if 81 - 81: iiII11i1I1IIi % IIi . OOoOoo
elif OOooO0oo0o00o == 3004 :
 OOo0o0O0 ( ooO0oOOooOo0 )
 if 66 - 66: Ii1I * IIi / ii * o0o00Oo0O % Oooo0O0oo00oO
elif OOooO0oo0o00o == 404 :
 iiIIiIi1i1I1 ( Oo0OO , ooO0oOOooOo0 , IiIIi1 )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * IIi / OooOO000 * ii
elif OOooO0oo0o00o == 405 :
 oO0oO0OoO00 ( ooO0oOOooOo0 )
 if 82 - 82: I1ii11iIi11i / IIi / IIi % IIi
elif OOooO0oo0o00o == 7030 :
 IiI1I1i1 ( )
 if 20 - 20: OOoOoo
elif OOooO0oo0o00o == 7021 :
 I1IIiiiiI1iIi ( Oo0OO )
 if 63 - 63: iI11I1II1I1I . oO0o
elif OOooO0oo0o00o == 7022 :
 OOOo0ooOO ( Oo0OO )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif OOooO0oo0o00o == 7000 :
 iiIII1iIiI1Ii11Iiii ( Oo0OO , ooO0oOOooOo0 , img )
 if 26 - 26: Oooo0O0oo00oO . oO0o % OOooOOo
elif OOooO0oo0o00o == 7050 :
 I1iIIII1 ( ooO0oOOooOo0 )
 if 94 - 94: iIi1i1ii1
elif OOooO0oo0o00o == 7051 :
 i1II1i1iiI1 ( ooO0oOOooOo0 )
 if 15 - 15: IIi - iIi1i1ii1 / o0o00Oo0O
elif OOooO0oo0o00o == 7052 :
 o0oo ( ooO0oOOooOo0 )
 if 28 - 28: OooOO000 . ooOoO0O00 / Ii1I
elif OOooO0oo0o00o == 7053 :
 O0oooOO ( ooO0oOOooOo0 )
 if 77 - 77: Ii / OooOO000 / Ii % OOooOOo - OooOO000
elif OOooO0oo0o00o == 7054 :
 CoolPlay ( ooO0oOOooOo0 )
 if 80 - 80: OooOO000 % OOooOOo . ii . IIiIiII11i % iIi1i1ii1
elif OOooO0oo0o00o == 7060 :
 ii111Ii1i ( )
 if 6 - 6: OooOO000 % iIi1i1ii1 / IIi + OooOO000 . O0oOO0
elif OOooO0oo0o00o == 7061 :
 I11Iiii1I ( ooO0oOOooOo0 )
 if 70 - 70: iI11I1II1I1I / IIi
elif OOooO0oo0o00o == 7063 :
 IiI1I1II ( ooO0oOOooOo0 )
 if 61 - 61: o0o00Oo0O * I11i + OooOO000 - Oooo0O0oo00oO . oOo0O0Ooo - iIi1i1ii1
elif OOooO0oo0o00o == 7062 :
 Ooo0o0o0ooo ( ooO0oOOooOo0 )
 if 7 - 7: Ii1I
elif OOooO0oo0o00o == 7064 :
 NATatozcat ( )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / oo0oO00
elif OOooO0oo0o00o == 7067 :
 oO0O0ooO0oOO ( ooO0oOOooOo0 )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif OOooO0oo0o00o == 7066 :
 NATatozA ( ooO0oOOooOo0 )
 if 13 - 13: Ii
elif OOooO0oo0o00o == 7065 :
 oO0000Oo ( ooO0oOOooOo0 )
 if 54 - 54: Oooo0O0oo00oO . Ii1I * oo0oO00 % OooOO000 . o0o00Oo0O * iIi1i1ii1
elif OOooO0oo0o00o == 7070 :
 o00OoOO00 ( )
 if 87 - 87: IIi % Ii1I * I1ii11iIi11i
elif OOooO0oo0o00o == 7071 :
 DIZIlist ( ooO0oOOooOo0 )
 if 59 - 59: I1ii11iIi11i / oo0oO00 - iI11I1II1I1I * iI11I1II1I1I
elif OOooO0oo0o00o == 7072 :
 DIZIpull ( ooO0oOOooOo0 )
 if 18 - 18: oo0oO00 * Ii1I / Ii / iI11I1II1I1I * ii . Oooo0O0oo00oO
elif OOooO0oo0o00o == 7073 :
 WATCHDIZI ( ooO0oOOooOo0 )
 if 69 - 69: I1ii11iIi11i * OOoOoo
elif OOooO0oo0o00o == 7002 :
 o0oi1i1ii11IiI ( )
 if 91 - 91: I11i . OOoOoo / oO0o / Ii * I11i
elif OOooO0oo0o00o == 7003 :
 O0o0Oo0o00o ( ooO0oOOooOo0 )
 if 52 - 52: oOo0O0Ooo - Ii / iIi1i1ii1 . O0oOO0
elif OOooO0oo0o00o == 7004 :
 iiIiooOo0oo0O0O ( ooO0oOOooOo0 )
 if 38 - 38: O0oOO0 + ii * OOooOOo % O0oOO0
elif OOooO0oo0o00o == 7020 :
 IiI1I ( ooO0oOOooOo0 )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif OOooO0oo0o00o == 7001 :
 O0o0oO ( )
 if 24 - 24: OOooOOo * IIi
elif OOooO0oo0o00o == 7010 :
 ooooooo0oOo0 ( ooO0oOOooOo0 )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif OOooO0oo0o00o == 7011 :
 iIIii ( ooO0oOOooOo0 )
 if 81 - 81: Oooo0O0oo00oO
elif OOooO0oo0o00o == 7012 :
 iiii1ii1 ( ooO0oOOooOo0 )
 if 58 - 58: IIiIiII11i . OooOO000 . IIi * ii / IIi / oo0oO00
elif OOooO0oo0o00o == 7013 :
 cnfTVPlay2 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Oo0OO , ooO0oOOooOo0 , IiIIi1 )
elif OOooO0oo0o00o == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOooO0oo0o00o == 7018 :
 iIi1i1I1I ( )
elif OOooO0oo0o00o == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooO0oOOooOo0 )
 if 41 - 41: oo0oO00 + oO0o . iiII11i1I1IIi
elif OOooO0oo0o00o == 8000 :
 iiIiI11IiI ( )
elif OOooO0oo0o00o == 8001 :
 iIi1Iii11111I1iii ( )
elif OOooO0oo0o00o == 8002 :
 oooOo0OO ( )
elif OOooO0oo0o00o == 8003 :
 o0OO0Oooo ( )
elif OOooO0oo0o00o == 8004 :
 o0000OOOo ( )
elif OOooO0oo0o00o == 8005 :
 oo0o ( )
elif OOooO0oo0o00o == 8006 :
 Iii1i11 ( Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8030 :
 ii1I11i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8045 :
 Ii11ii1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8046 :
 iiiIiiiI1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8047 :
 OO000OOOo0Oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8048 :
 OoiIiiII ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8049 :
 iII1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 804900 :
 o00oOOo0Oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8020 :
 I1o0OooOOOOOO ( )
elif OOooO0oo0o00o == 8021 :
 I1IiiI11 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8022 :
 iIII1II11I1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8023 :
 O000oOo0OO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8040 :
 ii1I1IIii11 ( )
elif OOooO0oo0o00o == 8041 :
 oOoOOoo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8042 :
 o0OOOO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8043 :
 yt . PlayVideo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8044 :
 OOoo0OOOo0o ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8060 :
 Ooo0O0oooo ( )
elif OOooO0oo0o00o == 8061 :
 i1IIIII1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8064 :
 OOooO0o0 ( )
elif OOooO0oo0o00o == 8065 :
 iII111iiiI11i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8070 :
 oO0o00 ( )
elif OOooO0oo0o00o == 8071 :
 Oo0OOOO0oOoo0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7080 :
 O0OIIII1i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8090 :
 I1ii1i11iI1 ( )
elif OOooO0oo0o00o == 8091 :
 oOo0O0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8092 :
 O00oIi11Iiii1iiii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8093 :
 iIi1iI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8081 :
 oOoO0o0o ( )
elif OOooO0oo0o00o == 8062 :
 oo0OoOO000O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8063 :
 iiI1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8050 :
 i11oo ( )
elif OOooO0oo0o00o == 8051 :
 iiIIiii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8052 :
 oooOo0oOO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8085 :
 iiIi ( )
elif OOooO0oo0o00o == 8086 :
 i1111I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8087 :
 OoOiII11IiIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 8088 :
 iII1I1i ( ooO0oOOooOo0 , Oo0OO )
elif OOooO0oo0o00o == 9000 :
 o00Ooo0 ( )
elif OOooO0oo0o00o == 1111 :
 i1III1 ( )
elif OOooO0oo0o00o == 9001 :
 i1O0 ( )
elif OOooO0oo0o00o == 9002 :
 iiI11i1II ( )
elif OOooO0oo0o00o == 9003 :
 o0o0ooOO0 ( )
elif OOooO0oo0o00o == 9004 :
 World1 ( )
elif OOooO0oo0o00o == 9005 :
 World2 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9006 :
 World3 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9007 :
 OOO0 ( )
elif OOooO0oo0o00o == 9008 :
 I11ii1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9009 :
 i1iIi1iiii1ii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9010 :
 iIIiIiii1 ( )
elif OOooO0oo0o00o == 9011 :
 oo0OO0Oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 50 :
 iIiI1I1ii1I1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9020 :
 champlist ( )
elif OOooO0oo0o00o == 9021 :
 iiO00O ( )
elif OOooO0oo0o00o == 9022 :
 IIIIIi1 ( )
elif OOooO0oo0o00o == 9023 :
 o0oIi1iiiii ( )
elif OOooO0oo0o00o == 9024 :
 OOI1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9030 :
 IiiIi1iIIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9031 :
 ii1IO0oo00o000 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9032 :
 II1111iiI1II ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9033 :
 OoOOOO00 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 9034 :
 IIIIiIiIi1 ( )
elif OOooO0oo0o00o == 7085 :
 Iiiiii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7086 :
 I1111IiII1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 7087 :
 iiiiI11 ( oo000ii )
elif OOooO0oo0o00o == 9666 :
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10100 : ii11 ( )
elif OOooO0oo0o00o == 101001 : Ii1I1iIiiI1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10105 : ooo0O0O0oo0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10106 : oo000oO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10104 : ooOoO0OoO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10107 : o00i111iiIiiIiI ( )
elif OOooO0oo0o00o == 10103 : IiIiII11i1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10108 : IiI11Ii1iI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10000 : Origin_Menu ( )
elif OOooO0oo0o00o == 10001 : oOOo0OOOOo0Oo ( )
elif OOooO0oo0o00o == 10002 : I1i111I ( )
elif OOooO0oo0o00o == 10003 : II1i11I ( )
elif OOooO0oo0o00o == 10004 : ooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10005 : O0Oo00 ( )
elif OOooO0oo0o00o == 10006 : Ii1iiI1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10007 : iIi1ooo0Oooooo ( ooO0oOOooOo0 , IiIIi1 )
elif OOooO0oo0o00o == 10008 : o0oOOoO000 ( )
elif OOooO0oo0o00o == 10009 : iI1 ( )
elif OOooO0oo0o00o == 10010 : iI1iiiiiii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10011 : O0o0O0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10012 : III111i11IiI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10109 : o0o0Oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10013 : IiiIiiIIII ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10014 : oOoo0ooOoo ( )
elif OOooO0oo0o00o == 10015 : o0oOo0OO ( )
elif OOooO0oo0o00o == 10016 : i1i1i1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10017 : Oooooooo00o00 ( )
elif OOooO0oo0o00o == 10018 : i1oooOoOoOO ( )
elif OOooO0oo0o00o == 10019 : iii1IiiiI1i1 ( )
elif OOooO0oo0o00o == 10020 : oOOO000o0O0O ( )
elif OOooO0oo0o00o == 10021 : ooOooOO0 ( )
elif OOooO0oo0o00o == 10022 : oooO0o0oOoO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10023 : i1IiI1ii1i ( Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10024 : i11Ii1IiIIIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10025 : iIIiIiI1I1 ( )
elif OOooO0oo0o00o == 10026 : ii111I11Ii ( )
elif OOooO0oo0o00o == 10027 : OooO0O ( )
elif OOooO0oo0o00o == 10028 : ooO0 ( )
elif OOooO0oo0o00o == 10029 : oOoi1I111II ( )
elif OOooO0oo0o00o == 423 : o0oOoO00 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 426 : III11I11ii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10030 : Izle_Films ( )
elif OOooO0oo0o00o == 10031 : Latest_Izle_Movies ( )
elif OOooO0oo0o00o == 10032 : Izle_Genres ( )
elif OOooO0oo0o00o == 10033 : Izle_Pop_Movies ( )
elif OOooO0oo0o00o == 10034 : Izle_Boxsets ( )
elif OOooO0oo0o00o == 10035 : Izle_Search ( )
elif OOooO0oo0o00o == 10036 : Izle_Genres_Movie ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10037 : Izle_Boxset_single ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10038 : Izle_IFRAME ( )
elif OOooO0oo0o00o == 10039 : Izle_Boxsets_Next ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10040 : OO0O0OOo0O ( )
elif OOooO0oo0o00o == 10041 : o0OoO0000oOO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10042 : I11iiIi1i1IIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10043 : oOIIIi11 ( )
elif OOooO0oo0o00o == 10044 : iiIIiIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10045 : o0Oo ( Oo0OO )
elif OOooO0oo0o00o == 10046 : i1Ii1i1I11III ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10047 : ii1I11iI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10048 : IiIiI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10049 : Oo0000o ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10050 : OO ( )
elif OOooO0oo0o00o == 10051 : o0i111 ( )
elif OOooO0oo0o00o == 10052 : O0oOO0o00OO ( )
elif OOooO0oo0o00o == 10053 : Addon ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10054 : OOOIII1i ( ooO0oOOooOo0 , Oo0OO )
elif OOooO0oo0o00o == 10055 :
 iII1IIiiI11II ( "addFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 IiIIi11i ( Oo0OO , ooO0oOOooOo0 , IiIIi1 , iiI11ii1I1 , O0OoOOo )
elif OOooO0oo0o00o == 10056 :
 iII1IIiiI11II ( "rmFavorite" )
 try :
  Oo0OO = Oo0OO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OO = Oo0OO . split ( '  - ' ) [ 0 ]
 except :
  pass
 i11i11Iiii11i ( Oo0OO )
elif OOooO0oo0o00o == 10057 :
 iII1IIiiI11II ( "getFavorites" )
 II1IIii1ii ( )
elif OOooO0oo0o00o == 10058 : oOIIiIi ( )
elif OOooO0oo0o00o == 10059 : Donators_Guide ( )
elif OOooO0oo0o00o == 10060 : oOo0OOoO0 ( )
elif OOooO0oo0o00o == 10061 : oOOOiIi1I1 ( )
elif OOooO0oo0o00o == 10062 : oOo0OooOo ( Oo0OO , ooO0oOOooOo0 , oo000ii )
elif OOooO0oo0o00o == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif OOooO0oo0o00o == 10064 : ooO00O00oOO ( )
elif OOooO0oo0o00o == 10065 : oO0oooooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10066 : iIIi1I1ii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10068 : ooo0OO0O0Oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10069 : iiIII1i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10070 : IIi11I1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10071 : Genie_Watch ( )
elif OOooO0oo0o00o == 10072 : o000 ( )
elif OOooO0oo0o00o == 10073 : oo00OOoOoO00 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10074 : oOooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10075 : iiiI1ii11 ( IiIIi1 , Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10076 : iIIiiIIi1IiI ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10077 : oO00OoOO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10078 : OOOoO ( )
elif OOooO0oo0o00o == 10079 : Genie_Watch_Tv_Shows ( )
elif OOooO0oo0o00o == 10080 : Genie_Watch_Tv_Genre ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10081 : Genie_Watch_TV_PlayRun ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10082 : Genie_Watch_TV_Episodes ( ooO0oOOooOo0 , IiIIi1 )
elif OOooO0oo0o00o == 10083 : Genie_Watch_Tv_Recent ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 10084 : iiiI ( )
elif OOooO0oo0o00o == 10085 : OOoO00 ( )
elif OOooO0oo0o00o == 10086 : i1IiiiI1iI ( )
elif OOooO0oo0o00o == 20000 : OOo0o ( )
elif OOooO0oo0o00o == 20001 : iiIi1i1Ii1Ii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 20002 : i1I111I1Iii1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 20003 : ooo0ii1iIIi11 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 20004 : oOO0Oooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 20005 : oO0O0o0O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 21004 : ii1IiIIi1i ( )
elif OOooO0oo0o00o == 21005 : II1i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 21006 : iiiiIiIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 21007 : I11iIooOo0O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30000 : Iii111IiIii ( )
elif OOooO0oo0o00o == 30001 : OOo00ooOoO0o ( )
elif OOooO0oo0o00o == 10012 : Resolve ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30003 : oOOOOOo ( )
elif OOooO0oo0o00o == 30004 : iiiI1iI1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30005 : III11I1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30006 : IIiii11ii1i ( )
elif OOooO0oo0o00o == 30007 : Ii11iiI1 ( )
elif OOooO0oo0o00o == 30008 : Oo0o00ooOOOoOo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30009 : Iiii1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30010 : oOo0OO0o0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30011 : iiIiIIII1iiIIi ( )
elif OOooO0oo0o00o == 30012 : oOoO0ooO0000 ( )
elif OOooO0oo0o00o == 30013 : I1iiiI ( )
elif OOooO0oo0o00o == 30014 : OoO0 ( )
elif OOooO0oo0o00o == 30015 : Ooo0oO ( ooO0oOOooOo0 , IiIIi1 , iiI11ii1I1 )
elif OOooO0oo0o00o == 30016 : iIIIIiiii1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30019 : O000o0oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30017 : O00o0O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30018 : II11Ii111II1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30030 : oO00o00 ( )
elif OOooO0oo0o00o == 30031 : oOOOO ( )
elif OOooO0oo0o00o == 30032 : I1i11 ( )
elif OOooO0oo0o00o == 30033 : OOooooO0o0O0 ( )
elif OOooO0oo0o00o == 30034 : oO0oo ( )
elif OOooO0oo0o00o == 30035 : OoOoO0OooOOo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30036 : oOIIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30037 : I1Ii1IIiI11i1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 30038 : i11iIIi ( )
elif OOooO0oo0o00o == 30039 : oO0O0OO0O ( )
elif OOooO0oo0o00o == 50000 : oOO0O00Oo0O0o ( )
elif OOooO0oo0o00o == 50001 : O0oo0O0 ( )
elif OOooO0oo0o00o == 50002 : oO0ooo0O0Ooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 50003 : I11iIiI1 ( oo000ii )
elif OOooO0oo0o00o == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OOooO0oo0o00o == 60001 : iiii11ii ( )
elif OOooO0oo0o00o == 60002 : IIIiiiI ( Oo0OO )
elif OOooO0oo0o00o == 60003 : Ii1iIi111i1i1 ( Oo0OO )
elif OOooO0oo0o00o == 50004 : iI1111iiii ( )
elif OOooO0oo0o00o == 50005 : speedtest . runtest ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 70001 : ii11I11i ( )
elif OOooO0oo0o00o == 70002 : oOo0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 70003 : OOOOo000o00OO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 70004 : Oo0oOo0O0o000Ooo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 70005 : oooo00o0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 70006 : I1IiI ( )
elif OOooO0oo0o00o == 50006 : OOOiiiiI ( i1 , i1111 )
elif OOooO0oo0o00o == 80000 : i1i ( )
elif OOooO0oo0o00o == 80001 : resolvefilmon ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80002 : oOOo0OoOOOoo ( )
elif OOooO0oo0o00o == 80003 : iIi11i ( Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80004 : O0o0OO00 ( Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80005 : oo00O0oO0O0 ( )
elif OOooO0oo0o00o == 80006 : II1I1iiIII1I1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80007 : o0Ooo0o0ooo0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80008 : oo0o0000Oo0 ( )
elif OOooO0oo0o00o == 80009 : o00OOo0o ( )
elif OOooO0oo0o00o == 80010 : IiIiIo00O0oo0 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80011 : iIo00oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 80012 : i11IiIi ( )
elif OOooO0oo0o00o == 90000 : I11i1i11IiIi1 ( Oo0OO , ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90001 : I1I1i1I ( )
elif OOooO0oo0o00o == 90002 : I11iI ( )
elif OOooO0oo0o00o == 90003 : iiiIIi ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90004 : OOoOo0O00oo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90005 : oo0oO0oOo0O ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90006 : iII1IiiIIIIii ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90007 : oOOOIii1IiiII1Ii1 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90008 : o0oo00oo0oO ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90009 : Ii1iii11I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90010 : oooOo0OOOoo0 ( )
elif OOooO0oo0o00o == 90020 : iiI1iIII1ii ( )
elif OOooO0oo0o00o == 90021 : hellyeah2 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90022 : hellyeah3 ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90023 : o00oO00 ( )
elif OOooO0oo0o00o == 90024 : OO0oO0o ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 90025 : catchuptv2 ( ooO0oOOooOo0 )
if 73 - 73: Ii * oOo0O0Ooo + I11i / O0oOO0
if 56 - 56: ooOoO0O00
elif OOooO0oo0o00o == 100001 : Stand_up ( )
if 11 - 11: Ii % I11i / oo0oO00 * ii
elif OOooO0oo0o00o == 100003 : i1i1i1I ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100004 : I111i1II ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100005 : Resolve ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100008 : Search ( )
elif OOooO0oo0o00o == 100007 : Ii11i1I11i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100009 : yt . PlayVideo ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100010 : ii1iIi1iIiI1i ( ooO0oOOooOo0 )
elif OOooO0oo0o00o == 100100 : OO0ooo0oOO ( IiIIi1 , ooO0oOOooOo0 , o00O00 )
elif OOooO0oo0o00o == 100101 : i1Ii1iii ( ooO0oOOooOo0 , Oo0OO , iiI11ii1I1 , o00O00 , IiIIi1 )
elif OOooO0oo0o00o == 100102 : O0oOo00o0o00O ( Oo0OO , ooO0oOOooOo0 , IiIIi1 , iiI11ii1I1 )
elif OOooO0oo0o00o == 100106 : iIi1 ( ooO0oOOooOo0 , Oo0OO )
elif OOooO0oo0o00o == 100107 : O0O0oOOo0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
