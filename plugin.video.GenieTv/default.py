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
from imports import Parse , CNF_Studio_Indexer
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
IiiIII111iI = "3.0.0"
IiII = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/' )
i1i1II = xbmc . translatePath ( 'special://home/addonsbroke/' )
O0oo0OO0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
I1i1iiI1 = 'plugin.video.GenieTv'
iiIIIII1i1iI = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
o0oO0 = xbmcaddon . Addon ( id = I1i1iiI1 )
oo00 = xbmc . translatePath ( 'special://home/media' )
o00 = 'plugin.video.GenieTv'
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0oOoO00o = "GenieTv"
i1 = Net ( )
oOOoo00O0O = xbmcgui . Dialog ( )
i1111 = base64 . decodestring
i11 = o0oO0 . getSetting ( 'Build' )
I11 = o0oO0 . getSetting ( 'Local' )
Oo0o0000o0o0 = o0oO0 . getSetting ( 'Remote' )
oOo0oooo00o = o0oO0 . getSetting ( 'LocalM3u' )
oO0o0o0ooO0oO = o0oO0 . getSetting ( 'TEXTCOL' )
oo0o0O00 = o0oO0 . getSetting ( 'User' )
oO = o0oO0 . getSetting ( 'Pass' )
i1iiIIiiI111 = o0oO0 . getSetting ( 'AdultPass' )
oooOOOOO = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
i1iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'fanart.jpg' ) )
ii11iIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1i1iiI1 , 'icon.png' ) )
iI111I11I1I1 = ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
OOooO0OOoo = xbmc . translatePath ( 'special://database' )
iIii1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
oOOoO0 = xbmc . translatePath ( 'special://thumbnails' ) ;
O0OoO000O0OO = "GenieTv"
iiI1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
ooOoOoo0O = 'http://'
OooO0 = base64 . decodestring ( 'LnBocA==' )
II11iiii1Ii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OO0o = [ ]
Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
O0o0Oo = o0oO0 . getLocalizedString
Oo00OOOOO = CookieJar ( )
O0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( Oo00OOOOO ) )
O0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O00o0OO = int ( sys . argv [ 1 ] )
I11i1 = xbmc . translatePath ( o0oO0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
iIi1ii1I1 = os . path . join ( iIii1 , 'favorites' )
o0 = iIii1 + '/addons.ini'
I11II1i = xbmc . translatePath ( 'special://home/userdata/' )
IIIII = xbmc . translatePath ( 'special://home/userdatabroke/' )
ooooooO0oo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
IIiiiiiiIi1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
I1IIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
oOoOooOo0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( iIi1ii1I1 ) == True :
 iiiiiIIii = open ( iIi1ii1I1 ) . read ( )
else : iiiiiIIii = [ ]
O000OO0 = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
def I11iii1Ii ( url ) :
 I1IIiiIiii = urllib2 . Request ( url )
 I1IIiiIiii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O000oo0O = ''
 OOOOi11i1 = ''
 try :
  O000oo0O = urllib2 . urlopen ( I1IIiiIiii )
  OOOOi11i1 = O000oo0O . read ( )
  O000oo0O . close ( )
 except : pass
 if OOOOi11i1 != '' :
  return OOOOi11i1
 else :
  OOOOi11i1 = 'Failed'
  return OOOOi11i1
  if 29 - 29: oo0OO % OoO0O0 * O0o0Ooo / o0Oo0O0Oo00oO - O0o0O0O0ooO0 + iIIIIii1
oo000OO00Oo = [ ]
O0OOO0OOoO0O = I11iii1Ii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if O0OOO0OOoO0O != 'Failed' :
 oo000OO00Oo . append ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not O0OOO0OOoO0O != 'Failed' :
 O00Oo000ooO0 = I11iii1Ii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if O00Oo000ooO0 != 'Failed' :
  oo000OO00Oo . append ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not O00Oo000ooO0 != 'Failed' :
  OoO0O00 = I11iii1Ii ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if OoO0O00 != 'Failed' :
   oo000OO00Oo . append ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not OoO0O00 != 'Failed' :
   IIiII = I11iii1Ii ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if IIiII != 'Failed' :
    oo000OO00Oo . append ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
o0ooOooo000oOO = ( str ( oo000OO00Oo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
Oo0oOOo = o0ooOooo000oOO + 'GenieArt/NEW/'
if 58 - 58: IiI11iII1 * OOO00O / oo0OO * IiI11iII1
if 65 - 65: Ii1I + O0o0Ooo
def iiiI1I11i1 ( ) :
 if not os . path . exists ( IiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIi1i11111 = 'genie tv repo not being installed '
  ooOO00O00oo ( IIi1i11111 )
 else :
  I1ii11iI ( )
  if 14 - 14: OOooOOo / iIIIIii1 . OOooOOo . O0o0Ooo % oO0o * O0o0Ooo
def I1ii11iI ( ) :
 if 16 - 16: OOooOOo . OOO00O + Ii
 i1i1I1IIii1II = O0 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 ii1ii1ii = open ( OOOO ) . read ( )
 oooooOoo0ooo = open ( OOO00 ) . read ( )
 if 6 - 6: O0o0Ooo - o0Oo0O0Oo00oO + iI11I1II1I1I - IiI11iII1 - Ii
 OO0oOO0O = re . compile ( 'version="(.+?)" provider' ) . findall ( ii1ii1ii )
 oOiIi1IIIi1 = re . compile ( 'version="(.+?)" provider-name' ) . findall ( oooooOoo0ooo )
 O0oOoOOOoOO = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( i1i1I1IIii1II )
 ii1ii11IIIiiI = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( i1i1I1IIii1II )
 for O00OOOoOoo0O in OO0oOO0O :
  O000OOo00oo = O00OOOoOoo0O
  for oo0OOo in O0oOoOOOoOO :
   if not oo0OOo == O000OOo00oo :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    ooOOO00Ooo ( )
   if oo0OOo == O000OOo00oo :
    IiIIIi1iIi
 for ooOOoooooo in oOiIi1IIIi1 :
  II1I = ooOOoooooo
  for O0i1II1Iiii1I11 in ii1ii11IIIiiI :
   if not O0i1II1Iiii1I11 == II1I :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    IIII ( )
   if O0i1II1Iiii1I11 == II1I :
    xbmc . sleep ( 100 )
    IiIIIi1iIi
def iiIiI ( ) :
 iiiI1I11i1 ( )
 o00oooO0Oo ( )
 o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , Oo0oOOo + 'GenieUpdate.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']WIZARD[/COLOR]' , str ( o0ooOooo000oOO ) , 4001 , Oo0oOOo + 'Wizard.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']STREAMS[/COLOR]' , str ( o0ooOooo000oOO ) , 4002 , Oo0oOOo + 'Streams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Music[/COLOR]' , str ( o0ooOooo000oOO ) , 4003 , Oo0oOOo + 'Music.png' , i1iIIi1 , '' )
  if 86 - 86: OOooOOo - o0Oo0O0Oo00oO - oO0o * O0o0O0O0ooO0
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']BUILDERS TOOLBOX[/COLOR]' , str ( o0ooOooo000oOO ) , 32 , Oo0oOOo + 'BuildersToolbox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']SOURCE LIST[/COLOR]' , str ( o0ooOooo000oOO ) , 46 , Oo0oOOo + 'SoruceList.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MAINTENANCE[/COLOR]' , str ( o0ooOooo000oOO ) , 3 , Oo0oOOo + 'Maintenance.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ADDONS[/COLOR]' , '' , 10050 , Oo0oOOo + 'Addons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']APK TOOL[/COLOR]' , str ( o0ooOooo000oOO ) , 30039 , Oo0oOOo + 'APKTools.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv RSS Feed[/COLOR]' , str ( o0ooOooo000oOO ) , 39 , Oo0oOOo + 'GenieTVRSSFeed.png' , i1iIIi1 , '' )
  if 66 - 66: ii + o0o00Oo0O
  if 11 - 11: O0o0Ooo + ii - oO0o / I11i + I1ii11iIi11i . IIiIiII11i
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 91 - 91: Ii1I + oOo0O0Ooo . OoO0O0 * Ii1I + oOo0O0Ooo * I1ii11iIi11i
def O000OOOOOo ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']BACKUP MY BUILD[/COLOR]' , str ( o0ooOooo000oOO ) , 10060 , Oo0oOOo + 'BackupMyBuild.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']RESTORE MY BUILD[/COLOR]' , str ( o0ooOooo000oOO ) , 49 , Oo0oOOo + 'RestoreMyBuild.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']WIPE GENIE[/COLOR]' , str ( o0ooOooo000oOO ) , 41 , Oo0oOOo + 'WipeGenie.png' , i1iIIi1 , '' )
 if 22 - 22: ooOoO0O00 + o0o00Oo0O . iI11I1II1I1I * O0o0O0O0ooO0 % Ii * oOo0O0Ooo
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Genie BUILDS[/COLOR]' , str ( o0ooOooo000oOO ) , 44 , Oo0oOOo + 'GenieBuilds.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def oo000o ( ) :
 iiiI1I11i1 ( )
 if i1iiIIiiI111 == '5knuckleshuffle' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']XVID[/COLOR]' , str ( o0ooOooo000oOO ) , 10100 , Oo0oOOo + 'Jizbox.png' , i1iIIi1 , '' )
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ADULT CHANNELS[/COLOR]' , str ( o0ooOooo000oOO ) , 30033 , Oo0oOOo + 'adu.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']FAVOURITES[/COLOR]' , str ( o0ooOooo000oOO ) , 10057 , Oo0oOOo + 'Favourites.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , str ( o0ooOooo000oOO ) , 9000 , Oo0oOOo + 'Search.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , Oo0oOOo + 'TvGuide.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']STREAM TEAM[/COLOR]' , str ( o0ooOooo000oOO ) , 4006 , Oo0oOOo + 'StreamTeam.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']24/7 STREAMS[/COLOR]' , '' , 30030 , Oo0oOOo + '247Streams.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MOVIES[/COLOR]' , str ( o0ooOooo000oOO ) , 4004 , Oo0oOOo + 'Movies.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']TV SHOWS[/COLOR]' , str ( o0ooOooo000oOO ) , 4005 , Oo0oOOo + 'TVShows.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( o0ooOooo000oOO ) , 4007 , Oo0oOOo + 'Kids.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEWS[/COLOR]' , str ( o0ooOooo000oOO ) , 30032 , Oo0oOOo + 'News.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv TUTORIALS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , Oo0oOOo + 'GenieTVTutorials.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']HOBBIES[/COLOR]' , str ( o0ooOooo000oOO ) , 4008 , Oo0oOOo + 'Hobbies.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH YOUTUBE[/COLOR]' , str ( o0ooOooo000oOO ) , 10064 , Oo0oOOo + 'SeachYouTube.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']REQUESTS[/COLOR]' , str ( o0ooOooo000oOO ) + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , Oo0oOOo + 'Requests.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']STAND UP[/COLOR]' , '' , 10003 , Oo0oOOo + 'StandUp.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']DOCUMENTARIES[/COLOR]' , str ( o0ooOooo000oOO ) , 8040 , Oo0oOOo + 'documentaries.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']DISCLOSE TV[/COLOR]' , str ( o0ooOooo000oOO ) , 7001 , Oo0oOOo + 'DiscloseTV.png' , i1iIIi1 , '' )
  if 44 - 44: ooOoO0O00 % IIiIiII11i + O0o0Ooo
  if 45 - 45: O0o0O0O0ooO0 / O0o0O0O0ooO0 + IiI11iII1 + OOO00O
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAYLIST LOADER[/COLOR]' , str ( o0ooOooo000oOO ) , 3000 , Oo0oOOo + 'PlaylistLoader.png' , i1iIIi1 , '' )
  if 47 - 47: I11i + OOO00O
  if 82 - 82: IIiIiII11i . iIIIIii1 - iI11I1II1I1I - iIIIIii1 * IIiIiII11i
  if 77 - 77: iI11I1II1I1I * oO0o
  if 95 - 95: oOo0O0Ooo + Ii
  if 6 - 6: OOO00O / Ii + O0o0O0O0ooO0 * oo0OO
  if 80 - 80: IIiIiII11i
  if 83 - 83: O0o0Ooo . Ii + IIiIiII11i . I11i * O0o0Ooo
  if 53 - 53: IIiIiII11i
  if 31 - 31: oO0o
  if 80 - 80: IiI11iII1 . Ii - I11i
  if 25 - 25: oO0o
  if 62 - 62: OoO0O0 + o0o00Oo0O
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 98 - 98: I11i
def o00oooO0Oo ( ) :
 if not os . path . exists ( II ) :
  OOOO0oo0 ( 'Change Log 08/07/16 - v2.9.0' , 'Silent Hunter and Redemption Streams added to search function, Quick Silver music source in music section, live music channels renewed, Discovery section fixed and updated with new content, Popcorn Box in movies section fixed and updated, Disclose Tv Fixed and updated' )
  os . makedirs ( II )
  if 35 - 35: o0Oo0O0Oo00oO - oOo0O0Ooo % I11i . ii % o0Oo0O0Oo00oO
  if 47 - 47: O0o0O0O0ooO0 - o0Oo0O0Oo00oO . IIiIiII11i + ii . Ii
def OOo0oO00ooO00 ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( o0ooOooo000oOO ) , 9001 , Oo0oOOo + 'Search.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']POPCORN BOX[/COLOR]' , str ( o0ooOooo000oOO ) , 7061 , Oo0oOOo + 'PopcornBox.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , Oo0oOOo + 'FilmTrailers.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , Oo0oOOo + 'ClassicMovies.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def oOO0O00oO0Ooo ( ) :
 iiiI1I11i1 ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , Oo0oOOo + 'GTVIPTV.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , Oo0oOOo + 'GTVIPTV.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , Oo0oOOo + 'GTVIPTV.png' , i1iIIi1 , '' )
 if 67 - 67: oO0o - OoO0O0
 if 36 - 36: iIIIIii1
def I11iI ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( o0ooOooo000oOO ) , 9002 , Oo0oOOo + 'Search.png' , i1iIIi1 , '' )
 if 37 - 37: OOO00O % oo0OO . Ii % o0Oo0O0Oo00oO . I1ii11iIi11i
 if 39 - 39: OoO0O0 - I1ii11iIi11i * Ii1I % I11i
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH SERIES[/COLOR]' , '' , 10040 , Oo0oOOo + 'WatchSeries.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']iWATCH SERIES[/COLOR]' , '' , 8020 , Oo0oOOo + 'iWatchSeries.png' , i1iIIi1 , '' )
 if 40 - 40: iI11I1II1I1I / OOooOOo % Ii1I + IIiIiII11i
 if 27 - 27: IIiIiII11i * OOooOOo * iI11I1II1I1I
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC TV[/COLOR]' , str ( o0ooOooo000oOO ) , 8064 , Oo0oOOo + 'ClassicTV.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , Oo0oOOo + 'TVShowTrailers.png' , i1iIIi1 , '' )
 if 86 - 86: oO0o * OoO0O0 . O0o0O0O0ooO0
 i1Iii1i1I ( 'movies' , 'MAIN' )
def iI ( ) :
 iiiI1I11i1 ( )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , Oo0oOOo + 'SilentHunter.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , Oo0oOOo + 'TheReaper.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']PANDORAS BOX[/COLOR]' , str ( o0ooOooo000oOO ) , 10025 , Oo0oOOo + 'PandorasBox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , Oo0oOOo + 'RedemptionStreams.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']DoJo STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , Oo0oOOo + 'DojoStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , str ( o0ooOooo000oOO ) , 1023 , Oo0oOOo + 'ScoobyStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , '' , 1017 , Oo0oOOo + 'Herovision.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , Oo0oOOo + 'ITVStreams.png' , i1iIIi1 , '' )
 if 90 - 90: IiI11iII1 % o0Oo0O0Oo00oO - iI11I1II1I1I - iI11I1II1I1I / Ii % Ii1I
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 37 - 37: oo0OO - oOo0O0Ooo . O0o0Ooo * o0Oo0O0Oo00oO - O0o0O0O0ooO0
def II1I11Ii1 ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , Oo0oOOo + 'SilentHunter.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , Oo0oOOo + 'SilentHunter.png' , i1iIIi1 , '' )
 if 44 - 44: iI11I1II1I1I . ii . O0o0Ooo / IiI11iII1 + O0o0O0O0ooO0 * IIiIiII11i
def OoO ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , Oo0oOOo + 'Herovision.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , Oo0oOOo + 'Herovision.png' , i1iIIi1 , '' )
 if 51 - 51: ii * OoO0O0
def OO0ooOOO0OOO ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , Oo0oOOo + 'SearchCartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( o0ooOooo000oOO ) , 21004 , Oo0oOOo + 'watchcartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 10001 , Oo0oOOo + 'Cartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , Oo0oOOo + 'anime.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def oO00oooOOoOo0 ( ) :
 iiiI1I11i1 ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']FOOTBALL[/COLOR]' , '' , 10002 , Oo0oOOo + 'Football.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , Oo0oOOo + 'Fitness.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Go Fishing[/COLOR]' , str ( o0ooOooo000oOO ) , 8090 , Oo0oOOo + 'GoFishing.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , Oo0oOOo + 'GenieTVKitchen.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
 if 62 - 62: ii * oOo0O0Ooo
 if 58 - 58: OOooOOo % I11i
def IiIIIi1iIi ( ) :
 O0OOO0OOoO0O = O0 ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 OO0oOO0O = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( O0OOO0OOoO0O )
 for IIi1i11111 in OO0oOO0O :
  IIi1i11111 = ( str ( IIi1i11111 ) )
  if os . path . exists ( xbmc . translatePath ( IIi1i11111 ) ) :
   i1OOoO = ( IIi1i11111 ) . replace ( 'special://home/addons/' , '' )
   OOOO0oo0 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1OOoO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OO0O000 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OO0O000 == 0 :
    ooOO00O00oo ( IIi1i11111 )
    iiIiI1i1 ( )
   elif OO0O000 == 1 :
    oO0O00oOOoooO ( IIi1i11111 )
  else :
   pass
   if 46 - 46: oOo0O0Ooo - ii - O0o0Ooo * IIiIiII11i
def oO0O00oOOoooO ( addon ) :
 i1OOoO = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 34 - 34: O0o0Ooo - O0o0O0O0ooO0 / OoO0O0 + Ii1I * o0Oo0O0Oo00oO
def ooOO00O00oo ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OO = os . path . join ( iiI1IiI , 'default.py' )
 OO0OoOO0o0o = open ( OO , "w+" )
 if 95 - 95: Ii
 OO0OoOO0o0o . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OO0OoOO0o0o . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OO0OoOO0o0o . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 32 - 32: OoO0O0
 if 42 - 42: iIIIIii1 * o0o00Oo0O % ooOoO0O00 . OoO0O0 / I11i
 if 32 - 32: oOo0O0Ooo * I1ii11iIi11i
 if 78 - 78: OoO0O0 - ii - Ii1I / OOO00O / IIiIiII11i
 if 29 - 29: oOo0O0Ooo % oOo0O0Ooo
 if 94 - 94: iI11I1II1I1I / I1ii11iIi11i % O0o0O0O0ooO0 * O0o0O0O0ooO0 * IIiIiII11i
 if 29 - 29: oO0o + OOooOOo / I11i / OoO0O0 * iI11I1II1I1I
 if 62 - 62: OoO0O0 / oo0OO - oO0o . O0o0Ooo
 if 11 - 11: Ii1I . oO0o * iIIIIii1 * ii + OOO00O
 if 33 - 33: o0o00Oo0O * I11i - IiI11iII1 % IiI11iII1
 if 18 - 18: IiI11iII1 / I1ii11iIi11i * IiI11iII1 + IiI11iII1 * Ii * Ii1I
 if 11 - 11: OOO00O / OOooOOo - iIIIIii1 * ii + ii . OOooOOo
 if 26 - 26: o0Oo0O0Oo00oO % Ii1I
 if 76 - 76: iIIIIii1 * O0o0O0O0ooO0
 if 52 - 52: OoO0O0
 if 19 - 19: oOo0O0Ooo
 if 25 - 25: o0Oo0O0Oo00oO / OOO00O
 if 31 - 31: OoO0O0 . o0o00Oo0O % oOo0O0Ooo . I11i + iIIIIii1
 if 71 - 71: IiI11iII1 . IIiIiII11i
def oo0 ( ) :
 iiIiII1 ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
 iiIiII1 ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
 iiIiII1 ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
 iiIiII1 ( 'Search' , '' , 10078 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
 if 61 - 61: OOooOOo - OoO0O0 - ooOoO0O00
def IiI1iIiIIIii ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoO00O0 = 'http://imoviemax.se/?s=' + ( oOoO ) . replace ( ' ' , '+' )
 OOIi1iI111II1I1 = oOoO00O0 . lower ( )
 oOOOOoOO0o ( OOIi1iI111II1I1 )
def i1II1 ( url ) :
 i11i1 = [ ]
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii , oo00oO0o in OO0oOO0O :
  if IiiiiI1i1Iii in i11i1 :
   pass
  else :
   iiIiII1 ( IiiiiI1i1Iii + ' - ' + oo00oO0o + ' Films' , url , 10074 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
   i11i1 . append ( IiiiiI1i1Iii )
   if 31 - 31: OoO0O0
def i1OOO0000oO ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii , iI1i111I1Ii in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii + ' - Views:' + iI1i111I1Ii , url , 10075 , Oo0oOOo + 'genievision.png' , i1iIIi1 , '' )
  if 25 - 25: IiI11iII1 - O0o0O0O0ooO0
  if 10 - 10: IIiIiII11i / oo0OO % ii * O0o0Ooo % Ii1I
def oOOOOoOO0o ( url ) :
 I1i11 = [ ]
 O0OOO0OOoO0O = O0 ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( O0OOO0OOoO0O )
 for next in next :
  iiIiII1 ( 'NEXT PAGE' , next , 10074 , Oo0oOOo + 'Next.png' , i1iIIi1 , '' )
 OO0oOO0O = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , IiiiiI1i1Iii , url in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 10075 , IiIi1I1 , IiIi1I1 , '' )
  I1i11 . append ( IiiiiI1i1Iii )
  if 39 - 39: IIiIiII11i + OOooOOo - OOO00O . OOooOOo
def OOOooo ( img , name , url ) :
 img = img
 name = name
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( O0OOO0OOoO0O )
 for OooO0OO , url in OO0oOO0O :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o0OOo0o0O0O = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o0OOo0o0O0O
  o0OO0o0oOOO0O = ( OooO0OO ) . replace ( 'play-' , 'Server ' )
  o0O0OOO0Ooo ( o0OO0o0oOOO0O , o0OOo0o0O0O , 10076 , img , img , '' )
  if 49 - 49: Ii1I . I11i . IIiIiII11i
def o000ooooO0o ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( O0OOO0OOoO0O )
 for iI1i11 in OO0oOO0O :
  if '=m' in iI1i11 :
   OoOOoooOO0O ( iI1i11 )
  elif 'php' in iI1i11 :
   o000ooooO0o ( url )
  else :
   O0OOO0OOoO0O = O0 ( iI1i11 )
   OO0oOO0O = re . compile ( 'content="(.+?)">' ) . findall ( O0OOO0OOoO0O )
   for ooo00Ooo in OO0oOO0O :
    OoOOoooOO0O ( iI1i11 )
    if 93 - 93: Ii - oOo0O0Ooo * Ii1I * O0o0Ooo % o0o00Oo0O + ii
    if 25 - 25: iIIIIii1 + o0Oo0O0Oo00oO / OOO00O . I11i % o0o00Oo0O * oO0o
    if 84 - 84: OOO00O % o0Oo0O0Oo00oO + Ii
def II1I1Ii ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Ooo0O0oooo = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for iiI , oOIIiIi in Ooo0O0oooo :
  print 'there ><><><><><><><><><><><><'
  iiI = iiI
  OO0oOO0O = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oOIIiIi ) )
  for IiiiiI1i1Iii , OOoOooOoOOOoo in OO0oOO0O :
   print 'here <><><><><><><><><><><><>'
   iiIiII1 ( '[COLORred]' + iiI + '[/COLOR] - ' + IiiiiI1i1Iii + ' - [COLOR' + oO0o0o0ooO0oO + ']' + OOoOooOoOOOoo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , Oo0oOOo + 'loader.png' , i1iIIi1 , '' )
 Iiii1iI1i = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for iiI , I1ii1ii11i1I in Iiii1iI1i :
  print 'there ><><><><><><><><><><><><'
  iiI = iiI
  OO0oOO0O = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1ii1ii11i1I ) )
  for IiiiiI1i1Iii , OOoOooOoOOOoo in OO0oOO0O :
   print 'here <><><><><><><><><><><><>'
   iiIiII1 ( '[COLORred]' + iiI + '[/COLOR] - ' + IiiiiI1i1Iii + ' - [COLOR' + oO0o0o0ooO0oO + ']' + OOoOooOoOOOoo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , Oo0oOOo + 'loader.png' , i1iIIi1 , '' )
   if 58 - 58: O0o0O0O0ooO0 + I1ii11iIi11i
   if 12 - 12: I11i - Ii1I % OOooOOo * O0o0Ooo
   if 44 - 44: O0o0O0O0ooO0 % o0Oo0O0Oo00oO
def iiI11i1II ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Iiii1iI1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for Iiii1iI1i in Iiii1iI1i :
  IiiiiI1i1Iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
  for IiiiiI1i1Iii in IiiiiI1i1Iii :
   IiiiiI1i1Iii = ( IiiiiI1i1Iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Iiii1iI1i ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  OO0O0OOo0O = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
  for OO0O0OOo0O in OO0O0OOo0O :
   OO0O0OOo0O = 'http:' + OO0O0OOo0O
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , '' , '' )
  if 36 - 36: OOO00O . I1ii11iIi11i % OOO00O % oO0o
  if 2 - 2: I11i - Ii1I
  if 58 - 58: o0Oo0O0Oo00oO + I11i - oOo0O0Ooo
  if 3 - 3: oO0o
def oooOoOOO0oo0o ( url ) :
 if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
 ooOOoO = [ ]
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for iI1i11 , IiIi1I1 , IiiiiI1i1Iii , I1i11i in OO0oOO0O :
  IiiiiI1i1Iii = ( IiiiiI1i1Iii ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O00Oo000ooO0 = O0 ( iI1i11 )
  oOiIi1IIIi1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O00Oo000ooO0 )
  for IiIi , OOOOO0O00 in oOiIi1IIIi1 :
   Iii = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OOOOO0O00 ) )
   for iIIiIiI1I1 in Iii :
    if IiiiiI1i1Iii in ooOOoO :
     pass
    else :
     o0O0OOO0Ooo ( IiiiiI1i1Iii , IiIi , 8043 , IiIi1I1 , IiIi1I1 , iIIiIiI1I1 )
     i1Iii1i1I ( 'movies' , 'INFO' )
     ooOOoO . append ( IiiiiI1i1Iii )
     if 56 - 56: oOo0O0Ooo . o0o00Oo0O + I1ii11iIi11i
     if 1 - 1: O0o0O0O0ooO0
def O0O0Ooo ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , oo0O0o00o0O , iIIiIiI1I1 , I11i1II , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 10065 , oo0O0o00o0O , I11i1II , iIIiIiI1I1 )
 i1Iii1i1I ( 'movies' , 'INFO' )
 if 72 - 72: iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
def ooo000o000 ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoO00O0 = 'https://www.youtube.com/results?search_query=' + ( oOoO ) . replace ( ' ' , '+' )
 OOIi1iI111II1I1 = oOoO00O0 . lower ( )
 O0OOO0OOoO0O = O0 ( OOIi1iI111II1I1 )
 OO0oOO0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( O0OOO0OOoO0O )
 for O0o in next :
  O0o = 'https://www.youtube.com' + O0o
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , O0o , 10065 , Oo0oOOo + 'Next.png' , i1iIIi1 , '' )
 for IiIi1I1 , O0o , IiiiiI1i1Iii , O0OOoOOO0oO , OOOOO0O00 in OO0oOO0O :
  OO0o . append ( IiiiiI1i1Iii )
  i1Iii1i1I ( 'tvshows' , 'INFO' )
  OO0O0OOo0O = 'http:' + ( IiIi1I1 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OO0O0OOo0O
  O0o = 'http://www.youtube.com' + O0o
  o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , OO0O0OOo0O , OOOOO0O00 )
 else :
  OO0oOO0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for IiIi1I1 , O0o , IiiiiI1i1Iii , O0OOoOOO0oO in OO0oOO0O :
   print 'im doing it'
   i1Iii1i1I ( 'tvshows' , 'INFO' )
   OO0O0OOo0O = 'http:' + ( IiIi1I1 ) . replace ( 'https:' , '' )
   O0o = 'http://www.youtube.com' + O0o
   if '&' in O0o :
    print ' i got here'
    O0OOO0OOoO0O = O0 ( O0o )
    Iiii1iI1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
    for Iiii1iI1i in Iiii1iI1i :
     IiiiiI1i1Iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
     for IiiiiI1i1Iii in IiiiiI1i1Iii :
      IiiiiI1i1Iii = ( IiiiiI1i1Iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     O0o = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Iiii1iI1i ) )
     for O0o in O0o :
      O0o = 'https://www.youtube.com/w' + O0o
     OO0O0OOo0O = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
     for OO0O0OOo0O in OO0O0OOo0O :
      OO0O0OOo0O = 'http:' + OO0O0OOo0O
     o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , i1iIIi1 , '' )
   elif IiiiiI1i1Iii in OO0o :
    pass
   elif 'user' in O0o or 'elete' in IiiiiI1i1Iii :
    pass
   elif 'hannel' in O0o :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + O0o
    O0OOO0OOoO0O = O0 ( O0o )
    I1ii11 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
    for IiIi1I1 , O0o , IiiiiI1i1Iii in I1ii11 :
     if 'outube' in O0o or 'list' in O0o :
      pass
     elif 'atch' in O0o :
      O0o = ( O0o ) . replace ( '/watch?v=' , '' )
      o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiIi1I1 , 'http:' + IiIi1I1 , '' )
     else :
      pass
   else :
    o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , OO0O0OOo0O , '' )
    if 74 - 74: I1ii11iIi11i - I11i . ooOoO0O00
def i1III ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( O0OOO0OOoO0O )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , url , 10065 , Oo0oOOo + 'Next.png' , i1iIIi1 , '' )
 for IiIi1I1 , url , IiiiiI1i1Iii , O0OOoOOO0oO , OOOOO0O00 in OO0oOO0O :
  OO0o . append ( IiiiiI1i1Iii )
  i1Iii1i1I ( 'tvshows' , 'INFO' )
  OO0O0OOo0O = 'http:' + ( IiIi1I1 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + OO0O0OOo0O
  url = 'http://www.youtube.com' + url
  o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , OO0O0OOo0O , OOOOO0O00 )
 else :
  OO0oOO0O = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for IiIi1I1 , url , IiiiiI1i1Iii , O0OOoOOO0oO in OO0oOO0O :
   i1Iii1i1I ( 'tvshows' , 'INFO' )
   OO0O0OOo0O = 'http:' + ( IiIi1I1 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    O0OOO0OOoO0O = O0 ( url )
    Iiii1iI1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
    for Iiii1iI1i in Iiii1iI1i :
     IiiiiI1i1Iii = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
     for IiiiiI1i1Iii in IiiiiI1i1Iii :
      IiiiiI1i1Iii = ( IiiiiI1i1Iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( Iiii1iI1i ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     OO0O0OOo0O = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( Iiii1iI1i ) )
     for OO0O0OOo0O in OO0O0OOo0O :
      OO0O0OOo0O = 'http:' + OO0O0OOo0O
     o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , i1iIIi1 , '' )
   elif IiiiiI1i1Iii in OO0o :
    pass
   elif 'user' in url or 'elete' in IiiiiI1i1Iii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    O0OOO0OOoO0O = O0 ( url )
    I1ii11 = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
    for IiIi1I1 , url , IiiiiI1i1Iii in I1ii11 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IiIi1I1 , 'http:' + IiIi1I1 , '' )
     else :
      pass
   else :
    o0O0OOO0Ooo ( '[COLORred]' + O0OOoOOO0oO + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O , OO0O0OOo0O , '' )
    if 49 - 49: Ii % o0Oo0O0Oo00oO . OOooOOo
    if 13 - 13: Ii + ooOoO0O00 * iI11I1II1I1I % ii - IIiIiII11i * OoO0O0
def iiIi1iI1iIii ( ) :
 if oO == 'insert_password' :
  oOOoo00O0O . ok ( '[COLOR' + oO0o0o0ooO0oO + ']Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLOR' + oO0o0o0ooO0oO + ']http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  o00OooO0oo = open ( o0 )
  OO0oOO0O = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( o00OooO0oo ) )
  for o0o0oOoOO0O , i1ii1II1ii in OO0oOO0O :
   if o0o0oOoOO0O == 'needs replacing' or i1ii1II1ii == 'needs replacing' :
    iII111Ii ( )
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']DONATORS LIST[/COLOR]' , str ( o0ooOooo000oOO ) + '/thelistnew.m3u' , 7080 , Oo0oOOo + 'GTVIPTV.png' , i1iIIi1 , '' )
  if 52 - 52: IIiIiII11i % iIIIIii1 . OOooOOo * iI11I1II1I1I
def I111i1II ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + Ooo + ")" )
 iII111Ii ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 69 - 69: o0Oo0O0Oo00oO * o0o00Oo0O . Ii / o0Oo0O0Oo00oO . I11i
def O0oOOo ( ) :
 try :
  I1II = gui . TVGuide ( )
  I1II . doModal ( )
  del I1II
  if 64 - 64: o0o00Oo0O % O0o0Ooo % o0o00Oo0O * oO0o . oo0OO + oOo0O0Ooo
 except :
  import sys
  import traceback as tb
  ( O00 , I11ii1i1 , traceback ) = sys . exc_info ( )
  tb . print_exception ( O00 , I11ii1i1 , traceback )
  if 78 - 78: O0o0O0O0ooO0
def iIiIIIIIii ( ) :
 iiIiII1 ( 'Full Backup' , '' , 10061 , Oo0oOOo + 'FullBackUp.png' , i1iIIi1 , 'Back Up Your Full System' )
 if os . path . exists ( oOoOooOo0o0 ) :
  iiIiII1 ( 'Backup Genie Favourites' , O0o , 10062 , Oo0oOOo + 'BackupGenieFavourites.png' , i1iIIi1 , 'Back Up Your favourites' )
 if os . path . exists ( IIiiiiiiIi1I1 ) :
  iiIiII1 ( 'Backup Ivue Config' , IIiiiiiiIi1I1 , 10062 , Oo0oOOo + 'BackUpIvueConfig.png' , i1iIIi1 , 'Back Up Your master.db' )
 if os . path . exists ( I1IIIii ) :
  iiIiII1 ( 'Backup Kodi Favourites' , I1IIIii , 10062 , Oo0oOOo + 'BackKodiFavourites.png' , i1iIIi1 , 'Back Up Your favourites.xml' )
  if 58 - 58: I11i / iIIIIii1 . OOooOOo / ii + IiI11iII1
  if 86 - 86: O0o0Ooo * oOo0O0Ooo + O0o0Ooo + IIiIiII11i
  if 8 - 8: IiI11iII1 - O0o0O0O0ooO0 / OOO00O
zip = o0oO0 . getSetting ( 'zip' )
oo0oOoo = xbmc . translatePath ( os . path . join ( zip ) )
def oOOO0o00o ( ) :
 iI11 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 96 - 96: OoO0O0
  if 85 - 85: I11i . OOooOOo / OOO00O . o0o00Oo0O % IiI11iII1
  if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . O0o0O0O0ooO0
def I1iii11 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = oOoOooOo0o0
  elif 'Ivue' in name :
   url = IIiiiiiiIi1I1
  elif 'Kodi' in name :
   url = I1IIIii
  oOOO0o00o ( )
  ooo0O = open ( url ) . read ( )
  iII1iii = os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] )
  i11i1iiiII = open ( iII1iii , mode = 'w' )
  i11i1iiiII . write ( ooo0O )
  i11i1iiiII . close ( )
 else :
  if 'guisettings.xml' in description :
   ooOO0oO0oo00o = open ( os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOOo0oo0O = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   OO0oOO0O = re . compile ( oOOo0oo0O ) . findall ( ooOO0oO0oo00o )
   for type , IiiIiI1Ii1i , i1iIi in OO0oOO0O :
    i1iIi = i1iIi . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IiiIiI1Ii1i , i1iIi ) )
  else :
   iII1iii = os . path . join ( url )
   ooo0O = open ( os . path . join ( oo0oOoo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i11i1iiiII = open ( iII1iii , mode = 'w' )
   i11i1iiiII . write ( ooo0O )
   i11i1iiiII . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 30 - 30: o0o00Oo0O - iI11I1II1I1I / ii
 if 89 - 89: O0o0O0O0ooO0 - OOO00O % I1ii11iIi11i % I11i
 if 49 - 49: I1ii11iIi11i - oOo0O0Ooo / iIIIIii1 / o0o00Oo0O % I11i * o0Oo0O0Oo00oO
 if 100 - 100: OoO0O0 . O0o0O0O0ooO0 / o0o00Oo0O * ooOoO0O00 * o0Oo0O0Oo00oO * I1ii11iIi11i
def OO00 ( ) :
 o0OOo00OoO = 1
 oOOO0o00o ( )
 iIi1 = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'Full Backup' , '' ) )
 i11iiI1111 = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'my_full_backup.zip' ) )
 oOoooo000Oo00 = xbmc . translatePath ( os . path . join ( oo0oOoo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIi1 ) :
  os . makedirs ( iIi1 )
 OOoo = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OOoo ) : return False , 0
 o00O00oO00 = OOoo
 Ii1i1i1i1I1Ii = xbmc . translatePath ( os . path . join ( iIi1 , o00O00oO00 + '.zip' ) )
 iiiI1 = [ 'plugin.video.GenieTv' ]
 OOOoO0O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0iiiI1I1iIIIi1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IiiI1iiiiI1iI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iIiiiii1i = "Creating full backup of existing build"
 iiIi1IIiI = "Creating Community Build"
 i1oO0OO0 = "Archiving..."
 o0O0Oo00 = ""
 O0Oo0o000oO = "Please Wait"
 oO0o00oOOooO0 ( i1iiIII111ii , Ii1i1i1i1I1Ii , iiIi1IIiI , i1oO0OO0 , o0O0Oo00 , O0Oo0o000oO , o0iiiI1I1iIIIi1 , IiiI1iiiiI1iI )
 time . sleep ( 1 )
 OOOoO000 = xbmc . translatePath ( os . path . join ( iIi1 , o00O00oO00 + '_guisettings.zip' ) )
 oOOOO = zipfile . ZipFile ( OOOoO000 , mode = 'w' )
 try :
  oOOOO . write ( xbmc . translatePath ( os . path . join ( i1iiIII111ii , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oOOOO . close ( )
 if o0OOo00OoO == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i11iiI1111 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + Ii1i1i1i1I1Ii + '[/COLOR]' )
  if 49 - 49: IIiIiII11i . oo0OO . Ii % iIIIIii1
def oO0o00oOOooO0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 i11i1iiI1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oO0oOOoo00000 = len ( sourcefile )
 oOo00 = [ ]
 i1iI11i1IIi = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for ii1IIi111 , iI1 , OoOo00o0OO in os . walk ( sourcefile ) :
  for file in OoOo00o0OO :
   i1iI11i1IIi . append ( file )
 ii1IIIIiI11 = len ( i1iI11i1IIi )
 for ii1IIi111 , iI1 , OoOo00o0OO in os . walk ( sourcefile ) :
  iI1 [ : ] = [ iI1IIIii for iI1IIIii in iI1 if iI1IIIii not in exclude_dirs ]
  OoOo00o0OO [ : ] = [ i11i1iiiII for i11i1iiiII in OoOo00o0OO if i11i1iiiII not in exclude_files ]
  for file in OoOo00o0OO :
   oOo00 . append ( file )
   I1i11ii11 = len ( oOo00 ) / float ( ii1IIIIiI11 ) * 100
   Oo0oO0ooo . update ( int ( I1i11ii11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OO00O0oOO = os . path . join ( ii1IIi111 , file )
   if not 'temp' in iI1 :
    if not 'plugin.program.originwizard' in iI1 :
     import time
     Ii1iI111 = '01/01/1980'
     O0oooo00o0Oo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OO00O0oOO ) ) )
     if O0oooo00o0Oo > Ii1iI111 :
      i11i1iiI1i . write ( OO00O0oOO , OO00O0oOO [ oO0oOOoo00000 : ] )
 i11i1iiI1i . close ( )
 Oo0oO0ooo . close ( )
 if 36 - 36: o0Oo0O0Oo00oO / IIiIiII11i / iIIIIii1 / iIIIIii1 + Ii1I
 if 95 - 95: iIIIIii1
def Ooo0oo ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , Oo0oOOo + 'scoob.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , Oo0oOOo + 'scoob.png' , i1iIIi1 , '' )
 if 41 - 41: OOooOOo * O0o0Ooo / OOooOOo % oo0OO
 if 18 - 18: IIiIiII11i . ii % OOooOOo % o0Oo0O0Oo00oO
def II1IiiIii ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( o0ooOooo000oOO ) , 9001 , Oo0oOOo + 'MOVIESv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( o0ooOooo000oOO ) , 9002 , Oo0oOOo + 'TVSHOWSv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , Oo0oOOo + 'ORIGINCARTOON' , i1iIIi1 , '' )
 if 84 - 84: oo0OO % ooOoO0O00
 if 70 - 70: I1ii11iIi11i . ii - O0o0O0O0ooO0
 if 30 - 30: Ii1I % oOo0O0Ooo
 if 89 - 89: IiI11iII1 + ii + IiI11iII1 * ooOoO0O00 + iI11I1II1I1I % O0o0Ooo
def oOo0oO ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9xdWlja3NpbHZlcm11c2ljLw==' ) ) , 1006 , Oo0oOOo + 'Quicksilver.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC CHANNELS[/COLOR]' , str ( o0ooOooo000oOO ) , 30031 , Oo0oOOo + 'MusicChannels.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , Oo0oOOo + 'UKRadio.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']WORLD RADIO[/COLOR]' , str ( o0ooOooo000oOO ) , 1013 , Oo0oOOo + 'WorldRadio.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , Oo0oOOo + 'Concerts.png' , i1iIIi1 , '' )
  if 5 - 5: OoO0O0 - OoO0O0 . I1ii11iIi11i + OOooOOo - OoO0O0 . oo0OO
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , Oo0oOOo + 'MusicVideos.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( o0ooOooo000oOO ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , Oo0oOOo + 'Music.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC SEARCH[/COLOR]' , str ( o0ooOooo000oOO ) , 1111 , Oo0oOOo + 'MusicSearch.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , Oo0oOOo + 'KodibleAudioBooks.png' , i1iIIi1 , '' )
 if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % O0o0Ooo
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 12 - 12: iI11I1II1I1I
def iIi1i ( ) :
 iiiI1I11i1 ( )
 if 4 - 4: IiI11iII1 / Ii / OoO0O0
 o0O0OOO0Ooo ( 'DELETE CACHE' , 'url' , 14 , Oo0oOOo + 'DeleteCache.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'DELETE PACKAGES' , 'url' , 6 , Oo0oOOo + 'DeletePackages.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'FORCE REFRESH' , 'url' , 10 , Oo0oOOo + 'ForceRefresh.png' , i1iIIi1 , 'Force Refresh All Repos' )
 if 91 - 91: iI11I1II1I1I % I11i . iI11I1II1I1I % ooOoO0O00 / IIiIiII11i * OOooOOo
 o0O0OOO0Ooo ( 'CHECK MY IP' , 'url' , 12 , Oo0oOOo + 'CheckMyIP.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , Oo0oOOo + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , i1iIIi1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ADVANCED SETTINGS XML[/COLOR]' , str ( o0ooOooo000oOO ) , 4 , Oo0oOOo + 'AdvancedSettingXML.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']URL FIXES[/COLOR]' , str ( o0ooOooo000oOO ) , 20 , Oo0oOOo + 'URLFixes.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 10 - 10: IIiIiII11i . O0o0O0O0ooO0
 if 32 - 32: o0Oo0O0Oo00oO . iIIIIii1 . ii - oO0o + oo0OO
def iI1Ii11111iIi ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , Oo0oOOo + 'repos.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEW[/COLOR]' , str ( o0ooOooo000oOO ) , 22 , Oo0oOOo + 'NEW.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']IPTV[/COLOR]' , str ( o0ooOooo000oOO ) , 23 , Oo0oOOo + 'IPTV.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']VIDEO[/COLOR]' , str ( o0ooOooo000oOO ) , 24 , Oo0oOOo + 'VIDEO.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SPORTS[/COLOR]' , str ( o0ooOooo000oOO ) , 25 , Oo0oOOo + 'SPORTS.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( o0ooOooo000oOO ) , 26 , Oo0oOOo + 'KIDS.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( o0ooOooo000oOO ) , 27 , Oo0oOOo + 'MUSIC.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']PROGRAMS[/COLOR]' , str ( o0ooOooo000oOO ) , 28 , Oo0oOOo + 'PROGRAMS.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']XXX[/COLOR]' , 'URL' , 29 , Oo0oOOo + 'XXX.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 88 - 88: O0o0O0O0ooO0
 if 19 - 19: IIiIiII11i * iIIIIii1 + o0Oo0O0Oo00oO
def O0ooO00oO ( ) :
 iiiI1I11i1 ( )
 o0O0OOO0Ooo ( 'CHECK ADVANCED XML' , str ( o0ooOooo000oOO ) , 8 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'MUCKYS XML' , str ( o0ooOooo000oOO ) + '/wizard/muckys.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( '0CACHE XML' , str ( o0ooOooo000oOO ) + '/wizard/0cache.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'MIKEY1234 XML' , str ( o0ooOooo000oOO ) + '/wizard/mikey.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'TUXENS XML' , str ( o0ooOooo000oOO ) + '/wizard/tuxens.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'P2P RECOMMENDED XML1' , str ( o0ooOooo000oOO ) + '/wizard/p2p1.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'P2P RECOMMENDED XML2' , str ( o0ooOooo000oOO ) + '/wizard/p2p2.xml' , 7 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'DELETE XML' , str ( o0ooOooo000oOO ) , 11 , Oo0oOOo + 'XML.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 36 - 36: OoO0O0
def O0oii111 ( ) :
 iiiI1I11i1 ( )
 o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']My Local Zip[/COLOR]' , I11 , 48 , Oo0oOOo + 'MyLocalZIP.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']My Online Zip[/COLOR]' , i11 , 43 , Oo0oOOo + 'MyOnlineZip.png' , i1iIIi1 , '' )
 if 58 - 58: OoO0O0 * I11i + o0o00Oo0O % OoO0O0
def iI1I1iIi11 ( ) :
 iiiI1I11i1 ( )
 o0O0OOO0Ooo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( o0ooOooo000oOO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , Oo0oOOo + 'FTV4.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( o0ooOooo000oOO ) + '/wizard/customftv/settings.xml' , 17 , Oo0oOOo + 'FTV3.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , Oo0oOOo + 'FTV1.png' , i1iIIi1 , '' )
 o0O0OOO0Ooo ( 'RESET FTV DATABASE' , 'url' , 18 , Oo0oOOo + 'FTV2.png' , i1iIIi1 , '' )
 if 87 - 87: OOooOOo
 if 25 - 25: ooOoO0O00 . oO0o - OOooOOo / oO0o % oO0o * iI11I1II1I1I
 if 50 - 50: oO0o . Ii - oo0OO . oo0OO
def I11I ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SKINS[/COLOR]' , str ( o0ooOooo000oOO ) , 33 , Oo0oOOo + 'Skins.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ARTWORK PACKS[/COLOR]' , str ( o0ooOooo000oOO ) , 34 , Oo0oOOo + 'ArtworkPacks.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIII111ii , 35 , Oo0oOOo + 'CreateUniversalPath.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 6 - 6: Ii1I + oo0OO
def Ii1iI11iI1 ( url ) :
 OOOOi11i1 = O0 ( i11I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 5 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 79 - 79: oO0o . O0o0O0O0ooO0 * o0Oo0O0Oo00oO - OoO0O0 + OOO00O
def ii11II1i ( ) :
 iiiI1I11i1 ( )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']GOTHAM SKINS[/COLOR]' , str ( o0ooOooo000oOO ) , 36 , Oo0oOOo + 'GothamSkins.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']HELIX SKINS[/COLOR]' , str ( o0ooOooo000oOO ) , 37 , Oo0oOOo + 'HelixSkins.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']ISENGAARD SKINS[/COLOR]' , i1iiIII111ii , 38 , Oo0oOOo + 'IsengaardSkins.png' , i1iIIi1 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 58 - 58: I1ii11iIi11i . iIIIIii1 - I1ii11iIi11i - IiI11iII1 * o0Oo0O0Oo00oO
def IIiI11i1111Ii ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + o00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 70 - 70: I1ii11iIi11i . OOooOOo
def O00o00O ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + ii1iii11i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 4 - 4: iIIIIii1 . iIIIIii1 % Ii1I % o0Oo0O0Oo00oO / o0Oo0O0Oo00oO
def II11iIiiI1111 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + OOO00oo0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 38 - 38: iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
def ooo ( url ) :
 OOOOi11i1 = O0 ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 94 - 94: OOooOOo - I1ii11iIi11i - oOo0O0Ooo % ooOoO0O00
def iIIiiiiI ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + I111i1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 40 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 62 - 62: OoO0O0 * IiI11iII1 / I1ii11iIi11i * I11i
def II1Ii1iI1i1 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + o0OoO000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 5 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 94 - 94: OOooOOo . o0o00Oo0O / o0Oo0O0Oo00oO . Ii1I - ooOoO0O00
def iIi1III1I ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']APK (Android only)[/COLOR]' , str ( o0ooOooo000oOO ) , 2 , Oo0oOOo + 'APKAndroidOnly.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']APK Search[/COLOR]' , str ( o0ooOooo000oOO ) , 30038 , Oo0oOOo + 'APKSearch.png' , i1iIIi1 , '' )
 if 71 - 71: IiI11iII1
def Ii1II ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy5hcGtjcmFmdC5jb20v' ) )
 OO0oOO0O = re . compile ( 'href="(.+?)">Android Apps</a>' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'href="(.+?)">Android Games</a>' ) . findall ( oOoO0 )
 ooO0O0o0 = re . compile ( 'href="(.+?)">Wallpapers</a>' ) . findall ( oOoO0 )
 OO0OOooOO0 = re . compile ( 'href="(.+?)">Widgets</a>' ) . findall ( oOoO0 )
 for O0o in OO0oOO0O :
  IIIIIii1ii11 ( 'Android Apps' , O0o , 30035 , Oo0oOOo + 'apps.png' )
 for O0o in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'Android Games' , O0o , 30035 , Oo0oOOo + 'GAMES.png' )
 for O0o in ooO0O0o0 :
  IIIIIii1ii11 ( 'Wallpapers' , O0o , 30036 , Oo0oOOo + 'wallpapers.png' )
 for O0o in OO0OOooOO0 :
  IIIIIii1ii11 ( 'Widgets' , O0o , 30036 , Oo0oOOo + 'widgets.png' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
def OOOooo0OooOoO ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if 'cat' in url :
   IIIIIii1ii11 ( IiiiiI1i1Iii , url , 30036 , Oo0oOOo + 'APK.png' )
def oOoOOOo ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( 'src="(.+?)".+?href="(.+?)" title ="(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'class="pagination_next"><a href="(.+?)">»</a></li>' ) . findall ( oOoO0 )
 for IiIi1I1 , url , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , url , 30037 , IiIi1I1 )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'NEXT PAGE' , url , 30036 , Oo0oOOo + 'APK.png' )
def ii1I ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '>Direct Download : <a  href="(.+?)">' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  o0OOoOoO00 ( url )
def o0OOoOoO00 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  I1iii ( url )
def oOO0OO0O ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOoO00O0 = 'http://www.apkcraft.com/search/app/?search_text=' + ( oOoO ) . replace ( ' ' , '+' ) + '&search_type=1'
 OOIi1iI111II1I1 = oOoO00O0 . lower ( )
 oOoOOOo ( OOIi1iI111II1I1 )
 if 78 - 78: o0Oo0O0Oo00oO / IIiIiII11i % OOooOOo
def I1iii ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( oO00OoOO , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I11IIiIiI = os . path . join ( iI11 , IiiiiI1i1Iii + '.apk' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 5 - 5: I1ii11iIi11i * OOooOOo
def ii1I11iIiIII1 ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I11IIiIiI = os . path . join ( iI11 , IiiiiI1i1Iii + '.mp4' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 52 - 52: I11i * iIIIIii1 + OOooOOo
 if 49 - 49: iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 - ii
def Ii1 ( name , url , description ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 I11IIiIiI = os . path . join ( iI11 , name )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 ooo0ooO = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ooo0ooO
 print '======================================='
 extract . all ( I11IIiIiI , ooo0ooO , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 17 - 17: Ii1I . IIiIiII11i . OOO00O / Ii1I
 if 57 - 57: O0o0Ooo
def oO0 ( url ) :
 OOOOi11i1 = O0 ( o0ooOooo000oOO + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 5 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'INFO' )
 if 87 - 87: oo0OO % o0Oo0O0Oo00oO
 if 83 - 83: IIiIiII11i - O0o0Ooo
def iiIii1IIi ( url ) :
 OOOOi11i1 = O0 ( o0ooOooo000oOO + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 30015 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 10 - 10: Ii - I11i % iI11I1II1I1I
def i111IIIiI ( url , iconimage , fanart ) :
 OOOOi11i1 = O0 ( url )
 o0OOo0o0O0O = url
 IiIi1I1 = iconimage
 fanart = fanart
 OO0oOO0O = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( OOOOi11i1 )
 for iI1i11 , IiiiiI1i1Iii in OO0oOO0O :
  if '.mp4' in IiiiiI1i1Iii :
   o0O0OOO0Ooo ( 'Watch VIDEO' , url + '/' + iI1i11 , 222 , IiIi1I1 , fanart , '' )
  if 'description' in IiiiiI1i1Iii :
   o0O0OOO0Ooo ( 'Read Description' , url + '/' + iI1i11 , 30017 , IiIi1I1 , fanart , '' )
  if 'images' in IiiiiI1i1Iii :
   iiIiII1 ( 'View Images' , url + '/' + iI1i11 , 30018 , IiIi1I1 , fanart , '' )
  if 'url' in IiiiiI1i1Iii :
   o0O0OOO0Ooo ( 'Install Build On Android' , url + '/' + iI1i11 , 30016 , IiIi1I1 , fanart , '' )
  if 'url' in IiiiiI1i1Iii :
   o0O0OOO0Ooo ( 'Install Build On Pc' , url + '/' + iI1i11 , 30019 , IiIi1I1 , fanart , '' )
 i1Iii1i1I ( 'movies' , 'INFO' )
 if 23 - 23: I1ii11iIi11i % O0o0Ooo - OoO0O0 % iI11I1II1I1I . OOooOOo
def I1Ii1 ( url ) :
 OOOOi11i1 = O0 ( url )
 OO0oOO0O = re . compile ( 'url="(.+?)"' ) . findall ( OOOOi11i1 )
 for url in OO0oOO0O :
  OoOooOo0O ( url )
  if 37 - 37: o0Oo0O0Oo00oO % oO0o
def oOooO0 ( url ) :
 OOOOi11i1 = O0 ( url )
 OO0oOO0O = re . compile ( 'url="(.+?)"' ) . findall ( OOOOi11i1 )
 for url in OO0oOO0O :
  O0O0ooOOO ( url )
  if 70 - 70: OOO00O . o0o00Oo0O . IiI11iII1 . o0o00Oo0O + ooOoO0O00
def i1II1I ( url ) :
 OOOOi11i1 = O0 ( url )
 OO0oOO0O = re . compile ( 'desc="(.+?)"' ) . findall ( OOOOi11i1 )
 for OOoO0ooOO in OO0oOO0O :
  OOOO0oo0 ( 'Description:' , OOoO0ooOO )
  if 24 - 24: ooOoO0O00 . Ii
def IIIII1iii11 ( url ) :
 OOOOi11i1 = O0 ( url )
 url = url
 OO0oOO0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOOOi11i1 )
 for iI1i11 , IiiiiI1i1Iii in OO0oOO0O :
  if 'png' in IiiiiI1i1Iii :
   o0O0OOO0Ooo ( 'image' , '' , '' , url + '/' + iI1i11 , url + '/' + iI1i11 , '' )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 35 - 35: oo0OO / IiI11iII1 / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . IiI11iII1
def O0O00O000OOO ( name , url , description ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I11IIiIiI = os . path . join ( iI11 , name + '.zip' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 iIOo0O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIOo0O
 print '======================================='
 extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iiIiI1i1 ( )
 if 1 - 1: o0o00Oo0O / O0o0O0O0ooO0 % IiI11iII1 . I1ii11iIi11i + iIIIIii1
 if 27 - 27: IiI11iII1 % ii + iIIIIii1 % ooOoO0O00 / oo0OO / ii
def O0O0ooOOO ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11IIiIiI = os . path . join ( iI11 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 iIOo0O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIOo0O
 print '======================================='
 extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
 III1IiIII1 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O00ooOo ( )
 if 80 - 80: I11i - OoO0O0 + ii
def OoOooOo0O ( url ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11IIiIiI = os . path . join ( iI11 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 iIOo0O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIOo0O
 print '======================================='
 extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
 III1IiIII1 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 98 - 98: OoO0O0 + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + O0o0Ooo
def IiiIi ( name , url , description ) :
 iIOo0O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 I11IIiIiI = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iIOo0O
 print '======================================='
 extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 10 - 10: oO0o / I1ii11iIi11i
 if 15 - 15: O0o0O0O0ooO0 . OOooOOo / O0o0O0O0ooO0 * O0o0Ooo - oOo0O0Ooo % Ii1I
def O00ooOo ( ) :
 OO0O000 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OO0O000 == 0 :
  return
 elif OO0O000 == 1 :
  pass
 oo0OOOOOO0 = i11Ii1I1I11I ( )
 print "Platform: " + str ( oo0OOOOOO0 )
 if oo0OOOOOO0 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oo0OOOOOO0 == 'linux' :
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oo0OOOOOO0 == 'android' :
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "Your system has been detected as Android, you " , "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Pulling the power cable is the simplest method to force close." )
 elif oo0OOOOOO0 == 'windows' :
  print "############   try windows force close  #################"
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
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "Your platform could not be detected so just pull the power cable." )
  if 29 - 29: ii . oOo0O0Ooo % Ii1I - O0o0O0O0ooO0
def i11Ii1I1I11I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) :
  return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) :
  return 'ios'
  if 8 - 8: ooOoO0O00
  if 32 - 32: oo0OO / IIiIiII11i
  if 45 - 45: Ii1I + oO0o * Ii / OoO0O0 % O0o0Ooo * o0o00Oo0O
def i1o0oooO ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooOo , iI1 , OoOo00o0OO in os . walk ( url ) :
  for file in OoOo00o0OO :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooOO0oO0oo00o = open ( ( os . path . join ( ooOo , file ) ) ) . read ( )
    o0oO0OoO0 = ooOO0oO0oo00o . replace ( i1iiIII111ii , 'special://home/' )
    i11i1iiiII = open ( ( os . path . join ( ooOo , file ) ) , mode = 'w' )
    i11i1iiiII . write ( str ( o0oO0OoO0 ) )
    i11i1iiiII . close ( )
 O00ooOo ( )
 if 70 - 70: oo0OO - oo0OO
def OoOO0OOoo ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , 'http://www.listenlive.eu/' + O0o , 10111113 , Oo0oOOo + 'radio.png' )
def IIIi11IiIiii ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , url , 222 , Oo0oOOo + 'radio.png' )
  if 24 - 24: O0o0O0O0ooO0 * IIiIiII11i % O0o0O0O0ooO0 % iIIIIii1 + ii
def IiIiiiIii ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.toonjet.com/' + O0o , 8051 , Oo0oOOo + 'classictoons.png' )
def IiiIIi11I1 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( oOoO0 )
 for url , IiIi1I1 in OO0oOO0O :
  if 'ol.gif' in IiIi1I1 :
   pass
  elif 'link_block_' in IiIi1I1 :
   pass
  elif '.png' in IiIi1I1 :
   pass
  else :
   IIIIIii1ii11 ( ( IiIi1I1 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , Oo0oOOo + 'vod.png' )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , Oo0oOOo + 'Next.png' )
def Ii1iIi111i1i1 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , Oo0oOOo + 'classictoons.png' )
  if 45 - 45: OOooOOo . I11i % OOooOOo * oOo0O0Ooo % oOo0O0Ooo
  if 63 - 63: IiI11iII1
def oo00ooOoo ( ) :
 iii1IIIiiiI ( 'Audio Books' , '' , 30011 , Oo0oOOo + 'AudioBooks.png' , Oo0oOOo + 'AudioBooks.png' , '' )
 iii1IIIiiiI ( 'Kids Audio Books' , '' , 30006 , Oo0oOOo + 'KidsAudioBooks.png' , Oo0oOOo + 'KidsAudioBooks.png' , '' )
 if 94 - 94: o0o00Oo0O - O0o0Ooo - iI11I1II1I1I % OOO00O / o0Oo0O0Oo00oO % O0o0O0O0ooO0
def iIi1IIi1ii ( ) :
 iii1IIIiiiI ( 'All' , '' , 30001 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
 iii1IIIiiiI ( 'Popular' , '' , 30012 , Oo0oOOo + 'POPULARv.png' , Oo0oOOo + 'POPULARv.png' , '' )
 iii1IIIiiiI ( 'Search' , '' , 30013 , Oo0oOOo + 'Search.png' , Oo0oOOo + 'Search.png' , '' )
 if 35 - 35: O0o0O0O0ooO0 / Ii1I * ii . IIiIiII11i / I1ii11iIi11i
def Iii11i ( ) :
 O0OOO0OOoO0O = O0 ( II11iiii1Ii + 'books' + OooO0 )
 OO0oOO0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , O0o , OOOOOOoO in OO0oOO0O :
  if 'Parent' in IiiiiI1i1Iii :
   pass
  elif '2' in OOOOOOoO :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 12 - 12: O0o0O0O0ooO0 . iIIIIii1 . OOooOOo / o0o00Oo0O
def OO0oOOo0o ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0OOO0OOoO0O = O0 ( II11iiii1Ii + 'books' + OooO0 )
 OO0oOO0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , O0o , OOOOOOoO in OO0oOO0O :
  if oOoO in IiiiiI1i1Iii . lower ( ) :
   if '1' in OOOOOOoO :
    iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOOOOOoO :
    iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOOOOOoO :
    iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30009 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
    if 50 - 50: O0o0O0O0ooO0 . Ii1I . oO0o * O0o0Ooo + IIiIiII11i % Ii
    if 8 - 8: OOO00O * o0o00Oo0O
def OOoO ( ) :
 O0OOO0OOoO0O = O0 ( II11iiii1Ii + 'books' + OooO0 )
 OO0oOO0O = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , O0o , OOOOOOoO in OO0oOO0O :
  if '1' in OOOOOOoO :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 3010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOOOOOoO :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOOOOOoO :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0o , 30009 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 18 - 18: iI11I1II1I1I + I1ii11iIi11i - OoO0O0 + ii * ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: OOO00O . I1ii11iIi11i + oOo0O0Ooo
def o0O0OO ( url ) :
 iI1i11 = url
 O0OOO0OOoO0O = O0 ( url )
 oOiIi1IIIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in oOiIi1IIIi1 :
  if 'mp3' in IiiiiI1i1Iii :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) , iI1i11 + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in IiiiiI1i1Iii :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) , iI1i11 + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in IiiiiI1i1Iii :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) , iI1i11 + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in IiiiiI1i1Iii :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iI1i11 + url , 30009 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 22 - 22: IIiIiII11i * oO0o * O0o0Ooo + Ii1I * I11i
   if 100 - 100: ooOoO0O00 / iIIIIii1
   if 3 - 3: IIiIiII11i % Ii1I - ii * I1ii11iIi11i . iI11I1II1I1I
def I1iI ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 iI1i11 = url
 OO0oOO0O = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if 'Parent' in IiiiiI1i1Iii :
   pass
  elif '.db' in IiiiiI1i1Iii :
   pass
  elif '.jpg' in IiiiiI1i1Iii :
   pass
  elif '.html' in IiiiiI1i1Iii :
   pass
  elif '.doc' in IiiiiI1i1Iii :
   pass
  elif 'mp3' in IiiiiI1i1Iii :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iI1i11 + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in IiiiiI1i1Iii :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iI1i11 + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  else :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iI1i11 + url , 30010 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 92 - 92: o0Oo0O0Oo00oO % O0o0O0O0ooO0 / Ii1I % Ii1I * oOo0O0Ooo
   if 74 - 74: o0o00Oo0O . oOo0O0Ooo % oO0o % iIIIIii1
def oOo0OooOo ( ) :
 iii1IIIiiiI ( 'A-Z' , '' , 30007 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
 iii1IIIiiiI ( 'All' , '' , 30003 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
 iii1IIIiiiI ( 'Search' , '' , 30014 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
 if 51 - 51: O0o0Ooo . I1ii11iIi11i
def IiiIiiIi ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 OO0oOO0O = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for O0o , IiIi1I1 in OO0oOO0O :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + O0o + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IiIi1I1 :
   pass
  else :
   iii1IIIiiiI ( IiIi1I1 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( O0o ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IiIi1I1 + '.gif' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 40 - 40: I11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: iI11I1II1I1I
 if 56 - 56: ii - O0o0Ooo - ooOoO0O00
def I1i1I ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if '</a>' in IiiiiI1i1Iii :
   pass
  elif '(' in IiiiiI1i1Iii :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: Ii - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 99 - 99: oO0o * Ii . ii % I1ii11iIi11i
def Oo0Oo0oOooOoOo ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OO0oOO0O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if oOoO in IiiiiI1i1Iii . lower ( ) :
   if '</a>' in IiiiiI1i1Iii :
    pass
   elif '(' in IiiiiI1i1Iii :
    iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0o , 30005 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   else :
    iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0o , 30004 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
    if 49 - 49: OoO0O0 . Ii1I . Ii - IIiIiII11i / o0Oo0O0Oo00oO
    if 62 - 62: OoO0O0
def i1I1i ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 OO0oOO0O = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if '</a>' in IiiiiI1i1Iii :
   pass
  elif '(' in IiiiiI1i1Iii :
   iii1IIIiiiI ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0o , 30005 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0o , 30004 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 87 - 87: I1ii11iIi11i / o0o00Oo0O * iIIIIii1 / I11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: IiI11iII1 + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
 if 16 - 16: oo0OO + OOO00O / I11i
def O00oOoo0OoO0 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( O0OOO0OOoO0O )
 for url in OO0oOO0O :
  iI1i11 = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iI1i11 )
  if 62 - 62: ooOoO0O00 / OOO00O . oOo0O0Ooo * I11i
def i11i1Ii1 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  if '<p align' in IiiiiI1i1Iii :
   pass
  elif '&nbsp;' in IiiiiI1i1Iii :
   pass
  else :
   iiIiII1 ( ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , Oo0oOOo + 'KodibleAudioBooks.png' , Oo0oOOo + 'KodibleAudioBooks.png' , '' )
   if 98 - 98: IiI11iII1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: IiI11iII1 - iI11I1II1I1I
 if 32 - 32: o0Oo0O0Oo00oO % oO0o * oO0o + iIIIIii1 * IIiIiII11i * o0Oo0O0Oo00oO
def iIiIii1I1II ( ) :
 O0OOO0OOoO0O = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 OO0oOO0O = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'ongoing' in O0o :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 21005 , Oo0oOOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in O0o :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 21005 , Oo0oOOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in O0o :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 21005 , Oo0oOOo + 'Disney.png' , '' , '' )
  if 'genre' in O0o :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 21005 , Oo0oOOo + 'Genre.png' , '' , '' )
  if 'years' in O0o :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 21005 , Oo0oOOo + 'Years.png' , '' , '' )
def O0Oooo ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oO000 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 21006 , IiIi1I1 , IiIi1I1 , IiiiiI1i1Iii )
 for url , IiiiiI1i1Iii in oO000 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 21005 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 21005 , Oo0oOOo + 'Next.png' , '' , '' )
def I1IiIiIi1IiI1 ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( '<li><a href="([^"]*)" >(.+?)</a></li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 O0OO0o0OO0OO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOo0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O0OOO0OOoO0O )
 III1i111i = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 21007 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
 for url in oOo0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , 'http:' + url , 222 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
 for url , IiiiiI1i1Iii in O0OO0o0OO0OO :
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 222 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
 else :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
def iI1i ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 222 , Oo0oOOo + 'watchcartoons.png' , '' , '' )
  if 46 - 46: IiI11iII1 % o0Oo0O0Oo00oO
def oOO ( ) :
 IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 20001 , Oo0oOOo + 'ORIGINCARTOON.png' )
 IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , Oo0oOOo + 'ORIGINCARTOON.png' )
 if 53 - 53: I11i % I1ii11iIi11i * I1ii11iIi11i
def OOo0o0Oo ( ) :
 IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , Oo0oOOo + 'ORIGINCARTOON.png' )
 IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , Oo0oOOo + 'ORIGINCARTOON.png' )
 if 77 - 77: iI11I1II1I1I - ooOoO0O00 . oo0OO
def iIi1iIIIiIiI ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if '?c=' in url :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , Oo0oOOo + 'ORIGINCARTOON.png' )
   if 62 - 62: Ii % OoO0O0 . iIIIIii1 . OoO0O0
def ooOo0O0O0oOO0 ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , iIiIIi , IiiiiI1i1Iii in OO0oOO0O :
  if 'Genre' in url :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , Oo0oOOo + 'ORIGINCARTOON.png' )
   if 14 - 14: I11i / OoO0O0 - iI11I1II1I1I - oo0OO % OOO00O
def I1iIiI1IiIIII ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , iIiIIi , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iIiIIi )
  if 18 - 18: OOO00O % Ii . iI11I1II1I1I - O0o0O0O0ooO0
def OOOOoo ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , iIiIIi , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , iIiIIi )
  if 29 - 29: I11i / Ii / oOo0O0Ooo % oo0OO % Ii
  if 18 - 18: OoO0O0 + IiI11iII1
  if 80 - 80: oo0OO + I11i * o0Oo0O0Oo00oO + oO0o
  if 75 - 75: O0o0Ooo / I11i / OoO0O0 / iIIIIii1 % OOO00O + IIiIiII11i
  if 4 - 4: O0o0O0O0ooO0 - I1ii11iIi11i - iIIIIii1 - O0o0Ooo % Ii / oO0o
def i1iii11 ( ) :
 if 92 - 92: OOooOOo . ii - IiI11iII1
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , Oo0oOOo + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Cartoons[/COLOR]' , '' , 10005 , Oo0oOOo + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 if 74 - 74: iI11I1II1I1I % O0o0O0O0ooO0 * OoO0O0 * iI11I1II1I1I
def oOo00OoOoO ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 OO0oOO0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if oOoO in IiiiiI1i1Iii . lower ( ) :
   if 'Dad!' in IiiiiI1i1Iii :
    pass
   elif 'Family Guy' in IiiiiI1i1Iii :
    pass
   elif '2 Stupid' in IiiiiI1i1Iii :
    pass
   elif 'The Zelfs' in IiiiiI1i1Iii :
    pass
   elif 'A Clone' in IiiiiI1i1Iii :
    pass
   elif 'A.T.O.M' in IiiiiI1i1Iii :
    pass
   elif 'Almost Naked' in IiiiiI1i1Iii :
    pass
   elif 'Angry Kid' in IiiiiI1i1Iii :
    pass
   elif 'Annoying Orange' in IiiiiI1i1Iii :
    pass
   elif 'Aqua Teen' in IiiiiI1i1Iii :
    pass
   elif 'Assy Mcgee' in IiiiiI1i1Iii :
    pass
   elif 'Astroblast' in IiiiiI1i1Iii :
    pass
   elif 'Atomic Betty' in IiiiiI1i1Iii :
    pass
   elif 'Axe Cop' in IiiiiI1i1Iii :
    pass
   elif 'Baby Playpen' in IiiiiI1i1Iii :
    pass
   elif 'Beavis and Butt' in IiiiiI1i1Iii :
    pass
   elif 'Celebrity Deathmatch' in IiiiiI1i1Iii :
    pass
   elif 'Clerks The' in IiiiiI1i1Iii :
    pass
   elif 'Crapston Villas' in IiiiiI1i1Iii :
    pass
   elif 'Duckman:' in IiiiiI1i1Iii :
    pass
   elif 'Stripperella' in IiiiiI1i1Iii :
    pass
   elif 'Vixen' in IiiiiI1i1Iii :
    pass
   else :
    iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 10006 , Oo0oOOo + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 66 - 66: oOo0O0Ooo - iIIIIii1
def iiIii ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if 'Dad!' in IiiiiI1i1Iii :
   pass
  elif 'Family Guy' in IiiiiI1i1Iii :
   pass
  elif '2 Stupid' in IiiiiI1i1Iii :
   pass
  elif 'The Zelfs' in IiiiiI1i1Iii :
   pass
  elif 'A Clone' in IiiiiI1i1Iii :
   pass
  elif 'A.T.O.M' in IiiiiI1i1Iii :
   pass
  elif 'Almost Naked' in IiiiiI1i1Iii :
   pass
  elif 'Angry Kid' in IiiiiI1i1Iii :
   pass
  elif 'Annoying Orange' in IiiiiI1i1Iii :
   pass
  elif 'Aqua Teen' in IiiiiI1i1Iii :
   pass
  elif 'Assy Mcgee' in IiiiiI1i1Iii :
   pass
  elif 'Astroblast' in IiiiiI1i1Iii :
   pass
  elif 'Atomic Betty' in IiiiiI1i1Iii :
   pass
  elif 'Axe Cop' in IiiiiI1i1Iii :
   pass
  elif 'Baby Playpen' in IiiiiI1i1Iii :
   pass
  elif 'Beavis and Butt' in IiiiiI1i1Iii :
   pass
  elif 'Celebrity Deathmatch' in IiiiiI1i1Iii :
   pass
  elif 'Clerks The' in IiiiiI1i1Iii :
   pass
  elif 'Crapston Villas' in IiiiiI1i1Iii :
   pass
  elif 'Duckman:' in IiiiiI1i1Iii :
   pass
  elif 'Stripperella' in IiiiiI1i1Iii :
   pass
  elif 'Vixen' in IiiiiI1i1Iii :
   pass
  else :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 10006 , Oo0oOOo + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: oo0OO
def ooo0oo ( url ) :
 oOoO0 = O0 ( url )
 oOiIi1IIIi1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oOoO0 )
 for IiIi1I1 in oOiIi1IIIi1 :
  IIiI1i = IiIi1I1
 ooO0O0o0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oOoO0 )
 for url in ooO0O0o0 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , url , 10006 , Oo0oOOo + 'Next.png' , i1iIIi1 , '' )
 OO0oOO0O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 10007 , IIiI1i )
  if 6 - 6: Ii1I / O0o0O0O0ooO0 - OoO0O0
  if 62 - 62: O0o0Ooo % OoO0O0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: OOooOOo % O0o0O0O0ooO0 . OOooOOo * OoO0O0 + OOooOOo % ooOoO0O00
def I1I1I11Ii ( url , IMAGE ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  print IiiiiI1i1Iii + '     ' + url
  if 'easy' in url :
   ii1Iii1 ( url )
   if 80 - 80: o0Oo0O0Oo00oO - I11i
   if 41 - 41: I11i - I1ii11iIi11i * oOo0O0Ooo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: oO0o % I11i % OoO0O0 / o0o00Oo0O
def ii1Iii1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( "url: '(.+?)'," ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OOOO0o0 ( url )
  if 7 - 7: O0o0O0O0ooO0
  if 78 - 78: OoO0O0 + O0o0O0O0ooO0 . iIIIIii1
  if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
def o0o0O0Oo ( ) :
 if 1 - 1: iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - O0o0O0O0ooO0 % iIIIIii1 + iIIIIii1
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Stand Up[/COLOR]' , '' , 10014 , Oo0oOOo + 'StandUp.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Comedian[/COLOR]' , '' , 10015 , Oo0oOOo + 'SearchComedian.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Others[/COLOR]' , '' , 10017 , Oo0oOOo + 'Others.png' , i1iIIi1 , '' )
 if 24 - 24: oOo0O0Ooo + I1ii11iIi11i + OoO0O0 - ii + I1ii11iIi11i
def O00i1 ( ) :
 O0OOO0OOoO0O = O0 ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  if 'elete' in IiiiiI1i1Iii :
   pass
  else :
   iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 222 , IiIi1I1 )
   if 49 - 49: o0o00Oo0O * oO0o - OOooOOo
def OoOOOOo ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0OOO0OOoO0O = O0 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOOOO0O0oO0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , I11Ii1iI11iI1 , i1iII1IiiIiI1 in OoOOOO0O0oO0 :
  for oOoO in I11Ii1iI11iI1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1III1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for O0o , IiiiiI1i1Iii in i1III1 :
    if 'tube' in O0o :
     pass
    elif 'stage' in O0o :
     iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + I11Ii1iI11iI1 + '   -   ' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiIi1I1 , )
    elif 'vee' in O0o :
     pass
     if 43 - 43: IIiIiII11i % IiI11iII1 . O0o0Ooo % o0o00Oo0O - ii + o0o00Oo0O
def OooO0ooo0 ( ) :
 O0OOO0OOoO0O = O0 ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OoOOOO0O0oO0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , I11Ii1iI11iI1 , i1iII1IiiIiI1 in OoOOOO0O0oO0 :
  i1III1 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for O0o , IiiiiI1i1Iii in i1III1 :
   if 'tube' in O0o :
    pass
   elif 'stage' in O0o :
    iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + I11Ii1iI11iI1 + '   -   ' + IiiiiI1i1Iii + '[/COLOR]' , ( O0o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IiIi1I1 )
   elif 'vee' in O0o :
    pass
    if 2 - 2: ii
    if 60 - 60: oO0o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: OOooOOo % o0Oo0O0Oo00oO
def oo0i1iIIi1II1iiI ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IiIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( O0OOO0OOoO0O )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IiIi ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IiIi :
  OOOO0o0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 31 - 31: I11i % O0o0Ooo + iI11I1II1I1I + Ii * IiI11iII1
  if 45 - 45: OoO0O0 * IiI11iII1 . OOO00O - IiI11iII1 + iIIIIii1
  if 34 - 34: OoO0O0 . I1ii11iIi11i
  if 78 - 78: Ii1I % oOo0O0Ooo / ii % OoO0O0 - O0o0O0O0ooO0
  if 2 - 2: iI11I1II1I1I
  if 45 - 45: ii / Ii
  if 10 - 10: O0o0O0O0ooO0 - oo0OO * iI11I1II1I1I % iI11I1II1I1I * iIIIIii1 - Ii1I
def OoO0O0oO00 ( ) :
 if 33 - 33: o0o00Oo0O
 oo0oO ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iIIi1 , '' )
 oo0oO ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % IiI11iII1 - iI11I1II1I1I % o0o00Oo0O
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 58 - 58: iIIIIii1 + iI11I1II1I1I
def Oo00OO0OO ( ) :
 oo0oO ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 oo0oO ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 85 - 85: I11i % OOO00O . OOooOOo % IiI11iII1 - I1ii11iIi11i
 i1Iii1i1I ( 'movies' , 'MAIN' )
def o0oO0oO0O ( ) :
 if 18 - 18: I1ii11iIi11i
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 IIIiI1ii1IIi = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 55 - 55: O0o0O0O0ooO0 - oO0o
 for o0i1I11iI1iiI in IIIiI1ii1IIi :
  I1 = ooooooO0oo + o0i1I11iI1iiI + OooO0
  O0OOO0OOoO0O = I11iii1Ii ( I1 )
  OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OOO0OOoO0O )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , I11i1II , IiiiiI1i1Iii in OO0oOO0O :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    iioO0o ( IiiiiI1i1Iii , O0o , 222 , oo0O0o00o0O , I11i1II , iIIiIiI1I1 )
    if 50 - 50: O0o0O0O0ooO0 / O0o0O0O0ooO0 + OoO0O0 * OOO00O / Ii1I
    i1Iii1i1I ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 14 - 14: o0Oo0O0Oo00oO % oOo0O0Ooo - iI11I1II1I1I . OoO0O0 + oO0o - IiI11iII1
    if 5 - 5: O0o0O0O0ooO0
def OOiI1 ( ) :
 if 42 - 42: OoO0O0 % oo0OO / oO0o - oo0OO * Ii
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 IIIiI1ii1IIi = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 19 - 19: oo0OO * oOo0O0Ooo % Ii
 for o0i1I11iI1iiI in IIIiI1ii1IIi :
  iiI1Ii1I = ooooooO0oo + o0i1I11iI1iiI + OooO0
  O0OOO0OOoO0O = I11iii1Ii ( iiI1Ii1I )
  OO0oOO0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for IiiiiI1i1Iii , iIIiIiI1I1 , O0o , IiIi1I1 , I11i1II , i11Ii1iIiII in OO0oOO0O :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    oo0oO ( IiiiiI1i1Iii , O0o , i11Ii1iIiII , IiIi1I1 , I11i1II , iIIiIiI1I1 )
    if 81 - 81: O0o0Ooo . ii * OOooOOo % iIIIIii1 . O0o0Ooo
    i1Iii1i1I ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 60 - 60: OoO0O0 / oOo0O0Ooo
    if 78 - 78: O0o0Ooo . iIIIIii1
def iI1i1II ( ) :
 if 14 - 14: OOO00O - iI11I1II1I1I / o0o00Oo0O % iIIIIii1 . OOooOOo
 oOoO0 = O0 ( ooooooO0oo + 'spongemain.php' )
 OO0oOO0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , iIIiIiI1I1 , O0o , IiIi1I1 , I11i1II , i11Ii1iIiII in OO0oOO0O :
  oo0oO ( IiiiiI1i1Iii , O0o , i11Ii1iIiII , IiIi1I1 , I11i1II , iIIiIiI1I1 )
  i1Iii1i1I ( 'movies' , 'MAIN' )
def iI1IIi11i1I1 ( url ) :
 if 60 - 60: O0o0Ooo / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0oOO00 = ( '%s%s' % ( ii11iiIi , url ) )
 OOOOi11i1 = O0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOOi11i1 )
 for url , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in OO0oOO0O :
  iioO0o ( IiiiiI1i1Iii , url , 222 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
  if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
  i1Iii1i1I ( 'movies' , 'MAIN' )
  if 95 - 95: o0Oo0O0Oo00oO % iIIIIii1 . o0o00Oo0O % IiI11iII1
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / O0o0Ooo . OOO00O / ooOoO0O00
  if 12 - 12: Ii1I * ooOoO0O00 * O0o0Ooo
def i1iiI ( url ) :
 if 49 - 49: O0o0Ooo . I11i % oo0OO / o0Oo0O0Oo00oO
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , iIIiIiI1I1 , url , IiIi1I1 , I11i1II , i11Ii1iIiII in OO0oOO0O :
  oo0oO ( IiiiiI1i1Iii , url , i11Ii1iIiII , IiIi1I1 , I11i1II , iIIiIiI1I1 )
  if 95 - 95: o0o00Oo0O * OOooOOo * iIIIIii1 . OOO00O / iI11I1II1I1I
  i1Iii1i1I ( 'movies' , 'MAIN' )
  if 28 - 28: iIIIIii1 + oo0OO - OOO00O / iI11I1II1I1I - oOo0O0Ooo
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * oo0OO * oO0o
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: Ii1I / O0o0O0O0ooO0 % oOo0O0Ooo + iI11I1II1I1I
def iioO0o ( name , url , mode , iconimage , fanart , description ) :
 if 79 - 79: OOooOOo / OOO00O
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIii1 . setProperty ( "Fanart_Image" , fanart )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = False )
 return OOoooooooO
 if 41 - 41: OOooOOo . Ii / O0o0Ooo
def oo0oO ( name , url , mode , iconimage , fanart , description ) :
 if 98 - 98: OOooOOo % IIiIiII11i
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIii1 . setProperty ( "Fanart_Image" , fanart )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = True )
 return OOoooooooO
if 95 - 95: iI11I1II1I1I - IiI11iII1 - OoO0O0 + IiI11iII1 % Ii1I . oOo0O0Ooo
if 41 - 41: o0o00Oo0O + oo0OO . ooOoO0O00 - IIiIiII11i * I11i . oO0o
if 68 - 68: I11i
if 20 - 20: IiI11iII1 - IiI11iII1
if 37 - 37: iIIIIii1
if 37 - 37: I1ii11iIi11i / iIIIIii1 * o0o00Oo0O
if 73 - 73: O0o0O0O0ooO0 * O0o0O0O0ooO0 / OOO00O
if 43 - 43: Ii1I . ooOoO0O00 . iIIIIii1 + o0o00Oo0O * o0Oo0O0Oo00oO * o0o00Oo0O
if 41 - 41: Ii1I + o0Oo0O0Oo00oO % ii . Ii1I + O0o0O0O0ooO0 . O0o0O0O0ooO0
if 31 - 31: Ii + IIiIiII11i . O0o0O0O0ooO0 * OOooOOo
if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
if 87 - 87: OoO0O0 + I11i . O0o0O0O0ooO0 - ii
if 6 - 6: iI11I1II1I1I * ii
if 28 - 28: I1ii11iIi11i * I11i / IiI11iII1
if 52 - 52: o0o00Oo0O / I11i % O0o0O0O0ooO0 * oOo0O0Ooo % OoO0O0
def o0oOOOO0 ( string ) :
 if O000OO0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 11 - 11: ooOoO0O00
def I1III1iIi ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoO00O0 = [ ]
 try :
  if 35 - 35: O0o0O0O0ooO0 . iIIIIii1 / ooOoO0O00 . iI11I1II1I1I . o0o00Oo0O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  o0oOOOO0 ( 'Making Favorites File' )
  OoO00O0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ooOO0oO0oo00o = open ( iIi1ii1I1 , "w" )
  ooOO0oO0oo00o . write ( json . dumps ( OoO00O0 ) )
  ooOO0oO0oo00o . close ( )
 else :
  o0oOOOO0 ( 'Appending Favorites' )
  ooOO0oO0oo00o = open ( iIi1ii1I1 ) . read ( )
  O0o0O = json . loads ( ooOO0oO0oo00o )
  O0o0O . append ( ( name , url , iconimage , fanart , mode ) )
  o0oO0OoO0 = open ( iIi1ii1I1 , "w" )
  o0oO0OoO0 . write ( json . dumps ( O0o0O ) )
  o0oO0OoO0 . close ( )
  if 6 - 6: IIiIiII11i
  if 7 - 7: o0Oo0O0Oo00oO % ooOoO0O00 * ii * o0o00Oo0O + O0o0O0O0ooO0
def OoO0oO ( ) :
 if os . path . exists ( iIi1ii1I1 ) == False :
  OoO00O0 = [ ]
  o0oOOOO0 ( 'Making Favorites File' )
  OoO00O0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ooOO0oO0oo00o = open ( iIi1ii1I1 , "w" )
  ooOO0oO0oo00o . write ( json . dumps ( OoO00O0 ) )
  ooOO0oO0oo00o . close ( )
 else :
  IiiI1iiI1III1i = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
  iii1 = len ( IiiI1iiI1III1i )
  for i11oooOo in IiiI1iiI1III1i :
   IiiiiI1i1Iii = i11oooOo [ 0 ]
   O0o = i11oooOo [ 1 ]
   oo0O0o00o0O = i11oooOo [ 2 ]
   try :
    oo0oo0O0 = i11oooOo [ 3 ]
    if oo0oo0O0 == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     oo0oo0O0 = oo0O0o00o0O
    else :
     oo0oo0O0 = I11i1II
   try : IiIIiiI = i11oooOo [ 5 ]
   except : IiIIiiI = None
   try : o0o0OO0o00o0O = i11oooOo [ 6 ]
   except : o0o0OO0o00o0O = None
   if 28 - 28: oO0o - oo0OO + OOooOOo + o0Oo0O0Oo00oO / iI11I1II1I1I
   if i11oooOo [ 4 ] == 0 :
    iiIiII1 ( IiiiiI1i1Iii , O0o , '' , oo0O0o00o0O , I11i1II , '' , 'fav' )
   else :
    iiIiII1 ( IiiiiI1i1Iii , O0o , i11oooOo [ 4 ] , oo0O0o00o0O , I11i1II , '' , 'fav' )
    if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
def O0oOoo ( name ) :
 O0o0O = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for OoOOoO0O0oO in range ( len ( O0o0O ) ) :
  if O0o0O [ OoOOoO0O0oO ] [ 0 ] == name :
   del O0o0O [ OoOOoO0O0oO ]
   o0oO0OoO0 = open ( iIi1ii1I1 , "w" )
   o0oO0OoO0 . write ( json . dumps ( O0o0O ) )
   o0oO0OoO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 92 - 92: I1ii11iIi11i / Ii + Ii1I
 if 87 - 87: OOooOOo % iI11I1II1I1I
def iII111Ii ( ) :
 o0O = os . path . join ( iIii1 , 'addons.ini' )
 O0OOO0O = open ( o0O , "w+" )
 if 36 - 36: Ii / O0o0O0O0ooO0 . O0o0Ooo + iIIIIii1 . o0o00Oo0O + oOo0O0Ooo
 O0OOO0O . write ( r'# This file contains the "built-in" channels' + '\n' )
 O0OOO0O . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 O0OOO0O . write ( r'[plugin.video.GenieTv]' + '\n' )
 O0OOO0O . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F191.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+One%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F190.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+Two%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F188.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+Four%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F208.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F207.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F206.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV3%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F205.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV4%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F183.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Channel+4%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F185.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Channel+5%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F187.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']5%2A%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F186.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']5USA%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F194.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']RTE+One%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F193.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']RTE+Two%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F192.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']TG4%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F32.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F33.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F35.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Living%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F34.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F325.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Dave%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F324.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Pick%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F326.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Gold%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F518.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Watch%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F377.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Yesterday%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F181.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Comedy+Central%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F830.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']London+Live%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F230.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F231.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Disney+Channel%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F198.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Animal+Planet%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F197.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F200.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F199.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Science%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F168.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F639.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Food+Network%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F234.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']MTV+Music%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F182.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Film4%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F853.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']True+Movies%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F852.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']True+Movies+2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F732.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F511.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F516.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F512.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F509.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F510.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F514.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F513.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F46.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F45.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F195.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F18.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F19.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F20.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F21.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F22.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F24.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F23.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F309.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F26.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F705.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F28.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F173.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Box+Nation%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F178.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']WWENetwork%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F269.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Eurosport+1%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F748.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Eurosport+2%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F170.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']At+the+Races%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F171.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Racing+UK%0D[%2FCOLOR]' + '\n' )
 O0OOO0O . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F826.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 36 - 36: ooOoO0O00 - Ii1I - IiI11iII1
 if 7 - 7: Ii + oOo0O0Ooo
def I1i1I1II ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  o0O0OOO0Ooo ( IiiiiI1i1Iii , ( O0o ) . strip ( ) , 222 , Oo0oOOo + '247.png' , Oo0oOOo + '247.png' , '' )
def O0OOOOOO0 ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  o0O0OOO0Ooo ( IiiiiI1i1Iii , ( O0o ) . strip ( ) , 222 , Oo0oOOo + 'musicch.png' , Oo0oOOo + 'musicch.png' , '' )
def Ooo0Oo0o ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  o0O0OOO0Ooo ( IiiiiI1i1Iii , ( O0o ) . strip ( ) , 222 , Oo0oOOo + 'NEWS.png' , Oo0oOOo + 'NEWS.png' , '' )
def oo0Oo0 ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  o0O0OOO0Ooo ( IiiiiI1i1Iii , ( O0o ) . strip ( ) , 222 , Oo0oOOo + 'adult.png' , Oo0oOOo + 'adult.png' , '' )
def oOOoOOO0oo0 ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 OO0oOO0O = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  o0O0OOO0Ooo ( IiiiiI1i1Iii , O0o , 1016 , Oo0oOOo + 'TUTS.png' , Oo0oOOo + 'TUTS.png' , '' )
  if 87 - 87: OOO00O / OOooOOo % I11i * oo0OO
  if 77 - 77: oo0OO - I1ii11iIi11i - iI11I1II1I1I
def IIi1i ( ) :
 if 21 - 21: oo0OO % oo0OO / oO0o
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Recent Episodes[/COLOR]' , '' , 10019 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , '' , 10020 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Search[/COLOR]' , '' , 10021 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 if 12 - 12: O0o0O0O0ooO0 / OOooOOo
def ooooo0Oo0 ( ) :
 if 97 - 97: iIIIIii1 . oo0OO . iIIIIii1
 oOoO0 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OO0oOO0O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiIi1I1 , IiiiiI1i1Iii , OOoOooOoOOOoo in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii + '  -  ' + ( OOoOooOoOOOoo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0o , 10023 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
  if 91 - 91: OoO0O0 + IiI11iII1 . O0o0Ooo
  if 15 - 15: O0o0Ooo
  if 94 - 94: IiI11iII1 % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
def oO0oOoo0O ( ) :
 if 26 - 26: I1ii11iIi11i + oOo0O0Ooo * OoO0O0 + OOO00O
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Action[/COLOR]' , 'Aksiyon' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Adventure[/COLOR]' , 'Macera' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Animation[/COLOR]' , 'Animasyon' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Anime[/COLOR]' , 'Anime' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Biography[/COLOR]' , 'Biyografi' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Comedy[/COLOR]' , 'Komedi' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Drama[/COLOR]' , 'Dram' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Family[/COLOR]' , 'Aile' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']History[/COLOR]' , 'Tarih' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Horror[/COLOR]' , 'Korku' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Mystery[/COLOR]' , 'Gizem' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Romance[/COLOR]' , 'Romantik' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Sport[/COLOR]' , 'Spor' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Western[/COLOR]' , 'Tarih' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
 if 88 - 88: O0o0Ooo + Ii % oo0OO * OoO0O0 * OoO0O0 * o0Oo0O0Oo00oO
def I1I1i ( url ) :
 o0OOo0o0O0O = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 O0OOO0OOoO0O = cloudflare . source ( o0OOo0o0O0O )
 OO0oOO0O = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 10022 , Oo0oOOo + 'dtv.png' , i1iIIi1 , '' )
  if 87 - 87: IiI11iII1 + OOO00O + o0o00Oo0O / ooOoO0O00 % iIIIIii1 / IiI11iII1
  if 64 - 64: oO0o % iIIIIii1 . IiI11iII1 % oO0o + O0o0Ooo * iIIIIii1
  if 83 - 83: I11i % oo0OO + O0o0Ooo % Ii + o0o00Oo0O
  if 65 - 65: iI11I1II1I1I % oo0OO + o0o00Oo0O / ii
def O0000oO0o00 ( ) :
 if 80 - 80: ii + iIIIIii1
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0o = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOoO ) . replace ( ' ' , '+' )
 O0OOO0OOoO0O = cloudflare . source ( O0o )
 OO0oOO0O = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  if oOoO in IiiiiI1i1Iii . lower ( ) :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 10022 , Oo0oOOo + 'dtv.png' )
   if 95 - 95: IiI11iII1 / oo0OO * IiI11iII1 - ii * ii % oO0o
   if 43 - 43: I1ii11iIi11i . IiI11iII1
   if 12 - 12: IiI11iII1 + OoO0O0 + O0o0Ooo . iIIIIii1 / o0Oo0O0Oo00oO
def i1I ( url ) :
 O0OOO0OOoO0O = cloudflare . source ( url )
 OO0oOO0O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for iI1i11 , oOOoooO0O0 , ii1 , IiiiiI1i1Iii in OO0oOO0O :
  O0ooooo000 = ( ii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OooOoOO0OO = ( oOOoooO0O0 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1iiIiiii1111 = 'Season ' + OooOoOO0OO + 'Episode ' + O0ooooo000 + IiiiiI1i1Iii
  I1ii1i11i ( I1iiIiiii1111 , iI1i11 )
  if 86 - 86: o0o00Oo0O % ooOoO0O00 . IIiIiII11i . O0o0Ooo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 44 - 44: Ii * O0o0Ooo + OOooOOo + iIIIIii1 * o0o00Oo0O . iIIIIii1
  if 19 - 19: IIiIiII11i - iIIIIii1
def I1ii1i11i ( name , url ) :
 iI1i11 = url
 OOOOo000o00OO = name
 O00Oo000ooO0 = cloudflare . source ( iI1i11 )
 oOiIi1IIIi1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( O00Oo000ooO0 )
 for IiIi , Oo0oOo0O0o000Ooo in oOiIi1IIIi1 :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + OOOOo000o00OO + Oo0oOo0O0o000Ooo + '[/COLOR]' , IiIi , 10012 , Oo0oOOo + 'dtv.png' )
  if 65 - 65: o0o00Oo0O . OOO00O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: OOO00O / o0o00Oo0O * iIIIIii1
 if 17 - 17: o0Oo0O0Oo00oO / iI11I1II1I1I - oO0o + oOo0O0Ooo % OoO0O0
def III1III11II ( ) :
 if 43 - 43: oOo0O0Ooo
 if 47 - 47: ii % OOooOOo
 if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . IiI11iII1
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 if 67 - 67: IIiIiII11i / I11i . OoO0O0 . ii
 if 19 - 19: iIIIIii1 . Ii1I / OOooOOo
 if 68 - 68: OOO00O / ii * O0o0Ooo / oo0OO
 if 88 - 88: I11i
 if 1 - 1: ii
 if 48 - 48: OOO00O * OOooOOo - OOO00O - OoO0O0 + OoO0O0
 if 40 - 40: Ii . iI11I1II1I1I
 if 2 - 2: ooOoO0O00 * oo0OO - oo0OO + ii % OOooOOo / OOooOOo
 if 3 - 3: ii
 if 71 - 71: iIIIIii1 + ooOoO0O00 - O0o0O0O0ooO0 - Ii . O0o0Ooo - OOO00O
 if 85 - 85: Ii1I - OOooOOo / Ii1I + OoO0O0 - O0o0O0O0ooO0
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.li/latest' , 10046 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.li/new' , 10042 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Search Program[/COLOR]' , '' , 10043 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + IiI11iII1
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * oo0OO
def Oo0O0000Oo00o ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Iiii1iI1i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 OO0oOO0O = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( Iiii1iI1i ) )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://watchseries.li/letters/' + url , 10049 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
  if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
def o00iIiiiII ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://watchseries.li/' + url , 10049 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
  if 5 - 5: ii / I11i % O0o0Ooo % oO0o * O0o0O0O0ooO0 + iI11I1II1I1I
def I11iiI11iiI ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 for url in oOiIi1IIIi1 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10049 , Oo0oOOo + 'Next.png' , '' , '' )
  if 51 - 51: oo0OO . iI11I1II1I1I + oO0o * o0Oo0O0Oo00oO + ooOoO0O00
  if 81 - 81: o0o00Oo0O - o0Oo0O0Oo00oO + I1ii11iIi11i
def oOo0OOO00Oo ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii1ii1II1 = 'http://www.watchseries.li/search/' + oOoO . replace ( ' ' , '%20' )
 O0OOO0OOoO0O = O0 ( i1ii1ii1II1 )
 OO0oOO0O = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'watch online' in IiiiiI1i1Iii :
   pass
  else :
   print O0o
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.watchseries.li' + O0o , 10044 , IiIi1I1 , '' , '' )
   if 6 - 6: OoO0O0 % IIiIiII11i - OoO0O0 + Ii1I
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 31 - 31: Ii * I11i / O0o0Ooo * ooOoO0O00 + I11i
def O00OoooO00 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , url , IiiiiI1i1Iii , ii1 , iIIiIiI1I1 in OO0oOO0O :
  IiII1 = ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( ii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiII1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , IiIi1I1 , '' , iIIiIiI1I1 )
  if 17 - 17: o0Oo0O0Oo00oO
def o00ooOOOoOo ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  IiII1 = ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiII1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 for url in oOiIi1IIIi1 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10046 , Oo0oOOo + 'Next.png' , '' , '' )
  if 30 - 30: OOO00O + OOO00O % iIIIIii1 - I11i - Ii1I
def i111IiiI1Ii ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , IiIi1I1 , '' , '' )
 for url in oOiIi1IIIi1 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10041 , Oo0oOOo + 'Next.png' , '' , '' )
  if 72 - 72: o0o00Oo0O . OOooOOo * I1ii11iIi11i + Ii1I - I11i
def iII1I11 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Iiii1iI1i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for oOOoooO0O0 , OoOOOO0O0oO0 in Iiii1iI1i :
  OO0oOO0O = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OoOOOO0O0oO0 ) )
  for url , IiiiiI1i1Iii in OO0oOO0O :
   IiII1 = ( oOOoooO0O0 ) . replace ( '  ' , '' ) + ' ' + ( IiiiiI1i1Iii ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiII1 + '[/COLOR]' , 'http://www.watchseries.li' + url , 10045 , Oo0oOOo + 'WATCHSERIES.png' , '' , '' )
 oOiIi1IIIi1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url in oOiIi1IIIi1 :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.li' + url , 10044 , Oo0oOOo + 'Next.png' , '' , '' )
  if 15 - 15: O0o0Ooo
  if 13 - 13: iI11I1II1I1I * OOooOOo / IiI11iII1 % OOO00O + oo0OO
class iiiI1iI1 ( ) :
 if 15 - 15: iIIIIii1 . ooOoO0O00 * OOooOOo % iI11I1II1I1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 35 - 35: Ii1I + IiI11iII1 - OOooOOo % oo0OO % I11i % OOooOOo
  IiII1 = name
  self . Get_Sources ( O0o , IiII1 )
  if 45 - 45: oOo0O0Ooo * OoO0O0 % oO0o
  if 24 - 24: OOO00O - O0o0Ooo * oo0OO
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  O0OOO0OOoO0O = O0 ( URL )
  OO0oOO0O = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for O0o , IiiiiI1i1Iii in OO0oOO0O :
   URL = 'http://www.watchseries.li/link/' + O0o
   self . Get_site_link ( URL , season_name )
   if 87 - 87: o0Oo0O0Oo00oO - Ii1I % Ii1I . oo0OO / Ii1I
 def Get_site_link ( self , url , season_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( O0OOO0OOoO0O )
  oOiIi1IIIi1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( O0OOO0OOoO0O )
  ooO0O0o0 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( O0OOO0OOoO0O )
  for url in OO0oOO0O :
   self . main ( url , season_name )
  for url in oOiIi1IIIi1 :
   self . main ( url , season_name )
  for url in ooO0O0o0 :
   self . main ( url , season_name )
   if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0O0OOo0oO = 'DACLIPS'
   if o0O0OOo0oO in iiiI1iI1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0O0OOo0oO )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o0O0OOo0oO = 'FILEHOOT'
    if o0O0OOo0oO in iiiI1iI1 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o0O0OOo0oO )
   else :
    if 'thevideo.me' in url :
     o0O0OOo0oO = 'THEVIDEO'
     if o0O0OOo0oO in iiiI1iI1 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o0O0OOo0oO )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o0O0OOo0oO = 'ALLMYVIDEOS'
      if o0O0OOo0oO in iiiI1iI1 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o0O0OOo0oO )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o0O0OOo0oO = 'VIDSPOT'
       if o0O0OOo0oO in iiiI1iI1 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o0O0OOo0oO )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o0O0OOo0oO = 'VODLOCKER'
        if o0O0OOo0oO in iiiI1iI1 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o0O0OOo0oO )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
         if 62 - 62: o0o00Oo0O . I1ii11iIi11i
 def allmyvid ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for iI1ii , IiiiiI1i1Iii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 76 - 76: o0Oo0O0Oo00oO + iI11I1II1I1I + OOooOOo . oO0o
 def vidspot ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( O0OOO0OOoO0O )
  for iI1ii , IiiiiI1i1Iii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 49 - 49: iIIIIii1 / OOO00O / OoO0O0
 def thevideo ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( O0OOO0OOoO0O )
  for iI1ii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - OOO00O
 def vodlocker ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for iI1ii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 38 - 38: I11i % IiI11iII1 + Ii + O0o0O0O0ooO0 + OOO00O / Ii
 def daclips ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( O0OOO0OOoO0O )
  for iI1ii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 94 - 94: O0o0O0O0ooO0 - I1ii11iIi11i + oo0OO
 def filehoot ( self , url , season_name , source_name ) :
  O0OOO0OOoO0O = O0 ( url )
  OO0oOO0O = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for iI1ii in OO0oOO0O :
   self . Printer ( iI1ii , season_name , source_name )
   if 59 - 59: O0o0Ooo . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 def Printer ( self , Link , season_name , source_name ) :
  if 56 - 56: oo0OO + OOO00O
  if Link in iiiI1iI1 . List :
   pass
  elif source_name in iiiI1iI1 . source_list :
   pass
  else :
   iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + source_name + '[/COLOR]' , Link , 10012 , Oo0oOOo + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   iiiI1iI1 . List . append ( Link )
   iiiI1iI1 . source_list . append ( source_name )
   if 32 - 32: IIiIiII11i + OOooOOo % OOO00O / OOooOOo + Ii1I
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 2 - 2: Ii - IiI11iII1 + oO0o % O0o0Ooo * o0Oo0O0Oo00oO
   if 54 - 54: o0o00Oo0O - O0o0O0O0ooO0 . OoO0O0 % O0o0O0O0ooO0 + O0o0O0O0ooO0
   if 36 - 36: OoO0O0 % Ii
   if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * oo0OO . O0o0Ooo / ooOoO0O00
   if 50 - 50: IiI11iII1 / ooOoO0O00 % ii
def oOOOOO0Ooooo ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Highlights[/COLOR]' , '' , 10008 , Oo0oOOo + 'Highlights.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Fixtures[/COLOR]' , '' , 10009 , Oo0oOOo + 'Fixtures.png' , i1iIIi1 , '' )
 if 57 - 57: o0Oo0O0Oo00oO - ii
def OOoOO0O0o0 ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 OO0oOO0O = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( IiiiiI1i1Iii ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0o , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiIi1I1 , i1iIIi1 , '' )
  if 44 - 44: OoO0O0 / I1ii11iIi11i + iIIIIii1 % IIiIiII11i / oO0o + Ii
def ii11Iiii ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Iiii1iI1i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for Iiii1iI1i in Iiii1iI1i :
  II1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( Iiii1iI1i ) )
  for OoooOo in II1 :
   OoooOo = OoooOo
  I1I1IIiiii1ii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( Iiii1iI1i ) )
  for oOo0Oi1i , IiIi1I1 , time , OOOO00OoooO in I1I1IIiiii1ii :
   I1ii11 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OOOO00OoooO )
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + OoooOo + ' - ' + oOo0Oi1i + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IiIi1I1 , i1iIIi1 , ( str ( I1ii11 ) ) )
   if 7 - 7: Ii1I / IIiIiII11i - O0o0Ooo + ooOoO0O00 + o0Oo0O0Oo00oO
 i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if 7 - 7: OOO00O + o0Oo0O0Oo00oO
def IiiIIiI1iI1 ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , Oo0oOOo + 'fanart.jpg' , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , Oo0oOOo + 'fanart.jpg' , '' )
 if 86 - 86: ooOoO0O00 / o0Oo0O0Oo00oO * oOo0O0Ooo
def OOoO0OOoO0ooo ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width="218" height="150" class="entry-thumb" src="([^"]*)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , url , IiiiiI1i1Iii in OO0oOO0O :
  ii11i1ii1 = IiiiiI1i1Iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + ii11i1ii1 + '[/COLOR]' , url , 10013 , IiIi1I1 )
 for url , IiiiiI1i1Iii , IiIi1I1 in oOiIi1IIIi1 :
  ii11i1ii1 = IiiiiI1i1Iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + ii11i1ii1 + '[/COLOR]' , url , 10013 , IiIi1I1 )
  if 37 - 37: Ii
def iI1ii11I ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( O0OOO0OOoO0O )
 for IiIi in OO0oOO0O :
  o0oO0o0oo0O0 = ( IiIi ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOO0o0 ( 'http:' + o0oO0o0oo0O0 )
  if 98 - 98: iIIIIii1 * iI11I1II1I1I . o0Oo0O0Oo00oO * I1ii11iIi11i / Ii1I + OOO00O
  if 25 - 25: oo0OO
def Iii11111iiI ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , url , 8046 , IiIi1I1 )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , Oo0oOOo + 'Next.png' )
def o0OOOOoO ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oOoO0 )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  OOOO0o0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 70 - 70: IIiIiII11i + IiI11iII1 + Ii - ooOoO0O00 / iIIIIii1
def iI1IIiiIIIII ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  yt . PlayVideo ( url )
  if 43 - 43: O0o0O0O0ooO0 + I1ii11iIi11i / ii
def Ii1II1 ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 ooii11i = Oo0 ( i1111 ( 'aHR0cDovL2RvY3VtZW50YXJ5c3Rvcm0uY29tLw==' ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( oOoO0 )
 O000oo00OOOOO = re . compile ( '<li class="cat-item cat-item.+?."><a href="([^"]*)".+?>(.+?)</a>' , re . DOTALL ) . findall ( ooii11i )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , O0o , 8041 , Oo0oOOo + 'documentary.png' )
 for O0o , IiiiiI1i1Iii in O000oo00OOOOO :
  if 'category' in O0o :
   IIIIIii1ii11 ( IiiiiI1i1Iii + '[COLOR' + oO0o0o0ooO0oO + '] - Storm[/COLOR]' , O0o , 8048 , Oo0oOOo + 'storm.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( oOoO0 )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  IIIIIii1ii11 ( ( IiiiiI1i1Iii ) . replace ( '&#039;s' , '' ) , url , 8042 , IiIi1I1 )
 for IiiiiI1i1Iii , url , IiIi1I1 in oOiIi1IIIi1 :
  IIIIIii1ii11 ( ( IiiiiI1i1Iii ) . replace ( '&#039;s' , '' ) , url , 8042 , IiIi1I1 )
 for url in next :
  IIIIIii1ii11 ( 'NEXT PAGE' , url , 8041 , Oo0oOOo + 'Next.png' )
  if 75 - 75: o0Oo0O0Oo00oO - O0o0Ooo % OOooOOo
  if 80 - 80: o0Oo0O0Oo00oO / OoO0O0
def iIIi1i11 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , IiIi1I1 , url , iIiIIi in OO0oOO0O :
  iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IiIi1I1 )
 for url in oOiIi1IIIi1 :
  iI1Iii11i1 ( ( url ) . replace ( '//' , 'http://' ) )
  if 34 - 34: oo0OO - OOO00O * I1ii11iIi11i / I11i
def iI1Iii11i1 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  iIi1IIiI ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oOOo + 'documentary.png' )
  if 19 - 19: Ii1I
def IiI ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  IIIIIii1ii11 ( ( IiiiiI1i1Iii ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , IiIi1I1 )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'NEXT' , url , 8048 , Oo0oOOo + 'Next.png' )
def Iii1iiI ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in oOiIi1IIIi1 :
  if 'rtd' in url :
   ii1IiiII ( url )
   if 7 - 7: iI11I1II1I1I * oO0o / OOooOOo % IiI11iII1 - I11i - OoO0O0
def ii1IiiII ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oOoO0 )
 for OOOOi11i1 , file in OO0oOO0O :
  url = ( 'https://rtd.rt.com' + OOOOi11i1 + file )
  OOOO0o0 ( url )
  if 28 - 28: iI11I1II1I1I
  if 7 - 7: I11i % iIIIIii1 * OOooOOo
def O0O00 ( ) :
 O0OOO0OOoO0O = Oo0 ( 'http://www.stream2watch.co/live-tv' )
 OO0oOO0O = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for O0o , IiIi1I1 , IiiiiI1i1Iii , Iii11I1iII1 in OO0oOO0O :
  IIIIIii1ii11 ( ( IiiiiI1i1Iii + '[COLOR' + oO0o0o0ooO0oO + ']' + Iii11I1iII1 + '[/COLOR]' ) , O0o , 8086 , IiIi1I1 )
  if 24 - 24: oo0OO / IiI11iII1 / O0o0Ooo % OOooOOo / Ii1I * OOO00O
def iiIiIIi11I1 ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 8087 , IiIi1I1 )
  if 86 - 86: iI11I1II1I1I . oOo0O0Ooo * O0o0Ooo
def ii1i11ii ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi11iIi ( url , IiiiiI1i1Iii )
  if 4 - 4: OoO0O0 / O0o0O0O0ooO0 * O0o0Ooo - I1ii11iIi11i * oOo0O0Ooo
def iIi11iIi ( url , name ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url in OO0oOO0O :
  print url
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 6 - 6: o0Oo0O0Oo00oO
def OooO0O ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 OO0oOO0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + O0o , 3002 , 'http://www.solie.org/alibrary/' + IiIi1I1 )
def I111 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiIi1I1 )
def iiiIii ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oOoO0 )
 OoOiIIi1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oOoO0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , Oo0oOOo + 'classicmovies.png' )
 for url , IiiiiI1i1Iii in OoOiIIi1 :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , Oo0oOOo + 'classicmovies.png' )
 for url in next :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , Oo0oOOo + 'Next.png' )
 for url , IiIi1I1 , IiiiiI1i1Iii in oOiIi1IIIi1 :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IiIi1I1 )
def ooIiI11i1I11111 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  Ii1IIIIIIiI1 ( url )
def Ii1IIIIIIiI1 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OOOO0o0 ( url )
  if 24 - 24: oOo0O0Ooo * o0Oo0O0Oo00oO % o0o00Oo0O - I1ii11iIi11i
def ii1IOoO0O ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 OO0oOO0O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0o , 8065 , Oo0oOOo + 'classicmovies.png' )
def Oo0oo ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( "v.src = '([^']*)';" ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OoOOoooOO0O ( url )
  if 54 - 54: ooOoO0O00 - O0o0Ooo % I1ii11iIi11i - oO0o / iIIIIii1 . o0o00Oo0O
def IiiOoo0o0ooooOOo ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 OO0oOO0O = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0o , 8065 , Oo0oOOo + 'classictv.png' )
def oOoOO0000oO00 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  if 'mp4' in url :
   OOOO0o0 ( url )
 for url in oOiIi1IIIi1 :
  yt . PlayVideo ( url )
  if 93 - 93: O0o0Ooo . OOooOOo / I1ii11iIi11i + oo0OO
def iiiiI1I ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + O0o , 8071 , Oo0oOOo + 'streams.png' )
def OOOOOOo0OOoOo ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  if '(Free Access)' in IiiiiI1i1Iii :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , Oo0oOOo + 'streams.png' )
def OO00O00o ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , IiiiiI1i1Iii , url in OO0oOO0O :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IiIi1I1 )
  if 4 - 4: OoO0O0 - oo0OO % OOooOOo / IIiIiII11i % oo0OO
def O0OO0OoO ( ) :
 iii1IIIiiiI ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , Oo0oOOo + 'Jizbox.png' , '' , '' )
 iii1IIIiiiI ( 'Genres' , 'http://www.xvideos.com' , 10106 , Oo0oOOo + 'Jizbox.png' , '' , '' )
 iii1IIIiiiI ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , Oo0oOOo + 'Jizbox.png' , '' , '' )
 iii1IIIiiiI ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , Oo0oOOo + 'Jizbox.png' , '' , '' )
 iii1IIIiiiI ( 'Search' , '' , 10107 , Oo0oOOo + 'Jizbox.png' , '' , '' , )
 if 83 - 83: OOO00O / OoO0O0
def i11iI1 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 i1Ii11ii1I = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( O0OOO0OOoO0O )
 for url in i1Ii11ii1I :
  iii1IIIiiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , Oo0oOOo + 'Jizbox.png' , '' , '' )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii , oo00oO0o in OO0oOO0O :
  iii1IIIiiiI ( ( IiiiiI1i1Iii + ' - No of Videos : ' + ( oo00oO0o ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , Oo0oOOo + 'Jizbox.png' , '' , '' )
  if 66 - 66: I1ii11iIi11i / ii % IiI11iII1 / O0o0O0O0ooO0 + ii
def ii1III1iiIi ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 i1Ii11ii1I = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( O0OOO0OOoO0O )
 for url in i1Ii11ii1I :
  iii1IIIiiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , Oo0oOOo + 'Next.png' , '' , '' )
 OO0oOO0O = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , url , IiiiiI1i1Iii , I1ii1iI in OO0oOO0O :
  iii1IIIiiiI ( IiiiiI1i1Iii + '--' + I1ii1iI , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IiIi1I1 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 99 - 99: I11i
  if 1 - 1: o0Oo0O0Oo00oO * OOooOOo * oO0o + I1ii11iIi11i
def O0OOoOooO00 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , url , IiiiiI1i1Iii , O0OOoOOO0oO , o0o00OOOO in OO0oOO0O :
  iii1IIIiiiI ( IiiiiI1i1Iii + ' - Porn Quality : ' + o0o00OOOO + ' - ' + O0OOoOOO0oO , 'http://www.xvideos.com' + url , 10108 , IiIi1I1 , IiIi1I1 , o0o00OOOO + ' - ' + O0OOoOOO0oO )
 i11iIi1iIIIIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( O0OOO0OOoO0O )
 for url in i11iIi1iIIIIi :
  iii1IIIiiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , Oo0oOOo + 'Next.png' , '' , '' )
  if 43 - 43: OOO00O * IiI11iII1 * IIiIiII11i % iI11I1II1I1I / Ii1I - iIIIIii1
def oo0O0oOoOoo ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Iiii1iI1i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 i1Ii11ii1I = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( O0OOO0OOoO0O )
 for url in i1Ii11ii1I :
  iii1IIIiiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , Oo0oOOo + 'Next.png' , '' , '' )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( Iiii1iI1i ) )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iii1IIIiiiI ( IiiiiI1i1Iii , 'http://www.xvideos.com' + url , 10105 , Oo0oOOo + 'Jizbox.png' , '' , '' )
  if 76 - 76: oO0o . ii % IiI11iII1 * o0Oo0O0Oo00oO
  if 23 - 23: iIIIIii1 + iI11I1II1I1I
def Ii1111III1 ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00oooo0 = ( oOoO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OOIi1iI111II1I1 = oO00oooo0 . lower ( )
 OO0 = 'http://www.xvideos.com/?k=' + OOIi1iI111II1I1
 print OO0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0OOO0OOoO0O = O0 ( OO0 )
 OO0oOO0O = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , O0o , IiiiiI1i1Iii , O0OOoOOO0oO , o0o00OOOO in OO0oOO0O :
  iii1IIIiiiI ( IiiiiI1i1Iii + ' - Porn Quality : ' + o0o00OOOO + ' - ' + O0OOoOOO0oO , 'http://www.xvideos.com' + O0o , 10108 , IiIi1I1 , IiIi1I1 , o0o00OOOO + ' - ' + O0OOoOOO0oO )
 i11iIi1iIIIIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( O0OOO0OOoO0O )
 for O0o in i11iIi1iIIIIi :
  iii1IIIiiiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + O0o , 10105 , Oo0oOOo + 'Next.png' , '' , '' )
  if 96 - 96: o0o00Oo0O . O0o0O0O0ooO0 - oOo0O0Ooo * I1ii11iIi11i
def OOoOOOo0 ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( O0OOO0OOoO0O )
 ooO0O0o0 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( O0OOO0OOoO0O )
 for url in OO0oOO0O :
  if 'http' in url :
   iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']LOW[/COLOR]' , url , 222 , Oo0oOOo + 'Jizbox.png' )
 for url in oOiIi1IIIi1 :
  if 'http' in url :
   iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']HIGH[/COLOR]' , url , 222 , Oo0oOOo + 'Jizbox.png' )
 for url in ooO0O0o0 :
  if 'http' in url :
   iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']HLS[/COLOR]' , url , 222 , Oo0oOOo + 'Jizbox.png' )
   if 84 - 84: oo0OO + OoO0O0 . O0o0O0O0ooO0
def O0o00 ( url ) :
 O0OO0o0OO0OO = xbmc . Player ( I1I1i1i ( ) )
 import urlresolver
 try : O0OO0o0OO0OO . play ( url )
 except : pass
 if 74 - 74: o0o00Oo0O % ii * I1ii11iIi11i + OoO0O0 * O0o0O0O0ooO0
 if 100 - 100: OoO0O0 + o0Oo0O0Oo00oO * I11i + IIiIiII11i
def oOo0O000Ooo0 ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 OO0oOO0O = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + O0o ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , Oo0oOOo + 'gofish.png' )
def i11i ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 oOiIi1IIIi1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , Oo0oOOo + 'gofish.png' )
 for url , IiiiiI1i1Iii , IiIi1I1 in oOiIi1IIIi1 :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + IiIi1I1 )
 for url in next :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , Oo0oOOo + 'Next.png' )
def O0o0O00o0o ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( O0OOO0OOoO0O )
 for url in OO0oOO0O :
  yt . PlayVideo ( url )
  if 6 - 6: Ii1I - oo0OO * Ii + OOooOOo / OOO00O % OoO0O0
  if 38 - 38: OoO0O0 % iIIIIii1 % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
  if 9 - 9: I11i % Ii1I . Ii1I
IiIIIIii11i = '{PQ},' ; oO0OOO00 = '{SC},' ; I1iIiI1iiiiI1 = '{XG},' ; IIII1ii1 = '{JP},' ; OOO0O0OOo = '{HW},' ; Iii1 = '{RT},'
def OOoOi1IiiI ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 O0OOO0 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0o = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 ooo00Ooo = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0OIi = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 IIi1iiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0o = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO00OO0o0O = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOoO
 III1IiiIiiI1i = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 OoO0o00OoO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 Oo00Oooo00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II11II1I = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 52 - 52: OoO0O0 * oo0OO + O0o0Ooo * O0o0Ooo % ooOoO0O00 % O0o0Ooo
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 O0OOO0OOoO0O = I11iii1Ii ( O0o )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 O00Oo000ooO0 = I11iii1Ii ( iI1i11 )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 OoO0O00 = I11iii1Ii ( ooo00Ooo )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 IIiII = I11iii1Ii ( o0OIi )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 OOOO000Ooo0O = I11iii1Ii ( IIi1iiI )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 oOo0oOooo0O = I11iii1Ii ( oOO00OO0o0O )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 iI1iIIIIIiIi1 = I11iii1Ii ( III1IiiIiiI1i )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIi = I11iii1Ii ( OoO0o00OoO )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOo = I11iii1Ii ( Oo00Oooo00o )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 ooOo0o = I11iii1Ii ( II11II1I )
 if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / O0o0Ooo + IiI11iII1
 if 17 - 17: OoO0O0 + IIiIiII11i
 if O0OOO0OOoO0O != 'Failed' :
  OO0oOO0O = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
  for I1i11I11Iii , IiiiiI1i1Iii in OO0oOO0O :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0o + I1i11I11Iii ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if O00Oo000ooO0 != 'Failed' :
  oOiIi1IIIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00Oo000ooO0 )
  for I1i11I11Iii , IiiiiI1i1Iii in oOiIi1IIIi1 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( iI1i11 + I1i11I11Iii ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if OoO0O00 != 'Failed' :
  ooO0O0o0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoO0O00 )
  for I1i11I11Iii , IiiiiI1i1Iii in ooO0O0o0 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( ooo00Ooo + I1i11I11Iii ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if IIiII != 'Failed' :
  OO0OOooOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
  for I1i11I11Iii , IiiiiI1i1Iii in OO0OOooOO0 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , O0o , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if OOOO000Ooo0O != 'Failed' :
  i1i1I11I = [ ]
  iiiIi111i1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOO000Ooo0O )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in iiiIi111i1i :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    if IiiiiI1i1Iii in i1i1I11I :
     pass
    else :
     iiIiII1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , O0o , 1016 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
     i1i1I11I . append ( IiiiiI1i1Iii )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if oOo0oOooo0O != 'Failed' :
  OOo0OOooo0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oOo0oOooo0O )
  for O0o , IiIi1I1 , IiiiiI1i1Iii in OOo0OOooo0 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + O0o , 7067 , IiIi1I1 )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 93 - 93: o0o00Oo0O - oO0o . oOo0O0Ooo
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if iI1iIIIIIiIi1 != 'Failed' :
  oOOOoo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIIIIIiIi1 )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in oOOOoo :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    o0O0OOO0Ooo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Redemption[/COLOR]' ) , O0o , 222 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 29 - 29: oOo0O0Ooo + Ii . o0o00Oo0O
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if iIi != 'Failed' :
  o0oo0Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in o0oo0Oo :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    o0O0OOO0Ooo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Reaper[/COLOR]' ) , O0o , 222 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 10 - 10: Ii1I
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if oOo != 'Failed' :
  oO0OOOoO0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in oO0OOOoO0o :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    o0O0OOO0Ooo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Herovision[/COLOR]' ) , O0o , 222 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 75 - 75: Ii1I
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: O0o0Ooo / o0o00Oo0O * oOo0O0Ooo - O0o0Ooo
 if ooOo0o != 'Failed' :
  oooOo00000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( ooOo0o )
  for O0o , oo0O0o00o0O , IiiiiI1i1Iii in oooOo00000 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Silent Hunter[/COLOR]' ) , O0o , 222 , oo0O0o00o0O )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 45 - 45: o0o00Oo0O * IiI11iII1 + Ii - OoO0O0 - iI11I1II1I1I
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 IIIiI1ii1IIi = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 5 - 5: OoO0O0 % I1ii11iIi11i % iIIIIii1 % OOO00O
 for o0i1I11iI1iiI in IIIiI1ii1IIi :
  I1 = ooooooO0oo + o0i1I11iI1iiI + OooO0
  I1Iiii = I11iii1Ii ( I1 )
  if I1Iiii != 'Failed' :
   I1I1Iii1Iiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1Iiii )
   for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in I1I1Iii1Iiii :
    if oOoO in IiiiiI1i1Iii . lower ( ) :
     o0O0OOO0Ooo ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + ' - Source Pandoras[/COLOR]' , O0o , 222 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 4 - 4: iIIIIii1
     i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
     if 93 - 93: oo0OO % ooOoO0O00
 IIIiI1ii1IIi = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 83 - 83: oOo0O0Ooo . I1ii11iIi11i - O0o0Ooo . I11i
 if 73 - 73: oOo0O0Ooo - O0o0O0O0ooO0 . O0o0O0O0ooO0
 for o0i1I11iI1iiI in IIIiI1ii1IIi :
  I1 = O0OOO0 + o0i1I11iI1iiI
  I1I1 = I11iii1Ii ( I1 )
  if OOOO000Ooo0O != 'Failed' :
   O0OOO0ooO00o = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( I1I1 )
   for I1i11I11Iii , IiiiiI1i1Iii in O0OOO0ooO00o :
    if oOoO in IiiiiI1i1Iii . lower ( ) :
     iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0OOO0 + o0i1I11iI1iiI + I1i11I11Iii ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 24 - 24: IiI11iII1 + ii . iIIIIii1 / OOooOOo / O0o0Ooo
     i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
     if 65 - 65: ii
     if 18 - 18: o0o00Oo0O - ooOoO0O00 . IiI11iII1
def o00OOo00 ( ) :
 if 65 - 65: ooOoO0O00
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 if 9 - 9: oo0OO
 O0o = ( i1111 ( 'aHR0cDovL2RsLmZhcnNpbW92aWUubmV0L1NlcmlhbC8=' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL3R2c2hvd3MvdHZtYWluLnBocA==' ) )
 ooo00Ooo = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0OIi = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IIi1iiI = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OOIi1iI111II1I1 ) . replace ( ' ' , '+' )
 o0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 oOO00OO0o0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 III1IiiIiiI1i = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 16 - 16: OoO0O0
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0OOO0OOoO0O = I11iii1Ii ( O0o )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 O00Oo000ooO0 = I11iii1Ii ( iI1i11 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 OoO0O00 = I11iii1Ii ( ooo00Ooo )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 IIiII = I11iii1Ii ( o0OIi )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 OOOO000Ooo0O = cloudflare . source ( IIi1iiI )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 I1I1 = I11iii1Ii ( o0o )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 oOo0oOooo0O = I11iii1Ii ( oOO00OO0o0O )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 iI1iIIIIIiIi1 = I11iii1Ii ( III1IiiIiiI1i )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 63 - 63: O0o0O0O0ooO0
 if iI1iIIIIIiIi1 != 'Failed' :
  oOOOoo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIIIIIiIi1 )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in oOOOoo :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    iiIiII1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source HeroVision[/COLOR]' ) , O0o , 1016 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 11 - 11: O0o0O0O0ooO0 - iI11I1II1I1I
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: oO0o
 if oOo0oOooo0O != 'Failed' :
  OOo0OOooo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo0oOooo0O )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in OOo0OOooo0 :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    iiIiII1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- source Reaper[/COLOR]' ) , O0o , 1016 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 15 - 15: iIIIIii1 / iIIIIii1 + iI11I1II1I1I % ii
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
    if 12 - 12: OOO00O
    if 36 - 36: IiI11iII1 . iIIIIii1 * ii - I11i
    if 60 - 60: OoO0O0 . O0o0O0O0ooO0 / iI11I1II1I1I + OoO0O0 * IiI11iII1
    if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - O0o0Ooo + o0Oo0O0Oo00oO
    if 48 - 48: Ii1I
    if 96 - 96: OOO00O . ii
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 39 - 39: OoO0O0 + oO0o
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if O0OOO0OOoO0O != 'Failed' :
  OO0oOO0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0OOO0OOoO0O )
  for IiiiiI1i1Iii in OO0oOO0O :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( IiiiiI1i1Iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + ' source 1 [/COLOR]' , ( O0o + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source 1 Links" )
    if 80 - 80: OoO0O0 % oO0o / OOooOOo
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if O00Oo000ooO0 != 'Failed' :
  oOiIi1IIIi1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00Oo000ooO0 )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in oOiIi1IIIi1 :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , O0o , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 54 - 54: I1ii11iIi11i % oO0o - OoO0O0 - O0o0Ooo
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if OoO0O00 != 'Failed' :
  ooO0O0o0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OoO0O00 )
  for IiiiiI1i1Iii in ooO0O0o0 :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooo00Ooo + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 71 - 71: OOO00O . Ii
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if IIiII != 'Failed' :
  OO0OOooOO0 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for IiiiiI1i1Iii in OO0OOooOO0 :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0OIi + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 56 - 56: o0o00Oo0O * O0o0O0O0ooO0 + O0o0O0O0ooO0 * iI11I1II1I1I / OOO00O * IiI11iII1
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if OOOO000Ooo0O != 'Failed' :
  iiiIi111i1i = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OOOO000Ooo0O )
  for O0o , IiIi1I1 , IiiiiI1i1Iii in iiiIi111i1i :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + ' - Source - Dizi[/COLOR]' , O0o , 8062 , IiIi1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 25 - 25: iI11I1II1I1I . O0o0Ooo * Ii + I1ii11iIi11i * O0o0Ooo
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if I1I1 != 'Failed' :
  O0OOO0ooO00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I1 )
  for O0o , oo0O0o00o0O , iIIiIiI1I1 , i11iI11I1I , IiiiiI1i1Iii in O0OOO0ooO00o :
   if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
    iiIiII1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '- Source Scooby[/COLOR]' ) , O0o , 1016 , oo0O0o00o0O , i11iI11I1I , iIIiIiI1I1 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 67 - 67: O0o0O0O0ooO0
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
    if 88 - 88: I1ii11iIi11i
 i1ii111i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 42 - 42: OoO0O0 % ii / iIIIIii1
 for o0i1I11iI1iiI in i1ii111i :
  I1 = ooooooO0oo + o0i1I11iI1iiI + OooO0
  oOo = O0 ( I1 )
  if oOo != 'Failed' :
   oO0OOOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOo )
   for IiiiiI1i1Iii , iIIiIiI1I1 , O0o , IiIi1I1 , I11i1II , i11Ii1iIiII in oO0OOOoO0o :
    if OOIi1iI111II1I1 in IiiiiI1i1Iii . lower ( ) :
     iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + ' - Source Pandoras[/COLOR]' , O0o , i11Ii1iIiII , IiIi1I1 , I11i1II , iIIiIiI1I1 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 4 - 4: Ii - OoO0O0 % Ii1I * IiI11iII1 % I11i
     i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
     if 71 - 71: OOO00O . OOO00O - iI11I1II1I1I
     if 22 - 22: ii / Ii1I % O0o0O0O0ooO0 * OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1IiiiI1ii ( ) :
 if 55 - 55: Ii1I
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0o = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 O0OOO0OOoO0O = O0 ( O0o )
 OO0oOO0O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiiiiI1i1Iii , IiIi1I1 , oOoo0OO0 in OO0oOO0O :
  iiIiIi1111iI1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiIi1I1 ) . replace ( '\\' , '' )
  if oOoO in IiiiiI1i1Iii . lower ( ) :
   IIIIIii1ii11 ( IiiiiI1i1Iii , '' , 7022 , iiIiIi1111iI1 )
   if 11 - 11: Ii1I . Ii1I + IIiIiII11i * OOooOOo . iIIIIii1
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
I1I1i1I1I1I1 = '{ZH},' ; iI11IiIiiII1 = '{IX},' ; I11iii1i = '{LM},'
if 29 - 29: ii . IIiIiII11i % OOooOOo
def IiiIi1I11 ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 OO0oOO0O = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( i1I1Ii11II1i )
 for url , oOOoooO0O0 , OOoOooOoOOOoo , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( ( oOOoooO0O0 ) . replace ( 'Sezon' , ' Season ' ) + ( OOoOooOoOOOoo ) . replace ( 'Bölüm' , ' Episode ' ) + IiiiiI1i1Iii , url , 8063 , '' )
  if 83 - 83: iIIIIii1
  if 30 - 30: I1ii11iIi11i
  if 8 - 8: o0o00Oo0O + oo0OO + IiI11iII1
  if 47 - 47: O0o0Ooo
def Oooo0O0Oooo ( url ) :
 i1I1Ii11II1i = cloudflare . source ( url )
 OO0oOO0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , url , 222 , '' )
  if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
  if 48 - 48: iIIIIii1
  if 96 - 96: oo0OO / o0o00Oo0O . IIiIiII11i + iIIIIii1 % I11i
  if 67 - 67: o0o00Oo0O % IiI11iII1
def III ( ) :
 if 48 - 48: OoO0O0 . OoO0O0 + Ii + Ii1I % o0o00Oo0O
 i1I1Ii11II1i = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 OO0oOO0O = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( i1I1Ii11II1i )
 for O0o , IiIi1I1 , IiiiiI1i1Iii , OOoOooOoOOOoo in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii + '  -  ' + ( OOoOooOoOOOoo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0o , 8063 , IiIi1I1 )
  if 67 - 67: OOO00O / O0o0Ooo * oOo0O0Ooo % ii
def ii1IIiI1iI1i ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 8002 , IiIi1I1 )
def IIiII11 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oOoO0 )
 for IiIi1I1 , time , url , IiiiiI1i1Iii , iIiIIi in OO0oOO0O :
  iiIiII1 ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , time ) , url , 1015 , IiIi1I1 , iIiIIi )
  if 58 - 58: O0o0O0O0ooO0
def I11IIIII ( ) :
 if 53 - 53: ii . ii + I11i - O0o0O0O0ooO0 + OoO0O0
 IIIIIii1ii11 ( 'Coronation Street' , '' , 8001 , '' )
 IIIIIii1ii11 ( 'Eastenders' , '' , 8002 , '' )
 IIIIIii1ii11 ( 'Emmerdale' , '' , 8003 , '' )
 IIIIIii1ii11 ( 'Hollyoaks' , '' , 8004 , '' )
 IIIIIii1ii11 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 44 - 44: IiI11iII1 - iIIIIii1
 if 100 - 100: oo0OO . oO0o - o0Oo0O0Oo00oO + o0o00Oo0O * oO0o
 if 59 - 59: IIiIiII11i
 if 43 - 43: I1ii11iIi11i + ii
def i1I111iIii1i1 ( ) :
 O0OOO0OOoO0O = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 OO0oOO0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'Holly' in IiiiiI1i1Iii :
   IiIi1I1 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in O0o :
    iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o . replace ( '\\/' , '/' ) , 8006 , IiIi1I1 )
   else :
    pass
    if 80 - 80: IiI11iII1 / Ii + ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 38 - 38: Ii1I % OOO00O + ooOoO0O00 * ii * oo0OO
def OoO0o0OO ( ) :
 O0OOO0OOoO0O = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 OO0oOO0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'East' in IiiiiI1i1Iii :
   IiIi1I1 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in O0o :
    iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o . replace ( '\\/' , '/' ) , 8006 , IiIi1I1 )
   else :
    pass
    if 10 - 10: oo0OO - O0o0O0O0ooO0 % IIiIiII11i - IiI11iII1 - ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1I - O0o0Ooo . IiI11iII1
def iiIIIi1iIi ( ) :
 O0OOO0OOoO0O = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 OO0oOO0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'Emmer' in IiiiiI1i1Iii :
   IiIi1I1 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in O0o :
    iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o . replace ( '\\/' , '/' ) , 8006 , IiIi1I1 )
   else :
    pass
    if 79 - 79: OoO0O0 % IiI11iII1 / oo0OO - iI11I1II1I1I - OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: IIiIiII11i
def oO0OOoo ( ) :
 O0OOO0OOoO0O = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 OO0oOO0O = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'Coro' in IiiiiI1i1Iii :
   IiIi1I1 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in O0o :
    iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o . replace ( '\\/' , '/' ) , 8006 , IiIi1I1 )
   else :
    pass
    if 96 - 96: OoO0O0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: O0o0O0O0ooO0 * ii
def iIi11III ( ) :
 O0OOO0OOoO0O = O0 ( 'http://uksoapshare.blogspot.co.uk/' )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'Celeb' in IiiiiI1i1Iii :
   IiIi1I1 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in O0o :
    iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0o . replace ( '\\/' , '/' ) , 8006 , IiIi1I1 )
   else :
    pass
    if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
def i1iI1IIi1I ( name , url ) :
 oo00i1i11I1I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oo00i1i11I1I1 :
  OOOOOoooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oOoO0 = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( oOoO0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oOoO0 = open_url ( url )
  oO0Oooo0OoO = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( oOoO0 ) [ - 1 ]
  OOOOOoooO = oO0Oooo0OoO . replace ( '\\/' , '/' )
 iIIii1 = xbmcgui . ListItem ( name , '' , '' )
 iIIii1 . setPath ( OOOOOoooO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIii1 )
 if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . o0Oo0O0Oo00oO + Ii1I * I1ii11iIi11i
 if 61 - 61: IIiIiII11i . iIIIIii1 - o0o00Oo0O * iIIIIii1
def Iii1I ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 OO0oOO0O = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , O0o , 7071 , Oo0oOOo + 'popcorn.png' )
 for O0o , IiiiiI1i1Iii in oOiIi1IIIi1 :
  IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , O0o , 7071 , Oo0oOOo + 'popcorn.png' )
  if 100 - 100: ii . I1ii11iIi11i / Ii1I
def I11i1I11iIii ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OO0oOO0O = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'Movies' in IiiiiI1i1Iii :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( O0o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , Oo0oOOo + 'popcorn.png' )
def O0OOo ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oOoO0 )
 OO0oOO0O = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oOoO0 )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiIi1I1 )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , Oo0oOOo + 'Next.png' )
  if 62 - 62: OOooOOo % OOO00O * iI11I1II1I1I
  if 38 - 38: Ii . iI11I1II1I1I . OoO0O0 / oO0o
def iI1111i1i1ii ( url ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 OO0oOO0O = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url , IiIi1I1 in OO0oOO0O :
  if '{{' in IiiiiI1i1Iii :
   pass
  else :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IiIi1I1 )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
OooOo = '{UJ},' ; O0OOoOOO0o0o = '{WE},' ; iIOoo0ooo0oo = '{WP},' ; I11iIiI1 = '{PP},'
def i1I1iiii1Ii11 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url , IiIi1I1 in OO0oOO0O :
  if '{{' in IiiiiI1i1Iii :
   pass
  else :
   IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IiIi1I1 )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIIIi ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  Oo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 222 , Oo0oOOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: oO0o % oO0o / I11i - OOooOOo
 if 44 - 44: OOO00O - o0o00Oo0O / IIiIiII11i . iI11I1II1I1I . ooOoO0O00
 if 63 - 63: iI11I1II1I1I + iIIIIii1 % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def OO0iiiii1iiIIii ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if '(cooltvseries.com)' in IiiiiI1i1Iii :
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , Oo0oOOo + 'CoolSeries.png' )
 for url , IiiiiI1i1Iii in oOiIi1IIIi1 :
  if '(cooltvseries.com)' in IiiiiI1i1Iii :
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , Oo0oOOo + 'CoolSeries.png' )
def II1IIii1I11I ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OOOO0o0 ( ( url ) . replace ( ' ' , '%20' ) )
ii1IiIIiI11111Ii = '{XX},' ; O0OOoO0o0O0 = '{UD},' ; OO0Oo00OO0oo = '{YT},' ; oOO00o0O0 = '{JS},' ; iIIii1iiiIiiI = '{PF},'
if 67 - 67: IIiIiII11i
def iI1iii1iIiiI ( ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 OO0oOO0O = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  iIi1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( O0o ) ) , 222 , IiIi1I1 )
  if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / OoO0O0
def IiiIiiIIII ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oOoO0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oOoO0 )
 for IiIi1I1 , url , IiiiiI1i1Iii in OO0oOO0O :
  if 'youtu' in url :
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IiIi1I1 )
 for url in next :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , Oo0oOOo + 'Next.png' )
  if 88 - 88: oO0o . IiI11iII1 / O0o0Ooo
def iIiI1I1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 62 - 62: I11i / iI11I1II1I1I
def O0OOoOoo0OOo ( url ) :
 oOoO0 = O0
 OO0oOO0O = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 222 , IiIi1I1 )
  if 30 - 30: o0o00Oo0O / OoO0O0 % O0o0Ooo
  if 6 - 6: O0o0Ooo . OOooOOo
  if 23 - 23: oOo0O0Ooo * OOO00O / OOooOOo . iI11I1II1I1I % Ii
  if 61 - 61: o0o00Oo0O
  if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( ) :
 if 75 - 75: IIiIiII11i + OOO00O % OoO0O0 + I1ii11iIi11i
 IIIIIii1ii11 ( 'All Channels' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Entertainment' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Movies' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Music' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'News' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Sports' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Documentary' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Kids' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Food' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Religious' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'USA Channels' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 IIIIIii1ii11 ( 'Other' , '' , 7021 , Oo0oOOo + 'livetv.png' )
 if 70 - 70: oO0o
 if 43 - 43: OOooOOo
def oO0Oo ( Cat_Name ) :
 if 91 - 91: O0o0Ooo + OOO00O / iIIIIii1 + oOo0O0Ooo - I1ii11iIi11i % o0o00Oo0O
 oO00o0oO0O = False
 iI11Iii1I = '0'
 if Cat_Name == 'All Channels' : oO00o0oO0O = True
 if Cat_Name == 'Entertainment' : iI11Iii1I = '1'
 if Cat_Name == 'Movies' : iI11Iii1I = '2'
 if Cat_Name == 'Music' : iI11Iii1I = '3'
 if Cat_Name == 'News' : iI11Iii1I = '4'
 if Cat_Name == 'Sports' : iI11Iii1I = '5'
 if Cat_Name == 'Documentary' : iI11Iii1I = '6'
 if Cat_Name == 'Kids' : iI11Iii1I = '7'
 if Cat_Name == 'Food' : iI11Iii1I = '8'
 if Cat_Name == 'Religious' : iI11Iii1I = '9'
 if Cat_Name == 'USA Channels' : iI11Iii1I = '10'
 if Cat_Name == 'Other' : iI11Iii1I = '11'
 if 62 - 62: iIIIIii1 . o0o00Oo0O . iI11I1II1I1I
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OO0oOO0O = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oOoO0 )
 print 'Len Match: >>>' + str ( len ( OO0oOO0O ) )
 for IiiiiI1i1Iii , IiIi1I1 , oOoo0OO0 in OO0oOO0O :
  iiIiIi1111iI1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiIi1I1 ) . replace ( '\\' , '' )
  if oOoo0OO0 == iI11Iii1I :
   IIIIIii1ii11 ( IiiiiI1i1Iii , '' , 7022 , iiIiIi1111iI1 )
  elif oO00o0oO0O == True :
   IIIIIii1ii11 ( IiiiiI1i1Iii , '' , 7022 , iiIiIi1111iI1 )
  else : pass
  if 94 - 94: OOO00O % O0o0Ooo % ooOoO0O00
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 90 - 90: o0Oo0O0Oo00oO * oO0o
def I1i ( Search_Name ) :
 oOoO0 = O0 ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 OO0oOO0O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOoO0 )
 OO0oOO0O = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( oOoO0 )
 for IiIi1I1 , O0o , iI1i11 , ooo00Ooo in OO0oOO0O :
  iiIiIi1111iI1 = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IiIi1I1 ) . replace ( '\\' , '' )
  iIi1IIiI ( Search_Name + ': Link 1' , ( O0o ) . replace ( '\\' , '' ) , 222 , iiIiIi1111iI1 )
  iIi1IIiI ( Search_Name + ': Link 2' , ( iI1i11 ) . replace ( '\\' , '' ) , 222 , iiIiIi1111iI1 )
  iIi1IIiI ( Search_Name + ': Link 3' , ( ooo00Ooo ) . replace ( '\\' , '' ) , 222 , iiIiIi1111iI1 )
  if 77 - 77: IiI11iII1 * OoO0O0 / OOO00O + Ii1I
def iiii11i ( ) :
 oOoO0 = O0 ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OO0oOO0O = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , ( O0o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , Oo0oOOo + 'english.png' )
def Oo00OOOoo0 ( ) :
 oOoO0 = O0 ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 OO0oOO0O = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , ( O0o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , Oo0oOOo + 'xxx.png' )
def O0OOOOO ( ) :
 oOoO0 = O0 ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 OO0oOO0O = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , O0o in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , ( O0o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , Oo0oOOo + 'vod(1).png' )
  if 14 - 14: oO0o
def i1iIii ( url ) :
 url
 O0o00I1IIi1iI1iiI = xbmcgui . ListItem ( IiiiiI1i1Iii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0o00I1IIi1iI1iiI )
 return
 if 27 - 27: iI11I1II1I1I % O0o0Ooo - IiI11iII1
 if 67 - 67: o0o00Oo0O / IiI11iII1 * o0Oo0O0Oo00oO % OOO00O . Ii1I * oo0OO
def IiiiIIIi11ii1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oOoO0 )
 for url , iIIiIiI1I1 , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IiIi1I1 , '' , ( iIIiIiI1I1 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 for url in oOiIi1IIIi1 :
  IIIIIii1ii11 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , Oo0oOOo + 'Next.png' )
  if 82 - 82: OoO0O0 * Ii1I % o0Oo0O0Oo00oO . OoO0O0
def iI1oOoo ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for url , iIIiIiI1I1 , IiIi1I1 in OO0oOO0O :
  o0O0OOO0Ooo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IiIi1I1 , '' , iIIiIiI1I1 )
  i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 OoOOOO0O0oO0 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for o00O0o00oo in OoOOOO0O0oO0 :
  iIiiII = ( o00O0o00oo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiIiII1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IiIi1I1 , '' , iIiiII )
  if 13 - 13: IIiIiII11i
def oO0o000oOO ( INFO ) :
 OOOO0oo0 ( 'info for workout' , INFO )
 if 27 - 27: o0o00Oo0O - O0o0Ooo * IIiIiII11i - iI11I1II1I1I / OOO00O
 if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % OoO0O0 * OOooOOo - iI11I1II1I1I
 if 50 - 50: IIiIiII11i
def IiIIiiiIi ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , url , 9031 , Oo0oOOo + 'icon.png' )
def IiI111 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , url , 9032 , Oo0oOOo + 'icon.png' )
def OO0OO00ooO0 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  if '://' in IiiiiI1i1Iii :
   pass
   iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , Oo0oOOo + 'icon.png' )
def OOOOOoO00oo00 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  iIi1IIiI ( IiiiiI1i1Iii , url , 222 , Oo0oOOo + 'icon.png' )
  if 9 - 9: oOo0O0Ooo - I1ii11iIi11i
  if 62 - 62: o0Oo0O0Oo00oO - oo0OO % iI11I1II1I1I
  if 57 - 57: ii / OOooOOo
def iI1ii1iIiii1i ( ) :
 oOoO0 = O0 ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 OO0oOO0O = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  if 'category' in O0o :
   IIIIIii1ii11 ( IiiiiI1i1Iii , 'http://www.disclose.tv/' + O0o , 7010 , Oo0oOOo + 'disclose.png' )
   if 87 - 87: oo0OO
   if 15 - 15: iI11I1II1I1I . OoO0O0 . Ii1I * Ii
def ooo00O0OOo ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oOoO0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii , IiIi1I1 in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , 'http://www.disclose.tv/' + url , 7011 , IiIi1I1 )
 for url in next :
  IIIIIii1ii11 ( 'NEXT' , url , 7010 , Oo0oOOo + 'Next.png' )
  if 45 - 45: oOo0O0Ooo / O0o0O0O0ooO0 + oo0OO + iIIIIii1
  if 15 - 15: oOo0O0Ooo % oO0o
def oOoo00oO0O0OO ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oOoO0 )
 ooO0O0o0 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  if 'http' in url :
   iIi1IIiI ( 'video/flv' , url , 222 , Oo0oOOo + 'disclose.png' )
 for url , IiiiiI1i1Iii in oOiIi1IIIi1 :
  iIi1IIiI ( IiiiiI1i1Iii , url , 222 , Oo0oOOo + 'disclose.png' )
 for url in ooO0O0o0 :
  iIi1IIiI ( 'YT Link' , url , 8043 , Oo0oOOo + 'disclose.png' )
  if 35 - 35: Ii % O0o0Ooo
  if 39 - 39: o0o00Oo0O . ooOoO0O00 * Ii1I - oO0o - O0o0O0O0ooO0 % I11i
def iIi1iii1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , Oo0oOOo + 'icon.png' )
  if 37 - 37: iI11I1II1I1I % O0o0Ooo / iIIIIii1
def i1IIIII1 ( name , url , img ) :
 O0OOO0OOoO0O = O0 ( url )
 IIIiiiiiI1I = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 O0oooO00ooO0 = len ( IIIiiiiiI1I )
 if 99 - 99: iIIIIii1
 if 92 - 92: oO0o + O0o0Ooo - iIIIIii1 . Ii1I * OOO00O - Ii
 if O0oooO00ooO0 == 1 :
  for oOO0oOo in IIIiiiiiI1I :
   oOO0oOo = oOO0oOo . replace ( 'player' , 'watch' )
   I1i1IIIIIII1 = oOO0oOo + '&fv=&sou='
   iI1I1I = O0 ( I1i1IIIIIII1 )
   ii11 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( iI1I1I )
   for iI1ii in ii11 :
    oOOooooO = False
    Resolve ( iI1ii )
    if 89 - 89: OOO00O * o0Oo0O0Oo00oO
 elif O0oooO00ooO0 > 1 :
  if 93 - 93: ooOoO0O00 . o0Oo0O0Oo00oO * IiI11iII1 . OOO00O
  for oOO0oOo in IIIiiiiiI1I :
   O0iI1I1ii11IIi1 = O0 ( oOO0oOo )
   OOoOOoOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( O0iI1I1ii11IIi1 )
   O0O00I1iIiiI11 = OOoOOoOO
   O0O00I1iIiiI11 = ( str ( O0O00I1iIiiI11 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0O00I1iIiiI11
   iIi1IIiI ( 'DOUBLE LINK' , O0O00I1iIiiI11 , 424 , '' )
   if 27 - 27: O0o0O0O0ooO0
   for url in OOoOOoOO :
    IIIIIii1ii11 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iI1i11 = Google . resolve ( url )
    except :
     pass
    try :
     o000 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iI1i11 ) )
     for oOiiIIIII , iiI1 in o000 :
      if 40 - 40: o0o00Oo0O + iIIIIii1 . o0Oo0O0Oo00oO
      HD_URLS . append ( oOiiIIIII )
      SD_URLS . append ( iiI1 )
    except :
     pass
 else :
  pass
  if 29 - 29: OoO0O0 / OOooOOo . iI11I1II1I1I / O0o0Ooo % OOooOOo % O0o0O0O0ooO0
def iiI1oooOOO0o0O0 ( ) :
 if 31 - 31: ii - oo0OO / IiI11iII1
 if 62 - 62: Ii - O0o0Ooo
 IIIIIii1ii11 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , Oo0oOOo + 'Movies.png' )
 if 81 - 81: O0o0Ooo
 IIIIIii1ii11 ( 'Search Movies' , '' , 7017 , Oo0oOOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: OoO0O0 - I1ii11iIi11i - ii / iIIIIii1 - ooOoO0O00
 if 81 - 81: ooOoO0O00 / IiI11iII1 % Ii . iI11I1II1I1I * OOooOOo + ii
def iiii1Ii1iii ( ) :
 oOoO0 = O0 ( 'http://cnfstudio.com/' )
 OO0oOO0O = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , 'http://cnfstudio.com/genre/' + O0o , 7003 , Oo0oOOo + 'icon.png' )
  if 73 - 73: Ii + oo0OO % O0o0Ooo . ii % oo0OO
oooOOOOO = xbmcgui . Dialog ( )
if 32 - 32: Ii - IIiIiII11i
iIii1II1I = '{UN},' ; iIIIii1 = '{IG},' ; iIIi11 = '{PL},' ; iIiiII1Ii1ii = '{LO},' ; iIIi1 = '{LP},' ; OoOo0O00 = '{HA},' ; iI1i1iI1iI = '{XD},' ; I1IIiIi = '{TA},' ; OOOOoOoO = '{DP},' ; OO000 = '{JT},' ; o0oOoo0o = '{JJ},' ; IiiIiIIi = '{MM},' ; O00Oo = '{FQ},' ; oOOoo = '{HH},'
if 74 - 74: iI11I1II1I1I / o0Oo0O0Oo00oO
def O0Oo0 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oOoO0 )
 Oo00o0o = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oOoO0 )
 for IiIi1I1 , url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IiIi1I1 )
 Oo00o0o = Oo00o0o
 for url in Oo00o0o :
  IIIIIii1ii11 ( 'Next Page' , url , 7003 , Oo0oOOo + 'Next.png' )
  if 17 - 17: iIIIIii1 / I11i . OoO0O0 + I11i / Ii1I . I1ii11iIi11i
def iII11 ( url ) :
 if 96 - 96: O0o0Ooo * Ii1I * o0Oo0O0Oo00oO + Ii1I % oOo0O0Ooo + Ii
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OOOOi11i1 = url + '&fv=&sou='
  OOOOi11i1 = OOOOi11i1 . replace ( 'player' , 'watch' )
  i1iI11Ii1i = Iii1Iii ( OOOOi11i1 )
  iiI11111II = Iii1Iii ( url )
  if 48 - 48: O0o0O0O0ooO0 % Ii . ii * iIIIIii1 % oO0o . O0o0O0O0ooO0
  if 6 - 6: o0o00Oo0O . OOO00O - oo0OO / Ii
def Iii1Iii ( url ) :
 if 84 - 84: O0o0Ooo / Ii1I * I11i * oO0o * OoO0O0 * o0o00Oo0O
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  OoOOoooOO0O ( url )
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
  if 75 - 75: IIiIiII11i . oOo0O0Ooo + OoO0O0 - OOooOOo - o0o00Oo0O . O0o0Ooo
def I11iIi1i1I1i1 ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , Oo0oOOo + 'LocalM3U.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , Oo0oOOo + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 14 - 14: O0o0Ooo
def iii1i ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  IIIIIIi1IIi1I11i = open ( oOo0oooo00o , 'r' )
  for O0o00I1IIi1iI1iiI in IIIIIIi1IIi1I11i :
   O0o0oOooOoo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0o00I1IIi1iI1iiI )
   for IiiiiI1i1Iii , O0o in O0o0oOooOoo :
    iIi1IIiI ( IiiiiI1i1Iii , O0o , 222 , Oo0oOOo + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 59 - 59: Ii1I + O0o0Ooo . oo0OO
def oOOo0oO ( url ) :
 if os . path . exists ( Remote ) :
  O0OOO0OOoO0O = Oo0 ( url )
  OO0oOO0O = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
  for IiiiiI1i1Iii , url in OO0oOO0O :
   url = ( url ) . strip ( )
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 19 - 19: O0o0O0O0ooO0
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + OoO0O0
def ooOOO00Ooo ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 OO0oOO0O = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( O0OOO0OOoO0O )
 for O0o in OO0oOO0O :
  O0o = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + O0o
 IiiiiI1i1Iii = 'plugin.video.GenieTv'
 if 31 - 31: o0Oo0O0Oo00oO * I11i * o0Oo0O0Oo00oO + oO0o * I11i . IiI11iII1
 Oo00oo00o00Oo ( O0o , IiiiiI1i1Iii )
 if 1 - 1: iIIIIii1
def IIII ( ) :
 O0OOO0OOoO0O = O0 ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 OO0oOO0O = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( O0OOO0OOoO0O )
 for O0o in OO0oOO0O :
  O0o = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + O0o
 IiiiiI1i1Iii = 'repository.GenieTv'
 if 31 - 31: ooOoO0O00
 Oo00oo00o00Oo ( O0o , IiiiiI1i1Iii )
 if 21 - 21: ooOoO0O00
 if 69 - 69: OOooOOo + OOooOOo + OoO0O0 % OoO0O0 * O0o0Ooo % o0Oo0O0Oo00oO
def ii1111IIiI1 ( ) :
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , Oo0oOOo + 'Catagories.png' , i1iIIi1 , '' )
 iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , Oo0oOOo + 'Search.png' , i1iIIi1 , '' )
 if 59 - 59: o0Oo0O0Oo00oO - I1ii11iIi11i
 if 34 - 34: o0Oo0O0Oo00oO - oo0OO * ii . oO0o / oOo0O0Ooo
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
oO0o0 = 'https://addons.tvaddons.ag/'
if 43 - 43: OoO0O0
def o0IiiIIII1I1i ( ) :
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 OO0 = 'https://addons.tvaddons.ag/search/?keyword=' + OOIi1iI111II1I1
 O0OOO0OOoO0O = O0 ( OO0 )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0OOO0OOoO0O )
 for O0o , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , O0o , 10054 , 'https://addons.tvaddons.ag/' + OO0O0OOo0O , i1iIIi1 , '' )
  if 26 - 26: O0o0O0O0ooO0 - I1ii11iIi11i + oOo0O0Ooo + I11i
  if 37 - 37: I11i * OoO0O0 + oOo0O0Ooo . Ii1I * ii
def OoooOO0 ( ) :
 O0OOO0OOoO0O = O0 ( oO0o0 )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0OOO0OOoO0O )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  if 'Repositories' in IiiiiI1i1Iii :
   pass
  elif 'Services' in IiiiiI1i1Iii :
   pass
  elif 'International' in IiiiiI1i1Iii :
   pass
  else :
   iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , O0o , 10053 , 'https://addons.tvaddons.ag/' + IiIi1I1 , i1iIIi1 , '' )
   if 69 - 69: IIiIiII11i + O0o0O0O0ooO0
   if 55 - 55: Ii + oOo0O0Ooo
def Addon ( url ) :
 O0OOO0OOoO0O = O0 ( url )
 Oo0ooo = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( O0OOO0OOoO0O )
 for url in Oo0ooo :
  iiIiII1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , Oo0oOOo + 'Next.png' , i1iIIi1 , '' )
 OO0oOO0O = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( O0OOO0OOoO0O )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  if 'Please' in IiiiiI1i1Iii :
   pass
  else :
   iiIiII1 ( IiiiiI1i1Iii , url , 10054 , 'https://addons.tvaddons.ag/' + IiIi1I1 , i1iIIi1 , '' )
   if 73 - 73: IIiIiII11i + OoO0O0 * O0o0O0O0ooO0 / O0o0O0O0ooO0
   if 74 - 74: o0o00Oo0O + iI11I1II1I1I + oo0OO * iIIIIii1
def I1o0 ( url , name ) :
 O0OOO0OOoO0O = O0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)"' ) . findall ( O0OOO0OOoO0O )
 for url in OO0oOO0O :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   I11IIiIiI = os . path . join ( iI11 , name + '.zip' )
   try :
    os . remove ( I11IIiIiI )
   except :
    pass
   downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
   iIOo0O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iIOo0O
   print '======================================='
   extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
   iiIiI1i1 ( )
   if 26 - 26: O0o0O0O0ooO0 * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
def Oo00oo00o00Oo ( url , name ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 I11IIiIiI = os . path . join ( iI11 , name + '.zip' )
 try :
  os . remove ( I11IIiIiI )
 except :
  pass
 downloader . download ( url , I11IIiIiI , Oo0oO0ooo )
 iIOo0O = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIOo0O
 print '======================================='
 extract . all ( I11IIiIiI , iIOo0O , Oo0oO0ooo )
 iiIiI1i1 ( )
 if 52 - 52: o0Oo0O0Oo00oO / OOooOOo + oO0o % o0Oo0O0Oo00oO % OoO0O0 / oo0OO
def iiIiI1i1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 91 - 91: oO0o / oO0o . IIiIiII11i . OOO00O - oOo0O0Ooo
 if 23 - 23: oOo0O0Ooo
def i1IIiI1iII ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , url , 1007 , OO0O0OOo0O )
def ii11ii11II ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 1006 , OO0O0OOo0O )
  if 35 - 35: I1ii11iIi11i * IIiIiII11i
  if 32 - 32: oo0OO . I1ii11iIi11i / OOO00O + OOO00O . Ii1I
def iiI1ii1Iii11I ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , iconimage , iIIiIiI1I1 , I11i1II , name in OO0oOO0O :
  if 'http' in url :
   if '.php' in url :
    oo0oO ( name , url , 1016 , iconimage , I11i1II , iIIiIiI1I1 )
   else :
    if 'youtube' in url :
     iioO0o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , I11i1II , iIIiIiI1I1 )
    else :
     iioO0o ( name , url , 222 , iconimage , I11i1II , iIIiIiI1I1 )
     i1Iii1i1I ( 'movies' , 'INFO' )
  else :
   IIiIi11 ( url , iconimage , name )
   if 77 - 77: I1ii11iIi11i - iIIIIii1
 else :
  OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
  for url , OO0O0OOo0O , name in OO0oOO0O :
   if 'http' in url :
    if '.php' in url :
     IIIIIii1ii11 ( name , url , 1016 , OO0O0OOo0O )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iIi1IIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OO0O0OOo0O )
     else :
      iIi1IIiI ( name , url , 222 , OO0O0OOo0O )
      i1Iii1i1I ( 'movies' , 'INFO' )
   else :
    IIiIi11 ( url , OO0O0OOo0O , name )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 50 - 50: oO0o % ii * IIiIiII11i
def IIiIi11 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oo0OO0O = ( url ) . replace ( iI11IiIiiII1 , 'http' ) . replace ( O0OOoO0o0O0 , '.com' ) ;
 OO0OooOOoO00OO00 = ( oo0OO0O ) . replace ( I11iii1i , 'a' ) . replace ( I1iIiI1iiiiI1 , 'b' ) . replace ( IIII1ii1 , 'c' ) . replace ( O0OOoOOO0o0o , 'd' ) . replace ( iIIi11 , 'e' ) . replace ( OO000 , 'f' ) ;
 ii11ii1iIiI1 = ( OO0OooOOoO00OO00 ) . replace ( ii1IiIIiI11111Ii , 'g' ) . replace ( OoOo0O00 , 'h' ) . replace ( OO0Oo00OO0oo , 'i' ) . replace ( iIIii1iiiIiiI , 'j' ) . replace ( OOO0O0OOo , 'k' ) . replace ( Iii1 , 'l' ) ;
 OoOo0oO0 = ( ii11ii1iIiI1 ) . replace ( i111iIi1i1 , 'm' ) . replace ( OOo00O0O , 'n' ) . replace ( oooOoO , 'o' ) . replace ( IiiIi1IiiiI , 'p' ) . replace ( OO0oooOO , 'q' ) . replace ( IIIi1iiIIiiiI , 'r' ) ;
 I1IIiIi1iI = ( OoOo0oO0 ) . replace ( oOo0 , 's' ) . replace ( iIOoo0ooo0oo , 't' ) . replace ( Iiii11 , 'u' ) . replace ( o00000O , 'v' ) . replace ( iIiiiII11 , 'w' ) . replace ( ooo00Oo0 , 'x' ) ;
 iIii1i1Ii = ( I1IIiIi1iI ) . replace ( III1iIii , 'y' ) . replace ( iiIII1i1 , 'z' ) . replace ( iIii1II1I , '.' ) . replace ( iIIIii1 , '(' ) . replace ( iIiiII1Ii1ii , ')' ) . replace ( iIIi1 , '/' ) ;
 oOOo0OOoOO0 = ( iIii1i1Ii ) . replace ( I1I1i1I1I1I1 , '1' ) . replace ( I11iIiI1 , '2' ) . replace ( IiIiIIi1IiiIi1III , '3' ) . replace ( I1IIiIi , '4' ) . replace ( OOOOoOoO , '5' ) . replace ( oOO00o0O0 , '6' ) ;
 IiIiIiiIIii = ( oOOo0OOoOO0 ) . replace ( o0oOoo0o , '7' ) . replace ( IiiIiIIi , '8' ) . replace ( O00Oo , '9' ) . replace ( oOOoo , '0' ) . replace ( IiIIIIii11i , ':' ) . replace ( oO0OOO00 , '%' ) ;
 url = ( IiIiIiiIIii ) . replace ( OooOo , '-' ) . replace ( iI1i1iI1iI , '_' ) ;
 iIi1IIiI ( name , url , 222 , iconimage ) ;
 if 77 - 77: oo0OO * OOO00O . OoO0O0 * o0Oo0O0Oo00oO % IIiIiII11i
 if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
def oOO0O0O ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for O0o , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , O0o , 1007 , OO0O0OOo0O )
def Oo0o0oOo0oO ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 1006 , OO0O0OOo0O )
  if 20 - 20: iIIIIii1 - iI11I1II1I1I
def i1I1iI1 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 oOOoO = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 oOOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOoO )
 if 28 - 28: iI11I1II1I1I * O0o0Ooo . oOo0O0Ooo
 if 78 - 78: ii . ii / o0o00Oo0O
def IiIii1i11i1 ( url ) :
 oOoO0 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOoO0 )
 for url , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  if '-dir-' in IiiiiI1i1Iii :
   IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IiIi1I1 )
  else :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' , url , 1006 , IiIi1I1 )
   if 91 - 91: ii * OOooOOo + oOo0O0Ooo
def O0ooO ( url ) :
 oOoO0 = Oo0 ( url )
 iIOO = ( 'http://afewbitsmore.com/' )
 OO0oOO0O = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if '[To Parent Directory]' in IiiiiI1i1Iii :
   IiiiiI1i1Iii = 'HOME'
   pass
  elif 'HOME' in IiiiiI1i1Iii :
   pass
  elif '.m3u' in IiiiiI1i1Iii :
   IIIIIii1ii11 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , iIOO + url , 2002 , Oo0oOOo + 'music.png' )
  elif '.mp3' in IiiiiI1i1Iii :
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iIOO + url , 222 , Oo0oOOo + 'music.png' )
  elif '.m4a' in IiiiiI1i1Iii :
   iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iIOO + url , 222 , Oo0oOOo + 'music.png' )
  else :
   IIIIIii1ii11 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) , iIOO + url , 1012 , Oo0oOOo + 'music.png' )
def I1III1I11I1 ( url ) :
 O0OOO0OOoO0O = Oo0 ( url )
 OO0oOO0O = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOO0OOoO0O )
 for IiIi1I1 , IiiiiI1i1Iii , url in OO0oOO0O :
  iIi1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + IiiiiI1i1Iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , Oo0oOOo + 'music.png' )
  if 85 - 85: IiI11iII1
def O0OoO00OoOO ( url ) :
 oOoO0 = Oo0 ( url )
 iIOO = url
 OO0oOO0O = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  if '.mp3' in IiiiiI1i1Iii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , Oo0oOOo + 'music.png' )
  else :
   IIIIIii1ii11 ( ( IiiiiI1i1Iii ) . replace ( '/' , '' ) , iIOO + url , 1011 , Oo0oOOo + 'music.png' )
def OOoOo0ooOoo ( ) :
 oOoO0 = Oo0 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 OO0oOO0O = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oOoO0 )
 for O0o , IiIi1I1 , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , ( 'http://www.cyn.net/music/' + O0o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IiIi1I1 ) . replace ( ' ' , '%20' ) )
def oO0OO00 ( url , img ) :
 oOoO0 = Oo0 ( url )
 iI1i11 = url
 img = img
 OO0oOO0O = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.mp3' , '' ) , ( iI1i11 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 16 - 16: ii / oo0OO . o0Oo0O0Oo00oO * OOO00O - oOo0O0Ooo
def iiIi ( url ) :
 oOoO0 = Oo0 ( url )
 iI1i11 = url
 OO0oOO0O = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oOoO0 )
 for type , url , IiiiiI1i1Iii in OO0oOO0O :
  if '[VID]' in type :
   iIi1IIiI ( ( IiiiiI1i1Iii ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iI1i11 + url , 222 , Oo0oOOo + 'music.png' )
  if '[DIR]' in type :
   iiIi ( iI1i11 + url )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: iI11I1II1I1I + iIIIIii1
 if 44 - 44: oO0o + O0o0Ooo % oO0o + ooOoO0O00 + O0o0O0O0ooO0 + o0o00Oo0O
def Ii1iII1ii1 ( ) :
 O0OOO0 = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOoO = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOIi1iI111II1I1 = oOoO . lower ( )
 O0o = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iI1i11 = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 ooo00Ooo = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 80 - 80: iI11I1II1I1I / Ii + O0o0O0O0ooO0
 O0OOO0OOoO0O = I11iii1Ii ( O0o )
 O00Oo000ooO0 = I11iii1Ii ( iI1i11 )
 OoO0O00 = I11iii1Ii ( ooo00Ooo )
 if 41 - 41: IiI11iII1 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
 if O0OOO0OOoO0O != 'Failed' :
  OO0oOO0O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0OOO0OOoO0O )
  for IiiiiI1i1Iii in OO0oOO0O :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0o + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if O00Oo000ooO0 != 'Failed' :
  oOiIi1IIIi1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( O0OOO0OOoO0O )
  for IiiiiI1i1Iii in oOiIi1IIIi1 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iI1i11 + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 25 - 25: ii . o0Oo0O0Oo00oO % O0o0O0O0ooO0 . iIIIIii1
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
 if OoO0O00 != 'Failed' :
  ooO0O0o0 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO0O00 )
  for IiiiiI1i1Iii in ooO0O0o0 :
   if oOoO in IiiiiI1i1Iii . lower ( ) :
    IIIIIii1ii11 ( ( IiiiiI1i1Iii + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooo00Ooo + IiiiiI1i1Iii ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 67 - 67: ii + IiI11iII1 / OOO00O
    i1Iii1i1I ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: iIIIIii1 / ii . oOo0O0Ooo + IiI11iII1 - IIiIiII11i
    if 33 - 33: iIIIIii1 / iIIIIii1 . Ii * Ii1I + I11i
    if 16 - 16: iIIIIii1
    if 10 - 10: OOooOOo . iIIIIii1 * iI11I1II1I1I - oo0OO - OOooOOo / IiI11iII1
    if 13 - 13: oo0OO + OOooOOo % iIIIIii1 % ii
    if 22 - 22: IiI11iII1
i111iIi1i1 = '{SF},' ; OOo00O0O = '{IF},' ; oooOoO = '{PW},' ; IiIiIIi1IiiIi1III = '{AM},' ; IiiIi1IiiiI = '{GF},' ; OO0oooOO = '{DD},' ; IIIi1iiIIiiiI = '{UO},' ; oOo0 = '{LE},' ; Iiii11 = '{ZY},' ; o00000O = '{UE},' ; iIiiiII11 = '{PE},' ; ooo00Oo0 = '{JE},' ; III1iIii = '{TH},' ; iiIII1i1 = '{LK},'
if 23 - 23: o0o00Oo0O
if 41 - 41: ooOoO0O00 . OoO0O0 / OOO00O / I11i % iIIIIii1 - o0Oo0O0Oo00oO
def iI1i1Iiii ( ) :
 oOoO0 = O0 ( 'http://www.iwatchseries.me/tv-list/' )
 OO0oOO0O = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , O0o , 8021 , Oo0oOOo + 'iwatch.png' )
def iiiIIII1IIi ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii , o00O00oO00 in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii + o00O00oO00 , url , 8022 , Oo0oOOo + 'iwatch.png' )
def Oo0oo0OOO0OOoOO ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oOoOII1i1 ( url )
def oOoOII1i1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oOoO0 )
 oOiIi1IIIi1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oOoO0 )
 ooO0O0o0 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( 'VidSpot - ' + IiiiiI1i1Iii , url , 222 , Oo0oOOo + 'iwatch.png' )
 for url in oOiIi1IIIi1 :
  iIi1IIiI ( 'VodLocker' , url , 222 , Oo0oOOo + 'iwatch.png' )
 for IiiiiI1i1Iii , url in ooO0O0o0 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iIi1IIiI ( 'TheVideo - ' + IiiiiI1i1Iii , url , 222 , Oo0oOOo + 'iwatch.png' )
   if 51 - 51: OOO00O * O0o0O0O0ooO0 / ooOoO0O00
def IIi1I1 ( ) :
 oOoO0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 OO0oOO0O = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , O0o , 1021 , Oo0oOOo + 'anime.png' )
  if 37 - 37: I11i * I1ii11iIi11i
  if 11 - 11: oo0OO
def Oo0O0o00o00 ( ) :
 oOoO0 = O0 ( 'http://www.animetoon.org/cartoon' )
 OO0oOO0O = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( oOoO0 )
 for O0o , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , O0o , 1002 , Oo0oOOo + 'anime.png' )
  if 90 - 90: IiI11iII1 . IIiIiII11i . Ii1I
  if 32 - 32: OOO00O - oO0o . O0o0O0O0ooO0 . O0o0O0O0ooO0 % ooOoO0O00 * o0Oo0O0Oo00oO
  if 65 - 65: O0o0O0O0ooO0 / OOO00O . IIiIiII11i
def o0oO00oooo ( url ) :
 oOoO0 = O0 ( url )
 oOiIi1IIIi1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oOoO0 )
 for IiIi1I1 in oOiIi1IIIi1 :
  IIiI1i = IiIi1I1
 ooO0O0o0 = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( oOoO0 )
 for url in ooO0O0o0 :
  IIIIIii1ii11 ( 'NEXT PAGE' , url , 1002 , Oo0oOOo + 'Next.png' )
 OO0oOO0O = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( oOoO0 )
 for url , IiiiiI1i1Iii in OO0oOO0O :
  IIIIIii1ii11 ( IiiiiI1i1Iii , url , 1003 , IIiI1i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0Oo00O ( url , IMAGE ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oOoO0 )
 for IiiiiI1i1Iii , url in OO0oOO0O :
  print IiiiiI1i1Iii + '     ' + url
  if 'easy' in url :
   I1iII1 ( url )
  elif 'playpanda' in url :
   I1iII1 ( url )
   if 70 - 70: ooOoO0O00 % OOO00O . Ii1I - iIIIIii1 + OoO0O0
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iII1 ( url ) :
 oOoO0 = O0 ( url )
 OO0oOO0O = re . compile ( "url: '(.+?)'," ) . findall ( oOoO0 )
 for url in OO0oOO0O :
  iIi1IIiI ( 'STREAM' , url , 222 , Oo0oOOo + 'anime.png' )
  if 84 - 84: oo0OO + IIiIiII11i * IIiIiII11i % I11i / O0o0O0O0ooO0 + OOO00O
  if 9 - 9: O0o0O0O0ooO0
def iIi11I1II ( url ) :
 I1IIiiIiii = urllib2 . Request ( url )
 I1IIiiIiii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 I1IIiiIiii . add_header ( 'referer' , url )
 O000oo0O = urllib2 . urlopen ( I1IIiiIiii )
 OOOOi11i1 = O000oo0O . read ( )
 O000oo0O . close ( )
 return OOOOi11i1
 if 93 - 93: Ii1I - OOO00O % Ii1I
def Oo0 ( url ) :
 I1IIiiIiii = urllib2 . Request ( url )
 I1IIiiIiii . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O000oo0O = urllib2 . urlopen ( I1IIiiIiii )
 OOOOi11i1 = O000oo0O . read ( )
 O000oo0O . close ( )
 return OOOOi11i1
 if 12 - 12: OoO0O0 + oO0o * O0o0Ooo + o0Oo0O0Oo00oO + iIIIIii1
def O0O00oOo0o000 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0oOO00 = ( '%s%s' % ( ii11iiIi , url ) )
 OOOOi11i1 = Oo0 ( url )
 OO0oOO0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOOOi11i1 )
 for url , OO0O0OOo0O , IiiiiI1i1Iii in OO0oOO0O :
  iIi1IIiI ( '%s' % ( IiiiiI1i1Iii ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , OO0O0OOo0O )
  if 85 - 85: oOo0O0Ooo % OOO00O
def OoOOoooOO0O ( url ) :
 O0OO0o0OO0OO = xbmc . Player ( I1I1i1i ( ) )
 import urlresolver
 try : O0OO0o0OO0OO . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( IiiiiI1i1Iii ) )
 O0OO0o0OO0OO = xbmc . Player ( I1I1i1i ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : O0OO0o0OO0OO . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 25 - 25: OOooOOo . IIiIiII11i * o0Oo0O0Oo00oO
def IiII111I ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % IiiiiI1i1Iii )
 xbmc . sleep ( 1 )
 O0OO0o0OO0OO = xbmc . Player ( I1I1i1i ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % IiiiiI1i1Iii )
 xbmc . sleep ( 1 )
 O0OO0o0OO0OO . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 62 - 62: ooOoO0O00 * iI11I1II1I1I % oo0OO % OOooOOo / ii
def OOOO0o0 ( url ) :
 O0OO0o0OO0OO = xbmc . Player ( I1I1i1i ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : O0OO0o0OO0OO . play ( url ) . strip ( )
 except : pass
 if 39 - 39: I1ii11iIi11i % O0o0O0O0ooO0
 if 90 - 90: oOo0O0Ooo * Ii1I . O0o0Ooo * o0Oo0O0Oo00oO - I11i
def I1I1i1i ( ) :
 try :
  IiI1 = getSet ( "core-player" )
  if ( IiI1 == 'DVDPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiI1 == 'MPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiI1 == 'PAPLAYER' ) : iII1i111iI = xbmc . PLAYER_CORE_PAPLAYER
  else : iII1i111iI = xbmc . PLAYER_CORE_AUTO
 except : iII1i111iI = xbmc . PLAYER_CORE_AUTO
 return iII1i111iI
 return True
 if 9 - 9: Ii + OoO0O0 - OOooOOo / OOO00O % ooOoO0O00 / oo0OO
def IIIIIii1ii11 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1II1II111 = [ ]
  if showcontext == 'fav' :
   iiI1II1II111 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiiiiIIii :
   iiI1II1II111 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIii1 . addContextMenuItems ( iiI1II1II111 )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = True )
 return OOoooooooO
 if 71 - 71: IIiIiII11i % IiI11iII1 + oOo0O0Ooo * OOO00O + iIIIIii1 . OOO00O
def iii1IIIiiiI ( name , url , mode , iconimage , fanart , description ) :
 if 25 - 25: OOO00O . I11i % oOo0O0Ooo + O0o0O0O0ooO0
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIii1 . setProperty ( "Fanart_Image" , fanart )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = True )
 return OOoooooooO
 if 61 - 61: oo0OO % OOO00O - Ii1I + oo0OO . OOooOOo
def iIi1IIiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiI1II1II111 = [ ]
  if showcontext == 'fav' :
   iiI1II1II111 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiiiiIIii :
   iiI1II1II111 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIii1 . addContextMenuItems ( iiI1II1II111 )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = False )
 return OOoooooooO
 if 44 - 44: Ii1I / o0o00Oo0O - iIIIIii1 + OoO0O0 . O0o0Ooo . Ii1I
 if 95 - 95: OOooOOo % IiI11iII1 % ooOoO0O00 * I11i + OoO0O0
 if 34 - 34: IiI11iII1 * I11i . oOo0O0Ooo % Ii
 if 61 - 61: iI11I1II1I1I + oo0OO * O0o0Ooo - ooOoO0O00 % oo0OO
 if 76 - 76: oo0OO / OOooOOo
 if 12 - 12: IiI11iII1
def OOOO0oo0 ( heading , announce ) :
 class OO0oOo ( ) :
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
   try : i11i1iiiII = open ( announce ) ; OOoO0ooOO = i11i1iiiII . read ( )
   except : OOoO0ooOO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OOoO0ooOO ) )
   return
 OO0oOo ( )
 OO0oOo ( )
 if 36 - 36: OOooOOo * oO0o / OOO00O / oOo0O0Ooo - o0Oo0O0Oo00oO
def o0oOo0OoO ( ) :
 OOOO0oo0 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 3 - 3: iIIIIii1 - ii * ii - oOo0O0Ooo / IiI11iII1 * Ii1I
 if 58 - 58: iIIIIii1 % iI11I1II1I1I / Ii % I11i . IiI11iII1 * O0o0O0O0ooO0
 if 32 - 32: ii + I11i
 if 91 - 91: OOO00O - IiI11iII1 * IiI11iII1
 if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
def iiIiI1i1 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 24 - 24: oO0o / IiI11iII1 + O0o0O0O0ooO0 * O0o0Ooo * O0o0O0O0ooO0
 if 10 - 10: oOo0O0Ooo - Ii1I - I1ii11iIi11i - I11i
 if 21 - 21: ii + IiI11iII1
 if 43 - 43: Ii . Ii1I . oo0OO
 if 31 - 31: o0Oo0O0Oo00oO % I11i % IiI11iII1 . Ii1I / I11i * oo0OO
 if 74 - 74: oOo0O0Ooo . OOO00O / O0o0O0O0ooO0 . iIIIIii1
 if 74 - 74: I1ii11iIi11i / IiI11iII1 % IiI11iII1 . iIIIIii1
 if 72 - 72: ooOoO0O00
 if 21 - 21: IiI11iII1 . OoO0O0 / Ii * ooOoO0O00
 if 82 - 82: OOO00O * I1ii11iIi11i % Ii * ooOoO0O00 . OoO0O0
 if 89 - 89: iIIIIii1 - ooOoO0O00 - iIIIIii1
 if 74 - 74: oO0o % oO0o
 if 28 - 28: OOooOOo % oo0OO - OoO0O0 + OoO0O0 + oo0OO / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * OoO0O0
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % o0Oo0O0Oo00oO
 if 81 - 81: oO0o - iI11I1II1I1I
 if 60 - 60: IiI11iII1
 if 77 - 77: oOo0O0Ooo / Ii1I
 if 95 - 95: IiI11iII1 * ooOoO0O00 + oo0OO
 if 40 - 40: IIiIiII11i
 if 7 - 7: OoO0O0 / oO0o
 if 88 - 88: ooOoO0O00
 if 53 - 53: OOO00O . OoO0O0 . I11i + oo0OO
def IiiiII ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + OoOo00OoOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 62 - 62: OOooOOo * ii * I11i
def ii111Ii1i ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + IiI1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / O0o0Ooo
def ii1IO0OOoooO ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + IIiiIiIIiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 39 - 39: O0o0Ooo / ii - o0Oo0O0Oo00oO + oO0o / OOooOOo
def oo0O0000oo0o0 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + Iii1I1I1iiI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 42 - 42: ii - OOooOOo - OoO0O0 * IiI11iII1
def OO0iii111 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + o00O000oooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 100 - 100: OOO00O % O0o0Ooo / o0o00Oo0O * o0Oo0O0Oo00oO - Ii
def o0oo ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + O0oooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 5 - 5: OOooOOo % Ii1I . OOO00O . O0o0Ooo - Ii
def Ii11I1 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + OO00OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 27 - 27: o0o00Oo0O * oOo0O0Ooo - iI11I1II1I1I - O0o0O0O0ooO0 % o0o00Oo0O . I1ii11iIi11i
def I1ii11IiI1I ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + Oo0Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 96 - 96: o0Oo0O0Oo00oO
def iio0Oo ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + IiiiiiiI111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 42 , oo0O0o00o0O , I11i1II , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 19 - 19: ii * oo0OO
def OoO00OO0 ( url ) :
 OOOOi11i1 = O0 ( str ( o0ooOooo000oOO ) + IiI1i11i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0oOO0O = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OOOOi11i1 )
 for IiiiiI1i1Iii , url , oo0O0o00o0O , I11i1II , OOOOO0O00 in OO0oOO0O :
  iiIiII1 ( IiiiiI1i1Iii , url , 5 , Oo0oOOo + 'GenieTVRSSFeed.png' , Oo0oOOo + 'GenieTVRSSFeed.png' , OOOOO0O00 )
 i1Iii1i1I ( 'movies' , 'MAIN' )
 if 92 - 92: OoO0O0 % IIiIiII11i . O0o0O0O0ooO0
 if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
 if 47 - 47: O0o0O0O0ooO0 * OOooOOo * iIIIIii1
 if 46 - 46: o0Oo0O0Oo00oO
 if 42 - 42: iI11I1II1I1I
 if 32 - 32: I1ii11iIi11i - o0Oo0O0Oo00oO . ii - ii - I1ii11iIi11i . iI11I1II1I1I
 if 34 - 34: I1ii11iIi11i
 if 31 - 31: ooOoO0O00 - O0o0Ooo + IiI11iII1 + OOO00O . OOO00O . o0o00Oo0O
 if 33 - 33: ooOoO0O00 / O0o0O0O0ooO0 * oO0o
def iI1ii1 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooOo , iI1 , OoOo00o0OO in os . walk ( oOOoO0 ) :
     O0oOOoii111IIiiiiI = 0
     O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
     if O0oOOoii111IIiiiiI > 0 :
      for i11i1iiiII in OoOo00o0OO :
       os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
  oo0OOoOo0 = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( oo0OOoOo0 )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 63 - 63: OOooOOo
 if 61 - 61: IIiIiII11i * o0Oo0O0Oo00oO + IIiIiII11i % O0o0O0O0ooO0 . ooOoO0O00 . oo0OO
 if 33 - 33: iI11I1II1I1I + oOo0O0Ooo / oo0OO * O0o0O0O0ooO0 - oo0OO
 if 96 - 96: O0o0Ooo . ii % IIiIiII11i % o0Oo0O0Oo00oO
 if 43 - 43: IIiIiII11i . Ii . o0Oo0O0Oo00oO - OOooOOo . IiI11iII1
 if 15 - 15: Ii1I - iI11I1II1I1I % IIiIiII11i / O0o0Ooo
 if 46 - 46: iI11I1II1I1I
 if 96 - 96: iIIIIii1
 if 56 - 56: O0o0Ooo / oo0OO - oo0OO
def iiiII1i1iiii ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 O00O = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( O00O ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( O00O ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 42 - 42: I11i + oo0OO - ii + O0o0O0O0ooO0 % oO0o
   if 12 - 12: ooOoO0O00 / Ii1I - O0o0O0O0ooO0 . Ii / ooOoO0O00 / ii
   if O0oOOoii111IIiiiiI > 0 :
    if 88 - 88: o0Oo0O0Oo00oO / Ii % OOooOOo % OoO0O0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: Ii1I . Ii1I / O0o0Ooo . Ii1I
     for i11i1iiiII in OoOo00o0OO :
      try :
       os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
      except :
       pass
     for iI1IIIii in iI1 :
      try :
       shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      except :
       pass
       if 37 - 37: ooOoO0O00 . IiI11iII1 - IIiIiII11i % I11i - ooOoO0O00 . oo0OO
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  iiiiI = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 66 - 66: ii + O0o0O0O0ooO0 . iIIIIii1 % ooOoO0O00
  for ooOo , iI1 , OoOo00o0OO in os . walk ( iiiiI ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 58 - 58: OoO0O0 % O0o0O0O0ooO0 * o0o00Oo0O + Ii1I - iIIIIii1
   if O0oOOoii111IIiiiiI > 0 :
    if 26 - 26: ooOoO0O00 / oOo0O0Ooo / O0o0Ooo + O0o0Ooo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 46 - 46: IiI11iII1 % Ii1I + o0Oo0O0Oo00oO
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / O0o0Ooo + OOO00O
   else :
    pass
  i11IiIiii = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 15 - 15: OOO00O * iI11I1II1I1I * oo0OO
  for ooOo , iI1 , OoOo00o0OO in os . walk ( i11IiIiii ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 96 - 96: IiI11iII1 * iI11I1II1I1I / OOooOOo % OoO0O0 * IIiIiII11i
   if O0oOOoii111IIiiiiI > 0 :
    if 3 - 3: OoO0O0 . I1ii11iIi11i / Ii + oO0o
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 47 - 47: iIIIIii1 . OoO0O0
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 96 - 96: O0o0Ooo % IIiIiII11i / OOO00O % OoO0O0 / OOO00O % Ii
   else :
    pass
    if 57 - 57: O0o0Ooo - O0o0Ooo % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
    if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - o0Oo0O0Oo00oO * iI11I1II1I1I
    if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oo0OO * I11i + OoO0O0
    if 89 - 89: OOO00O * oOo0O0Ooo . oo0OO
 O000O000 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( O000O000 ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( O000O000 ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 55 - 55: IIiIiII11i - IiI11iII1 - OoO0O0 % o0Oo0O0Oo00oO
   if 49 - 49: I1ii11iIi11i * IiI11iII1
   if O0oOOoii111IIiiiiI > 0 :
    if 53 - 53: I1ii11iIi11i / o0Oo0O0Oo00oO + oo0OO . O0o0O0O0ooO0 + iIIIIii1
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: o0Oo0O0Oo00oO
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 51 - 51: iI11I1II1I1I
   else :
    pass
    if 8 - 8: oO0o / I11i % O0o0O0O0ooO0 . Ii . ii . o0Oo0O0Oo00oO
    if 8 - 8: oO0o * I1ii11iIi11i
 IIiIIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( IIiIIII ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( IIiIIII ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 4 - 4: O0o0Ooo . iIIIIii1
   if 39 - 39: OoO0O0 . I1ii11iIi11i - OOooOOo * Ii
   if O0oOOoii111IIiiiiI > 0 :
    if 4 - 4: OOooOOo * o0o00Oo0O - O0o0Ooo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: O0o0Ooo + OOO00O / oOo0O0Ooo . iIIIIii1 % oO0o / Ii
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 13 - 13: IiI11iII1 % I11i + OoO0O0 + IiI11iII1 + Ii - Ii1I
   else :
    pass
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
    if 11 - 11: O0o0O0O0ooO0
 i1OooO00oO00o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( i1OooO00oO00o ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( i1OooO00oO00o ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 14 - 14: Ii1I * I1ii11iIi11i + Ii % OoO0O0 - oo0OO
   if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
   if O0oOOoii111IIiiiiI > 0 :
    if 95 - 95: IiI11iII1 + iIIIIii1 * iI11I1II1I1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0Oo0O0Oo00oO
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 19 - 19: ooOoO0O00 - iI11I1II1I1I . O0o0Ooo
   else :
    pass
    if 2 - 2: o0Oo0O0Oo00oO
    if 12 - 12: Ii - iI11I1II1I1I * iIIIIii1 * O0o0O0O0ooO0
    if 19 - 19: o0o00Oo0O + oo0OO + I11i
 oO0IIi11IiiiI11i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( oO0IIi11IiiiI11i ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 68 - 68: oo0OO + O0o0Ooo * oo0OO . iIIIIii1 % o0Oo0O0Oo00oO - ii
   if 60 - 60: oO0o % Ii
   if O0oOOoii111IIiiiiI > 0 :
    if 7 - 7: iIIIIii1
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: I1ii11iIi11i + O0o0O0O0ooO0 + oOo0O0Ooo * I11i
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 33 - 33: I11i * I1ii11iIi11i
   else :
    pass
    if 88 - 88: IiI11iII1 % OoO0O0 - OOooOOo - OOooOOo . oOo0O0Ooo
    if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - IiI11iII1
 Oo0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( Oo0OOo ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 43 - 43: iIIIIii1 % o0Oo0O0Oo00oO . OoO0O0 / I1ii11iIi11i
   if 55 - 55: Ii1I % ii
   if O0oOOoii111IIiiiiI > 0 :
    if 73 - 73: ooOoO0O00 - O0o0O0O0ooO0 % oo0OO / ooOoO0O00 + IIiIiII11i + Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: oo0OO
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 26 - 26: OOO00O % ii . IiI11iII1 * OOO00O + IIiIiII11i - Ii1I
   else :
    pass
    if 20 - 20: oO0o
    if 99 - 99: I1ii11iIi11i + ii . O0o0O0O0ooO0 + o0o00Oo0O
 oo000o0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( oo000o0O ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 1 - 1: IIiIiII11i - ooOoO0O00 + oo0OO
   if 58 - 58: O0o0O0O0ooO0 - ii
   if O0oOOoii111IIiiiiI > 0 :
    if 56 - 56: O0o0O0O0ooO0 / O0o0O0O0ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: o0o00Oo0O * OOO00O % OOooOOo / o0o00Oo0O
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 85 - 85: ii + ii
   else :
    pass
    if 23 - 23: ooOoO0O00
    if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / O0o0Ooo . oO0o
 oOOo0O0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( oOOo0O0Oo ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 50 - 50: oo0OO * O0o0Ooo + OoO0O0 - I1ii11iIi11i
   if 79 - 79: oO0o / ooOoO0O00
   if O0oOOoii111IIiiiiI > 0 :
    if 30 - 30: OOooOOo - Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 94 - 94: OOooOOo % O0o0O0O0ooO0
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 39 - 39: OOooOOo + IiI11iII1 % o0o00Oo0O
   else :
    pass
    if 26 - 26: OOO00O + OOooOOo
    if 17 - 17: Ii1I - O0o0O0O0ooO0 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * OoO0O0
 iIi1i1iiIiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( iIi1i1iiIiiiI ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 79 - 79: ii * IiI11iII1 - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
   if 82 - 82: OOooOOo . o0Oo0O0Oo00oO
   if O0oOOoii111IIiiiiI > 0 :
    if 73 - 73: IiI11iII1
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: iIIIIii1
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
   else :
    pass
    if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . o0Oo0O0Oo00oO - I1ii11iIi11i . Ii
    if 47 - 47: I1ii11iIi11i % oO0o - OOO00O - I1ii11iIi11i * oo0OO
 OOOOO0oOOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( OOOOO0oOOoO ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 42 - 42: oOo0O0Ooo + Ii / oO0o
   if 64 - 64: iIIIIii1
   if O0oOOoii111IIiiiiI > 0 :
    if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: o0o00Oo0O + iIIIIii1 * IiI11iII1
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 30 - 30: OOooOOo
   else :
    pass
    if 39 - 39: Ii1I + I11i + IiI11iII1 + iIIIIii1
    if 48 - 48: IiI11iII1 / OOO00O . iI11I1II1I1I
 ooo0OOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( ooo0OOoo ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 52 - 52: oO0o
   if 49 - 49: o0Oo0O0Oo00oO . Ii1I % OOO00O . I1ii11iIi11i * OoO0O0
   if O0oOOoii111IIiiiiI > 0 :
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . OOO00O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: O0o0O0O0ooO0 + I11i . IiI11iII1 / Ii
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 7 - 7: OOooOOo / OOooOOo . IiI11iII1 * o0o00Oo0O + iIIIIii1 + oo0OO
   else :
    pass
    if 98 - 98: IIiIiII11i * iIIIIii1 - oOo0O0Ooo % I11i - O0o0O0O0ooO0 % Ii1I
    if 69 - 69: ooOoO0O00 % oO0o % IiI11iII1 / OOO00O / OOO00O
 Ii1I1i1IiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( Oo0OOo ) == True :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( Ii1I1i1IiiI ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 37 - 37: oOo0O0Ooo + ii . IiI11iII1 + oOo0O0Ooo . iIIIIii1
   if 44 - 44: OOooOOo . IiI11iII1 . ooOoO0O00 . OOooOOo * OOO00O
   if O0oOOoii111IIiiiiI > 0 :
    if 59 - 59: IIiIiII11i * ii - ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 33 - 33: o0o00Oo0O . Ii % I11i
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
      if 50 - 50: OOO00O
   else :
    pass
    if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * OoO0O0
    if 83 - 83: Ii - oOo0O0Ooo * Ii
    if 59 - 59: O0o0O0O0ooO0 - ii / OOO00O + Ii1I . I11i - O0o0O0O0ooO0
 iiI1iI1i1 = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   OOOo0O0o0oo = os . path . join ( iiI1iI1i1 , "cache.db" )
   os . unlink ( OOOo0O0o0oo )
   if 25 - 25: ii
 except :
  pass
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + o0Oo0O0Oo00oO . OoO0O0
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 58 - 58: iI11I1II1I1I + IiI11iII1 - Ii1I - ooOoO0O00 * OOooOOo
 if 4 - 4: ii
 if 7 - 7: iIIIIii1
 if 26 - 26: OoO0O0 + I1ii11iIi11i
 if 71 - 71: oOo0O0Ooo . OOO00O
 if 43 - 43: Ii1I * OoO0O0
 if 1 - 1: oO0o * OOO00O + iIIIIii1 . oo0OO / OOO00O
 if 91 - 91: o0Oo0O0Oo00oO + O0o0Ooo - I1ii11iIi11i % OOooOOo . O0o0O0O0ooO0
 if 51 - 51: OoO0O0 / O0o0Ooo
def O0OOO00O0OO0 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 iI1I11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( iI1I11 ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 92 - 92: oOo0O0Ooo / oO0o - OoO0O0 / Ii
   if 23 - 23: IIiIiII11i / Ii - oO0o * oO0o + O0o0O0O0ooO0 * IIiIiII11i
   if O0oOOoii111IIiiiiI > 0 :
    if 82 - 82: I11i + o0Oo0O0Oo00oO * oOo0O0Ooo - oo0OO
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 6 - 6: OoO0O0 / iI11I1II1I1I / OOO00O / oOo0O0Ooo - ooOoO0O00 - OoO0O0
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
     oooOOOOO = xbmcgui . Dialog ( )
     oooOOOOO . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    oooOOOOO = xbmcgui . Dialog ( )
    oooOOOOO . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 8 - 8: Ii * O0o0Ooo . OoO0O0 / OoO0O0
 if 42 - 42: ii / IiI11iII1 . I11i / o0o00Oo0O - iIIIIii1 * iIIIIii1
 if 1 - 1: o0Oo0O0Oo00oO % IiI11iII1
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % OoO0O0 . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: IiI11iII1 % OOO00O - OOO00O % oOo0O0Ooo . OoO0O0 - ii
 if 100 - 100: oOo0O0Ooo + o0Oo0O0Oo00oO + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * IiI11iII1 - o0Oo0O0Oo00oO + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
def III1IiIII1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 iI1I11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooOo , iI1 , OoOo00o0OO in os . walk ( iI1I11 ) :
   O0oOOoii111IIiiiiI = 0
   O0oOOoii111IIiiiiI += len ( OoOo00o0OO )
   if 36 - 36: oo0OO * O0o0O0O0ooO0 + iIIIIii1 * O0o0O0O0ooO0 . Ii1I - iI11I1II1I1I
   if 14 - 14: O0o0Ooo * oo0OO + Ii
   if O0oOOoii111IIiiiiI > 0 :
    if 84 - 84: O0o0O0O0ooO0 / IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( O0oOOoii111IIiiiiI ) + " files found" , "Do you want to delete them?" ) :
     if 86 - 86: oOo0O0Ooo
     for i11i1iiiII in OoOo00o0OO :
      os . unlink ( os . path . join ( ooOo , i11i1iiiII ) )
     for iI1IIIii in iI1 :
      shutil . rmtree ( os . path . join ( ooOo , iI1IIIii ) )
     oooOOOOO = xbmcgui . Dialog ( )
     oooOOOOO . ok ( o0oOoO00o , "       Deleting Packages all done" )
    else :
     pass
   else :
    oooOOOOO = xbmcgui . Dialog ( )
    oooOOOOO . ok ( o0oOoO00o , "       No Packages to DELETE" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 iiiII1i1iiii ( url )
 return
 if 97 - 97: IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
 if 8 - 8: Ii / OOO00O
 if 33 - 33: IiI11iII1 * iIIIIii1 - o0o00Oo0O + oOo0O0Ooo / iIIIIii1
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: iIIIIii1 - I11i % OoO0O0 - IIiIiII11i
 if 56 - 56: o0Oo0O0Oo00oO * Ii
 if 92 - 92: IIiIiII11i - o0o00Oo0O . IiI11iII1
 if 59 - 59: OOooOOo
def iiII1iiI ( url , name ) :
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ooo0o00O0 = os . path . join ( iI11 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 I11iIiiIIII1ii1 = os . path . join ( iI11 , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11iIiiIIII1ii1 ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Ooo0o00O0 = os . path . join ( iI11 , 'advancedsettings.xml' )
   try :
    os . remove ( Ooo0o00O0 )
    print '=== GenieTv - REMOVING    ' + str ( Ooo0o00O0 ) + '    ==='
   except :
    pass
   OOOOi11i1 = i1 . http_GET ( url ) . content
   ooOO0oO0oo00o = open ( Ooo0o00O0 , "w" )
   ooOO0oO0oo00o . write ( OOOOi11i1 )
   ooOO0oO0oo00o . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Ooo0o00O0 ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Ooo0o00O0 = os . path . join ( iI11 , 'advancedsettings.xml' )
  try :
   os . remove ( Ooo0o00O0 )
   print '=== GenieTv - REMOVING    ' + str ( Ooo0o00O0 ) + '    ==='
  except :
   pass
  OOOOi11i1 = i1 . http_GET ( url ) . content
  ooOO0oO0oo00o = open ( Ooo0o00O0 , "w" )
  ooOO0oO0oo00o . write ( OOOOi11i1 )
  ooOO0oO0oo00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ooo0o00O0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 13 - 13: OOooOOo - oO0o * ii
def iIi1i111ii1II11ii ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ooo0o00O0 = os . path . join ( iI11 , 'advancedsettings.xml' )
 try :
  ooOO0oO0oo00o = open ( Ooo0o00O0 ) . read ( )
  if 'zero' in ooOO0oO0oo00o :
   name = '0CACHE'
  elif 'tuxen' in ooOO0oO0oo00o :
   name = 'TUXENS'
  elif 'muckys' in ooOO0oO0oo00o :
   name = 'MUCKYS'
  elif 'p2p1' in ooOO0oO0oo00o :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ooOO0oO0oo00o :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ooOO0oO0oo00o :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 21 - 21: O0o0Ooo
def OOO0O ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 iI11 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Ooo0o00O0 = os . path . join ( iI11 , 'advancedsettings.xml' )
 try :
  os . remove ( Ooo0o00O0 )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Ooo0o00O0 ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 21 - 21: I1ii11iIi11i / iIIIIii1 * OOooOOo - IiI11iII1
 if 44 - 44: ii + o0Oo0O0Oo00oO
 if 84 - 84: ooOoO0O00 - IIiIiII11i . ii / OOooOOo % o0Oo0O0Oo00oO
 if 7 - 7: ooOoO0O00 / iIIIIii1 / O0o0O0O0ooO0
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: OOO00O + oo0OO - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: iIIIIii1
 if 52 - 52: o0o00Oo0O + OOO00O
 if 11 - 11: ooOoO0O00 / IiI11iII1 * Ii1I * IiI11iII1 * OOO00O - Ii
 if 96 - 96: Ii1I % Ii1I
def ii1II11IIII1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 OO0oOO0O = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for I1IIII , oo0oO0o00Oo0 , i1I1I , O0Oi11iIii11 in OO0oOO0O :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I1IIII , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i1I1I , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0Oi11iIii11 )
  inc = inc + 1
  if 93 - 93: o0Oo0O0Oo00oO * iI11I1II1I1I * I11i
  if 23 - 23: OoO0O0 . o0Oo0O0Oo00oO * ii - O0o0Ooo
  if 99 - 99: ii % ooOoO0O00 % ii . O0o0O0O0ooO0
  if 20 - 20: oO0o . oo0OO
  if 4 - 4: I1ii11iIi11i % o0Oo0O0Oo00oO % oO0o * O0o0O0O0ooO0 % ii
  if 38 - 38: ii . O0o0O0O0ooO0
  if 43 - 43: ii
  if 8 - 8: OoO0O0 + O0o0Ooo . O0o0Ooo
  if 89 - 89: Ii1I * Ii1I * OOooOOo / O0o0O0O0ooO0
def OOo0 ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Ooo0o00O0 = os . path . join ( iI11 , 'addons2.ini' )
  OOOOi11i1 = i1 . http_GET ( url ) . content
  ooOO0oO0oo00o = open ( Ooo0o00O0 , "w" )
  ooOO0oO0oo00o . write ( OOOOi11i1 )
  ooOO0oO0oo00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ooo0o00O0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 45 - 45: IiI11iII1 - o0Oo0O0Oo00oO
def o0OoO ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  iI11 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Ooo0o00O0 = os . path . join ( iI11 , 'settings.xml' )
  OOOOi11i1 = i1 . http_GET ( url ) . content
  ooOO0oO0oo00o = open ( Ooo0o00O0 , "w" )
  ooOO0oO0oo00o . write ( OOOOi11i1 )
  ooOO0oO0oo00o . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Ooo0o00O0 ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 80 - 80: o0o00Oo0O
 if 74 - 74: Ii1I * oo0OO + O0o0O0O0ooO0 % o0o00Oo0O
def Iii1IiIiIii ( ) :
 try :
  OOo0ooOOOo0O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OOo0ooOOOo0O0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ooI1 = os . path . join ( OOo0ooOOOo0O0 , "source.db" )
    os . unlink ( ooI1 )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 4 - 4: O0o0O0O0ooO0 % Ii1I
 if 9 - 9: o0o00Oo0O * o0Oo0O0Oo00oO
 if 54 - 54: O0o0Ooo % O0o0Ooo - OOO00O
 if 32 - 32: I11i % IIiIiII11i / I11i . OoO0O0 . I11i
 if 29 - 29: ii % IIiIiII11i % Ii - I1ii11iIi11i
def O0 ( url ) :
 I1IIiiIiii = urllib2 . Request ( url )
 I1IIiiIiii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O000oo0O = urllib2 . urlopen ( I1IIiiIiii )
 OOOOi11i1 = O000oo0O . read ( )
 O000oo0O . close ( )
 return OOOOi11i1
 if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
 if 35 - 35: I11i + oO0o - Ii1I
 if 24 - 24: IIiIiII11i
 if 23 - 23: I1ii11iIi11i - O0o0O0O0ooO0
 if 79 - 79: O0o0Ooo . o0o00Oo0O - ooOoO0O00
 if 42 - 42: oo0OO - Ii % oo0OO - IiI11iII1 * o0o00Oo0O / IIiIiII11i
 if 5 - 5: I1ii11iIi11i
def oOoOo0o0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; II1Iiiii = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if II1Iiiii :
  OoO00 = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; OoO00 = xbmc . translatePath ( OoO00 ) ;
  iI1I = os . path . join ( OoO00 , ".." , ".." ) ; iI1I = os . path . abspath ( iI1I ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iI1I ) ; Oo0o = False
  try :
   for ooOo , iI1 , OoOo00o0OO in os . walk ( iI1I , topdown = True ) :
    iI1 [ : ] = [ iI1IIIii for iI1IIIii in iI1 if iI1IIIii not in iiIIIII1i1iI ]
    for IiiiiI1i1Iii in OoOo00o0OO :
     try : os . remove ( os . path . join ( ooOo , IiiiiI1i1Iii ) )
     except :
      if IiiiiI1i1Iii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0o = True
      plugintools . log ( "Error removing " + ooOo + " " + IiiiiI1i1Iii )
    for IiiiiI1i1Iii in iI1 :
     try : os . rmdir ( os . path . join ( ooOo , IiiiiI1i1Iii ) )
     except :
      if IiiiiI1i1Iii not in [ "Database" , "userdata" ] : Oo0o = True
      plugintools . log ( "Error removing " + ooOo + " " + IiiiiI1i1Iii )
   if not Oo0o : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 O00ooOo ( )
 if 88 - 88: OOO00O / I1ii11iIi11i + o0Oo0O0Oo00oO % Ii * oO0o
 if 23 - 23: OoO0O0 + OOO00O / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: O0o0O0O0ooO0 - I11i
def OOOOo0o0O0 ( ) :
 I1I1i1 = [ ]
 Ii1Ii = sys . argv [ 2 ]
 if len ( Ii1Ii ) >= 2 :
  iII = sys . argv [ 2 ]
  OOoOOooO = iII . replace ( '?' , '' )
  if ( iII [ len ( iII ) - 1 ] == '/' ) :
   iII = iII [ 0 : len ( iII ) - 2 ]
  i1111II1iIII = OOoOOooO . split ( '&' )
  I1I1i1 = { }
  for i11oooOo in range ( len ( i1111II1iIII ) ) :
   I1ii11ii1iiI = { }
   I1ii11ii1iiI = i1111II1iIII [ i11oooOo ] . split ( '=' )
   if ( len ( I1ii11ii1iiI ) ) == 2 :
    I1I1i1 [ I1ii11ii1iiI [ 0 ] ] = I1ii11ii1iiI [ 1 ]
    if 93 - 93: OOooOOo + O0o0Ooo
 return I1I1i1
 if 27 - 27: iI11I1II1I1I * O0o0Ooo
iiI1iiiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
oO00OoOO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOoOO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOo00OOoOOO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i11I1II = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1iII11I1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OoOo00OoOO00 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i1i1ii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IiI1I1II = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
IIiiIiIIiI1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Iii1I1I1iiI1i = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
o00O000oooOo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
O0oooOO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OO00OO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Oo0Ii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiiiiiiI111i = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0OoO000O = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i1Ii = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I111i1I1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
o00O0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ii1iii11i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OOO00oo0ooO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiI1i11i1iI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
ii11iiIi = base64 . decodestring ( 'Q1VOVA==' )
def iiIiII1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIii1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiI1II1II111 = [ ]
  if showcontext == 'fav' :
   iiI1II1II111 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in iiiiiIIii :
   iiI1II1II111 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIIii1 . addContextMenuItems ( iiI1II1II111 )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = True )
 return OOoooooooO
 if 40 - 40: iIIIIii1 . ii . oOo0O0Ooo + o0o00Oo0O % ooOoO0O00 / iIIIIii1
def o0O0OOO0Ooo ( name , url , mode , iconimage , fanart , description ) :
 oOo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOoooooooO = True
 iIIii1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIii1 . setProperty ( "Fanart_Image" , fanart )
 OOoooooooO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOo00o , listitem = iIIii1 , isFolder = False )
 return OOoooooooO
 if 36 - 36: ii - OOooOOo - oO0o * IiI11iII1 - oo0OO
 if 99 - 99: OOO00O / oOo0O0Ooo . o0Oo0O0Oo00oO - o0Oo0O0Oo00oO * oOo0O0Ooo
iII = OOOOo0o0O0 ( )
O0o = None
IiiiiI1i1Iii = None
i11Ii1iIiII = None
oo0O0o00o0O = None
I11i1II = None
OOOOO0O00 = None
I1IIiIIiiI1i = None
if 83 - 83: Ii1I * IIiIiII11i . IiI11iII1 - O0o0Ooo
if 46 - 46: oO0o % Ii1I
try :
 I1IIiIIiiI1i = int ( iII [ "fav_mode" ] )
except :
 pass
 if 58 - 58: oo0OO + iIIIIii1 % O0o0O0O0ooO0 - o0Oo0O0Oo00oO - OoO0O0 % o0Oo0O0Oo00oO
try :
 O0o = urllib . unquote_plus ( iII [ "url" ] )
except :
 pass
try :
 IiiiiI1i1Iii = urllib . unquote_plus ( iII [ "name" ] )
except :
 pass
try :
 oo0O0o00o0O = urllib . unquote_plus ( iII [ "iconimage" ] )
except :
 pass
try :
 i11Ii1iIiII = int ( iII [ "mode" ] )
except :
 pass
try :
 I11i1II = urllib . unquote_plus ( iII [ "fanart" ] )
except :
 pass
try :
 OOOOO0O00 = urllib . unquote_plus ( iII [ "description" ] )
except :
 pass
 if 86 - 86: I11i
 if 15 - 15: oo0OO - iI11I1II1I1I - IIiIiII11i - iIIIIii1 % Ii1I
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( i11Ii1iIiII )
print "URL: " + str ( O0o )
print "Name: " + str ( IiiiiI1i1Iii )
print "IconImage: " + str ( oo0O0o00o0O )
if 80 - 80: iIIIIii1 * O0o0O0O0ooO0 . ooOoO0O00 % o0Oo0O0Oo00oO % Ii1I + OOO00O
if 6 - 6: Ii1I . oo0OO . oO0o + iIIIIii1
def i1Iii1i1I ( content , viewType ) :
 if 65 - 65: Ii1I / OOO00O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 23 - 23: OoO0O0 / OoO0O0 * I11i * OoO0O0
if oo0O0o00o0O == None : oo0O0o00o0O = ii11iIi1I
if I11i1II == None : I11i1II = i1iIIi1
if i11Ii1iIiII == None :
 iiIiI ( )
 if 57 - 57: O0o0O0O0ooO0
elif i11Ii1iIiII == 1 :
 oO0 ( O0o )
 if 29 - 29: oOo0O0Ooo
elif i11Ii1iIiII == 44 :
 iiIii1IIi ( O0o )
 if 41 - 41: IiI11iII1 * oO0o - O0o0O0O0ooO0 . o0Oo0O0Oo00oO
elif i11Ii1iIiII == 2 :
 Ii1II ( )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - oo0OO + IiI11iII1
elif i11Ii1iIiII == 3 :
 iIi1i ( )
 if 22 - 22: o0o00Oo0O % iIIIIii1 % O0o0O0O0ooO0 % oOo0O0Ooo
elif i11Ii1iIiII == 21 :
 iI1Ii11111iIi ( )
 if 34 - 34: O0o0O0O0ooO0 . I1ii11iIi11i % Ii1I . O0o0O0O0ooO0 % iIIIIii1 / iIIIIii1
elif i11Ii1iIiII == 4 :
 O0ooO00oO ( )
 if 84 - 84: o0Oo0O0Oo00oO
elif i11Ii1iIiII == 5 :
 O0O0ooOOO ( O0o )
 if 1 - 1: oo0OO - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
elif i11Ii1iIiII == 6 :
 O0OOO00O0OO0 ( O0o )
 if 9 - 9: O0o0O0O0ooO0 - O0o0O0O0ooO0
elif i11Ii1iIiII == 7 :
 iiII1iiI ( O0o , IiiiiI1i1Iii )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + oo0OO
elif i11Ii1iIiII == 8 :
 iIi1i111ii1II11ii ( O0o , IiiiiI1i1Iii )
 if 20 - 20: oO0o + O0o0Ooo . IIiIiII11i / Ii
elif i11Ii1iIiII == 9 :
 FIXREPOSADDONS ( O0o )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
elif i11Ii1iIiII == 10 :
 iiIiI1i1 ( )
 if 41 - 41: Ii1I % Ii1I + iIIIIii1 . O0o0O0O0ooO0 % IiI11iII1 * OOO00O
elif i11Ii1iIiII == 11 :
 OOO0O ( O0o )
 if 57 - 57: o0Oo0O0Oo00oO . IiI11iII1 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
elif i11Ii1iIiII == 12 :
 ii1II11IIII1 ( )
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
elif i11Ii1iIiII == 13 :
 iI1ii1 ( )
 if 93 - 93: OOO00O / OoO0O0 * o0o00Oo0O
elif i11Ii1iIiII == 14 :
 iiiII1i1iiii ( O0o )
 if 17 - 17: oO0o / OOO00O % oOo0O0Ooo
elif i11Ii1iIiII == 15 :
 iI1I1iIi11 ( )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif i11Ii1iIiII == 16 :
 OOo0 ( O0o , IiiiiI1i1Iii )
 if 60 - 60: Ii1I / iIIIIii1 . Ii / oO0o % IIiIiII11i
elif i11Ii1iIiII == 17 :
 o0OoO ( O0o , IiiiiI1i1Iii )
 if 6 - 6: O0o0O0O0ooO0 % I11i + IiI11iII1
elif i11Ii1iIiII == 18 :
 Iii1IiIiIii ( )
 if 91 - 91: I11i + o0o00Oo0O * oo0OO * iIIIIii1 * Ii1I
elif i11Ii1iIiII == 19 :
 I1iii ( O0o )
 if 83 - 83: ii
elif i11Ii1iIiII == 40 :
 Ii1 ( IiiiiI1i1Iii , O0o , OOOOO0O00 )
 if 52 - 52: I11i / OOooOOo % oo0OO % oO0o / iIIIIii1 % I11i
elif i11Ii1iIiII == 42 :
 O0O00O000OOO ( IiiiiI1i1Iii , O0o , OOOOO0O00 )
 if 88 - 88: OoO0O0 / Ii / o0Oo0O0Oo00oO / Ii * Ii1I % O0o0Ooo
elif i11Ii1iIiII == 43 :
 OoOooOo0O ( O0o )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * o0Oo0O0Oo00oO + iI11I1II1I1I
elif i11Ii1iIiII == 20 :
 Ii1iI11iI1 ( O0o )
 if 80 - 80: I11i . O0o0O0O0ooO0 . ii
elif i11Ii1iIiII == 22 :
 IiiiII ( O0o )
 if 63 - 63: OOO00O . OoO0O0
elif i11Ii1iIiII == 23 :
 ii111Ii1i ( O0o )
 if 66 - 66: oOo0O0Ooo
elif i11Ii1iIiII == 24 :
 ii1IO0OOoooO ( O0o )
 if 99 - 99: oO0o % o0o00Oo0O . IiI11iII1 - Ii1I . I1ii11iIi11i / OOooOOo
elif i11Ii1iIiII == 25 :
 oo0O0000oo0o0 ( O0o )
 if 60 - 60: Ii1I
elif i11Ii1iIiII == 26 :
 OO0iii111 ( O0o )
 if 78 - 78: oo0OO + IIiIiII11i
elif i11Ii1iIiII == 27 :
 o0oo ( O0o )
 if 55 - 55: ii
elif i11Ii1iIiII == 28 :
 Ii11I1 ( O0o )
 if 90 - 90: oOo0O0Ooo
elif i11Ii1iIiII == 29 :
 I1ii11IiI1I ( O0o )
 if 4 - 4: OoO0O0 % OOO00O - OoO0O0 - I11i
elif i11Ii1iIiII == 30 :
 II1Ii1iI1i1 ( O0o )
 if 30 - 30: iIIIIii1
elif i11Ii1iIiII == 31 :
 iio0Oo ( O0o )
 if 34 - 34: oo0OO - IIiIiII11i - I11i + O0o0O0O0ooO0 + IiI11iII1
elif i11Ii1iIiII == 32 :
 I11I ( )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif i11Ii1iIiII == 33 :
 ii11II1i ( )
 if 20 - 20: Ii - IIiIiII11i - OOO00O % oo0OO . OOO00O
elif i11Ii1iIiII == 35 :
 i1o0oooO ( O0o )
 if 50 - 50: iI11I1II1I1I + IiI11iII1 - O0o0Ooo - ii
elif i11Ii1iIiII == 34 :
 iIIiiiiI ( O0o )
 if 84 - 84: OOooOOo - O0o0Ooo
elif i11Ii1iIiII == 36 :
 IIiI11i1111Ii ( O0o )
 if 80 - 80: Ii % OoO0O0 - I1ii11iIi11i % OoO0O0
elif i11Ii1iIiII == 37 :
 O00o00O ( O0o )
 if 89 - 89: o0Oo0O0Oo00oO * O0o0Ooo + OOooOOo / Ii
elif i11Ii1iIiII == 38 :
 II11iIiiI1111 ( O0o )
 if 68 - 68: ii * O0o0Ooo
elif i11Ii1iIiII == 41 :
 oOoOo0o0 ( iII )
 if 86 - 86: I11i / OOooOOo
elif i11Ii1iIiII == 39 :
 OoO00OO0 ( O0o )
 if 40 - 40: O0o0O0O0ooO0
elif i11Ii1iIiII == 45 :
 TEXTS ( )
 if 62 - 62: OOO00O / OoO0O0
elif i11Ii1iIiII == 46 :
 o0oOo0OoO ( )
 if 74 - 74: O0o0O0O0ooO0 % IiI11iII1 / IiI11iII1 - iI11I1II1I1I - IIiIiII11i + OoO0O0
elif i11Ii1iIiII == 47 :
 GEVID ( )
 if 92 - 92: O0o0Ooo % IiI11iII1
elif i11Ii1iIiII == 48 :
 IiiIi ( IiiiiI1i1Iii , O0o , OOOOO0O00 )
 if 18 - 18: OOO00O + IiI11iII1 / OoO0O0 / oo0OO + iI11I1II1I1I % iIIIIii1
elif i11Ii1iIiII == 49 :
 O0oii111 ( )
 if 94 - 94: O0o0Ooo
elif i11Ii1iIiII == 222 :
 OoOOoooOO0O ( O0o )
 if 37 - 37: oo0OO
elif i11Ii1iIiII == 333 :
 O0O00oOo0o000 ( O0o )
 if 52 - 52: Ii1I * oOo0O0Ooo . OoO0O0 + ooOoO0O00 % oo0OO / iI11I1II1I1I
 if 68 - 68: IiI11iII1 - OOooOOo . Ii + I11i
elif i11Ii1iIiII == 1020 :
 IIi1I1 ( )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif i11Ii1iIiII == 1021 :
 ANIMEEP ( )
 if 33 - 33: O0o0Ooo . I1ii11iIi11i
elif i11Ii1iIiII == 1022 :
 ANIMEPLAY ( O0o )
 if 89 - 89: O0o0O0O0ooO0 + ooOoO0O00 - iIIIIii1 + OOO00O . IIiIiII11i
elif i11Ii1iIiII == 1001 :
 Oo0O0o00o00 ( )
 if 85 - 85: iI11I1II1I1I - o0Oo0O0Oo00oO * I1ii11iIi11i . oo0OO + IiI11iII1
elif i11Ii1iIiII == 1005 :
 oOO0O0O ( )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif i11Ii1iIiII == 1007 :
 Oo0o0oOo0oO ( O0o )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . O0o0O0O0ooO0 / O0o0O0O0ooO0
elif i11Ii1iIiII == 1010 :
 IiIii1i11i1 ( O0o )
 if 43 - 43: oOo0O0Ooo
elif i11Ii1iIiII == 1011 :
 O0OoO00OoOO ( O0o )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif i11Ii1iIiII == 1012 :
 O0ooO ( O0o )
 if 34 - 34: I11i % Ii1I + o0Oo0O0Oo00oO * O0o0Ooo / oo0OO
elif i11Ii1iIiII == 1030 :
 OOoOo0ooOoo ( )
 if 18 - 18: OOO00O
elif i11Ii1iIiII == 1031 :
 oO0OO00 ( O0o , oo0O0o00o0O )
 if 92 - 92: oO0o % iI11I1II1I1I / iIIIIii1 * O0o0O0O0ooO0 . ooOoO0O00 + oo0OO
elif i11Ii1iIiII == 1032 :
 iiIi ( O0o )
 if 24 - 24: iIIIIii1 . O0o0O0O0ooO0 * iIIIIii1 % Ii . Ii + ooOoO0O00
elif i11Ii1iIiII == 1006 :
 Parse . ParseURL ( O0o )
 if 64 - 64: iI11I1II1I1I / iIIIIii1 / I1ii11iIi11i - Ii1I
elif i11Ii1iIiII == 2030 :
 Parse . addonParseURL ( O0o )
 if 100 - 100: iIIIIii1 + ooOoO0O00 * oO0o
elif i11Ii1iIiII == 2031 :
 Parse . apkParseURL ( O0o )
 if 64 - 64: oo0OO * Ii . I1ii11iIi11i
elif i11Ii1iIiII == 1002 :
 o0oO00oooo ( O0o )
 if 52 - 52: I1ii11iIi11i / OOO00O / O0o0O0O0ooO0 - I11i / O0o0O0O0ooO0
elif i11Ii1iIiII == 1003 :
 ooo0Oo00O ( O0o , oo0O0o00o0O )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif i11Ii1iIiII == 1004 :
 I1iII1 ( O0o )
 if 85 - 85: oOo0O0Ooo
elif i11Ii1iIiII == 1008 :
 iI1iii1iIiiI ( )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif i11Ii1iIiII == 1009 :
 oOOo0oO ( O0o )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif i11Ii1iIiII == 2001 :
 iii1i ( )
 if 46 - 46: OOooOOo * O0o0Ooo / oo0OO + I1ii11iIi11i + iIIIIii1
elif i11Ii1iIiII == 2002 :
 I1III1I11I1 ( O0o )
 if 95 - 95: I11i - o0Oo0O0Oo00oO
elif i11Ii1iIiII == 1013 :
 OoOO0OOoo ( )
elif i11Ii1iIiII == 10111113 :
 IIIi11IiIiii ( O0o )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif i11Ii1iIiII == 1014 :
 ii1IIiI1iI1i ( )
 if 19 - 19: OOooOOo . OoO0O0 . ii
elif i11Ii1iIiII == 1015 :
 IIiII11 ( O0o )
 if 79 - 79: OoO0O0 * OOO00O * oOo0O0Ooo * Ii1I / Ii1I
elif i11Ii1iIiII == 1016 :
 iiI1ii1Iii11I ( O0o , oo0O0o00o0O , IiiiiI1i1Iii )
 if 62 - 62: OOO00O * o0Oo0O0Oo00oO % Ii1I - ooOoO0O00 - Ii1I
elif i11Ii1iIiII == 1017 :
 OoO ( )
 if 24 - 24: OoO0O0
elif i11Ii1iIiII == 1023 :
 Ooo0oo ( )
 if 71 - 71: iIIIIii1 - ooOoO0O00
elif i11Ii1iIiII == 1024 :
 i1IIiI1iII ( O0o )
 if 56 - 56: OOooOOo + oo0OO
elif i11Ii1iIiII == 1025 :
 ii11ii11II ( O0o )
 if 74 - 74: O0o0O0O0ooO0 / IiI11iII1 / IIiIiII11i - O0o0O0O0ooO0 / oo0OO % O0o0Ooo
elif i11Ii1iIiII == 4001 :
 O000OOOOOo ( )
 if 19 - 19: iIIIIii1 % ii + ii
elif i11Ii1iIiII == 4002 :
 oo000o ( )
 if 7 - 7: ooOoO0O00
elif i11Ii1iIiII == 4003 :
 oOo0oO ( )
 if 91 - 91: OOooOOo - OOooOOo . iIIIIii1
elif i11Ii1iIiII == 4004 :
 OOo0oO00ooO00 ( )
 if 33 - 33: IiI11iII1 - iI11I1II1I1I / o0Oo0O0Oo00oO % o0o00Oo0O
elif i11Ii1iIiII == 4005 :
 I11iI ( )
 if 80 - 80: iIIIIii1 % ii - iIIIIii1
elif i11Ii1iIiII == 4006 :
 iI ( )
 if 27 - 27: IiI11iII1 - I11i * Ii1I - oOo0O0Ooo
elif i11Ii1iIiII == 4007 :
 OO0ooOOO0OOO ( )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - O0o0O0O0ooO0 . o0Oo0O0Oo00oO
elif i11Ii1iIiII == 4008 :
 oO00oooOOoOo0 ( )
 if 100 - 100: IIiIiII11i / IiI11iII1 / O0o0O0O0ooO0 - Ii1I * iI11I1II1I1I
elif i11Ii1iIiII == 4009 : oOO0O00oO0Ooo ( )
elif i11Ii1iIiII == 4010 : I111i1II ( )
elif i11Ii1iIiII == 3000 :
 I11iIi1i1I1i1 ( )
 if 7 - 7: ooOoO0O00 . iIIIIii1 % Ii * Ii1I . O0o0Ooo % Ii1I
elif i11Ii1iIiII == 3001 :
 OooO0O ( )
 if 35 - 35: oOo0O0Ooo
elif i11Ii1iIiII == 3002 :
 I111 ( O0o )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif i11Ii1iIiII == 3003 :
 iiiIii ( O0o )
 if 22 - 22: OOO00O . Ii . ii . ooOoO0O00
elif i11Ii1iIiII == 3004 :
 ooIiI11i1I11111 ( O0o )
 if 12 - 12: OOooOOo % OoO0O0 + oo0OO . o0o00Oo0O % iI11I1II1I1I
elif i11Ii1iIiII == 404 :
 i1I1iI1 ( IiiiiI1i1Iii , O0o , oo0O0o00o0O )
 if 41 - 41: ii
elif i11Ii1iIiII == 405 :
 IiII111I ( O0o )
 if 13 - 13: O0o0Ooo + IiI11iII1 - IiI11iII1 % oo0OO / O0o0Ooo
elif i11Ii1iIiII == 7030 :
 OO000OOOo0Oo ( )
 if 4 - 4: oOo0O0Ooo + OoO0O0 - iIIIIii1 + O0o0O0O0ooO0
elif i11Ii1iIiII == 7021 :
 oO0Oo ( IiiiiI1i1Iii )
 if 78 - 78: o0Oo0O0Oo00oO
elif i11Ii1iIiII == 7022 :
 I1i ( IiiiiI1i1Iii )
 if 29 - 29: IIiIiII11i
elif i11Ii1iIiII == 7000 :
 i1IIIII1 ( IiiiiI1i1Iii , O0o , img )
 if 79 - 79: iI11I1II1I1I - Ii + OOO00O - IIiIiII11i . iI11I1II1I1I
elif i11Ii1iIiII == 7050 :
 IiiIiiIIII ( O0o )
 if 84 - 84: I1ii11iIi11i % O0o0Ooo * o0o00Oo0O * O0o0Ooo
elif i11Ii1iIiII == 7051 :
 iIiI1I1 ( O0o )
 if 66 - 66: OoO0O0 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . OOO00O
elif i11Ii1iIiII == 7052 :
 OO0iiiii1iiIIii ( O0o )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif i11Ii1iIiII == 7053 :
 II1IIii1I11I ( O0o )
 if 37 - 37: ooOoO0O00 * Ii
elif i11Ii1iIiII == 7054 :
 CoolPlay ( O0o )
 if 95 - 95: Ii % IiI11iII1 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif i11Ii1iIiII == 7060 :
 I11i1I11iIii ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / OoO0O0 / IiI11iII1
elif i11Ii1iIiII == 7061 :
 iI1111i1i1ii ( O0o )
 if 35 - 35: O0o0O0O0ooO0 * OoO0O0
elif i11Ii1iIiII == 7063 :
 O0OOo ( O0o )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif i11Ii1iIiII == 7062 :
 i1I1iiii1Ii11 ( O0o )
 if 13 - 13: oO0o * IiI11iII1 + I1ii11iIi11i - iIIIIii1
elif i11Ii1iIiII == 7064 :
 NATatozcat ( )
 if 31 - 31: oO0o
elif i11Ii1iIiII == 7067 :
 IiIIIIi ( O0o )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif i11Ii1iIiII == 7066 :
 NATatozA ( O0o )
 if 77 - 77: Ii - IiI11iII1 . Ii1I % I1ii11iIi11i . o0Oo0O0Oo00oO
elif i11Ii1iIiII == 7065 :
 Oo ( O0o )
 if 9 - 9: I11i
elif i11Ii1iIiII == 7070 :
 Iii1I ( )
 if 55 - 55: OoO0O0 % iI11I1II1I1I + O0o0Ooo . OOO00O
elif i11Ii1iIiII == 7071 :
 DIZIlist ( O0o )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif i11Ii1iIiII == 7072 :
 DIZIpull ( O0o )
 if 23 - 23: Ii
elif i11Ii1iIiII == 7073 :
 WATCHDIZI ( O0o )
 if 88 - 88: IIiIiII11i - O0o0O0O0ooO0 / ii
elif i11Ii1iIiII == 7002 :
 iiii1Ii1iii ( )
 if 71 - 71: Ii1I
elif i11Ii1iIiII == 7003 :
 O0Oo0 ( O0o )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif i11Ii1iIiII == 7004 :
 iII11 ( O0o )
 if 1 - 1: iIIIIii1 % ooOoO0O00
elif i11Ii1iIiII == 7020 :
 Iii1Iii ( O0o )
 if 41 - 41: oO0o * oO0o / O0o0O0O0ooO0 + Ii1I . I11i
elif i11Ii1iIiII == 7001 :
 iI1ii1iIiii1i ( )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / o0Oo0O0Oo00oO
elif i11Ii1iIiII == 7010 :
 ooo00O0OOo ( O0o )
 if 80 - 80: Ii1I
elif i11Ii1iIiII == 7011 :
 oOoo00oO0O0OO ( O0o )
 if 67 - 67: IIiIiII11i
elif i11Ii1iIiII == 7012 :
 iIi1iii1 ( O0o )
 if 2 - 2: I11i - o0o00Oo0O * o0Oo0O0Oo00oO % iIIIIii1
elif i11Ii1iIiII == 7013 :
 cnfTVPlay2 ( O0o )
elif i11Ii1iIiII == 7014 :
 CNF_Studio_Indexer . MV_Movies ( O0o )
elif i11Ii1iIiII == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( O0o )
elif i11Ii1iIiII == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( IiiiiI1i1Iii , O0o , oo0O0o00o0O )
elif i11Ii1iIiII == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i11Ii1iIiII == 7018 :
 iiI1oooOOO0o0O0 ( )
elif i11Ii1iIiII == 7019 :
 CNF_Studio_Indexer . List_Movies ( O0o )
elif i11Ii1iIiII == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( O0o )
elif i11Ii1iIiII == 7024 :
 CNF_Studio_Indexer . Box_Office ( O0o )
 if 64 - 64: ooOoO0O00 . OOO00O
elif i11Ii1iIiII == 8000 :
 I11IIIII ( )
elif i11Ii1iIiII == 8001 :
 oO0OOoo ( )
elif i11Ii1iIiII == 8002 :
 OoO0o0OO ( )
elif i11Ii1iIiII == 8003 :
 iiIIIi1iIi ( )
elif i11Ii1iIiII == 8004 :
 i1I111iIii1i1 ( )
elif i11Ii1iIiII == 8005 :
 iIi11III ( )
elif i11Ii1iIiII == 8006 :
 i1iI1IIi1I ( IiiiiI1i1Iii , O0o )
elif i11Ii1iIiII == 8030 :
 ooo ( O0o )
elif i11Ii1iIiII == 8045 :
 Iii11111iiI ( O0o )
elif i11Ii1iIiII == 8046 :
 o0OOOOoO ( O0o )
elif i11Ii1iIiII == 8047 :
 iI1IIiiIIIII ( O0o )
elif i11Ii1iIiII == 8048 :
 IiI ( O0o )
elif i11Ii1iIiII == 8049 :
 Iii1iiI ( O0o )
elif i11Ii1iIiII == 8020 :
 iI1i1Iiii ( )
elif i11Ii1iIiII == 8021 :
 iiiIIII1IIi ( O0o )
elif i11Ii1iIiII == 8022 :
 Oo0oo0OOO0OOoOO ( O0o )
elif i11Ii1iIiII == 8023 :
 oOoOII1i1 ( O0o )
elif i11Ii1iIiII == 8040 :
 Ii1II1 ( )
elif i11Ii1iIiII == 8041 :
 OOo ( O0o )
elif i11Ii1iIiII == 8042 :
 iIIi1i11 ( O0o )
elif i11Ii1iIiII == 8043 :
 yt . PlayVideo ( O0o )
elif i11Ii1iIiII == 8044 :
 iI1Iii11i1 ( O0o )
elif i11Ii1iIiII == 8060 :
 ii1IOoO0O ( )
elif i11Ii1iIiII == 8061 :
 Oo0oo ( O0o )
elif i11Ii1iIiII == 8064 :
 IiiOoo0o0ooooOOo ( )
elif i11Ii1iIiII == 8065 :
 oOoOO0000oO00 ( O0o )
elif i11Ii1iIiII == 8070 :
 iiiiI1I ( )
elif i11Ii1iIiII == 8071 :
 OOOOOOo0OOoOo ( O0o )
elif i11Ii1iIiII == 7080 :
 OO00O00o ( O0o )
elif i11Ii1iIiII == 8090 :
 oOo0O000Ooo0 ( )
elif i11Ii1iIiII == 8091 :
 i11i ( O0o )
elif i11Ii1iIiII == 8092 :
 O0o0O00o0o ( O0o )
elif i11Ii1iIiII == 8081 :
 III ( )
elif i11Ii1iIiII == 8062 :
 IiiIi1I11 ( O0o )
elif i11Ii1iIiII == 8063 :
 Oooo0O0Oooo ( O0o )
elif i11Ii1iIiII == 8050 :
 IiIiiiIii ( )
elif i11Ii1iIiII == 8051 :
 IiiIIi11I1 ( O0o )
elif i11Ii1iIiII == 8052 :
 Ii1iIi111i1i1 ( O0o )
elif i11Ii1iIiII == 8085 :
 O0O00 ( )
elif i11Ii1iIiII == 8086 :
 iiIiIIi11I1 ( O0o )
elif i11Ii1iIiII == 8087 :
 ii1i11ii ( O0o )
elif i11Ii1iIiII == 8088 :
 iIi11iIi ( O0o , IiiiiI1i1Iii )
elif i11Ii1iIiII == 9000 :
 II1IiiIii ( )
elif i11Ii1iIiII == 1111 :
 Ii1iII1ii1 ( )
elif i11Ii1iIiII == 9001 :
 OOoOi1IiiI ( )
elif i11Ii1iIiII == 9002 :
 o00OOo00 ( )
elif i11Ii1iIiII == 9003 :
 Ii1IiiiI1ii ( )
elif i11Ii1iIiII == 50 :
 ii1I11iIiIII1 ( O0o )
elif i11Ii1iIiII == 9020 :
 champlist ( )
elif i11Ii1iIiII == 9021 :
 iiii11i ( )
elif i11Ii1iIiII == 9022 :
 Oo00OOOoo0 ( )
elif i11Ii1iIiII == 9023 :
 O0OOOOO ( )
elif i11Ii1iIiII == 9024 :
 i1iIii ( O0o )
elif i11Ii1iIiII == 9030 :
 IiIIiiiIi ( O0o )
elif i11Ii1iIiII == 9031 :
 IiI111 ( O0o )
elif i11Ii1iIiII == 9032 :
 OO0OO00ooO0 ( O0o )
elif i11Ii1iIiII == 9033 :
 OOOOOoO00oo00 ( O0o )
elif i11Ii1iIiII == 7085 :
 IiiiIIIi11ii1 ( O0o )
elif i11Ii1iIiII == 7086 :
 iI1oOoo ( O0o )
elif i11Ii1iIiII == 7087 :
 oO0o000oOO ( OOOOO0O00 )
elif i11Ii1iIiII == 9666 :
 III1IiIII1 ( O0o )
elif i11Ii1iIiII == 10100 : O0OO0OoO ( )
elif i11Ii1iIiII == 10105 : O0OOoOooO00 ( O0o )
elif i11Ii1iIiII == 10106 : oo0O0oOoOoo ( O0o )
elif i11Ii1iIiII == 10104 : ii1III1iiIi ( O0o )
elif i11Ii1iIiII == 10107 : Ii1111III1 ( )
elif i11Ii1iIiII == 10103 : i11iI1 ( O0o )
elif i11Ii1iIiII == 10108 : OOoOOOo0 ( O0o )
elif i11Ii1iIiII == 10107 : Ii1111III1 ( )
elif i11Ii1iIiII == 10000 : Origin_Menu ( )
elif i11Ii1iIiII == 10001 : i1iii11 ( )
elif i11Ii1iIiII == 10002 : oOOOOO0Ooooo ( )
elif i11Ii1iIiII == 10003 : o0o0O0Oo ( )
elif i11Ii1iIiII == 10004 : iiIii ( O0o )
elif i11Ii1iIiII == 10005 : oOo00OoOoO ( )
elif i11Ii1iIiII == 10006 : ooo0oo ( O0o )
elif i11Ii1iIiII == 10007 : I1I1I11Ii ( O0o , oo0O0o00o0O )
elif i11Ii1iIiII == 10008 : IiiIIiI1iI1 ( )
elif i11Ii1iIiII == 10009 : OOoOO0O0o0 ( )
elif i11Ii1iIiII == 10010 : ii11Iiii ( O0o )
elif i11Ii1iIiII == 10011 : OOoO0OOoO0ooo ( O0o )
elif i11Ii1iIiII == 10012 : OOOO0o0 ( O0o )
elif i11Ii1iIiII == 10013 : iI1ii11I ( O0o )
elif i11Ii1iIiII == 10014 : OooO0ooo0 ( )
elif i11Ii1iIiII == 10015 : OoOOOOo ( )
elif i11Ii1iIiII == 10016 : oo0i1iIIi1II1iiI ( O0o )
elif i11Ii1iIiII == 10017 : O00i1 ( )
elif i11Ii1iIiII == 10018 : IIi1i ( )
elif i11Ii1iIiII == 10019 : ooooo0Oo0 ( )
elif i11Ii1iIiII == 10020 : oO0oOoo0O ( )
elif i11Ii1iIiII == 10021 : O0000oO0o00 ( )
elif i11Ii1iIiII == 10022 : i1I ( O0o )
elif i11Ii1iIiII == 10023 : I1ii1i11i ( IiiiiI1i1Iii , O0o )
elif i11Ii1iIiII == 10024 : I1I1i ( O0o )
elif i11Ii1iIiII == 10025 : OoO0O0oO00 ( )
elif i11Ii1iIiII == 10026 : Oo00OO0OO ( )
elif i11Ii1iIiII == 10027 : o0oO0oO0O ( )
elif i11Ii1iIiII == 10028 : OOiI1 ( )
elif i11Ii1iIiII == 10029 : iI1i1II ( )
elif i11Ii1iIiII == 423 : i1iiI ( O0o )
elif i11Ii1iIiII == 426 : iI1IIi11i1I1 ( O0o )
elif i11Ii1iIiII == 10030 : Izle_Films ( )
elif i11Ii1iIiII == 10031 : Latest_Izle_Movies ( )
elif i11Ii1iIiII == 10032 : Izle_Genres ( )
elif i11Ii1iIiII == 10033 : Izle_Pop_Movies ( )
elif i11Ii1iIiII == 10034 : Izle_Boxsets ( )
elif i11Ii1iIiII == 10035 : Izle_Search ( )
elif i11Ii1iIiII == 10036 : Izle_Genres_Movie ( O0o )
elif i11Ii1iIiII == 10037 : Izle_Boxset_single ( O0o )
elif i11Ii1iIiII == 10038 : Izle_IFRAME ( )
elif i11Ii1iIiII == 10039 : Izle_Boxsets_Next ( O0o )
elif i11Ii1iIiII == 10040 : III1III11II ( )
elif i11Ii1iIiII == 10041 : i111IiiI1Ii ( O0o )
elif i11Ii1iIiII == 10042 : O00OoooO00 ( O0o )
elif i11Ii1iIiII == 10043 : oOo0OOO00Oo ( )
elif i11Ii1iIiII == 10044 : iII1I11 ( O0o )
elif i11Ii1iIiII == 10045 : iiiI1iI1 ( IiiiiI1i1Iii )
elif i11Ii1iIiII == 10046 : o00ooOOOoOo ( O0o )
elif i11Ii1iIiII == 10047 : Oo0O0000Oo00o ( O0o )
elif i11Ii1iIiII == 10048 : o00iIiiiII ( O0o )
elif i11Ii1iIiII == 10049 : I11iiI11iiI ( O0o )
elif i11Ii1iIiII == 10050 : ii1111IIiI1 ( )
elif i11Ii1iIiII == 10051 : OoooOO0 ( )
elif i11Ii1iIiII == 10052 : o0IiiIIII1I1i ( )
elif i11Ii1iIiII == 10053 : Addon ( O0o )
elif i11Ii1iIiII == 10054 : I1o0 ( O0o , IiiiiI1i1Iii )
elif i11Ii1iIiII == 10055 :
 o0oOOOO0 ( "addFavorite" )
 try :
  IiiiiI1i1Iii = IiiiiI1i1Iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiiiiI1i1Iii = IiiiiI1i1Iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1III1iIi ( IiiiiI1i1Iii , O0o , oo0O0o00o0O , I11i1II , I1IIiIIiiI1i )
elif i11Ii1iIiII == 10056 :
 o0oOOOO0 ( "rmFavorite" )
 try :
  IiiiiI1i1Iii = IiiiiI1i1Iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IiiiiI1i1Iii = IiiiiI1i1Iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0oOoo ( IiiiiI1i1Iii )
elif i11Ii1iIiII == 10057 :
 o0oOOOO0 ( "getFavorites" )
 OoO0oO ( )
elif i11Ii1iIiII == 10058 : iiIi1iI1iIii ( )
elif i11Ii1iIiII == 10059 : Donators_Guide ( )
elif i11Ii1iIiII == 10060 : iIiIIIIIii ( )
elif i11Ii1iIiII == 10061 : OO00 ( )
elif i11Ii1iIiII == 10062 : I1iii11 ( IiiiiI1i1Iii , O0o , OOOOO0O00 )
elif i11Ii1iIiII == 10063 : O0oOOo ( )
elif i11Ii1iIiII == 10064 : ooo000o000 ( )
elif i11Ii1iIiII == 10065 : i1III ( O0o )
elif i11Ii1iIiII == 10066 : O0O0Ooo ( O0o )
elif i11Ii1iIiII == 10068 : oooOoOOO0oo0o ( O0o )
elif i11Ii1iIiII == 10069 : iiI11i1II ( O0o )
elif i11Ii1iIiII == 10070 : II1I1Ii ( O0o )
elif i11Ii1iIiII == 10071 : Genie_Watch ( )
elif i11Ii1iIiII == 10072 : oo0 ( )
elif i11Ii1iIiII == 10073 : i1II1 ( O0o )
elif i11Ii1iIiII == 10074 : oOOOOoOO0o ( O0o )
elif i11Ii1iIiII == 10075 : OOOooo ( oo0O0o00o0O , IiiiiI1i1Iii , O0o )
elif i11Ii1iIiII == 10076 : o000ooooO0o ( O0o )
elif i11Ii1iIiII == 10077 : i1OOO0000oO ( O0o )
elif i11Ii1iIiII == 10078 : IiI1iIiIIIii ( )
elif i11Ii1iIiII == 10079 : Genie_Watch_Tv_Shows ( )
elif i11Ii1iIiII == 10080 : Genie_Watch_Tv_Genre ( O0o )
elif i11Ii1iIiII == 10081 : Genie_Watch_TV_PlayRun ( O0o )
elif i11Ii1iIiII == 10082 : Genie_Watch_TV_Episodes ( O0o , oo0O0o00o0O )
elif i11Ii1iIiII == 10083 : Genie_Watch_Tv_Recent ( O0o )
elif i11Ii1iIiII == 10084 : II1I11Ii1 ( )
elif i11Ii1iIiII == 10085 : ooOOO00Ooo ( )
elif i11Ii1iIiII == 10086 : IIII ( )
elif i11Ii1iIiII == 20000 : oOO ( )
elif i11Ii1iIiII == 20001 : OOo0o0Oo ( )
elif i11Ii1iIiII == 20002 : iIi1iIIIiIiI ( O0o )
elif i11Ii1iIiII == 20003 : ooOo0O0O0oOO0 ( O0o )
elif i11Ii1iIiII == 20004 : I1iIiI1IiIIII ( O0o )
elif i11Ii1iIiII == 21004 : iIiIii1I1II ( )
elif i11Ii1iIiII == 21005 : O0Oooo ( O0o )
elif i11Ii1iIiII == 21006 : I1IiIiIi1IiI1 ( O0o )
elif i11Ii1iIiII == 21007 : iI1i ( O0o )
elif i11Ii1iIiII == 30000 : oo00ooOoo ( )
elif i11Ii1iIiII == 30001 : OOoO ( )
elif i11Ii1iIiII == 10012 : Resolve ( O0o )
elif i11Ii1iIiII == 30003 : i1I1i ( )
elif i11Ii1iIiII == 30004 : O00oOoo0OoO0 ( O0o )
elif i11Ii1iIiII == 30005 : i11i1Ii1 ( O0o )
elif i11Ii1iIiII == 30006 : oOo0OooOo ( )
elif i11Ii1iIiII == 30007 : IiiIiiIi ( )
elif i11Ii1iIiII == 30008 : I1i1I ( O0o )
elif i11Ii1iIiII == 30009 : o0O0OO ( O0o )
elif i11Ii1iIiII == 30010 : I1iI ( O0o )
elif i11Ii1iIiII == 30011 : iIi1IIi1ii ( )
elif i11Ii1iIiII == 30012 : Iii11i ( )
elif i11Ii1iIiII == 30013 : OO0oOOo0o ( )
elif i11Ii1iIiII == 30014 : Oo0Oo0oOooOoOo ( )
elif i11Ii1iIiII == 30015 : i111IIIiI ( O0o , oo0O0o00o0O , I11i1II )
elif i11Ii1iIiII == 30016 : I1Ii1 ( O0o )
elif i11Ii1iIiII == 30019 : oOooO0 ( O0o )
elif i11Ii1iIiII == 30017 : i1II1I ( O0o )
elif i11Ii1iIiII == 30018 : IIIII1iii11 ( O0o )
elif i11Ii1iIiII == 30030 : I1i1I1II ( )
elif i11Ii1iIiII == 30031 : O0OOOOOO0 ( )
elif i11Ii1iIiII == 30032 : Ooo0Oo0o ( )
elif i11Ii1iIiII == 30033 : oo0Oo0 ( )
elif i11Ii1iIiII == 30034 : oOOoOOO0oo0 ( )
elif i11Ii1iIiII == 30035 : OOOooo0OooOoO ( O0o )
elif i11Ii1iIiII == 30036 : oOoOOOo ( O0o )
elif i11Ii1iIiII == 30037 : ii1I ( O0o )
elif i11Ii1iIiII == 30038 : oOO0OO0O ( )
elif i11Ii1iIiII == 30039 : iIi1III1I ( )
if 7 - 7: oo0OO . O0o0O0O0ooO0 - O0o0O0O0ooO0 / IiI11iII1 % I1ii11iIi11i
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
