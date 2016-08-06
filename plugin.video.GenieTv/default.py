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
IiiIII111iI = "3.0.3"
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
ooooooO0oo = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
IIiiiiiiIi1I1 = xbmc . translatePath ( 'special://home/userdata/addon_data' )
I1IIIii = IIiiiiiiIi1I1 + 'GenieTvWatched'
if not os . path . exists ( I1IIIii ) :
 os . makedirs ( I1IIIii )
oOoOooOo0o0 = I1IIIii + 'watched.txt'
if not os . path . exists ( oOoOooOo0o0 ) :
 open ( oOoOooOo0o0 , 'w+' )
OOOO = open ( oOoOooOo0o0 ) . read ( )
OOO00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
I11iii1Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
I1IIiiIiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
O000oo0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( iIi1ii1I1 ) == True :
 OOOOi11i1 = open ( iIi1ii1I1 ) . read ( )
else : OOOOi11i1 = [ ]
IIIii1II1II = o0oO0 . getSetting ( 'debug' )
if os . path . exists ( iIii1 ) == False :
 os . makedirs ( iIii1 )
def i1I1iI ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O = ''
 O00oO = ''
 try :
  o0O = urllib2 . urlopen ( oo0OooOOo0 )
  O00oO = o0O . read ( )
  o0O . close ( )
 except : pass
 if O00oO != '' :
  return O00oO
 else :
  O00oO = 'Failed'
  return O00oO
  if 39 - 39: O0O0O - i1IiIIIII % Ii1i111I / OoOO00O - IIiI1I - O00Oo000ooO0
OoO0O00 = [ ]
IIiII = i1I1iI ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if IIiII != 'Failed' :
 OoO0O00 . append ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not IIiII != 'Failed' :
 o0ooOooo000oOO = i1I1iI ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if o0ooOooo000oOO != 'Failed' :
  OoO0O00 . append ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not o0ooOooo000oOO != 'Failed' :
  Oo0oOOo = i1I1iI ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if Oo0oOOo != 'Failed' :
   OoO0O00 . append ( i1111 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not Oo0oOOo != 'Failed' :
   Oo0OoO00oOO0o = i1I1iI ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if Oo0OoO00oOO0o != 'Failed' :
    OoO0O00 . append ( i1111 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
OOO00O = ( str ( OoO0O00 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
OOoOO0oo0ooO = OOO00O + 'GenieArt/NEW/'
if 98 - 98: oO00Oo0o000 * O0oOO0 * Ii1I % IIiI1I
if 95 - 95: ooOoO0O00
def I1ii11iI ( ) :
 if not os . path . exists ( IiII ) :
  oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIi1i = 'genie tv repo not being installed '
  I1I1iIiII1 ( IIi1i )
 else :
  i11i1I1 ( )
  if 36 - 36: iI11I1II1I1I / OOooOOo * i1IiIIIII
def i11i1I1 ( ) :
 if 65 - 65: OoOO00O . iI11I1II1I1I / o0o00Oo0O - OoOO00O
 iii1i1iiiiIi = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 OO0OoO0o00 = open ( I1IIiiIiii ) . read ( )
 ooOO0O0ooOooO = open ( O000oo0O ) . read ( )
 if 55 - 55: I11i * OOooOOo
 o0O00oOoOO = re . compile ( 'version="(.+?)" provider' ) . findall ( OO0OoO0o00 )
 iIIi1i1 = re . compile ( 'version="(.+?)" provider-name' ) . findall ( ooOO0O0ooOooO )
 i1IIIiiII1 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( iii1i1iiiiIi )
 OOOOoOoo0O0O0 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( iii1i1iiiiIi )
 for OOOo00oo0oO in o0O00oOoOO :
  IIiIi1iI = OOOo00oo0oO
  for i1IiiiI1iI in i1IIIiiII1 :
   if not i1IiiiI1iI == IIiIi1iI :
    Oo0oO0ooo . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    i1iIi ( )
   if i1IiiiI1iI == IIiIi1iI :
    ooOOoooooo
 for II1I in iIIi1i1 :
  O0 = II1I
  for i1II1Iiii1I11 in OOOOoOoo0O0O0 :
   if not i1II1Iiii1I11 == O0 :
    Oo0oO0ooo . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    Oo0oO0ooo . close
    IIII ( )
   if i1II1Iiii1I11 == O0 :
    xbmc . sleep ( 100 )
    ooOOoooooo
def iiIiI ( ) :
 I1ii11iI ( )
 o00oooO0Oo ( )
 if 78 - 78: OoOO00O % oO00Oo0o000 + Ii1I
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']Force Genie Update Kodi 16+[/COLOR]' , i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , OOoOO0oo0ooO + 'GenieUpdate.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'My Build' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WIZARD[/COLOR]' , str ( OOO00O ) , 4001 , OOoOO0oo0ooO + 'Wizard.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Streams' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']STREAMS[/COLOR]' , str ( OOO00O ) , 4002 , OOoOO0oo0ooO + 'Streams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Music' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Music[/COLOR]' , str ( OOO00O ) , 4003 , OOoOO0oo0ooO + 'Music.png' , i1iIIi1 , '' )
  if 48 - 48: o0o00Oo0O
 if o0oO0 . getSetting ( 'Builders Toolbox' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']BUILDERS TOOLBOX[/COLOR]' , str ( OOO00O ) , 32 , OOoOO0oo0ooO + 'BuildersToolbox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Source List' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']SOURCE LIST[/COLOR]' , str ( OOO00O ) , 46 , OOoOO0oo0ooO + 'SoruceList.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Maintainance' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MAINTENANCE[/COLOR]' , str ( OOO00O ) , 3 , OOoOO0oo0ooO + 'Maintenance.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Addons' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ADDONS[/COLOR]' , '' , 10050 , OOoOO0oo0ooO + 'Addons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'APK Tool' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK TOOL[/COLOR]' , str ( OOO00O ) , 30039 , OOoOO0oo0ooO + 'APKTools.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Rss Feed' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv RSS Feed[/COLOR]' , str ( OOO00O ) , 39 , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , i1iIIi1 , '' )
  if 11 - 11: Ii1i111I + ii - oO0o / I11i + I1ii11iIi11i . IIiIiII11i
  if 41 - 41: OoOO00O - o0o00Oo0O - o0o00Oo0O
 oO00OOoO00 ( 'movies' , 'MAIN' )
def IiI111111IIII ( ) :
 i1Ii = wiz . log_check ( )
 ii111iI1iIi1 = i1Ii . replace ( LOG , "" )
 if os . path . exists ( i1Ii ) or not i1Ii == False :
  OOO = open ( i1Ii , mode = 'r' ) ; oo0OOo0 = OOO . read ( ) ; OOO . close ( )
  wiz . TextBoxes ( "%s - %s" % ( ADDONTITLE , ii111iI1iIi1 ) , oo0OOo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def I11IiI ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']BACKUP MY BUILD[/COLOR]' , str ( OOO00O ) , 10060 , OOoOO0oo0ooO + 'BackupMyBuild.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']RESTORE MY BUILD[/COLOR]' , str ( OOO00O ) , 49 , OOoOO0oo0ooO + 'RestoreMyBuild.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WIPE GENIE[/COLOR]' , str ( OOO00O ) , 41 , OOoOO0oo0ooO + 'WipeGenie.png' , i1iIIi1 , '' )
 if 53 - 53: IIiI1I % IIiIiII11i . O00Oo000ooO0 - iI11I1II1I1I - O00Oo000ooO0 * IIiIiII11i
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genie BUILDS[/COLOR]' , str ( OOO00O ) , 44 , OOoOO0oo0ooO + 'GenieBuilds.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def ooO0oOOooOo0 ( ) :
 I1ii11iI ( )
 if i1iiIIiiI111 == '5knuckleshuffle' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']XVID[/COLOR]' , str ( OOO00O ) , 10100 , OOoOO0oo0ooO + 'Jizbox.png' , i1iIIi1 , '' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ADULT CHANNELS[/COLOR]' , str ( OOO00O ) , 30033 , OOoOO0oo0ooO + 'adu.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Favourites' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']FAVOURITES[/COLOR]' , str ( OOO00O ) , 10057 , OOoOO0oo0ooO + 'Favourites.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Search' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , str ( OOO00O ) , 9000 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv Live List[/COLOR]' , '' , 4009 , OOoOO0oo0ooO + 'GTV.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , OOoOO0oo0ooO + 'TvGuide.png' , i1iIIi1 , '' )
  if 38 - 38: oO00Oo0o000
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']STREAM TEAM[/COLOR]' , str ( OOO00O ) , 4006 , OOoOO0oo0ooO + 'StreamTeam.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MOVIES[/COLOR]' , str ( OOO00O ) , 4004 , OOoOO0oo0ooO + 'Movies.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']TV SHOWS[/COLOR]' , str ( OOO00O ) , 4005 , OOoOO0oo0ooO + 'TVShows.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']FOOTBALL[/COLOR]' , '' , 10002 , OOoOO0oo0ooO + 'Football.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( OOO00O ) , 4007 , OOoOO0oo0ooO + 'Kids.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']24/7 STREAMS[/COLOR]' , '' , 30030 , OOoOO0oo0ooO + '247Streams.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEWS[/COLOR]' , str ( OOO00O ) , 30032 , OOoOO0oo0ooO + 'News.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv TUTORIALS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'GenieTVTutorials.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HOBBIES[/COLOR]' , str ( OOO00O ) , 4008 , OOoOO0oo0ooO + 'Hobbies.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'YOUTUBE' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH YOUTUBE[/COLOR]' , str ( OOO00O ) , 10064 , OOoOO0oo0ooO + 'SeachYouTube.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'REQUESTS' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']REQUESTS[/COLOR]' , str ( OOO00O ) + ( i1111 ( 'L1JFUVVFU1RTLnBocA==' ) ) , 10066 , OOoOO0oo0ooO + 'Requests.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Stand Up' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']STAND UP[/COLOR]' , '' , 10003 , OOoOO0oo0ooO + 'StandUp.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Documentaries' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']DOCUMENTARIES[/COLOR]' , str ( OOO00O ) , 8040 , OOoOO0oo0ooO + 'documentaries.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Disclose' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']DISCLOSE TV[/COLOR]' , str ( OOO00O ) , 7001 , OOoOO0oo0ooO + 'DiscloseTV.png' , i1iIIi1 , '' )
  if 84 - 84: iI11I1II1I1I % IIiI1I / iI11I1II1I1I % Ii1i111I
  if 45 - 45: o0o00Oo0O
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PLAYLIST LOADER[/COLOR]' , str ( OOO00O ) , 3000 , OOoOO0oo0ooO + 'PlaylistLoader.png' , i1iIIi1 , '' )
  if 26 - 26: Ii1i111I - iI11I1II1I1I - oOo0O0Ooo / oO0o . OOooOOo % iI11I1II1I1I
  if 91 - 91: I11i . iI11I1II1I1I / O0O0O + ooOoO0O00
  if 42 - 42: O0oOO0 . I11i . O0oOO0 - Ii1I
  if 40 - 40: O0oOO0 - Ii / OoOO00O
  if 35 - 35: OoOO00O - oOo0O0Ooo % I11i . ii % OoOO00O
  if 47 - 47: IIiI1I - OoOO00O . IIiIiII11i + ii . Ii
  if 94 - 94: I11i * OoOO00O / I1ii11iIi11i / OoOO00O
  if 87 - 87: I1ii11iIi11i . O00Oo000ooO0
  if 75 - 75: O0oOO0 + OOooOOo + I11i * Ii1i111I % O0O0O . IIiI1I
  if 55 - 55: i1IiIIIII . oOo0O0Ooo
  if 61 - 61: I1ii11iIi11i % O00Oo000ooO0 . I1ii11iIi11i
  if 100 - 100: oO00Oo0o000 * o0o00Oo0O
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 64 - 64: i1IiIIIII % iI11I1II1I1I * O0O0O
def o00oooO0Oo ( ) :
 if not os . path . exists ( II ) :
  o0iI11I1II ( 'Change Log 6/8/16 - v3.0.3' , 'G-Tv reintegrated into GenieTv, New look for the guide, football section put in streams with premier league table, fixtures and highlights, match list linked to G-Tv live streams, all searches updated, new servers online' )
  os . makedirs ( II )
  if 40 - 40: iI11I1II1I1I / OOooOOo % Ii1I + IIiIiII11i
  if 27 - 27: IIiIiII11i * OOooOOo * iI11I1II1I1I
def oOo00oOoO000 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( OOO00O ) , 9001 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']POPCORN BOX[/COLOR]' , str ( OOO00O ) , 7061 , OOoOO0oo0ooO + 'PopcornBox.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , OOoOO0oo0ooO + 'FilmTrailers.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , OOoOO0oo0ooO + 'ClassicMovies.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def OOooo0oOO0O ( ) :
 I1ii11iI ( )
 o00O0 ( )
 if 83 - 83: O0oOO0
 if 65 - 65: oOo0O0Ooo % OoOO00O * O0O0O
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , OOoOO0oo0ooO + 'TvGuide.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , OOoOO0oo0ooO + 'linkchannels.png' , i1iIIi1 , '' )
 if 19 - 19: oO00Oo0o000 + iI11I1II1I1I . ii . Ii1i111I / oO00Oo0o000 + O00Oo000ooO0
 if 85 - 85: Ii1I - iI11I1II1I1I
def Ii1iI1I1 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( OOO00O ) , 9002 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 57 - 57: Ii . Ii1I - OoOO00O - O0O0O + OOooOOo
 if 63 - 63: OOooOOo * IIiI1I
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH SERIES[/COLOR]' , '' , 10040 , OOoOO0oo0ooO + 'WatchSeries.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']iWATCH SERIES[/COLOR]' , '' , 8020 , OOoOO0oo0ooO + 'iWatchSeries.png' , i1iIIi1 , '' )
 if 69 - 69: o0o00Oo0O . oO0o
 if 49 - 49: oOo0O0Ooo - Ii1i111I
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC TV[/COLOR]' , str ( OOO00O ) , 8064 , OOoOO0oo0ooO + 'ClassicTV.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , OOoOO0oo0ooO + 'TVShowTrailers.png' , i1iIIi1 , '' )
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
 oO00OOoO00 ( 'movies' , 'MAIN' )
def oooOo0OOOoo0 ( ) :
 I1ii11iI ( )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'TheReaper.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PANDORAS BOX[/COLOR]' , str ( OOO00O ) , 10025 , OOoOO0oo0ooO + 'PandorasBox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbWFpbi5waHA=' ) ) , 1016 , OOoOO0oo0ooO + 'RedemptionStreams.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']DoJo STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'DojoStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , str ( OOO00O ) , 1023 , OOoOO0oo0ooO + 'ScoobyStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , '' , 1017 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'ITVStreams.png' , i1iIIi1 , '' )
 if 51 - 51: I1ii11iIi11i / OOooOOo . i1IiIIIII * I11i + oO0o * O00Oo000ooO0
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 73 - 73: oO0o + ii - o0o00Oo0O - OoOO00O - IIiIiII11i
def O0Oo0oOOoooOOOOo ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 if 62 - 62: O0oOO0
def o0O0o0 ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 if 37 - 37: Ii1I * Ii1i111I % Ii % O0oOO0 + OoOO00O
def OOoOO0o0o0 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'SearchCartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( OOO00O ) , 21004 , OOoOO0oo0ooO + 'watchcartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 10001 , OOoOO0oo0ooO + 'Cartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , OOoOO0oo0ooO + 'anime.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def ii1I1 ( ) :
 I1ii11iI ( )
 if o0oO0 . getSetting ( 'Football' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']FOOTBALL[/COLOR]' , '' , 10002 , OOoOO0oo0ooO + 'Football.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Fitness' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']FITNESS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , OOoOO0oo0ooO + 'Fitness.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Go Fishing' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Go Fishing[/COLOR]' , str ( OOO00O ) , 8090 , OOoOO0oo0ooO + 'GoFishing.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GenieTv Kitchen[/COLOR]' , ( i1111 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , OOoOO0oo0ooO + 'GenieTVKitchen.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 93 - 93: o0o00Oo0O % ooOoO0O00 . i1IiIIIII / oOo0O0Ooo - oO00Oo0o000 / oOo0O0Ooo
 if 36 - 36: O0O0O % O0O0O % ooOoO0O00 / ooOoO0O00 - O0oOO0
 if 30 - 30: Ii1i111I / oOo0O0Ooo
def ooOOoooooo ( ) :
 IIiII = Iiii ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o0O00oOoOO = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIiII )
 for IIi1i in o0O00oOoOO :
  IIi1i = ( str ( IIi1i ) )
  if os . path . exists ( xbmc . translatePath ( IIi1i ) ) :
   Iii1I1111ii = ( IIi1i ) . replace ( 'special://home/addons/' , '' )
   o0iI11I1II ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + Iii1I1111ii + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   ooOoO00 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if ooOoO00 == 0 :
    I1I1iIiII1 ( IIi1i )
    Ii1IIiI1i ( )
   elif ooOoO00 == 1 :
    o0O00Oo0 ( IIi1i )
  else :
   pass
   if 33 - 33: o0o00Oo0O * I11i - oO00Oo0o000 % oO00Oo0o000
def o0O00Oo0 ( addon ) :
 Iii1I1111ii = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 18 - 18: oO00Oo0o000 / I1ii11iIi11i * oO00Oo0o000 + oO00Oo0o000 * Ii * Ii1I
def I1I1iIiII1 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 I1II1 = os . path . join ( iiI1IiI , 'default.py' )
 oooO = open ( I1II1 , "w+" )
 if 26 - 26: OoOO00O % Ii1I
 oooO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oooO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oooO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 76 - 76: O00Oo000ooO0 * IIiI1I
 if 52 - 52: i1IiIIIII
 if 19 - 19: oOo0O0Ooo
 if 25 - 25: OoOO00O / O0oOO0
 if 31 - 31: i1IiIIIII . o0o00Oo0O % oOo0O0Ooo . I11i + O00Oo000ooO0
 if 71 - 71: oO00Oo0o000 . IIiIiII11i
 if 62 - 62: ii . Ii1i111I
 if 61 - 61: OOooOOo - i1IiIIIII - ooOoO0O00
 if 25 - 25: o0o00Oo0O * Ii1i111I + Ii1I . I11i . I11i
 if 58 - 58: oOo0O0Ooo
 if 53 - 53: ooOoO0O00
 if 59 - 59: I11i
 if 81 - 81: OOooOOo - OOooOOo . IIiI1I
 if 73 - 73: Ii1i111I % Ii - oOo0O0Ooo
 if 7 - 7: o0o00Oo0O * Ii * OoOO00O + O0oOO0 % oO0o - O0oOO0
 if 39 - 39: I1ii11iIi11i * i1IiIIIII % i1IiIIIII - ii + I11i - Ii1i111I
 if 23 - 23: Ii
 if 30 - 30: I11i - ooOoO0O00 % IIiIiII11i + Ii1i111I * iI11I1II1I1I
 if 81 - 81: O00Oo000ooO0 % ooOoO0O00 . iI11I1II1I1I
def Ii1Iii1iIi ( ) :
 o0OOOO00O0Oo ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Search' , '' , 10078 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 if 82 - 82: Ii1I / oOo0O0Ooo % iI11I1II1I1I / ooOoO0O00 - oOo0O0Ooo
def I1III1111iIi ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOo0oo0O0o00O = 'http://imoviemax.se/?s=' + ( I1i111I ) . replace ( ' ' , '+' )
 I1i11 = OooOo0oo0O0o00O . lower ( )
 IiIi1I1 ( I1i11 )
def IiIIi1 ( url ) :
 IIIIiii1IIii = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIiII )
 for url , II1i11I , ii1I1IIii11 in o0O00oOoOO :
  if II1i11I in IIIIiii1IIii :
   pass
  else :
   o0OOOO00O0Oo ( II1i11I + ' - ' + ii1I1IIii11 + ' Films' , url , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
   IIIIiii1IIii . append ( II1i11I )
   if 67 - 67: IIiI1I + Ii1i111I / I11i . O0O0O + i1IiIIIII
def ooOoOo0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I , I11iiiiI1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I + ' - Views:' + I11iiiiI1i , url , 10075 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
  if 40 - 40: Ii1I + ooOoO0O00 * i1IiIIIII
  if 85 - 85: OoOO00O * I1ii11iIi11i . o0o00Oo0O - Ii
def IiIi1I1 ( url ) :
 i1I1iIi = [ ]
 IIiII = Iiii ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIiII )
 for next in next :
  o0OOOO00O0Oo ( 'NEXT PAGE' , next , 10074 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , II1i11I , url in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 10075 , IIii11Ii1i1I , IIii11Ii1i1I , '' )
  i1I1iIi . append ( II1i11I )
  if 76 - 76: o0o00Oo0O + ooOoO0O00 . I1ii11iIi11i * oOo0O0Ooo * OoOO00O
def II1iI1I11I ( img , name , url ) :
 img = img
 name = name
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( IIiII )
 for o0OO0 , url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  IiI11ii1I = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + IiI11ii1I
  ooo = ( o0OO0 ) . replace ( 'play-' , 'Server ' )
  OOooOoooOoOo ( ooo , IiI11ii1I , 10076 , img , img , '' )
  if 36 - 36: ii . oO0o
def oOIIiIi ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( IIiII )
 for OOoOooOoOOOoo in o0O00oOoOO :
  if '=m' in OOoOooOoOOOoo :
   Iiii1iI1i ( OOoOooOoOOOoo )
  elif 'php' in OOoOooOoOOOoo :
   oOIIiIi ( url )
  else :
   IIiII = Iiii ( OOoOooOoOOOoo )
   o0O00oOoOO = re . compile ( 'content="(.+?)">' ) . findall ( IIiII )
   for I1ii1ii11i1I in o0O00oOoOO :
    Iiii1iI1i ( OOoOooOoOOOoo )
    if 58 - 58: IIiI1I + I1ii11iIi11i
    if 12 - 12: I11i - Ii1I % OOooOOo * Ii1i111I
    if 44 - 44: IIiI1I % OoOO00O
def iiI11i1II ( url ) :
 IIiII = Iiii ( url )
 OO0O0OOo0O = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for I1 , o0OooOOOOOO in OO0O0OOo0O :
  print 'there ><><><><><><><><><><><><'
  I1 = I1
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0OooOOOOOO ) )
  for II1i11I , OOooO0o0 in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + I1 + '[/COLOR] - ' + II1i11I + ' - [COLOR' + oO0o0o0ooO0oO + ']' + OOooO0o0 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
 iiIII1i = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for I1 , I1I in iiIII1i :
  print 'there ><><><><><><><><><><><><'
  I1 = I1
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I1I ) )
  for II1i11I , OOooO0o0 in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + I1 + '[/COLOR] - ' + II1i11I + ' - [COLOR' + oO0o0o0ooO0oO + ']' + OOooO0o0 + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
   if 68 - 68: O0oOO0
   if 25 - 25: Ii1I . O0oOO0
   if 24 - 24: O0O0O / Ii + O0O0O
def I1i11i ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
 for iiIII1i in iiIII1i :
  II1i11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iiIII1i ) )
  for II1i11I in II1i11I :
   II1i11I = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIII1i ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IiIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( iiIII1i ) )
  for IiIi in IiIi :
   IiIi = 'http:' + IiIi
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , '' , '' )
  if 87 - 87: Ii1I - Ii1I - IIiI1I + O0O0O
  if 82 - 82: O0O0O / iI11I1II1I1I . oOo0O0Ooo . i1IiIIIII / I11i
  if 42 - 42: I1ii11iIi11i
  if 19 - 19: O0O0O % Ii1I * iI11I1II1I1I + oOo0O0Ooo
def iii11I ( url ) :
 if 50 - 50: IIiI1I + o0o00Oo0O + OoOO00O . IIiIiII11i / I11i
 i1Iii11I1i = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIiII )
 for OOoOooOoOOOoo , IIii11Ii1i1I , II1i11I , Oo00o0OO0O00o in o0O00oOoOO :
  II1i11I = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0ooOooo000oOO = Iiii ( OOoOooOoOOOoo )
  iIIi1i1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0ooOooo000oOO )
  for O0Oooo , iiIi1i in iIIi1i1 :
   I1i11111i1i11 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( iiIi1i ) )
   for OOoOOO0 in I1i11111i1i11 :
    if II1i11I in i1Iii11I1i :
     pass
    else :
     OOooOoooOoOo ( II1i11I , O0Oooo , 8043 , IIii11Ii1i1I , IIii11Ii1i1I , OOoOOO0 )
     oO00OOoO00 ( 'movies' , 'INFO' )
     i1Iii11I1i . append ( II1i11I )
     if 10 - 10: oO00Oo0o000 / O0oOO0 + Ii / OoOO00O
     if 74 - 74: i1IiIIIII + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
def oOOO0oo0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , o00OooO0oo , OOoOOO0 , o0o0oOoOO0O , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 10065 , o00OooO0oo , o0o0oOoOO0O , OOoOOO0 )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 16 - 16: O00Oo000ooO0 % iI11I1II1I1I . OoOO00O
def oooooOOO000Oo ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOo0oo0O0o00O = 'https://www.youtube.com/results?search_query=' + ( I1i111I ) . replace ( ' ' , '+' )
 I1i11 = OooOo0oo0O0o00O . lower ( )
 IIiII = Iiii ( I1i11 )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for Ooo00OoOOO in next :
  Ooo00OoOOO = 'https://www.youtube.com' + Ooo00OoOOO
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , Ooo00OoOOO , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for IIii11Ii1i1I , Ooo00OoOOO , II1i11I , Oo0OO0000oooo , iiIi1i in o0O00oOoOO :
  OO0o . append ( II1i11I )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  IiIi = 'http:' + ( IIii11Ii1i1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiIi
  Ooo00OoOOO = 'http://www.youtube.com' + Ooo00OoOOO
  OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , IiIi , iiIi1i )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for IIii11Ii1i1I , Ooo00OoOOO , II1i11I , Oo0OO0000oooo in o0O00oOoOO :
   print 'im doing it'
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   IiIi = 'http:' + ( IIii11Ii1i1I ) . replace ( 'https:' , '' )
   Ooo00OoOOO = 'http://www.youtube.com' + Ooo00OoOOO
   if '&' in Ooo00OoOOO :
    print ' i got here'
    IIiII = Iiii ( Ooo00OoOOO )
    iiIII1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for iiIII1i in iiIII1i :
     II1i11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iiIII1i ) )
     for II1i11I in II1i11I :
      II1i11I = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     Ooo00OoOOO = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIII1i ) )
     for Ooo00OoOOO in Ooo00OoOOO :
      Ooo00OoOOO = 'https://www.youtube.com/w' + Ooo00OoOOO
     IiIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( iiIII1i ) )
     for IiIi in IiIi :
      IiIi = 'http:' + IiIi
     OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , i1iIIi1 , '' )
   elif II1i11I in OO0o :
    pass
   elif 'user' in Ooo00OoOOO or 'elete' in II1i11I :
    pass
   elif 'hannel' in Ooo00OoOOO :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Ooo00OoOOO
    IIiII = Iiii ( Ooo00OoOOO )
    IIII1iII = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for IIii11Ii1i1I , Ooo00OoOOO , II1i11I in IIII1iII :
     if 'outube' in Ooo00OoOOO or 'list' in Ooo00OoOOO :
      pass
     elif 'atch' in Ooo00OoOOO :
      Ooo00OoOOO = ( Ooo00OoOOO ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIii11Ii1i1I , 'http:' + IIii11Ii1i1I , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , IiIi , '' )
    if 28 - 28: ooOoO0O00 - IIiI1I
def o00o000oo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for url in next :
  url = 'https://www.youtube.com' + url
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , url , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for IIii11Ii1i1I , url , II1i11I , Oo0OO0000oooo , iiIi1i in o0O00oOoOO :
  OO0o . append ( II1i11I )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  IiIi = 'http:' + ( IIii11Ii1i1I ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiIi
  url = 'http://www.youtube.com' + url
  OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , IiIi , iiIi1i )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for IIii11Ii1i1I , url , II1i11I , Oo0OO0000oooo in o0O00oOoOO :
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   IiIi = 'http:' + ( IIii11Ii1i1I ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIiII = Iiii ( url )
    iiIII1i = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for iiIII1i in iiIII1i :
     II1i11I = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( iiIII1i ) )
     for II1i11I in II1i11I :
      II1i11I = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIII1i ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IiIi = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( iiIII1i ) )
     for IiIi in IiIi :
      IiIi = 'http:' + IiIi
     OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , i1iIIi1 , '' )
   elif II1i11I in OO0o :
    pass
   elif 'user' in url or 'elete' in II1i11I :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIiII = Iiii ( url )
    IIII1iII = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for IIii11Ii1i1I , url , II1i11I in IIII1iII :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + IIii11Ii1i1I , 'http:' + IIii11Ii1i1I , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + Oo0OO0000oooo + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi , IiIi , '' )
    if 44 - 44: oOo0O0Ooo - Ii1i111I % iI11I1II1I1I
    if 71 - 71: O0oOO0 . OoOO00O - ii % OoOO00O . IIiIiII11i
def o00O0 ( ) :
 if oO == 'insert_password' :
  oOOoo00O0O . ok ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + oO0o0o0ooO0oO + ']http://GenieTv.co.uk[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  O0iIiIIIIIii = open ( o0 )
  o0O00oOoOO = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( O0iIiIIIIIii ) )
  for OOo0 , ii11I1 in o0O00oOoOO :
   if OOo0 == 'needs replacing' or ii11I1 == 'needs replacing' :
    oO0oo ( )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv PRIVATE LIST[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'PrivateList.png' , i1iIIi1 , '' )
  if 38 - 38: ii * O0oOO0 % o0o00Oo0O * OOooOOo
def IIiiI ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + Ooo + ")" )
 oO0oo ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 31 - 31: Ii1I + OoOO00O + oO00Oo0o000 / OoOO00O
def iiI111 ( ) :
 try :
  I1iIiIi11i11 = gui . TVGuide ( )
  I1iIiIi11i11 . doModal ( )
  del I1iIiIi11i11
  if 52 - 52: O0oOO0 + o0o00Oo0O . IIiI1I . Ii1I . oO0o
 except :
  import sys
  import traceback as tb
  ( oo000ii , OoO , traceback ) = sys . exc_info ( )
  tb . print_exception ( oo000ii , OoO , traceback )
  if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . i1IiIIIII
def O0iII1 ( ) :
 o0OOOO00O0Oo ( 'Full Backup' , '' , 10061 , OOoOO0oo0ooO + 'FullBackUp.png' , i1iIIi1 , 'Back Up Your Full System' )
 if os . path . exists ( I11iii1Ii ) :
  o0OOOO00O0Oo ( 'Backup Genie Favourites' , Ooo00OoOOO , 10062 , OOoOO0oo0ooO + 'BackupGenieFavourites.png' , i1iIIi1 , 'Back Up Your favourites' )
 if os . path . exists ( iiiiiIIii ) :
  o0OOOO00O0Oo ( 'Backup Ivue Config' , iiiiiIIii , 10062 , OOoOO0oo0ooO + 'BackUpIvueConfig.png' , i1iIIi1 , 'Back Up Your master.db' )
 if os . path . exists ( O000OO0 ) :
  o0OOOO00O0Oo ( 'Backup Kodi Favourites' , O000OO0 , 10062 , OOoOO0oo0ooO + 'BackKodiFavourites.png' , i1iIIi1 , 'Back Up Your favourites.xml' )
  if 27 - 27: oO0o . Ii1i111I + OOooOOo / iI11I1II1I1I % IIiI1I . O0oOO0
  if 14 - 14: O0O0O + Ii1I - IIiI1I / o0o00Oo0O . oO00Oo0o000
  if 45 - 45: oO00Oo0o000
zip = o0oO0 . getSetting ( 'zip' )
oOIIi1iiii1iI = xbmc . translatePath ( os . path . join ( zip ) )
def iIiiii ( ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 51 - 51: oOo0O0Ooo / O00Oo000ooO0 / OoOO00O
  if 6 - 6: OoOO00O - O0oOO0 * i1IiIIIII . IIiI1I / o0o00Oo0O * O0oOO0
  if 22 - 22: I1ii11iIi11i % IIiI1I * Ii1I / i1IiIIIII % Ii * Ii1i111I
def Oo00OoOo ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I11iii1Ii
  elif 'Ivue' in name :
   url = iiiiiIIii
  elif 'Kodi' in name :
   url = O000OO0
  iIiiii ( )
  ii1ii111 = open ( url ) . read ( )
  i11111I1I = os . path . join ( oOIIi1iiii1iI , description . split ( 'Your ' ) [ 1 ] )
  OOO = open ( i11111I1I , mode = 'w' )
  OOO . write ( ii1ii111 )
  OOO . close ( )
 else :
  if 'guisettings.xml' in description :
   ii1 = open ( os . path . join ( oOIIi1iiii1iI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Oo0000oOo = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   o0O00oOoOO = re . compile ( Oo0000oOo ) . findall ( ii1 )
   for type , I11o0oO00oO0o0o0 , I1Iooooo in o0O00oOoOO :
    I1Iooooo = I1Iooooo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I11o0oO00oO0o0o0 , I1Iooooo ) )
  else :
   i11111I1I = os . path . join ( url )
   ii1ii111 = open ( os . path . join ( oOIIi1iiii1iI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOO = open ( i11111I1I , mode = 'w' )
   OOO . write ( ii1ii111 )
   OOO . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 1 - 1: O0oOO0 % OOooOOo * I1ii11iIi11i
 if 55 - 55: OOooOOo
 if 87 - 87: ii % IIiI1I . oOo0O0Ooo / O0oOO0
 if 8 - 8: Ii1i111I + I11i
def oOOo0o0oo ( ) :
 i11iiiiI1i = 1
 iIiiii ( )
 iIIii = xbmc . translatePath ( os . path . join ( oOIIi1iiii1iI , 'Build Backup' , 'Full Backup' , '' ) )
 i1iIiIi1I = xbmc . translatePath ( os . path . join ( oOIIi1iiii1iI , 'Build Backup' , 'my_full_backup.zip' ) )
 iiii11i = xbmc . translatePath ( os . path . join ( oOIIi1iiii1iI , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIIii ) :
  os . makedirs ( iIIii )
 III11II1I1Ii1 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not III11II1I1Ii1 ) : return False , 0
 O00Oo0o000oO = III11II1I1Ii1
 oO0o00oOOooO0 = xbmc . translatePath ( os . path . join ( iIIii , O00Oo0o000oO + '.zip' ) )
 OOOoO000 = [ 'plugin.video.GenieTv' ]
 oOOOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 IiIi1ii111i1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i1i1i1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 oOoo000 = "Creating full backup of existing build"
 OooOo00o = "Creating Community Build"
 IiI11i1IIiiI = "Archiving..."
 oOOo000oOoO0 = ""
 OoOo00o0OO = "Please Wait"
 ii1IIIIiI11 ( i1iiIII111ii , oO0o00oOOooO0 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 , OoOo00o0OO , IiIi1ii111i1 , i1i1i1I )
 time . sleep ( 1 )
 iI1IIIii = xbmc . translatePath ( os . path . join ( iIIii , O00Oo0o000oO + '_guisettings.zip' ) )
 I1i11ii11 = zipfile . ZipFile ( iI1IIIii , mode = 'w' )
 try :
  I1i11ii11 . write ( xbmc . translatePath ( os . path . join ( i1iiIII111ii , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1i11ii11 . close ( )
 if i11iiiiI1i == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i1iIiIi1I , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oO0o00oOOooO0 + '[/COLOR]' )
  if 81 - 81: i1IiIIIII - Ii1i111I % O0oOO0 - oO0o / I1ii11iIi11i
def ii1IIIIiI11 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Ii1iI111 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 O0oooo00o0Oo = len ( sourcefile )
 I1iii = [ ]
 oO0o0O0Ooo0o = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for i1Ii11II , IioO0oOOO0Ooo , i1i1I in os . walk ( sourcefile ) :
  for file in i1i1I :
   oO0o0O0Ooo0o . append ( file )
 IiIIi1iII11I1Ii1 = len ( oO0o0O0Ooo0o )
 for i1Ii11II , IioO0oOOO0Ooo , i1i1I in os . walk ( sourcefile ) :
  IioO0oOOO0Ooo [ : ] = [ o0o0 for o0o0 in IioO0oOOO0Ooo if o0o0 not in exclude_dirs ]
  i1i1I [ : ] = [ OOO for OOO in i1i1I if OOO not in exclude_files ]
  for file in i1i1I :
   I1iii . append ( file )
   oOo0oO = len ( I1iii ) / float ( IiIIi1iII11I1Ii1 ) * 100
   Oo0oO0ooo . update ( int ( oOo0oO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IIi1IIIIi = os . path . join ( i1Ii11II , file )
   if not 'temp' in IioO0oOOO0Ooo :
    if not 'plugin.program.originwizard' in IioO0oOOO0Ooo :
     import time
     OOOoO = '01/01/1980'
     I1i = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IIi1IIIIi ) ) )
     if I1i > OOOoO :
      Ii1iI111 . write ( IIi1IIIIi , IIi1IIIIi [ O0oooo00o0Oo : ] )
 Ii1iI111 . close ( )
 Oo0oO0ooo . close ( )
 if 12 - 12: ii
 if 20 - 20: ooOoO0O00 - Ii1i111I
def ii1ii11 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 if 84 - 84: o0o00Oo0O . Ii1i111I - IIiIiII11i . O0oOO0 / IIiIiII11i
 if 47 - 47: ii
def ii1i1i1IiII ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( OOO00O ) , 9001 , OOoOO0oo0ooO + 'MOVIESv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( OOO00O ) , 9002 , OOoOO0oo0ooO + 'TVSHOWSv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON' , i1iIIi1 , '' )
 if 63 - 63: IIiI1I . oO0o / IIiIiII11i * O00Oo000ooO0 + O0O0O % OoOO00O
 if 12 - 12: oO00Oo0o000 . oO0o . IIiI1I - ii % I1ii11iIi11i
 if 36 - 36: i1IiIIIII
 if 84 - 84: oO00Oo0o000 . oO0o . IIiIiII11i . Ii1i111I / OoOO00O % Ii1I
def OOO0oOoO0O ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWM=' ) ) , 1006 , OOoOO0oo0ooO + 'Quicksilver.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC CHANNELS[/COLOR]' , str ( OOO00O ) , 30031 , OOoOO0oo0ooO + 'MusicChannels.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , OOoOO0oo0ooO + 'UKRadio.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WORLD RADIO[/COLOR]' , str ( OOO00O ) , 1013 , OOoOO0oo0ooO + 'WorldRadio.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , OOoOO0oo0ooO + 'Concerts.png' , i1iIIi1 , '' )
  if 84 - 84: o0o00Oo0O * ii - O00Oo000ooO0 * O00Oo000ooO0
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , OOoOO0oo0ooO + 'MusicVideos.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( OOO00O ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOoOO0oo0ooO + 'Music.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC SEARCH[/COLOR]' , str ( OOO00O ) , 1111 , OOoOO0oo0ooO + 'MusicSearch.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , i1iIIi1 , '' )
 if 8 - 8: O0oOO0 / ooOoO0O00 . O0O0O
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 41 - 41: IIiI1I + oO0o
def oOO ( ) :
 I1ii11iI ( )
 if 11 - 11: Ii - O0O0O . O0O0O
 OOooOoooOoOo ( 'DELETE CACHE' , 'url' , 14 , OOoOO0oo0ooO + 'DeleteCache.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'DELETE PACKAGES' , 'url' , 6 , OOoOO0oo0ooO + 'DeletePackages.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FORCE REFRESH' , 'url' , 10 , OOoOO0oo0ooO + 'ForceRefresh.png' , i1iIIi1 , 'Force Refresh All Repos' )
 if 31 - 31: i1IiIIIII / I1ii11iIi11i * ooOoO0O00 . OOooOOo
 OOooOoooOoOo ( 'CHECK MY IP' , 'url' , 12 , OOoOO0oo0ooO + 'CheckMyIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOoOO0oo0ooO + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , i1iIIi1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ADVANCED SETTINGS XML[/COLOR]' , str ( OOO00O ) , 4 , OOoOO0oo0ooO + 'AdvancedSettingXML.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']URL FIXES[/COLOR]' , str ( OOO00O ) , 20 , OOoOO0oo0ooO + 'URLFixes.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 57 - 57: i1IiIIIII + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
 if 83 - 83: I11i / Ii % iI11I1II1I1I . Ii1i111I % O0O0O . ii
def iI1Ii11111iIi ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']REPOS[/COLOR]' , ( i1111 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , OOoOO0oo0ooO + 'repos.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEW[/COLOR]' , str ( OOO00O ) , 22 , OOoOO0oo0ooO + 'NEW.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']IPTV[/COLOR]' , str ( OOO00O ) , 23 , OOoOO0oo0ooO + 'IPTV.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']VIDEO[/COLOR]' , str ( OOO00O ) , 24 , OOoOO0oo0ooO + 'VIDEO.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SPORTS[/COLOR]' , str ( OOO00O ) , 25 , OOoOO0oo0ooO + 'SPORTS.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( OOO00O ) , 26 , OOoOO0oo0ooO + 'KIDS.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( OOO00O ) , 27 , OOoOO0oo0ooO + 'MUSIC.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PROGRAMS[/COLOR]' , str ( OOO00O ) , 28 , OOoOO0oo0ooO + 'PROGRAMS.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']XXX[/COLOR]' , 'URL' , 29 , OOoOO0oo0ooO + 'XXX.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 94 - 94: OoOO00O + iI11I1II1I1I % oO0o
 if 93 - 93: OoOO00O - i1IiIIIII + iI11I1II1I1I * I11i + oO00Oo0o000 . IIiI1I
def IiI1iII1II111 ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( 'CHECK ADVANCED XML' , str ( OOO00O ) , 8 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'MUCKYS XML' , str ( OOO00O ) + '/wizard/muckys.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '0CACHE XML' , str ( OOO00O ) + '/wizard/0cache.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'MIKEY1234 XML' , str ( OOO00O ) + '/wizard/mikey.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'TUXENS XML' , str ( OOO00O ) + '/wizard/tuxens.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'P2P RECOMMENDED XML1' , str ( OOO00O ) + '/wizard/p2p1.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'P2P RECOMMENDED XML2' , str ( OOO00O ) + '/wizard/p2p2.xml' , 7 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'DELETE XML' , str ( OOO00O ) , 11 , OOoOO0oo0ooO + 'XML.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 28 - 28: OOooOOo * oO0o . Ii1i111I % Ii1i111I / Ii1i111I * oO00Oo0o000
def ooO00O0O0 ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Local Zip[/COLOR]' , I11 , 48 , OOoOO0oo0ooO + 'MyLocalZIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Online Zip[/COLOR]' , i11 , 43 , OOoOO0oo0ooO + 'MyOnlineZip.png' , i1iIIi1 , '' )
 if 33 - 33: I1ii11iIi11i
def II11i11Iii ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( OOO00O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOoOO0oo0ooO + 'FTV4.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( OOO00O ) + '/wizard/customftv/settings.xml' , 17 , OOoOO0oo0ooO + 'FTV3.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOoOO0oo0ooO + 'FTV1.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'RESET FTV DATABASE' , 'url' , 18 , OOoOO0oo0ooO + 'FTV2.png' , i1iIIi1 , '' )
 if 68 - 68: ii % IIiIiII11i
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % Ii1i111I * Ii1i111I * Ii1I
 if 24 - 24: IIiIiII11i % oO00Oo0o000 - O0oOO0 + oOo0O0Ooo * Ii1I
def i11111I1IOoo0ooOOOOoOo ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SKINS[/COLOR]' , str ( OOO00O ) , 33 , OOoOO0oo0ooO + 'Skins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ARTWORK PACKS[/COLOR]' , str ( OOO00O ) , 34 , OOoOO0oo0ooO + 'ArtworkPacks.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIII111ii , 35 , OOoOO0oo0ooO + 'CreateUniversalPath.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 34 - 34: ii . o0o00Oo0O / O0O0O * OOooOOo - Ii1I
def IiiiI ( ) :
 O00oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o0O00oOoOO = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O00oO )
 for IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , IIii11Ii1i1I , IIii11Ii1i1I , '' )
 oO00OOoO00 ( 'tvshows' , 'INFO' )
 if 42 - 42: ooOoO0O00 . oOo0O0Ooo / ooOoO0O00 + OoOO00O
def O0o0O0OO00o ( url ) :
 O00oO = Iiii ( OOo00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 5 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 81 - 81: O00Oo000ooO0 . I11i / oO00Oo0o000
def Iii111Ii ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GOTHAM SKINS[/COLOR]' , str ( OOO00O ) , 36 , OOoOO0oo0ooO + 'GothamSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HELIX SKINS[/COLOR]' , str ( OOO00O ) , 37 , OOoOO0oo0ooO + 'HelixSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ISENGAARD SKINS[/COLOR]' , i1iiIII111ii , 38 , OOoOO0oo0ooO + 'IsengaardSkins.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 54 - 54: OoOO00O * oO00Oo0o000 - ii % oOo0O0Ooo + o0o00Oo0O
def IIiiIIIi ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OO0O0o0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: OoOO00O
def iIIiI1I1i ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + O0O0OOooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: oOo0O0Ooo * O0O0O + ii - IIiI1I / ii
def I111IIiii1Ii ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 32 - 32: oOo0O0Ooo - Ii1I - I1ii11iIi11i
def iiI1i11II ( url ) :
 O00oO = Iiii ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: O0O0O / O00Oo000ooO0 * I11i . IIiIiII11i
def oooOO0OO0O ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 40 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 47 - 47: I11i + IIiI1I - O0O0O % ii
def o0O0 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + ooOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 5 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 21 - 21: OOooOOo + Ii + oOo0O0Ooo * I11i % IIiI1I % IIiIiII11i
def oOO0OO0OO ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK (Android only)[/COLOR]' , str ( OOO00O ) , 2 , OOoOO0oo0ooO + 'APKAndroidOnly.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK Search[/COLOR]' , str ( OOO00O ) , 30038 , OOoOO0oo0ooO + 'APKSearch.png' , i1iIIi1 , '' )
 if 87 - 87: O0O0O + iI11I1II1I1I - ii
def IiI1 ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5hcGtjcmFmdC5jb20v' ) )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Android Apps</a>' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'href="(.+?)">Android Games</a>' ) . findall ( iIi1i1iIi1iI )
 i1IIii1iiIi = re . compile ( 'href="(.+?)">Wallpapers</a>' ) . findall ( iIi1i1iIi1iI )
 oooo0OOo = re . compile ( 'href="(.+?)">Widgets</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO in o0O00oOoOO :
  OoO00 ( 'Android Apps' , Ooo00OoOOO , 30035 , OOoOO0oo0ooO + 'apps.png' )
 for Ooo00OoOOO in iIIi1i1 :
  OoO00 ( 'Android Games' , Ooo00OoOOO , 30035 , OOoOO0oo0ooO + 'GAMES.png' )
 for Ooo00OoOOO in i1IIii1iiIi :
  OoO00 ( 'Wallpapers' , Ooo00OoOOO , 30036 , OOoOO0oo0ooO + 'wallpapers.png' )
 for Ooo00OoOOO in oooo0OOo :
  OoO00 ( 'Widgets' , Ooo00OoOOO , 30036 , OOoOO0oo0ooO + 'widgets.png' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def I11iIi1II ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if 'cat' in url :
   OoO00 ( II1i11I , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def ooo0OO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '" target="_blank" href="([^"]*)"><img title="([^"]*)" src="([^"]*)"></a></dt>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'class="pagination_next"><a href="(.+?)">»</a></li>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( II1i11I , 'https://apkpure.com' + url , 30037 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT PAGE' , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def iIi1IiI ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">Download APK<span' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I11IIIiIi11 ( url )
def I11IIIiIi11 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I11iiIi1i1 ( url )
def i1IiiI1iIi ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OooOo0oo0O0o00O = 'https://apkpure.com/search?q=' + ( I1i111I ) . replace ( ' ' , '+' ) + '&region='
 I1i11 = OooOo0oo0O0o00O . lower ( )
 ooo0OO ( I1i11 )
 if 66 - 66: oO0o * I1ii11iIi11i
def I11iiIi1i1 ( url ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( II1IIIiiI11 , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , II1i11I + '.apk' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 17 - 17: o0o00Oo0O . oO00Oo0o000 . o0o00Oo0O + o0o00Oo0O / I1ii11iIi11i . O0oOO0
def OO00OOoO0o ( url ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , II1i11I + '.mp4' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 4 - 4: ooOoO0O00 - Ii / Ii / ii
 if 100 - 100: I1ii11iIi11i + I11i - o0o00Oo0O % IIiIiII11i . IIiI1I
def ooOo0OoOooo00 ( name , url , description ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , name )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 OO00O000OOO = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OO00O000OOO
 print '======================================='
 extract . all ( OO0ooOOO00 , OO00O000OOO , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 3 - 3: o0o00Oo0O
 if 64 - 64: ooOoO0O00 % O0oOO0 / Ii - ooOoO0O00 % i1IiIIIII . IIiI1I
def II1i111 ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 5 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 50 - 50: O00Oo000ooO0 % ooOoO0O00
 if 21 - 21: ii - iI11I1II1I1I
def OO0OoOOO0 ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 30015 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 90 - 90: O0oOO0 + IIiIiII11i * Ii1I / OoOO00O . I11i + I11i
def I11I ( url , iconimage , fanart ) :
 O00oO = Iiii ( url )
 IiI11ii1I = url
 IIii11Ii1i1I = iconimage
 fanart = fanart
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for OOoOooOoOOOoo , II1i11I in o0O00oOoOO :
  if '.mp4' in II1i11I :
   OOooOoooOoOo ( 'Watch VIDEO' , url + '/' + OOoOooOoOOOoo , 222 , IIii11Ii1i1I , fanart , '' )
  if 'description' in II1i11I :
   OOooOoooOoOo ( 'Read Description' , url + '/' + OOoOooOoOOOoo , 30017 , IIii11Ii1i1I , fanart , '' )
  if 'images' in II1i11I :
   o0OOOO00O0Oo ( 'View Images' , url + '/' + OOoOooOoOOOoo , 30018 , IIii11Ii1i1I , fanart , '' )
  if 'url' in II1i11I :
   OOooOoooOoOo ( 'Install Build On Android' , url + '/' + OOoOooOoOOOoo , 30016 , IIii11Ii1i1I , fanart , '' )
  if 'url' in II1i11I :
   OOooOoooOoOo ( 'Install Build On Pc' , url + '/' + OOoOooOoOOOoo , 30019 , IIii11Ii1i1I , fanart , '' )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 69 - 69: ooOoO0O00
def ooOoOOOOo ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  ooooOooooOOo ( url )
  if 96 - 96: IIiI1I
def i1I11iIII1i1I ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  oOO0oo ( url )
  if 13 - 13: ii * O0O0O - OoOO00O / i1IiIIIII + Ii1i111I + O00Oo000ooO0
def iii1III1i ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'desc="(.+?)"' ) . findall ( O00oO )
 for iiiIi in o0O00oOoOO :
  o0iI11I1II ( 'Description:' , iiiIi )
  if 45 - 45: Ii1I + oO0o * Ii / i1IiIIIII % Ii1i111I * o0o00Oo0O
def i1o0oooO ( url ) :
 O00oO = Iiii ( url )
 url = url
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for OOoOooOoOOOoo , II1i11I in o0O00oOoOO :
  if 'png' in II1i11I :
   OOooOoooOoOo ( 'image' , '' , '' , url + '/' + OOoOooOoOOOoo , url + '/' + OOoOooOoOOOoo , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 89 - 89: IIiIiII11i / O0O0O
def IIo0OoO00 ( name , url , description ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , name + '.zip' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIIIIiII1
 print '======================================='
 extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 Ii1IIiI1i ( )
 if 45 - 45: oOo0O0Ooo / IIiI1I . IIiI1I
 if 35 - 35: oO00Oo0o000 . OOooOOo * Ii
def oOO0oo ( url ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIIIIiII1
 print '======================================='
 extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
 iiII ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 o0Oii1111i ( )
 if 75 - 75: O00Oo000ooO0 + IIiIiII11i / O0O0O - O0O0O / ii
def ooooOooooOOo ( url ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIIIIiII1
 print '======================================='
 extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
 iiII ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "DO NOT EXIT CLEANLY VIA SHUTDOWN, Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 2 - 2: I11i
 if 19 - 19: IIiIiII11i
def OoOO ( name , url , description ) :
 IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 OO0ooOOO00 = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print IIIIIiII1
 print '======================================='
 extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 32 - 32: OOooOOo * oOo0O0Ooo % O0oOO0 * OoOO00O . o0o00Oo0O
 if 48 - 48: IIiI1I * IIiI1I
def o0Oii1111i ( ) :
 ooOoO00 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if ooOoO00 == 0 :
  return
 elif ooOoO00 == 1 :
  pass
 I1I1 = iI1I1iiIi1I ( )
 print "Platform: " + str ( I1I1 )
 if I1I1 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1I1 == 'linux' :
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
 elif I1I1 == 'android' :
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
 elif I1I1 == 'windows' :
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
  if 26 - 26: O00Oo000ooO0 / ooOoO0O00 * O0O0O . oOo0O0Ooo
def iI1I1iiIi1I ( ) :
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
  if 17 - 17: OoOO00O . Ii
  if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . oO00Oo0o000 - O0oOO0
  if 63 - 63: O0O0O
def Oo0 ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( url ) :
  for file in i1i1I :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    ii1 = open ( ( os . path . join ( OOo0Oo0OOo0 , file ) ) ) . read ( )
    i1i11I = ii1 . replace ( i1iiIII111ii , 'special://home/' )
    OOO = open ( ( os . path . join ( OOo0Oo0OOo0 , file ) ) , mode = 'w' )
    OOO . write ( str ( i1i11I ) )
    OOO . close ( )
 o0Oii1111i ( )
 if 7 - 7: IIiIiII11i
def iI ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , 'http://www.listenlive.eu/' + Ooo00OoOOO , 10111113 , OOoOO0oo0ooO + 'radio.png' )
def i1oOOOOOOOoO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 222 , OOoOO0oo0ooO + 'radio.png' )
  if 84 - 84: Ii1i111I - I1ii11iIi11i / o0o00Oo0O - oO00Oo0o000
def ii1iI1II11ii ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.toonjet.com/' + Ooo00OoOOO , 8051 , OOoOO0oo0ooO + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1i1IiIiIi1Ii ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I in o0O00oOoOO :
  if 'ol.gif' in IIii11Ii1i1I :
   pass
  elif 'link_block_' in IIii11Ii1i1I :
   pass
  elif '.png' in IIii11Ii1i1I :
   pass
  else :
   OoO00 ( ( IIii11Ii1i1I ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOoOO0oo0ooO + 'vod.png' )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOoOO0oo0ooO + 'Next.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0ooOO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOoOO0oo0ooO + 'classictoons.png' )
  if 16 - 16: I1ii11iIi11i + O0oOO0 / I1ii11iIi11i / oO0o % O0O0O % Ii1I
  if 22 - 22: IIiIiII11i * oO0o * Ii1i111I + Ii1I * I11i
def oo0o0 ( ) :
 oO0ooOoO ( 'Audio Books' , '' , 30011 , OOoOO0oo0ooO + 'AudioBooks.png' , OOoOO0oo0ooO + 'AudioBooks.png' , '' )
 oO0ooOoO ( 'Kids Audio Books' , '' , 30006 , OOoOO0oo0ooO + 'KidsAudioBooks.png' , OOoOO0oo0ooO + 'KidsAudioBooks.png' , '' )
 if 59 - 59: o0o00Oo0O % I1ii11iIi11i
def O0o00O0Oo0 ( ) :
 oO0ooOoO ( 'All' , '' , 30001 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 oO0ooOoO ( 'Popular' , '' , 30012 , OOoOO0oo0ooO + 'POPULARv.png' , OOoOO0oo0ooO + 'POPULARv.png' , '' )
 oO0ooOoO ( 'Search' , '' , 30013 , OOoOO0oo0ooO + 'Search.png' , OOoOO0oo0ooO + 'Search.png' , '' )
 if 58 - 58: o0o00Oo0O
def oO00oOOo0Oo ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for II1i11I , Ooo00OoOOO , IIi in o0O00oOoOO :
  if 'Parent' in II1i11I :
   pass
  elif '2' in IIi :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: oO0o + I11i - IIiIiII11i / iI11I1II1I1I + o0o00Oo0O
def ooO0oo ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for II1i11I , Ooo00OoOOO , IIi in o0O00oOoOO :
  if I1i111I in II1i11I . lower ( ) :
   if '1' in IIi :
    oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '2' in IIi :
    oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '3' in IIi :
    oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 56 - 56: ii - Ii1i111I - ooOoO0O00
    if 8 - 8: oO00Oo0o000 / i1IiIIIII . oOo0O0Ooo + Ii1I / Ii
def I1Iii1iI1 ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for II1i11I , Ooo00OoOOO , IIi in o0O00oOoOO :
  if '1' in IIi :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 3010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '2' in IIi :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '3' in IIi :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ooo00OoOOO , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: o0o00Oo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: IIiI1I * i1IiIIIII . OOooOOo . ooOoO0O00 . ooOoO0O00 - I11i
def ii1iIIiii1 ( url ) :
 OOoOooOoOOOoo = url
 IIiII = Iiii ( url )
 iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
 for url , II1i11I in iIIi1i1 :
  if 'mp3' in II1i11I :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OOoOooOoOOOoo + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'wma' in II1i11I :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OOoOooOoOOOoo + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in II1i11I :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OOoOooOoOOOoo + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '/' in II1i11I :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOooOoOOOoo + url , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 62 - 62: i1IiIIIII
   if 1 - 1: O00Oo000ooO0 / O00Oo000ooO0 - Ii
   if 87 - 87: I1ii11iIi11i / o0o00Oo0O * O00Oo000ooO0 / I11i
def I1iiIII ( url ) :
 IIiII = Iiii ( url )
 OOoOooOoOOOoo = url
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  if 'Parent' in II1i11I :
   pass
  elif '.db' in II1i11I :
   pass
  elif '.jpg' in II1i11I :
   pass
  elif '.html' in II1i11I :
   pass
  elif '.doc' in II1i11I :
   pass
  elif 'mp3' in II1i11I :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOooOoOOOoo + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in II1i11I :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOooOoOOOoo + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OOoOooOoOOOoo + url , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 16 - 16: O0O0O + O0oOO0 / I11i
   if 82 - 82: O00Oo000ooO0 * Ii % IIiIiII11i - ii
def OO0 ( ) :
 oO0ooOoO ( 'A-Z' , '' , 30007 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 oO0ooOoO ( 'All' , '' , 30003 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 oO0ooOoO ( 'Search' , '' , 30014 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 if 62 - 62: ooOoO0O00 / O0oOO0 . oOo0O0Ooo * I11i
def i11i1Ii1 ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I in o0O00oOoOO :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + Ooo00OoOOO + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in IIii11Ii1i1I :
   pass
  else :
   oO0ooOoO ( IIii11Ii1i1I , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( Ooo00OoOOO ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + IIii11Ii1i1I + '.gif' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 98 - 98: oO00Oo0o000
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: oO00Oo0o000 - iI11I1II1I1I
 if 32 - 32: OoOO00O % oO0o * oO0o + O00Oo000ooO0 * IIiIiII11i * OoOO00O
def iIiIii1I1II ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  if '</a>' in II1i11I :
   pass
  elif '(' in II1i11I :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 61 - 61: O00Oo000ooO0 + iI11I1II1I1I + Ii / Ii % IIiIiII11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: OoOO00O * oO00Oo0o000 . O00Oo000ooO0 * oOo0O0Ooo + OOooOOo
def i1i1II11II1 ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if I1i111I in II1i11I . lower ( ) :
   if '</a>' in II1i11I :
    pass
   elif '(' in II1i11I :
    oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ooo00OoOOO , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   else :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ooo00OoOOO , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 5 - 5: I1ii11iIi11i - Ii1I % O0O0O - IIiIiII11i . oOo0O0Ooo + IIiI1I
    if 47 - 47: o0o00Oo0O - iI11I1II1I1I - IIiI1I
def I11oOoO0o ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if '</a>' in II1i11I :
   pass
  elif '(' in II1i11I :
   oO0ooOoO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ooo00OoOOO , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ooo00OoOOO , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 46 - 46: oO00Oo0o000 % OoOO00O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: iI11I1II1I1I
 if 45 - 45: I1ii11iIi11i - I11i % oO00Oo0o000
def i1IIi1i1Ii1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OOoOooOoOOOoo )
  if 45 - 45: iI11I1II1I1I . O0O0O / OOooOOo / O00Oo000ooO0
def ooOOOoOoOOO0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , url in o0O00oOoOO :
  if '<p align' in II1i11I :
   pass
  elif '&nbsp;' in II1i11I :
   pass
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 5 - 5: i1IiIIIII
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: IIiI1I % oO00Oo0o000 / oO0o . i1IiIIIII / i1IiIIIII - Ii1I
 if 79 - 79: Ii1I + oO00Oo0o000
def iIiIIi ( ) :
 IIiII = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o0O00oOoOO = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'ongoing' in Ooo00OoOOO :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 21005 , OOoOO0oo0ooO + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in Ooo00OoOOO :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 21005 , OOoOO0oo0ooO + 'CartoonShows.png' , '' , '' )
  if 'disney' in Ooo00OoOOO :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 21005 , OOoOO0oo0ooO + 'Disney.png' , '' , '' )
  if 'genre' in Ooo00OoOOO :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 21005 , OOoOO0oo0ooO + 'Genre.png' , '' , '' )
  if 'years' in Ooo00OoOOO :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 21005 , OOoOO0oo0ooO + 'Years.png' , '' , '' )
def III1I ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 I1I111iIi = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIiII )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , IIii11Ii1i1I , IIii11Ii1i1I , II1i11I )
 for url , II1i11I in I1I111iIi :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in next :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
def OoOOOO ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 I1iiIi111I = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 Iiii1iIii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIiII )
 oOoooO000O = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in Iiii1iIii :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , 'http:' + url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url , II1i11I in I1iiIi111I :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 else :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
def III1I11i1iIi ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
  if 69 - 69: I1ii11iIi11i * IIiIiII11i * O0oOO0 . IIiI1I - Ii1I
def I11iiIIiI1ii ( ) :
 OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 12 - 12: oO00Oo0o000 % Ii + I11i + oO00Oo0o000 / Ii1i111I
def O00 ( ) :
 OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 94 - 94: Ii1i111I . Ii1i111I + Ii - i1IiIIIII * Ii1I
def iIoo0ooooO ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  if '?c=' in url :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 12 - 12: IIiIiII11i
def IiIii1ii ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIiII )
 for url , IIiI1i , II1i11I in o0O00oOoOO :
  if 'Genre' in url :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 6 - 6: Ii1I / IIiI1I - i1IiIIIII
def o00O00Oo00O ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIiI1i , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIiI1i )
  if 46 - 46: OOooOOo % ooOoO0O00 / O0O0O * I1ii11iIi11i * i1IiIIIII
def OOoOOOo0Ooo0 ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIiI1i , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIiI1i )
  if 80 - 80: OoOO00O - I11i
  if 41 - 41: I11i - I1ii11iIi11i * oOo0O0Ooo
  if 82 - 82: oO0o % I11i % i1IiIIIII / o0o00Oo0O
  if 94 - 94: Ii1I + Ii1I + ii % O0oOO0
  if 7 - 7: IIiI1I
def oOo000O ( ) :
 if 1 - 1: iI11I1II1I1I
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Cartoons[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 if 54 - 54: ii - oOo0O0Ooo % Ii1I
def oO0Ooo0OooOOo ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 71 - 71: O00Oo000ooO0 + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIiII )
 if 55 - 55: ii + oO00Oo0o000 + ii * O0oOO0
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if I1i111I in II1i11I . lower ( ) :
   if 'Dad!' in II1i11I :
    pass
   elif 'Family Guy' in II1i11I :
    pass
   elif '2 Stupid' in II1i11I :
    pass
   elif 'The Zelfs' in II1i11I :
    pass
   elif 'A Clone' in II1i11I :
    pass
   elif 'A.T.O.M' in II1i11I :
    pass
   elif 'Almost Naked' in II1i11I :
    pass
   elif 'Angry Kid' in II1i11I :
    pass
   elif 'Annoying Orange' in II1i11I :
    pass
   elif 'Aqua Teen' in II1i11I :
    pass
   elif 'Assy Mcgee' in II1i11I :
    pass
   elif 'Astroblast' in II1i11I :
    pass
   elif 'Atomic Betty' in II1i11I :
    pass
   elif 'Axe Cop' in II1i11I :
    pass
   elif 'Baby Playpen' in II1i11I :
    pass
   elif 'Beavis and Butt' in II1i11I :
    pass
   elif 'Celebrity Deathmatch' in II1i11I :
    pass
   elif 'Clerks The' in II1i11I :
    pass
   elif 'Crapston Villas' in II1i11I :
    pass
   elif 'Duckman:' in II1i11I :
    pass
   elif 'Stripperella' in II1i11I :
    pass
   elif 'Vixen' in II1i11I :
    pass
   else :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
    if 68 - 68: o0o00Oo0O
    if 2 - 2: oO0o + o0o00Oo0O * oO0o - OoOO00O + O0O0O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 43 - 43: Ii1I - OOooOOo
def iI1iIIII1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if 'Dad!' in II1i11I :
   pass
  elif 'Family Guy' in II1i11I :
   pass
  elif '2 Stupid' in II1i11I :
   pass
  elif 'The Zelfs' in II1i11I :
   pass
  elif 'A Clone' in II1i11I :
   pass
  elif 'A.T.O.M' in II1i11I :
   pass
  elif 'Almost Naked' in II1i11I :
   pass
  elif 'Angry Kid' in II1i11I :
   pass
  elif 'Annoying Orange' in II1i11I :
   pass
  elif 'Aqua Teen' in II1i11I :
   pass
  elif 'Assy Mcgee' in II1i11I :
   pass
  elif 'Astroblast' in II1i11I :
   pass
  elif 'Atomic Betty' in II1i11I :
   pass
  elif 'Axe Cop' in II1i11I :
   pass
  elif 'Baby Playpen' in II1i11I :
   pass
  elif 'Beavis and Butt' in II1i11I :
   pass
  elif 'Celebrity Deathmatch' in II1i11I :
   pass
  elif 'Clerks The' in II1i11I :
   pass
  elif 'Crapston Villas' in II1i11I :
   pass
  elif 'Duckman:' in II1i11I :
   pass
  elif 'Stripperella' in II1i11I :
   pass
  elif 'Vixen' in II1i11I :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: OOooOOo . iI11I1II1I1I % O0oOO0 % OoOO00O * OOooOOo
def II1o0ooO0OOO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I in iIIi1i1 :
  o0oo000OoOoo0 = IIii11Ii1i1I
 i1IIii1iiIi = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iIi1i1iIi1iI )
 for url in i1IIii1iiIi :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 10007 , o0oo000OoOoo0 )
  if 81 - 81: o0o00Oo0O / O00Oo000ooO0 - iI11I1II1I1I / IIiIiII11i
  if 86 - 86: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % OoOO00O
def oo0 ( url , IMAGE ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  print II1i11I + '     ' + url
  if 'easy' in url :
   i1iIIi1II1iiI ( url )
   if 31 - 31: I11i % Ii1i111I + iI11I1II1I1I + Ii * oO00Oo0o000
   if 45 - 45: i1IiIIIII * oO00Oo0o000 . O0oOO0 - oO00Oo0o000 + O00Oo000ooO0
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: i1IiIIIII . I1ii11iIi11i
def i1iIIi1II1iiI ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  OOoO0oO00o ( url )
  if 10 - 10: oO0o
  if 22 - 22: Ii / o0o00Oo0O
  if 94 - 94: O0oOO0 * Ii1i111I - O00Oo000ooO0 . iI11I1II1I1I
def O000oO0O ( ) :
 if 93 - 93: oO00Oo0o000 + OoOO00O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Stand Up[/COLOR]' , '' , 10014 , OOoOO0oo0ooO + 'StandUp.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Comedian[/COLOR]' , '' , 10015 , OOoOO0oo0ooO + 'SearchComedian.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Others[/COLOR]' , '' , 10017 , OOoOO0oo0ooO + 'Others.png' , i1iIIi1 , '' )
 if 33 - 33: o0o00Oo0O
def oo0oO ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if 'elete' in II1i11I :
   pass
  else :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 222 , IIii11Ii1i1I )
   if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % oO00Oo0o000 - iI11I1II1I1I % o0o00Oo0O
def o0oO0Oo ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0OO000 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , o0OO0O0OO0oO0 , i1iII1IiiIiI1 in OO0OO000 :
  for I1i111I in o0OO0O0OO0oO0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iIiiIi11IIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for Ooo00OoOOO , II1i11I in iIiiIi11IIi :
    if 'tube' in Ooo00OoOOO :
     pass
    elif 'stage' in Ooo00OoOOO :
     I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0OO0O0OO0oO0 + '   -   ' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIii11Ii1i1I , )
    elif 'vee' in Ooo00OoOOO :
     pass
     if 64 - 64: ii . Ii1I % o0o00Oo0O + oOo0O0Ooo - I11i
def ooo0oo00O00oO ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OO0OO000 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , o0OO0O0OO0oO0 , i1iII1IiiIiI1 in OO0OO000 :
  iIiiIi11IIi = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for Ooo00OoOOO , II1i11I in iIiiIi11IIi :
   if 'tube' in Ooo00OoOOO :
    pass
   elif 'stage' in Ooo00OoOOO :
    I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0OO0O0OO0oO0 + '   -   ' + II1i11I + '[/COLOR]' , ( Ooo00OoOOO ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + IIii11Ii1i1I )
   elif 'vee' in Ooo00OoOOO :
    pass
    if 93 - 93: iI11I1II1I1I
    if 66 - 66: Ii * iI11I1II1I1I % ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: OOooOOo % ii
def OO0I111i1I ( url ) :
 IIiII = Iiii ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0Oooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIiII )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O0Oooo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O0Oooo :
  OOoO0oO00o ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 14 - 14: OoOO00O % oOo0O0Ooo - iI11I1II1I1I . i1IiIIIII + oO0o - oO00Oo0o000
  if 5 - 5: IIiI1I
  if 62 - 62: OOooOOo . ii . i1IiIIIII . oO0o * IIiI1I
  if 78 - 78: O0O0O / oO0o - O0O0O * ii . OOooOOo
  if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
  if 37 - 37: ooOoO0O00 - i1IiIIIII % ii / i1IiIIIII % O0oOO0
  if 48 - 48: Ii % O0O0O
def i11i11 ( ) :
 if 18 - 18: iI11I1II1I1I + Ii1i111I * oOo0O0Ooo - i1IiIIIII / oOo0O0Ooo
 o00iI1i1II ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iIIi1 , '' )
 o00iI1i1II ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 14 - 14: O0oOO0 - iI11I1II1I1I / o0o00Oo0O % O00Oo000ooO0 . OOooOOo
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 18 - 18: O0O0O * O0O0O % O0O0O
def Ii1I1I1i11ii ( ) :
 o00iI1i1II ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 o00iI1i1II ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 58 - 58: iI11I1II1I1I - Ii - Ii * OoOO00O + I11i . OOooOOo
 oO00OOoO00 ( 'movies' , 'MAIN' )
def OoOo00o ( ) :
 if 30 - 30: OOooOOo . Ii1i111I / Ii1i111I * Ii
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 II1III1i1iiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 27 - 27: OoOO00O - o0o00Oo0O % Ii1i111I * oO00Oo0o000 . O00Oo000ooO0 % iI11I1II1I1I
 for IiIi1i in II1III1i1iiI :
  oO0 = OOO00 + IiIi1i + OooO0
  IIiII = i1I1iI ( oO0 )
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiII )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , o0o0oOoOO0O , II1i11I in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    O0oO ( II1i11I , Ooo00OoOOO , 222 , o00OooO0oo , o0o0oOoOO0O , OOoOOO0 )
    if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - i1IiIIIII % I11i
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 30 - 30: oO00Oo0o000 % oO00Oo0o000 % O00Oo000ooO0 . OOooOOo
    if 9 - 9: O0oOO0 / IIiIiII11i . OOooOOo % I11i * IIiIiII11i - O0oOO0
def oOOoo0 ( ) :
 if 24 - 24: oO0o - O0O0O + Ii1I / IIiI1I % oOo0O0Ooo + iI11I1II1I1I
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 II1III1i1iiI = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 79 - 79: OOooOOo / O0oOO0
 for IiIi1i in II1III1i1iiI :
  oOo00o = OOO00 + IiIi1i + OooO0
  IIiII = i1I1iI ( oOo00o )
  o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIiII )
  for II1i11I , OOoOOO0 , Ooo00OoOOO , IIii11Ii1i1I , o0o0oOoOO0O , OOoooooooO in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    o00iI1i1II ( II1i11I , Ooo00OoOOO , OOoooooooO , IIii11Ii1i1I , o0o0oOoOO0O , OOoOOO0 )
    if 4 - 4: I1ii11iIi11i + I11i
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 17 - 17: oO0o * OOooOOo
    if 15 - 15: Ii / O0oOO0 % oOo0O0Ooo
def o00Oo ( ) :
 if 57 - 57: i1IiIIIII + oO00Oo0o000 % Ii1I . oO0o / oO0o * o0o00Oo0O
 iIi1i1iIi1iI = Iiii ( OOO00 + 'spongemain.php' )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , OOoOOO0 , Ooo00OoOOO , IIii11Ii1i1I , o0o0oOoOO0O , OOoooooooO in o0O00oOoOO :
  o00iI1i1II ( II1i11I , Ooo00OoOOO , OOoooooooO , IIii11Ii1i1I , o0o0oOoOO0O , OOoOOO0 )
  oO00OOoO00 ( 'movies' , 'MAIN' )
def Ii1iiII1i ( url ) :
 if 52 - 52: O0O0O / oO00Oo0o000
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0Oi11i1I = ( '%s%s' % ( O00O0 , url ) )
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , o00OooO0oo , OOoOOO0 , IiI , II1i11I in o0O00oOoOO :
  O0o0OO00 = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
  for iIi11i in O0o0OO00 :
   if iIi11i == url :
    II1i11I = ( '[COLORred]Watched - [/COLOR]' + II1i11I ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  O0oO ( II1i11I , url , 222 , o00OooO0oo , IiI , OOoOOO0 )
  if 56 - 56: Ii . O0oOO0 / IIiI1I
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 48 - 48: oO0o * i1IiIIIII + iI11I1II1I1I / IIiIiII11i
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: Ii1i111I
  if 59 - 59: O0O0O * i1IiIIIII + I11i . Ii1I
def ooooO ( url ) :
 if 92 - 92: I11i / I11i * OoOO00O
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , OOoOOO0 , url , IIii11Ii1i1I , o0o0oOoOO0O , OOoooooooO in o0O00oOoOO :
  o00iI1i1II ( II1i11I , url , OOoooooooO , IIii11Ii1i1I , o0o0oOoOO0O , OOoOOO0 )
  if 19 - 19: OoOO00O
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 55 - 55: i1IiIIIII % i1IiIIIII / o0o00Oo0O % IIiI1I - I11i . I1ii11iIi11i
  if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
def O0oO ( name , url , mode , iconimage , fanart , description ) :
 if 8 - 8: OOooOOo * I1ii11iIi11i / O00Oo000ooO0 % OoOO00O - oOo0O0Ooo
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = False )
 return Oo
 if 95 - 95: ii + Ii1i111I - Ii1I / Ii1I . ooOoO0O00 . ii
def o00iI1i1II ( name , url , mode , iconimage , fanart , description ) :
 if 29 - 29: O0oOO0 - ooOoO0O00 . Ii1i111I - Ii1I + O0oOO0 + ii
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
if 36 - 36: ooOoO0O00 / O0oOO0 . iI11I1II1I1I
if 12 - 12: OoOO00O
if 71 - 71: oOo0O0Ooo . IIiIiII11i . oOo0O0Ooo - O0oOO0
if 45 - 45: O00Oo000ooO0 / o0o00Oo0O / OOooOOo * i1IiIIIII
if 18 - 18: iI11I1II1I1I + i1IiIIIII + iI11I1II1I1I . Ii1I + oO00Oo0o000 . O0oOO0
if 7 - 7: Ii1I + iI11I1II1I1I * Ii1i111I * Ii1i111I / IIiIiII11i - OoOO00O
if 65 - 65: O0O0O + OOooOOo + IIiIiII11i
if 77 - 77: IIiIiII11i
if 50 - 50: o0o00Oo0O . o0o00Oo0O . O0oOO0 % I1ii11iIi11i
if 68 - 68: O0O0O
if 10 - 10: OoOO00O
if 77 - 77: i1IiIIIII / IIiIiII11i + O00Oo000ooO0 + O0oOO0 - Ii
if 44 - 44: oOo0O0Ooo + OOooOOo + Ii1I . oOo0O0Ooo * OOooOOo % iI11I1II1I1I
if 72 - 72: i1IiIIIII . i1IiIIIII - Ii1I
if 48 - 48: I1ii11iIi11i - O0oOO0 + I1ii11iIi11i - oOo0O0Ooo * Ii . IIiI1I
def I1iIIIiI ( string ) :
 if IIIii1II1II == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 60 - 60: oOo0O0Ooo . Ii + OOooOOo / Ii1I * IIiIiII11i * i1IiIIIII
def OOO0o0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 IIIIII111Ii = [ ]
 try :
  if 5 - 5: ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * o0o00Oo0O + OOooOOo % ooOoO0O00
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  I1iIIIiI ( 'Making Favorites File' )
  IIIIII111Ii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ii1 = open ( iIi1ii1I1 , "w" )
  ii1 . write ( json . dumps ( IIIIII111Ii ) )
  ii1 . close ( )
 else :
  I1iIIIiI ( 'Appending Favorites' )
  ii1 = open ( iIi1ii1I1 ) . read ( )
  O0OOo = json . loads ( ii1 )
  O0OOo . append ( ( name , url , iconimage , fanart , mode ) )
  i1i11I = open ( iIi1ii1I1 , "w" )
  i1i11I . write ( json . dumps ( O0OOo ) )
  i1i11I . close ( )
  if 41 - 41: OoOO00O + Ii / O00Oo000ooO0 % Ii1I
  if 22 - 22: OOooOOo % I11i * OoOO00O - Ii1I + I11i - I1ii11iIi11i
def iiIi1iiI1I ( ) :
 if os . path . exists ( iIi1ii1I1 ) == False :
  IIIIII111Ii = [ ]
  I1iIIIiI ( 'Making Favorites File' )
  IIIIII111Ii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ii1 = open ( iIi1ii1I1 , "w" )
  ii1 . write ( json . dumps ( IIIIII111Ii ) )
  ii1 . close ( )
 else :
  Iiii1I = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
  ooooo0Oo0 = len ( Iiii1I )
  for o0I1IIIi11ii11 in Iiii1I :
   II1i11I = o0I1IIIi11ii11 [ 0 ]
   Ooo00OoOOO = o0I1IIIi11ii11 [ 1 ]
   o00OooO0oo = o0I1IIIi11ii11 [ 2 ]
   try :
    O0o0oo0oOO0oO = o0I1IIIi11ii11 [ 3 ]
    if O0o0oo0oOO0oO == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     O0o0oo0oOO0oO = o00OooO0oo
    else :
     O0o0oo0oOO0oO = o0o0oOoOO0O
   try : iIiIII1iI1111 = o0I1IIIi11ii11 [ 5 ]
   except : iIiIII1iI1111 = None
   try : Ii1I1I111iI = o0I1IIIi11ii11 [ 6 ]
   except : Ii1I1I111iI = None
   if 31 - 31: IIiI1I + O00Oo000ooO0 . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
   if o0I1IIIi11ii11 [ 4 ] == 0 :
    o0OOOO00O0Oo ( II1i11I , Ooo00OoOOO , '' , o00OooO0oo , o0o0oOoOO0O , '' , 'fav' )
   else :
    o0OOOO00O0Oo ( II1i11I , Ooo00OoOOO , o0I1IIIi11ii11 [ 4 ] , o00OooO0oo , o0o0oOoOO0O , '' , 'fav' )
    if 83 - 83: O00Oo000ooO0 / oO00Oo0o000
def OOo000OO000 ( name ) :
 O0OOo = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for OOOO00OooO in range ( len ( O0OOo ) ) :
  if O0OOo [ OOOO00OooO ] [ 0 ] == name :
   del O0OOo [ OOOO00OooO ]
   i1i11I = open ( iIi1ii1I1 , "w" )
   i1i11I . write ( json . dumps ( O0OOo ) )
   i1i11I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 64 - 64: oO0o . oOo0O0Ooo - ii . O0oOO0 - IIiI1I
 if 77 - 77: OoOO00O % OOooOOo / IIiIiII11i % IIiI1I % ii % oO0o
def oO0oo ( ) :
 I1i11II11i1iI = os . path . join ( o0 )
 iI1 = open ( I1i11II11i1iI , "w+" )
 if 12 - 12: oO00Oo0o000 + i1IiIIIII + Ii1i111I . O00Oo000ooO0 / OoOO00O
 iI1 . write ( r'# This file contains the "built-in" channels' + '\n' )
 iI1 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 iI1 . write ( r'[plugin.video.gtv]' + '\n' )
 iI1 . write ( r'BBC One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F191.m3u8&mode=3&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BBC Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F190.m3u8&mode=3&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BBC Four=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F188.m3u8&mode=3&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'ITV=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F208.m3u8&mode=3&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'ITV2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F207.m3u8&mode=3&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'ITV3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F206.m3u8&mode=3&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'ITV4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F205.m3u8&mode=3&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Channel 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F183.m3u8&mode=3&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Channel 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F185.m3u8&mode=3&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'5STAR=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F187.m3u8&mode=3&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'5 USA=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F186.m3u8&mode=3&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'RTE One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F194.m3u8&mode=3&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'RTE Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F193.m3u8&mode=3&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'TG4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F192.m3u8&mode=3&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F32.m3u8&mode=3&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F33.m3u8&mode=3&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Living=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F35.m3u8&mode=3&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Atlantic=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F34.m3u8&mode=3&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Dave=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F325.m3u8&mode=3&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Pick=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F324.m3u8&mode=3&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'GOLD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F326.m3u8&mode=3&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Watch HD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F518.m3u8&mode=3&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'YESTERDAY=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F377.m3u8&mode=3&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Comedy Central=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F181.m3u8&mode=3&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'London Live=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F830.m3u8&mode=3&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Disney Junior=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F230.m3u8&mode=3&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Disney Chnl=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F231.m3u8&mode=3&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Animal Planet=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F198.m3u8&mode=3&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Nat Geo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F197.m3u8&mode=3&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Discovery=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F200.m3u8&mode=3&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Discovery Science=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F199.m3u8&mode=3&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Disc.Turbo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F168.m3u8&mode=3&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Food Network=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F639.m3u8&mode=3&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'MTV MUSIC=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F234.m3u8&mode=3&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Film4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F182.m3u8&mode=3&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'True Movies=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F853.m3u8&mode=3&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'True Movies 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F852.m3u8&mode=3&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Action=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F732.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky ScFiHorror=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F511.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'SkyPremiereHD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F516.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Greats=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F512.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Family=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F509.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky DramaRom=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F510.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Thriller=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F514.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Comedy=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F1022.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Showcase=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F46.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Select=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F45.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Disney=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F195.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F18.m3u8&mode=3&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F19.m3u8&mode=3&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports 3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F20.m3u8&mode=3&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F21.m3u8&mode=3&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F22.m3u8&mode=3&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports F1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F24.m3u8&mode=3&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Sky Sports News=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F23.m3u8&mode=3&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BT Sport 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F309.m3u8&mode=3&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BT Sport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F26.m3u8&mode=3&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BT Sport Europe=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F705.m3u8&mode=3&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BT Sport ESPN=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F28.m3u8&mode=3&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'BoxNation=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F173.m3u8&mode=3&name=[COLORgreen]Box+Nation+UK%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'WWENetwork=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F178.m3u8&mode=3&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Eurosport=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F269.m3u8&mode=3&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Eurosport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F748.m3u8&mode=3&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'At The Races=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F170.m3u8&mode=3&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Racing UK=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F171.m3u8&mode=3&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 iI1 . write ( r'Poker central US=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F826.m3u8&mode=3&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 29 - 29: O00Oo000ooO0 . O0oOO0 - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / O0O0O
def oOooo00000 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  OOooOoooOoOo ( II1i11I , ( Ooo00OoOOO ) . strip ( ) , 222 , OOoOO0oo0ooO + '247.png' , OOoOO0oo0ooO + '247.png' , '' )
def iiI11I1iiIiII1I ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  OOooOoooOoOo ( II1i11I , ( Ooo00OoOOO ) . strip ( ) , 222 , OOoOO0oo0ooO + 'musicch.png' , OOoOO0oo0ooO + 'musicch.png' , '' )
def o00ooOoo ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  OOooOoooOoOo ( II1i11I , ( Ooo00OoOOO ) . strip ( ) , 222 , OOoOO0oo0ooO + 'NEWS.png' , OOoOO0oo0ooO + 'NEWS.png' , '' )
def i111i1I1ii1i ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  OOooOoooOoOo ( II1i11I , ( Ooo00OoOOO ) . strip ( ) , 222 , OOoOO0oo0ooO + 'adult.png' , OOoOO0oo0ooO + 'adult.png' , '' )
def O0OoooI11iI1I ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o0O00oOoOO = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OOooOoooOoOo ( II1i11I , Ooo00OoOOO , 1016 , OOoOO0oo0ooO + 'TUTS.png' , OOoOO0oo0ooO + 'TUTS.png' , '' )
  if 50 - 50: iI11I1II1I1I * O00Oo000ooO0 . ii / IIiIiII11i - Ii1I * Ii1I
  if 98 - 98: oO0o - OoOO00O . O00Oo000ooO0 % Ii
def OO00oo ( ) :
 if 84 - 84: O0oOO0 + Ii - i1IiIIIII * O0oOO0
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Recent Episodes[/COLOR]' , '' , 10019 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , '' , 10020 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search[/COLOR]' , '' , 10021 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 if 33 - 33: O0oOO0 % ooOoO0O00 - O0O0O . o0o00Oo0O / o0o00Oo0O
def oo00o0 ( ) :
 if 17 - 17: OoOO00O / iI11I1II1I1I - oO0o + oOo0O0Ooo % i1IiIIIII
 iIi1i1iIi1iI = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I , OOooO0o0 in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I + '  -  ' + ( OOooO0o0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ooo00OoOOO , 10023 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 14 - 14: I11i % O00Oo000ooO0 + Ii1I + oO0o
  if 76 - 76: oO0o - Ii + OOooOOo + i1IiIIIII / ii
  if 50 - 50: IIiIiII11i - oO00Oo0o000 + iI11I1II1I1I + iI11I1II1I1I
def OoooooOo ( ) :
 if 67 - 67: IIiIiII11i / I11i . i1IiIIIII . ii
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Action[/COLOR]' , 'Aksiyon' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Adventure[/COLOR]' , 'Macera' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Animation[/COLOR]' , 'Animasyon' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Anime[/COLOR]' , 'Anime' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Biography[/COLOR]' , 'Biyografi' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Comedy[/COLOR]' , 'Komedi' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Drama[/COLOR]' , 'Dram' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Family[/COLOR]' , 'Aile' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']History[/COLOR]' , 'Tarih' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Horror[/COLOR]' , 'Korku' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Mystery[/COLOR]' , 'Gizem' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Romance[/COLOR]' , 'Romantik' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Sport[/COLOR]' , 'Spor' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Western[/COLOR]' , 'Tarih' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 if 19 - 19: O00Oo000ooO0 . Ii1I / OOooOOo
def O00oo ( url ) :
 IiI11ii1I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIiII = cloudflare . source ( IiI11ii1I )
 o0O00oOoOO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 10022 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
  if 70 - 70: O0O0O * O0O0O + I1ii11iIi11i * i1IiIIIII % oOo0O0Ooo + iI11I1II1I1I
  if 2 - 2: Ii
  if 98 - 98: O0O0O / oO0o - OoOO00O - oOo0O0Ooo / OOooOOo + Ii
def i1I1IiI1ii ( ) :
 if 64 - 64: IIiI1I * Ii1I % IIiIiII11i - OOooOOo + Ii1I
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1i111I ) . replace ( ' ' , '+' )
 IIiII = cloudflare . source ( Ooo00OoOOO )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if I1i111I in II1i11I . lower ( ) :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 10022 , OOoOO0oo0ooO + 'dtv.png' )
   if 62 - 62: OOooOOo % I11i % oOo0O0Ooo + O00Oo000ooO0 . oO0o
   if 48 - 48: oOo0O0Ooo * Ii % IIiIiII11i
   if 20 - 20: ooOoO0O00 / oOo0O0Ooo * O0O0O
def Oo0O0000Oo00o ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for OOoOooOoOOOoo , II1ii , o00iIiiiII , II1i11I in o0O00oOoOO :
  Ii1I1 = ( o00iIiiiII ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OO0ooO0 = ( II1ii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OoOooOO0oOOo0O = 'Season ' + OO0ooO0 + 'Episode ' + Ii1I1 + II1i11I
  I1II ( OoOooOO0oOOo0O , OOoOooOoOOOoo )
  if 9 - 9: I1ii11iIi11i % ii - OoOO00O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 43 - 43: oO0o % oO0o
  if 46 - 46: I1ii11iIi11i % iI11I1II1I1I . IIiI1I . o0o00Oo0O * O0oOO0 / ii
def I1II ( name , url ) :
 OOoOooOoOOOoo = url
 II1iI1IIi = name
 o0ooOooo000oOO = cloudflare . source ( OOoOooOoOOOoo )
 iIIi1i1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o0ooOooo000oOO )
 for O0Oooo , Ii11iiI1 in iIIi1i1 :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1iI1IIi + Ii11iiI1 + '[/COLOR]' , O0Oooo , 10012 , OOoOO0oo0ooO + 'dtv.png' )
  if 71 - 71: I11i / i1IiIIIII % i1IiIIIII
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: ii + Ii / Ii1i111I + iI11I1II1I1I % O0oOO0
 if 29 - 29: Ii1I
def Oo0o00ooOOOoOo ( ) :
 if 30 - 30: O0oOO0 + O0oOO0 % O00Oo000ooO0 - I11i - Ii1I
 if 36 - 36: Ii1i111I % i1IiIIIII
 if 72 - 72: oOo0O0Ooo / IIiI1I - o0o00Oo0O + Ii1i111I
 if 83 - 83: o0o00Oo0O
 if 89 - 89: I1ii11iIi11i + Ii1I - I11i
 if 40 - 40: oO0o + oO0o
 if 94 - 94: IIiI1I * iI11I1II1I1I . Ii1i111I
 if 13 - 13: iI11I1II1I1I * OOooOOo / oO00Oo0o000 % O0oOO0 + O0O0O
 if 41 - 41: Ii1I
 if 5 - 5: I1ii11iIi11i
 if 100 - 100: OoOO00O + iI11I1II1I1I
 if 59 - 59: O00Oo000ooO0
 if 89 - 89: OOooOOo % iI11I1II1I1I
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Program[/COLOR]' , '' , 10043 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 if 35 - 35: Ii1I + oO00Oo0o000 - OOooOOo % O0O0O % I11i % OOooOOo
 if 45 - 45: oOo0O0Ooo * i1IiIIIII % oO0o
def i111I11I ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 o0O00oOoOO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iiIII1i ) )
 for url , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
def I1iI11I ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 81 - 81: Ii + Ii * oO0o + O00Oo000ooO0
def iii ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 15 - 15: oOo0O0Ooo . oO0o
  if 17 - 17: Ii / I1ii11iIi11i . oO0o / oOo0O0Ooo
def Ii1 ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOooOOOOo0o = 'http://www.watchseries.ac/search/' + I1i111I . replace ( ' ' , '%20' )
 IIiII = Iiii ( oOooOOOOo0o )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'watch online' in II1i11I :
   pass
  else :
   print Ooo00OoOOO
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.watchseries.ac' + Ooo00OoOOO , 10044 , IIii11Ii1i1I , '' , '' )
   if 97 - 97: Ii1I / oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - O0oOO0
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 38 - 38: I11i % oO00Oo0o000 + Ii + IIiI1I + O0oOO0 / Ii
def o0OOOOOo0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I , o00iIiiiII , OOoOOO0 in o0O00oOoOO :
  oooOoO = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( o00iIiiiII ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oooOoO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , IIii11Ii1i1I , '' , OOoOOO0 )
  if 62 - 62: i1IiIIIII / IIiIiII11i + OOooOOo % O0oOO0 / OOooOOo + Ii1I
def IiI11I111 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  oooOoO = ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oooOoO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 54 - 54: o0o00Oo0O - IIiI1I . i1IiIIIII % IIiI1I + IIiI1I
def i1iI1Iiii1I ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , IIii11Ii1i1I , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 9 - 9: Ii1i111I / OOooOOo / IIiIiII11i + oO00Oo0o000
def o0O0oOO0Oooo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIiII )
 iiIII1i = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 for II1ii , OO0OO000 in iiIII1i :
  o0O00oOoOO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OO0OO000 ) )
  for url , II1i11I in o0O00oOoOO :
   oooOoO = ( II1ii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oooOoO + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , url in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: I11i / ii % O0oOO0 % i1IiIIIII
class oO0O0o0O ( ) :
 if 100 - 100: OOooOOo % I1ii11iIi11i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 76 - 76: IIiIiII11i / oO0o + ii . Ii1I . Ii1i111I . O0oOO0
  oooOoO = name
  self . Get_Sources ( Ooo00OoOOO , oooOoO )
  if 43 - 43: ooOoO0O00
  if 17 - 17: o0o00Oo0O - OOooOOo
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  IIiII = Iiii ( URL )
  o0O00oOoOO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIiII )
  for Ooo00OoOOO , II1i11I in o0O00oOoOO :
   URL = 'http://www.watchseries.ac/link/' + Ooo00OoOOO
   self . Get_site_link ( URL , season_name )
   if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 def Get_site_link ( self , url , season_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( IIiII )
  iIIi1i1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( IIiII )
  i1IIii1iiIi = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( IIiII )
  for url in o0O00oOoOO :
   self . main ( url , season_name )
  for url in iIIi1i1 :
   self . main ( url , season_name )
  for url in i1IIii1iiIi :
   self . main ( url , season_name )
   if 34 - 34: OoOO00O * OoOO00O - Ii1I - o0o00Oo0O . Ii
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IioOo0O = 'DACLIPS'
   if IioOo0O in oO0O0o0O . source_list :
    pass
   else :
    self . daclips ( url , season_name , IioOo0O )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    IioOo0O = 'FILEHOOT'
    if IioOo0O in oO0O0o0O . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , IioOo0O )
   else :
    if 'thevideo.me' in url :
     IioOo0O = 'THEVIDEO'
     if IioOo0O in oO0O0o0O . source_list :
      pass
     else :
      self . thevideo ( url , season_name , IioOo0O )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      IioOo0O = 'ALLMYVIDEOS'
      if IioOo0O in oO0O0o0O . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , IioOo0O )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       IioOo0O = 'VIDSPOT'
       if IioOo0O in oO0O0o0O . source_list :
        pass
       else :
        self . vidspot ( url , season_name , IioOo0O )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        IioOo0O = 'VODLOCKER'
        if IioOo0O in oO0O0o0O . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , IioOo0O )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 30 - 30: OoOO00O . Ii1I / i1IiIIIII
         if 2 - 2: O00Oo000ooO0 % oOo0O0Ooo - oO00Oo0o000
 def allmyvid ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIiII )
  for oooOo , II1i11I in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 79 - 79: O0O0O - IIiIiII11i
 def vidspot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( IIiII )
  for oooOo , II1i11I in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / OoOO00O * oOo0O0Ooo
 def thevideo ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIiII )
  for oooOo in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
 def vodlocker ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for oooOo in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 84 - 84: ii + oO00Oo0o000 / oOo0O0Ooo % i1IiIIIII % Ii1I * oOo0O0Ooo
 def daclips ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( IIiII )
  for oooOo in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / O0O0O
 def filehoot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for oooOo in o0O00oOoOO :
   self . Printer ( oooOo , season_name , source_name )
   if 24 - 24: oOo0O0Ooo * ooOoO0O00 % O0oOO0 / o0o00Oo0O + Ii
 def Printer ( self , Link , season_name , source_name ) :
  if 12 - 12: Ii1I / OoOO00O
  if Link in oO0O0o0O . List :
   pass
  elif source_name in oO0O0o0O . source_list :
   pass
  else :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + source_name + '[/COLOR]' , Link , 10012 , OOoOO0oo0ooO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   oO0O0o0O . List . append ( Link )
   oO0O0o0O . source_list . append ( source_name )
   if 5 - 5: ii
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 18 - 18: oOo0O0Ooo % ii - IIiI1I . Ii * I1ii11iIi11i % OoOO00O
   if 12 - 12: ooOoO0O00 / i1IiIIIII % O0oOO0 * O00Oo000ooO0 * o0o00Oo0O * iI11I1II1I1I
   if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * O0O0O . ii
   if 54 - 54: o0o00Oo0O / O00Oo000ooO0 % O0oOO0 * ooOoO0O00 * o0o00Oo0O
   if 48 - 48: I11i . O0O0O % OOooOOo - OOooOOo
def i1IiI1Iiii ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Highlights[/COLOR]' , '' , 10008 , OOoOO0oo0ooO + 'Highlights.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Fixtures[/COLOR]' , '' , 10009 , OOoOO0oo0ooO + 'Fixtures.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Today On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'Fixtures.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , OOoOO0oo0ooO + 'Fixtures.png' , i1iIIi1 , '' )
 if 87 - 87: O00Oo000ooO0 / oO00Oo0o000 - I1ii11iIi11i
def oOOoOOO0oOoo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for o0O0ooooooo00 , url , I1111ii11IIII , IiIi1II111I , I1iIiIi11i11 , o0o0 , o00oIIi1i1 , OOO , ii1 , o0O0Ooo , O0o in o0O00oOoOO :
  if 'Arsenal' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'arsenal-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Bournemouth' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'afc-bournemouth.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Burnley' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'KEGnQWW.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Chelsea' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'chelsea.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Crystal' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'CrystalPalace.0.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Everton' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'Everton.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Hull' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'hull-city-afc.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Leicester' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'leicester-city-fc-hd-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Liverpool' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'liverpool-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Manchester City' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'city-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Manchester United' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + '91.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Middlesborough' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'middlesbrough-fc-hd-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Southampton' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'southampton-fc-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Stoke City' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'stoke-city.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Sunderland' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'sunderland-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Swansea' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'swansea-city-afc.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Tottenham' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'tottenham-hotspur_zps4e3ed7c1.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Watford' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'watford-fc-hd-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'Bromwich' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'west-bromwich-albion-logo.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
  if 'West Ham' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'west-ham.png'
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '[/COLOR]' , url , 10010 , IiIi , IiIi , 'PL = ' + IiIi1II111I + ' - ' + 'W = ' + I1iIiIi11i11 + ' - ' + 'D = ' + o0o0 + ' - ' + 'L = ' + o00oIIi1i1 + ' - ' + 'F = ' + OOO + ' - ' + 'A = ' + ii1 + ' - ' + 'Pts = ' + o0O0Ooo + ' - ' + 'Diff = ' + O0o + ' - ' )
 oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if 63 - 63: O00Oo000ooO0 - ooOoO0O00 * I11i + ii
def I1iiIi1 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o0O00oOoOO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ooo00OoOOO , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIii11Ii1i1I , i1iIIi1 , '' )
  if 49 - 49: O0oOO0 . IIiIiII11i
def IioOooOOo00ooO ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIiII )
 for iiIII1i in iiIII1i :
  o0OO0oooo = re . compile ( '(.*?)</h2>' ) . findall ( str ( iiIII1i ) )
  for I11II1i1 in o0OO0oooo :
   I11II1i1 = I11II1i1
  IiI1ii11I1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iiIII1i ) )
  for I1i1iI , IIii11Ii1i1I , time , I1iI1I1ii1 in IiI1ii11I1 :
   IIII1iII = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1iI1I1ii1 )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + I11II1i1 + ' - ' + I1i1iI + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IIii11Ii1i1I , i1iIIi1 , ( str ( IIII1iII ) ) )
   if 33 - 33: I11i / o0o00Oo0O + i1IiIIIII
 oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if 75 - 75: O00Oo000ooO0 % Ii + iI11I1II1I1I
def oOoOo0o00o ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , OOoOO0oo0ooO + 'fanart.jpg' , '' )
 if 2 - 2: IIiIiII11i
def o0ooo0o0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width="218" height="150" class="entry-thumb" src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  O00Oooo00 = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + O00Oooo00 + '[/COLOR]' , url , 10013 , IIii11Ii1i1I )
 for url , II1i11I , IIii11Ii1i1I in iIIi1i1 :
  O00Oooo00 = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + O00Oooo00 + '[/COLOR]' , url , 10013 , IIii11Ii1i1I )
  if 93 - 93: o0o00Oo0O / O0oOO0 + oOo0O0Ooo
def I111 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( IIiII )
 for O0Oooo in o0O00oOoOO :
  iiiIii = ( O0Oooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOoO0oO00o ( 'http:' + iiiIii )
  if 55 - 55: ooOoO0O00 . ii + oOo0O0Ooo + OOooOOo + IIiI1I . O0O0O
  if 37 - 37: ooOoO0O00
def IiI11i1I11111 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 8046 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , OOoOO0oo0ooO + 'Next.png' )
def Ii1IIIIIIiI1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OOoO0oO00o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 24 - 24: oOo0O0Ooo * OoOO00O % o0o00Oo0O - I1ii11iIi11i
def ii1I ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 95 - 95: IIiIiII11i / OoOO00O - O0oOO0 - IIiIiII11i - Ii
def oO0O ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 25 - 25: O0O0O % oOo0O0Ooo + Ii + o0o00Oo0O * ii
 o0O00oOoOO = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 if 64 - 64: ooOoO0O00
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 8041 , OOoOO0oo0ooO + 'documentary.png' )
  if 10 - 10: oO00Oo0o000 % o0o00Oo0O / oOo0O0Ooo % Ii1i111I
  if 25 - 25: IIiIiII11i / oO0o
  if 64 - 64: o0o00Oo0O % O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1111i ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , IIii11Ii1i1I )
 for II1i11I , url , IIii11Ii1i1I in iIIi1i1 :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , IIii11Ii1i1I )
 for url in next :
  OoO00 ( 'NEXT PAGE' , url , 8041 , OOoOO0oo0ooO + 'Next.png' )
  if 39 - 39: oO00Oo0o000 % ii - IIiIiII11i % OOooOOo + O0O0O + o0o00Oo0O
  if 14 - 14: ii . I11i . Ii1i111I
def I1IIIIIi1IIiI ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , IIii11Ii1i1I , url , IIiI1i in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  III11I11ii ( ( url ) . replace ( '//' , 'http://' ) )
  if 82 - 82: i1IiIIIII % IIiIiII11i - i1IiIIIII + IIiIiII11i
def III11I11ii ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1IIiI ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoOO0oo0ooO + 'documentary.png' )
  if 61 - 61: Ii * O0O0O % I1ii11iIi11i * oO00Oo0o000 - ii - oO0o
def o0OOo ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT' , url , 8048 , OOoOO0oo0ooO + 'Next.png' )
def IiI1Ii11Ii ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in iIIi1i1 :
  if 'rtd' in url :
   OoO0oO0oo0O ( url )
   if 82 - 82: ii . OoOO00O
def OoO0oO0oo0O ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIi1i1iIi1iI )
 for O00oO , file in o0O00oOoOO :
  url = ( 'https://rtd.rt.com' + O00oO + file )
  OOoO0oO00o ( url )
  if 26 - 26: O0O0O + O00Oo000ooO0 - IIiIiII11i . IIiIiII11i + Ii1I + OOooOOo
  if 68 - 68: o0o00Oo0O
def o0oOoO00 ( ) :
 IIiII = iiIi1iI1iIii ( 'http://www.stream2watch.co/live-tv' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I , oOO000 in o0O00oOoOO :
  OoO00 ( ( II1i11I + '[COLOR' + oO0o0o0ooO0oO + ']' + oOO000 + '[/COLOR]' ) , Ooo00OoOOO , 8086 , IIii11Ii1i1I )
  if 95 - 95: o0o00Oo0O + oOo0O0Ooo + OOooOOo . i1IiIIIII
def OO0IIIIIIi111i ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 8087 , IIii11Ii1i1I )
  if 37 - 37: IIiI1I
def iIIiI1111 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  OooOO ( url , II1i11I )
  if 86 - 86: OoOO00O . i1IiIIIII / O00Oo000ooO0 - ii
def OooOO ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIiII )
 for url in o0O00oOoOO :
  print url
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 45 - 45: i1IiIIIII
def iIiI1i111ii ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Ooo00OoOOO , 3002 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def IiIo000OOO00O ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def O0oooo000oO0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 OoOoO00OOoOOOo0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url , II1i11I in OoOoO00OOoOOOo0 :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + II1i11I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url in next :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'Next.png' )
 for url , IIii11Ii1i1I , II1i11I in iIIi1i1 :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def oOoO00O ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I11I1I1i1i ( url )
def I11I1I1i1i ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  OOoO0oO00o ( url )
  if 74 - 74: o0o00Oo0O % ii * I1ii11iIi11i + i1IiIIIII * IIiI1I
def O000OO ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ooo00OoOOO , 8065 , OOoOO0oo0ooO + 'classicmovies.png' )
def I1Ii ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "v.src = '([^']*)';" ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  Iiii1iI1i ( url )
  if 76 - 76: IIiI1I % OOooOOo % iI11I1II1I1I . i1IiIIIII
def i11i ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ooo00OoOOO , 8065 , OOoOO0oo0ooO + 'classictv.png' )
def O0o0O00o0o ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  if 'mp4' in url :
   OOoO0oO00o ( url )
 for url in iIIi1i1 :
  yt . PlayVideo ( url )
  if 6 - 6: Ii1I - O0O0O * Ii + OOooOOo / O0oOO0 % i1IiIIIII
def II11IiIIiiI ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Ooo00OoOOO , 8071 , OOoOO0oo0ooO + 'streams.png' )
def OO ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , url in o0O00oOoOO :
  if '(Free Access)' in II1i11I :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , OOoOO0oo0ooO + 'streams.png' )
def o0oOOOOoo0 ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , II1i11I , url in o0O00oOoOO :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IIii11Ii1i1I , o0o0oOoOO0O , '' )
  if 80 - 80: Ii % Ii1I
def OOO00o0 ( ) :
 oO0ooOoO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Genres' , 'http://www.xvideos.com' , 10106 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Search' , '' , 10107 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' , )
 if 97 - 97: Ii1I / Ii1I / iI11I1II1I1I % ooOoO0O00 . Ii1I . O00Oo000ooO0
def IIII1ii1 ( url ) :
 IIiII = Iiii ( url )
 OOO0O0OOo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in OOO0O0OOo :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIiII )
 for url , II1i11I , ii1I1IIii11 in o0O00oOoOO :
  oO0ooOoO ( ( II1i11I + ' - No of Videos : ' + ( ii1I1IIii11 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 10 - 10: ii / IIiI1I / O0O0O * I1ii11iIi11i / iI11I1II1I1I
def oO0Oo ( url ) :
 IIiII = Iiii ( url )
 OOO0O0OOo = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIiII )
 for url in OOO0O0OOo :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I , iIi111iII1 in o0O00oOoOO :
  oO0ooOoO ( II1i11I + '--' + iIi111iII1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IIii11Ii1i1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 61 - 61: O0oOO0 . Ii + O0O0O
  if 8 - 8: iI11I1II1I1I
def oOOo0ooO0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I , Oo0OO0000oooo , ii1i1II11II1i in o0O00oOoOO :
  oO0ooOoO ( II1i11I + ' - Porn Quality : ' + ii1i1II11II1i + ' - ' + Oo0OO0000oooo , 'http://www.xvideos.com' + url , 10108 , IIii11Ii1i1I , IIii11Ii1i1I , ii1i1II11II1i + ' - ' + Oo0OO0000oooo )
 o00OO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for url in o00OO0 :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 48 - 48: Ii
def oO0I1iI1i11IiI11 ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 OOO0O0OOo = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in OOO0O0OOo :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iiIII1i ) )
 for url , II1i11I in o0O00oOoOO :
  oO0ooOoO ( II1i11I , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 82 - 82: oO00Oo0o000 * oO0o
  if 32 - 32: o0o00Oo0O
def Oo0o0OO0OO000OO ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00o0000OO = ( I1i111I ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 I1i11 = O00o0000OO . lower ( )
 O0Ooo0O0OO = 'http://www.xvideos.com/?k=' + I1i11
 print O0Ooo0O0OO + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIiII = Iiii ( O0Ooo0O0OO )
 o0O00oOoOO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , Ooo00OoOOO , II1i11I , Oo0OO0000oooo , ii1i1II11II1i in o0O00oOoOO :
  oO0ooOoO ( II1i11I + ' - Porn Quality : ' + ii1i1II11II1i + ' - ' + Oo0OO0000oooo , 'http://www.xvideos.com' + Ooo00OoOOO , 10108 , IIii11Ii1i1I , IIii11Ii1i1I , ii1i1II11II1i + ' - ' + Oo0OO0000oooo )
 o00OO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for Ooo00OoOOO in o00OO0 :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Ooo00OoOOO , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 38 - 38: oO00Oo0o000
def Iiiii1Iii1I ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIiII )
 iIIi1i1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIiII )
 i1IIii1iiIi = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'http' in url :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']LOW[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in iIIi1i1 :
  if 'http' in url :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']HIGH[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in i1IIii1iiIi :
  if 'http' in url :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']HLS[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
   if 83 - 83: OOooOOo
def oOoOo0 ( url ) :
 I1iiIi111I = xbmc . Player ( iIi ( ) )
 import urlresolver
 try : I1iiIi111I . play ( url )
 except : pass
 if 52 - 52: iI11I1II1I1I
 if 49 - 49: i1IiIIIII
def iIi1i ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 o0O00oOoOO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + Ooo00OoOOO ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , OOoOO0oo0ooO + 'gofish.png' )
def III ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , OOoOO0oo0ooO + 'gofish.png' )
 for url , II1i11I , IIii11Ii1i1I in iIIi1i1 :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + IIii11Ii1i1I )
 for url in next :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , OOoOO0oo0ooO + 'Next.png' )
def IiiI ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 75 - 75: ii . i1IiIIIII + oO0o / OoOO00O - oOo0O0Ooo % OoOO00O
  if 89 - 89: IIiI1I * iI11I1II1I1I + Ii . ii
  if 51 - 51: i1IiIIIII / O0oOO0 + oO0o % OOooOOo / OoOO00O
ii111i1i = '{PQ},' ; OOo0OOooo0 = '{SC},' ; oooOoOoOO = '{XG},' ; OooOOii = '{JP},' ; o0oo0Oo = '{HW},' ; i1i1I1II = '{RT},'
def o0o0oO ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 O00o = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0o0ooOo00 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 OO00oO0OoO0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I11I111i1I1 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iii1 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1i111I
 O0Ooo0O = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iii1oOo0OoOOOo0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 OOoo00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I1I1O0O = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 66 - 66: Ii1I - ooOoO0O00 % Ii1I / OoOO00O % ooOoO0O00 . Ii1i111I
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIiII = i1I1iI ( Ooo00OoOOO )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( o0o0ooOo00 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 Iii = i1I1iI ( OO00oO0OoO0o )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0OoooO = i1I1iI ( iii1 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOO0 = i1I1iI ( O0Ooo0O )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 Oo00Oo = i1I1iI ( iii1oOo0OoOOOo0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 iIiO0O = i1I1iI ( OOoo00 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 oOOoooo = i1I1iI ( I1I1O0O )
 if 70 - 70: IIiI1I . IIiIiII11i . IIiI1I - iI11I1II1I1I
 if 92 - 92: oO0o
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
  for I1I1ooo0 , II1i11I in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ooo00OoOOO + I1I1ooo0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0ooOooo000oOO )
  for I1I1ooo0 , II1i11I in iIIi1i1 :
   if I1i111I in II1i11I . lower ( ) :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( OOoOooOoOOOoo + I1I1ooo0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oOOo )
  for I1I1ooo0 , II1i11I in i1IIii1iiIi :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1ii1ii11i1I + I1I1ooo0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if Oo0OoO00oOO0o != 'Failed' :
  oooo0OOo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for I1I1ooo0 , II1i11I in oooo0OOo :
   if I1i111I in II1i11I . lower ( ) :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , Ooo00OoOOO , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if Iii != 'Failed' :
  I11OOO0 = [ ]
  I1Ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Iii )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in I1Ii1 :
   if I1i111I in II1i11I . lower ( ) :
    if II1i11I in I11OOO0 :
     pass
    else :
     o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
     I11OOO0 . append ( II1i11I )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0OoooO != 'Failed' :
  O0oo0oOoO00 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0OoooO )
  for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in O0oo0oOoO00 :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + Ooo00OoOOO , 7067 , IIii11Ii1i1I )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 48 - 48: Ii1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if ooOO0 != 'Failed' :
  o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO0 )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in o0o :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Redemption[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 39 - 39: i1IiIIIII + oO0o
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo00Oo != 'Failed' :
  oOoOOOO0OOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo00Oo )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in oOoOOOO0OOO :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Reaper[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 58 - 58: Ii1i111I % Ii / Ii * O0oOO0 - oO00Oo0o000
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iIiO0O != 'Failed' :
  i11ii111i1ii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIiO0O )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in i11ii111i1ii :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Herovision[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 97 - 97: Ii + I1ii11iIi11i * i1IiIIIII % IIiI1I . O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 4 - 4: o0o00Oo0O . IIiI1I - iI11I1II1I1I
 if oOOoooo != 'Failed' :
  I1iII11ii1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oOOoooo )
  for Ooo00OoOOO , o00OooO0oo , II1i11I in I1iII11ii1 :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Silent Hunter[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 4 - 4: Ii - i1IiIIIII % Ii1I * oO00Oo0o000 % I11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 II1III1i1iiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 71 - 71: O0oOO0 . O0oOO0 - iI11I1II1I1I
 for IiIi1i in II1III1i1iiI :
  oO0 = OOO00 + IiIi1i + OooO0
  Ii1IOoO0o0O = i1I1iI ( oO0 )
  if Ii1IOoO0o0O != 'Failed' :
   iIoOoO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1IOoO0o0O )
   for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in iIoOoO0 :
    if I1i111I in II1i11I . lower ( ) :
     OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source Pandoras[/COLOR]' , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 31 - 31: Ii - O0oOO0 / Ii1I - OoOO00O
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 5 - 5: Ii * I1ii11iIi11i
 II1III1i1iiI = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 29 - 29: OoOO00O / O0oOO0 % Ii1i111I
 if 10 - 10: iI11I1II1I1I % ii % Ii1I
 for IiIi1i in II1III1i1iiI :
  oO0 = O00o + IiIi1i
  IiiI1i111I1i = i1I1iI ( oO0 )
  if IiiI1i111I1i != 'Failed' :
   OO0O0OO0O0 = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( IiiI1i111I1i )
   for I1I1ooo0 , II1i11I in OO0O0OO0O0 :
    if I1i111I in II1i11I . lower ( ) :
     I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O00o + IiIi1i + I1I1ooo0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 78 - 78: O0O0O / ii . O0O0O
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 50 - 50: O00Oo000ooO0 . O0oOO0 - o0o00Oo0O % oOo0O0Ooo . oO00Oo0o000
     if 17 - 17: o0o00Oo0O + ii
def oo0OooO ( ) :
 if 4 - 4: O00Oo000ooO0 + iI11I1II1I1I * IIiI1I + I1ii11iIi11i * I11i % IIiIiII11i
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 if 88 - 88: O0O0O - ooOoO0O00 % Ii % IIiIiII11i * ii
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( I1i111I ) . replace ( ' ' , '%20' )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 o0o0ooOo00 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 OO00oO0OoO0o = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1i11 ) . replace ( ' ' , '+' )
 I11I111i1I1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 iii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 O0Ooo0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 40 - 40: I1ii11iIi11i
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 47 - 47: OOooOOo
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIiII = i1I1iI ( Ooo00OoOOO )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( o0o0ooOo00 )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 Iii = cloudflare . source ( OO00oO0OoO0o )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiI1i111I1i = i1I1iI ( I11I111i1I1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0OoooO = i1I1iI ( iii1 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 ooOO0 = i1I1iI ( O0Ooo0O )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 65 - 65: o0o00Oo0O + oO00Oo0o000 % OoOO00O * oOo0O0Ooo / O0oOO0 / OOooOOo
 if ooOO0 != 'Failed' :
  o0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOO0 )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in o0o :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source HeroVision[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 71 - 71: Ii / OOooOOo . O0O0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: O0O0O
 if o0OoooO != 'Failed' :
  O0oo0oOoO00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OoooO )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in O0oo0oOoO00 :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Reaper[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 39 - 39: oO0o + o0o00Oo0O + O0oOO0 * IIiIiII11i % o0o00Oo0O - o0o00Oo0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 41 - 41: O00Oo000ooO0 % I11i
    if 67 - 67: o0o00Oo0O % oO00Oo0o000
    if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % i1IiIIIII
    if 39 - 39: OoOO00O
    if 60 - 60: i1IiIIIII
    if 62 - 62: oO00Oo0o000 * Ii1i111I
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 74 - 74: OOooOOo . iI11I1II1I1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
  for IIii11Ii1i1I , Ooo00OoOOO , II1i11I in o0O00oOoOO :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + Ooo00OoOOO , 10044 , IIii11Ii1i1I , '' , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 87 - 87: O0oOO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 41 - 41: OOooOOo . iI11I1II1I1I % O0oOO0 + o0o00Oo0O
    if 22 - 22: I11i + I1ii11iIi11i . O0oOO0 + Ii1I * IIiI1I . Ii
    if 90 - 90: i1IiIIIII * OOooOOo - I1ii11iIi11i + I11i
    if 53 - 53: ii . ii + I11i - IIiI1I + i1IiIIIII
    if 44 - 44: oO00Oo0o000 - O00Oo000ooO0
    if 100 - 100: O0O0O . oO0o - OoOO00O + o0o00Oo0O * oO0o
    if 59 - 59: IIiIiII11i
    if 43 - 43: I1ii11iIi11i + ii
    if 47 - 47: O0oOO0
    if 92 - 92: Ii1i111I % Ii % I1ii11iIi11i
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOooo000oOO )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in iIIi1i1 :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , Ooo00OoOOO , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 23 - 23: IIiIiII11i * IIiI1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oOOo )
  for II1i11I in i1IIii1iiIi :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1ii1ii11i1I + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 80 - 80: oO00Oo0o000 / Ii + ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0OoO00oOO0o != 'Failed' :
  oooo0OOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for II1i11I in oooo0OOo :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0o0ooOo00 + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 38 - 38: Ii1I % O0oOO0 + ooOoO0O00 * ii * O0O0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Iii != 'Failed' :
  I1Ii1 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( Iii )
  for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in I1Ii1 :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source - Dizi[/COLOR]' , Ooo00OoOOO , 8062 , IIii11Ii1i1I )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 83 - 83: iI11I1II1I1I - O0oOO0 - oO00Oo0o000 / oO0o - o0o00Oo0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IiiI1i111I1i != 'Failed' :
  OO0O0OO0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiI1i111I1i )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in OO0O0OO0O0 :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Source Scooby[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 81 - 81: OoOO00O - O0O0O * Ii1I / oO00Oo0o000
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: oO0o
 O0o0oOOO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if IiiI1i111I1i != 'Failed' :
  for IiIi1i in O0o0oOOO :
   oO0 = OOO00 + IiIi1i + OooO0
   iIiO0O = Iiii ( oO0 )
   if iIiO0O != 'Failed' :
    i11ii111i1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIiO0O )
    for II1i11I , OOoOOO0 , Ooo00OoOOO , IIii11Ii1i1I , o0o0oOoOO0O , OOoooooooO in i11ii111i1ii :
     if I1i11 in II1i11I . lower ( ) :
      o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source Pandoras[/COLOR]' , Ooo00OoOOO , OOoooooooO , IIii11Ii1i1I , o0o0oOoOO0O , OOoOOO0 )
      Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
      if 24 - 24: I11i / OoOO00O / OoOO00O % IIiIiII11i - O0O0O * O0O0O
      oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
      if 58 - 58: OOooOOo
      if 60 - 60: IIiIiII11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0OOoo ( ) :
 if 96 - 96: i1IiIIIII
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIiII = Iiii ( Ooo00OoOOO )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , IIii11Ii1i1I , i1iiiIIi11II in o0O00oOoOO :
  o0oooOo0oo = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  if I1i111I in II1i11I . lower ( ) :
   OoO00 ( II1i11I , '' , 7022 , o0oooOo0oo )
   if 33 - 33: oO00Oo0o000 % IIiIiII11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
IIi1II = '{ZH},' ; i11iIi11I1I11II = '{IX},' ; IIiiiI = '{LM},'
if 59 - 59: O0O0O % O0oOO0
def ii1II1iiii ( url ) :
 IIIIIiiI11i1 = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IIIIIiiI11i1 )
 for url , II1ii , OOooO0o0 , II1i11I in o0O00oOoOO :
  OoO00 ( ( II1ii ) . replace ( 'Sezon' , ' Season ' ) + ( OOooO0o0 ) . replace ( 'Bölüm' , ' Episode ' ) + II1i11I , url , 8063 , '' )
  if 43 - 43: oOo0O0Ooo / IIiI1I / O0oOO0 + iI11I1II1I1I + ii
  if 33 - 33: IIiIiII11i - O00Oo000ooO0 - O0oOO0
  if 92 - 92: oO0o * O00Oo000ooO0
  if 92 - 92: O0O0O
def i1i1IIiII1I ( url ) :
 IIIIIiiI11i1 = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( IIIIIiiI11i1 )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 222 , '' )
  if 85 - 85: I1ii11iIi11i . Ii - Ii . oOo0O0Ooo . oO0o % ii
  if 20 - 20: oO00Oo0o000 + oO00Oo0o000 * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
  if 62 - 62: ii / OOooOOo . O00Oo000ooO0 . O00Oo000ooO0 % O0oOO0
  if 42 - 42: I11i . i1IiIIIII - O0oOO0
def IiiiO0oo0ooo0 ( ) :
 if 19 - 19: ooOoO0O00
 IIIIIiiI11i1 = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIIIIiiI11i1 )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I , OOooO0o0 in o0O00oOoOO :
  OoO00 ( II1i11I + '  -  ' + ( OOooO0o0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ooo00OoOOO , 8063 , IIii11Ii1i1I )
  if 60 - 60: OoOO00O * OOooOOo / I11i . oO00Oo0o000
def i1I1iiii1Ii11 ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 8002 , IIii11Ii1i1I )
def IiIIIIi ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , time , url , II1i11I , IIiI1i in o0O00oOoOO :
  o0OOOO00O0Oo ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , time ) , url , 1015 , IIii11Ii1i1I , IIiI1i )
  if 51 - 51: IIiIiII11i . O0O0O . oO0o % IIiIiII11i
def III1I1ii ( ) :
 if 4 - 4: iI11I1II1I1I . ooOoO0O00
 OoO00 ( 'Coronation Street' , '' , 8001 , '' )
 OoO00 ( 'Eastenders' , '' , 8002 , '' )
 OoO00 ( 'Emmerdale' , '' , 8003 , '' )
 OoO00 ( 'Hollyoaks' , '' , 8004 , '' )
 OoO00 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 63 - 63: iI11I1II1I1I + O00Oo000ooO0 % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
 if 60 - 60: I11i . OOooOOo % oO00Oo0o000 / oOo0O0Ooo / o0o00Oo0O
 if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / i1IiIIIII . Ii1I * O0oOO0
 if 59 - 59: iI11I1II1I1I / Ii1I % O0oOO0
def Oooo ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Holly' in II1i11I :
   IIii11Ii1i1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 74 - 74: O0oOO0 % OOooOOo / I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 2 - 2: O00Oo000ooO0 % O00Oo000ooO0 % oO00Oo0o000
def o0o00OoOo0 ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'East' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 98 - 98: ii % O0O0O * O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: oO0o * I11i * i1IiIIIII / I1ii11iIi11i * oO0o
def oOII11i1I ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Emmer' in II1i11I :
   IIii11Ii1i1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 69 - 69: O0oOO0 . i1IiIIIII - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: Ii . Ii1I / oOo0O0Ooo . i1IiIIIII + Ii
def i1I1i ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Coro' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 9 - 9: ii * Ii1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: I1ii11iIi11i + IIiI1I
def oooooO0oO0ooO ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Celeb' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 31 - 31: Ii1I
def O0OoOo ( name , url ) :
 OOOOoO0 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OOOOoO0 :
  IiiIiIIi1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIi1i1iIi1iI = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( iIi1i1iIi1iI ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIi1i1iIi1iI = open_url ( url )
  i1oo = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( iIi1i1iIi1iI ) [ - 1 ]
  IiiIiIIi1 = i1oo . replace ( '\\/' , '/' )
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , '' , '' )
 Ooi111i1iIi1 . setPath ( IiiIiIIi1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ooi111i1iIi1 )
 if 83 - 83: o0o00Oo0O + OOooOOo / o0o00Oo0O / Ii1i111I
 if 68 - 68: ooOoO0O00 . Ii1i111I . ooOoO0O00 + O00Oo000ooO0 % oOo0O0Ooo
def IIoO ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o0O00oOoOO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Ooo00OoOOO , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
 for Ooo00OoOOO , II1i11I in iIIi1i1 :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Ooo00OoOOO , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
  if 13 - 13: ooOoO0O00
def IiiI111 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Movies' in II1i11I :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( Ooo00OoOOO ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOoOO0oo0ooO + 'popcorn.png' )
def O0OOOo0Oo0 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOoOO0oo0ooO + 'Next.png' )
  if 55 - 55: i1IiIIIII / OOooOOo * i1IiIIIII
  if 40 - 40: oO0o . Ii + Ii1I + oOo0O0Ooo . O0O0O
def O0oo0O0OO0Oo ( url ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url , IIii11Ii1i1I in o0O00oOoOO :
  if '{{' in II1i11I :
   pass
  else :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IIii11Ii1i1I )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
oO00o0oO0O = '{UJ},' ; iI11Iii1I = '{WE},' ; o0i1I = '{WP},' ; O0o0o00OoOo = '{PP},'
def oO00o0O0Ooo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url , IIii11Ii1i1I in o0O00oOoOO :
  if '{{' in II1i11I :
   pass
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIii11Ii1i1I )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii11 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1i11IIIi ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1i11IIIi ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: O0O0O * IIiI1I + OOooOOo - O0O0O + Ii1I
 if 14 - 14: oO0o
 if 38 - 38: o0o00Oo0O
def ooO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '(cooltvseries.com)' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
 for url , II1i11I in iIIi1i1 :
  if '(cooltvseries.com)' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
def i1i1i11iI11II ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  OOoO0oO00o ( ( url ) . replace ( ' ' , '%20' ) )
II1iiI1iI = '{XX},' ; O0oo0000o = '{UD},' ; OOoO0oooO = '{YT},' ; o00oo = '{JS},' ; O000Oo00 = '{PF},'
if 43 - 43: oO0o . O0oOO0 * I1ii11iIi11i
def iio00O0o00oo ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( Ooo00OoOOO ) ) , 222 , IIii11Ii1i1I )
  if 19 - 19: oOo0O0Ooo
def oOOoo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  if 'youtu' in url :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IIii11Ii1i1I )
 for url in next :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , OOoOO0oo0ooO + 'Next.png' )
  if 26 - 26: Ii1i111I + oO00Oo0o000 + Ii1i111I / oO00Oo0o000
def oOo0Oo00O ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 28 - 28: O0oOO0 . ooOoO0O00
def o0o00O ( url ) :
 iIi1i1iIi1iI = Iiii
 o0O00oOoOO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , IIii11Ii1i1I )
  if 46 - 46: OOooOOo
  if 4 - 4: IIiI1I + o0o00Oo0O
  if 28 - 28: O00Oo000ooO0 + Ii + ii / oO0o
  if 6 - 6: oOo0O0Ooo - Ii
  if 61 - 61: oO00Oo0o000 * Ii1I % oOo0O0Ooo % oO0o % Ii1i111I + Ii1i111I
def i1111I ( ) :
 if 58 - 58: ii - Ii1i111I + iI11I1II1I1I * Ii
 OoO00 ( 'All Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Entertainment' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Movies' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Music' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'News' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Sports' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Documentary' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Kids' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Food' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Religious' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'USA Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 OoO00 ( 'Other' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 if 80 - 80: ooOoO0O00 . oOo0O0Ooo - O0O0O + i1IiIIIII + IIiI1I % O0O0O
 if 13 - 13: IIiIiII11i / OOooOOo / OOooOOo + O0oOO0
def Ii1i ( Cat_Name ) :
 if 62 - 62: ii . OoOO00O
 IIioo0 = False
 O0Ii11I = '0'
 if Cat_Name == 'All Channels' : IIioo0 = True
 if Cat_Name == 'Entertainment' : O0Ii11I = '1'
 if Cat_Name == 'Movies' : O0Ii11I = '2'
 if Cat_Name == 'Music' : O0Ii11I = '3'
 if Cat_Name == 'News' : O0Ii11I = '4'
 if Cat_Name == 'Sports' : O0Ii11I = '5'
 if Cat_Name == 'Documentary' : O0Ii11I = '6'
 if Cat_Name == 'Kids' : O0Ii11I = '7'
 if Cat_Name == 'Food' : O0Ii11I = '8'
 if Cat_Name == 'Religious' : O0Ii11I = '9'
 if Cat_Name == 'USA Channels' : O0Ii11I = '10'
 if Cat_Name == 'Other' : O0Ii11I = '11'
 if 72 - 72: o0o00Oo0O + I11i + oOo0O0Ooo / I1ii11iIi11i
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 print 'Len Match: >>>' + str ( len ( o0O00oOoOO ) )
 for II1i11I , IIii11Ii1i1I , i1iiiIIi11II in o0O00oOoOO :
  o0oooOo0oo = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  if i1iiiIIi11II == O0Ii11I :
   OoO00 ( II1i11I , '' , 7022 , o0oooOo0oo )
  elif IIioo0 == True :
   OoO00 ( II1i11I , '' , 7022 , o0oooOo0oo )
  else : pass
  if 83 - 83: O00Oo000ooO0 - oOo0O0Ooo . OoOO00O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: OOooOOo - O0O0O * ii
def IiI1I1IIIi1i ( Search_Name ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , Ooo00OoOOO , OOoOooOoOOOoo , I1ii1ii11i1I in o0O00oOoOO :
  o0oooOo0oo = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  I1IIiI ( Search_Name + ': Link 1' , ( Ooo00OoOOO ) . replace ( '\\' , '' ) , 222 , o0oooOo0oo )
  I1IIiI ( Search_Name + ': Link 2' , ( OOoOooOoOOOoo ) . replace ( '\\' , '' ) , 222 , o0oooOo0oo )
  I1IIiI ( Search_Name + ': Link 3' , ( I1ii1ii11i1I ) . replace ( '\\' , '' ) , 222 , o0oooOo0oo )
  if 73 - 73: o0o00Oo0O * oO00Oo0o000 . ooOoO0O00
def OO00OoOO ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOoOO0oo0ooO + 'english.png' )
def iiii1II1ii11 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'xxx.png' )
def i1IIIII1 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'vod(1).png' )
  if 13 - 13: oO0o % iI11I1II1I1I - IIiIiII11i / oOo0O0Ooo
def iII111iiiI11i ( url ) :
 url
 iIi11i = xbmcgui . ListItem ( II1i11I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIi11i )
 return
 if 4 - 4: O0oOO0 % O00Oo000ooO0 . oO00Oo0o000
 if 91 - 91: Ii1I + iI11I1II1I1I % O00Oo000ooO0
def O0o0OOOO0 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIi1i1iIi1iI )
 for url , OOoOOO0 , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , ( OOoOOO0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , OOoOO0oo0ooO + 'Next.png' )
  if 29 - 29: ii . oO00Oo0o000 % oO00Oo0o000
def IIIIIII1i ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIiII )
 for url , OOoOOO0 , IIii11Ii1i1I in o0O00oOoOO :
  OOooOoooOoOo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , OOoOOO0 )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 OO0OO000 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 for i1I1Iiii in OO0OO000 :
  I1iIIIiiii = ( i1I1Iiii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o0OOOO00O0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , I1iIIIiiii )
  if 44 - 44: oO00Oo0o000 / OoOO00O * i1IiIIIII * ooOoO0O00 . OoOO00O * Ii
def O0o0oo0O ( INFO ) :
 o0iI11I1II ( 'info for workout' , INFO )
 if 74 - 74: IIiIiII11i % Ii1i111I . oO0o * oO0o
 if 27 - 27: Ii1i111I * I1ii11iIi11i . OoOO00O . oOo0O0Ooo % IIiIiII11i - O0O0O
 if 52 - 52: oOo0O0Ooo % oO0o * OoOO00O * IIiI1I / i1IiIIIII
def oooO00oo0 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 9031 , OOoOO0oo0ooO + 'icon.png' )
def o000 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 9032 , OOoOO0oo0ooO + 'icon.png' )
def oOiiIIIII ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  if '://' in II1i11I :
   pass
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOoOO0oo0ooO + 'icon.png' )
def iiI1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 222 , OOoOO0oo0ooO + 'icon.png' )
  if 40 - 40: o0o00Oo0O + O00Oo000ooO0 . OoOO00O
  if 29 - 29: i1IiIIIII / OOooOOo . iI11I1II1I1I / Ii1i111I % OOooOOo % IIiI1I
  if 49 - 49: IIiIiII11i / O00Oo000ooO0 - OoOO00O
def IiIII ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'category' in Ooo00OoOOO :
   OoO00 ( II1i11I , 'http://www.disclose.tv/' + Ooo00OoOOO , 7010 , OOoOO0oo0ooO + 'disclose.png' )
   if 92 - 92: oOo0O0Ooo % IIiI1I
   if 31 - 31: ii - O0O0O / oO00Oo0o000
def oo00o000O ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( II1i11I , 'http://www.disclose.tv/' + url , 7011 , IIii11Ii1i1I )
 for url in next :
  OoO00 ( 'NEXT' , url , 7010 , OOoOO0oo0ooO + 'Next.png' )
  if 66 - 66: ii + I11i . ooOoO0O00 * IIiI1I
  if 92 - 92: Ii1i111I / oO00Oo0o000
def iiIIiii1iii1I ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 i1IIii1iiIi = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  if 'http' in url :
   I1IIiI ( 'video/flv' , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url , II1i11I in iIIi1i1 :
  I1IIiI ( II1i11I , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url in i1IIii1iiIi :
  I1IIiI ( 'YT Link' , url , 8043 , OOoOO0oo0ooO + 'disclose.png' )
  if 14 - 14: o0o00Oo0O / Ii1i111I . oO0o % IIiI1I . O0O0O
  if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def Iii1II1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOoOO0oo0ooO + 'icon.png' )
  if 54 - 54: OOooOOo . I1ii11iIi11i
def Ii1iIIi11 ( name , url , img ) :
 IIiII = Iiii ( url )
 iIiiII1Ii1ii = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIiII )
 iIIi1 = len ( iIiiII1Ii1ii )
 if 76 - 76: oOo0O0Ooo - oOo0O0Ooo - I11i % O0oOO0 * o0o00Oo0O
 if 11 - 11: OoOO00O + Ii1i111I . oO0o . Ii * oO0o
 if iIIi1 == 1 :
  for I1IIiIi in iIiiII1Ii1ii :
   I1IIiIi = I1IIiIi . replace ( 'player' , 'watch' )
   OOOOoOoO = I1IIiIi + '&fv=&sou='
   OO000 = Iiii ( OOOOoOoO )
   o0oOoo0o = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( OO000 )
   for oooOo in o0oOoo0o :
    IiiIiIIi = False
    Resolve ( oooOo )
    if 63 - 63: IIiI1I / Ii1I * O0O0O / IIiIiII11i + i1IiIIIII - o0o00Oo0O
 elif iIIi1 > 1 :
  if 16 - 16: IIiIiII11i / OoOO00O . OoOO00O - OoOO00O / Ii1I
  for I1IIiIi in iIiiII1Ii1ii :
   I1Ii11i1ii1i = Iiii ( I1IIiIi )
   oOOoOoOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( I1Ii11i1ii1i )
   iII11 = oOOoOoOO
   iII11 = ( str ( iII11 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iII11
   I1IIiI ( 'DOUBLE LINK' , iII11 , 424 , '' )
   if 96 - 96: Ii1i111I * Ii1I * OoOO00O + Ii1I % oOo0O0Ooo + Ii
   for url in oOOoOoOO :
    OoO00 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OOoOooOoOOOoo = Google . resolve ( url )
    except :
     pass
    try :
     i1iI11Ii1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OOoOooOoOOOoo ) )
     for Iii1Iii , iiI11111II in i1iI11Ii1i :
      if 48 - 48: IIiI1I % Ii . ii * O00Oo000ooO0 % oO0o . IIiI1I
      HD_URLS . append ( Iii1Iii )
      SD_URLS . append ( iiI11111II )
    except :
     pass
 else :
  pass
  if 6 - 6: o0o00Oo0O . O0oOO0 - O0O0O / Ii
def O00O0O00o0O ( ) :
 if 73 - 73: oO0o
 if 28 - 28: ii - Ii1i111I
 OoO00 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOoOO0oo0ooO + 'Movies.png' )
 if 84 - 84: IIiIiII11i
 OoO00 ( 'Search Movies' , '' , 7017 , OOoOO0oo0ooO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 36 - 36: i1IiIIIII - OOooOOo - iI11I1II1I1I
 if 10 - 10: Ii1I / OoOO00O * ooOoO0O00 % o0o00Oo0O + Ii1i111I
def I1i1ii1ii ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://cnfstudio.com/' )
 o0O00oOoOO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , 'http://cnfstudio.com/genre/' + Ooo00OoOOO , 7003 , OOoOO0oo0ooO + 'icon.png' )
  if 32 - 32: O00Oo000ooO0 / ii
oooOOOOO = xbmcgui . Dialog ( )
if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - IIiI1I - Ii
oo0O00o0 = '{UN},' ; Oo0oOooOooO = '{IG},' ; ii1I1iIII = '{PL},' ; IIii1 = '{LO},' ; II1iII1 = '{LP},' ; I11II11IiI11 = '{HA},' ; O00oIi11Iiii1iiii = '{XD},' ; i1IIII1111 = '{TA},' ; Ooo0o0000OO = '{DP},' ; iIiI1II1I1 = '{JT},' ; OooiIiI1i1Ii = '{JJ},' ; Oo0o00o = '{MM},' ; III1I1 = '{FQ},' ; iI1IIIIII = '{HH},'
if 79 - 79: I1ii11iIi11i - ii % oO00Oo0o000 + ii - Ii1i111I % OOooOOo
def iII ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 OOo0O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IIii11Ii1i1I )
 OOo0O = OOo0O
 for url in OOo0O :
  OoO00 ( 'Next Page' , url , 7003 , OOoOO0oo0ooO + 'Next.png' )
  if 18 - 18: oOo0O0Ooo . Ii1I - I1ii11iIi11i
def Iii1 ( url ) :
 if 64 - 64: O0oOO0 / ooOoO0O00 % IIiI1I
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  O00oO = url + '&fv=&sou='
  O00oO = O00oO . replace ( 'player' , 'watch' )
  OOoOo0O0 = I1o0 ( O00oO )
  I1IiiiiI1i1I = I1o0 ( url )
  if 48 - 48: Ii1i111I + IIiIiII11i % O0O0O % i1IiIIIII * IIiIiII11i
  if 41 - 41: oO0o
def I1o0 ( url ) :
 if 13 - 13: O0oOO0 - oOo0O0Ooo
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  Iiii1iI1i ( url )
  if 23 - 23: oOo0O0Ooo
  if 7 - 7: IIiI1I % Ii1I
def o0oOOO ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , OOoOO0oo0ooO + 'LocalM3U.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , OOoOO0oo0ooO + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 47 - 47: i1IiIIIII / IIiIiII11i % O00Oo000ooO0 . O0O0O * Ii1I
def iIii1iIiII1i1 ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  o0oO = open ( oOo0oooo00o , 'r' )
  for iIi11i in o0oO :
   o0Oo = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi11i )
   for II1i11I , Ooo00OoOOO in o0Oo :
    I1IIiI ( II1i11I , Ooo00OoOOO , 222 , OOoOO0oo0ooO + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 16 - 16: oO0o % OoOO00O + Ii1I + I1ii11iIi11i / iI11I1II1I1I
def OoOO0OO0O0o ( url ) :
 if os . path . exists ( Remote ) :
  IIiII = iiIi1iI1iIii ( url )
  o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
  for II1i11I , url in o0O00oOoOO :
   url = ( url ) . strip ( )
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 29 - 29: OOooOOo + oO00Oo0o000 / i1IiIIIII + O0oOO0
  if 42 - 42: iI11I1II1I1I - O0oOO0 - Ii1i111I - oO00Oo0o000
def i1iIi ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for Ooo00OoOOO in o0O00oOoOO :
  Ooo00OoOOO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + Ooo00OoOOO
 II1i11I = 'plugin.video.GenieTv'
 if 33 - 33: OOooOOo - o0o00Oo0O
 III11iI1i11i ( Ooo00OoOOO , II1i11I )
 if 30 - 30: OOooOOo / O0O0O / OoOO00O * I11i * O0O0O . oOo0O0Ooo
def IIII ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for Ooo00OoOOO in o0O00oOoOO :
  Ooo00OoOOO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + Ooo00OoOOO
 II1i11I = 'repository.GenieTv'
 if 93 - 93: OOooOOo
 III11iI1i11i ( Ooo00OoOOO , II1i11I )
 if 97 - 97: Ii
 if 68 - 68: O00Oo000ooO0 * oO0o . Ii1i111I / OoOO00O . I11i - Ii
def II11I ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , OOoOO0oo0ooO + 'Catagories.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 72 - 72: oO0o - iI11I1II1I1I . IIiI1I / OoOO00O
 if 12 - 12: oOo0O0Ooo + oO00Oo0o000
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
oOo = 'https://addons.tvaddons.ag/'
if 90 - 90: IIiIiII11i / oO0o / OoOO00O
def O0oooOOo0 ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 O0Ooo0O0OO = 'https://addons.tvaddons.ag/search/?keyword=' + I1i11
 IIiII = Iiii ( O0Ooo0O0OO )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , IiIi , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , Ooo00OoOOO , 10054 , 'https://addons.tvaddons.ag/' + IiIi , i1iIIi1 , '' )
  if 16 - 16: oO0o + Ii1i111I / iI11I1II1I1I % IIiIiII11i
  if 39 - 39: ooOoO0O00 . Ii1I / Ii1i111I / Ii1i111I
def ooOo0oO0O ( ) :
 IIiII = Iiii ( oOo )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if 'Repositories' in II1i11I :
   pass
  elif 'Services' in II1i11I :
   pass
  elif 'International' in II1i11I :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 10053 , 'https://addons.tvaddons.ag/' + IIii11Ii1i1I , i1iIIi1 , '' )
   if 17 - 17: O00Oo000ooO0 / oO00Oo0o000 . oOo0O0Ooo + ooOoO0O00
   if 28 - 28: O0O0O % OOooOOo + oO00Oo0o000 * IIiI1I * OoOO00O
def Addon ( url ) :
 IIiII = Iiii ( url )
 oOOo = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIiII )
 for url in oOOo :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if 'Please' in II1i11I :
   pass
  else :
   o0OOOO00O0Oo ( II1i11I , url , 10054 , 'https://addons.tvaddons.ag/' + IIii11Ii1i1I , i1iIIi1 , '' )
   if 33 - 33: Ii1I
   if 54 - 54: O0oOO0 * Ii1I . IIiIiII11i / i1IiIIIII % i1IiIIIII
def IiIIii1 ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   OO0ooOOO00 = os . path . join ( O0000OOO0 , name + '.zip' )
   try :
    os . remove ( OO0ooOOO00 )
   except :
    pass
   downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
   IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print IIIIIiII1
   print '======================================='
   extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
   Ii1IIiI1i ( )
   if 7 - 7: o0o00Oo0O - Ii1I / OOooOOo - OoOO00O - O0O0O / ii
def III11iI1i11i ( url , name ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 OO0ooOOO00 = os . path . join ( O0000OOO0 , name + '.zip' )
 try :
  os . remove ( OO0ooOOO00 )
 except :
  pass
 downloader . download ( url , OO0ooOOO00 , Oo0oO0ooo )
 IIIIIiII1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print IIIIIiII1
 print '======================================='
 extract . all ( OO0ooOOO00 , IIIIIiII1 , Oo0oO0ooo )
 Ii1IIiI1i ( )
 if 12 - 12: ii
def Ii1IIiI1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 55 - 55: Ii1I + Ii1I
 if 87 - 87: O00Oo000ooO0
def oOOo0OOoOO0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 1007 , IiIi )
def IiIiIIi1IiiIi1III ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IiIi )
  if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - O0O0O / Ii1I
  if 16 - 16: OoOO00O
def Oo00O00o0 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , iconimage , OOoOOO0 , o0o0oOoOO0O , name in o0O00oOoOO :
  if 'http' in url :
   if '.php' in url :
    O0o0OO00 = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
    for iIi11i in O0o0OO00 :
     if iIi11i == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    o00iI1i1II ( name , url , 1016 , iconimage , o0o0oOoOO0O , OOoOOO0 )
   else :
    if 'youtube' in url :
     O0o0OO00 = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
     for iIi11i in O0o0OO00 :
      if iIi11i == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0oO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0o0oOoOO0O , OOoOOO0 )
    else :
     O0o0OO00 = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
     for iIi11i in O0o0OO00 :
      if iIi11i == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0oO ( name , url , 222 , iconimage , o0o0oOoOO0O , OOoOOO0 )
     oO00OOoO00 ( 'movies' , 'INFO' )
  else :
   IiII1 ( url , iconimage , name )
   if 45 - 45: oO0o + oO0o % O0oOO0
 else :
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
  for url , IiIi , name in o0O00oOoOO :
   if 'http' in url :
    if '.php' in url :
     OoO00 ( name , url , 1016 , IiIi )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      I1IIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiIi )
     else :
      O0o0OO00 = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
      for iIi11i in O0o0OO00 :
       if iIi11i == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      I1IIiI ( name , url , 222 , IiIi )
      oO00OOoO00 ( 'movies' , 'INFO' )
   else :
    IiII1 ( url , IiIi , name )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 36 - 36: OoOO00O * Ii1i111I . Ii1i111I / I1ii11iIi11i / oOo0O0Ooo
def IiII1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oooO0ooo = ( url ) . replace ( i11iIi11I1I11II , 'http' ) . replace ( O0oo0000o , '.com' ) ;
 I1iI11IIiIiI1 = ( oooO0ooo ) . replace ( IIiiiI , 'a' ) . replace ( oooOoOoOO , 'b' ) . replace ( OooOOii , 'c' ) . replace ( iI11Iii1I , 'd' ) . replace ( ii1I1iIII , 'e' ) . replace ( iIiI1II1I1 , 'f' ) ;
 ii1Iiiiiii = ( I1iI11IIiIiI1 ) . replace ( II1iiI1iI , 'g' ) . replace ( I11II11IiI11 , 'h' ) . replace ( OOoO0oooO , 'i' ) . replace ( O000Oo00 , 'j' ) . replace ( o0oo0Oo , 'k' ) . replace ( i1i1I1II , 'l' ) ;
 OOoo0 = ( ii1Iiiiiii ) . replace ( Ii11I1iIIi , 'm' ) . replace ( O0ooO , 'n' ) . replace ( iIOO , 'o' ) . replace ( I1III1I11I1 , 'p' ) . replace ( oO000OoO00OoO , 'q' ) . replace ( I1IiIi1iiI , 'r' ) ;
 iiII1II11i = ( OOoo0 ) . replace ( ooO0 , 's' ) . replace ( o0i1I , 't' ) . replace ( OoooooOo0oOo0 , 'u' ) . replace ( II11II , 'v' ) . replace ( i1ii11 , 'w' ) . replace ( IIIo00O , 'x' ) ;
 ii1I1I1 = ( iiII1II11i ) . replace ( oo0oOOO0oOoo , 'y' ) . replace ( Ii1o0OOOoo0000 , 'z' ) . replace ( oo0O00o0 , '.' ) . replace ( Oo0oOooOooO , '(' ) . replace ( IIii1 , ')' ) . replace ( II1iII1 , '/' ) ;
 IiIIii1i1i11iII = ( ii1I1I1 ) . replace ( IIi1II , '1' ) . replace ( O0o0o00OoOo , '2' ) . replace ( o0II1 , '3' ) . replace ( i1IIII1111 , '4' ) . replace ( Ooo0o0000OO , '5' ) . replace ( o00oo , '6' ) ;
 OOOiiIII1I11iii = ( IiIIii1i1i11iII ) . replace ( OooiIiI1i1Ii , '7' ) . replace ( Oo0o00o , '8' ) . replace ( III1I1 , '9' ) . replace ( iI1IIIIII , '0' ) . replace ( ii111i1i , ':' ) . replace ( OOo0OOooo0 , '%' ) ;
 url = ( OOOiiIII1I11iii ) . replace ( oO00o0oO0O , '-' ) . replace ( O00oIi11Iiii1iiii , '_' ) ;
 I1IIiI ( name , url , 222 , iconimage ) ;
 if 95 - 95: o0o00Oo0O . oO0o
 if 89 - 89: ooOoO0O00
def I11II ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1007 , IiIi )
def OOOO0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IiIi )
  if 39 - 39: ii
def i1iIII1IIi ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 Oo0oo0OOO0OOoOO = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 Oo0oo0OOO0OOoOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0oo0OOO0OOoOO )
 if 97 - 97: ooOoO0O00
 if 46 - 46: Ii1I
def II1i1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if '-dir-' in II1i11I :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IIii11Ii1i1I )
  else :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IIii11Ii1i1I )
   if 51 - 51: O0oOO0 * IIiI1I / ooOoO0O00
def IIi1I1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 iIIiiII11i1I1 = ( 'http://afewbitsmore.com/' )
 o0O00oOoOO = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '[To Parent Directory]' in II1i11I :
   II1i11I = 'HOME'
   pass
  elif 'HOME' in II1i11I :
   pass
  elif '.m3u' in II1i11I :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , iIIiiII11i1I1 + url , 2002 , OOoOO0oo0ooO + 'music.png' )
  elif '.mp3' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iIIiiII11i1I1 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  elif '.m4a' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iIIiiII11i1I1 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) , iIIiiII11i1I1 + url , 1012 , OOoOO0oo0ooO + 'music.png' )
def Ii111Ii1iiIi1 ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , II1i11I , url in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , OOoOO0oo0ooO + 'music.png' )
  if 62 - 62: oO0o . IIiI1I . IIiI1I % ooOoO0O00 * O0O0O % I1ii11iIi11i
def I1I11 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 iIIiiII11i1I1 = url
 o0O00oOoOO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '.mp3' in II1i11I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '/' , '' ) , iIIiiII11i1I1 + url , 1011 , OOoOO0oo0ooO + 'music.png' )
def i1iiiiIIIi ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , ( 'http://www.cyn.net/music/' + Ooo00OoOOO ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IIii11Ii1i1I ) . replace ( ' ' , '%20' ) )
def Ii11Ii1 ( url , img ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOoOooOoOOOoo = url
 img = img
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OOoOooOoOOOoo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 39 - 39: OOooOOo . O00Oo000ooO0 - OoOO00O % ooOoO0O00 % O0oOO0 . O0O0O
def oO00OO0o0ooO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOoOooOoOOOoo = url
 o0O00oOoOO = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for type , url , II1i11I in o0O00oOoOO :
  if '[VID]' in type :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OOoOooOoOOOoo + url , 222 , OOoOO0oo0ooO + 'music.png' )
  if '[DIR]' in type :
   oO00OO0o0ooO ( OOoOooOoOOOoo + url )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: o0o00Oo0O * IIiI1I . OOooOOo / i1IiIIIII - OoOO00O . Ii1i111I
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - O0oOO0 % iI11I1II1I1I - OoOO00O
def III1I11II11I ( ) :
 O00o = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 78 - 78: Ii1I . oO00Oo0o000 . oO00Oo0o000 . Ii1i111I % IIiI1I
 IIiII = i1I1iI ( Ooo00OoOOO )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 if 26 - 26: O0oOO0 + oO0o / OOooOOo . IIiIiII11i * OoOO00O
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for II1i11I in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo00OoOOO + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + IIiI1I % oOo0O0Ooo * O0O0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for II1i11I in iIIi1i1 :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOoOooOoOOOoo + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 74 - 74: IIiI1I / Ii1i111I . oOo0O0Ooo - ii + IIiIiII11i + Ii1i111I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oo0oOOo )
  for II1i11I in i1IIii1iiIi :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1ii1ii11i1I + II1i11I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 36 - 36: OoOO00O * oOo0O0Ooo * Ii1I . Ii1i111I * Ii1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 76 - 76: i1IiIIIII + o0o00Oo0O / O00Oo000ooO0 - oO0o
    if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * IIiI1I * IIiIiII11i * Ii1I
    if 9 - 9: Ii + i1IiIIIII - OOooOOo / O0oOO0 % ooOoO0O00 / O0O0O
    if 22 - 22: ooOoO0O00
    if 3 - 3: oO0o * Ii1I - IIiI1I + Ii1I
    if 63 - 63: Ii1i111I * O0oOO0 % IIiIiII11i % oO00Oo0o000 + oOo0O0Ooo * I1ii11iIi11i
Ii11I1iIIi = '{SF},' ; O0ooO = '{IF},' ; iIOO = '{PW},' ; o0II1 = '{AM},' ; I1III1I11I1 = '{GF},' ; oO000OoO00OoO = '{DD},' ; I1IiIi1iiI = '{UO},' ; ooO0 = '{LE},' ; OoooooOo0oOo0 = '{ZY},' ; II11II = '{UE},' ; i1ii11 = '{PE},' ; IIIo00O = '{JE},' ; oo0oOOO0oOoo = '{TH},' ; Ii1o0OOOoo0000 = '{LK},'
if 96 - 96: O00Oo000ooO0
if 99 - 99: iI11I1II1I1I - O0oOO0
def Oo0O00O ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.iwatchseries.me/tv-list/' )
 o0O00oOoOO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 8021 , OOoOO0oo0ooO + 'iwatch.png' )
def OOoOOO0IiI1i1i1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , O00Oo0o000oO in o0O00oOoOO :
  OoO00 ( II1i11I + O00Oo0o000oO , url , 8022 , OOoOO0oo0ooO + 'iwatch.png' )
def O0O000oOO0 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1iI1iiI1Ii1 ( url )
def I1iI1iiI1Ii1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 i1IIii1iiIi = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( 'VidSpot - ' + II1i11I , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for url in iIIi1i1 :
  I1IIiI ( 'VodLocker' , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for II1i11I , url in i1IIii1iiIi :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   I1IIiI ( 'TheVideo - ' + II1i11I , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
   if 62 - 62: Ii1i111I % O0O0O / ii % ii
def oo0OO0oOo ( ) :
 iIi1i1iIi1iI = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o0O00oOoOO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1021 , OOoOO0oo0ooO + 'anime.png' )
  if 36 - 36: OOooOOo * oO0o / O0oOO0 / oOo0O0Ooo - OoOO00O
  if 53 - 53: O0O0O
def oo0OoO ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.animetoon.org/cartoon' )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1002 , OOoOO0oo0ooO + 'anime.png' )
  if 3 - 3: O00Oo000ooO0 - ii * ii - oOo0O0Ooo / oO00Oo0o000 * Ii1I
  if 58 - 58: O00Oo000ooO0 % iI11I1II1I1I / Ii % I11i . oO00Oo0o000 * IIiI1I
  if 32 - 32: ii + I11i
def o0000OOOo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I in iIIi1i1 :
  o0oo000OoOoo0 = IIii11Ii1i1I
 i1IIii1iiIi = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( iIi1i1iIi1iI )
 for url in i1IIii1iiIi :
  OoO00 ( 'NEXT PAGE' , url , 1002 , OOoOO0oo0ooO + 'Next.png' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 1003 , o0oo000OoOoo0 )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0oOO ( url , IMAGE ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  print II1i11I + '     ' + url
  if 'easy' in url :
   O000oOOoOOO ( url )
  elif 'playpanda' in url :
   O000oOOoOOO ( url )
   if 40 - 40: oOo0O0Ooo / ii + oO0o * oO0o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def O000oOOoOOO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1IIiI ( 'STREAM' , url , 222 , OOoOO0oo0ooO + 'anime.png' )
  if 9 - 9: iI11I1II1I1I
  if 57 - 57: O0oOO0 / OoOO00O % I11i % Ii
def o0OO0Oooo ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oo0OooOOo0 . add_header ( 'referer' , url )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 97 - 97: IIiI1I
def iiIi1iI1iIii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 88 - 88: ii - i1IiIIIII + o0o00Oo0O * O00Oo000ooO0 * Ii1i111I
def iIi1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0Oi11i1I = ( '%s%s' % ( O00O0 , url ) )
 O00oO = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , IiIi , II1i11I in o0O00oOoOO :
  I1IIiI ( '%s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IiIi )
  if 21 - 21: Ii * IIiI1I / O0oOO0 % IIiI1I * I1ii11iIi11i
def Iiii1iI1i ( url ) :
 if 84 - 84: iI11I1II1I1I
 III1Ii11i1II = open ( oOoOooOo0o0 , "a" )
 III1Ii11i1II . write ( 'url="' + url + '"\n' )
 III1Ii11i1II . close
 if 28 - 28: OOooOOo % O0O0O - i1IiIIIII + i1IiIIIII + O0O0O / iI11I1II1I1I
 I1iiIi111I = xbmc . Player ( iIi ( ) )
 import urlresolver
 try : I1iiIi111I . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( II1i11I ) )
 I1iiIi111I = xbmc . Player ( iIi ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I1iiIi111I . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * i1IiIIIII
def ooOoo000 ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % II1i11I )
 xbmc . sleep ( 1 )
 I1iiIi111I = xbmc . Player ( iIi ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % II1i11I )
 xbmc . sleep ( 1 )
 I1iiIi111I . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 56 - 56: O0oOO0 . iI11I1II1I1I + ooOoO0O00
def OOoO0oO00o ( url ) :
 I1iiIi111I = xbmc . Player ( iIi ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iiIi111I . play ( url ) . strip ( )
 except : pass
 if 84 - 84: IIiI1I % ooOoO0O00
 if 62 - 62: Ii1I . oO00Oo0o000 . OoOO00O
def iIi ( ) :
 try :
  iI1I1 = getSet ( "core-player" )
  if ( iI1I1 == 'DVDPLAYER' ) : oOOoiiII = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iI1I1 == 'MPLAYER' ) : oOOoiiII = xbmc . PLAYER_CORE_MPLAYER
  elif ( iI1I1 == 'PAPLAYER' ) : oOOoiiII = xbmc . PLAYER_CORE_PAPLAYER
  else : oOOoiiII = xbmc . PLAYER_CORE_AUTO
 except : oOOoiiII = xbmc . PLAYER_CORE_AUTO
 return oOOoiiII
 return True
 if 88 - 88: ooOoO0O00
def OoO00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0ooOo0Oooo = [ ]
  if showcontext == 'fav' :
   O0ooOo0Oooo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0ooOo0Oooo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0ooOo0Oooo )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 39 - 39: OoOO00O % ooOoO0O00 . Ii1I - o0o00Oo0O
def oO0ooOoO ( name , url , mode , iconimage , fanart , description ) :
 if 65 - 65: O0O0O * O0O0O / Ii1i111I + O0O0O % O0oOO0 + OOooOOo
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 92 - 92: I11i
def I1IIiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0ooOo0Oooo = [ ]
  if showcontext == 'fav' :
   O0ooOo0Oooo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0ooOo0Oooo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0ooOo0Oooo )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = False )
 return Oo
 if 37 - 37: O0O0O
 if 18 - 18: O00Oo000ooO0 * Ii + iI11I1II1I1I % Ii1i111I + ooOoO0O00 - oO0o
 if 85 - 85: oO0o * Ii1i111I + oO0o
 if 39 - 39: I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
 if 20 - 20: i1IiIIIII * O0O0O
 if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . i1IiIIIII
def o0iI11I1II ( heading , announce ) :
 class IIiiIiIIiI1 ( ) :
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
   try : OOO = open ( announce ) ; iiiIi = OOO . read ( )
   except : iiiIi = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( iiiIi ) )
   return
 IIiiIiIIiI1 ( )
 IIiiIiIIiI1 ( )
 if 39 - 39: Ii1i111I / ii - OoOO00O + oO0o / OOooOOo
def oo0O0000oo0o0 ( ) :
 o0iI11I1II ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 32 - 32: ii / IIiI1I / oO00Oo0o000 + IIiI1I - Ii1i111I + IIiIiII11i
 if 11 - 11: ii * I11i + ii - Ii1I
 if 47 - 47: oO00Oo0o000 % i1IiIIIII * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
 if 2 - 2: oO00Oo0o000 % ii - O0oOO0 * Ii1I * O00Oo000ooO0
 if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / O0oOO0 . i1IiIIIII % oOo0O0Ooo * Ii1i111I
def Ii1IIiI1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 95 - 95: O0O0O
 if 80 - 80: O00Oo000ooO0
 if 42 - 42: ii * IIiIiII11i
 if 53 - 53: oO00Oo0o000 + ooOoO0O00 . oO0o / Ii + OoOO00O % OOooOOo
 if 9 - 9: O0oOO0 . Ii1i111I - I1ii11iIi11i . oO00Oo0o000
 if 39 - 39: i1IiIIIII
 if 70 - 70: O00Oo000ooO0 % oO0o % oOo0O0Ooo
 if 95 - 95: OOooOOo - oO00Oo0o000 / o0o00Oo0O * oOo0O0Ooo - I11i
 if 12 - 12: iI11I1II1I1I % I1ii11iIi11i . IIiI1I . O00Oo000ooO0 % Ii
 if 2 - 2: O0O0O * O0O0O . OOooOOo * OoOO00O * iI11I1II1I1I
 if 13 - 13: Ii1i111I / o0o00Oo0O . Ii * ooOoO0O00 % Ii
 if 8 - 8: OOooOOo - ii
 if 99 - 99: IIiIiII11i / O00Oo000ooO0 % ii . Ii
 if 18 - 18: I11i . O0oOO0
 if 70 - 70: ii . O0oOO0 / O0O0O . O0O0O - I11i
 if 29 - 29: Ii1i111I % i1IiIIIII - O0oOO0
 if 26 - 26: o0o00Oo0O . Ii1i111I + IIiI1I - OoOO00O . Ii1i111I
 if 2 - 2: Ii1I . I1ii11iIi11i * i1IiIIIII % IIiIiII11i . IIiI1I
 if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
 if 47 - 47: IIiI1I * OOooOOo * O00Oo000ooO0
 if 46 - 46: OoOO00O
 if 42 - 42: iI11I1II1I1I
 if 32 - 32: I1ii11iIi11i - OoOO00O . ii - ii - I1ii11iIi11i . iI11I1II1I1I
 if 34 - 34: I1ii11iIi11i
def IiI1I1i1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + Iii11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 2 - 2: O0O0O . i1IiIIIII
def ii1O0oOOo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + ii111IIiiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 98 - 98: ooOoO0O00 - IIiI1I
def iIIiII11iI1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0oI1Iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 33 - 33: I11i - O0O0O % Ii1I * Ii1i111I . ii % OoOO00O
def I1iiiiI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0oOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 11 - 11: Ii1i111I / OOooOOo
def ii1IIi1IIIIi1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + iI1i1iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 16 - 16: ooOoO0O00 * O0oOO0 % oO0o + OoOO00O
def IIIi11Ii ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oOOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 24 - 24: O00Oo000ooO0
def o0o0O00OoOo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oOO0ooO00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 56 - 56: ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
def iIIIii111 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + I1111IiII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Ii1i111I + Ii1i111I
def i1II111iiii ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + iiI11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 10 - 10: O0oOO0 - I1ii11iIi11i % IIiIiII11i
def ooi11iI1111ii1I ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OoOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 5 , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 22 - 22: Ii + OOooOOo + ii
 if 2 - 2: O0oOO0 - Ii1i111I * ooOoO0O00 % i1IiIIIII / ii * i1IiIIIII
 if 82 - 82: Ii1I . Ii1I * OoOO00O % Ii1i111I % o0o00Oo0O / I1ii11iIi11i
 if 83 - 83: oO00Oo0o000 + I11i % O0O0O / oO0o
 if 59 - 59: OoOO00O * i1IiIIIII . O00Oo000ooO0
 if 68 - 68: o0o00Oo0O * iI11I1II1I1I / oO00Oo0o000
 if 65 - 65: i1IiIIIII - oOo0O0Ooo * oO00Oo0o000
 if 99 - 99: oOo0O0Ooo
 if 64 - 64: Ii1I * OoOO00O * I1ii11iIi11i % O00Oo000ooO0 % O0oOO0
def OoO0000O ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oOOoO0 ) :
     I1I1iI = 0
     I1I1iI += len ( i1i1I )
     if I1I1iI > 0 :
      for OOO in i1i1I :
       os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
  IIIOo0O = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( IIIOo0O )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 11 - 11: o0o00Oo0O
 if 96 - 96: IIiI1I + I11i
 if 10 - 10: Ii . ii . o0o00Oo0O % O0oOO0 / oO0o
 if 36 - 36: oOo0O0Ooo % ooOoO0O00 + oO0o
 if 59 - 59: Ii - Ii + oOo0O0Ooo
 if 4 - 4: I1ii11iIi11i * o0o00Oo0O - O0O0O % O0oOO0 + OOooOOo
 if 3 - 3: OOooOOo
 if 91 - 91: o0o00Oo0O - Ii1i111I % oO00Oo0o000
 if 46 - 46: O0oOO0 / oOo0O0Ooo . O00Oo000ooO0 % oO0o / Ii
def I1III1I1IiI ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 ooooooo0oOo0 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( ooooooo0oOo0 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( ooooooo0oOo0 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 81 - 81: Ii % oOo0O0Ooo / IIiI1I % oO0o / oO00Oo0o000 % iI11I1II1I1I
   if 14 - 14: Ii1I * I1ii11iIi11i + Ii % i1IiIIIII - O0O0O
   if I1I1iI > 0 :
    if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: oO00Oo0o000 + O00Oo000ooO0 * iI11I1II1I1I
     for OOO in i1i1I :
      try :
       os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
      except :
       pass
     for o0o0 in IioO0oOOO0Ooo :
      try :
       shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      except :
       pass
       if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / OoOO00O
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  iiii1ii1 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 12 - 12: Ii - iI11I1II1I1I * O00Oo000ooO0 * IIiI1I
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iiii1ii1 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 19 - 19: o0o00Oo0O + O0O0O + I11i
   if I1I1iI > 0 :
    if 81 - 81: iI11I1II1I1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( I1I1iI ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 51 - 51: I11i . Ii1I * OoOO00O / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 44 - 44: Ii % oO00Oo0o000 % O0O0O + Ii1i111I * O0O0O . OoOO00O
   else :
    pass
  OoOo0Oooo0o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 65 - 65: OOooOOo + oO00Oo0o000 % oOo0O0Ooo
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( OoOo0Oooo0o ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 54 - 54: oO00Oo0o000 / I11i
   if I1I1iI > 0 :
    if 39 - 39: i1IiIIIII % O0O0O * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( I1I1iI ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 64 - 64: IIiIiII11i / IIiIiII11i
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 52 - 52: oO00Oo0o000 * Ii1I
   else :
    pass
    if 35 - 35: I11i % oO0o
    if 27 - 27: OoOO00O - iI11I1II1I1I * OoOO00O
    if 30 - 30: I11i + OoOO00O / ii - O00Oo000ooO0 % O0O0O
    if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 I111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( I111i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( I111i ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 19 - 19: OOooOOo * Ii1I * Ii1I / o0o00Oo0O / O0oOO0 + Ii1I
   if 48 - 48: ii . IIiI1I + o0o00Oo0O
   if I1I1iI > 0 :
    if 85 - 85: IIiIiII11i - OoOO00O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 93 - 93: O00Oo000ooO0 / Ii - O0O0O + oO0o / ooOoO0O00
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
   else :
    pass
    if 81 - 81: O0O0O / o0o00Oo0O * O0oOO0 % OOooOOo / o0o00Oo0O
    if 85 - 85: ii + ii
 iiIIii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( iiIIii1 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iiIIii1 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 45 - 45: O0O0O + I11i + O00Oo000ooO0 / OoOO00O + I11i
   if 33 - 33: IIiI1I - I1ii11iIi11i - Ii1i111I
   if I1I1iI > 0 :
    if 61 - 61: OoOO00O + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / O0O0O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: oO00Oo0o000
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 25 - 25: IIiI1I + oOo0O0Ooo + OOooOOo + oO00Oo0o000 % o0o00Oo0O
   else :
    pass
    if 26 - 26: O0oOO0 + OOooOOo
    if 17 - 17: Ii1I - IIiI1I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * i1IiIIIII
 iIi1i1iiIiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( iIi1i1iiIiiiI ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iIi1i1iiIiiiI ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 79 - 79: ii * oO00Oo0o000 - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
   if 82 - 82: OOooOOo . OoOO00O
   if I1I1iI > 0 :
    if 73 - 73: oO00Oo0o000
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: O00Oo000ooO0
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
   else :
    pass
    if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . OoOO00O - I1ii11iIi11i . Ii
    if 47 - 47: I1ii11iIi11i % oO0o - O0oOO0 - I1ii11iIi11i * O0O0O
    if 72 - 72: I11i % I11i + IIiI1I + Ii1I / I1ii11iIi11i
 IIIiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( IIIiii ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( IIIiii ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 44 - 44: O00Oo000ooO0 . Ii1i111I % oOo0O0Ooo - ooOoO0O00
   if 2 - 2: OOooOOo + OOooOOo
   if I1I1iI > 0 :
    if 47 - 47: oO0o + oO00Oo0o000 . oO00Oo0o000 * o0o00Oo0O / I1ii11iIi11i + i1IiIIIII
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 44 - 44: I11i + oO00Oo0o000 + OOooOOo * I1ii11iIi11i
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 20 - 20: O0oOO0 . Ii1i111I . Ii / I11i / oO0o . OoOO00O
   else :
    pass
    if 47 - 47: o0o00Oo0O / iI11I1II1I1I - OOooOOo + OoOO00O
    if 4 - 4: Ii1I % O0oOO0 . I1ii11iIi11i * oO0o - Ii1i111I
 iiIIii1iII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iiIIii1iII1i ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 55 - 55: Ii * o0o00Oo0O
   if 86 - 86: o0o00Oo0O + OOooOOo
   if I1I1iI > 0 :
    if 99 - 99: o0o00Oo0O + O00Oo000ooO0 + O0oOO0 - O0oOO0 * Ii1I / O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 82 - 82: I11i - i1IiIIIII
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 84 - 84: IIiI1I % ooOoO0O00 % oO0o % IIiIiII11i
   else :
    pass
    if 94 - 94: O0oOO0 * o0o00Oo0O
    if 60 - 60: IIiI1I / IIiI1I - O0oOO0 / ii + o0o00Oo0O
 oOoooO0oo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oOoooO0oo0 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 44 - 44: OOooOOo . oO00Oo0o000 . ooOoO0O00 . OOooOOo * O0oOO0
   if 59 - 59: IIiIiII11i * ii - ii
   if I1I1iI > 0 :
    if 33 - 33: o0o00Oo0O . Ii % I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 50 - 50: O0oOO0
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * i1IiIIIII
   else :
    pass
    if 83 - 83: Ii - oOo0O0Ooo * Ii
    if 59 - 59: IIiI1I - ii / O0oOO0 + Ii1I . I11i - IIiI1I
 iiI1iI1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iiI1iI1i1 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 67 - 67: I1ii11iIi11i % IIiIiII11i - oO0o % ooOoO0O00 % O0oOO0
   if 31 - 31: iI11I1II1I1I / ii
   if I1I1iI > 0 :
    if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + OoOO00O . i1IiIIIII
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 58 - 58: iI11I1II1I1I + oO00Oo0o000 - Ii1I - ooOoO0O00 * OOooOOo
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 4 - 4: ii
   else :
    pass
    if 7 - 7: O00Oo000ooO0
    if 26 - 26: i1IiIIIII + I1ii11iIi11i
 oo0iI1i11II1i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oo0iI1i11II1i1i ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 61 - 61: Ii1i111I * OoOO00O + Ii1i111I - I1ii11iIi11i % OOooOOo . IIiI1I
   if 51 - 51: i1IiIIIII / Ii1i111I
   if I1I1iI > 0 :
    if 51 - 51: O0oOO0 * O0O0O - oO00Oo0o000 + IIiI1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: I11i - Ii % oO0o / OoOO00O - OOooOOo
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 88 - 88: O0O0O * oOo0O0Ooo / oO0o - i1IiIIIII / ooOoO0O00 . oO00Oo0o000
   else :
    pass
    if 26 - 26: Ii - O0oOO0
    if 45 - 45: O0oOO0 + IIiIiII11i % IIiI1I
 o00OoOo0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o00OoOo0 ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 22 - 22: iI11I1II1I1I / O0oOO0 / oOo0O0Ooo - I11i
   if 21 - 21: O0O0O . Ii * Ii1i111I . i1IiIIIII / i1IiIIIII
   if I1I1iI > 0 :
    if 42 - 42: ii / oO00Oo0o000 . I11i / o0o00Oo0O - O00Oo000ooO0 * O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: OoOO00O % oO00Oo0o000
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 97 - 97: OOooOOo
   else :
    pass
    if 13 - 13: OOooOOo % i1IiIIIII . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
    if 19 - 19: oO00Oo0o000 % O0oOO0 - O0oOO0 % oOo0O0Ooo . i1IiIIIII - ii
 OOO0oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( OOO0oO ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 82 - 82: O0O0O / OoOO00O
   if 75 - 75: O0oOO0
   if I1I1iI > 0 :
    if 23 - 23: OOooOOo * I1ii11iIi11i % ii - Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 46 - 46: I1ii11iIi11i
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 99 - 99: oO0o - O0oOO0 * o0o00Oo0O * Ii1I * iI11I1II1I1I - iI11I1II1I1I
   else :
    pass
    if 50 - 50: oOo0O0Ooo % Ii - oOo0O0Ooo * IIiI1I / O00Oo000ooO0 / o0o00Oo0O
    if 31 - 31: IIiIiII11i . ii + oO0o + I11i . oOo0O0Ooo . IIiIiII11i
 I111I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iiIIii1iII1i ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( I111I ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 86 - 86: IIiIiII11i . O00Oo000ooO0 + ii
   if 22 - 22: IIiIiII11i / Ii1I * O00Oo000ooO0 - I11i % Ii1I
   if I1I1iI > 0 :
    if 70 - 70: IIiIiII11i - O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: oO00Oo0o000
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 43 - 43: o0o00Oo0O / oO00Oo0o000 . iI11I1II1I1I - OOooOOo
   else :
    pass
    if 47 - 47: IIiIiII11i - Ii1I - OoOO00O
    if 9 - 9: Ii1I - O00Oo000ooO0
    if 64 - 64: ooOoO0O00
 o0O0oOo00oOoo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oOOO0oo0iI1IiiiiI = os . path . join ( o0O0oOo00oOoo , "cache.db" )
   os . unlink ( oOOO0oo0iI1IiiiiI )
   if 12 - 12: Ii . Ii1i111I * i1IiIIIII % ooOoO0O00 . O0oOO0
 except :
  pass
  if 58 - 58: IIiI1I % iI11I1II1I1I . iI11I1II1I1I / Ii1i111I
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 79 - 79: oO0o / i1IiIIIII - ooOoO0O00 + ooOoO0O00 - O00Oo000ooO0 + O00Oo000ooO0
 if 67 - 67: oO0o * oO0o / ii
 if 79 - 79: I11i % iI11I1II1I1I / IIiIiII11i / OoOO00O / OoOO00O + o0o00Oo0O
 if 46 - 46: ooOoO0O00 / O00Oo000ooO0
 if 84 - 84: OOooOOo / iI11I1II1I1I + O0O0O % O0oOO0 + O0O0O - iI11I1II1I1I
 if 27 - 27: o0o00Oo0O / I11i * oOo0O0Ooo
 if 41 - 41: O0oOO0
 if 11 - 11: ooOoO0O00 / oO00Oo0o000 * Ii1I * oO00Oo0o000 * O0oOO0 - Ii
 if 96 - 96: Ii1I % Ii1I
def ii1II11IIII1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( I1IIII ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 69 - 69: O00Oo000ooO0
   if 24 - 24: oO0o / o0o00Oo0O * O0oOO0 % iI11I1II1I1I + ooOoO0O00 % o0o00Oo0O
   if I1I1iI > 0 :
    if 26 - 26: O0oOO0 + O00Oo000ooO0 - o0o00Oo0O * O0O0O * IIiIiII11i . Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: OOooOOo / ii / Ii1i111I % OOooOOo * OoOO00O * O00Oo000ooO0
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
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
 if 11 - 11: Ii1I / i1IiIIIII . OoOO00O * Ii1I
 if 17 - 17: Ii1I * ii % ooOoO0O00 % ii . IIiI1I
 if 20 - 20: oO0o . O0O0O
 if 4 - 4: I1ii11iIi11i % OoOO00O % oO0o * IIiI1I % ii
 if 38 - 38: ii . IIiI1I
 if 43 - 43: ii
 if 8 - 8: i1IiIIIII + Ii1i111I . Ii1i111I
 if 89 - 89: Ii1I * Ii1I * OOooOOo / IIiI1I
 if 60 - 60: oO0o / IIiI1I / oOo0O0Ooo + O0O0O
def iiII ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 I1IIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( I1IIII ) :
   I1I1iI = 0
   I1I1iI += len ( i1i1I )
   if 93 - 93: ii * OoOO00O / o0o00Oo0O + OoOO00O - iI11I1II1I1I
   if 6 - 6: O00Oo000ooO0 - I1ii11iIi11i - Ii1i111I - o0o00Oo0O % ii
   if I1I1iI > 0 :
    if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( I1I1iI ) + " files found" , "Do you want to delete them?" ) :
     if 27 - 27: Ii % IIiI1I + OoOO00O . i1IiIIIII
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
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
 I1III1I1IiI ( url )
 return
 if 9 - 9: oO0o
 if 43 - 43: OoOO00O . i1IiIIIII + oOo0O0Ooo * Ii
 if 2 - 2: i1IiIIIII
 if 3 - 3: oOo0O0Ooo . IIiI1I % o0o00Oo0O - O0oOO0 / o0o00Oo0O
 if 79 - 79: OoOO00O + O0O0O % O0oOO0 % oOo0O0Ooo
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: IIiI1I . O0O0O / I1ii11iIi11i . oO0o . Ii
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
def I11Ii1 ( url , name ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0OOO = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 OoooooO0oOOoO = os . path . join ( O0000OOO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OoooooO0oOOoO ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oO0OOO = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
   try :
    os . remove ( oO0OOO )
    print '=== GenieTv - REMOVING    ' + str ( oO0OOO ) + '    ==='
   except :
    pass
   O00oO = i1 . http_GET ( url ) . content
   ii1 = open ( oO0OOO , "w" )
   ii1 . write ( O00oO )
   ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oO0OOO ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oO0OOO = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
  try :
   os . remove ( oO0OOO )
   print '=== GenieTv - REMOVING    ' + str ( oO0OOO ) + '    ==='
  except :
   pass
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oO0OOO , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0OOO ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 26 - 26: oO00Oo0o000 / oO00Oo0o000 + I1ii11iIi11i - I11i % IIiIiII11i . ii
def IiiI11Iii ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0OOO = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 try :
  ii1 = open ( oO0OOO ) . read ( )
  if 'zero' in ii1 :
   name = '0CACHE'
  elif 'tuxen' in ii1 :
   name = 'TUXENS'
  elif 'muckys' in ii1 :
   name = 'MUCKYS'
  elif 'p2p1' in ii1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ii1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ii1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 42 - 42: Ii1i111I + ooOoO0O00 - OoOO00O / O00Oo000ooO0 . IIiI1I
def II111i ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0OOO = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 try :
  os . remove ( oO0OOO )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oO0OOO ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 41 - 41: oOo0O0Ooo % i1IiIIIII
 if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % oO00Oo0o000
 if 78 - 78: Ii1I + ii - oOo0O0Ooo * OOooOOo * IIiI1I
 if 7 - 7: i1IiIIIII . O00Oo000ooO0 . oO00Oo0o000 / OoOO00O / I1ii11iIi11i
 if 83 - 83: Ii1i111I / I1ii11iIi11i
 if 23 - 23: iI11I1II1I1I
 if 10 - 10: Ii1i111I - I11i % ii - Ii1I
 if 64 - 64: oO0o / oOo0O0Ooo
 if 23 - 23: Ii1i111I * oO00Oo0o000 * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: O00Oo000ooO0 * ii . O0oOO0 % Ii
def IiIoO0oo0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o0O00oOoOO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for IiIiI1 , iiiI1 , III1 , Oo00OO in o0O00oOoOO :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IiIiI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % III1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % Oo00OO )
  inc = inc + 1
  if 8 - 8: oO0o + oO00Oo0o000 . i1IiIIIII
  if 86 - 86: oO0o - Ii1i111I
  if 83 - 83: oOo0O0Ooo % I1ii11iIi11i + OoOO00O + Ii
  if 70 - 70: iI11I1II1I1I
  if 79 - 79: Ii
  if 20 - 20: ooOoO0O00 - O00Oo000ooO0 + O00Oo000ooO0 . ii . oOo0O0Ooo + Ii1i111I
  if 10 - 10: O00Oo000ooO0 / I1ii11iIi11i
  if 82 - 82: Ii1I / IIiI1I + Ii1I + oO00Oo0o000
  if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / O0oOO0 % oOo0O0Ooo % ooOoO0O00
def OOOoOOooO0 ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oO0OOO = os . path . join ( O0000OOO0 , 'addons2.ini' )
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oO0OOO , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0OOO ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 2 - 2: O0oOO0 - o0o00Oo0O - Ii1I / Ii1i111I * OOooOOo
def III1II ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oO0OOO = os . path . join ( O0000OOO0 , 'settings.xml' )
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oO0OOO , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0OOO ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 81 - 81: IIiI1I - OoOO00O - i1IiIIIII % O00Oo000ooO0 % I11i . iI11I1II1I1I
 if 79 - 79: Ii1I - Ii1I . OoOO00O / O00Oo000ooO0
def O00o00o00OO0 ( ) :
 try :
  IIII1IiiI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IIII1IiiI ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ooO0O0OOO = os . path . join ( IIII1IiiI , "source.db" )
    os . unlink ( ooO0O0OOO )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 2 - 2: Ii / oO0o + O0oOO0 - Ii1I * oO0o
 if 3 - 3: oO0o % I11i % i1IiIIIII . Ii1I . Ii1I
 if 35 - 35: ooOoO0O00 * IIiI1I - IIiI1I . O00Oo000ooO0
 if 77 - 77: oOo0O0Ooo / iI11I1II1I1I * OoOO00O * iI11I1II1I1I + Ii1I
 if 78 - 78: O00Oo000ooO0 / IIiI1I * OoOO00O . i1IiIIIII . O0O0O - oO00Oo0o000
def Iiii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 39 - 39: O0oOO0 . ooOoO0O00 + ii . IIiI1I - Ii % oO00Oo0o000
 if 38 - 38: O0O0O
 if 9 - 9: Ii1i111I . oO0o . O0O0O / ii
 if 59 - 59: iI11I1II1I1I + ooOoO0O00 % IIiIiII11i
 if 2 - 2: IIiIiII11i + Ii1i111I . oO0o
 if 14 - 14: i1IiIIIII * oOo0O0Ooo - Ii1I
 if 10 - 10: IIiI1I % oO00Oo0o000 * Ii1I * o0o00Oo0O * Ii % oO00Oo0o000
def ooOoo0O0o0OO0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i11iiIiI11iII = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i11iiIiI11iII :
  oO0OIiIi1ii1Ii = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oO0OIiIi1ii1Ii = xbmc . translatePath ( oO0OIiIi1ii1Ii ) ;
  i1II111II1 = os . path . join ( oO0OIiIi1ii1Ii , ".." , ".." ) ; i1II111II1 = os . path . abspath ( i1II111II1 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + i1II111II1 ) ; I11I1iiI1 = False
  try :
   for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( i1II111II1 , topdown = True ) :
    IioO0oOOO0Ooo [ : ] = [ o0o0 for o0o0 in IioO0oOOO0Ooo if o0o0 not in iiIIIII1i1iI ]
    for II1i11I in i1i1I :
     try : os . remove ( os . path . join ( OOo0Oo0OOo0 , II1i11I ) )
     except :
      if II1i11I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : I11I1iiI1 = True
      plugintools . log ( "Error removing " + OOo0Oo0OOo0 + " " + II1i11I )
    for II1i11I in IioO0oOOO0Ooo :
     try : os . rmdir ( os . path . join ( OOo0Oo0OOo0 , II1i11I ) )
     except :
      if II1i11I not in [ "Database" , "userdata" ] : I11I1iiI1 = True
      plugintools . log ( "Error removing " + OOo0Oo0OOo0 + " " + II1i11I )
   if not I11I1iiI1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0Oii1111i ( )
 if 18 - 18: OOooOOo % O0O0O % oO0o / IIiI1I
 if 88 - 88: IIiI1I * i1IiIIIII / Ii / ooOoO0O00
 if 76 - 76: OoOO00O . Ii1i111I - i1IiIIIII + OOooOOo * oO0o % oO00Oo0o000
def ii1IiIi1iIi ( ) :
 IIiI111Iii = [ ]
 OOiIiI1iI = sys . argv [ 2 ]
 if len ( OOiIiI1iI ) >= 2 :
  ooo0oooO = sys . argv [ 2 ]
  O0O0Ooo0 = ooo0oooO . replace ( '?' , '' )
  if ( ooo0oooO [ len ( ooo0oooO ) - 1 ] == '/' ) :
   ooo0oooO = ooo0oooO [ 0 : len ( ooo0oooO ) - 2 ]
  IIIiIII1 = O0O0Ooo0 . split ( '&' )
  IIiI111Iii = { }
  for o0I1IIIi11ii11 in range ( len ( IIIiIII1 ) ) :
   OOo0OOo = { }
   OOo0OOo = IIIiIII1 [ o0I1IIIi11ii11 ] . split ( '=' )
   if ( len ( OOo0OOo ) ) == 2 :
    IIiI111Iii [ OOo0OOo [ 0 ] ] = OOo0OOo [ 1 ]
    if 77 - 77: O0O0O . OoOO00O / o0o00Oo0O * O0O0O
 return IIiI111Iii
 if 98 - 98: I1ii11iIi11i - O0O0O . oO00Oo0o000
O0oo0O0oO00O0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
II1IIIiiI11 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O0O0oOo0o0o0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oOOO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OOo00O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Iii111111 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
Iii11I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1IiIi11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ii111IIiiiiI = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0oI1Iii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0oOOO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iI1i1iii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOOooo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oOO0ooO00o = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1111IiII1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iiI11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooOoOo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1i1I1i1i1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o00o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OO0O0o0o0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0O0OOooOO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
II1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OoOo0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O00O0 = base64 . decodestring ( 'Q1VOVA==' )
def o0OOOO00O0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0ooOo0Oooo = [ ]
  if showcontext == 'fav' :
   O0ooOo0Oooo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0ooOo0Oooo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0ooOo0Oooo )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 35 - 35: iI11I1II1I1I % oO00Oo0o000 * Ii1i111I . I1ii11iIi11i
def OOooOoooOoOo ( name , url , mode , iconimage , fanart , description ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = False )
 return Oo
 if 3 - 3: O0oOO0 - Ii1I * oOo0O0Ooo . OOooOOo
 if 69 - 69: ii / iI11I1II1I1I - I11i % oO00Oo0o000 - iI11I1II1I1I
ooo0oooO = ii1IiIi1iIi ( )
Ooo00OoOOO = None
II1i11I = None
OOoooooooO = None
o00OooO0oo = None
o0o0oOoOO0O = None
iiIi1i = None
iIOo0oo = None
if 33 - 33: oOo0O0Ooo / Ii1i111I . I1ii11iIi11i
if 89 - 89: IIiI1I + ooOoO0O00 - O00Oo000ooO0 + O0oOO0 . IIiIiII11i
try :
 iIOo0oo = int ( ooo0oooO [ "fav_mode" ] )
except :
 pass
 if 85 - 85: iI11I1II1I1I - OoOO00O * I1ii11iIi11i . O0O0O + oO00Oo0o000
try :
 Ooo00OoOOO = urllib . unquote_plus ( ooo0oooO [ "url" ] )
except :
 pass
try :
 II1i11I = urllib . unquote_plus ( ooo0oooO [ "name" ] )
except :
 pass
try :
 o00OooO0oo = urllib . unquote_plus ( ooo0oooO [ "iconimage" ] )
except :
 pass
try :
 OOoooooooO = int ( ooo0oooO [ "mode" ] )
except :
 pass
try :
 o0o0oOoOO0O = urllib . unquote_plus ( ooo0oooO [ "fanart" ] )
except :
 pass
try :
 iiIi1i = urllib . unquote_plus ( ooo0oooO [ "description" ] )
except :
 pass
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IIiI1I / IIiI1I
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OOoooooooO )
print "URL: " + str ( Ooo00OoOOO )
print "Name: " + str ( II1i11I )
print "IconImage: " + str ( o00OooO0oo )
if 43 - 43: oOo0O0Ooo
if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
def oO00OOoO00 ( content , viewType ) :
 if 34 - 34: I11i % Ii1I + OoOO00O * Ii1i111I / O0O0O
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 18 - 18: O0oOO0
if o00OooO0oo == None : o00OooO0oo = ii11iIi1I
if o0o0oOoOO0O == None : o0o0oOoOO0O = i1iIIi1
if OOoooooooO == None :
 iiIiI ( )
 if 92 - 92: oO0o % iI11I1II1I1I / O00Oo000ooO0 * IIiI1I . ooOoO0O00 + O0O0O
elif OOoooooooO == 1 :
 II1i111 ( Ooo00OoOOO )
 if 24 - 24: O00Oo000ooO0 . IIiI1I * O00Oo000ooO0 % Ii . Ii + ooOoO0O00
elif OOoooooooO == 44 :
 OO0OoOOO0 ( Ooo00OoOOO )
 if 64 - 64: iI11I1II1I1I / O00Oo000ooO0 / I1ii11iIi11i - Ii1I
elif OOoooooooO == 2 :
 IiI1 ( )
 if 100 - 100: O00Oo000ooO0 + ooOoO0O00 * oO0o
elif OOoooooooO == 3 :
 oOO ( )
 if 64 - 64: O0O0O * Ii . I1ii11iIi11i
elif OOoooooooO == 21 :
 iI1Ii11111iIi ( )
 if 52 - 52: I1ii11iIi11i / O0oOO0 / IIiI1I - I11i / IIiI1I
elif OOoooooooO == 4 :
 IiI1iII1II111 ( )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif OOoooooooO == 5 :
 oOO0oo ( Ooo00OoOOO )
 if 85 - 85: oOo0O0Ooo
elif OOoooooooO == 6 :
 ii1II11IIII1 ( Ooo00OoOOO )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif OOoooooooO == 7 :
 I11Ii1 ( Ooo00OoOOO , II1i11I )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif OOoooooooO == 8 :
 IiiI11Iii ( Ooo00OoOOO , II1i11I )
 if 46 - 46: OOooOOo * Ii1i111I / O0O0O + I1ii11iIi11i + O00Oo000ooO0
elif OOoooooooO == 9 :
 FIXREPOSADDONS ( Ooo00OoOOO )
 if 95 - 95: I11i - OoOO00O
elif OOoooooooO == 10 :
 Ii1IIiI1i ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif OOoooooooO == 11 :
 II111i ( Ooo00OoOOO )
 if 19 - 19: OOooOOo . i1IiIIIII . ii
elif OOoooooooO == 12 :
 IiIoO0oo0 ( )
 if 79 - 79: i1IiIIIII * O0oOO0 * oOo0O0Ooo * Ii1I / Ii1I
elif OOoooooooO == 13 :
 OoO0000O ( )
 if 62 - 62: O0oOO0 * OoOO00O % Ii1I - ooOoO0O00 - Ii1I
elif OOoooooooO == 14 :
 I1III1I1IiI ( Ooo00OoOOO )
 if 24 - 24: i1IiIIIII
elif OOoooooooO == 15 :
 II11i11Iii ( )
 if 71 - 71: O00Oo000ooO0 - ooOoO0O00
elif OOoooooooO == 16 :
 OOOoOOooO0 ( Ooo00OoOOO , II1i11I )
 if 56 - 56: OOooOOo + O0O0O
elif OOoooooooO == 17 :
 III1II ( Ooo00OoOOO , II1i11I )
 if 74 - 74: IIiI1I / oO00Oo0o000 / IIiIiII11i - IIiI1I / O0O0O % Ii1i111I
elif OOoooooooO == 18 :
 O00o00o00OO0 ( )
 if 19 - 19: O00Oo000ooO0 % ii + ii
elif OOoooooooO == 19 :
 I11iiIi1i1 ( Ooo00OoOOO )
 if 7 - 7: ooOoO0O00
elif OOoooooooO == 40 :
 ooOo0OoOooo00 ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 91 - 91: OOooOOo - OOooOOo . O00Oo000ooO0
elif OOoooooooO == 42 :
 IIo0OoO00 ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 33 - 33: oO00Oo0o000 - iI11I1II1I1I / OoOO00O % o0o00Oo0O
elif OOoooooooO == 43 :
 ooooOooooOOo ( Ooo00OoOOO )
 if 80 - 80: O00Oo000ooO0 % ii - O00Oo000ooO0
elif OOoooooooO == 20 :
 O0o0O0OO00o ( Ooo00OoOOO )
 if 27 - 27: oO00Oo0o000 - I11i * Ii1I - oOo0O0Ooo
elif OOoooooooO == 22 :
 IiI1I1i1 ( Ooo00OoOOO )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIiI1I . OoOO00O
elif OOoooooooO == 23 :
 ii1O0oOOo ( Ooo00OoOOO )
 if 100 - 100: IIiIiII11i / oO00Oo0o000 / IIiI1I - Ii1I * iI11I1II1I1I
elif OOoooooooO == 24 :
 iIIiII11iI1 ( Ooo00OoOOO )
 if 7 - 7: ooOoO0O00 . O00Oo000ooO0 % Ii * Ii1I . Ii1i111I % Ii1I
elif OOoooooooO == 25 :
 I1iiiiI ( Ooo00OoOOO )
 if 35 - 35: oOo0O0Ooo
elif OOoooooooO == 26 :
 ii1IIi1IIIIi1 ( Ooo00OoOOO )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif OOoooooooO == 27 :
 IIIi11Ii ( Ooo00OoOOO )
 if 22 - 22: O0oOO0 . Ii . ii . ooOoO0O00
elif OOoooooooO == 28 :
 o0o0O00OoOo ( Ooo00OoOOO )
 if 12 - 12: OOooOOo % i1IiIIIII + O0O0O . o0o00Oo0O % iI11I1II1I1I
elif OOoooooooO == 29 :
 iIIIii111 ( Ooo00OoOOO )
 if 41 - 41: ii
elif OOoooooooO == 30 :
 o0O0 ( Ooo00OoOOO )
 if 13 - 13: Ii1i111I + oO00Oo0o000 - oO00Oo0o000 % O0O0O / Ii1i111I
elif OOoooooooO == 31 :
 i1II111iiii ( Ooo00OoOOO )
 if 4 - 4: oOo0O0Ooo + i1IiIIIII - O00Oo000ooO0 + IIiI1I
elif OOoooooooO == 32 :
 i11111I1IOoo0ooOOOOoOo ( )
 if 78 - 78: OoOO00O
elif OOoooooooO == 33 :
 Iii111Ii ( )
 if 29 - 29: IIiIiII11i
elif OOoooooooO == 35 :
 Oo0 ( Ooo00OoOOO )
 if 79 - 79: iI11I1II1I1I - Ii + O0oOO0 - IIiIiII11i . iI11I1II1I1I
elif OOoooooooO == 34 :
 oooOO0OO0O ( Ooo00OoOOO )
 if 84 - 84: I1ii11iIi11i % Ii1i111I * o0o00Oo0O * Ii1i111I
elif OOoooooooO == 36 :
 IIiiIIIi ( Ooo00OoOOO )
 if 66 - 66: i1IiIIIII / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0oOO0
elif OOoooooooO == 37 :
 iIIiI1I1i ( Ooo00OoOOO )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif OOoooooooO == 38 :
 I111IIiii1Ii ( Ooo00OoOOO )
 if 37 - 37: ooOoO0O00 * Ii
elif OOoooooooO == 41 :
 ooOoo0O0o0OO0 ( ooo0oooO )
 if 95 - 95: Ii % oO00Oo0o000 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif OOoooooooO == 39 :
 ooi11iI1111ii1I ( Ooo00OoOOO )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / i1IiIIIII / oO00Oo0o000
elif OOoooooooO == 45 :
 TEXTS ( )
 if 35 - 35: IIiI1I * i1IiIIIII
elif OOoooooooO == 46 :
 oo0O0000oo0o0 ( )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif OOoooooooO == 47 :
 GEVID ( )
 if 13 - 13: oO0o * oO00Oo0o000 + I1ii11iIi11i - O00Oo000ooO0
elif OOoooooooO == 48 :
 OoOO ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 31 - 31: oO0o
elif OOoooooooO == 49 :
 ooO00O0O0 ( )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif OOoooooooO == 222 :
 Iiii1iI1i ( Ooo00OoOOO )
 if 77 - 77: Ii - oO00Oo0o000 . Ii1I % I1ii11iIi11i . OoOO00O
elif OOoooooooO == 333 :
 iIi1 ( Ooo00OoOOO )
 if 9 - 9: I11i
 if 55 - 55: i1IiIIIII % iI11I1II1I1I + Ii1i111I . O0oOO0
elif OOoooooooO == 1020 :
 oo0OO0oOo ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif OOoooooooO == 1021 :
 ANIMEEP ( )
 if 23 - 23: Ii
elif OOoooooooO == 1022 :
 ANIMEPLAY ( Ooo00OoOOO )
 if 88 - 88: IIiIiII11i - IIiI1I / ii
elif OOoooooooO == 1001 :
 oo0OoO ( )
 if 71 - 71: Ii1I
elif OOoooooooO == 1005 :
 I11II ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OOoooooooO == 1007 :
 OOOO0 ( Ooo00OoOOO )
 if 1 - 1: O00Oo000ooO0 % ooOoO0O00
elif OOoooooooO == 1010 :
 II1i1 ( Ooo00OoOOO )
 if 41 - 41: oO0o * oO0o / IIiI1I + Ii1I . I11i
elif OOoooooooO == 1011 :
 I1I11 ( Ooo00OoOOO )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / OoOO00O
elif OOoooooooO == 1012 :
 IIi1I1 ( Ooo00OoOOO )
 if 80 - 80: Ii1I
elif OOoooooooO == 1030 :
 i1iiiiIIIi ( )
 if 67 - 67: IIiIiII11i
elif OOoooooooO == 1031 :
 Ii11Ii1 ( Ooo00OoOOO , o00OooO0oo )
 if 2 - 2: I11i - o0o00Oo0O * OoOO00O % O00Oo000ooO0
elif OOoooooooO == 1032 :
 oO00OO0o0ooO ( Ooo00OoOOO )
 if 64 - 64: ooOoO0O00 . O0oOO0
elif OOoooooooO == 1006 :
 Parse . ParseURL ( Ooo00OoOOO )
 if 7 - 7: O0O0O . IIiI1I - IIiI1I / oO00Oo0o000 % I1ii11iIi11i
elif OOoooooooO == 2030 :
 Parse . addonParseURL ( Ooo00OoOOO )
 if 61 - 61: O0O0O - Ii1I / IIiI1I % Ii1I + oO0o / I1ii11iIi11i
elif OOoooooooO == 2031 :
 Parse . apkParseURL ( Ooo00OoOOO )
 if 10 - 10: Ii / OOooOOo
elif OOoooooooO == 1002 :
 o0000OOOo ( Ooo00OoOOO )
 if 27 - 27: oOo0O0Ooo / ii
elif OOoooooooO == 1003 :
 oo0oOO ( Ooo00OoOOO , o00OooO0oo )
 if 74 - 74: Ii1I % oO00Oo0o000 - oO0o * Ii1i111I . ii * oO0o
elif OOoooooooO == 1004 :
 O000oOOoOOO ( Ooo00OoOOO )
 if 99 - 99: OOooOOo . IIiI1I - ii - o0o00Oo0O
elif OOoooooooO == 1008 :
 iio00O0o00oo ( )
 if 6 - 6: i1IiIIIII
elif OOoooooooO == 1009 :
 OoOO0OO0O0o ( Ooo00OoOOO )
 if 3 - 3: o0o00Oo0O - oO00Oo0o000 * OoOO00O * i1IiIIIII / OoOO00O
elif OOoooooooO == 2001 :
 iIii1iIiII1i1 ( )
 if 58 - 58: OoOO00O * iI11I1II1I1I + O0oOO0 . O0oOO0
elif OOoooooooO == 2002 :
 Ii111Ii1iiIi1 ( Ooo00OoOOO )
 if 74 - 74: O0oOO0 - I11i * O00Oo000ooO0 % O0oOO0
elif OOoooooooO == 1013 :
 iI ( )
elif OOoooooooO == 10111113 :
 i1oOOOOOOOoO ( Ooo00OoOOO )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * oO00Oo0o000 - oO0o - I11i
elif OOoooooooO == 1014 :
 i1I1iiii1Ii11 ( )
 if 44 - 44: ii
elif OOoooooooO == 1015 :
 IiIIIIi ( Ooo00OoOOO )
 if 82 - 82: OOooOOo . OOooOOo
elif OOoooooooO == 1016 :
 Oo00O00o0 ( Ooo00OoOOO , o00OooO0oo , II1i11I )
 if 10 - 10: I1ii11iIi11i * Ii1I . O0O0O . ii . i1IiIIIII * Ii1I
elif OOoooooooO == 1017 :
 o0O0o0 ( )
 if 80 - 80: oO00Oo0o000 + Ii1i111I . oO00Oo0o000 + i1IiIIIII
elif OOoooooooO == 1023 :
 ii1ii11 ( )
 if 85 - 85: Ii . Ii1i111I + OoOO00O / OoOO00O
elif OOoooooooO == 1024 :
 oOOo0OOoOO0 ( Ooo00OoOOO )
 if 43 - 43: O00Oo000ooO0 . ii - IIiIiII11i
elif OOoooooooO == 1025 :
 IiIiIIi1IiiIi1III ( Ooo00OoOOO )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * i1IiIIIII * O0O0O
elif OOoooooooO == 4001 :
 I11IiI ( )
 if 19 - 19: oO00Oo0o000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OOoooooooO == 4002 :
 ooO0oOOooOo0 ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OOoooooooO == 4003 :
 OOO0oOoO0O ( )
 if 15 - 15: OoOO00O + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OOoooooooO == 4004 :
 oOo00oOoO000 ( )
 if 54 - 54: O00Oo000ooO0 - IIiIiII11i . O0oOO0 + OoOO00O
elif OOoooooooO == 4005 :
 Ii1iI1I1 ( )
 if 45 - 45: O0O0O + IIiIiII11i . IIiI1I / Ii1I
elif OOoooooooO == 4006 :
 oooOo0OOOoo0 ( )
 if 76 - 76: OoOO00O + IIiI1I - O00Oo000ooO0 * iI11I1II1I1I % ooOoO0O00
elif OOoooooooO == 4007 :
 OOoOO0o0o0 ( )
 if 72 - 72: O0oOO0 + IIiIiII11i . o0o00Oo0O - IIiI1I / ii . oO00Oo0o000
elif OOoooooooO == 4008 :
 ii1I1 ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OOoooooooO == 4009 : OOooo0oOO0O ( )
elif OOoooooooO == 4010 : IIiiI ( )
elif OOoooooooO == 3000 :
 o0oOOO ( )
 if 32 - 32: ii
elif OOoooooooO == 3001 :
 iIiI1i111ii ( )
 if 29 - 29: Ii1I
elif OOoooooooO == 3002 :
 IiIo000OOO00O ( Ooo00OoOOO )
 if 41 - 41: OoOO00O
elif OOoooooooO == 3003 :
 O0oooo000oO0 ( Ooo00OoOOO )
 if 49 - 49: OoOO00O % IIiIiII11i . OoOO00O - I11i - Ii1i111I * O00Oo000ooO0
elif OOoooooooO == 3004 :
 oOoO00O ( Ooo00OoOOO )
 if 47 - 47: o0o00Oo0O . I11i / OoOO00O * IIiI1I
elif OOoooooooO == 404 :
 i1iIII1IIi ( II1i11I , Ooo00OoOOO , o00OooO0oo )
 if 63 - 63: oO00Oo0o000 - O0O0O - IIiI1I - O0oOO0 / O0O0O + oO0o
elif OOoooooooO == 405 :
 ooOoo000 ( Ooo00OoOOO )
 if 94 - 94: O00Oo000ooO0 / oOo0O0Ooo . IIiIiII11i
elif OOoooooooO == 7030 :
 i1111I ( )
 if 32 - 32: O0O0O . i1IiIIIII % i1IiIIIII . OOooOOo
elif OOoooooooO == 7021 :
 Ii1i ( II1i11I )
 if 37 - 37: i1IiIIIII + o0o00Oo0O + i1IiIIIII . IIiI1I . I11i
elif OOoooooooO == 7022 :
 IiI1I1IIIi1i ( II1i11I )
 if 78 - 78: oOo0O0Ooo / Ii1i111I + I11i . I1ii11iIi11i / o0o00Oo0O
elif OOoooooooO == 7000 :
 Ii1iIIi11 ( II1i11I , Ooo00OoOOO , img )
 if 49 - 49: Ii1I
elif OOoooooooO == 7050 :
 oOOoo ( Ooo00OoOOO )
 if 66 - 66: I11i . Ii1I
elif OOoooooooO == 7051 :
 oOo0Oo00O ( Ooo00OoOOO )
 if 18 - 18: I1ii11iIi11i + O00Oo000ooO0
elif OOoooooooO == 7052 :
 ooO ( Ooo00OoOOO )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % OoOO00O . oOo0O0Ooo
elif OOoooooooO == 7053 :
 i1i1i11iI11II ( Ooo00OoOOO )
 if 43 - 43: oOo0O0Ooo % Ii1I * OoOO00O
elif OOoooooooO == 7054 :
 CoolPlay ( Ooo00OoOOO )
 if 31 - 31: OoOO00O / IIiI1I
elif OOoooooooO == 7060 :
 IiiI111 ( )
 if 3 - 3: O00Oo000ooO0
elif OOoooooooO == 7061 :
 O0oo0O0OO0Oo ( Ooo00OoOOO )
 if 37 - 37: OoOO00O * ii * Ii1i111I + I1ii11iIi11i . oOo0O0Ooo
elif OOoooooooO == 7063 :
 O0OOOo0Oo0 ( Ooo00OoOOO )
 if 61 - 61: i1IiIIIII . i1IiIIIII
elif OOoooooooO == 7062 :
 oO00o0O0Ooo ( Ooo00OoOOO )
 if 17 - 17: IIiIiII11i / O0oOO0
elif OOoooooooO == 7064 :
 NATatozcat ( )
 if 80 - 80: i1IiIIIII * oO0o + OoOO00O
elif OOoooooooO == 7067 :
 ii11 ( Ooo00OoOOO )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif OOoooooooO == 7066 :
 NATatozA ( Ooo00OoOOO )
 if 98 - 98: I11i * I1ii11iIi11i - OoOO00O . O0oOO0
elif OOoooooooO == 7065 :
 I1i11IIIi ( Ooo00OoOOO )
 if 2 - 2: I1ii11iIi11i - O0oOO0 % iI11I1II1I1I
elif OOoooooooO == 7070 :
 IIoO ( )
 if 88 - 88: oO00Oo0o000 - oO0o
elif OOoooooooO == 7071 :
 DIZIlist ( Ooo00OoOOO )
 if 79 - 79: IIiI1I
elif OOoooooooO == 7072 :
 DIZIpull ( Ooo00OoOOO )
 if 45 - 45: IIiIiII11i + IIiI1I . Ii1i111I . o0o00Oo0O * ooOoO0O00 - OoOO00O
elif OOoooooooO == 7073 :
 WATCHDIZI ( Ooo00OoOOO )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif OOoooooooO == 7002 :
 I1i1ii1ii ( )
 if 76 - 76: Ii1I
elif OOoooooooO == 7003 :
 iII ( Ooo00OoOOO )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . OoOO00O
elif OOoooooooO == 7004 :
 Iii1 ( Ooo00OoOOO )
 if 51 - 51: OoOO00O + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OOoooooooO == 7020 :
 I1o0 ( Ooo00OoOOO )
 if 20 - 20: oO00Oo0o000 . Ii1i111I . OoOO00O + Ii1i111I - i1IiIIIII * O0O0O
elif OOoooooooO == 7001 :
 IiIII ( )
 if 82 - 82: oO0o
elif OOoooooooO == 7010 :
 oo00o000O ( Ooo00OoOOO )
 if 78 - 78: IIiIiII11i / Ii1i111I - Ii + Ii1I * I1ii11iIi11i
elif OOoooooooO == 7011 :
 iiIIiii1iii1I ( Ooo00OoOOO )
 if 17 - 17: OOooOOo
elif OOoooooooO == 7012 :
 Iii1II1 ( Ooo00OoOOO )
 if 72 - 72: IIiI1I . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OOoooooooO == 7013 :
 cnfTVPlay2 ( Ooo00OoOOO )
elif OOoooooooO == 7014 :
 CNF_Studio_Indexer . MV_Movies ( Ooo00OoOOO )
elif OOoooooooO == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( Ooo00OoOOO )
elif OOoooooooO == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( II1i11I , Ooo00OoOOO , o00OooO0oo )
elif OOoooooooO == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OOoooooooO == 7018 :
 O00O0O00o0O ( )
elif OOoooooooO == 7019 :
 CNF_Studio_Indexer . List_Movies ( Ooo00OoOOO )
elif OOoooooooO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Ooo00OoOOO )
elif OOoooooooO == 7024 :
 CNF_Studio_Indexer . Box_Office ( Ooo00OoOOO )
 if 64 - 64: O0O0O
elif OOoooooooO == 8000 :
 III1I1ii ( )
elif OOoooooooO == 8001 :
 i1I1i ( )
elif OOoooooooO == 8002 :
 o0o00OoOo0 ( )
elif OOoooooooO == 8003 :
 oOII11i1I ( )
elif OOoooooooO == 8004 :
 Oooo ( )
elif OOoooooooO == 8005 :
 oooooO0oO0ooO ( )
elif OOoooooooO == 8006 :
 O0OoOo ( II1i11I , Ooo00OoOOO )
elif OOoooooooO == 8030 :
 iiI1i11II ( Ooo00OoOOO )
elif OOoooooooO == 8045 :
 IiI11i1I11111 ( Ooo00OoOOO )
elif OOoooooooO == 8046 :
 Ii1IIIIIIiI1 ( Ooo00OoOOO )
elif OOoooooooO == 8047 :
 ii1I ( Ooo00OoOOO )
elif OOoooooooO == 8048 :
 o0OOo ( Ooo00OoOOO )
elif OOoooooooO == 8049 :
 IiI1Ii11Ii ( Ooo00OoOOO )
elif OOoooooooO == 8020 :
 Oo0O00O ( )
elif OOoooooooO == 8021 :
 OOoOOO0IiI1i1i1 ( Ooo00OoOOO )
elif OOoooooooO == 8022 :
 O0O000oOO0 ( Ooo00OoOOO )
elif OOoooooooO == 8023 :
 I1iI1iiI1Ii1 ( Ooo00OoOOO )
elif OOoooooooO == 8040 :
 oO0O ( )
elif OOoooooooO == 8041 :
 iI1111i ( Ooo00OoOOO )
elif OOoooooooO == 8042 :
 I1IIIIIi1IIiI ( Ooo00OoOOO )
elif OOoooooooO == 8043 :
 yt . PlayVideo ( Ooo00OoOOO )
elif OOoooooooO == 8044 :
 III11I11ii ( Ooo00OoOOO )
elif OOoooooooO == 8060 :
 O000OO ( )
elif OOoooooooO == 8061 :
 I1Ii ( Ooo00OoOOO )
elif OOoooooooO == 8064 :
 i11i ( )
elif OOoooooooO == 8065 :
 O0o0O00o0o ( Ooo00OoOOO )
elif OOoooooooO == 8070 :
 II11IiIIiiI ( )
elif OOoooooooO == 8071 :
 OO ( Ooo00OoOOO )
elif OOoooooooO == 7080 :
 o0oOOOOoo0 ( Ooo00OoOOO )
elif OOoooooooO == 8090 :
 iIi1i ( )
elif OOoooooooO == 8091 :
 III ( Ooo00OoOOO )
elif OOoooooooO == 8092 :
 IiiI ( Ooo00OoOOO )
elif OOoooooooO == 8081 :
 IiiiO0oo0ooo0 ( )
elif OOoooooooO == 8062 :
 ii1II1iiii ( Ooo00OoOOO )
elif OOoooooooO == 8063 :
 i1i1IIiII1I ( Ooo00OoOOO )
elif OOoooooooO == 8050 :
 ii1iI1II11ii ( )
elif OOoooooooO == 8051 :
 i1i1IiIiIi1Ii ( Ooo00OoOOO )
elif OOoooooooO == 8052 :
 oO0ooOO ( Ooo00OoOOO )
elif OOoooooooO == 8085 :
 o0oOoO00 ( )
elif OOoooooooO == 8086 :
 OO0IIIIIIi111i ( Ooo00OoOOO )
elif OOoooooooO == 8087 :
 iIIiI1111 ( Ooo00OoOOO )
elif OOoooooooO == 8088 :
 OooOO ( Ooo00OoOOO , II1i11I )
elif OOoooooooO == 9000 :
 ii1i1i1IiII ( )
elif OOoooooooO == 1111 :
 III1I11II11I ( )
elif OOoooooooO == 9001 :
 o0o0oO ( )
elif OOoooooooO == 9002 :
 oo0OooO ( )
elif OOoooooooO == 9003 :
 oO0OOoo ( )
elif OOoooooooO == 50 :
 OO00OOoO0o ( Ooo00OoOOO )
elif OOoooooooO == 9020 :
 champlist ( )
elif OOoooooooO == 9021 :
 OO00OoOO ( )
elif OOoooooooO == 9022 :
 iiii1II1ii11 ( )
elif OOoooooooO == 9023 :
 i1IIIII1 ( )
elif OOoooooooO == 9024 :
 iII111iiiI11i ( Ooo00OoOOO )
elif OOoooooooO == 9030 :
 oooO00oo0 ( Ooo00OoOOO )
elif OOoooooooO == 9031 :
 o000 ( Ooo00OoOOO )
elif OOoooooooO == 9032 :
 oOiiIIIII ( Ooo00OoOOO )
elif OOoooooooO == 9033 :
 iiI1 ( Ooo00OoOOO )
elif OOoooooooO == 7085 :
 O0o0OOOO0 ( Ooo00OoOOO )
elif OOoooooooO == 7086 :
 IIIIIII1i ( Ooo00OoOOO )
elif OOoooooooO == 7087 :
 O0o0oo0O ( iiIi1i )
elif OOoooooooO == 9666 :
 iiII ( Ooo00OoOOO )
elif OOoooooooO == 10100 : OOO00o0 ( )
elif OOoooooooO == 10105 : oOOo0ooO0 ( Ooo00OoOOO )
elif OOoooooooO == 10106 : oO0I1iI1i11IiI11 ( Ooo00OoOOO )
elif OOoooooooO == 10104 : oO0Oo ( Ooo00OoOOO )
elif OOoooooooO == 10107 : Oo0o0OO0OO000OO ( )
elif OOoooooooO == 10103 : IIII1ii1 ( Ooo00OoOOO )
elif OOoooooooO == 10108 : Iiiii1Iii1I ( Ooo00OoOOO )
elif OOoooooooO == 10107 : Oo0o0OO0OO000OO ( )
elif OOoooooooO == 10000 : Origin_Menu ( )
elif OOoooooooO == 10001 : oOo000O ( )
elif OOoooooooO == 10002 : i1IiI1Iiii ( )
elif OOoooooooO == 10003 : O000oO0O ( )
elif OOoooooooO == 10004 : iI1iIIII1 ( Ooo00OoOOO )
elif OOoooooooO == 10005 : oO0Ooo0OooOOo ( )
elif OOoooooooO == 10006 : II1o0ooO0OOO ( Ooo00OoOOO )
elif OOoooooooO == 10007 : oo0 ( Ooo00OoOOO , o00OooO0oo )
elif OOoooooooO == 10008 : oOoOo0o00o ( )
elif OOoooooooO == 10009 : I1iiIi1 ( )
elif OOoooooooO == 10010 : IioOooOOo00ooO ( Ooo00OoOOO )
elif OOoooooooO == 10011 : o0ooo0o0 ( Ooo00OoOOO )
elif OOoooooooO == 10012 : OOoO0oO00o ( Ooo00OoOOO )
elif OOoooooooO == 10013 : I111 ( Ooo00OoOOO )
elif OOoooooooO == 10014 : ooo0oo00O00oO ( )
elif OOoooooooO == 10015 : o0oO0Oo ( )
elif OOoooooooO == 10016 : OO0I111i1I ( Ooo00OoOOO )
elif OOoooooooO == 10017 : oo0oO ( )
elif OOoooooooO == 10018 : OO00oo ( )
elif OOoooooooO == 10019 : oo00o0 ( )
elif OOoooooooO == 10020 : OoooooOo ( )
elif OOoooooooO == 10021 : i1I1IiI1ii ( )
elif OOoooooooO == 10022 : Oo0O0000Oo00o ( Ooo00OoOOO )
elif OOoooooooO == 10023 : I1II ( II1i11I , Ooo00OoOOO )
elif OOoooooooO == 10024 : O00oo ( Ooo00OoOOO )
elif OOoooooooO == 10025 : i11i11 ( )
elif OOoooooooO == 10026 : Ii1I1I1i11ii ( )
elif OOoooooooO == 10027 : OoOo00o ( )
elif OOoooooooO == 10028 : oOOoo0 ( )
elif OOoooooooO == 10029 : o00Oo ( )
elif OOoooooooO == 423 : ooooO ( Ooo00OoOOO )
elif OOoooooooO == 426 : Ii1iiII1i ( Ooo00OoOOO )
elif OOoooooooO == 10030 : Izle_Films ( )
elif OOoooooooO == 10031 : Latest_Izle_Movies ( )
elif OOoooooooO == 10032 : Izle_Genres ( )
elif OOoooooooO == 10033 : Izle_Pop_Movies ( )
elif OOoooooooO == 10034 : Izle_Boxsets ( )
elif OOoooooooO == 10035 : Izle_Search ( )
elif OOoooooooO == 10036 : Izle_Genres_Movie ( Ooo00OoOOO )
elif OOoooooooO == 10037 : Izle_Boxset_single ( Ooo00OoOOO )
elif OOoooooooO == 10038 : Izle_IFRAME ( )
elif OOoooooooO == 10039 : Izle_Boxsets_Next ( Ooo00OoOOO )
elif OOoooooooO == 10040 : Oo0o00ooOOOoOo ( )
elif OOoooooooO == 10041 : i1iI1Iiii1I ( Ooo00OoOOO )
elif OOoooooooO == 10042 : o0OOOOOo0 ( Ooo00OoOOO )
elif OOoooooooO == 10043 : Ii1 ( )
elif OOoooooooO == 10044 : o0O0oOO0Oooo ( Ooo00OoOOO )
elif OOoooooooO == 10045 : oO0O0o0O ( II1i11I )
elif OOoooooooO == 10046 : IiI11I111 ( Ooo00OoOOO )
elif OOoooooooO == 10047 : i111I11I ( Ooo00OoOOO )
elif OOoooooooO == 10048 : I1iI11I ( Ooo00OoOOO )
elif OOoooooooO == 10049 : iii ( Ooo00OoOOO )
elif OOoooooooO == 10050 : II11I ( )
elif OOoooooooO == 10051 : ooOo0oO0O ( )
elif OOoooooooO == 10052 : O0oooOOo0 ( )
elif OOoooooooO == 10053 : Addon ( Ooo00OoOOO )
elif OOoooooooO == 10054 : IiIIii1 ( Ooo00OoOOO , II1i11I )
elif OOoooooooO == 10055 :
 I1iIIIiI ( "addFavorite" )
 try :
  II1i11I = II1i11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  II1i11I = II1i11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOO0o0 ( II1i11I , Ooo00OoOOO , o00OooO0oo , o0o0oOoOO0O , iIOo0oo )
elif OOoooooooO == 10056 :
 I1iIIIiI ( "rmFavorite" )
 try :
  II1i11I = II1i11I . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  II1i11I = II1i11I . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOo000OO000 ( II1i11I )
elif OOoooooooO == 10057 :
 I1iIIIiI ( "getFavorites" )
 iiIi1iiI1I ( )
elif OOoooooooO == 10058 : o00O0 ( )
elif OOoooooooO == 10059 : Donators_Guide ( )
elif OOoooooooO == 10060 : O0iII1 ( )
elif OOoooooooO == 10061 : oOOo0o0oo ( )
elif OOoooooooO == 10062 : Oo00OoOo ( II1i11I , Ooo00OoOOO , iiIi1i )
elif OOoooooooO == 10063 : iiI111 ( )
elif OOoooooooO == 10064 : oooooOOO000Oo ( )
elif OOoooooooO == 10065 : o00o000oo ( Ooo00OoOOO )
elif OOoooooooO == 10066 : oOOO0oo0 ( Ooo00OoOOO )
elif OOoooooooO == 10068 : iii11I ( Ooo00OoOOO )
elif OOoooooooO == 10069 : I1i11i ( Ooo00OoOOO )
elif OOoooooooO == 10070 : iiI11i1II ( Ooo00OoOOO )
elif OOoooooooO == 10071 : Genie_Watch ( )
elif OOoooooooO == 10072 : Ii1Iii1iIi ( )
elif OOoooooooO == 10073 : IiIIi1 ( Ooo00OoOOO )
elif OOoooooooO == 10074 : IiIi1I1 ( Ooo00OoOOO )
elif OOoooooooO == 10075 : II1iI1I11I ( o00OooO0oo , II1i11I , Ooo00OoOOO )
elif OOoooooooO == 10076 : oOIIiIi ( Ooo00OoOOO )
elif OOoooooooO == 10077 : ooOoOo0 ( Ooo00OoOOO )
elif OOoooooooO == 10078 : I1III1111iIi ( )
elif OOoooooooO == 10079 : Genie_Watch_Tv_Shows ( )
elif OOoooooooO == 10080 : Genie_Watch_Tv_Genre ( Ooo00OoOOO )
elif OOoooooooO == 10081 : Genie_Watch_TV_PlayRun ( Ooo00OoOOO )
elif OOoooooooO == 10082 : Genie_Watch_TV_Episodes ( Ooo00OoOOO , o00OooO0oo )
elif OOoooooooO == 10083 : Genie_Watch_Tv_Recent ( Ooo00OoOOO )
elif OOoooooooO == 10084 : O0Oo0oOOoooOOOOo ( )
elif OOoooooooO == 10085 : i1iIi ( )
elif OOoooooooO == 10086 : IIII ( )
elif OOoooooooO == 20000 : I11iiIIiI1ii ( )
elif OOoooooooO == 20001 : O00 ( )
elif OOoooooooO == 20002 : iIoo0ooooO ( Ooo00OoOOO )
elif OOoooooooO == 20003 : IiIii1ii ( Ooo00OoOOO )
elif OOoooooooO == 20004 : o00O00Oo00O ( Ooo00OoOOO )
elif OOoooooooO == 21004 : iIiIIi ( )
elif OOoooooooO == 21005 : III1I ( Ooo00OoOOO )
elif OOoooooooO == 21006 : OoOOOO ( Ooo00OoOOO )
elif OOoooooooO == 21007 : III1I11i1iIi ( Ooo00OoOOO )
elif OOoooooooO == 30000 : oo0o0 ( )
elif OOoooooooO == 30001 : I1Iii1iI1 ( )
elif OOoooooooO == 10012 : Resolve ( Ooo00OoOOO )
elif OOoooooooO == 30003 : I11oOoO0o ( )
elif OOoooooooO == 30004 : i1IIi1i1Ii1 ( Ooo00OoOOO )
elif OOoooooooO == 30005 : ooOOOoOoOOO0 ( Ooo00OoOOO )
elif OOoooooooO == 30006 : OO0 ( )
elif OOoooooooO == 30007 : i11i1Ii1 ( )
elif OOoooooooO == 30008 : iIiIii1I1II ( Ooo00OoOOO )
elif OOoooooooO == 30009 : ii1iIIiii1 ( Ooo00OoOOO )
elif OOoooooooO == 30010 : I1iiIII ( Ooo00OoOOO )
elif OOoooooooO == 30011 : O0o00O0Oo0 ( )
elif OOoooooooO == 30012 : oO00oOOo0Oo ( )
elif OOoooooooO == 30013 : ooO0oo ( )
elif OOoooooooO == 30014 : i1i1II11II1 ( )
elif OOoooooooO == 30015 : I11I ( Ooo00OoOOO , o00OooO0oo , o0o0oOoOO0O )
elif OOoooooooO == 30016 : ooOoOOOOo ( Ooo00OoOOO )
elif OOoooooooO == 30019 : i1I11iIII1i1I ( Ooo00OoOOO )
elif OOoooooooO == 30017 : iii1III1i ( Ooo00OoOOO )
elif OOoooooooO == 30018 : i1o0oooO ( Ooo00OoOOO )
elif OOoooooooO == 30030 : oOooo00000 ( )
elif OOoooooooO == 30031 : iiI11I1iiIiII1I ( )
elif OOoooooooO == 30032 : o00ooOoo ( )
elif OOoooooooO == 30033 : i111i1I1ii1i ( )
elif OOoooooooO == 30034 : O0OoooI11iI1I ( )
elif OOoooooooO == 30035 : I11iIi1II ( Ooo00OoOOO )
elif OOoooooooO == 30036 : ooo0OO ( Ooo00OoOOO )
elif OOoooooooO == 30037 : iIi1IiI ( Ooo00OoOOO )
elif OOoooooooO == 30038 : i1IiiI1iIi ( )
elif OOoooooooO == 30039 : oOO0OO0OO ( )
elif OOoooooooO == 50000 : IiI111111IIII ( )
elif OOoooooooO == 50001 : IiiiI ( )
elif OOoooooooO == 50002 : oOOoOOO0oOoo ( Ooo00OoOOO )
if 80 - 80: I11i % iI11I1II1I1I
if 63 - 63: O00Oo000ooO0 * Ii
if 86 - 86: Ii1i111I % Ii1i111I - OOooOOo + oO00Oo0o000 / oOo0O0Ooo * ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
