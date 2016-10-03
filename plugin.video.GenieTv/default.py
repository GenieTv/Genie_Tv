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
IiiIII111iI = "3.1.7"
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
  if 23 - 23: Ii
  if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + I11O0O0oOO00O00o * iI11I1II1I1I
 I1IIII1i ( '[COLOR' + iiI1IiI + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , OO0o , '' )
 if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 1023 , III1iII1I1ii + 'ScoobyStreams.png' , OO0o , '' )
 if oo00 . getSetting ( 'HeroVision' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , '' , 1017 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'ITVStreams.png' , OO0o , '' )
 if 81 - 81: ooOOOoO % ooOoO0O00 . iI11I1II1I1I
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 4 - 4: Ii % oO0o % ooOoO0O00 / ooOOOoO
def I11iI ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , OO0o , '' )
def ooOoo ( url ) :
 I1III1111iIi = I1i111I ( url )
 url = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( I1III1111iIi )
 for OooOo0oo0O0o00O , I1i11 in IIi1I11I1II :
  if '[DIR]' in OooOo0oo0O0o00O :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + I1i11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + I1i11 , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in I1i11 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + I1i11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + I1i11 , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in I1i11 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + I1i11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + I1i11 , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 47 - 47: I1ii11iIi11i * Ii1I + iI11I1II1I1I / ii1ii11IIIiiI / oO0o - ii
def iII1i11IIi1i ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HEROVISION SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'Herovision.png' , OO0o , '' )
 if 73 - 73: I11i * o0o00Oo0O - Ii
def O0O0o0oOOO ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'SearchCartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'WCO' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1IiI1 ) , 21004 , III1iII1I1ii + 'watchcartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'Cartoons' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 10001 , III1iII1I1ii + 'Cartoons.png' , OO0o , '' )
 if oo00 . getSetting ( 'Anime' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , III1iII1I1ii + 'anime.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def OOoOoOo ( ) :
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
 if 98 - 98: Ii1IIIi1
 if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
 if 38 - 38: O0OOOoOoo0 - O00o0O00 / Ii1IIIi1
def i1Ii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi1I11I1II = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIIi1I1IIii1II )
 for oo0OOo in IIi1I11I1II :
  oo0OOo = ( str ( oo0OOo ) )
  if os . path . exists ( xbmc . translatePath ( oo0OOo ) ) :
   OoOOoooOO0O = ( oo0OOo ) . replace ( 'special://home/addons/' , '' )
   O0O0Oooo0o ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OoOOoooOO0O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   ooo00Ooo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if ooo00Ooo == 0 :
    Oo0o0O00 ( oo0OOo )
    ii1 ( )
   elif ooo00Ooo == 1 :
    I1i11OO ( oo0OOo )
  else :
   pass
   if 84 - 84: O0OOOoOoo0 % iI1ii11iIi1i + Ii
def I1i11OO ( addon ) :
 OoOOoooOO0O = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 28 - 28: I1ii11iIi11i + oO0o * O00o0O00 % oO0oo0o . I11O0O0oOO00O00o % o0o00Oo0O
def Oo0o0O00 ( addon ) :
 iI111I11I1I1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1iiiiIii = os . path . join ( iIi1ii1I1 , 'default.py' )
 iIiIiIiI = open ( I1iiiiIii , "w+" )
 if 30 - 30: ii1ii11IIIiiI . O0OOOoOoo0 * Ii1I
 iIiIiIiI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 iIiIiIiI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 iIiIiIiI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 17 - 17: oOo0O0Ooo . o0o00Oo0O + oO0o
 if 43 - 43: IIiIiII11i . oO0oo0o / Ii1I
 if 20 - 20: oOo0O0Ooo
 if 95 - 95: Ii1IIIi1 - oOo0O0Ooo
def I1ii1ii11i1I ( ) :
 IiIi1I1 ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://www.join4films.com/' )
 IIi1I11I1II = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 80006 , III1iII1I1ii + 'Desi.png' )
def o0OoOO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( IIIi1I1IIii1II )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , url , 80007 , O0O0Oo00 )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def oOoO00o ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  url = ( url ) . replace ( ' ' , '%20' )
  oO00O0 ( url )
def IIi1IIIi ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOO0OOO = 'http://www.join4films.com/?s=' + ( O00Ooo ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1i1ii = OOOO0OOO . lower ( )
 o0OoOO ( i1i1ii )
 if 46 - 46: OOooOOo + oO0o
 if 70 - 70: Ii1IIIi1 / iI11I1II1I1I
 if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
 if 96 - 96: ii + oO0oo0o
 if 44 - 44: oO0oo0o
 if 20 - 20: I11O0O0oOO00O00o + iI1ii11iIi1i / o0o00Oo0O % iI11I1II1I1I
 if 88 - 88: OOooOOo / IIiIiII11i
 if 87 - 87: Ii1I - Ii1I - Ii1IIIi1 + oO0oo0o
 if 82 - 82: oO0oo0o / iI11I1II1I1I . oOo0O0Ooo . O00o0O00 / I11i
 if 42 - 42: I1ii11iIi11i
 if 19 - 19: oO0oo0o % Ii1I * iI11I1II1I1I + oOo0O0Ooo
 if 46 - 46: I1ii11iIi11i
 if 1 - 1: Ii1IIIi1
 if 97 - 97: O00o0O00 + Ii1IIIi1 + o0o00Oo0O + Ii
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . Ii1IIIi1 % Ii1IIIi1 + Ii
 if 72 - 72: iI11I1II1I1I * iI1ii11iIi1i % O0OOOoOoo0 / oO0o
def I11i1II ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 I1IIII1i ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
 if 72 - 72: iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
def ooo000o000 ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOO0OOO = 'http://imoviemax.se/?s=' + ( O00Ooo ) . replace ( ' ' , '+' )
 i1i1ii = OOOO0OOO . lower ( )
 O0o ( i1i1ii )
def O0OOoOOO0oO ( url ) :
 I1ii11 = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , oOoOoOoo0 in IIi1I11I1II :
  if oO00oooOOoOo0 in I1ii11 :
   pass
  else :
   I1IIII1i ( oO00oooOOoOo0 + ' - ' + oOoOoOoo0 + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
   I1ii11 . append ( oO00oooOOoOo0 )
   if 34 - 34: OOooOOo - O00o0O00 + o0o00Oo0O . iI1ii11iIi1i
def iIi1i1iIi1iI ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , iiIi1iI1iIii in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + ' - Views:' + iiIi1iI1iIii , url , 10075 , III1iII1I1ii + 'genievision.png' , OO0o , '' )
  if 68 - 68: O00o0O00
  if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % ooOOOoO / iI1ii11iIi1i . iI1ii11iIi1i
def O0o ( url ) :
 IIi = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIIi1I1IIii1II )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10075 , O0O0Oo00 , O0O0Oo00 , '' )
  IIi . append ( oO00oooOOoOo0 )
  if 66 - 66: oO0oo0o % oO0o . O00o0O00
def o0OIiiiI ( img , name , url ) :
 img = img
 name = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( IIIi1I1IIii1II )
 for O00OoOO0oo0 , url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oOO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oOO
  O0o0OO0000ooo = ( O00OoOO0oo0 ) . replace ( 'play-' , 'Server ' )
  iIiIIi1 ( O0o0OO0000ooo , oOO , 10076 , img , img , '' )
  if 4 - 4: iI1ii11iIi1i
def OO0oOOoo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( IIIi1I1IIii1II )
 for I1i11 in IIi1I11I1II :
  if '=m' in I1i11 :
   oOOO00o000o ( I1i11 )
  elif 'php' in I1i11 :
   OO0oOOoo ( url )
  else :
   IIIi1I1IIii1II = O0i1II1Iiii1I11 ( I1i11 )
   IIi1I11I1II = re . compile ( 'content="([^"]*)">' ) . findall ( IIIi1I1IIii1II )
   for iIi11i1 in IIi1I11I1II :
    oOOO00o000o ( I1i11 )
    if 71 - 71: O0OOOoOoo0
    if 53 - 53: ii % iI1ii11iIi1i . ooOOOoO / Ii % Ii1IIIi1
    if 28 - 28: I11O0O0oOO00O00o
def oOOOOoo ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OOo0 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii11I1 , oO0oo in OOo0 :
  print 'there ><><><><><><><><><><><><'
  ii11I1 = ii11I1
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oO0oo ) )
  for oO00oooOOoOo0 , Ii111iIi1iIi in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + ii11I1 + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + Ii111iIi1iIi + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
 IIIIIo0ooOoO000oO = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for ii11I1 , OOo in IIIIIo0ooOoO000oO :
  print 'there ><><><><><><><><><><><><'
  ii11I1 = ii11I1
  IIi1I11I1II = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOo ) )
  for oO00oooOOoOo0 , Ii111iIi1iIi in IIi1I11I1II :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + ii11I1 + '[/COLOR] - ' + oO00oooOOoOo0 + ' - [COLOR' + iiI1IiI + ']' + Ii111iIi1iIi + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , OO0o , '' )
   if 50 - 50: O0OOOoOoo0
   if 72 - 72: ii1ii11IIIiiI
   if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . Ii1IIIi1
def I1iii11 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIIIIo0ooOoO000oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for IIIIIo0ooOoO000oO in IIIIIo0ooOoO000oO :
  oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
  for oO00oooOOoOo0 in oO00oooOOoOo0 :
   oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
  for ooo0O in ooo0O :
   ooo0O = 'http:' + ooo0O
  iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , '' , '' )
  if 16 - 16: OOooOOo
  if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . O00o0O00
  if 83 - 83: Ii1IIIi1 . o0o00Oo0O / I1ii11iIi11i / O00o0O00 - IIiIiII11i
  if 100 - 100: oO0o
def II1i ( url ) :
 if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % oO0oo0o - IIiIiII11i - Ii1IIIi1
 iIi11iiIiI1I = [ ]
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for I1i11 , O0O0Oo00 , oO00oooOOoOo0 , Iiii in IIi1I11I1II :
  oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = O0i1II1Iiii1I11 ( I1i11 )
  OooOoooOo = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for oooOOoooo , O0000OOO0 in OooOoooOo :
   ooo0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( O0000OOO0 ) )
   for oO000oOo00o0o in ooo0 :
    if oO00oooOOoOo0 in iIi11iiIiI1I :
     pass
    else :
     iIiIIi1 ( oO00oooOOoOo0 , oooOOoooo , 8043 , O0O0Oo00 , O0O0Oo00 , oO000oOo00o0o )
     I1I1II1I11 ( 'movies' , 'INFO' )
     iIi11iiIiI1I . append ( oO00oooOOoOo0 )
     if 85 - 85: Ii1IIIi1 + ii * Ii1IIIi1 - ii1ii11IIIiiI % Ii
     if 71 - 71: Ii1I - O0OOOoOoo0 / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def ooo000ooO0000 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , oOoooo000Oo00 , oO000oOo00o0o , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 10065 , oOoooo000Oo00 , oOo0O , oO000oOo00o0o )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 93 - 93: Ii1I / oOo0O0Ooo / iI11I1II1I1I % ii1ii11IIIiiI % ii1ii11IIIiiI
def IiI11iI1i1i1i ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOO0OOO = 'https://www.youtube.com/results?search_query=' + ( O00Ooo ) . replace ( ' ' , '+' )
 i1i1ii = OOOO0OOO . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1i1ii )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in next :
  i1I1ii11i1Iii = 'https://www.youtube.com' + i1I1ii11i1Iii
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , i1I1ii11i1Iii , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 , oO0Ooooooo , O0000OOO0 in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  ooo0O = 'http:' + ( O0O0Oo00 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0O
  i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
  iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , O0000OOO0 )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 , oO0Ooooooo in IIi1I11I1II :
   print 'im doing it'
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   ooo0O = 'http:' + ( O0O0Oo00 ) . replace ( 'https:' , '' )
   i1I1ii11i1Iii = 'http://www.youtube.com' + i1I1ii11i1Iii
   if '&' in i1I1ii11i1Iii :
    print ' i got here'
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    IIIIIo0ooOoO000oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for IIIIIo0ooOoO000oO in IIIIIo0ooOoO000oO :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     i1I1ii11i1Iii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for i1I1ii11i1Iii in i1I1ii11i1Iii :
      i1I1ii11i1Iii = 'https://www.youtube.com/w' + i1I1ii11i1Iii
     ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for ooo0O in ooo0O :
      ooo0O = 'http:' + ooo0O
     iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in i1I1ii11i1Iii or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in i1I1ii11i1Iii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i1I1ii11i1Iii
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i1I1ii11i1Iii )
    I1IIIiI1I1ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 in I1IIIiI1I1ii1 :
     if 'outube' in i1I1ii11i1Iii or 'list' in i1I1ii11i1Iii :
      pass
     elif 'atch' in i1I1ii11i1Iii :
      i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0O0Oo00 , 'http:' + O0O0Oo00 , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , '' )
    if 30 - 30: o0o00Oo0O * ii
def I1iIIIi1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIIi1I1IIii1II )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + iiI1IiI + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 for O0O0Oo00 , url , oO00oooOOoOo0 , oO0Ooooooo , O0000OOO0 in IIi1I11I1II :
  IIiiiiiiIi1I1 . append ( oO00oooOOoOo0 )
  I1I1II1I11 ( 'tvshows' , 'INFO' )
  ooo0O = 'http:' + ( O0O0Oo00 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0O
  url = 'http://www.youtube.com' + url
  iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , O0000OOO0 )
 else :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0O0Oo00 , url , oO00oooOOoOo0 , oO0Ooooooo in IIi1I11I1II :
   I1I1II1I11 ( 'tvshows' , 'INFO' )
   ooo0O = 'http:' + ( O0O0Oo00 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    IIIIIo0ooOoO000oO = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for IIIIIo0ooOoO000oO in IIIIIo0ooOoO000oO :
     oO00oooOOoOo0 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for oO00oooOOoOo0 in oO00oooOOoOo0 :
      oO00oooOOoOo0 = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
     for ooo0O in ooo0O :
      ooo0O = 'http:' + ooo0O
     iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , OO0o , '' )
   elif oO00oooOOoOo0 in IIiiiiiiIi1I1 :
    pass
   elif 'user' in url or 'elete' in oO00oooOOoOo0 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
    I1IIIiI1I1ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
    for O0O0Oo00 , url , oO00oooOOoOo0 in I1IIIiI1I1ii1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + O0O0Oo00 , 'http:' + O0O0Oo00 , '' )
     else :
      pass
   else :
    iIiIIi1 ( '[COLORred]' + oO0Ooooooo + '[/COLOR]' + '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , '' )
    if 17 - 17: iI11I1II1I1I . ii / I11O0O0oOO00O00o % IIiIiII11i % ooOoO0O00 / Ii
    if 58 - 58: I1ii11iIi11i . IIiIiII11i + oO0oo0o - Ii / IIiIiII11i / o0o00Oo0O
def i1I1i111Ii ( ) :
 if OooO0 == 'insert_password' :
  iI111I11I1I1 . ok ( '[COLOR' + iiI1IiI + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiI1IiI + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  oOOoOo = open ( O000oo0O )
  IIi1I11I1II = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( oOOoOo ) )
  for ooOooo0 , oO0OO0 in IIi1I11I1II :
   if ooOooo0 == 'needs replacing' or oO0OO0 == 'needs replacing' :
    o0O0Oo00 ( )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv PRIVATE LIST[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , III1iII1I1ii + 'PrivateList.png' , OO0o , '' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']G-Tv ULTIMATE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'UltimateList.png' , OO0o , '' )
  if 51 - 51: O00o0O00 % iI11I1II1I1I - ii % O0OOOoOoo0 * iI11I1II1I1I % oO0o
def oO0o00oOOooO0 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + I1IIIii + ")" )
 o0O0Oo00 ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 79 - 79: oO0o - iI11I1II1I1I + iI1ii11iIi1i - ii1ii11IIIiiI
def OoOiIIiii ( ) :
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
 if 61 - 61: ooOOOoO . ooOoO0O00 / ii1ii11IIIiiI % Ii * Ii1IIIi1
def i1i1i1I ( name ) :
 oOoo000 = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , O0O0Oo00 , OooOo00o , i1I1ii11i1Iii in IIi1I11I1II :
  if oOoo000 == 'Full List' :
   i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
   iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , O0O0Oo00 , O0O0Oo00 , '' )
  else :
   oOoo000 = ( oOoo000 ) . replace ( 'World' , 'القنوات العربية' )
   if oOoo000 in OooOo00o :
    i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
    print i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , O0O0Oo00 , O0O0Oo00 , '' )
   else :
    pass
    if 20 - 20: ooOoO0O00 * ii1ii11IIIiiI + IIiIiII11i % I11i % oO0oo0o
def iIi1II ( name ) :
 oOoo000 = name
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( IIIi1I1IIii1II )
 for name , O0O0Oo00 , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii ) . replace ( '.ts' , '.m3u8' )
  iIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i1I1ii11i1Iii ) . strip ( ) , 10012 , O0O0Oo00 , O0O0Oo00 , '' )
 else :
  iIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 17 - 17: O00o0O00 % I1ii11iIi11i / Ii1I . ooOOOoO * O00o0O00 - IIiIiII11i
  if 41 - 41: iI1ii11iIi1i
  if 77 - 77: ii1ii11IIIiiI
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % oO0oo0o * oO0o
  if 38 - 38: OOooOOo / Ii1IIIi1 % I1ii11iIi11i
  if 11 - 11: Ii1IIIi1 - oO0oo0o + IIiIiII11i - iI11I1II1I1I
  if 7 - 7: ooOOOoO - I11O0O0oOO00O00o / IIiIiII11i * iI1ii11iIi1i . Ii1IIIi1 * Ii1IIIi1
  if 61 - 61: I11O0O0oOO00O00o % O0OOOoOoo0 - oO0o / I1ii11iIi11i
  if 4 - 4: ii - ooOoO0O00 % iI1ii11iIi1i - O00o0O00 * I11i
  if 85 - 85: ii * iI11I1II1I1I . Ii1IIIi1 / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: iI1ii11iIi1i / IIiIiII11i / ooOOOoO / ooOOOoO + Ii1I
  if 95 - 95: ooOOOoO
def Ooo0oo ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , OO0o , 'Back Up Your Full System' )
 if os . path . exists ( o00OO00OoO ) :
  I1IIII1i ( 'Backup Genie Favourites' , i1I1ii11i1Iii , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , OO0o , 'Back Up Your favourites' )
 if os . path . exists ( oO0Oo ) :
  I1IIII1i ( 'Backup Ivue Config' , oO0Oo , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , OO0o , 'Back Up Your master.db' )
 if os . path . exists ( oOOoo0Oo ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oOOoo0Oo , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , OO0o , 'Back Up Your favourites.xml' )
  if 41 - 41: OOooOOo * I11O0O0oOO00O00o / OOooOOo % oO0oo0o
  if 18 - 18: IIiIiII11i . ii % OOooOOo % iI1ii11iIi1i
  if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
zip = oo00 . getSetting ( 'zip' )
ii1Ii1IiIIi = xbmc . translatePath ( os . path . join ( zip ) )
def o0OO0 ( ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 37 - 37: ooOOOoO . I11i / O0OOOoOoo0 . O00o0O00
  if 66 - 66: O00o0O00
  if 42 - 42: OOooOOo - O00o0O00 . oO0oo0o
def IiIi1i1ii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = o00OO00OoO
  elif 'Ivue' in name :
   url = oO0Oo
  elif 'Kodi' in name :
   url = oOOoo0Oo
  o0OO0 ( )
  iiIi = open ( url ) . read ( )
  oOIi111 = os . path . join ( ii1Ii1IiIIi , description . split ( 'Your ' ) [ 1 ] )
  o0Oo00 = open ( oOIi111 , mode = 'w' )
  o0Oo00 . write ( iiIi )
  o0Oo00 . close ( )
 else :
  if 'guisettings.xml' in description :
   oO0i1iI = open ( os . path . join ( ii1Ii1IiIIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iioo0o0OoOOO = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi1I11I1II = re . compile ( iioo0o0OoOOO ) . findall ( oO0i1iI )
   for type , ooO0oO00O0o , ooOO00oOOo000 in IIi1I11I1II :
    ooOO00oOOo000 = ooOO00oOOo000 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , ooO0oO00O0o , ooOO00oOOo000 ) )
  else :
   oOIi111 = os . path . join ( url )
   iiIi = open ( os . path . join ( ii1Ii1IiIIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0Oo00 = open ( oOIi111 , mode = 'w' )
   o0Oo00 . write ( iiIi )
   o0Oo00 . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 14 - 14: oO0o . IIiIiII11i . I11O0O0oOO00O00o / iI1ii11iIi1i % Ii1I - O0OOOoOoo0
 if 67 - 67: I11O0O0oOO00O00o - O00o0O00 . ooOoO0O00
 if 35 - 35: Ii1IIIi1 + O0OOOoOoo0 - oO0oo0o . Ii1IIIi1 . ooOOOoO
 if 87 - 87: OOooOOo
def IioO0O ( ) :
 oOOiiiIIiIi = 1
 o0OO0 ( )
 OooOOO = xbmc . translatePath ( os . path . join ( ii1Ii1IiIIi , 'Build Backup' , 'Full Backup' , '' ) )
 Ii1iI11iI1 = xbmc . translatePath ( os . path . join ( ii1Ii1IiIIi , 'Build Backup' , 'my_full_backup.zip' ) )
 i11I1II = xbmc . translatePath ( os . path . join ( ii1Ii1IiIIi , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( OooOOO ) :
  os . makedirs ( OooOOO )
 OO0 = iI111I11I1I1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OO0 ) : return False , 0
 OOO0oOOo00O = OO0
 OO0oIII111i11IiI = xbmc . translatePath ( os . path . join ( OooOOO , OOO0oOOo00O + '.zip' ) )
 O0000 = [ 'plugin.video.GenieTv' ]
 ooO00O0O0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iII1I1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 o0Ooo0o0ooo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oo0o0000Oo0 = "Creating full backup of existing build"
 o0O00oOoo = "Creating Community Build"
 O000O0OO00oo = "Archiving..."
 oOOO = ""
 ooo0oooo0 = "Please Wait"
 OOO0ooo ( I11 , OO0oIII111i11IiI , o0O00oOoo , O000O0OO00oo , oOOO , ooo0oooo0 , iII1I1 , o0Ooo0o0ooo0 )
 time . sleep ( 1 )
 IIiiii = xbmc . translatePath ( os . path . join ( OooOOO , OOO0oOOo00O + '_guisettings.zip' ) )
 iI111i1I1II = zipfile . ZipFile ( IIiiii , mode = 'w' )
 try :
  iI111i1I1II . write ( xbmc . translatePath ( os . path . join ( I11 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iI111i1I1II . close ( )
 if oOOiiiIIiIi == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + Ii1iI11iI1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OO0oIII111i11IiI + '[/COLOR]' )
  if 96 - 96: ii1ii11IIIiiI / I1ii11iIi11i * IIiIiII11i - Ii1IIIi1 * I1ii11iIi11i
def OOO0ooo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0Ii1Iii111IiI1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O00oOooo0 = len ( sourcefile )
 OoOO = [ ]
 iIII1I1i1i = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for o0OIIiI1I1 , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( sourcefile ) :
  for file in IIIIIii1ii11 :
   iIII1I1i1i . append ( file )
 OOOooo0OooOoO = len ( iIII1I1i1i )
 for o0OIIiI1I1 , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( sourcefile ) :
  I11I1IIiiII1 [ : ] = [ oOoOOOo for oOoOOOo in I11I1IIiiII1 if oOoOOOo not in exclude_dirs ]
  IIIIIii1ii11 [ : ] = [ o0Oo00 for o0Oo00 in IIIIIii1ii11 if o0Oo00 not in exclude_files ]
  for file in IIIIIii1ii11 :
   OoOO . append ( file )
   ii1I = len ( OoOO ) / float ( OOOooo0OooOoO ) * 100
   o0oOoO00o . update ( int ( ii1I ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0OOoOoO00 = os . path . join ( o0OIIiI1I1 , file )
   if not 'temp' in I11I1IIiiII1 :
    if not 'plugin.program.originwizard' in I11I1IIiiII1 :
     import time
     I1iii = '01/01/1980'
     oOO0OO0O = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0OOoOoO00 ) ) )
     if oOO0OO0O > I1iii :
      o0Ii1Iii111IiI1 . write ( o0OOoOoO00 , o0OOoOoO00 [ O00oOooo0 : ] )
 o0Ii1Iii111IiI1 . close ( )
 o0oOoO00o . close ( )
 if 78 - 78: iI1ii11iIi1i / IIiIiII11i % OOooOOo
 if 52 - 52: O00o0O00 - Ii1IIIi1 * oO0oo0o
def Ii1I11I ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , OO0o , '' )
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
 if 5 - 5: I1ii11iIi11i * OOooOOo
def ii1I11iIiIII1 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'MOVIESv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'TVSHOWSv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON' , OO0o , '' )
 if 52 - 52: I11i * ooOOOoO + OOooOOo
 if 49 - 49: iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 - ii
 if 37 - 37: ooOoO0O00 . I11O0O0oOO00O00o % OOooOOo + ii / Ii1IIIi1
 if 3 - 3: Ii1I
def IIi1II ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , III1iII1I1ii + 'Quicksilver.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , OO0o , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , OO0o , '' )
  if 2 - 2: IIiIiII11i - oO0o . ooOOOoO * Ii1IIIi1 / oO0oo0o
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , OO0o , '' )
 if 80 - 80: O00o0O00 / I11O0O0oOO00O00o / OOooOOo + ooOoO0O00 - I1ii11iIi11i
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 11 - 11: I11i * oO0o
def iIi1IiI ( ) :
 O000OOo00oo ( )
 if 14 - 14: ooOOOoO % oO0oo0o % I1ii11iIi11i - Ii
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , OO0o , '' )
 iIiIIi1 ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , OO0o , '' )
 iIiIIi1 ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , OO0o , 'Force Refresh All Repos' )
 if 53 - 53: iI1ii11iIi1i % I1ii11iIi11i
 iIiIIi1 ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , OO0o , '' )
 iIiIIi1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , OO0o , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1I1IiI1 ) , 4 , III1iII1I1ii + 'AdvancedSettingXML.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']URL FIXES[/COLOR]' , str ( I1I1IiI1 ) , 20 , III1iII1I1ii + 'URLFixes.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 59 - 59: O00o0O00 % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * ooOOOoO
 if 41 - 41: iI1ii11iIi1i % Ii1I
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
 if 12 - 12: O00o0O00
 if 69 - 69: ii + O00o0O00
def IIi11I1 ( ) :
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
 if 49 - 49: IIiIiII11i - oOo0O0Ooo / I11O0O0oOO00O00o
def O0O0ooOOO ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Local Zip[/COLOR]' , iIii1 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , OO0o , '' )
 iIiIIi1 ( '[COLOR' + iiI1IiI + ']My Online Zip[/COLOR]' , OOooO0OOoo , 43 , III1iII1I1ii + 'MyOnlineZip.png' , OO0o , '' )
 if 70 - 70: O0OOOoOoo0 . o0o00Oo0O . ii1ii11IIIiiI . o0o00Oo0O + ooOoO0O00
def i1II1I ( ) :
 O000OOo00oo ( )
 iIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , OO0o , '' )
 iIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , OO0o , '' )
 iIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , OO0o , '' )
 if 95 - 95: oO0o - O00o0O00 / IIiIiII11i % Ii1I . I11i
 if 24 - 24: ooOoO0O00 . Ii
 if 16 - 16: I1ii11iIi11i % Ii1I + I11O0O0oOO00O00o - o0o00Oo0O . Ii1IIIi1 / ii1ii11IIIiiI
def IIi1I ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SKINS[/COLOR]' , str ( I1I1IiI1 ) , 33 , III1iII1I1ii + 'Skins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ARTWORK PACKS[/COLOR]' , str ( I1I1IiI1 ) , 34 , III1iII1I1ii + 'ArtworkPacks.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CREATE UNIVERSAL PATHS[/COLOR]' , I11 , 35 , III1iII1I1ii + 'CreateUniversalPath.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 27 - 27: o0o00Oo0O . ii1ii11IIIiiI / Ii1IIIi1
def OO00O000OOO ( ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi1I11I1II = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( OOO00O )
 for O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , O0O0Oo00 , O0O0Oo00 , '' )
 I1I1II1I11 ( 'tvshows' , 'INFO' )
 if 3 - 3: o0o00Oo0O
def Ooo0Oo0oo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( oOO0o000Oo00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 21 - 21: ii - iI11I1II1I1I
def OO0OoOOO0 ( ) :
 O000OOo00oo ( )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']ISENGAARD SKINS[/COLOR]' , I11 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , OO0o , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 90 - 90: O0OOOoOoo0 + IIiIiII11i * Ii1I / iI1ii11iIi1i . I11i + I11i
def I11I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + I11O0O0oOO00O00o
def IiiIi ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 96 - 96: Ii1IIIi1
def i1I11iIII1i1I ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + oOO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 13 - 13: ii * oO0oo0o - iI1ii11iIi1i / O00o0O00 + I11O0O0oOO00O00o + ooOOOoO
def iii1III1i ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 17 - 17: IIiIiII11i / IIiIiII11i
def o0OO0Oo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + I11iiii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 40 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 3 - 3: o0o00Oo0O % ii / O00o0O00
def ooOo ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0oO0OoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 70 - 70: oO0oo0o - oO0oo0o
def OoOO0OOoo ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']GenieTv Apps[/COLOR]' , '' , 80002 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Factory[/COLOR]' , str ( I1I1IiI1 ) , 2 , III1iII1I1ii + 'APKAndroidOnly.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']APK Search[/COLOR]' , str ( I1I1IiI1 ) , 30038 , III1iII1I1ii + 'APKSearch.png' , OO0o , '' )
 if 1 - 1: oOo0O0Ooo * Ii + ii1ii11IIIiiI * Ii + oO0o
def iIIi1IIi ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , i111i11I1ii in IIi1I11I1II :
  IiIi1I1 ( 'Android Apps' + i111i11I1ii , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'apps.png' )
 for i1I1ii11i1Iii , i111i11I1ii in OooOoooOo :
  IiIi1I1 ( 'Android Games' + i111i11I1ii , 'https://www.apkfiles.com' + i1I1ii11i1Iii , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
def OOooooo0 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/cat' in url :
   IiIi1I1 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def oOOII1i11i1iIi11 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '/app' in url :
   IiIi1I1 ( ( oO00oooOOoOo0 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , III1iII1I1ii + 'APK.png' )
def oo0O0oO0O0O ( url ) :
 I1III1111iIi = I1i111I ( url )
 I1i11 = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'href="([^"]*)" style="float:right;">next &gt;</a>' ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  if 'apk' in url :
   IiIi1I1 ( ( oO00oooOOoOo0 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + O0O0Oo00 )
 for url in OooOoooOo :
  IiIi1I1 ( 'NEXT' , I1i11 + url , 30037 , III1iII1I1ii + 'Next.png' )
def oOo0OI11i ( name , url ) :
 I1III1111iIi = I1i111I ( url )
 name = name
 IIi1I11I1II = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  url = 'https://www.apkfiles.com' + url
  Iiii1 ( name , url )
def iIIIiiiI11I ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOO0OOO = 'https://www.apkfiles.com/search?q=' + ( O00Ooo ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1i1ii = OOOO0OOO . lower ( )
 oo0O0oO0O0O ( i1i1ii )
 if 6 - 6: iI1ii11iIi1i % ooOoO0O00 . iI1ii11iIi1i * iI1ii11iIi1i
def o0Oo ( url ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( oo0ooO0 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , oO00oooOOoOo0 + '.apk' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 86 - 86: I11O0O0oOO00O00o / I11i - I11i + Ii1I + oO0oo0o
def IIiooOoO0OO0oOO ( url ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , oO00oooOOoOo0 + '.mp4' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 8 - 8: OOooOOo / o0o00Oo0O * o0o00Oo0O % ii1ii11IIIiiI - I1ii11iIi11i + I11O0O0oOO00O00o
 if 83 - 83: o0o00Oo0O . oOo0O0Ooo
def O0OIIi1 ( name , url , description ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , name )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 iIII1iiII = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIII1iiII
 print '======================================='
 extract . all ( IIiiiiIiIIii , iIII1iiII , o0oOoO00o )
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
   OOO0oOOo00O = IIi1I11I1II [ 0 ] [ 1 ]
   ooO0oo0o0 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( ooO0oo , OOO0oOOo00O )
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
def Iiii1 ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  Ooo0oO0 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ooo0oO0 : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I1i = name
  if Ooo0oO0 :
   if not os . path . exists ( oooOOOOO ) : os . makedirs ( oooOOOOO )
   if not oooooo0O000o ( url ) == True : o0Oo0oOooOoOo ( oo0o0O00 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1i , '' , 'Please Wait' )
   IIiiiiIiIIii = os . path . join ( oooOOOOO , "%s.apk" % name )
   try : os . remove ( IIiiiiIiIIii )
   except : pass
   downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IIiiiiIiIIii + '")' )
  else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 59 - 59: ii . iI1ii11iIi1i / o0o00Oo0O - O00o0O00
 if 1 - 1: ooOOOoO / ooOOOoO - Ii
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * ooOOOoO / I11i
 if 19 - 19: ii1ii11IIIiiI + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
def I1IiiiiI ( ) :
 if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
 OOO00O = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( OOO00O )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  i1I1ii11i1Iii = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + i1I1ii11i1Iii )
  iIi1I1 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , i1I1ii11i1Iii )
  if 63 - 63: Ii1IIIi1 * Ii1I . ii / O00o0O00 * I1ii11iIi11i . O0OOOoOoo0
def iIi1I1 ( name , url ) :
 if I1I1i1I ( ) == 'android' :
  Ooo0oO0 = iI111I11I1I1 . yesno ( oo0o0O00 , "Would you like to download and install:" , "%s" % name )
  if not Ooo0oO0 : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I1i = name
  if Ooo0oO0 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not oooooo0O000o ( url ) == True : o0Oo0oOooOoOo ( oo0o0O00 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oo0o0O00 , 'Downloading %s' % I1i , '' , 'Please Wait' )
   IIiiiiIiIIii = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( IIiiiiIiIIii )
   except : pass
   downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iI111I11I1I1 . ok ( oo0o0O00 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IIiiiiIiIIii + '")' )
  else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0Oo0oOooOoOo ( oo0o0O00 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 62 - 62: ooOoO0O00 / O0OOOoOoo0 . oOo0O0Ooo * I11i
 if 21 - 21: I11i
def O0Oo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 98 - 98: ii1ii11IIIiiI
 if 92 - 92: ii1ii11IIIiiI - iI11I1II1I1I
def I11III111i ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 30015 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 78 - 78: ii
def OOoo0 ( url , iconimage , fanart ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 oOO = url
 O0O0Oo00 = iconimage
 fanart = fanart
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for I1i11 , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp4' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Watch VIDEO' , url + '/' + I1i11 , 222 , O0O0Oo00 , fanart , '' )
  if 'description' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Read Description' , url + '/' + I1i11 , 30017 , O0O0Oo00 , fanart , '' )
  if 'images' in oO00oooOOoOo0 :
   I1IIII1i ( 'View Images' , url + '/' + I1i11 , 30018 , O0O0Oo00 , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Android' , url + '/' + I1i11 , 30016 , O0O0Oo00 , fanart , '' )
  if 'url' in oO00oooOOoOo0 :
   iIiIIi1 ( 'Install Build On Pc' , url + '/' + I1i11 , 30019 , O0O0Oo00 , fanart , '' )
 I1I1II1I11 ( 'movies' , 'INFO' )
 if 36 - 36: I11i + I11O0O0oOO00O00o - ooOOOoO + iI11I1II1I1I + ii
def IiI1i111IiIiIi1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  i1II11II1 ( url )
  if 5 - 5: I1ii11iIi11i - Ii1I % oO0oo0o - IIiIiII11i . oOo0O0Ooo + Ii1IIIi1
def iiIi1I1i1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url="([^"]*)"' ) . findall ( OOO00O )
 for url in IIi1I11I1II :
  OOOIiIi1111ii ( url )
  if 45 - 45: I1ii11iIi11i - I11i % ii1ii11IIIiiI
def i1IIi1i1Ii1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'desc="([^"]*)"' ) . findall ( OOO00O )
 for Iii in IIi1I11I1II :
  O0O0Oooo0o ( 'Description:' , Iii )
  if 63 - 63: ooOOOoO + I11i
def IIIIIIII ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( url )
 url = url
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOO00O )
 for I1i11 , oO00oooOOoOo0 in IIi1I11I1II :
  if 'png' in oO00oooOOoOo0 :
   iIiIIi1 ( 'image' , '' , '' , url + '/' + I1i11 , url + '/' + I1i11 , '' )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 83 - 83: iI11I1II1I1I
def o00o0oOo0O0O ( name , url , description ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , name + '.zip' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ii1 ( )
 if 7 - 7: IIiIiII11i - O00o0O00 . IIiIiII11i
 if 53 - 53: oO0oo0o % I11O0O0oOO00O00o . O0OOOoOoo0 - OOooOOo
def OOOIiIi1111ii ( url ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
 OoOoO0OoOOOOo ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OooOo000OOOOo ( )
 if 21 - 21: oOo0O0Ooo % I11i
def i1II11II1 ( url ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
 OoOoO0OoOOOOo ( url )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OooOo000OOOOo ( )
 if 33 - 33: O00o0O00
def IiiiI111I ( name , url , description ) :
 oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IIiiiiIiIIii = os . path . join ( iIii1 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OooOo000OOOOo ( )
 if 49 - 49: I11i * iI1ii11iIi1i + I11O0O0oOO00O00o + Ii1IIIi1
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
  IIi11 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  o0Oo00 . write ( IIi11 . rstrip ( '\r\n' ) + '\n' )
def OooOo000OOOOo ( ) :
 ooo00Ooo = iI111I11I1I1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if ooo00Ooo == 0 : return
 elif ooo00Ooo == 1 : pass
 ooo0O0OOO000o = I1I1i1I ( )
 oo00oOO000oO0 ( "Platform: " + str ( ooo0O0OOO000o ) )
 os . _exit ( 1 )
 oo00oOO000oO0 ( "Force close failed!  Trying alternate methods." )
 if ooo0O0OOO000o == 'osx' :
  oo00oOO000oO0 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iI111I11I1I1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ooo0O0OOO000o == 'linux' :
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
 elif ooo0O0OOO000o == 'android' :
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
 elif ooo0O0OOO000o == 'windows' :
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
 for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( url ) :
  for file in IIIIIii1ii11 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oO0i1iI = open ( ( os . path . join ( iIoo0ooooO , file ) ) ) . read ( )
    iiIIi = oO0i1iI . replace ( I11 , 'special://home/' )
    o0Oo00 = open ( ( os . path . join ( iIoo0ooooO , file ) ) , mode = 'w' )
    o0Oo00 . write ( str ( iiIIi ) )
    o0Oo00 . close ( )
 OooOo000OOOOo ( )
 if 36 - 36: I11O0O0oOO00O00o . IIiIiII11i
def iIIiI1iiI ( ) :
 IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 18 - 18: Ii1IIIi1 - oO0oo0o % Ii1IIIi1 / I11O0O0oOO00O00o
def O0Oo00OO00Ooo ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def OO0O00OoOOOo ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def Oo0 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in OooOoooOo :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']Filter - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , O0O0Oo00 )
def o0OOOOO0O ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oO00O0 ( url )
def I1I1IiIi1 ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo
 oOO0o0oo0 = 'https://www.radionomy.com/en/search/index?query=' + ( O00Ooo ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']Stream - ' + oO00oooOOoOo0 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + i1I1ii11i1Iii , 70005 , O0O0Oo00 )
  if 78 - 78: O00o0O00 + Ii1IIIi1 . ooOOOoO
  if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
def o0o0O0Oo ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , 'http://www.listenlive.eu/' + i1I1ii11i1Iii , 10111113 , III1iII1I1ii + 'radio.png' )
def IiiIIi ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'radio.png' )
  if 71 - 71: ooOOOoO + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + i1I1ii11i1Iii , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0oOOO0 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 in IIi1I11I1II :
  if 'ol.gif' in O0O0Oo00 :
   pass
  elif 'link_block_' in O0O0Oo00 :
   pass
  elif '.png' in O0O0Oo00 :
   pass
  else :
   IiIi1I1 ( ( O0O0Oo00 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in OooOoooOo :
  IiIi1I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOOiI1iIIII1 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
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
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ooooooO0oo + 'books' + IIIII )
 IIi1I11I1II = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , i1I1ii11i1Iii , o0ooOo00O in IIi1I11I1II :
  if O00Ooo in oO00oooOOoOo0 . lower ( ) :
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
 I1i11 = url
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in OooOoooOo :
  if 'mp3' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i11 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i11 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1i11 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in oO00oooOOoOo0 :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i11 + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 50 - 50: iI1ii11iIi1i
   if 22 - 22: I11O0O0oOO00O00o * o0o00Oo0O . IIiIiII11i - oO0o
   if 90 - 90: oO0oo0o
def O00OO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 I1i11 = url
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
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i11 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in oO00oooOOoOo0 :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i11 + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1i11 + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: Ii1IIIi1 + iI1ii11iIi1i % I11i
   if 1 - 1: OOooOOo % ii1ii11IIIiiI - O00o0O00 + oO0oo0o + o0o00Oo0O * I11i
def o0OooOo ( ) :
 OOoOoo00Oo ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 OOoOoo00Oo ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 OOoOoo00Oo ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 70 - 70: I1ii11iIi11i - oO0oo0o . iI11I1II1I1I % I11O0O0oOO00O00o / OOooOOo - o0o00Oo0O
def o0O0oo0o ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 in IIi1I11I1II :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i1I1ii11i1Iii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in O0O0Oo00 :
   pass
  else :
   OOoOoo00Oo ( O0O0Oo00 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i1I1ii11i1Iii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + O0O0Oo00 + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 12 - 12: OOooOOo % ooOOOoO % Ii1I . Ii * iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: Ii * iI11I1II1I1I % ii
 if 5 - 5: OOooOOo % ii
def OO0I111i1I ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 14 - 14: iI1ii11iIi1i % oOo0O0Ooo - iI11I1II1I1I . O00o0O00 + oO0o - ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: Ii1IIIi1
def OO ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if O00Ooo in oO00oooOOoOo0 . lower ( ) :
   if '</a>' in oO00oooOOoOo0 :
    pass
   elif '(' in oO00oooOOoOo0 :
    OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 1 - 1: O00o0O00 . ooOOOoO
    if 42 - 42: O00o0O00 % oO0oo0o / oO0o - oO0oo0o * Ii
def iI1IiiiIiI1Ii ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi1I11I1II = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '</a>' in oO00oooOOoOo0 :
   pass
  elif '(' in oO00oooOOoOo0 :
   OOoOoo00Oo ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i1I1ii11i1Iii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 78 - 78: ii / O00o0O00 % OOooOOo * ii
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: oO0oo0o
 if 29 - 29: Ii1IIIi1 + Ii % I11O0O0oOO00O00o
def oOo00Ooo0o0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  I1i11 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1i11 )
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
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , O0O0Oo00 , O0O0Oo00 , oO00oooOOoOo0 )
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
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']CARTOONS[/COLOR]' , '' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 55 - 55: oOo0O0Ooo
def Ii1i1 ( ) :
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 if 65 - 65: oO0oo0o + Ii1I / O00o0O00
def oo0oo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '?c=' in url :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 49 - 49: Ii % OOooOOo + ii1ii11IIIiiI . IIiIiII11i % Ii1IIIi1 * O00o0O00
def oooo ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , I11iII , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Genre' in url :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
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
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( IIIi1I1IIii1II )
 if 87 - 87: O00o0O00 + I11i . Ii1IIIi1 - ii
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if O00Ooo in oO00oooOOoOo0 . lower ( ) :
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
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1III1111iIi )
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
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1III1111iIi )
 for O0O0Oo00 in OooOoooOo :
  OoO00O0 = O0O0Oo00
 I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1III1111iIi )
 for url in I1 :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , OO0o , '' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10007 , OoO00O0 )
  if 23 - 23: ooOoO0O00 . iI11I1II1I1I . O00o0O00 . o0o00Oo0O % iI1ii11iIi1i % Ii
  if 11 - 11: o0o00Oo0O - IIiIiII11i . O00o0O00 . iI1ii11iIi1i % ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: I1ii11iIi11i / Ii1IIIi1 . ii1ii11IIIiiI * ii + I11O0O0oOO00O00o - ooOoO0O00
def ooooo0O0 ( url , IMAGE ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   i1III1iI ( url )
   if 38 - 38: iI11I1II1I1I / O0OOOoOoo0
   if 13 - 13: iI11I1II1I1I
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77: Ii - iI11I1II1I1I / oO0oo0o / O0OOOoOoo0 / oO0o
def i1III1iI ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oO00O0 ( url )
  if 56 - 56: ii * o0o00Oo0O
  if 85 - 85: ii % OOooOOo * iI11I1II1I1I
  if 44 - 44: iI11I1II1I1I . Ii1I + ii1ii11IIIiiI . O0OOOoOoo0
def II1i11 ( ) :
 if 28 - 28: IIiIiII11i - oO0oo0o % OOooOOo + oO0o - OOooOOo
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , OO0o , '' )
 if 28 - 28: IIiIiII11i . oO0oo0o + o0o00Oo0O . o0o00Oo0O . O00o0O00
def ooOoo000oO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  if 'elete' in oO00oooOOoOo0 :
   pass
  else :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 222 , O0O0Oo00 )
   if 50 - 50: ooOOOoO + I11i
def o0OoOOo ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0Oo0iI1II1III1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , oooo0O0o0OoOO , i1iII1IiiIiI1 in O0Oo0iI1II1III1 :
  for O00Ooo in oooo0O0o0OoOO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   III1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for i1I1ii11i1Iii , oO00oooOOoOo0 in III1 :
    if 'tube' in i1I1ii11i1Iii :
     pass
    elif 'stage' in i1I1ii11i1Iii :
     IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oooo0O0o0OoOO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0O0Oo00 , )
    elif 'vee' in i1I1ii11i1Iii :
     pass
     if 7 - 7: Ii + oOo0O0Ooo
def I1i1I1II ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0Oo0iI1II1III1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , oooo0O0o0OoOO , i1iII1IiiIiI1 in O0Oo0iI1II1III1 :
  III1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in III1 :
   if 'tube' in i1I1ii11i1Iii :
    pass
   elif 'stage' in i1I1ii11i1Iii :
    IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oooo0O0o0OoOO + '   -   ' + oO00oooOOoOo0 + '[/COLOR]' , ( i1I1ii11i1Iii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + O0O0Oo00 )
   elif 'vee' in i1I1ii11i1Iii :
    pass
    if 58 - 58: O00o0O00 . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
    if 50 - 50: Ii1IIIi1 % IIiIiII11i - O0OOOoOoo0 . ooOoO0O00 + o0o00Oo0O % Ii1IIIi1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1IIIi1 . ooOoO0O00 + iI1ii11iIi1i
def oOOoOOO0oo0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oooOOoooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIIi1I1IIii1II )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oooOOoooo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oooOOoooo :
  oO00O0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 87 - 87: O0OOOoOoo0 / OOooOOo % I11i * oO0oo0o
  if 77 - 77: oO0oo0o - I1ii11iIi11i - iI11I1II1I1I
  if 16 - 16: oO0o / Ii1IIIi1 / ooOoO0O00 . Ii1IIIi1 + oO0oo0o
  if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
  if 44 - 44: ii . IIiIiII11i . O00o0O00 % ii
  if 86 - 86: Ii + o0o00Oo0O * ooOOOoO - oO0o * O00o0O00 + o0o00Oo0O
  if 95 - 95: iI11I1II1I1I . ii1ii11IIIiiI % Ii1IIIi1 - ii1ii11IIIiiI * IIiIiII11i
def o0o ( ) :
 if 59 - 59: ooOoO0O00 % iI11I1II1I1I + ii
 oOOO0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , OO0o , '' )
 oOOO0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 32 - 32: O0OOOoOoo0 % ii1ii11IIIiiI * I1ii11iIi11i
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 72 - 72: O0OOOoOoo0 . Ii1IIIi1 - ii1ii11IIIiiI - iI1ii11iIi1i % ooOoO0O00
def oO0o00O0O0oo0 ( ) :
 oOOO0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 oOOO0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , OO0o , '' )
 if 24 - 24: ii1ii11IIIiiI * oO0oo0o
 I1I1II1I11 ( 'movies' , 'MAIN' )
def Oo000O ( ) :
 if 42 - 42: ooOOOoO % Ii1IIIi1 % I11i % oO0oo0o + I11O0O0oOO00O00o % OOooOOo
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 iI1iIIiii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 52 - 52: iI1ii11iIi1i % O00o0O00 * oOo0O0Ooo % I11O0O0oOO00O00o + O00o0O00 / Ii1IIIi1
 for oo000o in iI1iIIiii :
  OO00o0oOO = I11i1I1I + oo000o + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( OO00o0oOO )
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oOo0O , oO00oooOOoOo0 in IIi1I11I1II :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    i1i1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oOo0O , oO000oOo00o0o )
    if 46 - 46: I11O0O0oOO00O00o . ooOOOoO / IIiIiII11i % iI11I1II1I1I + ooOOOoO
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 61 - 61: O00o0O00 / oO0o + IIiIiII11i . oO0oo0o / I1ii11iIi11i * O00o0O00
    if 46 - 46: iI11I1II1I1I
def I111iiiii1 ( ) :
 if 100 - 100: Ii1I * Ii % oO0oo0o / I1ii11iIi11i / O0OOOoOoo0 + Ii1I
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 iI1iIIiii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 59 - 59: ii1ii11IIIiiI - ooOOOoO
 for oo000o in iI1iIIiii :
  iiiii111 = I11i1I1I + oo000o + IIIII
  IIIi1I1IIii1II = ooOooo000oOO ( iiiii111 )
  IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , oO000oOo00o0o , i1I1ii11i1Iii , O0O0Oo00 , oOo0O , oO0oo0o00o0O in IIi1I11I1II :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    oOOO0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , oO0oo0o00o0O , O0O0Oo00 , oOo0O , oO000oOo00o0o )
    if 80 - 80: iI11I1II1I1I
    I1I1II1I11 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 23 - 23: IIiIiII11i
    if 71 - 71: ii1ii11IIIiiI * I1ii11iIi11i . I11O0O0oOO00O00o
def i1ii1iiIi1II ( ) :
 if 98 - 98: oO0o - iI1ii11iIi1i . ooOOOoO % Ii
 I1III1111iIi = O0i1II1Iiii1I11 ( I11i1I1I + 'spongemain.php' )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , oO000oOo00o0o , i1I1ii11i1Iii , O0O0Oo00 , oOo0O , oO0oo0o00o0O in IIi1I11I1II :
  oOOO0 ( oO00oooOOoOo0 , i1I1ii11i1Iii , oO0oo0o00o0O , O0O0Oo00 , oOo0O , oO000oOo00o0o )
  I1I1II1I11 ( 'movies' , 'MAIN' )
def OO00oo ( url ) :
 if 84 - 84: O0OOOoOoo0 + Ii - O00o0O00 * O0OOOoOoo0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1IiiIiii1 = ( '%s%s' % ( i11i , url ) )
 OOO00O = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in IIi1I11I1II :
  OO0OOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
  for ooOOo0o in OO0OOO00 :
   if ooOOo0o == url :
    oO00oooOOoOo0 = ( '[COLORred]Watched - [/COLOR]' + oO00oooOOoOo0 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  i1i1I1 ( oO00oooOOoOo0 , url , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
  if 50 - 50: IIiIiII11i - ii1ii11IIIiiI + iI11I1II1I1I + iI11I1II1I1I
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 91 - 91: IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: I11i
  if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
def Ii11ii1I1 ( url ) :
 if 11 - 11: iI11I1II1I1I . OOooOOo / ooOOOoO % O0OOOoOoo0
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , oO000oOo00o0o , url , O0O0Oo00 , oOo0O , oO0oo0o00o0O in IIi1I11I1II :
  oOOO0 ( oO00oooOOoOo0 , url , oO0oo0o00o0O , O0O0Oo00 , oOo0O , oO000oOo00o0o )
  if 61 - 61: O0OOOoOoo0 - O00o0O00 + O00o0O00
  I1I1II1I11 ( 'movies' , 'MAIN' )
  if 40 - 40: Ii . iI11I1II1I1I
  if 2 - 2: ooOoO0O00 * oO0oo0o - oO0oo0o + ii % OOooOOo / OOooOOo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: ii
def i1i1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 71 - 71: ooOOOoO + ooOoO0O00 - Ii1IIIi1 - Ii . I11O0O0oOO00O00o - O0OOOoOoo0
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooOoo0OO . setProperty ( "Fanart_Image" , fanart )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = False )
 return IIii1III
 if 85 - 85: IIiIiII11i . O0OOOoOoo0 % O00o0O00 % I11O0O0oOO00O00o
def oOOO0 ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: oO0oo0o * I11O0O0oOO00O00o / iI11I1II1I1I % oO0oo0o / iI11I1II1I1I
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooOoo0OO . setProperty ( "Fanart_Image" , fanart )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = True )
 return IIii1III
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
if 45 - 45: iI1ii11iIi1i - O00o0O00
if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . I11O0O0oOO00O00o % O0OOOoOoo0 . IIiIiII11i
def I1ii1Ii1 ( string ) :
 if Ii1iIiII1ii1 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 73 - 73: o0o00Oo0O . oO0oo0o + Ii + iI11I1II1I1I - I11O0O0oOO00O00o / OOooOOo
def OO0OOOOo0000O ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1Ii11ii = [ ]
 try :
  if 89 - 89: I1ii11iIi11i + Ii1I - I11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I1IIiiIiii ) == False :
  I1ii1Ii1 ( 'Making Favorites File' )
  i1Ii11ii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oO0i1iI = open ( I1IIiiIiii , "w" )
  oO0i1iI . write ( json . dumps ( i1Ii11ii ) )
  oO0i1iI . close ( )
 else :
  I1ii1Ii1 ( 'Appending Favorites' )
  oO0i1iI = open ( I1IIiiIiii ) . read ( )
  iII1I11 = json . loads ( oO0i1iI )
  iII1I11 . append ( ( name , url , iconimage , fanart , mode ) )
  iiIIi = open ( I1IIiiIiii , "w" )
  iiIIi . write ( json . dumps ( iII1I11 ) )
  iiIIi . close ( )
  if 15 - 15: I11O0O0oOO00O00o
  if 13 - 13: iI11I1II1I1I * OOooOOo / ii1ii11IIIiiI % O0OOOoOoo0 + oO0oo0o
def iiiI1iI1 ( ) :
 if os . path . exists ( I1IIiiIiii ) == False :
  i1Ii11ii = [ ]
  I1ii1Ii1 ( 'Making Favorites File' )
  i1Ii11ii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oO0i1iI = open ( I1IIiiIiii , "w" )
  oO0i1iI . write ( json . dumps ( i1Ii11ii ) )
  oO0i1iI . close ( )
 else :
  I1oOoO0OOO00O = json . loads ( open ( I1IIiiIiii ) . read ( ) )
  OOOOO0o0OOo = len ( I1oOoO0OOO00O )
  for I11I11I11IiIi in I1oOoO0OOO00O :
   oO00oooOOoOo0 = I11I11I11IiIi [ 0 ]
   i1I1ii11i1Iii = I11I11I11IiIi [ 1 ]
   oOoooo000Oo00 = I11I11I11IiIi [ 2 ]
   try :
    OOii1ii1i11I1I = I11I11I11IiIi [ 3 ]
    if OOii1ii1i11I1I == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     OOii1ii1i11I1I = oOoooo000Oo00
    else :
     OOii1ii1i11I1I = oOo0O
   try : iiII1iiiiiii = I11I11I11IiIi [ 5 ]
   except : iiII1iiiiiii = None
   try : iiIiii = I11I11I11IiIi [ 6 ]
   except : iiIiii = None
   if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
   if I11I11I11IiIi [ 4 ] == 0 :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , '' , oOoooo000Oo00 , oOo0O , '' , 'fav' )
   else :
    I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , I11I11I11IiIi [ 4 ] , oOoooo000Oo00 , oOo0O , '' , 'fav' )
    if 83 - 83: ooOoO0O00
def O0OooOO ( name ) :
 iII1I11 = json . loads ( open ( I1IIiiIiii ) . read ( ) )
 for i1i1 in range ( len ( iII1I11 ) ) :
  if iII1I11 [ i1i1 ] [ 0 ] == name :
   del iII1I11 [ i1i1 ]
   iiIIi = open ( I1IIiiIiii , "w" )
   iiIIi . write ( json . dumps ( iII1I11 ) )
   iiIIi . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 68 - 68: iI1ii11iIi1i - oOo0O0Ooo
 if 41 - 41: oO0oo0o
def o0O0Oo00 ( ) :
 I11II1 = os . path . join ( O0O , 'addons.ini' )
 i1i1i1IOOOOOo = open ( I11II1 , "w+" )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://piesustv.net:8000/get.php?username=' + ooOoOoo0O + '&password=' + OooO0 + '&type=m3u_plus&output=mpegts' )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( IIIi1I1IIii1II )
 i1i1i1IOOOOOo . write ( r'[' + IiII + ']' + '\n' )
 for oO00oooOOoOo0 , O0O0Oo00 , OooOo00o , i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = ( i1I1ii11i1Iii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OOooO = ( oO00oooOOoOo0 + '=plugin://' + IiII + '/?url=' + i1I1ii11i1Iii + '&mode=10012&name=' + ( oO00oooOOoOo0 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( O0O0Oo00 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( O0O0Oo00 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  i1i1i1IOOOOOo . write ( OOooO + '\n' )
  if 28 - 28: O0OOOoOoo0 - O00o0O00 / oOo0O0Ooo
  if 27 - 27: ooOoO0O00 + oOo0O0Ooo * Ii1I + O00o0O00 . oO0oo0o
def i1I111I1Iii1 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + '247.png' , III1iII1I1ii + '247.png' , '' )
def O00Oo0 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def o0Oooo0 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def ii1iIIi11 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def iI1IIIII1Ii ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi1I11I1II = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  iIiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 13 - 13: IIiIiII11i
  if 57 - 57: iI1ii11iIi1i - ii
def OOoOO0O0o0 ( ) :
 if 44 - 44: O00o0O00 / I1ii11iIi11i + ooOOOoO % IIiIiII11i / oO0o + Ii
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
 if 20 - 20: Ii1I
def IIiiiiIiI1III ( ) :
 if 26 - 26: ooOoO0O00
 I1III1111iIi = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 , Ii111iIi1iIi in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 + '  -  ' + ( Ii111iIi1iIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 10023 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 35 - 35: oOo0O0Ooo
  if 80 - 80: oO0oo0o % oO0oo0o % o0o00Oo0O - Ii . Ii1IIIi1 / o0o00Oo0O
  if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / iI1ii11iIi1i . ooOoO0O00
def OOOO00OoooO ( ) :
 if 7 - 7: Ii1I / IIiIiII11i - I11O0O0oOO00O00o + ooOoO0O00 + iI1ii11iIi1i
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
 if 7 - 7: O0OOOoOoo0 + iI1ii11iIi1i
def IiiIIiI1iI1 ( url ) :
 oOO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIIi1I1IIii1II = cloudflare . source ( oOO )
 IIi1I11I1II = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , OO0o , '' )
  if 86 - 86: ooOoO0O00 / iI1ii11iIi1i * oOo0O0Ooo
  if 67 - 67: Ii1I * Ii1I / oO0oo0o * ii + OOooOOo
  if 79 - 79: ooOoO0O00
  if 1 - 1: oO0oo0o / ooOoO0O00
def O0oo0 ( ) :
 if 37 - 37: Ii
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O00Ooo ) . replace ( ' ' , '+' )
 IIIi1I1IIii1II = cloudflare . source ( i1I1ii11i1Iii )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  if O00Ooo in oO00oooOOoOo0 . lower ( ) :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10022 , III1iII1I1ii + 'dtv.png' )
   if 12 - 12: Ii1I / iI1ii11iIi1i
   if 5 - 5: ii
   if 18 - 18: oOo0O0Ooo % ii - Ii1IIIi1 . Ii * I1ii11iIi11i % iI1ii11iIi1i
def Ii1I1 ( url ) :
 IIIi1I1IIii1II = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for I1i11 , O0oo00oOOO0o , II1iI111iiIIiI1I , oO00oooOOoOo0 in IIi1I11I1II :
  ooO00Oo = ( II1iI111iiIIiI1I ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Iiii1Ii1I = ( O0oo00oOOO0o ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oooOOOOOi1iIii = 'Season ' + Iiii1Ii1I + 'Episode ' + ooO00Oo + oO00oooOOoOo0
  o0O0ooooooo00 ( oooOOOOOi1iIii , I1i11 )
  if 28 - 28: O0OOOoOoo0 * I11O0O0oOO00O00o % Ii * Ii1IIIi1 / iI1ii11iIi1i
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 41 - 41: O00o0O00 - I11i + iI1ii11iIi1i
  if 15 - 15: I11O0O0oOO00O00o / I11i + iI1ii11iIi1i
def o0O0ooooooo00 ( name , url ) :
 I1i11 = url
 O0oo00o = name
 O0 = cloudflare . source ( I1i11 )
 OooOoooOo = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for oooOOoooo , IIi1i1 in OooOoooOo :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + O0oo00o + IIi1i1 + '[/COLOR]' , oooOOoooo , 10012 , III1iII1I1ii + 'dtv.png' )
  if 84 - 84: O00o0O00 + iI1ii11iIi1i + I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: iI1ii11iIi1i
 if 93 - 93: O0OOOoOoo0
def II11iIIii ( ) :
 if 57 - 57: o0o00Oo0O * Ii1I . Ii
 if 69 - 69: o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
 if 52 - 52: oO0o * ii
 if 12 - 12: o0o00Oo0O + ooOOOoO * ooOoO0O00 . oO0o
 if 71 - 71: ii1ii11IIIiiI - I11i - O00o0O00
 if 28 - 28: iI11I1II1I1I
 if 7 - 7: I11i % ooOOOoO * OOooOOo
 if 58 - 58: ooOOOoO / I11O0O0oOO00O00o + IIiIiII11i % Ii1IIIi1 - ii
 if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * oO0oo0o
 if 30 - 30: I11O0O0oOO00O00o % OOooOOo / Ii1I * o0o00Oo0O * iI1ii11iIi1i . oOo0O0Ooo
 if 46 - 46: OOooOOo - o0o00Oo0O
 if 70 - 70: I11O0O0oOO00O00o + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * I11O0O0oOO00O00o
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 49 - 49: I11i
 if 25 - 25: Ii1IIIi1 . ii * iI11I1II1I1I . I11i / o0o00Oo0O + iI1ii11iIi1i
def ooo0o0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIIIIo0ooOoO000oO = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 IIi1I11I1II = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 84 - 84: I11O0O0oOO00O00o - I1ii11iIi11i * o0o00Oo0O / iI1ii11iIi1i . iI1ii11iIi1i
def ooO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 34 - 34: ooOoO0O00 % ooOOOoO
def OoOo ( url ) :
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
  if 33 - 33: ooOoO0O00 / ii1ii11IIIiiI - ooOoO0O00 . I1ii11iIi11i
  if 18 - 18: I1ii11iIi11i / o0o00Oo0O + Ii1IIIi1
def ooIiI11i1I11111 ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1IIIIIIiI1 = 'http://www.watchseries.ac/search/' + O00Ooo . replace ( ' ' , '%20' )
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( Ii1IIIIIIiI1 )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'watch online' in oO00oooOOoOo0 :
   pass
  else :
   print i1I1ii11i1Iii
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , O0O0Oo00 , '' , '' )
   if 24 - 24: oOo0O0Ooo * iI1ii11iIi1i % o0o00Oo0O - I1ii11iIi11i
   xbmcplugin . setContent ( O000OO0 , 'movies' )
   if 30 - 30: ooOoO0O00
def I11iiI1I1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , url , oO00oooOOoOo0 , II1iI111iiIIiI1I , oO000oOo00o0o in IIi1I11I1II :
  o0i1Ii11II = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( II1iI111iiIIiI1I ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + o0i1Ii11II + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , O0O0Oo00 , '' , oO000oOo00o0o )
  if 33 - 33: ooOOOoO . ii . oO0oo0o
def iI1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  o0i1Ii11II = ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + o0i1Ii11II + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 94 - 94: I11O0O0oOO00O00o . oOo0O0Ooo
def oooOoo0OoOO0000 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , O0O0Oo00 , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 2 - 2: iI1ii11iIi1i * Ii1I * ii
def oOOOooO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 IIIIIo0ooOoO000oO = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0oo00oOOO0o , O0Oo0iI1II1III1 in IIIIIo0ooOoO000oO :
  IIi1I11I1II = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0Oo0iI1II1III1 ) )
  for url , oO00oooOOoOo0 in IIi1I11I1II :
   o0i1Ii11II = ( O0oo00oOOO0o ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + o0i1Ii11II + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 OooOoooOo = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in OooOoooOo :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: I11i . I11O0O0oOO00O00o
class I1IIIIIi1IIiI ( ) :
 if 26 - 26: I11i % O00o0O00 + O00o0O00 % I11O0O0oOO00O00o * Ii / Ii1IIIi1
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 64 - 64: oO0oo0o % OOooOOo / IIiIiII11i % O0OOOoOoo0 - Ii1IIIi1
  o0i1Ii11II = name
  self . Get_Sources ( i1I1ii11i1Iii , o0i1Ii11II )
  if 2 - 2: ii1ii11IIIiiI - Ii1I + I11i * oO0o / Ii1IIIi1
  if 26 - 26: O00o0O00 * I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( URL )
  IIi1I11I1II = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   URL = 'http://www.watchseries.ac/link/' + i1I1ii11i1Iii
   self . Get_site_link ( URL , season_name )
   if 31 - 31: I11O0O0oOO00O00o * oO0oo0o . iI1ii11iIi1i
 def Get_site_link ( self , url , season_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  OooOoooOo = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  I1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for url in IIi1I11I1II :
   self . main ( url , season_name )
  for url in OooOoooOo :
   self . main ( url , season_name )
  for url in I1 :
   self . main ( url , season_name )
   if 35 - 35: I11O0O0oOO00O00o
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o00oo = 'DACLIPS'
   if o00oo in I1IIIIIi1IIiI . source_list :
    pass
   else :
    self . daclips ( url , season_name , o00oo )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o00oo = 'FILEHOOT'
    if o00oo in I1IIIIIi1IIiI . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o00oo )
   else :
    if 'thevideo.me' in url :
     o00oo = 'THEVIDEO'
     if o00oo in I1IIIIIi1IIiI . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o00oo )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o00oo = 'ALLMYVIDEOS'
      if o00oo in I1IIIIIi1IIiI . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o00oo )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o00oo = 'VIDSPOT'
       if o00oo in I1IIIIIi1IIiI . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o00oo )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o00oo = 'VODLOCKER'
        if o00oo in I1IIIIIi1IIiI . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o00oo )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 70 - 70: I11O0O0oOO00O00o - I1ii11iIi11i / ii % ii
         if 95 - 95: ii % ii . iI1ii11iIi1i
 def allmyvid ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for III1ii , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 38 - 38: Ii1I + OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( IIIi1I1IIii1II )
  for III1ii , oO00oooOOoOo0 in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 68 - 68: o0o00Oo0O
 def thevideo ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIIi1I1IIii1II )
  for III1ii in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 76 - 76: Ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for III1ii in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 99 - 99: I11i
 def daclips ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( IIIi1I1IIii1II )
  for III1ii in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 1 - 1: iI1ii11iIi1i * OOooOOo * oO0o + I1ii11iIi11i
 def filehoot ( self , url , season_name , source_name ) :
  IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
  IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for III1ii in IIi1I11I1II :
   self . Printer ( III1ii , season_name , source_name )
   if 90 - 90: ii1ii11IIIiiI % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / O00o0O00 + I11O0O0oOO00O00o
 def Printer ( self , Link , season_name , source_name ) :
  if 89 - 89: oO0oo0o
  if Link in I1IIIIIi1IIiI . List :
   pass
  elif source_name in I1IIIIIi1IIiI . source_list :
   pass
  else :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   I1IIIIIi1IIiI . List . append ( Link )
   I1IIIIIi1IIiI . source_list . append ( source_name )
   if 87 - 87: Ii1IIIi1 % I1ii11iIi11i
   xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 62 - 62: oO0o + O0OOOoOoo0 / Ii1IIIi1 * Ii
   if 37 - 37: Ii1IIIi1
   if 33 - 33: oO0o - o0o00Oo0O - oO0o
   if 94 - 94: ooOOOoO * I11O0O0oOO00O00o * ii / I11i . ooOOOoO - I11i
   if 13 - 13: O00o0O00 / ooOOOoO - oO0o / O00o0O00 . ooOoO0O00
def IiI1i111i ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , OO0o , '' )
 if 26 - 26: iI11I1II1I1I * I11i . I11O0O0oOO00O00o
def I11III11III1 ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( I1III1111iIi )
 for ooo , url , OoO00OooO0 , o00OOo , Ii11III , oOoOOOo , I1Ii1i11I1I , o0Oo00 , oO0i1iI , oo0o000o0oOO0 , OOO000OOo0o0O in IIi1I11I1II :
  OoO00OooO0 = OoO00OooO0
  if 'Arsenal' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'arsenal-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                                  ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Bournemouth' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'afc-bournemouth.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                       ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Burnley' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'KEGnQWW.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                                   ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Chelsea' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'chelsea.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                                  ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Crystal' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'CrystalPalace.0.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                       ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Everton' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'Everton.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                                   ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Hull' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'hull-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                                 ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Leicester' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                       ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Liverpool' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'liverpool-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                               ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Manchester City' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'city-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '               ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Manchester United' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + '91.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '          ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Middlesbrough' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                 ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Southampton' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'southampton-fc-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                   ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Stoke City' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'stoke-city.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                          ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Sunderland' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'sunderland-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                        ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Swansea' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'swansea-city-afc.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                    ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Tottenham' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '        ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Watford' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'watford-fc-hd-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '                              ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'Bromwich' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '   ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  elif 'West Ham' in OoO00OooO0 :
   ooo0O = III1iII1I1ii + 'west-ham.png'
   oO00oooOOoOo0 = '[COLOR' + iiI1IiI + ']' + ooo + ' - ' + OoO00OooO0 + '             ' + o00OOo + '        ' + Ii11III + '        ' + oOoOOOo + '        ' + I1Ii1i11I1I + '        ' + o0Oo00 + '        ' + oO0i1iI + '        ' + oo0o000o0oOO0 + '[/COLOR]'
  I1IIII1i ( str ( oO00oooOOoOo0 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , ooo0O , ooo0O , OoO00OooO0 )
  if 14 - 14: Ii1IIIi1 - I11O0O0oOO00O00o * ii + O00o0O00 . IIiIiII11i
def i1i1I11i1I ( description ) :
 OoO00OooO0 = description
 i1I1ii11i1Iii = ( 'http://www.fullmatchesandshows.com/?s=' + OoO00OooO0 ) . replace ( ' ' , '%20' )
 O0oII1IIiiI1 ( i1I1ii11i1Iii )
 if 96 - 96: O00o0O00 + O00o0O00 % ooOOOoO % O00o0O00
def IiiI1I ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi1I11I1II = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( '[COLOR' + iiI1IiI + ']' + ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i1I1ii11i1Iii , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0O0Oo00 , OO0o , '' )
  if 3 - 3: IIiIiII11i - iI1ii11iIi1i % OOooOOo / oO0oo0o
def Ii1 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIIIIo0ooOoO000oO = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for IIIIIo0ooOoO000oO in IIIIIo0ooOoO000oO :
  ooOO0OOO00o = re . compile ( '(.*?)</h2>' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
  for OoOoO0ooooO0 in ooOO0OOO00o :
   OoOoO0ooooO0 = OoOoO0ooooO0
  IIII1ii1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( IIIIIo0ooOoO000oO ) )
  for OOO0O0OOo , O0O0Oo00 , time , Iii1 in IIII1ii1 :
   I1IIIiI1I1ii1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Iii1 )
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + OoOoO0ooooO0 + ' - ' + OOO0O0OOo + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + O0O0Oo00 , OO0o , ( str ( I1IIIiI1I1ii1 ) ) )
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
 for O0O0Oo00 , url , oO00oooOOoOo0 in IIi1I11I1II :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   IiIIi1 ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , O0O0Oo00 )
 for url , O0O0Oo00 , oO00oooOOoOo0 in OooOoooOo :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , O0O0Oo00 )
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
 for url , O0O0Oo00 , oO00oooOOoOo0 in OooOoooOo :
  ii1i1II11II1i = oO00oooOOoOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in oO00oooOOoOo0 :
   pass
  else :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']' + ii1i1II11II1i + '[/COLOR]' , url , 10013 , O0O0Oo00 )
   if 48 - 48: ooOOOoO * oO0o % ii1ii11IIIiiI - I11O0O0oOO00O00o
def Oo0000OOO0 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( IIIi1I1IIii1II )
 for oooOOoooo in IIi1I11I1II :
  Ooo0O0OO = ( oooOOoooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  oO00O0 ( 'http:' + Ooo0O0OO )
  if 38 - 38: ii1ii11IIIiiI
  if 25 - 25: iI11I1II1I1I % IIiIiII11i / I11O0O0oOO00O00o / Ii1I
  if 22 - 22: oO0oo0o * Ii1IIIi1
  if 4 - 4: OOooOOo - oO0oo0o + oOo0O0Ooo
def iiIiIiIiiIiI ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , url , 8046 , O0O0Oo00 )
 for url in OooOoooOo :
  IiIi1I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def iIi1i ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  oO00O0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / I11O0O0oOO00O00o + ii1ii11IIIiiI
def iIiII11 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 33 - 33: I11i * Ii1IIIi1 * iI11I1II1I1I + Ii . ii
def O0O0 ( ) :
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 IiIi1I1 ( '[COLOR' + iiI1IiI + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0ooo00o0o000Oo ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I1III1111iIi )
 for O0O0Oo00 , url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + O0O0Oo00 )
 for url in next :
  IiIi1I1 ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 100 - 100: ooOoO0O00 - Ii . ii1ii11IIIiiI * oO0o
  if 62 - 62: o0o00Oo0O
def iiIIIIiii ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   IiIIi1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   iiii1 ( 'http:' + url )
   if 22 - 22: iI11I1II1I1I * ii1ii11IIIiiI / I1ii11iIi11i
def iiii1 ( url ) :
 IiIIi1 ( ( '[COLOR' + iiI1IiI + ']Pick Quality[/COLOR]' ) . replace ( '&#039;s' , '' ) , '' , 222 , III1iII1I1ii + 'documentary.png' )
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  url = ( url ) . replace ( '\/' , '/' )
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: Ii
def O0O0O ( ) :
 I1III1111iIi = I1i111I ( 'http://documentarylovers.com/' )
 IIi1I11I1II = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  if 'genre' in i1I1ii11i1Iii :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , i1I1ii11i1Iii , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1io0Oo00oOO ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , O0O0Oo00 )
 for url in next :
  IiIi1I1 ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 73 - 73: I11O0O0oOO00O00o / ii . IIiIiII11i - ooOOOoO * O0OOOoOoo0 * ooOOOoO
def IiI1IiI1iiI1 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in OooOoooOo :
  iiii1 ( url )
  if 70 - 70: O00o0O00 + O0OOOoOoo0 * iI1ii11iIi1i . iI1ii11iIi1i + oO0o
def ii1O0Ooo0O ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOO0OOO = 'http://documentarylovers.com/?s=' + ( O00Ooo ) . replace ( ' ' , '+' )
 i1i1ii = OOOO0OOO . lower ( )
 II1io0Oo00oOO ( i1i1ii )
 if 18 - 18: ooOoO0O00
def i1i1Ii1IiIII ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'films' in url :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def I1IIii11 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1III1111iIi )
 for O0O0Oo00 , url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'films' in url :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + O0O0Oo00 )
 for url in OooOoooOo :
  IiIi1I1 ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def I1I1 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  if 'rtd' in url :
   O0OOO0ooO00o ( url )
   if 24 - 24: ii1ii11IIIiiI + ii . ooOOOoO / OOooOOo / I11O0O0oOO00O00o
def O0OOO0ooO00o ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I1III1111iIi )
 for OOO00O , file in IIi1I11I1II :
  url = ( 'https://rtd.rt.com' + OOO00O + file )
  oO00O0 ( url )
  if 65 - 65: ii
  if 18 - 18: o0o00Oo0O - ooOoO0O00 . ii1ii11IIIiiI
def o00OOo00 ( ) :
 IIIi1I1IIii1II = I1i111I ( 'http://www.stream2watch.co/live-tv' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 , oooOIi1I1iIIIiiii in IIi1I11I1II :
  IiIi1I1 ( ( oO00oooOOoOo0 + '[COLOR' + iiI1IiI + ']' + oooOIi1I1iIIIiiii + '[/COLOR]' ) , i1I1ii11i1Iii , 8086 , O0O0Oo00 )
  if 70 - 70: Ii1IIIi1 . IIiIiII11i . Ii1IIIi1 - iI11I1II1I1I
def ooOo0O0 ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8087 , O0O0Oo00 )
  if 83 - 83: ii
def iIIi111IiII1i ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  oOo0O000oo0 ( url , oO00oooOOoOo0 )
  if 15 - 15: I1ii11iIi11i / iI1ii11iIi1i % o0o00Oo0O + Ii1I
def oOo0O000oo0 ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  print url
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 96 - 96: O0OOOoOoo0 . ii
def i1I1I1I ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i1I1ii11i1Iii , 3002 , 'http://www.solie.org/alibrary/' + O0O0Oo00 )
def iII1III ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0O0Oo00 )
def O0oo0oO00o ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 I1ii111i1ii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1III1111iIi )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , oO00oooOOoOo0 in I1ii111i1ii1 :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']Season- ' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , O0O0Oo00 , oO00oooOOoOo0 in OooOoooOo :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + O0O0Oo00 )
def o0Ii11iIiiI ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  o000 ( url )
def o000 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oO00O0 ( url )
  if 30 - 30: iI1ii11iIi1i + IIiIiII11i % ii
def oOo000O00O0 ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classicmovies.png' )
def iI1iiIii1I11I ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( "v.src = '([^']*)';" ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oOOO00o000o ( url )
  if 32 - 32: ii % oO0oo0o % iI11I1II1I1I / o0o00Oo0O
def Oo ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i1I1ii11i1Iii , 8065 , III1iII1I1ii + 'classictv.png' )
def o0oOOoo0O ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  if 'mp4' in url :
   oO00O0 ( url )
 for url in OooOoooOo :
  yt . PlayVideo ( url )
  if 57 - 57: oOo0O0Ooo . Ii * IIiIiII11i + ii + iI1ii11iIi1i
def OoO0o0oOOO ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i1I1ii11i1Iii , 8071 , III1iII1I1ii + 'streams.png' )
def oO0I1I1i1I1I1I1 ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '(Free Access)' in oO00oooOOoOo0 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def iI11IiIiiII1 ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , oO00oooOOoOo0 , url in IIi1I11I1II :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + ooOoOoo0O + '/' + OooO0 + url ) . strip ( )
  iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , O0O0Oo00 , oOo0O , '' )
  if 15 - 15: O0OOOoOoo0 - o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / o0o00Oo0O
def IIi1Iii1I11iI ( ) :
 OOoOoo00Oo ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Genres' , 'http://www.xvideos.com' , 10106 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 OOoOoo00Oo ( 'Search' , '' , 10107 , III1iII1I1ii + 'Jizbox.png' , '' , '' , )
 if 85 - 85: O00o0O00 + IIiIiII11i - O00o0O00 * oO0oo0o - ooOoO0O00 % Ii1IIIi1
def IiIiI ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iI1Ii11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in iI1Ii11 :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , oOoOoOoo0 in IIi1I11I1II :
  OOoOoo00Oo ( ( oO00oooOOoOo0 + ' - No of Videos : ' + ( oOoOoOoo0 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 93 - 93: oOo0O0Ooo / O0OOOoOoo0 / I11O0O0oOO00O00o + IIiIiII11i + Ii
def iiiII1III ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 iI1Ii11 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in iI1Ii11 :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , url , oO00oooOOoOo0 , i111i11I1ii in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + '--' + i111i11I1ii , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( O0O0Oo00 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 6 - 6: O00o0O00 * oO0oo0o / o0o00Oo0O . IIiIiII11i + ooOOOoO % I11i
  if 67 - 67: o0o00Oo0O % ii1ii11IIIiiI
def III ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , url , oO00oooOOoOo0 , oO0Ooooooo , I1I in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + ' - Porn Quality : ' + I1I + ' - ' + oO0Ooooooo , 'http://www.xvideos.com' + url , 10108 , O0O0Oo00 , O0O0Oo00 , I1I + ' - ' + oO0Ooooooo )
 o0oOo0000ooO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for url in o0oOo0000ooO :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 15 - 15: O0OOOoOoo0 . I11i + OOooOOo . iI11I1II1I1I % O0OOOoOoo0 + o0o00Oo0O
def IIiII11 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIIIIo0ooOoO000oO = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 iI1Ii11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( IIIi1I1IIii1II )
 for url in iI1Ii11 :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( IIIIIo0ooOoO000oO ) )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 58 - 58: Ii1IIIi1
  if 2 - 2: ooOOOoO - oO0oo0o % oO0o + I11i + iI1ii11iIi1i - iI11I1II1I1I
def iIII ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0000 = ( O00Ooo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1i1ii = OoO0000 . lower ( )
 oOO0o0oo0 = 'http://www.xvideos.com/?k=' + i1i1ii
 print oOO0o0oo0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 , oO0Ooooooo , I1I in IIi1I11I1II :
  OOoOoo00Oo ( oO00oooOOoOo0 + ' - Porn Quality : ' + I1I + ' - ' + oO0Ooooooo , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10108 , O0O0Oo00 , O0O0Oo00 , I1I + ' - ' + oO0Ooooooo )
 o0oOo0000ooO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in o0oOo0000ooO :
  OOoOoo00Oo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i1I1ii11i1Iii , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 11 - 11: oO0o - iI1ii11iIi1i + o0o00Oo0O * oO0o
def oOoOO ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 OooOoooOo = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 I1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'http' in url :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']LOW[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in OooOoooOo :
  if 'http' in url :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']HIGH[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in I1 :
  if 'http' in url :
   IiIIi1 ( '[COLOR' + iiI1IiI + ']HLS[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 20 - 20: O0OOOoOoo0 . oO0o * Ii1IIIi1
def OOii11Ii1IiiI1 ( url ) :
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
 import urlresolver
 try : II1III1i1iiI . play ( url )
 except : pass
 if 65 - 65: Ii1I % oO0oo0o . ii * I11i * oO0o
 if 10 - 10: oO0oo0o - Ii1IIIi1 % IIiIiII11i - ii1ii11IIIiiI - ooOoO0O00
def iIi11iI1i ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 8091 , III1iII1I1ii + 'gofish.png' )
def Ii1iIi ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1092 , O0O0Oo00 )
 for url in next :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def OOo0OOOoOOo ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 8092 , O0O0Oo00 )
 for url in next :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 8091 , III1iII1I1ii + 'Next.png' )
def IIIooo0o0O ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( "videoId: '([^']*)'," ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  yt . PlayVideo ( url )
  if 32 - 32: ii % ii . oO0oo0o - O0OOOoOoo0 . OOooOOo * oO0oo0o
  if 55 - 55: I11O0O0oOO00O00o
  if 93 - 93: Ii . I11i
IiiIiI1IIi1IIIii = '{PQ},' ; OOO0o = '{SC},' ; O0O00OO = '{XG},' ; IIiiiI = '{JP},' ; oO0Oooo0OoO = '{HW},' ; Iiii1IIIIiiI11 = '{RT},'
def I1iii1I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oooII111 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 29 - 29: ooOOOoO + Ii * o0o00Oo0O - Ii1IIIi1 . IIiIiII11i % iI1ii11iIi1i
 iIi11i1 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 III1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 OOOii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Iii1I11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0o0o = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O00Ooo
 IiiiIi1111I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iII1i1ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i1I1ii1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iiiiII11iIi = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 51 - 51: I1ii11iIi11i / ooOOOoO * iI1ii11iIi1i - IIiIiII11i / oOo0O0Ooo . ooOOOoO
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 65 - 65: ooOOOoO
 if 75 - 75: ii * Ii
 ii1ii1ii = ooOooo000oOO ( iIi11i1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( III1I )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 o0oOo = ooOooo000oOO ( OOOii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 OoIIiIIIII1I = ooOooo000oOO ( O0o0o )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooiiI = ooOooo000oOO ( IiiiIi1111I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 o00iIiI1iI1Ii1 = ooOooo000oOO ( iII1i1ii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 iioO = ooOooo000oOO ( i1I1ii1i )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ii11I = ooOooo000oOO ( iiiiII11iIi )
 if 97 - 97: ooOoO0O00 + Ii1IIIi1 . O0OOOoOoo0 - Ii1IIIi1
 if 53 - 53: o0o00Oo0O . oOo0O0Ooo
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
  for o0oOOoO000 , oO00oooOOoOo0 in IIi1I11I1II :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i1I1ii11i1Iii + o0oOOoO000 ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 86 - 86: iI11I1II1I1I - I11O0O0oOO00O00o % O0OOOoOoo0 . O00o0O00 * OOooOOo . ooOoO0O00
    if 75 - 75: I11O0O0oOO00O00o + O0OOOoOoo0 / O0OOOoOoo0 - O00o0O00 * oO0o * O0OOOoOoo0
    if 53 - 53: ooOOOoO % I1ii11iIi11i
    if 42 - 42: Ii / oOo0O0Ooo - oO0o - O0OOOoOoo0 + IIiIiII11i % O0OOOoOoo0
    if 50 - 50: ii + oO0oo0o * oOo0O0Ooo - iI1ii11iIi1i / Ii
    if 5 - 5: o0o00Oo0O - oOo0O0Ooo
    if 44 - 44: IIiIiII11i . IIiIiII11i + O00o0O00 * iI1ii11iIi1i
 if ii1ii1ii != 'Failed' :
  I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for o0oOOoO000 , oO00oooOOoOo0 in I1 :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIi11i1 + o0oOOoO000 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  i1iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in i1iIi :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 22 - 22: Ii1IIIi1 + oO0o - O0OOOoOoo0
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if o0oOo != 'Failed' :
  iiI1i = [ ]
  OoOoIII1IiIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0oOo )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in OoOoIII1IiIi1 :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    if oO00oooOOoOo0 in iiI1i :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i1I1ii11i1Iii , 1016 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
     iiI1i . append ( oO00oooOOoOo0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if OoIIiIIIII1I != 'Failed' :
  oOOoO0O = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OoIIiIIIII1I )
  for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in oOOoO0O :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i1I1ii11i1Iii , 7067 , O0O0Oo00 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 76 - 76: ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ooiiI != 'Failed' :
  oo00Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooiiI )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oo00Oo :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Redemption[/COLOR]' ) , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + I11O0O0oOO00O00o . O00o0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if o00iIiI1iI1Ii1 != 'Failed' :
  oo0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00iIiI1iI1Ii1 )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oo0O :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 23 - 23: oOo0O0Ooo * O0OOOoOoo0 / OOooOOo . iI11I1II1I1I % Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if iioO != 'Failed' :
  ooO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iioO )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in ooO :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    iIiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Herovision[/COLOR]' ) , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 84 - 84: iI11I1II1I1I . O0OOOoOoo0 + Ii1IIIi1
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 85 - 85: O00o0O00 % oO0oo0o * oO0oo0o + ii
 if ii11I != 'Failed' :
  O0OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ii11I )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO00oooOOoOo0 in O0OO :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Silent Hunter[/COLOR]' ) , i1I1ii11i1Iii , 222 , oOoooo000Oo00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 30 - 30: OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 iI1iIIiii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 46 - 46: oOo0O0Ooo . ooOOOoO - Ii - ii1ii11IIIiiI
 for oo000o in iI1iIIiii :
  OO00o0oOO = I11i1I1I + oo000o + IIIII
  oo0O0OO0Oo = ooOooo000oOO ( OO00o0oOO )
  if oo0O0OO0Oo != 'Failed' :
   oO00o0oO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O0OO0Oo )
   for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oO00o0oO0O :
    if O00Ooo in oO00oooOOoOo0 . lower ( ) :
     iIiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , 222 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 38 - 38: Ii1I - iI1ii11iIi1i * I11i
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 13 - 13: oOo0O0Ooo * oO0oo0o
 iI1iIIiii = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 41 - 41: ooOOOoO
 if 16 - 16: iI11I1II1I1I
 for oo000o in iI1iIIiii :
  OO00o0oOO = oooII111 + oo000o
  o000o0o00Oo = ooOooo000oOO ( OO00o0oOO )
  if o000o0o00Oo != 'Failed' :
   oo0O00o0O0Oo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o000o0o00Oo )
   for o0oOOoO000 , oO00oooOOoOo0 in oo0O00o0O0Oo :
    if O00Ooo in oO00oooOOoOo0 . lower ( ) :
     IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oooII111 + oo000o + o0oOOoO000 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 26 - 26: ooOoO0O00 / Ii1IIIi1 . Ii1IIIi1
     I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
     if 20 - 20: O00o0O00 - Ii1IIIi1 / I1ii11iIi11i * oO0o
     if 55 - 55: ii
def OO0OOOOOo ( ) :
 if 7 - 7: o0o00Oo0O + iI1ii11iIi1i . IIiIiII11i
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 if 12 - 12: oOo0O0Ooo - ooOoO0O00
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( O00Ooo ) . replace ( ' ' , '%20' )
 I1i11 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 iIi11i1 = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 III1I = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OOOii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i1i1ii ) . replace ( ' ' , '+' )
 Iii1I11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0o0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 IiiiIi1111I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 95 - 95: I11O0O0oOO00O00o / ooOOOoO . o0o00Oo0O * ooOOOoO - I11i * I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / iI1ii11iIi1i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 O0 = ooOooo000oOO ( I1i11 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ii1ii1ii = ooOooo000oOO ( iIi11i1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 oooooOoo0ooo = ooOooo000oOO ( III1I )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0oOo = cloudflare . source ( OOOii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o000o0o00Oo = ooOooo000oOO ( Iii1I11 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OoIIiIIIII1I = ooOooo000oOO ( O0o0o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 ooiiI = ooOooo000oOO ( IiiiIi1111I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 14 - 14: ii1ii11IIIiiI % ooOOOoO - o0o00Oo0O / ii1ii11IIIiiI
 if ooiiI != 'Failed' :
  oo00Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooiiI )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oo00Oo :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source HeroVision[/COLOR]' ) , i1I1ii11i1Iii , 1016 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 91 - 91: Ii % ii1ii11IIIiiI * oO0oo0o - Ii1I . ii1ii11IIIiiI
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 28 - 28: Ii
 if OoIIiIIIII1I != 'Failed' :
  oOOoO0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoIIiIIIII1I )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oOOoO0O :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- source Reaper[/COLOR]' ) , i1I1ii11i1Iii , 1016 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 51 - 51: oOo0O0Ooo + O0OOOoOoo0 * o0o00Oo0O . iI1ii11iIi1i
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: O00o0O00 * Ii1I % iI1ii11iIi1i . O00o0O00
    if 43 - 43: oO0o . O0OOOoOoo0 * I1ii11iIi11i
    if 20 - 20: ooOoO0O00 . ooOoO0O00 - I11O0O0oOO00O00o
    if 89 - 89: O0OOOoOoo0 - I11O0O0oOO00O00o . o0o00Oo0O % ii . Ii
    if 35 - 35: IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
    if 55 - 55: I1ii11iIi11i % ooOoO0O00 * I11O0O0oOO00O00o
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 95 - 95: O00o0O00 / IIiIiII11i - I11i % ii1ii11IIIiiI . I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for O0O0Oo00 , i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + i1I1ii11i1Iii , 10044 , O0O0Oo00 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 63 - 63: iI11I1II1I1I / O0OOOoOoo0
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % O00o0O00 * OOooOOo - iI11I1II1I1I
    if 50 - 50: IIiIiII11i
    if 39 - 39: IIiIiII11i . OOooOOo - I1ii11iIi11i * ooOoO0O00 . ii
    if 44 - 44: oOo0O0Ooo
    if 55 - 55: oO0oo0o . ii1ii11IIIiiI * ii1ii11IIIiiI
    if 82 - 82: oOo0O0Ooo % oO0o % I11O0O0oOO00O00o + I11O0O0oOO00O00o
    if 6 - 6: I1ii11iIi11i
    if 73 - 73: ii1ii11IIIiiI * Ii1I + I11i - I1ii11iIi11i . I11O0O0oOO00O00o
    if 93 - 93: Ii
    if 80 - 80: ooOoO0O00 . oOo0O0Ooo - oO0oo0o + O00o0O00 + Ii1IIIi1 % oO0oo0o
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in OooOoooOo :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , i1I1ii11i1Iii , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 13 - 13: IIiIiII11i / OOooOOo / OOooOOo + O0OOOoOoo0
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in I1 :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIi11i1 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % ooOOOoO
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  i1iIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for oO00oooOOoOo0 in i1iIi :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( III1I + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 13 - 13: oO0oo0o . iI11I1II1I1I . O00o0O00 . ooOOOoO
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if o0oOo != 'Failed' :
  OoOoIII1IiIi1 = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0oOo )
  for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in OoOoIII1IiIi1 :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source - Dizi[/COLOR]' , i1I1ii11i1Iii , 8062 , O0O0Oo00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 58 - 58: I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if o000o0o00Oo != 'Failed' :
  oo0O00o0O0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o000o0o00Oo )
  for i1I1ii11i1Iii , oOoooo000Oo00 , oO000oOo00o0o , oo0OoOO0o0o , oO00oooOOoOo0 in oo0O00o0O0Oo :
   if i1i1ii in oO00oooOOoOo0 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '- Source Scooby[/COLOR]' ) , i1I1ii11i1Iii , 1016 , oOoooo000Oo00 , oo0OoOO0o0o , oO000oOo00o0o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 7 - 7: IIiIiII11i / ooOOOoO % I11O0O0oOO00O00o + oOo0O0Ooo - o0o00Oo0O
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: oOo0O0Ooo / Ii1IIIi1 + oO0oo0o + ooOOOoO
 iIIII1Iii11 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if o000o0o00Oo != 'Failed' :
  for oo000o in iIIII1Iii11 :
   OO00o0oOO = I11i1I1I + oo000o + IIIII
   iioO = O0i1II1Iiii1I11 ( OO00o0oOO )
   if iioO != 'Failed' :
    ooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iioO )
    for oO00oooOOoOo0 , oO000oOo00o0o , i1I1ii11i1Iii , O0O0Oo00 , oOo0O , oO0oo0o00o0O in ooO :
     if i1i1ii in oO00oooOOoOo0 . lower ( ) :
      I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' - Source Pandoras[/COLOR]' , i1I1ii11i1Iii , oO0oo0o00o0O , O0O0Oo00 , oOo0O , oO000oOo00o0o )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 3 - 3: I11i % I11i % oOo0O0Ooo - ooOoO0O00
      I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
      if 84 - 84: I11O0O0oOO00O00o
      if 39 - 39: o0o00Oo0O . ooOoO0O00 * Ii1I - oO0o - Ii1IIIi1 % I11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIi1iii1 ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( O00Ooo ) . replace ( ' ' , '+' )
 if 37 - 37: iI11I1II1I1I % I11O0O0oOO00O00o / ooOOOoO
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 37 - 37: ii1ii11IIIiiI - oO0oo0o - oO0o
 if IIIi1I1IIii1II != 'Failed' :
  OooOoooOo = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIIi1 ( ( oO00oooOOoOo0 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + i1I1ii11i1Iii ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 42 - 42: iI11I1II1I1I % iI1ii11iIi1i - Ii1I + iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
iiI1I = '{ZH},' ; O0oooO00ooO0 = '{IX},' ; o00OOO0o00OO = '{LM},'
if 100 - 100: I11O0O0oOO00O00o
def iI1iIi ( url ) :
 I1i1IIIIIII1 = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( I1i1IIIIIII1 )
 for url , O0oo00oOOO0o , Ii111iIi1iIi , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( O0oo00oOOO0o ) . replace ( 'Sezon' , ' Season ' ) + ( Ii111iIi1iIi ) . replace ( 'Bölüm' , ' Episode ' ) + oO00oooOOoOo0 , url , 8063 , '' )
  if 10 - 10: Ii1I + ooOOOoO
  if 58 - 58: oOo0O0Ooo + ii / Ii1IIIi1 . O0OOOoOoo0 % I11i / Ii1I
  if 62 - 62: IIiIiII11i
  if 12 - 12: ooOOOoO + IIiIiII11i
def O0Ooo00o00O ( url ) :
 I1i1IIIIIII1 = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( I1i1IIIIIII1 )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , url , 222 , '' )
  if 80 - 80: Ii1IIIi1
  if 3 - 3: Ii1I * I11O0O0oOO00O00o
  if 53 - 53: iI11I1II1I1I / Ii1IIIi1 % oO0o + ooOOOoO / O0OOOoOoo0
  if 74 - 74: I1ii11iIi11i
def IiIiII11i1 ( ) :
 if 44 - 44: oOo0O0Ooo % O00o0O00 * Ii * Ii - I1ii11iIi11i . ii1ii11IIIiiI
 I1i1IIIIIII1 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi1I11I1II = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i1IIIIIII1 )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 , Ii111iIi1iIi in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 + '  -  ' + ( Ii111iIi1iIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i1I1ii11i1Iii , 8063 , O0O0Oo00 )
  if 68 - 68: Ii1IIIi1 . I11O0O0oOO00O00o
def i111iiIiiIiI ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 8002 , O0O0Oo00 )
def OOooooO ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1III1111iIi )
 for O0O0Oo00 , time , url , oO00oooOOoOo0 , I11iII in IIi1I11I1II :
  I1IIII1i ( '%s %s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , time ) , url , 1015 , O0O0Oo00 , I11iII )
  if 80 - 80: OOooOOo + iI11I1II1I1I . ooOOOoO
def ooOoOoo000O0O ( ) :
 if 42 - 42: I11i / ooOOOoO
 IiIi1I1 ( 'Coronation Street' , '' , 8001 , '' )
 IiIi1I1 ( 'Eastenders' , '' , 8002 , '' )
 IiIi1I1 ( 'Emmerdale' , '' , 8003 , '' )
 IiIi1I1 ( 'Hollyoaks' , '' , 8004 , '' )
 IiIi1I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 79 - 79: iI1ii11iIi1i
 if 27 - 27: oO0o + I1ii11iIi11i
 if 92 - 92: oOo0O0Ooo % Ii1IIIi1
 if 31 - 31: ii - oO0oo0o / ii1ii11IIIiiI
def oo00o000O ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Holly' in oO00oooOOoOo0 :
   O0O0Oo00 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i1I1ii11i1Iii :
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , O0O0Oo00 )
   else :
    pass
    if 66 - 66: ii + I11i . ooOoO0O00 * Ii1IIIi1
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 92 - 92: I11O0O0oOO00O00o / ii1ii11IIIiiI
def iiIIiii1iii1I ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'East' in oO00oooOOoOo0 :
   O0O0Oo00 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i1I1ii11i1Iii :
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , O0O0Oo00 )
   else :
    pass
    if 14 - 14: o0o00Oo0O / I11O0O0oOO00O00o . oO0o % Ii1IIIi1 . oO0oo0o
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def Iii1II1 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Emmer' in oO00oooOOoOo0 :
   O0O0Oo00 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i1I1ii11i1Iii :
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , O0O0Oo00 )
   else :
    pass
    if 54 - 54: OOooOOo . I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: ooOoO0O00 . I1ii11iIi11i * I1ii11iIi11i / Ii1I
def o0oo0OooOO0 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Coro' in oO00oooOOoOo0 :
   O0O0Oo00 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i1I1ii11i1Iii :
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , O0O0Oo00 )
   else :
    pass
    if 57 - 57: IIiIiII11i % oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: oOo0O0Ooo
def o0OoOo0O00 ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Celeb' in oO00oooOOoOo0 :
   O0O0Oo00 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i1I1ii11i1Iii :
    IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i1I1ii11i1Iii . replace ( '\\/' , '/' ) , 8006 , O0O0Oo00 )
   else :
    pass
    if 9 - 9: O00o0O00
def I1iII ( name , url ) :
 I1IIiIi = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if I1IIiIi :
  OOOOoOoO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1III1111iIi = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I1III1111iIi ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1III1111iIi = open_url ( url )
  OO000 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I1III1111iIi ) [ - 1 ]
  OOOOoOoO = OO000 . replace ( '\\/' , '/' )
 ooooOoo0OO = xbmcgui . ListItem ( name , '' , '' )
 ooooOoo0OO . setPath ( OOOOoOoO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooooOoo0OO )
 if 86 - 86: I11i
 if 83 - 83: oO0o
def iii1IiiIiIIiI ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi1I11I1II = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in OooOoooOo :
  IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i1I1ii11i1Iii , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 93 - 93: ooOOOoO % Ii1I
def IiIIii ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Movies' in oO00oooOOoOo0 :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( i1I1ii11i1Iii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def oo0O0Ii111Ii11 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1III1111iIi )
 IIi1I11I1II = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0O0Oo00 )
 for url in OooOoooOo :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - O00o0O00
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def O00000OO00OO ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url , O0O0Oo00 in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , O0O0Oo00 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
iI11iI = '{UJ},' ; Oo0oOO = '{WE},' ; iIi = '{WP},' ; OoiiI11111II = '{PP},'
def I1ii1i11iI1 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url , O0O0Oo00 in IIi1I11I1II :
  if '{{' in oO00oooOOoOo0 :
   pass
  else :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , O0O0Oo00 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiOOo0 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  o0O0O0O00o ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O0O0O00o ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
 if 75 - 75: IIiIiII11i . oOo0O0Ooo + O00o0O00 - OOooOOo - o0o00Oo0O . I11O0O0oOO00O00o
 if 19 - 19: iI1ii11iIi1i * ooOoO0O00 % o0o00Oo0O + I11O0O0oOO00O00o
def I1i1ii1ii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  if '(cooltvseries.com)' in oO00oooOOoOo0 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def i1ii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oO00O0 ( ( url ) . replace ( ' ' , '%20' ) )
oOOOOO0 = '{XX},' ; IIi1I1 = '{UD},' ; oO00o0oOoo = '{YT},' ; oOOI1 = '{JS},' ; OOI1i = '{PF},'
if 47 - 47: Ii1IIIi1 . OOooOOo
def o0oOO0 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIIi1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( i1I1ii11i1Iii ) ) , 222 , O0O0Oo00 )
  if 31 - 31: iI1ii11iIi1i * I11i * iI1ii11iIi1i + oO0o * I11i . ii1ii11IIIiiI
def Oo00oo00o00Oo ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1III1111iIi )
 for O0O0Oo00 , url , oO00oooOOoOo0 in IIi1I11I1II :
  if 'youtu' in url :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + O0O0Oo00 )
 for url in next :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 1 - 1: ooOOOoO
def iiiiOOOO00 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 92 - 92: I11O0O0oOO00O00o % o0o00Oo0O % iI1ii11iIi1i . iI1ii11iIi1i . ooOOOoO
def OOoO0Oo ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11
 IIi1I11I1II = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 222 , O0O0Oo00 )
  if 61 - 61: oOo0O0Ooo + oO0oo0o % ii1ii11IIIiiI % iI11I1II1I1I - ii
  if 22 - 22: O00o0O00 + IIiIiII11i + I1ii11iIi11i
  if 83 - 83: O0OOOoOoo0
  if 43 - 43: O00o0O00
  if 84 - 84: O00o0O00 . ooOOOoO . Ii1IIIi1
def iIII1I1i ( ) :
 if 26 - 26: Ii1IIIi1 - I1ii11iIi11i + oOo0O0Ooo + I11i
 IiIi1I1 ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiIi1I1 ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 37 - 37: I11i * O00o0O00 + oOo0O0Ooo . Ii1I * ii
 if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + O00o0O00 * IIiIiII11i
def iIiIiiIIIi1 ( Cat_Name ) :
 if 25 - 25: o0o00Oo0O
 Oo00o00 = False
 OoOo0O0 = '0'
 if Cat_Name == 'All Channels' : Oo00o00 = True
 if Cat_Name == 'Entertainment' : OoOo0O0 = '1'
 if Cat_Name == 'Movies' : OoOo0O0 = '2'
 if Cat_Name == 'Music' : OoOo0O0 = '3'
 if Cat_Name == 'News' : OoOo0O0 = '4'
 if Cat_Name == 'Sports' : OoOo0O0 = '5'
 if Cat_Name == 'Documentary' : OoOo0O0 = '6'
 if Cat_Name == 'Kids' : OoOo0O0 = '7'
 if Cat_Name == 'Food' : OoOo0O0 = '8'
 if Cat_Name == 'Religious' : OoOo0O0 = '9'
 if Cat_Name == 'USA Channels' : OoOo0O0 = '10'
 if Cat_Name == 'Other' : OoOo0O0 = '11'
 if 39 - 39: ii1ii11IIIiiI . oO0o % O0OOOoOoo0 . O00o0O00 / Ii1IIIi1 * oO0o
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1III1111iIi )
 print 'Len Match: >>>' + str ( len ( IIi1I11I1II ) )
 for oO00oooOOoOo0 , O0O0Oo00 , iiI1io0O00o0 in IIi1I11I1II :
  OoOoOooO0o = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0O0Oo00 ) . replace ( '\\' , '' )
  if iiI1io0O00o0 == OoOo0O0 :
   IiIi1I1 ( oO00oooOOoOo0 , '' , 7022 , OoOoOooO0o )
  elif Oo00o00 == True :
   IiIi1I1 ( oO00oooOOoOo0 , '' , 7022 , OoOoOooO0o )
  else : pass
  if 23 - 23: oOo0O0Ooo
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 7 - 7: Ii1IIIi1 % Ii1I
def o0oOOO ( Search_Name ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1III1111iIi )
 IIi1I11I1II = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1III1111iIi )
 for O0O0Oo00 , i1I1ii11i1Iii , I1i11 , iIi11i1 in IIi1I11I1II :
  OoOoOooO0o = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( O0O0Oo00 ) . replace ( '\\' , '' )
  IiIIi1 ( Search_Name + ': Link 1' , ( i1I1ii11i1Iii ) . replace ( '\\' , '' ) , 222 , OoOoOooO0o )
  IiIIi1 ( Search_Name + ': Link 2' , ( I1i11 ) . replace ( '\\' , '' ) , 222 , OoOoOooO0o )
  IiIIi1 ( Search_Name + ': Link 3' , ( iIi11i1 ) . replace ( '\\' , '' ) , 222 , OoOoOooO0o )
  if 47 - 47: O00o0O00 / IIiIiII11i % ooOOOoO . oO0oo0o * Ii1I
def iIii1iIiII1i1 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def o0oO ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def o0OoIII1IIiIi1 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , i1I1ii11i1Iii in IIi1I11I1II :
  IiIIi1 ( oO00oooOOoOo0 , ( i1I1ii11i1Iii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 97 - 97: I11i / ooOOOoO + OOooOOo + oO0o % ii1ii11IIIiiI
def iIIi1II1 ( url ) :
 url
 ooOOo0o = xbmcgui . ListItem ( oO00oooOOoOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooOOo0o )
 return
 if 42 - 42: iI11I1II1I1I - O0OOOoOoo0 - I11O0O0oOO00O00o - ii1ii11IIIiiI
 if 33 - 33: OOooOOo - o0o00Oo0O
def III11iI1i11i ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1III1111iIi )
 for url , oO000oOo00o0o , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + O0O0Oo00 , '' , ( oO000oOo00o0o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 for url in OooOoooOo :
  IiIi1I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 30 - 30: OOooOOo / oO0oo0o / iI1ii11iIi1i * I11i * oO0oo0o . oOo0O0Ooo
def o0oo000 ( url ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for url , oO000oOo00o0o , O0O0Oo00 in IIi1I11I1II :
  iIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + O0O0Oo00 , '' , oO000oOo00o0o )
  I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 O0Oo0iI1II1III1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for oo0o0OO in O0Oo0iI1II1III1 :
  iiI11I1III = ( oo0o0OO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + O0O0Oo00 , '' , iiI11I1III )
  if 13 - 13: IIiIiII11i
def OoOIiiIi1IiiiI ( INFO ) :
 O0O0Oooo0o ( 'info for workout' , INFO )
 if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 if 95 - 95: oO0oo0o
 if 48 - 48: I11O0O0oOO00O00o / iI11I1II1I1I % IIiIiII11i
def IiI111I ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'Name=(.+?)\n.+?m3u=(.+?)\n' , re . DOTALL ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  IiIi1I1 ( ( oO00oooOOoOo0 ) . replace ( 'SlyNet' , '' ) , url , 9032 , III1iII1I1ii + 'Sport.png' )
def oo0oO0 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , url , 9032 , III1iII1I1ii + 'icon.png' )
def ii1i1Iii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:-.+?,(.+?)\n(.+?)\n' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   IiIIi1 ( ( oO00oooOOoOo0 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def IIII11111Ii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  if '=' in oO00oooOOoOo0 :
   pass
  else :
   IiIIi1 ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'icon.png' )
   if 21 - 21: o0o00Oo0O + o0o00Oo0O / I11i - I11O0O0oOO00O00o
   if 88 - 88: Ii1I . IIiIiII11i / O00o0O00 % ooOoO0O00 - OOooOOo % Ii
   if 61 - 61: ii . o0o00Oo0O % I11i * o0o00Oo0O
   if 23 - 23: OOooOOo - iI1ii11iIi1i - oO0oo0o / ii
   if 12 - 12: ii
def oOO0o00 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( i11 ( 'aHR0cDovL3NvdXJjZXR2LmluZm8v' ) )
 IIi1I11I1II = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 9008 , III1iII1I1ii + 'disclose.png' )
def IIi1IIiII ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="article-image darken"><a href="([^"]*)"><img width="320" height="205" src="([^"]*)".+?title="([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , url , 9009 , O0O0Oo00 )
def oooOoO00Oo0O ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  IiIIi1 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 17 - 17: oO0o
def IIIi11i ( ) :
 I1III1111iIi = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if '.m3u' in i1I1ii11i1Iii :
   IiIi1I1 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + i1I1ii11i1Iii ) , 9011 , III1iII1I1ii + 'disclose.png' )
def oooOOoo0 ( url ) :
 I1III1111iIi = cloudflare . source ( url )
 IIi1I11I1II = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  IiIIi1 ( ( oO00oooOOoOo0 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 79 - 79: ii - O0OOOoOoo0 * iI1ii11iIi1i - IIiIiII11i % OOooOOo * ooOOOoO
def iI1III ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  if 'category' in i1I1ii11i1Iii :
   IiIi1I1 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + i1I1ii11i1Iii , 7010 , III1iII1I1ii + 'disclose.png' )
   if 42 - 42: O0OOOoOoo0 + Ii1IIIi1 + iI1ii11iIi1i * I11O0O0oOO00O00o . ooOoO0O00
   if 72 - 72: oOo0O0Ooo + iI1ii11iIi1i
def IiI1 ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1III1111iIi )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 , O0O0Oo00 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , 'http://www.disclose.tv/' + url , 7011 , O0O0Oo00 )
 for url in next :
  IiIi1I1 ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 11 - 11: OOooOOo / I11O0O0oOO00O00o
  if 47 - 47: O00o0O00 . ii1ii11IIIiiI % IIiIiII11i + I1ii11iIi11i - oO0oo0o . IIiIiII11i
def Ii1Iiiiii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1III1111iIi )
 I1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  if 'http' in url :
   IiIIi1 ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , oO00oooOOoOo0 in OooOoooOo :
  IiIIi1 ( oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in I1 :
  IiIIi1 ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 25 - 25: IIiIiII11i % IIiIiII11i - iI1ii11iIi1i . o0o00Oo0O
  if 79 - 79: ooOOOoO / oO0o * ii * OOooOOo + oOo0O0Ooo
def O0ooO ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 40 - 40: I11i . I11i * Ii
def i11III1I ( name , url , img ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 O00o0O00oO00O = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 II11Ii = len ( O00o0O00oO00O )
 if 58 - 58: Ii1IIIi1
 if 2 - 2: IIiIiII11i + ooOoO0O00
 if II11Ii == 1 :
  for oO0OO00 in O00o0O00oO00O :
   oO0OO00 = oO0OO00 . replace ( 'player' , 'watch' )
   IiiI = oO0OO00 + '&fv=&sou='
   O0oooooO = O0i1II1Iiii1I11 ( IiiI )
   IIi1 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O0oooooO )
   for III1ii in IIi1 :
    II11II = False
    Resolve ( III1ii )
    if 40 - 40: Ii1IIIi1 + o0o00Oo0O
 elif II11Ii > 1 :
  if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % oO0oo0o + oOo0O0Ooo % O0OOOoOoo0 / iI1ii11iIi1i
  for oO0OO00 in O00o0O00oO00O :
   iIioO00O0o0oOOO = O0i1II1Iiii1I11 ( oO0OO00 )
   ooooOoo00 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iIioO00O0o0oOOO )
   IIIIii1111i1 = ooooOoo00
   IIIIii1111i1 = ( str ( IIIIii1111i1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIIIii1111i1
   IiIIi1 ( 'DOUBLE LINK' , IIIIii1111i1 , 424 , '' )
   if 11 - 11: OOooOOo
   for url in ooooOoo00 :
    IiIi1I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1i11 = Google . resolve ( url )
    except :
     pass
    try :
     Iii1i1i11iII = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1i11 ) )
     for o0II1 , OOOiiIII1I11iii in Iii1i1i11iII :
      if 95 - 95: o0o00Oo0O . oO0o
      HD_URLS . append ( o0II1 )
      SD_URLS . append ( OOOiiIII1I11iii )
    except :
     pass
 else :
  pass
  if 89 - 89: ooOoO0O00
def I11II ( ) :
 if 89 - 89: oO0o . Ii1I - Ii * I1ii11iIi11i * Ii
 if 20 - 20: Ii . iI1ii11iIi1i
 IiIi1I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 17 - 17: OOooOOo - oOo0O0Ooo
 IiIi1I1 ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 63 - 63: OOooOOo - oO0oo0o / iI11I1II1I1I - iI1ii11iIi1i / ii1ii11IIIiiI
 if 34 - 34: Ii1IIIi1 / I11i + O00o0O00 - I11i + I1ii11iIi11i . oO0oo0o
def oOoOII1i1 ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( 'http://cnfstudio.com/' )
 IIi1I11I1II = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , 'http://cnfstudio.com/genre/' + i1I1ii11i1Iii , 7003 , III1iII1I1ii + 'icon.png' )
  if 51 - 51: O0OOOoOoo0 * Ii1IIIi1 / ooOoO0O00
iI111I11I1I1 = xbmcgui . Dialog ( )
if 2 - 2: oO0oo0o + ooOOOoO . Ii1IIIi1 - ooOoO0O00 + ii1ii11IIIiiI
ooOOo0O0o00o00 = '{UN},' ; o0oI1I1i = '{IG},' ; i111i1IIi1i = '{PL},' ; oo00oO00oooo = '{LO},' ; ooo0Oo00O = '{LP},' ; I1iII1 = '{HA},' ; Ooo0OOO0O00 = '{XD},' ; Ii1iiII11ii1 = '{TA},' ; iIi11I1II = '{DP},' ; oO00Oo0O0 = '{JT},' ; o0O00O = '{JJ},' ; OO00oOo0o00 = '{MM},' ; O0O0o = '{FQ},' ; i1i1i1Ii111II = '{HH},'
if 74 - 74: Ii1IIIi1 / I11O0O0oOO00O00o . oOo0O0Ooo - ii + IIiIiII11i + I11O0O0oOO00O00o
def I11iiI11I1II ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1III1111iIi )
 oO0iII1i111iI = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1III1111iIi )
 for O0O0Oo00 , url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , O0O0Oo00 )
 oO0iII1i111iI = oO0iII1i111iI
 for url in oO0iII1i111iI :
  IiIi1I1 ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 9 - 9: Ii + O00o0O00 - OOooOOo / O0OOOoOoo0 % ooOoO0O00 / oO0oo0o
def iiI1 ( url ) :
 if 42 - 42: oO0o - Ii1I * ooOOOoO - O0OOOoOoo0
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  OOO00O = url + '&fv=&sou='
  OOO00O = OOO00O . replace ( 'player' , 'watch' )
  O0oO00oO0o00o = o0OOo0O00OO0O ( OOO00O )
  oOO0oOOoO = o0OOo0O00OO0O ( url )
  if 87 - 87: O00o0O00
  if 7 - 7: ii1ii11IIIiiI - I11O0O0oOO00O00o % I11O0O0oOO00O00o + O0OOOoOoo0 * ooOoO0O00
def o0OOo0O00OO0O ( url ) :
 if 46 - 46: oOo0O0Ooo % ooOOOoO - iI11I1II1I1I * I11i
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  oOOO00o000o ( url )
  if 69 - 69: oO0oo0o . I11O0O0oOO00O00o
  if 36 - 36: O0OOOoOoo0
def O0oO0ooOOo ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Local M3u[/COLOR]' , O0OoO000O0OO , 2001 , III1iII1I1ii + 'LocalM3U.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']Remote M3u[/COLOR]' , oOOoO0 , 7080 , III1iII1I1ii + 'RemoteM3U.png' , OO0o , '' )
 if 9 - 9: ii1ii11IIIiiI - oO0o + iI11I1II1I1I % o0o00Oo0O + I11O0O0oOO00O00o + ooOOOoO
def ii1II1 ( ) :
 if os . path . exists ( O0OoO000O0OO ) :
  o0oOo0OoO = open ( O0OoO000O0OO , 'r' )
  for ooOOo0o in o0oOo0OoO :
   I11iIiiI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooOOo0o )
   for oO00oooOOoOo0 , i1I1ii11i1Iii in I11iIiiI :
    IiIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 222 , III1iII1I1ii + 'streams.png' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 88 - 88: Ii1I - I11O0O0oOO00O00o * ii * Ii1IIIi1 . Ii . I11i
def OooOoO0OO00 ( url ) :
 if os . path . exists ( Remote ) :
  IIIi1I1IIii1II = I1i111I ( url )
  IIi1I11I1II = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 , url in IIi1I11I1II :
   url = ( url ) . strip ( )
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iI111I11I1I1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 94 - 94: I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + ii % oO0o
  if 36 - 36: Ii1IIIi1 * I11O0O0oOO00O00o * o0o00Oo0O * O00o0O00 - I11i / Ii1I
def IiI111111IIII ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'plugin.video.GenieTv'
 if 54 - 54: ooOoO0O00 - oO0o / ii
 ooooOOo ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 100 - 100: O00o0O00 % Ii - oOo0O0Ooo * ii1ii11IIIiiI - I11i
def ooOOO00Ooo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi1I11I1II = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii in IIi1I11I1II :
  i1I1ii11i1Iii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + i1I1ii11i1Iii
 oO00oooOOoOo0 = 'repository.GenieTv'
 if 65 - 65: Ii - ii / o0o00Oo0O * ooOOOoO % I11O0O0oOO00O00o
 ooooOOo ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 53 - 53: O00o0O00 + ii1ii11IIIiiI
 if 10 - 10: I11O0O0oOO00O00o * ooOoO0O00 . oO0oo0o / ii1ii11IIIiiI . O00o0O00 / ii1ii11IIIiiI
def i1111I1iii1 ( ) :
 I1IIII1i ( '[COLOR' + iiI1IiI + ']CATAGORIES[/COLOR]' , '' , 10051 , III1iII1I1ii + 'Catagories.png' , OO0o , '' )
 I1IIII1i ( '[COLOR' + iiI1IiI + ']SEARCH[/COLOR]' , '' , 10052 , III1iII1I1ii + 'Search.png' , OO0o , '' )
 if 89 - 89: ooOOOoO - ooOoO0O00 - ooOOOoO
 if 74 - 74: oO0o % oO0o
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iI111I11I1I1 = xbmcgui . Dialog ( )
I11 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
IIIII1IIiIi = 'https://addons.tvaddons.ag/'
if 91 - 91: oOo0O0Ooo / IIiIiII11i * O00o0O00
def ooOoo000 ( ) :
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 oOO0o0oo0 = 'https://addons.tvaddons.ag/search/?keyword=' + i1i1ii
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( oOO0o0oo0 )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , i1I1ii11i1Iii , 10054 , 'https://addons.tvaddons.ag/' + ooo0O , OO0o , '' )
  if 56 - 56: O0OOOoOoo0 . iI11I1II1I1I + ooOoO0O00
  if 84 - 84: Ii1IIIi1 % ooOoO0O00
def oOo ( ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( IIIII1IIiIi )
 IIi1I11I1II = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIIi1I1IIii1II )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  if 'Repositories' in oO00oooOOoOo0 :
   pass
  elif 'Services' in oO00oooOOoOo0 :
   pass
  elif 'International' in oO00oooOOoOo0 :
   pass
  else :
   I1IIII1i ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , i1I1ii11i1Iii , 10053 , 'https://addons.tvaddons.ag/' + O0O0Oo00 , OO0o , '' )
   if 94 - 94: ooOoO0O00 / Ii1I / oOo0O0Ooo * ii1ii11IIIiiI * I1ii11iIi11i
   if 21 - 21: ii + o0o00Oo0O / ii / O00o0O00
def Addon ( url ) :
 HTML = OPEN_URL ( url )
 Next = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( HTML )
 match = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( HTML )
 for url , img , name in match :
  if 'Please' in name :
   pass
  else :
   addDir2 ( name , url , 10054 , 'https://addons.tvaddons.ag/' + img , FANART , '' )
 for url in Next :
  addDir ( '[COLOR' + TEXTCOL + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ART + 'Next.png' , FANART , '' )
  if 44 - 44: ooOoO0O00 . Ii1I - O0OOOoOoo0 . O00o0O00 . I11i + oO0oo0o
  if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + iI1ii11iIi1i % ooOoO0O00 . oO0oo0o
def o00OoOO00 ( url , name ) :
 IIIi1I1IIii1II = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)"' ) . findall ( IIIi1I1IIii1II )
 for url in IIi1I11I1II :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , name + '.zip' )
   try :
    os . remove ( IIiiiiIiIIii )
   except :
    pass
   downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
   oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oO0ooOO
   print '======================================='
   extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
   ii1 ( )
   if 62 - 62: OOooOOo * ii * I11i
def ooooOOo ( url , name ) :
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IIiiiiIiIIii = os . path . join ( oOo00Oo0o0Oo , name + '.zip' )
 try :
  os . remove ( IIiiiiIiIIii )
 except :
  pass
 downloader . download ( url , IIiiiiIiIIii , o0oOoO00o )
 oO0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oO0ooOO
 print '======================================='
 extract . all ( IIiiiiIiIIii , oO0ooOO , o0oOoO00o )
 ii1 ( )
 if 37 - 37: oO0oo0o
def ii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 18 - 18: ooOOOoO * Ii + iI11I1II1I1I % I11O0O0oOO00O00o + ooOoO0O00 - oO0o
 if 85 - 85: oO0o * I11O0O0oOO00O00o + oO0o
def iI1ii ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , url , 1007 , ooo0O )
def iII1I1IIiiiI ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , ooo0O )
  if 31 - 31: oO0oo0o % ooOoO0O00 . ii - I11i + ii
  if 45 - 45: O00o0O00 + I11O0O0oOO00O00o / ii - iI1ii11iIi1i + ii
def ii1i1I1111ii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , iconimage , oO000oOo00o0o , oOo0O , name in IIi1I11I1II :
  if 'http' in url :
   if '.php' in url :
    OO0OOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
    for ooOOo0o in OO0OOO00 :
     if ooOOo0o == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oOOO0 ( name , url , 1016 , iconimage , oOo0O , oO000oOo00o0o )
   else :
    if 'youtube' in url :
     OO0OOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for ooOOo0o in OO0OOO00 :
      if ooOOo0o == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1i1I1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oOo0O , oO000oOo00o0o )
    else :
     OO0OOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
     for ooOOo0o in OO0OOO00 :
      if ooOOo0o == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1i1I1 ( name , url , 222 , iconimage , oOo0O , oO000oOo00o0o )
     I1I1II1I11 ( 'movies' , 'INFO' )
  else :
   oo0ooo0O0O0O ( url , iconimage , name )
   if 71 - 71: Ii1I . ii1ii11IIIiiI
 else :
  IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
  for url , ooo0O , name in IIi1I11I1II :
   if 'http' in url :
    if '.php' in url :
     IiIi1I1 ( name , url , 1016 , ooo0O )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      IiIIi1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O )
     else :
      OO0OOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O00oO ) )
      for ooOOo0o in OO0OOO00 :
       if ooOOo0o == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      IiIIi1 ( name , url , 222 , ooo0O )
      I1I1II1I11 ( 'movies' , 'INFO' )
   else :
    oo0ooo0O0O0O ( url , ooo0O , name )
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 16 - 16: oO0oo0o - Ii1I . OOooOOo
def oo0ooo0O0O0O ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 O0OoO0oOOoo0 = ( url ) . replace ( O0oooO00ooO0 , 'http' ) . replace ( IIi1I1 , '.com' ) ;
 Oo000O000 = ( O0OoO0oOOoo0 ) . replace ( o00OOO0o00OO , 'a' ) . replace ( O0O00OO , 'b' ) . replace ( IIiiiI , 'c' ) . replace ( Oo0oOO , 'd' ) . replace ( i111i1IIi1i , 'e' ) . replace ( oO00Oo0O0 , 'f' ) ;
 iIi11 = ( Oo000O000 ) . replace ( oOOOOO0 , 'g' ) . replace ( I1iII1 , 'h' ) . replace ( oO00o0oOoo , 'i' ) . replace ( OOI1i , 'j' ) . replace ( oO0Oooo0OoO , 'k' ) . replace ( Iiii1IIIIiiI11 , 'l' ) ;
 O00oOoOo0ooO0O0oo = ( iIi11 ) . replace ( ii11IiI , 'm' ) . replace ( I1iI1Ii11 , 'n' ) . replace ( I1II11IIi11i , 'o' ) . replace ( oo00ooOo , 'p' ) . replace ( Ooo00OoO0O00 , 'q' ) . replace ( ii1ii1i1ii , 'r' ) ;
 iIi1Iii1 = ( O00oOoOo0ooO0O0oo ) . replace ( ooooI11iii1iIIIIi , 's' ) . replace ( iIi , 't' ) . replace ( III1i1iiI1 , 'u' ) . replace ( O0ooO0O00oo0 , 'v' ) . replace ( II1i1iI , 'w' ) . replace ( iI111I1 , 'x' ) ;
 iIiii1IIi1I = ( iIi1Iii1 ) . replace ( IiIi , 'y' ) . replace ( ii1IiI , 'z' ) . replace ( ooOOo0O0o00o00 , '.' ) . replace ( o0oI1I1i , '(' ) . replace ( oo00oO00oooo , ')' ) . replace ( ooo0Oo00O , '/' ) ;
 oo0o0ooOoo00O = ( iIiii1IIi1I ) . replace ( iiI1I , '1' ) . replace ( OoiiI11111II , '2' ) . replace ( iI1ii1 , '3' ) . replace ( Ii1iiII11ii1 , '4' ) . replace ( iIi11I1II , '5' ) . replace ( oOOI1 , '6' ) ;
 O0oOOo = ( oo0o0ooOoo00O ) . replace ( o0O00O , '7' ) . replace ( OO00oOo0o00 , '8' ) . replace ( O0O0o , '9' ) . replace ( i1i1i1Ii111II , '0' ) . replace ( IiiIiI1IIi1IIIii , ':' ) . replace ( OOO0o , '%' ) ;
 url = ( O0oOOo ) . replace ( iI11iI , '-' ) . replace ( Ooo0OOO0O00 , '_' ) ;
 IiIIi1 ( name , url , 222 , iconimage ) ;
 if 33 - 33: oOo0O0Ooo * ii1ii11IIIiiI
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . O0OOOoOoo0 - ooOoO0O00
def oOOoOo0OoOO ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1007 , ooo0O )
def OO00o ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , ooo0O )
  if 15 - 15: ooOoO0O00 . oOo0O0Ooo - OOooOOo % IIiIiII11i . O0OOOoOoo0 / oO0oo0o
def O0Oo00o0o ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 oooooO0oO0o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 oooooO0oO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooooO0oO0o )
 if 63 - 63: iI1ii11iIi1i - IIiIiII11i . I11O0O0oOO00O00o / OOooOOo
 if 17 - 17: O0OOOoOoo0
def IIi1IIII ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1III1111iIi )
 for url , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  if '-dir-' in oO00oooOOoOo0 :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , O0O0Oo00 )
  else :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' , url , 1006 , O0O0Oo00 )
   if 33 - 33: IIiIiII11i . Ii1I - o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def O00O ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIIIIi1 = ( 'http://afewbitsmore.com/' )
 IIi1I11I1II = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[To Parent Directory]' in oO00oooOOoOo0 :
   oO00oooOOoOo0 = 'HOME'
   pass
  elif 'HOME' in oO00oooOOoOo0 :
   pass
  elif '.m3u' in oO00oooOOoOo0 :
   IiIi1I1 ( '[COLOR' + iiI1IiI + ']PLAY ALL[/COLOR]' , IIIIIi1 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in oO00oooOOoOo0 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , IIIIIi1 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in oO00oooOOoOo0 :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , IIIIIi1 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) , IIIIIi1 + url , 1012 , III1iII1I1ii + 'music.png' )
def o0oIi1iiiii ( url ) :
 IIIi1I1IIii1II = I1i111I ( url )
 IIi1I11I1II = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIIi1I1IIii1II )
 for O0O0Oo00 , oO00oooOOoOo0 , url in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 88 - 88: iI1ii11iIi1i / Ii % OOooOOo % O00o0O00
def OOI1 ( url ) :
 I1III1111iIi = I1i111I ( url )
 IIIIIi1 = url
 IIi1I11I1II = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  if '.mp3' in oO00oooOOoOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   IiIi1I1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '/' , '' ) , IIIIIi1 + url , 1011 , III1iII1I1ii + 'music.png' )
def oooO00oOOooO ( ) :
 I1III1111iIi = I1i111I ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , O0O0Oo00 , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , ( 'http://www.cyn.net/music/' + i1I1ii11i1Iii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + O0O0Oo00 ) . replace ( ' ' , '%20' ) )
def iiiiI ( url , img ) :
 I1III1111iIi = I1i111I ( url )
 I1i11 = url
 img = img
 IIi1I11I1II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I1i11 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 66 - 66: ii + Ii1IIIi1 . ooOOOoO % ooOoO0O00
def O000OoOO0oO ( url ) :
 I1III1111iIi = I1i111I ( url )
 I1i11 = url
 IIi1I11I1II = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1III1111iIi )
 for type , url , oO00oooOOoOo0 in IIi1I11I1II :
  if '[VID]' in type :
   IiIIi1 ( ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I1i11 + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   O000OoOO0oO ( I1i11 + url )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: oOo0O0Ooo / OOooOOo
 if 72 - 72: I1ii11iIi11i + ii1ii11IIIiiI % Ii1I + O00o0O00 % ii1ii11IIIiiI
def iiiiI11 ( ) :
 oooII111 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 O00Ooo = iI111I11I1I1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1i1ii = O00Ooo . lower ( )
 i1I1ii11i1Iii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1i11 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iIi11i1 = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 10 - 10: O0OOOoOoo0 - I1ii11iIi11i % IIiIiII11i
 IIIi1I1IIii1II = ooOooo000oOO ( i1I1ii11i1Iii )
 O0 = ooOooo000oOO ( I1i11 )
 ii1ii1ii = ooOooo000oOO ( iIi11i1 )
 if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 if IIIi1I1IIii1II != 'Failed' :
  IIi1I11I1II = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in IIi1I11I1II :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1ii11i1Iii + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 46 - 46: ii1ii11IIIiiI * oO0oo0o . iI1ii11iIi1i * ii1ii11IIIiiI * iI11I1II1I1I / I11O0O0oOO00O00o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  OooOoooOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi1I1IIii1II )
  for oO00oooOOoOo0 in OooOoooOo :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i11 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 46 - 46: IIiIiII11i % Ii1I . O00o0O00 . I1ii11iIi11i / Ii + oO0o
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
 if ii1ii1ii != 'Failed' :
  I1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ii1ii1ii )
  for oO00oooOOoOo0 in I1 :
   if O00Ooo in oO00oooOOoOo0 . lower ( ) :
    IiIi1I1 ( ( oO00oooOOoOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIi11i1 + oO00oooOOoOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 47 - 47: ooOOOoO . O00o0O00
    I1I1II1I11 ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: I11O0O0oOO00O00o % IIiIiII11i / O0OOOoOoo0 % O00o0O00 / O0OOOoOoo0 % Ii
    if 57 - 57: I11O0O0oOO00O00o - I11O0O0oOO00O00o % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
    if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iI1ii11iIi1i * iI11I1II1I1I
    if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oO0oo0o * I11i + O00o0O00
    if 89 - 89: O0OOOoOoo0 * oOo0O0Ooo . oO0oo0o
    if 75 - 75: O0OOOoOoo0 - Ii1IIIi1 % Ii1IIIi1 + O0OOOoOoo0 * I11i - Ii1I
ii11IiI = '{SF},' ; I1iI1Ii11 = '{IF},' ; I1II11IIi11i = '{PW},' ; iI1ii1 = '{AM},' ; oo00ooOo = '{GF},' ; Ooo00OoO0O00 = '{DD},' ; ii1ii1i1ii = '{UO},' ; ooooI11iii1iIIIIi = '{LE},' ; III1i1iiI1 = '{ZY},' ; O0ooO0O00oo0 = '{UE},' ; II1i1iI = '{PE},' ; iI111I1 = '{JE},' ; IiIi = '{TH},' ; ii1IiI = '{LK},'
if 26 - 26: I11O0O0oOO00O00o * iI1ii11iIi1i % oOo0O0Ooo + Ii1IIIi1
if 38 - 38: Ii1IIIi1 - I1ii11iIi11i / iI1ii11iIi1i + oO0oo0o . Ii1IIIi1 + ooOOOoO
def iIiii1iI1Ii ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( 'http://www.iwatchseries.me/tv-list/' )
 IIi1I11I1II = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 8021 , III1iII1I1ii + 'iwatch.png' )
def ooIi ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 , OOO0oOOo00O in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 + OOO0oOOo00O , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def oO0oOo ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IIiIiii ( url )
def IIiIiii ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1III1111iIi )
 OooOoooOo = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1III1111iIi )
 I1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( 'VidSpot - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in OooOoooOo :
  IiIIi1 ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for oO00oooOOoOo0 , url in I1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   IiIIi1 ( 'TheVideo - ' + oO00oooOOoOo0 , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 71 - 71: I11i + O00o0O00 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
def oo000O0o ( ) :
 I1III1111iIi = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi1I11I1II = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1021 , III1iII1I1ii + 'anime.png' )
  if 99 - 99: oOo0O0Ooo
  if 78 - 78: oO0o / iI11I1II1I1I . iI1ii11iIi1i * oO0o * OOooOOo - O00o0O00
def IiI1I1iii ( ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( 'http://www.animetoon.org/cartoon' )
 IIi1I11I1II = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1III1111iIi )
 for i1I1ii11i1Iii , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , 1002 , III1iII1I1ii + 'anime.png' )
  if 34 - 34: ii
  if 84 - 84: Ii + iI1ii11iIi1i
  if 81 - 81: Ii % oOo0O0Ooo / Ii1IIIi1 % oO0o / ii1ii11IIIiiI % iI11I1II1I1I
def IIII1iI1IiIiI ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 OooOoooOo = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1III1111iIi )
 for O0O0Oo00 in OooOoooOo :
  OoO00O0 = O0O0Oo00
 I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1III1111iIi )
 for url in I1 :
  IiIi1I1 ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 IIi1I11I1II = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1III1111iIi )
 for url , oO00oooOOoOo0 in IIi1I11I1II :
  IiIi1I1 ( oO00oooOOoOo0 , url , 1003 , OoO00O0 )
 xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1II1 ( url , IMAGE ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1III1111iIi )
 for oO00oooOOoOo0 , url in IIi1I11I1II :
  print oO00oooOOoOo0 + '     ' + url
  if 'easy' in url :
   OoOoOoo0oOOooo0o ( url )
  elif 'playpanda' in url :
   OoOoOoo0oOOooo0o ( url )
   if 6 - 6: O00o0O00 . Ii - iI11I1II1I1I * ooOOOoO * Ii1IIIi1
  xbmcplugin . addSortMethod ( O000OO0 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOoOoo0oOOooo0o ( url ) :
 I1III1111iIi = O0i1II1Iiii1I11 ( url )
 IIi1I11I1II = re . compile ( "url: '(.+?)'," ) . findall ( I1III1111iIi )
 for url in IIi1I11I1II :
  IiIIi1 ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 19 - 19: o0o00Oo0O + oO0oo0o + I11i
  if 81 - 81: iI11I1II1I1I
def OOO00OiI ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0oOOo . add_header ( 'referer' , url )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 88 - 88: O00o0O00 . I1ii11iIi11i * ooOOOoO - iI11I1II1I1I % oO0oo0o
def I1i111I ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 80 - 80: iI1ii11iIi1i - Ii1I . iI1ii11iIi1i / Ii + o0o00Oo0O . ooOOOoO
def III11i ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1IiiIiii1 = ( '%s%s' % ( i11i , url ) )
 OOO00O = I1i111I ( url )
 IIi1I11I1II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOO00O )
 for url , ooo0O , oO00oooOOoOo0 in IIi1I11I1II :
  IiIIi1 ( '%s' % ( '[COLOR' + iiI1IiI + ']' + oO00oooOOoOo0 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooo0O )
  if 54 - 54: ii1ii11IIIiiI / I11i
def oOOO00o000o ( url ) :
 if 39 - 39: O00o0O00 % oO0oo0o * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
 oooOo = open ( o0O , "a" )
 oooOo . write ( 'url="' + url + '"\n' )
 oooOo . close
 if 91 - 91: oOo0O0Ooo - Ii1IIIi1 / oO0o - oO0o / iI1ii11iIi1i - ooOOOoO
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
 import urlresolver
 try : II1III1i1iiI . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( oO00oooOOoOo0 ) )
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
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
  if 14 - 14: O00o0O00 / I11i + iI1ii11iIi1i / ii - I11O0O0oOO00O00o
def O00o ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
 o0oOoO00o . update ( 100 , '%s' % oO00oooOOoOo0 )
 xbmc . sleep ( 1 )
 II1III1i1iiI . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 65 - 65: OOooOOo / Ii1I / I11i
def oO00O0 ( url ) :
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II1III1i1iiI . play ( url ) . strip ( )
 except : pass
 if 15 - 15: O0OOOoOoo0 / O0OOOoOoo0 % ii . ii1ii11IIIiiI
def oOoOooO0OOOoo ( url ) :
 II1III1i1iiI = xbmc . Player ( O00o0o ( ) )
 import urlresolver
 I1I111i = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 II1III1i1iiI . play ( I1I111i )
 xbmc . sleep ( 1 )
 II1III1i1iiI . play ( url )
 if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + oO0oo0o
 if 58 - 58: Ii1IIIi1 - ii
def O00o0o ( ) :
 try :
  o00o = getSet ( "core-player" )
  if ( o00o == 'DVDPLAYER' ) : O00 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o00o == 'MPLAYER' ) : O00 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o00o == 'PAPLAYER' ) : O00 = xbmc . PLAYER_CORE_PAPLAYER
  else : O00 = xbmc . PLAYER_CORE_AUTO
 except : O00 = xbmc . PLAYER_CORE_AUTO
 return O00
 return True
 if 27 - 27: Ii1IIIi1 . OOooOOo / ii
def IiIi1I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iii = [ ]
  if showcontext == 'fav' :
   iii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   iii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooOoo0OO . addContextMenuItems ( iii )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = True )
 return IIii1III
 if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % I11O0O0oOO00O00o
def OOoOoo00Oo ( name , url , mode , iconimage , fanart , description ) :
 if 39 - 39: I11i + ooOOOoO / iI1ii11iIi1i + I11i
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooOoo0OO . setProperty ( "Fanart_Image" , fanart )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = True )
 return IIii1III
 if 33 - 33: Ii1IIIi1 - I1ii11iIi11i - I11O0O0oOO00O00o
def IiIIi1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iii = [ ]
  if showcontext == 'fav' :
   iii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   iii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooooOoo0OO . addContextMenuItems ( iii )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = False )
 return IIii1III
 if 61 - 61: iI1ii11iIi1i + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / oO0oo0o
 if 47 - 47: ii1ii11IIIiiI
 if 25 - 25: Ii1IIIi1 + oOo0O0Ooo + OOooOOo + ii1ii11IIIiiI % o0o00Oo0O
 if 26 - 26: O0OOOoOoo0 + OOooOOo
 if 17 - 17: Ii1I - Ii1IIIi1 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * O00o0O00
 if 6 - 6: ii1ii11IIIiiI
def O0O0Oooo0o ( heading , announce ) :
 class ii1iiIiiiI11 ( ) :
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
   try : o0Oo00 = open ( announce ) ; Iii = o0Oo00 . read ( )
   except : Iii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Iii ) )
   return
 ii1iiIiiiI11 ( )
 ii1iiIiiiI11 ( )
 if 95 - 95: ii1ii11IIIiiI - ooOOOoO
def I1ii ( ) :
 O0O0Oooo0o ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 82 - 82: OOooOOo . iI1ii11iIi1i
 if 73 - 73: ii1ii11IIIiiI
 if 25 - 25: ooOOOoO
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . iI1ii11iIi1i - I1ii11iIi11i . Ii
def ii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
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
 if 55 - 55: oO0o % o0o00Oo0O / ii
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88: Ii1I * Ii1IIIi1 + IIiIiII11i
 if 62 - 62: ii
def iioOo00O0o ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI11IIi1iiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 83 - 83: I1ii11iIi11i / O0OOOoOoo0
def II1iiIiI1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Ii1I11IIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 41 - 41: O0OOOoOoo0 / oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . Ii1I
def iii11I1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + i1II1iIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 20 - 20: Ii
def oOOOoo0 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + iI1i11II1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 61 - 61: I11O0O0oOO00O00o * iI1ii11iIi1i + I11O0O0oOO00O00o - I1ii11iIi11i % OOooOOo . Ii1IIIi1
def oO0OO ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + OOO00O0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 76 - 76: oOo0O0Ooo
def II111IiiIIi ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + o0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 54 - 54: O0OOOoOoo0
def i11i1II ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + OOoOo0oOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 99 - 99: I11i / O00o0O00 / oO0oo0o . ii1ii11IIIiiI
def iiI1I1iii1 ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + Ii111ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + iI1ii11iIi1i % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + OoOO0o00OOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 42 , oOoooo000Oo00 , oOo0O , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 52 - 52: ii / iI1ii11iIi1i - o0o00Oo0O % ooOoO0O00 * O00o0O00
def oOOooOoO00O ( url ) :
 OOO00O = O0i1II1Iiii1I11 ( str ( I1I1IiI1 ) + I1i1IIiiI11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi1I11I1II = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOO00O )
 for oO00oooOOoOo0 , url , oOoooo000Oo00 , oOo0O , O0000OOO0 in IIi1I11I1II :
  I1IIII1i ( oO00oooOOoOo0 , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , O0000OOO0 )
 I1I1II1I11 ( 'movies' , 'MAIN' )
 if 4 - 4: oOo0O0Ooo / IIiIiII11i % o0o00Oo0O * O0OOOoOoo0 / IIiIiII11i . I1ii11iIi11i
 if 16 - 16: o0o00Oo0O + o0o00Oo0O - oOo0O0Ooo
 if 30 - 30: O0OOOoOoo0
 if 33 - 33: ii1ii11IIIiiI * ooOOOoO - o0o00Oo0O + oOo0O0Ooo / ooOOOoO
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: ooOOOoO - I11i % O00o0O00 - IIiIiII11i
 if 56 - 56: iI1ii11iIi1i * Ii
 if 92 - 92: IIiIiII11i - o0o00Oo0O . ii1ii11IIIiiI
 if 59 - 59: OOooOOo
def iiII1iiI ( ) :
 try :
  if os . path . exists ( O00o0OO ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( O00o0OO ) :
     Ooo0o00O0 = 0
     Ooo0o00O0 += len ( IIIIIii1ii11 )
     if Ooo0o00O0 > 0 :
      for o0Oo00 in IIIIIii1ii11 :
       os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
  I11iIiiIIII1ii1 = os . path . join ( Oo00OOOOO , "Textures13.db" )
  os . unlink ( I11iIiiIIII1ii1 )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 13 - 13: OOooOOo - oO0o * ii
 if 26 - 26: ii
 if 65 - 65: O00o0O00
 if 14 - 14: O0OOOoOoo0
 if 75 - 75: iI11I1II1I1I % O0OOOoOoo0 / O00o0O00 - Ii1IIIi1 % Ii
 if 11 - 11: I11O0O0oOO00O00o . iI1ii11iIi1i
 if 87 - 87: O00o0O00 + O00o0O00
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
def o0Oo0oOooOoOo ( title , message , times = 2000 , icon = Ooo ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 87 - 87: OOooOOo - oO0o * oO0o / iI1ii11iIi1i . I11O0O0oOO00O00o * I11i
def ooO0oOOooOo0 ( url ) :
 iii1I = os . path . join ( oO , 'addon_data' )
 oooo000 = [
 ( iii1I ) ,
 ( oOo0oooo00o ) ,
 ( os . path . join ( I11 , 'cache' ) ) ,
 ( os . path . join ( I11 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( iii1I , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iii1I , 'plugin.video.itv' , 'Images' ) ) ]
 if 27 - 27: iI11I1II1I1I + oO0oo0o % I1ii11iIi11i
 OooOoo0Oo = 0
 if 41 - 41: O0OOOoOoo0
 for ooOOo0o in oooo000 :
  if os . path . exists ( ooOOo0o ) and not ooOOo0o in [ oOo0oooo00o , iii1I ] :
   for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( ooOOo0o ) :
    Ooo0o00O0 = 0
    Ooo0o00O0 += len ( IIIIIii1ii11 )
    if Ooo0o00O0 > 0 :
     for o0Oo00 in IIIIIii1ii11 :
      if not o0Oo00 in i1iiIIiiI111 :
       try :
        os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
       except :
        pass
      else : oo00oOO000oO0 ( 'Ignore Log File: %s' % o0Oo00 )
     for oOoOOOo in I11I1IIiiII1 :
      try :
       shutil . rmtree ( os . path . join ( iIoo0ooooO , oOoOOOo ) )
       OooOoo0Oo += 1
       oo00oOO000oO0 ( "[Success] cleared %s files from %s" % ( str ( Ooo0o00O0 ) , os . path . join ( ooOOo0o , oOoOOOo ) ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( ooOOo0o , oOoOOOo ) )
  else :
   for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( ooOOo0o ) :
    for oOoOOOo in I11I1IIiiII1 :
     if 'cache' in oOoOOOo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIoo0ooooO , oOoOOOo ) )
       OooOoo0Oo += 1
       oo00oOO000oO0 ( "[Success] wiped %s " % os . path . join ( ooOOo0o , oOoOOOo ) )
      except :
       oo00oOO000oO0 ( "[Failed] to wipe cache in: %s" % os . path . join ( ooOOo0o , oOoOOOo ) )
       if 11 - 11: ooOoO0O00 / ii1ii11IIIiiI * Ii1I * ii1ii11IIIiiI * O0OOOoOoo0 - Ii
 o0Oo0oOooOoOo ( oo0o0O00 , 'Clear Cache: Removed %s Files' % OooOoo0Oo )
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . iI1ii11iIi1i
 if 26 - 26: oO0oo0o - O0OOOoOoo0 % I1ii11iIi11i - oO0oo0o + ooOOOoO
 if 33 - 33: iI1ii11iIi1i + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * ooOOOoO
 if 21 - 21: o0o00Oo0O * O0OOOoOoo0 % oO0o
 if 14 - 14: o0o00Oo0O / ii1ii11IIIiiI / O0OOOoOoo0 + ooOOOoO - ooOOOoO
 if 10 - 10: o0o00Oo0O - Ii1I / ii1ii11IIIiiI % OOooOOo / ii / iI1ii11iIi1i
def O000oOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o00Oo00O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( o00Oo00O0o ) :
   Ooo0o00O0 = 0
   Ooo0o00O0 += len ( IIIIIii1ii11 )
   if 83 - 83: ii . Ii1IIIi1
   if 20 - 20: oO0o . oO0oo0o
   if Ooo0o00O0 > 0 :
    if 4 - 4: I1ii11iIi11i % iI1ii11iIi1i % oO0o * Ii1IIIi1 % ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( Ooo0o00O0 ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: ii . Ii1IIIi1
     for o0Oo00 in IIIIIii1ii11 :
      os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
     for oOoOOOo in I11I1IIiiII1 :
      shutil . rmtree ( os . path . join ( iIoo0ooooO , oOoOOOo ) )
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
def OoOoO0OoOOOOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 o00Oo00O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( o00Oo00O0o ) :
   Ooo0o00O0 = 0
   Ooo0o00O0 += len ( IIIIIii1ii11 )
   if 43 - 43: iI1ii11iIi1i . O00o0O00 + oOo0O0Ooo * Ii
   if 2 - 2: O00o0O00
   if Ooo0o00O0 > 0 :
    if 3 - 3: oOo0O0Ooo . Ii1IIIi1 % o0o00Oo0O - O0OOOoOoo0 / o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( Ooo0o00O0 ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79: iI1ii11iIi1i + oO0oo0o % O0OOOoOoo0 % oOo0O0Ooo
     for o0Oo00 in IIIIIii1ii11 :
      os . unlink ( os . path . join ( iIoo0ooooO , o0Oo00 ) )
     for oOoOOOo in I11I1IIiiII1 :
      shutil . rmtree ( os . path . join ( iIoo0ooooO , oOoOOOo ) )
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
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI1I = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( iI1I ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoO00 = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml' )
   try :
    os . remove ( OoO00 )
    print '=== GenieTv - REMOVING    ' + str ( OoO00 ) + '    ==='
   except :
    pass
   OOO00O = ii11iIi1I . http_GET ( url ) . content
   oO0i1iI = open ( OoO00 , "w" )
   oO0i1iI . write ( OOO00O )
   oO0i1iI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoO00 = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml' )
  try :
   os . remove ( OoO00 )
   print '=== GenieTv - REMOVING    ' + str ( OoO00 ) + '    ==='
  except :
   pass
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  oO0i1iI = open ( OoO00 , "w" )
  oO0i1iI . write ( OOO00O )
  oO0i1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 73 - 73: oOo0O0Ooo / o0o00Oo0O % Ii1IIIi1 * IIiIiII11i
def o000oO ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml' )
 try :
  oO0i1iI = open ( OoO00 ) . read ( )
  if 'zero' in oO0i1iI :
   name = '0CACHE'
  elif 'tuxen' in oO0i1iI :
   name = 'TUXENS'
  elif 'muckys' in oO0i1iI :
   name = 'MUCKYS'
  elif 'p2p1' in oO0i1iI :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oO0i1iI :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oO0i1iI :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 23 - 23: O00o0O00 + O0OOOoOoo0 / Ii * I1ii11iIi11i . oO0o
def i1I111II ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoO00 = os . path . join ( oOo00Oo0o0Oo , 'advancedsettings.xml' )
 try :
  os . remove ( OoO00 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 51 - 51: oOo0O0Ooo * O0OOOoOoo0
 if 47 - 47: O00o0O00 . O00o0O00 . ooOOOoO . ii1ii11IIIiiI / ooOoO0O00
 if 77 - 77: IIiIiII11i % I11O0O0oOO00O00o / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
 if 10 - 10: I11O0O0oOO00O00o - I11i % ii - Ii1I
 if 64 - 64: oO0o / oOo0O0Ooo
 if 23 - 23: I11O0O0oOO00O00o * ii1ii11IIIiiI * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: ooOOOoO * ii . O0OOOoOoo0 % Ii
 if 11 - 11: iI11I1II1I1I . ii1ii11IIIiiI - I1ii11iIi11i / I11O0O0oOO00O00o + IIiIiII11i
 if 29 - 29: I11O0O0oOO00O00o . Ii + ooOoO0O00 - iI1ii11iIi1i + o0o00Oo0O . oOo0O0Ooo
def i1iIiII1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi1I11I1II = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii11iIi1I . http_GET ( url ) . content )
 for Oo00OO , iIi111 , I11I1I , i1i1ii1 in IIi1I11I1II :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Oo00OO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I11I1I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i1i1ii1 )
  inc = inc + 1
  if 2 - 2: ii
  if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
  if 46 - 46: o0o00Oo0O % ii
  if 22 - 22: Ii1IIIi1 + ii - OOooOOo - oO0o * ii1ii11IIIiiI - oO0oo0o
  if 99 - 99: O0OOOoOoo0 / oOo0O0Ooo . iI1ii11iIi1i - iI1ii11iIi1i * oOo0O0Ooo
  if 24 - 24: I11O0O0oOO00O00o * oO0o - oO0oo0o / iI11I1II1I1I - I1ii11iIi11i . O00o0O00
  if 2 - 2: O0OOOoOoo0 - o0o00Oo0O - Ii1I / I11O0O0oOO00O00o * OOooOOo
  if 26 - 26: Ii1I + ii1ii11IIIiiI - oO0oo0o + ooOOOoO % O00o0O00
  if 84 - 84: I11O0O0oOO00O00o % iI1ii11iIi1i % o0o00Oo0O * I11i
def IIIiIi11 ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoO00 = os . path . join ( oOo00Oo0o0Oo , 'addons2.ini' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  oO0i1iI = open ( OoO00 , "w" )
  oO0i1iI . write ( OOO00O )
  oO0i1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 57 - 57: O0OOOoOoo0 * iI11I1II1I1I * Ii1IIIi1 * iI1ii11iIi1i / iI1ii11iIi1i
def IiIiIiIII1Iii ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoO00 = os . path . join ( oOo00Oo0o0Oo , 'settings.xml' )
  OOO00O = ii11iIi1I . http_GET ( url ) . content
  oO0i1iI = open ( OoO00 , "w" )
  oO0i1iI . write ( OOO00O )
  oO0i1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoO00 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 57 - 57: oO0oo0o / O00o0O00 / O00o0O00 * I11i * Ii1I - Ii
 if 82 - 82: oOo0O0Ooo . oO0o
def OOOo00O0OoOo ( ) :
 try :
  OO0oO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO0oO0 ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I11iI1i11IiI = os . path . join ( OO0oO0 , "source.db" )
    os . unlink ( I11iI1i11IiI )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 78 - 78: ooOOOoO / Ii1IIIi1 * iI1ii11iIi1i . O00o0O00 . oO0oo0o - ii1ii11IIIiiI
 if 39 - 39: O0OOOoOoo0 . ooOoO0O00 + ii . Ii1IIIi1 - Ii % ii1ii11IIIiiI
 if 38 - 38: oO0oo0o
 if 9 - 9: I11O0O0oOO00O00o . oO0o . oO0oo0o / ii
 if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
def O0i1II1Iiii1I11 ( url ) :
 Oo0oOOo = urllib2 . Request ( url )
 Oo0oOOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 Oo0OoO00oOO0o = urllib2 . urlopen ( Oo0oOOo )
 OOO00O = Oo0OoO00oOO0o . read ( )
 Oo0OoO00oOO0o . close ( )
 return OOO00O
 if 2 - 2: IIiIiII11i + I11O0O0oOO00O00o . oO0o
 if 14 - 14: O00o0O00 * oOo0O0Ooo - Ii1I
 if 10 - 10: Ii1IIIi1 % ii1ii11IIIiiI * Ii1I * o0o00Oo0O * Ii % ii1ii11IIIiiI
 if 68 - 68: ii * OOooOOo
 if 9 - 9: ii1ii11IIIiiI
 if 36 - 36: ii1ii11IIIiiI / OOooOOo + OOooOOo * O0OOOoOoo0 / O00o0O00 * o0o00Oo0O
 if 17 - 17: oO0o / O0OOOoOoo0 % oOo0O0Ooo
def IIiI1IiI1iIi1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iIiiI11II11 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iIiiI11II11 :
  o0o0O00O = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; o0o0O00O = xbmc . translatePath ( o0o0O00O ) ;
  oO0oO0OoO00 = os . path . join ( o0o0O00O , ".." , ".." ) ; oO0oO0OoO00 = os . path . abspath ( oO0oO0OoO00 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oO0oO0OoO00 ) ; Oo0ooo00o0O0 = False
  try :
   for iIoo0ooooO , I11I1IIiiII1 , IIIIIii1ii11 in os . walk ( oO0oO0OoO00 , topdown = True ) :
    I11I1IIiiII1 [ : ] = [ oOoOOOo for oOoOOOo in I11I1IIiiII1 if oOoOOOo not in o0oO0 ]
    for oO00oooOOoOo0 in IIIIIii1ii11 :
     try : os . remove ( os . path . join ( iIoo0ooooO , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0ooo00o0O0 = True
      plugintools . log ( "Error removing " + iIoo0ooooO + " " + oO00oooOOoOo0 )
    for oO00oooOOoOo0 in I11I1IIiiII1 :
     try : os . rmdir ( os . path . join ( iIoo0ooooO , oO00oooOOoOo0 ) )
     except :
      if oO00oooOOoOo0 not in [ "Database" , "userdata" ] : Oo0ooo00o0O0 = True
      plugintools . log ( "Error removing " + iIoo0ooooO + " " + oO00oooOOoOo0 )
   if not Oo0ooo00o0O0 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OooOo000OOOOo ( )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * iI1ii11iIi1i + iI11I1II1I1I
 if 80 - 80: I11i . Ii1IIIi1 . ii
 if 63 - 63: O0OOOoOoo0 . O00o0O00
def o000Oo ( ) :
 IiIiIIIiI1iII = [ ]
 IiooO0O = sys . argv [ 2 ]
 if len ( IiooO0O ) >= 2 :
  O0Ooo0O0O = sys . argv [ 2 ]
  OOOO0 = O0Ooo0O0O . replace ( '?' , '' )
  if ( O0Ooo0O0O [ len ( O0Ooo0O0O ) - 1 ] == '/' ) :
   O0Ooo0O0O = O0Ooo0O0O [ 0 : len ( O0Ooo0O0O ) - 2 ]
  OOo0OOo = OOOO0 . split ( '&' )
  IiIiIIIiI1iII = { }
  for I11I11I11IiIi in range ( len ( OOo0OOo ) ) :
   OOIiI1IIIiI1I1i = { }
   OOIiI1IIIiI1I1i = OOo0OOo [ I11I11I11IiIi ] . split ( '=' )
   if ( len ( OOIiI1IIIiI1I1i ) ) == 2 :
    IiIiIIIiI1iII [ OOIiI1IIIiI1I1i [ 0 ] ] = OOIiI1IIIiI1I1i [ 1 ]
    if 84 - 84: OOooOOo - I11O0O0oOO00O00o
 return IiIiIIIiI1iII
 if 80 - 80: Ii % O00o0O00 - I1ii11iIi11i % O00o0O00
O0O0oOo0o0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
oo0ooO0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oOOOIii111111 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
I1IiIi11 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oOO0o000Oo00o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1i1I1i1i1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iI11IIi1iiI1I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Ii11i1IiII = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
Ii1I11IIi1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1II1iIii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iI1i11II1i1i = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OOO00O0OO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o0oo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OOoOo0oOooo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Ii111ii1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoOO0o00OOO0o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0oO0OoO0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
OooO00oo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I11iiii1I = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOoO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iIIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oOO0oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1i1IIiiI11II = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
i11i = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooOoo0OO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iii = [ ]
  if showcontext == 'fav' :
   iii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oO0 :
   iii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooooOoo0OO . addContextMenuItems ( iii )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = True )
 return IIii1III
 if 63 - 63: O00o0O00
def iIiIIi1 ( name , url , mode , iconimage , fanart , description ) :
 OOoOOOO00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIii1III = True
 ooooOoo0OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooooOoo0OO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooooOoo0OO . setProperty ( "Fanart_Image" , fanart )
 IIii1III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOoOOOO00 , listitem = ooooOoo0OO , isFolder = False )
 return IIii1III
 if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . I11O0O0oOO00O00o
 if 59 - 59: Ii1IIIi1 . ooOoO0O00
O0Ooo0O0O = o000Oo ( )
i1I1ii11i1Iii = None
oO00oooOOoOo0 = None
oO0oo0o00o0O = None
oOoooo000Oo00 = None
oOo0O = None
O0000OOO0 = None
iiii1I1 = None
if 82 - 82: I11i * oO0o / ooOOOoO
if 5 - 5: Ii1IIIi1 / oO0oo0o % O0OOOoOoo0 . Ii % OOooOOo + oO0oo0o
try :
 iiii1I1 = int ( O0Ooo0O0O [ "fav_mode" ] )
except :
 pass
 if 95 - 95: Ii1I
try :
 i1I1ii11i1Iii = urllib . unquote_plus ( O0Ooo0O0O [ "url" ] )
except :
 pass
try :
 oO00oooOOoOo0 = urllib . unquote_plus ( O0Ooo0O0O [ "name" ] )
except :
 pass
try :
 oOoooo000Oo00 = urllib . unquote_plus ( O0Ooo0O0O [ "iconimage" ] )
except :
 pass
try :
 oO0oo0o00o0O = int ( O0Ooo0O0O [ "mode" ] )
except :
 pass
try :
 oOo0O = urllib . unquote_plus ( O0Ooo0O0O [ "fanart" ] )
except :
 pass
try :
 O0000OOO0 = urllib . unquote_plus ( O0Ooo0O0O [ "description" ] )
except :
 pass
 if 48 - 48: I11O0O0oOO00O00o
 if 14 - 14: iI11I1II1I1I / I11i * ooOOOoO
print str ( I11i1 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oO0oo0o00o0O )
print "URL: " + str ( i1I1ii11i1Iii )
print "Name: " + str ( oO00oooOOoOo0 )
print "IconImage: " + str ( oOoooo000Oo00 )
if 35 - 35: iI11I1II1I1I
if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
def I1I1II1I11 ( content , viewType ) :
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 75 - 75: oOo0O0Ooo - O0OOOoOoo0 - oOo0O0Ooo % oO0oo0o % ii
if oOoooo000Oo00 == None : oOoooo000Oo00 = Ooo
if oOo0O == None : oOo0O = OO0o
if oO0oo0o00o0O == None :
 I11IiI ( )
 if 13 - 13: O0OOOoOoo0 * oO0o % iI11I1II1I1I / ooOOOoO * Ii1IIIi1 . I1ii11iIi11i
elif oO0oo0o00o0O == 1 :
 O0Oo0 ( i1I1ii11i1Iii )
 if 23 - 23: O0OOOoOoo0 / ooOOOoO . Ii1IIIi1 * iI1ii11iIi1i
elif oO0oo0o00o0O == 44 :
 I11III111i ( i1I1ii11i1Iii )
 if 87 - 87: Ii
elif oO0oo0o00o0O == 2 :
 iIIi1IIi ( )
 if 34 - 34: ooOoO0O00
elif oO0oo0o00o0O == 3 :
 iIi1IiI ( )
 if 64 - 64: iI11I1II1I1I / ooOOOoO / I1ii11iIi11i - Ii1I
elif oO0oo0o00o0O == 21 :
 i1i1II ( )
 if 100 - 100: ooOOOoO + ooOoO0O00 * oO0o
elif oO0oo0o00o0O == 4 :
 IIi11I1 ( )
 if 64 - 64: oO0oo0o * Ii . I1ii11iIi11i
elif oO0oo0o00o0O == 5 :
 OOOIiIi1111ii ( i1I1ii11i1Iii )
 if 52 - 52: I1ii11iIi11i / O0OOOoOoo0 / Ii1IIIi1 - I11i / Ii1IIIi1
elif oO0oo0o00o0O == 6 :
 O000oOo ( i1I1ii11i1Iii )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif oO0oo0o00o0O == 7 :
 II1Iiiii ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 85 - 85: oOo0O0Ooo
elif oO0oo0o00o0O == 8 :
 o000oO ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif oO0oo0o00o0O == 9 :
 FIXREPOSADDONS ( i1I1ii11i1Iii )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif oO0oo0o00o0O == 10 :
 ii1 ( )
 if 46 - 46: OOooOOo * I11O0O0oOO00O00o / oO0oo0o + I1ii11iIi11i + ooOOOoO
elif oO0oo0o00o0O == 11 :
 i1I111II ( i1I1ii11i1Iii )
 if 95 - 95: I11i - iI1ii11iIi1i
elif oO0oo0o00o0O == 12 :
 i1iIiII1 ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif oO0oo0o00o0O == 13 :
 iiII1iiI ( )
 if 19 - 19: OOooOOo . O00o0O00 . ii
elif oO0oo0o00o0O == 14 :
 ooO0oOOooOo0 ( i1I1ii11i1Iii )
 if 79 - 79: O00o0O00 * O0OOOoOoo0 * oOo0O0Ooo * Ii1I / Ii1I
elif oO0oo0o00o0O == 15 :
 i1II1I ( )
 if 62 - 62: O0OOOoOoo0 * iI1ii11iIi1i % Ii1I - ooOoO0O00 - Ii1I
elif oO0oo0o00o0O == 16 :
 IIIiIi11 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 24 - 24: O00o0O00
elif oO0oo0o00o0O == 17 :
 IiIiIiIII1Iii ( i1I1ii11i1Iii , oO00oooOOoOo0 )
 if 71 - 71: ooOOOoO - ooOoO0O00
elif oO0oo0o00o0O == 18 :
 OOOo00O0OoOo ( )
 if 56 - 56: OOooOOo + oO0oo0o
elif oO0oo0o00o0O == 19 :
 o0Oo ( i1I1ii11i1Iii )
 if 74 - 74: Ii1IIIi1 / ii1ii11IIIiiI / IIiIiII11i - Ii1IIIi1 / oO0oo0o % I11O0O0oOO00O00o
elif oO0oo0o00o0O == 40 :
 O0OIIi1 ( oO00oooOOoOo0 , i1I1ii11i1Iii , O0000OOO0 )
 if 19 - 19: ooOOOoO % ii + ii
elif oO0oo0o00o0O == 42 :
 o00o0oOo0O0O ( oO00oooOOoOo0 , i1I1ii11i1Iii , O0000OOO0 )
 if 7 - 7: ooOoO0O00
elif oO0oo0o00o0O == 43 :
 i1II11II1 ( i1I1ii11i1Iii )
 if 91 - 91: OOooOOo - OOooOOo . ooOOOoO
elif oO0oo0o00o0O == 20 :
 Ooo0Oo0oo0 ( i1I1ii11i1Iii )
 if 33 - 33: ii1ii11IIIiiI - iI11I1II1I1I / iI1ii11iIi1i % o0o00Oo0O
elif oO0oo0o00o0O == 22 :
 iioOo00O0o ( i1I1ii11i1Iii )
 if 80 - 80: ooOOOoO % ii - ooOOOoO
elif oO0oo0o00o0O == 23 :
 II1iiIiI1 ( i1I1ii11i1Iii )
 if 27 - 27: ii1ii11IIIiiI - I11i * Ii1I - oOo0O0Ooo
elif oO0oo0o00o0O == 24 :
 iii11I1 ( i1I1ii11i1Iii )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - Ii1IIIi1 . iI1ii11iIi1i
elif oO0oo0o00o0O == 25 :
 oOOOoo0 ( i1I1ii11i1Iii )
 if 100 - 100: IIiIiII11i / ii1ii11IIIiiI / Ii1IIIi1 - Ii1I * iI11I1II1I1I
elif oO0oo0o00o0O == 26 :
 oO0OO ( i1I1ii11i1Iii )
 if 7 - 7: ooOoO0O00 . ooOOOoO % Ii * Ii1I . I11O0O0oOO00O00o % Ii1I
elif oO0oo0o00o0O == 27 :
 II111IiiIIi ( i1I1ii11i1Iii )
 if 35 - 35: oOo0O0Ooo
elif oO0oo0o00o0O == 28 :
 i11i1II ( i1I1ii11i1Iii )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif oO0oo0o00o0O == 29 :
 iiI1I1iii1 ( i1I1ii11i1Iii )
 if 22 - 22: O0OOOoOoo0 . Ii . ii . ooOoO0O00
elif oO0oo0o00o0O == 30 :
 ooOo ( i1I1ii11i1Iii )
 if 12 - 12: OOooOOo % O00o0O00 + oO0oo0o . o0o00Oo0O % iI11I1II1I1I
elif oO0oo0o00o0O == 31 :
 oo000O ( i1I1ii11i1Iii )
 if 41 - 41: ii
elif oO0oo0o00o0O == 32 :
 IIi1I ( )
 if 13 - 13: I11O0O0oOO00O00o + ii1ii11IIIiiI - ii1ii11IIIiiI % oO0oo0o / I11O0O0oOO00O00o
elif oO0oo0o00o0O == 33 :
 OO0OoOOO0 ( )
 if 4 - 4: oOo0O0Ooo + O00o0O00 - ooOOOoO + Ii1IIIi1
elif oO0oo0o00o0O == 35 :
 Oo0O0Oo00O ( i1I1ii11i1Iii )
 if 78 - 78: iI1ii11iIi1i
elif oO0oo0o00o0O == 34 :
 o0OO0Oo ( i1I1ii11i1Iii )
 if 29 - 29: IIiIiII11i
elif oO0oo0o00o0O == 36 :
 I11I ( i1I1ii11i1Iii )
 if 79 - 79: iI11I1II1I1I - Ii + O0OOOoOoo0 - IIiIiII11i . iI11I1II1I1I
elif oO0oo0o00o0O == 37 :
 IiiIi ( i1I1ii11i1Iii )
 if 84 - 84: I1ii11iIi11i % I11O0O0oOO00O00o * o0o00Oo0O * I11O0O0oOO00O00o
elif oO0oo0o00o0O == 38 :
 i1I11iIII1i1I ( i1I1ii11i1Iii )
 if 66 - 66: O00o0O00 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OOOoOoo0
elif oO0oo0o00o0O == 41 :
 IIiI1IiI1iIi1 ( O0Ooo0O0O )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif oO0oo0o00o0O == 39 :
 oOOooOoO00O ( i1I1ii11i1Iii )
 if 37 - 37: ooOoO0O00 * Ii
elif oO0oo0o00o0O == 45 :
 TEXTS ( )
 if 95 - 95: Ii % ii1ii11IIIiiI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif oO0oo0o00o0O == 46 :
 I1ii ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / O00o0O00 / ii1ii11IIIiiI
elif oO0oo0o00o0O == 47 :
 GEVID ( )
 if 35 - 35: Ii1IIIi1 * O00o0O00
elif oO0oo0o00o0O == 48 :
 IiiiI111I ( oO00oooOOoOo0 , i1I1ii11i1Iii , O0000OOO0 )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif oO0oo0o00o0O == 49 :
 O0O0ooOOO ( )
 if 13 - 13: oO0o * ii1ii11IIIiiI + I1ii11iIi11i - ooOOOoO
elif oO0oo0o00o0O == 222 :
 oOOO00o000o ( i1I1ii11i1Iii )
 if 31 - 31: oO0o
elif oO0oo0o00o0O == 333 :
 III11i ( i1I1ii11i1Iii )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - ii1ii11IIIiiI . Ii1I % I1ii11iIi11i . iI1ii11iIi1i
elif oO0oo0o00o0O == 1020 :
 oo000O0o ( )
 if 9 - 9: I11i
elif oO0oo0o00o0O == 1021 :
 ANIMEEP ( )
 if 55 - 55: O00o0O00 % iI11I1II1I1I + I11O0O0oOO00O00o . O0OOOoOoo0
elif oO0oo0o00o0O == 1022 :
 ANIMEPLAY ( i1I1ii11i1Iii )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif oO0oo0o00o0O == 1001 :
 IiI1I1iii ( )
 if 23 - 23: Ii
elif oO0oo0o00o0O == 1005 :
 oOOoOo0OoOO ( )
 if 88 - 88: IIiIiII11i - Ii1IIIi1 / ii
elif oO0oo0o00o0O == 1007 :
 OO00o ( i1I1ii11i1Iii )
 if 71 - 71: Ii1I
elif oO0oo0o00o0O == 1010 :
 IIi1IIII ( i1I1ii11i1Iii )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif oO0oo0o00o0O == 1011 :
 OOI1 ( i1I1ii11i1Iii )
 if 1 - 1: ooOOOoO % ooOoO0O00
elif oO0oo0o00o0O == 1012 :
 O00O ( i1I1ii11i1Iii )
 if 41 - 41: oO0o * oO0o / Ii1IIIi1 + Ii1I . I11i
elif oO0oo0o00o0O == 1030 :
 oooO00oOOooO ( )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / iI1ii11iIi1i
elif oO0oo0o00o0O == 1031 :
 iiiiI ( i1I1ii11i1Iii , oOoooo000Oo00 )
 if 80 - 80: Ii1I
elif oO0oo0o00o0O == 1032 :
 O000OoOO0oO ( i1I1ii11i1Iii )
 if 67 - 67: IIiIiII11i
elif oO0oo0o00o0O == 1006 :
 Parse . ParseURL ( i1I1ii11i1Iii )
 if 2 - 2: I11i - o0o00Oo0O * iI1ii11iIi1i % ooOOOoO
elif oO0oo0o00o0O == 2030 :
 Parse . addonParseURL ( i1I1ii11i1Iii )
 if 64 - 64: ooOoO0O00 . O0OOOoOoo0
elif oO0oo0o00o0O == 2031 :
 Parse . apkParseURL ( i1I1ii11i1Iii )
 if 7 - 7: oO0oo0o . Ii1IIIi1 - Ii1IIIi1 / ii1ii11IIIiiI % I1ii11iIi11i
elif oO0oo0o00o0O == 1002 :
 IIII1iI1IiIiI ( i1I1ii11i1Iii )
 if 61 - 61: oO0oo0o - Ii1I / Ii1IIIi1 % Ii1I + oO0o / I1ii11iIi11i
elif oO0oo0o00o0O == 1003 :
 i1II1 ( i1I1ii11i1Iii , oOoooo000Oo00 )
 if 10 - 10: Ii / OOooOOo
elif oO0oo0o00o0O == 1004 :
 OoOoOoo0oOOooo0o ( i1I1ii11i1Iii )
 if 27 - 27: oOo0O0Ooo / ii
elif oO0oo0o00o0O == 1008 :
 o0oOO0 ( )
 if 74 - 74: Ii1I % ii1ii11IIIiiI - oO0o * I11O0O0oOO00O00o . ii * oO0o
elif oO0oo0o00o0O == 1009 :
 OooOoO0OO00 ( i1I1ii11i1Iii )
 if 99 - 99: OOooOOo . Ii1IIIi1 - ii - o0o00Oo0O
elif oO0oo0o00o0O == 2001 :
 ii1II1 ( )
 if 6 - 6: O00o0O00
elif oO0oo0o00o0O == 2002 :
 o0oIi1iiiii ( i1I1ii11i1Iii )
 if 3 - 3: o0o00Oo0O - ii1ii11IIIiiI * iI1ii11iIi1i * O00o0O00 / iI1ii11iIi1i
elif oO0oo0o00o0O == 1013 :
 o0o0O0Oo ( )
elif oO0oo0o00o0O == 10111113 :
 IiiIIi ( i1I1ii11i1Iii )
 if 58 - 58: iI1ii11iIi1i * iI11I1II1I1I + O0OOOoOoo0 . O0OOOoOoo0
elif oO0oo0o00o0O == 1014 :
 i111iiIiiIiI ( )
 if 74 - 74: O0OOOoOoo0 - I11i * ooOOOoO % O0OOOoOoo0
elif oO0oo0o00o0O == 1015 :
 OOooooO ( i1I1ii11i1Iii )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * ii1ii11IIIiiI - oO0o - I11i
elif oO0oo0o00o0O == 1016 :
 ii1i1I1111ii ( i1I1ii11i1Iii , oOoooo000Oo00 , oO00oooOOoOo0 )
 if 44 - 44: ii
elif oO0oo0o00o0O == 1017 :
 iII1i11IIi1i ( )
 if 82 - 82: OOooOOo . OOooOOo
elif oO0oo0o00o0O == 1018 :
 ooOoo ( i1I1ii11i1Iii )
 if 10 - 10: I1ii11iIi11i * Ii1I . oO0oo0o . ii . O00o0O00 * Ii1I
elif oO0oo0o00o0O == 1023 :
 Ii1I11I ( )
 if 80 - 80: ii1ii11IIIiiI + I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00
elif oO0oo0o00o0O == 1024 :
 iI1ii ( i1I1ii11i1Iii )
 if 85 - 85: Ii . I11O0O0oOO00O00o + iI1ii11iIi1i / iI1ii11iIi1i
elif oO0oo0o00o0O == 1025 :
 iII1I1IIiiiI ( i1I1ii11i1Iii )
 if 43 - 43: ooOOOoO . ii - IIiIiII11i
elif oO0oo0o00o0O == 4001 :
 oo0O0 ( )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * O00o0O00 * oO0oo0o
elif oO0oo0o00o0O == 4002 :
 O000OOO ( )
 if 19 - 19: ii1ii11IIIiiI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif oO0oo0o00o0O == 4003 :
 IIi1II ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif oO0oo0o00o0O == 4004 :
 I1II1 ( )
 if 15 - 15: iI1ii11iIi1i + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif oO0oo0o00o0O == 4005 :
 Iii11iI1i ( )
 if 54 - 54: ooOOOoO - IIiIiII11i . O0OOOoOoo0 + iI1ii11iIi1i
elif oO0oo0o00o0O == 4006 :
 o0O0OOOOoOO0 ( )
 if 45 - 45: oO0oo0o + IIiIiII11i . Ii1IIIi1 / Ii1I
elif oO0oo0o00o0O == 4007 :
 O0O0o0oOOO ( )
 if 76 - 76: iI1ii11iIi1i + Ii1IIIi1 - ooOOOoO * iI11I1II1I1I % ooOoO0O00
elif oO0oo0o00o0O == 4008 :
 OOoOoOo ( )
 if 72 - 72: O0OOOoOoo0 + IIiIiII11i . o0o00Oo0O - Ii1IIIi1 / ii . ii1ii11IIIiiI
elif oO0oo0o00o0O == 4009 : oooO ( )
elif oO0oo0o00o0O == 4010 : oO0o00oOOooO0 ( )
elif oO0oo0o00o0O == 3000 :
 O0oO0ooOOo ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif oO0oo0o00o0O == 3001 :
 i1I1I1I ( )
 if 32 - 32: ii
elif oO0oo0o00o0O == 3002 :
 iII1III ( i1I1ii11i1Iii )
 if 29 - 29: Ii1I
elif oO0oo0o00o0O == 3003 :
 O0oo0oO00o ( i1I1ii11i1Iii )
 if 41 - 41: iI1ii11iIi1i
elif oO0oo0o00o0O == 3004 :
 o0Ii11iIiiI ( i1I1ii11i1Iii )
 if 49 - 49: iI1ii11iIi1i % IIiIiII11i . iI1ii11iIi1i - I11i - I11O0O0oOO00O00o * ooOOOoO
elif oO0oo0o00o0O == 404 :
 O0Oo00o0o ( oO00oooOOoOo0 , i1I1ii11i1Iii , oOoooo000Oo00 )
 if 47 - 47: o0o00Oo0O . I11i / iI1ii11iIi1i * Ii1IIIi1
elif oO0oo0o00o0O == 405 :
 O00o ( i1I1ii11i1Iii )
 if 63 - 63: ii1ii11IIIiiI - oO0oo0o - Ii1IIIi1 - O0OOOoOoo0 / oO0oo0o + oO0o
elif oO0oo0o00o0O == 7030 :
 iIII1I1i ( )
 if 94 - 94: ooOOOoO / oOo0O0Ooo . IIiIiII11i
elif oO0oo0o00o0O == 7021 :
 iIiIiiIIIi1 ( oO00oooOOoOo0 )
 if 32 - 32: oO0oo0o . O00o0O00 % O00o0O00 . OOooOOo
elif oO0oo0o00o0O == 7022 :
 o0oOOO ( oO00oooOOoOo0 )
 if 37 - 37: O00o0O00 + o0o00Oo0O + O00o0O00 . Ii1IIIi1 . I11i
elif oO0oo0o00o0O == 7000 :
 i11III1I ( oO00oooOOoOo0 , i1I1ii11i1Iii , img )
 if 78 - 78: oOo0O0Ooo / I11O0O0oOO00O00o + I11i . I1ii11iIi11i / o0o00Oo0O
elif oO0oo0o00o0O == 7050 :
 Oo00oo00o00Oo ( i1I1ii11i1Iii )
 if 49 - 49: Ii1I
elif oO0oo0o00o0O == 7051 :
 iiiiOOOO00 ( i1I1ii11i1Iii )
 if 66 - 66: I11i . Ii1I
elif oO0oo0o00o0O == 7052 :
 I1i1ii1ii ( i1I1ii11i1Iii )
 if 18 - 18: I1ii11iIi11i + ooOOOoO
elif oO0oo0o00o0O == 7053 :
 i1ii ( i1I1ii11i1Iii )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % iI1ii11iIi1i . oOo0O0Ooo
elif oO0oo0o00o0O == 7054 :
 CoolPlay ( i1I1ii11i1Iii )
 if 43 - 43: oOo0O0Ooo % Ii1I * iI1ii11iIi1i
elif oO0oo0o00o0O == 7060 :
 IiIIii ( )
 if 31 - 31: iI1ii11iIi1i / Ii1IIIi1
elif oO0oo0o00o0O == 7061 :
 O00000OO00OO ( i1I1ii11i1Iii )
 if 3 - 3: ooOOOoO
elif oO0oo0o00o0O == 7063 :
 oo0O0Ii111Ii11 ( i1I1ii11i1Iii )
 if 37 - 37: iI1ii11iIi1i * ii * I11O0O0oOO00O00o + I1ii11iIi11i . oOo0O0Ooo
elif oO0oo0o00o0O == 7062 :
 I1ii1i11iI1 ( i1I1ii11i1Iii )
 if 61 - 61: O00o0O00 . O00o0O00
elif oO0oo0o00o0O == 7064 :
 NATatozcat ( )
 if 17 - 17: IIiIiII11i / O0OOOoOoo0
elif oO0oo0o00o0O == 7067 :
 IiOOo0 ( i1I1ii11i1Iii )
 if 80 - 80: O00o0O00 * oO0o + iI1ii11iIi1i
elif oO0oo0o00o0O == 7066 :
 NATatozA ( i1I1ii11i1Iii )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif oO0oo0o00o0O == 7065 :
 o0O0O0O00o ( i1I1ii11i1Iii )
 if 98 - 98: I11i * I1ii11iIi11i - iI1ii11iIi1i . O0OOOoOoo0
elif oO0oo0o00o0O == 7070 :
 iii1IiiIiIIiI ( )
 if 2 - 2: I1ii11iIi11i - O0OOOoOoo0 % iI11I1II1I1I
elif oO0oo0o00o0O == 7071 :
 DIZIlist ( i1I1ii11i1Iii )
 if 88 - 88: ii1ii11IIIiiI - oO0o
elif oO0oo0o00o0O == 7072 :
 DIZIpull ( i1I1ii11i1Iii )
 if 79 - 79: Ii1IIIi1
elif oO0oo0o00o0O == 7073 :
 WATCHDIZI ( i1I1ii11i1Iii )
 if 45 - 45: IIiIiII11i + Ii1IIIi1 . I11O0O0oOO00O00o . o0o00Oo0O * ooOoO0O00 - iI1ii11iIi1i
elif oO0oo0o00o0O == 7002 :
 oOoOII1i1 ( )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif oO0oo0o00o0O == 7003 :
 I11iiI11I1II ( i1I1ii11i1Iii )
 if 76 - 76: Ii1I
elif oO0oo0o00o0O == 7004 :
 iiI1 ( i1I1ii11i1Iii )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . iI1ii11iIi1i
elif oO0oo0o00o0O == 7020 :
 o0OOo0O00OO0O ( i1I1ii11i1Iii )
 if 51 - 51: iI1ii11iIi1i + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif oO0oo0o00o0O == 7001 :
 iI1III ( )
 if 20 - 20: ii1ii11IIIiiI . I11O0O0oOO00O00o . iI1ii11iIi1i + I11O0O0oOO00O00o - O00o0O00 * oO0oo0o
elif oO0oo0o00o0O == 7010 :
 IiI1 ( i1I1ii11i1Iii )
 if 82 - 82: oO0o
elif oO0oo0o00o0O == 7011 :
 Ii1Iiiiii ( i1I1ii11i1Iii )
 if 78 - 78: IIiIiII11i / I11O0O0oOO00O00o - Ii + Ii1I * I1ii11iIi11i
elif oO0oo0o00o0O == 7012 :
 O0ooO ( i1I1ii11i1Iii )
 if 17 - 17: OOooOOo
elif oO0oo0o00o0O == 7013 :
 cnfTVPlay2 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oO00oooOOoOo0 , i1I1ii11i1Iii , oOoooo000Oo00 )
elif oO0oo0o00o0O == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oO0oo0o00o0O == 7018 :
 I11II ( )
elif oO0oo0o00o0O == 7019 :
 CNF_Studio_Indexer . List_Movies ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7024 :
 CNF_Studio_Indexer . Box_Office ( i1I1ii11i1Iii )
 if 72 - 72: Ii1IIIi1 . I1ii11iIi11i - Ii / oOo0O0Ooo
elif oO0oo0o00o0O == 8000 :
 ooOoOoo000O0O ( )
elif oO0oo0o00o0O == 8001 :
 o0oo0OooOO0 ( )
elif oO0oo0o00o0O == 8002 :
 iiIIiii1iii1I ( )
elif oO0oo0o00o0O == 8003 :
 Iii1II1 ( )
elif oO0oo0o00o0O == 8004 :
 oo00o000O ( )
elif oO0oo0o00o0O == 8005 :
 o0OoOo0O00 ( )
elif oO0oo0o00o0O == 8006 :
 I1iII ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8030 :
 iii1III1i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8045 :
 iiIiIiIiiIiI ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8046 :
 iIi1i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8047 :
 iIiII11 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8048 :
 i1i1Ii1IiIII ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8049 :
 I1IIii11 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 804900 :
 I1I1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8020 :
 iIiii1iI1Ii ( )
elif oO0oo0o00o0O == 8021 :
 ooIi ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8022 :
 oO0oOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8023 :
 IIiIiii ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8040 :
 O0O0 ( )
elif oO0oo0o00o0O == 8041 :
 oO0ooo00o0o000Oo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8042 :
 iiIIIIiii ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8043 :
 yt . PlayVideo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8044 :
 iiii1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8060 :
 oOo000O00O0 ( )
elif oO0oo0o00o0O == 8061 :
 iI1iiIii1I11I ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8064 :
 Oo ( )
elif oO0oo0o00o0O == 8065 :
 o0oOOoo0O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8070 :
 OoO0o0oOOO ( )
elif oO0oo0o00o0O == 8071 :
 oO0I1I1i1I1I1I1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7080 :
 iI11IiIiiII1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8090 :
 iIi11iI1i ( )
elif oO0oo0o00o0O == 8091 :
 Ii1iIi ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8092 :
 IIIooo0o0O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8093 :
 OOo0OOOoOOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8081 :
 IiIiII11i1 ( )
elif oO0oo0o00o0O == 8062 :
 iI1iIi ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8063 :
 O0Ooo00o00O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8050 :
 OoO00o0 ( )
elif oO0oo0o00o0O == 8051 :
 ooo0oOOO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8052 :
 oOOOiI1iIIII1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8085 :
 o00OOo00 ( )
elif oO0oo0o00o0O == 8086 :
 ooOo0O0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8087 :
 iIIi111IiII1i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 8088 :
 oOo0O000oo0 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif oO0oo0o00o0O == 9000 :
 ii1I11iIiIII1 ( )
elif oO0oo0o00o0O == 1111 :
 iiiiI11 ( )
elif oO0oo0o00o0O == 9001 :
 I1iii1I ( )
elif oO0oo0o00o0O == 9002 :
 OO0OOOOOo ( )
elif oO0oo0o00o0O == 9003 :
 iIi1iii1 ( )
elif oO0oo0o00o0O == 9004 :
 World1 ( )
elif oO0oo0o00o0O == 9005 :
 World2 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9006 :
 World3 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9007 :
 oOO0o00 ( )
elif oO0oo0o00o0O == 9008 :
 IIi1IIiII ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9009 :
 oooOoO00Oo0O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9010 :
 IIIi11i ( )
elif oO0oo0o00o0O == 9011 :
 oooOOoo0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 50 :
 IIiooOoO0OO0oOO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9020 :
 champlist ( )
elif oO0oo0o00o0O == 9021 :
 iIii1iIiII1i1 ( )
elif oO0oo0o00o0O == 9022 :
 o0oO ( )
elif oO0oo0o00o0O == 9023 :
 o0OoIII1IIiIi1 ( )
elif oO0oo0o00o0O == 9024 :
 iIIi1II1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9030 :
 IiI111I ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9031 :
 oo0oO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9032 :
 ii1i1Iii ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9033 :
 IIII11111Ii ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 9034 :
 o0oooOO00 ( )
elif oO0oo0o00o0O == 7085 :
 III11iI1i11i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7086 :
 o0oo000 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 7087 :
 OoOIiiIi1IiiiI ( O0000OOO0 )
elif oO0oo0o00o0O == 9666 :
 OoOoO0OoOOOOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10100 : IIi1Iii1I11iI ( )
elif oO0oo0o00o0O == 10105 : III ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10106 : IIiII11 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10104 : iiiII1III ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10107 : iIII ( )
elif oO0oo0o00o0O == 10103 : IiIiI ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10108 : oOoOO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10107 : iIII ( )
elif oO0oo0o00o0O == 10000 : Origin_Menu ( )
elif oO0oo0o00o0O == 10001 : oO00 ( )
elif oO0oo0o00o0O == 10002 : IiI1i111i ( )
elif oO0oo0o00o0O == 10003 : II1i11 ( )
elif oO0oo0o00o0O == 10004 : o0oOOOO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10005 : oOooo00O ( )
elif oO0oo0o00o0O == 10006 : I1III1iIi ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10007 : ooooo0O0 ( i1I1ii11i1Iii , oOoooo000Oo00 )
elif oO0oo0o00o0O == 10008 : I1iII1IIi1IiI ( )
elif oO0oo0o00o0O == 10009 : IiiI1I ( )
elif oO0oo0o00o0O == 10010 : Ii1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10011 : oOOo0ooO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10012 : oO00O0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10109 : oOoOooO0OOOoo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10013 : Oo0000OOO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10014 : I1i1I1II ( )
elif oO0oo0o00o0O == 10015 : o0OoOOo ( )
elif oO0oo0o00o0O == 10016 : oOOoOOO0oo0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10017 : ooOoo000oO ( )
elif oO0oo0o00o0O == 10018 : OOoOO0O0o0 ( )
elif oO0oo0o00o0O == 10019 : IIiiiiIiI1III ( )
elif oO0oo0o00o0O == 10020 : OOOO00OoooO ( )
elif oO0oo0o00o0O == 10021 : O0oo0 ( )
elif oO0oo0o00o0O == 10022 : Ii1I1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10023 : o0O0ooooooo00 ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10024 : IiiIIiI1iI1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10025 : o0o ( )
elif oO0oo0o00o0O == 10026 : oO0o00O0O0oo0 ( )
elif oO0oo0o00o0O == 10027 : Oo000O ( )
elif oO0oo0o00o0O == 10028 : I111iiiii1 ( )
elif oO0oo0o00o0O == 10029 : i1ii1iiIi1II ( )
elif oO0oo0o00o0O == 423 : Ii11ii1I1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 426 : OO00oo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10030 : Izle_Films ( )
elif oO0oo0o00o0O == 10031 : Latest_Izle_Movies ( )
elif oO0oo0o00o0O == 10032 : Izle_Genres ( )
elif oO0oo0o00o0O == 10033 : Izle_Pop_Movies ( )
elif oO0oo0o00o0O == 10034 : Izle_Boxsets ( )
elif oO0oo0o00o0O == 10035 : Izle_Search ( )
elif oO0oo0o00o0O == 10036 : Izle_Genres_Movie ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10037 : Izle_Boxset_single ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10038 : Izle_IFRAME ( )
elif oO0oo0o00o0O == 10039 : Izle_Boxsets_Next ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10040 : II11iIIii ( )
elif oO0oo0o00o0O == 10041 : oooOoo0OoOO0000 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10042 : I11iiI1I1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10043 : ooIiI11i1I11111 ( )
elif oO0oo0o00o0O == 10044 : oOOOooO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10045 : I1IIIIIi1IIiI ( oO00oooOOoOo0 )
elif oO0oo0o00o0O == 10046 : iI1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10047 : ooo0o0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10048 : ooO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10049 : OoOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10050 : i1111I1iii1 ( )
elif oO0oo0o00o0O == 10051 : oOo ( )
elif oO0oo0o00o0O == 10052 : ooOoo000 ( )
elif oO0oo0o00o0O == 10053 : Addon ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10054 : o00OoOO00 ( i1I1ii11i1Iii , oO00oooOOoOo0 )
elif oO0oo0o00o0O == 10055 :
 I1ii1Ii1 ( "addFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO0OOOOo0000O ( oO00oooOOoOo0 , i1I1ii11i1Iii , oOoooo000Oo00 , oOo0O , iiii1I1 )
elif oO0oo0o00o0O == 10056 :
 I1ii1Ii1 ( "rmFavorite" )
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oO00oooOOoOo0 = oO00oooOOoOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0OooOO ( oO00oooOOoOo0 )
elif oO0oo0o00o0O == 10057 :
 I1ii1Ii1 ( "getFavorites" )
 iiiI1iI1 ( )
elif oO0oo0o00o0O == 10058 : i1I1i111Ii ( )
elif oO0oo0o00o0O == 10059 : Donators_Guide ( )
elif oO0oo0o00o0O == 10060 : Ooo0oo ( )
elif oO0oo0o00o0O == 10061 : IioO0O ( )
elif oO0oo0o00o0O == 10062 : IiIi1i1ii ( oO00oooOOoOo0 , i1I1ii11i1Iii , O0000OOO0 )
elif oO0oo0o00o0O == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOoOooOo0o0 + ")" )
elif oO0oo0o00o0O == 10064 : IiI11iI1i1i1i ( )
elif oO0oo0o00o0O == 10065 : I1iIIIi1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10066 : ooo000ooO0000 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10068 : II1i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10069 : I1iii11 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10070 : oOOOOoo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10071 : Genie_Watch ( )
elif oO0oo0o00o0O == 10072 : I11i1II ( )
elif oO0oo0o00o0O == 10073 : O0OOoOOO0oO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10074 : O0o ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10075 : o0OIiiiI ( oOoooo000Oo00 , oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10076 : OO0oOOoo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10077 : iIi1i1iIi1iI ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10078 : ooo000o000 ( )
elif oO0oo0o00o0O == 10079 : Genie_Watch_Tv_Shows ( )
elif oO0oo0o00o0O == 10080 : Genie_Watch_Tv_Genre ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10081 : Genie_Watch_TV_PlayRun ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10082 : Genie_Watch_TV_Episodes ( i1I1ii11i1Iii , oOoooo000Oo00 )
elif oO0oo0o00o0O == 10083 : Genie_Watch_Tv_Recent ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 10084 : I11iI ( )
elif oO0oo0o00o0O == 10085 : IiI111111IIII ( )
elif oO0oo0o00o0O == 10086 : ooOOO00Ooo ( )
elif oO0oo0o00o0O == 20000 : ii1ii1I1IIi1 ( )
elif oO0oo0o00o0O == 20001 : Ii1i1 ( )
elif oO0oo0o00o0O == 20002 : oo0oo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 20003 : oooo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 20004 : iii1IIiI ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 21004 : O00oo ( )
elif oO0oo0o00o0O == 21005 : OoOo0oO0o ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 21006 : i111i ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 21007 : Oo0oOo0ooOOOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30000 : I1I11ii ( )
elif oO0oo0o00o0O == 30001 : iiii ( )
elif oO0oo0o00o0O == 10012 : Resolve ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30003 : iI1IiiiIiI1Ii ( )
elif oO0oo0o00o0O == 30004 : oOo00Ooo0o0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30005 : oOO0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30006 : o0OooOo ( )
elif oO0oo0o00o0O == 30007 : o0O0oo0o ( )
elif oO0oo0o00o0O == 30008 : OO0I111i1I ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30009 : iIii1iII1Ii ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30010 : O00OO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30011 : II1 ( )
elif oO0oo0o00o0O == 30012 : OOOo ( )
elif oO0oo0o00o0O == 30013 : I1I11IiiI ( )
elif oO0oo0o00o0O == 30014 : OO ( )
elif oO0oo0o00o0O == 30015 : OOoo0 ( i1I1ii11i1Iii , oOoooo000Oo00 , oOo0O )
elif oO0oo0o00o0O == 30016 : IiI1i111IiIiIi1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30019 : iiIi1I1i1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30017 : i1IIi1i1Ii1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30018 : IIIIIIII ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30030 : i1I111I1Iii1 ( )
elif oO0oo0o00o0O == 30031 : O00Oo0 ( )
elif oO0oo0o00o0O == 30032 : o0Oooo0 ( )
elif oO0oo0o00o0O == 30033 : ii1iIIi11 ( )
elif oO0oo0o00o0O == 30034 : iI1IIIII1Ii ( )
elif oO0oo0o00o0O == 30035 : OOooooo0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30036 : oOOII1i11i1iIi11 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30037 : oo0O0oO0O0O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 30038 : iIIIiiiI11I ( )
elif oO0oo0o00o0O == 30039 : OoOO0OOoo ( )
elif oO0oo0o00o0O == 50000 : IIiiIiII1Ii ( )
elif oO0oo0o00o0O == 50001 : OO00O000OOO ( )
elif oO0oo0o00o0O == 50002 : I11III11III1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 50003 : i1i1I11i1I ( O0000OOO0 )
elif oO0oo0o00o0O == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oO0oo0o00o0O == 60001 : OoOiIIiii ( )
elif oO0oo0o00o0O == 60002 : iIi1II ( oO00oooOOoOo0 )
elif oO0oo0o00o0O == 60003 : i1i1i1I ( oO00oooOOoOo0 )
elif oO0oo0o00o0O == 50004 : OO0ooOOO0OOO ( )
elif oO0oo0o00o0O == 50005 : speedtest . runtest ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 70001 : iIIiI1iiI ( )
elif oO0oo0o00o0O == 70002 : O0Oo00OO00Ooo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 70003 : OO0O00OoOOOo ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 70004 : Oo0 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 70005 : o0OOOOO0O ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 70006 : I1I1IiIi1 ( )
elif oO0oo0o00o0O == 50006 : O0O0Oooo0o ( i1 , i1111 )
elif oO0oo0o00o0O == 80000 : OooOo000OOOOo ( )
elif oO0oo0o00o0O == 80001 : resolvefilmon ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80002 : o0O0Oo0Ooo0 ( )
elif oO0oo0o00o0O == 80003 : Iiii1 ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80004 : oOo0OI11i ( oO00oooOOoOo0 , i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80005 : I1ii1ii11i1I ( )
elif oO0oo0o00o0O == 80006 : o0OoOO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80007 : oOoO00o ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80008 : IIi1IIIi ( )
elif oO0oo0o00o0O == 80009 : O0O0O ( )
elif oO0oo0o00o0O == 80010 : II1io0Oo00oOO ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80011 : IiI1IiI1iiI1 ( i1I1ii11i1Iii )
elif oO0oo0o00o0O == 80012 : ii1O0Ooo0O ( )
if 64 - 64: oO0oo0o
if 80 - 80: I11i % iI11I1II1I1I
if 63 - 63: ooOOOoO * Ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
if 86 - 86: I11O0O0oOO00O00o % I11O0O0oOO00O00o - OOooOOo + ii1ii11IIIiiI / oOo0O0Ooo * ii
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
IiI1iIIiIi1Ii = StorageServer . StorageServer ( "plugin.video.GenieTv" , 24 )
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
if 9 - 9 : Ii . o0o00Oo0O - iI11I1II1I1I
if 71 - 71 : ii
O0oOoOOO000 = ''
def oOo00o0oO ( i , t1 , t2 = [ ] ) :
 iIiIi = O0oOoOOO000
 for I1Iii11II in t1 :
  iIiIi += chr ( I1Iii11II )
  i += 1
  if i > 1 :
   iIiIi = iIiIi [ : - 1 ]
   i = 0
 for I1Iii11II in t2 :
  iIiIi += chr ( I1Iii11II )
  i += 1
  if i > 1 :
   iIiIi = iIiIi [ : - 1 ]
   i = 0
 return iIiIi
 if 40 - 40 : ooOoO0O00 * IIiIiII11i
 if 51 - 51 : oOo0O0Ooo * I1ii11iIi11i
 if 48 - 48 : oO0o / OOooOOo / I11i / Ii1I
ii11III1 = "3.1.7"
OOOoO0oo0oo0o = 'plugin.video.GenieTv'
oo0OO0O = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
ooooO0 = xbmc . translatePath ( 'special://home/addons/' )
II1IooOO00Oo = xbmc . translatePath ( 'special://home/addonsbroke/' )
I11ii1i1I = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
i11IIii1I11 = 'plugin.video.GenieTv'
iIoo0 = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
o0OoO = xbmcaddon . Addon ( id = i11IIii1I11 )
OOOo00OOooO = xbmc . translatePath ( 'special://home/media' )
OO0OOOoO0O0 = 'plugin.video.GenieTv'
iII1I1iIi1i = xbmcgui . DialogProgress ( )
O0OO0o = '[COLORsteelblue]GenieTv[/COLOR]'
Ii11IiiI = base64 . b64decode ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3BlZWR0ZXN0LnR4dA==' )
iII11iiI1i11I = uservar . CONTACT
I1Iii1III = base64 . decodestring
Oo0oo0OoO0o0 = xbmc . translatePath ( 'special://home/' )
I1IO0 = os . path . join ( Oo0oo0OoO0o0 , 'userdata' )
i1I1Iii1IiiIi = os . path . join ( I1IO0 , 'addon_data' , OOOoO0oo0oo0o )
OoOo00ooOO000 = os . path . join ( i1I1Iii1IiiIi , 'wizard.log' )
iIOoO0O00o0ooo0 = uservar . ADDONTITLE
o0oOoooOoo0 = xbmc . translatePath ( 'special://profile/' )
IiI1Iii1iIIII = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
ooooO0 = os . path . join ( Oo0oo0OoO0o0 , 'addons' )
oo0 = os . path . join ( ooooO0 , 'packages' )
o00OoO00o0 = os . path . join ( ooooO0 , 'HUB' )
ooOOO = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
ii111II = Net ( )
ooOOoOoOoO00 = xbmcgui . Dialog ( )
OO0oo00O = o0OoO . getSetting ( 'Build' )
ooOiiIII = o0OoO . getSetting ( 'Local' )
ii1IooO00OO0ooo = o0OoO . getSetting ( 'Remote' )
O0oi1i1ii1Ii111i = o0OoO . getSetting ( 'LocalM3u' )
iiiI1iiI11iii = o0OoO . getSetting ( 'TEXTCOL' )
o0O0oOOoo0O0 = xbmc . translatePath ( 'special://logpath/' )
OO00OOo = o0OoO . getSetting ( 'User' )
IiI11i1IiI1 = o0OoO . getSetting ( 'Pass' )
o00oOO00 = o0OoO . getSetting ( 'AdultPass' )
ooOOoOoOoO00 = xbmcgui . Dialog ( )
Oo0oo0OoO0o0 = xbmc . translatePath ( 'special://home/' )
o00O0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i11IIii1I11 , 'fanart.jpg' ) )
i1OOO00oO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + i11IIii1I11 , 'icon.png' ) )
IIi1OOoO0OooO = ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
IiiOo = xbmc . translatePath ( 'special://database' )
iiiIiii11i1i = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
ooo0O0Oo0O = xbmc . translatePath ( 'special://thumbnails' ) ;
Oo0o = "GenieTv"
i1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
OO00O0O00oOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
ii1111iIIiIIi = 'http://'
ooOo0Oo = base64 . decodestring ( 'LnBocA==' )
I11i1I111II1IiI = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
oo00O0oOo = [ ]
IiI1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
oOO00o0oooOo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
iIII1iIi = o0OoO . getLocalizedString
iiii1Ii = CookieJar ( )
IIiiiIii11 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( iiii1Ii ) )
IIiiiIii11 . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
iI1i1i1i1i = int ( sys . argv [ 1 ] )
iiII1i1II1iIi = xbmc . translatePath ( o0OoO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iII = os . path . join ( iiiIiii11i1i , 'favorites' )
OOOO0o0Oo0 = iiiIiii11i1i + '/addons.ini'
I1IO0 = xbmc . translatePath ( 'special://home/userdata/' )
I1iIiI1iiI = xbmc . translatePath ( 'special://home/userdatabroke/' )
oO000O00 = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
IiIIIii1iIII1 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
OoOooooo0oo = IiIIIii1iIII1 + 'GenieTvWatched'
if not os . path . exists ( OoOooooo0oo ) :
 os . makedirs ( OoOooooo0oo )
ii1II1i1I1II11I1 = OoOooooo0oo + 'watched.txt'
if not os . path . exists ( ii1II1i1I1II11I1 ) :
 open ( ii1II1i1I1II11I1 , 'w+' )
oo0o = open ( ii1II1i1I1II11I1 ) . read ( )
OoOoo = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
O0oOoOooo00oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
OOO0OO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
II1IiII1I1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
oooOII111iiI1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( iII ) == True :
 oo0oO0oO00oO = open ( iII ) . read ( )
else : oo0oO0oO00oO = [ ]
o0OOo000ooo0o = o0OoO . getSetting ( 'debug' )
if os . path . exists ( iiiIiii11i1i ) == False :
 os . makedirs ( iiiIiii11i1i )
def oo00oO0o000 ( url ) :
 iIi1ii = urllib2 . Request ( url )
 iIi1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1I11 = ''
 I1iIIiI1i = ''
 try :
  I1I11 = urllib2 . urlopen ( iIi1ii )
  I1iIIiI1i = I1I11 . read ( )
  I1I11 . close ( )
 except : pass
 if I1iIIiI1i != '' :
  return I1iIIiI1i
 else :
  I1iIIiI1i = 'Failed'
  return I1iIIiI1i
  if 84 - 84 : oO0oo0o * O00o0O00 . I11O0O0oOO00O00o + iI1ii11iIi1i
O0oOOOOooOo0 = [ ]
o0000o0OOOo = oo00oO0o000 ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if o0000o0OOOo != 'Failed' :
 O0oOOOOooOo0 . append ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not o0000o0OOOo != 'Failed' :
 iiiiiI1iii11 = oo00oO0o000 ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if iiiiiI1iii11 != 'Failed' :
  O0oOOOOooOo0 . append ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not iiiiiI1iii11 != 'Failed' :
  IIIi11iiIIi = oo00oO0o000 ( I1Iii1III ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if IIIi11iiIIi != 'Failed' :
   O0oOOOOooOo0 . append ( I1Iii1III ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not IIIi11iiIIi != 'Failed' :
   oOo000O00O = oo00oO0o000 ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if oOo000O00O != 'Failed' :
    O0oOOOOooOo0 . append ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
OooO = ( str ( O0oOOOOooOo0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
ooOOoOO000 = OooO + 'GenieArt/NEW/'
if 61 - 61 : Ii1IIIi1
if 86 - 86 : ooOOOoO % ii1ii11IIIiiI - O0OOOoOoo0 - I1ii11iIi11i
def oOO0i1 ( ) :
 if not os . path . exists ( oo0OO0O ) :
  ooOOoOoOoO00 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  i1iIi1IiI = 'genie tv repo not being installed '
  i11i11Iii ( )
 else :
  OO0o00Oo0oo0 ( )
  if 68 - 68 : Ii % Ii1I + Ii
def OO0o00Oo0oo0 ( ) :
 if 31 - 31 : IIiIiII11i . oOo0O0Ooo
 I11Oo0O00O0O00 = II1I1i ( I1Iii1III ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 O00OoOo0OooOo = open ( II1IiII1I1II ) . read ( )
 OOooOoOOo0O = open ( oooOII111iiI1Ii1 ) . read ( )
 if 91 - 91 : Ii1IIIi1 % ooOoO0O00 % iI11I1II1I1I
 IIi11ii = re . compile ( 'version="([^"]*)" provider' ) . findall ( O00OoOo0OooOo )
 OOOO0oO0OOo0o = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( OOooOoOOo0O )
 OoOOii = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( I11Oo0O00O0O00 )
 iiI = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( I11Oo0O00O0O00 )
 for ooo0O0O0OO in IIi11ii :
  oOooOOoO = ooo0O0O0OO
  for o0o000OOO in OoOOii :
   if not o0o000OOO == oOooOOoO :
    iII1I1iIi1i . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    iII1I1iIi1i . close
    I1111iii1ii11 ( )
   if o0o000OOO == oOooOOoO :
    Oooo
 for III1II1I1iI in OOOO0oO0OOo0o :
  oOOOO = III1II1I1iI
  for Oo0OO0o0oOO0 in iiI :
   if not Oo0OO0o0oOO0 == oOOOO :
    iII1I1iIi1i . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    iII1I1iIi1i . close
    i11i11Iii ( )
   if Oo0OO0o0oOO0 == oOOOO :
    xbmc . sleep ( 100 )
    Oooo
def i1II1IiIIi ( ) :
 oOO0i1 ( )
 o0O0 ( )
 iiIi1I1IIIII1IIi ( i11iii1II1I1 )
 if not os . path . exists ( o00OoO00o0 ) :
  IiIi11iI1IIi ( )
  if 80 - 80 : ii1ii11IIIiiI . Ii - I11i
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']CONTACT US[/COLOR]' , '' , 50006 , ooOOoOO000 + 'Contact-Us.png' , o00O0oOOo , '' )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , ooOOoOO000 + 'settings.png' , o00O0oOOo , '' )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']Force Genie Update Kodi 16+[/COLOR]' , I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , ooOOoOO000 + 'GenieUpdate.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'My Build' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']WIZARD[/COLOR]' , str ( OooO ) , 4001 , ooOOoOO000 + 'Wizard.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Streams' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']STREAMS[/COLOR]' , str ( OooO ) , 4002 , ooOOoOO000 + 'Streams.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Music' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Music[/COLOR]' , str ( OooO ) , 4003 , ooOOoOO000 + 'Music.png' , o00O0oOOo , '' )
  if 2 - 2 : I11O0O0oOO00O00o + iI1ii11iIi1i - oOo0O0Ooo % I11i . Ii1IIIi1
 if o0OoO . getSetting ( 'Builders Toolbox' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']BUILDERS TOOLBOX[/COLOR]' , str ( OooO ) , 32 , ooOOoOO000 + 'BuildersToolbox.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Source List' ) == 'true' :
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']SOURCE LIST[/COLOR]' , str ( OooO ) , 46 , ooOOoOO000 + 'SoruceList.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Maintainance' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MAINTENANCE[/COLOR]' , str ( OooO ) , 3 , ooOOoOO000 + 'Maintenance.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Addons' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ADDONS[/COLOR]' , '' , 10050 , ooOOoOO000 + 'Addons.png' , o00O0oOOo , '' )
 if IiI1III1 ( ) == 'android' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']APK TOOL[/COLOR]' , str ( OooO ) , 30039 , ooOOoOO000 + 'APKTools.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Rss Feed' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']GenieTv RSS Feed[/COLOR]' , str ( OooO ) , 39 , ooOOoOO000 + 'GenieTVRSSFeed.png' , o00O0oOOo , '' )
  if 30 - 30 : ii
  if 5 - 5 : O0OOOoOoo0 - IIiIiII11i - ii % iI1ii11iIi1i + oOo0O0Ooo * iI11I1II1I1I
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def OoOO00OO0 ( ) :
 OoOoooOooOO0o = I1iooOOooO ( )
 O0O00o00O0 = OoOoooOooOO0o . replace ( o0O0oOOoo0O0 , "" )
 if os . path . exists ( OoOoooOooOO0o ) or not OoOoooOooOO0o == False :
  O00o0 = open ( OoOoooOooOO0o , mode = 'r' ) ; I1ii1i1 = O00o0 . read ( ) ; O00o0 . close ( )
  i11i1IiIi11 ( "%s - %s" % ( O0OO0o , O0O00o00O0 ) , I1ii1i1 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def I1iooOOooO ( ) :
 Oo0O = False
 if os . path . exists ( os . path . join ( o0O0oOOoo0O0 , 'xbmc.log' ) ) :
  Oo0O = os . path . join ( o0O0oOOoo0O0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( o0O0oOOoo0O0 , 'kodi.log' ) ) :
  Oo0O = os . path . join ( o0O0oOOoo0O0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( o0O0oOOoo0O0 , 'spmc.log' ) ) :
  Oo0O = os . path . join ( o0O0oOOoo0O0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( o0O0oOOoo0O0 , 'tvmc.log' ) ) :
  Oo0O = os . path . join ( o0O0oOOoo0O0 , 'tvmc.log' )
 return Oo0O
 if 98 - 98 : O00o0O00 + ooOOOoO + oO0oo0o % ii
def iI1IiiI ( url ) :
 if url == 'http://' : return False
 try :
  iIi1ii = urllib2 . Request ( url )
  iIi1ii . add_header ( 'User-Agent' , I11ii1i1I )
  I1I11 = urllib2 . urlopen ( iIi1ii )
  I1I11 . close ( )
 except Exception , III1i1iII1 :
  return III1i1iII1
 return True
 if 51 - 51 : ii * O00o0O00
def IiiiiI11iii11iI ( ) :
 I1iIIiI1i = II1I1i ( Ii11IiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( I1iIIiI1i )
 if len ( IIi11ii ) > 0 :
  for I111iIii1i1 , i11iii1II1I1 , I1i1I1i1I1 , i1I in IIi11ii :
   iII111I ( I111iIii1i1 , i11iii1II1I1 , 50005 , I1i1I1i1I1 , i1I , '' )
def OOOo0OO0ooO0O0O ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']BACKUP MY BUILD[/COLOR]' , str ( OooO ) , 10060 , ooOOoOO000 + 'BackupMyBuild.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']RESTORE MY BUILD[/COLOR]' , str ( OooO ) , 49 , ooOOoOO000 + 'RestoreMyBuild.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']WIPE GENIE[/COLOR]' , str ( OooO ) , 41 , ooOOoOO000 + 'WipeGenie.png' , o00O0oOOo , '' )
 if 22 - 22 : OOooOOo . O00o0O00 * OOooOOo
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Genie BUILDS[/COLOR]' , str ( OooO ) , 44 , ooOOoOO000 + 'GenieBuilds.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def oO00O ( ) :
 oOO0i1 ( )
 if o00oOO00 == '5knuckleshuffle' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']XVID[/COLOR]' , str ( OooO ) , 10100 , ooOOoOO000 + 'Jizbox.png' , o00O0oOOo , '' )
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ADULT CHANNELS[/COLOR]' , str ( OooO ) , 30033 , ooOOoOO000 + 'adu.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Favourites' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']FAVOURITES[/COLOR]' , str ( OooO ) , 10057 , ooOOoOO000 + 'Favourites.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Search' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH[/COLOR]' , str ( OooO ) , 9000 , ooOOoOO000 + 'Search.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']G-Tv Live List[/COLOR]' , '' , 4009 , ooOOoOO000 + 'GTV.png' , o00O0oOOo , '' )
 if 20 - 20 : I11i . IIiIiII11i % O00o0O00 * iI11I1II1I1I
 if o0OoO . getSetting ( 'TV GUIDE' ) == 'true' :
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']TV GUIDE[/COLOR]' , '' , 10063 , ooOOoOO000 + 'TvGuide.png' , o00O0oOOo , '' )
  if 98 - 98 : oOo0O0Ooo % iI1ii11iIi1i * ii
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']STREAM TEAM[/COLOR]' , str ( OooO ) , 4006 , ooOOoOO000 + 'StreamTeam.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MOVIES[/COLOR]' , str ( OooO ) , 4004 , ooOOoOO000 + 'Movies.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']TV SHOWS[/COLOR]' , str ( OooO ) , 4005 , ooOOoOO000 + 'TVShows.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Football' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']FOOTBALL[/COLOR]' , '' , 10002 , ooOOoOO000 + 'Football.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']KIDS[/COLOR]' , str ( OooO ) , 4007 , ooOOoOO000 + 'Kids.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']24/7 STREAMS[/COLOR]' , '' , 30030 , ooOOoOO000 + '247Streams.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NEWS[/COLOR]' , str ( OooO ) , 30032 , ooOOoOO000 + 'News.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']GenieTv TUTORIALS[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , ooOOoOO000 + 'GenieTVTutorials.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']HOBBIES[/COLOR]' , str ( OooO ) , 4008 , ooOOoOO000 + 'Hobbies.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'YOUTUBE' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH YOUTUBE[/COLOR]' , str ( OooO ) , 10064 , ooOOoOO000 + 'SeachYouTube.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'REQUESTS' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']REQUESTS[/COLOR]' , str ( OooO ) + ( I1Iii1III ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , ooOOoOO000 + 'Requests.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Stand Up' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']STAND UP[/COLOR]' , '' , 10003 , ooOOoOO000 + 'StandUp.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Documentaries' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']DOCUMENTARIES[/COLOR]' , str ( OooO ) , 8040 , ooOOoOO000 + 'documentaries.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Disclose' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']DISCLOSE TV[/COLOR]' , str ( OooO ) , 7001 , ooOOoOO000 + 'DiscloseTV.png' , o00O0oOOo , '' )
  if 51 - 51 : iI11I1II1I1I . OOooOOo / oO0oo0o + I11i
  if 33 - 33 : O0OOOoOoo0 . IIiIiII11i % Ii1IIIi1 + I11i
 if o0OoO . getSetting ( 'Playlist Loader' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']PLAYLIST LOADER[/COLOR]' , str ( OooO ) , 3000 , ooOOoOO000 + 'PlaylistLoader.png' , o00O0oOOo , '' )
  if 71 - 71 : I1ii11iIi11i % O00o0O00
  if 98 - 98 : I11O0O0oOO00O00o % Ii % O0OOOoOoo0 + iI1ii11iIi1i
  if 78 - 78 : Ii1I % oO0oo0o / Ii1IIIi1 - iI11I1II1I1I
  if 69 - 69 : ii1ii11IIIiiI
  if 11 - 11 : oOo0O0Ooo
  if 16 - 16 : iI1ii11iIi1i + ooOOOoO * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
  if 67 - 67 : ii / oOo0O0Ooo * iI1ii11iIi1i + I11O0O0oOO00O00o
  if 65 - 65 : ii - Ii1I / O0OOOoOoo0 / IIiIiII11i / ooOoO0O00
  if 71 - 71 : ii1ii11IIIiiI + iI1ii11iIi1i
  if 28 - 28 : O00o0O00
  if 38 - 38 : O0OOOoOoo0 % IIiIiII11i % I11O0O0oOO00O00o / oO0o + OOooOOo / ooOoO0O00
  if 54 - 54 : iI11I1II1I1I % Ii1I - O00o0O00 / oO0oo0o - oO0o . I11O0O0oOO00O00o
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 11 - 11 : Ii1I . oO0o * ooOOOoO * ii + O0OOOoOoo0
def o0O0 ( ) :
 if not os . path . exists ( OO00O0O00oOOO ) :
  i11i1IiIi11 ( 'Change Log 30/9/16 - v3.1.6' , 'Apk tool added download and instal over 100,000 apps direct to your box, new documentaries section added, Bollywood section added' )
  os . makedirs ( OO00O0O00oOOO )
  if 33 - 33 : o0o00Oo0O * I11i - ii1ii11IIIiiI % ii1ii11IIIiiI
  if 18 - 18 : ii1ii11IIIiiI / I1ii11iIi11i * ii1ii11IIIiiI + ii1ii11IIIiiI * Ii * Ii1I
def ooooooO0o00 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH MOVIES[/COLOR]' , str ( OooO ) , 9001 , ooOOoOO000 + 'Search.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Popcorn Box' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']POPCORN BOX[/COLOR]' , str ( OooO ) , 7061 , ooOOoOO000 + 'PopcornBox.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Desi Flix[/COLOR]' , '' , 80005 , ooOOoOO000 + 'Desi.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Film Trailers[/COLOR]' , I1Iii1III ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , ooOOoOO000 + 'FilmTrailers.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , ooOOoOO000 + 'ClassicMovies.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def Oo00o00O00 ( ) :
 oOO0i1 ( )
 OOOoOO ( )
 if 67 - 67 : oOo0O0Ooo . ooOoO0O00
 if 27 - 27 : O0OOOoOoo0 % oOo0O0Ooo
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Live Sport On G-Tv[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'TV GUIDE' ) == 'true' :
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']TV GUIDE[/COLOR]' , '' , 10063 , ooOOoOO000 + 'TvGuide.png' , o00O0oOOo , '' )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']Link GTV to Guide[/COLOR]' , '' , 4010 , ooOOoOO000 + 'linkchannels.png' , o00O0oOOo , '' )
def OooOoOoo0ooo0 ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Lists[/COLOR]' , I1Iii1III ( 'aHR0cDovL2Rvd25sb2FkLnByb2dkdmIuY29tL3R2c3QvU2x5TmV0LnR2c3Q=' ) , 9030 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Find Me A Stream[/COLOR]' , '' , 9003 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']World IPTV[/COLOR]' , '' , 9004 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']World IPTV 2[/COLOR]' , '' , 9007 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Iptv Lists[/COLOR]' , '' , 9010 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 if 32 - 32 : ii1ii11IIIiiI
 if 30 - 30 : iI11I1II1I1I / I11O0O0oOO00O00o . oO0o - I11i
def oO000oOo0oO0 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH SERIES[/COLOR]' , str ( OooO ) , 9002 , ooOOoOO000 + 'Search.png' , o00O0oOOo , '' )
 if 57 - 57 : I11i
 if 51 - 51 : oOo0O0Ooo . iI11I1II1I1I - Ii1I / o0o00Oo0O
 if o0OoO . getSetting ( 'Watch Series' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']WATCH SERIES[/COLOR]' , '' , 10040 , ooOOoOO000 + 'WatchSeries.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']iWATCH SERIES[/COLOR]' , '' , 8020 , ooOOoOO000 + 'iWatchSeries.png' , o00O0oOOo , '' )
 if 52 - 52 : I11i + o0o00Oo0O + Ii1IIIi1 + I1ii11iIi11i % Ii1IIIi1
 if 75 - 75 : oOo0O0Ooo . O0OOOoOoo0 . o0o00Oo0O * ii1ii11IIIiiI
 if o0OoO . getSetting ( 'CLASSIC TV' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CLASSIC TV[/COLOR]' , str ( OooO ) , 8064 , ooOOoOO000 + 'ClassicTV.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']TV Show Trailers[/COLOR]' , I1Iii1III ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , ooOOoOO000 + 'TVShowTrailers.png' , o00O0oOOo , '' )
 if 4 - 4 : iI1ii11iIi1i % oO0oo0o * oO0o
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def IIIiiii1 ( ) :
 oOO0i1 ( )
 if o0OoO . getSetting ( 'Silent Hunter' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SILENT HUNTER[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , ooOOoOO000 + 'SilentHunter.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'The Reaper' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']THE REAPER[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , ooOOoOO000 + 'TheReaper.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Pandoras Box' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']PANDORAS BOX[/COLOR]' , str ( OooO ) , 10025 , ooOOoOO000 + 'PandorasBox.png' , o00O0oOOo , '' )
  if 23 - 23 : Ii
  if 30 - 30 : I11i - ooOoO0O00 % IIiIiII11i + I11O0O0oOO00O00o * iI11I1II1I1I
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']DoJo STREAMS[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ooOOoOO000 + 'DojoStreams.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Scooby Streams' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SCOOBY STREAMS[/COLOR]' , str ( OooO ) , 1023 , ooOOoOO000 + 'ScoobyStreams.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'HeroVision' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']HEROVISION[/COLOR]' , '' , 1017 , ooOOoOO000 + 'Herovision.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ITV[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , ooOOoOO000 + 'ITVStreams.png' , o00O0oOOo , '' )
 if 81 - 81 : ooOOOoO % ooOoO0O00 . iI11I1II1I1I
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 4 - 4 : Ii % oO0o % ooOoO0O00 / ooOOOoO
def oOO0o0OO ( ) :
 oOO0i1 ( )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']SILENT HUNTER[/COLOR]' , ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , ooOOoOO000 + 'SilentHunter.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SERVER 1[/COLOR]' , ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , ooOOoOO000 + 'SilentHunter.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SERVER 2[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , ooOOoOO000 + 'SilentHunter.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SCRAPES[/COLOR]' , ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , ooOOoOO000 + 'SilentHunter.png' , o00O0oOOo , '' )
def oo0Oooo0O ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 url = url
 IIi11ii = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( ooO0Oo )
 for i11II , II1OoOOoOOOoooO0 in IIi11ii :
  if '[DIR]' in i11II :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + II1OoOOoOOOoooO0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + II1OoOOoOOOoooO0 , 1018 , ooOOoOO000 + 'SilentHunter.png' )
  if 'mkv' in II1OoOOoOOOoooO0 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + II1OoOOoOOOoooO0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + II1OoOOoOOOoooO0 , 222 , ooOOoOO000 + 'SilentHunter.png' )
  if 'avi' in II1OoOOoOOOoooO0 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + II1OoOOoOOOoooO0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + II1OoOOoOOOoooO0 , 222 , ooOOoOO000 + 'SilentHunter.png' )
   if 47 - 47 : I1ii11iIi11i * Ii1I + iI11I1II1I1I / ii1ii11IIIiiI / oO0o - ii
def O0oo0ooO ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']HEROVISION[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , ooOOoOO000 + 'Herovision.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']HEROVISION SCRAPES[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , ooOOoOO000 + 'Herovision.png' , o00O0oOOo , '' )
 if 73 - 73 : I11i * o0o00Oo0O - Ii
def ii1i1 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOOoOO000 + 'SearchCartoons.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'WCO' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( OooO ) , 21004 , ooOOoOO000 + 'watchcartoons.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Cartoons' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CARTOONS[/COLOR]' , '' , 10001 , ooOOoOO000 + 'Cartoons.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Anime' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']AnimeLand[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , ooOOoOO000 + 'anime.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def IIII1I11Ii11 ( ) :
 oOO0i1 ( )
 if o0OoO . getSetting ( 'Football' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']FOOTBALL[/COLOR]' , '' , 10002 , ooOOoOO000 + 'Football.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Fitness' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']FITNESS[/COLOR]' , ( I1Iii1III ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , ooOOoOO000 + 'Fitness.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'Go Fishing' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Go Fishing[/COLOR]' , str ( OooO ) , 8090 , ooOOoOO000 + 'GoFishing.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']GenieTv Kitchen[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , ooOOoOO000 + 'GenieTVKitchen.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 98 - 98 : Ii1IIIi1
 if 68 - 68 : iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
 if 38 - 38 : O0OOOoOoo0 - O00o0O00 / Ii1IIIi1
def Oooo ( ) :
 o0000o0OOOo = II1I1i ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi11ii = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( o0000o0OOOo )
 for i1iIi1IiI in IIi11ii :
  i1iIi1IiI = ( str ( i1iIi1IiI ) )
  if os . path . exists ( xbmc . translatePath ( i1iIi1IiI ) ) :
   ooooO0O = ( i1iIi1IiI ) . replace ( 'special://home/addons/' , '' )
   i11i1IiIi11 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + ooooO0O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iiiiOo000O00o0O = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iiiiOo000O00o0O == 0 :
    o0o0oo0oO ( i1iIi1IiI )
    Ii1iii1 ( )
   elif iiiiOo000O00o0O == 1 :
    OO0oooOo ( i1iIi1IiI )
  else :
   pass
   if 84 - 84 : O0OOOoOoo0 % iI1ii11iIi1i + Ii
def OO0oooOo ( addon ) :
 ooooO0O = ( addon ) . replace ( 'special://home/addons/' , '' )
 iII1I1iIi1i . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 iII1I1iIi1i . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 iII1I1iIi1i . close ( )
 if 28 - 28 : I1ii11iIi11i + oO0o * O00o0O00 % oO0oo0o . I11O0O0oOO00O00o % o0o00Oo0O
def o0o0oo0oO ( addon ) :
 ooOOoOoOoO00 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OoO0o00o = os . path . join ( i1i , 'default.py' )
 I1111iI = open ( OoO0o00o , "w+" )
 if 30 - 30 : ii1ii11IIIiiI . O0OOOoOoo0 * Ii1I
 I1111iI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1111iI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1111iI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 17 - 17 : oOo0O0Ooo . o0o00Oo0O + oO0o
 if 43 - 43 : IIiIiII11i . oO0oo0o / Ii1I
 if 20 - 20 : oOo0O0Ooo
 if 95 - 95 : Ii1IIIi1 - oOo0O0Ooo
def O000o0O0 ( ) :
 i11i1i1i ( 'Search' , '' , 80008 , ooOOoOO000 + 'Search.png' )
 o0000o0OOOo = II1I1i ( 'http://www.join4films.com/' )
 IIi11ii = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 80006 , ooOOoOO000 + 'Desi.png' )
def O0000oOoO0o0 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( o0000o0OOOo )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( o0000o0OOOo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  OoO00O ( I111iIii1i1 , url , 80007 , IiiIiII1Ii1 )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( 'Next' , url , 80006 , ooOOoOO000 + 'Next.png' )
def o000o0O ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( 'file: "([^"]*)"' ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  url = ( url ) . replace ( ' ' , '%20' )
  IIIIi1I ( url )
def I1III ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0OOo = 'http://www.join4films.com/?s=' + ( ii1I1IIi ) . replace ( ' ' , '+' ) + '&search_type=1'
 OooOooO0OoOoo0o = o00oOO0OOo . lower ( )
 O0000oOoO0o0 ( OooOooO0OoOoo0o )
 if 46 - 46 : OOooOOo + oO0o
 if 70 - 70 : Ii1IIIi1 / iI11I1II1I1I
 if 85 - 85 : ii % ooOoO0O00 * ii / Ii1I
 if 96 - 96 : ii + oO0oo0o
 if 44 - 44 : oO0oo0o
 if 20 - 20 : I11O0O0oOO00O00o + iI1ii11iIi1i / o0o00Oo0O % iI11I1II1I1I
 if 88 - 88 : OOooOOo / IIiIiII11i
 if 87 - 87 : Ii1I - Ii1I - Ii1IIIi1 + oO0oo0o
 if 82 - 82 : oO0oo0o / iI11I1II1I1I . oOo0O0Ooo . O00o0O00 / I11i
 if 42 - 42 : I1ii11iIi11i
 if 19 - 19 : oO0oo0o % Ii1I * iI11I1II1I1I + oOo0O0Ooo
 if 46 - 46 : I1ii11iIi11i
 if 1 - 1 : Ii1IIIi1
 if 97 - 97 : O00o0O00 + Ii1IIIi1 + o0o00Oo0O + Ii
 if 77 - 77 : I11i / ii
 if 46 - 46 : I11i % iI11I1II1I1I . Ii1IIIi1 % Ii1IIIi1 + Ii
 if 72 - 72 : iI11I1II1I1I * iI1ii11iIi1i % O0OOOoOoo0 / oO0o
def iII1iIIIIII ( ) :
 Ooooo0Oo0oOo ( 'Genre' , I1Iii1III ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Most Viewed' , I1Iii1III ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Box Office' , I1Iii1III ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Search' , '' , 10078 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
 if 72 - 72 : iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
def IIIIII11iIiI1III ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0OOo = 'http://imoviemax.se/?s=' + ( ii1I1IIi ) . replace ( ' ' , '+' )
 OooOooO0OoOoo0o = o00oOO0OOo . lower ( )
 o0Ooo0 ( OooOooO0OoOoo0o )
def I1ii11iiIIi ( url ) :
 ooOoO0o0OoOo = [ ]
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiII11iI in IIi11ii :
  if I111iIii1i1 in ooOoO0o0OoOo :
   pass
  else :
   Ooooo0Oo0oOo ( I111iIii1i1 + ' - ' + IiII11iI + ' Films' , url , 10074 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
   ooOoO0o0OoOo . append ( I111iIii1i1 )
   if 34 - 34 : OOooOOo - O00o0O00 + o0o00Oo0O . iI1ii11iIi1i
def o00o000 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IIIi1IiI1iII in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 + ' - Views:' + IIIi1IiI1iII , url , 10075 , ooOOoOO000 + 'genievision.png' , o00O0oOOo , '' )
  if 68 - 68 : O00o0O00
  if 82 - 82 : iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % ooOOOoO / iI1ii11iIi1i . iI1ii11iIi1i
def o0Ooo0 ( url ) :
 OOOO0oo = [ ]
 o0000o0OOOo = II1I1i ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( o0000o0OOOo )
 for next in next :
  Ooooo0Oo0oOo ( 'NEXT PAGE' , next , 10074 , ooOOoOO000 + 'Next.png' , o00O0oOOo , '' )
 IIi11ii = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , I111iIii1i1 , url in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 10075 , IiiIiII1Ii1 , IiiIiII1Ii1 , '' )
  OOOO0oo . append ( I111iIii1i1 )
  if 66 - 66 : oO0oo0o % oO0o . O00o0O00
def iii1I1ii1 ( img , name , url ) :
 img = img
 name = name
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( o0000o0OOOo )
 for IIiII11Iiii1i1II , url in IIi11ii :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  ii1iIii = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + ii1iIii
  OoOOOO0 = ( IIiII11Iiii1i1II ) . replace ( 'play-' , 'Server ' )
  iII111I ( OoOOOO0 , ii1iIii , 10076 , img , img , '' )
  if 4 - 4 : iI1ii11iIi1i
def Iii1iii11 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( o0000o0OOOo )
 for II1OoOOoOOOoooO0 in IIi11ii :
  if '=m' in II1OoOOoOOOoooO0 :
   Ii11 ( II1OoOOoOOOoooO0 )
  elif 'php' in II1OoOOoOOOoooO0 :
   Iii1iii11 ( url )
  else :
   o0000o0OOOo = II1I1i ( II1OoOOoOOOoooO0 )
   IIi11ii = re . compile ( 'content="([^"]*)">' ) . findall ( o0000o0OOOo )
   for II11i1 in IIi11ii :
    Ii11 ( II1OoOOoOOOoooO0 )
    if 71 - 71 : O0OOOoOoo0
    if 53 - 53 : ii % iI1ii11iIi1i . ooOOOoO / Ii % Ii1IIIi1
    if 28 - 28 : I11O0O0oOO00O00o
def IIIi1IIiI ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IiIi1I1i = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IIiiI , IiiI1II in IiIi1I1i :
  print 'there ><><><><><><><><><><><><'
  IIiiI = IIiiI
  IIi11ii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiiI1II ) )
  for I111iIii1i1 , i11i1IIi in IIi11ii :
   print 'here <><><><><><><><><><><><>'
   Ooooo0Oo0oOo ( '[COLORred]' + IIiiI + '[/COLOR] - ' + I111iIii1i1 + ' - [COLOR' + iiiI1iiI11iii + ']' + i11i1IIi + '[/COLOR]' , I1Iii1III ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOOoOO000 + 'loader.png' , o00O0oOOo , '' )
 Oo0oiiiii11i = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IIiiI , OOoOOo0o0OOo0 in Oo0oiiiii11i :
  print 'there ><><><><><><><><><><><><'
  IIiiI = IIiiI
  IIi11ii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOoOOo0o0OOo0 ) )
  for I111iIii1i1 , i11i1IIi in IIi11ii :
   print 'here <><><><><><><><><><><><>'
   Ooooo0Oo0oOo ( '[COLORred]' + IIiiI + '[/COLOR] - ' + I111iIii1i1 + ' - [COLOR' + iiiI1iiI11iii + ']' + i11i1IIi + '[/COLOR]' , I1Iii1III ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , ooOOoOO000 + 'loader.png' , o00O0oOOo , '' )
   if 50 - 50 : O0OOOoOoo0
   if 72 - 72 : ii1ii11IIIiiI
   if 90 - 90 : I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . Ii1IIIi1
def iiiI11I ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Oo0oiiiii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for Oo0oiiiii11i in Oo0oiiiii11i :
  I111iIii1i1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
  for I111iIii1i1 in I111iIii1i1 :
   I111iIii1i1 = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0oiiiii11i ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  OOoi1I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
  for OOoi1I1I in OOoi1I1I :
   OOoi1I1I = 'http:' + OOoi1I1I
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , '' , '' )
  if 16 - 16 : OOooOOo
  if 41 - 41 : ooOoO0O00 * IIiIiII11i / ii . O00o0O00
  if 83 - 83 : Ii1IIIi1 . o0o00Oo0O / I1ii11iIi11i / O00o0O00 - IIiIiII11i
  if 100 - 100 : oO0o
def iIiiiIII1II ( url ) :
 if 2 - 2 : iI11I1II1I1I * I1ii11iIi11i % oO0oo0o - IIiIiII11i - Ii1IIIi1
 oO00oOOOO = [ ]
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for II1OoOOoOOOoooO0 , IiiIiII1Ii1 , I111iIii1i1 , o0o0OOO0ooo00 in IIi11ii :
  I111iIii1i1 = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iiiiiI1iii11 = II1I1i ( II1OoOOoOOOoooO0 )
  OOOO0oO0OOo0o = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiiiiI1iii11 )
  for I11III111i1I , O0ooOO0O00 in OOOO0oO0OOo0o :
   OOO0O = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( O0ooOO0O00 ) )
   for iIi11OoO0OOOo0Oo in OOO0O :
    if I111iIii1i1 in oO00oOOOO :
     pass
    else :
     iII111I ( I111iIii1i1 , I11III111i1I , 8043 , IiiIiII1Ii1 , IiiIiII1Ii1 , iIi11OoO0OOOo0Oo )
     iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
     oO00oOOOO . append ( I111iIii1i1 )
     if 85 - 85 : Ii1IIIi1 + ii * Ii1IIIi1 - ii1ii11IIIiiI % Ii
     if 71 - 71 : Ii1I - O0OOOoOoo0 / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def Oooo0OOo0O0o ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , O0O00OOOo00O , iIi11OoO0OOOo0Oo , i1I , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 10065 , O0O00OOOo00O , i1I , iIi11OoO0OOOo0Oo )
 iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
 if 93 - 93 : Ii1I / oOo0O0Ooo / iI11I1II1I1I % ii1ii11IIIiiI % ii1ii11IIIiiI
def I1iOO000o0o0oo ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0OOo = 'https://www.youtube.com/results?search_query=' + ( ii1I1IIi ) . replace ( ' ' , '+' )
 OooOooO0OoOoo0o = o00oOO0OOo . lower ( )
 o0000o0OOOo = II1I1i ( OooOooO0OoOoo0o )
 IIi11ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 in next :
  i11iii1II1I1 = 'https://www.youtube.com' + i11iii1II1I1
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + '] NEXT [/COLOR]' , i11iii1II1I1 , 10065 , ooOOoOO000 + 'Next.png' , o00O0oOOo , '' )
 for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 , oO00oOoo0ooO0 , O0ooOO0O00 in IIi11ii :
  oo00O0oOo . append ( I111iIii1i1 )
  iiiiII1i1Iii1I1 ( 'tvshows' , 'INFO' )
  OOoi1I1I = 'http:' + ( IiiIiII1Ii1 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OOoi1I1I
  i11iii1II1I1 = 'http://www.youtube.com' + i11iii1II1I1
  iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , OOoi1I1I , O0ooOO0O00 )
 else :
  IIi11ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
  for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 , oO00oOoo0ooO0 in IIi11ii :
   print 'im doing it'
   iiiiII1i1Iii1I1 ( 'tvshows' , 'INFO' )
   OOoi1I1I = 'http:' + ( IiiIiII1Ii1 ) . replace ( 'https:' , '' )
   i11iii1II1I1 = 'http://www.youtube.com' + i11iii1II1I1
   if '&' in i11iii1II1I1 :
    print ' i got here'
    o0000o0OOOo = II1I1i ( i11iii1II1I1 )
    Oo0oiiiii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o0000o0OOOo )
    for Oo0oiiiii11i in Oo0oiiiii11i :
     I111iIii1i1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
     for I111iIii1i1 in I111iIii1i1 :
      I111iIii1i1 = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     i11iii1II1I1 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0oiiiii11i ) )
     for i11iii1II1I1 in i11iii1II1I1 :
      i11iii1II1I1 = 'https://www.youtube.com/w' + i11iii1II1I1
     OOoi1I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
     for OOoi1I1I in OOoi1I1I :
      OOoi1I1I = 'http:' + OOoi1I1I
     iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , o00O0oOOo , '' )
   elif I111iIii1i1 in oo00O0oOo :
    pass
   elif 'user' in i11iii1II1I1 or 'elete' in I111iIii1i1 :
    pass
   elif 'hannel' in i11iii1II1I1 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + i11iii1II1I1
    o0000o0OOOo = II1I1i ( i11iii1II1I1 )
    Ooo0o0ooO0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
    for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 in Ooo0o0ooO0 :
     if 'outube' in i11iii1II1I1 or 'list' in i11iii1II1I1 :
      pass
     elif 'atch' in i11iii1II1I1 :
      i11iii1II1I1 = ( i11iii1II1I1 ) . replace ( '/watch?v=' , '' )
      iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiiIiII1Ii1 , 'http:' + IiiIiII1Ii1 , '' )
     else :
      pass
   else :
    iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , OOoi1I1I , '' )
    if 30 - 30 : o0o00Oo0O * ii
def oO0o0O ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( o0000o0OOOo )
 for url in next :
  url = 'https://www.youtube.com' + url
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + '] NEXT [/COLOR]' , url , 10065 , ooOOoOO000 + 'Next.png' , o00O0oOOo , '' )
 for IiiIiII1Ii1 , url , I111iIii1i1 , oO00oOoo0ooO0 , O0ooOO0O00 in IIi11ii :
  oo00O0oOo . append ( I111iIii1i1 )
  iiiiII1i1Iii1I1 ( 'tvshows' , 'INFO' )
  OOoi1I1I = 'http:' + ( IiiIiII1Ii1 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OOoi1I1I
  url = 'http://www.youtube.com' + url
  iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , OOoi1I1I , O0ooOO0O00 )
 else :
  IIi11ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
  for IiiIiII1Ii1 , url , I111iIii1i1 , oO00oOoo0ooO0 in IIi11ii :
   iiiiII1i1Iii1I1 ( 'tvshows' , 'INFO' )
   OOoi1I1I = 'http:' + ( IiiIiII1Ii1 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    o0000o0OOOo = II1I1i ( url )
    Oo0oiiiii11i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( o0000o0OOOo )
    for Oo0oiiiii11i in Oo0oiiiii11i :
     I111iIii1i1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
     for I111iIii1i1 in I111iIii1i1 :
      I111iIii1i1 = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Oo0oiiiii11i ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     OOoi1I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( Oo0oiiiii11i ) )
     for OOoi1I1I in OOoi1I1I :
      OOoi1I1I = 'http:' + OOoi1I1I
     iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , o00O0oOOo , '' )
   elif I111iIii1i1 in oo00O0oOo :
    pass
   elif 'user' in url or 'elete' in I111iIii1i1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    o0000o0OOOo = II1I1i ( url )
    Ooo0o0ooO0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
    for IiiIiII1Ii1 , url , I111iIii1i1 in Ooo0o0ooO0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiiIiII1Ii1 , 'http:' + IiiIiII1Ii1 , '' )
     else :
      pass
   else :
    iII111I ( '[COLORred]' + oO00oOoo0ooO0 + '[/COLOR]' + '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I , OOoi1I1I , '' )
    if 17 - 17 : iI11I1II1I1I . ii / I11O0O0oOO00O00o % IIiIiII11i % ooOoO0O00 / Ii
    if 58 - 58 : I1ii11iIi11i . IIiIiII11i + oO0oo0o - Ii / IIiIiII11i / o0o00Oo0O
def OOOoOO ( ) :
 if IiI11i1IiI1 == 'insert_password' :
  ooOOoOoOoO00 . ok ( '[COLOR' + iiiI1iiI11iii + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + iiiI1iiI11iii + ']http://GenieTv.co.uk[/COLOR]' )
  o0OoO . openSettings ( sys . argv [ 0 ] )
 else :
  OoO0 = open ( OOOO0o0Oo0 )
  IIi11ii = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OoO0 ) )
  for O00OO0OoO00oO , iiiI1iiIiII1 in IIi11ii :
   if O00OO0OoO00oO == 'needs replacing' or iiiI1iiIiII1 == 'needs replacing' :
    oOo0oOOoo0O ( )
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']G-Tv PRIVATE LIST[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , ooOOoOO000 + 'PrivateList.png' , o00O0oOOo , '' )
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']G-Tv ULTIMATE[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
  if 51 - 51 : O00o0O00 % iI11I1II1I1I - ii % O0OOOoOoo0 * iI11I1II1I1I % oO0o
def iI1IiI11Ii11i ( ) :
 ooOOoOoOoO00 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + IiI1Ii + ")" )
 oOo0oOOoo0O ( )
 ooOOoOoOoO00 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 79 - 79 : oO0o - iI11I1II1I1I + iI1ii11iIi1i - ii1ii11IIIiiI
def O0oi1IiI1I ( ) :
 Ooooo0Oo0oOo ( 'Full List' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'PPV' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Entertainment' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Factual' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Movie Channels' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'US Movie Channels TEST' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Kids' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Music' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'UK Sports' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'International Sports' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'News UK & International' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'German' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'Arabic' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'TV Series Latest' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'VOD Latest' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( 'VOD Bollywood' , '' , 60003 , ooOOoOO000 + 'UltimateList.png' , o00O0oOOo , '' )
 if 61 - 61 : ooOOOoO . ooOoO0O00 / ii1ii11IIIiiI % Ii * Ii1IIIi1
def O00OOoOo0 ( name ) :
 O0ooO0oOO = name
 o0000o0OOOo = II1I1i ( 'http://piesustv.net:8000/get.php?username=' + OO00OOo + '&password=' + IiI11i1IiI1 + '&type=m3u_plus&output=mpegts' )
 IIi11ii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( o0000o0OOOo )
 for name , IiiIiII1Ii1 , ii111I1iII1i1 , i11iii1II1I1 in IIi11ii :
  if O0ooO0oOO == 'Full List' :
   i11iii1II1I1 = ( i11iii1II1I1 ) . replace ( '.ts' , '.m3u8' )
   iII111I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i11iii1II1I1 ) . strip ( ) , 10012 , IiiIiII1Ii1 , IiiIiII1Ii1 , '' )
  else :
   O0ooO0oOO = ( O0ooO0oOO ) . replace ( 'World' , 'القنوات العربية' )
   if O0ooO0oOO in ii111I1iII1i1 :
    i11iii1II1I1 = ( i11iii1II1I1 ) . replace ( '.ts' , '.m3u8' )
    print i11iii1II1I1 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    iII111I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i11iii1II1I1 ) . strip ( ) , 10012 , IiiIiII1Ii1 , IiiIiII1Ii1 , '' )
   else :
    pass
    if 20 - 20 : ooOoO0O00 * ii1ii11IIIiiI + IIiIiII11i % I11i % oO0oo0o
def O000000oooOOo ( name ) :
 O0ooO0oOO = name
 o0000o0OOOo = II1I1i ( 'http://piesustv.net:8000/get.php?username=' + OO00OOo + '&password=' + IiI11i1IiI1 + '&type=m3u_plus&output=mpegts' )
 IIi11ii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( o0000o0OOOo )
 for name , IiiIiII1Ii1 , i11iii1II1I1 in IIi11ii :
  i11iii1II1I1 = ( i11iii1II1I1 ) . replace ( '.ts' , '.m3u8' )
  iII111I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( i11iii1II1I1 ) . strip ( ) , 10012 , IiiIiII1Ii1 , IiiIiII1Ii1 , '' )
 else :
  iII111I ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 17 - 17 : O00o0O00 % I1ii11iIi11i / Ii1I . ooOOOoO * O00o0O00 - IIiIiII11i
  if 41 - 41 : iI1ii11iIi1i
  if 77 - 77 : ii1ii11IIIiiI
  if 65 - 65 : IIiIiII11i . oOo0O0Ooo % oO0oo0o * oO0o
  if 38 - 38 : OOooOOo / Ii1IIIi1 % I1ii11iIi11i
  if 11 - 11 : Ii1IIIi1 - oO0oo0o + IIiIiII11i - iI11I1II1I1I
  if 7 - 7 : ooOOOoO - I11O0O0oOO00O00o / IIiIiII11i * iI1ii11iIi1i . Ii1IIIi1 * Ii1IIIi1
  if 61 - 61 : I11O0O0oOO00O00o % O0OOOoOoo0 - oO0o / I1ii11iIi11i
  if 4 - 4 : ii - ooOoO0O00 % iI1ii11iIi1i - O00o0O00 * I11i
  if 85 - 85 : ii * iI11I1II1I1I . Ii1IIIi1 / ii % oOo0O0Ooo % o0o00Oo0O
  if 36 - 36 : iI1ii11iIi1i / IIiIiII11i / ooOOOoO / ooOOOoO + Ii1I
  if 95 - 95 : ooOOOoO
def I11iiI1 ( ) :
 Ooooo0Oo0oOo ( 'Full Backup' , '' , 10061 , ooOOoOO000 + 'FullBackUp.png' , o00O0oOOo , 'Back Up Your Full System' )
 if os . path . exists ( oOO00 ) :
  Ooooo0Oo0oOo ( 'Backup Genie Favourites' , i11iii1II1I1 , 10062 , ooOOoOO000 + 'BackupGenieFavourites.png' , o00O0oOOo , 'Back Up Your favourites' )
 if os . path . exists ( O0oOoOooo00oo ) :
  Ooooo0Oo0oOo ( 'Backup Ivue Config' , O0oOoOooo00oo , 10062 , ooOOoOO000 + 'BackUpIvueConfig.png' , o00O0oOOo , 'Back Up Your master.db' )
 if os . path . exists ( OOO0OO00 ) :
  Ooooo0Oo0oOo ( 'Backup Kodi Favourites' , OOO0OO00 , 10062 , ooOOoOO000 + 'BackKodiFavourites.png' , o00O0oOOo , 'Back Up Your favourites.xml' )
  if 41 - 41 : OOooOOo * I11O0O0oOO00O00o / OOooOOo % oO0oo0o
  if 18 - 18 : IIiIiII11i . ii % OOooOOo % iI1ii11iIi1i
  if 9 - 9 : oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
zip = o0OoO . getSetting ( 'zip' )
I1Ioo000oooooooO = xbmc . translatePath ( os . path . join ( zip ) )
def II1IIi1ii111 ( ) :
 II1OO = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  ooOOoOoOoO00 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0OoO . openSettings ( sys . argv [ 0 ] )
  if 37 - 37 : ooOOOoO . I11i / O0OOOoOoo0 . O00o0O00
  if 66 - 66 : O00o0O00
  if 42 - 42 : OOooOOo - O00o0O00 . oO0oo0o
def oo0OOO0O0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOO00
  elif 'Ivue' in name :
   url = O0oOoOooo00oo
  elif 'Kodi' in name :
   url = OOO0OO00
  II1IIi1ii111 ( )
  OoooOooo = open ( url ) . read ( )
  IiIi1iiII = os . path . join ( I1Ioo000oooooooO , description . split ( 'Your ' ) [ 1 ] )
  O00o0 = open ( IiIi1iiII , mode = 'w' )
  O00o0 . write ( OoooOooo )
  O00o0 . close ( )
 else :
  if 'guisettings.xml' in description :
   ooO0o0o = open ( os . path . join ( I1Ioo000oooooooO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Ii1IiIi1IiI = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi11ii = re . compile ( Ii1IiIi1IiI ) . findall ( ooO0o0o )
   for type , ooOOOooOooOOoO0O , i1I111ii11Iii in IIi11ii :
    i1I111ii11Iii = i1I111ii11Iii . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , ooOOOooOooOOoO0O , i1I111ii11Iii ) )
  else :
   IiIi1iiII = os . path . join ( url )
   OoooOooo = open ( os . path . join ( I1Ioo000oooooooO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O00o0 = open ( IiIi1iiII , mode = 'w' )
   O00o0 . write ( OoooOooo )
   O00o0 . close ( )
 ooOOoOoOoO00 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 14 - 14 : oO0o . IIiIiII11i . I11O0O0oOO00O00o / iI1ii11iIi1i % Ii1I - O0OOOoOoo0
 if 67 - 67 : I11O0O0oOO00O00o - O00o0O00 . ooOoO0O00
 if 35 - 35 : Ii1IIIi1 + O0OOOoOoo0 - oO0oo0o . Ii1IIIi1 . ooOOOoO
 if 87 - 87 : OOooOOo
def i11i11iiIiIiI ( ) :
 o00Oo00OoO = 1
 II1IIi1ii111 ( )
 iIi1IiI11 = xbmc . translatePath ( os . path . join ( I1Ioo000oooooooO , 'Build Backup' , 'Full Backup' , '' ) )
 I11Iii = xbmc . translatePath ( os . path . join ( I1Ioo000oooooooO , 'Build Backup' , 'my_full_backup.zip' ) )
 oO0o0OO0oOOOO = xbmc . translatePath ( os . path . join ( I1Ioo000oooooooO , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIi1IiI11 ) :
  os . makedirs ( iIi1IiI11 )
 I1iI11IiIi1II = ooOOoOoOoO00 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1iI11IiIi1II ) : return False , 0
 OooooO0000 = I1iI11IiIi1II
 o0ooooOOo = xbmc . translatePath ( os . path . join ( iIi1IiI11 , OooooO0000 + '.zip' ) )
 oo0i1ii = [ 'plugin.video.GenieTv' ]
 I1ii1ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iIiIiiiII11i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1oO0oO00OO00 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OO0o00 = "Creating full backup of existing build"
 OOooo000 = "Creating Community Build"
 Ooo0 = "Archiving..."
 o0oOoO00oo0oOo = ""
 iiOO00O = "Please Wait"
 iiO0OoO0OOO00 ( Oo0oo0OoO0o0 , o0ooooOOo , OOooo000 , Ooo0 , o0oOoO00oo0oOo , iiOO00O , iIiIiiiII11i , I1oO0oO00OO00 )
 time . sleep ( 1 )
 IIIiii1I = xbmc . translatePath ( os . path . join ( iIi1IiI11 , OooooO0000 + '_guisettings.zip' ) )
 ii1iiii11IiI1 = zipfile . ZipFile ( IIIiii1I , mode = 'w' )
 try :
  ii1iiii11IiI1 . write ( xbmc . translatePath ( os . path . join ( Oo0oo0OoO0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 ii1iiii11IiI1 . close ( )
 if o00Oo00OoO == 0 :
  ooOOoOoOoO00 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  ooOOoOoOoO00 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  ooOOoOoOoO00 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I11Iii , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + o0ooooOOo + '[/COLOR]' )
  if 96 - 96 : ii1ii11IIIiiI / I1ii11iIi11i * IIiIiII11i - Ii1IIIi1 * I1ii11iIi11i
def iiO0OoO0OOO00 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 O0OoO0ooOoo = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIIi1i1i11IIi = len ( sourcefile )
 oOOO0o00 = [ ]
 O00ooi1i1iIiiI1Ii1 = [ ]
 iII1I1iIi1i . create ( message_header , message1 , message2 , message3 )
 for iIIIi11iI1I1I11II , oo0O00O0oO , IIIIi1iII in os . walk ( sourcefile ) :
  for file in IIIIi1iII :
   O00ooi1i1iIiiI1Ii1 . append ( file )
 ii1oO0Oo = len ( O00ooi1i1iIiiI1Ii1 )
 for iIIIi11iI1I1I11II , oo0O00O0oO , IIIIi1iII in os . walk ( sourcefile ) :
  oo0O00O0oO [ : ] = [ iIi1IIIi1Ii for iIi1IIIi1Ii in oo0O00O0oO if iIi1IIIi1Ii not in exclude_dirs ]
  IIIIi1iII [ : ] = [ O00o0 for O00o0 in IIIIi1iII if O00o0 not in exclude_files ]
  for file in IIIIi1iII :
   oOOO0o00 . append ( file )
   Ii1IiIIIi1i = len ( oOOO0o00 ) / float ( ii1oO0Oo ) * 100
   iII1I1iIi1i . update ( int ( Ii1IiIIIi1i ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   II111Ii1I1I = os . path . join ( iIIIi11iI1I1I11II , file )
   if not 'temp' in oo0O00O0oO :
    if not 'plugin.program.originwizard' in oo0O00O0oO :
     import time
     o00oo0oOo0o0 = '01/01/1980'
     i1Ii1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( II111Ii1I1I ) ) )
     if i1Ii1 > o00oo0oOo0o0 :
      O0OoO0ooOoo . write ( II111Ii1I1I , II111Ii1I1I [ iIIi1i1i11IIi : ] )
 O0OoO0ooOoo . close ( )
 iII1I1iIi1i . close ( )
 if 78 - 78 : iI1ii11iIi1i / IIiIiII11i % OOooOOo
 if 52 - 52 : O00o0O00 - Ii1IIIi1 * oO0oo0o
def i1I1ii1iI1 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SCOOBY STREAMS[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , ooOOoOO000 + 'scoob.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SCOOBY SCRAPES[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , ooOOoOO000 + 'scoob.png' , o00O0oOOo , '' )
 if 36 - 36 : o0o00Oo0O + I1ii11iIi11i
 if 5 - 5 : I1ii11iIi11i * OOooOOo
def OoI1Ii ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH MOVIES[/COLOR]' , str ( OooO ) , 9001 , ooOOoOO000 + 'MOVIESv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH SERIES[/COLOR]' , str ( OooO ) , 9002 , ooOOoOO000 + 'TVSHOWSv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , ooOOoOO000 + 'ORIGINCARTOON' , o00O0oOOo , '' )
 if 52 - 52 : I11i * ooOOOoO + OOooOOo
 if 49 - 49 : iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 - ii
 if 37 - 37 : ooOoO0O00 . I11O0O0oOO00O00o % OOooOOo + ii / Ii1IIIi1
 if 3 - 3 : Ii1I
def IIIII1iII1 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']RaysRavers[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , ooOOoOO000 + 'Rays-Ravers.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']QuickSilver[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , ooOOoOO000 + 'Quicksilver.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']RadioNomy[/COLOR]' , '' , 70001 , ooOOoOO000 + 'RadioNomy.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MUSIC CHANNELS[/COLOR]' , str ( OooO ) , 30031 , ooOOoOO000 + 'MusicChannels.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']UK RADIO[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , ooOOoOO000 + 'UKRadio.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']WORLD RADIO[/COLOR]' , str ( OooO ) , 1013 , ooOOoOO000 + 'WorldRadio.png' , o00O0oOOo , '' )
 if o0OoO . getSetting ( 'CONCERTS' ) == 'true' :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CONCERTS[/COLOR]' , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , ooOOoOO000 + 'Concerts.png' , o00O0oOOo , '' )
  if 2 - 2 : IIiIiII11i - oO0o . ooOOOoO * Ii1IIIi1 / oO0oo0o
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MUSIC VIDEOS[/COLOR]' , ( I1Iii1III ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , ooOOoOO000 + 'MusicVideos.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MUSIC[/COLOR]' , str ( OooO ) + ( I1Iii1III ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , ooOOoOO000 + 'Music.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MUSIC SEARCH[/COLOR]' , str ( OooO ) , 1111 , ooOOoOO000 + 'MusicSearch.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , ooOOoOO000 + 'KodibleAudioBooks.png' , o00O0oOOo , '' )
 if 80 - 80 : O00o0O00 / I11O0O0oOO00O00o / OOooOOo + ooOoO0O00 - I1ii11iIi11i
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 11 - 11 : I11i * oO0o
def OO0oOoO0O0 ( ) :
 oOO0i1 ( )
 if 14 - 14 : ooOOOoO % oO0oo0o % I1ii11iIi11i - Ii
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']KILL KODI[/COLOR]' , '' , 80000 , ooOOoOO000 + 'KillKodi.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SPEEDTEST[/COLOR]' , '' , 50004 , ooOOoOO000 + 'Speedtest.png' , o00O0oOOo , '' )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , ooOOoOO000 + 'View-Log-File.png' , o00O0oOOo , '' )
 iII111I ( 'DELETE CACHE' , 'url' , 14 , ooOOoOO000 + 'DeleteCache.png' , o00O0oOOo , '' )
 iII111I ( 'DELETE PACKAGES' , 'url' , 6 , ooOOoOO000 + 'DeletePackages.png' , o00O0oOOo , '' )
 iII111I ( 'FORCE REFRESH' , 'url' , 10 , ooOOoOO000 + 'ForceRefresh.png' , o00O0oOOo , 'Force Refresh All Repos' )
 if 53 - 53 : iI1ii11iIi1i % I1ii11iIi11i
 iII111I ( 'CHECK MY IP' , 'url' , 12 , ooOOoOO000 + 'CheckMyIP.png' , o00O0oOOo , '' )
 iII111I ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , ooOOoOO000 + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , o00O0oOOo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ADVANCED SETTINGS XML[/COLOR]' , str ( OooO ) , 4 , ooOOoOO000 + 'AdvancedSettingXML.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']URL FIXES[/COLOR]' , str ( OooO ) , 20 , ooOOoOO000 + 'URLFixes.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 59 - 59 : O00o0O00 % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * ooOOOoO
 if 41 - 41 : iI1ii11iIi1i % Ii1I
def ooooO0 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']REPOS[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , ooOOoOO000 + 'repos.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NEW[/COLOR]' , str ( OooO ) , 22 , ooOOoOO000 + 'NEW.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']IPTV[/COLOR]' , str ( OooO ) , 23 , ooOOoOO000 + 'IPTV.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']VIDEO[/COLOR]' , str ( OooO ) , 24 , ooOOoOO000 + 'VIDEO.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SPORTS[/COLOR]' , str ( OooO ) , 25 , ooOOoOO000 + 'SPORTS.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']KIDS[/COLOR]' , str ( OooO ) , 26 , ooOOoOO000 + 'KIDS.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']MUSIC[/COLOR]' , str ( OooO ) , 27 , ooOOoOO000 + 'MUSIC.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']PROGRAMS[/COLOR]' , str ( OooO ) , 28 , ooOOoOO000 + 'PROGRAMS.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']XXX[/COLOR]' , 'URL' , 29 , ooOOoOO000 + 'XXX.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 12 - 12 : O00o0O00
 if 69 - 69 : ii + O00o0O00
def iiiI1i ( ) :
 oOO0i1 ( )
 iII111I ( 'CHECK ADVANCED XML' , str ( OooO ) , 8 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'MUCKYS XML' , str ( OooO ) + '/wizard/muckys.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( '0CACHE XML' , str ( OooO ) + '/wizard/0cache.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'MIKEY1234 XML' , str ( OooO ) + '/wizard/mikey.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'TUXENS XML' , str ( OooO ) + '/wizard/tuxens.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'P2P RECOMMENDED XML1' , str ( OooO ) + '/wizard/p2p1.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'P2P RECOMMENDED XML2' , str ( OooO ) + '/wizard/p2p2.xml' , 7 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iII111I ( 'DELETE XML' , str ( OooO ) , 11 , ooOOoOO000 + 'XML.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 49 - 49 : IIiIiII11i - oOo0O0Ooo / I11O0O0oOO00O00o
def O0OooO00O0 ( ) :
 oOO0i1 ( )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']My Local Zip[/COLOR]' , ooOiiIII , 48 , ooOOoOO000 + 'MyLocalZIP.png' , o00O0oOOo , '' )
 iII111I ( '[COLOR' + iiiI1iiI11iii + ']My Online Zip[/COLOR]' , OO0oo00O , 43 , ooOOoOO000 + 'MyOnlineZip.png' , o00O0oOOo , '' )
 if 70 - 70 : O0OOOoOoo0 . o0o00Oo0O . ii1ii11IIIiiI . o0o00Oo0O + ooOoO0O00
def iiI1i111I1 ( ) :
 oOO0i1 ( )
 iII111I ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( OooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , ooOOoOO000 + 'FTV4.png' , o00O0oOOo , '' )
 iII111I ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( OooO ) + '/wizard/customftv/settings.xml' , 17 , ooOOoOO000 + 'FTV3.png' , o00O0oOOo , '' )
 iII111I ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , ooOOoOO000 + 'FTV1.png' , o00O0oOOo , '' )
 iII111I ( 'RESET FTV DATABASE' , 'url' , 18 , ooOOoOO000 + 'FTV2.png' , o00O0oOOo , '' )
 if 95 - 95 : oO0o - O00o0O00 / IIiIiII11i % Ii1I . I11i
 if 24 - 24 : ooOoO0O00 . Ii
 if 16 - 16 : I1ii11iIi11i % Ii1I + I11O0O0oOO00O00o - o0o00Oo0O . Ii1IIIi1 / ii1ii11IIIiiI
def iiIi11i1I1 ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SKINS[/COLOR]' , str ( OooO ) , 33 , ooOOoOO000 + 'Skins.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ARTWORK PACKS[/COLOR]' , str ( OooO ) , 34 , ooOOoOO000 + 'ArtworkPacks.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CREATE UNIVERSAL PATHS[/COLOR]' , Oo0oo0OoO0o0 , 35 , ooOOoOO000 + 'CreateUniversalPath.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 27 - 27 : o0o00Oo0O . ii1ii11IIIiiI / Ii1IIIi1
def o0OoO0 ( ) :
 I1iIIiI1i = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi11ii = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( I1iIIiI1i )
 for IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , IiiIiII1Ii1 , IiiIiII1Ii1 , '' )
 iiiiII1i1Iii1I1 ( 'tvshows' , 'INFO' )
 if 3 - 3 : o0o00Oo0O
def I11Ii1I1I ( url ) :
 I1iIIiI1i = II1I1i ( oo00OO0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 5 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 21 - 21 : ii - iI11I1II1I1I
def o0oo0000Oo ( ) :
 oOO0i1 ( )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']GOTHAM SKINS[/COLOR]' , str ( OooO ) , 36 , ooOOoOO000 + 'GothamSkins.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']HELIX SKINS[/COLOR]' , str ( OooO ) , 37 , ooOOoOO000 + 'HelixSkins.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']ISENGAARD SKINS[/COLOR]' , Oo0oo0OoO0o0 , 38 , ooOOoOO000 + 'IsengaardSkins.png' , o00O0oOOo , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 90 - 90 : O0OOOoOoo0 + IIiIiII11i * Ii1I / iI1ii11iIi1i . I11i + I11i
def o00O00 ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + I1I1Ii1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 26 - 26 : OOooOOo / I1ii11iIi11i - ooOoO0O00 + I11O0O0oOO00O00o
def O00oooOoO ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + IIi1i111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 96 - 96 : Ii1IIIi1
def Ii1oo0O0OO ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + oO00II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 13 - 13 : ii * oO0oo0o - iI1ii11iIi1i / O00o0O00 + I11O0O0oOO00O00o + ooOOOoO
def II1ii1I11 ( url ) :
 I1iIIiI1i = II1I1i ( I1Iii1III ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 17 - 17 : IIiIiII11i / IIiIiII11i
def ii1I11 ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + ooOOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 40 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 3 - 3 : o0o00Oo0O % ii / O00o0O00
def i1I11I1iIii ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + i11IiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 5 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 70 - 70 : oO0oo0o - oO0oo0o
def I1II1oooOooOO ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']GenieTv Apps[/COLOR]' , '' , 80002 , ooOOoOO000 + 'APKAndroidOnly.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']APK Factory[/COLOR]' , str ( OooO ) , 2 , ooOOoOO000 + 'APKAndroidOnly.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']APK Search[/COLOR]' , str ( OooO ) , 30038 , ooOOoOO000 + 'APKSearch.png' , o00O0oOOo , '' )
 if 1 - 1 : oOo0O0Ooo * Ii + ii1ii11IIIiiI * Ii + oO0o
def i1i1IIiIiI11 ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi11ii = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , ooo0OO0o00 in IIi11ii :
  i11i1i1i ( 'Android Apps' + ooo0OO0o00 , 'https://www.apkfiles.com' + i11iii1II1I1 , 30035 , ooOOoOO000 + 'apps.png' )
 for i11iii1II1I1 , ooo0OO0o00 in OOOO0oO0OOo0o :
  i11i1i1i ( 'Android Games' + ooo0OO0o00 , 'https://www.apkfiles.com' + i11iii1II1I1 , 30035 , ooOOoOO000 + 'GAMES.png' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def ooO00O ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if '/cat' in url :
   i11i1i1i ( ( I111iIii1i1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , ooOOoOO000 + 'APK.png' )
def Oo0OoooOoO0O0 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if '/app' in url :
   i11i1i1i ( ( I111iIii1i1 ) . replace ( '&amp;' , ' - ' ) , ( I1Iii1III ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , ooOOoOO000 + 'APK.png' )
def iIi1iOoo ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 II1OoOOoOOOoooO0 = url
 IIi11ii = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'href="([^"]*)" style="float:right;">next &gt;</a>' ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if 'apk' in url :
   i11i1i1i ( ( I111iIii1i1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + IiiIiII1Ii1 )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( 'NEXT' , II1OoOOoOOOoooO0 + url , 30037 , ooOOoOO000 + 'Next.png' )
def Iiii1ii ( name , url ) :
 ooO0Oo = oO0ooo000 ( url )
 name = name
 IIi11ii = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  url = 'https://www.apkfiles.com' + url
  OOOO0oo0o0O ( name , url )
def IIiiiIooooO0OOo0o0 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0OOo = 'https://www.apkfiles.com/search?q=' + ( ii1I1IIi ) . replace ( ' ' , '+' ) + '&search_type=1'
 OooOooO0OoOoo0o = o00oOO0OOo . lower ( )
 iIi1iOoo ( OooOooO0OoOoo0o )
 if 6 - 6 : iI1ii11iIi1i % ooOoO0O00 . iI1ii11iIi1i * iI1ii11iIi1i
def IIo000o0O0000o ( url ) :
 II1OO = xbmc . translatePath ( os . path . join ( ii1Iii1iiI11 , 'Download' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i11ii1II = os . path . join ( II1OO , I111iIii1i1 + '.apk' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 86 - 86 : I11O0O0oOO00O00o / I11i - I11i + Ii1I + oO0oo0o
def ooOo00OOo0 ( url ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i11ii1II = os . path . join ( II1OO , I111iIii1i1 + '.mp4' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 8 - 8 : OOooOOo / o0o00Oo0O * o0o00Oo0O % ii1ii11IIIiiI - I1ii11iIi11i + I11O0O0oOO00O00o
 if 83 - 83 : o0o00Oo0O . oOo0O0Ooo
def ii1IIi ( name , url , description ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i11ii1II = os . path . join ( II1OO , name )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 iii1Ii = xbmc . translatePath ( os . path . join ( OOOo00OOooO ) )
 time . sleep ( 2 )
 iII1I1iIi1i . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iii1Ii
 print '======================================='
 extract . all ( i11ii1II , iii1Ii , iII1I1iIi1i )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 16 - 16 : I1ii11iIi11i + O0OOOoOoo0 / I1ii11iIi11i / oO0o % oO0oo0o % Ii1I
 if 22 - 22 : IIiIiII11i * oO0o * I11O0O0oOO00O00o + Ii1I * I11i
 if 100 - 100 : ooOoO0O00 / ooOOOoO
 if 3 - 3 : IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
 if 37 - 37 : Ii1IIIi1 / I1ii11iIi11i . I11O0O0oOO00O00o * I11O0O0oOO00O00o
def O0Oo0Oo000 ( ) :
 I1iIIiI1i = II1I1i ( ooOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi11ii = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , i11iii1II1I1 , I1i1I1i1I1 , i1I , ooo0Oo00000oooO in IIi11ii :
  iII111I ( I111iIii1i1 , i11iii1II1I1 , 80003 , I1i1I1i1I1 , ooOOoOO000 + 'APKToolsB.png' , ooo0Oo00000oooO )
def iIiiiiIi111I ( apk , ret = None ) :
 if apk == "kodi" :
  ooOo00oOOOO0 = "https://kodi.tv/download/"
  I1iIIiI1i = II1I1i ( ooOo00oOOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi11ii = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( I1iIIiI1i )
  if len ( IIi11ii ) == 1 :
   iii1IiIiII1 = IIi11ii [ 0 ] [ 0 ]
   OooooO0000 = IIi11ii [ 0 ] [ 1 ]
   O00oo00O0OO0ooO = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( iii1IiIiII1 , OooooO0000 )
  if ret == 'version' : return iii1IiIiII1
  else : return O00oo00O0OO0ooO
 elif apk == "spmc" :
  iIi1I = 'https://github.com/koying/SPMC/releases/latest/'
  I1iIIiI1i = II1I1i ( iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi11ii = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( I1iIIiI1i )
  iii1IiIiII1 = re . sub ( '<[^<]+?>' , '' , IIi11ii [ 0 ] ) . replace ( ' ' , '' )
  O00oo00O0OO0ooO = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( iii1IiIiII1 , iii1IiIiII1 )
  if ret == 'version' : return iii1IiIiII1
  else : return O00oo00O0OO0ooO
def OOOO0oo0o0O ( name , url ) :
 if IiI1III1 ( ) == 'android' :
  OO0O0ooOo = ooOOoOoOoO00 . yesno ( iIOoO0O00o0ooo0 , "Would you like to download and install:" , "%s" % name )
  if not OO0O0ooOo : iI11 ( iIOoO0O00o0ooo0 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iI1ii111II = name
  if OO0O0ooOo :
   if not os . path . exists ( oo0 ) : os . makedirs ( oo0 )
   if not iI1IiiI ( url ) == True : iI11 ( iIOoO0O00o0ooo0 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iII1I1iIi1i . create ( iIOoO0O00o0ooo0 , 'Downloading %s' % iI1ii111II , '' , 'Please Wait' )
   i11ii1II = os . path . join ( oo0 , "%s.apk" % name )
   try : os . remove ( i11ii1II )
   except : pass
   downloader . download ( url , i11ii1II , iII1I1iIi1i )
   xbmc . sleep ( 500 )
   iII1I1iIi1i . close ( )
   ooOOoOoOoO00 . ok ( iIOoO0O00o0ooo0 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + i11ii1II + '")' )
  else : iI11 ( iIOoO0O00o0ooo0 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iI11 ( iIOoO0O00o0ooo0 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 59 - 59 : ii . iI1ii11iIi1i / o0o00Oo0O - O00o0O00
 if 1 - 1 : ooOOOoO / ooOOOoO - Ii
 if 87 - 87 : I1ii11iIi11i / o0o00Oo0O * ooOOOoO / I11i
 if 19 - 19 : ii1ii11IIIiiI + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
def IiIi11iI1IIi ( ) :
 if not os . path . exists ( o00OoO00o0 ) : os . makedirs ( o00OoO00o0 )
 I1iIIiI1i = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( I1iIIiI1i )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11iii1II1I1 = ( ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + i11iii1II1I1 )
  oo0Oo0oo ( ( I111iIii1i1 ) . replace ( '_' , ' ' ) , i11iii1II1I1 )
  if 63 - 63 : Ii1IIIi1 * Ii1I . ii / O00o0O00 * I1ii11iIi11i . O0OOOoOoo0
def oo0Oo0oo ( name , url ) :
 if IiI1III1 ( ) == 'android' :
  OO0O0ooOo = ooOOoOoOoO00 . yesno ( iIOoO0O00o0ooo0 , "Would you like to download and install:" , "%s" % name )
  if not OO0O0ooOo : iI11 ( iIOoO0O00o0ooo0 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iI1ii111II = name
  if OO0O0ooOo :
   if not os . path . exists ( o00OoO00o0 ) : os . makedirs ( o00OoO00o0 )
   if not iI1IiiI ( url ) == True : iI11 ( iIOoO0O00o0ooo0 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   iII1I1iIi1i . create ( iIOoO0O00o0ooo0 , 'Downloading %s' % iI1ii111II , '' , 'Please Wait' )
   i11ii1II = os . path . join ( o00OoO00o0 , "%s.apk" % name )
   try : os . remove ( i11ii1II )
   except : pass
   downloader . download ( url , i11ii1II , iII1I1iIi1i )
   xbmc . sleep ( 500 )
   iII1I1iIi1i . close ( )
   ooOOoOoOoO00 . ok ( iIOoO0O00o0ooo0 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + i11ii1II + '")' )
  else : iI11 ( iIOoO0O00o0ooo0 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iI11 ( iIOoO0O00o0ooo0 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 62 - 62 : ooOoO0O00 / O0OOOoOoo0 . oOo0O0Ooo * I11i
 if 21 - 21 : I11i
def o0Ooo0oOoo ( url ) :
 I1iIIiI1i = II1I1i ( OooO + ( I1Iii1III ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 5 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
 if 98 - 98 : ii1ii11IIIiiI
 if 92 - 92 : ii1ii11IIIiiI - iI11I1II1I1I
def O0OoO0O ( url ) :
 I1iIIiI1i = II1I1i ( OooO + ( I1Iii1III ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 30015 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 78 - 78 : ii
def OoOoo00O00oOOO ( url , iconimage , fanart ) :
 I1iIIiI1i = II1I1i ( url )
 ii1iIii = url
 IiiIiII1Ii1 = iconimage
 fanart = fanart
 IIi11ii = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( I1iIIiI1i )
 for II1OoOOoOOOoooO0 , I111iIii1i1 in IIi11ii :
  if '.mp4' in I111iIii1i1 :
   iII111I ( 'Watch VIDEO' , url + '/' + II1OoOOoOOOoooO0 , 222 , IiiIiII1Ii1 , fanart , '' )
  if 'description' in I111iIii1i1 :
   iII111I ( 'Read Description' , url + '/' + II1OoOOoOOOoooO0 , 30017 , IiiIiII1Ii1 , fanart , '' )
  if 'images' in I111iIii1i1 :
   Ooooo0Oo0oOo ( 'View Images' , url + '/' + II1OoOOoOOOoooO0 , 30018 , IiiIiII1Ii1 , fanart , '' )
  if 'url' in I111iIii1i1 :
   iII111I ( 'Install Build On Android' , url + '/' + II1OoOOoOOOoooO0 , 30016 , IiiIiII1Ii1 , fanart , '' )
  if 'url' in I111iIii1i1 :
   iII111I ( 'Install Build On Pc' , url + '/' + II1OoOOoOOOoooO0 , 30019 , IiiIiII1Ii1 , fanart , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
 if 36 - 36 : I11i + I11O0O0oOO00O00o - ooOOOoO + iI11I1II1I1I + ii
def OoooOOOoO0 ( url ) :
 I1iIIiI1i = II1I1i ( url )
 IIi11ii = re . compile ( 'url="([^"]*)"' ) . findall ( I1iIIiI1i )
 for url in IIi11ii :
  O0OO0 ( url )
  if 5 - 5 : I1ii11iIi11i - Ii1I % oO0oo0o - IIiIiII11i . oOo0O0Ooo + Ii1IIIi1
def OO0oO0o0oOO ( url ) :
 I1iIIiI1i = II1I1i ( url )
 IIi11ii = re . compile ( 'url="([^"]*)"' ) . findall ( I1iIIiI1i )
 for url in IIi11ii :
  Iii1OO ( url )
  if 45 - 45 : I1ii11iIi11i - I11i % ii1ii11IIIiiI
def iI1III11IIi11Ii11 ( url ) :
 I1iIIiI1i = II1I1i ( url )
 IIi11ii = re . compile ( 'desc="([^"]*)"' ) . findall ( I1iIIiI1i )
 for iII1I in IIi11ii :
  i11i1IiIi11 ( 'Description:' , iII1I )
  if 63 - 63 : ooOOOoO + I11i
def oOoOo0O00Oo ( url ) :
 I1iIIiI1i = II1I1i ( url )
 url = url
 IIi11ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1iIIiI1i )
 for II1OoOOoOOOoooO0 , I111iIii1i1 in IIi11ii :
  if 'png' in I111iIii1i1 :
   iII111I ( 'image' , '' , '' , url + '/' + II1OoOOoOOOoooO0 , url + '/' + II1OoOOoOOOoooO0 , '' )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 83 - 83 : iI11I1II1I1I
def Iiii1iiIi ( name , url , description ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i11ii1II = os . path . join ( II1OO , name + '.zip' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 iII1I1iIi1i . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoOOi1iIiII111i11
 print '======================================='
 extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ii1iii1 ( )
 if 7 - 7 : IIiIiII11i - O00o0O00 . IIiIiII11i
 if 53 - 53 : oO0oo0o % I11O0O0oOO00O00o . O0OOOoOoo0 - OOooOOo
def Iii1OO ( url ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i11ii1II = os . path . join ( II1OO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iII1I1iIi1i . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoOOi1iIiII111i11
 print '======================================='
 extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
 i1iIiiii ( url )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0o0oOo0OooO ( )
 if 21 - 21 : oOo0O0Ooo % I11i
def O0OO0 ( url ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i11ii1II = os . path . join ( II1OO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 iII1I1iIi1i . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoOOi1iIiII111i11
 print '======================================='
 extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
 i1iIiiii ( url )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0o0oOo0OooO ( )
 if 33 - 33 : O00o0O00
def iI1IiI1 ( name , url , description ) :
 oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 i11ii1II = os . path . join ( ooOiiIII )
 time . sleep ( 2 )
 iII1I1iIi1i . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oOoOOi1iIiII111i11
 print '======================================='
 extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0o0oOo0OooO ( )
 if 49 - 49 : I11i * iI1ii11iIi1i + I11O0O0oOO00O00o + Ii1IIIi1
def IiI1III1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def OoOoooOooOO0o ( log ) :
 xbmc . log ( "[%s]: %s" % ( iIOoO0O00o0ooo0 , log ) )
 if not os . path . exists ( i1I1Iii1IiiIi ) : os . makedirs ( i1I1Iii1IiiIi )
 if not os . path . exists ( OoOo00ooOO000 ) : O00o0 = open ( OoOo00ooOO000 , 'w' ) ; O00o0 . close ( )
 with open ( OoOo00ooOO000 , 'a' ) as O00o0 :
  o0o0ooo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  O00o0 . write ( o0o0ooo . rstrip ( '\r\n' ) + '\n' )
def O0o0oOo0OooO ( ) :
 iiiiOo000O00o0O = ooOOoOoOoO00 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iiiiOo000O00o0O == 0 : return
 elif iiiiOo000O00o0O == 1 : pass
 oOooO = IiI1III1 ( )
 OoOoooOooOO0o ( "Platform: " + str ( oOooO ) )
 os . _exit ( 1 )
 OoOoooOooOO0o ( "Force close failed!  Trying alternate methods." )
 if oOooO == 'osx' :
  OoOoooOooOO0o ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  ooOOoOoOoO00 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOooO == 'linux' :
  OoOoooOooOO0o ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  ooOOoOoOoO00 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oOooO == 'android' :
  OoOoooOooOO0o ( "############ try android force close #################" )
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
  ooOOoOoOoO00 . ok ( iIOoO0O00o0ooo0 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif oOooO == 'windows' :
  OoOoooOooOO0o ( "############ try windows force close #################" )
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
  ooOOoOoOoO00 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  OoOoooOooOO0o ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  OoOoooOooOO0o ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  ooOOoOoOoO00 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 4 - 4 : ooOoO0O00 + O0OOOoOoo0 + ooOoO0O00
  if 31 - 31 : iI1ii11iIi1i
  if 78 - 78 : Ii + I11i + ii1ii11IIIiiI / I11i % iI11I1II1I1I % ooOOOoO
def o0OOooo0ooo0o ( url ) :
 iII1I1iIi1i . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( url ) :
  for file in IIIIi1iII :
   if file . endswith ( ".xml" ) :
    iII1I1iIi1i . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooO0o0o = open ( ( os . path . join ( i11IIi , file ) ) ) . read ( )
    O00iiIi1iI1iI1i = ooO0o0o . replace ( Oo0oo0OoO0o0 , 'special://home/' )
    O00o0 = open ( ( os . path . join ( i11IIi , file ) ) , mode = 'w' )
    O00o0 . write ( str ( O00iiIi1iI1iI1i ) )
    O00o0 . close ( )
 O0o0oOo0OooO ( )
 if 36 - 36 : I11O0O0oOO00O00o . IIiIiII11i
def I1I1iI ( ) :
 i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']GENRE[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , ooOOoOO000 + 'RadioNomy.png' )
 i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']SORT BY[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , ooOOoOO000 + 'RadioNomy.png' )
 i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']SEARCH[/COLOR]' ) , '' , 70006 , ooOOoOO000 + 'RadioNomy.png' )
 if 18 - 18 : Ii1IIIi1 - oO0oo0o % Ii1IIIi1 / I11O0O0oOO00O00o
def ii1IiIiIi ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , ooOOoOO000 + 'RadioNomy.png' )
def OoO0OoOOOO ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , ooOOoOO000 + 'RadioNomy.png' )
def I1iII1IiI11i ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in OOOO0oO0OOo0o :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']Filter - ' + I111iIii1i1 + '[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , ooOOoOO000 + 'RadioNomy.png' )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']Stream - ' + I111iIii1i1 + '[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , IiiIiII1Ii1 )
def OOOoO ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  IIIIi1I ( url )
def ooOO0O0OooO0 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi
 IiiIoOOoO0 = 'https://www.radionomy.com/en/search/index?query=' + ( ii1I1IIi ) . replace ( ' ' , '+' )
 o0000o0OOOo = II1I1i ( IiiIoOOoO0 )
 IIi11ii = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']Stream - ' + I111iIii1i1 + '[/COLOR]' ) , ( I1Iii1III ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + i11iii1II1I1 , 70005 , IiiIiII1Ii1 )
  if 78 - 78 : O00o0O00 + Ii1IIIi1 . ooOOOoO
  if 91 - 91 : iI11I1II1I1I . I11i . Ii1I + ii
def oooO00O0O0OOO ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , 'http://www.listenlive.eu/' + i11iii1II1I1 , 10111113 , ooOOoOO000 + 'radio.png' )
def I1iIiIi111 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  OoO00O ( I111iIii1i1 , url , 222 , ooOOoOO000 + 'radio.png' )
  if 71 - 71 : ooOOOoO + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OO0o0oo ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.toonjet.com/' + i11iii1II1I1 , 8051 , ooOOoOO000 + 'classictoons.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00I11II1iI ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 in IIi11ii :
  if 'ol.gif' in IiiIiII1Ii1 :
   pass
  elif 'link_block_' in IiiIiII1Ii1 :
   pass
  elif '.png' in IiiIiII1Ii1 :
   pass
  else :
   i11i1i1i ( ( IiiIiII1Ii1 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , ooOOoOO000 + 'vod.png' )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , ooOOoOO000 + 'Next.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1Ooo0O0OO0OOo ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , ooOOoOO000 + 'classictoons.png' )
  if 57 - 57 : OOooOOo . iI11I1II1I1I % O0OOOoOoo0 % iI1ii11iIi1i * OOooOOo
  if 8 - 8 : OOooOOo . O0OOOoOoo0 % oO0oo0o . oOo0O0Ooo % oOo0O0Ooo . iI1ii11iIi1i
def i111ii11I1 ( ) :
 iii1I1 ( 'Audio Books' , '' , 30011 , ooOOoOO000 + 'AudioBooks.png' , ooOOoOO000 + 'AudioBooks.png' , '' )
 iii1I1 ( 'Kids Audio Books' , '' , 30006 , ooOOoOO000 + 'KidsAudioBooks.png' , ooOOoOO000 + 'KidsAudioBooks.png' , '' )
 if 9 - 9 : IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
def O00Iii1IIiIi ( ) :
 iii1I1 ( 'All' , '' , 30001 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
 iii1I1 ( 'Popular' , '' , 30012 , ooOOoOO000 + 'POPULARv.png' , ooOOoOO000 + 'POPULARv.png' , '' )
 iii1I1 ( 'Search' , '' , 30013 , ooOOoOO000 + 'Search.png' , ooOOoOO000 + 'Search.png' , '' )
 if 27 - 27 : iI1ii11iIi1i + oOo0O0Ooo * iI11I1II1I1I . ii * OOooOOo
def OooOo0o ( ) :
 o0000o0OOOo = II1I1i ( I11i1I111II1IiI + 'books' + ooOo0Oo )
 IIi11ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , i11iii1II1I1 , O0000O0 in IIi11ii :
  if 'Parent' in I111iIii1i1 :
   pass
  elif '2' in O0000O0 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 38 - 38 : iI11I1II1I1I + Ii * oO0o * O0OOOoOoo0 % O00o0O00
def iiI1iii1I111 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 o0000o0OOOo = II1I1i ( I11i1I111II1IiI + 'books' + ooOo0Oo )
 IIi11ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , i11iii1II1I1 , O0000O0 in IIi11ii :
  if ii1I1IIi in I111iIii1i1 . lower ( ) :
   if '1' in O0000O0 :
    iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   elif '2' in O0000O0 :
    iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   elif '3' in O0000O0 :
    iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30009 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
    if 40 - 40 : I11O0O0oOO00O00o % ii - O00o0O00 + I11i / O00o0O00
    if 84 - 84 : o0o00Oo0O
def I11I1 ( ) :
 o0000o0OOOo = II1I1i ( I11i1I111II1IiI + 'books' + ooOo0Oo )
 IIi11ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , i11iii1II1I1 , O0000O0 in IIi11ii :
  if '1' in O0000O0 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 3010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  elif '2' in O0000O0 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  elif '3' in O0000O0 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , i11iii1II1I1 , 30009 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 10 - 10 : Ii1IIIi1 - oO0oo0o * iI11I1II1I1I % iI11I1II1I1I * ooOOOoO - Ii1I
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97 : IIiIiII11i % ii1ii11IIIiiI + ii1ii11IIIiiI - oO0o / iI1ii11iIi1i * oOo0O0Ooo
def o0oOI1 ( url ) :
 II1OoOOoOOOoooO0 = url
 o0000o0OOOo = II1I1i ( url )
 OOOO0oO0OOo0o = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in OOOO0oO0OOo0o :
  if 'mp3' in I111iIii1i1 :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , II1OoOOoOOOoooO0 + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I111iIii1i1 :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , II1OoOOoOOOoooO0 + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I111iIii1i1 :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , II1OoOOoOOOoooO0 + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  elif '/' in I111iIii1i1 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , II1OoOOoOOOoooO0 + url , 30009 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 50 - 50 : iI1ii11iIi1i
   if 22 - 22 : I11O0O0oOO00O00o * o0o00Oo0O . IIiIiII11i - oO0o
   if 90 - 90 : oO0oo0o
def II11iiii ( url ) :
 o0000o0OOOo = II1I1i ( url )
 II1OoOOoOOOoooO0 = url
 IIi11ii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  if 'Parent' in I111iIii1i1 :
   pass
  elif '.db' in I111iIii1i1 :
   pass
  elif '.jpg' in I111iIii1i1 :
   pass
  elif '.html' in I111iIii1i1 :
   pass
  elif '.doc' in I111iIii1i1 :
   pass
  elif 'mp3' in I111iIii1i1 :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , II1OoOOoOOOoooO0 + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I111iIii1i1 :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , II1OoOOoOOOoooO0 + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  else :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , II1OoOOoOOOoooO0 + url , 30010 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 94 - 94 : Ii1IIIi1 + iI1ii11iIi1i % I11i
   if 1 - 1 : OOooOOo % ii1ii11IIIiiI - O00o0O00 + oO0oo0o + o0o00Oo0O * I11i
def O000o0Ooo ( ) :
 iii1I1 ( 'A-Z' , '' , 30007 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
 iii1I1 ( 'All' , '' , 30003 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
 iii1I1 ( 'Search' , '' , 30014 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
 if 70 - 70 : I1ii11iIi11i - oO0oo0o . iI11I1II1I1I % I11O0O0oOO00O00o / OOooOOo - o0o00Oo0O
def OOOOoo ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi11ii = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 in IIi11ii :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + i11iii1II1I1 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IiiIiII1Ii1 :
   pass
  else :
   iii1I1 ( IiiIiII1Ii1 , ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( i11iii1II1I1 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IiiIiII1Ii1 + '.gif' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 12 - 12 : OOooOOo % ooOOOoO % Ii1I . Ii * iI11I1II1I1I
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66 : Ii * iI11I1II1I1I % ii
 if 5 - 5 : OOooOOo % ii
def ooO00oOOo ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  if '</a>' in I111iIii1i1 :
   pass
  elif '(' in I111iIii1i1 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  else :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 14 - 14 : iI1ii11iIi1i % oOo0O0Ooo - iI11I1II1I1I . O00o0O00 + oO0o - ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5 : Ii1IIIi1
def iII1I11ii1III ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi11ii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if ii1I1IIi in I111iIii1i1 . lower ( ) :
   if '</a>' in I111iIii1i1 :
    pass
   elif '(' in I111iIii1i1 :
    iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i11iii1II1I1 , 30005 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   else :
    Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i11iii1II1I1 , 30004 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
    if 1 - 1 : O00o0O00 . ooOOOoO
    if 42 - 42 : O00o0O00 % oO0oo0o / oO0o - oO0oo0o * Ii
def IIii1iIIiII ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi11ii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if '</a>' in I111iIii1i1 :
   pass
  elif '(' in I111iIii1i1 :
   iii1I1 ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i11iii1II1I1 , 30005 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
  else :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + i11iii1II1I1 , 30004 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 78 - 78 : ii / O00o0O00 % OOooOOo * ii
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68 : oO0oo0o
 if 29 - 29 : Ii1IIIi1 + Ii % I11O0O0oOO00O00o
def i11i1IIOO0o ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  II1OoOOoOOOoooO0 = ( I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( II1OoOOoOOOoooO0 )
  if 33 - 33 : I11O0O0oOO00O00o
def oo00oO ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , url in IIi11ii :
  if '<p align' in I111iIii1i1 :
   pass
  elif '&nbsp;' in I111iIii1i1 :
   pass
  else :
   Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , I1Iii1III ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , ooOOoOO000 + 'KodibleAudioBooks.png' , ooOOoOO000 + 'KodibleAudioBooks.png' , '' )
   if 15 - 15 : I1ii11iIi11i + I11O0O0oOO00O00o . O0OOOoOoo0 - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 86 - 86 : oOo0O0Ooo / oO0oo0o * iI1ii11iIi1i
 if 64 - 64 : O0OOOoOoo0 / o0o00Oo0O * OOooOOo * O0OOOoOoo0
def ooOOO000 ( ) :
 o0000o0OOOo = cloudflare . source ( I1Iii1III ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi11ii = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'ongoing' in i11iii1II1I1 :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 21005 , ooOOoOO000 + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in i11iii1II1I1 :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 21005 , ooOOoOO000 + 'CartoonShows.png' , '' , '' )
  if 'disney' in i11iii1II1I1 :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 21005 , ooOOoOO000 + 'Disney.png' , '' , '' )
  if 'genre' in i11iii1II1I1 :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 21005 , ooOOoOO000 + 'Genre.png' , '' , '' )
  if 'years' in i11iii1II1I1 :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 21005 , ooOOoOO000 + 'Years.png' , '' , '' )
def O0OoO ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 oOo0O00 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o0000o0OOOo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , IiiIiII1Ii1 , IiiIiII1Ii1 , I111iIii1i1 )
 for url , I111iIii1i1 in oOo0O00 :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 21005 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
 for url in next :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NEXT[/COLOR]' , url , 21005 , ooOOoOO000 + 'Next.png' , '' , '' )
def iI11II ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 II111iii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 oOOiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o0000o0OOOo )
 O0O0Oo0O0Oo00 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
 for url in oOOiI :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']PLAY[/COLOR]' , 'http:' + url , 222 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
 for url , I111iIii1i1 in II111iii :
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 222 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
 else :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
def o0Oo0Ooo ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  iII111I ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 222 , ooOOoOO000 + 'watchcartoons.png' , '' , '' )
  if 71 - 71 : IIiIiII11i - iI1ii11iIi1i - Ii1IIIi1 * o0o00Oo0O * ooOOOoO
def o000ooOo0o0Oo ( ) :
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']CARTOONS[/COLOR]' , '' , 20001 , ooOOoOO000 + 'ORIGINCARTOON.png' )
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , ooOOoOO000 + 'ORIGINCARTOON.png' )
 if 55 - 55 : oOo0O0Ooo
def o0OO0II111Iiii1 ( ) :
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , ooOOoOO000 + 'ORIGINCARTOON.png' )
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , ooOOoOO000 + 'ORIGINCARTOON.png' )
 if 65 - 65 : oO0oo0o + Ii1I / O00o0O00
def iIiIII1Ii ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  if '?c=' in url :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOOoOO000 + 'ORIGINCARTOON.png' )
   if 49 - 49 : Ii % OOooOOo + ii1ii11IIIiiI . IIiIiII11i % Ii1IIIi1 * O00o0O00
def O0oOo ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , ooo0Oo00000oooO , I111iIii1i1 in IIi11ii :
  if 'Genre' in url :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , ooOOoOO000 + 'ORIGINCARTOON.png' )
   if 27 - 27 : Ii - oOo0O0Ooo
def iIII1Ii1 ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , ooo0Oo00000oooO , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , ooo0Oo00000oooO )
  if 33 - 33 : I11O0O0oOO00O00o
def I1111i1I ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , ooo0Oo00000oooO , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , ooo0Oo00000oooO )
  if 69 - 69 : iI11I1II1I1I * oOo0O0Ooo - Ii1IIIi1 + o0o00Oo0O + o0o00Oo0O
  if 65 - 65 : ii1ii11IIIiiI / Ii / oO0o - O00o0O00
  if 9 - 9 : oOo0O0Ooo / ii1ii11IIIiiI - I1ii11iIi11i * iI11I1II1I1I
  if 86 - 86 : IIiIiII11i + O0OOOoOoo0 + ooOOOoO
  if 9 - 9 : O0OOOoOoo0 + IIiIiII11i % O0OOOoOoo0 % ooOOOoO + iI11I1II1I1I
def OOoooOO0o ( ) :
 if 7 - 7 : o0o00Oo0O % ii1ii11IIIiiI + Ii1I + iI1ii11iIi1i % ii . I1ii11iIi11i
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Cartoons[/COLOR]' , I1Iii1III ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , ooOOoOO000 + 'ORIGINCARTOON.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Search Cartoons[/COLOR]' , '' , 10005 , ooOOoOO000 + 'ORIGINCARTOON.png' , o00O0oOOo , '' )
 if 56 - 56 : Ii1IIIi1
def O00oo0Ooo ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 66 - 66 : OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 IIi11ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o0000o0OOOo )
 if 87 - 87 : O00o0O00 + I11i . Ii1IIIi1 - ii
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if ii1I1IIi in I111iIii1i1 . lower ( ) :
   if 'Dad!' in I111iIii1i1 :
    pass
   elif 'Family Guy' in I111iIii1i1 :
    pass
   elif '2 Stupid' in I111iIii1i1 :
    pass
   elif 'The Zelfs' in I111iIii1i1 :
    pass
   elif 'A Clone' in I111iIii1i1 :
    pass
   elif 'A.T.O.M' in I111iIii1i1 :
    pass
   elif 'Almost Naked' in I111iIii1i1 :
    pass
   elif 'Angry Kid' in I111iIii1i1 :
    pass
   elif 'Annoying Orange' in I111iIii1i1 :
    pass
   elif 'Aqua Teen' in I111iIii1i1 :
    pass
   elif 'Assy Mcgee' in I111iIii1i1 :
    pass
   elif 'Astroblast' in I111iIii1i1 :
    pass
   elif 'Atomic Betty' in I111iIii1i1 :
    pass
   elif 'Axe Cop' in I111iIii1i1 :
    pass
   elif 'Baby Playpen' in I111iIii1i1 :
    pass
   elif 'Beavis and Butt' in I111iIii1i1 :
    pass
   elif 'Celebrity Deathmatch' in I111iIii1i1 :
    pass
   elif 'Clerks The' in I111iIii1i1 :
    pass
   elif 'Crapston Villas' in I111iIii1i1 :
    pass
   elif 'Duckman:' in I111iIii1i1 :
    pass
   elif 'Stripperella' in I111iIii1i1 :
    pass
   elif 'Vixen' in I111iIii1i1 :
    pass
   else :
    Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 10006 , ooOOoOO000 + 'ORIGINCARTOON.png' , o00O0oOOo , '' )
    if 6 - 6 : iI11I1II1I1I * ii
    if 28 - 28 : I1ii11iIi11i * I11i / ii1ii11IIIiiI
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52 : o0o00Oo0O / I11i % Ii1IIIi1 * oOo0O0Ooo % O00o0O00
def iIiI ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if 'Dad!' in I111iIii1i1 :
   pass
  elif 'Family Guy' in I111iIii1i1 :
   pass
  elif '2 Stupid' in I111iIii1i1 :
   pass
  elif 'The Zelfs' in I111iIii1i1 :
   pass
  elif 'A Clone' in I111iIii1i1 :
   pass
  elif 'A.T.O.M' in I111iIii1i1 :
   pass
  elif 'Almost Naked' in I111iIii1i1 :
   pass
  elif 'Angry Kid' in I111iIii1i1 :
   pass
  elif 'Annoying Orange' in I111iIii1i1 :
   pass
  elif 'Aqua Teen' in I111iIii1i1 :
   pass
  elif 'Assy Mcgee' in I111iIii1i1 :
   pass
  elif 'Astroblast' in I111iIii1i1 :
   pass
  elif 'Atomic Betty' in I111iIii1i1 :
   pass
  elif 'Axe Cop' in I111iIii1i1 :
   pass
  elif 'Baby Playpen' in I111iIii1i1 :
   pass
  elif 'Beavis and Butt' in I111iIii1i1 :
   pass
  elif 'Celebrity Deathmatch' in I111iIii1i1 :
   pass
  elif 'Clerks The' in I111iIii1i1 :
   pass
  elif 'Crapston Villas' in I111iIii1i1 :
   pass
  elif 'Duckman:' in I111iIii1i1 :
   pass
  elif 'Stripperella' in I111iIii1i1 :
   pass
  elif 'Vixen' in I111iIii1i1 :
   pass
  else :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 10006 , ooOOoOO000 + 'ORIGINCARTOON.png' , o00O0oOOo , '' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11 : ooOoO0O00
def iIi1Iii ( url ) :
 ooO0Oo = II1I1i ( url )
 OOOO0oO0OOo0o = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 in OOOO0oO0OOo0o :
  OoOO0OooOoooo = IiiIiII1Ii1
 IIIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( ooO0Oo )
 for url in IIIii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NEXT PAGE[/COLOR]' , url , 10006 , ooOOoOO000 + 'Next.png' , o00O0oOOo , '' )
 IIi11ii = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 10007 , OoOO0OooOoooo )
  if 23 - 23 : ooOoO0O00 . iI11I1II1I1I . O00o0O00 . o0o00Oo0O % iI1ii11iIi1i % Ii
  if 11 - 11 : o0o00Oo0O - IIiIiII11i . O00o0O00 . iI1ii11iIi1i % ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21 : I1ii11iIi11i / Ii1IIIi1 . ii1ii11IIIiiI * ii + I11O0O0oOO00O00o - ooOoO0O00
def iIii1111Ii1I1 ( url , IMAGE ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  print I111iIii1i1 + '     ' + url
  if 'easy' in url :
   O00o00oOOo ( url )
   if 38 - 38 : iI11I1II1I1I / O0OOOoOoo0
   if 13 - 13 : iI11I1II1I1I
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 77 - 77 : Ii - iI11I1II1I1I / oO0oo0o / O0OOOoOoo0 / oO0o
def O00o00oOOo ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( "url: '(.+?)'," ) . findall ( ooO0Oo )
 for url in IIi11ii :
  IIIIi1I ( url )
  if 56 - 56 : ii * o0o00Oo0O
  if 85 - 85 : ii % OOooOOo * iI11I1II1I1I
  if 44 - 44 : iI11I1II1I1I . Ii1I + ii1ii11IIIiiI . O0OOOoOoo0
def I1oO ( ) :
 if 28 - 28 : IIiIiII11i - oO0oo0o % OOooOOo + oO0o - OOooOOo
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Stand Up[/COLOR]' , '' , 10014 , ooOOoOO000 + 'StandUp.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Search Comedian[/COLOR]' , '' , 10015 , ooOOoOO000 + 'SearchComedian.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Others[/COLOR]' , '' , 10017 , ooOOoOO000 + 'Others.png' , o00O0oOOo , '' )
 if 28 - 28 : IIiIiII11i . oO0oo0o + o0o00Oo0O . o0o00Oo0O . O00o0O00
def Oo0o0O0oO0o ( ) :
 o0000o0OOOo = II1I1i ( ( I1Iii1III ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if 'elete' in I111iIii1i1 :
   pass
  else :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 222 , IiiIiII1Ii1 )
   if 50 - 50 : ooOOOoO + I11i
def iiIioo0O0 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 o0000o0OOOo = II1I1i ( ( I1Iii1III ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oooO000oO0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , I1iIIiiII , I1Iii11II in oooO000oO0O :
  for ii1I1IIi in I1iIIiiII :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0ooo0ooo0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1Iii11II )
   for i11iii1II1I1 , I111iIii1i1 in o0ooo0ooo0 :
    if 'tube' in i11iii1II1I1 :
     pass
    elif 'stage' in i11iii1II1I1 :
     OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I1iIIiiII + '   -   ' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiiIiII1Ii1 , )
    elif 'vee' in i11iii1II1I1 :
     pass
     if 7 - 7 : Ii + oOo0O0Ooo
def IIi1Ii1I ( ) :
 o0000o0OOOo = II1I1i ( ( I1Iii1III ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 oooO000oO0O = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , I1iIIiiII , I1Iii11II in oooO000oO0O :
  o0ooo0ooo0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1Iii11II )
  for i11iii1II1I1 , I111iIii1i1 in o0ooo0ooo0 :
   if 'tube' in i11iii1II1I1 :
    pass
   elif 'stage' in i11iii1II1I1 :
    OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I1iIIiiII + '   -   ' + I111iIii1i1 + '[/COLOR]' , ( i11iii1II1I1 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiiIiII1Ii1 )
   elif 'vee' in i11iii1II1I1 :
    pass
    if 58 - 58 : O00o0O00 . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
    if 50 - 50 : Ii1IIIi1 % IIiIiII11i - O0OOOoOoo0 . ooOoO0O00 + o0o00Oo0O % Ii1IIIi1
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10 : Ii1IIIi1 . ooOoO0O00 + iI1ii11iIi1i
def Ii1i1i11I ( url ) :
 o0000o0OOOo = II1I1i ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I11III111i1I = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( o0000o0OOOo )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I11III111i1I ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I11III111i1I :
  IIIIi1I ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 87 - 87 : O0OOOoOoo0 / OOooOOo % I11i * oO0oo0o
  if 77 - 77 : oO0oo0o - I1ii11iIi11i - iI11I1II1I1I
  if 16 - 16 : oO0o / Ii1IIIi1 / ooOoO0O00 . Ii1IIIi1 + oO0oo0o
  if 26 - 26 : iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
  if 44 - 44 : ii . IIiIiII11i . O00o0O00 % ii
  if 86 - 86 : Ii + o0o00Oo0O * ooOOOoO - oO0o * O00o0O00 + o0o00Oo0O
  if 95 - 95 : iI11I1II1I1I . ii1ii11IIIiiI % Ii1IIIi1 - ii1ii11IIIiiI * IIiIiII11i
def OoooOoOo ( ) :
 if 59 - 59 : ooOoO0O00 % iI11I1II1I1I + ii
 iiII ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , o00O0oOOo , '' )
 iiII ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , o00O0oOOo , '' )
 if 32 - 32 : O0OOOoOoo0 % ii1ii11IIIiiI * I1ii11iIi11i
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 72 - 72 : O0OOOoOoo0 . Ii1IIIi1 - ii1ii11IIIiiI - iI1ii11iIi1i % ooOoO0O00
def i1iiIIiIi1 ( ) :
 iiII ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , o00O0oOOo , '' )
 iiII ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , o00O0oOOo , '' )
 if 24 - 24 : ii1ii11IIIiiI * oO0oo0o
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def IiI1111i1i11I ( ) :
 if 42 - 42 : ooOOOoO % Ii1IIIi1 % I11i % oO0oo0o + I11O0O0oOO00O00o % OOooOOo
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 O000oOoOO0oO0ooOOOoO = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 52 - 52 : iI1ii11iIi1i % O00o0O00 * oOo0O0Ooo % I11O0O0oOO00O00o + O00o0O00 / Ii1IIIi1
 for iIiIIii11iI in O000oOoOO0oO0ooOOOoO :
  ii1II1i1 = OoOoo + iIiIIii11iI + ooOo0Oo
  o0000o0OOOo = oo00oO0o000 ( ii1II1i1 )
  IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0000o0OOOo )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , i1I , I111iIii1i1 in IIi11ii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    oOOOOOOooO ( I111iIii1i1 , i11iii1II1I1 , 222 , O0O00OOOo00O , i1I , iIi11OoO0OOOo0Oo )
    if 46 - 46 : I11O0O0oOO00O00o . ooOOOoO / IIiIiII11i % iI11I1II1I1I + ooOOOoO
    iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 61 - 61 : O00o0O00 / oO0o + IIiIiII11i . oO0oo0o / I1ii11iIi11i * O00o0O00
    if 46 - 46 : iI11I1II1I1I
def i1iI1Iii11Iii11 ( ) :
 if 100 - 100 : Ii1I * Ii % oO0oo0o / I1ii11iIi11i / O0OOOoOoo0 + Ii1I
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 O000oOoOO0oO0ooOOOoO = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 59 - 59 : ii1ii11IIIiiI - ooOOOoO
 for iIiIIii11iI in O000oOoOO0oO0ooOOOoO :
  iIiiI = OoOoo + iIiIIii11iI + ooOo0Oo
  o0000o0OOOo = oo00oO0o000 ( iIiiI )
  IIi11ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0000o0OOOo )
  for I111iIii1i1 , iIi11OoO0OOOo0Oo , i11iii1II1I1 , IiiIiII1Ii1 , i1I , OOo000 in IIi11ii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iiII ( I111iIii1i1 , i11iii1II1I1 , OOo000 , IiiIiII1Ii1 , i1I , iIi11OoO0OOOo0Oo )
    if 80 - 80 : iI11I1II1I1I
    iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 23 - 23 : IIiIiII11i
    if 71 - 71 : ii1ii11IIIiiI * I1ii11iIi11i . I11O0O0oOO00O00o
def iI1iIIiIi1I1 ( ) :
 if 98 - 98 : oO0o - iI1ii11iIi1i . ooOOOoO % Ii
 ooO0Oo = II1I1i ( OoOoo + 'spongemain.php' )
 IIi11ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , iIi11OoO0OOOo0Oo , i11iii1II1I1 , IiiIiII1Ii1 , i1I , OOo000 in IIi11ii :
  iiII ( I111iIii1i1 , i11iii1II1I1 , OOo000 , IiiIiII1Ii1 , i1I , iIi11OoO0OOOo0Oo )
  iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
def oOo0oO0 ( url ) :
 if 84 - 84 : O0OOOoOoo0 + Ii - O00o0O00 * O0OOOoOoo0
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiIiIiiI1Ii = ( '%s%s' % ( iIIiiii , url ) )
 I1iIIiI1i = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iIIiI1i )
 for url , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in IIi11ii :
  OOo0o0oOOOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oo0o ) )
  for oo0Oii1IIi1ii in OOo0o0oOOOO00 :
   if oo0Oii1IIi1ii == url :
    I111iIii1i1 = ( '[COLORred]Watched - [/COLOR]' + I111iIii1i1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  oOOOOOOooO ( I111iIii1i1 , url , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
  if 50 - 50 : IIiIiII11i - ii1ii11IIIiiI + iI11I1II1I1I + iI11I1II1I1I
  iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
  if 91 - 91 : IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26 : I11i
  if 12 - 12 : ii / o0o00Oo0O + IIiIiII11i * Ii1I
def II1IiiI ( url ) :
 if 11 - 11 : iI11I1II1I1I . OOooOOo / ooOOOoO % O0OOOoOoo0
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , iIi11OoO0OOOo0Oo , url , IiiIiII1Ii1 , i1I , OOo000 in IIi11ii :
  iiII ( I111iIii1i1 , url , OOo000 , IiiIiII1Ii1 , i1I , iIi11OoO0OOOo0Oo )
  if 61 - 61 : O0OOOoOoo0 - O00o0O00 + O00o0O00
  iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
  if 40 - 40 : Ii . iI11I1II1I1I
  if 2 - 2 : ooOoO0O00 * oO0oo0o - oO0oo0o + ii % OOooOOo / OOooOOo
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3 : ii
def oOOOOOOooO ( name , url , mode , iconimage , fanart , description ) :
 if 71 - 71 : ooOOOoO + ooOoO0O00 - Ii1IIIi1 - Ii . I11O0O0oOO00O00o - O0OOOoOoo0
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoo0OoooOo0o . setProperty ( "Fanart_Image" , fanart )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = False )
 return Iii11i1111II
 if 85 - 85 : IIiIiII11i . O0OOOoOoo0 % O00o0O00 % I11O0O0oOO00O00o
def iiII ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80 : oO0oo0o * I11O0O0oOO00O00o / iI11I1II1I1I % oO0oo0o / iI11I1II1I1I
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoo0OoooOo0o . setProperty ( "Fanart_Image" , fanart )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = True )
 return Iii11i1111II
if 42 - 42 : ooOoO0O00 / Ii . I1ii11iIi11i * Ii1IIIi1 . Ii * o0o00Oo0O
if 44 - 44 : ooOoO0O00 . oOo0O0Ooo / Ii + ooOOOoO
if 27 - 27 : O00o0O00
if 52 - 52 : ii1ii11IIIiiI % OOooOOo + iI11I1II1I1I * oO0oo0o . iI1ii11iIi1i
if 95 - 95 : iI11I1II1I1I . ooOOOoO - ii * oO0o / I11i
if 74 - 74 : oO0oo0o
if 34 - 34 : Ii1IIIi1
if 44 - 44 : ooOoO0O00 % oOo0O0Ooo % I11i
if 9 - 9 : I1ii11iIi11i % ii - iI1ii11iIi1i
if 43 - 43 : oO0o % oO0o
if 46 - 46 : I1ii11iIi11i % iI11I1II1I1I . Ii1IIIi1 . o0o00Oo0O * O0OOOoOoo0 / ii
if 7 - 7 : oO0oo0o - o0o00Oo0O * I11O0O0oOO00O00o - I11i - IIiIiII11i
if 41 - 41 : oOo0O0Ooo - ii1ii11IIIiiI % IIiIiII11i . ii1ii11IIIiiI - I11O0O0oOO00O00o
if 45 - 45 : iI1ii11iIi1i - O00o0O00
if 70 - 70 : oO0o % oOo0O0Ooo / oOo0O0Ooo . I11O0O0oOO00O00o % O0OOOoOoo0 . IIiIiII11i
def oOoooOOO0o0 ( string ) :
 if o0OOo000ooo0o == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 73 - 73 : o0o00Oo0O . oO0oo0o + Ii + iI11I1II1I1I - I11O0O0oOO00O00o / OOooOOo
def i11iII1Ii1ii111 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iII11IIi1I1 = [ ]
 try :
  if 89 - 89 : I1ii11iIi11i + Ii1I - I11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iII ) == False :
  oOoooOOO0o0 ( 'Making Favorites File' )
  iII11IIi1I1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooO0o0o = open ( iII , "w" )
  ooO0o0o . write ( json . dumps ( iII11IIi1I1 ) )
  ooO0o0o . close ( )
 else :
  oOoooOOO0o0 ( 'Appending Favorites' )
  ooO0o0o = open ( iII ) . read ( )
  o00o0o = json . loads ( ooO0o0o )
  o00o0o . append ( ( name , url , iconimage , fanart , mode ) )
  O00iiIi1iI1iI1i = open ( iII , "w" )
  O00iiIi1iI1iI1i . write ( json . dumps ( o00o0o ) )
  O00iiIi1iI1iI1i . close ( )
  if 15 - 15 : I11O0O0oOO00O00o
  if 13 - 13 : iI11I1II1I1I * OOooOOo / ii1ii11IIIiiI % O0OOOoOoo0 + oO0oo0o
def ooOoOo ( ) :
 if os . path . exists ( iII ) == False :
  iII11IIi1I1 = [ ]
  oOoooOOO0o0 ( 'Making Favorites File' )
  iII11IIi1I1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ooO0o0o = open ( iII , "w" )
  ooO0o0o . write ( json . dumps ( iII11IIi1I1 ) )
  ooO0o0o . close ( )
 else :
  oO0oo0o00O0 = json . loads ( open ( iII ) . read ( ) )
  oO00Oo0 = len ( oO0oo0o00O0 )
  for iII11I1iIiI in oO0oo0o00O0 :
   I111iIii1i1 = iII11I1iIiI [ 0 ]
   i11iii1II1I1 = iII11I1iIiI [ 1 ]
   O0O00OOOo00O = iII11I1iIiI [ 2 ]
   try :
    IiIiI1111 = iII11I1iIiI [ 3 ]
    if IiIiI1111 == None :
     raise
   except :
    if o0OoO . getSetting ( 'use_thumb' ) == "true" :
     IiIiI1111 = O0O00OOOo00O
    else :
     IiIiI1111 = i1I
   try : OoO0OOOoo = iII11I1iIiI [ 5 ]
   except : OoO0OOOoo = None
   try : Oo00OoooO0o = iII11I1iIiI [ 6 ]
   except : Oo00OoooO0o = None
   if 39 - 39 : oOo0O0Ooo + I1ii11iIi11i
   if iII11I1iIiI [ 4 ] == 0 :
    Ooooo0Oo0oOo ( I111iIii1i1 , i11iii1II1I1 , '' , O0O00OOOo00O , i1I , '' , 'fav' )
   else :
    Ooooo0Oo0oOo ( I111iIii1i1 , i11iii1II1I1 , iII11I1iIiI [ 4 ] , O0O00OOOo00O , i1I , '' , 'fav' )
    if 83 - 83 : ooOoO0O00
def I1III1ii1 ( name ) :
 o00o0o = json . loads ( open ( iII ) . read ( ) )
 for iiI111iiII in range ( len ( o00o0o ) ) :
  if o00o0o [ iiI111iiII ] [ 0 ] == name :
   del o00o0o [ iiI111iiII ]
   O00iiIi1iI1iI1i = open ( iII , "w" )
   O00iiIi1iI1iI1i . write ( json . dumps ( o00o0o ) )
   O00iiIi1iI1iI1i . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 68 - 68 : iI1ii11iIi1i - oOo0O0Ooo
 if 41 - 41 : oO0oo0o
def oOo0oOOoo0O ( ) :
 O00oOI11I1iI = os . path . join ( iiiIiii11i1i , 'addons.ini' )
 OOoo00o0 = open ( O00oOI11I1iI , "w+" )
 o0000o0OOOo = II1I1i ( 'http://piesustv.net:8000/get.php?username=' + OO00OOo + '&password=' + IiI11i1IiI1 + '&type=m3u_plus&output=mpegts' )
 IIi11ii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( o0000o0OOOo )
 OOoo00o0 . write ( r'[' + OOOoO0oo0oo0o + ']' + '\n' )
 for I111iIii1i1 , IiiIiII1Ii1 , ii111I1iII1i1 , i11iii1II1I1 in IIi11ii :
  i11iii1II1I1 = ( i11iii1II1I1 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  o0OO0iI1II1i1ii = ( I111iIii1i1 + '=plugin://' + OOOoO0oo0oo0o + '/?url=' + i11iii1II1I1 + '&mode=10012&name=' + ( I111iIii1i1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( IiiIiII1Ii1 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( IiiIiII1Ii1 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OOoo00o0 . write ( o0OO0iI1II1i1ii + '\n' )
  if 28 - 28 : O0OOOoOoo0 - O00o0O00 / oOo0O0Ooo
  if 27 - 27 : ooOoO0O00 + oOo0O0Ooo * Ii1I + O00o0O00 . oO0oo0o
def OOooOOooo000OoO ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  iII111I ( I111iIii1i1 , ( i11iii1II1I1 ) . strip ( ) , 222 , ooOOoOO000 + '247.png' , ooOOoOO000 + '247.png' , '' )
def O0OOo ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  iII111I ( I111iIii1i1 , ( i11iii1II1I1 ) . strip ( ) , 222 , ooOOoOO000 + 'musicch.png' , ooOOoOO000 + 'musicch.png' , '' )
def oooOO0O ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  iII111I ( I111iIii1i1 , ( i11iii1II1I1 ) . strip ( ) , 222 , ooOOoOO000 + 'NEWS.png' , ooOOoOO000 + 'NEWS.png' , '' )
def oOOOoo00o0 ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  iII111I ( I111iIii1i1 , ( i11iii1II1I1 ) . strip ( ) , 222 , ooOOoOO000 + 'adult.png' , ooOOoOO000 + 'adult.png' , '' )
def oo0oO ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi11ii = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  iII111I ( I111iIii1i1 , i11iii1II1I1 , 1016 , ooOOoOO000 + 'TUTS.png' , ooOOoOO000 + 'TUTS.png' , '' )
  if 13 - 13 : IIiIiII11i
  if 57 - 57 : iI1ii11iIi1i - ii
def O0O0O0OoO0o0OO ( ) :
 if 44 - 44 : O00o0O00 / I1ii11iIi11i + ooOOOoO % IIiIiII11i / oO0o + Ii
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Recent Episodes[/COLOR]' , '' , 10019 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Genres[/COLOR]' , '' , 10020 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Search[/COLOR]' , '' , 10021 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 if 20 - 20 : Ii1I
def IiIIi ( ) :
 if 26 - 26 : ooOoO0O00
 ooO0Oo = cloudflare . source ( I1Iii1III ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi11ii = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 , i11i1IIi in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 + '  -  ' + ( i11i1IIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i11iii1II1I1 , 10023 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
  if 35 - 35 : oOo0O0Ooo
  if 80 - 80 : oO0oo0o % oO0oo0o % o0o00Oo0O - Ii . Ii1IIIi1 / o0o00Oo0O
  if 13 - 13 : oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / iI1ii11iIi1i . ooOoO0O00
def Oo0o0O0OO0 ( ) :
 if 7 - 7 : Ii1I / IIiIiII11i - I11O0O0oOO00O00o + ooOoO0O00 + iI1ii11iIi1i
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Action[/COLOR]' , 'Aksiyon' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Adventure[/COLOR]' , 'Macera' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Animation[/COLOR]' , 'Animasyon' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Anime[/COLOR]' , 'Anime' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Biography[/COLOR]' , 'Biyografi' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Comedy[/COLOR]' , 'Komedi' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Drama[/COLOR]' , 'Dram' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Family[/COLOR]' , 'Aile' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']History[/COLOR]' , 'Tarih' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Horror[/COLOR]' , 'Korku' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Mystery[/COLOR]' , 'Gizem' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Romance[/COLOR]' , 'Romantik' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Sport[/COLOR]' , 'Spor' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Western[/COLOR]' , 'Tarih' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
 if 7 - 7 : O0OOOoOoo0 + iI1ii11iIi1i
def O0OoooO ( url ) :
 ii1iIii = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 o0000o0OOOo = cloudflare . source ( ii1iIii )
 IIi11ii = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 10022 , ooOOoOO000 + 'dtv.png' , o00O0oOOo , '' )
  if 86 - 86 : ooOoO0O00 / iI1ii11iIi1i * oOo0O0Ooo
  if 67 - 67 : Ii1I * Ii1I / oO0oo0o * ii + OOooOOo
  if 79 - 79 : ooOoO0O00
  if 1 - 1 : oO0oo0o / ooOoO0O00
def iii1Io0OOOooo ( ) :
 if 37 - 37 : Ii
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 i11iii1II1I1 = ( I1Iii1III ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( ii1I1IIi ) . replace ( ' ' , '+' )
 o0000o0OOOo = cloudflare . source ( i11iii1II1I1 )
 IIi11ii = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if ii1I1IIi in I111iIii1i1 . lower ( ) :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 10022 , ooOOoOO000 + 'dtv.png' )
   if 12 - 12 : Ii1I / iI1ii11iIi1i
   if 5 - 5 : ii
   if 18 - 18 : oOo0O0Ooo % ii - Ii1IIIi1 . Ii * I1ii11iIi11i % iI1ii11iIi1i
def IiIIiIiI1ii ( url ) :
 o0000o0OOOo = cloudflare . source ( url )
 IIi11ii = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for II1OoOOoOOOoooO0 , I1ii1iiii , IIIII1iiI , I111iIii1i1 in IIi11ii :
  iIiiI11iI111 = ( IIIII1iiI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIioOO00oOO0o = ( I1ii1iiii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOoOOO0O0O = 'Season ' + IIioOO00oOO0o + 'Episode ' + iIiiI11iI111 + I111iIii1i1
  OOooOOO ( oOoOOO0O0O , II1OoOOoOOOoooO0 )
  if 28 - 28 : O0OOOoOoo0 * I11O0O0oOO00O00o % Ii * Ii1IIIi1 / iI1ii11iIi1i
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 41 - 41 : O00o0O00 - I11i + iI1ii11iIi1i
  if 15 - 15 : I11O0O0oOO00O00o / I11i + iI1ii11iIi1i
def OOooOOO ( name , url ) :
 II1OoOOoOOOoooO0 = url
 IiIii1iII = name
 iiiiiI1iii11 = cloudflare . source ( II1OoOOoOOOoooO0 )
 OOOO0oO0OOo0o = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iiiiiI1iii11 )
 for I11III111i1I , O0o0Oo00O000O in OOOO0oO0OOo0o :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + IiIii1iII + O0o0Oo00O000O + '[/COLOR]' , I11III111i1I , 10012 , ooOOoOO000 + 'dtv.png' )
  if 84 - 84 : O00o0O00 + iI1ii11iIi1i + I11i
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33 : iI1ii11iIi1i
 if 93 - 93 : O0OOOoOoo0
def I11I1i1I ( ) :
 if 57 - 57 : o0o00Oo0O * Ii1I . Ii
 if 69 - 69 : o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66 : o0o00Oo0O
 if 52 - 52 : oO0o * ii
 if 12 - 12 : o0o00Oo0O + ooOOOoO * ooOoO0O00 . oO0o
 if 71 - 71 : ii1ii11IIIiiI - I11i - O00o0O00
 if 28 - 28 : iI11I1II1I1I
 if 7 - 7 : I11i % ooOOOoO * OOooOOo
 if 58 - 58 : ooOOOoO / I11O0O0oOO00O00o + IIiIiII11i % Ii1IIIi1 - ii
 if 25 - 25 : OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * oO0oo0o
 if 30 - 30 : I11O0O0oOO00O00o % OOooOOo / Ii1I * o0o00Oo0O * iI1ii11iIi1i . oOo0O0Ooo
 if 46 - 46 : OOooOOo - o0o00Oo0O
 if 70 - 70 : I11O0O0oOO00O00o + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * I11O0O0oOO00O00o
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Search Program[/COLOR]' , '' , 10043 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 if 49 - 49 : I11i
 if 25 - 25 : Ii1IIIi1 . ii * iI11I1II1I1I . I11i / o0o00Oo0O + iI1ii11iIi1i
def i11IIiIi ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Oo0oiiiii11i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( o0000o0OOOo )
 IIi11ii = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Oo0oiiiii11i ) )
 for url , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
  if 84 - 84 : I11O0O0oOO00O00o - I1ii11iIi11i * o0o00Oo0O / iI1ii11iIi1i . iI1ii11iIi1i
def oOI11Ii1 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
  if 34 - 34 : ooOoO0O00 % ooOOOoO
def iII111Ii ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  if 'episode' in url :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
  else :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 for url in OOOO0oO0OOo0o :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , ooOOoOO000 + 'Next.png' , '' , '' )
  if 33 - 33 : ooOoO0O00 / ii1ii11IIIiiI - ooOoO0O00 . I1ii11iIi11i
  if 18 - 18 : I1ii11iIi11i / o0o00Oo0O + Ii1IIIi1
def O00Oo0O ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIII1Ii1II1 = 'http://www.watchseries.ac/search/' + ii1I1IIi . replace ( ' ' , '%20' )
 o0000o0OOOo = II1I1i ( IIII1Ii1II1 )
 IIi11ii = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'watch online' in I111iIii1i1 :
   pass
  else :
   print i11iii1II1I1
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.watchseries.ac' + i11iii1II1I1 , 10044 , IiiIiII1Ii1 , '' , '' )
   if 24 - 24 : oOo0O0Ooo * iI1ii11iIi1i % o0o00Oo0O - I1ii11iIi11i
   xbmcplugin . setContent ( iI1i1i1i1i , 'movies' )
   if 30 - 30 : ooOoO0O00
def IiiIiIiIIIii1 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , url , I111iIii1i1 , IIIII1iiI , iIi11OoO0OOOo0Oo in IIi11ii :
  OOOo0oOOO = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IIIII1iiI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + OOOo0oOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IiiIiII1Ii1 , '' , iIi11OoO0OOOo0Oo )
  if 33 - 33 : ooOOOoO . ii . oO0oo0o
def O0oOO0O000O0 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  OOOo0oOOO = ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + OOOo0oOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 for url in OOOO0oO0OOo0o :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , ooOOoOO000 + 'Next.png' , '' , '' )
  if 94 - 94 : I11O0O0oOO00O00o . oOo0O0Ooo
def i11I1IIII ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , IiiIiII1Ii1 , '' , '' )
 for url in OOOO0oO0OOo0o :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , ooOOoOO000 + 'Next.png' , '' , '' )
  if 2 - 2 : iI1ii11iIi1i * Ii1I * ii
def O0ooOOo0 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( o0000o0OOOo )
 Oo0oiiiii11i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for I1ii1iiii , oooO000oO0O in Oo0oiiiii11i :
  IIi11ii = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( oooO000oO0O ) )
  for url , I111iIii1i1 in IIi11ii :
   OOOo0oOOO = ( I1ii1iiii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + OOOo0oOOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 OOOO0oO0OOo0o = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , url in IIi11ii :
  Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , ooOOoOO000 + 'WATCHSERIES.png' , '' , '' )
 for url in OOOO0oO0OOo0o :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , ooOOoOO000 + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16 : I11i . I11O0O0oOO00O00o
class ii1iiiI ( ) :
 if 26 - 26 : I11i % O00o0O00 + O00o0O00 % I11O0O0oOO00O00o * Ii / Ii1IIIi1
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 64 - 64 : oO0oo0o % OOooOOo / IIiIiII11i % O0OOOoOoo0 - Ii1IIIi1
  OOOo0oOOO = name
  self . Get_Sources ( i11iii1II1I1 , OOOo0oOOO )
  if 2 - 2 : ii1ii11IIIiiI - Ii1I + I11i * oO0o / Ii1IIIi1
  if 26 - 26 : O00o0O00 * I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  iII1I1iIi1i = xbmcgui . DialogProgress ( )
  o0000o0OOOo = II1I1i ( URL )
  IIi11ii = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( o0000o0OOOo )
  for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
   URL = 'http://www.watchseries.ac/link/' + i11iii1II1I1
   self . Get_site_link ( URL , season_name )
   if 31 - 31 : I11O0O0oOO00O00o * oO0oo0o . iI1ii11iIi1i
 def Get_site_link ( self , url , season_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( o0000o0OOOo )
  OOOO0oO0OOo0o = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( o0000o0OOOo )
  IIIii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( o0000o0OOOo )
  for url in IIi11ii :
   self . main ( url , season_name )
  for url in OOOO0oO0OOo0o :
   self . main ( url , season_name )
  for url in IIIii :
   self . main ( url , season_name )
   if 35 - 35 : I11O0O0oOO00O00o
 def main ( self , url , season_name ) :
  iII1I1iIi1i . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   i1iII1 = 'DACLIPS'
   if i1iII1 in ii1iiiI . source_list :
    pass
   else :
    self . daclips ( url , season_name , i1iII1 )
    iII1I1iIi1i . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    i1iII1 = 'FILEHOOT'
    if i1iII1 in ii1iiiI . source_list :
     pass
    else :
     iII1I1iIi1i . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , i1iII1 )
   else :
    if 'thevideo.me' in url :
     i1iII1 = 'THEVIDEO'
     if i1iII1 in ii1iiiI . source_list :
      pass
     else :
      self . thevideo ( url , season_name , i1iII1 )
      iII1I1iIi1i . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      i1iII1 = 'ALLMYVIDEOS'
      if i1iII1 in ii1iiiI . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , i1iII1 )
       iII1I1iIi1i . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       i1iII1 = 'VIDSPOT'
       if i1iII1 in ii1iiiI . source_list :
        pass
       else :
        self . vidspot ( url , season_name , i1iII1 )
        iII1I1iIi1i . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        i1iII1 = 'VODLOCKER'
        if i1iII1 in ii1iiiI . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , i1iII1 )
         iII1I1iIi1i . update ( 0 , "" , "Getting Vodlocker Links" )
         if 70 - 70 : I11O0O0oOO00O00o - I1ii11iIi11i / ii % ii
         if 95 - 95 : ii % ii . iI1ii11iIi1i
 def allmyvid ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
  for oOoo0o00O , I111iIii1i1 in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 38 - 38 : Ii1I + OOooOOo
 def vidspot ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( o0000o0OOOo )
  for oOoo0o00O , I111iIii1i1 in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 68 - 68 : o0o00Oo0O
 def thevideo ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( o0000o0OOOo )
  for oOoo0o00O in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 76 - 76 : Ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( o0000o0OOOo )
  for oOoo0o00O in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 99 - 99 : I11i
 def daclips ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( o0000o0OOOo )
  for oOoo0o00O in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 1 - 1 : iI1ii11iIi1i * OOooOOo * oO0o + I1ii11iIi11i
 def filehoot ( self , url , season_name , source_name ) :
  o0000o0OOOo = II1I1i ( url )
  IIi11ii = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( o0000o0OOOo )
  for oOoo0o00O in IIi11ii :
   self . Printer ( oOoo0o00O , season_name , source_name )
   if 90 - 90 : ii1ii11IIIiiI % I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / O00o0O00 + I11O0O0oOO00O00o
 def Printer ( self , Link , season_name , source_name ) :
  if 89 - 89 : oO0oo0o
  if Link in ii1iiiI . List :
   pass
  elif source_name in ii1iiiI . source_list :
   pass
  else :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + source_name + '[/COLOR]' , Link , 10012 , ooOOoOO000 + 'WATCHSERIES.png' )
   iII1I1iIi1i . update ( 100 , "" , "Got Source" )
   ii1iiiI . List . append ( Link )
   ii1iiiI . source_list . append ( source_name )
   if 87 - 87 : Ii1IIIi1 % I1ii11iIi11i
   xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 62 - 62 : oO0o + O0OOOoOoo0 / Ii1IIIi1 * Ii
   if 37 - 37 : Ii1IIIi1
   if 33 - 33 : oO0o - o0o00Oo0O - oO0o
   if 94 - 94 : ooOOOoO * I11O0O0oOO00O00o * ii / I11i . ooOOOoO - I11i
   if 13 - 13 : O00o0O00 / ooOOOoO - oO0o / O00o0O00 . ooOoO0O00
def I1Ii1 ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Highlights[/COLOR]' , '' , 10008 , ooOOoOO000 + 'Highlights.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Fixtures[/COLOR]' , '' , 10009 , ooOOoOO000 + 'Fixtures.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Live Sport On G-Tv[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , ooOOoOO000 + 'Sport.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , ooOOoOO000 + 'PremiereLeague.png' , o00O0oOOo , '' )
 if 26 - 26 : iI11I1II1I1I * I11i . I11O0O0oOO00O00o
def O000ooo ( url ) :
 Ooooo0Oo0oOo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( ooO0Oo )
 for iI1I1I1 , url , IIiI11iiIi , OO0ooo00o , II1iIiiI , iIi1IIIi1Ii , ii1IOO00OOOO00oOO , O00o0 , ooO0o0o , O0o0ooO0oO0oO , iI1iII111ii1I in IIi11ii :
  IIiI11iiIi = IIiI11iiIi
  if 'Arsenal' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'arsenal-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                                  ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Bournemouth' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'afc-bournemouth.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                       ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Burnley' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'KEGnQWW.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                                   ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Chelsea' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'chelsea.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                                  ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Crystal' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'CrystalPalace.0.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                       ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Everton' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'Everton.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                                   ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Hull' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'hull-city-afc.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                                 ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Leicester' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'leicester-city-fc-hd-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                       ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Liverpool' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'liverpool-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                               ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Manchester City' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'city-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '               ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Manchester United' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + '91.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '          ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Middlesbrough' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'middlesbrough-fc-hd-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                 ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Southampton' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'southampton-fc-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                   ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Stoke City' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'stoke-city.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                          ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Sunderland' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'sunderland-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                        ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Swansea' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'swansea-city-afc.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                    ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Tottenham' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'tottenham-hotspur_zps4e3ed7c1.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '        ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Watford' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'watford-fc-hd-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '                              ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'Bromwich' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'west-bromwich-albion-logo.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '   ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  elif 'West Ham' in IIiI11iiIi :
   OOoi1I1I = ooOOoOO000 + 'west-ham.png'
   I111iIii1i1 = '[COLOR' + iiiI1iiI11iii + ']' + iI1I1I1 + ' - ' + IIiI11iiIi + '             ' + OO0ooo00o + '        ' + II1iIiiI + '        ' + iIi1IIIi1Ii + '        ' + ii1IOO00OOOO00oOO + '        ' + O00o0 + '        ' + ooO0o0o + '        ' + O0o0ooO0oO0oO + '[/COLOR]'
  Ooooo0Oo0oOo ( str ( I111iIii1i1 ) , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , OOoi1I1I , OOoi1I1I , IIiI11iiIi )
  if 14 - 14 : Ii1IIIi1 - I11O0O0oOO00O00o * ii + O00o0O00 . IIiIiII11i
def OOO0o0OO ( description ) :
 IIiI11iiIi = description
 i11iii1II1I1 = ( 'http://www.fullmatchesandshows.com/?s=' + IIiI11iiIi ) . replace ( ' ' , '%20' )
 II1i111i11i1i ( i11iii1II1I1 )
 if 96 - 96 : O00o0O00 + O00o0O00 % ooOOOoO % O00o0O00
def OOo0o ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi11ii = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , I1Iii1III ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i11iii1II1I1 , 10010 , I1Iii1III ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiiIiII1Ii1 , o00O0oOOo , '' )
  if 3 - 3 : IIiIiII11i - iI1ii11iIi1i % OOooOOo / oO0oo0o
def iII1 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Oo0oiiiii11i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( o0000o0OOOo )
 for Oo0oiiiii11i in Oo0oiiiii11i :
  IiIiIiiii = re . compile ( '(.*?)</h2>' ) . findall ( str ( Oo0oiiiii11i ) )
  for oOO0o in IiIiIiiii :
   oOO0o = oOO0o
  OOOi1I1IIII = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Oo0oiiiii11i ) )
  for iI11iii111 , IiiIiII1Ii1 , time , IIi1i1111i in OOOi1I1IIII :
   Ooo0o0ooO0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IIi1i1111i )
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + oOO0o + ' - ' + iI11iii111 + ' - ' + time + '[/COLOR]' , '' , 10010 , I1Iii1III ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IiiIiII1Ii1 , o00O0oOOo , ( str ( Ooo0o0ooO0 ) ) )
   if 96 - 96 : I1ii11iIi11i / oO0oo0o . IIiIiII11i . I1ii11iIi11i
 iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if 91 - 91 : IIiIiII11i . O00o0O00 + I11i
def o0ooiiII ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , ooOOoOO000 + 'fanart.jpg' , '' )
 if 8 - 8 : iI11I1II1I1I
def oo0ooo0OOO ( url ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Live On G-Tv[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , ooOOoOO000 + 'TodaysMacthes.png' , o00O0oOOo , '' )
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , url , I111iIii1i1 in IIi11ii :
  iiiiiIIii11I = I111iIii1i1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I111iIii1i1 :
   pass
  else :
   iiiiiIIii11I = I111iIii1i1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + iiiiiIIii11I + '[/COLOR]' , url , 10013 , IiiIiII1Ii1 )
 for url , IiiIiII1Ii1 , I111iIii1i1 in OOOO0oO0OOo0o :
  iiiiiIIii11I = I111iIii1i1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I111iIii1i1 :
   pass
  else :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + iiiiiIIii11I + '[/COLOR]' , url , 10013 , IiiIiII1Ii1 )
def II1i111i11i1i ( url ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Live On G-Tv[/COLOR]' , ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , ooOOoOO000 + 'TodaysMacthes.png' , o00O0oOOo , '' )
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 if 95 - 95 : I11O0O0oOO00O00o + I11i * Ii1I
 if 85 - 85 : Ii . ii - iI11I1II1I1I
 if 38 - 38 : I11O0O0oOO00O00o . I11O0O0oOO00O00o * oO0oo0o / ii % O0OOOoOoo0
 if 80 - 80 : oO0o / ooOOOoO * oOo0O0Ooo % ooOOOoO
 if 95 - 95 : o0o00Oo0O / I11O0O0oOO00O00o . ii1ii11IIIiiI
 if 17 - 17 : I11O0O0oOO00O00o
 if 56 - 56 : O0OOOoOoo0 * I11i + I11O0O0oOO00O00o
 for url , IiiIiII1Ii1 , I111iIii1i1 in OOOO0oO0OOo0o :
  iiiiiIIii11I = I111iIii1i1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I111iIii1i1 :
   pass
  else :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + iiiiiIIii11I + '[/COLOR]' , url , 10013 , IiiIiII1Ii1 )
   if 48 - 48 : ooOOOoO * oO0o % ii1ii11IIIiiI - I11O0O0oOO00O00o
def I1iiiiii ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( o0000o0OOOo )
 for I11III111i1I in IIi11ii :
  i1i1iIi1I = ( I11III111i1I ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  IIIIi1I ( 'http:' + i1i1iIi1I )
  if 38 - 38 : ii1ii11IIIiiI
  if 25 - 25 : iI11I1II1I1I % IIiIiII11i / I11O0O0oOO00O00o / Ii1I
  if 22 - 22 : oO0oo0o * Ii1IIIi1
  if 4 - 4 : OOooOOo - oO0oo0o + oOo0O0Ooo
def iIiII ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  OoO00O ( I111iIii1i1 , url , 8046 , IiiIiII1Ii1 )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , ooOOoOO000 + 'Next.png' )
def IIi1i1i1iii ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  IIIIi1I ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 44 - 44 : I1ii11iIi11i . I1ii11iIi11i + ii * Ii / I11O0O0oOO00O00o + ii1ii11IIIiiI
def III11ii ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( ooO0Oo )
 for url in IIi11ii :
  yt . PlayVideo ( url )
  if 33 - 33 : I11i * Ii1IIIi1 * iI11I1II1I1I + Ii . ii
def oo0oOooo0O ( ) :
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , ooOOoOO000 + 'documentary.png' )
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , ooOOoOO000 + 'documentary.png' )
 i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']Search Docs[/COLOR]' , '' , 80012 , ooOOoOO000 + 'Search.png' )
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 8041 , ooOOoOO000 + 'documentary.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1i1ii ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( 'NEXT PAGE' , url , 8041 , ooOOoOO000 + 'Next.png' )
  if 100 - 100 : ooOoO0O00 - Ii . ii1ii11IIIiiI * oO0o
  if 62 - 62 : o0o00Oo0O
def ii1iIiIIiIIii ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']YouTube[/COLOR]' , url , 8043 , ooOOoOO000 + 'documentary.png' )
  else :
   ooooo ( 'http:' + url )
   if 22 - 22 : iI11I1II1I1I * ii1ii11IIIiiI / I1ii11iIi11i
def ooooo ( url ) :
 OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']Pick Quality[/COLOR]' ) . replace ( '&#039;s' , '' ) , '' , 222 , ooOOoOO000 + 'documentary.png' )
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  url = ( url ) . replace ( '\/' , '/' )
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 222 , ooOOoOO000 + 'documentary.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31 : Ii
def i1i1i1IiiiIi1 ( ) :
 ooO0Oo = oO0ooo000 ( 'http://documentarylovers.com/' )
 IIi11ii = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  if 'genre' in i11iii1II1I1 :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , i11iii1II1I1 , 80010 , ooOOoOO000 + 'documentary.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo00OO ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( 'NEXT PAGE' , url , 80010 , ooOOoOO000 + 'Next.png' )
  if 73 - 73 : I11O0O0oOO00O00o / ii . IIiIiII11i - ooOOOoO * O0OOOoOoo0 * ooOOOoO
def iI1iIIIiIi ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']YouTube[/COLOR]' , url , 8043 , ooOOoOO000 + 'documentary.png' )
 for url in OOOO0oO0OOo0o :
  ooooo ( url )
  if 70 - 70 : O00o0O00 + O0OOOoOoo0 * iI1ii11iIi1i . iI1ii11iIi1i + oO0o
def IiI1IioOo00OOOoo0 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0OOo = 'http://documentarylovers.com/?s=' + ( ii1I1IIi ) . replace ( ' ' , '+' )
 OooOooO0OoOoo0o = o00oOO0OOo . lower ( )
 ooo00OO ( OooOooO0OoOoo0o )
 if 18 - 18 : ooOoO0O00
def i1i1111I11II ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if 'films' in url :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , ooOOoOO000 + 'documentary.png' )
def O00O00 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , url , I111iIii1i1 in IIi11ii :
  if 'films' in url :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + IiiIiII1Ii1 )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( 'NEXT' , url , 8049 , ooOOoOO000 + 'Next.png' )
def i1I1iiIiII11 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  if 'rtd' in url :
   Oo0oO0o0OOo ( url )
   if 24 - 24 : ii1ii11IIIiiI + ii . ooOOOoO / OOooOOo / I11O0O0oOO00O00o
def Oo0oO0o0OOo ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( ooO0Oo )
 for I1iIIiI1i , file in IIi11ii :
  url = ( 'https://rtd.rt.com' + I1iIIiI1i + file )
  IIIIi1I ( url )
  if 65 - 65 : ii
  if 18 - 18 : o0o00Oo0O - ooOoO0O00 . ii1ii11IIIiiI
def I111ii11I ( ) :
 o0000o0OOOo = oO0ooo000 ( 'http://www.stream2watch.co/live-tv' )
 IIi11ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 , IiIii1II in IIi11ii :
  i11i1i1i ( ( I111iIii1i1 + '[COLOR' + iiiI1iiI11iii + ']' + IiIii1II + '[/COLOR]' ) , i11iii1II1I1 , 8086 , IiiIiII1Ii1 )
  if 70 - 70 : Ii1IIIi1 . IIiIiII11i . Ii1IIIi1 - iI11I1II1I1I
def iiiIIII1Ii1 ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 8087 , IiiIiII1Ii1 )
  if 83 - 83 : ii
def o0Oo00OoO000O ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 in IIi11ii :
  II1iii ( url , I111iIii1i1 )
  if 15 - 15 : I1ii11iIi11i / iI1ii11iIi1i % o0o00Oo0O + Ii1I
def II1iii ( url , name ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  print url
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 96 - 96 : O0OOOoOoo0 . ii
def O0oOOOO0o ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi11ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + i11iii1II1I1 , 3002 , 'http://www.solie.org/alibrary/' + IiiIiII1Ii1 )
def OoOOO0 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiiIiII1Ii1 )
def IiIio0oO0O ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 IiiiiII1Ii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( ooO0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , ooOOoOO000 + 'classicmovies.png' )
 for url , I111iIii1i1 in IiiiiII1Ii1 :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']Season- ' + I111iIii1i1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOOoOO000 + 'classicmovies.png' )
 for url in next :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , ooOOoOO000 + 'Next.png' )
 for url , IiiIiII1Ii1 , I111iIii1i1 in OOOO0oO0OOo0o :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiiIiII1Ii1 )
def oOo00OoooOoo ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  II1ii1i1i ( url )
def II1ii1i1i ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  IIIIi1I ( url )
  if 30 - 30 : iI1ii11iIi1i + IIiIiII11i % ii
def O0OOo00Ooo00 ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i11iii1II1I1 , 8065 , ooOOoOO000 + 'classicmovies.png' )
def IiiiiiiiI1i11 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( "v.src = '([^']*)';" ) . findall ( ooO0Oo )
 for url in IIi11ii :
  Ii11 ( url )
  if 32 - 32 : ii % oO0oo0o % iI11I1II1I1I / o0o00Oo0O
def Ii1i1i ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , i11iii1II1I1 , 8065 , ooOOoOO000 + 'classictv.png' )
def i1IIi ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  if 'mp4' in url :
   IIIIi1I ( url )
 for url in OOOO0oO0OOo0o :
  yt . PlayVideo ( url )
  if 57 - 57 : oOo0O0Ooo . Ii * IIiIiII11i + ii + iI1ii11iIi1i
def O0Ooo ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi11ii = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + i11iii1II1I1 , 8071 , ooOOoOO000 + 'streams.png' )
def OoO00OOOoOOo ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000o0OOOo )
 for I111iIii1i1 , url in IIi11ii :
  if '(Free Access)' in I111iIii1i1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( I1Iii1III ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO00OOo + '/' + IiI11i1IiI1 + url ) . strip ( )
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , ooOOoOO000 + 'streams.png' )
def oOOo0oOoooO0o ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , I111iIii1i1 , url in IIi11ii :
  url = ( ( I1Iii1III ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO00OOo + '/' + IiI11i1IiI1 + url ) . strip ( )
  iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IiiIiII1Ii1 , i1I , '' )
  if 15 - 15 : O0OOOoOoo0 - o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / o0o00Oo0O
def IiIIooOoo0 ( ) :
 iii1I1 ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
 iii1I1 ( 'Genres' , 'http://www.xvideos.com' , 10106 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
 iii1I1 ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
 iii1I1 ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
 iii1I1 ( 'Search' , '' , 10107 , ooOOoOO000 + 'Jizbox.png' , '' , '' , )
 if 85 - 85 : O00o0O00 + IIiIiII11i - O00o0O00 * oO0oo0o - ooOoO0O00 % Ii1IIIi1
def iii1II1iI1III ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Ooo00OO00oOO0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( o0000o0OOOo )
 for url in Ooo00OO00oOO0 :
  iii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
 IIi11ii = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiII11iI in IIi11ii :
  iii1I1 ( ( I111iIii1i1 + ' - No of Videos : ' + ( IiII11iI ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
  if 93 - 93 : oOo0O0Ooo / O0OOOoOoo0 / I11O0O0oOO00O00o + IIiIiII11i + Ii
def oooO0OOo0 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Ooo00OO00oOO0 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( o0000o0OOOo )
 for url in Ooo00OO00oOO0 :
  iii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , ooOOoOO000 + 'Next.png' , '' , '' )
 IIi11ii = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , url , I111iIii1i1 , ooo0OO0o00 in IIi11ii :
  iii1I1 ( I111iIii1i1 + '--' + ooo0OO0o00 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IiiIiII1Ii1 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 6 - 6 : O00o0O00 * oO0oo0o / o0o00Oo0O . IIiIiII11i + ooOOOoO % I11i
  if 67 - 67 : o0o00Oo0O % ii1ii11IIIiiI
def I1oo0O0Ooo0O00 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , url , I111iIii1i1 , oO00oOoo0ooO0 , III111iiiIi in IIi11ii :
  iii1I1 ( I111iIii1i1 + ' - Porn Quality : ' + III111iiiIi + ' - ' + oO00oOoo0ooO0 , 'http://www.xvideos.com' + url , 10108 , IiiIiII1Ii1 , IiiIiII1Ii1 , III111iiiIi + ' - ' + oO00oOoo0ooO0 )
 o0ooOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o0000o0OOOo )
 for url in o0ooOo :
  iii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , ooOOoOO000 + 'Next.png' , '' , '' )
  if 15 - 15 : O0OOOoOoo0 . I11i + OOooOOo . iI11I1II1I1I % O0OOOoOoo0 + o0o00Oo0O
def oO0OOOOo ( url ) :
 o0000o0OOOo = II1I1i ( url )
 Oo0oiiiii11i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 Ooo00OO00oOO0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( o0000o0OOOo )
 for url in Ooo00OO00oOO0 :
  iii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , ooOOoOO000 + 'Next.png' , '' , '' )
 IIi11ii = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Oo0oiiiii11i ) )
 for url , I111iIii1i1 in IIi11ii :
  iii1I1 ( I111iIii1i1 , 'http://www.xvideos.com' + url , 10105 , ooOOoOO000 + 'Jizbox.png' , '' , '' )
  if 58 - 58 : Ii1IIIi1
  if 2 - 2 : ooOOOoO - oO0oo0o % oO0o + I11i + iI1ii11iIi1i - iI11I1II1I1I
def iiIiI111Ii1 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00oOO0o0oO0O = ( ii1I1IIi ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OooOooO0OoOoo0o = o00oOO0o0oO0O . lower ( )
 IiiIoOOoO0 = 'http://www.xvideos.com/?k=' + OooOooO0OoOoo0o
 print IiiIoOOoO0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o0000o0OOOo = II1I1i ( IiiIoOOoO0 )
 IIi11ii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 , oO00oOoo0ooO0 , III111iiiIi in IIi11ii :
  iii1I1 ( I111iIii1i1 + ' - Porn Quality : ' + III111iiiIi + ' - ' + oO00oOoo0ooO0 , 'http://www.xvideos.com' + i11iii1II1I1 , 10108 , IiiIiII1Ii1 , IiiIiII1Ii1 , III111iiiIi + ' - ' + oO00oOoo0ooO0 )
 o0ooOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 in o0ooOo :
  iii1I1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + i11iii1II1I1 , 10105 , ooOOoOO000 + 'Next.png' , '' , '' )
  if 11 - 11 : oO0o - iI1ii11iIi1i + o0o00Oo0O * oO0o
def IIiiI1iiI ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( o0000o0OOOo )
 OOOO0oO0OOo0o = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( o0000o0OOOo )
 IIIii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  if 'http' in url :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']LOW[/COLOR]' , url , 222 , ooOOoOO000 + 'Jizbox.png' )
 for url in OOOO0oO0OOo0o :
  if 'http' in url :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']HIGH[/COLOR]' , url , 222 , ooOOoOO000 + 'Jizbox.png' )
 for url in IIIii :
  if 'http' in url :
   OoO00O ( '[COLOR' + iiiI1iiI11iii + ']HLS[/COLOR]' , url , 222 , ooOOoOO000 + 'Jizbox.png' )
   if 20 - 20 : O0OOOoOoo0 . oO0o * Ii1IIIi1
def OoO0o ( url ) :
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 import urlresolver
 try : II111iii . play ( url )
 except : pass
 if 65 - 65 : Ii1I % oO0oo0o . ii * I11i * oO0o
 if 10 - 10 : oO0oo0o - Ii1IIIi1 % IIiIiII11i - ii1ii11IIIiiI - ooOoO0O00
def OooO0O0o0 ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 8091 , ooOOoOO000 + 'gofish.png' )
def IiiOo0o0Oo0O0 ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 1092 , IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']NEXT[/COLOR]' , url , 8091 , ooOOoOO000 + 'Next.png' )
def Oo0OoO00O ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o0000o0OOOo )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 8092 , IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']NEXT[/COLOR]' , url , 8091 , ooOOoOO000 + 'Next.png' )
def IIiIIiiiiI ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( "videoId: '([^']*)'," ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  yt . PlayVideo ( url )
  if 32 - 32 : ii % ii . oO0oo0o - O0OOOoOoo0 . OOooOOo * oO0oo0o
  if 55 - 55 : I11O0O0oOO00O00o
  if 93 - 93 : Ii . I11i
I1iiIi = '{PQ},' ; IIoooO = '{SC},' ; I1ii1I1i1 = '{XG},' ; i11iii = '{JP},' ; oO0OoOoo00 = '{HW},' ; IIiiIi1i = '{RT},'
def IiiiiI1iIi ( ) :
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 II11IIiii = ( I1Iii1III ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 i11iii1II1I1 = ( I1Iii1III ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 29 - 29 : ooOOOoO + Ii * o0o00Oo0O - Ii1IIIi1 . IIiIiII11i % iI1ii11iIi1i
 II11i1 = ( I1Iii1III ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iII11 = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 iIIIooOo = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 IIi11iiI1 = ( I1Iii1III ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiIIIIiIi = ( I1Iii1III ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ii1I1IIi
 oo0IIII1 = ( I1Iii1III ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 II1ii111 = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 iII1Iiii11I1i = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II11 = ( I1Iii1III ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 51 - 51 : I1ii11iIi11i / ooOOOoO * iI1ii11iIi1i - IIiIiII11i / oOo0O0Ooo . ooOOOoO
 iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0000o0OOOo = oo00oO0o000 ( i11iii1II1I1 )
 iII1I1iIi1i . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 65 - 65 : ooOOOoO
 if 75 - 75 : ii * Ii
 IIIi11iiIIi = oo00oO0o000 ( II11i1 )
 iII1I1iIi1i . update ( 28 , "" , "Checking Source 3/9 Links" )
 oOo000O00O = oo00oO0o000 ( iII11 )
 iII1I1iIi1i . update ( 40 , "" , "Checking Source 4/9 Links" )
 OOOooO0 = oo00oO0o000 ( iIIIooOo )
 iII1I1iIi1i . update ( 52 , "" , "Checking Source 5/9 Links" )
 iii1iIIi1ii = oo00oO0o000 ( IiIIIIiIi )
 iII1I1iIi1i . update ( 64 , "" , "Checking Source 6/9 Links" )
 iI1iIII = oo00oO0o000 ( oo0IIII1 )
 iII1I1iIi1i . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIIIiIiII1iiiii = oo00oO0o000 ( II1ii111 )
 iII1I1iIi1i . update ( 88 , "" , "Checking Source 8/9 Links" )
 II1II1i = oo00oO0o000 ( iII1Iiii11I1i )
 iII1I1iIi1i . update ( 100 , "" , "Checking Source 9/9 Links" )
 IiIIooO00oOo0 = oo00oO0o000 ( II11 )
 if 97 - 97 : ooOoO0O00 + Ii1IIIi1 . O0OOOoOoo0 - Ii1IIIi1
 if 53 - 53 : o0o00Oo0O . oOo0O0Ooo
 if o0000o0OOOo != 'Failed' :
  IIi11ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0000o0OOOo )
  for IIiIiii111iI , I111iIii1i1 in IIi11ii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i11iii1II1I1 + IIiIiii111iI ) , 222 , '' )
    iII1I1iIi1i . update ( 0 , "" , "Getting Source 1 Links" )
    if 86 - 86 : iI11I1II1I1I - I11O0O0oOO00O00o % O0OOOoOoo0 . O00o0O00 * OOooOOo . ooOoO0O00
    if 75 - 75 : I11O0O0oOO00O00o + O0OOOoOoo0 / O0OOOoOoo0 - O00o0O00 * oO0o * O0OOOoOoo0
    if 53 - 53 : ooOOOoO % I1ii11iIi11i
    if 42 - 42 : Ii / oOo0O0Ooo - oO0o - O0OOOoOoo0 + IIiIiII11i % O0OOOoOoo0
    if 50 - 50 : ii + oO0oo0o * oOo0O0Ooo - iI1ii11iIi1i / Ii
    if 5 - 5 : o0o00Oo0O - oOo0O0Ooo
    if 44 - 44 : IIiIiII11i . IIiIiII11i + O00o0O00 * iI1ii11iIi1i
 if IIIi11iiIIi != 'Failed' :
  IIIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIIi11iiIIi )
  for IIiIiii111iI , I111iIii1i1 in IIIii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II11i1 + IIiIiii111iI ) , 1006 , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 18 , "" , "Getting Source 3 Links" )
 if oOo000O00O != 'Failed' :
  i11I1I1iI11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo000O00O )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in i11I1I1iI11I :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Silent Hunter[/COLOR]' ) , i11iii1II1I1 , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 22 - 22 : Ii1IIIi1 + oO0o - O0OOOoOoo0
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOOooO0 != 'Failed' :
  O0O0oii1I11i = [ ]
  iIIIIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOooO0 )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in iIIIIi1 :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    if I111iIii1i1 in O0O0oii1I11i :
     pass
    else :
     Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , i11iii1II1I1 , 1016 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
     O0O0oii1I11i . append ( I111iIii1i1 )
     iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     iII1I1iIi1i . update ( 36 , "" , "Getting Scooby Links" )
     iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if iii1iIIi1ii != 'Failed' :
  iIIIiiI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iii1iIIi1ii )
  for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in iIIIiiI :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + i11iii1II1I1 , 7067 , IiiIiII1Ii1 )
    iII1I1iIi1i . update ( 45 , "" , "Getting Snag Links" )
    if 76 - 76 : ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if iI1iIII != 'Failed' :
  o0oOo0O0o0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIII )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in o0oOo0O0o0oO :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Redemption[/COLOR]' ) , i11iii1II1I1 , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 53 , "" , "Getting Redemption Links" )
    if 6 - 6 : oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + I11O0O0oOO00O00o . O00o0O00
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if iIIIiIiII1iiiii != 'Failed' :
  O00o000O0O0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIiIiII1iiiii )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in O00o000O0O0oO :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Reaper[/COLOR]' ) , i11iii1II1I1 , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 61 , "" , "Getting Reaper Links" )
    if 23 - 23 : oOo0O0Ooo * O0OOOoOoo0 / OOooOOo . iI11I1II1I1I % Ii
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if II1II1i != 'Failed' :
  iIiI111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1II1i )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in iIiI111ii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    iII111I ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Herovision[/COLOR]' ) , i11iii1II1I1 , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 70 , "" , "Getting Herovision Links" )
    if 84 - 84 : iI11I1II1I1I . O0OOOoOoo0 + Ii1IIIi1
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 85 - 85 : O00o0O00 % oO0oo0o * oO0oo0o + ii
 if IiIIooO00oOo0 != 'Failed' :
  IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IiIIooO00oOo0 )
  for i11iii1II1I1 , O0O00OOOo00O , I111iIii1i1 in IiI :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Silent Hunter[/COLOR]' ) , i11iii1II1I1 , 222 , O0O00OOOo00O )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 30 - 30 : OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 O000oOoOO0oO0ooOOOoO = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 46 - 46 : oOo0O0Ooo . ooOOOoO - Ii - ii1ii11IIIiiI
 for iIiIIii11iI in O000oOoOO0oO0ooOOOoO :
  ii1II1i1 = OoOoo + iIiIIii11iI + ooOo0Oo
  oOO0ooO000 = oo00oO0o000 ( ii1II1i1 )
  if oOO0ooO000 != 'Failed' :
   ooI11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO0ooO000 )
   for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in ooI11 :
    if ii1I1IIi in I111iIii1i1 . lower ( ) :
     iII111I ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + ' - Source Pandoras[/COLOR]' , i11iii1II1I1 , 222 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
     iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     iII1I1iIi1i . update ( 89 , "" , "Getting Pandoras Links" )
     if 38 - 38 : Ii1I - iI1ii11iIi1i * I11i
     iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
     if 13 - 13 : oOo0O0Ooo * oO0oo0o
 O000oOoOO0oO0ooOOOoO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 41 - 41 : ooOOOoO
 if 16 - 16 : iI11I1II1I1I
 for iIiIIii11iI in O000oOoOO0oO0ooOOOoO :
  ii1II1i1 = II11IIiii + iIiIIii11iI
  OOoOo0Oo = oo00oO0o000 ( ii1II1i1 )
  if OOoOo0Oo != 'Failed' :
   oOo0o0O = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OOoOo0Oo )
   for IIiIiii111iI , I111iIii1i1 in oOo0o0O :
    if ii1I1IIi in I111iIii1i1 . lower ( ) :
     OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( II11IIiii + iIiIIii11iI + IIiIiii111iI ) , 222 , '' )
     iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     iII1I1iIi1i . update ( 100 , "" , "Getting Source 5 Links" )
     if 26 - 26 : ooOoO0O00 / Ii1IIIi1 . Ii1IIIi1
     iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
     if 20 - 20 : O00o0O00 - Ii1IIIi1 / I1ii11iIi11i * oO0o
     if 55 - 55 : ii
def I1I1Ii111 ( ) :
 if 7 - 7 : o0o00Oo0O + iI1ii11iIi1i . IIiIiII11i
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 if 12 - 12 : oOo0O0Ooo - ooOoO0O00
 i11iii1II1I1 = ( I1Iii1III ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( ii1I1IIi ) . replace ( ' ' , '%20' )
 II1OoOOoOOOoooO0 = ( I1Iii1III ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 II11i1 = ( I1Iii1III ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 iII11 = ( I1Iii1III ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIIIooOo = ( I1Iii1III ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OooOooO0OoOoo0o ) . replace ( ' ' , '+' )
 IIi11iiI1 = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IiIIIIiIi = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 oo0IIII1 = ( I1Iii1III ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 95 - 95 : I11O0O0oOO00O00o / ooOOOoO . o0o00Oo0O * ooOOOoO - I11i * I1ii11iIi11i
 iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 6 - 6 : OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / iI1ii11iIi1i
 iII1I1iIi1i . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0000o0OOOo = oo00oO0o000 ( i11iii1II1I1 )
 iII1I1iIi1i . update ( 14 , "" , "Checking Source 2/9 Links" )
 iiiiiI1iii11 = oo00oO0o000 ( II1OoOOoOOOoooO0 )
 iII1I1iIi1i . update ( 28 , "" , "Checking Source 3/9 Links" )
 IIIi11iiIIi = oo00oO0o000 ( II11i1 )
 iII1I1iIi1i . update ( 40 , "" , "Checking Source 4/9 Links" )
 oOo000O00O = oo00oO0o000 ( iII11 )
 iII1I1iIi1i . update ( 52 , "" , "Checking Source 5/9 Links" )
 OOOooO0 = cloudflare . source ( iIIIooOo )
 iII1I1iIi1i . update ( 64 , "" , "Checking Source 6/9 Links" )
 OOoOo0Oo = oo00oO0o000 ( IIi11iiI1 )
 iII1I1iIi1i . update ( 76 , "" , "Checking Source 7/9 Links" )
 iii1iIIi1ii = oo00oO0o000 ( IiIIIIiIi )
 iII1I1iIi1i . update ( 88 , "" , "Checking Source 8/9 Links" )
 iI1iIII = oo00oO0o000 ( oo0IIII1 )
 iII1I1iIi1i . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 14 - 14 : ii1ii11IIIiiI % ooOOOoO - o0o00Oo0O / ii1ii11IIIiiI
 if iI1iIII != 'Failed' :
  o0oOo0O0o0oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIII )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in o0oOo0O0o0oO :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source HeroVision[/COLOR]' ) , i11iii1II1I1 , 1016 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 10 , "" , "Getting Herovision Links" )
    if 91 - 91 : Ii % ii1ii11IIIiiI * oO0oo0o - Ii1I . ii1ii11IIIiiI
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 28 - 28 : Ii
 if iii1iIIi1ii != 'Failed' :
  iIIIiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1iIIi1ii )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in iIIIiiI :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- source Reaper[/COLOR]' ) , i11iii1II1I1 , 1016 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 20 , "" , "Getting Reaper Links" )
    if 51 - 51 : oOo0O0Ooo + O0OOOoOoo0 * o0o00Oo0O . iI1ii11iIi1i
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 82 - 82 : O00o0O00 * Ii1I % iI1ii11iIi1i . O00o0O00
    if 43 - 43 : oO0o . O0OOOoOoo0 * I1ii11iIi11i
    if 20 - 20 : ooOoO0O00 . ooOoO0O00 - I11O0O0oOO00O00o
    if 89 - 89 : O0OOOoOoo0 - I11O0O0oOO00O00o . o0o00Oo0O % ii . Ii
    if 35 - 35 : IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
    if 55 - 55 : I1ii11iIi11i % ooOoO0O00 * I11O0O0oOO00O00o
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 30 , "" , "Getting CoolSeries Links" )
    if 95 - 95 : O00o0O00 / IIiIiII11i - I11i % ii1ii11IIIiiI . I11O0O0oOO00O00o
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0000o0OOOo != 'Failed' :
  IIi11ii = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( o0000o0OOOo )
  for IiiIiII1Ii1 , i11iii1II1I1 , I111iIii1i1 in IIi11ii :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + i11iii1II1I1 , 10044 , IiiIiII1Ii1 , '' , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 63 - 63 : iI11I1II1I1I / O0OOOoOoo0
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 24 - 24 : I1ii11iIi11i / iI11I1II1I1I % O00o0O00 * OOooOOo - iI11I1II1I1I
    if 50 - 50 : IIiIiII11i
    if 39 - 39 : IIiIiII11i . OOooOOo - I1ii11iIi11i * ooOoO0O00 . ii
    if 44 - 44 : oOo0O0Ooo
    if 55 - 55 : oO0oo0o . ii1ii11IIIiiI * ii1ii11IIIiiI
    if 82 - 82 : oOo0O0Ooo % oO0o % I11O0O0oOO00O00o + I11O0O0oOO00O00o
    if 6 - 6 : I1ii11iIi11i
    if 73 - 73 : ii1ii11IIIiiI * Ii1I + I11i - I1ii11iIi11i . I11O0O0oOO00O00o
    if 93 - 93 : Ii
    if 80 - 80 : ooOoO0O00 . oOo0O0Ooo - oO0oo0o + O00o0O00 + Ii1IIIi1 % oO0oo0o
 if iiiiiI1iii11 != 'Failed' :
  OOOO0oO0OOo0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiiiI1iii11 )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in OOOO0oO0OOo0o :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , i11iii1II1I1 , 1016 , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 50 , "" , "Getting Redemption Links" )
    if 13 - 13 : IIiIiII11i / OOooOOo / OOooOOo + O0OOOoOoo0
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if IIIi11iiIIi != 'Failed' :
  IIIii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIIi11iiIIi )
  for I111iIii1i1 in IIIii :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( II11i1 + I111iIii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 60 , "" , "Getting Source 3 Links" )
    if 49 - 49 : o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % ooOOOoO
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if oOo000O00O != 'Failed' :
  i11I1I1iI11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oOo000O00O )
  for I111iIii1i1 in i11I1I1iI11I :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iII11 + I111iIii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 70 , "" , "Getting Source 4 Links" )
    if 13 - 13 : oO0oo0o . iI11I1II1I1I . O00o0O00 . ooOOOoO
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOOooO0 != 'Failed' :
  iIIIIi1 = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OOOooO0 )
  for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in iIIIIi1 :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + ' - Source - Dizi[/COLOR]' , i11iii1II1I1 , 8062 , IiiIiII1Ii1 )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 80 , "" , "Getting Dizi Links" )
    if 58 - 58 : I11O0O0oOO00O00o
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOoOo0Oo != 'Failed' :
  oOo0o0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOo0Oo )
  for i11iii1II1I1 , O0O00OOOo00O , iIi11OoO0OOOo0Oo , ii111Ii , I111iIii1i1 in oOo0o0O :
   if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
    Ooooo0Oo0oOo ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '- Source Scooby[/COLOR]' ) , i11iii1II1I1 , 1016 , O0O00OOOo00O , ii111Ii , iIi11OoO0OOOo0Oo )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 90 , "" , "Getting Scooby Links" )
    if 7 - 7 : IIiIiII11i / ooOOOoO % I11O0O0oOO00O00o + oOo0O0Ooo - o0o00Oo0O
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 45 - 45 : oOo0O0Ooo / Ii1IIIi1 + oO0oo0o + ooOOOoO
 o0o0o0oO0oOoo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if OOoOo0Oo != 'Failed' :
  for iIiIIii11iI in o0o0o0oO0oOoo :
   ii1II1i1 = OoOoo + iIiIIii11iI + ooOo0Oo
   II1II1i = II1I1i ( ii1II1i1 )
   if II1II1i != 'Failed' :
    iIiI111ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II1II1i )
    for I111iIii1i1 , iIi11OoO0OOOo0Oo , i11iii1II1I1 , IiiIiII1Ii1 , i1I , OOo000 in iIiI111ii :
     if OooOooO0OoOoo0o in I111iIii1i1 . lower ( ) :
      Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + ' - Source Pandoras[/COLOR]' , i11iii1II1I1 , OOo000 , IiiIiII1Ii1 , i1I , iIi11OoO0OOOo0Oo )
      iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      iII1I1iIi1i . update ( 100 , "" , "Getting Pandoras Links" )
      if 3 - 3 : I11i % I11i % oOo0O0Ooo - ooOoO0O00
      iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
      if 84 - 84 : I11O0O0oOO00O00o
      if 39 - 39 : o0o00Oo0O . ooOoO0O00 * Ii1I - oO0o - Ii1IIIi1 % I11i
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooi1I11i1 ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i11iii1II1I1 = ( I1Iii1III ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( ii1I1IIi ) . replace ( ' ' , '+' )
 if 37 - 37 : iI11I1II1I1I % I11O0O0oOO00O00o / ooOOOoO
 iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 iII1I1iIi1i . update ( 0 , "" , "Checking Source Links" )
 o0000o0OOOo = oo00oO0o000 ( i11iii1II1I1 )
 iII1I1iIi1i . update ( 100 , "" , "Checking Source Links" )
 if 37 - 37 : ii1ii11IIIiiI - oO0oo0o - oO0o
 if o0000o0OOOo != 'Failed' :
  OOOO0oO0OOo0o = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( o0000o0OOOo )
  for i11iii1II1I1 , I111iIii1i1 in OOOO0oO0OOo0o :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    OoO00O ( ( I111iIii1i1 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + i11iii1II1I1 ) , 222 , '' )
    iII1I1iIi1i . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iII1I1iIi1i . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 42 - 42 : iI11I1II1I1I % iI1ii11iIi1i - Ii1I + iI11I1II1I1I
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
II1iiiii = '{ZH},' ; iI11iIiIiiiI = '{IX},' ; I1oo0Oo = '{LM},'
if 100 - 100 : I11O0O0oOO00O00o
def I1OO0Oo0 ( url ) :
 iI1IIiI1 = cloudflare . source ( url )
 IIi11ii = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1IIiI1 )
 for url , I1ii1iiii , i11i1IIi , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( I1ii1iiii ) . replace ( 'Sezon' , ' Season ' ) + ( i11i1IIi ) . replace ( 'Bölüm' , ' Episode ' ) + I111iIii1i1 , url , 8063 , '' )
  if 10 - 10 : Ii1I + ooOOOoO
  if 58 - 58 : oOo0O0Ooo + ii / Ii1IIIi1 . O0OOOoOoo0 % I11i / Ii1I
  if 62 - 62 : IIiIiII11i
  if 12 - 12 : ooOOOoO + IIiIiII11i
def iIIii111i1 ( url ) :
 iI1IIiI1 = cloudflare . source ( url )
 IIi11ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI1IIiI1 )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( I111iIii1i1 , url , 222 , '' )
  if 80 - 80 : Ii1IIIi1
  if 3 - 3 : Ii1I * I11O0O0oOO00O00o
  if 53 - 53 : iI11I1II1I1I / Ii1IIIi1 % oO0o + ooOOOoO / O0OOOoOoo0
  if 74 - 74 : I1ii11iIi11i
def iIIIIi ( ) :
 if 44 - 44 : oOo0O0Ooo % O00o0O00 * Ii * Ii - I1ii11iIi11i . ii1ii11IIIiiI
 iI1IIiI1 = cloudflare . source ( I1Iii1III ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi11ii = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1IIiI1 )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 , i11i1IIi in IIi11ii :
  i11i1i1i ( I111iIii1i1 + '  -  ' + ( i11i1IIi ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , i11iii1II1I1 , 8063 , IiiIiII1Ii1 )
  if 68 - 68 : Ii1IIIi1 . I11O0O0oOO00O00o
def iiI1oOo00O ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 8002 , IiiIiII1Ii1 )
def IiIIIi11 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , time , url , I111iIii1i1 , ooo0Oo00000oooO in IIi11ii :
  Ooooo0Oo0oOo ( '%s %s' % ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , time ) , url , 1015 , IiiIiII1Ii1 , ooo0Oo00000oooO )
  if 80 - 80 : OOooOOo + iI11I1II1I1I . ooOOOoO
def Ii1i1I ( ) :
 if 42 - 42 : I11i / ooOOOoO
 i11i1i1i ( 'Coronation Street' , '' , 8001 , '' )
 i11i1i1i ( 'Eastenders' , '' , 8002 , '' )
 i11i1i1i ( 'Emmerdale' , '' , 8003 , '' )
 i11i1i1i ( 'Hollyoaks' , '' , 8004 , '' )
 i11i1i1i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 79 - 79 : iI1ii11iIi1i
 if 27 - 27 : oO0o + I1ii11iIi11i
 if 92 - 92 : oOo0O0Ooo % Ii1IIIi1
 if 31 - 31 : ii - oO0oo0o / ii1ii11IIIiiI
def OoO0oIiii1I ( ) :
 o0000o0OOOo = II1I1i ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi11ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'Holly' in I111iIii1i1 :
   IiiIiII1Ii1 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in i11iii1II1I1 :
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i11iii1II1I1 . replace ( '\\/' , '/' ) , 8006 , IiiIiII1Ii1 )
   else :
    pass
    if 66 - 66 : ii + I11i . ooOoO0O00 * Ii1IIIi1
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 92 - 92 : I11O0O0oOO00O00o / ii1ii11IIIiiI
def III11I1i ( ) :
 o0000o0OOOo = II1I1i ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi11ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'East' in I111iIii1i1 :
   IiiIiII1Ii1 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in i11iii1II1I1 :
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i11iii1II1I1 . replace ( '\\/' , '/' ) , 8006 , IiiIiII1Ii1 )
   else :
    pass
    if 14 - 14 : o0o00Oo0O / I11O0O0oOO00O00o . oO0o % Ii1IIIi1 . oO0oo0o
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16 : ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def O0O00o0Ooo0O0 ( ) :
 o0000o0OOOo = II1I1i ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi11ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'Emmer' in I111iIii1i1 :
   IiiIiII1Ii1 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in i11iii1II1I1 :
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i11iii1II1I1 . replace ( '\\/' , '/' ) , 8006 , IiiIiII1Ii1 )
   else :
    pass
    if 54 - 54 : OOooOOo . I1ii11iIi11i
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38 : ooOoO0O00 . I1ii11iIi11i * I1ii11iIi11i / Ii1I
def IIi1ii1I11II1 ( ) :
 o0000o0OOOo = II1I1i ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi11ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'Coro' in I111iIii1i1 :
   IiiIiII1Ii1 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in i11iii1II1I1 :
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i11iii1II1I1 . replace ( '\\/' , '/' ) , 8006 , IiiIiII1Ii1 )
   else :
    pass
    if 57 - 57 : IIiIiII11i % oOo0O0Ooo
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34 : oOo0O0Ooo
def o000000 ( ) :
 o0000o0OOOo = II1I1i ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'Celeb' in I111iIii1i1 :
   IiiIiII1Ii1 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in i11iii1II1I1 :
    OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , i11iii1II1I1 . replace ( '\\/' , '/' ) , 8006 , IiiIiII1Ii1 )
   else :
    pass
    if 9 - 9 : O00o0O00
def o0O0OO ( name , url ) :
 II1i1iIIi1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if II1i1iIIi1 :
  i1I1I1i1I1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  ooO0Oo = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( ooO0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  ooO0Oo = open_url ( url )
  IioooO = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( ooO0Oo ) [ - 1 ]
  i1I1I1i1I1 = IioooO . replace ( '\\/' , '/' )
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , '' , '' )
 oOoo0OoooOo0o . setPath ( i1I1I1i1I1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOoo0OoooOo0o )
 if 86 - 86 : I11i
 if 83 - 83 : oO0o
def oo0oo00OooOO ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi11ii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , i11iii1II1I1 , 7071 , ooOOoOO000 + 'popcorn.png' )
 for i11iii1II1I1 , I111iIii1i1 in OOOO0oO0OOo0o :
  i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , i11iii1II1I1 , 7071 , ooOOoOO000 + 'popcorn.png' )
  if 93 - 93 : ooOOOoO % Ii1I
def O0O00ooO0O0O ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi11ii = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'Movies' in I111iIii1i1 :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( i11iii1II1I1 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , ooOOoOO000 + 'popcorn.png' )
def Iiii1II ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( ooO0Oo )
 IIi11ii = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiiIiII1Ii1 )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , ooOOoOO000 + 'Next.png' )
  if 10 - 10 : ii . oOo0O0Ooo * o0o00Oo0O * oO0o - O00o0O00
  if 33 - 33 : Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def Ooo0o0OoOO ( url ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi11ii = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , url , IiiIiII1Ii1 in IIi11ii :
  if '{{' in I111iIii1i1 :
   pass
  else :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IiiIiII1Ii1 )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
IIi11oo0 = '{UJ},' ; OoOoo00oO = '{WE},' ; oo0OO0oo000O00oo = '{WP},' ; ooOO = '{PP},'
def i1IiI1i1iI1Ii ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , url , IiiIiII1Ii1 in IIi11ii :
  if '{{' in I111iIii1i1 :
   pass
  else :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiiIiII1Ii1 )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00OiIIII1iiIII ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  OO0oO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0oO ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 222 , ooOOoOO000 + 'popcorn.png' )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83 : o0o00Oo0O % IIiIiII11i + I11i / ii
 if 75 - 75 : IIiIiII11i . oOo0O0Ooo + O00o0O00 - OOooOOo - o0o00Oo0O . I11O0O0oOO00O00o
 if 19 - 19 : iI1ii11iIi1i * ooOoO0O00 % o0o00Oo0O + I11O0O0oOO00O00o
def ii11iIIi1i ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if '(cooltvseries.com)' in I111iIii1i1 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOOoOO000 + 'CoolSeries.png' )
 for url , I111iIii1i1 in OOOO0oO0OOo0o :
  if '(cooltvseries.com)' in I111iIii1i1 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , ooOOoOO000 + 'CoolSeries.png' )
def oOOooO00oOo00 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  IIIIi1I ( ( url ) . replace ( ' ' , '%20' ) )
iIII1II1iI = '{XX},' ; oOOOOoO00o0oo = '{UD},' ; i1i1iIiI = '{YT},' ; oO000ooO = '{JS},' ; OoOiIIiI = '{PF},'
if 47 - 47 : Ii1IIIi1 . OOooOOo
def IIi111i1i1III ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi11ii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  OoO00O ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( I1Iii1III ( i11iii1II1I1 ) ) , 222 , IiiIiII1Ii1 )
  if 31 - 31 : iI1ii11iIi1i * I11i * iI1ii11iIi1i + oO0o * I11i . ii1ii11IIIiiI
def O00oOo ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , url , I111iIii1i1 in IIi11ii :
  if 'youtu' in url :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']NEXT[/COLOR]' , url , 7050 , ooOOoOO000 + 'Next.png' )
  if 1 - 1 : ooOOOoO
def Ii1Ii1ii ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 92 - 92 : I11O0O0oOO00O00o % o0o00Oo0O % iI1ii11iIi1i . iI1ii11iIi1i . ooOOOoO
def oO0OOoooooo0o ( url ) :
 ooO0Oo = II1I1i
 IIi11ii = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 222 , IiiIiII1Ii1 )
  if 61 - 61 : oOo0O0Ooo + oO0oo0o % ii1ii11IIIiiI % iI11I1II1I1I - ii
  if 22 - 22 : O00o0O00 + IIiIiII11i + I1ii11iIi11i
  if 83 - 83 : O0OOOoOoo0
  if 43 - 43 : O00o0O00
  if 84 - 84 : O00o0O00 . ooOOOoO . Ii1IIIi1
def o0ooO0OO ( ) :
 if 26 - 26 : Ii1IIIi1 - I1ii11iIi11i + oOo0O0Ooo + I11i
 i11i1i1i ( 'All Channels' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Entertainment' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Movies' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Music' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'News' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Sports' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Documentary' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Kids' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Food' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Religious' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'USA Channels' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 i11i1i1i ( 'Other' , '' , 7021 , ooOOoOO000 + 'livetv.png' )
 if 37 - 37 : I11i * O00o0O00 + oOo0O0Ooo . Ii1I * ii
 if 82 - 82 : Ii + iI11I1II1I1I / I1ii11iIi11i + O00o0O00 * IIiIiII11i
def I1IiI1i1Iii ( Cat_Name ) :
 if 25 - 25 : o0o00Oo0O
 i1i1III11i1111i = False
 OO0OoO = '0'
 if Cat_Name == 'All Channels' : i1i1III11i1111i = True
 if Cat_Name == 'Entertainment' : OO0OoO = '1'
 if Cat_Name == 'Movies' : OO0OoO = '2'
 if Cat_Name == 'Music' : OO0OoO = '3'
 if Cat_Name == 'News' : OO0OoO = '4'
 if Cat_Name == 'Sports' : OO0OoO = '5'
 if Cat_Name == 'Documentary' : OO0OoO = '6'
 if Cat_Name == 'Kids' : OO0OoO = '7'
 if Cat_Name == 'Food' : OO0OoO = '8'
 if Cat_Name == 'Religious' : OO0OoO = '9'
 if Cat_Name == 'USA Channels' : OO0OoO = '10'
 if Cat_Name == 'Other' : OO0OoO = '11'
 if 39 - 39 : ii1ii11IIIiiI . oO0o % O0OOOoOoo0 . O00o0O00 / Ii1IIIi1 * oO0o
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi11ii = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( ooO0Oo )
 print 'Len Match: >>>' + str ( len ( IIi11ii ) )
 for I111iIii1i1 , IiiIiII1Ii1 , Oo0ooo in IIi11ii :
  iI1I1i1i = I1Iii1III ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiiIiII1Ii1 ) . replace ( '\\' , '' )
  if Oo0ooo == OO0OoO :
   i11i1i1i ( I111iIii1i1 , '' , 7022 , iI1I1i1i )
  elif i1i1III11i1111i == True :
   i11i1i1i ( I111iIii1i1 , '' , 7022 , iI1I1i1i )
  else : pass
  if 23 - 23 : oOo0O0Ooo
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 7 - 7 : Ii1IIIi1 % Ii1I
def ii1IIIiIII ( Search_Name ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi11ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( ooO0Oo )
 IIi11ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , i11iii1II1I1 , II1OoOOoOOOoooO0 , II11i1 in IIi11ii :
  iI1I1i1i = I1Iii1III ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiiIiII1Ii1 ) . replace ( '\\' , '' )
  OoO00O ( Search_Name + ': Link 1' , ( i11iii1II1I1 ) . replace ( '\\' , '' ) , 222 , iI1I1i1i )
  OoO00O ( Search_Name + ': Link 2' , ( II1OoOOoOOOoooO0 ) . replace ( '\\' , '' ) , 222 , iI1I1i1i )
  OoO00O ( Search_Name + ': Link 3' , ( II11i1 ) . replace ( '\\' , '' ) , 222 , iI1I1i1i )
  if 47 - 47 : O00o0O00 / IIiIiII11i % ooOOOoO . oO0oo0o * Ii1I
def ii11IoOo0O0Oo ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( oOo00o0oO ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi11ii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  OoO00O ( I111iIii1i1 , ( i11iii1II1I1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , ooOOoOO000 + 'english.png' )
def o0OO ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( oOo00o0oO ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi11ii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  OoO00O ( I111iIii1i1 , ( i11iii1II1I1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOOoOO000 + 'xxx.png' )
def I11ii1 ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( oOo00o0oO ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi11ii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( ooO0Oo )
 for I111iIii1i1 , i11iii1II1I1 in IIi11ii :
  OoO00O ( I111iIii1i1 , ( i11iii1II1I1 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , ooOOoOO000 + 'vod(1).png' )
  if 97 - 97 : I11i / ooOOOoO + OOooOOo + oO0o % ii1ii11IIIiiI
def iI1iI ( url ) :
 url
 oo0Oii1IIi1ii = xbmcgui . ListItem ( I111iIii1i1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo0Oii1IIi1ii )
 return
 if 42 - 42 : iI11I1II1I1I - O0OOOoOoo0 - I11O0O0oOO00O00o - ii1ii11IIIiiI
 if 33 - 33 : OOooOOo - o0o00Oo0O
def I1I1I1Ii1iI ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( ooO0Oo )
 for url , iIi11OoO0OOOo0Oo , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IiiIiII1Ii1 , '' , ( iIi11OoO0OOOo0Oo ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 for url in OOOO0oO0OOo0o :
  i11i1i1i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , ooOOoOO000 + 'Next.png' )
  if 30 - 30 : OOooOOo / oO0oo0o / iI1ii11iIi1i * I11i * oO0oo0o . oOo0O0Ooo
def OoOoOO0ooo0o0 ( url ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for url , iIi11OoO0OOOo0Oo , IiiIiII1Ii1 in IIi11ii :
  iII111I ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IiiIiII1Ii1 , '' , iIi11OoO0OOOo0Oo )
  iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 oooO000oO0O = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( o0000o0OOOo )
 for iiI1iIi1 in oooO000oO0O :
  oO00IiiIIi1IiI = ( iiI1iIi1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  Ooooo0Oo0oOo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IiiIiII1Ii1 , '' , oO00IiiIIi1IiI )
  if 13 - 13 : IIiIiII11i
def IIi1iiIii1Ii ( INFO ) :
 i11i1IiIi11 ( 'info for workout' , INFO )
 if 79 - 79 : Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 if 95 - 95 : oO0oo0o
 if 48 - 48 : I11O0O0oOO00O00o / iI11I1II1I1I % IIiIiII11i
def o000OOooO0O ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'Name=(.+?)\n.+?m3u=(.+?)\n' , re . DOTALL ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  i11i1i1i ( ( I111iIii1i1 ) . replace ( 'SlyNet' , '' ) , url , 9032 , ooOOoOO000 + 'Sport.png' )
def IIi1iIiII1iiiI11 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , url , 9032 , ooOOoOO000 + 'icon.png' )
def Ooo0ooo0OOo ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '#EXTINF:-.+?,(.+?)\n(.+?)\n' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  if '=' in I111iIii1i1 :
   pass
  else :
   OoO00O ( ( I111iIii1i1 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , ooOOoOO000 + 'icon.png' )
def oo0o0oOO ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  if '=' in I111iIii1i1 :
   pass
  else :
   OoO00O ( I111iIii1i1 , url , 222 , ooOOoOO000 + 'icon.png' )
   if 21 - 21 : o0o00Oo0O + o0o00Oo0O / I11i - I11O0O0oOO00O00o
   if 88 - 88 : Ii1I . IIiIiII11i / O00o0O00 % ooOoO0O00 - OOooOOo % Ii
   if 61 - 61 : ii . o0o00Oo0O % I11i * o0o00Oo0O
   if 23 - 23 : OOooOOo - iI1ii11iIi1i - oO0oo0o / ii
   if 12 - 12 : ii
def IiiiIIi111Ii1 ( ) :
 ooO0Oo = II1I1i ( I1Iii1III ( 'aHR0cDovL3NvdXJjZXR2LmluZm8v' ) )
 IIi11ii = re . compile ( '<li class="cat-item cat-item-.+?"><a href="([^"]*)" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 9008 , ooOOoOO000 + 'disclose.png' )
def O00OOO0OO ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="article-image darken"><a href="([^"]*)"><img width="320" height="205" src="([^"]*)".+?title="([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , url , 9009 , IiiIiII1Ii1 )
def iII1ii1iiI1 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  OoO00O ( ( I111iIii1i1 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 17 - 17 : oO0o
def ii1iiii1I ( ) :
 ooO0Oo = cloudflare . source ( I1Iii1III ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if '.m3u' in i11iii1II1I1 :
   i11i1i1i ( ( I111iIii1i1 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( I1Iii1III ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + i11iii1II1I1 ) , 9011 , ooOOoOO000 + 'disclose.png' )
def O0O0ii1IiIiI1 ( url ) :
 ooO0Oo = cloudflare . source ( url )
 IIi11ii = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  OoO00O ( ( I111iIii1i1 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 79 - 79 : ii - O0OOOoOoo0 * iI1ii11iIi1i - IIiIiII11i % OOooOOo * ooOOOoO
def Ii1111i ( ) :
 ooO0Oo = II1I1i ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi11ii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  if 'category' in i11iii1II1I1 :
   i11i1i1i ( I111iIii1i1 , 'http://www.disclose.tv/' + i11iii1II1I1 , 7010 , ooOOoOO000 + 'disclose.png' )
   if 42 - 42 : O0OOOoOoo0 + Ii1IIIi1 + iI1ii11iIi1i * I11O0O0oOO00O00o . ooOoO0O00
   if 72 - 72 : oOo0O0Ooo + iI1ii11iIi1i
def i1iiIiI ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( ooO0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 , IiiIiII1Ii1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , 'http://www.disclose.tv/' + url , 7011 , IiiIiII1Ii1 )
 for url in next :
  i11i1i1i ( 'NEXT' , url , 7010 , ooOOoOO000 + 'Next.png' )
  if 11 - 11 : OOooOOo / I11O0O0oOO00O00o
  if 47 - 47 : O00o0O00 . ii1ii11IIIiiI % IIiIiII11i + I1ii11iIi11i - oO0oo0o . IIiIiII11i
def IIii ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( ooO0Oo )
 IIIii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  if 'http' in url :
   OoO00O ( 'video/flv' , url , 222 , ooOOoOO000 + 'disclose.png' )
 for url , I111iIii1i1 in OOOO0oO0OOo0o :
  OoO00O ( I111iIii1i1 , url , 222 , ooOOoOO000 + 'disclose.png' )
 for url in IIIii :
  OoO00O ( 'YT Link' , url , 8043 , ooOOoOO000 + 'disclose.png' )
  if 25 - 25 : IIiIiII11i % IIiIiII11i - iI1ii11iIi1i . o0o00Oo0O
  if 79 - 79 : ooOOOoO / oO0o * ii * OOooOOo + oOo0O0Ooo
def iiiiIIiIIII ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , ooOOoOO000 + 'icon.png' )
  if 40 - 40 : I11i . I11i * Ii
def oooooO0oOO00oOo ( name , url , img ) :
 o0000o0OOOo = II1I1i ( url )
 OOo0oO0 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( o0000o0OOOo )
 i1ii1i1Iii = len ( OOo0oO0 )
 if 58 - 58 : Ii1IIIi1
 if 2 - 2 : IIiIiII11i + ooOoO0O00
 if i1ii1i1Iii == 1 :
  for IiioOoo in OOo0oO0 :
   IiioOoo = IiioOoo . replace ( 'player' , 'watch' )
   iIIiiIi1 = IiioOoo + '&fv=&sou='
   O0Oo0oO0 = II1I1i ( iIIiiIi1 )
   IiIi1Ii = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O0Oo0oO0 )
   for oOoo0o00O in IiIi1Ii :
    iii111IIiI11 = False
    Resolve ( oOoo0o00O )
    if 40 - 40 : Ii1IIIi1 + o0o00Oo0O
 elif i1ii1i1Iii > 1 :
  if 18 - 18 : iI11I1II1I1I % iI11I1II1I1I % oO0oo0o + oOo0O0Ooo % O0OOOoOoo0 / iI1ii11iIi1i
  for IiioOoo in OOo0oO0 :
   OoOOo = II1I1i ( IiioOoo )
   II1iiIIiII1 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OoOOo )
   ooO0o0O = II1iiIIiII1
   ooO0o0O = ( str ( ooO0o0O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooO0o0O
   OoO00O ( 'DOUBLE LINK' , ooO0o0O , 424 , '' )
   if 11 - 11 : OOooOOo
   for url in II1iiIIiII1 :
    i11i1i1i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     II1OoOOoOOOoooO0 = Google . resolve ( url )
    except :
     pass
    try :
     iIIiI11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( II1OoOOoOOOoooO0 ) )
     for iIi1Ii1ii1 , OOooOiii1 in iIIiI11 :
      if 95 - 95 : o0o00Oo0O . oO0o
      HD_URLS . append ( iIi1Ii1ii1 )
      SD_URLS . append ( OOooOiii1 )
    except :
     pass
 else :
  pass
  if 89 - 89 : ooOoO0O00
def i1i1IiiI11i ( ) :
 if 89 - 89 : oO0o . Ii1I - Ii * I1ii11iIi11i * Ii
 if 20 - 20 : Ii . iI1ii11iIi1i
 i11i1i1i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , ooOOoOO000 + 'Movies.png' )
 if 17 - 17 : OOooOOo - oOo0O0Ooo
 i11i1i1i ( 'Search Movies' , '' , 7017 , ooOOoOO000 + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 63 - 63 : OOooOOo - oO0oo0o / iI11I1II1I1I - iI1ii11iIi1i / ii1ii11IIIiiI
 if 34 - 34 : Ii1IIIi1 / I11i + O00o0O00 - I11i + I1ii11iIi11i . oO0oo0o
def ooII11iI1i ( ) :
 ooO0Oo = II1I1i ( 'http://cnfstudio.com/' )
 IIi11ii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , 'http://cnfstudio.com/genre/' + i11iii1II1I1 , 7003 , ooOOoOO000 + 'icon.png' )
  if 51 - 51 : O0OOOoOoo0 * Ii1IIIi1 / ooOoO0O00
ooOOoOoOoO00 = xbmcgui . Dialog ( )
if 2 - 2 : oO0oo0o + ooOOOoO . Ii1IIIi1 - ooOoO0O00 + ii1ii11IIIiiI
IIIIi11 = '{UN},' ; o000oOOoooo0o = '{IG},' ; OoOooOOo = '{PL},' ; o0Oo0OOO0 = '{LO},' ; OOoOOoo0ooo = '{LP},' ; OO0OOo00OOO00 = '{HA},' ; o0ooOO000o = '{XD},' ; O0Oo = '{TA},' ; o0O0oO00oo0O = '{DP},' ; i1iI = '{JT},' ; Oo0oOOoIIiIi = '{JJ},' ; iii111iI = '{MM},' ; OOoO00ooO0o0o000o = '{FQ},' ; i111 = '{HH},'
if 74 - 74 : Ii1IIIi1 / I11O0O0oOO00O00o . oOo0O0Ooo - ii + IIiIiII11i + I11O0O0oOO00O00o
def o0Ii11I ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( ooO0Oo )
 i1Ii1I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 , url , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IiiIiII1Ii1 )
 i1Ii1I = i1Ii1I
 for url in i1Ii1I :
  i11i1i1i ( 'Next Page' , url , 7003 , ooOOoOO000 + 'Next.png' )
  if 9 - 9 : Ii + O00o0O00 - OOooOOo / O0OOOoOoo0 % ooOoO0O00 / oO0oo0o
def I1iI1i ( url ) :
 if 42 - 42 : oO0o - Ii1I * ooOOOoO - O0OOOoOoo0
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  I1iIIiI1i = url + '&fv=&sou='
  I1iIIiI1i = I1iIIiI1i . replace ( 'player' , 'watch' )
  OO0o0O0 = o0o00OOoo ( I1iIIiI1i )
  oOOoOooo0oOO0 = o0o00OOoo ( url )
  if 87 - 87 : O00o0O00
  if 7 - 7 : ii1ii11IIIiiI - I11O0O0oOO00O00o % I11O0O0oOO00O00o + O0OOOoOoo0 * ooOoO0O00
def o0o00OOoo ( url ) :
 if 46 - 46 : oOo0O0Ooo % ooOOOoO - iI11I1II1I1I * I11i
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( ooO0Oo )
 for url in IIi11ii :
  Ii11 ( url )
  if 69 - 69 : oO0oo0o . I11O0O0oOO00O00o
  if 36 - 36 : O0OOOoOoo0
def o00o0O0oo ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Local M3u[/COLOR]' , O0oi1i1ii1Ii111i , 2001 , ooOOoOO000 + 'LocalM3U.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']Remote M3u[/COLOR]' , ii1IooO00OO0ooo , 7080 , ooOOoOO000 + 'RemoteM3U.png' , o00O0oOOo , '' )
 if 9 - 9 : ii1ii11IIIiiI - oO0o + iI11I1II1I1I % o0o00Oo0O + I11O0O0oOO00O00o + ooOOOoO
def IIIi11i1 ( ) :
 if os . path . exists ( O0oi1i1ii1Ii111i ) :
  o00oO = open ( O0oi1i1ii1Ii111i , 'r' )
  for oo0Oii1IIi1ii in o00oO :
   ii1II1IiIIiI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oo0Oii1IIi1ii )
   for I111iIii1i1 , i11iii1II1I1 in ii1II1IiIIiI :
    OoO00O ( I111iIii1i1 , i11iii1II1I1 , 222 , ooOOoOO000 + 'streams.png' )
 else :
  ooOOoOoOoO00 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0OoO . openSettings ( sys . argv [ 0 ] )
  if 88 - 88 : Ii1I - I11O0O0oOO00O00o * ii * Ii1IIIi1 . Ii . I11i
def I1Ii1i111I ( url ) :
 if os . path . exists ( Remote ) :
  o0000o0OOOo = oO0ooo000 ( url )
  IIi11ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000o0OOOo )
  for I111iIii1i1 , url in IIi11ii :
   url = ( url ) . strip ( )
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  ooOOoOoOoO00 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0OoO . openSettings ( sys . argv [ 0 ] )
  if 94 - 94 : I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + ii % oO0o
  if 36 - 36 : Ii1IIIi1 * I11O0O0oOO00O00o * o0o00Oo0O * O00o0O00 - I11i / Ii1I
def I1111iii1ii11 ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi11ii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 in IIi11ii :
  i11iii1II1I1 = I1Iii1III ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + i11iii1II1I1
 I111iIii1i1 = 'plugin.video.GenieTv'
 if 54 - 54 : ooOoO0O00 - oO0o / ii
 Oo00oo ( i11iii1II1I1 , I111iIii1i1 )
 if 100 - 100 : O00o0O00 % Ii - oOo0O0Ooo * ii1ii11IIIiiI - I11i
def i11i11Iii ( ) :
 o0000o0OOOo = II1I1i ( I1Iii1III ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi11ii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 in IIi11ii :
  i11iii1II1I1 = I1Iii1III ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + i11iii1II1I1
 I111iIii1i1 = 'repository.GenieTv'
 if 65 - 65 : Ii - ii / o0o00Oo0O * ooOOOoO % I11O0O0oOO00O00o
 Oo00oo ( i11iii1II1I1 , I111iIii1i1 )
 if 53 - 53 : O00o0O00 + ii1ii11IIIiiI
 if 10 - 10 : I11O0O0oOO00O00o * ooOoO0O00 . oO0oo0o / ii1ii11IIIiiI . O00o0O00 / ii1ii11IIIiiI
def II1ioOO0Oo ( ) :
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']CATAGORIES[/COLOR]' , '' , 10051 , ooOOoOO000 + 'Catagories.png' , o00O0oOOo , '' )
 Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']SEARCH[/COLOR]' , '' , 10052 , ooOOoOO000 + 'Search.png' , o00O0oOOo , '' )
 if 89 - 89 : ooOOOoO - ooOoO0O00 - ooOOOoO
 if 74 - 74 : oO0o % oO0o
o0OoO = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
ooOOoOoOoO00 = xbmcgui . Dialog ( )
Oo0oo0OoO0o0 = xbmc . translatePath ( 'special://home/' )
iII1I1iIi1i = xbmcgui . DialogProgress ( )
iIIiIi1111iiIii = 'https://addons.tvaddons.ag/'
if 91 - 91 : oOo0O0Ooo / IIiIiII11i * O00o0O00
def iii11IiiiI ( ) :
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 IiiIoOOoO0 = 'https://addons.tvaddons.ag/search/?keyword=' + OooOooO0OoOoo0o
 o0000o0OOOo = II1I1i ( IiiIoOOoO0 )
 IIi11ii = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , OOoi1I1I , I111iIii1i1 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , i11iii1II1I1 , 10054 , 'https://addons.tvaddons.ag/' + OOoi1I1I , o00O0oOOo , '' )
  if 56 - 56 : O0OOOoOoo0 . iI11I1II1I1I + ooOoO0O00
  if 84 - 84 : Ii1IIIi1 % ooOoO0O00
def O0ooO0 ( ) :
 o0000o0OOOo = II1I1i ( iIIiIi1111iiIii )
 IIi11ii = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0000o0OOOo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if 'Repositories' in I111iIii1i1 :
   pass
  elif 'Services' in I111iIii1i1 :
   pass
  elif 'International' in I111iIii1i1 :
   pass
  else :
   Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , i11iii1II1I1 , 10053 , 'https://addons.tvaddons.ag/' + IiiIiII1Ii1 , o00O0oOOo , '' )
   if 94 - 94 : ooOoO0O00 / Ii1I / oOo0O0Ooo * ii1ii11IIIiiI * I1ii11iIi11i
   if 21 - 21 : ii + o0o00Oo0O / ii / O00o0O00
def Addon ( url ) :
 o0000o0OOOo = II1I1i ( url )
 oOOOii = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( o0000o0OOOo )
 IIi11ii = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( o0000o0OOOo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if 'Please' in I111iIii1i1 :
   pass
  else :
   iII111I ( I111iIii1i1 , url , 10054 , 'https://addons.tvaddons.ag/' + IiiIiII1Ii1 , o00O0oOOo , '' )
 for url in oOOOii :
  Ooooo0Oo0oOo ( '[COLOR' + iiiI1iiI11iii + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , ooOOoOO000 + 'Next.png' , o00O0oOOo , '' )
  if 69 - 69 : oO0oo0o - ii1ii11IIIiiI / I1ii11iIi11i
  if 15 - 15 : ooOoO0O00
def II11I111 ( url , name ) :
 o0000o0OOOo = II1I1i ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)"' ) . findall ( o0000o0OOOo )
 for url in IIi11ii :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   iII1I1iIi1i = xbmcgui . DialogProgress ( )
   iII1I1iIi1i . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   i11ii1II = os . path . join ( II1OO , name + '.zip' )
   try :
    os . remove ( i11ii1II )
   except :
    pass
   downloader . download ( url , i11ii1II , iII1I1iIi1i )
   oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   iII1I1iIi1i . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oOoOOi1iIiII111i11
   print '======================================='
   extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
   Ii1iii1 ( )
   if 29 - 29 : I11O0O0oOO00O00o + oO0oo0o % O0OOOoOoo0 + OOooOOo
def Oo00oo ( url , name ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i11ii1II = os . path . join ( II1OO , name + '.zip' )
 try :
  os . remove ( i11ii1II )
 except :
  pass
 downloader . download ( url , i11ii1II , iII1I1iIi1i )
 oOoOOi1iIiII111i11 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 iII1I1iIi1i . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOoOOi1iIiII111i11
 print '======================================='
 extract . all ( i11ii1II , oOoOOi1iIiII111i11 , iII1I1iIi1i )
 Ii1iii1 ( )
 if 92 - 92 : I11i
def Ii1iii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 37 - 37 : oO0oo0o
 if 18 - 18 : ooOOOoO * Ii + iI11I1II1I1I % I11O0O0oOO00O00o + ooOoO0O00 - oO0o
def O00oO00Oooo0O ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , OOoi1I1I , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , url , 1007 , OOoi1I1I )
def iIi11IiII11 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , OOoi1I1I , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 1006 , OOoi1I1I )
  if 11 - 11 : Ii1IIIi1 / oO0oo0o % ooOoO0O00 . Ii1I
  if 16 - 16 : ii - O00o0O00 + I1ii11iIi11i
def OO0OOO ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , iconimage , iIi11OoO0OOOo0Oo , i1I , name in IIi11ii :
  if 'http' in url :
   if '.php' in url :
    OOo0o0oOOOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oo0o ) )
    for oo0Oii1IIi1ii in OOo0o0oOOOO00 :
     if oo0Oii1IIi1ii == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iiII ( name , url , 1016 , iconimage , i1I , iIi11OoO0OOOo0Oo )
   else :
    if 'youtube' in url :
     OOo0o0oOOOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oo0o ) )
     for oo0Oii1IIi1ii in OOo0o0oOOOO00 :
      if oo0Oii1IIi1ii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     oOOOOOOooO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , i1I , iIi11OoO0OOOo0Oo )
    else :
     OOo0o0oOOOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oo0o ) )
     for oo0Oii1IIi1ii in OOo0o0oOOOO00 :
      if oo0Oii1IIi1ii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     oOOOOOOooO ( name , url , 222 , iconimage , i1I , iIi11OoO0OOOo0Oo )
     iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
  else :
   iI1I11Ii1I ( url , iconimage , name )
   if 21 - 21 : ooOoO0O00
 else :
  IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
  for url , OOoi1I1I , name in IIi11ii :
   if 'http' in url :
    if '.php' in url :
     i11i1i1i ( name , url , 1016 , OOoi1I1I )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OoO00O ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoi1I1I )
     else :
      OOo0o0oOOOO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( oo0o ) )
      for oo0Oii1IIi1ii in OOo0o0oOOOO00 :
       if oo0Oii1IIi1ii == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OoO00O ( name , url , 222 , OOoi1I1I )
      iiiiII1i1Iii1I1 ( 'movies' , 'INFO' )
   else :
    iI1I11Ii1I ( url , OOoi1I1I , name )
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 85 - 85 : Ii1I * OOooOOo % I11O0O0oOO00O00o
def iI1I11Ii1I ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooO000OOOOOoO = ( url ) . replace ( iI11iIiIiiiI , 'http' ) . replace ( oOOOOoO00o0oo , '.com' ) ;
 IiiIiI1 = ( ooO000OOOOOoO ) . replace ( I1oo0Oo , 'a' ) . replace ( I1ii1I1i1 , 'b' ) . replace ( i11iii , 'c' ) . replace ( OoOoo00oO , 'd' ) . replace ( OoOooOOo , 'e' ) . replace ( i1iI , 'f' ) ;
 i1II = ( IiiIiI1 ) . replace ( iIII1II1iI , 'g' ) . replace ( OO0OOo00OOO00 , 'h' ) . replace ( i1i1iIiI , 'i' ) . replace ( OoOiIIiI , 'j' ) . replace ( oO0OoOoo00 , 'k' ) . replace ( IIiiIi1i , 'l' ) ;
 I1oO0O00oOo00o = ( i1II ) . replace ( I1oOooo , 'm' ) . replace ( II11IiI1I1I1 , 'n' ) . replace ( I1IIiIiI , 'o' ) . replace ( IioOo0Ooo0 , 'p' ) . replace ( o0OO0oooo00o , 'q' ) . replace ( iiII11iI1 , 'r' ) ;
 iII11Ii = ( I1oO0O00oOo00o ) . replace ( iIII1 , 's' ) . replace ( oo0OO0oo000O00oo , 't' ) . replace ( oOooO00O0oO0O , 'u' ) . replace ( iiIIOOo0o0o , 'v' ) . replace ( ii1i1II , 'w' ) . replace ( iiiI , 'x' ) ;
 IIO0 = ( iII11Ii ) . replace ( OOOooo , 'y' ) . replace ( IIIi111iI1I , 'z' ) . replace ( IIIIi11 , '.' ) . replace ( o000oOOoooo0o , '(' ) . replace ( o0Oo0OOO0 , ')' ) . replace ( OOoOOoo0ooo , '/' ) ;
 O0i1i11I1IIi1II = ( IIO0 ) . replace ( II1iiiii , '1' ) . replace ( ooOO , '2' ) . replace ( Ooo0O0O0Oo0OO , '3' ) . replace ( O0Oo , '4' ) . replace ( o0O0oO00oo0O , '5' ) . replace ( oO000ooO , '6' ) ;
 II1iIIII1 = ( O0i1i11I1IIi1II ) . replace ( Oo0oOOoIIiIi , '7' ) . replace ( iii111iI , '8' ) . replace ( OOoO00ooO0o0o000o , '9' ) . replace ( i111 , '0' ) . replace ( I1iiIi , ':' ) . replace ( IIoooO , '%' ) ;
 url = ( II1iIIII1 ) . replace ( IIi11oo0 , '-' ) . replace ( o0ooOO000o , '_' ) ;
 OoO00O ( name , url , 222 , iconimage ) ;
 if 81 - 81 : O0OOOoOoo0 + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * ii1ii11IIIiiI
 if 98 - 98 : Ii1I - ii / oOo0O0Ooo . O0OOOoOoo0 - ooOoO0O00
def IiIiI1IiIi ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , OOoi1I1I , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 1007 , OOoi1I1I )
def Ooo0O00o00 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , OOoi1I1I , I111iIii1i1 in IIi11ii :
  i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 1006 , OOoi1I1I )
  if 15 - 15 : ooOoO0O00 . oOo0O0Ooo - OOooOOo % IIiIiII11i . O0OOOoOoo0 / oO0oo0o
def oooo0OOoo0oO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iIiiiiiIii = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iIiiiiiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIiiiiiIii )
 if 63 - 63 : iI1ii11iIi1i - IIiIiII11i . I11O0O0oOO00O00o / OOooOOo
 if 17 - 17 : O0OOOoOoo0
def O00ii111I ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooO0Oo )
 for url , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  if '-dir-' in I111iIii1i1 :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IiiIiII1Ii1 )
  else :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' , url , 1006 , IiiIiII1Ii1 )
   if 33 - 33 : IIiIiII11i . Ii1I - o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def Iii11i1 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 ii1Ii1 = ( 'http://afewbitsmore.com/' )
 IIi11ii = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if '[To Parent Directory]' in I111iIii1i1 :
   I111iIii1i1 = 'HOME'
   pass
  elif 'HOME' in I111iIii1i1 :
   pass
  elif '.m3u' in I111iIii1i1 :
   i11i1i1i ( '[COLOR' + iiiI1iiI11iii + ']PLAY ALL[/COLOR]' , ii1Ii1 + url , 2002 , ooOOoOO000 + 'music.png' )
  elif '.mp3' in I111iIii1i1 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , ii1Ii1 + url , 222 , ooOOoOO000 + 'music.png' )
  elif '.m4a' in I111iIii1i1 :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , ii1Ii1 + url , 222 , ooOOoOO000 + 'music.png' )
  else :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) , ii1Ii1 + url , 1012 , ooOOoOO000 + 'music.png' )
def I1IiiIi11iIi1 ( url ) :
 o0000o0OOOo = oO0ooo000 ( url )
 IIi11ii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o0000o0OOOo )
 for IiiIiII1Ii1 , I111iIii1i1 , url in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , ooOOoOO000 + 'music.png' )
  if 88 - 88 : iI1ii11iIi1i / Ii % OOooOOo % O00o0O00
def o00oOoO0oO0ooO0o0 ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 ii1Ii1 = url
 IIi11ii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  if '.mp3' in I111iIii1i1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , ooOOoOO000 + 'music.png' )
  else :
   i11i1i1i ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '/' , '' ) , ii1Ii1 + url , 1011 , ooOOoOO000 + 'music.png' )
def O0ooOo00o0oOO ( ) :
 ooO0Oo = oO0ooo000 ( I1Iii1III ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi11ii = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( ooO0Oo )
 for i11iii1II1I1 , IiiIiII1Ii1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , ( 'http://www.cyn.net/music/' + i11iii1II1I1 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IiiIiII1Ii1 ) . replace ( ' ' , '%20' ) )
def I111iiiIiii1i ( url , img ) :
 ooO0Oo = oO0ooo000 ( url )
 II1OoOOoOOOoooO0 = url
 img = img
 IIi11ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( II1OoOOoOOOoooO0 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 66 - 66 : ii + Ii1IIIi1 . ooOOOoO % ooOoO0O00
def iI11iiiii ( url ) :
 ooO0Oo = oO0ooo000 ( url )
 II1OoOOoOOOoooO0 = url
 IIi11ii = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( ooO0Oo )
 for type , url , I111iIii1i1 in IIi11ii :
  if '[VID]' in type :
   OoO00O ( ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , II1OoOOoOOOoooO0 + url , 222 , ooOOoOO000 + 'music.png' )
  if '[DIR]' in type :
   iI11iiiii ( II1OoOOoOOOoooO0 + url )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31 : oOo0O0Ooo / OOooOOo
 if 72 - 72 : I1ii11iIi11i + ii1ii11IIIiiI % Ii1I + O00o0O00 % ii1ii11IIIiiI
def i1I1IIi1iI ( ) :
 II11IIiii = ( I1Iii1III ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 ii1I1IIi = ooOOoOoOoO00 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOooO0OoOoo0o = ii1I1IIi . lower ( )
 i11iii1II1I1 = ( I1Iii1III ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 II1OoOOoOOOoooO0 = ( I1Iii1III ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 II11i1 = ( I1Iii1III ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 10 - 10 : O0OOOoOoo0 - I1ii11iIi11i % IIiIiII11i
 o0000o0OOOo = oo00oO0o000 ( i11iii1II1I1 )
 iiiiiI1iii11 = oo00oO0o000 ( II1OoOOoOOOoooO0 )
 IIIi11iiIIi = oo00oO0o000 ( II11i1 )
 if 66 - 66 : iI11I1II1I1I . iI11I1II1I1I
 if o0000o0OOOo != 'Failed' :
  IIi11ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000o0OOOo )
  for I111iIii1i1 in IIi11ii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i11iii1II1I1 + I111iIii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 46 - 46 : ii1ii11IIIiiI * oO0oo0o . iI1ii11iIi1i * ii1ii11IIIiiI * iI11I1II1I1I / I11O0O0oOO00O00o
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if iiiiiI1iii11 != 'Failed' :
  OOOO0oO0OOo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o0000o0OOOo )
  for I111iIii1i1 in OOOO0oO0OOo0o :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( II1OoOOoOOOoooO0 + I111iIii1i1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 46 - 46 : IIiIiII11i % Ii1I . O00o0O00 . I1ii11iIi11i / Ii + oO0o
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
 if IIIi11iiIIi != 'Failed' :
  IIIii = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIIi11iiIIi )
  for I111iIii1i1 in IIIii :
   if ii1I1IIi in I111iIii1i1 . lower ( ) :
    i11i1i1i ( ( I111iIii1i1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( II11i1 + I111iIii1i1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 47 - 47 : ooOOOoO . O00o0O00
    iiiiII1i1Iii1I1 ( 'tvshows' , 'Media Info 3' )
    if 96 - 96 : I11O0O0oOO00O00o % IIiIiII11i / O0OOOoOoo0 % O00o0O00 / O0OOOoOoo0 % Ii
    if 57 - 57 : I11O0O0oOO00O00o - I11O0O0oOO00O00o % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
    if 91 - 91 : oOo0O0Ooo - oO0o - I1ii11iIi11i - iI1ii11iIi1i * iI11I1II1I1I
    if 68 - 68 : oO0o % o0o00Oo0O * iI11I1II1I1I / oO0oo0o * I11i + O00o0O00
    if 89 - 89 : O0OOOoOoo0 * oOo0O0Ooo . oO0oo0o
    if 75 - 75 : O0OOOoOoo0 - Ii1IIIi1 % Ii1IIIi1 + O0OOOoOoo0 * I11i - Ii1I
I1oOooo = '{SF},' ; II11IiI1I1I1 = '{IF},' ; I1IIiIiI = '{PW},' ; Ooo0O0O0Oo0OO = '{AM},' ; IioOo0Ooo0 = '{GF},' ; o0OO0oooo00o = '{DD},' ; iiII11iI1 = '{UO},' ; iIII1 = '{LE},' ; oOooO00O0oO0O = '{ZY},' ; iiIIOOo0o0o = '{UE},' ; ii1i1II = '{PE},' ; iiiI = '{JE},' ; OOOooo = '{TH},' ; IIIi111iI1I = '{LK},'
if 26 - 26 : I11O0O0oOO00O00o * iI1ii11iIi1i % oOo0O0Ooo + Ii1IIIi1
if 38 - 38 : Ii1IIIi1 - I1ii11iIi11i / iI1ii11iIi1i + oO0oo0o . Ii1IIIi1 + ooOOOoO
def oo0o00oOo0 ( ) :
 ooO0Oo = II1I1i ( 'http://www.iwatchseries.me/tv-list/' )
 IIi11ii = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 8021 , ooOOoOO000 + 'iwatch.png' )
def OoooO0 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 , OooooO0000 in IIi11ii :
  i11i1i1i ( I111iIii1i1 + OooooO0000 , url , 8022 , ooOOoOO000 + 'iwatch.png' )
def i1IOo0 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( ooO0Oo )
 for url in IIi11ii :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OoOo0Oo0 ( url )
def OoOo0Oo0 ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( ooO0Oo )
 OOOO0oO0OOo0o = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( ooO0Oo )
 IIIii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  OoO00O ( 'VidSpot - ' + I111iIii1i1 , url , 222 , ooOOoOO000 + 'iwatch.png' )
 for url in OOOO0oO0OOo0o :
  OoO00O ( 'VodLocker' , url , 222 , ooOOoOO000 + 'iwatch.png' )
 for I111iIii1i1 , url in IIIii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OoO00O ( 'TheVideo - ' + I111iIii1i1 , url , 222 , ooOOoOO000 + 'iwatch.png' )
   if 71 - 71 : I11i + O00o0O00 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
def o0Oo0OOoOOO000 ( ) :
 ooO0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi11ii = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 1021 , ooOOoOO000 + 'anime.png' )
  if 99 - 99 : oOo0O0Ooo
  if 78 - 78 : oO0o / iI11I1II1I1I . iI1ii11iIi1i * oO0o * OOooOOo - O00o0O00
def I1IO0OO0oo ( ) :
 ooO0Oo = II1I1i ( 'http://www.animetoon.org/cartoon' )
 IIi11ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( ooO0Oo )
 for i11iii1II1I1 , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , i11iii1II1I1 , 1002 , ooOOoOO000 + 'anime.png' )
  if 34 - 34 : ii
  if 84 - 84 : Ii + iI1ii11iIi1i
  if 81 - 81 : Ii % oOo0O0Ooo / Ii1IIIi1 % oO0o / ii1ii11IIIiiI % iI11I1II1I1I
def OoOOo0O0oOoo ( url ) :
 ooO0Oo = II1I1i ( url )
 OOOO0oO0OOo0o = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( ooO0Oo )
 for IiiIiII1Ii1 in OOOO0oO0OOo0o :
  OoOO0OooOoooo = IiiIiII1Ii1
 IIIii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( ooO0Oo )
 for url in IIIii :
  i11i1i1i ( 'NEXT PAGE' , url , 1002 , ooOOoOO000 + 'Next.png' )
 IIi11ii = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( ooO0Oo )
 for url , I111iIii1i1 in IIi11ii :
  i11i1i1i ( I111iIii1i1 , url , 1003 , OoOO0OooOoooo )
 xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0O0oOOoO ( url , IMAGE ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( ooO0Oo )
 for I111iIii1i1 , url in IIi11ii :
  print I111iIii1i1 + '     ' + url
  if 'easy' in url :
   i1iIIiII11I ( url )
  elif 'playpanda' in url :
   i1iIIiII11I ( url )
   if 6 - 6 : O00o0O00 . Ii - iI11I1II1I1I * ooOOOoO * Ii1IIIi1
  xbmcplugin . addSortMethod ( iI1i1i1i1i , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iIIiII11I ( url ) :
 ooO0Oo = II1I1i ( url )
 IIi11ii = re . compile ( "url: '(.+?)'," ) . findall ( ooO0Oo )
 for url in IIi11ii :
  OoO00O ( 'STREAM' , url , 222 , ooOOoOO000 + 'anime.png' )
  if 19 - 19 : o0o00Oo0O + oO0oo0o + I11i
  if 81 - 81 : iI11I1II1I1I
def I1OoO0ooOOO ( url ) :
 iIi1ii = urllib2 . Request ( url )
 iIi1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 iIi1ii . add_header ( 'referer' , url )
 I1I11 = urllib2 . urlopen ( iIi1ii )
 I1iIIiI1i = I1I11 . read ( )
 I1I11 . close ( )
 return I1iIIiI1i
 if 88 - 88 : O00o0O00 . I1ii11iIi11i * ooOOOoO - iI11I1II1I1I % oO0oo0o
def oO0ooo000 ( url ) :
 iIi1ii = urllib2 . Request ( url )
 iIi1ii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1I11 = urllib2 . urlopen ( iIi1ii )
 I1iIIiI1i = I1I11 . read ( )
 I1I11 . close ( )
 return I1iIIiI1i
 if 80 - 80 : iI1ii11iIi1i - Ii1I . iI1ii11iIi1i / Ii + o0o00Oo0O . ooOOOoO
def oO0O0O00 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiIiIiiI1Ii = ( '%s%s' % ( iIIiiii , url ) )
 I1iIIiI1i = oO0ooo000 ( url )
 IIi11ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1iIIiI1i )
 for url , OOoi1I1I , I111iIii1i1 in IIi11ii :
  OoO00O ( '%s' % ( '[COLOR' + iiiI1iiI11iii + ']' + I111iIii1i1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , OOoi1I1I )
  if 54 - 54 : ii1ii11IIIiiI / I11i
def Ii11 ( url ) :
 if 39 - 39 : O00o0O00 % oO0oo0o * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
 OOo00 = open ( ii1II1i1I1II11I1 , "a" )
 OOo00 . write ( 'url="' + url + '"\n' )
 OOo00 . close
 if 91 - 91 : oOo0O0Ooo - Ii1IIIi1 / oO0o - oO0o / iI1ii11iIi1i - ooOOOoO
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 import urlresolver
 try : II111iii . play ( url )
 except : pass
 from urlresolver import common
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( 'LOADING' , 'Opening %s Now' % ( I111iIii1i1 ) )
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if iII1I1iIi1i . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  if ooOOoOoOoO00 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   ooOOoOoOoO00 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : II111iii . play ( url )
  except : pass
  try : o0OoO . resolve_url ( url )
  except : pass
  iII1I1iIi1i . close ( )
  if 14 - 14 : O00o0O00 / I11i + iI1ii11iIi1i / ii - I11O0O0oOO00O00o
def i1iIIII11I ( url ) :
 iII1I1iIi1i = xbmcgui . DialogProgress ( )
 iII1I1iIi1i . create ( 'Featching Your Video' , 'Featching Your Video' )
 iII1I1iIi1i . update ( 0 , '%s' % I111iIii1i1 )
 xbmc . sleep ( 1 )
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 iII1I1iIi1i . update ( 100 , '%s' % I111iIii1i1 )
 xbmc . sleep ( 1 )
 II111iii . play ( url ) . strip ( )
 iII1I1iIi1i . close ( )
 if 65 - 65 : OOooOOo / Ii1I / I11i
def IIIIi1I ( url ) :
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II111iii . play ( url ) . strip ( )
 except : pass
 if 15 - 15 : O0OOOoOoo0 / O0OOOoOoo0 % ii . ii1ii11IIIiiI
def i111I ( url ) :
 II111iii = xbmc . Player ( OOoO0ooo ( ) )
 import urlresolver
 OO0OoO0o00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 II111iii . play ( OO0OoO0o00 )
 xbmc . sleep ( 1 )
 II111iii . play ( url )
 if 90 - 90 : oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + oO0oo0o
 if 58 - 58 : Ii1IIIi1 - ii
def OOoO0ooo ( ) :
 try :
  oOO00Oo = getSet ( "core-player" )
  if ( oOO00Oo == 'DVDPLAYER' ) : Ii1I1iII1I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oOO00Oo == 'MPLAYER' ) : Ii1I1iII1I = xbmc . PLAYER_CORE_MPLAYER
  elif ( oOO00Oo == 'PAPLAYER' ) : Ii1I1iII1I = xbmc . PLAYER_CORE_PAPLAYER
  else : Ii1I1iII1I = xbmc . PLAYER_CORE_AUTO
 except : Ii1I1iII1I = xbmc . PLAYER_CORE_AUTO
 return Ii1I1iII1I
 return True
 if 27 - 27 : Ii1IIIi1 . OOooOOo / ii
def i11i1i1i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0o0O = [ ]
  if showcontext == 'fav' :
   O0o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oo0oO0oO00oO :
   O0o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoo0OoooOo0o . addContextMenuItems ( O0o0O )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = True )
 return Iii11i1111II
 if 58 - 58 : ooOoO0O00 + o0o00Oo0O . oO0o % I11O0O0oOO00O00o
def iii1I1 ( name , url , mode , iconimage , fanart , description ) :
 if 39 - 39 : I11i + ooOOOoO / iI1ii11iIi1i + I11i
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoo0OoooOo0o . setProperty ( "Fanart_Image" , fanart )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = True )
 return Iii11i1111II
 if 33 - 33 : Ii1IIIi1 - I1ii11iIi11i - I11O0O0oOO00O00o
def OoO00O ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0o0O = [ ]
  if showcontext == 'fav' :
   O0o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oo0oO0oO00oO :
   O0o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOoo0OoooOo0o . addContextMenuItems ( O0o0O )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = False )
 return Iii11i1111II
 if 61 - 61 : iI1ii11iIi1i + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / oO0oo0o
 if 47 - 47 : ii1ii11IIIiiI
 if 25 - 25 : Ii1IIIi1 + oOo0O0Ooo + OOooOOo + ii1ii11IIIiiI % o0o00Oo0O
 if 26 - 26 : O0OOOoOoo0 + OOooOOo
 if 17 - 17 : Ii1I - Ii1IIIi1 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * O00o0O00
 if 6 - 6 : ii1ii11IIIiiI
def i11i1IiIi11 ( heading , announce ) :
 class O0o0000oo ( ) :
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
   try : O00o0 = open ( announce ) ; iII1I = O00o0 . read ( )
   except : iII1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iII1I ) )
   return
 O0o0000oo ( )
 O0o0000oo ( )
 if 95 - 95 : ii1ii11IIIiiI - ooOOOoO
def iIIIi1I ( ) :
 i11i1IiIi11 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 82 - 82 : OOooOOo . iI1ii11iIi1i
 if 73 - 73 : ii1ii11IIIiiI
 if 25 - 25 : ooOOOoO
 if 77 - 77 : I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87 : IIiIiII11i - ii / ooOoO0O00 . iI1ii11iIi1i - I1ii11iIi11i . Ii
def Ii1iii1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 47 - 47 : I1ii11iIi11i % oO0o - O0OOOoOoo0 - I1ii11iIi11i * oO0oo0o
 if 72 - 72 : I11i % I11i + Ii1IIIi1 + Ii1I / I1ii11iIi11i
 if 30 - 30 : I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if 64 - 64 : ooOOOoO
 if 80 - 80 : oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
 if 89 - 89 : o0o00Oo0O + ooOOOoO * ii1ii11IIIiiI
 if 30 - 30 : OOooOOo
 if 39 - 39 : Ii1I + I11i + ii1ii11IIIiiI + ooOOOoO
 if 48 - 48 : ii1ii11IIIiiI / O0OOOoOoo0 . iI11I1II1I1I
 if 72 - 72 : ooOoO0O00 . I11i
 if 3 - 3 : OOooOOo % IIiIiII11i - o0o00Oo0O
 if 52 - 52 : oO0o
 if 49 - 49 : iI1ii11iIi1i . Ii1I % O0OOOoOoo0 . I1ii11iIi11i * O00o0O00
 if 44 - 44 : iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0OOOoOoo0
 if 20 - 20 : Ii1IIIi1 + I11i . ii1ii11IIIiiI / Ii
 if 7 - 7 : OOooOOo / OOooOOo . ii1ii11IIIiiI * o0o00Oo0O + ooOOOoO + oO0oo0o
 if 98 - 98 : IIiIiII11i * ooOOOoO - oOo0O0Ooo % I11i - Ii1IIIi1 % Ii1I
 if 69 - 69 : ooOoO0O00 % oO0o % ii1ii11IIIiiI / O0OOOoOoo0 / O0OOOoOoo0
 if 6 - 6 : IIiIiII11i % Ii1I % ooOoO0O00 * O0OOOoOoo0
 if 47 - 47 : o0o00Oo0O
 if 55 - 55 : oO0o % o0o00Oo0O / ii
 if 49 - 49 : oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88 : Ii1I * Ii1IIIi1 + IIiIiII11i
 if 62 - 62 : ii
def OOOoOOoo ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + IiIi1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 83 - 83 : I1ii11iIi11i / O0OOOoOoo0
def II11I ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + o0oO0IIii1iIIiiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 41 - 41 : O0OOOoOoo0 / oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . Ii1I
def O0OOOo0 ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + oOOo0Ooo0oOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 20 - 20 : Ii
def iI1iIiIIiIiiI ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + ooO0o0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 61 - 61 : I11O0O0oOO00O00o * iI1ii11iIi1i + I11O0O0oOO00O00o - I1ii11iIi11i % OOooOOo . Ii1IIIi1
def ooOooo ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + I111I1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 76 - 76 : oOo0O0Ooo
def i11io00OOO00Oo ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + O000OOO00O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 54 - 54 : O0OOOoOoo0
def i1III ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + iI111i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 99 - 99 : I11i / O00o0O00 / oO0oo0o . ii1ii11IIIiiI
def OOOi1i1Iiii ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + O00OOOOOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 80 - 80 : iI11I1II1I1I * iI11I1II1I1I + iI1ii11iIi1i % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def iI1Ii1III ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + i111iI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 42 , O0O00OOOo00O , i1I , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 52 - 52 : ii / iI1ii11iIi1i - o0o00Oo0O % ooOoO0O00 * O00o0O00
def OooOO ( url ) :
 I1iIIiI1i = II1I1i ( str ( OooO ) + O0OIIiI1I1Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi11ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( I1iIIiI1i )
 for I111iIii1i1 , url , O0O00OOOo00O , i1I , O0ooOO0O00 in IIi11ii :
  Ooooo0Oo0oOo ( I111iIii1i1 , url , 5 , ooOOoOO000 + 'GenieTVRSSFeed.png' , ooOOoOO000 + 'GenieTVRSSFeed.png' , O0ooOO0O00 )
 iiiiII1i1Iii1I1 ( 'movies' , 'MAIN' )
 if 4 - 4 : oOo0O0Ooo / IIiIiII11i % o0o00Oo0O * O0OOOoOoo0 / IIiIiII11i . I1ii11iIi11i
 if 16 - 16 : o0o00Oo0O + o0o00Oo0O - oOo0O0Ooo
 if 30 - 30 : O0OOOoOoo0
 if 33 - 33 : ii1ii11IIIiiI * ooOOOoO - o0o00Oo0O + oOo0O0Ooo / ooOOOoO
 if 19 - 19 : ooOoO0O00 % IIiIiII11i
 if 85 - 85 : ooOOOoO - I11i % O00o0O00 - IIiIiII11i
 if 56 - 56 : iI1ii11iIi1i * Ii
 if 92 - 92 : IIiIiII11i - o0o00Oo0O . ii1ii11IIIiiI
 if 59 - 59 : OOooOOo
def oOOoO0ii1I1Ii11 ( ) :
 try :
  if os . path . exists ( ooo0O0Oo0O ) == True :
   ooOOoOoOoO00 = xbmcgui . Dialog ( )
   if ooOOoOoOoO00 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( ooo0O0Oo0O ) :
     OO0OOOO = 0
     OO0OOOO += len ( IIIIi1iII )
     if OO0OOOO > 0 :
      for O00o0 in IIIIi1iII :
       os . unlink ( os . path . join ( i11IIi , O00o0 ) )
  I1Iiiii1 = os . path . join ( IiiOo , "Textures13.db" )
  os . unlink ( I1Iiiii1 )
  ooOOoOoOoO00 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 13 - 13 : OOooOOo - oO0o * ii
 if 26 - 26 : ii
 if 65 - 65 : O00o0O00
 if 14 - 14 : O0OOOoOoo0
 if 75 - 75 : iI11I1II1I1I % O0OOOoOoo0 / O00o0O00 - Ii1IIIi1 % Ii
 if 11 - 11 : I11O0O0oOO00O00o . iI1ii11iIi1i
 if 87 - 87 : O00o0O00 + O00o0O00
 if 45 - 45 : ooOoO0O00 - I1ii11iIi11i
def iI11 ( title , message , times = 2000 , icon = i1OOO00oO0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 87 - 87 : OOooOOo - oO0o * oO0o / iI1ii11iIi1i . I11O0O0oOO00O00o * I11i
def iiIi1I1IIIII1IIi ( url ) :
 OoOo00O = os . path . join ( o0oOoooOoo0 , 'addon_data' )
 o0O00ooO0O0Oo = [
 ( OoOo00O ) ,
 ( i1I1Iii1IiiIi ) ,
 ( os . path . join ( Oo0oo0OoO0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0oo0OoO0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( i1I1Iii1IiiIi , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( i1I1Iii1IiiIi , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OoOo00O , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OoOo00O , 'plugin.video.itv' , 'Images' ) ) ]
 if 27 - 27 : iI11I1II1I1I + oO0oo0o % I1ii11iIi11i
 ooOo0ooO0Oo = 0
 if 41 - 41 : O0OOOoOoo0
 for oo0Oii1IIi1ii in o0O00ooO0O0Oo :
  if os . path . exists ( oo0Oii1IIi1ii ) and not oo0Oii1IIi1ii in [ i1I1Iii1IiiIi , OoOo00O ] :
   for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( oo0Oii1IIi1ii ) :
    OO0OOOO = 0
    OO0OOOO += len ( IIIIi1iII )
    if OO0OOOO > 0 :
     for O00o0 in IIIIi1iII :
      if not O00o0 in IiI1Iii1iIIII :
       try :
        os . unlink ( os . path . join ( i11IIi , O00o0 ) )
       except :
        pass
      else : OoOoooOooOO0o ( 'Ignore Log File: %s' % O00o0 )
     for iIi1IIIi1Ii in oo0O00O0oO :
      try :
       shutil . rmtree ( os . path . join ( i11IIi , iIi1IIIi1Ii ) )
       ooOo0ooO0Oo += 1
       OoOoooOooOO0o ( "[Success] cleared %s files from %s" % ( str ( OO0OOOO ) , os . path . join ( oo0Oii1IIi1ii , iIi1IIIi1Ii ) ) )
      except :
       OoOoooOooOO0o ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0Oii1IIi1ii , iIi1IIIi1Ii ) )
  else :
   for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( oo0Oii1IIi1ii ) :
    for iIi1IIIi1Ii in oo0O00O0oO :
     if 'cache' in iIi1IIIi1Ii . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( i11IIi , iIi1IIIi1Ii ) )
       ooOo0ooO0Oo += 1
       OoOoooOooOO0o ( "[Success] wiped %s " % os . path . join ( oo0Oii1IIi1ii , iIi1IIIi1Ii ) )
      except :
       OoOoooOooOO0o ( "[Failed] to wipe cache in: %s" % os . path . join ( oo0Oii1IIi1ii , iIi1IIIi1Ii ) )
       if 11 - 11 : ooOoO0O00 / ii1ii11IIIiiI * Ii1I * ii1ii11IIIiiI * O0OOOoOoo0 - Ii
 iI11 ( iIOoO0O00o0ooo0 , 'Clear Cache: Removed %s Files' % ooOo0ooO0Oo )
 if 96 - 96 : Ii1I % Ii1I
 if 1 - 1 : oOo0O0Ooo . iI1ii11iIi1i
 if 26 - 26 : oO0oo0o - O0OOOoOoo0 % I1ii11iIi11i - oO0oo0o + ooOOOoO
 if 33 - 33 : iI1ii11iIi1i + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * ooOOOoO
 if 21 - 21 : o0o00Oo0O * O0OOOoOoo0 % oO0o
 if 14 - 14 : o0o00Oo0O / ii1ii11IIIiiI / O0OOOoOoo0 + ooOOOoO - ooOOOoO
 if 10 - 10 : o0o00Oo0O - Ii1I / ii1ii11IIIiiI % OOooOOo / ii / iI1ii11iIi1i
def II1iiI1iIii1i ( url ) :
 print '###' + O0OO0o + ' - DELETING PACKAGES###'
 ooO0OO0OoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( ooO0OO0OoO0 ) :
   OO0OOOO = 0
   OO0OOOO += len ( IIIIi1iII )
   if 83 - 83 : ii . Ii1IIIi1
   if 20 - 20 : oO0o . oO0oo0o
   if OO0OOOO > 0 :
    if 4 - 4 : I1ii11iIi11i % iI1ii11iIi1i % oO0o * Ii1IIIi1 % ii
    ooOOoOoOoO00 = xbmcgui . Dialog ( )
    if ooOOoOoOoO00 . yesno ( "Delete Package Cache Files" , str ( OO0OOOO ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38 : ii . Ii1IIIi1
     for O00o0 in IIIIi1iII :
      os . unlink ( os . path . join ( i11IIi , O00o0 ) )
     for iIi1IIIi1Ii in oo0O00O0oO :
      shutil . rmtree ( os . path . join ( i11IIi , iIi1IIIi1Ii ) )
     ooOOoOoOoO00 = xbmcgui . Dialog ( )
     ooOOoOoOoO00 . ok ( O0OO0o , "       Deleting Packages all done" )
    else :
     pass
   else :
    ooOOoOoOoO00 = xbmcgui . Dialog ( )
    ooOOoOoOoO00 . ok ( O0OO0o , "       No Packages to DELETE" )
 except :
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 43 - 43 : ii
 if 8 - 8 : O00o0O00 + I11O0O0oOO00O00o . I11O0O0oOO00O00o
 if 89 - 89 : Ii1I * Ii1I * OOooOOo / Ii1IIIi1
 if 60 - 60 : oO0o / Ii1IIIi1 / oOo0O0Ooo + oO0oo0o
 if 93 - 93 : ii * iI1ii11iIi1i / o0o00Oo0O + iI1ii11iIi1i - iI11I1II1I1I
 if 6 - 6 : ooOOOoO - I1ii11iIi11i - I11O0O0oOO00O00o - o0o00Oo0O % ii
 if 88 - 88 : o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if 27 - 27 : Ii % Ii1IIIi1 + iI1ii11iIi1i . O00o0O00
 if 9 - 9 : oO0o
def i1iIiiii ( url ) :
 print '###' + O0OO0o + ' - DELETING PACKAGES###'
 ooO0OO0OoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( ooO0OO0OoO0 ) :
   OO0OOOO = 0
   OO0OOOO += len ( IIIIi1iII )
   if 43 - 43 : iI1ii11iIi1i . O00o0O00 + oOo0O0Ooo * Ii
   if 2 - 2 : O00o0O00
   if OO0OOOO > 0 :
    if 3 - 3 : oOo0O0Ooo . Ii1IIIi1 % o0o00Oo0O - O0OOOoOoo0 / o0o00Oo0O
    ooOOoOoOoO00 = xbmcgui . Dialog ( )
    if ooOOoOoOoO00 . yesno ( "Delete Package Cache Files" , str ( OO0OOOO ) + " files found" , "Do you want to delete them?" ) :
     if 79 - 79 : iI1ii11iIi1i + oO0oo0o % O0OOOoOoo0 % oOo0O0Ooo
     for O00o0 in IIIIi1iII :
      os . unlink ( os . path . join ( i11IIi , O00o0 ) )
     for iIi1IIIi1Ii in oo0O00O0oO :
      shutil . rmtree ( os . path . join ( i11IIi , iIi1IIIi1Ii ) )
     ooOOoOoOoO00 = xbmcgui . Dialog ( )
     ooOOoOoOoO00 . ok ( O0OO0o , "       Deleting Packages all done" )
    else :
     pass
   else :
    ooOOoOoOoO00 = xbmcgui . Dialog ( )
    ooOOoOoOoO00 . ok ( O0OO0o , "       No Packages to DELETE" )
 except :
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 iiIi1I1IIIII1IIi ( url )
 return
 if 68 - 68 : IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53 : Ii1IIIi1 . oO0oo0o / I1ii11iIi11i . oO0o . Ii
 if 60 - 60 : IIiIiII11i
 if 25 - 25 : I1ii11iIi11i + I11i - oO0o
 if 57 - 57 : IIiIiII11i . ooOoO0O00
 if 33 - 33 : Ii1IIIi1 + I1ii11iIi11i % I11O0O0oOO00O00o . oO0oo0o
 if 6 - 6 : ooOOOoO + Ii1I
 if 62 - 62 : oO0oo0o . ii1ii11IIIiiI - ii * IIiIiII11i . Ii
 if 13 - 13 : iI11I1II1I1I * I11i - Ii
 if 63 - 63 : ii * ii1ii11IIIiiI
def IIIIIi ( url , name ) :
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0OooO0oOoO = os . path . join ( II1OO , 'advancedsettings.xml' )
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 Ii11I111i1i11 = os . path . join ( II1OO , 'advancedsettings.xml.bak' )
 if os . path . exists ( Ii11I111i1i11 ) == False :
  if ooOOoOoOoO00 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + O0OO0o + ' - ADVANCED XML###'
   II1OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oo0OooO0oOoO = os . path . join ( II1OO , 'advancedsettings.xml' )
   try :
    os . remove ( oo0OooO0oOoO )
    print '=== GenieTv - REMOVING    ' + str ( oo0OooO0oOoO ) + '    ==='
   except :
    pass
   I1iIIiI1i = ii111II . http_GET ( url ) . content
   ooO0o0o = open ( oo0OooO0oOoO , "w" )
   ooO0o0o . write ( I1iIIiI1i )
   ooO0o0o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oo0OooO0oOoO ) + '    ==='
   ooOOoOoOoO00 = xbmcgui . Dialog ( )
   ooOOoOoOoO00 . ok ( O0OO0o , "       Done Adding new Advanced XML" )
 else :
  print '###' + O0OO0o + ' - ADVANCED XML###'
  II1OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oo0OooO0oOoO = os . path . join ( II1OO , 'advancedsettings.xml' )
  try :
   os . remove ( oo0OooO0oOoO )
   print '=== GenieTv - REMOVING    ' + str ( oo0OooO0oOoO ) + '    ==='
  except :
   pass
  I1iIIiI1i = ii111II . http_GET ( url ) . content
  ooO0o0o = open ( oo0OooO0oOoO , "w" )
  ooO0o0o . write ( I1iIIiI1i )
  ooO0o0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0OooO0oOoO ) + '    ==='
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "       Done Adding new Advanced XML" )
 return
 if 73 - 73 : oOo0O0Ooo / o0o00Oo0O % Ii1IIIi1 * IIiIiII11i
def O0oOO0Oo0O0O ( url , name ) :
 print '###' + O0OO0o + ' - CHECK ADVANCE XML###'
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0OooO0oOoO = os . path . join ( II1OO , 'advancedsettings.xml' )
 try :
  ooO0o0o = open ( oo0OooO0oOoO ) . read ( )
  if 'zero' in ooO0o0o :
   name = '0CACHE'
  elif 'tuxen' in ooO0o0o :
   name = 'TUXENS'
  elif 'muckys' in ooO0o0o :
   name = 'MUCKYS'
  elif 'p2p1' in ooO0o0o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooO0o0o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooO0o0o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 ooOOoOoOoO00 . ok ( O0OO0o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 23 - 23 : O00o0O00 + O0OOOoOoo0 / Ii * I1ii11iIi11i . oO0o
def O000 ( url ) :
 print '###' + O0OO0o + ' - DELETING ADVANCE XML###'
 II1OO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oo0OooO0oOoO = os . path . join ( II1OO , 'advancedsettings.xml' )
 try :
  os . remove ( oo0OooO0oOoO )
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oo0OooO0oOoO ) + '    ==='
  ooOOoOoOoO00 . ok ( O0OO0o , "       Remove Advanced Settings Sucessfull" )
 except :
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "       No Advanced Settings To Remove" )
 return
 if 51 - 51 : oOo0O0Ooo * O0OOOoOoo0
 if 47 - 47 : O00o0O00 . O00o0O00 . ooOOOoO . ii1ii11IIIiiI / ooOoO0O00
 if 77 - 77 : IIiIiII11i % I11O0O0oOO00O00o / I1ii11iIi11i
 if 23 - 23 : iI11I1II1I1I
 if 10 - 10 : I11O0O0oOO00O00o - I11i % ii - Ii1I
 if 64 - 64 : oO0o / oOo0O0Ooo
 if 23 - 23 : I11O0O0oOO00O00o * ii1ii11IIIiiI * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41 : ooOOOoO * ii . O0OOOoOoo0 % Ii
 if 11 - 11 : iI11I1II1I1I . ii1ii11IIIiiI - I1ii11iIi11i / I11O0O0oOO00O00o + IIiIiII11i
 if 29 - 29 : I11O0O0oOO00O00o . Ii + ooOoO0O00 - iI1ii11iIi1i + o0o00Oo0O . oOo0O0Ooo
def OO0I11 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi11ii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( ii111II . http_GET ( url ) . content )
 for OoOi1I1I1 , ii11IiIII , ii1ii1I11Ii , o0oo0OoOO0Ooo in IIi11ii :
  if inc < 2 : ooOOoOoOoO00 = xbmcgui . Dialog ( ) ; ooOOoOoOoO00 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OoOi1I1I1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ii1ii1I11Ii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % o0oo0OoOO0Ooo )
  inc = inc + 1
  if 2 - 2 : ii
  if 100 - 100 : I1ii11iIi11i / o0o00Oo0O * Ii * ii
  if 46 - 46 : o0o00Oo0O % ii
  if 22 - 22 : Ii1IIIi1 + ii - OOooOOo - oO0o * ii1ii11IIIiiI - oO0oo0o
  if 99 - 99 : O0OOOoOoo0 / oOo0O0Ooo . iI1ii11iIi1i - iI1ii11iIi1i * oOo0O0Ooo
  if 24 - 24 : I11O0O0oOO00O00o * oO0o - oO0oo0o / iI11I1II1I1I - I1ii11iIi11i . O00o0O00
  if 2 - 2 : O0OOOoOoo0 - o0o00Oo0O - Ii1I / I11O0O0oOO00O00o * OOooOOo
  if 26 - 26 : Ii1I + ii1ii11IIIiiI - oO0oo0o + ooOOOoO % O00o0O00
  if 84 - 84 : I11O0O0oOO00O00o % iI1ii11iIi1i % o0o00Oo0O * I11i
def ooOoooO ( url , name ) :
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 if ooOOoOoOoO00 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + O0OO0o + ' - CUSTOM FTV INI###'
  II1OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo0OooO0oOoO = os . path . join ( II1OO , 'addons2.ini' )
  I1iIIiI1i = ii111II . http_GET ( url ) . content
  ooO0o0o = open ( oo0OooO0oOoO , "w" )
  ooO0o0o . write ( I1iIIiI1i )
  ooO0o0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0OooO0oOoO ) + '    ==='
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "                               Done Adding New .ini File" )
 return
 if 57 - 57 : O0OOOoOoo0 * iI11I1II1I1I * Ii1IIIi1 * iI1ii11iIi1i / iI1ii11iIi1i
def iiiii ( url , name ) :
 ooOOoOoOoO00 = xbmcgui . Dialog ( )
 if ooOOoOoOoO00 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + O0OO0o + ' - CUSTOM FTV SETTINGS###'
  II1OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oo0OooO0oOoO = os . path . join ( II1OO , 'settings.xml' )
  I1iIIiI1i = ii111II . http_GET ( url ) . content
  ooO0o0o = open ( oo0OooO0oOoO , "w" )
  ooO0o0o . write ( I1iIIiI1i )
  ooO0o0o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oo0OooO0oOoO ) + '    ==='
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "                               Done Adding New Settings" )
 return
 if 57 - 57 : oO0oo0o / O00o0O00 / O00o0O00 * I11i * Ii1I - Ii
 if 82 - 82 : oOo0O0Ooo . oO0o
def iI1IIIOoO0O0O ( ) :
 try :
  IiI1IiI1Ii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IiI1IiI1Ii ) == True :
   ooOOoOoOoO00 = xbmcgui . Dialog ( )
   if ooOOoOoOoO00 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    Iii1i1I1iIi = os . path . join ( IiI1IiI1Ii , "source.db" )
    os . unlink ( Iii1i1I1iIi )
  ooOOoOoOoO00 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  ooOOoOoOoO00 = xbmcgui . Dialog ( )
  ooOOoOoOoO00 . ok ( O0OO0o , "               Error Deleting Database No Database To Delete" )
 return
 if 78 - 78 : ooOOOoO / Ii1IIIi1 * iI1ii11iIi1i . O00o0O00 . oO0oo0o - ii1ii11IIIiiI
 if 39 - 39 : O0OOOoOoo0 . ooOoO0O00 + ii . Ii1IIIi1 - Ii % ii1ii11IIIiiI
 if 38 - 38 : oO0oo0o
 if 9 - 9 : I11O0O0oOO00O00o . oO0o . oO0oo0o / ii
 if 59 - 59 : iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
def II1I1i ( url ) :
 iIi1ii = urllib2 . Request ( url )
 iIi1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 I1I11 = urllib2 . urlopen ( iIi1ii )
 I1iIIiI1i = I1I11 . read ( )
 I1I11 . close ( )
 return I1iIIiI1i
 if 2 - 2 : IIiIiII11i + I11O0O0oOO00O00o . oO0o
 if 14 - 14 : O00o0O00 * oOo0O0Ooo - Ii1I
 if 10 - 10 : Ii1IIIi1 % ii1ii11IIIiiI * Ii1I * o0o00Oo0O * Ii % ii1ii11IIIiiI
 if 68 - 68 : ii * OOooOOo
 if 9 - 9 : ii1ii11IIIiiI
 if 36 - 36 : ii1ii11IIIiiI / OOooOOo + OOooOOo * O0OOOoOoo0 / O00o0O00 * o0o00Oo0O
 if 17 - 17 : oO0o / O0OOOoOoo0 % oOo0O0Ooo
def o0oO00O000Oo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; I1I1ii1IiIIII = plugintools . message_yes_no ( O0OO0o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if I1I1ii1IiIIII :
  iiiOo00Oo = xbmcaddon . Addon ( id = OO0OOOoO0O0 ) . getAddonInfo ( 'path' ) ; iiiOo00Oo = xbmc . translatePath ( iiiOo00Oo ) ;
  i1IIIii11i = os . path . join ( iiiOo00Oo , ".." , ".." ) ; i1IIIii11i = os . path . abspath ( i1IIIii11i ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + i1IIIii11i ) ; oOo0 = False
  try :
   for i11IIi , oo0O00O0oO , IIIIi1iII in os . walk ( i1IIIii11i , topdown = True ) :
    oo0O00O0oO [ : ] = [ iIi1IIIi1Ii for iIi1IIIi1Ii in oo0O00O0oO if iIi1IIIi1Ii not in iIoo0 ]
    for I111iIii1i1 in IIIIi1iII :
     try : os . remove ( os . path . join ( i11IIi , I111iIii1i1 ) )
     except :
      if I111iIii1i1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oOo0 = True
      plugintools . log ( "Error removing " + i11IIi + " " + I111iIii1i1 )
    for I111iIii1i1 in oo0O00O0oO :
     try : os . rmdir ( os . path . join ( i11IIi , I111iIii1i1 ) )
     except :
      if I111iIii1i1 not in [ "Database" , "userdata" ] : oOo0 = True
      plugintools . log ( "Error removing " + i11IIi + " " + I111iIii1i1 )
   if not oOo0 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( O0OO0o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( O0OO0o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( O0OO0o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( O0OO0o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 O0o0oOo0OooO ( )
 if 43 - 43 : OOooOOo * oO0o % ooOoO0O00 * iI1ii11iIi1i + iI11I1II1I1I
 if 80 - 80 : I11i . Ii1IIIi1 . ii
 if 63 - 63 : O0OOOoOoo0 . O00o0O00
def oO0ooo ( ) :
 o0Ooi1 = [ ]
 IiiIOoo00OOO = sys . argv [ 2 ]
 if len ( IiiIOoo00OOO ) >= 2 :
  OOO0 = sys . argv [ 2 ]
  o00iIiIIi = OOO0 . replace ( '?' , '' )
  if ( OOO0 [ len ( OOO0 ) - 1 ] == '/' ) :
   OOO0 = OOO0 [ 0 : len ( OOO0 ) - 2 ]
  i1I1I = o00iIiIIi . split ( '&' )
  o0Ooi1 = { }
  for iII11I1iIiI in range ( len ( i1I1I ) ) :
   oOi111II11IIiii = { }
   oOi111II11IIiii = i1I1I [ iII11I1iIiI ] . split ( '=' )
   if ( len ( oOi111II11IIiii ) ) == 2 :
    o0Ooi1 [ oOi111II11IIiii [ 0 ] ] = oOi111II11IIiii [ 1 ]
    if 84 - 84 : OOooOOo - I11O0O0oOO00O00o
 return o0Ooi1
 if 80 - 80 : Ii % O00o0O00 - I1ii11iIi11i % O00o0O00
o0o0O00O0oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ii1Iii1iiI11 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o0O00 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O00ooO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oo00OO0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OO00Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IiIi1i = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iIiIi1III1iII = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
o0oO0IIii1iIIiiIIi = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oOOo0Ooo0oOOo = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
ooO0o0OO = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
I111I1I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
O000OOO00O0Oo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iI111i1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O00OOOOOo0O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i111iI1I = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i11IiIi = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i11IIi1III1II = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
ooOOoo0 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I1I1Ii1Iii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
IIi1i111 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oO00II = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
O0OIIiI1I1Ii1I = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iIIiiii = base64 . decodestring ( 'Q1VOVA==' )
def Ooooo0Oo0oOo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoo0OoooOo0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0o0O = [ ]
  if showcontext == 'fav' :
   O0o0O . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in oo0oO0oO00oO :
   O0o0O . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOoo0OoooOo0o . addContextMenuItems ( O0o0O )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = True )
 return Iii11i1111II
 if 63 - 63 : O00o0O00
def iII111I ( name , url , mode , iconimage , fanart , description ) :
 oOoo00OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Iii11i1111II = True
 oOoo0OoooOo0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOoo0OoooOo0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOoo0OoooOo0o . setProperty ( "Fanart_Image" , fanart )
 Iii11i1111II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoo00OO0 , listitem = oOoo0OoooOo0o , isFolder = False )
 return Iii11i1111II
 if 52 - 52 : iI11I1II1I1I * OOooOOo + I11i . I11O0O0oOO00O00o
 if 59 - 59 : Ii1IIIi1 . ooOoO0O00
OOO0 = oO0ooo ( )
i11iii1II1I1 = None
I111iIii1i1 = None
OOo000 = None
O0O00OOOo00O = None
i1I = None
O0ooOO0O00 = None
O0OooOOo0OOOO = None
if 82 - 82 : I11i * oO0o / ooOOOoO
if 5 - 5 : Ii1IIIi1 / oO0oo0o % O0OOOoOoo0 . Ii % OOooOOo + oO0oo0o
try :
 O0OooOOo0OOOO = int ( OOO0 [ "fav_mode" ] )
except :
 pass
 if 95 - 95 : Ii1I
try :
 i11iii1II1I1 = urllib . unquote_plus ( OOO0 [ "url" ] )
except :
 pass
try :
 I111iIii1i1 = urllib . unquote_plus ( OOO0 [ "name" ] )
except :
 pass
try :
 O0O00OOOo00O = urllib . unquote_plus ( OOO0 [ "iconimage" ] )
except :
 pass
try :
 OOo000 = int ( OOO0 [ "mode" ] )
except :
 pass
try :
 i1I = urllib . unquote_plus ( OOO0 [ "fanart" ] )
except :
 pass
try :
 O0ooOO0O00 = urllib . unquote_plus ( OOO0 [ "description" ] )
except :
 pass
 if 48 - 48 : I11O0O0oOO00O00o
 if 14 - 14 : iI11I1II1I1I / I11i * ooOOOoO
print str ( Oo0o ) + ': ' + str ( ii11III1 )
print "Mode: " + str ( OOo000 )
print "URL: " + str ( i11iii1II1I1 )
print "Name: " + str ( I111iIii1i1 )
print "IconImage: " + str ( O0O00OOOo00O )
if 35 - 35 : iI11I1II1I1I
if 34 - 34 : oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
def iiiiII1i1Iii1I1 ( content , viewType ) :
 if 30 - 30 : oOo0O0Ooo + oOo0O0Ooo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0OoO . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0OoO . getSetting ( viewType ) )
  if 75 - 75 : oOo0O0Ooo - O0OOOoOoo0 - oOo0O0Ooo % oO0oo0o % ii
if O0O00OOOo00O == None : O0O00OOOo00O = i1OOO00oO0O
if i1I == None : i1I = o00O0oOOo
if OOo000 == None :
 i1II1IiIIi ( )
 if 13 - 13 : O0OOOoOoo0 * oO0o % iI11I1II1I1I / ooOOOoO * Ii1IIIi1 . I1ii11iIi11i
elif OOo000 == 1 :
 o0Ooo0oOoo ( i11iii1II1I1 )
 if 23 - 23 : O0OOOoOoo0 / ooOOOoO . Ii1IIIi1 * iI1ii11iIi1i
elif OOo000 == 44 :
 O0OoO0O ( i11iii1II1I1 )
 if 87 - 87 : Ii
elif OOo000 == 2 :
 i1i1IIiIiI11 ( )
 if 34 - 34 : ooOoO0O00
elif OOo000 == 3 :
 OO0oOoO0O0 ( )
 if 64 - 64 : iI11I1II1I1I / ooOOOoO / I1ii11iIi11i - Ii1I
elif OOo000 == 21 :
 ooooO0 ( )
 if 100 - 100 : ooOOOoO + ooOoO0O00 * oO0o
elif OOo000 == 4 :
 iiiI1i ( )
 if 64 - 64 : oO0oo0o * Ii . I1ii11iIi11i
elif OOo000 == 5 :
 Iii1OO ( i11iii1II1I1 )
 if 52 - 52 : I1ii11iIi11i / O0OOOoOoo0 / Ii1IIIi1 - I11i / Ii1IIIi1
elif OOo000 == 6 :
 II1iiI1iIii1i ( i11iii1II1I1 )
 if 74 - 74 : ooOoO0O00 . iI11I1II1I1I
elif OOo000 == 7 :
 IIIIIi ( i11iii1II1I1 , I111iIii1i1 )
 if 85 - 85 : oOo0O0Ooo
elif OOo000 == 8 :
 O0oOO0Oo0O0O ( i11iii1II1I1 , I111iIii1i1 )
 if 10 - 10 : o0o00Oo0O . IIiIiII11i / ii
elif OOo000 == 9 :
 FIXREPOSADDONS ( i11iii1II1I1 )
 if 72 - 72 : ii . I11i + o0o00Oo0O
elif OOo000 == 10 :
 Ii1iii1 ( )
 if 46 - 46 : OOooOOo * I11O0O0oOO00O00o / oO0oo0o + I1ii11iIi11i + ooOOOoO
elif OOo000 == 11 :
 O000 ( i11iii1II1I1 )
 if 95 - 95 : I11i - iI1ii11iIi1i
elif OOo000 == 12 :
 OO0I11 ( )
 if 67 - 67 : Ii1I * I1ii11iIi11i % I11i
elif OOo000 == 13 :
 oOOoO0ii1I1Ii11 ( )
 if 19 - 19 : OOooOOo . O00o0O00 . ii
elif OOo000 == 14 :
 iiIi1I1IIIII1IIi ( i11iii1II1I1 )
 if 79 - 79 : O00o0O00 * O0OOOoOoo0 * oOo0O0Ooo * Ii1I / Ii1I
elif OOo000 == 15 :
 iiI1i111I1 ( )
 if 62 - 62 : O0OOOoOoo0 * iI1ii11iIi1i % Ii1I - ooOoO0O00 - Ii1I
elif OOo000 == 16 :
 ooOoooO ( i11iii1II1I1 , I111iIii1i1 )
 if 24 - 24 : O00o0O00
elif OOo000 == 17 :
 iiiii ( i11iii1II1I1 , I111iIii1i1 )
 if 71 - 71 : ooOOOoO - ooOoO0O00
elif OOo000 == 18 :
 iI1IIIOoO0O0O ( )
 if 56 - 56 : OOooOOo + oO0oo0o
elif OOo000 == 19 :
 IIo000o0O0000o ( i11iii1II1I1 )
 if 74 - 74 : Ii1IIIi1 / ii1ii11IIIiiI / IIiIiII11i - Ii1IIIi1 / oO0oo0o % I11O0O0oOO00O00o
elif OOo000 == 40 :
 ii1IIi ( I111iIii1i1 , i11iii1II1I1 , O0ooOO0O00 )
 if 19 - 19 : ooOOOoO % ii + ii
elif OOo000 == 42 :
 Iiii1iiIi ( I111iIii1i1 , i11iii1II1I1 , O0ooOO0O00 )
 if 7 - 7 : ooOoO0O00
elif OOo000 == 43 :
 O0OO0 ( i11iii1II1I1 )
 if 91 - 91 : OOooOOo - OOooOOo . ooOOOoO
elif OOo000 == 20 :
 I11Ii1I1I ( i11iii1II1I1 )
 if 33 - 33 : ii1ii11IIIiiI - iI11I1II1I1I / iI1ii11iIi1i % o0o00Oo0O
elif OOo000 == 22 :
 OOOoOOoo ( i11iii1II1I1 )
 if 80 - 80 : ooOOOoO % ii - ooOOOoO
elif OOo000 == 23 :
 II11I ( i11iii1II1I1 )
 if 27 - 27 : ii1ii11IIIiiI - I11i * Ii1I - oOo0O0Ooo
elif OOo000 == 24 :
 O0OOOo0 ( i11iii1II1I1 )
 if 22 - 22 : I1ii11iIi11i % ii - I1ii11iIi11i - Ii1IIIi1 . iI1ii11iIi1i
elif OOo000 == 25 :
 iI1iIiIIiIiiI ( i11iii1II1I1 )
 if 100 - 100 : IIiIiII11i / ii1ii11IIIiiI / Ii1IIIi1 - Ii1I * iI11I1II1I1I
elif OOo000 == 26 :
 ooOooo ( i11iii1II1I1 )
 if 7 - 7 : ooOoO0O00 . ooOOOoO % Ii * Ii1I . I11O0O0oOO00O00o % Ii1I
elif OOo000 == 27 :
 i11io00OOO00Oo ( i11iii1II1I1 )
 if 35 - 35 : oOo0O0Ooo
elif OOo000 == 28 :
 i1III ( i11iii1II1I1 )
 if 48 - 48 : ii % ii - oO0o . OOooOOo
elif OOo000 == 29 :
 OOOi1i1Iiii ( i11iii1II1I1 )
 if 22 - 22 : O0OOOoOoo0 . Ii . ii . ooOoO0O00
elif OOo000 == 30 :
 i1I11I1iIii ( i11iii1II1I1 )
 if 12 - 12 : OOooOOo % O00o0O00 + oO0oo0o . o0o00Oo0O % iI11I1II1I1I
elif OOo000 == 31 :
 iI1Ii1III ( i11iii1II1I1 )
 if 41 - 41 : ii
elif OOo000 == 32 :
 iiIi11i1I1 ( )
 if 13 - 13 : I11O0O0oOO00O00o + ii1ii11IIIiiI - ii1ii11IIIiiI % oO0oo0o / I11O0O0oOO00O00o
elif OOo000 == 33 :
 o0oo0000Oo ( )
 if 4 - 4 : oOo0O0Ooo + O00o0O00 - ooOOOoO + Ii1IIIi1
elif OOo000 == 35 :
 o0OOooo0ooo0o ( i11iii1II1I1 )
 if 78 - 78 : iI1ii11iIi1i
elif OOo000 == 34 :
 ii1I11 ( i11iii1II1I1 )
 if 29 - 29 : IIiIiII11i
elif OOo000 == 36 :
 o00O00 ( i11iii1II1I1 )
 if 79 - 79 : iI11I1II1I1I - Ii + O0OOOoOoo0 - IIiIiII11i . iI11I1II1I1I
elif OOo000 == 37 :
 O00oooOoO ( i11iii1II1I1 )
 if 84 - 84 : I1ii11iIi11i % I11O0O0oOO00O00o * o0o00Oo0O * I11O0O0oOO00O00o
elif OOo000 == 38 :
 Ii1oo0O0OO ( i11iii1II1I1 )
 if 66 - 66 : O00o0O00 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0OOOoOoo0
elif OOo000 == 41 :
 o0oO00O000Oo ( OOO0 )
 if 12 - 12 : I1ii11iIi11i + oOo0O0Ooo
elif OOo000 == 39 :
 OooOO ( i11iii1II1I1 )
 if 37 - 37 : ooOoO0O00 * Ii
elif OOo000 == 45 :
 TEXTS ( )
 if 95 - 95 : Ii % ii1ii11IIIiiI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif OOo000 == 46 :
 iIIIi1I ( )
 if 7 - 7 : oO0o * Ii * iI11I1II1I1I / O00o0O00 / ii1ii11IIIiiI
elif OOo000 == 47 :
 GEVID ( )
 if 35 - 35 : Ii1IIIi1 * O00o0O00
elif OOo000 == 48 :
 iI1IiI1 ( I111iIii1i1 , i11iii1II1I1 , O0ooOO0O00 )
 if 65 - 65 : IIiIiII11i % ooOoO0O00
elif OOo000 == 49 :
 O0OooO00O0 ( )
 if 13 - 13 : oO0o * ii1ii11IIIiiI + I1ii11iIi11i - ooOOOoO
elif OOo000 == 222 :
 Ii11 ( i11iii1II1I1 )
 if 31 - 31 : oO0o
elif OOo000 == 333 :
 oO0O0O00 ( i11iii1II1I1 )
 if 68 - 68 : oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77 : Ii - ii1ii11IIIiiI . Ii1I % I1ii11iIi11i . iI1ii11iIi1i
elif OOo000 == 1020 :
 o0Oo0OOoOOO000 ( )
 if 9 - 9 : I11i
elif OOo000 == 1021 :
 ANIMEEP ( )
 if 55 - 55 : O00o0O00 % iI11I1II1I1I + I11O0O0oOO00O00o . O0OOOoOoo0
elif OOo000 == 1022 :
 ANIMEPLAY ( i11iii1II1I1 )
 if 71 - 71 : Ii / ooOoO0O00 + OOooOOo
elif OOo000 == 1001 :
 I1IO0OO0oo ( )
 if 23 - 23 : Ii
elif OOo000 == 1005 :
 IiIiI1IiIi ( )
 if 88 - 88 : IIiIiII11i - Ii1IIIi1 / ii
elif OOo000 == 1007 :
 Ooo0O00o00 ( i11iii1II1I1 )
 if 71 - 71 : Ii1I
elif OOo000 == 1010 :
 O00ii111I ( i11iii1II1I1 )
 if 19 - 19 : I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OOo000 == 1011 :
 o00oOoO0oO0ooO0o0 ( i11iii1II1I1 )
 if 1 - 1 : ooOOOoO % ooOoO0O00
elif OOo000 == 1012 :
 Iii11i1 ( i11iii1II1I1 )
 if 41 - 41 : oO0o * oO0o / Ii1IIIi1 + Ii1I . I11i
elif OOo000 == 1030 :
 O0ooOo00o0oOO ( )
 if 84 - 84 : Ii + oO0o * oOo0O0Ooo + Ii1I / iI1ii11iIi1i
elif OOo000 == 1031 :
 I111iiiIiii1i ( i11iii1II1I1 , O0O00OOOo00O )
 if 80 - 80 : Ii1I
elif OOo000 == 1032 :
 iI11iiiii ( i11iii1II1I1 )
 if 67 - 67 : IIiIiII11i
elif OOo000 == 1006 :
 Parse . ParseURL ( i11iii1II1I1 )
 if 2 - 2 : I11i - o0o00Oo0O * iI1ii11iIi1i % ooOOOoO
elif OOo000 == 2030 :
 Parse . addonParseURL ( i11iii1II1I1 )
 if 64 - 64 : ooOoO0O00 . O0OOOoOoo0
elif OOo000 == 2031 :
 Parse . apkParseURL ( i11iii1II1I1 )
 if 7 - 7 : oO0oo0o . Ii1IIIi1 - Ii1IIIi1 / ii1ii11IIIiiI % I1ii11iIi11i
elif OOo000 == 1002 :
 OoOOo0O0oOoo ( i11iii1II1I1 )
 if 61 - 61 : oO0oo0o - Ii1I / Ii1IIIi1 % Ii1I + oO0o / I1ii11iIi11i
elif OOo000 == 1003 :
 oO0O0oOOoO ( i11iii1II1I1 , O0O00OOOo00O )
 if 10 - 10 : Ii / OOooOOo
elif OOo000 == 1004 :
 i1iIIiII11I ( i11iii1II1I1 )
 if 27 - 27 : oOo0O0Ooo / ii
elif OOo000 == 1008 :
 IIi111i1i1III ( )
 if 74 - 74 : Ii1I % ii1ii11IIIiiI - oO0o * I11O0O0oOO00O00o . ii * oO0o
elif OOo000 == 1009 :
 I1Ii1i111I ( i11iii1II1I1 )
 if 99 - 99 : OOooOOo . Ii1IIIi1 - ii - o0o00Oo0O
elif OOo000 == 2001 :
 IIIi11i1 ( )
 if 6 - 6 : O00o0O00
elif OOo000 == 2002 :
 I1IiiIi11iIi1 ( i11iii1II1I1 )
 if 3 - 3 : o0o00Oo0O - ii1ii11IIIiiI * iI1ii11iIi1i * O00o0O00 / iI1ii11iIi1i
elif OOo000 == 1013 :
 oooO00O0O0OOO ( )
elif OOo000 == 10111113 :
 I1iIiIi111 ( i11iii1II1I1 )
 if 58 - 58 : iI1ii11iIi1i * iI11I1II1I1I + O0OOOoOoo0 . O0OOOoOoo0
elif OOo000 == 1014 :
 iiI1oOo00O ( )
 if 74 - 74 : O0OOOoOoo0 - I11i * ooOOOoO % O0OOOoOoo0
elif OOo000 == 1015 :
 IiIIIi11 ( i11iii1II1I1 )
 if 93 - 93 : iI11I1II1I1I / OOooOOo % I1ii11iIi11i * ii1ii11IIIiiI - oO0o - I11i
elif OOo000 == 1016 :
 OO0OOO ( i11iii1II1I1 , O0O00OOOo00O , I111iIii1i1 )
 if 44 - 44 : ii
elif OOo000 == 1017 :
 O0oo0ooO ( )
 if 82 - 82 : OOooOOo . OOooOOo
elif OOo000 == 1018 :
 oo0Oooo0O ( i11iii1II1I1 )
 if 10 - 10 : I1ii11iIi11i * Ii1I . oO0oo0o . ii . O00o0O00 * Ii1I
elif OOo000 == 1023 :
 i1I1ii1iI1 ( )
 if 80 - 80 : ii1ii11IIIiiI + I11O0O0oOO00O00o . ii1ii11IIIiiI + O00o0O00
elif OOo000 == 1024 :
 O00oO00Oooo0O ( i11iii1II1I1 )
 if 85 - 85 : Ii . I11O0O0oOO00O00o + iI1ii11iIi1i / iI1ii11iIi1i
elif OOo000 == 1025 :
 iIi11IiII11 ( i11iii1II1I1 )
 if 43 - 43 : ooOOOoO . ii - IIiIiII11i
elif OOo000 == 4001 :
 OOOo0OO0ooO0O0O ( )
 if 90 - 90 : oOo0O0Ooo - iI11I1II1I1I + Ii1I * O00o0O00 * oO0oo0o
elif OOo000 == 4002 :
 oO00O ( )
 if 19 - 19 : ii1ii11IIIiiI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OOo000 == 4003 :
 IIIII1iII1 ( )
 if 27 - 27 : OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OOo000 == 4004 :
 ooooooO0o00 ( )
 if 15 - 15 : iI1ii11iIi1i + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OOo000 == 4005 :
 oO000oOo0oO0 ( )
 if 54 - 54 : ooOOOoO - IIiIiII11i . O0OOOoOoo0 + iI1ii11iIi1i
elif OOo000 == 4006 :
 IIIiiii1 ( )
 if 45 - 45 : oO0oo0o + IIiIiII11i . Ii1IIIi1 / Ii1I
elif OOo000 == 4007 :
 ii1i1 ( )
 if 76 - 76 : iI1ii11iIi1i + Ii1IIIi1 - ooOOOoO * iI11I1II1I1I % ooOoO0O00
elif OOo000 == 4008 :
 IIII1I11Ii11 ( )
 if 72 - 72 : O0OOOoOoo0 + IIiIiII11i . o0o00Oo0O - Ii1IIIi1 / ii . ii1ii11IIIiiI
elif OOo000 == 4009 : Oo00o00O00 ( )
elif OOo000 == 4010 : iI1IiI11Ii11i ( )
elif OOo000 == 3000 :
 o00o0O0oo ( )
 if 28 - 28 : iI11I1II1I1I . o0o00Oo0O
elif OOo000 == 3001 :
 O0oOOOO0o ( )
 if 32 - 32 : ii
elif OOo000 == 3002 :
 OoOOO0 ( i11iii1II1I1 )
 if 29 - 29 : Ii1I
elif OOo000 == 3003 :
 IiIio0oO0O ( i11iii1II1I1 )
 if 41 - 41 : iI1ii11iIi1i
elif OOo000 == 3004 :
 oOo00OoooOoo ( i11iii1II1I1 )
 if 49 - 49 : iI1ii11iIi1i % IIiIiII11i . iI1ii11iIi1i - I11i - I11O0O0oOO00O00o * ooOOOoO
elif OOo000 == 404 :
 oooo0OOoo0oO ( I111iIii1i1 , i11iii1II1I1 , O0O00OOOo00O )
 if 47 - 47 : o0o00Oo0O . I11i / iI1ii11iIi1i * Ii1IIIi1
elif OOo000 == 405 :
 i1iIIII11I ( i11iii1II1I1 )
 if 63 - 63 : ii1ii11IIIiiI - oO0oo0o - Ii1IIIi1 - O0OOOoOoo0 / oO0oo0o + oO0o
elif OOo000 == 7030 :
 o0ooO0OO ( )
 if 94 - 94 : ooOOOoO / oOo0O0Ooo . IIiIiII11i
elif OOo000 == 7021 :
 I1IiI1i1Iii ( I111iIii1i1 )
 if 32 - 32 : oO0oo0o . O00o0O00 % O00o0O00 . OOooOOo
elif OOo000 == 7022 :
 ii1IIIiIII ( I111iIii1i1 )
 if 37 - 37 : O00o0O00 + o0o00Oo0O + O00o0O00 . Ii1IIIi1 . I11i
elif OOo000 == 7000 :
 oooooO0oOO00oOo ( I111iIii1i1 , i11iii1II1I1 , img )
 if 78 - 78 : oOo0O0Ooo / I11O0O0oOO00O00o + I11i . I1ii11iIi11i / o0o00Oo0O
elif OOo000 == 7050 :
 O00oOo ( i11iii1II1I1 )
 if 49 - 49 : Ii1I
elif OOo000 == 7051 :
 Ii1Ii1ii ( i11iii1II1I1 )
 if 66 - 66 : I11i . Ii1I
elif OOo000 == 7052 :
 ii11iIIi1i ( i11iii1II1I1 )
 if 18 - 18 : I1ii11iIi11i + ooOOOoO
elif OOo000 == 7053 :
 oOOooO00oOo00 ( i11iii1II1I1 )
 if 79 - 79 : oO0o - o0o00Oo0O + IIiIiII11i % iI1ii11iIi1i . oOo0O0Ooo
elif OOo000 == 7054 :
 CoolPlay ( i11iii1II1I1 )
 if 43 - 43 : oOo0O0Ooo % Ii1I * iI1ii11iIi1i
elif OOo000 == 7060 :
 O0O00ooO0O0O ( )
 if 31 - 31 : iI1ii11iIi1i / Ii1IIIi1
elif OOo000 == 7061 :
 Ooo0o0OoOO ( i11iii1II1I1 )
 if 3 - 3 : ooOOOoO
elif OOo000 == 7063 :
 Iiii1II ( i11iii1II1I1 )
 if 37 - 37 : iI1ii11iIi1i * ii * I11O0O0oOO00O00o + I1ii11iIi11i . oOo0O0Ooo
elif OOo000 == 7062 :
 i1IiI1i1iI1Ii ( i11iii1II1I1 )
 if 61 - 61 : O00o0O00 . O00o0O00
elif OOo000 == 7064 :
 NATatozcat ( )
 if 17 - 17 : IIiIiII11i / O0OOOoOoo0
elif OOo000 == 7067 :
 O00OiIIII1iiIII ( i11iii1II1I1 )
 if 80 - 80 : O00o0O00 * oO0o + iI1ii11iIi1i
elif OOo000 == 7066 :
 NATatozA ( i11iii1II1I1 )
 if 62 - 62 : ii . o0o00Oo0O % I1ii11iIi11i
elif OOo000 == 7065 :
 OO0oO ( i11iii1II1I1 )
 if 98 - 98 : I11i * I1ii11iIi11i - iI1ii11iIi1i . O0OOOoOoo0
elif OOo000 == 7070 :
 oo0oo00OooOO ( )
 if 2 - 2 : I1ii11iIi11i - O0OOOoOoo0 % iI11I1II1I1I
elif OOo000 == 7071 :
 DIZIlist ( i11iii1II1I1 )
 if 88 - 88 : ii1ii11IIIiiI - oO0o
elif OOo000 == 7072 :
 DIZIpull ( i11iii1II1I1 )
 if 79 - 79 : Ii1IIIi1
elif OOo000 == 7073 :
 WATCHDIZI ( i11iii1II1I1 )
 if 45 - 45 : IIiIiII11i + Ii1IIIi1 . I11O0O0oOO00O00o . o0o00Oo0O * ooOoO0O00 - iI1ii11iIi1i
elif OOo000 == 7002 :
 ooII11iI1i ( )
 if 48 - 48 : Ii1I + I1ii11iIi11i
elif OOo000 == 7003 :
 o0Ii11I ( i11iii1II1I1 )
 if 76 - 76 : Ii1I
elif OOo000 == 7004 :
 I1iI1i ( i11iii1II1I1 )
 if 98 - 98 : IIiIiII11i + oOo0O0Ooo - Ii1I . iI1ii11iIi1i
elif OOo000 == 7020 :
 o0o00OOoo ( i11iii1II1I1 )
 if 51 - 51 : iI1ii11iIi1i + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OOo000 == 7001 :
 Ii1111i ( )
 if 20 - 20 : ii1ii11IIIiiI . I11O0O0oOO00O00o . iI1ii11iIi1i + I11O0O0oOO00O00o - O00o0O00 * oO0oo0o
elif OOo000 == 7010 :
 i1iiIiI ( i11iii1II1I1 )
 if 82 - 82 : oO0o
elif OOo000 == 7011 :
 IIii ( i11iii1II1I1 )
 if 78 - 78 : IIiIiII11i / I11O0O0oOO00O00o - Ii + Ii1I * I1ii11iIi11i
elif OOo000 == 7012 :
 iiiiIIiIIII ( i11iii1II1I1 )
 if 17 - 17 : OOooOOo
elif OOo000 == 7013 :
 cnfTVPlay2 ( i11iii1II1I1 )
elif OOo000 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( i11iii1II1I1 )
elif OOo000 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( i11iii1II1I1 )
elif OOo000 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I111iIii1i1 , i11iii1II1I1 , O0O00OOOo00O )
elif OOo000 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOo000 == 7018 :
 i1i1IiiI11i ( )
elif OOo000 == 7019 :
 CNF_Studio_Indexer . List_Movies ( i11iii1II1I1 )
elif OOo000 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( i11iii1II1I1 )
elif OOo000 == 7024 :
 CNF_Studio_Indexer . Box_Office ( i11iii1II1I1 )
 if 72 - 72 : Ii1IIIi1 . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OOo000 == 8000 :
 Ii1i1I ( )
elif OOo000 == 8001 :
 IIi1ii1I11II1 ( )
elif OOo000 == 8002 :
 III11I1i ( )
elif OOo000 == 8003 :
 O0O00o0Ooo0O0 ( )
elif OOo000 == 8004 :
 OoO0oIiii1I ( )
elif OOo000 == 8005 :
 o000000 ( )
elif OOo000 == 8006 :
 o0O0OO ( I111iIii1i1 , i11iii1II1I1 )
elif OOo000 == 8030 :
 II1ii1I11 ( i11iii1II1I1 )
elif OOo000 == 8045 :
 iIiII ( i11iii1II1I1 )
elif OOo000 == 8046 :
 IIi1i1i1iii ( i11iii1II1I1 )
elif OOo000 == 8047 :
 III11ii ( i11iii1II1I1 )
elif OOo000 == 8048 :
 i1i1111I11II ( i11iii1II1I1 )
elif OOo000 == 8049 :
 O00O00 ( i11iii1II1I1 )
elif OOo000 == 804900 :
 i1I1iiIiII11 ( i11iii1II1I1 )
elif OOo000 == 8020 :
 oo0o00oOo0 ( )
elif OOo000 == 8021 :
 OoooO0 ( i11iii1II1I1 )
elif OOo000 == 8022 :
 i1IOo0 ( i11iii1II1I1 )
elif OOo000 == 8023 :
 OoOo0Oo0 ( i11iii1II1I1 )
elif OOo000 == 8040 :
 oo0oOooo0O ( )
elif OOo000 == 8041 :
 I1i1ii ( i11iii1II1I1 )
elif OOo000 == 8042 :
 ii1iIiIIiIIii ( i11iii1II1I1 )
elif OOo000 == 8043 :
 yt . PlayVideo ( i11iii1II1I1 )
elif OOo000 == 8044 :
 ooooo ( i11iii1II1I1 )
elif OOo000 == 8060 :
 O0OOo00Ooo00 ( )
elif OOo000 == 8061 :
 IiiiiiiiI1i11 ( i11iii1II1I1 )
elif OOo000 == 8064 :
 Ii1i1i ( )
elif OOo000 == 8065 :
 i1IIi ( i11iii1II1I1 )
elif OOo000 == 8070 :
 O0Ooo ( )
elif OOo000 == 8071 :
 OoO00OOOoOOo ( i11iii1II1I1 )
elif OOo000 == 7080 :
 oOOo0oOoooO0o ( i11iii1II1I1 )
elif OOo000 == 8090 :
 OooO0O0o0 ( )
elif OOo000 == 8091 :
 IiiOo0o0Oo0O0 ( i11iii1II1I1 )
elif OOo000 == 8092 :
 IIiIIiiiiI ( i11iii1II1I1 )
elif OOo000 == 8093 :
 Oo0OoO00O ( i11iii1II1I1 )
elif OOo000 == 8081 :
 iIIIIi ( )
elif OOo000 == 8062 :
 I1OO0Oo0 ( i11iii1II1I1 )
elif OOo000 == 8063 :
 iIIii111i1 ( i11iii1II1I1 )
elif OOo000 == 8050 :
 OO0o0oo ( )
elif OOo000 == 8051 :
 o00I11II1iI ( i11iii1II1I1 )
elif OOo000 == 8052 :
 i1Ooo0O0OO0OOo ( i11iii1II1I1 )
elif OOo000 == 8085 :
 I111ii11I ( )
elif OOo000 == 8086 :
 iiiIIII1Ii1 ( i11iii1II1I1 )
elif OOo000 == 8087 :
 o0Oo00OoO000O ( i11iii1II1I1 )
elif OOo000 == 8088 :
 II1iii ( i11iii1II1I1 , I111iIii1i1 )
elif OOo000 == 9000 :
 OoI1Ii ( )
elif OOo000 == 1111 :
 i1I1IIi1iI ( )
elif OOo000 == 9001 :
 IiiiiI1iIi ( )
elif OOo000 == 9002 :
 I1I1Ii111 ( )
elif OOo000 == 9003 :
 Ooi1I11i1 ( )
elif OOo000 == 9004 :
 World1 ( )
elif OOo000 == 9005 :
 World2 ( i11iii1II1I1 )
elif OOo000 == 9006 :
 World3 ( i11iii1II1I1 )
elif OOo000 == 9007 :
 IiiiIIi111Ii1 ( )
elif OOo000 == 9008 :
 O00OOO0OO ( i11iii1II1I1 )
elif OOo000 == 9009 :
 iII1ii1iiI1 ( i11iii1II1I1 )
elif OOo000 == 9010 :
 ii1iiii1I ( )
elif OOo000 == 9011 :
 O0O0ii1IiIiI1 ( i11iii1II1I1 )
elif OOo000 == 50 :
 ooOo00OOo0 ( i11iii1II1I1 )
elif OOo000 == 9020 :
 champlist ( )
elif OOo000 == 9021 :
 ii11IoOo0O0Oo ( )
elif OOo000 == 9022 :
 o0OO ( )
elif OOo000 == 9023 :
 I11ii1 ( )
elif OOo000 == 9024 :
 iI1iI ( i11iii1II1I1 )
elif OOo000 == 9030 :
 o000OOooO0O ( i11iii1II1I1 )
elif OOo000 == 9031 :
 IIi1iIiII1iiiI11 ( i11iii1II1I1 )
elif OOo000 == 9032 :
 Ooo0ooo0OOo ( i11iii1II1I1 )
elif OOo000 == 9033 :
 oo0o0oOO ( i11iii1II1I1 )
elif OOo000 == 9034 :
 OooOoOoo0ooo0 ( )
elif OOo000 == 7085 :
 I1I1I1Ii1iI ( i11iii1II1I1 )
elif OOo000 == 7086 :
 OoOoOO0ooo0o0 ( i11iii1II1I1 )
elif OOo000 == 7087 :
 IIi1iiIii1Ii ( O0ooOO0O00 )
elif OOo000 == 9666 :
 i1iIiiii ( i11iii1II1I1 )
elif OOo000 == 10100 : IiIIooOoo0 ( )
elif OOo000 == 10105 : I1oo0O0Ooo0O00 ( i11iii1II1I1 )
elif OOo000 == 10106 : oO0OOOOo ( i11iii1II1I1 )
elif OOo000 == 10104 : oooO0OOo0 ( i11iii1II1I1 )
elif OOo000 == 10107 : iiIiI111Ii1 ( )
elif OOo000 == 10103 : iii1II1iI1III ( i11iii1II1I1 )
elif OOo000 == 10108 : IIiiI1iiI ( i11iii1II1I1 )
elif OOo000 == 10107 : iiIiI111Ii1 ( )
elif OOo000 == 10000 : Origin_Menu ( )
elif OOo000 == 10001 : OOoooOO0o ( )
elif OOo000 == 10002 : I1Ii1 ( )
elif OOo000 == 10003 : I1oO ( )
elif OOo000 == 10004 : iIiI ( i11iii1II1I1 )
elif OOo000 == 10005 : O00oo0Ooo ( )
elif OOo000 == 10006 : iIi1Iii ( i11iii1II1I1 )
elif OOo000 == 10007 : iIii1111Ii1I1 ( i11iii1II1I1 , O0O00OOOo00O )
elif OOo000 == 10008 : o0ooiiII ( )
elif OOo000 == 10009 : OOo0o ( )
elif OOo000 == 10010 : iII1 ( i11iii1II1I1 )
elif OOo000 == 10011 : oo0ooo0OOO ( i11iii1II1I1 )
elif OOo000 == 10012 : IIIIi1I ( i11iii1II1I1 )
elif OOo000 == 10109 : i111I ( i11iii1II1I1 )
elif OOo000 == 10013 : I1iiiiii ( i11iii1II1I1 )
elif OOo000 == 10014 : IIi1Ii1I ( )
elif OOo000 == 10015 : iiIioo0O0 ( )
elif OOo000 == 10016 : Ii1i1i11I ( i11iii1II1I1 )
elif OOo000 == 10017 : Oo0o0O0oO0o ( )
elif OOo000 == 10018 : O0O0O0OoO0o0OO ( )
elif OOo000 == 10019 : IiIIi ( )
elif OOo000 == 10020 : Oo0o0O0OO0 ( )
elif OOo000 == 10021 : iii1Io0OOOooo ( )
elif OOo000 == 10022 : IiIIiIiI1ii ( i11iii1II1I1 )
elif OOo000 == 10023 : OOooOOO ( I111iIii1i1 , i11iii1II1I1 )
elif OOo000 == 10024 : O0OoooO ( i11iii1II1I1 )
elif OOo000 == 10025 : OoooOoOo ( )
elif OOo000 == 10026 : i1iiIIiIi1 ( )
elif OOo000 == 10027 : IiI1111i1i11I ( )
elif OOo000 == 10028 : i1iI1Iii11Iii11 ( )
elif OOo000 == 10029 : iI1iIIiIi1I1 ( )
elif OOo000 == 423 : II1IiiI ( i11iii1II1I1 )
elif OOo000 == 426 : oOo0oO0 ( i11iii1II1I1 )
elif OOo000 == 10030 : Izle_Films ( )
elif OOo000 == 10031 : Latest_Izle_Movies ( )
elif OOo000 == 10032 : Izle_Genres ( )
elif OOo000 == 10033 : Izle_Pop_Movies ( )
elif OOo000 == 10034 : Izle_Boxsets ( )
elif OOo000 == 10035 : Izle_Search ( )
elif OOo000 == 10036 : Izle_Genres_Movie ( i11iii1II1I1 )
elif OOo000 == 10037 : Izle_Boxset_single ( i11iii1II1I1 )
elif OOo000 == 10038 : Izle_IFRAME ( )
elif OOo000 == 10039 : Izle_Boxsets_Next ( i11iii1II1I1 )
elif OOo000 == 10040 : I11I1i1I ( )
elif OOo000 == 10041 : i11I1IIII ( i11iii1II1I1 )
elif OOo000 == 10042 : IiiIiIiIIIii1 ( i11iii1II1I1 )
elif OOo000 == 10043 : O00Oo0O ( )
elif OOo000 == 10044 : O0ooOOo0 ( i11iii1II1I1 )
elif OOo000 == 10045 : ii1iiiI ( I111iIii1i1 )
elif OOo000 == 10046 : O0oOO0O000O0 ( i11iii1II1I1 )
elif OOo000 == 10047 : i11IIiIi ( i11iii1II1I1 )
elif OOo000 == 10048 : oOI11Ii1 ( i11iii1II1I1 )
elif OOo000 == 10049 : iII111Ii ( i11iii1II1I1 )
elif OOo000 == 10050 : II1ioOO0Oo ( )
elif OOo000 == 10051 : O0ooO0 ( )
elif OOo000 == 10052 : iii11IiiiI ( )
elif OOo000 == 10053 : Addon ( i11iii1II1I1 )
elif OOo000 == 10054 : II11I111 ( i11iii1II1I1 , I111iIii1i1 )
elif OOo000 == 10055 :
 oOoooOOO0o0 ( "addFavorite" )
 try :
  I111iIii1i1 = I111iIii1i1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I111iIii1i1 = I111iIii1i1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 i11iII1Ii1ii111 ( I111iIii1i1 , i11iii1II1I1 , O0O00OOOo00O , i1I , O0OooOOo0OOOO )
elif OOo000 == 10056 :
 oOoooOOO0o0 ( "rmFavorite" )
 try :
  I111iIii1i1 = I111iIii1i1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I111iIii1i1 = I111iIii1i1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1III1ii1 ( I111iIii1i1 )
elif OOo000 == 10057 :
 oOoooOOO0o0 ( "getFavorites" )
 ooOoOo ( )
elif OOo000 == 10058 : OOOoOO ( )
elif OOo000 == 10059 : Donators_Guide ( )
elif OOo000 == 10060 : I11iiI1 ( )
elif OOo000 == 10061 : i11i11iiIiIiI ( )
elif OOo000 == 10062 : oo0OOO0O0 ( I111iIii1i1 , i11iii1II1I1 , O0ooOO0O00 )
elif OOo000 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + oOO00o0oooOo0 + ")" )
elif OOo000 == 10064 : I1iOO000o0o0oo ( )
elif OOo000 == 10065 : oO0o0O ( i11iii1II1I1 )
elif OOo000 == 10066 : Oooo0OOo0O0o ( i11iii1II1I1 )
elif OOo000 == 10068 : iIiiiIII1II ( i11iii1II1I1 )
elif OOo000 == 10069 : iiiI11I ( i11iii1II1I1 )
elif OOo000 == 10070 : IIIi1IIiI ( i11iii1II1I1 )
elif OOo000 == 10071 : Genie_Watch ( )
elif OOo000 == 10072 : iII1iIIIIII ( )
elif OOo000 == 10073 : I1ii11iiIIi ( i11iii1II1I1 )
elif OOo000 == 10074 : o0Ooo0 ( i11iii1II1I1 )
elif OOo000 == 10075 : iii1I1ii1 ( O0O00OOOo00O , I111iIii1i1 , i11iii1II1I1 )
elif OOo000 == 10076 : Iii1iii11 ( i11iii1II1I1 )
elif OOo000 == 10077 : o00o000 ( i11iii1II1I1 )
elif OOo000 == 10078 : IIIIII11iIiI1III ( )
elif OOo000 == 10079 : Genie_Watch_Tv_Shows ( )
elif OOo000 == 10080 : Genie_Watch_Tv_Genre ( i11iii1II1I1 )
elif OOo000 == 10081 : Genie_Watch_TV_PlayRun ( i11iii1II1I1 )
elif OOo000 == 10082 : Genie_Watch_TV_Episodes ( i11iii1II1I1 , O0O00OOOo00O )
elif OOo000 == 10083 : Genie_Watch_Tv_Recent ( i11iii1II1I1 )
elif OOo000 == 10084 : oOO0o0OO ( )
elif OOo000 == 10085 : I1111iii1ii11 ( )
elif OOo000 == 10086 : i11i11Iii ( )
elif OOo000 == 20000 : o000ooOo0o0Oo ( )
elif OOo000 == 20001 : o0OO0II111Iiii1 ( )
elif OOo000 == 20002 : iIiIII1Ii ( i11iii1II1I1 )
elif OOo000 == 20003 : O0oOo ( i11iii1II1I1 )
elif OOo000 == 20004 : iIII1Ii1 ( i11iii1II1I1 )
elif OOo000 == 21004 : ooOOO000 ( )
elif OOo000 == 21005 : O0OoO ( i11iii1II1I1 )
elif OOo000 == 21006 : iI11II ( i11iii1II1I1 )
elif OOo000 == 21007 : o0Oo0Ooo ( i11iii1II1I1 )
elif OOo000 == 30000 : i111ii11I1 ( )
elif OOo000 == 30001 : I11I1 ( )
elif OOo000 == 10012 : Resolve ( i11iii1II1I1 )
elif OOo000 == 30003 : IIii1iIIiII ( )
elif OOo000 == 30004 : i11i1IIOO0o ( i11iii1II1I1 )
elif OOo000 == 30005 : oo00oO ( i11iii1II1I1 )
elif OOo000 == 30006 : O000o0Ooo ( )
elif OOo000 == 30007 : OOOOoo ( )
elif OOo000 == 30008 : ooO00oOOo ( i11iii1II1I1 )
elif OOo000 == 30009 : o0oOI1 ( i11iii1II1I1 )
elif OOo000 == 30010 : II11iiii ( i11iii1II1I1 )
elif OOo000 == 30011 : O00Iii1IIiIi ( )
elif OOo000 == 30012 : OooOo0o ( )
elif OOo000 == 30013 : iiI1iii1I111 ( )
elif OOo000 == 30014 : iII1I11ii1III ( )
elif OOo000 == 30015 : OoOoo00O00oOOO ( i11iii1II1I1 , O0O00OOOo00O , i1I )
elif OOo000 == 30016 : OoooOOOoO0 ( i11iii1II1I1 )
elif OOo000 == 30019 : OO0oO0o0oOO ( i11iii1II1I1 )
elif OOo000 == 30017 : iI1III11IIi11Ii11 ( i11iii1II1I1 )
elif OOo000 == 30018 : oOoOo0O00Oo ( i11iii1II1I1 )
elif OOo000 == 30030 : OOooOOooo000OoO ( )
elif OOo000 == 30031 : O0OOo ( )
elif OOo000 == 30032 : oooOO0O ( )
elif OOo000 == 30033 : oOOOoo00o0 ( )
elif OOo000 == 30034 : oo0oO ( )
elif OOo000 == 30035 : ooO00O ( i11iii1II1I1 )
elif OOo000 == 30036 : Oo0OoooOoO0O0 ( i11iii1II1I1 )
elif OOo000 == 30037 : iIi1iOoo ( i11iii1II1I1 )
elif OOo000 == 30038 : IIiiiIooooO0OOo0o0 ( )
elif OOo000 == 30039 : I1II1oooOooOO ( )
elif OOo000 == 50000 : OoOO00OO0 ( )
elif OOo000 == 50001 : o0OoO0 ( )
elif OOo000 == 50002 : O000ooo ( i11iii1II1I1 )
elif OOo000 == 50003 : OOO0o0OO ( O0ooOO0O00 )
elif OOo000 == 60000 : o0OoO . openSettings ( sys . argv [ 0 ] )
elif OOo000 == 60001 : O0oi1IiI1I ( )
elif OOo000 == 60002 : O000000oooOOo ( I111iIii1i1 )
elif OOo000 == 60003 : O00OOoOo0 ( I111iIii1i1 )
elif OOo000 == 50004 : IiiiiI11iii11iI ( )
elif OOo000 == 50005 : speedtest . runtest ( i11iii1II1I1 )
elif OOo000 == 70001 : I1I1iI ( )
elif OOo000 == 70002 : ii1IiIiIi ( i11iii1II1I1 )
elif OOo000 == 70003 : OoO0OoOOOO ( i11iii1II1I1 )
elif OOo000 == 70004 : I1iII1IiI11i ( i11iii1II1I1 )
elif OOo000 == 70005 : OOOoO ( i11iii1II1I1 )
elif OOo000 == 70006 : ooOO0O0OooO0 ( )
elif OOo000 == 50006 : i11i1IiIi11 ( O0OO0o , iII11iiI1i11I )
elif OOo000 == 80000 : O0o0oOo0OooO ( )
elif OOo000 == 80001 : resolvefilmon ( i11iii1II1I1 )
elif OOo000 == 80002 : O0Oo0Oo000 ( )
elif OOo000 == 80003 : OOOO0oo0o0O ( I111iIii1i1 , i11iii1II1I1 )
elif OOo000 == 80004 : Iiii1ii ( I111iIii1i1 , i11iii1II1I1 )
elif OOo000 == 80005 : O000o0O0 ( )
elif OOo000 == 80006 : O0000oOoO0o0 ( i11iii1II1I1 )
elif OOo000 == 80007 : o000o0O ( i11iii1II1I1 )
elif OOo000 == 80008 : I1III ( )
elif OOo000 == 80009 : i1i1i1IiiiIi1 ( )
elif OOo000 == 80010 : ooo00OO ( i11iii1II1I1 )
elif OOo000 == 80011 : iI1iIIIiIi ( i11iii1II1I1 )
elif OOo000 == 80012 : IiI1IioOo00OOOoo0 ( )
if 64 - 64 : oO0oo0o
if 80 - 80 : I11i % iI11I1II1I1I
if 63 - 63 : ooOOOoO * Ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
if 47 - 47: Ii1I / iI11I1II1I1I % OOooOOo / I11O0O0oOO00O00o / iI1ii11iIi1i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
