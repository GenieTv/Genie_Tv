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
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Football On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , OOoOO0oo0ooO + 'TvGuide.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']Link GTV to Guide[/COLOR]' , '' , 4010 , OOoOO0oo0ooO + 'linkchannels.png' , i1iIIi1 , '' )
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
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Today On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , OOoOO0oo0ooO + 'PremiereLeague.png' , i1iIIi1 , '' )
 if 87 - 87: O00Oo000ooO0 / oO00Oo0o000 - I1ii11iIi11i
def oOOoOOO0oOoo ( url ) :
 o0OOOO00O0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for o0O0ooooooo00 , url , I1111ii11IIII , IiIi1II111I , I1iIiIi11i11 , o0o0 , o00oIIi1i1 , OOO , ii1 , o0O0Ooo , O0o in o0O00oOoOO :
  I1111ii11IIII = I1111ii11IIII
  if 'Arsenal' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'arsenal-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                                  ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Bournemouth' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'afc-bournemouth.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                       ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Burnley' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'KEGnQWW.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                                   ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Chelsea' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'chelsea.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                                  ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Crystal' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'CrystalPalace.0.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                       ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Everton' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'Everton.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                                   ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Hull' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'hull-city-afc.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                                 ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Leicester' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'leicester-city-fc-hd-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                       ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Liverpool' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'liverpool-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                               ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Manchester City' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'city-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '               ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Manchester United' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + '91.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '          ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Middlesbrough' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'middlesbrough-fc-hd-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                 ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Southampton' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'southampton-fc-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                   ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Stoke City' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'stoke-city.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                          ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Sunderland' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'sunderland-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                        ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Swansea' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'swansea-city-afc.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                    ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Tottenham' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'tottenham-hotspur_zps4e3ed7c1.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '        ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Watford' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'watford-fc-hd-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '                              ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'Bromwich' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'west-bromwich-albion-logo.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '   ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  elif 'West Ham' in I1111ii11IIII :
   IiIi = OOoOO0oo0ooO + 'west-ham.png'
   II1i11I = '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0ooooooo00 + ' - ' + I1111ii11IIII + '             ' + IiIi1II111I + '        ' + I1iIiIi11i11 + '        ' + o0o0 + '        ' + o00oIIi1i1 + '        ' + OOO + '        ' + ii1 + '        ' + o0O0Ooo + '[/COLOR]'
  o0OOOO00O0Oo ( str ( II1i11I ) , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , IiIi , IiIi , I1111ii11IIII )
  if 63 - 63: O00Oo000ooO0 - ooOoO0O00 * I11i + ii
def I1iiIi1 ( description ) :
 I1111ii11IIII = description
 Ooo00OoOOO = ( 'http://www.fullmatchesandshows.com/?s=' + I1111ii11IIII ) . replace ( ' ' , '%20' )
 i1iiiIi1Iii ( Ooo00OoOOO )
 if 54 - 54: O0oOO0 . iI11I1II1I1I * ooOoO0O00
def II1II1i ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o0O00oOoOO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ooo00OoOOO , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IIii11Ii1i1I , i1iIIi1 , '' )
  if 1 - 1: o0o00Oo0O
def I11II1i1 ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIiII )
 for iiIII1i in iiIII1i :
  IiI1ii11I1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( iiIII1i ) )
  for I1i1iI in IiI1ii11I1 :
   I1i1iI = I1i1iI
  I1iI1I1ii1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iiIII1i ) )
  for iIIi1 , IIii11Ii1i1I , time , o0Ooo0o0Oo in I1iI1I1ii1 :
   IIII1iII = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0Ooo0o0Oo )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + I1i1iI + ' - ' + iIIi1 + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + IIii11Ii1i1I , i1iIIi1 , ( str ( IIII1iII ) ) )
   if 55 - 55: iI11I1II1I1I * IIiI1I
 oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if 85 - 85: iI11I1II1I1I . IIiIiII11i
def o0ooo0o0 ( ) :
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
 if 84 - 84: Ii1i111I - I1ii11iIi11i * o0o00Oo0O / OoOO00O . OoOO00O
def ooO0 ( url ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  ii111iiIii = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in II1i11I :
   pass
  else :
   ii111iiIii = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + ii111iiIii + '[/COLOR]' , url , 10013 , IIii11Ii1i1I )
 for url , IIii11Ii1i1I , II1i11I in iIIi1i1 :
  ii111iiIii = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in II1i11I :
   pass
  else :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + ii111iiIii + '[/COLOR]' , url , 10013 , IIii11Ii1i1I )
def i1iiiIi1Iii ( url ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIiII )
 if 57 - 57: I11i / oO00Oo0o000
 if 13 - 13: ii + oO0o
 if 32 - 32: o0o00Oo0O + O0O0O % I1ii11iIi11i
 if 7 - 7: Ii1I / O0oOO0
 if 11 - 11: O00Oo000ooO0 * O0oOO0 / O0oOO0 - i1IiIIIII
 if 68 - 68: oOo0O0Ooo % O00Oo000ooO0 - O00Oo000ooO0 / oOo0O0Ooo + Ii1I - I1ii11iIi11i
 if 65 - 65: O0oOO0 - ooOoO0O00
 for url , IIii11Ii1i1I , II1i11I in iIIi1i1 :
  ii111iiIii = II1i11I . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in II1i11I :
   pass
  else :
   I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + ii111iiIii + '[/COLOR]' , url , 10013 , IIii11Ii1i1I )
   if 62 - 62: Ii1i111I / O0O0O % I1ii11iIi11i . ii / Ii / oO00Oo0o000
def OooO0O0Ooo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( IIiII )
 for O0Oooo in o0O00oOoOO :
  oO0O = ( O0Oooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOoO0oO00o ( 'http:' + oO0O )
  if 25 - 25: O0O0O % oOo0O0Ooo + Ii + o0o00Oo0O * ii
  if 64 - 64: ooOoO0O00
  if 10 - 10: oO00Oo0o000 % o0o00Oo0O / oOo0O0Ooo % Ii1i111I
  if 25 - 25: IIiIiII11i / oO0o
def oo0OoOO0000 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 8046 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , OOoOO0oo0ooO + 'Next.png' )
def i11Ii1iIIIIi ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OOoO0oO00o ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 14 - 14: ii . I11i . Ii1i111I
def I1IIIIIi1IIiI ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 26 - 26: I11i % i1IiIIIII + i1IiIIIII % Ii1i111I * Ii / IIiI1I
def OOoO0oO00oOOO0OoO0oo0OO ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 31 - 31: Ii1i111I * O0O0O . OoOO00O
 o0O00oOoOO = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 if 35 - 35: Ii1i111I
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 8041 , OOoOO0oo0ooO + 'documentary.png' )
  if 94 - 94: O0oOO0 / Ii % o0o00Oo0O
  if 70 - 70: Ii1i111I - I1ii11iIi11i / ii % ii
  if 95 - 95: ii % ii . OoOO00O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def III1ii ( url ) :
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
  if 38 - 38: Ii1I + OOooOOo
  if 68 - 68: o0o00Oo0O
def o0oOoO00 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , IIii11Ii1i1I , url , IIiI1i in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  oOO000 ( ( url ) . replace ( '//' , 'http://' ) )
  if 95 - 95: o0o00Oo0O + oOo0O0Ooo + OOooOOo . i1IiIIIII
def oOO000 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1IIiI ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoOO0oo0ooO + 'documentary.png' )
  if 73 - 73: O0O0O . IIiIiII11i * IIiI1I % O0O0O + OOooOOo - oO0o
def I1iIi1iIIIIiI ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT' , url , 8048 , OOoOO0oo0ooO + 'Next.png' )
def O000oooOO0Oo0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in iIIi1i1 :
  if 'rtd' in url :
   I1iIiIii ( url )
   if 76 - 76: oO0o . ii % oO00Oo0o000 * OoOO00O
def I1iIiIii ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIi1i1iIi1iI )
 for O00oO , file in o0O00oOoOO :
  url = ( 'https://rtd.rt.com' + O00oO + file )
  OOoO0oO00o ( url )
  if 23 - 23: O00Oo000ooO0 + iI11I1II1I1I
  if 14 - 14: o0o00Oo0O % O00Oo000ooO0 % OoOO00O * O0O0O
def o0OOO00ooo ( ) :
 IIiII = iiIi1iI1iIii ( 'http://www.stream2watch.co/live-tv' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I , I1iI11IiiI11i in o0O00oOoOO :
  OoO00 ( ( II1i11I + '[COLOR' + oO0o0o0ooO0oO + ']' + I1iI11IiiI11i + '[/COLOR]' ) , Ooo00OoOOO , 8086 , IIii11Ii1i1I )
  if 37 - 37: I11i % ooOoO0O00 - I11i + iI11I1II1I1I + oO00Oo0o000
def oOoO00O ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 8087 , IIii11Ii1i1I )
  if 31 - 31: O0oOO0 . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * IIiI1I
def I1i1iII1I11 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , II1i11I in o0O00oOoOO :
  o00OOo0o0O ( url , II1i11I )
  if 14 - 14: IIiI1I - Ii1i111I * ii + i1IiIIIII . IIiIiII11i
def o00OOo0o0O ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIiII )
 for url in o0O00oOoOO :
  print url
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 15 - 15: Ii1i111I % Ii
def O0o0O00o0o ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Ooo00OoOOO , 3002 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def II1IIiiI1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def O00O00 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 oOooO0OoO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url , II1i11I in oOooO0OoO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + II1i11I + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url in next :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'Next.png' )
 for url , IIii11Ii1i1I , II1i11I in iIIi1i1 :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + IIii11Ii1i1I )
def o0oOOOOoo0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  ooOO0OOO00o ( url )
def ooOO0OOO00o ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  OOoO0oO00o ( url )
  if 76 - 76: ii * ii - IIiI1I - iI11I1II1I1I . ii / Ii1I
def oOOOO0oo0O0OO ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ooo00OoOOO , 8065 , OOoOO0oo0ooO + 'classicmovies.png' )
def O0OOoo0o ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( "v.src = '([^']*)';" ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  Iiii1iI1i ( url )
  if 19 - 19: O0oOO0 % O0O0O
def iIi ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ooo00OoOOO , 8065 , OOoOO0oo0ooO + 'classictv.png' )
def iIiiI1Ii111i ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  if 'mp4' in url :
   OOoO0oO00o ( url )
 for url in iIIi1i1 :
  yt . PlayVideo ( url )
  if 38 - 38: O0O0O % ii + oO0o * Ii
def ooO ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Ooo00OoOOO , 8071 , OOoOO0oo0ooO + 'streams.png' )
def IIi1ii ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , url in o0O00oOoOO :
  if '(Free Access)' in II1i11I :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , OOoOO0oo0ooO + 'streams.png' )
def Ii1i1i ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , II1i11I , url in o0O00oOoOO :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , IIii11Ii1i1I , o0o0oOoOO0O , '' )
  if 83 - 83: Ii1i111I - Ii1I * O0O0O
def oOO00OO0OooOo ( ) :
 oO0ooOoO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Genres' , 'http://www.xvideos.com' , 10106 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 oO0ooOoO ( 'Search' , '' , 10107 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' , )
 if 13 - 13: o0o00Oo0O % O0oOO0 % Ii1i111I
def Ii11IiI111 ( url ) :
 IIiII = Iiii ( url )
 IIiii11ii1II1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in IIiii11ii1II1 :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIiII )
 for url , II1i11I , ii1I1IIii11 in o0O00oOoOO :
  oO0ooOoO ( ( II1i11I + ' - No of Videos : ' + ( ii1I1IIii11 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 97 - 97: Ii1i111I - I11i + O0oOO0
def OO0000 ( url ) :
 IIiII = Iiii ( url )
 IIiii11ii1II1 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIiII )
 for url in IIiii11ii1II1 :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I , o000OOO000 in o0O00oOoOO :
  oO0ooOoO ( II1i11I + '--' + o000OOO000 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( IIii11Ii1i1I ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 53 - 53: IIiI1I . I11i
  if 96 - 96: I1ii11iIi11i + oO00Oo0o000 . ooOoO0O00
def OooIii1I1iI ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , url , II1i11I , Oo0OO0000oooo , oOoOo0 in o0O00oOoOO :
  oO0ooOoO ( II1i11I + ' - Porn Quality : ' + oOoOo0 + ' - ' + Oo0OO0000oooo , 'http://www.xvideos.com' + url , 10108 , IIii11Ii1i1I , IIii11Ii1i1I , oOoOo0 + ' - ' + Oo0OO0000oooo )
 iIioOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for url in iIioOo :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 66 - 66: IIiIiII11i + oO0o
def II1iI1iiiI ( url ) :
 IIiII = Iiii ( url )
 iiIII1i = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 IIiii11ii1II1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in IIiii11ii1II1 :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iiIII1i ) )
 for url , II1i11I in o0O00oOoOO :
  oO0ooOoO ( II1i11I , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 75 - 75: ii . i1IiIIIII + oO0o / OoOO00O - oOo0O0Ooo % OoOO00O
  if 89 - 89: IIiI1I * iI11I1II1I1I + Ii . ii
def O0O0 ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0ooo00o0o000Oo = ( I1i111I ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 I1i11 = oO0ooo00o0o000Oo . lower ( )
 Oooo00OOo = 'http://www.xvideos.com/?k=' + I1i11
 print Oooo00OOo + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIiII = Iiii ( Oooo00OOo )
 o0O00oOoOO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , Ooo00OoOOO , II1i11I , Oo0OO0000oooo , oOoOo0 in o0O00oOoOO :
  oO0ooOoO ( II1i11I + ' - Porn Quality : ' + oOoOo0 + ' - ' + Oo0OO0000oooo , 'http://www.xvideos.com' + Ooo00OoOOO , 10108 , IIii11Ii1i1I , IIii11Ii1i1I , oOoOo0 + ' - ' + Oo0OO0000oooo )
 iIioOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for Ooo00OoOOO in iIioOo :
  oO0ooOoO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Ooo00OoOOO , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 6 - 6: O0O0O / oOo0O0Ooo / OOooOOo
def OooOO ( url ) :
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
   if 32 - 32: Ii
def II1i ( url ) :
 I1iiIi111I = xbmc . Player ( IiiiI1 ( ) )
 import urlresolver
 try : I1iiIi111I . play ( url )
 except : pass
 if 34 - 34: OoOO00O + I1ii11iIi11i - ooOoO0O00 - O00Oo000ooO0 + iI11I1II1I1I
 if 75 - 75: Ii1I
def O00o ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 o0O00oOoOO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + Ooo00OoOOO ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , OOoOO0oo0ooO + 'gofish.png' )
def o0o0ooOo00 ( url ) :
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
def OO00oO0OoO0o ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 5 - 5: i1IiIIIII % I1ii11iIi11i % O00Oo000ooO0 % O0oOO0
  if 17 - 17: OoOO00O + IIiIiII11i + ii / i1IiIIIII / O00Oo000ooO0
  if 80 - 80: I11i % ooOoO0O00 / Ii1i111I
ooi1i1Ii1IiIII = '{PQ},' ; I1IIii11 = '{SC},' ; I1I1O0O = '{XG},' ; OO0ooO00o = '{JP},' ; I1iii1 = '{HW},' ; iIiiiIIiii = '{RT},'
def OO0Oo00Oo ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iIiO0O = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oOOoooo = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 O0oIi1iIiIi1I11 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ii1I11 = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOO0 = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I1i111I
 I1Ii1 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 O0oo0oOoO00 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 i1ii1iIi = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 I1I1Ii = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 42 - 42: I11i - I1ii11iIi11i % Ii1I
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIiII = i1I1iI ( Ooo00OoOOO )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( oOOoooo )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 I11ii1iI11 = i1I1iI ( O0oIi1iIiIi1I11 )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 i11ii111i1ii = i1I1iI ( OOO0 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 Oo0O0O = i1I1iI ( I1Ii1 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 IiIiiI1ii111 = i1I1iI ( O0oo0oOoO00 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 i11ii1 = i1I1iI ( i1ii1iIi )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 Ii111I11 = i1I1iI ( I1I1Ii )
 if 51 - 51: ii + I11i * iI11I1II1I1I * O0O0O / ooOoO0O00
 if 19 - 19: IIiI1I - OOooOOo % O0O0O / ii % IIiI1I
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
  for ooOoOoO0 , II1i11I in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( Ooo00OoOOO + ooOoOoO0 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0ooOooo000oOO )
  for ooOoOoO0 , II1i11I in iIIi1i1 :
   if I1i111I in II1i11I . lower ( ) :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( OOoOooOoOOOoo + ooOoOoO0 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oOOo )
  for ooOoOoO0 , II1i11I in i1IIii1iiIi :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1ii1ii11i1I + ooOoOoO0 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if Oo0OoO00oOO0o != 'Failed' :
  oooo0OOo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for ooOoOoO0 , II1i11I in oooo0OOo :
   if I1i111I in II1i11I . lower ( ) :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , Ooo00OoOOO , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if I11ii1iI11 != 'Failed' :
  Iii1II1ii = [ ]
  ooOo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I11ii1iI11 )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in ooOo00 :
   if I1i111I in II1i11I . lower ( ) :
    if II1i11I in Iii1II1ii :
     pass
    else :
     o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
     Iii1II1ii . append ( II1i11I )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if i11ii111i1ii != 'Failed' :
  OO0III = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i11ii111i1ii )
  for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in OO0III :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + Ooo00OoOOO , 7067 , IIii11Ii1i1I )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 59 - 59: ii / O00Oo000ooO0 + Ii1i111I . IIiI1I * OoOO00O - ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0O0O != 'Failed' :
  OO0O0OO0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0O0O )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in OO0O0OO0O0 :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Redemption[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 78 - 78: O0O0O / ii . O0O0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IiIiiI1ii111 != 'Failed' :
  I1IOoo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIiiI1ii111 )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in I1IOoo :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Reaper[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 94 - 94: IIiIiII11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if i11ii1 != 'Failed' :
  i1iI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11ii1 )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in i1iI :
   if I1i111I in II1i11I . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Herovision[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 26 - 26: iI11I1II1I1I - Ii1I . O00Oo000ooO0 . O00Oo000ooO0 + iI11I1II1I1I * I1ii11iIi11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 85 - 85: i1IiIIIII + IIiIiII11i - i1IiIIIII * O0O0O - ooOoO0O00 % IIiI1I
 if Ii111I11 != 'Failed' :
  IiIiI = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Ii111I11 )
  for Ooo00OoOOO , o00OooO0oo , II1i11I in IiIiI :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Silent Hunter[/COLOR]' ) , Ooo00OoOOO , 222 , o00OooO0oo )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 47 - 47: OOooOOo
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 II1III1i1iiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 65 - 65: o0o00Oo0O + oO00Oo0o000 % OoOO00O * oOo0O0Ooo / O0oOO0 / OOooOOo
 for IiIi1i in II1III1i1iiI :
  oO0 = OOO00 + IiIi1i + OooO0
  oooOO = i1I1iI ( oO0 )
  if oooOO != 'Failed' :
   iI1IIIi11 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oooOO )
   for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in iI1IIIi11 :
    if I1i111I in II1i11I . lower ( ) :
     OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source Pandoras[/COLOR]' , Ooo00OoOOO , 222 , o00OooO0oo , IiI , OOoOOO0 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 69 - 69: o0o00Oo0O - o0o00Oo0O
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 41 - 41: O00Oo000ooO0 % I11i
 II1III1i1iiI = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 67 - 67: o0o00Oo0O % oO00Oo0o000
 if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % i1IiIIIII
 for IiIi1i in II1III1i1iiI :
  oO0 = iIiO0O + IiIi1i
  iIi1Ii1111i = i1I1iI ( oO0 )
  if iIi1Ii1111i != 'Failed' :
   i1i = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( iIi1Ii1111i )
   for ooOoOoO0 , II1i11I in i1i :
    if I1i111I in II1i11I . lower ( ) :
     I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIiO0O + IiIi1i + ooOoOoO0 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 97 - 97: Ii - IIiI1I + iI11I1II1I1I
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 45 - 45: ooOoO0O00 . oO0o * ii - oOo0O0Ooo + O0oOO0 * Ii1I
     if 2 - 2: O00Oo000ooO0 . O00Oo000ooO0 - O0O0O % oO0o + I1ii11iIi11i
def OooOoOOO00O ( ) :
 if 29 - 29: O00Oo000ooO0 * IIiI1I * O0O0O . O0O0O
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 if 42 - 42: oO00Oo0o000 % oO0o . Ii1I
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( I1i111I ) . replace ( ' ' , '%20' )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 oOOoooo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 O0oIi1iIiIi1I11 = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I1i11 ) . replace ( ' ' , '+' )
 ii1I11 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 OOO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 I1Ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 4 - 4: ooOoO0O00 + OOooOOo
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 39 - 39: iI11I1II1I1I + O0oOO0
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIiII = i1I1iI ( Ooo00OoOOO )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( oOOoooo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 I11ii1iI11 = cloudflare . source ( O0oIi1iIiIi1I11 )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 iIi1Ii1111i = i1I1iI ( ii1I11 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 i11ii111i1ii = i1I1iI ( OOO0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 Oo0O0O = i1I1iI ( I1Ii1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 92 - 92: Ii1i111I % Ii % I1ii11iIi11i
 if Oo0O0O != 'Failed' :
  OO0O0OO0O0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0O0O )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in OO0O0OO0O0 :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source HeroVision[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 23 - 23: IIiIiII11i * IIiI1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 80 - 80: oO00Oo0o000 / Ii + ii
 if i11ii111i1ii != 'Failed' :
  OO0III = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i11ii111i1ii )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in OO0III :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- source Reaper[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 38 - 38: Ii1I % O0oOO0 + ooOoO0O00 * ii * O0O0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: iI11I1II1I1I - O0oOO0 - oO00Oo0o000 / oO0o - o0o00Oo0O
    if 81 - 81: OoOO00O - O0O0O * Ii1I / oO00Oo0o000
    if 21 - 21: oO0o
    if 63 - 63: Ii1i111I . o0o00Oo0O * Ii1i111I + iI11I1II1I1I
    if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - OoOO00O
    if 79 - 79: IIiIiII11i - O0O0O * Ii1I - OOooOOo . Ii1I
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 11 - 11: o0o00Oo0O * OOooOOo
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
  for IIii11Ii1i1I , Ooo00OoOOO , II1i11I in o0O00oOoOO :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + Ooo00OoOOO , 10044 , IIii11Ii1i1I , '' , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % oO00Oo0o000 / IIiI1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 18 - 18: ii
    if 57 - 57: O0oOO0 . OOooOOo * I11i - ii
    if 75 - 75: Ii / I11i . O00Oo000ooO0 . ooOoO0O00 . ooOoO0O00 / Ii1i111I
    if 94 - 94: O0oOO0 + oOo0O0Ooo
    if 56 - 56: OOooOOo % I11i
    if 40 - 40: i1IiIIIII / O00Oo000ooO0
    if 29 - 29: OoOO00O - OoOO00O / O0oOO0
    if 49 - 49: Ii1i111I + O0O0O % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
    if 4 - 4: IIiIiII11i - O0O0O % I1ii11iIi11i * Ii
    if 18 - 18: I1ii11iIi11i % o0o00Oo0O
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOooo000oOO )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in iIIi1i1 :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , Ooo00OoOOO , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oOOo )
  for II1i11I in i1IIii1iiIi :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1ii1ii11i1I + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 47 - 47: Ii1I * O0O0O + iI11I1II1I1I - O0O0O / O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0OoO00oOO0o != 'Failed' :
  oooo0OOo = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for II1i11I in oooo0OOo :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOoooo + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 86 - 86: O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if I11ii1iI11 != 'Failed' :
  ooOo00 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I11ii1iI11 )
  for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in ooOo00 :
   if I1i11 in II1i11I . lower ( ) :
    OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source - Dizi[/COLOR]' , Ooo00OoOOO , 8062 , IIii11Ii1i1I )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 43 - 43: oOo0O0Ooo / IIiI1I / O0oOO0 + iI11I1II1I1I + ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iIi1Ii1111i != 'Failed' :
  i1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi1Ii1111i )
  for Ooo00OoOOO , o00OooO0oo , OOoOOO0 , IiI , II1i11I in i1i :
   if I1i11 in II1i11I . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '- Source Scooby[/COLOR]' ) , Ooo00OoOOO , 1016 , o00OooO0oo , IiI , OOoOOO0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 33 - 33: IIiIiII11i - O00Oo000ooO0 - O0oOO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: oO0o * O00Oo000ooO0
 ooo00o0OO = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if iIi1Ii1111i != 'Failed' :
  for IiIi1i in ooo00o0OO :
   oO0 = OOO00 + IiIi1i + OooO0
   i11ii1 = Iiii ( oO0 )
   if i11ii1 != 'Failed' :
    i1iI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i11ii1 )
    for II1i11I , OOoOOO0 , Ooo00OoOOO , IIii11Ii1i1I , o0o0oOoOO0O , OOoooooooO in i1iI :
     if I1i11 in II1i11I . lower ( ) :
      o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' - Source Pandoras[/COLOR]' , Ooo00OoOOO , OOoooooooO , IIii11Ii1i1I , o0o0oOoOO0O , OOoOOO0 )
      Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
      if 32 - 32: i1IiIIIII + IIiI1I + iI11I1II1I1I * I1ii11iIi11i
      oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
      if 62 - 62: Ii
      if 2 - 2: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0O ( ) :
 if 91 - 91: O00Oo000ooO0 * OoOO00O / oO00Oo0o000 . oOo0O0Ooo . IIiI1I - IIiIiII11i
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIiII = Iiii ( Ooo00OoOOO )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIiII )
 for II1i11I , IIii11Ii1i1I , ii1111I in o0O00oOoOO :
  iII1i1ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  if I1i111I in II1i11I . lower ( ) :
   OoO00 ( II1i11I , '' , 7022 , iII1i1ii )
   if 30 - 30: Ii1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
Ooo0ooo0oo = '{ZH},' ; I11iIiI1 = '{IX},' ; i1I1iiii1Ii11 = '{LM},'
if 25 - 25: Ii / OOooOOo - oO00Oo0o000 / oO0o . I11i . I11i
def iI1iIIII1Oooo ( url ) :
 iI1I = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1I )
 for url , II1ii , OOooO0o0 , II1i11I in o0O00oOoOO :
  OoO00 ( ( II1ii ) . replace ( 'Sezon' , ' Season ' ) + ( OOooO0o0 ) . replace ( 'Bölüm' , ' Episode ' ) + II1i11I , url , 8063 , '' )
  if 11 - 11: IIiIiII11i * OoOO00O / IIiIiII11i + Ii1i111I - o0o00Oo0O
  if 51 - 51: oOo0O0Ooo + ooOoO0O00 * o0o00Oo0O / O00Oo000ooO0 / iI11I1II1I1I
  if 2 - 2: ii + o0o00Oo0O / i1IiIIIII
  if 86 - 86: Ii1I * ooOoO0O00 + IIiI1I . Ii1I
def Ooooo0O0 ( url ) :
 iI1I = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( iI1I )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 222 , '' )
  if 99 - 99: I1ii11iIi11i + Ii
  if 36 - 36: OoOO00O * oO00Oo0o000 * iI11I1II1I1I - Ii1i111I % Ii
  if 98 - 98: iI11I1II1I1I - ooOoO0O00 + O0oOO0 % Ii1i111I + O0oOO0 / O0O0O
  if 97 - 97: O00Oo000ooO0 % O0oOO0 + IIiIiII11i - O00Oo000ooO0 % oO0o + O0oOO0
def iIIII11i ( ) :
 if 97 - 97: OOooOOo % O0oOO0 . O0O0O
 iI1I = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1I )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I , OOooO0o0 in o0O00oOoOO :
  OoO00 ( II1i11I + '  -  ' + ( OOooO0o0 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ooo00OoOOO , 8063 , IIii11Ii1i1I )
  if 67 - 67: OoOO00O / Ii
def iiiIIiiIi ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , Ooo00OoOOO , 8002 , IIii11Ii1i1I )
def Oooo0oOooOO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , time , url , II1i11I , IIiI1i in o0O00oOoOO :
  o0OOOO00O0Oo ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , time ) , url , 1015 , IIii11Ii1i1I , IIiI1i )
  if 82 - 82: O0oOO0 + IIiIiII11i . oOo0O0Ooo / Ii1I
def o0ooOooO ( ) :
 if 63 - 63: O00Oo000ooO0 + iI11I1II1I1I + oOo0O0Ooo + oO00Oo0o000
 OoO00 ( 'Coronation Street' , '' , 8001 , '' )
 OoO00 ( 'Eastenders' , '' , 8002 , '' )
 OoO00 ( 'Emmerdale' , '' , 8003 , '' )
 OoO00 ( 'Hollyoaks' , '' , 8004 , '' )
 OoO00 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 72 - 72: oO0o + Ii + Ii1I
 if 96 - 96: O0O0O % ooOoO0O00 / I11i
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + IIiI1I
 if 88 - 88: o0o00Oo0O . O0O0O % oOo0O0Ooo
def iii111i ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Holly' in II1i11I :
   IIii11Ii1i1I = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 21 - 21: Ii1i111I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 50 - 50: O00Oo000ooO0 % oOo0O0Ooo
def IIoO ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'East' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 13 - 13: ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: o0o00Oo0O + oO0o . IIiI1I * I11i * IIiI1I
def OOOo0Oo0O ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Emmer' in II1i11I :
   IIii11Ii1i1I = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 48 - 48: O0oOO0 % OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: iI11I1II1I1I % oO0o + Ii
def IiOo00O0o0O ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Coro' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 86 - 86: Ii1i111I + o0o00Oo0O + I1ii11iIi11i - Ii1i111I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: IIiIiII11i % oOo0O0Ooo % oO00Oo0o000 + I1ii11iIi11i - OOooOOo
def O0Ooo0OOOo0oo ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Celeb' in II1i11I :
   IIii11Ii1i1I = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Ooo00OoOOO :
    I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ooo00OoOOO . replace ( '\\/' , '/' ) , 8006 , IIii11Ii1i1I )
   else :
    pass
    if 11 - 11: OoOO00O + IIiI1I * ooOoO0O00 % ii * OoOO00O * oO0o
def I1iO0o0O0OooOoo ( name , url ) :
 IiII1i11III = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiII1i11III :
  i1II1IIIII = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIi1i1iIi1iI = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( iIi1i1iIi1iI ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIi1i1iIi1iI = open_url ( url )
  iIii1ii = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( iIi1i1iIi1iI ) [ - 1 ]
  i1II1IIIII = iIii1ii . replace ( '\\/' , '/' )
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , '' , '' )
 Ooi111i1iIi1 . setPath ( i1II1IIIII )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ooi111i1iIi1 )
 if 24 - 24: ooOoO0O00 / oO00Oo0o000 * Ii1i111I / o0o00Oo0O
 if 88 - 88: Ii1I . oO00Oo0o000 * I1ii11iIi11i - i1IiIIIII . OOooOOo . oO00Oo0o000
def iiI1iI ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o0O00oOoOO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Ooo00OoOOO , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
 for Ooo00OoOOO , II1i11I in iIIi1i1 :
  OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Ooo00OoOOO , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
  if 74 - 74: O00Oo000ooO0 - o0o00Oo0O / oO00Oo0o000 * OoOO00O % O0oOO0 . oO00Oo0o000
def OO ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'Movies' in II1i11I :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( Ooo00OoOOO ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOoOO0oo0ooO + 'popcorn.png' )
def ooOo00oo0 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIii11Ii1i1I )
 for url in iIIi1i1 :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOoOO0oo0ooO + 'Next.png' )
  if 82 - 82: i1IiIIIII * Ii1I % OoOO00O . i1IiIIIII
  if 43 - 43: oO0o . O0oOO0 * I1ii11iIi11i
def iio00O0o00oo ( url ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url , IIii11Ii1i1I in o0O00oOoOO :
  if '{{' in II1i11I :
   pass
  else :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , IIii11Ii1i1I )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
iIiiII = '{UJ},' ; iII1I = '{WE},' ; o00oOOo0Oo = '{WP},' ; Oooo0o0oO = '{PP},'
def o0OOoOooO0ooO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url , IIii11Ii1i1I in o0O00oOoOO :
  if '{{' in II1i11I :
   pass
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , IIii11Ii1i1I )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiiiIi ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  IiI111 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiI111 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: oOo0O0Ooo % oO0o % Ii1i111I + Ii1i111I
 if 6 - 6: I1ii11iIi11i
 if 73 - 73: oO00Oo0o000 * Ii1I + I11i - I1ii11iIi11i . Ii1i111I
def o0oOOO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '(cooltvseries.com)' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
 for url , II1i11I in iIIi1i1 :
  if '(cooltvseries.com)' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
def o00OoOooo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  OOoO0oO00o ( ( url ) . replace ( ' ' , '%20' ) )
i1I1ii1 = '{XX},' ; Iii1i = '{UD},' ; ooOooo00O = '{YT},' ; I1i1I1IIiIIi = '{JS},' ; iII1ii1IIII = '{PF},'
if 98 - 98: Ii . oO00Oo0o000 * O0O0O . IIiI1I
def OOOo0o0O ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  I1IIiI ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( Ooo00OoOOO ) ) , 222 , IIii11Ii1i1I )
  if 100 - 100: o0o00Oo0O
def oOOO00Oo ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  if 'youtu' in url :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + IIii11Ii1i1I )
 for url in next :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , OOoOO0oo0ooO + 'Next.png' )
  if 48 - 48: IIiIiII11i + IIiIiII11i * ooOoO0O00 / OoOO00O
def iii11III1I ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 61 - 61: Ii1I + iI11I1II1I1I % I11i
def ooooooO0O ( url ) :
 iIi1i1iIi1iI = Iiii
 o0O00oOoOO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 222 , IIii11Ii1i1I )
  if 64 - 64: O00Oo000ooO0 * iI11I1II1I1I . Ii1I / Ii1i111I * iI11I1II1I1I
  if 4 - 4: O0oOO0 % O00Oo000ooO0 . oO00Oo0o000
  if 91 - 91: Ii1I + iI11I1II1I1I % O00Oo000ooO0
  if 90 - 90: O0oOO0 - Ii1i111I . oO0o + oO0o
  if 45 - 45: OOooOOo / ii . oO00Oo0o000 % o0o00Oo0O * Ii1I * I1ii11iIi11i
def oOO0ooO ( ) :
 if 57 - 57: IIiI1I - oOo0O0Ooo + ii / IIiI1I . O0oOO0 % ooOoO0O00
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
 if 52 - 52: o0o00Oo0O - iI11I1II1I1I / oO0o / O00Oo000ooO0
 if 29 - 29: OoOO00O * i1IiIIIII * ooOoO0O00 . OoOO00O * oO00Oo0o000 . O0oOO0
def O0iI1I1ii11IIi1 ( Cat_Name ) :
 if 100 - 100: I1ii11iIi11i . OoOO00O . oOo0O0Ooo % IIiIiII11i - O0O0O
 Oo0O00o0O0 = False
 IiIii11ii111 = '0'
 if Cat_Name == 'All Channels' : Oo0O00o0O0 = True
 if Cat_Name == 'Entertainment' : IiIii11ii111 = '1'
 if Cat_Name == 'Movies' : IiIii11ii111 = '2'
 if Cat_Name == 'Music' : IiIii11ii111 = '3'
 if Cat_Name == 'News' : IiIii11ii111 = '4'
 if Cat_Name == 'Sports' : IiIii11ii111 = '5'
 if Cat_Name == 'Documentary' : IiIii11ii111 = '6'
 if Cat_Name == 'Kids' : IiIii11ii111 = '7'
 if Cat_Name == 'Food' : IiIii11ii111 = '8'
 if Cat_Name == 'Religious' : IiIii11ii111 = '9'
 if Cat_Name == 'USA Channels' : IiIii11ii111 = '10'
 if Cat_Name == 'Other' : IiIii11ii111 = '11'
 if 75 - 75: o0o00Oo0O
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 print 'Len Match: >>>' + str ( len ( o0O00oOoOO ) )
 for II1i11I , IIii11Ii1i1I , ii1111I in o0O00oOoOO :
  iII1i1ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  if ii1111I == IiIii11ii111 :
   OoO00 ( II1i11I , '' , 7022 , iII1i1ii )
  elif Oo0O00o0O0 == True :
   OoO00 ( II1i11I , '' , 7022 , iII1i1ii )
  else : pass
  if 56 - 56: oO0o / IIiIiII11i
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 39 - 39: OOooOOo - ii - ooOoO0O00 / IIiIiII11i
def IIIii1 ( Search_Name ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , Ooo00OoOOO , OOoOooOoOOOoo , I1ii1ii11i1I in o0O00oOoOO :
  iII1i1ii = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( IIii11Ii1i1I ) . replace ( '\\' , '' )
  I1IIiI ( Search_Name + ': Link 1' , ( Ooo00OoOOO ) . replace ( '\\' , '' ) , 222 , iII1i1ii )
  I1IIiI ( Search_Name + ': Link 2' , ( OOoOooOoOOOoo ) . replace ( '\\' , '' ) , 222 , iII1i1ii )
  I1IIiI ( Search_Name + ': Link 3' , ( I1ii1ii11i1I ) . replace ( '\\' , '' ) , 222 , iII1i1ii )
  if 76 - 76: oOo0O0Ooo * i1IiIIIII
def ii111 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOoOO0oo0ooO + 'english.png' )
def IIiiI11 ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'xxx.png' )
def IiIII ( ) :
 iIi1i1iIi1iI = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , Ooo00OoOOO in o0O00oOoOO :
  I1IIiI ( II1i11I , ( Ooo00OoOOO ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'vod(1).png' )
  if 92 - 92: oOo0O0Ooo % IIiI1I
def iiiI1IiI ( url ) :
 url
 iIi11i = xbmcgui . ListItem ( II1i11I , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIi11i )
 return
 if 2 - 2: o0o00Oo0O % oO00Oo0o000 % Ii1I % I11i - I1ii11iIi11i
 if 20 - 20: I11i
def o0oo00oo0oO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1i1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIi1i1iIi1iI )
 for url , OOoOOO0 , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , ( OOoOOO0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 for url in iIIi1i1 :
  OoO00 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , OOoOO0oo0ooO + 'Next.png' )
  if 49 - 49: oOo0O0Ooo
def Iii1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIiII )
 for url , OOoOOO0 , IIii11Ii1i1I in o0O00oOoOO :
  OOooOoooOoOo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , OOoOOO0 )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 OO0OO000 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 for oooo00Oo0O in OO0OO000 :
  IiIiiIiiiiI = ( oooo00Oo0O ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o0OOOO00O0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + IIii11Ii1i1I , '' , IiIiiIiiiiI )
  if 48 - 48: O0oOO0 . Ii1I
def IiiIIIIi ( INFO ) :
 o0iI11I1II ( 'info for workout' , INFO )
 if 23 - 23: ooOoO0O00 + Ii1I + oOo0O0Ooo - O0oOO0 % ii . O00Oo000ooO0
 if 49 - 49: O0O0O . OOooOOo
 if 73 - 73: OoOO00O / oOo0O0Ooo / ii + oOo0O0Ooo
def o0OoOo0O00 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 9031 , OOoOO0oo0ooO + 'icon.png' )
def iI1i1iI1iI ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 9032 , OOoOO0oo0ooO + 'icon.png' )
def I1IIiIi ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  if '://' in II1i11I :
   pass
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOoOO0oo0ooO + 'icon.png' )
def OOOOoOoO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  I1IIiI ( II1i11I , url , 222 , OOoOO0oo0ooO + 'icon.png' )
  if 72 - 72: OOooOOo / oO00Oo0o000 * O00Oo000ooO0 % iI11I1II1I1I
  if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * i1IiIIIII / I11i
  if 34 - 34: OOooOOo
def iiI1i11I ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  if 'category' in Ooo00OoOOO :
   OoO00 ( II1i11I , 'http://www.disclose.tv/' + Ooo00OoOOO , 7010 , OOoOO0oo0ooO + 'disclose.png' )
   if 31 - 31: IIiIiII11i + i1IiIIIII - ii . Ii1i111I
   if 28 - 28: OoOO00O . Ii1I
def oOo000Oo00o ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , IIii11Ii1i1I in o0O00oOoOO :
  OoO00 ( II1i11I , 'http://www.disclose.tv/' + url , 7011 , IIii11Ii1i1I )
 for url in next :
  OoO00 ( 'NEXT' , url , 7010 , OOoOO0oo0ooO + 'Next.png' )
  if 81 - 81: ii
  if 88 - 88: o0o00Oo0O * I11i
def IIiIIiII11 ( url ) :
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
  if 96 - 96: Ii1i111I * Ii1I * OoOO00O + Ii1I % oOo0O0Ooo + Ii
  if 37 - 37: Ii1i111I % Ii1I / O0oOO0
def o0oO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOoOO0oo0ooO + 'icon.png' )
  if 53 - 53: oOo0O0Ooo
def i1Iii ( name , url , img ) :
 IIiII = Iiii ( url )
 iiI11111II = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIiII )
 I1ii1i11iI1 = len ( iiI11111II )
 if 6 - 6: o0o00Oo0O . O0oOO0 - O0O0O / Ii
 if 84 - 84: Ii1i111I / Ii1I * I11i * oO0o * i1IiIIIII * o0o00Oo0O
 if I1ii1i11iI1 == 1 :
  for OoOooOo00o in iiI11111II :
   OoOooOo00o = OoOooOo00o . replace ( 'player' , 'watch' )
   iI1IIi = OoOooOo00o + '&fv=&sou='
   II11 = Iiii ( iI1IIi )
   oo0o0O = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( II11 )
   for oooOo in oo0o0O :
    ooo0ooooo0o = False
    Resolve ( oooOo )
    if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - IIiI1I - Ii
 elif I1ii1i11iI1 > 1 :
  if 84 - 84: ooOoO0O00 - oOo0O0Ooo % IIiI1I
  for OoOooOo00o in iiI11111II :
   oO00o0oOoo = Iiii ( OoOooOo00o )
   oOOI1 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oO00o0oOoo )
   OOI1i = oOOI1
   OOI1i = ( str ( OOI1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OOI1i
   I1IIiI ( 'DOUBLE LINK' , OOI1i , 424 , '' )
   if 47 - 47: IIiI1I . OOooOOo
   for url in oOOI1 :
    OoO00 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OOoOooOoOOOoo = Google . resolve ( url )
    except :
     pass
    try :
     o0oOO0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OOoOooOoOOOoo ) )
     for I11II11IiI11 , O00oIi11Iiii1iiii in o0oOO0 :
      if 10 - 10: IIiI1I % I1ii11iIi11i
      HD_URLS . append ( I11II11IiI11 )
      SD_URLS . append ( O00oIi11Iiii1iiii )
    except :
     pass
 else :
  pass
  if 48 - 48: i1IiIIIII + oO00Oo0o000 % i1IiIIIII
def Ooo0o0000OO ( ) :
 if 8 - 8: Ii1I % O0O0O / OoOO00O
 if 37 - 37: O0O0O % oO00Oo0o000 % O0O0O
 OoO00 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOoOO0oo0ooO + 'Movies.png' )
 if 14 - 14: oO0o / oOo0O0Ooo
 OoO00 ( 'Search Movies' , '' , 7017 , OOoOO0oo0ooO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 66 - 66: I1ii11iIi11i / Ii % O0oOO0
 if 43 - 43: i1IiIIIII
def o0IiiIIII1I1i ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://cnfstudio.com/' )
 o0O00oOoOO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , 'http://cnfstudio.com/genre/' + Ooo00OoOOO , 7003 , OOoOO0oo0ooO + 'icon.png' )
  if 26 - 26: IIiI1I - I1ii11iIi11i + oOo0O0Ooo + I11i
oooOOOOO = xbmcgui . Dialog ( )
if 37 - 37: I11i * i1IiIIIII + oOo0O0Ooo . Ii1I * ii
OoooOO0 = '{UN},' ; oo0OoO = '{IG},' ; iIIi1iii1 = '{PL},' ; o00o0 = '{LO},' ; OOoOo0O0 = '{LP},' ; I1o0 = '{HA},' ; I1IiiiiI1i1I = '{XD},' ; I11i1I1 = '{TA},' ; ooOooO = '{DP},' ; oooo = '{JT},' ; IIIiI1iIIII = '{JJ},' ; o0oo00OOOo = '{MM},' ; oo0oOi1i1IIi = '{FQ},' ; o0oo0Ooo0 = '{HH},'
if 74 - 74: OoOO00O + Ii1I + oOo0O0Ooo
def i11iII1II1I1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 iIIi1II1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIi1i1iIi1iI )
 for IIii11Ii1i1I , url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , IIii11Ii1i1I )
 iIIi1II1 = iIIi1II1
 for url in iIIi1II1 :
  OoO00 ( 'Next Page' , url , 7003 , OOoOO0oo0ooO + 'Next.png' )
  if 42 - 42: iI11I1II1I1I - O0oOO0 - Ii1i111I - oO00Oo0o000
def iIiI11II ( url ) :
 if 87 - 87: I1ii11iIi11i . ii * oO00Oo0o000 * IIiIiII11i / ooOoO0O00 * OOooOOo
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  O00oO = url + '&fv=&sou='
  O00oO = O00oO . replace ( 'player' , 'watch' )
  I11IiIi1iI1ii = O0oOo0o0OOoO0 ( O00oO )
  i1I1IIIiii1 = O0oOo0o0OOoO0 ( url )
  if 76 - 76: ii
  if 42 - 42: OoOO00O * o0o00Oo0O / O0O0O
def O0oOo0o0OOoO0 ( url ) :
 if 8 - 8: ooOoO0O00 + IIiIiII11i / OoOO00O + Ii1I % OoOO00O - iI11I1II1I1I
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  Iiii1iI1i ( url )
  if 29 - 29: I1ii11iIi11i + IIiIiII11i
  if 95 - 95: O0O0O
def i11ii ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , OOoOO0oo0ooO + 'LocalM3U.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , OOoOO0oo0ooO + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 39 - 39: ooOoO0O00 . Ii1I / Ii1i111I / Ii1i111I
def ooOo0oO0O ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  I1i1 = open ( oOo0oooo00o , 'r' )
  for iIi11i in I1i1 :
   ii11 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIi11i )
   for II1i11I , Ooo00OoOOO in ii11 :
    I1IIiI ( II1i11I , Ooo00OoOOO , 222 , OOoOO0oo0ooO + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 65 - 65: oO00Oo0o000 + IIiI1I * IIiI1I
def OoOOiI ( url ) :
 if os . path . exists ( Remote ) :
  IIiII = iiIi1iI1iIii ( url )
  o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
  for II1i11I , url in o0O00oOoOO :
   url = ( url ) . strip ( )
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 54 - 54: O0oOO0 * Ii1I . IIiIiII11i / i1IiIIIII % i1IiIIIII
  if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % oO00Oo0o000
def i1iIi ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for Ooo00OoOOO in o0O00oOoOO :
  Ooo00OoOOO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + Ooo00OoOOO
 II1i11I = 'plugin.video.GenieTv'
 if 53 - 53: ooOoO0O00
 OO0oOoo ( Ooo00OoOOO , II1i11I )
 if 9 - 9: ooOoO0O00 - OOooOOo
def IIII ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for Ooo00OoOOO in o0O00oOoOO :
  Ooo00OoOOO = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + Ooo00OoOOO
 II1i11I = 'repository.GenieTv'
 if 57 - 57: iI11I1II1I1I * OoOO00O * IIiI1I / O0O0O
 OO0oOoo ( Ooo00OoOOO , II1i11I )
 if 46 - 46: OoOO00O
 if 61 - 61: I11i / O0oOO0 - IIiIiII11i
def oOoO0 ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , OOoOO0oo0ooO + 'Catagories.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 95 - 95: O0oOO0 / ii + o0o00Oo0O
 if 44 - 44: oO0o * O0O0O
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0oOoOooOOo = 'https://addons.tvaddons.ag/'
if 16 - 16: O00Oo000ooO0 % ii - O0oOO0 * OoOO00O - OoOO00O
def I1iiII1 ( ) :
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Oooo00OOo = 'https://addons.tvaddons.ag/search/?keyword=' + I1i11
 IIiII = Iiii ( Oooo00OOo )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for Ooo00OoOOO , IiIi , II1i11I in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , Ooo00OoOOO , 10054 , 'https://addons.tvaddons.ag/' + IiIi , i1iIIi1 , '' )
  if 45 - 45: oO0o + oO0o % O0oOO0
  if 36 - 36: OoOO00O * Ii1i111I . Ii1i111I / I1ii11iIi11i / oOo0O0Ooo
def oooO0ooo ( ) :
 IIiII = Iiii ( o0oOoOooOOo )
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
   if 48 - 48: O0oOO0 + i1IiIIIII . oO00Oo0o000 % IIiIiII11i + O0O0O
   if 38 - 38: O0O0O
def Addon ( url ) :
 IIiII = Iiii ( url )
 iii1i1Iiiiiii = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIiII )
 for url in iii1i1Iiiiiii :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if 'Please' in II1i11I :
   pass
  else :
   o0OOOO00O0Oo ( II1i11I , url , 10054 , 'https://addons.tvaddons.ag/' + IIii11Ii1i1I , i1iIIi1 , '' )
   if 58 - 58: I11i / Ii / o0o00Oo0O % Ii1i111I % oOo0O0Ooo
   if 86 - 86: O00Oo000ooO0 + OOooOOo / oOo0O0Ooo + Ii1i111I % Ii1i111I / Ii
def iIiI1I ( url , name ) :
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
   if 2 - 2: I11i . OoOO00O % OOooOOo
def OO0oOoo ( url , name ) :
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
 if 58 - 58: Ii1I % OoOO00O * OoOO00O - IIiI1I
def Ii1IIiI1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 9 - 9: O0oOO0 - OoOO00O % IIiIiII11i + O00Oo000ooO0 + i1IiIIIII % o0o00Oo0O
 if 65 - 65: i1IiIIIII - oO0o % Ii
def oooOoo0oOO0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , url , 1007 , IiIi )
def o0o0oooO00O0 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IiIi )
  if 33 - 33: ooOoO0O00 / oOo0O0Ooo
  if 43 - 43: ooOoO0O00 * I1ii11iIi11i
def I1II11I ( url , iconimage , name ) :
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
   iI1i ( url , iconimage , name )
   if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % O0O0O + oOo0O0Ooo % O0oOO0 / OoOO00O
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
    iI1i ( url , IiIi , name )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 36 - 36: OOooOOo . Ii
def iI1i ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oO00O0o0oOOO = ( url ) . replace ( I11iIiI1 , 'http' ) . replace ( Iii1i , '.com' ) ;
 ooooOoo00 = ( oO00O0o0oOOO ) . replace ( i1I1iiii1Ii11 , 'a' ) . replace ( I1I1O0O , 'b' ) . replace ( OO0ooO00o , 'c' ) . replace ( iII1I , 'd' ) . replace ( iIIi1iii1 , 'e' ) . replace ( oooo , 'f' ) ;
 IIIIii1111i1 = ( ooooOoo00 ) . replace ( i1I1ii1 , 'g' ) . replace ( I1o0 , 'h' ) . replace ( ooOooo00O , 'i' ) . replace ( iII1ii1IIII , 'j' ) . replace ( I1iii1 , 'k' ) . replace ( iIiiiIIiii , 'l' ) ;
 iiI1ii1 = ( IIIIii1111i1 ) . replace ( I1oOOoo0 , 'm' ) . replace ( II1OOO , 'n' ) . replace ( iiIII1I11iii , 'o' ) . replace ( ooIii , 'p' ) . replace ( o0OO00oOOO0o0 , 'q' ) . replace ( iiii , 'r' ) ;
 oOOOOOoOOoo0 = ( iiI1ii1 ) . replace ( oo0OOO0OOoOO , 's' ) . replace ( o00oOOo0Oo , 't' ) . replace ( oOoO , 'u' ) . replace ( II1i1 , 'v' ) . replace ( o0o0oo0OOo0O0 , 'w' ) . replace ( iIIiiII11i1I1 , 'x' ) ;
 Ii111Ii1iiIi1 = ( oOOOOOoOOoo0 ) . replace ( OOI11i1IIi1i1 , 'y' ) . replace ( I11i1iiiiIIIi , 'z' ) . replace ( OoooOO0 , '.' ) . replace ( oo0OoO , '(' ) . replace ( o00o0 , ')' ) . replace ( OOoOo0O0 , '/' ) ;
 Ii11Ii1 = ( Ii111Ii1iiIi1 ) . replace ( Ooo0ooo0oo , '1' ) . replace ( Oooo0o0oO , '2' ) . replace ( III , '3' ) . replace ( I11i1I1 , '4' ) . replace ( ooOooO , '5' ) . replace ( I1i1I1IIiIIi , '6' ) ;
 O0oo0OOO0O0 = ( Ii11Ii1 ) . replace ( IIIiI1iIIII , '7' ) . replace ( o0oo00OOOo , '8' ) . replace ( oo0oOi1i1IIi , '9' ) . replace ( o0oo0Ooo0 , '0' ) . replace ( ooi1i1Ii1IiIII , ':' ) . replace ( I1IIii11 , '%' ) ;
 url = ( O0oo0OOO0O0 ) . replace ( iIiiII , '-' ) . replace ( I1IiiiiI1i1I , '_' ) ;
 I1IIiI ( name , url , 222 , iconimage ) ;
 if 97 - 97: O00Oo000ooO0 - Ii1i111I / IIiIiII11i
 if 26 - 26: IIiI1I + o0o00Oo0O * IIiI1I . ooOoO0O00
def Ii11I1II1 ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1007 , IiIi )
def I11Ii1I11 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IiIi , II1i11I in o0O00oOoOO :
  OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IiIi )
  if 43 - 43: oOo0O0Ooo % O00Oo000ooO0 % Ii1I
def OO00oOo0o00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0O0o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0o )
 if 45 - 45: OOooOOo
 if 100 - 100: ooOoO0O00 % OoOO00O
def oO000O ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIi1i1iIi1iI )
 for url , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  if '-dir-' in II1i11I :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , IIii11Ii1i1I )
  else :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' , url , 1006 , IIii11Ii1i1I )
   if 62 - 62: ooOoO0O00 * iI11I1II1I1I % O0O0O % OOooOOo / ii
def iI1111iiI1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOO0ooO0Oo0 = ( 'http://afewbitsmore.com/' )
 o0O00oOoOO = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '[To Parent Directory]' in II1i11I :
   II1i11I = 'HOME'
   pass
  elif 'HOME' in II1i11I :
   pass
  elif '.m3u' in II1i11I :
   OoO00 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , OOO0ooO0Oo0 + url , 2002 , OOoOO0oo0ooO + 'music.png' )
  elif '.mp3' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OOO0ooO0Oo0 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  elif '.m4a' in II1i11I :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OOO0ooO0Oo0 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) , OOO0ooO0Oo0 + url , 1012 , OOoOO0oo0ooO + 'music.png' )
def oo000oOo0OoO0 ( url ) :
 IIiII = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for IIii11Ii1i1I , II1i11I , url in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , OOoOO0oo0ooO + 'music.png' )
  if 28 - 28: O0oOO0 % ooOoO0O00 / O0O0O
def iiI1 ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOO0ooO0Oo0 = url
 o0O00oOoOO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  if '.mp3' in II1i11I :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   OoO00 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '/' , '' ) , OOO0ooO0Oo0 + url , 1011 , OOoOO0oo0ooO + 'music.png' )
def II1II111 ( ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , IIii11Ii1i1I , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , ( 'http://www.cyn.net/music/' + Ooo00OoOOO ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + IIii11Ii1i1I ) . replace ( ' ' , '%20' ) )
def OoO00oO0o00 ( url , img ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOoOooOoOOOoo = url
 img = img
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I in o0O00oOoOO :
  I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OOoOooOoOOOoo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 25 - 25: O0oOO0 . I11i % oOo0O0Ooo + IIiI1I
def OOO0OOoOOO ( url ) :
 iIi1i1iIi1iI = iiIi1iI1iIii ( url )
 OOoOooOoOOOoo = url
 o0O00oOoOO = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIi1i1iIi1iI )
 for type , url , II1i11I in o0O00oOoOO :
  if '[VID]' in type :
   I1IIiI ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OOoOooOoOOOoo + url , 222 , OOoOO0oo0ooO + 'music.png' )
  if '[DIR]' in type :
   OOO0OOoOOO ( OOoOooOoOOOoo + url )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: Ii1I - o0o00Oo0O
 if 35 - 35: i1IiIIIII . Ii1i111I . oO00Oo0o000 - Ii1i111I % Ii1i111I + oO00Oo0o000
def oO0oO00 ( ) :
 iIiO0O = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I1i111I = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i11 = I1i111I . lower ( )
 Ooo00OoOOO = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OOoOooOoOOOoo = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1ii1ii11i1I = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 15 - 15: oOo0O0Ooo % O0O0O . I1ii11iIi11i % iI11I1II1I1I
 IIiII = i1I1iI ( Ooo00OoOOO )
 o0ooOooo000oOO = i1I1iI ( OOoOooOoOOOoo )
 Oo0oOOo = i1I1iI ( I1ii1ii11i1I )
 if 98 - 98: Ii1i111I - ooOoO0O00 % OoOO00O - ii
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for II1i11I in o0O00oOoOO :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( Ooo00OoOOO + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 19 - 19: iI11I1II1I1I + oO00Oo0o000 . oO00Oo0o000 - I1ii11iIi11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for II1i11I in iIIi1i1 :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OOoOooOoOOOoo + II1i11I ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 41 - 41: oOo0O0Ooo . I1ii11iIi11i . O00Oo000ooO0 % ii + oO0o
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  i1IIii1iiIi = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oo0oOOo )
  for II1i11I in i1IIii1iiIi :
   if I1i111I in II1i11I . lower ( ) :
    OoO00 ( ( II1i11I + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1ii1ii11i1I + II1i11I ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 23 - 23: oOo0O0Ooo - I11i % O0O0O . o0o00Oo0O * ii + O0oOO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: I1ii11iIi11i
    if 3 - 3: O00Oo000ooO0 - ii * ii - oOo0O0Ooo / oO00Oo0o000 * Ii1I
    if 58 - 58: O00Oo000ooO0 % iI11I1II1I1I / Ii % I11i . oO00Oo0o000 * IIiI1I
    if 32 - 32: ii + I11i
    if 91 - 91: O0oOO0 - oO00Oo0o000 * oO00Oo0o000
    if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
I1oOOoo0 = '{SF},' ; II1OOO = '{IF},' ; iiIII1I11iii = '{PW},' ; III = '{AM},' ; ooIii = '{GF},' ; o0OO00oOOO0o0 = '{DD},' ; iiii = '{UO},' ; oo0OOO0OOoOO = '{LE},' ; oOoO = '{ZY},' ; II1i1 = '{UE},' ; o0o0oo0OOo0O0 = '{PE},' ; iIIiiII11i1I1 = '{JE},' ; OOI11i1IIi1i1 = '{TH},' ; I11i1iiiiIIIi = '{LK},'
if 24 - 24: oO0o / oO00Oo0o000 + IIiI1I * Ii1i111I * IIiI1I
if 10 - 10: oOo0O0Ooo - Ii1I - I1ii11iIi11i - I11i
def ii1IIii ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.iwatchseries.me/tv-list/' )
 o0O00oOoOO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 8021 , OOoOO0oo0ooO + 'iwatch.png' )
def Ii1111Ii1 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIi1i1iIi1iI )
 for url , II1i11I , O00Oo0o000oO in o0O00oOoOO :
  OoO00 ( II1i11I + O00Oo0o000oO , url , 8022 , OOoOO0oo0ooO + 'iwatch.png' )
def III1Iiii1i11 ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OO00 ( url )
def OO00 ( url ) :
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
   if 10 - 10: Ii1i111I * ooOoO0O00 . O0O0O / oO00Oo0o000 . i1IiIIIII / oO00Oo0o000
def i1111I1iii1 ( ) :
 iIi1i1iIi1iI = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o0O00oOoOO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1021 , OOoOO0oo0ooO + 'anime.png' )
  if 89 - 89: O00Oo000ooO0 - ooOoO0O00 - O00Oo000ooO0
  if 74 - 74: oO0o % oO0o
def IIIII1IIiIi ( ) :
 iIi1i1iIi1iI = Iiii ( 'http://www.animetoon.org/cartoon' )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( iIi1i1iIi1iI )
 for Ooo00OoOOO , II1i11I in o0O00oOoOO :
  OoO00 ( II1i11I , Ooo00OoOOO , 1002 , OOoOO0oo0ooO + 'anime.png' )
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * i1IiIIIII
  if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
  if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % OoOO00O
def oOoOo00oo ( url ) :
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
def II11IiIIiiiii ( url , IMAGE ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( iIi1i1iIi1iI )
 for II1i11I , url in o0O00oOoOO :
  print II1i11I + '     ' + url
  if 'easy' in url :
   oooOOo0o0OOO ( url )
  elif 'playpanda' in url :
   oooOOo0o0OOO ( url )
   if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + OoOO00O % ooOoO0O00 . O0O0O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooOOo0o0OOO ( url ) :
 iIi1i1iIi1iI = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( iIi1i1iIi1iI )
 for url in o0O00oOoOO :
  I1IIiI ( 'STREAM' , url , 222 , OOoOO0oo0ooO + 'anime.png' )
  if 57 - 57: O0O0O
  if 92 - 92: IIiIiII11i - oO0o - i1IiIIIII % oOo0O0Ooo - OOooOOo * oO00Oo0o000
def IiIi11 ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oo0OooOOo0 . add_header ( 'referer' , url )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 89 - 89: IIiI1I . OOooOOo . Ii1i111I
def iiIi1iI1iIii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 55 - 55: IIiI1I + I1ii11iIi11i
def o0OOOoO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 o0Oi11i1I = ( '%s%s' % ( O00O0 , url ) )
 O00oO = iiIi1iI1iIii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , IiIi , II1i11I in o0O00oOoOO :
  I1IIiI ( '%s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + II1i11I + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IiIi )
  if 73 - 73: ii / ii
def Iiii1iI1i ( url ) :
 if 88 - 88: oO00Oo0o000 - OoOO00O - O0O0O + ooOoO0O00
 ii11IiiIi = open ( oOoOooOo0o0 , "a" )
 ii11IiiIi . write ( 'url="' + url + '"\n' )
 ii11IiiIi . close
 if 39 - 39: oO0o / I1ii11iIi11i % IIiIiII11i % Ii1i111I
 I1iiIi111I = xbmc . Player ( IiiiI1 ( ) )
 import urlresolver
 try : I1iiIi111I . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( II1i11I ) )
 I1iiIi111I = xbmc . Player ( IiiiI1 ( ) )
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
  if 57 - 57: oO0o
def oO0o0o ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % II1i11I )
 xbmc . sleep ( 1 )
 I1iiIi111I = xbmc . Player ( IiiiI1 ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % II1i11I )
 xbmc . sleep ( 1 )
 I1iiIi111I . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 94 - 94: O00Oo000ooO0 % OoOO00O % Ii . O00Oo000ooO0
def OOoO0oO00o ( url ) :
 I1iiIi111I = xbmc . Player ( IiiiI1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I1iiIi111I . play ( url ) . strip ( )
 except : pass
 if 6 - 6: oO00Oo0o000 / ii / IIiI1I / oO00Oo0o000 + IIiI1I - OOooOOo
 if 71 - 71: Ii1I . oO00Oo0o000
def IiiiI1 ( ) :
 try :
  iIiII111 = getSet ( "core-player" )
  if ( iIiII111 == 'DVDPLAYER' ) : OO0iii111 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIiII111 == 'MPLAYER' ) : OO0iii111 = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIiII111 == 'PAPLAYER' ) : OO0iii111 = xbmc . PLAYER_CORE_PAPLAYER
  else : OO0iii111 = xbmc . PLAYER_CORE_AUTO
 except : OO0iii111 = xbmc . PLAYER_CORE_AUTO
 return OO0iii111
 return True
 if 59 - 59: O0oOO0 * oO00Oo0o000
def OoO00 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0oooOo0000o0 )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 95 - 95: O0O0O
def oO0ooOoO ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: O00Oo000ooO0
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 42 - 42: ii * IIiIiII11i
def I1IIiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0oooOo0000o0 )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = False )
 return Oo
 if 53 - 53: oO00Oo0o000 + ooOoO0O00 . oO0o / Ii + OoOO00O % OOooOOo
 if 9 - 9: O0oOO0 . Ii1i111I - I1ii11iIi11i . oO00Oo0o000
 if 39 - 39: i1IiIIIII
 if 70 - 70: O00Oo000ooO0 % oO0o % oOo0O0Ooo
 if 95 - 95: OOooOOo - oO00Oo0o000 / o0o00Oo0O * oOo0O0Ooo - I11i
 if 12 - 12: iI11I1II1I1I % I1ii11iIi11i . IIiI1I . O00Oo000ooO0 % Ii
def o0iI11I1II ( heading , announce ) :
 class IIiI1I11ii1i ( ) :
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
 IIiI1I11ii1i ( )
 IIiI1I11ii1i ( )
 if 75 - 75: o0o00Oo0O
def oooooOOo0Oo ( ) :
 o0iI11I1II ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 29 - 29: o0o00Oo0O * Ii / ii / I11i . O0oOO0
 if 70 - 70: ii . O0oOO0 / O0O0O . O0O0O - I11i
 if 29 - 29: Ii1i111I % i1IiIIIII - O0oOO0
 if 26 - 26: o0o00Oo0O . Ii1i111I + IIiI1I - OoOO00O . Ii1i111I
 if 2 - 2: Ii1I . I1ii11iIi11i * i1IiIIIII % IIiIiII11i . IIiI1I
def Ii1IIiI1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
 if 47 - 47: IIiI1I * OOooOOo * O00Oo000ooO0
 if 46 - 46: OoOO00O
 if 42 - 42: iI11I1II1I1I
 if 32 - 32: I1ii11iIi11i - OoOO00O . ii - ii - I1ii11iIi11i . iI11I1II1I1I
 if 34 - 34: I1ii11iIi11i
 if 31 - 31: ooOoO0O00 - Ii1i111I + oO00Oo0o000 + O0oOO0 . O0oOO0 . o0o00Oo0O
 if 33 - 33: ooOoO0O00 / IIiI1I * oO0o
 if 2 - 2: O0O0O . i1IiIIIII
 if 43 - 43: iI11I1II1I1I
 if 29 - 29: O00Oo000ooO0 % O0oOO0 + oO0o . ooOoO0O00 + oOo0O0Ooo
 if 24 - 24: oO00Oo0o000 / OoOO00O * Ii1I - ii / oOo0O0Ooo . O0O0O
 if 98 - 98: ooOoO0O00 - IIiI1I
 if 49 - 49: I11i . OoOO00O . O0O0O
 if 9 - 9: O00Oo000ooO0 - IIiIiII11i * oO0o
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * O0O0O / IIiI1I / OOooOOo
 if 15 - 15: O0oOO0 / O0O0O
 if 54 - 54: O0oOO0 - iI11I1II1I1I - Ii1i111I % OoOO00O / IIiIiII11i
 if 80 - 80: Ii % iI11I1II1I1I / Ii
 if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - OoOO00O - iI11I1II1I1I
 if 28 - 28: OOooOOo % ii
 if 13 - 13: O00Oo000ooO0 . I1ii11iIi11i - Ii1i111I / O0O0O - I1ii11iIi11i - oOo0O0Ooo
 if 84 - 84: IIiIiII11i
 if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def O00O ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + IIIIIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 82 - 82: oO00Oo0o000 . ooOoO0O00 / O0O0O
def oooooo0Oo00o ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0OoOoOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 37 - 37: ooOoO0O00 . oO00Oo0o000 - IIiIiII11i % I11i - ooOoO0O00 . O0O0O
def iiiiI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + Ooo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 21 - 21: IIiI1I % O00Oo000ooO0 % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OO000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 1 - 1: o0o00Oo0O
def iIOOO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OoOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 15 - 15: O0oOO0 * iI11I1II1I1I * O0O0O
def O0oo0O00ooOo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oOoOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 2 - 2: O0oOO0 - Ii1i111I * ooOoO0O00 % i1IiIIIII / ii * i1IiIIIII
def OOO000ooO0OO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OoOOOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 15 - 15: i1IiIIIII * O0oOO0 + IIiIiII11i . oO00Oo0o000 . O0O0O
def I1I11iII11 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + O0O000OOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 95 - 95: OoOO00O % oOo0O0Ooo + I1ii11iIi11i * I11i * IIiI1I
def i1iII1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 42 , o00OooO0oo , o0o0oOoOO0O , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 25 - 25: I11i % IIiI1I . Ii
def i1ii ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oO0oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for II1i11I , url , o00OooO0oo , o0o0oOoOO0O , iiIi1i in o0O00oOoOO :
  o0OOOO00O0Oo ( II1i11I , url , 5 , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , iiIi1i )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 43 - 43: O0O0O + OOooOOo . oOo0O0Ooo . Ii
 if 71 - 71: I11i + i1IiIIIII . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
 if 91 - 91: o0o00Oo0O - Ii1i111I % oO00Oo0o000
 if 46 - 46: O0oOO0 / oOo0O0Ooo . O00Oo000ooO0 % oO0o / Ii
 if 13 - 13: oO00Oo0o000 % I11i + i1IiIIIII + oO00Oo0o000 + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: IIiI1I
 if 20 - 20: OoOO00O . oO00Oo0o000 % OoOO00O
 if 5 - 5: i1IiIIIII + IIiI1I
def i1ii11III1 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oOOoO0 ) :
     IIiIiIIii1 = 0
     IIiIiIIii1 += len ( i1i1I )
     if IIiIiIIii1 > 0 :
      for OOO in i1i1I :
       os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
  i11iiIII1Iii1 = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( i11iiIII1Iii1 )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Ii1i111I
 if 2 - 2: OoOO00O
 if 12 - 12: Ii - iI11I1II1I1I * O00Oo000ooO0 * IIiI1I
 if 19 - 19: o0o00Oo0O + O0O0O + I11i
 if 81 - 81: iI11I1II1I1I
 if 51 - 51: I11i . Ii1I * OoOO00O / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % oO00Oo0o000 % O0O0O + Ii1i111I * O0O0O . OoOO00O
 if 89 - 89: ii % IIiIiII11i - oO0o % Ii
 if 7 - 7: O00Oo000ooO0
def III11i ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 o0OO0OOOOOoOOOOooo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( o0OO0OOOOOoOOOOooo ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o0OO0OOOOOoOOOOooo ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 29 - 29: oO00Oo0o000 / Ii1I * oOo0O0Ooo + IIiI1I
   if 52 - 52: oO0o / OoOO00O - O00Oo000ooO0
   if IIiIiIIii1 > 0 :
    if 14 - 14: i1IiIIIII / I11i + OoOO00O / ii - Ii1i111I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 88 - 88: OoOO00O / ii % OOooOOo - ooOoO0O00
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
       if 49 - 49: I11i - iI11I1II1I1I
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  o00oo00O0OoOo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o00oo00O0OoOo ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
   if IIiIiIIii1 > 0 :
    if 27 - 27: i1IiIIIII * O00Oo000ooO0 / Ii - O0O0O + IIiIiII11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( IIiIiIIii1 ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 43 - 43: Ii1I - IIiIiII11i
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 56 - 56: Ii1I . ooOoO0O00 / IIiI1I % O0O0O / o0o00Oo0O * Ii1i111I
   else :
    pass
  oo0oOoo = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 23 - 23: ooOoO0O00
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oo0oOoo ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Ii1i111I . oO0o
   if IIiIiIIii1 > 0 :
    if 74 - 74: I1ii11iIi11i - IIiIiII11i - O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( IIiIiIIii1 ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 50 - 50: oOo0O0Ooo - O0O0O + O0O0O * Ii1i111I + O0O0O
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
   else :
    pass
    if 30 - 30: OOooOOo - Ii
    if 94 - 94: OOooOOo % IIiI1I
    if 39 - 39: OOooOOo + oO00Oo0o000 % o0o00Oo0O
    if 26 - 26: O0oOO0 + OOooOOo
 II111I1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( II111I1i1 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( II111I1i1 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 10 - 10: o0o00Oo0O . OOooOOo * O00Oo000ooO0 / oO00Oo0o000 / ooOoO0O00
   if 32 - 32: o0o00Oo0O / i1IiIIIII . O0oOO0 % oO00Oo0o000
   if IIiIiIIii1 > 0 :
    if 18 - 18: O00Oo000ooO0 * IIiI1I / Ii1i111I / o0o00Oo0O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 11 - 11: iI11I1II1I1I / OoOO00O + ii % ooOoO0O00 * Ii
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 86 - 86: Ii - o0o00Oo0O - Ii . iI11I1II1I1I . O00Oo000ooO0
   else :
    pass
    if 84 - 84: ooOoO0O00 / iI11I1II1I1I / O0O0O / OoOO00O
    if 7 - 7: OOooOOo . i1IiIIIII % I1ii11iIi11i
 o00OO000 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( o00OO000 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o00OO000 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 53 - 53: OOooOOo - ooOoO0O00 % Ii1I
   if 37 - 37: oO0o - I1ii11iIi11i
   if IIiIiIIii1 > 0 :
    if 38 - 38: Ii / oO0o
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 64 - 64: O00Oo000ooO0
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
   else :
    pass
    if 89 - 89: o0o00Oo0O + O00Oo000ooO0 * oO00Oo0o000
    if 30 - 30: OOooOOo
 IIIII11 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( IIIII11 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( IIIII11 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 48 - 48: oO00Oo0o000 / O0oOO0 . iI11I1II1I1I
   if 72 - 72: ooOoO0O00 . I11i
   if IIiIiIIii1 > 0 :
    if 3 - 3: OOooOOo % IIiIiII11i - o0o00Oo0O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 52 - 52: oO0o
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 49 - 49: OoOO00O . Ii1I % O0oOO0 . I1ii11iIi11i * i1IiIIIII
   else :
    pass
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0oOO0
    if 20 - 20: IIiI1I + I11i . oO00Oo0o000 / Ii
    if 7 - 7: OOooOOo / OOooOOo . oO00Oo0o000 * o0o00Oo0O + O00Oo000ooO0 + O0O0O
 OoO00oOO00O00 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( OoO00oOO00O00 ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( OoO00oOO00O00 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 78 - 78: oO0o % IIiIiII11i
   if 94 - 94: O0oOO0 * o0o00Oo0O
   if IIiIiIIii1 > 0 :
    if 60 - 60: IIiI1I / IIiI1I - O0oOO0 / ii + o0o00Oo0O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 55 - 55: oO0o % o0o00Oo0O / ii
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
   else :
    pass
    if 88 - 88: Ii1I * IIiI1I + IIiIiII11i
    if 62 - 62: ii
 iioOo00O0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( iioOo00O0o ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 18 - 18: O0oOO0
   if 37 - 37: I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . O0oOO0
   if IIiIiIIii1 > 0 :
    if 62 - 62: ii / O0oOO0 + Ii1I . I11i - IIiI1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 29 - 29: O0O0O
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 26 - 26: o0o00Oo0O % i1IiIIIII - O00Oo000ooO0 . i1IiIIIII
   else :
    pass
    if 70 - 70: I11i + Ii1i111I / IIiI1I + O0oOO0 / oOo0O0Ooo
    if 33 - 33: ii . o0o00Oo0O
 oOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oOo ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 8 - 8: Ii1I % oO0o % O0O0O . Ii1I * Ii1I
   if 94 - 94: Ii + ii
   if IIiIiIIii1 > 0 :
    if 20 - 20: Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 86 - 86: OOooOOo / i1IiIIIII
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 40 - 40: iI11I1II1I1I / O0oOO0 / oOo0O0Ooo + Ii1I * i1IiIIIII
   else :
    pass
    if 1 - 1: oO0o * O0oOO0 + O00Oo000ooO0 . O0O0O / O0oOO0
    if 91 - 91: OoOO00O + Ii1i111I - I1ii11iIi11i % OOooOOo . IIiI1I
 oO0OO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( oO0OO ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 89 - 89: O0O0O - oO00Oo0o000 + OOooOOo % I11i % OoOO00O - Ii
   if 34 - 34: OoOO00O - O00Oo000ooO0 + oO00Oo0o000
   if IIiIiIIii1 > 0 :
    if 92 - 92: oOo0O0Ooo / oO0o - i1IiIIIII / Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 23 - 23: IIiIiII11i / Ii - oO0o * oO0o + IIiI1I * IIiIiII11i
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 82 - 82: I11i + OoOO00O * oOo0O0Ooo - O0O0O
   else :
    pass
    if 6 - 6: i1IiIIIII / iI11I1II1I1I / O0oOO0 / oOo0O0Ooo - ooOoO0O00 - i1IiIIIII
    if 8 - 8: Ii * Ii1i111I . i1IiIIIII / i1IiIIIII
 Iii1Ii111ii1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( Iii1Ii111ii1 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + OoOO00O % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
   if 79 - 79: ii + Ii1i111I * oO00Oo0o000
   if IIiIiIIii1 > 0 :
    if 63 - 63: O0oOO0 % oOo0O0Ooo . i1IiIIIII - O0oOO0 / I1ii11iIi11i % oOo0O0Ooo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 39 - 39: I11i . ooOoO0O00 % O0O0O / Ii1i111I % o0o00Oo0O
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 100 - 100: oO00Oo0o000 - OOooOOo
   else :
    pass
    if 78 - 78: ii - OOooOOo . Ii
    if 36 - 36: O0O0O * IIiI1I + O00Oo000ooO0 * IIiI1I . Ii1I - iI11I1II1I1I
 i1IIi1ii1i1ii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( i1IIi1ii1i1ii ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 97 - 97: IIiIiII11i
   if 38 - 38: oOo0O0Ooo
   if IIiIiIIii1 > 0 :
    if 42 - 42: I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: Ii / O0oOO0
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 33 - 33: oO00Oo0o000 * O00Oo000ooO0 - o0o00Oo0O + oOo0O0Ooo / O00Oo000ooO0
   else :
    pass
    if 19 - 19: ooOoO0O00 % IIiIiII11i
    if 85 - 85: O00Oo000ooO0 - I11i % i1IiIIIII - IIiIiII11i
 o0o0OOooo0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o0o0OOooo0Oo ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 48 - 48: I11i + Ii1I / Ii1I
   if 80 - 80: ii
   if IIiIiIIii1 > 0 :
    if 65 - 65: O0O0O * ooOoO0O00 . ii % O0oOO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: Ii * IIiIiII11i - OoOO00O % ii
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 55 - 55: ooOoO0O00
   else :
    pass
    if 67 - 67: oOo0O0Ooo - oO0o
    if 60 - 60: ooOoO0O00 / iI11I1II1I1I * O0O0O + O0oOO0 + ii + IIiIiII11i
 ii1ii1111 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( iioOo00O0o ) == True :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( ii1ii1111 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 14 - 14: Ii1I * i1IiIIIII
   if 72 - 72: iI11I1II1I1I . iI11I1II1I1I / OoOO00O % oOo0O0Ooo * oO0o
   if IIiIiIIii1 > 0 :
    if 66 - 66: ooOoO0O00 + ooOoO0O00 - O00Oo000ooO0 + i1IiIIIII * OOooOOo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 95 - 95: oO0o / OoOO00O . IIiI1I
     for OOO in i1i1I :
      os . unlink ( os . path . join ( OOo0Oo0OOo0 , OOO ) )
     for o0o0 in IioO0oOOO0Ooo :
      shutil . rmtree ( os . path . join ( OOo0Oo0OOo0 , o0o0 ) )
      if 75 - 75: iI11I1II1I1I / IIiIiII11i / OoOO00O / OOooOOo
   else :
    pass
    if 77 - 77: OOooOOo
    if 31 - 31: O00Oo000ooO0 / IIiI1I
    if 97 - 97: oO0o + iI11I1II1I1I
 O0OOoo = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   i1I = os . path . join ( O0OOoo , "cache.db" )
   os . unlink ( i1I )
   if 32 - 32: O0oOO0 . O00Oo000ooO0 . IIiIiII11i
 except :
  pass
  if 25 - 25: O00Oo000ooO0 * oO00Oo0o000 - O0O0O * Ii * oOo0O0Ooo * i1IiIIIII
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % IIiI1I
 if 59 - 59: O0oOO0 % I1ii11iIi11i - O0O0O + O00Oo000ooO0
 if 33 - 33: OoOO00O + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * O00Oo000ooO0
 if 21 - 21: o0o00Oo0O * O0oOO0 % oO0o
 if 14 - 14: o0o00Oo0O / oO00Oo0o000 / O0oOO0 + O00Oo000ooO0 - O00Oo000ooO0
 if 10 - 10: o0o00Oo0O - Ii1I / oO00Oo0o000 % OOooOOo / ii / OoOO00O
 if 73 - 73: O0oOO0 + O00Oo000ooO0 % I11i . Ii1I / i1IiIIIII . oO00Oo0o000
 if 76 - 76: Ii1i111I . Ii1I * ii % IIiI1I
 if 24 - 24: ii
def ooOOo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 O000O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( O000O0 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 84 - 84: I1ii11iIi11i
   if 18 - 18: ii
   if IIiIiIIii1 > 0 :
    if 85 - 85: ii . oO0o . oO0o
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: Ii1i111I
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
 if 72 - 72: oO00Oo0o000 - O0oOO0 - oOo0O0Ooo - IIiI1I + i1IiIIIII - ooOoO0O00
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: IIiI1I % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * O0O0O + IIiI1I % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % O00Oo000ooO0 . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
 if 55 - 55: OOooOOo . iI11I1II1I1I * i1IiIIIII % iI11I1II1I1I . oO0o
 if 43 - 43: OoOO00O . i1IiIIIII + oOo0O0Ooo * Ii
 if 2 - 2: i1IiIIIII
 if 3 - 3: oOo0O0Ooo . IIiI1I % o0o00Oo0O - O0oOO0 / o0o00Oo0O
def iiII ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 O000O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( O000O0 ) :
   IIiIiIIii1 = 0
   IIiIiIIii1 += len ( i1i1I )
   if 79 - 79: OoOO00O + O0O0O % O0oOO0 % oOo0O0Ooo
   if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
   if IIiIiIIii1 > 0 :
    if 53 - 53: IIiI1I . O0O0O / I1ii11iIi11i . oO0o . Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( IIiIiIIii1 ) + " files found" , "Do you want to delete them?" ) :
     if 60 - 60: IIiIiII11i
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
 III11i ( url )
 return
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: IIiI1I + I1ii11iIi11i % Ii1i111I . O0O0O
 if 6 - 6: O00Oo000ooO0 + Ii1I
 if 62 - 62: O0O0O . oO00Oo0o000 - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
 if 63 - 63: ii * oO00Oo0o000
 if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . O0O0O % IIiIiII11i
 if 18 - 18: Ii1i111I % ii + oO0o / Ii1i111I
 if 37 - 37: ooOoO0O00 - OoOO00O / O00Oo000ooO0 . IIiIiII11i % O0oOO0
def i11iIi1I1i1 ( url , name ) :
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOOi1I111II = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 oo0O0o0o0o0o0 = os . path . join ( O0000OOO0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oo0O0o0o0o0o0 ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oOOi1I111II = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
   try :
    os . remove ( oOOi1I111II )
    print '=== GenieTv - REMOVING    ' + str ( oOOi1I111II ) + '    ==='
   except :
    pass
   O00oO = i1 . http_GET ( url ) . content
   ii1 = open ( oOOi1I111II , "w" )
   ii1 . write ( O00oO )
   ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oOOi1I111II ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oOOi1I111II = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
  try :
   os . remove ( oOOi1I111II )
   print '=== GenieTv - REMOVING    ' + str ( oOOi1I111II ) + '    ==='
  except :
   pass
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oOOi1I111II , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOOi1I111II ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 21 - 21: IIiI1I + oOo0O0Ooo / I1ii11iIi11i % iI11I1II1I1I / iI11I1II1I1I
def I11IIiII ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOOi1I111II = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 try :
  ii1 = open ( oOOi1I111II ) . read ( )
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
 if 20 - 20: oOo0O0Ooo + ooOoO0O00
def O00OO0oOOO ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOOi1I111II = os . path . join ( O0000OOO0 , 'advancedsettings.xml' )
 try :
  os . remove ( oOOi1I111II )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oOOi1I111II ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 41 - 41: O00Oo000ooO0 * ii . O0oOO0 % Ii
 if 11 - 11: iI11I1II1I1I . oO00Oo0o000 - I1ii11iIi11i / Ii1i111I + IIiIiII11i
 if 29 - 29: Ii1i111I . Ii + ooOoO0O00 - OoOO00O + o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: OoOO00O - ii + oO00Oo0o000 % I11i - OOooOOo . oOo0O0Ooo
 if 42 - 42: oO00Oo0o000
 if 70 - 70: I11i / Ii1i111I + O0O0O % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: i1IiIIIII
 if 12 - 12: OoOO00O
def i1IiI1i ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o0O00oOoOO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for i1iii , oOoOO0OO0O0 , oooO000Oo000O , iIiiI1i1I in o0O00oOoOO :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1iii , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oooO000Oo000O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iIiiI1i1I )
  inc = inc + 1
  if 100 - 100: IIiIiII11i . oO00Oo0o000 - OOooOOo % IIiIiII11i
  if 81 - 81: Ii1I - oO0o * O0O0O
  if 81 - 81: IIiI1I - OoOO00O - i1IiIIIII % O00Oo000ooO0 % I11i . iI11I1II1I1I
  if 79 - 79: Ii1I - Ii1I . OoOO00O / O00Oo000ooO0
  if 57 - 57: O0oOO0 * iI11I1II1I1I * IIiI1I * OoOO00O / OoOO00O
  if 43 - 43: o0o00Oo0O * Ii - ii - O0O0O
  if 46 - 46: O0O0O * ooOoO0O00 / Ii1I
  if 100 - 100: oOo0O0Ooo - i1IiIIIII
  if 91 - 91: I11i * Ii1I - IIiI1I . IIiIiII11i
def iI11II ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oOOi1I111II = os . path . join ( O0000OOO0 , 'addons2.ini' )
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oOOi1I111II , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOOi1I111II ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 3 - 3: oO0o % I11i % i1IiIIIII . Ii1I . Ii1I
def IiI1i1111iI1i ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  O0000OOO0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oOOi1I111II = os . path . join ( O0000OOO0 , 'settings.xml' )
  O00oO = i1 . http_GET ( url ) . content
  ii1 = open ( oOOi1I111II , "w" )
  ii1 . write ( O00oO )
  ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOOi1I111II ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 85 - 85: iI11I1II1I1I + OoOO00O - IIiIiII11i * O00Oo000ooO0 * IIiI1I
 if 17 - 17: i1IiIIIII . O0O0O - I1ii11iIi11i * iI11I1II1I1I * O0oOO0
def iiOo0OoOoOo0o ( ) :
 try :
  iiIIIi1ii = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iiIIIi1ii ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iii1IiI = os . path . join ( iiIIIi1ii , "source.db" )
    os . unlink ( iii1IiI )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 87 - 87: oOo0O0Ooo - o0o00Oo0O - Ii1i111I * oO00Oo0o000 % oO00Oo0o000
 if 99 - 99: o0o00Oo0O * Ii % i1IiIIIII * IIiIiII11i
 if 98 - 98: o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: O0oOO0 / i1IiIIIII * o0o00Oo0O
def Iiii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 17 - 17: oO0o / O0oOO0 % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / O00Oo000ooO0 . Ii / oO0o % IIiIiII11i
 if 6 - 6: IIiI1I % I11i + oO00Oo0o000
 if 91 - 91: I11i + o0o00Oo0O * O0O0O * O00Oo000ooO0 * Ii1I
 if 83 - 83: ii
 if 52 - 52: I11i / OOooOOo % O0O0O % oO0o / O00Oo000ooO0 % I11i
def O0oo ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; Ii1I1I11I1I1i = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if Ii1I1I11I1I1i :
  I1II1i = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; I1II1i = xbmc . translatePath ( I1II1i ) ;
  o00o000Oo = os . path . join ( I1II1i , ".." , ".." ) ; o00o000Oo = os . path . abspath ( o00o000Oo ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o00o000Oo ) ; IiIiIIIiI1iII = False
  try :
   for OOo0Oo0OOo0 , IioO0oOOO0Ooo , i1i1I in os . walk ( o00o000Oo , topdown = True ) :
    IioO0oOOO0Ooo [ : ] = [ o0o0 for o0o0 in IioO0oOOO0Ooo if o0o0 not in iiIIIII1i1iI ]
    for II1i11I in i1i1I :
     try : os . remove ( os . path . join ( OOo0Oo0OOo0 , II1i11I ) )
     except :
      if II1i11I not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiIiIIIiI1iII = True
      plugintools . log ( "Error removing " + OOo0Oo0OOo0 + " " + II1i11I )
    for II1i11I in IioO0oOOO0Ooo :
     try : os . rmdir ( os . path . join ( OOo0Oo0OOo0 , II1i11I ) )
     except :
      if II1i11I not in [ "Database" , "userdata" ] : IiIiIIIiI1iII = True
      plugintools . log ( "Error removing " + OOo0Oo0OOo0 + " " + II1i11I )
   if not IiIiIIIiI1iII : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0Oii1111i ( )
 if 29 - 29: ii . Ii * Ii / O0O0O
 if 73 - 73: O0oOO0 - i1IiIIIII - IIiIiII11i - iI11I1II1I1I
 if 89 - 89: I11i % O0O0O - IIiIiII11i
def I111IIi ( ) :
 oo0OoOIiI1IIIiI1I1i = [ ]
 oO00O0oO = sys . argv [ 2 ]
 if len ( oO00O0oO ) >= 2 :
  O00O00IIi1i = sys . argv [ 2 ]
  o0ooOOOo0O = O00O00IIi1i . replace ( '?' , '' )
  if ( O00O00IIi1i [ len ( O00O00IIi1i ) - 1 ] == '/' ) :
   O00O00IIi1i = O00O00IIi1i [ 0 : len ( O00O00IIi1i ) - 2 ]
  i11111i1I1IiI = o0ooOOOo0O . split ( '&' )
  oo0OoOIiI1IIIiI1I1i = { }
  for o0I1IIIi11ii11 in range ( len ( i11111i1I1IiI ) ) :
   Ii111i1I1i1i = { }
   Ii111i1I1i1i = i11111i1I1IiI [ o0I1IIIi11ii11 ] . split ( '=' )
   if ( len ( Ii111i1I1i1i ) ) == 2 :
    oo0OoOIiI1IIIiI1I1i [ Ii111i1I1i1i [ 0 ] ] = Ii111i1I1i1i [ 1 ]
    if 70 - 70: i1IiIIIII - O00Oo000ooO0 . oO00Oo0o000
 return oo0OoOIiI1IIIiI1I1i
 if 11 - 11: Ii + I11i - oO00Oo0o000 * Ii - oOo0O0Ooo
IiiIi1II1iI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
II1IIIiiI11 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1Iii1ii = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iii1I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OOo00O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
O0OoO0o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IIIIIi1 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o0Oo00oOOO0o = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
o0OoOoOo0O = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Ooo000 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OO000oo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OoOooo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oOoOOo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
OoOOOO00 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
O0O000OOOoO = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0oo0 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooOoOo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0ii1I1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o00o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OO0O0o0o0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
O0O0OOooOO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
II1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oO0oOo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
O00O0 = base64 . decodestring ( 'Q1VOVA==' )
def o0OOOO00O0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ooi111i1iIi1 . addContextMenuItems ( O0oooOo0000o0 )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = True )
 return Oo
 if 35 - 35: iI11I1II1I1I
def OOooOoooOoOo ( name , url , mode , iconimage , fanart , description ) :
 oo0ooooo00o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo = True
 Ooi111i1iIi1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooi111i1iIi1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ooi111i1iIi1 . setProperty ( "Fanart_Image" , fanart )
 Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0ooooo00o , listitem = Ooi111i1iIi1 , isFolder = False )
 return Oo
 if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
O00O00IIi1i = I111IIi ( )
Ooo00OoOOO = None
II1i11I = None
OOoooooooO = None
o00OooO0oo = None
o0o0oOoOO0O = None
iiIi1i = None
OOO00o0O = None
if 18 - 18: O0oOO0
if 92 - 92: oO0o % iI11I1II1I1I / O00Oo000ooO0 * IIiI1I . ooOoO0O00 + O0O0O
try :
 OOO00o0O = int ( O00O00IIi1i [ "fav_mode" ] )
except :
 pass
 if 24 - 24: O00Oo000ooO0 . IIiI1I * O00Oo000ooO0 % Ii . Ii + ooOoO0O00
try :
 Ooo00OoOOO = urllib . unquote_plus ( O00O00IIi1i [ "url" ] )
except :
 pass
try :
 II1i11I = urllib . unquote_plus ( O00O00IIi1i [ "name" ] )
except :
 pass
try :
 o00OooO0oo = urllib . unquote_plus ( O00O00IIi1i [ "iconimage" ] )
except :
 pass
try :
 OOoooooooO = int ( O00O00IIi1i [ "mode" ] )
except :
 pass
try :
 o0o0oOoOO0O = urllib . unquote_plus ( O00O00IIi1i [ "fanart" ] )
except :
 pass
try :
 iiIi1i = urllib . unquote_plus ( O00O00IIi1i [ "description" ] )
except :
 pass
 if 64 - 64: iI11I1II1I1I / O00Oo000ooO0 / I1ii11iIi11i - Ii1I
 if 100 - 100: O00Oo000ooO0 + ooOoO0O00 * oO0o
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OOoooooooO )
print "URL: " + str ( Ooo00OoOOO )
print "Name: " + str ( II1i11I )
print "IconImage: " + str ( o00OooO0oo )
if 64 - 64: O0O0O * Ii . I1ii11iIi11i
if 52 - 52: I1ii11iIi11i / O0oOO0 / IIiI1I - I11i / IIiI1I
def oO00OOoO00 ( content , viewType ) :
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 85 - 85: oOo0O0Ooo
if o00OooO0oo == None : o00OooO0oo = ii11iIi1I
if o0o0oOoOO0O == None : o0o0oOoOO0O = i1iIIi1
if OOoooooooO == None :
 iiIiI ( )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif OOoooooooO == 1 :
 II1i111 ( Ooo00OoOOO )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif OOoooooooO == 44 :
 OO0OoOOO0 ( Ooo00OoOOO )
 if 46 - 46: OOooOOo * Ii1i111I / O0O0O + I1ii11iIi11i + O00Oo000ooO0
elif OOoooooooO == 2 :
 IiI1 ( )
 if 95 - 95: I11i - OoOO00O
elif OOoooooooO == 3 :
 oOO ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif OOoooooooO == 21 :
 iI1Ii11111iIi ( )
 if 19 - 19: OOooOOo . i1IiIIIII . ii
elif OOoooooooO == 4 :
 IiI1iII1II111 ( )
 if 79 - 79: i1IiIIIII * O0oOO0 * oOo0O0Ooo * Ii1I / Ii1I
elif OOoooooooO == 5 :
 oOO0oo ( Ooo00OoOOO )
 if 62 - 62: O0oOO0 * OoOO00O % Ii1I - ooOoO0O00 - Ii1I
elif OOoooooooO == 6 :
 ooOOo ( Ooo00OoOOO )
 if 24 - 24: i1IiIIIII
elif OOoooooooO == 7 :
 i11iIi1I1i1 ( Ooo00OoOOO , II1i11I )
 if 71 - 71: O00Oo000ooO0 - ooOoO0O00
elif OOoooooooO == 8 :
 I11IIiII ( Ooo00OoOOO , II1i11I )
 if 56 - 56: OOooOOo + O0O0O
elif OOoooooooO == 9 :
 FIXREPOSADDONS ( Ooo00OoOOO )
 if 74 - 74: IIiI1I / oO00Oo0o000 / IIiIiII11i - IIiI1I / O0O0O % Ii1i111I
elif OOoooooooO == 10 :
 Ii1IIiI1i ( )
 if 19 - 19: O00Oo000ooO0 % ii + ii
elif OOoooooooO == 11 :
 O00OO0oOOO ( Ooo00OoOOO )
 if 7 - 7: ooOoO0O00
elif OOoooooooO == 12 :
 i1IiI1i ( )
 if 91 - 91: OOooOOo - OOooOOo . O00Oo000ooO0
elif OOoooooooO == 13 :
 i1ii11III1 ( )
 if 33 - 33: oO00Oo0o000 - iI11I1II1I1I / OoOO00O % o0o00Oo0O
elif OOoooooooO == 14 :
 III11i ( Ooo00OoOOO )
 if 80 - 80: O00Oo000ooO0 % ii - O00Oo000ooO0
elif OOoooooooO == 15 :
 II11i11Iii ( )
 if 27 - 27: oO00Oo0o000 - I11i * Ii1I - oOo0O0Ooo
elif OOoooooooO == 16 :
 iI11II ( Ooo00OoOOO , II1i11I )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIiI1I . OoOO00O
elif OOoooooooO == 17 :
 IiI1i1111iI1i ( Ooo00OoOOO , II1i11I )
 if 100 - 100: IIiIiII11i / oO00Oo0o000 / IIiI1I - Ii1I * iI11I1II1I1I
elif OOoooooooO == 18 :
 iiOo0OoOoOo0o ( )
 if 7 - 7: ooOoO0O00 . O00Oo000ooO0 % Ii * Ii1I . Ii1i111I % Ii1I
elif OOoooooooO == 19 :
 I11iiIi1i1 ( Ooo00OoOOO )
 if 35 - 35: oOo0O0Ooo
elif OOoooooooO == 40 :
 ooOo0OoOooo00 ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif OOoooooooO == 42 :
 IIo0OoO00 ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 22 - 22: O0oOO0 . Ii . ii . ooOoO0O00
elif OOoooooooO == 43 :
 ooooOooooOOo ( Ooo00OoOOO )
 if 12 - 12: OOooOOo % i1IiIIIII + O0O0O . o0o00Oo0O % iI11I1II1I1I
elif OOoooooooO == 20 :
 O0o0O0OO00o ( Ooo00OoOOO )
 if 41 - 41: ii
elif OOoooooooO == 22 :
 O00O ( Ooo00OoOOO )
 if 13 - 13: Ii1i111I + oO00Oo0o000 - oO00Oo0o000 % O0O0O / Ii1i111I
elif OOoooooooO == 23 :
 oooooo0Oo00o ( Ooo00OoOOO )
 if 4 - 4: oOo0O0Ooo + i1IiIIIII - O00Oo000ooO0 + IIiI1I
elif OOoooooooO == 24 :
 iiiiI ( Ooo00OoOOO )
 if 78 - 78: OoOO00O
elif OOoooooooO == 25 :
 OoOoooOO00OO ( Ooo00OoOOO )
 if 29 - 29: IIiIiII11i
elif OOoooooooO == 26 :
 iIOOO ( Ooo00OoOOO )
 if 79 - 79: iI11I1II1I1I - Ii + O0oOO0 - IIiIiII11i . iI11I1II1I1I
elif OOoooooooO == 27 :
 O0oo0O00ooOo ( Ooo00OoOOO )
 if 84 - 84: I1ii11iIi11i % Ii1i111I * o0o00Oo0O * Ii1i111I
elif OOoooooooO == 28 :
 OOO000ooO0OO ( Ooo00OoOOO )
 if 66 - 66: i1IiIIIII / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0oOO0
elif OOoooooooO == 29 :
 I1I11iII11 ( Ooo00OoOOO )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif OOoooooooO == 30 :
 o0O0 ( Ooo00OoOOO )
 if 37 - 37: ooOoO0O00 * Ii
elif OOoooooooO == 31 :
 i1iII1 ( Ooo00OoOOO )
 if 95 - 95: Ii % oO00Oo0o000 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif OOoooooooO == 32 :
 i11111I1IOoo0ooOOOOoOo ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / i1IiIIIII / oO00Oo0o000
elif OOoooooooO == 33 :
 Iii111Ii ( )
 if 35 - 35: IIiI1I * i1IiIIIII
elif OOoooooooO == 35 :
 Oo0 ( Ooo00OoOOO )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif OOoooooooO == 34 :
 oooOO0OO0O ( Ooo00OoOOO )
 if 13 - 13: oO0o * oO00Oo0o000 + I1ii11iIi11i - O00Oo000ooO0
elif OOoooooooO == 36 :
 IIiiIIIi ( Ooo00OoOOO )
 if 31 - 31: oO0o
elif OOoooooooO == 37 :
 iIIiI1I1i ( Ooo00OoOOO )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif OOoooooooO == 38 :
 I111IIiii1Ii ( Ooo00OoOOO )
 if 77 - 77: Ii - oO00Oo0o000 . Ii1I % I1ii11iIi11i . OoOO00O
elif OOoooooooO == 41 :
 O0oo ( O00O00IIi1i )
 if 9 - 9: I11i
elif OOoooooooO == 39 :
 i1ii ( Ooo00OoOOO )
 if 55 - 55: i1IiIIIII % iI11I1II1I1I + Ii1i111I . O0oOO0
elif OOoooooooO == 45 :
 TEXTS ( )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif OOoooooooO == 46 :
 oooooOOo0Oo ( )
 if 23 - 23: Ii
elif OOoooooooO == 47 :
 GEVID ( )
 if 88 - 88: IIiIiII11i - IIiI1I / ii
elif OOoooooooO == 48 :
 OoOO ( II1i11I , Ooo00OoOOO , iiIi1i )
 if 71 - 71: Ii1I
elif OOoooooooO == 49 :
 ooO00O0O0 ( )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif OOoooooooO == 222 :
 Iiii1iI1i ( Ooo00OoOOO )
 if 1 - 1: O00Oo000ooO0 % ooOoO0O00
elif OOoooooooO == 333 :
 o0OOOoO ( Ooo00OoOOO )
 if 41 - 41: oO0o * oO0o / IIiI1I + Ii1I . I11i
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / OoOO00O
elif OOoooooooO == 1020 :
 i1111I1iii1 ( )
 if 80 - 80: Ii1I
elif OOoooooooO == 1021 :
 ANIMEEP ( )
 if 67 - 67: IIiIiII11i
elif OOoooooooO == 1022 :
 ANIMEPLAY ( Ooo00OoOOO )
 if 2 - 2: I11i - o0o00Oo0O * OoOO00O % O00Oo000ooO0
elif OOoooooooO == 1001 :
 IIIII1IIiIi ( )
 if 64 - 64: ooOoO0O00 . O0oOO0
elif OOoooooooO == 1005 :
 Ii11I1II1 ( )
 if 7 - 7: O0O0O . IIiI1I - IIiI1I / oO00Oo0o000 % I1ii11iIi11i
elif OOoooooooO == 1007 :
 I11Ii1I11 ( Ooo00OoOOO )
 if 61 - 61: O0O0O - Ii1I / IIiI1I % Ii1I + oO0o / I1ii11iIi11i
elif OOoooooooO == 1010 :
 oO000O ( Ooo00OoOOO )
 if 10 - 10: Ii / OOooOOo
elif OOoooooooO == 1011 :
 iiI1 ( Ooo00OoOOO )
 if 27 - 27: oOo0O0Ooo / ii
elif OOoooooooO == 1012 :
 iI1111iiI1 ( Ooo00OoOOO )
 if 74 - 74: Ii1I % oO00Oo0o000 - oO0o * Ii1i111I . ii * oO0o
elif OOoooooooO == 1030 :
 II1II111 ( )
 if 99 - 99: OOooOOo . IIiI1I - ii - o0o00Oo0O
elif OOoooooooO == 1031 :
 OoO00oO0o00 ( Ooo00OoOOO , o00OooO0oo )
 if 6 - 6: i1IiIIIII
elif OOoooooooO == 1032 :
 OOO0OOoOOO ( Ooo00OoOOO )
 if 3 - 3: o0o00Oo0O - oO00Oo0o000 * OoOO00O * i1IiIIIII / OoOO00O
elif OOoooooooO == 1006 :
 Parse . ParseURL ( Ooo00OoOOO )
 if 58 - 58: OoOO00O * iI11I1II1I1I + O0oOO0 . O0oOO0
elif OOoooooooO == 2030 :
 Parse . addonParseURL ( Ooo00OoOOO )
 if 74 - 74: O0oOO0 - I11i * O00Oo000ooO0 % O0oOO0
elif OOoooooooO == 2031 :
 Parse . apkParseURL ( Ooo00OoOOO )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * oO00Oo0o000 - oO0o - I11i
elif OOoooooooO == 1002 :
 oOoOo00oo ( Ooo00OoOOO )
 if 44 - 44: ii
elif OOoooooooO == 1003 :
 II11IiIIiiiii ( Ooo00OoOOO , o00OooO0oo )
 if 82 - 82: OOooOOo . OOooOOo
elif OOoooooooO == 1004 :
 oooOOo0o0OOO ( Ooo00OoOOO )
 if 10 - 10: I1ii11iIi11i * Ii1I . O0O0O . ii . i1IiIIIII * Ii1I
elif OOoooooooO == 1008 :
 OOOo0o0O ( )
 if 80 - 80: oO00Oo0o000 + Ii1i111I . oO00Oo0o000 + i1IiIIIII
elif OOoooooooO == 1009 :
 OoOOiI ( Ooo00OoOOO )
 if 85 - 85: Ii . Ii1i111I + OoOO00O / OoOO00O
elif OOoooooooO == 2001 :
 ooOo0oO0O ( )
 if 43 - 43: O00Oo000ooO0 . ii - IIiIiII11i
elif OOoooooooO == 2002 :
 oo000oOo0OoO0 ( Ooo00OoOOO )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * i1IiIIIII * O0O0O
elif OOoooooooO == 1013 :
 iI ( )
elif OOoooooooO == 10111113 :
 i1oOOOOOOOoO ( Ooo00OoOOO )
 if 19 - 19: oO00Oo0o000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif OOoooooooO == 1014 :
 iiiIIiiIi ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif OOoooooooO == 1015 :
 Oooo0oOooOO ( Ooo00OoOOO )
 if 15 - 15: OoOO00O + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif OOoooooooO == 1016 :
 I1II11I ( Ooo00OoOOO , o00OooO0oo , II1i11I )
 if 54 - 54: O00Oo000ooO0 - IIiIiII11i . O0oOO0 + OoOO00O
elif OOoooooooO == 1017 :
 o0O0o0 ( )
 if 45 - 45: O0O0O + IIiIiII11i . IIiI1I / Ii1I
elif OOoooooooO == 1023 :
 ii1ii11 ( )
 if 76 - 76: OoOO00O + IIiI1I - O00Oo000ooO0 * iI11I1II1I1I % ooOoO0O00
elif OOoooooooO == 1024 :
 oooOoo0oOO0 ( Ooo00OoOOO )
 if 72 - 72: O0oOO0 + IIiIiII11i . o0o00Oo0O - IIiI1I / ii . oO00Oo0o000
elif OOoooooooO == 1025 :
 o0o0oooO00O0 ( Ooo00OoOOO )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif OOoooooooO == 4001 :
 I11IiI ( )
 if 32 - 32: ii
elif OOoooooooO == 4002 :
 ooO0oOOooOo0 ( )
 if 29 - 29: Ii1I
elif OOoooooooO == 4003 :
 OOO0oOoO0O ( )
 if 41 - 41: OoOO00O
elif OOoooooooO == 4004 :
 oOo00oOoO000 ( )
 if 49 - 49: OoOO00O % IIiIiII11i . OoOO00O - I11i - Ii1i111I * O00Oo000ooO0
elif OOoooooooO == 4005 :
 Ii1iI1I1 ( )
 if 47 - 47: o0o00Oo0O . I11i / OoOO00O * IIiI1I
elif OOoooooooO == 4006 :
 oooOo0OOOoo0 ( )
 if 63 - 63: oO00Oo0o000 - O0O0O - IIiI1I - O0oOO0 / O0O0O + oO0o
elif OOoooooooO == 4007 :
 OOoOO0o0o0 ( )
 if 94 - 94: O00Oo000ooO0 / oOo0O0Ooo . IIiIiII11i
elif OOoooooooO == 4008 :
 ii1I1 ( )
 if 32 - 32: O0O0O . i1IiIIIII % i1IiIIIII . OOooOOo
elif OOoooooooO == 4009 : OOooo0oOO0O ( )
elif OOoooooooO == 4010 : IIiiI ( )
elif OOoooooooO == 3000 :
 i11ii ( )
 if 37 - 37: i1IiIIIII + o0o00Oo0O + i1IiIIIII . IIiI1I . I11i
elif OOoooooooO == 3001 :
 O0o0O00o0o ( )
 if 78 - 78: oOo0O0Ooo / Ii1i111I + I11i . I1ii11iIi11i / o0o00Oo0O
elif OOoooooooO == 3002 :
 II1IIiiI1 ( Ooo00OoOOO )
 if 49 - 49: Ii1I
elif OOoooooooO == 3003 :
 O00O00 ( Ooo00OoOOO )
 if 66 - 66: I11i . Ii1I
elif OOoooooooO == 3004 :
 o0oOOOOoo0 ( Ooo00OoOOO )
 if 18 - 18: I1ii11iIi11i + O00Oo000ooO0
elif OOoooooooO == 404 :
 OO00oOo0o00 ( II1i11I , Ooo00OoOOO , o00OooO0oo )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % OoOO00O . oOo0O0Ooo
elif OOoooooooO == 405 :
 oO0o0o ( Ooo00OoOOO )
 if 43 - 43: oOo0O0Ooo % Ii1I * OoOO00O
elif OOoooooooO == 7030 :
 oOO0ooO ( )
 if 31 - 31: OoOO00O / IIiI1I
elif OOoooooooO == 7021 :
 O0iI1I1ii11IIi1 ( II1i11I )
 if 3 - 3: O00Oo000ooO0
elif OOoooooooO == 7022 :
 IIIii1 ( II1i11I )
 if 37 - 37: OoOO00O * ii * Ii1i111I + I1ii11iIi11i . oOo0O0Ooo
elif OOoooooooO == 7000 :
 i1Iii ( II1i11I , Ooo00OoOOO , img )
 if 61 - 61: i1IiIIIII . i1IiIIIII
elif OOoooooooO == 7050 :
 oOOO00Oo ( Ooo00OoOOO )
 if 17 - 17: IIiIiII11i / O0oOO0
elif OOoooooooO == 7051 :
 iii11III1I ( Ooo00OoOOO )
 if 80 - 80: i1IiIIIII * oO0o + OoOO00O
elif OOoooooooO == 7052 :
 o0oOOO ( Ooo00OoOOO )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif OOoooooooO == 7053 :
 o00OoOooo ( Ooo00OoOOO )
 if 98 - 98: I11i * I1ii11iIi11i - OoOO00O . O0oOO0
elif OOoooooooO == 7054 :
 CoolPlay ( Ooo00OoOOO )
 if 2 - 2: I1ii11iIi11i - O0oOO0 % iI11I1II1I1I
elif OOoooooooO == 7060 :
 OO ( )
 if 88 - 88: oO00Oo0o000 - oO0o
elif OOoooooooO == 7061 :
 iio00O0o00oo ( Ooo00OoOOO )
 if 79 - 79: IIiI1I
elif OOoooooooO == 7063 :
 ooOo00oo0 ( Ooo00OoOOO )
 if 45 - 45: IIiIiII11i + IIiI1I . Ii1i111I . o0o00Oo0O * ooOoO0O00 - OoOO00O
elif OOoooooooO == 7062 :
 o0OOoOooO0ooO ( Ooo00OoOOO )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif OOoooooooO == 7064 :
 NATatozcat ( )
 if 76 - 76: Ii1I
elif OOoooooooO == 7067 :
 IiiiIi ( Ooo00OoOOO )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . OoOO00O
elif OOoooooooO == 7066 :
 NATatozA ( Ooo00OoOOO )
 if 51 - 51: OoOO00O + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif OOoooooooO == 7065 :
 IiI111 ( Ooo00OoOOO )
 if 20 - 20: oO00Oo0o000 . Ii1i111I . OoOO00O + Ii1i111I - i1IiIIIII * O0O0O
elif OOoooooooO == 7070 :
 iiI1iI ( )
 if 82 - 82: oO0o
elif OOoooooooO == 7071 :
 DIZIlist ( Ooo00OoOOO )
 if 78 - 78: IIiIiII11i / Ii1i111I - Ii + Ii1I * I1ii11iIi11i
elif OOoooooooO == 7072 :
 DIZIpull ( Ooo00OoOOO )
 if 17 - 17: OOooOOo
elif OOoooooooO == 7073 :
 WATCHDIZI ( Ooo00OoOOO )
 if 72 - 72: IIiI1I . I1ii11iIi11i - Ii / oOo0O0Ooo
elif OOoooooooO == 7002 :
 o0IiiIIII1I1i ( )
 if 64 - 64: O0O0O
elif OOoooooooO == 7003 :
 i11iII1II1I1 ( Ooo00OoOOO )
 if 80 - 80: I11i % iI11I1II1I1I
elif OOoooooooO == 7004 :
 iIiI11II ( Ooo00OoOOO )
 if 63 - 63: O00Oo000ooO0 * Ii
elif OOoooooooO == 7020 :
 O0oOo0o0OOoO0 ( Ooo00OoOOO )
 if 86 - 86: Ii1i111I % Ii1i111I - OOooOOo + oO00Oo0o000 / oOo0O0Ooo * ii
elif OOoooooooO == 7001 :
 iiI1i11I ( )
 if 26 - 26: IIiIiII11i * IIiI1I + I11i / o0o00Oo0O + ooOoO0O00 - Ii1i111I
elif OOoooooooO == 7010 :
 oOo000Oo00o ( Ooo00OoOOO )
 if 56 - 56: i1IiIIIII
elif OOoooooooO == 7011 :
 IIiIIiII11 ( Ooo00OoOOO )
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + O00Oo000ooO0 - Ii1i111I
elif OOoooooooO == 7012 :
 o0oO ( Ooo00OoOOO )
 if 81 - 81: Ii1I + ii - i1IiIIIII * o0o00Oo0O
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
 Ooo0o0000OO ( )
elif OOoooooooO == 7019 :
 CNF_Studio_Indexer . List_Movies ( Ooo00OoOOO )
elif OOoooooooO == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Ooo00OoOOO )
elif OOoooooooO == 7024 :
 CNF_Studio_Indexer . Box_Office ( Ooo00OoOOO )
 if 100 - 100: iI11I1II1I1I - OOooOOo
elif OOoooooooO == 8000 :
 o0ooOooO ( )
elif OOoooooooO == 8001 :
 IiOo00O0o0O ( )
elif OOoooooooO == 8002 :
 IIoO ( )
elif OOoooooooO == 8003 :
 OOOo0Oo0O ( )
elif OOoooooooO == 8004 :
 iii111i ( )
elif OOoooooooO == 8005 :
 O0Ooo0OOOo0oo ( )
elif OOoooooooO == 8006 :
 I1iO0o0O0OooOoo ( II1i11I , Ooo00OoOOO )
elif OOoooooooO == 8030 :
 iiI1i11II ( Ooo00OoOOO )
elif OOoooooooO == 8045 :
 oo0OoOO0000 ( Ooo00OoOOO )
elif OOoooooooO == 8046 :
 i11Ii1iIIIIi ( Ooo00OoOOO )
elif OOoooooooO == 8047 :
 I1IIIIIi1IIiI ( Ooo00OoOOO )
elif OOoooooooO == 8048 :
 I1iIi1iIIIIiI ( Ooo00OoOOO )
elif OOoooooooO == 8049 :
 O000oooOO0Oo0 ( Ooo00OoOOO )
elif OOoooooooO == 8020 :
 ii1IIii ( )
elif OOoooooooO == 8021 :
 Ii1111Ii1 ( Ooo00OoOOO )
elif OOoooooooO == 8022 :
 III1Iiii1i11 ( Ooo00OoOOO )
elif OOoooooooO == 8023 :
 OO00 ( Ooo00OoOOO )
elif OOoooooooO == 8040 :
 OOoO0oO00oOOO0OoO0oo0OO ( )
elif OOoooooooO == 8041 :
 III1ii ( Ooo00OoOOO )
elif OOoooooooO == 8042 :
 o0oOoO00 ( Ooo00OoOOO )
elif OOoooooooO == 8043 :
 yt . PlayVideo ( Ooo00OoOOO )
elif OOoooooooO == 8044 :
 oOO000 ( Ooo00OoOOO )
elif OOoooooooO == 8060 :
 oOOOO0oo0O0OO ( )
elif OOoooooooO == 8061 :
 O0OOoo0o ( Ooo00OoOOO )
elif OOoooooooO == 8064 :
 iIi ( )
elif OOoooooooO == 8065 :
 iIiiI1Ii111i ( Ooo00OoOOO )
elif OOoooooooO == 8070 :
 ooO ( )
elif OOoooooooO == 8071 :
 IIi1ii ( Ooo00OoOOO )
elif OOoooooooO == 7080 :
 Ii1i1i ( Ooo00OoOOO )
elif OOoooooooO == 8090 :
 O00o ( )
elif OOoooooooO == 8091 :
 o0o0ooOo00 ( Ooo00OoOOO )
elif OOoooooooO == 8092 :
 OO00oO0OoO0o ( Ooo00OoOOO )
elif OOoooooooO == 8081 :
 iIIII11i ( )
elif OOoooooooO == 8062 :
 iI1iIIII1Oooo ( Ooo00OoOOO )
elif OOoooooooO == 8063 :
 Ooooo0O0 ( Ooo00OoOOO )
elif OOoooooooO == 8050 :
 ii1iI1II11ii ( )
elif OOoooooooO == 8051 :
 i1i1IiIiIi1Ii ( Ooo00OoOOO )
elif OOoooooooO == 8052 :
 oO0ooOO ( Ooo00OoOOO )
elif OOoooooooO == 8085 :
 o0OOO00ooo ( )
elif OOoooooooO == 8086 :
 oOoO00O ( Ooo00OoOOO )
elif OOoooooooO == 8087 :
 I1i1iII1I11 ( Ooo00OoOOO )
elif OOoooooooO == 8088 :
 o00OOo0o0O ( Ooo00OoOOO , II1i11I )
elif OOoooooooO == 9000 :
 ii1i1i1IiII ( )
elif OOoooooooO == 1111 :
 oO0oO00 ( )
elif OOoooooooO == 9001 :
 OO0Oo00Oo ( )
elif OOoooooooO == 9002 :
 OooOoOOO00O ( )
elif OOoooooooO == 9003 :
 oo0O ( )
elif OOoooooooO == 50 :
 OO00OOoO0o ( Ooo00OoOOO )
elif OOoooooooO == 9020 :
 champlist ( )
elif OOoooooooO == 9021 :
 ii111 ( )
elif OOoooooooO == 9022 :
 IIiiI11 ( )
elif OOoooooooO == 9023 :
 IiIII ( )
elif OOoooooooO == 9024 :
 iiiI1IiI ( Ooo00OoOOO )
elif OOoooooooO == 9030 :
 o0OoOo0O00 ( Ooo00OoOOO )
elif OOoooooooO == 9031 :
 iI1i1iI1iI ( Ooo00OoOOO )
elif OOoooooooO == 9032 :
 I1IIiIi ( Ooo00OoOOO )
elif OOoooooooO == 9033 :
 OOOOoOoO ( Ooo00OoOOO )
elif OOoooooooO == 7085 :
 o0oo00oo0oO ( Ooo00OoOOO )
elif OOoooooooO == 7086 :
 Iii1 ( Ooo00OoOOO )
elif OOoooooooO == 7087 :
 IiiIIIIi ( iiIi1i )
elif OOoooooooO == 9666 :
 iiII ( Ooo00OoOOO )
elif OOoooooooO == 10100 : oOO00OO0OooOo ( )
elif OOoooooooO == 10105 : OooIii1I1iI ( Ooo00OoOOO )
elif OOoooooooO == 10106 : II1iI1iiiI ( Ooo00OoOOO )
elif OOoooooooO == 10104 : OO0000 ( Ooo00OoOOO )
elif OOoooooooO == 10107 : O0O0 ( )
elif OOoooooooO == 10103 : Ii11IiI111 ( Ooo00OoOOO )
elif OOoooooooO == 10108 : OooOO ( Ooo00OoOOO )
elif OOoooooooO == 10107 : O0O0 ( )
elif OOoooooooO == 10000 : Origin_Menu ( )
elif OOoooooooO == 10001 : oOo000O ( )
elif OOoooooooO == 10002 : i1IiI1Iiii ( )
elif OOoooooooO == 10003 : O000oO0O ( )
elif OOoooooooO == 10004 : iI1iIIII1 ( Ooo00OoOOO )
elif OOoooooooO == 10005 : oO0Ooo0OooOOo ( )
elif OOoooooooO == 10006 : II1o0ooO0OOO ( Ooo00OoOOO )
elif OOoooooooO == 10007 : oo0 ( Ooo00OoOOO , o00OooO0oo )
elif OOoooooooO == 10008 : o0ooo0o0 ( )
elif OOoooooooO == 10009 : II1II1i ( )
elif OOoooooooO == 10010 : I11II1i1 ( Ooo00OoOOO )
elif OOoooooooO == 10011 : ooO0 ( Ooo00OoOOO )
elif OOoooooooO == 10012 : OOoO0oO00o ( Ooo00OoOOO )
elif OOoooooooO == 10013 : OooO0O0Ooo ( Ooo00OoOOO )
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
elif OOoooooooO == 10050 : oOoO0 ( )
elif OOoooooooO == 10051 : oooO0ooo ( )
elif OOoooooooO == 10052 : I1iiII1 ( )
elif OOoooooooO == 10053 : Addon ( Ooo00OoOOO )
elif OOoooooooO == 10054 : iIiI1I ( Ooo00OoOOO , II1i11I )
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
 OOO0o0 ( II1i11I , Ooo00OoOOO , o00OooO0oo , o0o0oOoOO0O , OOO00o0O )
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
elif OOoooooooO == 50003 : I1iiIi1 ( iiIi1i )
if 28 - 28: I1ii11iIi11i . o0o00Oo0O . Ii1i111I
if 60 - 60: IIiIiII11i + oO00Oo0o000 / O0O0O % ii - ooOoO0O00
if 57 - 57: O0oOO0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
