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
IiiIII111iI = "3.2.6"
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
def OOoO ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 o00oooO0Oo = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for iiIiI1i1 , oO0O00oOOoooO in o00oooO0Oo :
  OOOiiiiI ( '[COLOR' + iiI1IiI + ']Tommys List[/COLOR]  ' + iiIiI1i1 , oO0O00oOOoooO )
def IiIi11iI ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 o00oooO0Oo = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
def i11I1IiII1i1i ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( OO0O000 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , ooI1111i , OO0o , '' )
 for url in next :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , oOOOo00O00oOo + 'NEXT.png' , OO0o , '' )
def iIIii ( url ) :
 OO0O000 = O0 ( url )
 o00O0O = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 ii1iii1i = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o00oooO0Oo = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for Oo0O00O000 , url in o0O0OOO0Ooo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for Oo0O00O000 , url in ii1iii1i :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
 for url in o00O0O :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , oOOOo00O00oOo + 'tommysreplays.png' , OO0o , '' )
  if 35 - 35: IIiIiII11i % Oooo0O0oo00oO . OOoOoo + OOoOoo % IIiIiII11i % IIiIiII11i
def ooOoO00 ( url ) :
 if 'drive' in url :
  Ii1IIiI1i ( url )
 else :
  OO0O000 = O0 ( url )
  o00oooO0Oo = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( OO0O000 )
  for url in o00oooO0Oo :
   Ii1IIiI1i ( url )
   if 78 - 78: Ii1I
def I1iIIiiIIi1i ( ) :
 o0Oo0oO0oOO00 = False
 if os . path . exists ( os . path . join ( II , 'xbmc.log' ) ) :
  o0Oo0oO0oOO00 = os . path . join ( II , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II , 'kodi.log' ) ) :
  o0Oo0oO0oOO00 = os . path . join ( II , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II , 'spmc.log' ) ) :
  o0Oo0oO0oOO00 = os . path . join ( II , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II , 'tvmc.log' ) ) :
  o0Oo0oO0oOO00 = os . path . join ( II , 'tvmc.log' )
 return o0Oo0oO0oOO00
 if 92 - 92: ii * OooOO000
def o0000oO ( url ) :
 if url == 'http://' : return False
 try :
  OOO00O = urllib2 . Request ( url )
  OOO00O . add_header ( 'User-Agent' , I1i1iiI1 )
  OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
  OOoOO0oo0ooO . close ( )
 except Exception , I1II1 :
  return I1II1
 return True
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
def II1i111Ii1i ( ) :
 O0o0O00Oo0o0 = O0 ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 if len ( o00oooO0Oo ) > 0 :
  for Oo0O00O000 , ooO0oOOooOo0 , iii1 , ooO0oooOO0 in o00oooO0Oo :
   o0OIiII ( Oo0O00O000 , ooO0oOOooOo0 , 50005 , iii1 , ooO0oooOO0 , '' )
def o0o ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Wizard[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   oo0 ( )
  if O0oO0 == 1 :
   oOOOoo00 ( )
  if O0oO0 == 2 :
   iiIiIIIiiI ( iiI1IIIi )
  if O0oO0 == 3 :
   II11IiIi11 ( ooO0oOOooOo0 )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 7 - 7: oO0o . IIi % O0oOO0 * OOoOoo + iIi1i1ii1 + OooOO000
def IIIIiII1i ( ) :
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
   if 1 - 1: IIiIiII11i
   if 68 - 68: iiII11i1I1IIi - oOo0O0Ooo / OooOO000 / oo0oO00
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , OO0o , '' )
  if 12 - 12: IIi + Ii * iI11I1II1I1I / Ii1I . oo0oO00
  if 5 - 5: ooOoO0O00 + iIi1i1ii1 / I11i . iiII11i1I1IIi / oo0oO00
  if 32 - 32: oOo0O0Ooo % iI11I1II1I1I / ooOoO0O00 - oOo0O0Ooo
  if 7 - 7: OooOO000 * oO0o - OOoOoo + Oooo0O0oo00oO * oOo0O0Ooo % oO0o
  if 15 - 15: OOooOOo % oOo0O0Ooo * oo0oO00
  if 81 - 81: OOoOoo - iI11I1II1I1I - ooOoO0O00 / OooOO000 - o0o00Oo0O * oo0oO00
  if 20 - 20: O0oOO0 % iIi1i1ii1
  if 19 - 19: Ii1I % iIi1i1ii1 + OOoOoo / OooOO000 . OOoOoo
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , OO0o , '' )
  if 12 - 12: ooOoO0O00 + ooOoO0O00 - Ii1I * I1ii11iIi11i % I1ii11iIi11i - IIiIiII11i
  if 52 - 52: OOoOoo . iiII11i1I1IIi + OooOO000
  if 38 - 38: ooOoO0O00 - IIiIiII11i . OooOO000
  if 58 - 58: oOo0O0Ooo . iiII11i1I1IIi + OOooOOo
  if 66 - 66: iiII11i1I1IIi / O0oOO0 * ii + ii % oo0oO00
  if 49 - 49: O0oOO0 - Ii . OooOO000 * IIi % iiII11i1I1IIi + ooOoO0O00
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def oOO0OOOo ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , '[COLOR' + iiI1IiI + ']Dont Blame Us Tv[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']CATEGORIES[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  oo0o0000 ( )
 if O0oO0 == 1 :
  iiI ( )
 if O0oO0 == 2 :
  oOOO0o ( )
 if O0oO0 == 3 :
  O00oOOooo ( )
 if O0oO0 == 4 :
  iI1iIii11Ii ( )
 if O0oO0 == 5 :
  IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , I1i1i1 , Oo0O00O000 )
 if O0oO0 == 6 :
  OoO0O00O0oo0O ( )
 if O0oO0 == 7 :
  I1IiI11 ( )
 if O0oO0 == 8 :
  iI1iiiiIii ( )
 if O0oO0 == 9 :
  iIiIiIiI ( )
 if O0oO0 == 10 :
  i11OOoo ( )
  if 50 - 50: oO0o
  if 43 - 43: IIiIiII11i . O0oOO0 / Ii1I
def I11IiI ( ) :
 if not os . path . exists ( o0 ) :
  OOOiiiiI ( 'Change Log 9/11/16 - v3.2.5' , 'Freeview section added to streams 30+ channels, search series fixed, more movies and music added, Tommys Sports section updated with new football highlights section' )
  os . makedirs ( o0 )
  if 20 - 20: oOo0O0Ooo
  if 95 - 95: iiII11i1I1IIi - oOo0O0Ooo
def oo0o0000 ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , '[COLOR' + iiI1IiI + ']DESI FLIX[/COLOR]' , '[COLOR' + iiI1IiI + ']FILM TRAILERS[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I1ii1ii11i1I ( )
  if O0oO0 == 1 :
   o0OoOO ( ooO0oOOooOo0 )
  if O0oO0 == 2 :
   O0O0Oo00 ( )
  if O0oO0 == 3 :
   oOoO00o ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0oO0 == 4 :
   oO00O0 ( )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def IIi1IIIi ( ) :
 Oo00oo0oO ( )
 O00Ooo ( )
 if 52 - 52: Ii1I - I1ii11iIi11i + Ii1I % I11i
 if 35 - 35: iI11I1II1I1I
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0OIiII ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , OO0o , '' )
def i11OOoo ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']DAILY LISTS[/COLOR]' , '' , 9007 , Ooo , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Ooo , OO0o , '' )
 if 42 - 42: OooOO000 . oOo0O0Ooo . ooOoO0O00 + OOooOOo + Oooo0O0oo00oO + oOo0O0Ooo
 if 31 - 31: iiII11i1I1IIi . Oooo0O0oo00oO - OOoOoo . ii / ii
 if 56 - 56: oO0o / O0oOO0 / Ii + ii - I1ii11iIi11i - oo0oO00
 if 21 - 21: o0o00Oo0O % iIi1i1ii1 . oOo0O0Ooo / IIiIiII11i + iIi1i1ii1
 if 53 - 53: O0oOO0 - oOo0O0Ooo - O0oOO0 * iiII11i1I1IIi
def iiI ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , '[COLOR' + iiI1IiI + ']TV SHOW TRAILERS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   oooooo0OO ( )
  if O0oO0 == 1 :
   iI1I ( )
  if O0oO0 == 2 :
   OooOoOo ( )
  if O0oO0 == 3 :
   III1I1Iii1iiI ( )
  if O0oO0 == 4 :
   i1Iii11I1i ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , OO0o , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , OO0o , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def Oo00o0OO0O00o ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   O0Oooo = '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   iiIi1i = '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1i11111i1i11 = '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   OOoOOO0 = '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1I1i = '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]'
  ii1I = [ O0Oooo , iiIi1i , I1i11111i1i11 , '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , I1I1i , '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , OOoOOO0 ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']StreamTeam[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , I1i1i1 , Oo0O00O000 )
  if O0oO0 == 1 :
   IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , I1i1i1 , Oo0O00O000 )
  if O0oO0 == 2 :
   I1IIIiIiIi ( )
  if O0oO0 == 3 :
   IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , I1i1i1 , Oo0O00O000 )
  if O0oO0 == 4 :
   IIIII1 ( )
  if O0oO0 == 5 :
   IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , I1i1i1 , Oo0O00O000 )
  if O0oO0 == 6 :
   iIi1Ii1i1iI ( )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL3JvZ3VlLW1lZGlhLnVrL3JlYXBlci9tYWlubWVudS5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'TheReaper.png' , OO0o , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , OO0o , '' )
   if 16 - 16: Oooo0O0oo00oO / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % Oooo0O0oo00oO
   if 71 - 71: OOooOOo
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , OO0o , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , OO0o , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , OO0o , '' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , OO0o , '' )
  if 14 - 14: Ii % Oooo0O0oo00oO
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % iIi1i1ii1 / IIi . IIi
def IIioOoO00oo0O ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , OO0o , '' )
def IiiiI ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 url = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OO0O000 )
 for oOO , O0o0OO0000ooo in o00oooO0Oo :
  if '[DIR]' in oOO :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + O0o0OO0000ooo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + O0o0OO0000ooo , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in O0o0OO0000ooo :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + O0o0OO0000ooo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + O0o0OO0000ooo , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in O0o0OO0000ooo :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + O0o0OO0000ooo + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + O0o0OO0000ooo , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 9 - 9: O0oOO0 + oo0oO00 / oo0oO00
def IIIII1 ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 I1IiiiiI ( '[COLORred]****[/COLOR][COLOR' + iiI1IiI + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , OO0o , '' )
 if 12 - 12: ii % I11i * oo0oO00 % iI11I1II1I1I / IIi
def Ii1ii1IiIII ( url ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for Oo0O00O000 , url , ooOOo00O00Oo , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI in o00oooO0Oo :
  if IiII1 == '123' :
   IiII1 = oOOOo00O00oOo + 'appstreams.png'
  if ooO0oooOO0 == '123' :
   ooO0oooOO0 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100010 , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100007 , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100100 , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif not 'http' in url :
   I1i11ii ( Oo0O00O000 , url , 100009 , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI , '' )
  else :
   I1i11ii ( Oo0O00O000 , url , 100005 , IiII1 , ooO0oooOO0 , I1iIi1iIiiIiI , '' )
   if 42 - 42: iiII11i1I1IIi + iIi1i1ii1
def o00oOoOo0 ( url ) :
 I1 = ooO0o ( url )
 o0O0O0ooo0oOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , ooI1111i , I1iIi1iIiiIiI , ooO0oooOO0 , Oo0O00O000 in o0O0O0ooo0oOO :
  if ooI1111i == '123' :
   ooI1111i = oOOOo00O00oOo + 'appstreams.png'
  if ooO0oooOO0 == '123' :
   ooO0oooOO0 = OO0o
  if 'php' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100004 , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif 'playlist' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100007 , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif 'watchseries' in url :
   I1IiiiiI ( Oo0O00O000 , url , 100100 , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
  elif not 'http' in url :
   I1i11ii ( Oo0O00O000 , url , 100009 , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI , '' )
  else :
   I1i11ii ( Oo0O00O000 , url , 100005 , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI , '' )
   if 97 - 97: oOo0O0Ooo / iiII11i1I1IIi
def Oooo0 ( url ) :
 if 59 - 59: ii
 I1 = ooO0o ( url )
 i1iiiii1 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for O0iII1 in i1iiiii1 :
  IiII1 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O0iII1 ) )
  for IiII1 in IiII1 :
   IiII1 = IiII1
  Oo0O00O000 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O0iII1 ) )
  for Oo0O00O000 in Oo0O00O000 :
   if 'elete' in Oo0O00O000 :
    pass
   elif 'rivate Vid' in Oo0O00O000 :
    pass
   else :
    Oo0O00O000 = ( Oo0O00O000 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  IIII1i = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O0iII1 ) )
  for IIII1i in IIII1i :
   IIII1i = IIII1i
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O0iII1 ) )
  for url in url :
   url = url
  I1i11ii ( '[COLORred]' + str ( IIII1i ) + '[/COLOR] : ' + str ( Oo0O00O000 ) , str ( url ) , 100009 , str ( IiII1 ) , OO0o , '' , '' )
  Iii1I1I11iiI1 ( 'movies' , '' )
  if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % O0oOO0 - IIiIiII11i - iiII11i1I1IIi
  if 3 - 3: OooOO000
  if 45 - 45: OooOO000
  if 83 - 83: OOooOOo . ii
  if 58 - 58: Ii + ii % ii / iIi1i1ii1 / Ii
def oOOoo ( iconimage , url , extra ) :
 IiII1 = ' '
 iII1111III1I = ' '
 ooO0oooOO0 = ' '
 ii11i = ' '
 O00oOo00o0o = ooO0o ( url )
 IiII1 = re . compile ( '<img src="(.+?)">' ) . findall ( O00oOo00o0o )
 for IiII1 in IiII1 :
  IiII1 = IiII1
 O00oO0 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( O00oOo00o0o )
 for ooO0oooOO0 in O00oO0 :
  ooO0oooOO0 = ooO0oooOO0
 o00oooO0Oo = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( O00oOo00o0o )
 for url , ii11i in o00oooO0Oo :
  ii11i = 'S' + ( ii11i ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = o0O + url
  O0Oo00OoOo ( ( ii11i ) . replace ( '  ' , '' ) , url , 100101 , IiII1 , ooO0oooOO0 , iII1111III1I , '' )
  Iii1I1I11iiI1 ( 'Movies' , 'info' )
  if 24 - 24: Ii - OooOO000
def i11iiI1111 ( url , name , fanart , extra , iconimage ) :
 oOoooo000Oo00 = extra
 ii11i = name
 O00oOo00o0o = ooO0o ( url )
 IiII1 = iconimage
 o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( O00oOo00o0o )
 for url , name , OOoo in o00oooO0Oo :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = o0O + url
  OOoo = OOoo
  o00O00oO00 = name + ' - [COLORred]' + OOoo + '[/COLOR]'
  O0Oo00OoOo ( o00O00oO00 , url , 100102 , IiII1 , fanart , 'Aired : ' + OOoo , o00O00oO00 )
  if 23 - 23: iI11I1II1I1I * ooOoO0O00 % ii * iIi1i1ii1
def I1Iiiiiii ( name , URL , iconimage , fanart ) :
 I1 = ooO0o ( URL )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , name in o00oooO0Oo :
  for I1IIIiI1I1ii1 in O00oO :
   if I1IIIiI1I1ii1 in ooO0oOOooOo0 :
    URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
    I1i11ii ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , OO0o , '' , '' )
 if len ( o00oooO0Oo ) <= 0 :
  O0Oo00OoOo ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 30 - 30: o0o00Oo0O * ii
  if 38 - 38: iIi1i1ii1 - Ii1I . OOooOOo - OooOO000 . ii
def ooo ( url , name ) :
 OooooO0oOO = name
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 ii1iii1i = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Iiiiii1iI ( url , OooooO0oOO )
 for url in o0O0OOO0Ooo :
  Iiiiii1iI ( url , OooooO0oOO )
 for url in ii1iii1i :
  Iiiiii1iI ( url , OooooO0oOO )
  if 49 - 49: I11i . iIi1i1ii1 / oO0o + IIiIiII11i
def Iiiiii1iI ( url , season_name ) :
 if 'daclips.in' in url :
  ii11iIII11II1I1Ii1 ( url , season_name )
 elif 'filehoot.com' in url :
  O00Oo0o000oO ( url , season_name )
 elif 'allmyvideos.net' in url :
  oO0o00oOOooO0 ( url , season_name )
 elif 'vidspot.net' in url :
  OOOoO000 ( url , season_name )
 elif 'vodlocker' in url :
  oOOOO ( url , season_name )
 elif 'vidto' in url :
  IiIi1ii111i1 ( url , season_name )
  if 31 - 31: Oooo0O0oo00oO + o0o00Oo0O
  if 87 - 87: OOoOoo
def IiIi1ii111i1 ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for IIIii , Oo0O00O000 in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 20 - 20: ooOoO0O00 * OooOO000 + IIiIiII11i % I11i % O0oOO0
  if 13 - 13: I1ii11iIi11i
def oO0o00oOOooO0 ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for IIIii , Oo0O00O000 in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 60 - 60: Ii1I * oOo0O0Ooo
def OOOoO000 ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for IIIii , Oo0O00O000 in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 17 - 17: Oooo0O0oo00oO % I1ii11iIi11i / Ii1I . iIi1i1ii1 * Oooo0O0oo00oO - IIiIiII11i
def oOOOO ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for IIIii in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 41 - 41: IIi
def ii11iIII11II1I1Ii1 ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for IIIii in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 77 - 77: OooOO000
def O00Oo0o000oO ( url , season_name ) :
 I1 = ooO0o ( url )
 o00oooO0Oo = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for IIIii in o00oooO0Oo :
  O00OooOo00o ( IIIii , season_name )
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % O0oOO0 * oO0o
def O00OooOo00o ( Link , season_name ) :
 if 'http:/' in Link :
  iI11I ( Link )
  if 11 - 11: iiII11i1I1IIi - O0oOO0 + IIiIiII11i - iI11I1II1I1I
def I1i11ii11 ( url ) :
 I1 = OPEN_URL_1 ( url )
 OO00O0oOO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in OO00O0oOO :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 4 - 4: ii - ooOoO0O00 % IIi - Oooo0O0oo00oO * I11i
def O0Oo00OoOo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  if 17 - 17: IIi + O0oOO0 . oO0o - I1ii11iIi11i * Ii
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = True )
 return oooo0O0O0o0
 if 20 - 20: oOo0O0Ooo . ii % Oooo0O0oo00oO
 if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def I1i11ii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  IIi11IIiIii1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = False )
 return oooo0O0O0o0
 if 39 - 39: iiII11i1I1IIi / IIiIiII11i / Ii1I % oOo0O0Ooo
def O0Oo00 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 41 - 41: iI11I1II1I1I % oo0oO00
def oOo0oO ( url ) :
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IIi1IIIIi . play ( url ) . strip ( )
 except : pass
 if 14 - 14: oo0oO00 . iI11I1II1I1I . ii . IIiIiII11i / I11i
def iI11I ( url ) :
 IIi1IIIIi = xbmc . Player ( )
 import urlresolver
 try : IIi1IIIIi . play ( url )
 except : pass
 if 21 - 21: Ii / ooOoO0O00 + oOo0O0Ooo * Oooo0O0oo00oO . OooOO000
def ooO0o ( url ) :
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
  if 84 - 84: o0o00Oo0O . oo0oO00 - IIiIiII11i . OOoOoo / IIiIiII11i
  if 47 - 47: ii
  if 4 - 4: oOo0O0Ooo % oo0oO00
def O00oOOooo ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']MORE CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']ANIME LAND[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Kids[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   I1oOO0o0 ( )
  if O0oO0 == 1 :
   iiI11I1i1i1iI ( )
  if O0oO0 == 2 :
   OoOOo000o0 ( )
  if O0oO0 == 3 :
   iiI1II11II1i ( )
  if O0oO0 == 4 :
   o0O0O0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def OoO0O00O0oo0O ( ) :
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
 if 6 - 6: iiII11i1I1IIi . iIi1i1ii1 * OOooOOo . ooOoO0O00
 if 98 - 98: ooOoO0O00
 if 65 - 65: OOooOOo / oO0o % iIi1i1ii1
def IiI111111IIII ( ) :
 I1 = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o00oooO0Oo = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiIi1iI in o00oooO0Oo :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   iIiIIii = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOOiiiiI ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iIiIIii + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0oO0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0oO0 == 0 :
    OOo00 ( IIiIi1iI )
    o00O0 ( )
   elif O0oO0 == 1 :
    iIII ( IIiIi1iI )
  else :
   pass
   if 48 - 48: iI11I1II1I1I % ooOoO0O00 % iiII11i1I1IIi + OOoOoo
def iIII ( addon ) :
 iIiIIii = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 30 - 30: Ii % iI11I1II1I1I . oo0oO00 % iI11I1II1I1I
def OOo00 ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOO00oO00O0OO = os . path . join ( iIi1ii1I1 , 'default.py' )
 oOo00OO = open ( oOO00oO00O0OO , "w+" )
 if 93 - 93: oo0oO00 - iI11I1II1I1I
 oOo00OO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oOo00OO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oOo00OO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 39 - 39: I11i * OOoOoo + IIi * IIiIiII11i
 if 97 - 97: iI11I1II1I1I + oo0oO00 + IIiIiII11i % iIi1i1ii1 % OooOO000 % O0oOO0
 if 21 - 21: oOo0O0Ooo / OOoOoo % OOoOoo - I11i
 if 70 - 70: I1ii11iIi11i . OOooOOo
def O00o00O ( ) :
 I1 = O0 ( 'http://www.tvcatchup.com/channels/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for ii1iii11i1 , ooI1111i , ooO0oOOooOo0 in o00oooO0Oo :
  oOOO00o000o ( ii1iii11i1 , 'http://www.tvcatchup.com' + ooO0oOOooOo0 , 90024 , 'http://www.tvcatchup.com' + ooI1111i )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def I11Oo00oO0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
  if 96 - 96: Ii1I / IIiIiII11i . IIi - iiII11i1I1IIi * oo0oO00 * O0oOO0
def O0O0Oo00 ( ) :
 iIIII1iIIii ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O0 ( 'http://www.join4films.com/' )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def O00oo0ooO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , url , 80007 , ooI1111i )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def iiIii1ii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in o00oooO0Oo :
  url = ( url ) . replace ( ' ' , '%20' )
  Ii1IIiI1i ( url )
def iIIIII1iiiiII ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i1I1 = 'http://www.join4films.com/?s=' + ( oooO ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0o00OOo00O0O = I111i1I1 . lower ( )
 O00oo0ooO ( O0o00OOo00O0O )
 if 5 - 5: I11i / ii * I11i * o0o00Oo0O . IIi % iIi1i1ii1
 if 43 - 43: I11i
 if 71 - 71: O0oOO0 % oo0oO00 * OOooOOo . o0o00Oo0O / IIi . Ii1I
 if 58 - 58: I1ii11iIi11i / O0oOO0
 if 44 - 44: Oooo0O0oo00oO
 if 54 - 54: IIi - oo0oO00 - OooOO000 . iI11I1II1I1I
 if 79 - 79: IIi . oO0o
 if 40 - 40: I11i + I1ii11iIi11i . I11i % OOoOoo
 if 15 - 15: IIi * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 if 60 - 60: oOo0O0Ooo * OooOO000 % oO0o + O0oOO0
 if 52 - 52: ooOoO0O00
 if 84 - 84: IIi / iIi1i1ii1
 if 86 - 86: OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % iI11I1II1I1I / Oooo0O0oo00oO
 if 11 - 11: oOo0O0Ooo * O0oOO0 + Ii1I / Ii1I
 if 37 - 37: Ii + ooOoO0O00
 if 23 - 23: iiII11i1I1IIi + oo0oO00 . OOooOOo * oOo0O0Ooo + Ii1I
 if 18 - 18: iIi1i1ii1 * I11i . iIi1i1ii1 / o0o00Oo0O
def iiIII1II ( ) :
 I1IiiiiI ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 I1IiiiiI ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
 if 100 - 100: I1ii11iIi11i % IIi / oo0oO00
def iIII11Ii ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i1I1 = 'http://imoviemax.se/?s=' + ( oooO ) . replace ( ' ' , '+' )
 O0o00OOo00O0O = I111i1I1 . lower ( )
 o0O0 ( O0o00OOo00O0O )
def ooOoOo ( url ) :
 IIIi1i = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , Oo0O00O000 , O0oOoOOO0OO in o00oooO0Oo :
  if Oo0O00O000 in IIIi1i :
   pass
  else :
   I1IiiiiI ( Oo0O00O000 + ' - ' + O0oOoOOO0OO + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
   IIIi1i . append ( Oo0O00O000 )
   if 91 - 91: iIi1i1ii1 + OOooOOo + I11i - iI11I1II1I1I
def iiiI1ii11 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 , ii1i in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 + ' - Views:' + ii1i , url , 10075 , oOOOo00O00oOo + 'genievision.png' , OO0o , '' )
  if 5 - 5: O0oOO0 . Ii1I . IIiIiII11i . ii
  if 96 - 96: Ii - Oooo0O0oo00oO % o0o00Oo0O / oO0o
def o0O0 ( url ) :
 O0O0 = [ ]
 I1 = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IiiiiI ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , Oo0O00O000 , url in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 10075 , ooI1111i , ooI1111i , '' )
  O0O0 . append ( Oo0O00O000 )
  if 83 - 83: IIiIiII11i - oo0oO00
def iiIii1IIi ( img , name , url ) :
 img = img
 name = name
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for ii1IiIiI1 , url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OOOoOo00O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OOOoOo00O
  O0ooOo0o0Oo = ( ii1IiIiI1 ) . replace ( 'play-' , 'Server ' )
  o0OIiII ( O0ooOo0o0Oo , OOOoOo00O , 10076 , img , img , '' )
  if 71 - 71: iI11I1II1I1I - Oooo0O0oo00oO . oOo0O0Ooo % ii + Oooo0O0oo00oO
def IIi11I1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for O0o0OO0000ooo in o00oooO0Oo :
  if '=m' in O0o0OO0000ooo :
   iiiI111I ( O0o0OO0000ooo )
  elif 'php' in O0o0OO0000ooo :
   IIi11I1 ( url )
  else :
   I1 = O0 ( O0o0OO0000ooo )
   o00oooO0Oo = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for oooOOO00o0 in o00oooO0Oo :
    iiiI111I ( O0o0OO0000ooo )
    if 1 - 1: iI11I1II1I1I
    if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
    if 99 - 99: oo0oO00 - OooOO000 - O0oOO0 % oO0o
def IiiIIiiiiii ( url ) :
 I1 = O0 ( url )
 OOOO0o = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoo , i1I1iIi1IiI in OOOO0o :
  print 'there ><><><><><><><><><><><><'
  OOoo = OOoo
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I1iIi1IiI ) )
  for Oo0O00O000 , i1111O0O000OOOo in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + OOoo + '[/COLOR] - ' + Oo0O00O000 + ' - [COLOR' + iiI1IiI + ']' + i1111O0O000OOOo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
 O0iII1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoo , i11ii1Ii1 in O0iII1 :
  print 'there ><><><><><><><><><><><><'
  OOoo = OOoo
  o00oooO0Oo = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i11ii1Ii1 ) )
  for Oo0O00O000 , i1111O0O000OOOo in o00oooO0Oo :
   print 'here <><><><><><><><><><><><>'
   I1IiiiiI ( '[COLORred]' + OOoo + '[/COLOR] - ' + Oo0O00O000 + ' - [COLOR' + iiI1IiI + ']' + i1111O0O000OOOo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , OO0o , '' )
   if 25 - 25: Oooo0O0oo00oO
   if 83 - 83: OooOO000
   if 48 - 48: IIiIiII11i * Oooo0O0oo00oO * OooOO000
def i1Iii11I1i ( url ) :
 I1 = O0 ( url )
 O0iII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for O0iII1 in O0iII1 :
  Oo0O00O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0iII1 ) )
  for Oo0O00O000 in Oo0O00O000 :
   Oo0O00O000 = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0iII1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IiII1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0iII1 ) )
  for IiII1 in IiII1 :
   IiII1 = 'http:' + IiII1
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , '' , '' )
  if 50 - 50: iIi1i1ii1 % ooOoO0O00
  if 21 - 21: ii - iI11I1II1I1I
  if 93 - 93: O0oOO0 - I11i % OOooOOo . OOooOOo - OOoOoo
  if 90 - 90: OOoOoo + IIiIiII11i * Ii1I / IIi . I11i + I11i
def oOoO00o ( url ) :
 if 40 - 40: OOoOoo / OOooOOo % Ii % Ii1I / oOo0O0Ooo
 ooOOOOo0 = [ ]
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ooI1111i , Oo0O00O000 , IiiIi in o00oooO0Oo :
  Oo0O00O000 = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O0 ( O0o0OO0000ooo )
  o0O0OOO0Ooo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for OO00O0oOO , iII1111III1I in o0O0OOO0Ooo :
   iIIi = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iII1111III1I ) )
   for I1iIi1iIiiIiI in iIIi :
    if Oo0O00O000 in ooOOOOo0 :
     pass
    else :
     o0OIiII ( Oo0O00O000 , OO00O0oOO , 8043 , ooI1111i , ooI1111i , I1iIi1iIiiIiI )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
     ooOOOOo0 . append ( Oo0O00O000 )
     if 96 - 96: iiII11i1I1IIi
     if 18 - 18: iiII11i1I1IIi * oo0oO00 - IIi
def II1i1III ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , I1i1i1 , I1iIi1iIiiIiI , ooO0oooOO0 , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 10065 , I1i1i1 , ooO0oooOO0 , I1iIi1iIiiIiI )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 34 - 34: OooOO000 - Ii / iI11I1II1I1I
def OOOo ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i1I1 = 'https://www.youtube.com/results?search_query=' + ( oooO ) . replace ( ' ' , '+' )
 O0o00OOo00O0O = I111i1I1 . lower ( )
 I1 = O0 ( O0o00OOo00O0O )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for ooO0oOOooOo0 in next :
  ooO0oOOooOo0 = 'https://www.youtube.com' + ooO0oOOooOo0
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , ooO0oOOooOo0 , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 , oO00OoOoo0 , iII1111III1I in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0O00O000 )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  IiII1 = 'http:' + ( ooI1111i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiII1
  ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
  o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , IiII1 , iII1111III1I )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 , oO00OoOoo0 in o00oooO0Oo :
   print 'im doing it'
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   IiII1 = 'http:' + ( ooI1111i ) . replace ( 'https:' , '' )
   ooO0oOOooOo0 = 'http://www.youtube.com' + ooO0oOOooOo0
   if '&' in ooO0oOOooOo0 :
    print ' i got here'
    I1 = O0 ( ooO0oOOooOo0 )
    O0iII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for O0iII1 in O0iII1 :
     Oo0O00O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0iII1 ) )
     for Oo0O00O000 in Oo0O00O000 :
      Oo0O00O000 = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     ooO0oOOooOo0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0iII1 ) )
     for ooO0oOOooOo0 in ooO0oOOooOo0 :
      ooO0oOOooOo0 = 'https://www.youtube.com/w' + ooO0oOOooOo0
     IiII1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0iII1 ) )
     for IiII1 in IiII1 :
      IiII1 = 'http:' + IiII1
     o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , OO0o , '' )
   elif Oo0O00O000 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in ooO0oOOooOo0 or 'elete' in Oo0O00O000 :
    pass
   elif 'hannel' in ooO0oOOooOo0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + ooO0oOOooOo0
    I1 = O0 ( ooO0oOOooOo0 )
    I1iiiiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 in I1iiiiii :
     if 'outube' in ooO0oOOooOo0 or 'list' in ooO0oOOooOo0 :
      pass
     elif 'atch' in ooO0oOOooOo0 :
      ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooI1111i , 'http:' + ooI1111i , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , IiII1 , '' )
    if 65 - 65: iIi1i1ii1 + I1ii11iIi11i
def Ooo0O0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IiiiiI ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 for ooI1111i , url , Oo0O00O000 , oO00OoOoo0 , iII1111III1I in o00oooO0Oo :
  IIiiiiiiIi1I1 . append ( Oo0O00O000 )
  Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
  IiII1 = 'http:' + ( ooI1111i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiII1
  url = 'http://www.youtube.com' + url
  o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , IiII1 , iII1111III1I )
 else :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for ooI1111i , url , Oo0O00O000 , oO00OoOoo0 in o00oooO0Oo :
   Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
   IiII1 = 'http:' + ( ooI1111i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O0 ( url )
    O0iII1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for O0iII1 in O0iII1 :
     Oo0O00O000 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O0iII1 ) )
     for Oo0O00O000 in Oo0O00O000 :
      Oo0O00O000 = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O0iII1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IiII1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O0iII1 ) )
     for IiII1 in IiII1 :
      IiII1 = 'http:' + IiII1
     o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , OO0o , '' )
   elif Oo0O00O000 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in Oo0O00O000 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O0 ( url )
    I1iiiiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for ooI1111i , url , Oo0O00O000 in I1iiiiii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooI1111i , 'http:' + ooI1111i , '' )
     else :
      pass
   else :
    o0OIiII ( '[COLORred]' + oO00OoOoo0 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 , IiII1 , '' )
    if 71 - 71: ii
    if 11 - 11: iIi1i1ii1
def O00Ooo ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  o0oooO = open ( O000oo0O )
  o00oooO0Oo = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o0oooO ) )
  for ooOo , o0oO0OoO0 in o00oooO0Oo :
   if ooOo == 'needs replacing' or o0oO0OoO0 == 'needs replacing' :
    oOOOOOoOO ( )
    if 81 - 81: IIiIiII11i + Ii / iiII11i1I1IIi
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , OO0o , '' )
  if 85 - 85: Ii + OooOO000 * OOooOOo
def iiiII ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 oOOOOOoOO ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 57 - 57: oo0oO00 . I1ii11iIi11i + IIiIiII11i
def i111i11I1ii ( ) :
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
 if 64 - 64: O0oOO0 / Ii / I11i . ii
def i1iiIIi11I ( name ) :
 o0o0oOo000o0 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , ooI1111i , I1iI1I1 , ooO0oOOooOo0 in o00oooO0Oo :
  if o0o0oOo000o0 == 'Full List' :
   ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
   o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , ooI1111i , ooI1111i , '' )
  else :
   o0o0oOo000o0 = ( o0o0oOo000o0 ) . replace ( 'World' , 'القنوات العربية' )
   if o0o0oOo000o0 in I1iI1I1 :
    ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
    print ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , ooI1111i , ooI1111i , '' )
   else :
    pass
    if 48 - 48: oOo0O0Ooo / Ii - I11i * O0oOO0 / ii
def OoOo ( name ) :
 o0o0oOo000o0 = name
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , ooI1111i , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 ) . replace ( '.ts' , '.m3u8' )
  o0OIiII ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( ooO0oOOooOo0 ) . strip ( ) , 10012 , ooI1111i , ooI1111i , '' )
 else :
  o0OIiII ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 17 - 17: IIi . Ii
  if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . OooOO000 - OOoOoo
  if 63 - 63: O0oOO0
  if 71 - 71: ooOoO0O00 . IIi * iiII11i1I1IIi % ii + Oooo0O0oo00oO
  if 36 - 36: iIi1i1ii1
  if 49 - 49: Oooo0O0oo00oO / ii / oOo0O0Ooo
  if 74 - 74: OooOO000 % Ii1I
  if 7 - 7: IIiIiII11i
  if 27 - 27: O0oOO0 . ii + Ii
  if 86 - 86: oo0oO00 / I11i - I11i + Ii1I + O0oOO0
  if 33 - 33: I11i . iiII11i1I1IIi . iIi1i1ii1 . ooOoO0O00
  if 49 - 49: Ii1I
def oo0 ( ) :
 I1IiiiiI ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IiiiiI ( 'Backup Genie Favourites' , ooO0oOOooOo0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( o00OO00OoO ) :
  I1IiiiiI ( 'Backup Ivue Config' , o00OO00OoO , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( OOOO0OOoO0O0 ) :
  I1IiiiiI ( 'Backup Kodi Favourites' , OOOO0OOoO0O0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 84 - 84: oo0oO00 - I1ii11iIi11i / o0o00Oo0O - OooOO000
  if 21 - 21: o0o00Oo0O * o0o00Oo0O % Ii1I
  if 94 - 94: oo0oO00 + IIiIiII11i % Ii
zip = oo00 . getSetting ( 'zip' )
i1i1IiIiIi1Ii = xbmc . translatePath ( os . path . join ( zip ) )
def oO0ooOO ( ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 16 - 16: I1ii11iIi11i + OOoOoo / I1ii11iIi11i / oO0o % O0oOO0 % Ii1I
  if 22 - 22: IIiIiII11i * oO0o * oo0oO00 + Ii1I * I11i
  if 100 - 100: ooOoO0O00 / iIi1i1ii1
def IiII1iiIiI ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = O0Oo000ooO00
  elif 'Ivue' in name :
   url = o00OO00OoO
  elif 'Kodi' in name :
   url = OOOO0OOoO0O0
  oO0ooOO ( )
  ooO0000o00O = open ( url ) . read ( )
  O0Ooo = os . path . join ( i1i1IiIiIi1Ii , description . split ( 'Your ' ) [ 1 ] )
  oOOo0O00o = open ( O0Ooo , mode = 'w' )
  oOOo0O00o . write ( ooO0000o00O )
  oOOo0O00o . close ( )
 else :
  if 'guisettings.xml' in description :
   oO00oOOo0Oo = open ( os . path . join ( i1i1IiIiIi1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IIiIIIIii = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   o00oooO0Oo = re . compile ( IIiIIIIii ) . findall ( oO00oOOo0Oo )
   for type , iI , iI1 in o00oooO0Oo :
    iI1 = iI1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iI , iI1 ) )
  else :
   O0Ooo = os . path . join ( url )
   ooO0000o00O = open ( os . path . join ( i1i1IiIiIi1Ii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0O00o = open ( O0Ooo , mode = 'w' )
   oOOo0O00o . write ( ooO0000o00O )
   oOOo0O00o . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 14 - 14: Ii1I
 if 49 - 49: O0oOO0 / ooOoO0O00 % IIi . oOo0O0Ooo
 if 93 - 93: Oooo0O0oo00oO
 if 43 - 43: Ii1I / oOo0O0Ooo . OOoOoo
def Ooo0oO0 ( ) :
 o0Oo0oOooOoOo = 1
 oO0ooOO ( )
 I1i = xbmc . translatePath ( os . path . join ( i1i1IiIiIi1Ii , 'Build Backup' , 'Full Backup' , '' ) )
 Oo = xbmc . translatePath ( os . path . join ( i1i1IiIiIi1Ii , 'Build Backup' , 'my_full_backup.zip' ) )
 IiIiIi1I1 = xbmc . translatePath ( os . path . join ( i1i1IiIiIi1Ii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1i ) :
  os . makedirs ( I1i )
 IiI1ii1Ii = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IiI1ii1Ii ) : return False , 0
 oooOOOoOOOo0O = IiI1ii1Ii
 O00oOoo0OoO0 = xbmc . translatePath ( os . path . join ( I1i , oooOOOoOOOo0O + '.zip' ) )
 Ooo0 = [ 'plugin.video.GenieTv' ]
 oooO00o0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0o00oO0oo000 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oO000o = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0Oo = "Creating full backup of existing build"
 o0O0I1I1Iiii1 = "Creating Community Build"
 i111i1 = "Archiving..."
 OoOoOo0 = ""
 i1II11II1 = "Please Wait"
 II1IIIii ( I11 , O00oOoo0OoO0 , o0O0I1I1Iiii1 , i111i1 , OoOoOo0 , i1II11II1 , o0o00oO0oo000 , oO000o )
 time . sleep ( 1 )
 iIIIiIi1I1i = xbmc . translatePath ( os . path . join ( I1i , oooOOOoOOOo0O + '_guisettings.zip' ) )
 OoOOoO0oOo = zipfile . ZipFile ( iIIIiIi1I1i , mode = 'w' )
 try :
  OoOOoO0oOo . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 OoOOoO0oOo . close ( )
 if o0Oo0oOooOoOo == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + Oo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O00oOoo0OoO0 + '[/COLOR]' )
  if 70 - 70: oo0oO00 % iI11I1II1I1I . I1ii11iIi11i + I1ii11iIi11i - I11i % OooOO000
def II1IIIii ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i1IIi1i1Ii1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Iii = len ( sourcefile )
 o0Oo0oO = [ ]
 iIII1iiIi11 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for ooOo0O0O0oOO0 , iIiIIi , III1I in os . walk ( sourcefile ) :
  for file in III1I :
   iIII1iiIi11 . append ( file )
 I1I111iIi = len ( iIII1iiIi11 )
 for ooOo0O0O0oOO0 , iIiIIi , III1I in os . walk ( sourcefile ) :
  iIiIIi [ : ] = [ OoOOOO for OoOOOO in iIiIIi if OoOOOO not in exclude_dirs ]
  III1I [ : ] = [ oOOo0O00o for oOOo0O00o in III1I if oOOo0O00o not in exclude_files ]
  for file in III1I :
   o0Oo0oO . append ( file )
   I1iiIi111I = len ( o0Oo0oO ) / float ( I1I111iIi ) * 100
   o0oOoO00o . update ( int ( I1iiIi111I ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   Iiii1iIii = os . path . join ( ooOo0O0O0oOO0 , file )
   if not 'temp' in iIiIIi :
    if not 'plugin.program.originwizard' in iIiIIi :
     import time
     oOoooO000O = '01/01/1980'
     III1I11i1iIi = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Iiii1iIii ) ) )
     if III1I11i1iIi > oOoooO000O :
      i1IIi1i1Ii1 . write ( Iiii1iIii , Iiii1iIii [ Iii : ] )
 i1IIi1i1Ii1 . close ( )
 o0oOoO00o . close ( )
 if 69 - 69: I1ii11iIi11i * IIiIiII11i * OOoOoo . iiII11i1I1IIi - Ii1I
 if 39 - 39: IIi * oOo0O0Ooo % oO0o . OOooOOo
def iIi1Ii1i1iI ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , OO0o , '' )
 if 24 - 24: ooOoO0O00 * iI11I1II1I1I / IIi
 if 78 - 78: Ii + I11i + OooOO000 / I11i % iI11I1II1I1I % iIi1i1ii1
def Oo0O0Oo00O ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Search Genie[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  I1ii1ii11i1I ( )
 if O0oO0 == 1 :
  oooooo0OO ( )
 if O0oO0 == 2 :
  I1oOO0o0 ( )
 if O0oO0 == 3 :
  OOOo ( )
  if 9 - 9: I11i . oOo0O0Ooo - Ii1I
  if 32 - 32: ii / oOo0O0Ooo / iI11I1II1I1I + IIiIiII11i . O0oOO0 . I11i
  if 21 - 21: iI11I1II1I1I / IIiIiII11i % ooOoO0O00
  if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
  if 43 - 43: Ii1I - iiII11i1I1IIi
  if 70 - 70: iiII11i1I1IIi / Oooo0O0oo00oO % OOoOoo - IIi
  if 47 - 47: iiII11i1I1IIi
  if 92 - 92: Oooo0O0oo00oO + OOooOOo % ooOoO0O00
  if 23 - 23: OooOO000 - Oooo0O0oo00oO + IIi - OOooOOo * OOooOOo . I1ii11iIi11i
def iIii11iI1II ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   IIi1i1I11Iii ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , I1i1i1 , Oo0O00O000 )
  if O0oO0 == 1 :
   Parse . ParseURL ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) )
  if O0oO0 == 2 :
   I1II1I1I ( )
  if O0oO0 == 3 :
   OOo0 ( )
  if O0oO0 == 4 :
   oOO0o0oo0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0oO0 == 5 :
   oOo000O ( )
  if O0oO0 == 6 :
   iII ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0oO0 == 7 :
   ooO0o0O0Oo ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0oO0 == 8 :
   IiiIIi ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0oO0 == 9 :
   O00o0O ( )
  if O0oO0 == 10 :
   iIIIiI ( )
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
  if 93 - 93: OOoOoo . iI11I1II1I1I % Ii . OOooOOo % OOoOoo + o0o00Oo0O
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 65 - 65: IIi + oO0o - ii
def OOoOO0o ( ) :
 Oo00oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1I = [ '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE CACHE[/COLOR]' , '[COLOR' + iiI1IiI + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + iiI1IiI + ']FORCE REFRESH[/COLOR]' , '[COLOR' + iiI1IiI + ']CHECK MY IP[/COLOR]' , '[COLOR' + iiI1IiI + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Maintenance[/COLOR]' , ii1I )
  if O0oO0 == 0 :
   oO0O0oO0 ( )
  if O0oO0 == 1 :
   II1i111Ii1i ( )
  if O0oO0 == 2 :
   oOO0O00Oo0O0o ( )
  if O0oO0 == 3 :
   O0ooO0Oo00o ( ooO0oOOooOo0 )
  if O0oO0 == 4 :
   I11Ii1iI11iI1 ( ooO0oOOooOo0 )
  if O0oO0 == 5 :
   o00O0 ( )
  if O0oO0 == 6 :
   i1III1 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0oO0 == 7 :
   Iii111IiIii ( )
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
  if 100 - 100: IIiIiII11i - I11i . IIiIiII11i * IIiIiII11i . iIi1i1ii1
  if 2 - 2: ii
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 60 - 60: oO0o
 if 81 - 81: OOooOOo % IIi
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
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % IIi - iI11I1II1I1I
def i11II ( ) :
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
 if 71 - 71: iIi1i1ii1 . OooOO000 . oO0o
def oOOOoo00 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , OO0o , '' )
 o0OIiII ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , OO0o , '' )
 if 68 - 68: Ii % O0oOO0 * oO0o * iIi1i1ii1 * IIiIiII11i + o0o00Oo0O
def o00OoO0oO00 ( ) :
 Oo00oo0oO ( )
 o0OIiII ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , OO0o , '' )
 o0OIiII ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , OO0o , '' )
 o0OIiII ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , OO0o , '' )
 if 2 - 2: iI11I1II1I1I
 if 45 - 45: ii / Ii
 if 10 - 10: iiII11i1I1IIi - O0oOO0 * iI11I1II1I1I % iI11I1II1I1I * iIi1i1ii1 - Ii1I
def OoOoO ( ) :
 Oo00oo0oO ( )
 ii1I = [ '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  OoO0O0oO00 ( )
 if O0oO0 == 0 :
  i1i1 ( ooO0oOOooOo0 )
 if O0oO0 == 0 :
  i1IiIi1 ( ooO0oOOooOo0 )
  if 22 - 22: oo0oO00 * o0o00Oo0O . IIiIiII11i - oO0o
  if 90 - 90: O0oOO0
  if 94 - 94: oo0oO00 / Ii1I * OooOO000 - OOooOOo
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 44 - 44: IIi % Ii - iiII11i1I1IIi * Ii1I + I1ii11iIi11i * Oooo0O0oo00oO
def IiI1iI1IiiIi1 ( ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o00oooO0Oo = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O0o0O00Oo0o0 )
 for ooI1111i , Oo0O00O000 in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , ooI1111i , ooI1111i , '' )
 Iii1I1I11iiI1 ( 'tvshows' , 'INFO' )
 if 90 - 90: o0o00Oo0O + oo0oO00 - ii . oo0oO00
def oOII1ii1ii11I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( o0ooOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 5 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 71 - 71: ii
def OoO0O0oO00 ( ) :
 Oo00oo0oO ( )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , OO0o , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 5 - 5: OOooOOo % ii
def OO0 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I111i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 14 - 14: IIi % oOo0O0Ooo - iI11I1II1I1I . Oooo0O0oo00oO + oO0o - OooOO000
def iI1iIiiiI1I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + OOOOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 50 - 50: IIi - Ii + iI11I1II1I1I / o0o00Oo0O - IIi + I11i
def Iii111Ii1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + III11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 5 - 5: ii * OOooOOo % iIi1i1ii1 . Ii1I % oOo0O0Ooo
def I1ii1 ( url ) :
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 87 - 87: OOooOOo / iIi1i1ii1 + iI11I1II1I1I
def i1i1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oo0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 40 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 13 - 13: iI11I1II1I1I . OOooOOo * oOo0O0Ooo / O0oOO0 * IIi
def O00o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oO0o00ooO0OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 5 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 1 - 1: OOooOOo . Ii % OOooOOo - iiII11i1I1IIi % ooOoO0O00 + Ii1I
def oO0O0OO0O ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  IiiIiIi111iI1 ( )
 if O0oO0 == 1 :
  oOOO0o0ooOo ( )
 if O0oO0 == 2 :
  O0o00o000oO ( )
  if 62 - 62: Ii1I / oo0oO00 . ooOoO0O00
  if 99 - 99: OOooOOo . OooOO000
  if 59 - 59: oo0oO00 / I1ii11iIi11i / Oooo0O0oo00oO / o0o00Oo0O / OOooOOo + I11i
  if 13 - 13: I11i % O0oOO0 / OooOO000 % OooOO000 % o0o00Oo0O
def oOOO0o0ooOo ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , o0Ii1 in o00oooO0Oo :
  iIIII1iIIii ( 'Android Apps' + o0Ii1 , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for ooO0oOOooOo0 , o0Ii1 in o0O0OOO0Ooo :
  iIIII1iIIii ( 'Android Games' + o0Ii1 , 'https://www.apkfiles.com' + ooO0oOOooOo0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def IIi1IiII ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '/cat' in url :
   iIIII1iIIii ( ( Oo0O00O000 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def o0IIIIiI11I ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '/app' in url :
   iIIII1iIIii ( ( Oo0O00O000 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def iiiI11iIIi1 ( url ) :
 OO0O000 = O0 ( url )
 o00OoooooooOo = url
 if "page=" in str ( url ) :
  o00OoooooooOo = url . split ( '?' ) [ 0 ]
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if 'apk' in url :
   o0OIiII ( ( Oo0O00O000 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + ooI1111i )
 if len ( o0O0OOO0Ooo ) > 1 :
  o0O0OOO0Ooo = str ( o0O0OOO0Ooo [ len ( o0O0OOO0Ooo ) - 1 ] )
 o0OIiII ( 'Next Page' , o00OoooooooOo + str ( o0O0OOO0Ooo ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def iIii1I ( name , url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 name = name
 o00oooO0Oo = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  url = 'https://www.apkfiles.com' + url
  iii11i1 ( name , url , 'Brackets' )
def O0o00o000oO ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i1I1 = 'https://www.apkfiles.com/search?q=' + ( oooO ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0o00OOo00O0O = I111i1I1 . lower ( )
 iiiI11iIIi1 ( O0o00OOo00O0O )
 if 48 - 48: OOoOoo * Ii1I
def II111iIiI1Ii ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( Ii1iiII1i , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , Oo0O00O000 + '.apk' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 52 - 52: O0oOO0 / OooOO000
def o0Oi11i1I ( url ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , Oo0O00O000 + '.mp4' )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 100 - 100: iiII11i1I1IIi / oO0o * iI11I1II1I1I * o0o00Oo0O - ooOoO0O00
 if 48 - 48: o0o00Oo0O * IIi * oO0o . oO0o * oo0oO00 - IIi
def iIi11i ( name , url , description ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 Ii1I1Ii = os . path . join ( oOooO0 , name )
 try :
  os . remove ( Ii1I1Ii )
 except :
  pass
 downloader . download ( url , Ii1I1Ii , o0oOoO00o )
 ooIII1II1iii1i = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ooIII1II1iii1i
 print '======================================='
 extract . all ( Ii1I1Ii , ooIII1II1iii1i , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 75 - 75: iIi1i1ii1 - OOooOOo - iI11I1II1I1I % I11i
 if 58 - 58: o0o00Oo0O . iIi1i1ii1 / ii . oO0o / I1ii11iIi11i * IIiIiII11i
 if 53 - 53: IIi - o0o00Oo0O / I11i % iiII11i1I1IIi * oOo0O0Ooo % Oooo0O0oo00oO
 if 69 - 69: Ii1I
 if 83 - 83: I11i
def IiiIiIi111iI1 ( ) :
 O0o0O00Oo0o0 = O0 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00oooO0Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , ooO0oOOooOo0 , iii1 , ooO0oooOO0 , i1iiii in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ooO0oOOooOo0 , 80003 , iii1 , oOOOo00O00oOo + 'APKToolsB.png' , i1iiii )
def OOOO0oOo00O ( apk , ret = None ) :
 if apk == "kodi" :
  i1I1I1i1i1i = "https://kodi.tv/download/"
  O0o0O00Oo0o0 = O0 ( i1I1I1i1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( O0o0O00Oo0o0 )
  if len ( o00oooO0Oo ) == 1 :
   ii1o0oo0Ooooo0 = o00oooO0Oo [ 0 ] [ 0 ]
   oooOOOoOOOo0O = o00oooO0Oo [ 0 ] [ 1 ]
   Oo0oOo000OoO0 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( ii1o0oo0Ooooo0 , oooOOOoOOOo0O )
  if ret == 'version' : return ii1o0oo0Ooooo0
  else : return Oo0oOo000OoO0
 elif apk == "spmc" :
  IIii1I1i = 'https://github.com/koying/SPMC/releases/latest/'
  O0o0O00Oo0o0 = O0 ( IIii1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00oooO0Oo = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( O0o0O00Oo0o0 )
  ii1o0oo0Ooooo0 = re . sub ( '<[^<]+?>' , '' , o00oooO0Oo [ 0 ] ) . replace ( ' ' , '' )
  Oo0oOo000OoO0 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( ii1o0oo0Ooooo0 , ii1o0oo0Ooooo0 )
  if ret == 'version' : return ii1o0oo0Ooooo0
  else : return Oo0oOo000OoO0
def iii11i1 ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  IIII1iIIii = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not IIII1iIIii : IiiOooooOo0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I1ii1I1Ii = name
  if IIII1iIIii :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not o0000oO ( url ) == True : IiiOooooOo0 ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1ii1I1Ii , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    OoOOoO0oOo = zipfile . ZipFile ( Ii1I1Ii )
    for file in OoOOoO0oOo . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( oooOOOOO , os . path . basename ( file ) ) , 'wb' ) as oOOo0O00o :
       IiI = file . split ( '/' ) [ 1 ]
       oOOo0O00o . write ( OoOOoO0oOo . read ( file ) )
       xbmc . sleep ( 500 )
       oOOo0O00o . close ( )
       try :
        os . remove ( Ii1I1Ii )
       except :
        pass
       Ii1I1Ii = os . path . join ( oooOOOOO , IiI )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : IiiOooooOo0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : IiiOooooOo0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 60 - 60: OooOO000
 if 98 - 98: OOoOoo
 if 34 - 34: iI11I1II1I1I * oo0oO00 * oo0oO00 / Ii1I
 if 28 - 28: oO0o - O0oOO0 + OOooOOo + IIi / iI11I1II1I1I
def iiiii11I1 ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 O0o0O00Oo0o0 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( O0o0O00Oo0o0 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + ooO0oOOooOo0 )
  Ii1 ( ( Oo0O00O000 ) . replace ( '_' , ' ' ) , ooO0oOOooOo0 )
  if 77 - 77: Oooo0O0oo00oO / IIiIiII11i + iIi1i1ii1 + OOoOoo - Ii
def Ii1 ( name , url ) :
 if ii1iII1II ( ) == 'android' :
  IIII1iIIii = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not IIII1iIIii : IiiOooooOo0 ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1ii1I1Ii = name
  if IIII1iIIii :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not o0000oO ( url ) == True : IiiOooooOo0 ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1ii1I1Ii , '' , 'Please Wait' )
   Ii1I1Ii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( Ii1I1Ii )
   except : pass
   downloader . download ( url , Ii1I1Ii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + Ii1I1Ii + '")' )
  else : IiiOooooOo0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : IiiOooooOo0 ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 44 - 44: oOo0O0Ooo + OOooOOo + Ii1I . oOo0O0Ooo * OOooOOo % iI11I1II1I1I
 if 72 - 72: Oooo0O0oo00oO . Oooo0O0oo00oO - Ii1I
def III1II1i ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 5 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 3 - 3: iiII11i1I1IIi
 if 35 - 35: iIi1i1ii1 . o0o00Oo0O + I1ii11iIi11i + Oooo0O0oo00oO + ooOoO0O00
def II11IiIi11 ( url ) :
 O0o0O00Oo0o0 = O0 ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 30015 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
def Oo0O0OOO0o0O ( url , iconimage , fanart ) :
 O0o0O00Oo0o0 = O0 ( url )
 OOOoOo00O = url
 ooI1111i = iconimage
 fanart = fanart
 o00oooO0Oo = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for O0o0OO0000ooo , Oo0O00O000 in o00oooO0Oo :
  if '.mp4' in Oo0O00O000 :
   o0OIiII ( 'Watch VIDEO' , url + '/' + O0o0OO0000ooo , 222 , ooI1111i , fanart , '' )
  if 'description' in Oo0O00O000 :
   o0OIiII ( 'Read Description' , url + '/' + O0o0OO0000ooo , 30017 , ooI1111i , fanart , '' )
  if 'images' in Oo0O00O000 :
   I1IiiiiI ( 'View Images' , url + '/' + O0o0OO0000ooo , 30018 , ooI1111i , fanart , '' )
  if 'url' in Oo0O00O000 :
   o0OIiII ( 'Install Build On Android' , url + '/' + O0o0OO0000ooo , 30016 , ooI1111i , fanart , '' )
  if 'url' in Oo0O00O000 :
   o0OIiII ( 'Install Build On Pc' , url + '/' + O0o0OO0000ooo , 30019 , ooI1111i , fanart , '' )
 Iii1I1I11iiI1 ( 'movies' , 'INFO' )
 if 51 - 51: O0oOO0 + oO0o + iiII11i1I1IIi + iiII11i1I1IIi % I11i
def iIi1i1iIi1Ii1 ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  oOOoOOO0oo0 ( url )
  if 87 - 87: OOoOoo / OOooOOo % I11i * O0oOO0
def oOOOoo0o ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for url in o00oooO0Oo :
  iiiI1IiIIii ( url )
  if 25 - 25: Ii1I + O0oOO0 + ii . IIiIiII11i . iiII11i1I1IIi
def o0Oo0oO00OOO ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( 'desc="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Iii11I111i in o00oooO0Oo :
  OOOiiiiI ( 'Description:' , Iii11I111i )
  if 89 - 89: iiII11i1I1IIi . oOo0O0Ooo
def ooOoo0OoOO ( url ) :
 O0o0O00Oo0o0 = O0 ( url )
 url = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( O0o0O00Oo0o0 )
 for O0o0OO0000ooo , Oo0O00O000 in o00oooO0Oo :
  if 'png' in Oo0O00O000 :
   o0OIiII ( 'image' , '' , '' , url + '/' + O0o0OO0000ooo , url + '/' + O0o0OO0000ooo , '' )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 38 - 38: oO0o / OOoOoo % OooOO000 * oo0oO00 + Ii % OOoOoo
def O000oOo0O ( name , url , description ) :
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
 if 82 - 82: iIi1i1ii1
 if 86 - 86: I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
def iiiI1IiIIii ( url ) :
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
 oO0O0oO0 ( )
 if 83 - 83: iIi1i1ii1 / OooOO000
def oOOoOOO0oo0 ( url ) :
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
 oO0O0oO0 ( )
 if 64 - 64: oO0o % iIi1i1ii1 . OooOO000 % oO0o + oo0oO00 * iIi1i1ii1
def OOOO00OooO ( name , url , description ) :
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
 oO0O0oO0 ( )
 if 64 - 64: oO0o . oOo0O0Ooo - ii . OOoOoo - iiII11i1I1IIi
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
  O0oO0o000o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oOOo0O00o . write ( O0oO0o000o . rstrip ( '\r\n' ) + '\n' )
def oO0O0oO0 ( ) :
 O0oO0 = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0oO0 == 0 : return
 elif O0oO0 == 1 : pass
 i11i11II11i1 = ii1iII1II ( )
 ii1 ( "Platform: " + str ( i11i11II11i1 ) )
 os . _exit ( 1 )
 ii1 ( "Force close failed!  Trying alternate methods." )
 if i11i11II11i1 == 'osx' :
  ii1 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i11i11II11i1 == 'linux' :
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
 elif i11i11II11i1 == 'android' :
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
 elif i11i11II11i1 == 'windows' :
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
  if 17 - 17: IIiIiII11i + I1ii11iIi11i . OooOO000
  if 12 - 12: OooOO000 + Oooo0O0oo00oO + oo0oO00 . iIi1i1ii1 / IIi
  if 29 - 29: iIi1i1ii1 . OOoOoo - IIiIiII11i
def i1IiIi1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooooO0 , iIiIIi , III1I in os . walk ( url ) :
  for file in III1I :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oO00oOOo0Oo = open ( ( os . path . join ( ooooO0 , file ) ) ) . read ( )
    Iiii111 = oO00oOOo0Oo . replace ( I11 , 'special://home/' )
    oOOo0O00o = open ( ( os . path . join ( ooooO0 , file ) ) , mode = 'w' )
    oOOo0O00o . write ( str ( Iiii111 ) )
    oOOo0O00o . close ( )
 oO0O0oO0 ( )
 if 71 - 71: o0o00Oo0O / oOo0O0Ooo . OooOO000 / OooOO000 * OOoOoo
def I1II1I1I ( ) :
 iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 60 - 60: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + Ii1I * Ii1I
def I1iiIiiii1111 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def I1ii1i11i ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def Oooooo0O00o ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o0O0OOO0Ooo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']Filter - ' + Oo0O00O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0O00O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , ooI1111i )
def II11ii1 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def ii1II1II ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO
 i11i11II11i = 'https://www.radionomy.com/en/search/index?query=' + ( oooO ) . replace ( ' ' , '+' )
 I1 = O0 ( i11i11II11i )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']Stream - ' + Oo0O00O000 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + ooO0oOOooOo0 , 70005 , ooI1111i )
  if 9 - 9: OOooOOo - Ii1I * OOoOoo . OOoOoo - oOo0O0Ooo
  if 74 - 74: Ii1I * Ii / oOo0O0Ooo - o0o00Oo0O . OOoOoo
def oOo000O ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , 'http://www.listenlive.eu/' + ooO0oOOooOo0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def oOO0o0oo0 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 39 - 39: OOoOoo / o0o00Oo0O * iIi1i1ii1
def I1IiI ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.toonjet.com/' + ooO0oOOooOo0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iI1 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OO0O000 )
 for url , ooI1111i in o00oooO0Oo :
  if 'ol.gif' in ooI1111i :
   pass
  elif 'link_block_' in ooI1111i :
   pass
  elif '.png' in ooI1111i :
   pass
  else :
   iIIII1iIIii ( ( ooI1111i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in o0O0OOO0Ooo :
  iIIII1iIIii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOO00OOOoOO ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 23 - 23: OOooOOo . I11i - oO0o / OOooOOo * iI11I1II1I1I
  if 13 - 13: I11i * Ii / Ii . oO0o . Oooo0O0oo00oO . Ii1I
def iIIIiI ( ) :
 iIIiIi ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 iIIiIi ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 88 - 88: OOooOOo - Oooo0O0oo00oO
def o0oo0O0oOoooO ( ) :
 iIIiIi ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iIIiIi ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 iIIiIi ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 70 - 70: O0oOO0 * O0oOO0 + I1ii11iIi11i * Oooo0O0oo00oO % oOo0O0Ooo + iI11I1II1I1I
def i1oOOO0ooOO ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0O00O000 , ooO0oOOooOo0 , i11IiI1iiI11 in o00oooO0Oo :
  if 'Parent' in Oo0O00O000 :
   pass
  elif '2' in i11IiI1iiI11 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: Ii1I - OOooOOo / Ii1I + Oooo0O0oo00oO - iiII11i1I1IIi
def IIii1III ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0O00O000 , ooO0oOOooOo0 , i11IiI1iiI11 in o00oooO0Oo :
  if oooO in Oo0O00O000 . lower ( ) :
   if '1' in i11IiI1iiI11 :
    iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in i11IiI1iiI11 :
    iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in i11IiI1iiI11 :
    iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 94 - 94: Ii % ii / oOo0O0Ooo
    if 24 - 24: oOo0O0Ooo * O0oOO0
def Oo0 ( ) :
 I1 = O0 ( ooooooO0oo + 'books' + IIIII )
 o00oooO0Oo = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for Oo0O00O000 , ooO0oOOooOo0 , i11IiI1iiI11 in o00oooO0Oo :
  if '1' in i11IiI1iiI11 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in i11IiI1iiI11 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in i11IiI1iiI11 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , ooO0oOOooOo0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 96 - 96: oo0oO00 % IIi % O0oOO0 * oo0oO00 / Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iI11I1II1I1I - oO0o
def ooo0 ( url ) :
 O0o0OO0000ooo = url
 I1 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0O00O000 in o0O0OOO0Ooo :
  if 'mp3' in Oo0O00O000 :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0o0OO0000ooo + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Oo0O00O000 :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0o0OO0000ooo + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Oo0O00O000 :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , O0o0OO0000ooo + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in Oo0O00O000 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0o0OO0000ooo + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: iiII11i1I1IIi
   if 90 - 90: o0o00Oo0O
   if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + iIi1i1ii1
def iI111II1ii ( url ) :
 I1 = O0 ( url )
 O0o0OO0000ooo = url
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if 'Parent' in Oo0O00O000 :
   pass
  elif '.db' in Oo0O00O000 :
   pass
  elif '.jpg' in Oo0O00O000 :
   pass
  elif '.html' in Oo0O00O000 :
   pass
  elif '.doc' in Oo0O00O000 :
   pass
  elif 'mp3' in Oo0O00O000 :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0o0OO0000ooo + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Oo0O00O000 :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0o0OO0000ooo + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , O0o0OO0000ooo + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: iiII11i1I1IIi * iI11I1II1I1I . iIi1i1ii1 - ii * IIiIiII11i
   if 45 - 45: o0o00Oo0O % oOo0O0Ooo - iiII11i1I1IIi . oO0o
def I1II ( ) :
 iIIiIi ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iIIiIi ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 iIIiIi ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 9 - 9: I1ii11iIi11i % ii - IIi
def iIII11Iiii1 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i in o00oooO0Oo :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + ooO0oOOooOo0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in ooI1111i :
   pass
  else :
   iIIiIi ( ooI1111i , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( ooO0oOOooOo0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + ooI1111i + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 95 - 95: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: o0o00Oo0O
 if 76 - 76: OooOO000 - O0oOO0 . Oooo0O0oo00oO % I11i
def iIi11iiI11 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '</a>' in Oo0O00O000 :
   pass
  elif '(' in Oo0O00O000 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 45 - 45: IIi - Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . oo0oO00 % OOoOoo . IIiIiII11i
def I1ii1Ii1 ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if oooO in Oo0O00O000 . lower ( ) :
   if '</a>' in Oo0O00O000 :
    pass
   elif '(' in Oo0O00O000 :
    iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 73 - 73: o0o00Oo0O . O0oOO0 + Ii + iI11I1II1I1I - oo0oO00 / OOooOOo
    if 99 - 99: Ii1I * O0oOO0 * Ii1I - IIiIiII11i + IIi
def OOooO0Oo00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o00oooO0Oo = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if '</a>' in Oo0O00O000 :
   pass
  elif '(' in Oo0O00O000 :
   iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + ooO0oOOooOo0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: iIi1i1ii1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: I11i + I11i - I1ii11iIi11i
 if 27 - 27: oO0o + OOooOOo * OOoOoo
def o0oOoO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in o00oooO0Oo :
  O0o0OO0000ooo = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( O0o0OO0000ooo )
  if 75 - 75: OOoOoo + oO0o - Ii1I . ii . OOoOoo + oOo0O0Ooo
def IIiO0Oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for Oo0O00O000 , url in o00oooO0Oo :
  if '<p align' in Oo0O00O000 :
   pass
  elif '&nbsp;' in Oo0O00O000 :
   pass
  else :
   I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: Ii1I + OooOO000 - OOooOOo % O0oOO0 % I11i % OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: oOo0O0Ooo * Oooo0O0oo00oO % oO0o
 if 24 - 24: OOoOoo - oo0oO00 * O0oOO0
def iiI11I1i1i1iI ( ) :
 I1 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o00oooO0Oo = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'ongoing' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Disney.png' , '' , '' )
  if 'genre' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Genre.png' , '' , '' )
  if 'years' in ooO0oOOooOo0 :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 21005 , oOOOo00O00oOo + 'Years.png' , '' , '' )
def O00OoOoO ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 ooO0o0oo = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , ooI1111i , ooI1111i , Oo0O00O000 )
 for url , Oo0O00O000 in ooO0o0oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def o0O0OOo0oO ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 IIi1IIIIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 Iiiii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 iiIIiiIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in Iiiii :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , Oo0O00O000 in IIi1IIIIi :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def i1ii1I ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 50 - 50: iI11I1II1I1I + OOooOOo . OOooOOo + ooOoO0O00 + iIi1i1ii1
def iiI1II11II1i ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 o00oooO0Oo = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if '9cart' in ooO0oOOooOo0 :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 27 - 27: ooOoO0O00 % IIi - oO0o / O0oOO0 . OOoOoo / I1ii11iIi11i
def OO0OoO0o ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 ii1iii1i = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if '9cart' in url :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in o0O0OOO0Ooo :
  if '9cart' in url :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , Oo0O00O000 in ii1iii1i :
  if '9cart' in url :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 98 - 98: OooOO000
def IIIIIIi1IiIi ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 20003 , ooI1111i )
 for url , Oo0O00O000 in o0O0OOO0Ooo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 14 - 14: oO0o / OOoOoo - Oooo0O0oo00oO / oOo0O0Ooo
def Ii1IIIi ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'Watch' in url :
   iIIII1iIIii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 70 - 70: OOooOOo . Oooo0O0oo00oO * iIi1i1ii1 + oo0oO00
def OOoo000O00O ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 18 - 18: Ii % OooOO000 + ooOoO0O00 + IIiIiII11i . OooOO000
def ii1iIIi11 ( url ) :
 url = cloudflare . source ( url )
 iiiI111I ( url )
 if 21 - 21: I1ii11iIi11i % iIi1i1ii1
def oOO0Oooo ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . recompile ( 'src="([^"]*)"' )
 for url in o00oooO0Oo :
  iiiI111I ( url )
  if 26 - 26: I11i / ii % OOoOoo % Oooo0O0oo00oO
  if 54 - 54: OOooOOo - OooOO000
def OoOOo000o0 ( ) :
 if 65 - 65: OooOO000 . OOoOoo + Oooo0O0oo00oO / I1ii11iIi11i + iIi1i1ii1 % ooOoO0O00
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 if 28 - 28: Ii + o0o00Oo0O / Ii1I
def I1oOO0o0 ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if oooO in Oo0O00O000 . lower ( ) :
   if 'Dad!' in Oo0O00O000 :
    pass
   elif 'Family Guy' in Oo0O00O000 :
    pass
   elif '2 Stupid' in Oo0O00O000 :
    pass
   elif 'The Zelfs' in Oo0O00O000 :
    pass
   elif 'A Clone' in Oo0O00O000 :
    pass
   elif 'A.T.O.M' in Oo0O00O000 :
    pass
   elif 'Almost Naked' in Oo0O00O000 :
    pass
   elif 'Angry Kid' in Oo0O00O000 :
    pass
   elif 'Annoying Orange' in Oo0O00O000 :
    pass
   elif 'Aqua Teen' in Oo0O00O000 :
    pass
   elif 'Assy Mcgee' in Oo0O00O000 :
    pass
   elif 'Astroblast' in Oo0O00O000 :
    pass
   elif 'Atomic Betty' in Oo0O00O000 :
    pass
   elif 'Axe Cop' in Oo0O00O000 :
    pass
   elif 'Baby Playpen' in Oo0O00O000 :
    pass
   elif 'Beavis and Butt' in Oo0O00O000 :
    pass
   elif 'Celebrity Deathmatch' in Oo0O00O000 :
    pass
   elif 'Clerks The' in Oo0O00O000 :
    pass
   elif 'Crapston Villas' in Oo0O00O000 :
    pass
   elif 'Duckman:' in Oo0O00O000 :
    pass
   elif 'Stripperella' in Oo0O00O000 :
    pass
   elif 'Vixen' in Oo0O00O000 :
    pass
   else :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
    if 34 - 34: IIi * IIi - Ii1I - o0o00Oo0O . Ii
    if 32 - 32: iI11I1II1I1I . oO0o * O0oOO0 / Oooo0O0oo00oO . IIiIiII11i - I1ii11iIi11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 10 - 10: Ii1I / Ii - IIi + O0oOO0 * oOo0O0Ooo
def o0O0O0 ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if 'Dad!' in Oo0O00O000 :
   pass
  elif 'Family Guy' in Oo0O00O000 :
   pass
  elif '2 Stupid' in Oo0O00O000 :
   pass
  elif 'The Zelfs' in Oo0O00O000 :
   pass
  elif 'A Clone' in Oo0O00O000 :
   pass
  elif 'A.T.O.M' in Oo0O00O000 :
   pass
  elif 'Almost Naked' in Oo0O00O000 :
   pass
  elif 'Angry Kid' in Oo0O00O000 :
   pass
  elif 'Annoying Orange' in Oo0O00O000 :
   pass
  elif 'Aqua Teen' in Oo0O00O000 :
   pass
  elif 'Assy Mcgee' in Oo0O00O000 :
   pass
  elif 'Astroblast' in Oo0O00O000 :
   pass
  elif 'Atomic Betty' in Oo0O00O000 :
   pass
  elif 'Axe Cop' in Oo0O00O000 :
   pass
  elif 'Baby Playpen' in Oo0O00O000 :
   pass
  elif 'Beavis and Butt' in Oo0O00O000 :
   pass
  elif 'Celebrity Deathmatch' in Oo0O00O000 :
   pass
  elif 'Clerks The' in Oo0O00O000 :
   pass
  elif 'Crapston Villas' in Oo0O00O000 :
   pass
  elif 'Duckman:' in Oo0O00O000 :
   pass
  elif 'Stripperella' in Oo0O00O000 :
   pass
  elif 'Vixen' in Oo0O00O000 :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , OO0o , '' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
def o0Oo0oo ( url ) :
 OO0O000 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0O000 )
 for ooI1111i in o0O0OOO0Ooo :
  Ii11iiIIiI1 = ooI1111i
 ii1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OO0O000 )
 for url in ii1iii1i :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , OO0o , '' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 10007 , Ii11iiIIiI1 )
  if 6 - 6: iIi1i1ii1 * ii + OooOO000 / IIi
  if 35 - 35: OOoOoo % oOo0O0Ooo - OOoOoo - oO0o - ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: ooOoO0O00 . ooOoO0O00 . O0oOO0 / oo0oO00 / OOoOoo
def Ii1Iiii ( url , IMAGE ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  print Oo0O00O000 + '     ' + url
  if 'easy' in url :
   Ooi1IIii11i1I1 ( url )
   if 12 - 12: ooOoO0O00 / Oooo0O0oo00oO % OOoOoo * iIi1i1ii1 * o0o00Oo0O * iI11I1II1I1I
   if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * O0oOO0 . ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 54 - 54: o0o00Oo0O / iIi1i1ii1 % OOoOoo * ooOoO0O00 * o0o00Oo0O
def Ooi1IIii11i1I1 ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
  if 48 - 48: I11i . O0oOO0 % OOooOOo - OOooOOo
  if 33 - 33: oo0oO00 % IIiIiII11i + oO0o
  if 93 - 93: ooOoO0O00 . iIi1i1ii1 / oOo0O0Ooo + iIi1i1ii1
def I1IiI11 ( ) :
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , OO0o , '' )
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - iiII11i1I1IIi . I11i
def Oooooooo00o00 ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if 'elete' in Oo0O00O000 :
   pass
  else :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 222 , ooI1111i )
   if 100 - 100: OooOO000 % IIiIiII11i . IIi % oO0o + Ii1I
def o0oOo0OO ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0oo00oOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , I1iOO0O0O , i1iII1IiiIiI1 in OO0oo00oOO :
  for oooO in I1iOO0O0O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1i1iIII11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for ooO0oOOooOo0 , Oo0O00O000 in i1i1iIII11i :
    if 'tube' in ooO0oOOooOo0 :
     pass
    elif 'stage' in ooO0oOOooOo0 :
     oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + I1iOO0O0O + '   -   ' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooI1111i , )
    elif 'vee' in ooO0oOOooOo0 :
     pass
     if 40 - 40: iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
def oOoo0ooOoo ( ) :
 I1 = O0 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0oo00oOO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , I1iOO0O0O , i1iII1IiiIiI1 in OO0oo00oOO :
  i1i1iIII11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for ooO0oOOooOo0 , Oo0O00O000 in i1i1iIII11i :
   if 'tube' in ooO0oOOooOo0 :
    pass
   elif 'stage' in ooO0oOOooOo0 :
    oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + I1iOO0O0O + '   -   ' + Oo0O00O000 + '[/COLOR]' , ( ooO0oOOooOo0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooI1111i )
   elif 'vee' in ooO0oOOooOo0 :
    pass
    if 52 - 52: oO0o * ii
    if 12 - 12: o0o00Oo0O + iIi1i1ii1 * ooOoO0O00 . oO0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: OooOO000 - I11i - Oooo0O0oo00oO
def I1i11ii11 ( url ) :
 I1 = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OO00O0oOO = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OO00O0oOO ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OO00O0oOO :
  Ii1IIiI1i ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 28 - 28: iI11I1II1I1I
  if 7 - 7: I11i % iIi1i1ii1 * OOooOOo
  if 58 - 58: iIi1i1ii1 / oo0oO00 + IIiIiII11i % iiII11i1I1IIi - ii
  if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * O0oOO0
  if 30 - 30: oo0oO00 % OOooOOo / Ii1I * o0o00Oo0O * IIi . oOo0O0Ooo
  if 46 - 46: OOooOOo - o0o00Oo0O
  if 70 - 70: oo0oO00 + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * oo0oO00
def I1IIIiIiIi ( ) :
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
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 oO0oiIiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 46 - 46: iiII11i1I1IIi
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  I1 = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , ooO0oooOO0 , Oo0O00O000 in o00oooO0Oo :
   if oooO in Oo0O00O000 . lower ( ) :
    Ii11IiIiiii1 ( Oo0O00O000 , ooO0oOOooOo0 , 222 , I1i1i1 , ooO0oooOO0 , I1iIi1iIiiIiI )
    if 60 - 60: oOo0O0Ooo % O0oOO0 / I11i % O0oOO0 * Ii / iiII11i1I1IIi
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 34 - 34: OooOO000 - Oooo0O0oo00oO
    if 25 - 25: O0oOO0 % oOo0O0Ooo + Ii + o0o00Oo0O * ii
def ooO0 ( ) :
 if 94 - 94: oo0oO00 . oOo0O0Ooo
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 oO0oiIiI = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 73 - 73: ooOoO0O00 / IIiIiII11i
 for ooIiI11i1I11111 in oO0oiIiI :
  I1i1I = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  I1 = Oo0OoO00oOO0o ( I1i1I )
  o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for Oo0O00O000 , I1iIi1iIiiIiI , ooO0oOOooOo0 , ooI1111i , ooO0oooOO0 , ooOOo00O00Oo in o00oooO0Oo :
   if oooO in Oo0O00O000 . lower ( ) :
    I11iiI ( Oo0O00O000 , ooO0oOOooOo0 , ooOOo00O00Oo , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
    if 17 - 17: oo0oO00 - iiII11i1I1IIi % IIi
    Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 2 - 2: IIi * Ii1I * ii
    if 73 - 73: OOooOOo + I1ii11iIi11i
def oOo ( ) :
 if 19 - 19: I11i
 OO0O000 = O0 ( oOOoo0Oo + 'spongemain.php' )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , I1iIi1iIiiIiI , ooO0oOOooOo0 , ooI1111i , ooO0oooOO0 , ooOOo00O00Oo in o00oooO0Oo :
  I11iiI ( Oo0O00O000 , ooO0oOOooOo0 , ooOOo00O00Oo , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
def o00OOOOOo0OOo ( url ) :
 if 44 - 44: oo0oO00 * I11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II11ii1I11 = ( '%s%s' % ( o0oO00o , url ) )
 O0o0O00Oo0o0 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in o00oooO0Oo :
  OOO0OoO0oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
  for I1IIIiI1I1ii1 in OOO0OoO0oo0OO :
   if I1IIIiI1I1ii1 == url :
    Oo0O00O000 = ( '[COLORred]Watched - [/COLOR]' + Oo0O00O000 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  Ii11IiIiiii1 ( Oo0O00O000 , url , 222 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
  if 31 - 31: oo0oO00 * O0oOO0 . IIi
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 35 - 35: oo0oO00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 94 - 94: OOoOoo / Ii % o0o00Oo0O
  if 70 - 70: oo0oO00 - I1ii11iIi11i / ii % ii
def oooo0o0OOO0 ( url ) :
 if 17 - 17: IIiIiII11i + oOo0O0Ooo
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , I1iIi1iIiiIiI , url , ooI1111i , ooO0oooOO0 , ooOOo00O00Oo in o00oooO0Oo :
  I11iiI ( Oo0O00O000 , url , ooOOo00O00Oo , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
  if 59 - 59: iI11I1II1I1I % IIi . Ii
  Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
  if 59 - 59: I11i . O0oOO0 . IIi * OOooOOo * oO0o + I1ii11iIi11i
  if 90 - 90: OooOO000 % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / Oooo0O0oo00oO + oo0oO00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: O0oOO0
def Ii11IiIiiii1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 87 - 87: iiII11i1I1IIi % I1ii11iIi11i
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  IIi11IIiIii1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = False )
 return oooo0O0O0o0
 if 62 - 62: oO0o + OOoOoo / iiII11i1I1IIi * Ii
def I11iiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 37 - 37: iiII11i1I1IIi
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  IIi11IIiIii1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = True )
 return oooo0O0O0o0
if 33 - 33: oO0o - o0o00Oo0O - oO0o
if 94 - 94: iIi1i1ii1 * oo0oO00 * ii / I11i . iIi1i1ii1 - I11i
if 13 - 13: Oooo0O0oo00oO / iIi1i1ii1 - oO0o / Oooo0O0oo00oO . ooOoO0O00
if 22 - 22: o0o00Oo0O - oo0oO00 + OooOO000 . IIi * ooOoO0O00
if 26 - 26: iI11I1II1I1I * I11i . oo0oO00
if 10 - 10: OooOO000 * O0oOO0 % I1ii11iIi11i - oo0oO00 % I1ii11iIi11i
if 65 - 65: iiII11i1I1IIi * iI11I1II1I1I / o0o00Oo0O . oo0oO00
if 94 - 94: I1ii11iIi11i . OOoOoo * Ii - I11i . iiII11i1I1IIi
if 98 - 98: Oooo0O0oo00oO + IIi
if 52 - 52: I1ii11iIi11i / OOooOOo - OooOO000 . iiII11i1I1IIi
if 50 - 50: iI11I1II1I1I - iiII11i1I1IIi - oo0oO00
if 60 - 60: iI11I1II1I1I * OOoOoo
if 71 - 71: OOooOOo % I1ii11iIi11i % OOoOoo
if 34 - 34: oo0oO00 / oo0oO00 % iIi1i1ii1 . OOooOOo / I1ii11iIi11i
if 99 - 99: OOoOoo * oOo0O0Ooo - OOoOoo % IIi
def I1i1II111Iii1 ( string ) :
 if Oo0oOOo == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 30 - 30: ooOoO0O00
def O0Oo0O00o0oo0OO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OooO00 = [ ]
 try :
  if 66 - 66: IIi % IIi - iIi1i1ii1
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  I1i1II111Iii1 ( 'Making Favorites File' )
  OooO00 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oO00oOOo0Oo = open ( I1IIiiIiii , "w" )
  oO00oOOo0Oo . write ( json . dumps ( OooO00 ) )
  oO00oOOo0Oo . close ( )
 else :
  I1i1II111Iii1 ( 'Appending Favorites' )
  oO00oOOo0Oo = open ( I1IIiiIiii ) . read ( )
  oOooO0OoO = json . loads ( oO00oOOo0Oo )
  oOooO0OoO . append ( ( name , url , iconimage , fanart , mode ) )
  Iiii111 = open ( I1IIiiIiii , "w" )
  Iiii111 . write ( json . dumps ( oOooO0OoO ) )
  Iiii111 . close ( )
  if 58 - 58: IIi % ii
  if 49 - 49: Ii1I + o0o00Oo0O . IIi * ii
def oO0OOO00 ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  OooO00 = [ ]
  I1i1II111Iii1 ( 'Making Favorites File' )
  OooO00 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oO00oOOo0Oo = open ( I1IIiiIiii , "w" )
  oO00oOOo0Oo . write ( json . dumps ( OooO00 ) )
  oO00oOOo0Oo . close ( )
 else :
  I1iIiI1iiiiI1 = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  IIII1ii1 = len ( I1iIiI1iiiiI1 )
  for OOO0O0OOo in I1iIiI1iiiiI1 :
   Oo0O00O000 = OOO0O0OOo [ 0 ]
   ooO0oOOooOo0 = OOO0O0OOo [ 1 ]
   I1i1i1 = OOO0O0OOo [ 2 ]
   try :
    Iii1 = OOO0O0OOo [ 3 ]
    if Iii1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     Iii1 = I1i1i1
    else :
     Iii1 = ooO0oooOO0
   try : OOoOi1IiiI = OOO0O0OOo [ 5 ]
   except : OOoOi1IiiI = None
   try : O0OOO0 = OOO0O0OOo [ 6 ]
   except : O0OOO0 = None
   if 61 - 61: OOoOoo . Ii + O0oOO0
   if OOO0O0OOo [ 4 ] == 0 :
    I1IiiiiI ( Oo0O00O000 , ooO0oOOooOo0 , '' , I1i1i1 , ooO0oooOO0 , '' , 'fav' )
   else :
    I1IiiiiI ( Oo0O00O000 , ooO0oOOooOo0 , OOO0O0OOo [ 4 ] , I1i1i1 , ooO0oooOO0 , '' , 'fav' )
    if 8 - 8: iI11I1II1I1I
def oOOo0ooO0 ( name ) :
 oOooO0OoO = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for ii1i1II11II1i in range ( len ( oOooO0OoO ) ) :
  if oOooO0OoO [ ii1i1II11II1i ] [ 0 ] == name :
   del oOooO0OoO [ ii1i1II11II1i ]
   Iiii111 = open ( I1IIiiIiii , "w" )
   Iiii111 . write ( json . dumps ( oOooO0OoO ) )
   Iiii111 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 95 - 95: oo0oO00 + I11i * Ii1I
 if 85 - 85: Ii . ii - iI11I1II1I1I
def oOOOOOoOO ( ) :
 I1OO0o = os . path . join ( O0O , 'addons.ini' )
 OoO000o0 = open ( I1OO0o , "w+" )
 I1 = O0 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 OoO000o0 . write ( r'[' + IiII + ']' + '\n' )
 for Oo0O00O000 , ooI1111i , I1iI1I1 , ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = ( ooO0oOOooOo0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  ooo00 = ( Oo0O00O000 + '=plugin://' + IiII + '/?url=' + ooO0oOOooOo0 + '&mode=10012&name=' + ( Oo0O00O000 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( ooI1111i ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( ooI1111i ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OoO000o0 . write ( ooo00 + '\n' )
  if 17 - 17: oo0oO00
  if 56 - 56: OOoOoo * I11i + oo0oO00
def I11II11111i11 ( ) :
 OO0O000 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  iIIII1iIIii ( '24/7' , ooO0oOOooOo0 , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 83 - 83: O0oOO0 - OOoOoo - iIi1i1ii1 % ooOoO0O00 - iiII11i1I1IIi . I11i
def oOo0oOooo0O ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def OOo0 ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def iI1iIii11Ii ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def iI1iIIIIIiIi1 ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ( ooO0oOOooOo0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def iIi ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o00oooO0Oo = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  o0OIiII ( Oo0O00O000 , ooO0oOOooOo0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 52 - 52: iI11I1II1I1I
  if 49 - 49: Oooo0O0oo00oO
def iIi1i ( ) :
 if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / oo0oO00 + OooOO000
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
 if 17 - 17: Oooo0O0oo00oO + IIiIiII11i
def I1i11I11Iii ( ) :
 if 3 - 3: I11i
 OO0O000 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 , i1111O0O000OOOo in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 + '  -  ' + ( i1111O0O000OOOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 10023 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 77 - 77: oOo0O0Ooo % OOoOoo
  if 74 - 74: OOooOOo / ooOoO0O00 % ii
  if 52 - 52: iIi1i1ii1 % OOoOoo
def I111 ( ) :
 if 51 - 51: Ii1I * O0oOO0
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
 if 23 - 23: Ii
def OOooOoO ( url ) :
 OOOoOo00O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( OOOoOo00O )
 o00oooO0Oo = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , OO0o , '' )
  if 24 - 24: I11i + oOo0O0Ooo - IIiIiII11i
  if 29 - 29: oOo0O0Ooo + Ii . o0o00Oo0O
  if 75 - 75: OooOO000 + iI11I1II1I1I
  if 19 - 19: oOo0O0Ooo + Ii . iIi1i1ii1 - oo0oO00 / IIi + I11i
def II1i ( ) :
 if 75 - 75: Ii1I
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oooO ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( ooO0oOOooOo0 )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if oooO in Oo0O00O000 . lower ( ) :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 92 - 92: oo0oO00 / o0o00Oo0O * oOo0O0Ooo - oo0oO00
   if 99 - 99: Ii % ii
   if 56 - 56: iIi1i1ii1 * OooOO000
def O00oO0O ( url ) :
 I1 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for O0o0OO0000ooo , ii11i , IiiI111I11 , Oo0O00O000 in o00oooO0Oo :
  oO0Ooooo000 = ( IiiI111I11 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Iii1Iiii = ( ii11i ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1i1Ii1IiIII = 'Season ' + Iii1Iiii + 'Episode ' + oO0Ooooo000 + Oo0O00O000
  I1IIii11 ( i1i1Ii1IiIII , O0o0OO0000ooo )
  if 22 - 22: OOoOoo / OOoOoo - IIi % oo0oO00 . Oooo0O0oo00oO + iIi1i1ii1
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 64 - 64: ooOoO0O00 % Ii1I / IIi % ii
  if 24 - 24: OooOO000 + ii . iIi1i1ii1 / OOooOOo / oo0oO00
def I1IIii11 ( name , url ) :
 O0o0OO0000ooo = url
 ooO = name
 iii1i1iiiiIi = cloudflare . source ( O0o0OO0000ooo )
 o0O0OOO0Ooo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for OO00O0oOO , ooOO0 in o0O0OOO0Ooo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + ooO + ooOO0 + '[/COLOR]' , OO00O0oOO , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 81 - 81: Ii + IIi % Ii - ooOoO0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: O0oOO0
 if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
def iI1I ( ) :
 if 16 - 16: Oooo0O0oo00oO
 if 63 - 63: iiII11i1I1IIi
 if 11 - 11: iiII11i1I1IIi - iI11I1II1I1I
 if 92 - 92: oO0o
 if 15 - 15: iIi1i1ii1 / iIi1i1ii1 + iI11I1II1I1I % ii
 if 12 - 12: OOoOoo
 if 36 - 36: OooOO000 . iIi1i1ii1 * ii - I11i
 if 60 - 60: Oooo0O0oo00oO . iiII11i1I1IIi / iI11I1II1I1I + Oooo0O0oo00oO * OooOO000
 if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - oo0oO00 + IIi
 if 48 - 48: Ii1I
 if 96 - 96: OOoOoo . ii
 if 39 - 39: Oooo0O0oo00oO + oO0o
 if 80 - 80: Oooo0O0oo00oO % oO0o / OOooOOo
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 54 - 54: I1ii11iIi11i % oO0o - Oooo0O0oo00oO - oo0oO00
 if 71 - 71: OOoOoo . Ii
def OoO000oo000o0 ( url ) :
 I1 = O0 ( url )
 O0iII1 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O0iII1 ) )
 for url , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 6 - 6: OOoOoo
def o0Ii11iIiiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 82 - 82: ii
def OoOO00oo0o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if 'episode' in url :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 76 - 76: iiII11i1I1IIi . iIi1i1ii1 % iiII11i1I1IIi - OooOO000
  if 51 - 51: ii + I11i * iI11I1II1I1I * O0oOO0 / ooOoO0O00
def I11IiI1i ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooO = 'http://www.watchseries.ac/search/' + oooO . replace ( ' ' , '%20' )
 I1 = O0 ( OooO )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'watch online' in Oo0O00O000 :
   pass
  else :
   print ooO0oOOooOo0
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , ooI1111i , '' , '' )
   if 85 - 85: IIiIiII11i
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 55 - 55: Ii1I
def oOoo0OO0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 , IiiI111I11 , I1iIi1iIiiIiI in o00oooO0Oo :
  OooooO0oOO = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IiiI111I11 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OooooO0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , ooI1111i , '' , I1iIi1iIiiIiI )
  if 5 - 5: Ii * I1ii11iIi11i
def i111 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  OooooO0oOO = ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OooooO0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 71 - 71: oO0o
def ooOOO0ooO0o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , ooI1111i , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 72 - 72: Oooo0O0oo00oO % ii % I11i * Oooo0O0oo00oO % oOo0O0Ooo * IIi
def iI11IiIiiII1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 O0iII1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for ii11i , OO0oo00oOO in O0iII1 :
  o00oooO0Oo = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OO0oo00oOO ) )
  for url , Oo0O00O000 in o00oooO0Oo :
   OooooO0oOO = ( ii11i ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + OooooO0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 o0O0OOO0Ooo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for Oo0O00O000 , url in o00oooO0Oo :
  I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in o0O0OOO0Ooo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: OOoOoo - o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / o0o00Oo0O
class IIi1I ( ) :
 if 15 - 15: Ii1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 4 - 4: iIi1i1ii1 + iI11I1II1I1I * iiII11i1I1IIi + I1ii11iIi11i * I11i % IIiIiII11i
  OooooO0oOO = name
  self . Get_Sources ( ooO0oOOooOo0 , OooooO0oOO )
  if 88 - 88: O0oOO0 - ooOoO0O00 % Ii % IIiIiII11i * ii
  if 40 - 40: I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O0 ( URL )
  o00oooO0Oo = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
   URL = 'http://www.watchseries.ac/link/' + ooO0oOOooOo0
   self . Get_site_link ( URL , season_name )
   if 47 - 47: OOooOOo
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
   if 65 - 65: o0o00Oo0O + OooOO000 % IIi * oOo0O0Ooo / OOoOoo / OOooOOo
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oooOO = 'DACLIPS'
   if oooOO in IIi1I . source_list :
    pass
   else :
    self . daclips ( url , season_name , oooOO )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    oooOO = 'FILEHOOT'
    if oooOO in IIi1I . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , oooOO )
   else :
    if 'thevideo.me' in url :
     oooOO = 'THEVIDEO'
     if oooOO in IIi1I . source_list :
      pass
     else :
      self . thevideo ( url , season_name , oooOO )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      oooOO = 'ALLMYVIDEOS'
      if oooOO in IIi1I . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , oooOO )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       oooOO = 'VIDSPOT'
       if oooOO in IIi1I . source_list :
        pass
       else :
        self . vidspot ( url , season_name , oooOO )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        oooOO = 'VODLOCKER'
        if oooOO in IIi1I . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , oooOO )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 33 - 33: O0oOO0
         if 39 - 39: oO0o + o0o00Oo0O + OOoOoo * IIiIiII11i % o0o00Oo0O - o0o00Oo0O
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for IIIii , Oo0O00O000 in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 41 - 41: iIi1i1ii1 % I11i
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for IIIii , Oo0O00O000 in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 67 - 67: o0o00Oo0O % OooOO000
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for IIIii in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % Oooo0O0oo00oO
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for IIIii in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 39 - 39: IIi
 def daclips ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for IIIii in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 60 - 60: Oooo0O0oo00oO
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O0 ( url )
  o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for IIIii in o00oooO0Oo :
   self . Printer ( IIIii , season_name , source_name )
   if 62 - 62: OooOO000 * oo0oO00
 def Printer ( self , Link , season_name , source_name ) :
  if 74 - 74: OOooOOo . iI11I1II1I1I
  if Link in IIi1I . List :
   pass
  elif source_name in IIi1I . source_list :
   pass
  else :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IIi1I . List . append ( Link )
   IIi1I . source_list . append ( source_name )
   if 87 - 87: OOoOoo
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 41 - 41: OOooOOo . iI11I1II1I1I % OOoOoo + o0o00Oo0O
   if 22 - 22: I11i + I1ii11iIi11i . OOoOoo + Ii1I * iiII11i1I1IIi . Ii
   if 90 - 90: Oooo0O0oo00oO * OOooOOo - I1ii11iIi11i + I11i
   if 53 - 53: ii . ii + I11i - iiII11i1I1IIi + Oooo0O0oo00oO
   if 44 - 44: OooOO000 - iIi1i1ii1
def oOOO0o ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , OO0o , '' )
 if 100 - 100: O0oOO0 . oO0o - IIi + o0o00Oo0O * oO0o
def oOoOO ( url ) :
 I1IiiiiI ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OO0O000 )
 for i11I1iIii1i11 , url , iIiiI11II11i , o00OoO0o0 , o0OOOoO0ooOOOo0 , OoOOOO , o0oOOO , oOOo0O00o , oO00oOOo0Oo , IIi11 , O0OOO in o00oooO0Oo :
  iIiiI11II11i = iIiiI11II11i
  if 'Arsenal' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'arsenal-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                                  ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Bournemouth' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'afc-bournemouth.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                       ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Burnley' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'KEGnQWW.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                                   ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Chelsea' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'chelsea.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                                  ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Crystal' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'CrystalPalace.0.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                       ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Everton' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'Everton.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                                   ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Hull' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'hull-city-afc.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                                 ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Leicester' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                       ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Liverpool' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'liverpool-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                               ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Manchester City' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'city-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '               ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Manchester United' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + '91.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '          ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Middlesbrough' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                 ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Southampton' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'southampton-fc-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                   ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Stoke City' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'stoke-city.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                          ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Sunderland' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'sunderland-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                        ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Swansea' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'swansea-city-afc.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                    ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Tottenham' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '        ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Watford' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '                              ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'Bromwich' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '   ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  elif 'West Ham' in iIiiI11II11i :
   IiII1 = oOOOo00O00oOo + 'west-ham.png'
   Oo0O00O000 = '[COLOR' + iiI1IiI + ']' + i11I1iIii1i11 + ' - ' + iIiiI11II11i + '             ' + o00OoO0o0 + '        ' + o0OOOoO0ooOOOo0 + '        ' + OoOOOO + '        ' + o0oOOO + '        ' + oOOo0O00o + '        ' + oO00oOOo0Oo + '        ' + IIi11 + '[/COLOR]'
  I1IiiiiI ( str ( Oo0O00O000 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , IiII1 , IiII1 , iIiiI11II11i )
  if 11 - 11: iI11I1II1I1I - iIi1i1ii1 / o0o00Oo0O
def iIIii1i1Ii11 ( description ) :
 iIiiI11II11i = description
 ooO0oOOooOo0 = ( 'http://www.fullmatchesandshows.com/?s=' + iIiiI11II11i ) . replace ( ' ' , '%20' )
 iIIiOOOo00o ( ooO0oOOooOo0 )
 if 3 - 3: I11i
def IiiIiI1IIi1IIIii ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o00oooO0Oo = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0oOOooOo0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooI1111i , OO0o , '' )
  if 69 - 69: I1ii11iIi11i / IIi - IIi / OOooOOo * oO0o * oo0oO00
def OOOOOoooO ( url ) :
 I1 = O0 ( url )
 O0iII1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for O0iII1 in O0iII1 :
  oO0Oooo0OoO = re . compile ( '(.*?)</h2>' ) . findall ( str ( O0iII1 ) )
  for Iiii1IIIIiiI11 in oO0Oooo0OoO :
   Iiii1IIIIiiI11 = Iiii1IIIIiiI11
  I1iii1I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O0iII1 ) )
  for oooII111 , ooI1111i , time , I11iIi in I1iii1I :
   I1iiiiii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I11iIi )
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Iiii1IIIIiiI11 + ' - ' + oooII111 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + ooI1111i , OO0o , ( str ( I1iiiiii ) ) )
   if 10 - 10: IIiIiII11i % oO0o % oOo0O0Ooo - I1ii11iIi11i - Oooo0O0oo00oO
 Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if 46 - 46: iI11I1II1I1I * O0oOO0 + Ii . iI11I1II1I1I . Oooo0O0oo00oO / oO0o
def iI1111i1i1ii ( ) :
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
 if 62 - 62: ii / OOooOOo . iIi1i1ii1 . iIi1i1ii1 % OOoOoo
def iIIO0ooo ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  II1ii1iii1ii = Oo0O00O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0O00O000 :
   pass
  else :
   II1ii1iii1ii = Oo0O00O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + II1ii1iii1ii + '[/COLOR]' , url , 10013 , ooI1111i )
 for url , ooI1111i , Oo0O00O000 in o0O0OOO0Ooo :
  II1ii1iii1ii = Oo0O00O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0O00O000 :
   pass
  else :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + II1ii1iii1ii + '[/COLOR]' , url , 10013 , ooI1111i )
def iIIiOOOo00o ( url ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , OO0o , '' )
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 21 - 21: iIi1i1ii1 - oOo0O0Ooo % ii + I11i
 if 92 - 92: OOoOoo + iIi1i1ii1
 if 52 - 52: IIiIiII11i / oOo0O0Ooo . O0oOO0 * iIi1i1ii1 . oo0oO00
 if 25 - 25: Ii / OOooOOo - OooOO000 / oO0o . I11i . I11i
 if 6 - 6: O0oOO0 . oo0oO00
 if 43 - 43: Ii1I + I11i
 if 50 - 50: O0oOO0 % ooOoO0O00 * o0o00Oo0O
 for url , ooI1111i , Oo0O00O000 in o0O0OOO0Ooo :
  II1ii1iii1ii = Oo0O00O000 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Oo0O00O000 :
   pass
  else :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + II1ii1iii1ii + '[/COLOR]' , url , 10013 , ooI1111i )
   if 4 - 4: iI11I1II1I1I . ooOoO0O00
def Oo00oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for OO00O0oOO in o00oooO0Oo :
  oO0oO = ( OO00O0oOO ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  Ii1IIiI1i ( 'http:' + oO0oO )
  if 71 - 71: OooOO000 / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / Oooo0O0oo00oO . Ii1I * OOoOoo
  if 59 - 59: iI11I1II1I1I / Ii1I % OOoOoo
  if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % oo0oO00
def oOoO000 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , url , 8046 , ooI1111i )
 for url in o0O0OOO0Ooo :
  iIIII1iIIii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def Oo00o00Oo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  Ii1IIiI1i ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 50 - 50: OOoOoo % I1ii11iIi11i
def oO0000O0Oo00O ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 42 - 42: Ii / oOo0O0Ooo - oO0o - OOoOoo + IIiIiII11i % OOoOoo
def iI1iiiiIii ( ) :
 iIIII1iIIii ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 iIIII1iIIii ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 iIIII1iIIii ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1IIii ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OO0O000 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + ooI1111i )
 for url in next :
  iIIII1iIIii ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 80 - 80: Ii
  if 29 - 29: oOo0O0Ooo . Oooo0O0oo00oO + IIiIiII11i . I1ii11iIi11i
def I1iii1iIi ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def i1II1i ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  url = ( url ) . replace ( '\/' , '/' )
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 222 , '' )
  if 27 - 27: Ii1I / Oooo0O0oo00oO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiIiiIIII ( name , url ) :
 oOoOOOOoO0 = 0
 name = name
 url = url
 ii1I = [ '144' , '240' , '380' , '480' , '720' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']Resolution[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  Ii1IIiI1i ( url )
  if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - IIi
  if 40 - 40: iiII11i1I1IIi . OOooOOo * o0o00Oo0O
  if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + oo0oO00 . Oooo0O0oo00oO
  if 74 - 74: ooOoO0O00
  if 15 - 15: ooOoO0O00 + iIi1i1ii1 % oOo0O0Ooo / Ii * OOooOOo
  if 69 - 69: Ii
  if 61 - 61: o0o00Oo0O
  if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( ) :
 OO0O000 = O00OoOO0oo0 ( 'http://documentarylovers.com/' )
 o00oooO0Oo = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  if 'genre' in ooO0oOOooOo0 :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , ooO0oOOooOo0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo00O0O ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OO0O000 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , ooI1111i )
 for url in next :
  iIIII1iIIii ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 70 - 70: oO0o
def iIiiI1I ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in o0O0OOO0Ooo :
  i1II1i ( url )
  if 5 - 5: OOooOOo * IIiIiII11i % I1ii11iIi11i * I11i * oo0oO00 + I1ii11iIi11i
def I1I11i ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i1I1 = 'http://documentarylovers.com/?s=' + ( oooO ) . replace ( ' ' , '+' )
 O0o00OOo00O0O = I111i1I1 . lower ( )
 Oo00O0O ( O0o00OOo00O0O )
 if 77 - 77: OooOO000 + O0oOO0
def iI11Iii1I ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if 'films' in url :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def o0i1I ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OO0O000 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  if 'films' in url :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + ooI1111i )
 for url in o0O0OOO0Ooo :
  iIIII1iIIii ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def O0o0o00OoOo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  if 'rtd' in url :
   oO00o0O0Ooo ( url )
   if 44 - 44: ii / iiII11i1I1IIi
def oO00o0O0Ooo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OO0O000 )
 for O0o0O00Oo0o0 , file in o00oooO0Oo :
  url = ( 'https://rtd.rt.com' + O0o0O00Oo0o0 + file )
  Ii1IIiI1i ( url )
  if 81 - 81: O0oOO0 - Oooo0O0oo00oO
  if 21 - 21: I1ii11iIi11i * I11i + ii . OooOO000 % O0oOO0
def IIIIIiiI ( ) :
 I1 = O00OoOO0oo0 ( 'http://www.stream2watch.co/live-tv' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 , i1iIii in o00oooO0Oo :
  iIIII1iIIii ( ( Oo0O00O000 + '[COLOR' + iiI1IiI + ']' + i1iIii + '[/COLOR]' ) , ooO0oOOooOo0 , 8086 , ooI1111i )
  if 95 - 95: oo0oO00 / iIi1i1ii1 . o0o00Oo0O * iIi1i1ii1 - I11i * I1ii11iIi11i
def II1 ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 8087 , ooI1111i )
  if 27 - 27: oOo0O0Ooo
def iiI11I1ii11 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  O0OoO0oooOO ( url , Oo0O00O000 )
  if 44 - 44: OOoOoo * Ii
def O0OoO0oooOO ( url , name ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  print url
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 6 - 6: I11i % Oooo0O0oo00oO * Ii1I % IIi . Oooo0O0oo00oO
def iI1oOoo ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + ooO0oOOooOo0 , 3002 , 'http://www.solie.org/alibrary/' + ooI1111i )
def o00O0o00oo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooI1111i )
def iIiiII ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 iII1I = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OO0O000 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , Oo0O00O000 in iII1I :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']Season- ' + Oo0O00O000 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , ooI1111i , Oo0O00O000 in o0O0OOO0Ooo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooI1111i )
def o00oOOo0Oo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  Oooo0o0oO ( url )
def Oooo0o0oO ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
  if 82 - 82: OOoOoo
def oO00O0 ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def OoOooO0 ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "v.src = '([^']*)';" ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  iiiI111I ( url )
  if 9 - 9: OOooOOo - iIi1i1ii1
def III1I1Iii1iiI ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , ooO0oOOooOo0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def iiIi ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  if 'mp4' in url :
   Ii1IIiI1i ( url )
 for url in o0O0OOO0Ooo :
  yt . PlayVideo ( url )
  if 31 - 31: Ii + iIi1i1ii1 - OooOO000 * iiII11i1I1IIi
def O0OO00 ( ) :
 I1 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + ooO0oOOooOo0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def i1111I ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for Oo0O00O000 , url in o00oooO0Oo :
  if '(Free Access)' in Oo0O00O000 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def OoO00oo0 ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , Oo0O00O000 , url in o00oooO0Oo :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , ooI1111i , ooO0oooOO0 , '' )
  if 96 - 96: ooOoO0O00
def oOOO00 ( ) :
 ii1I = [ '[COLOR' + iiI1IiI + ']XXX Vids[/COLOR]' , '[COLOR' + iiI1IiI + ']Perfect Girls[/COLOR]' , '[COLOR' + iiI1IiI + ']Best Videos[/COLOR]' , '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '[COLOR' + iiI1IiI + ']Recently Uploaded[/COLOR]' , '[COLOR' + iiI1IiI + ']100% Verified[/COLOR]' , '[COLOR' + iiI1IiI + ']Tags[/COLOR]' , '[COLOR' + iiI1IiI + ']In Your Language[/COLOR]' , '[COLOR' + iiI1IiI + ']Search[/COLOR]' ]
 O0oO0 = xbmcgui . Dialog ( ) . select ( '[COLOR' + iiI1IiI + ']TOOLS[/COLOR]' , ii1I )
 if O0oO0 == 0 :
  ooooOOO0 ( 'http://watchxxxfree.com/categories' )
 if O0oO0 == 1 :
  Ii1i ( 'http://www.perfectgirls.net' )
 if O0oO0 == 2 :
  ooooOoOooo00Oo ( 'http://www.xvideos.com/best' )
 if O0oO0 == 3 :
  ooo00O0OOo ( 'http://www.xvideos.com/best' )
 if O0oO0 == 4 :
  ooooOoOooo00Oo ( 'http://www.xvideos.com/best' )
 if O0oO0 == 5 :
  ooooOoOooo00Oo ( 'http://www.xvideos.com/verified/videos' )
 if O0oO0 == 6 :
  IiI1 ( 'http://www.xvideos.com/tags' )
 if O0oO0 == 7 :
  Iii1IIII1Iii ( 'http://www.xvideos.com/porn' )
 if O0oO0 == 8 :
  OOOOOOo0o0O0o ( )
  if 8 - 8: I11i / I11i - oo0oO00 + I11i * OOooOOo . I11i
  if 45 - 45: IIiIiII11i * ooOoO0O00
  if 25 - 25: OOooOOo + iI11I1II1I1I % oo0oO00 / I1ii11iIi11i * I1ii11iIi11i
  if 51 - 51: O0oOO0 - oO0o + iiII11i1I1IIi - I11i . oO0o % Ii1I
  if 14 - 14: oOo0O0Ooo / o0o00Oo0O
  if 43 - 43: O0oOO0 - iIi1i1ii1 % Ii * IIiIiII11i . OooOO000 - oo0oO00
  if 13 - 13: oO0o
  if 70 - 70: iIi1i1ii1 . OooOO000 * oO0o + oo0oO00 - iIi1i1ii1 . iIi1i1ii1
  if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if 'ch' in url :
   iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def OOOOOO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 oOO0O = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , Oo0O00O000 in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for Oo0O00O000 , url in oOO0O :
  I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oooo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   OOOOiiI ( url )
def o000Ooo00o00O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def ooooOOO0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 , O0oOoOOO0OO in o00oooO0Oo :
  if 'category' in url :
   iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORorange]   ' + O0oOoOOO0OO + '[/COLOR]' , url , 90006 , ooI1111i , oOOOo00O00oOo + 'Jizbox.png' , '' )
def ooo0O0O0oo0 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 oOO0O = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , ooI1111i , '' , '' )
 for url in oOO0O :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oo000oO ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'jetload' in url :
   OOOOiiI ( url )
def OOOOiiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( url )
def Ii1i ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 , O0oOoOOO0OO in o00oooO0Oo :
  if 'category' in url :
   iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORorange]' + O0oOoOOO0OO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiIiII11i1 ( url ) :
 I1 = O0 ( url )
 O0o0OO0000ooo = url
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 oOO0O = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , ooI1111i , '' , '' )
 for url in oOO0O :
  I1IiiiiI ( '[COLORred]NEXT[/COLOR]' , O0o0OO0000ooo + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def Ii1I1iIiiI1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in o00oooO0Oo :
  o00i111iiIiiIiI ( 'http://www.perfectgirls.net' + url )
def o00i111iiIiiIiI ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( 'http://' + url )
def Iii1IIII1Iii ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , Oo0O00O000 , O0oOoOOO0OO in o00oooO0Oo :
  iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORgreen] - No of Videos : [COLORorange]' + O0oOoOOO0OO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiI1 ( url ) :
 I1 = O0 ( url )
 oOO0O = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in oOO0O :
  iIIiIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , Oo0O00O000 , O0oOoOOO0OO in o00oooO0Oo :
  iIIiIi ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORgreen] - No of Videos : [COLORorange]' + ( O0oOoOOO0OO + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 59 - 59: Oooo0O0oo00oO + oOo0O0Ooo / IIiIiII11i / OOooOOo
def oOoo00 ( url ) :
 I1 = O0 ( url )
 oOO0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in oOO0O :
  iIIiIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 , o0Ii1 in o00oooO0Oo :
  iIIiIi ( Oo0O00O000 + '--' + ( o0Ii1 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( ooI1111i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 29 - 29: Oooo0O0oo00oO / OOooOOo . iI11I1II1I1I / oo0oO00 % OOooOOo % iiII11i1I1IIi
  if 49 - 49: IIiIiII11i / iIi1i1ii1 - IIi
def ooooOoOooo00Oo ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , url , Oo0O00O000 , oO00OoOoo0 , IiIII in o00oooO0Oo :
  iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + IiIII + ' - [COLORred]' + oO00OoOoo0 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , ooI1111i , ooI1111i , IiIII + ' - ' + oO00OoOoo0 )
 oO0oOOooO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in oO0oOOooO0 :
  iIIiIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 62 - 62: Ii - oo0oO00
def ooo00O0OOo ( url ) :
 I1 = O0 ( url )
 O0iII1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 oOO0O = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in oOO0O :
  iIIiIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O0iII1 ) )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '/c/' in url :
   iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 81 - 81: oo0oO00
   if 92 - 92: Oooo0O0oo00oO - I1ii11iIi11i - ii / iIi1i1ii1 - ooOoO0O00
def OOOOOOo0o0O0o ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo00o = ( oooO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 O0o00OOo00O0O = Oo00o . lower ( )
 i11i11II11i = 'http://www.xvideos.com/?k=' + O0o00OOo00O0O
 print i11i11II11i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O0 ( i11i11II11i )
 o00oooO0Oo = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 , oO00OoOoo0 , IiIII in o00oooO0Oo :
  iIIiIi ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[COLORgreen] - Porn Quality : [COLORorange]' + IiIII + ' - [COLORred]' + oO00OoOoo0 + '[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10108 , ooI1111i , ooI1111i , IiIII + ' - ' + oO00OoOoo0 )
 oO0oOOooO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for ooO0oOOooOo0 in oO0oOOooO0 :
  iIIiIi ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + ooO0oOOooOo0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 3 - 3: I1ii11iIi11i . ii + ooOoO0O00 / ooOoO0O00 % iI11I1II1I1I / IIi
def oooo00Oo0O ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 o0O0OOO0Ooo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 ii1iii1i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in o00oooO0Oo :
  if 'http' in url :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in o0O0OOO0Ooo :
  if 'http' in url :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in ii1iii1i :
  if 'http' in url :
   oOOO00o000o ( '[COLOR' + iiI1IiI + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def Iii1II1 ( url ) :
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 import urlresolver
 try : IIi1IIIIi . play ( url )
 except : pass
 if 54 - 54: OOooOOo . I1ii11iIi11i
 if 38 - 38: ooOoO0O00 . I1ii11iIi11i * I1ii11iIi11i / Ii1I
def o0oo0OooOO0 ( ) :
 if 57 - 57: IIiIiII11i % oOo0O0Ooo
 if 34 - 34: oOo0O0Ooo
 if 57 - 57: Oooo0O0oo00oO . IIi % I11i
 if 32 - 32: oo0oO00 / iIi1i1ii1 - o0o00Oo0O * iI11I1II1I1I
 if 70 - 70: ii % ii % oO0o
 if 98 - 98: oO0o
 if 18 - 18: oo0oO00 + I1ii11iIi11i - oO0o / OooOO000 / Oooo0O0oo00oO
 if 53 - 53: Oooo0O0oo00oO + I11i . O0oOO0 / oo0oO00
 if 52 - 52: OooOO000 + OooOO000
 if 73 - 73: I11i . Ii % ii + OOoOoo . ii / Oooo0O0oo00oO
 I1 = O0 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def oOiiI1i11I ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 8092 , ooI1111i )
 for url in next :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def IiIIii ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 oo0O0 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for ooI1111i in oo0O0 :
  ooI1111i = ooI1111i
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 8092 , ooI1111i )
 for url in next :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 34 - 34: IIiIiII11i - iIi1i1ii1 % OOooOOo % IIi / OOoOoo
def Ii1II ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( url )
  if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
  if 32 - 32: iIi1i1ii1 - OOoOoo * iiII11i1I1IIi * oo0oO00
  if 84 - 84: IIi + Ii1I % oOo0O0Ooo + Ii
  if 37 - 37: oo0oO00 % Ii1I / OOoOoo
o0oO = '{PQ},' ; ooOo0 = '{SC},' ; oOo0o = '{XG},' ; O000OOO000o = '{JP},' ; I11iiIiiI1iIi11 = '{HW},' ; II1I1I11i1I1 = '{RT},'
def I1ii1ii11i1I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiIi1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 84 - 84: IIiIiII11i
 oooOOO00o0 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1IIii1i = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 O0oOo0o0O0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0iii1i = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIIIIIi1IIi1I11i = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oooO
 O0o0oOooOoo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oOo0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 iIi1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIIII1iII1i = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 98 - 98: OooOO000 % oO0o - OOoOoo % Ii + OooOO000 - iIi1i1ii1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 97 - 97: OOoOoo / iI11I1II1I1I % OOoOoo / oOo0O0Ooo * iiII11i1I1IIi % OOooOOo
 if 17 - 17: iI11I1II1I1I
 Iiii = Oo0OoO00oOO0o ( oooOOO00o0 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( i1IIii1i )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 ooi11I = Oo0OoO00oOO0o ( O0oOo0o0O0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i111111 = Oo0OoO00oOO0o ( IIIIIIi1IIi1I11i )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o0oO0OOoO0OoO0 = Oo0OoO00oOO0o ( O0o0oOooOoo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iI11IiiiIII = Oo0OoO00oOO0o ( oOo0O0 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 i1i1Ii = Oo0OoO00oOO0o ( iIi1iI )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 Oo0o00o = Oo0OoO00oOO0o ( iIIII1iII1i )
 if 32 - 32: OOooOOo + OOoOoo + IIi + oOo0O0Ooo
 if 26 - 26: iiII11i1I1IIi - I1ii11iIi11i + oOo0O0Ooo + I11i
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for III1iI1Ii11Ii , Oo0O00O000 in o00oooO0Oo :
   if oooO in Oo0O00O000 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooO0oOOooOo0 + III1iI1Ii11Ii ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 29 - 29: OOooOOo
    if 37 - 37: IIiIiII11i % IIiIiII11i + I11i % I1ii11iIi11i / oOo0O0Ooo . O0oOO0
    if 60 - 60: oo0oO00 . o0o00Oo0O / o0o00Oo0O
    if 73 - 73: IIiIiII11i + Oooo0O0oo00oO * iiII11i1I1IIi / iiII11i1I1IIi
    if 74 - 74: o0o00Oo0O + iI11I1II1I1I + O0oOO0 * iIi1i1ii1
    if 39 - 39: OooOO000 . oO0o % OOoOoo . Oooo0O0oo00oO / iiII11i1I1IIi * oO0o
    if 12 - 12: oOo0O0Ooo / I11i
 if Iiii != 'Failed' :
  ii1iii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for III1iI1Ii11Ii , Oo0O00O000 in ii1iii1i :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oooOOO00o0 + III1iI1Ii11Ii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  o00O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in o00O0O :
   if oooO in Oo0O00O000 . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 86 - 86: I1ii11iIi11i % OOooOOo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if ooi11I != 'Failed' :
  o0o0O00oOo = [ ]
  iI1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooi11I )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in iI1ii :
   if oooO in Oo0O00O000 . lower ( ) :
    if Oo0O00O000 in o0o0O00oOo :
     pass
    else :
     I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ooO0oOOooOo0 , 1016 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
     o0o0O00oOo . append ( Oo0O00O000 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if i111111 != 'Failed' :
  iiOOoO0oOOO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i111111 )
  for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in iiOOoO0oOOO :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ooO0oOOooOo0 , 7067 , ooI1111i )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 47 - 47: Oooo0O0oo00oO / IIiIiII11i % iIi1i1ii1 . O0oOO0 * Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 35 - 35: I1ii11iIi11i * IIiIiII11i
    if 32 - 32: O0oOO0 . I1ii11iIi11i / OOoOoo + OOoOoo . Ii1I
    if 50 - 50: iI11I1II1I1I * O0oOO0
    if 85 - 85: ooOoO0O00
    if 100 - 100: ii / oo0oO00 % oO0o + IIi
    if 42 - 42: I1ii11iIi11i / iIi1i1ii1 . IIi * oOo0O0Ooo
    if 54 - 54: OOooOOo * iiII11i1I1IIi + oO0o
    if 93 - 93: I11i / oOo0O0Ooo
    if 47 - 47: I1ii11iIi11i * Oooo0O0oo00oO
 if iI11IiiiIII != 'Failed' :
  oOoO0O00o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI11IiiiIII )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in oOoO0O00o :
   if oooO in Oo0O00O000 . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 222 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 25 - 25: o0o00Oo0O + oo0oO00 + Oooo0O0oo00oO * Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if i1i1Ii != 'Failed' :
  OO0Iii1iIiI111Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i1Ii )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in OO0Iii1iIiI111Ii :
   if oooO in Oo0O00O000 . lower ( ) :
    o0OIiII ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 222 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 61 - 61: ii * OOooOOo
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 97 - 97: Ii
 if Oo0o00o != 'Failed' :
  O0oOo0o0OOoO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oo0o00o )
  for ooO0oOOooOo0 , I1i1i1 , Oo0O00O000 in O0oOo0o0OOoO0 :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Silent Hunter[/COLOR]' ) , ooO0oOOooOo0 , 222 , I1i1i1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 30 - 30: IIi % oo0oO00 + I11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 oO0oiIiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 65 - 65: iI11I1II1I1I . iiII11i1I1IIi / IIi
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
  iI11ii = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  if iI11ii != 'Failed' :
   oOoooO00OO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI11ii )
   for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in oOoooO00OO0o :
    if oooO in Oo0O00O000 . lower ( ) :
     o0OIiII ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , 222 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 29 - 29: I1ii11iIi11i + IIiIiII11i
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 95 - 95: O0oOO0
 oO0oiIiI = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 48 - 48: oo0oO00 / iI11I1II1I1I % IIiIiII11i
 if 39 - 39: ooOoO0O00 . Ii1I / oo0oO00 / oo0oO00
 for ooIiI11i1I11111 in oO0oiIiI :
  Ii1IIIIIIiI1 = iiIi1 + ooIiI11i1I11111
  ooOo0oO0O = Oo0OoO00oOO0o ( Ii1IIIIIIiI1 )
  if ooOo0oO0O != 'Failed' :
   I1i1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( ooOo0oO0O )
   for III1iI1Ii11Ii , Oo0O00O000 in I1i1 :
    if oooO in Oo0O00O000 . lower ( ) :
     oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiIi1 + ooIiI11i1I11111 + III1iI1Ii11Ii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 35 - 35: IIiIiII11i / IIi
     Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
     if 79 - 79: OOooOOo + OooOO000 * iiII11i1I1IIi * IIi
     if 53 - 53: Oooo0O0oo00oO / I1ii11iIi11i
def oooooo0OO ( ) :
 if 10 - 10: Ii1I . I11i
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 if 75 - 75: o0o00Oo0O * ooOoO0O00 - oo0oO00 / Oooo0O0oo00oO % Oooo0O0oo00oO / OOooOOo
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( oooO ) . replace ( ' ' , '%20' )
 O0o0OO0000ooo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 oooOOO00o0 = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 i1IIii1i = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 O0oOo0o0O0o = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O0o00OOo00O0O ) . replace ( ' ' , '+' )
 o0iii1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IIIIIIi1IIi1I11i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 O0o0oOooOoo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 5 - 5: o0o00Oo0O - iiII11i1I1IIi / OooOO000 . I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 7 - 7: Ii1I - OOooOOo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( O0o0OO0000ooo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = Oo0OoO00oOO0o ( oooOOO00o0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = Oo0OoO00oOO0o ( i1IIii1i )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 ooi11I = cloudflare . source ( O0oOo0o0O0o )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOo0oO0O = Oo0OoO00oOO0o ( o0iii1i )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i111111 = Oo0OoO00oOO0o ( IIIIIIi1IIi1I11i )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 o0oO0OOoO0OoO0 = Oo0OoO00oOO0o ( O0o0oOooOoo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 54 - 54: O0oOO0 / iI11I1II1I1I / ii . ooOoO0O00 - OOooOOo
 if o0oO0OOoO0OoO0 != 'Failed' :
  Oo00o0OOo0OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0oO0OOoO0OoO0 )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in Oo00o0OOo0OO :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source APPRENTICE[/COLOR]' ) , ooO0oOOooOo0 , 1016 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting APPRENTICE Links" )
    if 18 - 18: OOoOoo - iIi1i1ii1 / IIiIiII11i / Ii1I
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 31 - 31: OooOO000 * oOo0O0Ooo + OOoOoo
 if i111111 != 'Failed' :
  iiOOoO0oOOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i111111 )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in iiOOoO0oOOO :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- source Reaper[/COLOR]' ) , ooO0oOOooOo0 , 1016 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 48 - 48: o0o00Oo0O
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 44 - 44: oO0o * O0oOO0
    if 54 - 54: IIi % ooOoO0O00
    if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
    if 61 - 61: ii . IIi % O0oOO0 * ii
    if 96 - 96: IIi - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
    if 75 - 75: I1ii11iIi11i + IIi + oO0o
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 97 - 97: OOoOoo % Ii % oo0oO00
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for ooI1111i , ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + ooO0oOOooOo0 , 10044 , ooI1111i , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 21 - 21: I1ii11iIi11i / IIi / Ii1I / ooOoO0O00 / I11i
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 86 - 86: ooOoO0O00
    if 33 - 33: OOooOOo % Ii * Oooo0O0oo00oO
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
    if 34 - 34: iiII11i1I1IIi % Ii + Ii - iiII11i1I1IIi
    if 2 - 2: IIiIiII11i + ooOoO0O00
    if 68 - 68: Oooo0O0oo00oO + IIi
    if 58 - 58: iIi1i1ii1 * IIi . ooOoO0O00
    if 19 - 19: O0oOO0
    if 85 - 85: OOoOoo - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
 if Iiii != 'Failed' :
  ii1iii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for Oo0O00O000 in ii1iii1i :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( Oo0O00O000 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oooOOO00o0 + Oo0O00O000 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 94 - 94: iI11I1II1I1I + iIi1i1ii1
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  o00O0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for Oo0O00O000 in o00O0O :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( Oo0O00O000 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1IIii1i + Oo0O00O000 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 44 - 44: oO0o + oo0oO00 % oO0o + ooOoO0O00 + iiII11i1I1IIi + o0o00Oo0O
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if ooi11I != 'Failed' :
  iI1ii = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( ooi11I )
  for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in iI1ii :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + ' - Source - Dizi[/COLOR]' , ooO0oOOooOo0 , 8062 , ooI1111i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % O0oOO0 + oOo0O0Ooo % OOoOoo / IIi
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if ooOo0oO0O != 'Failed' :
  I1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOo0oO0O )
  for ooO0oOOooOo0 , I1i1i1 , I1iIi1iIiiIiI , O00oO0 , Oo0O00O000 in I1i1 :
   if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
    I1IiiiiI ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '- Source Scooby[/COLOR]' ) , ooO0oOOooOo0 , 1016 , I1i1i1 , O00oO0 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 36 - 36: OOooOOo . Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 81 - 81: I1ii11iIi11i * iiII11i1I1IIi * oO0o
 ooOOO0oOoooOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if ooOo0oO0O != 'Failed' :
  for ooIiI11i1I11111 in ooOOO0oOoooOo :
   Ii1IIIIIIiI1 = oOOoo0Oo + ooIiI11i1I11111 + IIIII
   i1i1Ii = O0 ( Ii1IIIIIIiI1 )
   if i1i1Ii != 'Failed' :
    OO0Iii1iIiI111Ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1i1Ii )
    for Oo0O00O000 , I1iIi1iIiiIiI , ooO0oOOooOo0 , ooI1111i , ooO0oooOO0 , ooOOo00O00Oo in OO0Iii1iIiI111Ii :
     if O0o00OOo00O0O in Oo0O00O000 . lower ( ) :
      I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + ' - Source Pandoras[/COLOR]' , ooO0oOOooOo0 , ooOOo00O00Oo , ooI1111i , ooO0oooOO0 , I1iIi1iIiiIiI )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 16 - 16: o0o00Oo0O % iIi1i1ii1 % I1ii11iIi11i - ii + ii
      Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
      if 94 - 94: iiII11i1I1IIi % iIi1i1ii1 / ii . oOo0O0Ooo + OooOO000 - IIiIiII11i
      if 33 - 33: iIi1i1ii1 / iIi1i1ii1 . Ii * Ii1I + I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1iI11IiIIi ( ) :
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oooO ) . replace ( ' ' , '+' )
 if 47 - 47: Oooo0O0oo00oO . O0oOO0 + OOooOOo % iIi1i1ii1 % ooOoO0O00 / iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 95 - 95: o0o00Oo0O . oO0o
 if I1 != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for ooO0oOOooOo0 , Oo0O00O000 in o0O0OOO0Ooo :
   if oooO in Oo0O00O000 . lower ( ) :
    oOOO00o000o ( ( Oo0O00O000 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + ooO0oOOooOo0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 89 - 89: ooOoO0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
I11II = '{ZH},' ; OOOO0 = '{IX},' ; iiii = '{LM},'
if 80 - 80: oOo0O0Ooo
def oO0OOo ( url ) :
 Oo0oo0OOO0OOoOO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Oo0oo0OOO0OOoOO )
 for url , ii11i , i1111O0O000OOOo , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( ii11i ) . replace ( 'Sezon' , ' Season ' ) + ( i1111O0O000OOOo ) . replace ( 'Bölüm' , ' Episode ' ) + Oo0O00O000 , url , 8063 , '' )
  if 97 - 97: ooOoO0O00
  if 46 - 46: Ii1I
  if 30 - 30: oO0o / o0o00Oo0O * I11i * OooOO000 + ii * iiII11i1I1IIi
  if 23 - 23: oo0oO00
def I1I ( url ) :
 Oo0oo0OOO0OOoOO = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Oo0oo0OOO0OOoOO )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , url , 222 , '' )
  if 81 - 81: OooOO000 / I1ii11iIi11i - iI11I1II1I1I
  if 17 - 17: iiII11i1I1IIi - ii % O0oOO0 * iIi1i1ii1
  if 28 - 28: IIiIiII11i * OOoOoo * OOooOOo * OooOO000 . IIiIiII11i . Ii1I
  if 32 - 32: OOoOoo - oO0o . iiII11i1I1IIi . iiII11i1I1IIi % ooOoO0O00 * IIi
def o0o0 ( ) :
 if 28 - 28: oo0oO00 . ii * Oooo0O0oo00oO + Ii % oOo0O0Ooo . iI11I1II1I1I
 Oo0oo0OOO0OOoOO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o00oooO0Oo = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Oo0oo0OOO0OOoOO )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 , i1111O0O000OOOo in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 + '  -  ' + ( i1111O0O000OOOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , ooO0oOOooOo0 , 8063 , ooI1111i )
  if 63 - 63: IIiIiII11i - oo0oO00 . OOooOOo
def IIi1I1iII111 ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 8002 , ooI1111i )
def o0OoO00OO0o0ooO ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OO0O000 )
 for ooI1111i , time , url , Oo0O00O000 , i1iiii in o00oooO0Oo :
  I1IiiiiI ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , time ) , url , 1015 , ooI1111i , i1iiii )
  if 42 - 42: o0o00Oo0O * iiII11i1I1IIi . OOooOOo / Oooo0O0oo00oO - IIi . oo0oO00
def OO0OOO ( ) :
 if 80 - 80: iI11I1II1I1I - I1ii11iIi11i % OooOO000 % I1ii11iIi11i + oOo0O0Ooo % IIi
 iIIII1iIIii ( 'Coronation Street' , '' , 8001 , '' )
 iIIII1iIIii ( 'Eastenders' , '' , 8002 , '' )
 iIIII1iIIii ( 'Emmerdale' , '' , 8003 , '' )
 iIIII1iIIii ( 'Hollyoaks' , '' , 8004 , '' )
 iIIII1iIIii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 86 - 86: OooOO000 - O0oOO0 % Oooo0O0oo00oO % Ii
 if 57 - 57: OooOO000
 if 10 - 10: oo0oO00 % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
 if 100 - 100: ooOoO0O00 % IIi
def oO000O ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Holly' in Oo0O00O000 :
   ooI1111i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in ooO0oOOooOo0 :
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , ooI1111i )
   else :
    pass
    if 62 - 62: ooOoO0O00 * iI11I1II1I1I % O0oOO0 % OOooOOo / ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 39 - 39: I1ii11iIi11i % iiII11i1I1IIi
def OooO00O0OO0oo ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'East' in Oo0O00O000 :
   ooI1111i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in ooO0oOOooOo0 :
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , ooI1111i )
   else :
    pass
    if 60 - 60: IIiIiII11i + I11i % OooOO000 + OOoOoo . iIi1i1ii1 % IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: OOoOoo
def i1iI11ii ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Emmer' in Oo0O00O000 :
   ooI1111i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in ooO0oOOooOo0 :
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , ooI1111i )
   else :
    pass
    if 65 - 65: ooOoO0O00 . Ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: Ii1I + oO0o - Ii1I * iIi1i1ii1 - oo0oO00 * oo0oO00
def OO00o ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Coro' in Oo0O00O000 :
   ooI1111i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in ooO0oOOooOo0 :
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , ooI1111i )
   else :
    pass
    if 36 - 36: iIi1i1ii1 . ooOoO0O00 * iI11I1II1I1I - IIi * OOooOOo - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: oo0oO00 % Ii1I - OOooOOo * Ii1I
def II1iIIi ( ) :
 I1 = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Celeb' in Oo0O00O000 :
   ooI1111i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in ooO0oOOooOo0 :
    oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , ooO0oOOooOo0 . replace ( '\\/' , '/' ) , 8006 , ooI1111i )
   else :
    pass
    if 35 - 35: Oooo0O0oo00oO . oo0oO00 . OooOO000 - oo0oO00 % oo0oO00 + OooOO000
def oO0oO00 ( name , url ) :
 IiiI1Ii1II = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiiI1Ii1II :
  OO0oIii1I1I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OO0O000 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OO0O000 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OO0O000 = open_url ( url )
  IIiIIiIi1II1IiI = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OO0O000 ) [ - 1 ]
  OO0oIii1I1I = IIiIIiIi1II1IiI . replace ( '\\/' , '/' )
 Ooo0oo = xbmcgui . ListItem ( name , '' , '' )
 Ooo0oo . setPath ( OO0oIii1I1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ooo0oo )
 if 99 - 99: I1ii11iIi11i
 if 17 - 17: Ii - Ii + Ii1I * OOoOoo * O0oOO0 / ii
def i1II111ii1ii ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o00oooO0Oo = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for ooO0oOOooOo0 , Oo0O00O000 in o0O0OOO0Ooo :
  iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , ooO0oOOooOo0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 54 - 54: iiII11i1I1IIi * IIiIiII11i / ii + OooOO000 - O0oOO0 + OOoOoo
def OOOOoOOOo0oOO ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Movies' in Oo0O00O000 :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( ooO0oOOooOo0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def O000oOOoOOO ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0O000 )
 o00oooO0Oo = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooI1111i )
 for url in o0O0OOO0Ooo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 40 - 40: oOo0O0Ooo / ii + oO0o * oO0o
  if 9 - 9: iI11I1II1I1I
def o0OoOO ( url ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url , ooI1111i in o00oooO0Oo :
  if '{{' in Oo0O00O000 :
   pass
  else :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , ooI1111i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
O0000 = '{UJ},' ; ooO0OO0Oooo0o = '{WE},' ; OOoO00o000 = '{WP},' ; iIi1 = '{PP},'
def Iii11111I1iii ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url , ooI1111i in o00oooO0Oo :
  if '{{' in Oo0O00O000 :
   pass
  else :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooI1111i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0Oo00 ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  IIi11I ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIi11I ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: Oooo0O0oo00oO + Oooo0O0oo00oO + O0oOO0 / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * Oooo0O0oo00oO
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '(cooltvseries.com)' in Oo0O00O000 :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , Oo0O00O000 in o0O0OOO0Ooo :
  if '(cooltvseries.com)' in Oo0O00O000 :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def oOoOooO ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  Ii1IIiI1i ( ( url ) . replace ( ' ' , '%20' ) )
o0OoOOoooooOO = '{XX},' ; oOOo = '{UD},' ; oOOOo0Oooo = '{YT},' ; I1iiIIiI11I = '{JS},' ; I11II1I = '{PF},'
if 92 - 92: I11i
def ii111Ii1i ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  oOOO00o000o ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( ooO0oOOooOo0 ) ) , 222 , ooI1111i )
  if 46 - 46: ooOoO0O00 - iiII11i1I1IIi + OooOO000 + oO0o + oo0oO00
def iII ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OO0O000 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OO0O000 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  if 'youtu' in url :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + ooI1111i )
 for url in next :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 45 - 45: oOo0O0Ooo + oo0oO00 + ooOoO0O00
def i1II ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . Oooo0O0oo00oO
def IIiiIiIIiI1 ( url ) :
 OO0O000 = O0
 o00oooO0Oo = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 222 , ooI1111i )
  if 39 - 39: oo0oO00 / ii - IIi + oO0o / OOooOOo
  if 87 - 87: OooOO000
  if 32 - 32: oo0oO00 - Oooo0O0oo00oO * o0o00Oo0O % iIi1i1ii1 . iIi1i1ii1 . oOo0O0Ooo
  if 91 - 91: ooOoO0O00 . iiII11i1I1IIi
  if 37 - 37: iiII11i1I1IIi - oo0oO00 + iI11I1II1I1I / OooOO000 - oO0o . I11i
def oO0000Oo ( ) :
 if 45 - 45: I1ii11iIi11i . ii + Oooo0O0oo00oO . OooOO000 % Ii1I
 iIIII1iIIii ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iIIII1iIIii ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 19 - 19: OooOO000 * iIi1i1ii1 - iIi1i1ii1 * iI11I1II1I1I . I1ii11iIi11i / iI11I1II1I1I
 if 100 - 100: OOoOoo % oo0oO00 / o0o00Oo0O * IIi - Ii
def o0oo ( Cat_Name ) :
 if 53 - 53: OooOO000 + ooOoO0O00 . oO0o / Ii + IIi % OOooOOo
 I1Io0Oo00 = False
 I1II11IIi11i = '0'
 if Cat_Name == 'All Channels' : I1Io0Oo00 = True
 if Cat_Name == 'Entertainment' : I1II11IIi11i = '1'
 if Cat_Name == 'Movies' : I1II11IIi11i = '2'
 if Cat_Name == 'Music' : I1II11IIi11i = '3'
 if Cat_Name == 'News' : I1II11IIi11i = '4'
 if Cat_Name == 'Sports' : I1II11IIi11i = '5'
 if Cat_Name == 'Documentary' : I1II11IIi11i = '6'
 if Cat_Name == 'Kids' : I1II11IIi11i = '7'
 if Cat_Name == 'Food' : I1II11IIi11i = '8'
 if Cat_Name == 'Religious' : I1II11IIi11i = '9'
 if Cat_Name == 'USA Channels' : I1II11IIi11i = '10'
 if Cat_Name == 'Other' : I1II11IIi11i = '11'
 if 67 - 67: iI11I1II1I1I - iiII11i1I1IIi
 OO0O000 = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO0O000 )
 print 'Len Match: >>>' + str ( len ( o00oooO0Oo ) )
 for Oo0O00O000 , ooI1111i , oOI1ii11IiI1I in o00oooO0Oo :
  Oo0Ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooI1111i ) . replace ( '\\' , '' )
  if oOI1ii11IiI1I == I1II11IIi11i :
   iIIII1iIIii ( Oo0O00O000 , '' , 7022 , Oo0Ii )
  elif I1Io0Oo00 == True :
   iIIII1iIIii ( Oo0O00O000 , '' , 7022 , Oo0Ii )
  else : pass
  if 96 - 96: IIi
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 24 - 24: o0o00Oo0O
def Ii1Iii1 ( Search_Name ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OO0O000 )
 o00oooO0Oo = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OO0O000 )
 for ooI1111i , ooO0oOOooOo0 , O0o0OO0000ooo , oooOOO00o0 in o00oooO0Oo :
  Oo0Ii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooI1111i ) . replace ( '\\' , '' )
  oOOO00o000o ( Search_Name + ': Link 1' , ( ooO0oOOooOo0 ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  oOOO00o000o ( Search_Name + ': Link 2' , ( O0o0OO0000ooo ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  oOOO00o000o ( Search_Name + ': Link 3' , ( oooOOO00o0 ) . replace ( '\\' , '' ) , 222 , Oo0Ii )
  if 87 - 87: ii
def iiI1 ( ) :
 OO0O000 = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def OoIII ( ) :
 OO0O000 = O0 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def OO00O ( ) :
 OO0O000 = O0 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OO0O000 )
 for Oo0O00O000 , ooO0oOOooOo0 in o00oooO0Oo :
  oOOO00o000o ( Oo0O00O000 , ( ooO0oOOooOo0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 66 - 66: IIi / o0o00Oo0O . oo0oO00 + iiII11i1I1IIi - IIi . oo0oO00
def II1Iii1I1II1i ( url ) :
 url
 I1IIIiI1I1ii1 = xbmcgui . ListItem ( Oo0O00O000 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1IIIiI1I1ii1 )
 return
 if 100 - 100: Ii - I1ii11iIi11i
 if 47 - 47: iiII11i1I1IIi * OOooOOo * iIi1i1ii1
def iIiii1IIi1I ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OO0O000 )
 for url , I1iIi1iIiiIiI , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + ooI1111i , '' , ( I1iIi1iIiiIiI ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 for url in o0O0OOO0Ooo :
  iIIII1iIIii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def IiI1I1i1 ( url ) :
 I1 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , I1iIi1iIiiIiI , ooI1111i in o00oooO0Oo :
  o0OIiII ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + ooI1111i , '' , I1iIi1iIiiIiI )
  Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 OO0oo00oOO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for Iii11I in OO0oo00oOO :
  oO0O00oOOoooO = ( Iii11I ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IiiiiI ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + ooI1111i , '' , oO0O00oOOoooO )
  if 2 - 2: O0oOO0 . Oooo0O0oo00oO
def ii1O0oOOo ( INFO ) :
 OOOiiiiI ( 'info for workout' , INFO )
 if 33 - 33: oOo0O0Ooo * OooOO000
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . OOoOoo - ooOoO0O00
 if 60 - 60: OOooOOo % OOooOOo
def I1Ii11iI11ii ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( ( Oo0O00O000 ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def oOo0 ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def ii1II ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  if '=' in Oo0O00O000 :
   pass
  else :
   oOOO00o000o ( ( Oo0O00O000 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def OOo00o0o0O0oo ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  if '=' in Oo0O00O000 :
   pass
  else :
   oOOO00o000o ( Oo0O00O000 , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 15 - 15: Oooo0O0oo00oO
   if 77 - 77: OOooOOo
   if 91 - 91: O0oOO0
   if 56 - 56: iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
   if 13 - 13: iIi1i1ii1 . I1ii11iIi11i - oo0oO00 / O0oOO0 - I1ii11iIi11i - oOo0O0Ooo
def oOO0o ( ) :
 OO0O000 = O0 ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 o00oooO0Oo = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'Daily' in Oo0O00O000 :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 9008 , Ooo )
def ooIi11II1IIIIIi ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Ooo )
def Oo0ooOO ( url ) :
 oOOO00o000o ( '[COLOR' + iiI1IiI + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 oOOO00o000o ( '[COLOR' + iiI1IiI + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 oOOO00o000o ( '[COLOR' + iiI1IiI + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  oOOO00o000o ( ( Oo0O00O000 ) . replace ( '_' , ' ' ) , url , 10012 , Ooo )
  if 6 - 6: Ii / ooOoO0O00 / iIi1i1ii1 . oOo0O0Ooo - Oooo0O0oo00oO % Ii
def o0OoOoOo0O ( ) :
 OO0O000 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if '.m3u' in ooO0oOOooOo0 :
   iIIII1iIIii ( ( Oo0O00O000 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + ooO0oOOooOo0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def IiIOOOoo ( url ) :
 OO0O000 = cloudflare . source ( url )
 o00oooO0Oo = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  oOOO00o000o ( ( Oo0O00O000 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 61 - 61: IIiIiII11i / IIiIiII11i . Ii
def iIiIiIiI ( ) :
 OO0O000 = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  if 'category' in ooO0oOOooOo0 :
   iIIII1iIIii ( Oo0O00O000 , 'http://www.disclose.tv/' + ooO0oOOooOo0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 61 - 61: oO0o - Ii / oo0oO00 % iIi1i1ii1
   if 21 - 21: iiII11i1I1IIi % iIi1i1ii1 % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OO0O000 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO0O000 )
 for url , Oo0O00O000 , ooI1111i in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , 'http://www.disclose.tv/' + url , 7011 , ooI1111i )
 for url in next :
  iIIII1iIIii ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 76 - 76: Ii1I + Oooo0O0oo00oO % o0o00Oo0O * Ii . o0o00Oo0O . Ii
  if 28 - 28: oO0o
def OOOOoOooo ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OO0O000 )
 ii1iii1i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  if 'http' in url :
   oOOO00o000o ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , Oo0O00O000 in o0O0OOO0Ooo :
  oOOO00o000o ( Oo0O00O000 , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in ii1iii1i :
  oOOO00o000o ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 15 - 15: OOoOoo * iI11I1II1I1I * O0oOO0
  if 96 - 96: OooOO000 * iI11I1II1I1I / OOooOOo % Oooo0O0oo00oO * IIiIiII11i
def I1iiIIii ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 90 - 90: iIi1i1ii1 * oo0oO00 % IIiIiII11i / Oooo0O0oo00oO
def o00oO0O000 ( name , url , img ) :
 I1 = O0 ( url )
 oO0o0OoOOOO00o0 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 O0ooo0 = len ( oO0o0OoOOOO00o0 )
 if 65 - 65: Oooo0O0oo00oO - oOo0O0Ooo * OooOO000
 if 99 - 99: oOo0O0Ooo
 if O0ooo0 == 1 :
  for OO000O000OOO in oO0o0OoOOOO00o0 :
   OO000O000OOO = OO000O000OOO . replace ( 'player' , 'watch' )
   I111Ii1I1I1iI = OO000O000OOO + '&fv=&sou='
   III = O0 ( I111Ii1I1I1iI )
   Oo0O = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( III )
   for IIIii in Oo0O :
    i1iIi1iiii1ii = False
    Resolve ( IIIii )
    if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
 elif O0ooo0 > 1 :
  if 21 - 21: OOooOOo - Ii - OOooOOo
  for OO000O000OOO in oO0o0OoOOOO00o0 :
   i1oo0OO0Oo = O0 ( OO000O000OOO )
   iIIi111I1i1i = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1oo0OO0Oo )
   IiIii111III1 = iIIi111I1i1i
   IiIii111III1 = ( str ( IiIii111III1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IiIii111III1
   oOOO00o000o ( 'DOUBLE LINK' , IiIii111III1 , 424 , '' )
   if 39 - 39: Ii - Oooo0O0oo00oO - OooOO000 + ii / oOo0O0Ooo / iI11I1II1I1I
   for url in iIIi111I1i1i :
    iIIII1iIIii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     O0o0OO0000ooo = Google . resolve ( url )
    except :
     pass
    try :
     IIi1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( O0o0OO0000ooo ) )
     for OooO00oO00o , IIII1iI1IiIiI in IIi1 :
      if 43 - 43: IIiIiII11i
      HD_URLS . append ( OooO00oO00o )
      SD_URLS . append ( IIII1iI1IiIiI )
    except :
     pass
 else :
  pass
  if 95 - 95: OooOO000 + iIi1i1ii1 * iI11I1II1I1I
def II1Iii1iI ( ) :
 if 56 - 56: iI11I1II1I1I . oo0oO00
 if 2 - 2: IIi
 iIIII1iIIii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 12 - 12: Ii - iI11I1II1I1I * iIi1i1ii1 * iiII11i1I1IIi
 iIIII1iIIii ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 19 - 19: o0o00Oo0O + O0oOO0 + I11i
 if 81 - 81: iI11I1II1I1I
def OOO00OiI ( ) :
 OO0O000 = O0 ( 'http://cnfstudio.com/' )
 o00oooO0Oo = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , 'http://cnfstudio.com/genre/' + ooO0oOOooOo0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 88 - 88: Oooo0O0oo00oO . I1ii11iIi11i * iIi1i1ii1 - iI11I1II1I1I % O0oOO0
iI111I11I1I1 = xbmcgui . Dialog ( )
if 80 - 80: IIi - Ii1I . IIi / Ii + o0o00Oo0O . iIi1i1ii1
III11i = '{UN},' ; o0OO0 = '{IG},' ; OOOOOoOOOOooo = '{PL},' ; I11IIIIiII11i = '{LO},' ; oOOo0Oo00O = '{LP},' ; IiIIiIiIIiI = '{HA},' ; I1ii11I1IiI = '{XD},' ; i1IIIii = '{TA},' ; I1I111i = '{DP},' ; OOooOOoO0 = '{JT},' ; Ii11i = '{JJ},' ; O00 = '{MM},' ; i1i = '{FQ},' ; iiiiIIiii1I1I = '{HH},'
if 62 - 62: IIiIiII11i - OOooOOo * IIi
def oO0OO0O ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OO0O000 )
 oooOoooOOo0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OO0O000 )
 for ooI1111i , url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , ooI1111i )
 oooOoooOOo0 = oooOoooOOo0
 for url in oooOoooOOo0 :
  iIIII1iIIii ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 25 - 25: iiII11i1I1IIi + oOo0O0Ooo + OOooOOo + OooOO000 % o0o00Oo0O
def i1Ii1I ( url ) :
 if 60 - 60: OOoOoo * IIi + OooOO000 . Oooo0O0oo00oO . o0o00Oo0O
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  O0o0O00Oo0o0 = url + '&fv=&sou='
  O0o0O00Oo0o0 = O0o0O00Oo0o0 . replace ( 'player' , 'watch' )
  Ii1i1ii = ooOOoO00o0o0oo0o ( O0o0O00Oo0o0 )
  i1i1ii11IiI = ooOOoO00o0o0oo0o ( url )
  if 6 - 6: Ii
  if 16 - 16: iIi1i1ii1
def ooOOoO00o0o0oo0o ( url ) :
 if 84 - 84: ooOoO0O00 / iI11I1II1I1I / O0oOO0 / IIi
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  iiiI111I ( url )
  if 7 - 7: OOooOOo . Oooo0O0oo00oO % I1ii11iIi11i
  if 55 - 55: OOoOoo - I1ii11iIi11i * O0oOO0
def OOOOO0oOOoO ( ) :
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , OO0o , '' )
 I1IiiiiI ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , OO0o , '' )
 if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  oo000o = open ( O0OoO000O0OO , 'r' )
  for I1IIIiI1I1ii1 in oo000o :
   iIIIII = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1IIIiI1I1ii1 )
   for Oo0O00O000 , ooO0oOOooOo0 in iIIIII :
    oOOO00o000o ( Oo0O00O000 , ooO0oOOooOo0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 if os . path . exists ( Remote ) :
  I1 = O00OoOO0oo0 ( url )
  o00oooO0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for Oo0O00O000 , url in o00oooO0Oo :
   url = ( url ) . strip ( )
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
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
 Oo0O00O000 = 'plugin.video.GenieTv'
 if 55 - 55: Ii * o0o00Oo0O
 ooO00Oo ( ooO0oOOooOo0 , Oo0O00O000 )
 if 46 - 46: OOoOoo - OOoOoo * Ii1I / iiII11i1I1IIi * Oooo0O0oo00oO / I11i
def i1IiiiI1iI ( ) :
 I1 = O0 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o00oooO0Oo = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for ooO0oOOooOo0 in o00oooO0Oo :
  ooO0oOOooOo0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + ooO0oOOooOo0
 Oo0O00O000 = 'repository.GenieTv'
 if 67 - 67: Oooo0O0oo00oO - IIi % iiII11i1I1IIi / IIiIiII11i + oOo0O0Ooo * OOoOoo
 ooO00Oo ( ooO0oOOooOo0 , Oo0O00O000 )
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
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 i11i11II11i = 'https://addons.tvaddons.ag/search/?keyword=' + O0o00OOo00O0O
 I1 = O0 ( i11i11II11i )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , IiII1 , Oo0O00O000 in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , ooO0oOOooOo0 , 10054 , 'https://addons.tvaddons.ag/' + IiII1 , OO0o , '' )
  if 11 - 11: I11i - IIiIiII11i % O0oOO0 . IIiIiII11i
  if 65 - 65: O0oOO0 . Ii % Oooo0O0oo00oO * iiII11i1I1IIi % I1ii11iIi11i
def IiiII1I ( ) :
 I1 = O0 ( oo0ooO0O )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if 'Repositories' in Oo0O00O000 :
   pass
  elif 'Services' in Oo0O00O000 :
   pass
  elif 'International' in Oo0O00O000 :
   pass
  else :
   I1IiiiiI ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , ooO0oOOooOo0 , 10053 , 'https://addons.tvaddons.ag/' + ooI1111i , OO0o , '' )
   if 51 - 51: oO0o % iiII11i1I1IIi
   if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
def Addon ( url ) :
 I1 = O0 ( url )
 II1IiI1II1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 o00oooO0Oo = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if 'Please' in Oo0O00O000 :
   pass
  else :
   o0OIiII ( Oo0O00O000 , url , 10054 , 'https://addons.tvaddons.ag/' + ooI1111i , OO0o , '' )
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
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , IiII1 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , url , 1007 , IiII1 )
def I1IiiIIiIii1i ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , IiII1 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 1006 , IiII1 )
  if 27 - 27: OOoOoo . I1ii11iIi11i + OOoOoo + iiII11i1I1IIi
  if 28 - 28: oO0o - OOoOoo - O0oOO0 % O0oOO0 / o0o00Oo0O
def IIi1i1I11Iii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , iconimage , I1iIi1iIiiIiI , ooO0oooOO0 , name in o00oooO0Oo :
  if 'http' in url :
   if '.php' in url :
    OOO0OoO0oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
    for I1IIIiI1I1ii1 in OOO0OoO0oo0OO :
     if I1IIIiI1I1ii1 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I11iiI ( name , url , 1016 , iconimage , ooO0oooOO0 , I1iIi1iIiiIiI )
   else :
    if 'youtube' in url :
     OOO0OoO0oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for I1IIIiI1I1ii1 in OOO0OoO0oo0OO :
      if I1IIIiI1I1ii1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Ii11IiIiiii1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , ooO0oooOO0 , I1iIi1iIiiIiI )
    else :
     OOO0OoO0oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
     for I1IIIiI1I1ii1 in OOO0OoO0oo0OO :
      if I1IIIiI1I1ii1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     Ii11IiIiiii1 ( name , url , 222 , iconimage , ooO0oooOO0 , I1iIi1iIiiIiI )
     Iii1I1I11iiI1 ( 'movies' , 'INFO' )
  else :
   oooo0OoOo ( url , iconimage , name )
   if 69 - 69: O0oOO0
 else :
  o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
  for url , IiII1 , name in o00oooO0Oo :
   if 'http' in url :
    if '.php' in url :
     iIIII1iIIii ( name , url , 1016 , IiII1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOOO00o000o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiII1 )
     else :
      OOO0OoO0oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oO0Oo ) )
      for I1IIIiI1I1ii1 in OOO0OoO0oo0OO :
       if I1IIIiI1I1ii1 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOOO00o000o ( name , url , 222 , IiII1 )
      Iii1I1I11iiI1 ( 'movies' , 'INFO' )
   else :
    oooo0OoOo ( url , IiII1 , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 95 - 95: iI11I1II1I1I
def oooo0OoOo ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o0O0ooo0o = ( url ) . replace ( OOOO0 , 'http' ) . replace ( oOOo , '.com' ) ;
 O0Oo = ( o0O0ooo0o ) . replace ( iiii , 'a' ) . replace ( oOo0o , 'b' ) . replace ( O000OOO000o , 'c' ) . replace ( ooO0OO0Oooo0o , 'd' ) . replace ( OOOOOoOOOOooo , 'e' ) . replace ( OOooOOoO0 , 'f' ) ;
 O0oOo00Oo0oo0 = ( O0Oo ) . replace ( o0OoOOoooooOO , 'g' ) . replace ( IiIIiIiIIiI , 'h' ) . replace ( oOOOo0Oooo , 'i' ) . replace ( I11II1I , 'j' ) . replace ( I11iiIiiI1iIi11 , 'k' ) . replace ( II1I1I11i1I1 , 'l' ) ;
 i111O0oOO0o00OO = ( O0oOo00Oo0oo0 ) . replace ( II1i11i1iI1I , 'm' ) . replace ( oooOoO00O , 'n' ) . replace ( I1i1IIiiI11II , 'o' ) . replace ( Ii1i1 , 'p' ) . replace ( iiiIiIIiIiiii , 'q' ) . replace ( o00O0OooO0 , 'r' ) ;
 iii1II11II1 = ( i111O0oOO0o00OO ) . replace ( I11i1Iii1I , 's' ) . replace ( OOoO00o000 , 't' ) . replace ( iIIiII1 , 'u' ) . replace ( iI1Iii1i1 , 'v' ) . replace ( OoOo00oOoo0oO , 'w' ) . replace ( i1ii1iIII , 'x' ) ;
 oooo = ( iii1II11II1 ) . replace ( ooo0000oo0 , 'y' ) . replace ( O0oooo000o , 'z' ) . replace ( III11i , '.' ) . replace ( o0OO0 , '(' ) . replace ( I11IIIIiII11i , ')' ) . replace ( oOOo0Oo00O , '/' ) ;
 IIiIiI11II = ( oooo ) . replace ( I11II , '1' ) . replace ( iIi1 , '2' ) . replace ( oOo00 , '3' ) . replace ( i1IIIii , '4' ) . replace ( I1I111i , '5' ) . replace ( I1iiIIiI11I , '6' ) ;
 Oooo = ( IIiIiI11II ) . replace ( Ii11i , '7' ) . replace ( O00 , '8' ) . replace ( i1i , '9' ) . replace ( iiiiIIiii1I1I , '0' ) . replace ( o0oO , ':' ) . replace ( ooOo0 , '%' ) ;
 url = ( Oooo ) . replace ( O0000 , '-' ) . replace ( I1ii11I1IiI , '_' ) ;
 oOOO00o000o ( name , url , 222 , iconimage ) ;
 if 18 - 18: IIi + OOooOOo . ooOoO0O00 / iIi1i1ii1 / iiII11i1I1IIi
 if 97 - 97: oO0o + iI11I1II1I1I
def O0OOoo ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , IiII1 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 1007 , IiII1 )
def i1I ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , IiII1 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 1006 , IiII1 )
  if 32 - 32: OOoOoo . iIi1i1ii1 . IIiIiII11i
def I1I11I1i1i1II ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ii1II11IIII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ii1II11IIII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1II11IIII1 )
 if 33 - 33: IIi + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * iIi1i1ii1
 if 21 - 21: o0o00Oo0O * OOoOoo % oO0o
def IiiIIi ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O000 )
 for url , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  if '-dir-' in Oo0O00O000 :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , ooI1111i )
  else :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' , url , 1006 , ooI1111i )
   if 14 - 14: o0o00Oo0O / OooOO000 / OOoOoo + iIi1i1ii1 - iIi1i1ii1
def IiiI11iIi ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 I1I111iIiI = ( 'http://afewbitsmore.com/' )
 o00oooO0Oo = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '[To Parent Directory]' in Oo0O00O000 :
   Oo0O00O000 = 'HOME'
   pass
  elif 'HOME' in Oo0O00O000 :
   pass
  elif '.m3u' in Oo0O00O000 :
   iIIII1iIIii ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , I1I111iIiI + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in Oo0O00O000 :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , I1I111iIiI + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in Oo0O00O000 :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , I1I111iIiI + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) , I1I111iIiI + url , 1012 , oOOOo00O00oOo + 'music.png' )
def I1Ii11I1i1iii ( url ) :
 I1 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for ooI1111i , Oo0O00O000 , url in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 83 - 83: o0o00Oo0O / oO0o
def o0O000O00o ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 I1I111iIiI = url
 o00oooO0Oo = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  if '.mp3' in Oo0O00O000 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   iIIII1iIIii ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '/' , '' ) , I1I111iIiI + url , 1011 , oOOOo00O00oOo + 'music.png' )
def iiooo ( ) :
 OO0O000 = O00OoOO0oo0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , ooI1111i , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ( 'http://www.cyn.net/music/' + ooO0oOOooOo0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + ooI1111i ) . replace ( ' ' , '%20' ) )
def ii111I1I1I ( url , img ) :
 OO0O000 = O00OoOO0oo0 ( url )
 O0o0OO0000ooo = url
 img = img
 o00oooO0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( O0o0OO0000ooo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 34 - 34: Ii1I % ooOoO0O00 - oO0o
def ooO0o0O0Oo ( url ) :
 OO0O000 = O00OoOO0oo0 ( url )
 O0o0OO0000ooo = url
 o00oooO0Oo = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O000 )
 for type , url , Oo0O00O000 in o00oooO0Oo :
  if '[VID]' in type :
   oOOO00o000o ( ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , O0o0OO0000ooo + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   ooO0o0O0Oo ( O0o0OO0000ooo + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: oOo0O0Ooo + OooOO000 - iiII11i1I1IIi % IIiIiII11i / OOooOOo % o0o00Oo0O
 if 59 - 59: o0o00Oo0O . I11i % Ii1I * O0oOO0 + oo0oO00
def O00o0O ( ) :
 iiIi1 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oooO = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0o00OOo00O0O = oooO . lower ( )
 ooO0oOOooOo0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 O0o0OO0000ooo = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oooOOO00o0 = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 82 - 82: ii
 I1 = Oo0OoO00oOO0o ( ooO0oOOooOo0 )
 iii1i1iiiiIi = Oo0OoO00oOO0o ( O0o0OO0000ooo )
 Iiii = Oo0OoO00oOO0o ( oooOOO00o0 )
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if I1 != 'Failed' :
  o00oooO0Oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0O00O000 in o00oooO0Oo :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( Oo0O00O000 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooO0oOOooOo0 + Oo0O00O000 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 27 - 27: Ii % iiII11i1I1IIi + IIi . Oooo0O0oo00oO
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  o0O0OOO0Ooo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for Oo0O00O000 in o0O0OOO0Ooo :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( Oo0O00O000 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o0OO0000ooo + Oo0O00O000 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 9 - 9: oO0o
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  ii1iii1i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for Oo0O00O000 in ii1iii1i :
   if oooO in Oo0O00O000 . lower ( ) :
    iIIII1iIIii ( ( Oo0O00O000 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oooOOO00o0 + Oo0O00O000 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 43 - 43: IIi . Oooo0O0oo00oO + oOo0O0Ooo * Ii
    Iii1I1I11iiI1 ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: Oooo0O0oo00oO
    if 3 - 3: oOo0O0Ooo . iiII11i1I1IIi % o0o00Oo0O - OOoOoo / o0o00Oo0O
    if 79 - 79: IIi + O0oOO0 % OOoOoo % oOo0O0Ooo
    if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
    if 53 - 53: iiII11i1I1IIi . O0oOO0 / I1ii11iIi11i . oO0o . Ii
    if 60 - 60: IIiIiII11i
II1i11i1iI1I = '{SF},' ; oooOoO00O = '{IF},' ; I1i1IIiiI11II = '{PW},' ; oOo00 = '{AM},' ; Ii1i1 = '{GF},' ; iiiIiIIiIiiii = '{DD},' ; o00O0OooO0 = '{UO},' ; I11i1Iii1I = '{LE},' ; iIIiII1 = '{ZY},' ; iI1Iii1i1 = '{UE},' ; OoOo00oOoo0oO = '{PE},' ; i1ii1iIII = '{JE},' ; ooo0000oo0 = '{TH},' ; O0oooo000o = '{LK},'
if 25 - 25: I1ii11iIi11i + I11i - oO0o
if 57 - 57: IIiIiII11i . ooOoO0O00
def OooOoOo ( ) :
 OO0O000 = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 o00oooO0Oo = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def I11Ii1 ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 , oooOOOoOOOo0O in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 + oooOOOoOOOo0O , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def oO0O ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OOOoooooO0oOOoO ( url )
def OOOoooooO0oOOoO ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OO0O000 )
 o0O0OOO0Ooo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OO0O000 )
 ii1iii1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( 'VidSpot - ' + Oo0O00O000 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in o0O0OOO0Ooo :
  oOOO00o000o ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for Oo0O00O000 , url in ii1iii1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOOO00o000o ( 'TheVideo - ' + Oo0O00O000 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 26 - 26: OooOO000 / OooOO000 + I1ii11iIi11i - I11i % IIiIiII11i . ii
def IiiI11Iii ( ) :
 OO0O000 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o00oooO0Oo = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 42 - 42: oo0oO00 + ooOoO0O00 - IIi / iIi1i1ii1 . iiII11i1I1IIi
  if 30 - 30: I1ii11iIi11i + IIi % Ii * ooOoO0O00 + oOo0O0Ooo % Oooo0O0oo00oO
def IiiIIiiI1I11 ( ) :
 OO0O000 = O0 ( 'http://www.animetoon.org/cartoon' )
 o00oooO0Oo = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OO0O000 )
 for ooO0oOOooOo0 , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , ooO0oOOooOo0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 74 - 74: I11i - OOoOoo / oOo0O0Ooo
  if 98 - 98: o0o00Oo0O % Ii % Oooo0O0oo00oO
  if 6 - 6: OooOO000 / IIi / iiII11i1I1IIi + oOo0O0Ooo / I1ii11iIi11i % ooOoO0O00
def iIIOOoOOooO ( url ) :
 OO0O000 = O0 ( url )
 o0O0OOO0Ooo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OO0O000 )
 for ooI1111i in o0O0OOO0Ooo :
  Ii11iiIIiI1 = ooI1111i
 ii1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OO0O000 )
 for url in ii1iii1i :
  iIIII1iIIii ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 o00oooO0Oo = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O000 )
 for url , Oo0O00O000 in o00oooO0Oo :
  iIIII1iIIii ( Oo0O00O000 , url , 1003 , Ii11iiIIiI1 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1111II1iIII ( url , IMAGE ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OO0O000 )
 for Oo0O00O000 , url in o00oooO0Oo :
  print Oo0O00O000 + '     ' + url
  if 'easy' in url :
   I1ii11ii1iiI ( url )
  elif 'playpanda' in url :
   I1ii11ii1iiI ( url )
   if 93 - 93: OOooOOo + oo0oO00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1ii11ii1iiI ( url ) :
 OO0O000 = O0 ( url )
 o00oooO0Oo = re . compile ( "url: '(.+?)'," ) . findall ( OO0O000 )
 for url in o00oooO0Oo :
  oOOO00o000o ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 27 - 27: iI11I1II1I1I * oo0oO00
  if 42 - 42: O0oOO0
def iiiiiiI1iIi ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOO00O . add_header ( 'referer' , url )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 40 - 40: Ii1I * oO0o % ii
def O00OoOO0oo0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 73 - 73: I11i - OOooOOo . oO0o + OooOO000 . iIi1i1ii1 % IIiIiII11i
def o0O0OOOO0o ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 II11ii1I11 = ( '%s%s' % ( o0oO00o , url ) )
 O0o0O00Oo0o0 = O00OoOO0oo0 ( url )
 o00oooO0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0o0O00Oo0o0 )
 for url , IiII1 , Oo0O00O000 in o00oooO0Oo :
  oOOO00o000o ( '%s' % ( '[COLOR' + iiI1IiI + ']' + Oo0O00O000 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IiII1 )
  if 70 - 70: iI11I1II1I1I
def iiiI111I ( url ) :
 if 79 - 79: Ii
 IiI1i1ii = open ( I11i1I1I , "a" )
 IiI1i1ii . write ( 'url="' + url + '"\n' )
 IiI1i1ii . close
 if 46 - 46: o0o00Oo0O % ii
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 import urlresolver
 try : IIi1IIIIi . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Oo0O00O000 ) )
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IIi1IIIIi . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 22 - 22: iiII11i1I1IIi + ii - OOooOOo - oO0o * OooOO000 - O0oOO0
def O0ooO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Oo0O00O000 )
 xbmc . sleep ( 1 )
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 o0oOoO00o . update ( 100 , '%s' % Oo0O00O000 )
 xbmc . sleep ( 1 )
 IIi1IIIIi . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 80 - 80: oOo0O0Ooo % iIi1i1ii1 / oo0oO00 * oO0o - O0oOO0 / O0oOO0
def Ii1IIiI1i ( url ) :
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IIi1IIIIi . play ( url ) . strip ( )
 except : pass
 if 13 - 13: I1ii11iIi11i
def oO0OooO00Oo ( url ) :
 IIi1IIIIi = xbmc . Player ( OOOoO ( ) )
 import urlresolver
 oO0OO00O0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 IIi1IIIIi . play ( oO0OO00O0 )
 xbmc . sleep ( 1 )
 IIi1IIIIi . play ( url )
 if 65 - 65: Oooo0O0oo00oO % iIi1i1ii1 % I11i . IIi . Ii1I
 if 64 - 64: Ii1I . IIi / Ii1I * IIi
def OOOoO ( ) :
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
def iIIII1iIIii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIi11IIiIii1 = [ ]
  IIi11IIiIii1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = True )
 return oooo0O0O0o0
 if 1 - 1: Oooo0O0oo00oO + OooOO000 * Ii1I
def iIIiIi ( name , url , mode , iconimage , fanart , description ) :
 if 44 - 44: iiII11i1I1IIi
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = True )
 return oooo0O0O0o0
 if 79 - 79: I11i % Oooo0O0oo00oO . o0o00Oo0O
def oOOO00o000o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIi11IIiIii1 = [ ]
  IIi11IIiIii1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = False )
 return oooo0O0O0o0
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
   try : oOOo0O00o = open ( announce ) ; Iii11I111i = oOOo0O00o . read ( )
   except : Iii11I111i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Iii11I111i ) )
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
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 15 - 15: ii - OOoOoo / oo0oO00 % IIi * iiII11i1I1IIi
def I1IiIi11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1i1I1i1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 35 - 35: iI11I1II1I1I % OooOO000 * oo0oO00 . I1ii11iIi11i
def I11IiiI1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + oOo0OoOOoO0Ooo0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 33 - 33: oOo0O0Ooo / oo0oO00 . I1ii11iIi11i
def O0OoO0o ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + o0Oo00oOOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 60 - 60: oo0oO00 . OOooOOo . IIiIiII11i
def I1Iiii11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + i1I1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 45 - 45: OOooOOo / oOo0O0Ooo
def IIII11i1Ii ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I11Iii11i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 65 - 65: iI11I1II1I1I * iIi1i1ii1
def O0ooOooOOoo ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + III1II11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 23 - 23: oO0o - O0oOO0 * iI11I1II1I1I
def i1iIi1I1 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + I1iiii1iiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 1 - 1: ooOoO0O00
def iIiiIIiI11 ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + iIIII11iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 42 , I1i1i1 , ooO0oooOO0 , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 78 - 78: iIi1i1ii1 + oo0oO00 - I11i + oO0o / iI11I1II1I1I
def Ii1I1i ( url ) :
 O0o0O00Oo0o0 = O0 ( str ( ooOO0O0ooOooO ) + ii111I111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00oooO0Oo = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( O0o0O00Oo0o0 )
 for Oo0O00O000 , url , I1i1i1 , ooO0oooOO0 , iII1111III1I in o00oooO0Oo :
  I1IiiiiI ( Oo0O00O000 , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , iII1111III1I )
 Iii1I1I11iiI1 ( 'movies' , 'MAIN' )
 if 18 - 18: O0oOO0 - iIi1i1ii1 % oo0oO00 * IIi
 if 66 - 66: ooOoO0O00 - ooOoO0O00 - Oooo0O0oo00oO . oo0oO00
 if 25 - 25: ooOoO0O00 * oOo0O0Ooo - OOooOOo + O0oOO0
 if 74 - 74: iiII11i1I1IIi / OooOO000 / IIiIiII11i - iiII11i1I1IIi / O0oOO0 % oo0oO00
 if 19 - 19: iIi1i1ii1 % ii + ii
 if 7 - 7: ooOoO0O00
 if 91 - 91: OOooOOo - OOooOOo . iIi1i1ii1
 if 33 - 33: OooOO000 - iI11I1II1I1I / IIi % o0o00Oo0O
 if 80 - 80: iIi1i1ii1 % ii - iIi1i1ii1
def Iii111IiIii ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooooO0 , iIiIIi , III1I in os . walk ( O00o0OO ) :
     I11IIIIi1 = 0
     I11IIIIi1 += len ( III1I )
     if I11IIIIi1 > 0 :
      for oOOo0O00o in III1I :
       os . unlink ( os . path . join ( ooooO0 , oOOo0O00o ) )
  ooOOo000 = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( ooOOo000 )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 77 - 77: oOo0O0Ooo / OooOO000
 if 65 - 65: Ii1I * o0o00Oo0O . ii * oo0oO00 / iIi1i1ii1
 if 87 - 87: iI11I1II1I1I
 if 58 - 58: Ii1I % Ii + OOooOOo / oo0oO00 - ii
 if 62 - 62: oO0o . OOooOOo
 if 22 - 22: OOoOoo . Ii . ii . ooOoO0O00
 if 12 - 12: OOooOOo % Oooo0O0oo00oO + O0oOO0 . o0o00Oo0O % iI11I1II1I1I
 if 41 - 41: ii
def IiiOooooOo0 ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 13 - 13: oo0oO00 + OooOO000 - OooOO000 % O0oOO0 / oo0oO00
def O0ooO0Oo00o ( url ) :
 IIIII11 = os . path . join ( oO , 'addon_data' )
 oooo00OoOoO = [
 ( IIIII11 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( IIIII11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( IIIII11 , 'plugin.video.itv' , 'Images' ) ) ]
 if 99 - 99: IIiIiII11i
 I1I111i1I = 0
 if 81 - 81: Ii1I % iI11I1II1I1I
 for I1IIIiI1I1ii1 in oooo00OoOoO :
  if os . path . exists ( I1IIIiI1I1ii1 ) and not I1IIIiI1I1ii1 in [ oOo0oooo00o , IIIII11 ] :
   for ooooO0 , iIiIIi , III1I in os . walk ( I1IIIiI1I1ii1 ) :
    I11IIIIi1 = 0
    I11IIIIi1 += len ( III1I )
    if I11IIIIi1 > 0 :
     for oOOo0O00o in III1I :
      if not oOOo0O00o in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( ooooO0 , oOOo0O00o ) )
       except :
        pass
      else : ii1 ( 'Ignore Log File: %s' % oOOo0O00o )
     for OoOOOO in iIiIIi :
      try :
       shutil . rmtree ( os . path . join ( ooooO0 , OoOOOO ) )
       I1I111i1I += 1
       ii1 ( "[Success] cleared %s files from %s" % ( str ( I11IIIIi1 ) , os . path . join ( I1IIIiI1I1ii1 , OoOOOO ) ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I1IIIiI1I1ii1 , OoOOOO ) )
  else :
   for ooooO0 , iIiIIi , III1I in os . walk ( I1IIIiI1I1ii1 ) :
    for OoOOOO in iIiIIi :
     if 'cache' in OoOOOO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooooO0 , OoOOOO ) )
       I1I111i1I += 1
       ii1 ( "[Success] wiped %s " % os . path . join ( I1IIIiI1I1ii1 , OoOOOO ) )
      except :
       ii1 ( "[Failed] to wipe cache in: %s" % os . path . join ( I1IIIiI1I1ii1 , OoOOOO ) )
       if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
 IiiOooooOo0 ( oo0o0O00 , 'Clear Cache: Removed %s Files' % I1I111i1I )
 if 43 - 43: I1ii11iIi11i / OooOO000 / ooOoO0O00
 if 3 - 3: IIi * OOoOoo . oO0o * ii + OOooOOo / o0o00Oo0O
 if 60 - 60: oo0oO00
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
 if 66 - 66: IIiIiII11i + iiII11i1I1IIi * O0oOO0 % oo0oO00 / ooOoO0O00 / iI11I1II1I1I
 if 62 - 62: OOooOOo + O0oOO0 * iIi1i1ii1 + o0o00Oo0O / Oooo0O0oo00oO + OOoOoo
 if 38 - 38: ooOoO0O00 / iI11I1II1I1I + iiII11i1I1IIi
def I11Ii1iI11iI1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI1Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooooO0 , iIiIIi , III1I in os . walk ( iI1Oo ) :
   I11IIIIi1 = 0
   I11IIIIi1 += len ( III1I )
   if 92 - 92: iI11I1II1I1I - IIi + ii . I11i - I11i
   if 82 - 82: iI11I1II1I1I + oo0oO00 . oo0oO00 * ii + Ii
   if I11IIIIi1 > 0 :
    if 46 - 46: ooOoO0O00 + o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I11IIIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: I11i + oOo0O0Ooo / ii % Ii % ii - I11i
     for oOOo0O00o in III1I :
      os . unlink ( os . path . join ( ooooO0 , oOOo0O00o ) )
     for OoOOOO in iIiIIi :
      shutil . rmtree ( os . path . join ( ooooO0 , OoOOOO ) )
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
 if 53 - 53: oO0o + Ii / iI11I1II1I1I
 if 1 - 1: iIi1i1ii1 % ooOoO0O00
 if 41 - 41: oO0o * oO0o / iiII11i1I1IIi + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / IIi
 if 80 - 80: Ii1I
 if 67 - 67: IIiIiII11i
 if 2 - 2: I11i - o0o00Oo0O * IIi % iIi1i1ii1
 if 64 - 64: ooOoO0O00 . OOoOoo
 if 7 - 7: O0oOO0 . iiII11i1I1IIi - iiII11i1I1IIi / OooOO000 % I1ii11iIi11i
def OO0Oooo0oOO0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iI1Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooooO0 , iIiIIi , III1I in os . walk ( iI1Oo ) :
   I11IIIIi1 = 0
   I11IIIIi1 += len ( III1I )
   if 61 - 61: O0oOO0 - Ii1I / iiII11i1I1IIi % Ii1I + oO0o / I1ii11iIi11i
   if 10 - 10: Ii / OOooOOo
   if I11IIIIi1 > 0 :
    if 27 - 27: oOo0O0Ooo / ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( I11IIIIi1 ) + " files found" , "Do you want to delete them?" ) :
     if 74 - 74: Ii1I % OooOO000 - oO0o * oo0oO00 . ii * oO0o
     for oOOo0O00o in III1I :
      os . unlink ( os . path . join ( ooooO0 , oOOo0O00o ) )
     for OoOOOO in iIiIIi :
      shutil . rmtree ( os . path . join ( ooooO0 , OoOOOO ) )
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
 if 99 - 99: OOooOOo . iiII11i1I1IIi - ii - o0o00Oo0O
 if 6 - 6: Oooo0O0oo00oO
 if 3 - 3: o0o00Oo0O - OooOO000 * IIi * Oooo0O0oo00oO / IIi
 if 58 - 58: IIi * iI11I1II1I1I + OOoOoo . OOoOoo
 if 74 - 74: OOoOoo - I11i * iIi1i1ii1 % OOoOoo
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * OooOO000 - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . O0oOO0 . ii . Oooo0O0oo00oO * Ii1I
 if 80 - 80: OooOO000 + oo0oO00 . OooOO000 + Oooo0O0oo00oO
def OoI11II ( url , name ) :
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iii11IiIi = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 OOOoO000oOOo = os . path . join ( oOooO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOOoO000oOOo ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Iii11IiIi = os . path . join ( oOooO0 , 'advancedsettings.xml' )
   try :
    os . remove ( Iii11IiIi )
    print '=== GenieTv - REMOVING    ' + str ( Iii11IiIi ) + '    ==='
   except :
    pass
   O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
   oO00oOOo0Oo = open ( Iii11IiIi , "w" )
   oO00oOOo0Oo . write ( O0o0O00Oo0o0 )
   oO00oOOo0Oo . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Iii11IiIi ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Iii11IiIi = os . path . join ( oOooO0 , 'advancedsettings.xml' )
  try :
   os . remove ( Iii11IiIi )
   print '=== GenieTv - REMOVING    ' + str ( Iii11IiIi ) + '    ==='
  except :
   pass
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  oO00oOOo0Oo = open ( Iii11IiIi , "w" )
  oO00oOOo0Oo . write ( O0o0O00Oo0o0 )
  oO00oOOo0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iii11IiIi ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
def I11IIi ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iii11IiIi = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  oO00oOOo0Oo = open ( Iii11IiIi ) . read ( )
  if 'zero' in oO00oOOo0Oo :
   name = '0CACHE'
  elif 'tuxen' in oO00oOOo0Oo :
   name = 'TUXENS'
  elif 'muckys' in oO00oOOo0Oo :
   name = 'MUCKYS'
  elif 'p2p1' in oO00oOOo0Oo :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oO00oOOo0Oo :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oO00oOOo0Oo :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 51 - 51: ooOoO0O00 % I11i - O0oOO0 - iIi1i1ii1
def i11IIII ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iii11IiIi = os . path . join ( oOooO0 , 'advancedsettings.xml' )
 try :
  os . remove ( Iii11IiIi )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Iii11IiIi ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 7 - 7: iiII11i1I1IIi / Ii1I
 if 76 - 76: IIi + iiII11i1I1IIi - iIi1i1ii1 * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: OOoOoo + IIiIiII11i . o0o00Oo0O - iiII11i1I1IIi / ii . OooOO000
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
 if 29 - 29: Ii1I
 if 41 - 41: IIi
 if 49 - 49: IIi % IIiIiII11i . IIi - I11i - oo0oO00 * iIi1i1ii1
 if 47 - 47: o0o00Oo0O . I11i / IIi * iiII11i1I1IIi
 if 63 - 63: OooOO000 - O0oOO0 - iiII11i1I1IIi - OOoOoo / O0oOO0 + oO0o
def i1III1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o00oooO0Oo = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for o0oOo , II1oOO0O0Ooo0 , I11iiI1i , ooOoOO in o00oooO0Oo :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % o0oOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I11iiI1i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ooOoOO )
  inc = inc + 1
  if 31 - 31: I11i
  if 59 - 59: I1ii11iIi11i / I1ii11iIi11i
  if 87 - 87: Ii1I % OOooOOo + IIi . Ii / IIi
  if 32 - 32: IIi + iIi1i1ii1 + Ii1I
  if 79 - 79: ooOoO0O00 / IIi
  if 81 - 81: iI11I1II1I1I
  if 86 - 86: iIi1i1ii1 % iIi1i1ii1 % ii
  if 42 - 42: I1ii11iIi11i . O0oOO0 + o0o00Oo0O / Oooo0O0oo00oO % ii
  if 19 - 19: OOoOoo / IIi
def III1IIii1i ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Iii11IiIi = os . path . join ( oOooO0 , 'addons2.ini' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  oO00oOOo0Oo = open ( Iii11IiIi , "w" )
  oO00oOOo0Oo . write ( O0o0O00Oo0o0 )
  oO00oOOo0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iii11IiIi ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 38 - 38: OOoOoo - I11i - o0o00Oo0O + OOoOoo % OOooOOo . I11i
def Ii1iI1I1i1I1I ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOooO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Iii11IiIi = os . path . join ( oOooO0 , 'settings.xml' )
  O0o0O00Oo0o0 = ii11iIi1I . http_GET ( url ) . content
  oO00oOOo0Oo = open ( Iii11IiIi , "w" )
  oO00oOOo0Oo . write ( O0o0O00Oo0o0 )
  oO00oOOo0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iii11IiIi ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 27 - 27: iiII11i1I1IIi
 if 8 - 8: o0o00Oo0O * ooOoO0O00 - OOooOOo % oOo0O0Ooo / Ii1I
def IIOoOooO ( ) :
 try :
  OO00o0OoOOOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO00o0OoOOOo ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I1ioO000O0oO00 = os . path . join ( OO00o0OoOOOo , "source.db" )
    os . unlink ( I1ioO000O0oO00 )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 25 - 25: oo0oO00 - OOooOOo
 if 4 - 4: I1ii11iIi11i - o0o00Oo0O / oo0oO00 + o0o00Oo0O - O0oOO0 * I1ii11iIi11i
 if 25 - 25: oOo0O0Ooo
 if 64 - 64: O0oOO0
 if 80 - 80: I11i % iI11I1II1I1I
def O0 ( url ) :
 OOO00O = urllib2 . Request ( url )
 OOO00O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 OOoOO0oo0ooO = urllib2 . urlopen ( OOO00O )
 O0o0O00Oo0o0 = OOoOO0oo0ooO . read ( )
 OOoOO0oo0ooO . close ( )
 return O0o0O00Oo0o0
 if 63 - 63: iIi1i1ii1 * Ii
 if 86 - 86: oo0oO00 % oo0oO00 - OOooOOo + OooOO000 / oOo0O0Ooo * ii
 if 26 - 26: IIiIiII11i * iiII11i1I1IIi + I11i / o0o00Oo0O + ooOoO0O00 - oo0oO00
 if 56 - 56: Oooo0O0oo00oO
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + iIi1i1ii1 - oo0oO00
 if 81 - 81: Ii1I + ii - Oooo0O0oo00oO * o0o00Oo0O
 if 100 - 100: iI11I1II1I1I - OOooOOo
def iiIiIIIiiI ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iIiI1Iii11II = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iIiI1Iii11II :
  ii11III1 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; ii11III1 = xbmc . translatePath ( ii11III1 ) ;
  OOOoO0oo0oo0o = os . path . join ( ii11III1 , ".." , ".." ) ; OOOoO0oo0oo0o = os . path . abspath ( OOOoO0oo0oo0o ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OOOoO0oo0oo0o ) ; oo0OO0O = False
  try :
   for ooooO0 , iIiIIi , III1I in os . walk ( OOOoO0oo0oo0o , topdown = True ) :
    iIiIIi [ : ] = [ OoOOOO for OoOOOO in iIiIIi if OoOOOO not in o0oO0 ]
    for Oo0O00O000 in III1I :
     try : os . remove ( os . path . join ( ooooO0 , Oo0O00O000 ) )
     except :
      if Oo0O00O000 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oo0OO0O = True
      plugintools . log ( "Error removing " + ooooO0 + " " + Oo0O00O000 )
    for Oo0O00O000 in iIiIIi :
     try : os . rmdir ( os . path . join ( ooooO0 , Oo0O00O000 ) )
     except :
      if Oo0O00O000 not in [ "Database" , "userdata" ] : oo0OO0O = True
      plugintools . log ( "Error removing " + ooooO0 + " " + Oo0O00O000 )
   if not oo0OO0O : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO0O0oO0 ( )
 if 81 - 81: Ii + IIiIiII11i . I1ii11iIi11i
 if 80 - 80: ooOoO0O00 * Ii1I
 if 93 - 93: o0o00Oo0O - Ii - oO0o + IIi
def Oo0OOo ( ) :
 oOoO000OOoo0 = [ ]
 IIiiI1iii1 = sys . argv [ 2 ]
 if len ( IIiiI1iii1 ) >= 2 :
  iiI1IIIi = sys . argv [ 2 ]
  o0OoO = iiI1IIIi . replace ( '?' , '' )
  if ( iiI1IIIi [ len ( iiI1IIIi ) - 1 ] == '/' ) :
   iiI1IIIi = iiI1IIIi [ 0 : len ( iiI1IIIi ) - 2 ]
  OOOo00OOooO = o0OoO . split ( '&' )
  oOoO000OOoo0 = { }
  for OOO0O0OOo in range ( len ( OOOo00OOooO ) ) :
   OO0OOOoO0O0 = { }
   OO0OOOoO0O0 = OOOo00OOooO [ OOO0O0OOo ] . split ( '=' )
   if ( len ( OO0OOOoO0O0 ) ) == 2 :
    oOoO000OOoo0 [ OO0OOOoO0O0 [ 0 ] ] = OO0OOOoO0O0 [ 1 ]
    if 8 - 8: iiII11i1I1IIi
 return oOoO000OOoo0
 if 43 - 43: Ii1I * Ii * Ii1I
I11II1ii1Ii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
Ii1iiII1i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ooOiII11iiI1i11I = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1Iii1III = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
o0ooOO0o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo0oo0OoO0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oOOO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1IO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1i1I1i1i1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOo0OoOOoO0Ooo0oo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0Oo00oOOO0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1I1I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I11Iii11i1Ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
III1II11 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1iiii1iiiI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iIIII11iII = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
oO0o00ooO0OoO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i1I1Iii1IiiIi = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
oo0O0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I111i1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOOOOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
III11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
ii111I111i = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
o0oO00o = base64 . decodestring ( 'Q1VOVA==' )
def I1IiiiiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = True )
 return oooo0O0O0o0
 if 73 - 73: o0o00Oo0O . OooOO000 - ii % oo0oO00 % ooOoO0O00
def o0OIiII ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ooooo00o0OoO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oooo0O0O0o0 = True
 Ooo0oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooo0oo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIi11IIiIii1 = [ ]
  if showcontext == 'fav' :
   IIi11IIiIii1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in ooOooo000oOO :
   IIi11IIiIii1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooo0oo . addContextMenuItems ( IIi11IIiIii1 )
 oooo0O0O0o0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ooooo00o0OoO , listitem = Ooo0oo , isFolder = False )
 return oooo0O0O0o0
 if 14 - 14: OooOO000 + IIi * I1ii11iIi11i
 if 49 - 49: I1ii11iIi11i
iiI1IIIi = Oo0OOo ( )
ooO0oOOooOo0 = None
Oo0O00O000 = None
ooOOo00O00Oo = None
I1i1i1 = None
ooO0oooOO0 = None
iII1111III1I = None
OoO0O00o0ooo0 = None
o0oOoooOoo0 = None
if 26 - 26: o0o00Oo0O * IIi - oOo0O0Ooo - iiII11i1I1IIi / iI11I1II1I1I
if 57 - 57: Ii1I - oO0o * iI11I1II1I1I
try :
 o0oOoooOoo0 = int ( iiI1IIIi [ "fav_mode" ] )
except :
 pass
 if 26 - 26: oO0o % OOoOoo % I11i % OOooOOo . iiII11i1I1IIi % o0o00Oo0O
try :
 ooO0oOOooOo0 = urllib . unquote_plus ( iiI1IIIi [ "url" ] )
except :
 pass
try :
 Oo0O00O000 = urllib . unquote_plus ( iiI1IIIi [ "name" ] )
except :
 pass
try :
 I1i1i1 = urllib . unquote_plus ( iiI1IIIi [ "iconimage" ] )
except :
 pass
try :
 ooOOo00O00Oo = int ( iiI1IIIi [ "mode" ] )
except :
 pass
try :
 ooO0oooOO0 = urllib . unquote_plus ( iiI1IIIi [ "fanart" ] )
except :
 pass
try :
 iII1111III1I = urllib . unquote_plus ( iiI1IIIi [ "description" ] )
except :
 pass
 if 91 - 91: IIiIiII11i . I1ii11iIi11i . O0oOO0 - ii / OOooOOo
 if 30 - 30: oo0oO00 % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( ooOOo00O00Oo )
print "URL: " + str ( ooO0oOOooOo0 )
print "Name: " + str ( Oo0O00O000 )
print "IconImage: " + str ( I1i1i1 )
if 55 - 55: oO0o
if 20 - 20: OOoOoo * OooOO000 * I11i - OOoOoo
def Iii1I1I11iiI1 ( content , viewType ) :
 if 32 - 32: IIi * O0oOO0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 85 - 85: Ii . oO0o + oO0o
if I1i1i1 == None : I1i1i1 = Ooo
if ooO0oooOO0 == None : ooO0oooOO0 = OO0o
if ooOOo00O00Oo == None :
 oo0OOo0 ( )
 if 28 - 28: I1ii11iIi11i
elif ooOOo00O00Oo == 1 :
 III1II1i ( ooO0oOOooOo0 )
 if 62 - 62: I1ii11iIi11i + ii / iiII11i1I1IIi
elif ooOOo00O00Oo == 44 :
 II11IiIi11 ( ooO0oOOooOo0 )
 if 60 - 60: IIi / OOooOOo . oo0oO00 % Oooo0O0oo00oO
elif ooOOo00O00Oo == 2 :
 oOOO0o0ooOo ( )
 if 61 - 61: o0o00Oo0O . IIi . o0o00Oo0O * Ii * IIiIiII11i / OooOO000
elif ooOOo00O00Oo == 3 :
 OOoOO0o ( )
 if 69 - 69: oo0oO00
elif ooOOo00O00Oo == 21 :
 i1i1II ( )
 if 17 - 17: oo0oO00
elif ooOOo00O00Oo == 4 :
 i11II ( )
 if 38 - 38: OooOO000 % Oooo0O0oo00oO
elif ooOOo00O00Oo == 5 :
 iiiI1IiIIii ( ooO0oOOooOo0 )
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
elif ooOOo00O00Oo == 6 :
 I11Ii1iI11iI1 ( ooO0oOOooOo0 )
 if 44 - 44: Ii1I % iIi1i1ii1
elif ooOOo00O00Oo == 7 :
 OoI11II ( ooO0oOOooOo0 , Oo0O00O000 )
 if 6 - 6: oO0o
elif ooOOo00O00Oo == 8 :
 I11IIi ( ooO0oOOooOo0 , Oo0O00O000 )
 if 82 - 82: iI11I1II1I1I . oo0oO00 / iIi1i1ii1 / Oooo0O0oo00oO * IIiIiII11i % O0oOO0
elif ooOOo00O00Oo == 9 :
 FIXREPOSADDONS ( ooO0oOOooOo0 )
 if 62 - 62: IIiIiII11i
elif ooOOo00O00Oo == 10 :
 o00O0 ( )
 if 96 - 96: oo0oO00 % OOooOOo * Ii1I
elif ooOOo00O00Oo == 11 :
 i11IIII ( ooO0oOOooOo0 )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . OOoOoo
elif ooOOo00O00Oo == 12 :
 i1III1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . iIi1i1ii1 * I11i + Oooo0O0oo00oO
elif ooOOo00O00Oo == 13 :
 Iii111IiIii ( )
 if 77 - 77: I11i
elif ooOOo00O00Oo == 14 :
 O0ooO0Oo00o ( ooO0oOOooOo0 )
 if 63 - 63: OOoOoo * O0oOO0 + OOoOoo * IIi + I1ii11iIi11i / Ii1I
elif ooOOo00O00Oo == 15 :
 o00OoO0oO00 ( )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
elif ooOOo00O00Oo == 16 :
 III1IIii1i ( ooO0oOOooOo0 , Oo0O00O000 )
 if 65 - 65: OooOO000 + o0o00Oo0O % I11i
elif ooOOo00O00Oo == 17 :
 Ii1iI1I1i1I1I ( ooO0oOOooOo0 , Oo0O00O000 )
 if 72 - 72: Oooo0O0oo00oO . OOooOOo / IIiIiII11i
elif ooOOo00O00Oo == 18 :
 IIOoOooO ( )
 if 69 - 69: Oooo0O0oo00oO * IIiIiII11i - OOoOoo - ooOoO0O00 + Ii
elif ooOOo00O00Oo == 19 :
 II111iIiI1Ii ( ooO0oOOooOo0 )
 if 50 - 50: ii * ooOoO0O00 / O0oOO0
elif ooOOo00O00Oo == 40 :
 iIi11i ( Oo0O00O000 , ooO0oOOooOo0 , iII1111III1I )
 if 83 - 83: ooOoO0O00
elif ooOOo00O00Oo == 42 :
 O000oOo0O ( Oo0O00O000 , ooO0oOOooOo0 , iII1111III1I )
 if 38 - 38: ii * iI11I1II1I1I
elif ooOOo00O00Oo == 43 :
 oOOoOOO0oo0 ( ooO0oOOooOo0 )
 if 54 - 54: ii . OooOO000
elif ooOOo00O00Oo == 20 :
 oOII1ii1ii11I1 ( ooO0oOOooOo0 )
 if 71 - 71: IIi
elif ooOOo00O00Oo == 22 :
 O0O0oOo0o0o0 ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 . Ii . oO0o * I1ii11iIi11i % IIi . I11i
elif ooOOo00O00Oo == 23 :
 I1IiIi11 ( ooO0oOOooOo0 )
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
elif ooOOo00O00Oo == 24 :
 I11IiiI1 ( ooO0oOOooOo0 )
 if 93 - 93: OOoOoo % OooOO000
elif ooOOo00O00Oo == 25 :
 O0OoO0o ( ooO0oOOooOo0 )
 if 46 - 46: Ii1I * OOooOOo * iIi1i1ii1 * Ii1I . Ii1I
elif ooOOo00O00Oo == 26 :
 I1Iiii11 ( ooO0oOOooOo0 )
 if 43 - 43: OOoOoo . ooOoO0O00
elif ooOOo00O00Oo == 27 :
 IIII11i1Ii ( ooO0oOOooOo0 )
 if 68 - 68: iIi1i1ii1 % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
elif ooOOo00O00Oo == 28 :
 O0ooOooOOoo ( ooO0oOOooOo0 )
 if 45 - 45: oOo0O0Ooo
elif ooOOo00O00Oo == 29 :
 i1iIi1I1 ( ooO0oOOooOo0 )
 if 17 - 17: ii - OOoOoo + IIi . ii % I1ii11iIi11i
elif ooOOo00O00Oo == 30 :
 O00o ( ooO0oOOooOo0 )
 if 92 - 92: OooOO000 - Oooo0O0oo00oO % oO0o - I11i % ooOoO0O00
elif ooOOo00O00Oo == 31 :
 iIiiIIiI11 ( ooO0oOOooOo0 )
 if 38 - 38: Ii1I . oo0oO00 / OOooOOo % oo0oO00
elif ooOOo00O00Oo == 32 :
 OoOoO ( )
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / iiII11i1I1IIi
elif ooOOo00O00Oo == 33 :
 OoO0O0oO00 ( )
 if 61 - 61: I1ii11iIi11i - OooOO000
elif ooOOo00O00Oo == 35 :
 i1IiIi1 ( ooO0oOOooOo0 )
 if 51 - 51: iiII11i1I1IIi * OOoOoo / o0o00Oo0O / o0o00Oo0O
elif ooOOo00O00Oo == 34 :
 i1i1 ( ooO0oOOooOo0 )
 if 52 - 52: ii % o0o00Oo0O
elif ooOOo00O00Oo == 36 :
 OO0 ( ooO0oOOooOo0 )
 if 56 - 56: O0oOO0 - ooOoO0O00 * ii - IIiIiII11i
elif ooOOo00O00Oo == 37 :
 iI1iIiiiI1I1 ( ooO0oOOooOo0 )
 if 28 - 28: ooOoO0O00 / oo0oO00 . I11i
elif ooOOo00O00Oo == 38 :
 Iii111Ii1 ( ooO0oOOooOo0 )
 if 11 - 11: I1ii11iIi11i * ii - Ii
elif ooOOo00O00Oo == 41 :
 iiIiIIIiiI ( iiI1IIIi )
 if 13 - 13: Ii . o0o00Oo0O / Oooo0O0oo00oO * ooOoO0O00
elif ooOOo00O00Oo == 39 :
 Ii1I1i ( ooO0oOOooOo0 )
 if 14 - 14: iIi1i1ii1 + iIi1i1ii1 . oo0oO00 / IIi . iI11I1II1I1I
elif ooOOo00O00Oo == 45 :
 TEXTS ( )
 if 10 - 10: IIiIiII11i . Oooo0O0oo00oO / iiII11i1I1IIi
elif ooOOo00O00Oo == 46 :
 OOI1iI1ii1II ( )
 if 35 - 35: iiII11i1I1IIi / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif ooOOo00O00Oo == 47 :
 GEVID ( )
 if 3 - 3: Ii1I
elif ooOOo00O00Oo == 48 :
 OOOO00OooO ( Oo0O00O000 , ooO0oOOooOo0 , iII1111III1I )
 if 42 - 42: oo0oO00 % I1ii11iIi11i + iIi1i1ii1 - oo0oO00 . iI11I1II1I1I - IIi
elif ooOOo00O00Oo == 49 :
 oOOOoo00 ( )
 if 27 - 27: iiII11i1I1IIi % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif ooOOo00O00Oo == 222 :
 iiiI111I ( ooO0oOOooOo0 )
 if 37 - 37: iiII11i1I1IIi + OooOO000 * IIi + iIi1i1ii1
elif ooOOo00O00Oo == 333 :
 o0O0OOOO0o ( ooO0oOOooOo0 )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + IIi / IIiIiII11i
 if 66 - 66: OOoOoo + O0oOO0 % ii
elif ooOOo00O00Oo == 1020 :
 IiiI11Iii ( )
 if 23 - 23: O0oOO0 . OOooOOo + iI11I1II1I1I
elif ooOOo00O00Oo == 1021 :
 ANIMEEP ( )
 if 17 - 17: iIi1i1ii1
elif ooOOo00O00Oo == 1022 :
 ANIMEPLAY ( ooO0oOOooOo0 )
 if 12 - 12: ooOoO0O00 . oO0o
elif ooOOo00O00Oo == 1001 :
 IiiIIiiI1I11 ( )
 if 14 - 14: Oooo0O0oo00oO + IIiIiII11i % Oooo0O0oo00oO . O0oOO0 * OOoOoo
elif ooOOo00O00Oo == 1005 :
 O0OOoo ( )
 if 54 - 54: OOoOoo * oo0oO00 - OooOO000
elif ooOOo00O00Oo == 1007 :
 i1I ( ooO0oOOooOo0 )
 if 15 - 15: iiII11i1I1IIi / o0o00Oo0O
elif ooOOo00O00Oo == 1010 :
 IiiIIi ( ooO0oOOooOo0 )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + OOoOoo . OooOO000 * OOoOoo
elif ooOOo00O00Oo == 1011 :
 o0O000O00o ( ooO0oOOooOo0 )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif ooOOo00O00Oo == 1012 :
 IiiI11iIi ( ooO0oOOooOo0 )
 if 82 - 82: o0o00Oo0O / iiII11i1I1IIi * oO0o - oo0oO00 + I1ii11iIi11i
elif ooOOo00O00Oo == 1030 :
 iiooo ( )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + IIi * IIiIiII11i
elif ooOOo00O00Oo == 1031 :
 ii111I1I1I ( ooO0oOOooOo0 , I1i1i1 )
 if 78 - 78: OooOO000 - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif ooOOo00O00Oo == 1032 :
 ooO0o0O0Oo ( ooO0oOOooOo0 )
 if 97 - 97: ooOoO0O00
elif ooOOo00O00Oo == 1006 :
 Parse . ParseURL ( ooO0oOOooOo0 )
 if 29 - 29: oOo0O0Ooo
elif ooOOo00O00Oo == 2030 :
 Parse . addonParseURL ( ooO0oOOooOo0 )
 if 37 - 37: Ii1I * OooOO000 * oOo0O0Ooo * o0o00Oo0O
elif ooOOo00O00Oo == 2031 :
 Parse . apkParseURL ( ooO0oOOooOo0 )
 if 35 - 35: oOo0O0Ooo - Ii1I * iiII11i1I1IIi + iIi1i1ii1 / ooOoO0O00
elif ooOOo00O00Oo == 1002 :
 iIIOOoOOooO ( ooO0oOOooOo0 )
 if 46 - 46: I1ii11iIi11i . OOoOoo % I1ii11iIi11i / IIiIiII11i * OOoOoo * Oooo0O0oo00oO
elif ooOOo00O00Oo == 1003 :
 i1111II1iIII ( ooO0oOOooOo0 , I1i1i1 )
 if 59 - 59: OooOO000 * iiII11i1I1IIi
elif ooOOo00O00Oo == 1004 :
 I1ii11ii1iiI ( ooO0oOOooOo0 )
 if 31 - 31: oo0oO00 / o0o00Oo0O
elif ooOOo00O00Oo == 1008 :
 ii111Ii1i ( )
 if 57 - 57: ooOoO0O00 % OOoOoo
elif ooOOo00O00Oo == 1009 :
 IIoooOoOO0o ( ooO0oOOooOo0 )
 if 69 - 69: I11i
elif ooOOo00O00Oo == 2001 :
 o00OooooOOOO ( )
 if 69 - 69: OooOO000
elif ooOOo00O00Oo == 2002 :
 I1Ii11I1i1iii ( ooO0oOOooOo0 )
 if 83 - 83: iI11I1II1I1I . I11i + OooOO000 . ii / OOoOoo + IIiIiII11i
elif ooOOo00O00Oo == 1013 :
 oOo000O ( )
elif ooOOo00O00Oo == 10111113 :
 oOO0o0oo0 ( ooO0oOOooOo0 )
 if 90 - 90: IIi * iiII11i1I1IIi / Oooo0O0oo00oO
elif ooOOo00O00Oo == 1014 :
 IIi1I1iII111 ( )
 if 68 - 68: OOooOOo
elif ooOOo00O00Oo == 1015 :
 o0OoO00OO0o0ooO ( ooO0oOOooOo0 )
 if 65 - 65: O0oOO0
elif ooOOo00O00Oo == 1016 :
 IIi1i1I11Iii ( ooO0oOOooOo0 , I1i1i1 , Oo0O00O000 )
 if 82 - 82: I11i
elif ooOOo00O00Oo == 1017 :
 IIIII1 ( )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + OooOO000
elif ooOOo00O00Oo == 1018 :
 IiiiI ( ooO0oOOooOo0 )
 if 65 - 65: IIi
elif ooOOo00O00Oo == 1023 :
 iIi1Ii1i1iI ( )
 if 71 - 71: OooOO000 % OooOO000 . O0oOO0 + Ii - Ii
elif ooOOo00O00Oo == 1024 :
 II1iiII1 ( ooO0oOOooOo0 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / OooOO000 - Ii . OOoOoo / Oooo0O0oo00oO
elif ooOOo00O00Oo == 1025 :
 I1IiiIIiIii1i ( ooO0oOOooOo0 )
 if 13 - 13: I11i % o0o00Oo0O - OooOO000 * ii / I1ii11iIi11i - ii
elif ooOOo00O00Oo == 4001 :
 o0o ( )
 if 78 - 78: O0oOO0 % ii
elif ooOOo00O00Oo == 4002 :
 IIIIiII1i ( )
 if 73 - 73: oOo0O0Ooo % OOoOoo % iIi1i1ii1 + ooOoO0O00 - ii / O0oOO0
elif ooOOo00O00Oo == 4003 :
 iIii11iI1II ( )
 if 78 - 78: ii % O0oOO0 - Ii
elif ooOOo00O00Oo == 4004 :
 oo0o0000 ( )
 if 37 - 37: iIi1i1ii1 % IIi % ooOoO0O00
elif ooOOo00O00Oo == 4005 :
 iiI ( )
 if 23 - 23: OOoOoo - o0o00Oo0O + Ii
elif ooOOo00O00Oo == 4006 :
 Oo00o0OO0O00o ( )
 if 98 - 98: ii
elif ooOOo00O00Oo == 4007 :
 O00oOOooo ( )
 if 61 - 61: I11i . iIi1i1ii1 . o0o00Oo0O + ii + o0o00Oo0O
elif ooOOo00O00Oo == 4008 :
 OoO0O00O0oo0O ( )
 if 65 - 65: ooOoO0O00 * Oooo0O0oo00oO * ii - iIi1i1ii1 . iiII11i1I1IIi - oO0o
elif ooOOo00O00Oo == 4009 : IIi1IIIi ( )
elif ooOOo00O00Oo == 4010 : iiiII ( )
elif ooOOo00O00Oo == 3000 :
 OOOOO0oOOoO ( )
 if 71 - 71: IIi * OOooOOo
elif ooOOo00O00Oo == 3001 :
 iI1oOoo ( )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % OooOO000 * I11i
elif ooOOo00O00Oo == 3002 :
 o00O0o00oo ( ooO0oOOooOo0 )
 if 64 - 64: OOoOoo / OOoOoo + Ii1I * Oooo0O0oo00oO % Oooo0O0oo00oO
elif ooOOo00O00Oo == 3003 :
 iIiiII ( ooO0oOOooOo0 )
 if 87 - 87: oO0o * I1ii11iIi11i
elif ooOOo00O00Oo == 3004 :
 o00oOOo0Oo ( ooO0oOOooOo0 )
 if 83 - 83: ooOoO0O00 * OooOO000 - iIi1i1ii1 / IIi
elif ooOOo00O00Oo == 404 :
 I1I11I1i1i1II ( Oo0O00O000 , ooO0oOOooOo0 , I1i1i1 )
 if 48 - 48: O0oOO0 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif ooOOo00O00Oo == 405 :
 O0ooO ( ooO0oOOooOo0 )
 if 32 - 32: IIi * oOo0O0Ooo - Oooo0O0oo00oO . I1ii11iIi11i / o0o00Oo0O + IIi
elif ooOOo00O00Oo == 7030 :
 oO0000Oo ( )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif ooOOo00O00Oo == 7021 :
 o0oo ( Oo0O00O000 )
 if 7 - 7: Ii % Ii1I / OooOO000 % I1ii11iIi11i - oO0o
elif ooOOo00O00Oo == 7022 :
 Ii1Iii1 ( Oo0O00O000 )
 if 73 - 73: Ii1I
elif ooOOo00O00Oo == 7000 :
 o00oO0O000 ( Oo0O00O000 , ooO0oOOooOo0 , img )
 if 92 - 92: Ii + o0o00Oo0O * oo0oO00
elif ooOOo00O00Oo == 7050 :
 iII ( ooO0oOOooOo0 )
 if 60 - 60: I11i / I1ii11iIi11i
elif ooOOo00O00Oo == 7051 :
 i1II ( ooO0oOOooOo0 )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif ooOOo00O00Oo == 7052 :
 OOOo0Ooo0o00o ( ooO0oOOooOo0 )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % OooOO000 / Ii1I
elif ooOOo00O00Oo == 7053 :
 oOoOooO ( ooO0oOOooOo0 )
 if 76 - 76: oO0o * O0oOO0 - oO0o
elif ooOOo00O00Oo == 7054 :
 CoolPlay ( ooO0oOOooOo0 )
 if 57 - 57: ii / OOooOOo + O0oOO0 . IIi
elif ooOOo00O00Oo == 7060 :
 OOOOoOOOo0oOO ( )
 if 14 - 14: Ii % Oooo0O0oo00oO * I11i * OOooOOo
elif ooOOo00O00Oo == 7061 :
 o0OoOO ( ooO0oOOooOo0 )
 if 55 - 55: OooOO000 * Oooo0O0oo00oO * OooOO000
elif ooOOo00O00Oo == 7063 :
 O000oOOoOOO ( ooO0oOOooOo0 )
 if 70 - 70: o0o00Oo0O . IIi
elif ooOOo00O00Oo == 7062 :
 Iii11111I1iii ( ooO0oOOooOo0 )
 if 33 - 33: Oooo0O0oo00oO * IIi
elif ooOOo00O00Oo == 7064 :
 NATatozcat ( )
 if 64 - 64: Ii . iI11I1II1I1I
elif ooOOo00O00Oo == 7067 :
 OO0Oo00 ( ooO0oOOooOo0 )
 if 7 - 7: OOooOOo % OOoOoo + OOooOOo - OOooOOo * Ii % oO0o
elif ooOOo00O00Oo == 7066 :
 NATatozA ( ooO0oOOooOo0 )
 if 57 - 57: Oooo0O0oo00oO / oO0o + Ii1I
elif ooOOo00O00Oo == 7065 :
 IIi11I ( ooO0oOOooOo0 )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % Oooo0O0oo00oO + iIi1i1ii1 . oO0o . I1ii11iIi11i
elif ooOOo00O00Oo == 7070 :
 i1II111ii1ii ( )
 if 70 - 70: oo0oO00 . Ii1I * O0oOO0
elif ooOOo00O00Oo == 7071 :
 DIZIlist ( ooO0oOOooOo0 )
 if 97 - 97: O0oOO0 . iI11I1II1I1I - Oooo0O0oo00oO
elif ooOOo00O00Oo == 7072 :
 DIZIpull ( ooO0oOOooOo0 )
 if 23 - 23: Ii1I % oo0oO00
elif ooOOo00O00Oo == 7073 :
 WATCHDIZI ( ooO0oOOooOo0 )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif ooOOo00O00Oo == 7002 :
 OOO00OiI ( )
 if 99 - 99: OooOO000 - Ii1I - oOo0O0Ooo - OooOO000 + oO0o + IIiIiII11i
elif ooOOo00O00Oo == 7003 :
 oO0OO0O ( ooO0oOOooOo0 )
 if 34 - 34: OooOO000 * oo0oO00
elif ooOOo00O00Oo == 7004 :
 i1Ii1I ( ooO0oOOooOo0 )
 if 31 - 31: iIi1i1ii1 . O0oOO0
elif ooOOo00O00Oo == 7020 :
 ooOOoO00o0o0oo0o ( ooO0oOOooOo0 )
 if 40 - 40: IIi - oo0oO00 / IIiIiII11i * ooOoO0O00 + iIi1i1ii1 * IIiIiII11i
elif ooOOo00O00Oo == 7001 :
 iIiIiIiI ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - OooOO000
elif ooOOo00O00Oo == 7010 :
 OoOoooOO00OO ( ooO0oOOooOo0 )
 if 99 - 99: IIi - iIi1i1ii1 - ooOoO0O00 / Ii . iIi1i1ii1
elif ooOOo00O00Oo == 7011 :
 OOOOoOooo ( ooO0oOOooOo0 )
 if 58 - 58: Oooo0O0oo00oO
elif ooOOo00O00Oo == 7012 :
 I1iiIIii ( ooO0oOOooOo0 )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif ooOOo00O00Oo == 7013 :
 cnfTVPlay2 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Oo0O00O000 , ooO0oOOooOo0 , I1i1i1 )
elif ooOOo00O00Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif ooOOo00O00Oo == 7018 :
 II1Iii1iI ( )
elif ooOOo00O00Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( ooO0oOOooOo0 )
 if 64 - 64: OOooOOo + iIi1i1ii1 - ooOoO0O00 . IIiIiII11i . oO0o
elif ooOOo00O00Oo == 8000 :
 OO0OOO ( )
elif ooOOo00O00Oo == 8001 :
 OO00o ( )
elif ooOOo00O00Oo == 8002 :
 OooO00O0OO0oo ( )
elif ooOOo00O00Oo == 8003 :
 i1iI11ii ( )
elif ooOOo00O00Oo == 8004 :
 oO000O ( )
elif ooOOo00O00Oo == 8005 :
 II1iIIi ( )
elif ooOOo00O00Oo == 8006 :
 oO0oO00 ( Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8030 :
 I1ii1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8045 :
 oOoO000 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8046 :
 Oo00o00Oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8047 :
 oO0000O0Oo00O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8048 :
 iI11Iii1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8049 :
 o0i1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 804900 :
 O0o0o00OoOo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8020 :
 OooOoOo ( )
elif ooOOo00O00Oo == 8021 :
 I11Ii1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8022 :
 oO0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8023 :
 OOOoooooO0oOOoO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8040 :
 iI1iiiiIii ( )
elif ooOOo00O00Oo == 8041 :
 Ii1IIii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8042 :
 I1iii1iIi ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8043 :
 yt . PlayVideo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8044 :
 i1II1i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8060 :
 oO00O0 ( )
elif ooOOo00O00Oo == 8061 :
 OoOooO0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8064 :
 III1I1Iii1iiI ( )
elif ooOOo00O00Oo == 8065 :
 iiIi ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8070 :
 O0OO00 ( )
elif ooOOo00O00Oo == 8071 :
 i1111I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7080 :
 OoO00oo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8090 :
 o0oo0OooOO0 ( )
elif ooOOo00O00Oo == 8091 :
 oOiiI1i11I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8092 :
 Ii1II ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8093 :
 IiIIii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8081 :
 o0o0 ( )
elif ooOOo00O00Oo == 8062 :
 oO0OOo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8063 :
 I1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8050 :
 I1IiI ( )
elif ooOOo00O00Oo == 8051 :
 I1iI1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8052 :
 oOOO00OOOoOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8085 :
 IIIIIiiI ( )
elif ooOOo00O00Oo == 8086 :
 II1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8087 :
 iiI11I1ii11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 8088 :
 O0OoO0oooOO ( ooO0oOOooOo0 , Oo0O00O000 )
elif ooOOo00O00Oo == 9000 :
 Oo0O0Oo00O ( )
elif ooOOo00O00Oo == 1111 :
 O00o0O ( )
elif ooOOo00O00Oo == 9001 :
 I1ii1ii11i1I ( )
elif ooOOo00O00Oo == 9002 :
 oooooo0OO ( )
elif ooOOo00O00Oo == 9003 :
 ii1iI11IiIIi ( )
elif ooOOo00O00Oo == 9004 :
 World1 ( )
elif ooOOo00O00Oo == 9005 :
 World2 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9006 :
 World3 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9007 :
 oOO0o ( )
elif ooOOo00O00Oo == 9008 :
 ooIi11II1IIIIIi ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9009 :
 Oo0ooOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9010 :
 o0OoOoOo0O ( )
elif ooOOo00O00Oo == 9011 :
 IiIOOOoo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 50 :
 o0Oi11i1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9020 :
 champlist ( )
elif ooOOo00O00Oo == 9021 :
 iiI1 ( )
elif ooOOo00O00Oo == 9022 :
 OoIII ( )
elif ooOOo00O00Oo == 9023 :
 OO00O ( )
elif ooOOo00O00Oo == 9024 :
 II1Iii1I1II1i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9030 :
 I1Ii11iI11ii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9031 :
 oOo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9032 :
 ii1II ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9033 :
 OOo00o0o0O0oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 9034 :
 i11OOoo ( )
elif ooOOo00O00Oo == 7085 :
 iIiii1IIi1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7086 :
 IiI1I1i1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 7087 :
 ii1O0oOOo ( iII1111III1I )
elif ooOOo00O00Oo == 9666 :
 OO0Oooo0oOO0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10100 : oOOO00 ( )
elif ooOOo00O00Oo == 101001 : Iii1IIII1Iii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10105 : ooooOoOooo00Oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10106 : ooo00O0OOo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10104 : oOoo00 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10107 : OOOOOOo0o0O0o ( )
elif ooOOo00O00Oo == 10103 : IiI1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10108 : oooo00Oo0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10000 : Origin_Menu ( )
elif ooOOo00O00Oo == 10001 : OoOOo000o0 ( )
elif ooOOo00O00Oo == 10002 : oOOO0o ( )
elif ooOOo00O00Oo == 10003 : I1IiI11 ( )
elif ooOOo00O00Oo == 10004 : o0O0O0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10005 : I1oOO0o0 ( )
elif ooOOo00O00Oo == 10006 : o0Oo0oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10007 : Ii1Iiii ( ooO0oOOooOo0 , I1i1i1 )
elif ooOOo00O00Oo == 10008 : iI1111i1i1ii ( )
elif ooOOo00O00Oo == 10009 : IiiIiI1IIi1IIIii ( )
elif ooOOo00O00Oo == 10010 : OOOOOoooO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10011 : iIIO0ooo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10012 : Ii1IIiI1i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10109 : oO0OooO00Oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10013 : Oo00oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10014 : oOoo0ooOoo ( )
elif ooOOo00O00Oo == 10015 : o0oOo0OO ( )
elif ooOOo00O00Oo == 10016 : I1i11ii11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10017 : Oooooooo00o00 ( )
elif ooOOo00O00Oo == 10018 : iIi1i ( )
elif ooOOo00O00Oo == 10019 : I1i11I11Iii ( )
elif ooOOo00O00Oo == 10020 : I111 ( )
elif ooOOo00O00Oo == 10021 : II1i ( )
elif ooOOo00O00Oo == 10022 : O00oO0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10023 : I1IIii11 ( Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10024 : OOooOoO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10025 : I1IIIiIiIi ( )
elif ooOOo00O00Oo == 10026 : ii111I11Ii ( )
elif ooOOo00O00Oo == 10027 : OooO0O ( )
elif ooOOo00O00Oo == 10028 : ooO0 ( )
elif ooOOo00O00Oo == 10029 : oOo ( )
elif ooOOo00O00Oo == 423 : oooo0o0OOO0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 426 : o00OOOOOo0OOo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10030 : Izle_Films ( )
elif ooOOo00O00Oo == 10031 : Latest_Izle_Movies ( )
elif ooOOo00O00Oo == 10032 : Izle_Genres ( )
elif ooOOo00O00Oo == 10033 : Izle_Pop_Movies ( )
elif ooOOo00O00Oo == 10034 : Izle_Boxsets ( )
elif ooOOo00O00Oo == 10035 : Izle_Search ( )
elif ooOOo00O00Oo == 10036 : Izle_Genres_Movie ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10037 : Izle_Boxset_single ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10038 : Izle_IFRAME ( )
elif ooOOo00O00Oo == 10039 : Izle_Boxsets_Next ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10040 : iI1I ( )
elif ooOOo00O00Oo == 10041 : ooOOO0ooO0o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10042 : oOoo0OO0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10043 : I11IiI1i ( )
elif ooOOo00O00Oo == 10044 : iI11IiIiiII1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10045 : IIi1I ( Oo0O00O000 )
elif ooOOo00O00Oo == 10046 : i111 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10047 : OoO000oo000o0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10048 : o0Ii11iIiiI ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10049 : OoOO00oo0o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10050 : OO ( )
elif ooOOo00O00Oo == 10051 : IiiII1I ( )
elif ooOOo00O00Oo == 10052 : iI1iI1iIi1ii1I1 ( )
elif ooOOo00O00Oo == 10053 : Addon ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10054 : Iii1I ( ooO0oOOooOo0 , Oo0O00O000 )
elif ooOOo00O00Oo == 10055 :
 I1i1II111Iii1 ( "addFavorite" )
 try :
  Oo0O00O000 = Oo0O00O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0O00O000 = Oo0O00O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0Oo0O00o0oo0OO ( Oo0O00O000 , ooO0oOOooOo0 , I1i1i1 , ooO0oooOO0 , o0oOoooOoo0 )
elif ooOOo00O00Oo == 10056 :
 I1i1II111Iii1 ( "rmFavorite" )
 try :
  Oo0O00O000 = Oo0O00O000 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0O00O000 = Oo0O00O000 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOo0ooO0 ( Oo0O00O000 )
elif ooOOo00O00Oo == 10057 :
 I1i1II111Iii1 ( "getFavorites" )
 oO0OOO00 ( )
elif ooOOo00O00Oo == 10058 : O00Ooo ( )
elif ooOOo00O00Oo == 10059 : Donators_Guide ( )
elif ooOOo00O00Oo == 10060 : oo0 ( )
elif ooOOo00O00Oo == 10061 : Ooo0oO0 ( )
elif ooOOo00O00Oo == 10062 : IiII1iiIiI ( Oo0O00O000 , ooO0oOOooOo0 , iII1111III1I )
elif ooOOo00O00Oo == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif ooOOo00O00Oo == 10064 : OOOo ( )
elif ooOOo00O00Oo == 10065 : Ooo0O0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10066 : II1i1III ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10068 : oOoO00o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10069 : i1Iii11I1i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10070 : IiiIIiiiiii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10071 : Genie_Watch ( )
elif ooOOo00O00Oo == 10072 : iiIII1II ( )
elif ooOOo00O00Oo == 10073 : ooOoOo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10074 : o0O0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10075 : iiIii1IIi ( I1i1i1 , Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10076 : IIi11I1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10077 : iiiI1ii11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10078 : iIII11Ii ( )
elif ooOOo00O00Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif ooOOo00O00Oo == 10080 : Genie_Watch_Tv_Genre ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10081 : Genie_Watch_TV_PlayRun ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10082 : Genie_Watch_TV_Episodes ( ooO0oOOooOo0 , I1i1i1 )
elif ooOOo00O00Oo == 10083 : Genie_Watch_Tv_Recent ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 10084 : IIioOoO00oo0O ( )
elif ooOOo00O00Oo == 10085 : OOoO00 ( )
elif ooOOo00O00Oo == 10086 : i1IiiiI1iI ( )
elif ooOOo00O00Oo == 20000 : iiI1II11II1i ( )
elif ooOOo00O00Oo == 20001 : OO0OoO0o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 20002 : IIIIIIi1IiIi ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 20003 : Ii1IIIi ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 20004 : OOoo000O00O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 20005 : ii1iIIi11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 21004 : iiI11I1i1i1iI ( )
elif ooOOo00O00Oo == 21005 : O00OoOoO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 21006 : o0O0OOo0oO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 21007 : i1ii1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30000 : iIIIiI ( )
elif ooOOo00O00Oo == 30001 : Oo0 ( )
elif ooOOo00O00Oo == 10012 : Resolve ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30003 : OOooO0Oo00 ( )
elif ooOOo00O00Oo == 30004 : o0oOoO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30005 : IIiO0Oo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30006 : I1II ( )
elif ooOOo00O00Oo == 30007 : iIII11Iiii1 ( )
elif ooOOo00O00Oo == 30008 : iIi11iiI11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30009 : ooo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30010 : iI111II1ii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30011 : o0oo0O0oOoooO ( )
elif ooOOo00O00Oo == 30012 : i1oOOO0ooOO ( )
elif ooOOo00O00Oo == 30013 : IIii1III ( )
elif ooOOo00O00Oo == 30014 : I1ii1Ii1 ( )
elif ooOOo00O00Oo == 30015 : Oo0O0OOO0o0O ( ooO0oOOooOo0 , I1i1i1 , ooO0oooOO0 )
elif ooOOo00O00Oo == 30016 : iIi1i1iIi1Ii1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30019 : oOOOoo0o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30017 : o0Oo0oO00OOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30018 : ooOoo0OoOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30030 : oOo0oOooo0O ( )
elif ooOOo00O00Oo == 30031 : OOo0 ( )
elif ooOOo00O00Oo == 30032 : iI1iIii11Ii ( )
elif ooOOo00O00Oo == 30033 : iI1iIIIIIiIi1 ( )
elif ooOOo00O00Oo == 30034 : iIi ( )
elif ooOOo00O00Oo == 30035 : IIi1IiII ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30036 : o0IIIIiI11I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30037 : iiiI11iIIi1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 30038 : O0o00o000oO ( )
elif ooOOo00O00Oo == 30039 : oO0O0OO0O ( )
elif ooOOo00O00Oo == 50000 : oOO0O00Oo0O0o ( )
elif ooOOo00O00Oo == 50001 : IiI1iI1IiiIi1 ( )
elif ooOOo00O00Oo == 50002 : oOoOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 50003 : iIIii1i1Ii11 ( iII1111III1I )
elif ooOOo00O00Oo == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif ooOOo00O00Oo == 60001 : i111i11I1ii ( )
elif ooOOo00O00Oo == 60002 : OoOo ( Oo0O00O000 )
elif ooOOo00O00Oo == 60003 : i1iiIIi11I ( Oo0O00O000 )
elif ooOOo00O00Oo == 50004 : II1i111Ii1i ( )
elif ooOOo00O00Oo == 50005 : speedtest . runtest ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 70001 : I1II1I1I ( )
elif ooOOo00O00Oo == 70002 : I1iiIiiii1111 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 70003 : I1ii1i11i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 70004 : Oooooo0O00o ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 70005 : II11ii1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 70006 : ii1II1II ( )
elif ooOOo00O00Oo == 50006 : OOOiiiiI ( i1 , i1111 )
elif ooOOo00O00Oo == 80000 : oO0O0oO0 ( )
elif ooOOo00O00Oo == 80001 : resolvefilmon ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80002 : IiiIiIi111iI1 ( )
elif ooOOo00O00Oo == 80003 : iii11i1 ( Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80004 : iIii1I ( Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80005 : O0O0Oo00 ( )
elif ooOOo00O00Oo == 80006 : O00oo0ooO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80007 : iiIii1ii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80008 : iIIIII1iiiiII ( )
elif ooOOo00O00Oo == 80009 : OO000OOOo0Oo ( )
elif ooOOo00O00Oo == 80010 : Oo00O0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80011 : iIiiI1I ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 80012 : I1I11i ( )
elif ooOOo00O00Oo == 90000 : IiiIiiIIII ( Oo0O00O000 , ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90001 : I1I1i1I ( )
elif ooOOo00O00Oo == 90002 : oOO0OOOo ( )
elif ooOOo00O00Oo == 90003 : IiIiII11i1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90004 : Ii1I1iIiiI1 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90005 : o00i111iiIiiIiI ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90006 : ooo0O0O0oo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90007 : oo000oO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90008 : OOOOOO ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90009 : oooo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90010 : oooOo0OOOoo0 ( )
elif ooOOo00O00Oo == 90020 : I11II11111i11 ( )
elif ooOOo00O00Oo == 90021 : hellyeah2 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90022 : hellyeah3 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90023 : O00o00O ( )
elif ooOOo00O00Oo == 90024 : I11Oo00oO0O ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90025 : catchuptv2 ( ooO0oOOooOo0 )
if 31 - 31: O0oOO0 . iiII11i1I1IIi - oo0oO00 . iI11I1II1I1I + oo0oO00 . OOooOOo
elif ooOOo00O00Oo == 90030 : OOoO ( )
elif ooOOo00O00Oo == 90031 : IiIi11iI ( )
elif ooOOo00O00Oo == 90032 : i11I1IiII1i1i ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90033 : iIIii ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 90034 : ooOoO00 ( ooO0oOOooOo0 )
if 86 - 86: Ii1I - Ii1I / iiII11i1I1IIi - Ii1I * iiII11i1I1IIi + OooOO000
if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - iIi1i1ii1
elif ooOOo00O00Oo == 100001 : Stand_up ( )
if 30 - 30: ii % Oooo0O0oo00oO
elif ooOOo00O00Oo == 100003 : I1i11ii11 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100004 : o00oOoOo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100005 : Resolve ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100008 : Search ( )
elif ooOOo00O00Oo == 100007 : Oooo0 ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100009 : yt . PlayVideo ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100010 : Ii1ii1IiIII ( ooO0oOOooOo0 )
elif ooOOo00O00Oo == 100100 : oOOoo ( I1i1i1 , ooO0oOOooOo0 , OoO0O00o0ooo0 )
elif ooOOo00O00Oo == 100101 : i11iiI1111 ( ooO0oOOooOo0 , Oo0O00O000 , ooO0oooOO0 , OoO0O00o0ooo0 , I1i1i1 )
elif ooOOo00O00Oo == 100102 : I1Iiiiiii ( Oo0O00O000 , ooO0oOOooOo0 , I1i1i1 , ooO0oooOO0 )
elif ooOOo00O00Oo == 100106 : ooo ( ooO0oOOooOo0 , Oo0O00O000 )
elif ooOOo00O00Oo == 100107 : O0Oo00 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
