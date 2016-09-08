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
IiiIII111iI = "3.1.1"
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
i11 = xbmc . translatePath ( 'special://home/' )
I11 = os . path . join ( i11 , 'userdata' )
Oo0o0000o0o0 = os . path . join ( I11 , 'addon_data' , IiII )
oOo0oooo00o = os . path . join ( Oo0o0000o0o0 , 'wizard.log' )
oO0o0o0ooO0oO = uservar . ADDONTITLE
oo0o0O00 = xbmc . translatePath ( 'special://profile/' )
oO = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1iiIIiiI111 = Net ( )
oooOOOOO = xbmcgui . Dialog ( )
i1iiIII111ii = base64 . decodestring
i1iIIi1 = oo00 . getSetting ( 'Build' )
ii11iIi1I = oo00 . getSetting ( 'Local' )
iI111I11I1I1 = oo00 . getSetting ( 'Remote' )
OOooO0OOoo = oo00 . getSetting ( 'LocalM3u' )
iIii1 = oo00 . getSetting ( 'TEXTCOL' )
oOOoO0 = xbmc . translatePath ( 'special://logpath/' )
O0OoO000O0OO = oo00 . getSetting ( 'User' )
iiI1IiI = oo00 . getSetting ( 'Pass' )
II = oo00 . getSetting ( 'AdultPass' )
oooOOOOO = xbmcgui . Dialog ( )
i11 = xbmc . translatePath ( 'special://home/' )
ooOoOoo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
OooO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
II11iiii1Ii = ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OO0o = xbmc . translatePath ( 'special://database' )
Ooo = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
O0o0Oo = xbmc . translatePath ( 'special://thumbnails' ) ;
Oo00OOOOO = "GenieTv"
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
O00o0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
I11i1 = 'http://'
iIi1ii1I1 = base64 . decodestring ( 'LnBocA==' )
o0 = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
I11II1i = [ ]
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
IIiiiiiiIi1I1 = oo00 . getLocalizedString
I1IIIii = CookieJar ( )
oOoOooOo0o0 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( I1IIIii ) )
oOoOooOo0o0 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOOO = int ( sys . argv [ 1 ] )
OOO00 = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iiiiiIIii = os . path . join ( Ooo , 'favorites' )
O000OO0 = Ooo + '/addons.ini'
I11 = xbmc . translatePath ( 'special://home/userdata/' )
I11iii1Ii = xbmc . translatePath ( 'special://home/userdatabroke/' )
I1IIiiIiii = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
O000oo0O = xbmc . translatePath ( 'special://home/userdata/addon_data' )
OOOOi11i1 = O000oo0O + 'GenieTvWatched'
if not os . path . exists ( OOOOi11i1 ) :
 os . makedirs ( OOOOi11i1 )
IIIii1II1II = OOOOi11i1 + 'watched.txt'
if not os . path . exists ( IIIii1II1II ) :
 open ( IIIii1II1II , 'w+' )
i1I1iI = open ( IIIii1II1II ) . read ( )
oo0OooOOo0 = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
o0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
O00oO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I11i1I1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
oO0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
oOOoo0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( iiiiiIIii ) == True :
 o00OO00OoO = open ( iiiiiIIii ) . read ( )
else : o00OO00OoO = [ ]
OOOO0OOoO0O0 = oo00 . getSetting ( 'debug' )
if os . path . exists ( Ooo ) == False :
 os . makedirs ( Ooo )
def O0Oo000ooO00 ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1iIiII1ii1 = ''
 ooOooo000oOO = ''
 try :
  Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
  ooOooo000oOO = Ii1iIiII1ii1 . read ( )
  Ii1iIiII1ii1 . close ( )
 except : pass
 if ooOooo000oOO != '' :
  return ooOooo000oOO
 else :
  ooOooo000oOO = 'Failed'
  return ooOooo000oOO
  if 59 - 59: IIIi + O0OoO - oO0o0OOOO % O0O0OoOO0
iiiI1I11i1 = [ ]
IIi1i11111 = O0Oo000ooO00 ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if IIi1i11111 != 'Failed' :
 iiiI1I11i1 . append ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not IIi1i11111 != 'Failed' :
 ooOO00O00oo = O0Oo000ooO00 ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if ooOO00O00oo != 'Failed' :
  iiiI1I11i1 . append ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not ooOO00O00oo != 'Failed' :
  I1ii11iI = O0Oo000ooO00 ( i1iiIII111ii ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if I1ii11iI != 'Failed' :
   iiiI1I11i1 . append ( i1iiIII111ii ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not I1ii11iI != 'Failed' :
   IIi1i = O0Oo000ooO00 ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if IIi1i != 'Failed' :
    iiiI1I11i1 . append ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
I1I1iIiII1 = ( str ( iiiI1I11i1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
i11i1I1 = I1I1iIiII1 + 'GenieArt/NEW/'
if 36 - 36: IIIIi1i / ooo0oo0o0oo . iii1iiii1
if 53 - 53: OO0 + O0O0OoOO0 . I11i * OO0 + o0o00Oo0O
def iI1iiIiiII ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  oooOOOOO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIIi11I1 = 'genie tv repo not being installed '
  ooOOOoO ( )
 else :
  o0o ( )
  if 84 - 84: o0o00Oo0O
def o0o ( ) :
 if 74 - 74: Ii1I - oOo0O0Ooo - I1ii11iIi11i . O0O0OoOO0 - ooo0oo0o0oo
 OOOoOoo0O = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 oo0OOo = open ( oO0Oo ) . read ( )
 ooOOO00Ooo = open ( oOOoo0Oo ) . read ( )
 if 16 - 16: IIiIiII11i % OOooOOo - IIiIiII11i + O0O0OoOO0
 i1I1i = re . compile ( 'version="([^"]*)" provider' ) . findall ( oo0OOo )
 Iiiii1i = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( ooOOO00Ooo )
 I11i1ii1 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( OOOoOoo0O )
 O0Oooo0O = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( OOOoOoo0O )
 for O0o in i1I1i :
  OoOooO = O0o
  for II111iiiI1Ii in I11i1ii1 :
   if not II111iiiI1Ii == OoOooO :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    o0O0OOO0Ooo ( )
   if II111iiiI1Ii == OoOooO :
    iiIiI
 for I1 in Iiiii1i :
  OOO00O0O = I1
  for iii in O0Oooo0O :
   if not iii == OOO00O0O :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    ooOOOoO ( )
   if iii == OOO00O0O :
    xbmc . sleep ( 100 )
    iiIiI
def oOooOOOoOo ( ) :
 iI1iiIiiII ( )
 i1Iii1i1I ( )
 OOoO00 ( IiI111111IIII )
 if 37 - 37: iii1iiii1 / OOooOOo
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']CONTACT US[/COLOR]' , '' , 50006 , i11i1I1 + 'Contact-Us.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , i11i1I1 + 'settings.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']Force Genie Update Kodi 16+[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , i11i1I1 + 'GenieUpdate.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']WIZARD[/COLOR]' , str ( I1I1iIiII1 ) , 4001 , i11i1I1 + 'Wizard.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']STREAMS[/COLOR]' , str ( I1I1iIiII1 ) , 4002 , i11i1I1 + 'Streams.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']Music[/COLOR]' , str ( I1I1iIiII1 ) , 4003 , i11i1I1 + 'Music.png' , ooOoOoo0O , '' )
  if 84 - 84: OO0 * IIiIiII11i + I1ii11iIi11i
 if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1I1iIiII1 ) , 32 , i11i1I1 + 'BuildersToolbox.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Source List' ) == 'true' :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']SOURCE LIST[/COLOR]' , str ( I1I1iIiII1 ) , 46 , i11i1I1 + 'SoruceList.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']MAINTENANCE[/COLOR]' , str ( I1I1iIiII1 ) , 3 , i11i1I1 + 'Maintenance.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Addons' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']ADDONS[/COLOR]' , '' , 10050 , i11i1I1 + 'Addons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'APK Tool' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']APK TOOL[/COLOR]' , str ( I1I1iIiII1 ) , 30039 , i11i1I1 + 'APKTools.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']GenieTv RSS Feed[/COLOR]' , str ( I1I1iIiII1 ) , 39 , i11i1I1 + 'GenieTVRSSFeed.png' , ooOoOoo0O , '' )
  if 53 - 53: IIIIi1i % IIiIiII11i . ooo0oo0o0oo - iI11I1II1I1I - ooo0oo0o0oo * IIiIiII11i
  if 77 - 77: iI11I1II1I1I * oO0o
 oOooOo0 ( 'movies' , 'MAIN' )
def i1I1ii11i1Iii ( ) :
 I1IiiiiI = o0OIiII ( )
 ii1iII1II = I1IiiiiI . replace ( oOOoO0 , "" )
 if os . path . exists ( I1IiiiiI ) or not I1IiiiiI == False :
  Iii1I1I11iiI1 = open ( I1IiiiiI , mode = 'r' ) ; I1I1i1I = Iii1I1I11iiI1 . read ( ) ; Iii1I1I11iiI1 . close ( )
  ii1I ( "%s - %s" % ( i1 , ii1iII1II ) , I1I1i1I )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def o0OIiII ( ) :
 O0oO0 = False
 if os . path . exists ( os . path . join ( oOOoO0 , 'xbmc.log' ) ) :
  O0oO0 = os . path . join ( oOOoO0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( oOOoO0 , 'kodi.log' ) ) :
  O0oO0 = os . path . join ( oOOoO0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( oOOoO0 , 'spmc.log' ) ) :
  O0oO0 = os . path . join ( oOOoO0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( oOOoO0 , 'tvmc.log' ) ) :
  O0oO0 = os . path . join ( oOOoO0 , 'tvmc.log' )
 return O0oO0
 if 87 - 87: I1ii11iIi11i . ooo0oo0o0oo
def O0OO0O ( url ) :
 if url == 'http://' : return False
 try :
  oO0 = urllib2 . Request ( url )
  oO0 . add_header ( 'User-Agent' , I1i1iiI1 )
  Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
  Ii1iIiII1ii1 . close ( )
 except Exception , OO :
  return OO
 return True
 if 83 - 83: o0o00Oo0O / oOo0O0Ooo - oO0o - O0OoO
def iI1i11iII111 ( ) :
 ooOooo000oOO = O000OOo00oo ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( ooOooo000oOO )
 if len ( i1I1i ) > 0 :
  for Iii1IIII11I , IiI111111IIII , OOOoo0OO , oO0o0 in i1I1i :
   i1I1iI1iIi111i ( Iii1IIII11I , IiI111111IIII , 50005 , OOOoo0OO , oO0o0 , '' )
def iI1Ii11iIiI1 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1iIiII1 ) , 10060 , i11i1I1 + 'BackupMyBuild.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1iIiII1 ) , 49 , i11i1I1 + 'RestoreMyBuild.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']WIPE GENIE[/COLOR]' , str ( I1I1iIiII1 ) , 41 , i11i1I1 + 'WipeGenie.png' , ooOoOoo0O , '' )
 if 86 - 86: IIIi * I11i % ooOoO0O00 . O0O0OoOO0 . Ii
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Genie BUILDS[/COLOR]' , str ( I1I1iIiII1 ) , 44 , i11i1I1 + 'GenieBuilds.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
def oOOoo00O00o ( ) :
 iI1iiIiiII ( )
 if II == '5knuckleshuffle' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']XVID[/COLOR]' , str ( I1I1iIiII1 ) , 10100 , i11i1I1 + 'Jizbox.png' , ooOoOoo0O , '' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']ADULT CHANNELS[/COLOR]' , str ( I1I1iIiII1 ) , 30033 , i11i1I1 + 'adu.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Favourites' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']FAVOURITES[/COLOR]' , str ( I1I1iIiII1 ) , 10057 , i11i1I1 + 'Favourites.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Search' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH[/COLOR]' , str ( I1I1iIiII1 ) , 9000 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']G-Tv Live List[/COLOR]' , '' , 4009 , i11i1I1 + 'GTV.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']TV GUIDE[/COLOR]' , '' , 10063 , i11i1I1 + 'TvGuide.png' , ooOoOoo0O , '' )
  if 98 - 98: O0OoO + ooo0oo0o0oo + IIIi % ii
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']STREAM TEAM[/COLOR]' , str ( I1I1iIiII1 ) , 4006 , i11i1I1 + 'StreamTeam.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MOVIES[/COLOR]' , str ( I1I1iIiII1 ) , 4004 , i11i1I1 + 'Movies.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']TV SHOWS[/COLOR]' , str ( I1I1iIiII1 ) , 4005 , i11i1I1 + 'TVShows.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']FOOTBALL[/COLOR]' , '' , 10002 , i11i1I1 + 'Football.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']KIDS[/COLOR]' , str ( I1I1iIiII1 ) , 4007 , i11i1I1 + 'Kids.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']24/7 STREAMS[/COLOR]' , '' , 30030 , i11i1I1 + '247Streams.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEWS[/COLOR]' , str ( I1I1iIiII1 ) , 30032 , i11i1I1 + 'News.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']GenieTv TUTORIALS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , i11i1I1 + 'GenieTVTutorials.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HOBBIES[/COLOR]' , str ( I1I1iIiII1 ) , 4008 , i11i1I1 + 'Hobbies.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'YOUTUBE' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH YOUTUBE[/COLOR]' , str ( I1I1iIiII1 ) , 10064 , i11i1I1 + 'SeachYouTube.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'REQUESTS' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']REQUESTS[/COLOR]' , str ( I1I1iIiII1 ) + ( i1iiIII111ii ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , i11i1I1 + 'Requests.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Stand Up' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']STAND UP[/COLOR]' , '' , 10003 , i11i1I1 + 'StandUp.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Documentaries' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']DOCUMENTARIES[/COLOR]' , str ( I1I1iIiII1 ) , 8040 , i11i1I1 + 'documentaries.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Disclose' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']DISCLOSE TV[/COLOR]' , str ( I1I1iIiII1 ) , 7001 , i11i1I1 + 'DiscloseTV.png' , ooOoOoo0O , '' )
  if 97 - 97: o0o00Oo0O * ii . ii
  if 33 - 33: iii1iiii1 + IIIIi1i * IIIi / iI11I1II1I1I - oOo0O0Ooo
 if oo00 . getSetting ( 'Playlist Loader' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']PLAYLIST LOADER[/COLOR]' , str ( I1I1iIiII1 ) , 3000 , i11i1I1 + 'PlaylistLoader.png' , ooOoOoo0O , '' )
  if 54 - 54: iii1iiii1 / O0OoO . IIIi % IIIIi1i
  if 57 - 57: Ii . Ii1I - O0O0OoOO0 - IIIi + OOooOOo
  if 63 - 63: OOooOOo * IIIIi1i
  if 69 - 69: o0o00Oo0O . oO0o
  if 49 - 49: oOo0O0Ooo - oO0o0OOOO
  if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
  if 62 - 62: ii * oOo0O0Ooo
  if 58 - 58: OOooOOo % I11i
  if 50 - 50: iii1iiii1 . I11i
  if 97 - 97: o0o00Oo0O + OOooOOo
  if 89 - 89: I11i + oO0o * oO0o0OOOO * O0O0OoOO0
  if 37 - 37: ii - o0o00Oo0O - I11i
 oOooOo0 ( 'movies' , 'MAIN' )
 if 77 - 77: O0OoO * iI11I1II1I1I
def i1Iii1i1I ( ) :
 if not os . path . exists ( O00o0OO ) :
  ii1I ( 'Change Log 5/9/16 - v3.1.0' , 'GenieTv now clears cache on every start-up, Force close on all platforms Android included, RaysRavers added to music section, RadioNomy section added to music, Quicksilver fixed in music, WatchSeries fixed now playing from genres, Go fishing work in progress, View log file from within maintenance, Speedtest added to maintenance section, GenieTv contact information within addon, Search tweaked performing faster and more sources, Tv theme tunes section added to music, new servers online' )
  os . makedirs ( O00o0OO )
  if 98 - 98: oOo0O0Ooo % O0O0OoOO0 * ii
  if 51 - 51: iI11I1II1I1I . OOooOOo / IIIi + I11i
def I11iI1i1I11I11 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH MOVIES[/COLOR]' , str ( I1I1iIiII1 ) , 9001 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']POPCORN BOX[/COLOR]' , str ( I1I1iIiII1 ) , 7061 , i11i1I1 + 'PopcornBox.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Film Trailers[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , i11i1I1 + 'FilmTrailers.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , i11i1I1 + 'ClassicMovies.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
def o000O0O ( ) :
 iI1iiIiiII ( )
 I1i1i1iii ( )
 if 16 - 16: O0O0OoOO0 + ooo0oo0o0oo * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
 if 67 - 67: ii / oOo0O0Ooo * O0O0OoOO0 + oO0o0OOOO
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live Sport On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']TV GUIDE[/COLOR]' , '' , 10063 , i11i1I1 + 'TvGuide.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']Link GTV to Guide[/COLOR]' , '' , 4010 , i11i1I1 + 'linkchannels.png' , ooOoOoo0O , '' )
 if 65 - 65: ii - Ii1I / OO0 / IIiIiII11i / ooOoO0O00
 if 71 - 71: iii1iiii1 + O0O0OoOO0
def iI1111ii1I ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH SERIES[/COLOR]' , str ( I1I1iIiII1 ) , 9002 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if 45 - 45: ooOoO0O00 + I11i
 if 94 - 94: IIIi . ooOoO0O00 - I11i % o0o00Oo0O - oO0o
 if oo00 . getSetting ( 'Watch Series' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']WATCH SERIES[/COLOR]' , '' , 10040 , i11i1I1 + 'WatchSeries.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']iWATCH SERIES[/COLOR]' , '' , 8020 , i11i1I1 + 'iWatchSeries.png' , ooOoOoo0O , '' )
 if 72 - 72: O0O0OoOO0
 if 1 - 1: oO0o * ooo0oo0o0oo * ii + OO0
 if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CLASSIC TV[/COLOR]' , str ( I1I1iIiII1 ) , 8064 , i11i1I1 + 'ClassicTV.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']TV Show Trailers[/COLOR]' , i1iiIII111ii ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , i11i1I1 + 'TVShowTrailers.png' , ooOoOoo0O , '' )
 if 33 - 33: o0o00Oo0O * I11i - iii1iiii1 % iii1iiii1
 oOooOo0 ( 'movies' , 'MAIN' )
def I11I ( ) :
 iI1iiIiiII ( )
 if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']SILENT HUNTER[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'The Reaper' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']THE REAPER[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , i11i1I1 + 'TheReaper.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']PANDORAS BOX[/COLOR]' , str ( I1I1iIiII1 ) , 10025 , i11i1I1 + 'PandorasBox.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Redemption Streams' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']Redemption Streams[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , i11i1I1 + 'RedemptionStreams.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']DoJo STREAMS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , i11i1I1 + 'DojoStreams.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1iIiII1 ) , 1023 , i11i1I1 + 'ScoobyStreams.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'HeroVision' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']HEROVISION[/COLOR]' , '' , 1017 , i11i1I1 + 'Herovision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ITV[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , i11i1I1 + 'ITVStreams.png' , ooOoOoo0O , '' )
 if 50 - 50: iii1iiii1 * Ii * iI11I1II1I1I - IIiIiII11i * I11i * OOooOOo
 oOooOo0 ( 'movies' , 'MAIN' )
 if 94 - 94: ii + ii . IIiIiII11i + oO0o0OOOO / Ii1I % O0O0OoOO0
def I1Ii1iiiiii1 ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']SILENT HUNTER[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SERVER 1[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SERVER 2[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
def ooO0oooOO0 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 url = url
 i1I1i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( o0ooo0 )
 for iiIiIIIiiI , iiI1IIIi in i1I1i :
  if '[DIR]' in iiIiIIIiiI :
   II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + iiI1IIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iiI1IIIi , 1018 , i11i1I1 + 'SilentHunter.png' )
  if 'mkv' in iiI1IIIi :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + iiI1IIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iiI1IIIi , 222 , i11i1I1 + 'SilentHunter.png' )
  if 'avi' in iiI1IIIi :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + iiI1IIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iiI1IIIi , 222 , i11i1I1 + 'SilentHunter.png' )
   if 18 - 18: oO0o0OOOO - Ii / IIiIiII11i . O0OoO
def OoOo00o0O00 ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HEROVISION[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , i11i1I1 + 'Herovision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HEROVISION SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , i11i1I1 + 'Herovision.png' , ooOoOoo0O , '' )
 if 2 - 2: Ii . Ii1I
def oOoo0oOo00 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , i11i1I1 + 'SearchCartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'WCO' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1iIiII1 ) , 21004 , i11i1I1 + 'watchcartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Cartoons' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CARTOONS[/COLOR]' , '' , 10001 , i11i1I1 + 'Cartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Anime' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']AnimeLand[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , i11i1I1 + 'anime.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
def IiiiIiii11 ( ) :
 iI1iiIiiII ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']FOOTBALL[/COLOR]' , '' , 10002 , i11i1I1 + 'Football.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']FITNESS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , i11i1I1 + 'Fitness.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']Go Fishing[/COLOR]' , str ( I1I1iIiII1 ) , 8090 , i11i1I1 + 'GoFishing.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']GenieTv Kitchen[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , i11i1I1 + 'GenieTVKitchen.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 92 - 92: OOooOOo + iii1iiii1 * O0O0OoOO0 % oOo0O0Ooo
 if 42 - 42: I1ii11iIi11i
 if 76 - 76: oOo0O0Ooo * IIIIi1i % iii1iiii1
def iiIiI ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1I1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIi1i11111 )
 for IIIi11I1 in i1I1i :
  IIIi11I1 = ( str ( IIIi11I1 ) )
  if os . path . exists ( xbmc . translatePath ( IIIi11I1 ) ) :
   OoooO00o = ( IIIi11I1 ) . replace ( 'special://home/addons/' , '' )
   ii1I ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OoooO00o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   o0O0o = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if o0O0o == 0 :
    OO0o0o00 ( IIIi11I1 )
    IiIi1I1 ( )
   elif o0O0o == 1 :
    IiIIi1 ( IIIi11I1 )
  else :
   pass
   if 47 - 47: I1ii11iIi11i * Ii1I + iI11I1II1I1I / iii1iiii1 / oO0o - ii
def IiIIi1 ( addon ) :
 OoooO00o = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 33 - 33: OOooOOo * O0OoO - IIiIiII11i
def OO0o0o00 ( addon ) :
 oooOOOOO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOo0o0O0O = os . path . join ( O0O , 'default.py' )
 o0OO0o0oOOO0O = open ( OOo0o0O0O , "w+" )
 if 49 - 49: Ii1I . I11i . IIiIiII11i
 o0OO0o0oOOO0O . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o0OO0o0oOOO0O . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o0OO0o0oOOO0O . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 98 - 98: IIIIi1i
 if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
 if 38 - 38: OO0 - O0OoO / IIIIi1i
 if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / O0O0OoOO0 + Ii1I
 if 86 - 86: I11i
 if 5 - 5: ooo0oo0o0oo * OOooOOo
 if 5 - 5: iii1iiii1
 if 90 - 90: iii1iiii1 . OO0 / O0O0OoOO0 - oO0o0OOOO
 if 40 - 40: ii
 if 25 - 25: ooo0oo0o0oo + O0O0OoOO0 / OO0 . I11i % o0o00Oo0O * oO0o
 if 84 - 84: OO0 % O0O0OoOO0 + Ii
 if 28 - 28: I1ii11iIi11i + oO0o * O0OoO % IIIi . oO0o0OOOO % o0o00Oo0O
 if 16 - 16: oO0o0OOOO - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
 if 19 - 19: oO0o - I1ii11iIi11i . o0o00Oo0O
 if 60 - 60: IIiIiII11i + I1ii11iIi11i
 if 9 - 9: OO0 * ii - iI11I1II1I1I + OOooOOo / oO0o . oO0o
 if 49 - 49: IIiIiII11i
 if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * IIIi
 if 81 - 81: IIIIi1i + ooo0oo0o0oo
def o0oo0 ( ) :
 iiIi1IIi1I ( 'Genre' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Most Viewed' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Box Office' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Search' , '' , 10078 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 if 97 - 97: OOooOOo % Ii1I
def iIiIII1I1I1 ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'http://imoviemax.se/?s=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1IIIi = III11I1 . lower ( )
 O00Ooo ( IIi1IIIi )
def OOOO0OOO ( url ) :
 i1i1ii = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iII1ii1 in i1I1i :
  if Iii1IIII11I in i1i1ii :
   pass
  else :
   iiIi1IIi1I ( Iii1IIII11I + ' - ' + iII1ii1 + ' Films' , url , 10074 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
   i1i1ii . append ( Iii1IIII11I )
   if 12 - 12: O0OoO - OO0 . ii / Ii1I . ooOoO0O00 * oO0o
def IiIiII1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , Iii1iiIi1II in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I + ' - Views:' + Iii1iiIi1II , url , 10075 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
  if 60 - 60: oOo0O0Ooo - IIIi * oO0o0OOOO % IIiIiII11i
  if 62 - 62: iI11I1II1I1I
def O00Ooo ( url ) :
 i1II = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIi1i11111 )
 for next in next :
  iiIi1IIi1I ( 'NEXT PAGE' , next , 10074 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 i1I1i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , Iii1IIII11I , url in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 10075 , iI1I , iI1I , '' )
  i1II . append ( Iii1IIII11I )
  if 100 - 100: iI11I1II1I1I + OOooOOo / I1ii11iIi11i . Ii
def III1I1Iii1iiI ( img , name , url ) :
 img = img
 name = name
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIi1i11111 )
 for i1Iii11I1i , url in i1I1i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Oo00o0OO0O00o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Oo00o0OO0O00o
  O0Oooo = ( i1Iii11I1i ) . replace ( 'play-' , 'Server ' )
  i1I1iI1iIi111i ( O0Oooo , Oo00o0OO0O00o , 10076 , img , img , '' )
  if 21 - 21: I1ii11iIi11i
def I1ii1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIi1i11111 )
 for iiI1IIIi in i1I1i :
  if '=m' in iiI1IIIi :
   O00 ( iiI1IIIi )
  elif 'php' in iiI1IIIi :
   I1ii1 ( url )
  else :
   IIi1i11111 = O000OOo00oo ( iiI1IIIi )
   i1I1i = re . compile ( 'content="([^"]*)">' ) . findall ( IIi1i11111 )
   for Oo0o0000OOoO in i1I1i :
    O00 ( iiI1IIIi )
    if 46 - 46: o0o00Oo0O * IIiIiII11i - I1ii11iIi11i * OO0
    if 33 - 33: O0O0OoOO0
    if 74 - 74: O0OoO + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
def oOOO0oo0 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 iIi1i1iIi1iI = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iiIi1iI1iIii , o00OooO0oo in iIi1i1iIi1iI :
  print 'there ><><><><><><><><><><><><'
  iiIi1iI1iIii = iiIi1iI1iIii
  i1I1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o00OooO0oo ) )
  for Iii1IIII11I , o0o0oOoOO0O in i1I1i :
   print 'here <><><><><><><><><><><><>'
   iiIi1IIi1I ( '[COLORred]' + iiIi1iI1iIii + '[/COLOR] - ' + Iii1IIII11I + ' - [COLOR' + iIii1 + ']' + o0o0oOoOO0O + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i11i1I1 + 'loader.png' , ooOoOoo0O , '' )
 i1ii1II1ii = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iiIi1iI1iIii , iII111Ii in i1ii1II1ii :
  print 'there ><><><><><><><><><><><><'
  iiIi1iI1iIii = iiIi1iI1iIii
  i1I1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iII111Ii ) )
  for Iii1IIII11I , o0o0oOoOO0O in i1I1i :
   print 'here <><><><><><><><><><><><>'
   iiIi1IIi1I ( '[COLORred]' + iiIi1iI1iIii + '[/COLOR] - ' + Iii1IIII11I + ' - [COLOR' + iIii1 + ']' + o0o0oOoOO0O + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i11i1I1 + 'loader.png' , ooOoOoo0O , '' )
   if 52 - 52: IIiIiII11i % ooo0oo0o0oo . OOooOOo * iI11I1II1I1I
   if 50 - 50: OO0 - iii1iiii1 * ooo0oo0o0oo . Ii1I
   if 37 - 37: OO0 % Ii % IIiIiII11i . o0o00Oo0O . O0O0OoOO0
def OO0oOOoo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1ii1II1ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
 for i1ii1II1ii in i1ii1II1ii :
  Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
  for Iii1IIII11I in Iii1IIII11I :
   Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1ii1II1ii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oOOO00o000o = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
  for oOOO00o000o in oOOO00o000o :
   oOOO00o000o = 'http:' + oOOO00o000o
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , '' , '' )
  if 9 - 9: IIIi + oO0o0OOOO / oO0o0OOOO
  if 12 - 12: ii % I11i * oO0o0OOOO % iI11I1II1I1I / O0O0OoOO0
  if 27 - 27: Ii % IIiIiII11i % oO0o0OOOO . o0o00Oo0O - I1ii11iIi11i + OOooOOo
  if 57 - 57: iI11I1II1I1I / oO0o0OOOO - ooOoO0O00
def ooOOo00O00Oo ( url ) :
 if 42 - 42: o0o00Oo0O / I11i + ii * OO0 % OO0
 i1iIi = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iiI1IIIi , iI1I , Iii1IIII11I , IIIIIo0ooOoO000oO in i1I1i :
  Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  ooOO00O00oo = O000OOo00oo ( iiI1IIIi )
  Iiiii1i = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( ooOO00O00oo )
  for OOo , i1i11I1I1iii1 in Iiiii1i :
   I1iii11 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
   for ooo0O in I1iii11 :
    if Iii1IIII11I in i1iIi :
     pass
    else :
     i1I1iI1iIi111i ( Iii1IIII11I , OOo , 8043 , iI1I , iI1I , ooo0O )
     oOooOo0 ( 'movies' , 'INFO' )
     i1iIi . append ( Iii1IIII11I )
     if 16 - 16: OOooOOo
     if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . O0OoO
def O0 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , iII1 , ooo0O , oO0o0 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 10065 , iII1 , oO0o0 , ooo0O )
 oOooOo0 ( 'movies' , 'INFO' )
 if 27 - 27: oO0o . oO0o0OOOO + OOooOOo / iI11I1II1I1I % IIIIi1i . OO0
def IIIIi1 ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'https://www.youtube.com/results?search_query=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1IIIi = III11I1 . lower ( )
 IIi1i11111 = O000OOo00oo ( IIi1IIIi )
 i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in next :
  IiI111111IIII = 'https://www.youtube.com' + IiI111111IIII
  iiIi1IIi1I ( '[COLOR' + iIii1 + '] NEXT [/COLOR]' , IiI111111IIII , 10065 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 for iI1I , IiI111111IIII , Iii1IIII11I , iIi11iiIiI1I , i1i11I1I1iii1 in i1I1i :
  I11II1i . append ( Iii1IIII11I )
  oOooOo0 ( 'tvshows' , 'INFO' )
  oOOO00o000o = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOO00o000o
  IiI111111IIII = 'http://www.youtube.com' + IiI111111IIII
  i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , oOOO00o000o , i1i11I1I1iii1 )
 else :
  i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
  for iI1I , IiI111111IIII , Iii1IIII11I , iIi11iiIiI1I in i1I1i :
   print 'im doing it'
   oOooOo0 ( 'tvshows' , 'INFO' )
   oOOO00o000o = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
   IiI111111IIII = 'http://www.youtube.com' + IiI111111IIII
   if '&' in IiI111111IIII :
    print ' i got here'
    IIi1i11111 = O000OOo00oo ( IiI111111IIII )
    i1ii1II1ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
    for i1ii1II1ii in i1ii1II1ii :
     Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
     for Iii1IIII11I in Iii1IIII11I :
      Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     IiI111111IIII = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1ii1II1ii ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = 'https://www.youtube.com/w' + IiI111111IIII
     oOOO00o000o = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
     for oOOO00o000o in oOOO00o000o :
      oOOO00o000o = 'http:' + oOOO00o000o
     i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , ooOoOoo0O , '' )
   elif Iii1IIII11I in I11II1i :
    pass
   elif 'user' in IiI111111IIII or 'elete' in Iii1IIII11I :
    pass
   elif 'hannel' in IiI111111IIII :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IiI111111IIII
    IIi1i11111 = O000OOo00oo ( IiI111111IIII )
    Iiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
    for iI1I , IiI111111IIII , Iii1IIII11I in Iiii :
     if 'outube' in IiI111111IIII or 'list' in IiI111111IIII :
      pass
     elif 'atch' in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '/watch?v=' , '' )
      i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iI1I , 'http:' + iI1I , '' )
     else :
      pass
   else :
    i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , oOOO00o000o , '' )
    if 89 - 89: IIIi
def iIiiii ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1i11111 )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiIi1IIi1I ( '[COLOR' + iIii1 + '] NEXT [/COLOR]' , url , 10065 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 for iI1I , url , Iii1IIII11I , iIi11iiIiI1I , i1i11I1I1iii1 in i1I1i :
  I11II1i . append ( Iii1IIII11I )
  oOooOo0 ( 'tvshows' , 'INFO' )
  oOOO00o000o = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOO00o000o
  url = 'http://www.youtube.com' + url
  i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , oOOO00o000o , i1i11I1I1iii1 )
 else :
  i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
  for iI1I , url , Iii1IIII11I , iIi11iiIiI1I in i1I1i :
   oOooOo0 ( 'tvshows' , 'INFO' )
   oOOO00o000o = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIi1i11111 = O000OOo00oo ( url )
    i1ii1II1ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
    for i1ii1II1ii in i1ii1II1ii :
     Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
     for Iii1IIII11I in Iii1IIII11I :
      Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1ii1II1ii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oOOO00o000o = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1ii1II1ii ) )
     for oOOO00o000o in oOOO00o000o :
      oOOO00o000o = 'http:' + oOOO00o000o
     i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , ooOoOoo0O , '' )
   elif Iii1IIII11I in I11II1i :
    pass
   elif 'user' in url or 'elete' in Iii1IIII11I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIi1i11111 = O000OOo00oo ( url )
    Iiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
    for iI1I , url , Iii1IIII11I in Iiii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iI1I , 'http:' + iI1I , '' )
     else :
      pass
   else :
    i1I1iI1iIi111i ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o , oOOO00o000o , '' )
    if 89 - 89: IIIIi1i - OO0 % I1ii11iIi11i % I11i
    if 49 - 49: I1ii11iIi11i - oOo0O0Ooo / ooo0oo0o0oo / o0o00Oo0O % I11i * O0O0OoOO0
def I1i1i1iii ( ) :
 if iiI1IiI == 'insert_password' :
  oooOOOOO . ok ( '[COLOR' + iIii1 + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iIii1 + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OOoO0 = open ( O000OO0 )
  i1I1i = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OOoO0 ) )
  for II11iI111i1 , Oo00OoOo in i1I1i :
   if II11iI111i1 == 'needs replacing' or Oo00OoOo == 'needs replacing' :
    ii1ii111 ( )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']G-Tv PRIVATE LIST[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , i11i1I1 + 'PrivateList.png' , ooOoOoo0O , '' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']G-Tv ULTIMATE[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
  if 33 - 33: Ii1I
def O00O0Ooooo00 ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + IIIII + ")" )
 ii1ii111 ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 97 - 97: OO0 / iii1iiii1 % ooOoO0O00 % Ii1I
def ii111I11iI ( ) :
 iiIi1IIi1I ( 'Live Events' , '' , 60002 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Live Stream Channels' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'PPV' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Entertainment' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Factual' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Movie Channels' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'US Movie Channels TEST' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Kids' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Music' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'UK Sports' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'International Sports' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'News UK & International' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Full List' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'World' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'German' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Arabic' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'VOD Latest' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'VOD Bollywood' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'TV Series Latest' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * oO0o0OOOO
def Ooooooo ( name ) :
 I1IIIiI1I1ii1 = name
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 i1I1i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIi1i11111 )
 for name , iI1I , iiiI1I1iIIIi1 , IiI111111IIII in i1I1i :
  if I1IIIiI1I1ii1 == 'Full List' :
   IiI111111IIII = ( IiI111111IIII ) . replace ( 'replace_user' , O0OoO000O0OO ) . replace ( 'replace_pass' , iiI1IiI )
   i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , iI1I , iI1I , '' )
  else :
   I1IIIiI1I1ii1 = ( I1IIIiI1I1ii1 ) . replace ( 'World' , 'القنوات العربية' )
   if I1IIIiI1I1ii1 in iiiI1I1iIIIi1 :
    IiI111111IIII = ( IiI111111IIII ) . replace ( 'replace_user' , O0OoO000O0OO ) . replace ( 'replace_pass' , iiI1IiI )
    print IiI111111IIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , iI1I , iI1I , '' )
   else :
    pass
    if 17 - 17: iI11I1II1I1I . ii / oO0o0OOOO % IIiIiII11i % ooOoO0O00 / Ii
def OOO ( name ) :
 I1IIIiI1I1ii1 = name
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 i1I1i = re . compile ( '#EXTINF:-1 tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIi1i11111 )
 for name , iI1I , IiI111111IIII in i1I1i :
  IiI111111IIII = ( IiI111111IIII ) . replace ( 'replace_user' , O0OoO000O0OO ) . replace ( 'replace_pass' , iiI1IiI )
  i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , iI1I , iI1I , '' )
 else :
  i1I1iI1iIi111i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 30 - 30: ii - ii . o0o00Oo0O / IIIIi1i
  if 31 - 31: O0OoO + I11i . ii
  if 89 - 89: IIiIiII11i + ooOoO0O00 + IIiIiII11i
  if 7 - 7: o0o00Oo0O % I11i + Ii1I * IIIIi1i - IIIIi1i
  if 42 - 42: OOooOOo * OOooOOo * iii1iiii1 . oO0o0OOOO
  if 51 - 51: O0OoO % iI11I1II1I1I - ii % OO0 * iI11I1II1I1I % oO0o
  if 99 - 99: IIIi * IIiIiII11i * iii1iiii1
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / ooo0oo0o0oo
  if 79 - 79: oO0o - iI11I1II1I1I + O0O0OoOO0 - iii1iiii1
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
def Ii1ii111i1 ( ) :
 iiIi1IIi1I ( 'Full Backup' , '' , 10061 , i11i1I1 + 'FullBackUp.png' , ooOoOoo0O , 'Back Up Your Full System' )
 if os . path . exists ( I11i1I1I ) :
  iiIi1IIi1I ( 'Backup Genie Favourites' , IiI111111IIII , 10062 , i11i1I1 + 'BackupGenieFavourites.png' , ooOoOoo0O , 'Back Up Your favourites' )
 if os . path . exists ( o0O ) :
  iiIi1IIi1I ( 'Backup Ivue Config' , o0O , 10062 , i11i1I1 + 'BackUpIvueConfig.png' , ooOoOoo0O , 'Back Up Your master.db' )
 if os . path . exists ( O00oO ) :
  iiIi1IIi1I ( 'Backup Kodi Favourites' , O00oO , 10062 , i11i1I1 + 'BackKodiFavourites.png' , ooOoOoo0O , 'Back Up Your favourites.xml' )
  if 31 - 31: O0OoO + o0o00Oo0O
  if 87 - 87: OO0
  if 45 - 45: oO0o / ii - IIIIi1i / O0O0OoOO0 % ooo0oo0o0oo
zip = oo00 . getSetting ( 'zip' )
OoO = xbmc . translatePath ( os . path . join ( zip ) )
def Iii11iI11i1I ( ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 86 - 86: IIiIiII11i % Ii + O0O0OoOO0 % Ii
  if 92 - 92: Ii - IIIIi1i / OO0 / IIIi
  if 43 - 43: IIiIiII11i + O0OoO + IIIIi1i
def iI1IIIii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I11i1I1I
  elif 'Ivue' in name :
   url = o0O
  elif 'Kodi' in name :
   url = O00oO
  Iii11iI11i1I ( )
  I1i11ii11 = open ( url ) . read ( )
  OO00O0oOO = os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] )
  Iii1I1I11iiI1 = open ( OO00O0oOO , mode = 'w' )
  Iii1I1I11iiI1 . write ( I1i11ii11 )
  Iii1I1I11iiI1 . close ( )
 else :
  if 'guisettings.xml' in description :
   Ii1iI111 = open ( os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0oooo00o0Oo = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1I1i = re . compile ( O0oooo00o0Oo ) . findall ( Ii1iI111 )
   for type , I1iii , oO0o0O0Ooo0o in i1I1i :
    oO0o0O0Ooo0o = oO0o0O0Ooo0o . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1iii , oO0o0O0Ooo0o ) )
  else :
   OO00O0oOO = os . path . join ( url )
   I1i11ii11 = open ( os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii1I1I11iiI1 = open ( OO00O0oOO , mode = 'w' )
   Iii1I1I11iiI1 . write ( I1i11ii11 )
   Iii1I1I11iiI1 . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 21 - 21: iii1iiii1 - oOo0O0Ooo + oO0o0OOOO
 if 78 - 78: ii - Ii - IIiIiII11i
 if 77 - 77: OOooOOo % O0O0OoOO0
 if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( ) :
 o0OO0 = 1
 Iii11iI11i1I ( )
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'Full Backup' , '' ) )
 I1I1 = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'my_full_backup.zip' ) )
 O0iIi1IiII = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOo00Oo0o0Oo ) :
  os . makedirs ( oOo00Oo0o0Oo )
 I1i = oooOOOOO . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1i ) : return False , 0
 ooo = I1i
 ii1iiIi1 = xbmc . translatePath ( os . path . join ( oOo00Oo0o0Oo , ooo + '.zip' ) )
 i111iiI1ii = [ 'plugin.video.GenieTv' ]
 IIiii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 I1i1i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOOOooO0oO00O0o = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 ooOO00oOOo000 = "Creating full backup of existing build"
 IIi = "Creating Community Build"
 i11II11II1 = "Archiving..."
 II1I = ""
 OoOo000oOo0oo = "Please Wait"
 oO0O ( i11 , ii1iiIi1 , IIi , i11II11II1 , II1I , OoOo000oOo0oo , I1i1i , OOOOooO0oO00O0o )
 time . sleep ( 1 )
 oOO = xbmc . translatePath ( os . path . join ( oOo00Oo0o0Oo , ooo + '_guisettings.zip' ) )
 iiiIIiIi = zipfile . ZipFile ( oOO , mode = 'w' )
 try :
  iiiIIiIi . write ( xbmc . translatePath ( os . path . join ( i11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iiiIIiIi . close ( )
 if o0OO0 == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1I1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + ii1iiIi1 + '[/COLOR]' )
  if 68 - 68: o0o00Oo0O + OOooOOo / IIIi - O0OoO + iI11I1II1I1I % O0O0OoOO0
def oO0O ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i1iI1iii11i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oOO00oO00O0OO = len ( sourcefile )
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for Oo00OoO00o0 , OOoOoO00O0O0o , iI1I11i in os . walk ( sourcefile ) :
  for file in iI1I11i :
   o0oOO0OO . append ( file )
 Ooo0o0oo = len ( o0oOO0OO )
 for Oo00OoO00o0 , OOoOoO00O0O0o , iI1I11i in os . walk ( sourcefile ) :
  OOoOoO00O0O0o [ : ] = [ Ii1i1i1111 for Ii1i1i1111 in OOoOoO00O0O0o if Ii1i1i1111 not in exclude_dirs ]
  iI1I11i [ : ] = [ Iii1I1I11iiI1 for Iii1I1I11iiI1 in iI1I11i if Iii1I1I11iiI1 not in exclude_files ]
  for file in iI1I11i :
   oOo00OO . append ( file )
   o0oO0O00oOo = len ( oOo00OO ) / float ( Ooo0o0oo ) * 100
   o0oOoO00o . update ( int ( o0oO0O00oOo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1111I1II11 = os . path . join ( Oo00OoO00o0 , file )
   if not 'temp' in OOoOoO00O0O0o :
    if not 'plugin.program.originwizard' in OOoOoO00O0O0o :
     import time
     iiiIIIIiIi = '01/01/1980'
     Iii = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1111I1II11 ) ) )
     if Iii > iiiIIIIiIi :
      i1iI1iii11i . write ( I1111I1II11 , I1111I1II11 [ oOO00oO00O0OO : ] )
 i1iI1iii11i . close ( )
 o0oOoO00o . close ( )
 if 6 - 6: O0OoO - Ii1I + O0O0OoOO0 + ooOoO0O00 / o0o00Oo0O / I11i
 if 42 - 42: ooOoO0O00 . oOo0O0Ooo / ooOoO0O00 + O0O0OoOO0
def O0o0O0OO00o ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCOOBY STREAMS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , i11i1I1 + 'scoob.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCOOBY SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , i11i1I1 + 'scoob.png' , ooOoOoo0O , '' )
 if 92 - 92: I11i + iii1iiii1 / I1ii11iIi11i % oO0o % ooo0oo0o0oo . ii
 if 52 - 52: OO0 / Ii - O0OoO . ooo0oo0o0oo % iI11I1II1I1I + I11i
def OO00oOooo0O ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH MOVIES[/COLOR]' , str ( I1I1iIiII1 ) , 9001 , i11i1I1 + 'MOVIESv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH SERIES[/COLOR]' , str ( I1I1iIiII1 ) , 9002 , i11i1I1 + 'TVSHOWSv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , i11i1I1 + 'ORIGINCARTOON' , ooOoOoo0O , '' )
 if 58 - 58: I1ii11iIi11i / IIIi
 if 44 - 44: O0OoO
 if 54 - 54: O0O0OoOO0 - oO0o0OOOO - iii1iiii1 . iI11I1II1I1I
 if 79 - 79: O0O0OoOO0 . oO0o
def IIiI1I1 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']RaysRavers[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , i11i1I1 + 'Rays-Ravers.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']QuickSilver[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , i11i1I1 + 'Quicksilver.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']RadioNomy[/COLOR]' , '' , 70001 , i11i1I1 + 'RadioNomy.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1iIiII1 ) , 30031 , i11i1I1 + 'MusicChannels.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']UK RADIO[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , i11i1I1 + 'UKRadio.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']WORLD RADIO[/COLOR]' , str ( I1I1iIiII1 ) , 1013 , i11i1I1 + 'WorldRadio.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CONCERTS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , i11i1I1 + 'Concerts.png' , ooOoOoo0O , '' )
  if 15 - 15: O0O0OoOO0 * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC VIDEOS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , i11i1I1 + 'MusicVideos.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC[/COLOR]' , str ( I1I1iIiII1 ) + ( i1iiIII111ii ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , i11i1I1 + 'Music.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC SEARCH[/COLOR]' , str ( I1I1iIiII1 ) , 1111 , i11i1I1 + 'MusicSearch.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , i11i1I1 + 'KodibleAudioBooks.png' , ooOoOoo0O , '' )
 if 60 - 60: oOo0O0Ooo * iii1iiii1 % oO0o + IIIi
 oOooOo0 ( 'movies' , 'MAIN' )
 if 52 - 52: ooOoO0O00
def o000 ( ) :
 iI1iiIiiII ( )
 if 94 - 94: I11i + o0o00Oo0O / oO0o0OOOO . oOo0O0Ooo + O0OoO . iI11I1II1I1I
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']KILL KODI[/COLOR]' , '' , 80000 , i11i1I1 + 'KillKodi.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SPEEDTEST[/COLOR]' , '' , 50004 , i11i1I1 + 'Speedtest.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , i11i1I1 + 'View-Log-File.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'DELETE CACHE' , 'url' , 14 , i11i1I1 + 'DeleteCache.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'DELETE PACKAGES' , 'url' , 6 , i11i1I1 + 'DeletePackages.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FORCE REFRESH' , 'url' , 10 , i11i1I1 + 'ForceRefresh.png' , ooOoOoo0O , 'Force Refresh All Repos' )
 if 62 - 62: OOooOOo / oOo0O0Ooo - Ii1I - oOo0O0Ooo + Ii + ooOoO0O00
 i1I1iI1iIi111i ( 'CHECK MY IP' , 'url' , 12 , i11i1I1 + 'CheckMyIP.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , i11i1I1 + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , ooOoOoo0O , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1I1iIiII1 ) , 4 , i11i1I1 + 'AdvancedSettingXML.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']URL FIXES[/COLOR]' , str ( I1I1iIiII1 ) , 20 , i11i1I1 + 'URLFixes.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 23 - 23: IIIIi1i + oO0o0OOOO . OOooOOo * oOo0O0Ooo + Ii1I
 if 18 - 18: ooo0oo0o0oo * I11i . ooo0oo0o0oo / o0o00Oo0O
def i1i1II ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']REPOS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , i11i1I1 + 'repos.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEW[/COLOR]' , str ( I1I1iIiII1 ) , 22 , i11i1I1 + 'NEW.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']IPTV[/COLOR]' , str ( I1I1iIiII1 ) , 23 , i11i1I1 + 'IPTV.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']VIDEO[/COLOR]' , str ( I1I1iIiII1 ) , 24 , i11i1I1 + 'VIDEO.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SPORTS[/COLOR]' , str ( I1I1iIiII1 ) , 25 , i11i1I1 + 'SPORTS.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']KIDS[/COLOR]' , str ( I1I1iIiII1 ) , 26 , i11i1I1 + 'KIDS.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC[/COLOR]' , str ( I1I1iIiII1 ) , 27 , i11i1I1 + 'MUSIC.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']PROGRAMS[/COLOR]' , str ( I1I1iIiII1 ) , 28 , i11i1I1 + 'PROGRAMS.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']XXX[/COLOR]' , 'URL' , 29 , i11i1I1 + 'XXX.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 8 - 8: I11i
 if 4 - 4: Ii1I + Ii1I * OO0 - OOooOOo
def o00o ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( 'CHECK ADVANCED XML' , str ( I1I1iIiII1 ) , 8 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'MUCKYS XML' , str ( I1I1iIiII1 ) + '/wizard/muckys.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '0CACHE XML' , str ( I1I1iIiII1 ) + '/wizard/0cache.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'MIKEY1234 XML' , str ( I1I1iIiII1 ) + '/wizard/mikey.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'TUXENS XML' , str ( I1I1iIiII1 ) + '/wizard/tuxens.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'P2P RECOMMENDED XML1' , str ( I1I1iIiII1 ) + '/wizard/p2p1.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'P2P RECOMMENDED XML2' , str ( I1I1iIiII1 ) + '/wizard/p2p2.xml' , 7 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'DELETE XML' , str ( I1I1iIiII1 ) , 11 , i11i1I1 + 'XML.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 47 - 47: I11i + IIIIi1i - IIIi % ii
def o0O0 ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']My Local Zip[/COLOR]' , ii11iIi1I , 48 , i11i1I1 + 'MyLocalZIP.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']My Online Zip[/COLOR]' , i1iIIi1 , 43 , i11i1I1 + 'MyOnlineZip.png' , ooOoOoo0O , '' )
 if 74 - 74: ooOoO0O00 + o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1iIiII1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , i11i1I1 + 'FTV4.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1iIiII1 ) + '/wizard/customftv/settings.xml' , 17 , i11i1I1 + 'FTV3.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , i11i1I1 + 'FTV1.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'RESET FTV DATABASE' , 'url' , 18 , i11i1I1 + 'FTV2.png' , ooOoOoo0O , '' )
 if 55 - 55: I1ii11iIi11i - O0OoO
 if 84 - 84: iii1iiii1 + I1ii11iIi11i - OOooOOo * OOooOOo
 if 61 - 61: ii . IIIi . ii / I1ii11iIi11i
def o00O ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 33 , i11i1I1 + 'Skins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ARTWORK PACKS[/COLOR]' , str ( I1I1iIiII1 ) , 34 , i11i1I1 + 'ArtworkPacks.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']CREATE UNIVERSAL PATHS[/COLOR]' , i11 , 35 , i11i1I1 + 'CreateUniversalPath.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 48 - 48: IIIIi1i . Ii
def IIioo0OO ( ) :
 ooOooo000oOO = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1I1i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for iI1I , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iI1I , iI1I , '' )
 oOooOo0 ( 'tvshows' , 'INFO' )
 if 2 - 2: IIiIiII11i - oO0o . ooo0oo0o0oo * IIIIi1i / IIIi
def OOo0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( iiIii1IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 10 - 10: Ii - I11i % iI11I1II1I1I
def i111IIIiI ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']GOTHAM SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 36 , i11i1I1 + 'GothamSkins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HELIX SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 37 , i11i1I1 + 'HelixSkins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ISENGAARD SKINS[/COLOR]' , i11 , 38 , i11i1I1 + 'IsengaardSkins.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 23 - 23: I1ii11iIi11i % oO0o0OOOO - O0OoO % iI11I1II1I1I . OOooOOo
def I1Ii1 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + OoOooOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 37 - 37: O0O0OoOO0 % oO0o
def oOooO0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + O0O0ooOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 70 - 70: OO0 . o0o00Oo0O . iii1iiii1 . o0o00Oo0O + ooOoO0O00
def i1II1I ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + OOoO0ooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 24 - 24: ooOoO0O00 . Ii
def IIIII1iii11 ( url ) :
 ooOooo000oOO = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 35 - 35: IIIi / iii1iiii1 / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . iii1iiii1
def O0O00O000OOO ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 40 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 100 - 100: oOo0O0Ooo / I11i * IIIIi1i . o0o00Oo0O / O0OoO
def oOO0o000Oo00o ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iii11II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 5 - 5: OOooOOo - ooo0oo0o0oo * ooo0oo0o0oo
def IiiIi1IIII1i ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']APK (Android only)[/COLOR]' , str ( I1I1iIiII1 ) , 2 , i11i1I1 + 'APKAndroidOnly.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']APK Search[/COLOR]' , str ( I1I1iIiII1 ) , 30038 , i11i1I1 + 'APKSearch.png' , ooOoOoo0O , '' )
 if 98 - 98: O0OoO + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
def iIIi1I1ii ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20vZ2FtZS8=' ) )
 i1I1i = re . compile ( 'href="([^"]*)">GAME</a>' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'href="([^"]*)">APP</a>' ) . findall ( o0ooo0 )
 for IiI111111IIII in i1I1i :
  II11IiIi11 ( 'Android Apps' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiI111111IIII , 30036 , i11i1I1 + 'apps.png' )
 for IiI111111IIII in Iiiii1i :
  II11IiIi11 ( 'Android Games' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiI111111IIII , 30035 , i11i1I1 + 'GAMES.png' )
 oOooOo0 ( 'movies' , 'MAIN' )
def Iiiii1io00O00o ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if '/game' in url :
   II11IiIi11 ( ( Iii1IIII11I ) . replace ( '&amp;' , ' - ' ) , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'APK.png' )
def O0o0OO ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if '/app' in url :
   II11IiIi11 ( ( Iii1IIII11I ) . replace ( '&amp;' , ' - ' ) , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'APK.png' )
def iI1iii ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( ' <img src="([^"]*)".+?title="([^"]*)">.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'href="([^"]*)">NEXT </a>' ) . findall ( o0ooo0 )
 for iI1I , Iii1IIII11I , url in i1I1i :
  II11IiIi11 ( ( Iii1IIII11I ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , url , 19 , iI1I )
 for url in Iiiii1i :
  II11IiIi11 ( 'NEXT' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'Next.png' )
def OOOo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'href="([^"]*)">Download APK from APKCRAFT</a></p>' ) . findall ( o0ooo0 )
 for url in i1I1i :
  oO00OoOoo0 ( url )
def I1iiiiii ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'http://apk.koplayer.com/search?q=' + ( i11IIIiI11 ) . replace ( ' ' , '+' ) + '&region='
 IIi1IIIi = III11I1 . lower ( )
 iI1iii ( IIi1IIIi )
 if 65 - 65: ooo0oo0o0oo + I1ii11iIi11i
def oO00OoOoo0 ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( Ooo0O0 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , Iii1IIII11I + '.apk' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 55 - 55: I1ii11iIi11i
def ooO0o ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , Iii1IIII11I + '.mp4' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 25 - 25: iI11I1II1I1I - IIIIi1i
 if 3 - 3: oOo0O0Ooo * OO0 + IIiIiII11i - oO0o
def OOOOOoOO0OOoo ( name , url , description ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , name )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 IIIi11IiIiii = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIIi11IiIiii
 print '======================================='
 extract . all ( ooo0 , IIIi11IiIiii , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 38 - 38: I1ii11iIi11i - oO0o0OOOO . I1ii11iIi11i
 if 38 - 38: ooOoO0O00 + O0O0OoOO0
def Oo00O0ooOO ( url ) :
 ooOooo000oOO = O000OOo00oo ( I1I1iIiII1 + ( i1iiIII111ii ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'INFO' )
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
 if 72 - 72: ii / oOo0O0Ooo + O0O0OoOO0 / OOooOOo * O0O0OoOO0
def Ii1iIi111i1i1 ( url ) :
 ooOooo000oOO = O000OOo00oo ( I1I1iIiII1 + ( i1iiIII111ii ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 30015 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 45 - 45: OOooOOo . I11i % OOooOOo * oOo0O0Ooo % oOo0O0Ooo
def oOoOo00ooOooo ( url , iconimage , fanart ) :
 ooOooo000oOO = O000OOo00oo ( url )
 Oo00o0OO0O00o = url
 iI1I = iconimage
 fanart = fanart
 i1I1i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( ooOooo000oOO )
 for iiI1IIIi , Iii1IIII11I in i1I1i :
  if '.mp4' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Watch VIDEO' , url + '/' + iiI1IIIi , 222 , iI1I , fanart , '' )
  if 'description' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Read Description' , url + '/' + iiI1IIIi , 30017 , iI1I , fanart , '' )
  if 'images' in Iii1IIII11I :
   iiIi1IIi1I ( 'View Images' , url + '/' + iiI1IIIi , 30018 , iI1I , fanart , '' )
  if 'url' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Install Build On Android' , url + '/' + iiI1IIIi , 30016 , iI1I , fanart , '' )
  if 'url' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Install Build On Pc' , url + '/' + iiI1IIIi , 30019 , iI1I , fanart , '' )
 oOooOo0 ( 'movies' , 'INFO' )
 if 12 - 12: Ii . OOooOOo % I1ii11iIi11i - ii . o0o00Oo0O
def OOoO00oo0000O ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url="([^"]*)"' ) . findall ( ooOooo000oOO )
 for url in i1I1i :
  Ii1IIi ( url )
  if 70 - 70: oOo0O0Ooo / oO0o0OOOO
def IIiiiiIiIIii ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url="([^"]*)"' ) . findall ( ooOooo000oOO )
 for url in i1I1i :
  O0OO ( url )
  if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
def I1ii1II1iII ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'desc="([^"]*)"' ) . findall ( ooOooo000oOO )
 for II1i in i1I1i :
  ii1I ( 'Description:' , II1i )
  if 81 - 81: Ii1I
def o00ooo ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 url = url
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ooOooo000oOO )
 for iiI1IIIi , Iii1IIII11I in i1I1i :
  if 'png' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'image' , '' , '' , url + '/' + iiI1IIIi , url + '/' + iiI1IIIi , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 31 - 31: o0o00Oo0O * I11i % I11i / IIIi / oO0o0OOOO / oO0o
def III1ii ( name , url , description ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I
 print '======================================='
 extract . all ( ooo0 , i1I , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IiIi1I1 ( )
 if 36 - 36: oOo0O0Ooo * I1ii11iIi11i
 if 77 - 77: IIIi % ooOoO0O00 - O0O0OoOO0
def O0OO ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I
 print '======================================='
 extract . all ( ooo0 , i1I , o0oOoO00o )
 oOO00OO0ooo0o ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOO0o ( )
 if 4 - 4: I1ii11iIi11i . ooOoO0O00 - IIIIi1i
def Ii1IIi ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I
 print '======================================='
 extract . all ( ooo0 , i1I , o0oOoO00o )
 oOO00OO0ooo0o ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOO0o ( )
 if 10 - 10: oO0o0OOOO * O0O0OoOO0 % ii
def O0Oo0Ooo ( name , url , description ) :
 i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 ooo0 = os . path . join ( ii11iIi1I )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print i1I
 print '======================================='
 extract . all ( ooo0 , i1I , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOO0o ( )
 if 78 - 78: oO0o % ooo0oo0o0oo * ooOoO0O00
def O0iI ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def I1IiiiiI ( log ) :
 xbmc . log ( "[%s]: %s" % ( oO0o0o0ooO0oO , log ) )
 if not os . path . exists ( Oo0o0000o0o0 ) : os . makedirs ( Oo0o0000o0o0 )
 if not os . path . exists ( oOo0oooo00o ) : Iii1I1I11iiI1 = open ( oOo0oooo00o , 'w' ) ; Iii1I1I11iiI1 . close ( )
 with open ( oOo0oooo00o , 'a' ) as Iii1I1I11iiI1 :
  Ii1IIiiIiiIi = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  Iii1I1I11iiI1 . write ( Ii1IIiiIiiIi . rstrip ( '\r\n' ) + '\n' )
def OOO0o ( ) :
 o0O0o = oooOOOOO . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o0O0o == 0 : return
 elif o0O0o == 1 : pass
 i1iiIIIi = O0iI ( )
 I1IiiiiI ( "Platform: " + str ( i1iiIIIi ) )
 os . _exit ( 1 )
 I1IiiiiI ( "Force close failed!  Trying alternate methods." )
 if i1iiIIIi == 'osx' :
  I1IiiiiI ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1iiIIIi == 'linux' :
  I1IiiiiI ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1iiIIIi == 'android' :
  I1IiiiiI ( "############ try android force close #################" )
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
  oooOOOOO . ok ( oO0o0o0ooO0oO , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif i1iiIIIi == 'windows' :
  I1IiiiiI ( "############ try windows force close #################" )
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
  oooOOOOO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  I1IiiiiI ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  I1IiiiiI ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 62 - 62: o0o00Oo0O / oOo0O0Ooo % o0o00Oo0O * oO0o % oOo0O0Ooo
  if 33 - 33: oOo0O0Ooo . IIIi * oO0o * iI11I1II1I1I
  if 5 - 5: I1ii11iIi11i / ooo0oo0o0oo % o0o00Oo0O . iii1iiii1 * ooo0oo0o0oo
def ooOooOoOoO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( url ) :
  for file in iI1I11i :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    Ii1iI111 = open ( ( os . path . join ( ooOOooo0Oo , file ) ) ) . read ( )
    oo0O0o = Ii1iI111 . replace ( i11 , 'special://home/' )
    Iii1I1I11iiI1 = open ( ( os . path . join ( ooOOooo0Oo , file ) ) , mode = 'w' )
    Iii1I1I11iiI1 . write ( str ( oo0O0o ) )
    Iii1I1I11iiI1 . close ( )
 OOO0o ( )
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * ooo0oo0o0oo / I11i
def I1iiIII ( ) :
 II11IiIi11 ( ( '[COLOR' + iIii1 + ']GENRE[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , i11i1I1 + 'RadioNomy.png' )
 II11IiIi11 ( ( '[COLOR' + iIii1 + ']SORT BY[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , i11i1I1 + 'RadioNomy.png' )
 II11IiIi11 ( ( '[COLOR' + iIii1 + ']SEARCH[/COLOR]' ) , '' , 70006 , i11i1I1 + 'RadioNomy.png' )
 if 16 - 16: IIIi + OO0 / I11i
def O00oOoo0OoO0 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
def Ooo0 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
def oooO00o0 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in Iiiii1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']Filter - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
 for url , iI1I , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']Stream - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iI1I )
def o0o00oO0oo000 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( o0ooo0 )
 for url in i1I1i :
  oO000o ( url )
def o0Oo ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11
 o0O0I1I1Iiii1 = 'https://www.radionomy.com/en/search/index?query=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1i11111 = O000OOo00oo ( o0O0I1I1Iiii1 )
 i1I1i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']Stream - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + IiI111111IIII , 70005 , iI1I )
  if 2 - 2: oO0o0OOOO + OO0
  if 76 - 76: iii1iiii1
def OoOoOo0 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , 'http://www.listenlive.eu/' + IiI111111IIII , 10111113 , i11i1I1 + 'radio.png' )
def i1II11II1 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , url in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , url , 222 , i11i1I1 + 'radio.png' )
  if 5 - 5: I1ii11iIi11i - Ii1I % IIIi - IIiIiII11i . oOo0O0Ooo + IIIIi1i
def iiIi1I1i1 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.toonjet.com/' + IiI111111IIII , 8051 , i11i1I1 + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOIiIi1111ii ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( o0ooo0 )
 for url , iI1I in i1I1i :
  if 'ol.gif' in iI1I :
   pass
  elif 'link_block_' in iI1I :
   pass
  elif '.png' in iI1I :
   pass
  else :
   II11IiIi11 ( ( iI1I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , i11i1I1 + 'vod.png' )
 for url in Iiiii1i :
  II11IiIi11 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , i11i1I1 + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1I1II1 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( o0ooo0 )
 for url in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , i11i1I1 + 'classictoons.png' )
  if 92 - 92: ii - ii * oO0o % oOo0O0Ooo
  if 77 - 77: iI11I1II1I1I - ooOoO0O00 . IIIi
def iIi1iIIIiIiI ( ) :
 OooOo000o0o ( 'Audio Books' , '' , 30011 , i11i1I1 + 'AudioBooks.png' , i11i1I1 + 'AudioBooks.png' , '' )
 OooOo000o0o ( 'Kids Audio Books' , '' , 30006 , i11i1I1 + 'KidsAudioBooks.png' , i11i1I1 + 'KidsAudioBooks.png' , '' )
 if 42 - 42: IIIi % O0OoO
def OOO0 ( ) :
 OooOo000o0o ( 'All' , '' , 30001 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'Popular' , '' , 30012 , i11i1I1 + 'POPULARv.png' , i11i1I1 + 'POPULARv.png' , '' )
 OooOo000o0o ( 'Search' , '' , 30013 , i11i1I1 + 'Search.png' , i11i1I1 + 'Search.png' , '' )
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( ) :
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , Oo0O0O000 in i1I1i :
  if 'Parent' in Iii1IIII11I :
   pass
  elif '2' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
def oO00 ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , Oo0O0O000 in i1I1i :
  if i11IIIiI11 in Iii1IIII11I . lower ( ) :
   if '1' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   elif '2' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   elif '3' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
    if 1 - 1: IIIi
    if 12 - 12: OO0 % oOo0O0Ooo + IIIi - ooOoO0O00 . O0O0OoOO0 / oOo0O0Ooo
def o0IiiiI111I ( ) :
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , Oo0O0O000 in i1I1i :
  if '1' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 3010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '2' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '3' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: I11i * O0O0OoOO0 + oO0o0OOOO + IIIIi1i
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I11i / O0OoO / ooo0oo0o0oo % OO0 + IIiIiII11i
def I1III111i ( url ) :
 iiI1IIIi = url
 IIi1i11111 = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in Iiiii1i :
  if 'mp3' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iiI1IIIi + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iiI1IIIi + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iiI1IIIi + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '/' in Iii1IIII11I :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iiI1IIIi + url , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 4 - 4: ooOoO0O00 + OO0 + ooOoO0O00
   if 31 - 31: O0O0OoOO0
   if 78 - 78: Ii + I11i + iii1iiii1 / I11i % iI11I1II1I1I % ooo0oo0o0oo
def Oo0O0Oo00O ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 iiI1IIIi = url
 i1I1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if 'Parent' in Iii1IIII11I :
   pass
  elif '.db' in Iii1IIII11I :
   pass
  elif '.jpg' in Iii1IIII11I :
   pass
  elif '.html' in Iii1IIII11I :
   pass
  elif '.doc' in Iii1IIII11I :
   pass
  elif 'mp3' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iiI1IIIi + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iiI1IIIi + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  else :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iiI1IIIi + url , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: I11i . oOo0O0Ooo - Ii1I
   if 32 - 32: ii / oOo0O0Ooo / iI11I1II1I1I + IIiIiII11i . IIIi . I11i
def ii1ii ( ) :
 OooOo000o0o ( 'A-Z' , '' , 30007 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'All' , '' , 30003 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'Search' , '' , 30014 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1I1i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I in i1I1i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IiI111111IIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iI1I :
   pass
  else :
   OooOo000o0o ( iI1I , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IiI111111IIII ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iI1I + '.gif' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 54 - 54: OOooOOo % IIIIi1i . OOooOOo * O0OoO + OOooOOo % ooOoO0O00
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: iii1iiii1 - O0OoO + O0O0OoOO0 - OOooOOo * OOooOOo . I1ii11iIi11i
 if 47 - 47: IIIi % iI11I1II1I1I
def IiI1IIIII1I ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if '</a>' in Iii1IIII11I :
   pass
  elif '(' in Iii1IIII11I :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  else :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: O0O0OoOO0 - O0O0OoOO0 + ooOoO0O00 - o0o00Oo0O - iii1iiii1
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: OOooOOo - IIIIi1i - ii
def o00ii111Iiii ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1I1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if i11IIIiI11 in Iii1IIII11I . lower ( ) :
   if '</a>' in Iii1IIII11I :
    pass
   elif '(' in Iii1IIII11I :
    OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   else :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30004 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
    if 54 - 54: ii - oOo0O0Ooo % Ii1I
    if 92 - 92: oO0o * OO0
def i1iIIi1o0o0OoOOOOOo ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1I1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if '</a>' in Iii1IIII11I :
   pass
  elif '(' in Iii1IIII11I :
   OooOo000o0o ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  else :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30004 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 39 - 39: ii * O0OoO * o0o00Oo0O . oO0o0OOOO . oO0o + OO0
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: OOooOOo + IIIi % ii + I11i
 if 56 - 56: ii + Ii1I - IIIIi1i
def III1I1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( IIi1i11111 )
 for url in i1I1i :
  iiI1IIIi = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iiI1IIIi )
  if 12 - 12: iI11I1II1I1I % OO0 % OO0
def o0i1iI1iiI1I ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , url in i1I1i :
  if '<p align' in Iii1IIII11I :
   pass
  elif '&nbsp;' in Iii1IIII11I :
   pass
  else :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 52 - 52: oO0o % O0O0OoOO0 * IIiIiII11i
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: oO0o0OOOO % o0o00Oo0O - ii + OO0 . IIIi % IIiIiII11i
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
def II1 ( ) :
 IIi1i11111 = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1I1i = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'ongoing' in IiI111111IIII :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 21005 , i11i1I1 + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in IiI111111IIII :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 21005 , i11i1I1 + 'CartoonShows.png' , '' , '' )
  if 'disney' in IiI111111IIII :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 21005 , i11i1I1 + 'Disney.png' , '' , '' )
  if 'genre' in IiI111111IIII :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 21005 , i11i1I1 + 'Genre.png' , '' , '' )
  if 'years' in IiI111111IIII :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 21005 , i11i1I1 + 'Years.png' , '' , '' )
def I11Iii1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 i1iIIi1II1iiI = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIi1i11111 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iI1I , iI1I , Iii1IIII11I )
 for url , Iii1IIII11I in i1iIIi1II1iiI :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 21005 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 21005 , i11i1I1 + 'Next.png' , '' , '' )
def III1Ii1i1I1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 O0O00OooO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 I1IiI1iI11 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIi1i11111 )
 iIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url in I1IiI1iI11 :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']PLAY[/COLOR]' , 'http:' + url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url , Iii1IIII11I in O0O00OooO :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 else :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , i11i1I1 + 'watchcartoons.png' , '' , '' )
def iiO0O0o0oO0O00 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
  if 70 - 70: iii1iiii1 + IIIi
def o00ooo0 ( ) :
 II11IiIi11 ( '[COLOR' + iIii1 + ']CARTOONS[/COLOR]' , '' , 20001 , i11i1I1 + 'ORIGINCARTOON.png' )
 II11IiIi11 ( '[COLOR' + iIii1 + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , i11i1I1 + 'ORIGINCARTOON.png' )
 if 39 - 39: OO0 . IIiIiII11i
def iIiIi1iI11iiI ( ) :
 II11IiIi11 ( '[COLOR' + iIii1 + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , i11i1I1 + 'ORIGINCARTOON.png' )
 II11IiIi11 ( '[COLOR' + iIii1 + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , i11i1I1 + 'ORIGINCARTOON.png' )
 if 26 - 26: iI11I1II1I1I * iii1iiii1 - O0OoO
def III1II111Ii1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if '?c=' in url :
   II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i11i1I1 + 'ORIGINCARTOON.png' )
   if 82 - 82: iii1iiii1 - O0OoO + oO0o
def OO0iIiiIi11IIi ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Oo0 , Iii1IIII11I in i1I1i :
  if 'Genre' in url :
   II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i11i1I1 + 'ORIGINCARTOON.png' )
   if 60 - 60: I11i . I11i / IIIIi1i
def Iio00 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Oo0 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Oo0 )
  if 46 - 46: iI11I1II1I1I * iii1iiii1 - iI11I1II1I1I . OOooOOo - iii1iiii1
def IiiIiI1iI1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Oo0 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Oo0 )
  if 23 - 23: IIIIi1i + O0OoO * OO0 / iI11I1II1I1I - IIIIi1i
  if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . O0OoO + oO0o - iii1iiii1
  if 5 - 5: IIIIi1i
  if 62 - 62: OOooOOo . ii . O0OoO . oO0o * IIIIi1i
  if 78 - 78: IIIi / oO0o - IIIi * ii . OOooOOo
def OOoooOoO0Oo ( ) :
 if 78 - 78: ii / O0OoO % OOooOOo * ii
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Cartoons[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Cartoons[/COLOR]' , '' , 10005 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
 if 68 - 68: IIIi
def i11i11 ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 18 - 18: iI11I1II1I1I + oO0o0OOOO * oOo0O0Ooo - O0OoO / oOo0O0Ooo
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIi1i11111 )
 if 78 - 78: oO0o0OOOO . ooo0oo0o0oo
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if i11IIIiI11 in Iii1IIII11I . lower ( ) :
   if 'Dad!' in Iii1IIII11I :
    pass
   elif 'Family Guy' in Iii1IIII11I :
    pass
   elif '2 Stupid' in Iii1IIII11I :
    pass
   elif 'The Zelfs' in Iii1IIII11I :
    pass
   elif 'A Clone' in Iii1IIII11I :
    pass
   elif 'A.T.O.M' in Iii1IIII11I :
    pass
   elif 'Almost Naked' in Iii1IIII11I :
    pass
   elif 'Angry Kid' in Iii1IIII11I :
    pass
   elif 'Annoying Orange' in Iii1IIII11I :
    pass
   elif 'Aqua Teen' in Iii1IIII11I :
    pass
   elif 'Assy Mcgee' in Iii1IIII11I :
    pass
   elif 'Astroblast' in Iii1IIII11I :
    pass
   elif 'Atomic Betty' in Iii1IIII11I :
    pass
   elif 'Axe Cop' in Iii1IIII11I :
    pass
   elif 'Baby Playpen' in Iii1IIII11I :
    pass
   elif 'Beavis and Butt' in Iii1IIII11I :
    pass
   elif 'Celebrity Deathmatch' in Iii1IIII11I :
    pass
   elif 'Clerks The' in Iii1IIII11I :
    pass
   elif 'Crapston Villas' in Iii1IIII11I :
    pass
   elif 'Duckman:' in Iii1IIII11I :
    pass
   elif 'Stripperella' in Iii1IIII11I :
    pass
   elif 'Vixen' in Iii1IIII11I :
    pass
   else :
    iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 10006 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
    if 38 - 38: OOooOOo + ooo0oo0o0oo
    if 15 - 15: I1ii11iIi11i + oO0o0OOOO . OO0 - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 86 - 86: oOo0O0Ooo / IIIi * O0O0OoOO0
def O00o ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if 'Dad!' in Iii1IIII11I :
   pass
  elif 'Family Guy' in Iii1IIII11I :
   pass
  elif '2 Stupid' in Iii1IIII11I :
   pass
  elif 'The Zelfs' in Iii1IIII11I :
   pass
  elif 'A Clone' in Iii1IIII11I :
   pass
  elif 'A.T.O.M' in Iii1IIII11I :
   pass
  elif 'Almost Naked' in Iii1IIII11I :
   pass
  elif 'Angry Kid' in Iii1IIII11I :
   pass
  elif 'Annoying Orange' in Iii1IIII11I :
   pass
  elif 'Aqua Teen' in Iii1IIII11I :
   pass
  elif 'Assy Mcgee' in Iii1IIII11I :
   pass
  elif 'Astroblast' in Iii1IIII11I :
   pass
  elif 'Atomic Betty' in Iii1IIII11I :
   pass
  elif 'Axe Cop' in Iii1IIII11I :
   pass
  elif 'Baby Playpen' in Iii1IIII11I :
   pass
  elif 'Beavis and Butt' in Iii1IIII11I :
   pass
  elif 'Celebrity Deathmatch' in Iii1IIII11I :
   pass
  elif 'Clerks The' in Iii1IIII11I :
   pass
  elif 'Crapston Villas' in Iii1IIII11I :
   pass
  elif 'Duckman:' in Iii1IIII11I :
   pass
  elif 'Stripperella' in Iii1IIII11I :
   pass
  elif 'Vixen' in Iii1IIII11I :
   pass
  else :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 10006 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: Ii1I * IIiIiII11i * oO0o0OOOO
def oO0OoooO0oOO00OoOo ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o0ooo0 )
 for iI1I in Iiiii1i :
  OoOi111i = iI1I
 II1III1i1iiI = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o0ooo0 )
 for url in II1III1i1iiI :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , url , 10006 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 i1I1i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 10007 , OoOi111i )
  if 27 - 27: O0O0OoOO0 - o0o00Oo0O % oO0o0OOOO * iii1iiii1 . ooo0oo0o0oo % iI11I1II1I1I
  if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % OO0
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: OOooOOo
def Oo0oOo0ooOOOo ( url , IMAGE ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o0ooo0 )
 for Iii1IIII11I , url in i1I1i :
  print Iii1IIII11I + '     ' + url
  if 'easy' in url :
   OoO0000o ( url )
   if 90 - 90: ooo0oo0o0oo . OO0 / iI11I1II1I1I
   if 28 - 28: ooo0oo0o0oo + IIIi - OO0 / iI11I1II1I1I - oOo0O0Ooo
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * IIIi * oO0o
def OoO0000o ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( "url: '(.+?)'," ) . findall ( o0ooo0 )
 for url in i1I1i :
  oO000o ( url )
  if 35 - 35: Ii1I / IIIIi1i % oOo0O0Ooo + iI11I1II1I1I
  if 79 - 79: OOooOOo / OO0
  if 77 - 77: I1ii11iIi11i
def i1i111Iiiiiii ( ) :
 if 19 - 19: oOo0O0Ooo . I1ii11iIi11i + ii - oOo0O0Ooo
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Stand Up[/COLOR]' , '' , 10014 , i11i1I1 + 'StandUp.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Comedian[/COLOR]' , '' , 10015 , i11i1I1 + 'SearchComedian.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Others[/COLOR]' , '' , 10017 , i11i1I1 + 'Others.png' , ooOoOoo0O , '' )
 if 93 - 93: iI11I1II1I1I + oOo0O0Ooo + Ii
def O0Oo0 ( ) :
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  if 'elete' in Iii1IIII11I :
   pass
  else :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 222 , iI1I )
   if 99 - 99: Ii1I . oO0o * oO0o0OOOO % iii1iiii1
def II1Ii ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1iiII1i = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , oO00O , i1iII1IiiIiI1 in Ii1iiII1i :
  for i11IIIiI11 in oO00O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIiI11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IiI111111IIII , Iii1IIII11I in IIiI11 :
    if 'tube' in IiI111111IIII :
     pass
    elif 'stage' in IiI111111IIII :
     IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + oO00O + '   -   ' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iI1I , )
    elif 'vee' in IiI111111IIII :
     pass
     if 9 - 9: OO0 + IIiIiII11i % OO0 % ooo0oo0o0oo + iI11I1II1I1I
def oO00IiI1II11iiI ( ) :
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1iiII1i = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , oO00O , i1iII1IiiIiI1 in Ii1iiII1i :
  IIiI11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IiI111111IIII , Iii1IIII11I in IIiI11 :
   if 'tube' in IiI111111IIII :
    pass
   elif 'stage' in IiI111111IIII :
    IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + oO00O + '   -   ' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iI1I )
   elif 'vee' in IiI111111IIII :
    pass
    if 56 - 56: IIIIi1i
    if 84 - 84: OOooOOo - Ii
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: IIIIi1i * OOooOOo
def OO0ooo0 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIi1i11111 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OOo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OOo :
  oO000o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 7 - 7: Ii1I - IIIi * O0OoO + I11i . Ii1I
  if 85 - 85: o0o00Oo0O
  if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * O0O0OoOO0
  if 19 - 19: O0O0OoOO0
  if 55 - 55: O0OoO % O0OoO / o0o00Oo0O % IIIIi1i - I11i . I1ii11iIi11i
  if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
  if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
def IIiI11I1I1i1i ( ) :
 if 86 - 86: ooOoO0O00
 i1o0oo0Ooooo0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , ooOoOoo0O , '' )
 i1o0oo0Ooooo0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 if 76 - 76: ooOoO0O00 * ii * o0o00Oo0O + iii1iiii1 * iii1iiii1
 oOooOo0 ( 'movies' , 'MAIN' )
 if 35 - 35: I11i
def ooOoooo0 ( ) :
 i1o0oo0Ooooo0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 i1o0oo0Ooooo0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 if 54 - 54: ooOoO0O00 . oO0o0OOOO - Ii1I + OO0 + I1ii11iIi11i / I1ii11iIi11i
 oOooOo0 ( 'movies' , 'MAIN' )
def i1i ( ) :
 if 12 - 12: O0O0OoOO0
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 Oo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 12 - 12: oOo0O0Ooo - OO0
 for I1ii1I1Ii in Oo :
  IiI = oo0OooOOo0 + I1ii1I1Ii + iIi1ii1I1
  IIi1i11111 = O0Oo000ooO00 ( IiI )
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1i11111 )
  for IiI111111IIII , iII1 , ooo0O , oO0o0 , Iii1IIII11I in i1I1i :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    o0o0OO0o00o0O ( Iii1IIII11I , IiI111111IIII , 222 , iII1 , oO0o0 , ooo0O )
    if 28 - 28: oO0o - IIIi + OOooOOo + O0O0OoOO0 / iI11I1II1I1I
    oOooOo0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
    if 68 - 68: O0OoO + IIIi . o0o00Oo0O . O0O0OoOO0 % ooOoO0O00 % O0OoO
def i1I1iIoOOoO ( ) :
 if 87 - 87: OOooOOo % iI11I1II1I1I
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 Oo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 72 - 72: O0OoO . O0OoO - Ii1I
 for I1ii1I1Ii in Oo :
  III1II1i = oo0OooOOo0 + I1ii1I1Ii + iIi1ii1I1
  IIi1i11111 = O0Oo000ooO00 ( III1II1i )
  i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi1i11111 )
  for Iii1IIII11I , ooo0O , IiI111111IIII , iI1I , oO0o0 , iI1i1IiIIIIi in i1I1i :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    i1o0oo0Ooooo0 ( Iii1IIII11I , IiI111111IIII , iI1i1IiIIIIi , iI1I , oO0o0 , ooo0O )
    if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
    oOooOo0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
    if 58 - 58: O0OoO . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
def I1Iii1Ii1i1 ( ) :
 if 10 - 10: IIIIi1i . ooOoO0O00 + O0O0OoOO0
 o0ooo0 = O000OOo00oo ( oo0OooOOo0 + 'spongemain.php' )
 i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , ooo0O , IiI111111IIII , iI1I , oO0o0 , iI1i1IiIIIIi in i1I1i :
  i1o0oo0Ooooo0 ( Iii1IIII11I , IiI111111IIII , iI1i1IiIIIIi , iI1I , oO0o0 , ooo0O )
  oOooOo0 ( 'movies' , 'MAIN' )
def oOOoOOO0oo0 ( url ) :
 if 87 - 87: OO0 / OOooOOo % I11i * IIIi
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOOOoo0o = ( '%s%s' % ( iiiI1IiIIii , url ) )
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOooo000oOO )
 for url , iII1 , ooo0O , IIIIiii , Iii1IIII11I in i1I1i :
  Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
  for OOOo00 in Ii11Ii1iI :
   if OOOo00 == url :
    Iii1IIII11I = ( '[COLORred]Watched - [/COLOR]' + Iii1IIII11I ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o0o0OO0o00o0O ( Iii1IIII11I , url , 222 , iII1 , IIIIiii , ooo0O )
  if 15 - 15: oO0o0OOOO
  oOooOo0 ( 'movies' , 'MAIN' )
  if 94 - 94: iii1iiii1 % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: I1ii11iIi11i - oO0o0OOOO
  if 24 - 24: ii . oO0o * IIiIiII11i
def o0oO00 ( url ) :
 if 88 - 88: oO0o0OOOO + Ii % IIIi * O0OoO * O0OoO * O0O0OoOO0
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , ooo0O , url , iI1I , oO0o0 , iI1i1IiIIIIi in i1I1i :
  i1o0oo0Ooooo0 ( Iii1IIII11I , url , iI1i1IiIIIIi , iI1I , oO0o0 , ooo0O )
  if 24 - 24: OO0 / IIIIi1i + ooo0oo0o0oo . ooo0oo0o0oo
  oOooOo0 ( 'movies' , 'MAIN' )
  if 39 - 39: OO0 + o0o00Oo0O / ooOoO0O00 % ooo0oo0o0oo / IIIi * ooo0oo0o0oo
  if 77 - 77: ooo0oo0o0oo . iii1iiii1 % OOooOOo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: ooo0oo0o0oo % IIIIi1i % I11i % IIIi + oO0o0OOOO % OOooOOo
def o0o0OO0o00o0O ( name , url , mode , iconimage , fanart , description ) :
 if 3 - 3: IIIi
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i11II11i1iI . setProperty ( "Fanart_Image" , fanart )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = False )
 return O00oO0o000oO
 if 43 - 43: I1ii11iIi11i . iii1iiii1
def i1o0oo0Ooooo0 ( name , url , mode , iconimage , fanart , description ) :
 if 12 - 12: iii1iiii1 + O0OoO + oO0o0OOOO . ooo0oo0o0oo / O0O0OoOO0
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i11II11i1iI . setProperty ( "Fanart_Image" , fanart )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = True )
 return O00oO0o000oO
if 29 - 29: ooo0oo0o0oo . OO0 - IIiIiII11i
if 68 - 68: iI11I1II1I1I + IIiIiII11i / IIIi
if 91 - 91: OOooOOo % iI11I1II1I1I . oOo0O0Ooo
if 70 - 70: oO0o0OOOO % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / iii1iiii1
if 100 - 100: Ii1I * Ii % IIIi / I1ii11iIi11i / OO0 + Ii1I
if 59 - 59: iii1iiii1 - ooo0oo0o0oo
if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
if 5 - 5: ooo0oo0o0oo
if 84 - 84: IIiIiII11i * IIIi * IIiIiII11i % ooo0oo0o0oo / oOo0O0Ooo
if 100 - 100: ooo0oo0o0oo . O0O0OoOO0 - iI11I1II1I1I . Ii / IIiIiII11i
if 71 - 71: iii1iiii1 * I1ii11iIi11i . oO0o0OOOO
if 49 - 49: ooo0oo0o0oo * o0o00Oo0O . ooo0oo0o0oo
if 19 - 19: IIiIiII11i - ooo0oo0o0oo
if 59 - 59: I11i * oO0o - O0O0OoOO0 . O0OoO
if 89 - 89: O0OoO
def o00oo0OO0 ( string ) :
 if OOOO0OOoO0O0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 60 - 60: OO0
def O000O ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iiii1IIi1 = [ ]
 try :
  if 87 - 87: ooo0oo0o0oo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iiiiiIIii ) == False :
  o00oo0OO0 ( 'Making Favorites File' )
  iiii1IIi1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Ii1iI111 = open ( iiiiiIIii , "w" )
  Ii1iI111 . write ( json . dumps ( iiii1IIi1 ) )
  Ii1iI111 . close ( )
 else :
  o00oo0OO0 ( 'Appending Favorites' )
  Ii1iI111 = open ( iiiiiIIii ) . read ( )
  I1IiI = json . loads ( Ii1iI111 )
  I1IiI . append ( ( name , url , iconimage , fanart , mode ) )
  oo0O0o = open ( iiiiiIIii , "w" )
  oo0O0o . write ( json . dumps ( I1IiI ) )
  oo0O0o . close ( )
  if 44 - 44: O0OoO / O0OoO . I11i % ooo0oo0o0oo + OOooOOo
  if 57 - 57: IIIIi1i % oO0o - oO0o
def ii1iIII ( ) :
 if os . path . exists ( iiiiiIIii ) == False :
  iiii1IIi1 = [ ]
  o00oo0OO0 ( 'Making Favorites File' )
  iiii1IIi1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Ii1iI111 = open ( iiiiiIIii , "w" )
  Ii1iI111 . write ( json . dumps ( iiii1IIi1 ) )
  Ii1iI111 . close ( )
 else :
  iIii11Iiiiii = json . loads ( open ( iiiiiIIii ) . read ( ) )
  iIiiiIiIi = len ( iIii11Iiiiii )
  for i1I1Ii11i in iIii11Iiiiii :
   Iii1IIII11I = i1I1Ii11i [ 0 ]
   IiI111111IIII = i1I1Ii11i [ 1 ]
   iII1 = i1I1Ii11i [ 2 ]
   try :
    I1iIiiiI1 = i1I1Ii11i [ 3 ]
    if I1iIiiiI1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     I1iIiiiI1 = iII1
    else :
     I1iIiiiI1 = oO0o0
   try : OOO0O00Oo = i1I1Ii11i [ 5 ]
   except : OOO0O00Oo = None
   try : ii1 = i1I1Ii11i [ 6 ]
   except : ii1 = None
   if 86 - 86: IIIi - oO0o
   if i1I1Ii11i [ 4 ] == 0 :
    iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , '' , iII1 , oO0o0 , '' , 'fav' )
   else :
    iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , i1I1Ii11i [ 4 ] , iII1 , oO0o0 , '' , 'fav' )
    if 63 - 63: oOo0O0Ooo / OOooOOo + ii . oO0o0OOOO . OO0
def IiI1iiI11 ( name ) :
 I1IiI = json . loads ( open ( iiiiiIIii ) . read ( ) )
 for OOoOOOO00 in range ( len ( I1IiI ) ) :
  if I1IiI [ OOoOOOO00 ] [ 0 ] == name :
   del I1IiI [ OOoOOOO00 ]
   oo0O0o = open ( iiiiiIIii , "w" )
   oo0O0o . write ( json . dumps ( I1IiI ) )
   oo0O0o . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + iii1iiii1
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * IIIi
def ii1ii111 ( ) :
 Oo0O0000Oo00o = os . path . join ( Ooo , 'addons.ini' )
 II1ii = open ( Oo0O0000Oo00o , "w+" )
 if 89 - 89: IIIIi1i . Ii * o0o00Oo0O
 II1ii . write ( r'# This file contains the "built-in" channels' + '\n' )
 II1ii . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 II1ii . write ( r'[plugin.video.GenieTv]' + '\n' )
 II1ii . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F191.m3u8&mode=10012&name===BBC+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F190.m3u8&mode=10012&name===BBC+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BBC Three=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F189.m3u8&mode=10012&name===BBC+Three+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;description=' + '\n' )
 II1ii . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F188.m3u8&mode=10012&name===BBC+Four+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F208.m3u8&mode=10012&name===ITV1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;description=' + '\n' )
 II1ii . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F207.m3u8&mode=10012&name===ITV2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F206.m3u8&mode=10012&name===ITV3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F205.m3u8&mode=10012&name===ITV4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'ITV Encore=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F328.m3u8&mode=10012&name===ITV+Encore&amp;iconimage=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;fanart=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;description=' + '\n' )
 II1ii . write ( r'ITVBe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F203.m3u8&mode=10012&name===ITV+BE+UK&amp;iconimage=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;fanart=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'E4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F775.m3u8&mode=10012&name===E4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'More4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F776.m3u8&mode=10012&name===More4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F187.m3u8&mode=10012&name===5%2A+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F186.m3u8&mode=10012&name===5USA+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F183.m3u8&mode=10012&name===Channel+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F185.m3u8&mode=10012&name===Channel+5+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;description=' + '\n' )
 II1ii . write ( r'alibi HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F329.m3u8&mode=10012&name===Alibi+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Dave HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F325.m3u8&mode=10012&name===Dave+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F326.m3u8&mode=10012&name===Gold+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F324.m3u8&mode=10012&name===Pick+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Really=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F631.m3u8&mode=10012&name===Really&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F377.m3u8&mode=10012&name===Yesterday+UK&amp;iconimage=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;fanart=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F518.m3u8&mode=10012&name===Watch+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'CBS Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F637.m3u8&mode=10012&name===CBS+Action+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'CBS Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F636.m3u8&mode=10012&name===CBC+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CBS Reality=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F635.m3u8&mode=10012&name===CBS+Reality+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'True Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F634.m3u8&mode=10012&name===True+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Challenge=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F772.m3u8&mode=10012&name===Challenge+UK&amp;iconimage=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;fanart=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F194.m3u8&mode=10012&name===RTE+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F193.m3u8&mode=10012&name===RTE+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F192.m3u8&mode=10012&name===TG4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'3e=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F769.m3u8&mode=10012&name===3e+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F774.m3u8&mode=10012&name===TV3+UK&amp;iconimage=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;fanart=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'ComedyXtra=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F767.m3u8&mode=10012&name===Comedy+Central+Extra+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F179.m3u8&mode=10012&name===FOX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Syfy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F180.m3u8&mode=10012&name===Syfy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;description=' + '\n' )
 II1ii . write ( r'TCM=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F632.m3u8&mode=10012&name===TCM+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TLC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F768.m3u8&mode=10012&name===TLC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Universal HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F404.m3u8&mode=10012&name===Universal+Channel+UK&amp;iconimage=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;fanart=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Universal+1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F771.m3u8&mode=10012&name===Universal+Channel+%2B1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F32.m3u8&mode=10012&name===Sky+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F33.m3u8&mode=10012&name===Sky+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F35.m3u8&mode=10012&name===Sky+Living+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F34.m3u8&mode=10012&name===Sky+Atlantic+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F639.m3u8&mode=10012&name===Food+Network&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F516.m3u8&mode=10012&name===Sky+Movies+Premiere+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F732.m3u8&mode=10012&name===Sky+Movies+Action+%26+Adventure+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F514.m3u8&mode=10012&name===Sky+Movies+Crime+%26+Thriller+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F511.m3u8&mode=10012&name===Sky+Movies+Sci-Fi+%26+Horror+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F513.m3u8&mode=10012&name===Sky+Movies+Comedy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F512.m3u8&mode=10012&name===Sky+Movies+Greats+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F46.m3u8&mode=10012&name===Sky+Movies+Showcase+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F45.m3u8&mode=10012&name===Sky+Movies+Select+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F510.m3u8&mode=10012&name===Sky+Movies+Drama+%26+Romance+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F509.m3u8&mode=10012&name===Sky+Movies+Family+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F195.m3u8&mode=10012&name===Sky+Movies+Disney+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F182.m3u8&mode=10012&name===Film4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Movies 24=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F633.m3u8&mode=10012&name===Movies+24+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'JollyHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F739.m3u8&mode=10012&name===JollyHD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Film Dy HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F777.m3u8&mode=10012&name===Film+Dy+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Film Nje HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F778.m3u8&mode=10012&name===Film+Nje+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F564.m3u8&mode=10012&name===HBO+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO 2 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F672.m3u8&mode=10012&name===HBO+2+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO 3 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F738.m3u8&mode=10012&name===HBO+3+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO 1 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F675.m3u8&mode=10012&name===HBO+1+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO 2 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F674.m3u8&mode=10012&name===HBO+2+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO 3 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F673.m3u8&mode=10012&name===HBO+3+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TVCINE 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F851.m3u8&mode=10012&name===TVCINE+1+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC1.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC1.png+&amp;description=' + '\n' )
 II1ii . write ( r'TVCINE 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F850.m3u8&mode=10012&name===TVCINE+2+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC2.png&amp;fanart=http%3A//www.zipestream.com/images/TVC2.png&amp;description=' + '\n' )
 II1ii . write ( r'TVCINE 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F849.m3u8&mode=10012&name===TVCINE+3+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC3.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC3.png+&amp;description=' + '\n' )
 II1ii . write ( r'TVCINE 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F848.m3u8&mode=10012&name===TVCINE+4+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC4.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC4.png+&amp;description=' + '\n' )
 II1ii . write ( r'Hollywood (Pt)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F702.m3u8&mode=10012&name===Hollywood+%28Pt%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'US &amp; UK Movies from Asia=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F396.m3u8&mode=10012&name===US+%26+UK+Movies+from+Asia&amp;iconimage=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;fanart=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'ABC HD US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F295.m3u8&mode=10012&name===ABC+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'ABC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F11.m3u8&mode=10012&name===ABC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'A&E=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F16.m3u8&mode=10012&name===A%26E+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'AMC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F52.m3u8&mode=10012&name===AMC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'AXS TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F392.m3u8&mode=10012&name===AXS+TV+%28US%29&amp;iconimage=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;fanart=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Bravo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F14.m3u8&mode=10012&name===Bravo+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F250.m3u8&mode=10012&name===CBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;description=' + '\n' )
 II1ii . write ( r'CW=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F626.m3u8&mode=10012&name===CW+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F297.m3u8&mode=10012&name===Fox+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F13.m3u8&mode=10012&name===Fox+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F409.m3u8&mode=10012&name===FX+%28US%29&amp;iconimage=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;fanart=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'NBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F15.m3u8&mode=10012&name===NBC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'PBSNET (PBS)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F398.m3u8&mode=10012&name===PBS+%28US%29&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;fanart=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Lifetime HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F627.m3u8&mode=10012&name===Lifetime+USA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Spike TV<=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F375.m3u8&mode=10012&name===Spike+%28US%29&amp;iconimage=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;fanart=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Syfy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F238.m3u8&mode=10012&name===Syfy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F253.m3u8&mode=10012&name===TBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TNT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F381.m3u8&mode=10012&name===TNT+%28US%29&amp;iconimage=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;fanart=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F379.m3u8&mode=10012&name===USA+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'KTLA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F628.m3u8&mode=10012&name===KTLA+/CW&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Global BC (CA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F399.m3u8&mode=10012&name===Global+BC+%28CA%29&amp;iconimage=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;fanart=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Space HD Ca=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F630.m3u8&mode=10012&name===Space+HD+Ca&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'WPIX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F629.m3u8&mode=10012&name===WPIX+II+CA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Hallmark Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F525.m3u8&mode=10012&name===Hallmark+Channel+HD&amp;iconimage=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;fanart=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'CineMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F553.m3u8&mode=10012&name===Cinemax+East&amp;iconimage=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;fanart=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;description=' + '\n' )
 II1ii . write ( r'Cinemax 5 StarMAX HD East (5MAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F403.m3u8&mode=10012&name===Cinemax+5+StarMax&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;fanart=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;description=' + '\n' )
 II1ii . write ( r'Cinemax ActionMax HD East (AMAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F402.m3u8&mode=10012&name===Cinemax+ActionMax+East&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'MoreMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F401.m3u8&mode=10012&name===Cinemax+Moremax&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'HBO (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F249.m3u8&mode=10012&name===HBO&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'HBO Comedy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F244.m3u8&mode=10012&name===HBO+Comedy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'HBO Signature (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F247.m3u8&mode=10012&name===HBO+Signature&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HBO Zone (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F242.m3u8&mode=10012&name===HBO+Zone&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Starz (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F582.m3u8&mode=10012&name===Starz+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Starz Cinema=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F400.m3u8&mode=10012&name===Starz+Cinema+East&amp;iconimage=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;fanart=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;description=' + '\n' )
 II1ii . write ( r'Starz Edge (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F413.m3u8&mode=10012&name===Starz+Edge+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Encore (ENCe)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F581.m3u8&mode=10012&name===Starz+Encore+East+%28US%29&amp;iconimage=http%3A//www.secv.com/images/premium_starz.jpg+&amp;fanart=http%3A//www.secv.com/images/premium_starz.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Showtime=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F554.m3u8&mode=10012&name===Showtime+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F414.m3u8&mode=10012&name===Showtime+2+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Showtime West=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F416.m3u8&mode=10012&name===Showtime+West&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F415.m3u8&mode=10012&name===Showtime+Showcase+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'BabyTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F523.m3u8&mode=10012&name===BabyTV&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F519.m3u8&mode=10012&name===Cartoon+Netwrk&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F231.m3u8&mode=10012&name===Disney+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F230.m3u8&mode=10012&name===Disney+Jr.+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Disney XD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F770.m3u8&mode=10012&name===Disney+XD+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Nicktoons=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F520.m3u8&mode=10012&name===Nicktoons&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Nickelodeon=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F521.m3u8&mode=10012&name===Nickelodeon&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Nick Jr.=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F522.m3u8&mode=10012&name===Nick+Jr.&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Animal Planet (APL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F198.m3u8&mode=10012&name===Animal+Planet+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F200.m3u8&mode=10012&name===Discovery+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Disc.History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F201.m3u8&mode=10012&name===Discovery+History+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Disc.Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F199.m3u8&mode=10012&name===Discovery+Science+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F168.m3u8&mode=10012&name===Discovery+Turbo+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'DMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F638.m3u8&mode=10012&name===DMAX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F196.m3u8&mode=10012&name===History+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'H2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F468.m3u8&mode=10012&name===H2+UK&amp;iconimage=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;fanart=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CI=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F202.m3u8&mode=10012&name===Crime+%26+Investigation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F197.m3u8&mode=10012&name===National+Geographic+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'National Geographic Wild=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F622.m3u8&mode=10012&name===Nat+Geo+Wild+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'MTV HITS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F235.m3u8&mode=10012&name===MTV+Hits&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F234.m3u8&mode=10012&name===MTV+Music+UK&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;description=' + '\n' )
 II1ii . write ( r'VH1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F556.m3u8&mode=10012&name===VH1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F323.m3u8&mode=10012&name===Sky+Sports+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F18.m3u8&mode=10012&name===Sky+Sports+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F322.m3u8&mode=10012&name===Sky+Sports+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F19.m3u8&mode=10012&name===Sky+Sports+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F321.m3u8&mode=10012&name===Sky+Sports+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F20.m3u8&mode=10012&name===Sky+Sports+3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F320.m3u8&mode=10012&name===Sky+Sports+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F21.m3u8&mode=10012&name===Sky+Sports+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 5 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F339.m3u8&mode=10012&name===Sky+Sports+5+HD&amp;iconimage=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;fanart=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F22.m3u8&mode=10012&name===Sky+Sports+5+UK&amp;iconimage=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;fanart=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports F1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F374.m3u8&mode=10012&name===Sky+Sports+F1+HD&amp;iconimage=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;fanart=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F24.m3u8&mode=10012&name===Sky+Sports+F1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky SpN HQ HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F23.m3u8&mode=10012&name===Sky+Sports+News+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F316.m3u8&mode=10012&name===BT+Sport+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F309.m3u8&mode=10012&name===BT+Sport+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F308.m3u8&mode=10012&name===BT+Sport+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sports 2 HD (1080) Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F599.m3u8&mode=10012&name===BT+Sports+2+HD+%281080%29+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sports 2 HD Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F707.m3u8&mode=10012&name===BT+Sports+2+HD+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F26.m3u8&mode=10012&name===BT+Sport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport EurHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F382.m3u8&mode=10012&name===BT+Sport+Europe+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F705.m3u8&mode=10012&name===BT+Sport+Europe&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BT Sport\/\/ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F28.m3u8&mode=10012&name===BT+Sport+ESPN&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Premier HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F310.m3u8&mode=10012&name===Premier+Sports+HD&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Premier Sports HD 1080P=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F384.m3u8&mode=10012&name===Premier+Sports+HD+1080P&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Premier Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F175.m3u8&mode=10012&name===Premier+Sports+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Setanta Ireland=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F176.m3u8&mode=10012&name===Setanta+Sports+Ireland+1+UK&amp;iconimage=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;fanart=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;description=' + '\n' )
 II1ii . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F170.m3u8&mode=10012&name===At+the+Races+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F171.m3u8&mode=10012&name===Racing+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MUTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F172.m3u8&mode=10012&name===Manchester+United+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;description=' + '\n' )
 II1ii . write ( r'LFCTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F174.m3u8&mode=10012&name===Liverpool+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;description=' + '\n' )
 II1ii . write ( r'Chelsea TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F177.m3u8&mode=10012&name===Chelsea+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F269.m3u8&mode=10012&name===Eurosport+1+UK&amp;iconimage=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;fanart=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Eurosport 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F748.m3u8&mode=10012&name===Eurosport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'1HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F83.m3u8&mode=10012&name===BEIN+SPORTS+1&amp;iconimage=http%3A//digigroup.az/media/images/1.jpg+&amp;fanart=http%3A//digigroup.az/media/images/1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'2HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F84.m3u8&mode=10012&name===BEIN+SPORTS+2&amp;iconimage=http%3A//digigroup.az/media/images/2.jpg++&amp;fanart=http%3A//digigroup.az/media/images/2.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'3HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F85.m3u8&mode=10012&name===BEIN+SPORTS+3&amp;iconimage=http%3A//digigroup.az/media/images/3.jpg++&amp;fanart=http%3A//digigroup.az/media/images/3.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'4HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F86.m3u8&mode=10012&name===BEIN+SPORTS+4&amp;iconimage=http%3A//digigroup.az/media/images/4.jpg++&amp;fanart=http%3A//digigroup.az/media/images/4.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'5HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F87.m3u8&mode=10012&name===BEIN+SPORTS+5&amp;iconimage=http%3A//digigroup.az/media/images/5.jpg++&amp;fanart=http%3A//digigroup.az/media/images/5.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'6HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F88.m3u8&mode=10012&name===BEIN+SPORTS+6&amp;iconimage=http%3A//digigroup.az/media/images/6.jpg++&amp;fanart=http%3A//digigroup.az/media/images/6.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'7HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F89.m3u8&mode=10012&name===BEIN+SPORTS+7&amp;iconimage=http%3A//digigroup.az/media/images/7.jpg++&amp;fanart=http%3A//digigroup.az/media/images/7.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'8HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F90.m3u8&mode=10012&name===BEIN+SPORTS+8&amp;iconimage=http%3A//digigroup.az/media/images/8.jpg++&amp;fanart=http%3A//digigroup.az/media/images/8.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'9HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F91.m3u8&mode=10012&name===BEIN+SPORTS+9&amp;iconimage=http%3A//digigroup.az/media/images/9.jpg++&amp;fanart=http%3A//digigroup.az/media/images/9.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'10HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F92.m3u8&mode=10012&name===BEIN+SPORTS+10&amp;iconimage=http%3A//digigroup.az/media/images/10.jpg++&amp;fanart=http%3A//digigroup.az/media/images/10.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'12HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F424.m3u8&mode=10012&name===BEIN+SPORTS+12&amp;iconimage=http%3A//digigroup.az/media/images/12.jpg++&amp;fanart=http%3A//digigroup.az/media/images/12.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Astro SuperSport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F60.m3u8&mode=10012&name===Astro+Supersport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Astro SuperSport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F59.m3u8&mode=10012&name===Astro+Supersport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Astro SuperSport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F58.m3u8&mode=10012&name===Astro+Supersport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Astro SuperSport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F57.m3u8&mode=10012&name===Astro+Supersport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 1 (CTH 211 SD / 56HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F67.m3u8&mode=10012&name===CTH+Stadium+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 2 (CTH 212 SD / 57 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F66.m3u8&mode=10012&name===CTH+Stadium+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 3 (CTH 213 SD / 58 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F65.m3u8&mode=10012&name===CTH+Stadium+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 4 (CTH 214 SD / 59 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F64.m3u8&mode=10012&name===CTH+Stadium+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 5 (CTH 216 SD / 60 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F63.m3u8&mode=10012&name===CTH+Stadium+5+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM 6 (CTH 216 SD / 61 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F62.m3u8&mode=10012&name===CTH+STADIUM+6+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'STADIUM X (CTH 217 SD / 62 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F61.m3u8&mode=10012&name===CTH+STADIUM+X+HD&amp;iconimage=http%3A//stepfb.net/live/movieposters/136.png++&amp;fanart=http%3A//stepfb.net/live/movieposters/136.png++&amp;description=' + '\n' )
 II1ii . write ( r'TV Arena Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F163.m3u8&mode=10012&name===Arena+Sport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TV Arena Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F167.m3u8&mode=10012&name===Arena+Sport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'TV Arena Sport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F164.m3u8&mode=10012&name===Arena+Sport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'TV Arena Sport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F165.m3u8&mode=10012&name===Arena+Sport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'TSN1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F96.m3u8&mode=10012&name===TSN+1&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'TSN2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F97.m3u8&mode=10012&name===TSN+2&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'TSN3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F98.m3u8&mode=10012&name===TSN+3&amp;iconimage=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;fanart=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'TSN4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F99.m3u8&mode=10012&name===TSN+4&amp;iconimage=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;fanart=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX Sports 1 Eredivisie HD"=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F531.m3u8&mode=10012&name===Fox+Sports+1+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F530.m3u8&mode=10012&name===Fox+Sports+2+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX Sports 3 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F529.m3u8&mode=10012&name===Fox+Sports+3+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F528.m3u8&mode=10012&name===Fox+Sports+4+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX Sports 5 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F527.m3u8&mode=10012&name===Fox+Sports+5+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Arena Sport 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F166.m3u8&mode=10012&name===Arena+Sport+5&amp;iconimage=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;fanart=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'CBS Sports Network (CBS SN)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F378.m3u8&mode=10012&name===CBS+Sports+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'NBA TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F304.m3u8&mode=10012&name===NBA+TV+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'NFL NETWORK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F95.m3u8&mode=10012&name===NFL+Network+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Viasat Sports RU=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F278.m3u8&mode=10012&name===Viasat+Sports+RU&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;description=' + '\n' )
 II1ii . write ( r'E! Entertainment Television=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F835.m3u8&mode=10012&name===E%21+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F830.m3u8&mode=10012&name===London+Live&amp;iconimage=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;fanart=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'AXNHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F842.m3u8&mode=10012&name===AXN+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'AXNBLACKHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F841.m3u8&mode=10012&name===AXN+BLACK+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F845.m3u8&mode=10012&name===Fox+hd+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOXLIFE=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F843.m3u8&mode=10012&name===FoxLife+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOXCRIME=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F844.m3u8&mode=10012&name===Fox+Crime+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MOVHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F839.m3u8&mode=10012&name===Mov+HD+PT&amp;iconimage=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;fanart=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;description=' + '\n' )
 II1ii . write ( r'SYFYHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F838.m3u8&mode=10012&name===SyFy+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'True Movies 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F853.m3u8&mode=10012&name===True+Movies+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'True Movies 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F852.m3u8&mode=10012&name===True+Movies+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FOXMOVIESHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F846.m3u8&mode=10012&name===Fox+Movies+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F837.m3u8&mode=10012&name===Comedy+Central+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Discovery Family Channel (DFCH)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F836.m3u8&mode=10012&name===Discovery+Family++HD+US&amp;iconimage=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;fanart=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'E! (E!)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F834.m3u8&mode=10012&name===E%21+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'ABC Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F833.m3u8&mode=10012&name===Family+Channel+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'VH1 (VH1)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F828.m3u8&mode=10012&name===VH1+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Slice=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F829.m3u8&mode=10012&name===SLICE+TV+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Lifetime Movie Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F524.m3u8&mode=10012&name===LMN+US&amp;iconimage=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;fanart=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F519.m3u8&mode=10012&name===Cartoon+Network+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Cartoon Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F809.m3u8&mode=10012&name===Cartoon+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CBBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F808.m3u8&mode=10012&name===CBBC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CBeebies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F807.m3u8&mode=10012&name===Cbeebies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F818.m3u8&mode=10012&name===Animal+Planet+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'The Discovery Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F817.m3u8&mode=10012&name===Discovery+Channel+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Do-It-Yourself Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F815.m3u8&mode=10012&name===DIY+Network+US&amp;iconimage=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;fanart=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'H2 (H2)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F814.m3u8&mode=10012&name===H2+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'History Channel (HIST)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F813.m3u8&mode=10012&name===HISTORY+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Investigation Discovery (ID)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F812.m3u8&mode=10012&name===Investigation+Discovery++US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F810.m3u8&mode=10012&name===National+Geographic+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'NatGeo WILD (NGWILD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F811.m3u8&mode=10012&name===NAT+GEO+WILD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Clubland TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F806.m3u8&mode=10012&name===Clubland+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'The Box=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F805.m3u8&mode=10012&name===The+Box&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'BoxNation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F173.m3u8&mode=10012&name===Box+Nation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Big Ten HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F823.m3u8&mode=10012&name===Big+Ten+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'MLB Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F822.m3u8&mode=10012&name===MLB+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Willow Cricket=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F824.m3u8&mode=10012&name===Willow+Sports+HD+US&amp;iconimage=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;fanart=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;description=' + '\n' )
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + ooo0oo0o0oo
 if 27 - 27: O0OoO
 II1ii . write ( r'AXN White HD PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F840.m3u8&mode=10012&name===AXN+White+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CINEMUNDO PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F847.m3u8&mode=10012&name===CINEMUNDO+PT&amp;iconimage=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;fanart=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'FreeForm US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F832.m3u8&mode=10012&name===FreeForm+US&amp;iconimage=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;fanart=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'HIFI US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F831.m3u8&mode=10012&name===HIFI+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Discovery Home &amp; Health UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F816.m3u8&mode=10012&name===Discovery+Home+%26+Health+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'CITY TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F803.m3u8&mode=10012&name===CITY+TV&amp;iconimage=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;fanart=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'DANCE HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F802.m3u8&mode=10012&name===DANCE+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Dream music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F799.m3u8&mode=10012&name===Dream+music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Europe Plus Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F796.m3u8&mode=10012&name===Europe+Plus+Music&amp;iconimage=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;fanart=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;description=' + '\n' )
 II1ii . write ( r'HITV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F804.m3u8&mode=10012&name===HITV+Music&amp;iconimage=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;fanart=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Music Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F800.m3u8&mode=10012&name===Music+Channel&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Heavy Metal=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F801.m3u8&mode=10012&name===Heavy+Metal&amp;iconimage=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;fanart=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;description=' + '\n' )
 II1ii . write ( r'Si TV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F797.m3u8&mode=10012&name===Si+TV+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'VEVO Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F798.m3u8&mode=10012&name===VEVO+Music&amp;iconimage=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;fanart=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'beIN Sport 1 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F9.m3u8&mode=10012&name===beIN+Sport+1+%28Fr%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'beIN Sport 2 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F81.m3u8&mode=10012&name===beIN+Sport+2+%28Fr%29&amp;iconimage=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;fanart=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;description=' + '\n' )
 II1ii . write ( r'beIN Sport 3 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F82.m3u8&mode=10012&name===beIN+Sport+3+%28Fr%29&amp;iconimage=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;fanart=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'Bein Sport US HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F766.m3u8&mode=10012&name===Bein+Sport+US+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'RDS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F505.m3u8&mode=10012&name===RDS&amp;iconimage=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;fanart=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;description=' + '\n' )
 II1ii . write ( r'Fox Sports 1 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F262.m3u8&mode=10012&name===Fox+Sports+1+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Fox Sports 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F261.m3u8&mode=10012&name===Fox+Sports+2+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Fox Sports 1 (Asia)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F391.m3u8&mode=10012&name===Fox+Sports+1+%28Asia%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'KP+ PM HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F475.m3u8&mode=10012&name===KP%2B+PM+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'K+ 1 HD Sports/Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F390.m3u8&mode=10012&name===K%2B+1+HD+Sports/Movies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Skynet Sports HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F473.m3u8&mode=10012&name===Skynet+Sports+HD&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Skynet Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F474.m3u8&mode=10012&name===Skynet+Sports+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'True SportsHD 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F274.m3u8&mode=10012&name===True+SportsHD+3&amp;iconimage=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;fanart=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'True Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F276.m3u8&mode=10012&name===True+Sport+2&amp;iconimage=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;fanart=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;description=' + '\n' )
 II1ii . write ( r'NBC Sports Network (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F209.m3u8&mode=10012&name===NBC+Sports+Network+%28US%29&amp;iconimage=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;fanart=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;description=' + '\n' )
 II1ii . write ( r'EPL Extra Time 1 (USA TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F255.m3u8&mode=10012&name===EPL+Extra+Time+1+%28USA+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'EPL Extra Time 3 (Spike USA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F257.m3u8&mode=10012&name===EPL+Extra+Time+3+%28Spike+USA%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'EPL Extra Time 4 (AXS TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F258.m3u8&mode=10012&name===EPL+Extra+Time+4+%28AXS+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Sportsnet World=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F367.m3u8&mode=10012&name===Sportsnet+World+HD+US&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Sportsnet NY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F385.m3u8&mode=10012&name===Sportsnet+Ontario+HD&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sportsnet One HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F259.m3u8&mode=10012&name===Sportsnet+One+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F314.m3u8&mode=10012&name===ESPN+%28US%29&amp;iconimage=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;fanart=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;description=' + '\n' )
 II1ii . write ( r'ESPN 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F315.m3u8&mode=10012&name===ESPN+2+%28US%29&amp;iconimage=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;fanart=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sport Klub 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F594.m3u8&mode=10012&name===Sport+Klub+1&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sport Klub 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F593.m3u8&mode=10012&name===Sport+Klub+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sport Klub 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F592.m3u8&mode=10012&name===Sport+Klub+3&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Golf HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F260.m3u8&mode=10012&name===Golf+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Golf Channel 1080p=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F332.m3u8&mode=10012&name===Golf+Channel+1080p&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;description=' + '\n' )
 II1ii . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F178.m3u8&mode=10012&name===WWENetwork&amp;iconimage=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;fanart=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'Motor Sports 1 Aus=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F281.m3u8&mode=10012&name===Motor+Sports+1+Aus&amp;iconimage=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;fanart=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;description=' + '\n' )
 II1ii . write ( r'Fight Sports (USEE)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F433.m3u8&mode=10012&name===Fight+Sports+%28USEE%29&amp;iconimage=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;fanart=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sport 2 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F471.m3u8&mode=10012&name===Sky+Sport+2+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'Sky Sport 1 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F472.m3u8&mode=10012&name===Sky+Sport+1+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;description=' + '\n' )
 II1ii . write ( r'TyC Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F31.m3u8&mode=10012&name===TyC+Sports&amp;iconimage=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;fanart=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;description=' + '\n' )
 II1ii . write ( r'ORF Sport +=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + O0OoO000O0OO + '%2F' + iiI1IiI + '%2F423.m3u8&mode=10012&name===ORF+Sport+%2B&amp;iconimage=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;fanart=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;description=' + '\n' )
 if 52 - 52: iii1iiii1 % OOooOOo + iI11I1II1I1I * IIIi . O0O0OoOO0
 if 95 - 95: iI11I1II1I1I . ooo0oo0o0oo - ii * oO0o / I11i
def oOo0OO0o0 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + '247.png' , i11i1I1 + '247.png' , '' )
def II1I1I ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'musicch.png' , i11i1I1 + 'musicch.png' , '' )
def III11I ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'NEWS.png' , i11i1I1 + 'NEWS.png' , '' )
def i1o0oo0 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'adult.png' , i11i1I1 + 'adult.png' , '' )
def OoO0OOoO0Oo0 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1I1i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , IiI111111IIII , 1016 , i11i1I1 + 'TUTS.png' , i11i1I1 + 'TUTS.png' , '' )
  if 91 - 91: IIiIiII11i
  if 53 - 53: oO0o % I11i / O0OoO % ooo0oo0o0oo % oO0o % ii
def i11i1i ( ) :
 if 10 - 10: O0O0OoOO0 - Ii . Ii1I % ooOoO0O00
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Recent Episodes[/COLOR]' , '' , 10019 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Genres[/COLOR]' , '' , 10020 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search[/COLOR]' , '' , 10021 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - O0OoO . iI11I1II1I1I
def I111I1I ( ) :
 if 54 - 54: IIiIiII11i + oO0o0OOOO % oO0o0OOOO % I11i
 o0ooo0 = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1I1i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , iI1I , Iii1IIII11I , o0o0oOoOO0O in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I + '  -  ' + ( o0o0oOoOO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiI111111IIII , 10023 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
  if 25 - 25: IIIIi1i - I1ii11iIi11i
  if 10 - 10: o0o00Oo0O % ooo0oo0o0oo . oO0o + I11i + Ii1I
  if 52 - 52: OOooOOo / oO0o + iii1iiii1
def Iii1i11iiI1 ( ) :
 if 95 - 95: IIIi * iI11I1II1I1I + Ii1I
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Action[/COLOR]' , 'Aksiyon' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Adventure[/COLOR]' , 'Macera' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Animation[/COLOR]' , 'Animasyon' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Anime[/COLOR]' , 'Anime' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Biography[/COLOR]' , 'Biyografi' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Comedy[/COLOR]' , 'Komedi' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Drama[/COLOR]' , 'Dram' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Family[/COLOR]' , 'Aile' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']History[/COLOR]' , 'Tarih' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Horror[/COLOR]' , 'Korku' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Mystery[/COLOR]' , 'Gizem' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Romance[/COLOR]' , 'Romantik' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Sport[/COLOR]' , 'Spor' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Western[/COLOR]' , 'Tarih' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 if 5 - 5: I1ii11iIi11i
def o0oOo00 ( url ) :
 Oo00o0OO0O00o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIi1i11111 = cloudflare . source ( Oo00o0OO0O00o )
 i1I1i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 10022 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
  if 22 - 22: iI11I1II1I1I + ooo0oo0o0oo + Ii1I + iii1iiii1 - O0O0OoOO0
  if 48 - 48: O0O0OoOO0 - OOooOOo - oO0o + oOo0O0Ooo * O0O0OoOO0
  if 67 - 67: I1ii11iIi11i / OO0 - ooo0oo0o0oo
  if 74 - 74: oO0o0OOOO * O0O0OoOO0 - Ii1I % iI11I1II1I1I
def oOoOoO0o0 ( ) :
 if 18 - 18: O0O0OoOO0
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1i11111 = cloudflare . source ( IiI111111IIII )
 i1I1i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  if i11IIIiI11 in Iii1IIII11I . lower ( ) :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 10022 , i11i1I1 + 'dtv.png' )
   if 25 - 25: oO0o * IIIi % Ii + Ii * oO0o
   if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
   if 62 - 62: o0o00Oo0O . I1ii11iIi11i
def iI1ii ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iiI1IIIi , O0OooOO , i1i1 , Iii1IIII11I in i1I1i :
  o0oOoOo0 = ( i1i1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  III1IiI1i1i = ( O0OooOO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0OOOOOo0 = 'Season ' + III1IiI1i1i + 'Episode ' + o0oOoOo0 + Iii1IIII11I
  oooOoO ( o0OOOOOo0 , iiI1IIIi )
  if 62 - 62: O0OoO / IIiIiII11i + OOooOOo % OO0 / OOooOOo + Ii1I
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 2 - 2: Ii - iii1iiii1 + oO0o % oO0o0OOOO * O0O0OoOO0
  if 54 - 54: o0o00Oo0O - IIIIi1i . O0OoO % IIIIi1i + IIIIi1i
def oooOoO ( name , url ) :
 iiI1IIIi = url
 i1iI1Iiii1I = name
 ooOO00O00oo = cloudflare . source ( iiI1IIIi )
 Iiiii1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( ooOO00O00oo )
 for OOo , I1iII in Iiiii1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + i1iI1Iiii1I + I1iII + '[/COLOR]' , OOo , 10012 , i11i1I1 + 'dtv.png' )
  if 29 - 29: ooOoO0O00 % IIIIi1i / ooo0oo0o0oo + OOooOOo - O0OoO - Ii1I
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: iI11I1II1I1I . IIiIiII11i . ooOoO0O00 - I11i
 if 79 - 79: OO0 % O0OoO
def oO0O0o0O ( ) :
 if 100 - 100: OOooOOo % I1ii11iIi11i
 if 76 - 76: IIiIiII11i / oO0o + ii . Ii1I . oO0o0OOOO . OO0
 if 43 - 43: ooOoO0O00
 if 17 - 17: o0o00Oo0O - OOooOOo
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 if 34 - 34: O0O0OoOO0 * O0O0OoOO0 - Ii1I - o0o00Oo0O . Ii
 if 32 - 32: iI11I1II1I1I . oO0o * IIIi / O0OoO . IIiIiII11i - I1ii11iIi11i
 if 10 - 10: Ii1I / Ii - O0O0OoOO0 + IIIi * oOo0O0Ooo
 if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
 if 64 - 64: oO0o0OOOO + oO0o
 if 25 - 25: oOo0O0Ooo . OO0 + oOo0O0Ooo % O0O0OoOO0 * iI11I1II1I1I
 if 31 - 31: Ii + O0OoO - o0o00Oo0O
 if 51 - 51: oO0o * ooOoO0O00 / O0O0OoOO0 * O0OoO + OO0 % Ii1I
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Program[/COLOR]' , '' , 10043 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 if 34 - 34: IIIi * ii + O0O0OoOO0 + Ii
 if 22 - 22: ooOoO0O00
def I11io0Oo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1ii1II1ii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 i1I1i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1ii1II1ii ) )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
  if 4 - 4: IIiIiII11i
def Iiiii11IIii ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
  if 85 - 85: O0OoO . O0O0OoOO0 + iii1iiii1 . ooOoO0O00 / O0OoO % iii1iiii1
def O0oo00oOOO0o ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if 'episode' in url :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
  else :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , i11i1I1 + 'Next.png' , '' , '' )
  if 5 - 5: I11i / oOo0O0Ooo % O0O0OoOO0 . ooo0oo0o0oo
  if 86 - 86: ooOoO0O00 * OOooOOo . o0o00Oo0O - O0O0OoOO0 - I11i - OOooOOo
def i11IiI ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoIi1I1I = 'http://www.watchseries.ac/search/' + i11IIIiI11 . replace ( ' ' , '%20' )
 IIi1i11111 = O000OOo00oo ( OoIi1I1I )
 i1I1i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'watch online' in Iii1IIII11I :
   pass
  else :
   print IiI111111IIII
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac' + IiI111111IIII , 10044 , iI1I , '' , '' )
   if 56 - 56: o0o00Oo0O
   xbmcplugin . setContent ( OOOO , 'movies' )
   if 45 - 45: OOooOOo - oO0o - OOooOOo
def IIiiI ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , url , Iii1IIII11I , i1i1 , ooo0O in i1I1i :
  iII11iiiiiii = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1i1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + iII11iiiiiii + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , iI1I , '' , ooo0O )
  if 82 - 82: oO0o0OOOO / OO0 * oO0o0OOOO % Ii * IIiIiII11i
def OOOOOO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  iII11iiiiiii = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + iII11iiiiiii + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , i11i1I1 + 'Next.png' , '' , '' )
  if 77 - 77: I1ii11iIi11i
def II111I1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , iI1I , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , i11i1I1 + 'Next.png' , '' , '' )
  if 32 - 32: O0OoO % ooOoO0O00
def IIi1i1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIi1i11111 )
 i1ii1II1ii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O0OooOO , Ii1iiII1i in i1ii1II1ii :
  i1I1i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Ii1iiII1i ) )
  for url , Iii1IIII11I in i1I1i :
   iII11iiiiiii = ( O0OooOO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + iII11iiiiiii + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , url in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , i11i1I1 + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: O0OoO + O0O0OoOO0 + I11i
class i1i1iIII11i ( ) :
 if 40 - 40: iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 56 - 56: O0OoO
  iII11iiiiiii = name
  self . Get_Sources ( IiI111111IIII , iII11iiiiiii )
  if 49 - 49: OO0 . IIiIiII11i
  if 24 - 24: o0o00Oo0O . ii - oO0o * ii
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIi1i11111 = O000OOo00oo ( URL )
  i1I1i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIi1i11111 )
  for IiI111111IIII , Iii1IIII11I in i1I1i :
   URL = 'http://www.watchseries.ac/link/' + IiI111111IIII
   self . Get_site_link ( URL , season_name )
   if 12 - 12: o0o00Oo0O + ooo0oo0o0oo * ooOoO0O00 . oO0o
 def Get_site_link ( self , url , season_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIi1i11111 )
  Iiiii1i = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIi1i11111 )
  II1III1i1iiI = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIi1i11111 )
  for url in i1I1i :
   self . main ( url , season_name )
  for url in Iiiii1i :
   self . main ( url , season_name )
  for url in II1III1i1iiI :
   self . main ( url , season_name )
   if 71 - 71: iii1iiii1 - I11i - O0OoO
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iiI = 'DACLIPS'
   if iiI in i1i1iIII11i . source_list :
    pass
   else :
    self . daclips ( url , season_name , iiI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    iiI = 'FILEHOOT'
    if iiI in i1i1iIII11i . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , iiI )
   else :
    if 'thevideo.me' in url :
     iiI = 'THEVIDEO'
     if iiI in i1i1iIII11i . source_list :
      pass
     else :
      self . thevideo ( url , season_name , iiI )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      iiI = 'ALLMYVIDEOS'
      if iiI in i1i1iIII11i . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , iiI )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       iiI = 'VIDSPOT'
       if iiI in i1i1iIII11i . source_list :
        pass
       else :
        self . vidspot ( url , season_name , iiI )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        iiI = 'VODLOCKER'
        if iiI in i1i1iIII11i . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , iiI )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 81 - 81: ooo0oo0o0oo * Ii1I + IIiIiII11i % ooo0oo0o0oo
         if 46 - 46: IIiIiII11i % IIIIi1i - ooOoO0O00 / oO0o0OOOO * OOooOOo
 def allmyvid ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
  for oO0o0oOo , Iii1IIII11I in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 92 - 92: ooOoO0O00 % OO0 + OO0 - iI11I1II1I1I . O0O0OoOO0
 def vidspot ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIi1i11111 )
  for oO0o0oOo , Iii1IIII11I in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 33 - 33: I11i / o0o00Oo0O + O0OoO
 def thevideo ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIi1i11111 )
  for oO0o0oOo in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 75 - 75: ooo0oo0o0oo % Ii + iI11I1II1I1I
 def vodlocker ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIi1i11111 )
  for oO0o0oOo in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 92 - 92: OOooOOo % o0o00Oo0O
 def daclips ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIi1i11111 )
  for oO0o0oOo in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 55 - 55: iI11I1II1I1I * IIIIi1i
 def filehoot ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIi1i11111 )
  for oO0o0oOo in i1I1i :
   self . Printer ( oO0o0oOo , season_name , source_name )
   if 85 - 85: iI11I1II1I1I . IIiIiII11i
 def Printer ( self , Link , season_name , source_name ) :
  if 54 - 54: O0O0OoOO0 . ii % I1ii11iIi11i
  if Link in i1i1iIII11i . List :
   pass
  elif source_name in i1i1iIII11i . source_list :
   pass
  else :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + source_name + '[/COLOR]' , Link , 10012 , i11i1I1 + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   i1i1iIII11i . List . append ( Link )
   i1i1iIII11i . source_list . append ( source_name )
   if 22 - 22: O0OoO
   xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 22 - 22: IIIIi1i * oO0o0OOOO - I1ii11iIi11i * o0o00Oo0O / Ii
   if 78 - 78: I1ii11iIi11i * o0o00Oo0O / OO0 + ii + O0OoO
   if 23 - 23: IIIIi1i % ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
   if 94 - 94: ooOoO0O00
   if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
def iIIiiiI1iI1 ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Highlights[/COLOR]' , '' , 10008 , i11i1I1 + 'Highlights.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Fixtures[/COLOR]' , '' , 10009 , i11i1I1 + 'Fixtures.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live Sport On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , i11i1I1 + 'PremiereLeague.png' , ooOoOoo0O , '' )
 if 86 - 86: Ii1I * OO0
def O0oO0o0OOOOOO ( url ) :
 iiIi1IIi1I ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI1i11IiIiii , url , I11iiI1I1 , o0i1Ii11II , i1iiiiI11ii , Ii1i1i1111 , oooooOOo0o , Iii1I1I11iiI1 , Ii1iI111 , oOO0 , OoO000Oo0oO in i1I1i :
  I11iiI1I1 = I11iiI1I1
  if 'Arsenal' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'arsenal-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                                  ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Bournemouth' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'afc-bournemouth.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                       ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Burnley' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'KEGnQWW.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                                   ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Chelsea' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'chelsea.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                                  ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Crystal' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'CrystalPalace.0.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                       ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Everton' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'Everton.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                                   ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Hull' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'hull-city-afc.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                                 ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Leicester' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'leicester-city-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                       ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Liverpool' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'liverpool-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                               ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Manchester City' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'city-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '               ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Manchester United' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + '91.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '          ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Middlesbrough' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'middlesbrough-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                 ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Southampton' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'southampton-fc-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                   ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Stoke City' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'stoke-city.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                          ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Sunderland' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'sunderland-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                        ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Swansea' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'swansea-city-afc.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                    ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Tottenham' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'tottenham-hotspur_zps4e3ed7c1.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '        ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Watford' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'watford-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '                              ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'Bromwich' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'west-bromwich-albion-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '   ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  elif 'West Ham' in I11iiI1I1 :
   oOOO00o000o = i11i1I1 + 'west-ham.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + IiI1i11IiIiii + ' - ' + I11iiI1I1 + '             ' + o0i1Ii11II + '        ' + i1iiiiI11ii + '        ' + Ii1i1i1111 + '        ' + oooooOOo0o + '        ' + Iii1I1I11iiI1 + '        ' + Ii1iI111 + '        ' + oOO0 + '[/COLOR]'
  iiIi1IIi1I ( str ( Iii1IIII11I ) , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , oOOO00o000o , oOOO00o000o , I11iiI1I1 )
  if 46 - 46: o0o00Oo0O - OOooOOo . ii
def i1I111II ( description ) :
 I11iiI1I1 = description
 IiI111111IIII = ( 'http://www.fullmatchesandshows.com/?s=' + I11iiI1I1 ) . replace ( ' ' , '%20' )
 Oo0OOo ( IiI111111IIII )
 if 44 - 44: oO0o0OOOO * I11i
def II11ii1I11 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1I1i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiI111111IIII , 10010 , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI1I , ooOoOoo0O , '' )
  if 65 - 65: O0OoO + IIiIiII11i
def Oo0O0OO0OoO0 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1ii1II1ii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIi1i11111 )
 for i1ii1II1ii in i1ii1II1ii :
  iIIiI11iI1Ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1ii1II1ii ) )
  for o00oo in iIIiI11iI1Ii1 :
   o00oo = o00oo
  O0oO0oo0O = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1ii1II1ii ) )
  for oooOOO0ooOoOOO , iI1I , time , o0IiIiI111IIII1 in O0oO0oo0O :
   Iiii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0IiIiI111IIII1 )
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + o00oo + ' - ' + oooOOO0ooOoOOO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iI1I , ooOoOoo0O , ( str ( Iiii ) ) )
   if 100 - 100: O0OoO * o0o00Oo0O + oOo0O0Ooo + OOooOOo . O0OoO
 oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if 73 - 73: IIIi . IIiIiII11i * IIIIi1i % IIIi + OOooOOo - oO0o
def I1iIi1iIIIIiI ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , i11i1I1 + 'fanart.jpg' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , i11i1I1 + 'fanart.jpg' , '' )
 if 94 - 94: ooo0oo0o0oo * oO0o0OOOO * ii / I11i . ooo0oo0o0oo - I11i
def I1I1i ( url ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'TodaysMacthes.png' , ooOoOoo0O , '' )
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , url , Iii1IIII11I in i1I1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , iI1I )
 for url , iI1I , Iii1IIII11I in Iiiii1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , iI1I )
def Oo0OOo ( url ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'TodaysMacthes.png' , ooOoOoo0O , '' )
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 if 93 - 93: ooOoO0O00 % OOooOOo / iI11I1II1I1I * I11i . o0o00Oo0O % O0OoO
 if 88 - 88: IIIi % I1ii11iIi11i - oO0o0OOOO % IIIi + ooo0oo0o0oo - IIIIi1i
 if 23 - 23: o0o00Oo0O
 if 9 - 9: oO0o0OOOO * I1ii11iIi11i . OO0 * Ii - o0o00Oo0O
 if 54 - 54: oOo0O0Ooo * O0OoO + I11i % ooOoO0O00 - I11i + OOooOOo
 if 15 - 15: OOooOOo * IIIi + O0OoO . oO0o0OOOO % oOo0O0Ooo - OO0
 if 13 - 13: OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * ooOoO0O00 % oO0o0OOOO
 for url , iI1I , Iii1IIII11I in Iiiii1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , iI1I )
   if 82 - 82: ooo0oo0o0oo . OOooOOo / OO0 + IIIIi1i - OO0
def o00OOo0o0O ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIi1i11111 )
 for OOo in i1I1i :
  I111Iii1 = ( OOo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  oO000o ( 'http:' + I111Iii1 )
  if 30 - 30: ooOoO0O00
  if 75 - 75: oO0o0OOOO . O0OoO - iI11I1II1I1I * oO0o * IIIIi1i
  if 93 - 93: OO0
  if 18 - 18: OO0
def OOOooO00OO00O ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , url , 8046 , iI1I )
 for url in Iiiii1i :
  II11IiIi11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , i11i1I1 + 'Next.png' )
def OoOOooO0O ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( o0ooo0 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  oO000o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 3 - 3: IIiIiII11i - O0O0OoOO0 % OOooOOo / IIIi
def Ii1 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( o0ooo0 )
 for url in i1I1i :
  yt . PlayVideo ( url )
  if 80 - 80: Ii % Ii1I
def OOO00o0 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 97 - 97: Ii1I / Ii1I / iI11I1II1I1I % ooOoO0O00 . Ii1I . ooo0oo0o0oo
 i1I1i = re . compile ( '<a href="([^"]*)" >(.+?)</a></li>' ) . findall ( o0ooo0 )
 if 4 - 4: I1ii11iIi11i - oO0o - Ii * iii1iiii1 / O0O0OoOO0 - O0OoO
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , IiI111111IIII , 8041 , i11i1I1 + 'documentary.png' )
  if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
  if 82 - 82: IIiIiII11i / IIIIi1i
  if 96 - 96: I1ii11iIi11i / IIIi . IIiIiII11i . I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooIi111iII ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 next = re . compile ( 'class="inactive">.+?</a><a href="([^"]*)">Next</a></div>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , iI1I )
 for Iii1IIII11I , url , iI1I in Iiiii1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , iI1I )
 for url in next :
  II11IiIi11 ( 'NEXT PAGE' , url , 8041 , i11i1I1 + 'Next.png' )
  if 83 - 83: ii + oO0o * IIIi . o0o00Oo0O
  if 13 - 13: I11i
def IIi1ii ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<meta itemprop="name" content="([^"]*)".+?<meta itemprop="thumbnailUrl" content="([^"]*)".+?<meta itemprop="embedUrl" content="([^"]*)".+?<meta itemprop="description" content="([^"]*)" />' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , iI1I , url , Oo0 in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iI1I )
 for url in Iiiii1i :
  Ii1i1i ( ( url ) . replace ( '//' , 'http://' ) )
  if 83 - 83: oO0o0OOOO - Ii1I * IIIi
def Ii1i1i ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<link rel="canonical" href="([^"]*)">  <link rel="stylesheet"' ) . findall ( o0ooo0 )
 for url in i1I1i :
  IIOOO0O00O0OOOO ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1I1 + 'documentary.png' )
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
def OO0OooOo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , iI1I )
 for url in Iiiii1i :
  II11IiIi11 ( 'NEXT' , url , 8048 , i11i1I1 + 'Next.png' )
def ii111iI1i1 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o0ooo0 )
 for url in i1I1i :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in Iiiii1i :
  if 'rtd' in url :
   OO000 ( url )
   if 31 - 31: oO0o * o0o00Oo0O / oO0o0OOOO . ii * oO0o0OOOO . Ii1I
def OO000 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( o0ooo0 )
 for ooOooo000oOO , file in i1I1i :
  url = ( 'https://rtd.rt.com' + ooOooo000oOO + file )
  oO000o ( url )
  if 50 - 50: oO0o * oO0o0OOOO - I11i + ooo0oo0o0oo * oO0o % IIIi
  if 92 - 92: oO0o0OOOO % ooOoO0O00 % OO0 % ooo0oo0o0oo % I11i
def O00Ooo0O0OOOo ( ) :
 IIi1i11111 = oOOOoo00 ( 'http://www.stream2watch.co/live-tv' )
 i1I1i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I , Iii1IIII11I , o0oooo0O in i1I1i :
  II11IiIi11 ( ( Iii1IIII11I + '[COLOR' + iIii1 + ']' + o0oooo0O + '[/COLOR]' ) , IiI111111IIII , 8086 , iI1I )
  if 22 - 22: IIIi * IIIIi1i
def iIIIiIi1i ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 8087 , iI1I )
  if 36 - 36: OOooOOo
def IiIIIiI ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  II1iI1iiiI ( url , Iii1IIII11I )
  if 75 - 75: ii . O0OoO + oO0o / O0O0OoOO0 - oOo0O0Ooo % O0O0OoOO0
def II1iI1iiiI ( url , name ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIi1i11111 )
 for url in i1I1i :
  print url
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 89 - 89: IIIIi1i * iI11I1II1I1I + Ii . ii
def O0O0 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1I1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IiI111111IIII , 3002 , 'http://www.solie.org/alibrary/' + iI1I )
def oO0oo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iI1I )
def o00o0o000Oo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 Oooo00OOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( o0ooo0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , i11i1I1 + 'classicmovies.png' )
 for url , Iii1IIII11I in Oooo00OOo :
  II11IiIi11 ( '[COLOR' + iIii1 + ']Season- ' + Iii1IIII11I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i11i1I1 + 'classicmovies.png' )
 for url in next :
  II11IiIi11 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i11i1I1 + 'Next.png' )
 for url , iI1I , Iii1IIII11I in Iiiii1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iI1I )
def iIiII ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( o0ooo0 )
 for url in i1I1i :
  OooOO ( url )
def OooOO ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( o0ooo0 )
 for url in i1I1i :
  oO000o ( url )
  if 32 - 32: Ii
def II1iIiiiI1 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiI111111IIII , 8065 , i11i1I1 + 'classicmovies.png' )
def I1IIIi ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( "v.src = '([^']*)';" ) . findall ( o0ooo0 )
 for url in i1I1i :
  O00 ( url )
  if 39 - 39: oO0o0OOOO . Ii1I . O0OoO * oO0o0OOOO / o0o00Oo0O * I11i
def Ii1iiIi11111I ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiI111111IIII , 8065 , i11i1I1 + 'classictv.png' )
def OOOOoO ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  if 'mp4' in url :
   oO000o ( url )
 for url in Iiiii1i :
  yt . PlayVideo ( url )
  if 80 - 80: I1ii11iIi11i % ooo0oo0o0oo % ii * I1ii11iIi11i % O0O0OoOO0
def iii1 ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1I1i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IiI111111IIII , 8071 , i11i1I1 + 'streams.png' )
def O0Ooo0O ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , url in i1I1i :
  if '(Free Access)' in Iii1IIII11I :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1iiIII111ii ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0OoO000O0OO + '/' + iiI1IiI + url ) . strip ( )
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , i11i1I1 + 'streams.png' )
def iii1oOo0OoOOOo0 ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , Iii1IIII11I , url in i1I1i :
  url = ( ( i1iiIII111ii ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0OoO000O0OO + '/' + iiI1IiI + url ) . strip ( )
  i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , iI1I , oO0o0 , '' )
  if 55 - 55: IIIi + o0o00Oo0O / IIIIi1i % OO0 / ii
def O00o0OO0OO0oo ( ) :
 OooOo000o0o ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Genres' , 'http://www.xvideos.com' , 10106 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Search' , '' , 10107 , i11i1I1 + 'Jizbox.png' , '' , '' , )
 if 59 - 59: ii % oO0o0OOOO / iii1iiii1 + ii . ii
def o0OoooO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 ooOO0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in ooOO0 :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i11i1I1 + 'Jizbox.png' , '' , '' )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iII1ii1 in i1I1i :
  OooOo000o0o ( ( Iii1IIII11I + ' - No of Videos : ' + ( iII1ii1 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
  if 81 - 81: Ii + O0O0OoOO0 % Ii - ooOoO0O00
def ii11i1I1i ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 ooOO0 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in ooOO0 :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , i11i1I1 + 'Next.png' , '' , '' )
 i1I1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , url , Iii1IIII11I , Iiiii1I in i1I1i :
  OooOo000o0o ( Iii1IIII11I + '--' + Iiiii1I , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iI1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 13 - 13: IIiIiII11i . IIIIi1i - iii1iiii1 . oO0o . iI11I1II1I1I
  if 66 - 66: I1ii11iIi11i * ooo0oo0o0oo
def ooo0I11 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , url , Iii1IIII11I , iIi11iiIiI1I , OOO0I1Ii1 in i1I1i :
  OooOo000o0o ( Iii1IIII11I + ' - Porn Quality : ' + OOO0I1Ii1 + ' - ' + iIi11iiIiI1I , 'http://www.xvideos.com' + url , 10108 , iI1I , iI1I , OOO0I1Ii1 + ' - ' + iIi11iiIiI1I )
 O0oo0oOoO00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1i11111 )
 for url in O0oo0oOoO00 :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Next.png' , '' , '' )
  if 48 - 48: Ii1I
def o0oi1I1I1I ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1ii1II1ii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 ooOO0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in ooOO0 :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , i11i1I1 + 'Next.png' , '' , '' )
 i1I1i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1ii1II1ii ) )
 for url , Iii1IIII11I in i1I1i :
  OooOo000o0o ( Iii1IIII11I , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
  if 25 - 25: I11i + IIIIi1i - I1ii11iIi11i
  if 59 - 59: O0OoO - oO0o0OOOO % ooOoO0O00
def IIOO ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ooo000o0oo0 = ( i11IIIiI11 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIi1IIIi = Ooo000o0oo0 . lower ( )
 o0O0I1I1Iiii1 = 'http://www.xvideos.com/?k=' + IIi1IIIi
 print o0O0I1I1Iiii1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi1i11111 = O000OOo00oo ( o0O0I1I1Iiii1 )
 i1I1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , IiI111111IIII , Iii1IIII11I , iIi11iiIiI1I , OOO0I1Ii1 in i1I1i :
  OooOo000o0o ( Iii1IIII11I + ' - Porn Quality : ' + OOO0I1Ii1 + ' - ' + iIi11iiIiI1I , 'http://www.xvideos.com' + IiI111111IIII , 10108 , iI1I , iI1I , OOO0I1Ii1 + ' - ' + iIi11iiIiI1I )
 O0oo0oOoO00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in O0oo0oOoO00 :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IiI111111IIII , 10105 , i11i1I1 + 'Next.png' , '' , '' )
  if 71 - 71: OO0 . oO0o0OOOO + O0OoO
def IiIiiI1ii111 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIi1i11111 )
 II1III1i1iiI = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIi1i11111 )
 for url in i1I1i :
  if 'http' in url :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']LOW[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
 for url in Iiiii1i :
  if 'http' in url :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']HIGH[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
 for url in II1III1i1iiI :
  if 'http' in url :
   IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']HLS[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
   if 30 - 30: O0O0OoOO0 + IIiIiII11i % ii
def oOo000O00O0 ( url ) :
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 import urlresolver
 try : O0O00OooO . play ( url )
 except : pass
 if 32 - 32: ii % IIIi % iI11I1II1I1I / o0o00Oo0O
 if 61 - 61: IIiIiII11i . o0o00Oo0O - O0O0OoOO0 - Ii1I / Ii - IIiIiII11i
def O0oo0oOo ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 8091 , i11i1I1 + 'gofish.png' )
def i111iI1i1iI ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1092 , iI1I )
 for url in next :
  II11IiIi11 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 8091 , i11i1I1 + 'Next.png' )
def IiiI1i111I1i ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 8092 , iI1I )
 for url in next :
  II11IiIi11 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 8091 , i11i1I1 + 'Next.png' )
def OO0O0OO0O0 ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( "videoId: '([^']*)'," ) . findall ( IIi1i11111 )
 for url in i1I1i :
  yt . PlayVideo ( url )
  if 78 - 78: IIIi / ii . IIIi
  if 50 - 50: ooo0oo0o0oo . OO0 - o0o00Oo0O % oOo0O0Ooo . iii1iiii1
  if 17 - 17: o0o00Oo0O + ii
oo0OooO = '{PQ},' ; I11iI1 = '{SC},' ; oOo00OO0o0 = '{XG},' ; IiIiI = '{JP},' ; iI1Ii11 = '{HW},' ; Ooo0IiiiIIi = '{RT},'
def I1IIIiOoOooOo00O ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oo0O0oOOO0o = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 70 - 70: I1ii11iIi11i % O0O0OoOO0 . Ii1I
 Oo0o0000OOoO = ( i1iiIII111ii ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 Ii1111iiI = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 I1I = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0oO0oo = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ooOO00Oo = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + i11IIIiI11
 oO00OOOOOO0o = ( i1iiIII111ii ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIII = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 OoO0000 = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 III11iIIi = ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 29 - 29: OOooOOo / ii + OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 13 - 13: oO0o * oO0o0OOOO % Ii % ooOoO0O00 + ooo0oo0o0oo / IIiIiII11i
 if 84 - 84: ooOoO0O00 + oO0o * ii . IIIIi1i + IIIIi1i
 I1ii11iI = O0Oo000ooO00 ( Oo0o0000OOoO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 IIi1i = O0Oo000ooO00 ( Ii1111iiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 o0o0oO00OoO0o = O0Oo000ooO00 ( I1I )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 Oo0OO00 = O0Oo000ooO00 ( ooOO00Oo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o0ooOOOo = O0Oo000ooO00 ( oO00OOOOOO0o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OOoOOo0oO = O0Oo000ooO00 ( iIII )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 I1Ii1IIIiII = O0Oo000ooO00 ( OoO0000 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iiII1IIii1i1 = O0Oo000ooO00 ( III11iIIi )
 if 38 - 38: IIIIi1i * ii
 if 2 - 2: IIIi - Ii
 if IIi1i11111 != 'Failed' :
  i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1i11111 )
  for OOOo00o , Iii1IIII11I in i1I1i :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiI111111IIII + OOOo00o ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 3 - 3: I11i
    if 16 - 16: ooOoO0O00 . ooOoO0O00 / iii1iiii1 % OOooOOo / oOo0O0Ooo * Ii1I
    if 30 - 30: I11i + ii + O0OoO / IIiIiII11i * I1ii11iIi11i
    if 59 - 59: O0O0OoOO0 / OOooOOo * oO0o * IIIIi1i % IIIi
    if 61 - 61: I1ii11iIi11i - o0o00Oo0O - ii
    if 4 - 4: IIiIiII11i - IIIi % I1ii11iIi11i * Ii
    if 18 - 18: I1ii11iIi11i % o0o00Oo0O
 if I1ii11iI != 'Failed' :
  II1III1i1iiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1ii11iI )
  for OOOo00o , Iii1IIII11I in II1III1i1iiI :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Oo0o0000OOoO + OOOo00o ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if IIi1i != 'Failed' :
  oooooO00OOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1i )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in oooooO00OOO :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Silent Hunter[/COLOR]' ) , IiI111111IIII , 222 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 53 - 53: IIiIiII11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if o0o0oO00OoO0o != 'Failed' :
  Oo0O0ooo0O0O = [ ]
  iIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o0oO00OoO0o )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in iIIiI :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    if Iii1IIII11I in Oo0O0ooo0O0O :
     pass
    else :
     iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , IiI111111IIII , 1016 , iII1 , IIIIiii , ooo0O )
     Oo0O0ooo0O0O . append ( Iii1IIII11I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if Oo0OO00 != 'Failed' :
  Oo0O00oOoo00 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Oo0OO00 )
  for IiI111111IIII , iI1I , Iii1IIII11I in Oo0O00oOoo00 :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + IiI111111IIII , 7067 , iI1I )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 28 - 28: Ii1I + IIIi / O0OoO + IIIIi1i + OO0
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if o0ooOOOo != 'Failed' :
  iiiiii1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOOOo )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in iiiiii1Ii :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Redemption[/COLOR]' ) , IiI111111IIII , 222 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 20 - 20: iii1iiii1 + iii1iiii1 * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if OOoOOo0oO != 'Failed' :
  OooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOOo0oO )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in OooOo :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Reaper[/COLOR]' ) , IiI111111IIII , 222 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 87 - 87: OO0 * oO0o + I11i . O0OoO - OO0
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if I1Ii1IIIiII != 'Failed' :
  IiiiO0oo0ooo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1Ii1IIIiII )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in IiiiO0oo0ooo0 :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Herovision[/COLOR]' ) , IiI111111IIII , 222 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 19 - 19: ooOoO0O00
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: O0O0OoOO0 * OOooOOo / I11i . iii1iiii1
 if iiII1IIii1i1 != 'Failed' :
  i1I1iiii1Ii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiII1IIii1i1 )
  for IiI111111IIII , iII1 , Iii1IIII11I in i1I1iiii1Ii11 :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Silent Hunter[/COLOR]' ) , IiI111111IIII , 222 , iII1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 25 - 25: Ii / OOooOOo - iii1iiii1 / oO0o . I11i . I11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 Oo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 6 - 6: IIIi . oO0o0OOOO
 for I1ii1I1Ii in Oo :
  IiI = oo0OooOOo0 + I1ii1I1Ii + iIi1ii1I1
  iIIII1 = O0Oo000ooO00 ( IiI )
  if iIIII1 != 'Failed' :
   Oooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII1 )
   for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in Oooo :
    if i11IIIiI11 in Iii1IIII11I . lower ( ) :
     i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source Pandoras[/COLOR]' , IiI111111IIII , 222 , iII1 , IIIIiii , ooo0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 7 - 7: ooOoO0O00
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: iI11I1II1I1I + ooo0oo0o0oo % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
 Oo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 60 - 60: I11i . OOooOOo % iii1iiii1 / oOo0O0Ooo / o0o00Oo0O
 if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / O0OoO . Ii1I * OO0
 for I1ii1I1Ii in Oo :
  IiI = oo0O0oOOO0o + I1ii1I1Ii
  oo0O = O0Oo000ooO00 ( IiI )
  if oo0O != 'Failed' :
   Ooooo0O0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O )
   for OOOo00o , Iii1IIII11I in Ooooo0O0 :
    if i11IIIiI11 in Iii1IIII11I . lower ( ) :
     IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oo0O0oOOO0o + I1ii1I1Ii + OOOo00o ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 99 - 99: I1ii11iIi11i + Ii
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
     if 36 - 36: O0O0OoOO0 * iii1iiii1 * iI11I1II1I1I - oO0o0OOOO % Ii
     if 98 - 98: iI11I1II1I1I - ooOoO0O00 + OO0 % oO0o0OOOO + OO0 / IIIi
def O0O0Oo00OO ( ) :
 if 100 - 100: I11i . oOo0O0Ooo
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 if 62 - 62: OO0 + IIiIiII11i % OO0
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( i11IIIiI11 ) . replace ( ' ' , '%20' )
 iiI1IIIi = ( i1iiIII111ii ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 Oo0o0000OOoO = ( i1iiIII111ii ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 Ii1111iiI = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 I1I = ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIi1IIIi ) . replace ( ' ' , '+' )
 o0oO0oo = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 ooOO00Oo = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oO00OOOOOO0o = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 50 - 50: ii + IIIi * oOo0O0Ooo - O0O0OoOO0 / Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 5 - 5: o0o00Oo0O - oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ooOO00O00oo = O0Oo000ooO00 ( iiI1IIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 I1ii11iI = O0Oo000ooO00 ( Oo0o0000OOoO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IIi1i = O0Oo000ooO00 ( Ii1111iiI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0o0oO00OoO0o = cloudflare . source ( I1I )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oo0O = O0Oo000ooO00 ( o0oO0oo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 Oo0OO00 = O0Oo000ooO00 ( ooOO00Oo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 o0ooOOOo = O0Oo000ooO00 ( oO00OOOOOO0o )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 44 - 44: IIiIiII11i . IIiIiII11i + O0OoO * O0O0OoOO0
 if o0ooOOOo != 'Failed' :
  iiiiii1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOOOo )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in iiiiii1Ii :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source HeroVision[/COLOR]' ) , IiI111111IIII , 1016 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 16 - 16: IIiIiII11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 100 - 100: o0o00Oo0O - ooOoO0O00
 if Oo0OO00 != 'Failed' :
  Oo0O00oOoo00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0OO00 )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in Oo0O00oOoo00 :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Reaper[/COLOR]' ) , IiI111111IIII , 1016 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 48 - 48: IIIi % OO0 + o0o00Oo0O
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 27 - 27: Ii1I / O0OoO
    if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
    if 63 - 63: ooo0oo0o0oo + iI11I1II1I1I + oOo0O0Ooo + iii1iiii1
    if 72 - 72: oO0o + Ii + Ii1I
    if 96 - 96: IIIi % ooOoO0O00 / I11i
    if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + IIIIi1i
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 88 - 88: o0o00Oo0O . IIIi % oOo0O0Ooo
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if IIi1i11111 != 'Failed' :
  i1I1i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIi1i11111 )
  for iI1I , IiI111111IIII , Iii1IIII11I in i1I1i :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + IiI111111IIII , 10044 , iI1I , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 10 - 10: oOo0O0Ooo + o0o00Oo0O
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: o0o00Oo0O % iI11I1II1I1I / OOooOOo % O0OoO / ooo0oo0o0oo
    if 31 - 31: Ii * OOooOOo
    if 69 - 69: Ii
    if 61 - 61: o0o00Oo0O
    if 21 - 21: oO0o % iI11I1II1I1I . oO0o
    if 99 - 99: I11i * O0OoO % IIIi * IIIi + ii
    if 82 - 82: oO0o0OOOO / OOooOOo - O0OoO / OO0
    if 50 - 50: O0OoO + oO0o . Ii + Ii1I + Ii
    if 31 - 31: IIIi * iii1iiii1 . OOooOOo * oO0o0OOOO
    if 28 - 28: ooo0oo0o0oo + oOo0O0Ooo - I1ii11iIi11i % O0OoO . oO0o0OOOO + oOo0O0Ooo
 if ooOO00O00oo != 'Failed' :
  Iiiii1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO00O00oo )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in Iiiii1i :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , IiI111111IIII , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 72 - 72: O0O0OoOO0 / I1ii11iIi11i / IIIi * OOooOOo + O0OoO
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if I1ii11iI != 'Failed' :
  II1III1i1iiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1ii11iI )
  for Iii1IIII11I in II1III1i1iiI :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Oo0o0000OOoO + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - ooo0oo0o0oo . ii
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if IIi1i != 'Failed' :
  oooooO00OOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i )
  for Iii1IIII11I in oooooO00OOO :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1111iiI + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 10 - 10: iii1iiii1
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if o0o0oO00OoO0o != 'Failed' :
  iIIiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0o0oO00OoO0o )
  for IiI111111IIII , iI1I , Iii1IIII11I in iIIiI :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source - Dizi[/COLOR]' , IiI111111IIII , 8062 , iI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 48 - 48: IIIIi1i * ooOoO0O00 % ii * O0O0OoOO0 * oO0o
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if oo0O != 'Failed' :
  Ooooo0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O )
  for IiI111111IIII , iII1 , ooo0O , IIIIiii , Iii1IIII11I in Ooooo0O0 :
   if IIi1IIIi in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- Source Scooby[/COLOR]' ) , IiI111111IIII , 1016 , iII1 , IIIIiii , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 7 - 7: IIIIi1i . O0O0OoOO0 . IIIIi1i - iii1iiii1
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: OO0 + ii - oO0o / ooOoO0O00 / ii
 OOO0IIIIii11II1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if oo0O != 'Failed' :
  for I1ii1I1Ii in OOO0IIIIii11II1I :
   IiI = oo0OooOOo0 + I1ii1I1Ii + iIi1ii1I1
   I1Ii1IIIiII = O000OOo00oo ( IiI )
   if I1Ii1IIIiII != 'Failed' :
    IiiiO0oo0ooo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1Ii1IIIiII )
    for Iii1IIII11I , ooo0O , IiI111111IIII , iI1I , oO0o0 , iI1i1IiIIIIi in IiiiO0oo0ooo0 :
     if IIi1IIIi in Iii1IIII11I . lower ( ) :
      iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source Pandoras[/COLOR]' , IiI111111IIII , iI1i1IiIIIIi , iI1I , oO0o0 , ooo0O )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 48 - 48: Ii1I - o0o00Oo0O . oO0o
      oOooOo0 ( 'tvshows' , 'Media Info 3' )
      if 38 - 38: o0o00Oo0O
      if 79 - 79: ooOoO0O00 . IIIi
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1i1i11iI11II ( ) :
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / O0O0OoOO0
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1i11111 = O000OOo00oo ( IiI111111IIII )
 i1I1i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , iI1I , I1I1ii1111 in i1I1i :
  IIIiI1iiiIIIi = i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  if i11IIIiI11 in Iii1IIII11I . lower ( ) :
   II11IiIi11 ( Iii1IIII11I , '' , 7022 , IIIiI1iiiIIIi )
   if 85 - 85: o0o00Oo0O . IIIIi1i % ooo0oo0o0oo - oO0o0OOOO % o0o00Oo0O - O0O0OoOO0
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
ooO00Oo = '{ZH},' ; iIi1 = '{IX},' ; O0o00ooo = '{LM},'
if 5 - 5: ooOoO0O00 - IIIi / OOooOOo
def iII1I ( url ) :
 o00oOOo0Oo = cloudflare . source ( url )
 i1I1i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( o00oOOo0Oo )
 for url , O0OooOO , o0o0oOoOO0O , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( O0OooOO ) . replace ( 'Sezon' , ' Season ' ) + ( o0o0oOoOO0O ) . replace ( 'Bölüm' , ' Episode ' ) + Iii1IIII11I , url , 8063 , '' )
  if 91 - 91: IIiIiII11i - iI11I1II1I1I / ooOoO0O00 * ooOoO0O00 % I1ii11iIi11i
  if 82 - 82: OO0
  if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / IIIIi1i
  if 9 - 9: OOooOOo - ooo0oo0o0oo
def iiIi ( url ) :
 o00oOOo0Oo = cloudflare . source ( url )
 i1I1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o00oOOo0Oo )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , url , 222 , '' )
  if 31 - 31: Ii + ooo0oo0o0oo - iii1iiii1 * IIIIi1i
  if 60 - 60: IIIIi1i + oO0o + oO0o0OOOO % iI11I1II1I1I . I1ii11iIi11i
  if 73 - 73: iii1iiii1 * Ii1I + I11i - I1ii11iIi11i . oO0o0OOOO
  if 93 - 93: Ii
def OoOiII11IiIi ( ) :
 if 27 - 27: oO0o + OOooOOo
 o00oOOo0Oo = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1I1i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o00oOOo0Oo )
 for IiI111111IIII , iI1I , Iii1IIII11I , o0o0oOoOO0O in i1I1i :
  II11IiIi11 ( Iii1IIII11I + '  -  ' + ( o0o0oOoOO0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiI111111IIII , 8063 , iI1I )
  if 97 - 97: ooOoO0O00 * iii1iiii1 . IIiIiII11i
def ooooOoOooo00Oo ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I , iI1I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 8002 , iI1I )
def ooo00O0OOo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( o0ooo0 )
 for iI1I , time , url , Iii1IIII11I , Oo0 in i1I1i :
  iiIi1IIi1I ( '%s %s' % ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , time ) , url , 1015 , iI1I , Oo0 )
  if 45 - 45: oOo0O0Ooo / IIIIi1i + IIIi + ooo0oo0o0oo
def iIIII1Iii11 ( ) :
 if 3 - 3: I11i % I11i % oOo0O0Ooo - ooOoO0O00
 II11IiIi11 ( 'Coronation Street' , '' , 8001 , '' )
 II11IiIi11 ( 'Eastenders' , '' , 8002 , '' )
 II11IiIi11 ( 'Emmerdale' , '' , 8003 , '' )
 II11IiIi11 ( 'Hollyoaks' , '' , 8004 , '' )
 II11IiIi11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 84 - 84: oO0o0OOOO
 if 39 - 39: o0o00Oo0O . ooOoO0O00 * Ii1I - oO0o - IIIIi1i % I11i
 if 6 - 6: oO0o - IIIIi1i / IIiIiII11i
 if 25 - 25: I1ii11iIi11i % OOooOOo
def o00OIIIIII1iI1II ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Holly' in Iii1IIII11I :
   iI1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IiI111111IIII :
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 14 - 14: oOo0O0Ooo / o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 43 - 43: IIIi - ooo0oo0o0oo % Ii * IIiIiII11i . iii1iiii1 - oO0o0OOOO
def i11i111 ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'East' in Iii1IIII11I :
   iI1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IiI111111IIII :
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 36 - 36: oO0o0OOOO - ooo0oo0o0oo . ooo0oo0o0oo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Emmer' in Iii1IIII11I :
   iI1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IiI111111IIII :
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 90 - 90: IIIi + oO0o + Ii1I - iii1iiii1
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1I + ooo0oo0o0oo
def Ooooo00 ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Coro' in Iii1IIII11I :
   iI1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IiI111111IIII :
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 99 - 99: Ii1I - IIIi
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: IIiIiII11i . oO0o
def o000Ooo00o00O ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Celeb' in Iii1IIII11I :
   iI1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IiI111111IIII :
    IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 80 - 80: IIIIi1i
def iI1I1ii11IIi1 ( name , url ) :
 OOoOOoOO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OOoOOoOO :
  O0O00 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  o0ooo0 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( o0ooo0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  o0ooo0 = open_url ( url )
  I1iIiiI11 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( o0ooo0 ) [ - 1 ]
  O0O00 = I1iIiiI11 . replace ( '\\/' , '/' )
 I1i11II11i1iI = xbmcgui . ListItem ( name , '' , '' )
 I1i11II11i1iI . setPath ( O0O00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1i11II11i1iI )
 if 27 - 27: IIIIi1i
 if 74 - 74: ooo0oo0o0oo / OO0
def OooOoO ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1I1i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IiI111111IIII , 7071 , i11i1I1 + 'popcorn.png' )
 for IiI111111IIII , Iii1IIII11I in Iiiii1i :
  II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IiI111111IIII , 7071 , i11i1I1 + 'popcorn.png' )
  if 59 - 59: O0OoO + oOo0O0Ooo / IIiIiII11i / OOooOOo
def oOoo00 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1I1i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Movies' in Iii1IIII11I :
   II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( IiI111111IIII ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , i11i1I1 + 'popcorn.png' )
def IIiIi ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o0ooo0 )
 i1I1i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( o0ooo0 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iI1I )
 for url in Iiiii1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , i11i1I1 + 'Next.png' )
  if 12 - 12: O0O0OoOO0 % IIIIi1i + oO0o + IIiIiII11i / I11i
  if 89 - 89: O0O0OoOO0 . oOo0O0Ooo / oO0o + iii1iiii1 + IIiIiII11i
def ooOOooO0OoO ( url ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1I1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , url , iI1I in i1I1i :
  if '{{' in Iii1IIII11I :
   pass
  else :
   II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iI1I )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
Ii111IIIIii = '{UJ},' ; O00oIii1iIIiii1ii = '{WE},' ; Ii1iii11I = '{WP},' ; Ii11iIiiI = '{PP},'
def iiII ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o0ooo0 )
 for Iii1IIII11I , url , iI1I in i1I1i :
  if '{{' in Iii1IIII11I :
   pass
  else :
   II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iI1I )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII1IiiIIIIii ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  oOOO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOO ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: o0o00Oo0O * ooo0oo0o0oo / ooOoO0O00 + IIIi . OOooOOo
 if 73 - 73: O0O0OoOO0 / oOo0O0Ooo / ii + oOo0O0Ooo
 if 57 - 57: O0OoO . O0O0OoOO0 % I11i
def I1I11 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if '(cooltvseries.com)' in Iii1IIII11I :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i11i1I1 + 'CoolSeries.png' )
 for url , Iii1IIII11I in Iiiii1i :
  if '(cooltvseries.com)' in Iii1IIII11I :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i11i1I1 + 'CoolSeries.png' )
def iI1i1iI1iI ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( o0ooo0 )
 for url in i1I1i :
  oO000o ( ( url ) . replace ( ' ' , '%20' ) )
I1IIiIi = '{XX},' ; OOOOoOoO = '{UD},' ; OO000o0oOoo0o = '{YT},' ; IiiIiIIi = '{JS},' ; O00Oo = '{PF},'
if 63 - 63: I11i / o0o00Oo0O - ii
def oo0O0 ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1I1i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I , iI1I in i1I1i :
  IIOOO0O00O0OOOO ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1iiIII111ii ( IiI111111IIII ) ) , 222 , iI1I )
  if 34 - 34: IIiIiII11i - ooo0oo0o0oo % OOooOOo % O0O0OoOO0 / OO0
def Ii1II ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( o0ooo0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( o0ooo0 )
 for iI1I , url , Iii1IIII11I in i1I1i :
  if 'youtu' in url :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iI1I )
 for url in next :
  II11IiIi11 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 7050 , i11i1I1 + 'Next.png' )
  if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
def I1111111 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 57 - 57: O0OoO % oO0o - oOo0O0Ooo
def i11iI11 ( url ) :
 o0ooo0 = O000OOo00oo
 i1I1i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , iI1I )
  if 39 - 39: Ii % oO0o
  if 53 - 53: oOo0O0Ooo
  if 10 - 10: iii1iiii1 / Ii - IIiIiII11i
  if 48 - 48: O0OoO
  if 26 - 26: IIIIi1i * iii1iiii1 * IIIi * OOooOOo
def I1ii1i11iI1 ( ) :
 if 6 - 6: o0o00Oo0O . OO0 - IIIi / Ii
 II11IiIi11 ( 'All Channels' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Entertainment' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Movies' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Music' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'News' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Sports' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Documentary' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Kids' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Food' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Religious' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'USA Channels' , '' , 7021 , i11i1I1 + 'livetv.png' )
 II11IiIi11 ( 'Other' , '' , 7021 , i11i1I1 + 'livetv.png' )
 if 84 - 84: oO0o0OOOO / Ii1I * I11i * oO0o * O0OoO * o0o00Oo0O
 if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ooi1IIii1i ( Cat_Name ) :
 if 60 - 60: O0O0OoOO0 % I1ii11iIi11i / oO0o0OOOO . IIIIi1i / iii1iiii1 - ii
 o0iii1i = False
 IIIIIIi1IIi1I11i = '0'
 if Cat_Name == 'All Channels' : o0iii1i = True
 if Cat_Name == 'Entertainment' : IIIIIIi1IIi1I11i = '1'
 if Cat_Name == 'Movies' : IIIIIIi1IIi1I11i = '2'
 if Cat_Name == 'Music' : IIIIIIi1IIi1I11i = '3'
 if Cat_Name == 'News' : IIIIIIi1IIi1I11i = '4'
 if Cat_Name == 'Sports' : IIIIIIi1IIi1I11i = '5'
 if Cat_Name == 'Documentary' : IIIIIIi1IIi1I11i = '6'
 if Cat_Name == 'Kids' : IIIIIIi1IIi1I11i = '7'
 if Cat_Name == 'Food' : IIIIIIi1IIi1I11i = '8'
 if Cat_Name == 'Religious' : IIIIIIi1IIi1I11i = '9'
 if Cat_Name == 'USA Channels' : IIIIIIi1IIi1I11i = '10'
 if Cat_Name == 'Other' : IIIIIIi1IIi1I11i = '11'
 if 70 - 70: O0O0OoOO0 % O0O0OoOO0 . OOooOOo / Ii
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1I1i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o0ooo0 )
 print 'Len Match: >>>' + str ( len ( i1I1i ) )
 for Iii1IIII11I , iI1I , I1I1ii1111 in i1I1i :
  IIIiI1iiiIIIi = i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  if I1I1ii1111 == IIIIIIi1IIi1I11i :
   II11IiIi11 ( Iii1IIII11I , '' , 7022 , IIIiI1iiiIIIi )
  elif o0iii1i == True :
   II11IiIi11 ( Iii1IIII11I , '' , 7022 , IIIiI1iiiIIIi )
  else : pass
  if 12 - 12: iI11I1II1I1I / I1ii11iIi11i - Ii1I + Ii
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 71 - 71: Ii * oOo0O0Ooo + iI11I1II1I1I - iii1iiii1
def ii1Io0oOO0 ( Search_Name ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1I1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o0ooo0 )
 i1I1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o0ooo0 )
 for iI1I , IiI111111IIII , iiI1IIIi , Oo0o0000OOoO in i1I1i :
  IIIiI1iiiIIIi = i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  IIOOO0O00O0OOOO ( Search_Name + ': Link 1' , ( IiI111111IIII ) . replace ( '\\' , '' ) , 222 , IIIiI1iiiIIIi )
  IIOOO0O00O0OOOO ( Search_Name + ': Link 2' , ( iiI1IIIi ) . replace ( '\\' , '' ) , 222 , IIIiI1iiiIIIi )
  IIOOO0O00O0OOOO ( Search_Name + ': Link 3' , ( Oo0o0000OOoO ) . replace ( '\\' , '' ) , 222 , IIIiI1iiiIIIi )
  if 31 - 31: O0O0OoOO0 * I11i * O0O0OoOO0 + oO0o * I11i . iii1iiii1
def Oo00oo00o00Oo ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , i11i1I1 + 'english.png' )
def iiiiiii11III ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , i11i1I1 + 'xxx.png' )
def I11111ii1i ( ) :
 o0ooo0 = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( o0ooo0 )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , i11i1I1 + 'vod(1).png' )
  if 78 - 78: oO0o0OOOO % I1ii11iIi11i + OOooOOo . Ii1I % IIIi / O0O0OoOO0
def iI11IiiiIII ( url ) :
 url
 OOOo00 = xbmcgui . ListItem ( Iii1IIII11I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOo00 )
 return
 if 43 - 43: IIIIi1i + Ii
 if 96 - 96: O0OoO . OOooOOo * o0o00Oo0O
def o0ooOOOO0O0o ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( o0ooo0 )
 for url , ooo0O , iI1I , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iI1I , '' , ( ooo0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oOooOo0 ( 'tvshows' , 'Media Info 3' )
 for url in Iiiii1i :
  II11IiIi11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , i11i1I1 + 'Next.png' )
  if 26 - 26: IIIIi1i - I1ii11iIi11i + oOo0O0Ooo + I11i
def III1iI1Ii11Ii ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , ooo0O , iI1I in i1I1i :
  i1I1iI1iIi111i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iI1I , '' , ooo0O )
  oOooOo0 ( 'tvshows' , 'Media Info 3' )
 Ii1iiII1i = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI11iIi in Ii1iiII1i :
  OOoo = ( iI11iIi ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiIi1IIi1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iI1I , '' , OOoo )
  if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . oO0o0OOOO
def o00o0 ( INFO ) :
 ii1I ( 'info for workout' , INFO )
 if 84 - 84: OOooOOo - I1ii11iIi11i . OO0 . ooo0oo0o0oo - I1ii11iIi11i
 if 99 - 99: iii1iiii1
 if 75 - 75: OO0 . O0OoO / ooo0oo0o0oo
def oooIi1II1I11i1I ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'cat-item-.+?"><a href="([^"]*)" >(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , url , 9031 , i11i1I1 + 'icon.png' )
def OOoOo ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , url , 9032 , i11i1I1 + 'icon.png' )
def Iiiiiii11IIiI ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( o0ooo0 )
 for Iii1IIII11I , url in i1I1i :
  if '://' in Iii1IIII11I :
   pass
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , i11i1I1 + 'icon.png' )
def oOOO0o ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( o0ooo0 )
 for Iii1IIII11I , url in i1I1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , url , 222 , i11i1I1 + 'icon.png' )
  if 70 - 70: Ii / OO0 * Ii1I - ooOoO0O00 + OO0
  if 37 - 37: O0OoO / Ii
  if 63 - 63: oO0o + OO0
def IIi1iI1i ( ) :
 o0ooo0 = O000OOo00oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1I1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'category' in IiI111111IIII :
   II11IiIi11 ( Iii1IIII11I , 'http://www.disclose.tv/' + IiI111111IIII , 7010 , i11i1I1 + 'disclose.png' )
   if 22 - 22: ii - O0O0OoOO0 . oO0o % O0O0OoOO0 + Ii1I + oOo0O0Ooo
   if 37 - 37: ooo0oo0o0oo
def OOO0O ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( o0ooo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I , iI1I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , 'http://www.disclose.tv/' + url , 7011 , iI1I )
 for url in next :
  II11IiIi11 ( 'NEXT' , url , 7010 , i11i1I1 + 'Next.png' )
  if 47 - 47: iii1iiii1 + IIiIiII11i / oOo0O0Ooo - ii + iii1iiii1
  if 39 - 39: oO0o * IIIi - IIIi . OO0
def OooOOoO00OO00 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( o0ooo0 )
 II1III1i1iiI = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  if 'http' in url :
   IIOOO0O00O0OOOO ( 'video/flv' , url , 222 , i11i1I1 + 'disclose.png' )
 for url , Iii1IIII11I in Iiiii1i :
  IIOOO0O00O0OOOO ( Iii1IIII11I , url , 222 , i11i1I1 + 'disclose.png' )
 for url in II1III1i1iiI :
  IIOOO0O00O0OOOO ( 'YT Link' , url , 8043 , i11i1I1 + 'disclose.png' )
  if 17 - 17: ii * iii1iiii1 * oOo0O0Ooo
  if 30 - 30: OOooOOo / IIIi / O0O0OoOO0 * I11i * IIIi . oOo0O0Ooo
def o0oo000 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , i11i1I1 + 'icon.png' )
  if 87 - 87: oO0o
def I1Io0oO00O ( name , url , img ) :
 IIi1i11111 = O000OOo00oo ( url )
 OOooo00oo = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIi1i11111 )
 i1iiIi1IiiiI = len ( OOooo00oo )
 if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 if 95 - 95: IIIi
 if i1iiIi1IiiiI == 1 :
  for i11ii in OOooo00oo :
   i11ii = i11ii . replace ( 'player' , 'watch' )
   IiI111I = i11ii + '&fv=&sou='
   oo0oO0 = O000OOo00oo ( IiI111I )
   ii1i1Iii = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( oo0oO0 )
   for oO0o0oOo in ii1i1Iii :
    IIII11111Ii = False
    Resolve ( oO0o0oOo )
    if 21 - 21: o0o00Oo0O + o0o00Oo0O / I11i - oO0o0OOOO
 elif i1iiIi1IiiiI > 1 :
  if 88 - 88: Ii1I . IIiIiII11i / O0OoO % ooOoO0O00 - OOooOOo % Ii
  for i11ii in OOooo00oo :
   Oo0IiiIIII1 = O000OOo00oo ( i11ii )
   IiiioOO0o00 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo0IiiIIII1 )
   IIi1IIiII = IiiioOO0o00
   IIi1IIiII = ( str ( IIi1IIiII ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIi1IIiII
   IIOOO0O00O0OOOO ( 'DOUBLE LINK' , IIi1IIiII , 424 , '' )
   if 96 - 96: ooOoO0O00 * IIiIiII11i
   for url in IiiioOO0o00 :
    II11IiIi11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iiI1IIIi = Google . resolve ( url )
    except :
     pass
    try :
     o00Oo0O = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iiI1IIIi ) )
     for ii1IIIi , OOoO in o00Oo0O :
      if 11 - 11: Ii1I - ii
      HD_URLS . append ( ii1IIIi )
      SD_URLS . append ( OOoO )
    except :
     pass
 else :
  pass
  if 16 - 16: ooo0oo0o0oo % ii - OO0 * O0O0OoOO0 - O0O0OoOO0
def I1iiII1 ( ) :
 if 45 - 45: oO0o + oO0o % OO0
 if 36 - 36: O0O0OoOO0 * oO0o0OOOO . oO0o0OOOO / I1ii11iIi11i / oOo0O0Ooo
 II11IiIi11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , i11i1I1 + 'Movies.png' )
 if 80 - 80: ii - ooOoO0O00
 II11IiIi11 ( 'Search Movies' , '' , 7017 , i11i1I1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 51 - 51: ooOoO0O00 . OOooOOo / OOooOOo % Ii * O0OoO - iii1iiii1
 if 49 - 49: I1ii11iIi11i - iI11I1II1I1I
def o0oo0o ( ) :
 o0ooo0 = O000OOo00oo ( 'http://cnfstudio.com/' )
 i1I1i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , 'http://cnfstudio.com/genre/' + IiI111111IIII , 7003 , i11i1I1 + 'icon.png' )
  if 78 - 78: ii . ii / o0o00Oo0O
oooOOOOO = xbmcgui . Dialog ( )
if 25 - 25: IIiIiII11i % IIiIiII11i - O0O0OoOO0 . o0o00Oo0O
O00O0 = '{UN},' ; ii11i1i = '{IG},' ; iIiI1I = '{PL},' ; iIOOO0O00 = '{LO},' ; Oo0O000OoO00 = '{LP},' ; oOO00OoOo = '{HA},' ; oOoo = '{XD},' ; oO0OO00 = '{TA},' ; IiiI = '{DP},' ; O0oooooO = '{JT},' ; IIi1 = '{JJ},' ; II11II = '{MM},' ; i1ii11 = '{FQ},' ; III = '{HH},'
if 75 - 75: OO0 / O0O0OoOO0
def iIioO00O0o0oOOO ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0ooo0 )
 ooooOoo00 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( o0ooo0 )
 for iI1I , url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iI1I )
 ooooOoo00 = ooooOoo00
 for url in ooooOoo00 :
  II11IiIi11 ( 'Next Page' , url , 7003 , i11i1I1 + 'Next.png' )
  if 7 - 7: O0OoO * oO0o + ii . OO0 * oO0o0OOOO
def oooOoO0oo0o0 ( url ) :
 if 4 - 4: Ii * Ii1I + ii - ooo0oo0o0oo . OO0 . iI11I1II1I1I
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  ooOooo000oOO = url + '&fv=&sou='
  ooOooo000oOO = ooOooo000oOO . replace ( 'player' , 'watch' )
  IIiIIiI1iIII = o0ooo0oooO ( ooOooo000oOO )
  ooOo = o0ooo0oooO ( url )
  if 98 - 98: Ii1I - O0O0OoOO0 * oO0o . Ii1I - iii1iiii1
  if 4 - 4: Ii + ii / Ii . ii % Ii1I / OOooOOo
def o0ooo0oooO ( url ) :
 if 35 - 35: Ii1I % ooOoO0O00 + I11i - iI11I1II1I1I
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( o0ooo0 )
 for url in i1I1i :
  O00 ( url )
  if 28 - 28: oOo0O0Ooo * IIiIiII11i * OOooOOo % O0OoO - O0OoO
  if 35 - 35: I1ii11iIi11i . OO0 - ooOoO0O00 . OOooOOo
def I1iI1 ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Local M3u[/COLOR]' , OOooO0OOoo , 2001 , i11i1I1 + 'LocalM3U.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Remote M3u[/COLOR]' , iI111I11I1I1 , 7080 , i11i1I1 + 'RemoteM3U.png' , ooOoOoo0O , '' )
 if 9 - 9: I1ii11iIi11i - OO0 * IIIIi1i / Ii / I1ii11iIi11i % IIIi
def I1Ii1IIi ( ) :
 if os . path . exists ( OOooO0OOoo ) :
  I11i1I1i1 = open ( OOooO0OOoo , 'r' )
  for OOOo00 in I11i1I1i1 :
   o00Oo0ooOo0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOOo00 )
   for Iii1IIII11I , IiI111111IIII in o00Oo0ooOo0O :
    IIOOO0O00O0OOOO ( Iii1IIII11I , IiI111111IIII , 222 , i11i1I1 + 'streams.png' )
 else :
  oooOOOOO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: oO0o
def I11i1IIi1i1 ( url ) :
 if os . path . exists ( Remote ) :
  IIi1i11111 = oOOOoo00 ( url )
  i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
  for Iii1IIII11I , url in i1I1i :
   url = ( url ) . strip ( )
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oooOOOOO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 28 - 28: oO0o0OOOO . ii * O0OoO + Ii % oOo0O0Ooo . iI11I1II1I1I
  if 63 - 63: IIiIiII11i - oO0o0OOOO . OOooOOo
def o0O0OOO0Ooo ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1I1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in i1I1i :
  IiI111111IIII = i1iiIII111ii ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IiI111111IIII
 Iii1IIII11I = 'plugin.video.GenieTv'
 if 8 - 8: oOo0O0Ooo * OO0 / ooo0oo0o0oo + OOooOOo . ooo0oo0o0oo - O0OoO
 Oo0O ( IiI111111IIII , Iii1IIII11I )
 if 60 - 60: O0OoO * OO0 * oO0o
def ooOOOoO ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1I1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in i1I1i :
  IiI111111IIII = i1iiIII111ii ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IiI111111IIII
 Iii1IIII11I = 'repository.GenieTv'
 if 64 - 64: oO0o0OOOO / IIiIiII11i / oO0o - OO0 * iI11I1II1I1I . IIIIi1i
 Oo0O ( IiI111111IIII , Iii1IIII11I )
 if 25 - 25: O0OoO - O0O0OoOO0 . oO0o0OOOO
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - OO0 % iI11I1II1I1I - O0O0OoOO0
def III1I11II11I ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']CATAGORIES[/COLOR]' , '' , 10051 , i11i1I1 + 'Catagories.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH[/COLOR]' , '' , 10052 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if 78 - 78: Ii1I . iii1iiii1 . iii1iiii1 . oO0o0OOOO % IIIIi1i
 if 26 - 26: OO0 + oO0o / OOooOOo . IIiIiII11i * O0O0OoOO0
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oooOOOOO = xbmcgui . Dialog ( )
i11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
IiII111I = 'https://addons.tvaddons.ag/'
if 62 - 62: ooOoO0O00 * iI11I1II1I1I % IIIi % OOooOOo / ii
def iI1111iiI1 ( ) :
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 o0O0I1I1Iiii1 = 'https://addons.tvaddons.ag/search/?keyword=' + IIi1IIIi
 IIi1i11111 = O000OOo00oo ( o0O0I1I1Iiii1 )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , oOOO00o000o , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , 10054 , 'https://addons.tvaddons.ag/' + oOOO00o000o , ooOoOoo0O , '' )
  if 71 - 71: I11i % O0OoO + o0o00Oo0O / Ii1I
  if 88 - 88: oO0o0OOOO / I1ii11iIi11i - iii1iiii1
def I1iIi1IiI1i ( ) :
 IIi1i11111 = O000OOo00oo ( IiII111I )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  if 'Repositories' in Iii1IIII11I :
   pass
  elif 'Services' in Iii1IIII11I :
   pass
  elif 'International' in Iii1IIII11I :
   pass
  else :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 10053 , 'https://addons.tvaddons.ag/' + iI1I , ooOoOoo0O , '' )
   if 50 - 50: ooOoO0O00 * IIIi / Ii / Ii / IIIi
   if 84 - 84: Ii1I - IIIIi1i + Ii1I
def Addon ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 O0000oO00oO0o = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIi1i11111 )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  if 'Please' in Iii1IIII11I :
   pass
  else :
   i1I1iI1iIi111i ( Iii1IIII11I , url , 10054 , 'https://addons.tvaddons.ag/' + iI1I , ooOoOoo0O , '' )
 for url in O0000oO00oO0o :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
  if 86 - 86: I11i / OO0 . I11i % oOo0O0Ooo + IIIi % oO0o0OOOO
  if 72 - 72: OO0 - Ii1I + IIIi . OOooOOo
def IIIiI1i ( url , name ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)"' ) . findall ( IIi1i11111 )
 for url in i1I1i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   ooo0 = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
   try :
    os . remove ( ooo0 )
   except :
    pass
   downloader . download ( url , ooo0 , o0oOoO00o )
   i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print i1I
   print '======================================='
   extract . all ( ooo0 , i1I , o0oOoO00o )
   IiIi1I1 ( )
   if 72 - 72: oO0o0OOOO * OOooOOo % iii1iiii1 % OO0
def Oo0O ( url , name ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ooo0 = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
 try :
  os . remove ( ooo0 )
 except :
  pass
 downloader . download ( url , ooo0 , o0oOoO00o )
 i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print i1I
 print '======================================='
 extract . all ( ooo0 , i1I , o0oOoO00o )
 IiIi1I1 ( )
 if 22 - 22: O0OoO - Ii1I / ooo0oo0o0oo
def IiIi1I1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 95 - 95: I11i
 if 69 - 69: IIIi . oO0o0OOOO
def iII11iI1iiIIi ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , oOOO00o000o , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , url , 1007 , oOOO00o000o )
def I1II1iIi ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , oOOO00o000o , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , oOOO00o000o )
  if 36 - 36: OOooOOo * oO0o / OO0 / oOo0O0Ooo - O0O0OoOO0
  if 53 - 53: IIIi
def oo0OoO ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , iconimage , ooo0O , oO0o0 , name in i1I1i :
  if 'http' in url :
   if '.php' in url :
    Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
    for OOOo00 in Ii11Ii1iI :
     if OOOo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    i1o0oo0Ooooo0 ( name , url , 1016 , iconimage , oO0o0 , ooo0O )
   else :
    if 'youtube' in url :
     Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
     for OOOo00 in Ii11Ii1iI :
      if OOOo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0o0OO0o00o0O ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oO0o0 , ooo0O )
    else :
     Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
     for OOOo00 in Ii11Ii1iI :
      if OOOo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0o0OO0o00o0O ( name , url , 222 , iconimage , oO0o0 , ooo0O )
     oOooOo0 ( 'movies' , 'INFO' )
  else :
   I11iIiiI ( url , iconimage , name )
   if 88 - 88: Ii1I - oO0o0OOOO * ii * IIIIi1i . Ii . I11i
 else :
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
  for url , oOOO00o000o , name in i1I1i :
   if 'http' in url :
    if '.php' in url :
     II11IiIi11 ( name , url , 1016 , oOOO00o000o )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      IIOOO0O00O0OOOO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOO00o000o )
     else :
      Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
      for OOOo00 in Ii11Ii1iI :
       if OOOo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      IIOOO0O00O0OOOO ( name , url , 222 , oOOO00o000o )
      oOooOo0 ( 'movies' , 'INFO' )
   else :
    I11iIiiI ( url , oOOO00o000o , name )
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 96 - 96: oOo0O0Ooo % oOo0O0Ooo / I11i / OOooOOo * OO0 - iii1iiii1
def I11iIiiI ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OOOoOOOo = ( url ) . replace ( iIi1 , 'http' ) . replace ( OOOOoOoO , '.com' ) ;
 oO0000 = ( OOOoOOOo ) . replace ( O0o00ooo , 'a' ) . replace ( oOo00OO0o0 , 'b' ) . replace ( IiIiI , 'c' ) . replace ( O00oIii1iIIiii1ii , 'd' ) . replace ( iIiI1I , 'e' ) . replace ( O0oooooO , 'f' ) ;
 OOOIIIIiiIi = ( oO0000 ) . replace ( I1IIiIi , 'g' ) . replace ( oOO00OoOo , 'h' ) . replace ( OO000o0oOoo0o , 'i' ) . replace ( O00Oo , 'j' ) . replace ( iI1Ii11 , 'k' ) . replace ( Ooo0IiiiIIi , 'l' ) ;
 ooooOOo = ( OOOIIIIiiIi ) . replace ( O0Oo0oO0OO0 , 'm' ) . replace ( oo0o0 , 'n' ) . replace ( OoO00o00 , 'o' ) . replace ( ooOoo0oo00000O , 'p' ) . replace ( oo0 , 'q' ) . replace ( o0Oo00o0 , 'r' ) ;
 i11II = ( ooooOOo ) . replace ( oOOoOo0Ooo , 's' ) . replace ( Ii1iii11I , 't' ) . replace ( o0OOoOoo00 , 'u' ) . replace ( Oo0Ooo0 , 'v' ) . replace ( IiIIiIi11ii , 'w' ) . replace ( II11IiIIiiiii , 'x' ) ;
 oooOOo0o0OOO = ( i11II ) . replace ( IiiiII , 'y' ) . replace ( OoOo00OoOO00 , 'z' ) . replace ( O00O0 , '.' ) . replace ( ii11i1i , '(' ) . replace ( iIOOO0O00 , ')' ) . replace ( Oo0O000OoO00 , '/' ) ;
 oO0oOOoOo000O = ( oooOOo0o0OOO ) . replace ( ooO00Oo , '1' ) . replace ( Ii11iIiiI , '2' ) . replace ( II1o0O0OO , '3' ) . replace ( oO0OO00 , '4' ) . replace ( IiiI , '5' ) . replace ( IiiIiIIi , '6' ) ;
 oOoO0o = ( oO0oOOoOo000O ) . replace ( IIi1 , '7' ) . replace ( II11II , '8' ) . replace ( i1ii11 , '9' ) . replace ( III , '0' ) . replace ( oo0OooO , ':' ) . replace ( I11iI1 , '%' ) ;
 url = ( oOoO0o ) . replace ( Ii111IIIIii , '-' ) . replace ( oOoo , '_' ) ;
 IIOOO0O00O0OOOO ( name , url , 222 , iconimage ) ;
 if 22 - 22: ooo0oo0o0oo / O0OoO
 if 62 - 62: O0O0OoOO0 - IIIi + iI11I1II1I1I / O0OoO . IIIIi1i / O0O0OoOO0
def oOoO ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for IiI111111IIII , oOOO00o000o , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , IiI111111IIII , 1007 , oOOO00o000o )
def o0O0o0O ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , oOOO00o000o , Iii1IIII11I in i1I1i :
  II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , oOOO00o000o )
  if 16 - 16: ii % OOooOOo + ooo0oo0o0oo
def I1I11Oo0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 I1iiioO0O0ooO0oOO = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 I1iiioO0O0ooO0oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iiioO0O0ooO0oOO )
 if 62 - 62: Ii1I
 if 47 - 47: iii1iiii1 % O0OoO * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0ooo0 )
 for url , iI1I , Iii1IIII11I in i1I1i :
  if '-dir-' in Iii1IIII11I :
   II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iI1I )
  else :
   II11IiIi11 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , iI1I )
   if 7 - 7: oOo0O0Ooo
def i111i11iI1i1I ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 IiI1 = ( 'http://afewbitsmore.com/' )
 i1I1i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if '[To Parent Directory]' in Iii1IIII11I :
   Iii1IIII11I = 'HOME'
   pass
  elif 'HOME' in Iii1IIII11I :
   pass
  elif '.m3u' in Iii1IIII11I :
   II11IiIi11 ( '[COLOR' + iIii1 + ']PLAY ALL[/COLOR]' , IiI1 + url , 2002 , i11i1I1 + 'music.png' )
  elif '.mp3' in Iii1IIII11I :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , IiI1 + url , 222 , i11i1I1 + 'music.png' )
  elif '.m4a' in Iii1IIII11I :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , IiI1 + url , 222 , i11i1I1 + 'music.png' )
  else :
   II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , IiI1 + url , 1012 , i11i1I1 + 'music.png' )
def Iiii11IiI ( url ) :
 IIi1i11111 = oOOOoo00 ( url )
 i1I1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for iI1I , Iii1IIII11I , url in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , i11i1I1 + 'music.png' )
  if 14 - 14: oO0o0OOOO - I1ii11iIi11i . I1ii11iIi11i * O0OoO . oOo0O0Ooo % IIIIi1i
def OO00OO ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 IiI1 = url
 i1I1i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  if '.mp3' in Iii1IIII11I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , i11i1I1 + 'music.png' )
  else :
   II11IiIi11 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '/' , '' ) , IiI1 + url , 1011 , i11i1I1 + 'music.png' )
def IiIiIi11iiIi1 ( ) :
 o0ooo0 = oOOOoo00 ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1I1i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( o0ooo0 )
 for IiI111111IIII , iI1I , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , ( 'http://www.cyn.net/music/' + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iI1I ) . replace ( ' ' , '%20' ) )
def OoOoO0O00oo ( url , img ) :
 o0ooo0 = oOOOoo00 ( url )
 iiI1IIIi = url
 img = img
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( iiI1IIIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 71 - 71: o0o00Oo0O % o0o00Oo0O
def oooooOOo0Oo ( url ) :
 o0ooo0 = oOOOoo00 ( url )
 iiI1IIIi = url
 i1I1i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o0ooo0 )
 for type , url , Iii1IIII11I in i1I1i :
  if '[VID]' in type :
   IIOOO0O00O0OOOO ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iiI1IIIi + url , 222 , i11i1I1 + 'music.png' )
  if '[DIR]' in type :
   oooooOOo0Oo ( iiI1IIIi + url )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: o0o00Oo0O * Ii / ii / I11i . OO0
 if 70 - 70: ii . OO0 / IIIi . IIIi - I11i
def i1II1i1iiI1 ( ) :
 oo0O0oOOO0o = ( i1iiIII111ii ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 i11IIIiI11 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iiI1IIIi = ( i1iiIII111ii ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 Oo0o0000OOoO = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 62 - 62: O0O0OoOO0 . Ii % o0o00Oo0O % iii1iiii1 - I1ii11iIi11i
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 ooOO00O00oo = O0Oo000ooO00 ( iiI1IIIi )
 I1ii11iI = O0Oo000ooO00 ( Oo0o0000OOoO )
 if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % O0O0OoOO0 + oOo0O0Ooo
 if IIi1i11111 != 'Failed' :
  i1I1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i11111 )
  for Iii1IIII11I in i1I1i :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiI111111IIII + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 100 - 100: Ii - I1ii11iIi11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if ooOO00O00oo != 'Failed' :
  Iiiii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i11111 )
  for Iii1IIII11I in Iiiii1i :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiI1IIIi + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 47 - 47: IIIIi1i * OOooOOo * ooo0oo0o0oo
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if I1ii11iI != 'Failed' :
  II1III1i1iiI = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1ii11iI )
  for Iii1IIII11I in II1III1i1iiI :
   if i11IIIiI11 in Iii1IIII11I . lower ( ) :
    II11IiIi11 ( ( Iii1IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Oo0o0000OOoO + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 46 - 46: O0O0OoOO0
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 42 - 42: iI11I1II1I1I
    if 32 - 32: I1ii11iIi11i - O0O0OoOO0 . ii - ii - I1ii11iIi11i . iI11I1II1I1I
    if 34 - 34: I1ii11iIi11i
    if 31 - 31: ooOoO0O00 - oO0o0OOOO + iii1iiii1 + OO0 . OO0 . o0o00Oo0O
    if 33 - 33: ooOoO0O00 / IIIIi1i * oO0o
    if 2 - 2: IIIi . O0OoO
O0Oo0oO0OO0 = '{SF},' ; oo0o0 = '{IF},' ; OoO00o00 = '{PW},' ; II1o0O0OO = '{AM},' ; ooOoo0oo00000O = '{GF},' ; oo0 = '{DD},' ; o0Oo00o0 = '{UO},' ; oOOoOo0Ooo = '{LE},' ; o0OOoOoo00 = '{ZY},' ; Oo0Ooo0 = '{UE},' ; IiIIiIi11ii = '{PE},' ; II11IiIIiiiii = '{JE},' ; IiiiII = '{TH},' ; OoOo00OoOO00 = '{LK},'
if 43 - 43: iI11I1II1I1I
if 29 - 29: ooo0oo0o0oo % OO0 + oO0o . ooOoO0O00 + oOo0O0Ooo
def I111I ( ) :
 o0ooo0 = O000OOo00oo ( 'http://www.iwatchseries.me/tv-list/' )
 i1I1i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , IiI111111IIII , 8021 , i11i1I1 + 'iwatch.png' )
def oooO ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I , ooo in i1I1i :
  II11IiIi11 ( Iii1IIII11I + ooo , url , 8022 , i11i1I1 + 'iwatch.png' )
def oo0OOoOo0 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o0ooo0 )
 for url in i1I1i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oO00oO0 ( url )
def oO00oO0 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( o0ooo0 )
 Iiiii1i = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( o0ooo0 )
 II1III1i1iiI = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( 'VidSpot - ' + Iii1IIII11I , url , 222 , i11i1I1 + 'iwatch.png' )
 for url in Iiiii1i :
  IIOOO0O00O0OOOO ( 'VodLocker' , url , 222 , i11i1I1 + 'iwatch.png' )
 for Iii1IIII11I , url in II1III1i1iiI :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   IIOOO0O00O0OOOO ( 'TheVideo - ' + Iii1IIII11I , url , 222 , i11i1I1 + 'iwatch.png' )
   if 80 - 80: IIIIi1i . o0o00Oo0O
def I1Iii ( ) :
 o0ooo0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1I1i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , IiI111111IIII , 1021 , i11i1I1 + 'anime.png' )
  if 33 - 33: I11i - IIIi % Ii1I * oO0o0OOOO . ii % O0O0OoOO0
  if 29 - 29: IIIIi1i + IIiIiII11i . Ii . O0O0OoOO0 - o0o00Oo0O
def IIIOoo ( ) :
 o0ooo0 = O000OOo00oo ( 'http://www.animetoon.org/cartoon' )
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o0ooo0 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , IiI111111IIII , 1002 , i11i1I1 + 'anime.png' )
  if 71 - 71: iI11I1II1I1I . iI11I1II1I1I * ooo0oo0o0oo
  if 56 - 56: oO0o0OOOO / IIIi - IIIi
  if 40 - 40: Ii * IIiIiII11i
def Oo0ooooO0o00 ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o0ooo0 )
 for iI1I in Iiiii1i :
  OoOi111i = iI1I
 II1III1i1iiI = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o0ooo0 )
 for url in II1III1i1iiI :
  II11IiIi11 ( 'NEXT PAGE' , url , 1002 , i11i1I1 + 'Next.png' )
 i1I1i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o0ooo0 )
 for url , Iii1IIII11I in i1I1i :
  II11IiIi11 ( Iii1IIII11I , url , 1003 , OoOi111i )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIIIIIi11Ii ( url , IMAGE ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o0ooo0 )
 for Iii1IIII11I , url in i1I1i :
  print Iii1IIII11I + '     ' + url
  if 'easy' in url :
   oOOo ( url )
  elif 'playpanda' in url :
   oOOo ( url )
   if 85 - 85: ooOoO0O00 . ooOoO0O00
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOo ( url ) :
 o0ooo0 = O000OOo00oo ( url )
 i1I1i = re . compile ( "url: '(.+?)'," ) . findall ( o0ooo0 )
 for url in i1I1i :
  IIOOO0O00O0OOOO ( 'STREAM' , url , 222 , i11i1I1 + 'anime.png' )
  if 16 - 16: oOo0O0Ooo - O0OoO % O0O0OoOO0 . O0OoO + Ii1I % Ii
  if 59 - 59: Ii - oO0o0OOOO
def oooO00oOOooO ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oO0 . add_header ( 'referer' , url )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
def oOOOoo00 ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 3 - 3: I11i - ii + IIIIi1i . oO0o0OOOO
def o00000Oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 oOOOoo0o = ( '%s%s' % ( iiiI1IiIIii , url ) )
 ooOooo000oOO = oOOOoo00 ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooOooo000oOO )
 for url , oOOO00o000o , Iii1IIII11I in i1I1i :
  IIOOO0O00O0OOOO ( '%s' % ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOOO00o000o )
  if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
def O00 ( url ) :
 if 50 - 50: OOooOOo % O0O0OoOO0 + OOooOOo * O0O0OoOO0 - O0OoO
 oooiiI11 = open ( IIIii1II1II , "a" )
 oooiiI11 . write ( 'url="' + url + '"\n' )
 oooiiI11 . close
 if 10 - 10: OO0 - I1ii11iIi11i % IIiIiII11i
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 import urlresolver
 try : O0O00OooO . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Iii1IIII11I ) )
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O0O00OooO . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
def I1iI1111ii1I1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Iii1IIII11I )
 xbmc . sleep ( 1 )
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 o0oOoO00o . update ( 100 , '%s' % Iii1IIII11I )
 xbmc . sleep ( 1 )
 O0O00OooO . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 70 - 70: Ii1I . o0o00Oo0O
def oO000o ( url ) :
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0O00OooO . play ( url ) . strip ( )
 except : pass
 if 70 - 70: I1ii11iIi11i + Ii
def ii1IO0oo00o000 ( url ) :
 O0O00OooO = xbmc . Player ( iI1iiIii1I11I ( ) )
 import urlresolver
 II1111iiI1II = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 O0O00OooO . play ( II1111iiI1II )
 xbmc . sleep ( 1 )
 O0O00OooO . play ( url )
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - O0O0OoOO0 * iI11I1II1I1I
 if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / IIIi * I11i + O0OoO
def iI1iiIii1I11I ( ) :
 try :
  o0oOO00O000O0 = getSet ( "core-player" )
  if ( o0oOO00O000O0 == 'DVDPLAYER' ) : OOOoO000 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0oOO00O000O0 == 'MPLAYER' ) : OOOoO000 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0oOO00O000O0 == 'PAPLAYER' ) : OOOoO000 = xbmc . PLAYER_CORE_PAPLAYER
  else : OOOoO000 = xbmc . PLAYER_CORE_AUTO
 except : OOOoO000 = xbmc . PLAYER_CORE_AUTO
 return OOOoO000
 return True
 if 79 - 79: IIIIi1i / iii1iiii1 + I11i
def II11IiIi11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oO0oOO = [ ]
  if showcontext == 'fav' :
   oO0oOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oO0oOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1i11II11i1iI . addContextMenuItems ( oO0oOO )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = True )
 return O00oO0o000oO
 if 84 - 84: Ii / I11i % iI11I1II1I1I . OO0 . oO0o / IIIIi1i
def OooOo000o0o ( name , url , mode , iconimage , fanart , description ) :
 if 55 - 55: IIIIi1i
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i11II11i1iI . setProperty ( "Fanart_Image" , fanart )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = True )
 return O00oO0o000oO
 if 3 - 3: iI11I1II1I1I
def IIOOO0O00O0OOOO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oO0oOO = [ ]
  if showcontext == 'fav' :
   oO0oOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oO0oOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1i11II11i1iI . addContextMenuItems ( oO0oOO )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = False )
 return O00oO0o000oO
 if 19 - 19: IIiIiII11i . oO0o * oO0o + oOo0O0Ooo % I1ii11iIi11i
 if 21 - 21: OOooOOo - Ii - OOooOOo
 if 4 - 4: oO0o0OOOO . ooo0oo0o0oo
 if 39 - 39: O0OoO . I1ii11iIi11i - OOooOOo * Ii
 if 4 - 4: OOooOOo * o0o00Oo0O - oO0o0OOOO
 if 72 - 72: oO0o0OOOO + OO0 / oOo0O0Ooo . ooo0oo0o0oo % oO0o / Ii
def ii1I ( heading , announce ) :
 class I1III1I1IiI ( ) :
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
   try : Iii1I1I11iiI1 = open ( announce ) ; II1i = Iii1I1I11iiI1 . read ( )
   except : II1i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( II1i ) )
   return
 I1III1I1IiI ( )
 I1III1I1IiI ( )
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def iiIi1111iiI1 ( ) :
 ii1I ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 85 - 85: oO0o0OOOO + iii1iiii1
 if 11 - 11: oO0o0OOOO
 if 95 - 95: I1ii11iIi11i + Ii % O0OoO - IIIi
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: iii1iiii1 + ooo0oo0o0oo * iI11I1II1I1I
def IiIi1I1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / O0O0OoOO0
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . oO0o0OOOO
 if 2 - 2: O0O0OoOO0
 if 12 - 12: Ii - iI11I1II1I1I * ooo0oo0o0oo * IIIIi1i
 if 19 - 19: o0o00Oo0O + IIIi + I11i
 if 81 - 81: iI11I1II1I1I
 if 51 - 51: I11i . Ii1I * O0O0OoOO0 / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % iii1iiii1 % IIIi + oO0o0OOOO * IIIi . O0O0OoOO0
 if 89 - 89: ii % IIiIiII11i - oO0o % Ii
 if 7 - 7: ooo0oo0o0oo
 if 15 - 15: I1ii11iIi11i + IIIIi1i + oOo0O0Ooo * I11i
 if 33 - 33: I11i * I1ii11iIi11i
 if 88 - 88: iii1iiii1 % O0OoO - OOooOOo - OOooOOo . oOo0O0Ooo
 if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - iii1iiii1
 if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
 if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - O0O0OoOO0
 if 59 - 59: ooo0oo0o0oo % IIIi
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 if 15 - 15: OO0 / OO0 % ii . iii1iiii1
 if 93 - 93: Ii1I * Ii1I / ii
 if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
 if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
 if 27 - 27: O0OoO * ooo0oo0o0oo / Ii - IIIi + IIiIiII11i
 if 43 - 43: Ii1I - IIiIiII11i
def OOoIiI1i11iIi1 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iiiiIIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 11 - 11: oO0o0OOOO
def IIIIi1IiII1II1 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + O0ooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 30 - 30: OOooOOo - Ii
def oO0OOOO00o ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + i1Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 60 - 60: OO0 * O0O0OoOO0 + iii1iiii1 . O0OoO . o0o00Oo0O
def Ii1i1ii ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 79 - 79: ii * iii1iiii1 - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
def oO0ooo00OoOooooo ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + OoooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 7 - 7: OOooOOo . O0OoO % I1ii11iIi11i
def o00OO000 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + oO0oOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 42 - 42: oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 6 - 6: O0OoO + Ii1I + I1ii11iIi11i
def o0OOo0o0o0ooo ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + o0OOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 52 - 52: oO0o
def I1O0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + oO0oo0oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , iII1 , oO0o0 , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 5 - 5: ii * Ii1I
def IIio0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iIOoO0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , iII1 , oO0o0 , i1i11I1I1iii1 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , i11i1I1 + 'GenieTVRSSFeed.png' , i11i1I1 + 'GenieTVRSSFeed.png' , i1i11I1I1iii1 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 96 - 96: ooo0oo0o0oo - IIIIi1i
 if 34 - 34: O0OoO - Ii1I * IIIIi1i % O0O0OoOO0
 if 25 - 25: IIiIiII11i + oOo0O0Ooo * OO0 * Ii1I . IIIIi1i
 if 26 - 26: IIIIi1i - OO0 / ii + I11i . I1ii11iIi11i
 if 75 - 75: o0o00Oo0O / OOooOOo . iii1iiii1
 if 7 - 7: oO0o * IIIIi1i
 if 16 - 16: iii1iiii1 . ooOoO0O00 . ooo0oo0o0oo
 if 50 - 50: oO0o - IIiIiII11i * ii - oOo0O0Ooo . o0o00Oo0O + o0o00Oo0O
 if 80 - 80: I11i
def i1I1iii1I11II ( ) :
 try :
  if os . path . exists ( O0o0Oo ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( O0o0Oo ) :
     IiI1I = 0
     IiI1I += len ( iI1I11i )
     if IiI1I > 0 :
      for Iii1I1I11iiI1 in iI1I11i :
       os . unlink ( os . path . join ( ooOOooo0Oo , Iii1I1I11iiI1 ) )
  oO0oO0ooOoO0 = os . path . join ( OO0o , "Textures13.db" )
  os . unlink ( oO0oO0ooOoO0 )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 10 - 10: Ii % O0OoO * IIIIi1i % I1ii11iIi11i
 if 51 - 51: oO0o % IIIIi1i
 if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
 if 8 - 8: Ii1I % oO0o % IIIi . Ii1I * Ii1I
 if 94 - 94: Ii + ii
 if 20 - 20: Ii
 if 86 - 86: OOooOOo / O0OoO
 if 40 - 40: iI11I1II1I1I / OO0 / oOo0O0Ooo + Ii1I * O0OoO
def III1i1iI111I1 ( title , message , times = 2000 , icon = OooO0 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 64 - 64: I1ii11iIi11i % OOooOOo . I11i % oOo0O0Ooo / O0OoO
def OOoO00 ( url ) :
 O00OOO00 = os . path . join ( oo0o0O00 , 'addon_data' )
 II1iiII1 = [
 ( O00OOO00 ) ,
 ( Oo0o0000o0o0 ) ,
 ( os . path . join ( i11 , 'cache' ) ) ,
 ( os . path . join ( i11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( O00OOO00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( O00OOO00 , 'plugin.video.itv' , 'Images' ) ) ]
 if 48 - 48: iii1iiii1 * ooOoO0O00 - Ii1I / oOo0O0Ooo + Ii - ooOoO0O00
 oOo0O = 0
 if 40 - 40: IIIIi1i * IIIIi1i / I11i
 for OOOo00 in II1iiII1 :
  if os . path . exists ( OOOo00 ) and not OOOo00 in [ Oo0o0000o0o0 , O00OOO00 ] :
   for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( OOOo00 ) :
    IiI1I = 0
    IiI1I += len ( iI1I11i )
    if IiI1I > 0 :
     for Iii1I1I11iiI1 in iI1I11i :
      if not Iii1I1I11iiI1 in oO :
       try :
        os . unlink ( os . path . join ( ooOOooo0Oo , Iii1I1I11iiI1 ) )
       except :
        pass
      else : I1IiiiiI ( 'Ignore Log File: %s' % Iii1I1I11iiI1 )
     for Ii1i1i1111 in OOoOoO00O0O0o :
      try :
       shutil . rmtree ( os . path . join ( ooOOooo0Oo , Ii1i1i1111 ) )
       oOo0O += 1
       I1IiiiiI ( "[Success] cleared %s files from %s" % ( str ( IiI1I ) , os . path . join ( OOOo00 , Ii1i1i1111 ) ) )
      except :
       I1IiiiiI ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOo00 , Ii1i1i1111 ) )
  else :
   for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( OOOo00 ) :
    for Ii1i1i1111 in OOoOoO00O0O0o :
     if 'cache' in Ii1i1i1111 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooOOooo0Oo , Ii1i1i1111 ) )
       oOo0O += 1
       I1IiiiiI ( "[Success] wiped %s " % os . path . join ( OOOo00 , Ii1i1i1111 ) )
      except :
       I1IiiiiI ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOo00 , Ii1i1i1111 ) )
       if 42 - 42: O0O0OoOO0 * oOo0O0Ooo - o0o00Oo0O - OO0
 III1i1iI111I1 ( oO0o0o0ooO0oO , 'Clear Cache: Removed %s Files' % oOo0O )
 if 22 - 22: iI11I1II1I1I / OO0 / oOo0O0Ooo - I11i
 if 21 - 21: IIIi . Ii * oO0o0OOOO . O0OoO / O0OoO
 if 42 - 42: ii / iii1iiii1 . I11i / o0o00Oo0O - ooo0oo0o0oo * ooo0oo0o0oo
 if 1 - 1: O0O0OoOO0 % iii1iiii1
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % O0OoO . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: iii1iiii1 % OO0 - OO0 % oOo0O0Ooo . O0OoO - ii
def OOO0oO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oO00II1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( oO00II1I ) :
   IiI1I = 0
   IiI1I += len ( iI1I11i )
   if 78 - 78: ii - OOooOOo . Ii
   if 36 - 36: IIIi * IIIIi1i + ooo0oo0o0oo * IIIIi1i . Ii1I - iI11I1II1I1I
   if IiI1I > 0 :
    if 14 - 14: oO0o0OOOO * IIIi + Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( IiI1I ) + " files found" , "Do you want to delete them?" ) :
     if 84 - 84: IIIIi1i / IIiIiII11i
     for Iii1I1I11iiI1 in iI1I11i :
      os . unlink ( os . path . join ( ooOOooo0Oo , Iii1I1I11iiI1 ) )
     for Ii1i1i1111 in OOoOoO00O0O0o :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , Ii1i1i1111 ) )
     oooOOOOO = xbmcgui . Dialog ( )
     oooOOOOO . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    oooOOOOO = xbmcgui . Dialog ( )
    oooOOOOO . ok ( i1 , "       No Packages to DELETE" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
 if 8 - 8: Ii / OO0
 if 33 - 33: iii1iiii1 * ooo0oo0o0oo - o0o00Oo0O + oOo0O0Ooo / ooo0oo0o0oo
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: ooo0oo0o0oo - I11i % O0OoO - IIiIiII11i
 if 56 - 56: O0O0OoOO0 * Ii
def oOO00OO0ooo0o ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oO00II1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( oO00II1I ) :
   IiI1I = 0
   IiI1I += len ( iI1I11i )
   if 92 - 92: IIiIiII11i - o0o00Oo0O . iii1iiii1
   if 59 - 59: OOooOOo
   if IiI1I > 0 :
    if 47 - 47: IIiIiII11i - Ii1I - O0O0OoOO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( IiI1I ) + " files found" , "Do you want to delete them?" ) :
     if 9 - 9: Ii1I - ooo0oo0o0oo
     for Iii1I1I11iiI1 in iI1I11i :
      os . unlink ( os . path . join ( ooOOooo0Oo , Iii1I1I11iiI1 ) )
     for Ii1i1i1111 in OOoOoO00O0O0o :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , Ii1i1i1111 ) )
     oooOOOOO = xbmcgui . Dialog ( )
     oooOOOOO . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    oooOOOOO = xbmcgui . Dialog ( )
    oooOOOOO . ok ( i1 , "       No Packages to DELETE" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 OOoO00 ( url )
 return
 if 64 - 64: ooOoO0O00
 if 71 - 71: ooo0oo0o0oo * I11i
 if 99 - 99: I11i
 if 28 - 28: ii % o0o00Oo0O - O0OoO / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * ooo0oo0o0oo / oO0o . IIIi
 if 50 - 50: ii + iI11I1II1I1I / IIIi / O0OoO . Ii . OO0
 if 75 - 75: iI11I1II1I1I % OO0 / O0OoO - IIIIi1i % Ii
 if 11 - 11: oO0o0OOOO . O0O0OoOO0
 if 87 - 87: O0OoO + O0OoO
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
def OO0OoOo00 ( url , name ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 OoOOo0OO0OOoo = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OoOOo0OO0OOoo ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
   try :
    os . remove ( OoooI1iIiii )
    print '=== GenieTv - REMOVING    ' + str ( OoooI1iIiii ) + '    ==='
   except :
    pass
   ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
   Ii1iI111 = open ( OoooI1iIiii , "w" )
   Ii1iI111 . write ( ooOooo000oOO )
   Ii1iI111 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoooI1iIiii ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
  try :
   os . remove ( OoooI1iIiii )
   print '=== GenieTv - REMOVING    ' + str ( OoooI1iIiii ) + '    ==='
  except :
   pass
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  Ii1iI111 = open ( OoooI1iIiii , "w" )
  Ii1iI111 . write ( ooOooo000oOO )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoooI1iIiii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 38 - 38: ooo0oo0o0oo . I11i
def i1Ii111 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 try :
  Ii1iI111 = open ( OoooI1iIiii ) . read ( )
  if 'zero' in Ii1iI111 :
   name = '0CACHE'
  elif 'tuxen' in Ii1iI111 :
   name = 'TUXENS'
  elif 'muckys' in Ii1iI111 :
   name = 'MUCKYS'
  elif 'p2p1' in Ii1iI111 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Ii1iI111 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Ii1iI111 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 58 - 58: IIIi * Ii * oOo0O0Ooo * Ii1I % Ii - ii
def ii1II11IIII ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 try :
  os . remove ( OoooI1iIiii )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoooI1iIiii ) + '    ==='
  oooOOOOO . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 90 - 90: I1ii11iIi11i * O0O0OoOO0
 if 54 - 54: Ii1I + iI11I1II1I1I % ooo0oo0o0oo
 if 24 - 24: oO0o / o0o00Oo0O * OO0 % iI11I1II1I1I + ooOoO0O00 % o0o00Oo0O
 if 26 - 26: OO0 + ooo0oo0o0oo - o0o00Oo0O * IIIi * IIiIiII11i . Ii1I
 if 75 - 75: OOooOOo / ii / oO0o0OOOO % OOooOOo * O0O0OoOO0 * ooo0oo0o0oo
 if 11 - 11: Ii1I / O0OoO . O0O0OoOO0 * Ii1I
 if 17 - 17: Ii1I * ii % ooOoO0O00 % ii . IIIIi1i
 if 20 - 20: oO0o . IIIi
 if 4 - 4: I1ii11iIi11i % O0O0OoOO0 % oO0o * IIIIi1i % ii
 if 38 - 38: ii . IIIIi1i
def iiII11 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1I1i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1iiIIiiI111 . http_GET ( url ) . content )
 for OO0OoO0OOoOo , oO000 , iIiI1ii1I1I , I1ii11ii1I in i1I1i :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OO0OoO0OOoOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iIiI1ii1I1I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1ii11ii1I )
  inc = inc + 1
  if 8 - 8: I11i . IIiIiII11i . IIIIi1i - Ii
  if 50 - 50: O0O0OoOO0 . o0o00Oo0O % oO0o . IIIi + O0O0OoOO0 . OOooOOo
  if 69 - 69: Ii + Ii . Ii - Ii % O0O0OoOO0 / IIIIi1i
  if 59 - 59: ii
  if 96 - 96: O0O0OoOO0
  if 54 - 54: oO0o0OOOO % oO0o0OOOO - OO0
  if 32 - 32: I11i % IIiIiII11i / I11i . O0OoO . I11i
  if 29 - 29: ii % IIiIiII11i % Ii - I1ii11iIi11i
  if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
def iIIIIi ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'addons2.ini' )
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  Ii1iI111 = open ( OoooI1iIiii , "w" )
  Ii1iI111 . write ( ooOooo000oOO )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoooI1iIiii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 15 - 15: oOo0O0Ooo / O0OoO
def IIi1IiiI1II ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoooI1iIiii = os . path . join ( oOoOOo000oOoO0 , 'settings.xml' )
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  Ii1iI111 = open ( OoooI1iIiii , "w" )
  Ii1iI111 . write ( ooOooo000oOO )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoooI1iIiii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 79 - 79: IIIi
 if 64 - 64: ii * IIiIiII11i . iI11I1II1I1I . IIIIi1i + Ii1I . I11i
def I1i1I ( ) :
 try :
  O0OoooIiiI11Iii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( O0OoooIiiI11Iii ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I1Iii1 = os . path . join ( O0OoooIiiI11Iii , "source.db" )
    os . unlink ( I1Iii1 )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 9 - 9: IIiIiII11i % I1ii11iIi11i * O0O0OoOO0 + ooo0oo0o0oo % oO0o . ooOoO0O00
 if 68 - 68: IIiIiII11i % iii1iiii1 * Ii
 if 9 - 9: IIiIiII11i + Ii1I / IIIIi1i
 if 51 - 51: oO0o0OOOO % Ii1I + ii - oOo0O0Ooo * OOooOOo * IIIIi1i
 if 7 - 7: O0OoO . ooo0oo0o0oo . iii1iiii1 / O0O0OoOO0 / I1ii11iIi11i
def O000OOo00oo ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 83 - 83: oO0o0OOOO / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
 if 10 - 10: oO0o0OOOO - I11i % ii - Ii1I
 if 64 - 64: oO0o / oOo0O0Ooo
 if 23 - 23: oO0o0OOOO * iii1iiii1 * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: ooo0oo0o0oo * ii . OO0 % Ii
 if 11 - 11: iI11I1II1I1I . iii1iiii1 - I1ii11iIi11i / oO0o0OOOO + IIiIiII11i
def I1III1i ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iiOOoOO = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iiOOoOO :
  OOo00OOoOOO = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; OOo00OOoOOO = xbmc . translatePath ( OOo00OOoOOO ) ;
  I1iII11I1I = os . path . join ( OOo00OOoOOO , ".." , ".." ) ; I1iII11I1I = os . path . abspath ( I1iII11I1I ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + I1iII11I1I ) ; i1i1ii1 = False
  try :
   for ooOOooo0Oo , OOoOoO00O0O0o , iI1I11i in os . walk ( I1iII11I1I , topdown = True ) :
    OOoOoO00O0O0o [ : ] = [ Ii1i1i1111 for Ii1i1i1111 in OOoOoO00O0O0o if Ii1i1i1111 not in o0oO0 ]
    for Iii1IIII11I in iI1I11i :
     try : os . remove ( os . path . join ( ooOOooo0Oo , Iii1IIII11I ) )
     except :
      if Iii1IIII11I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : i1i1ii1 = True
      plugintools . log ( "Error removing " + ooOOooo0Oo + " " + Iii1IIII11I )
    for Iii1IIII11I in OOoOoO00O0O0o :
     try : os . rmdir ( os . path . join ( ooOOooo0Oo , Iii1IIII11I ) )
     except :
      if Iii1IIII11I not in [ "Database" , "userdata" ] : i1i1ii1 = True
      plugintools . log ( "Error removing " + ooOOooo0Oo + " " + Iii1IIII11I )
   if not i1i1ii1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OOO0o ( )
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
def I1IiII ( ) :
 o0O00o0o = [ ]
 I11Ii111IIi = sys . argv [ 2 ]
 if len ( I11Ii111IIi ) >= 2 :
  OoOoO0OooO00Oo = sys . argv [ 2 ]
  oO0OO00O0 = OoOoO0OooO00Oo . replace ( '?' , '' )
  if ( OoOoO0OooO00Oo [ len ( OoOoO0OooO00Oo ) - 1 ] == '/' ) :
   OoOoO0OooO00Oo = OoOoO0OooO00Oo [ 0 : len ( OoOoO0OooO00Oo ) - 2 ]
  O000oOo0OO = oO0OO00O0 . split ( '&' )
  o0O00o0o = { }
  for i1I1Ii11i in range ( len ( O000oOo0OO ) ) :
   oo00O000 = { }
   oo00O000 = O000oOo0OO [ i1I1Ii11i ] . split ( '=' )
   if ( len ( oo00O000 ) ) == 2 :
    o0O00o0o [ oo00O000 [ 0 ] ] = oo00O000 [ 1 ]
    if 90 - 90: IIIIi1i
 return o0O00o0o
 if 81 - 81: O0O0OoOO0 % oO0o
OOIII = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
Ooo0O0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IiiI1iIiI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOOOo0ooOOO0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iiIii1IIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo00O0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iiiiIIIi = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IIIIiI1i1111iI1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
O0ooOo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1Ii1I = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
ooO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OoooooO0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oO0oOOoO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oo000o = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0OOoo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oO0oo0oOO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iii11II1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OoO00o = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iI = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OoOooOo0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0O0ooOOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OOoO0ooOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iIOoO0O00 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iiiI1IiIIii = base64 . decodestring ( 'Q1VOVA==' )
def iiIi1IIi1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i11II11i1iI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oO0oOO = [ ]
  if showcontext == 'fav' :
   oO0oOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oO0oOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1i11II11i1iI . addContextMenuItems ( oO0oOO )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = True )
 return O00oO0o000oO
 if 90 - 90: ii % Ii % I11i % iii1iiii1 - OO0 + iI11I1II1I1I
def i1I1iI1iIi111i ( name , url , mode , iconimage , fanart , description ) :
 OOOiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00oO0o000oO = True
 I1i11II11i1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1i11II11i1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1i11II11i1iI . setProperty ( "Fanart_Image" , fanart )
 O00oO0o000oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOiI1 , listitem = I1i11II11i1iI , isFolder = False )
 return O00oO0o000oO
 if 98 - 98: o0o00Oo0O / IIIi / IIIIi1i
 if 83 - 83: iii1iiii1
OoOoO0OooO00Oo = I1IiII ( )
IiI111111IIII = None
Iii1IIII11I = None
iI1i1IiIIIIi = None
iII1 = None
oO0o0 = None
i1i11I1I1iii1 = None
iiIi1iIiI = None
if 20 - 20: oO0o + oO0o0OOOO . IIiIiII11i / Ii
if 50 - 50: ii / oO0o % iI11I1II1I1I
try :
 iiIi1iIiI = int ( OoOoO0OooO00Oo [ "fav_mode" ] )
except :
 pass
 if 41 - 41: Ii1I % Ii1I + ooo0oo0o0oo . IIIIi1i % iii1iiii1 * OO0
try :
 IiI111111IIII = urllib . unquote_plus ( OoOoO0OooO00Oo [ "url" ] )
except :
 pass
try :
 Iii1IIII11I = urllib . unquote_plus ( OoOoO0OooO00Oo [ "name" ] )
except :
 pass
try :
 iII1 = urllib . unquote_plus ( OoOoO0OooO00Oo [ "iconimage" ] )
except :
 pass
try :
 iI1i1IiIIIIi = int ( OoOoO0OooO00Oo [ "mode" ] )
except :
 pass
try :
 oO0o0 = urllib . unquote_plus ( OoOoO0OooO00Oo [ "fanart" ] )
except :
 pass
try :
 i1i11I1I1iii1 = urllib . unquote_plus ( OoOoO0OooO00Oo [ "description" ] )
except :
 pass
 if 57 - 57: O0O0OoOO0 . iii1iiii1 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
print str ( Oo00OOOOO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( iI1i1IiIIIIi )
print "URL: " + str ( IiI111111IIII )
print "Name: " + str ( Iii1IIII11I )
print "IconImage: " + str ( iII1 )
if 93 - 93: OO0 / O0OoO * o0o00Oo0O
if 17 - 17: oO0o / OO0 % oOo0O0Ooo
def oOooOo0 ( content , viewType ) :
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 60 - 60: Ii1I / ooo0oo0o0oo . Ii / oO0o % IIiIiII11i
if iII1 == None : iII1 = OooO0
if oO0o0 == None : oO0o0 = ooOoOoo0O
if iI1i1IiIIIIi == None :
 oOooOOOoOo ( )
 if 6 - 6: IIIIi1i % I11i + iii1iiii1
elif iI1i1IiIIIIi == 1 :
 Oo00O0ooOO ( IiI111111IIII )
 if 91 - 91: I11i + o0o00Oo0O * IIIi * ooo0oo0o0oo * Ii1I
elif iI1i1IiIIIIi == 44 :
 Ii1iIi111i1i1 ( IiI111111IIII )
 if 83 - 83: ii
elif iI1i1IiIIIIi == 2 :
 iIIi1I1ii ( )
 if 52 - 52: I11i / OOooOOo % IIIi % oO0o / ooo0oo0o0oo % I11i
elif iI1i1IiIIIIi == 3 :
 o000 ( )
 if 88 - 88: O0OoO / Ii / O0O0OoOO0 / Ii * Ii1I % oO0o0OOOO
elif iI1i1IiIIIIi == 21 :
 i1i1II ( )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * O0O0OoOO0 + iI11I1II1I1I
elif iI1i1IiIIIIi == 4 :
 o00o ( )
 if 80 - 80: I11i . IIIIi1i . ii
elif iI1i1IiIIIIi == 5 :
 O0OO ( IiI111111IIII )
 if 63 - 63: OO0 . O0OoO
elif iI1i1IiIIIIi == 6 :
 OOO0oO ( IiI111111IIII )
 if 66 - 66: oOo0O0Ooo
elif iI1i1IiIIIIi == 7 :
 OO0OoOo00 ( IiI111111IIII , Iii1IIII11I )
 if 99 - 99: oO0o % o0o00Oo0O . iii1iiii1 - Ii1I . I1ii11iIi11i / OOooOOo
elif iI1i1IiIIIIi == 8 :
 i1Ii111 ( IiI111111IIII , Iii1IIII11I )
 if 60 - 60: Ii1I
elif iI1i1IiIIIIi == 9 :
 FIXREPOSADDONS ( IiI111111IIII )
 if 78 - 78: IIIi + IIiIiII11i
elif iI1i1IiIIIIi == 10 :
 IiIi1I1 ( )
 if 55 - 55: ii
elif iI1i1IiIIIIi == 11 :
 ii1II11IIII ( IiI111111IIII )
 if 90 - 90: oOo0O0Ooo
elif iI1i1IiIIIIi == 12 :
 iiII11 ( )
 if 4 - 4: O0OoO % OO0 - O0OoO - I11i
elif iI1i1IiIIIIi == 13 :
 i1I1iii1I11II ( )
 if 30 - 30: ooo0oo0o0oo
elif iI1i1IiIIIIi == 14 :
 OOoO00 ( IiI111111IIII )
 if 34 - 34: IIIi - IIiIiII11i - I11i + IIIIi1i + iii1iiii1
elif iI1i1IiIIIIi == 15 :
 iIIIi1i1I11i ( )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif iI1i1IiIIIIi == 16 :
 iIIIIi ( IiI111111IIII , Iii1IIII11I )
 if 20 - 20: Ii - IIiIiII11i - OO0 % IIIi . OO0
elif iI1i1IiIIIIi == 17 :
 IIi1IiiI1II ( IiI111111IIII , Iii1IIII11I )
 if 50 - 50: iI11I1II1I1I + iii1iiii1 - oO0o0OOOO - ii
elif iI1i1IiIIIIi == 18 :
 I1i1I ( )
 if 84 - 84: OOooOOo - oO0o0OOOO
elif iI1i1IiIIIIi == 19 :
 oO00OoOoo0 ( IiI111111IIII )
 if 80 - 80: Ii % O0OoO - I1ii11iIi11i % O0OoO
elif iI1i1IiIIIIi == 40 :
 OOOOOoOO0OOoo ( Iii1IIII11I , IiI111111IIII , i1i11I1I1iii1 )
 if 89 - 89: O0O0OoOO0 * oO0o0OOOO + OOooOOo / Ii
elif iI1i1IiIIIIi == 42 :
 III1ii ( Iii1IIII11I , IiI111111IIII , i1i11I1I1iii1 )
 if 68 - 68: ii * oO0o0OOOO
elif iI1i1IiIIIIi == 43 :
 Ii1IIi ( IiI111111IIII )
 if 86 - 86: I11i / OOooOOo
elif iI1i1IiIIIIi == 20 :
 OOo0 ( IiI111111IIII )
 if 40 - 40: IIIIi1i
elif iI1i1IiIIIIi == 22 :
 OOoIiI1i11iIi1 ( IiI111111IIII )
 if 62 - 62: OO0 / O0OoO
elif iI1i1IiIIIIi == 23 :
 IIIIi1IiII1II1 ( IiI111111IIII )
 if 74 - 74: IIIIi1i % iii1iiii1 / iii1iiii1 - iI11I1II1I1I - IIiIiII11i + O0OoO
elif iI1i1IiIIIIi == 24 :
 oO0OOOO00o ( IiI111111IIII )
 if 92 - 92: oO0o0OOOO % iii1iiii1
elif iI1i1IiIIIIi == 25 :
 Ii1i1ii ( IiI111111IIII )
 if 18 - 18: OO0 + iii1iiii1 / O0OoO / IIIi + iI11I1II1I1I % ooo0oo0o0oo
elif iI1i1IiIIIIi == 26 :
 oO0ooo00OoOooooo ( IiI111111IIII )
 if 94 - 94: oO0o0OOOO
elif iI1i1IiIIIIi == 27 :
 o00OO000 ( IiI111111IIII )
 if 37 - 37: IIIi
elif iI1i1IiIIIIi == 28 :
 o00OooooOOOO ( IiI111111IIII )
 if 52 - 52: Ii1I * oOo0O0Ooo . O0OoO + ooOoO0O00 % IIIi / iI11I1II1I1I
elif iI1i1IiIIIIi == 29 :
 o0OOo0o0o0ooo ( IiI111111IIII )
 if 68 - 68: iii1iiii1 - OOooOOo . Ii + I11i
elif iI1i1IiIIIIi == 30 :
 oOO0o000Oo00o ( IiI111111IIII )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif iI1i1IiIIIIi == 31 :
 I1O0 ( IiI111111IIII )
 if 33 - 33: oO0o0OOOO . I1ii11iIi11i
elif iI1i1IiIIIIi == 32 :
 o00O ( )
 if 89 - 89: IIIIi1i + ooOoO0O00 - ooo0oo0o0oo + OO0 . IIiIiII11i
elif iI1i1IiIIIIi == 33 :
 i111IIIiI ( )
 if 85 - 85: iI11I1II1I1I - O0O0OoOO0 * I1ii11iIi11i . IIIi + iii1iiii1
elif iI1i1IiIIIIi == 35 :
 ooOooOoOoO ( IiI111111IIII )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif iI1i1IiIIIIi == 34 :
 O0O00O000OOO ( IiI111111IIII )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IIIIi1i / IIIIi1i
elif iI1i1IiIIIIi == 36 :
 I1Ii1 ( IiI111111IIII )
 if 43 - 43: oOo0O0Ooo
elif iI1i1IiIIIIi == 37 :
 oOooO0 ( IiI111111IIII )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif iI1i1IiIIIIi == 38 :
 i1II1I ( IiI111111IIII )
 if 34 - 34: I11i % Ii1I + O0O0OoOO0 * oO0o0OOOO / IIIi
elif iI1i1IiIIIIi == 41 :
 I1III1i ( OoOoO0OooO00Oo )
 if 18 - 18: OO0
elif iI1i1IiIIIIi == 39 :
 IIio0 ( IiI111111IIII )
 if 92 - 92: oO0o % iI11I1II1I1I / ooo0oo0o0oo * IIIIi1i . ooOoO0O00 + IIIi
elif iI1i1IiIIIIi == 45 :
 TEXTS ( )
 if 24 - 24: ooo0oo0o0oo . IIIIi1i * ooo0oo0o0oo % Ii . Ii + ooOoO0O00
elif iI1i1IiIIIIi == 46 :
 iiIi1111iiI1 ( )
 if 64 - 64: iI11I1II1I1I / ooo0oo0o0oo / I1ii11iIi11i - Ii1I
elif iI1i1IiIIIIi == 47 :
 GEVID ( )
 if 100 - 100: ooo0oo0o0oo + ooOoO0O00 * oO0o
elif iI1i1IiIIIIi == 48 :
 O0Oo0Ooo ( Iii1IIII11I , IiI111111IIII , i1i11I1I1iii1 )
 if 64 - 64: IIIi * Ii . I1ii11iIi11i
elif iI1i1IiIIIIi == 49 :
 o0O0 ( )
 if 52 - 52: I1ii11iIi11i / OO0 / IIIIi1i - I11i / IIIIi1i
elif iI1i1IiIIIIi == 222 :
 O00 ( IiI111111IIII )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif iI1i1IiIIIIi == 333 :
 o00000Oo ( IiI111111IIII )
 if 85 - 85: oOo0O0Ooo
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif iI1i1IiIIIIi == 1020 :
 I1Iii ( )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif iI1i1IiIIIIi == 1021 :
 ANIMEEP ( )
 if 46 - 46: OOooOOo * oO0o0OOOO / IIIi + I1ii11iIi11i + ooo0oo0o0oo
elif iI1i1IiIIIIi == 1022 :
 ANIMEPLAY ( IiI111111IIII )
 if 95 - 95: I11i - O0O0OoOO0
elif iI1i1IiIIIIi == 1001 :
 IIIOoo ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif iI1i1IiIIIIi == 1005 :
 oOoO ( )
 if 19 - 19: OOooOOo . O0OoO . ii
elif iI1i1IiIIIIi == 1007 :
 o0O0o0O ( IiI111111IIII )
 if 79 - 79: O0OoO * OO0 * oOo0O0Ooo * Ii1I / Ii1I
elif iI1i1IiIIIIi == 1010 :
 I1Ii111I111 ( IiI111111IIII )
 if 62 - 62: OO0 * O0O0OoOO0 % Ii1I - ooOoO0O00 - Ii1I
elif iI1i1IiIIIIi == 1011 :
 OO00OO ( IiI111111IIII )
 if 24 - 24: O0OoO
elif iI1i1IiIIIIi == 1012 :
 i111i11iI1i1I ( IiI111111IIII )
 if 71 - 71: ooo0oo0o0oo - ooOoO0O00
elif iI1i1IiIIIIi == 1030 :
 IiIiIi11iiIi1 ( )
 if 56 - 56: OOooOOo + IIIi
elif iI1i1IiIIIIi == 1031 :
 OoOoO0O00oo ( IiI111111IIII , iII1 )
 if 74 - 74: IIIIi1i / iii1iiii1 / IIiIiII11i - IIIIi1i / IIIi % oO0o0OOOO
elif iI1i1IiIIIIi == 1032 :
 oooooOOo0Oo ( IiI111111IIII )
 if 19 - 19: ooo0oo0o0oo % ii + ii
elif iI1i1IiIIIIi == 1006 :
 Parse . ParseURL ( IiI111111IIII )
 if 7 - 7: ooOoO0O00
elif iI1i1IiIIIIi == 2030 :
 Parse . addonParseURL ( IiI111111IIII )
 if 91 - 91: OOooOOo - OOooOOo . ooo0oo0o0oo
elif iI1i1IiIIIIi == 2031 :
 Parse . apkParseURL ( IiI111111IIII )
 if 33 - 33: iii1iiii1 - iI11I1II1I1I / O0O0OoOO0 % o0o00Oo0O
elif iI1i1IiIIIIi == 1002 :
 Oo0ooooO0o00 ( IiI111111IIII )
 if 80 - 80: ooo0oo0o0oo % ii - ooo0oo0o0oo
elif iI1i1IiIIIIi == 1003 :
 iIIIIIi11Ii ( IiI111111IIII , iII1 )
 if 27 - 27: iii1iiii1 - I11i * Ii1I - oOo0O0Ooo
elif iI1i1IiIIIIi == 1004 :
 oOOo ( IiI111111IIII )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIIIi1i . O0O0OoOO0
elif iI1i1IiIIIIi == 1008 :
 oo0O0 ( )
 if 100 - 100: IIiIiII11i / iii1iiii1 / IIIIi1i - Ii1I * iI11I1II1I1I
elif iI1i1IiIIIIi == 1009 :
 I11i1IIi1i1 ( IiI111111IIII )
 if 7 - 7: ooOoO0O00 . ooo0oo0o0oo % Ii * Ii1I . oO0o0OOOO % Ii1I
elif iI1i1IiIIIIi == 2001 :
 I1Ii1IIi ( )
 if 35 - 35: oOo0O0Ooo
elif iI1i1IiIIIIi == 2002 :
 Iiii11IiI ( IiI111111IIII )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif iI1i1IiIIIIi == 1013 :
 OoOoOo0 ( )
elif iI1i1IiIIIIi == 10111113 :
 i1II11II1 ( IiI111111IIII )
 if 22 - 22: OO0 . Ii . ii . ooOoO0O00
elif iI1i1IiIIIIi == 1014 :
 ooooOoOooo00Oo ( )
 if 12 - 12: OOooOOo % O0OoO + IIIi . o0o00Oo0O % iI11I1II1I1I
elif iI1i1IiIIIIi == 1015 :
 ooo00O0OOo ( IiI111111IIII )
 if 41 - 41: ii
elif iI1i1IiIIIIi == 1016 :
 oo0OoO ( IiI111111IIII , iII1 , Iii1IIII11I )
 if 13 - 13: oO0o0OOOO + iii1iiii1 - iii1iiii1 % IIIi / oO0o0OOOO
elif iI1i1IiIIIIi == 1017 :
 OoOo00o0O00 ( )
 if 4 - 4: oOo0O0Ooo + O0OoO - ooo0oo0o0oo + IIIIi1i
elif iI1i1IiIIIIi == 1018 :
 ooO0oooOO0 ( IiI111111IIII )
 if 78 - 78: O0O0OoOO0
elif iI1i1IiIIIIi == 1023 :
 O0o0O0OO00o ( )
 if 29 - 29: IIiIiII11i
elif iI1i1IiIIIIi == 1024 :
 iII11iI1iiIIi ( IiI111111IIII )
 if 79 - 79: iI11I1II1I1I - Ii + OO0 - IIiIiII11i . iI11I1II1I1I
elif iI1i1IiIIIIi == 1025 :
 I1II1iIi ( IiI111111IIII )
 if 84 - 84: I1ii11iIi11i % oO0o0OOOO * o0o00Oo0O * oO0o0OOOO
elif iI1i1IiIIIIi == 4001 :
 iI1Ii11iIiI1 ( )
 if 66 - 66: O0OoO / iI11I1II1I1I - OOooOOo % o0o00Oo0O . OO0
elif iI1i1IiIIIIi == 4002 :
 oOOoo00O00o ( )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif iI1i1IiIIIIi == 4003 :
 IIiI1I1 ( )
 if 37 - 37: ooOoO0O00 * Ii
elif iI1i1IiIIIIi == 4004 :
 I11iI1i1I11I11 ( )
 if 95 - 95: Ii % iii1iiii1 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif iI1i1IiIIIIi == 4005 :
 iI1111ii1I ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / O0OoO / iii1iiii1
elif iI1i1IiIIIIi == 4006 :
 I11I ( )
 if 35 - 35: IIIIi1i * O0OoO
elif iI1i1IiIIIIi == 4007 :
 oOoo0oOo00 ( )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif iI1i1IiIIIIi == 4008 :
 IiiiIiii11 ( )
 if 13 - 13: oO0o * iii1iiii1 + I1ii11iIi11i - ooo0oo0o0oo
elif iI1i1IiIIIIi == 4009 : o000O0O ( )
elif iI1i1IiIIIIi == 4010 : O00O0Ooooo00 ( )
elif iI1i1IiIIIIi == 3000 :
 I1iI1 ( )
 if 31 - 31: oO0o
elif iI1i1IiIIIIi == 3001 :
 O0O0 ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif iI1i1IiIIIIi == 3002 :
 oO0oo ( IiI111111IIII )
 if 77 - 77: Ii - iii1iiii1 . Ii1I % I1ii11iIi11i . O0O0OoOO0
elif iI1i1IiIIIIi == 3003 :
 o00o0o000Oo ( IiI111111IIII )
 if 9 - 9: I11i
elif iI1i1IiIIIIi == 3004 :
 iIiII ( IiI111111IIII )
 if 55 - 55: O0OoO % iI11I1II1I1I + oO0o0OOOO . OO0
elif iI1i1IiIIIIi == 404 :
 I1I11Oo0 ( Iii1IIII11I , IiI111111IIII , iII1 )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif iI1i1IiIIIIi == 405 :
 I1iI1111ii1I1 ( IiI111111IIII )
 if 23 - 23: Ii
elif iI1i1IiIIIIi == 7030 :
 I1ii1i11iI1 ( )
 if 88 - 88: IIiIiII11i - IIIIi1i / ii
elif iI1i1IiIIIIi == 7021 :
 Ooi1IIii1i ( Iii1IIII11I )
 if 71 - 71: Ii1I
elif iI1i1IiIIIIi == 7022 :
 ii1Io0oOO0 ( Iii1IIII11I )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif iI1i1IiIIIIi == 7000 :
 I1Io0oO00O ( Iii1IIII11I , IiI111111IIII , img )
 if 1 - 1: ooo0oo0o0oo % ooOoO0O00
elif iI1i1IiIIIIi == 7050 :
 Ii1II ( IiI111111IIII )
 if 41 - 41: oO0o * oO0o / IIIIi1i + Ii1I . I11i
elif iI1i1IiIIIIi == 7051 :
 I1111111 ( IiI111111IIII )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / O0O0OoOO0
elif iI1i1IiIIIIi == 7052 :
 I1I11 ( IiI111111IIII )
 if 80 - 80: Ii1I
elif iI1i1IiIIIIi == 7053 :
 iI1i1iI1iI ( IiI111111IIII )
 if 67 - 67: IIiIiII11i
elif iI1i1IiIIIIi == 7054 :
 CoolPlay ( IiI111111IIII )
 if 2 - 2: I11i - o0o00Oo0O * O0O0OoOO0 % ooo0oo0o0oo
elif iI1i1IiIIIIi == 7060 :
 oOoo00 ( )
 if 64 - 64: ooOoO0O00 . OO0
elif iI1i1IiIIIIi == 7061 :
 ooOOooO0OoO ( IiI111111IIII )
 if 7 - 7: IIIi . IIIIi1i - IIIIi1i / iii1iiii1 % I1ii11iIi11i
elif iI1i1IiIIIIi == 7063 :
 IIiIi ( IiI111111IIII )
 if 61 - 61: IIIi - Ii1I / IIIIi1i % Ii1I + oO0o / I1ii11iIi11i
elif iI1i1IiIIIIi == 7062 :
 iiII ( IiI111111IIII )
 if 10 - 10: Ii / OOooOOo
elif iI1i1IiIIIIi == 7064 :
 NATatozcat ( )
 if 27 - 27: oOo0O0Ooo / ii
elif iI1i1IiIIIIi == 7067 :
 iII1IiiIIIIii ( IiI111111IIII )
 if 74 - 74: Ii1I % iii1iiii1 - oO0o * oO0o0OOOO . ii * oO0o
elif iI1i1IiIIIIi == 7066 :
 NATatozA ( IiI111111IIII )
 if 99 - 99: OOooOOo . IIIIi1i - ii - o0o00Oo0O
elif iI1i1IiIIIIi == 7065 :
 oOOO ( IiI111111IIII )
 if 6 - 6: O0OoO
elif iI1i1IiIIIIi == 7070 :
 OooOoO ( )
 if 3 - 3: o0o00Oo0O - iii1iiii1 * O0O0OoOO0 * O0OoO / O0O0OoOO0
elif iI1i1IiIIIIi == 7071 :
 DIZIlist ( IiI111111IIII )
 if 58 - 58: O0O0OoOO0 * iI11I1II1I1I + OO0 . OO0
elif iI1i1IiIIIIi == 7072 :
 DIZIpull ( IiI111111IIII )
 if 74 - 74: OO0 - I11i * ooo0oo0o0oo % OO0
elif iI1i1IiIIIIi == 7073 :
 WATCHDIZI ( IiI111111IIII )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * iii1iiii1 - oO0o - I11i
elif iI1i1IiIIIIi == 7002 :
 o0oo0o ( )
 if 44 - 44: ii
elif iI1i1IiIIIIi == 7003 :
 iIioO00O0o0oOOO ( IiI111111IIII )
 if 82 - 82: OOooOOo . OOooOOo
elif iI1i1IiIIIIi == 7004 :
 oooOoO0oo0o0 ( IiI111111IIII )
 if 10 - 10: I1ii11iIi11i * Ii1I . IIIi . ii . O0OoO * Ii1I
elif iI1i1IiIIIIi == 7020 :
 o0ooo0oooO ( IiI111111IIII )
 if 80 - 80: iii1iiii1 + oO0o0OOOO . iii1iiii1 + O0OoO
elif iI1i1IiIIIIi == 7001 :
 IIi1iI1i ( )
 if 85 - 85: Ii . oO0o0OOOO + O0O0OoOO0 / O0O0OoOO0
elif iI1i1IiIIIIi == 7010 :
 OOO0O ( IiI111111IIII )
 if 43 - 43: ooo0oo0o0oo . ii - IIiIiII11i
elif iI1i1IiIIIIi == 7011 :
 OooOOoO00OO00 ( IiI111111IIII )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O0OoO * IIIi
elif iI1i1IiIIIIi == 7012 :
 o0oo000 ( IiI111111IIII )
 if 19 - 19: iii1iiii1 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif iI1i1IiIIIIi == 7013 :
 cnfTVPlay2 ( IiI111111IIII )
elif iI1i1IiIIIIi == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IiI111111IIII )
elif iI1i1IiIIIIi == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IiI111111IIII )
elif iI1i1IiIIIIi == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Iii1IIII11I , IiI111111IIII , iII1 )
elif iI1i1IiIIIIi == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iI1i1IiIIIIi == 7018 :
 I1iiII1 ( )
elif iI1i1IiIIIIi == 7019 :
 CNF_Studio_Indexer . List_Movies ( IiI111111IIII )
elif iI1i1IiIIIIi == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IiI111111IIII )
elif iI1i1IiIIIIi == 7024 :
 CNF_Studio_Indexer . Box_Office ( IiI111111IIII )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif iI1i1IiIIIIi == 8000 :
 iIIII1Iii11 ( )
elif iI1i1IiIIIIi == 8001 :
 Ooooo00 ( )
elif iI1i1IiIIIIi == 8002 :
 i11i111 ( )
elif iI1i1IiIIIIi == 8003 :
 ooo000o ( )
elif iI1i1IiIIIIi == 8004 :
 o00OIIIIII1iI1II ( )
elif iI1i1IiIIIIi == 8005 :
 o000Ooo00o00O ( )
elif iI1i1IiIIIIi == 8006 :
 iI1I1ii11IIi1 ( Iii1IIII11I , IiI111111IIII )
elif iI1i1IiIIIIi == 8030 :
 IIIII1iii11 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8045 :
 OOOooO00OO00O ( IiI111111IIII )
elif iI1i1IiIIIIi == 8046 :
 OoOOooO0O ( IiI111111IIII )
elif iI1i1IiIIIIi == 8047 :
 Ii1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8048 :
 OO0OooOo ( IiI111111IIII )
elif iI1i1IiIIIIi == 8049 :
 ii111iI1i1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8020 :
 I111I ( )
elif iI1i1IiIIIIi == 8021 :
 oooO ( IiI111111IIII )
elif iI1i1IiIIIIi == 8022 :
 oo0OOoOo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8023 :
 oO00oO0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8040 :
 OOO00o0 ( )
elif iI1i1IiIIIIi == 8041 :
 ooIi111iII ( IiI111111IIII )
elif iI1i1IiIIIIi == 8042 :
 IIi1ii ( IiI111111IIII )
elif iI1i1IiIIIIi == 8043 :
 yt . PlayVideo ( IiI111111IIII )
elif iI1i1IiIIIIi == 8044 :
 Ii1i1i ( IiI111111IIII )
elif iI1i1IiIIIIi == 8060 :
 II1iIiiiI1 ( )
elif iI1i1IiIIIIi == 8061 :
 I1IIIi ( IiI111111IIII )
elif iI1i1IiIIIIi == 8064 :
 Ii1iiIi11111I ( )
elif iI1i1IiIIIIi == 8065 :
 OOOOoO ( IiI111111IIII )
elif iI1i1IiIIIIi == 8070 :
 iii1 ( )
elif iI1i1IiIIIIi == 8071 :
 O0Ooo0O ( IiI111111IIII )
elif iI1i1IiIIIIi == 7080 :
 iii1oOo0OoOOOo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8090 :
 O0oo0oOo ( )
elif iI1i1IiIIIIi == 8091 :
 i111iI1i1iI ( IiI111111IIII )
elif iI1i1IiIIIIi == 8092 :
 OO0O0OO0O0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8093 :
 IiiI1i111I1i ( IiI111111IIII )
elif iI1i1IiIIIIi == 8081 :
 OoOiII11IiIi ( )
elif iI1i1IiIIIIi == 8062 :
 iII1I ( IiI111111IIII )
elif iI1i1IiIIIIi == 8063 :
 iiIi ( IiI111111IIII )
elif iI1i1IiIIIIi == 8050 :
 iiIi1I1i1 ( )
elif iI1i1IiIIIIi == 8051 :
 OOOIiIi1111ii ( IiI111111IIII )
elif iI1i1IiIIIIi == 8052 :
 iI1I1II1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 8085 :
 O00Ooo0O0OOOo ( )
elif iI1i1IiIIIIi == 8086 :
 iIIIiIi1i ( IiI111111IIII )
elif iI1i1IiIIIIi == 8087 :
 IiIIIiI ( IiI111111IIII )
elif iI1i1IiIIIIi == 8088 :
 II1iI1iiiI ( IiI111111IIII , Iii1IIII11I )
elif iI1i1IiIIIIi == 9000 :
 OO00oOooo0O ( )
elif iI1i1IiIIIIi == 1111 :
 i1II1i1iiI1 ( )
elif iI1i1IiIIIIi == 9001 :
 I1IIIiOoOooOo00O ( )
elif iI1i1IiIIIIi == 9002 :
 O0O0Oo00OO ( )
elif iI1i1IiIIIIi == 9003 :
 i1i1i11iI11II ( )
elif iI1i1IiIIIIi == 50 :
 ooO0o ( IiI111111IIII )
elif iI1i1IiIIIIi == 9020 :
 champlist ( )
elif iI1i1IiIIIIi == 9021 :
 Oo00oo00o00Oo ( )
elif iI1i1IiIIIIi == 9022 :
 iiiiiii11III ( )
elif iI1i1IiIIIIi == 9023 :
 I11111ii1i ( )
elif iI1i1IiIIIIi == 9024 :
 iI11IiiiIII ( IiI111111IIII )
elif iI1i1IiIIIIi == 9030 :
 oooIi1II1I11i1I ( IiI111111IIII )
elif iI1i1IiIIIIi == 9031 :
 OOoOo ( IiI111111IIII )
elif iI1i1IiIIIIi == 9032 :
 Iiiiiii11IIiI ( IiI111111IIII )
elif iI1i1IiIIIIi == 9033 :
 oOOO0o ( IiI111111IIII )
elif iI1i1IiIIIIi == 7085 :
 o0ooOOOO0O0o ( IiI111111IIII )
elif iI1i1IiIIIIi == 7086 :
 III1iI1Ii11Ii ( IiI111111IIII )
elif iI1i1IiIIIIi == 7087 :
 o00o0 ( i1i11I1I1iii1 )
elif iI1i1IiIIIIi == 9666 :
 oOO00OO0ooo0o ( IiI111111IIII )
elif iI1i1IiIIIIi == 10100 : O00o0OO0OO0oo ( )
elif iI1i1IiIIIIi == 10105 : ooo0I11 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10106 : o0oi1I1I1I ( IiI111111IIII )
elif iI1i1IiIIIIi == 10104 : ii11i1I1i ( IiI111111IIII )
elif iI1i1IiIIIIi == 10107 : IIOO ( )
elif iI1i1IiIIIIi == 10103 : o0OoooO ( IiI111111IIII )
elif iI1i1IiIIIIi == 10108 : IiIiiI1ii111 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10107 : IIOO ( )
elif iI1i1IiIIIIi == 10000 : Origin_Menu ( )
elif iI1i1IiIIIIi == 10001 : OOoooOoO0Oo ( )
elif iI1i1IiIIIIi == 10002 : iIIiiiI1iI1 ( )
elif iI1i1IiIIIIi == 10003 : i1i111Iiiiiii ( )
elif iI1i1IiIIIIi == 10004 : O00o ( IiI111111IIII )
elif iI1i1IiIIIIi == 10005 : i11i11 ( )
elif iI1i1IiIIIIi == 10006 : oO0OoooO0oOO00OoOo ( IiI111111IIII )
elif iI1i1IiIIIIi == 10007 : Oo0oOo0ooOOOo ( IiI111111IIII , iII1 )
elif iI1i1IiIIIIi == 10008 : I1iIi1iIIIIiI ( )
elif iI1i1IiIIIIi == 10009 : II11ii1I11 ( )
elif iI1i1IiIIIIi == 10010 : Oo0O0OO0OoO0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10011 : I1I1i ( IiI111111IIII )
elif iI1i1IiIIIIi == 10012 : oO000o ( IiI111111IIII )
elif iI1i1IiIIIIi == 10109 : ii1IO0oo00o000 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10013 : o00OOo0o0O ( IiI111111IIII )
elif iI1i1IiIIIIi == 10014 : oO00IiI1II11iiI ( )
elif iI1i1IiIIIIi == 10015 : II1Ii ( )
elif iI1i1IiIIIIi == 10016 : OO0ooo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10017 : O0Oo0 ( )
elif iI1i1IiIIIIi == 10018 : i11i1i ( )
elif iI1i1IiIIIIi == 10019 : I111I1I ( )
elif iI1i1IiIIIIi == 10020 : Iii1i11iiI1 ( )
elif iI1i1IiIIIIi == 10021 : oOoOoO0o0 ( )
elif iI1i1IiIIIIi == 10022 : iI1ii ( IiI111111IIII )
elif iI1i1IiIIIIi == 10023 : oooOoO ( Iii1IIII11I , IiI111111IIII )
elif iI1i1IiIIIIi == 10024 : o0oOo00 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10025 : IIiI11I1I1i1i ( )
elif iI1i1IiIIIIi == 10026 : ooOoooo0 ( )
elif iI1i1IiIIIIi == 10027 : i1i ( )
elif iI1i1IiIIIIi == 10028 : i1I1iIoOOoO ( )
elif iI1i1IiIIIIi == 10029 : I1Iii1Ii1i1 ( )
elif iI1i1IiIIIIi == 423 : o0oO00 ( IiI111111IIII )
elif iI1i1IiIIIIi == 426 : oOOoOOO0oo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10030 : Izle_Films ( )
elif iI1i1IiIIIIi == 10031 : Latest_Izle_Movies ( )
elif iI1i1IiIIIIi == 10032 : Izle_Genres ( )
elif iI1i1IiIIIIi == 10033 : Izle_Pop_Movies ( )
elif iI1i1IiIIIIi == 10034 : Izle_Boxsets ( )
elif iI1i1IiIIIIi == 10035 : Izle_Search ( )
elif iI1i1IiIIIIi == 10036 : Izle_Genres_Movie ( IiI111111IIII )
elif iI1i1IiIIIIi == 10037 : Izle_Boxset_single ( IiI111111IIII )
elif iI1i1IiIIIIi == 10038 : Izle_IFRAME ( )
elif iI1i1IiIIIIi == 10039 : Izle_Boxsets_Next ( IiI111111IIII )
elif iI1i1IiIIIIi == 10040 : oO0O0o0O ( )
elif iI1i1IiIIIIi == 10041 : II111I1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10042 : IIiiI ( IiI111111IIII )
elif iI1i1IiIIIIi == 10043 : i11IiI ( )
elif iI1i1IiIIIIi == 10044 : IIi1i1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10045 : i1i1iIII11i ( Iii1IIII11I )
elif iI1i1IiIIIIi == 10046 : OOOOOO ( IiI111111IIII )
elif iI1i1IiIIIIi == 10047 : I11io0Oo ( IiI111111IIII )
elif iI1i1IiIIIIi == 10048 : Iiiii11IIii ( IiI111111IIII )
elif iI1i1IiIIIIi == 10049 : O0oo00oOOO0o ( IiI111111IIII )
elif iI1i1IiIIIIi == 10050 : III1I11II11I ( )
elif iI1i1IiIIIIi == 10051 : I1iIi1IiI1i ( )
elif iI1i1IiIIIIi == 10052 : iI1111iiI1 ( )
elif iI1i1IiIIIIi == 10053 : Addon ( IiI111111IIII )
elif iI1i1IiIIIIi == 10054 : IIIiI1i ( IiI111111IIII , Iii1IIII11I )
elif iI1i1IiIIIIi == 10055 :
 o00oo0OO0 ( "addFavorite" )
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 O000O ( Iii1IIII11I , IiI111111IIII , iII1 , oO0o0 , iiIi1iIiI )
elif iI1i1IiIIIIi == 10056 :
 o00oo0OO0 ( "rmFavorite" )
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 IiI1iiI11 ( Iii1IIII11I )
elif iI1i1IiIIIIi == 10057 :
 o00oo0OO0 ( "getFavorites" )
 ii1iIII ( )
elif iI1i1IiIIIIi == 10058 : I1i1i1iii ( )
elif iI1i1IiIIIIi == 10059 : Donators_Guide ( )
elif iI1i1IiIIIIi == 10060 : Ii1ii111i1 ( )
elif iI1i1IiIIIIi == 10061 : ii1Ii1IiIIi ( )
elif iI1i1IiIIIIi == 10062 : iI1IIIii ( Iii1IIII11I , IiI111111IIII , i1i11I1I1iii1 )
elif iI1i1IiIIIIi == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + ooooooO0oo + ")" )
elif iI1i1IiIIIIi == 10064 : IIIIi1 ( )
elif iI1i1IiIIIIi == 10065 : iIiiii ( IiI111111IIII )
elif iI1i1IiIIIIi == 10066 : O0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10068 : ooOOo00O00Oo ( IiI111111IIII )
elif iI1i1IiIIIIi == 10069 : OO0oOOoo ( IiI111111IIII )
elif iI1i1IiIIIIi == 10070 : oOOO0oo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10071 : Genie_Watch ( )
elif iI1i1IiIIIIi == 10072 : o0oo0 ( )
elif iI1i1IiIIIIi == 10073 : OOOO0OOO ( IiI111111IIII )
elif iI1i1IiIIIIi == 10074 : O00Ooo ( IiI111111IIII )
elif iI1i1IiIIIIi == 10075 : III1I1Iii1iiI ( iII1 , Iii1IIII11I , IiI111111IIII )
elif iI1i1IiIIIIi == 10076 : I1ii1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10077 : IiIiII1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 10078 : iIiIII1I1I1 ( )
elif iI1i1IiIIIIi == 10079 : Genie_Watch_Tv_Shows ( )
elif iI1i1IiIIIIi == 10080 : Genie_Watch_Tv_Genre ( IiI111111IIII )
elif iI1i1IiIIIIi == 10081 : Genie_Watch_TV_PlayRun ( IiI111111IIII )
elif iI1i1IiIIIIi == 10082 : Genie_Watch_TV_Episodes ( IiI111111IIII , iII1 )
elif iI1i1IiIIIIi == 10083 : Genie_Watch_Tv_Recent ( IiI111111IIII )
elif iI1i1IiIIIIi == 10084 : I1Ii1iiiiii1 ( )
elif iI1i1IiIIIIi == 10085 : o0O0OOO0Ooo ( )
elif iI1i1IiIIIIi == 10086 : ooOOOoO ( )
elif iI1i1IiIIIIi == 20000 : o00ooo0 ( )
elif iI1i1IiIIIIi == 20001 : iIiIi1iI11iiI ( )
elif iI1i1IiIIIIi == 20002 : III1II111Ii1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 20003 : OO0iIiiIi11IIi ( IiI111111IIII )
elif iI1i1IiIIIIi == 20004 : Iio00 ( IiI111111IIII )
elif iI1i1IiIIIIi == 21004 : II1 ( )
elif iI1i1IiIIIIi == 21005 : I11Iii1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 21006 : III1Ii1i1I1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 21007 : iiO0O0o0oO0O00 ( IiI111111IIII )
elif iI1i1IiIIIIi == 30000 : iIi1iIIIiIiI ( )
elif iI1i1IiIIIIi == 30001 : o0IiiiI111I ( )
elif iI1i1IiIIIIi == 10012 : Resolve ( IiI111111IIII )
elif iI1i1IiIIIIi == 30003 : i1iIIi1o0o0OoOOOOOo ( )
elif iI1i1IiIIIIi == 30004 : III1I1 ( IiI111111IIII )
elif iI1i1IiIIIIi == 30005 : o0i1iI1iiI1I ( IiI111111IIII )
elif iI1i1IiIIIIi == 30006 : ii1ii ( )
elif iI1i1IiIIIIi == 30007 : iI11Ii111 ( )
elif iI1i1IiIIIIi == 30008 : IiI1IIIII1I ( IiI111111IIII )
elif iI1i1IiIIIIi == 30009 : I1III111i ( IiI111111IIII )
elif iI1i1IiIIIIi == 30010 : Oo0O0Oo00O ( IiI111111IIII )
elif iI1i1IiIIIIi == 30011 : OOO0 ( )
elif iI1i1IiIIIIi == 30012 : Ii1iI ( )
elif iI1i1IiIIIIi == 30013 : oO00 ( )
elif iI1i1IiIIIIi == 30014 : o00ii111Iiii ( )
elif iI1i1IiIIIIi == 30015 : oOoOo00ooOooo ( IiI111111IIII , iII1 , oO0o0 )
elif iI1i1IiIIIIi == 30016 : OOoO00oo0000O ( IiI111111IIII )
elif iI1i1IiIIIIi == 30019 : IIiiiiIiIIii ( IiI111111IIII )
elif iI1i1IiIIIIi == 30017 : I1ii1II1iII ( IiI111111IIII )
elif iI1i1IiIIIIi == 30018 : o00ooo ( IiI111111IIII )
elif iI1i1IiIIIIi == 30030 : oOo0OO0o0 ( )
elif iI1i1IiIIIIi == 30031 : II1I1I ( )
elif iI1i1IiIIIIi == 30032 : III11I ( )
elif iI1i1IiIIIIi == 30033 : i1o0oo0 ( )
elif iI1i1IiIIIIi == 30034 : OoO0OOoO0Oo0 ( )
elif iI1i1IiIIIIi == 30035 : Iiiii1io00O00o ( IiI111111IIII )
elif iI1i1IiIIIIi == 30036 : O0o0OO ( IiI111111IIII )
elif iI1i1IiIIIIi == 30037 : iI1iii ( IiI111111IIII )
elif iI1i1IiIIIIi == 30038 : I1iiiiii ( )
elif iI1i1IiIIIIi == 30039 : IiiIi1IIII1i ( )
elif iI1i1IiIIIIi == 50000 : i1I1ii11i1Iii ( )
elif iI1i1IiIIIIi == 50001 : IIioo0OO ( )
elif iI1i1IiIIIIi == 50002 : O0oO0o0OOOOOO ( IiI111111IIII )
elif iI1i1IiIIIIi == 50003 : i1I111II ( i1i11I1I1iii1 )
elif iI1i1IiIIIIi == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif iI1i1IiIIIIi == 60001 : ii111I11iI ( )
elif iI1i1IiIIIIi == 60002 : OOO ( Iii1IIII11I )
elif iI1i1IiIIIIi == 60003 : Ooooooo ( Iii1IIII11I )
elif iI1i1IiIIIIi == 50004 : iI1i11iII111 ( )
elif iI1i1IiIIIIi == 50005 : speedtest . runtest ( IiI111111IIII )
elif iI1i1IiIIIIi == 70001 : I1iiIII ( )
elif iI1i1IiIIIIi == 70002 : O00oOoo0OoO0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 70003 : Ooo0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 70004 : oooO00o0 ( IiI111111IIII )
elif iI1i1IiIIIIi == 70005 : o0o00oO0oo000 ( IiI111111IIII )
elif iI1i1IiIIIIi == 70006 : o0Oo ( )
elif iI1i1IiIIIIi == 50006 : ii1I ( i1 , i1111 )
elif iI1i1IiIIIIi == 80000 : OOO0o ( )
if 15 - 15: O0O0OoOO0 + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
if 54 - 54: ooo0oo0o0oo - IIiIiII11i . OO0 + O0O0OoOO0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
