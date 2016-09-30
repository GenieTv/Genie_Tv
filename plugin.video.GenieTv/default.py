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
IiiIII111iI = "3.1.4"
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
 if not os . path . exists ( i1iiIII111ii ) :
  I1IiiiiI ( )
  if 80 - 80: ii1ii11IIIiiI . Ii - I11i
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']CONTACT US[/COLOR]' , '' , 50006 , III1iII1I1ii + 'Contact-Us.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , III1iII1I1ii + 'settings.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , III1iII1I1ii + 'GenieUpdate.png' , OO0o , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , OO0o , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , OO0o , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , OO0o , '' )
  if 2 - 2: I11O0O0oOO00O00o + iI1ii11iIi1i - oOo0O0Ooo % I11i . Ii1IIIi1
 if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1I1IiI1 ) , 32 , III1iII1I1ii + 'BuildersToolbox.png' , OO0o , '' )
 if oo00 . getSetting ( 'Source List' ) == 'true' :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']SOURCE LIST[/COLOR]' , str ( I1I1IiI1 ) , 46 , III1iII1I1ii + 'SoruceList.png' , OO0o , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , OO0o , '' )
 if oo00 . getSetting ( 'Addons' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']ADDONS[/COLOR]' , '' , 10050 , III1iII1I1ii + 'Addons.png' , OO0o , '' )
 if I1I1i1I ( ) == 'android' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']APK TOOL[/COLOR]' , str ( I1I1IiI1 ) , 30039 , III1iII1I1ii + 'APKTools.png' , OO0o , '' )
 if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv RSS Feed[/COLOR]' , str ( I1I1IiI1 ) , 39 , III1iII1I1ii + 'GenieTVRSSFeed.png' , OO0o , '' )
  if 30 - 30: ii
  if 5 - 5: O0OOOoOoo0 - IIiIiII11i - ii % iI1ii11iIi1i + oOo0O0Ooo * iI11I1II1I1I
 I1I1II1I11 ( 'movies' , 'MAIN' )
def IIiiIiII1Ii ( ) :
 oo00oOO000oO0 = iIIII11I1II ( )
 Ii1IIiI1i = oo00oOO000oO0 . replace ( II , "" )
 if os . path . exists ( oo00oOO000oO0 ) or not oo00oOO000oO0 == False :
  o0Oo00 = open ( oo00oOO000oO0 , mode = 'r' ) ; iI = o0Oo00 . read ( ) ; o0Oo00 . close ( )
  O0O0Oooo0o ( "%s - %s" % ( i1 , Ii1IIiI1i ) , iI )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def iIIII11I1II ( ) :
 oOOoo00O00o = False
 if os . path . exists ( os . path . join ( II , 'xbmc.log' ) ) :
  oOOoo00O00o = os . path . join ( II , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II , 'kodi.log' ) ) :
  oOOoo00O00o = os . path . join ( II , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II , 'spmc.log' ) ) :
  oOOoo00O00o = os . path . join ( II , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II , 'tvmc.log' ) ) :
  oOOoo00O00o = os . path . join ( II , 'tvmc.log' )
 return oOOoo00O00o
 if 98 - 98: O00o0O00 + ooOOOoO + oO0oo0o % ii
def oooooo0O000o ( url ) :
 if url == 'http://' : return False
 try :
  Oo0oOOo = urllib2 . Request ( url )
  Oo0oOOo . add_header ( 'User-Agent' , I1i1iiI1 )
  Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
  Oo0OoO00oOO0o . close ( )
 except Exception , OoO :
  return OoO
 return True
 if 51 - 51: ii * O00o0O00
def OO0ooOOO0OOO ( ) :
 OOO00O = O0i1II1Iiii1I11 ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( OOO00O )
 if len ( IIi1I11I1II ) > 0 :
  for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOoOooooOOo , oOo0O in IIi1I11I1II :
   iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 50005 , OoOOoOooooOOo , oOo0O , '' )
def oo0O0 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , OO0o , '' )
 if 22 - 22: OOooOOo . O00o0O00 * OOooOOo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def O000OOO ( ) :
 O000OOo00oo ( )
 if II11iiii1Ii == '5knuckleshuffle' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , OO0o , '' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , OO0o , '' )
 if oo00 . getSetting ( 'Favourites' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , OO0o , '' )
 if oo00 . getSetting ( 'Search' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , OO0o , '' )
 if 20 - 20: I11i . IIiIiII11i % O00o0O00 * iI11I1II1I1I
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , OO0o , '' )
  if 98 - 98: oOo0O0Ooo % iI1ii11iIi1i * ii
 I1IIII1i ( '[COLOR' + iiI1IiI + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 4004 , III1iII1I1ii + 'Movies.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']TV SHOWS[/COLOR]' , str ( I1I1IiI1 ) , 4005 , III1iII1I1ii + 'TVShows.png' , OO0o , '' )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 4007 , III1iII1I1ii + 'Kids.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']24/7 STREAMS[/COLOR]' , '' , 30030 , III1iII1I1ii + '247Streams.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']NEWS[/COLOR]' , str ( I1I1IiI1 ) , 30032 , III1iII1I1ii + 'News.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'GenieTVTutorials.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HOBBIES[/COLOR]' , str ( I1I1IiI1 ) , 4008 , III1iII1I1ii + 'Hobbies.png' , OO0o , '' )
 if oo00 . getSetting ( 'YOUTUBE' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH YOUTUBE[/COLOR]' , str ( I1I1IiI1 ) , 10064 , III1iII1I1ii + 'SeachYouTube.png' , OO0o , '' )
 if oo00 . getSetting ( 'REQUESTS' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']REQUESTS[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , III1iII1I1ii + 'Requests.png' , OO0o , '' )
 if oo00 . getSetting ( 'Stand Up' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']STAND UP[/COLOR]' , '' , 10003 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
 if oo00 . getSetting ( 'Documentaries' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']DOCUMENTARIES[/COLOR]' , str ( I1I1IiI1 ) , 8040 , III1iII1I1ii + 'documentaries.png' , OO0o , '' )
 if oo00 . getSetting ( 'Disclose' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']DISCLOSE TV[/COLOR]' , str ( I1I1IiI1 ) , 7001 , III1iII1I1ii + 'DiscloseTV.png' , OO0o , '' )
  if 51 - 51: iI11I1II1I1I . OOooOOo / oO0oo0o + I11i
  if 33 - 33: O0OOOoOoo0 . IIiIiII11i % Ii1IIIi1 + I11i
 if oo00 . getSetting ( 'Playlist Loader' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']PLAYLIST LOADER[/COLOR]' , str ( I1I1IiI1 ) , 3000 , III1iII1I1ii + 'PlaylistLoader.png' , OO0o , '' )
  if 71 - 71: I1ii11iIi11i % O00o0O00
  if 98 - 98: I11O0O0oOO00O00o % Ii % O0OOOoOoo0 + iI1ii11iIi1i
  if 78 - 78: Ii1I % oO0oo0o / Ii1IIIi1 - iI11I1II1I1I
  if 69 - 69: ii1ii11IIIiiI
  if 11 - 11: oOo0O0Ooo
  if 16 - 16: iI1ii11iIi1i + ooOOOoO * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
  if 67 - 67: ii / oOo0O0Ooo * iI1ii11iIi1i + I11O0O0oOO00O00o
  if 65 - 65: ii - Ii1I / O0OOOoOoo0 / IIiIiII11i / ooOoO0O00
  if 71 - 71: ii1ii11IIIiiI + iI1ii11iIi1i
  if 28 - 28: O00o0O00
  if 38 - 38: O0OOOoOoo0 % IIiIiII11i % I11O0O0oOO00O00o / oO0o + OOooOOo / ooOoO0O00
  if 54 - 54: iI11I1II1I1I % Ii1I - O00o0O00 / oO0oo0o - oO0o . I11O0O0oOO00O00o
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 11 - 11: Ii1I . oO0o * ooOOOoO * ii + O0OOOoOoo0
def O0ooO0Oo00o ( ) :
 if not os . path . exists ( o0 ) :
  O0O0Oooo0o ( 'Change Log 5/9/16 - v3.1.0' , 'GenieTv now clears cache on every start-up, Force close on all platforms Android included, RaysRavers added to music section, RadioNomy section added to music, Quicksilver fixed in music, WatchSeries fixed now playing from genres, Go fishing work in progress, View log file from within maintenance, Speedtest added to maintenance section, GenieTv contact information within addon, Search tweaked performing faster and more sources, Tv theme tunes section added to music, new servers online' )
  os . makedirs ( o0 )
  if 33 - 33: o0o00Oo0O * I11i - ii1ii11IIIiiI % ii1ii11IIIiiI
  if 18 - 18: ii1ii11IIIiiI / I1ii11iIi11i * ii1ii11IIIiiI + ii1ii11IIIiiI * Ii * Ii1I
def I1II1 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , OO0o , '' )
 if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def oooO ( ) :
 O000OOo00oo ( )
 i1I1i111Ii ( )
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
 if 27 - 27: O0OOOoOoo0 % oOo0O0Ooo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']Link GTV to Guide[/COLOR]' , '' , 4010 , III1iII1I1ii + 'linkchannels.png' , OO0o , '' )
def o0oooOO00 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Lists[/COLOR]' , i11 ( 'aHR0cDovL2Rvd25sb2FkLnByb2dkdmIuY29tL3R2c3QvU2x5TmV0LnR2c3Q=' ) , 9030 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Find Me A Stream[/COLOR]' , '' , 9003 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']World IPTV[/COLOR]' , '' , 9004 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']World IPTV 2[/COLOR]' , '' , 9007 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Iptv Lists[/COLOR]' , '' , 9010 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 if 32 - 32: ii1ii11IIIiiI
 if 30 - 30: iI11I1II1I1I / I11O0O0oOO00O00o . oO0o - I11i
def Iii11iI1i ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if 57 - 57: I11i
 if 51 - 51: oOo0O0Ooo . iI11I1II1I1I - Ii1I / o0o00Oo0O
 if oo00 . getSetting ( 'Watch Series' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']WATCH SERIES[/COLOR]' , '' , 10040 , III1iII1I1ii + 'WatchSeries.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , OO0o , '' )
 if 52 - 52: I11i + o0o00Oo0O + Ii1IIIi1 + I1ii11iIi11i % Ii1IIIi1
 if 75 - 75: oOo0O0Ooo . O0OOOoOoo0 . o0o00Oo0O * ii1ii11IIIiiI
 if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , OO0o , '' )
 if 4 - 4: iI1ii11iIi1i % oO0oo0o * oO0o
 I1I1II1I11 ( 'movies' , 'MAIN' )
def o0O0OOOOoOO0 ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 if oo00 . getSetting ( 'The Reaper' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'TheReaper.png' , OO0o , '' )
 if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , OO0o , '' )
 if oo00 . getSetting ( 'Redemption Streams' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']Redemption Streams[/COLOR]' , ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'RedemptionStreams.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , OO0o , '' )
 if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 1023 , III1iII1I1ii + 'ScoobyStreams.png' , OO0o , '' )
 if oo00 . getSetting ( 'HeroVision' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , '' , 1017 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'ITVStreams.png' , OO0o , '' )
 if 23 - 23: Ii
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + I11O0O0oOO00O00o * iI11I1II1I1I
def o0ooooO0o0O ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
def iiIi11iI1iii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 url = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( oo000o0000oO )
 for i11i1ii1I , o0OO0o0o00o in IIi1I11I1II :
  if '[DIR]' in i11i1ii1I :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + o0OO0o0o00o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0OO0o0o00o , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in o0OO0o0o00o :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + o0OO0o0o00o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0OO0o0o00o , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in o0OO0o0o00o :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + o0OO0o0o00o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0OO0o0o00o , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 10 - 10: Ii1IIIi1 + I1ii11iIi11i * Ii1I + iI11I1II1I1I / ii1ii11IIIiiI / Ii1I
def iI1II ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 if 69 - 69: O0OOOoOoo0 % oO0oo0o
def ii1I1IIii11 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'SearchCartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'WCO' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1IiI1 ) , 21004 , III1iII1I1ii + 'watchcartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'Cartoons' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , III1iII1I1ii + 'Cartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'Anime' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , III1iII1I1ii + 'anime.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def O0o0oO ( ) :
 O000OOo00oo ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , OO0o , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , III1iII1I1ii + 'Fitness.png' , OO0o , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']Go Fishing[/COLOR]' , str ( I1I1IiI1 ) , 8090 , III1iII1I1ii + 'GoFishing.png' , OO0o , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , III1iII1I1ii + 'GenieTVKitchen.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 38 - 38: oO0oo0o % OOooOOo + Ii1I . Ii
 if 53 - 53: Ii * Ii1IIIi1
 if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
def i1Ii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi1I11I1II = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIIi1I1IIii1II )
 for oo0OOo in IIi1I11I1II :
  oo0OOo = ( str ( oo0OOo ) )
  if os . path . exists ( xbmc . translatePath ( oo0OOo ) ) :
   i1i11I11 = ( oo0OOo ) . replace ( 'special://home/addons/' , '' )
   O0O0Oooo0o ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1i11I11 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iiiiII1I = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iiiiII1I == 0 :
    ooo00Ooo ( oo0OOo )
    Oo0o0O00 ( )
   elif iiiiII1I == 1 :
    ii1 ( oo0OOo )
  else :
   pass
   if 39 - 39: iI1ii11iIi1i / O0OOOoOoo0 . I11i % o0o00Oo0O * Ii1IIIi1 + oOo0O0Ooo
def ii1 ( addon ) :
 i1i11I11 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 77 - 77: iI1ii11iIi1i + IIiIiII11i . OOooOOo * ii1ii11IIIiiI + O00o0O00 + O00o0O00
def ooo00Ooo ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1ii1I1iiii = os . path . join ( iIi1ii1I1 , 'default.py' )
 iiI = open ( I1ii1I1iiii , "w+" )
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 iiI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iiI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iiI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 39 - 39: o0o00Oo0O + ii1ii11IIIiiI
 if 91 - 91: ii - iI11I1II1I1I + OOooOOo / oO0o . OOooOOo + o0o00Oo0O
 if 26 - 26: Ii1I - ii
 if 11 - 11: oOo0O0Ooo * oO0oo0o
 if 81 - 81: Ii1IIIi1 + ooOOOoO
 if 98 - 98: oOo0O0Ooo
 if 95 - 95: O0OOOoOoo0 / O0OOOoOoo0
 if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
 if 55 - 55: O0OOOoOoo0 - I11O0O0oOO00O00o + IIiIiII11i + Ii1IIIi1 % iI1ii11iIi1i
 if 41 - 41: ooOoO0O00 - I11O0O0oOO00O00o - iI1ii11iIi1i
 if 8 - 8: oO0o + ii1ii11IIIiiI - I11i % I1ii11iIi11i % I11i * oO0oo0o
 if 9 - 9: I1ii11iIi11i - Ii - O00o0O00 * iI1ii11iIi1i + O0OOOoOoo0
 if 44 - 44: IIiIiII11i
 if 52 - 52: Ii1I - I1ii11iIi11i + Ii1I % I11i
 if 35 - 35: iI11I1II1I1I
 if 42 - 42: ii1ii11IIIiiI . oOo0O0Ooo . ooOoO0O00 + OOooOOo + O00o0O00 + oOo0O0Ooo
 if 31 - 31: Ii1IIIi1 . O00o0O00 - O0OOOoOoo0 . ii / ii
 if 56 - 56: oO0o / oO0oo0o / Ii + ii - I1ii11iIi11i - I11O0O0oOO00O00o
 if 21 - 21: o0o00Oo0O % ooOOOoO . oOo0O0Ooo / IIiIiII11i + ooOOOoO
def OOOO0O00o ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 if 62 - 62: iI11I1II1I1I
def i1II ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOoOo = 'http://imoviemax.se/?s=' + ( iI1I ) . replace ( ' ' , '+' )
 III1I1Iii1iiI = OooOoOo . lower ( )
 i1Iii11I1i ( III1I1Iii1iiI )
def Oo00o0OO0O00o ( url ) :
 O0Oooo = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , iiIi1i in IIi1I11I1II :
  if oO00oooOOoOo0 in O0Oooo :
   pass
  else :
   I1IIII1i ( oO00oooOOoOo0 + ' - ' + iiIi1i + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
   O0Oooo . append ( oO00oooOOoOo0 )
   if 27 - 27: O00o0O00 * O0OOOoOoo0 . ii1ii11IIIiiI % ooOOOoO * ooOOOoO . ooOoO0O00
def O0OOoOOO0oO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , I1ii11 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + ' - Views:' + I1ii11 , url , 10075 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
  if 74 - 74: I1ii11iIi11i - I11i . ooOoO0O00
  if 43 - 43: Ii1IIIi1 / oOo0O0Ooo
def i1Iii11I1i ( url ) :
 OO0oo0O = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIIi1I1IIii1II )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10075 , Ii1i1iI , Ii1i1iI , '' )
  OO0oo0O . append ( oO00oooOOoOo0 )
  if 16 - 16: O00o0O00 / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % O00o0O00
def ooo0o00 ( img , name , url ) :
 img = img
 name = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIIi1I1IIii1II )
 for ooO , url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o0o00 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o0o00
  IIi = ( ooO ) . replace ( 'play-' , 'Server ' )
  iIiIIi1 ( IIi , o0o00 , 10076 , img , img , '' )
  if 66 - 66: oO0oo0o % oO0o . O00o0O00
def o0OIiiiI ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o in IIi1I11I1II :
  if '=m' in o0OO0o0o00o :
   O00OoOO0oo0 ( o0OO0o0o00o )
  elif 'php' in o0OO0o0o00o :
   o0OIiiiI ( url )
  else :
   IIIi1I1IIii1II = O0i1II1Iiii1I11 ( o0OO0o0o00o )
   IIi1I11I1II = re . compile ( 'content="([^"]*)">' ) . findall ( IIIi1I1IIii1II )
   for oOO in IIi1I11I1II :
    O00OoOO0oo0 ( o0OO0o0o00o )
    if 53 - 53: ii1ii11IIIiiI * ooOOOoO . I1ii11iIi11i - iI1ii11iIi1i % iI1ii11iIi1i * Ii
    if 7 - 7: o0o00Oo0O . iI1ii11iIi1i
    if 51 - 51: oO0o - o0o00Oo0O % oO0oo0o - IIiIiII11i
def I1II ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 Oo000ooOOO = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii11i1I11i , I11i1iIiIIIIIii in Oo000ooOOO :
  print 'there ><><><><><><><><><><><><'
  Ii11i1I11i = Ii11i1I11i
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11i1iIiIIIIIii ) )
  for oO00oooOOoOo0 , OOo0 in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + Ii11i1I11i + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + OOo0 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
 ii11I1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii11i1I11i , oO0oo in ii11I1 :
  print 'there ><><><><><><><><><><><><'
  Ii11i1I11i = Ii11i1I11i
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oO0oo ) )
  for oO00oooOOoOo0 , OOo0 in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + Ii11i1I11i + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + OOo0 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
   if 38 - 38: ii * O0OOOoOoo0 % o0o00Oo0O * OOooOOo
   if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - iI1ii11iIi1i
   if 20 - 20: ooOoO0O00 % oO0o . oOo0O0Ooo / ooOOOoO * Ii * O00o0O00
def OOo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii11I1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii11I1 in ii11I1 :
  oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11I1 ) )
  for oO00oooOOoOo0 in oO00oooOOoOo0 :
   oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11I1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i1i11I1I1iii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11I1 ) )
  for i1i11I1I1iii1 in i1i11I1I1iii1 :
   i1i11I1I1iii1 = 'http:' + i1i11I1I1iii1
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , '' , '' )
  if 8 - 8: O0OOOoOoo0 + IIiIiII11i / Ii1IIIi1 / I11O0O0oOO00O00o
  if 74 - 74: o0o00Oo0O / ooOoO0O00
  if 78 - 78: ii . oO0o + O0OOOoOoo0 - ooOoO0O00
  if 31 - 31: ii . O00o0O00
def O0iII1 ( url ) :
 if 27 - 27: oO0o . I11O0O0oOO00O00o + OOooOOo / iI11I1II1I1I % Ii1IIIi1 . O0OOOoOoo0
 IIIIi1 = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o , Ii1i1iI , oO00oooOOoOo0 , iIi11iiIiI1I in IIi1I11I1II :
  oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = O0i1II1Iiii1I11 ( o0OO0o0o00o )
  OooOoooOo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for Iiii , oooOOoooo in OooOoooOo :
   O0000OOO0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oooOOoooo ) )
   for ooo0 in O0000OOO0 :
    if oO00oooOOoOo0 in IIIIi1 :
     pass
    else :
     iIiIIi1 ( oO00oooOOoOo0 , Iiii , 8043 , Ii1i1iI , Ii1i1iI , ooo0 )
     I1I1II1I11 ( 'movies' , 'INFO' )
     IIIIi1 . append ( oO00oooOOoOo0 )
     if 78 - 78: O0OOOoOoo0
     if 53 - 53: O0OOOoOoo0 * O00o0O00 . Ii1IIIi1 / o0o00Oo0O * O0OOOoOoo0
def II11iI111i1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , Oo00OoOo , ooo0 , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10065 , Oo00OoOo , oOo0O , ooo0 )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 24 - 24: Ii - ii1ii11IIIiiI
def i11iiI1111 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOoOo = 'https://www.youtube.com/results?search_query=' + ( iI1I ) . replace ( ' ' , '+' )
 III1I1Iii1iiI = OooOoOo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( III1I1Iii1iiI )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in next :
  i1I1ii11i1Iii = 'https://www.youtube.com' + i1I1ii11i1Iii
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , i1I1ii11i1Iii , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 , oOoooo000Oo00 , oooOOoooo in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  i1i11I1I1iii1 = 'http:' + ( Ii1i1iI ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i1i11I1I1iii1
  i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
  iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , i1i11I1I1iii1 , oooOOoooo )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 , oOoooo000Oo00 in IIi1I11I1II :
   print 'im doing it'
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   i1i11I1I1iii1 = 'http:' + ( Ii1i1iI ) . replace ( 'https:' , '' )
   i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
   if '&' in i1I1ii11i1Iii :
    print ' i got here'
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    ii11I1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for ii11I1 in ii11I1 :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11I1 ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     i1I1ii11i1Iii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11I1 ) )
     for i1I1ii11i1Iii in i1I1ii11i1Iii :
      i1I1ii11i1Iii = 'https://www.youtube.com/w' + i1I1ii11i1Iii
     i1i11I1I1iii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11I1 ) )
     for i1i11I1I1iii1 in i1i11I1I1iii1 :
      i1i11I1I1iii1 = 'http:' + i1i11I1I1iii1
     iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in i1I1ii11i1Iii or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in i1I1ii11i1Iii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i1I1ii11i1Iii
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    OOoo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 in OOoo :
     if 'outube' in i1I1ii11i1Iii or 'list' in i1I1ii11i1Iii :
      pass
     elif 'atch' in i1I1ii11i1Iii :
      i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ii1i1iI , 'http:' + Ii1i1iI , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , i1i11I1I1iii1 , '' )
    if 69 - 69: I11O0O0oOO00O00o
def O00oO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for Ii1i1iI , url , oO00oooOOoOo0 , oOoooo000Oo00 , oooOOoooo in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  i1i11I1I1iii1 = 'http:' + ( Ii1i1iI ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i1i11I1I1iii1
  url = 'http://www.youtube.com' + url
  iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , i1i11I1I1iii1 , oooOOoooo )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for Ii1i1iI , url , oO00oooOOoOo0 , oOoooo000Oo00 in IIi1I11I1II :
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   i1i11I1I1iii1 = 'http:' + ( Ii1i1iI ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    ii11I1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for ii11I1 in ii11I1 :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ii11I1 ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ii11I1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i1i11I1I1iii1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ii11I1 ) )
     for i1i11I1I1iii1 in i1i11I1I1iii1 :
      i1i11I1I1iii1 = 'http:' + i1i11I1I1iii1
     iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    OOoo = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for Ii1i1iI , url , oO00oooOOoOo0 in OOoo :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + Ii1i1iI , 'http:' + Ii1i1iI , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + oOoooo000Oo00 + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 , i1i11I1I1iii1 , '' )
    if 97 - 97: ii1ii11IIIiiI - iI11I1II1I1I
    if 75 - 75: ii * ooOOOoO
def i1I1i111Ii ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  I1Iiiiiii = open ( O000oo0O )
  IIi1I11I1II = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( I1Iiiiiii ) )
  for I1IIIiI1I1ii1 , iiiI1I1iIIIi1 in IIi1I11I1II :
   if I1IIIiI1I1ii1 == 'needs replacing' or iiiI1I1iIIIi1 == 'needs replacing' :
    Iii ( )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv PRIVATE LIST[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , III1iII1I1ii + 'PrivateList.png' , OO0o , '' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv ULTIMATE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
  if 19 - 19: I11O0O0oOO00O00o % IIiIiII11i / Ii / Ii1IIIi1 - ii
def iIIii ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 Iii ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 18 - 18: Ii1IIIi1 . oOo0O0Ooo
def iiIi1IIiI ( ) :
 I1IIII1i ( 'Full List' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'PPV' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Entertainment' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Factual' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Movie Channels' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'US Movie Channels TEST' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Kids' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Music' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'UK Sports' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'International Sports' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'News UK & International' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'German' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'Arabic' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'TV Series Latest' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'VOD Latest' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 I1IIII1i ( 'VOD Bollywood' , '' , 60003 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
 if 23 - 23: iI1ii11iIi1i . O00o0O00
def i1II11II ( name ) :
 oOo00O000Oo0 = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , Ii1i1iI , I1iI1I1I1i11i , i1I1ii11i1Iii in IIi1I11I1II :
  if oOo00O000Oo0 == 'Full List' :
   i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
   iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , Ii1i1iI , Ii1i1iI , '' )
  else :
   oOo00O000Oo0 = ( oOo00O000Oo0 ) . replace ( 'World' , 'القنوات العربية' )
   if oOo00O000Oo0 in I1iI1I1I1i11i :
    i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
    print i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , Ii1i1iI , Ii1i1iI , '' )
   else :
    pass
    if 39 - 39: IIiIiII11i / ooOOOoO + iI1ii11iIi1i
def OOoO000 ( name ) :
 oOo00O000Oo0 = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , Ii1i1iI , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
  iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , Ii1i1iI , Ii1i1iI , '' )
 else :
  iIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 57 - 57: IIiIiII11i
  if 54 - 54: I1ii11iIi11i + oO0oo0o + Ii
  if 28 - 28: oO0oo0o
  if 70 - 70: ooOOOoO
  if 34 - 34: ii1ii11IIIiiI % ooOOOoO
  if 3 - 3: IIiIiII11i / O00o0O00 + ooOOOoO . O0OOOoOoo0 . oO0o
  if 83 - 83: oO0oo0o + ii
  if 22 - 22: iI1ii11iIi1i % Ii1IIIi1 * ii - I11i / iI11I1II1I1I
  if 86 - 86: ii . Ii1IIIi1 % OOooOOo / I11O0O0oOO00O00o * Ii1IIIi1 / I11i
  if 64 - 64: Ii
  if 38 - 38: ooOOOoO / oOo0O0Ooo - ooOOOoO . I11O0O0oOO00O00o
  if 69 - 69: ii + Ii1I
def O0oOo00o0 ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( o00OO00OoO ) :
  I1IIII1i ( 'Backup Genie Favourites' , i1I1ii11i1Iii , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( oO0Oo ) :
  I1IIII1i ( 'Backup Ivue Config' , oO0Oo , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( oOOoo0Oo ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oOOoo0Oo , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % oO0oo0o * oO0o
  if 38 - 38: OOooOOo / Ii1IIIi1 % I1ii11iIi11i
  if 11 - 11: Ii1IIIi1 - oO0oo0o + IIiIiII11i - iI11I1II1I1I
zip = oo00 . getSetting ( 'zip' )
I1i11ii11 = xbmc . translatePath ( os . path . join ( zip ) )
def OO00O0oOO ( ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 51 - 51: ooOOOoO * o0o00Oo0O / IIiIiII11i . iI1ii11iIi1i % O00o0O00 / oOo0O0Ooo
  if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
  if 30 - 30: ooOOOoO + ii1ii11IIIiiI - ooOOOoO . ooOOOoO - IIiIiII11i + o0o00Oo0O
def oOO0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = o00OO00OoO
  elif 'Ivue' in name :
   url = oO0Oo
  elif 'Kodi' in name :
   url = oOOoo0Oo
  OO00O0oOO ( )
  i1IIiIii1i = open ( url ) . read ( )
  ooOOO0OooOo = os . path . join ( I1i11ii11 , description . split ( 'Your ' ) [ 1 ] )
  o0Oo00 = open ( ooOOO0OooOo , mode = 'w' )
  o0Oo00 . write ( i1IIiIii1i )
  o0Oo00 . close ( )
 else :
  if 'guisettings.xml' in description :
   I1Ii = open ( os . path . join ( I1i11ii11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOIi1II = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi1I11I1II = re . compile ( oOOIi1II ) . findall ( I1Ii )
   for type , O0Oo00 , ii1IiIIi1i in IIi1I11I1II :
    ii1IiIIi1i = ii1IiIIi1i . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , O0Oo00 , ii1IiIIi1i ) )
  else :
   ooOOO0OooOo = os . path . join ( url )
   i1IIiIii1i = open ( os . path . join ( I1i11ii11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0Oo00 = open ( ooOOO0OooOo , mode = 'w' )
   o0Oo00 . write ( i1IIiIii1i )
   o0Oo00 . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 54 - 54: O0OOOoOoo0
 if 67 - 67: O00o0O00 . I1ii11iIi11i + OOooOOo - ii
 if 70 - 70: O00o0O00 / IIiIiII11i - iI11I1II1I1I - Ii1IIIi1
 if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - I11O0O0oOO00O00o
def ii1ii11 ( ) :
 OoOoo0oO = 1
 OO00O0oOO ( )
 iioo0o0OoOOO = xbmc . translatePath ( os . path . join ( I1i11ii11 , 'Build Backup' , 'Full Backup' , '' ) )
 ooO0oO00O0o = xbmc . translatePath ( os . path . join ( I1i11ii11 , 'Build Backup' , 'my_full_backup.zip' ) )
 ooOO00oOOo000 = xbmc . translatePath ( os . path . join ( I1i11ii11 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iioo0o0OoOOO ) :
  os . makedirs ( iioo0o0OoOOO )
 IIii11II11II1 = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IIii11II11II1 ) : return False , 0
 II1IOoOo000oOo0oo = IIii11II11II1
 oO0O = xbmc . translatePath ( os . path . join ( iioo0o0OoOOO , II1IOoOo000oOo0oo + '.zip' ) )
 oOOiiiIIiIi = [ 'plugin.video.GenieTv' ]
 OooOOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Ii1iI11iI1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i11I1II = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OO0 = "Creating full backup of existing build"
 OOO0oOOo00O = "Creating Community Build"
 OO0oIII111i11IiI = "Archiving..."
 O0000 = ""
 ooO00O0O0 = "Please Wait"
 iII1I1 ( I11 , oO0O , OOO0oOOo00O , OO0oIII111i11IiI , O0000 , ooO00O0O0 , Ii1iI11iI1 , i11I1II )
 time . sleep ( 1 )
 o0Ooo0o0ooo0 = xbmc . translatePath ( os . path . join ( iioo0o0OoOOO , II1IOoOo000oOo0oo + '_guisettings.zip' ) )
 oo0o0000Oo0 = zipfile . ZipFile ( o0Ooo0o0ooo0 , mode = 'w' )
 try :
  oo0o0000Oo0 . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oo0o0000Oo0 . close ( )
 if OoOoo0oO == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + ooO0oO00O0o , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oO0O + '[/COLOR]' )
  if 80 - 80: ii1ii11IIIiiI - I1ii11iIi11i
def iII1I1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OOooO = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O00O0OO00oo = len ( sourcefile )
 oOOO = [ ]
 ooo0oooo0 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for OOO0ooo , IIiiii , iI111i1I1II in os . walk ( sourcefile ) :
  for file in iI111i1I1II :
   ooo0oooo0 . append ( file )
 O00OO = len ( ooo0oooo0 )
 for OOO0ooo , IIiiii , iI111i1I1II in os . walk ( sourcefile ) :
  IIiiii [ : ] = [ II1Ii1iI1i1 for II1Ii1iI1i1 in IIiiii if II1Ii1iI1i1 not in exclude_dirs ]
  iI111i1I1II [ : ] = [ o0Oo00 for o0Oo00 in iI111i1I1II if o0Oo00 not in exclude_files ]
  for file in iI111i1I1II :
   oOOO . append ( file )
   o0OoO000O = len ( oOOO ) / float ( O00OO ) * 100
   o0oOoO00o . update ( int ( o0OoO000O ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OOoiIIiiIIIi1I = os . path . join ( OOO0ooo , file )
   if not 'temp' in IIiiii :
    if not 'plugin.program.originwizard' in IIiiii :
     import time
     OO0o0o0oo0O = '01/01/1980'
     IIiI1I1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OOoiIIiiIIIi1I ) ) )
     if IIiI1I1 > OO0o0o0oo0O :
      OOooO . write ( OOoiIIiiIIIi1I , OOoiIIiiIIIi1I [ O00O0OO00oo : ] )
 OOooO . close ( )
 o0oOoO00o . close ( )
 if 15 - 15: iI1ii11iIi1i * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 if 60 - 60: oOo0O0Ooo * ii1ii11IIIiiI % oO0o + oO0oo0o
def o0oo ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 if 80 - 80: ii1ii11IIIiiI * OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % oOo0O0Ooo
 if 13 - 13: oO0oo0o . oOo0O0Ooo * oO0oo0o + oOo0O0Ooo
def OoOooo ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'MOVIESv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'TVSHOWSv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON' , OO0o , '' )
 if 74 - 74: iI11I1II1I1I * ooOOOoO % OOooOOo
 if 36 - 36: ii - oO0oo0o
 if 85 - 85: I11i . ooOOOoO / o0o00Oo0O . I11i . Ii1I . oO0o
 if 60 - 60: I11i - OOooOOo * I1ii11iIi11i % iI1ii11iIi1i / IIiIiII11i % OOooOOo
def oO00OoOO ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , III1iII1I1ii + 'Quicksilver.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , OO0o , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , OO0o , '' )
  if 18 - 18: O0OOOoOoo0 - OOooOOo % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , OO0o , '' )
 if 91 - 91: OOooOOo + O0OOOoOoo0 . oOo0O0Ooo
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 71 - 71: Ii1IIIi1 % I11i / O00o0O00 / I1ii11iIi11i
def OO0OO0OO ( ) :
 O000OOo00oo ( )
 if 61 - 61: ii . oO0oo0o . ii / I1ii11iIi11i
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , OO0o , '' )
 iIiIIi1 ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , OO0o , 'Force Refresh All Repos' )
 if 72 - 72: ooOoO0O00
 iIiIIi1 ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , OO0o , '' )
 iIiIIi1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , OO0o , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1I1IiI1 ) , 4 , III1iII1I1ii + 'AdvancedSettingXML.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']URL FIXES[/COLOR]' , str ( I1I1IiI1 ) , 20 , III1iII1I1ii + 'URLFixes.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
 if 63 - 63: Ii1I
def i1i1II ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , III1iII1I1ii + 'repos.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']NEW[/COLOR]' , str ( I1I1IiI1 ) , 22 , III1iII1I1ii + 'NEW.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']IPTV[/COLOR]' , str ( I1I1IiI1 ) , 23 , III1iII1I1ii + 'IPTV.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']VIDEO[/COLOR]' , str ( I1I1IiI1 ) , 24 , III1iII1I1ii + 'VIDEO.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SPORTS[/COLOR]' , str ( I1I1IiI1 ) , 25 , III1iII1I1ii + 'SPORTS.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 26 , III1iII1I1ii + 'KIDS.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 27 , III1iII1I1ii + 'MUSIC.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']PROGRAMS[/COLOR]' , str ( I1I1IiI1 ) , 28 , III1iII1I1ii + 'PROGRAMS.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']XXX[/COLOR]' , 'URL' , 29 , III1iII1I1ii + 'XXX.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 6 - 6: O0OOOoOoo0 / Ii1I
 if 57 - 57: I11O0O0oOO00O00o
def oO0oO00oOo0OOO ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( 'CHECK ADVANCED XML' , str ( I1I1IiI1 ) , 8 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'MUCKYS XML' , str ( I1I1IiI1 ) + '/wizard/muckys.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( '0CACHE XML' , str ( I1I1IiI1 ) + '/wizard/0cache.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'MIKEY1234 XML' , str ( I1I1IiI1 ) + '/wizard/mikey.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'TUXENS XML' , str ( I1I1IiI1 ) + '/wizard/tuxens.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'P2P RECOMMENDED XML1' , str ( I1I1IiI1 ) + '/wizard/p2p1.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'P2P RECOMMENDED XML2' , str ( I1I1IiI1 ) + '/wizard/p2p2.xml' , 7 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE XML' , str ( I1I1IiI1 ) , 11 , III1iII1I1ii + 'XML.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 23 - 23: ooOoO0O00 . I11i * oO0o
def iIi1IiI ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , III1iII1I1ii + 'MyOnlineZip.png' , OO0o , '' )
 if 14 - 14: ooOOOoO % oO0oo0o % I1ii11iIi11i - Ii
def o0OO000ooOo ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , OO0o , '' )
 iIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , OO0o , '' )
 if 86 - 86: oO0o * ii
 if 71 - 71: iI11I1II1I1I - O00o0O00 . oOo0O0Ooo % ii + O00o0O00
 if 26 - 26: I1ii11iIi11i + O00o0O00 / oO0o % OOooOOo % Ii1I + IIiIiII11i
def i11I1I1iiI ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , str ( I1I1IiI1 ) , 33 , III1iII1I1ii + 'Skins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , str ( I1I1IiI1 ) , 34 , III1iII1I1ii + 'ArtworkPacks.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' , I11 , 35 , III1iII1I1ii + 'CreateUniversalPath.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 34 - 34: I11O0O0oOO00O00o % O0OOOoOoo0 . o0o00Oo0O . iI11I1II1I1I
def ooi1II1I ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi1I11I1II = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( OOO00O )
 for Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , Ii1i1iI , Ii1i1iI , '' )
 I1I1II1I11 ( 'tvshows' , 'INFO' )
 if 95 - 95: oO0o - O00o0O00 / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( oo0OoOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 95 - 95: ooOOOoO * Ii1I % O0OOOoOoo0 % iI1ii11iIi1i - iI1ii11iIi1i
def oOoooO0 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 68 - 68: O0OOOoOoo0 / I11i
def Ii11 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + II1i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 50 - 50: ooOOOoO % ooOoO0O00
def iii11II1I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI111I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 23 - 23: iI1ii11iIi1i . I11i + I1ii11iIi11i - O00o0O00
def II1iiIiIiI ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIIi1I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 14 - 14: o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 40 - 40: Ii1IIIi1 . oO0oo0o + oOo0O0Ooo + Ii1I + ii1ii11IIIiiI
def i11Ii1I1I11I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 40 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 34 - 34: Ii1IIIi1 - ii . oOo0O0Ooo / IIiIiII11i
def II1II ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 95 - 95: ii . o0o00Oo0O . I11i * I1ii11iIi11i . iI1ii11iIi1i
def iI1 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '' , 80002 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , str ( I1I1IiI1 ) , 2 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' , str ( I1I1IiI1 ) , 30038 , III1iII1I1ii + 'APKSearch.png' , OO0o , '' )
 if 31 - 31: oO0oo0o / iI11I1II1I1I
def o0oO0OoO0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oOOOOOoOO in IIi1I11I1II :
  oOo0 ( 'Android Apps' + oOOOOOoOO , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'apps.png' )
 for i1I1ii11i1Iii , oOOOOOoOO in OooOoooOo :
  oOo0 ( 'Android Games' + oOOOOOoOO , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def oooo00 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/cat' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def i1oO ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/app' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , III1iII1I1ii + 'APK.png' )
def iIIi1IIi ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'href="([^"]*)" style="float:right;">next &gt;</a>' ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if 'apk' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + Ii1i1iI )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , o0OO0o0o00o + url , 30037 , III1iII1I1ii + 'Next.png' )
def i111i11I1ii ( name , url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 name = name
 IIi1I11I1II = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  url = 'https://www.apkfiles.com' + url
  OOooooo0 ( name , url )
def oOOII1i11i1iIi11 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOoOo = 'https://www.apkfiles.com/search?q=' + ( iI1I ) . replace ( ' ' , '+' ) + '&search_type=1'
 III1I1Iii1iiI = OooOoOo . lower ( )
 iIIi1IIi ( III1I1Iii1iiI )
 if 83 - 83: iI1ii11iIi1i
def I1iI1I1 ( url ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( IiIi1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo00ooOoo = os . path . join ( Ii1iI111 , oO00oooOOoOo0 + '.apk' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 28 - 28: iI1ii11iIi1i
def iIIIiiiI11I ( url ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo00ooOoo = os . path . join ( Ii1iI111 , oO00oooOOoOo0 + '.mp4' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 6 - 6: iI1ii11iIi1i % ooOoO0O00 . iI1ii11iIi1i * iI1ii11iIi1i
 if 81 - 81: O00o0O00 / iI11I1II1I1I + ooOOOoO
def i1iiI ( name , url , description ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oo00ooOoo = os . path . join ( Ii1iI111 , name )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 o0OooooOoOO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0OooooOoOO
 print '======================================='
 extract . all ( oo00ooOoo , o0OooooOoOO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 19 - 19: ooOOOoO
 if 78 - 78: O00o0O00 % I11i
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
 if 7 - 7: ooOOOoO . OOooOOo / Ii1I . O00o0O00 * I11O0O0oOO00O00o - IIiIiII11i
 if 37 - 37: ii1ii11IIIiiI . OOooOOo / o0o00Oo0O * Ii1IIIi1
def III11iiii11i1 ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1I11I1II = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOoOooooOOo , oOo0O , ooOo0OoO in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 80003 , OoOOoOooooOOo , III1iII1I1ii + 'APKToolsB.png' , ooOo0OoO )
def i1iiIIi1I ( apk , ret = None ) :
 if apk == "kodi" :
  iiI1I1IIi11i1 = "https://kodi.tv/download/"
  OOO00O = O0i1II1Iiii1I11 ( iiI1I1IIi11i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( OOO00O )
  if len ( IIi1I11I1II ) == 1 :
   i1II1iii1i = IIi1I11I1II [ 0 ] [ 0 ]
   II1IOoOo000oOo0oo = IIi1I11I1II [ 0 ] [ 1 ]
   OOO0o = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( i1II1iii1i , II1IOoOo000oOo0oo )
  if ret == 'version' : return i1II1iii1i
  else : return OOO0o
 elif apk == "spmc" :
  iII = 'https://github.com/koying/SPMC/releases/latest/'
  OOO00O = O0i1II1Iiii1I11 ( iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( OOO00O )
  i1II1iii1i = re . sub ( '<[^<]+?>' , '' , IIi1I11I1II [ 0 ] ) . replace ( ' ' , '' )
  OOO0o = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( i1II1iii1i , i1II1iii1i )
  if ret == 'version' : return i1II1iii1i
  else : return OOO0o
def OOooooo0 ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  II1 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not II1 : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I1I11i = name
  if II1 :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not oooooo0O000o ( url ) == True : Oo00O0Oo0Oo ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1I11i , '' , 'Please Wait' )
   oo00ooOoo = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( oo00ooOoo )
   except : pass
   downloader . download ( url , oo00ooOoo , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oo00ooOoo + '")' )
  else : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 66 - 66: iI1ii11iIi1i . oOo0O0Ooo + I11i . iI11I1II1I1I
 if 51 - 51: I11O0O0oOO00O00o . I1ii11iIi11i
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i / o0o00Oo0O . Ii1I
 if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
def I1IiiiiI ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( OOO00O )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  i1I1ii11i1Iii = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + i1I1ii11i1Iii )
  ooO0oo0o0 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , i1I1ii11i1Iii )
  if 9 - 9: oOo0O0Ooo + Ii1I / oOo0O0Ooo . oO0oo0o * O0OOOoOoo0
def ooO0oo0o0 ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  II1 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not II1 : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1I11i = name
  if II1 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not oooooo0O000o ( url ) == True : Oo00O0Oo0Oo ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1I11i , '' , 'Please Wait' )
   oo00ooOoo = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oo00ooOoo )
   except : pass
   downloader . download ( url , oo00ooOoo , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oo00ooOoo + '")' )
  else : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Oo00O0Oo0Oo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 45 - 45: Ii
 if 82 - 82: iI1ii11iIi1i + ooOOOoO
def i111i1iIiiIiI ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 26 - 26: iI11I1II1I1I % Ii % Ii1I
 if 67 - 67: ii
def IiIiIi1I1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 30015 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 2 - 2: ooOoO0O00 - O0OOOoOoo0 + oOo0O0Ooo . I11i * I11i / OOooOOo
def oOOOiIi1I1 ( url , iconimage , fanart ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 o0o00 = url
 Ii1i1iI = iconimage
 fanart = fanart
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for o0OO0o0o00o , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp4' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Watch VIDEO' , url + '/' + o0OO0o0o00o , 222 , Ii1i1iI , fanart , '' )
  if 'description' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Read Description' , url + '/' + o0OO0o0o00o , 30017 , Ii1i1iI , fanart , '' )
  if 'images' in oO00oooOOoOo0 :
   I1IIII1i ( 'View Images' , url + '/' + o0OO0o0o00o , 30018 , Ii1i1iI , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Android' , url + '/' + o0OO0o0o00o , 30016 , Ii1i1iI , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Pc' , url + '/' + o0OO0o0o00o , 30019 , Ii1i1iI , fanart , '' )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 63 - 63: Ii1IIIi1 * Ii1I . ii / O00o0O00 * I1ii11iIi11i . O0OOOoOoo0
def Ooo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  oooO00o0 ( url )
  if 53 - 53: O0OOOoOoo0
def o0oO0oo0000OO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  I1i1ii1IiIii ( url )
  if 69 - 69: OOooOOo % oO0oo0o - I11O0O0oOO00O00o
def Iiii1ii ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'desc="([^"]*)"' ) . findall ( OOO00O )
 for I1i111IiIiIi1 in IIi1I11I1II :
  O0O0Oooo0o ( 'Description:' , I1i111IiIiIi1 )
  if 39 - 39: I11O0O0oOO00O00o - Ii1I
def OOO0o0OO0OO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 url = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for o0OO0o0o00o , oO00oooOOoOo0 in IIi1I11I1II :
  if 'png' in oO00oooOOoOo0 :
   iIiIIi1 ( 'image' , '' , '' , url + '/' + o0OO0o0o00o , url + '/' + o0OO0o0o00o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 64 - 64: IIiIiII11i
def iIIIiIi1I1i ( name , url , description ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo00ooOoo = os . path . join ( Ii1iI111 , name + '.zip' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOoO0oOo
 print '======================================='
 extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Oo0o0O00 ( )
 if 70 - 70: I11O0O0oOO00O00o % iI11I1II1I1I . I1ii11iIi11i + I1ii11iIi11i - I11i % ii1ii11IIIiiI
 if 38 - 38: ii1ii11IIIiiI % O00o0O00 - ii
def I1i1ii1IiIii ( url ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo00ooOoo = os . path . join ( Ii1iI111 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOoO0oOo
 print '======================================='
 extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
 oOo0OOoooO ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1iIIIiIiI ( )
 if 62 - 62: Ii % O00o0O00 . ooOOOoO . O00o0O00
def oooO00o0 ( url ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo00ooOoo = os . path . join ( Ii1iI111 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOoO0oOo
 print '======================================='
 extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
 oOo0OOoooO ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1iIIIiIiI ( )
 if 84 - 84: Ii * oO0o
def I1I1iII1i ( name , url , description ) :
 OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oo00ooOoo = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OoOOoO0oOo
 print '======================================='
 extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1iIIIiIiI ( )
 if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
def I1I1i1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def oo00oOO000oO0 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oo0o0O00 , log ) )
 if not os . path . exists ( oOo0oooo00o ) : os . makedirs ( oOo0oooo00o )
 if not os . path . exists ( oO0o0o0ooO0oO ) : o0Oo00 = open ( oO0o0o0ooO0oO , 'w' ) ; o0Oo00 . close ( )
 with open ( oO0o0o0ooO0oO , 'a' ) as o0Oo00 :
  III1I = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  o0Oo00 . write ( III1I . rstrip ( '\r\n' ) + '\n' )
def iIi1iIIIiIiI ( ) :
 iiiiII1I = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiiiII1I == 0 : return
 elif iiiiII1I == 1 : pass
 I1I111iIi = I1I1i1I ( )
 oo00oOO000oO0 ( "Platform: " + str ( I1I111iIi ) )
 os . _exit ( 1 )
 oo00oOO000oO0 ( "Force close failed!  Trying alternate methods." )
 if I1I111iIi == 'osx' :
  oo00oOO000oO0 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1I111iIi == 'linux' :
  oo00oOO000oO0 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1I111iIi == 'android' :
  oo00oOO000oO0 ( "############ try android force close #################" )
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
 elif I1I111iIi == 'windows' :
  oo00oOO000oO0 ( "############ try windows force close #################" )
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
  oo00oOO000oO0 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oo00oOO000oO0 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 53 - 53: iI11I1II1I1I + I11i - OOooOOo - oO0oo0o / O0OOOoOoo0 % Ii
  if 3 - 3: Ii1IIIi1 . O0OOOoOoo0 % oOo0O0Ooo + Ii1I
  if 64 - 64: ooOoO0O00
def IIii1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( url ) :
  for file in iI111i1I1II :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    I1Ii = open ( ( os . path . join ( IiiiI111I , file ) ) ) . read ( )
    III1I11i1iIi = I1Ii . replace ( I11 , 'special://home/' )
    o0Oo00 = open ( ( os . path . join ( IiiiI111I , file ) ) , mode = 'w' )
    o0Oo00 . write ( str ( III1I11i1iIi ) )
    o0Oo00 . close ( )
 iIi1iIIIiIiI ( )
 if 69 - 69: I1ii11iIi11i * IIiIiII11i * O0OOOoOoo0 . Ii1IIIi1 - Ii1I
def I11iiIIiI1ii ( ) :
 oOo0 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 12 - 12: ii1ii11IIIiiI % Ii + I11i + ii1ii11IIIiiI / I11O0O0oOO00O00o
def O00 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def O0OO0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def OOoOOo0o ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , Ii1i1iI )
def iIiii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  IiIii1ii ( url )
def IIiI1i ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I
 iII1 = 'https://www.radionomy.com/en/search/index?query=' + ( iI1I ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( iII1 )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + i1I1ii11i1Iii , 70005 , Ii1i1iI )
  if 70 - 70: Ii1IIIi1 / O00o0O00 % O0OOOoOoo0 - iI1ii11iIi1i
  if 47 - 47: Ii1IIIi1
def o00Ooo0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , 'http://www.listenlive.eu/' + i1I1ii11i1Iii , 10111113 , III1iII1I1ii + 'radio.png' )
def O0O00O ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'radio.png' )
  if 4 - 4: OOooOOo + iI1ii11iIi1i / oO0oo0o
def i1iI1IIIII1 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + i1I1ii11i1Iii , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1I1IiIi1I ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( oo000o0000oO )
 for url , Ii1i1iI in IIi1I11I1II :
  if 'ol.gif' in Ii1i1iI :
   pass
  elif 'link_block_' in Ii1i1iI :
   pass
  elif '.png' in Ii1i1iI :
   pass
  else :
   oOo0 ( ( Ii1i1iI ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in OooOoooOo :
  oOo0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1i1ii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 82 - 82: OOooOOo + o0o00Oo0O - ooOOOoO % oO0oo0o * Ii
  if 15 - 15: I11i
def I1iI ( ) :
 oO0Ooo0OooOOo ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 oO0Ooo0OooOOo ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 71 - 71: ooOOOoO + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( ) :
 oO0Ooo0OooOOo ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oO0Ooo0OooOOo ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 oO0Ooo0OooOOo ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 68 - 68: o0o00Oo0O
def II1iIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOOOo in IIi1I11I1II :
  if 'Parent' in oO00oooOOoOo0 :
   pass
  elif '2' in OoOOOOo :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 61 - 61: ooOoO0O00 * oO0o - I1ii11iIi11i - O0OOOoOoo0
def OO0I11Ii1iI11iI1 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOOOo in IIi1I11I1II :
  if iI1I in oO00oooOOoOo0 . lower ( ) :
   if '1' in OoOOOOo :
    oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in OoOOOOo :
    oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in OoOOOOo :
    oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 32 - 32: oOo0O0Ooo
    if 78 - 78: OOooOOo - oO0o % O0OOOoOoo0
def o0OoOoo00O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOOOo in IIi1I11I1II :
  if '1' in OoOOOOo :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in OoOOOOo :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in OoOOOOo :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 29 - 29: I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: IIiIiII11i . ooOOOoO
def iIiI ( url ) :
 o0OO0o0o00o = url
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in OooOoooOo :
  if 'mp3' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0OO0o0o00o + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0OO0o0o00o + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0OO0o0o00o + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in oO00oooOOoOo0 :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 81 - 81: OOooOOo % iI1ii11iIi1i
   if 87 - 87: iI11I1II1I1I . ii * OOooOOo
   if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % iI1ii11iIi1i - iI11I1II1I1I
def i11II ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 o0OO0o0o00o = url
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Parent' in oO00oooOOoOo0 :
   pass
  elif '.db' in oO00oooOOoOo0 :
   pass
  elif '.jpg' in oO00oooOOoOo0 :
   pass
  elif '.html' in oO00oooOOoOo0 :
   pass
  elif '.doc' in oO00oooOOoOo0 :
   pass
  elif 'mp3' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 71 - 71: ooOOOoO . ii1ii11IIIiiI . oO0o
   if 68 - 68: Ii % oO0oo0o * oO0o * ooOOOoO * IIiIiII11i + o0o00Oo0O
def o00OoO0oO00 ( ) :
 oO0Ooo0OooOOo ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oO0Ooo0OooOOo ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oO0Ooo0OooOOo ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 2 - 2: iI11I1II1I1I
def iiii1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI in IIi1I11I1II :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in Ii1i1iI :
   pass
  else :
   oO0Ooo0OooOOo ( Ii1i1iI , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i1I1ii11i1Iii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + Ii1i1iI + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 66 - 66: oO0oo0o * iI11I1II1I1I % iI11I1II1I1I * ooOOOoO - O0OOOoOoo0 - ooOOOoO
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: ii1ii11IIIiiI + oO0oo0o
 if 93 - 93: ii1ii11IIIiiI + iI1ii11iIi1i
def i1i1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 27 - 27: ii1ii11IIIiiI + ii - OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: oO0oo0o / I11O0O0oOO00O00o * o0o00Oo0O . IIiIiII11i - oO0o
def o0Oo00OO0 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if iI1I in oO00oooOOoOo0 . lower ( ) :
   if '</a>' in oO00oooOOoOo0 :
    pass
   elif '(' in oO00oooOOoOo0 :
    oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 50 - 50: iI1ii11iIi1i * I11i % Ii
    if 96 - 96: Ii1I + I1ii11iIi11i * oO0o % O0OOOoOoo0 - o0o00Oo0O
def OO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   oO0Ooo0OooOOo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 77 - 77: Ii / ii + ooOOOoO % oO0oo0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: oO0oo0o
 if 74 - 74: ii
def OoOoO0O ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  o0OO0o0o00o = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( o0OO0o0o00o )
  if 100 - 100: o0o00Oo0O
def o00IiI1iiII1i1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '<p align' in oO00oooOOoOo0 :
   pass
  elif '&nbsp;' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 18 - 18: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: Ii1I / iI11I1II1I1I % OOooOOo
 if 80 - 80: oO0o % Ii1IIIi1
def O0Oo0 ( ) :
 IIIi1I1IIii1II = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi1I11I1II = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'ongoing' in i1I1ii11i1Iii :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in i1I1ii11i1Iii :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in i1I1ii11i1Iii :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in i1I1ii11i1Iii :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in i1I1ii11i1Iii :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def OOooO0OO0 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 iI1iIiiiI1I1 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , Ii1i1iI , Ii1i1iI , oO00oooOOoOo0 )
 for url , oO00oooOOoOo0 in iI1iIiiiI1I1 :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def OOOOOo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 I1IiiiIiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 O0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIIi1I1IIii1II )
 I1Ii1iIiII = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in O0Oo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , oO00oooOOoOo0 in I1IiiiIiI :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def O0oOo00Ooo0o0 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 33 - 33: I11O0O0oOO00O00o
def oOO0IIi1I1i ( ) :
 oOo0 ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 13 - 13: iI11I1II1I1I . OOooOOo * oOo0O0Ooo / oO0oo0o * iI1ii11iIi1i
def O00o ( ) :
 oOo0 ( '[COLOR' + iiI1IiI + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 86 - 86: Ii1I * IIiIiII11i * I11O0O0oOO00O00o
def oO0OoooO0oOO00OoOo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '?c=' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + ooOOOoO % Ii % OOooOOo
def O0OOO0 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , ooOo0OoO , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Genre' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 8 - 8: Ii / IIiIiII11i + I11i * iI1ii11iIi1i % ooOOOoO . I11O0O0oOO00O00o
def I1iIIIiIi1 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , ooOo0OoO , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , ooOo0OoO )
  if 21 - 21: iI11I1II1I1I / ii1ii11IIIiiI + O0OOOoOoo0 - I11O0O0oOO00O00o / I1ii11iIi11i / IIiIiII11i
def oOI11 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , ooOo0OoO , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , ooOo0OoO )
  if 54 - 54: iI1ii11iIi1i - ii1ii11IIIiiI
  if 81 - 81: ooOOOoO . o0o00Oo0O + IIiIiII11i * iI11I1II1I1I * O00o0O00 / OOooOOo
  if 88 - 88: IIiIiII11i - I11i * oOo0O0Ooo . oO0o
  if 65 - 65: ooOOOoO . ooOoO0O00
  if 95 - 95: oOo0O0Ooo + oOo0O0Ooo - O00o0O00 - Ii1IIIi1
def i1i ( ) :
 if 27 - 27: iI1ii11iIi1i * I1ii11iIi11i . OOooOOo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 if 17 - 17: IIiIiII11i % Ii1IIIi1 * O00o0O00 % ooOoO0O00 . oOo0O0Ooo . iI11I1II1I1I
def iiiIIIii ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 93 - 93: iI11I1II1I1I + oOo0O0Ooo + Ii
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIIi1I1IIii1II )
 if 74 - 74: I11O0O0oOO00O00o / IIiIiII11i + O0OOOoOoo0 * iI11I1II1I1I - ii1ii11IIIiiI - oO0o
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if iI1I in oO00oooOOoOo0 . lower ( ) :
   if 'Dad!' in oO00oooOOoOo0 :
    pass
   elif 'Family Guy' in oO00oooOOoOo0 :
    pass
   elif '2 Stupid' in oO00oooOOoOo0 :
    pass
   elif 'The Zelfs' in oO00oooOOoOo0 :
    pass
   elif 'A Clone' in oO00oooOOoOo0 :
    pass
   elif 'A.T.O.M' in oO00oooOOoOo0 :
    pass
   elif 'Almost Naked' in oO00oooOOoOo0 :
    pass
   elif 'Angry Kid' in oO00oooOOoOo0 :
    pass
   elif 'Annoying Orange' in oO00oooOOoOo0 :
    pass
   elif 'Aqua Teen' in oO00oooOOoOo0 :
    pass
   elif 'Assy Mcgee' in oO00oooOOoOo0 :
    pass
   elif 'Astroblast' in oO00oooOOoOo0 :
    pass
   elif 'Atomic Betty' in oO00oooOOoOo0 :
    pass
   elif 'Axe Cop' in oO00oooOOoOo0 :
    pass
   elif 'Baby Playpen' in oO00oooOOoOo0 :
    pass
   elif 'Beavis and Butt' in oO00oooOOoOo0 :
    pass
   elif 'Celebrity Deathmatch' in oO00oooOOoOo0 :
    pass
   elif 'Clerks The' in oO00oooOOoOo0 :
    pass
   elif 'Crapston Villas' in oO00oooOOoOo0 :
    pass
   elif 'Duckman:' in oO00oooOOoOo0 :
    pass
   elif 'Stripperella' in oO00oooOOoOo0 :
    pass
   elif 'Vixen' in oO00oooOOoOo0 :
    pass
   else :
    I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
    if 69 - 69: iI11I1II1I1I * oOo0O0Ooo - Ii1IIIi1 + o0o00Oo0O + o0o00Oo0O
    if 65 - 65: ii1ii11IIIiiI / Ii / oO0o - O00o0O00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: oOo0O0Ooo / ii1ii11IIIiiI - I1ii11iIi11i * iI11I1II1I1I
def ooO00o ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Dad!' in oO00oooOOoOo0 :
   pass
  elif 'Family Guy' in oO00oooOOoOo0 :
   pass
  elif '2 Stupid' in oO00oooOOoOo0 :
   pass
  elif 'The Zelfs' in oO00oooOOoOo0 :
   pass
  elif 'A Clone' in oO00oooOOoOo0 :
   pass
  elif 'A.T.O.M' in oO00oooOOoOo0 :
   pass
  elif 'Almost Naked' in oO00oooOOoOo0 :
   pass
  elif 'Angry Kid' in oO00oooOOoOo0 :
   pass
  elif 'Annoying Orange' in oO00oooOOoOo0 :
   pass
  elif 'Aqua Teen' in oO00oooOOoOo0 :
   pass
  elif 'Assy Mcgee' in oO00oooOOoOo0 :
   pass
  elif 'Astroblast' in oO00oooOOoOo0 :
   pass
  elif 'Atomic Betty' in oO00oooOOoOo0 :
   pass
  elif 'Axe Cop' in oO00oooOOoOo0 :
   pass
  elif 'Baby Playpen' in oO00oooOOoOo0 :
   pass
  elif 'Beavis and Butt' in oO00oooOOoOo0 :
   pass
  elif 'Celebrity Deathmatch' in oO00oooOOoOo0 :
   pass
  elif 'Clerks The' in oO00oooOOoOo0 :
   pass
  elif 'Crapston Villas' in oO00oooOOoOo0 :
   pass
  elif 'Duckman:' in oO00oooOOoOo0 :
   pass
  elif 'Stripperella' in oO00oooOOoOo0 :
   pass
  elif 'Vixen' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: Ii1IIIi1 * Ii1IIIi1 / O0OOOoOoo0
def IIii1i11iI1II11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oo000o0000oO )
 for Ii1i1iI in OooOoooOo :
  iIi11i = Ii1i1iI
 ooIII1II1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oo000o0000oO )
 for url in ooIII1II1iii1i :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10007 , iIi11i )
  if 75 - 75: ooOOOoO - OOooOOo - iI11I1II1I1I % I11i
  if 58 - 58: o0o00Oo0O . ooOOOoO / ii . oO0o / I1ii11iIi11i * IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: iI1ii11iIi1i - o0o00Oo0O / I11i % Ii1IIIi1 * oOo0O0Ooo % O00o0O00
def o0oOOOO0 ( url , IMAGE ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   ii1I ( url )
   if 84 - 84: Ii1I - iI11I1II1I1I % o0o00Oo0O + Ii1IIIi1
   if 93 - 93: I1ii11iIi11i / ooOOOoO % Ii1I
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: Ii % ooOoO0O00 % ooOOOoO
def ii1I ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  IiIii1ii ( url )
  if 15 - 15: iI11I1II1I1I . o0o00Oo0O
  if 70 - 70: iI1ii11iIi1i . Ii % iI1ii11iIi1i . o0o00Oo0O - iI11I1II1I1I
  if 26 - 26: O00o0O00
def Oo0oOo000OoO0 ( ) :
 if 25 - 25: Ii1I . ooOoO0O00 . IIiIiII11i / ii1ii11IIIiiI
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , OO0o , '' )
 if 54 - 54: ooOoO0O00 . I11O0O0oOO00O00o - Ii1I + O0OOOoOoo0 + I1ii11iIi11i / I1ii11iIi11i
def i1ii1IiiiiIi1I ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if 'elete' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 222 , Ii1i1iI )
   if 56 - 56: ii * o0o00Oo0O
def oo0OoOOooO ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0o0OO0o00o0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , IIIIIIi1i , i1iII1IiiIiI1 in o0o0OO0o00o0O :
  for iI1I in IIIIIIi1i :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiiii11I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for i1I1ii11i1Iii , oO00oooOOoOo0 in iiiii11I1 :
    if 'tube' in i1I1ii11i1Iii :
     pass
    elif 'stage' in i1I1ii11i1Iii :
     OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIIIIIi1i + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ii1i1iI , )
    elif 'vee' in i1I1ii11i1Iii :
     pass
     if 16 - 16: o0o00Oo0O . iI1ii11iIi1i % ooOoO0O00 % O00o0O00
def i1I1iIoOOoO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0o0OO0o00o0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , IIIIIIi1i , i1iII1IiiIiI1 in o0o0OO0o00o0O :
  iiiii11I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in iiiii11I1 :
   if 'tube' in i1I1ii11i1Iii :
    pass
   elif 'stage' in i1I1ii11i1Iii :
    OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIIIIIi1i + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + Ii1i1iI )
   elif 'vee' in i1I1ii11i1Iii :
    pass
    if 87 - 87: OOooOOo % iI11I1II1I1I
    if 72 - 72: O00o0O00 . O00o0O00 - Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: I1ii11iIi11i - O0OOOoOoo0 + I1ii11iIi11i - oOo0O0Ooo * Ii . Ii1IIIi1
def I1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 Iiii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIIi1I1IIii1II )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( Iiii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in Iiii :
  IiIii1ii ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 35 - 35: oOo0O0Ooo
  if 36 - 36: ooOoO0O00 - Ii1I - ii1ii11IIIiiI
  if 7 - 7: Ii + oOo0O0Ooo
  if 47 - 47: ii1ii11IIIiiI - O00o0O00 / O0OOOoOoo0 - I1ii11iIi11i + Ii1IIIi1 - iI11I1II1I1I
  if 68 - 68: iI1ii11iIi1i - oO0oo0o + I1ii11iIi11i
  if 44 - 44: iI1ii11iIi1i * I11i * IIiIiII11i
  if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + OOooOOo % ooOoO0O00
def O0OOo ( ) :
 if 41 - 41: iI1ii11iIi1i + Ii / ooOOOoO % Ii1I
 II1II1IIII ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 II1II1IIII ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 37 - 37: ii
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 69 - 69: oOo0O0Ooo + Ii1IIIi1
def i1IiII ( ) :
 II1II1IIII ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 II1II1IIII ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 12 - 12: Ii1IIIi1 / OOooOOo
 I1I1II1I11 ( 'movies' , 'MAIN' )
def ooooo0Oo0 ( ) :
 if 97 - 97: ooOOOoO . oO0oo0o . ooOOOoO
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 oOo00o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 12 - 12: I11i * ii1ii11IIIiiI % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
 for oO0oOoo0O in oOo00o :
  II1iI11 = I11i1I1I + oO0oOoo0O + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( II1iI11 )
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    O00o0O ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , Oo00OoOo , oOo0O , ooo0 )
    if 85 - 85: O00o0O00 * ooOoO0O00 % oOo0O0Ooo - O0OOOoOoo0
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 37 - 37: ooOOOoO . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
    if 83 - 83: ooOOOoO / ii1ii11IIIiiI
def OOo000OO000 ( ) :
 if 83 - 83: I11i % oO0oo0o + I11O0O0oOO00O00o % Ii + o0o00Oo0O
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 oOo00o = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 65 - 65: iI11I1II1I1I % oO0oo0o + o0o00Oo0O / ii
 for oO0oOoo0O in oOo00o :
  O0000oO0o00 = I11i1I1I + oO0oOoo0O + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( O0000oO0o00 )
  IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , ooo0 , i1I1ii11i1Iii , Ii1i1iI , oOo0O , oo000o in IIi1I11I1II :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    II1II1IIII ( oO00oooOOoOo0 , i1I1ii11i1Iii , oo000o , Ii1i1iI , oOo0O , ooo0 )
    if 95 - 95: oO0oo0o - O0OOOoOoo0 * I11O0O0oOO00O00o / oO0o / IIiIiII11i + o0o00Oo0O
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 37 - 37: I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00 + I11O0O0oOO00O00o . ooOOOoO / iI1ii11iIi1i
    if 29 - 29: ooOOOoO . O0OOOoOoo0 - IIiIiII11i
def ooooO0 ( ) :
 if 37 - 37: Ii + oOo0O0Ooo . O00o0O00 % I11O0O0oOO00O00o % I11O0O0oOO00O00o
 oo000o0000oO = O0i1II1Iiii1I11 ( I11i1I1I + 'spongemain.php' )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , ooo0 , i1I1ii11i1Iii , Ii1i1iI , oOo0O , oo000o in IIi1I11I1II :
  II1II1IIII ( oO00oooOOoOo0 , i1I1ii11i1Iii , oo000o , Ii1i1iI , oOo0O , ooo0 )
  I1I1II1I11 ( 'movies' , 'MAIN' )
def iiI11I1iiIiII1I ( url ) :
 if 59 - 59: ii1ii11IIIiiI - ooOOOoO
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiiii111 = ( '%s%s' % ( oO0oo0o00o0O , url ) )
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in IIi1I11I1II :
  I11iI1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
  for Iii1iiIi1II1 in I11iI1I :
   if Iii1iiIi1II1 == url :
    oO00oooOOoOo0 = ( '[COLORred]Watched - [/COLOR]' + oO00oooOOoOo0 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  O00o0O ( oO00oooOOoOo0 , url , 222 , Oo00OoOo , ooo , ooo0 )
  if 53 - 53: o0o00Oo0O + O00o0O00 % Ii * O00o0O00
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 69 - 69: O0OOOoOoo0 - ii * o0o00Oo0O
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: O0OOOoOoo0 + Ii - O00o0O00 * O0OOOoOoo0
  if 33 - 33: O0OOOoOoo0 % ooOoO0O00 - oO0oo0o . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( url ) :
 if 17 - 17: iI1ii11iIi1i / iI11I1II1I1I - oO0o + oOo0O0Ooo % O00o0O00
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , ooo0 , url , Ii1i1iI , oOo0O , oo000o in IIi1I11I1II :
  II1II1IIII ( oO00oooOOoOo0 , url , oo000o , Ii1i1iI , oOo0O , ooo0 )
  if 14 - 14: I11i % ooOOOoO + Ii1I + oO0o
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 76 - 76: oO0o - Ii + OOooOOo + O00o0O00 / ii
  if 50 - 50: IIiIiII11i - ii1ii11IIIiiI + iI11I1II1I1I + iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
def O00o0O ( name , url , mode , iconimage , fanart , description ) :
 if 26 - 26: I11i
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOoooO000OO . setProperty ( "Fanart_Image" , fanart )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = False )
 return oO0Oo00oo
 if 62 - 62: O00o0O00 + I1ii11iIi11i % iI11I1II1I1I / iI11I1II1I1I . O0OOOoOoo0 . ooOOOoO
def II1II1IIII ( name , url , mode , iconimage , fanart , description ) :
 if 21 - 21: oO0o - iI1ii11iIi1i - oOo0O0Ooo / OOooOOo
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOoooO000OO . setProperty ( "Fanart_Image" , fanart )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = True )
 return oO0Oo00oo
if 48 - 48: ii
if 16 - 16: OOooOOo * Ii1I * Ii1I / o0o00Oo0O * Ii
if 64 - 64: Ii1IIIi1 * Ii1I % IIiIiII11i - OOooOOo + Ii1I
if 62 - 62: OOooOOo % I11i % oOo0O0Ooo + ooOOOoO . oO0o
if 48 - 48: oOo0O0Ooo * Ii % IIiIiII11i
if 20 - 20: ooOoO0O00 / oOo0O0Ooo * oO0oo0o
if 85 - 85: IIiIiII11i . O0OOOoOoo0 % O00o0O00 % I11O0O0oOO00O00o
if 80 - 80: oO0oo0o * I11O0O0oOO00O00o / iI11I1II1I1I % oO0oo0o / iI11I1II1I1I
if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * Ii1IIIi1 . Ii * o0o00Oo0O
if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + ooOOOoO
if 27 - 27: O00o0O00
if 52 - 52: ii1ii11IIIiiI % OOooOOo + iI11I1II1I1I * oO0oo0o . iI1ii11iIi1i
if 95 - 95: iI11I1II1I1I . ooOOOoO - ii * oO0o / I11i
if 74 - 74: oO0oo0o
if 34 - 34: Ii1IIIi1
def ii1IIiI1IIi ( string ) :
 if Ii1iIiII1ii1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 76 - 76: Ii1IIIi1 / oO0o + OOooOOo
def Oooo00 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iii1II1iI1IIi = [ ]
 try :
  if 41 - 41: oOo0O0Ooo - ii1ii11IIIiiI % IIiIiII11i . ii1ii11IIIiiI - I11O0O0oOO00O00o
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  ii1IIiI1IIi ( 'Making Favorites File' )
  iii1II1iI1IIi . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  I1Ii = open ( I1IIiiIiii , "w" )
  I1Ii . write ( json . dumps ( iii1II1iI1IIi ) )
  I1Ii . close ( )
 else :
  ii1IIiI1IIi ( 'Appending Favorites' )
  I1Ii = open ( I1IIiiIiii ) . read ( )
  i1I111Ii = json . loads ( I1Ii )
  i1I111Ii . append ( ( name , url , iconimage , fanart , mode ) )
  III1I11i1iIi = open ( I1IIiiIiii , "w" )
  III1I11i1iIi . write ( json . dumps ( i1I111Ii ) )
  III1I11i1iIi . close ( )
  if 31 - 31: oOo0O0Ooo
  if 73 - 73: O0OOOoOoo0 . o0o00Oo0O / I11i - ii % Ii
def O000 ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  iii1II1iI1IIi = [ ]
  ii1IIiI1IIi ( 'Making Favorites File' )
  iii1II1iI1IIi . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  I1Ii = open ( I1IIiiIiii , "w" )
  I1Ii . write ( json . dumps ( iii1II1iI1IIi ) )
  I1Ii . close ( )
 else :
  iIIiIi = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  I111I1I = len ( iIIiIi )
  for Oo0000 in iIIiIi :
   oO00oooOOoOo0 = Oo0000 [ 0 ]
   i1I1ii11i1Iii = Oo0000 [ 1 ]
   Oo00OoOo = Oo0000 [ 2 ]
   try :
    oO0OoOo = Oo0000 [ 3 ]
    if oO0OoOo == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oO0OoOo = Oo00OoOo
    else :
     oO0OoOo = oOo0O
   try : oOOOOOo = Oo0000 [ 5 ]
   except : oOOOOOo = None
   try : i1I11ii = Oo0000 [ 6 ]
   except : i1I11ii = None
   if 72 - 72: I11O0O0oOO00O00o
   if Oo0000 [ 4 ] == 0 :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , '' , Oo00OoOo , oOo0O , '' , 'fav' )
   else :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , Oo0000 [ 4 ] , Oo00OoOo , oOo0O , '' , 'fav' )
    if 87 - 87: ooOoO0O00
def II1IIiIiiI1iI ( name ) :
 i1I111Ii = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for oo00o0OoO in range ( len ( i1I111Ii ) ) :
  if i1I111Ii [ oo00o0OoO ] [ 0 ] == name :
   del i1I111Ii [ oo00o0OoO ]
   III1I11i1iIi = open ( I1IIiiIiii , "w" )
   III1I11i1iIi . write ( json . dumps ( i1I111Ii ) )
   III1I11i1iIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 88 - 88: Ii1I - iI1ii11iIi1i * OOooOOo
 if 73 - 73: I11i % oO0o + ooOOOoO + oOo0O0Ooo
def Iii ( ) :
 OoOO00 = os . path . join ( O0O , 'addons.ini' )
 O0O00OoOoOOo = open ( OoOO00 , "w+" )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIIi1I1IIii1II )
 O0O00OoOoOOo . write ( r'[' + IiII + ']' + '\n' )
 for oO00oooOOoOo0 , Ii1i1iI , I1iI1I1I1i11i , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  o0o0oo0 = ( oO00oooOOoOo0 + '=plugin://' + IiII + '/?url=' + i1I1ii11i1Iii + '&mode=10012&name=' + ( oO00oooOOoOo0 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( Ii1i1iI ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( Ii1i1iI ) . replace ( ' ' , '' ) + '+&amp;description=' )
  O0O00OoOoOOo . write ( o0o0oo0 + '\n' )
  if 25 - 25: oO0o * oO0oo0o % Ii + Ii * oO0o
  if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
def ooiiI1ii ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + '247.png' , III1iII1I1ii + '247.png' , '' )
def O0OooOO ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def i1i1o0oOoOo0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def III1IiI1i1i ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def o0OOOOOo0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi1I11I1II = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
  if 56 - 56: oO0oo0o + O0OOOoOoo0
def Ii1Ii1 ( ) :
 if 35 - 35: Ii - oO0oo0o % Ii
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 48 - 48: oO0o % I11O0O0oOO00O00o * I11i % oO0oo0o % Ii . Ii1IIIi1
def O00Oo0 ( ) :
 if 70 - 70: OOooOOo
 oo000o0000oO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 , OOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + '  -  ' + ( OOo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 10023 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 94 - 94: Ii / ii1ii11IIIiiI / I1ii11iIi11i
  if 9 - 9: I11O0O0oOO00O00o / OOooOOo / IIiIiII11i + ii1ii11IIIiiI
  if 71 - 71: Ii1IIIi1 / I1ii11iIi11i
def OOOO0Oo ( ) :
 if 13 - 13: IIiIiII11i
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Action[/COLOR]' , 'Aksiyon' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Adventure[/COLOR]' , 'Macera' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Animation[/COLOR]' , 'Animasyon' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Anime[/COLOR]' , 'Anime' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Biography[/COLOR]' , 'Biyografi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Comedy[/COLOR]' , 'Komedi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Drama[/COLOR]' , 'Dram' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Family[/COLOR]' , 'Aile' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']History[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Horror[/COLOR]' , 'Korku' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Mystery[/COLOR]' , 'Gizem' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Romance[/COLOR]' , 'Romantik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Sport[/COLOR]' , 'Spor' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Western[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 57 - 57: iI1ii11iIi1i - ii
def OOoOO0O0o0 ( url ) :
 o0o00 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIIi1I1IIii1II = cloudflare . source ( o0o00 )
 IIi1I11I1II = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 44 - 44: O00o0O00 / I1ii11iIi11i + ooOOOoO % IIiIiII11i / oO0o + Ii
  if 20 - 20: Ii1I
  if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
  if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
def I1I1IIiiii1ii ( ) :
 if 92 - 92: oO0oo0o / O00o0O00 . Ii1I
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iI1I ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = cloudflare . source ( i1I1ii11i1Iii )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if iI1I in oO00oooOOoOo0 . lower ( ) :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10022 , III1iII1I1ii + 'dtv.png' )
   if 30 - 30: iI1ii11iIi1i . Ii1I / O00o0O00
   if 2 - 2: ooOOOoO % oOo0O0Ooo - ii1ii11IIIiiI
   if 79 - 79: ii / Ii1I . o0o00Oo0O
def oOoO0Oo0 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o , i11i11i , iiI1iI , oO00oooOOoOo0 in IIi1I11I1II :
  Ooo00O0 = ( iiI1iI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OoO0OOoO0 = ( i11i11i ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iiI11i = 'Season ' + OoO0OOoO0 + 'Episode ' + Ooo00O0 + oO00oooOOoOo0
  o0Oo ( iiI11i , o0OO0o0o00o )
  if 4 - 4: IIiIiII11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 20 - 20: Ii % ii . ooOOOoO / I11O0O0oOO00O00o
  if 34 - 34: Ii / ii1ii11IIIiiI * O00o0O00 . I1ii11iIi11i
def o0Oo ( name , url ) :
 o0OO0o0o00o = url
 ooo0O00000oo0 = name
 O0 = cloudflare . source ( o0OO0o0o00o )
 OooOoooOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for Iiii , oOO0oo in OooOoooOo :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + ooo0O00000oo0 + oOO0oo + '[/COLOR]' , Iiii , 10012 , III1iII1I1ii + 'dtv.png' )
  if 62 - 62: iI1ii11iIi1i - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: ooOOOoO * ooOOOoO * o0o00Oo0O / O00o0O00 + o0o00Oo0O
 if 51 - 51: I11i - OOooOOo + I1ii11iIi11i / I11O0O0oOO00O00o % OOooOOo
def iIiii1Ii1I1II ( ) :
 if 14 - 14: oO0o
 if 36 - 36: oO0oo0o + OOooOOo + Ii1IIIi1 + oOo0O0Ooo
 if 39 - 39: oO0oo0o / I1ii11iIi11i
 if 9 - 9: oO0oo0o - ii1ii11IIIiiI % o0o00Oo0O . ooOoO0O00 . oOo0O0Ooo / oOo0O0Ooo
 if 82 - 82: I11O0O0oOO00O00o / O0OOOoOoo0 * I11O0O0oOO00O00o % Ii * IIiIiII11i
 if 83 - 83: oO0o + O00o0O00 - I11i + iI11I1II1I1I % I1ii11iIi11i
 if 23 - 23: I11i + iI1ii11iIi1i % OOooOOo % oOo0O0Ooo % ii
 if 78 - 78: oO0o / I1ii11iIi11i - iI11I1II1I1I - Ii * Ii1IIIi1
 if 84 - 84: O00o0O00 + iI1ii11iIi1i + I11i
 if 33 - 33: iI1ii11iIi1i
 if 93 - 93: O0OOOoOoo0
 if 34 - 34: oO0oo0o - O0OOOoOoo0 * I1ii11iIi11i / I11i
 if 19 - 19: Ii1I
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii11I1 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ii11I1 ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 71 - 71: ii1ii11IIIiiI - I11i - O00o0O00
def iiIO0OO0o0O00oO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 81 - 81: ooOOOoO / I11O0O0oOO00O00o
def III1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'episode' in url :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 24 - 24: oO0oo0o / ii1ii11IIIiiI / I11O0O0oOO00O00o % OOooOOo / Ii1I * O0OOOoOoo0
  if 8 - 8: iI1ii11iIi1i
def iIIi1 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Ooo0o0Oo = 'http://www.watchseries.ac/search/' + iI1I . replace ( ' ' , '%20' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( o0Ooo0o0Oo )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'watch online' in oO00oooOOoOo0 :
   pass
  else :
   print i1I1ii11i1Iii
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , Ii1i1iI , '' , '' )
   if 55 - 55: iI11I1II1I1I * Ii1IIIi1
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 85 - 85: iI11I1II1I1I . IIiIiII11i
def o0ooo0o0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , url , oO00oooOOoOo0 , iiI1iI , ooo0 in IIi1I11I1II :
  O00Oooo00 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iiI1iI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + O00Oooo00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , Ii1i1iI , '' , ooo0 )
  if 93 - 93: o0o00Oo0O / O0OOOoOoo0 + oOo0O0Ooo
def I111 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  O00Oooo00 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + O00Oooo00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 17 - 17: iI11I1II1I1I + oOo0O0Ooo
def oO0oiIiI ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , Ii1i1iI , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 46 - 46: Ii1IIIi1
def ooIiI11i1I11111 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 ii11I1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i11i11i , o0o0OO0o00o0O in ii11I1 :
  IIi1I11I1II = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o0o0OO0o00o0O ) )
  for url , oO00oooOOoOo0 in IIi1I11I1II :
   O00Oooo00 = ( i11i11i ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + O00Oooo00 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: oOo0O0Ooo * OOooOOo * oO0oo0o + Ii1I
class II1i ( ) :
 if 62 - 62: I11O0O0oOO00O00o / oO0oo0o % I1ii11iIi11i . ii / Ii / ii1ii11IIIiiI
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 60 - 60: oOo0O0Ooo % oO0oo0o / I11i % oO0oo0o * Ii / Ii1IIIi1
  O00Oooo00 = name
  self . Get_Sources ( i1I1ii11i1Iii , O00Oooo00 )
  if 34 - 34: ii1ii11IIIiiI - O00o0O00
  if 25 - 25: oO0oo0o % oOo0O0Ooo + Ii + o0o00Oo0O * ii
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( URL )
  IIi1I11I1II = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   URL = 'http://www.watchseries.ac/link/' + i1I1ii11i1Iii
   self . Get_site_link ( URL , season_name )
   if 64 - 64: ooOoO0O00
 def Get_site_link ( self , url , season_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  OooOoooOo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  ooIII1II1iii1i = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for url in IIi1I11I1II :
   self . main ( url , season_name )
  for url in OooOoooOo :
   self . main ( url , season_name )
  for url in ooIII1II1iii1i :
   self . main ( url , season_name )
   if 10 - 10: ii1ii11IIIiiI % o0o00Oo0O / oOo0O0Ooo % I11O0O0oOO00O00o
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iiII = 'DACLIPS'
   if iiII in II1i . source_list :
    pass
   else :
    self . daclips ( url , season_name , iiII )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    iiII = 'FILEHOOT'
    if iiII in II1i . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , iiII )
   else :
    if 'thevideo.me' in url :
     iiII = 'THEVIDEO'
     if iiII in II1i . source_list :
      pass
     else :
      self . thevideo ( url , season_name , iiII )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      iiII = 'ALLMYVIDEOS'
      if iiII in II1i . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , iiII )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       iiII = 'VIDSPOT'
       if iiII in II1i . source_list :
        pass
       else :
        self . vidspot ( url , season_name , iiII )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        iiII = 'VODLOCKER'
        if iiII in II1i . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , iiII )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 28 - 28: O0OOOoOoo0 . ii + I11i + iI1ii11iIi1i % Ii1IIIi1
         if 80 - 80: I1ii11iIi11i
 def allmyvid ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 19 - 19: I11i
 def vidspot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 73 - 73: ii1ii11IIIiiI * I1ii11iIi11i * OOooOOo
 def thevideo ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
 def vodlocker ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 26 - 26: I11i % O00o0O00 + O00o0O00 % I11O0O0oOO00O00o * Ii / Ii1IIIi1
 def daclips ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 64 - 64: oO0oo0o % OOooOOo / IIiIiII11i % O0OOOoOoo0 - Ii1IIIi1
 def filehoot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for OOo0oOOOOooOo in IIi1I11I1II :
   self . Printer ( OOo0oOOOOooOo , season_name , source_name )
   if 2 - 2: ii1ii11IIIiiI - Ii1I + I11i * oO0o / Ii1IIIi1
 def Printer ( self , Link , season_name , source_name ) :
  if 26 - 26: O00o0O00 * I1ii11iIi11i
  if Link in II1i . List :
   pass
  elif source_name in II1i . source_list :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   II1i . List . append ( Link )
   II1i . source_list . append ( source_name )
   if 31 - 31: I11O0O0oOO00O00o * oO0oo0o . iI1ii11iIi1i
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 35 - 35: I11O0O0oOO00O00o
   if 94 - 94: O0OOOoOoo0 / Ii % o0o00Oo0O
   if 70 - 70: I11O0O0oOO00O00o - I1ii11iIi11i / ii % ii
   if 95 - 95: ii % ii . iI1ii11iIi1i
   if 26 - 26: oO0oo0o + ooOOOoO - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
def o0IiIiI111IIII1 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , OO0o , '' )
 if 100 - 100: O00o0O00 * o0o00Oo0O + oOo0O0Ooo + OOooOOo . O00o0O00
def OO0IIIIIIi111i ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( oo000o0000oO )
 for iiIIIIiI111 , url , OoooOO0Oo0 , I1iIiIii , OO0I1iiI1iiI1i1 , II1Ii1iI1i1 , OOOO00OOO00 , o0Oo00 , I1Ii , ii1OO0 , Oo in IIi1I11I1II :
  OoooOO0Oo0 = OoooOO0Oo0
  if 'Arsenal' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'arsenal-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                                  ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Bournemouth' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'afc-bournemouth.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                       ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Burnley' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'KEGnQWW.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                                   ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Chelsea' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'chelsea.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                                  ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Crystal' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'CrystalPalace.0.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                       ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Everton' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'Everton.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                                   ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Hull' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'hull-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                                 ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Leicester' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                       ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Liverpool' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'liverpool-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                               ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Manchester City' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'city-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '               ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Manchester United' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + '91.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '          ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Middlesbrough' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                 ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Southampton' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'southampton-fc-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                   ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Stoke City' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'stoke-city.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                          ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Sunderland' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'sunderland-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                        ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Swansea' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'swansea-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                    ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Tottenham' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '        ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Watford' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'watford-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '                              ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'Bromwich' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '   ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  elif 'West Ham' in OoooOO0Oo0 :
   i1i11I1I1iii1 = III1iII1I1ii + 'west-ham.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + iiIIIIiI111 + ' - ' + OoooOO0Oo0 + '             ' + I1iIiIii + '        ' + OO0I1iiI1iiI1i1 + '        ' + II1Ii1iI1i1 + '        ' + OOOO00OOO00 + '        ' + o0Oo00 + '        ' + I1Ii + '        ' + ii1OO0 + '[/COLOR]'
  I1IIII1i ( str ( oO00oooOOoOo0 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , i1i11I1I1iii1 , i1i11I1I1iii1 , OoooOO0Oo0 )
  if 54 - 54: oOo0O0Ooo * O00o0O00 + I11i % ooOoO0O00 - I11i + OOooOOo
def IIIIiI11Ii1i ( description ) :
 OoooOO0Oo0 = description
 i1I1ii11i1Iii = ( 'http://www.fullmatchesandshows.com/?s=' + OoooOO0Oo0 ) . replace ( ' ' , '%20' )
 O0O0O0o ( i1I1ii11i1Iii )
 if 83 - 83: Ii1IIIi1 % I11O0O0oOO00O00o
def III1OOO000OOo0o0O ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi1I11I1II = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1I1ii11i1Iii , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ii1i1iI , OO0o , '' )
  if 14 - 14: Ii1IIIi1 - I11O0O0oOO00O00o * ii + O00o0O00 . IIiIiII11i
def i1i1I11i1I ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii11I1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii11I1 in ii11I1 :
  O0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( ii11I1 ) )
  for II1IIiiI1 in O0o :
   II1IIiiI1 = II1IIiiI1
  O00O00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ii11I1 ) )
  for oOooO0OoO , Ii1i1iI , time , o0oOOOOoo0 in O00O00 :
   OOoo = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0oOOOOoo0 )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + II1IIiiI1 + ' - ' + oOooO0OoO + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + Ii1i1iI , OO0o , ( str ( OOoo ) ) )
   if 80 - 80: Ii % Ii1I
 I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if 54 - 54: I11i + I11O0O0oOO00O00o - iI11I1II1I1I % O0OOOoOoo0 % ooOOOoO
def II1iiI1 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 if 4 - 4: I1ii11iIi11i - oO0o - Ii * ii1ii11IIIiiI / iI1ii11iIi1i - O00o0O00
def II1IIii1ii ( url ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , url , oO00oooOOoOo0 in IIi1I11I1II :
  IIiIiIiiI1Iii = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   IIiIiIiiI1Iii = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIiIiIiiI1Iii + '[/COLOR]' , url , 10013 , Ii1i1iI )
 for url , Ii1i1iI , oO00oooOOoOo0 in OooOoooOo :
  IIiIiIiiI1Iii = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIiIiIiiI1Iii + '[/COLOR]' , url , 10013 , Ii1i1iI )
def O0O0O0o ( url ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 if 43 - 43: o0o00Oo0O - O0OOOoOoo0 % ii % O00o0O00 + Ii1IIIi1
 if 61 - 61: O0OOOoOoo0 . Ii + oO0oo0o
 if 8 - 8: iI11I1II1I1I
 if 55 - 55: oO0oo0o
 if 37 - 37: ooOOOoO / Ii / I1ii11iIi11i
 if 97 - 97: ii1ii11IIIiiI . I11O0O0oOO00O00o / oOo0O0Ooo
 if 83 - 83: I11O0O0oOO00O00o - Ii1I * oO0oo0o
 for url , Ii1i1iI , oO00oooOOoOo0 in OooOoooOo :
  IIiIiIiiI1Iii = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIiIiIiiI1Iii + '[/COLOR]' , url , 10013 , Ii1i1iI )
   if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
def OO0OooOo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIIi1I1IIii1II )
 for Iiii in IIi1I11I1II :
  ii111iI1i1 = ( Iiii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  IiIii1ii ( 'http:' + ii111iI1i1 )
  if 80 - 80: oO0o / ooOOOoO * oOo0O0Ooo % ooOOOoO
  if 95 - 95: o0o00Oo0O / I11O0O0oOO00O00o . ii1ii11IIIiiI
  if 17 - 17: I11O0O0oOO00O00o
  if 56 - 56: O0OOOoOoo0 * I11i + I11O0O0oOO00O00o
def I11II11111i11 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 8046 , Ii1i1iI )
 for url in OooOoooOo :
  oOo0 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def OOO000Oo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  IiIii1ii ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 8 - 8: O0OOOoOoo0 - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * iI1ii11iIi1i - iI11I1II1I1I
def i1IiI1iIIIIIi ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 36 - 36: ooOOOoO
def iIi ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 52 - 52: iI11I1II1I1I
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a></li>' ) . findall ( oo000o0000oO )
 if 49 - 49: O00o0O00
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8041 , III1iII1I1ii + 'documentary.png' )
  if 23 - 23: oO0o / Ii1IIIi1 / iI11I1II1I1I
  if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / I11O0O0oOO00O00o + ii1ii11IIIiiI
  if 17 - 17: O00o0O00 + IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1i11I11Iii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 next = re . compile ( 'class="inactive">.+?</a><a href="([^"]*)">Next</a></div>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , Ii1i1iI )
 for oO00oooOOoOo0 , url , Ii1i1iI in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , Ii1i1iI )
 for url in next :
  oOo0 ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 3 - 3: I11i
  if 77 - 77: oOo0O0Ooo % O0OOOoOoo0
def oO0ooo00o0o000Oo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<meta itemprop="name" content="([^"]*)".+?<meta itemprop="thumbnailUrl" content="([^"]*)".+?<meta itemprop="embedUrl" content="([^"]*)".+?<meta itemprop="description" content="([^"]*)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , Ii1i1iI , url , ooOo0OoO in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , Ii1i1iI )
 for url in OooOoooOo :
  Oooo00OOo ( ( url ) . replace ( '//' , 'http://' ) )
  if 6 - 6: oO0oo0o / oOo0O0Ooo / OOooOOo
def Oooo00OOo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<link rel="canonical" href="([^"]*)">  <link rel="stylesheet"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOOoOO ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , III1iII1I1ii + 'documentary.png' )
  if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , Ii1i1iI )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , url , 8048 , III1iII1I1ii + 'Next.png' )
def Ii1I1IIIiI1i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in OooOoooOo :
  if 'rtd' in url :
   o0Oo00oOO ( url )
   if 73 - 73: I11O0O0oOO00O00o / ii . IIiIiII11i - ooOOOoO * O0OOOoOoo0 * ooOOOoO
def o0Oo00oOO ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oo000o0000oO )
 for OOO00O , file in IIi1I11I1II :
  url = ( 'https://rtd.rt.com' + OOO00O + file )
  IiIii1ii ( url )
  if 45 - 45: o0o00Oo0O * ii1ii11IIIiiI + Ii - O00o0O00 - iI11I1II1I1I
  if 5 - 5: O00o0O00 % I1ii11iIi11i % ooOOOoO % O0OOOoOoo0
def I1Iiii ( ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( 'http://www.stream2watch.co/live-tv' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 , I1I1Iii1Iiii in IIi1I11I1II :
  oOo0 ( ( oO00oooOOoOo0 + '[COLOR' + iiI1IiI + ']' + I1I1Iii1Iiii + '[/COLOR]' ) , i1I1ii11i1Iii , 8086 , Ii1i1iI )
  if 4 - 4: ooOOOoO
def oOo0OoOOOo0 ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8087 , Ii1i1iI )
  if 55 - 55: oO0oo0o + o0o00Oo0O / Ii1IIIi1 % O0OOOoOoo0 / ii
def O00o0OO0OO0oo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  Ooo0O0ooo0o ( url , oO00oooOOoOo0 )
  if 50 - 50: Ii - ii . oO0oo0o + o0o00Oo0O . ooOoO0O00
def Ooo0O0ooo0o ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  print url
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 91 - 91: I11i . Ii1IIIi1 % I1ii11iIi11i - Ii1IIIi1 . oO0oo0o % Ii
def iIiO0O ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i1I1ii11i1Iii , 3002 , 'http://www.solie.org/alibrary/' + Ii1i1iI )
def oOOoooo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ii1i1iI )
def O0oIi1iIiIi1I11 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 ii1I11 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oo000o0000oO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , oO00oooOOoOo0 in ii1I11 :
  oOo0 ( '[COLOR' + iiI1IiI + ']Season- ' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , Ii1i1iI , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + Ii1i1iI )
def OOO0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  I1Ii1 ( url )
def I1Ii1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  IiIii1ii ( url )
  if 67 - 67: I11O0O0oOO00O00o % Ii . iI11I1II1I1I * oOo0O0Ooo - I11O0O0oOO00O00o + iI1ii11iIi1i
def i1ii1iIi ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classicmovies.png' )
def I1I1Ii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "v.src = '([^']*)';" ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  O00OoOO0oo0 ( url )
  if 42 - 42: I11i - I1ii11iIi11i % Ii1I
def I11ii1iI11 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classictv.png' )
def i11ii111i1ii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'mp4' in url :
   IiIii1ii ( url )
 for url in OooOoooOo :
  yt . PlayVideo ( url )
  if 97 - 97: Ii + I1ii11iIi11i * O00o0O00 % Ii1IIIi1 . ooOOOoO
def iiOo0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1I1ii11i1Iii , 8071 , III1iII1I1ii + 'streams.png' )
def OOO00ii1Ii111I11I ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '(Free Access)' in oO00oooOOoOo0 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def o0OoOoo ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , oO00oooOOoOo0 , url in IIi1I11I1II :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , Ii1i1iI , oOo0O , '' )
  if 75 - 75: Ii1IIIi1 * oOo0O0Ooo + Ii1IIIi1 - ii
def OooO ( ) :
 oO0Ooo0OooOOo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 oO0Ooo0OooOOo ( 'Genres' , 'http://www.xvideos.com' , 10106 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 oO0Ooo0OooOOo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 oO0Ooo0OooOOo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 oO0Ooo0OooOOo ( 'Search' , '' , 10107 , III1iII1I1ii + 'Jizbox.png' , '' , '' , )
 if 85 - 85: IIiIiII11i
def o0oOOoo0O ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OoooOo00 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in OoooOo00 :
  oO0Ooo0OooOOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , iiIi1i in IIi1I11I1II :
  oO0Ooo0OooOOo ( ( oO00oooOOoOo0 + ' - No of Videos : ' + ( iiIi1i ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 98 - 98: oO0o . iI11I1II1I1I % ii % I1ii11iIi11i - Ii1I
def oO0I1I1i1I1I1I1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OoooOo00 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in OoooOo00 :
  oO0Ooo0OooOOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , url , oO00oooOOoOo0 , oOOOOOoOO in IIi1I11I1II :
  oO0Ooo0OooOOo ( oO00oooOOoOo0 + '--' + oOOOOOoOO , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( Ii1i1iI ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 34 - 34: oO0o * iI1ii11iIi1i * I1ii11iIi11i
  if 21 - 21: ii . OOooOOo - iI11I1II1I1I % ooOOOoO
def Oooo0ooOoo0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , url , oO00oooOOoOo0 , oOoooo000Oo00 , i1Iii in IIi1I11I1II :
  oO0Ooo0OooOOo ( oO00oooOOoOo0 + ' - Porn Quality : ' + i1Iii + ' - ' + oOoooo000Oo00 , 'http://www.xvideos.com' + url , 10108 , Ii1i1iI , Ii1i1iI , i1Iii + ' - ' + oOoooo000Oo00 )
 oO00oO00O0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for url in oO00oO00O0Oo :
  oO0Ooo0OooOOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 88 - 88: oO0oo0o - ooOoO0O00 % Ii % IIiIiII11i * ii
def iIiII1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 ii11I1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OoooOo00 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in OoooOo00 :
  oO0Ooo0OooOOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ii11I1 ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oO0Ooo0OooOOo ( oO00oooOOoOo0 , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 47 - 47: I11O0O0oOO00O00o
  if 92 - 92: ii % oOo0O0Ooo / OOooOOo * OOooOOo % Ii / ii
def IiII1 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111iI = ( iI1I ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 III1I1Iii1iiI = ii111iI . lower ( )
 iII1 = 'http://www.xvideos.com/?k=' + III1I1Iii1iiI
 print iII1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( iII1 )
 IIi1I11I1II = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 , oOoooo000Oo00 , i1Iii in IIi1I11I1II :
  oO0Ooo0OooOOo ( oO00oooOOoOo0 + ' - Porn Quality : ' + i1Iii + ' - ' + oOoooo000Oo00 , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10108 , Ii1i1iI , Ii1i1iI , i1Iii + ' - ' + oOoooo000Oo00 )
 oO00oO00O0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in oO00oO00O0Oo :
  oO0Ooo0OooOOo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 9 - 9: oO0o
def II1i1i1I1iII ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 ooIII1II1iii1i = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']LOW[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in OooOoooOo :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']HIGH[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in ooIII1II1iii1i :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']HLS[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 48 - 48: O00o0O00 . O00o0O00 + Ii + Ii1I % o0o00Oo0O
def O0000ii1i1II ( url ) :
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 try : I1IiiiIiI . play ( url )
 except : pass
 if 35 - 35: Ii1I * Ii1IIIi1 . ooOOOoO . ooOOOoO - oO0oo0o % OOooOOo
 if 42 - 42: I11i - iI11I1II1I1I % ii
def iII11IiI1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 8091 , III1iII1I1ii + 'gofish.png' )
def OoOOOO00oOO ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1092 , Ii1i1iI )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def iiIIiIi ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8092 , Ii1i1iI )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def O000oO ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "videoId: '([^']*)'," ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 23 - 23: IIiIiII11i * Ii1IIIi1
  if 80 - 80: ii1ii11IIIiiI / Ii + ii
  if 38 - 38: Ii1I % O0OOOoOoo0 + ooOoO0O00 * ii * oO0oo0o
OoO0o0OO = '{PQ},' ; II11IiI1 = '{SC},' ; iIIi11i = '{XG},' ; III = '{JP},' ; iiIi111Ii1II = '{HW},' ; oOoo0oO = '{RT},'
def IIii1i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o00oo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 18 - 18: Ii - O0OOOoOoo0 * oO0oo0o + I11i
 oOO = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 IiiiIi1iiii11 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 iIIi1IIIii11i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ii11I1I11II = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIiiiI = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iI1I
 oO0Oooo0OoO = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 Iiii1IIIIiiI11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I1iii1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oooII111 = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 29 - 29: ooOOOoO + Ii * o0o00Oo0O - Ii1IIIi1 . IIiIiII11i % iI1ii11iIi1i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 41 - 41: oO0oo0o / O00o0O00 + Ii1IIIi1 + O0OOOoOoo0
 if 13 - 13: Ii - Ii . iI11I1II1I1I
 ii1ii1ii = ooOooo000oOO ( oOO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( IiiiIi1iiii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 Iii1I11 = ooOooo000oOO ( iIIi1IIIii11i )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 O0o0o = ooOooo000oOO ( IIiiiI )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiiIi1111I = ooOooo000oOO ( oO0Oooo0OoO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iII1i1ii = ooOooo000oOO ( Iiii1IIIIiiI11 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 i1I1ii1i = ooOooo000oOO ( I1iii1I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iiiiII11iIi = ooOooo000oOO ( oooII111 )
 if 51 - 51: I1ii11iIi11i / ooOOOoO * iI1ii11iIi1i - IIiIiII11i / oOo0O0Ooo . ooOOOoO
 if 65 - 65: ooOOOoO
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oooOOo0oOoOO , oO00oooOOoOo0 in IIi1I11I1II :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1I1ii11i1Iii + oooOOo0oOoOO ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 6 - 6: oO0oo0o . I11O0O0oOO00O00o
    if 43 - 43: Ii1I + I11i
    if 50 - 50: oO0oo0o % ooOoO0O00 * o0o00Oo0O
    if 4 - 4: iI11I1II1I1I . ooOoO0O00
    if 63 - 63: iI11I1II1I1I + ooOOOoO % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
    if 60 - 60: I11i . OOooOOo % ii1ii11IIIiiI / oOo0O0Ooo / o0o00Oo0O
    if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / O00o0O00 . Ii1I * O0OOOoOoo0
 if ii1ii1ii != 'Failed' :
  ooIII1II1iii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for oooOOo0oOoOO , oO00oooOOoOo0 in ooIII1II1iii1i :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOO + oooOOo0oOoOO ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  oo0OOoooo0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in oo0OOoooo0O0 :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 99 - 99: I1ii11iIi11i + Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if Iii1I11 != 'Failed' :
  I111Ii11i11I = [ ]
  i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Iii1I11 )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in i11I :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    if oO00oooOOoOo0 in I111Ii11i11I :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i1I1ii11i1Iii , 1016 , Oo00OoOo , ooo , ooo0 )
     I111Ii11i11I . append ( oO00oooOOoOo0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if O0o0o != 'Failed' :
  oO0000O0Oo00O = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( O0o0o )
  for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in oO0000O0Oo00O :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1I1ii11i1Iii , 7067 , Ii1i1iI )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 42 - 42: Ii / oOo0O0Ooo - oO0o - O0OOOoOoo0 + IIiIiII11i % O0OOOoOoo0
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if IiiiIi1111I != 'Failed' :
  Ii1IIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiiIi1111I )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in Ii1IIii :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Redemption[/COLOR]' ) , i1I1ii11i1Iii , 222 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 80 - 80: Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if iII1i1ii != 'Failed' :
  IiIiiI1iii1iIiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1i1ii )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in IiIiiI1iii1iIiiI :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 222 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / O00o0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if i1I1ii1i != 'Failed' :
  IiiIiiIIII = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1ii1i )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in IiiIiiIIII :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Herovision[/COLOR]' ) , i1I1ii11i1Iii , 222 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 88 - 88: oO0o . ii1ii11IIIiiI / I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 47 - 47: oO0o + Ii1I . O0OOOoOoo0
 if iiiiII11iIi != 'Failed' :
  IiiIiIIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiiiII11iIi )
  for i1I1ii11i1Iii , Oo00OoOo , oO00oooOOoOo0 in IiiIiIIi1 :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , Oo00OoOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 40 - 40: Ii1IIIi1 . OOooOOo * o0o00Oo0O
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 oOo00o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + I11O0O0oOO00O00o . O00o0O00
 for oO0oOoo0O in oOo00o :
  II1iI11 = I11i1I1I + oO0oOoo0O + IIIII
  oo0OIii1iI1iiIii = ooOooo000oOO ( II1iI11 )
  if oo0OIii1iI1iiIii != 'Failed' :
   iIiiI111I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0OIii1iI1iiIii )
   for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in iIiiI111I11 :
    if iI1I in oO00oooOOoOo0 . lower ( ) :
     iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , 222 , Oo00OoOo , ooo , ooo0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 86 - 86: oO0oo0o + Ii1IIIi1 / ii - I11O0O0oOO00O00o
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 55 - 55: O00o0O00 / OOooOOo * O00o0O00
 oOo00o = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 40 - 40: oO0o . Ii + Ii1I + oOo0O0Ooo . oO0oo0o
 if 90 - 90: ii1ii11IIIiiI . OOooOOo * IIiIiII11i % O0OOOoOoo0
 for oO0oOoo0O in oOo00o :
  II1iI11 = o00oo + oO0oOoo0O
  II1IiII1 = ooOooo000oOO ( II1iI11 )
  if II1IiII1 != 'Failed' :
   Ii1iI1IIIII = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( II1IiII1 )
   for oooOOo0oOoOO , oO00oooOOoOo0 in Ii1iI1IIIII :
    if iI1I in oO00oooOOoOo0 . lower ( ) :
     OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o00oo + oO0oOoo0O + oooOOo0oOoOO ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 93 - 93: iI11I1II1I1I - O0OOOoOoo0 / oO0oo0o + Ii + ooOOOoO
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 16 - 16: iI11I1II1I1I
     if 94 - 94: O0OOOoOoo0 % I11O0O0oOO00O00o % ooOoO0O00
def o0OoOo0o0O00 ( ) :
 if 33 - 33: O0OOOoOoo0 + ii - oO0o / ooOoO0O00 / ii
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 if 82 - 82: Ii1I / O00o0O00 - Ii1IIIi1 / I1ii11iIi11i * oO0o
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( iI1I ) . replace ( ' ' , '%20' )
 o0OO0o0o00o = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 oOO = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 IiiiIi1iiii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIIi1IIIii11i = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( III1I1Iii1iiI ) . replace ( ' ' , '+' )
 Ii11I1I11II = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IIiiiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oO0Oooo0OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 55 - 55: ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0 = ooOooo000oOO ( o0OO0o0o00o )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ii1ii1ii = ooOooo000oOO ( oOO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( IiiiIi1iiii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 Iii1I11 = cloudflare . source ( iIIi1IIIii11i )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 II1IiII1 = ooOooo000oOO ( Ii11I1I11II )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0o0o = ooOooo000oOO ( IIiiiI )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 IiiiIi1111I = ooOooo000oOO ( oO0Oooo0OoO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 38 - 38: o0o00Oo0O
 if IiiiIi1111I != 'Failed' :
  Ii1IIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiiIi1111I )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in Ii1IIii :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source HeroVision[/COLOR]' ) , i1I1ii11i1Iii , 1016 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 79 - 79: ooOoO0O00 . oO0oo0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: ii1ii11IIIiiI * IIiIiII11i
 if O0o0o != 'Failed' :
  oO0000O0Oo00O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0o )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in oO0000O0Oo00O :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 1016 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 71 - 71: ooOOOoO
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 97 - 97: Ii1I
    if 86 - 86: I1ii11iIi11i - O00o0O00 . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
    if 34 - 34: I11i . ii1ii11IIIiiI % ooOOOoO - o0o00Oo0O / ii1ii11IIIiiI
    if 91 - 91: Ii % ii1ii11IIIiiI * oO0oo0o - Ii1I . ii1ii11IIIiiI
    if 28 - 28: Ii
    if 51 - 51: oOo0O0Ooo + O0OOOoOoo0 * o0o00Oo0O . iI1ii11iIi1i
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 82 - 82: O00o0O00 * Ii1I % iI1ii11iIi1i . O00o0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for Ii1i1iI , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , Ii1i1iI , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 43 - 43: oO0o . O0OOOoOoo0 * I1ii11iIi11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 20 - 20: ooOoO0O00 . ooOoO0O00 - I11O0O0oOO00O00o
    if 89 - 89: O0OOOoOoo0 - I11O0O0oOO00O00o . o0o00Oo0O % ii . Ii
    if 35 - 35: IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
    if 55 - 55: I1ii11iIi11i % ooOoO0O00 * I11O0O0oOO00O00o
    if 95 - 95: O00o0O00 / IIiIiII11i - I11i % ii1ii11IIIiiI . I11O0O0oOO00O00o
    if 63 - 63: iI11I1II1I1I / O0OOOoOoo0
    if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % O00o0O00 * OOooOOo - iI11I1II1I1I
    if 50 - 50: IIiIiII11i
    if 39 - 39: IIiIiII11i . OOooOOo - I1ii11iIi11i * ooOoO0O00 . ii
    if 44 - 44: oOo0O0Ooo
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in OooOoooOo :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , i1I1ii11i1Iii , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 55 - 55: oO0oo0o . ii1ii11IIIiiI * ii1ii11IIIiiI
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  ooIII1II1iii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in ooIII1II1iii1i :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOO + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 82 - 82: oOo0O0Ooo % oO0o % I11O0O0oOO00O00o + I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  oo0OOoooo0O0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for oO00oooOOoOo0 in oo0OOoooo0O0 :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiIi1iiii11 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 6 - 6: I1ii11iIi11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if Iii1I11 != 'Failed' :
  i11I = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( Iii1I11 )
  for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in i11I :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source - Dizi[/COLOR]' , i1I1ii11i1Iii , 8062 , Ii1i1iI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 73 - 73: ii1ii11IIIiiI * Ii1I + I11i - I1ii11iIi11i . I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if II1IiII1 != 'Failed' :
  Ii1iI1IIIII = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1IiII1 )
  for i1I1ii11i1Iii , Oo00OoOo , ooo0 , ooo , oO00oooOOoOo0 in Ii1iI1IIIII :
   if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- Source Scooby[/COLOR]' ) , i1I1ii11i1Iii , 1016 , Oo00OoOo , ooo , ooo0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 93 - 93: Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: ooOoO0O00 . oOo0O0Ooo - oO0oo0o + O00o0O00 + Ii1IIIi1 % oO0oo0o
 IiiII = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if II1IiII1 != 'Failed' :
  for oO0oOoo0O in IiiII :
   II1iI11 = I11i1I1I + oO0oOoo0O + IIIII
   i1I1ii1i = O0i1II1Iiii1I11 ( II1iI11 )
   if i1I1ii1i != 'Failed' :
    IiiIiiIIII = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1I1ii1i )
    for oO00oooOOoOo0 , ooo0 , i1I1ii11i1Iii , Ii1i1iI , oOo0O , oo000o in IiiIiiIIII :
     if III1I1Iii1iiI in oO00oooOOoOo0 . lower ( ) :
      I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , oo000o , Ii1i1iI , oOo0O , ooo0 )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 47 - 47: Ii1IIIi1 + o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . iI1ii11iIi1i
      I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
      if 28 - 28: oO0oo0o . oO0oo0o . iI11I1II1I1I . O00o0O00 . Ii1I * Ii
      if 72 - 72: I11O0O0oOO00O00o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1I1IIiIIi ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( iI1I ) . replace ( ' ' , '+' )
 if 33 - 33: oO0o % ooOOOoO - iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 33 - 33: oO0o + OOooOOo - oO0oo0o * Ii . ii1ii11IIIiiI
 if IIIi1I1IIii1II != 'Failed' :
  OooOoooOo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    OOOoOO ( ( oO00oooOOoOo0 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + i1I1ii11i1Iii ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 92 - 92: oO0oo0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
OOOOo0o0O0o = '{ZH},' ; IIIIIIiIIIi1iii1 = '{IX},' ; iii11III1I = '{LM},'
if 61 - 61: Ii1I + iI11I1II1I1I % I11i
def ooooooO0O ( url ) :
 O0oooO00ooO0 = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O0oooO00ooO0 )
 for url , i11i11i , OOo0 , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( i11i11i ) . replace ( 'Sezon' , ' Season ' ) + ( OOo0 ) . replace ( 'Bölüm' , ' Episode ' ) + oO00oooOOoOo0 , url , 8063 , '' )
  if 99 - 99: ooOOOoO
  if 92 - 92: oO0o + I11O0O0oOO00O00o - ooOOOoO . Ii1I * O0OOOoOoo0 - Ii
  if 74 - 74: oO0o + Ii1IIIi1 + IIiIiII11i
  if 48 - 48: ii
def Oo0OOOOOOO0oo ( url ) :
 O0oooO00ooO0 = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0oooO00ooO0 )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , '' )
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
  if 15 - 15: O0OOOoOoo0 % I11i / oO0oo0o - IIiIiII11i . iI11I1II1I1I
  if 28 - 28: IIiIiII11i * O0OOOoOoo0 * iI1ii11iIi1i
  if 93 - 93: ooOoO0O00 . iI1ii11iIi1i * ii1ii11IIIiiI . O0OOOoOoo0
def O0iI1I1ii11IIi1 ( ) :
 if 100 - 100: I1ii11iIi11i . iI1ii11iIi1i . oOo0O0Ooo % IIiIiII11i - oO0oo0o
 O0oooO00ooO0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0oooO00ooO0 )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 , OOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 + '  -  ' + ( OOo0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 8063 , Ii1i1iI )
  if 52 - 52: oOo0O0Ooo % oO0o * iI1ii11iIi1i * Ii1IIIi1 / O00o0O00
def oooO00oo0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 8002 , Ii1i1iI )
def o000 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oo000o0000oO )
 for Ii1i1iI , time , url , oO00oooOOoOo0 , ooOo0OoO in IIi1I11I1II :
  I1IIII1i ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , time ) , url , 1015 , Ii1i1iI , ooOo0OoO )
  if 75 - 75: o0o00Oo0O
def oOoO ( ) :
 if 59 - 59: O00o0O00 + oOo0O0Ooo / IIiIiII11i / OOooOOo
 oOo0 ( 'Coronation Street' , '' , 8001 , '' )
 oOo0 ( 'Eastenders' , '' , 8002 , '' )
 oOo0 ( 'Emmerdale' , '' , 8003 , '' )
 oOo0 ( 'Hollyoaks' , '' , 8004 , '' )
 oOo0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 80 - 80: OOooOOo + iI11I1II1I1I . ooOOOoO
 if 76 - 76: oOo0O0Ooo * O00o0O00
 if 12 - 12: iI11I1II1I1I / I11O0O0oOO00O00o % iI1ii11iIi1i
 if 49 - 49: oO0o + IIiIiII11i / ooOOOoO - o0o00Oo0O % iI1ii11iIi1i
def iII1i1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Holly' in oO00oooOOoOo0 :
   Ii1i1iI = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , Ii1i1iI )
   else :
    pass
    if 34 - 34: oO0o / ii - oO0oo0o / oO0oo0o * oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 61 - 61: I11O0O0oOO00O00o
def o00OOOOooO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'East' in oO00oooOOoOo0 :
   Ii1i1iI = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , Ii1i1iI )
   else :
    pass
    if 86 - 86: ii1ii11IIIiiI % oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: Ii * ii1ii11IIIiiI . I1ii11iIi11i . ii + oOo0O0Ooo
def Iii1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Emmer' in oO00oooOOoOo0 :
   Ii1i1iI = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , Ii1i1iI )
   else :
    pass
    if 66 - 66: I11O0O0oOO00O00o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: o0o00Oo0O
def Oo0Oo0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Coro' in oO00oooOOoOo0 :
   Ii1i1iI = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , Ii1i1iI )
   else :
    pass
    if 80 - 80: oOo0O0Ooo - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: IIiIiII11i
def iIii1II1I ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Celeb' in oO00oooOOoOo0 :
   Ii1i1iI = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , Ii1i1iI )
   else :
    pass
    if 25 - 25: OOooOOo
def iii1IiII ( name , url ) :
 o0oo0OooOO0 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if o0oo0OooOO0 :
  oooOooOOo00 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oo000o0000oO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( oo000o0000oO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oo000o0000oO = open_url ( url )
  OOo0O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( oo000o0000oO ) [ - 1 ]
  oooOooOOo00 = OOo0O . replace ( '\\/' , '/' )
 OoOoooO000OO = xbmcgui . ListItem ( name , '' , '' )
 OoOoooO000OO . setPath ( oooOooOOo00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoOoooO000OO )
 if 86 - 86: iI11I1II1I1I . I1ii11iIi11i % ii % ii % O0OOOoOoo0 + Ii
 if 43 - 43: OOooOOo % I11O0O0oOO00O00o
def oOo00 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 53 - 53: O00o0O00 + I11i . oO0oo0o / I11O0O0oOO00O00o
def o0000oO ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Movies' in oO00oooOOoOo0 :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( i1I1ii11i1Iii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def ooo0oo ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ii1i1iI )
 for url in OooOoooOo :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 70 - 70: o0o00Oo0O / ii + Ii1I + ooOoO0O00
  if 63 - 63: Ii1IIIi1 / Ii1I * oO0oo0o / IIiIiII11i + O00o0O00 - o0o00Oo0O
def Iii1I ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url , Ii1i1iI in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , Ii1i1iI )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
oOo000Oo00o = '{UJ},' ; o0o = '{WE},' ; oOOoOoOO = '{WP},' ; iII11 = '{PP},'
def O00OO00OOOoO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url , Ii1i1iI in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , Ii1i1iI )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiI11Ii1iI ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  ooOo0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOo0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: IIiIiII11i
 if 48 - 48: O00o0O00
 if 26 - 26: Ii1IIIi1 * ii1ii11IIIiiI * oO0oo0o * OOooOOo
def I1ii1i11iI1 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def IiOOo0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  IiIii1ii ( ( url ) . replace ( ' ' , '%20' ) )
o0O0O0O00o = '{XX},' ; OoOooOo00o = '{UD},' ; iI1IIi = '{YT},' ; II11 = '{JS},' ; oo0o0O = '{PF},'
if 91 - 91: iI11I1II1I1I % o0o00Oo0O
def oooIi1i ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( i1I1ii11i1Iii ) ) , 222 , Ii1i1iI )
  if 49 - 49: oO0oo0o + oO0oo0o + Ii % Ii1IIIi1
def I1I1 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oo000o0000oO )
 for Ii1i1iI , url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'youtu' in url :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + Ii1i1iI )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 80 - 80: I11i % Ii1IIIi1
def ooOooOooOOO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 59 - 59: I11O0O0oOO00O00o
def OOI1i ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11
 IIi1I11I1II = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , Ii1i1iI )
  if 47 - 47: Ii1IIIi1 . OOooOOo
  if 58 - 58: Ii1IIIi1 + I1ii11iIi11i / oOo0O0Ooo
  if 68 - 68: ooOOOoO * iI1ii11iIi1i
  if 91 - 91: iI1ii11iIi1i + oO0o * I11i . ii1ii11IIIiiI
  if 89 - 89: ii * iI1ii11iIi1i * oOo0O0Ooo . O0OOOoOoo0 * iI1ii11iIi1i / Ii1IIIi1
def iioo ( ) :
 if 21 - 21: ooOoO0O00
 oOo0 ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 oOo0 ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 69 - 69: OOooOOo + OOooOOo + O00o0O00 % O00o0O00 * I11O0O0oOO00O00o % iI1ii11iIi1i
 if 10 - 10: iI1ii11iIi1i
def I11IIiI1IiI1 ( Cat_Name ) :
 if 37 - 37: oO0oo0o % ii1ii11IIIiiI % oO0oo0o
 iIII = False
 i1i1Ii = '0'
 if Cat_Name == 'All Channels' : iIII = True
 if Cat_Name == 'Entertainment' : i1i1Ii = '1'
 if Cat_Name == 'Movies' : i1i1Ii = '2'
 if Cat_Name == 'Music' : i1i1Ii = '3'
 if Cat_Name == 'News' : i1i1Ii = '4'
 if Cat_Name == 'Sports' : i1i1Ii = '5'
 if Cat_Name == 'Documentary' : i1i1Ii = '6'
 if Cat_Name == 'Kids' : i1i1Ii = '7'
 if Cat_Name == 'Food' : i1i1Ii = '8'
 if Cat_Name == 'Religious' : i1i1Ii = '9'
 if Cat_Name == 'USA Channels' : i1i1Ii = '10'
 if Cat_Name == 'Other' : i1i1Ii = '11'
 if 69 - 69: o0o00Oo0O + iI11I1II1I1I % Ii1IIIi1 * oOo0O0Ooo . I1ii11iIi11i - OOooOOo
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oo000o0000oO )
 print 'Len Match: >>>' + str ( len ( IIi1I11I1II ) )
 for oO00oooOOoOo0 , Ii1i1iI , I1iiII in IIi1I11I1II :
  oOOOO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ii1i1iI ) . replace ( '\\' , '' )
  if I1iiII == i1i1Ii :
   oOo0 ( oO00oooOOoOo0 , '' , 7022 , oOOOO0 )
  elif iIII == True :
   oOo0 ( oO00oooOOoOo0 , '' , 7022 , oOOOO0 )
  else : pass
  if 99 - 99: O00o0O00 + oOo0O0Ooo . Ii1I * ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + O00o0O00 * IIiIiII11i
def iIiIiiIIIi1 ( Search_Name ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oo000o0000oO )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oo000o0000oO )
 for Ii1i1iI , i1I1ii11i1Iii , o0OO0o0o00o , oOO in IIi1I11I1II :
  oOOOO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( Ii1i1iI ) . replace ( '\\' , '' )
  OOOoOO ( Search_Name + ': Link 1' , ( i1I1ii11i1Iii ) . replace ( '\\' , '' ) , 222 , oOOOO0 )
  OOOoOO ( Search_Name + ': Link 2' , ( o0OO0o0o00o ) . replace ( '\\' , '' ) , 222 , oOOOO0 )
  OOOoOO ( Search_Name + ': Link 3' , ( oOO ) . replace ( '\\' , '' ) , 222 , oOOOO0 )
  if 25 - 25: o0o00Oo0O
def Oo00o00 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def OoOo0O0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def I1o0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 26 - 26: Ii1IIIi1 * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
def O0OO ( url ) :
 url
 Iii1iiIi1II1 = xbmcgui . ListItem ( oO00oooOOoOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Iii1iiIi1II1 )
 return
 if 77 - 77: iI1ii11iIi1i % O00o0O00 / oO0oo0o
 if 91 - 91: oO0o / oO0o . IIiIiII11i . O0OOOoOoo0 - oOo0O0Ooo
def iii11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oo000o0000oO )
 for url , ooo0 , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + Ii1i1iI , '' , ( ooo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 59 - 59: I1ii11iIi11i / Ii * oOo0O0Ooo + oO0o
def I11iIIIIi1Iii1iIi ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , ooo0 , Ii1i1iI in IIi1I11I1II :
  iIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + Ii1i1iI , '' , ooo0 )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 o0o0OO0o00o0O = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii1IIi1iI1ii1 in o0o0OO0o00o0O :
  o00iIIiIi111iI = ( ii1IIi1iI1ii1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + Ii1i1iI , '' , o00iIIiIi111iI )
  if 40 - 40: OOooOOo + oO0o % ii * I11i / OOooOOo + ii
def o0OOOoO0O ( INFO ) :
 O0O0Oooo0o ( 'info for workout' , INFO )
 if 74 - 74: ooOoO0O00 / OOooOOo - I1ii11iIi11i . ooOOOoO % Ii1I - ooOOOoO
 if 86 - 86: I1ii11iIi11i
 if 88 - 88: ii1ii11IIIiiI * oOo0O0Ooo
def IIiI ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'Name=(.+?)\n.+?m3u=(.+?)\n' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  oOo0 ( ( oO00oooOOoOo0 ) . replace ( 'SlyNet' , '' ) , url , 9032 , III1iII1I1ii + 'Sport.png' )
def OOoOo0oO0oo00 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 9032 , III1iII1I1ii + 'icon.png' )
def OOI1I ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:-.+?,(.+?)\n(.+?)\n' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def o0oO00O ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'icon.png' )
   if 72 - 72: oO0o - iI11I1II1I1I . Ii1IIIi1 / iI1ii11iIi1i
   if 12 - 12: oOo0O0Ooo + ii1ii11IIIiiI
   if 80 - 80: oO0oo0o . o0o00Oo0O
   if 90 - 90: IIiIiII11i / oO0o / iI1ii11iIi1i
   if 70 - 70: iI1ii11iIi1i - IIiIiII11i . I1ii11iIi11i / I1ii11iIi11i
def IIIi1iiIIiiiI ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3NvdXJjZXR2LmluZm8v' ) )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 9008 , III1iII1I1ii + 'disclose.png' )
def I1IIiIi1iI ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="article-image darken"><a href="([^"]*)"><img width="320" height="205" src="([^"]*)".+?title="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 9009 , Ii1i1iI )
def oOo0Iiii11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 65 - 65: ii1ii11IIIiiI + Ii1IIIi1 * Ii1IIIi1
def OoOO ( ) :
 oo000o0000oO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '.m3u' in i1I1ii11i1Iii :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + i1I1ii11i1Iii ) , 9011 , III1iII1I1ii + 'disclose.png' )
def iIO0oOoo00Oo0O ( url ) :
 oo000o0000oO = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 5 - 5: o0o00Oo0O - Ii1IIIi1 / ii1ii11IIIiiI . I11i
def iIII1iIii ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'category' in i1I1ii11i1Iii :
   oOo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + i1I1ii11i1Iii , 7010 , III1iII1I1ii + 'disclose.png' )
   if 9 - 9: ooOoO0O00 - OOooOOo
   if 57 - 57: iI11I1II1I1I * iI1ii11iIi1i * Ii1IIIi1 / oO0oo0o
def iIIiII1i1ii ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , Ii1i1iI in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + url , 7011 , Ii1i1iI )
 for url in next :
  oOo0 ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 57 - 57: O0OOOoOoo0 + ii1ii11IIIiiI
  if 49 - 49: OOooOOo * ii
def i1III ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oo000o0000oO )
 ooIII1II1iii1i = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'http' in url :
   OOOoOO ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in ooIII1II1iii1i :
  OOOoOO ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - oO0oo0o / Ii1I
  if 16 - 16: iI1ii11iIi1i
def Oo00O00o0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + iI1ii11iIi1i + oO0o
def o00o0o0oOo0 ( name , url , img ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IiI1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 iI1I1 = len ( IiI1 )
 if 5 - 5: ii1ii11IIIiiI % IIiIiII11i + I1ii11iIi11i - iI11I1II1I1I
 if 64 - 64: ii1ii11IIIiiI + iI11I1II1I1I
 if iI1I1 == 1 :
  for I1Iii in IiI1 :
   I1Iii = I1Iii . replace ( 'player' , 'watch' )
   iiIooo0o00o = I1Iii + '&fv=&sou='
   O0oOOo0 = O0i1II1Iiii1I11 ( iiIooo0o00o )
   oooOOOoO0O = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O0oOOo0 )
   for OOo0oOOOOooOo in oooOOOoO0O :
    iIOOO0O00 = False
    Resolve ( OOo0oOOOOooOo )
    if 54 - 54: o0o00Oo0O * oO0oo0o * iI1ii11iIi1i * oO0o % IIiIiII11i
 elif iI1I1 > 1 :
  if 46 - 46: O00o0O00 % oO0oo0o . I11i + Ii1IIIi1 % Ii + Ii1I
  for I1Iii in IiI1 :
   Iii1iI = O0i1II1Iiii1I11 ( I1Iii )
   OO00o0oo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Iii1iI )
   I1I1iiiiiIi1 = OO00o0oo
   I1I1iiiiiIi1 = ( str ( I1I1iiiiiIi1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + I1I1iiiiiIi1
   OOOoOO ( 'DOUBLE LINK' , I1I1iiiiiIi1 , 424 , '' )
   if 22 - 22: ooOOOoO . Ii1IIIi1 + I1ii11iIi11i
   for url in OO00o0oo :
    oOo0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     o0OO0o0o00o = Google . resolve ( url )
    except :
     pass
    try :
     IIIIiI1ii1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( o0OO0o0o00o ) )
     for ooOO0oo00Oo , i1I11I1i in IIIIiI1ii1 :
      if 100 - 100: oO0oo0o
      HD_URLS . append ( ooOO0oo00Oo )
      SD_URLS . append ( i1I11I1i )
    except :
     pass
 else :
  pass
  if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
def Ii1o0OOOoo0000 ( ) :
 if 19 - 19: ii . oOo0O0Ooo + ii1ii11IIIiiI - oOo0O0Ooo / oOo0O0Ooo % ooOOOoO
 if 4 - 4: Ii * Ii1I + ii - ooOOOoO . O0OOOoOoo0 . iI11I1II1I1I
 oOo0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 48 - 48: I11i * oO0oo0o . oOo0O0Ooo - ii1ii11IIIiiI + O00o0O00 . I1ii11iIi11i
 oOo0 ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 62 - 62: I11O0O0oOO00O00o + ii * iI11I1II1I1I / ooOoO0O00 * o0o00Oo0O
 if 10 - 10: iI11I1II1I1I * ii / O00o0O00
def III11iIII1 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://cnfstudio.com/' )
 IIi1I11I1II = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , 'http://cnfstudio.com/genre/' + i1I1ii11i1Iii , 7003 , III1iII1I1ii + 'icon.png' )
  if 4 - 4: Ii + ii / Ii . ii % Ii1I / OOooOOo
iI111I11I1I1 = xbmcgui . Dialog ( )
if 35 - 35: Ii1I % ooOoO0O00 + I11i - iI11I1II1I1I
II1i1III1IIiI = '{UN},' ; OoOI1iI1 = '{IG},' ; II11i1ii = '{PL},' ; oo0O0Oo0O = '{LO},' ; iIIO0O = '{LP},' ; o0o000Oo0ooOo = '{HA},' ; OoOo0000o0OOo = '{XD},' ; oo0o00oO00ooo = '{TA},' ; IIii1Ii = '{DP},' ; Oo0O0o = '{JT},' ; I111ii1III1I = '{JJ},' ; OO0o0oo = '{MM},' ; o0oo0oOOOo00 = '{FQ},' ; OO0OOO = '{HH},'
if 80 - 80: iI11I1II1I1I - I1ii11iIi11i % ii1ii11IIIiiI % I1ii11iIi11i + oOo0O0Ooo % iI1ii11iIi1i
def O00O00oO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oo000o0000oO )
 I11O0O0o = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oo000o0000oO )
 for Ii1i1iI , url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , Ii1i1iI )
 I11O0O0o = I11O0O0o
 for url in I11O0O0o :
  oOo0 ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 45 - 45: OOooOOo
def oo0OoOO000O ( url ) :
 if 62 - 62: ooOoO0O00 * iI11I1II1I1I % oO0oo0o % OOooOOo / ii
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOO00O = url + '&fv=&sou='
  OOO00O = OOO00O . replace ( 'player' , 'watch' )
  iI1111iiI1 = OOO0ooO0Oo0 ( OOO00O )
  oo000oOo0OoO0 = OOO0ooO0Oo0 ( url )
  if 28 - 28: O0OOOoOoo0 % ooOoO0O00 / oO0oo0o
  if 22 - 22: ooOoO0O00
def OOO0ooO0Oo0 ( url ) :
 if 3 - 3: oO0o * Ii1I - Ii1IIIi1 + Ii1I
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  O00OoOO0oo0 ( url )
  if 63 - 63: I11O0O0oOO00O00o * O0OOOoOoo0 % IIiIiII11i % ii1ii11IIIiiI + oOo0O0Ooo * I1ii11iIi11i
  if 96 - 96: ooOOOoO
def oo00OOo0 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , III1iII1I1ii + 'LocalM3U.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , III1iII1I1ii + 'RemoteM3U.png' , OO0o , '' )
 if 61 - 61: oO0oo0o % O0OOOoOoo0 - Ii1I + oO0oo0o . OOooOOo
def IIIi ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  I1i = open ( O0OoO000O0OO , 'r' )
  for Iii1iiIi1II1 in I1i :
   O00O000oOO0oO = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( Iii1iiIi1II1 )
   for oO00oooOOoOo0 , i1I1ii11i1Iii in O00O000oOO0oO :
    OOOoOO ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , III1iII1I1ii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 88 - 88: I11i . oOo0O0Ooo % oO0oo0o . I1ii11iIi11i % O0OOOoOoo0 . oO0oo0o
def OoO0ooOOoo ( url ) :
 if os . path . exists ( Remote ) :
  IIIi1I1IIii1II = iI1i111I1Ii ( url )
  IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , url in IIi1I11I1II :
   url = ( url ) . strip ( )
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 95 - 95: I1ii11iIi11i * O00o0O00 + oOo0O0Ooo . o0o00Oo0O
  if 36 - 36: OOooOOo * oO0o / O0OOOoOoo0 / oOo0O0Ooo - iI1ii11iIi1i
def IiI111111IIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'plugin.video.GenieTv'
 if 53 - 53: oO0oo0o
 oo0OoO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 3 - 3: ooOOOoO - ii * ii - oOo0O0Ooo / ii1ii11IIIiiI * Ii1I
def ooOOO00Ooo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'repository.GenieTv'
 if 58 - 58: ooOOOoO % iI11I1II1I1I / Ii % I11i . ii1ii11IIIiiI * Ii1IIIi1
 oo0OoO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 32 - 32: ii + I11i
 if 91 - 91: O0OOOoOoo0 - ii1ii11IIIiiI * ii1ii11IIIiiI
def ooOOOo0 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '' , 10051 , III1iII1I1ii + 'Catagories.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10052 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if 19 - 19: ii1ii11IIIiiI + Ii1IIIi1 * ii1ii11IIIiiI
 if 71 - 71: I11i . oOo0O0Ooo - Ii1I - I1ii11iIi11i - ooOoO0O00 - oOo0O0Ooo
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
iIIiiiIIi1111 = 'https://addons.tvaddons.ag/'
if 53 - 53: ii1ii11IIIiiI
def III1Iiii1i11 ( ) :
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 iII1 = 'https://addons.tvaddons.ag/search/?keyword=' + III1I1Iii1iiI
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( iII1 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , 10054 , 'https://addons.tvaddons.ag/' + i1i11I1I1iii1 , OO0o , '' )
  if 74 - 74: I1ii11iIi11i / ii1ii11IIIiiI % ii1ii11IIIiiI . ooOOOoO
  if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( iIIiiiIIi1111 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Repositories' in oO00oooOOoOo0 :
   pass
  elif 'Services' in oO00oooOOoOo0 :
   pass
  elif 'International' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10053 , 'https://addons.tvaddons.ag/' + Ii1i1iI , OO0o , '' )
   if 67 - 67: Ii1I + oO0oo0o * ooOOOoO / IIiIiII11i % oO0o % oO0o
   if 28 - 28: OOooOOo % oO0oo0o - O00o0O00 + O00o0O00 + oO0oo0o / iI11I1II1I1I
def Addon ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 oo0o = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Please' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIi1 ( oO00oooOOoOo0 , url , 10054 , 'https://addons.tvaddons.ag/' + Ii1i1iI , OO0o , '' )
 for url in oo0o :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , OO0o , '' )
  if 69 - 69: I11i + Ii1I / iI11I1II1I1I . ooOOOoO % Ii1I * OOooOOo
  if 13 - 13: iI11I1II1I1I + Ii1IIIi1 / iI1ii11iIi1i / ooOoO0O00 % oO0o - iI11I1II1I1I
def o0oooO0O00OoO ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   oo00ooOoo = os . path . join ( Ii1iI111 , name + '.zip' )
   try :
    os . remove ( oo00ooOoo )
   except :
    pass
   downloader . download ( url , oo00ooOoo , o0oOoO00o )
   OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OoOOoO0oOo
   print '======================================='
   extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
   Oo0o0O00 ( )
   if 40 - 40: IIiIiII11i
def oo0OoO ( url , name ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo00ooOoo = os . path . join ( Ii1iI111 , name + '.zip' )
 try :
  os . remove ( oo00ooOoo )
 except :
  pass
 downloader . download ( url , oo00ooOoo , o0oOoO00o )
 OoOOoO0oOo = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOoO0oOo
 print '======================================='
 extract . all ( oo00ooOoo , OoOOoO0oOo , o0oOoO00o )
 Oo0o0O00 ( )
 if 7 - 7: O00o0O00 / oO0o
def Oo0o0O00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 88 - 88: ooOoO0O00
 if 53 - 53: O0OOOoOoo0 . O00o0O00 . I11i + oO0oo0o
def IiiiII ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 1007 , i1i11I1I1iii1 )
def OoOo00OoOO00 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , i1i11I1I1iii1 )
  if 62 - 62: OOooOOo * ii * I11i
  if 37 - 37: oO0oo0o
def I1Ii1iI1IiI1I ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , iconimage , ooo0 , oOo0O , name in IIi1I11I1II :
  if 'http' in url :
   if '.php' in url :
    I11iI1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
    for Iii1iiIi1II1 in I11iI1I :
     if Iii1iiIi1II1 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    II1II1IIII ( name , url , 1016 , iconimage , oOo0O , ooo0 )
   else :
    if 'youtube' in url :
     I11iI1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for Iii1iiIi1II1 in I11iI1I :
      if Iii1iiIi1II1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O00o0O ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oOo0O , ooo0 )
    else :
     I11iI1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for Iii1iiIi1II1 in I11iI1I :
      if Iii1iiIi1II1 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O00o0O ( name , url , 222 , iconimage , oOo0O , ooo0 )
     I1I1II1I11 ( 'movies' , 'INFO' )
  else :
   o0OOOoO ( url , iconimage , name )
   if 73 - 73: ii / ii
 else :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
  for url , i1i11I1I1iii1 , name in IIi1I11I1II :
   if 'http' in url :
    if '.php' in url :
     oOo0 ( name , url , 1016 , i1i11I1I1iii1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OOOoOO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1i11I1I1iii1 )
     else :
      I11iI1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
      for Iii1iiIi1II1 in I11iI1I :
       if Iii1iiIi1II1 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOOoOO ( name , url , 222 , i1i11I1I1iii1 )
      I1I1II1I11 ( 'movies' , 'INFO' )
   else :
    o0OOOoO ( url , i1i11I1I1iii1 , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 88 - 88: ii1ii11IIIiiI - iI1ii11iIi1i - oO0oo0o + ooOoO0O00
def o0OOOoO ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ii11IiiIi = ( url ) . replace ( IIIIIIiIIIi1iii1 , 'http' ) . replace ( OoOooOo00o , '.com' ) ;
 II1IoOoO0oOO0o = ( ii11IiiIi ) . replace ( iii11III1I , 'a' ) . replace ( iIIi11i , 'b' ) . replace ( III , 'c' ) . replace ( o0o , 'd' ) . replace ( II11i1ii , 'e' ) . replace ( Oo0O0o , 'f' ) ;
 oO0000oo0o0o0 = ( II1IoOoO0oOO0o ) . replace ( o0O0O0O00o , 'g' ) . replace ( o0o000Oo0ooOo , 'h' ) . replace ( iI1IIi , 'i' ) . replace ( oo0o0O , 'j' ) . replace ( iiIi111Ii1II , 'k' ) . replace ( oOoo0oO , 'l' ) ;
 i1I1 = ( oO0000oo0o0o0 ) . replace ( O0ooO0o , 'm' ) . replace ( IiII1111I , 'n' ) . replace ( iiIIii111Ii , 'o' ) . replace ( OO000oooOo000 , 'p' ) . replace ( o0oO0o0Oo0 , 'q' ) . replace ( i1I1iiiI , 'r' ) ;
 i1IiIi1I1i = ( i1I1 ) . replace ( Ii11I1 , 's' ) . replace ( oOOoOoOO , 't' ) . replace ( OO00OO , 'u' ) . replace ( IiIiIi11iiIi1 , 'v' ) . replace ( OoOoO0O00oo , 'w' ) . replace ( ooo0o0oooo , 'x' ) ;
 o0OoIiiiiiiI111i = ( i1IiIi1I1i ) . replace ( iiIIIIiI11II1 , 'y' ) . replace ( IiI1i11i1iI , 'z' ) . replace ( II1i1III1IIiI , '.' ) . replace ( OoOI1iI1 , '(' ) . replace ( oo0O0Oo0O , ')' ) . replace ( iIIO0O , '/' ) ;
 o0oo0O0OO0 = ( o0OoIiiiiiiI111i ) . replace ( OOOOo0o0O0o , '1' ) . replace ( iII11 , '2' ) . replace ( IIiIi11I1Ii1Iiii1 , '3' ) . replace ( oo0o00oO00ooo , '4' ) . replace ( IIii1Ii , '5' ) . replace ( II11 , '6' ) ;
 o0oooOoOoOo = ( o0oo0O0OO0 ) . replace ( I111ii1III1I , '7' ) . replace ( OO0o0oo , '8' ) . replace ( o0oo0oOOOo00 , '9' ) . replace ( OO0OOO , '0' ) . replace ( OoO0o0OO , ':' ) . replace ( II11IiI1 , '%' ) ;
 url = ( o0oooOoOoOo ) . replace ( oOo000Oo00o , '-' ) . replace ( OoOo0000o0OOo , '_' ) ;
 OOOoOO ( name , url , 222 , iconimage ) ;
 if 96 - 96: OOooOOo / oO0o % ii * O0OOOoOoo0
 if 6 - 6: oOo0O0Ooo . IIiIiII11i + ii1ii11IIIiiI / oO0o % oOo0O0Ooo . ii
def Oooo000 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1007 , i1i11I1I1iii1 )
def IIii1i1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , i1i11I1I1iii1 )
  if 98 - 98: Ii1I - ii / oOo0O0Ooo . O0OOOoOoo0 - ooOoO0O00
def oOOoOo0OoOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OO00o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OO00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO00o )
 if 15 - 15: ooOoO0O00 . oOo0O0Ooo - OOooOOo % IIiIiII11i . O0OOOoOoo0 / oO0oo0o
 if 54 - 54: O0OOOoOoo0 - iI11I1II1I1I - I11O0O0oOO00O00o % iI1ii11iIi1i / IIiIiII11i
def oooooO0oO0o ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  if '-dir-' in oO00oooOOoOo0 :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , Ii1i1iI )
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , Ii1i1iI )
   if 63 - 63: iI1ii11iIi1i - IIiIiII11i . I11O0O0oOO00O00o / OOooOOo
def ii1IIi1IIIIi1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 iI1i1iii = ( 'http://afewbitsmore.com/' )
 IIi1I11I1II = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[To Parent Directory]' in oO00oooOOoOo0 :
   oO00oooOOoOo0 = 'HOME'
   pass
  elif 'HOME' in oO00oooOOoOo0 :
   pass
  elif '.m3u' in oO00oooOOoOo0 :
   oOo0 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , iI1i1iii + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iI1i1iii + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iI1i1iii + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , iI1i1iii + url , 1012 , III1iII1I1ii + 'music.png' )
def Ii11II1IIIIIi ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for Ii1i1iI , oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 83 - 83: iI11I1II1I1I + IIiIiII11i * oO0oo0o / o0o00Oo0O - Ii1IIIi1
def iii1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 iI1i1iii = url
 IIi1I11I1II = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp3' in oO00oooOOoOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/' , '' ) , iI1i1iii + url , 1011 , III1iII1I1ii + 'music.png' )
def o0o0O00OoOo ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , Ii1i1iI , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , ( 'http://www.cyn.net/music/' + i1I1ii11i1Iii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + Ii1i1iI ) . replace ( ' ' , '%20' ) )
def oOO0ooO00o ( url , img ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 img = img
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( o0OO0o0o00o + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 56 - 56: ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
def iIIIii111 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for type , url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[VID]' in type :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , o0OO0o0o00o + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   iIIIii111 ( o0OO0o0o00o + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: Ii1IIIi1 % ooOOOoO % I1ii11iIi11i % o0o00Oo0O
 if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
def III11II111 ( ) :
 o00oo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iI1I = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1I1Iii1iiI = iI1I . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 o0OO0o0o00o = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOO = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 8 - 8: Ii
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 O0 = ooOooo000oOO ( o0OO0o0o00o )
 ii1ii1ii = ooOooo000oOO ( oOO )
 if 4 - 4: Ii
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in IIi1I11I1II :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1ii11i1Iii + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 28 - 28: oO0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in OooOoooOo :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OO0o0o00o + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 73 - 73: I1ii11iIi11i . O0OOOoOoo0 - I1ii11iIi11i % O00o0O00 / Ii / iI11I1II1I1I
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  ooIII1II1iii1i = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in ooIII1II1iii1i :
   if iI1I in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOO + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 15 - 15: O0OOOoOoo0 * iI11I1II1I1I * oO0oo0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: ii1ii11IIIiiI * iI11I1II1I1I / OOooOOo % O00o0O00 * IIiIiII11i
    if 3 - 3: O00o0O00 . I1ii11iIi11i / Ii + oO0o
    if 47 - 47: ooOOOoO . O00o0O00
    if 96 - 96: I11O0O0oOO00O00o % IIiIiII11i / O0OOOoOoo0 % O00o0O00 / O0OOOoOoo0 % Ii
    if 57 - 57: I11O0O0oOO00O00o - I11O0O0oOO00O00o % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
    if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iI1ii11iIi1i * iI11I1II1I1I
O0ooO0o = '{SF},' ; IiII1111I = '{IF},' ; iiIIii111Ii = '{PW},' ; IIiIi11I1Ii1Iiii1 = '{AM},' ; OO000oooOo000 = '{GF},' ; o0oO0o0Oo0 = '{DD},' ; i1I1iiiI = '{UO},' ; Ii11I1 = '{LE},' ; OO00OO = '{ZY},' ; IiIiIi11iiIi1 = '{UE},' ; OoOoO0O00oo = '{PE},' ; ooo0o0oooo = '{JE},' ; iiIIIIiI11II1 = '{TH},' ; IiI1i11i1iI = '{LK},'
if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oO0oo0o * I11i + O00o0O00
if 89 - 89: O0OOOoOoo0 * oOo0O0Ooo . oO0oo0o
def O000O000 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.iwatchseries.me/tv-list/' )
 IIi1I11I1II = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8021 , III1iII1I1ii + 'iwatch.png' )
def OoO0000O ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , II1IOoOo000oOo0oo in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 + II1IOoOo000oOo0oo , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def I1I1iI ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IIIOo0O ( url )
def IIIOo0O ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oo000o0000oO )
 ooIII1II1iii1i = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( 'VidSpot - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in OooOoooOo :
  OOOoOO ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for oO00oooOOoOo0 , url in ooIII1II1iii1i :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OOOoOO ( 'TheVideo - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 11 - 11: o0o00Oo0O
def o0Oo0o ( ) :
 oo000o0000oO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi1I11I1II = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1021 , III1iII1I1ii + 'anime.png' )
  if 4 - 4: ii
  if 78 - 78: IIiIiII11i
def oO0oOo ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.animetoon.org/cartoon' )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1002 , III1iII1I1ii + 'anime.png' )
  if 43 - 43: oO0oo0o + OOooOOo . oOo0O0Ooo . Ii
  if 71 - 71: I11i + O00o0O00 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
  if 91 - 91: o0o00Oo0O - I11O0O0oOO00O00o % ii1ii11IIIiiI
def I1ii ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oo000o0000oO )
 for Ii1i1iI in OooOoooOo :
  iIi11i = Ii1i1iI
 ooIII1II1iii1i = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oo000o0000oO )
 for url in ooIII1II1iii1i :
  oOo0 ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 1003 , iIi11i )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOooOOOO0O0OoO0O0 ( url , IMAGE ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   iiii1i1 ( url )
  elif 'playpanda' in url :
   iiii1i1 ( url )
   if 81 - 81: Ii % oOo0O0Ooo / Ii1IIIi1 % oO0o / ii1ii11IIIiiI % iI11I1II1I1I
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiii1i1 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOOoOO ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 14 - 14: Ii1I * I1ii11iIi11i + Ii % O00o0O00 - oO0oo0o
  if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0oOOo . add_header ( 'referer' , url )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 58 - 58: O0OOOoOoo0 + IIiIiII11i + iI1ii11iIi1i . ii
def iI1i111I1Ii ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 42 - 42: iI11I1II1I1I / I11O0O0oOO00O00o . o0o00Oo0O . iI1ii11iIi1i
def Ii1i111iI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiiii111 = ( '%s%s' % ( oO0oo0o00o0O , url ) )
 OOO00O = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , i1i11I1I1iii1 , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '%s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i1i11I1I1iii1 )
  if 48 - 48: I1ii11iIi11i
def O00OoOO0oo0 ( url ) :
 if 64 - 64: iI11I1II1I1I % I11i . o0o00Oo0O * I11i
 O00O = open ( o0O , "a" )
 O00O . write ( 'url="' + url + '"\n' )
 O00O . close
 if 23 - 23: oO0o . ooOOOoO
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 try : I1IiiiIiI . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( oO00oooOOoOo0 ) )
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1IiiiIiI . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 79 - 79: O00o0O00
def o00oO00O0 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 o0oOoO00o . update ( 100 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 I1IiiiIiI . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 16 - 16: iI1ii11iIi1i / Ii + o0o00Oo0O . ooOOOoO
def IiIii1ii ( url ) :
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1IiiiIiI . play ( url ) . strip ( )
 except : pass
 if 15 - 15: I1ii11iIi11i + Ii1IIIi1 + oOo0O0Ooo * I11i
def iII1111IIIIiI ( url ) :
 I1IiiiIiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 IiiiiIi11 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 I1IiiiIiI . play ( IiiiiIi11 )
 xbmc . sleep ( 1 )
 I1IiiiIiI . play ( url )
 if 57 - 57: Ii1IIIi1 / oO0o - IIiIiII11i
 if 43 - 43: ooOOOoO % iI1ii11iIi1i . O00o0O00 / I1ii11iIi11i
def iiI1ii1IIiI ( ) :
 try :
  oOo00Oo00oO = getSet ( "core-player" )
  if ( oOo00Oo00oO == 'DVDPLAYER' ) : iiIIiIiOoo00O0OoOooO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOo00Oo00oO == 'MPLAYER' ) : iiIIiIiOoo00O0OoOooO = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOo00Oo00oO == 'PAPLAYER' ) : iiIIiIiOoo00O0OoOooO = xbmc . PLAYER_CORE_PAPLAYER
  else : iiIIiIiOoo00O0OoOooO = xbmc . PLAYER_CORE_AUTO
 except : iiIIiIiOoo00O0OoOooO = xbmc . PLAYER_CORE_AUTO
 return iiIIiIiOoo00O0OoOooO
 return True
 if 99 - 99: I1ii11iIi11i + ii . Ii1IIIi1 + o0o00Oo0O
def oOo0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oo000o0O = [ ]
  if showcontext == 'fav' :
   oo000o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   oo000o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OoOoooO000OO . addContextMenuItems ( oo000o0O )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = True )
 return oO0Oo00oo
 if 1 - 1: IIiIiII11i - ooOoO0O00 + oO0oo0o
def oO0Ooo0OooOOo ( name , url , mode , iconimage , fanart , description ) :
 if 58 - 58: Ii1IIIi1 - ii
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOoooO000OO . setProperty ( "Fanart_Image" , fanart )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = True )
 return oO0Oo00oo
 if 56 - 56: Ii1IIIi1 / Ii1IIIi1
def OOOoOO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oo000o0O = [ ]
  if showcontext == 'fav' :
   oo000o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   oo000o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OoOoooO000OO . addContextMenuItems ( oo000o0O )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = False )
 return oO0Oo00oo
 if 21 - 21: o0o00Oo0O * O0OOOoOoo0 % OOooOOo / o0o00Oo0O
 if 85 - 85: ii + ii
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / I11O0O0oOO00O00o . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - ooOOOoO
 if 50 - 50: oOo0O0Ooo - oO0oo0o + oO0oo0o * I11O0O0oOO00O00o + oO0oo0o
def O0O0Oooo0o ( heading , announce ) :
 class oooOoooOOo0 ( ) :
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
   try : o0Oo00 = open ( announce ) ; I1i111IiIiIi1 = o0Oo00 . read ( )
   except : I1i111IiIiIi1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1i111IiIiIi1 ) )
   return
 oooOoooOOo0 ( )
 oooOoooOOo0 ( )
 if 25 - 25: Ii1IIIi1 + oOo0O0Ooo + OOooOOo + ii1ii11IIIiiI % o0o00Oo0O
def i1Ii1I ( ) :
 O0O0Oooo0o ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 60 - 60: O0OOOoOoo0 * iI1ii11iIi1i + ii1ii11IIIiiI . O00o0O00 . o0o00Oo0O
 if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
 if 66 - 66: ii1ii11IIIiiI * I11i / ooOOOoO * Ii1IIIi1 / ii
 if 72 - 72: iI11I1II1I1I
 if 82 - 82: OOooOOo . iI1ii11iIi1i
def Oo0o0O00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 73 - 73: ii1ii11IIIiiI
 if 25 - 25: ooOOOoO
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . iI1ii11iIi1i - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oO0o - O0OOOoOoo0 - I1ii11iIi11i * oO0oo0o
 if 72 - 72: I11i % I11i + Ii1IIIi1 + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if 64 - 64: ooOOOoO
 if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
 if 89 - 89: o0o00Oo0O + ooOOOoO * ii1ii11IIIiiI
 if 30 - 30: OOooOOo
 if 39 - 39: Ii1I + I11i + ii1ii11IIIiiI + ooOOOoO
 if 48 - 48: ii1ii11IIIiiI / O0OOOoOoo0 . iI11I1II1I1I
 if 72 - 72: ooOoO0O00 . I11i
 if 3 - 3: OOooOOo % IIiIiII11i - o0o00Oo0O
 if 52 - 52: oO0o
 if 49 - 49: iI1ii11iIi1i . Ii1I % O0OOOoOoo0 . I1ii11iIi11i * O00o0O00
 if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OOOoOoo0
 if 20 - 20: Ii1IIIi1 + I11i . ii1ii11IIIiiI / Ii
 if 7 - 7: OOooOOo / OOooOOo . ii1ii11IIIiiI * o0o00Oo0O + ooOOOoO + oO0oo0o
 if 98 - 98: IIiIiII11i * ooOOOoO - oOo0O0Ooo % I11i - Ii1IIIi1 % Ii1I
 if 69 - 69: ooOoO0O00 % oO0o % ii1ii11IIIiiI / O0OOOoOoo0 / O0OOOoOoo0
 if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0OOOoOoo0
 if 47 - 47: o0o00Oo0O
def oOoooO0oo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + IIio0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 59 - 59: IIiIiII11i * ii - ii
def iioOo00O0o ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI11IIi1iiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 83 - 83: I1ii11iIi11i / O0OOOoOoo0
def II1iiIiI1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Ii1I11IIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 41 - 41: O0OOOoOoo0 / oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . Ii1I
def iii11I1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + i1II1iIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 20 - 20: Ii
def oOOOoo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI1i11II1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 61 - 61: I11O0O0oOO00O00o * iI1ii11iIi1i + I11O0O0oOO00O00o - I1ii11iIi11i % OOooOOo . Ii1IIIi1
def oO0OO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + OOO00O0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 76 - 76: oOo0O0Ooo
def II111IiiIIi ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0oooOOO00o0OOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 65 - 65: o0o00Oo0O - O0OOOoOoo0
def Iii1II1iI ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0oO0ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 31 - 31: o0o00Oo0O - ooOOOoO * Ii * ooOoO0O00
def O0oOo00Oo0oo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , Oo00OoOo , oOo0O , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 63 - 63: O0OOOoOoo0 % oOo0O0Ooo . O00o0O00 - O0OOOoOoo0 / I1ii11iIi11i % oOo0O0Ooo
def II1i11i1iI1I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oooOoO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , Oo00OoOo , oOo0O , oooOOoooo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , oooOOoooo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 42 - 42: ooOOOoO * Ii1IIIi1 . Ii1I - iI11I1II1I1I . O0OOOoOoo0 + I11O0O0oOO00O00o
 if 35 - 35: Ii1IIIi1 . oOo0O0Ooo / IIiIiII11i % ooOOOoO
 if 6 - 6: iI11I1II1I1I * IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
 if 8 - 8: Ii / O0OOOoOoo0
 if 33 - 33: ii1ii11IIIiiI * ooOOOoO - o0o00Oo0O + oOo0O0Ooo / ooOOOoO
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: ooOOOoO - I11i % O00o0O00 - IIiIiII11i
def o0o0OOooo0Oo ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( O00o0OO ) :
     iIiII1iI1Iii1i1 = 0
     iIiII1iI1Iii1i1 += len ( iI111i1I1II )
     if iIiII1iI1Iii1i1 > 0 :
      for o0Oo00 in iI111i1I1II :
       os . unlink ( os . path . join ( IiiiI111I , o0Oo00 ) )
  OoOo00oOoo0oO = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( OoOo00oOoo0oO )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 35 - 35: ii1ii11IIIiiI - ooOoO0O00 / ooOOOoO
 if 13 - 13: OOooOOo - oO0o * ii
 if 26 - 26: ii
 if 65 - 65: O00o0O00
 if 14 - 14: O0OOOoOoo0
 if 75 - 75: iI11I1II1I1I % O0OOOoOoo0 / O00o0O00 - Ii1IIIi1 % Ii
 if 11 - 11: I11O0O0oOO00O00o . iI1ii11iIi1i
 if 87 - 87: O00o0O00 + O00o0O00
def Oo00O0Oo0Oo ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
def ooO0oOOooOo0 ( url ) :
 OO0OoOo00 = os . path . join ( oO , 'addon_data' )
 Oooo = [
 ( OO0OoOo00 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OO0OoOo00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OO0OoOo00 , 'plugin.video.itv' , 'Images' ) ) ]
 if 18 - 18: iI1ii11iIi1i + OOooOOo . ooOoO0O00 / ooOOOoO / Ii1IIIi1
 oOo0OO0 = 0
 if 56 - 56: IIiIiII11i . IIiIiII11i + ooOOOoO . I11i
 for Iii1iiIi1II1 in Oooo :
  if os . path . exists ( Iii1iiIi1II1 ) and not Iii1iiIi1II1 in [ oOo0oooo00o , OO0OoOo00 ] :
   for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( Iii1iiIi1II1 ) :
    iIiII1iI1Iii1i1 = 0
    iIiII1iI1Iii1i1 += len ( iI111i1I1II )
    if iIiII1iI1Iii1i1 > 0 :
     for o0Oo00 in iI111i1I1II :
      if not o0Oo00 in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( IiiiI111I , o0Oo00 ) )
       except :
        pass
      else : oo00oOO000oO0 ( 'Ignore Log File: %s' % o0Oo00 )
     for II1Ii1iI1i1 in IIiiii :
      try :
       shutil . rmtree ( os . path . join ( IiiiI111I , II1Ii1iI1i1 ) )
       oOo0OO0 += 1
       oo00oOO000oO0 ( "[Success] cleared %s files from %s" % ( str ( iIiII1iI1Iii1i1 ) , os . path . join ( Iii1iiIi1II1 , II1Ii1iI1i1 ) ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( Iii1iiIi1II1 , II1Ii1iI1i1 ) )
  else :
   for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( Iii1iiIi1II1 ) :
    for II1Ii1iI1i1 in IIiiii :
     if 'cache' in II1Ii1iI1i1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( IiiiI111I , II1Ii1iI1i1 ) )
       oOo0OO0 += 1
       oo00oOO000oO0 ( "[Success] wiped %s " % os . path . join ( Iii1iiIi1II1 , II1Ii1iI1i1 ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( Iii1iiIi1II1 , II1Ii1iI1i1 ) )
       if 32 - 32: O0OOOoOoo0 . ooOOOoO . IIiIiII11i
 Oo00O0Oo0Oo ( oo0o0O00 , 'Clear Cache: Removed %s Files' % oOo0OO0 )
 if 25 - 25: ooOOOoO * ii1ii11IIIiiI - oO0oo0o * Ii * oOo0O0Ooo * O00o0O00
 if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % Ii1IIIi1
 if 59 - 59: O0OOOoOoo0 % I1ii11iIi11i - oO0oo0o + ooOOOoO
 if 33 - 33: iI1ii11iIi1i + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * ooOOOoO
 if 21 - 21: o0o00Oo0O * O0OOOoOoo0 % oO0o
 if 14 - 14: o0o00Oo0O / ii1ii11IIIiiI / O0OOOoOoo0 + ooOOOoO - ooOOOoO
 if 10 - 10: o0o00Oo0O - Ii1I / ii1ii11IIIiiI % OOooOOo / ii / iI1ii11iIi1i
def O000oOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o00Oo00O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( o00Oo00O0o ) :
   iIiII1iI1Iii1i1 = 0
   iIiII1iI1Iii1i1 += len ( iI111i1I1II )
   if 83 - 83: ii . Ii1IIIi1
   if 20 - 20: oO0o . oO0oo0o
   if iIiII1iI1Iii1i1 > 0 :
    if 4 - 4: I1ii11iIi11i % iI1ii11iIi1i % oO0o * Ii1IIIi1 % ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( iIiII1iI1Iii1i1 ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: ii . Ii1IIIi1
     for o0Oo00 in iI111i1I1II :
      os . unlink ( os . path . join ( IiiiI111I , o0Oo00 ) )
     for II1Ii1iI1i1 in IIiiii :
      shutil . rmtree ( os . path . join ( IiiiI111I , II1Ii1iI1i1 ) )
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
 if 43 - 43: ii
 if 8 - 8: O00o0O00 + I11O0O0oOO00O00o . I11O0O0oOO00O00o
 if 89 - 89: Ii1I * Ii1I * OOooOOo / Ii1IIIi1
 if 60 - 60: oO0o / Ii1IIIi1 / oOo0O0Ooo + oO0oo0o
 if 93 - 93: ii * iI1ii11iIi1i / o0o00Oo0O + iI1ii11iIi1i - iI11I1II1I1I
 if 6 - 6: ooOOOoO - I1ii11iIi11i - I11O0O0oOO00O00o - o0o00Oo0O % ii
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if 27 - 27: Ii % Ii1IIIi1 + iI1ii11iIi1i . O00o0O00
 if 9 - 9: oO0o
def oOo0OOoooO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o00Oo00O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( o00Oo00O0o ) :
   iIiII1iI1Iii1i1 = 0
   iIiII1iI1Iii1i1 += len ( iI111i1I1II )
   if 43 - 43: iI1ii11iIi1i . O00o0O00 + oOo0O0Ooo * Ii
   if 2 - 2: O00o0O00
   if iIiII1iI1Iii1i1 > 0 :
    if 3 - 3: oOo0O0Ooo . Ii1IIIi1 % o0o00Oo0O - O0OOOoOoo0 / o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( iIiII1iI1Iii1i1 ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: iI1ii11iIi1i + oO0oo0o % O0OOOoOoo0 % oOo0O0Ooo
     for o0Oo00 in iI111i1I1II :
      os . unlink ( os . path . join ( IiiiI111I , o0Oo00 ) )
     for II1Ii1iI1i1 in IIiiii :
      shutil . rmtree ( os . path . join ( IiiiI111I , II1Ii1iI1i1 ) )
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
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: Ii1IIIi1 . oO0oo0o / I1ii11iIi11i . oO0o . Ii
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: Ii1IIIi1 + I1ii11iIi11i % I11O0O0oOO00O00o . oO0oo0o
 if 6 - 6: ooOOOoO + Ii1I
 if 62 - 62: oO0oo0o . ii1ii11IIIiiI - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
 if 63 - 63: ii * ii1ii11IIIiiI
def II1Iiiii ( url , name ) :
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( Ii1iI111 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI1IOo0o = os . path . join ( Ii1iI111 , 'advancedsettings.xml.bak' )
 if os . path . exists ( iI1IOo0o ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoO00 = os . path . join ( Ii1iI111 , 'advancedsettings.xml' )
   try :
    os . remove ( OoO00 )
    print '=== GenieTv - REMOVING    ' + str ( OoO00 ) + '    ==='
   except :
    pass
   OOO00O = ii11iIi1I . http_GET ( url ) . content
   I1Ii = open ( OoO00 , "w" )
   I1Ii . write ( OOO00O )
   I1Ii . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoO00 = os . path . join ( Ii1iI111 , 'advancedsettings.xml' )
  try :
   os . remove ( OoO00 )
   print '=== GenieTv - REMOVING    ' + str ( OoO00 ) + '    ==='
  except :
   pass
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I1Ii = open ( OoO00 , "w" )
  I1Ii . write ( OOO00O )
  I1Ii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 88 - 88: O0OOOoOoo0 / I1ii11iIi11i + iI1ii11iIi1i % Ii * oO0o
def I1i11i ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( Ii1iI111 , 'advancedsettings.xml' )
 try :
  I1Ii = open ( OoO00 ) . read ( )
  if 'zero' in I1Ii :
   name = '0CACHE'
  elif 'tuxen' in I1Ii :
   name = 'TUXENS'
  elif 'muckys' in I1Ii :
   name = 'MUCKYS'
  elif 'p2p1' in I1Ii :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in I1Ii :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in I1Ii :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 9 - 9: IIiIiII11i + Ii1I / Ii1IIIi1
def O0OOOo0o0O0 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( Ii1iI111 , 'advancedsettings.xml' )
 try :
  os . remove ( OoO00 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 7 - 7: O00o0O00 . ooOOOoO . ii1ii11IIIiiI / iI1ii11iIi1i / I1ii11iIi11i
 if 83 - 83: I11O0O0oOO00O00o / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
 if 10 - 10: I11O0O0oOO00O00o - I11i % ii - Ii1I
 if 64 - 64: oO0o / oOo0O0Ooo
 if 23 - 23: I11O0O0oOO00O00o * ii1ii11IIIiiI * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: ooOOOoO * ii . O0OOOoOoo0 % Ii
 if 11 - 11: iI11I1II1I1I . ii1ii11IIIiiI - I1ii11iIi11i / I11O0O0oOO00O00o + IIiIiII11i
 if 29 - 29: I11O0O0oOO00O00o . Ii + ooOoO0O00 - iI1ii11iIi1i + o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: I11i
def ooOO0O0O ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi1I11I1II = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for IIIiIIIi111iI , II1IIII1i1i , IiIiI1i1ii , iiii1I1IiI in IIi1I11I1II :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IIIiIIIi111iI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IiIiI1i1ii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iiii1I1IiI )
  inc = inc + 1
  if 49 - 49: Ii1I + oO0oo0o * Ii1IIIi1 * O0OOOoOoo0 / oOo0O0Ooo . Ii1I
  if 80 - 80: oOo0O0Ooo % ooOOOoO / I11O0O0oOO00O00o * oO0o - oO0oo0o / oO0oo0o
  if 13 - 13: I1ii11iIi11i
  if 70 - 70: Ii1IIIi1
  if 51 - 51: o0o00Oo0O - Ii1I / I11O0O0oOO00O00o * IIiIiII11i + oO0o % Ii1I
  if 58 - 58: oO0oo0o + ooOOOoO % Ii1IIIi1 - iI1ii11iIi1i - O00o0O00 % iI1ii11iIi1i
  if 86 - 86: I11i
  if 15 - 15: oO0oo0o - iI11I1II1I1I - IIiIiII11i - ooOOOoO % Ii1I
  if 80 - 80: ooOOOoO * Ii1IIIi1 . ooOoO0O00 % iI1ii11iIi1i % Ii1I + O0OOOoOoo0
def IIII1IiiI ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoO00 = os . path . join ( Ii1iI111 , 'addons2.ini' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I1Ii = open ( OoO00 , "w" )
  I1Ii . write ( OOO00O )
  I1Ii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 100 - 100: oOo0O0Ooo - O00o0O00
def OOOOo0ooOOO0 ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  Ii1iI111 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoO00 = os . path . join ( Ii1iI111 , 'settings.xml' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  I1Ii = open ( OoO00 , "w" )
  I1Ii . write ( OOO00O )
  I1Ii . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 91 - 91: Ii + iI1ii11iIi1i % iI1ii11iIi1i + I11i
 if 15 - 15: Ii1I . oOo0O0Ooo - ii1ii11IIIiiI - ooOoO0O00
def O00OO0o0 ( ) :
 try :
  oO0o00o0o0OO0O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oO0o00o0o0OO0O0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IiiiI1 = os . path . join ( oO0o00o0o0OO0O0 , "source.db" )
    os . unlink ( IiiiI1 )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 83 - 83: ii1ii11IIIiiI
 if 38 - 38: oO0oo0o
 if 9 - 9: I11O0O0oOO00O00o . oO0o . oO0oo0o / ii
 if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
 if 2 - 2: IIiIiII11i + I11O0O0oOO00O00o . oO0o
def O0i1II1Iiii1I11 ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 14 - 14: O00o0O00 * oOo0O0Ooo - Ii1I
 if 10 - 10: Ii1IIIi1 % ii1ii11IIIiiI * Ii1I * o0o00Oo0O * Ii % ii1ii11IIIiiI
 if 68 - 68: ii * OOooOOo
 if 9 - 9: ii1ii11IIIiiI
 if 36 - 36: ii1ii11IIIiiI / OOooOOo + OOooOOo * O0OOOoOoo0 / O00o0O00 * o0o00Oo0O
 if 17 - 17: oO0o / O0OOOoOoo0 % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def OOo0iIiiI11II11 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; o0o0O00O = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if o0o0O00O :
  oO0oO0OoO00 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oO0oO0OoO00 = xbmc . translatePath ( oO0oO0OoO00 ) ;
  Oo0ooo00o0O0 = os . path . join ( oO0oO0OoO00 , ".." , ".." ) ; Oo0ooo00o0O0 = os . path . abspath ( Oo0ooo00o0O0 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + Oo0ooo00o0O0 ) ; II1I1iI1i1IiI = False
  try :
   for IiiiI111I , IIiiii , iI111i1I1II in os . walk ( Oo0ooo00o0O0 , topdown = True ) :
    IIiiii [ : ] = [ II1Ii1iI1i1 for II1Ii1iI1i1 in IIiiii if II1Ii1iI1i1 not in o0oO0 ]
    for oO00oooOOoOo0 in iI111i1I1II :
     try : os . remove ( os . path . join ( IiiiI111I , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : II1I1iI1i1IiI = True
      plugintools . log ( "Error removing " + IiiiI111I + " " + oO00oooOOoOo0 )
    for oO00oooOOoOo0 in IIiiii :
     try : os . rmdir ( os . path . join ( IiiiI111I , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Database" , "userdata" ] : II1I1iI1i1IiI = True
      plugintools . log ( "Error removing " + IiiiI111I + " " + oO00oooOOoOo0 )
   if not II1I1iI1i1IiI : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iIi1iIIIiIiI ( )
 if 9 - 9: oO0oo0o / ii / O00o0O00 * Ii - O0OOOoOoo0 + ii1ii11IIIiiI
 if 69 - 69: o0o00Oo0O . ii1ii11IIIiiI - o0o00Oo0O
 if 58 - 58: OOooOOo + Ii1I
def IiIIiIii1ii ( ) :
 III1I1Iii1 = [ ]
 IIIiIII1 = sys . argv [ 2 ]
 if len ( IIIiIII1 ) >= 2 :
  OOo0OOo = sys . argv [ 2 ]
  OOIiI1IIIiI1I1i = OOo0OOo . replace ( '?' , '' )
  if ( OOo0OOo [ len ( OOo0OOo ) - 1 ] == '/' ) :
   OOo0OOo = OOo0OOo [ 0 : len ( OOo0OOo ) - 2 ]
  oO00O0oO = OOIiI1IIIiI1I1i . split ( '&' )
  III1I1Iii1 = { }
  for Oo0000 in range ( len ( oO00O0oO ) ) :
   O00O00IIi1i = { }
   O00O00IIi1i = oO00O0oO [ Oo0000 ] . split ( '=' )
   if ( len ( O00O00IIi1i ) ) == 2 :
    III1I1Iii1 [ O00O00IIi1i [ 0 ] ] = O00O00IIi1i [ 1 ]
    if 90 - 90: ooOOOoO % IIiIiII11i
 return III1I1Iii1
 if 19 - 19: I1ii11iIi11i + Ii1IIIi1 . ii - ooOoO0O00
O000o0O0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
IiIi1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1i111i1I1 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1IIo0o0OoOO00Oo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oo0OoOooo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i1iiIi1II1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IIio0O0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiI1Iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iI11IIi1iiI1I = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Ii1I11IIi1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
i1II1iIii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iI1i11II1i1i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OOO00O0OO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0oooOOO00o0OOO00 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o0oO0ooo0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i111 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
oo0O = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
ooOoo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
Ii1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
II1i111 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iI111I11i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iIIi1I1ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oooOoO00O = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oO0oo0o00o0O = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOoooO000OO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oo000o0O = [ ]
  if showcontext == 'fav' :
   oo000o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   oo000o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OoOoooO000OO . addContextMenuItems ( oo000o0O )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = True )
 return oO0Oo00oo
 if 11 - 11: ooOOOoO + OOooOOo % I11i * oO0o / ooOOOoO
def iIiIIi1 ( name , url , mode , iconimage , fanart , description ) :
 IiIi = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Oo00oo = True
 OoOoooO000OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OoOoooO000OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OoOoooO000OO . setProperty ( "Fanart_Image" , fanart )
 oO0Oo00oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIi , listitem = OoOoooO000OO , isFolder = False )
 return oO0Oo00oo
 if 5 - 5: Ii1IIIi1 / oO0oo0o % O0OOOoOoo0 . Ii % OOooOOo + oO0oo0o
 if 95 - 95: Ii1I
OOo0OOo = IiIIiIii1ii ( )
i1I1ii11i1Iii = None
oO00oooOOoOo0 = None
oo000o = None
Oo00OoOo = None
oOo0O = None
oooOOoooo = None
iiIii1I1Ii = None
if 14 - 14: Ii1IIIi1 % oO0o
if 6 - 6: I11i % iI1ii11iIi1i
try :
 iiIii1I1Ii = int ( OOo0OOo [ "fav_mode" ] )
except :
 pass
 if 45 - 45: ii / oOo0O0Ooo + oOo0O0Ooo
try :
 i1I1ii11i1Iii = urllib . unquote_plus ( OOo0OOo [ "url" ] )
except :
 pass
try :
 oO00oooOOoOo0 = urllib . unquote_plus ( OOo0OOo [ "name" ] )
except :
 pass
try :
 Oo00OoOo = urllib . unquote_plus ( OOo0OOo [ "iconimage" ] )
except :
 pass
try :
 oo000o = int ( OOo0OOo [ "mode" ] )
except :
 pass
try :
 oOo0O = urllib . unquote_plus ( OOo0OOo [ "fanart" ] )
except :
 pass
try :
 oooOOoooo = urllib . unquote_plus ( OOo0OOo [ "description" ] )
except :
 pass
 if 75 - 75: oOo0O0Ooo - O0OOOoOoo0 - oOo0O0Ooo % oO0oo0o % ii
 if 13 - 13: O0OOOoOoo0 * oO0o % iI11I1II1I1I / ooOOOoO * Ii1IIIi1 . I1ii11iIi11i
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oo000o )
print "URL: " + str ( i1I1ii11i1Iii )
print "Name: " + str ( oO00oooOOoOo0 )
print "IconImage: " + str ( Oo00OoOo )
if 23 - 23: O0OOOoOoo0 / ooOOOoO . Ii1IIIi1 * iI1ii11iIi1i
if 87 - 87: Ii
def I1I1II1I11 ( content , viewType ) :
 if 34 - 34: ooOoO0O00
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 64 - 64: iI11I1II1I1I / ooOOOoO / I1ii11iIi11i - Ii1I
if Oo00OoOo == None : Oo00OoOo = Ooo
if oOo0O == None : oOo0O = OO0o
if oo000o == None :
 I11IiI ( )
 if 100 - 100: ooOOOoO + ooOoO0O00 * oO0o
elif oo000o == 1 :
 i111i1iIiiIiI ( i1I1ii11i1Iii )
 if 64 - 64: oO0oo0o * Ii . I1ii11iIi11i
elif oo000o == 44 :
 IiIiIi1I1 ( i1I1ii11i1Iii )
 if 52 - 52: I1ii11iIi11i / O0OOOoOoo0 / Ii1IIIi1 - I11i / Ii1IIIi1
elif oo000o == 2 :
 o0oO0OoO0 ( )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif oo000o == 3 :
 OO0OO0OO ( )
 if 85 - 85: oOo0O0Ooo
elif oo000o == 21 :
 i1i1II ( )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif oo000o == 4 :
 oO0oO00oOo0OOO ( )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif oo000o == 5 :
 I1i1ii1IiIii ( i1I1ii11i1Iii )
 if 46 - 46: OOooOOo * I11O0O0oOO00O00o / oO0oo0o + I1ii11iIi11i + ooOOOoO
elif oo000o == 6 :
 O000oOo ( i1I1ii11i1Iii )
 if 95 - 95: I11i - iI1ii11iIi1i
elif oo000o == 7 :
 II1Iiiii ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif oo000o == 8 :
 I1i11i ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 19 - 19: OOooOOo . O00o0O00 . ii
elif oo000o == 9 :
 FIXREPOSADDONS ( i1I1ii11i1Iii )
 if 79 - 79: O00o0O00 * O0OOOoOoo0 * oOo0O0Ooo * Ii1I / Ii1I
elif oo000o == 10 :
 Oo0o0O00 ( )
 if 62 - 62: O0OOOoOoo0 * iI1ii11iIi1i % Ii1I - ooOoO0O00 - Ii1I
elif oo000o == 11 :
 O0OOOo0o0O0 ( i1I1ii11i1Iii )
 if 24 - 24: O00o0O00
elif oo000o == 12 :
 ooOO0O0O ( )
 if 71 - 71: ooOOOoO - ooOoO0O00
elif oo000o == 13 :
 o0o0OOooo0Oo ( )
 if 56 - 56: OOooOOo + oO0oo0o
elif oo000o == 14 :
 ooO0oOOooOo0 ( i1I1ii11i1Iii )
 if 74 - 74: Ii1IIIi1 / ii1ii11IIIiiI / IIiIiII11i - Ii1IIIi1 / oO0oo0o % I11O0O0oOO00O00o
elif oo000o == 15 :
 o0OO000ooOo ( )
 if 19 - 19: ooOOOoO % ii + ii
elif oo000o == 16 :
 IIII1IiiI ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 7 - 7: ooOoO0O00
elif oo000o == 17 :
 OOOOo0ooOOO0 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 91 - 91: OOooOOo - OOooOOo . ooOOOoO
elif oo000o == 18 :
 O00OO0o0 ( )
 if 33 - 33: ii1ii11IIIiiI - iI11I1II1I1I / iI1ii11iIi1i % o0o00Oo0O
elif oo000o == 19 :
 I1iI1I1 ( i1I1ii11i1Iii )
 if 80 - 80: ooOOOoO % ii - ooOOOoO
elif oo000o == 40 :
 i1iiI ( oO00oooOOoOo0 , i1I1ii11i1Iii , oooOOoooo )
 if 27 - 27: ii1ii11IIIiiI - I11i * Ii1I - oOo0O0Ooo
elif oo000o == 42 :
 iIIIiIi1I1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , oooOOoooo )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - Ii1IIIi1 . iI1ii11iIi1i
elif oo000o == 43 :
 oooO00o0 ( i1I1ii11i1Iii )
 if 100 - 100: IIiIiII11i / ii1ii11IIIiiI / Ii1IIIi1 - Ii1I * iI11I1II1I1I
elif oo000o == 20 :
 iii1IIII1iii11I ( i1I1ii11i1Iii )
 if 7 - 7: ooOoO0O00 . ooOOOoO % Ii * Ii1I . I11O0O0oOO00O00o % Ii1I
elif oo000o == 22 :
 oOoooO0oo0 ( i1I1ii11i1Iii )
 if 35 - 35: oOo0O0Ooo
elif oo000o == 23 :
 iioOo00O0o ( i1I1ii11i1Iii )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif oo000o == 24 :
 II1iiIiI1 ( i1I1ii11i1Iii )
 if 22 - 22: O0OOOoOoo0 . Ii . ii . ooOoO0O00
elif oo000o == 25 :
 iii11I1 ( i1I1ii11i1Iii )
 if 12 - 12: OOooOOo % O00o0O00 + oO0oo0o . o0o00Oo0O % iI11I1II1I1I
elif oo000o == 26 :
 oOOOoo0 ( i1I1ii11i1Iii )
 if 41 - 41: ii
elif oo000o == 27 :
 oO0OO ( i1I1ii11i1Iii )
 if 13 - 13: I11O0O0oOO00O00o + ii1ii11IIIiiI - ii1ii11IIIiiI % oO0oo0o / I11O0O0oOO00O00o
elif oo000o == 28 :
 II111IiiIIi ( i1I1ii11i1Iii )
 if 4 - 4: oOo0O0Ooo + O00o0O00 - ooOOOoO + Ii1IIIi1
elif oo000o == 29 :
 Iii1II1iI ( i1I1ii11i1Iii )
 if 78 - 78: iI1ii11iIi1i
elif oo000o == 30 :
 II1II ( i1I1ii11i1Iii )
 if 29 - 29: IIiIiII11i
elif oo000o == 31 :
 O0oOo00Oo0oo0 ( i1I1ii11i1Iii )
 if 79 - 79: iI11I1II1I1I - Ii + O0OOOoOoo0 - IIiIiII11i . iI11I1II1I1I
elif oo000o == 32 :
 i11I1I1iiI ( )
 if 84 - 84: I1ii11iIi11i % I11O0O0oOO00O00o * o0o00Oo0O * I11O0O0oOO00O00o
elif oo000o == 33 :
 oOoooO0 ( )
 if 66 - 66: O00o0O00 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OOOoOoo0
elif oo000o == 35 :
 IIii1 ( i1I1ii11i1Iii )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif oo000o == 34 :
 i11Ii1I1I11I ( i1I1ii11i1Iii )
 if 37 - 37: ooOoO0O00 * Ii
elif oo000o == 36 :
 Ii11 ( i1I1ii11i1Iii )
 if 95 - 95: Ii % ii1ii11IIIiiI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif oo000o == 37 :
 iii11II1I ( i1I1ii11i1Iii )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / O00o0O00 / ii1ii11IIIiiI
elif oo000o == 38 :
 II1iiIiIiI ( i1I1ii11i1Iii )
 if 35 - 35: Ii1IIIi1 * O00o0O00
elif oo000o == 41 :
 OOo0iIiiI11II11 ( OOo0OOo )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif oo000o == 39 :
 II1i11i1iI1I ( i1I1ii11i1Iii )
 if 13 - 13: oO0o * ii1ii11IIIiiI + I1ii11iIi11i - ooOOOoO
elif oo000o == 45 :
 TEXTS ( )
 if 31 - 31: oO0o
elif oo000o == 46 :
 i1Ii1I ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif oo000o == 47 :
 GEVID ( )
 if 77 - 77: Ii - ii1ii11IIIiiI . Ii1I % I1ii11iIi11i . iI1ii11iIi1i
elif oo000o == 48 :
 I1I1iII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , oooOOoooo )
 if 9 - 9: I11i
elif oo000o == 49 :
 iIi1IiI ( )
 if 55 - 55: O00o0O00 % iI11I1II1I1I + I11O0O0oOO00O00o . O0OOOoOoo0
elif oo000o == 222 :
 O00OoOO0oo0 ( i1I1ii11i1Iii )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif oo000o == 333 :
 Ii1i111iI ( i1I1ii11i1Iii )
 if 23 - 23: Ii
 if 88 - 88: IIiIiII11i - Ii1IIIi1 / ii
elif oo000o == 1020 :
 o0Oo0o ( )
 if 71 - 71: Ii1I
elif oo000o == 1021 :
 ANIMEEP ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif oo000o == 1022 :
 ANIMEPLAY ( i1I1ii11i1Iii )
 if 1 - 1: ooOOOoO % ooOoO0O00
elif oo000o == 1001 :
 oO0oOo ( )
 if 41 - 41: oO0o * oO0o / Ii1IIIi1 + Ii1I . I11i
elif oo000o == 1005 :
 Oooo000 ( )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / iI1ii11iIi1i
elif oo000o == 1007 :
 IIii1i1 ( i1I1ii11i1Iii )
 if 80 - 80: Ii1I
elif oo000o == 1010 :
 oooooO0oO0o ( i1I1ii11i1Iii )
 if 67 - 67: IIiIiII11i
elif oo000o == 1011 :
 iii1 ( i1I1ii11i1Iii )
 if 2 - 2: I11i - o0o00Oo0O * iI1ii11iIi1i % ooOOOoO
elif oo000o == 1012 :
 ii1IIi1IIIIi1 ( i1I1ii11i1Iii )
 if 64 - 64: ooOoO0O00 . O0OOOoOoo0
elif oo000o == 1030 :
 o0o0O00OoOo ( )
 if 7 - 7: oO0oo0o . Ii1IIIi1 - Ii1IIIi1 / ii1ii11IIIiiI % I1ii11iIi11i
elif oo000o == 1031 :
 oOO0ooO00o ( i1I1ii11i1Iii , Oo00OoOo )
 if 61 - 61: oO0oo0o - Ii1I / Ii1IIIi1 % Ii1I + oO0o / I1ii11iIi11i
elif oo000o == 1032 :
 iIIIii111 ( i1I1ii11i1Iii )
 if 10 - 10: Ii / OOooOOo
elif oo000o == 1006 :
 Parse . ParseURL ( i1I1ii11i1Iii )
 if 27 - 27: oOo0O0Ooo / ii
elif oo000o == 2030 :
 Parse . addonParseURL ( i1I1ii11i1Iii )
 if 74 - 74: Ii1I % ii1ii11IIIiiI - oO0o * I11O0O0oOO00O00o . ii * oO0o
elif oo000o == 2031 :
 Parse . apkParseURL ( i1I1ii11i1Iii )
 if 99 - 99: OOooOOo . Ii1IIIi1 - ii - o0o00Oo0O
elif oo000o == 1002 :
 I1ii ( i1I1ii11i1Iii )
 if 6 - 6: O00o0O00
elif oo000o == 1003 :
 OOooOOOO0O0OoO0O0 ( i1I1ii11i1Iii , Oo00OoOo )
 if 3 - 3: o0o00Oo0O - ii1ii11IIIiiI * iI1ii11iIi1i * O00o0O00 / iI1ii11iIi1i
elif oo000o == 1004 :
 iiii1i1 ( i1I1ii11i1Iii )
 if 58 - 58: iI1ii11iIi1i * iI11I1II1I1I + O0OOOoOoo0 . O0OOOoOoo0
elif oo000o == 1008 :
 oooIi1i ( )
 if 74 - 74: O0OOOoOoo0 - I11i * ooOOOoO % O0OOOoOoo0
elif oo000o == 1009 :
 OoO0ooOOoo ( i1I1ii11i1Iii )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * ii1ii11IIIiiI - oO0o - I11i
elif oo000o == 2001 :
 IIIi ( )
 if 44 - 44: ii
elif oo000o == 2002 :
 Ii11II1IIIIIi ( i1I1ii11i1Iii )
 if 82 - 82: OOooOOo . OOooOOo
elif oo000o == 1013 :
 o00Ooo0 ( )
elif oo000o == 10111113 :
 O0O00O ( i1I1ii11i1Iii )
 if 10 - 10: I1ii11iIi11i * Ii1I . oO0oo0o . ii . O00o0O00 * Ii1I
elif oo000o == 1014 :
 oooO00oo0 ( )
 if 80 - 80: ii1ii11IIIiiI + I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00
elif oo000o == 1015 :
 o000 ( i1I1ii11i1Iii )
 if 85 - 85: Ii . I11O0O0oOO00O00o + iI1ii11iIi1i / iI1ii11iIi1i
elif oo000o == 1016 :
 I1Ii1iI1IiI1I ( i1I1ii11i1Iii , Oo00OoOo , oO00oooOOoOo0 )
 if 43 - 43: ooOOOoO . ii - IIiIiII11i
elif oo000o == 1017 :
 iI1II ( )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O00o0O00 * oO0oo0o
elif oo000o == 1018 :
 iiIi11iI1iii ( i1I1ii11i1Iii )
 if 19 - 19: ii1ii11IIIiiI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif oo000o == 1023 :
 o0oo ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif oo000o == 1024 :
 IiiiII ( i1I1ii11i1Iii )
 if 15 - 15: iI1ii11iIi1i + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif oo000o == 1025 :
 OoOo00OoOO00 ( i1I1ii11i1Iii )
 if 54 - 54: ooOOOoO - IIiIiII11i . O0OOOoOoo0 + iI1ii11iIi1i
elif oo000o == 4001 :
 oo0O0 ( )
 if 45 - 45: oO0oo0o + IIiIiII11i . Ii1IIIi1 / Ii1I
elif oo000o == 4002 :
 O000OOO ( )
 if 76 - 76: iI1ii11iIi1i + Ii1IIIi1 - ooOOOoO * iI11I1II1I1I % ooOoO0O00
elif oo000o == 4003 :
 oO00OoOO ( )
 if 72 - 72: O0OOOoOoo0 + IIiIiII11i . o0o00Oo0O - Ii1IIIi1 / ii . ii1ii11IIIiiI
elif oo000o == 4004 :
 I1II1 ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif oo000o == 4005 :
 Iii11iI1i ( )
 if 32 - 32: ii
elif oo000o == 4006 :
 o0O0OOOOoOO0 ( )
 if 29 - 29: Ii1I
elif oo000o == 4007 :
 ii1I1IIii11 ( )
 if 41 - 41: iI1ii11iIi1i
elif oo000o == 4008 :
 O0o0oO ( )
 if 49 - 49: iI1ii11iIi1i % IIiIiII11i . iI1ii11iIi1i - I11i - I11O0O0oOO00O00o * ooOOOoO
elif oo000o == 4009 : oooO ( )
elif oo000o == 4010 : iIIii ( )
elif oo000o == 3000 :
 oo00OOo0 ( )
 if 47 - 47: o0o00Oo0O . I11i / iI1ii11iIi1i * Ii1IIIi1
elif oo000o == 3001 :
 iIiO0O ( )
 if 63 - 63: ii1ii11IIIiiI - oO0oo0o - Ii1IIIi1 - O0OOOoOoo0 / oO0oo0o + oO0o
elif oo000o == 3002 :
 oOOoooo ( i1I1ii11i1Iii )
 if 94 - 94: ooOOOoO / oOo0O0Ooo . IIiIiII11i
elif oo000o == 3003 :
 O0oIi1iIiIi1I11 ( i1I1ii11i1Iii )
 if 32 - 32: oO0oo0o . O00o0O00 % O00o0O00 . OOooOOo
elif oo000o == 3004 :
 OOO0 ( i1I1ii11i1Iii )
 if 37 - 37: O00o0O00 + o0o00Oo0O + O00o0O00 . Ii1IIIi1 . I11i
elif oo000o == 404 :
 oOOoOo0OoOO ( oO00oooOOoOo0 , i1I1ii11i1Iii , Oo00OoOo )
 if 78 - 78: oOo0O0Ooo / I11O0O0oOO00O00o + I11i . I1ii11iIi11i / o0o00Oo0O
elif oo000o == 405 :
 o00oO00O0 ( i1I1ii11i1Iii )
 if 49 - 49: Ii1I
elif oo000o == 7030 :
 iioo ( )
 if 66 - 66: I11i . Ii1I
elif oo000o == 7021 :
 I11IIiI1IiI1 ( oO00oooOOoOo0 )
 if 18 - 18: I1ii11iIi11i + ooOOOoO
elif oo000o == 7022 :
 iIiIiiIIIi1 ( oO00oooOOoOo0 )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % iI1ii11iIi1i . oOo0O0Ooo
elif oo000o == 7000 :
 o00o0o0oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , img )
 if 43 - 43: oOo0O0Ooo % Ii1I * iI1ii11iIi1i
elif oo000o == 7050 :
 I1I1 ( i1I1ii11i1Iii )
 if 31 - 31: iI1ii11iIi1i / Ii1IIIi1
elif oo000o == 7051 :
 ooOooOooOOO ( i1I1ii11i1Iii )
 if 3 - 3: ooOOOoO
elif oo000o == 7052 :
 I1ii1i11iI1 ( i1I1ii11i1Iii )
 if 37 - 37: iI1ii11iIi1i * ii * I11O0O0oOO00O00o + I1ii11iIi11i . oOo0O0Ooo
elif oo000o == 7053 :
 IiOOo0 ( i1I1ii11i1Iii )
 if 61 - 61: O00o0O00 . O00o0O00
elif oo000o == 7054 :
 CoolPlay ( i1I1ii11i1Iii )
 if 17 - 17: IIiIiII11i / O0OOOoOoo0
elif oo000o == 7060 :
 o0000oO ( )
 if 80 - 80: O00o0O00 * oO0o + iI1ii11iIi1i
elif oo000o == 7061 :
 Iii1I ( i1I1ii11i1Iii )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif oo000o == 7063 :
 ooo0oo ( i1I1ii11i1Iii )
 if 98 - 98: I11i * I1ii11iIi11i - iI1ii11iIi1i . O0OOOoOoo0
elif oo000o == 7062 :
 O00OO00OOOoO ( i1I1ii11i1Iii )
 if 2 - 2: I1ii11iIi11i - O0OOOoOoo0 % iI11I1II1I1I
elif oo000o == 7064 :
 NATatozcat ( )
 if 88 - 88: ii1ii11IIIiiI - oO0o
elif oo000o == 7067 :
 IiI11Ii1iI ( i1I1ii11i1Iii )
 if 79 - 79: Ii1IIIi1
elif oo000o == 7066 :
 NATatozA ( i1I1ii11i1Iii )
 if 45 - 45: IIiIiII11i + Ii1IIIi1 . I11O0O0oOO00O00o . o0o00Oo0O * ooOoO0O00 - iI1ii11iIi1i
elif oo000o == 7065 :
 ooOo0 ( i1I1ii11i1Iii )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif oo000o == 7070 :
 oOo00 ( )
 if 76 - 76: Ii1I
elif oo000o == 7071 :
 DIZIlist ( i1I1ii11i1Iii )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . iI1ii11iIi1i
elif oo000o == 7072 :
 DIZIpull ( i1I1ii11i1Iii )
 if 51 - 51: iI1ii11iIi1i + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif oo000o == 7073 :
 WATCHDIZI ( i1I1ii11i1Iii )
 if 20 - 20: ii1ii11IIIiiI . I11O0O0oOO00O00o . iI1ii11iIi1i + I11O0O0oOO00O00o - O00o0O00 * oO0oo0o
elif oo000o == 7002 :
 III11iIII1 ( )
 if 82 - 82: oO0o
elif oo000o == 7003 :
 O00O00oO ( i1I1ii11i1Iii )
 if 78 - 78: IIiIiII11i / I11O0O0oOO00O00o - Ii + Ii1I * I1ii11iIi11i
elif oo000o == 7004 :
 oo0OoOO000O ( i1I1ii11i1Iii )
 if 17 - 17: OOooOOo
elif oo000o == 7020 :
 OOO0ooO0Oo0 ( i1I1ii11i1Iii )
 if 72 - 72: Ii1IIIi1 . I1ii11iIi11i - Ii / oOo0O0Ooo
elif oo000o == 7001 :
 iIII1iIii ( )
 if 64 - 64: oO0oo0o
elif oo000o == 7010 :
 iIIiII1i1ii ( i1I1ii11i1Iii )
 if 80 - 80: I11i % iI11I1II1I1I
elif oo000o == 7011 :
 i1III ( i1I1ii11i1Iii )
 if 63 - 63: ooOOOoO * Ii
elif oo000o == 7012 :
 Oo00O00o0 ( i1I1ii11i1Iii )
 if 86 - 86: I11O0O0oOO00O00o % I11O0O0oOO00O00o - OOooOOo + ii1ii11IIIiiI / oOo0O0Ooo * ii
elif oo000o == 7013 :
 cnfTVPlay2 ( i1I1ii11i1Iii )
elif oo000o == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1I1ii11i1Iii )
elif oo000o == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1I1ii11i1Iii )
elif oo000o == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oO00oooOOoOo0 , i1I1ii11i1Iii , Oo00OoOo )
elif oo000o == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oo000o == 7018 :
 Ii1o0OOOoo0000 ( )
elif oo000o == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1I1ii11i1Iii )
elif oo000o == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1I1ii11i1Iii )
elif oo000o == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1I1ii11i1Iii )
 if 26 - 26: IIiIiII11i * Ii1IIIi1 + I11i / o0o00Oo0O + ooOoO0O00 - I11O0O0oOO00O00o
elif oo000o == 8000 :
 oOoO ( )
elif oo000o == 8001 :
 Oo0Oo0 ( )
elif oo000o == 8002 :
 o00OOOOooO ( )
elif oo000o == 8003 :
 Iii1 ( )
elif oo000o == 8004 :
 iII1i1 ( )
elif oo000o == 8005 :
 iIii1II1I ( )
elif oo000o == 8006 :
 iii1IiII ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oo000o == 8030 :
 ooO00O00oOO ( i1I1ii11i1Iii )
elif oo000o == 8045 :
 I11II11111i11 ( i1I1ii11i1Iii )
elif oo000o == 8046 :
 OOO000Oo ( i1I1ii11i1Iii )
elif oo000o == 8047 :
 i1IiI1iIIIIIi ( i1I1ii11i1Iii )
elif oo000o == 8048 :
 iiI1ii1Iii ( i1I1ii11i1Iii )
elif oo000o == 8049 :
 Ii1I1IIIiI1i ( i1I1ii11i1Iii )
elif oo000o == 8020 :
 O000O000 ( )
elif oo000o == 8021 :
 OoO0000O ( i1I1ii11i1Iii )
elif oo000o == 8022 :
 I1I1iI ( i1I1ii11i1Iii )
elif oo000o == 8023 :
 IIIOo0O ( i1I1ii11i1Iii )
elif oo000o == 8040 :
 iIi ( )
elif oo000o == 8041 :
 I1i11I11Iii ( i1I1ii11i1Iii )
elif oo000o == 8042 :
 oO0ooo00o0o000Oo ( i1I1ii11i1Iii )
elif oo000o == 8043 :
 yt . PlayVideo ( i1I1ii11i1Iii )
elif oo000o == 8044 :
 Oooo00OOo ( i1I1ii11i1Iii )
elif oo000o == 8060 :
 i1ii1iIi ( )
elif oo000o == 8061 :
 I1I1Ii ( i1I1ii11i1Iii )
elif oo000o == 8064 :
 I11ii1iI11 ( )
elif oo000o == 8065 :
 i11ii111i1ii ( i1I1ii11i1Iii )
elif oo000o == 8070 :
 iiOo0 ( )
elif oo000o == 8071 :
 OOO00ii1Ii111I11I ( i1I1ii11i1Iii )
elif oo000o == 7080 :
 o0OoOoo ( i1I1ii11i1Iii )
elif oo000o == 8090 :
 iII11IiI1 ( )
elif oo000o == 8091 :
 OoOOOO00oOO ( i1I1ii11i1Iii )
elif oo000o == 8092 :
 O000oO ( i1I1ii11i1Iii )
elif oo000o == 8093 :
 iiIIiIi ( i1I1ii11i1Iii )
elif oo000o == 8081 :
 O0iI1I1ii11IIi1 ( )
elif oo000o == 8062 :
 ooooooO0O ( i1I1ii11i1Iii )
elif oo000o == 8063 :
 Oo0OOOOOOO0oo ( i1I1ii11i1Iii )
elif oo000o == 8050 :
 i1iI1IIIII1 ( )
elif oo000o == 8051 :
 iI1I1IiIi1I ( i1I1ii11i1Iii )
elif oo000o == 8052 :
 II1i1ii ( i1I1ii11i1Iii )
elif oo000o == 8085 :
 I1Iiii ( )
elif oo000o == 8086 :
 oOo0OoOOOo0 ( i1I1ii11i1Iii )
elif oo000o == 8087 :
 O00o0OO0OO0oo ( i1I1ii11i1Iii )
elif oo000o == 8088 :
 Ooo0O0ooo0o ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif oo000o == 9000 :
 OoOooo ( )
elif oo000o == 1111 :
 III11II111 ( )
elif oo000o == 9001 :
 IIii1i ( )
elif oo000o == 9002 :
 o0OoOo0o0O00 ( )
elif oo000o == 9003 :
 i1I1IIiIIi ( )
elif oo000o == 9004 :
 World1 ( )
elif oo000o == 9005 :
 World2 ( i1I1ii11i1Iii )
elif oo000o == 9006 :
 World3 ( i1I1ii11i1Iii )
elif oo000o == 9007 :
 IIIi1iiIIiiiI ( )
elif oo000o == 9008 :
 I1IIiIi1iI ( i1I1ii11i1Iii )
elif oo000o == 9009 :
 oOo0Iiii11 ( i1I1ii11i1Iii )
elif oo000o == 9010 :
 OoOO ( )
elif oo000o == 9011 :
 iIO0oOoo00Oo0O ( i1I1ii11i1Iii )
elif oo000o == 50 :
 iIIIiiiI11I ( i1I1ii11i1Iii )
elif oo000o == 9020 :
 champlist ( )
elif oo000o == 9021 :
 Oo00o00 ( )
elif oo000o == 9022 :
 OoOo0O0 ( )
elif oo000o == 9023 :
 I1o0 ( )
elif oo000o == 9024 :
 O0OO ( i1I1ii11i1Iii )
elif oo000o == 9030 :
 IIiI ( i1I1ii11i1Iii )
elif oo000o == 9031 :
 OOoOo0oO0oo00 ( i1I1ii11i1Iii )
elif oo000o == 9032 :
 OOI1I ( i1I1ii11i1Iii )
elif oo000o == 9033 :
 o0oO00O ( i1I1ii11i1Iii )
elif oo000o == 9034 :
 o0oooOO00 ( )
elif oo000o == 7085 :
 iii11 ( i1I1ii11i1Iii )
elif oo000o == 7086 :
 I11iIIIIi1Iii1iIi ( i1I1ii11i1Iii )
elif oo000o == 7087 :
 o0OOOoO0O ( oooOOoooo )
elif oo000o == 9666 :
 oOo0OOoooO ( i1I1ii11i1Iii )
elif oo000o == 10100 : OooO ( )
elif oo000o == 10105 : Oooo0ooOoo0 ( i1I1ii11i1Iii )
elif oo000o == 10106 : iIiII1 ( i1I1ii11i1Iii )
elif oo000o == 10104 : oO0I1I1i1I1I1I1 ( i1I1ii11i1Iii )
elif oo000o == 10107 : IiII1 ( )
elif oo000o == 10103 : o0oOOoo0O ( i1I1ii11i1Iii )
elif oo000o == 10108 : II1i1i1I1iII ( i1I1ii11i1Iii )
elif oo000o == 10107 : IiII1 ( )
elif oo000o == 10000 : Origin_Menu ( )
elif oo000o == 10001 : i1i ( )
elif oo000o == 10002 : o0IiIiI111IIII1 ( )
elif oo000o == 10003 : Oo0oOo000OoO0 ( )
elif oo000o == 10004 : ooO00o ( i1I1ii11i1Iii )
elif oo000o == 10005 : iiiIIIii ( )
elif oo000o == 10006 : IIii1i11iI1II11 ( i1I1ii11i1Iii )
elif oo000o == 10007 : o0oOOOO0 ( i1I1ii11i1Iii , Oo00OoOo )
elif oo000o == 10008 : II1iiI1 ( )
elif oo000o == 10009 : III1OOO000OOo0o0O ( )
elif oo000o == 10010 : i1i1I11i1I ( i1I1ii11i1Iii )
elif oo000o == 10011 : II1IIii1ii ( i1I1ii11i1Iii )
elif oo000o == 10012 : IiIii1ii ( i1I1ii11i1Iii )
elif oo000o == 10109 : iII1111IIIIiI ( i1I1ii11i1Iii )
elif oo000o == 10013 : OO0OooOo ( i1I1ii11i1Iii )
elif oo000o == 10014 : i1I1iIoOOoO ( )
elif oo000o == 10015 : oo0OoOOooO ( )
elif oo000o == 10016 : I1 ( i1I1ii11i1Iii )
elif oo000o == 10017 : i1ii1IiiiiIi1I ( )
elif oo000o == 10018 : Ii1Ii1 ( )
elif oo000o == 10019 : O00Oo0 ( )
elif oo000o == 10020 : OOOO0Oo ( )
elif oo000o == 10021 : I1I1IIiiii1ii ( )
elif oo000o == 10022 : oOoO0Oo0 ( i1I1ii11i1Iii )
elif oo000o == 10023 : o0Oo ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oo000o == 10024 : OOoOO0O0o0 ( i1I1ii11i1Iii )
elif oo000o == 10025 : O0OOo ( )
elif oo000o == 10026 : i1IiII ( )
elif oo000o == 10027 : ooooo0Oo0 ( )
elif oo000o == 10028 : OOo000OO000 ( )
elif oo000o == 10029 : ooooO0 ( )
elif oo000o == 423 : oo00o0 ( i1I1ii11i1Iii )
elif oo000o == 426 : iiI11I1iiIiII1I ( i1I1ii11i1Iii )
elif oo000o == 10030 : Izle_Films ( )
elif oo000o == 10031 : Latest_Izle_Movies ( )
elif oo000o == 10032 : Izle_Genres ( )
elif oo000o == 10033 : Izle_Pop_Movies ( )
elif oo000o == 10034 : Izle_Boxsets ( )
elif oo000o == 10035 : Izle_Search ( )
elif oo000o == 10036 : Izle_Genres_Movie ( i1I1ii11i1Iii )
elif oo000o == 10037 : Izle_Boxset_single ( i1I1ii11i1Iii )
elif oo000o == 10038 : Izle_IFRAME ( )
elif oo000o == 10039 : Izle_Boxsets_Next ( i1I1ii11i1Iii )
elif oo000o == 10040 : iIiii1Ii1I1II ( )
elif oo000o == 10041 : oO0oiIiI ( i1I1ii11i1Iii )
elif oo000o == 10042 : o0ooo0o0 ( i1I1ii11i1Iii )
elif oo000o == 10043 : iIIi1 ( )
elif oo000o == 10044 : ooIiI11i1I11111 ( i1I1ii11i1Iii )
elif oo000o == 10045 : II1i ( oO00oooOOoOo0 )
elif oo000o == 10046 : I111 ( i1I1ii11i1Iii )
elif oo000o == 10047 : oOooOOo00ooO ( i1I1ii11i1Iii )
elif oo000o == 10048 : iiIO0OO0o0O00oO ( i1I1ii11i1Iii )
elif oo000o == 10049 : III1 ( i1I1ii11i1Iii )
elif oo000o == 10050 : ooOOOo0 ( )
elif oo000o == 10051 : I1Iii11111I1iii ( )
elif oo000o == 10052 : III1Iiii1i11 ( )
elif oo000o == 10053 : Addon ( i1I1ii11i1Iii )
elif oo000o == 10054 : o0oooO0O00OoO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif oo000o == 10055 :
 ii1IIiI1IIi ( "addFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oooo00 ( oO00oooOOoOo0 , i1I1ii11i1Iii , Oo00OoOo , oOo0O , iiIii1I1Ii )
elif oo000o == 10056 :
 ii1IIiI1IIi ( "rmFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 II1IIiIiiI1iI ( oO00oooOOoOo0 )
elif oo000o == 10057 :
 ii1IIiI1IIi ( "getFavorites" )
 O000 ( )
elif oo000o == 10058 : i1I1i111Ii ( )
elif oo000o == 10059 : Donators_Guide ( )
elif oo000o == 10060 : O0oOo00o0 ( )
elif oo000o == 10061 : ii1ii11 ( )
elif oo000o == 10062 : oOO0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , oooOOoooo )
elif oo000o == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif oo000o == 10064 : i11iiI1111 ( )
elif oo000o == 10065 : O00oO0 ( i1I1ii11i1Iii )
elif oo000o == 10066 : II11iI111i1 ( i1I1ii11i1Iii )
elif oo000o == 10068 : O0iII1 ( i1I1ii11i1Iii )
elif oo000o == 10069 : OOo ( i1I1ii11i1Iii )
elif oo000o == 10070 : I1II ( i1I1ii11i1Iii )
elif oo000o == 10071 : Genie_Watch ( )
elif oo000o == 10072 : OOOO0O00o ( )
elif oo000o == 10073 : Oo00o0OO0O00o ( i1I1ii11i1Iii )
elif oo000o == 10074 : i1Iii11I1i ( i1I1ii11i1Iii )
elif oo000o == 10075 : ooo0o00 ( Oo00OoOo , oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oo000o == 10076 : o0OIiiiI ( i1I1ii11i1Iii )
elif oo000o == 10077 : O0OOoOOO0oO ( i1I1ii11i1Iii )
elif oo000o == 10078 : i1II ( )
elif oo000o == 10079 : Genie_Watch_Tv_Shows ( )
elif oo000o == 10080 : Genie_Watch_Tv_Genre ( i1I1ii11i1Iii )
elif oo000o == 10081 : Genie_Watch_TV_PlayRun ( i1I1ii11i1Iii )
elif oo000o == 10082 : Genie_Watch_TV_Episodes ( i1I1ii11i1Iii , Oo00OoOo )
elif oo000o == 10083 : Genie_Watch_Tv_Recent ( i1I1ii11i1Iii )
elif oo000o == 10084 : o0ooooO0o0O ( )
elif oo000o == 10085 : IiI111111IIII ( )
elif oo000o == 10086 : ooOOO00Ooo ( )
elif oo000o == 20000 : oOO0IIi1I1i ( )
elif oo000o == 20001 : O00o ( )
elif oo000o == 20002 : oO0OoooO0oOO00OoOo ( i1I1ii11i1Iii )
elif oo000o == 20003 : O0OOO0 ( i1I1ii11i1Iii )
elif oo000o == 20004 : I1iIIIiIi1 ( i1I1ii11i1Iii )
elif oo000o == 21004 : O0Oo0 ( )
elif oo000o == 21005 : OOooO0OO0 ( i1I1ii11i1Iii )
elif oo000o == 21006 : OOOOOo ( i1I1ii11i1Iii )
elif oo000o == 21007 : O0oOo00Ooo0o0 ( i1I1ii11i1Iii )
elif oo000o == 30000 : I1iI ( )
elif oo000o == 30001 : o0OoOoo00O ( )
elif oo000o == 10012 : Resolve ( i1I1ii11i1Iii )
elif oo000o == 30003 : OO ( )
elif oo000o == 30004 : OoOoO0O ( i1I1ii11i1Iii )
elif oo000o == 30005 : o00IiI1iiII1i1i ( i1I1ii11i1Iii )
elif oo000o == 30006 : o00OoO0oO00 ( )
elif oo000o == 30007 : iiii1 ( )
elif oo000o == 30008 : i1i1 ( i1I1ii11i1Iii )
elif oo000o == 30009 : iIiI ( i1I1ii11i1Iii )
elif oo000o == 30010 : i11II ( i1I1ii11i1Iii )
elif oo000o == 30011 : OoO00o0 ( )
elif oo000o == 30012 : II1iIII ( )
elif oo000o == 30013 : OO0I11Ii1iI11iI1 ( )
elif oo000o == 30014 : o0Oo00OO0 ( )
elif oo000o == 30015 : oOOOiIi1I1 ( i1I1ii11i1Iii , Oo00OoOo , oOo0O )
elif oo000o == 30016 : Ooo0 ( i1I1ii11i1Iii )
elif oo000o == 30019 : o0oO0oo0000OO ( i1I1ii11i1Iii )
elif oo000o == 30017 : Iiii1ii ( i1I1ii11i1Iii )
elif oo000o == 30018 : OOO0o0OO0OO ( i1I1ii11i1Iii )
elif oo000o == 30030 : ooiiI1ii ( )
elif oo000o == 30031 : O0OooOO ( )
elif oo000o == 30032 : i1i1o0oOoOo0 ( )
elif oo000o == 30033 : III1IiI1i1i ( )
elif oo000o == 30034 : o0OOOOOo0 ( )
elif oo000o == 30035 : oooo00 ( i1I1ii11i1Iii )
elif oo000o == 30036 : i1oO ( i1I1ii11i1Iii )
elif oo000o == 30037 : iIIi1IIi ( i1I1ii11i1Iii )
elif oo000o == 30038 : oOOII1i11i1iIi11 ( )
elif oo000o == 30039 : iI1 ( )
elif oo000o == 50000 : IIiiIiII1Ii ( )
elif oo000o == 50001 : ooi1II1I ( )
elif oo000o == 50002 : OO0IIIIIIi111i ( i1I1ii11i1Iii )
elif oo000o == 50003 : IIIIiI11Ii1i ( oooOOoooo )
elif oo000o == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oo000o == 60001 : iiIi1IIiI ( )
elif oo000o == 60002 : OOoO000 ( oO00oooOOoOo0 )
elif oo000o == 60003 : i1II11II ( oO00oooOOoOo0 )
elif oo000o == 50004 : OO0ooOOO0OOO ( )
elif oo000o == 50005 : speedtest . runtest ( i1I1ii11i1Iii )
elif oo000o == 70001 : I11iiIIiI1ii ( )
elif oo000o == 70002 : O00 ( i1I1ii11i1Iii )
elif oo000o == 70003 : O0OO0 ( i1I1ii11i1Iii )
elif oo000o == 70004 : OOoOOo0o ( i1I1ii11i1Iii )
elif oo000o == 70005 : iIiii ( i1I1ii11i1Iii )
elif oo000o == 70006 : IIiI1i ( )
elif oo000o == 50006 : O0O0Oooo0o ( i1 , i1111 )
elif oo000o == 80000 : iIi1iIIIiIiI ( )
elif oo000o == 80001 : resolvefilmon ( i1I1ii11i1Iii )
elif oo000o == 80002 : III11iiii11i1 ( )
elif oo000o == 80003 : OOooooo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oo000o == 80004 : i111i11I1ii ( oO00oooOOoOo0 , i1I1ii11i1Iii )
if 56 - 56: O00o0O00
if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + ooOOOoO - I11O0O0oOO00O00o
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
