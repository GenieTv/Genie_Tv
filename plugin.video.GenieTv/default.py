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
IiiIII111iI = "3.1.3"
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
 if 98 - 98: O0OoO + ooo0oo0o0oo + IIIi % ii
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']TV GUIDE[/COLOR]' , '' , 10063 , i11i1I1 + 'TvGuide.png' , ooOoOoo0O , '' )
  if 97 - 97: o0o00Oo0O * ii . ii
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
  if 33 - 33: iii1iiii1 + IIIIi1i * IIIi / iI11I1II1I1I - oOo0O0Ooo
  if 54 - 54: iii1iiii1 / O0OoO . IIIi % IIIIi1i
 if oo00 . getSetting ( 'Playlist Loader' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']PLAYLIST LOADER[/COLOR]' , str ( I1I1iIiII1 ) , 3000 , i11i1I1 + 'PlaylistLoader.png' , ooOoOoo0O , '' )
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
  if 77 - 77: O0OoO * iI11I1II1I1I
 oOooOo0 ( 'movies' , 'MAIN' )
 if 98 - 98: oOo0O0Ooo % O0O0OoOO0 * ii
def i1Iii1i1I ( ) :
 if not os . path . exists ( O00o0OO ) :
  ii1I ( 'Change Log 5/9/16 - v3.1.0' , 'GenieTv now clears cache on every start-up, Force close on all platforms Android included, RaysRavers added to music section, RadioNomy section added to music, Quicksilver fixed in music, WatchSeries fixed now playing from genres, Go fishing work in progress, View log file from within maintenance, Speedtest added to maintenance section, GenieTv contact information within addon, Search tweaked performing faster and more sources, Tv theme tunes section added to music, new servers online' )
  os . makedirs ( O00o0OO )
  if 51 - 51: iI11I1II1I1I . OOooOOo / IIIi + I11i
  if 33 - 33: OO0 . IIiIiII11i % IIIIi1i + I11i
def oO00O000oO0 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH MOVIES[/COLOR]' , str ( I1I1iIiII1 ) , 9001 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']POPCORN BOX[/COLOR]' , str ( I1I1iIiII1 ) , 7061 , i11i1I1 + 'PopcornBox.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Film Trailers[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , i11i1I1 + 'FilmTrailers.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , i11i1I1 + 'ClassicMovies.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
def O0OoOO0o ( ) :
 iI1iiIiiII ( )
 ooooo0O0000oo ( )
 if 21 - 21: I11i - oOo0O0Ooo
 if 18 - 18: I1ii11iIi11i + oO0o0OOOO % O0OoO - ii - Ii1I / ooOoO0O00
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live Sport On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']TV GUIDE[/COLOR]' , '' , 10063 , i11i1I1 + 'TvGuide.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']Link GTV to Guide[/COLOR]' , '' , 4010 , i11i1I1 + 'linkchannels.png' , ooOoOoo0O , '' )
def oo0oO ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Lists[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL2Rvd25sb2FkLnByb2dkdmIuY29tL3R2c3QvU2x5TmV0LnR2c3Q=' ) , 9030 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Find Me A Stream[/COLOR]' , '' , 9003 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']World IPTV[/COLOR]' , '' , 9004 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']World IPTV 2[/COLOR]' , '' , 9007 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Iptv Lists[/COLOR]' , '' , 9010 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 if 94 - 94: iI11I1II1I1I / I1ii11iIi11i % IIIIi1i * IIIIi1i * IIiIiII11i
 if 29 - 29: oO0o + OOooOOo / I11i / O0OoO * iI11I1II1I1I
def O0OO ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH SERIES[/COLOR]' , str ( I1I1iIiII1 ) , 9002 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if 6 - 6: iI11I1II1I1I % Ii % Ii1I
 if 93 - 93: ooo0oo0o0oo * ii + OO0
 if oo00 . getSetting ( 'Watch Series' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']WATCH SERIES[/COLOR]' , '' , 10040 , i11i1I1 + 'WatchSeries.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']iWATCH SERIES[/COLOR]' , '' , 8020 , i11i1I1 + 'iWatchSeries.png' , ooOoOoo0O , '' )
 if 33 - 33: o0o00Oo0O * I11i - iii1iiii1 % iii1iiii1
 if 18 - 18: iii1iiii1 / I1ii11iIi11i * iii1iiii1 + iii1iiii1 * Ii * Ii1I
 if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CLASSIC TV[/COLOR]' , str ( I1I1iIiII1 ) , 8064 , i11i1I1 + 'ClassicTV.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']TV Show Trailers[/COLOR]' , i1iiIII111ii ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , i11i1I1 + 'TVShowTrailers.png' , ooOoOoo0O , '' )
 if 11 - 11: OO0 / OOooOOo - ooo0oo0o0oo * ii + ii . OOooOOo
 oOooOo0 ( 'movies' , 'MAIN' )
def i1I1i111Ii ( ) :
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
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
 oOooOo0 ( 'movies' , 'MAIN' )
 if 27 - 27: OO0 % oOo0O0Ooo
def o0oooOO00 ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']SILENT HUNTER[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SERVER 1[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SERVER 2[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , i11i1I1 + 'SilentHunter.png' , ooOoOoo0O , '' )
def iiIiii1IIIII ( url ) :
 o00o = IIIIiiIiiI ( url )
 url = url
 i1I1i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( o00o )
 for IIIIiI11I11 , oo00o0 in i1I1i :
  if '[DIR]' in IIIIiI11I11 :
   i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 1018 , i11i1I1 + 'SilentHunter.png' )
  if 'mkv' in oo00o0 :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 222 , i11i1I1 + 'SilentHunter.png' )
  if 'avi' in oo00o0 :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 222 , i11i1I1 + 'SilentHunter.png' )
   if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + oO0o0OOOO * iI11I1II1I1I
def o0ooooO0o0O ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HEROVISION[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , i11i1I1 + 'Herovision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HEROVISION SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , i11i1I1 + 'Herovision.png' , ooOoOoo0O , '' )
 if 24 - 24: o0o00Oo0O * I11i
def IiI1iiiIii ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , i11i1I1 + 'SearchCartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'WCO' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1iIiII1 ) , 21004 , i11i1I1 + 'watchcartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Cartoons' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CARTOONS[/COLOR]' , '' , 10001 , i11i1I1 + 'Cartoons.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'Anime' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']AnimeLand[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , i11i1I1 + 'anime.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
def I1III1111iIi ( ) :
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
 if 38 - 38: IIIIi1i + oO0o0OOOO / iii1iiii1 % OO0 - Ii1I
 if 14 - 14: IIIi / iii1iiii1
 if 85 - 85: oO0o0OOOO
def iiIiI ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1I1i = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIi1i11111 )
 for IIIi11I1 in i1I1i :
  IIIi11I1 = ( str ( IIIi11I1 ) )
  if os . path . exists ( xbmc . translatePath ( IIIi11I1 ) ) :
   iI1i11II1i = ( IIIi11I1 ) . replace ( 'special://home/addons/' , '' )
   ii1I ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iI1i11II1i + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   o0o0OoOo0O0OO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if o0o0OoOo0O0OO == 0 :
    iIi1I11I ( IIIi11I1 )
    Iii1 ( )
   elif o0o0OoOo0O0OO == 1 :
    ooO ( IIIi11I1 )
  else :
   pass
   if 84 - 84: O0OoO - IIIIi1i / OO0
def ooO ( addon ) :
 iI1i11II1i = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 65 - 65: O0O0OoOO0 / oO0o0OOOO / OOooOOo
def iIi1I11I ( addon ) :
 oooOOOOO . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Ooo0000O0 = os . path . join ( O0O , 'default.py' )
 IIIIIIiIiIi1 = open ( Ooo0000O0 , "w+" )
 if 2 - 2: IIIIi1i % iI11I1II1I1I * iI11I1II1I1I . I11i / IIIIi1i
 IIIIIIiIiIi1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 IIIIIIiIiIi1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 IIIIIIiIiIi1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 27 - 27: oO0o + OO0 - ooOoO0O00
 if 69 - 69: ooo0oo0o0oo - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
 if 79 - 79: o0o00Oo0O * Ii - ooo0oo0o0oo / ooo0oo0o0oo
 if 48 - 48: o0o00Oo0O
 if 93 - 93: Ii - oOo0O0Ooo * Ii1I * oO0o0OOOO % o0o00Oo0O + ii
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
 if 98 - 98: oOo0O0Ooo
 if 95 - 95: OO0 / OO0
 if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
 if 55 - 55: OO0 - oO0o0OOOO + IIiIiII11i + IIIIi1i % O0O0OoOO0
def iiI11i1II ( ) :
 iiIi1IIi1I ( 'Genre' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Most Viewed' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Box Office' , i1iiIII111ii ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Search' , '' , 10078 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
 if 51 - 51: I11i % I1ii11iIi11i % I11i * o0o00Oo0O - O0OoO % I1ii11iIi11i
def o0O00OooOOOOO ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIII1i = 'http://imoviemax.se/?s=' + ( IIIiiI1i1 ) . replace ( ' ' , '+' )
 I1I = iiIII1i . lower ( )
 ooooO0oOoOOoO ( I1I )
def I1i11i ( url ) :
 IiIi = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , OOOOO0O00 in i1I1i :
  if Iii1IIII11I in IiIi :
   pass
  else :
   iiIi1IIi1I ( Iii1IIII11I + ' - ' + OOOOO0O00 + ' Films' , url , 10074 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
   IiIi . append ( Iii1IIII11I )
   if 30 - 30: iI11I1II1I1I . oOo0O0Ooo . O0OoO / I11i
def iiI1I1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , ooOii in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I + ' - Views:' + ooOii , url , 10075 , i11i1I1 + 'genievision.png' , ooOoOoo0O , '' )
  if 82 - 82: OOooOOo - oO0o % OOooOOo * Ii . IIiIiII11i % IIiIiII11i
  if 54 - 54: oO0o0OOOO + O0O0OoOO0
def ooooO0oOoOOoO ( url ) :
 o00I1 = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIi1i11111 )
 for next in next :
  iiIi1IIi1I ( 'NEXT PAGE' , next , 10074 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 i1I1i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , Iii1IIII11I , url in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 10075 , O00 , O00 , '' )
  o00I1 . append ( Iii1IIII11I )
  if 30 - 30: oOo0O0Ooo + oO0o % O0O0OoOO0 * IIIIi1i / I1ii11iIi11i - oO0o0OOOO
def ooo ( img , name , url ) :
 img = img
 name = name
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIi1i11111 )
 for iIi1i , url in i1I1i :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1i11111i1i11 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1i11111i1i11
  OOoOOO0 = ( iIi1i ) . replace ( 'play-' , 'Server ' )
  i1I1iI1iIi111i ( OOoOOO0 , I1i11111i1i11 , 10076 , img , img , '' )
  if 10 - 10: iii1iiii1 / OO0 + Ii / O0O0OoOO0
def OOOoOoO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIi1i11111 )
 for oo00o0 in i1I1i :
  if '=m' in oo00o0 :
   iIIIII1ii1I ( oo00o0 )
  elif 'php' in oo00o0 :
   OOOoOoO ( url )
  else :
   IIi1i11111 = O000OOo00oo ( oo00o0 )
   i1I1i = re . compile ( 'content="([^"]*)">' ) . findall ( IIi1i11111 )
   for Ii1i1iI in i1I1i :
    iIIIII1ii1I ( oo00o0 )
    if 16 - 16: O0OoO / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % O0OoO
    if 71 - 71: OOooOOo
    if 14 - 14: Ii % O0OoO
def OooO0oo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 o0o0oOoOO0O = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for i1ii1II1ii , iII111Ii in o0o0oOoOO0O :
  print 'there ><><><><><><><><><><><><'
  i1ii1II1ii = i1ii1II1ii
  i1I1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iII111Ii ) )
  for Iii1IIII11I , Ooo00OoOOO in i1I1i :
   print 'here <><><><><><><><><><><><>'
   iiIi1IIi1I ( '[COLORred]' + i1ii1II1ii + '[/COLOR] - ' + Iii1IIII11I + ' - [COLOR' + iIii1 + ']' + Ooo00OoOOO + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i11i1I1 + 'loader.png' , ooOoOoo0O , '' )
 Oo0OO0000oooo = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for i1ii1II1ii , IIII1iII in Oo0OO0000oooo :
  print 'there ><><><><><><><><><><><><'
  i1ii1II1ii = i1ii1II1ii
  i1I1i = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIII1iII ) )
  for Iii1IIII11I , Ooo00OoOOO in i1I1i :
   print 'here <><><><><><><><><><><><>'
   iiIi1IIi1I ( '[COLORred]' + i1ii1II1ii + '[/COLOR] - ' + Iii1IIII11I + ' - [COLOR' + iIii1 + ']' + Ooo00OoOOO + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , i11i1I1 + 'loader.png' , ooOoOoo0O , '' )
   if 28 - 28: ooOoO0O00 - IIIIi1i
   if 54 - 54: IIIIi1i - o0o00Oo0O % O0OoO
   if 73 - 73: o0o00Oo0O . OOooOOo + oOo0O0Ooo - oO0o0OOOO % oO0o0OOOO . oO0o0OOOO
def I11ii1i1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Oo0OO0000oooo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
 for Oo0OO0000oooo in Oo0OO0000oooo :
  Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
  for Iii1IIII11I in Iii1IIII11I :
   Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0OO0000oooo ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooo0OoOOOOO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
  for ooo0OoOOOOO in ooo0OoOOOOO :
   ooo0OoOOOOO = 'http:' + ooo0OoOOOOO
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , '' , '' )
  if 26 - 26: Ii1I
  if 73 - 73: Ii - ooo0oo0o0oo
  if 25 - 25: ii + ooo0oo0o0oo * Ii1I
  if 92 - 92: oOo0O0Ooo + oO0o0OOOO + o0o00Oo0O / I11i + iii1iiii1
def I1iIi1iIiiIiI ( url ) :
 if 47 - 47: O0O0OoOO0 + iii1iiii1 / ooOoO0O00 % Ii
 i111iI = [ ]
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIi1i11111 )
 for oo00o0 , O00 , Iii1IIII11I , OOo in i1I1i :
  Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  ooOO00O00oo = O000OOo00oo ( oo00o0 )
  Iiiii1i = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( ooOO00O00oo )
  for i1i11I1I1iii1 , I1iii11 in Iiiii1i :
   ooo0O = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1iii11 ) )
   for iII1iii in ooo0O :
    if Iii1IIII11I in i111iI :
     pass
    else :
     i1I1iI1iIi111i ( Iii1IIII11I , i1i11I1I1iii1 , 8043 , O00 , O00 , iII1iii )
     oOooOo0 ( 'movies' , 'INFO' )
     i111iI . append ( Iii1IIII11I )
     if 12 - 12: O0OoO
     if 83 - 83: IIIIi1i . o0o00Oo0O / I1ii11iIi11i / O0OoO - IIiIiII11i
def oO0oO0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , i1i1IIIIi1i , iII1iii , oO0o0 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 10065 , i1i1IIIIi1i , oO0o0 , iII1iii )
 oOooOo0 ( 'movies' , 'INFO' )
 if 7 - 7: iI11I1II1I1I + IIIIi1i * Ii / ii + IIIIi1i - I1ii11iIi11i
def Iiii ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIII1i = 'https://www.youtube.com/results?search_query=' + ( IIIiiI1i1 ) . replace ( ' ' , '+' )
 I1I = iiIII1i . lower ( )
 IIi1i11111 = O000OOo00oo ( I1I )
 i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in next :
  IiI111111IIII = 'https://www.youtube.com' + IiI111111IIII
  iiIi1IIi1I ( '[COLOR' + iIii1 + '] NEXT [/COLOR]' , IiI111111IIII , 10065 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 for O00 , IiI111111IIII , Iii1IIII11I , oooOOoooo , I1iii11 in i1I1i :
  I11II1i . append ( Iii1IIII11I )
  oOooOo0 ( 'tvshows' , 'INFO' )
  ooo0OoOOOOO = 'http:' + ( O00 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0OoOOOOO
  IiI111111IIII = 'http://www.youtube.com' + IiI111111IIII
  i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooo0OoOOOOO , I1iii11 )
 else :
  i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
  for O00 , IiI111111IIII , Iii1IIII11I , oooOOoooo in i1I1i :
   print 'im doing it'
   oOooOo0 ( 'tvshows' , 'INFO' )
   ooo0OoOOOOO = 'http:' + ( O00 ) . replace ( 'https:' , '' )
   IiI111111IIII = 'http://www.youtube.com' + IiI111111IIII
   if '&' in IiI111111IIII :
    print ' i got here'
    IIi1i11111 = O000OOo00oo ( IiI111111IIII )
    Oo0OO0000oooo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
    for Oo0OO0000oooo in Oo0OO0000oooo :
     Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
     for Iii1IIII11I in Iii1IIII11I :
      Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     IiI111111IIII = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0OO0000oooo ) )
     for IiI111111IIII in IiI111111IIII :
      IiI111111IIII = 'https://www.youtube.com/w' + IiI111111IIII
     ooo0OoOOOOO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
     for ooo0OoOOOOO in ooo0OoOOOOO :
      ooo0OoOOOOO = 'http:' + ooo0OoOOOOO
     i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooOoOoo0O , '' )
   elif Iii1IIII11I in I11II1i :
    pass
   elif 'user' in IiI111111IIII or 'elete' in Iii1IIII11I :
    pass
   elif 'hannel' in IiI111111IIII :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IiI111111IIII
    IIi1i11111 = O000OOo00oo ( IiI111111IIII )
    O0000OOO0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
    for O00 , IiI111111IIII , Iii1IIII11I in O0000OOO0 :
     if 'outube' in IiI111111IIII or 'list' in IiI111111IIII :
      pass
     elif 'atch' in IiI111111IIII :
      IiI111111IIII = ( IiI111111IIII ) . replace ( '/watch?v=' , '' )
      i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O00 , 'http:' + O00 , '' )
     else :
      pass
   else :
    i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooo0OoOOOOO , '' )
    if 51 - 51: oOo0O0Ooo / ooo0oo0o0oo / O0O0OoOO0
def I111iIi1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIi1i11111 )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiIi1IIi1I ( '[COLOR' + iIii1 + '] NEXT [/COLOR]' , url , 10065 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 for O00 , url , Iii1IIII11I , oooOOoooo , I1iii11 in i1I1i :
  I11II1i . append ( Iii1IIII11I )
  oOooOo0 ( 'tvshows' , 'INFO' )
  ooo0OoOOOOO = 'http:' + ( O00 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0OoOOOOO
  url = 'http://www.youtube.com' + url
  i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooo0OoOOOOO , I1iii11 )
 else :
  i1I1i = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
  for O00 , url , Iii1IIII11I , oooOOoooo in i1I1i :
   oOooOo0 ( 'tvshows' , 'INFO' )
   ooo0OoOOOOO = 'http:' + ( O00 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIi1i11111 = O000OOo00oo ( url )
    Oo0OO0000oooo = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIi1i11111 )
    for Oo0OO0000oooo in Oo0OO0000oooo :
     Iii1IIII11I = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
     for Iii1IIII11I in Iii1IIII11I :
      Iii1IIII11I = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0OO0000oooo ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooo0OoOOOOO = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0OO0000oooo ) )
     for ooo0OoOOOOO in ooo0OoOOOOO :
      ooo0OoOOOOO = 'http:' + ooo0OoOOOOO
     i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooOoOoo0O , '' )
   elif Iii1IIII11I in I11II1i :
    pass
   elif 'user' in url or 'elete' in Iii1IIII11I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIi1i11111 = O000OOo00oo ( url )
    O0000OOO0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
    for O00 , url , Iii1IIII11I in O0000OOO0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O00 , 'http:' + O00 , '' )
     else :
      pass
   else :
    i1I1iI1iIi111i ( '[COLORred]' + oooOOoooo + '[/COLOR]' + '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO , ooo0OoOOOOO , '' )
    if 92 - 92: OO0
    if 22 - 22: I1ii11iIi11i % IIIIi1i * Ii1I / O0OoO % Ii * oO0o0OOOO
def ooooo0O0000oo ( ) :
 if iiI1IiI == 'insert_password' :
  oooOOOOO . ok ( '[COLOR' + iIii1 + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iIii1 + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  Oo00OoOo = open ( O000OO0 )
  i1I1i = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( Oo00OoOo ) )
  for ii1ii111 , i11111I1I in i1I1i :
   if ii1ii111 == 'needs replacing' or i11111I1I == 'needs replacing' :
    ii1 ( )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']G-Tv PRIVATE LIST[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , i11i1I1 + 'PrivateList.png' , ooOoOoo0O , '' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']G-Tv ULTIMATE[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
  if 80 - 80: ii - O0OoO * O0O0OoOO0 * Ii1I / oOo0O0Ooo / O0OoO
def I1I11iI11iI1i ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + IIIII + ")" )
 ii1 ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 75 - 75: ii * ooo0oo0o0oo
def I1Iiiiiii ( ) :
 iiIi1IIi1I ( 'Full List' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
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
 iiIi1IIi1I ( 'German' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'Arabic' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'TV Series Latest' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'VOD Latest' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( 'VOD Bollywood' , '' , 60003 , i11i1I1 + 'UltimateList.png' , ooOoOoo0O , '' )
 if 39 - 39: ooo0oo0o0oo * I1ii11iIi11i + iI11I1II1I1I - ooo0oo0o0oo + O0OoO
def o0iiiI1I1iIIIi1 ( name ) :
 Iii = name
 IIi1i11111 = O000OOo00oo ( 'http://piesustv.net:8000/get.php?username=' + O0OoO000O0OO + '&password=' + iiI1IiI + '&type=m3u_plus&output=mpegts' )
 i1I1i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIi1i11111 )
 for name , O00 , I1iiiiI1iI , IiI111111IIII in i1I1i :
  if Iii == 'Full List' :
   IiI111111IIII = ( IiI111111IIII ) . replace ( '.ts' , '.m3u8' )
   i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , O00 , O00 , '' )
  else :
   Iii = ( Iii ) . replace ( 'World' , 'القنوات العربية' )
   if Iii in I1iiiiI1iI :
    IiI111111IIII = ( IiI111111IIII ) . replace ( '.ts' , '.m3u8' )
    print IiI111111IIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , O00 , O00 , '' )
   else :
    pass
    if 43 - 43: IIIi - ii
def ii1iI ( name ) :
 Iii = name
 IIi1i11111 = O000OOo00oo ( 'http://piesustv.net:8000/get.php?username=' + O0OoO000O0OO + '&password=' + iiI1IiI + '&type=m3u_plus&output=mpegts' )
 i1I1i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIi1i11111 )
 for name , O00 , IiI111111IIII in i1I1i :
  IiI111111IIII = ( IiI111111IIII ) . replace ( '.ts' , '.m3u8' )
  i1I1iI1iIi111i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( IiI111111IIII ) . strip ( ) , 10012 , O00 , O00 , '' )
 else :
  i1I1iI1iIi111i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 49 - 49: I11i . ooo0oo0o0oo / oO0o + IIiIiII11i
  if 47 - 47: o0o00Oo0O / O0O0OoOO0
  if 67 - 67: oOo0O0Ooo
  if 55 - 55: Ii1I - IIIIi1i * I11i + OOooOOo * OOooOOo * o0o00Oo0O
  if 91 - 91: iii1iiii1 - O0OoO % iI11I1II1I1I - ii % OO0
  if 98 - 98: oO0o . oO0o * IIIi * IIiIiII11i * iii1iiii1
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / ooo0oo0o0oo
  if 79 - 79: oO0o - iI11I1II1I1I + O0O0OoOO0 - iii1iiii1
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
  if 15 - 15: Ii % oOo0O0Ooo * oO0o0OOOO / iii1iiii1
def oooO0o0o0O0 ( ) :
 iiIi1IIi1I ( 'Full Backup' , '' , 10061 , i11i1I1 + 'FullBackUp.png' , ooOoOoo0O , 'Back Up Your Full System' )
 if os . path . exists ( I11i1I1I ) :
  iiIi1IIi1I ( 'Backup Genie Favourites' , IiI111111IIII , 10062 , i11i1I1 + 'BackupGenieFavourites.png' , ooOoOoo0O , 'Back Up Your favourites' )
 if os . path . exists ( o0O ) :
  iiIi1IIi1I ( 'Backup Ivue Config' , o0O , 10062 , i11i1I1 + 'BackUpIvueConfig.png' , ooOoOoo0O , 'Back Up Your master.db' )
 if os . path . exists ( O00oO ) :
  iiIi1IIi1I ( 'Backup Kodi Favourites' , O00oO , 10062 , i11i1I1 + 'BackKodiFavourites.png' , ooOoOoo0O , 'Back Up Your favourites.xml' )
  if 27 - 27: ii - IIIIi1i / oO0o0OOOO
  if 76 - 76: I11i % oOo0O0Ooo . iI11I1II1I1I - ooo0oo0o0oo * ii . IIIIi1i
  if 84 - 84: iii1iiii1 + oO0o0OOOO
zip = oo00 . getSetting ( 'zip' )
IIiiIIi1 = xbmc . translatePath ( os . path . join ( zip ) )
def o00ooO00O ( ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 81 - 81: IIIi * oO0o
  if 38 - 38: OOooOOo / IIIIi1i % I1ii11iIi11i
  if 11 - 11: IIIIi1i - IIIi + IIiIiII11i - iI11I1II1I1I
def I1i11ii11 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I11i1I1I
  elif 'Ivue' in name :
   url = o0O
  elif 'Kodi' in name :
   url = O00oO
  o00ooO00O ( )
  OO00O0oOO = open ( url ) . read ( )
  Ii1iI111 = os . path . join ( IIiiIIi1 , description . split ( 'Your ' ) [ 1 ] )
  Iii1I1I11iiI1 = open ( Ii1iI111 , mode = 'w' )
  Iii1I1I11iiI1 . write ( OO00O0oOO )
  Iii1I1I11iiI1 . close ( )
 else :
  if 'guisettings.xml' in description :
   O0oooo00o0Oo = open ( os . path . join ( IIiiIIi1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   I1iii = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1I1i = re . compile ( I1iii ) . findall ( O0oooo00o0Oo )
   for type , oO0o0O0Ooo0o , i1Ii11II in i1I1i :
    i1Ii11II = i1Ii11II . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oO0o0O0Ooo0o , i1Ii11II ) )
  else :
   Ii1iI111 = os . path . join ( url )
   OO00O0oOO = open ( os . path . join ( IIiiIIi1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii1I1I11iiI1 = open ( Ii1iI111 , mode = 'w' )
   Iii1I1I11iiI1 . write ( OO00O0oOO )
   Iii1I1I11iiI1 . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 18 - 18: IIiIiII11i . ii % OOooOOo % O0O0OoOO0
 if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
 if 2 - 2: ii % O0OoO
 if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def I1ii ( ) :
 O00O0O = 1
 o00ooO00O ( )
 IIi1i1IiIIi1i = xbmc . translatePath ( os . path . join ( IIiiIIi1 , 'Build Backup' , 'Full Backup' , '' ) )
 oOOo0OOOOo0Oo = xbmc . translatePath ( os . path . join ( IIiiIIi1 , 'Build Backup' , 'my_full_backup.zip' ) )
 OOo0o = xbmc . translatePath ( os . path . join ( IIiiIIi1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( IIi1i1IiIIi1i ) :
  os . makedirs ( IIi1i1IiIIi1i )
 oooii1iiIi1 = oooOOOOO . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oooii1iiIi1 ) : return False , 0
 i111iiI1ii = oooii1iiIi1
 IIiii = xbmc . translatePath ( os . path . join ( IIi1i1IiIIi1i , i111iiI1ii + '.zip' ) )
 I1i1i = [ 'plugin.video.GenieTv' ]
 OOOOooO0oO00O0o = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ooOO00oOOo000 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IIi = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 i11II11II1 = "Creating full backup of existing build"
 II1I = "Creating Community Build"
 OoOo000oOo0oo = "Archiving..."
 oO0O = ""
 oOO = "Please Wait"
 iiiIIiIi ( i11 , IIiii , II1I , OoOo000oOo0oo , oO0O , oOO , ooOO00oOOo000 , IIi )
 time . sleep ( 1 )
 OooOOO = xbmc . translatePath ( os . path . join ( IIi1i1IiIIi1i , i111iiI1ii + '_guisettings.zip' ) )
 Ii1iI11iI1 = zipfile . ZipFile ( OooOOO , mode = 'w' )
 try :
  Ii1iI11iI1 . write ( xbmc . translatePath ( os . path . join ( i11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 Ii1iI11iI1 . close ( )
 if O00O0O == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOOo0OOOOo0Oo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + IIiii + '[/COLOR]' )
  if 5 - 5: iI11I1II1I1I
def iiiIIiIi ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OOoo00oO00 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OO0oOOo = len ( sourcefile )
 OO0oO0o = [ ]
 III111i11IiI = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for O0000 , ooO00O0O0 , iII1I1 in os . walk ( sourcefile ) :
  for file in iII1I1 :
   III111i11IiI . append ( file )
 o0Ooo0o0ooo0 = len ( III111i11IiI )
 for O0000 , ooO00O0O0 , iII1I1 in os . walk ( sourcefile ) :
  ooO00O0O0 [ : ] = [ oo0o0000Oo0 for oo0o0000Oo0 in ooO00O0O0 if oo0o0000Oo0 not in exclude_dirs ]
  iII1I1 [ : ] = [ Iii1I1I11iiI1 for Iii1I1I11iiI1 in iII1I1 if Iii1I1I11iiI1 not in exclude_files ]
  for file in iII1I1 :
   OO0oO0o . append ( file )
   o0O00oOoo = len ( OO0oO0o ) / float ( o0Ooo0o0ooo0 ) * 100
   o0oOoO00o . update ( int ( o0O00oOoo ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O000O0OO00oo = os . path . join ( O0000 , file )
   if not 'temp' in ooO00O0O0 :
    if not 'plugin.program.originwizard' in ooO00O0O0 :
     import time
     oOOO = '01/01/1980'
     ooo0oooo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O000O0OO00oo ) ) )
     if ooo0oooo0 > oOOO :
      OOoo00oO00 . write ( O000O0OO00oo , O000O0OO00oo [ OO0oOOo : ] )
 OOoo00oO00 . close ( )
 o0oOoO00o . close ( )
 if 62 - 62: Ii1I + O0O0OoOO0 + ooOoO0O00 / ii
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
def I111i1I1 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCOOBY STREAMS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , i11i1I1 + 'scoob.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SCOOBY SCRAPES[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , i11i1I1 + 'scoob.png' , ooOoOoo0O , '' )
 if 62 - 62: O0OoO * iii1iiii1 / I1ii11iIi11i * I11i
 if 29 - 29: I1ii11iIi11i % oO0o % ooo0oo0o0oo . I11i / ii * OO0
def o0OoO000O ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH MOVIES[/COLOR]' , str ( I1I1iIiII1 ) , 9001 , i11i1I1 + 'MOVIESv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH SERIES[/COLOR]' , str ( I1I1iIiII1 ) , 9002 , i11i1I1 + 'TVSHOWSv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , i11i1I1 + 'ORIGINCARTOON' , ooOoOoo0O , '' )
 if 94 - 94: OOooOOo . o0o00Oo0O / O0O0OoOO0 . Ii1I - ooOoO0O00
 if 26 - 26: oO0o - O0OoO . I11i
 if 65 - 65: Ii1I % o0o00Oo0O % iI11I1II1I1I * O0O0OoOO0
 if 31 - 31: O0O0OoOO0
def iIIiI1I1i ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']RaysRavers[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , i11i1I1 + 'Rays-Ravers.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']QuickSilver[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , i11i1I1 + 'Quicksilver.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']RadioNomy[/COLOR]' , '' , 70001 , i11i1I1 + 'RadioNomy.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1iIiII1 ) , 30031 , i11i1I1 + 'MusicChannels.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']UK RADIO[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , i11i1I1 + 'UKRadio.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']WORLD RADIO[/COLOR]' , str ( I1I1iIiII1 ) , 1013 , i11i1I1 + 'WorldRadio.png' , ooOoOoo0O , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']CONCERTS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , i11i1I1 + 'Concerts.png' , ooOoOoo0O , '' )
  if 68 - 68: oO0o0OOOO % iii1iiii1 + Ii1I - Ii . I11i - iii1iiii1
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC VIDEOS[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , i11i1I1 + 'MusicVideos.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC[/COLOR]' , str ( I1I1iIiII1 ) + ( i1iiIII111ii ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , i11i1I1 + 'Music.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']MUSIC SEARCH[/COLOR]' , str ( I1I1iIiII1 ) , 1111 , i11i1I1 + 'MusicSearch.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , i11i1I1 + 'KodibleAudioBooks.png' , ooOoOoo0O , '' )
 if 31 - 31: oOo0O0Ooo * IIIi + ii - IIIIi1i / ii
 oOooOo0 ( 'movies' , 'MAIN' )
 if 19 - 19: ooo0oo0o0oo * OO0 * I11i + o0o00Oo0O / o0o00Oo0O
def ooOoO ( ) :
 iI1iiIiiII ( )
 if 91 - 91: IIIi + oOo0O0Ooo
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']KILL KODI[/COLOR]' , '' , 80000 , i11i1I1 + 'KillKodi.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SPEEDTEST[/COLOR]' , '' , 50004 , i11i1I1 + 'Speedtest.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , i11i1I1 + 'View-Log-File.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'DELETE CACHE' , 'url' , 14 , i11i1I1 + 'DeleteCache.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'DELETE PACKAGES' , 'url' , 6 , i11i1I1 + 'DeletePackages.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FORCE REFRESH' , 'url' , 10 , i11i1I1 + 'ForceRefresh.png' , ooOoOoo0O , 'Force Refresh All Repos' )
 if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / oO0o0OOOO
 i1I1iI1iIi111i ( 'CHECK MY IP' , 'url' , 12 , i11i1I1 + 'CheckMyIP.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , i11i1I1 + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , ooOoOoo0O , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1I1iIiII1 ) , 4 , i11i1I1 + 'AdvancedSettingXML.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']URL FIXES[/COLOR]' , str ( I1I1iIiII1 ) , 20 , i11i1I1 + 'URLFixes.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 44 - 44: oO0o0OOOO . OOooOOo * oOo0O0Ooo + ii - IIIIi1i - ooo0oo0o0oo
 if 15 - 15: ooo0oo0o0oo / o0o00Oo0O . I11i . Ii
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
 if 59 - 59: iii1iiii1 - I11i - OO0
 if 48 - 48: ooOoO0O00 + oO0o0OOOO % OOooOOo / I1ii11iIi11i - I11i
def OOoOOo0O00O ( ) :
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
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']My Local Zip[/COLOR]' , ii11iIi1I , 48 , i11i1I1 + 'MyLocalZIP.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']My Online Zip[/COLOR]' , i1iIIi1 , 43 , i11i1I1 + 'MyOnlineZip.png' , ooOoOoo0O , '' )
 if 55 - 55: I1ii11iIi11i - O0OoO
def O0OO0OIiiiIiiI ( ) :
 iI1iiIiiII ( )
 i1I1iI1iIi111i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1iIiII1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , i11i1I1 + 'FTV4.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1iIiII1 ) + '/wizard/customftv/settings.xml' , 17 , i11i1I1 + 'FTV3.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , i11i1I1 + 'FTV1.png' , ooOoOoo0O , '' )
 i1I1iI1iIi111i ( 'RESET FTV DATABASE' , 'url' , 18 , i11i1I1 + 'FTV2.png' , ooOoOoo0O , '' )
 if 72 - 72: ooOoO0O00
 if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
 if 63 - 63: Ii1I
def i1II ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 33 , i11i1I1 + 'Skins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ARTWORK PACKS[/COLOR]' , str ( I1I1iIiII1 ) , 34 , i11i1I1 + 'ArtworkPacks.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']CREATE UNIVERSAL PATHS[/COLOR]' , i11 , 35 , i11i1I1 + 'CreateUniversalPath.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 2 - 2: IIiIiII11i - oO0o . ooo0oo0o0oo * IIIIi1i / IIIi
def OOo0 ( ) :
 ooOooo000oOO = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1I1i = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( ooOooo000oOO )
 for O00 , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , O00 , O00 , '' )
 oOooOo0 ( 'tvshows' , 'INFO' )
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
def OooOOo0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( ooO000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 53 - 53: I11i . IIIIi1i / O0O0OoOO0
def I11iiIi1i1 ( ) :
 iI1iiIiiII ( )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']GOTHAM SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 36 , i11i1I1 + 'GothamSkins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']HELIX SKINS[/COLOR]' , str ( I1I1iIiII1 ) , 37 , i11i1I1 + 'HelixSkins.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']ISENGAARD SKINS[/COLOR]' , i11 , 38 , i11i1I1 + 'IsengaardSkins.png' , ooOoOoo0O , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 41 - 41: O0O0OoOO0 % Ii1I
def i1iIiIi1I ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + i1I1IIIiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 71 - 71: O0OoO * oO0o % ii % oO0o / oOo0O0Ooo
def Oo0ooo0Ooo ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + i1II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 95 - 95: oO0o - O0OoO / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + oo0OoOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 95 - 95: ooo0oo0o0oo * Ii1I % OO0 % O0O0OoOO0 - O0O0OoOO0
def oOoooO0 ( url ) :
 ooOooo000oOO = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 68 - 68: OO0 / I11i
def Ii11 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + II1i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 40 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 50 - 50: ooo0oo0o0oo % ooOoO0O00
def iii11II1I ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iI111I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 23 - 23: O0O0OoOO0 . I11i + I1ii11iIi11i - O0OoO
def II1iiIiIiI ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']APK (Android only)[/COLOR]' , str ( I1I1iIiII1 ) , 2 , i11i1I1 + 'APKAndroidOnly.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']APK Search[/COLOR]' , str ( I1I1iIiII1 ) , 30038 , i11i1I1 + 'APKSearch.png' , ooOoOoo0O , '' )
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + oO0o0OOOO
def IiiIi ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20vZ2FtZS8=' ) )
 i1I1i = re . compile ( 'href="([^"]*)">GAME</a>' ) . findall ( o00o )
 Iiiii1i = re . compile ( 'href="([^"]*)">APP</a>' ) . findall ( o00o )
 for IiI111111IIII in i1I1i :
  i11II1I11I1 ( 'Android Apps' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiI111111IIII , 30036 , i11i1I1 + 'apps.png' )
 for IiI111111IIII in Iiiii1i :
  i11II1I11I1 ( 'Android Games' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + IiI111111IIII , 30035 , i11i1I1 + 'GAMES.png' )
 oOooOo0 ( 'movies' , 'MAIN' )
def iIIi ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  if '/game' in url :
   i11II1I11I1 ( ( Iii1IIII11I ) . replace ( '&amp;' , ' - ' ) , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'APK.png' )
def ooO00O00oOO ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  if '/app' in url :
   i11II1I11I1 ( ( Iii1IIII11I ) . replace ( '&amp;' , ' - ' ) , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'APK.png' )
def I1IIII1ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( ' <img src="([^"]*)".+?title="([^"]*)">.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( 'href="([^"]*)">NEXT </a>' ) . findall ( o00o )
 for O00 , Iii1IIII11I , url in i1I1i :
  i11II1I11I1 ( ( Iii1IIII11I ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , url , 19 , O00 )
 for url in Iiiii1i :
  i11II1I11I1 ( 'NEXT' , ( i1iiIII111ii ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , i11i1I1 + 'Next.png' )
def IiIIi1I1I11Ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'href="([^"]*)">Download APK from APKCRAFT</a></p>' ) . findall ( o00o )
 for url in i1I1i :
  o0OO ( url )
def Oo ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIII1i = 'http://apk.koplayer.com/search?q=' + ( IIIiiI1i1 ) . replace ( ' ' , '+' ) + '&region='
 I1I = iiIII1i . lower ( )
 I1IIII1ii ( I1I )
 if 23 - 23: IIiIiII11i / IIIi
def o0OO ( url ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( iII1Iii1I11i , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oo00o0Oo , Iii1IIII11I + '.apk' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 89 - 89: IIiIiII11i / IIIi
def IIo0OoO00 ( url ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oo00o0Oo , Iii1IIII11I + '.mp4' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 18 - 18: IIIi - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / IIIIi1i . oOo0O0Ooo * OOooOOo
def IIiIiiiIIIIi1 ( name , url , description ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oo00o0Oo , name )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 iIi11 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIi11
 print '======================================='
 extract . all ( i1o0oooO , iIi11 , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 81 - 81: oO0o0OOOO / oO0o % ii * IIIi / IIIi
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
def OoOO ( url ) :
 ooOooo000oOO = O000OOo00oo ( I1I1iIiII1 + ( i1iiIII111ii ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'INFO' )
 if 32 - 32: OOooOOo * oOo0O0Ooo % OO0 * O0O0OoOO0 . o0o00Oo0O
 if 48 - 48: IIIIi1i * IIIIi1i
def I1I1 ( url ) :
 ooOooo000oOO = O000OOo00oo ( I1I1iIiII1 + ( i1iiIII111ii ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 30015 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 4 - 4: I11i % OOooOOo * O0OoO
def ii1IiIi11 ( url , iconimage , fanart ) :
 ooOooo000oOO = O000OOo00oo ( url )
 I1i11111i1i11 = url
 O00 = iconimage
 fanart = fanart
 i1I1i = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( ooOooo000oOO )
 for oo00o0 , Iii1IIII11I in i1I1i :
  if '.mp4' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Watch VIDEO' , url + '/' + oo00o0 , 222 , O00 , fanart , '' )
  if 'description' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Read Description' , url + '/' + oo00o0 , 30017 , O00 , fanart , '' )
  if 'images' in Iii1IIII11I :
   iiIi1IIi1I ( 'View Images' , url + '/' + oo00o0 , 30018 , O00 , fanart , '' )
  if 'url' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Install Build On Android' , url + '/' + oo00o0 , 30016 , O00 , fanart , '' )
  if 'url' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'Install Build On Pc' , url + '/' + oo00o0 , 30019 , O00 , fanart , '' )
 oOooOo0 ( 'movies' , 'INFO' )
 if 22 - 22: IIIi
def ii1ii ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url="([^"]*)"' ) . findall ( ooOooo000oOO )
 for url in i1I1i :
  oOoooO00O ( url )
  if 6 - 6: O0O0OoOO0 % ooOoO0O00 . O0O0OoOO0 * O0O0OoOO0
def o0Oo ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url="([^"]*)"' ) . findall ( ooOooo000oOO )
 for url in i1I1i :
  oo0ooO0 ( url )
  if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + IIIi
def i1oOOOOOOOoO ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( 'desc="([^"]*)"' ) . findall ( ooOooo000oOO )
 for I1IIiI in i1I1i :
  ii1I ( 'Description:' , I1IIiI )
  if 84 - 84: oO0o0OOOO - I1ii11iIi11i / o0o00Oo0O - iii1iiii1
def ii1iI1II11ii ( url ) :
 ooOooo000oOO = O000OOo00oo ( url )
 url = url
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ooOooo000oOO )
 for oo00o0 , Iii1IIII11I in i1I1i :
  if 'png' in Iii1IIII11I :
   i1I1iI1iIi111i ( 'image' , '' , '' , url + '/' + oo00o0 , url + '/' + oo00o0 , '' )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 8 - 8: OO0 * o0o00Oo0O
def OOoO ( name , url , description ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oo00o0Oo , name + '.zip' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Iii1 ( )
 if 89 - 89: oO0o / oOo0O0Ooo
 if 16 - 16: I1ii11iIi11i + OO0 / I1ii11iIi11i / oO0o % IIIi % Ii1I
def oo0ooO0 ( url ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oo00o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 Ii1II11II1iii ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 59 - 59: o0o00Oo0O % I1ii11iIi11i
def oOoooO00O ( url ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oo00o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 Ii1II11II1iii ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 92 - 92: O0O0OoOO0 % IIIIi1i / Ii1I % Ii1I * oOo0O0Ooo
def OooO00oOOo0Oo ( name , url , description ) :
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 i1o0oooO = os . path . join ( ii11iIi1I )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 5 - 5: I11i . o0o00Oo0O / I1ii11iIi11i % oO0o
def OoOo ( ) :
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
  IIIiiIIIiI1ii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  Iii1I1I11iiI1 . write ( IIIiiIIIiI1ii . rstrip ( '\r\n' ) + '\n' )
def o0oOO0ooOoO ( ) :
 o0o0OoOo0O0OO = oooOOOOO . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o0o0OoOo0O0OO == 0 : return
 elif o0o0OoOo0O0OO == 1 : pass
 oo0OOoOoo0O0O = OoOo ( )
 I1IiiiiI ( "Platform: " + str ( oo0OOoOoo0O0O ) )
 os . _exit ( 1 )
 I1IiiiiI ( "Force close failed!  Trying alternate methods." )
 if oo0OOoOoo0O0O == 'osx' :
  I1IiiiiI ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oo0OOoOoo0O0O == 'linux' :
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
 elif oo0OOoOoo0O0O == 'android' :
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
 elif oo0OOoOoo0O0O == 'windows' :
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
  if 15 - 15: IIIIi1i
  if 20 - 20: ooo0oo0o0oo % o0o00Oo0O . iii1iiii1
  if 93 - 93: Ii % iI11I1II1I1I % Ii + I11i / I11i / IIiIiII11i
def I1i ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( url ) :
  for file in iII1I1 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    O0oooo00o0Oo = open ( ( os . path . join ( OoIiIiIi1I1 , file ) ) ) . read ( )
    IiI1ii1Ii = O0oooo00o0Oo . replace ( i11 , 'special://home/' )
    Iii1I1I11iiI1 = open ( ( os . path . join ( OoIiIiIi1I1 , file ) ) , mode = 'w' )
    Iii1I1I11iiI1 . write ( str ( IiI1ii1Ii ) )
    Iii1I1I11iiI1 . close ( )
 o0oOO0ooOoO ( )
 if 51 - 51: Ii * I11i / oOo0O0Ooo
def iIIi1I ( ) :
 i11II1I11I1 ( ( '[COLOR' + iIii1 + ']GENRE[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , i11i1I1 + 'RadioNomy.png' )
 i11II1I11I1 ( ( '[COLOR' + iIii1 + ']SORT BY[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , i11i1I1 + 'RadioNomy.png' )
 i11II1I11I1 ( ( '[COLOR' + iIii1 + ']SEARCH[/COLOR]' ) , '' , 70006 , i11i1I1 + 'RadioNomy.png' )
 if 82 - 82: ooo0oo0o0oo * Ii % IIiIiII11i - ii
def OO0Ooo0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
def oooO00o0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
def o0o00oO0oo000 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in Iiiii1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']Filter - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , i11i1I1 + 'RadioNomy.png' )
 for url , O00 , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']Stream - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , O00 )
def oO000o ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( o00o )
 for url in i1I1i :
  o0Ooo0O0 ( url )
def I1I1Iiii1 ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1
 i111i1 = 'https://www.radionomy.com/en/search/index?query=' + ( IIIiiI1i1 ) . replace ( ' ' , '+' )
 IIi1i11111 = O000OOo00oo ( i111i1 )
 i1I1i = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']Stream - ' + Iii1IIII11I + '[/COLOR]' ) , ( i1iiIII111ii ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + IiI111111IIII , 70005 , O00 )
  if 99 - 99: oOo0O0Ooo + ooOoO0O00 + Ii + I1ii11iIi11i % IIIi / oO0o0OOOO
  if 60 - 60: O0O0OoOO0 * OOooOOo - Ii % OO0
def oOOOooOo0O ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , 'http://www.listenlive.eu/' + IiI111111IIII , 10111113 , i11i1I1 + 'radio.png' )
def III1i111i ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , url , 222 , i11i1I1 + 'radio.png' )
  if 42 - 42: Ii1I / ooOoO0O00 % OOooOOo
def I11iiIIII1I1 ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.toonjet.com/' + IiI111111IIII , 8051 , i11i1I1 + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1IIi1i1Ii1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( o00o )
 Iiiii1i = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( o00o )
 for url , O00 in i1I1i :
  if 'ol.gif' in O00 :
   pass
  elif 'link_block_' in O00 :
   pass
  elif '.png' in O00 :
   pass
  else :
   i11II1I11I1 ( ( O00 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , i11i1I1 + 'vod.png' )
 for url in Iiiii1i :
  i11II1I11I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , i11i1I1 + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Iiio0Oo0oO ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( o00o )
 for url in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , i11i1I1 + 'classictoons.png' )
  if 48 - 48: IIIi . I11i / IIIi
  if 56 - 56: iI11I1II1I1I . Ii - O0OoO * IIiIiII11i * iii1iiii1
def i1I1 ( ) :
 OOO0 ( 'Audio Books' , '' , 30011 , i11i1I1 + 'AudioBooks.png' , i11i1I1 + 'AudioBooks.png' , '' )
 OOO0 ( 'Kids Audio Books' , '' , 30006 , i11i1I1 + 'KidsAudioBooks.png' , i11i1I1 + 'KidsAudioBooks.png' , '' )
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( ) :
 OOO0 ( 'All' , '' , 30001 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OOO0 ( 'Popular' , '' , 30012 , i11i1I1 + 'POPULARv.png' , i11i1I1 + 'POPULARv.png' , '' )
 OOO0 ( 'Search' , '' , 30013 , i11i1I1 + 'Search.png' , i11i1I1 + 'Search.png' , '' )
 if 53 - 53: iI11I1II1I1I - IIIi % OOooOOo * iii1iiii1 % OO0
def II1Ii ( ) :
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , OOoO00ooO in i1I1i :
  if 'Parent' in Iii1IIII11I :
   pass
  elif '2' in OOoO00ooO :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 12 - 12: OO0 % oOo0O0Ooo + IIIi - ooOoO0O00 . O0O0OoOO0 / oOo0O0Ooo
def o0IiiiI111I ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , OOoO00ooO in i1I1i :
  if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
   if '1' in OOoO00ooO :
    OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOoO00ooO :
    OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOoO00ooO :
    OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
    if 49 - 49: I11i * O0O0OoOO0 + oO0o0OOOO + IIIIi1i
    if 30 - 30: I11i / O0OoO / ooo0oo0o0oo % OO0 + IIiIiII11i
def I1III111i ( ) :
 IIi1i11111 = O000OOo00oo ( o0 + 'books' + iIi1ii1I1 )
 i1I1i = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIi1i11111 )
 for Iii1IIII11I , IiI111111IIII , OOoO00ooO in i1I1i :
  if '1' in OOoO00ooO :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 3010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOoO00ooO :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOoO00ooO :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiI111111IIII , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 4 - 4: ooOoO0O00 + OO0 + ooOoO0O00
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: O0O0OoOO0
def OoOOo00 ( url ) :
 oo00o0 = url
 IIi1i11111 = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in Iiiii1i :
  if 'mp3' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif '/' in Iii1IIII11I :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 30009 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 53 - 53: ooo0oo0o0oo . iii1iiii1 % iI11I1II1I1I % OOooOOo % oO0o0OOOO
   if 53 - 53: iii1iiii1
   if 69 - 69: OOooOOo . I11i . oOo0O0Ooo - Ii1I
def IiiiI ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 oo00o0 = url
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
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Iii1IIII11I :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 10012 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  else :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 30010 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 12 - 12: IIiIiII11i
   if 2 - 2: ooOoO0O00 - oOo0O0Ooo + oO0o0OOOO . IIiIiII11i
def iIIiI1iiI ( ) :
 OOO0 ( 'A-Z' , '' , 30007 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OOO0 ( 'All' , '' , 30003 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 OOO0 ( 'Search' , '' , 30014 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
 if 18 - 18: IIIIi1i - IIIi % IIIIi1i / oO0o0OOOO
def O0Oo00OO00Ooo ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1I1i = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 in i1I1i :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IiI111111IIII + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in O00 :
   pass
  else :
   OOO0 ( O00 , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IiI111111IIII ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + O00 + '.gif' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: I1ii11iIi11i * O0OoO % ooo0oo0o0oo % OOooOOo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: OOooOOo + O0O0OoOO0 / IIIi
 if 13 - 13: IIIIi1i
def o0OOOOO0O ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if '</a>' in Iii1IIII11I :
   pass
  elif '(' in Iii1IIII11I :
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
  else :
   iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: O0O0OoOO0 - O0O0OoOO0 + ooOoO0O00 - o0o00Oo0O - iii1iiii1
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: OOooOOo - IIIIi1i - ii
def o00ii111Iiii ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1I1i = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
   if '</a>' in Iii1IIII11I :
    pass
   elif '(' in Iii1IIII11I :
    OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
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
   OOO0 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiI111111IIII , 30005 , i11i1I1 + 'KodibleAudioBooks.png' , i11i1I1 + 'KodibleAudioBooks.png' , '' )
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
  oo00o0 = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oo00o0 )
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
 for url , Iii1IIII11I , O00 in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , O00 , O00 , Iii1IIII11I )
 for url , Iii1IIII11I in i1iIIi1II1iiI :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 21005 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 21005 , i11i1I1 + 'Next.png' , '' , '' )
def III1Ii1i1I1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 O0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 O00OooO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIi1i11111 )
 I1IiI1iI11 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url in O00OooO :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']PLAY[/COLOR]' , 'http:' + url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 for url , Iii1IIII11I in O0 :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
 else :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , i11i1I1 + 'watchcartoons.png' , '' , '' )
def iIi ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'watchcartoons.png' , '' , '' )
  if 29 - 29: o0o00Oo0O . iii1iiii1
def OO0o0oO0O000o ( ) :
 i11II1I11I1 ( '[COLOR' + iIii1 + ']CARTOONS[/COLOR]' , '' , 20001 , i11i1I1 + 'ORIGINCARTOON.png' )
 i11II1I11I1 ( '[COLOR' + iIii1 + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , i11i1I1 + 'ORIGINCARTOON.png' )
 if 47 - 47: iii1iiii1 - oO0o / O0O0OoOO0 * ii / O0O0OoOO0 . I1ii11iIi11i
def iiII1IiIi1iI1 ( ) :
 i11II1I11I1 ( '[COLOR' + iIii1 + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , i11i1I1 + 'ORIGINCARTOON.png' )
 i11II1I11I1 ( '[COLOR' + iIii1 + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , i11i1I1 + 'ORIGINCARTOON.png' )
 if 72 - 72: o0o00Oo0O
def o0oO0Oo ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  if '?c=' in url :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i11i1I1 + 'ORIGINCARTOON.png' )
   if 71 - 71: I11i - OOooOOo * IIIIi1i + O0O0OoOO0 % Ii - OO0
def o0O0OO0o ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , OOOoOo , Iii1IIII11I in i1I1i :
  if 'Genre' in url :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , i11i1I1 + 'ORIGINCARTOON.png' )
   if 70 - 70: I1ii11iIi11i - IIIi . iI11I1II1I1I % oO0o0OOOO / OOooOOo - o0o00Oo0O
def o0O0oo0o ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , OOOoOo , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOOoOo )
  if 12 - 12: OOooOOo % ooo0oo0o0oo % Ii1I . Ii * iI11I1II1I1I
def oo0oooo0OoO0o ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , OOOoOo , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , OOOoOo )
  if 50 - 50: IIIIi1i / IIIIi1i + O0OoO * OO0 / Ii1I
  if 14 - 14: O0O0OoOO0 % oOo0O0Ooo - iI11I1II1I1I . O0OoO + oO0o - iii1iiii1
  if 5 - 5: IIIIi1i
  if 62 - 62: OOooOOo . ii . O0OoO . oO0o * IIIIi1i
  if 78 - 78: IIIi / oO0o - IIIi * ii . OOooOOo
def OOoooOoO0Oo ( ) :
 if 78 - 78: ii / O0OoO % OOooOOo * ii
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Cartoons[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Cartoons[/COLOR]' , '' , 10005 , i11i1I1 + 'ORIGINCARTOON.png' , ooOoOoo0O , '' )
 if 68 - 68: IIIi
def i11i11 ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 18 - 18: iI11I1II1I1I + oO0o0OOOO * oOo0O0Ooo - O0OoO / oOo0O0Ooo
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIi1i11111 )
 if 78 - 78: oO0o0OOOO . ooo0oo0o0oo
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
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
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o00o )
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
 o00o = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o00o )
 for O00 in Iiiii1i :
  OoO = O00
 i111i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o00o )
 for url in i111i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , url , 10006 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
 i1I1i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 10007 , OoO )
  if 46 - 46: oO0o * I1ii11iIi11i % IIIi + o0o00Oo0O * ooo0oo0o0oo
  if 34 - 34: oO0o
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: O0O0OoOO0 - o0o00Oo0O % oO0o0OOOO * iii1iiii1 . ooo0oo0o0oo % iI11I1II1I1I
def IiIi1i ( url , IMAGE ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  print Iii1IIII11I + '     ' + url
  if 'easy' in url :
   oO0O0oO ( url )
   if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - O0OoO % I11i
   if 30 - 30: iii1iiii1 % iii1iiii1 % ooo0oo0o0oo . OOooOOo
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: OO0 / IIiIiII11i . OOooOOo % I11i * IIiIiII11i - OO0
def oO0O0oO ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( "url: '(.+?)'," ) . findall ( o00o )
 for url in i1I1i :
  o0Ooo0O0 ( url )
  if 55 - 55: oOo0O0Ooo
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * IIIi * oO0o
  if 35 - 35: Ii1I / IIIIi1i % oOo0O0Ooo + iI11I1II1I1I
def oO00o ( ) :
 if 36 - 36: iii1iiii1 . IIiIiII11i % OO0
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Stand Up[/COLOR]' , '' , 10014 , i11i1I1 + 'StandUp.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Comedian[/COLOR]' , '' , 10015 , i11i1I1 + 'SearchComedian.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Others[/COLOR]' , '' , 10017 , i11i1I1 + 'Others.png' , ooOoOoo0O , '' )
 if 84 - 84: ii - Ii / iI11I1II1I1I / ii / Ii1I
def iIIii1 ( ) :
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  if 'elete' in Iii1IIII11I :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 222 , O00 )
   if 41 - 41: OOooOOo . Ii / oO0o0OOOO
def oOo00OoO0O ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOoO0OooOOo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , oOIIi , i1iII1IiiIiI1 in OoOoO0OooOOo :
  for IIIiiI1i1 in oOIIi :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1Ii1IIiI11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IiI111111IIII , Iii1IIII11I in I1Ii1IIiI11i1 :
    if 'tube' in IiI111111IIII :
     pass
    elif 'stage' in IiI111111IIII :
     OOoOO0ooo ( '[COLOR' + iIii1 + ']' + oOIIi + '   -   ' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O00 , )
    elif 'vee' in IiI111111IIII :
     pass
     if 45 - 45: IIiIiII11i % OO0 % ooo0oo0o0oo + Ii1I . ooOoO0O00 . OOooOOo
def O0o0OO00 ( ) :
 IIi1i11111 = O000OOo00oo ( ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOoO0OooOOo = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , oOIIi , i1iII1IiiIiI1 in OoOoO0OooOOo :
  I1Ii1IIiI11i1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IiI111111IIII , Iii1IIII11I in I1Ii1IIiI11i1 :
   if 'tube' in IiI111111IIII :
    pass
   elif 'stage' in IiI111111IIII :
    OOoOO0ooo ( '[COLOR' + iIii1 + ']' + oOIIi + '   -   ' + Iii1IIII11I + '[/COLOR]' , ( IiI111111IIII ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O00 )
   elif 'vee' in IiI111111IIII :
    pass
    if 14 - 14: Ii1I + Ii
    if 83 - 83: Ii1I / Ii + IIiIiII11i . IIIIi1i * O0OoO + ooo0oo0o0oo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: ooOoO0O00 % IIiIiII11i . OO0
def II1II1iI ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i1i11I1I1iii1 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIi1i11111 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i1i11I1I1iii1 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i1i11I1I1iii1 :
  o0Ooo0O0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 58 - 58: o0o00Oo0O . ooo0oo0o0oo / ii . oO0o / I1ii11iIi11i * IIiIiII11i
  if 53 - 53: O0O0OoOO0 - o0o00Oo0O / I11i % IIIIi1i * oOo0O0Ooo % O0OoO
  if 69 - 69: Ii1I
  if 83 - 83: I11i
  if 38 - 38: iii1iiii1 + ii . ooOoO0O00
  if 19 - 19: IIIIi1i - I11i - O0O0OoOO0 - OOooOOo . IIIIi1i . iii1iiii1
  if 48 - 48: IIIIi1i + ooo0oo0o0oo
def O0o0o0 ( ) :
 if 15 - 15: iI11I1II1I1I . o0o00Oo0O
 O0o0O ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , ooOoOoo0O , '' )
 O0o0O ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 if 6 - 6: IIiIiII11i
 oOooOo0 ( 'movies' , 'MAIN' )
 if 7 - 7: O0O0OoOO0 % ooOoO0O00 * ii * o0o00Oo0O + IIIIi1i
def OoO0oO ( ) :
 O0o0O ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 O0o0O ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , ooOoOoo0O , '' )
 if 10 - 10: ooOoO0O00 . IIiIiII11i / I11i * OO0
 oOooOo0 ( 'movies' , 'MAIN' )
def i1III1iI ( ) :
 if 38 - 38: iI11I1II1I1I / OO0
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 i11oooOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 98 - 98: IIiIiII11i - ii * o0o00Oo0O
 for oo0OoOOooO in i11oooOo :
  o0o0OO0o00o0O = oo0OooOOo0 + oo0OoOOooO + iIi1ii1I1
  IIi1i11111 = O0Oo000ooO00 ( o0o0OO0o00o0O )
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1i11111 )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , oO0o0 , Iii1IIII11I in i1I1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    IIIIIIi1i ( Iii1IIII11I , IiI111111IIII , 222 , i1i1IIIIi1i , oO0o0 , iII1iii )
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
    oOooOo0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: O0OoO + IIIi . o0o00Oo0O . O0O0OoOO0 % ooOoO0O00 % O0OoO
    if 50 - 50: ooo0oo0o0oo + I11i
def o0OoOOo ( ) :
 if 56 - 56: oO0o0OOOO / iI11I1II1I1I + OOooOOo % O0OoO . O0OoO - Ii1I
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 i11oooOo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 48 - 48: I1ii11iIi11i - OO0 + I1ii11iIi11i - oOo0O0Ooo * Ii . IIIIi1i
 for oo0OoOOooO in i11oooOo :
  I1iIIIiI = oo0OooOOo0 + oo0OoOOooO + iIi1ii1I1
  IIi1i11111 = O0Oo000ooO00 ( I1iIIIiI )
  i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIi1i11111 )
  for Iii1IIII11I , iII1iii , IiI111111IIII , O00 , oO0o0 , OoiI1I1 in i1I1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    O0o0O ( Iii1IIII11I , IiI111111IIII , OoiI1I1 , O00 , oO0o0 , iII1iii )
    if 27 - 27: OO0 - I1ii11iIi11i + IIIIi1i - O0OoO . oOo0O0Ooo
    oOooOo0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 51 - 51: IIIi + oO0o + IIIIi1i + IIIIi1i % I11i
    if 29 - 29: OO0
def ii1iIi1Ii1 ( ) :
 if 66 - 66: oO0o % I11i
 o00o = O000OOo00oo ( oo0OooOOo0 + 'spongemain.php' )
 i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , iII1iii , IiI111111IIII , O00 , oO0o0 , OoiI1I1 in i1I1i :
  O0o0O ( Iii1IIII11I , IiI111111IIII , OoiI1I1 , O00 , oO0o0 , iII1iii )
  oOooOo0 ( 'movies' , 'MAIN' )
def iI1ii11Ii ( url ) :
 if 97 - 97: iii1iiii1 + IIIi - oO0o % IIIi - I11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1i = ( '%s%s' % ( iiiI1IiIIii , url ) )
 ooOooo000oOO = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOooo000oOO )
 for url , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in i1I1i :
  Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
  for OOOo00 in Ii11Ii1iI :
   if OOOo00 == url :
    Iii1IIII11I = ( '[COLORred]Watched - [/COLOR]' + Iii1IIII11I ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IIIIIIi1i ( Iii1IIII11I , url , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
  if 15 - 15: oO0o0OOOO
  oOooOo0 ( 'movies' , 'MAIN' )
  if 94 - 94: iii1iiii1 % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: I1ii11iIi11i - oO0o0OOOO
  if 24 - 24: ii . oO0o * IIiIiII11i
def o0oO00 ( url ) :
 if 88 - 88: oO0o0OOOO + Ii % IIIi * O0OoO * O0OoO * O0O0OoOO0
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , iII1iii , url , O00 , oO0o0 , OoiI1I1 in i1I1i :
  O0o0O ( Iii1IIII11I , url , OoiI1I1 , O00 , oO0o0 , iII1iii )
  if 24 - 24: OO0 / IIIIi1i + ooo0oo0o0oo . ooo0oo0o0oo
  oOooOo0 ( 'movies' , 'MAIN' )
  if 39 - 39: OO0 + o0o00Oo0O / ooOoO0O00 % ooo0oo0o0oo / IIIi * ooo0oo0o0oo
  if 77 - 77: ooo0oo0o0oo . iii1iiii1 % OOooOOo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: ooo0oo0o0oo % IIIIi1i % I11i % IIIi + oO0o0OOOO % OOooOOo
def IIIIIIi1i ( name , url , mode , iconimage , fanart , description ) :
 if 3 - 3: IIIi
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = False )
 return iI1
 if 19 - 19: ooo0oo0o0oo * iii1iiii1 / IIIi * iii1iiii1 - ii * oO0o0OOOO
def O0o0O ( name , url , mode , iconimage , fanart , description ) :
 if 17 - 17: IIiIiII11i + I1ii11iIi11i . iii1iiii1
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = True )
 return iI1
if 12 - 12: iii1iiii1 + O0OoO + oO0o0OOOO . ooo0oo0o0oo / O0O0OoOO0
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
def o0OO00oo0O ( string ) :
 if OOOO0OOoO0O0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 46 - 46: Ii - O0OoO * oOo0O0Ooo * oO0o0OOOO % Ii1I * ooOoO0O00
def Iii1I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1i1i1i1IiII1 = [ ]
 try :
  if 32 - 32: O0OoO . I11i % ooo0oo0o0oo + Ii1I + oO0o
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iiiiiIIii ) == False :
  o0OO00oo0O ( 'Making Favorites File' )
  i1i1i1i1IiII1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  O0oooo00o0Oo = open ( iiiiiIIii , "w" )
  O0oooo00o0Oo . write ( json . dumps ( i1i1i1i1IiII1 ) )
  O0oooo00o0Oo . close ( )
 else :
  o0OO00oo0O ( 'Appending Favorites' )
  O0oooo00o0Oo = open ( iiiiiIIii ) . read ( )
  OOOoOOo0o = json . loads ( O0oooo00o0Oo )
  OOOoOOo0o . append ( ( name , url , iconimage , fanart , mode ) )
  IiI1ii1Ii = open ( iiiiiIIii , "w" )
  IiI1ii1Ii . write ( json . dumps ( OOOoOOo0o ) )
  IiI1ii1Ii . close ( )
  if 50 - 50: IIiIiII11i - iii1iiii1 + iI11I1II1I1I + iI11I1II1I1I
  if 91 - 91: IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
def iiIiiIi1 ( ) :
 if os . path . exists ( iiiiiIIii ) == False :
  i1i1i1i1IiII1 = [ ]
  o0OO00oo0O ( 'Making Favorites File' )
  i1i1i1i1IiII1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  O0oooo00o0Oo = open ( iiiiiIIii , "w" )
  O0oooo00o0Oo . write ( json . dumps ( i1i1i1i1IiII1 ) )
  O0oooo00o0Oo . close ( )
 else :
  I1Ii11i = json . loads ( open ( iiiiiIIii ) . read ( ) )
  I1iIiiiI1 = len ( I1Ii11i )
  for OOO0O00Oo in I1Ii11i :
   Iii1IIII11I = OOO0O00Oo [ 0 ]
   IiI111111IIII = OOO0O00Oo [ 1 ]
   i1i1IIIIi1i = OOO0O00Oo [ 2 ]
   try :
    ii1oOOO0ooOO = OOO0O00Oo [ 3 ]
    if ii1oOOO0ooOO == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     ii1oOOO0ooOO = i1i1IIIIi1i
    else :
     ii1oOOO0ooOO = oO0o0
   try : i11IiI1iiI11 = OOO0O00Oo [ 5 ]
   except : i11IiI1iiI11 = None
   try : OOoOOOO00 = OOO0O00Oo [ 6 ]
   except : OOoOOOO00 = None
   if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + iii1iiii1
   if OOO0O00Oo [ 4 ] == 0 :
    iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , '' , i1i1IIIIi1i , oO0o0 , '' , 'fav' )
   else :
    iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , OOO0O00Oo [ 4 ] , i1i1IIIIi1i , oO0o0 , '' , 'fav' )
    if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * IIIi
def Oo0 ( name ) :
 OOOoOOo0o = json . loads ( open ( iiiiiIIii ) . read ( ) )
 for O0000Oo00o in range ( len ( OOOoOOo0o ) ) :
  if OOOoOOo0o [ O0000Oo00o ] [ 0 ] == name :
   del OOOoOOo0o [ O0000Oo00o ]
   IiI1ii1Ii = open ( iiiiiIIii , "w" )
   IiI1ii1Ii . write ( json . dumps ( OOOoOOo0o ) )
   IiI1ii1Ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
 if 89 - 89: IIIIi1i . Ii * o0o00Oo0O
def ii1 ( ) :
 Iiii1 = os . path . join ( Ooo , 'addons.ini' )
 iI111II1ii = open ( Iiii1 , "w+" )
 IIi1i11111 = O000OOo00oo ( 'http://piesustv.net:8000/get.php?username=' + O0OoO000O0OO + '&password=' + iiI1IiI + '&type=m3u_plus&output=mpegts' )
 i1I1i = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIi1i11111 )
 iI111II1ii . write ( r'[' + IiII + ']' + '\n' )
 for Iii1IIII11I , O00 , I1iiiiI1iI , IiI111111IIII in i1I1i :
  IiI111111IIII = ( IiI111111IIII + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  O0ooO00ooOO0o = ( Iii1IIII11I + '=plugin://' + IiII + '/?url=' + IiI111111IIII + '&mode=10012&name=' + ( Iii1IIII11I ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( O00 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( O00 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iI111II1ii . write ( O0ooO00ooOO0o + '\n' )
  if 65 - 65: IIIIi1i . oO0o + O0O0OoOO0
  if 25 - 25: I11i + I1ii11iIi11i . I1ii11iIi11i % ii - O0O0OoOO0
def iIII11Iiii1 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + '247.png' , i11i1I1 + '247.png' , '' )
def o0oo0 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'musicch.png' , i11i1I1 + 'musicch.png' , '' )
def OoO0OOoO0Oo0 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'NEWS.png' , i11i1I1 + 'NEWS.png' , '' )
def oO00O ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , ( IiI111111IIII ) . strip ( ) , 222 , i11i1I1 + 'adult.png' , i11i1I1 + 'adult.png' , '' )
def II111IiiiI1 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1I1i = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i1I1iI1iIi111i ( Iii1IIII11I , IiI111111IIII , 1016 , i11i1I1 + 'TUTS.png' , i11i1I1 + 'TUTS.png' , '' )
  if 75 - 75: OO0
  if 29 - 29: Ii1I
def Oo0o00ooOOOoOo ( ) :
 if 30 - 30: OO0 + OO0 % ooo0oo0o0oo - I11i - Ii1I
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Recent Episodes[/COLOR]' , '' , 10019 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Genres[/COLOR]' , '' , 10020 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search[/COLOR]' , '' , 10021 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
 if 36 - 36: oO0o0OOOO % O0OoO
def OoO0 ( ) :
 if 37 - 37: oO0o0OOOO
 o00o = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1I1i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , O00 , Iii1IIII11I , Ooo00OoOOO in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I + '  -  ' + ( Ooo00OoOOO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiI111111IIII , 10023 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
  if 83 - 83: o0o00Oo0O
  if 89 - 89: I1ii11iIi11i + Ii1I - I11i
  if 40 - 40: oO0o + oO0o
def o0oo0o00ooO00 ( ) :
 if 37 - 37: oO0o - Ii1I . ii . OO0 + OOooOOo / O0O0OoOO0
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
 if 15 - 15: ooo0oo0o0oo . ooOoO0O00 * OOooOOo % iI11I1II1I1I
def III11I1 ( url ) :
 I1i11111i1i11 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIi1i11111 = cloudflare . source ( I1i11111i1i11 )
 i1I1i = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , O00 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 10022 , i11i1I1 + 'dtv.png' , ooOoOoo0O , '' )
  if 61 - 61: OOooOOo - oO0o + oOo0O0Ooo * O0OoO % oO0o
  if 24 - 24: OO0 - oO0o0OOOO * IIIi
  if 87 - 87: O0O0OoOO0 - Ii1I % Ii1I . IIIi / Ii1I
  if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
def o0O0OOo0oO ( ) :
 if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIIiiI1i1 ) . replace ( ' ' , '+' )
 IIi1i11111 = cloudflare . source ( IiI111111IIII )
 i1I1i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 10022 , i11i1I1 + 'dtv.png' )
   if 62 - 62: o0o00Oo0O . I1ii11iIi11i
   if 33 - 33: I1ii11iIi11i / iI11I1II1I1I % ooOoO0O00
   if 76 - 76: O0O0OoOO0 + iI11I1II1I1I + OOooOOo . oO0o
def i1i1 ( url ) :
 IIi1i11111 = cloudflare . source ( url )
 i1I1i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 )
 for oo00o0 , o0oOoOo0 , III1IiI1i1i , Iii1IIII11I in i1I1i :
  o0OOOOOo0 = ( III1IiI1i1i ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oooOoO = ( o0oOoOo0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0Oo0 = 'Season ' + oooOoO + 'Episode ' + o0OOOOOo0 + Iii1IIII11I
  iIIIi1IiI11I1 ( O0Oo0 , oo00o0 )
  if 71 - 71: O0O0OoOO0 - o0o00Oo0O - IIIIi1i . O0OoO % I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: ii + O0OoO % OOooOOo . oO0o * ooOoO0O00
  if 2 - 2: I1ii11iIi11i * o0o00Oo0O
def iIIIi1IiI11I1 ( name , url ) :
 oo00o0 = url
 ooOOo00oo0 = name
 ooOO00O00oo = cloudflare . source ( oo00o0 )
 Iiiii1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( ooOO00O00oo )
 for i1i11I1I1iii1 , IIIII1Ii in Iiiii1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + ooOOo00oo0 + IIIII1Ii + '[/COLOR]' , i1i11I1I1iii1 , 10012 , i11i1I1 + 'dtv.png' )
  if 13 - 13: IIiIiII11i
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: O0O0OoOO0 - ii
 if 68 - 68: I11i % Ii1I / iii1iiii1 + iii1iiii1 - iii1iiii1 . oO0o
def oOO00ooOOo ( ) :
 if 20 - 20: Ii1I
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 if 34 - 34: O0O0OoOO0 * O0O0OoOO0 - Ii1I - o0o00Oo0O . Ii
 if 32 - 32: iI11I1II1I1I . oO0o * IIIi / O0OoO . IIiIiII11i - I1ii11iIi11i
 if 10 - 10: Ii1I / Ii - O0O0OoOO0 + IIIi * oOo0O0Ooo
 if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
 if 64 - 64: oO0o0OOOO + oO0o
 if 25 - 25: oOo0O0Ooo . OO0 + oOo0O0Ooo % O0O0OoOO0 * iI11I1II1I1I
 if 31 - 31: Ii + O0OoO - o0o00Oo0O
 if 51 - 51: oO0o * ooOoO0O00 / O0O0OoOO0 * O0OoO + OO0 % Ii1I
 if 34 - 34: IIIi * ii + O0O0OoOO0 + Ii
 if 22 - 22: ooOoO0O00
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Search Program[/COLOR]' , '' , 10043 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 if 24 - 24: oO0o0OOOO / oOo0O0Ooo * ooOoO0O00 % ii
 if 99 - 99: Ii . IIiIiII11i . ii
def Ooi1IIii11i1I1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Oo0OO0000oooo = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 i1I1i = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Oo0OO0000oooo ) )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
  if 12 - 12: ooOoO0O00 / O0OoO % OO0 * ooo0oo0o0oo * o0o00Oo0O * iI11I1II1I1I
def OOOOoO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
  if 19 - 19: oOo0O0Ooo % O0O0OoOO0 . ooo0oo0o0oo * OO0
def oOo0OOOOoO ( url ) :
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
  if 70 - 70: IIiIiII11i + iii1iiii1 + Ii - ooOoO0O00 / ooo0oo0o0oo
  if 40 - 40: Ii1I * iii1iiii1
def IiI ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIIII1i = 'http://www.watchseries.ac/search/' + IIIiiI1i1 . replace ( ' ' , '%20' )
 IIi1i11111 = O000OOo00oo ( IIIII1i )
 i1I1i = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'watch online' in Iii1IIII11I :
   pass
  else :
   print IiI111111IIII
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.watchseries.ac' + IiI111111IIII , 10044 , O00 , '' , '' )
   if 39 - 39: IIIi / I1ii11iIi11i
   xbmcplugin . setContent ( OOOO , 'movies' )
   if 9 - 9: IIIi - iii1iiii1 % o0o00Oo0O . ooOoO0O00 . oOo0O0Ooo / oOo0O0Ooo
def O0000Oo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , url , Iii1IIII11I , III1IiI1i1i , iII1iii in i1I1i :
  OOOOOO = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( III1IiI1i1i ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + OOOOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , O00 , '' , iII1iii )
  if 77 - 77: I1ii11iIi11i
def II111I1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I in i1I1i :
  OOOOOO = ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + OOOOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , i11i1I1 + 'Next.png' , '' , '' )
  if 32 - 32: O0OoO % ooOoO0O00
def IIi1i1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , O00 in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , O00 , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , i11i1I1 + 'Next.png' , '' , '' )
  if 84 - 84: O0OoO + O0O0OoOO0 + I11i
def i1i1iIII11i ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIi1i11111 )
 Oo0OO0000oooo = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for o0oOoOo0 , OoOoO0OooOOo in Oo0OO0000oooo :
  i1I1i = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OoOoO0OooOOo ) )
  for url , Iii1IIII11I in i1I1i :
   OOOOOO = ( o0oOoOo0 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + OOOOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 Iiiii1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , url in i1I1i :
  iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , i11i1I1 + 'WATCHSERIES.png' , '' , '' )
 for url in Iiiii1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , i11i1I1 + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 40 - 40: iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
class oOoo0ooOoo ( ) :
 if 52 - 52: oO0o * ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 12 - 12: o0o00Oo0O + ooo0oo0o0oo * ooOoO0O00 . oO0o
  OOOOOO = name
  self . Get_Sources ( IiI111111IIII , OOOOOO )
  if 71 - 71: iii1iiii1 - I11i - O0OoO
  if 28 - 28: iI11I1II1I1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIi1i11111 = O000OOo00oo ( URL )
  i1I1i = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIi1i11111 )
  for IiI111111IIII , Iii1IIII11I in i1I1i :
   URL = 'http://www.watchseries.ac/link/' + IiI111111IIII
   self . Get_site_link ( URL , season_name )
   if 7 - 7: I11i % ooo0oo0o0oo * OOooOOo
 def Get_site_link ( self , url , season_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIi1i11111 )
  Iiiii1i = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIi1i11111 )
  i111i = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIi1i11111 )
  for url in i1I1i :
   self . main ( url , season_name )
  for url in Iiiii1i :
   self . main ( url , season_name )
  for url in i111i :
   self . main ( url , season_name )
   if 58 - 58: ooo0oo0o0oo / oO0o0OOOO + IIiIiII11i % IIIIi1i - ii
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   II1iII1i1i = 'DACLIPS'
   if II1iII1i1i in oOoo0ooOoo . source_list :
    pass
   else :
    self . daclips ( url , season_name , II1iII1i1i )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    II1iII1i1i = 'FILEHOOT'
    if II1iII1i1i in oOoo0ooOoo . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , II1iII1i1i )
   else :
    if 'thevideo.me' in url :
     II1iII1i1i = 'THEVIDEO'
     if II1iII1i1i in oOoo0ooOoo . source_list :
      pass
     else :
      self . thevideo ( url , season_name , II1iII1i1i )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      II1iII1i1i = 'ALLMYVIDEOS'
      if II1iII1i1i in oOoo0ooOoo . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , II1iII1i1i )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       II1iII1i1i = 'VIDSPOT'
       if II1iII1i1i in oOoo0ooOoo . source_list :
        pass
       else :
        self . vidspot ( url , season_name , II1iII1i1i )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        II1iII1i1i = 'VODLOCKER'
        if II1iII1i1i in oOoo0ooOoo . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , II1iII1i1i )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 63 - 63: O0OoO * oO0o0OOOO
         if 22 - 22: Ii1I * o0o00Oo0O * iI11I1II1I1I
 def allmyvid ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
  for ooOOo00 , Iii1IIII11I in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 39 - 39: I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * OOooOOo % o0o00Oo0O
 def vidspot ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIi1i11111 )
  for ooOOo00 , Iii1IIII11I in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 55 - 55: iI11I1II1I1I * IIIIi1i
 def thevideo ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIi1i11111 )
  for ooOOo00 in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 85 - 85: iI11I1II1I1I . IIiIiII11i
 def vodlocker ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIi1i11111 )
  for ooOOo00 in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 54 - 54: O0O0OoOO0 . ii % I1ii11iIi11i
 def daclips ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIi1i11111 )
  for ooOOo00 in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 22 - 22: O0OoO
 def filehoot ( self , url , season_name , source_name ) :
  IIi1i11111 = O000OOo00oo ( url )
  i1I1i = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIi1i11111 )
  for ooOOo00 in i1I1i :
   self . Printer ( ooOOo00 , season_name , source_name )
   if 22 - 22: IIIIi1i * oO0o0OOOO - I1ii11iIi11i * o0o00Oo0O / Ii
 def Printer ( self , Link , season_name , source_name ) :
  if 78 - 78: I1ii11iIi11i * o0o00Oo0O / OO0 + ii + O0OoO
  if Link in oOoo0ooOoo . List :
   pass
  elif source_name in oOoo0ooOoo . source_list :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']' + source_name + '[/COLOR]' , Link , 10012 , i11i1I1 + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   oOoo0ooOoo . List . append ( Link )
   oOoo0ooOoo . source_list . append ( source_name )
   if 23 - 23: IIIIi1i % ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
   xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 94 - 94: ooOoO0O00
   if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
   if 46 - 46: IIIIi1i
   if 65 - 65: ooOoO0O00 . Ii1I / OO0
   if 11 - 11: ooo0oo0o0oo * OO0 / OO0 - O0OoO
def OoO0o0OOOO ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Highlights[/COLOR]' , '' , 10008 , i11i1I1 + 'Highlights.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Fixtures[/COLOR]' , '' , 10009 , i11i1I1 + 'Fixtures.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Live Sport On G-Tv[/COLOR]' , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , i11i1I1 + 'Sport.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , i11i1I1 + 'PremiereLeague.png' , ooOoOoo0O , '' )
 if 39 - 39: Ii1I / ooOoO0O00 * ooo0oo0o0oo - oOo0O0Ooo
def OoOoooo0O ( url ) :
 iiIi1IIi1I ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( o00o )
 for OoO0O , url , Oo0oo , Oo00OOoOo , oOoo , oo0o0000Oo0 , I1ii1i1iiii , Iii1I1I11iiI1 , O0oooo00o0Oo , I1i1I , i1111iI1 in i1I1i :
  Oo0oo = Oo0oo
  if 'Arsenal' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'arsenal-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                                  ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Bournemouth' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'afc-bournemouth.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                       ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Burnley' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'KEGnQWW.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                                   ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Chelsea' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'chelsea.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                                  ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Crystal' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'CrystalPalace.0.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                       ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Everton' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'Everton.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                                   ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Hull' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'hull-city-afc.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                                 ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Leicester' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'leicester-city-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                       ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Liverpool' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'liverpool-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                               ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Manchester City' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'city-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '               ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Manchester United' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + '91.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '          ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Middlesbrough' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'middlesbrough-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                 ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Southampton' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'southampton-fc-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                   ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Stoke City' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'stoke-city.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                          ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Sunderland' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'sunderland-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                        ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Swansea' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'swansea-city-afc.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                    ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Tottenham' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'tottenham-hotspur_zps4e3ed7c1.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '        ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Watford' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'watford-fc-hd-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '                              ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'Bromwich' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'west-bromwich-albion-logo.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '   ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  elif 'West Ham' in Oo0oo :
   ooo0OoOOOOO = i11i1I1 + 'west-ham.png'
   Iii1IIII11I = '[COLOR' + iIii1 + ']' + OoO0O + ' - ' + Oo0oo + '             ' + Oo00OOoOo + '        ' + oOoo + '        ' + oo0o0000Oo0 + '        ' + I1ii1i1iiii + '        ' + Iii1I1I11iiI1 + '        ' + O0oooo00o0Oo + '        ' + I1i1I + '[/COLOR]'
  iiIi1IIi1I ( str ( Iii1IIII11I ) , ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , ooo0OoOOOOO , ooo0OoOOOOO , Oo0oo )
  if 76 - 76: ii - IIiIiII11i % OOooOOo + IIIi + iI11I1II1I1I . OOooOOo
def iI ( description ) :
 Oo0oo = description
 IiI111111IIII = ( 'http://www.fullmatchesandshows.com/?s=' + Oo0oo ) . replace ( ' ' , '%20' )
 o00OOOOOo0OOo ( IiI111111IIII )
 if 44 - 44: oO0o0OOOO * I11i
def II11ii1I11 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1I1i = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiI111111IIII , 10010 , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O00 , ooOoOoo0O , '' )
  if 65 - 65: O0OoO + IIiIiII11i
def Oo0O0OO0OoO0 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Oo0OO0000oooo = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIi1i11111 )
 for Oo0OO0000oooo in Oo0OO0000oooo :
  iIIiI11iI1Ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( Oo0OO0000oooo ) )
  for o00oo in iIIiI11iI1Ii1 :
   o00oo = o00oo
  O0oO0oo0O = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Oo0OO0000oooo ) )
  for oooOOO0ooOoOOO , O00 , time , o0IiIiI111IIII1 in O0oO0oo0O :
   O0000OOO0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0IiIiI111IIII1 )
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + o00oo + ' - ' + oooOOO0ooOoOOO + ' - ' + time + '[/COLOR]' , '' , 10010 , i1iiIII111ii ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + O00 , ooOoOoo0O , ( str ( O0000OOO0 ) ) )
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
 for O00 , url , Iii1IIII11I in i1I1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoOO0ooo ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , O00 )
 for url , O00 , Iii1IIII11I in Iiiii1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , O00 )
def o00OOOOOo0OOo ( url ) :
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
 for url , O00 , Iii1IIII11I in Iiiii1i :
  iii1IiI1i = Iii1IIII11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1IIII11I :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']' + iii1IiI1i + '[/COLOR]' , url , 10013 , O00 )
   if 82 - 82: ooo0oo0o0oo . OOooOOo / OO0 + IIIIi1i - OO0
def o00OOo0o0O ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIi1i11111 )
 for i1i11I1I1iii1 in i1I1i :
  I111Iii1 = ( i1i11I1I1iii1 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o0Ooo0O0 ( 'http:' + I111Iii1 )
  if 30 - 30: ooOoO0O00
  if 75 - 75: oO0o0OOOO . O0OoO - iI11I1II1I1I * oO0o * IIIIi1i
  if 93 - 93: OO0
  if 18 - 18: OO0
def OOOooO00OO00O ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I , O00 in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , url , 8046 , O00 )
 for url in Iiiii1i :
  i11II1I11I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , i11i1I1 + 'Next.png' )
def OoOOooO0O ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  o0Ooo0O0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 3 - 3: IIiIiII11i - O0O0OoOO0 % OOooOOo / IIIi
def Ii1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( o00o )
 for url in i1I1i :
  yt . PlayVideo ( url )
  if 80 - 80: Ii % Ii1I
def OOO00o0 ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 97 - 97: Ii1I / Ii1I / iI11I1II1I1I % ooOoO0O00 . Ii1I . ooo0oo0o0oo
 i1I1i = re . compile ( '<a href="([^"]*)" >(.+?)</a></li>' ) . findall ( o00o )
 if 4 - 4: I1ii11iIi11i - oO0o - Ii * iii1iiii1 / O0O0OoOO0 - O0OoO
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 8041 , i11i1I1 + 'documentary.png' )
  if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
  if 82 - 82: IIiIiII11i / IIIIi1i
  if 96 - 96: I1ii11iIi11i / IIIi . IIiIiII11i . I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooIi111iII ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( 'class="inactive">.+?</a><a href="([^"]*)">Next</a></div>' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I , O00 in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , O00 )
 for Iii1IIII11I , url , O00 in Iiiii1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , O00 )
 for url in next :
  i11II1I11I1 ( 'NEXT PAGE' , url , 8041 , i11i1I1 + 'Next.png' )
  if 83 - 83: ii + oO0o * IIIi . o0o00Oo0O
  if 13 - 13: I11i
def IIi1ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<meta itemprop="name" content="([^"]*)".+?<meta itemprop="thumbnailUrl" content="([^"]*)".+?<meta itemprop="embedUrl" content="([^"]*)".+?<meta itemprop="description" content="([^"]*)" />' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , O00 , url , OOOoOo in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , O00 )
 for url in Iiiii1i :
  Ii1i1i ( ( url ) . replace ( '//' , 'http://' ) )
  if 83 - 83: oO0o0OOOO - Ii1I * IIIi
def Ii1i1i ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<link rel="canonical" href="([^"]*)">  <link rel="stylesheet"' ) . findall ( o00o )
 for url in i1I1i :
  OOoOO0ooo ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11i1I1 + 'documentary.png' )
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
def OO0OooOo ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( o00o )
 for url , Iii1IIII11I , O00 in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , O00 )
 for url in Iiiii1i :
  i11II1I11I1 ( 'NEXT' , url , 8048 , i11i1I1 + 'Next.png' )
def ii111iI1i1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00o )
 Iiiii1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00o )
 for url in i1I1i :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in Iiiii1i :
  if 'rtd' in url :
   OO000 ( url )
   if 31 - 31: oO0o * o0o00Oo0O / oO0o0OOOO . ii * oO0o0OOOO . Ii1I
def OO000 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( o00o )
 for ooOooo000oOO , file in i1I1i :
  url = ( 'https://rtd.rt.com' + ooOooo000oOO + file )
  o0Ooo0O0 ( url )
  if 50 - 50: oO0o * oO0o0OOOO - I11i + ooo0oo0o0oo * oO0o % IIIi
  if 92 - 92: oO0o0OOOO % ooOoO0O00 % OO0 % ooo0oo0o0oo % I11i
def O00Ooo0O0OOOo ( ) :
 IIi1i11111 = IIIIiiIiiI ( 'http://www.stream2watch.co/live-tv' )
 i1I1i = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 , Iii1IIII11I , o0oooo0O in i1I1i :
  i11II1I11I1 ( ( Iii1IIII11I + '[COLOR' + iIii1 + ']' + o0oooo0O + '[/COLOR]' ) , IiI111111IIII , 8086 , O00 )
  if 22 - 22: IIIi * IIIIi1i
def iIIIiIi1i ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 8087 , O00 )
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
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 89 - 89: IIIIi1i * iI11I1II1I1I + Ii . ii
def O0O0 ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1I1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IiI111111IIII , 3002 , 'http://www.solie.org/alibrary/' + O00 )
def oO0oo ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O00 )
def o00o0o000Oo ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 Oooo00OOo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( o00o )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( o00o )
 Iiiii1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , i11i1I1 + 'classicmovies.png' )
 for url , Iii1IIII11I in Oooo00OOo :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']Season- ' + Iii1IIII11I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i11i1I1 + 'classicmovies.png' )
 for url in next :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , i11i1I1 + 'Next.png' )
 for url , O00 , Iii1IIII11I in Iiiii1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O00 )
def iIiII ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( o00o )
 for url in i1I1i :
  OooOO ( url )
def OooOO ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( o00o )
 for url in i1I1i :
  o0Ooo0O0 ( url )
  if 32 - 32: Ii
def II1i ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiI111111IIII , 8065 , i11i1I1 + 'classicmovies.png' )
def IiiiI1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( "v.src = '([^']*)';" ) . findall ( o00o )
 for url in i1I1i :
  iIIIII1ii1I ( url )
  if 34 - 34: O0O0OoOO0 + I1ii11iIi11i - ooOoO0O00 - ooo0oo0o0oo + iI11I1II1I1I
def o0Oo00oOO ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiI111111IIII , 8065 , i11i1I1 + 'classictv.png' )
def O0oo ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  if 'mp4' in url :
   o0Ooo0O0 ( url )
 for url in Iiiii1i :
  yt . PlayVideo ( url )
  if 56 - 56: ooo0oo0o0oo * iii1iiii1
def O00oO0O ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1I1i = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IiI111111IIII , 8071 , i11i1I1 + 'streams.png' )
def IiiI111I11 ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for Iii1IIII11I , url in i1I1i :
  if '(Free Access)' in Iii1IIII11I :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1iiIII111ii ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0OoO000O0OO + '/' + iiI1IiI + url ) . strip ( )
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , i11i1I1 + 'streams.png' )
def oO0Ooooo000 ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , Iii1IIII11I , url in i1I1i :
  url = ( ( i1iiIII111ii ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + O0OoO000O0OO + '/' + iiI1IiI + url ) . strip ( )
  i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , O00 , oO0o0 , '' )
  if 46 - 46: oOo0O0Ooo - oO0o0OOOO / ii - ooOoO0O00 . Ii
def Ii1Ii1IiIIIi1 ( ) :
 OOO0 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OOO0 ( 'Genres' , 'http://www.xvideos.com' , 10106 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OOO0 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OOO0 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , i11i1I1 + 'Jizbox.png' , '' , '' )
 OOO0 ( 'Search' , '' , 10107 , i11i1I1 + 'Jizbox.png' , '' , '' , )
 if 55 - 55: IIIi + o0o00Oo0O / IIIIi1i % OO0 / ii
def O00o0OO0OO0oo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Ooo0O0ooo0o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in Ooo0O0ooo0o :
  OOO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , i11i1I1 + 'Jizbox.png' , '' , '' )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , OOOOO0O00 in i1I1i :
  OOO0 ( ( Iii1IIII11I + ' - No of Videos : ' + ( OOOOO0O00 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
  if 50 - 50: Ii - ii . IIIi + o0o00Oo0O . ooOoO0O00
def OO0Oo00Oo ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Ooo0O0ooo0o = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in Ooo0O0ooo0o :
  OOO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , i11i1I1 + 'Next.png' , '' , '' )
 i1I1i = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , url , Iii1IIII11I , iIiO0O in i1I1i :
  OOO0 ( Iii1IIII11I + '--' + iIiO0O , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( O00 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 71 - 71: Ii1I + oO0o
  if 17 - 17: o0o00Oo0O . O0OoO
def oooO0o0oOoO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , url , Iii1IIII11I , oooOOoooo , I11iii in i1I1i :
  OOO0 ( Iii1IIII11I + ' - Porn Quality : ' + I11iii + ' - ' + oooOOoooo , 'http://www.xvideos.com' + url , 10108 , O00 , O00 , I11iii + ' - ' + oooOOoooo )
 IIi111 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1i11111 )
 for url in IIi111 :
  OOO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Next.png' , '' , '' )
  if 61 - 61: Ii1I - O0OoO
def I1Ii1 ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 Oo0OO0000oooo = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 Ooo0O0ooo0o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIi1i11111 )
 for url in Ooo0O0ooo0o :
  OOO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , i11i1I1 + 'Next.png' , '' , '' )
 i1I1i = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Oo0OO0000oooo ) )
 for url , Iii1IIII11I in i1I1i :
  OOO0 ( Iii1IIII11I , 'http://www.xvideos.com' + url , 10105 , i11i1I1 + 'Jizbox.png' , '' , '' )
  if 67 - 67: oO0o0OOOO % Ii . iI11I1II1I1I * oOo0O0Ooo - oO0o0OOOO + O0O0OoOO0
  if 48 - 48: Ii1I
def o0oi1I1I1I ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iII1III = ( IIIiiI1i1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 I1I = iII1III . lower ( )
 i111i1 = 'http://www.xvideos.com/?k=' + I1I
 print i111i1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi1i11111 = O000OOo00oo ( i111i1 )
 i1I1i = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , IiI111111IIII , Iii1IIII11I , oooOOoooo , I11iii in i1I1i :
  OOO0 ( Iii1IIII11I + ' - Porn Quality : ' + I11iii + ' - ' + oooOOoooo , 'http://www.xvideos.com' + IiI111111IIII , 10108 , O00 , O00 , I11iii + ' - ' + oooOOoooo )
 IIi111 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in IIi111 :
  OOO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IiI111111IIII , 10105 , i11i1I1 + 'Next.png' , '' , '' )
  if 58 - 58: oO0o0OOOO % Ii / Ii * OO0 - iii1iiii1
def i11ii111i1ii ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIi1i11111 )
 Iiiii1i = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIi1i11111 )
 i111i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIi1i11111 )
 for url in i1I1i :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']LOW[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
 for url in Iiiii1i :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']HIGH[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
 for url in i111i :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + iIii1 + ']HLS[/COLOR]' , url , 222 , i11i1I1 + 'Jizbox.png' )
   if 97 - 97: Ii + I1ii11iIi11i * O0OoO % IIIIi1i . ooo0oo0o0oo
def iiOo0 ( url ) :
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 import urlresolver
 try : O0 . play ( url )
 except : pass
 if 71 - 71: OO0 . OO0 - iI11I1II1I1I
 if 22 - 22: ii / Ii1I % IIIIi1i * OOooOOo
def Ii1IiiiI1ii ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 8091 , i11i1I1 + 'gofish.png' )
def o0oOOoo0O ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , O00 in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1092 , O00 )
 for url in next :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 8091 , i11i1I1 + 'Next.png' )
def OoooOo00 ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIi1i11111 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , Iii1IIII11I , O00 in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 8092 , O00 )
 for url in next :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 8091 , i11i1I1 + 'Next.png' )
def OO0III ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( "videoId: '([^']*)'," ) . findall ( IIi1i11111 )
 for url in i1I1i :
  yt . PlayVideo ( url )
  if 59 - 59: ii / ooo0oo0o0oo + oO0o0OOOO . IIIIi1i * O0O0OoOO0 - ii
  if 97 - 97: O0OoO % oOo0O0Ooo * oOo0O0Ooo % I1ii11iIi11i
  if 86 - 86: O0O0OoOO0 * ooOoO0O00 + IIIi
iI1i1I11i = '{PQ},' ; iiiIii1iIi1Ii = '{SC},' ; I1IiI11I1Ii11II = '{XG},' ; oo0ooOoOOoO = '{JP},' ; Oo0000o = '{HW},' ; iI1IiiiIIiiII = '{RT},'
def oOo000o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oOII1i1i1I1iII = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 48 - 48: O0OoO . O0OoO + Ii + Ii1I % o0o00Oo0O
 Ii1i1iI = ( i1iiIII111ii ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0000ii1i1II = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 iiI1ii1IIiI = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IIi1i1I11IIII = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OooOoOOO00O = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIIiiI1i1
 I111iIIII11iI = ( i1iiIII111ii ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oOoOO = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i11I1iIii1i11 = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIiiI11II11i = ( i1iiIII111ii ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 98 - 98: IIIIi1i - IIIIi1i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 58 - 58: IIIi
 if 98 - 98: I11i * oO0o
 I1ii11iI = O0Oo000ooO00 ( Ii1i1iI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 IIi1i = O0Oo000ooO00 ( O0000ii1i1II )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 II11IiI1 = O0Oo000ooO00 ( iiI1ii1IIiI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iIIi11i = O0Oo000ooO00 ( OooOoOOO00O )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 III = O0Oo000ooO00 ( I111iIIII11iI )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iiIi111Ii1II = O0Oo000ooO00 ( oOoOO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOoo0oO = O0Oo000ooO00 ( i11I1iIii1i11 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IIii1i = O0Oo000ooO00 ( iIiiI11II11i )
 if 69 - 69: iii1iiii1 / ii % Ii
 if 18 - 18: Ii - OO0 * IIIi + I11i
 if IIi1i11111 != 'Failed' :
  i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1i11111 )
  for IiiiIi1iiii11 , Iii1IIII11I in i1I1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiI111111IIII + IiiiIi1iiii11 ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 27 - 27: oOo0O0Ooo * IIiIiII11i - oO0o0OOOO
    if 50 - 50: ii + O0OoO / IIiIiII11i * I1ii11iIi11i
    if 59 - 59: O0O0OoOO0 / OOooOOo * oO0o * IIIIi1i % IIIi
    if 61 - 61: I1ii11iIi11i - o0o00Oo0O - ii
    if 4 - 4: IIiIiII11i - IIIi % I1ii11iIi11i * Ii
    if 18 - 18: I1ii11iIi11i % o0o00Oo0O
    if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 if I1ii11iI != 'Failed' :
  i111i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1ii11iI )
  for IiiiIi1iiii11 , Iii1IIII11I in i111i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ii1i1iI + IiiiIi1iiii11 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if IIi1i != 'Failed' :
  IIIIIiiI11i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIi1i )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in IIIIIiiI11i1 :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Silent Hunter[/COLOR]' ) , IiI111111IIII , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 43 - 43: oOo0O0Ooo / IIIIi1i / OO0 + iI11I1II1I1I + ii
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if II11IiI1 != 'Failed' :
  iiI111i1 = [ ]
  IiIii11i1IIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11IiI1 )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in IiIii11i1IIiI :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    if Iii1IIII11I in iiI111i1 :
     pass
    else :
     iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , IiI111111IIII , 1016 , i1i1IIIIi1i , IIIIiii , iII1iii )
     iiI111i1 . append ( Iii1IIII11I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if iIIi11i != 'Failed' :
  I11iIIi = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iIIi11i )
  for IiI111111IIII , O00 , Iii1IIII11I in I11iIIi :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + IiI111111IIII , 7067 , O00 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 5 - 5: iI11I1II1I1I
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if III != 'Failed' :
  Iii1I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in Iii1I11 :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Redemption[/COLOR]' ) , IiI111111IIII , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 94 - 94: O0O0OoOO0 / iii1iiii1 . oOo0O0Ooo . IIIIi1i - ii / iI11I1II1I1I
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if iiIi111Ii1II != 'Failed' :
  i111IIiIII1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiIi111Ii1II )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in i111IIiIII1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Reaper[/COLOR]' ) , IiI111111IIII , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 74 - 74: IIiIiII11i / o0o00Oo0O
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if oOoo0oO != 'Failed' :
  O0oo0ooo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoo0oO )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in O0oo0ooo0 :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i1I1iI1iIi111i ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Herovision[/COLOR]' ) , IiI111111IIII , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 19 - 19: ooOoO0O00
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: O0O0OoOO0 * OOooOOo / I11i . iii1iiii1
 if IIii1i != 'Failed' :
  i1I1iiii1Ii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIii1i )
  for IiI111111IIII , i1i1IIIIi1i , Iii1IIII11I in i1I1iiii1Ii11 :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Silent Hunter[/COLOR]' ) , IiI111111IIII , 222 , i1i1IIIIi1i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 25 - 25: Ii / OOooOOo - iii1iiii1 / oO0o . I11i . I11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 i11oooOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 6 - 6: IIIi . oO0o0OOOO
 for oo0OoOOooO in i11oooOo :
  o0o0OO0o00o0O = oo0OooOOo0 + oo0OoOOooO + iIi1ii1I1
  iIIII1 = O0Oo000ooO00 ( o0o0OO0o00o0O )
  if iIIII1 != 'Failed' :
   Oooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII1 )
   for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in Oooo :
    if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
     i1I1iI1iIi111i ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source Pandoras[/COLOR]' , IiI111111IIII , 222 , i1i1IIIIi1i , IIIIiii , iII1iii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 7 - 7: ooOoO0O00
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: iI11I1II1I1I + ooo0oo0o0oo % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
 i11oooOo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 60 - 60: I11i . OOooOOo % iii1iiii1 / oOo0O0Ooo / o0o00Oo0O
 if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / O0OoO . Ii1I * OO0
 for oo0OoOOooO in i11oooOo :
  o0o0OO0o00o0O = oOII1i1i1I1iII + oo0OoOOooO
  oo0O = O0Oo000ooO00 ( o0o0OO0o00o0O )
  if oo0O != 'Failed' :
   Ooooo0O0 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O )
   for IiiiIi1iiii11 , Iii1IIII11I in Ooooo0O0 :
    if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
     OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOII1i1i1I1iII + oo0OoOOooO + IiiiIi1iiii11 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 99 - 99: I1ii11iIi11i + Ii
     oOooOo0 ( 'tvshows' , 'Media Info 3' )
     if 36 - 36: O0O0OoOO0 * iii1iiii1 * iI11I1II1I1I - oO0o0OOOO % Ii
     if 98 - 98: iI11I1II1I1I - ooOoO0O00 + OO0 % oO0o0OOOO + OO0 / IIIi
def O0O0Oo00OO ( ) :
 if 100 - 100: I11i . oOo0O0Ooo
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 if 62 - 62: OO0 + IIiIiII11i % OO0
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( IIIiiI1i1 ) . replace ( ' ' , '%20' )
 oo00o0 = ( i1iiIII111ii ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 Ii1i1iI = ( i1iiIII111ii ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 O0000ii1i1II = ( i1iiIII111ii ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iiI1ii1IIiI = ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1I ) . replace ( ' ' , '+' )
 IIi1i1I11IIII = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OooOoOOO00O = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 I111iIIII11iI = ( i1iiIII111ii ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 50 - 50: ii + IIIi * oOo0O0Ooo - O0O0OoOO0 / Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 5 - 5: o0o00Oo0O - oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ooOO00O00oo = O0Oo000ooO00 ( oo00o0 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 I1ii11iI = O0Oo000ooO00 ( Ii1i1iI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IIi1i = O0Oo000ooO00 ( O0000ii1i1II )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 II11IiI1 = cloudflare . source ( iiI1ii1IIiI )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oo0O = O0Oo000ooO00 ( IIi1i1I11IIII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIIi11i = O0Oo000ooO00 ( OooOoOOO00O )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 III = O0Oo000ooO00 ( I111iIIII11iI )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 44 - 44: IIiIiII11i . IIiIiII11i + O0OoO * O0O0OoOO0
 if III != 'Failed' :
  Iii1I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in Iii1I11 :
   if I1I in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source HeroVision[/COLOR]' ) , IiI111111IIII , 1016 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 16 - 16: IIiIiII11i
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 100 - 100: o0o00Oo0O - ooOoO0O00
 if iIIi11i != 'Failed' :
  I11iIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi11i )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in I11iIIi :
   if I1I in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- source Reaper[/COLOR]' ) , IiI111111IIII , 1016 , i1i1IIIIi1i , IIIIiii , iII1iii )
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
  for O00 , IiI111111IIII , Iii1IIII11I in i1I1i :
   if I1I in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + IiI111111IIII , 10044 , O00 , '' , '' )
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
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in Iiiii1i :
   if I1I in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , IiI111111IIII , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 72 - 72: O0O0OoOO0 / I1ii11iIi11i / IIIi * OOooOOo + O0OoO
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if I1ii11iI != 'Failed' :
  i111i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1ii11iI )
  for Iii1IIII11I in i111i :
   if I1I in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1i1iI + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - ooo0oo0o0oo . ii
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if IIi1i != 'Failed' :
  IIIIIiiI11i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i )
  for Iii1IIII11I in IIIIIiiI11i1 :
   if I1I in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0000ii1i1II + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 10 - 10: iii1iiii1
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if II11IiI1 != 'Failed' :
  IiIii11i1IIiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11IiI1 )
  for IiI111111IIII , O00 , Iii1IIII11I in IiIii11i1IIiI :
   if I1I in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source - Dizi[/COLOR]' , IiI111111IIII , 8062 , O00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 48 - 48: IIIIi1i * ooOoO0O00 % ii * O0O0OoOO0 * oO0o
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if oo0O != 'Failed' :
  Ooooo0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O )
  for IiI111111IIII , i1i1IIIIi1i , iII1iii , IIIIiii , Iii1IIII11I in Ooooo0O0 :
   if I1I in Iii1IIII11I . lower ( ) :
    iiIi1IIi1I ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '- Source Scooby[/COLOR]' ) , IiI111111IIII , 1016 , i1i1IIIIi1i , IIIIiii , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 7 - 7: IIIIi1i . O0O0OoOO0 . IIIIi1i - iii1iiii1
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: OO0 + ii - oO0o / ooOoO0O00 / ii
 OOO0IIIIii11II1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if oo0O != 'Failed' :
  for oo0OoOOooO in OOO0IIIIii11II1I :
   o0o0OO0o00o0O = oo0OooOOo0 + oo0OoOOooO + iIi1ii1I1
   oOoo0oO = O000OOo00oo ( o0o0OO0o00o0O )
   if oOoo0oO != 'Failed' :
    O0oo0ooo0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOoo0oO )
    for Iii1IIII11I , iII1iii , IiI111111IIII , O00 , oO0o0 , OoiI1I1 in O0oo0ooo0 :
     if I1I in Iii1IIII11I . lower ( ) :
      iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' - Source Pandoras[/COLOR]' , IiI111111IIII , OoiI1I1 , O00 , oO0o0 , iII1iii )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 48 - 48: Ii1I - o0o00Oo0O . oO0o
      oOooOo0 ( 'tvshows' , 'Media Info 3' )
      if 38 - 38: o0o00Oo0O
      if 79 - 79: ooOoO0O00 . IIIi
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1i1i11iI11II ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IIIiiI1i1 ) . replace ( ' ' , '+' )
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / O0O0OoOO0
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 14 - 14: iii1iiii1 % ooo0oo0o0oo - o0o00Oo0O / iii1iiii1
 if IIi1i11111 != 'Failed' :
  Iiiii1i = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( IIi1i11111 )
  for IiI111111IIII , Iii1IIII11I in Iiiii1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    OOoOO0ooo ( ( Iii1IIII11I + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + IiI111111IIII ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 91 - 91: Ii % iii1iiii1 * IIIi - Ii1I . iii1iiii1
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
iIo00oo = '{ZH},' ; O000Oo00 = '{IX},' ; iI1oOoo = '{LM},'
if 59 - 59: ooo0oo0o0oo % O0O0OoOO0
def O0ooo ( url ) :
 IiIIiII1I = cloudflare . source ( url )
 i1I1i = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IiIIiII1I )
 for url , o0oOoOo0 , Ooo00OoOOO , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( o0oOoOo0 ) . replace ( 'Sezon' , ' Season ' ) + ( Ooo00OoOOO ) . replace ( 'Bölüm' , ' Episode ' ) + Iii1IIII11I , url , 8063 , '' )
  if 92 - 92: iii1iiii1 % O0O0OoOO0
  if 30 - 30: IIiIiII11i - I11i % iii1iiii1 . oO0o0OOOO
  if 63 - 63: iI11I1II1I1I / OO0
  if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % O0OoO * OOooOOo - iI11I1II1I1I
def iI1ii ( url ) :
 IiIIiII1I = cloudflare . source ( url )
 i1I1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IiIIiII1I )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , url , 222 , '' )
  if 61 - 61: I1ii11iIi11i * ooOoO0O00 . ii
  if 44 - 44: oOo0O0Ooo
  if 55 - 55: IIIi . iii1iiii1 * iii1iiii1
  if 82 - 82: oOo0O0Ooo % oO0o % oO0o0OOOO + oO0o0OOOO
def i1111I ( ) :
 if 58 - 58: ii - oO0o0OOOO + iI11I1II1I1I * Ii
 IiIIiII1I = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1I1i = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IiIIiII1I )
 for IiI111111IIII , O00 , Iii1IIII11I , Ooo00OoOOO in i1I1i :
  i11II1I11I1 ( Iii1IIII11I + '  -  ' + ( Ooo00OoOOO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiI111111IIII , 8063 , O00 )
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - IIIi + O0OoO + IIIIi1i % IIIi
def IiiII ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I , O00 in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 8002 , O00 )
def I1ii1iI ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( o00o )
 for O00 , time , url , Iii1IIII11I , OOOoOo in i1I1i :
  iiIi1IIi1I ( '%s %s' % ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , time ) , url , 1015 , O00 , OOOoOo )
  if 32 - 32: ii
def ooOoOooo00Oo ( ) :
 if 72 - 72: oO0o0OOOO
 i11II1I11I1 ( 'Coronation Street' , '' , 8001 , '' )
 i11II1I11I1 ( 'Eastenders' , '' , 8002 , '' )
 i11II1I11I1 ( 'Emmerdale' , '' , 8003 , '' )
 i11II1I11I1 ( 'Hollyoaks' , '' , 8004 , '' )
 i11II1I11I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 26 - 26: ooo0oo0o0oo % I1ii11iIi11i
 if 72 - 72: o0o00Oo0O + I11i + oOo0O0Ooo / I1ii11iIi11i
 if 83 - 83: ooo0oo0o0oo - oOo0O0Ooo . O0O0OoOO0
 if 34 - 34: OOooOOo - IIIi * ii
def IiI1I1IIIi1i ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Holly' in Iii1IIII11I :
   O00 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IiI111111IIII :
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , O00 )
   else :
    pass
    if 73 - 73: o0o00Oo0O * iii1iiii1 . ooOoO0O00
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 51 - 51: oO0o - IIIIi1i % o0o00Oo0O - OOooOOo
def o0ooo ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'East' in Iii1IIII11I :
   O00 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IiI111111IIII :
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , O00 )
   else :
    pass
    if 77 - 77: oO0o0OOOO + ooOoO0O00 . oO0o0OOOO
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: I11i + O0OoO * IIIi
def i1iI1IIi ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Emmer' in Iii1IIII11I :
   O00 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IiI111111IIII :
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , O00 )
   else :
    pass
    if 27 - 27: o0o00Oo0O / oO0o
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: O0O0OoOO0 - ooo0oo0o0oo * iI11I1II1I1I . IIiIiII11i
def OooO00o000 ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Coro' in Iii1IIII11I :
   O00 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IiI111111IIII :
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , O00 )
   else :
    pass
    if 36 - 36: oO0o0OOOO - ooo0oo0o0oo . ooo0oo0o0oo
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( ) :
 IIi1i11111 = O000OOo00oo ( 'http://uksoapshare.blogspot.co.uk/' )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Celeb' in Iii1IIII11I :
   O00 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IiI111111IIII :
    OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiI111111IIII . replace ( '\\/' , '/' ) , 8006 , O00 )
   else :
    pass
    if 90 - 90: IIIi + oO0o + Ii1I - iii1iiii1
def iI1I1I ( name , url ) :
 ii11 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ii11 :
  oOOooooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  o00o = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( o00o ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  o00o = open_url ( url )
  o000Ooo00o00O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( o00o ) [ - 1 ]
  oOOooooO = o000Ooo00o00O . replace ( '\\/' , '/' )
 O00oO0o000oO = xbmcgui . ListItem ( name , '' , '' )
 O00oO0o000oO . setPath ( oOOooooO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00oO0o000oO )
 if 80 - 80: IIIIi1i
 if 3 - 3: Ii1I * oO0o0OOOO
def Oo00O ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1I1i = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( o00o )
 Iiiii1i = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IiI111111IIII , 7071 , i11i1I1 + 'popcorn.png' )
 for IiI111111IIII , Iii1IIII11I in Iiiii1i :
  i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IiI111111IIII , 7071 , i11i1I1 + 'popcorn.png' )
  if 44 - 44: OO0 * oO0o0OOOO
def i1ooOO00o0 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1I1i = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'Movies' in Iii1IIII11I :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( IiI111111IIII ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , i11i1I1 + 'popcorn.png' )
def Ii1I1iIiiI1 ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o00o )
 i1I1i = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O00 )
 for url in Iiiii1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , i11i1I1 + 'Next.png' )
  if 68 - 68: IIIIi1i . oO0o0OOOO
  if 29 - 29: OO0 * ooo0oo0o0oo
def oOiiIIIII ( url ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1I1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , url , O00 in i1I1i :
  if '{{' in Iii1IIII11I :
   pass
  else :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , O00 )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
iiI1 = '{UJ},' ; iii11i1 = '{WE},' ; IIiI1I1IIiiI1 = '{WP},' ; oooOOO0o0O0 = '{PP},'
def iiiI1IiI ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , url , O00 in i1I1i :
  if '{{' in Iii1IIII11I :
   pass
  else :
   i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O00 )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii111IIIIii ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  O00oIii1iIIiii1ii ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00oIii1iIIiii1ii ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , i11i1I1 + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . O0O0OoOO0 % oO0o
 if 2 - 2: ii - O0O0OoOO0 % IIIi / oOo0O0Ooo / I11i
 if 3 - 3: IIiIiII11i / O0OoO
def i1I ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o00o )
 Iiiii1i = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  if '(cooltvseries.com)' in Iii1IIII11I :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i11i1I1 + 'CoolSeries.png' )
 for url , Iii1IIII11I in Iiiii1i :
  if '(cooltvseries.com)' in Iii1IIII11I :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , i11i1I1 + 'CoolSeries.png' )
def IiiIIIIi ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( o00o )
 for url in i1I1i :
  o0Ooo0O0 ( ( url ) . replace ( ' ' , '%20' ) )
IiIIIi = '{XX},' ; Oo0iII = '{UD},' ; O0ooiIIi1 = '{YT},' ; OoOo0O00 = '{JS},' ; iI1i1iI1iI = '{PF},'
if 18 - 18: oO0o0OOOO + I1ii11iIi11i - oO0o / iii1iiii1 / O0OoO
def OOoOoO ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1I1i = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I , O00 in i1I1i :
  OOoOO0ooo ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1iiIII111ii ( IiI111111IIII ) ) , 222 , O00 )
  if 72 - 72: OOooOOo / iii1iiii1 * ooo0oo0o0oo % iI11I1II1I1I
def OOiii1IiiIiIIiI ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( o00o )
 for O00 , url , Iii1IIII11I in i1I1i :
  if 'youtu' in url :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + O00 )
 for url in next :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']NEXT[/COLOR]' , url , 7050 , i11i1I1 + 'Next.png' )
  if 93 - 93: ooo0oo0o0oo % Ii1I
def IiIIii ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 74 - 74: iI11I1II1I1I / O0O0OoOO0
def O0Oo0Oo00o0o ( url ) :
 o00o = O000OOo00oo
 i1I1i = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 222 , O00 )
  if 17 - 17: ooo0oo0o0oo / I11i . O0OoO + I11i / Ii1I . I1ii11iIi11i
  if 39 - 39: I11i / ooo0oo0o0oo - IIIIi1i
  if 96 - 96: oO0o0OOOO * Ii1I * O0O0OoOO0 + Ii1I % oOo0O0Ooo + Ii
  if 37 - 37: oO0o0OOOO % Ii1I / OO0
  if 94 - 94: oO0o0OOOO / oO0o . I11i
def iIiOo ( ) :
 if 48 - 48: O0OoO
 i11II1I11I1 ( 'All Channels' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Entertainment' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Movies' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Music' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'News' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Sports' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Documentary' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Kids' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Food' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Religious' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'USA Channels' , '' , 7021 , i11i1I1 + 'livetv.png' )
 i11II1I11I1 ( 'Other' , '' , 7021 , i11i1I1 + 'livetv.png' )
 if 26 - 26: IIIIi1i * iii1iiii1 * IIIi * OOooOOo
 if 48 - 48: IIIIi1i % Ii . ii * ooo0oo0o0oo % oO0o . IIIIi1i
def IiOOo0 ( Cat_Name ) :
 if 85 - 85: iii1iiii1 % Ii1I
 OO00o0O0oOooO = False
 IiiIII1IIii1 = '0'
 if Cat_Name == 'All Channels' : OO00o0O0oOooO = True
 if Cat_Name == 'Entertainment' : IiiIII1IIii1 = '1'
 if Cat_Name == 'Movies' : IiiIII1IIii1 = '2'
 if Cat_Name == 'Music' : IiiIII1IIii1 = '3'
 if Cat_Name == 'News' : IiiIII1IIii1 = '4'
 if Cat_Name == 'Sports' : IiiIII1IIii1 = '5'
 if Cat_Name == 'Documentary' : IiiIII1IIii1 = '6'
 if Cat_Name == 'Kids' : IiiIII1IIii1 = '7'
 if Cat_Name == 'Food' : IiiIII1IIii1 = '8'
 if Cat_Name == 'Religious' : IiiIII1IIii1 = '9'
 if Cat_Name == 'USA Channels' : IiiIII1IIii1 = '10'
 if Cat_Name == 'Other' : IiiIII1IIii1 = '11'
 if 19 - 19: O0O0OoOO0 * ooOoO0O00 % o0o00Oo0O + oO0o0OOOO
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1I1i = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00o )
 print 'Len Match: >>>' + str ( len ( i1I1i ) )
 for Iii1IIII11I , O00 , I1i1ii1ii in i1I1i :
  i1ii = i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O00 ) . replace ( '\\' , '' )
  if I1i1ii1ii == IiiIII1IIii1 :
   i11II1I11I1 ( Iii1IIII11I , '' , 7022 , i1ii )
  elif OO00o0O0oOooO == True :
   i11II1I11I1 ( Iii1IIII11I , '' , 7022 , i1ii )
  else : pass
  if 70 - 70: Ii1I + oOo0O0Ooo
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 65 - 65: IIIIi1i - IIIIi1i . I1ii11iIi11i
def oO00o0O00o ( Search_Name ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1I1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o00o )
 i1I1i = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o00o )
 for O00 , IiI111111IIII , oo00o0 , Ii1i1iI in i1I1i :
  i1ii = i1iiIII111ii ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O00 ) . replace ( '\\' , '' )
  OOoOO0ooo ( Search_Name + ': Link 1' , ( IiI111111IIII ) . replace ( '\\' , '' ) , 222 , i1ii )
  OOoOO0ooo ( Search_Name + ': Link 2' , ( oo00o0 ) . replace ( '\\' , '' ) , 222 , i1ii )
  OOoOO0ooo ( Search_Name + ': Link 3' , ( Ii1i1iI ) . replace ( '\\' , '' ) , 222 , i1ii )
  if 78 - 78: Ii + iI11I1II1I1I
def oOOI1 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , i11i1I1 + 'english.png' )
def OOI1i ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , i11i1I1 + 'xxx.png' )
def i1II1iII1 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1I1i = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for Iii1IIII11I , IiI111111IIII in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , ( IiI111111IIII ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , i11i1I1 + 'vod(1).png' )
  if 31 - 31: O0O0OoOO0 * I11i * O0O0OoOO0 + oO0o * I11i . iii1iiii1
def Oo00oo00o00Oo ( url ) :
 url
 OOOo00 = xbmcgui . ListItem ( Iii1IIII11I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOo00 )
 return
 if 1 - 1: ooo0oo0o0oo
 if 31 - 31: ooOoO0O00
def i11I ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( o00o )
 for url , iII1iii , O00 , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + O00 , '' , ( iII1iii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oOooOo0 ( 'tvshows' , 'Media Info 3' )
 for url in Iiiii1i :
  i11II1I11I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , i11i1I1 + 'Next.png' )
  if 48 - 48: O0OoO + iii1iiii1 % O0OoO
def Ooo0o0000OO ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIi1i11111 )
 for url , iII1iii , O00 in i1I1i :
  i1I1iI1iIi111i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + O00 , '' , iII1iii )
  oOooOo0 ( 'tvshows' , 'Media Info 3' )
 OoOoO0OooOOo = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 )
 for iIiI1II1I1 in OoOoO0OooOOo :
  OooiIiI1i1Ii = ( iIiI1II1I1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiIi1IIi1I ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + O00 , '' , OooiIiI1i1Ii )
  if 69 - 69: o0o00Oo0O + iI11I1II1I1I % IIIIi1i * oOo0O0Ooo . I1ii11iIi11i - OOooOOo
def I1iiII ( INFO ) :
 ii1I ( 'info for workout' , INFO )
 if 81 - 81: OOooOOo + I11i + I1ii11iIi11i
 if 79 - 79: I1ii11iIi11i - ii % iii1iiii1 + ii - oO0o0OOOO % OOooOOo
 if 5 - 5: OOooOOo . I1ii11iIi11i
def OOo0O ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'Name=(.+?)\n.+?m3u=(.+?)\n' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  i11II1I11I1 ( ( Iii1IIII11I ) . replace ( 'SlyNet' , '' ) , url , 9032 , i11i1I1 + 'Sport.png' )
def iiOo0ooo ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , url , 9032 , i11i1I1 + 'icon.png' )
def Oo00o00 ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '#EXTINF:-.+?,(.+?)\n(.+?)\n' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  if '=' in Iii1IIII11I :
   pass
  else :
   OOoOO0ooo ( ( Iii1IIII11I ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , i11i1I1 + 'icon.png' )
def OoOo0O0 ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  if '=' in Iii1IIII11I :
   pass
  else :
   OOoOO0ooo ( Iii1IIII11I , url , 222 , i11i1I1 + 'icon.png' )
   if 39 - 39: iii1iiii1 . oO0o % OO0 . O0OoO / IIIIi1i * oO0o
   if 12 - 12: oOo0O0Ooo / I11i
   if 86 - 86: I1ii11iIi11i % OOooOOo
def o0o0O00oOo ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3d3dy5yYW1hbGluLmNvbS8=' ) )
 i1I1i = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" >(.+?)</a>(.+?)</li>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I , iIiO0O in i1I1i :
  if 'category' in IiI111111IIII :
   i11II1I11I1 ( Iii1IIII11I + iIiO0O , IiI111111IIII , 9005 , i11i1I1 + 'disclose.png' )
def iI1iiii ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="entry-thumb">.+?<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , url , 9006 , O00 )
def OOoO0oOOO ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<br />\n#EXTINF:.+?,(.+?)<br />\n(.+?)<br />' , re . DOTALL ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  OOoOO0ooo ( Iii1IIII11I , url , 10012 , '' )
  if 47 - 47: O0OoO / IIiIiII11i % ooo0oo0o0oo . IIIi * Ii1I
def iIii1iIiII1i1 ( ) :
 o00o = O000OOo00oo ( i1iiIII111ii ( 'aHR0cDovL3NvdXJjZXR2LmluZm8v' ) )
 i1I1i = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 9008 , i11i1I1 + 'disclose.png' )
def o0oO ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="article-image darken"><a href="([^"]*)"><img width="320" height="205" src="([^"]*)".+?title="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , url , 9009 , O00 )
def o0OoIII1IIiIi1 ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  OOoOO0ooo ( ( Iii1IIII11I ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 97 - 97: I11i / ooo0oo0o0oo + OOooOOo + oO0o % iii1iiii1
def iIIi1II1 ( ) :
 o00o = cloudflare . source ( i1iiIII111ii ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if '.m3u' in IiI111111IIII :
   i11II1I11I1 ( ( Iii1IIII11I ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i1iiIII111ii ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + IiI111111IIII ) , 9011 , i11i1I1 + 'disclose.png' )
def IiI1I11ii ( url ) :
 o00o = cloudflare . source ( url )
 i1I1i = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  OOoOO0ooo ( ( Iii1IIII11I ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 57 - 57: I1ii11iIi11i . ooo0oo0o0oo % O0OoO
def OoO0o00oo0oO ( ) :
 o00o = O000OOo00oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1I1i = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  if 'category' in IiI111111IIII :
   i11II1I11I1 ( Iii1IIII11I , 'http://www.disclose.tv/' + IiI111111IIII , 7010 , i11i1I1 + 'disclose.png' )
   if 25 - 25: O0O0OoOO0 * I11i * IIIi . oOo0O0Ooo
   if 93 - 93: OOooOOo
def o0OoOo0o0OOoO0 ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00o )
 for url , Iii1IIII11I , O00 in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , 'http://www.disclose.tv/' + url , 7011 , O00 )
 for url in next :
  i11II1I11I1 ( 'NEXT' , url , 7010 , i11i1I1 + 'Next.png' )
  if 30 - 30: O0O0OoOO0 % oO0o0OOOO + I11i
  if 65 - 65: iI11I1II1I1I . IIIIi1i / O0O0OoOO0
def iI11ii ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( o00o )
 i111i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  if 'http' in url :
   OOoOO0ooo ( 'video/flv' , url , 222 , i11i1I1 + 'disclose.png' )
 for url , Iii1IIII11I in Iiiii1i :
  OOoOO0ooo ( Iii1IIII11I , url , 222 , i11i1I1 + 'disclose.png' )
 for url in i111i :
  OOoOO0ooo ( 'YT Link' , url , 8043 , i11i1I1 + 'disclose.png' )
  if 65 - 65: ooo0oo0o0oo
  if 50 - 50: IIiIiII11i / oO0o
def OO0oooOO ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , i11i1I1 + 'icon.png' )
  if 30 - 30: IIIi . oO0o + oO0o0OOOO / iI11I1II1I1I % I1ii11iIi11i / IIIi
def iIi11ooOo0oO0O ( name , url , img ) :
 IIi1i11111 = O000OOo00oo ( url )
 I1i1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIi1i11111 )
 ii11o00000O = len ( I1i1 )
 if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 if 33 - 33: Ii1I
 if ii11o00000O == 1 :
  for O0oOoo00Oo0O in I1i1 :
   O0oOoo00Oo0O = O0oOoo00Oo0O . replace ( 'player' , 'watch' )
   Iii1i1Ii = O0oOoo00Oo0O + '&fv=&sou='
   III1iIii = O000OOo00oo ( Iii1i1Ii )
   iiIII1i1 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( III1iIii )
   for ooOOo00 in iiIII1i1 :
    oOOo0OOoOO0 = False
    Resolve ( ooOOo00 )
    if 30 - 30: IIiIiII11i / oOo0O0Ooo - OO0 + OOooOOo * OO0 / OOooOOo
 elif ii11o00000O > 1 :
  if 17 - 17: oO0o
  for O0oOoo00Oo0O in I1i1 :
   IIIi11i = O000OOo00oo ( O0oOoo00Oo0O )
   oooOOoo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIIi11i )
   Oo00O00o0 = oooOOoo0
   Oo00O00o0 = ( str ( Oo00O00o0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + Oo00O00o0
   OOoOO0ooo ( 'DOUBLE LINK' , Oo00O00o0 , 424 , '' )
   if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + O0O0OoOO0 + oO0o
   for url in oooOOoo0 :
    i11II1I11I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oo00o0 = Google . resolve ( url )
    except :
     pass
    try :
     o00o0o0oOo0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oo00o0 ) )
     for IiI1 , iI1I1 in o00o0o0oOo0 :
      if 5 - 5: iii1iiii1 % IIiIiII11i + I1ii11iIi11i - iI11I1II1I1I
      HD_URLS . append ( IiI1 )
      SD_URLS . append ( iI1I1 )
    except :
     pass
 else :
  pass
  if 64 - 64: iii1iiii1 + iI11I1II1I1I
def I1Iii ( ) :
 if 30 - 30: ooOoO0O00 . Ii1I
 if 77 - 77: IIiIiII11i - Ii
 i11II1I11I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , i11i1I1 + 'Movies.png' )
 if 78 - 78: O0O0OoOO0
 i11II1I11I1 ( 'Search Movies' , '' , 7017 , i11i1I1 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 72 - 72: iii1iiii1 * oO0o
 if 89 - 89: OOooOOo + oOo0O0Ooo
def O0ooO ( ) :
 o00o = O000OOo00oo ( 'http://cnfstudio.com/' )
 i1I1i = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , 'http://cnfstudio.com/genre/' + IiI111111IIII , 7003 , i11i1I1 + 'icon.png' )
  if 40 - 40: I11i . I11i * Ii
oooOOOOO = xbmcgui . Dialog ( )
if 44 - 44: I11i
OOO0O00 = '{UN},' ; Oo0O000OoO00 = '{IG},' ; oOO00OoOo = '{PL},' ; oOoooO0OO00 = '{LO},' ; IiiI = '{LP},' ; O0oooooO = '{HA},' ; IIi1 = '{XD},' ; II11II = '{TA},' ; i1ii11 = '{DP},' ; IIIo00O = '{JT},' ; ii1I1I1 = '{JJ},' ; oo0oOOO0oOoo = '{MM},' ; Ii1o0OOOoo0000 = '{FQ},' ; IiIIii1i1i11iII = '{HH},'
if 53 - 53: Ii
def ooO00OoOOoO0o ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o00o )
 o0O00ooo0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( o00o )
 for O00 , url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , O00 )
 o0O00ooo0 = o0O00ooo0
 for url in o0O00ooo0 :
  i11II1I11I1 ( 'Next Page' , url , 7003 , i11i1I1 + 'Next.png' )
  if 23 - 23: o0o00Oo0O
def Iiio0OO00oOOO0o0 ( url ) :
 if 39 - 39: ii
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  ooOooo000oOO = url + '&fv=&sou='
  ooOooo000oOO = ooOooo000oOO . replace ( 'player' , 'watch' )
  i1iIII1IIi = Oo0oo0OOO0OOoOO ( ooOooo000oOO )
  oOoO = Oo0oo0OOO0OOoOO ( url )
  if 30 - 30: oO0o / o0o00Oo0O * I11i * iii1iiii1 + ii * IIIIi1i
  if 23 - 23: oO0o0OOOO
def Oo0oo0OOO0OOoOO ( url ) :
 if 36 - 36: ooo0oo0o0oo . IIIIi1i - ooOoO0O00 + iii1iiii1
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( o00o )
 for url in i1I1i :
  iIIIII1ii1I ( url )
  if 54 - 54: ii . IIIi - IIIIi1i
  if 76 - 76: iii1iiii1
def O00o0 ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Local M3u[/COLOR]' , OOooO0OOoo , 2001 , i11i1I1 + 'LocalM3U.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']Remote M3u[/COLOR]' , iI111I11I1I1 , 7080 , i11i1I1 + 'RemoteM3U.png' , ooOoOoo0O , '' )
 if 98 - 98: iI11I1II1I1I + Ii * Ii1I / iii1iiii1 / OO0 - o0o00Oo0O
def i111i1IIi1i ( ) :
 if os . path . exists ( OOooO0OOoo ) :
  oo00oO00oooo = open ( OOooO0OOoo , 'r' )
  for OOOo00 in oo00oO00oooo :
   ooo0Oo00O = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOOo00 )
   for Iii1IIII11I , IiI111111IIII in ooo0Oo00O :
    OOoOO0ooo ( Iii1IIII11I , IiI111111IIII , 222 , i11i1I1 + 'streams.png' )
 else :
  oooOOOOO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 28 - 28: ooo0oo0o0oo + OOooOOo . ooo0oo0o0oo - O0O0OoOO0 % ooOoO0O00 % iI11I1II1I1I
def OO0O00OO0 ( url ) :
 if os . path . exists ( Remote ) :
  IIi1i11111 = IIIIiiIiiI ( url )
  i1I1i = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
  for Iii1IIII11I , url in i1I1i :
   url = ( url ) . strip ( )
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oooOOOOO . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 29 - 29: IIiIiII11i / oO0o - OO0 * iI11I1II1I1I . IIIIi1i
  if 25 - 25: O0OoO - O0O0OoOO0 . oO0o0OOOO
def o0O0OOO0Ooo ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1I1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in i1I1i :
  IiI111111IIII = i1iiIII111ii ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IiI111111IIII
 Iii1IIII11I = 'plugin.video.GenieTv'
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - OO0 % iI11I1II1I1I - O0O0OoOO0
 III1I11II11I ( IiI111111IIII , Iii1IIII11I )
 if 78 - 78: Ii1I . iii1iiii1 . iii1iiii1 . oO0o0OOOO % IIIIi1i
def ooOOOoO ( ) :
 IIi1i11111 = O000OOo00oo ( i1iiIII111ii ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1I1i = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIi1i11111 )
 for IiI111111IIII in i1I1i :
  IiI111111IIII = i1iiIII111ii ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IiI111111IIII
 Iii1IIII11I = 'repository.GenieTv'
 if 26 - 26: OO0 + oO0o / OOooOOo . IIiIiII11i * O0O0OoOO0
 III1I11II11I ( IiI111111IIII , Iii1IIII11I )
 if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + IIIIi1i % oOo0O0Ooo * IIIi
 if 74 - 74: IIIIi1i / oO0o0OOOO . oOo0O0Ooo - ii + IIiIiII11i + oO0o0OOOO
def I11iiI11I1II ( ) :
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']CATAGORIES[/COLOR]' , '' , 10051 , i11i1I1 + 'Catagories.png' , ooOoOoo0O , '' )
 iiIi1IIi1I ( '[COLOR' + iIii1 + ']SEARCH[/COLOR]' , '' , 10052 , i11i1I1 + 'Search.png' , ooOoOoo0O , '' )
 if 70 - 70: Ii1I . ooo0oo0o0oo
 if 41 - 41: I11i % I1ii11iIi11i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oooOOOOO = xbmcgui . Dialog ( )
i11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
o00oOo0OoO0oO = 'https://addons.tvaddons.ag/'
if 84 - 84: ooOoO0O00 / ooOoO0O00 - ooOoO0O00 . IIIi . oO0o * Ii1I
def oOO000000oO0 ( ) :
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 i111i1 = 'https://addons.tvaddons.ag/search/?keyword=' + I1I
 IIi1i11111 = O000OOo00oo ( i111i1 )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , IiI111111IIII , 10054 , 'https://addons.tvaddons.ag/' + ooo0OoOOOOO , ooOoOoo0O , '' )
  if 94 - 94: OO0 + iI11I1II1I1I
  if 86 - 86: I11i / OO0 . I11i % oOo0O0Ooo + IIIi % oO0o0OOOO
def O0OOoOOO ( ) :
 IIi1i11111 = O000OOo00oo ( o00oOo0OoO0oO )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  if 'Repositories' in Iii1IIII11I :
   pass
  elif 'Services' in Iii1IIII11I :
   pass
  elif 'International' in Iii1IIII11I :
   pass
  else :
   iiIi1IIi1I ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , IiI111111IIII , 10053 , 'https://addons.tvaddons.ag/' + O00 , ooOoOoo0O , '' )
   if 96 - 96: Ii1I - o0o00Oo0O
   if 35 - 35: O0OoO . oO0o0OOOO . iii1iiii1 - oO0o0OOOO % oO0o0OOOO + iii1iiii1
def Addon ( url ) :
 IIi1i11111 = O000OOo00oo ( url )
 oO0oO00 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIi1i11111 )
 i1I1i = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIi1i11111 )
 for url , O00 , Iii1IIII11I in i1I1i :
  if 'Please' in Iii1IIII11I :
   pass
  else :
   i1I1iI1iIi111i ( Iii1IIII11I , url , 10054 , 'https://addons.tvaddons.ag/' + O00 , ooOoOoo0O , '' )
 for url in oO0oO00 :
  iiIi1IIi1I ( '[COLOR' + iIii1 + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , i11i1I1 + 'Next.png' , ooOoOoo0O , '' )
  if 15 - 15: oOo0O0Ooo % IIIi . I1ii11iIi11i % iI11I1II1I1I
  if 98 - 98: oO0o0OOOO - ooOoO0O00 % O0O0OoOO0 - ii
def Iii1I1I ( url , name ) :
 IIi1i11111 = O000OOo00oo ( url )
 i1I1i = re . compile ( '<a href="([^"]*)"' ) . findall ( IIi1i11111 )
 for url in i1I1i :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   i1o0oooO = os . path . join ( oo00o0Oo , name + '.zip' )
   try :
    os . remove ( i1o0oooO )
   except :
    pass
   downloader . download ( url , i1o0oooO , o0oOoO00o )
   IiIIII = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print IiIIII
   print '======================================='
   extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
   Iii1 ( )
   if 41 - 41: oOo0O0Ooo . I1ii11iIi11i . ooo0oo0o0oo % ii + oO0o
def III1I11II11I ( url , name ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oo00o0Oo , name + '.zip' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 Iii1 ( )
 if 23 - 23: oOo0O0Ooo - I11i % IIIi . o0o00Oo0O * ii + OO0
def Iii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 53 - 53: I1ii11iIi11i
 if 3 - 3: ooo0oo0o0oo - ii * ii - oOo0O0Ooo / iii1iiii1 * Ii1I
def O0oo0ooO00 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , url , 1007 , ooo0OoOOOOO )
def oOoO0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , ooo0OoOOOOO )
  if 50 - 50: iii1iiii1 * iii1iiii1 * I1ii11iIi11i - oO0o
  if 12 - 12: I1ii11iIi11i + IIIIi1i / oO0o / I1ii11iIi11i
def O000oOOoOOO ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , iconimage , iII1iii , oO0o0 , name in i1I1i :
  if 'http' in url :
   if '.php' in url :
    Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
    for OOOo00 in Ii11Ii1iI :
     if OOOo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    O0o0O ( name , url , 1016 , iconimage , oO0o0 , iII1iii )
   else :
    if 'youtube' in url :
     Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
     for OOOo00 in Ii11Ii1iI :
      if OOOo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IIIIIIi1i ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oO0o0 , iII1iii )
    else :
     Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
     for OOOo00 in Ii11Ii1iI :
      if OOOo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IIIIIIi1i ( name , url , 222 , iconimage , oO0o0 , iII1iii )
     oOooOo0 ( 'movies' , 'INFO' )
  else :
   IiIiooooOOo ( url , iconimage , name )
   if 100 - 100: O0OoO % Ii - oOo0O0Ooo * iii1iiii1 - I11i
 else :
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
  for url , ooo0OoOOOOO , name in i1I1i :
   if 'http' in url :
    if '.php' in url :
     i11II1I11I1 ( name , url , 1016 , ooo0OoOOOOO )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OOoOO0ooo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0OoOOOOO )
     else :
      Ii11Ii1iI = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( i1I1iI ) )
      for OOOo00 in Ii11Ii1iI :
       if OOOo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOoOO0ooo ( name , url , 222 , ooo0OoOOOOO )
      oOooOo0 ( 'movies' , 'INFO' )
   else :
    IiIiooooOOo ( url , ooo0OoOOOOO , name )
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 65 - 65: Ii - ii / o0o00Oo0O * ooo0oo0o0oo % oO0o0OOOO
def IiIiooooOOo ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o00o00 = ( url ) . replace ( O000Oo00 , 'http' ) . replace ( Oo0iII , '.com' ) ;
 ooOo = ( o00o00 ) . replace ( iI1oOoo , 'a' ) . replace ( I1IiI11I1Ii11II , 'b' ) . replace ( oo0ooOoOOoO , 'c' ) . replace ( iii11i1 , 'd' ) . replace ( oOO00OoOo , 'e' ) . replace ( IIIo00O , 'f' ) ;
 o0oo00000O = ( ooOo ) . replace ( IiIIIi , 'g' ) . replace ( O0oooooO , 'h' ) . replace ( O0ooiIIi1 , 'i' ) . replace ( iI1i1iI1iI , 'j' ) . replace ( Oo0000o , 'k' ) . replace ( iI1IiiiIIiiII , 'l' ) ;
 oo0 = ( o0oo00000O ) . replace ( o0Oo00o0 , 'm' ) . replace ( i11II , 'n' ) . replace ( oOOoOo0Ooo , 'o' ) . replace ( o0OOoOoo00 , 'p' ) . replace ( Oo0Ooo0 , 'q' ) . replace ( IiIIiIi11ii , 'r' ) ;
 II11IiIIiiiii = ( oo0 ) . replace ( oooOOo0o0OOO , 's' ) . replace ( IIiI1I1IIiiI1 , 't' ) . replace ( IiiiII , 'u' ) . replace ( OoOo00OoOO00 , 'v' ) . replace ( oO0oOOoOo000O , 'w' ) . replace ( II1o0O0OO , 'x' ) ;
 oOoO0o = ( II11IiIIiiiii ) . replace ( i1IIOOOoooOo00O , 'y' ) . replace ( iiIIiI1I , 'z' ) . replace ( OOO0O00 , '.' ) . replace ( Oo0O000OoO00 , '(' ) . replace ( oOoooO0OO00 , ')' ) . replace ( IiiI , '/' ) ;
 oOoO0oOO0o = ( oOoO0o ) . replace ( iIo00oo , '1' ) . replace ( oooOOO0o0O0 , '2' ) . replace ( oO0000oo0o0o0 , '3' ) . replace ( II11II , '4' ) . replace ( i1ii11 , '5' ) . replace ( OoOo0O00 , '6' ) ;
 i1I1O0ooO0o = ( oOoO0oOO0o ) . replace ( ii1I1I1 , '7' ) . replace ( oo0oOOO0oOoo , '8' ) . replace ( Ii1o0OOOoo0000 , '9' ) . replace ( IiIIii1i1i11iII , '0' ) . replace ( iI1i1I11i , ':' ) . replace ( iiiIii1iIi1Ii , '%' ) ;
 url = ( i1I1O0ooO0o ) . replace ( iiI1 , '-' ) . replace ( IIi1 , '_' ) ;
 OOoOO0ooo ( name , url , 222 , iconimage ) ;
 if 42 - 42: ii - OOooOOo - O0OoO * iii1iiii1
 if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for IiI111111IIII , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 1007 , ooo0OoOOOOO )
def iIi11O00oO ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , ooo0OoOOOOO )
  if 80 - 80: ooo0oo0o0oo
def iiiI1I1iiiII ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 IIiIi1I1iI1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 IIiIi1I1iI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIiIi1I1iI1 )
 if 39 - 39: O0OoO
 if 70 - 70: ooo0oo0o0oo % oO0o % oOo0O0Ooo
def OOo00oOo ( url ) :
 o00o = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , O00 , Iii1IIII11I in i1I1i :
  if '-dir-' in Iii1IIII11I :
   i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , O00 )
  else :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' , url , 1006 , O00 )
   if 51 - 51: IIIIi1i
def oOI1ii11IiI1I ( url ) :
 o00o = IIIIiiIiiI ( url )
 Oo0Ii = ( 'http://afewbitsmore.com/' )
 i1I1i = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  if '[To Parent Directory]' in Iii1IIII11I :
   Iii1IIII11I = 'HOME'
   pass
  elif 'HOME' in Iii1IIII11I :
   pass
  elif '.m3u' in Iii1IIII11I :
   i11II1I11I1 ( '[COLOR' + iIii1 + ']PLAY ALL[/COLOR]' , Oo0Ii + url , 2002 , i11i1I1 + 'music.png' )
  elif '.mp3' in Iii1IIII11I :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Oo0Ii + url , 222 , i11i1I1 + 'music.png' )
  elif '.m4a' in Iii1IIII11I :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Oo0Ii + url , 222 , i11i1I1 + 'music.png' )
  else :
   i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) , Oo0Ii + url , 1012 , i11i1I1 + 'music.png' )
def oooooOOo0Oo ( url ) :
 IIi1i11111 = IIIIiiIiiI ( url )
 i1I1i = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIi1i11111 )
 for O00 , Iii1IIII11I , url in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , i11i1I1 + 'music.png' )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . OO0
def OoIII ( url ) :
 o00o = IIIIiiIiiI ( url )
 Oo0Ii = url
 i1I1i = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  if '.mp3' in Iii1IIII11I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , i11i1I1 + 'music.png' )
  else :
   i11II1I11I1 ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '/' , '' ) , Oo0Ii + url , 1011 , i11i1I1 + 'music.png' )
def OO00O ( ) :
 o00o = IIIIiiIiiI ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1I1i = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( o00o )
 for IiI111111IIII , O00 , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , ( 'http://www.cyn.net/music/' + IiI111111IIII ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + O00 ) . replace ( ' ' , '%20' ) )
def O0ooOOo00o0oO0O0 ( url , img ) :
 o00o = IIIIiiIiiI ( url )
 oo00o0 = url
 img = img
 i1I1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oo00o0 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 68 - 68: IIiIiII11i
def oOO0o0oOoO ( url ) :
 o00o = IIIIiiIiiI ( url )
 oo00o0 = url
 i1I1i = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for type , url , Iii1IIII11I in i1I1i :
  if '[VID]' in type :
   OOoOO0ooo ( ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oo00o0 + url , 222 , i11i1I1 + 'music.png' )
  if '[DIR]' in type :
   oOO0o0oOoO ( oo00o0 + url )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: IIIIi1i * OOooOOo * ooo0oo0o0oo
 if 46 - 46: O0O0OoOO0
def ii1o0 ( ) :
 oOII1i1i1I1iII = ( i1iiIII111ii ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIIiiI1i1 = oooOOOOO . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1I = IIIiiI1i1 . lower ( )
 IiI111111IIII = ( i1iiIII111ii ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oo00o0 = ( i1iiIII111ii ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 Ii1i1iI = ( i1iiIII111ii ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 67 - 67: ii - o0o00Oo0O
 IIi1i11111 = O0Oo000ooO00 ( IiI111111IIII )
 ooOO00O00oo = O0Oo000ooO00 ( oo00o0 )
 I1ii11iI = O0Oo000ooO00 ( Ii1i1iI )
 if 40 - 40: oOo0O0Ooo
 if IIi1i11111 != 'Failed' :
  i1I1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i11111 )
  for Iii1IIII11I in i1I1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiI111111IIII + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 3 - 3: OO0 / ooOoO0O00 - OOooOOo
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if ooOO00O00oo != 'Failed' :
  Iiiii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i11111 )
  for Iii1IIII11I in Iiiii1i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo00o0 + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 73 - 73: ii * o0o00Oo0O * OO0
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
 if I1ii11iI != 'Failed' :
  i111i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1ii11iI )
  for Iii1IIII11I in i111i :
   if IIIiiI1i1 in Iii1IIII11I . lower ( ) :
    i11II1I11I1 ( ( Iii1IIII11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ii1i1iI + Iii1IIII11I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 7 - 7: IIiIiII11i + ooOoO0O00
    oOooOo0 ( 'tvshows' , 'Media Info 3' )
    if 95 - 95: Ii + ii / O0OoO - iI11I1II1I1I + iI11I1II1I1I
    if 29 - 29: ooo0oo0o0oo % OO0 + oO0o . ooOoO0O00 + oOo0O0Ooo
    if 24 - 24: iii1iiii1 / O0O0OoOO0 * Ii1I - ii / oOo0O0Ooo . IIIi
    if 98 - 98: ooOoO0O00 - IIIIi1i
    if 49 - 49: I11i . O0O0OoOO0 . IIIi
    if 9 - 9: ooo0oo0o0oo - IIiIiII11i * oO0o
o0Oo00o0 = '{SF},' ; i11II = '{IF},' ; oOOoOo0Ooo = '{PW},' ; oO0000oo0o0o0 = '{AM},' ; o0OOoOoo00 = '{GF},' ; Oo0Ooo0 = '{DD},' ; IiIIiIi11ii = '{UO},' ; oooOOo0o0OOO = '{LE},' ; IiiiII = '{ZY},' ; OoOo00OoOO00 = '{UE},' ; oO0oOOoOo000O = '{PE},' ; II1o0O0OO = '{JE},' ; i1IIOOOoooOo00O = '{TH},' ; iiIIiI1I = '{LK},'
if 78 - 78: iI11I1II1I1I / o0o00Oo0O * IIIi / IIIIi1i / OOooOOo
if 15 - 15: OO0 / IIIi
def O0Oo00o0o ( ) :
 o00o = O000OOo00oo ( 'http://www.iwatchseries.me/tv-list/' )
 i1I1i = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 8021 , i11i1I1 + 'iwatch.png' )
def oooooO0oO0o ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( o00o )
 for url , Iii1IIII11I , i111iiI1ii in i1I1i :
  i11II1I11I1 ( Iii1IIII11I + i111iiI1ii , url , 8022 , i11i1I1 + 'iwatch.png' )
def O0ooo0Ooo ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00o )
 for url in i1I1i :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oOOo0OOOOo0o ( url )
def oOOo0OOOOo0o ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( o00o )
 Iiiii1i = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( o00o )
 i111i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( 'VidSpot - ' + Iii1IIII11I , url , 222 , i11i1I1 + 'iwatch.png' )
 for url in Iiiii1i :
  OOoOO0ooo ( 'VodLocker' , url , 222 , i11i1I1 + 'iwatch.png' )
 for Iii1IIII11I , url in i111i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OOoOO0ooo ( 'TheVideo - ' + Iii1IIII11I , url , 222 , i11i1I1 + 'iwatch.png' )
   if 29 - 29: ooo0oo0o0oo - oO0o0OOOO . o0o00Oo0O . o0o00Oo0O
def Ii11II1IIIIIi ( ) :
 o00o = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1I1i = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 1021 , i11i1I1 + 'anime.png' )
  if 83 - 83: iI11I1II1I1I + IIiIiII11i * IIIi / o0o00Oo0O - IIIIi1i
  if 23 - 23: ooOoO0O00
def iIi11i1I11Ii ( ) :
 o00o = O000OOo00oo ( 'http://www.animetoon.org/cartoon' )
 i1I1i = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o00o )
 for IiI111111IIII , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , IiI111111IIII , 1002 , i11i1I1 + 'anime.png' )
  if 59 - 59: Ii - oO0o0OOOO
  if 59 - 59: ii * I11i / iii1iiii1
  if 75 - 75: I11i - ii
def Iiiiii ( url ) :
 o00o = O000OOo00oo ( url )
 Iiiii1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o00o )
 for O00 in Iiiii1i :
  OoO = O00
 i111i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o00o )
 for url in i111i :
  i11II1I11I1 ( 'NEXT PAGE' , url , 1002 , i11i1I1 + 'Next.png' )
 i1I1i = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , Iii1IIII11I in i1I1i :
  i11II1I11I1 ( Iii1IIII11I , url , 1003 , OoO )
 xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoo000o ( url , IMAGE ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o00o )
 for Iii1IIII11I , url in i1I1i :
  print Iii1IIII11I + '     ' + url
  if 'easy' in url :
   O000OoOO0oO ( url )
  elif 'playpanda' in url :
   O000OoOO0oO ( url )
   if 31 - 31: oOo0O0Ooo / OOooOOo
  xbmcplugin . addSortMethod ( OOOO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O000OoOO0oO ( url ) :
 o00o = O000OOo00oo ( url )
 i1I1i = re . compile ( "url: '(.+?)'," ) . findall ( o00o )
 for url in i1I1i :
  OOoOO0ooo ( 'STREAM' , url , 222 , i11i1I1 + 'anime.png' )
  if 72 - 72: I1ii11iIi11i + iii1iiii1 % Ii1I + O0OoO % iii1iiii1
  if 8 - 8: Ii
def iii1iII11IiI ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oO0 . add_header ( 'referer' , url )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 30 - 30: iI11I1II1I1I
def IIIIiiIiiI ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 15 - 15: OO0 * iI11I1II1I1I * IIIi
def O0oo0O00ooOo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1i = ( '%s%s' % ( iiiI1IiIIii , url ) )
 ooOooo000oOO = IIIIiiIiiI ( url )
 i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooOooo000oOO )
 for url , ooo0OoOOOOO , Iii1IIII11I in i1I1i :
  OOoOO0ooo ( '%s' % ( '[COLOR' + iIii1 + ']' + Iii1IIII11I + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooo0OoOOOOO )
  if 70 - 70: I1ii11iIi11i + Ii
def iIIIII1ii1I ( url ) :
 if 44 - 44: Ii / O0OoO * OO0
 Ooo00o000o = open ( IIIii1II1II , "a" )
 Ooo00o000o . write ( 'url="' + url + '"\n' )
 Ooo00o000o . close
 if 57 - 57: oO0o0OOOO - oO0o0OOOO % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 import urlresolver
 try : O0 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Iii1IIII11I ) )
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O0 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - O0O0OoOO0 * iI11I1II1I1I
def OO0ooo0OOO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Iii1IIII11I )
 xbmc . sleep ( 1 )
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 o0oOoO00o . update ( 100 , '%s' % Iii1IIII11I )
 xbmc . sleep ( 1 )
 O0 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 69 - 69: iii1iiii1 + iI11I1II1I1I * IIIi + ooo0oo0o0oo % OO0 - O0O0OoOO0
def o0Ooo0O0 ( url ) :
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0 . play ( url ) . strip ( )
 except : pass
 if 83 - 83: ooo0oo0o0oo % I11i * I11i
def o0000Oo0 ( url ) :
 O0 = xbmc . Player ( OOO00ii1Ii111I11I ( ) )
 import urlresolver
 I1iII1iI = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 O0 . play ( I1iII1iI )
 xbmc . sleep ( 1 )
 O0 . play ( url )
 if 46 - 46: ii * O0O0OoOO0 . iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 * oO0o
 if 83 - 83: IIIIi1i . Ii . ii . O0O0OoOO0
def OOO00ii1Ii111I11I ( ) :
 try :
  iIII1iIiIIIIi = getSet ( "core-player" )
  if ( iIII1iIiIIIIi == 'DVDPLAYER' ) : ii11I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIII1iIiIIIIi == 'MPLAYER' ) : ii11I = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIII1iIiIIIIi == 'PAPLAYER' ) : ii11I = xbmc . PLAYER_CORE_PAPLAYER
  else : ii11I = xbmc . PLAYER_CORE_AUTO
 except : ii11I = xbmc . PLAYER_CORE_AUTO
 return ii11I
 return True
 if 54 - 54: O0OoO
def i11II1I11I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOooO0OOo000O = [ ]
  if showcontext == 'fav' :
   oOooO0OOo000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oOooO0OOo000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O00oO0o000oO . addContextMenuItems ( oOooO0OOo000O )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = True )
 return iI1
 if 75 - 75: Ii * oOo0O0Ooo
def OOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 78 - 78: oO0o / iI11I1II1I1I . O0O0OoOO0 * oO0o * OOooOOo - O0OoO
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = True )
 return iI1
 if 39 - 39: Ii - O0OoO - iii1iiii1 + ii / oOo0O0Ooo / iI11I1II1I1I
def OOoOO0ooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oOooO0OOo000O = [ ]
  if showcontext == 'fav' :
   oOooO0OOo000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oOooO0OOo000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O00oO0o000oO . addContextMenuItems ( oOooO0OOo000O )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = False )
 return iI1
 if 16 - 16: OOooOOo / O0O0OoOO0 . iii1iiii1 % Ii % oOo0O0Ooo / O0OoO
 if 85 - 85: oO0o0OOOO + iii1iiii1
 if 11 - 11: oO0o0OOOO
 if 95 - 95: I1ii11iIi11i + Ii % O0OoO - IIIi
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: iii1iiii1 + ooo0oo0o0oo * iI11I1II1I1I
def ii1I ( heading , announce ) :
 class II1Iii1iI ( ) :
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
   try : Iii1I1I11iiI1 = open ( announce ) ; I1IIiI = Iii1I1I11iiI1 . read ( )
   except : I1IIiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1IIiI ) )
   return
 II1Iii1iI ( )
 II1Iii1iI ( )
 if 56 - 56: iI11I1II1I1I . oO0o0OOOO
def iiIIi1i111i ( ) :
 ii1I ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 48 - 48: I1ii11iIi11i . I11i - IIIIi1i
 if 15 - 15: I11i
 if 87 - 87: I11i
 if 99 - 99: O0O0OoOO0 / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % iii1iiii1 % IIIi + oO0o0OOOO * IIIi . O0O0OoOO0
def Iii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
 if 56 - 56: Ii1I . ooOoO0O00 / IIIIi1i % IIIi / o0o00Oo0O * oO0o0OOOO
 if 98 - 98: o0o00Oo0O + IIIIi1i
 if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / oO0o0OOOO . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - ooo0oo0o0oo
 if 50 - 50: oOo0O0Ooo - IIIi + IIIi * oO0o0OOOO + IIIi
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
def oO0OOOO00o ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + i1Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 60 - 60: OO0 * O0O0OoOO0 + iii1iiii1 . O0OoO . o0o00Oo0O
def Ii1i1ii ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + ooOOoO00o0o0oo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 13 - 13: oO0o0OOOO % iii1iiii1 . ooOoO0O00
def IIiIiiiii11 ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + oooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 65 - 65: I1ii11iIi11i . OOooOOo . O0OoO % I11i + oO0o
def OOO000OOOO0oO ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iIIIiiiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 15 - 15: oO0o0OOOO % oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
def oo000o ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iIIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + Oo00OOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 27 - 27: iii1iiii1
def iii1iI ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + IIio0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 27 - 27: OOooOOo . iii1iiii1 * OOooOOo
def iI111iI11iII ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + O000o0Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 31 - 31: o0o00Oo0O * IIIIi1i - IIIIi1i / IIIIi1i - OO0 / OOooOOo
def iI1IiiiI ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + o0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 42 , i1i1IIIIi1i , oO0o0 , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 48 - 48: iii1iiii1
def iI1II1iIiiiI ( url ) :
 ooOooo000oOO = O000OOo00oo ( str ( I1I1iIiII1 ) + iiIIi11I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1i = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( ooOooo000oOO )
 for Iii1IIII11I , url , i1i1IIIIi1i , oO0o0 , I1iii11 in i1I1i :
  iiIi1IIi1I ( Iii1IIII11I , url , 5 , i11i1I1 + 'GenieTVRSSFeed.png' , i11i1I1 + 'GenieTVRSSFeed.png' , I1iii11 )
 oOooOo0 ( 'movies' , 'MAIN' )
 if 14 - 14: O0OoO + I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . OO0
 if 62 - 62: ii / OO0 + Ii1I . I11i - IIIIi1i
 if 29 - 29: IIIi
 if 26 - 26: o0o00Oo0O % O0OoO - ooo0oo0o0oo . O0OoO
 if 70 - 70: I11i + oO0o0OOOO / IIIIi1i + OO0 / oOo0O0Ooo
 if 33 - 33: ii . o0o00Oo0O
 if 59 - 59: iI11I1II1I1I
 if 45 - 45: o0o00Oo0O
 if 78 - 78: oO0o0OOOO - iI11I1II1I1I + iii1iiii1 - Ii1I - iii1iiii1
def iii1 ( ) :
 try :
  if os . path . exists ( O0o0Oo ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( O0o0Oo ) :
     iII1iiio0O0o = 0
     iII1iiio0O0o += len ( iII1I1 )
     if iII1iiio0O0o > 0 :
      for Iii1I1I11iiI1 in iII1I1 :
       os . unlink ( os . path . join ( OoIiIiIi1I1 , Iii1I1I11iiI1 ) )
  OO0o0o = os . path . join ( OO0o , "Textures13.db" )
  os . unlink ( OO0o0o )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 61 - 61: oO0o0OOOO * O0O0OoOO0 + oO0o0OOOO - I1ii11iIi11i % OOooOOo . IIIIi1i
 if 51 - 51: O0OoO / oO0o0OOOO
 if 51 - 51: OO0 * IIIi - iii1iiii1 + IIIIi1i
 if 46 - 46: I11i - Ii % oO0o / O0O0OoOO0 - OOooOOo
 if 88 - 88: IIIi * oOo0O0Ooo / oO0o - O0OoO / ooOoO0O00 . iii1iiii1
 if 26 - 26: Ii - OO0
 if 45 - 45: OO0 + IIiIiII11i % IIIIi1i
 if 55 - 55: OO0 - IIIi % oOo0O0Ooo
def ooOooo0OoOo0o ( title , message , times = 2000 , icon = OooO0 ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 65 - 65: iI11I1II1I1I . IIiIiII11i % O0OoO - iii1iiii1 + ii / o0o00Oo0O
def OOoO00 ( url ) :
 oOo000oo = os . path . join ( oo0o0O00 , 'addon_data' )
 O0oOo00Oo0oo0 = [
 ( oOo000oo ) ,
 ( Oo0o0000o0o0 ) ,
 ( os . path . join ( i11 , 'cache' ) ) ,
 ( os . path . join ( i11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOo000oo , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo000oo , 'plugin.video.itv' , 'Images' ) ) ]
 if 36 - 36: iii1iiii1 / iii1iiii1 % IIIi
 OoOO0o00OOO0o = 0
 if 52 - 52: ii / O0O0OoOO0 - o0o00Oo0O % ooOoO0O00 * O0OoO
 for OOOo00 in O0oOo00Oo0oo0 :
  if os . path . exists ( OOOo00 ) and not OOOo00 in [ Oo0o0000o0o0 , oOo000oo ] :
   for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( OOOo00 ) :
    iII1iiio0O0o = 0
    iII1iiio0O0o += len ( iII1I1 )
    if iII1iiio0O0o > 0 :
     for Iii1I1I11iiI1 in iII1I1 :
      if not Iii1I1I11iiI1 in oO :
       try :
        os . unlink ( os . path . join ( OoIiIiIi1I1 , Iii1I1I11iiI1 ) )
       except :
        pass
      else : I1IiiiiI ( 'Ignore Log File: %s' % Iii1I1I11iiI1 )
     for oo0o0000Oo0 in ooO00O0O0 :
      try :
       shutil . rmtree ( os . path . join ( OoIiIiIi1I1 , oo0o0000Oo0 ) )
       OoOO0o00OOO0o += 1
       I1IiiiiI ( "[Success] cleared %s files from %s" % ( str ( iII1iiio0O0o ) , os . path . join ( OOOo00 , oo0o0000Oo0 ) ) )
      except :
       I1IiiiiI ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOo00 , oo0o0000Oo0 ) )
  else :
   for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( OOOo00 ) :
    for oo0o0000Oo0 in ooO00O0O0 :
     if 'cache' in oo0o0000Oo0 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OoIiIiIi1I1 , oo0o0000Oo0 ) )
       OoOO0o00OOO0o += 1
       I1IiiiiI ( "[Success] wiped %s " % os . path . join ( OOOo00 , oo0o0000Oo0 ) )
      except :
       I1IiiiiI ( "[Failed] to wipe cache in: %s" % os . path . join ( OOOo00 , oo0o0000Oo0 ) )
       if 92 - 92: I1ii11iIi11i % ii - Ii
 ooOooo0OoOo0o ( oO0o0o0ooO0oO , 'Clear Cache: Removed %s Files' % OoOO0o00OOO0o )
 if 46 - 46: I1ii11iIi11i
 if 99 - 99: oO0o - OO0 * o0o00Oo0O * Ii1I * iI11I1II1I1I - iI11I1II1I1I
 if 50 - 50: oOo0O0Ooo % Ii - oOo0O0Ooo * IIIIi1i / ooo0oo0o0oo / o0o00Oo0O
 if 31 - 31: IIiIiII11i . ii + oO0o + I11i . oOo0O0Ooo . IIiIiII11i
 if 3 - 3: oO0o0OOOO / iii1iiii1 * ooo0oo0o0oo - o0o00Oo0O + oOo0O0Ooo / ooo0oo0o0oo
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: ooo0oo0o0oo - I11i % O0OoO - IIiIiII11i
def o0o0OOooo0Oo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iIiII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( iIiII1 ) :
   iII1iiio0O0o = 0
   iII1iiio0O0o += len ( iII1I1 )
   if 9 - 9: Ii1I - ooo0oo0o0oo
   if 64 - 64: ooOoO0O00
   if iII1iiio0O0o > 0 :
    if 71 - 71: ooo0oo0o0oo * I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( iII1iiio0O0o ) + " files found" , "Do you want to delete them?" ) :
     if 99 - 99: I11i
     for Iii1I1I11iiI1 in iII1I1 :
      os . unlink ( os . path . join ( OoIiIiIi1I1 , Iii1I1I11iiI1 ) )
     for oo0o0000Oo0 in ooO00O0O0 :
      shutil . rmtree ( os . path . join ( OoIiIiIi1I1 , oo0o0000Oo0 ) )
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
 if 28 - 28: ii % o0o00Oo0O - O0OoO / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * ooo0oo0o0oo / oO0o . IIIi
 if 50 - 50: ii + iI11I1II1I1I / IIIi / O0OoO . Ii . OO0
 if 75 - 75: iI11I1II1I1I % OO0 / O0OoO - IIIIi1i % Ii
 if 11 - 11: oO0o0OOOO . O0O0OoOO0
 if 87 - 87: O0OoO + O0OoO
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / O0O0OoOO0 . oO0o0OOOO * I11i
 if 21 - 21: IIiIiII11i
def Ii1II11II1iii ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iIiII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( iIiII1 ) :
   iII1iiio0O0o = 0
   iII1iiio0O0o += len ( iII1I1 )
   if 29 - 29: OOooOOo % O0O0OoOO0
   if 7 - 7: ooOoO0O00 / ooo0oo0o0oo / IIIIi1i
   if iII1iiio0O0o > 0 :
    if 97 - 97: oO0o + iI11I1II1I1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( iII1iiio0O0o ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: OO0 + IIIi - IIiIiII11i . I1ii11iIi11i
     for Iii1I1I11iiI1 in iII1I1 :
      os . unlink ( os . path . join ( OoIiIiIi1I1 , Iii1I1I11iiI1 ) )
     for oo0o0000Oo0 in ooO00O0O0 :
      shutil . rmtree ( os . path . join ( OoIiIiIi1I1 , oo0o0000Oo0 ) )
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
 if 26 - 26: ooo0oo0o0oo
 if 52 - 52: o0o00Oo0O + OO0
 if 11 - 11: ooOoO0O00 / iii1iiii1 * Ii1I * iii1iiii1 * OO0 - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . O0O0OoOO0
 if 26 - 26: IIIi - OO0 % I1ii11iIi11i - IIIi + ooo0oo0o0oo
 if 33 - 33: O0O0OoOO0 + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * ooo0oo0o0oo
 if 21 - 21: o0o00Oo0O * OO0 % oO0o
 if 14 - 14: o0o00Oo0O / iii1iiii1 / OO0 + ooo0oo0o0oo - ooo0oo0o0oo
 if 10 - 10: o0o00Oo0O - Ii1I / iii1iiii1 % OOooOOo / ii / O0O0OoOO0
def O000oOo ( url , name ) :
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00Oo00O0o = os . path . join ( oo00o0Oo , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 ooooOOo = os . path . join ( oo00o0Oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( ooooOOo ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o00Oo00O0o = os . path . join ( oo00o0Oo , 'advancedsettings.xml' )
   try :
    os . remove ( o00Oo00O0o )
    print '=== GenieTv - REMOVING    ' + str ( o00Oo00O0o ) + '    ==='
   except :
    pass
   ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
   O0oooo00o0Oo = open ( o00Oo00O0o , "w" )
   O0oooo00o0Oo . write ( ooOooo000oOO )
   O0oooo00o0Oo . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o00Oo00O0o ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o00Oo00O0o = os . path . join ( oo00o0Oo , 'advancedsettings.xml' )
  try :
   os . remove ( o00Oo00O0o )
   print '=== GenieTv - REMOVING    ' + str ( o00Oo00O0o ) + '    ==='
  except :
   pass
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  O0oooo00o0Oo = open ( o00Oo00O0o , "w" )
  O0oooo00o0Oo . write ( ooOooo000oOO )
  O0oooo00o0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00Oo00O0o ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 73 - 73: O0O0OoOO0 + IIIIi1i % O0OoO + ii * I1ii11iIi11i
def i1Ii ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00Oo00O0o = os . path . join ( oo00o0Oo , 'advancedsettings.xml' )
 try :
  O0oooo00o0Oo = open ( o00Oo00O0o ) . read ( )
  if 'zero' in O0oooo00o0Oo :
   name = '0CACHE'
  elif 'tuxen' in O0oooo00o0Oo :
   name = 'TUXENS'
  elif 'muckys' in O0oooo00o0Oo :
   name = 'MUCKYS'
  elif 'p2p1' in O0oooo00o0Oo :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in O0oooo00o0Oo :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in O0oooo00o0Oo :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 16 - 16: oO0o
def I11OO0OoO0OOoOo ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o00Oo00O0o = os . path . join ( oo00o0Oo , 'advancedsettings.xml' )
 try :
  os . remove ( o00Oo00O0o )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o00Oo00O0o ) + '    ==='
  oooOOOOO . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 84 - 84: IIIi / O0O0OoOO0 * IIIIi1i
 if 20 - 20: OOooOOo % o0o00Oo0O
 if 59 - 59: o0o00Oo0O . I11i % Ii1I * IIIi + oO0o0OOOO
 if 82 - 82: ii
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if 27 - 27: Ii % IIIIi1i + O0O0OoOO0 . O0OoO
 if 9 - 9: oO0o
 if 43 - 43: O0O0OoOO0 . O0OoO + oOo0O0Ooo * Ii
 if 2 - 2: O0OoO
 if 3 - 3: oOo0O0Ooo . IIIIi1i % o0o00Oo0O - OO0 / o0o00Oo0O
def O00O00 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1I1i = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1iiIIiiI111 . http_GET ( url ) . content )
 for IIiiiIi1IiI , ooOoOoOoOoo , iIIIIIiiiII , Oo0Ooo in i1I1i :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IIiiiIi1IiI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iIIIIIiiiII , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % Oo0Ooo )
  inc = inc + 1
  if 42 - 42: IIIi - Ii % IIIi - iii1iiii1 * o0o00Oo0O / IIiIiII11i
  if 5 - 5: I1ii11iIi11i
  if 84 - 84: Ii1I
  if 53 - 53: IIIi
  if 26 - 26: iii1iiii1 / iii1iiii1 + I1ii11iIi11i - I11i % IIiIiII11i . ii
  if 7 - 7: IIiIiII11i - Ii1I / oO0o0OOOO % ii + ooOoO0O00
  if 42 - 42: oO0o0OOOO + ooOoO0O00 - O0O0OoOO0 / ooo0oo0o0oo . IIIIi1i
  if 30 - 30: I1ii11iIi11i + O0O0OoOO0 % Ii * ooOoO0O00 + oOo0O0Ooo % O0OoO
  if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % iii1iiii1
def OOOo0o ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o00Oo00O0o = os . path . join ( oo00o0Oo , 'addons2.ini' )
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  O0oooo00o0Oo = open ( o00Oo00O0o , "w" )
  O0oooo00o0Oo . write ( ooOooo000oOO )
  O0oooo00o0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00Oo00O0o ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 98 - 98: o0o00Oo0O % Ii % O0OoO
def I1i1Ii1Ii ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oo00o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o00Oo00O0o = os . path . join ( oo00o0Oo , 'settings.xml' )
  ooOooo000oOO = i1iiIIiiI111 . http_GET ( url ) . content
  O0oooo00o0Oo = open ( o00Oo00O0o , "w" )
  O0oooo00o0Oo . write ( ooOooo000oOO )
  O0oooo00o0Oo . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o00Oo00O0o ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 15 - 15: o0o00Oo0O
 if 60 - 60: O0O0OoOO0 % IIIi - Ii1I / IIIi
def iii111 ( ) :
 try :
  OO0oOOOOO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO0oOOOOO ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OoOooO0 = os . path . join ( OO0oOOOOO , "source.db" )
    os . unlink ( OoOooO0 )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 25 - 25: oO0o0OOOO + IIiIiII11i / OO0
 if 12 - 12: Ii + ooOoO0O00 - O0O0OoOO0 + o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: O0O0OoOO0 - ii + iii1iiii1 % I11i - OOooOOo . oOo0O0Ooo
def O000OOo00oo ( url ) :
 oO0 = urllib2 . Request ( url )
 oO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Ii1iIiII1ii1 = urllib2 . urlopen ( oO0 )
 ooOooo000oOO = Ii1iIiII1ii1 . read ( )
 Ii1iIiII1ii1 . close ( )
 return ooOooo000oOO
 if 42 - 42: iii1iiii1
 if 70 - 70: I11i / oO0o0OOOO + IIIi % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: O0OoO
 if 12 - 12: O0O0OoOO0
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
def I1IiII ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; o0O00o0o = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if o0O00o0o :
  I11Ii111IIi = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; I11Ii111IIi = xbmc . translatePath ( I11Ii111IIi ) ;
  OoOoO0OooO00Oo = os . path . join ( I11Ii111IIi , ".." , ".." ) ; OoOoO0OooO00Oo = os . path . abspath ( OoOoO0OooO00Oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OoOoO0OooO00Oo ) ; oO0OO00O0 = False
  try :
   for OoIiIiIi1I1 , ooO00O0O0 , iII1I1 in os . walk ( OoOoO0OooO00Oo , topdown = True ) :
    ooO00O0O0 [ : ] = [ oo0o0000Oo0 for oo0o0000Oo0 in ooO00O0O0 if oo0o0000Oo0 not in o0oO0 ]
    for Iii1IIII11I in iII1I1 :
     try : os . remove ( os . path . join ( OoIiIiIi1I1 , Iii1IIII11I ) )
     except :
      if Iii1IIII11I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oO0OO00O0 = True
      plugintools . log ( "Error removing " + OoIiIiIi1I1 + " " + Iii1IIII11I )
    for Iii1IIII11I in ooO00O0O0 :
     try : os . rmdir ( os . path . join ( OoIiIiIi1I1 , Iii1IIII11I ) )
     except :
      if Iii1IIII11I not in [ "Database" , "userdata" ] : oO0OO00O0 = True
      plugintools . log ( "Error removing " + OoIiIiIi1I1 + " " + Iii1IIII11I )
   if not oO0OO00O0 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0oOO0ooOoO ( )
 if 65 - 65: O0OoO % ooo0oo0o0oo % I11i . O0O0OoOO0 . Ii1I
 if 64 - 64: Ii1I . O0O0OoOO0 / Ii1I * O0O0OoOO0
 if 86 - 86: iI11I1II1I1I * IIIIi1i * O0O0OoOO0 / oO0o % OO0 - o0o00Oo0O
def ooOOO0Oo ( ) :
 IiIiI1I1IIIi1 = [ ]
 iII11I = sys . argv [ 2 ]
 if len ( iII11I ) >= 2 :
  i1I1IiIiIII = sys . argv [ 2 ]
  OO0oO0oO0o00OoO = i1I1IiIiIII . replace ( '?' , '' )
  if ( i1I1IiIiIII [ len ( i1I1IiIiIII ) - 1 ] == '/' ) :
   i1I1IiIiIII = i1I1IiIiIII [ 0 : len ( i1I1IiIiIII ) - 2 ]
  O000o = OO0oO0oO0o00OoO . split ( '&' )
  IiIiI1I1IIIi1 = { }
  for OOO0O00Oo in range ( len ( O000o ) ) :
   oOO0O0o0Oo = { }
   oOO0O0o0Oo = O000o [ OOO0O00Oo ] . split ( '=' )
   if ( len ( oOO0O0o0Oo ) ) == 2 :
    IiIiI1I1IIIi1 [ oOO0O0o0Oo [ 0 ] ] = oOO0O0o0Oo [ 1 ]
    if 9 - 9: IIIIi1i - IIIIi1i
 return IiIiI1I1IIIi1
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + IIIi
IIi1iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iII1Iii1I11i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii1Ii = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
IIIIi11111 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
ooO000O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo0o00o0oOoo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
i1Ii1I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1II = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ooOOoO00o0o0oo0o = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oooo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIIIiiiII = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iIIIII = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Oo00OOO0 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IIio0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O000o0Oo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0O0o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iI111I11i = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o000 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
II1i111 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
i1I1IIIiiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1II1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo0OoOooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iiIIi11I1ii = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iiiI1IiIIii = base64 . decodestring ( 'Q1VOVA==' )
def iiIi1IIi1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oOooO0OOo000O = [ ]
  if showcontext == 'fav' :
   oOooO0OOo000O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in o00OO00OoO :
   oOooO0OOo000O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O00oO0o000oO . addContextMenuItems ( oOooO0OOo000O )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = True )
 return iI1
 if 8 - 8: I1ii11iIi11i
def i1I1iI1iIi111i ( name , url , mode , iconimage , fanart , description ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 O00oO0o000oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO0o000oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O00oO0o000oO . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = O00oO0o000oO , isFolder = False )
 return iI1
 if 22 - 22: OO0 % OOooOOo / I11i
 if 98 - 98: oO0o / I11i * oOo0O0Ooo
i1I1IiIiIII = ooOOO0Oo ( )
IiI111111IIII = None
Iii1IIII11I = None
OoiI1I1 = None
i1i1IIIIi1i = None
oO0o0 = None
I1iii11 = None
OOo0iIiiI11II11 = None
if 75 - 75: iii1iiii1 - IIIIi1i . IIIi
if 88 - 88: IIIIi1i - ii . OO0 - I11i / OOooOOo % oO0o0OOOO
try :
 OOo0iIiiI11II11 = int ( i1I1IiIiIII [ "fav_mode" ] )
except :
 pass
 if 61 - 61: IIIIi1i + ooo0oo0o0oo
try :
 IiI111111IIII = urllib . unquote_plus ( i1I1IiIiIII [ "url" ] )
except :
 pass
try :
 Iii1IIII11I = urllib . unquote_plus ( i1I1IiIiIII [ "name" ] )
except :
 pass
try :
 i1i1IIIIi1i = urllib . unquote_plus ( i1I1IiIiIII [ "iconimage" ] )
except :
 pass
try :
 OoiI1I1 = int ( i1I1IiIiIII [ "mode" ] )
except :
 pass
try :
 oO0o0 = urllib . unquote_plus ( i1I1IiIiIII [ "fanart" ] )
except :
 pass
try :
 I1iii11 = urllib . unquote_plus ( i1I1IiIiIII [ "description" ] )
except :
 pass
 if 54 - 54: ii * oOo0O0Ooo % ooOoO0O00 . OO0 % O0O0OoOO0 . Ii1I
 if 72 - 72: OO0 % oO0o0OOOO + oO0o
print str ( Oo00OOOOO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OoiI1I1 )
print "URL: " + str ( IiI111111IIII )
print "Name: " + str ( Iii1IIII11I )
print "IconImage: " + str ( i1i1IIIIi1i )
if 94 - 94: O0O0OoOO0 + iI11I1II1I1I
if 80 - 80: I11i . IIIIi1i . ii
def oOooOo0 ( content , viewType ) :
 if 63 - 63: OO0 . O0OoO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 66 - 66: oOo0O0Ooo
if i1i1IIIIi1i == None : i1i1IIIIi1i = OooO0
if oO0o0 == None : oO0o0 = ooOoOoo0O
if OoiI1I1 == None :
 oOooOOOoOo ( )
 if 99 - 99: oO0o % o0o00Oo0O . iii1iiii1 - Ii1I . I1ii11iIi11i / OOooOOo
elif OoiI1I1 == 1 :
 OoOO ( IiI111111IIII )
 if 60 - 60: Ii1I
elif OoiI1I1 == 44 :
 I1I1 ( IiI111111IIII )
 if 78 - 78: IIIi + IIiIiII11i
elif OoiI1I1 == 2 :
 IiiIi ( )
 if 55 - 55: ii
elif OoiI1I1 == 3 :
 ooOoO ( )
 if 90 - 90: oOo0O0Ooo
elif OoiI1I1 == 21 :
 i1i1II ( )
 if 4 - 4: O0OoO % OO0 - O0OoO - I11i
elif OoiI1I1 == 4 :
 OOoOOo0O00O ( )
 if 30 - 30: ooo0oo0o0oo
elif OoiI1I1 == 5 :
 oo0ooO0 ( IiI111111IIII )
 if 34 - 34: IIIi - IIiIiII11i - I11i + IIIIi1i + iii1iiii1
elif OoiI1I1 == 6 :
 o0o0OOooo0Oo ( IiI111111IIII )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif OoiI1I1 == 7 :
 O000oOo ( IiI111111IIII , Iii1IIII11I )
 if 20 - 20: Ii - IIiIiII11i - OO0 % IIIi . OO0
elif OoiI1I1 == 8 :
 i1Ii ( IiI111111IIII , Iii1IIII11I )
 if 50 - 50: iI11I1II1I1I + iii1iiii1 - oO0o0OOOO - ii
elif OoiI1I1 == 9 :
 FIXREPOSADDONS ( IiI111111IIII )
 if 84 - 84: OOooOOo - oO0o0OOOO
elif OoiI1I1 == 10 :
 Iii1 ( )
 if 80 - 80: Ii % O0OoO - I1ii11iIi11i % O0OoO
elif OoiI1I1 == 11 :
 I11OO0OoO0OOoOo ( IiI111111IIII )
 if 89 - 89: O0O0OoOO0 * oO0o0OOOO + OOooOOo / Ii
elif OoiI1I1 == 12 :
 O00O00 ( )
 if 68 - 68: ii * oO0o0OOOO
elif OoiI1I1 == 13 :
 iii1 ( )
 if 86 - 86: I11i / OOooOOo
elif OoiI1I1 == 14 :
 OOoO00 ( IiI111111IIII )
 if 40 - 40: IIIIi1i
elif OoiI1I1 == 15 :
 O0OO0OIiiiIiiI ( )
 if 62 - 62: OO0 / O0OoO
elif OoiI1I1 == 16 :
 OOOo0o ( IiI111111IIII , Iii1IIII11I )
 if 74 - 74: IIIIi1i % iii1iiii1 / iii1iiii1 - iI11I1II1I1I - IIiIiII11i + O0OoO
elif OoiI1I1 == 17 :
 I1i1Ii1Ii ( IiI111111IIII , Iii1IIII11I )
 if 92 - 92: oO0o0OOOO % iii1iiii1
elif OoiI1I1 == 18 :
 iii111 ( )
 if 18 - 18: OO0 + iii1iiii1 / O0OoO / IIIi + iI11I1II1I1I % ooo0oo0o0oo
elif OoiI1I1 == 19 :
 o0OO ( IiI111111IIII )
 if 94 - 94: oO0o0OOOO
elif OoiI1I1 == 40 :
 IIiIiiiIIIIi1 ( Iii1IIII11I , IiI111111IIII , I1iii11 )
 if 37 - 37: IIIi
elif OoiI1I1 == 42 :
 OOoO ( Iii1IIII11I , IiI111111IIII , I1iii11 )
 if 52 - 52: Ii1I * oOo0O0Ooo . O0OoO + ooOoO0O00 % IIIi / iI11I1II1I1I
elif OoiI1I1 == 43 :
 oOoooO00O ( IiI111111IIII )
 if 68 - 68: iii1iiii1 - OOooOOo . Ii + I11i
elif OoiI1I1 == 20 :
 OooOOo0 ( IiI111111IIII )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif OoiI1I1 == 22 :
 oO0OOOO00o ( IiI111111IIII )
 if 33 - 33: oO0o0OOOO . I1ii11iIi11i
elif OoiI1I1 == 23 :
 Ii1i1ii ( IiI111111IIII )
 if 89 - 89: IIIIi1i + ooOoO0O00 - ooo0oo0o0oo + OO0 . IIiIiII11i
elif OoiI1I1 == 24 :
 IIiIiiiii11 ( IiI111111IIII )
 if 85 - 85: iI11I1II1I1I - O0O0OoOO0 * I1ii11iIi11i . IIIi + iii1iiii1
elif OoiI1I1 == 25 :
 OOO000OOOO0oO ( IiI111111IIII )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif OoiI1I1 == 26 :
 oo000o ( IiI111111IIII )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IIIIi1i / IIIIi1i
elif OoiI1I1 == 27 :
 IIoooOoOO0o ( IiI111111IIII )
 if 43 - 43: oOo0O0Ooo
elif OoiI1I1 == 28 :
 iii1iI ( IiI111111IIII )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif OoiI1I1 == 29 :
 iI111iI11iII ( IiI111111IIII )
 if 34 - 34: I11i % Ii1I + O0O0OoOO0 * oO0o0OOOO / IIIi
elif OoiI1I1 == 30 :
 iii11II1I ( IiI111111IIII )
 if 18 - 18: OO0
elif OoiI1I1 == 31 :
 iI1IiiiI ( IiI111111IIII )
 if 92 - 92: oO0o % iI11I1II1I1I / ooo0oo0o0oo * IIIIi1i . ooOoO0O00 + IIIi
elif OoiI1I1 == 32 :
 i1II ( )
 if 24 - 24: ooo0oo0o0oo . IIIIi1i * ooo0oo0o0oo % Ii . Ii + ooOoO0O00
elif OoiI1I1 == 33 :
 I11iiIi1i1 ( )
 if 64 - 64: iI11I1II1I1I / ooo0oo0o0oo / I1ii11iIi11i - Ii1I
elif OoiI1I1 == 35 :
 I1i ( IiI111111IIII )
 if 100 - 100: ooo0oo0o0oo + ooOoO0O00 * oO0o
elif OoiI1I1 == 34 :
 Ii11 ( IiI111111IIII )
 if 64 - 64: IIIi * Ii . I1ii11iIi11i
elif OoiI1I1 == 36 :
 i1iIiIi1I ( IiI111111IIII )
 if 52 - 52: I1ii11iIi11i / OO0 / IIIIi1i - I11i / IIIIi1i
elif OoiI1I1 == 37 :
 Oo0ooo0Ooo ( IiI111111IIII )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif OoiI1I1 == 38 :
 iii1IIII1iii11I ( IiI111111IIII )
 if 85 - 85: oOo0O0Ooo
elif OoiI1I1 == 41 :
 I1IiII ( i1I1IiIiIII )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif OoiI1I1 == 39 :
 iI1II1iIiiiI ( IiI111111IIII )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif OoiI1I1 == 45 :
 TEXTS ( )
 if 46 - 46: OOooOOo * oO0o0OOOO / IIIi + I1ii11iIi11i + ooo0oo0o0oo
elif OoiI1I1 == 46 :
 iiIIi1i111i ( )
 if 95 - 95: I11i - O0O0OoOO0
elif OoiI1I1 == 47 :
 GEVID ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif OoiI1I1 == 48 :
 OooO00oOOo0Oo ( Iii1IIII11I , IiI111111IIII , I1iii11 )
 if 19 - 19: OOooOOo . O0OoO . ii
elif OoiI1I1 == 49 :
 iIIIi1i1I11i ( )
 if 79 - 79: O0OoO * OO0 * oOo0O0Ooo * Ii1I / Ii1I
elif OoiI1I1 == 222 :
 iIIIII1ii1I ( IiI111111IIII )
 if 62 - 62: OO0 * O0O0OoOO0 % Ii1I - ooOoO0O00 - Ii1I
elif OoiI1I1 == 333 :
 O0oo0O00ooOo ( IiI111111IIII )
 if 24 - 24: O0OoO
 if 71 - 71: ooo0oo0o0oo - ooOoO0O00
elif OoiI1I1 == 1020 :
 Ii11II1IIIIIi ( )
 if 56 - 56: OOooOOo + IIIi
elif OoiI1I1 == 1021 :
 ANIMEEP ( )
 if 74 - 74: IIIIi1i / iii1iiii1 / IIiIiII11i - IIIIi1i / IIIi % oO0o0OOOO
elif OoiI1I1 == 1022 :
 ANIMEPLAY ( IiI111111IIII )
 if 19 - 19: ooo0oo0o0oo % ii + ii
elif OoiI1I1 == 1001 :
 iIi11i1I11Ii ( )
 if 7 - 7: ooOoO0O00
elif OoiI1I1 == 1005 :
 I1Ii111I111 ( )
 if 91 - 91: OOooOOo - OOooOOo . ooo0oo0o0oo
elif OoiI1I1 == 1007 :
 iIi11O00oO ( IiI111111IIII )
 if 33 - 33: iii1iiii1 - iI11I1II1I1I / O0O0OoOO0 % o0o00Oo0O
elif OoiI1I1 == 1010 :
 OOo00oOo ( IiI111111IIII )
 if 80 - 80: ooo0oo0o0oo % ii - ooo0oo0o0oo
elif OoiI1I1 == 1011 :
 OoIII ( IiI111111IIII )
 if 27 - 27: iii1iiii1 - I11i * Ii1I - oOo0O0Ooo
elif OoiI1I1 == 1012 :
 oOI1ii11IiI1I ( IiI111111IIII )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIIIi1i . O0O0OoOO0
elif OoiI1I1 == 1030 :
 OO00O ( )
 if 100 - 100: IIiIiII11i / iii1iiii1 / IIIIi1i - Ii1I * iI11I1II1I1I
elif OoiI1I1 == 1031 :
 O0ooOOo00o0oO0O0 ( IiI111111IIII , i1i1IIIIi1i )
 if 7 - 7: ooOoO0O00 . ooo0oo0o0oo % Ii * Ii1I . oO0o0OOOO % Ii1I
elif OoiI1I1 == 1032 :
 oOO0o0oOoO ( IiI111111IIII )
 if 35 - 35: oOo0O0Ooo
elif OoiI1I1 == 1006 :
 Parse . ParseURL ( IiI111111IIII )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif OoiI1I1 == 2030 :
 Parse . addonParseURL ( IiI111111IIII )
 if 22 - 22: OO0 . Ii . ii . ooOoO0O00
elif OoiI1I1 == 2031 :
 Parse . apkParseURL ( IiI111111IIII )
 if 12 - 12: OOooOOo % O0OoO + IIIi . o0o00Oo0O % iI11I1II1I1I
elif OoiI1I1 == 1002 :
 Iiiiii ( IiI111111IIII )
 if 41 - 41: ii
elif OoiI1I1 == 1003 :
 OOoo000o ( IiI111111IIII , i1i1IIIIi1i )
 if 13 - 13: oO0o0OOOO + iii1iiii1 - iii1iiii1 % IIIi / oO0o0OOOO
elif OoiI1I1 == 1004 :
 O000OoOO0oO ( IiI111111IIII )
 if 4 - 4: oOo0O0Ooo + O0OoO - ooo0oo0o0oo + IIIIi1i
elif OoiI1I1 == 1008 :
 OOoOoO ( )
 if 78 - 78: O0O0OoOO0
elif OoiI1I1 == 1009 :
 OO0O00OO0 ( IiI111111IIII )
 if 29 - 29: IIiIiII11i
elif OoiI1I1 == 2001 :
 i111i1IIi1i ( )
 if 79 - 79: iI11I1II1I1I - Ii + OO0 - IIiIiII11i . iI11I1II1I1I
elif OoiI1I1 == 2002 :
 oooooOOo0Oo ( IiI111111IIII )
 if 84 - 84: I1ii11iIi11i % oO0o0OOOO * o0o00Oo0O * oO0o0OOOO
elif OoiI1I1 == 1013 :
 oOOOooOo0O ( )
elif OoiI1I1 == 10111113 :
 III1i111i ( IiI111111IIII )
 if 66 - 66: O0OoO / iI11I1II1I1I - OOooOOo % o0o00Oo0O . OO0
elif OoiI1I1 == 1014 :
 IiiII ( )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif OoiI1I1 == 1015 :
 I1ii1iI ( IiI111111IIII )
 if 37 - 37: ooOoO0O00 * Ii
elif OoiI1I1 == 1016 :
 O000oOOoOOO ( IiI111111IIII , i1i1IIIIi1i , Iii1IIII11I )
 if 95 - 95: Ii % iii1iiii1 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif OoiI1I1 == 1017 :
 o0ooooO0o0O ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / O0OoO / iii1iiii1
elif OoiI1I1 == 1018 :
 iiIiii1IIIII ( IiI111111IIII )
 if 35 - 35: IIIIi1i * O0OoO
elif OoiI1I1 == 1023 :
 I111i1I1 ( )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif OoiI1I1 == 1024 :
 O0oo0ooO00 ( IiI111111IIII )
 if 13 - 13: oO0o * iii1iiii1 + I1ii11iIi11i - ooo0oo0o0oo
elif OoiI1I1 == 1025 :
 oOoO0 ( IiI111111IIII )
 if 31 - 31: oO0o
elif OoiI1I1 == 4001 :
 iI1Ii11iIiI1 ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif OoiI1I1 == 4002 :
 oOOoo00O00o ( )
 if 77 - 77: Ii - iii1iiii1 . Ii1I % I1ii11iIi11i . O0O0OoOO0
elif OoiI1I1 == 4003 :
 iIIiI1I1i ( )
 if 9 - 9: I11i
elif OoiI1I1 == 4004 :
 oO00O000oO0 ( )
 if 55 - 55: O0OoO % iI11I1II1I1I + oO0o0OOOO . OO0
elif OoiI1I1 == 4005 :
 O0OO ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif OoiI1I1 == 4006 :
 i1I1i111Ii ( )
 if 23 - 23: Ii
elif OoiI1I1 == 4007 :
 IiI1iiiIii ( )
 if 88 - 88: IIiIiII11i - IIIIi1i / ii
elif OoiI1I1 == 4008 :
 I1III1111iIi ( )
 if 71 - 71: Ii1I
elif OoiI1I1 == 4009 : O0OoOO0o ( )
elif OoiI1I1 == 4010 : I1I11iI11iI1i ( )
elif OoiI1I1 == 3000 :
 O00o0 ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OoiI1I1 == 3001 :
 O0O0 ( )
 if 1 - 1: ooo0oo0o0oo % ooOoO0O00
elif OoiI1I1 == 3002 :
 oO0oo ( IiI111111IIII )
 if 41 - 41: oO0o * oO0o / IIIIi1i + Ii1I . I11i
elif OoiI1I1 == 3003 :
 o00o0o000Oo ( IiI111111IIII )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / O0O0OoOO0
elif OoiI1I1 == 3004 :
 iIiII ( IiI111111IIII )
 if 80 - 80: Ii1I
elif OoiI1I1 == 404 :
 iiiI1I1iiiII ( Iii1IIII11I , IiI111111IIII , i1i1IIIIi1i )
 if 67 - 67: IIiIiII11i
elif OoiI1I1 == 405 :
 OO0ooo0OOO ( IiI111111IIII )
 if 2 - 2: I11i - o0o00Oo0O * O0O0OoOO0 % ooo0oo0o0oo
elif OoiI1I1 == 7030 :
 iIiOo ( )
 if 64 - 64: ooOoO0O00 . OO0
elif OoiI1I1 == 7021 :
 IiOOo0 ( Iii1IIII11I )
 if 7 - 7: IIIi . IIIIi1i - IIIIi1i / iii1iiii1 % I1ii11iIi11i
elif OoiI1I1 == 7022 :
 oO00o0O00o ( Iii1IIII11I )
 if 61 - 61: IIIi - Ii1I / IIIIi1i % Ii1I + oO0o / I1ii11iIi11i
elif OoiI1I1 == 7000 :
 iIi11ooOo0oO0O ( Iii1IIII11I , IiI111111IIII , img )
 if 10 - 10: Ii / OOooOOo
elif OoiI1I1 == 7050 :
 OOiii1IiiIiIIiI ( IiI111111IIII )
 if 27 - 27: oOo0O0Ooo / ii
elif OoiI1I1 == 7051 :
 IiIIii ( IiI111111IIII )
 if 74 - 74: Ii1I % iii1iiii1 - oO0o * oO0o0OOOO . ii * oO0o
elif OoiI1I1 == 7052 :
 i1I ( IiI111111IIII )
 if 99 - 99: OOooOOo . IIIIi1i - ii - o0o00Oo0O
elif OoiI1I1 == 7053 :
 IiiIIIIi ( IiI111111IIII )
 if 6 - 6: O0OoO
elif OoiI1I1 == 7054 :
 CoolPlay ( IiI111111IIII )
 if 3 - 3: o0o00Oo0O - iii1iiii1 * O0O0OoOO0 * O0OoO / O0O0OoOO0
elif OoiI1I1 == 7060 :
 i1ooOO00o0 ( )
 if 58 - 58: O0O0OoOO0 * iI11I1II1I1I + OO0 . OO0
elif OoiI1I1 == 7061 :
 oOiiIIIII ( IiI111111IIII )
 if 74 - 74: OO0 - I11i * ooo0oo0o0oo % OO0
elif OoiI1I1 == 7063 :
 Ii1I1iIiiI1 ( IiI111111IIII )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * iii1iiii1 - oO0o - I11i
elif OoiI1I1 == 7062 :
 iiiI1IiI ( IiI111111IIII )
 if 44 - 44: ii
elif OoiI1I1 == 7064 :
 NATatozcat ( )
 if 82 - 82: OOooOOo . OOooOOo
elif OoiI1I1 == 7067 :
 Ii111IIIIii ( IiI111111IIII )
 if 10 - 10: I1ii11iIi11i * Ii1I . IIIi . ii . O0OoO * Ii1I
elif OoiI1I1 == 7066 :
 NATatozA ( IiI111111IIII )
 if 80 - 80: iii1iiii1 + oO0o0OOOO . iii1iiii1 + O0OoO
elif OoiI1I1 == 7065 :
 O00oIii1iIIiii1ii ( IiI111111IIII )
 if 85 - 85: Ii . oO0o0OOOO + O0O0OoOO0 / O0O0OoOO0
elif OoiI1I1 == 7070 :
 Oo00O ( )
 if 43 - 43: ooo0oo0o0oo . ii - IIiIiII11i
elif OoiI1I1 == 7071 :
 DIZIlist ( IiI111111IIII )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O0OoO * IIIi
elif OoiI1I1 == 7072 :
 DIZIpull ( IiI111111IIII )
 if 19 - 19: iii1iiii1 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OoiI1I1 == 7073 :
 WATCHDIZI ( IiI111111IIII )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OoiI1I1 == 7002 :
 O0ooO ( )
 if 15 - 15: O0O0OoOO0 + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OoiI1I1 == 7003 :
 ooO00OoOOoO0o ( IiI111111IIII )
 if 54 - 54: ooo0oo0o0oo - IIiIiII11i . OO0 + O0O0OoOO0
elif OoiI1I1 == 7004 :
 Iiio0OO00oOOO0o0 ( IiI111111IIII )
 if 45 - 45: IIIi + IIiIiII11i . IIIIi1i / Ii1I
elif OoiI1I1 == 7020 :
 Oo0oo0OOO0OOoOO ( IiI111111IIII )
 if 76 - 76: O0O0OoOO0 + IIIIi1i - ooo0oo0o0oo * iI11I1II1I1I % ooOoO0O00
elif OoiI1I1 == 7001 :
 OoO0o00oo0oO ( )
 if 72 - 72: OO0 + IIiIiII11i . o0o00Oo0O - IIIIi1i / ii . iii1iiii1
elif OoiI1I1 == 7010 :
 o0OoOo0o0OOoO0 ( IiI111111IIII )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OoiI1I1 == 7011 :
 iI11ii ( IiI111111IIII )
 if 32 - 32: ii
elif OoiI1I1 == 7012 :
 OO0oooOO ( IiI111111IIII )
 if 29 - 29: Ii1I
elif OoiI1I1 == 7013 :
 cnfTVPlay2 ( IiI111111IIII )
elif OoiI1I1 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IiI111111IIII )
elif OoiI1I1 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IiI111111IIII )
elif OoiI1I1 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Iii1IIII11I , IiI111111IIII , i1i1IIIIi1i )
elif OoiI1I1 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OoiI1I1 == 7018 :
 I1Iii ( )
elif OoiI1I1 == 7019 :
 CNF_Studio_Indexer . List_Movies ( IiI111111IIII )
elif OoiI1I1 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IiI111111IIII )
elif OoiI1I1 == 7024 :
 CNF_Studio_Indexer . Box_Office ( IiI111111IIII )
 if 41 - 41: O0O0OoOO0
elif OoiI1I1 == 8000 :
 ooOoOooo00Oo ( )
elif OoiI1I1 == 8001 :
 OooO00o000 ( )
elif OoiI1I1 == 8002 :
 o0ooo ( )
elif OoiI1I1 == 8003 :
 i1iI1IIi ( )
elif OoiI1I1 == 8004 :
 IiI1I1IIIi1i ( )
elif OoiI1I1 == 8005 :
 ooo000o ( )
elif OoiI1I1 == 8006 :
 iI1I1I ( Iii1IIII11I , IiI111111IIII )
elif OoiI1I1 == 8030 :
 oOoooO0 ( IiI111111IIII )
elif OoiI1I1 == 8045 :
 OOOooO00OO00O ( IiI111111IIII )
elif OoiI1I1 == 8046 :
 OoOOooO0O ( IiI111111IIII )
elif OoiI1I1 == 8047 :
 Ii1 ( IiI111111IIII )
elif OoiI1I1 == 8048 :
 OO0OooOo ( IiI111111IIII )
elif OoiI1I1 == 8049 :
 ii111iI1i1 ( IiI111111IIII )
elif OoiI1I1 == 8020 :
 O0Oo00o0o ( )
elif OoiI1I1 == 8021 :
 oooooO0oO0o ( IiI111111IIII )
elif OoiI1I1 == 8022 :
 O0ooo0Ooo ( IiI111111IIII )
elif OoiI1I1 == 8023 :
 oOOo0OOOOo0o ( IiI111111IIII )
elif OoiI1I1 == 8040 :
 OOO00o0 ( )
elif OoiI1I1 == 8041 :
 ooIi111iII ( IiI111111IIII )
elif OoiI1I1 == 8042 :
 IIi1ii ( IiI111111IIII )
elif OoiI1I1 == 8043 :
 yt . PlayVideo ( IiI111111IIII )
elif OoiI1I1 == 8044 :
 Ii1i1i ( IiI111111IIII )
elif OoiI1I1 == 8060 :
 II1i ( )
elif OoiI1I1 == 8061 :
 IiiiI1 ( IiI111111IIII )
elif OoiI1I1 == 8064 :
 o0Oo00oOO ( )
elif OoiI1I1 == 8065 :
 O0oo ( IiI111111IIII )
elif OoiI1I1 == 8070 :
 O00oO0O ( )
elif OoiI1I1 == 8071 :
 IiiI111I11 ( IiI111111IIII )
elif OoiI1I1 == 7080 :
 oO0Ooooo000 ( IiI111111IIII )
elif OoiI1I1 == 8090 :
 Ii1IiiiI1ii ( )
elif OoiI1I1 == 8091 :
 o0oOOoo0O ( IiI111111IIII )
elif OoiI1I1 == 8092 :
 OO0III ( IiI111111IIII )
elif OoiI1I1 == 8093 :
 OoooOo00 ( IiI111111IIII )
elif OoiI1I1 == 8081 :
 i1111I ( )
elif OoiI1I1 == 8062 :
 O0ooo ( IiI111111IIII )
elif OoiI1I1 == 8063 :
 iI1ii ( IiI111111IIII )
elif OoiI1I1 == 8050 :
 I11iiIIII1I1 ( )
elif OoiI1I1 == 8051 :
 i1IIi1i1Ii1 ( IiI111111IIII )
elif OoiI1I1 == 8052 :
 Iiio0Oo0oO ( IiI111111IIII )
elif OoiI1I1 == 8085 :
 O00Ooo0O0OOOo ( )
elif OoiI1I1 == 8086 :
 iIIIiIi1i ( IiI111111IIII )
elif OoiI1I1 == 8087 :
 IiIIIiI ( IiI111111IIII )
elif OoiI1I1 == 8088 :
 II1iI1iiiI ( IiI111111IIII , Iii1IIII11I )
elif OoiI1I1 == 9000 :
 o0OoO000O ( )
elif OoiI1I1 == 1111 :
 ii1o0 ( )
elif OoiI1I1 == 9001 :
 oOo000o ( )
elif OoiI1I1 == 9002 :
 O0O0Oo00OO ( )
elif OoiI1I1 == 9003 :
 i1i1i11iI11II ( )
elif OoiI1I1 == 9004 :
 o0o0O00oOo ( )
elif OoiI1I1 == 9005 :
 iI1iiii ( IiI111111IIII )
elif OoiI1I1 == 9006 :
 OOoO0oOOO ( IiI111111IIII )
elif OoiI1I1 == 9007 :
 iIii1iIiII1i1 ( )
elif OoiI1I1 == 9008 :
 o0oO ( IiI111111IIII )
elif OoiI1I1 == 9009 :
 o0OoIII1IIiIi1 ( IiI111111IIII )
elif OoiI1I1 == 9010 :
 iIIi1II1 ( )
elif OoiI1I1 == 9011 :
 IiI1I11ii ( IiI111111IIII )
elif OoiI1I1 == 50 :
 IIo0OoO00 ( IiI111111IIII )
elif OoiI1I1 == 9020 :
 champlist ( )
elif OoiI1I1 == 9021 :
 oOOI1 ( )
elif OoiI1I1 == 9022 :
 OOI1i ( )
elif OoiI1I1 == 9023 :
 i1II1iII1 ( )
elif OoiI1I1 == 9024 :
 Oo00oo00o00Oo ( IiI111111IIII )
elif OoiI1I1 == 9030 :
 OOo0O ( IiI111111IIII )
elif OoiI1I1 == 9031 :
 iiOo0ooo ( IiI111111IIII )
elif OoiI1I1 == 9032 :
 Oo00o00 ( IiI111111IIII )
elif OoiI1I1 == 9033 :
 OoOo0O0 ( IiI111111IIII )
elif OoiI1I1 == 9034 :
 oo0oO ( )
elif OoiI1I1 == 7085 :
 i11I ( IiI111111IIII )
elif OoiI1I1 == 7086 :
 Ooo0o0000OO ( IiI111111IIII )
elif OoiI1I1 == 7087 :
 I1iiII ( I1iii11 )
elif OoiI1I1 == 9666 :
 Ii1II11II1iii ( IiI111111IIII )
elif OoiI1I1 == 10100 : Ii1Ii1IiIIIi1 ( )
elif OoiI1I1 == 10105 : oooO0o0oOoO ( IiI111111IIII )
elif OoiI1I1 == 10106 : I1Ii1 ( IiI111111IIII )
elif OoiI1I1 == 10104 : OO0Oo00Oo ( IiI111111IIII )
elif OoiI1I1 == 10107 : o0oi1I1I1I ( )
elif OoiI1I1 == 10103 : O00o0OO0OO0oo ( IiI111111IIII )
elif OoiI1I1 == 10108 : i11ii111i1ii ( IiI111111IIII )
elif OoiI1I1 == 10107 : o0oi1I1I1I ( )
elif OoiI1I1 == 10000 : Origin_Menu ( )
elif OoiI1I1 == 10001 : OOoooOoO0Oo ( )
elif OoiI1I1 == 10002 : OoO0o0OOOO ( )
elif OoiI1I1 == 10003 : oO00o ( )
elif OoiI1I1 == 10004 : O00o ( IiI111111IIII )
elif OoiI1I1 == 10005 : i11i11 ( )
elif OoiI1I1 == 10006 : oO0OoooO0oOO00OoOo ( IiI111111IIII )
elif OoiI1I1 == 10007 : IiIi1i ( IiI111111IIII , i1i1IIIIi1i )
elif OoiI1I1 == 10008 : I1iIi1iIIIIiI ( )
elif OoiI1I1 == 10009 : II11ii1I11 ( )
elif OoiI1I1 == 10010 : Oo0O0OO0OoO0 ( IiI111111IIII )
elif OoiI1I1 == 10011 : I1I1i ( IiI111111IIII )
elif OoiI1I1 == 10012 : o0Ooo0O0 ( IiI111111IIII )
elif OoiI1I1 == 10109 : o0000Oo0 ( IiI111111IIII )
elif OoiI1I1 == 10013 : o00OOo0o0O ( IiI111111IIII )
elif OoiI1I1 == 10014 : O0o0OO00 ( )
elif OoiI1I1 == 10015 : oOo00OoO0O ( )
elif OoiI1I1 == 10016 : II1II1iI ( IiI111111IIII )
elif OoiI1I1 == 10017 : iIIii1 ( )
elif OoiI1I1 == 10018 : Oo0o00ooOOOoOo ( )
elif OoiI1I1 == 10019 : OoO0 ( )
elif OoiI1I1 == 10020 : o0oo0o00ooO00 ( )
elif OoiI1I1 == 10021 : o0O0OOo0oO ( )
elif OoiI1I1 == 10022 : i1i1 ( IiI111111IIII )
elif OoiI1I1 == 10023 : iIIIi1IiI11I1 ( Iii1IIII11I , IiI111111IIII )
elif OoiI1I1 == 10024 : III11I1 ( IiI111111IIII )
elif OoiI1I1 == 10025 : O0o0o0 ( )
elif OoiI1I1 == 10026 : OoO0oO ( )
elif OoiI1I1 == 10027 : i1III1iI ( )
elif OoiI1I1 == 10028 : o0OoOOo ( )
elif OoiI1I1 == 10029 : ii1iIi1Ii1 ( )
elif OoiI1I1 == 423 : o0oO00 ( IiI111111IIII )
elif OoiI1I1 == 426 : iI1ii11Ii ( IiI111111IIII )
elif OoiI1I1 == 10030 : Izle_Films ( )
elif OoiI1I1 == 10031 : Latest_Izle_Movies ( )
elif OoiI1I1 == 10032 : Izle_Genres ( )
elif OoiI1I1 == 10033 : Izle_Pop_Movies ( )
elif OoiI1I1 == 10034 : Izle_Boxsets ( )
elif OoiI1I1 == 10035 : Izle_Search ( )
elif OoiI1I1 == 10036 : Izle_Genres_Movie ( IiI111111IIII )
elif OoiI1I1 == 10037 : Izle_Boxset_single ( IiI111111IIII )
elif OoiI1I1 == 10038 : Izle_IFRAME ( )
elif OoiI1I1 == 10039 : Izle_Boxsets_Next ( IiI111111IIII )
elif OoiI1I1 == 10040 : oOO00ooOOo ( )
elif OoiI1I1 == 10041 : IIi1i1 ( IiI111111IIII )
elif OoiI1I1 == 10042 : O0000Oo ( IiI111111IIII )
elif OoiI1I1 == 10043 : IiI ( )
elif OoiI1I1 == 10044 : i1i1iIII11i ( IiI111111IIII )
elif OoiI1I1 == 10045 : oOoo0ooOoo ( Iii1IIII11I )
elif OoiI1I1 == 10046 : II111I1 ( IiI111111IIII )
elif OoiI1I1 == 10047 : Ooi1IIii11i1I1 ( IiI111111IIII )
elif OoiI1I1 == 10048 : OOOOoO ( IiI111111IIII )
elif OoiI1I1 == 10049 : oOo0OOOOoO ( IiI111111IIII )
elif OoiI1I1 == 10050 : I11iiI11I1II ( )
elif OoiI1I1 == 10051 : O0OOoOOO ( )
elif OoiI1I1 == 10052 : oOO000000oO0 ( )
elif OoiI1I1 == 10053 : Addon ( IiI111111IIII )
elif OoiI1I1 == 10054 : Iii1I1I ( IiI111111IIII , Iii1IIII11I )
elif OoiI1I1 == 10055 :
 o0OO00oo0O ( "addFavorite" )
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 Iii1I ( Iii1IIII11I , IiI111111IIII , i1i1IIIIi1i , oO0o0 , OOo0iIiiI11II11 )
elif OoiI1I1 == 10056 :
 o0OO00oo0O ( "rmFavorite" )
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1IIII11I = Iii1IIII11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oo0 ( Iii1IIII11I )
elif OoiI1I1 == 10057 :
 o0OO00oo0O ( "getFavorites" )
 iiIiiIi1 ( )
elif OoiI1I1 == 10058 : ooooo0O0000oo ( )
elif OoiI1I1 == 10059 : Donators_Guide ( )
elif OoiI1I1 == 10060 : oooO0o0o0O0 ( )
elif OoiI1I1 == 10061 : I1ii ( )
elif OoiI1I1 == 10062 : I1i11ii11 ( Iii1IIII11I , IiI111111IIII , I1iii11 )
elif OoiI1I1 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + ooooooO0oo + ")" )
elif OoiI1I1 == 10064 : Iiii ( )
elif OoiI1I1 == 10065 : I111iIi1 ( IiI111111IIII )
elif OoiI1I1 == 10066 : oO0oO0 ( IiI111111IIII )
elif OoiI1I1 == 10068 : I1iIi1iIiiIiI ( IiI111111IIII )
elif OoiI1I1 == 10069 : I11ii1i1 ( IiI111111IIII )
elif OoiI1I1 == 10070 : OooO0oo ( IiI111111IIII )
elif OoiI1I1 == 10071 : Genie_Watch ( )
elif OoiI1I1 == 10072 : iiI11i1II ( )
elif OoiI1I1 == 10073 : I1i11i ( IiI111111IIII )
elif OoiI1I1 == 10074 : ooooO0oOoOOoO ( IiI111111IIII )
elif OoiI1I1 == 10075 : ooo ( i1i1IIIIi1i , Iii1IIII11I , IiI111111IIII )
elif OoiI1I1 == 10076 : OOOoOoO ( IiI111111IIII )
elif OoiI1I1 == 10077 : iiI1I1 ( IiI111111IIII )
elif OoiI1I1 == 10078 : o0O00OooOOOOO ( )
elif OoiI1I1 == 10079 : Genie_Watch_Tv_Shows ( )
elif OoiI1I1 == 10080 : Genie_Watch_Tv_Genre ( IiI111111IIII )
elif OoiI1I1 == 10081 : Genie_Watch_TV_PlayRun ( IiI111111IIII )
elif OoiI1I1 == 10082 : Genie_Watch_TV_Episodes ( IiI111111IIII , i1i1IIIIi1i )
elif OoiI1I1 == 10083 : Genie_Watch_Tv_Recent ( IiI111111IIII )
elif OoiI1I1 == 10084 : o0oooOO00 ( )
elif OoiI1I1 == 10085 : o0O0OOO0Ooo ( )
elif OoiI1I1 == 10086 : ooOOOoO ( )
elif OoiI1I1 == 20000 : OO0o0oO0O000o ( )
elif OoiI1I1 == 20001 : iiII1IiIi1iI1 ( )
elif OoiI1I1 == 20002 : o0oO0Oo ( IiI111111IIII )
elif OoiI1I1 == 20003 : o0O0OO0o ( IiI111111IIII )
elif OoiI1I1 == 20004 : o0O0oo0o ( IiI111111IIII )
elif OoiI1I1 == 21004 : II1 ( )
elif OoiI1I1 == 21005 : I11Iii1 ( IiI111111IIII )
elif OoiI1I1 == 21006 : III1Ii1i1I1 ( IiI111111IIII )
elif OoiI1I1 == 21007 : iIi ( IiI111111IIII )
elif OoiI1I1 == 30000 : i1I1 ( )
elif OoiI1I1 == 30001 : I1III111i ( )
elif OoiI1I1 == 10012 : Resolve ( IiI111111IIII )
elif OoiI1I1 == 30003 : i1iIIi1o0o0OoOOOOOo ( )
elif OoiI1I1 == 30004 : III1I1 ( IiI111111IIII )
elif OoiI1I1 == 30005 : o0i1iI1iiI1I ( IiI111111IIII )
elif OoiI1I1 == 30006 : iIIiI1iiI ( )
elif OoiI1I1 == 30007 : O0Oo00OO00Ooo ( )
elif OoiI1I1 == 30008 : o0OOOOO0O ( IiI111111IIII )
elif OoiI1I1 == 30009 : OoOOo00 ( IiI111111IIII )
elif OoiI1I1 == 30010 : IiiiI ( IiI111111IIII )
elif OoiI1I1 == 30011 : Ii1iI ( )
elif OoiI1I1 == 30012 : II1Ii ( )
elif OoiI1I1 == 30013 : o0IiiiI111I ( )
elif OoiI1I1 == 30014 : o00ii111Iiii ( )
elif OoiI1I1 == 30015 : ii1IiIi11 ( IiI111111IIII , i1i1IIIIi1i , oO0o0 )
elif OoiI1I1 == 30016 : ii1ii ( IiI111111IIII )
elif OoiI1I1 == 30019 : o0Oo ( IiI111111IIII )
elif OoiI1I1 == 30017 : i1oOOOOOOOoO ( IiI111111IIII )
elif OoiI1I1 == 30018 : ii1iI1II11ii ( IiI111111IIII )
elif OoiI1I1 == 30030 : iIII11Iiii1 ( )
elif OoiI1I1 == 30031 : o0oo0 ( )
elif OoiI1I1 == 30032 : OoO0OOoO0Oo0 ( )
elif OoiI1I1 == 30033 : oO00O ( )
elif OoiI1I1 == 30034 : II111IiiiI1 ( )
elif OoiI1I1 == 30035 : iIIi ( IiI111111IIII )
elif OoiI1I1 == 30036 : ooO00O00oOO ( IiI111111IIII )
elif OoiI1I1 == 30037 : I1IIII1ii ( IiI111111IIII )
elif OoiI1I1 == 30038 : Oo ( )
elif OoiI1I1 == 30039 : II1iiIiIiI ( )
elif OoiI1I1 == 50000 : i1I1ii11i1Iii ( )
elif OoiI1I1 == 50001 : OOo0 ( )
elif OoiI1I1 == 50002 : OoOoooo0O ( IiI111111IIII )
elif OoiI1I1 == 50003 : iI ( I1iii11 )
elif OoiI1I1 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OoiI1I1 == 60001 : I1Iiiiiii ( )
elif OoiI1I1 == 60002 : ii1iI ( Iii1IIII11I )
elif OoiI1I1 == 60003 : o0iiiI1I1iIIIi1 ( Iii1IIII11I )
elif OoiI1I1 == 50004 : iI1i11iII111 ( )
elif OoiI1I1 == 50005 : speedtest . runtest ( IiI111111IIII )
elif OoiI1I1 == 70001 : iIIi1I ( )
elif OoiI1I1 == 70002 : OO0Ooo0 ( IiI111111IIII )
elif OoiI1I1 == 70003 : oooO00o0 ( IiI111111IIII )
elif OoiI1I1 == 70004 : o0o00oO0oo000 ( IiI111111IIII )
elif OoiI1I1 == 70005 : oO000o ( IiI111111IIII )
elif OoiI1I1 == 70006 : I1I1Iiii1 ( )
elif OoiI1I1 == 50006 : ii1I ( i1 , i1111 )
elif OoiI1I1 == 80000 : o0oOO0ooOoO ( )
if 49 - 49: O0O0OoOO0 % IIiIiII11i . O0O0OoOO0 - I11i - oO0o0OOOO * ooo0oo0o0oo
if 47 - 47: o0o00Oo0O . I11i / O0O0OoOO0 * IIIIi1i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
