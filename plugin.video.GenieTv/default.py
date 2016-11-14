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
IiiIII111iI = "3.2.8"
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
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , OO0o , '' )
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
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , OO0o , '' )
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
 o0OIiII ( '[COLOR' + iiI1IiI + ']Todays Games[/COLOR]' , str ( ooOO0O0ooOooO ) , 90030 , oOOOo00O00oOo + 'tgames.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Tommys Replays[/COLOR]' , str ( ooOO0O0ooOooO ) , 90031 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 51 - 51: I1ii11iIi11i / OOooOOo . Oooo0O0oo00oO * I11i + oO0o * iIi1i1ii1
def OOOoOo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 o00oooO0Oo = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for I11iII , iIIII in o00oooO0Oo :
  OOOiiiiI ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]  ' + I11iII , iIIII )
def I11iI1i1I11I11 ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 O00o0 = O0 ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 o00oooO0Oo = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
def I1i1i1iii ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( O00o0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , I1111i , OO0o , '' )
 for url in next :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , oOOOo00O00oOo + 'NEXT.png' , OO0o , '' )
def iIIii ( url ) :
 O00o0 = O0 ( url )
 o00O0O = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 ii1iii1i = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o00oooO0Oo = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for o000O0O , url in o0O0OOO0Ooo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for o000O0O , url in ii1iii1i :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for url in o00O0O :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
  if 35 - 35: IIiIiII11i % Oooo0O0oo00oO . OOoOoo + OOoOoo % IIiIiII11i % IIiIiII11i
def ooOoO00 ( url ) :
 if 'drive' in url :
  Ii1IIiI1i ( url )
 else :
  O00o0 = O0 ( url )
  o00oooO0Oo = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( O00o0 )
  for url in o00oooO0Oo :
   Ii1IIiI1i ( url )
def o0O00Oo0 ( url ) :
 IiII111i1i11 = liveresolver . resolve ( url )
 i111iIi1i1II1 = xbmcgui . ListItem ( path = IiII111i1i11 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111iIi1i1II1 )
def oooO ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 i1I1i111Ii = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I1i111Ii )
def I1iIIiiIIi1i ( ) :
 ooo = False
 if os . path . exists ( os . path . join ( II , 'xbmc.log' ) ) :
  ooo = os . path . join ( II , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II , 'kodi.log' ) ) :
  ooo = os . path . join ( II , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II , 'spmc.log' ) ) :
  ooo = os . path . join ( II , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II , 'tvmc.log' ) ) :
  ooo = os . path . join ( II , 'tvmc.log' )
 return ooo
 if 27 - 27: OOoOoo % oOo0O0Ooo
def o0oooOO00 ( url ) :
 if url == 'http://' : return False
 try :
  OOO00O = urllib2 . Request ( url )
  OOO00O . add_header ( 'User-Agent' , I1i1iiI1 )
  OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
  OOoOO0oo0ooO . close ( )
 except Exception , iiIiii1IIIII :
  return iiIiii1IIIII
 return True
 if 67 - 67: IIi / iIi1i1ii1
def iiIiIIIiiI ( ) :
 O0o0O00Oo0o0 = O0 ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 if len ( o00oooO0Oo ) > 0 :
  for o000O0O , ooO0oOOooOo0 , iiI1IIIi , II11IiIi11 in o00oooO0Oo :
   o0OIiII ( o000O0O , ooO0oOOooOo0 , 50005 , iiI1IIIi , II11IiIi11 , '' )
def IIOOO0O00O0OOOO ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I1iiii1I ( )
  if O0oO0 == 1 :
   OOo0 ( )
  if O0oO0 == 2 :
   oO00ooooO0o ( oo0o )
  if O0oO0 == 3 :
   o0oO0oooOoo ( ooO0oOOooOo0 )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 7 - 7: OooOO000 * oO0o - OOoOoo + Oooo0O0oo00oO * oOo0O0Ooo % oO0o
def iI1i111I1Ii ( ) :
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
   if 25 - 25: OooOO000 - iiII11i1I1IIi
   if 10 - 10: IIiIiII11i / O0oOO0 % ii * oo0oO00 % Ii1I
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , OO0o , '' )
  if 48 - 48: OOoOoo / OooOO000 . iI11I1II1I1I * OOooOOo * O0oOO0 / ooOoO0O00
  if 92 - 92: I1ii11iIi11i % I1ii11iIi11i - I11i / OOooOOo
  if 10 - 10: iiII11i1I1IIi + I1ii11iIi11i * Ii1I + iI11I1II1I1I / OooOO000 / Ii1I
  if 42 - 42: oOo0O0Ooo
  if 38 - 38: Oooo0O0oo00oO + IIiIiII11i % OOoOoo % OOooOOo - IIi / ii
  if 73 - 73: I11i * o0o00Oo0O - Ii
  if 85 - 85: IIi % iiII11i1I1IIi + oo0oO00 / I11i . O0oOO0 + Oooo0O0oo00oO
  if 62 - 62: Ii + Ii - I11i
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , OO0o , '' )
  if 28 - 28: iiII11i1I1IIi . iiII11i1I1IIi % iI11I1II1I1I * iI11I1II1I1I . I11i / iiII11i1I1IIi
  if 27 - 27: oO0o + OOoOoo - ooOoO0O00
  if 69 - 69: iIi1i1ii1 - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
  if 79 - 79: o0o00Oo0O * Ii - iIi1i1ii1 / iIi1i1ii1
  if 48 - 48: o0o00Oo0O
  if 93 - 93: Ii - oOo0O0Ooo * Ii1I * oo0oO00 % o0o00Oo0O + ii
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I1i1i1 ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  OoO0O00O0oo0O ( )
 if O0oO0 == 1 :
  I1IiI11 ( )
 if O0oO0 == 2 :
  iI1iiiiIii ( )
 if O0oO0 == 3 :
  iIiIiIiI ( )
 if O0oO0 == 4 :
  i11OOoo ( )
 if O0oO0 == 5 :
  iIIiiiI ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , oo0 , o000O0O )
 if O0oO0 == 6 :
  IiI111ii1ii ( )
 if O0oO0 == 7 :
  O0OOo ( )
 if O0oO0 == 8 :
  IiIII1 ( )
 if O0oO0 == 9 :
  O0Oo000 ( )
 if O0oO0 == 10 :
  iiI11i1II ( )
  if 51 - 51: I11i % I1ii11iIi11i % I11i * o0o00Oo0O - Oooo0O0oo00oO % I1ii11iIi11i
  if 65 - 65: OOoOoo
def I11IiI ( ) :
 if not os . path . exists ( o0 ) :
  OOOiiiiI ( 'Change Log 9/11/16 - v3.2.6' , 'Freeview section added to streams 30+ channels, search series fixed, more movies and music added, Tommys Sports section updated with new football highlights section' )
  os . makedirs ( o0 )
  if 68 - 68: OOoOoo % Ii + IIiIiII11i
  if 52 - 52: Ii1I - I1ii11iIi11i + Ii1I % I11i
def OoO0O00O0oo0O ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   iI1 ( )
  if O0oO0 == 1 :
   IiI ( ooO0oOOooOo0 )
  if O0oO0 == 2 :
   iI1ii1i ( )
  if O0oO0 == 3 :
   Oo0oooO0oO ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0oO0 == 4 :
   IiIiII1 ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def Iii1iiIi1II ( ) :
 Oo00oo0oO ( )
 OO0O00oOo ( )
 if 14 - 14: oOo0O0Ooo
 if 19 - 19: oO0o - I1ii11iIi11i . O0oOO0 / O0oOO0 % OOoOoo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , OO0o , '' )
def iiI11i1II ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , Ooo , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Ooo , OO0o , '' )
 if 56 - 56: oOo0O0Ooo . o0o00Oo0O + I1ii11iIi11i
 if 1 - 1: iiII11i1I1IIi
 if 97 - 97: Oooo0O0oo00oO + iiII11i1I1IIi + o0o00Oo0O + Ii
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . iiII11i1I1IIi % iiII11i1I1IIi + Ii
def I1IiI11 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   Oo00o0OO0O00o ( )
  if O0oO0 == 1 :
   O0Oooo ( )
  if O0oO0 == 2 :
   iiIi1i ( )
  if O0oO0 == 3 :
   I1i11111i1i11 ( )
  if O0oO0 == 4 :
   OOoOOO0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I1I1i ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IIIiIiIi = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   IIIII1 = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iIi1Ii1i1iI = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   IIiI1 = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   i1iI1 = '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]'
  ii1I = [ I1IIIiIiIi , IIIII1 , iIi1Ii1i1iI , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , i1iI1 , '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , IIiI1 ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   iIIiiiI ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , oo0 , o000O0O )
  if O0oO0 == 1 :
   iIIiiiI ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , oo0 , o000O0O )
  if O0oO0 == 2 :
   ii1I1IiiI1ii1i ( )
  if O0oO0 == 3 :
   iIIiiiI ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , oo0 , o000O0O )
  if O0oO0 == 4 :
   O0o ( )
  if O0oO0 == 5 :
   iIIiiiI ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , oo0 , o000O0O )
  if O0oO0 == 6 :
   oO0OoO00o ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'TheReaper.png' , OO0o , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , OO0o , '' )
   if 11 - 11: I1ii11iIi11i - oOo0O0Ooo * IIiIiII11i . Ii1I . O0oOO0
   if 61 - 61: iiII11i1I1IIi % oOo0O0Ooo - I11i - IIiIiII11i % o0o00Oo0O
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , OO0o , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , OO0o , '' )
  if 90 - 90: iI11I1II1I1I + Ii1I + OOoOoo - OooOO000 * iIi1i1ii1 . Ii1I
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 37 - 37: OOoOoo % Ii % IIiIiII11i . o0o00Oo0O . IIi
def OO0oOOoo ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
def oOOO00o000o ( url ) :
 O00o0 = iIi11i1 ( url )
 url = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( O00o0 )
 for oO00oo0o00o0o , IiIIIIIi in o00oooO0Oo :
  if '[DIR]' in oO00oo0o00o0o :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in IiIIIIIi :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in IiIIIIIi :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
def O0o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 if 63 - 63: OOooOOo - ii % OooOO000
def oOi11iI11iIiIi ( url ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for o000O0O , url , O0ooo0 , I1iii11 , II11IiIi11 , ooo0O in o00oooO0Oo :
  if I1iii11 == '123' :
   I1iii11 = oOOOo00O00oOo + 'appstreams.png'
  if II11IiIi11 == '123' :
   II11IiIi11 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IiiiiI ( o000O0O , url , 100010 , I1iii11 , II11IiIi11 , ooo0O )
  elif 'playlist' in url :
   I1IiiiiI ( o000O0O , url , 100007 , I1iii11 , II11IiIi11 , ooo0O )
  elif 'watchseries' in url :
   I1IiiiiI ( o000O0O , url , 100100 , I1iii11 , II11IiIi11 , ooo0O )
  elif not 'http' in url :
   iII1iii ( o000O0O , url , 100009 , I1iii11 , II11IiIi11 , ooo0O , '' )
  else :
   iII1iii ( o000O0O , url , 100005 , I1iii11 , II11IiIi11 , ooo0O , '' )
   if 12 - 12: Oooo0O0oo00oO
def O0iII1 ( url ) :
 I1 = O00 ( url )
 IIII1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , I1111i , ooo0O , II11IiIi11 , o000O0O in IIII1i :
  if I1111i == '123' :
   I1111i = oOOOo00O00oOo + 'appstreams.png'
  if II11IiIi11 == '123' :
   II11IiIi11 = OO0o
  if 'php' in url :
   I1IiiiiI ( o000O0O , url , 100004 , I1111i , II11IiIi11 , ooo0O )
  elif 'playlist' in url :
   I1IiiiiI ( o000O0O , url , 100007 , I1111i , II11IiIi11 , ooo0O )
  elif 'watchseries' in url :
   I1IiiiiI ( o000O0O , url , 100100 , I1111i , II11IiIi11 , ooo0O )
  elif not 'http' in url :
   iII1iii ( o000O0O , url , 100009 , I1111i , II11IiIi11 , ooo0O , '' )
  else :
   iII1iii ( o000O0O , url , 100005 , I1111i , II11IiIi11 , ooo0O , '' )
   if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % O0oOO0 - IIiIiII11i - iiII11i1I1IIi
def iIi11iiIiI1I ( url ) :
 if 3 - 3: ooOoO0O00 / IIiIiII11i / Ii * ooOoO0O00 - IIiIiII11i
 I1 = O00 ( url )
 IiiII1111III1I = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for ii11i in IiiII1111III1I :
  I1iii11 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( ii11i ) )
  for I1iii11 in I1iii11 :
   I1iii11 = I1iii11
  o000O0O = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( ii11i ) )
  for o000O0O in o000O0O :
   if 'elete' in o000O0O :
    pass
   elif 'rivate Vid' in o000O0O :
    pass
   else :
    o000O0O = ( o000O0O ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  O00oOo00o0o = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( ii11i ) )
  for O00oOo00o0o in O00oOo00o0o :
   O00oOo00o0o = O00oOo00o0o
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( ii11i ) )
  for url in url :
   url = url
  iII1iii ( '[COLORred]' + str ( O00oOo00o0o ) + '[/COLOR] : ' + str ( o000O0O ) , str ( url ) , 100009 , str ( I1iii11 ) , OO0o , '' , '' )
  Iii1I1I11iiI1 ( 'movies' , '' )
  if 85 - 85: iiII11i1I1IIi + ii * iiII11i1I1IIi - OooOO000 % Ii
  if 71 - 71: Ii1I - OOoOoo / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
  if 53 - 53: OooOO000
  if 21 - 21: oo0oO00
  if 92 - 92: Ii / OooOO000 - iiII11i1I1IIi % OOoOoo * OooOO000 + I1ii11iIi11i
def ii1Oo0000oOo ( iconimage , url , extra ) :
 I1iii11 = ' '
 I11o0oO00oO0o0o0 = ' '
 II11IiIi11 = ' '
 I1I = ' '
 ooooo = O00 ( url )
 I1iii11 = re . compile ( '<img src="(.+?)">' ) . findall ( ooooo )
 for I1iii11 in I1iii11 :
  I1iii11 = I1iii11
 i11IIIiI1I = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( ooooo )
 for II11IiIi11 in i11IIIiI1I :
  II11IiIi11 = II11IiIi11
 o00oooO0Oo = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( ooooo )
 for url , I1I in o00oooO0Oo :
  I1I = 'S' + ( I1I ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o0O + url
  o0iiiI1I1iIIIi1 ( ( I1I ) . replace ( '  ' , '' ) , url , 100101 , I1iii11 , II11IiIi11 , I11o0oO00oO0o0o0 , '' )
  Iii1I1I11iiI1 ( 'Movies' , 'info' )
  if 17 - 17: iI11I1II1I1I . ii / oo0oO00 % IIiIiII11i % ooOoO0O00 / Ii
def OOOIiiiii1iI ( url , name , fanart , extra , iconimage ) :
 IIiooOooo0 = extra
 I1I = name
 ooooo = O00 ( url )
 I1iii11 = iconimage
 o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( ooooo )
 for url , name , oO0OO0 in o00oooO0Oo :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o0O + url
  oO0OO0 = oO0OO0
  o0O0Oo00 = name + ' - [COLORred]' + oO0OO0 + '[/COLOR]'
  o0iiiI1I1iIIIi1 ( o0O0Oo00 , url , 100102 , I1iii11 , fanart , 'Aired : ' + oO0OO0 , o0O0Oo00 )
  if 51 - 51: Oooo0O0oo00oO % iI11I1II1I1I - ii % OOoOoo * iI11I1II1I1I % oO0o
def oO0o00oOOooO0 ( name , URL , iconimage , fanart ) :
 I1 = O00 ( URL )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , name in o00oooO0Oo :
  for i111iIi1i1II1 in O00oO :
   if i111iIi1i1II1 in ooO0oOOooOo0 :
    URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
    iII1iii ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' , '' )
 if len ( o00oooO0Oo ) <= 0 :
  o0iiiI1I1iIIIi1 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 79 - 79: oO0o - iI11I1II1I1I + IIi - OooOO000
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
def ooO0o ( url , name ) :
 o000 = name
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 ii1iii1i = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  IiI1i ( url , o000 )
 for url in o0O0OOO0Ooo :
  IiI1i ( url , o000 )
 for url in ii1iii1i :
  IiI1i ( url , o000 )
  if 87 - 87: OOoOoo
def IiI1i ( url , season_name ) :
 if 'daclips.in' in url :
  IIIii ( url , season_name )
 elif 'filehoot.com' in url :
  O00OooOo00o ( url , season_name )
 elif 'allmyvideos.net' in url :
  IiI11i1IIiiI ( url , season_name )
 elif 'vidspot.net' in url :
  oOOo000oOoO0 ( url , season_name )
 elif 'vodlocker' in url :
  OoOo00o0OO ( url , season_name )
 elif 'vidto' in url :
  ii1IIIIiI11 ( url , season_name )
  if 40 - 40: I11i
  if 67 - 67: O0oOO0 + IIiIiII11i - o0o00Oo0O . O0oOO0 * IIiIiII11i * oo0oO00
def ii1IIIIiI11 ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO , o000O0O in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 51 - 51: iIi1i1ii1 * o0o00Oo0O / IIiIiII11i . IIi % Oooo0O0oo00oO / oOo0O0Ooo
  if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
def IiI11i1IIiiI ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO , o000O0O in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 30 - 30: iIi1i1ii1 + OooOO000 - iIi1i1ii1 . iIi1i1ii1 - IIiIiII11i + o0o00Oo0O
def oOOo000oOoO0 ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for o00OO00O0oOO , o000O0O in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 86 - 86: ooOoO0O00
def OoOo00o0OO ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 41 - 41: OOooOOo * oo0oO00 / OOooOOo % O0oOO0
def IIIii ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for o00OO00O0oOO in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 18 - 18: IIiIiII11i . ii % OOooOOo % IIi
def O00OooOo00o ( url , season_name ) :
 I1 = O00 ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO in o00oooO0Oo :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def Ii1iI111 ( Link , season_name ) :
 if 'http:/' in Link :
  ii1Ii1IiIIi ( Link )
  if 83 - 83: oo0oO00 / Ii1I
def II1Ii11Ii1i1I ( url ) :
 I1 = OPEN_URL_1 ( url )
 ii1iIi1II = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in ii1iIi1II :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 2 - 2: I1ii11iIi11i + OOooOOo - Oooo0O0oo00oO . oOo0O0Ooo - Oooo0O0oo00oO
def o0iiiI1I1iIIIi1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if 30 - 30: oo0oO00 / IIi . iIi1i1ii1 . ii - I1ii11iIi11i
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 44 - 44: o0o00Oo0O * ii % OOoOoo + IIiIiII11i
 if 39 - 39: O0oOO0 % iI11I1II1I1I % o0o00Oo0O % ii * Ii1I + iiII11i1I1IIi
def iII1iii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 68 - 68: I1ii11iIi11i + Ii
def Oo0oOooo000OO ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 98 - 98: I11i + o0o00Oo0O % ooOoO0O00 - Oooo0O0oo00oO + I1ii11iIi11i
def OoOo000oOo0oo ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 11 - 11: Ii - O0oOO0 . O0oOO0
def ii1Ii1IiIIi ( url ) :
 oO0O = xbmc . Player ( )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 31 - 31: Oooo0O0oo00oO / I1ii11iIi11i * ooOoO0O00 . OOooOOo
def O00 ( url ) :
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
  if 57 - 57: Oooo0O0oo00oO + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
  if 83 - 83: I11i / Ii % iI11I1II1I1I . oo0oO00 % O0oOO0 . ii
  if 94 - 94: IIi + iI11I1II1I1I % oO0o
def iIiIiIiI ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   O0OO0oOOo ( )
  if O0oO0 == 1 :
   OO0oO0o ( )
  if O0oO0 == 2 :
   III111i11IiI ( )
  if O0oO0 == 3 :
   O0000 ( )
  if O0oO0 == 4 :
   ooO00O0O0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def IiI111ii1ii ( ) :
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
 if 33 - 33: I1ii11iIi11i
 if 49 - 49: oO0o % iiII11i1I1IIi % iiII11i1I1IIi / iiII11i1I1IIi
 if 53 - 53: iI11I1II1I1I
def IiI111111IIII ( ) :
 I1 = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o00oooO0Oo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiIi1iI in o00oooO0Oo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   oooo00o0o0o = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOOiiiiI ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oooo00o0o0o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO0 == 0 :
    O0Oo00oO0O00 ( IIiIi1iI )
    o00O0 ( )
   elif O0oO0 == 1 :
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
 iIIIII1iiiiII = os . path . join ( iIi1ii1I1 , 'default.py' )
 oooOI111i1I1 = open ( iIIIII1iiiiII , "w+" )
 if 62 - 62: Oooo0O0oo00oO * OooOO000 / I1ii11iIi11i * I11i
 oooOI111i1I1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oooOI111i1I1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oooOI111i1I1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 29 - 29: I1ii11iIi11i % oO0o % iIi1i1ii1 . I11i / ii * OOoOoo
 if 54 - 54: o0o00Oo0O
 if 68 - 68: oO0o * I11i . OOoOoo % O0oOO0 % OooOO000
 if 75 - 75: OOooOOo
def i1OoOO ( ) :
 I1 = O0 ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O0 ( 'http://www.djing.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for iIII1I1i1i , I1111i , ooO0oOOooOo0 in o00oooO0Oo :
  O0OoO0ooOO0o ( iIII1I1i1i , 'http://www.tvcatchup.com' + ooO0oOOooOo0 , 90024 , 'http://www.tvcatchup.com' + I1111i )
 for ooO0oOOooOo0 , I1111i , o000O0O in o0O0OOO0Ooo :
  if 'Submit' in o000O0O :
   pass
  elif '&lt;' in o000O0O :
   pass
  else :
   o0OIiII ( 'DJing  ' + o000O0O , ooO0oOOooOo0 , 90025 , 'http://www.djing.com' + I1111i , OO0o , '' )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o0OIIiI1I1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def I11I1IIiiII1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 31 - 31: oOo0O0Ooo * O0oOO0 + ii - iiII11i1I1IIi / ii
def iI1ii1i ( ) :
 IiIi1iIIi1 ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O0 ( 'http://www.join4films.com/' )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def I111IIiii1Ii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , url , 80007 , I1111i )
 for url , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def II1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  url = ( url ) . replace ( ' ' , '%20' )
  Ii1IIiI1i ( url )
def iiIIIiIii ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://www.join4films.com/?s=' + ( I1i11II ) . replace ( ' ' , '+' ) + '&search_type=1'
 I1iii = II11 . lower ( )
 I111IIiii1Ii ( I1iii )
 if 51 - 51: Ii1I
 if 41 - 41: Ii1I * OOoOoo - IIi + I1ii11iIi11i
 if 23 - 23: IIiIiII11i % I11i + I11i + iiII11i1I1IIi - iiII11i1I1IIi
 if 62 - 62: I11i
 if 45 - 45: Oooo0O0oo00oO * OOoOoo
 if 74 - 74: ooOoO0O00 + o0o00Oo0O + I1ii11iIi11i
 if 5 - 5: I1ii11iIi11i * OOooOOo
 if 46 - 46: OOoOoo
 if 33 - 33: iiII11i1I1IIi - IIiIiII11i * ii - I1ii11iIi11i - Oooo0O0oo00oO
 if 84 - 84: OooOO000 + I1ii11iIi11i - OOooOOo * OOooOOo
 if 61 - 61: ii . O0oOO0 . ii / I1ii11iIi11i
 if 72 - 72: ooOoO0O00
 if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
 if 63 - 63: Ii1I
 if 6 - 6: OOoOoo / Ii1I
 if 57 - 57: oo0oO00
 if 67 - 67: oO0o . OOoOoo
def oO00oOo0OOO ( ) :
 I1IiiiiI ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 if 23 - 23: ooOoO0O00 . I11i * oO0o
def iIi1IiI ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://imoviemax.se/?s=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iii = II11 . lower ( )
 I11IIIiIi11 ( I1iii )
def I11iiIi1i1 ( url ) :
 i1IiiI1iIi = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , o000O0O , oOOo00O0OOOo in o00oooO0Oo :
  if o000O0O in i1IiiI1iIi :
   pass
  else :
   I1IiiiiI ( o000O0O + ' - ' + oOOo00O0OOOo + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
   i1IiiI1iIi . append ( o000O0O )
   if 31 - 31: oo0oO00 % Oooo0O0oo00oO * oo0oO00
def IiII1i1iii1Ii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O , iI in o00oooO0Oo :
  I1IiiiiI ( o000O0O + ' - Views:' + iI , url , 10075 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
  if 99 - 99: oo0oO00 - OooOO000 - O0oOO0 % oO0o
  if 21 - 21: IIiIiII11i % Ii1I . ooOoO0O00 - ii
def I11IIIiIi11 ( url ) :
 iiOOOO0o = [ ]
 I1 = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IiiiiI ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for I1111i , o000O0O , url in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 10075 , I1111i , I1111i , '' )
  iiOOOO0o . append ( o000O0O )
  if 10 - 10: OooOO000 % oOo0O0Ooo
def oo0OoOooo ( img , name , url ) :
 img = img
 name = name
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for O00O00O000OOO , url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIOo0O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIOo0O
  Ii11 = ( O00O00O000OOO ) . replace ( 'play-' , 'Server ' )
  o0OIiII ( Ii11 , iIOo0O , 10076 , img , img , '' )
  if 8 - 8: I1ii11iIi11i + IIiIiII11i * Oooo0O0oo00oO * OOooOOo * oo0oO00 / iIi1i1ii1
def iIii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for IiIIIIIi in o00oooO0Oo :
  if '=m' in IiIIIIIi :
   OO0OoOOO0 ( IiIIIIIi )
  elif 'php' in IiIIIIIi :
   iIii ( url )
  else :
   I1 = O0 ( IiIIIIIi )
   o00oooO0Oo = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for O00ooOo in o00oooO0Oo :
    OO0OoOOO0 ( IiIIIIIi )
    if 80 - 80: I11i - Oooo0O0oo00oO + ii
    if 98 - 98: Oooo0O0oo00oO + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
    if 24 - 24: I1ii11iIi11i - ooOoO0O00 + oo0oO00
def IiiIi ( url ) :
 I1 = O0 ( url )
 iIIi = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oO0OO0 , ooO00O00oOO in iIIi :
  print 'there ><><><><><><><><><><><><'
  oO0OO0 = oO0OO0
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooO00O00oOO ) )
  for o000O0O , I1IIII1ii in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + oO0OO0 + '[/COLOR] - ' + o000O0O + ' - [COLOR' + iiI1IiI + ']' + I1IIII1ii + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
 ii11i = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oO0OO0 , IiIIi1I1I11Ii in ii11i :
  print 'there ><><><><><><><><><><><><'
  oO0OO0 = oO0OO0
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiIIi1I1I11Ii ) )
  for o000O0O , I1IIII1ii in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + oO0OO0 + '[/COLOR] - ' + o000O0O + ' - [COLOR' + iiI1IiI + ']' + I1IIII1ii + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
   if 64 - 64: ii
   if 81 - 81: Ii1I - o0o00Oo0O * ii
   if 23 - 23: IIiIiII11i / O0oOO0
def OOoOOO0 ( url ) :
 I1 = O0 ( url )
 ii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for ii11i in ii11i :
  o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11i ) )
  for o000O0O in o000O0O :
   o000O0O = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11i ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I1iii11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11i ) )
  for I1iii11 in I1iii11 :
   I1iii11 = 'http:' + I1iii11
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , '' , '' )
  if 28 - 28: I1ii11iIi11i * OOoOoo - oO0o
  if 19 - 19: oo0oO00
  if 67 - 67: o0o00Oo0O % iI11I1II1I1I / iIi1i1ii1 . Ii - IIi + o0o00Oo0O
  if 27 - 27: Oooo0O0oo00oO
def Oo0oooO0oO ( url ) :
 if 89 - 89: IIiIiII11i / O0oOO0
 IIo0OoO00 = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for IiIIIIIi , I1111i , o000O0O , IIIIIiII1 in o00oooO0Oo :
  o000O0O = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O0 ( IiIIIIIi )
  o0O0OOO0Ooo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for ii1iIi1II , I11o0oO00oO0o0o0 in o0O0OOO0Ooo :
   iii11 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I11o0oO00oO0o0o0 ) )
   for ooo0O in iii11 :
    if o000O0O in IIo0OoO00 :
     pass
    else :
     o0OIiII ( o000O0O , ii1iIi1II , 8043 , I1111i , I1111i , ooo0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
     IIo0OoO00 . append ( o000O0O )
     if 35 - 35: OooOO000 . OOooOOo * Ii
     if 44 - 44: Ii / I1ii11iIi11i
def Ii1IIi ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , oo0 , ooo0O , II11IiIi11 , o000O0O in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 10065 , oo0 , II11IiIi11 , ooo0O )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 43 - 43: OooOO000 % iiII11i1I1IIi
def o0O0ooOOoO ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'https://www.youtube.com/results?search_query=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iii = II11 . lower ( )
 I1 = O0 ( I1iii )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for ooO0oOOooOo0 in next :
  ooO0oOOooOo0 = 'https://www.youtube.com' + ooO0oOOooOo0
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , ooO0oOOooOo0 , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for I1111i , ooO0oOOooOo0 , o000O0O , iIi11ii , I11o0oO00oO0o0o0 in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( o000O0O )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  I1iii11 = 'http:' + ( I1111i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1iii11
  ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
  o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , I1iii11 , I11o0oO00oO0o0o0 )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for I1111i , ooO0oOOooOo0 , o000O0O , iIi11ii in o00oooO0Oo :
   print 'im doing it'
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   I1iii11 = 'http:' + ( I1111i ) . replace ( 'https:' , '' )
   ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
   if '&' in ooO0oOOooOo0 :
    print ' i got here'
    I1 = O0 ( ooO0oOOooOo0 )
    ii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for ii11i in ii11i :
     o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11i ) )
     for o000O0O in o000O0O :
      o000O0O = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     ooO0oOOooOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11i ) )
     for ooO0oOOooOo0 in ooO0oOOooOo0 :
      ooO0oOOooOo0 = 'https://www.youtube.com/w' + ooO0oOOooOo0
     I1iii11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11i ) )
     for I1iii11 in I1iii11 :
      I1iii11 = 'http:' + I1iii11
     o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , OO0o , '' )
   elif o000O0O in IIiiiiiiIi1I1 :
    pass
   elif 'user' in ooO0oOOooOo0 or 'elete' in o000O0O :
    pass
   elif 'hannel' in ooO0oOOooOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooO0oOOooOo0
    I1 = O0 ( ooO0oOOooOo0 )
    i11I1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for I1111i , ooO0oOOooOo0 , o000O0O in i11I1 :
     if 'outube' in ooO0oOOooOo0 or 'list' in ooO0oOOooOo0 :
      pass
     elif 'atch' in ooO0oOOooOo0 :
      ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1111i , 'http:' + I1111i , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , I1iii11 , '' )
    if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + iiII11i1I1IIi * iI11I1II1I1I % IIi
def I1iI1I1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for I1111i , url , o000O0O , iIi11ii , I11o0oO00oO0o0o0 in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( o000O0O )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  I1iii11 = 'http:' + ( I1111i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1iii11
  url = 'http://www.youtube.com' + url
  o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , I1iii11 , I11o0oO00oO0o0o0 )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for I1111i , url , o000O0O , iIi11ii in o00oooO0Oo :
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   I1iii11 = 'http:' + ( I1111i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O0 ( url )
    ii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for ii11i in ii11i :
     o000O0O = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11i ) )
     for o000O0O in o000O0O :
      o000O0O = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11i ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I1iii11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11i ) )
     for I1iii11 in I1iii11 :
      I1iii11 = 'http:' + I1iii11
     o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , OO0o , '' )
   elif o000O0O in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in o000O0O :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O0 ( url )
    i11I1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for I1111i , url , o000O0O in i11I1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I1111i , 'http:' + I1111i , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + iIi11ii + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 , I1iii11 , '' )
    if 48 - 48: oOo0O0Ooo / Ii - I11i * O0oOO0 / ii
    if 89 - 89: iI11I1II1I1I / oOo0O0Ooo - IIiIiII11i / IIi . Ii . IIi
def OO0O00oOo ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  IiiiI1 = open ( O000oo0O )
  o00oooO0Oo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( IiiiI1 ) )
  for OOOo0 , OOo0Oo0OOo0 in o00oooO0Oo :
   if OOOo0 == 'needs replacing' or OOo0Oo0OOo0 == 'needs replacing' :
    i1i11I ( )
    if 7 - 7: IIiIiII11i
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if 27 - 27: O0oOO0 . ii + Ii
def O0OO ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 i1i11I ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
def I1i ( ) :
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
 if 49 - 49: Ii1I
def O0oOOo0o ( name ) :
 I1III11iiii11i1 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , I1111i , ooOo0OoO , ooO0oOOooOo0 in o00oooO0Oo :
  if I1III11iiii11i1 == 'Full List' :
   ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
   o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , I1111i , I1111i , '' )
  else :
   I1III11iiii11i1 = ( I1III11iiii11i1 ) . replace ( 'World' , 'القنوات العربية' )
   if I1III11iiii11i1 in ooOo0OoO :
    ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
    print ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , I1111i , I1111i , '' )
   else :
    pass
    if 36 - 36: iIi1i1ii1 - ii / oO0o
def iIIi1iI1I1IIi ( name ) :
 I1III11iiii11i1 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , I1111i , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
  o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , I1111i , I1111i , '' )
 else :
  o0OIiII ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 77 - 77: OOoOoo / I1ii11iIi11i + OOoOoo % I11i - oOo0O0Ooo * oOo0O0Ooo
  if 23 - 23: iiII11i1I1IIi . IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
  if 37 - 37: iiII11i1I1IIi / I1ii11iIi11i . oo0oO00 * oo0oO00
  if 80 - 80: Oooo0O0oo00oO % Ii1I
  if 91 - 91: oo0oO00 / o0o00Oo0O - IIi . oOo0O0Ooo
  if 82 - 82: iIi1i1ii1 * Oooo0O0oo00oO / O0oOO0
  if 2 - 2: oOo0O0Ooo + I11i . I11i . o0o00Oo0O / oo0oO00
  if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
  if 14 - 14: Ii1I
  if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
  if 56 - 56: ii - oo0oO00 - ooOoO0O00
  if 8 - 8: OooOO000 / Oooo0O0oo00oO . oOo0O0Ooo + Ii1I / Ii
def I1iiii1I ( ) :
 I1IiiiiI ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IiiiiI ( 'Backup Genie Favourites' , ooO0oOOooOo0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( o00OO00OoO ) :
  I1IiiiiI ( 'Backup Ivue Config' , o00OO00OoO , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  I1IiiiiI ( 'Backup Kodi Favourites' , OOOO0OOoO0O0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 31 - 31: OOoOoo - iI11I1II1I1I + iiII11i1I1IIi . I1ii11iIi11i / iIi1i1ii1 % iI11I1II1I1I
  if 6 - 6: iIi1i1ii1 * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
  if 53 - 53: oo0oO00 + iI11I1II1I1I
zip = oo00 . getSetting ( 'zip' )
oOooo0Oo = xbmc . translatePath ( os . path . join ( zip ) )
def oo0O0o ( ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 87 - 87: I1ii11iIi11i / o0o00Oo0O * iIi1i1ii1 / I11i
  if 19 - 19: OooOO000 + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
  if 16 - 16: O0oOO0 + OOoOoo / I11i
def O00oOoo0OoO0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O0Oo000ooO00
  elif 'Ivue' in name :
   url = o00OO00OoO
  elif 'Kodi' in name :
   url = OOOO0OOoO0O0
  oo0O0o ( )
  Ooo0 = open ( url ) . read ( )
  oooO00o0 = os . path . join ( oOooo0Oo , description . split ( 'Your ' ) [ 1 ] )
  oOOo0O00o = open ( oooO00o0 , mode = 'w' )
  oOOo0O00o . write ( Ooo0 )
  oOOo0O00o . close ( )
 else :
  if 'guisettings.xml' in description :
   o0o00oO0oo000 = open ( os . path . join ( oOooo0Oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oO000o = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   o00oooO0Oo = re . compile ( oO000o ) . findall ( o0o00oO0oo000 )
   for type , o0Oo , o0O0 in o00oooO0Oo :
    o0O0 = o0O0 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o0Oo , o0O0 ) )
  else :
   oooO00o0 = os . path . join ( url )
   Ooo0 = open ( os . path . join ( oOooo0Oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0O00o = open ( oooO00o0 , mode = 'w' )
   oOOo0O00o . write ( Ooo0 )
   oOOo0O00o . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 48 - 48: oo0oO00 - iIi1i1ii1 + iI11I1II1I1I + ii
 if 4 - 4: IIiIiII11i . oo0oO00 + IIi * OooOO000 . OOoOoo
 if 87 - 87: OOooOOo / oO0o / Ii
 if 74 - 74: O0oOO0 / Ii1I % I11i
def OO0o0OO0 ( ) :
 OooOo0OOO = 1
 oo0O0o ( )
 I1Io00oOOoO0oO = xbmc . translatePath ( os . path . join ( oOooo0Oo , 'Build Backup' , 'Full Backup' , '' ) )
 I11iiIIII1I1 = xbmc . translatePath ( os . path . join ( oOooo0Oo , 'Build Backup' , 'my_full_backup.zip' ) )
 i1IIi1i1Ii1 = xbmc . translatePath ( os . path . join ( oOooo0Oo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1Io00oOOoO0oO ) :
  os . makedirs ( I1Io00oOOoO0oO )
 Iii = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Iii ) : return False , 0
 o0Oo0oO = Iii
 iIII1iiIi11 = xbmc . translatePath ( os . path . join ( I1Io00oOOoO0oO , o0Oo0oO + '.zip' ) )
 ooOo0O0O0oOO0 = [ 'plugin.video.GenieTv' ]
 iIiIIi = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 III1I = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1I111iIi = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OoOOOO = "Creating full backup of existing build"
 I1iiIi111I = "Creating Community Build"
 Iiii1iIii = "Archiving..."
 oOoooO000O = ""
 III1I11i1iIi = "Please Wait"
 OO0oo0O0OOO0 ( I11 , iIII1iiIi11 , I1iiIi111I , Iiii1iIii , oOoooO000O , III1I11i1iIi , III1I , I1I111iIi )
 time . sleep ( 1 )
 OoOOo = xbmc . translatePath ( os . path . join ( I1Io00oOOoO0oO , o0Oo0oO + '_guisettings.zip' ) )
 Iii1 = zipfile . ZipFile ( OoOOo , mode = 'w' )
 try :
  Iii1 . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 Iii1 . close ( )
 if OooOo0OOO == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I11iiIIII1I1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iIII1iiIi11 + '[/COLOR]' )
  if 78 - 78: Ii + I11i + OooOO000 / I11i % iI11I1II1I1I % iIi1i1ii1
def OO0oo0O0OOO0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Oo0O0Oo00O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIoo0ooooO = len ( sourcefile )
 iiIIi = [ ]
 i1i = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for iIIiI1iiI , I11Ii111I , Oo00OO0 in os . walk ( sourcefile ) :
  for file in Oo00OO0 :
   i1i . append ( file )
 oo0O = len ( i1i )
 for iIIiI1iiI , I11Ii111I , Oo00OO0 in os . walk ( sourcefile ) :
  I11Ii111I [ : ] = [ oO00OoOOOo for oO00OoOOOo in I11Ii111I if oO00OoOOOo not in exclude_dirs ]
  Oo00OO0 [ : ] = [ oOOo0O00o for oOOo0O00o in Oo00OO0 if oOOo0O00o not in exclude_files ]
  for file in Oo00OO0 :
   iiIIi . append ( file )
   Oo0 = len ( iiIIi ) / float ( oo0O ) * 100
   o0oOoO00o . update ( int ( Oo0 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0OOOOO0O = os . path . join ( iIIiI1iiI , file )
   if not 'temp' in I11Ii111I :
    if not 'plugin.program.originwizard' in I11Ii111I :
     import time
     I1I1IiIi1 = '01/01/1980'
     oOO0o0oo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0OOOOO0O ) ) )
     if oOO0o0oo0 > I1I1IiIi1 :
      Oo0O0Oo00O . write ( o0OOOOO0O , o0OOOOO0O [ iIoo0ooooO : ] )
 Oo0O0Oo00O . close ( )
 o0oOoO00o . close ( )
 if 78 - 78: Oooo0O0oo00oO + iiII11i1I1IIi . iIi1i1ii1
 if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
def oO0OoO00o ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 if 69 - 69: OooOO000 - oOo0O0Ooo
 if 95 - 95: oOo0O0Ooo * Ii . OOoOoo
def iIIi1 ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  iI1 ( )
 if O0oO0 == 1 :
  Oo00o0OO0O00o ( )
 if O0oO0 == 2 :
  O0OO0oOOo ( )
 if O0oO0 == 3 :
  o0O0ooOOoO ( )
  if 83 - 83: iIi1i1ii1 * oo0oO00 / I1ii11iIi11i
  if 32 - 32: I11i + OOooOOo - ii
  if 39 - 39: ii * Oooo0O0oo00oO * o0o00Oo0O . oo0oO00 . oO0o + OOoOoo
  if 9 - 9: OOooOOo + O0oOO0 % ii + I11i
  if 56 - 56: ii + Ii1I - iiII11i1I1IIi
  if 24 - 24: I11i + OOoOoo + oo0oO00 - iI11I1II1I1I
  if 49 - 49: oo0oO00 . OOoOoo * OOooOOo % iIi1i1ii1 . o0o00Oo0O
  if 48 - 48: o0o00Oo0O * IIi - o0o00Oo0O / IIi + OOooOOo
  if 52 - 52: oO0o % IIi * IIiIiII11i
def I1IiIii11I ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   iIIiiiI ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , oo0 , o000O0O )
  if O0oO0 == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if O0oO0 == 2 :
   i1iii1ii ( )
  if O0oO0 == 3 :
   II1I11Iii1 ( )
  if O0oO0 == 4 :
   i1iIIi1II1iiI ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO0 == 5 :
   III1Ii1i1I1 ( )
  if O0oO0 == 6 :
   O0O00OooO ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO0 == 7 :
   I1IiI1iI11 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO0 == 8 :
   iIi ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO0 == 9 :
   iiO0O0o0oO0O00 ( )
  if O0oO0 == 10 :
   o0O0oO0 ( )
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
  if 77 - 77: o0o00Oo0O . IIi
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 39 - 39: OOoOoo . IIiIiII11i
def iIiIi1iI11iiI ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   iiI1Ii11II1I ( )
  if O0oO0 == 1 :
   iiIiIIIiiI ( )
  if O0oO0 == 2 :
   oOO0O00Oo0O0o ( )
  if O0oO0 == 3 :
   O0ooO0Oo00o ( ooO0oOOooOo0 )
  if O0oO0 == 4 :
   I1Ii11II1I1 ( ooO0oOOooOo0 )
  if O0oO0 == 5 :
   o00O0 ( )
  if O0oO0 == 6 :
   IiI1iI1IiiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO0 == 7 :
   OoO0oo ( )
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
  if 72 - 72: o0o00Oo0O + oOo0O0Ooo - iiII11i1I1IIi - oO0o
  if 100 - 100: o0o00Oo0O
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 79 - 79: iI11I1II1I1I
 if 81 - 81: Oooo0O0oo00oO + iI11I1II1I1I * OooOO000 - iI11I1II1I1I . Oooo0O0oo00oO
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
 if 48 - 48: oo0oO00 . ii . oOo0O0Ooo . OOooOOo % Ii1I / iiII11i1I1IIi
 if 11 - 11: ooOoO0O00 % oO0o % iiII11i1I1IIi
def O0Oo0 ( ) :
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
 if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . Oooo0O0oo00oO + oO0o - OooOO000
def OOo0 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , OO0o , '' )
 if 5 - 5: iiII11i1I1IIi
def OOiI1 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , OO0o , '' )
 o0OIiII ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , OO0o , '' )
 if 42 - 42: Oooo0O0oo00oO % O0oOO0 / oO0o - O0oOO0 * Ii
 if 19 - 19: O0oOO0 * oOo0O0Ooo % Ii
 if 24 - 24: I11i
def OoOoO ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  iIi1Iii111I ( )
 if O0oO0 == 0 :
  IIi11i11 ( ooO0oOOooOo0 )
 if O0oO0 == 0 :
  Ii11Iii ( ooO0oOOooOo0 )
  if 68 - 68: oOo0O0Ooo % o0o00Oo0O
  if 74 - 74: ooOoO0O00 + OOooOOo + iI11I1II1I1I * OOooOOo * iI11I1II1I1I + oo0oO00
  if 64 - 64: iI11I1II1I1I / o0o00Oo0O % iIi1i1ii1 . ii + iIi1i1ii1 + O0oOO0
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 79 - 79: ii - iIi1i1ii1 * iIi1i1ii1 . OOooOOo
def Oo00ooO0OoOo ( ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o00oooO0Oo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O0o0O00Oo0o0 )
 for I1111i , o000O0O in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , I1111i , I1111i , '' )
 Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
 if 99 - 99: OOooOOo
def oO00OoOo ( url ) :
 O0o0O00Oo0o0 = O0 ( OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 5 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 10 - 10: oo0oO00 / oo0oO00 * Ii
def iIi1Iii111I ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 46 - 46: oO0o * I1ii11iIi11i % O0oOO0 + o0o00Oo0O * iIi1i1ii1
def ii1I11i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + O0OOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 37 - 37: o0o00Oo0O - oo0oO00
def IiI1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + O0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - Oooo0O0oo00oO % I11i
def I111i1Ii1i1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iI1IIi1IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * O0oOO0 * oO0o
def II11I ( url ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 31 - 31: IIi
def IIi11i11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i11iIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 40 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 93 - 93: OOoOoo / Oooo0O0oo00oO * ii - Ii / oOo0O0Ooo
def iIiiiii1IIiI ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i1i1Ii11Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 5 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 57 - 57: Oooo0O0oo00oO + OooOO000 % Ii1I . oO0o / oO0o * o0o00Oo0O
def oO0O0OO0O ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ii1iiII1i ( )
 if O0oO0 == 1 :
  oO00O ( )
 if O0oO0 == 2 :
  IIiI11 ( )
  if 9 - 9: OOoOoo + IIiIiII11i % OOoOoo % iIi1i1ii1 + iI11I1II1I1I
  if 59 - 59: ooOoO0O00
  if 48 - 48: o0o00Oo0O * IIi * oO0o . oO0o * oo0oO00 - IIi
  if 14 - 14: Ii1I + Ii
def oO00O ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , OOOoo in o00oooO0Oo :
  IiIi1iIIi1 ( 'Android Apps' + OOOoo , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for ooO0oOOooOo0 , OOOoo in o0O0OOO0Ooo :
  IiIi1iIIi1 ( 'Android Games' + OOOoo , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def III1II1iii1i ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if '/cat' in url :
   IiIi1iIIi1 ( ( o000O0O ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def O0OO0oOO ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if '/app' in url :
   IiIi1iIIi1 ( ( o000O0O ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def ooooO ( url ) :
 O00o0 = O0 ( url )
 oO0O0 = url
 if "page=" in str ( url ) :
  oO0O0 = url . split ( '?' ) [ 0 ]
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  if 'apk' in url :
   o0OIiII ( ( o000O0O ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + I1111i )
 if len ( o0O0OOO0Ooo ) > 1 :
  o0O0OOO0Ooo = str ( o0O0OOO0Ooo [ len ( o0O0OOO0Ooo ) - 1 ] )
 o0OIiII ( 'Next Page' , oO0O0 + str ( o0O0OOO0Ooo ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def iI111i11iI1 ( name , url ) :
 O00o0 = iIi11i1 ( url )
 name = name
 o00oooO0Oo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  url = 'https://www.apkfiles.com' + url
  III1ii ( name , url , 'Brackets' )
def IIiI11 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'https://www.apkfiles.com/search?q=' + ( I1i11II ) . replace ( ' ' , '+' ) + '&search_type=1'
 I1iii = II11 . lower ( )
 ooooO ( I1iii )
 if 23 - 23: O0oOO0 * iiII11i1I1IIi
def O0oOo00O ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( i1I1I1i1i1i , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , o000O0O + '.apk' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 23 - 23: iI11I1II1I1I
def Ii11ii1Iiii ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , o000O0O + '.mp4' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 7 - 7: IIi % ooOoO0O00 * ii * o0o00Oo0O + iiII11i1I1IIi
 if 95 - 95: ii + oo0oO00 - Ii1I / Ii1I . ooOoO0O00 . ii
def I1iiI1II ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , name )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 IIIi = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIIi
 print '======================================='
 extract . all ( Ii1I1Ii , IIIi , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 23 - 23: OOoOoo
 if 13 - 13: iI11I1II1I1I
 if 77 - 77: Ii - iI11I1II1I1I / O0oOO0 / OOoOoo / oO0o
 if 56 - 56: ii * o0o00Oo0O
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
def Ii1iiII1i ( ) :
 O0o0O00Oo0o0 = O0 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , ooO0oOOooOo0 , iiI1IIIi , II11IiIi11 , IiIo0o0OO0o00o0O in o00oooO0Oo :
  o0OIiII ( o000O0O , ooO0oOOooOo0 , 80003 , iiI1IIIi , oOOOo00O00oOo + 'APKToolsB.png' , IiIo0o0OO0o00o0O )
def IIIIIIi1i ( apk , ret = None ) :
 if apk == "kodi" :
  iiiii11I1 = "https://kodi.tv/download/"
  O0o0O00Oo0o0 = O0 ( iiiii11I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O0o0O00Oo0o0 )
  if len ( o00oooO0Oo ) == 1 :
   Ii1 = o00oooO0Oo [ 0 ] [ 0 ]
   o0Oo0oO = o00oooO0Oo [ 0 ] [ 1 ]
   OOOo = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( Ii1 , o0Oo0oO )
  if ret == 'version' : return Ii1
  else : return OOOo
 elif apk == "spmc" :
  I1iI1IiI = 'https://github.com/koying/SPMC/releases/latest/'
  O0o0O00Oo0o0 = O0 ( I1iI1IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O0o0O00Oo0o0 )
  Ii1 = re . sub ( '<[^<]+?>' , '' , o00oooO0Oo [ 0 ] ) . replace ( ' ' , '' )
  OOOo = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( Ii1 , Ii1 )
  if ret == 'version' : return Ii1
  else : return OOOo
def III1ii ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  i1i1Ii1I = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not i1i1Ii1I : I1II1III1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  oooo0O0o0OoOO = name
  if i1i1Ii1I :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not o0oooOO00 ( url ) == True : I1II1III1 ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % oooo0O0o0OoOO , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    Iii1 = zipfile . ZipFile ( Ii1I1Ii )
    for file in Iii1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as oOOo0O00o :
       III1 = file . split ( '/' ) [ 1 ]
       oOOo0O00o . write ( Iii1 . read ( file ) )
       xbmc . sleep ( 500 )
       oOOo0O00o . close ( )
       try :
        os . remove ( Ii1I1Ii )
       except :
        pass
       Ii1I1Ii = os . path . join ( oooOOOOO , III1 )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : I1II1III1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : I1II1III1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 7 - 7: Ii + oOo0O0Ooo
 if 47 - 47: OooOO000 - Oooo0O0oo00oO / OOoOoo - I1ii11iIi11i + iiII11i1I1IIi - iI11I1II1I1I
 if 68 - 68: IIi - O0oOO0 + I1ii11iIi11i
 if 44 - 44: IIi * I11i * IIiIiII11i
def Ii1i1i ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O0o0O00Oo0o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  ooO0oOOooOo0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + ooO0oOOooOo0 )
  iIi1Ii1IIiI ( ( o000O0O ) . replace ( '_' , ' ' ) , ooO0oOOooOo0 )
  if 63 - 63: ii % oo0oO00 . iIi1i1ii1
def iIi1Ii1IIiI ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  i1i1Ii1I = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not i1i1Ii1I : I1II1III1 ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  oooo0O0o0OoOO = name
  if i1i1Ii1I :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not o0oooOO00 ( url ) == True : I1II1III1 ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % oooo0O0o0OoOO , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : I1II1III1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : I1II1III1 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 58 - 58: oo0oO00 * OOooOOo
 if 94 - 94: IIi - Ii1I + I11i - I1ii11iIi11i
def iiIi1iiI1I ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 5 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
 if 44 - 44: ii . IIiIiII11i . Oooo0O0oo00oO % ii
def o0oO0oooOoo ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 30015 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 86 - 86: Ii + o0o00Oo0O * iIi1i1ii1 - oO0o * Oooo0O0oo00oO + o0o00Oo0O
def Oo0O00o0oo0oOO ( url , iconimage , fanart ) :
 O0o0O00Oo0o0 = O0 ( url )
 iIOo0O = url
 I1111i = iconimage
 fanart = fanart
 o00oooO0Oo = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for IiIIIIIi , o000O0O in o00oooO0Oo :
  if '.mp4' in o000O0O :
   o0OIiII ( 'Watch VIDEO' , url + '/' + IiIIIIIi , 222 , I1111i , fanart , '' )
  if 'description' in o000O0O :
   o0OIiII ( 'Read Description' , url + '/' + IiIIIIIi , 30017 , I1111i , fanart , '' )
  if 'images' in o000O0O :
   I1IiiiiI ( 'View Images' , url + '/' + IiIIIIIi , 30018 , I1111i , fanart , '' )
  if 'url' in o000O0O :
   o0OIiII ( 'Install Build On Android' , url + '/' + IiIIIIIi , 30016 , I1111i , fanart , '' )
  if 'url' in o000O0O :
   o0OIiII ( 'Install Build On Pc' , url + '/' + IiIIIIIi , 30019 , I1111i , fanart , '' )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 75 - 75: iI11I1II1I1I + ii
def oOOO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  i111I11i1I ( url )
  if 85 - 85: Oooo0O0oo00oO * ooOoO0O00 % oOo0O0Ooo - OOoOoo
def I11I1ii1i ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  II11Ii111II1 ( url )
  if 72 - 72: iiII11i1I1IIi % I11i % O0oOO0 + oo0oO00 % Ii + o0o00Oo0O
def OoOOoooO000 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'desc="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for OoO0o000oOo in o00oooO0Oo :
  OOOiiiiI ( 'Description:' , OoO0o000oOo )
  if 88 - 88: ooOoO0O00 * OooOO000 * O0oOO0 - OOoOoo * oo0oO00 / ii
def iiI1i ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 url = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for IiIIIIIi , o000O0O in o00oooO0Oo :
  if 'png' in o000O0O :
   o0OIiII ( 'image' , '' , '' , url + '/' + IiIIIIIi , url + '/' + IiIIIIIi , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 72 - 72: OOooOOo * iI11I1II1I1I % oo0oO00
def IiIi1I1i1II ( name , url , description ) :
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
 if 15 - 15: O0oOO0 / OooOO000
 if 37 - 37: Ii + oOo0O0Ooo . Oooo0O0oo00oO % oo0oO00 % oo0oO00
def II11Ii111II1 ( url ) :
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
 iiI1Ii11II1I ( )
 if 26 - 26: o0o00Oo0O
def i111I11i1I ( url ) :
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
 iiI1Ii11II1I ( )
 if 34 - 34: OOoOoo * OooOO000
def OooOoOO0OO ( name , url , description ) :
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
 iiI1Ii11II1I ( )
 if 27 - 27: iIi1i1ii1 * oOo0O0Ooo . iI11I1II1I1I - iI11I1II1I1I
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
  i111i1I1ii1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOo0O00o . write ( i111i1I1ii1i . rstrip ( '\r\n' ) + '\n' )
def iiI1Ii11II1I ( ) :
 O0oO0 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO0 == 0 : return
 elif O0oO0 == 1 : pass
 O0OoooI11iI1I = ii1iII1II ( )
 ii1 ( "Platform: " + str ( O0OoooI11iI1I ) )
 os . _exit ( 1 )
 ii1 ( "Force close failed!  Trying alternate methods." )
 if O0OoooI11iI1I == 'osx' :
  ii1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif O0OoooI11iI1I == 'linux' :
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
 elif O0OoooI11iI1I == 'android' :
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
 elif O0OoooI11iI1I == 'windows' :
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
  if 50 - 50: iI11I1II1I1I * iIi1i1ii1 . ii / IIiIiII11i - Ii1I * Ii1I
  if 98 - 98: oO0o - IIi . iIi1i1ii1 % Ii
  if 69 - 69: Ii1I + iiII11i1I1IIi * o0o00Oo0O . Oooo0O0oo00oO % OOooOOo
def Ii11Iii ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( url ) :
  for file in Oo00OO0 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    o0o00oO0oo000 = open ( ( os . path . join ( O0O000O , file ) ) ) . read ( )
    iiii1IIi1 = o0o00oO0oo000 . replace ( I11 , 'special://home/' )
    oOOo0O00o = open ( ( os . path . join ( O0O000O , file ) ) , mode = 'w' )
    oOOo0O00o . write ( str ( iiii1IIi1 ) )
    oOOo0O00o . close ( )
 iiI1Ii11II1I ( )
 if 87 - 87: iIi1i1ii1
def i1iii1ii ( ) :
 IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 17 - 17: IIi / iI11I1II1I1I - oO0o + oOo0O0Ooo % Oooo0O0oo00oO
def III1III11II ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def iIi1iI ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def OO0Oo ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o0O0OOO0Ooo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , I1111i , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']Stream - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , I1111i )
def IIiiiiiIiIIi ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def iiIiiIi1 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II
 I1Ii11i = 'https://www.radionomy.com/en/search/index?query=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1 = O0 ( I1Ii11i )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']Stream - ' + o000O0O + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + ooO0oOOooOo0 , 70005 , I1111i )
  if 19 - 19: iIi1i1ii1 - I11i . iI11I1II1I1I . OOooOOo / Oooo0O0oo00oO
  if 87 - 87: OOooOOo - OOoOoo - Oooo0O0oo00oO + I1ii11iIi11i % iI11I1II1I1I / Ii
def III1Ii1i1I1 ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , 'http://www.listenlive.eu/' + ooO0oOOooOo0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def i1iIIi1II1iiI ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 12 - 12: OOoOoo
def oOOO0ooOO ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.toonjet.com/' + ooO0oOOooOo0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i11IiI1iiI11 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( O00o0 )
 for url , I1111i in o00oooO0Oo :
  if 'ol.gif' in I1111i :
   pass
  elif 'link_block_' in I1111i :
   pass
  elif '.png' in I1111i :
   pass
  else :
   IiIi1iIIi1 ( ( I1111i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in o0O0OOO0Ooo :
  IiIi1iIIi1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoOOOO00 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + OooOO000
  if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * O0oOO0
def o0O0oO0 ( ) :
 Oo0O0000Oo00o ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 Oo0O0000Oo00o ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
def o00iIiiiII ( ) :
 Oo0O0000Oo00o ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 Oo0O0000Oo00o ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 Oo0O0000Oo00o ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 5 - 5: ii / I11i % oo0oO00 % oO0o * iiII11i1I1IIi + iI11I1II1I1I
def I11iiI11iiI ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for o000O0O , ooO0oOOooOo0 , OOOII1i1II in o00oooO0Oo :
  if 'Parent' in o000O0O :
   pass
  elif '2' in OOOII1i1II :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: I1ii11iIi11i % ii - IIi
def iIII11Iiii1 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for o000O0O , ooO0oOOooOo0 , OOOII1i1II in o00oooO0Oo :
  if I1i11II in o000O0O . lower ( ) :
   if '1' in OOOII1i1II :
    Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOOII1i1II :
    Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOOII1i1II :
    Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 95 - 95: oOo0O0Ooo
    if 99 - 99: o0o00Oo0O
def O0oO0OOoO ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for o000O0O , ooO0oOOooOo0 , OOOII1i1II in o00oooO0Oo :
  if '1' in OOOII1i1II :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOOII1i1II :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOOII1i1II :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 69 - 69: oo0oO00 / Ii * I11i / OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: I11i / Oooo0O0oo00oO % Oooo0O0oo00oO
def OoooO0 ( url ) :
 IiIIIIIi = url
 I1 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , o000O0O in o0O0OOO0Ooo :
  if 'mp3' in o000O0O :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in o000O0O :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in o000O0O :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in o000O0O :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 75 - 75: OOoOoo
   if 29 - 29: Ii1I
   if 53 - 53: Ii . Ii1I % IIi / OOoOoo % iI11I1II1I1I
def iIiIii1I1 ( url ) :
 I1 = O0 ( url )
 IiIIIIIi = url
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
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
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in o000O0O :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 81 - 81: iIi1i1ii1 - I11i - I1ii11iIi11i - IIi / Oooo0O0oo00oO % oo0oO00
   if 52 - 52: Ii1I / iiII11i1I1IIi
def i1ii1IIIII ( ) :
 Oo0O0000Oo00o ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 Oo0O0000Oo00o ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 Oo0O0000Oo00o ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 52 - 52: OOooOOo / oO0o + OooOO000
def Iii1i11iiI1 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i in o00oooO0Oo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I1111i :
   pass
  else :
   Oo0O0000Oo00o ( I1111i , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooO0oOOooOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I1111i + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 95 - 95: O0oOO0 * iI11I1II1I1I + Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: I1ii11iIi11i
 if 100 - 100: IIi + iI11I1II1I1I
def o0o0OoO0OOO0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  if '</a>' in o000O0O :
   pass
  elif '(' in o000O0O :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 79 - 79: O0oOO0 % I11i % OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: oOo0O0Ooo * Oooo0O0oo00oO % oO0o
def i111I11I ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if I1i11II in o000O0O . lower ( ) :
   if '</a>' in o000O0O :
    pass
   elif '(' in o000O0O :
    Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
    if 48 - 48: OooOO000 . Ii / ooOoO0O00 % iIi1i1ii1 % iiII11i1I1IIi + O0oOO0
def iiII1iiiiiii ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if '</a>' in o000O0O :
   pass
  elif '(' in o000O0O :
   Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: ii + O0oOO0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: o0o00Oo0O
 if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
def o0OO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in o00oooO0Oo :
  IiIIIIIi = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IiIIIIIi )
  if 76 - 76: o0o00Oo0O . oO0o + OOooOOo
def ii11iI1iIiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for o000O0O , url in o00oooO0Oo :
  if '<p align' in o000O0O :
   pass
  elif '&nbsp;' in o000O0O :
   pass
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 97 - 97: IIi * oO0o - OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: OOooOOo
 if 83 - 83: Ii * OooOO000
def OO0oO0o ( ) :
 I1 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'ongoing' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Disney.png' , '' , '' )
  if 'genre' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Genre.png' , '' , '' )
  if 'years' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Years.png' , '' , '' )
def IIIIIIi1IiIi ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 III1i = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , I1111i , I1111i , o000O0O )
 for url , o000O0O in III1i :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def o0Oo0 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 oO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 ii1IiI11I = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 OO0Ooo000O0 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in ii1IiI11I :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , o000O0O in oO0O :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def o00o ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * O0oOO0 . oo0oO00 / ooOoO0O00
def O0000 ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 o00oooO0Oo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if '9cart' in ooO0oOOooOo0 :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 50 - 50: OooOO000 / ooOoO0O00 % ii
def oOOOOO0Ooooo ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 ii1iii1i = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in o0O0OOO0Ooo :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , o000O0O in ii1iii1i :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 57 - 57: IIi - ii
def OOoOO0O0o0 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 20003 , I1111i )
 for url , o000O0O in o0O0OOO0Ooo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 44 - 44: Oooo0O0oo00oO / I1ii11iIi11i + iIi1i1ii1 % IIiIiII11i / oO0o + Ii
def ii11Iiii ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'Watch' in url :
   IiIi1iIIi1 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
def iiI111 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 62 - 62: Ii1I - o0o00Oo0O . oOo0O0Ooo . o0o00Oo0O * iI11I1II1I1I
def oOo0O ( url ) :
 url = cloudflare . source ( url )
 OO0OoOOO0 ( url )
 if 30 - 30: IIi . Ii1I / Oooo0O0oo00oO
def i1II11IiiiI ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . recompile ( 'src="([^"]*)"' )
 for url in o00oooO0Oo :
  OO0OoOOO0 ( url )
  if 7 - 7: Ii1I / IIiIiII11i - oo0oO00 + ooOoO0O00 + IIi
  if 7 - 7: OOoOoo + IIi
def III111i11IiI ( ) :
 if 32 - 32: iI11I1II1I1I % oOo0O0Ooo / Ii + Oooo0O0oo00oO - I11i . iiII11i1I1IIi
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 if 86 - 86: ooOoO0O00 / IIi * oOo0O0Ooo
def O0OO0oOOo ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 67 - 67: Ii1I * Ii1I / O0oOO0 * ii + OOooOOo
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 79 - 79: ooOoO0O00
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if I1i11II in o000O0O . lower ( ) :
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
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
    if 1 - 1: O0oOO0 / ooOoO0O00
    if 74 - 74: oo0oO00 / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: Ii . ii / oo0oO00 * Ii1I + ii
def ooO00O0O0 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
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
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * iiII11i1I1IIi / Oooo0O0oo00oO
def O00oo00oOOO0o ( url ) :
 O00o0 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O00o0 )
 for I1111i in o0O0OOO0Ooo :
  II1i = I1111i
 ii1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O00o0 )
 for url in ii1iii1i :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 10007 , II1i )
  if 6 - 6: iIi1i1ii1 * iIi1i1ii1 * o0o00Oo0O / Oooo0O0oo00oO + o0o00Oo0O
  if 51 - 51: I11i - OOooOOo + I1ii11iIi11i / oo0oO00 % OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: Ii1I * ooOoO0O00 . ooOoO0O00
def o0O0O ( url , IMAGE ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  print o000O0O + '     ' + url
  if 'easy' in url :
   oOOoOOO0oOoo ( url )
   if 65 - 65: iiII11i1I1IIi . O0oOO0 - IIi
   if 93 - 93: o0o00Oo0O
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 4 - 4: oOo0O0Ooo / oOo0O0Ooo
def oOOoOOO0oOoo ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
  if 82 - 82: oo0oO00 / OOoOoo * oo0oO00 % Ii * IIiIiII11i
  if 83 - 83: oO0o + Oooo0O0oo00oO - I11i + iI11I1II1I1I % I1ii11iIi11i
  if 23 - 23: I11i + IIi % OOooOOo % oOo0O0Ooo % ii
def O0OOo ( ) :
 if 78 - 78: oO0o / I1ii11iIi11i - iI11I1II1I1I - Ii * iiII11i1I1IIi
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , OO0o , '' )
 if 84 - 84: Oooo0O0oo00oO + IIi + I11i
def i1i1iIII11i ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  if 'elete' in o000O0O :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 222 , I1111i )
   if 40 - 40: iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
def oOoo0ooOoo ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOooOOo00ooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for I1111i , o0OO0oooo , i1iII1IiiIiI1 in oOooOOo00ooO :
  for I1i11II in o0OO0oooo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I11II1i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for ooO0oOOooOo0 , o000O0O in I11II1i1 :
    if 'tube' in ooO0oOOooOo0 :
     pass
    elif 'stage' in ooO0oOOooOo0 :
     O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o0OO0oooo + '   -   ' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1111i , )
    elif 'vee' in ooO0oOOooOo0 :
     pass
     if 46 - 46: IIiIiII11i % iiII11i1I1IIi - ooOoO0O00 / oo0oO00 * OOooOOo
def oO0o0oOo ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oOooOOo00ooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for I1111i , o0OO0oooo , i1iII1IiiIiI1 in oOooOOo00ooO :
  I11II1i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for ooO0oOOooOo0 , o000O0O in I11II1i1 :
   if 'tube' in ooO0oOOooOo0 :
    pass
   elif 'stage' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o0OO0oooo + '   -   ' + o000O0O + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I1111i )
   elif 'vee' in ooO0oOOooOo0 :
    pass
    if 92 - 92: ooOoO0O00 % OOoOoo + OOoOoo - iI11I1II1I1I . IIi
    if 33 - 33: I11i / o0o00Oo0O + Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: iIi1i1ii1 % Ii + iI11I1II1I1I
def II1Ii11Ii1i1I ( url ) :
 I1 = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ii1iIi1II = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( ii1iIi1II ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in ii1iIi1II :
  Ii1IIiI1i ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 92 - 92: OOooOOo % o0o00Oo0O
  if 55 - 55: iI11I1II1I1I * iiII11i1I1IIi
  if 85 - 85: iI11I1II1I1I . IIiIiII11i
  if 54 - 54: IIi . ii % I1ii11iIi11i
  if 22 - 22: Oooo0O0oo00oO
  if 22 - 22: iiII11i1I1IIi * oo0oO00 - I1ii11iIi11i * o0o00Oo0O / Ii
  if 78 - 78: I1ii11iIi11i * o0o00Oo0O / OOoOoo + ii + Oooo0O0oo00oO
def ii1I1IiiI1ii1i ( ) :
 if 23 - 23: iiII11i1I1IIi % ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
 oOoO ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 oOoO ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 32 - 32: o0o00Oo0O + O0oOO0 % I1ii11iIi11i
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 7 - 7: Ii1I / OOoOoo
def I1i1I11111iI1 ( ) :
 oOoO ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 oOoO ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 32 - 32: oOo0O0Ooo + Ii1I - O0oOO0 + Ii1I / ooOoO0O00 * O0oOO0
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o0OoOoooo0 ( ) :
 if 60 - 60: oOo0O0Ooo % O0oOO0 / I11i % O0oOO0 * Ii / iiII11i1I1IIi
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 i1Ii11II = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 33 - 33: iIi1i1ii1 . ii . O0oOO0
 for iI1o0 in i1Ii11II :
  IiiiI1i1I = oOOoo0Oo + iI1o0 + IIIII
  I1 = Oo0OoO00oOO0o ( IiiiI1i1I )
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for ooO0oOOooOo0 , oo0 , ooo0O , II11IiIi11 , o000O0O in o00oooO0Oo :
   if I1i11II in o000O0O . lower ( ) :
    i1111iI1 ( o000O0O , ooO0oOOooOo0 , 222 , oo0 , II11IiIi11 , ooo0O )
    if 76 - 76: ii - IIiIiII11i % OOooOOo + O0oOO0 + iI11I1II1I1I . OOooOOo
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 16 - 16: I11i . oo0oO00
    if 50 - 50: OOoOoo * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
def i11II ( ) :
 if 69 - 69: OooOO000 - ooOoO0O00 % iiII11i1I1IIi . Oooo0O0oo00oO - Oooo0O0oo00oO
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 i1Ii11II = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 65 - 65: Oooo0O0oo00oO + IIiIiII11i
 for iI1o0 in i1Ii11II :
  Oo0O0OO0OoO0 = oOOoo0Oo + iI1o0 + IIIII
  I1 = Oo0OoO00oOO0o ( Oo0O0OO0OoO0 )
  o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for o000O0O , ooo0O , ooO0oOOooOo0 , I1111i , II11IiIi11 , O0ooo0 in o00oooO0Oo :
   if I1i11II in o000O0O . lower ( ) :
    oOoO ( o000O0O , ooO0oOOooOo0 , O0ooo0 , I1111i , II11IiIi11 , ooo0O )
    if 26 - 26: Oooo0O0oo00oO * I1ii11iIi11i
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 31 - 31: oo0oO00 * O0oOO0 . IIi
    if 35 - 35: oo0oO00
def o00oo ( ) :
 if 70 - 70: oo0oO00 - I1ii11iIi11i / ii % ii
 O00o0 = O0 ( oOOoo0Oo + 'spongemain.php' )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooo0O , ooO0oOOooOo0 , I1111i , II11IiIi11 , O0ooo0 in o00oooO0Oo :
  oOoO ( o000O0O , ooO0oOOooOo0 , O0ooo0 , I1111i , II11IiIi11 , ooo0O )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def oooo0o0OOO0 ( url ) :
 if 17 - 17: IIiIiII11i + oOo0O0Ooo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooo0oO0oOo = ( '%s%s' % ( O0OOOO0000O , url ) )
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , oo0 , ooo0O , i11IIIiI1I , o000O0O in o00oooO0Oo :
  iiiI11 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
  for i111iIi1i1II1 in iiiI11 :
   if i111iIi1i1II1 == url :
    o000O0O = ( '[COLORred]Watched - [/COLOR]' + o000O0O ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  i1111iI1 ( o000O0O , url , 222 , oo0 , i11IIIiI1I , ooo0O )
  if 89 - 89: O0oOO0
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 87 - 87: iiII11i1I1IIi % I1ii11iIi11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: oO0o + OOoOoo / iiII11i1I1IIi * Ii
  if 37 - 37: iiII11i1I1IIi
def iIIiI1111 ( url ) :
 if 91 - 91: ii / I11i . iIi1i1ii1 - iI11I1II1I1I - IIi
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooo0O , url , I1111i , II11IiIi11 , O0ooo0 in o00oooO0Oo :
  oOoO ( o000O0O , url , O0ooo0 , I1111i , II11IiIi11 , ooo0O )
  if 31 - 31: iIi1i1ii1 - oO0o / Oooo0O0oo00oO . ooOoO0O00 / IIi
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 66 - 66: oO0o
  if 72 - 72: OooOO000
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: IIiIiII11i / iIi1i1ii1 + iI11I1II1I1I . oo0oO00 - o0o00Oo0O
def i1111iI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 70 - 70: IIi * O0oOO0 - oo0oO00 + I1ii11iIi11i % Ii1I - iIi1i1ii1
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 81 - 81: o0o00Oo0O . o0o00Oo0O
def oOoO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 75 - 75: iI11I1II1I1I % iIi1i1ii1 + Ii1I * o0o00Oo0O . iiII11i1I1IIi - OOoOoo
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
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
if 18 - 18: OOoOoo
if 66 - 66: O0oOO0 * Ii + OOooOOo / Oooo0O0oo00oO
if 96 - 96: Oooo0O0oo00oO + Oooo0O0oo00oO % iIi1i1ii1 % Oooo0O0oo00oO
if 28 - 28: iI11I1II1I1I + OOooOOo . I11i % Ii
if 58 - 58: oo0oO00 / ii % O0oOO0 + oO0o
def o0ooOO0OOO00o ( string ) :
 if Oo0oOOo == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 76 - 76: ii * ii - iiII11i1I1IIi - iI11I1II1I1I . ii / Ii1I
def oOOOO0oo0O0OO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 O0OOoo0o = [ ]
 try :
  if 19 - 19: OOoOoo % O0oOO0
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  o0ooOO0OOO00o ( 'Making Favorites File' )
  O0OOoo0o . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  o0o00oO0oo000 = open ( I1IIiiIiii , "w" )
  o0o00oO0oo000 . write ( json . dumps ( O0OOoo0o ) )
  o0o00oO0oo000 . close ( )
 else :
  o0ooOO0OOO00o ( 'Appending Favorites' )
  o0o00oO0oo000 = open ( I1IIiiIiii ) . read ( )
  iIiiIiiI1Ii111i = json . loads ( o0o00oO0oo000 )
  iIiiIiiI1Ii111i . append ( ( name , url , iconimage , fanart , mode ) )
  iiii1IIi1 = open ( I1IIiiIiii , "w" )
  iiii1IIi1 . write ( json . dumps ( iIiiIiiI1Ii111i ) )
  iiii1IIi1 . close ( )
  if 38 - 38: O0oOO0 % ii + oO0o * Ii
  if 61 - 61: iI11I1II1I1I
def IIi1iiI ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  O0OOoo0o = [ ]
  o0ooOO0OOO00o ( 'Making Favorites File' )
  O0OOoo0o . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  o0o00oO0oo000 = open ( I1IIiiIiii , "w" )
  o0o00oO0oo000 . write ( json . dumps ( O0OOoo0o ) )
  o0o00oO0oo000 . close ( )
 else :
  o0o = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  oOO00OO0o0O = len ( o0o )
  for III1IiiIiiI1i in o0o :
   o000O0O = III1IiiIiiI1i [ 0 ]
   ooO0oOOooOo0 = III1IiiIiiI1i [ 1 ]
   oo0 = III1IiiIiiI1i [ 2 ]
   try :
    OoO0o00OoO = III1IiiIiiI1i [ 3 ]
    if OoO0o00OoO == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     OoO0o00OoO = oo0
    else :
     OoO0o00OoO = II11IiIi11
   try : Oo00Oooo00o = III1IiiIiiI1i [ 5 ]
   except : Oo00Oooo00o = None
   try : II11II1I = III1IiiIiiI1i [ 6 ]
   except : II11II1I = None
   if 52 - 52: Oooo0O0oo00oO * O0oOO0 + oo0oO00 * oo0oO00 % ooOoO0O00 % oo0oO00
   if III1IiiIiiI1i [ 4 ] == 0 :
    I1IiiiiI ( o000O0O , ooO0oOOooOo0 , '' , oo0 , II11IiIi11 , '' , 'fav' )
   else :
    I1IiiiiI ( o000O0O , ooO0oOOooOo0 , III1IiiIiiI1i [ 4 ] , oo0 , II11IiIi11 , '' , 'fav' )
    if 96 - 96: I11i * O0oOO0 - Oooo0O0oo00oO * I11i * ooOoO0O00
def I1IIIi1i ( name ) :
 iIiiIiiI1Ii111i = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for OooIii1I1iI in range ( len ( iIiiIiiI1Ii111i ) ) :
  if iIiiIiiI1Ii111i [ OooIii1I1iI ] [ 0 ] == name :
   del iIiiIiiI1Ii111i [ OooIii1I1iI ]
   iiii1IIi1 = open ( I1IIiiIiii , "w" )
   iiii1IIi1 . write ( json . dumps ( iIiiIiiI1Ii111i ) )
   iiii1IIi1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 62 - 62: O0oOO0 + I1ii11iIi11i / Ii
 if 90 - 90: iI11I1II1I1I + OOooOOo
def i1i11I ( ) :
 IiIIIiI = os . path . join ( O0O , 'addons.ini' )
 II1iI1iiiI = open ( IiIIIiI , "w+" )
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 II1iI1iiiI . write ( r'[' + IiII + ']' + '\n' )
 for o000O0O , I1111i , ooOo0OoO , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OoOoO00o00 = ( o000O0O + '=plugin://' + IiII + '/?url=' + ooO0oOOooOo0 + '&mode=10012&name=' + ( o000O0O ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( I1111i ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( I1111i ) . replace ( ' ' , '' ) + '+&amp;description=' )
  II1iI1iiiI . write ( OoOoO00o00 + '\n' )
  if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . IIi - Oooo0O0oo00oO / oOo0O0Ooo
  if 98 - 98: IIiIiII11i + IIi + ii / ooOoO0O00 - IIi
def O0o0 ( ) :
 O00o0 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  IiIi1iIIi1 ( '24/7' , ooO0oOOooOo0 , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 81 - 81: ii - Ii1I * ooOoO0O00 - Ii . OOoOoo
def oooOoOoOO ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( o000O0O , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def II1I11Iii1 ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( o000O0O , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def i11OOoo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( o000O0O , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def OooOO ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( o000O0O , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def iio0oo0Oo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o00oooO0Oo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  o0OIiII ( o000O0O , ooO0oOOooOo0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 10 - 10: Ii1I
  if 87 - 87: I1ii11iIi11i % IIi
def ooO0o0oO0 ( ) :
 if 66 - 66: OooOO000 % o0o00Oo0O
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 55 - 55: OOoOoo % oo0oO00 / Ii
def I1111 ( ) :
 if 90 - 90: OooOO000 % oO0o . OooOO000
 O00o0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , I1111i , o000O0O , I1IIII1ii in o00oooO0Oo :
  I1IiiiiI ( o000O0O + '  -  ' + ( I1IIII1ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 10023 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 51 - 51: Ii1I
  if 70 - 70: Ii
  if 57 - 57: oo0oO00 % Oooo0O0oo00oO + OOoOoo * IIi . I1ii11iIi11i
def oooo0 ( ) :
 if 88 - 88: oo0oO00 + oOo0O0Ooo - oo0oO00 / ii - Ii
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
 if 24 - 24: iI11I1II1I1I
def O0Oo0oOOo0O ( url ) :
 iIOo0O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( iIOo0O )
 o00oooO0Oo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 73 - 73: oOo0O0Ooo - iiII11i1I1IIi . iiII11i1I1IIi
  if 22 - 22: OOoOoo / OOoOoo - IIi % oo0oO00 . Oooo0O0oo00oO + iIi1i1ii1
  if 64 - 64: ooOoO0O00 % Ii1I / IIi % ii
  if 24 - 24: OooOO000 + ii . iIi1i1ii1 / OOooOOo / oo0oO00
def ooO ( ) :
 if 61 - 61: o0o00Oo0O
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1i11II ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( ooO0oOOooOo0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  if I1i11II in o000O0O . lower ( ) :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 25 - 25: iI11I1II1I1I * oo0oO00 - O0oOO0 % Ii + IIi % O0oOO0
   if 5 - 5: iI11I1II1I1I . O0oOO0
   if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
def iIi1iiI1i1 ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for IiIIIIIi , I1I , iIio0oooo0OOo00 , o000O0O in o00oooO0Oo :
  OOO0 = ( iIio0oooo0OOo00 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1Ii1 = ( I1I ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0oo0oOoO00 = 'Season ' + I1Ii1 + 'Episode ' + OOO0 + o000O0O
  i1ii1iIi ( O0oo0oOoO00 , IiIIIIIi )
  if 43 - 43: IIi + iiII11i1I1IIi + ooOoO0O00 - OOooOOo + I11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 54 - 54: Ii1I + Ii1I + oo0oO00 % ooOoO0O00 % Ii
  if 100 - 100: Ii1I
def i1ii1iIi ( name , url ) :
 IiIIIIIi = url
 OOOoo000o0oo0 = name
 iii1i1iiiiIi = cloudflare . source ( IiIIIIIi )
 o0O0OOO0Ooo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for ii1iIi1II , o0Ii11iIiiI in o0O0OOO0Ooo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + OOOoo000o0oo0 + o0Ii11iIiiI + '[/COLOR]' , ii1iIi1II , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 82 - 82: ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: IIiIiII11i % oOo0O0Ooo + Oooo0O0oo00oO % ii / iIi1i1ii1
 if 4 - 4: Ii - Oooo0O0oo00oO % Ii1I * OooOO000 % I11i
def O0Oooo ( ) :
 if 71 - 71: OOoOoo . OOoOoo - iI11I1II1I1I
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
 if 79 - 79: o0o00Oo0O
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 32 - 32: IIiIiII11i . o0o00Oo0O + IIi / OOooOOo / iIi1i1ii1 / Oooo0O0oo00oO
 if 15 - 15: Ii1I
def I11iI1 ( url ) :
 I1 = O0 ( url )
 ii11i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii11i ) )
 for url , o000O0O in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 96 - 96: I11i % iIi1i1ii1 / Oooo0O0oo00oO
def Oo0o0ooOoO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 47 - 47: OOooOOo
def Oo0000o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  if 'episode' in url :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 33 - 33: OOooOOo * oo0oO00
  if 48 - 48: ii . OOooOOo
def oOIIIi11 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooOo00O0 = 'http://www.watchseries.ac/search/' + I1i11II . replace ( ' ' , '%20' )
 I1 = O0 ( oooOo00O0 )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for I1111i , ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'watch online' in o000O0O :
   pass
  else :
   print ooO0oOOooOo0
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , I1111i , '' , '' )
   if 26 - 26: OooOO000 . IIi + oOo0O0Ooo . OOooOOo + Oooo0O0oo00oO
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 17 - 17: Oooo0O0oo00oO + Ii + Ii1I % Oooo0O0oo00oO . O0oOO0
def I11iiIi1i1IIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O , iIio0oooo0OOo00 , ooo0O in o00oooO0Oo :
  o000 = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iIio0oooo0OOo00 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , I1111i , '' , ooo0O )
  if 46 - 46: oO0o . o0o00Oo0O * OOoOoo / I11i + ii
def i1Ii1i1I11III ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  o000 = ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 36 - 36: IIi - ii . ii + Ii1I
def o0OoO0000oOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , I1111i , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 42 - 42: OooOO000 % oO0o . Ii1I
def iiIIiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 ii11i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for I1I , oOooOOo00ooO in ii11i :
  o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oOooOOo00ooO ) )
  for url , o000O0O in o00oooO0Oo :
   o000 = ( I1I ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for o000O0O , url in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: iiII11i1I1IIi + oo0oO00 % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * iiII11i1I1IIi
class o0Ooi1II11i1iI1 ( ) :
 if 81 - 81: O0oOO0 . ii * I11i * oO0o
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 10 - 10: O0oOO0 - iiII11i1I1IIi % IIiIiII11i - OooOO000 - ooOoO0O00
  o000 = name
  self . Get_Sources ( ooO0oOOooOo0 , o000 )
  if 10 - 10: Ii1I - oo0oO00 . OooOO000
  if 8 - 8: iI11I1II1I1I % O0oOO0 + I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O0 ( URL )
  o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
   URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
   self . Get_site_link ( URL , season_name )
   if 24 - 24: I11i / IIi / IIi % IIiIiII11i - O0oOO0 * O0oOO0
 def Get_site_link ( self , url , season_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( I1 )
  o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  ii1iii1i = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in o00oooO0Oo :
   self . main ( url , season_name )
  for url in o0O0OOO0Ooo :
   self . main ( url , season_name )
  for url in ii1iii1i :
   self . main ( url , season_name )
   if 58 - 58: OOooOOo
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0oOO = 'DACLIPS'
   if o0oOO in o0Ooi1II11i1iI1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0oOO )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o0oOO = 'FILEHOOT'
    if o0oOO in o0Ooi1II11i1iI1 . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o0oOO )
   else :
    if 'thevideo.me' in url :
     o0oOO = 'THEVIDEO'
     if o0oOO in o0Ooi1II11i1iI1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o0oOO )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o0oOO = 'ALLMYVIDEOS'
      if o0oOO in o0Ooi1II11i1iI1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o0oOO )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o0oOO = 'VIDSPOT'
       if o0oOO in o0Ooi1II11i1iI1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o0oOO )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o0oOO = 'VODLOCKER'
        if o0oOO in o0Ooi1II11i1iI1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o0oOO )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 84 - 84: Ii + OOoOoo . o0o00Oo0O
         if 69 - 69: OooOO000 / ii % Ii
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for o00OO00O0oOO , o000O0O in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 18 - 18: Ii - OOoOoo * O0oOO0 + I11i
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO , o000O0O in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for o00OO00O0oOO in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 33 - 33: OooOO000 % IIiIiII11i
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for o00OO00O0oOO in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 49 - 49: Ii1I + oo0oO00 / I11i + ii + Oooo0O0oo00oO / iIi1i1ii1
 def daclips ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for o00OO00O0oOO in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 29 - 29: IIi - IIi / OOoOoo
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for o00OO00O0oOO in o00oooO0Oo :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 49 - 49: oo0oO00 + O0oOO0 % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
 def Printer ( self , Link , season_name , source_name ) :
  if 4 - 4: IIiIiII11i - O0oOO0 % I1ii11iIi11i * Ii
  if Link in o0Ooi1II11i1iI1 . List :
   pass
  elif source_name in o0Ooi1II11i1iI1 . source_list :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   o0Ooi1II11i1iI1 . List . append ( Link )
   o0Ooi1II11i1iI1 . source_list . append ( source_name )
   if 18 - 18: I1ii11iIi11i % o0o00Oo0O
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
   if 47 - 47: Ii1I * O0oOO0 + iI11I1II1I1I - O0oOO0 / iIi1i1ii1
   if 86 - 86: iIi1i1ii1
   if 43 - 43: oOo0O0Ooo / iiII11i1I1IIi / OOoOoo + iI11I1II1I1I + ii
   if 33 - 33: IIiIiII11i - iIi1i1ii1 - OOoOoo
def iI1iiiiIii ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 92 - 92: oO0o * iIi1i1ii1
def ooo00o0OO ( url ) :
 I1IiiiiI ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( O00o0 )
 for I1I11i , url , Iii1Iii , o000o0o0ooO0 , iIiO0OOoOOO0o0o , oO00OoOOOo , iIOoo0ooo0oo , oOOo0O00o , o0o00oO0oo000 , I11iIiI1 , i1I1iiii1Ii11 in o00oooO0Oo :
  Iii1Iii = Iii1Iii
  if 'Arsenal' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'arsenal-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                                  ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Bournemouth' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'afc-bournemouth.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                       ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Burnley' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'KEGnQWW.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                                   ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Chelsea' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'chelsea.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                                  ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Crystal' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'CrystalPalace.0.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                       ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Everton' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'Everton.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                                   ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Hull' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'hull-city-afc.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                                 ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Leicester' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                       ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Liverpool' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'liverpool-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                               ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Manchester City' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'city-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '               ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Manchester United' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + '91.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '          ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Middlesbrough' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                 ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Southampton' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'southampton-fc-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                   ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Stoke City' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'stoke-city.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                          ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Sunderland' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'sunderland-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                        ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Swansea' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'swansea-city-afc.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                    ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Tottenham' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '        ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Watford' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '                              ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'Bromwich' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '   ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  elif 'West Ham' in Iii1Iii :
   I1iii11 = oOOOo00O00oOo + 'west-ham.png'
   o000O0O = '[COLOR' + iiI1IiI + ']' + I1I11i + ' - ' + Iii1Iii + '             ' + o000o0o0ooO0 + '        ' + iIiO0OOoOOO0o0o + '        ' + oO00OoOOOo + '        ' + iIOoo0ooo0oo + '        ' + oOOo0O00o + '        ' + o0o00oO0oo000 + '        ' + I11iIiI1 + '[/COLOR]'
  I1IiiiiI ( str ( o000O0O ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I1iii11 , I1iii11 , Iii1Iii )
  if 25 - 25: Ii / OOooOOo - OooOO000 / oO0o . I11i . I11i
def iI1iIIII1 ( description ) :
 Iii1Iii = description
 ooO0oOOooOo0 = ( 'http://www.fullmatchesandshows.com/?s=' + Iii1Iii ) . replace ( ' ' , '%20' )
 Oooo ( ooO0oOOooOo0 )
 if 7 - 7: ooOoO0O00
def Oo00oo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o00oooO0Oo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0oOOooOo0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I1111i , OO0o , '' )
  if 79 - 79: Ii1I / o0o00Oo0O % I11i
def o0ooo ( url ) :
 I1 = O0 ( url )
 ii11i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for ii11i in ii11i :
  IiIii11I = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii11i ) )
  for Ooo0O00 in IiIii11I :
   Ooo0O00 = Ooo0O00
  oooo0oOOoO000 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii11i ) )
  for Oo00o00Oo , I1111i , time , i1I1i1I111 in oooo0oOOoO000 :
   i11I1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( i1I1i1I111 )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Ooo0O00 + ' - ' + Oo00o00Oo + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I1111i , OO0o , ( str ( i11I1 ) ) )
   if 90 - 90: I11i * Oooo0O0oo00oO / iIi1i1ii1
 Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if 40 - 40: oOo0O0Ooo * I11i . oOo0O0Ooo
def o00o0O0 ( ) :
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
 if 47 - 47: OOoOoo
def Oo0oo ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  IiIi = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   IiIi = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + IiIi + '[/COLOR]' , url , 10013 , I1111i )
 for url , I1111i , o000O0O in o0O0OOO0Ooo :
  IiIi = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + IiIi + '[/COLOR]' , url , 10013 , I1111i )
def Oooo ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 36 - 36: Oooo0O0oo00oO * IIi
 if 16 - 16: IIiIiII11i
 if 100 - 100: o0o00Oo0O - ooOoO0O00
 if 48 - 48: O0oOO0 % OOoOoo + o0o00Oo0O
 if 27 - 27: Ii1I / Oooo0O0oo00oO
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: iIi1i1ii1 + iI11I1II1I1I + oOo0O0Ooo + OooOO000
 for url , I1111i , o000O0O in o0O0OOO0Ooo :
  IiIi = o000O0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o000O0O :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + IiIi + '[/COLOR]' , url , 10013 , I1111i )
   if 72 - 72: oO0o + Ii + Ii1I
def oOooOoOOo0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for ii1iIi1II in o00oooO0Oo :
  i1Iii1IIiiI = ( ii1iIi1II ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  Ii1IIiI1i ( 'http:' + i1Iii1IIiiI )
  if 34 - 34: oo0oO00
  if 68 - 68: ooOoO0O00 . oo0oO00 . ooOoO0O00 + iIi1i1ii1 % oOo0O0Ooo
  if 32 - 32: OOooOOo . iI11I1II1I1I % O0oOO0 . o0o00Oo0O . OOooOOo / iiII11i1I1IIi
  if 45 - 45: iI11I1II1I1I
def I1I111IIIi1 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , url , 8046 , I1111i )
 for url in o0O0OOO0Ooo :
  IiIi1iIIi1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def oOOo00O0O0 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  Ii1IIiI1i ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 11 - 11: Ii + Ii1I + Ii
def IIi11I1i1I1I ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % IIi % IIiIiII11i
def IiIII1 ( ) :
 IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0OOOO ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( O00o0 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + I1111i )
 for url in next :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - iIi1i1ii1 . ii
  if 10 - 10: OooOO000
def I11i1i11IiIi1 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def I11i1I1Ii ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  url = ( url ) . replace ( '\/' , '/' )
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 10012 , '' )
  if 26 - 26: ooOoO0O00 / iiII11i1I1IIi . iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1i11IIIi ( name , url ) :
 III1IIIIIiiI = 0
 name = name
 url = url
 ii1I = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ii1IIiI1i ( url )
  if 38 - 38: o0o00Oo0O
  if 79 - 79: ooOoO0O00 . O0oOO0
  if 34 - 34: OooOO000 * IIiIiII11i
  if 71 - 71: iIi1i1ii1
  if 97 - 97: Ii1I
  if 86 - 86: I1ii11iIi11i - Oooo0O0oo00oO . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
  if 34 - 34: I11i . OooOO000 % iIi1i1ii1 - o0o00Oo0O / OooOO000
  if 91 - 91: Ii % OooOO000 * O0oOO0 - Ii1I . OooOO000
def iIo00oo ( ) :
 O00o0 = iIi11i1 ( 'http://documentarylovers.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  if 'genre' in ooO0oOOooOo0 :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , ooO0oOOooOo0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O000Oo00 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( O00o0 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , I1111i )
 for url in next :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 43 - 43: oO0o . OOoOoo * I1ii11iIi11i
def iio00O0o00oo ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in o0O0OOO0Ooo :
  I11i1I1Ii ( url )
  if 19 - 19: oOo0O0Ooo
def oOOoo ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II11 = 'http://documentarylovers.com/?s=' + ( I1i11II ) . replace ( ' ' , '+' )
 I1iii = II11 . lower ( )
 O000Oo00 ( I1iii )
 if 26 - 26: oo0oO00 + OooOO000 + oo0oO00 / OooOO000
def oOo0Oo00O ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if 'films' in url :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def i1io0o00O ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O00o0 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  if 'films' in url :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + I1111i )
 for url in o0O0OOO0Ooo :
  IiIi1iIIi1 ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def iiiI1ii ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  if 'rtd' in url :
   oOoooOooOOoO ( url )
   if 90 - 90: iiII11i1I1IIi * IIi - iiII11i1I1IIi + oO0o + oo0oO00 % o0o00Oo0O
def oOoooOooOOoO ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( O00o0 )
 for O0o0O00Oo0o0 , file in o00oooO0Oo :
  url = ( 'https://rtd.rt.com' + O0o0O00Oo0o0 + file )
  Ii1IIiI1i ( url )
  if 11 - 11: Oooo0O0oo00oO % OooOO000 * OOooOOo
  if 58 - 58: ii - oo0oO00 + iI11I1II1I1I * Ii
def OoOiII11IiIi ( ) :
 I1 = iIi11i1 ( 'http://www.stream2watch.co/live-tv' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i , o000O0O , iII1I1i in o00oooO0Oo :
  IiIi1iIIi1 ( ( o000O0O + '[COLOR' + iiI1IiI + ']' + iII1I1i + '[/COLOR]' ) , ooO0oOOooOo0 , 8086 , I1111i )
  if 6 - 6: O0oOO0 / o0o00Oo0O / IIi / iIi1i1ii1 / O0oOO0 . iI11I1II1I1I
def oo0O0 ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 8087 , I1111i )
  if 7 - 7: IIiIiII11i / iIi1i1ii1 % oo0oO00 + oOo0O0Ooo - o0o00Oo0O
def IiI1Iii1IIII1Iii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  OOOOOOo0o0O0o ( url , o000O0O )
  if 8 - 8: I11i / I11i - oo0oO00 + I11i * OOooOOo . I11i
def OOOOOOo0o0O0o ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  print url
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 45 - 45: IIiIiII11i * ooOoO0O00
def II1ii1 ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooO0oOOooOo0 , 3002 , 'http://www.solie.org/alibrary/' + I1111i )
def oO0OOO ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1111i )
def IiI1IIiiiii ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 II111iii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( O00o0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , o000O0O in II111iii :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']Season- ' + o000O0O + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , I1111i , o000O0O in o0O0OOO0Ooo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I1111i )
def OooO00o000 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  i1i11II1 ( url )
def i1i11II1 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
  if 5 - 5: oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
def IiIiII1 ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def Oo0OOOOOOO0oo ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "v.src = '([^']*)';" ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  OO0OoOOO0 ( url )
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
def I1i11111i1i11 ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def I1iIIIiiii ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  if 'mp4' in url :
   Ii1IIiI1i ( url )
 for url in o0O0OOO0Ooo :
  yt . PlayVideo ( url )
  if 44 - 44: OooOO000 / IIi * Oooo0O0oo00oO * ooOoO0O00 . IIi * Ii
def O0o0oo0O ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooO0oOOooOo0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def Ooo00OOo000 ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for o000O0O , url in o00oooO0Oo :
  if '(Free Access)' in o000O0O :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def i1ooOO00o0 ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for I1111i , o000O0O , url in o00oooO0Oo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , I1111i , II11IiIi11 , '' )
  if 44 - 44: oOo0O0Ooo % Oooo0O0oo00oO * Ii * Ii - I1ii11iIi11i . OooOO000
def o00i111iiIiiIiI ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  OOooooO ( 'http://watchxxxfree.com/categories' )
 if O0oO0 == 1 :
  oOoo00 ( 'http://www.perfectgirls.net' )
 if O0oO0 == 2 :
  IIiIi ( 'http://www.xvideos.com/best' )
 if O0oO0 == 3 :
  I1I1IIiiI1 ( 'http://www.xvideos.com/best' )
 if O0oO0 == 4 :
  IIiIi ( 'http://www.xvideos.com/best' )
 if O0oO0 == 5 :
  IIiIi ( 'http://www.xvideos.com/verified/videos' )
 if O0oO0 == 6 :
  oooOOO0o0O0 ( 'http://www.xvideos.com/tags' )
 if O0oO0 == 7 :
  iiiI1IiI ( 'http://www.xvideos.com/porn' )
 if O0oO0 == 8 :
  Ii111IIIIii ( )
  if 54 - 54: iiII11i1I1IIi / oOo0O0Ooo * oo0oO00 / Ii * OooOO000 . iI11I1II1I1I
  if 40 - 40: oOo0O0Ooo . IIi / ooOoO0O00
  if 28 - 28: IIi
  if 66 - 66: oo0oO00
  if 27 - 27: o0o00Oo0O
  if 73 - 73: Ii + O0oOO0 % oo0oO00 . ii % O0oOO0
  if 32 - 32: Ii - IIiIiII11i
  if 21 - 21: OOooOOo - IIiIiII11i
  if 10 - 10: OOooOOo - I11i * Ii / I1ii11iIi11i + I11i + iI11I1II1I1I
def IiIIIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  if 'ch' in url :
   Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def Oo0iII ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 O0oo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , o000O0O in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for o000O0O , url in O0oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iIIi1OoOo0O00 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   iI1i1iI1iI ( url )
def I1IIiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def OOooooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O , oOOo00O0OOOo in o00oooO0Oo :
  if 'category' in url :
   Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORorange]   ' + oOOo00O0OOOo + '[/COLOR]' , url , 90006 , I1111i , oOOOo00O00oOo + 'Jizbox.png' , '' )
def OOOOoOoO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 O0oo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , I1111i , '' , '' )
 for url in O0oo :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OO000 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   iI1i1iI1iI ( url )
def iI1i1iI1iI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def oOoo00 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O , oOOo00O0OOOo in o00oooO0Oo :
  if 'category' in url :
   Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORorange]' + oOOo00O0OOOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def o0oOoo0o ( url ) :
 I1 = O0 ( url )
 IiIIIIIi = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 O0oo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , I1111i , '' , '' )
 for url in O0oo :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , IiIIIIIi + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def IiiIiIIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in o00oooO0Oo :
  O00Oo ( 'http://www.perfectgirls.net' + url )
def O00Oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( 'http://' + url )
def iiiI1IiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , o000O0O , oOOo00O0OOOo in o00oooO0Oo :
  Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORgreen] - No of Videos : [COLORorange]' + oOOo00O0OOOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oooOOO0o0O0 ( url ) :
 I1 = O0 ( url )
 O0oo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0oo :
  Oo0O0000Oo00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , o000O0O , oOOo00O0OOOo in o00oooO0Oo :
  Oo0O0000Oo00o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORgreen] - No of Videos : [COLORorange]' + ( oOOo00O0OOOo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 63 - 63: I11i / o0o00Oo0O - ii
def oo0O0Ii111Ii11 ( url ) :
 I1 = O0 ( url )
 O0oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in O0oo :
  Oo0O0000Oo00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O , OOOoo in o00oooO0Oo :
  Oo0O0000Oo00o ( o000O0O + '--' + ( OOOoo ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I1111i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - Oooo0O0oo00oO
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def IIiIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , o000O0O , iIi11ii , O00000OO00OO in o00oooO0Oo :
  Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORgreen] - Porn Quality : [COLORorange]' + O00000OO00OO + ' - [COLORred]' + iIi11ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , I1111i , I1111i , O00000OO00OO + ' - ' + iIi11ii )
 iI11iI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in iI11iI :
  Oo0O0000Oo00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 100 - 100: ii + Ii % I11i + oOo0O0Ooo . I1ii11iIi11i . IIiIiII11i
def I1I1IIiiI1 ( url ) :
 I1 = O0 ( url )
 ii11i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 O0oo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0oo :
  Oo0O0000Oo00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii11i ) )
 for url , o000O0O in o00oooO0Oo :
  if '/c/' in url :
   Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 93 - 93: IIiIiII11i . Ii + IIiIiII11i % O0oOO0
   if 98 - 98: OooOO000 * O0oOO0 * OOooOOo + IIi * iiII11i1I1IIi
def Ii111IIIIii ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii11iI1iIiiI = ( I1i11II ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 I1iii = ii11iI1iIiiI . lower ( )
 I1Ii11i = 'http://www.xvideos.com/?k=' + I1iii
 print I1Ii11i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O0 ( I1Ii11i )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for I1111i , ooO0oOOooOo0 , o000O0O , iIi11ii , O00000OO00OO in o00oooO0Oo :
  Oo0O0000Oo00o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[COLORgreen] - Porn Quality : [COLORorange]' + O00000OO00OO + ' - [COLORred]' + iIi11ii + '[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10108 , I1111i , I1111i , O00000OO00OO + ' - ' + iIi11ii )
 iI11iI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for ooO0oOOooOo0 in iI11iI :
  Oo0O0000Oo00o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 99 - 99: Ii - iiII11i1I1IIi
def o0O0O0O00o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 ii1iii1i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in o0O0OOO0Ooo :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in ii1iii1i :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Oo ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 36 - 36: Oooo0O0oo00oO - OOooOOo - iI11I1II1I1I
 if 10 - 10: Ii1I / IIi * ooOoO0O00 % o0o00Oo0O + oo0oO00
def I1i1ii1ii ( ) :
 if 32 - 32: iIi1i1ii1 / ii
 if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - iiII11i1I1IIi - Ii
 if 84 - 84: ooOoO0O00 - oOo0O0Ooo % iiII11i1I1IIi
 if 80 - 80: I11i % iiII11i1I1IIi
 if 80 - 80: IIi
 if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
 if 59 - 59: Ii1I + oo0oO00 . O0oOO0
 if 87 - 87: oO0o
 if 34 - 34: OooOO000 . OOooOOo / Ii / iiII11i1I1IIi
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + Oooo0O0oo00oO
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def I11II11IiI11 ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 8092 , I1111i )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def O00o ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 Ii11Iiii1iiii = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for I1111i in Ii11Iiii1iiii :
  I1111i = I1111i
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 8092 , I1111i )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 10 - 10: iiII11i1I1IIi % I1ii11iIi11i
def i111111 ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 77 - 77: iI11I1II1I1I
  if 77 - 77: IIi
  if 90 - 90: oO0o % o0o00Oo0O + oo0oO00 + ooOoO0O00 - O0oOO0
  if 77 - 77: iiII11i1I1IIi + IIi - OooOO000
ooOO = '{PQ},' ; oO0o0 = '{SC},' ; i1Ii1i11ii = '{XG},' ; oO0O0oo = '{JP},' ; OOOOOOO00OO = '{HW},' ; o0Oo00 = '{RT},'
def iI1 ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiII1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 69 - 69: IIiIiII11i + iiII11i1I1IIi
 O00ooOo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oooOOO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 Iii1o00o0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OOoOo0O0 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1o0 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1i11II
 I1IiiiiI1i1I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I11i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 ooOooO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oooo = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 29 - 29: Ii1I % oOo0O0Ooo - OooOO000 + oOo0O0Ooo . oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 45 - 45: ooOoO0O00 % Oooo0O0oo00oO % IIiIiII11i
 if 4 - 4: O0oOO0 * oOo0O0Ooo - OOoOoo / IIiIiII11i + Oooo0O0oo00oO / Ii
 Iiii = Oo0OoO00oOO0o ( O00ooOo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( oooOOO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oO0o0O = Oo0OoO00oOO0o ( Iii1o00o0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iiI1ii1Iii11I = Oo0OoO00oOO0o ( I1o0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IIiIi11 = Oo0OoO00oOO0o ( I1IiiiiI1i1I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oO0OO0O0 = Oo0OoO00oOO0o ( I11i1I1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 iIIi1II1 = Oo0OoO00oOO0o ( ooOooO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IiI1I11ii = Oo0OoO00oOO0o ( oooo )
 if 57 - 57: I1ii11iIi11i . iIi1i1ii1 % Oooo0O0oo00oO
 if 56 - 56: ii * iIi1i1ii1 + OooOO000 / oOo0O0Ooo * iIi1i1ii1 / ooOoO0O00
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for i111IiIi1 , o000O0O in o00oooO0Oo :
   if I1i11II in o000O0O . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooO0oOOooOo0 + i111IiIi1 ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 16 - 16: Ii * Oooo0O0oo00oO . iIi1i1ii1
    if 100 - 100: oO0o . oo0oO00 / IIi . I11i - OOooOOo . oo0oO00
    if 30 - 30: IIi % oo0oO00 + I11i
    if 65 - 65: iI11I1II1I1I . iiII11i1I1IIi / IIi
    if 12 - 12: oOo0O0Ooo + OooOO000
    if 80 - 80: O0oOO0 . o0o00Oo0O
    if 90 - 90: IIiIiII11i / oO0o / IIi
 if Iiii != 'Failed' :
  ii1iii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for i111IiIi1 , o000O0O in ii1iii1i :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O00ooOo + i111IiIi1 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  o00O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in o00O0O :
   if I1i11II in o000O0O . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 70 - 70: IIi - IIiIiII11i . I1ii11iIi11i / I1ii11iIi11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if oO0o0O != 'Failed' :
  III = [ ]
  i1iiIIiiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0o0O )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in i1iiIIiiiI :
   if I1i11II in o000O0O . lower ( ) :
    if o000O0O in III :
     pass
    else :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooO0oOOooOo0 , 1016 , oo0 , i11IIIiI1I , ooo0O )
     III . append ( o000O0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iiI1ii1Iii11I != 'Failed' :
  I1IIiIi1iI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iiI1ii1Iii11I )
  for ooO0oOOooOo0 , I1111i , o000O0O in I1IIiIi1iI :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooO0oOOooOo0 , 7067 , I1111i )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 87 - 87: I11i / iIi1i1ii1 / Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 95 - 95: ooOoO0O00 / IIi / IIi
    if 65 - 65: OooOO000 + iiII11i1I1IIi * iiII11i1I1IIi
    if 79 - 79: ooOoO0O00 / I1ii11iIi11i - oOo0O0Ooo . o0o00Oo0O
    if 56 - 56: iIi1i1ii1 % o0o00Oo0O * ooOoO0O00 - IIiIiII11i
    if 74 - 74: ooOoO0O00 - OOooOOo % O0oOO0 . o0o00Oo0O - ii
    if 84 - 84: OooOO000
    if 53 - 53: ooOoO0O00
    if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
    if 9 - 9: ooOoO0O00 - OOooOOo
 if oO0OO0O0 != 'Failed' :
  Oo00o0OOo0OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OO0O0 )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in Oo00o0OOo0OO :
   if I1i11II in o000O0O . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 222 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 18 - 18: OOoOoo - iIi1i1ii1 / IIiIiII11i / Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iIIi1II1 != 'Failed' :
  i1Ii1IiiIi1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1II1 )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in i1Ii1IiiIi1II :
   if I1i11II in o000O0O . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 222 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 54 - 54: IIi % ooOoO0O00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
 if IiI1I11ii != 'Failed' :
  Oo0Oo00O00o0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiI1I11ii )
  for ooO0oOOooOo0 , oo0 , o000O0O in Oo0Oo00O00o0 :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , oo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + IIi + oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 i1Ii11II = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 97 - 97: OOoOoo % Ii % oo0oO00
 for iI1o0 in i1Ii11II :
  IiiiI1i1I = oOOoo0Oo + iI1o0 + IIIII
  IIi1i = Oo0OoO00oOO0o ( IiiiI1i1I )
  if IIi1i != 'Failed' :
   oO0oi1I1iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1i )
   for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in oO0oi1I1iI1 :
    if I1i11II in o000O0O . lower ( ) :
     o0OIiII ( '[COLOR' + iiI1IiI + ']' + o000O0O + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , 222 , oo0 , i11IIIiI1I , ooo0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 91 - 91: O0oOO0 / iI11I1II1I1I + O0oOO0
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 28 - 28: iI11I1II1I1I * oo0oO00 . oOo0O0Ooo
 i1Ii11II = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 78 - 78: ii . ii / o0o00Oo0O
 if 25 - 25: IIiIiII11i % IIiIiII11i - IIi . o0o00Oo0O
 for iI1o0 in i1Ii11II :
  IiiiI1i1I = iiII1 + iI1o0
  O00O0 = Oo0OoO00oOO0o ( IiiiI1i1I )
  if O00O0 != 'Failed' :
   ii11i1i = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O00O0 )
   for i111IiIi1 , o000O0O in ii11i1i :
    if I1i11II in o000O0O . lower ( ) :
     O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiII1 + iI1o0 + i111IiIi1 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 12 - 12: OOooOOo + I11i . OooOO000
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 52 - 52: oO0o
     if 4 - 4: IIi % Ii1I + oo0oO00 - Ii1I
def Oo00o0OO0O00o ( ) :
 if 98 - 98: IIi - o0o00Oo0O * O0oOO0 * IIi * IIi
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 if 44 - 44: iIi1i1ii1 + oo0oO00
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( I1i11II ) . replace ( ' ' , '%20' )
 IiIIIIIi = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 O00ooOo = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 oooOOO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 Iii1o00o0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1iii ) . replace ( ' ' , '+' )
 OOoOo0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 I1o0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 I1IiiiiI1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 66 - 66: O0oOO0
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 34 - 34: iiII11i1I1IIi % Ii + Ii - iiII11i1I1IIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( IiIIIIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = Oo0OoO00oOO0o ( O00ooOo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( oooOOO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 oO0o0O = cloudflare . source ( Iii1o00o0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O00O0 = Oo0OoO00oOO0o ( OOoOo0O0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iiI1ii1Iii11I = Oo0OoO00oOO0o ( I1o0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 IIiIi11 = Oo0OoO00oOO0o ( I1IiiiiI1i1I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 2 - 2: IIiIiII11i + ooOoO0O00
 if IIiIi11 != 'Failed' :
  oO0OO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiIi11 )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in oO0OO00 :
   if I1iii in o000O0O . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
    if 16 - 16: ii / O0oOO0 . IIi * OOoOoo - oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 32 - 32: oOo0O0Ooo / oO0o
 if iiI1ii1Iii11I != 'Failed' :
  I1IIiIi1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI1ii1Iii11I )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in I1IIiIi1iI :
   if I1iii in o000O0O . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 1016 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 28 - 28: I1ii11iIi11i / iIi1i1ii1 . iiII11i1I1IIi + oO0o + oo0oO00 % I1ii11iIi11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
    if 92 - 92: IIi . OOooOOo . oo0oO00 - ii / OOoOoo
    if 80 - 80: iI11I1II1I1I / Ii + iiII11i1I1IIi
    if 41 - 41: OooOO000 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
    if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . IIi % iiII11i1I1IIi . iIi1i1ii1
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 67 - 67: ii + OooOO000 / OOoOoo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for I1111i , ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
   if I1iii in o000O0O . lower ( ) :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , I1111i , '' , '' )
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
  ii1iii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for o000O0O in ii1iii1i :
   if I1iii in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( o000O0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00ooOo + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 54 - 54: ii . O0oOO0 - iiII11i1I1IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for o000O0O in o00O0O :
   if I1iii in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( o000O0O + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oooOOO + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 76 - 76: OooOO000
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if oO0o0O != 'Failed' :
  i1iiIIiiiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0o0O )
  for ooO0oOOooOo0 , I1111i , o000O0O in i1iiIIiiiI :
   if I1iii in o000O0O . lower ( ) :
    IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + ' - Source - Dizi[/COLOR]' , ooO0oOOooOo0 , 8062 , I1111i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 61 - 61: OOoOoo / IIiIiII11i * OOoOoo * OOooOOo * OooOO000 . Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if O00O0 != 'Failed' :
  ii11i1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00O0 )
  for ooO0oOOooOo0 , oo0 , ooo0O , i11IIIiI1I , o000O0O in ii11i1i :
   if I1iii in o000O0O . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '- Source Scooby[/COLOR]' ) , ooO0oOOooOo0 , 1016 , oo0 , i11IIIiI1I , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 26 - 26: OooOO000 / OOoOoo - oO0o . iI11I1II1I1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: OOoOoo % IIi / I1ii11iIi11i - iiII11i1I1IIi / o0o00Oo0O
 oo00oO00oooo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if O00O0 != 'Failed' :
  for iI1o0 in oo00oO00oooo :
   IiiiI1i1I = oOOoo0Oo + iI1o0 + IIIII
   iIIi1II1 = O0 ( IiiiI1i1I )
   if iIIi1II1 != 'Failed' :
    i1Ii1IiiIi1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIi1II1 )
    for o000O0O , ooo0O , ooO0oOOooOo0 , I1111i , II11IiIi11 , O0ooo0 in i1Ii1IiiIi1II :
     if I1iii in o000O0O . lower ( ) :
      I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , O0ooo0 , I1111i , II11IiIi11 , ooo0O )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 63 - 63: IIiIiII11i - oo0oO00 . OOooOOo
      Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
      if 8 - 8: oOo0O0Ooo * OOoOoo / iIi1i1ii1 + OOooOOo . iIi1i1ii1 - Oooo0O0oo00oO
      if 80 - 80: iI11I1II1I1I / O0oOO0 * I1ii11iIi11i - Oooo0O0oo00oO * iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0ooOO0 ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( I1i11II ) . replace ( ' ' , '+' )
 if 99 - 99: iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 81 - 81: Ii1I + Oooo0O0oo00oO
 if I1 != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , o000O0O in o0O0OOO0Ooo :
   if I1i11II in o000O0O . lower ( ) :
    O0OoO0ooOO0o ( ( o000O0O + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + ooO0oOOooOo0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 11 - 11: Ii1I % I1ii11iIi11i * OooOO000 - O0oOO0 + Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
Oo0O00OO = '{ZH},' ; o0OO00O00oO = '{IX},' ; I11O0O0o = '{LM},'
if 45 - 45: OOooOOo
def oo0OoOO000O ( url ) :
 Oo0o0OoOoOo0 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo0o0OoOoOo0 )
 for url , I1I , I1IIII1ii , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( I1I ) . replace ( 'Sezon' , ' Season ' ) + ( I1IIII1ii ) . replace ( 'Bölüm' , ' Episode ' ) + o000O0O , url , 8063 , '' )
  if 36 - 36: IIi * oOo0O0Ooo * Ii1I . oo0oO00 * Ii1I
  if 76 - 76: Oooo0O0oo00oO + o0o00Oo0O / iIi1i1ii1 - oO0o
  if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * iiII11i1I1IIi * IIiIiII11i * Ii1I
  if 9 - 9: Ii + Oooo0O0oo00oO - OOooOOo / OOoOoo % ooOoO0O00 / O0oOO0
def iiI1 ( url ) :
 Oo0o0OoOoOo0 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Oo0o0OoOoOo0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , url , 222 , '' )
  if 42 - 42: oO0o - Ii1I * iIi1i1ii1 - OOoOoo
  if 75 - 75: iiII11i1I1IIi * I1ii11iIi11i / OooOO000 * I1ii11iIi11i / OOoOoo
  if 14 - 14: ooOoO0O00 * iI11I1II1I1I - IIi * OOooOOo - iiII11i1I1IIi / O0oOO0
  if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
def oOoO0o0o ( ) :
 if 72 - 72: oo0oO00 * OOooOOo % OooOO000 % OOoOoo
 Oo0o0OoOoOo0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo0o0OoOoOo0 )
 for ooO0oOOooOo0 , I1111i , o000O0O , I1IIII1ii in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O + '  -  ' + ( I1IIII1ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 8063 , I1111i )
  if 22 - 22: Oooo0O0oo00oO - Ii1I / iIi1i1ii1
def o0ooO0Oo ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O , I1111i in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 8002 , I1111i )
def O00oO0oo ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( O00o0 )
 for I1111i , time , url , o000O0O , IiIo0o0OO0o00o0O in o00oooO0Oo :
  I1IiiiiI ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , time ) , url , 1015 , I1111i , IiIo0o0OO0o00o0O )
  if 65 - 65: o0o00Oo0O . Ii1I * OooOO000
def iiIiI11IiI ( ) :
 if 23 - 23: oOo0O0Ooo - I11i % O0oOO0 . o0o00Oo0O * ii + OOoOoo
 IiIi1iIIi1 ( 'Coronation Street' , '' , 8001 , '' )
 IiIi1iIIi1 ( 'Eastenders' , '' , 8002 , '' )
 IiIi1iIIi1 ( 'Emmerdale' , '' , 8003 , '' )
 IiIi1iIIi1 ( 'Hollyoaks' , '' , 8004 , '' )
 IiIi1iIIi1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 53 - 53: I1ii11iIi11i
 if 3 - 3: iIi1i1ii1 - ii * ii - oOo0O0Ooo / OooOO000 * Ii1I
 if 58 - 58: iIi1i1ii1 % iI11I1II1I1I / Ii % I11i . OooOO000 * iiII11i1I1IIi
 if 32 - 32: ii + I11i
def o0000OOOo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Holly' in o000O0O :
   I1111i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , I1111i )
   else :
    pass
    if 56 - 56: ooOoO0O00 + ii % oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 36 - 36: iiII11i1I1IIi * oo0oO00 * o0o00Oo0O * Oooo0O0oo00oO - I11i / Ii1I
def oooOo0OO ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'East' in o000O0O :
   I1111i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , I1111i )
   else :
    pass
    if 9 - 9: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: OOoOoo / IIi % I11i % Ii
def o0OO0Oooo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Emmer' in o000O0O :
   I1111i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , I1111i )
   else :
    pass
    if 97 - 97: iiII11i1I1IIi
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: ii - Oooo0O0oo00oO + o0o00Oo0O * iIi1i1ii1 * oo0oO00
def iIi1 ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Coro' in o000O0O :
   I1111i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , I1111i )
   else :
    pass
    if 21 - 21: Ii * iiII11i1I1IIi / OOoOoo % iiII11i1I1IIi * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: iI11I1II1I1I
def III1Ii11i1II ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Celeb' in o000O0O :
   I1111i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooO0oOOooOo0 :
    O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , I1111i )
   else :
    pass
    if 28 - 28: OOooOOo % O0oOO0 - Oooo0O0oo00oO + Oooo0O0oo00oO + O0oOO0 / iI11I1II1I1I
def oo0oOOoOoo ( name , url ) :
 OOOo0Ooo0o00o = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OOOo0Ooo0o00o :
  oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  O00o0 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( O00o0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  O00o0 = open_url ( url )
  OooO = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( O00o0 ) [ - 1 ]
  oOo = OooO . replace ( '\\/' , '/' )
 i111iiI1ii = xbmcgui . ListItem ( name , '' , '' )
 i111iiI1ii . setPath ( oOo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111iiI1ii )
 if 95 - 95: OooOO000 * ooOoO0O00 + O0oOO0
 if 40 - 40: IIiIiII11i
def iII1 ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for ooO0oOOooOo0 , o000O0O in o0O0OOO0Ooo :
  IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 7 - 7: Ii1I - iI11I1II1I1I
def oOOOo0Oooo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Movies' in o000O0O :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooO0oOOooOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def I1iiIIiI11I ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O00o0 )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1111i )
 for url in o0O0OOO0Ooo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 29 - 29: oo0oO00 + O0oOO0 % OOoOoo + OOooOOo
  if 92 - 92: I11i
def IiI ( url ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url , I1111i in o00oooO0Oo :
  if '{{' in o000O0O :
   pass
  else :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I1111i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
ii111Ii1i = '{UJ},' ; IiI1I1II = '{WE},' ; oOoO0o = '{WP},' ; i1II = '{PP},'
def OOOoooOo00O ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url , I1111i in o00oooO0Oo :
  if '{{' in o000O0O :
   pass
  else :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I1111i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiIIiI1I ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  oOoO0oOO0o ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoO0oOO0o ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: O0oOO0 * oo0oO00
 if 88 - 88: o0o00Oo0O % iIi1i1ii1 . iIi1i1ii1 . OooOO000 / ooOoO0O00
 if 16 - 16: I1ii11iIi11i * OooOO000
def O0ooO0o ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if '(cooltvseries.com)' in o000O0O :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , o000O0O in o0O0OOO0Ooo :
  if '(cooltvseries.com)' in o000O0O :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def IiII1111I ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( ( url ) . replace ( ' ' , '%20' ) )
iiIIii111Ii = '{XX},' ; OO000oooOo000 = '{UD},' ; o0oO0o0Oo0 = '{YT},' ; i1I1iiiI = '{JS},' ; i1IiIi1I1i = '{PF},'
if 39 - 39: Ii + Oooo0O0oo00oO % iiII11i1I1IIi + IIi * oOo0O0Ooo + OooOO000
def Oo00oOo ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O , I1111i in o00oooO0Oo :
  O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( ooO0oOOooOo0 ) ) , 222 , I1111i )
  if 51 - 51: iiII11i1I1IIi
def O0O00OooO ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( O00o0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( O00o0 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  if 'youtu' in url :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I1111i )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 81 - 81: o0o00Oo0O
def i11ii11IiI1 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 47 - 47: iI11I1II1I1I % oo0oO00 . oo0oO00 / o0o00Oo0O . Ii * IIi
def iio0Oo ( url ) :
 O00o0 = O0
 o00oooO0Oo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 222 , I1111i )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . OOoOoo
  if 70 - 70: ii . OOoOoo / O0oOO0 . O0oOO0 - I11i
  if 29 - 29: oo0oO00 % Oooo0O0oo00oO - OOoOoo
  if 26 - 26: o0o00Oo0O . oo0oO00 + iiII11i1I1IIi - IIi . oo0oO00
  if 2 - 2: Ii1I . I1ii11iIi11i * Oooo0O0oo00oO % IIiIiII11i . iiII11i1I1IIi
def II1i1iI ( ) :
 if 5 - 5: OOooOOo + iiII11i1I1IIi * OOoOoo
 IiIi1iIIi1 ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
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
 O00o0 = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O00o0 )
 print 'Len Match: >>>' + str ( len ( o00oooO0Oo ) )
 for o000O0O , I1111i , OoooO in o00oooO0Oo :
  oo0OOoOo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1111i ) . replace ( '\\' , '' )
  if OoooO == i1Iiii111 :
   IiIi1iIIi1 ( o000O0O , '' , 7022 , oo0OOoOo0 )
  elif iii11Ii == True :
   IiIi1iIIi1 ( o000O0O , '' , 7022 , oo0OOoOo0 )
  else : pass
  if 63 - 63: OOooOOo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: IIiIiII11i * IIi + IIiIiII11i % iiII11i1I1IIi . ooOoO0O00 . O0oOO0
def Iiii1II ( Search_Name ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O00o0 )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( O00o0 )
 for I1111i , ooO0oOOooOo0 , IiIIIIIi , O00ooOo in o00oooO0Oo :
  oo0OOoOo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I1111i ) . replace ( '\\' , '' )
  O0OoO0ooOO0o ( Search_Name + ': Link 1' , ( ooO0oOOooOo0 ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  O0OoO0ooOO0o ( Search_Name + ': Link 2' , ( IiIIIIIi ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  O0OoO0ooOO0o ( Search_Name + ': Link 3' , ( O00ooOo ) . replace ( '\\' , '' ) , 222 , oo0OOoOo0 )
  if 83 - 83: Ii1I * oo0oO00 . ii % IIi
def I1iiiiI ( ) :
 O00o0 = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def o0oOOO0 ( ) :
 O00o0 = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def i1Iii ( ) :
 O00o0 = O0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( O00o0 )
 for o000O0O , ooO0oOOooOo0 in o00oooO0Oo :
  O0OoO0ooOO0o ( o000O0O , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 96 - 96: iIi1i1ii1
def o0OOO ( url ) :
 url
 i111iIi1i1II1 = xbmcgui . ListItem ( o000O0O , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111iIi1i1II1 )
 return
 if 40 - 40: Ii * IIiIiII11i
 if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def O00O ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( O00o0 )
 for url , ooo0O , I1111i , o000O0O in o00oooO0Oo :
  I1IiiiiI ( o000O0O , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I1111i , '' , ( ooo0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 for url in o0O0OOO0Ooo :
  IiIi1iIIi1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 42 - 42: I11i + O0oOO0 - ii + iiII11i1I1IIi % oO0o
def IiIIi ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , ooo0O , I1111i in o00oooO0Oo :
  o0OIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I1111i , '' , ooo0O )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 oOooOOo00ooO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for ooiIi11i1I11Ii in oOooOOo00ooO :
  iIIII = ( ooiIi11i1I11Ii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IiiiiI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I1111i , '' , iIIII )
  if 59 - 59: Ii - oo0oO00
def oooO00oOOooO ( INFO ) :
 OOOiiiiI ( 'info for workout' , INFO )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
 if 3 - 3: I11i - ii + iiII11i1I1IIi . oo0oO00
 if 88 - 88: oo0oO00 - iiII11i1I1IIi
def OOoOO0oOooo ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( ( o000O0O ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def i1II11II11 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def oooiiI11 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  if '=' in o000O0O :
   pass
  else :
   O0OoO0ooOO0o ( ( o000O0O ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def i11IiIiii ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  if '=' in o000O0O :
   pass
  else :
   O0OoO0ooOO0o ( o000O0O , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 15 - 15: OOoOoo * iI11I1II1I1I * O0oOO0
   if 96 - 96: OooOO000 * iI11I1II1I1I / OOooOOo % Oooo0O0oo00oO * IIiIiII11i
   if 3 - 3: Oooo0O0oo00oO . I1ii11iIi11i / Ii + oO0o
   if 47 - 47: iIi1i1ii1 . Oooo0O0oo00oO
   if 96 - 96: oo0oO00 % IIiIiII11i / OOoOoo % Oooo0O0oo00oO / OOoOoo % Ii
def O0000ooO ( ) :
 O00o0 = O0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 o00oooO0Oo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'Daily' in o000O0O :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 9008 , Ooo )
def O00OoO ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def I11i11 ( url ) :
 O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 O0OoO0ooOO0o ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  O0OoO0ooOO0o ( ( o000O0O ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 68 - 68: o0o00Oo0O * iI11I1II1I1I / OooOO000
def o00O00oO ( ) :
 O00o0 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if '.m3u' in ooO0oOOooOo0 :
   IiIi1iIIi1 ( ( o000O0O ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + ooO0oOOooOo0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def OO000O000OOO ( url ) :
 O00o0 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  O0OoO0ooOO0o ( ( o000O0O ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 26 - 26: oo0oO00 * IIi % oOo0O0Ooo + iiII11i1I1IIi
def O0Oo000 ( ) :
 O00o0 = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  if 'category' in ooO0oOOooOo0 :
   IiIi1iIIi1 ( o000O0O , 'http://www.disclose.tv/' + ooO0oOOooOo0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 38 - 38: iiII11i1I1IIi - I1ii11iIi11i / IIi + O0oOO0 . iiII11i1I1IIi + iIi1i1ii1
   if 19 - 19: IIi
def oo0iIi1iiii1ii ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( O00o0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O00o0 )
 for url , o000O0O , I1111i in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , 'http://www.disclose.tv/' + url , 7011 , I1111i )
 for url in next :
  IiIi1iIIi1 ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
  if 21 - 21: OOooOOo - Ii - OOooOOo
def i1oo0OO0Oo ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( O00o0 )
 ii1iii1i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  if 'http' in url :
   O0OoO0ooOO0o ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , o000O0O in o0O0OOO0Ooo :
  O0OoO0ooOO0o ( o000O0O , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in ii1iii1i :
  O0OoO0ooOO0o ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 4 - 4: OOooOOo * o0o00Oo0O - oo0oO00
  if 72 - 72: oo0oO00 + OOoOoo / oOo0O0Ooo . iIi1i1ii1 % oO0o / Ii
def I1III1I1IiI ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
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
   iII = O0 ( oo0iiIIi1i111i )
   OoOo0Oo00Oo = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iII )
   for o00OO00O0oOO in OoOo0Oo00Oo :
    i11i11I = False
    Resolve ( o00OO00O0oOO )
    if 61 - 61: iI11I1II1I1I % IIi - O0oOO0 * ii % IIiIiII11i - IIi
 elif o0oO0O > 1 :
  if 44 - 44: o0o00Oo0O
  for II1Iii1iI in o00oo00 :
   IIIi1iIii1II11 = O0 ( II1Iii1iI )
   OOOOoOOOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIIi1iIii1II11 )
   iiIi1 = OOOOoOOOO
   iiIi1 = ( str ( iiIi1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iiIi1
   O0OoO0ooOO0o ( 'DOUBLE LINK' , iiIi1 , 424 , '' )
   if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
   for url in OOOOoOOOO :
    IiIi1iIIi1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiIIIIIi = Google . resolve ( url )
    except :
     pass
    try :
     Oo0o0OOo0Oo0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiIIIIIi ) )
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
 IiIi1iIIi1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 85 - 85: ii + ii
 IiIi1iIIi1 ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / oo0oO00 . oO0o
def oOOo0O0Oo ( ) :
 O00o0 = O0 ( 'http://cnfstudio.com/' )
 o00oooO0Oo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , 'http://cnfstudio.com/genre/' + ooO0oOOooOo0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 50 - 50: O0oOO0 * oo0oO00 + Oooo0O0oo00oO - I1ii11iIi11i
iI111I11I1I1 = xbmcgui . Dialog ( )
if 79 - 79: oO0o / ooOoO0O00
iIi1i1I1I = '{UN},' ; i11iiiI = '{IG},' ; o0OOOO0o0o0oo0Oo0 = '{PL},' ; IiIii111iI11i = '{LO},' ; ooo0ooO00o = '{LP},' ; o0OOii = '{HA},' ; IIiiiiiI1iIi = '{XD},' ; IIIII11II1 = '{TA},' ; OOOO0oOO = '{DP},' ; IIIiii = '{JT},' ; I11OoooO = '{JJ},' ; i1IIi11 = '{MM},' ; oOIIIII11 = '{FQ},' ; i1i1 = '{HH},'
if 15 - 15: Ii / I11i / oO0o . OOooOOo % O0oOO0
def iiII1i11 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( O00o0 )
 o0OOO0oo0oOOo = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( O00o0 )
 for I1111i , url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I1111i )
 o0OOO0oo0oOOo = o0OOO0oo0oOOo
 for url in o0OOO0oo0oOOo :
  IiIi1iIIi1 ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 31 - 31: Ii1I / iiII11i1I1IIi + I11i . OooOO000 / o0o00Oo0O . iIi1i1ii1
def iIOoO0O00 ( url ) :
 if 96 - 96: iIi1i1ii1 - iiII11i1I1IIi
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  O0o0O00Oo0o0 = url + '&fv=&sou='
  O0o0O00Oo0o0 = O0o0O00Oo0o0 . replace ( 'player' , 'watch' )
  I11I111i = o0o00 ( O0o0O00Oo0o0 )
  Ii1I1i1IiiI = o0o00 ( url )
  if 37 - 37: oOo0O0Ooo + ii . OooOO000 + oOo0O0Ooo . iIi1i1ii1
  if 44 - 44: OOooOOo . OooOO000 . ooOoO0O00 . OOooOOo * OOoOoo
def o0o00 ( url ) :
 if 59 - 59: IIiIiII11i * ii - ii
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  OO0OoOOO0 ( url )
  if 33 - 33: o0o00Oo0O . Ii % I11i
  if 50 - 50: OOoOoo
def Oooo0O00OOo0o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , OO0o , '' )
 if 4 - 4: O0oOO0 * ii % I1ii11iIi11i / OOoOoo
def II1iiIiI1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  Ii1I11IIi1 = open ( O0OoO000O0OO , 'r' )
  for i111iIi1i1II1 in Ii1I11IIi1 :
   I1ii = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i111iIi1i1II1 )
   for o000O0O , ooO0oOOooOo0 in I1ii :
    O0OoO0ooOO0o ( o000O0O , ooO0oOOooOo0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 25 - 25: ii
def IiIi1I1IiI1II1 ( url ) :
 if os . path . exists ( Remote ) :
  I1 = iIi11i1 ( url )
  o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for o000O0O , url in o00oooO0Oo :
   url = ( url ) . strip ( )
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 21 - 21: ii . o0o00Oo0O / Ii
  if 86 - 86: OOooOOo / Oooo0O0oo00oO
def OOoO00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + ooO0oOOooOo0
 o000O0O = 'plugin.video.GenieTv'
 if 40 - 40: iI11I1II1I1I / OOoOoo / oOo0O0Ooo + Ii1I * Oooo0O0oo00oO
 III1i1iI111I1 ( ooO0oOOooOo0 , o000O0O )
 if 64 - 64: I1ii11iIi11i % OOooOOo . I11i % oOo0O0Ooo / Oooo0O0oo00oO
def i1IiiiI1iI ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooO0oOOooOo0
 o000O0O = 'repository.GenieTv'
 if 74 - 74: iIi1i1ii1 - O0oOO0 * oO0o - OooOO000
 III1i1iI111I1 ( ooO0oOOooOo0 , o000O0O )
 if 81 - 81: I11i % IIi - Ii
 if 34 - 34: IIi - iIi1i1ii1 + OooOO000
def OO ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  OoOO ( )
 if O0oO0 == 1 :
  IioOo0O ( )
  if 40 - 40: iiII11i1I1IIi * iiII11i1I1IIi / I11i
  if 42 - 42: IIi * oOo0O0Ooo - o0o00Oo0O - OOoOoo
  if 22 - 22: iI11I1II1I1I / OOoOoo / oOo0O0Ooo - I11i
  if 21 - 21: O0oOO0 . Ii * oo0oO00 . Oooo0O0oo00oO / Oooo0O0oo00oO
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
Iii1Ii111ii1 = 'https://addons.tvaddons.ag/'
if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + IIi % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def IioOo0O ( ) :
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 I1Ii11i = 'https://addons.tvaddons.ag/search/?keyword=' + I1iii
 I1 = O0 ( I1Ii11i )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , I1iii11 , o000O0O in o00oooO0Oo :
  I1IiiiiI ( o000O0O , ooO0oOOooOo0 , 10054 , 'https://addons.tvaddons.ag/' + I1iii11 , OO0o , '' )
  if 79 - 79: ii + oo0oO00 * OooOO000
  if 63 - 63: OOoOoo % oOo0O0Ooo . Oooo0O0oo00oO - OOoOoo / I1ii11iIi11i % oOo0O0Ooo
def OoOO ( ) :
 I1 = O0 ( Iii1Ii111ii1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  if 'Repositories' in o000O0O :
   pass
  elif 'Services' in o000O0O :
   pass
  elif 'International' in o000O0O :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , ooO0oOOooOo0 , 10053 , 'https://addons.tvaddons.ag/' + I1111i , OO0o , '' )
   if 39 - 39: I11i . ooOoO0O00 % O0oOO0 / oo0oO00 % o0o00Oo0O
   if 100 - 100: OooOO000 - OOooOOo
def Addon ( url ) :
 I1 = O0 ( url )
 oooOoO00O = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  if 'Please' in o000O0O :
   pass
  else :
   o0OIiII ( o000O0O , url , 10054 , 'https://addons.tvaddons.ag/' + I1111i , OO0o , '' )
 for url in oooOoO00O :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
  if 42 - 42: iIi1i1ii1 * iiII11i1I1IIi . Ii1I - iI11I1II1I1I . OOoOoo + oo0oO00
  if 35 - 35: iiII11i1I1IIi . oOo0O0Ooo / IIiIiII11i % iIi1i1ii1
def iiiIiIIiIiiii ( url , name ) :
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
   if 99 - 99: iIi1i1ii1 % OooOO000
def III1i1iI111I1 ( url , name ) :
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
 if 61 - 61: o0o00Oo0O + oOo0O0Ooo / ii * iiII11i1I1IIi / IIiIiII11i / iiII11i1I1IIi
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 56 - 56: iiII11i1I1IIi * Ii1I - IIiIiII11i % Ii1I
 if 30 - 30: Ii % oO0o * IIiIiII11i - o0o00Oo0O . Ii1I * iI11I1II1I1I
def iIiII1 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , I1iii11 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , url , 1007 , I1iii11 )
def iI1Iii1i1 ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , I1iii11 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 1006 , I1iii11 )
  if 87 - 87: Ii * IIiIiII11i - IIi % ii
  if 55 - 55: ooOoO0O00
def iIIiiiI ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , iconimage , ooo0O , II11IiIi11 , name in o00oooO0Oo :
  if 'http' in url :
   if '.php' in url :
    iiiI11 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
    for i111iIi1i1II1 in iiiI11 :
     if i111iIi1i1II1 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oOoO ( name , url , 1016 , iconimage , II11IiIi11 , ooo0O )
   else :
    if 'youtube' in url :
     iiiI11 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for i111iIi1i1II1 in iiiI11 :
      if i111iIi1i1II1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1111iI1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , II11IiIi11 , ooo0O )
    else :
     iiiI11 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for i111iIi1i1II1 in iiiI11 :
      if i111iIi1i1II1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1111iI1 ( name , url , 222 , iconimage , II11IiIi11 , ooo0O )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
  else :
   oOOO0oo0 ( url , iconimage , name )
   if 13 - 13: OOooOOo - oO0o * ii
 else :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
  for url , I1iii11 , name in o00oooO0Oo :
   if 'http' in url :
    if '.php' in url :
     IiIi1iIIi1 ( name , url , 1016 , I1iii11 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      O0OoO0ooOO0o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iii11 )
     else :
      iiiI11 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
      for i111iIi1i1II1 in iiiI11 :
       if i111iIi1i1II1 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      O0OoO0ooOO0o ( name , url , 222 , I1iii11 )
      Iii1I1I11iiI1 ( 'movies' , 'INFO' )
   else :
    oOOO0oo0 ( url , I1iii11 , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 26 - 26: ii
def oOOO0oo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooo0000oo0 = ( url ) . replace ( o0OO00O00oO , 'http' ) . replace ( OO000oooOo000 , '.com' ) ;
 O0oooo000o = ( ooo0000oo0 ) . replace ( I11O0O0o , 'a' ) . replace ( i1Ii1i11ii , 'b' ) . replace ( oO0O0oo , 'c' ) . replace ( IiI1I1II , 'd' ) . replace ( o0OOOO0o0o0oo0Oo0 , 'e' ) . replace ( IIIiii , 'f' ) ;
 IIiIiI11II = ( O0oooo000o ) . replace ( iiIIii111Ii , 'g' ) . replace ( o0OOii , 'h' ) . replace ( o0oO0o0Oo0 , 'i' ) . replace ( i1IiIi1I1i , 'j' ) . replace ( OOOOOOO00OO , 'k' ) . replace ( o0Oo00 , 'l' ) ;
 oOo00 = ( IIiIiI11II ) . replace ( OoooI1iIiii , 'm' ) . replace ( OoOOo0OO0OOoo , 'n' ) . replace ( i1I , 'o' ) . replace ( i1Ii111 , 'p' ) . replace ( OO0o0o0OOoooo , 'q' ) . replace ( oOO00OOOO0o , 'r' ) ;
 oOOOO0o0o0o = ( oOo00 ) . replace ( I1o0o , 's' ) . replace ( oOoO0o , 't' ) . replace ( iI1I11i1IiiI1 , 'u' ) . replace ( ooo000O , 'v' ) . replace ( OoOoOo000Oo0 , 'w' ) . replace ( Oo0ooo0ooo , 'x' ) ;
 I1o00O00oOooo = ( oOOOO0o0o0o ) . replace ( oooii111I1I1I , 'y' ) . replace ( iIIiIi1IiI1 , 'z' ) . replace ( iIi1i1I1I , '.' ) . replace ( i11iiiI , '(' ) . replace ( IiIii111iI11i , ')' ) . replace ( ooo0ooO00o , '/' ) ;
 Oo0O = ( I1o00O00oOooo ) . replace ( Oo0O00OO , '1' ) . replace ( i1II , '2' ) . replace ( Iii1I1III11 , '3' ) . replace ( IIIII11II1 , '4' ) . replace ( OOOO0oOO , '5' ) . replace ( i1I1iiiI , '6' ) ;
 i1ii1IiIiIii = ( Oo0O ) . replace ( I11OoooO , '7' ) . replace ( i1IIi11 , '8' ) . replace ( oOIIIII11 , '9' ) . replace ( i1i1 , '0' ) . replace ( ooOO , ':' ) . replace ( oO0o0 , '%' ) ;
 url = ( i1ii1IiIiIii ) . replace ( ii111Ii1i , '-' ) . replace ( IIiiiiiI1iIi , '_' ) ;
 O0OoO0ooOO0o ( name , url , 222 , iconimage ) ;
 if 55 - 55: OOooOOo . iI11I1II1I1I * Oooo0O0oo00oO % iI11I1II1I1I . oO0o
 if 43 - 43: IIi . Oooo0O0oo00oO + oOo0O0Ooo * Ii
def ii1ii11Ii ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , I1iii11 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 1007 , I1iii11 )
def I1III11i11Iii ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , I1iii11 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 1006 , I1iii11 )
  if 16 - 16: Oooo0O0oo00oO . IIiIiII11i - IIi - ii
def ooOoOoOoo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 i1I1i111Ii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 i1I1i111Ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I1i111Ii )
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
def iIi ( url ) :
 O00o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00o0 )
 for url , I1111i , o000O0O in o00oooO0Oo :
  if '-dir-' in o000O0O :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , I1111i )
  else :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' , url , 1006 , I1111i )
   if 33 - 33: iiII11i1I1IIi + I1ii11iIi11i % oo0oO00 . O0oOO0
def i1II1i ( url ) :
 O00o0 = iIi11i1 ( url )
 O0oooooO0oOOo = ( 'http://afewbitsmore.com/' )
 o00oooO0Oo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if '[To Parent Directory]' in o000O0O :
   o000O0O = 'HOME'
   pass
  elif 'HOME' in o000O0O :
   pass
  elif '.m3u' in o000O0O :
   IiIi1iIIi1 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , O0oooooO0oOOo + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in o000O0O :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , O0oooooO0oOOo + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in o000O0O :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , O0oooooO0oOOo + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) , O0oooooO0oOOo + url , 1012 , oOOOo00O00oOo + 'music.png' )
def oo0O0OO0Oooo ( url ) :
 I1 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for I1111i , o000O0O , url in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 7 - 7: IIiIiII11i - Ii1I / oo0oO00 % ii + ooOoO0O00
def I1Iii1 ( url ) :
 O00o0 = iIi11i1 ( url )
 O0oooooO0oOOo = url
 o00oooO0Oo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  if '.mp3' in o000O0O :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIi1iIIi1 ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '/' , '' ) , O0oooooO0oOOo + url , 1011 , oOOOo00O00oOo + 'music.png' )
def Ii1II111iIi ( ) :
 O00o0 = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O00o0 )
 for ooO0oOOooOo0 , I1111i , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ( 'http://www.cyn.net/music/' + ooO0oOOooOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I1111i ) . replace ( ' ' , '%20' ) )
def oo00ooOOoo ( url , img ) :
 O00o0 = iIi11i1 ( url )
 IiIIIIIi = url
 img = img
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( IiIIIIIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 58 - 58: OooOO000 - oo0oO00 % Ii1I + ii - OOoOoo
def I1IiI1iI11 ( url ) :
 O00o0 = iIi11i1 ( url )
 IiIIIIIi = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( O00o0 )
 for type , url , o000O0O in o00oooO0Oo :
  if '[VID]' in type :
   O0OoO0ooOO0o ( ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , IiIIIIIi + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   I1IiI1iI11 ( IiIIIIIi + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: iiII11i1I1IIi + Oooo0O0oo00oO . Oooo0O0oo00oO . iIi1i1ii1 . OooOO000 / ooOoO0O00
 if 77 - 77: IIiIiII11i % oo0oO00 / I1ii11iIi11i
def iiO0O0o0oO0O00 ( ) :
 iiII1 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1i11II = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1iii = I1i11II . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiIIIIIi = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 O00ooOo = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 23 - 23: iI11I1II1I1I
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( IiIIIIIi )
 Iiii = Oo0OoO00oOO0o ( O00ooOo )
 if 10 - 10: oo0oO00 - I11i % ii - Ii1I
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for o000O0O in o00oooO0Oo :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( o000O0O + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooO0oOOooOo0 + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 64 - 64: oO0o / oOo0O0Ooo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for o000O0O in o0O0OOO0Ooo :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( o000O0O + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIIIIIi + o000O0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 23 - 23: oo0oO00 * OooOO000 * I11i - oOo0O0Ooo % OOooOOo + I11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  ii1iii1i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for o000O0O in ii1iii1i :
   if I1i11II in o000O0O . lower ( ) :
    IiIi1iIIi1 ( ( o000O0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O00ooOo + o000O0O ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 41 - 41: iIi1i1ii1 * ii . OOoOoo % Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: iI11I1II1I1I . OooOO000 - I1ii11iIi11i / oo0oO00 + IIiIiII11i
    if 29 - 29: oo0oO00 . Ii + ooOoO0O00 - IIi + o0o00Oo0O . oOo0O0Ooo
    if 8 - 8: I11i
    if 78 - 78: ooOoO0O00 - I1ii11iIi11i
    if 48 - 48: IIi - ii + OooOO000 % I11i - OOooOOo . oOo0O0Ooo
    if 42 - 42: OooOO000
OoooI1iIiii = '{SF},' ; OoOOo0OO0OOoo = '{IF},' ; i1I = '{PW},' ; Iii1I1III11 = '{AM},' ; i1Ii111 = '{GF},' ; OO0o0o0OOoooo = '{DD},' ; oOO00OOOO0o = '{UO},' ; I1o0o = '{LE},' ; iI1I11i1IiiI1 = '{ZY},' ; ooo000O = '{UE},' ; OoOoOo000Oo0 = '{PE},' ; Oo0ooo0ooo = '{JE},' ; oooii111I1I1I = '{TH},' ; iIIiIi1IiI1 = '{LK},'
if 70 - 70: I11i / oo0oO00 + O0oOO0 % oOo0O0Ooo % I1ii11iIi11i + oO0o
if 80 - 80: Oooo0O0oo00oO
def iiIi1i ( ) :
 O00o0 = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 o00oooO0Oo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def iiii1IiI1i1 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( O00o0 )
 for url , o000O0O , o0Oo0oO in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O + o0Oo0oO , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def ii1iii1 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IiII1II1 ( url )
def IiII1II1 ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( O00o0 )
 o0O0OOO0Ooo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( O00o0 )
 ii1iii1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( 'VidSpot - ' + o000O0O , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in o0O0OOO0Ooo :
  O0OoO0ooOO0o ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for o000O0O , url in ii1iii1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0OoO0ooOO0o ( 'TheVideo - ' + o000O0O , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / OOoOoo % oOo0O0Ooo % ooOoO0O00
def OOOoOOooO0 ( ) :
 O00o0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o00oooO0Oo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 2 - 2: OOoOoo - o0o00Oo0O - Ii1I / oo0oO00 * OOooOOo
  if 26 - 26: Ii1I + OooOO000 - O0oOO0 + iIi1i1ii1 % Oooo0O0oo00oO
def O0000oOo0OO ( ) :
 O00o0 = O0 ( 'http://www.animetoon.org/cartoon' )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( O00o0 )
 for ooO0oOOooOo0 , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , ooO0oOOooOo0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 57 - 57: Ii1I
  if 30 - 30: Ii1I * iIi1i1ii1 % iIi1i1ii1 * iiII11i1I1IIi . iiII11i1I1IIi
  if 23 - 23: oO0o % OOoOoo - O0oOO0 . Ii1I . ii
def o0OooO0 ( url ) :
 O00o0 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O00o0 )
 for I1111i in o0O0OOO0Ooo :
  II1i = I1111i
 ii1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( O00o0 )
 for url in ii1iii1i :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( O00o0 )
 for url , o000O0O in o00oooO0Oo :
  IiIi1iIIi1 ( o000O0O , url , 1003 , II1i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1I1 ( url , IMAGE ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( O00o0 )
 for o000O0O , url in o00oooO0Oo :
  print o000O0O + '     ' + url
  if 'easy' in url :
   Oo0ooOOO ( url )
  elif 'playpanda' in url :
   Oo0ooOOO ( url )
   if 99 - 99: oO0o - iiII11i1I1IIi . oO0o % I11i % Oooo0O0oo00oO . o0o00Oo0O
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0ooOOO ( url ) :
 O00o0 = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( O00o0 )
 for url in o00oooO0Oo :
  O0OoO0ooOO0o ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 56 - 56: O0oOO0 + ooOoO0O00 * iiII11i1I1IIi - o0o00Oo0O
  if 84 - 84: iiII11i1I1IIi % oOo0O0Ooo / iI11I1II1I1I * IIi * iI11I1II1I1I + Ii1I
def O000o ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOO00O . add_header ( 'referer' , url )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 76 - 76: Oooo0O0oo00oO
def iIi11i1 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 52 - 52: I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
def i11i1IiIi ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooo0oO0oOo = ( '%s%s' % ( O0OOOO0000O , url ) )
 O0o0O00Oo0o0 = iIi11i1 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , I1iii11 , o000O0O in o00oooO0Oo :
  O0OoO0ooOO0o ( '%s' % ( '[COLOR' + iiI1IiI + ']' + o000O0O + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1iii11 )
  if 63 - 63: oo0oO00
def OO0OoOOO0 ( url ) :
 if 6 - 6: O0oOO0 / Ii1I / oO0o
 iiiiIIii1I = open ( I11i1I1I , "a" )
 iiiiIIii1I . write ( 'url="' + url + '"\n' )
 iiiiIIii1I . close
 if 14 - 14: Oooo0O0oo00oO * oOo0O0Ooo - Ii1I
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( o000O0O ) )
 oO0O = xbmc . Player ( oOO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO0O . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 10 - 10: iiII11i1I1IIi % OooOO000 * Ii1I * o0o00Oo0O * Ii % OooOO000
def ooOoo0O0o0OO0 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % o000O0O )
 xbmc . sleep ( 1 )
 oO0O = xbmc . Player ( oOO ( ) )
 o0oOoO00o . update ( 100 , '%s' % o000O0O )
 xbmc . sleep ( 1 )
 oO0O . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 47 - 47: OooOO000 * Oooo0O0oo00oO
def Ii1IIiI1i ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 8 - 8: I1ii11iIi11i
def i1iII1IiI1I ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 IiIi1ii1Ii = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0O . play ( IiIi1ii1Ii )
 xbmc . sleep ( 1 )
 oO0O . play ( url )
 if 6 - 6: iiII11i1I1IIi % I11i + OooOO000
 if 91 - 91: I11i + o0o00Oo0O * O0oOO0 * iIi1i1ii1 * Ii1I
def oOO ( ) :
 try :
  oO0oO0OoO00 = getSet ( "core-player" )
  if ( oO0oO0OoO00 == 'DVDPLAYER' ) : Oo0ooo00o0O0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oO0oO0OoO00 == 'MPLAYER' ) : Oo0ooo00o0O0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( oO0oO0OoO00 == 'PAPLAYER' ) : Oo0ooo00o0O0 = xbmc . PLAYER_CORE_PAPLAYER
  else : Oo0ooo00o0O0 = xbmc . PLAYER_CORE_AUTO
 except : Oo0ooo00o0O0 = xbmc . PLAYER_CORE_AUTO
 return Oo0ooo00o0O0
 return True
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * IIi + iI11I1II1I1I
def IiIi1iIIi1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 80 - 80: I11i . iiII11i1I1IIi . ii
def Oo0O0000Oo00o ( name , url , mode , iconimage , fanart , description ) :
 if 63 - 63: OOoOoo . Oooo0O0oo00oO
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 66 - 66: oOo0O0Ooo
def O0OoO0ooOO0o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 99 - 99: oO0o % o0o00Oo0O . OooOO000 - Ii1I . I1ii11iIi11i / OOooOOo
 if 60 - 60: Ii1I
 if 78 - 78: O0oOO0 + IIiIiII11i
 if 55 - 55: ii
 if 90 - 90: oOo0O0Ooo
 if 4 - 4: Oooo0O0oo00oO % OOoOoo - Oooo0O0oo00oO - I11i
def OOOiiiiI ( heading , announce ) :
 class iI1IIIiIII11 ( ) :
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
   try : oOOo0O00o = open ( announce ) ; OoO0o000oOo = oOOo0O00o . read ( )
   except : OoO0o000oOo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OoO0o000oOo ) )
   return
 iI1IIIiIII11 ( )
 iI1IIIiIII11 ( )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
def OOI1iI1ii1II ( ) :
 OOOiiiiI ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 20 - 20: Ii - IIiIiII11i - OOoOoo % O0oOO0 . OOoOoo
 if 50 - 50: iI11I1II1I1I + OooOO000 - oo0oO00 - ii
 if 84 - 84: OOooOOo - oo0oO00
 if 80 - 80: Ii % Oooo0O0oo00oO - I1ii11iIi11i % Oooo0O0oo00oO
 if 89 - 89: IIi * oo0oO00 + OOooOOo / Ii
def o00O0 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 68 - 68: ii * oo0oO00
 if 86 - 86: I11i / OOooOOo
 if 40 - 40: iiII11i1I1IIi
 if 62 - 62: OOoOoo / Oooo0O0oo00oO
 if 74 - 74: iiII11i1I1IIi % OooOO000 / OooOO000 - iI11I1II1I1I - IIiIiII11i + Oooo0O0oo00oO
 if 92 - 92: oo0oO00 % OooOO000
 if 18 - 18: OOoOoo + OooOO000 / Oooo0O0oo00oO / O0oOO0 + iI11I1II1I1I % iIi1i1ii1
 if 94 - 94: oo0oO00
 if 37 - 37: O0oOO0
 if 52 - 52: Ii1I * oOo0O0Ooo . Oooo0O0oo00oO + ooOoO0O00 % O0oOO0 / iI11I1II1I1I
 if 68 - 68: OooOO000 - OOooOOo . Ii + I11i
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
 if 33 - 33: oo0oO00 . I1ii11iIi11i
 if 89 - 89: iiII11i1I1IIi + ooOoO0O00 - iIi1i1ii1 + OOoOoo . IIiIiII11i
 if 85 - 85: iI11I1II1I1I - IIi * I1ii11iIi11i . O0oOO0 + OooOO000
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . iiII11i1I1IIi / iiII11i1I1IIi
 if 43 - 43: oOo0O0Ooo
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + IIi * oo0oO00 / O0oOO0
 if 18 - 18: OOoOoo
 if 92 - 92: oO0o % iI11I1II1I1I / iIi1i1ii1 * iiII11i1I1IIi . ooOoO0O00 + O0oOO0
 if 24 - 24: iIi1i1ii1 . iiII11i1I1IIi * iIi1i1ii1 % Ii . Ii + ooOoO0O00
 if 64 - 64: iI11I1II1I1I / iIi1i1ii1 / I1ii11iIi11i - Ii1I
def o00oOOO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OoOOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 53 - 53: I11i / oo0oO00 % o0o00Oo0O / iI11I1II1I1I / iiII11i1I1IIi
def iIiii1Ii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iiI11Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 37 - 37: I1ii11iIi11i + OooOO000 * O0oOO0 / I11i
def O0O0OOo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ii1i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 66 - 66: OooOO000 * ii / Ii1I - oo0oO00 - OOoOoo * oo0oO00
def OOoOooO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 49 - 49: iIi1i1ii1 % iiII11i1I1IIi / OooOO000 / Ii1I
def i1I1iI11Iii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i1IIi1iII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 15 - 15: o0o00Oo0O % I1ii11iIi11i % iIi1i1ii1 % ii - iIi1i1ii1
def I11IIIIi1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ooOOo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 77 - 77: oOo0O0Ooo / OooOO000
def OOoo0oo000oo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOOooOO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 20 - 20: oO0o
def ii1iiiiii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOOoO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 12 - 12: ii . oo0oO00 . oO0o
def O00oO0oOOOOOO ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + Oo0ooo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 42 , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 1 - 1: ii * iI11I1II1I1I / Ii1I * oo0oO00
def Ii1I1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i1I1i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for o000O0O , url , oo0 , II11IiIi11 , I11o0oO00oO0o0o0 in o00oooO0Oo :
  I1IiiiiI ( o000O0O , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , I11o0oO00oO0o0o0 )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
 if 43 - 43: I1ii11iIi11i / OooOO000 / ooOoO0O00
 if 3 - 3: IIi * OOoOoo . oO0o * ii + OOooOOo / o0o00Oo0O
 if 60 - 60: oo0oO00
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
 if 66 - 66: IIiIiII11i + iiII11i1I1IIi * O0oOO0 % oo0oO00 / ooOoO0O00 / iI11I1II1I1I
 if 62 - 62: OOooOOo + O0oOO0 * iIi1i1ii1 + o0o00Oo0O / Oooo0O0oo00oO + OOoOoo
 if 38 - 38: ooOoO0O00 / iI11I1II1I1I + iiII11i1I1IIi
 if 26 - 26: Ii1I . IIi % I11i
def OoO0oo ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( O00o0OO ) :
     i1IiI1iiIII1 = 0
     i1IiI1iiIII1 += len ( Oo00OO0 )
     if i1IiI1iiIII1 > 0 :
      for oOOo0O00o in Oo00OO0 :
       os . unlink ( os . path . join ( O0O000O , oOOo0O00o ) )
  oo0OooOoOo = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( oo0OooOoOo )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 8 - 8: iIi1i1ii1
 if 37 - 37: oOo0O0Ooo / ii % Ii % Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
 if 1 - 1: iIi1i1ii1 % ooOoO0O00
 if 41 - 41: oO0o * oO0o / iiII11i1I1IIi + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / IIi
 if 80 - 80: Ii1I
 if 67 - 67: IIiIiII11i
def I1II1III1 ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 2 - 2: I11i - o0o00Oo0O * IIi % iIi1i1ii1
def O0ooO0Oo00o ( url ) :
 ooooOO0o000OO = os . path . join ( oO , 'addon_data' )
 OoO00OOoO = [
 ( ooooOO0o000OO ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( ooooOO0o000OO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( ooooOO0o000OO , 'plugin.video.itv' , 'Images' ) ) ]
 if 39 - 39: ooOoO0O00
 iiiiii1 = 0
 if 97 - 97: Ii1I - OOoOoo * Ii + OooOO000 % ii
 for i111iIi1i1II1 in OoO00OOoO :
  if os . path . exists ( i111iIi1i1II1 ) and not i111iIi1i1II1 in [ oOo0oooo00o , ooooOO0o000OO ] :
   for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( i111iIi1i1II1 ) :
    i1IiI1iiIII1 = 0
    i1IiI1iiIII1 += len ( Oo00OO0 )
    if i1IiI1iiIII1 > 0 :
     for oOOo0O00o in Oo00OO0 :
      if not oOOo0O00o in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( O0O000O , oOOo0O00o ) )
       except :
        pass
      else : ii1 ( 'Ignore Log File: %s' % oOOo0O00o )
     for oO00OoOOOo in I11Ii111I :
      try :
       shutil . rmtree ( os . path . join ( O0O000O , oO00OoOOOo ) )
       iiiiii1 += 1
       ii1 ( "[Success] cleared %s files from %s" % ( str ( i1IiI1iiIII1 ) , os . path . join ( i111iIi1i1II1 , oO00OoOOOo ) ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( i111iIi1i1II1 , oO00OoOOOo ) )
  else :
   for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( i111iIi1i1II1 ) :
    for oO00OoOOOo in I11Ii111I :
     if 'cache' in oO00OoOOOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( O0O000O , oO00OoOOOo ) )
       iiiiii1 += 1
       ii1 ( "[Success] wiped %s " % os . path . join ( i111iIi1i1II1 , oO00OoOOOo ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( i111iIi1i1II1 , oO00OoOOOo ) )
       if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . Oooo0O0oo00oO
 I1II1III1 ( oo0o0O00 , 'Clear Cache: Removed %s Files' % iiiiii1 )
 if 3 - 3: o0o00Oo0O - OooOO000 * IIi * Oooo0O0oo00oO / IIi
 if 58 - 58: IIi * iI11I1II1I1I + OOoOoo . OOoOoo
 if 74 - 74: OOoOoo - I11i * iIi1i1ii1 % OOoOoo
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * OooOO000 - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . O0oOO0 . ii . Oooo0O0oo00oO * Ii1I
def I1Ii11II1I1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0o0O00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( O0o0O00 ) :
   i1IiI1iiIII1 = 0
   i1IiI1iiIII1 += len ( Oo00OO0 )
   if 85 - 85: Ii . oo0oO00 + IIi / IIi
   if 43 - 43: iIi1i1ii1 . ii - IIiIiII11i
   if i1IiI1iiIII1 > 0 :
    if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * Oooo0O0oo00oO * O0oOO0
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( i1IiI1iiIII1 ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OooOO000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
     for oOOo0O00o in Oo00OO0 :
      os . unlink ( os . path . join ( O0O000O , oOOo0O00o ) )
     for oO00OoOOOo in I11Ii111I :
      shutil . rmtree ( os . path . join ( O0O000O , oO00OoOOOo ) )
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
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
 if 15 - 15: IIi + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
 if 54 - 54: iIi1i1ii1 - IIiIiII11i . OOoOoo + IIi
 if 45 - 45: O0oOO0 + IIiIiII11i . iiII11i1I1IIi / Ii1I
 if 76 - 76: IIi + iiII11i1I1IIi - iIi1i1ii1 * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: OOoOoo + IIiIiII11i . o0o00Oo0O - iiII11i1I1IIi / ii . OooOO000
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
 if 29 - 29: Ii1I
def OO0Oooo0oOO0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0o0O00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( O0o0O00 ) :
   i1IiI1iiIII1 = 0
   i1IiI1iiIII1 += len ( Oo00OO0 )
   if 41 - 41: IIi
   if 49 - 49: IIi % IIiIiII11i . IIi - I11i - oo0oO00 * iIi1i1ii1
   if i1IiI1iiIII1 > 0 :
    if 47 - 47: o0o00Oo0O . I11i / IIi * iiII11i1I1IIi
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( i1IiI1iiIII1 ) + " files found" , "Do you want to delete them?" ) :
     if 63 - 63: OooOO000 - O0oOO0 - iiII11i1I1IIi - OOoOoo / O0oOO0 + oO0o
     for oOOo0O00o in Oo00OO0 :
      os . unlink ( os . path . join ( O0O000O , oOOo0O00o ) )
     for oO00OoOOOo in I11Ii111I :
      shutil . rmtree ( os . path . join ( O0O000O , oO00OoOOOo ) )
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
 if 94 - 94: iIi1i1ii1 / oOo0O0Ooo . IIiIiII11i
 if 32 - 32: O0oOO0 . Oooo0O0oo00oO % Oooo0O0oo00oO . OOooOOo
 if 37 - 37: Oooo0O0oo00oO + o0o00Oo0O + Oooo0O0oo00oO . iiII11i1I1IIi . I11i
 if 78 - 78: oOo0O0Ooo / oo0oO00 + I11i . I1ii11iIi11i / o0o00Oo0O
 if 49 - 49: Ii1I
 if 66 - 66: I11i . Ii1I
 if 18 - 18: I1ii11iIi11i + iIi1i1ii1
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % IIi . oOo0O0Ooo
 if 43 - 43: oOo0O0Ooo % Ii1I * IIi
 if 31 - 31: IIi / iiII11i1I1IIi
def iI1111iI1iII ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0ooo0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 o0OO0OOoo0oO = os . path . join ( oOooO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( o0OO0OOoo0oO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0ooo0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
   try :
    os . remove ( o0ooo0 )
    print '=== GenieTv - REMOVING    ' + str ( o0ooo0 ) + '    ==='
   except :
    pass
   O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
   o0o00oO0oo000 = open ( o0ooo0 , "w" )
   o0o00oO0oo000 . write ( O0o0O00Oo0o0 )
   o0o00oO0oo000 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0ooo0 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0ooo0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
  try :
   os . remove ( o0ooo0 )
   print '=== GenieTv - REMOVING    ' + str ( o0ooo0 ) + '    ==='
  except :
   pass
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  o0o00oO0oo000 = open ( o0ooo0 , "w" )
  o0o00oO0oo000 . write ( O0o0O00Oo0o0 )
  o0o00oO0oo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0ooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 98 - 98: I11i * I1ii11iIi11i - IIi . OOoOoo
def iI11i1iI ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0ooo0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  o0o00oO0oo000 = open ( o0ooo0 ) . read ( )
  if 'zero' in o0o00oO0oo000 :
   name = '0CACHE'
  elif 'tuxen' in o0o00oO0oo000 :
   name = 'TUXENS'
  elif 'muckys' in o0o00oO0oo000 :
   name = 'MUCKYS'
  elif 'p2p1' in o0o00oO0oo000 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in o0o00oO0oo000 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in o0o00oO0oo000 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 95 - 95: Ii % oO0o % OOoOoo
def i1iOO ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0ooo0 = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  os . remove ( o0ooo0 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0ooo0 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 23 - 23: ooOoO0O00 + Ii1I + IIi + Ii1I . OOoOoo
 if 64 - 64: I11i / iI11I1II1I1I / Ii1I
 if 76 - 76: I1ii11iIi11i * OOoOoo % Oooo0O0oo00oO . oO0o
 if 31 - 31: oOo0O0Ooo - ii . iIi1i1ii1
 if 12 - 12: oo0oO00 . IIi + oo0oO00 - Oooo0O0oo00oO * iiII11i1I1IIi - o0o00Oo0O
 if 44 - 44: ooOoO0O00 % O0oOO0 / OOooOOo % iIi1i1ii1 . Ii1I
 if 38 - 38: OOooOOo . oo0oO00
 if 66 - 66: iiII11i1I1IIi
 if 61 - 61: Ii / O0oOO0 / Ii
 if 61 - 61: oo0oO00 / iI11I1II1I1I - ooOoO0O00 - iIi1i1ii1 * Ii
def IiI1iI1IiiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o00oooO0Oo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for O0O0OOo00Oo , IiI1iIIiIi1Ii , O0oOoOOO000 , oOo00o0oO in o00oooO0Oo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O0O0OOo00Oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0oOoOOO000 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oOo00o0oO )
  inc = inc + 1
  if 14 - 14: oO0o / I1ii11iIi11i . Ii
  if 9 - 9: oo0oO00 - IIiIiII11i + OooOO000 / O0oOO0 % Ii1I
  if 17 - 17: iI11I1II1I1I - OOoOoo
  if 99 - 99: I1ii11iIi11i + OooOO000 % OOoOoo - I11i
  if 52 - 52: Ii1I
  if 93 - 93: iiII11i1I1IIi . Ii
  if 24 - 24: Oooo0O0oo00oO . oO0o + OooOO000 . O0oOO0 - Ii1I % iiII11i1I1IIi
  if 49 - 49: o0o00Oo0O . I1ii11iIi11i / IIi
  if 29 - 29: Ii1I / O0oOO0 * o0o00Oo0O - Ii - oO0o + IIi
def Oo0OOo ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0ooo0 = os . path . join ( oOooO0 , 'addons2.ini' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  o0o00oO0oo000 = open ( o0ooo0 , "w" )
  o0o00oO0oo000 . write ( O0o0O00Oo0o0 )
  o0o00oO0oo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0ooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 78 - 78: iiII11i1I1IIi
def i111II ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0ooo0 = os . path . join ( oOooO0 , 'settings.xml' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  o0o00oO0oo000 = open ( o0ooo0 , "w" )
  o0o00oO0oo000 . write ( O0o0O00Oo0o0 )
  o0o00oO0oo000 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0ooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 8 - 8: Oooo0O0oo00oO
 if 44 - 44: oO0o % Ii . OooOO000 - o0o00Oo0O / iiII11i1I1IIi . OOoOoo
def iIiI1I1IIi1 ( ) :
 try :
  oooOOOoO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oooOOOoO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOOOoO0O = os . path . join ( oooOOOoO , "source.db" )
    os . unlink ( OOOOoO0O )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 79 - 79: Ii
 if 81 - 81: iiII11i1I1IIi + iIi1i1ii1 - Ii
 if 60 - 60: OooOO000
 if 14 - 14: I1ii11iIi11i % O0oOO0 * iiII11i1I1IIi - Ii / Ii1I * Ii
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * oo0oO00 + Oooo0O0oo00oO
def O0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 14 - 14: IIi - o0o00Oo0O
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
 if 45 - 45: OooOO000 * oo0oO00 / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
 if 49 - 49: IIi / iiII11i1I1IIi . iiII11i1I1IIi . iiII11i1I1IIi + Ii % oo0oO00
 if 7 - 7: iIi1i1ii1 * OOoOoo + OOooOOo
 if 22 - 22: iiII11i1I1IIi
 if 48 - 48: Ii1I . oOo0O0Ooo
def oO00ooooO0o ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OoOo00ooOO000 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OoOo00ooOO000 :
  iIOoO0O00o0ooo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; iIOoO0O00o0ooo0 = xbmc . translatePath ( iIOoO0O00o0ooo0 ) ;
  o0oOoooOoo0 = os . path . join ( iIOoO0O00o0ooo0 , ".." , ".." ) ; o0oOoooOoo0 = os . path . abspath ( o0oOoooOoo0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o0oOoooOoo0 ) ; IiI1Iii1iIIII = False
  try :
   for O0O000O , I11Ii111I , Oo00OO0 in os . walk ( o0oOoooOoo0 , topdown = True ) :
    I11Ii111I [ : ] = [ oO00OoOOOo for oO00OoOOOo in I11Ii111I if oO00OoOOOo not in o0oO0 ]
    for o000O0O in Oo00OO0 :
     try : os . remove ( os . path . join ( O0O000O , o000O0O ) )
     except :
      if o000O0O not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiI1Iii1iIIII = True
      plugintools . log ( "Error removing " + O0O000O + " " + o000O0O )
    for o000O0O in I11Ii111I :
     try : os . rmdir ( os . path . join ( O0O000O , o000O0O ) )
     except :
      if o000O0O not in [ "Database" , "userdata" ] : IiI1Iii1iIIII = True
      plugintools . log ( "Error removing " + O0O000O + " " + o000O0O )
   if not IiI1Iii1iIIII : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iiI1Ii11II1I ( )
 if 87 - 87: IIiIiII11i . IIi * oO0o
 if 74 - 74: I11i % OOooOOo . iiII11i1I1IIi % OooOO000 . o0o00Oo0O % IIiIiII11i
 if 5 - 5: O0oOO0 - ii / OOooOOo
def I1II1i1iIIi ( ) :
 ooO0000 = [ ]
 Ooo00O0OooOOO = sys . argv [ 2 ]
 if len ( Ooo00O0OooOOO ) >= 2 :
  oo0o = sys . argv [ 2 ]
  iIIIIi = oo0o . replace ( '?' , '' )
  if ( oo0o [ len ( oo0o ) - 1 ] == '/' ) :
   oo0o = oo0o [ 0 : len ( oo0o ) - 2 ]
  IIi1iI11I = iIIIIi . split ( '&' )
  ooO0000 = { }
  for III1IiiIiiI1i in range ( len ( IIi1iI11I ) ) :
   OooO0o = { }
   OooO0o = IIi1iI11I [ III1IiiIiiI1i ] . split ( '=' )
   if ( len ( OooO0o ) ) == 2 :
    ooO0000 [ OooO0o [ 0 ] ] = OooO0o [ 1 ]
    if 33 - 33: Oooo0O0oo00oO * o0o00Oo0O
 return ooO0000
 if 71 - 71: oo0oO00 . I1ii11iIi11i
I1iiiiiIi1I1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1I1I1i1i1i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1iii1i11I1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
Iii1I111I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OoO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OOOoo0ooO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OoOOOo0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Oo0OoO00OO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iiI11Ii1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
ii1i111 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OOoO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1IIi1iII1i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
ooOOo000 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OOOooOO0oO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
OOOoO0o = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
Oo0ooo00OoO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1i1Ii11Ii = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
oO000OO0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i11iIIi = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O0OOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iI1IIi1IiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1i1I1i1Ii = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O0OOOO0000O = base64 . decodestring ( 'Q1VOVA==' )
def I1IiiiiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 96 - 96: ooOoO0O00 % Ii1I + iI11I1II1I1I
def o0OIiII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 37 - 37: o0o00Oo0O
 if 97 - 97: O0oOO0 - oO0o + iiII11i1I1IIi * o0o00Oo0O
oo0o = I1II1i1iIIi ( )
ooO0oOOooOo0 = None
o000O0O = None
O0ooo0 = None
oo0 = None
II11IiIi11 = None
I11o0oO00oO0o0o0 = None
Oo0oOo0 = None
OOoO0OooO = None
if 38 - 38: oOo0O0Ooo . O0oOO0 / o0o00Oo0O % I1ii11iIi11i / iIi1i1ii1 / ii
if 11 - 11: o0o00Oo0O / OooOO000 / iI11I1II1I1I % IIi
try :
 OOoO0OooO = int ( oo0o [ "fav_mode" ] )
except :
 pass
 if 31 - 31: oo0oO00 . Ii . oO0o * I1ii11iIi11i % IIi . I11i
try :
 ooO0oOOooOo0 = urllib . unquote_plus ( oo0o [ "url" ] )
except :
 pass
try :
 o000O0O = urllib . unquote_plus ( oo0o [ "name" ] )
except :
 pass
try :
 oo0 = urllib . unquote_plus ( oo0o [ "iconimage" ] )
except :
 pass
try :
 O0ooo0 = int ( oo0o [ "mode" ] )
except :
 pass
try :
 II11IiIi11 = urllib . unquote_plus ( oo0o [ "fanart" ] )
except :
 pass
try :
 I11o0oO00oO0o0o0 = urllib . unquote_plus ( oo0o [ "description" ] )
except :
 pass
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 if 93 - 93: OOoOoo % OooOO000
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O0ooo0 )
print "URL: " + str ( ooO0oOOooOo0 )
print "Name: " + str ( o000O0O )
print "IconImage: " + str ( oo0 )
if 46 - 46: Ii1I * OOooOOo * iIi1i1ii1 * Ii1I . Ii1I
if 43 - 43: OOoOoo . ooOoO0O00
def Iii1I1I11iiI1 ( content , viewType ) :
 if 68 - 68: iIi1i1ii1 % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 45 - 45: oOo0O0Ooo
if oo0 == None : oo0 = Ooo
if II11IiIi11 == None : II11IiIi11 = OO0o
if O0ooo0 == None :
 oo0OOo0 ( )
 if 17 - 17: ii - OOoOoo + IIi . ii % I1ii11iIi11i
elif O0ooo0 == 1 :
 iiIi1iiI1I ( ooO0oOOooOo0 )
 if 92 - 92: OooOO000 - Oooo0O0oo00oO % oO0o - I11i % ooOoO0O00
elif O0ooo0 == 44 :
 o0oO0oooOoo ( ooO0oOOooOo0 )
 if 38 - 38: Ii1I . oo0oO00 / OOooOOo % oo0oO00
elif O0ooo0 == 2 :
 oO00O ( )
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / iiII11i1I1IIi
elif O0ooo0 == 3 :
 iIiIi1iI11iiI ( )
 if 61 - 61: I1ii11iIi11i - OooOO000
elif O0ooo0 == 21 :
 i1i1II ( )
 if 51 - 51: iiII11i1I1IIi * OOoOoo / o0o00Oo0O / o0o00Oo0O
elif O0ooo0 == 4 :
 O0Oo0 ( )
 if 52 - 52: ii % o0o00Oo0O
elif O0ooo0 == 5 :
 II11Ii111II1 ( ooO0oOOooOo0 )
 if 56 - 56: O0oOO0 - ooOoO0O00 * ii - IIiIiII11i
elif O0ooo0 == 6 :
 I1Ii11II1I1 ( ooO0oOOooOo0 )
 if 28 - 28: ooOoO0O00 / oo0oO00 . I11i
elif O0ooo0 == 7 :
 iI1111iI1iII ( ooO0oOOooOo0 , o000O0O )
 if 11 - 11: I1ii11iIi11i * ii - Ii
elif O0ooo0 == 8 :
 iI11i1iI ( ooO0oOOooOo0 , o000O0O )
 if 13 - 13: Ii . o0o00Oo0O / Oooo0O0oo00oO * ooOoO0O00
elif O0ooo0 == 9 :
 FIXREPOSADDONS ( ooO0oOOooOo0 )
 if 14 - 14: iIi1i1ii1 + iIi1i1ii1 . oo0oO00 / IIi . iI11I1II1I1I
elif O0ooo0 == 10 :
 o00O0 ( )
 if 10 - 10: IIiIiII11i . Oooo0O0oo00oO / iiII11i1I1IIi
elif O0ooo0 == 11 :
 i1iOO ( ooO0oOOooOo0 )
 if 35 - 35: iiII11i1I1IIi / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif O0ooo0 == 12 :
 IiI1iI1IiiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 3 - 3: Ii1I
elif O0ooo0 == 13 :
 OoO0oo ( )
 if 42 - 42: oo0oO00 % I1ii11iIi11i + iIi1i1ii1 - oo0oO00 . iI11I1II1I1I - IIi
elif O0ooo0 == 14 :
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if 27 - 27: iiII11i1I1IIi % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif O0ooo0 == 15 :
 OOiI1 ( )
 if 37 - 37: iiII11i1I1IIi + OooOO000 * IIi + iIi1i1ii1
elif O0ooo0 == 16 :
 Oo0OOo ( ooO0oOOooOo0 , o000O0O )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + IIi / IIiIiII11i
elif O0ooo0 == 17 :
 i111II ( ooO0oOOooOo0 , o000O0O )
 if 66 - 66: OOoOoo + O0oOO0 % ii
elif O0ooo0 == 18 :
 iIiI1I1IIi1 ( )
 if 23 - 23: O0oOO0 . OOooOOo + iI11I1II1I1I
elif O0ooo0 == 19 :
 O0oOo00O ( ooO0oOOooOo0 )
 if 17 - 17: iIi1i1ii1
elif O0ooo0 == 40 :
 I1iiI1II ( o000O0O , ooO0oOOooOo0 , I11o0oO00oO0o0o0 )
 if 12 - 12: ooOoO0O00 . oO0o
elif O0ooo0 == 42 :
 IiIi1I1i1II ( o000O0O , ooO0oOOooOo0 , I11o0oO00oO0o0o0 )
 if 14 - 14: Oooo0O0oo00oO + IIiIiII11i % Oooo0O0oo00oO . O0oOO0 * OOoOoo
elif O0ooo0 == 43 :
 i111I11i1I ( ooO0oOOooOo0 )
 if 54 - 54: OOoOoo * oo0oO00 - OooOO000
elif O0ooo0 == 20 :
 oO00OoOo ( ooO0oOOooOo0 )
 if 15 - 15: iiII11i1I1IIi / o0o00Oo0O
elif O0ooo0 == 22 :
 o00oOOO ( ooO0oOOooOo0 )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + OOoOoo . OooOO000 * OOoOoo
elif O0ooo0 == 23 :
 iIiii1Ii ( ooO0oOOooOo0 )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif O0ooo0 == 24 :
 O0O0OOo ( ooO0oOOooOo0 )
 if 82 - 82: o0o00Oo0O / iiII11i1I1IIi * oO0o - oo0oO00 + I1ii11iIi11i
elif O0ooo0 == 25 :
 OOoOooO0o ( ooO0oOOooOo0 )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + IIi * IIiIiII11i
elif O0ooo0 == 26 :
 i1I1iI11Iii ( ooO0oOOooOo0 )
 if 78 - 78: OooOO000 - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif O0ooo0 == 27 :
 I11IIIIi1 ( ooO0oOOooOo0 )
 if 97 - 97: ooOoO0O00
elif O0ooo0 == 28 :
 OOoo0oo000oo ( ooO0oOOooOo0 )
 if 29 - 29: oOo0O0Ooo
elif O0ooo0 == 29 :
 ii1iiiiii ( ooO0oOOooOo0 )
 if 37 - 37: Ii1I * OooOO000 * oOo0O0Ooo * o0o00Oo0O
elif O0ooo0 == 30 :
 iIiiiii1IIiI ( ooO0oOOooOo0 )
 if 35 - 35: oOo0O0Ooo - Ii1I * iiII11i1I1IIi + iIi1i1ii1 / ooOoO0O00
elif O0ooo0 == 31 :
 O00oO0oOOOOOO ( ooO0oOOooOo0 )
 if 46 - 46: I1ii11iIi11i . OOoOoo % I1ii11iIi11i / IIiIiII11i * OOoOoo * Oooo0O0oo00oO
elif O0ooo0 == 32 :
 OoOoO ( )
 if 59 - 59: OooOO000 * iiII11i1I1IIi
elif O0ooo0 == 33 :
 iIi1Iii111I ( )
 if 31 - 31: oo0oO00 / o0o00Oo0O
elif O0ooo0 == 35 :
 Ii11Iii ( ooO0oOOooOo0 )
 if 57 - 57: ooOoO0O00 % OOoOoo
elif O0ooo0 == 34 :
 IIi11i11 ( ooO0oOOooOo0 )
 if 69 - 69: I11i
elif O0ooo0 == 36 :
 ii1I11i ( ooO0oOOooOo0 )
 if 69 - 69: OooOO000
elif O0ooo0 == 37 :
 IiI1 ( ooO0oOOooOo0 )
 if 83 - 83: iI11I1II1I1I . I11i + OooOO000 . ii / OOoOoo + IIiIiII11i
elif O0ooo0 == 38 :
 I111i1Ii1i1 ( ooO0oOOooOo0 )
 if 90 - 90: IIi * iiII11i1I1IIi / Oooo0O0oo00oO
elif O0ooo0 == 41 :
 oO00ooooO0o ( oo0o )
 if 68 - 68: OOooOOo
elif O0ooo0 == 39 :
 Ii1I1i ( ooO0oOOooOo0 )
 if 65 - 65: O0oOO0
elif O0ooo0 == 45 :
 TEXTS ( )
 if 82 - 82: I11i
elif O0ooo0 == 46 :
 OOI1iI1ii1II ( )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + OooOO000
elif O0ooo0 == 47 :
 GEVID ( )
 if 65 - 65: IIi
elif O0ooo0 == 48 :
 OooOoOO0OO ( o000O0O , ooO0oOOooOo0 , I11o0oO00oO0o0o0 )
 if 71 - 71: OooOO000 % OooOO000 . O0oOO0 + Ii - Ii
elif O0ooo0 == 49 :
 OOo0 ( )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / OooOO000 - Ii . OOoOoo / Oooo0O0oo00oO
elif O0ooo0 == 222 :
 OO0OoOOO0 ( ooO0oOOooOo0 )
 if 13 - 13: I11i % o0o00Oo0O - OooOO000 * ii / I1ii11iIi11i - ii
elif O0ooo0 == 333 :
 i11i1IiIi ( ooO0oOOooOo0 )
 if 78 - 78: O0oOO0 % ii
 if 73 - 73: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + ooOoO0O00 - ii / O0oOO0
elif O0ooo0 == 1020 :
 OOOoOOooO0 ( )
 if 78 - 78: ii % O0oOO0 - Ii
elif O0ooo0 == 1021 :
 ANIMEEP ( )
 if 37 - 37: iIi1i1ii1 % IIi % ooOoO0O00
elif O0ooo0 == 1022 :
 ANIMEPLAY ( ooO0oOOooOo0 )
 if 23 - 23: OOoOoo - o0o00Oo0O + Ii
elif O0ooo0 == 1001 :
 O0000oOo0OO ( )
 if 98 - 98: ii
elif O0ooo0 == 1005 :
 ii1ii11Ii ( )
 if 61 - 61: I11i . iIi1i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
elif O0ooo0 == 1007 :
 I1III11i11Iii ( ooO0oOOooOo0 )
 if 65 - 65: ooOoO0O00 * Oooo0O0oo00oO * ii - iIi1i1ii1 . iiII11i1I1IIi - oO0o
elif O0ooo0 == 1010 :
 iIi ( ooO0oOOooOo0 )
 if 71 - 71: IIi * OOooOOo
elif O0ooo0 == 1011 :
 I1Iii1 ( ooO0oOOooOo0 )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % OooOO000 * I11i
elif O0ooo0 == 1012 :
 i1II1i ( ooO0oOOooOo0 )
 if 64 - 64: OOoOoo / OOoOoo + Ii1I * Oooo0O0oo00oO % Oooo0O0oo00oO
elif O0ooo0 == 1030 :
 Ii1II111iIi ( )
 if 87 - 87: oO0o * I1ii11iIi11i
elif O0ooo0 == 1031 :
 oo00ooOOoo ( ooO0oOOooOo0 , oo0 )
 if 83 - 83: ooOoO0O00 * OooOO000 - iIi1i1ii1 / IIi
elif O0ooo0 == 1032 :
 I1IiI1iI11 ( ooO0oOOooOo0 )
 if 48 - 48: O0oOO0 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif O0ooo0 == 1006 :
 Parse . ParseURL ( ooO0oOOooOo0 )
 if 32 - 32: IIi * oOo0O0Ooo - Oooo0O0oo00oO . I1ii11iIi11i / o0o00Oo0O + IIi
elif O0ooo0 == 2030 :
 Parse . addonParseURL ( ooO0oOOooOo0 )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif O0ooo0 == 2031 :
 Parse . apkParseURL ( ooO0oOOooOo0 )
 if 7 - 7: Ii % Ii1I / OooOO000 % I1ii11iIi11i - oO0o
elif O0ooo0 == 1002 :
 o0OooO0 ( ooO0oOOooOo0 )
 if 73 - 73: Ii1I
elif O0ooo0 == 1003 :
 II1I1 ( ooO0oOOooOo0 , oo0 )
 if 92 - 92: Ii + o0o00Oo0O * oo0oO00
elif O0ooo0 == 1004 :
 Oo0ooOOO ( ooO0oOOooOo0 )
 if 60 - 60: I11i / I1ii11iIi11i
elif O0ooo0 == 1008 :
 Oo00oOo ( )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif O0ooo0 == 1009 :
 IiIi1I1IiI1II1 ( ooO0oOOooOo0 )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % OooOO000 / Ii1I
elif O0ooo0 == 2001 :
 II1iiIiI1 ( )
 if 76 - 76: oO0o * O0oOO0 - oO0o
elif O0ooo0 == 2002 :
 oo0O0OO0Oooo ( ooO0oOOooOo0 )
 if 57 - 57: ii / OOooOOo + O0oOO0 . IIi
elif O0ooo0 == 1013 :
 III1Ii1i1I1 ( )
elif O0ooo0 == 10111113 :
 i1iIIi1II1iiI ( ooO0oOOooOo0 )
 if 14 - 14: Ii % Oooo0O0oo00oO * I11i * OOooOOo
elif O0ooo0 == 1014 :
 o0ooO0Oo ( )
 if 55 - 55: OooOO000 * Oooo0O0oo00oO * OooOO000
elif O0ooo0 == 1015 :
 O00oO0oo ( ooO0oOOooOo0 )
 if 70 - 70: o0o00Oo0O . IIi
elif O0ooo0 == 1016 :
 iIIiiiI ( ooO0oOOooOo0 , oo0 , o000O0O )
 if 33 - 33: Oooo0O0oo00oO * IIi
elif O0ooo0 == 1017 :
 O0o ( )
 if 64 - 64: Ii . iI11I1II1I1I
elif O0ooo0 == 1018 :
 oOOO00o000o ( ooO0oOOooOo0 )
 if 7 - 7: OOooOOo % OOoOoo + OOooOOo - OOooOOo * Ii % oO0o
elif O0ooo0 == 1023 :
 oO0OoO00o ( )
 if 57 - 57: Oooo0O0oo00oO / oO0o + Ii1I
elif O0ooo0 == 1024 :
 iIiII1 ( ooO0oOOooOo0 )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % Oooo0O0oo00oO + iIi1i1ii1 . oO0o . I1ii11iIi11i
elif O0ooo0 == 1025 :
 iI1Iii1i1 ( ooO0oOOooOo0 )
 if 70 - 70: oo0oO00 . Ii1I * O0oOO0
elif O0ooo0 == 4001 :
 IIOOO0O00O0OOOO ( )
 if 97 - 97: O0oOO0 . iI11I1II1I1I - Oooo0O0oo00oO
elif O0ooo0 == 4002 :
 iI1i111I1Ii ( )
 if 23 - 23: Ii1I % oo0oO00
elif O0ooo0 == 4003 :
 I1IiIii11I ( )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif O0ooo0 == 4004 :
 OoO0O00O0oo0O ( )
 if 99 - 99: OooOO000 - Ii1I - oOo0O0Ooo - OooOO000 + oO0o + IIiIiII11i
elif O0ooo0 == 4005 :
 I1IiI11 ( )
 if 34 - 34: OooOO000 * oo0oO00
elif O0ooo0 == 4006 :
 I1I1i ( )
 if 31 - 31: iIi1i1ii1 . O0oOO0
elif O0ooo0 == 4007 :
 iIiIiIiI ( )
 if 40 - 40: IIi - oo0oO00 / IIiIiII11i * ooOoO0O00 + iIi1i1ii1 * IIiIiII11i
elif O0ooo0 == 4008 :
 IiI111ii1ii ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - OooOO000
elif O0ooo0 == 4009 : Iii1iiIi1II ( )
elif O0ooo0 == 4010 : O0OO ( )
elif O0ooo0 == 3000 :
 Oooo0O00OOo0o ( )
 if 99 - 99: IIi - iIi1i1ii1 - ooOoO0O00 / Ii . iIi1i1ii1
elif O0ooo0 == 3001 :
 II1ii1 ( )
 if 58 - 58: Oooo0O0oo00oO
elif O0ooo0 == 3002 :
 oO0OOO ( ooO0oOOooOo0 )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif O0ooo0 == 3003 :
 IiI1IIiiiii ( ooO0oOOooOo0 )
 if 64 - 64: OOooOOo + iIi1i1ii1 - ooOoO0O00 . IIiIiII11i . oO0o
elif O0ooo0 == 3004 :
 OooO00o000 ( ooO0oOOooOo0 )
 if 31 - 31: O0oOO0 . iiII11i1I1IIi - oo0oO00 . iI11I1II1I1I + oo0oO00 . OOooOOo
elif O0ooo0 == 404 :
 ooOoOoOoo ( o000O0O , ooO0oOOooOo0 , oo0 )
 if 86 - 86: Ii1I - Ii1I / iiII11i1I1IIi - Ii1I * iiII11i1I1IIi + OooOO000
elif O0ooo0 == 405 :
 ooOoo0O0o0OO0 ( ooO0oOOooOo0 )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - iIi1i1ii1
elif O0ooo0 == 7030 :
 II1i1iI ( )
 if 30 - 30: ii % Oooo0O0oo00oO
elif O0ooo0 == 7021 :
 i1IiI ( o000O0O )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - Oooo0O0oo00oO
elif O0ooo0 == 7022 :
 Iiii1II ( o000O0O )
 if 81 - 81: iiII11i1I1IIi % IIi . OOoOoo
elif O0ooo0 == 7000 :
 iiIi1111iiI1 ( o000O0O , ooO0oOOooOo0 , img )
 if 66 - 66: Ii1I * IIi / ii * o0o00Oo0O % Oooo0O0oo00oO
elif O0ooo0 == 7050 :
 O0O00OooO ( ooO0oOOooOo0 )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * IIi / OooOO000 * ii
elif O0ooo0 == 7051 :
 i11ii11IiI1 ( ooO0oOOooOo0 )
 if 82 - 82: I1ii11iIi11i / IIi / IIi % IIi
elif O0ooo0 == 7052 :
 O0ooO0o ( ooO0oOOooOo0 )
 if 20 - 20: OOoOoo
elif O0ooo0 == 7053 :
 IiII1111I ( ooO0oOOooOo0 )
 if 63 - 63: iI11I1II1I1I . oO0o
elif O0ooo0 == 7054 :
 CoolPlay ( ooO0oOOooOo0 )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif O0ooo0 == 7060 :
 oOOOo0Oooo ( )
 if 26 - 26: Oooo0O0oo00oO . oO0o % OOooOOo
elif O0ooo0 == 7061 :
 IiI ( ooO0oOOooOo0 )
 if 94 - 94: iIi1i1ii1
elif O0ooo0 == 7063 :
 I1iiIIiI11I ( ooO0oOOooOo0 )
 if 15 - 15: IIi - iIi1i1ii1 / o0o00Oo0O
elif O0ooo0 == 7062 :
 OOOoooOo00O ( ooO0oOOooOo0 )
 if 28 - 28: OooOO000 . ooOoO0O00 / Ii1I
elif O0ooo0 == 7064 :
 NATatozcat ( )
 if 77 - 77: Ii / OooOO000 / Ii % OOooOOo - OooOO000
elif O0ooo0 == 7067 :
 iiIIiI1I ( ooO0oOOooOo0 )
 if 80 - 80: OooOO000 % OOooOOo . ii . IIiIiII11i % iIi1i1ii1
elif O0ooo0 == 7066 :
 NATatozA ( ooO0oOOooOo0 )
 if 6 - 6: OooOO000 % iIi1i1ii1 / IIi + OooOO000 . O0oOO0
elif O0ooo0 == 7065 :
 oOoO0oOO0o ( ooO0oOOooOo0 )
 if 70 - 70: iI11I1II1I1I / IIi
elif O0ooo0 == 7070 :
 iII1 ( )
 if 61 - 61: o0o00Oo0O * I11i + OooOO000 - Oooo0O0oo00oO . oOo0O0Ooo - iIi1i1ii1
elif O0ooo0 == 7071 :
 DIZIlist ( ooO0oOOooOo0 )
 if 7 - 7: Ii1I
elif O0ooo0 == 7072 :
 DIZIpull ( ooO0oOOooOo0 )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / oo0oO00
elif O0ooo0 == 7073 :
 WATCHDIZI ( ooO0oOOooOo0 )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif O0ooo0 == 7002 :
 oOOo0O0Oo ( )
 if 13 - 13: Ii
elif O0ooo0 == 7003 :
 iiII1i11 ( ooO0oOOooOo0 )
 if 54 - 54: Oooo0O0oo00oO . Ii1I * oo0oO00 % OooOO000 . o0o00Oo0O * iIi1i1ii1
elif O0ooo0 == 7004 :
 iIOoO0O00 ( ooO0oOOooOo0 )
 if 87 - 87: IIi % Ii1I * I1ii11iIi11i
elif O0ooo0 == 7020 :
 o0o00 ( ooO0oOOooOo0 )
 if 59 - 59: I1ii11iIi11i / oo0oO00 - iI11I1II1I1I * iI11I1II1I1I
elif O0ooo0 == 7001 :
 O0Oo000 ( )
 if 18 - 18: oo0oO00 * Ii1I / Ii / iI11I1II1I1I * ii . Oooo0O0oo00oO
elif O0ooo0 == 7010 :
 oo0iIi1iiii1ii ( ooO0oOOooOo0 )
 if 69 - 69: I1ii11iIi11i * OOoOoo
elif O0ooo0 == 7011 :
 i1oo0OO0Oo ( ooO0oOOooOo0 )
 if 91 - 91: I11i . OOoOoo / oO0o / Ii * I11i
elif O0ooo0 == 7012 :
 I1III1I1IiI ( ooO0oOOooOo0 )
 if 52 - 52: oOo0O0Ooo - Ii / iIi1i1ii1 . O0oOO0
elif O0ooo0 == 7013 :
 cnfTVPlay2 ( ooO0oOOooOo0 )
elif O0ooo0 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooO0oOOooOo0 )
elif O0ooo0 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooO0oOOooOo0 )
elif O0ooo0 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( o000O0O , ooO0oOOooOo0 , oo0 )
elif O0ooo0 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O0ooo0 == 7018 :
 I1i1IiIIiIiII ( )
elif O0ooo0 == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooO0oOOooOo0 )
elif O0ooo0 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooO0oOOooOo0 )
elif O0ooo0 == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooO0oOOooOo0 )
 if 38 - 38: O0oOO0 + ii * OOooOOo % O0oOO0
elif O0ooo0 == 8000 :
 iiIiI11IiI ( )
elif O0ooo0 == 8001 :
 iIi1 ( )
elif O0ooo0 == 8002 :
 oooOo0OO ( )
elif O0ooo0 == 8003 :
 o0OO0Oooo ( )
elif O0ooo0 == 8004 :
 o0000OOOo ( )
elif O0ooo0 == 8005 :
 III1Ii11i1II ( )
elif O0ooo0 == 8006 :
 oo0oOOoOoo ( o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 8030 :
 II11I ( ooO0oOOooOo0 )
elif O0ooo0 == 8045 :
 I1I111IIIi1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8046 :
 oOOo00O0O0 ( ooO0oOOooOo0 )
elif O0ooo0 == 8047 :
 IIi11I1i1I1I ( ooO0oOOooOo0 )
elif O0ooo0 == 8048 :
 oOo0Oo00O ( ooO0oOOooOo0 )
elif O0ooo0 == 8049 :
 i1io0o00O ( ooO0oOOooOo0 )
elif O0ooo0 == 804900 :
 iiiI1ii ( ooO0oOOooOo0 )
elif O0ooo0 == 8020 :
 iiIi1i ( )
elif O0ooo0 == 8021 :
 iiii1IiI1i1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8022 :
 ii1iii1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8023 :
 IiII1II1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8040 :
 IiIII1 ( )
elif O0ooo0 == 8041 :
 o0OOOO ( ooO0oOOooOo0 )
elif O0ooo0 == 8042 :
 I11i1i11IiIi1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8043 :
 yt . PlayVideo ( ooO0oOOooOo0 )
elif O0ooo0 == 8044 :
 I11i1I1Ii ( ooO0oOOooOo0 )
elif O0ooo0 == 8060 :
 IiIiII1 ( )
elif O0ooo0 == 8061 :
 Oo0OOOOOOO0oo ( ooO0oOOooOo0 )
elif O0ooo0 == 8064 :
 I1i11111i1i11 ( )
elif O0ooo0 == 8065 :
 I1iIIIiiii ( ooO0oOOooOo0 )
elif O0ooo0 == 8070 :
 O0o0oo0O ( )
elif O0ooo0 == 8071 :
 Ooo00OOo000 ( ooO0oOOooOo0 )
elif O0ooo0 == 7080 :
 i1ooOO00o0 ( ooO0oOOooOo0 )
elif O0ooo0 == 8090 :
 I1i1ii1ii ( )
elif O0ooo0 == 8091 :
 I11II11IiI11 ( ooO0oOOooOo0 )
elif O0ooo0 == 8092 :
 i111111 ( ooO0oOOooOo0 )
elif O0ooo0 == 8093 :
 O00o ( ooO0oOOooOo0 )
elif O0ooo0 == 8081 :
 oOoO0o0o ( )
elif O0ooo0 == 8062 :
 oo0OoOO000O ( ooO0oOOooOo0 )
elif O0ooo0 == 8063 :
 iiI1 ( ooO0oOOooOo0 )
elif O0ooo0 == 8050 :
 oOOO0ooOO ( )
elif O0ooo0 == 8051 :
 i11IiI1iiI11 ( ooO0oOOooOo0 )
elif O0ooo0 == 8052 :
 OOoOOOO00 ( ooO0oOOooOo0 )
elif O0ooo0 == 8085 :
 OoOiII11IiIi ( )
elif O0ooo0 == 8086 :
 oo0O0 ( ooO0oOOooOo0 )
elif O0ooo0 == 8087 :
 IiI1Iii1IIII1Iii ( ooO0oOOooOo0 )
elif O0ooo0 == 8088 :
 OOOOOOo0o0O0o ( ooO0oOOooOo0 , o000O0O )
elif O0ooo0 == 9000 :
 iIIi1 ( )
elif O0ooo0 == 1111 :
 iiO0O0o0oO0O00 ( )
elif O0ooo0 == 9001 :
 iI1 ( )
elif O0ooo0 == 9002 :
 Oo00o0OO0O00o ( )
elif O0ooo0 == 9003 :
 o0o0ooOO0 ( )
elif O0ooo0 == 9004 :
 World1 ( )
elif O0ooo0 == 9005 :
 World2 ( ooO0oOOooOo0 )
elif O0ooo0 == 9006 :
 World3 ( ooO0oOOooOo0 )
elif O0ooo0 == 9007 :
 O0000ooO ( )
elif O0ooo0 == 9008 :
 O00OoO ( ooO0oOOooOo0 )
elif O0ooo0 == 9009 :
 I11i11 ( ooO0oOOooOo0 )
elif O0ooo0 == 9010 :
 o00O00oO ( )
elif O0ooo0 == 9011 :
 OO000O000OOO ( ooO0oOOooOo0 )
elif O0ooo0 == 50 :
 Ii11ii1Iiii ( ooO0oOOooOo0 )
elif O0ooo0 == 9020 :
 champlist ( )
elif O0ooo0 == 9021 :
 I1iiiiI ( )
elif O0ooo0 == 9022 :
 o0oOOO0 ( )
elif O0ooo0 == 9023 :
 i1Iii ( )
elif O0ooo0 == 9024 :
 o0OOO ( ooO0oOOooOo0 )
elif O0ooo0 == 9030 :
 OOoOO0oOooo ( ooO0oOOooOo0 )
elif O0ooo0 == 9031 :
 i1II11II11 ( ooO0oOOooOo0 )
elif O0ooo0 == 9032 :
 oooiiI11 ( ooO0oOOooOo0 )
elif O0ooo0 == 9033 :
 i11IiIiii ( ooO0oOOooOo0 )
elif O0ooo0 == 9034 :
 iiI11i1II ( )
elif O0ooo0 == 7085 :
 O00O ( ooO0oOOooOo0 )
elif O0ooo0 == 7086 :
 IiIIi ( ooO0oOOooOo0 )
elif O0ooo0 == 7087 :
 oooO00oOOooO ( I11o0oO00oO0o0o0 )
elif O0ooo0 == 9666 :
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
elif O0ooo0 == 10100 : o00i111iiIiiIiI ( )
elif O0ooo0 == 101001 : iiiI1IiI ( ooO0oOOooOo0 )
elif O0ooo0 == 10105 : IIiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 10106 : I1I1IIiiI1 ( ooO0oOOooOo0 )
elif O0ooo0 == 10104 : oo0O0Ii111Ii11 ( ooO0oOOooOo0 )
elif O0ooo0 == 10107 : Ii111IIIIii ( )
elif O0ooo0 == 10103 : oooOOO0o0O0 ( ooO0oOOooOo0 )
elif O0ooo0 == 10108 : o0O0O0O00o ( ooO0oOOooOo0 )
elif O0ooo0 == 10000 : Origin_Menu ( )
elif O0ooo0 == 10001 : III111i11IiI ( )
elif O0ooo0 == 10002 : iI1iiiiIii ( )
elif O0ooo0 == 10003 : O0OOo ( )
elif O0ooo0 == 10004 : ooO00O0O0 ( ooO0oOOooOo0 )
elif O0ooo0 == 10005 : O0OO0oOOo ( )
elif O0ooo0 == 10006 : O00oo00oOOO0o ( ooO0oOOooOo0 )
elif O0ooo0 == 10007 : o0O0O ( ooO0oOOooOo0 , oo0 )
elif O0ooo0 == 10008 : o00o0O0 ( )
elif O0ooo0 == 10009 : Oo00oo ( )
elif O0ooo0 == 10010 : o0ooo ( ooO0oOOooOo0 )
elif O0ooo0 == 10011 : Oo0oo ( ooO0oOOooOo0 )
elif O0ooo0 == 10012 : Ii1IIiI1i ( ooO0oOOooOo0 )
elif O0ooo0 == 10109 : i1iII1IiI1I ( ooO0oOOooOo0 )
elif O0ooo0 == 10013 : oOooOoOOo0O ( ooO0oOOooOo0 )
elif O0ooo0 == 10014 : oO0o0oOo ( )
elif O0ooo0 == 10015 : oOoo0ooOoo ( )
elif O0ooo0 == 10016 : II1Ii11Ii1i1I ( ooO0oOOooOo0 )
elif O0ooo0 == 10017 : i1i1iIII11i ( )
elif O0ooo0 == 10018 : ooO0o0oO0 ( )
elif O0ooo0 == 10019 : I1111 ( )
elif O0ooo0 == 10020 : oooo0 ( )
elif O0ooo0 == 10021 : ooO ( )
elif O0ooo0 == 10022 : iIi1iiI1i1 ( ooO0oOOooOo0 )
elif O0ooo0 == 10023 : i1ii1iIi ( o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 10024 : O0Oo0oOOo0O ( ooO0oOOooOo0 )
elif O0ooo0 == 10025 : ii1I1IiiI1ii1i ( )
elif O0ooo0 == 10026 : I1i1I11111iI1 ( )
elif O0ooo0 == 10027 : o0OoOoooo0 ( )
elif O0ooo0 == 10028 : i11II ( )
elif O0ooo0 == 10029 : o00oo ( )
elif O0ooo0 == 423 : iIIiI1111 ( ooO0oOOooOo0 )
elif O0ooo0 == 426 : oooo0o0OOO0 ( ooO0oOOooOo0 )
elif O0ooo0 == 10030 : Izle_Films ( )
elif O0ooo0 == 10031 : Latest_Izle_Movies ( )
elif O0ooo0 == 10032 : Izle_Genres ( )
elif O0ooo0 == 10033 : Izle_Pop_Movies ( )
elif O0ooo0 == 10034 : Izle_Boxsets ( )
elif O0ooo0 == 10035 : Izle_Search ( )
elif O0ooo0 == 10036 : Izle_Genres_Movie ( ooO0oOOooOo0 )
elif O0ooo0 == 10037 : Izle_Boxset_single ( ooO0oOOooOo0 )
elif O0ooo0 == 10038 : Izle_IFRAME ( )
elif O0ooo0 == 10039 : Izle_Boxsets_Next ( ooO0oOOooOo0 )
elif O0ooo0 == 10040 : O0Oooo ( )
elif O0ooo0 == 10041 : o0OoO0000oOO ( ooO0oOOooOo0 )
elif O0ooo0 == 10042 : I11iiIi1i1IIi ( ooO0oOOooOo0 )
elif O0ooo0 == 10043 : oOIIIi11 ( )
elif O0ooo0 == 10044 : iiIIiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 10045 : o0Ooi1II11i1iI1 ( o000O0O )
elif O0ooo0 == 10046 : i1Ii1i1I11III ( ooO0oOOooOo0 )
elif O0ooo0 == 10047 : I11iI1 ( ooO0oOOooOo0 )
elif O0ooo0 == 10048 : Oo0o0ooOoO ( ooO0oOOooOo0 )
elif O0ooo0 == 10049 : Oo0000o ( ooO0oOOooOo0 )
elif O0ooo0 == 10050 : OO ( )
elif O0ooo0 == 10051 : OoOO ( )
elif O0ooo0 == 10052 : IioOo0O ( )
elif O0ooo0 == 10053 : Addon ( ooO0oOOooOo0 )
elif O0ooo0 == 10054 : iiiIiIIiIiiii ( ooO0oOOooOo0 , o000O0O )
elif O0ooo0 == 10055 :
 o0ooOO0OOO00o ( "addFavorite" )
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOOO0oo0O0OO ( o000O0O , ooO0oOOooOo0 , oo0 , II11IiIi11 , OOoO0OooO )
elif O0ooo0 == 10056 :
 o0ooOO0OOO00o ( "rmFavorite" )
 try :
  o000O0O = o000O0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o000O0O = o000O0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1IIIi1i ( o000O0O )
elif O0ooo0 == 10057 :
 o0ooOO0OOO00o ( "getFavorites" )
 IIi1iiI ( )
elif O0ooo0 == 10058 : OO0O00oOo ( )
elif O0ooo0 == 10059 : Donators_Guide ( )
elif O0ooo0 == 10060 : I1iiii1I ( )
elif O0ooo0 == 10061 : OO0o0OO0 ( )
elif O0ooo0 == 10062 : O00oOoo0OoO0 ( o000O0O , ooO0oOOooOo0 , I11o0oO00oO0o0o0 )
elif O0ooo0 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif O0ooo0 == 10064 : o0O0ooOOoO ( )
elif O0ooo0 == 10065 : I1iI1I1 ( ooO0oOOooOo0 )
elif O0ooo0 == 10066 : Ii1IIi ( ooO0oOOooOo0 )
elif O0ooo0 == 10068 : Oo0oooO0oO ( ooO0oOOooOo0 )
elif O0ooo0 == 10069 : OOoOOO0 ( ooO0oOOooOo0 )
elif O0ooo0 == 10070 : IiiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 10071 : Genie_Watch ( )
elif O0ooo0 == 10072 : oO00oOo0OOO ( )
elif O0ooo0 == 10073 : I11iiIi1i1 ( ooO0oOOooOo0 )
elif O0ooo0 == 10074 : I11IIIiIi11 ( ooO0oOOooOo0 )
elif O0ooo0 == 10075 : oo0OoOooo ( oo0 , o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 10076 : iIii ( ooO0oOOooOo0 )
elif O0ooo0 == 10077 : IiII1i1iii1Ii ( ooO0oOOooOo0 )
elif O0ooo0 == 10078 : iIi1IiI ( )
elif O0ooo0 == 10079 : Genie_Watch_Tv_Shows ( )
elif O0ooo0 == 10080 : Genie_Watch_Tv_Genre ( ooO0oOOooOo0 )
elif O0ooo0 == 10081 : Genie_Watch_TV_PlayRun ( ooO0oOOooOo0 )
elif O0ooo0 == 10082 : Genie_Watch_TV_Episodes ( ooO0oOOooOo0 , oo0 )
elif O0ooo0 == 10083 : Genie_Watch_Tv_Recent ( ooO0oOOooOo0 )
elif O0ooo0 == 10084 : OO0oOOoo ( )
elif O0ooo0 == 10085 : OOoO00 ( )
elif O0ooo0 == 10086 : i1IiiiI1iI ( )
elif O0ooo0 == 20000 : O0000 ( )
elif O0ooo0 == 20001 : oOOOOO0Ooooo ( ooO0oOOooOo0 )
elif O0ooo0 == 20002 : OOoOO0O0o0 ( ooO0oOOooOo0 )
elif O0ooo0 == 20003 : ii11Iiii ( ooO0oOOooOo0 )
elif O0ooo0 == 20004 : iiI111 ( ooO0oOOooOo0 )
elif O0ooo0 == 20005 : oOo0O ( ooO0oOOooOo0 )
elif O0ooo0 == 21004 : OO0oO0o ( )
elif O0ooo0 == 21005 : IIIIIIi1IiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 21006 : o0Oo0 ( ooO0oOOooOo0 )
elif O0ooo0 == 21007 : o00o ( ooO0oOOooOo0 )
elif O0ooo0 == 30000 : o0O0oO0 ( )
elif O0ooo0 == 30001 : O0oO0OOoO ( )
elif O0ooo0 == 10012 : Resolve ( ooO0oOOooOo0 )
elif O0ooo0 == 30003 : iiII1iiiiiii ( )
elif O0ooo0 == 30004 : o0OO ( ooO0oOOooOo0 )
elif O0ooo0 == 30005 : ii11iI1iIiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 30006 : i1ii1IIIII ( )
elif O0ooo0 == 30007 : Iii1i11iiI1 ( )
elif O0ooo0 == 30008 : o0o0OoO0OOO0 ( ooO0oOOooOo0 )
elif O0ooo0 == 30009 : OoooO0 ( ooO0oOOooOo0 )
elif O0ooo0 == 30010 : iIiIii1I1 ( ooO0oOOooOo0 )
elif O0ooo0 == 30011 : o00iIiiiII ( )
elif O0ooo0 == 30012 : I11iiI11iiI ( )
elif O0ooo0 == 30013 : iIII11Iiii1 ( )
elif O0ooo0 == 30014 : i111I11I ( )
elif O0ooo0 == 30015 : Oo0O00o0oo0oOO ( ooO0oOOooOo0 , oo0 , II11IiIi11 )
elif O0ooo0 == 30016 : oOOO0 ( ooO0oOOooOo0 )
elif O0ooo0 == 30019 : I11I1ii1i ( ooO0oOOooOo0 )
elif O0ooo0 == 30017 : OoOOoooO000 ( ooO0oOOooOo0 )
elif O0ooo0 == 30018 : iiI1i ( ooO0oOOooOo0 )
elif O0ooo0 == 30030 : oooOoOoOO ( )
elif O0ooo0 == 30031 : II1I11Iii1 ( )
elif O0ooo0 == 30032 : i11OOoo ( )
elif O0ooo0 == 30033 : OooOO ( )
elif O0ooo0 == 30034 : iio0oo0Oo ( )
elif O0ooo0 == 30035 : III1II1iii1i ( ooO0oOOooOo0 )
elif O0ooo0 == 30036 : O0OO0oOO ( ooO0oOOooOo0 )
elif O0ooo0 == 30037 : ooooO ( ooO0oOOooOo0 )
elif O0ooo0 == 30038 : IIiI11 ( )
elif O0ooo0 == 30039 : oO0O0OO0O ( )
elif O0ooo0 == 50000 : oOO0O00Oo0O0o ( )
elif O0ooo0 == 50001 : Oo00ooO0OoOo ( )
elif O0ooo0 == 50002 : ooo00o0OO ( ooO0oOOooOo0 )
elif O0ooo0 == 50003 : iI1iIIII1 ( I11o0oO00oO0o0o0 )
elif O0ooo0 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif O0ooo0 == 60001 : I1i ( )
elif O0ooo0 == 60002 : iIIi1iI1I1IIi ( o000O0O )
elif O0ooo0 == 60003 : O0oOOo0o ( o000O0O )
elif O0ooo0 == 50004 : iiIiIIIiiI ( )
elif O0ooo0 == 50005 : speedtest . runtest ( ooO0oOOooOo0 )
elif O0ooo0 == 70001 : i1iii1ii ( )
elif O0ooo0 == 70002 : III1III11II ( ooO0oOOooOo0 )
elif O0ooo0 == 70003 : iIi1iI ( ooO0oOOooOo0 )
elif O0ooo0 == 70004 : OO0Oo ( ooO0oOOooOo0 )
elif O0ooo0 == 70005 : IIiiiiiIiIIi ( ooO0oOOooOo0 )
elif O0ooo0 == 70006 : iiIiiIi1 ( )
elif O0ooo0 == 50006 : OOOiiiiI ( i1 , i1111 )
elif O0ooo0 == 80000 : iiI1Ii11II1I ( )
elif O0ooo0 == 80001 : resolvefilmon ( ooO0oOOooOo0 )
elif O0ooo0 == 80002 : Ii1iiII1i ( )
elif O0ooo0 == 80003 : III1ii ( o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 80004 : iI111i11iI1 ( o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 80005 : iI1ii1i ( )
elif O0ooo0 == 80006 : I111IIiii1Ii ( ooO0oOOooOo0 )
elif O0ooo0 == 80007 : II1 ( ooO0oOOooOo0 )
elif O0ooo0 == 80008 : iiIIIiIii ( )
elif O0ooo0 == 80009 : iIo00oo ( )
elif O0ooo0 == 80010 : O000Oo00 ( ooO0oOOooOo0 )
elif O0ooo0 == 80011 : iio00O0o00oo ( ooO0oOOooOo0 )
elif O0ooo0 == 80012 : oOOoo ( )
elif O0ooo0 == 90000 : I1i11IIIi ( o000O0O , ooO0oOOooOo0 )
elif O0ooo0 == 90001 : I1I1i1I ( )
elif O0ooo0 == 90002 : I1i1i1 ( )
elif O0ooo0 == 90003 : o0oOoo0o ( ooO0oOOooOo0 )
elif O0ooo0 == 90004 : IiiIiIIi ( ooO0oOOooOo0 )
elif O0ooo0 == 90005 : O00Oo ( ooO0oOOooOo0 )
elif O0ooo0 == 90006 : OOOOoOoO ( ooO0oOOooOo0 )
elif O0ooo0 == 90007 : OO000 ( ooO0oOOooOo0 )
elif O0ooo0 == 90008 : Oo0iII ( ooO0oOOooOo0 )
elif O0ooo0 == 90009 : iIIi1OoOo0O00 ( ooO0oOOooOo0 )
elif O0ooo0 == 90010 : oooOo0OOOoo0 ( )
elif O0ooo0 == 90020 : O0o0 ( )
elif O0ooo0 == 90021 : hellyeah2 ( ooO0oOOooOo0 )
elif O0ooo0 == 90022 : hellyeah3 ( ooO0oOOooOo0 )
elif O0ooo0 == 90023 : i1OoOO ( )
elif O0ooo0 == 90024 : o0OIIiI1I1 ( ooO0oOOooOo0 )
elif O0ooo0 == 90025 : I11I1IIiiII1 ( ooO0oOOooOo0 )
if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif O0ooo0 == 90030 : OOOoOo ( )
elif O0ooo0 == 90031 : I11iI1i1I11I11 ( )
elif O0ooo0 == 90032 : I1i1i1iii ( ooO0oOOooOo0 )
elif O0ooo0 == 90033 : iIIii ( ooO0oOOooOo0 )
elif O0ooo0 == 90034 : ooOoO00 ( ooO0oOOooOo0 )
elif O0ooo0 == 90035 : o0O00Oo0 ( ooO0oOOooOo0 )
if 24 - 24: OOooOOo * IIi
if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif O0ooo0 == 100001 : Stand_up ( )
if 81 - 81: Oooo0O0oo00oO
elif O0ooo0 == 100003 : II1Ii11Ii1i1I ( ooO0oOOooOo0 )
elif O0ooo0 == 100004 : O0iII1 ( ooO0oOOooOo0 )
elif O0ooo0 == 100005 : Resolve ( ooO0oOOooOo0 )
elif O0ooo0 == 100008 : Search ( )
elif O0ooo0 == 100007 : iIi11iiIiI1I ( ooO0oOOooOo0 )
elif O0ooo0 == 100009 : yt . PlayVideo ( ooO0oOOooOo0 )
elif O0ooo0 == 100010 : oOi11iI11iIiIi ( ooO0oOOooOo0 )
elif O0ooo0 == 100100 : ii1Oo0000oOo ( oo0 , ooO0oOOooOo0 , Oo0oOo0 )
elif O0ooo0 == 100101 : OOOIiiiii1iI ( ooO0oOOooOo0 , o000O0O , II11IiIi11 , Oo0oOo0 , oo0 )
elif O0ooo0 == 100102 : oO0o00oOOooO0 ( o000O0O , ooO0oOOooOo0 , oo0 , II11IiIi11 )
elif O0ooo0 == 100106 : ooO0o ( ooO0oOOooOo0 , o000O0O )
elif O0ooo0 == 100107 : Oo0oOooo000OO ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
