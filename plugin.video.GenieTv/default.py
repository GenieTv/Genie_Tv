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
IiiIII111iI = "3.1.6"
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
  O0O0Oooo0o ( 'Change Log 30/9/16 - v3.1.6' , 'Apk tool added download and instal over 100,000 apps direct to your box, new documentaries section added, Bollywood section added' )
  os . makedirs ( o0 )
  if 33 - 33: o0o00Oo0O * I11i - ii1ii11IIIiiI % ii1ii11IIIiiI
  if 18 - 18: ii1ii11IIIiiI / I1ii11iIi11i * ii1ii11IIIiiI + ii1ii11IIIiiI * Ii * Ii1I
def I1II1 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , OO0o , '' )
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
def o000oo ( ) :
 oOo0 ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://www.join4films.com/' )
 IIi1I11I1II = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 80006 , III1iII1I1ii + 'Desi.png' )
def o00o0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( IIIi1I1IIii1II )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 80007 , II1III1I1I1Ii )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def OOOOoO00o0O ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  url = ( url ) . replace ( ' ' , '%20' )
  I1I1I1IIi1III ( url )
def II11IiiIII ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1iiIiIII1ii = 'http://www.join4films.com/?s=' + ( o0OOOo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oO0o0oooO0oO = ii1iiIiIII1ii . lower ( )
 o00o0 ( oO0o0oooO0oO )
 if 19 - 19: Ii + ii - I1ii11iIi11i - I11O0O0oOO00O00o
 if 21 - 21: o0o00Oo0O % ooOOOoO . oOo0O0Ooo / IIiIiII11i + ooOOOoO
 if 53 - 53: oO0oo0o - oOo0O0Ooo - oO0oo0o * Ii1IIIi1
 if 71 - 71: o0o00Oo0O - iI11I1II1I1I
 if 12 - 12: O00o0O00 / I11i
 if 42 - 42: I1ii11iIi11i
 if 19 - 19: oO0oo0o % Ii1I * iI11I1II1I1I + oOo0O0Ooo
 if 46 - 46: I1ii11iIi11i
 if 1 - 1: Ii1IIIi1
 if 97 - 97: O00o0O00 + Ii1IIIi1 + o0o00Oo0O + Ii
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . Ii1IIIi1 % Ii1IIIi1 + Ii
 if 72 - 72: iI11I1II1I1I * iI1ii11iIi1i % O0OOOoOoo0 / oO0o
 if 35 - 35: O0OOOoOoo0 + ooOoO0O00 % Ii1I % I11O0O0oOO00O00o + oO0oo0o
 if 17 - 17: ooOoO0O00
 if 21 - 21: I1ii11iIi11i
 if 29 - 29: I11O0O0oOO00O00o / IIiIiII11i / O0OOOoOoo0 * O00o0O00
def I111i1i1111 ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 if 49 - 49: oO0o / oO0oo0o + o0o00Oo0O * I11i
def I1ii11 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1iiIiIII1ii = 'http://imoviemax.se/?s=' + ( o0OOOo ) . replace ( ' ' , '+' )
 oO0o0oooO0oO = ii1iiIiIII1ii . lower ( )
 oOoOoOoo0 ( oO0o0oooO0oO )
def III1ii1I ( url ) :
 Ii1i1iI = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , IIiI1 in IIi1I11I1II :
  if oO00oooOOoOo0 in Ii1i1iI :
   pass
  else :
   I1IIII1i ( oO00oooOOoOo0 + ' - ' + IIiI1 + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
   Ii1i1iI . append ( oO00oooOOoOo0 )
   if 17 - 17: O00o0O00 / O00o0O00 / I11O0O0oOO00O00o
def ii1I1IiiI1ii1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , O0o in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + ' - Views:' + O0o , url , 10075 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
  if 54 - 54: O00o0O00
  if 45 - 45: ii - O00o0O00 + o0o00Oo0O * iI1ii11iIi1i . Ii1I
def oOoOoOoo0 ( url ) :
 IiiiI = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIIi1I1IIii1II )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10075 , II1III1I1I1Ii , II1III1I1I1Ii , '' )
  IiiiI . append ( oO00oooOOoOo0 )
  if 61 - 61: O00o0O00 % O00o0O00 * I11i / I11i
def o0oOO ( img , name , url ) :
 img = img
 name = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIIi1I1IIii1II )
 for O0o0OO0000ooo , url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIIII1iIIii = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIIII1iIIii
  oOOO00o000o = ( O0o0OO0000ooo ) . replace ( 'play-' , 'Server ' )
  iIiIIi1 ( oOOO00o000o , iIIII1iIIii , 10076 , img , img , '' )
  if 9 - 9: oO0oo0o + I11O0O0oOO00O00o / I11O0O0oOO00O00o
def Ii1I11ii1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o in IIi1I11I1II :
  if '=m' in o0OO0o0o00o :
   O0iIiIIIIIii ( o0OO0o0o00o )
  elif 'php' in o0OO0o0o00o :
   Ii1I11ii1i ( url )
  else :
   IIIi1I1IIii1II = O0i1II1Iiii1I11 ( o0OO0o0o00o )
   IIi1I11I1II = re . compile ( 'content="([^"]*)">' ) . findall ( IIIi1I1IIii1II )
   for OOo0 in IIi1I11I1II :
    O0iIiIIIIIii ( o0OO0o0o00o )
    if 25 - 25: ii + ooOOOoO * Ii1I
    if 92 - 92: oOo0O0Ooo + I11O0O0oOO00O00o + o0o00Oo0O / I11i + ii1ii11IIIiiI
    if 18 - 18: O0OOOoOoo0 * OOooOOo . Ii1IIIi1 / Ii1I / Ii
def IIIIIo0ooOoO000oO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OOo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1i11I1I1iii1 , I1iii11 in OOo :
  print 'there ><><><><><><><><><><><><'
  i1i11I1I1iii1 = i1i11I1I1iii1
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1iii11 ) )
  for oO00oooOOoOo0 , ooo0O in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + i1i11I1I1iii1 + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + ooo0O + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
 iII1iii = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1i11I1I1iii1 , i11i1iiiII in iII1iii :
  print 'there ><><><><><><><><><><><><'
  i1i11I1I1iii1 = i1i11I1I1iii1
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i11i1iiiII ) )
  for oO00oooOOoOo0 , ooo0O in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + i1i11I1I1iii1 + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + ooo0O + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
   if 68 - 68: Ii * oO0o
   if 46 - 46: OOooOOo / iI11I1II1I1I % Ii1IIIi1 . iI11I1II1I1I * Ii1IIIi1
   if 38 - 38: Ii1I - Ii1IIIi1 / o0o00Oo0O . ii1ii11IIIiiI
def i1iiIiI1Ii1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iII1iii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for iII1iii in iII1iii :
  oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII1iii ) )
  for oO00oooOOoOo0 in oO00oooOOoOo0 :
   oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII1iii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i1iIi = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII1iii ) )
  for i1iIi in i1iIi :
   i1iIi = 'http:' + i1iIi
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , '' , '' )
  if 30 - 30: o0o00Oo0O - iI11I1II1I1I / ii
  if 89 - 89: Ii1IIIi1 - O0OOOoOoo0 % I1ii11iIi11i % I11i
  if 49 - 49: I1ii11iIi11i - oOo0O0Ooo / ooOOOoO / o0o00Oo0O % I11i * iI1ii11iIi1i
  if 100 - 100: O00o0O00 . Ii1IIIi1 / o0o00Oo0O * ooOoO0O00 * iI1ii11iIi1i * I1ii11iIi11i
def OO00 ( url ) :
 if 92 - 92: I11O0O0oOO00O00o
 Oo00OoOo = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o , II1III1I1I1Ii , oO00oooOOoOo0 , ii1ii111 in IIi1I11I1II :
  oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = O0i1II1Iiii1I11 ( o0OO0o0o00o )
  OooOoooOo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for i11111I1I , ii1Oo0000oOo in OooOoooOo :
   I11o0oO00oO0o0o0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( ii1Oo0000oOo ) )
   for I1I in I11o0oO00oO0o0o0 :
    if oO00oooOOoOo0 in Oo00OoOo :
     pass
    else :
     iIiIIi1 ( oO00oooOOoOo0 , i11111I1I , 8043 , II1III1I1I1Ii , II1III1I1I1Ii , I1I )
     I1I1II1I11 ( 'movies' , 'INFO' )
     Oo00OoOo . append ( oO00oooOOoOo0 )
     if 89 - 89: ooOoO0O00 / IIiIiII11i . iI11I1II1I1I
     if 1 - 1: O0OOOoOoo0 % OOooOOo * I1ii11iIi11i
def o0O0oo0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , iiiI1I1iIIIi1 , I1I , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10065 , iiiI1I1iIIIi1 , oOo0O , I1I )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 17 - 17: iI11I1II1I1I . ii / I11O0O0oOO00O00o % IIiIiII11i % ooOoO0O00 / Ii
def OOOIiiiii1iI ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1iiIiIII1ii = 'https://www.youtube.com/results?search_query=' + ( o0OOOo ) . replace ( ' ' , '+' )
 oO0o0oooO0oO = ii1iiIiIII1ii . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oO0o0oooO0oO )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in next :
  i1I1ii11i1Iii = 'https://www.youtube.com' + i1I1ii11i1Iii
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , i1I1ii11i1Iii , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 , IIi , ii1Oo0000oOo in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  i1iIi = 'http:' + ( II1III1I1I1Ii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i1iIi
  i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
  iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , i1iIi , ii1Oo0000oOo )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 , IIi in IIi1I11I1II :
   print 'im doing it'
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   i1iIi = 'http:' + ( II1III1I1I1Ii ) . replace ( 'https:' , '' )
   i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
   if '&' in i1I1ii11i1Iii :
    print ' i got here'
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    iII1iii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for iII1iii in iII1iii :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII1iii ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     i1I1ii11i1Iii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII1iii ) )
     for i1I1ii11i1Iii in i1I1ii11i1Iii :
      i1I1ii11i1Iii = 'https://www.youtube.com/w' + i1I1ii11i1Iii
     i1iIi = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII1iii ) )
     for i1iIi in i1iIi :
      i1iIi = 'http:' + i1iIi
     iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in i1I1ii11i1Iii or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in i1I1ii11i1Iii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i1I1ii11i1Iii
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    ooOooo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 in ooOooo0 :
     if 'outube' in i1I1ii11i1Iii or 'list' in i1I1ii11i1Iii :
      pass
     elif 'atch' in i1I1ii11i1Iii :
      i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + II1III1I1I1Ii , 'http:' + II1III1I1I1Ii , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , i1iIi , '' )
    if 67 - 67: oOo0O0Ooo
def OO00OO0O0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 , IIi , ii1Oo0000oOo in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  i1iIi = 'http:' + ( II1III1I1I1Ii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i1iIi
  url = 'http://www.youtube.com' + url
  iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , i1iIi , ii1Oo0000oOo )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for II1III1I1I1Ii , url , oO00oooOOoOo0 , IIi in IIi1I11I1II :
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   i1iIi = 'http:' + ( II1III1I1I1Ii ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    iII1iii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for iII1iii in iII1iii :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII1iii ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII1iii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i1iIi = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII1iii ) )
     for i1iIi in i1iIi :
      i1iIi = 'http:' + i1iIi
     iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    ooOooo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for II1III1I1I1Ii , url , oO00oooOOoOo0 in ooOooo0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + II1III1I1I1Ii , 'http:' + II1III1I1I1Ii , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + IIi + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi , i1iIi , '' )
    if 48 - 48: ii1ii11IIIiiI
    if 72 - 72: Ii1IIIi1 * oO0oo0o % iI1ii11iIi1i . ii
def i1I1i111Ii ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OoO0O0O0o00 = open ( O000oo0O )
  IIi1I11I1II = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OoO0O0O0o00 ) )
  for iiiI11 , OOoO000 in IIi1I11I1II :
   if iiiI11 == 'needs replacing' or OOoO000 == 'needs replacing' :
    oOOOO ( )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv PRIVATE LIST[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , III1iII1I1ii + 'PrivateList.png' , OO0o , '' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv ULTIMATE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
  if 49 - 49: IIiIiII11i . oO0oo0o . Ii % ooOOOoO
def i11i1iiI1i ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 oOOOO ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 87 - 87: O0OOOoOoo0
def IIIii ( ) :
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
 if 83 - 83: ooOOOoO % I11i % oOo0O0Ooo . iI11I1II1I1I - ooOOOoO
def o00o ( name ) :
 Ii1IIiiIIi = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , II1III1I1I1Ii , Oo000o , i1I1ii11i1Iii in IIi1I11I1II :
  if Ii1IIiiIIi == 'Full List' :
   i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
   iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , II1III1I1I1Ii , II1III1I1I1Ii , '' )
  else :
   Ii1IIiiIIi = ( Ii1IIiiIIi ) . replace ( 'World' , 'القنوات العربية' )
   if Ii1IIiiIIi in Oo000o :
    i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
    print i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , II1III1I1I1Ii , II1III1I1I1Ii , '' )
   else :
    pass
    if 39 - 39: Ii1I
def O0oOo00o0 ( name ) :
 Ii1IIiiIIi = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , II1III1I1I1Ii , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
  iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , II1III1I1I1Ii , II1III1I1I1Ii , '' )
 else :
  iIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % oO0oo0o * oO0o
  if 38 - 38: OOooOOo / Ii1IIIi1 % I1ii11iIi11i
  if 11 - 11: Ii1IIIi1 - oO0oo0o + IIiIiII11i - iI11I1II1I1I
  if 7 - 7: ooOOOoO - I11O0O0oOO00O00o / IIiIiII11i * iI1ii11iIi1i . Ii1IIIi1 * Ii1IIIi1
  if 61 - 61: I11O0O0oOO00O00o % O0OOOoOoo0 - oO0o / I1ii11iIi11i
  if 4 - 4: ii - ooOoO0O00 % iI1ii11iIi1i - O00o0O00 * I11i
  if 85 - 85: ii * iI11I1II1I1I . Ii1IIIi1 / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: iI1ii11iIi1i / IIiIiII11i / ooOOOoO / ooOOOoO + Ii1I
  if 95 - 95: ooOOOoO
  if 51 - 51: IIiIiII11i + ooOOOoO . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
  if 72 - 72: oO0oo0o + oO0oo0o / IIiIiII11i . ii % iI1ii11iIi1i
  if 49 - 49: oO0oo0o . oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( o00OO00OoO ) :
  I1IIII1i ( 'Backup Genie Favourites' , i1I1ii11i1Iii , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( oO0Oo ) :
  I1IIII1i ( 'Backup Ivue Config' , oO0Oo , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( oOOoo0Oo ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oOOoo0Oo , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 83 - 83: I11O0O0oOO00O00o / Ii1I
  if 34 - 34: oOo0O0Ooo * I1ii11iIi11i * ii1ii11IIIiiI / oO0o * I11O0O0oOO00O00o / iI11I1II1I1I
  if 74 - 74: I1ii11iIi11i / Ii - IIiIiII11i * I11i
zip = oo00 . getSetting ( 'zip' )
IIi1IIIIi = xbmc . translatePath ( os . path . join ( zip ) )
def OOOoO ( ) :
 I1i = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 12 - 12: ii
  if 20 - 20: ooOoO0O00 - I11O0O0oOO00O00o
  if 30 - 30: OOooOOo
def Ii111 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = o00OO00OoO
  elif 'Ivue' in name :
   url = oO0Oo
  elif 'Kodi' in name :
   url = oOOoo0Oo
  OOOoO ( )
  oO0i1iI = open ( url ) . read ( )
  iioo0o0OoOOO = os . path . join ( IIi1IIIIi , description . split ( 'Your ' ) [ 1 ] )
  o0Oo00 = open ( iioo0o0OoOOO , mode = 'w' )
  o0Oo00 . write ( oO0i1iI )
  o0Oo00 . close ( )
 else :
  if 'guisettings.xml' in description :
   ooO0oO00O0o = open ( os . path . join ( IIi1IIIIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOO00oOOo000 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi1I11I1II = re . compile ( ooOO00oOOo000 ) . findall ( ooO0oO00O0o )
   for type , IIii11II11II1 , II1IOoOo000oOo0oo in IIi1I11I1II :
    II1IOoOo000oOo0oo = II1IOoOo000oOo0oo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IIii11II11II1 , II1IOoOo000oOo0oo ) )
  else :
   iioo0o0OoOOO = os . path . join ( url )
   oO0i1iI = open ( os . path . join ( IIi1IIIIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0Oo00 = open ( iioo0o0OoOOO , mode = 'w' )
   o0Oo00 . write ( oO0i1iI )
   o0Oo00 . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 65 - 65: OOooOOo / oO0o % ooOOOoO
 if 45 - 45: OOooOOo
 if 66 - 66: oO0o
 if 56 - 56: o0o00Oo0O
def OOo00 ( ) :
 iIII = 1
 OOOoO ( )
 Ii1iI11iI1 = xbmc . translatePath ( os . path . join ( IIi1IIIIi , 'Build Backup' , 'Full Backup' , '' ) )
 i11I1II = xbmc . translatePath ( os . path . join ( IIi1IIIIi , 'Build Backup' , 'my_full_backup.zip' ) )
 OO0 = xbmc . translatePath ( os . path . join ( IIi1IIIIi , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( Ii1iI11iI1 ) :
  os . makedirs ( Ii1iI11iI1 )
 OOO0oOOo00O = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OOO0oOOo00O ) : return False , 0
 OO0oIII111i11IiI = OOO0oOOo00O
 O0000 = xbmc . translatePath ( os . path . join ( Ii1iI11iI1 , OO0oIII111i11IiI + '.zip' ) )
 ooO00O0O0 = [ 'plugin.video.GenieTv' ]
 iII1I1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0Ooo0o0ooo0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oo0o0000Oo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0O00oOoo = "Creating full backup of existing build"
 O000O0OO00oo = "Creating Community Build"
 oOOO = "Archiving..."
 ooo0oooo0 = ""
 OOO0ooo = "Please Wait"
 IIiiii ( I11 , O0000 , O000O0OO00oo , oOOO , ooo0oooo0 , OOO0ooo , o0Ooo0o0ooo0 , oo0o0000Oo0 )
 time . sleep ( 1 )
 iI111i1I1II = xbmc . translatePath ( os . path . join ( Ii1iI11iI1 , OO0oIII111i11IiI + '_guisettings.zip' ) )
 O00OO = zipfile . ZipFile ( iI111i1I1II , mode = 'w' )
 try :
  O00OO . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 O00OO . close ( )
 if iIII == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i11I1II , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O0000 + '[/COLOR]' )
  if 29 - 29: I1ii11iIi11i % oO0o % ooOOOoO . I11i / ii * O0OOOoOoo0
def IIiiii ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0OoO000O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 OOoiIIiiIIIi1I = len ( sourcefile )
 OO0o0o0oo0O = [ ]
 IIiI1I1 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for I11I1IIiiII1 , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( sourcefile ) :
  for file in OOOooo0OooOoO :
   IIiI1I1 . append ( file )
 oOoOOOo = len ( IIiI1I1 )
 for I11I1IIiiII1 , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( sourcefile ) :
  IIIIIii1ii11 [ : ] = [ ii1I for ii1I in IIIIIii1ii11 if ii1I not in exclude_dirs ]
  OOOooo0OooOoO [ : ] = [ o0Oo00 for o0Oo00 in OOOooo0OooOoO if o0Oo00 not in exclude_files ]
  for file in OOOooo0OooOoO :
   OO0o0o0oo0O . append ( file )
   o0OOoOoO00 = len ( OO0o0o0oo0O ) / float ( oOoOOOo ) * 100
   o0oOoO00o . update ( int ( o0OOoOoO00 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1iii = os . path . join ( I11I1IIiiII1 , file )
   if not 'temp' in IIIIIii1ii11 :
    if not 'plugin.program.originwizard' in IIIIIii1ii11 :
     import time
     oOO0OO0O = '01/01/1980'
     o00oIII11I = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1iii ) ) )
     if o00oIII11I > oOO0OO0O :
      o0OoO000O . write ( I1iii , I1iii [ OOoiIIiiIIIi1I : ] )
 o0OoO000O . close ( )
 o0oOoO00o . close ( )
 if 17 - 17: ii + O00o0O00 * I11O0O0oOO00O00o * OOooOOo
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 if 55 - 55: I1ii11iIi11i - O00o0O00
 if 84 - 84: ii1ii11IIIiiI + I1ii11iIi11i - OOooOOo * OOooOOo
def OoooO0o ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'MOVIESv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'TVSHOWSv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON' , OO0o , '' )
 if 24 - 24: OOooOOo % ooOoO0O00 + Ii1IIIi1 . Ii . Ii1I
 if 17 - 17: Ii1I . IIiIiII11i . O0OOOoOoo0 / Ii1I
 if 57 - 57: I11O0O0oOO00O00o
 if 67 - 67: oO0o . O0OOOoOoo0
def oO00oOo0OOO ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , III1iII1I1ii + 'Quicksilver.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , OO0o , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , OO0o , '' )
  if 23 - 23: ooOoO0O00 . I11i * oO0o
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , OO0o , '' )
 if 15 - 15: OOooOOo
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 62 - 62: iI1ii11iIi1i
def ooO000O ( ) :
 O000OOo00oo ( )
 if 53 - 53: I11i . Ii1IIIi1 / iI1ii11iIi1i
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , OO0o , '' )
 iIiIIi1 ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , OO0o , 'Force Refresh All Repos' )
 if 39 - 39: iI1ii11iIi1i % o0o00Oo0O % OOooOOo . ooOoO0O00
 iIiIIi1 ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , OO0o , '' )
 iIiIIi1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , OO0o , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1I1IiI1 ) , 4 , III1iII1I1ii + 'AdvancedSettingXML.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']URL FIXES[/COLOR]' , str ( I1I1IiI1 ) , 20 , III1iII1I1ii + 'URLFixes.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 86 - 86: oO0o * ii
 if 71 - 71: iI11I1II1I1I - O00o0O00 . oOo0O0Ooo % ii + O00o0O00
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
 if 26 - 26: I1ii11iIi11i + O00o0O00 / oO0o % OOooOOo % Ii1I + IIiIiII11i
 if 31 - 31: I11O0O0oOO00O00o % O00o0O00 * I11O0O0oOO00O00o
def IiI ( ) :
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
 if 34 - 34: I11O0O0oOO00O00o % O0OOOoOoo0 . o0o00Oo0O . iI11I1II1I1I
def ooi1II1I ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , III1iII1I1ii + 'MyOnlineZip.png' , OO0o , '' )
 if 95 - 95: oO0o - O00o0O00 / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , OO0o , '' )
 iIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , OO0o , '' )
 if 97 - 97: ii - ii1ii11IIIiiI
 if 58 - 58: iI11I1II1I1I + o0o00Oo0O
 if 30 - 30: O0OOOoOoo0 % Ii1IIIi1 * O00o0O00 - Ii1I * iI1ii11iIi1i % O0OOOoOoo0
def iiiiI11ii ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , str ( I1I1IiI1 ) , 33 , III1iII1I1ii + 'Skins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , str ( I1I1IiI1 ) , 34 , III1iII1I1ii + 'ArtworkPacks.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' , I11 , 35 , III1iII1I1ii + 'CreateUniversalPath.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 96 - 96: Ii1IIIi1 . o0o00Oo0O / Ii1IIIi1 % o0o00Oo0O
def o0o000 ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi1I11I1II = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( OOO00O )
 for II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , II1III1I1I1Ii , II1III1I1I1Ii , '' )
 I1I1II1I11 ( 'tvshows' , 'INFO' )
 if 50 - 50: ooOOOoO % ooOoO0O00
def iii11II1I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( iI111I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 23 - 23: iI1ii11iIi1i . I11i + I1ii11iIi11i - O00o0O00
def II1iiIiIiI ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + I11O0O0oOO00O00o
def IiiIi ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 96 - 96: Ii1IIIi1
def i1I11iIII1i1I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oOO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 13 - 13: ii * oO0oo0o - iI1ii11iIi1i / O00o0O00 + I11O0O0oOO00O00o + ooOOOoO
def iii1III1i ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iiiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 45 - 45: Ii1I + oO0o * Ii / O00o0O00 % I11O0O0oOO00O00o * o0o00Oo0O
def i1o0oooO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 89 - 89: IIiIiII11i / oO0oo0o
def IIo0OoO00 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + IIIIIiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 40 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 45 - 45: oOo0O0Ooo / Ii1IIIi1 . Ii1IIIi1
def i1oO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIIi1IIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 43 - 43: ii1ii11IIIiiI % Ii1IIIi1
def o0O0ooOOoO ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '' , 80002 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , str ( I1I1IiI1 ) , 2 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' , str ( I1I1IiI1 ) , 30038 , III1iII1I1ii + 'APKSearch.png' , OO0o , '' )
 if 19 - 19: Ii
def oo0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oOO in IIi1I11I1II :
  oOo0 ( 'Android Apps' + oOO , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'apps.png' )
 for i1I1ii11i1Iii , oOO in OooOoooOo :
  oOo0 ( 'Android Games' + oOO , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def II1i11i1iIi11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/cat' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def oo0O0oO0O0O ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/app' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , III1iII1I1ii + 'APK.png' )
def oOo0OI11i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'href="([^"]*)" style="float:right;">next &gt;</a>' ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'apk' in url :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + II1III1I1I1Ii )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , o0OO0o0o00o + url , 30037 , III1iII1I1ii + 'Next.png' )
def Iiii1 ( name , url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 name = name
 IIi1I11I1II = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  url = 'https://www.apkfiles.com' + url
  iIIIiiiI11I ( name , url )
def I1ii1111Ii ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii1iiIiIII1ii = 'https://www.apkfiles.com/search?q=' + ( o0OOOo ) . replace ( ' ' , '+' ) + '&search_type=1'
 oO0o0oooO0oO = ii1iiIiIII1ii . lower ( )
 oOo0OI11i ( oO0o0oooO0oO )
 if 69 - 69: ooOOOoO . oO0o + IIiIiII11i
def oO0oOooooOoO ( url ) :
 I1i = xbmc . translatePath ( os . path . join ( i1oOOOOOOOoO , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1 = os . path . join ( I1i , oO00oooOOoOo0 + '.apk' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 13 - 13: OOooOOo / Ii1I . O00o0O00 * I11O0O0oOO00O00o - I1ii11iIi11i / oO0oo0o
def II1i ( url ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1 = os . path . join ( I1i , oO00oooOOoOo0 + '.mp4' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 81 - 81: Ii1I
 if 94 - 94: I11O0O0oOO00O00o + IIiIiII11i % Ii
def i1i1IiIiIi1Ii ( name , url , description ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I1 = os . path . join ( I1i , name )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 oO0ooOO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( I1 , oO0ooOO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 16 - 16: I1ii11iIi11i + O0OOOoOoo0 / I1ii11iIi11i / oO0o % oO0oo0o % Ii1I
 if 22 - 22: IIiIiII11i * oO0o * I11O0O0oOO00O00o + Ii1I * I11i
 if 100 - 100: ooOoO0O00 / ooOOOoO
 if 3 - 3: IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
 if 37 - 37: Ii1IIIi1 / I1ii11iIi11i . I11O0O0oOO00O00o * I11O0O0oOO00O00o
def o0O0Oo0Ooo0 ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i1iIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1I11I1II = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , OoOOoOooooOOo , oOo0O , I11iII in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 80003 , OoOOoOooooOOo , III1iII1I1ii + 'APKToolsB.png' , I11iII )
def IiiIiI ( apk , ret = None ) :
 if apk == "kodi" :
  iIIIIiiIii = "https://kodi.tv/download/"
  OOO00O = O0i1II1Iiii1I11 ( iIIIIiiIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( OOO00O )
  if len ( IIi1I11I1II ) == 1 :
   ooO0oo = IIi1I11I1II [ 0 ] [ 0 ]
   OO0oIII111i11IiI = IIi1I11I1II [ 0 ] [ 1 ]
   ooO0oo0o0 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( ooO0oo , OO0oIII111i11IiI )
  if ret == 'version' : return ooO0oo
  else : return ooO0oo0o0
 elif apk == "spmc" :
  IIiIii1 = 'https://github.com/koying/SPMC/releases/latest/'
  OOO00O = O0i1II1Iiii1I11 ( IIiIii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi1I11I1II = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( OOO00O )
  ooO0oo = re . sub ( '<[^<]+?>' , '' , IIi1I11I1II [ 0 ] ) . replace ( ' ' , '' )
  ooO0oo0o0 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( ooO0oo , ooO0oo )
  if ret == 'version' : return ooO0oo
  else : return ooO0oo0o0
def iIIIiiiI11I ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  Ooo0oO0 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ooo0oO0 : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I1iOo = name
  if Ooo0oO0 :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not oooooo0O000o ( url ) == True : o0Oo0oOooOoOo ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1iOo , '' , 'Please Wait' )
   I1 = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( I1 )
   except : pass
   downloader . download ( url , I1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1 + '")' )
  else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + O00o0O00 * ooOOOoO
 if 2 - 2: ooOoO0O00 - O0OOOoOoo0 + oOo0O0Ooo . I11i * I11i / OOooOOo
 if 93 - 93: ooOoO0O00
 if 53 - 53: ii + I1ii11iIi11i + oO0oo0o
def I1IiiiiI ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( OOO00O )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  i1I1ii11i1Iii = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + i1I1ii11i1Iii )
  I1I111iI ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , i1I1ii11i1Iii )
  if 29 - 29: ooOOOoO
def I1I111iI ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  Ooo0oO0 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ooo0oO0 : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1iOo = name
  if Ooo0oO0 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not oooooo0O000o ( url ) == True : o0Oo0oOooOoOo ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1iOo , '' , 'Please Wait' )
   I1 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( I1 )
   except : pass
   downloader . download ( url , I1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I1 + '")' )
  else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 66 - 66: I1ii11iIi11i
 if 97 - 97: ooOoO0O00 - ii / ii1ii11IIIiiI * oOo0O0Ooo
def oO0oOo00o00oO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 95 - 95: oOo0O0Ooo
 if 88 - 88: ooOOOoO % oO0o + ii1ii11IIIiiI + ii1ii11IIIiiI * IIiIiII11i
def o0Oo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 30015 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 57 - 57: O00o0O00 / I1ii11iIi11i
def oO0O0Ooo ( url , iconimage , fanart ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 iIIII1iIIii = url
 II1III1I1I1Ii = iconimage
 fanart = fanart
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for o0OO0o0o00o , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp4' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Watch VIDEO' , url + '/' + o0OO0o0o00o , 222 , II1III1I1I1Ii , fanart , '' )
  if 'description' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Read Description' , url + '/' + o0OO0o0o00o , 30017 , II1III1I1I1Ii , fanart , '' )
  if 'images' in oO00oooOOoOo0 :
   I1IIII1i ( 'View Images' , url + '/' + o0OO0o0o00o , 30018 , II1III1I1I1Ii , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Android' , url + '/' + o0OO0o0o00o , 30016 , II1III1I1I1Ii , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Pc' , url + '/' + o0OO0o0o00o , 30019 , II1III1I1I1Ii , fanart , '' )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 4 - 4: IIiIiII11i . I11O0O0oOO00O00o + iI1ii11iIi1i * ii1ii11IIIiiI . O0OOOoOoo0
def oOoOo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  oO0OO ( url )
  if 88 - 88: OOooOOo - Ii % I11i * I11O0O0oOO00O00o + Ii1I
def Oo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  iIIIiIi1I1i ( url )
  if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + O00o0O00
def OooOOOO0O0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'desc="([^"]*)"' ) . findall ( OOO00O )
 for i1IIi1i1Ii1 in IIi1I11I1II :
  O0O0Oooo0o ( 'Description:' , i1IIi1i1Ii1 )
  if 45 - 45: iI11I1II1I1I . oO0oo0o / OOooOOo / ooOOOoO
def ooOOOoOoOOO0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 url = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for o0OO0o0o00o , oO00oooOOoOo0 in IIi1I11I1II :
  if 'png' in oO00oooOOoOo0 :
   iIiIIi1 ( 'image' , '' , '' , url + '/' + o0OO0o0o00o , url + '/' + o0OO0o0o00o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 5 - 5: O00o0O00
def I1i1iIi1I1 ( name , url , description ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1 = os . path . join ( I1i , name + '.zip' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 OOO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO0
 print '======================================='
 extract . all ( I1 , OOO0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Oo0o0O00 ( )
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
 if 43 - 43: iI11I1II1I1I / IIiIiII11i % I11i - O00o0O00
def iIIIiIi1I1i ( url ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1 = os . path . join ( I1i , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 OOO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO0
 print '======================================='
 extract . all ( I1 , OOO0 , o0oOoO00o )
 oO0O000oOo ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOOO ( )
 if 18 - 18: O0OOOoOoo0 % Ii . iI11I1II1I1I - Ii1IIIi1
def oO0OO ( url ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I1 = os . path . join ( I1i , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 OOO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO0
 print '======================================='
 extract . all ( I1 , OOO0 , o0oOoO00o )
 oO0O000oOo ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOOO ( )
 if 80 - 80: oOo0O0Ooo + oO0oo0o - ooOoO0O00 . iI1ii11iIi1i / I11i / oOo0O0Ooo
def I1Iiii ( name , url , description ) :
 OOO0 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 I1 = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OOO0
 print '======================================='
 extract . all ( I1 , OOO0 , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OoOOOO ( )
 if 34 - 34: iI1ii11iIi1i * OOooOOo - ooOOOoO - oOo0O0Ooo - iI1ii11iIi1i
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
  Ii1iIi111I1i = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  o0Oo00 . write ( Ii1iIi111I1i . rstrip ( '\r\n' ) + '\n' )
def OoOOOO ( ) :
 iiiiII1I = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiiiII1I == 0 : return
 elif iiiiII1I == 1 : pass
 I1III111i = I1I1i1I ( )
 oo00oOO000oO0 ( "Platform: " + str ( I1III111i ) )
 os . _exit ( 1 )
 oo00oOO000oO0 ( "Force close failed!  Trying alternate methods." )
 if I1III111i == 'osx' :
  oo00oOO000oO0 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1III111i == 'linux' :
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
 elif I1III111i == 'android' :
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
 elif I1III111i == 'windows' :
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
  if 4 - 4: ooOoO0O00 + O0OOOoOoo0 + ooOoO0O00
  if 31 - 31: iI1ii11iIi1i
  if 78 - 78: Ii + I11i + ii1ii11IIIiiI / I11i % iI11I1II1I1I % ooOOOoO
def Oo0O0Oo00O ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( url ) :
  for file in OOOooo0OooOoO :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooO0oO00O0o = open ( ( os . path . join ( iIoo0ooooO , file ) ) ) . read ( )
    iiIIi = ooO0oO00O0o . replace ( I11 , 'special://home/' )
    o0Oo00 = open ( ( os . path . join ( iIoo0ooooO , file ) ) , mode = 'w' )
    o0Oo00 . write ( str ( iiIIi ) )
    o0Oo00 . close ( )
 OoOOOO ( )
 if 36 - 36: I11O0O0oOO00O00o . IIiIiII11i
def iIIiI1iiI ( ) :
 oOo0 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 oOo0 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 18 - 18: Ii1IIIi1 - oO0oo0o % Ii1IIIi1 / I11O0O0oOO00O00o
def O0Oo00OO00Ooo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def OO0O00OoOOOo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def Oo0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , II1III1I1I1Ii )
def o0OOOOO0O ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  I1I1I1IIi1III ( url )
def I1I1IiIi1 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo
 oOO0o0oo0 = 'https://www.radionomy.com/en/search/index?query=' + ( o0OOOo ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + i1I1ii11i1Iii , 70005 , II1III1I1I1Ii )
  if 78 - 78: O00o0O00 + Ii1IIIi1 . ooOOOoO
  if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
def o0o0O0Oo ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , 'http://www.listenlive.eu/' + i1I1ii11i1Iii , 10111113 , III1iII1I1ii + 'radio.png' )
def IiiIIi ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'radio.png' )
  if 71 - 71: ooOOOoO + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + i1I1ii11i1Iii , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0oOOO0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii in IIi1I11I1II :
  if 'ol.gif' in II1III1I1I1Ii :
   pass
  elif 'link_block_' in II1III1I1I1Ii :
   pass
  elif '.png' in II1III1I1I1Ii :
   pass
  else :
   oOo0 ( ( II1III1I1I1Ii ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in OooOoooOo :
  oOo0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOOiI1iIIII1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 57 - 57: OOooOOo . iI11I1II1I1I % O0OOOoOoo0 % iI1ii11iIi1i * OOooOOo
  if 8 - 8: OOooOOo . O0OOOoOoo0 % oO0oo0o . oOo0O0Ooo % oOo0O0Ooo . iI1ii11iIi1i
def I1I11ii ( ) :
 OOoOoo00Oo ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 OOoOoo00Oo ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
def II1 ( ) :
 OOoOoo00Oo ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 OOoOoo00Oo ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 OOoOoo00Oo ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 27 - 27: iI1ii11iIi1i + oOo0O0Ooo * iI11I1II1I1I . ii * OOooOOo
def OOOo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , o0ooOo00O in IIi1I11I1II :
  if 'Parent' in oO00oooOOoOo0 :
   pass
  elif '2' in o0ooOo00O :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: iI11I1II1I1I + Ii * oO0o * O0OOOoOoo0 % O00o0O00
def I1I11IiiI ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , o0ooOo00O in IIi1I11I1II :
  if o0OOOo in oO00oooOOoOo0 . lower ( ) :
   if '1' in o0ooOo00O :
    OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in o0ooOo00O :
    OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in o0ooOo00O :
    OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 40 - 40: I11O0O0oOO00O00o % ii - O00o0O00 + I11i / O00o0O00
    if 84 - 84: o0o00Oo0O
def iiii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , o0ooOo00O in IIi1I11I1II :
  if '1' in o0ooOo00O :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in o0ooOo00O :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in o0ooOo00O :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i1I1ii11i1Iii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 10 - 10: Ii1IIIi1 - oO0oo0o * iI11I1II1I1I % iI11I1II1I1I * ooOOOoO - Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97: IIiIiII11i % ii1ii11IIIiiI + ii1ii11IIIiiI - oO0o / iI1ii11iIi1i * oOo0O0Ooo
def iIii1iII1Ii ( url ) :
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
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 50 - 50: iI1ii11iIi1i
   if 22 - 22: I11O0O0oOO00O00o * o0o00Oo0O . IIiIiII11i - oO0o
   if 90 - 90: oO0oo0o
def O00OOo000Oo0 ( url ) :
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
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0OO0o0o00o + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 82 - 82: ii1ii11IIIiiI - O00o0O00 + oO0o
   if 64 - 64: I11i . o0o00Oo0O * iI1ii11iIi1i + ii - I1ii11iIi11i . ii
def OOoO0oo0O ( ) :
 OOoOoo00Oo ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 OOoOoo00Oo ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 OOoOoo00Oo ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 49 - 49: I11i
def II1ii1ii11I1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii in IIi1I11I1II :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in II1III1I1I1Ii :
   pass
  else :
   OOoOoo00Oo ( II1III1I1I1Ii , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i1I1ii11i1Iii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + II1III1I1I1Ii + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 88 - 88: Ii1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: iI11I1II1I1I
 if 66 - 66: Ii * iI11I1II1I1I % ii
def iIiI1iI1i1I ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 82 - 82: oOo0O0Ooo % Ii1I * Ii1IIIi1 . iI1ii11iIi1i % oOo0O0Ooo - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: Ii1I % ii1ii11IIIiiI + Ii
def I1iIiiiI1 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if o0OOOo in oO00oooOOoOo0 . lower ( ) :
   if '</a>' in oO00oooOOoOo0 :
    pass
   elif '(' in oO00oooOOoOo0 :
    OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 42 - 42: O00o0O00 % oO0oo0o / oO0o - oO0oo0o * Ii
    if 19 - 19: oO0oo0o * oOo0O0Ooo % Ii
def iiI1Ii1I ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 28 - 28: O00o0O00 % O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: Ii % oO0oo0o
 if 29 - 29: Ii1IIIi1 + Ii % I11O0O0oOO00O00o
def oOo00Ooo0o0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  o0OO0o0o00o = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( o0OO0o0o00o )
  if 33 - 33: I11O0O0oOO00O00o
def oOO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '<p align' in oO00oooOOoOo0 :
   pass
  elif '&nbsp;' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 15 - 15: I1ii11iIi11i + I11O0O0oOO00O00o . O0OOOoOoo0 - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: oOo0O0Ooo / oO0oo0o * iI1ii11iIi1i
 if 64 - 64: O0OOOoOoo0 / o0o00Oo0O * OOooOOo * O0OOOoOoo0
def O00oo ( ) :
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
def OoOo0oO0o ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 o0OoOo00ooO = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , II1III1I1I1Ii , II1III1I1I1Ii , oO00oooOOoOo0 )
 for url , oO00oooOOoOo0 in o0OoOo00ooO :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def i111i ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 II1III1i1iiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 I11i11i1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIIi1I1IIii1II )
 OOOii1i1iiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in I11i11i1 :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , oO00oooOOoOo0 in II1III1i1iiI :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def Oo0oOo0ooOOOo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 71 - 71: IIiIiII11i - iI1ii11iIi1i - Ii1IIIi1 * o0o00Oo0O * ooOOOoO
def ii1ii1I1IIi1 ( ) :
 oOo0 ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 55 - 55: oOo0O0Ooo
def Ii1i1 ( ) :
 oOo0 ( '[COLOR' + iiI1IiI + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 oOo0 ( '[COLOR' + iiI1IiI + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 65 - 65: oO0oo0o + Ii1I / O00o0O00
def oo0oo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '?c=' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 49 - 49: Ii % OOooOOo + ii1ii11IIIiiI . IIiIiII11i % Ii1IIIi1 * O00o0O00
def oooo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , I11iII , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Genre' in url :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 27 - 27: Ii - oOo0O0Ooo
def iii1IIiI ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , I11iII , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I11iII )
  if 33 - 33: I11O0O0oOO00O00o
def oOo00OoO0O ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , I11iII , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , I11iII )
  if 69 - 69: iI11I1II1I1I * oOo0O0Ooo - Ii1IIIi1 + o0o00Oo0O + o0o00Oo0O
  if 65 - 65: ii1ii11IIIiiI / Ii / oO0o - O00o0O00
  if 9 - 9: oOo0O0Ooo / ii1ii11IIIiiI - I1ii11iIi11i * iI11I1II1I1I
  if 86 - 86: IIiIiII11i + O0OOOoOoo0 + ooOOOoO
  if 9 - 9: O0OOOoOoo0 + IIiIiII11i % O0OOOoOoo0 % ooOOOoO + iI11I1II1I1I
def oO00 ( ) :
 if 7 - 7: o0o00Oo0O % ii1ii11IIIiiI + Ii1I + iI1ii11iIi1i % ii . I1ii11iIi11i
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , OO0o , '' )
 if 56 - 56: Ii1IIIi1
def oOooo00O ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIIi1I1IIii1II )
 if 87 - 87: O00o0O00 + I11i . Ii1IIIi1 - ii
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if o0OOOo in oO00oooOOoOo0 . lower ( ) :
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
    if 6 - 6: iI11I1II1I1I * ii
    if 28 - 28: I1ii11iIi11i * I11i / ii1ii11IIIiiI
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: o0o00Oo0O / I11i % Ii1IIIi1 * oOo0O0Ooo % O00o0O00
def o0oOOOO0 ( url ) :
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
 if 11 - 11: ooOoO0O00
def I1III1iIi ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii in OooOoooOo :
  OoO00O0 = II1III1I1I1Ii
 I1Iii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oo000o0000oO )
 for url in I1Iii :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10007 , OoO00O0 )
  if 14 - 14: O00o0O00
  if 79 - 79: iI1ii11iIi1i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: iI11I1II1I1I
def Ooi111i1iIi1 ( url , IMAGE ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   OoO0oO ( url )
   if 10 - 10: ooOoO0O00 . IIiIiII11i / I11i * O0OOOoOoo0
   if 10 - 10: I11O0O0oOO00O00o - I1ii11iIi11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: ii * I1ii11iIi11i + ooOoO0O00
def OoO0oO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  I1I1I1IIi1III ( url )
  if 23 - 23: O0OOOoOoo0
  if 13 - 13: iI11I1II1I1I
  if 77 - 77: Ii - iI11I1II1I1I / oO0oo0o / O0OOOoOoo0 / oO0o
def ooo0O0o0OoOO ( ) :
 if 9 - 9: oO0o
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , OO0o , '' )
 if 60 - 60: ii1ii11IIIiiI
def oOO0o00o0Oo0O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'elete' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 222 , II1III1I1I1Ii )
   if 41 - 41: oO0o - IIiIiII11i + iI1ii11iIi1i
def iIiiii1 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ooOoo000oO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , i1I1iIoOOoO , i1iII1IiiIiI1 in ooOoo000oO :
  for o0OOOo in i1I1iIoOOoO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOo0Oo0O0O = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for i1I1ii11i1Iii , oO00oooOOoOo0 in oOo0Oo0O0O :
    if 'tube' in i1I1ii11i1Iii :
     pass
    elif 'stage' in i1I1ii11i1Iii :
     OOOoOO ( '[COLOR' + iiI1IiI + ']' + i1I1iIoOOoO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + II1III1I1I1Ii , )
    elif 'vee' in i1I1ii11i1Iii :
     pass
     if 48 - 48: I1ii11iIi11i - O0OOOoOoo0 + I1ii11iIi11i - oOo0O0Ooo * Ii . Ii1IIIi1
def I1iIIIiI ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 ooOoo000oO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , i1I1iIoOOoO , i1iII1IiiIiI1 in ooOoo000oO :
  oOo0Oo0O0O = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in oOo0Oo0O0O :
   if 'tube' in i1I1ii11i1Iii :
    pass
   elif 'stage' in i1I1ii11i1Iii :
    OOOoOO ( '[COLOR' + iiI1IiI + ']' + i1I1iIoOOoO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + II1III1I1I1Ii )
   elif 'vee' in i1I1ii11i1Iii :
    pass
    if 60 - 60: oOo0O0Ooo . Ii + OOooOOo / Ii1I * IIiIiII11i * O00o0O00
    if 59 - 59: I1ii11iIi11i + Ii1IIIi1 - O00o0O00 . I11i + oOo0O0Ooo % oO0oo0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 37 - 37: Ii1IIIi1 + Ii1IIIi1 % I11i
def iIi1i1iIi1Ii1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i11111I1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIIi1I1IIii1II )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i11111I1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i11111I1I :
  I1I1I1IIi1III ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 66 - 66: oO0o % I11i
  if 21 - 21: OOooOOo - ii % Ii
  if 71 - 71: ooOoO0O00 - I11O0O0oOO00O00o * ii1ii11IIIiiI + oO0oo0o - oO0o % Ii1I
  if 63 - 63: iI11I1II1I1I + O00o0O00 . oO0o / oOo0O0Ooo
  if 84 - 84: ooOoO0O00
  if 42 - 42: IIiIiII11i - oO0o - ii . Ii1IIIi1 / OOooOOo
  if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
def O00O ( ) :
 if 2 - 2: oO0oo0o . ii1ii11IIIiiI * I1ii11iIi11i + o0o00Oo0O - I11O0O0oOO00O00o * iI11I1II1I1I
 II111i1ii1iII ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 II111i1ii1iII ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 75 - 75: iI11I1II1I1I + ii
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 97 - 97: Ii1I / I1ii11iIi11i + ii1ii11IIIiiI
def i111I11i1I ( ) :
 II111i1ii1iII ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 II111i1ii1iII ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 85 - 85: O00o0O00 * ooOoO0O00 % oOo0O0Ooo - O0OOOoOoo0
 I1I1II1I11 ( 'movies' , 'MAIN' )
def I11I1ii1i ( ) :
 if 22 - 22: oO0oo0o * iI1ii11iIi1i * Ii + Ii1IIIi1 * OOooOOo * oO0o
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 O000OOO00Ooo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 65 - 65: iI11I1II1I1I % oO0oo0o + o0o00Oo0O / ii
 for O0000oO0o00 in O000OOO00Ooo :
  oo000o = I11i1I1I + O0000oO0o00 + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( oo000o )
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    OO00o0oOO ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , oOo0O , I1I )
    if 27 - 27: I1ii11iIi11i
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 95 - 95: I11O0O0oOO00O00o
    if 44 - 44: O00o0O00 + I11O0O0oOO00O00o . ooOOOoO / IIiIiII11i % iI11I1II1I1I + ooOOOoO
def O0OOo ( ) :
 if 30 - 30: ii1ii11IIIiiI - I1ii11iIi11i
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 O000OOO00Ooo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 69 - 69: iI11I1II1I1I . O00o0O00 / O00o0O00
 for O0000oO0o00 in O000OOO00Ooo :
  Oooooo0000 = I11i1I1I + O0000oO0o00 + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( Oooooo0000 )
  IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , I1I , i1I1ii11i1Iii , II1III1I1I1Ii , oOo0O , OooO0OOo in IIi1I11I1II :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    II111i1ii1iII ( oO00oooOOoOo0 , i1I1ii11i1Iii , OooO0OOo , II1III1I1I1Ii , oOo0O , I1I )
    if 51 - 51: iI11I1II1I1I * I11i / iI11I1II1I1I . iI11I1II1I1I . Ii1IIIi1 * I11O0O0oOO00O00o
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 93 - 93: oO0oo0o * iI1ii11iIi1i
    if 27 - 27: oOo0O0Ooo * O0OOOoOoo0
def oO0ooooo0O00 ( ) :
 if 5 - 5: OOooOOo % Ii1IIIi1 + ooOOOoO
 oo000o0000oO = O0i1II1Iiii1I11 ( I11i1I1I + 'spongemain.php' )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , I1I , i1I1ii11i1Iii , II1III1I1I1Ii , oOo0O , OooO0OOo in IIi1I11I1II :
  II111i1ii1iII ( oO00oooOOoOo0 , i1I1ii11i1Iii , OooO0OOo , II1III1I1I1Ii , oOo0O , I1I )
  I1I1II1I11 ( 'movies' , 'MAIN' )
def iiiIi1II1III ( url ) :
 if 8 - 8: ooOOOoO % O00o0O00 . I1ii11iIi11i % O0OOOoOoo0 - Ii1IIIi1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iII1Ii1I1i1 = ( '%s%s' % ( OooOooo0 , url ) )
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in IIi1I11I1II :
  oo0OoOO0o0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
  for OO0OOO00 in oo0OoOO0o0o :
   if OO0OOO00 == url :
    oO00oooOOoOo0 = ( '[COLORred]Watched - [/COLOR]' + oO00oooOOoOo0 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  OO00o0oOO ( oO00oooOOoOo0 , url , 222 , iiiI1I1iIIIi1 , i11i , I1I )
  if 62 - 62: Ii + OOooOOo + ooOoO0O00
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 69 - 69: OOooOOo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . ii1ii11IIIiiI
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def OooOo ( url ) :
 if 67 - 67: I1ii11iIi11i / o0o00Oo0O
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , I1I , url , II1III1I1I1Ii , oOo0O , OooO0OOo in IIi1I11I1II :
  II111i1ii1iII ( oO00oooOOoOo0 , url , OooO0OOo , II1III1I1I1Ii , oOo0O , I1I )
  if 88 - 88: OOooOOo - O00o0O00
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 63 - 63: ooOOOoO * ii
  if 19 - 19: ooOOOoO - I11i . iI11I1II1I1I . OOooOOo / O00o0O00
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: OOooOOo - O0OOOoOoo0 - O00o0O00 + I1ii11iIi11i % iI11I1II1I1I / Ii
def OO00o0oOO ( name , url , mode , iconimage , fanart , description ) :
 if 12 - 12: O0OOOoOoo0
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOOOO00 . setProperty ( "Fanart_Image" , fanart )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = False )
 return i11IiI1iiI11
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + ii1ii11IIIiiI
def II111i1ii1iII ( name , url , mode , iconimage , fanart , description ) :
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * oO0oo0o
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOOOO00 . setProperty ( "Fanart_Image" , fanart )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = True )
 return i11IiI1iiI11
if 85 - 85: IIiIiII11i . O0OOOoOoo0 % O00o0O00 % I11O0O0oOO00O00o
if 80 - 80: oO0oo0o * I11O0O0oOO00O00o / iI11I1II1I1I % oO0oo0o / iI11I1II1I1I
if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * Ii1IIIi1 . Ii * o0o00Oo0O
if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + ooOOOoO
if 27 - 27: O00o0O00
if 52 - 52: ii1ii11IIIiiI % OOooOOo + iI11I1II1I1I * oO0oo0o . iI1ii11iIi1i
if 95 - 95: iI11I1II1I1I . ooOOOoO - ii * oO0o / I11i
if 74 - 74: oO0oo0o
if 34 - 34: Ii1IIIi1
if 44 - 44: ooOoO0O00 % oOo0O0Ooo % I11i
if 9 - 9: I1ii11iIi11i % ii - iI1ii11iIi1i
if 43 - 43: oO0o % oO0o
if 46 - 46: I1ii11iIi11i % iI11I1II1I1I . Ii1IIIi1 . o0o00Oo0O * O0OOOoOoo0 / ii
if 7 - 7: oO0oo0o - o0o00Oo0O * I11O0O0oOO00O00o - I11i - IIiIiII11i
if 41 - 41: oOo0O0Ooo - ii1ii11IIIiiI % IIiIiII11i . ii1ii11IIIiiI - I11O0O0oOO00O00o
def i1I111Ii ( string ) :
 if Ii1iIiII1ii1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 31 - 31: oOo0O0Ooo
def O0oI1ii1Ii1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoOoO = [ ]
 try :
  if 13 - 13: OOooOOo % O0OOOoOoo0
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  i1I111Ii ( 'Making Favorites File' )
  OoOoO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooO0oO00O0o = open ( I1IIiiIiii , "w" )
  ooO0oO00O0o . write ( json . dumps ( OoOoO ) )
  ooO0oO00O0o . close ( )
 else :
  i1I111Ii ( 'Appending Favorites' )
  ooO0oO00O0o = open ( I1IIiiIiii ) . read ( )
  O0OOOOo0 = json . loads ( ooO0oO00O0o )
  O0OOOOo0 . append ( ( name , url , iconimage , fanart , mode ) )
  iiIIi = open ( I1IIiiIiii , "w" )
  iiIIi . write ( json . dumps ( O0OOOOo0 ) )
  iiIIi . close ( )
  if 72 - 72: I11i % oOo0O0Ooo / Ii1IIIi1 - o0o00Oo0O + I11O0O0oOO00O00o
  if 83 - 83: o0o00Oo0O
def oOOOOOo ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  OoOoO = [ ]
  i1I111Ii ( 'Making Favorites File' )
  OoOoO . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ooO0oO00O0o = open ( I1IIiiIiii , "w" )
  ooO0oO00O0o . write ( json . dumps ( OoOoO ) )
  ooO0oO00O0o . close ( )
 else :
  i1I11ii = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  o0ooO00O0O = len ( i1I11ii )
  for iiiI1iI1 in i1I11ii :
   oO00oooOOoOo0 = iiiI1iI1 [ 0 ]
   i1I1ii11i1Iii = iiiI1iI1 [ 1 ]
   iiiI1I1iIIIi1 = iiiI1iI1 [ 2 ]
   try :
    I1oOoO0OOO00O = iiiI1iI1 [ 3 ]
    if I1oOoO0OOO00O == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     I1oOoO0OOO00O = iiiI1I1iIIIi1
    else :
     I1oOoO0OOO00O = oOo0O
   try : OOOOO0o0OOo = iiiI1iI1 [ 5 ]
   except : OOOOO0o0OOo = None
   try : I11I11I11IiIi = iiiI1iI1 [ 6 ]
   except : I11I11I11IiIi = None
   if 62 - 62: Ii1I . OOooOOo / iI11I1II1I1I * ii1ii11IIIiiI
   if iiiI1iI1 [ 4 ] == 0 :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , '' , iiiI1I1iIIIi1 , oOo0O , '' , 'fav' )
   else :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , iiiI1iI1 [ 4 ] , iiiI1I1iIIIi1 , oOo0O , '' , 'fav' )
    if 18 - 18: iI1ii11iIi1i
def II1IIi1iII1i ( name ) :
 O0OOOOo0 = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for iii in range ( len ( O0OOOOo0 ) ) :
  if O0OOOOo0 [ iii ] [ 0 ] == name :
   del O0OOOOo0 [ iii ]
   iiIIi = open ( I1IIiiIiii , "w" )
   iiIIi . write ( json . dumps ( O0OOOOo0 ) )
   iiIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 26 - 26: oOo0O0Ooo
 if 41 - 41: oOo0O0Ooo - Ii
def oOOOO ( ) :
 iIiI1 = os . path . join ( O0O , 'addons.ini' )
 iII1IiiIIII = open ( iIiI1 , "w+" )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIIi1I1IIii1II )
 iII1IiiIIII . write ( r'[' + IiII + ']' + '\n' )
 for oO00oooOOoOo0 , II1III1I1I1Ii , Oo000o , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I11iI = ( oO00oooOOoOo0 + '=plugin://' + IiII + '/?url=' + i1I1ii11i1Iii + '&mode=10012&name=' + ( oO00oooOOoOo0 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( II1III1I1I1Ii ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( II1III1I1I1Ii ) . replace ( ' ' , '' ) + '+&amp;description=' )
  iII1IiiIIII . write ( I11iI + '\n' )
  if 79 - 79: o0o00Oo0O + oO0oo0o
  if 21 - 21: O0OOOoOoo0 + I11i % ii1ii11IIIiiI + Ii + Ii1IIIi1 + IIiIiII11i
def oOO0OOOOOo0Oo ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + '247.png' , III1iII1I1ii + '247.png' , '' )
def iIi ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def Ii1Ii1Ii1IIIi ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def OO ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def O000O0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi1I11I1II = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 65 - 65: Ii
  if 84 - 84: I1ii11iIi11i % Ii1IIIi1 % ii + O00o0O00 % Ii
def Iiii1Ii ( ) :
 if 62 - 62: ooOoO0O00 % OOooOOo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 37 - 37: I11O0O0oOO00O00o * ooOoO0O00
def I1IIII ( ) :
 if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / iI1ii11iIi1i
 oo000o0000oO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 , ooo0O in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + '  -  ' + ( ooo0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 10023 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 20 - 20: O00o0O00 * IIiIiII11i - OOooOOo - oO0oo0o * ii1ii11IIIiiI
  if 6 - 6: O0OOOoOoo0 + O00o0O00 / I1ii11iIi11i + ooOOOoO % IIiIiII11i / oO0o
  if 45 - 45: ii
def I1oo ( ) :
 if 17 - 17: o0o00Oo0O - OOooOOo
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
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
def I1I1IIiiii1ii ( url ) :
 iIIII1iIIii = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIIi1I1IIii1II = cloudflare . source ( iIIII1iIIii )
 IIi1I11I1II = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 92 - 92: oO0oo0o / O00o0O00 . Ii1I
  if 30 - 30: iI1ii11iIi1i . Ii1I / O00o0O00
  if 2 - 2: ooOOOoO % oOo0O0Ooo - ii1ii11IIIiiI
  if 79 - 79: ii / Ii1I . o0o00Oo0O
def oOoO0Oo0 ( ) :
 if 7 - 7: O0OOOoOoo0 + iI1ii11iIi1i
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0OOOo ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = cloudflare . source ( i1I1ii11i1Iii )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if o0OOOo in oO00oooOOoOo0 . lower ( ) :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10022 , III1iII1I1ii + 'dtv.png' )
   if 32 - 32: iI11I1II1I1I % oOo0O0Ooo / Ii + O00o0O00 - I11i . Ii1IIIi1
   if 86 - 86: ooOoO0O00 / iI1ii11iIi1i * oOo0O0Ooo
   if 67 - 67: Ii1I * Ii1I / oO0oo0o * ii + OOooOOo
def ooooo0o0oo0Ooo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for o0OO0o0o00o , iI1i , i11I , oO00oooOOoOo0 in IIi1I11I1II :
  o0oO0o0oo0O0 = ( i11I ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0oo00oOOO0o = ( iI1i ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1iI111iiIIiI1I = 'Season ' + O0oo00oOOO0o + 'Episode ' + o0oO0o0oo0O0 + oO00oooOOoOo0
  ooO00Oo ( II1iI111iiIIiI1I , o0OO0o0o00o )
  if 41 - 41: Ii - ooOoO0O00 / I1ii11iIi11i * ooOOOoO / ii1ii11IIIiiI - I1ii11iIi11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 56 - 56: o0o00Oo0O
  if 45 - 45: OOooOOo - oO0o - OOooOOo
def ooO00Oo ( name , url ) :
 o0OO0o0o00o = url
 IIiiI = name
 O0 = cloudflare . source ( o0OO0o0o00o )
 OooOoooOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for i11111I1I , iII11iiiiiii in OooOoooOo :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + IIiiI + iII11iiiiiii + '[/COLOR]' , i11111I1I , 10012 , III1iII1I1ii + 'dtv.png' )
  if 82 - 82: I11O0O0oOO00O00o / O0OOOoOoo0 * I11O0O0oOO00O00o % Ii * IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: oO0o + O00o0O00 - I11i + iI11I1II1I1I % I1ii11iIi11i
 if 23 - 23: I11i + iI1ii11iIi1i % OOooOOo % oOo0O0Ooo % ii
def OOOOoo00OO0O0Ooo0 ( ) :
 if 93 - 93: O0OOOoOoo0
 if 34 - 34: oO0oo0o - O0OOOoOoo0 * I1ii11iIi11i / I11i
 if 19 - 19: Ii1I
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
 if 52 - 52: oO0o * ii
 if 12 - 12: o0o00Oo0O + ooOOOoO * ooOoO0O00 . oO0o
 if 71 - 71: ii1ii11IIIiiI - I11i - O00o0O00
 if 28 - 28: iI11I1II1I1I
 if 7 - 7: I11i % ooOOOoO * OOooOOo
 if 58 - 58: ooOOOoO / I11O0O0oOO00O00o + IIiIiII11i % Ii1IIIi1 - ii
 if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * oO0oo0o
 if 30 - 30: I11O0O0oOO00O00o % OOooOOo / Ii1I * o0o00Oo0O * iI1ii11iIi1i . oOo0O0Ooo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 46 - 46: OOooOOo - o0o00Oo0O
 if 70 - 70: I11O0O0oOO00O00o + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * I11O0O0oOO00O00o
def ii1i11ii ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iII1iii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iII1iii ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 11 - 11: I1ii11iIi11i - o0o00Oo0O
def OOoI111 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 65 - 65: I1ii11iIi11i * o0o00Oo0O / iI1ii11iIi1i . ii1ii11IIIiiI % I1ii11iIi11i
def i1Ii1i1 ( url ) :
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
  if 80 - 80: ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
  if 94 - 94: ooOoO0O00
def iiIIi1 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIiI11i1I11111 = 'http://www.watchseries.ac/search/' + o0OOOo . replace ( ' ' , '%20' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooIiI11i1I11111 )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'watch online' in oO00oooOOoOo0 :
   pass
  else :
   print i1I1ii11i1Iii
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , II1III1I1I1Ii , '' , '' )
   if 34 - 34: oOo0O0Ooo * OOooOOo * oO0oo0o + Ii1I
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 39 - 39: Ii1I / ooOoO0O00 * ooOOOoO - oOo0O0Ooo
def OoOoooo0O ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 , i11I , I1I in IIi1I11I1II :
  OoO0O = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i11I ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + OoO0O + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , II1III1I1I1Ii , '' , I1I )
  if 98 - 98: Ii / oOo0O0Ooo * I11i / ii1ii11IIIiiI
def o0OOoOo0oo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OoO0O = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + OoO0O + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 64 - 64: ooOoO0O00
def I1ii1i1iiii ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , II1III1I1I1Ii , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 45 - 45: iI1ii11iIi1i / O0OOOoOoo0 . ii + oO0o
def O00oO000Oo0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 iII1iii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for iI1i , ooOoo000oO in iII1iii :
  IIi1I11I1II = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( ooOoo000oO ) )
  for url , oO00oooOOoOo0 in IIi1I11I1II :
   OoO0O = ( iI1i ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + OoO0O + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: I1ii11iIi11i + o0o00Oo0O - iI11I1II1I1I
class iiI1 ( ) :
 if 50 - 50: O0OOOoOoo0 * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 20 - 20: ii1ii11IIIiiI / I11i % OOooOOo
  OoO0O = name
  self . Get_Sources ( i1I1ii11i1Iii , OoO0O )
  if 69 - 69: ii1ii11IIIiiI - ooOoO0O00 % Ii1IIIi1 . O00o0O00 - O00o0O00
  if 65 - 65: O00o0O00 + IIiIiII11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( URL )
  IIi1I11I1II = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   URL = 'http://www.watchseries.ac/link/' + i1I1ii11i1Iii
   self . Get_site_link ( URL , season_name )
   if 61 - 61: Ii * oO0oo0o % I1ii11iIi11i * ii1ii11IIIiiI - ii - oO0o
 def Get_site_link ( self , url , season_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  OooOoooOo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  I1Iii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for url in IIi1I11I1II :
   self . main ( url , season_name )
  for url in OooOoooOo :
   self . main ( url , season_name )
  for url in I1Iii :
   self . main ( url , season_name )
   if 83 - 83: O0OOOoOoo0 / O00o0O00
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i11iI1 = 'DACLIPS'
   if i11iI1 in iiI1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , i11iI1 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    i11iI1 = 'FILEHOOT'
    if i11iI1 in iiI1 . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , i11iI1 )
   else :
    if 'thevideo.me' in url :
     i11iI1 = 'THEVIDEO'
     if i11iI1 in iiI1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , i11iI1 )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      i11iI1 = 'ALLMYVIDEOS'
      if i11iI1 in iiI1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , i11iI1 )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       i11iI1 = 'VIDSPOT'
       if i11iI1 in iiI1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , i11iI1 )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        i11iI1 = 'VODLOCKER'
        if i11iI1 in iiI1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , i11iI1 )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 35 - 35: I11O0O0oOO00O00o
         if 94 - 94: O0OOOoOoo0 / Ii % o0o00Oo0O
 def allmyvid ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 82 - 82: ii . iI1ii11iIi1i
 def vidspot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 26 - 26: oO0oo0o + ooOOOoO - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
 def thevideo ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 68 - 68: o0o00Oo0O
 def vodlocker ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 76 - 76: Ii1I
 def daclips ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 99 - 99: I11i
 def filehoot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0oO0oo0O in IIi1I11I1II :
   self . Printer ( O0oO0oo0O , season_name , source_name )
   if 1 - 1: iI1ii11iIi1i * OOooOOo * oO0o + I1ii11iIi11i
 def Printer ( self , Link , season_name , source_name ) :
  if 90 - 90: ii1ii11IIIiiI % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / O00o0O00 + I11O0O0oOO00O00o
  if Link in iiI1 . List :
   pass
  elif source_name in iiI1 . source_list :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   iiI1 . List . append ( Link )
   iiI1 . source_list . append ( source_name )
   if 89 - 89: oO0oo0o
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 87 - 87: Ii1IIIi1 % I1ii11iIi11i
   if 62 - 62: oO0o + O0OOOoOoo0 / Ii1IIIi1 * Ii
   if 37 - 37: Ii1IIIi1
   if 33 - 33: oO0o - o0o00Oo0O - oO0o
   if 94 - 94: ooOOOoO * I11O0O0oOO00O00o * ii / I11i . ooOOOoO - I11i
def I1I1i ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , OO0o , '' )
 if 45 - 45: O00o0O00
def iIiI1i111ii ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( oo000o0000oO )
 for IiIo000OOO00O , url , O0oooo000oO0 , OoOoO00OOoOOOo0 , oOoO00O , ii1I , I11I1I1i1i , o0Oo00 , ooO0oO00O0o , Oo0oOO0O00 , o00OOo0o0O in IIi1I11I1II :
  O0oooo000oO0 = O0oooo000oO0
  if 'Arsenal' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'arsenal-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                                  ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Bournemouth' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'afc-bournemouth.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                       ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Burnley' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'KEGnQWW.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                                   ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Chelsea' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'chelsea.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                                  ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Crystal' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'CrystalPalace.0.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                       ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Everton' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'Everton.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                                   ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Hull' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'hull-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                                 ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Leicester' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                       ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Liverpool' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'liverpool-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                               ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Manchester City' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'city-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '               ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Manchester United' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + '91.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '          ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Middlesbrough' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                 ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Southampton' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'southampton-fc-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                   ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Stoke City' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'stoke-city.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                          ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Sunderland' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'sunderland-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                        ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Swansea' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'swansea-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                    ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Tottenham' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '        ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Watford' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'watford-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '                              ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'Bromwich' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '   ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  elif 'West Ham' in O0oooo000oO0 :
   i1iIi = III1iII1I1ii + 'west-ham.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + IiIo000OOO00O + ' - ' + O0oooo000oO0 + '             ' + OoOoO00OOoOOOo0 + '        ' + oOoO00O + '        ' + ii1I + '        ' + I11I1I1i1i + '        ' + o0Oo00 + '        ' + ooO0oO00O0o + '        ' + Oo0oOO0O00 + '[/COLOR]'
  I1IIII1i ( str ( oO00oooOOoOo0 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , i1iIi , i1iIi , O0oooo000oO0 )
  if 14 - 14: Ii1IIIi1 - I11O0O0oOO00O00o * ii + O00o0O00 . IIiIiII11i
def i1i1I11i1I ( description ) :
 O0oooo000oO0 = description
 i1I1ii11i1Iii = ( 'http://www.fullmatchesandshows.com/?s=' + O0oooo000oO0 ) . replace ( ' ' , '%20' )
 O0oII1IIiiI1 ( i1I1ii11i1Iii )
 if 96 - 96: O00o0O00 + O00o0O00 % ooOOOoO % O00o0O00
def IiiI1I ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi1I11I1II = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1I1ii11i1Iii , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + II1III1I1I1Ii , OO0o , '' )
  if 3 - 3: IIiIiII11i - iI1ii11iIi1i % OOooOOo / oO0oo0o
def Ii1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iII1iii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for iII1iii in iII1iii :
  ooOO0OOO00o = re . compile ( '(.*?)</h2>' ) . findall ( str ( iII1iii ) )
  for OoOoO0ooooO0 in ooOO0OOO00o :
   OoOoO0ooooO0 = OoOoO0ooooO0
  IIII1ii1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iII1iii ) )
  for OOO0O0OOo , II1III1I1I1Ii , time , Iii1 in IIII1ii1 :
   ooOooo0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Iii1 )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + OoOoO0ooooO0 + ' - ' + OOO0O0OOo + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + II1III1I1I1Ii , OO0o , ( str ( ooOooo0 ) ) )
   if 96 - 96: I1ii11iIi11i / oO0oo0o . IIiIiII11i . I1ii11iIi11i
 I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if 91 - 91: IIiIiII11i . O00o0O00 + I11i
def I1iII1IIi1IiI ( ) :
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
 if 8 - 8: iI11I1II1I1I
def oOOo0ooO0 ( url ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 in IIi1I11I1II :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , II1III1I1I1Ii )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in OooOoooOo :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , II1III1I1I1Ii )
def O0oII1IIiiI1 ( url ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , OO0o , '' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 if 95 - 95: I11O0O0oOO00O00o + I11i * Ii1I
 if 85 - 85: Ii . ii - iI11I1II1I1I
 if 38 - 38: I11O0O0oOO00O00o . I11O0O0oOO00O00o * oO0oo0o / ii % O0OOOoOoo0
 if 80 - 80: oO0o / ooOOOoO * oOo0O0Ooo % ooOOOoO
 if 95 - 95: o0o00Oo0O / I11O0O0oOO00O00o . ii1ii11IIIiiI
 if 17 - 17: I11O0O0oOO00O00o
 if 56 - 56: O0OOOoOoo0 * I11i + I11O0O0oOO00O00o
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in OooOoooOo :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , II1III1I1I1Ii )
   if 48 - 48: ooOOOoO * oO0o % ii1ii11IIIiiI - I11O0O0oOO00O00o
def Oo0000OOO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIIi1I1IIii1II )
 for i11111I1I in IIi1I11I1II :
  Ooo0O0OO = ( i11111I1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  I1I1I1IIi1III ( 'http:' + Ooo0O0OO )
  if 38 - 38: ii1ii11IIIiiI
  if 25 - 25: iI11I1II1I1I % IIiIiII11i / I11O0O0oOO00O00o / Ii1I
  if 22 - 22: oO0oo0o * Ii1IIIi1
  if 4 - 4: OOooOOo - oO0oo0o + oOo0O0Ooo
def iiIiIiIiiIiI ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 8046 , II1III1I1I1Ii )
 for url in OooOoooOo :
  oOo0 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def iIi1i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  I1I1I1IIi1III ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / I11O0O0oOO00O00o + ii1ii11IIIiiI
def iIiII11 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 33 - 33: I11i * Ii1IIIi1 * iI11I1II1I1I + Ii . ii
def O0O0 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0oo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + II1III1I1I1Ii )
 for url in next :
  oOo0 ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 52 - 52: ooOOOoO % O0OOOoOoo0
  if 25 - 25: I11O0O0oOO00O00o / I11O0O0oOO00O00o % ii - Ii1I * oO0oo0o
def i1oooOoOoOO ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OOOoOO ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   OooOO ( 'http:' + url )
   if 32 - 32: Ii
def OooOO ( url ) :
 OOOoOO ( ( '[COLOR' + iiI1IiI + ']Pick Quality[/COLOR]' ) . replace ( '&#039;s' , '' ) , '' , 222 , III1iII1I1ii + 'documentary.png' )
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  url = ( url ) . replace ( '\/' , '/' )
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 222 , III1iII1I1ii + 'documentary.png' )
  if 6 - 6: OOooOOo / iI11I1II1I1I * ii1ii11IIIiiI / oOo0O0Ooo + o0o00Oo0O
def Ii1I1IIIiI1i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , II1III1I1I1Ii )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , url , 8048 , III1iII1I1ii + 'Next.png' )
def o0Oo00oOO ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in OooOoooOo :
  if 'rtd' in url :
   O0oo ( url )
   if 56 - 56: ooOOOoO * ii1ii11IIIiiI
def O0oo ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oo000o0000oO )
 for OOO00O , file in IIi1I11I1II :
  url = ( 'https://rtd.rt.com' + OOO00O + file )
  I1I1I1IIi1III ( url )
  if 98 - 98: I11O0O0oOO00O00o + o0o00Oo0O * ii1ii11IIIiiI + Ii - O00o0O00 - iI11I1II1I1I
  if 5 - 5: O00o0O00 % I1ii11iIi11i % ooOOOoO % O0OOOoOoo0
def I1IiiiI1I1Iii1Iiii ( ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( 'http://www.stream2watch.co/live-tv' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 , i1i1Ii1IiIII in IIi1I11I1II :
  oOo0 ( ( oO00oooOOoOo0 + '[COLOR' + iiI1IiI + ']' + i1i1Ii1IiIII + '[/COLOR]' ) , i1I1ii11i1Iii , 8086 , II1III1I1I1Ii )
  if 9 - 9: I11O0O0oOO00O00o - oO0oo0o + o0o00Oo0O / Ii1IIIi1 % ooOoO0O00
def oO000o0OO0OO0 ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8087 , II1III1I1I1Ii )
  if 23 - 23: Ii1IIIi1 - iI1ii11iIi1i
def iI1iii1iI1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  ooO ( url , oO00oooOOoOo0 )
  if 61 - 61: o0o00Oo0O
def ooO ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  print url
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 25 - 25: iI11I1II1I1I * I11O0O0oOO00O00o - oO0oo0o % Ii + iI1ii11iIi1i % oO0oo0o
def iiIIi1I1iIIIiiii ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i1I1ii11i1Iii , 3002 , 'http://www.solie.org/alibrary/' + II1III1I1I1Ii )
def O0oIi1iIiIi1I11 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + II1III1I1I1Ii )
def ii1I11 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 OOO0I1Ii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oo000o0000oO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , oO00oooOOoOo0 in OOO0I1Ii1 :
  oOo0 ( '[COLOR' + iiI1IiI + ']Season- ' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + II1III1I1I1Ii )
def O0oo0oOoO00 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  i1ii1iIi ( url )
def i1ii1iIi ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  I1I1I1IIi1III ( url )
  if 43 - 43: iI1ii11iIi1i + Ii1IIIi1 + ooOoO0O00 - OOooOOo + I11i
def OOOO00 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classicmovies.png' )
def o0I1iI111ii111i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( "v.src = '([^']*)';" ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  O0iIiIIIIIii ( url )
  if 83 - 83: iI11I1II1I1I
def Oo0O0O ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classictv.png' )
def IiIiiI1ii111 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'mp4' in url :
   I1I1I1IIi1III ( url )
 for url in OooOoooOo :
  yt . PlayVideo ( url )
  if 30 - 30: iI1ii11iIi1i + IIiIiII11i % ii
def oOo000O00O0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1I1ii11i1Iii , 8071 , III1iII1I1ii + 'streams.png' )
def iI1iiIii1I11I ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '(Free Access)' in oO00oooOOoOo0 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def Ii1IiiiI1ii ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , oO00oooOOoOo0 , url in IIi1I11I1II :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , II1III1I1I1Ii , oOo0O , '' )
  if 55 - 55: Ii1I
def oOoo0OO0 ( ) :
 OOoOoo00Oo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Genres' , 'http://www.xvideos.com' , 10106 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Search' , '' , 10107 , III1iII1I1ii + 'Jizbox.png' , '' , '' , )
 if 5 - 5: Ii * I1ii11iIi11i
def i111 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 o0o0oO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in o0o0oO :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , IIiI1 in IIi1I11I1II :
  OOoOoo00Oo ( ( oO00oooOOoOo0 + ' - No of Videos : ' + ( IIiI1 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * I11O0O0oOO00O00o
def O0o0O0O0O ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 o0o0oO = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in o0o0oO :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 , oOO in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + '--' + oOO , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( II1III1I1I1Ii ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 79 - 79: ooOOOoO + ooOOOoO + iI1ii11iIi1i
  if 39 - 39: o0o00Oo0O - ii
def oo0O00ooo0o ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 , IIi , ii1i1Iii in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + ' - Porn Quality : ' + ii1i1Iii + ' - ' + IIi , 'http://www.xvideos.com' + url , 10108 , II1III1I1I1Ii , II1III1I1I1Ii , ii1i1Iii + ' - ' + IIi )
 oO00oO00O0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for url in oO00oO00O0Oo :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 88 - 88: oO0oo0o - ooOoO0O00 % Ii % IIiIiII11i * ii
def iIiII1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iII1iii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 o0o0oO = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in o0o0oO :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iII1iii ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 47 - 47: I11O0O0oOO00O00o
  if 92 - 92: ii % oOo0O0Ooo / OOooOOo * OOooOOo % Ii / ii
def IiII1 ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii111iI = ( o0OOOo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 oO0o0oooO0oO = ii111iI . lower ( )
 oOO0o0oo0 = 'http://www.xvideos.com/?k=' + oO0o0oooO0oO
 print oOO0o0oo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 , IIi , ii1i1Iii in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + ' - Porn Quality : ' + ii1i1Iii + ' - ' + IIi , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10108 , II1III1I1I1Ii , II1III1I1I1Ii , ii1i1Iii + ' - ' + IIi )
 oO00oO00O0Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in oO00oO00O0Oo :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 9 - 9: oO0o
def II1i1i1I1iII ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 I1Iii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']LOW[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in OooOoooOo :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']HIGH[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in I1Iii :
  if 'http' in url :
   OOOoOO ( '[COLOR' + iiI1IiI + ']HLS[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 48 - 48: O00o0O00 . O00o0O00 + Ii + Ii1I % o0o00Oo0O
def O0000ii1i1II ( url ) :
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 try : II1III1i1iiI . play ( url )
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
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1092 , II1III1I1I1Ii )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def iiIIiIi ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8092 , II1III1I1I1Ii )
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
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 18 - 18: Ii - O0OOOoOoo0 * oO0oo0o + I11i
 OOo0 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 IiiiIi1iiii11 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 iIIi1IIIii11i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ii11I1I11II = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIiiiI = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0OOOo
 oO0Oooo0OoO = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 Iii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i1IIIIiiI11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I1iii1I = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 100 - 100: ii . I1ii11iIi11i / Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 29 - 29: O0OOOoOoo0 * IIiIiII11i * oO0o * ooOOOoO
 if 92 - 92: oO0oo0o
 ii1ii1ii = ooOooo000oOO ( OOo0 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( IiiiIi1iiii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1i1IIiII1I = ooOooo000oOO ( iIIi1IIIii11i )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 OOOii = ooOooo000oOO ( IIiiiI )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 Iii1I11 = ooOooo000oOO ( oO0Oooo0OoO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0o0o = ooOooo000oOO ( Iii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 IiiiIi1111I = ooOooo000oOO ( i1IIIIiiI11 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iII1i1ii = ooOooo000oOO ( I1iii1I )
 if 30 - 30: Ii1I
 if 88 - 88: ooOoO0O00 % O0OOOoOoo0 . Ii . ooOoO0O00
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
  for ooOOoOoO0oO00O , oO00oooOOoOo0 in IIi1I11I1II :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1I1ii11i1Iii + ooOOoOoO0oO00O ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 79 - 79: ii / oOo0O0Ooo
    if 87 - 87: ooOOOoO . ooOoO0O00 % ii * Ii
    if 67 - 67: ii1ii11IIIiiI / oO0o . ii
    if 51 - 51: IIiIiII11i . oO0oo0o . oO0o % IIiIiII11i
    if 41 - 41: OOooOOo - O00o0O00 + O0OOOoOoo0 - ooOoO0O00
    if 6 - 6: IIiIiII11i
    if 7 - 7: ooOoO0O00
 if ii1ii1ii != 'Failed' :
  I1Iii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for ooOOoOoO0oO00O , oO00oooOOoOo0 in I1Iii :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( OOo0 + ooOOoOoO0oO00O ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Oo00oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in Oo00oo :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 79 - 79: Ii1I / o0o00Oo0O % I11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if i1i1IIiII1I != 'Failed' :
  o0ooo = [ ]
  IiIii11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i1IIiII1I )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in IiIii11I :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    if oO00oooOOoOo0 in o0ooo :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i1I1ii11i1Iii , 1016 , iiiI1I1iIIIi1 , i11i , I1I )
     o0ooo . append ( oO00oooOOoOo0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if OOOii != 'Failed' :
  Ooo0O00 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOOii )
  for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in Ooo0O00 :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1I1ii11i1Iii , 7067 , II1III1I1I1Ii )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 53 - 53: o0o00Oo0O . oOo0O0Ooo
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if Iii1I11 != 'Failed' :
  o0oOOoO000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Iii1I11 )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in o0oOOoO000 :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Redemption[/COLOR]' ) , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 86 - 86: iI11I1II1I1I - I11O0O0oOO00O00o % O0OOOoOoo0 . O00o0O00 * OOooOOo . ooOoO0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if O0o0o != 'Failed' :
  O0o0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0o0o )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in O0o0O0 :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 88 - 88: oO0o * I11i * O00o0O00 / I1ii11iIi11i * oO0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if IiiiIi1111I != 'Failed' :
  oOII11i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiiIi1111I )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in oOII11i1I :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Herovision[/COLOR]' ) , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 69 - 69: O0OOOoOoo0 . O00o0O00 - oOo0O0Ooo
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 29 - 29: Ii . Ii1I / oOo0O0Ooo . O00o0O00 + Ii
 if iII1i1ii != 'Failed' :
  i1I1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iII1i1ii )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , oO00oooOOoOo0 in i1I1i :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 9 - 9: ii * Ii1I
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 O000OOO00Ooo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 9 - 9: I1ii11iIi11i + Ii1IIIi1
 for O0000oO0o00 in O000OOO00Ooo :
  oo000o = I11i1I1I + O0000oO0o00 + IIIII
  oooooO0oO0ooO = ooOooo000oOO ( oo000o )
  if oooooO0oO0ooO != 'Failed' :
   iIII1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooO0oO0ooO )
   for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in iIII1IiI :
    if o0OOOo in oO00oooOOoOo0 . lower ( ) :
     iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , 222 , iiiI1I1iIIIi1 , i11i , I1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 32 - 32: OOooOOo % oO0o + Ii + O0OOOoOoo0 - iI1ii11iIi1i + oO0oo0o
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 31 - 31: iI11I1II1I1I - I11i
 O000OOO00Ooo = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 57 - 57: I1ii11iIi11i % oO0o
 if 1 - 1: OOooOOo * o0o00Oo0O . oO0oo0o % o0o00Oo0O + IIiIiII11i
 for O0000oO0o00 in O000OOO00Ooo :
  oo000o = o00oo + O0000oO0o00
  i1Oo = ooOooo000oOO ( oo000o )
  if i1Oo != 'Failed' :
   Ii11ii1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( i1Oo )
   for ooOOoOoO0oO00O , oO00oooOOoOo0 in Ii11ii1 :
    if o0OOOo in oO00oooOOoOo0 . lower ( ) :
     OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o00oo + O0000oO0o00 + ooOOoOoO0oO00O ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 1 - 1: iI11I1II1I1I % oO0oo0o . iI11I1II1I1I
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 10 - 10: Ii1IIIi1 + oO0o
     if 6 - 6: oO0o
def OO000OOOo0Oo ( ) :
 if 75 - 75: IIiIiII11i + O0OOOoOoo0 % O00o0O00 + I1ii11iIi11i
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 if 70 - 70: oO0o
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( o0OOOo ) . replace ( ' ' , '%20' )
 o0OO0o0o00o = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 OOo0 = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 IiiiIi1iiii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIIi1IIIii11i = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oO0o0oooO0oO ) . replace ( ' ' , '+' )
 Ii11I1I11II = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IIiiiI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oO0Oooo0OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 43 - 43: OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 57 - 57: oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0 = ooOooo000oOO ( o0OO0o0o00o )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ii1ii1ii = ooOooo000oOO ( OOo0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( IiiiIi1iiii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1i1IIiII1I = cloudflare . source ( iIIi1IIIii11i )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 i1Oo = ooOooo000oOO ( Ii11I1I11II )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OOOii = ooOooo000oOO ( IIiiiI )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 Iii1I11 = ooOooo000oOO ( oO0Oooo0OoO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 65 - 65: Ii - O0OOOoOoo0 * I11O0O0oOO00O00o + O0OOOoOoo0 / ooOOOoO + I11i
 if Iii1I11 != 'Failed' :
  o0oOOoO000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Iii1I11 )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in o0oOOoO000 :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source HeroVision[/COLOR]' ) , i1I1ii11i1Iii , 1016 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % iI1ii11iIi1i % IIiIiII11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 77 - 77: ii1ii11IIIiiI + oO0oo0o
 if OOOii != 'Failed' :
  Ooo0O00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOii )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in Ooo0O00 :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 1016 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 38 - 38: Ii1I - iI1ii11iIi1i * I11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 13 - 13: oOo0O0Ooo * oO0oo0o
    if 41 - 41: ooOOOoO
    if 16 - 16: iI11I1II1I1I
    if 94 - 94: O0OOOoOoo0 % I11O0O0oOO00O00o % ooOoO0O00
    if 90 - 90: iI1ii11iIi1i * oO0o
    if 7 - 7: Ii1IIIi1 . iI1ii11iIi1i . Ii1IIIi1 - ii1ii11IIIiiI
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 33 - 33: O0OOOoOoo0 + ii - oO0o / ooOoO0O00 / ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for II1III1I1I1Ii , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , II1III1I1I1Ii , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 82 - 82: Ii1I / O00o0O00 - Ii1IIIi1 / I1ii11iIi11i * oO0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: ii
    if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
    if 38 - 38: o0o00Oo0O
    if 79 - 79: ooOoO0O00 . oO0oo0o
    if 34 - 34: ii1ii11IIIiiI * IIiIiII11i
    if 71 - 71: ooOOOoO
    if 97 - 97: Ii1I
    if 86 - 86: I1ii11iIi11i - O00o0O00 . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
    if 34 - 34: I11i . ii1ii11IIIiiI % ooOOOoO - o0o00Oo0O / ii1ii11IIIiiI
    if 91 - 91: Ii % ii1ii11IIIiiI * oO0oo0o - Ii1I . ii1ii11IIIiiI
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in OooOoooOo :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , i1I1ii11i1Iii , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 28 - 28: Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  I1Iii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in I1Iii :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOo0 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 51 - 51: oOo0O0Ooo + O0OOOoOoo0 * o0o00Oo0O . iI1ii11iIi1i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Oo00oo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for oO00oooOOoOo0 in Oo00oo :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiiIi1iiii11 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 82 - 82: O00o0O00 * Ii1I % iI1ii11iIi1i . O00o0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if i1i1IIiII1I != 'Failed' :
  IiIii11I = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( i1i1IIiII1I )
  for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IiIii11I :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source - Dizi[/COLOR]' , i1I1ii11i1Iii , 8062 , II1III1I1I1Ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 43 - 43: oO0o . O0OOOoOoo0 * I1ii11iIi11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if i1Oo != 'Failed' :
  Ii11ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo )
  for i1I1ii11i1Iii , iiiI1I1iIIIi1 , I1I , i11i , oO00oooOOoOo0 in Ii11ii1 :
   if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- Source Scooby[/COLOR]' ) , i1I1ii11i1Iii , 1016 , iiiI1I1iIIIi1 , i11i , I1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 20 - 20: ooOoO0O00 . ooOoO0O00 - I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 89 - 89: O0OOOoOoo0 - I11O0O0oOO00O00o . o0o00Oo0O % ii . Ii
 IiIIiII1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if i1Oo != 'Failed' :
  for O0000oO0o00 in IiIIiII1I :
   oo000o = I11i1I1I + O0000oO0o00 + IIIII
   IiiiIi1111I = O0i1II1Iiii1I11 ( oo000o )
   if IiiiIi1111I != 'Failed' :
    oOII11i1I = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IiiiIi1111I )
    for oO00oooOOoOo0 , I1I , i1I1ii11i1Iii , II1III1I1I1Ii , oOo0O , OooO0OOo in oOII11i1I :
     if oO0o0oooO0oO in oO00oooOOoOo0 . lower ( ) :
      I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , OooO0OOo , II1III1I1I1Ii , oOo0O , I1I )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 92 - 92: ii1ii11IIIiiI % iI1ii11iIi1i
      I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
      if 30 - 30: IIiIiII11i - I11i % ii1ii11IIIiiI . I11O0O0oOO00O00o
      if 63 - 63: iI11I1II1I1I / O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1iOOoOooO0o ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o0OOOo ) . replace ( ' ' , '+' )
 if 28 - 28: ooOOOoO + Ii + ii / oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 6 - 6: oOo0O0Ooo - Ii
 if IIIi1I1IIii1II != 'Failed' :
  OooOoooOo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    OOOoOO ( ( oO00oooOOoOo0 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + i1I1ii11i1Iii ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 61 - 61: ii1ii11IIIiiI * Ii1I % oOo0O0Ooo % oO0o % I11O0O0oOO00O00o + I11O0O0oOO00O00o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
i1111I = '{ZH},' ; OoO00oo0 = '{IX},' ; oOOOo00OoOooo = '{LM},'
if 47 - 47: O0OOOoOoo0 + Ii1IIIi1 + ooOoO0O00
def IIiii ( url ) :
 ooOoOooo00Oo = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( ooOoOooo00Oo )
 for url , iI1i , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( iI1i ) . replace ( 'Sezon' , ' Season ' ) + ( ooo0O ) . replace ( 'Bölüm' , ' Episode ' ) + oO00oooOOoOo0 , url , 8063 , '' )
  if 72 - 72: I11O0O0oOO00O00o
  if 26 - 26: ooOOOoO % I1ii11iIi11i
  if 72 - 72: o0o00Oo0O + I11i + oOo0O0Ooo / I1ii11iIi11i
  if 83 - 83: ooOOOoO - oOo0O0Ooo . iI1ii11iIi1i
def iI1Iii11i ( url ) :
 ooOoOooo00Oo = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( ooOoOooo00Oo )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , '' )
  if 61 - 61: iI1ii11iIi1i - Ii1I - ooOoO0O00 + Ii % I11O0O0oOO00O00o
  if 39 - 39: o0o00Oo0O . ooOoO0O00 * Ii1I - oO0o - Ii1IIIi1 % I11i
  if 6 - 6: oO0o - Ii1IIIi1 / IIiIiII11i
  if 25 - 25: I1ii11iIi11i % OOooOOo
def o00O ( ) :
 if 36 - 36: O00o0O00 * oO0o - Ii1I + Ii1IIIi1
 ooOoOooo00Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooOoOooo00Oo )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 , ooo0O in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 + '  -  ' + ( ooo0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 8063 , II1III1I1I1Ii )
  if 13 - 13: oO0o % iI11I1II1I1I - IIiIiII11i / oOo0O0Ooo
def iII111iiiI11i ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 8002 , II1III1I1I1Ii )
def i1i111III1 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii , time , url , oO00oooOOoOo0 , I11iII in IIi1I11I1II :
  I1IIII1i ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , time ) , url , 1015 , II1III1I1I1Ii , I11iII )
  if 12 - 12: Ii1I * O0OOOoOoo0 - I11O0O0oOO00O00o . oO0o + oO0o + Ii1IIIi1
def ii1O0O ( ) :
 if 37 - 37: oO0o + Ii1I - o0o00Oo0O * IIiIiII11i
 oOo0 ( 'Coronation Street' , '' , 8001 , '' )
 oOo0 ( 'Eastenders' , '' , 8002 , '' )
 oOo0 ( 'Emmerdale' , '' , 8003 , '' )
 oOo0 ( 'Hollyoaks' , '' , 8004 , '' )
 oOo0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 if 15 - 15: O0OOOoOoo0 % I11i / oO0oo0o - IIiIiII11i . iI11I1II1I1I
 if 28 - 28: IIiIiII11i * O0OOOoOoo0 * iI1ii11iIi1i
 if 93 - 93: ooOoO0O00 . iI1ii11iIi1i * ii1ii11IIIiiI . O0OOOoOoo0
def O0iI1I1ii11IIi1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Holly' in oO00oooOOoOo0 :
   II1III1I1I1Ii = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , II1III1I1I1Ii )
   else :
    pass
    if 100 - 100: I1ii11iIi11i . iI1ii11iIi1i . oOo0O0Ooo % IIiIiII11i - oO0oo0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 52 - 52: oOo0O0Ooo % oO0o * iI1ii11iIi1i * Ii1IIIi1 / O00o0O00
def oooO00oo0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'East' in oO00oooOOoOo0 :
   II1III1I1I1Ii = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , II1III1I1I1Ii )
   else :
    pass
    if 74 - 74: ooOOOoO / O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86: o0o00Oo0O . ooOoO0O00 - oO0o / I1ii11iIi11i / Ii1I
def oooooO0OO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Emmer' in oO00oooOOoOo0 :
   II1III1I1I1Ii = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , II1III1I1I1Ii )
   else :
    pass
    if 49 - 49: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: O0OOOoOoo0 / O00o0O00 / OOooOOo . iI11I1II1I1I / O00o0O00
def O0OOooO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Coro' in oO00oooOOoOo0 :
   II1III1I1I1Ii = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , II1III1I1I1Ii )
   else :
    pass
    if 89 - 89: iI1ii11iIi1i . oOo0O0Ooo / oO0o + ii1ii11IIIiiI + IIiIiII11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: oOo0O0Ooo % Ii1I + ii
def IIiIi11i111II ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Celeb' in oO00oooOOoOo0 :
   II1III1I1I1Ii = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1I1ii11i1Iii :
    OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , II1III1I1I1Ii )
   else :
    pass
    if 52 - 52: ii / ooOOOoO - ooOoO0O00
def Oo00o ( name , url ) :
 IIIi1ii = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IIIi1ii :
  Ii1iii11I = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oo000o0000oO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( oo000o0000oO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oo000o0000oO = open_url ( url )
  Ii11iIiiI = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( oo000o0000oO ) [ - 1 ]
  Ii1iii11I = Ii11iIiiI . replace ( '\\/' , '/' )
 OOoOOOO00 = xbmcgui . ListItem ( name , '' , '' )
 OOoOOOO00 . setPath ( Ii1iii11I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoOOOO00 )
 if 3 - 3: IIiIiII11i / O00o0O00
 if 48 - 48: O0OOOoOoo0 . Ii1I
def IiiIIIIi ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
  oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 23 - 23: ooOoO0O00 + Ii1I + oOo0O0Ooo - O0OOOoOoo0 % ii . ooOOOoO
def iII ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Movies' in oO00oooOOoOo0 :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( i1I1ii11i1Iii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def O0ooiIIi1 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , II1III1I1I1Ii )
 for url in OooOoooOo :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 76 - 76: oOo0O0Ooo - oOo0O0Ooo - I11i % O0OOOoOoo0 * o0o00Oo0O
  if 11 - 11: iI1ii11iIi1i + I11O0O0oOO00O00o . oO0o . Ii * oO0o
def I1IIiIi ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url , II1III1I1I1Ii in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , II1III1I1I1Ii )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
OOOOoOoO = '{UJ},' ; OO000 = '{WE},' ; o0oOoo0o = '{WP},' ; IiiIiIIi = '{PP},'
def O00Oo ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url , II1III1I1I1Ii in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , II1III1I1I1Ii )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOoo ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  oo0O0Ii111Ii11 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0O0Ii111Ii11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - O00o0O00
 if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
 if 54 - 54: O0OOOoOoo0 * Ii1IIIi1 * Ii1IIIi1 % OOooOOo - O00o0O00 % Ii1I
def iIIiI11Ii1iI ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def ooOo0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  I1I1I1IIi1III ( ( url ) . replace ( ' ' , '%20' ) )
oOo0o = '{XX},' ; O000OOO000o = '{UD},' ; I11iiIiiI1iIi11 = '{YT},' ; II1I1I11i1I1 = '{JS},' ; iiIi1 = '{PF},'
if 84 - 84: IIiIiII11i
def i1IIii1i ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  OOOoOO ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( i1I1ii11i1Iii ) ) , 222 , II1III1I1I1Ii )
  if 60 - 60: iI1ii11iIi1i % I1ii11iIi11i / I11O0O0oOO00O00o . Ii1IIIi1 / ii1ii11IIIiiI - ii
def o0iii1i ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii , url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'youtu' in url :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + II1III1I1I1Ii )
 for url in next :
  oOo0 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - Ii1IIIi1 - Ii
def oo0O00o0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 51 - 51: o0o00Oo0O % IIiIiII11i % Ii + O00o0O00 . ii
def IIIi1I ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11
 IIi1I11I1II = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , II1III1I1I1Ii )
  if 87 - 87: oO0o
  if 34 - 34: ii1ii11IIIiiI . OOooOOo / Ii / Ii1IIIi1
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + O00o0O00
  if 31 - 31: iI1ii11iIi1i * I11i * iI1ii11iIi1i + oO0o * I11i . ii1ii11IIIiiI
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
 iIIIi1i1Ii = False
 Oo0o00o = '0'
 if Cat_Name == 'All Channels' : iIIIi1i1Ii = True
 if Cat_Name == 'Entertainment' : Oo0o00o = '1'
 if Cat_Name == 'Movies' : Oo0o00o = '2'
 if Cat_Name == 'Music' : Oo0o00o = '3'
 if Cat_Name == 'News' : Oo0o00o = '4'
 if Cat_Name == 'Sports' : Oo0o00o = '5'
 if Cat_Name == 'Documentary' : Oo0o00o = '6'
 if Cat_Name == 'Kids' : Oo0o00o = '7'
 if Cat_Name == 'Food' : Oo0o00o = '8'
 if Cat_Name == 'Religious' : Oo0o00o = '9'
 if Cat_Name == 'USA Channels' : Oo0o00o = '10'
 if Cat_Name == 'Other' : Oo0o00o = '11'
 if 32 - 32: OOooOOo + O0OOOoOoo0 + iI1ii11iIi1i + oOo0O0Ooo
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oo000o0000oO )
 print 'Len Match: >>>' + str ( len ( IIi1I11I1II ) )
 for oO00oooOOoOo0 , II1III1I1I1Ii , I1IIIIII1 in IIi1I11I1II :
  O0oO0O = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( II1III1I1I1Ii ) . replace ( '\\' , '' )
  if I1IIIIII1 == Oo0o00o :
   oOo0 ( oO00oooOOoOo0 , '' , 7022 , O0oO0O )
  elif iIIIi1i1Ii == True :
   oOo0 ( oO00oooOOoOo0 , '' , 7022 , O0oO0O )
  else : pass
  if 20 - 20: OOooOOo % IIiIiII11i . OOooOOo . ooOOOoO + O00o0O00
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: Ii1IIIi1 / ii - I1ii11iIi11i
def iIIi1iii1 ( Search_Name ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oo000o0000oO )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii , i1I1ii11i1Iii , o0OO0o0o00o , OOo0 in IIi1I11I1II :
  O0oO0O = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( II1III1I1I1Ii ) . replace ( '\\' , '' )
  OOOoOO ( Search_Name + ': Link 1' , ( i1I1ii11i1Iii ) . replace ( '\\' , '' ) , 222 , O0oO0O )
  OOOoOO ( Search_Name + ': Link 2' , ( o0OO0o0o00o ) . replace ( '\\' , '' ) , 222 , O0oO0O )
  OOOoOO ( Search_Name + ': Link 3' , ( OOo0 ) . replace ( '\\' , '' ) , 222 , O0oO0O )
  if 64 - 64: O0OOOoOoo0 / ooOoO0O00 % Ii1IIIi1
def OOoOo0O0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def I1o0 ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def I1IiiiiI1i1I ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  OOOoOO ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 48 - 48: I11O0O0oOO00O00o + IIiIiII11i % oO0oo0o % O00o0O00 * IIiIiII11i
def iiiI1i ( url ) :
 url
 OO0OOO00 = xbmcgui . ListItem ( oO00oooOOoOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO0OOO00 )
 return
 if 23 - 23: oOo0O0Ooo
 if 7 - 7: Ii1IIIi1 % Ii1I
def o0oOOO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oo000o0000oO )
 for url , I1I , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + II1III1I1I1Ii , '' , ( I1I ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 for url in OooOoooOo :
  oOo0 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 47 - 47: O00o0O00 / IIiIiII11i % ooOOOoO . oO0oo0o * Ii1I
def iIii1iIiII1i1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , I1I , II1III1I1I1Ii in IIi1I11I1II :
  iIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + II1III1I1I1Ii , '' , I1I )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 ooOoo000oO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for o0oO in ooOoo000oO :
  o0OoIII1IIiIi1 = ( o0oO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + II1III1I1I1Ii , '' , o0OoIII1IIiIi1 )
  if 97 - 97: I11i / ooOOOoO + OOooOOo + oO0o % ii1ii11IIIiiI
def iIIi1II1 ( INFO ) :
 O0O0Oooo0o ( 'info for workout' , INFO )
 if 42 - 42: iI11I1II1I1I - O0OOOoOoo0 - I11O0O0oOO00O00o - ii1ii11IIIiiI
 if 33 - 33: OOooOOo - o0o00Oo0O
 if 38 - 38: O00o0O00 * ooOOOoO - ii * ooOOOoO + ii
def Oo0oO ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'Name=(.+?)\n.+?m3u=(.+?)\n' , re . DOTALL ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  oOo0 ( ( oO00oooOOoOo0 ) . replace ( 'SlyNet' , '' ) , url , 9032 , III1iII1I1ii + 'Sport.png' )
def I11IiIi1iI1ii ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 9032 , III1iII1I1ii + 'icon.png' )
def O0oOo0o0OOoO0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:-.+?,(.+?)\n(.+?)\n' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def i1I1IIIiii1 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'icon.png' )
   if 76 - 76: ii
   if 42 - 42: iI1ii11iIi1i * o0o00Oo0O / oO0oo0o
   if 8 - 8: ooOoO0O00 + IIiIiII11i / iI1ii11iIi1i + Ii1I % iI1ii11iIi1i - iI11I1II1I1I
   if 29 - 29: I1ii11iIi11i + IIiIiII11i
   if 95 - 95: oO0oo0o
def i11ii ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3NvdXJjZXR2LmluZm8v' ) )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 9008 , III1iII1I1ii + 'disclose.png' )
def IiI111I ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="article-image darken"><a href="([^"]*)"><img width="320" height="205" src="([^"]*)".+?title="([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 9009 , II1III1I1I1Ii )
def oo0oO0 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 49 - 49: ii - ooOOOoO
def Iiii11 ( ) :
 oo000o0000oO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '.m3u' in i1I1ii11i1Iii :
   oOo0 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + i1I1ii11i1Iii ) , 9011 , III1iII1I1ii + 'disclose.png' )
def o00000O ( url ) :
 oo000o0000oO = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 23 - 23: I1ii11iIi11i - o0o00Oo0O
def iI111iIi ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'category' in i1I1ii11i1Iii :
   oOo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + i1I1ii11i1Iii , 7010 , III1iII1I1ii + 'disclose.png' )
   if 26 - 26: O00o0O00 % O00o0O00 / Ii + Ii1I - o0o00Oo0O
   if 20 - 20: ii1ii11IIIiiI . o0o00Oo0O - Ii1I / OOooOOo - I11i
def oooooOoOO ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oo000o0000oO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , II1III1I1I1Ii in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + url , 7011 , II1III1I1I1Ii )
 for url in next :
  oOo0 ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 59 - 59: ooOOOoO . ii % oO0oo0o % Ii + oO0oo0o % OOooOOo
  if 18 - 18: O0OOOoOoo0 - ooOOOoO / IIiIiII11i / Ii1I
def i1Ii1IiiIi1II ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oo000o0000oO )
 I1Iii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  if 'http' in url :
   OOOoOO ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  OOOoOO ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in I1Iii :
  OOOoOO ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 54 - 54: iI1ii11iIi1i % ooOoO0O00
  if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
def Oo0Oo00O00o0 ( url ) :
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
  for I1IiiiiIooo0o00o in IiI1 :
   I1IiiiiIooo0o00o = I1IiiiiIooo0o00o . replace ( 'player' , 'watch' )
   O0oOOo0 = I1IiiiiIooo0o00o + '&fv=&sou='
   oooOOOoO0O = O0i1II1Iiii1I11 ( O0oOOo0 )
   iIOOO0O00 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( oooOOOoO0O )
   for O0oO0oo0O in iIOOO0O00 :
    Oo0O000OoO00 = False
    Resolve ( O0oO0oo0O )
    if 66 - 66: oO0oo0o
 elif iI1I1 > 1 :
  if 34 - 34: Ii1IIIi1 % Ii + Ii - Ii1IIIi1
  for I1IiiiiIooo0o00o in IiI1 :
   iii1iII = O0i1II1Iiii1I11 ( I1IiiiiIooo0o00o )
   O00o0o = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iii1iII )
   i11I1iiii = O00o0o
   i11I1iiii = ( str ( i11I1iiii ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i11I1iiii
   OOOoOO ( 'DOUBLE LINK' , i11I1iiii , 424 , '' )
   if 31 - 31: ii1ii11IIIiiI / I1ii11iIi11i / iI11I1II1I1I
   for url in O00o0o :
    oOo0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     o0OO0o0o00o = Google . resolve ( url )
    except :
     pass
    try :
     oOO00OOOoO0o = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( o0OO0o0o00o ) )
     for Ii1iII1ii1 , ooOo0I11I1i in oOO00OOOoO0o :
      if 100 - 100: oO0oo0o
      HD_URLS . append ( Ii1iII1ii1 )
      SD_URLS . append ( ooOo0I11I1i )
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
 for II1III1I1I1Ii , url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , II1III1I1I1Ii )
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
  O0iIiIIIIIii ( url )
  if 63 - 63: I11O0O0oOO00O00o * O0OOOoOoo0 % IIiIiII11i % ii1ii11IIIiiI + oOo0O0Ooo * I1ii11iIi11i
  if 96 - 96: ooOOOoO
def oo00OOo0 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , III1iII1I1ii + 'LocalM3U.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , III1iII1I1ii + 'RemoteM3U.png' , OO0o , '' )
 if 61 - 61: oO0oo0o % O0OOOoOoo0 - Ii1I + oO0oo0o . OOooOOo
def IIIi ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  I1iO00O000oOO0oO = open ( O0OoO000O0OO , 'r' )
  for OO0OOO00 in I1iO00O000oOO0oO :
   OO0i1Ii1II11 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OO0OOO00 )
   for oO00oooOOoOo0 , i1I1ii11i1Iii in OO0i1Ii1II11 :
    OOOoOO ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , III1iII1I1ii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 25 - 25: ii % oO0oo0o / iI11I1II1I1I + o0o00Oo0O
def OOO0oOoO00OoO ( url ) :
 if os . path . exists ( Remote ) :
  IIIi1I1IIii1II = iI1i111I1Ii ( url )
  IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , url in IIi1I11I1II :
   url = ( url ) . strip ( )
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 23 - 23: oOo0O0Ooo - I11i % oO0oo0o . o0o00Oo0O * ii + O0OOOoOoo0
  if 53 - 53: I1ii11iIi11i
def IiI111111IIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'plugin.video.GenieTv'
 if 3 - 3: ooOOOoO - ii * ii - oOo0O0Ooo / ii1ii11IIIiiI * Ii1I
 O0oo0ooO00 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 81 - 81: oOo0O0Ooo / ii
def ooOOO00Ooo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'repository.GenieTv'
 if 52 - 52: oO0oo0o + ii1ii11IIIiiI * ii1ii11IIIiiI * I1ii11iIi11i - iI11I1II1I1I + Ii1I
 O0oo0ooO00 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 34 - 34: Ii1IIIi1 / oO0o / I1ii11iIi11i
 if 92 - 92: ii1ii11IIIiiI % Ii1IIIi1 % I11i . oOo0O0Ooo - Ii1I - I11i
def IiIi ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '' , 10051 , III1iII1I1ii + 'Catagories.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10052 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
 if 61 - 61: iI1ii11iIi1i * iI1ii11iIi1i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
O0III1Iiii1i11 = 'https://addons.tvaddons.ag/'
if 74 - 74: I1ii11iIi11i / ii1ii11IIIiiI % ii1ii11IIIiiI . ooOOOoO
def ooOo ( ) :
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 oOO0o0oo0 = 'https://addons.tvaddons.ag/search/?keyword=' + oO0o0oooO0oO
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , 10054 , 'https://addons.tvaddons.ag/' + i1iIi , OO0o , '' )
  if 93 - 93: ii1ii11IIIiiI % Ii
  if 25 - 25: O0OOOoOoo0 % Ii1IIIi1 * Ii1IIIi1 + iI11I1II1I1I . ooOoO0O00
def OO0Oo00 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( O0III1Iiii1i11 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Repositories' in oO00oooOOoOo0 :
   pass
  elif 'Services' in oO00oooOOoOo0 :
   pass
  elif 'International' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10053 , 'https://addons.tvaddons.ag/' + II1III1I1I1Ii , OO0o , '' )
   if 28 - 28: oO0o + ii1ii11IIIiiI / OOooOOo % oO0oo0o - I1ii11iIi11i
   if 70 - 70: ooOoO0O00 - iI11I1II1I1I - ii1ii11IIIiiI
def Addon ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 i1i11 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Please' in oO00oooOOoOo0 :
   pass
  else :
   iIiIIi1 ( oO00oooOOoOo0 , url , 10054 , 'https://addons.tvaddons.ag/' + II1III1I1I1Ii , OO0o , '' )
 for url in i1i11 :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , OO0o , '' )
  if 40 - 40: Ii1I / iI11I1II1I1I . ooOOOoO % O0OOOoOoo0
  if 56 - 56: O0OOOoOoo0 . iI11I1II1I1I + ooOoO0O00
def o0oOOoOo00o ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   I1 = os . path . join ( I1i , name + '.zip' )
   try :
    os . remove ( I1 )
   except :
    pass
   downloader . download ( url , I1 , o0oOoO00o )
   OOO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OOO0
   print '======================================='
   extract . all ( I1 , OOO0 , o0oOoO00o )
   Oo0o0O00 ( )
   if 22 - 22: ii1ii11IIIiiI - oOo0O0Ooo
def O0oo0ooO00 ( url , name ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I1 = os . path . join ( I1i , name + '.zip' )
 try :
  os . remove ( I1 )
 except :
  pass
 downloader . download ( url , I1 , o0oOoO00o )
 OOO0 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OOO0
 print '======================================='
 extract . all ( I1 , OOO0 , o0oOoO00o )
 Oo0o0O00 ( )
 if 96 - 96: ooOoO0O00 + I1ii11iIi11i - IIiIiII11i . ii . O00o0O00 / oO0o
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
 for url , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 1007 , i1iIi )
def OoOo00OoOO00 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , i1iIi )
  if 62 - 62: OOooOOo * ii * I11i
  if 37 - 37: oO0oo0o
def I1Ii1iI1IiI1I ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , iconimage , I1I , oOo0O , name in IIi1I11I1II :
  if 'http' in url :
   if '.php' in url :
    oo0OoOO0o0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
    for OO0OOO00 in oo0OoOO0o0o :
     if OO0OOO00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    II111i1ii1iII ( name , url , 1016 , iconimage , oOo0O , I1I )
   else :
    if 'youtube' in url :
     oo0OoOO0o0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for OO0OOO00 in oo0OoOO0o0o :
      if OO0OOO00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OO00o0oOO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oOo0O , I1I )
    else :
     oo0OoOO0o0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for OO0OOO00 in oo0OoOO0o0o :
      if OO0OOO00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OO00o0oOO ( name , url , 222 , iconimage , oOo0O , I1I )
     I1I1II1I11 ( 'movies' , 'INFO' )
  else :
   o0OOOoO ( url , iconimage , name )
   if 73 - 73: ii / ii
 else :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
  for url , i1iIi , name in IIi1I11I1II :
   if 'http' in url :
    if '.php' in url :
     oOo0 ( name , url , 1016 , i1iIi )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OOOoOO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i1iIi )
     else :
      oo0OoOO0o0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
      for OO0OOO00 in oo0OoOO0o0o :
       if OO0OOO00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOOoOO ( name , url , 222 , i1iIi )
      I1I1II1I11 ( 'movies' , 'INFO' )
   else :
    o0OOOoO ( url , i1iIi , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 88 - 88: ii1ii11IIIiiI - iI1ii11iIi1i - oO0oo0o + ooOoO0O00
def o0OOOoO ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ii11IiiIi = ( url ) . replace ( OoO00oo0 , 'http' ) . replace ( O000OOO000o , '.com' ) ;
 II1IoOoO0oOO0o = ( ii11IiiIi ) . replace ( oOOOo00OoOooo , 'a' ) . replace ( iIIi11i , 'b' ) . replace ( III , 'c' ) . replace ( OO000 , 'd' ) . replace ( II11i1ii , 'e' ) . replace ( Oo0O0o , 'f' ) ;
 oO0000oo0o0o0 = ( II1IoOoO0oOO0o ) . replace ( oOo0o , 'g' ) . replace ( o0o000Oo0ooOo , 'h' ) . replace ( I11iiIiiI1iIi11 , 'i' ) . replace ( iiIi1 , 'j' ) . replace ( iiIi111Ii1II , 'k' ) . replace ( oOoo0oO , 'l' ) ;
 i1I1 = ( oO0000oo0o0o0 ) . replace ( O0ooO0o , 'm' ) . replace ( IiII1111I , 'n' ) . replace ( iiIIii111Ii , 'o' ) . replace ( OO000oooOo000 , 'p' ) . replace ( o0oO0o0Oo0 , 'q' ) . replace ( i1I1iiiI , 'r' ) ;
 i1IiIi1I1i = ( i1I1 ) . replace ( Ii11I1 , 's' ) . replace ( o0oOoo0o , 't' ) . replace ( OO00OO , 'u' ) . replace ( IiIiIi11iiIi1 , 'v' ) . replace ( OoOoO0O00oo , 'w' ) . replace ( ooo0o0oooo , 'x' ) ;
 o0OoIiiiiiiI111i = ( i1IiIi1I1i ) . replace ( iiIIIIiI11II1 , 'y' ) . replace ( IiI1i11i1iI , 'z' ) . replace ( II1i1III1IIiI , '.' ) . replace ( OoOI1iI1 , '(' ) . replace ( oo0O0Oo0O , ')' ) . replace ( iIIO0O , '/' ) ;
 o0oo0O0OO0 = ( o0OoIiiiiiiI111i ) . replace ( i1111I , '1' ) . replace ( IiiIiIIi , '2' ) . replace ( IIiI , '3' ) . replace ( oo0o00oO00ooo , '4' ) . replace ( IIii1Ii , '5' ) . replace ( II1I1I11i1I1 , '6' ) ;
 i11I1Ii1Iiii1 = ( o0oo0O0OO0 ) . replace ( I111ii1III1I , '7' ) . replace ( OO0o0oo , '8' ) . replace ( o0oo0oOOOo00 , '9' ) . replace ( OO0OOO , '0' ) . replace ( OoO0o0OO , ':' ) . replace ( II11IiI1 , '%' ) ;
 url = ( i11I1Ii1Iiii1 ) . replace ( OOOOoOoO , '-' ) . replace ( OoOo0000o0OOo , '_' ) ;
 OOOoOO ( name , url , 222 , iconimage ) ;
 if 64 - 64: iI1ii11iIi1i . ii - Ii1I
 if 19 - 19: I1ii11iIi11i
def iIIiI1I1i1 ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1007 , i1iIi )
def Iii11I ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , i1iIi )
  if 2 - 2: oO0oo0o . O00o0O00
def ii1O0oOOo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ii111IIiiiiI = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ii111IIiiiiI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii111IIiiiiI )
 if 98 - 98: ooOoO0O00 - Ii1IIIi1
 if 49 - 49: I11i . iI1ii11iIi1i . oO0oo0o
def i11iI11ii ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oo000o0000oO )
 for url , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  if '-dir-' in oO00oooOOoOo0 :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , II1III1I1I1Ii )
  else :
   oOo0 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , II1III1I1I1Ii )
   if 85 - 85: ooOoO0O00
def oOooo0OO0O0 ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0o0o0O0oo = ( 'http://afewbitsmore.com/' )
 IIi1I11I1II = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[To Parent Directory]' in oO00oooOOoOo0 :
   oO00oooOOoOo0 = 'HOME'
   pass
  elif 'HOME' in oO00oooOOoOo0 :
   pass
  elif '.m3u' in oO00oooOOoOo0 :
   oOo0 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , o0o0o0O0oo + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , o0o0o0O0oo + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in oO00oooOOoOo0 :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , o0o0o0O0oo + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , o0o0o0O0oo + url , 1012 , III1iII1I1ii + 'music.png' )
def i1iI1iIII ( url ) :
 IIIi1I1IIii1II = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for II1III1I1I1Ii , oO00oooOOoOo0 , url in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 76 - 76: IIiIiII11i
def Iii1i1I ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0o0o0O0oo = url
 IIi1I11I1II = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp3' in oO00oooOOoOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   oOo0 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/' , '' ) , o0o0o0O0oo + url , 1011 , III1iII1I1ii + 'music.png' )
def iIIIIi1iiI ( ) :
 oo000o0000oO = iI1i111I1Ii ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , II1III1I1I1Ii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , ( 'http://www.cyn.net/music/' + i1I1ii11i1Iii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + II1III1I1I1Ii ) . replace ( ' ' , '%20' ) )
def O0ii ( url , img ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 img = img
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( o0OO0o0o00o + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 53 - 53: iI1ii11iIi1i / oOo0O0Ooo * iI1ii11iIi1i + I11i + oO0oo0o - I1ii11iIi11i
def IIi1iiIIi1i ( url ) :
 oo000o0000oO = iI1i111I1Ii ( url )
 o0OO0o0o00o = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oo000o0000oO )
 for type , url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[VID]' in type :
   OOOoOO ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , o0OO0o0o00o + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   IIi1iiIIi1i ( o0OO0o0o00o + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: ii / ooOOOoO
 if 51 - 51: O00o0O00 % Ii
def o0OoOoOo0O ( ) :
 o00oo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o0OOOo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0oooO0oO = o0OOOo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 o0OO0o0o00o = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 OOo0 = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 37 - 37: ooOoO0O00 . ii1ii11IIIiiI - IIiIiII11i % I11i - ooOoO0O00 . oO0oo0o
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 O0 = ooOooo000oOO ( o0OO0o0o00o )
 ii1ii1ii = ooOooo000oOO ( OOo0 )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in IIi1I11I1II :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1ii11i1Iii + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 3 - 3: I11i - ii + Ii1IIIi1 . I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in OooOoooOo :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OO0o0o00o + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 88 - 88: I11O0O0oOO00O00o - Ii1IIIi1
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  I1Iii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in I1Iii :
   if o0OOOo in oO00oooOOoOo0 . lower ( ) :
    oOo0 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOo0 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 68 - 68: I1ii11iIi11i % oO0oo0o . ooOOOoO - I11i / ooOoO0O00 / ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: I11O0O0oOO00O00o % I1ii11iIi11i + iI1ii11iIi1i
    if 93 - 93: iI1ii11iIi1i - ii1ii11IIIiiI % o0o00Oo0O
    if 11 - 11: Ii
    if 6 - 6: IIiIiII11i
    if 1 - 1: O0OOOoOoo0 % I1ii11iIi11i . oO0oo0o
    if 98 - 98: IIiIiII11i + IIiIiII11i - iI11I1II1I1I . OOooOOo . ii1ii11IIIiiI
O0ooO0o = '{SF},' ; IiII1111I = '{IF},' ; iiIIii111Ii = '{PW},' ; IIiI = '{AM},' ; OO000oooOo000 = '{GF},' ; o0oO0o0Oo0 = '{DD},' ; i1I1iiiI = '{UO},' ; Ii11I1 = '{LE},' ; OO00OO = '{ZY},' ; IiIiIi11iiIi1 = '{UE},' ; OoOoO0O00oo = '{PE},' ; ooo0o0oooo = '{JE},' ; iiIIIIiI11II1 = '{TH},' ; IiI1i11i1iI = '{LK},'
if 99 - 99: oO0oo0o . iI1ii11iIi1i * ii1ii11IIIiiI * iI11I1II1I1I / OOooOOo % ooOOOoO
if 70 - 70: Ii1I . o0o00Oo0O
def oOoOOo ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.iwatchseries.me/tv-list/' )
 IIi1I11I1II = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8021 , III1iII1I1ii + 'iwatch.png' )
def I1111ii11 ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 , OO0oIII111i11IiI in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 + OO0oIII111i11IiI , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def I1iI1I1111i ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  iII11IiIIII ( url )
def iII11IiIIII ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oo000o0000oO )
 OooOoooOo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oo000o0000oO )
 I1Iii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( 'VidSpot - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in OooOoooOo :
  OOOoOO ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for oO00oooOOoOo0 , url in I1Iii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OOOoOO ( 'TheVideo - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 99 - 99: O00o0O00 . O00o0O00 * O0OOOoOoo0 + IIiIiII11i . iI11I1II1I1I
def OO00O00 ( ) :
 oo000o0000oO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi1I11I1II = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1021 , III1iII1I1ii + 'anime.png' )
  if 15 - 15: I11O0O0oOO00O00o - Ii1I * O0OOOoOoo0
  if 80 - 80: Ii1IIIi1 + O0OOOoOoo0 * I11i - IIiIiII11i - Ii1I
def O0Oo0O0O0o ( ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( 'http://www.animetoon.org/cartoon' )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oo000o0000oO )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1002 , III1iII1I1ii + 'anime.png' )
  if 36 - 36: iI11I1II1I1I % OOooOOo - Ii1IIIi1
  if 90 - 90: iI1ii11iIi1i . I11i
  if 11 - 11: o0o00Oo0O
def o0Oo0o ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oo000o0000oO )
 for II1III1I1I1Ii in OooOoooOo :
  OoO00O0 = II1III1I1I1Ii
 I1Iii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oo000o0000oO )
 for url in I1Iii :
  oOo0 ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oo000o0000oO )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0 ( oO00oooOOoOo0 , url , 1003 , OoO00O0 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1ii ( url , IMAGE ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oo000o0000oO )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   oO0oOo ( url )
  elif 'playpanda' in url :
   oO0oOo ( url )
   if 43 - 43: oO0oo0o + OOooOOo . oOo0O0Ooo . Ii
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0oOo ( url ) :
 oo000o0000oO = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( oo000o0000oO )
 for url in IIi1I11I1II :
  OOOoOO ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 71 - 71: I11i + O00o0O00 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
  if 91 - 91: o0o00Oo0O - I11O0O0oOO00O00o % ii1ii11IIIiiI
def I1ii ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0oOOo . add_header ( 'referer' , url )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 78 - 78: oO0o / iI11I1II1I1I . iI1ii11iIi1i * oO0o * OOooOOo - O00o0O00
def iI1i111I1Ii ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 39 - 39: Ii - O00o0O00 - ii1ii11IIIiiI + ii / oOo0O0Ooo / iI11I1II1I1I
def IIi1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iII1Ii1I1i1 = ( '%s%s' % ( OooOooo0 , url ) )
 OOO00O = iI1i111I1Ii ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , i1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  OOOoOO ( '%s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i1iIi )
  if 81 - 81: Ii % oOo0O0Ooo / Ii1IIIi1 % oO0o / ii1ii11IIIiiI % iI11I1II1I1I
def O0iIiIIIIIii ( url ) :
 if 14 - 14: Ii1I * I1ii11iIi11i + Ii % O00o0O00 - oO0oo0o
 iIIii = open ( o0O , "a" )
 iIIii . write ( 'url="' + url + '"\n' )
 iIIii . close
 if 95 - 95: ii1ii11IIIiiI + ooOOOoO * iI11I1II1I1I
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 try : II1III1i1iiI . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( oO00oooOOoOo0 ) )
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : II1III1i1iiI . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / iI1ii11iIi1i
def iiii1ii1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 o0oOoO00o . update ( 100 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 II1III1i1iiI . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 12 - 12: Ii - iI11I1II1I1I * ooOOOoO * Ii1IIIi1
def I1I1I1IIi1III ( url ) :
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II1III1i1iiI . play ( url ) . strip ( )
 except : pass
 if 19 - 19: o0o00Oo0O + oO0oo0o + I11i
def oO0IIi11IiiiI11i ( url ) :
 II1III1i1iiI = xbmc . Player ( iiI1ii1IIiI ( ) )
 import urlresolver
 OO00oO = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 II1III1i1iiI . play ( OO00oO )
 xbmc . sleep ( 1 )
 II1III1i1iiI . play ( url )
 if 80 - 80: iI1ii11iIi1i - Ii1I . iI1ii11iIi1i / Ii + o0o00Oo0O . ooOOOoO
 if 15 - 15: I1ii11iIi11i + Ii1IIIi1 + oOo0O0Ooo * I11i
def iiI1ii1IIiI ( ) :
 try :
  iII1111IIIIiI = getSet ( "core-player" )
  if ( iII1111IIIIiI == 'DVDPLAYER' ) : IiiiiIi11 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iII1111IIIIiI == 'MPLAYER' ) : IiiiiIi11 = xbmc . PLAYER_CORE_MPLAYER
  elif ( iII1111IIIIiI == 'PAPLAYER' ) : IiiiiIi11 = xbmc . PLAYER_CORE_PAPLAYER
  else : IiiiiIi11 = xbmc . PLAYER_CORE_AUTO
 except : IiiiiIi11 = xbmc . PLAYER_CORE_AUTO
 return IiiiiIi11
 return True
 if 57 - 57: Ii1IIIi1 / oO0o - IIiIiII11i
def oOo0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i1i1IIi1I = [ ]
  if showcontext == 'fav' :
   I1i1i1IIi1I . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   I1i1i1IIi1I . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOoOOOO00 . addContextMenuItems ( I1i1i1IIi1I )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = True )
 return i11IiI1iiI11
 if 18 - 18: oO0oo0o * iI1ii11iIi1i / ii % OOooOOo - ooOoO0O00
def OOoOoo00Oo ( name , url , mode , iconimage , fanart , description ) :
 if 49 - 49: I11i - iI11I1II1I1I
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOOOO00 . setProperty ( "Fanart_Image" , fanart )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = True )
 return i11IiI1iiI11
 if 61 - 61: Ii1IIIi1 * O0OOOoOoo0
def OOOoOO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i1i1IIi1I = [ ]
  if showcontext == 'fav' :
   I1i1i1IIi1I . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   I1i1i1IIi1I . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOoOOOO00 . addContextMenuItems ( I1i1i1IIi1I )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = False )
 return i11IiI1iiI11
 if 1 - 1: ii1ii11IIIiiI * OOooOOo
 if 100 - 100: Ii1I / o0o00Oo0O / O0OOOoOoo0 + Ii1I
 if 48 - 48: ii . Ii1IIIi1 + o0o00Oo0O
 if 85 - 85: IIiIiII11i - iI1ii11iIi1i
 if 93 - 93: ooOOOoO / Ii - oO0oo0o + oO0o / ooOoO0O00
 if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
def O0O0Oooo0o ( heading , announce ) :
 class OO0oOOo0o ( ) :
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
   try : o0Oo00 = open ( announce ) ; i1IIi1i1Ii1 = o0Oo00 . read ( )
   except : i1IIi1i1Ii1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i1IIi1i1Ii1 ) )
   return
 OO0oOOo0o ( )
 OO0oOOo0o ( )
 if 46 - 46: ii
def iiII ( ) :
 O0O0Oooo0o ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 39 - 39: o0o00Oo0O . I11O0O0oOO00O00o
 if 45 - 45: oO0oo0o + I11i + ooOOOoO / iI1ii11iIi1i + I11i
 if 33 - 33: Ii1IIIi1 - I1ii11iIi11i - I11O0O0oOO00O00o
 if 61 - 61: iI1ii11iIi1i + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / oO0oo0o
 if 47 - 47: ii1ii11IIIiiI
def Oo0o0O00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 25 - 25: Ii1IIIi1 + oOo0O0Ooo + OOooOOo + ii1ii11IIIiiI % o0o00Oo0O
 if 26 - 26: O0OOOoOoo0 + OOooOOo
 if 17 - 17: Ii1I - Ii1IIIi1 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * O00o0O00
 if 6 - 6: ii1ii11IIIiiI
 if 46 - 46: IIiIiII11i * ii1ii11IIIiiI
 if 23 - 23: ooOoO0O00 - o0o00Oo0O
 if 6 - 6: O0OOOoOoo0 % ii * ii1ii11IIIiiI - ooOOOoO
 if 24 - 24: I11O0O0oOO00O00o / iI11I1II1I1I . ii % OOooOOo . iI1ii11iIi1i
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
def I1O0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oO0oo0oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 5 - 5: ii * Ii1I
def IIio0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIOoO0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 96 - 96: ooOOOoO - Ii1IIIi1
def I11I111i ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0OOOoOoo0
def iIIoooO0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI1iIi1ii1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 59 - 59: IIiIiII11i * ii - ii
def iioOo00O0o ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI11IIi1iiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 83 - 83: I1ii11iIi11i / O0OOOoOoo0
def II1iiIiI1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Ii1I11IIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 41 - 41: O0OOOoOoo0 / oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . Ii1I
def iii11I1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + i1II1iIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 20 - 20: Ii
def oOOOoo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI1i11II1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 61 - 61: I11O0O0oOO00O00o * iI1ii11iIi1i + I11O0O0oOO00O00o - I1ii11iIi11i % OOooOOo . Ii1IIIi1
def oO0OOOOO00O0OO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oOO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 88 - 88: oO0oo0o * oOo0O0Ooo / oO0o - O00o0O00 / ooOoO0O00 . ii1ii11IIIiiI
def ii1III11 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + III11IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , iiiI1I1iIIIi1 , oOo0O , ii1Oo0000oOo in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , ii1Oo0000oOo )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 6 - 6: O00o0O00 / iI11I1II1I1I / O0OOOoOoo0 / oOo0O0Ooo - ooOoO0O00 - O00o0O00
 if 8 - 8: Ii * I11O0O0oOO00O00o . O00o0O00 / O00o0O00
 if 42 - 42: ii / ii1ii11IIIiiI . I11i / o0o00Oo0O - ooOOOoO * ooOOOoO
 if 1 - 1: iI1ii11iIi1i % ii1ii11IIIiiI
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % O00o0O00 . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: ii1ii11IIIiiI % O0OOOoOoo0 - O0OOOoOoo0 % oOo0O0Ooo . O00o0O00 - ii
 if 100 - 100: oOo0O0Ooo + iI1ii11iIi1i + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * ii1ii11IIIiiI - iI1ii11iIi1i + I1ii11iIi11i
def oOi1II111i1IIii ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( O00o0OO ) :
     IIIi1ii1i1 = 0
     IIIi1ii1i1 += len ( OOOooo0OooOoO )
     if IIIi1ii1i1 > 0 :
      for o0Oo00 in OOOooo0OooOoO :
       os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
  iiiIiIIiIiiii = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( iiiIiIIiIiiii )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 99 - 99: ooOOOoO % ii1ii11IIIiiI
 if 61 - 61: o0o00Oo0O + oOo0O0Ooo / ii * Ii1IIIi1 / IIiIiII11i / Ii1IIIi1
 if 56 - 56: Ii1IIIi1 * Ii1I - IIiIiII11i % Ii1I
 if 30 - 30: Ii % oO0o * IIiIiII11i - o0o00Oo0O . Ii1I * iI11I1II1I1I
 if 48 - 48: I11i + Ii1I / Ii1I
 if 80 - 80: ii
 if 65 - 65: oO0oo0o * ooOoO0O00 . ii % O0OOOoOoo0
 if 87 - 87: Ii * IIiIiII11i - iI1ii11iIi1i % ii
def o0Oo0oOooOoOo ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 55 - 55: ooOoO0O00
def ooO0oOOooOo0 ( url ) :
 oOOO0oo0 = os . path . join ( oO , 'addon_data' )
 iI1IiiiiI = [
 ( oOOO0oo0 ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOOO0oo0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOOO0oo0 , 'plugin.video.itv' , 'Images' ) ) ]
 if 12 - 12: Ii . I11O0O0oOO00O00o * O00o0O00 % ooOoO0O00 . O0OOOoOoo0
 O0oooo000o = 0
 if 42 - 42: oO0o % oO0oo0o / I1ii11iIi11i / ooOOOoO
 for OO0OOO00 in iI1IiiiiI :
  if os . path . exists ( OO0OOO00 ) and not OO0OOO00 in [ oOo0oooo00o , oOOO0oo0 ] :
   for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( OO0OOO00 ) :
    IIIi1ii1i1 = 0
    IIIi1ii1i1 += len ( OOOooo0OooOoO )
    if IIIi1ii1i1 > 0 :
     for o0Oo00 in OOOooo0OooOoO :
      if not o0Oo00 in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
       except :
        pass
      else : oo00oOO000oO0 ( 'Ignore Log File: %s' % o0Oo00 )
     for ii1I in IIIIIii1ii11 :
      try :
       shutil . rmtree ( os . path . join ( iIoo0ooooO , ii1I ) )
       O0oooo000o += 1
       oo00oOO000oO0 ( "[Success] cleared %s files from %s" % ( str ( IIIi1ii1i1 ) , os . path . join ( OO0OOO00 , ii1I ) ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( OO0OOO00 , ii1I ) )
  else :
   for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( OO0OOO00 ) :
    for ii1I in IIIIIii1ii11 :
     if 'cache' in ii1I . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIoo0ooooO , ii1I ) )
       O0oooo000o += 1
       oo00oOO000oO0 ( "[Success] wiped %s " % os . path . join ( OO0OOO00 , ii1I ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( OO0OOO00 , ii1I ) )
       if 86 - 86: ii1ii11IIIiiI + IIiIiII11i + ii + iI1ii11iIi1i
 o0Oo0oOooOoOo ( oo0o0O00 , 'Clear Cache: Removed %s Files' % O0oooo000o )
 if 84 - 84: ooOoO0O00 - IIiIiII11i . ii / OOooOOo % iI1ii11iIi1i
 if 7 - 7: ooOoO0O00 / ooOOOoO / Ii1IIIi1
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: O0OOOoOoo0 + oO0oo0o - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: ooOOOoO
 if 52 - 52: o0o00Oo0O + O0OOOoOoo0
 if 11 - 11: ooOoO0O00 / ii1ii11IIIiiI * Ii1I * ii1ii11IIIiiI * O0OOOoOoo0 - Ii
def oOOoooo0o0 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0OOOO0o0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( O0OOOO0o0O ) :
   IIIi1ii1i1 = 0
   IIIi1ii1i1 += len ( OOOooo0OooOoO )
   if 76 - 76: oO0o + O00o0O00 - ooOOOoO . ooOoO0O00
   if 87 - 87: O0OOOoOoo0 + o0o00Oo0O
   if IIIi1ii1i1 > 0 :
    if 69 - 69: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i . oO0o * oO0oo0o * ooOOOoO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( IIIi1ii1i1 ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: ii1ii11IIIiiI
     for o0Oo00 in OOOooo0OooOoO :
      os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
     for ii1I in IIIIIii1ii11 :
      shutil . rmtree ( os . path . join ( iIoo0ooooO , ii1I ) )
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
 if 62 - 62: IIiIiII11i
 if 60 - 60: ooOoO0O00 * IIiIiII11i + iI1ii11iIi1i / ii1ii11IIIiiI % OOooOOo
 if 100 - 100: iI11I1II1I1I * ooOoO0O00 - Ii - ii1ii11IIIiiI % iI1ii11iIi1i
 if 56 - 56: I11O0O0oOO00O00o
 if 99 - 99: ii % ooOoO0O00 % ii . Ii1IIIi1
 if 20 - 20: oO0o . oO0oo0o
 if 4 - 4: I1ii11iIi11i % iI1ii11iIi1i % oO0o * Ii1IIIi1 % ii
 if 38 - 38: ii . Ii1IIIi1
 if 43 - 43: ii
def oO0O000oOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0OOOO0o0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( O0OOOO0o0O ) :
   IIIi1ii1i1 = 0
   IIIi1ii1i1 += len ( OOOooo0OooOoO )
   if 8 - 8: O00o0O00 + I11O0O0oOO00O00o . I11O0O0oOO00O00o
   if 89 - 89: Ii1I * Ii1I * OOooOOo / Ii1IIIi1
   if IIIi1ii1i1 > 0 :
    if 60 - 60: oO0o / Ii1IIIi1 / oOo0O0Ooo + oO0oo0o
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( IIIi1ii1i1 ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: ii * iI1ii11iIi1i / o0o00Oo0O + iI1ii11iIi1i - iI11I1II1I1I
     for o0Oo00 in OOOooo0OooOoO :
      os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
     for ii1I in IIIIIii1ii11 :
      shutil . rmtree ( os . path . join ( iIoo0ooooO , ii1I ) )
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
 if 6 - 6: ooOOOoO - I1ii11iIi11i - I11O0O0oOO00O00o - o0o00Oo0O % ii
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if 27 - 27: Ii % Ii1IIIi1 + iI1ii11iIi1i . O00o0O00
 if 9 - 9: oO0o
 if 43 - 43: iI1ii11iIi1i . O00o0O00 + oOo0O0Ooo * Ii
 if 2 - 2: O00o0O00
 if 3 - 3: oOo0O0Ooo . Ii1IIIi1 % o0o00Oo0O - O0OOOoOoo0 / o0o00Oo0O
 if 79 - 79: iI1ii11iIi1i + oO0oo0o % O0OOOoOoo0 % oOo0O0Ooo
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: Ii1IIIi1 . oO0oo0o / I1ii11iIi11i . oO0o . Ii
def ooOOO ( url , name ) :
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoooo = os . path . join ( I1i , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 I11Ii1 = os . path . join ( I1i , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11Ii1 ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   I1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOoooo = os . path . join ( I1i , 'advancedsettings.xml' )
   try :
    os . remove ( OOoooo )
    print '=== GenieTv - REMOVING    ' + str ( OOoooo ) + '    ==='
   except :
    pass
   OOO00O = ii11iIi1I . http_GET ( url ) . content
   ooO0oO00O0o = open ( OOoooo , "w" )
   ooO0oO00O0o . write ( OOO00O )
   ooO0oO00O0o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOoooo ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  I1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOoooo = os . path . join ( I1i , 'advancedsettings.xml' )
  try :
   os . remove ( OOoooo )
   print '=== GenieTv - REMOVING    ' + str ( OOoooo ) + '    ==='
  except :
   pass
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  ooO0oO00O0o = open ( OOoooo , "w" )
  ooO0oO00O0o . write ( OOO00O )
  ooO0oO00O0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoooo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 63 - 63: ooOoO0O00
def II1iII11 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoooo = os . path . join ( I1i , 'advancedsettings.xml' )
 try :
  ooO0oO00O0o = open ( OOoooo ) . read ( )
  if 'zero' in ooO0oO00O0o :
   name = '0CACHE'
  elif 'tuxen' in ooO0oO00O0o :
   name = 'TUXENS'
  elif 'muckys' in ooO0oO00O0o :
   name = 'MUCKYS'
  elif 'p2p1' in ooO0oO00O0o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooO0oO00O0o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooO0oO00O0o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 19 - 19: IIiIiII11i
def i1iIIi ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 I1i = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOoooo = os . path . join ( I1i , 'advancedsettings.xml' )
 try :
  os . remove ( OOoooo )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOoooo ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 63 - 63: ii * ii1ii11IIIiiI
 if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . oO0oo0o % IIiIiII11i
 if 18 - 18: I11O0O0oOO00O00o % ii + oO0o / I11O0O0oOO00O00o
 if 37 - 37: ooOoO0O00 - iI1ii11iIi1i / ooOOOoO . IIiIiII11i % O0OOOoOoo0
 if 39 - 39: iI1ii11iIi1i % Ii * oO0o
 if 23 - 23: O00o0O00 + O0OOOoOoo0 / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: Ii1IIIi1 - I11i
 if 92 - 92: I1ii11iIi11i % I11i - O0OOOoOoo0 / O0OOOoOoo0 / OOooOOo
 if 84 - 84: O00o0O00
 if 4 - 4: ooOOOoO . ii1ii11IIIiiI / iI1ii11iIi1i / Ii1IIIi1 + IIiIiII11i
def IiiiiI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi1I11I1II = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for OOOoOOooOoo , O00OO0oOOO , I1ii11ii1iiI , oO0oo0 in IIi1I11I1II :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOOoOOooOoo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1ii11ii1iiI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % oO0oo0 )
  inc = inc + 1
  if 12 - 12: Ii + ooOoO0O00 - iI1ii11iIi1i + o0o00Oo0O . oOo0O0Ooo
  if 8 - 8: I11i
  if 78 - 78: ooOoO0O00 - I1ii11iIi11i
  if 48 - 48: iI1ii11iIi1i - ii + ii1ii11IIIiiI % I11i - OOooOOo . oOo0O0Ooo
  if 42 - 42: ii1ii11IIIiiI
  if 70 - 70: I11i / I11O0O0oOO00O00o + oO0oo0o % oOo0O0Ooo % I1ii11iIi11i + oO0o
  if 80 - 80: O00o0O00
  if 12 - 12: iI1ii11iIi1i
  if 2 - 2: ii
def OO0ooOo ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  I1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoooo = os . path . join ( I1i , 'addons2.ini' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  ooO0oO00O0o = open ( OOoooo , "w" )
  ooO0oO00O0o . write ( OOO00O )
  ooO0oO00O0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoooo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 75 - 75: ii
def I1IiII ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  I1i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOoooo = os . path . join ( I1i , 'settings.xml' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  ooO0oO00O0o = open ( OOoooo , "w" )
  ooO0oO00O0o . write ( OOO00O )
  ooO0oO00O0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOoooo ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 85 - 85: ii1ii11IIIiiI - O0OOOoOoo0 - Ii1IIIi1
 if 30 - 30: oOo0O0Ooo . iI1ii11iIi1i - iI1ii11iIi1i * ooOoO0O00 + ii1ii11IIIiiI * I11O0O0oOO00O00o
def oOOo ( ) :
 try :
  ii1I1IiiI1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ii1I1IiiI1 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o0OOO = os . path . join ( ii1I1IiiI1 , "source.db" )
    os . unlink ( o0OOO )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 95 - 95: Ii1IIIi1 - O00o0O00 * Ii1IIIi1
 if 65 - 65: O00o0O00 % ooOOOoO % I11i . iI1ii11iIi1i . Ii1I
 if 64 - 64: Ii1I . iI1ii11iIi1i / Ii1I * iI1ii11iIi1i
 if 86 - 86: iI11I1II1I1I * Ii1IIIi1 * iI1ii11iIi1i / oO0o % O0OOOoOoo0 - o0o00Oo0O
 if 63 - 63: Ii1I
def O0i1II1Iiii1I11 ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 16 - 16: oO0o + oO0oo0o * ooOoO0O00 / Ii1I
 if 100 - 100: oOo0O0Ooo - O00o0O00
 if 91 - 91: I11i * Ii1I - Ii1IIIi1 . IIiIiII11i
 if 1 - 1: O00o0O00 + ii1ii11IIIiiI * Ii1I
 if 44 - 44: Ii1IIIi1
 if 79 - 79: I11i % O00o0O00 . o0o00Oo0O
 if 56 - 56: oO0oo0o + ooOoO0O00 * Ii1IIIi1 - o0o00Oo0O
def O0oO0o00OoO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; O000o = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O000o :
  oOO0O0o0Oo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oOO0O0o0Oo = xbmc . translatePath ( oOO0O0o0Oo ) ;
  i11i1IiIi = os . path . join ( oOO0O0o0Oo , ".." , ".." ) ; i11i1IiIi = os . path . abspath ( i11i1IiIi ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + i11i1IiIi ) ; ooOoOoOOOo = False
  try :
   for iIoo0ooooO , IIIIIii1ii11 , OOOooo0OooOoO in os . walk ( i11i1IiIi , topdown = True ) :
    IIIIIii1ii11 [ : ] = [ ii1I for ii1I in IIIIIii1ii11 if ii1I not in o0oO0 ]
    for oO00oooOOoOo0 in OOOooo0OooOoO :
     try : os . remove ( os . path . join ( iIoo0ooooO , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : ooOoOoOOOo = True
      plugintools . log ( "Error removing " + iIoo0ooooO + " " + oO00oooOOoOo0 )
    for oO00oooOOoOo0 in IIIIIii1ii11 :
     try : os . rmdir ( os . path . join ( iIoo0ooooO , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Database" , "userdata" ] : ooOoOoOOOo = True
      plugintools . log ( "Error removing " + iIoo0ooooO + " " + oO00oooOOoOo0 )
   if not ooOoOoOOOo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoOOOO ( )
 if 73 - 73: Ii / OOooOOo
 if 45 - 45: I11O0O0oOO00O00o . oO0o
 if 14 - 14: O00o0O00 * oOo0O0Ooo - Ii1I
def I1111I1i1i ( ) :
 O0oOo = [ ]
 I1i1II = sys . argv [ 2 ]
 if len ( I1i1II ) >= 2 :
  o000 = sys . argv [ 2 ]
  iiI11i = o000 . replace ( '?' , '' )
  if ( o000 [ len ( o000 ) - 1 ] == '/' ) :
   o000 = o000 [ 0 : len ( o000 ) - 2 ]
  IIiI1IiI1iIi1 = iiI11i . split ( '&' )
  O0oOo = { }
  for iiiI1iI1 in range ( len ( IIiI1IiI1iIi1 ) ) :
   iIiiI11II11 = { }
   iIiiI11II11 = IIiI1IiI1iIi1 [ iiiI1iI1 ] . split ( '=' )
   if ( len ( iIiiI11II11 ) ) == 2 :
    O0oOo [ iIiiI11II11 [ 0 ] ] = iIiiI11II11 [ 1 ]
    if 75 - 75: ii1ii11IIIiiI - Ii1IIIi1 . oO0oo0o
 return O0oOo
 if 88 - 88: Ii1IIIi1 - ii . O0OOOoOoo0 - I11i / OOooOOo % I11O0O0oOO00O00o
o00O00o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1oOOOOOOOoO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ooO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O00O0O0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
iI111I11i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
ii1IiIi1iIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oO0oo0oOO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IIiI111Iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iIOoO0O00 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0o00 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iI1iIi1ii1I1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iI11IIi1iiI1I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1I11IIi1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
i1II1iIii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iI1i11II1i1i = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oOO0O = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iIIi1IIi = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OOiIiI1iI = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
IIIIIiII1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iIIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOO0oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iiiIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
III11IiI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OooOooo0 = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOOOO00 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i1i1IIi1I = [ ]
  if showcontext == 'fav' :
   I1i1i1IIi1I . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   I1i1i1IIi1I . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OOoOOOO00 . addContextMenuItems ( I1i1i1IIi1I )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = True )
 return i11IiI1iiI11
 if 61 - 61: Ii - ii
def iIiIIi1 ( name , url , mode , iconimage , fanart , description ) :
 oOOO0ooOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11IiI1iiI11 = True
 OOoOOOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOoOOOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOoOOOO00 . setProperty ( "Fanart_Image" , fanart )
 i11IiI1iiI11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO0ooOO , listitem = OOoOOOO00 , isFolder = False )
 return i11IiI1iiI11
 if 90 - 90: oOo0O0Ooo
 if 4 - 4: O00o0O00 % O0OOOoOoo0 - O00o0O00 - I11i
o000 = I1111I1i1i ( )
i1I1ii11i1Iii = None
oO00oooOOoOo0 = None
OooO0OOo = None
iiiI1I1iIIIi1 = None
oOo0O = None
ii1Oo0000oOo = None
iI1IIIiIII11 = None
if 70 - 70: ii + oO0o * I1ii11iIi11i
if 20 - 20: Ii - IIiIiII11i - O0OOOoOoo0 % oO0oo0o . O0OOOoOoo0
try :
 iI1IIIiIII11 = int ( o000 [ "fav_mode" ] )
except :
 pass
 if 50 - 50: iI11I1II1I1I + ii1ii11IIIiiI - I11O0O0oOO00O00o - ii
try :
 i1I1ii11i1Iii = urllib . unquote_plus ( o000 [ "url" ] )
except :
 pass
try :
 oO00oooOOoOo0 = urllib . unquote_plus ( o000 [ "name" ] )
except :
 pass
try :
 iiiI1I1iIIIi1 = urllib . unquote_plus ( o000 [ "iconimage" ] )
except :
 pass
try :
 OooO0OOo = int ( o000 [ "mode" ] )
except :
 pass
try :
 oOo0O = urllib . unquote_plus ( o000 [ "fanart" ] )
except :
 pass
try :
 ii1Oo0000oOo = urllib . unquote_plus ( o000 [ "description" ] )
except :
 pass
 if 84 - 84: OOooOOo - I11O0O0oOO00O00o
 if 80 - 80: Ii % O00o0O00 - I1ii11iIi11i % O00o0O00
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OooO0OOo )
print "URL: " + str ( i1I1ii11i1Iii )
print "Name: " + str ( oO00oooOOoOo0 )
print "IconImage: " + str ( iiiI1I1iIIIi1 )
if 89 - 89: iI1ii11iIi1i * I11O0O0oOO00O00o + OOooOOo / Ii
if 68 - 68: ii * I11O0O0oOO00O00o
def I1I1II1I11 ( content , viewType ) :
 if 86 - 86: I11i / OOooOOo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 40 - 40: Ii1IIIi1
if iiiI1I1iIIIi1 == None : iiiI1I1iIIIi1 = Ooo
if oOo0O == None : oOo0O = OO0o
if OooO0OOo == None :
 I11IiI ( )
 if 62 - 62: O0OOOoOoo0 / O00o0O00
elif OooO0OOo == 1 :
 oO0oOo00o00oO ( i1I1ii11i1Iii )
 if 74 - 74: Ii1IIIi1 % ii1ii11IIIiiI / ii1ii11IIIiiI - iI11I1II1I1I - IIiIiII11i + O00o0O00
elif OooO0OOo == 44 :
 o0Oo ( i1I1ii11i1Iii )
 if 92 - 92: I11O0O0oOO00O00o % ii1ii11IIIiiI
elif OooO0OOo == 2 :
 oo0 ( )
 if 18 - 18: O0OOOoOoo0 + ii1ii11IIIiiI / O00o0O00 / oO0oo0o + iI11I1II1I1I % ooOOOoO
elif OooO0OOo == 3 :
 ooO000O ( )
 if 94 - 94: I11O0O0oOO00O00o
elif OooO0OOo == 21 :
 i1i1II ( )
 if 37 - 37: oO0oo0o
elif OooO0OOo == 4 :
 IiI ( )
 if 52 - 52: Ii1I * oOo0O0Ooo . O00o0O00 + ooOoO0O00 % oO0oo0o / iI11I1II1I1I
elif OooO0OOo == 5 :
 iIIIiIi1I1i ( i1I1ii11i1Iii )
 if 68 - 68: ii1ii11IIIiiI - OOooOOo . Ii + I11i
elif OooO0OOo == 6 :
 oOOoooo0o0 ( i1I1ii11i1Iii )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif OooO0OOo == 7 :
 ooOOO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 33 - 33: I11O0O0oOO00O00o . I1ii11iIi11i
elif OooO0OOo == 8 :
 II1iII11 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 89 - 89: Ii1IIIi1 + ooOoO0O00 - ooOOOoO + O0OOOoOoo0 . IIiIiII11i
elif OooO0OOo == 9 :
 FIXREPOSADDONS ( i1I1ii11i1Iii )
 if 85 - 85: iI11I1II1I1I - iI1ii11iIi1i * I1ii11iIi11i . oO0oo0o + ii1ii11IIIiiI
elif OooO0OOo == 10 :
 Oo0o0O00 ( )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif OooO0OOo == 11 :
 i1iIIi ( i1I1ii11i1Iii )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . Ii1IIIi1 / Ii1IIIi1
elif OooO0OOo == 12 :
 IiiiiI ( )
 if 43 - 43: oOo0O0Ooo
elif OooO0OOo == 13 :
 oOi1II111i1IIii ( )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif OooO0OOo == 14 :
 ooO0oOOooOo0 ( i1I1ii11i1Iii )
 if 34 - 34: I11i % Ii1I + iI1ii11iIi1i * I11O0O0oOO00O00o / oO0oo0o
elif OooO0OOo == 15 :
 iii1IIII1iii11I ( )
 if 18 - 18: O0OOOoOoo0
elif OooO0OOo == 16 :
 OO0ooOo ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 92 - 92: oO0o % iI11I1II1I1I / ooOOOoO * Ii1IIIi1 . ooOoO0O00 + oO0oo0o
elif OooO0OOo == 17 :
 I1IiII ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 24 - 24: ooOOOoO . Ii1IIIi1 * ooOOOoO % Ii . Ii + ooOoO0O00
elif OooO0OOo == 18 :
 oOOo ( )
 if 64 - 64: iI11I1II1I1I / ooOOOoO / I1ii11iIi11i - Ii1I
elif OooO0OOo == 19 :
 oO0oOooooOoO ( i1I1ii11i1Iii )
 if 100 - 100: ooOOOoO + ooOoO0O00 * oO0o
elif OooO0OOo == 40 :
 i1i1IiIiIi1Ii ( oO00oooOOoOo0 , i1I1ii11i1Iii , ii1Oo0000oOo )
 if 64 - 64: oO0oo0o * Ii . I1ii11iIi11i
elif OooO0OOo == 42 :
 I1i1iIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , ii1Oo0000oOo )
 if 52 - 52: I1ii11iIi11i / O0OOOoOoo0 / Ii1IIIi1 - I11i / Ii1IIIi1
elif OooO0OOo == 43 :
 oO0OO ( i1I1ii11i1Iii )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif OooO0OOo == 20 :
 iii11II1I ( i1I1ii11i1Iii )
 if 85 - 85: oOo0O0Ooo
elif OooO0OOo == 22 :
 I1O0 ( i1I1ii11i1Iii )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif OooO0OOo == 23 :
 IIio0 ( i1I1ii11i1Iii )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif OooO0OOo == 24 :
 I11I111i ( i1I1ii11i1Iii )
 if 46 - 46: OOooOOo * I11O0O0oOO00O00o / oO0oo0o + I1ii11iIi11i + ooOOOoO
elif OooO0OOo == 25 :
 iIIoooO0 ( i1I1ii11i1Iii )
 if 95 - 95: I11i - iI1ii11iIi1i
elif OooO0OOo == 26 :
 iioOo00O0o ( i1I1ii11i1Iii )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif OooO0OOo == 27 :
 II1iiIiI1 ( i1I1ii11i1Iii )
 if 19 - 19: OOooOOo . O00o0O00 . ii
elif OooO0OOo == 28 :
 iii11I1 ( i1I1ii11i1Iii )
 if 79 - 79: O00o0O00 * O0OOOoOoo0 * oOo0O0Ooo * Ii1I / Ii1I
elif OooO0OOo == 29 :
 oOOOoo0 ( i1I1ii11i1Iii )
 if 62 - 62: O0OOOoOoo0 * iI1ii11iIi1i % Ii1I - ooOoO0O00 - Ii1I
elif OooO0OOo == 30 :
 i1oO ( i1I1ii11i1Iii )
 if 24 - 24: O00o0O00
elif OooO0OOo == 31 :
 oO0OOOOO00O0OO ( i1I1ii11i1Iii )
 if 71 - 71: ooOOOoO - ooOoO0O00
elif OooO0OOo == 32 :
 iiiiI11ii ( )
 if 56 - 56: OOooOOo + oO0oo0o
elif OooO0OOo == 33 :
 II1iiIiIiI ( )
 if 74 - 74: Ii1IIIi1 / ii1ii11IIIiiI / IIiIiII11i - Ii1IIIi1 / oO0oo0o % I11O0O0oOO00O00o
elif OooO0OOo == 35 :
 Oo0O0Oo00O ( i1I1ii11i1Iii )
 if 19 - 19: ooOOOoO % ii + ii
elif OooO0OOo == 34 :
 IIo0OoO00 ( i1I1ii11i1Iii )
 if 7 - 7: ooOoO0O00
elif OooO0OOo == 36 :
 IiiIi ( i1I1ii11i1Iii )
 if 91 - 91: OOooOOo - OOooOOo . ooOOOoO
elif OooO0OOo == 37 :
 i1I11iIII1i1I ( i1I1ii11i1Iii )
 if 33 - 33: ii1ii11IIIiiI - iI11I1II1I1I / iI1ii11iIi1i % o0o00Oo0O
elif OooO0OOo == 38 :
 iii1III1i ( i1I1ii11i1Iii )
 if 80 - 80: ooOOOoO % ii - ooOOOoO
elif OooO0OOo == 41 :
 O0oO0o00OoO ( o000 )
 if 27 - 27: ii1ii11IIIiiI - I11i * Ii1I - oOo0O0Ooo
elif OooO0OOo == 39 :
 ii1III11 ( i1I1ii11i1Iii )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - Ii1IIIi1 . iI1ii11iIi1i
elif OooO0OOo == 45 :
 TEXTS ( )
 if 100 - 100: IIiIiII11i / ii1ii11IIIiiI / Ii1IIIi1 - Ii1I * iI11I1II1I1I
elif OooO0OOo == 46 :
 iiII ( )
 if 7 - 7: ooOoO0O00 . ooOOOoO % Ii * Ii1I . I11O0O0oOO00O00o % Ii1I
elif OooO0OOo == 47 :
 GEVID ( )
 if 35 - 35: oOo0O0Ooo
elif OooO0OOo == 48 :
 I1Iiii ( oO00oooOOoOo0 , i1I1ii11i1Iii , ii1Oo0000oOo )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif OooO0OOo == 49 :
 ooi1II1I ( )
 if 22 - 22: O0OOOoOoo0 . Ii . ii . ooOoO0O00
elif OooO0OOo == 222 :
 O0iIiIIIIIii ( i1I1ii11i1Iii )
 if 12 - 12: OOooOOo % O00o0O00 + oO0oo0o . o0o00Oo0O % iI11I1II1I1I
elif OooO0OOo == 333 :
 IIi1 ( i1I1ii11i1Iii )
 if 41 - 41: ii
 if 13 - 13: I11O0O0oOO00O00o + ii1ii11IIIiiI - ii1ii11IIIiiI % oO0oo0o / I11O0O0oOO00O00o
elif OooO0OOo == 1020 :
 OO00O00 ( )
 if 4 - 4: oOo0O0Ooo + O00o0O00 - ooOOOoO + Ii1IIIi1
elif OooO0OOo == 1021 :
 ANIMEEP ( )
 if 78 - 78: iI1ii11iIi1i
elif OooO0OOo == 1022 :
 ANIMEPLAY ( i1I1ii11i1Iii )
 if 29 - 29: IIiIiII11i
elif OooO0OOo == 1001 :
 O0Oo0O0O0o ( )
 if 79 - 79: iI11I1II1I1I - Ii + O0OOOoOoo0 - IIiIiII11i . iI11I1II1I1I
elif OooO0OOo == 1005 :
 iIIiI1I1i1 ( )
 if 84 - 84: I1ii11iIi11i % I11O0O0oOO00O00o * o0o00Oo0O * I11O0O0oOO00O00o
elif OooO0OOo == 1007 :
 Iii11I ( i1I1ii11i1Iii )
 if 66 - 66: O00o0O00 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OOOoOoo0
elif OooO0OOo == 1010 :
 i11iI11ii ( i1I1ii11i1Iii )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif OooO0OOo == 1011 :
 Iii1i1I ( i1I1ii11i1Iii )
 if 37 - 37: ooOoO0O00 * Ii
elif OooO0OOo == 1012 :
 oOooo0OO0O0 ( i1I1ii11i1Iii )
 if 95 - 95: Ii % ii1ii11IIIiiI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif OooO0OOo == 1030 :
 iIIIIi1iiI ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / O00o0O00 / ii1ii11IIIiiI
elif OooO0OOo == 1031 :
 O0ii ( i1I1ii11i1Iii , iiiI1I1iIIIi1 )
 if 35 - 35: Ii1IIIi1 * O00o0O00
elif OooO0OOo == 1032 :
 IIi1iiIIi1i ( i1I1ii11i1Iii )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif OooO0OOo == 1006 :
 Parse . ParseURL ( i1I1ii11i1Iii )
 if 13 - 13: oO0o * ii1ii11IIIiiI + I1ii11iIi11i - ooOOOoO
elif OooO0OOo == 2030 :
 Parse . addonParseURL ( i1I1ii11i1Iii )
 if 31 - 31: oO0o
elif OooO0OOo == 2031 :
 Parse . apkParseURL ( i1I1ii11i1Iii )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif OooO0OOo == 1002 :
 o0Oo0o ( i1I1ii11i1Iii )
 if 77 - 77: Ii - ii1ii11IIIiiI . Ii1I % I1ii11iIi11i . iI1ii11iIi1i
elif OooO0OOo == 1003 :
 i1ii ( i1I1ii11i1Iii , iiiI1I1iIIIi1 )
 if 9 - 9: I11i
elif OooO0OOo == 1004 :
 oO0oOo ( i1I1ii11i1Iii )
 if 55 - 55: O00o0O00 % iI11I1II1I1I + I11O0O0oOO00O00o . O0OOOoOoo0
elif OooO0OOo == 1008 :
 i1IIii1i ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif OooO0OOo == 1009 :
 OOO0oOoO00OoO ( i1I1ii11i1Iii )
 if 23 - 23: Ii
elif OooO0OOo == 2001 :
 IIIi ( )
 if 88 - 88: IIiIiII11i - Ii1IIIi1 / ii
elif OooO0OOo == 2002 :
 i1iI1iIII ( i1I1ii11i1Iii )
 if 71 - 71: Ii1I
elif OooO0OOo == 1013 :
 o0o0O0Oo ( )
elif OooO0OOo == 10111113 :
 IiiIIi ( i1I1ii11i1Iii )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OooO0OOo == 1014 :
 iII111iiiI11i ( )
 if 1 - 1: ooOOOoO % ooOoO0O00
elif OooO0OOo == 1015 :
 i1i111III1 ( i1I1ii11i1Iii )
 if 41 - 41: oO0o * oO0o / Ii1IIIi1 + Ii1I . I11i
elif OooO0OOo == 1016 :
 I1Ii1iI1IiI1I ( i1I1ii11i1Iii , iiiI1I1iIIIi1 , oO00oooOOoOo0 )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / iI1ii11iIi1i
elif OooO0OOo == 1017 :
 iI1II ( )
 if 80 - 80: Ii1I
elif OooO0OOo == 1018 :
 iiIi11iI1iii ( i1I1ii11i1Iii )
 if 67 - 67: IIiIiII11i
elif OooO0OOo == 1023 :
 iIIIi1i1I11i ( )
 if 2 - 2: I11i - o0o00Oo0O * iI1ii11iIi1i % ooOOOoO
elif OooO0OOo == 1024 :
 IiiiII ( i1I1ii11i1Iii )
 if 64 - 64: ooOoO0O00 . O0OOOoOoo0
elif OooO0OOo == 1025 :
 OoOo00OoOO00 ( i1I1ii11i1Iii )
 if 7 - 7: oO0oo0o . Ii1IIIi1 - Ii1IIIi1 / ii1ii11IIIiiI % I1ii11iIi11i
elif OooO0OOo == 4001 :
 oo0O0 ( )
 if 61 - 61: oO0oo0o - Ii1I / Ii1IIIi1 % Ii1I + oO0o / I1ii11iIi11i
elif OooO0OOo == 4002 :
 O000OOO ( )
 if 10 - 10: Ii / OOooOOo
elif OooO0OOo == 4003 :
 oO00oOo0OOO ( )
 if 27 - 27: oOo0O0Ooo / ii
elif OooO0OOo == 4004 :
 I1II1 ( )
 if 74 - 74: Ii1I % ii1ii11IIIiiI - oO0o * I11O0O0oOO00O00o . ii * oO0o
elif OooO0OOo == 4005 :
 Iii11iI1i ( )
 if 99 - 99: OOooOOo . Ii1IIIi1 - ii - o0o00Oo0O
elif OooO0OOo == 4006 :
 o0O0OOOOoOO0 ( )
 if 6 - 6: O00o0O00
elif OooO0OOo == 4007 :
 ii1I1IIii11 ( )
 if 3 - 3: o0o00Oo0O - ii1ii11IIIiiI * iI1ii11iIi1i * O00o0O00 / iI1ii11iIi1i
elif OooO0OOo == 4008 :
 O0o0oO ( )
 if 58 - 58: iI1ii11iIi1i * iI11I1II1I1I + O0OOOoOoo0 . O0OOOoOoo0
elif OooO0OOo == 4009 : oooO ( )
elif OooO0OOo == 4010 : i11i1iiI1i ( )
elif OooO0OOo == 3000 :
 oo00OOo0 ( )
 if 74 - 74: O0OOOoOoo0 - I11i * ooOOOoO % O0OOOoOoo0
elif OooO0OOo == 3001 :
 iiIIi1I1iIIIiiii ( )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * ii1ii11IIIiiI - oO0o - I11i
elif OooO0OOo == 3002 :
 O0oIi1iIiIi1I11 ( i1I1ii11i1Iii )
 if 44 - 44: ii
elif OooO0OOo == 3003 :
 ii1I11 ( i1I1ii11i1Iii )
 if 82 - 82: OOooOOo . OOooOOo
elif OooO0OOo == 3004 :
 O0oo0oOoO00 ( i1I1ii11i1Iii )
 if 10 - 10: I1ii11iIi11i * Ii1I . oO0oo0o . ii . O00o0O00 * Ii1I
elif OooO0OOo == 404 :
 ii1O0oOOo ( oO00oooOOoOo0 , i1I1ii11i1Iii , iiiI1I1iIIIi1 )
 if 80 - 80: ii1ii11IIIiiI + I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00
elif OooO0OOo == 405 :
 iiii1ii1 ( i1I1ii11i1Iii )
 if 85 - 85: Ii . I11O0O0oOO00O00o + iI1ii11iIi1i / iI1ii11iIi1i
elif OooO0OOo == 7030 :
 iioo ( )
 if 43 - 43: ooOOOoO . ii - IIiIiII11i
elif OooO0OOo == 7021 :
 I11IIiI1IiI1 ( oO00oooOOoOo0 )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O00o0O00 * oO0oo0o
elif OooO0OOo == 7022 :
 iIIi1iii1 ( oO00oooOOoOo0 )
 if 19 - 19: ii1ii11IIIiiI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OooO0OOo == 7000 :
 o00o0o0oOo0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , img )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OooO0OOo == 7050 :
 o0iii1i ( i1I1ii11i1Iii )
 if 15 - 15: iI1ii11iIi1i + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OooO0OOo == 7051 :
 oo0O00o0 ( i1I1ii11i1Iii )
 if 54 - 54: ooOOOoO - IIiIiII11i . O0OOOoOoo0 + iI1ii11iIi1i
elif OooO0OOo == 7052 :
 iIIiI11Ii1iI ( i1I1ii11i1Iii )
 if 45 - 45: oO0oo0o + IIiIiII11i . Ii1IIIi1 / Ii1I
elif OooO0OOo == 7053 :
 ooOo0 ( i1I1ii11i1Iii )
 if 76 - 76: iI1ii11iIi1i + Ii1IIIi1 - ooOOOoO * iI11I1II1I1I % ooOoO0O00
elif OooO0OOo == 7054 :
 CoolPlay ( i1I1ii11i1Iii )
 if 72 - 72: O0OOOoOoo0 + IIiIiII11i . o0o00Oo0O - Ii1IIIi1 / ii . ii1ii11IIIiiI
elif OooO0OOo == 7060 :
 iII ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OooO0OOo == 7061 :
 I1IIiIi ( i1I1ii11i1Iii )
 if 32 - 32: ii
elif OooO0OOo == 7063 :
 O0ooiIIi1 ( i1I1ii11i1Iii )
 if 29 - 29: Ii1I
elif OooO0OOo == 7062 :
 O00Oo ( i1I1ii11i1Iii )
 if 41 - 41: iI1ii11iIi1i
elif OooO0OOo == 7064 :
 NATatozcat ( )
 if 49 - 49: iI1ii11iIi1i % IIiIiII11i . iI1ii11iIi1i - I11i - I11O0O0oOO00O00o * ooOOOoO
elif OooO0OOo == 7067 :
 oOOoo ( i1I1ii11i1Iii )
 if 47 - 47: o0o00Oo0O . I11i / iI1ii11iIi1i * Ii1IIIi1
elif OooO0OOo == 7066 :
 NATatozA ( i1I1ii11i1Iii )
 if 63 - 63: ii1ii11IIIiiI - oO0oo0o - Ii1IIIi1 - O0OOOoOoo0 / oO0oo0o + oO0o
elif OooO0OOo == 7065 :
 oo0O0Ii111Ii11 ( i1I1ii11i1Iii )
 if 94 - 94: ooOOOoO / oOo0O0Ooo . IIiIiII11i
elif OooO0OOo == 7070 :
 IiiIIIIi ( )
 if 32 - 32: oO0oo0o . O00o0O00 % O00o0O00 . OOooOOo
elif OooO0OOo == 7071 :
 DIZIlist ( i1I1ii11i1Iii )
 if 37 - 37: O00o0O00 + o0o00Oo0O + O00o0O00 . Ii1IIIi1 . I11i
elif OooO0OOo == 7072 :
 DIZIpull ( i1I1ii11i1Iii )
 if 78 - 78: oOo0O0Ooo / I11O0O0oOO00O00o + I11i . I1ii11iIi11i / o0o00Oo0O
elif OooO0OOo == 7073 :
 WATCHDIZI ( i1I1ii11i1Iii )
 if 49 - 49: Ii1I
elif OooO0OOo == 7002 :
 III11iIII1 ( )
 if 66 - 66: I11i . Ii1I
elif OooO0OOo == 7003 :
 O00O00oO ( i1I1ii11i1Iii )
 if 18 - 18: I1ii11iIi11i + ooOOOoO
elif OooO0OOo == 7004 :
 oo0OoOO000O ( i1I1ii11i1Iii )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % iI1ii11iIi1i . oOo0O0Ooo
elif OooO0OOo == 7020 :
 OOO0ooO0Oo0 ( i1I1ii11i1Iii )
 if 43 - 43: oOo0O0Ooo % Ii1I * iI1ii11iIi1i
elif OooO0OOo == 7001 :
 iI111iIi ( )
 if 31 - 31: iI1ii11iIi1i / Ii1IIIi1
elif OooO0OOo == 7010 :
 oooooOoOO ( i1I1ii11i1Iii )
 if 3 - 3: ooOOOoO
elif OooO0OOo == 7011 :
 i1Ii1IiiIi1II ( i1I1ii11i1Iii )
 if 37 - 37: iI1ii11iIi1i * ii * I11O0O0oOO00O00o + I1ii11iIi11i . oOo0O0Ooo
elif OooO0OOo == 7012 :
 Oo0Oo00O00o0 ( i1I1ii11i1Iii )
 if 61 - 61: O00o0O00 . O00o0O00
elif OooO0OOo == 7013 :
 cnfTVPlay2 ( i1I1ii11i1Iii )
elif OooO0OOo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1I1ii11i1Iii )
elif OooO0OOo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1I1ii11i1Iii )
elif OooO0OOo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oO00oooOOoOo0 , i1I1ii11i1Iii , iiiI1I1iIIIi1 )
elif OooO0OOo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OooO0OOo == 7018 :
 Ii1o0OOOoo0000 ( )
elif OooO0OOo == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1I1ii11i1Iii )
elif OooO0OOo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1I1ii11i1Iii )
elif OooO0OOo == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1I1ii11i1Iii )
 if 17 - 17: IIiIiII11i / O0OOOoOoo0
elif OooO0OOo == 8000 :
 ii1O0O ( )
elif OooO0OOo == 8001 :
 O0OOooO ( )
elif OooO0OOo == 8002 :
 oooO00oo0 ( )
elif OooO0OOo == 8003 :
 oooooO0OO ( )
elif OooO0OOo == 8004 :
 O0iI1I1ii11IIi1 ( )
elif OooO0OOo == 8005 :
 IIiIi11i111II ( )
elif OooO0OOo == 8006 :
 Oo00o ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif OooO0OOo == 8030 :
 i1o0oooO ( i1I1ii11i1Iii )
elif OooO0OOo == 8045 :
 iiIiIiIiiIiI ( i1I1ii11i1Iii )
elif OooO0OOo == 8046 :
 iIi1i ( i1I1ii11i1Iii )
elif OooO0OOo == 8047 :
 iIiII11 ( i1I1ii11i1Iii )
elif OooO0OOo == 8048 :
 Ii1I1IIIiI1i ( i1I1ii11i1Iii )
elif OooO0OOo == 8049 :
 o0Oo00oOO ( i1I1ii11i1Iii )
elif OooO0OOo == 8020 :
 oOoOOo ( )
elif OooO0OOo == 8021 :
 I1111ii11 ( i1I1ii11i1Iii )
elif OooO0OOo == 8022 :
 I1iI1I1111i ( i1I1ii11i1Iii )
elif OooO0OOo == 8023 :
 iII11IiIIII ( i1I1ii11i1Iii )
elif OooO0OOo == 8040 :
 O0O0 ( )
elif OooO0OOo == 8041 :
 oO0oo ( i1I1ii11i1Iii )
elif OooO0OOo == 8042 :
 i1oooOoOoOO ( i1I1ii11i1Iii )
elif OooO0OOo == 8043 :
 yt . PlayVideo ( i1I1ii11i1Iii )
elif OooO0OOo == 8044 :
 OooOO ( i1I1ii11i1Iii )
elif OooO0OOo == 8060 :
 OOOO00 ( )
elif OooO0OOo == 8061 :
 o0I1iI111ii111i ( i1I1ii11i1Iii )
elif OooO0OOo == 8064 :
 Oo0O0O ( )
elif OooO0OOo == 8065 :
 IiIiiI1ii111 ( i1I1ii11i1Iii )
elif OooO0OOo == 8070 :
 oOo000O00O0 ( )
elif OooO0OOo == 8071 :
 iI1iiIii1I11I ( i1I1ii11i1Iii )
elif OooO0OOo == 7080 :
 Ii1IiiiI1ii ( i1I1ii11i1Iii )
elif OooO0OOo == 8090 :
 iII11IiI1 ( )
elif OooO0OOo == 8091 :
 OoOOOO00oOO ( i1I1ii11i1Iii )
elif OooO0OOo == 8092 :
 O000oO ( i1I1ii11i1Iii )
elif OooO0OOo == 8093 :
 iiIIiIi ( i1I1ii11i1Iii )
elif OooO0OOo == 8081 :
 o00O ( )
elif OooO0OOo == 8062 :
 IIiii ( i1I1ii11i1Iii )
elif OooO0OOo == 8063 :
 iI1Iii11i ( i1I1ii11i1Iii )
elif OooO0OOo == 8050 :
 OoO00o0 ( )
elif OooO0OOo == 8051 :
 ooo0oOOO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 8052 :
 oOOOiI1iIIII1 ( i1I1ii11i1Iii )
elif OooO0OOo == 8085 :
 I1IiiiI1I1Iii1Iiii ( )
elif OooO0OOo == 8086 :
 oO000o0OO0OO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 8087 :
 iI1iii1iI1 ( i1I1ii11i1Iii )
elif OooO0OOo == 8088 :
 ooO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif OooO0OOo == 9000 :
 OoooO0o ( )
elif OooO0OOo == 1111 :
 o0OoOoOo0O ( )
elif OooO0OOo == 9001 :
 IIii1i ( )
elif OooO0OOo == 9002 :
 OO000OOOo0Oo ( )
elif OooO0OOo == 9003 :
 II1iOOoOooO0o ( )
elif OooO0OOo == 9004 :
 World1 ( )
elif OooO0OOo == 9005 :
 World2 ( i1I1ii11i1Iii )
elif OooO0OOo == 9006 :
 World3 ( i1I1ii11i1Iii )
elif OooO0OOo == 9007 :
 i11ii ( )
elif OooO0OOo == 9008 :
 IiI111I ( i1I1ii11i1Iii )
elif OooO0OOo == 9009 :
 oo0oO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 9010 :
 Iiii11 ( )
elif OooO0OOo == 9011 :
 o00000O ( i1I1ii11i1Iii )
elif OooO0OOo == 50 :
 II1i ( i1I1ii11i1Iii )
elif OooO0OOo == 9020 :
 champlist ( )
elif OooO0OOo == 9021 :
 OOoOo0O0 ( )
elif OooO0OOo == 9022 :
 I1o0 ( )
elif OooO0OOo == 9023 :
 I1IiiiiI1i1I ( )
elif OooO0OOo == 9024 :
 iiiI1i ( i1I1ii11i1Iii )
elif OooO0OOo == 9030 :
 Oo0oO ( i1I1ii11i1Iii )
elif OooO0OOo == 9031 :
 I11IiIi1iI1ii ( i1I1ii11i1Iii )
elif OooO0OOo == 9032 :
 O0oOo0o0OOoO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 9033 :
 i1I1IIIiii1 ( i1I1ii11i1Iii )
elif OooO0OOo == 9034 :
 o0oooOO00 ( )
elif OooO0OOo == 7085 :
 o0oOOO ( i1I1ii11i1Iii )
elif OooO0OOo == 7086 :
 iIii1iIiII1i1 ( i1I1ii11i1Iii )
elif OooO0OOo == 7087 :
 iIIi1II1 ( ii1Oo0000oOo )
elif OooO0OOo == 9666 :
 oO0O000oOo ( i1I1ii11i1Iii )
elif OooO0OOo == 10100 : oOoo0OO0 ( )
elif OooO0OOo == 10105 : oo0O00ooo0o ( i1I1ii11i1Iii )
elif OooO0OOo == 10106 : iIiII1 ( i1I1ii11i1Iii )
elif OooO0OOo == 10104 : O0o0O0O0O ( i1I1ii11i1Iii )
elif OooO0OOo == 10107 : IiII1 ( )
elif OooO0OOo == 10103 : i111 ( i1I1ii11i1Iii )
elif OooO0OOo == 10108 : II1i1i1I1iII ( i1I1ii11i1Iii )
elif OooO0OOo == 10107 : IiII1 ( )
elif OooO0OOo == 10000 : Origin_Menu ( )
elif OooO0OOo == 10001 : oO00 ( )
elif OooO0OOo == 10002 : I1I1i ( )
elif OooO0OOo == 10003 : ooo0O0o0OoOO ( )
elif OooO0OOo == 10004 : o0oOOOO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10005 : oOooo00O ( )
elif OooO0OOo == 10006 : I1III1iIi ( i1I1ii11i1Iii )
elif OooO0OOo == 10007 : Ooi111i1iIi1 ( i1I1ii11i1Iii , iiiI1I1iIIIi1 )
elif OooO0OOo == 10008 : I1iII1IIi1IiI ( )
elif OooO0OOo == 10009 : IiiI1I ( )
elif OooO0OOo == 10010 : Ii1 ( i1I1ii11i1Iii )
elif OooO0OOo == 10011 : oOOo0ooO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10012 : I1I1I1IIi1III ( i1I1ii11i1Iii )
elif OooO0OOo == 10109 : oO0IIi11IiiiI11i ( i1I1ii11i1Iii )
elif OooO0OOo == 10013 : Oo0000OOO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10014 : I1iIIIiI ( )
elif OooO0OOo == 10015 : iIiiii1 ( )
elif OooO0OOo == 10016 : iIi1i1iIi1Ii1 ( i1I1ii11i1Iii )
elif OooO0OOo == 10017 : oOO0o00o0Oo0O ( )
elif OooO0OOo == 10018 : Iiii1Ii ( )
elif OooO0OOo == 10019 : I1IIII ( )
elif OooO0OOo == 10020 : I1oo ( )
elif OooO0OOo == 10021 : oOoO0Oo0 ( )
elif OooO0OOo == 10022 : ooooo0o0oo0Ooo ( i1I1ii11i1Iii )
elif OooO0OOo == 10023 : ooO00Oo ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif OooO0OOo == 10024 : I1I1IIiiii1ii ( i1I1ii11i1Iii )
elif OooO0OOo == 10025 : O00O ( )
elif OooO0OOo == 10026 : i111I11i1I ( )
elif OooO0OOo == 10027 : I11I1ii1i ( )
elif OooO0OOo == 10028 : O0OOo ( )
elif OooO0OOo == 10029 : oO0ooooo0O00 ( )
elif OooO0OOo == 423 : OooOo ( i1I1ii11i1Iii )
elif OooO0OOo == 426 : iiiIi1II1III ( i1I1ii11i1Iii )
elif OooO0OOo == 10030 : Izle_Films ( )
elif OooO0OOo == 10031 : Latest_Izle_Movies ( )
elif OooO0OOo == 10032 : Izle_Genres ( )
elif OooO0OOo == 10033 : Izle_Pop_Movies ( )
elif OooO0OOo == 10034 : Izle_Boxsets ( )
elif OooO0OOo == 10035 : Izle_Search ( )
elif OooO0OOo == 10036 : Izle_Genres_Movie ( i1I1ii11i1Iii )
elif OooO0OOo == 10037 : Izle_Boxset_single ( i1I1ii11i1Iii )
elif OooO0OOo == 10038 : Izle_IFRAME ( )
elif OooO0OOo == 10039 : Izle_Boxsets_Next ( i1I1ii11i1Iii )
elif OooO0OOo == 10040 : OOOOoo00OO0O0Ooo0 ( )
elif OooO0OOo == 10041 : I1ii1i1iiii ( i1I1ii11i1Iii )
elif OooO0OOo == 10042 : OoOoooo0O ( i1I1ii11i1Iii )
elif OooO0OOo == 10043 : iiIIi1 ( )
elif OooO0OOo == 10044 : O00oO000Oo0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10045 : iiI1 ( oO00oooOOoOo0 )
elif OooO0OOo == 10046 : o0OOoOo0oo ( i1I1ii11i1Iii )
elif OooO0OOo == 10047 : ii1i11ii ( i1I1ii11i1Iii )
elif OooO0OOo == 10048 : OOoI111 ( i1I1ii11i1Iii )
elif OooO0OOo == 10049 : i1Ii1i1 ( i1I1ii11i1Iii )
elif OooO0OOo == 10050 : IiIi ( )
elif OooO0OOo == 10051 : OO0Oo00 ( )
elif OooO0OOo == 10052 : ooOo ( )
elif OooO0OOo == 10053 : Addon ( i1I1ii11i1Iii )
elif OooO0OOo == 10054 : o0oOOoOo00o ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif OooO0OOo == 10055 :
 i1I111Ii ( "addFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0oI1ii1Ii1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , iiiI1I1iIIIi1 , oOo0O , iI1IIIiIII11 )
elif OooO0OOo == 10056 :
 i1I111Ii ( "rmFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 II1IIi1iII1i ( oO00oooOOoOo0 )
elif OooO0OOo == 10057 :
 i1I111Ii ( "getFavorites" )
 oOOOOOo ( )
elif OooO0OOo == 10058 : i1I1i111Ii ( )
elif OooO0OOo == 10059 : Donators_Guide ( )
elif OooO0OOo == 10060 : ii1Ii1IiIIi ( )
elif OooO0OOo == 10061 : OOo00 ( )
elif OooO0OOo == 10062 : Ii111 ( oO00oooOOoOo0 , i1I1ii11i1Iii , ii1Oo0000oOo )
elif OooO0OOo == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif OooO0OOo == 10064 : OOOIiiiii1iI ( )
elif OooO0OOo == 10065 : OO00OO0O0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10066 : o0O0oo0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10068 : OO00 ( i1I1ii11i1Iii )
elif OooO0OOo == 10069 : i1iiIiI1Ii1i ( i1I1ii11i1Iii )
elif OooO0OOo == 10070 : IIIIIo0ooOoO000oO ( i1I1ii11i1Iii )
elif OooO0OOo == 10071 : Genie_Watch ( )
elif OooO0OOo == 10072 : I111i1i1111 ( )
elif OooO0OOo == 10073 : III1ii1I ( i1I1ii11i1Iii )
elif OooO0OOo == 10074 : oOoOoOoo0 ( i1I1ii11i1Iii )
elif OooO0OOo == 10075 : o0oOO ( iiiI1I1iIIIi1 , oO00oooOOoOo0 , i1I1ii11i1Iii )
elif OooO0OOo == 10076 : Ii1I11ii1i ( i1I1ii11i1Iii )
elif OooO0OOo == 10077 : ii1I1IiiI1ii1i ( i1I1ii11i1Iii )
elif OooO0OOo == 10078 : I1ii11 ( )
elif OooO0OOo == 10079 : Genie_Watch_Tv_Shows ( )
elif OooO0OOo == 10080 : Genie_Watch_Tv_Genre ( i1I1ii11i1Iii )
elif OooO0OOo == 10081 : Genie_Watch_TV_PlayRun ( i1I1ii11i1Iii )
elif OooO0OOo == 10082 : Genie_Watch_TV_Episodes ( i1I1ii11i1Iii , iiiI1I1iIIIi1 )
elif OooO0OOo == 10083 : Genie_Watch_Tv_Recent ( i1I1ii11i1Iii )
elif OooO0OOo == 10084 : o0ooooO0o0O ( )
elif OooO0OOo == 10085 : IiI111111IIII ( )
elif OooO0OOo == 10086 : ooOOO00Ooo ( )
elif OooO0OOo == 20000 : ii1ii1I1IIi1 ( )
elif OooO0OOo == 20001 : Ii1i1 ( )
elif OooO0OOo == 20002 : oo0oo ( i1I1ii11i1Iii )
elif OooO0OOo == 20003 : oooo ( i1I1ii11i1Iii )
elif OooO0OOo == 20004 : iii1IIiI ( i1I1ii11i1Iii )
elif OooO0OOo == 21004 : O00oo ( )
elif OooO0OOo == 21005 : OoOo0oO0o ( i1I1ii11i1Iii )
elif OooO0OOo == 21006 : i111i ( i1I1ii11i1Iii )
elif OooO0OOo == 21007 : Oo0oOo0ooOOOo ( i1I1ii11i1Iii )
elif OooO0OOo == 30000 : I1I11ii ( )
elif OooO0OOo == 30001 : iiii ( )
elif OooO0OOo == 10012 : Resolve ( i1I1ii11i1Iii )
elif OooO0OOo == 30003 : iiI1Ii1I ( )
elif OooO0OOo == 30004 : oOo00Ooo0o0 ( i1I1ii11i1Iii )
elif OooO0OOo == 30005 : oOO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 30006 : OOoO0oo0O ( )
elif OooO0OOo == 30007 : II1ii1ii11I1 ( )
elif OooO0OOo == 30008 : iIiI1iI1i1I ( i1I1ii11i1Iii )
elif OooO0OOo == 30009 : iIii1iII1Ii ( i1I1ii11i1Iii )
elif OooO0OOo == 30010 : O00OOo000Oo0 ( i1I1ii11i1Iii )
elif OooO0OOo == 30011 : II1 ( )
elif OooO0OOo == 30012 : OOOo ( )
elif OooO0OOo == 30013 : I1I11IiiI ( )
elif OooO0OOo == 30014 : I1iIiiiI1 ( )
elif OooO0OOo == 30015 : oO0O0Ooo ( i1I1ii11i1Iii , iiiI1I1iIIIi1 , oOo0O )
elif OooO0OOo == 30016 : oOoOo ( i1I1ii11i1Iii )
elif OooO0OOo == 30019 : Oo ( i1I1ii11i1Iii )
elif OooO0OOo == 30017 : OooOOOO0O0 ( i1I1ii11i1Iii )
elif OooO0OOo == 30018 : ooOOOoOoOOO0 ( i1I1ii11i1Iii )
elif OooO0OOo == 30030 : oOO0OOOOOo0Oo ( )
elif OooO0OOo == 30031 : iIi ( )
elif OooO0OOo == 30032 : Ii1Ii1Ii1IIIi ( )
elif OooO0OOo == 30033 : OO ( )
elif OooO0OOo == 30034 : O000O0 ( )
elif OooO0OOo == 30035 : II1i11i1iIi11 ( i1I1ii11i1Iii )
elif OooO0OOo == 30036 : oo0O0oO0O0O ( i1I1ii11i1Iii )
elif OooO0OOo == 30037 : oOo0OI11i ( i1I1ii11i1Iii )
elif OooO0OOo == 30038 : I1ii1111Ii ( )
elif OooO0OOo == 30039 : o0O0ooOOoO ( )
elif OooO0OOo == 50000 : IIiiIiII1Ii ( )
elif OooO0OOo == 50001 : o0o000 ( )
elif OooO0OOo == 50002 : iIiI1i111ii ( i1I1ii11i1Iii )
elif OooO0OOo == 50003 : i1i1I11i1I ( ii1Oo0000oOo )
elif OooO0OOo == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OooO0OOo == 60001 : IIIii ( )
elif OooO0OOo == 60002 : O0oOo00o0 ( oO00oooOOoOo0 )
elif OooO0OOo == 60003 : o00o ( oO00oooOOoOo0 )
elif OooO0OOo == 50004 : OO0ooOOO0OOO ( )
elif OooO0OOo == 50005 : speedtest . runtest ( i1I1ii11i1Iii )
elif OooO0OOo == 70001 : iIIiI1iiI ( )
elif OooO0OOo == 70002 : O0Oo00OO00Ooo ( i1I1ii11i1Iii )
elif OooO0OOo == 70003 : OO0O00OoOOOo ( i1I1ii11i1Iii )
elif OooO0OOo == 70004 : Oo0 ( i1I1ii11i1Iii )
elif OooO0OOo == 70005 : o0OOOOO0O ( i1I1ii11i1Iii )
elif OooO0OOo == 70006 : I1I1IiIi1 ( )
elif OooO0OOo == 50006 : O0O0Oooo0o ( i1 , i1111 )
elif OooO0OOo == 80000 : OoOOOO ( )
elif OooO0OOo == 80001 : resolvefilmon ( i1I1ii11i1Iii )
elif OooO0OOo == 80002 : o0O0Oo0Ooo0 ( )
elif OooO0OOo == 80003 : iIIIiiiI11I ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif OooO0OOo == 80004 : Iiii1 ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif OooO0OOo == 80005 : o000oo ( )
elif OooO0OOo == 80006 : o00o0 ( i1I1ii11i1Iii )
elif OooO0OOo == 80007 : OOOOoO00o0O ( i1I1ii11i1Iii )
elif OooO0OOo == 80008 : II11IiiIII ( )
if 80 - 80: O00o0O00 * oO0o + iI1ii11iIi1i
if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
