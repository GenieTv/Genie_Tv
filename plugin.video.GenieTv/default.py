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
IiiIII111iI = "3.0.7"
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
i11 = Net ( )
I11 = xbmcgui . Dialog ( )
Oo0o0000o0o0 = base64 . decodestring
oOo0oooo00o = oo00 . getSetting ( 'Build' )
oO0o0o0ooO0oO = oo00 . getSetting ( 'Local' )
oo0o0O00 = oo00 . getSetting ( 'Remote' )
oO = oo00 . getSetting ( 'LocalM3u' )
i1iiIIiiI111 = oo00 . getSetting ( 'TEXTCOL' )
oooOOOOO = xbmc . translatePath ( 'special://logpath/' )
i1iiIII111ii = oo00 . getSetting ( 'User' )
i1iIIi1 = oo00 . getSetting ( 'Pass' )
ii11iIi1I = oo00 . getSetting ( 'AdultPass' )
iI111I11I1I1 = xbmcgui . Dialog ( )
OOooO0OOoo = xbmc . translatePath ( 'special://home/' )
iIii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
oOOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
O0OoO000O0OO = ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
iiI1IiI = xbmc . translatePath ( 'special://database' )
II = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
ooOoOoo0O = xbmc . translatePath ( 'special://thumbnails' ) ;
OooO0 = "GenieTv"
II11iiii1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
OO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
Ooo = 'http://'
O0o0Oo = base64 . decodestring ( 'LnBocA==' )
Oo00OOOOO = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
O0O = [ ]
O00o0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
I11i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
iIi1ii1I1 = oo00 . getLocalizedString
o0 = CookieJar ( )
I11II1i = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( o0 ) )
I11II1i . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
IIIII = int ( sys . argv [ 1 ] )
ooooooO0oo = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
IIiiiiiiIi1I1 = os . path . join ( II , 'favorites' )
I1IIIii = II + '/addons.ini'
oOoOooOo0o0 = xbmc . translatePath ( 'special://home/userdata/' )
OOOO = xbmc . translatePath ( 'special://home/userdatabroke/' )
OOO00 = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
iiiiiIIii = xbmc . translatePath ( 'special://home/userdata/addon_data' )
O000OO0 = iiiiiIIii + 'GenieTvWatched'
if not os . path . exists ( O000OO0 ) :
 os . makedirs ( O000OO0 )
I11iii1Ii = O000OO0 + 'watched.txt'
if not os . path . exists ( I11iii1Ii ) :
 open ( I11iii1Ii , 'w+' )
I1IIiiIiii = open ( I11iii1Ii ) . read ( )
O000oo0O = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
OOOOi11i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
IIIii1II1II = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
i1I1iI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
oo0OooOOo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
o0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( IIiiiiiiIi1I1 ) == True :
 O00oO = open ( IIiiiiiiIi1I1 ) . read ( )
else : O00oO = [ ]
I11i1I1I = oo00 . getSetting ( 'debug' )
if os . path . exists ( II ) == False :
 os . makedirs ( II )
def oO0Oo ( url ) :
 oOOoo0Oo = urllib2 . Request ( url )
 oOOoo0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o00OO00OoO = ''
 OOOO0OOoO0O0 = ''
 try :
  o00OO00OoO = urllib2 . urlopen ( oOOoo0Oo )
  OOOO0OOoO0O0 = o00OO00OoO . read ( )
  o00OO00OoO . close ( )
 except : pass
 if OOOO0OOoO0O0 != '' :
  return OOOO0OOoO0O0
 else :
  OOOO0OOoO0O0 = 'Failed'
  return OOOO0OOoO0O0
  if 65 - 65: o000o * O0OoO0O00o0oO . Ooo0Oo0oOoo . OoOOOOOo0o . iI1i1IiI + OO
I1III = [ ]
OO0O0OoOO0 = oO0Oo ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if OO0O0OoOO0 != 'Failed' :
 I1III . append ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not OO0O0OoOO0 != 'Failed' :
 iiiI1I11i1 = oO0Oo ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if iiiI1I11i1 != 'Failed' :
  I1III . append ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not iiiI1I11i1 != 'Failed' :
  IIi1i11111 = oO0Oo ( Oo0o0000o0o0 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if IIi1i11111 != 'Failed' :
   I1III . append ( Oo0o0000o0o0 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not IIi1i11111 != 'Failed' :
   ooOO00O00oo = oO0Oo ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if ooOO00O00oo != 'Failed' :
    I1III . append ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
I1ii11iI = ( str ( I1III ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
IIi1i = I1ii11iI + 'GenieArt/NEW/'
if 46 - 46: ooOoOO0oOO % oO0OOoo0OO * Ii1I - OoOOOOOo0o . ooOoO0O00
if 13 - 13: OoOOOOOo0o . ooOoO0O00 / oOo0O0Ooo * iI11I1II1I1I
def oooooOoo0ooo ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  I11 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  I1I1IiI1 = 'genie tv repo not being installed '
  III1iII1I1ii ( I1I1IiI1 )
 else :
  oOOo0 ( )
  if 54 - 54: o0o00Oo0O - OO % O0OoO0O00o0oO
def oOOo0 ( ) :
 if 77 - 77: OOooOOo / oOo0O0Ooo / oO0o + oO0o . O0OoO0O00o0oO
 ii1ii11IIIiiI = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 O000OOo00oo = open ( oo0OooOOo0 ) . read ( )
 oo0OOo = open ( o0O ) . read ( )
 if 64 - 64: Ooo0Oo0oOoo
 iI11Ii = re . compile ( 'version="([^"]*)" provider' ) . findall ( O000OOo00oo )
 i1iIIIi1i = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( oo0OOo )
 iI1iIIiiii = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( ii1ii11IIIiiI )
 i1iI11i1ii11 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( ii1ii11IIIiiI )
 for OOooo0O00o in iI11Ii :
  oOOoOooOo = OOooo0O00o
  for O000oo in iI1iIIiiii :
   if not O000oo == oOOoOooOo :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    IIi1I11I1II ( )
   if O000oo == oOOoOooOo :
    OooOoooOo
 for ii11IIII11I in i1iIIIi1i :
  OOooo = ii11IIII11I
  for oOooOOOoOo in i1iI11i1ii11 :
   if not oOooOOOoOo == OOooo :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    i1Iii1i1I ( )
   if oOooOOOoOo == OOooo :
    xbmc . sleep ( 100 )
    OooOoooOo
def OOoO00 ( ) :
 oooooOoo0ooo ( )
 IiI111111IIII ( )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']CONTACT US[/COLOR]' , '' , 50006 , IIi1i + 'Contact-Us.png' , iIii1 , '' )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , IIi1i + 'settings.png' , iIii1 , '' )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']Force Genie Update Kodi 16+[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , IIi1i + 'GenieUpdate.png' , iIii1 , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']WIZARD[/COLOR]' , str ( I1ii11iI ) , 4001 , IIi1i + 'Wizard.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']STREAMS[/COLOR]' , str ( I1ii11iI ) , 4002 , IIi1i + 'Streams.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Music[/COLOR]' , str ( I1ii11iI ) , 4003 , IIi1i + 'Music.png' , iIii1 , '' )
  if 78 - 78: oO0o . O0OoO0O00o0oO + oO0o / Ooo0Oo0oOoo / oO0o
 if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1ii11iI ) , 32 , IIi1i + 'BuildersToolbox.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Source List' ) == 'true' :
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']SOURCE LIST[/COLOR]' , str ( I1ii11iI ) , 46 , IIi1i + 'SoruceList.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MAINTENANCE[/COLOR]' , str ( I1ii11iI ) , 3 , IIi1i + 'Maintenance.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Addons' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ADDONS[/COLOR]' , '' , 10050 , IIi1i + 'Addons.png' , iIii1 , '' )
 if oo00 . getSetting ( 'APK Tool' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']APK TOOL[/COLOR]' , str ( I1ii11iI ) , 30039 , IIi1i + 'APKTools.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']GenieTv RSS Feed[/COLOR]' , str ( I1ii11iI ) , 39 , IIi1i + 'GenieTVRSSFeed.png' , iIii1 , '' )
  if 54 - 54: OOooOOo % iI1i1IiI
  if 37 - 37: OOooOOo * I1ii11iIi11i / oO0OOoo0OO - iI1i1IiI % IIiIiII11i . o000o
 O00 ( 'movies' , 'MAIN' )
def I1iI1 ( ) :
 iiiIi1 = i1I1ii11i1Iii ( )
 I1IiiiiI = iiiIi1 . replace ( oooOOOOO , "" )
 if os . path . exists ( iiiIi1 ) or not iiiIi1 == False :
  o0OIiII = open ( iiiIi1 , mode = 'r' ) ; ii1iII1II = o0OIiII . read ( ) ; o0OIiII . close ( )
  Iii1I1I11iiI1 ( "%s - %s" % ( i1 , I1IiiiiI ) , ii1iII1II )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def i1I1ii11i1Iii ( ) :
 I1I1i1I = False
 if os . path . exists ( os . path . join ( oooOOOOO , 'xbmc.log' ) ) :
  I1I1i1I = os . path . join ( oooOOOOO , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( oooOOOOO , 'kodi.log' ) ) :
  I1I1i1I = os . path . join ( oooOOOOO , 'kodi.log' )
 elif os . path . exists ( os . path . join ( oooOOOOO , 'spmc.log' ) ) :
  I1I1i1I = os . path . join ( oooOOOOO , 'spmc.log' )
 elif os . path . exists ( os . path . join ( oooOOOOO , 'tvmc.log' ) ) :
  I1I1i1I = os . path . join ( oooOOOOO , 'tvmc.log' )
 return I1I1i1I
 if 30 - 30: ii
def I1Ii1iI1 ( url ) :
 if url == 'http://' : return False
 try :
  oOOoo0Oo = urllib2 . Request ( url )
  oOOoo0Oo . add_header ( 'User-Agent' , I1i1iiI1 )
  o00OO00OoO = urllib2 . urlopen ( oOOoo0Oo )
  o00OO00OoO . close ( )
 except Exception , oO0 :
  return oO0
 return True
 if 75 - 75: oO0OOoo0OO + OOooOOo + I11i * Ooo0Oo0oOoo % o000o . iI1i1IiI
def oOI1Ii1I1 ( ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 if len ( iI11Ii ) > 0 :
  for IiII111iI1ii1 , iI11I1II , Ii1IIiI1i , o0Oo00 in iI11Ii :
   i1Ii ( IiII111iI1ii1 , iI11I1II , 50005 , Ii1IIiI1i , o0Oo00 , '' )
def iI ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']BACKUP MY BUILD[/COLOR]' , str ( I1ii11iI ) , 10060 , IIi1i + 'BackupMyBuild.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']RESTORE MY BUILD[/COLOR]' , str ( I1ii11iI ) , 49 , IIi1i + 'RestoreMyBuild.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']WIPE GENIE[/COLOR]' , str ( I1ii11iI ) , 41 , IIi1i + 'WipeGenie.png' , iIii1 , '' )
 if 90 - 90: ooOoOO0oOO % OoOOOOOo0o - iI11I1II1I1I - iI11I1II1I1I / Ii % Ii1I
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Genie BUILDS[/COLOR]' , str ( I1ii11iI ) , 44 , IIi1i + 'GenieBuilds.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
def IIii11I1 ( ) :
 oooooOoo0ooo ( )
 if ii11iIi1I == '5knuckleshuffle' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']XVID[/COLOR]' , str ( I1ii11iI ) , 10100 , IIi1i + 'Jizbox.png' , iIii1 , '' )
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ADULT CHANNELS[/COLOR]' , str ( I1ii11iI ) , 30033 , IIi1i + 'adu.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Favourites' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']FAVOURITES[/COLOR]' , str ( I1ii11iI ) , 10057 , IIi1i + 'Favourites.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Search' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH[/COLOR]' , str ( I1ii11iI ) , 9000 , IIi1i + 'Search.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']G-Tv Live List[/COLOR]' , '' , 4009 , IIi1i + 'GTV.png' , iIii1 , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']TV GUIDE[/COLOR]' , '' , 10063 , IIi1i + 'TvGuide.png' , iIii1 , '' )
  if 83 - 83: oO0OOoo0OO
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']STREAM TEAM[/COLOR]' , str ( I1ii11iI ) , 4006 , IIi1i + 'StreamTeam.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MOVIES[/COLOR]' , str ( I1ii11iI ) , 4004 , IIi1i + 'Movies.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']TV SHOWS[/COLOR]' , str ( I1ii11iI ) , 4005 , IIi1i + 'TVShows.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']FOOTBALL[/COLOR]' , '' , 10002 , IIi1i + 'Football.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']KIDS[/COLOR]' , str ( I1ii11iI ) , 4007 , IIi1i + 'Kids.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']24/7 STREAMS[/COLOR]' , '' , 30030 , IIi1i + '247Streams.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NEWS[/COLOR]' , str ( I1ii11iI ) , 30032 , IIi1i + 'News.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']GenieTv TUTORIALS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , IIi1i + 'GenieTVTutorials.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']HOBBIES[/COLOR]' , str ( I1ii11iI ) , 4008 , IIi1i + 'Hobbies.png' , iIii1 , '' )
 if oo00 . getSetting ( 'YOUTUBE' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH YOUTUBE[/COLOR]' , str ( I1ii11iI ) , 10064 , IIi1i + 'SeachYouTube.png' , iIii1 , '' )
 if oo00 . getSetting ( 'REQUESTS' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']REQUESTS[/COLOR]' , str ( I1ii11iI ) + ( Oo0o0000o0o0 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , IIi1i + 'Requests.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Stand Up' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']STAND UP[/COLOR]' , '' , 10003 , IIi1i + 'StandUp.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Documentaries' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']DOCUMENTARIES[/COLOR]' , str ( I1ii11iI ) , 8040 , IIi1i + 'documentaries.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Disclose' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']DISCLOSE TV[/COLOR]' , str ( I1ii11iI ) , 7001 , IIi1i + 'DiscloseTV.png' , iIii1 , '' )
  if 65 - 65: oOo0O0Ooo % OoOOOOOo0o * o000o
  if 19 - 19: ooOoOO0oOO + iI11I1II1I1I . ii . Ooo0Oo0oOoo / ooOoOO0oOO + OO
 if oo00 . getSetting ( 'Playlist Loader' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']PLAYLIST LOADER[/COLOR]' , str ( I1ii11iI ) , 3000 , IIi1i + 'PlaylistLoader.png' , iIii1 , '' )
  if 85 - 85: Ii1I - iI11I1II1I1I
  if 31 - 31: ii - ii * Ooo0Oo0oOoo - o000o
  if 85 - 85: Ii % o000o . O0OoO0O00o0oO - OoOOOOOo0o
  if 42 - 42: o000o + oO0OOoo0OO / iI1i1IiI + O0OoO0O00o0oO
  if 30 - 30: o0o00Oo0O
  if 44 - 44: o000o / Ooo0Oo0oOoo / Ooo0Oo0oOoo
  if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / o000o
  if 25 - 25: oOo0O0Ooo . oOo0O0Ooo - OOooOOo % OOooOOo - Ii / ooOoOO0oOO
  if 51 - 51: I1ii11iIi11i / OOooOOo . O0OoO0O00o0oO * I11i + oO0o * OO
  if 73 - 73: oO0o + ii - o0o00Oo0O - OoOOOOOo0o - IIiIiII11i
  if 99 - 99: oO0OOoo0OO . OoOOOOOo0o + ooOoOO0oOO + ii % I11i
  if 51 - 51: iI11I1II1I1I
 O00 ( 'movies' , 'MAIN' )
 if 34 - 34: o000o + oOo0O0Ooo - o000o
def IiI111111IIII ( ) :
 if not os . path . exists ( OO0o ) :
  Iii1I1I11iiI1 ( 'Change Log 5/9/16 - v3.0.7' , 'RaysRavers added to music section, RadioNomy section added to music, Quicksilver fixed in music, WatchSeries fixed now playing from genres, Go fishing work in progress, View log file from within maintenance, Speedtest added to maintenance section, GenieTv contact information within addon, Search tweaked performing faster and more sources, Tv theme tunes section added to music, new servers online' )
  os . makedirs ( OO0o )
  if 17 - 17: IIiIiII11i % iI1i1IiI + Ooo0Oo0oOoo - iI1i1IiI / O0OoO0O00o0oO + oO0OOoo0OO
  if 59 - 59: O0OoO0O00o0oO % OOooOOo . OoOOOOOo0o * Ii1I % Ooo0Oo0oOoo
def oO0o0o0oo ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH MOVIES[/COLOR]' , str ( I1ii11iI ) , 9001 , IIi1i + 'Search.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']POPCORN BOX[/COLOR]' , str ( I1ii11iI ) , 7061 , IIi1i + 'PopcornBox.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Film Trailers[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , IIi1i + 'FilmTrailers.png' , iIii1 , '' )
 if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , IIi1i + 'ClassicMovies.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
def iI1111iiii ( ) :
 oooooOoo0ooo ( )
 Oo0OO ( )
 if 78 - 78: O0OoO0O00o0oO - ii - Ii1I / oO0OOoo0OO / IIiIiII11i
 if 29 - 29: oOo0O0Ooo % oOo0O0Ooo
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Football On G-Tv[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , IIi1i + 'TodaysMacthes.png' , iIii1 , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']TV GUIDE[/COLOR]' , '' , 10063 , IIi1i + 'TvGuide.png' , iIii1 , '' )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']Link GTV to Guide[/COLOR]' , '' , 4010 , IIi1i + 'linkchannels.png' , iIii1 , '' )
 if 94 - 94: iI11I1II1I1I / I1ii11iIi11i % iI1i1IiI * iI1i1IiI * IIiIiII11i
 if 29 - 29: oO0o + OOooOOo / I11i / O0OoO0O00o0oO * iI11I1II1I1I
def O0OO ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH SERIES[/COLOR]' , str ( I1ii11iI ) , 9002 , IIi1i + 'Search.png' , iIii1 , '' )
 if 6 - 6: iI11I1II1I1I % Ii % Ii1I
 if 93 - 93: OO * ii + oO0OOoo0OO
 if oo00 . getSetting ( 'Watch Series' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']WATCH SERIES[/COLOR]' , '' , 10040 , IIi1i + 'WatchSeries.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']iWATCH SERIES[/COLOR]' , '' , 8020 , IIi1i + 'iWatchSeries.png' , iIii1 , '' )
 if 33 - 33: o0o00Oo0O * I11i - ooOoOO0oOO % ooOoOO0oOO
 if 18 - 18: ooOoOO0oOO / I1ii11iIi11i * ooOoOO0oOO + ooOoOO0oOO * Ii * Ii1I
 if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CLASSIC TV[/COLOR]' , str ( I1ii11iI ) , 8064 , IIi1i + 'ClassicTV.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']TV Show Trailers[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , IIi1i + 'TVShowTrailers.png' , iIii1 , '' )
 if 11 - 11: oO0OOoo0OO / OOooOOo - OO * ii + ii . OOooOOo
 O00 ( 'movies' , 'MAIN' )
def i1I1i111Ii ( ) :
 oooooOoo0ooo ( )
 if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SILENT HUNTER[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , IIi1i + 'SilentHunter.png' , iIii1 , '' )
 if oo00 . getSetting ( 'The Reaper' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']THE REAPER[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , IIi1i + 'TheReaper.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']PANDORAS BOX[/COLOR]' , str ( I1ii11iI ) , 10025 , IIi1i + 'PandorasBox.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Redemption Streams' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Redemption Streams[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , IIi1i + 'RedemptionStreams.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']DoJo STREAMS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , IIi1i + 'DojoStreams.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SCOOBY STREAMS[/COLOR]' , str ( I1ii11iI ) , 1023 , IIi1i + 'ScoobyStreams.png' , iIii1 , '' )
 if oo00 . getSetting ( 'HeroVision' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']HEROVISION[/COLOR]' , '' , 1017 , IIi1i + 'Herovision.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ITV[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , IIi1i + 'ITVStreams.png' , iIii1 , '' )
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
 O00 ( 'movies' , 'MAIN' )
 if 27 - 27: oO0OOoo0OO % oOo0O0Ooo
def o0oooOO00 ( ) :
 oooooOoo0ooo ( )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']SILENT HUNTER[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , IIi1i + 'SilentHunter.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SERVER 1[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , IIi1i + 'SilentHunter.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SERVER 2[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , IIi1i + 'SilentHunter.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SCRAPES[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , IIi1i + 'SilentHunter.png' , iIii1 , '' )
def iiIiii1IIIII ( url ) :
 o00o = IIIIiiIiiI ( url )
 url = url
 iI11Ii = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( o00o )
 for IIIIiI11I11 , oo00o0 in iI11Ii :
  if '[DIR]' in IIIIiI11I11 :
   i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 1018 , IIi1i + 'SilentHunter.png' )
  if 'mkv' in oo00o0 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 222 , IIi1i + 'SilentHunter.png' )
  if 'avi' in oo00o0 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + oo00o0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oo00o0 , 222 , IIi1i + 'SilentHunter.png' )
   if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + Ooo0Oo0oOoo * iI11I1II1I1I
def o0ooooO0o0O ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']HEROVISION[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , IIi1i + 'Herovision.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']HEROVISION SCRAPES[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , IIi1i + 'Herovision.png' , iIii1 , '' )
 if 24 - 24: o0o00Oo0O * I11i
def IiI1iiiIii ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , IIi1i + 'SearchCartoons.png' , iIii1 , '' )
 if oo00 . getSetting ( 'WCO' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1ii11iI ) , 21004 , IIi1i + 'watchcartoons.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Cartoons' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CARTOONS[/COLOR]' , '' , 10001 , IIi1i + 'Cartoons.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Anime' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']AnimeLand[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , IIi1i + 'anime.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
def I1III1111iIi ( ) :
 oooooOoo0ooo ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']FOOTBALL[/COLOR]' , '' , 10002 , IIi1i + 'Football.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']FITNESS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , IIi1i + 'Fitness.png' , iIii1 , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Go Fishing[/COLOR]' , str ( I1ii11iI ) , 8090 , IIi1i + 'GoFishing.png' , iIii1 , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']GenieTv Kitchen[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , IIi1i + 'GenieTVKitchen.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 38 - 38: iI1i1IiI + Ooo0Oo0oOoo / ooOoOO0oOO % oO0OOoo0OO - Ii1I
 if 14 - 14: o000o / ooOoOO0oOO
 if 85 - 85: Ooo0Oo0oOoo
def OooOoooOo ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 iI11Ii = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( OO0O0OoOO0 )
 for I1I1IiI1 in iI11Ii :
  I1I1IiI1 = ( str ( I1I1IiI1 ) )
  if os . path . exists ( xbmc . translatePath ( I1I1IiI1 ) ) :
   iI1i11II1i = ( I1I1IiI1 ) . replace ( 'special://home/addons/' , '' )
   Iii1I1I11iiI1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iI1i11II1i + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   o0o0OoOo0O0OO = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if o0o0OoOo0O0OO == 0 :
    III1iII1I1ii ( I1I1IiI1 )
    iIi1I11I ( )
   elif o0o0OoOo0O0OO == 1 :
    Iii1 ( I1I1IiI1 )
  else :
   pass
   if 58 - 58: oOo0O0Ooo . iI1i1IiI + OOooOOo
def Iii1 ( addon ) :
 iI1i11II1i = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 66 - 66: iI1i1IiI / o000o * ii + ii % Ooo0Oo0oOoo
def III1iII1I1ii ( addon ) :
 I11 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 IIii1111 = os . path . join ( II11iiii1Ii , 'default.py' )
 I1iI = open ( IIii1111 , "w+" )
 if 38 - 38: o000o % OOooOOo + Ii1I . Ii
 I1iI . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1iI . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1iI . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 53 - 53: Ii * iI1i1IiI
 if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
 if 38 - 38: oO0OOoo0OO - O0OoO0O00o0oO / iI1i1IiI
 if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / OoOOOOOo0o + Ii1I
 if 86 - 86: I11i
 if 5 - 5: OO * OOooOOo
 if 5 - 5: ooOoOO0oOO
 if 90 - 90: ooOoOO0oOO . oO0OOoo0OO / OoOOOOOo0o - Ooo0Oo0oOoo
 if 40 - 40: ii
 if 25 - 25: OO + OoOOOOOo0o / oO0OOoo0OO . I11i % o0o00Oo0O * oO0o
 if 84 - 84: oO0OOoo0OO % OoOOOOOo0o + Ii
 if 28 - 28: I1ii11iIi11i + oO0o * O0OoO0O00o0oO % o000o . Ooo0Oo0oOoo % o0o00Oo0O
 if 16 - 16: Ooo0Oo0oOoo - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
 if 19 - 19: oO0o - I1ii11iIi11i . o0o00Oo0O
 if 60 - 60: IIiIiII11i + I1ii11iIi11i
 if 9 - 9: oO0OOoo0OO * ii - iI11I1II1I1I + OOooOOo / oO0o . oO0o
 if 49 - 49: IIiIiII11i
 if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * o000o
 if 81 - 81: iI1i1IiI + OO
def o0oo0 ( ) :
 ii111iI1iIi1 ( 'Genre' , Oo0o0000o0o0 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , IIi1i + 'genievision.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Most Viewed' , Oo0o0000o0o0 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , IIi1i + 'genievision.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Box Office' , Oo0o0000o0o0 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , IIi1i + 'genievision.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Search' , '' , 10078 , IIi1i + 'genievision.png' , iIii1 , '' )
 if 97 - 97: OOooOOo % Ii1I
def iIiIII1I1I1 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'http://imoviemax.se/?s=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1IIIi = III11I1 . lower ( )
 O00Ooo ( IIi1IIIi )
def OOOO0OOO ( url ) :
 i1i1ii = [ ]
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iII1ii1 in iI11Ii :
  if IiII111iI1ii1 in i1i1ii :
   pass
  else :
   ii111iI1iIi1 ( IiII111iI1ii1 + ' - ' + iII1ii1 + ' Films' , url , 10074 , IIi1i + 'genievision.png' , iIii1 , '' )
   i1i1ii . append ( IiII111iI1ii1 )
   if 12 - 12: O0OoO0O00o0oO - oO0OOoo0OO . ii / Ii1I . ooOoO0O00 * oO0o
def IiIiII1 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , Iii1iiIi1II in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 + ' - Views:' + Iii1iiIi1II , url , 10075 , IIi1i + 'genievision.png' , iIii1 , '' )
  if 60 - 60: oOo0O0Ooo - o000o * Ooo0Oo0oOoo % IIiIiII11i
  if 62 - 62: iI11I1II1I1I
def O00Ooo ( url ) :
 i1II = [ ]
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( OO0O0OoOO0 )
 for next in next :
  ii111iI1iIi1 ( 'NEXT PAGE' , next , 10074 , IIi1i + 'Next.png' , iIii1 , '' )
 iI11Ii = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , IiII111iI1ii1 , url in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 10075 , iI1I , iI1I , '' )
  i1II . append ( IiII111iI1ii1 )
  if 100 - 100: iI11I1II1I1I + OOooOOo / I1ii11iIi11i . Ii
def III1I1Iii1iiI ( img , name , url ) :
 img = img
 name = name
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( OO0O0OoOO0 )
 for i1Iii11I1i , url in iI11Ii :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Oo00o0OO0O00o = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Oo00o0OO0O00o
  O0Oooo = ( i1Iii11I1i ) . replace ( 'play-' , 'Server ' )
  i1Ii ( O0Oooo , Oo00o0OO0O00o , 10076 , img , img , '' )
  if 21 - 21: I1ii11iIi11i
def I1ii1 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( OO0O0OoOO0 )
 for oo00o0 in iI11Ii :
  if '=m' in oo00o0 :
   O00Oo0o0000OOoO ( oo00o0 )
  elif 'php' in oo00o0 :
   I1ii1 ( url )
  else :
   OO0O0OoOO0 = O00OOOoOoo0O ( oo00o0 )
   iI11Ii = re . compile ( 'content="([^"]*)">' ) . findall ( OO0O0OoOO0 )
   for IiIi1I1ii111 in iI11Ii :
    O00Oo0o0000OOoO ( oo00o0 )
    if 46 - 46: o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
    if 83 - 83: Ii1I - oOo0O0Ooo + O0OoO0O00o0oO
    if 5 - 5: OoOOOOOo0o
def iIi1i1iIi1iI ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iiIi1iI1iIii = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for o00OooO0oo , o0o0oOoOO0O in iiIi1iI1iIii :
  print 'there ><><><><><><><><><><><><'
  o00OooO0oo = o00OooO0oo
  iI11Ii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0o0oOoOO0O ) )
  for IiII111iI1ii1 , i1ii1II1ii in iI11Ii :
   print 'here <><><><><><><><><><><><>'
   ii111iI1iIi1 ( '[COLORred]' + o00OooO0oo + '[/COLOR] - ' + IiII111iI1ii1 + ' - [COLOR' + i1iiIIiiI111 + ']' + i1ii1II1ii + '[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , IIi1i + 'loader.png' , iIii1 , '' )
 iII111Ii = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for o00OooO0oo , Ooo00OoOOO in iII111Ii :
  print 'there ><><><><><><><><><><><><'
  o00OooO0oo = o00OooO0oo
  iI11Ii = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Ooo00OoOOO ) )
  for IiII111iI1ii1 , i1ii1II1ii in iI11Ii :
   print 'here <><><><><><><><><><><><>'
   ii111iI1iIi1 ( '[COLORred]' + o00OooO0oo + '[/COLOR] - ' + IiII111iI1ii1 + ' - [COLOR' + i1iiIIiiI111 + ']' + i1ii1II1ii + '[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , IIi1i + 'loader.png' , iIii1 , '' )
   if 98 - 98: iI11I1II1I1I * Ii1I * O0OoO0O00o0oO + oO0OOoo0OO % Ii % o0o00Oo0O
   if 27 - 27: o0o00Oo0O
   if 79 - 79: I11i - Ooo0Oo0oOoo + I11i . o000o
def ii1III11 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iII111Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iII111Ii in iII111Ii :
  IiII111iI1ii1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII111Ii ) )
  for IiII111iI1ii1 in IiII111iI1ii1 :
   IiII111iI1ii1 = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII111Ii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I1iiIIIi11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII111Ii ) )
  for I1iiIIIi11 in I1iiIIIi11 :
   I1iiIIIi11 = 'http:' + I1iiIIIi11
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , '' , '' )
  if 12 - 12: ii % I11i * Ooo0Oo0oOoo % iI11I1II1I1I / OoOOOOOo0o
  if 27 - 27: Ii % IIiIiII11i % Ooo0Oo0oOoo . o0o00Oo0O - I1ii11iIi11i + OOooOOo
  if 57 - 57: iI11I1II1I1I / Ooo0Oo0oOoo - ooOoO0O00
  if 51 - 51: OO
def ii11I1 ( url ) :
 if 75 - 75: oO0o / IIiIiII11i % o0o00Oo0O
 Ii111iIi1iIi = [ ]
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for oo00o0 , iI1I , IiII111iI1ii1 , IIIIIo0ooOoO000oO in iI11Ii :
  IiII111iI1ii1 = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iiiI1I11i1 = O00OOOoOoo0O ( oo00o0 )
  i1iIIIi1i = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iiiI1I11i1 )
  for OOo , i1i11I1I1iii1 in i1iIIIi1i :
   I1iii11 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i1i11I1I1iii1 ) )
   for ooo0O in I1iii11 :
    if IiII111iI1ii1 in Ii111iIi1iIi :
     pass
    else :
     i1Ii ( IiII111iI1ii1 , OOo , 8043 , iI1I , iI1I , ooo0O )
     O00 ( 'movies' , 'INFO' )
     Ii111iIi1iIi . append ( IiII111iI1ii1 )
     if 16 - 16: OOooOOo
     if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . O0OoO0O00o0oO
def O0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , iII1 , ooo0O , o0Oo00 , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 10065 , iII1 , o0Oo00 , ooo0O )
 O00 ( 'movies' , 'INFO' )
 if 27 - 27: oO0o . Ooo0Oo0oOoo + OOooOOo / iI11I1II1I1I % iI1i1IiI . oO0OOoo0OO
def IIIIi1 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'https://www.youtube.com/results?search_query=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 IIi1IIIi = III11I1 . lower ( )
 OO0O0OoOO0 = O00OOOoOoo0O ( IIi1IIIi )
 iI11Ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II in next :
  iI11I1II = 'https://www.youtube.com' + iI11I1II
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + '] NEXT [/COLOR]' , iI11I1II , 10065 , IIi1i + 'Next.png' , iIii1 , '' )
 for iI1I , iI11I1II , IiII111iI1ii1 , iIi11iiIiI1I , i1i11I1I1iii1 in iI11Ii :
  O0O . append ( IiII111iI1ii1 )
  O00 ( 'tvshows' , 'INFO' )
  I1iiIIIi11 = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1iiIIIi11
  iI11I1II = 'http://www.youtube.com' + iI11I1II
  i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , I1iiIIIi11 , i1i11I1I1iii1 )
 else :
  iI11Ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for iI1I , iI11I1II , IiII111iI1ii1 , iIi11iiIiI1I in iI11Ii :
   print 'im doing it'
   O00 ( 'tvshows' , 'INFO' )
   I1iiIIIi11 = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
   iI11I1II = 'http://www.youtube.com' + iI11I1II
   if '&' in iI11I1II :
    print ' i got here'
    OO0O0OoOO0 = O00OOOoOoo0O ( iI11I1II )
    iII111Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
    for iII111Ii in iII111Ii :
     IiII111iI1ii1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII111Ii ) )
     for IiII111iI1ii1 in IiII111iI1ii1 :
      IiII111iI1ii1 = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iI11I1II = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII111Ii ) )
     for iI11I1II in iI11I1II :
      iI11I1II = 'https://www.youtube.com/w' + iI11I1II
     I1iiIIIi11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII111Ii ) )
     for I1iiIIIi11 in I1iiIIIi11 :
      I1iiIIIi11 = 'http:' + I1iiIIIi11
     i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , iIii1 , '' )
   elif IiII111iI1ii1 in O0O :
    pass
   elif 'user' in iI11I1II or 'elete' in IiII111iI1ii1 :
    pass
   elif 'hannel' in iI11I1II :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iI11I1II
    OO0O0OoOO0 = O00OOOoOoo0O ( iI11I1II )
    Iiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
    for iI1I , iI11I1II , IiII111iI1ii1 in Iiii :
     if 'outube' in iI11I1II or 'list' in iI11I1II :
      pass
     elif 'atch' in iI11I1II :
      iI11I1II = ( iI11I1II ) . replace ( '/watch?v=' , '' )
      i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iI1I , 'http:' + iI1I , '' )
     else :
      pass
   else :
    i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , I1iiIIIi11 , '' )
    if 89 - 89: o000o
def iIiiii ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( OO0O0OoOO0 )
 for url in next :
  url = 'https://www.youtube.com' + url
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + '] NEXT [/COLOR]' , url , 10065 , IIi1i + 'Next.png' , iIii1 , '' )
 for iI1I , url , IiII111iI1ii1 , iIi11iiIiI1I , i1i11I1I1iii1 in iI11Ii :
  O0O . append ( IiII111iI1ii1 )
  O00 ( 'tvshows' , 'INFO' )
  I1iiIIIi11 = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I1iiIIIi11
  url = 'http://www.youtube.com' + url
  i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , I1iiIIIi11 , i1i11I1I1iii1 )
 else :
  iI11Ii = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for iI1I , url , IiII111iI1ii1 , iIi11iiIiI1I in iI11Ii :
   O00 ( 'tvshows' , 'INFO' )
   I1iiIIIi11 = 'http:' + ( iI1I ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    OO0O0OoOO0 = O00OOOoOoo0O ( url )
    iII111Ii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
    for iII111Ii in iII111Ii :
     IiII111iI1ii1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iII111Ii ) )
     for IiII111iI1ii1 in IiII111iI1ii1 :
      IiII111iI1ii1 = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iII111Ii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I1iiIIIi11 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iII111Ii ) )
     for I1iiIIIi11 in I1iiIIIi11 :
      I1iiIIIi11 = 'http:' + I1iiIIIi11
     i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , iIii1 , '' )
   elif IiII111iI1ii1 in O0O :
    pass
   elif 'user' in url or 'elete' in IiII111iI1ii1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    OO0O0OoOO0 = O00OOOoOoo0O ( url )
    Iiii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
    for iI1I , url , IiII111iI1ii1 in Iiii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iI1I , 'http:' + iI1I , '' )
     else :
      pass
   else :
    i1Ii ( '[COLORred]' + iIi11iiIiI1I + '[/COLOR]' + '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 , I1iiIIIi11 , '' )
    if 89 - 89: iI1i1IiI - oO0OOoo0OO % I1ii11iIi11i % I11i
    if 49 - 49: I1ii11iIi11i - oOo0O0Ooo / OO / o0o00Oo0O % I11i * OoOOOOOo0o
def Oo0OO ( ) :
 if i1iIIi1 == 'insert_password' :
  I11 . ok ( '[COLOR' + i1iiIIiiI111 + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + i1iiIIiiI111 + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OOoO0 = open ( I1IIIii )
  iI11Ii = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OOoO0 ) )
  for II11iI111i1 , Oo00OoOo in iI11Ii :
   if II11iI111i1 == 'needs replacing' or Oo00OoOo == 'needs replacing' :
    ii1ii111 ( )
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']G-Tv PRIVATE LIST[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , IIi1i + 'PrivateList.png' , iIii1 , '' )
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']G-Tv ULTIMATE[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , IIi1i + 'UltimateList.png' , iIii1 , '' )
  if 33 - 33: Ii1I
def O00O0Ooooo00 ( ) :
 iI111I11I1I1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + O00o0OO + ")" )
 ii1ii111 ( )
 iI111I11I1I1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 97 - 97: oO0OOoo0OO / ooOoOO0oOO % ooOoO0O00 % Ii1I
def ii111I11iI ( ) :
 ii111iI1iIi1 ( 'Live Events' , '' , 60002 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Live Stream Channels' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'PPV' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Entertainment' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Factual' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Movie Channels' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'US Movie Channels TEST' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Kids' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Music' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'UK Sports' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'International Sports' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'News UK & International' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Full List' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'World' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'German' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'Arabic' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'VOD Latest' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'VOD Bollywood' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 ii111iI1iIi1 ( 'TV Series Latest' , '' , 60003 , IIi1i + 'UltimateList.png' , iIii1 , '' )
 if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * Ooo0Oo0oOoo
def Ooooooo ( name ) :
 I1IIIiI1I1ii1 = name
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 iI11Ii = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( OO0O0OoOO0 )
 for name , iI1I , iiiI1I1iIIIi1 , iI11I1II in iI11Ii :
  if I1IIIiI1I1ii1 == 'Full List' :
   iI11I1II = ( iI11I1II ) . replace ( 'replace_user' , i1iiIII111ii ) . replace ( 'replace_pass' , i1iIIi1 )
   i1Ii ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iI11I1II ) . strip ( ) , 10012 , iI1I , iI1I , '' )
  else :
   I1IIIiI1I1ii1 = ( I1IIIiI1I1ii1 ) . replace ( 'World' , 'القنوات العربية' )
   if I1IIIiI1I1ii1 in iiiI1I1iIIIi1 :
    iI11I1II = ( iI11I1II ) . replace ( 'replace_user' , i1iiIII111ii ) . replace ( 'replace_pass' , i1iIIi1 )
    print iI11I1II + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    i1Ii ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iI11I1II ) . strip ( ) , 10012 , iI1I , iI1I , '' )
   else :
    pass
    if 17 - 17: iI11I1II1I1I . ii / Ooo0Oo0oOoo % IIiIiII11i % ooOoO0O00 / Ii
def OOO ( name ) :
 I1IIIiI1I1ii1 = name
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) )
 iI11Ii = re . compile ( '#EXTINF:-1 tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( OO0O0OoOO0 )
 for name , iI1I , iI11I1II in iI11Ii :
  iI11I1II = ( iI11I1II ) . replace ( 'replace_user' , i1iiIII111ii ) . replace ( 'replace_pass' , i1iIIi1 )
  i1Ii ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iI11I1II ) . strip ( ) , 10012 , iI1I , iI1I , '' )
 else :
  i1Ii ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 30 - 30: ii - ii . o0o00Oo0O / iI1i1IiI
  if 31 - 31: O0OoO0O00o0oO + I11i . ii
  if 89 - 89: IIiIiII11i + ooOoO0O00 + IIiIiII11i
  if 7 - 7: o0o00Oo0O % I11i + Ii1I * iI1i1IiI - iI1i1IiI
  if 42 - 42: OOooOOo * OOooOOo * ooOoOO0oOO . Ooo0Oo0oOoo
  if 51 - 51: O0OoO0O00o0oO % iI11I1II1I1I - ii % oO0OOoo0OO * iI11I1II1I1I % oO0o
  if 99 - 99: o000o * IIiIiII11i * ooOoOO0oOO
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / OO
  if 79 - 79: oO0o - iI11I1II1I1I + OoOOOOOo0o - ooOoOO0oOO
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
def Ii1ii111i1 ( ) :
 ii111iI1iIi1 ( 'Full Backup' , '' , 10061 , IIi1i + 'FullBackUp.png' , iIii1 , 'Back Up Your Full System' )
 if os . path . exists ( i1I1iI ) :
  ii111iI1iIi1 ( 'Backup Genie Favourites' , iI11I1II , 10062 , IIi1i + 'BackupGenieFavourites.png' , iIii1 , 'Back Up Your favourites' )
 if os . path . exists ( OOOOi11i1 ) :
  ii111iI1iIi1 ( 'Backup Ivue Config' , OOOOi11i1 , 10062 , IIi1i + 'BackUpIvueConfig.png' , iIii1 , 'Back Up Your master.db' )
 if os . path . exists ( IIIii1II1II ) :
  ii111iI1iIi1 ( 'Backup Kodi Favourites' , IIIii1II1II , 10062 , IIi1i + 'BackKodiFavourites.png' , iIii1 , 'Back Up Your favourites.xml' )
  if 31 - 31: O0OoO0O00o0oO + o0o00Oo0O
  if 87 - 87: oO0OOoo0OO
  if 45 - 45: oO0o / ii - iI1i1IiI / OoOOOOOo0o % OO
zip = oo00 . getSetting ( 'zip' )
OoO = xbmc . translatePath ( os . path . join ( zip ) )
def Iii11iI11i1I ( ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iI111I11I1I1 . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 86 - 86: IIiIiII11i % Ii + OoOOOOOo0o % Ii
  if 92 - 92: Ii - iI1i1IiI / oO0OOoo0OO / o000o
  if 43 - 43: IIiIiII11i + O0OoO0O00o0oO + iI1i1IiI
def iI1IIIii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = i1I1iI
  elif 'Ivue' in name :
   url = OOOOi11i1
  elif 'Kodi' in name :
   url = IIIii1II1II
  Iii11iI11i1I ( )
  I1i11ii11 = open ( url ) . read ( )
  OO00O0oOO = os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] )
  o0OIiII = open ( OO00O0oOO , mode = 'w' )
  o0OIiII . write ( I1i11ii11 )
  o0OIiII . close ( )
 else :
  if 'guisettings.xml' in description :
   Ii1iI111 = open ( os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0oooo00o0Oo = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   iI11Ii = re . compile ( O0oooo00o0Oo ) . findall ( Ii1iI111 )
   for type , I1iii , oO0o0O0Ooo0o in iI11Ii :
    oO0o0O0Ooo0o = oO0o0O0Ooo0o . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1iii , oO0o0O0Ooo0o ) )
  else :
   OO00O0oOO = os . path . join ( url )
   I1i11ii11 = open ( os . path . join ( OoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0OIiII = open ( OO00O0oOO , mode = 'w' )
   o0OIiII . write ( I1i11ii11 )
   o0OIiII . close ( )
 iI111I11I1I1 . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 21 - 21: ooOoOO0oOO - oOo0O0Ooo + Ooo0Oo0oOoo
 if 78 - 78: ii - Ii - IIiIiII11i
 if 77 - 77: OOooOOo % OoOOOOOo0o
 if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( ) :
 o0OO0 = 1
 Iii11iI11i1I ( )
 oOo00Oo0o0Oo = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'Full Backup' , '' ) )
 I1 = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'my_full_backup.zip' ) )
 I1O0 = xbmc . translatePath ( os . path . join ( OoO , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOo00Oo0o0Oo ) :
  os . makedirs ( oOo00Oo0o0Oo )
 iIi1IiII = I11 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iIi1IiII ) : return False , 0
 I1i = iIi1IiII
 ooo = xbmc . translatePath ( os . path . join ( oOo00Oo0o0Oo , I1i + '.zip' ) )
 ii1iiIi1 = [ 'plugin.video.GenieTv' ]
 i111iiI1ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 IIiii = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 I1i1i = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OOOOooO0oO00O0o = "Creating full backup of existing build"
 ooOO00oOOo000 = "Creating Community Build"
 IIi = "Archiving..."
 i11II11II1 = ""
 II1I = "Please Wait"
 OoOo000oOo0oo ( OOooO0OOoo , ooo , ooOO00oOOo000 , IIi , i11II11II1 , II1I , IIiii , I1i1i )
 time . sleep ( 1 )
 oO0O = xbmc . translatePath ( os . path . join ( oOo00Oo0o0Oo , I1i + '_guisettings.zip' ) )
 oOO = zipfile . ZipFile ( oO0O , mode = 'w' )
 try :
  oOO . write ( xbmc . translatePath ( os . path . join ( OOooO0OOoo , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oOO . close ( )
 if o0OO0 == 0 :
  iI111I11I1I1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iI111I11I1I1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iI111I11I1I1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + ooo + '[/COLOR]' )
  if 11 - 11: Ii - o000o . o000o
def OoOo000oOo0oo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I11I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIIII1i = len ( sourcefile )
 o00oO0 = [ ]
 i11I1II = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for OO0 , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( sourcefile ) :
  for file in OO0oIII111i11IiI :
   i11I1II . append ( file )
 O0000 = len ( i11I1II )
 for OO0 , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( sourcefile ) :
  OOO0oOOo00O [ : ] = [ ooO00O0O0 for ooO00O0O0 in OOO0oOOo00O if ooO00O0O0 not in exclude_dirs ]
  OO0oIII111i11IiI [ : ] = [ o0OIiII for o0OIiII in OO0oIII111i11IiI if o0OIiII not in exclude_files ]
  for file in OO0oIII111i11IiI :
   o00oO0 . append ( file )
   iII1I1 = len ( o00oO0 ) / float ( O0000 ) * 100
   o0oOoO00o . update ( int ( iII1I1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0Ooo0o0ooo0 = os . path . join ( OO0 , file )
   if not 'temp' in OOO0oOOo00O :
    if not 'plugin.program.originwizard' in OOO0oOOo00O :
     import time
     oo0o0000Oo0 = '01/01/1980'
     o0O00oOoo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0Ooo0o0ooo0 ) ) )
     if o0O00oOoo > oo0o0000Oo0 :
      I11I . write ( o0Ooo0o0ooo0 , o0Ooo0o0ooo0 [ iIIII1i : ] )
 I11I . close ( )
 o0oOoO00o . close ( )
 if 63 - 63: iI1i1IiI * Ooo0Oo0oOoo * OoOOOOOo0o - o000o - OoOOOOOo0o
 if 97 - 97: O0OoO0O00o0oO / ii
def IIIiIi ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SCOOBY STREAMS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , IIi1i + 'scoob.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SCOOBY SCRAPES[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , IIi1i + 'scoob.png' , iIii1 , '' )
 if 34 - 34: ii . o0o00Oo0O / o000o * OOooOOo - Ii1I
 if 36 - 36: ooOoO0O00 / o0o00Oo0O / oO0o - o0o00Oo0O - ooOoO0O00
def ii1I11 ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH MOVIES[/COLOR]' , str ( I1ii11iI ) , 9001 , IIi1i + 'MOVIESv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH SERIES[/COLOR]' , str ( I1ii11iI ) , 9002 , IIi1i + 'TVSHOWSv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , IIi1i + 'ORIGINCARTOON' , iIii1 , '' )
 if 99 - 99: O0OoO0O00o0oO
 if 45 - 45: o000o - O0OoO0O00o0oO * ooOoOO0oOO / I1ii11iIi11i * IIiIiII11i - ooOoOO0oOO
 if 83 - 83: oO0o % OO . ii
 if 52 - 52: oO0OOoo0OO / Ii - O0OoO0O00o0oO . OO % iI11I1II1I1I + I11i
def OO00oOooo0O ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']RaysRavers[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , IIi1i + 'Rays-Ravers.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']QuickSilver[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWMv' ) ) , 1006 , IIi1i + 'Quicksilver.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']RadioNomy[/COLOR]' , '' , 70001 , IIi1i + 'RadioNomy.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MUSIC CHANNELS[/COLOR]' , str ( I1ii11iI ) , 30031 , IIi1i + 'MusicChannels.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']UK RADIO[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , IIi1i + 'UKRadio.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']WORLD RADIO[/COLOR]' , str ( I1ii11iI ) , 1013 , IIi1i + 'WorldRadio.png' , iIii1 , '' )
 if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CONCERTS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , IIi1i + 'Concerts.png' , iIii1 , '' )
  if 58 - 58: I1ii11iIi11i / o000o
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MUSIC VIDEOS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , IIi1i + 'MusicVideos.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MUSIC[/COLOR]' , str ( I1ii11iI ) + ( Oo0o0000o0o0 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , IIi1i + 'Music.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MUSIC SEARCH[/COLOR]' , str ( I1ii11iI ) , 1111 , IIi1i + 'MusicSearch.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , IIi1i + 'KodibleAudioBooks.png' , iIii1 , '' )
 if 44 - 44: O0OoO0O00o0oO
 O00 ( 'movies' , 'MAIN' )
 if 54 - 54: OoOOOOOo0o - Ooo0Oo0oOoo - ooOoOO0oOO . iI11I1II1I1I
def o0OIIiI1I1 ( ) :
 oooooOoo0ooo ( )
 if 15 - 15: OoOOOOOo0o * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SPEEDTEST[/COLOR]' , '' , 50004 , IIi1i + 'Speedtest.png' , iIii1 , '' )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , IIi1i + 'View-Log-File.png' , iIii1 , '' )
 i1Ii ( 'DELETE CACHE' , 'url' , 14 , IIi1i + 'DeleteCache.png' , iIii1 , '' )
 i1Ii ( 'DELETE PACKAGES' , 'url' , 6 , IIi1i + 'DeletePackages.png' , iIii1 , '' )
 i1Ii ( 'FORCE REFRESH' , 'url' , 10 , IIi1i + 'ForceRefresh.png' , iIii1 , 'Force Refresh All Repos' )
 if 60 - 60: oOo0O0Ooo * ooOoOO0oOO % oO0o + o000o
 i1Ii ( 'CHECK MY IP' , 'url' , 12 , IIi1i + 'CheckMyIP.png' , iIii1 , '' )
 i1Ii ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , IIi1i + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , iIii1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ADVANCED SETTINGS XML[/COLOR]' , str ( I1ii11iI ) , 4 , IIi1i + 'AdvancedSettingXML.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']URL FIXES[/COLOR]' , str ( I1ii11iI ) , 20 , IIi1i + 'URLFixes.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 52 - 52: ooOoO0O00
 if 84 - 84: OoOOOOOo0o / OO
def i1i1II ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']REPOS[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , IIi1i + 'repos.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NEW[/COLOR]' , str ( I1ii11iI ) , 22 , IIi1i + 'NEW.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']IPTV[/COLOR]' , str ( I1ii11iI ) , 23 , IIi1i + 'IPTV.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']VIDEO[/COLOR]' , str ( I1ii11iI ) , 24 , IIi1i + 'VIDEO.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SPORTS[/COLOR]' , str ( I1ii11iI ) , 25 , IIi1i + 'SPORTS.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']KIDS[/COLOR]' , str ( I1ii11iI ) , 26 , IIi1i + 'KIDS.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']MUSIC[/COLOR]' , str ( I1ii11iI ) , 27 , IIi1i + 'MUSIC.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']PROGRAMS[/COLOR]' , str ( I1ii11iI ) , 28 , IIi1i + 'PROGRAMS.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']XXX[/COLOR]' , 'URL' , 29 , IIi1i + 'XXX.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 86 - 86: OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % iI11I1II1I1I / O0OoO0O00o0oO
 if 11 - 11: oOo0O0Ooo * o000o + Ii1I / Ii1I
def iiii1I1 ( ) :
 oooooOoo0ooo ( )
 i1Ii ( 'CHECK ADVANCED XML' , str ( I1ii11iI ) , 8 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'MUCKYS XML' , str ( I1ii11iI ) + '/wizard/muckys.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( '0CACHE XML' , str ( I1ii11iI ) + '/wizard/0cache.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'MIKEY1234 XML' , str ( I1ii11iI ) + '/wizard/mikey.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'TUXENS XML' , str ( I1ii11iI ) + '/wizard/tuxens.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'P2P RECOMMENDED XML1' , str ( I1ii11iI ) + '/wizard/p2p1.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'P2P RECOMMENDED XML2' , str ( I1ii11iI ) + '/wizard/p2p2.xml' , 7 , IIi1i + 'XML.png' , iIii1 , '' )
 i1Ii ( 'DELETE XML' , str ( I1ii11iI ) , 11 , IIi1i + 'XML.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 14 - 14: OOooOOo * oOo0O0Ooo + ii - iI1i1IiI - OO
def I1iiioOO0OO0O ( ) :
 oooooOoo0ooo ( )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']My Local Zip[/COLOR]' , oO0o0o0ooO0oO , 48 , IIi1i + 'MyLocalZIP.png' , iIii1 , '' )
 i1Ii ( '[COLOR' + i1iiIIiiI111 + ']My Online Zip[/COLOR]' , oOo0oooo00o , 43 , IIi1i + 'MyOnlineZip.png' , iIii1 , '' )
 if 78 - 78: OoOOOOOo0o / IIiIiII11i % OOooOOo
def oO00OoOO ( ) :
 oooooOoo0ooo ( )
 i1Ii ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1ii11iI ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , IIi1i + 'FTV4.png' , iIii1 , '' )
 i1Ii ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1ii11iI ) + '/wizard/customftv/settings.xml' , 17 , IIi1i + 'FTV3.png' , iIii1 , '' )
 i1Ii ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , IIi1i + 'FTV1.png' , iIii1 , '' )
 i1Ii ( 'RESET FTV DATABASE' , 'url' , 18 , IIi1i + 'FTV2.png' , iIii1 , '' )
 if 18 - 18: oO0OOoo0OO - OOooOOo % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
 if 91 - 91: OOooOOo + oO0OOoo0OO . oOo0O0Ooo
 if 71 - 71: iI1i1IiI % I11i / O0OoO0O00o0oO / I1ii11iIi11i
def OO0OO0OO ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SKINS[/COLOR]' , str ( I1ii11iI ) , 33 , IIi1i + 'Skins.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ARTWORK PACKS[/COLOR]' , str ( I1ii11iI ) , 34 , IIi1i + 'ArtworkPacks.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CREATE UNIVERSAL PATHS[/COLOR]' , OOooO0OOoo , 35 , IIi1i + 'CreateUniversalPath.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 61 - 61: ii . o000o . ii / I1ii11iIi11i
def o00O ( ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 iI11Ii = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( OOOO0OOoO0O0 )
 for iI1I , IiII111iI1ii1 in iI11Ii :
  i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iI1I , iI1I , '' )
 O00 ( 'tvshows' , 'INFO' )
 if 48 - 48: iI1i1IiI . Ii
def IIioo0OO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( IiiI11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 5 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 80 - 80: O0OoO0O00o0oO / Ooo0Oo0oOoo / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def iIIiiIIi1IiI ( ) :
 oooooOoo0ooo ( )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']GOTHAM SKINS[/COLOR]' , str ( I1ii11iI ) , 36 , IIi1i + 'GothamSkins.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']HELIX SKINS[/COLOR]' , str ( I1ii11iI ) , 37 , IIi1i + 'HelixSkins.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']ISENGAARD SKINS[/COLOR]' , OOooO0OOoo , 38 , IIi1i + 'IsengaardSkins.png' , iIii1 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 14 - 14: OO % o000o % I1ii11iIi11i - Ii
def o0OO000ooOo ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + oOo00OooO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 16 - 16: OO / I1ii11iIi11i + O0OoO0O00o0oO / OoOOOOOo0o
def IIIiiI1 ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + O0O0ooOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 70 - 70: oO0OOoo0OO . o0o00Oo0O . ooOoOO0oOO . o0o00Oo0O + ooOoO0O00
def i1II1I ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + OOoO0ooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 24 - 24: ooOoO0O00 . Ii
def IIIII1iii11 ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 35 - 35: o000o / ooOoOO0oOO / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . ooOoOO0oOO
def O0O00O000OOO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + iIOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 40 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 1 - 1: o0o00Oo0O / iI1i1IiI % ooOoOO0oOO . I1ii11iIi11i + OO
def I1Ii11iiiI ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + i1II1IiIII111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 5 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 50 - 50: IIiIiII11i * Ii1I / OoOOOOOo0o . I11i + I1ii11iIi11i - O0OoO0O00o0oO
def II1iiIiIiI ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']APK (Android only)[/COLOR]' , str ( I1ii11iI ) , 2 , IIi1i + 'APKAndroidOnly.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']APK Search[/COLOR]' , str ( I1ii11iI ) , 30038 , IIi1i + 'APKSearch.png' , iIii1 , '' )
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + Ooo0Oo0oOoo
def IiiIi ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20vZ2FtZS8=' ) )
 iI11Ii = re . compile ( 'href="([^"]*)">GAME</a>' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'href="([^"]*)">APP</a>' ) . findall ( o00o )
 for iI11I1II in iI11Ii :
  i11II1I11I1 ( 'Android Apps' , ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + iI11I1II , 30036 , IIi1i + 'apps.png' )
 for iI11I1II in i1iIIIi1i :
  i11II1I11I1 ( 'Android Games' , ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + iI11I1II , 30035 , IIi1i + 'GAMES.png' )
 O00 ( 'movies' , 'MAIN' )
def iIIi ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if '/game' in url :
   i11II1I11I1 ( ( IiII111iI1ii1 ) . replace ( '&amp;' , ' - ' ) , ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , IIi1i + 'APK.png' )
def ooO00O00oOO ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if '/app' in url :
   i11II1I11I1 ( ( IiII111iI1ii1 ) . replace ( '&amp;' , ' - ' ) , ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , IIi1i + 'APK.png' )
def I1IIII1ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( ' <img src="([^"]*)".+?title="([^"]*)">.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'href="([^"]*)">NEXT </a>' ) . findall ( o00o )
 for iI1I , IiII111iI1ii1 , url in iI11Ii :
  i11II1I11I1 ( ( IiII111iI1ii1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , url , 19 , iI1I )
 for url in i1iIIIi1i :
  i11II1I11I1 ( 'NEXT' , ( Oo0o0000o0o0 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , IIi1i + 'Next.png' )
def IiIIi1I1I11Ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'href="([^"]*)">Download APK from APKCRAFT</a></p>' ) . findall ( o00o )
 for url in iI11Ii :
  o0OO ( url )
def Oo ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11I1 = 'http://apk.koplayer.com/search?q=' + ( i11IIIiI11 ) . replace ( ' ' , '+' ) + '&region='
 IIi1IIIi = III11I1 . lower ( )
 I1IIII1ii ( IIi1IIIi )
 if 23 - 23: IIiIiII11i / o000o
def o0OO ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( iII1Iii1I11i , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , IiII111iI1ii1 + '.apk' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 89 - 89: IIiIiII11i / o000o
def IIo0OoO00 ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , IiII111iI1ii1 + '.mp4' )
 try :
  os . remove ( i1o0oooO )
 except :
  pass
 downloader . download ( url , i1o0oooO , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 18 - 18: o000o - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / iI1i1IiI . oOo0O0Ooo * OOooOOo
def IIiIiiiIIIIi1 ( name , url , description ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , name )
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
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 81 - 81: Ooo0Oo0oOoo / oO0o % ii * o000o / o000o
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
def OoOO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( I1ii11iI + ( Oo0o0000o0o0 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 5 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'INFO' )
 if 32 - 32: OOooOOo * oOo0O0Ooo % oO0OOoo0OO * OoOOOOOo0o . o0o00Oo0O
 if 48 - 48: iI1i1IiI * iI1i1IiI
def I1I1 ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( I1ii11iI + ( Oo0o0000o0o0 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 30015 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 4 - 4: I11i % OOooOOo * O0OoO0O00o0oO
def ii1IiIi11 ( url , iconimage , fanart ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 Oo00o0OO0O00o = url
 iI1I = iconimage
 fanart = fanart
 iI11Ii = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( OOOO0OOoO0O0 )
 for oo00o0 , IiII111iI1ii1 in iI11Ii :
  if '.mp4' in IiII111iI1ii1 :
   i1Ii ( 'Watch VIDEO' , url + '/' + oo00o0 , 222 , iI1I , fanart , '' )
  if 'description' in IiII111iI1ii1 :
   i1Ii ( 'Read Description' , url + '/' + oo00o0 , 30017 , iI1I , fanart , '' )
  if 'images' in IiII111iI1ii1 :
   ii111iI1iIi1 ( 'View Images' , url + '/' + oo00o0 , 30018 , iI1I , fanart , '' )
  if 'url' in IiII111iI1ii1 :
   i1Ii ( 'Install Build On Android' , url + '/' + oo00o0 , 30016 , iI1I , fanart , '' )
  if 'url' in IiII111iI1ii1 :
   i1Ii ( 'Install Build On Pc' , url + '/' + oo00o0 , 30019 , iI1I , fanart , '' )
 O00 ( 'movies' , 'INFO' )
 if 22 - 22: o000o
def ii1ii ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'url="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for url in iI11Ii :
  oOoooO00O ( url )
  if 6 - 6: OoOOOOOo0o % ooOoO0O00 . OoOOOOOo0o * OoOOOOOo0o
def o0Oo ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'url="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for url in iI11Ii :
  oo0ooO0 ( url )
  if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + o000o
def i1oOOOOOOOoO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'desc="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for I1IIiI in iI11Ii :
  Iii1I1I11iiI1 ( 'Description:' , I1IIiI )
  if 84 - 84: Ooo0Oo0oOoo - I1ii11iIi11i / o0o00Oo0O - ooOoOO0oOO
def ii1iI1II11ii ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 url = url
 iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOOO0OOoO0O0 )
 for oo00o0 , IiII111iI1ii1 in iI11Ii :
  if 'png' in IiII111iI1ii1 :
   i1Ii ( 'image' , '' , '' , url + '/' + oo00o0 , url + '/' + oo00o0 , '' )
 O00 ( 'movies' , 'MAIN' )
 if 8 - 8: oO0OOoo0OO * o0o00Oo0O
def OOoO ( name , url , description ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
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
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1I11I ( )
 if 89 - 89: oO0o / oOo0O0Ooo
 if 16 - 16: I1ii11iIi11i + oO0OOoo0OO / I1ii11iIi11i / oO0o % o000o % Ii1I
def oo0ooO0 ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , 'plugin.program.GenieTv.install' + '.zip' )
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
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 59 - 59: o0o00Oo0O % I1ii11iIi11i
def oOoooO00O ( url ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , 'plugin.program.GenieTv.install' + '.zip' )
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
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 92 - 92: OoOOOOOo0o % iI1i1IiI / Ii1I % Ii1I * oOo0O0Ooo
def OooO00oOOo0Oo ( name , url , description ) :
 IiIIII = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 i1o0oooO = os . path . join ( oO0o0o0ooO0oO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IiIIII
 print '======================================='
 extract . all ( i1o0oooO , IiIIII , o0oOoO00o )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0oOO0ooOoO ( )
 if 5 - 5: I11i . o0o00Oo0O / I1ii11iIi11i % oO0o
 if 60 - 60: IIiIiII11i / iI11I1II1I1I + Ii1I . Ii
def o0oOO0ooOoO ( ) :
 o0o0OoOo0O0OO = DIALOG . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o0o0OoOo0O0OO == 0 : return
 elif o0o0OoOo0O0OO == 1 : pass
 i1iiIIIi = platform ( )
 log ( "Platform: " + str ( i1iiIIIi ) )
 os . _exit ( 1 )
 log ( "Force close failed!  Trying alternate methods." )
 if i1iiIIIi == 'osx' :
  log ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  DIALOG . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1iiIIIi == 'linux' :
  log ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  DIALOG . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1iiIIIi == 'android' :
  log ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  DIALOG . ok ( ADDONTITLE , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif i1iiIIIi == 'windows' :
  log ( "############ try windows force close #################" )
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
  DIALOG . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  log ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  log ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  DIALOG . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 62 - 62: o0o00Oo0O / oOo0O0Ooo % o0o00Oo0O * oO0o % oOo0O0Ooo
  if 33 - 33: oOo0O0Ooo . o000o * oO0o * iI11I1II1I1I
  if 5 - 5: I1ii11iIi11i / OO % o0o00Oo0O . ooOoOO0oOO * OO
def ooOooOoOoO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( url ) :
  for file in OO0oIII111i11IiI :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    Ii1iI111 = open ( ( os . path . join ( ooOOooo0Oo , file ) ) ) . read ( )
    oo0O0o = Ii1iI111 . replace ( OOooO0OOoo , 'special://home/' )
    o0OIiII = open ( ( os . path . join ( ooOOooo0Oo , file ) ) , mode = 'w' )
    o0OIiII . write ( str ( oo0O0o ) )
    o0OIiII . close ( )
 o0oOO0ooOoO ( )
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * OO / I11i
def I1iiIII ( ) :
 i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']GENRE[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , IIi1i + 'radio.png' )
 i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']SORT BY[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , IIi1i + 'radio.png' )
 i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']SEARCH[/COLOR]' ) , '' , 70006 , IIi1i + 'radio.png' )
 if 16 - 16: o000o + oO0OOoo0OO / I11i
def O00oOoo0OoO0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , IIi1i + 'radio.png' )
def Ooo0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , IIi1i + 'radio.png' )
def oooO00o0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in i1iIIIi1i :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']Filter - ' + IiII111iI1ii1 + '[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , IIi1i + 'radio.png' )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']Stream - ' + IiII111iI1ii1 + '[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iI1I )
def o0o00oO0oo000 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( o00o )
 for url in iI11Ii :
  oO000o ( url )
def o0Ooo0O0 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11
 I1I1Iiii1 = 'https://www.radionomy.com/en/search/index?query=' + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 OO0O0OoOO0 = O00OOOoOoo0O ( I1I1Iiii1 )
 iI11Ii = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']Stream - ' + IiII111iI1ii1 + '[/COLOR]' ) , ( Oo0o0000o0o0 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iI11I1II , 70005 , iI1I )
  if 2 - 2: Ooo0Oo0oOoo + oO0OOoo0OO
  if 76 - 76: ooOoOO0oOO
def OoOoOo0 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , 'http://www.listenlive.eu/' + iI11I1II , 10111113 , IIi1i + 'radio.png' )
def i1II11II1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , url in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , url , 222 , IIi1i + 'radio.png' )
  if 5 - 5: I1ii11iIi11i - Ii1I % o000o - IIiIiII11i . oOo0O0Ooo + iI1i1IiI
def iiIi1I1i1 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.toonjet.com/' + iI11I1II , 8051 , IIi1i + 'classictoons.png' )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOIiIi1111ii ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( o00o )
 for url , iI1I in iI11Ii :
  if 'ol.gif' in iI1I :
   pass
  elif 'link_block_' in iI1I :
   pass
  elif '.png' in iI1I :
   pass
  else :
   i11II1I11I1 ( ( iI1I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , IIi1i + 'vod.png' )
 for url in i1iIIIi1i :
  i11II1I11I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , IIi1i + 'Next.png' )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1I1II1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( o00o )
 for url in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , IIi1i + 'classictoons.png' )
  if 92 - 92: ii - ii * oO0o % oOo0O0Ooo
  if 77 - 77: iI11I1II1I1I - ooOoO0O00 . o000o
def iIi1iIIIiIiI ( ) :
 OooOo000o0o ( 'Audio Books' , '' , 30011 , IIi1i + 'AudioBooks.png' , IIi1i + 'AudioBooks.png' , '' )
 OooOo000o0o ( 'Kids Audio Books' , '' , 30006 , IIi1i + 'KidsAudioBooks.png' , IIi1i + 'KidsAudioBooks.png' , '' )
 if 42 - 42: o000o % O0OoO0O00o0oO
def OOO0 ( ) :
 OooOo000o0o ( 'All' , '' , 30001 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'Popular' , '' , 30012 , IIi1i + 'POPULARv.png' , IIi1i + 'POPULARv.png' , '' )
 OooOo000o0o ( 'Search' , '' , 30013 , IIi1i + 'Search.png' , IIi1i + 'Search.png' , '' )
 if 10 - 10: I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo00OOOOO + 'books' + O0o0Oo )
 iI11Ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , iI11I1II , Oo0O0O000 in iI11Ii :
  if 'Parent' in IiII111iI1ii1 :
   pass
  elif '2' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
def oO00 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo00OOOOO + 'books' + O0o0Oo )
 iI11Ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , iI11I1II , Oo0O0O000 in iI11Ii :
  if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
   if '1' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   elif '2' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   elif '3' in Oo0O0O000 :
    OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30009 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
    if 1 - 1: o000o
    if 12 - 12: oO0OOoo0OO % oOo0O0Ooo + o000o - ooOoO0O00 . OoOOOOOo0o / oOo0O0Ooo
def o0IiiiI111I ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo00OOOOO + 'books' + O0o0Oo )
 iI11Ii = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , iI11I1II , Oo0O0O000 in iI11Ii :
  if '1' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 3010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  elif '2' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  elif '3' in Oo0O0O000 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI11I1II , 30009 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: I11i * OoOOOOOo0o + Ooo0Oo0oOoo + iI1i1IiI
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I11i / O0OoO0O00o0oO / OO % oO0OOoo0OO + IIiIiII11i
def I1III111i ( url ) :
 oo00o0 = url
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 i1iIIIi1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in i1iIIIi1i :
  if 'mp3' in IiII111iI1ii1 :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  if 'wma' in IiII111iI1ii1 :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in IiII111iI1ii1 :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00o0 + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  elif '/' in IiII111iI1ii1 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 30009 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 4 - 4: ooOoO0O00 + oO0OOoo0OO + ooOoO0O00
   if 31 - 31: OoOOOOOo0o
   if 78 - 78: Ii + I11i + ooOoOO0oOO / I11i % iI11I1II1I1I % OO
def Oo0O0Oo00O ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 oo00o0 = url
 iI11Ii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  if 'Parent' in IiII111iI1ii1 :
   pass
  elif '.db' in IiII111iI1ii1 :
   pass
  elif '.jpg' in IiII111iI1ii1 :
   pass
  elif '.html' in IiII111iI1ii1 :
   pass
  elif '.doc' in IiII111iI1ii1 :
   pass
  elif 'mp3' in IiII111iI1ii1 :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in IiII111iI1ii1 :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  else :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00o0 + url , 30010 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: I11i . oOo0O0Ooo - Ii1I
   if 32 - 32: ii / oOo0O0Ooo / iI11I1II1I1I + IIiIiII11i . o000o . I11i
def ii1iiIIiI1i ( ) :
 OooOo000o0o ( 'A-Z' , '' , 30007 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'All' , '' , 30003 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
 OooOo000o0o ( 'Search' , '' , 30014 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
 if 6 - 6: Ii1I / iI1i1IiI - O0OoO0O00o0oO
def o00O00Oo00O ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 iI11Ii = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I in iI11Ii :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iI11I1II + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iI1I :
   pass
  else :
   OooOo000o0o ( iI1I , ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iI11I1II ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iI1I + '.gif' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 46 - 46: OOooOOo % ooOoO0O00 / o000o * I1ii11iIi11i * O0OoO0O00o0oO
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: OOooOOo * OOooOOo . OOooOOo + OoOOOOOo0o / o000o
 if 13 - 13: iI1i1IiI
def o0OOOOO0O ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  if '</a>' in IiII111iI1ii1 :
   pass
  elif '(' in IiII111iI1ii1 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  else :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: OoOOOOOo0o - OoOOOOOo0o + ooOoO0O00 - o0o00Oo0O - ooOoOO0oOO
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: OOooOOo - iI1i1IiI - ii
def o00ii111Iiii ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI11Ii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
   if '</a>' in IiII111iI1ii1 :
    pass
   elif '(' in IiII111iI1ii1 :
    OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI11I1II , 30005 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   else :
    ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI11I1II , 30004 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
    if 54 - 54: ii - oOo0O0Ooo % Ii1I
    if 92 - 92: oO0o * oO0OOoo0OO
def i1iIIi1o0o0OoOOOOOo ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 iI11Ii = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if '</a>' in IiII111iI1ii1 :
   pass
  elif '(' in IiII111iI1ii1 :
   OooOo000o0o ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI11I1II , 30005 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
  else :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI11I1II , 30004 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 39 - 39: ii * O0OoO0O00o0oO * o0o00Oo0O . Ooo0Oo0oOoo . oO0o + oO0OOoo0OO
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: OOooOOo + o000o % ii + I11i
 if 56 - 56: ii + Ii1I - iI1i1IiI
def III1I1 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( OO0O0OoOO0 )
 for url in iI11Ii :
  oo00o0 = ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oo00o0 )
  if 12 - 12: iI11I1II1I1I % oO0OOoo0OO % oO0OOoo0OO
def o0i1iI1iiI1I ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , url in iI11Ii :
  if '<p align' in IiII111iI1ii1 :
   pass
  elif '&nbsp;' in IiII111iI1ii1 :
   pass
  else :
   ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , IIi1i + 'KodibleAudioBooks.png' , IIi1i + 'KodibleAudioBooks.png' , '' )
   if 52 - 52: oO0o % OoOOOOOo0o * IIiIiII11i
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: Ooo0Oo0oOoo % o0o00Oo0O - ii + oO0OOoo0OO . o000o % IIiIiII11i
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
def II1 ( ) :
 OO0O0OoOO0 = cloudflare . source ( Oo0o0000o0o0 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 iI11Ii = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'ongoing' in iI11I1II :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 21005 , IIi1i + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in iI11I1II :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 21005 , IIi1i + 'CartoonShows.png' , '' , '' )
  if 'disney' in iI11I1II :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 21005 , IIi1i + 'Disney.png' , '' , '' )
  if 'genre' in iI11I1II :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 21005 , IIi1i + 'Genre.png' , '' , '' )
  if 'years' in iI11I1II :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 21005 , IIi1i + 'Years.png' , '' , '' )
def I11Iii1 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIi1II1iiI = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iI1I , iI1I , IiII111iI1ii1 )
 for url , IiII111iI1ii1 in i1iIIi1II1iiI :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 21005 , IIi1i + 'watchcartoons.png' , '' , '' )
 for url in next :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT[/COLOR]' , url , 21005 , IIi1i + 'Next.png' , '' , '' )
def III1Ii1i1I1 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 O0O00OooO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 I1IiI1iI11 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OO0O0OoOO0 )
 iIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , IIi1i + 'watchcartoons.png' , '' , '' )
 for url in I1IiI1iI11 :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']PLAY[/COLOR]' , 'http:' + url , 222 , IIi1i + 'watchcartoons.png' , '' , '' )
 for url , IiII111iI1ii1 in O0O00OooO :
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 222 , IIi1i + 'watchcartoons.png' , '' , '' )
 else :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , IIi1i + 'watchcartoons.png' , '' , '' )
def iiO0O0o0oO0O00 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  i1Ii ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 222 , IIi1i + 'watchcartoons.png' , '' , '' )
  if 70 - 70: ooOoOO0oOO + o000o
def o00ooo0 ( ) :
 i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']CARTOONS[/COLOR]' , '' , 20001 , IIi1i + 'ORIGINCARTOON.png' )
 i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , IIi1i + 'ORIGINCARTOON.png' )
 if 39 - 39: oO0OOoo0OO . IIiIiII11i
def iIiIi1iI11iiI ( ) :
 i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , IIi1i + 'ORIGINCARTOON.png' )
 i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , IIi1i + 'ORIGINCARTOON.png' )
 if 26 - 26: iI11I1II1I1I * ooOoOO0oOO - O0OoO0O00o0oO
def III1II111Ii1 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( 'href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  if '?c=' in url :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , IIi1i + 'ORIGINCARTOON.png' )
   if 82 - 82: ooOoOO0oOO - O0OoO0O00o0oO + oO0o
def OO0iIiiIi11IIi ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( 'href="([^"]*)" title="([^"]*)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , Oo0 , IiII111iI1ii1 in iI11Ii :
  if 'Genre' in url :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , IIi1i + 'ORIGINCARTOON.png' )
   if 60 - 60: I11i . I11i / iI1i1IiI
def Iio00 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( 'src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , Oo0 , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Oo0 )
  if 46 - 46: iI11I1II1I1I * ooOoOO0oOO - iI11I1II1I1I . OOooOOo - ooOoOO0oOO
def Iii ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( '<img width="120" height="165" src="([^"]*)" style=.+?<a class="bigChar" href="([^"]*)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , Oo0 , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , Oo0 )
  if 31 - 31: ii + iI1i1IiI - OOooOOo . ooOoO0O00 % iI1i1IiI
  if 43 - 43: O0OoO0O00o0oO * oO0OOoo0OO / iI11I1II1I1I - OoOOOOOo0o * OoOOOOOo0o
  if 60 - 60: iI11I1II1I1I . O0OoO0O00o0oO + Ii1I
  if 44 - 44: o0o00Oo0O . o000o * Ii % Ii + o0o00Oo0O / O0OoO0O00o0oO
  if 89 - 89: OoOOOOOo0o % ooOoO0O00 % o000o
def oOooO0O0OoooO ( ) :
 if 10 - 10: I11i % OoOOOOOo0o / O0OoO0O00o0oO
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Cartoons[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , IIi1i + 'ORIGINCARTOON.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Search Cartoons[/COLOR]' , '' , 10005 , IIi1i + 'ORIGINCARTOON.png' , iIii1 , '' )
 if 28 - 28: O0OoO0O00o0oO % oO0OOoo0OO
def iiIiII11i1 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 93 - 93: OOooOOo % iI11I1II1I1I
 iI11Ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OO0O0OoOO0 )
 if 90 - 90: oOo0O0Ooo - O0OoO0O00o0oO / OoOOOOOo0o / o0o00Oo0O / Ooo0Oo0oOoo
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
   if 'Dad!' in IiII111iI1ii1 :
    pass
   elif 'Family Guy' in IiII111iI1ii1 :
    pass
   elif '2 Stupid' in IiII111iI1ii1 :
    pass
   elif 'The Zelfs' in IiII111iI1ii1 :
    pass
   elif 'A Clone' in IiII111iI1ii1 :
    pass
   elif 'A.T.O.M' in IiII111iI1ii1 :
    pass
   elif 'Almost Naked' in IiII111iI1ii1 :
    pass
   elif 'Angry Kid' in IiII111iI1ii1 :
    pass
   elif 'Annoying Orange' in IiII111iI1ii1 :
    pass
   elif 'Aqua Teen' in IiII111iI1ii1 :
    pass
   elif 'Assy Mcgee' in IiII111iI1ii1 :
    pass
   elif 'Astroblast' in IiII111iI1ii1 :
    pass
   elif 'Atomic Betty' in IiII111iI1ii1 :
    pass
   elif 'Axe Cop' in IiII111iI1ii1 :
    pass
   elif 'Baby Playpen' in IiII111iI1ii1 :
    pass
   elif 'Beavis and Butt' in IiII111iI1ii1 :
    pass
   elif 'Celebrity Deathmatch' in IiII111iI1ii1 :
    pass
   elif 'Clerks The' in IiII111iI1ii1 :
    pass
   elif 'Crapston Villas' in IiII111iI1ii1 :
    pass
   elif 'Duckman:' in IiII111iI1ii1 :
    pass
   elif 'Stripperella' in IiII111iI1ii1 :
    pass
   elif 'Vixen' in IiII111iI1ii1 :
    pass
   else :
    ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 10006 , IIi1i + 'ORIGINCARTOON.png' , iIii1 , '' )
    if 87 - 87: OOooOOo / OO + iI11I1II1I1I
    if 93 - 93: iI11I1II1I1I + o000o % oO0OOoo0OO
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: O0OoO0O00o0oO
def iIiI1I1IIi11 ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if 'Dad!' in IiII111iI1ii1 :
   pass
  elif 'Family Guy' in IiII111iI1ii1 :
   pass
  elif '2 Stupid' in IiII111iI1ii1 :
   pass
  elif 'The Zelfs' in IiII111iI1ii1 :
   pass
  elif 'A Clone' in IiII111iI1ii1 :
   pass
  elif 'A.T.O.M' in IiII111iI1ii1 :
   pass
  elif 'Almost Naked' in IiII111iI1ii1 :
   pass
  elif 'Angry Kid' in IiII111iI1ii1 :
   pass
  elif 'Annoying Orange' in IiII111iI1ii1 :
   pass
  elif 'Aqua Teen' in IiII111iI1ii1 :
   pass
  elif 'Assy Mcgee' in IiII111iI1ii1 :
   pass
  elif 'Astroblast' in IiII111iI1ii1 :
   pass
  elif 'Atomic Betty' in IiII111iI1ii1 :
   pass
  elif 'Axe Cop' in IiII111iI1ii1 :
   pass
  elif 'Baby Playpen' in IiII111iI1ii1 :
   pass
  elif 'Beavis and Butt' in IiII111iI1ii1 :
   pass
  elif 'Celebrity Deathmatch' in IiII111iI1ii1 :
   pass
  elif 'Clerks The' in IiII111iI1ii1 :
   pass
  elif 'Crapston Villas' in IiII111iI1ii1 :
   pass
  elif 'Duckman:' in IiII111iI1ii1 :
   pass
  elif 'Stripperella' in IiII111iI1ii1 :
   pass
  elif 'Vixen' in IiII111iI1ii1 :
   pass
  else :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 10006 , IIi1i + 'ORIGINCARTOON.png' , iIii1 , '' )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: oO0OOoo0OO + iI1i1IiI - Ooo0Oo0oOoo / ooOoO0O00 % Ii1I / OO
def oo0oO0oO ( url ) :
 o00o = O00OOOoOoo0O ( url )
 i1iIIIi1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o00o )
 for iI1I in i1iIIIi1i :
  IIiIi11iiIi = iI1I
 i11iI11I1I = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o00o )
 for url in i11iI11I1I :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT PAGE[/COLOR]' , url , 10006 , IIi1i + 'Next.png' , iIii1 , '' )
 iI11Ii = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 10007 , IIiIi11iiIi )
  if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
  if 95 - 95: OoOOOOOo0o % OO . o0o00Oo0O % ooOoOO0oOO
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / Ooo0Oo0oOoo . oO0OOoo0OO / ooOoO0O00
def iI1i1iIi1iiII ( url , IMAGE ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o00o )
 for IiII111iI1ii1 , url in iI11Ii :
  print IiII111iI1ii1 + '     ' + url
  if 'easy' in url :
   o0OoO0000o ( url )
   if 90 - 90: OO . oO0OOoo0OO / iI11I1II1I1I
   if 28 - 28: OO + o000o - oO0OOoo0OO / iI11I1II1I1I - oOo0O0Ooo
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * o000o * oO0o
def o0OoO0000o ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( "url: '(.+?)'," ) . findall ( o00o )
 for url in iI11Ii :
  oO000o ( url )
  if 35 - 35: Ii1I / iI1i1IiI % oOo0O0Ooo + iI11I1II1I1I
  if 79 - 79: OOooOOo / oO0OOoo0OO
  if 77 - 77: I1ii11iIi11i
def i1i111Iiiiiii ( ) :
 if 19 - 19: oOo0O0Ooo . I1ii11iIi11i + ii - oOo0O0Ooo
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Stand Up[/COLOR]' , '' , 10014 , IIi1i + 'StandUp.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Search Comedian[/COLOR]' , '' , 10015 , IIi1i + 'SearchComedian.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Others[/COLOR]' , '' , 10017 , IIi1i + 'Others.png' , iIii1 , '' )
 if 93 - 93: iI11I1II1I1I + oOo0O0Ooo + Ii
def O0Oo0 ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( ( Oo0o0000o0o0 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  if 'elete' in IiII111iI1ii1 :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 222 , iI1I )
   if 99 - 99: Ii1I . oO0o * Ooo0Oo0oOoo % ooOoOO0oOO
def II1Ii ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 OO0O0OoOO0 = O00OOOoOoo0O ( ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1iiII1i = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , oO00O , i1iII1IiiIiI1 in Ii1iiII1i :
  for i11IIIiI11 in oO00O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIiI11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iI11I1II , IiII111iI1ii1 in IIiI11 :
    if 'tube' in iI11I1II :
     pass
    elif 'stage' in iI11I1II :
     OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + oO00O + '   -   ' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iI1I , )
    elif 'vee' in iI11I1II :
     pass
     if 9 - 9: oO0OOoo0OO + IIiIiII11i % oO0OOoo0OO % OO + iI11I1II1I1I
def oO00IiI1II11iiI ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 Ii1iiII1i = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , oO00O , i1iII1IiiIiI1 in Ii1iiII1i :
  IIiI11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iI11I1II , IiII111iI1ii1 in IIiI11 :
   if 'tube' in iI11I1II :
    pass
   elif 'stage' in iI11I1II :
    OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + oO00O + '   -   ' + IiII111iI1ii1 + '[/COLOR]' , ( iI11I1II ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iI1I )
   elif 'vee' in iI11I1II :
    pass
    if 56 - 56: iI1i1IiI
    if 84 - 84: OOooOOo - Ii
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: iI1i1IiI * OOooOOo
def OO0ooo0 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( OO0O0OoOO0 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OOo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OOo :
  oO000o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 7 - 7: Ii1I - o000o * O0OoO0O00o0oO + I11i . Ii1I
  if 85 - 85: o0o00Oo0O
  if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * OoOOOOOo0o
  if 19 - 19: OoOOOOOo0o
  if 55 - 55: O0OoO0O00o0oO % O0OoO0O00o0oO / o0o00Oo0O % iI1i1IiI - I11i . I1ii11iIi11i
  if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
  if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
def IIiI11I1I1i1i ( ) :
 if 86 - 86: ooOoO0O00
 i1o0oo0Ooooo0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , iIii1 , '' )
 i1o0oo0Ooooo0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIii1 , '' )
 if 76 - 76: ooOoO0O00 * ii * o0o00Oo0O + ooOoOO0oOO * ooOoOO0oOO
 O00 ( 'movies' , 'MAIN' )
 if 35 - 35: I11i
def ooOoooo0 ( ) :
 i1o0oo0Ooooo0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIii1 , '' )
 i1o0oo0Ooooo0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , iIii1 , '' )
 if 54 - 54: ooOoO0O00 . Ooo0Oo0oOoo - Ii1I + oO0OOoo0OO + I1ii11iIi11i / I1ii11iIi11i
 O00 ( 'movies' , 'MAIN' )
def i1i ( ) :
 if 12 - 12: OoOOOOOo0o
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 Ooii1IIi1ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
 for IiI in Ooii1IIi1ii :
  o0o0OO0o00o0O = O000oo0O + IiI + O0o0Oo
  OO0O0OoOO0 = oO0Oo ( o0o0OO0o00o0O )
  iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0O0OoOO0 )
  for iI11I1II , iII1 , ooo0O , o0Oo00 , IiII111iI1ii1 in iI11Ii :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    IIIIIIi1i ( IiII111iI1ii1 , iI11I1II , 222 , iII1 , o0Oo00 , ooo0O )
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
    O00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 68 - 68: O0OoO0O00o0oO + o000o . o0o00Oo0O . OoOOOOOo0o % ooOoO0O00 % O0OoO0O00o0oO
    if 50 - 50: OO + I11i
def o0OoOOo ( ) :
 if 56 - 56: Ooo0Oo0oOoo / iI11I1II1I1I + OOooOOo % O0OoO0O00o0oO . O0OoO0O00o0oO - Ii1I
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 Ooii1IIi1ii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 48 - 48: I1ii11iIi11i - oO0OOoo0OO + I1ii11iIi11i - oOo0O0Ooo * Ii . iI1i1IiI
 for IiI in Ooii1IIi1ii :
  I1iIIIiI = O000oo0O + IiI + O0o0Oo
  OO0O0OoOO0 = oO0Oo ( I1iIIIiI )
  iI11Ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for IiII111iI1ii1 , ooo0O , iI11I1II , iI1I , o0Oo00 , OoiI1I1 in iI11Ii :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i1o0oo0Ooooo0 ( IiII111iI1ii1 , iI11I1II , OoiI1I1 , iI1I , o0Oo00 , ooo0O )
    if 27 - 27: oO0OOoo0OO - I1ii11iIi11i + iI1i1IiI - O0OoO0O00o0oO . oOo0O0Ooo
    O00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 51 - 51: o000o + oO0o + iI1i1IiI + iI1i1IiI % I11i
    if 29 - 29: oO0OOoo0OO
def ii1iIi1Ii1 ( ) :
 if 66 - 66: oO0o % I11i
 o00o = O00OOOoOoo0O ( O000oo0O + 'spongemain.php' )
 iI11Ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , ooo0O , iI11I1II , iI1I , o0Oo00 , OoiI1I1 in iI11Ii :
  i1o0oo0Ooooo0 ( IiII111iI1ii1 , iI11I1II , OoiI1I1 , iI1I , o0Oo00 , ooo0O )
  O00 ( 'movies' , 'MAIN' )
def iI1ii11Ii ( url ) :
 if 97 - 97: ooOoOO0oOO + o000o - oO0o % o000o - I11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1iiiiI1IiIIii = ( '%s%s' % ( IIIIiii , url ) )
 OOOO0OOoO0O0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOO0OOoO0O0 )
 for url , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in iI11Ii :
  OOOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( I1IIiiIiii ) )
  for i1I111i1ii in OOOo00 :
   if i1I111i1ii == url :
    IiII111iI1ii1 = ( '[COLORred]Watched - [/COLOR]' + IiII111iI1ii1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IIIIIIi1i ( IiII111iI1ii1 , url , 222 , iII1 , Ii11Ii1iI , ooo0O )
  if 81 - 81: I1ii11iIi11i - Ooo0Oo0oOoo
  O00 ( 'movies' , 'MAIN' )
  if 24 - 24: ii . oO0o * IIiIiII11i
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: ooOoOO0oOO + oO0o / O0OoO0O00o0oO
  if 97 - 97: I1ii11iIi11i * iI1i1IiI % oO0OOoo0OO . iI1i1IiI - ooOoOO0oOO - O0OoO0O00o0oO
def oo0O0o00 ( url ) :
 if 39 - 39: oO0OOoo0OO + o0o00Oo0O / ooOoO0O00 % OO / o000o * OO
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , ooo0O , url , iI1I , o0Oo00 , OoiI1I1 in iI11Ii :
  i1o0oo0Ooooo0 ( IiII111iI1ii1 , url , OoiI1I1 , iI1I , o0Oo00 , ooo0O )
  if 77 - 77: OO . ooOoOO0oOO % OOooOOo
  O00 ( 'movies' , 'MAIN' )
  if 42 - 42: OO % iI1i1IiI % I11i % o000o + Ooo0Oo0oOoo % OOooOOo
  if 3 - 3: o000o
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: oO0o . oOo0O0Ooo - ii . oO0OOoo0OO - iI1i1IiI
def IIIIIIi1i ( name , url , mode , iconimage , fanart , description ) :
 if 77 - 77: OoOOOOOo0o % OOooOOo / IIiIiII11i % iI1i1IiI % ii % oO0o
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1i1i . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = False )
 return iI1
 if 87 - 87: OOooOOo / OO . oO0OOoo0OO - O0OoO0O00o0oO / oO0o
def i1o0oo0Ooooo0 ( name , url , mode , iconimage , fanart , description ) :
 if 41 - 41: IIiIiII11i
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1i1i . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = True )
 return iI1
if 27 - 27: I1ii11iIi11i * OOooOOo % iI11I1II1I1I . oOo0O0Ooo
if 70 - 70: Ooo0Oo0oOoo % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / ooOoOO0oOO
if 100 - 100: Ii1I * Ii % o000o / I1ii11iIi11i / oO0OOoo0OO + Ii1I
if 59 - 59: ooOoOO0oOO - OO
if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
if 5 - 5: OO
if 84 - 84: IIiIiII11i * o000o * IIiIiII11i % OO / oOo0O0Ooo
if 100 - 100: OO . OoOOOOOo0o - iI11I1II1I1I . Ii / IIiIiII11i
if 71 - 71: ooOoOO0oOO * I1ii11iIi11i . Ooo0Oo0oOoo
if 49 - 49: OO * o0o00Oo0O . OO
if 19 - 19: IIiIiII11i - OO
if 59 - 59: I11i * oO0o - OoOOOOOo0o . O0OoO0O00o0oO
if 89 - 89: O0OoO0O00o0oO
if 69 - 69: oO0OOoo0OO - ii * o0o00Oo0O
if 84 - 84: oO0OOoo0OO + Ii - O0OoO0O00o0oO * oO0OOoo0OO
def I1IiiIiii1 ( string ) :
 if I11i1I1I == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 39 - 39: oO0OOoo0OO / o0o00Oo0O * OO
def I1IiI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1iI1oOOO00OOOoOO = [ ]
 try :
  if 23 - 23: OOooOOo . I11i - oO0o / OOooOOo * iI11I1II1I1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIiiiiiiIi1I1 ) == False :
  I1IiiIiii1 ( 'Making Favorites File' )
  I1iI1oOOO00OOOoOO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Ii1iI111 = open ( IIiiiiiiIi1I1 , "w" )
  Ii1iI111 . write ( json . dumps ( I1iI1oOOO00OOOoOO ) )
  Ii1iI111 . close ( )
 else :
  I1IiiIiii1 ( 'Appending Favorites' )
  Ii1iI111 = open ( IIiiiiiiIi1I1 ) . read ( )
  IIiiiiiIiIIi = json . loads ( Ii1iI111 )
  IIiiiiiIiIIi . append ( ( name , url , iconimage , fanart , mode ) )
  oo0O0o = open ( IIiiiiiiIi1I1 , "w" )
  oo0O0o . write ( json . dumps ( IIiiiiiIiIIi ) )
  oo0O0o . close ( )
  if 26 - 26: I11i
  if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
def Ii11ii1I1 ( ) :
 if os . path . exists ( IIiiiiiiIi1I1 ) == False :
  I1iI1oOOO00OOOoOO = [ ]
  I1IiiIiii1 ( 'Making Favorites File' )
  I1iI1oOOO00OOOoOO . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Ii1iI111 = open ( IIiiiiiiIi1I1 , "w" )
  Ii1iI111 . write ( json . dumps ( I1iI1oOOO00OOOoOO ) )
  Ii1iI111 . close ( )
 else :
  Iii11III1I11 = json . loads ( open ( IIiiiiiiIi1I1 ) . read ( ) )
  iii = len ( Iii11III1I11 )
  for IiIIII1iiIIi in Iii11III1I11 :
   IiII111iI1ii1 = IiIIII1iiIIi [ 0 ]
   iI11I1II = IiIIII1iiIIi [ 1 ]
   iII1 = IiIIII1iiIIi [ 2 ]
   try :
    i1I1IiI1ii = IiIIII1iiIIi [ 3 ]
    if i1I1IiI1ii == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     i1I1IiI1ii = iII1
    else :
     i1I1IiI1ii = o0Oo00
   try : O00OOoOOOO00O = IiIIII1iiIIi [ 5 ]
   except : O00OOoOOOO00O = None
   try : Ooo0OOO = IiIIII1iiIIi [ 6 ]
   except : Ooo0OOO = None
   if 94 - 94: Ii % ii / oOo0O0Ooo
   if IiIIII1iiIIi [ 4 ] == 0 :
    ii111iI1iIi1 ( IiII111iI1ii1 , iI11I1II , '' , iII1 , o0Oo00 , '' , 'fav' )
   else :
    ii111iI1iIi1 ( IiII111iI1ii1 , iI11I1II , IiIIII1iiIIi [ 4 ] , iII1 , o0Oo00 , '' , 'fav' )
    if 24 - 24: oOo0O0Ooo * o000o
def Oo0O0000Oo00o ( name ) :
 IIiiiiiIiIIi = json . loads ( open ( IIiiiiiiIi1I1 ) . read ( ) )
 for II1ii in range ( len ( IIiiiiiIiIIi ) ) :
  if IIiiiiiIiIIi [ II1ii ] [ 0 ] == name :
   del IIiiiiiIiIIi [ II1ii ]
   oo0O0o = open ( IIiiiiiiIi1I1 , "w" )
   oo0O0o . write ( json . dumps ( IIiiiiiIiIIi ) )
   oo0O0o . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 89 - 89: iI1i1IiI . Ii * o0o00Oo0O
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OO
def ii1ii111 ( ) :
 iI111II1ii = os . path . join ( II , 'addons.ini' )
 O0ooO00ooOO0o = open ( iI111II1ii , "w+" )
 if 65 - 65: iI1i1IiI . oO0o + OoOOOOOo0o
 O0ooO00ooOO0o . write ( r'# This file contains the "built-in" channels' + '\n' )
 O0ooO00ooOO0o . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 O0ooO00ooOO0o . write ( r'[plugin.video.GenieTv]' + '\n' )
 O0ooO00ooOO0o . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F191.m3u8&mode=10012&name===BBC+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_one.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F190.m3u8&mode=10012&name===BBC+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_two_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BBC Three=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F189.m3u8&mode=10012&name===BBC+Three+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_three.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F188.m3u8&mode=10012&name===BBC+Four+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_four_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F208.m3u8&mode=10012&name===ITV1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv_uk_london.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F207.m3u8&mode=10012&name===ITV2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv2.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F206.m3u8&mode=10012&name===ITV3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv3.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F205.m3u8&mode=10012&name===ITV4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/itv4.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITV Encore=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F328.m3u8&mode=10012&name===ITV+Encore&amp;iconimage=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;fanart=http%3A//j.static-locatetv.com/images/content/mid/3/1026632_the_encore_hour.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ITVBe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F203.m3u8&mode=10012&name===ITV+BE+UK&amp;iconimage=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;fanart=http%3A//hub.tv-ark.org.uk/images/itv/images/itv_be.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'E4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F775.m3u8&mode=10012&name===E4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e4_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'More4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F776.m3u8&mode=10012&name===More4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_more4_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F187.m3u8&mode=10012&name===5%2A+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_star.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F186.m3u8&mode=10012&name===5USA+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_usa.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F183.m3u8&mode=10012&name===Channel+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel4_ie.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F185.m3u8&mode=10012&name===Channel+5+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/channel5_uk.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'alibi HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F329.m3u8&mode=10012&name===Alibi+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/alibi_uktv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Dave HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F325.m3u8&mode=10012&name===Dave+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dave_uktv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F326.m3u8&mode=10012&name===Gold+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/gold_uktv.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F324.m3u8&mode=10012&name===Pick+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/pick_tv.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Really=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F631.m3u8&mode=10012&name===Really&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/really_uktv.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F377.m3u8&mode=10012&name===Yesterday+UK&amp;iconimage=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;fanart=http%3A//lm-media-ltd.net/logos/Yesterday.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F518.m3u8&mode=10012&name===Watch+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/watch_uktv.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBS Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F637.m3u8&mode=10012&name===CBS+Action+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_action.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBS Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F636.m3u8&mode=10012&name===CBC+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_drama.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBS Reality=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F635.m3u8&mode=10012&name===CBS+Reality+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs_reality.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'True Drama=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F634.m3u8&mode=10012&name===True+Drama+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_drama_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Challenge=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F772.m3u8&mode=10012&name===Challenge+UK&amp;iconimage=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;fanart=https%3A//i.ytimg.com/i/RCV-1IVhGZWY1k-Em9QVQA/mq1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F194.m3u8&mode=10012&name===RTE+One+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_one.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F193.m3u8&mode=10012&name===RTE+Two+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/rte_two.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F192.m3u8&mode=10012&name===TG4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tg4.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'3e=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F769.m3u8&mode=10012&name===3e+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/3e_ie.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F774.m3u8&mode=10012&name===TV3+UK&amp;iconimage=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;fanart=https%3A//pbs.twimg.com/profile_images/683994318852485125/eQ0KQ53-.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ComedyXtra=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F767.m3u8&mode=10012&name===Comedy+Central+Extra+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_extra_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F179.m3u8&mode=10012&name===FOX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Syfy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F180.m3u8&mode=10012&name===Syfy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_uk.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TCM=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F632.m3u8&mode=10012&name===TCM+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tcm_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TLC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F768.m3u8&mode=10012&name===TLC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tlc_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Universal HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F404.m3u8&mode=10012&name===Universal+Channel+UK&amp;iconimage=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;fanart=http%3A//theident.gallery/universalhd/2013/misc/UNIVERSAL-2013-PROMO-100PERCENT-1-8.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Universal+1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F771.m3u8&mode=10012&name===Universal+Channel+%2B1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/universal_channel_uk_plus1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F32.m3u8&mode=10012&name===Sky+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_1.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F33.m3u8&mode=10012&name===Sky+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_2.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F35.m3u8&mode=10012&name===Sky+Living+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_living.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F34.m3u8&mode=10012&name===Sky+Atlantic+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_atlantic.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F639.m3u8&mode=10012&name===Food+Network&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/food_network_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F516.m3u8&mode=10012&name===Sky+Movies+Premiere+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_premiere.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F732.m3u8&mode=10012&name===Sky+Movies+Action+%26+Adventure+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_action_adventure.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F514.m3u8&mode=10012&name===Sky+Movies+Crime+%26+Thriller+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_crime_thriller.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F511.m3u8&mode=10012&name===Sky+Movies+Sci-Fi+%26+Horror+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_scifi_horror.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F513.m3u8&mode=10012&name===Sky+Movies+Comedy+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_comedy.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F512.m3u8&mode=10012&name===Sky+Movies+Greats+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_modern_greats.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F46.m3u8&mode=10012&name===Sky+Movies+Showcase+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_showcase.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F45.m3u8&mode=10012&name===Sky+Movies+Select+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_select_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F510.m3u8&mode=10012&name===Sky+Movies+Drama+%26+Romance+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_drama_romance.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F509.m3u8&mode=10012&name===Sky+Movies+Family+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_family_hd.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F195.m3u8&mode=10012&name===Sky+Movies+Disney+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_movies_disney.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F182.m3u8&mode=10012&name===Film4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/film4.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Movies 24=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F633.m3u8&mode=10012&name===Movies+24+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/movies24_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'JollyHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F739.m3u8&mode=10012&name===JollyHD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tring_jolly_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Film Dy HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F777.m3u8&mode=10012&name===Film+Dy+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Dy-DigitAlb_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Film Nje HD AL=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F778.m3u8&mode=10012&name===Film+Nje+HD+AL&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Film-Nje-DigitAlb_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F564.m3u8&mode=10012&name===HBO+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_adria.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO 2 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F672.m3u8&mode=10012&name===HBO+2+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_ce.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO 3 Adria=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F738.m3u8&mode=10012&name===HBO+3+Adria&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO 1 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F675.m3u8&mode=10012&name===HBO+1+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_nl_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO 2 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F674.m3u8&mode=10012&name===HBO+2+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo2_nl.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO 3 (NL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F673.m3u8&mode=10012&name===HBO+3+%28NL%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo3_nl.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TVCINE 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F851.m3u8&mode=10012&name===TVCINE+1+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC1.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC1.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TVCINE 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F850.m3u8&mode=10012&name===TVCINE+2+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC2.png&amp;fanart=http%3A//www.zipestream.com/images/TVC2.png&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TVCINE 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F849.m3u8&mode=10012&name===TVCINE+3+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC3.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC3.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TVCINE 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F848.m3u8&mode=10012&name===TVCINE+4+HD+PT&amp;iconimage=http%3A//www.zipestream.com/images/TVC4.png+&amp;fanart=http%3A//www.zipestream.com/images/TVC4.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Hollywood (Pt)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F702.m3u8&mode=10012&name===Hollywood+%28Pt%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/canal_hollywood_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'US &amp; UK Movies from Asia=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F396.m3u8&mode=10012&name===US+%26+UK+Movies+from+Asia&amp;iconimage=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;fanart=http%3A//vignette4.wikia.nocookie.net/logopedia/images/8/8e/My_Movie_Channel_official_slogan.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ABC HD US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F295.m3u8&mode=10012&name===ABC+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ABC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F11.m3u8&mode=10012&name===ABC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/abc_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'A&E=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F16.m3u8&mode=10012&name===A%26E+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ae_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'AMC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F52.m3u8&mode=10012&name===AMC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/amc_us.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'AXS TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F392.m3u8&mode=10012&name===AXS+TV+%28US%29&amp;iconimage=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;fanart=http%3A//www.musicnewsnashville.com/wp-content/uploads/2014/04/axs-tv_logo.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Bravo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F14.m3u8&mode=10012&name===Bravo+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bravo_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F250.m3u8&mode=10012&name===CBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cbs.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CW=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F626.m3u8&mode=10012&name===CW+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/kcwq_palm_springs.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F297.m3u8&mode=10012&name===Fox+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F13.m3u8&mode=10012&name===Fox+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_bg.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F409.m3u8&mode=10012&name===FX+%28US%29&amp;iconimage=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;fanart=http%3A//www.casinopartydesigners.com/images/fx-140x140.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'NBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F15.m3u8&mode=10012&name===NBC+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nbc.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'PBSNET (PBS)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F398.m3u8&mode=10012&name===PBS+%28US%29&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;fanart=http%3A//vignette2.wikia.nocookie.net/arthur/images/5/58/PBS.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Lifetime HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F627.m3u8&mode=10012&name===Lifetime+USA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/lifetime_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Spike TV<=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F375.m3u8&mode=10012&name===Spike+%28US%29&amp;iconimage=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;fanart=http%3A//1.images.spike.com/images/missing_image2.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Syfy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F238.m3u8&mode=10012&name===Syfy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TBS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F253.m3u8&mode=10012&name===TBS+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/tbs_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TNT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F381.m3u8&mode=10012&name===TNT+%28US%29&amp;iconimage=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;fanart=http%3A//web.cablecolor.cl/images/Canales/Seriespeliculas/tnt.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F379.m3u8&mode=10012&name===USA+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/24BBCD1DC-0C7F-5F83-A9B18707E9842A5E.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'KTLA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F628.m3u8&mode=10012&name===KTLA+/CW&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/ktla_cw5_los_angeles.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Global BC (CA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F399.m3u8&mode=10012&name===Global+BC+%28CA%29&amp;iconimage=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;fanart=http%3A//priceypads.com/wp-content/uploads/2010/01/Global-BC.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Space HD Ca=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F630.m3u8&mode=10012&name===Space+HD+Ca&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/space_ca_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'WPIX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F629.m3u8&mode=10012&name===WPIX+II+CA&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/wpix_cw11_new_york.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Hallmark Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F525.m3u8&mode=10012&name===Hallmark+Channel+HD&amp;iconimage=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;fanart=http%3A//www.kadoshop-leenhouts.nl/uploads/1/3/5/1/13510121/8447772_orig.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CineMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F553.m3u8&mode=10012&name===Cinemax+East&amp;iconimage=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;fanart=http%3A//static.wixstatic.com/media/17a537_42bb4d4b404748b490b8252b9d3c8451.jpeg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Cinemax 5 StarMAX HD East (5MAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F403.m3u8&mode=10012&name===Cinemax+5+StarMax&amp;iconimage=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;fanart=http%3A//vignette2.wikia.nocookie.net/logopedia/images/2/22/5StarMax_2011.jpg++++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Cinemax ActionMax HD East (AMAXHD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F402.m3u8&mode=10012&name===Cinemax+ActionMax+East&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/company-bumpers/images/1/10/ActionMax_ID_%281998-2001%29.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MoreMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F401.m3u8&mode=10012&name===Cinemax+Moremax&amp;iconimage=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;fanart=http%3A//vignette3.wikia.nocookie.net/logopedia/images/3/38/MoreMax_2011.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F249.m3u8&mode=10012&name===HBO&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_east.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO Comedy HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F244.m3u8&mode=10012&name===HBO+Comedy+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_comedy_us.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO Signature (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F247.m3u8&mode=10012&name===HBO+Signature&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_signature.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HBO Zone (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F242.m3u8&mode=10012&name===HBO+Zone&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hbo_zone_us.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Starz (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F582.m3u8&mode=10012&name===Starz+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Starz Cinema=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F400.m3u8&mode=10012&name===Starz+Cinema+East&amp;iconimage=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;fanart=https%3A//www.starzplay.com/Images/starz/starz_facebook_logo_large.png+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Starz Edge (Pacific)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F413.m3u8&mode=10012&name===Starz+Edge+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/starz_edge.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Encore (ENCe)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F581.m3u8&mode=10012&name===Starz+Encore+East+%28US%29&amp;iconimage=http%3A//www.secv.com/images/premium_starz.jpg+&amp;fanart=http%3A//www.secv.com/images/premium_starz.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Showtime=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F554.m3u8&mode=10012&name===Showtime+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F414.m3u8&mode=10012&name===Showtime+2+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime2_east.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Showtime West=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F416.m3u8&mode=10012&name===Showtime+West&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_west.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Showtime Beyond=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F415.m3u8&mode=10012&name===Showtime+Showcase+East&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/showtime_showcase_east.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BabyTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F523.m3u8&mode=10012&name===BabyTV&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/baby_tv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F519.m3u8&mode=10012&name===Cartoon+Netwrk&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F231.m3u8&mode=10012&name===Disney+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_channel_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F230.m3u8&mode=10012&name===Disney+Jr.+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_junior_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disney XD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F770.m3u8&mode=10012&name===Disney+XD+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/disney_xd_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Nicktoons=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F520.m3u8&mode=10012&name===Nicktoons&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nicktoons_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Nickelodeon=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F521.m3u8&mode=10012&name===Nickelodeon&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nickelodeon_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Nick Jr.=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F522.m3u8&mode=10012&name===Nick+Jr.&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nick_jr_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Animal Planet (APL)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F198.m3u8&mode=10012&name===Animal+Planet+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_europe.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F200.m3u8&mode=10012&name===Discovery+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disc.History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F201.m3u8&mode=10012&name===Discovery+History+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_history.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disc.Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F199.m3u8&mode=10012&name===Discovery+Science+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_science.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F168.m3u8&mode=10012&name===Discovery+Turbo+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_turbo_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'DMAX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F638.m3u8&mode=10012&name===DMAX+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dmax_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'History=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F196.m3u8&mode=10012&name===History+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'H2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F468.m3u8&mode=10012&name===H2+UK&amp;iconimage=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;fanart=http%3A//www.mediared.tv/uploads/9/0/6/6/9066987/9872449.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CI=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F202.m3u8&mode=10012&name===Crime+%26+Investigation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/crime_investigation_network_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F197.m3u8&mode=10012&name===National+Geographic+Channel+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'National Geographic Wild=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F622.m3u8&mode=10012&name===Nat+Geo+Wild+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MTV HITS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F235.m3u8&mode=10012&name===MTV+Hits&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_hits_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F234.m3u8&mode=10012&name===MTV+Music+UK&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/MTV_Music_2013.png/220px-MTV_Music_2013.png&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'VH1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F556.m3u8&mode=10012&name===VH1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F323.m3u8&mode=10012&name===Sky+Sports+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F18.m3u8&mode=10012&name===Sky+Sports+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F322.m3u8&mode=10012&name===Sky+Sports+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F19.m3u8&mode=10012&name===Sky+Sports+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd2.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 3 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F321.m3u8&mode=10012&name===Sky+Sports+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F20.m3u8&mode=10012&name===Sky+Sports+3+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd3.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F320.m3u8&mode=10012&name===Sky+Sports+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F21.m3u8&mode=10012&name===Sky+Sports+4+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_hd4.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 5 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F339.m3u8&mode=10012&name===Sky+Sports+5+HD&amp;iconimage=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;fanart=http%3A//www.sky.com/shop/export/sites/www.sky.com/shop/__EPG/EPGImages/sports_5hd.png_1689595083.png&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F22.m3u8&mode=10012&name===Sky+Sports+5+UK&amp;iconimage=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;fanart=http%3A//store.virginmedia.com/content/dam/eSales/TV/logos-81x45/sky-sports-5-hd-pos.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports F1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F374.m3u8&mode=10012&name===Sky+Sports+F1+HD&amp;iconimage=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;fanart=http%3A//img.skysports.com/11/11/660x350/f1new_2682772.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F24.m3u8&mode=10012&name===Sky+Sports+F1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_f1_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky SpN HQ HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F23.m3u8&mode=10012&name===Sky+Sports+News+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_uk_sports_news_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport 1 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F316.m3u8&mode=10012&name===BT+Sport+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F309.m3u8&mode=10012&name===BT+Sport+1+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F308.m3u8&mode=10012&name===BT+Sport+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sports 2 HD (1080) Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F599.m3u8&mode=10012&name===BT+Sports+2+HD+%281080%29+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sports 2 HD Test=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F707.m3u8&mode=10012&name===BT+Sports+2+HD+Test&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F26.m3u8&mode=10012&name===BT+Sport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_2_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport EurHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F382.m3u8&mode=10012&name===BT+Sport+Europe+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F705.m3u8&mode=10012&name===BT+Sport+Europe&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bt_sport_1_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BT Sport\/\/ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F28.m3u8&mode=10012&name===BT+Sport+ESPN&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/espn_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Premier HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F310.m3u8&mode=10012&name===Premier+Sports+HD&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Premier Sports HD 1080P=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F384.m3u8&mode=10012&name===Premier+Sports+HD+1080P&amp;iconimage=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;fanart=http%3A//w3.satkurier.pl/pliki/24801.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Premier Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F175.m3u8&mode=10012&name===Premier+Sports+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/premier_sports.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Setanta Ireland=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F176.m3u8&mode=10012&name===Setanta+Sports+Ireland+1+UK&amp;iconimage=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;fanart=http%3A//www.setanta.com/Themes/setanta/img/channel_logos/Setanta.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F170.m3u8&mode=10012&name===At+the+Races+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/at_the_races_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F171.m3u8&mode=10012&name===Racing+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/racing_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MUTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F172.m3u8&mode=10012&name===Manchester+United+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mutv.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'LFCTV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F174.m3u8&mode=10012&name===Liverpool+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/liverpool_football_club.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Chelsea TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F177.m3u8&mode=10012&name===Chelsea+TV+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/chelsea_tv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F269.m3u8&mode=10012&name===Eurosport+1+UK&amp;iconimage=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;fanart=http%3A//euro-2012.ru/download/Logo-eurosport.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Eurosport 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F748.m3u8&mode=10012&name===Eurosport+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/eurosport2.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'1HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F83.m3u8&mode=10012&name===BEIN+SPORTS+1&amp;iconimage=http%3A//digigroup.az/media/images/1.jpg+&amp;fanart=http%3A//digigroup.az/media/images/1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'2HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F84.m3u8&mode=10012&name===BEIN+SPORTS+2&amp;iconimage=http%3A//digigroup.az/media/images/2.jpg++&amp;fanart=http%3A//digigroup.az/media/images/2.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'3HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F85.m3u8&mode=10012&name===BEIN+SPORTS+3&amp;iconimage=http%3A//digigroup.az/media/images/3.jpg++&amp;fanart=http%3A//digigroup.az/media/images/3.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'4HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F86.m3u8&mode=10012&name===BEIN+SPORTS+4&amp;iconimage=http%3A//digigroup.az/media/images/4.jpg++&amp;fanart=http%3A//digigroup.az/media/images/4.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'5HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F87.m3u8&mode=10012&name===BEIN+SPORTS+5&amp;iconimage=http%3A//digigroup.az/media/images/5.jpg++&amp;fanart=http%3A//digigroup.az/media/images/5.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'6HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F88.m3u8&mode=10012&name===BEIN+SPORTS+6&amp;iconimage=http%3A//digigroup.az/media/images/6.jpg++&amp;fanart=http%3A//digigroup.az/media/images/6.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'7HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F89.m3u8&mode=10012&name===BEIN+SPORTS+7&amp;iconimage=http%3A//digigroup.az/media/images/7.jpg++&amp;fanart=http%3A//digigroup.az/media/images/7.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'8HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F90.m3u8&mode=10012&name===BEIN+SPORTS+8&amp;iconimage=http%3A//digigroup.az/media/images/8.jpg++&amp;fanart=http%3A//digigroup.az/media/images/8.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'9HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F91.m3u8&mode=10012&name===BEIN+SPORTS+9&amp;iconimage=http%3A//digigroup.az/media/images/9.jpg++&amp;fanart=http%3A//digigroup.az/media/images/9.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'10HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F92.m3u8&mode=10012&name===BEIN+SPORTS+10&amp;iconimage=http%3A//digigroup.az/media/images/10.jpg++&amp;fanart=http%3A//digigroup.az/media/images/10.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'12HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F424.m3u8&mode=10012&name===BEIN+SPORTS+12&amp;iconimage=http%3A//digigroup.az/media/images/12.jpg++&amp;fanart=http%3A//digigroup.az/media/images/12.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Astro SuperSport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F60.m3u8&mode=10012&name===Astro+Supersport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport1.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Astro SuperSport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F59.m3u8&mode=10012&name===Astro+Supersport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport2.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Astro SuperSport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F58.m3u8&mode=10012&name===Astro+Supersport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport3.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Astro SuperSport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F57.m3u8&mode=10012&name===Astro+Supersport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/astro_supersport4.jpg++++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 1 (CTH 211 SD / 56HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F67.m3u8&mode=10012&name===CTH+Stadium+1+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium1_th.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 2 (CTH 212 SD / 57 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F66.m3u8&mode=10012&name===CTH+Stadium+2+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium2_th.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 3 (CTH 213 SD / 58 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F65.m3u8&mode=10012&name===CTH+Stadium+3+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium3_th.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 4 (CTH 214 SD / 59 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F64.m3u8&mode=10012&name===CTH+Stadium+4+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium4_th.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 5 (CTH 216 SD / 60 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F63.m3u8&mode=10012&name===CTH+Stadium+5+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium5_th.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM 6 (CTH 216 SD / 61 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F62.m3u8&mode=10012&name===CTH+STADIUM+6+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/stadium6_th.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'STADIUM X (CTH 217 SD / 62 HD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F61.m3u8&mode=10012&name===CTH+STADIUM+X+HD&amp;iconimage=http%3A//stepfb.net/live/movieposters/136.png++&amp;fanart=http%3A//stepfb.net/live/movieposters/136.png++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TV Arena Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F163.m3u8&mode=10012&name===Arena+Sport+1&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport1_rs.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TV Arena Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F167.m3u8&mode=10012&name===Arena+Sport+2&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport2_rs.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TV Arena Sport 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F164.m3u8&mode=10012&name===Arena+Sport+3&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport3_rs.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TV Arena Sport 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F165.m3u8&mode=10012&name===Arena+Sport+4&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/arenasport4_rs.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TSN1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F96.m3u8&mode=10012&name===TSN+1&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn1.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TSN2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F97.m3u8&mode=10012&name===TSN+2&amp;iconimage=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;fanart=http%3A//tgo-tv.com/images/tv/tsn2.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TSN3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F98.m3u8&mode=10012&name===TSN+3&amp;iconimage=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;fanart=http%3A//cdn1.sportngin.com/attachments/news_article/5782/7585/tsn_thumb.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TSN4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F99.m3u8&mode=10012&name===TSN+4&amp;iconimage=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;fanart=http%3A//contact.sourcecable.ca/wp-content/uploads/2015/05/TSN4_CMYK.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX Sports 1 Eredivisie HD"=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F531.m3u8&mode=10012&name===Fox+Sports+1+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports1_au.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX Sports 2 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F530.m3u8&mode=10012&name===Fox+Sports+2+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_nl_02.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX Sports 3 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F529.m3u8&mode=10012&name===Fox+Sports+3+%28Nl%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports3_au.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX Sports 4 HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F528.m3u8&mode=10012&name===Fox+Sports+4+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-4-Int-NL_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX Sports 5 Eredivisie HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F527.m3u8&mode=10012&name===Fox+Sports+5+%28Nl%29&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Fox-Sports-5-Eredivisie_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Arena Sport 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F166.m3u8&mode=10012&name===Arena+Sport+5&amp;iconimage=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;fanart=http%3A//fanclub365.vn/s/41663-arena_sport_5-.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBS Sports Network (CBS SN)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F378.m3u8&mode=10012&name===CBS+Sports+%28US%29&amp;iconimage=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;fanart=http%3A//images.bwwstatic.com/columnpic6/2FBEB2A30-DAF8-BAC8-F5562F03F5F07369.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'NBA TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F304.m3u8&mode=10012&name===NBA+TV+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nba_tv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'NFL NETWORK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F95.m3u8&mode=10012&name===NFL+Network+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nfl_network.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Viasat Sports RU=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F278.m3u8&mode=10012&name===Viasat+Sports+RU&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/viasat_sport_no.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'E! Entertainment Television=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F835.m3u8&mode=10012&name===E%21+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F830.m3u8&mode=10012&name===London+Live&amp;iconimage=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;fanart=http%3A//www.londoncommunications.co.uk/wp-content/uploads/2014/03/London-Live.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'AXNHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F842.m3u8&mode=10012&name===AXN+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_de_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'AXNBLACKHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F841.m3u8&mode=10012&name===AXN+BLACK+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_black_pt.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOX=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F845.m3u8&mode=10012&name===Fox+hd+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_hd_lam.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOXLIFE=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F843.m3u8&mode=10012&name===FoxLife+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_life_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOXCRIME=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F844.m3u8&mode=10012&name===Fox+Crime+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_crime_asia_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MOVHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F839.m3u8&mode=10012&name===Mov+HD+PT&amp;iconimage=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;fanart=http%3A//canalmov.pt/wp-content/themes/site/images/cabecera_logo/logoprincipal.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'SYFYHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F838.m3u8&mode=10012&name===SyFy+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/syfy_universal_fr.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'True Movies 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F853.m3u8&mode=10012&name===True+Movies+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies1_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'True Movies 2 UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F852.m3u8&mode=10012&name===True+Movies+2+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/true_movies2.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FOXMOVIESHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F846.m3u8&mode=10012&name===Fox+Movies+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_movies_pt.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F837.m3u8&mode=10012&name===Comedy+Central+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/comedy_central_at_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Discovery Family Channel (DFCH)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F836.m3u8&mode=10012&name===Discovery+Family++HD+US&amp;iconimage=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;fanart=https%3A//pmcdeadline2.files.wordpress.com/2015/03/discovery-family.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'E! (E!)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F834.m3u8&mode=10012&name===E%21+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/e_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ABC Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F833.m3u8&mode=10012&name===Family+Channel+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/my_family_tv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'VH1 (VH1)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F828.m3u8&mode=10012&name===VH1+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/vh1_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Slice=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F829.m3u8&mode=10012&name===SLICE+TV+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/slice.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Lifetime Movie Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F524.m3u8&mode=10012&name===LMN+US&amp;iconimage=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;fanart=http%3A//cdn.realscreen.com/wp/wp-content/uploads/2013/09/LMN.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Cartoon Netwrk=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F519.m3u8&mode=10012&name===Cartoon+Network+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Cartoon Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F809.m3u8&mode=10012&name===Cartoon+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/cartoon_network_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBBC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F808.m3u8&mode=10012&name===CBBC+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbbc.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CBeebies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F807.m3u8&mode=10012&name===Cbeebies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/bbc_cbeebies_asia.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F818.m3u8&mode=10012&name===Animal+Planet+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/animal_planet_us_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'The Discovery Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F817.m3u8&mode=10012&name===Discovery+Channel+HD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_ca.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Do-It-Yourself Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F815.m3u8&mode=10012&name===DIY+Network+US&amp;iconimage=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;fanart=http%3A//www.homesoldpledge.com/wp-content/uploads/2014/04/logo-diy-network.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'H2 (H2)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F814.m3u8&mode=10012&name===H2+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_2_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'History Channel (HIST)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F813.m3u8&mode=10012&name===HISTORY+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/history_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Investigation Discovery (ID)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F812.m3u8&mode=10012&name===Investigation+Discovery++US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/investigation_discovery_us_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'National Geographic Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F810.m3u8&mode=10012&name===National+Geographic+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_eur_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'NatGeo WILD (NGWILD)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F811.m3u8&mode=10012&name===NAT+GEO+WILD+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/nat_geo_wild_us_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MTV CLASSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F420.m3u8&mode=10012&name===MTV+Classic&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mtv_classic_uk.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Clubland TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F806.m3u8&mode=10012&name===Clubland+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/clubland_tv.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'The Box=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F805.m3u8&mode=10012&name===The+Box&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/the_box_uk.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'BoxNation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F173.m3u8&mode=10012&name===Box+Nation+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/box_nation.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Big Ten HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F823.m3u8&mode=10012&name===Big+Ten+Network+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/big_ten_network_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'MLB Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F822.m3u8&mode=10012&name===MLB+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/mlb_network.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Willow Cricket=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F824.m3u8&mode=10012&name===Willow+Sports+HD+US&amp;iconimage=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;fanart=https%3A//1.bp.blogspot.com/-Ar8J69gqR44/Vuak-8J1uWI/AAAAAAAAA1o/nQgEJbrZRbQnz_iXtg4TkNU5TAg5MPDLA/s320/willow-cricket.jpg+&amp;description=' + '\n' )
 if 25 - 25: I11i + I1ii11iIi11i . I1ii11iIi11i % ii - OoOOOOOo0o
 if 43 - 43: oO0o % oO0o
 O0ooO00ooOO0o . write ( r'AXN White HD PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F840.m3u8&mode=10012&name===AXN+White+HD+PT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/axn_white_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CINEMUNDO PT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F847.m3u8&mode=10012&name===CINEMUNDO+PT&amp;iconimage=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;fanart=https%3A//i.vimeocdn.com/portrait/9079238_300x300.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'FreeForm US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F832.m3u8&mode=10012&name===FreeForm+US&amp;iconimage=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;fanart=http%3A//t2.snewsi.com/188/8/18885012.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HIFI US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F831.m3u8&mode=10012&name===HIFI+US&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/hifi_music_art.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Discovery Home &amp; Health UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F816.m3u8&mode=10012&name===Discovery+Home+%26+Health+UK&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/discovery_home_health_uk_plus1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'CITY TV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F803.m3u8&mode=10012&name===CITY+TV&amp;iconimage=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;fanart=http%3A//thewatchtv.com/wp-content/uploads/2013/05/Watch-CITY-TV-Live-TV-from-Bulgaria.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'DANCE HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F802.m3u8&mode=10012&name===DANCE+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dance_tv_hu.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Dream music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F799.m3u8&mode=10012&name===Dream+music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/dream_tv_tr.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Europe Plus Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F796.m3u8&mode=10012&name===Europe+Plus+Music&amp;iconimage=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;fanart=http%3A//1tv.ucoz.ru/logo_channel/ee.jpeg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'HITV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F804.m3u8&mode=10012&name===HITV+Music&amp;iconimage=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;fanart=http%3A//static-cdn1.ustream.tv/i/channel/picture/8/6/3/7/8637664/8637664_hit_music_channel_1309019162%2C66x66%2Cr%3A1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Music Channel=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F800.m3u8&mode=10012&name===Music+Channel&amp;iconimage=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;fanart=https%3A//upload.wikimedia.org/wikipedia/en/f/f8/Music_Choice_%2528logo%2529.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Heavy Metal=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F801.m3u8&mode=10012&name===Heavy+Metal&amp;iconimage=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;fanart=https%3A//channelpear.com/images/heavymetaltelevision.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Si TV Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F797.m3u8&mode=10012&name===Si+TV+Music&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/si_tv_hn.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'VEVO Music=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F798.m3u8&mode=10012&name===VEVO+Music&amp;iconimage=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;fanart=http%3A//i.imgur.com/6Bv76t9.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'beIN Sport 1 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F9.m3u8&mode=10012&name===beIN+Sport+1+%28Fr%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport1_hd.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'beIN Sport 2 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F81.m3u8&mode=10012&name===beIN+Sport+2+%28Fr%29&amp;iconimage=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;fanart=http%3A//3.bp.blogspot.com/-X28wcyKEmyA/Vl-TLcw3MEI/AAAAAAAAAIo/AZGqtQkviSM/s1600/index.png+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'beIN Sport 3 (Fr)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F82.m3u8&mode=10012&name===beIN+Sport+3+%28Fr%29&amp;iconimage=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;fanart=http%3A//nowwatchtvlive.me/wp-content/uploads/2014/01/beinsport_3hd.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Bein Sport US HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F766.m3u8&mode=10012&name===Bein+Sport+US+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/be_in_sport_us.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'RDS=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F505.m3u8&mode=10012&name===RDS&amp;iconimage=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;fanart=http%3A//www.bellmedia.ca/wp-content/uploads/2014/02/tv_rds-500x500.png++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Fox Sports 1 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F262.m3u8&mode=10012&name===Fox+Sports+1+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Fox Sports 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F261.m3u8&mode=10012&name===Fox+Sports+2+%28US%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_basico.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Fox Sports 1 (Asia)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F391.m3u8&mode=10012&name===Fox+Sports+1+%28Asia%29&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/fox_sports_lam_hd.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'KP+ PM HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F475.m3u8&mode=10012&name===KP%2B+PM+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_pc.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'K+ 1 HD Sports/Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F390.m3u8&mode=10012&name===K%2B+1+HD+Sports/Movies&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/k_plus_1.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Skynet Sports HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F473.m3u8&mode=10012&name===Skynet+Sports+HD&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-HD_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Skynet Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F474.m3u8&mode=10012&name===Skynet+Sports+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sky-Net-Sports-2_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'True SportsHD 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F274.m3u8&mode=10012&name===True+SportsHD+3&amp;iconimage=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;fanart=http%3A//stepfb.net/live/movieposters/22.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'True Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F276.m3u8&mode=10012&name===True+Sport+2&amp;iconimage=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;fanart=http%3A//tv-online.im/wp-content/uploads/2013/10/True-Sport-2-LIVE.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'NBC Sports Network (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F209.m3u8&mode=10012&name===NBC+Sports+Network+%28US%29&amp;iconimage=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;fanart=http%3A//www.nyinterconnect.com/wp-content/uploads/nbc_sports.jpg+++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'EPL Extra Time 1 (USA TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F255.m3u8&mode=10012&name===EPL+Extra+Time+1+%28USA+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'EPL Extra Time 3 (Spike USA)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F257.m3u8&mode=10012&name===EPL+Extra+Time+3+%28Spike+USA%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'EPL Extra Time 4 (AXS TV)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F258.m3u8&mode=10012&name===EPL+Extra+Time+4+%28AXS+TV%29&amp;iconimage=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;fanart=https%3A//secure.toolkitfiles.co.uk/clients/7007/siteimages/medium/Premier_League_logo.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sportsnet World=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F367.m3u8&mode=10012&name===Sportsnet+World+HD+US&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sportsnet%2520world%2520live%2520stream.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sportsnet NY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F385.m3u8&mode=10012&name===Sportsnet+Ontario+HD&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/Sportsnet_ontario%2520live%2520stream.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sportsnet One HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F259.m3u8&mode=10012&name===Sportsnet+One+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sportsnet_one.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F314.m3u8&mode=10012&name===ESPN+%28US%29&amp;iconimage=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;fanart=http%3A//www.allaccess.com/assets/img/editorial/raw/es/espn.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ESPN 2 (US)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F315.m3u8&mode=10012&name===ESPN+2+%28US%29&amp;iconimage=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;fanart=http%3A//www.lime.com/widgets/limetv/bb-coverflow/images/channel-logos/espn2-logo.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sport Klub 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F594.m3u8&mode=10012&name===Sport+Klub+1&amp;iconimage=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;fanart=http%3A//www.stream2watch.co/images/thumbs/sport_klub_si_1.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sport Klub 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F593.m3u8&mode=10012&name===Sport+Klub+2&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-2-Slovenia_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sport Klub 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F592.m3u8&mode=10012&name===Sport+Klub+3&amp;iconimage=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;fanart=http%3A//www.sat-address.com/f/pics/logotipi/Sport-Klub-3-Slovenia_o.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Golf HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F260.m3u8&mode=10012&name===Golf+HD&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Golf Channel 1080p=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F332.m3u8&mode=10012&name===Golf+Channel+1080p&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/golf_channel_us_hd.jpg&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F178.m3u8&mode=10012&name===WWENetwork&amp;iconimage=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;fanart=http%3A//3.bp.blogspot.com/-d6ZVw8_zw14/VWh38v-qd2I/AAAAAAAAFKQ/9_kwqxiqYUc/s320/20140102_EPLIGHT_Network_Announcement_nodate_C.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Motor Sports 1 Aus=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F281.m3u8&mode=10012&name===Motor+Sports+1+Aus&amp;iconimage=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;fanart=http%3A//4.bp.blogspot.com/_Fb0x6TGTbPs/SMhHr89KwEI/AAAAAAAABkU/CCkn-Bo_iEY/s400/motosport%2Btv.JPG++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Fight Sports (USEE)=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F433.m3u8&mode=10012&name===Fight+Sports+%28USEE%29&amp;iconimage=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;fanart=http%3A//www.frocus.net/images/logotv/original/fight-channel.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sport 2 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F471.m3u8&mode=10012&name===Sky+Sport+2+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport2_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'Sky Sport 1 IT=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F472.m3u8&mode=10012&name===Sky+Sport+1+IT&amp;iconimage=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;fanart=http%3A//www.tv-logo.com/pt-data/uploads/images/logo/sky_it_sport1_hd.jpg+&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'TyC Sports=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F31.m3u8&mode=10012&name===TyC+Sports&amp;iconimage=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;fanart=http%3A//1.bp.blogspot.com/_yDxTw4hZsW8/TEnPHPkFjqI/AAAAAAAAQsk/IJH-Y4kFA8g/s400/TYC_logo.jpg++&amp;description=' + '\n' )
 O0ooO00ooOO0o . write ( r'ORF Sport +=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + i1iiIII111ii + '%2F' + i1iIIi1 + '%2F423.m3u8&mode=10012&name===ORF+Sport+%2B&amp;iconimage=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;fanart=http%3A//tubestatic.orf.at/static/images/site/tube/20141042/17.10.14-sporthd.5298157.jpg+&amp;description=' + '\n' )
 if 46 - 46: I1ii11iIi11i % iI11I1II1I1I . iI1i1IiI . o0o00Oo0O * oO0OOoo0OO / ii
 if 7 - 7: o000o - o0o00Oo0O * Ooo0Oo0oOoo - I11i - IIiIiII11i
def Ii11iiI1 ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  i1Ii ( IiII111iI1ii1 , ( iI11I1II ) . strip ( ) , 222 , IIi1i + '247.png' , IIi1i + '247.png' , '' )
def oO0OOOoooO00o0o ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  i1Ii ( IiII111iI1ii1 , ( iI11I1II ) . strip ( ) , 222 , IIi1i + 'musicch.png' , IIi1i + 'musicch.png' , '' )
def I1ii1Ii1 ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  i1Ii ( IiII111iI1ii1 , ( iI11I1II ) . strip ( ) , 222 , IIi1i + 'NEWS.png' , IIi1i + 'NEWS.png' , '' )
def OoOoO ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  i1Ii ( IiII111iI1ii1 , ( iI11I1II ) . strip ( ) , 222 , IIi1i + 'adult.png' , IIi1i + 'adult.png' , '' )
def iI111I1III ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 iI11Ii = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i1Ii ( IiII111iI1ii1 , iI11I1II , 1016 , IIi1i + 'TUTS.png' , IIi1i + 'TUTS.png' , '' )
  if 36 - 36: Ooo0Oo0oOoo % O0OoO0O00o0oO
  if 72 - 72: oOo0O0Ooo / iI1i1IiI - o0o00Oo0O + Ooo0Oo0oOoo
def o0iIIIIi ( ) :
 if 50 - 50: ooOoOO0oOO + oO0OOoo0OO + iI1i1IiI
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Recent Episodes[/COLOR]' , '' , 10019 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Genres[/COLOR]' , '' , 10020 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Search[/COLOR]' , '' , 10021 , IIi1i + 'dtv.png' , iIii1 , '' )
 if 15 - 15: Ooo0Oo0oOoo
def IiiI11I1IIiI ( ) :
 if 5 - 5: I1ii11iIi11i
 o00o = cloudflare . source ( Oo0o0000o0o0 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI11Ii = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , iI1I , IiII111iI1ii1 , i1ii1II1ii in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 + '  -  ' + ( i1ii1II1ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI11I1II , 10023 , IIi1i + 'dtv.png' , iIii1 , '' )
  if 100 - 100: OoOOOOOo0o + iI11I1II1I1I
  if 59 - 59: OO
  if 89 - 89: OOooOOo % iI11I1II1I1I
def III11I1OOOO0o0O ( ) :
 if 41 - 41: I11i + oO0OOoo0OO
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Action[/COLOR]' , 'Aksiyon' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Adventure[/COLOR]' , 'Macera' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Animation[/COLOR]' , 'Animasyon' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Anime[/COLOR]' , 'Anime' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Biography[/COLOR]' , 'Biyografi' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Comedy[/COLOR]' , 'Komedi' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Drama[/COLOR]' , 'Dram' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Family[/COLOR]' , 'Aile' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']History[/COLOR]' , 'Tarih' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Horror[/COLOR]' , 'Korku' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Mystery[/COLOR]' , 'Gizem' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Romance[/COLOR]' , 'Romantik' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Sport[/COLOR]' , 'Spor' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Western[/COLOR]' , 'Tarih' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , IIi1i + 'dtv.png' , iIii1 , '' )
 if 90 - 90: OO - Ii1I % Ooo0Oo0oOoo % iI11I1II1I1I - Ii1I
def IiIiI1i1 ( url ) :
 Oo00o0OO0O00o = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 OO0O0OoOO0 = cloudflare . source ( Oo00o0OO0O00o )
 iI11Ii = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 10022 , IIi1i + 'dtv.png' , iIii1 , '' )
  if 18 - 18: OoOOOOOo0o
  if 25 - 25: oO0o * o000o % Ii + Ii * oO0o
  if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
  if 62 - 62: o0o00Oo0O . I1ii11iIi11i
def iI1ii ( ) :
 if 76 - 76: OoOOOOOo0o + iI11I1II1I1I + OOooOOo . oO0o
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 iI11I1II = ( Oo0o0000o0o0 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i11IIIiI11 ) . replace ( ' ' , '+' )
 OO0O0OoOO0 = cloudflare . source ( iI11I1II )
 iI11Ii = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 10022 , IIi1i + 'dtv.png' )
   if 49 - 49: OO / oO0OOoo0OO / O0OoO0O00o0oO
   if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - oO0OOoo0OO
   if 38 - 38: I11i % ooOoOO0oOO + Ii + iI1i1IiI + oO0OOoo0OO / Ii
def o0OOOOOo0 ( url ) :
 OO0O0OoOO0 = cloudflare . source ( url )
 iI11Ii = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for oo00o0 , oooOoO , O0Oo0iIIIi1IiI11I1 , IiII111iI1ii1 in iI11Ii :
  O0Ooo000 = ( O0Oo0iIIIi1IiI11I1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIi11iI1Iii = ( oooOoO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IiIi1i = 'Season ' + IIi11iI1Iii + 'Episode ' + O0Ooo000 + IiII111iI1ii1
  i11ii ( IiIi1i , oo00o0 )
  if 83 - 83: Ii1I * Ii1I + O0OoO0O00o0oO
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / OoOOOOOo0o
  if 20 - 20: O0OoO0O00o0oO * IIiIiII11i - OOooOOo - o000o * ooOoOO0oOO
def i11ii ( name , url ) :
 oo00o0 = url
 I1i1II1 = name
 iiiI1I11i1 = cloudflare . source ( oo00o0 )
 i1iIIIi1i = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iiiI1I11i1 )
 for OOo , oOOoo in i1iIIIi1i :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + I1i1II1 + oOOoo + '[/COLOR]' , OOo , 10012 , IIi1i + 'dtv.png' )
  if 9 - 9: Ooo0Oo0oOoo . oO0o * ooOoO0O00 . ii
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
 if 11 - 11: o0o00Oo0O + oOo0O0Ooo
def OO0OOoooo0o ( ) :
 if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / OoOOOOOo0o . ooOoO0O00
 if 60 - 60: I1ii11iIi11i . OO % oOo0O0Ooo - ooOoOO0oOO
 if 79 - 79: ii / Ii1I . o0o00Oo0O
 if 79 - 79: o000o - IIiIiII11i
 if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / OoOOOOOo0o * oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
 if 84 - 84: ii + ooOoOO0oOO / oOo0O0Ooo % O0OoO0O00o0oO % Ii1I * oOo0O0Ooo
 if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / o000o
 if 24 - 24: oOo0O0Ooo * ooOoO0O00 % oO0OOoo0OO / o0o00Oo0O + Ii
 if 12 - 12: Ii1I / OoOOOOOo0o
 if 5 - 5: ii
 if 18 - 18: oOo0O0Ooo % ii - iI1i1IiI . Ii * I1ii11iIi11i % OoOOOOOo0o
 if 12 - 12: ooOoO0O00 / O0OoO0O00o0oO % oO0OOoo0OO * OO * o0o00Oo0O * iI11I1II1I1I
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Search Program[/COLOR]' , '' , 10043 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * o000o . ii
 if 54 - 54: o0o00Oo0O / OO % oO0OOoo0OO * ooOoO0O00 * o0o00Oo0O
def IIOOOoO00O ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iII111Ii = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 iI11Ii = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iII111Ii ) )
 for url , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , IIi1i + 'WATCHSERIES.png' , '' , '' )
  if 27 - 27: Ii1I * ooOoO0O00 . ooOoO0O00
def o0O0O ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , IIi1i + 'WATCHSERIES.png' , '' , '' )
  if 56 - 56: o0o00Oo0O
def iIIIII1iI ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  if 'episode' in url :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IIi1i + 'WATCHSERIES.png' , '' , '' )
  else :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 for url in i1iIIIi1i :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , IIi1i + 'Next.png' , '' , '' )
  if 18 - 18: I1ii11iIi11i - o0o00Oo0O
  if 85 - 85: OoOOOOOo0o - o0o00Oo0O * Ii . ooOoO0O00
def i11i1 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00oo00OOOO = 'http://www.watchseries.ac/search/' + i11IIIiI11 . replace ( ' ' , '%20' )
 OO0O0OoOO0 = O00OOOoOoo0O ( O00oo00OOOO )
 iI11Ii = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'watch online' in IiII111iI1ii1 :
   pass
  else :
   print iI11I1II
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.watchseries.ac' + iI11I1II , 10044 , iI1I , '' , '' )
   if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
   xbmcplugin . setContent ( IIIII , 'movies' )
   if 79 - 79: OOooOOo % oOo0O0Ooo % OoOOOOOo0o / ooOoO0O00 % oO0o
def oo0o00OO ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , url , IiII111iI1ii1 , O0Oo0iIIIi1IiI11I1 , ooo0O in iI11Ii :
  oOoo00o0oOO = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( O0Oo0iIIIi1IiI11I1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + oOoo00o0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , iI1I , '' , ooo0O )
  if 61 - 61: ooOoO0O00 * I11i + iI11I1II1I1I / OOooOOo - o0o00Oo0O * iI11I1II1I1I
def oOoo0ooOoo ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  oOoo00o0oOO = ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + oOoo00o0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 for url in i1iIIIi1i :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , IIi1i + 'Next.png' , '' , '' )
  if 52 - 52: oO0o * ii
def Ii11iiI ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , iI1I , '' , '' )
 for url in i1iIIIi1i :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , IIi1i + 'Next.png' , '' , '' )
  if 71 - 71: ooOoOO0oOO - I11i - O0OoO0O00o0oO
def iiI ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 iII111Ii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for oooOoO , Ii1iiII1i in iII111Ii :
  iI11Ii = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( Ii1iiII1i ) )
  for url , IiII111iI1ii1 in iI11Ii :
   oOoo00o0oOO = ( oooOoO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + oOoo00o0oOO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 i1iIIIi1i = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , url in iI11Ii :
  ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , IIi1i + 'WATCHSERIES.png' , '' , '' )
 for url in i1iIIIi1i :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , IIi1i + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 81 - 81: OO * Ii1I + IIiIiII11i % OO
class IiI1ii11I1 ( ) :
 if 19 - 19: ooOoOO0oOO + OO / o000o / IIiIiII11i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 92 - 92: ooOoO0O00 % oO0OOoo0OO + oO0OOoo0OO - iI11I1II1I1I . OoOOOOOo0o
  oOoo00o0oOO = name
  self . Get_Sources ( iI11I1II , oOoo00o0oOO )
  if 33 - 33: I11i / o0o00Oo0O + O0OoO0O00o0oO
  if 75 - 75: OO % Ii + iI11I1II1I1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  OO0O0OoOO0 = O00OOOoOoo0O ( URL )
  iI11Ii = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for iI11I1II , IiII111iI1ii1 in iI11Ii :
   URL = 'http://www.watchseries.ac/link/' + iI11I1II
   self . Get_site_link ( URL , season_name )
   if 92 - 92: OOooOOo % o0o00Oo0O
 def Get_site_link ( self , url , season_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( OO0O0OoOO0 )
  i1iIIIi1i = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( OO0O0OoOO0 )
  i11iI11I1I = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( OO0O0OoOO0 )
  for url in iI11Ii :
   self . main ( url , season_name )
  for url in i1iIIIi1i :
   self . main ( url , season_name )
  for url in i11iI11I1I :
   self . main ( url , season_name )
   if 55 - 55: iI11I1II1I1I * iI1i1IiI
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ooIi11iI = 'DACLIPS'
   if ooIi11iI in IiI1ii11I1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , ooIi11iI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    ooIi11iI = 'FILEHOOT'
    if ooIi11iI in IiI1ii11I1 . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , ooIi11iI )
   else :
    if 'thevideo.me' in url :
     ooIi11iI = 'THEVIDEO'
     if ooIi11iI in IiI1ii11I1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , ooIi11iI )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      ooIi11iI = 'ALLMYVIDEOS'
      if ooIi11iI in IiI1ii11I1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , ooIi11iI )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       ooIi11iI = 'VIDSPOT'
       if ooIi11iI in IiI1ii11I1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , ooIi11iI )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        ooIi11iI = 'VODLOCKER'
        if ooIi11iI in IiI1ii11I1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , ooIi11iI )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 22 - 22: O0OoO0O00o0oO
         if 22 - 22: iI1i1IiI * Ooo0Oo0oOoo - I1ii11iIi11i * o0o00Oo0O / Ii
 def allmyvid ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 , IiII111iI1ii1 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 17 - 17: iI11I1II1I1I + oOo0O0Ooo
 def vidspot ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 , IiII111iI1ii1 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 57 - 57: I11i / ooOoOO0oOO
 def thevideo ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 13 - 13: ii + oO0o
 def vodlocker ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 32 - 32: o0o00Oo0O + o000o % I1ii11iIi11i
 def daclips ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 7 - 7: Ii1I / oO0OOoo0OO
 def filehoot ( self , url , season_name , source_name ) :
  OO0O0OoOO0 = O00OOOoOoo0O ( url )
  iI11Ii = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for OOooO0Oo0o000 in iI11Ii :
   self . Printer ( OOooO0Oo0o000 , season_name , source_name )
   if 11 - 11: OO * oO0OOoo0OO / oO0OOoo0OO - O0OoO0O00o0oO
 def Printer ( self , Link , season_name , source_name ) :
  if 68 - 68: oOo0O0Ooo % OO - OO / oOo0O0Ooo + Ii1I - I1ii11iIi11i
  if Link in IiI1ii11I1 . List :
   pass
  elif source_name in IiI1ii11I1 . source_list :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + source_name + '[/COLOR]' , Link , 10012 , IIi1i + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IiI1ii11I1 . List . append ( Link )
   IiI1ii11I1 . source_list . append ( source_name )
   if 65 - 65: oO0OOoo0OO - ooOoO0O00
   xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 62 - 62: Ooo0Oo0oOoo / o000o % I1ii11iIi11i . ii / Ii / ooOoOO0oOO
   if 60 - 60: oOo0O0Ooo % o000o / I11i % o000o * Ii / iI1i1IiI
   if 34 - 34: ooOoOO0oOO - O0OoO0O00o0oO
   if 25 - 25: o000o % oOo0O0Ooo + Ii + o0o00Oo0O * ii
   if 64 - 64: ooOoO0O00
def I1ii1i1iiii ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Highlights[/COLOR]' , '' , 10008 , IIi1i + 'Highlights.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Fixtures[/COLOR]' , '' , 10009 , IIi1i + 'Fixtures.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Today On G-Tv[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , IIi1i + 'TodaysMacthes.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , IIi1i + 'PremiereLeague.png' , iIii1 , '' )
 if 45 - 45: OoOOOOOo0o / oO0OOoo0OO . ii + oO0o
def O00oO000Oo0 ( url ) :
 ii111iI1iIi1 ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( o00o )
 for iIIiiIi , url , i1I111II , Oo0OOo , i1II11I11ii1 , ooO00O0O0 , OOoO0oO00o , o0OIiII , Ii1iI111 , OOO0OoO0oo0OO , i1iI1Ii11Ii1 in iI11Ii :
  i1I111II = i1I111II
  if 'Arsenal' in i1I111II :
   I1iiIIIi11 = IIi1i + 'arsenal-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                                  ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Bournemouth' in i1I111II :
   I1iiIIIi11 = IIi1i + 'afc-bournemouth.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                       ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Burnley' in i1I111II :
   I1iiIIIi11 = IIi1i + 'KEGnQWW.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                                   ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Chelsea' in i1I111II :
   I1iiIIIi11 = IIi1i + 'chelsea.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                                  ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Crystal' in i1I111II :
   I1iiIIIi11 = IIi1i + 'CrystalPalace.0.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                       ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Everton' in i1I111II :
   I1iiIIIi11 = IIi1i + 'Everton.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                                   ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Hull' in i1I111II :
   I1iiIIIi11 = IIi1i + 'hull-city-afc.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                                 ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Leicester' in i1I111II :
   I1iiIIIi11 = IIi1i + 'leicester-city-fc-hd-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                       ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Liverpool' in i1I111II :
   I1iiIIIi11 = IIi1i + 'liverpool-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                               ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Manchester City' in i1I111II :
   I1iiIIIi11 = IIi1i + 'city-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '               ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Manchester United' in i1I111II :
   I1iiIIIi11 = IIi1i + '91.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '          ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Middlesbrough' in i1I111II :
   I1iiIIIi11 = IIi1i + 'middlesbrough-fc-hd-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                 ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Southampton' in i1I111II :
   I1iiIIIi11 = IIi1i + 'southampton-fc-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                   ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Stoke City' in i1I111II :
   I1iiIIIi11 = IIi1i + 'stoke-city.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                          ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Sunderland' in i1I111II :
   I1iiIIIi11 = IIi1i + 'sunderland-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                        ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Swansea' in i1I111II :
   I1iiIIIi11 = IIi1i + 'swansea-city-afc.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                    ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Tottenham' in i1I111II :
   I1iiIIIi11 = IIi1i + 'tottenham-hotspur_zps4e3ed7c1.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '        ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Watford' in i1I111II :
   I1iiIIIi11 = IIi1i + 'watford-fc-hd-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '                              ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'Bromwich' in i1I111II :
   I1iiIIIi11 = IIi1i + 'west-bromwich-albion-logo.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '   ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  elif 'West Ham' in i1I111II :
   I1iiIIIi11 = IIi1i + 'west-ham.png'
   IiII111iI1ii1 = '[COLOR' + i1iiIIiiI111 + ']' + iIIiiIi + ' - ' + i1I111II + '             ' + Oo0OOo + '        ' + i1II11I11ii1 + '        ' + ooO00O0O0 + '        ' + OOoO0oO00o + '        ' + o0OIiII + '        ' + Ii1iI111 + '        ' + OOO0OoO0oo0OO + '[/COLOR]'
  ii111iI1iIi1 ( str ( IiII111iI1ii1 ) , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I1iiIIIi11 , I1iiIIIi11 , i1I111II )
  if 82 - 82: o0o00Oo0O
def O0oO0oo0O ( description ) :
 i1I111II = description
 iI11I1II = ( 'http://www.fullmatchesandshows.com/?s=' + i1I111II ) . replace ( ' ' , '%20' )
 oooOOO0ooOoOOO ( iI11I1II )
 if 68 - 68: o0o00Oo0O
def o0oOoO00 ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 iI11Ii = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , Oo0o0000o0o0 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI11I1II , 10010 , Oo0o0000o0o0 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI1I , iIii1 , '' )
  if 94 - 94: oO0o + OO + oO0OOoo0OO
def OOoOooO00 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iII111Ii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iII111Ii in iII111Ii :
  o0o00OOOO = re . compile ( '(.*?)</h2>' ) . findall ( str ( iII111Ii ) )
  for i11iIi1iIIIIi in o0o00OOOO :
   i11iIi1iIIIIi = i11iIi1iIIIIi
  I1111iiiII1Ii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iII111Ii ) )
  for oO0oOoOoo0 , iI1I , time , o0o000o in I1111iiiII1Ii :
   Iiii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0o000o )
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + i11iIi1iIIIIi + ' - ' + oO0oOoOoo0 + ' - ' + time + '[/COLOR]' , '' , 10010 , Oo0o0000o0o0 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iI1I , iIii1 , ( str ( Iiii ) ) )
   if 26 - 26: iI11I1II1I1I * I11i . Ooo0Oo0oOoo
 O00 ( 'tvshows' , 'Media Info 3' )
 if 10 - 10: ooOoOO0oOO * o000o % I1ii11iIi11i - Ooo0Oo0oOoo % I1ii11iIi11i
def O0oooo000oO0 ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , IIi1i + 'fanart.jpg' , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , IIi1i + 'fanart.jpg' , '' )
 if 96 - 96: o0o00Oo0O . iI1i1IiI - oOo0O0Ooo * I1ii11iIi11i
def OOoOOOo0 ( url ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Live On G-Tv[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , IIi1i + 'TodaysMacthes.png' , iIii1 , '' )
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , url , IiII111iI1ii1 in iI11Ii :
  oOoO00O = IiII111iI1ii1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiII111iI1ii1 :
   pass
  else :
   oOoO00O = IiII111iI1ii1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + oOoO00O + '[/COLOR]' , url , 10013 , iI1I )
 for url , iI1I , IiII111iI1ii1 in i1iIIIi1i :
  oOoO00O = IiII111iI1ii1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiII111iI1ii1 :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + oOoO00O + '[/COLOR]' , url , 10013 , iI1I )
def oooOOO0ooOoOOO ( url ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Live On G-Tv[/COLOR]' , ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , IIi1i + 'TodaysMacthes.png' , iIii1 , '' )
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 if 31 - 31: oO0OOoo0OO . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * iI1i1IiI
 if 22 - 22: Ooo0Oo0oOoo % OO . OOooOOo / oO0OOoo0OO + O0OoO0O00o0oO
 if 85 - 85: oOo0O0Ooo - oO0OOoo0OO % I1ii11iIi11i % IIiIiII11i - ii % OO
 if 40 - 40: OoOOOOOo0o
 if 59 - 59: Ooo0Oo0oOoo * ii + O0OoO0O00o0oO . iI11I1II1I1I / ooOoO0O00
 if 75 - 75: Ooo0Oo0oOoo . O0OoO0O00o0oO - iI11I1II1I1I * oO0o * iI1i1IiI
 if 93 - 93: oO0OOoo0OO
 for url , iI1I , IiII111iI1ii1 in i1iIIIi1i :
  oOoO00O = IiII111iI1ii1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in IiII111iI1ii1 :
   pass
  else :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + oOoO00O + '[/COLOR]' , url , 10013 , iI1I )
   if 18 - 18: oO0OOoo0OO
def OOOooO00OO00O ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( OO0O0OoOO0 )
 for OOo in iI11Ii :
  OoOOooO0O = ( OOo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  oO000o ( 'http:' + OoOOooO0O )
  if 3 - 3: IIiIiII11i - OoOOOOOo0o % OOooOOo / o000o
  if 44 - 44: o0o00Oo0O . OoOOOOOo0o * iI1i1IiI / Ii
  if 56 - 56: OOooOOo % Ii1I - OoOOOOOo0o % iI11I1II1I1I
  if 76 - 76: ii * ii - iI1i1IiI - iI11I1II1I1I . ii / Ii1I
def oOOOO0oo0O0OO ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , url , 8046 , iI1I )
 for url in i1iIIIi1i :
  i11II1I11I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , IIi1i + 'Next.png' )
def O0OOoo0o ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( o00o )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  oO000o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 19 - 19: oO0OOoo0OO % o000o
def iIiiIiiI1Ii111i ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( o00o )
 for url in iI11Ii :
  yt . PlayVideo ( url )
  if 38 - 38: o000o % ii + oO0o * Ii
def ooO ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 7 - 7: oOo0O0Ooo + OO / Ii / I1ii11iIi11i
 iI11Ii = re . compile ( '<a href="([^"]*)" >(.+?)</a></li>' ) . findall ( o00o )
 if 97 - 97: ooOoOO0oOO . Ooo0Oo0oOoo / oOo0O0Ooo
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , iI11I1II , 8041 , IIi1i + 'documentary.png' )
  if 83 - 83: Ooo0Oo0oOoo - Ii1I * o000o
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
  if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . Ooo0Oo0oOoo
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iI1i11IiI11 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( 'class="inactive">.+?</a><a href="([^"]*)">Next</a></div>' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , iI1I )
 for IiII111iI1ii1 , url , iI1I in i1iIIIi1i :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , iI1I )
 for url in next :
  i11II1I11I1 ( 'NEXT PAGE' , url , 8041 , IIi1i + 'Next.png' )
  if 82 - 82: ooOoOO0oOO * oO0o
  if 32 - 32: o0o00Oo0O
def Oo0o0OO0OO000OO ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<meta itemprop="name" content="([^"]*)".+?<meta itemprop="thumbnailUrl" content="([^"]*)".+?<meta itemprop="embedUrl" content="([^"]*)".+?<meta itemprop="description" content="([^"]*)" />' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , iI1I , url , Oo0 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , iI1I )
 for url in i1iIIIi1i :
  O00o0000OO ( ( url ) . replace ( '//' , 'http://' ) )
  if 61 - 61: OO % ooOoO0O00 - iI1i1IiI . oO0OOoo0OO - I1ii11iIi11i + I1ii11iIi11i
def O00o0000OO ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<link rel="canonical" href="([^"]*)">  <link rel="stylesheet"' ) . findall ( o00o )
 for url in iI11Ii :
  OOoOO0ooo ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1i + 'documentary.png' )
  if 12 - 12: I11i / iI11I1II1I1I % IIiIiII11i / Ooo0Oo0oOoo / ooOoO0O00 - oOo0O0Ooo
def OoOOOOOoOo0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , iI1I )
 for url in i1iIIIi1i :
  i11II1I11I1 ( 'NEXT' , url , 8048 , IIi1i + 'Next.png' )
def iIioOo ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00o )
 for url in iI11Ii :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in i1iIIIi1i :
  if 'rtd' in url :
   ooOo0o ( url )
   if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / Ooo0Oo0oOoo + ooOoOO0oOO
def ooOo0o ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( o00o )
 for OOOO0OOoO0O0 , file in iI11Ii :
  url = ( 'https://rtd.rt.com' + OOOO0OOoO0O0 + file )
  oO000o ( url )
  if 17 - 17: O0OoO0O00o0oO + IIiIiII11i
  if 43 - 43: Ooo0Oo0oOoo % OoOOOOOo0o / I11i * ooOoOO0oOO
def oooIi1I11IiI1i ( ) :
 OO0O0OoOO0 = IIIIiiIiiI ( 'http://www.stream2watch.co/live-tv' )
 iI11Ii = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I , IiII111iI1ii1 , I111 in iI11Ii :
  i11II1I11I1 ( ( IiII111iI1ii1 + '[COLOR' + i1iiIIiiI111 + ']' + I111 + '[/COLOR]' ) , iI11I1II , 8086 , iI1I )
  if 25 - 25: Ooo0Oo0oOoo / Ooo0Oo0oOoo % ii - Ii1I * o000o
def i1oooOoOoOO ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 8087 , iI1I )
  if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 in iI11Ii :
  Ii1I1IIIiI1i ( url , IiII111iI1ii1 )
  if 75 - 75: Ii1I
def Ii1I1IIIiI1i ( url , name ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url in iI11Ii :
  print url
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 92 - 92: Ooo0Oo0oOoo / o0o00Oo0O * oOo0O0Ooo - Ooo0Oo0oOoo
def oooOo00000 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 iI11Ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iI11I1II , 3002 , 'http://www.solie.org/alibrary/' + iI1I )
def IiI1IiI1iiI1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iI1I )
def O000o0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 Iiiii1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( o00o )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , IIi1i + 'classicmovies.png' )
 for url , IiII111iI1ii1 in Iiiii1 :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']Season- ' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , IIi1i + 'classicmovies.png' )
 for url in next :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , IIi1i + 'Next.png' )
 for url , iI1I , IiII111iI1ii1 in i1iIIIi1i :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iI1I )
def O0Ooo0O ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( o00o )
 for url in iI11Ii :
  iii1 ( url )
def iii1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( o00o )
 for url in iI11Ii :
  oO000o ( url )
  if 93 - 93: o000o % ooOoO0O00
def OOo0 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI11I1II , 8065 , IIi1i + 'classicmovies.png' )
def OOoo00 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( "v.src = '([^']*)';" ) . findall ( o00o )
 for url in iI11Ii :
  O00Oo0o0000OOoO ( url )
  if 22 - 22: oO0OOoo0OO / oO0OOoo0OO - OoOOOOOo0o % Ooo0Oo0oOoo . O0OoO0O00o0oO + OO
def OooO00oo0O0 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI11I1II , 8065 , IIi1i + 'classictv.png' )
def i1iI ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  if 'mp4' in url :
   oO000o ( url )
 for url in i1iIIIi1i :
  yt . PlayVideo ( url )
  if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
def IiI11IIi11Iii ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 iI11Ii = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iI11I1II , 8071 , IIi1i + 'streams.png' )
def ii11i1I1i ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , url in iI11Ii :
  if '(Free Access)' in IiII111iI1ii1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( Oo0o0000o0o0 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + i1iiIII111ii + '/' + i1iIIi1 + url ) . strip ( )
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , IIi1i + 'streams.png' )
def Iiiii1I ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , IiII111iI1ii1 , url in iI11Ii :
  url = ( ( Oo0o0000o0o0 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + i1iiIII111ii + '/' + i1iIIi1 + url ) . strip ( )
  i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , iI1I , o0Oo00 , '' )
  if 13 - 13: IIiIiII11i . iI1i1IiI - ooOoOO0oOO . oO0o . iI11I1II1I1I
def oO00oooo0OOo ( ) :
 OooOo000o0o ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , IIi1i + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Genres' , 'http://www.xvideos.com' , 10106 , IIi1i + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , IIi1i + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , IIi1i + 'Jizbox.png' , '' , '' )
 OooOo000o0o ( 'Search' , '' , 10107 , IIi1i + 'Jizbox.png' , '' , '' , )
 if 93 - 93: o000o * I11i / O0OoO0O00o0oO - O0OoO0O00o0oO . iI1i1IiI / oOo0O0Ooo
def I111ii1iI ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 i1IiI1ii1i = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OO0O0OoOO0 )
 for url in i1IiI1ii1i :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , IIi1i + 'Jizbox.png' , '' , '' )
 iI11Ii = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iII1ii1 in iI11Ii :
  OooOo000o0o ( ( IiII111iI1ii1 + ' - No of Videos : ' + ( iII1ii1 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , IIi1i + 'Jizbox.png' , '' , '' )
  if 39 - 39: O0OoO0O00o0oO + oO0o
def oOoOOOO0OOO ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 i1IiI1ii1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( OO0O0OoOO0 )
 for url in i1IiI1ii1i :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , IIi1i + 'Next.png' , '' , '' )
 iI11Ii = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , url , IiII111iI1ii1 , O0oo0oO00o in iI11Ii :
  OooOo000o0o ( IiII111iI1ii1 + '--' + O0oo0oO00o , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iI1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 35 - 35: iI1i1IiI * iI11I1II1I1I / oO0OOoo0OO * ooOoO0O00 * o0o00Oo0O % iI11I1II1I1I
  if 97 - 97: Ii + I1ii11iIi11i * O0OoO0O00o0oO % iI1i1IiI . OO
def iiOo0 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , url , IiII111iI1ii1 , iIi11iiIiI1I , OOO00ii1Ii111I11I in iI11Ii :
  OooOo000o0o ( IiII111iI1ii1 + ' - Porn Quality : ' + OOO00ii1Ii111I11I + ' - ' + iIi11iiIiI1I , 'http://www.xvideos.com' + url , 10108 , iI1I , iI1I , OOO00ii1Ii111I11I + ' - ' + iIi11iiIiI1I )
 o0OoOoo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OO0O0OoOO0 )
 for url in o0OoOoo :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , IIi1i + 'Next.png' , '' , '' )
  if 75 - 75: iI1i1IiI * oOo0O0Ooo + iI1i1IiI - ii
def OooO ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iII111Ii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 i1IiI1ii1i = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( OO0O0OoOO0 )
 for url in i1IiI1ii1i :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , IIi1i + 'Next.png' , '' , '' )
 iI11Ii = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iII111Ii ) )
 for url , IiII111iI1ii1 in iI11Ii :
  OooOo000o0o ( IiII111iI1ii1 , 'http://www.xvideos.com' + url , 10105 , IIi1i + 'Jizbox.png' , '' , '' )
  if 85 - 85: IIiIiII11i
  if 55 - 55: Ii1I
def oOoo0OO0 ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIiIi1111iI1 = ( i11IIIiI11 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 IIi1IIIi = iiIiIi1111iI1 . lower ( )
 I1I1Iiii1 = 'http://www.xvideos.com/?k=' + IIi1IIIi
 print I1I1Iiii1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OO0O0OoOO0 = O00OOOoOoo0O ( I1I1Iiii1 )
 iI11Ii = re . compile ( '<div class="thumb-inside"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , iI11I1II , IiII111iI1ii1 , iIi11iiIiI1I , OOO00ii1Ii111I11I in iI11Ii :
  OooOo000o0o ( IiII111iI1ii1 + ' - Porn Quality : ' + OOO00ii1Ii111I11I + ' - ' + iIi11iiIiI1I , 'http://www.xvideos.com' + iI11I1II , 10108 , iI1I , iI1I , OOO00ii1Ii111I11I + ' - ' + iIi11iiIiI1I )
 o0OoOoo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II in o0OoOoo :
  OooOo000o0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iI11I1II , 10105 , IIi1i + 'Next.png' , '' , '' )
  if 11 - 11: Ii1I . Ii1I + IIiIiII11i * OOooOOo . OO
def I1I1i1I1I1I1 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( OO0O0OoOO0 )
 i1iIIIi1i = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( OO0O0OoOO0 )
 i11iI11I1I = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( OO0O0OoOO0 )
 for url in iI11Ii :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']LOW[/COLOR]' , url , 222 , IIi1i + 'Jizbox.png' )
 for url in i1iIIIi1i :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']HIGH[/COLOR]' , url , 222 , IIi1i + 'Jizbox.png' )
 for url in i11iI11I1I :
  if 'http' in url :
   OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']HLS[/COLOR]' , url , 222 , IIi1i + 'Jizbox.png' )
   if 34 - 34: oO0o * OoOOOOOo0o * I1ii11iIi11i
def Iioo0O00ooo0o ( url ) :
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 import urlresolver
 try : O0O00OooO . play ( url )
 except : pass
 if 26 - 26: OO / iI11I1II1I1I - iI11I1II1I1I
 if 57 - 57: OO
def IiI11I1Ii11II ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 8091 , IIi1i + 'gofish.png' )
def oo0ooOoOOoO ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 8092 , iI1I )
 for url in next :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT[/COLOR]' , url , 8091 , IIi1i + 'Next.png' )
def Oo0000o ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 next = re . compile ( 'href="([^"]*)">&raquo;' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 8092 , iI1I )
 for url in next :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT[/COLOR]' , url , 8091 , IIi1i + 'Next.png' )
def iI1IiiiIIiiII ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( "videoId: '([^']*)'," ) . findall ( OO0O0OoOO0 )
 for url in iI11Ii :
  yt . PlayVideo ( url )
  if 94 - 94: OOooOOo + OO . oO0OOoo0OO
  if 69 - 69: o0o00Oo0O - o0o00Oo0O
  if 41 - 41: OO % I11i
oo0O0oOOO0o = '{PQ},' ; oOo0Oo0Oo0 = '{SC},' ; OooOo0o0OO = '{XG},' ; iiI1ii1IIiI = '{JP},' ; IIi1i1I11IIII = '{HW},' ; OooOoOOO00O = '{RT},'
def I111iIIII11iI ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oOoOO = ( Oo0o0000o0o0 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 iI11I1II = ( Oo0o0000o0o0 ( 'aHR0cDovL20zLmRvY3Rvci1tb3ZpZXMuY29tL2VuZ2xpc2gv' ) )
 if 20 - 20: oO0OOoo0OO . oO0o * iI1i1IiI
 IiIi1I1ii111 = ( Oo0o0000o0o0 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OOii11Ii1IiiI1 = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 O00o0o = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OOoO0o0OOo0 = ( Oo0o0000o0o0 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0OoO0ooOOO = ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + i11IIIiI11
 IiI1iIIIi1iIi = ( Oo0o0000o0o0 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 OOo0OOOoOOo = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 III = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 ooo0o0O = ( Oo0o0000o0o0 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 32 - 32: ii % ii . o000o - oO0OOoo0OO . OOooOOo * o000o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 OO0O0OoOO0 = oO0Oo ( iI11I1II )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 55 - 55: Ooo0Oo0oOoo
 if 93 - 93: Ii . I11i
 IIi1i11111 = oO0Oo ( IiIi1I1ii111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 ooOO00O00oo = oO0Oo ( OOii11Ii1IiiI1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IiiIiI1IIi1IIIii = oO0Oo ( O00o0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 OOO0o = oO0Oo ( O0OoO0ooOOO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0O00OO = oO0Oo ( IiI1iIIIi1iIi )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIiiiI = oO0Oo ( OOo0OOOoOOo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0Oooo0OoO = oO0Oo ( III )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 Iiii1IIIIiiI11 = oO0Oo ( ooo0o0O )
 if 8 - 8: OoOOOOOo0o + oOo0O0Ooo / iI1i1IiI / oO0OOoo0OO + iI11I1II1I1I + ii
 if 33 - 33: IIiIiII11i - OO - oO0OOoo0OO
 if OO0O0OoOO0 != 'Failed' :
  iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OO0O0OoOO0 )
  for oO00oOoo00o0 , IiII111iI1ii1 in iI11Ii :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iI11I1II + oO00oOoo00o0 ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 41 - 41: o000o / O0OoO0O00o0oO + iI1i1IiI + oO0OOoo0OO
    if 13 - 13: Ii - Ii . iI11I1II1I1I
    if 33 - 33: ii + ooOoOO0oOO / ooOoOO0oOO + ooOoOO0oOO * OO
    if 26 - 26: ooOoOO0oOO . oOo0O0Ooo . iI1i1IiI - ii / iI11I1II1I1I
    if 47 - 47: OO
    if 76 - 76: oO0o * iI11I1II1I1I + Ii1I - oO0OOoo0OO - Ooo0Oo0oOoo / ooOoO0O00
    if 27 - 27: Ii1I . OO
 if IIi1i11111 != 'Failed' :
  i11iI11I1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( IIi1i11111 )
  for oO00oOoo00o0 , IiII111iI1ii1 in i11iI11I1I :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiIi1I1ii111 + oO00oOoo00o0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if ooOO00O00oo != 'Failed' :
  Oo0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO00O00oo )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in Oo0o :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Silent Hunter[/COLOR]' ) , iI11I1II , 222 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 2 - 2: ii % iI11I1II1I1I
    O00 ( 'tvshows' , 'Media Info 3' )
 if IiiIiI1IIi1IIIii != 'Failed' :
  I11iIiI1 = [ ]
  i1I1iiii1Ii11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIiI1IIi1IIIii )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in i1I1iiii1Ii11 :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    if IiII111iI1ii1 in I11iIiI1 :
     pass
    else :
     ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iI11I1II , 1016 , iII1 , Ii11Ii1iI , ooo0O )
     I11iIiI1 . append ( IiII111iI1ii1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     O00 ( 'tvshows' , 'Media Info 3' )
 if OOO0o != 'Failed' :
  IiIIIIi = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( OOO0o )
  for iI11I1II , iI1I , IiII111iI1ii1 in IiIIIIi :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iI11I1II , 7067 , iI1I )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 51 - 51: IIiIiII11i . o000o . oO0o % IIiIiII11i
    O00 ( 'tvshows' , 'Media Info 3' )
 if O0O00OO != 'Failed' :
  III1I1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0O00OO )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in III1I1ii :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Redemption[/COLOR]' ) , iI11I1II , 222 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Redemption Links" )
    if 4 - 4: iI11I1II1I1I . ooOoO0O00
    O00 ( 'tvshows' , 'Media Info 3' )
 if IIiiiI != 'Failed' :
  Oo00oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiiiI )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in Oo00oo :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Reaper[/COLOR]' ) , iI11I1II , 222 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 79 - 79: Ii1I / o0o00Oo0O % I11i
    O00 ( 'tvshows' , 'Media Info 3' )
 if oO0Oooo0OoO != 'Failed' :
  o0ooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0Oooo0OoO )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in o0ooo :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i1Ii ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Herovision[/COLOR]' ) , iI11I1II , 222 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / O0OoO0O00o0oO . Ii1I * oO0OOoo0OO
    O00 ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: iI11I1II1I1I / Ii1I % oO0OOoo0OO
 if Iiii1IIIIiiI11 != 'Failed' :
  Oooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Iiii1IIIIiiI11 )
  for iI11I1II , iII1 , IiII111iI1ii1 in Oooo :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Silent Hunter[/COLOR]' ) , iI11I1II , 222 , iII1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 74 - 74: oO0OOoo0OO % OOooOOo / I1ii11iIi11i
    O00 ( 'tvshows' , 'Media Info 3' )
 Ooii1IIi1ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 2 - 2: OO % OO % ooOoOO0oOO
 for IiI in Ooii1IIi1ii :
  o0o0OO0o00o0O = O000oo0O + IiI + O0o0Oo
  o0o00OoOo0 = oO0Oo ( o0o0OO0o00o0O )
  if o0o00OoOo0 != 'Failed' :
   oo0O0000O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o00OoOo0 )
   for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in oo0O0000O0 :
    if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
     i1Ii ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + ' - Source Pandoras[/COLOR]' , iI11I1II , 222 , iII1 , Ii11Ii1iI , ooo0O )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 53 - 53: OO % I1ii11iIi11i
     O00 ( 'tvshows' , 'Media Info 3' )
     if 42 - 42: Ii / oOo0O0Ooo - oO0o - oO0OOoo0OO + IIiIiII11i % oO0OOoo0OO
 Ooii1IIi1ii = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 50 - 50: ii + o000o * oOo0O0Ooo - OoOOOOOo0o / Ii
 if 5 - 5: o0o00Oo0O - oOo0O0Ooo
 for IiI in Ooii1IIi1ii :
  o0o0OO0o00o0O = oOoOO + IiI
  IiiI1iii1iIiiI = oO0Oo ( o0o0OO0o00o0O )
  if IiiI1iii1iIiiI != 'Failed' :
   II1iiiiI1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( IiiI1iii1iIiiI )
   for oO00oOoo00o0 , IiII111iI1ii1 in II1iiiiI1 :
    if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
     OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOoOO + IiI + oO00oOoo00o0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
     O00 ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: OO + iI11I1II1I1I + oOo0O0Ooo + ooOoOO0oOO
     if 72 - 72: oO0o + Ii + Ii1I
def oOooOoOOo0O ( ) :
 if 41 - 41: iI1i1IiI
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 if 88 - 88: o0o00Oo0O . o000o % oOo0O0Ooo
 iI11I1II = ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( i11IIIiI11 ) . replace ( ' ' , '%20' )
 oo00o0 = ( Oo0o0000o0o0 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 IiIi1I1ii111 = ( Oo0o0000o0o0 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 OOii11Ii1IiiI1 = ( Oo0o0000o0o0 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 O00o0o = ( Oo0o0000o0o0 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIi1IIIi ) . replace ( ' ' , '+' )
 OOoO0o0OOo0 = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0OoO0ooOOO = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 IiI1iIIIi1iIi = ( Oo0o0000o0o0 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 10 - 10: oOo0O0Ooo + o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 75 - 75: o0o00Oo0O % iI11I1II1I1I / OOooOOo % O0OoO0O00o0oO / OO
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 OO0O0OoOO0 = oO0Oo ( iI11I1II )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iiiI1I11i1 = oO0Oo ( oo00o0 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 IIi1i11111 = oO0Oo ( IiIi1I1ii111 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 ooOO00O00oo = oO0Oo ( OOii11Ii1IiiI1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IiiIiI1IIi1IIIii = cloudflare . source ( O00o0o )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiI1iii1iIiiI = oO0Oo ( OOoO0o0OOo0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OOO0o = oO0Oo ( O0OoO0ooOOO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 O0O00OO = oO0Oo ( IiI1iIIIi1iIi )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 31 - 31: Ii * OOooOOo
 if O0O00OO != 'Failed' :
  III1I1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0O00OO )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in III1I1ii :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source HeroVision[/COLOR]' ) , iI11I1II , 1016 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 69 - 69: Ii
    O00 ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: o0o00Oo0O
 if OOO0o != 'Failed' :
  IiIIIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOO0o )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in IiIIIIi :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- source Reaper[/COLOR]' ) , iI11I1II , 1016 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 21 - 21: oO0o % iI11I1II1I1I . oO0o
    O00 ( 'tvshows' , 'Media Info 3' )
    if 99 - 99: I11i * O0OoO0O00o0oO % o000o * o000o + ii
    if 82 - 82: Ooo0Oo0oOoo / OOooOOo - O0OoO0O00o0oO / oO0OOoo0OO
    if 50 - 50: O0OoO0O00o0oO + oO0o . Ii + Ii1I + Ii
    if 31 - 31: o000o * ooOoOO0oOO . OOooOOo * Ooo0Oo0oOoo
    if 28 - 28: OO + oOo0O0Ooo - I1ii11iIi11i % O0OoO0O00o0oO . Ooo0Oo0oOoo + oOo0O0Ooo
    if 72 - 72: OoOOOOOo0o / I1ii11iIi11i / o000o * OOooOOo + O0OoO0O00o0oO
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - OO . ii
    O00 ( 'tvshows' , 'Media Info 3' )
 if OO0O0OoOO0 != 'Failed' :
  iI11Ii = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for iI1I , iI11I1II , IiII111iI1ii1 in iI11Ii :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + iI11I1II , 10044 , iI1I , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 10 - 10: ooOoOO0oOO
    O00 ( 'tvshows' , 'Media Info 3' )
    if 48 - 48: iI1i1IiI * ooOoO0O00 % ii * OoOOOOOo0o * oO0o
    if 7 - 7: iI1i1IiI . OoOOOOOo0o . iI1i1IiI - ooOoOO0oOO
    if 33 - 33: oO0OOoo0OO + ii - oO0o / ooOoO0O00 / ii
    if 82 - 82: Ii1I / O0OoO0O00o0oO - iI1i1IiI / I1ii11iIi11i * oO0o
    if 55 - 55: ii
    if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
    if 38 - 38: o0o00Oo0O
    if 79 - 79: ooOoO0O00 . o000o
    if 34 - 34: ooOoOO0oOO * IIiIiII11i
    if 71 - 71: OO
 if iiiI1I11i1 != 'Failed' :
  i1iIIIi1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiI1I11i1 )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in i1iIIIi1i :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , iI11I1II , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 97 - 97: Ii1I
    O00 ( 'tvshows' , 'Media Info 3' )
 if IIi1i11111 != 'Failed' :
  i11iI11I1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIi1i11111 )
  for IiII111iI1ii1 in i11iI11I1I :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1I1ii111 + IiII111iI1ii1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 86 - 86: I1ii11iIi11i - O0OoO0O00o0oO . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
    O00 ( 'tvshows' , 'Media Info 3' )
 if ooOO00O00oo != 'Failed' :
  Oo0o = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ooOO00O00oo )
  for IiII111iI1ii1 in Oo0o :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOii11Ii1IiiI1 + IiII111iI1ii1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 34 - 34: I11i . ooOoOO0oOO % OO - o0o00Oo0O / ooOoOO0oOO
    O00 ( 'tvshows' , 'Media Info 3' )
 if IiiIiI1IIi1IIIii != 'Failed' :
  i1I1iiii1Ii11 = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IiiIiI1IIi1IIIii )
  for iI11I1II , iI1I , IiII111iI1ii1 in i1I1iiii1Ii11 :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + ' - Source - Dizi[/COLOR]' , iI11I1II , 8062 , iI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 91 - 91: Ii % ooOoOO0oOO * o000o - Ii1I . ooOoOO0oOO
    O00 ( 'tvshows' , 'Media Info 3' )
 if IiiI1iii1iIiiI != 'Failed' :
  II1iiiiI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiI1iii1iIiiI )
  for iI11I1II , iII1 , ooo0O , Ii11Ii1iI , IiII111iI1ii1 in II1iiiiI1 :
   if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
    ii111iI1iIi1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '- Source Scooby[/COLOR]' ) , iI11I1II , 1016 , iII1 , Ii11Ii1iI , ooo0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 28 - 28: Ii
    O00 ( 'tvshows' , 'Media Info 3' )
    if 51 - 51: oOo0O0Ooo + oO0OOoo0OO * o0o00Oo0O . OoOOOOOo0o
 O00Oo00OOoO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if IiiI1iii1iIiiI != 'Failed' :
  for IiI in O00Oo00OOoO0 :
   o0o0OO0o00o0O = O000oo0O + IiI + O0o0Oo
   oO0Oooo0OoO = O00OOOoOoo0O ( o0o0OO0o00o0O )
   if oO0Oooo0OoO != 'Failed' :
    o0ooo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0Oooo0OoO )
    for IiII111iI1ii1 , ooo0O , iI11I1II , iI1I , o0Oo00 , OoiI1I1 in o0ooo :
     if IIi1IIIi in IiII111iI1ii1 . lower ( ) :
      ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + ' - Source Pandoras[/COLOR]' , iI11I1II , OoiI1I1 , iI1I , o0Oo00 , ooo0O )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
      if 99 - 99: oO0o / ooOoO0O00 . Ii1I
      O00 ( 'tvshows' , 'Media Info 3' )
      if 23 - 23: OoOOOOOo0o * oO0OOoo0OO - Ooo0Oo0oOoo . o0o00Oo0O % iI11I1II1I1I
      if 19 - 19: oOo0O0Ooo
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOooI1I1i11 ( ) :
 if 79 - 79: I11i - IIiIiII11i
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 iI11I1II = ( Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OO0O0OoOO0 = O00OOOoOoo0O ( iI11I1II )
 iI11Ii = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for IiII111iI1ii1 , iI1I , O0Ooo0o in iI11Ii :
  o0o00O = Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
   i11II1I11I1 ( IiII111iI1ii1 , '' , 7022 , o0o00O )
   if 46 - 46: OOooOOo
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
i1iiII = '{ZH},' ; ooii = '{IX},' ; oOO0O0O0OO00oo = '{LM},'
if 39 - 39: OO % OOooOOo * Ii1I - ii - I1ii11iIi11i
def Oo0oOOO ( url ) :
 o00OoOooo = cloudflare . source ( url )
 iI11Ii = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( o00OoOooo )
 for url , oooOoO , i1ii1II1ii , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( oooOoO ) . replace ( 'Sezon' , ' Season ' ) + ( i1ii1II1ii ) . replace ( 'Bölüm' , ' Episode ' ) + IiII111iI1ii1 , url , 8063 , '' )
  if 47 - 47: oO0OOoo0OO + iI1i1IiI + ooOoO0O00
  if 6 - 6: o000o / o0o00Oo0O / OoOOOOOo0o / OO / o000o . iI11I1II1I1I
  if 62 - 62: iI11I1II1I1I
  if 4 - 4: Ii1I * Ooo0Oo0oOoo . Ooo0Oo0oOoo . IIiIiII11i / O0OoO0O00o0oO
def oOOoOOooO0 ( url ) :
 o00OoOooo = cloudflare . source ( url )
 iI11Ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o00OoOooo )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , url , 222 , '' )
  if 42 - 42: iI11I1II1I1I * OoOOOOOo0o / oO0o + O0OoO0O00o0oO
  if 48 - 48: ii - ooOoOO0oOO . Ii * iI1i1IiI - OoOOOOOo0o - I11i
  if 59 - 59: iI1i1IiI / Ooo0Oo0oOoo . I1ii11iIi11i
  if 100 - 100: o0o00Oo0O
def oOOO00Oo ( ) :
 if 48 - 48: IIiIiII11i + IIiIiII11i * ooOoO0O00 / OoOOOOOo0o
 o00OoOooo = cloudflare . source ( Oo0o0000o0o0 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 iI11Ii = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o00OoOooo )
 for iI11I1II , iI1I , IiII111iI1ii1 , i1ii1II1ii in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 + '  -  ' + ( i1ii1II1ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI11I1II , 8063 , iI1I )
  if 37 - 37: iI11I1II1I1I % Ooo0Oo0oOoo / OO
def i1IIIII1 ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 , iI1I in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 8002 , iI1I )
def IIIiiiiiI1I ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( o00o )
 for iI1I , time , url , IiII111iI1ii1 , Oo0 in iI11Ii :
  ii111iI1iIi1 ( '%s %s' % ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , time ) , url , 1015 , iI1I , Oo0 )
  if 64 - 64: OO * iI11I1II1I1I . Ii1I / Ooo0Oo0oOoo * iI11I1II1I1I
def i1i111III1 ( ) :
 if 12 - 12: Ii1I * oO0OOoo0OO - Ooo0Oo0oOoo . oO0o + oO0o + iI1i1IiI
 i11II1I11I1 ( 'Coronation Street' , '' , 8001 , '' )
 i11II1I11I1 ( 'Eastenders' , '' , 8002 , '' )
 i11II1I11I1 ( 'Emmerdale' , '' , 8003 , '' )
 i11II1I11I1 ( 'Hollyoaks' , '' , 8004 , '' )
 i11II1I11I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 29 - 29: ii . ooOoOO0oOO % ooOoOO0oOO
 if 9 - 9: I1ii11iIi11i - I1ii11iIi11i - I11i + ooOoOO0oOO - IIiIiII11i . oOo0O0Ooo
 if 57 - 57: iI1i1IiI - oOo0O0Ooo + ii / iI1i1IiI . oO0OOoo0OO % ooOoO0O00
 if 52 - 52: o0o00Oo0O - iI11I1II1I1I / oO0o / OO
def I11Iii11i11I1 ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 iI11Ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'Holly' in IiII111iI1ii1 :
   iI1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iI11I1II :
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI11I1II . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 1 - 1: ooOoO0O00 . Ii1I * I11i % IIiIiII11i % iI11I1II1I1I
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 71 - 71: oO0o + OO / Ooo0Oo0oOoo * I1ii11iIi11i . OoOOOOOo0o . Ooo0Oo0oOoo
def III11 ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 iI11Ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'East' in IiII111iI1ii1 :
   iI1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iI11I1II :
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI11I1II . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 32 - 32: ooOoOO0oOO + oOo0O0Ooo % O0OoO0O00o0oO * Ii * Ii - iI11I1II1I1I
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: IIiIiII11i % iI1i1IiI . IIiIiII11i % OO / OO * Ooo0Oo0oOoo
def iiiIiIII ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 iI11Ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'Emmer' in IiII111iI1ii1 :
   iI1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iI11I1II :
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI11I1II . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 49 - 49: oOo0O0Ooo / IIiIiII11i / OoOOOOOo0o + I1ii11iIi11i
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: iI11I1II1I1I . OoOOOOOo0o * IIiIiII11i
def ooOoo000O ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 iI11Ii = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'Coro' in IiII111iI1ii1 :
   iI1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iI11I1II :
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI11I1II . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 81 - 81: ooOoO0O00 + I11i / OO
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: OoOOOOOo0o
def iII1i1 ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( 'http://uksoapshare.blogspot.co.uk/' )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'Celeb' in IiII111iI1ii1 :
   iI1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iI11I1II :
    OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI11I1II . replace ( '\\/' , '/' ) , 8006 , iI1I )
   else :
    pass
    if 34 - 34: oO0o / ii - o000o / o000o * oOo0O0Ooo
def o0o000OOOO ( name , url ) :
 i1i11ii1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if i1i11ii1 :
  o0iiii1ii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  o00o = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( o00o ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  o00o = open_url ( url )
  Ii1iii11I = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( o00o ) [ - 1 ]
  o0iiii1ii = Ii1iii11I . replace ( '\\/' , '/' )
 I1I1i1i = xbmcgui . ListItem ( name , '' , '' )
 I1I1i1i . setPath ( o0iiii1ii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1I1i1i )
 if 2 - 2: ii - OoOOOOOo0o % o000o / oOo0O0Ooo / I11i
 if 3 - 3: IIiIiII11i / O0OoO0O00o0oO
def i1I ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 iI11Ii = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iI11I1II , 7071 , IIi1i + 'popcorn.png' )
 for iI11I1II , IiII111iI1ii1 in i1iIIIi1i :
  i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iI11I1II , 7071 , IIi1i + 'popcorn.png' )
  if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - oO0OOoo0OO / I1ii11iIi11i
def iIi11ii1 ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI11Ii = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'Movies' in IiII111iI1ii1 :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( iI11I1II ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , IIi1i + 'popcorn.png' )
def iII ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o00o )
 iI11Ii = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( o00o )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iI1I )
 for url in i1iIIIi1i :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , IIi1i + 'Next.png' )
  if 73 - 73: OoOOOOOo0o / oOo0O0Ooo / ii + oOo0O0Ooo
  if 57 - 57: O0OoO0O00o0oO . OoOOOOOo0o % I11i
def I1I11 ( url ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 iI11Ii = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , url , iI1I in iI11Ii :
  if '{{' in IiII111iI1ii1 :
   pass
  else :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iI1I )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
iI1i1iI1iI = '{UJ},' ; I1IIiIi = '{WE},' ; OOOOoOoO = '{WP},' ; OO000 = '{PP},'
def o0oOoo0o ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( o00o )
 for IiII111iI1ii1 , url , iI1I in iI11Ii :
  if '{{' in IiII111iI1ii1 :
   pass
  else :
   i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iI1I )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiIiIIi ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  O00Oo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00Oo ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 222 , IIi1i + 'popcorn.png' )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: I11i / o0o00Oo0O - ii
 if 74 - 74: iI11I1II1I1I / OoOOOOOo0o
 if 59 - 59: OoOOOOOo0o / IIiIiII11i - OO % OOooOOo % ii
def O0o ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o00o )
 i1iIIIi1i = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if '(cooltvseries.com)' in IiII111iI1ii1 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , IIi1i + 'CoolSeries.png' )
 for url , IiII111iI1ii1 in i1iIIIi1i :
  if '(cooltvseries.com)' in IiII111iI1ii1 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , IIi1i + 'CoolSeries.png' )
def I1iII ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( o00o )
 for url in iI11Ii :
  oO000o ( ( url ) . replace ( ' ' , '%20' ) )
ooOOOOoO = '{XX},' ; O00000OO00OO = '{UD},' ; iI11iI = '{YT},' ; Oo0oOO = '{JS},' ; iIiOo = '{PF},'
if 48 - 48: O0OoO0O00o0oO
def I1111III111ii ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 iI11Ii = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 , iI1I in iI11Ii :
  OOoOO0ooo ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( Oo0o0000o0o0 ( iI11I1II ) ) , 222 , iI1I )
  if 90 - 90: Ooo0Oo0oOoo
def o0oOooO ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( o00o )
 for iI1I , url , IiII111iI1ii1 in iI11Ii :
  if 'youtu' in url :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iI1I )
 for url in next :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT[/COLOR]' , url , 7050 , IIi1i + 'Next.png' )
  if 99 - 99: Ii - iI1i1IiI
def o0O0O0O00o ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ooi1IIii1i ( url ) :
 o00o = O00OOOoOoo0O
 iI11Ii = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( o00o )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 222 , iI1I )
  if 60 - 60: OoOOOOOo0o % I1ii11iIi11i / Ooo0Oo0oOoo . iI1i1IiI / ooOoOO0oOO - ii
  if 76 - 76: o0o00Oo0O
  if 71 - 71: oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + o000o + o000o + iI1i1IiI
  if 4 - 4: I11i + Ooo0Oo0oOoo / iI1i1IiI + ooOoO0O00 % I11i % iI1i1IiI
def ooOooOooOOO ( ) :
 if 59 - 59: Ooo0Oo0oOoo
 i11II1I11I1 ( 'All Channels' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Entertainment' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Movies' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Music' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'News' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Sports' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Documentary' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Kids' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Food' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Religious' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'USA Channels' , '' , 7021 , IIi1i + 'livetv.png' )
 i11II1I11I1 ( 'Other' , '' , 7021 , IIi1i + 'livetv.png' )
 if 63 - 63: oO0o . o000o + ooOoOO0oOO . OOooOOo / Ii / iI1i1IiI
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + O0OoO0O00o0oO
def I11II11IiI11 ( Cat_Name ) :
 if 97 - 97: oO0OOoo0OO / iI11I1II1I1I % oO0OOoo0OO / oOo0O0Ooo * iI1i1IiI % OOooOOo
 i1iiii1 = False
 oOO0000 = '0'
 if Cat_Name == 'All Channels' : i1iiii1 = True
 if Cat_Name == 'Entertainment' : oOO0000 = '1'
 if Cat_Name == 'Movies' : oOO0000 = '2'
 if Cat_Name == 'Music' : oOO0000 = '3'
 if Cat_Name == 'News' : oOO0000 = '4'
 if Cat_Name == 'Sports' : oOO0000 = '5'
 if Cat_Name == 'Documentary' : oOO0000 = '6'
 if Cat_Name == 'Kids' : oOO0000 = '7'
 if Cat_Name == 'Food' : oOO0000 = '8'
 if Cat_Name == 'Religious' : oOO0000 = '9'
 if Cat_Name == 'USA Channels' : oOO0000 = '10'
 if Cat_Name == 'Other' : oOO0000 = '11'
 if 84 - 84: o0o00Oo0O % OoOOOOOo0o . OoOOOOOo0o . iI1i1IiI * Ooo0Oo0oOoo
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI11Ii = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( o00o )
 print 'Len Match: >>>' + str ( len ( iI11Ii ) )
 for IiII111iI1ii1 , iI1I , O0Ooo0o in iI11Ii :
  o0o00O = Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  if O0Ooo0o == oOO0000 :
   i11II1I11I1 ( IiII111iI1ii1 , '' , 7022 , o0o00O )
  elif i1iiii1 == True :
   i11II1I11I1 ( IiII111iI1ii1 , '' , 7022 , o0o00O )
  else : pass
  if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: oOo0O0Ooo + o000o % ooOoOO0oOO % iI11I1II1I1I - ii
def iIIiI1 ( Search_Name ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 iI11Ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o00o )
 iI11Ii = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( o00o )
 for iI1I , iI11I1II , oo00o0 , IiIi1I1ii111 in iI11Ii :
  o0o00O = Oo0o0000o0o0 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iI1I ) . replace ( '\\' , '' )
  OOoOO0ooo ( Search_Name + ': Link 1' , ( iI11I1II ) . replace ( '\\' , '' ) , 222 , o0o00O )
  OOoOO0ooo ( Search_Name + ': Link 2' , ( oo00o0 ) . replace ( '\\' , '' ) , 222 , o0o00O )
  OOoOO0ooo ( Search_Name + ': Link 3' , ( IiIi1I1ii111 ) . replace ( '\\' , '' ) , 222 , o0o00O )
  if 4 - 4: ii + iI1i1IiI % o0o00Oo0O + iI11I1II1I1I % iI1i1IiI * Ii
def III1I1iI1IIIIII ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI11Ii = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , ( iI11I1II ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , IIi1i + 'english.png' )
def OO0oO0Oo ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 iI11Ii = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , ( iI11I1II ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , IIi1i + 'xxx.png' )
def OoooOO0 ( ) :
 o00o = O00OOOoOoo0O ( Oo0o0000o0o0 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 iI11Ii = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for IiII111iI1ii1 , iI11I1II in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , ( iI11I1II ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , IIi1i + 'vod(1).png' )
  if 69 - 69: IIiIiII11i + iI1i1IiI
def oooOOO ( url ) :
 url
 i1I111i1ii = xbmcgui . ListItem ( IiII111iI1ii1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I111i1ii )
 return
 if 4 - 4: o0o00Oo0O / Ooo0Oo0oOoo . oO0o - oO0OOoo0OO / O0OoO0O00o0oO
 if 25 - 25: Ooo0Oo0oOoo * OOooOOo - I1ii11iIi11i . oO0OOoo0OO . o000o
def oo00Oo0oO00Oo ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( o00o )
 for url , ooo0O , iI1I , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iI1I , '' , ( ooo0O ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  O00 ( 'tvshows' , 'Media Info 3' )
 for url in i1iIIIi1i :
  i11II1I11I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , IIi1i + 'Next.png' )
  if 20 - 20: I11i / OO
def II1I11 ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for url , ooo0O , iI1I in iI11Ii :
  i1Ii ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iI1I , '' , ooo0O )
  O00 ( 'tvshows' , 'Media Info 3' )
 Ii1iiII1i = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for I11iIiIii in Ii1iiII1i :
  Ooooo = ( I11iIiIii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  ii111iI1iIi1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iI1I , '' , Ooooo )
  if 29 - 29: Ii1I % oOo0O0Ooo - ooOoOO0oOO + oOo0O0Ooo . oOo0O0Ooo
def ii11ii11II ( INFO ) :
 Iii1I1I11iiI1 ( 'info for workout' , INFO )
 if 35 - 35: I1ii11iIi11i * IIiIiII11i
 if 32 - 32: o000o . I1ii11iIi11i / oO0OOoo0OO + oO0OOoo0OO . Ii1I
 if 50 - 50: iI11I1II1I1I * o000o
def o0OoIII1IIiIi1 ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'cat-item-.+?"><a href="([^"]*)" >(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , url , 9031 , IIi1i + 'icon.png' )
def OOO0O ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , url , 9032 , IIi1i + 'icon.png' )
def I1iiIIIII1III ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( o00o )
 for IiII111iI1ii1 , url in iI11Ii :
  if '://' in IiII111iI1ii1 :
   pass
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , IIi1i + 'icon.png' )
def II11iiIIiI11I ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( o00o )
 for IiII111iI1ii1 , url in iI11Ii :
  OOoOO0ooo ( IiII111iI1ii1 , url , 222 , IIi1i + 'icon.png' )
  if 56 - 56: ii * OO + ooOoOO0oOO / oOo0O0Ooo * OO / ooOoO0O00
  if 47 - 47: oO0OOoo0OO - OoOOOOOo0o
  if 98 - 98: o000o . ooOoOO0oOO / OOooOOo . oO0OOoo0OO
def i111iIi1i1 ( ) :
 o00o = O00OOOoOoo0O ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 iI11Ii = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  if 'category' in iI11I1II :
   i11II1I11I1 ( IiII111iI1ii1 , 'http://www.disclose.tv/' + iI11I1II , 7010 , IIi1i + 'disclose.png' )
   if 65 - 65: OOooOOo . IIiIiII11i % iI1i1IiI + OoOOOOOo0o
   if 37 - 37: o000o - iI11I1II1I1I + IIiIiII11i . OoOOOOOo0o % iI11I1II1I1I
def i11iiI ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( o00o )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( o00o )
 for url , IiII111iI1ii1 , iI1I in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , 'http://www.disclose.tv/' + url , 7011 , iI1I )
 for url in next :
  i11II1I11I1 ( 'NEXT' , url , 7010 , IIi1i + 'Next.png' )
  if 8 - 8: ooOoO0O00 + IIiIiII11i / OoOOOOOo0o + Ii1I % OoOOOOOo0o - iI11I1II1I1I
  if 29 - 29: I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( o00o )
 i11iI11I1I = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  if 'http' in url :
   OOoOO0ooo ( 'video/flv' , url , 222 , IIi1i + 'disclose.png' )
 for url , IiII111iI1ii1 in i1iIIIi1i :
  OOoOO0ooo ( IiII111iI1ii1 , url , 222 , IIi1i + 'disclose.png' )
 for url in i11iI11I1I :
  OOoOO0ooo ( 'YT Link' , url , 8043 , IIi1i + 'disclose.png' )
  if 64 - 64: ooOoO0O00
  if 31 - 31: Ooo0Oo0oOoo / oO0OOoo0OO % o000o + ii
def iiI1IiIi1i1I ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , IIi1i + 'icon.png' )
  if 31 - 31: OoOOOOOo0o / OoOOOOOo0o
def o00000O ( name , url , img ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iIiiiII11 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 ooo00Oo0 = len ( iIiiiII11 )
 if 46 - 46: o000o
 if 56 - 56: ii
 if ooo00Oo0 == 1 :
  for oOooOOOO0oOo in iIiiiII11 :
   oOooOOOO0oOo = oOooOOOO0oOo . replace ( 'player' , 'watch' )
   iIiI = oOooOOOO0oOo + '&fv=&sou='
   Oo00o0OOo0OO = O00OOOoOoo0O ( iIiI )
   I1i1iiIi = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( Oo00o0OOo0OO )
   for OOooO0Oo0o000 in I1i1iiIi :
    IIi1IiiIi1III = False
    Resolve ( OOooO0Oo0o000 )
    if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - o000o / Ii1I
 elif ooo00Oo0 > 1 :
  if 16 - 16: OoOOOOOo0o
  for oOooOOOO0oOo in iIiiiII11 :
   Oo00O00o0 = O00OOOoOoo0O ( oOooOOOO0oOo )
   IiII1 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo00O00o0 )
   iI1I1I = IiII1
   iI1I1I = ( str ( iI1I1I ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iI1I1I
   OOoOO0ooo ( 'DOUBLE LINK' , iI1I1I , 424 , '' )
   if 81 - 81: Ii % ooOoO0O00 % IIiIiII11i % oOo0O0Ooo + oOo0O0Ooo % Ii1I
   for url in IiII1 :
    i11II1I11I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oo00o0 = Google . resolve ( url )
    except :
     pass
    try :
     i1iiiI1I = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oo00o0 ) )
     for o00OoOOoO , iii1i1Iiiiiii in i1iiiI1I :
      if 58 - 58: I11i / Ii / o0o00Oo0O % Ooo0Oo0oOoo % oOo0O0Ooo
      HD_URLS . append ( o00OoOOoO )
      SD_URLS . append ( iii1i1Iiiiiii )
    except :
     pass
 else :
  pass
  if 86 - 86: OO + OOooOOo / oOo0O0Ooo + Ooo0Oo0oOoo % Ooo0Oo0oOoo / Ii
def iIiI1I ( ) :
 if 2 - 2: I11i . OoOOOOOo0o % OOooOOo
 if 58 - 58: Ii1I % OoOOOOOo0o * OoOOOOOo0o - iI1i1IiI
 i11II1I11I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , IIi1i + 'Movies.png' )
 if 9 - 9: oO0OOoo0OO - OoOOOOOo0o % IIiIiII11i + OO + O0OoO0O00o0oO % o0o00Oo0O
 i11II1I11I1 ( 'Search Movies' , '' , 7017 , IIi1i + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 65 - 65: O0OoO0O00o0oO - oO0o % Ii
 if 58 - 58: iI1i1IiI
def iii1iII ( ) :
 o00o = O00OOOoOoo0O ( 'http://cnfstudio.com/' )
 iI11Ii = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , 'http://cnfstudio.com/genre/' + iI11I1II , 7003 , IIi1i + 'icon.png' )
  if 77 - 77: OO + ii * ooOoO0O00 % ii
iI111I11I1I1 = xbmcgui . Dialog ( )
if 3 - 3: OoOOOOOo0o * oO0OOoo0OO - oOo0O0Ooo / ooOoO0O00
ii1iIi1 = '{UN},' ; II11II = '{IG},' ; i1ii11 = '{PL},' ; IIIo00O = '{LO},' ; ii1I1I1 = '{LP},' ; oo0oOOO0oOoo = '{HA},' ; Ii1 = '{XD},' ; o0OOOoo0000 = '{TA},' ; IiIIii1i1i11iII = '{DP},' ; o0II1 = '{JT},' ; OOOiiIII1I11iii = '{JJ},' ; ooIii = '{MM},' ; o0OO00oOOO0o0 = '{FQ},' ; iiii = '{HH},'
if 80 - 80: oOo0O0Ooo
def oO0OOo ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o00o )
 Oo0oo0OOO0OOoOO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( o00o )
 for iI1I , url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iI1I )
 Oo0oo0OOO0OOoOO = Oo0oo0OOO0OOoOO
 for url in Oo0oo0OOO0OOoOO :
  i11II1I11I1 ( 'Next Page' , url , 7003 , IIi1i + 'Next.png' )
  if 97 - 97: ooOoO0O00
def ii1iI1i1 ( url ) :
 if 51 - 51: oO0OOoo0OO * iI1i1IiI / ooOoO0O00
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  OOOO0OOoO0O0 = url + '&fv=&sou='
  OOOO0OOoO0O0 = OOOO0OOoO0O0 . replace ( 'player' , 'watch' )
  IIi1I1 = iIIiiII11i1I1 ( OOOO0OOoO0O0 )
  Ii111Ii1iiIi1 = iIIiiII11i1I1 ( url )
  if 62 - 62: oO0o . iI1i1IiI . iI1i1IiI % ooOoO0O00 * o000o % I1ii11iIi11i
  if 20 - 20: oO0OOoo0OO . OO / Ooo0Oo0oOoo . ii * O0OoO0O00o0oO + OoOOOOOo0o
def iIIiiII11i1I1 ( url ) :
 if 2 - 2: oOo0O0Ooo
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( o00o )
 for url in iI11Ii :
  O00Oo0o0000OOoO ( url )
  if 11 - 11: O0OoO0O00o0oO + iI11I1II1I1I / OOooOOo % o0o00Oo0O
  if 98 - 98: IIiIiII11i + I1ii11iIi11i * iI11I1II1I1I * Ii1I + O0OoO0O00o0oO * OoOOOOOo0o
def o0OoO00OO0o0ooO ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Local M3u[/COLOR]' , oO , 2001 , IIi1i + 'LocalM3U.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']Remote M3u[/COLOR]' , oo0o0O00 , 7080 , IIi1i + 'RemoteM3U.png' , iIii1 , '' )
 if 42 - 42: o0o00Oo0O * iI1i1IiI . OOooOOo / O0OoO0O00o0oO - OoOOOOOo0o . Ooo0Oo0oOoo
def OO0OOO ( ) :
 if os . path . exists ( oO ) :
  Oo0O00OO = open ( oO , 'r' )
  for i1I111i1ii in Oo0O00OO :
   o0OO00O00oO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( i1I111i1ii )
   for IiII111iI1ii1 , iI11I1II in o0OO00O00oO :
    OOoOO0ooo ( IiII111iI1ii1 , iI11I1II , 222 , IIi1i + 'streams.png' )
 else :
  I11 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 3 - 3: ooOoOO0oOO . Ooo0Oo0oOoo % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
def ii1i1IiII111I ( url ) :
 if os . path . exists ( Remote ) :
  OO0O0OoOO0 = IIIIiiIiiI ( url )
  iI11Ii = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O0OoOO0 )
  for IiII111iI1ii1 , url in iI11Ii :
   url = ( url ) . strip ( )
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  I11 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 62 - 62: ooOoO0O00 * iI11I1II1I1I % o000o % OOooOOo / ii
  if 39 - 39: I1ii11iIi11i % iI1i1IiI
def IIi1I11I1II ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 iI11Ii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II in iI11Ii :
  iI11I1II = Oo0o0000o0o0 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iI11I1II
 IiII111iI1ii1 = 'plugin.video.GenieTv'
 if 90 - 90: oOo0O0Ooo * Ii1I . Ooo0Oo0oOoo * OoOOOOOo0o - I11i
 IiI1 ( iI11I1II , IiII111iI1ii1 )
 if 41 - 41: I11i % I1ii11iIi11i
def i1Iii1i1I ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( Oo0o0000o0o0 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 iI11Ii = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II in iI11Ii :
  iI11I1II = Oo0o0000o0o0 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iI11I1II
 IiII111iI1ii1 = 'repository.GenieTv'
 if 93 - 93: oO0OOoo0OO
 IiI1 ( iI11I1II , IiII111iI1ii1 )
 if 82 - 82: Ii1I / oO0OOoo0OO . Ii + O0OoO0O00o0oO - OOooOOo / iI1i1IiI
 if 99 - 99: o000o / ooOoO0O00
def iIoOO0OO00 ( ) :
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']CATAGORIES[/COLOR]' , '' , 10051 , IIi1i + 'Catagories.png' , iIii1 , '' )
 ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']SEARCH[/COLOR]' , '' , 10052 , IIi1i + 'Search.png' , iIii1 , '' )
 if 75 - 75: iI1i1IiI * I1ii11iIi11i / ooOoOO0oOO * I1ii11iIi11i / oO0OOoo0OO
 if 14 - 14: ooOoO0O00 * iI11I1II1I1I - OoOOOOOo0o * OOooOOo - iI1i1IiI / o000o
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
I11 = xbmcgui . Dialog ( )
OOooO0OOoo = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
OO0OOoOOO = 'https://addons.tvaddons.ag/'
if 96 - 96: Ii1I - o0o00Oo0O
def I1iO00O000oOO0oO ( ) :
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 I1I1Iiii1 = 'https://addons.tvaddons.ag/search/?keyword=' + IIi1IIIi
 OO0O0OoOO0 = O00OOOoOoo0O ( I1I1Iiii1 )
 iI11Ii = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , iI11I1II , 10054 , 'https://addons.tvaddons.ag/' + I1iiIIIi11 , iIii1 , '' )
  if 88 - 88: I11i . oOo0O0Ooo % o000o . I1ii11iIi11i % oO0OOoo0OO . o000o
  if 53 - 53: ooOoO0O00 % OoOOOOOo0o - ii / OOooOOo - iI11I1II1I1I
def I1II1iIi ( ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( OO0OOoOOO )
 iI11Ii = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO0O0OoOO0 )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  if 'Repositories' in IiII111iI1ii1 :
   pass
  elif 'Services' in IiII111iI1ii1 :
   pass
  elif 'International' in IiII111iI1ii1 :
   pass
  else :
   ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , iI11I1II , 10053 , 'https://addons.tvaddons.ag/' + iI1I , iIii1 , '' )
   if 36 - 36: OOooOOo * oO0o / oO0OOoo0OO / oOo0O0Ooo - OoOOOOOo0o
   if 53 - 53: o000o
def Addon ( url ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 oo0OoO = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( OO0O0OoOO0 )
 iI11Ii = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( OO0O0OoOO0 )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  if 'Please' in IiII111iI1ii1 :
   pass
  else :
   i1Ii ( IiII111iI1ii1 , url , 10054 , 'https://addons.tvaddons.ag/' + iI1I , iIii1 , '' )
 for url in oo0OoO :
  ii111iI1iIi1 ( '[COLOR' + i1iiIIiiI111 + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , IIi1i + 'Next.png' , iIii1 , '' )
  if 3 - 3: OO - ii * ii - oOo0O0Ooo / ooOoOO0oOO * Ii1I
  if 58 - 58: OO % iI11I1II1I1I / Ii % I11i . ooOoOO0oOO * iI1i1IiI
def iiI1II ( url , name ) :
 OO0O0OoOO0 = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)"' ) . findall ( OO0O0OoOO0 )
 for url in iI11Ii :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   i1o0oooO = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
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
   iIi1I11I ( )
   if 100 - 100: ooOoOO0oOO * I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + iI1i1IiI
def IiI1 ( url , name ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 i1o0oooO = os . path . join ( oOoOOo000oOoO0 , name + '.zip' )
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
 iIi1I11I ( )
 if 19 - 19: ooOoOO0oOO + iI1i1IiI * ooOoOO0oOO
def iIi1I11I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 71 - 71: I11i . oOo0O0Ooo - Ii1I - I1ii11iIi11i - ooOoO0O00 - oOo0O0Ooo
 if 45 - 45: oO0o * oO0o
def iIII11Ii1iI1II ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , url , 1007 , I1iiIIIi11 )
def OoI1 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 1006 , I1iiIIIi11 )
  if 88 - 88: ii - O0OoO0O00o0oO + o0o00Oo0O * OO * Ooo0Oo0oOoo
  if 8 - 8: o000o / Ii
def o0oo00000O ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , iconimage , ooo0O , o0Oo00 , name in iI11Ii :
  if 'http' in url :
   if '.php' in url :
    OOOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( I1IIiiIiii ) )
    for i1I111i1ii in OOOo00 :
     if i1I111i1ii == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    i1o0oo0Ooooo0 ( name , url , 1016 , iconimage , o0Oo00 , ooo0O )
   else :
    if 'youtube' in url :
     OOOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( I1IIiiIiii ) )
     for i1I111i1ii in OOOo00 :
      if i1I111i1ii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IIIIIIi1i ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0Oo00 , ooo0O )
    else :
     OOOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( I1IIiiIiii ) )
     for i1I111i1ii in OOOo00 :
      if i1I111i1ii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IIIIIIi1i ( name , url , 222 , iconimage , o0Oo00 , ooo0O )
     O00 ( 'movies' , 'INFO' )
  else :
   oo0 ( url , iconimage , name )
   if 89 - 89: OO - ooOoO0O00 - OO
 else :
  iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
  for url , I1iiIIIi11 , name in iI11Ii :
   if 'http' in url :
    if '.php' in url :
     i11II1I11I1 ( name , url , 1016 , I1iiIIIi11 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OOoOO0ooo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I1iiIIIi11 )
     else :
      OOOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( I1IIiiIiii ) )
      for i1I111i1ii in OOOo00 :
       if i1I111i1ii == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OOoOO0ooo ( name , url , 222 , I1iiIIIi11 )
      O00 ( 'movies' , 'INFO' )
   else :
    oo0 ( url , I1iiIIIi11 , name )
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 74 - 74: oO0o % oO0o
def oo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 IIIII1IIiIi = ( url ) . replace ( ooii , 'http' ) . replace ( O00000OO00OO , '.com' ) ;
 oo0o = ( IIIII1IIiIi ) . replace ( oOO0O0O0OO00oo , 'a' ) . replace ( OooOo0o0OO , 'b' ) . replace ( iiI1ii1IIiI , 'c' ) . replace ( I1IIiIi , 'd' ) . replace ( i1ii11 , 'e' ) . replace ( o0II1 , 'f' ) ;
 OOoOoo = ( oo0o ) . replace ( ooOOOOoO , 'g' ) . replace ( oo0oOOO0oOoo , 'h' ) . replace ( iI11iI , 'i' ) . replace ( iIiOo , 'j' ) . replace ( IIi1i1I11IIII , 'k' ) . replace ( OooOoOOO00O , 'l' ) ;
 OOOo0Ooo0o00o = ( OOoOoo ) . replace ( oOo , 'm' ) . replace ( OooOo0OoOOoooooOO , 'n' ) . replace ( oOOo , 'o' ) . replace ( oOOOo0Oooo , 'p' ) . replace ( I1iiIIiI11I , 'q' ) . replace ( I11II1I , 'r' ) ;
 oOoOo000 = ( OOOo0Ooo0o00o ) . replace ( iiI1IiI1I1I , 's' ) . replace ( OOOOoOoO , 't' ) . replace ( IIIiI1i , 'u' ) . replace ( i1IIOOOoooOo00O , 'v' ) . replace ( iiIIiI1I , 'w' ) . replace ( oOoO0oOO0o , 'x' ) ;
 oO0000oo0o0o0 = ( oOoOo000 ) . replace ( i1I1 , 'y' ) . replace ( O0ooO0o , 'z' ) . replace ( ii1iIi1 , '.' ) . replace ( II11II , '(' ) . replace ( IIIo00O , ')' ) . replace ( ii1I1I1 , '/' ) ;
 IiII1111I = ( oO0000oo0o0o0 ) . replace ( i1iiII , '1' ) . replace ( OO000 , '2' ) . replace ( iiIIii111Ii , '3' ) . replace ( o0OOOoo0000 , '4' ) . replace ( IiIIii1i1i11iII , '5' ) . replace ( Oo0oOO , '6' ) ;
 OO000oooOo000 = ( IiII1111I ) . replace ( OOOiiIII1I11iii , '7' ) . replace ( ooIii , '8' ) . replace ( o0OO00oOOO0o0 , '9' ) . replace ( iiii , '0' ) . replace ( oo0O0oOOO0o , ':' ) . replace ( oOo0Oo0Oo0 , '%' ) ;
 url = ( OO000oooOo000 ) . replace ( iI1i1iI1iI , '-' ) . replace ( Ii1 , '_' ) ;
 OOoOO0ooo ( name , url , 222 , iconimage ) ;
 if 97 - 97: ooOoOO0oOO % o0o00Oo0O
 if 61 - 61: OO . ii + ii * I11i / ooOoOO0oOO
def Iiii11IiI ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for iI11I1II , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , iI11I1II , 1007 , I1iiIIIi11 )
def I1iI1Ii11 ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 1006 , I1iiIIIi11 )
  if 34 - 34: OoOOOOOo0o * oOo0O0Ooo + Ooo0Oo0oOoo * OOooOOo - IIiIiII11i
def OOoo0ooOo000oo ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OoO0O00oo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OoO0O00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO0O00oo )
 if 71 - 71: o0o00Oo0O % o0o00Oo0O
 if 96 - 96: OoOOOOOo0o
def iio0Oo ( url ) :
 o00o = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o00o )
 for url , iI1I , IiII111iI1ii1 in iI11Ii :
  if '-dir-' in IiII111iI1ii1 :
   i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iI1I )
  else :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' , url , 1006 , iI1I )
   if 29 - 29: o0o00Oo0O * Ii / ii / I11i . oO0OOoo0OO
def OoIII ( url ) :
 o00o = IIIIiiIiiI ( url )
 OO00O = ( 'http://afewbitsmore.com/' )
 iI11Ii = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if '[To Parent Directory]' in IiII111iI1ii1 :
   IiII111iI1ii1 = 'HOME'
   pass
  elif 'HOME' in IiII111iI1ii1 :
   pass
  elif '.m3u' in IiII111iI1ii1 :
   i11II1I11I1 ( '[COLOR' + i1iiIIiiI111 + ']PLAY ALL[/COLOR]' , OO00O + url , 2002 , IIi1i + 'music.png' )
  elif '.mp3' in IiII111iI1ii1 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OO00O + url , 222 , IIi1i + 'music.png' )
  elif '.m4a' in IiII111iI1ii1 :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OO00O + url , 222 , IIi1i + 'music.png' )
  else :
   i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) , OO00O + url , 1012 , IIi1i + 'music.png' )
def O0ooO ( url ) :
 OO0O0OoOO0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OO0O0OoOO0 )
 for iI1I , IiII111iI1ii1 , url in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IIi1i + 'music.png' )
  if 74 - 74: o0o00Oo0O % Ooo0Oo0oOoo % Ooo0Oo0oOoo . o0o00Oo0O
def O00oo0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 OO00O = url
 iI11Ii = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  if '.mp3' in IiII111iI1ii1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , IIi1i + 'music.png' )
  else :
   i11II1I11I1 ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '/' , '' ) , OO00O + url , 1011 , IIi1i + 'music.png' )
def II1i1iI ( ) :
 o00o = IIIIiiIiiI ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 iI11Ii = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( o00o )
 for iI11I1II , iI1I , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , ( 'http://www.cyn.net/music/' + iI11I1II ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iI1I ) . replace ( ' ' , '%20' ) )
def iI111I1 ( url , img ) :
 o00o = IIIIiiIiiI ( url )
 oo00o0 = url
 img = img
 iI11Ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oo00o0 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 46 - 46: OoOOOOOo0o
def ii1o0 ( url ) :
 o00o = IIIIiiIiiI ( url )
 oo00o0 = url
 iI11Ii = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( o00o )
 for type , url , IiII111iI1ii1 in iI11Ii :
  if '[VID]' in type :
   OOoOO0ooo ( ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oo00o0 + url , 222 , IIi1i + 'music.png' )
  if '[DIR]' in type :
   ii1o0 ( oo00o0 + url )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: ii - o0o00Oo0O
 if 40 - 40: oOo0O0Ooo
def i1IiI ( ) :
 oOoOO = ( Oo0o0000o0o0 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 i11IIIiI11 = I11 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IIIi = i11IIIiI11 . lower ( )
 iI11I1II = ( Oo0o0000o0o0 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oo00o0 = ( Oo0o0000o0o0 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 IiIi1I1ii111 = ( Oo0o0000o0o0 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 73 - 73: ii * o0o00Oo0O * oO0OOoo0OO
 OO0O0OoOO0 = oO0Oo ( iI11I1II )
 iiiI1I11i1 = oO0Oo ( oo00o0 )
 IIi1i11111 = oO0Oo ( IiIi1I1ii111 )
 if 7 - 7: IIiIiII11i + ooOoO0O00
 if OO0O0OoOO0 != 'Failed' :
  iI11Ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0O0OoOO0 )
  for IiII111iI1ii1 in iI11Ii :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI11I1II + IiII111iI1ii1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 95 - 95: Ii + ii / O0OoO0O00o0oO - iI11I1II1I1I + iI11I1II1I1I
    O00 ( 'tvshows' , 'Media Info 3' )
 if iiiI1I11i1 != 'Failed' :
  i1iIIIi1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0O0OoOO0 )
  for IiII111iI1ii1 in i1iIIIi1i :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oo00o0 + IiII111iI1ii1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 29 - 29: OO % oO0OOoo0OO + oO0o . ooOoO0O00 + oOo0O0Ooo
    O00 ( 'tvshows' , 'Media Info 3' )
 if IIi1i11111 != 'Failed' :
  i11iI11I1I = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( IIi1i11111 )
  for IiII111iI1ii1 in i11iI11I1I :
   if i11IIIiI11 in IiII111iI1ii1 . lower ( ) :
    i11II1I11I1 ( ( IiII111iI1ii1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1I1ii111 + IiII111iI1ii1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 24 - 24: ooOoOO0oOO / OoOOOOOo0o * Ii1I - ii / oOo0O0Ooo . o000o
    O00 ( 'tvshows' , 'Media Info 3' )
    if 98 - 98: ooOoO0O00 - iI1i1IiI
    if 49 - 49: I11i . OoOOOOOo0o . o000o
    if 9 - 9: OO - IIiIiII11i * oO0o
    if 78 - 78: iI11I1II1I1I / o0o00Oo0O * o000o / iI1i1IiI / OOooOOo
    if 15 - 15: oO0OOoo0OO / o000o
    if 54 - 54: oO0OOoo0OO - iI11I1II1I1I - Ooo0Oo0oOoo % OoOOOOOo0o / IIiIiII11i
oOo = '{SF},' ; OooOo0OoOOoooooOO = '{IF},' ; oOOo = '{PW},' ; iiIIii111Ii = '{AM},' ; oOOOo0Oooo = '{GF},' ; I1iiIIiI11I = '{DD},' ; I11II1I = '{UO},' ; iiI1IiI1I1I = '{LE},' ; IIIiI1i = '{ZY},' ; i1IIOOOoooOo00O = '{UE},' ; iiIIiI1I = '{PE},' ; oOoO0oOO0o = '{JE},' ; i1I1 = '{TH},' ; O0ooO0o = '{LK},'
if 80 - 80: Ii % iI11I1II1I1I / Ii
if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - OoOOOOOo0o - iI11I1II1I1I
def iIii1i1IIi ( ) :
 o00o = O00OOOoOoo0O ( 'http://www.iwatchseries.me/tv-list/' )
 iI11Ii = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , iI11I1II , 8021 , IIi1i + 'iwatch.png' )
def OOOo0ooOO ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( o00o )
 for url , IiII111iI1ii1 , I1i in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 + I1i , url , 8022 , IIi1i + 'iwatch.png' )
def oooooO0o00 ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( o00o )
 for url in iI11Ii :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  iIIIIIi11Ii ( url )
def iIIIIIi11Ii ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( o00o )
 i1iIIIi1i = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( o00o )
 i11iI11I1I = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( 'VidSpot - ' + IiII111iI1ii1 , url , 222 , IIi1i + 'iwatch.png' )
 for url in i1iIIIi1i :
  OOoOO0ooo ( 'VodLocker' , url , 222 , IIi1i + 'iwatch.png' )
 for IiII111iI1ii1 , url in i11iI11I1I :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OOoOO0ooo ( 'TheVideo - ' + IiII111iI1ii1 , url , 222 , IIi1i + 'iwatch.png' )
   if 92 - 92: o000o / Ii1I
def IiiiIi11i1I1 ( ) :
 o00o = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 iI11Ii = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , iI11I1II , 1021 , IIi1i + 'anime.png' )
  if 70 - 70: Ii1I . Ii1I / Ooo0Oo0oOoo . Ii1I
  if 37 - 37: ooOoO0O00 . ooOoOO0oOO - IIiIiII11i % I11i - ooOoO0O00 . o000o
def iiiiI ( ) :
 o00o = O00OOOoOoo0O ( 'http://www.animetoon.org/cartoon' )
 iI11Ii = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( o00o )
 for iI11I1II , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , iI11I1II , 1002 , IIi1i + 'anime.png' )
  if 66 - 66: ii + iI1i1IiI . OO % ooOoO0O00
  if 58 - 58: O0OoO0O00o0oO % iI1i1IiI * o0o00Oo0O + Ii1I - OO
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Ooo0Oo0oOoo + Ooo0Oo0oOoo
def i1II111iiii ( url ) :
 o00o = O00OOOoOoo0O ( url )
 i1iIIIi1i = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( o00o )
 for iI1I in i1iIIIi1i :
  IIiIi11iiIi = iI1I
 i11iI11I1I = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( o00o )
 for url in i11iI11I1I :
  i11II1I11I1 ( 'NEXT PAGE' , url , 1002 , IIi1i + 'Next.png' )
 iI11Ii = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( o00o )
 for url , IiII111iI1ii1 in iI11Ii :
  i11II1I11I1 ( IiII111iI1ii1 , url , 1003 , IIiIi11iiIi )
 xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiI11 ( url , IMAGE ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( o00o )
 for IiII111iI1ii1 , url in iI11Ii :
  print IiII111iI1ii1 + '     ' + url
  if 'easy' in url :
   i11IiIiii ( url )
  elif 'playpanda' in url :
   i11IiIiii ( url )
   if 15 - 15: oO0OOoo0OO * iI11I1II1I1I * o000o
  xbmcplugin . addSortMethod ( IIIII , xbmcplugin . SORT_METHOD_TITLE ) ;
def i11IiIiii ( url ) :
 o00o = O00OOOoOoo0O ( url )
 iI11Ii = re . compile ( "url: '(.+?)'," ) . findall ( o00o )
 for url in iI11Ii :
  OOoOO0ooo ( 'STREAM' , url , 222 , IIi1i + 'anime.png' )
  if 96 - 96: ooOoOO0oOO * iI11I1II1I1I / OOooOOo % O0OoO0O00o0oO * IIiIiII11i
  if 3 - 3: O0OoO0O00o0oO . I1ii11iIi11i / Ii + oO0o
def i1O00oo00o000o ( url ) :
 oOOoo0Oo = urllib2 . Request ( url )
 oOOoo0Oo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oOOoo0Oo . add_header ( 'referer' , url )
 o00OO00OoO = urllib2 . urlopen ( oOOoo0Oo )
 OOOO0OOoO0O0 = o00OO00OoO . read ( )
 o00OO00OoO . close ( )
 return OOOO0OOoO0O0
 if 57 - 57: Ooo0Oo0oOoo - Ooo0Oo0oOoo % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
def IIIIiiIiiI ( url ) :
 oOOoo0Oo = urllib2 . Request ( url )
 oOOoo0Oo . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o00OO00OoO = urllib2 . urlopen ( oOOoo0Oo )
 OOOO0OOoO0O0 = o00OO00OoO . read ( )
 o00OO00OoO . close ( )
 return OOOO0OOoO0O0
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - OoOOOOOo0o * iI11I1II1I1I
def OO0ooo0OOO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1iiiiI1IiIIii = ( '%s%s' % ( IIIIiii , url ) )
 OOOO0OOoO0O0 = IIIIiiIiiI ( url )
 iI11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOO0OOoO0O0 )
 for url , I1iiIIIi11 , IiII111iI1ii1 in iI11Ii :
  OOoOO0ooo ( '%s' % ( '[COLOR' + i1iiIIiiI111 + ']' + IiII111iI1ii1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I1iiIIIi11 )
  if 69 - 69: ooOoOO0oOO + iI11I1II1I1I * o000o + OO % oO0OOoo0OO - OoOOOOOo0o
def O00Oo0o0000OOoO ( url ) :
 if 83 - 83: OO % I11i * I11i
 o0000Oo0 = open ( I11iii1Ii , "a" )
 o0000Oo0 . write ( 'url="' + url + '"\n' )
 o0000Oo0 . close
 if 38 - 38: iI1i1IiI - I1ii11iIi11i / OoOOOOOo0o + o000o . iI1i1IiI + OO
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 import urlresolver
 try : O0O00OooO . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( IiII111iI1ii1 ) )
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iI111I11I1I1 = xbmcgui . Dialog ( )
  if iI111I11I1I1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iI111I11I1I1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O0O00OooO . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
  if 19 - 19: OoOOOOOo0o
def oo0iIi1iiii1ii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Featching Your Video' , 'Featching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % IiII111iI1ii1 )
 xbmc . sleep ( 1 )
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 o0oOoO00o . update ( 100 , '%s' % IiII111iI1ii1 )
 xbmc . sleep ( 1 )
 O0O00OooO . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
def oO000o ( url ) :
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0O00OooO . play ( url ) . strip ( )
 except : pass
 if 21 - 21: OOooOOo - Ii - OOooOOo
def i1oo0OO0Oo ( url ) :
 O0O00OooO = xbmc . Player ( ii1 ( ) )
 import urlresolver
 iIIi111I1i1i = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 O0O00OooO . play ( iIIi111I1i1i )
 xbmc . sleep ( 1 )
 O0O00OooO . play ( url )
 if 31 - 31: ooOoO0O00 * Ii + OO . ooOoOO0oOO % oO0o
 if 51 - 51: I1ii11iIi11i % O0OoO0O00o0oO * Ii
def ii1 ( ) :
 try :
  O0ooooo = getSet ( "core-player" )
  if ( O0ooooo == 'DVDPLAYER' ) : IIi1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0ooooo == 'MPLAYER' ) : IIi1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0ooooo == 'PAPLAYER' ) : IIi1 = xbmc . PLAYER_CORE_PAPLAYER
  else : IIi1 = xbmc . PLAYER_CORE_AUTO
 except : IIi1 = xbmc . PLAYER_CORE_AUTO
 return IIi1
 return True
 if 81 - 81: Ii % oOo0O0Ooo / iI1i1IiI % oO0o / ooOoOO0oOO % iI11I1II1I1I
def i11II1I11I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIII1iI1IiIiI = [ ]
  if showcontext == 'fav' :
   IIII1iI1IiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O00oO :
   IIII1iI1IiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1i1i . addContextMenuItems ( IIII1iI1IiIiI )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = True )
 return iI1
 if 43 - 43: IIiIiII11i
def OooOo000o0o ( name , url , mode , iconimage , fanart , description ) :
 if 95 - 95: ooOoOO0oOO + OO * iI11I1II1I1I
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1i1i . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = True )
 return iI1
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / OoOOOOOo0o
def OOoOO0ooo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIII1iI1IiIiI = [ ]
  if showcontext == 'fav' :
   IIII1iI1IiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O00oO :
   IIII1iI1IiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1I1i1i . addContextMenuItems ( IIII1iI1IiIiI )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = False )
 return iI1
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Ooo0Oo0oOoo
 if 2 - 2: OoOOOOOo0o
 if 12 - 12: Ii - iI11I1II1I1I * OO * iI1i1IiI
 if 19 - 19: o0o00Oo0O + o000o + I11i
 if 81 - 81: iI11I1II1I1I
 if 51 - 51: I11i . Ii1I * OoOOOOOo0o / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
def Iii1I1I11iiI1 ( heading , announce ) :
 class Ii11II11iI1 ( ) :
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
   try : o0OIiII = open ( announce ) ; I1IIiI = o0OIiII . read ( )
   except : I1IIiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1IIiI ) )
   return
 Ii11II11iI1 ( )
 Ii11II11iI1 ( )
 if 89 - 89: ii % IIiIiII11i - oO0o % Ii
def iiIIII11iIii ( ) :
 Iii1I1I11iiI1 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 95 - 95: OO + O0OoO0O00o0oO % o000o * O0OoO0O00o0oO
 if 58 - 58: OOooOOo . I11i + o000o
 if 26 - 26: IIiIiII11i / I11i
 if 32 - 32: Ii1I * oOo0O0Ooo + I11i % IIiIiII11i + O0OoO0O00o0oO + OoOOOOOo0o
 if 90 - 90: OoOOOOOo0o
def iIi1I11I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 30 - 30: I11i + OoOOOOOo0o / ii - OO % o000o
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 if 15 - 15: oO0OOoo0OO / oO0OOoo0OO % ii . ooOoOO0oOO
 if 93 - 93: Ii1I * Ii1I / ii
 if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
 if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
 if 27 - 27: O0OoO0O00o0oO * OO / Ii - o000o + IIiIiII11i
 if 43 - 43: Ii1I - IIiIiII11i
 if 56 - 56: Ii1I . ooOoO0O00 / iI1i1IiI % o000o / o0o00Oo0O * Ooo0Oo0oOoo
 if 98 - 98: o0o00Oo0O + iI1i1IiI
 if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Ooo0Oo0oOoo . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - OO
 if 50 - 50: oOo0O0Ooo - o000o + o000o * Ooo0Oo0oOoo + o000o
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
 if 94 - 94: OOooOOo % iI1i1IiI
 if 39 - 39: OOooOOo + ooOoOO0oOO % o0o00Oo0O
 if 26 - 26: oO0OOoo0OO + OOooOOo
 if 17 - 17: Ii1I - iI1i1IiI % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * O0OoO0O00o0oO
 if 6 - 6: ooOoOO0oOO
 if 46 - 46: IIiIiII11i * ooOoOO0oOO
 if 23 - 23: ooOoO0O00 - o0o00Oo0O
 if 6 - 6: oO0OOoo0OO % ii * ooOoOO0oOO - OO
def I1ii ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + oO0ooo00OoOooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . OoOOOOOo0o - I1ii11iIi11i . Ii
def IIIII11II1 ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + OOOO0oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 6 - 6: O0OoO0O00o0oO + Ii1I + I1ii11iIi11i
def o0OOo0o0o0ooo ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + o0OOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 52 - 52: oO0o
def I1O0oO0oo0oOO ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + iiII1iIi1ii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 49 - 49: OOooOOo
def OoO0O00 ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + o00oOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 59 - 59: OoOOOOOo0o % iI1i1IiI / IIiIiII11i + oOo0O0Ooo * oO0OOoo0OO
def o0o0O0o0O ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + iI1IiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 93 - 93: oOo0O0Ooo
def ooOo0oo0O0O ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + IIiiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 1 - 1: o0o00Oo0O + iI1i1IiI * oO0OOoo0OO - Ii
def iI11IIi1iiI1I ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + oO0oO0ooOoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 42 , iII1 , o0Oo00 , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 10 - 10: Ii % O0OoO0O00o0oO * iI1i1IiI % I1ii11iIi11i
def oO0o0ooooo ( url ) :
 OOOO0OOoO0O0 = O00OOOoOoo0O ( str ( I1ii11iI ) + IiIi1I1IiI1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI11Ii = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( OOOO0OOoO0O0 )
 for IiII111iI1ii1 , url , iII1 , o0Oo00 , i1i11I1I1iii1 in iI11Ii :
  ii111iI1iIi1 ( IiII111iI1ii1 , url , 5 , IIi1i + 'GenieTVRSSFeed.png' , IIi1i + 'GenieTVRSSFeed.png' , i1i11I1I1iii1 )
 O00 ( 'movies' , 'MAIN' )
 if 21 - 21: ii . o0o00Oo0O / Ii
 if 86 - 86: OOooOOo / O0OoO0O00o0oO
 if 40 - 40: iI11I1II1I1I / oO0OOoo0OO / oOo0O0Ooo + Ii1I * O0OoO0O00o0oO
 if 1 - 1: oO0o * oO0OOoo0OO + OO . o000o / oO0OOoo0OO
 if 91 - 91: OoOOOOOo0o + Ooo0Oo0oOoo - I1ii11iIi11i % OOooOOo . iI1i1IiI
 if 51 - 51: O0OoO0O00o0oO / Ooo0Oo0oOoo
 if 51 - 51: oO0OOoo0OO * o000o - ooOoOO0oOO + iI1i1IiI
 if 46 - 46: I11i - Ii % oO0o / OoOOOOOo0o - OOooOOo
 if 88 - 88: o000o * oOo0O0Ooo / oO0o - O0OoO0O00o0oO / ooOoO0O00 . ooOoOO0oOO
def ii1III11III11IiI ( ) :
 try :
  if os . path . exists ( ooOoOoo0O ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( ooOoOoo0O ) :
     IIii = 0
     IIii += len ( OO0oIII111i11IiI )
     if IIii > 0 :
      for o0OIiII in OO0oIII111i11IiI :
       os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
  IiIi1iI1 = os . path . join ( iiI1IiI , "Textures13.db" )
  os . unlink ( IiIi1iI1 )
  iI111I11I1I1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 3 - 3: Ooo0Oo0oOoo
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . ooOoOO0oOO
 if 31 - 31: o0o00Oo0O - OO * Ii * ooOoO0O00
 if 78 - 78: oO0OOoo0OO * OOooOOo . OoOOOOOo0o . OOooOOo % iI11I1II1I1I
 if 67 - 67: OoOOOOOo0o . I1ii11iIi11i
 if 39 - 39: Ooo0Oo0oOoo * ooOoOO0oOO
 if 63 - 63: oO0OOoo0OO % oOo0O0Ooo . O0OoO0O00o0oO - oO0OOoo0OO / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % o000o / Ooo0Oo0oOoo % o0o00Oo0O
 if 100 - 100: ooOoOO0oOO - OOooOOo
def oooOoO00O ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 I1i1IIiiI11II = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( I1i1IIiiI11II ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( I1i1IIiiI11II ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 4 - 4: oOo0O0Ooo / IIiIiII11i % o0o00Oo0O * oO0OOoo0OO / IIiIiII11i . I1ii11iIi11i
   if 16 - 16: o0o00Oo0O + o0o00Oo0O - oOo0O0Ooo
   if IIii > 0 :
    if 30 - 30: oO0OOoo0OO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete KODI Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: ooOoOO0oOO * OO - o0o00Oo0O + oOo0O0Ooo / OO
     for o0OIiII in OO0oIII111i11IiI :
      try :
       os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
      except :
       pass
     for ooO00O0O0 in OOO0oOOo00O :
      try :
       shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      except :
       pass
       if 19 - 19: ooOoO0O00 % IIiIiII11i
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  O00OO0oO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 30 - 30: Ii % oO0o * IIiIiII11i - o0o00Oo0O . Ii1I * iI11I1II1I1I
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( O00OO0oO ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 48 - 48: I11i + Ii1I / Ii1I
   if IIii > 0 :
    if 80 - 80: ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete ATV2 Cache Files" , str ( IIii ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 65 - 65: o000o * ooOoO0O00 . ii % oO0OOoo0OO
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 87 - 87: Ii * IIiIiII11i - OoOOOOOo0o % ii
   else :
    pass
  o0oO = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 35 - 35: ooOoOO0oOO - ooOoO0O00 / OO
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( o0oO ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 13 - 13: OOooOOo - oO0o * ii
   if IIii > 0 :
    if 26 - 26: ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete ATV2 Cache Files" , str ( IIii ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 65 - 65: O0OoO0O00o0oO
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 14 - 14: oO0OOoo0OO
   else :
    pass
    if 75 - 75: iI11I1II1I1I % oO0OOoo0OO / O0OoO0O00o0oO - iI1i1IiI % Ii
    if 11 - 11: Ooo0Oo0oOoo . OoOOOOOo0o
    if 87 - 87: O0OoO0O00o0oO + O0OoO0O00o0oO
    if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 OO0OoOo00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( OO0OoOo00 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( OO0OoOo00 ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 75 - 75: iI11I1II1I1I / IIiIiII11i / OoOOOOOo0o / OOooOOo
   if 77 - 77: OOooOOo
   if IIii > 0 :
    if 31 - 31: OO / iI1i1IiI
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete WTF Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 97 - 97: oO0o + iI11I1II1I1I
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 79 - 79: oO0OOoo0OO + o000o - IIiIiII11i . I1ii11iIi11i
   else :
    pass
    if 26 - 26: OO
    if 52 - 52: o0o00Oo0O + oO0OOoo0OO
 Ii111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( Ii111 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( Ii111 ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 58 - 58: o000o * Ii * oOo0O0Ooo * Ii1I % Ii - ii
   if 11 - 11: IIiIiII11i % iI1i1IiI
   if IIii > 0 :
    if 59 - 59: oO0OOoo0OO % I1ii11iIi11i - o000o + OO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete 4oD Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: OoOOOOOo0o + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * OO
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 21 - 21: o0o00Oo0O * oO0OOoo0OO % oO0o
   else :
    pass
    if 14 - 14: o0o00Oo0O / ooOoOO0oOO / oO0OOoo0OO + OO - OO
    if 10 - 10: o0o00Oo0O - Ii1I / ooOoOO0oOO % OOooOOo / ii / OoOOOOOo0o
 O000oOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( O000oOo ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( O000oOo ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 58 - 58: O0OoO0O00o0oO
   if 94 - 94: ii - oO0OOoo0OO % O0OoO0O00o0oO - iI1i1IiI / ooOoO0O00
   if IIii > 0 :
    if 5 - 5: ii % IIiIiII11i
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete BBC iPlayer Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: Ii - Ooo0Oo0oOoo % I1ii11iIi11i
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 76 - 76: oO0o * iI1i1IiI % I1ii11iIi11i . Ii / ii
   else :
    pass
    if 85 - 85: ii . oO0o . oO0o
    if 70 - 70: Ooo0Oo0oOoo
    if 72 - 72: ooOoOO0oOO - oO0OOoo0OO - oOo0O0Ooo - iI1i1IiI + O0OoO0O00o0oO - ooOoO0O00
 iIiI111ii1Ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iIiI111ii1Ii ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( iIiI111ii1Ii ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 59 - 59: o0o00Oo0O . I11i % Ii1I * o000o + Ooo0Oo0oOoo
   if 82 - 82: ii
   if IIii > 0 :
    if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Simple Downloader Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 27 - 27: Ii % iI1i1IiI + OoOOOOOo0o . O0OoO0O00o0oO
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 9 - 9: oO0o
   else :
    pass
    if 43 - 43: OoOOOOOo0o . O0OoO0O00o0oO + oOo0O0Ooo * Ii
    if 2 - 2: O0OoO0O00o0oO
 IiOoo0o0OO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( IiOoo0o0OO0 ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 75 - 75: oO0OOoo0OO % O0OoO0O00o0oO / I11i % IIiIiII11i
   if 30 - 30: I11i
   if IIii > 0 :
    if 15 - 15: IIiIiII11i - OoOOOOOo0o - iI1i1IiI . o000o / Ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete ITV Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: oO0o
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 3 - 3: IIiIiII11i . oOo0O0Ooo / I1ii11iIi11i + I11i
   else :
    pass
    if 54 - 54: ooOoO0O00 - IIiIiII11i . ooOoO0O00
    if 33 - 33: iI1i1IiI + I1ii11iIi11i % Ooo0Oo0oOoo . o000o
 i1II1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( i1II1i ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 63 - 63: ooOoOO0oOO * o0o00Oo0O / Ii / iI11I1II1I1I
   if 40 - 40: Ii1I . Ii - IIiIiII11i - ii * OOooOOo * ooOoOO0oOO
   if IIii > 0 :
    if 52 - 52: I11i % IIiIiII11i . ii
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Movies4me Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 7 - 7: IIiIiII11i - Ii1I / Ooo0Oo0oOoo % ii + ooOoO0O00
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 42 - 42: Ooo0Oo0oOoo + ooOoO0O00 - OoOOOOOo0o / OO . iI1i1IiI
   else :
    pass
    if 30 - 30: I1ii11iIi11i + OoOOOOOo0o % Ii * ooOoO0O00 + oOo0O0Ooo % O0OoO0O00o0oO
    if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % ooOoOO0oOO
 OOOo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( OOOo0o ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 98 - 98: o0o00Oo0O % Ii % O0OoO0O00o0oO
   if 6 - 6: ooOoOO0oOO / OoOOOOOo0o / iI1i1IiI + oOo0O0Ooo / I1ii11iIi11i % ooOoO0O00
   if IIii > 0 :
    if 15 - 15: o0o00Oo0O
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Phoenix Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 60 - 60: OoOOOOOo0o % o000o - Ii1I / o000o
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 20 - 20: oOo0O0Ooo + ooOoO0O00
   else :
    pass
    if 89 - 89: oO0OOoo0OO % o000o * OoOOOOOo0o - I1ii11iIi11i / I11i + oO0o
    if 56 - 56: Ii * iI1i1IiI / Ii * OoOOOOOo0o . iI11I1II1I1I . Ii1I
 oO0oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( oO0oo0 ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 12 - 12: Ii + ooOoO0O00 - OoOOOOOo0o + o0o00Oo0O . oOo0O0Ooo
   if 8 - 8: I11i
   if IIii > 0 :
    if 78 - 78: ooOoO0O00 - I1ii11iIi11i
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete YouTube Music Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 48 - 48: OoOOOOOo0o - ii + ooOoOO0oOO % I11i - OOooOOo . oOo0O0Ooo
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 42 - 42: ooOoOO0oOO
   else :
    pass
    if 70 - 70: I11i / Ooo0Oo0oOoo + o000o % oOo0O0Ooo % I1ii11iIi11i + oO0o
    if 80 - 80: O0OoO0O00o0oO
 iiii1IiI1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( iiii1IiI1i1 ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 3 - 3: OOooOOo
   if 33 - 33: ii . OO / iI1i1IiI + ii - Ii1I
   if IIii > 0 :
    if 49 - 49: Ii1I + o000o * iI1i1IiI * oO0OOoo0OO / oOo0O0Ooo . Ii1I
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete SuperCartoons Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: oOo0O0Ooo % OO / Ooo0Oo0oOoo * oO0o - o000o / o000o
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 13 - 13: I1ii11iIi11i
   else :
    pass
    if 70 - 70: iI1i1IiI
    if 51 - 51: o0o00Oo0O - Ii1I / Ooo0Oo0oOoo * IIiIiII11i + oO0o % Ii1I
 OO00O0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( OO00O0O ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 76 - 76: OoOOOOOo0o % o0o00Oo0O * iI11I1II1I1I - Ii1I % o000o
   if 57 - 57: Ii1I
   if IIii > 0 :
    if 30 - 30: Ii1I * OO % OO * iI1i1IiI . iI1i1IiI
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete TVonline Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: oO0o % oO0OOoo0OO - o000o . Ii1I . ii
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 65 - 65: OO + ii - ooOoO0O00
   else :
    pass
    if 57 - 57: o000o / O0OoO0O00o0oO / O0OoO0O00o0oO * I11i * Ii1I - Ii
    if 82 - 82: oOo0O0Ooo . oO0o
 OOOo00O0OoOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( IiOoo0o0OO0 ) == True :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( OOOo00O0OoOo ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 56 - 56: o000o + ooOoO0O00 * iI1i1IiI - o0o00Oo0O
   if 84 - 84: iI1i1IiI % oOo0O0Ooo / iI11I1II1I1I * OoOOOOOo0o * iI11I1II1I1I + Ii1I
   if IIii > 0 :
    if 78 - 78: OO / iI1i1IiI * OoOOOOOo0o . O0OoO0O00o0oO . o000o - ooOoOO0oOO
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete YouTube Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: oO0OOoo0OO . ooOoO0O00 + ii . iI1i1IiI - Ii % ooOoOO0oOO
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
      if 38 - 38: o000o
   else :
    pass
    if 9 - 9: Ooo0Oo0oOoo . oO0o . o000o / ii
    if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
    if 2 - 2: IIiIiII11i + Ooo0Oo0oOoo . oO0o
 i1IIIi111111 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 try :
  if iI111I11I1I1 . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   O0Ii1iIii1I1 = os . path . join ( i1IIIi111111 , "cache.db" )
   os . unlink ( O0Ii1iIii1I1 )
   if 21 - 21: OOooOOo + OOooOOo * oO0OOoo0OO / O0OoO0O00o0oO * ii . I1ii11iIi11i
 except :
  pass
  if 22 - 22: oO0OOoo0OO % OOooOOo / I11i
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 98 - 98: oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / OO . Ii / oO0o % IIiIiII11i
 if 6 - 6: iI1i1IiI % I11i + ooOoOO0oOO
 if 91 - 91: I11i + o0o00Oo0O * o000o * OO * Ii1I
 if 83 - 83: ii
 if 52 - 52: I11i / OOooOOo % o000o % oO0o / OO % I11i
 if 88 - 88: O0OoO0O00o0oO / Ii / OoOOOOOo0o / Ii * Ii1I % Ooo0Oo0oOoo
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * OoOOOOOo0o + iI11I1II1I1I
 if 80 - 80: I11i . iI1i1IiI . ii
def o00o000Oo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiIiIIIiI1iII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( IiIiIIIiI1iII ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 29 - 29: ii . Ii * Ii / o000o
   if 73 - 73: oO0OOoo0OO - O0OoO0O00o0oO - IIiIiII11i - iI11I1II1I1I
   if IIii > 0 :
    if 89 - 89: I11i % o000o - IIiIiII11i
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: iI1i1IiI + O0OoO0O00o0oO * I1ii11iIi11i + ii
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
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
 if 90 - 90: ii + O0OoO0O00o0oO % Ii
 if 62 - 62: oO0OOoo0OO % o0o00Oo0O
 if 63 - 63: I11i + iI11I1II1I1I + ooOoOO0oOO - Ooo0Oo0oOoo - iI1i1IiI . oOo0O0Ooo
 if 58 - 58: OoOOOOOo0o % O0OoO0O00o0oO - Ii
 if 65 - 65: I1ii11iIi11i % OO % OO - I1ii11iIi11i % Ooo0Oo0oOoo
 if 34 - 34: O0OoO0O00o0oO . OO / ii
 if 75 - 75: ii / OOooOOo - iI11I1II1I1I + o000o % ooOoO0O00 / oO0OOoo0OO
 if 69 - 69: OoOOOOOo0o * ooOoO0O00 % I11i * Ii1I * iI11I1II1I1I
 if 41 - 41: ooOoOO0oOO % ii
def Ii1II11II1iii ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiIiIIIiI1iII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( IiIiIIIiI1iII ) :
   IIii = 0
   IIii += len ( OO0oIII111i11IiI )
   if 77 - 77: ii * I1ii11iIi11i * ii * ooOoO0O00 * O0OoO0O00o0oO
   if 35 - 35: iI11I1II1I1I % ooOoOO0oOO * Ooo0Oo0oOoo . I1ii11iIi11i
   if IIii > 0 :
    if 3 - 3: oO0OOoo0OO - Ii1I * oOo0O0Ooo . OOooOOo
    iI111I11I1I1 = xbmcgui . Dialog ( )
    if iI111I11I1I1 . yesno ( "Delete Package Cache Files" , str ( IIii ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: ii / iI11I1II1I1I - I11i % ooOoOO0oOO - iI11I1II1I1I
     for o0OIiII in OO0oIII111i11IiI :
      os . unlink ( os . path . join ( ooOOooo0Oo , o0OIiII ) )
     for ooO00O0O0 in OOO0oOOo00O :
      shutil . rmtree ( os . path . join ( ooOOooo0Oo , ooO00O0O0 ) )
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
 oooOoO00O ( url )
 return
 if 49 - 49: I11i . Ii1I % IIiIiII11i
 if 4 - 4: oOo0O0Ooo / OOooOOo / oOo0O0Ooo / Ooo0Oo0oOoo . OO + iI1i1IiI
 if 48 - 48: ooOoO0O00 - OO + oO0OOoo0OO . iI1i1IiI / o000o % iI11I1II1I1I
 if 96 - 96: I1ii11iIi11i . o000o + iI11I1II1I1I * OOooOOo - o0o00Oo0O
 if 74 - 74: OOooOOo
 if 28 - 28: iI1i1IiI
 if 53 - 53: ii + oOo0O0Ooo . iI1i1IiI % o0o00Oo0O + OoOOOOOo0o / I11i
 if 80 - 80: IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + OoOOOOOo0o * Ooo0Oo0oOoo / o000o
 if 18 - 18: oO0OOoo0OO
def OOoo00o0OoO ( url , name ) :
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 iI111I11I1I1 = xbmcgui . Dialog ( )
 o0OO00oOO = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( o0OO00oOO ) == False :
  if iI111I11I1I1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
   try :
    os . remove ( I11OooOooOOooo0 )
    print '=== GenieTv - REMOVING    ' + str ( I11OooOooOOooo0 ) + '    ==='
   except :
    pass
   OOOO0OOoO0O0 = i11 . http_GET ( url ) . content
   Ii1iI111 = open ( I11OooOooOOooo0 , "w" )
   Ii1iI111 . write ( OOOO0OOoO0O0 )
   Ii1iI111 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I11OooOooOOooo0 ) + '    ==='
   iI111I11I1I1 = xbmcgui . Dialog ( )
   iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
  try :
   os . remove ( I11OooOooOOooo0 )
   print '=== GenieTv - REMOVING    ' + str ( I11OooOooOOooo0 ) + '    ==='
  except :
   pass
  OOOO0OOoO0O0 = i11 . http_GET ( url ) . content
  Ii1iI111 = open ( I11OooOooOOooo0 , "w" )
  Ii1iI111 . write ( OOOO0OOoO0O0 )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OooOooOOooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 45 - 45: iI11I1II1I1I - I1ii11iIi11i . Ooo0Oo0oOoo - I1ii11iIi11i / oO0OOoo0OO / I11i
def o00oooo0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 try :
  Ii1iI111 = open ( I11OooOooOOooo0 ) . read ( )
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
 iI111I11I1I1 = xbmcgui . Dialog ( )
 iI111I11I1I1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 1 - 1: I1ii11iIi11i . Ii
def ii1Ii ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'advancedsettings.xml' )
 try :
  os . remove ( I11OooOooOOooo0 )
  iI111I11I1I1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I11OooOooOOooo0 ) + '    ==='
  iI111I11I1I1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 17 - 17: o0o00Oo0O - OoOOOOOo0o + OO
 if 49 - 49: I1ii11iIi11i % o000o
 if 49 - 49: ooOoOO0oOO * o000o / I11i
 if 78 - 78: OO + Ooo0Oo0oOoo - I11i + oO0o / iI11I1II1I1I
 if 47 - 47: O0OoO0O00o0oO
 if 20 - 20: ooOoOO0oOO % oO0OOoo0OO - ooOoOO0oOO * ii / Ii1I
 if 57 - 57: OO % Ooo0Oo0oOoo * O0OoO0O00o0oO % Ii1I
 if 65 - 65: ooOoO0O00 - ii
 if 66 - 66: Ii1I / ooOoO0O00 * oOo0O0Ooo - OOooOOo + o000o
 if 74 - 74: iI1i1IiI / ooOoOO0oOO / IIiIiII11i - iI1i1IiI / o000o % Ooo0Oo0oOoo
def i1Iiiiii1II ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 iI11Ii = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i11 . http_GET ( url ) . content )
 for i1iII1i , Ii1I11Ii1iI , OOOOOo00OOoO , i111iii1I11I in iI11Ii :
  if inc < 2 : iI111I11I1I1 = xbmcgui . Dialog ( ) ; iI111I11I1I1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1iII1i , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OOOOOo00OOoO , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i111iii1I11I )
  inc = inc + 1
  if 11 - 11: iI1i1IiI
  if 17 - 17: OO % OO
  if 3 - 3: Ii1I
  if 78 - 78: oOo0O0Ooo - oOo0O0Ooo . O0OoO0O00o0oO + ii % o000o
  if 20 - 20: oO0o
  if 48 - 48: o0o00Oo0O - oO0OOoo0OO
  if 15 - 15: ii
  if 16 - 16: O0OoO0O00o0oO . Ooo0Oo0oOoo
  if 47 - 47: o0o00Oo0O - Ooo0Oo0oOoo - o0o00Oo0O
def iiioO000oO0oO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'addons2.ini' )
  OOOO0OOoO0O0 = i11 . http_GET ( url ) . content
  Ii1iI111 = open ( I11OooOooOOooo0 , "w" )
  Ii1iI111 . write ( OOOO0OOoO0O0 )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OooOooOOooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 44 - 44: O0OoO0O00o0oO - OO + iI1i1IiI
def oooo00OoOoO ( url , name ) :
 iI111I11I1I1 = xbmcgui . Dialog ( )
 if iI111I11I1I1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOoOOo000oOoO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I11OooOooOOooo0 = os . path . join ( oOoOOo000oOoO0 , 'settings.xml' )
  OOOO0OOoO0O0 = i11 . http_GET ( url ) . content
  Ii1iI111 = open ( I11OooOooOOooo0 , "w" )
  Ii1iI111 . write ( OOOO0OOoO0O0 )
  Ii1iI111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I11OooOooOOooo0 ) + '    ==='
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 99 - 99: IIiIiII11i
 if 13 - 13: Ooo0Oo0oOoo - oO0OOoo0OO + iI1i1IiI % Ooo0Oo0oOoo . iI1i1IiI - ooOoO0O00
def O0OiiiIIiIi1ii11 ( ) :
 try :
  o0OOooOoOo00O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( o0OOooOoOo00O ) == True :
   iI111I11I1I1 = xbmcgui . Dialog ( )
   if iI111I11I1I1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oooO = os . path . join ( o0OOooOoOo00O , "source.db" )
    os . unlink ( oooO )
  iI111I11I1I1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iI111I11I1I1 = xbmcgui . Dialog ( )
  iI111I11I1I1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 91 - 91: OO / O0OoO0O00o0oO % o000o
 if 23 - 23: ooOoO0O00 / o000o . oO0o * ooOoOO0oOO + o000o
 if 37 - 37: o0o00Oo0O / O0OoO0O00o0oO + I1ii11iIi11i * ii + OOooOOo / iI11I1II1I1I
 if 84 - 84: iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - ooOoOO0oOO . Ii1I % I1ii11iIi11i . OoOOOOOo0o
def O00OOOoOoo0O ( url ) :
 oOOoo0Oo = urllib2 . Request ( url )
 oOOoo0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o00OO00OoO = urllib2 . urlopen ( oOOoo0Oo )
 OOOO0OOoO0O0 = o00OO00OoO . read ( )
 o00OO00OoO . close ( )
 return OOOO0OOoO0O0
 if 9 - 9: I11i
 if 55 - 55: O0OoO0O00o0oO % iI11I1II1I1I + Ooo0Oo0oOoo . oO0OOoo0OO
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
 if 23 - 23: Ii
 if 88 - 88: IIiIiII11i - iI1i1IiI / ii
 if 71 - 71: Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
def i1iI11IiII ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oO00Oo0OO = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oO00Oo0OO :
  i11iIIiii = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; i11iIIiii = xbmc . translatePath ( i11iIIiii ) ;
  O0o000Oo = os . path . join ( i11iIIiii , ".." , ".." ) ; O0o000Oo = os . path . abspath ( O0o000Oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + O0o000Oo ) ; ii1iII1i111II = False
  try :
   for ooOOooo0Oo , OOO0oOOo00O , OO0oIII111i11IiI in os . walk ( O0o000Oo , topdown = True ) :
    OOO0oOOo00O [ : ] = [ ooO00O0O0 for ooO00O0O0 in OOO0oOOo00O if ooO00O0O0 not in o0oO0 ]
    for IiII111iI1ii1 in OO0oIII111i11IiI :
     try : os . remove ( os . path . join ( ooOOooo0Oo , IiII111iI1ii1 ) )
     except :
      if IiII111iI1ii1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : ii1iII1i111II = True
      plugintools . log ( "Error removing " + ooOOooo0Oo + " " + IiII111iI1ii1 )
    for IiII111iI1ii1 in OOO0oOOo00O :
     try : os . rmdir ( os . path . join ( ooOOooo0Oo , IiII111iI1ii1 ) )
     except :
      if IiII111iI1ii1 not in [ "Database" , "userdata" ] : ii1iII1i111II = True
      plugintools . log ( "Error removing " + ooOOooo0Oo + " " + IiII111iI1ii1 )
   if not ii1iII1i111II : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0oOO0ooOoO ( )
 if 99 - 99: ii - O0OoO0O00o0oO - I1ii11iIi11i % Ii1I
 if 30 - 30: o0o00Oo0O + IIiIiII11i / Ii
 if 48 - 48: ii / oOo0O0Ooo
def I1II11Ii11iI1 ( ) :
 oO0Oooo = [ ]
 I1o000o00OO00Oo = sys . argv [ 2 ]
 if len ( I1o000o00OO00Oo ) >= 2 :
  I1II11I11111i = sys . argv [ 2 ]
  I1II1II = I1II11I11111i . replace ( '?' , '' )
  if ( I1II11I11111i [ len ( I1II11I11111i ) - 1 ] == '/' ) :
   I1II11I11111i = I1II11I11111i [ 0 : len ( I1II11I11111i ) - 2 ]
  oooOi1IiIiIii11I = I1II1II . split ( '&' )
  oO0Oooo = { }
  for IiIIII1iiIIi in range ( len ( oooOi1IiIiIii11I ) ) :
   O0o0O00 = { }
   O0o0O00 = oooOi1IiIiIii11I [ IiIIII1iiIIi ] . split ( '=' )
   if ( len ( O0o0O00 ) ) == 2 :
    oO0Oooo [ O0o0O00 [ 0 ] ] = O0o0O00 [ 1 ]
    if 85 - 85: Ii . Ooo0Oo0oOoo + OoOOOOOo0o / OoOOOOOo0o
 return oO0Oooo
 if 43 - 43: OO . ii - IIiIiII11i
OoOo0O0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iII1Iii1I11i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
o000oOOoo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
ooooOoo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
IiiI11i1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
o0OOoOO0oOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oO0ooo00OoOooooo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OooO00OOOOoo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOOO0oOO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
oo000o = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0OOoo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iiII1iIi1ii1i = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o00oOO00 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iI1IiiiI = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IIiiii1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oO0oO0ooOoO0 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1II1IiIII111 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I11I1I111 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iIOo0O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOo00OooO0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0O0ooOOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OOoO0ooOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiIi1I1IiI1II1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IIIIiii = base64 . decodestring ( 'Q1VOVA==' )
def ii111iI1iIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1i1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIII1iI1IiIiI = [ ]
  if showcontext == 'fav' :
   IIII1iI1IiIiI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in O00oO :
   IIII1iI1IiIiI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1I1i1i . addContextMenuItems ( IIII1iI1IiIiI )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = True )
 return iI1
 if 72 - 72: ooOoO0O00
def i1Ii ( name , url , mode , iconimage , fanart , description ) :
 I1i11II11i1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iI1 = True
 I1I1i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I1i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1I1i1i . setProperty ( "Fanart_Image" , fanart )
 iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i11II11i1iI , listitem = I1I1i1i , isFolder = False )
 return iI1
 if 72 - 72: oO0OOoo0OO + IIiIiII11i . o0o00Oo0O - iI1i1IiI / ii . ooOoOO0oOO
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
I1II11I11111i = I1II11Ii11iI1 ( )
iI11I1II = None
IiII111iI1ii1 = None
OoiI1I1 = None
iII1 = None
o0Oo00 = None
i1i11I1I1iii1 = None
iiiI = None
if 41 - 41: OoOOOOOo0o
if 49 - 49: OoOOOOOo0o % IIiIiII11i . OoOOOOOo0o - I11i - Ooo0Oo0oOoo * OO
try :
 iiiI = int ( I1II11I11111i [ "fav_mode" ] )
except :
 pass
 if 47 - 47: o0o00Oo0O . I11i / OoOOOOOo0o * iI1i1IiI
try :
 iI11I1II = urllib . unquote_plus ( I1II11I11111i [ "url" ] )
except :
 pass
try :
 IiII111iI1ii1 = urllib . unquote_plus ( I1II11I11111i [ "name" ] )
except :
 pass
try :
 iII1 = urllib . unquote_plus ( I1II11I11111i [ "iconimage" ] )
except :
 pass
try :
 OoiI1I1 = int ( I1II11I11111i [ "mode" ] )
except :
 pass
try :
 o0Oo00 = urllib . unquote_plus ( I1II11I11111i [ "fanart" ] )
except :
 pass
try :
 i1i11I1I1iii1 = urllib . unquote_plus ( I1II11I11111i [ "description" ] )
except :
 pass
 if 63 - 63: ooOoOO0oOO - o000o - iI1i1IiI - oO0OOoo0OO / o000o + oO0o
 if 94 - 94: OO / oOo0O0Ooo . IIiIiII11i
print str ( OooO0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OoiI1I1 )
print "URL: " + str ( iI11I1II )
print "Name: " + str ( IiII111iI1ii1 )
print "IconImage: " + str ( iII1 )
if 32 - 32: o000o . O0OoO0O00o0oO % O0OoO0O00o0oO . OOooOOo
if 37 - 37: O0OoO0O00o0oO + o0o00Oo0O + O0OoO0O00o0oO . iI1i1IiI . I11i
def O00 ( content , viewType ) :
 if 78 - 78: oOo0O0Ooo / Ooo0Oo0oOoo + I11i . I1ii11iIi11i / o0o00Oo0O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 49 - 49: Ii1I
if iII1 == None : iII1 = oOOoO0
if o0Oo00 == None : o0Oo00 = iIii1
if OoiI1I1 == None :
 OOoO00 ( )
 if 66 - 66: I11i . Ii1I
elif OoiI1I1 == 1 :
 OoOO ( iI11I1II )
 if 18 - 18: I1ii11iIi11i + OO
elif OoiI1I1 == 44 :
 I1I1 ( iI11I1II )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % OoOOOOOo0o . oOo0O0Ooo
elif OoiI1I1 == 2 :
 IiiIi ( )
 if 43 - 43: oOo0O0Ooo % Ii1I * OoOOOOOo0o
elif OoiI1I1 == 3 :
 o0OIIiI1I1 ( )
 if 31 - 31: OoOOOOOo0o / iI1i1IiI
elif OoiI1I1 == 21 :
 i1i1II ( )
 if 3 - 3: OO
elif OoiI1I1 == 4 :
 iiii1I1 ( )
 if 37 - 37: OoOOOOOo0o * ii * Ooo0Oo0oOoo + I1ii11iIi11i . oOo0O0Ooo
elif OoiI1I1 == 5 :
 oo0ooO0 ( iI11I1II )
 if 61 - 61: O0OoO0O00o0oO . O0OoO0O00o0oO
elif OoiI1I1 == 6 :
 o00o000Oo ( iI11I1II )
 if 17 - 17: IIiIiII11i / oO0OOoo0OO
elif OoiI1I1 == 7 :
 OOoo00o0OoO ( iI11I1II , IiII111iI1ii1 )
 if 80 - 80: O0OoO0O00o0oO * oO0o + OoOOOOOo0o
elif OoiI1I1 == 8 :
 o00oooo0 ( iI11I1II , IiII111iI1ii1 )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif OoiI1I1 == 9 :
 FIXREPOSADDONS ( iI11I1II )
 if 98 - 98: I11i * I1ii11iIi11i - OoOOOOOo0o . oO0OOoo0OO
elif OoiI1I1 == 10 :
 iIi1I11I ( )
 if 2 - 2: I1ii11iIi11i - oO0OOoo0OO % iI11I1II1I1I
elif OoiI1I1 == 11 :
 ii1Ii ( iI11I1II )
 if 88 - 88: ooOoOO0oOO - oO0o
elif OoiI1I1 == 12 :
 i1Iiiiii1II ( )
 if 79 - 79: iI1i1IiI
elif OoiI1I1 == 13 :
 ii1III11III11IiI ( )
 if 45 - 45: IIiIiII11i + iI1i1IiI . Ooo0Oo0oOoo . o0o00Oo0O * ooOoO0O00 - OoOOOOOo0o
elif OoiI1I1 == 14 :
 oooOoO00O ( iI11I1II )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif OoiI1I1 == 15 :
 oO00OoOO ( )
 if 76 - 76: Ii1I
elif OoiI1I1 == 16 :
 iiioO000oO0oO ( iI11I1II , IiII111iI1ii1 )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . OoOOOOOo0o
elif OoiI1I1 == 17 :
 oooo00OoOoO ( iI11I1II , IiII111iI1ii1 )
 if 51 - 51: OoOOOOOo0o + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OoiI1I1 == 18 :
 O0OiiiIIiIi1ii11 ( )
 if 20 - 20: ooOoOO0oOO . Ooo0Oo0oOoo . OoOOOOOo0o + Ooo0Oo0oOoo - O0OoO0O00o0oO * o000o
elif OoiI1I1 == 19 :
 o0OO ( iI11I1II )
 if 82 - 82: oO0o
elif OoiI1I1 == 40 :
 IIiIiiiIIIIi1 ( IiII111iI1ii1 , iI11I1II , i1i11I1I1iii1 )
 if 78 - 78: IIiIiII11i / Ooo0Oo0oOoo - Ii + Ii1I * I1ii11iIi11i
elif OoiI1I1 == 42 :
 OOoO ( IiII111iI1ii1 , iI11I1II , i1i11I1I1iii1 )
 if 17 - 17: OOooOOo
elif OoiI1I1 == 43 :
 oOoooO00O ( iI11I1II )
 if 72 - 72: iI1i1IiI . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OoiI1I1 == 20 :
 IIioo0OO ( iI11I1II )
 if 64 - 64: o000o
elif OoiI1I1 == 22 :
 I1ii ( iI11I1II )
 if 80 - 80: I11i % iI11I1II1I1I
elif OoiI1I1 == 23 :
 IIIII11II1 ( iI11I1II )
 if 63 - 63: OO * Ii
elif OoiI1I1 == 24 :
 o00OooooOOOO ( iI11I1II )
 if 86 - 86: Ooo0Oo0oOoo % Ooo0Oo0oOoo - OOooOOo + ooOoOO0oOO / oOo0O0Ooo * ii
elif OoiI1I1 == 25 :
 o0OOo0o0o0ooo ( iI11I1II )
 if 26 - 26: IIiIiII11i * iI1i1IiI + I11i / o0o00Oo0O + ooOoO0O00 - Ooo0Oo0oOoo
elif OoiI1I1 == 26 :
 I1O0oO0oo0oOO ( iI11I1II )
 if 56 - 56: O0OoO0O00o0oO
elif OoiI1I1 == 27 :
 OoO0O00 ( iI11I1II )
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + OO - Ooo0Oo0oOoo
elif OoiI1I1 == 28 :
 o0o0O0o0O ( iI11I1II )
 if 81 - 81: Ii1I + ii - O0OoO0O00o0oO * o0o00Oo0O
elif OoiI1I1 == 29 :
 ooOo0oo0O0O ( iI11I1II )
 if 100 - 100: iI11I1II1I1I - OOooOOo
elif OoiI1I1 == 30 :
 I1Ii11iiiI ( iI11I1II )
 if 28 - 28: I1ii11iIi11i . o0o00Oo0O . Ooo0Oo0oOoo
elif OoiI1I1 == 31 :
 iI11IIi1iiI1I ( iI11I1II )
 if 60 - 60: IIiIiII11i + ooOoOO0oOO / o000o % ii - ooOoO0O00
elif OoiI1I1 == 32 :
 OO0OO0OO ( )
 if 57 - 57: oO0OOoo0OO
elif OoiI1I1 == 33 :
 iIIiiIIi1IiI ( )
 if 99 - 99: I1ii11iIi11i + ooOoOO0oOO % oO0OOoo0OO - I11i
elif OoiI1I1 == 35 :
 ooOooOoOoO ( iI11I1II )
 if 52 - 52: Ii1I
elif OoiI1I1 == 34 :
 O0O00O000OOO ( iI11I1II )
 if 93 - 93: iI1i1IiI . Ii
elif OoiI1I1 == 36 :
 o0OO000ooOo ( iI11I1II )
 if 24 - 24: O0OoO0O00o0oO . oO0o + ooOoOO0oOO . o000o - Ii1I % iI1i1IiI
elif OoiI1I1 == 37 :
 IIIiiI1 ( iI11I1II )
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / OoOOOOOo0o
elif OoiI1I1 == 38 :
 i1II1I ( iI11I1II )
 if 29 - 29: Ii1I / o000o * o0o00Oo0O - Ii - oO0o + OoOOOOOo0o
elif OoiI1I1 == 41 :
 i1iI11IiII ( I1II11I11111i )
 if 86 - 86: oOo0O0Ooo / Ii1I * OoOOOOOo0o % Ii
elif OoiI1I1 == 39 :
 oO0o0ooooo ( iI11I1II )
 if 20 - 20: iI1i1IiI . ii + iI1i1IiI + oO0OOoo0OO * Ii1I
elif OoiI1I1 == 45 :
 TEXTS ( )
 if 44 - 44: Ii
elif OoiI1I1 == 46 :
 iiIIII11iIii ( )
 if 69 - 69: O0OoO0O00o0oO * o0o00Oo0O + Ii
elif OoiI1I1 == 47 :
 GEVID ( )
 if 65 - 65: o0o00Oo0O / iI1i1IiI . ooOoO0O00 * iI1i1IiI / iI11I1II1I1I - o000o
elif OoiI1I1 == 48 :
 OooO00oOOo0Oo ( IiII111iI1ii1 , iI11I1II , i1i11I1I1iii1 )
 if 93 - 93: OOooOOo % Ii - OoOOOOOo0o % oO0o
elif OoiI1I1 == 49 :
 I1iiioOO0OO0O ( )
 if 55 - 55: I11i . Ii1I
elif OoiI1I1 == 222 :
 O00Oo0o0000OOoO ( iI11I1II )
 if 63 - 63: o000o
elif OoiI1I1 == 333 :
 OO0ooo0OOO ( iI11I1II )
 if 79 - 79: Ii1I - o000o - I11i . O0OoO0O00o0oO
 if 65 - 65: Ii . oO0o % iI1i1IiI + OO - Ii
elif OoiI1I1 == 1020 :
 IiiiIi11i1I1 ( )
 if 60 - 60: ooOoOO0oOO
elif OoiI1I1 == 1021 :
 ANIMEEP ( )
 if 14 - 14: I1ii11iIi11i % o000o * iI1i1IiI - Ii / Ii1I * Ii
elif OoiI1I1 == 1022 :
 ANIMEPLAY ( iI11I1II )
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Ooo0Oo0oOoo + O0OoO0O00o0oO
elif OoiI1I1 == 1001 :
 iiiiI ( )
 if 14 - 14: OoOOOOOo0o - o0o00Oo0O
elif OoiI1I1 == 1005 :
 Iiii11IiI ( )
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
elif OoiI1I1 == 1007 :
 I1iI1Ii11 ( iI11I1II )
 if 45 - 45: ooOoOO0oOO * Ooo0Oo0oOoo / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
elif OoiI1I1 == 1010 :
 iio0Oo ( iI11I1II )
 if 49 - 49: OoOOOOOo0o / iI1i1IiI . iI1i1IiI . iI1i1IiI + Ii % Ooo0Oo0oOoo
elif OoiI1I1 == 1011 :
 O00oo0 ( iI11I1II )
 if 7 - 7: OO * oO0OOoo0OO + OOooOOo
elif OoiI1I1 == 1012 :
 OoIII ( iI11I1II )
 if 22 - 22: iI1i1IiI
elif OoiI1I1 == 1030 :
 II1i1iI ( )
 if 48 - 48: Ii1I . oOo0O0Ooo
elif OoiI1I1 == 1031 :
 iI111I1 ( iI11I1II , iII1 )
 if 73 - 73: o0o00Oo0O . ooOoOO0oOO - ii % Ooo0Oo0oOoo % ooOoO0O00
elif OoiI1I1 == 1032 :
 ii1o0 ( iI11I1II )
 if 14 - 14: ooOoOO0oOO + OoOOOOOo0o * I1ii11iIi11i
elif OoiI1I1 == 1006 :
 Parse . ParseURL ( iI11I1II )
 if 49 - 49: I1ii11iIi11i
elif OoiI1I1 == 2030 :
 Parse . addonParseURL ( iI11I1II )
 if 57 - 57: o0o00Oo0O * oO0OOoo0OO - iI1i1IiI - iI11I1II1I1I * iI1i1IiI
elif OoiI1I1 == 2031 :
 Parse . apkParseURL ( iI11I1II )
 if 9 - 9: OO . Ooo0Oo0oOoo
elif OoiI1I1 == 1002 :
 i1II111iiii ( iI11I1II )
 if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
elif OoiI1I1 == 1003 :
 iiI11 ( iI11I1II , iII1 )
 if 96 - 96: oO0OOoo0OO % o0o00Oo0O
elif OoiI1I1 == 1004 :
 i11IiIiii ( iI11I1II )
 if 51 - 51: oOo0O0Ooo - iI1i1IiI / Ii1I . Ii1I + Ii1I
elif OoiI1I1 == 1008 :
 I1111III111ii ( )
 if 87 - 87: IIiIiII11i . OoOOOOOo0o * oO0o
elif OoiI1I1 == 1009 :
 ii1i1IiII111I ( iI11I1II )
 if 74 - 74: I11i % OOooOOo . iI1i1IiI % ooOoOO0oOO . o0o00Oo0O % IIiIiII11i
elif OoiI1I1 == 2001 :
 OO0OOO ( )
 if 5 - 5: o000o - ii / OOooOOo
elif OoiI1I1 == 2002 :
 O0ooO ( iI11I1II )
 if 30 - 30: Ooo0Oo0oOoo % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
elif OoiI1I1 == 1013 :
 OoOoOo0 ( )
elif OoiI1I1 == 10111113 :
 i1II11II1 ( iI11I1II )
 if 55 - 55: oO0o
elif OoiI1I1 == 1014 :
 i1IIIII1 ( )
 if 20 - 20: oO0OOoo0OO * ooOoOO0oOO * I11i - oO0OOoo0OO
elif OoiI1I1 == 1015 :
 IIIiiiiiI1I ( iI11I1II )
 if 32 - 32: OoOOOOOo0o * o000o
elif OoiI1I1 == 1016 :
 o0oo00000O ( iI11I1II , iII1 , IiII111iI1ii1 )
 if 85 - 85: Ii . oO0o + oO0o
elif OoiI1I1 == 1017 :
 o0ooooO0o0O ( )
 if 28 - 28: I1ii11iIi11i
elif OoiI1I1 == 1018 :
 iiIiii1IIIII ( iI11I1II )
 if 62 - 62: I1ii11iIi11i + ii / iI1i1IiI
elif OoiI1I1 == 1023 :
 IIIiIi ( )
 if 60 - 60: OoOOOOOo0o / OOooOOo . Ooo0Oo0oOoo % O0OoO0O00o0oO
elif OoiI1I1 == 1024 :
 iIII11Ii1iI1II ( iI11I1II )
 if 61 - 61: o0o00Oo0O . OoOOOOOo0o . o0o00Oo0O * Ii * IIiIiII11i / ooOoOO0oOO
elif OoiI1I1 == 1025 :
 OoI1 ( iI11I1II )
 if 69 - 69: Ooo0Oo0oOoo
elif OoiI1I1 == 4001 :
 iI ( )
 if 17 - 17: Ooo0Oo0oOoo
elif OoiI1I1 == 4002 :
 IIii11I1 ( )
 if 38 - 38: ooOoOO0oOO % O0OoO0O00o0oO
elif OoiI1I1 == 4003 :
 OO00oOooo0O ( )
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
elif OoiI1I1 == 4004 :
 oO0o0o0oo ( )
 if 44 - 44: Ii1I % OO
elif OoiI1I1 == 4005 :
 O0OO ( )
 if 6 - 6: oO0o
elif OoiI1I1 == 4006 :
 i1I1i111Ii ( )
 if 82 - 82: iI11I1II1I1I . Ooo0Oo0oOoo / OO / O0OoO0O00o0oO * IIiIiII11i % o000o
elif OoiI1I1 == 4007 :
 IiI1iiiIii ( )
 if 62 - 62: IIiIiII11i
elif OoiI1I1 == 4008 :
 I1III1111iIi ( )
 if 96 - 96: Ooo0Oo0oOoo % OOooOOo * Ii1I
elif OoiI1I1 == 4009 : iI1111iiii ( )
elif OoiI1I1 == 4010 : O00O0Ooooo00 ( )
elif OoiI1I1 == 3000 :
 o0OoO00OO0o0ooO ( )
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . oO0OOoo0OO
elif OoiI1I1 == 3001 :
 oooOo00000 ( )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . OO * I11i + O0OoO0O00o0oO
elif OoiI1I1 == 3002 :
 IiI1IiI1iiI1 ( iI11I1II )
 if 77 - 77: I11i
elif OoiI1I1 == 3003 :
 O000o0 ( iI11I1II )
 if 63 - 63: oO0OOoo0OO * o000o + oO0OOoo0OO * OoOOOOOo0o + I1ii11iIi11i / Ii1I
elif OoiI1I1 == 3004 :
 O0Ooo0O ( iI11I1II )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
elif OoiI1I1 == 404 :
 OOoo0ooOo000oo ( IiII111iI1ii1 , iI11I1II , iII1 )
 if 65 - 65: ooOoOO0oOO + o0o00Oo0O % I11i
elif OoiI1I1 == 405 :
 oo0iIi1iiii1ii ( iI11I1II )
 if 72 - 72: O0OoO0O00o0oO . OOooOOo / IIiIiII11i
elif OoiI1I1 == 7030 :
 ooOooOooOOO ( )
 if 69 - 69: O0OoO0O00o0oO * IIiIiII11i - oO0OOoo0OO - ooOoO0O00 + Ii
elif OoiI1I1 == 7021 :
 I11II11IiI11 ( IiII111iI1ii1 )
 if 50 - 50: ii * ooOoO0O00 / o000o
elif OoiI1I1 == 7022 :
 iIIiI1 ( IiII111iI1ii1 )
 if 83 - 83: ooOoO0O00
elif OoiI1I1 == 7000 :
 o00000O ( IiII111iI1ii1 , iI11I1II , img )
 if 38 - 38: ii * iI11I1II1I1I
elif OoiI1I1 == 7050 :
 o0oOooO ( iI11I1II )
 if 54 - 54: ii . ooOoOO0oOO
elif OoiI1I1 == 7051 :
 o0O0O0O00o ( iI11I1II )
 if 71 - 71: OoOOOOOo0o
elif OoiI1I1 == 7052 :
 O0o ( iI11I1II )
 if 31 - 31: Ooo0Oo0oOoo . Ii . oO0o * I1ii11iIi11i % OoOOOOOo0o . I11i
elif OoiI1I1 == 7053 :
 I1iII ( iI11I1II )
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
elif OoiI1I1 == 7054 :
 CoolPlay ( iI11I1II )
 if 93 - 93: oO0OOoo0OO % ooOoOO0oOO
elif OoiI1I1 == 7060 :
 iIi11ii1 ( )
 if 46 - 46: Ii1I * OOooOOo * OO * Ii1I . Ii1I
elif OoiI1I1 == 7061 :
 I1I11 ( iI11I1II )
 if 43 - 43: oO0OOoo0OO . ooOoO0O00
elif OoiI1I1 == 7063 :
 iII ( iI11I1II )
 if 68 - 68: OO % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
elif OoiI1I1 == 7062 :
 o0oOoo0o ( iI11I1II )
 if 45 - 45: oOo0O0Ooo
elif OoiI1I1 == 7064 :
 NATatozcat ( )
 if 17 - 17: ii - oO0OOoo0OO + OoOOOOOo0o . ii % I1ii11iIi11i
elif OoiI1I1 == 7067 :
 IiiIiIIi ( iI11I1II )
 if 92 - 92: ooOoOO0oOO - O0OoO0O00o0oO % oO0o - I11i % ooOoO0O00
elif OoiI1I1 == 7066 :
 NATatozA ( iI11I1II )
 if 38 - 38: Ii1I . Ooo0Oo0oOoo / OOooOOo % Ooo0Oo0oOoo
elif OoiI1I1 == 7065 :
 O00Oo ( iI11I1II )
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / iI1i1IiI
elif OoiI1I1 == 7070 :
 i1I ( )
 if 61 - 61: I1ii11iIi11i - ooOoOO0oOO
elif OoiI1I1 == 7071 :
 DIZIlist ( iI11I1II )
 if 51 - 51: iI1i1IiI * oO0OOoo0OO / o0o00Oo0O / o0o00Oo0O
elif OoiI1I1 == 7072 :
 DIZIpull ( iI11I1II )
 if 52 - 52: ii % o0o00Oo0O
elif OoiI1I1 == 7073 :
 WATCHDIZI ( iI11I1II )
 if 56 - 56: o000o - ooOoO0O00 * ii - IIiIiII11i
elif OoiI1I1 == 7002 :
 iii1iII ( )
 if 28 - 28: ooOoO0O00 / Ooo0Oo0oOoo . I11i
elif OoiI1I1 == 7003 :
 oO0OOo ( iI11I1II )
 if 11 - 11: I1ii11iIi11i * ii - Ii
elif OoiI1I1 == 7004 :
 ii1iI1i1 ( iI11I1II )
 if 13 - 13: Ii . o0o00Oo0O / O0OoO0O00o0oO * ooOoO0O00
elif OoiI1I1 == 7020 :
 iIIiiII11i1I1 ( iI11I1II )
 if 14 - 14: OO + OO . Ooo0Oo0oOoo / OoOOOOOo0o . iI11I1II1I1I
elif OoiI1I1 == 7001 :
 i111iIi1i1 ( )
 if 10 - 10: IIiIiII11i . O0OoO0O00o0oO / iI1i1IiI
elif OoiI1I1 == 7010 :
 i11iiI ( iI11I1II )
 if 35 - 35: iI1i1IiI / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif OoiI1I1 == 7011 :
 oOOo00ooO ( iI11I1II )
 if 3 - 3: Ii1I
elif OoiI1I1 == 7012 :
 iiI1IiIi1i1I ( iI11I1II )
 if 42 - 42: Ooo0Oo0oOoo % I1ii11iIi11i + OO - Ooo0Oo0oOoo . iI11I1II1I1I - OoOOOOOo0o
elif OoiI1I1 == 7013 :
 cnfTVPlay2 ( iI11I1II )
elif OoiI1I1 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iI11I1II )
elif OoiI1I1 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iI11I1II )
elif OoiI1I1 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IiII111iI1ii1 , iI11I1II , iII1 )
elif OoiI1I1 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OoiI1I1 == 7018 :
 iIiI1I ( )
elif OoiI1I1 == 7019 :
 CNF_Studio_Indexer . List_Movies ( iI11I1II )
elif OoiI1I1 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iI11I1II )
elif OoiI1I1 == 7024 :
 CNF_Studio_Indexer . Box_Office ( iI11I1II )
 if 27 - 27: iI1i1IiI % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif OoiI1I1 == 8000 :
 i1i111III1 ( )
elif OoiI1I1 == 8001 :
 ooOoo000O ( )
elif OoiI1I1 == 8002 :
 III11 ( )
elif OoiI1I1 == 8003 :
 iiiIiIII ( )
elif OoiI1I1 == 8004 :
 I11Iii11i11I1 ( )
elif OoiI1I1 == 8005 :
 iII1i1 ( )
elif OoiI1I1 == 8006 :
 o0o000OOOO ( IiII111iI1ii1 , iI11I1II )
elif OoiI1I1 == 8030 :
 IIIII1iii11 ( iI11I1II )
elif OoiI1I1 == 8045 :
 oOOOO0oo0O0OO ( iI11I1II )
elif OoiI1I1 == 8046 :
 O0OOoo0o ( iI11I1II )
elif OoiI1I1 == 8047 :
 iIiiIiiI1Ii111i ( iI11I1II )
elif OoiI1I1 == 8048 :
 OoOOOOOoOo0 ( iI11I1II )
elif OoiI1I1 == 8049 :
 iIioOo ( iI11I1II )
elif OoiI1I1 == 8020 :
 iIii1i1IIi ( )
elif OoiI1I1 == 8021 :
 OOOo0ooOO ( iI11I1II )
elif OoiI1I1 == 8022 :
 oooooO0o00 ( iI11I1II )
elif OoiI1I1 == 8023 :
 iIIIIIi11Ii ( iI11I1II )
elif OoiI1I1 == 8040 :
 ooO ( )
elif OoiI1I1 == 8041 :
 I1iI1i11IiI11 ( iI11I1II )
elif OoiI1I1 == 8042 :
 Oo0o0OO0OO000OO ( iI11I1II )
elif OoiI1I1 == 8043 :
 yt . PlayVideo ( iI11I1II )
elif OoiI1I1 == 8044 :
 O00o0000OO ( iI11I1II )
elif OoiI1I1 == 8060 :
 OOo0 ( )
elif OoiI1I1 == 8061 :
 OOoo00 ( iI11I1II )
elif OoiI1I1 == 8064 :
 OooO00oo0O0 ( )
elif OoiI1I1 == 8065 :
 i1iI ( iI11I1II )
elif OoiI1I1 == 8070 :
 IiI11IIi11Iii ( )
elif OoiI1I1 == 8071 :
 ii11i1I1i ( iI11I1II )
elif OoiI1I1 == 7080 :
 Iiiii1I ( iI11I1II )
elif OoiI1I1 == 8090 :
 IiI11I1Ii11II ( )
elif OoiI1I1 == 8091 :
 oo0ooOoOOoO ( iI11I1II )
elif OoiI1I1 == 8092 :
 iI1IiiiIIiiII ( iI11I1II )
elif OoiI1I1 == 8093 :
 Oo0000o ( iI11I1II )
elif OoiI1I1 == 8081 :
 oOOO00Oo ( )
elif OoiI1I1 == 8062 :
 Oo0oOOO ( iI11I1II )
elif OoiI1I1 == 8063 :
 oOOoOOooO0 ( iI11I1II )
elif OoiI1I1 == 8050 :
 iiIi1I1i1 ( )
elif OoiI1I1 == 8051 :
 OOOIiIi1111ii ( iI11I1II )
elif OoiI1I1 == 8052 :
 iI1I1II1 ( iI11I1II )
elif OoiI1I1 == 8085 :
 oooIi1I11IiI1i ( )
elif OoiI1I1 == 8086 :
 i1oooOoOoOO ( iI11I1II )
elif OoiI1I1 == 8087 :
 iiI1ii1Iii ( iI11I1II )
elif OoiI1I1 == 8088 :
 Ii1I1IIIiI1i ( iI11I1II , IiII111iI1ii1 )
elif OoiI1I1 == 9000 :
 ii1I11 ( )
elif OoiI1I1 == 1111 :
 i1IiI ( )
elif OoiI1I1 == 9001 :
 I111iIIII11iI ( )
elif OoiI1I1 == 9002 :
 oOooOoOOo0O ( )
elif OoiI1I1 == 9003 :
 oOOooI1I1i11 ( )
elif OoiI1I1 == 50 :
 IIo0OoO00 ( iI11I1II )
elif OoiI1I1 == 9020 :
 champlist ( )
elif OoiI1I1 == 9021 :
 III1I1iI1IIIIII ( )
elif OoiI1I1 == 9022 :
 OO0oO0Oo ( )
elif OoiI1I1 == 9023 :
 OoooOO0 ( )
elif OoiI1I1 == 9024 :
 oooOOO ( iI11I1II )
elif OoiI1I1 == 9030 :
 o0OoIII1IIiIi1 ( iI11I1II )
elif OoiI1I1 == 9031 :
 OOO0O ( iI11I1II )
elif OoiI1I1 == 9032 :
 I1iiIIIII1III ( iI11I1II )
elif OoiI1I1 == 9033 :
 II11iiIIiI11I ( iI11I1II )
elif OoiI1I1 == 7085 :
 oo00Oo0oO00Oo ( iI11I1II )
elif OoiI1I1 == 7086 :
 II1I11 ( iI11I1II )
elif OoiI1I1 == 7087 :
 ii11ii11II ( i1i11I1I1iii1 )
elif OoiI1I1 == 9666 :
 Ii1II11II1iii ( iI11I1II )
elif OoiI1I1 == 10100 : oO00oooo0OOo ( )
elif OoiI1I1 == 10105 : iiOo0 ( iI11I1II )
elif OoiI1I1 == 10106 : OooO ( iI11I1II )
elif OoiI1I1 == 10104 : oOoOOOO0OOO ( iI11I1II )
elif OoiI1I1 == 10107 : oOoo0OO0 ( )
elif OoiI1I1 == 10103 : I111ii1iI ( iI11I1II )
elif OoiI1I1 == 10108 : I1I1i1I1I1I1 ( iI11I1II )
elif OoiI1I1 == 10107 : oOoo0OO0 ( )
elif OoiI1I1 == 10000 : Origin_Menu ( )
elif OoiI1I1 == 10001 : oOooO0O0OoooO ( )
elif OoiI1I1 == 10002 : I1ii1i1iiii ( )
elif OoiI1I1 == 10003 : i1i111Iiiiiii ( )
elif OoiI1I1 == 10004 : iIiI1I1IIi11 ( iI11I1II )
elif OoiI1I1 == 10005 : iiIiII11i1 ( )
elif OoiI1I1 == 10006 : oo0oO0oO ( iI11I1II )
elif OoiI1I1 == 10007 : iI1i1iIi1iiII ( iI11I1II , iII1 )
elif OoiI1I1 == 10008 : O0oooo000oO0 ( )
elif OoiI1I1 == 10009 : o0oOoO00 ( )
elif OoiI1I1 == 10010 : OOoOooO00 ( iI11I1II )
elif OoiI1I1 == 10011 : OOoOOOo0 ( iI11I1II )
elif OoiI1I1 == 10012 : oO000o ( iI11I1II )
elif OoiI1I1 == 10109 : i1oo0OO0Oo ( iI11I1II )
elif OoiI1I1 == 10013 : OOOooO00OO00O ( iI11I1II )
elif OoiI1I1 == 10014 : oO00IiI1II11iiI ( )
elif OoiI1I1 == 10015 : II1Ii ( )
elif OoiI1I1 == 10016 : OO0ooo0 ( iI11I1II )
elif OoiI1I1 == 10017 : O0Oo0 ( )
elif OoiI1I1 == 10018 : o0iIIIIi ( )
elif OoiI1I1 == 10019 : IiiI11I1IIiI ( )
elif OoiI1I1 == 10020 : III11I1OOOO0o0O ( )
elif OoiI1I1 == 10021 : iI1ii ( )
elif OoiI1I1 == 10022 : o0OOOOOo0 ( iI11I1II )
elif OoiI1I1 == 10023 : i11ii ( IiII111iI1ii1 , iI11I1II )
elif OoiI1I1 == 10024 : IiIiI1i1 ( iI11I1II )
elif OoiI1I1 == 10025 : IIiI11I1I1i1i ( )
elif OoiI1I1 == 10026 : ooOoooo0 ( )
elif OoiI1I1 == 10027 : i1i ( )
elif OoiI1I1 == 10028 : o0OoOOo ( )
elif OoiI1I1 == 10029 : ii1iIi1Ii1 ( )
elif OoiI1I1 == 423 : oo0O0o00 ( iI11I1II )
elif OoiI1I1 == 426 : iI1ii11Ii ( iI11I1II )
elif OoiI1I1 == 10030 : Izle_Films ( )
elif OoiI1I1 == 10031 : Latest_Izle_Movies ( )
elif OoiI1I1 == 10032 : Izle_Genres ( )
elif OoiI1I1 == 10033 : Izle_Pop_Movies ( )
elif OoiI1I1 == 10034 : Izle_Boxsets ( )
elif OoiI1I1 == 10035 : Izle_Search ( )
elif OoiI1I1 == 10036 : Izle_Genres_Movie ( iI11I1II )
elif OoiI1I1 == 10037 : Izle_Boxset_single ( iI11I1II )
elif OoiI1I1 == 10038 : Izle_IFRAME ( )
elif OoiI1I1 == 10039 : Izle_Boxsets_Next ( iI11I1II )
elif OoiI1I1 == 10040 : OO0OOoooo0o ( )
elif OoiI1I1 == 10041 : Ii11iiI ( iI11I1II )
elif OoiI1I1 == 10042 : oo0o00OO ( iI11I1II )
elif OoiI1I1 == 10043 : i11i1 ( )
elif OoiI1I1 == 10044 : iiI ( iI11I1II )
elif OoiI1I1 == 10045 : IiI1ii11I1 ( IiII111iI1ii1 )
elif OoiI1I1 == 10046 : oOoo0ooOoo ( iI11I1II )
elif OoiI1I1 == 10047 : IIOOOoO00O ( iI11I1II )
elif OoiI1I1 == 10048 : o0O0O ( iI11I1II )
elif OoiI1I1 == 10049 : iIIIII1iI ( iI11I1II )
elif OoiI1I1 == 10050 : iIoOO0OO00 ( )
elif OoiI1I1 == 10051 : I1II1iIi ( )
elif OoiI1I1 == 10052 : I1iO00O000oOO0oO ( )
elif OoiI1I1 == 10053 : Addon ( iI11I1II )
elif OoiI1I1 == 10054 : iiI1II ( iI11I1II , IiII111iI1ii1 )
elif OoiI1I1 == 10055 :
 I1IiiIiii1 ( "addFavorite" )
 try :
  IiII111iI1ii1 = IiII111iI1ii1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiII111iI1ii1 = IiII111iI1ii1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1IiI ( IiII111iI1ii1 , iI11I1II , iII1 , o0Oo00 , iiiI )
elif OoiI1I1 == 10056 :
 I1IiiIiii1 ( "rmFavorite" )
 try :
  IiII111iI1ii1 = IiII111iI1ii1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiII111iI1ii1 = IiII111iI1ii1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oo0O0000Oo00o ( IiII111iI1ii1 )
elif OoiI1I1 == 10057 :
 I1IiiIiii1 ( "getFavorites" )
 Ii11ii1I1 ( )
elif OoiI1I1 == 10058 : Oo0OO ( )
elif OoiI1I1 == 10059 : Donators_Guide ( )
elif OoiI1I1 == 10060 : Ii1ii111i1 ( )
elif OoiI1I1 == 10061 : ii1Ii1IiIIi ( )
elif OoiI1I1 == 10062 : iI1IIIii ( IiII111iI1ii1 , iI11I1II , i1i11I1I1iii1 )
elif OoiI1I1 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + I11i1 + ")" )
elif OoiI1I1 == 10064 : IIIIi1 ( )
elif OoiI1I1 == 10065 : iIiiii ( iI11I1II )
elif OoiI1I1 == 10066 : O0 ( iI11I1II )
elif OoiI1I1 == 10068 : ii11I1 ( iI11I1II )
elif OoiI1I1 == 10069 : ii1III11 ( iI11I1II )
elif OoiI1I1 == 10070 : iIi1i1iIi1iI ( iI11I1II )
elif OoiI1I1 == 10071 : Genie_Watch ( )
elif OoiI1I1 == 10072 : o0oo0 ( )
elif OoiI1I1 == 10073 : OOOO0OOO ( iI11I1II )
elif OoiI1I1 == 10074 : O00Ooo ( iI11I1II )
elif OoiI1I1 == 10075 : III1I1Iii1iiI ( iII1 , IiII111iI1ii1 , iI11I1II )
elif OoiI1I1 == 10076 : I1ii1 ( iI11I1II )
elif OoiI1I1 == 10077 : IiIiII1 ( iI11I1II )
elif OoiI1I1 == 10078 : iIiIII1I1I1 ( )
elif OoiI1I1 == 10079 : Genie_Watch_Tv_Shows ( )
elif OoiI1I1 == 10080 : Genie_Watch_Tv_Genre ( iI11I1II )
elif OoiI1I1 == 10081 : Genie_Watch_TV_PlayRun ( iI11I1II )
elif OoiI1I1 == 10082 : Genie_Watch_TV_Episodes ( iI11I1II , iII1 )
elif OoiI1I1 == 10083 : Genie_Watch_Tv_Recent ( iI11I1II )
elif OoiI1I1 == 10084 : o0oooOO00 ( )
elif OoiI1I1 == 10085 : IIi1I11I1II ( )
elif OoiI1I1 == 10086 : i1Iii1i1I ( )
elif OoiI1I1 == 20000 : o00ooo0 ( )
elif OoiI1I1 == 20001 : iIiIi1iI11iiI ( )
elif OoiI1I1 == 20002 : III1II111Ii1 ( iI11I1II )
elif OoiI1I1 == 20003 : OO0iIiiIi11IIi ( iI11I1II )
elif OoiI1I1 == 20004 : Iio00 ( iI11I1II )
elif OoiI1I1 == 21004 : II1 ( )
elif OoiI1I1 == 21005 : I11Iii1 ( iI11I1II )
elif OoiI1I1 == 21006 : III1Ii1i1I1 ( iI11I1II )
elif OoiI1I1 == 21007 : iiO0O0o0oO0O00 ( iI11I1II )
elif OoiI1I1 == 30000 : iIi1iIIIiIiI ( )
elif OoiI1I1 == 30001 : o0IiiiI111I ( )
elif OoiI1I1 == 10012 : Resolve ( iI11I1II )
elif OoiI1I1 == 30003 : i1iIIi1o0o0OoOOOOOo ( )
elif OoiI1I1 == 30004 : III1I1 ( iI11I1II )
elif OoiI1I1 == 30005 : o0i1iI1iiI1I ( iI11I1II )
elif OoiI1I1 == 30006 : ii1iiIIiI1i ( )
elif OoiI1I1 == 30007 : o00O00Oo00O ( )
elif OoiI1I1 == 30008 : o0OOOOO0O ( iI11I1II )
elif OoiI1I1 == 30009 : I1III111i ( iI11I1II )
elif OoiI1I1 == 30010 : Oo0O0Oo00O ( iI11I1II )
elif OoiI1I1 == 30011 : OOO0 ( )
elif OoiI1I1 == 30012 : Ii1iI ( )
elif OoiI1I1 == 30013 : oO00 ( )
elif OoiI1I1 == 30014 : o00ii111Iiii ( )
elif OoiI1I1 == 30015 : ii1IiIi11 ( iI11I1II , iII1 , o0Oo00 )
elif OoiI1I1 == 30016 : ii1ii ( iI11I1II )
elif OoiI1I1 == 30019 : o0Oo ( iI11I1II )
elif OoiI1I1 == 30017 : i1oOOOOOOOoO ( iI11I1II )
elif OoiI1I1 == 30018 : ii1iI1II11ii ( iI11I1II )
elif OoiI1I1 == 30030 : Ii11iiI1 ( )
elif OoiI1I1 == 30031 : oO0OOOoooO00o0o ( )
elif OoiI1I1 == 30032 : I1ii1Ii1 ( )
elif OoiI1I1 == 30033 : OoOoO ( )
elif OoiI1I1 == 30034 : iI111I1III ( )
elif OoiI1I1 == 30035 : iIIi ( iI11I1II )
elif OoiI1I1 == 30036 : ooO00O00oOO ( iI11I1II )
elif OoiI1I1 == 30037 : I1IIII1ii ( iI11I1II )
elif OoiI1I1 == 30038 : Oo ( )
elif OoiI1I1 == 30039 : II1iiIiIiI ( )
elif OoiI1I1 == 50000 : I1iI1 ( )
elif OoiI1I1 == 50001 : o00O ( )
elif OoiI1I1 == 50002 : O00oO000Oo0 ( iI11I1II )
elif OoiI1I1 == 50003 : O0oO0oo0O ( i1i11I1I1iii1 )
elif OoiI1I1 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OoiI1I1 == 60001 : ii111I11iI ( )
elif OoiI1I1 == 60002 : OOO ( IiII111iI1ii1 )
elif OoiI1I1 == 60003 : Ooooooo ( IiII111iI1ii1 )
elif OoiI1I1 == 50004 : oOI1Ii1I1 ( )
elif OoiI1I1 == 50005 : speedtest . runtest ( iI11I1II )
elif OoiI1I1 == 70001 : I1iiIII ( )
elif OoiI1I1 == 70002 : O00oOoo0OoO0 ( iI11I1II )
elif OoiI1I1 == 70003 : Ooo0 ( iI11I1II )
elif OoiI1I1 == 70004 : oooO00o0 ( iI11I1II )
elif OoiI1I1 == 70005 : o0o00oO0oo000 ( iI11I1II )
elif OoiI1I1 == 70006 : o0Ooo0O0 ( )
elif OoiI1I1 == 50006 : Iii1I1I11iiI1 ( i1 , i1111 )
if 37 - 37: iI1i1IiI + ooOoOO0oOO * OoOOOOOo0o + OO
if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + OoOOOOOo0o / IIiIiII11i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
