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
IiiIII111iI = "3.0.5"
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
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SERVER 1[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SERVER 2[/COLOR]' , ( i1111 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
def o0oO0O0o0O00O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 url = url
 o0O00oOoOO = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for OooooOOoo0 , i1I1IiiIi1i in o0O00oOoOO :
  if '[DIR]' in OooooOOoo0 :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 1018 , OOoOO0oo0ooO + 'SilentHunter.png' )
  if 'mkv' in i1I1IiiIi1i :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 222 , OOoOO0oo0ooO + 'SilentHunter.png' )
  if 'avi' in i1I1IiiIi1i :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + i1I1IiiIi1i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i1I1IiiIi1i , 222 , OOoOO0oo0ooO + 'SilentHunter.png' )
   if 70 - 70: O0O0O
def oOOoO0o0oO ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 if 93 - 93: O00Oo000ooO0 * ii + O0oOO0
def IiII111i1i11 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'SearchCartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( OOO00O ) , 21004 , OOoOO0oo0ooO + 'watchcartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 10001 , OOoOO0oo0ooO + 'Cartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , OOoOO0oo0ooO + 'anime.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def i111iIi1i1II1 ( ) :
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
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
 if 19 - 19: Ii1I % ii % O00Oo000ooO0 * I11i % o0o00Oo0O
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
def ooOOoooooo ( ) :
 IIiII = Iiii ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o0O00oOoOO = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIiII )
 for IIi1i in o0O00oOoOO :
  IIi1i = ( str ( IIi1i ) )
  if os . path . exists ( xbmc . translatePath ( IIi1i ) ) :
   i1i1iI1iiiI = ( IIi1i ) . replace ( 'special://home/addons/' , '' )
   o0iI11I1II ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1i1iI1iiiI + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   Ooo0oOooo0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if Ooo0oOooo0 == 0 :
    I1I1iIiII1 ( IIi1i )
    oOOOoo00 ( )
   elif Ooo0oOooo0 == 1 :
    iiIiIIIiiI ( IIi1i )
  else :
   pass
   if 12 - 12: o0o00Oo0O - I11i
def iiIiIIIiiI ( addon ) :
 i1i1iI1iiiI = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 81 - 81: OOooOOo - OOooOOo . IIiI1I
def I1I1iIiII1 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 o0OoOo00o0o = os . path . join ( iiI1IiI , 'default.py' )
 I1II1I11I1I = open ( o0OoOo00o0o , "w+" )
 if 54 - 54: ii + I11i - ooOoO0O00 % Ii
 I1II1I11I1I . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I1II1I11I1I . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I1II1I11I1I . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 3 - 3: I11i % I11i
 if 83 - 83: IIiIiII11i + oO00Oo0o000
 if 73 - 73: IIiI1I
 if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % Ii1i111I
 if 41 - 41: O00Oo000ooO0 / o0o00Oo0O
 if 51 - 51: Ii1i111I % oOo0O0Ooo
 if 60 - 60: oOo0O0Ooo / i1IiIIIII . oOo0O0Ooo / oO00Oo0o000 . O00Oo000ooO0
 if 92 - 92: OOooOOo + oO00Oo0o000 * OoOO00O % oOo0O0Ooo
 if 42 - 42: I1ii11iIi11i
 if 76 - 76: oOo0O0Ooo * IIiI1I % oO00Oo0o000
 if 57 - 57: iI11I1II1I1I - ooOoO0O00 / oO00Oo0o000 - o0o00Oo0O * ii % IIiIiII11i
 if 68 - 68: ii * Ii1i111I % OOooOOo - O00Oo000ooO0
 if 34 - 34: oO00Oo0o000 . iI11I1II1I1I * OOooOOo * O0O0O / oO00Oo0o000 / Ii1I
 if 78 - 78: I1ii11iIi11i - I11i / OOooOOo
 if 10 - 10: IIiI1I + I1ii11iIi11i * Ii1I + iI11I1II1I1I / oO00Oo0o000 / Ii1I
 if 42 - 42: oOo0O0Ooo
 if 38 - 38: i1IiIIIII + IIiIiII11i % O0oOO0 % OOooOOo - OoOO00O / ii
 if 73 - 73: I11i * o0o00Oo0O - Ii
 if 85 - 85: OoOO00O % IIiI1I + Ii1i111I / I11i . O0O0O + i1IiIIIII
def ooOoOo0 ( ) :
 o0OOOO00O0Oo ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Search' , '' , 10078 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 if 2 - 2: IIiI1I % iI11I1II1I1I * iI11I1II1I1I . I11i / IIiI1I
def iII1i1 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'http://imoviemax.se/?s=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 Oo0o0O00 = ooo00Ooo . lower ( )
 ii1 ( Oo0o0O00 )
def I1i11 ( url ) :
 OO = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIiII )
 for url , o0O0oo0OO0O , OO0 in o0O00oOoOO :
  if o0O0oo0OO0O in OO :
   pass
  else :
   o0OOOO00O0Oo ( o0O0oo0OO0O + ' - ' + OO0 + ' Films' , url , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
   OO . append ( o0O0oo0OO0O )
   if 72 - 72: ii
def OooooOoooO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O , oOIIiIi in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O + ' - Views:' + oOIIiIi , url , 10075 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
  if 91 - 91: Ii1I * I1ii11iIi11i / oOo0O0Ooo . o0o00Oo0O + oO0o + OOooOOo
  if 8 - 8: O0O0O / Ii1I
def ii1 ( url ) :
 i1iI1 = [ ]
 IIiII = Iiii ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIiII )
 for next in next :
  o0OOOO00O0Oo ( 'NEXT PAGE' , next , 10074 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , o0O0oo0OO0O , url in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 10075 , i11ii1ii11i , i11ii1ii11i , '' )
  i1iI1 . append ( o0O0oo0OO0O )
  if 70 - 70: ooOoO0O00 - IIiI1I + I1ii11iIi11i
def II1I1I1Ii ( img , name , url ) :
 img = img
 name = name
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( IIiII )
 for OOOOoO00o0O , url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1I1I1IIi1III = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1I1I1IIi1III
  II11IiiIII = ( OOOOoO00o0O ) . replace ( 'play-' , 'Server ' )
  OOooOoooOoOo ( II11IiiIII , I1I1I1IIi1III , 10076 , img , img , '' )
  if 58 - 58: OoOO00O + I11i - oOo0O0Ooo
def i1i1ii ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( IIiII )
 for i1I1IiiIi1i in o0O00oOoOO :
  if '=m' in i1I1IiiIi1i :
   iII1ii1 ( i1I1IiiIi1i )
  elif 'php' in i1I1IiiIi1i :
   i1i1ii ( url )
  else :
   IIiII = Iiii ( i1I1IiiIi1i )
   o0O00oOoOO = re . compile ( 'content="(.+?)">' ) . findall ( IIiII )
   for I1i1iiiI1 in o0O00oOoOO :
    iII1ii1 ( i1I1IiiIi1i )
    if 24 - 24: O0O0O / Ii + O0O0O
    if 20 - 20: Ii1i111I + OoOO00O / o0o00Oo0O % iI11I1II1I1I
    if 88 - 88: OOooOOo / IIiIiII11i
def OOOOO0O00 ( url ) :
 IIiII = Iiii ( url )
 Iii = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for iIIiIiI1I1 , ooO in Iii :
  print 'there ><><><><><><><><><><><><'
  iIIiIiI1I1 = iIIiIiI1I1
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ooO ) )
  for o0O0oo0OO0O , iiOO0O0Ooo in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + iIIiIiI1I1 + '[/COLOR] - ' + o0O0oo0OO0O + ' - [COLOR' + oO0o0o0ooO0oO + ']' + iiOO0O0Ooo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
 oOoO0 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for iIIiIiI1I1 , Oo0 in oOoO0 :
  print 'there ><><><><><><><><><><><><'
  iIIiIiI1I1 = iIIiIiI1I1
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0 ) )
  for o0O0oo0OO0O , iiOO0O0Ooo in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + iIIiIiI1I1 + '[/COLOR] - ' + o0O0oo0OO0O + ' - [COLOR' + oO0o0o0ooO0oO + ']' + iiOO0O0Ooo + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
   if 83 - 83: Ii % I11i % O0oOO0
   if 11 - 11: IIiIiII11i % oO0o * IIiI1I + O0oOO0 + OoOO00O
   if 24 - 24: I1ii11iIi11i - O0O0O % iI11I1II1I1I . ooOoO0O00 / o0o00Oo0O
def ii1ii111 ( url ) :
 IIiII = Iiii ( url )
 oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
 for oOoO0 in oOoO0 :
  o0O0oo0OO0O = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOoO0 ) )
  for o0O0oo0OO0O in o0O0oo0OO0O :
   o0O0oo0OO0O = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOoO0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I111i1i1111 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOoO0 ) )
  for I111i1i1111 in I111i1i1111 :
   I111i1i1111 = 'http:' + I111i1i1111
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , '' , '' )
  if 49 - 49: oO0o / O0O0O + o0o00Oo0O * I11i
  if 28 - 28: O0oOO0 + Ii / Ii1i111I % OOooOOo % I1ii11iIi11i - o0o00Oo0O
  if 54 - 54: ooOoO0O00 + IIiIiII11i
  if 83 - 83: Ii1I - oOo0O0Ooo + i1IiIIIII
def iIi1Ii1i1iI ( url ) :
 if 16 - 16: i1IiIIIII / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % i1IiIIIII
 ooo0o00 = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIiII )
 for i1I1IiiIi1i , i11ii1ii11i , o0O0oo0OO0O , ooOo0o00 in o0O00oOoOO :
  o0O0oo0OO0O = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0ooOooo000oOO = Iiii ( i1I1IiiIi1i )
  iIIi1i1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0ooOooo000oOO )
  for IIi , oOoO00oo0O in iIIi1i1 :
   IiiiI = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oOoO00oo0O ) )
   for O00OoOO0oo0 in IiiiI :
    if o0O0oo0OO0O in ooo0o00 :
     pass
    else :
     OOooOoooOoOo ( o0O0oo0OO0O , IIi , 8043 , i11ii1ii11i , i11ii1ii11i , O00OoOO0oo0 )
     oO00OOoO00 ( 'movies' , 'INFO' )
     ooo0o00 . append ( o0O0oo0OO0O )
     if 96 - 96: OOooOOo . I11i - O0oOO0
     if 99 - 99: O00Oo000ooO0 . I1ii11iIi11i - OoOO00O % OoOO00O * o0o00Oo0O . IIiIiII11i
def iIIII1iIIii ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOOO00o000o , O00OoOO0oo0 , iIi11i1 , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 10065 , oOOO00o000o , iIi11i1 , O00OoOO0oo0 )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 71 - 71: O0oOO0
def Ooo0o00o0o ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'https://www.youtube.com/results?search_query=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 Oo0o0O00 = ooo00Ooo . lower ( )
 IIiII = Iiii ( Oo0o0O00 )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for IiIIIIIi in next :
  IiIIIIIi = 'https://www.youtube.com' + IiIIIIIi
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , IiIIIIIi , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 , oOoO00oo0O in o0O00oOoOO :
  OO0o . append ( o0O0oo0OO0O )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111i1i1111
  IiIIIIIi = 'http://www.youtube.com' + IiIIIIIi
  OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , oOoO00oo0O )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 in o0O00oOoOO :
   print 'im doing it'
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
   IiIIIIIi = 'http://www.youtube.com' + IiIIIIIi
   if '&' in IiIIIIIi :
    print ' i got here'
    IIiII = Iiii ( IiIIIIIi )
    oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for oOoO0 in oOoO0 :
     o0O0oo0OO0O = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOoO0 ) )
     for o0O0oo0OO0O in o0O0oo0OO0O :
      o0O0oo0OO0O = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     IiIIIIIi = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOoO0 ) )
     for IiIIIIIi in IiIIIIIi :
      IiIIIIIi = 'https://www.youtube.com/w' + IiIIIIIi
     I111i1i1111 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOoO0 ) )
     for I111i1i1111 in I111i1i1111 :
      I111i1i1111 = 'http:' + I111i1i1111
     OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , i1iIIi1 , '' )
   elif o0O0oo0OO0O in OO0o :
    pass
   elif 'user' in IiIIIIIi or 'elete' in o0O0oo0OO0O :
    pass
   elif 'hannel' in IiIIIIIi :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + IiIIIIIi
    IIiII = Iiii ( IiIIIIIi )
    O0OoO0ooOO0o = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in O0OoO0ooOO0o :
     if 'outube' in IiIIIIIi or 'list' in IiIIIIIi :
      pass
     elif 'atch' in IiIIIIIi :
      IiIIIIIi = ( IiIIIIIi ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i11ii1ii11i , 'http:' + i11ii1ii11i , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , '' )
    if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
def oO0o00ooO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for url in next :
  url = 'https://www.youtube.com' + url
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , url , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 , oOoO00oo0O in o0O00oOoOO :
  OO0o . append ( o0O0oo0OO0O )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111i1i1111
  url = 'http://www.youtube.com' + url
  OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , oOoO00oo0O )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 in o0O00oOoOO :
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   I111i1i1111 = 'http:' + ( i11ii1ii11i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIiII = Iiii ( url )
    oOoO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for oOoO0 in oOoO0 :
     o0O0oo0OO0O = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oOoO0 ) )
     for o0O0oo0OO0O in o0O0oo0OO0O :
      o0O0oo0OO0O = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oOoO0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I111i1i1111 = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oOoO0 ) )
     for I111i1i1111 in I111i1i1111 :
      I111i1i1111 = 'http:' + I111i1i1111
     OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , i1iIIi1 , '' )
   elif o0O0oo0OO0O in OO0o :
    pass
   elif 'user' in url or 'elete' in o0O0oo0OO0O :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIiII = Iiii ( url )
    O0OoO0ooOO0o = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for i11ii1ii11i , url , o0O0oo0OO0O in O0OoO0ooOO0o :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + i11ii1ii11i , 'http:' + i11ii1ii11i , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + IiIi1iIIi1 + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 , I111i1i1111 , '' )
    if 24 - 24: O00Oo000ooO0 * Ii * i1IiIIIII
    if 85 - 85: I11i . OOooOOo / O0oOO0 . o0o00Oo0O % oO00Oo0o000
def o00O0 ( ) :
 if oO == 'insert_password' :
  oOOoo00O0O . ok ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + oO0o0o0ooO0oO + ']http://GenieTv.co.uk[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  OO0ooo0oOO = open ( o0 )
  o0O00oOoOO = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OO0ooo0oOO ) )
  for oo000ii , OoO in o0O00oOoOO :
   if oo000ii == 'needs replacing' or OoO == 'needs replacing' :
    Iiiiii111i1ii ( )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv PRIVATE LIST[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'PrivateList.png' , i1iIIi1 , '' )
  if 25 - 25: i1IiIIIII - O0oOO0 / Ii
def iiI1ii11i1 ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + Ooo + ")" )
 Iiiiii111i1ii ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 38 - 38: Ii1I - IIiI1I / o0o00Oo0O . oO00Oo0o000
def i1iiIiI1Ii1i ( ) :
 try :
  i1iIiiiiii1II = gui . TVGuide ( )
  i1iIiiiiii1II . doModal ( )
  del i1iIiiiiii1II
  if 81 - 81: OoOO00O * I11i + oO00Oo0o000 + I1ii11iIi11i - ii
 except :
  import sys
  import traceback as tb
  ( i1i1I111iIi1 , oo00O00oO000o , traceback ) = sys . exc_info ( )
  tb . print_exception ( i1i1I111iIi1 , oo00O00oO000o , traceback )
  if 71 - 71: Ii1I - O0oOO0 / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def ooo000ooO0000 ( ) :
 o0OOOO00O0Oo ( 'Full Backup' , '' , 10061 , OOoOO0oo0ooO + 'FullBackUp.png' , i1iIIi1 , 'Back Up Your Full System' )
 if os . path . exists ( I11iii1Ii ) :
  o0OOOO00O0Oo ( 'Backup Genie Favourites' , IiIIIIIi , 10062 , OOoOO0oo0ooO + 'BackupGenieFavourites.png' , i1iIIi1 , 'Back Up Your favourites' )
 if os . path . exists ( iiiiiIIii ) :
  o0OOOO00O0Oo ( 'Backup Ivue Config' , iiiiiIIii , 10062 , OOoOO0oo0ooO + 'BackUpIvueConfig.png' , i1iIIi1 , 'Back Up Your master.db' )
 if os . path . exists ( O000OO0 ) :
  o0OOOO00O0Oo ( 'Backup Kodi Favourites' , O000OO0 , 10062 , OOoOO0oo0ooO + 'BackKodiFavourites.png' , i1iIIi1 , 'Back Up Your favourites.xml' )
  if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
  if 16 - 16: O0oOO0 % ii - i1IiIIIII * OoOO00O * Ii1I / ii
  if 31 - 31: Ii1i111I . oO00Oo0o000 * O0oOO0 + Ii * O0O0O
zip = o0oO0 . getSetting ( 'zip' )
OO0ooo0o0O0Oooooo = xbmc . translatePath ( os . path . join ( zip ) )
def i11IIIiI1I ( ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 17 - 17: iI11I1II1I1I . ii / Ii1i111I % IIiIiII11i % ooOoO0O00 / Ii
  if 58 - 58: I1ii11iIi11i . IIiIiII11i + O0O0O - Ii / IIiIiII11i / o0o00Oo0O
  if 85 - 85: OOooOOo + i1IiIIIII
def I1II ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I11iii1Ii
  elif 'Ivue' in name :
   url = iiiiiIIii
  elif 'Kodi' in name :
   url = O000OO0
  i11IIIiI1I ( )
  iii1 = open ( url ) . read ( )
  oO0OO0 = os . path . join ( OO0ooo0o0O0Oooooo , description . split ( 'Your ' ) [ 1 ] )
  OOO = open ( oO0OO0 , mode = 'w' )
  OOO . write ( iii1 )
  OOO . close ( )
 else :
  if 'guisettings.xml' in description :
   o0O0Oo00 = open ( os . path . join ( OO0ooo0o0O0Oooooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0Oo0o000oO = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   o0O00oOoOO = re . compile ( O0Oo0o000oO ) . findall ( o0O0Oo00 )
   for type , oO0o00oOOooO0 , OOOoO000 in o0O00oOoOO :
    OOOoO000 = OOOoO000 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oO0o00oOOooO0 , OOOoO000 ) )
  else :
   oO0OO0 = os . path . join ( url )
   iii1 = open ( os . path . join ( OO0ooo0o0O0Oooooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOO = open ( oO0OO0 , mode = 'w' )
   OOO . write ( iii1 )
   OOO . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 57 - 57: IIiIiII11i
 if 54 - 54: I1ii11iIi11i + O0O0O + Ii
 if 28 - 28: O0O0O
 if 70 - 70: O00Oo000ooO0
def i11i1iiI1i ( ) :
 oO0oOOoo00000 = 1
 i11IIIiI1I ( )
 oOo00 = xbmc . translatePath ( os . path . join ( OO0ooo0o0O0Oooooo , 'Build Backup' , 'Full Backup' , '' ) )
 i1iI11i1IIi = xbmc . translatePath ( os . path . join ( OO0ooo0o0O0Oooooo , 'Build Backup' , 'my_full_backup.zip' ) )
 ii1IIi111 = xbmc . translatePath ( os . path . join ( OO0ooo0o0O0Oooooo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oOo00 ) :
  os . makedirs ( oOo00 )
 iI1 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iI1 ) : return False , 0
 OoOo00o0OO = iI1
 ii1IIIIiI11 = xbmc . translatePath ( os . path . join ( oOo00 , OoOo00o0OO + '.zip' ) )
 iI1IIIii = [ 'plugin.video.GenieTv' ]
 I1i11ii11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 OO00O0oOO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 Ii1iI111 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0oooo00o0Oo = "Creating full backup of existing build"
 I1iii = "Creating Community Build"
 oO0o0O0Ooo0o = "Archiving..."
 i1Ii11II = ""
 IioO0oOOO0Ooo = "Please Wait"
 i1i1I ( i1iiIII111ii , ii1IIIIiI11 , I1iii , oO0o0O0Ooo0o , i1Ii11II , IioO0oOOO0Ooo , OO00O0oOO , Ii1iI111 )
 time . sleep ( 1 )
 IiIIi1 = xbmc . translatePath ( os . path . join ( oOo00 , OoOo00o0OO + '_guisettings.zip' ) )
 iII11I1Ii1 = zipfile . ZipFile ( IiIIi1 , mode = 'w' )
 try :
  iII11I1Ii1 . write ( xbmc . translatePath ( os . path . join ( i1iiIII111ii , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iII11I1Ii1 . close ( )
 if oO0oOOoo00000 == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i1iI11i1IIi , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + ii1IIIIiI11 + '[/COLOR]' )
  if 92 - 92: Ii1i111I / Ii1i111I . Ii1I
def i1i1I ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 ii1iIi1II = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IIIIi1I = len ( sourcefile )
 IiIi1i1ii = [ ]
 iiIi = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for oOIi111 , oO0 , i1iI in os . walk ( sourcefile ) :
  for file in i1iI :
   iiIi . append ( file )
 iioo0o0OoOOO = len ( iiIi )
 for oOIi111 , oO0 , i1iI in os . walk ( sourcefile ) :
  oO0 [ : ] = [ ooO0oO00O0o for ooO0oO00O0o in oO0 if ooO0oO00O0o not in exclude_dirs ]
  i1iI [ : ] = [ OOO for OOO in i1iI if OOO not in exclude_files ]
  for file in i1iI :
   IiIi1i1ii . append ( file )
   ooOO00oOOo000 = len ( IiIi1i1ii ) / float ( iioo0o0OoOOO ) * 100
   Oo0oO0ooo . update ( int ( ooOO00oOOo000 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IIii11II11II1 = os . path . join ( oOIi111 , file )
   if not 'temp' in oO0 :
    if not 'plugin.program.originwizard' in oO0 :
     import time
     II1IOoOo000oOo0oo = '01/01/1980'
     oO0O = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IIii11II11II1 ) ) )
     if oO0O > II1IOoOo000oOo0oo :
      ii1iIi1II . write ( IIii11II11II1 , IIii11II11II1 [ IIIIi1I : ] )
 ii1iIi1II . close ( )
 Oo0oO0ooo . close ( )
 if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
 if 56 - 56: o0o00Oo0O
def OOo00 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 if 37 - 37: ooOoO0O00
 if 46 - 46: OOooOOo - Ii1i111I - OoOO00O . ooOoO0O00
def IiI1iii11iIi1 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( OOO00O ) , 9001 , OOoOO0oo0ooO + 'MOVIESv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( OOO00O ) , 9002 , OOoOO0oo0ooO + 'TVSHOWSv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON' , i1iIIi1 , '' )
 if 40 - 40: Ii1i111I % oO0o . oO00Oo0o000
 if 84 - 84: OOooOOo % O0oOO0 - OOooOOo . I11i
 if 5 - 5: OOooOOo * oO00Oo0o000 - Ii1I / iI11I1II1I1I % O0O0O + O00Oo000ooO0
 if 51 - 51: oO00Oo0o000 * IIiIiII11i % O0oOO0
def oO0o000OoOoO0 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9rb2RpbXVzaWM=' ) ) , 1006 , OOoOO0oo0ooO + 'Quicksilver.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC CHANNELS[/COLOR]' , str ( OOO00O ) , 30031 , OOoOO0oo0ooO + 'MusicChannels.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , OOoOO0oo0ooO + 'UKRadio.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WORLD RADIO[/COLOR]' , str ( OOO00O ) , 1013 , OOoOO0oo0ooO + 'WorldRadio.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , OOoOO0oo0ooO + 'Concerts.png' , i1iIIi1 , '' )
  if 99 - 99: I11i * oOo0O0Ooo % I1ii11iIi11i . OOooOOo
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , OOoOO0oo0ooO + 'MusicVideos.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( OOO00O ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOoOO0oo0ooO + 'Music.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC SEARCH[/COLOR]' , str ( OOO00O ) , 1111 , OOoOO0oo0ooO + 'MusicSearch.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , i1iIIi1 , '' )
 if 58 - 58: Ii1i111I + IIiIiII11i * IIiI1I * Ii - iI11I1II1I1I
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 68 - 68: ii % IIiIiII11i
def Ii1i1i1111 ( ) :
 I1ii11iI ( )
 if 57 - 57: OoOO00O % IIiIiII11i
 OOooOoooOoOo ( 'DELETE CACHE' , 'url' , 14 , OOoOO0oo0ooO + 'DeleteCache.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'DELETE PACKAGES' , 'url' , 6 , OOoOO0oo0ooO + 'DeletePackages.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FORCE REFRESH' , 'url' , 10 , OOoOO0oo0ooO + 'ForceRefresh.png' , i1iIIi1 , 'Force Refresh All Repos' )
 if 67 - 67: O0oOO0 + oOo0O0Ooo * Ii - O0O0O / O00Oo000ooO0 % IIiI1I
 OOooOoooOoOo ( 'CHECK MY IP' , 'url' , 12 , OOoOO0oo0ooO + 'CheckMyIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOoOO0oo0ooO + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , i1iIIi1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ADVANCED SETTINGS XML[/COLOR]' , str ( OOO00O ) , 4 , OOoOO0oo0ooO + 'AdvancedSettingXML.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']URL FIXES[/COLOR]' , str ( OOO00O ) , 20 , OOoOO0oo0ooO + 'URLFixes.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 92 - 92: OoOO00O - O0O0O - O0oOO0 % ii / i1IiIIIII
 if 19 - 19: I1ii11iIi11i - oO0o
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
 if 56 - 56: Ii1I
 if 26 - 26: ii % ii
def iIIIII1iiiiII ( ) :
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
 if 54 - 54: ooOoO0O00
def ii1I11 ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Local Zip[/COLOR]' , I11 , 48 , OOoOO0oo0ooO + 'MyLocalZIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Online Zip[/COLOR]' , i11 , 43 , OOoOO0oo0ooO + 'MyOnlineZip.png' , i1iIIi1 , '' )
 if 99 - 99: i1IiIIIII
def II11i11II ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( OOO00O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOoOO0oo0ooO + 'FTV4.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( OOO00O ) + '/wizard/customftv/settings.xml' , 17 , OOoOO0oo0ooO + 'FTV3.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOoOO0oo0ooO + 'FTV1.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'RESET FTV DATABASE' , 'url' , 18 , OOoOO0oo0ooO + 'FTV2.png' , i1iIIi1 , '' )
 if 29 - 29: I1ii11iIi11i % oO0o % O00Oo000ooO0 . I11i / ii * O0oOO0
 if 54 - 54: o0o00Oo0O
 if 68 - 68: oO0o * I11i . O0oOO0 % O0O0O % oO00Oo0o000
def oooo0OO ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SKINS[/COLOR]' , str ( OOO00O ) , 33 , OOoOO0oo0ooO + 'Skins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ARTWORK PACKS[/COLOR]' , str ( OOO00O ) , 34 , OOoOO0oo0ooO + 'ArtworkPacks.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIII111ii , 35 , OOoOO0oo0ooO + 'CreateUniversalPath.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 23 - 23: O0O0O + oO0o
def III1I1i1 ( ) :
 O00oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 o0O00oOoOO = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( O00oO )
 for i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , i11ii1ii11i , i11ii1ii11i , '' )
 oO00OOoO00 ( 'tvshows' , 'INFO' )
 if 11 - 11: o0o00Oo0O / oO0o % i1IiIIIII + I11i + iI11I1II1I1I
def I1i1111I ( url ) :
 O00oO = Iiii ( OooOO0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 91 - 91: O0O0O + ii - ooOoO0O00
def o000 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GOTHAM SKINS[/COLOR]' , str ( OOO00O ) , 36 , OOoOO0oo0ooO + 'GothamSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HELIX SKINS[/COLOR]' , str ( OOO00O ) , 37 , OOoOO0oo0ooO + 'HelixSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ISENGAARD SKINS[/COLOR]' , i1iiIII111ii , 38 , OOoOO0oo0ooO + 'IsengaardSkins.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 94 - 94: I11i + o0o00Oo0O / Ii1i111I . oOo0O0Ooo + i1IiIIIII . iI11I1II1I1I
def OOOoO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 74 - 74: iI11I1II1I1I * O00Oo000ooO0 % OOooOOo
def iiI11iIi ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oooOO0OO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 78 - 78: OoOO00O / IIiIiII11i % OOooOOo
def oO00OoOO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + I11IIiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 5 - 5: I1ii11iIi11i * OOooOOo
def ii1I11iIiIII1 ( url ) :
 O00oO = Iiii ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 52 - 52: I11i * O00Oo000ooO0 + OOooOOo
def IiiiIiiI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 40 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 48 - 48: IIiI1I . Ii
def IIioo0OO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + IiiI11i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 80 - 80: i1IiIIIII / Ii1i111I / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def iIIiiIIi1IiI ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK (Android only)[/COLOR]' , str ( OOO00O ) , 2 , OOoOO0oo0ooO + 'APKAndroidOnly.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK Search[/COLOR]' , str ( OOO00O ) , 30038 , OOoOO0oo0ooO + 'APKSearch.png' , i1iIIi1 , '' )
 if 14 - 14: O00Oo000ooO0 % O0O0O % I1ii11iIi11i - Ii
def o0OO000ooOo ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5hcGtjcmFmdC5jb20v' ) )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Android Apps</a>' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'href="(.+?)">Android Games</a>' ) . findall ( OoO000O0Oo )
 oOo00OooO0oO = re . compile ( 'href="(.+?)">Wallpapers</a>' ) . findall ( OoO000O0Oo )
 I1IIi = re . compile ( 'href="(.+?)">Widgets</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi in o0O00oOoOO :
  iiI11ii1I1 ( 'Android Apps' , IiIIIIIi , 30035 , OOoOO0oo0ooO + 'apps.png' )
 for IiIIIIIi in iIIi1i1 :
  iiI11ii1I1 ( 'Android Games' , IiIIIIIi , 30035 , OOoOO0oo0ooO + 'GAMES.png' )
 for IiIIIIIi in oOo00OooO0oO :
  iiI11ii1I1 ( 'Wallpapers' , IiIIIIIi , 30036 , OOoOO0oo0ooO + 'wallpapers.png' )
 for IiIIIIIi in I1IIi :
  iiI11ii1I1 ( 'Widgets' , IiIIIIIi , 30036 , OOoOO0oo0ooO + 'widgets.png' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def O0OOOo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if 'cat' in url :
   iiI11ii1I1 ( o0O0oo0OO0O , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def i11I1I1iiI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '" target="_blank" href="([^"]*)"><img title="([^"]*)" src="([^"]*)"></a></dt>' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'class="pagination_next"><a href="(.+?)">»</a></li>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , 'https://apkpure.com' + url , 30037 , i11ii1ii11i )
 for url in iIIi1i1 :
  iiI11ii1I1 ( 'NEXT PAGE' , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def I1i1iii1Ii ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">Download APK<span' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  iI ( url )
def iI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O0O00OOo ( url )
def OoOOo ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooo00Ooo = 'https://apkpure.com/search?q=' + ( O0oOOoooOO0O ) . replace ( ' ' , '+' ) + '&region='
 Oo0o0O00 = ooo00Ooo . lower ( )
 i11I1I1iiI ( Oo0o0O00 )
 if 17 - 17: ooOoO0O00
def O0O00OOo ( url ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( i1IIII1iii11I , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , o0O0oo0OO0O + '.apk' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 95 - 95: O00Oo000ooO0 * Ii1I % O0oOO0 % OoOO00O - OoOO00O
def oOoooO0 ( url ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , o0O0oo0OO0O + '.mp4' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 68 - 68: O0oOO0 / I11i
 if 1 - 1: o0o00Oo0O / IIiI1I % oO00Oo0o000 . I1ii11iIi11i + O00Oo000ooO0
def I1Ii11iiiI ( name , url , description ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , name )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 i1II1IiIII111 = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1II1IiIII111
 print '======================================='
 extract . all ( oo0OoOooo , i1II1IiIII111 , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 50 - 50: IIiIiII11i * Ii1I / OoOO00O . I11i + I1ii11iIi11i - i1IiIIIII
 if 18 - 18: OOooOOo % Ii % Ii1I / O0O0O / I11i / ooOoO0O00
def IIi1I1 ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 5 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 28 - 28: Ii1I . ooOoO0O00
 if 10 - 10: oO0o / I1ii11iIi11i
def I1i ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 30015 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 50 - 50: I11i * OoOO00O % Ii1I / I1ii11iIi11i - o0o00Oo0O % IIiI1I
def IIII1ii ( url , iconimage , fanart ) :
 O00oO = Iiii ( url )
 I1I1I1IIi1III = url
 i11ii1ii11i = iconimage
 fanart = fanart
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for i1I1IiiIi1i , o0O0oo0OO0O in o0O00oOoOO :
  if '.mp4' in o0O0oo0OO0O :
   OOooOoooOoOo ( 'Watch VIDEO' , url + '/' + i1I1IiiIi1i , 222 , i11ii1ii11i , fanart , '' )
  if 'description' in o0O0oo0OO0O :
   OOooOoooOoOo ( 'Read Description' , url + '/' + i1I1IiiIi1i , 30017 , i11ii1ii11i , fanart , '' )
  if 'images' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( 'View Images' , url + '/' + i1I1IiiIi1i , 30018 , i11ii1ii11i , fanart , '' )
  if 'url' in o0O0oo0OO0O :
   OOooOoooOoOo ( 'Install Build On Android' , url + '/' + i1I1IiiIi1i , 30016 , i11ii1ii11i , fanart , '' )
  if 'url' in o0O0oo0OO0O :
   OOooOoooOoOo ( 'Install Build On Pc' , url + '/' + i1I1IiiIi1i , 30019 , i11ii1ii11i , fanart , '' )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 13 - 13: ii * O0O0O - OoOO00O / i1IiIIIII + Ii1i111I + O00Oo000ooO0
def iii1III1i ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  iiiIi ( url )
  if 45 - 45: Ii1I + oO0o * Ii / i1IiIIIII % Ii1i111I * o0o00Oo0O
def i1o0oooO ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  ooOo ( url )
  if 84 - 84: i1IiIIIII
def o0OoO00 ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'desc="(.+?)"' ) . findall ( O00oO )
 for IIIIIiII1 in o0O00oOoOO :
  o0iI11I1II ( 'Description:' , IIIIIiII1 )
  if 45 - 45: oOo0O0Ooo / IIiI1I . IIiI1I
def i1oO ( url ) :
 O00oO = Iiii ( url )
 url = url
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for i1I1IiiIi1i , o0O0oo0OO0O in o0O00oOoOO :
  if 'png' in o0O0oo0OO0O :
   OOooOoooOoOo ( 'image' , '' , '' , url + '/' + i1I1IiiIi1i , url + '/' + i1I1IiiIi1i , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 30 - 30: I1ii11iIi11i . oO0o
def o0Oii1111i ( name , url , description ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , name + '.zip' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 O0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print O0ooOO
 print '======================================='
 extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOOoo00 ( )
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
 if 72 - 72: ii / oOo0O0Ooo + OoOO00O / OOooOOo * OoOO00O
def ooOo ( url ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 O0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print O0ooOO
 print '======================================='
 extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
 Ii1iIi111i1i1 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IIOO0ooOo0OoOo0 ( )
 if 87 - 87: O0O0O . oOo0O0Ooo
def iiiIi ( url ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 O0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print O0ooOO
 print '======================================='
 extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
 Ii1iIi111i1i1 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "DO NOT EXIT CLEANLY VIA SHUTDOWN, Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 17 - 17: OoOO00O . Ii
 if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . oO00Oo0o000 - O0oOO0
def o00oo0000 ( name , url , description ) :
 O0ooOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 oo0OoOooo = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print O0ooOO
 print '======================================='
 extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
 if 90 - 90: IIiIiII11i + ii % ii
def IIOO0ooOo0OoOo0 ( ) :
 Ooo0oOooo0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if Ooo0oOooo0 == 0 :
  return
 elif Ooo0oOooo0 == 1 :
  pass
 I11Ii = iIiII ( )
 print "Platform: " + str ( I11Ii )
 if I11Ii == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I11Ii == 'linux' :
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
 elif I11Ii == 'android' :
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
 elif I11Ii == 'windows' :
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
  if 19 - 19: O00Oo000ooO0
def iIiII ( ) :
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
  if 78 - 78: i1IiIIIII % I11i
  if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
  if 7 - 7: O00Oo000ooO0 . OOooOOo / Ii1I . i1IiIIIII * Ii1i111I - IIiIiII11i
def I1 ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ii1iI1II11ii , oO0 , i1iI in os . walk ( url ) :
  for file in i1iI :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    o0O0Oo00 = open ( ( os . path . join ( ii1iI1II11ii , file ) ) ) . read ( )
    i1i1IiIiIi1Ii = o0O0Oo00 . replace ( i1iiIII111ii , 'special://home/' )
    OOO = open ( ( os . path . join ( ii1iI1II11ii , file ) ) , mode = 'w' )
    OOO . write ( str ( i1i1IiIiIi1Ii ) )
    OOO . close ( )
 IIOO0ooOo0OoOo0 ( )
 if 64 - 64: i1IiIIIII + ii * ii
def i1I ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.listenlive.eu/' + IiIIIIIi , 10111113 , OOoOO0oo0ooO + 'radio.png' )
def iiI1I1IIi11i1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , OOoOO0oo0ooO + 'radio.png' )
  if 45 - 45: O0oOO0 % I11i - O0oOO0
def i1i1 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.toonjet.com/' + IiIIIIIi , 8051 , OOoOO0oo0ooO + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0ooOoO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i in o0O00oOoOO :
  if 'ol.gif' in i11ii1ii11i :
   pass
  elif 'link_block_' in i11ii1ii11i :
   pass
  elif '.png' in i11ii1ii11i :
   pass
  else :
   iiI11ii1I1 ( ( i11ii1ii11i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOoOO0oo0ooO + 'vod.png' )
 for url in iIIi1i1 :
  iiI11ii1I1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOoOO0oo0ooO + 'Next.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0000o00O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOoOO0oo0ooO + 'classictoons.png' )
  if 91 - 91: Ii1i111I / o0o00Oo0O - OoOO00O . oOo0O0Ooo
  if 82 - 82: O00Oo000ooO0 * i1IiIIIII / O0O0O
def IiiIiI ( ) :
 iIIIIiiIii ( 'Audio Books' , '' , 30011 , OOoOO0oo0ooO + 'AudioBooks.png' , OOoOO0oo0ooO + 'AudioBooks.png' , '' )
 iIIIIiiIii ( 'Kids Audio Books' , '' , 30006 , OOoOO0oo0ooO + 'KidsAudioBooks.png' , OOoOO0oo0ooO + 'KidsAudioBooks.png' , '' )
 if 58 - 58: I1ii11iIi11i
def IiiIIIiI1ii ( ) :
 iIIIIiiIii ( 'All' , '' , 30001 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 iIIIIiiIii ( 'Popular' , '' , 30012 , OOoOO0oo0ooO + 'POPULARv.png' , OOoOO0oo0ooO + 'POPULARv.png' , '' )
 iIIIIiiIii ( 'Search' , '' , 30013 , OOoOO0oo0ooO + 'Search.png' , OOoOO0oo0ooO + 'Search.png' , '' )
 if 78 - 78: o0o00Oo0O * i1IiIIIII
def iIii1Ooo0oO0 ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for o0O0oo0OO0O , IiIIIIIi , o0Oo0oOooOoOo in o0O00oOoOO :
  if 'Parent' in o0O0oo0OO0O :
   pass
  elif '2' in o0Oo0oOooOoOo :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: i1IiIIIII . Ii1I . Ii - IIiIiII11i / OoOO00O
def ooOo0O0o0 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for o0O0oo0OO0O , IiIIIIIi , o0Oo0oOooOoOo in o0O00oOoOO :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   if '1' in o0Oo0oOooOoOo :
    iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '2' in o0Oo0oOooOoOo :
    iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '3' in o0Oo0oOooOoOo :
    iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 65 - 65: O0oOO0 + o0o00Oo0O
    if 32 - 32: ii - OOooOOo - Ii * I11i / I1ii11iIi11i + ii
def ii1I1I111 ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for o0O0oo0OO0O , IiIIIIIi , o0Oo0oOooOoOo in o0O00oOoOO :
  if '1' in o0Oo0oOooOoOo :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 3010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '2' in o0Oo0oOooOoOo :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '3' in o0Oo0oOooOoOo :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , IiIIIIIi , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 3 - 3: ii / i1IiIIIII * I1ii11iIi11i . O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: ooOoO0O00 / O0oOO0 . oOo0O0Ooo * I11i
def i11i1Ii1 ( url ) :
 i1I1IiiIi1i = url
 IIiII = Iiii ( url )
 iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
 for url , o0O0oo0OO0O in iIIi1i1 :
  if 'mp3' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'wma' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1I1IiiIi1i + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '/' in o0O0oo0OO0O :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 98 - 98: oO00Oo0o000
   if 92 - 92: oO00Oo0o000 - iI11I1II1I1I
   if 32 - 32: OoOO00O % oO0o * oO0o + O00Oo000ooO0 * IIiIiII11i * OoOO00O
def iIiIii1I1II ( url ) :
 IIiII = Iiii ( url )
 i1I1IiiIi1i = url
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if 'Parent' in o0O0oo0OO0O :
   pass
  elif '.db' in o0O0oo0OO0O :
   pass
  elif '.jpg' in o0O0oo0OO0O :
   pass
  elif '.html' in o0O0oo0OO0O :
   pass
  elif '.doc' in o0O0oo0OO0O :
   pass
  elif 'mp3' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in o0O0oo0OO0O :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1I1IiiIi1i + url , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 61 - 61: O00Oo000ooO0 + iI11I1II1I1I + Ii / Ii % IIiIiII11i
   if 42 - 42: OoOO00O * oO00Oo0o000 . O00Oo000ooO0 * oOo0O0Ooo + OOooOOo
def i1i1II11II1 ( ) :
 iIIIIiiIii ( 'A-Z' , '' , 30007 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 iIIIIiiIii ( 'All' , '' , 30003 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 iIIIIiiIii ( 'Search' , '' , 30014 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 if 5 - 5: I1ii11iIi11i - Ii1I % O0O0O - IIiIiII11i . oOo0O0Ooo + IIiI1I
def iiIi1I1i1 ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIiII )
 for IiIIIIIi , i11ii1ii11i in o0O00oOoOO :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + IiIIIIIi + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in i11ii1ii11i :
   pass
  else :
   iIIIIiiIii ( i11ii1ii11i , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( IiIIIIIi ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + i11ii1ii11i + '.gif' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: oO0o . ii + Ii1i111I - OOooOOo / IIiIiII11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: Ii1i111I % iI11I1II1I1I . I1ii11iIi11i + I1ii11iIi11i - I11i % oO00Oo0o000
 if 38 - 38: oO00Oo0o000 % i1IiIIIII - ii
def oOo0OOoooO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if '</a>' in o0O0oo0OO0O :
   pass
  elif '(' in o0O0oo0OO0O :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 26 - 26: I11i * O00Oo000ooO0 . ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
def OooOo000o0o ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   if '</a>' in o0O0oo0OO0O :
    pass
   elif '(' in o0O0oo0OO0O :
    iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   else :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 42 - 42: O0O0O % i1IiIIIII
    if 60 - 60: OOooOOo / oO00Oo0o000 - IIiIiII11i . I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if '</a>' in o0O0oo0OO0O :
   pass
  elif '(' in o0O0oo0OO0O :
   iIIIIiiIii ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + IiIIIIIi , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 53 - 53: iI11I1II1I1I - O0O0O % OOooOOo * oO00Oo0o000 % O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
 if 64 - 64: O0O0O / O0oOO0 % Ii
def I11oOOooo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i1I1IiiIi1i )
  if 80 - 80: oOo0O0Ooo - Ii
def oOoooO000O ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( IIiII )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  if '<p align' in o0O0oo0OO0O :
   pass
  elif '&nbsp;' in o0O0oo0OO0O :
   pass
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: I11i * OoOO00O + Ii1i111I + IIiI1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I11i / i1IiIIIII / O00Oo000ooO0 % O0oOO0 + IIiIiII11i
 if 4 - 4: IIiI1I - I1ii11iIi11i - O00Oo000ooO0 - Ii1i111I % Ii / oO0o
def i1iii11 ( ) :
 IIiII = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o0O00oOoOO = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'ongoing' in IiIIIIIi :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , OOoOO0oo0ooO + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in IiIIIIIi :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , OOoOO0oo0ooO + 'CartoonShows.png' , '' , '' )
  if 'disney' in IiIIIIIi :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , OOoOO0oo0ooO + 'Disney.png' , '' , '' )
  if 'genre' in IiIIIIIi :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , OOoOO0oo0ooO + 'Genre.png' , '' , '' )
  if 'years' in IiIIIIIi :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 21005 , OOoOO0oo0ooO + 'Years.png' , '' , '' )
def oOo0O0o0000o0O0 ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 o0OoOoOOoOo0o = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIiII )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , i11ii1ii11i , i11ii1ii11i , o0O0oo0OO0O )
 for url , o0O0oo0OO0O in o0OoOoOOoOo0o :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in next :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
def iIiii ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 IiIii1ii = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 IIiI1i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIiII )
 iII1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in IIiI1i :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , 'http:' + url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url , o0O0oo0OO0O in IiIii1ii :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 else :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
def O000O ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
  if 98 - 98: iI11I1II1I1I + oO00Oo0o000 % OOooOOo + Ii1i111I % OOooOOo
def iI1I1I11IiII ( ) :
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 47 - 47: O0O0O % iI11I1II1I1I
def IiI1IIIII1I ( ) :
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 35 - 35: OoOO00O - OoOO00O + ooOoO0O00 - o0o00Oo0O - oO00Oo0o000
def oOO0o0oo0 ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if '?c=' in url :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 78 - 78: i1IiIIIII + IIiI1I . O00Oo000ooO0
def Oo ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi1iI , o0O0oo0OO0O in o0O00oOoOO :
  if 'Genre' in url :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 92 - 92: oO0o * O0oOO0
def i1iIIi1o0o0OoOOOOOo ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi1iI , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi1iI )
  if 39 - 39: ii * i1IiIIIII * o0o00Oo0O . Ii1i111I . oO0o + O0oOO0
def II1IIi ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi1iI , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi1iI )
  if 51 - 51: I1ii11iIi11i + O0O0O / IIiI1I - ooOoO0O00
  if 51 - 51: I1ii11iIi11i - Ii1I * Ii1i111I
  if 12 - 12: iI11I1II1I1I % O0oOO0 % O0oOO0
  if 78 - 78: O00Oo000ooO0 . OOooOOo . Ii1i111I
  if 97 - 97: O0O0O
def oOoO0O00oo ( ) :
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / IIiI1I * O0O0O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Cartoons[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 if 29 - 29: I11i
def oo0 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 2 - 2: ii
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIiII )
 if 60 - 60: oO0o
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   if 'Dad!' in o0O0oo0OO0O :
    pass
   elif 'Family Guy' in o0O0oo0OO0O :
    pass
   elif '2 Stupid' in o0O0oo0OO0O :
    pass
   elif 'The Zelfs' in o0O0oo0OO0O :
    pass
   elif 'A Clone' in o0O0oo0OO0O :
    pass
   elif 'A.T.O.M' in o0O0oo0OO0O :
    pass
   elif 'Almost Naked' in o0O0oo0OO0O :
    pass
   elif 'Angry Kid' in o0O0oo0OO0O :
    pass
   elif 'Annoying Orange' in o0O0oo0OO0O :
    pass
   elif 'Aqua Teen' in o0O0oo0OO0O :
    pass
   elif 'Assy Mcgee' in o0O0oo0OO0O :
    pass
   elif 'Astroblast' in o0O0oo0OO0O :
    pass
   elif 'Atomic Betty' in o0O0oo0OO0O :
    pass
   elif 'Axe Cop' in o0O0oo0OO0O :
    pass
   elif 'Baby Playpen' in o0O0oo0OO0O :
    pass
   elif 'Beavis and Butt' in o0O0oo0OO0O :
    pass
   elif 'Celebrity Deathmatch' in o0O0oo0OO0O :
    pass
   elif 'Clerks The' in o0O0oo0OO0O :
    pass
   elif 'Crapston Villas' in o0O0oo0OO0O :
    pass
   elif 'Duckman:' in o0O0oo0OO0O :
    pass
   elif 'Stripperella' in o0O0oo0OO0O :
    pass
   elif 'Vixen' in o0O0oo0OO0O :
    pass
   else :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
    if 81 - 81: OOooOOo % OoOO00O
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % OoOO00O - iI11I1II1I1I
def i11II ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if 'Dad!' in o0O0oo0OO0O :
   pass
  elif 'Family Guy' in o0O0oo0OO0O :
   pass
  elif '2 Stupid' in o0O0oo0OO0O :
   pass
  elif 'The Zelfs' in o0O0oo0OO0O :
   pass
  elif 'A Clone' in o0O0oo0OO0O :
   pass
  elif 'A.T.O.M' in o0O0oo0OO0O :
   pass
  elif 'Almost Naked' in o0O0oo0OO0O :
   pass
  elif 'Angry Kid' in o0O0oo0OO0O :
   pass
  elif 'Annoying Orange' in o0O0oo0OO0O :
   pass
  elif 'Aqua Teen' in o0O0oo0OO0O :
   pass
  elif 'Assy Mcgee' in o0O0oo0OO0O :
   pass
  elif 'Astroblast' in o0O0oo0OO0O :
   pass
  elif 'Atomic Betty' in o0O0oo0OO0O :
   pass
  elif 'Axe Cop' in o0O0oo0OO0O :
   pass
  elif 'Baby Playpen' in o0O0oo0OO0O :
   pass
  elif 'Beavis and Butt' in o0O0oo0OO0O :
   pass
  elif 'Celebrity Deathmatch' in o0O0oo0OO0O :
   pass
  elif 'Clerks The' in o0O0oo0OO0O :
   pass
  elif 'Crapston Villas' in o0O0oo0OO0O :
   pass
  elif 'Duckman:' in o0O0oo0OO0O :
   pass
  elif 'Stripperella' in o0O0oo0OO0O :
   pass
  elif 'Vixen' in o0O0oo0OO0O :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: O00Oo000ooO0 . oO00Oo0o000 . oO0o
def Oo0O0O00Oo ( url ) :
 OoO000O0Oo = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for i11ii1ii11i in iIIi1i1 :
  I111Ii = i11ii1ii11i
 oOo00OooO0oO = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in oOo00OooO0oO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10007 , I111Ii )
  if 34 - 34: I11i / IIiI1I % o0o00Oo0O . oO0o . ooOoO0O00
  if 29 - 29: o0o00Oo0O . oO00Oo0o000
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: O0O0O * iI11I1II1I1I % iI11I1II1I1I * O00Oo000ooO0 - O0oOO0 - O00Oo000ooO0
def o0O0oO0 ( url , IMAGE ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  print o0O0oo0OO0O + '     ' + url
  if 'easy' in url :
   oo0i1 ( url )
   if 27 - 27: oO00Oo0o000 + ii - OOooOOo
   if 15 - 15: O0O0O / Ii1i111I * o0o00Oo0O . IIiIiII11i - oO0o
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 90 - 90: O0O0O
def oo0i1 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O00OO ( url )
  if 94 - 94: IIiI1I + OoOO00O % I11i
  if 1 - 1: OOooOOo % oO00Oo0o000 - i1IiIIIII + O0O0O + o0o00Oo0O * I11i
  if 97 - 97: OOooOOo
def OoOo ( ) :
 if 70 - 70: I1ii11iIi11i - O0O0O . iI11I1II1I1I % Ii1i111I / OOooOOo - o0o00Oo0O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Stand Up[/COLOR]' , '' , 10014 , OOoOO0oo0ooO + 'StandUp.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Comedian[/COLOR]' , '' , 10015 , OOoOO0oo0ooO + 'SearchComedian.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Others[/COLOR]' , '' , 10017 , OOoOO0oo0ooO + 'Others.png' , i1iIIi1 , '' )
 if 55 - 55: IIiI1I - oO0o
def o0i1I11iI1iiI ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiII )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  if 'elete' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 222 , i11ii1ii11i )
   if 48 - 48: Ii1i111I . ii . oOo0O0Ooo . OOooOOo % Ii1I / IIiI1I
def ii1I111i1Ii ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOOooO0OO0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , I1iIiiiI1 , i1iII1IiiIiI1 in OOOooO0OO0o :
  for O0oOOoooOO0O in I1iIiiiI1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1iIII1IiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for IiIIIIIi , o0O0oo0OO0O in I1iIII1IiiI :
    if 'tube' in IiIIIIIi :
     pass
    elif 'stage' in IiIIIIIi :
     Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + I1iIiiiI1 + '   -   ' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i11ii1ii11i , )
    elif 'vee' in IiIIIIIi :
     pass
     if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
def Ii1Iii11 ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOOooO0OO0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , I1iIiiiI1 , i1iII1IiiIiI1 in OOOooO0OO0o :
  I1iIII1IiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for IiIIIIIi , o0O0oo0OO0O in I1iIII1IiiI :
   if 'tube' in IiIIIIIi :
    pass
   elif 'stage' in IiIIIIIi :
    Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + I1iIiiiI1 + '   -   ' + o0O0oo0OO0O + '[/COLOR]' , ( IiIIIIIi ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + i11ii1ii11i )
   elif 'vee' in IiIIIIIi :
    pass
    if 97 - 97: i1IiIIIII / O0O0O . IIiIiII11i
    if 44 - 44: OoOO00O % Ii1i111I . oO00Oo0o000
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: iI11I1II1I1I + Ii1i111I * oOo0O0Ooo - i1IiIIIII / oOo0O0Ooo
def o00iI1i1II ( url ) :
 IIiII = Iiii ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIi = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIiII )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIi ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIi :
  O00OO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 14 - 14: O0oOO0 - iI11I1II1I1I / o0o00Oo0O % O00Oo000ooO0 . OOooOOo
  if 18 - 18: O0O0O * O0O0O % O0O0O
  if 17 - 17: o0o00Oo0O * OOooOOo * Ii1I * IIiIiII11i * Ii1i111I % ooOoO0O00
  if 33 - 33: Ii1I * Ii1I . O0oOO0 . Ii
  if 48 - 48: I11i . OoOO00O + OOooOOo % Ii1I / Ii
  if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + O00Oo000ooO0 % Ii % OOooOOo
  if 78 - 78: OoOO00O + OOooOOo + O00Oo000ooO0 - O00Oo000ooO0 . Ii / oO0o
def I11i11i1 ( ) :
 if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / Ii1i111I . O0oOO0 / ooOoO0O00
 iI1i1iIi1iiII ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iIIi1 , '' )
 iI1i1iIi1iiII ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 53 - 53: Ii1i111I
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 68 - 68: O0O0O / oO00Oo0o000 % oO00Oo0o000 % o0o00Oo0O
def o0Ii1 ( ) :
 iI1i1iIi1iiII ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 iI1i1iIi1iiII ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 50 - 50: O0O0O - O0oOO0 / iI11I1II1I1I - oO0o + IIiIiII11i - o0o00Oo0O
 oO00OOoO00 ( 'movies' , 'MAIN' )
def oOOOOoO00Ooo0 ( ) :
 if 18 - 18: O0oOO0 + OoOO00O
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 ii11i11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 70 - 70: ooOoO0O00 . oOo0O0Ooo . IIiIiII11i . ii
 for oOOOo in ii11i11 :
  IIiIii = OOO00 + oOOOo + OooO0
  IIiII = i1I1iI ( IIiIii )
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiII )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iIi11i1 , o0O0oo0OO0O in o0O00oOoOO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    O0Oo0 ( o0O0oo0OO0O , IiIIIIIi , 222 , oOOO00o000o , iIi11i1 , O00OoOO0oo0 )
    if 99 - 99: Ii1I . oO0o * Ii1i111I % oO00Oo0o000
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 14 - 14: oO0o / oO0o * o0o00Oo0O . O0O0O
    if 59 - 59: IIiIiII11i * Ii
def ooOooO00Oo ( ) :
 if 86 - 86: IIiIiII11i + O0oOO0 + O00Oo000ooO0
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 ii11i11 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 9 - 9: O0oOO0 + IIiIiII11i % O0oOO0 % O00Oo000ooO0 + iI11I1II1I1I
 for oOOOo in ii11i11 :
  oO00 = OOO00 + oOOOo + OooO0
  IIiII = i1I1iI ( oO00 )
  o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIiII )
  for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , IiI1II11iiI in o0O00oOoOO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iI1i1iIi1iiII ( o0O0oo0OO0O , IiIIIIIi , IiI1II11iiI , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
    if 56 - 56: IIiI1I
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 84 - 84: OOooOOo - Ii
    if 1 - 1: IIiI1I * OOooOOo
def OO0ooo0 ( ) :
 if 7 - 7: Ii1I - O0O0O * i1IiIIIII + I11i . Ii1I
 OoO000O0Oo = Iiii ( OOO00 + 'spongemain.php' )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , IiI1II11iiI in o0O00oOoOO :
  iI1i1iIi1iiII ( o0O0oo0OO0O , IiIIIIIi , IiI1II11iiI , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
  oO00OOoO00 ( 'movies' , 'MAIN' )
def ooooO ( url ) :
 if 92 - 92: I11i / I11i * OoOO00O
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iI111i11iI1 = ( '%s%s' % ( III1ii , url ) )
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in o0O00oOoOO :
  i11I1I = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
  for oo0ooooo00o in i11I1I :
   if oo0ooooo00o == url :
    o0O0oo0OO0O = ( '[COLORred]Watched - [/COLOR]' + o0O0oo0OO0O ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  O0Oo0 ( o0O0oo0OO0O , url , 222 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
  if 78 - 78: iI11I1II1I1I . I11i % iI11I1II1I1I . o0o00Oo0O / i1IiIIIII
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 76 - 76: ooOoO0O00 * ii * o0o00Oo0O + oO00Oo0o000 * oO00Oo0o000
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: I11i
  if 73 - 73: o0o00Oo0O - Ii1I
def ii1I ( url ) :
 if 98 - 98: ooOoO0O00
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , O00OoOO0oo0 , url , i11ii1ii11i , iIi11i1 , IiI1II11iiI in o0O00oOoOO :
  iI1i1iIi1iiII ( o0O0oo0OO0O , url , IiI1II11iiI , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
  if 51 - 51: Ii1I + O0oOO0 + I1ii11iIi11i / ooOoO0O00 + ooOoO0O00
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 12 - 12: iI11I1II1I1I . OoOO00O . Ii1I % oOo0O0Ooo . IIiIiII11i . O0O0O
  if 32 - 32: Ii1I + O00Oo000ooO0 / o0o00Oo0O / OOooOOo * ii % O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: oO0o
def O0Oo0 ( name , url , mode , iconimage , fanart , description ) :
 if 66 - 66: iI11I1II1I1I
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiIIiiii11 . setProperty ( "Fanart_Image" , fanart )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = False )
 return Ii1IIIII
 if 39 - 39: O0O0O . o0o00Oo0O . OoOO00O % ooOoO0O00 % i1IiIIIII
def iI1i1iIi1iiII ( name , url , mode , iconimage , fanart , description ) :
 if 50 - 50: O00Oo000ooO0 + I11i
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiIIiiii11 . setProperty ( "Fanart_Image" , fanart )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = True )
 return Ii1IIIII
if 96 - 96: oO0o
if 92 - 92: I1ii11iIi11i / Ii + Ii1I
if 87 - 87: OOooOOo % iI11I1II1I1I
if 72 - 72: i1IiIIIII . i1IiIIIII - Ii1I
if 48 - 48: I1ii11iIi11i - O0oOO0 + I1ii11iIi11i - oOo0O0Ooo * Ii . IIiI1I
if 35 - 35: O00Oo000ooO0 . o0o00Oo0O + I1ii11iIi11i + i1IiIIIII + ooOoO0O00
if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
if 58 - 58: i1IiIIIII . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
if 50 - 50: IIiI1I % IIiIiII11i - O0oOO0 . ooOoO0O00 + o0o00Oo0O % IIiI1I
if 10 - 10: IIiI1I . ooOoO0O00 + OoOO00O
if 66 - 66: oO0o % I11i
if 21 - 21: OOooOOo - ii % Ii
if 71 - 71: ooOoO0O00 - Ii1i111I * oO00Oo0o000 + O0O0O - oO0o % Ii1I
if 63 - 63: iI11I1II1I1I + i1IiIIIII . oO0o / oOo0O0Ooo
def oO0OIiii1I ( string ) :
 if IIIii1II1II == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
def O00O ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 II1 = [ ]
 try :
  if 91 - 91: i1IiIIIII + oO00Oo0o000 . Ii1i111I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  oO0OIiii1I ( 'Making Favorites File' )
  II1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  o0O0Oo00 = open ( iIi1ii1I1 , "w" )
  o0O0Oo00 . write ( json . dumps ( II1 ) )
  o0O0Oo00 . close ( )
 else :
  oO0OIiii1I ( 'Appending Favorites' )
  o0O0Oo00 = open ( iIi1ii1I1 ) . read ( )
  i1I111i1ii = json . loads ( o0O0Oo00 )
  i1I111i1ii . append ( ( name , url , iconimage , fanart , mode ) )
  i1i1IiIiIi1Ii = open ( iIi1ii1I1 , "w" )
  i1i1IiIiIi1Ii . write ( json . dumps ( i1I111i1ii ) )
  i1i1IiIiIi1Ii . close ( )
  if 81 - 81: I1ii11iIi11i - Ii1i111I
  if 24 - 24: ii . oO0o * IIiIiII11i
def o0oO00 ( ) :
 if os . path . exists ( iIi1ii1I1 ) == False :
  II1 = [ ]
  oO0OIiii1I ( 'Making Favorites File' )
  II1 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  o0O0Oo00 = open ( iIi1ii1I1 , "w" )
  o0O0Oo00 . write ( json . dumps ( II1 ) )
  o0O0Oo00 . close ( )
 else :
  O00o0O = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
  O00oOo0O0o00O = len ( O00o0O )
  for ooo0oo00O00Oo in O00o0O :
   o0O0oo0OO0O = ooo0oo00O00Oo [ 0 ]
   IiIIIIIi = ooo0oo00O00Oo [ 1 ]
   oOOO00o000o = ooo0oo00O00Oo [ 2 ]
   try :
    OOO000000OOO0 = ooo0oo00O00Oo [ 3 ]
    if OOO000000OOO0 == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     OOO000000OOO0 = oOOO00o000o
    else :
     OOO000000OOO0 = iIi11i1
   try : ooOoOOoooO000 = ooo0oo00O00Oo [ 5 ]
   except : ooOoOOoooO000 = None
   try : OoO0o000oOo = ooo0oo00O00Oo [ 6 ]
   except : OoO0o000oOo = None
   if 88 - 88: ooOoO0O00 * oO00Oo0o000 * O0O0O - O0oOO0 * Ii1i111I / ii
   if ooo0oo00O00Oo [ 4 ] == 0 :
    o0OOOO00O0Oo ( o0O0oo0OO0O , IiIIIIIi , '' , oOOO00o000o , iIi11i1 , '' , 'fav' )
   else :
    o0OOOO00O0Oo ( o0O0oo0OO0O , IiIIIIIi , ooo0oo00O00Oo [ 4 ] , oOOO00o000o , iIi11i1 , '' , 'fav' )
    if 41 - 41: o0o00Oo0O / oO00Oo0o000 + iI11I1II1I1I
def oO0o0o00oOo0O ( name ) :
 i1I111i1ii = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for oOOoooO0O0 in range ( len ( i1I111i1ii ) ) :
  if i1I111i1ii [ oOOoooO0O0 ] [ 0 ] == name :
   del i1I111i1ii [ oOOoooO0O0 ]
   i1i1IiIiIi1Ii = open ( iIi1ii1I1 , "w" )
   i1i1IiIiIi1Ii . write ( json . dumps ( i1I111i1ii ) )
   i1i1IiIiIi1Ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 46 - 46: iI11I1II1I1I
 if 33 - 33: Ii1i111I % Ii1i111I % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
def Iiiiii111i1ii ( ) :
 O0O0ooOoOO0OO = os . path . join ( o0 )
 I1iiIiiii1111 = open ( O0O0ooOoOO0OO , "w+" )
 if 29 - 29: OoOO00O - oOo0O0Ooo / oOo0O0Ooo * OoOO00O * O00Oo000ooO0 . i1IiIIIII
 I1iiIiiii1111 . write ( r'# This file contains the "built-in" channels' + '\n' )
 I1iiIiiii1111 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 I1iiIiiii1111 . write ( r'[plugin.video.gtv]' + '\n' )
 I1iiIiiii1111 . write ( r'BBC One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F191.m3u8&mode=3&name=[COLORgreen]BBC+One%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BBC Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F190.m3u8&mode=3&name=[COLORgreen]BBC+Two%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BBC Four=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F188.m3u8&mode=3&name=[COLORgreen]BBC+Four%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'ITV=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F208.m3u8&mode=3&name=[COLORgreen]ITV1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'ITV2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F207.m3u8&mode=3&name=[COLORgreen]ITV2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'ITV3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F206.m3u8&mode=3&name=[COLORgreen]ITV3%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'ITV4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F205.m3u8&mode=3&name=[COLORgreen]ITV4%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Channel 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F183.m3u8&mode=3&name=[COLORgreen]Channel+4%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Channel 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F185.m3u8&mode=3&name=[COLORgreen]Channel+5%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'5STAR=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F187.m3u8&mode=3&name=[COLORgreen]5%2A%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'5 USA=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F186.m3u8&mode=3&name=[COLORgreen]5USA%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'RTE One=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F194.m3u8&mode=3&name=[COLORgreen]RTE+One%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'RTE Two=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F193.m3u8&mode=3&name=[COLORgreen]RTE+Two%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'TG4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F192.m3u8&mode=3&name=[COLORgreen]TG4%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F32.m3u8&mode=3&name=[COLORgreen]Sky+1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F33.m3u8&mode=3&name=[COLORgreen]Sky+2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Living=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F35.m3u8&mode=3&name=[COLORgreen]Sky+Living%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Atlantic=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F34.m3u8&mode=3&name=[COLORgreen]Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Dave=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F325.m3u8&mode=3&name=[COLORgreen]Dave%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Pick=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F324.m3u8&mode=3&name=[COLORgreen]Pick%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'GOLD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F326.m3u8&mode=3&name=[COLORgreen]Gold%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Watch HD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F518.m3u8&mode=3&name=[COLORgreen]Watch%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'YESTERDAY=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F377.m3u8&mode=3&name=[COLORgreen]Yesterday%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Comedy Central=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F181.m3u8&mode=3&name=[COLORgreen]Comedy+Central%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'London Live=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F830.m3u8&mode=3&name=[COLORgreen]London+Live%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Disney Junior=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F230.m3u8&mode=3&name=[COLORgreen]Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Disney Chnl=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F231.m3u8&mode=3&name=[COLORgreen]Disney+Channel%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Animal Planet=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F198.m3u8&mode=3&name=[COLORgreen]Animal+Planet%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Nat Geo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F197.m3u8&mode=3&name=[COLORgreen]National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Discovery=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F200.m3u8&mode=3&name=[COLORgreen]Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Discovery Science=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F199.m3u8&mode=3&name=[COLORgreen]Discovery+Science%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Disc.Turbo=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F168.m3u8&mode=3&name=[COLORgreen]Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Food Network=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F639.m3u8&mode=3&name=[COLORgreen]Food+Network%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'MTV MUSIC=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F234.m3u8&mode=3&name=[COLORgreen]MTV+Music%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Film4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F182.m3u8&mode=3&name=[COLORgreen]Film4%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'True Movies=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F853.m3u8&mode=3&name=[COLORgreen]True+Movies%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'True Movies 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F852.m3u8&mode=3&name=[COLORgreen]True+Movies+2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Action=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F732.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky ScFiHorror=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F511.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'SkyPremiereHD=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F516.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Greats=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F512.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Family=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F509.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky DramaRom=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F510.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Thriller=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F514.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Comedy=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F1022.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Showcase=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F46.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Select=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F45.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Disney=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F195.m3u8&mode=3&name=[COLORgreen]Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F18.m3u8&mode=3&name=[COLORgreen]Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F19.m3u8&mode=3&name=[COLORgreen]Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports 3=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F20.m3u8&mode=3&name=[COLORgreen]Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports 4=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F21.m3u8&mode=3&name=[COLORgreen]Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports 5=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F22.m3u8&mode=3&name=[COLORgreen]Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports F1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F24.m3u8&mode=3&name=[COLORgreen]Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Sky Sports News=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F23.m3u8&mode=3&name=[COLORgreen]Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BT Sport 1=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F309.m3u8&mode=3&name=[COLORgreen]BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BT Sport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F26.m3u8&mode=3&name=[COLORgreen]BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BT Sport Europe=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F705.m3u8&mode=3&name=[COLORgreen]BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BT Sport ESPN=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F28.m3u8&mode=3&name=[COLORgreen]BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'BoxNation=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F173.m3u8&mode=3&name=[COLORgreen]Box+Nation+UK%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'WWENetwork=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F178.m3u8&mode=3&name=[COLORgreen]WWENetwork%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Eurosport=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F269.m3u8&mode=3&name=[COLORgreen]Eurosport+1%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Eurosport 2=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F748.m3u8&mode=3&name=[COLORgreen]Eurosport+2%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'At The Races=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F170.m3u8&mode=3&name=[COLORgreen]At+the+Races%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Racing UK=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F171.m3u8&mode=3&name=[COLORgreen]Racing+UK%0D[%2FCOLOR]' + '\n' )
 I1iiIiiii1111 . write ( r'Poker central US=plugin://plugin.video.gtv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F826.m3u8&mode=3&name=[COLORgreen]Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 80 - 80: iI11I1II1I1I
 if 23 - 23: IIiIiII11i
def o0oO0OO00oo0o ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  OOooOoooOoOo ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , OOoOO0oo0ooO + '247.png' , OOoOO0oo0ooO + '247.png' , '' )
def I1II1 ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  OOooOoooOoOo ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , OOoOO0oo0ooO + 'musicch.png' , OOoOO0oo0ooO + 'musicch.png' , '' )
def Oo000o ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  OOooOoooOoOo ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , OOoOO0oo0ooO + 'NEWS.png' , OOoOO0oo0ooO + 'NEWS.png' , '' )
def OO00oo ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  OOooOoooOoOo ( o0O0oo0OO0O , ( IiIIIIIi ) . strip ( ) , 222 , OOoOO0oo0ooO + 'adult.png' , OOoOO0oo0ooO + 'adult.png' , '' )
def O0Oo0O0 ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o0O00oOoOO = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  OOooOoooOoOo ( o0O0oo0OO0O , IiIIIIIi , 1016 , OOoOO0oo0ooO + 'TUTS.png' , OOoOO0oo0ooO + 'TUTS.png' , '' )
  if 33 - 33: O0oOO0 % ooOoO0O00 - O0O0O . o0o00Oo0O / o0o00Oo0O
  if 96 - 96: ii + O00Oo000ooO0 * o0o00Oo0O
def oo0OoOO0o0o ( ) :
 if 67 - 67: OOooOOo - OOooOOo * oO0o - IIiI1I % O0O0O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Recent Episodes[/COLOR]' , '' , 10019 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , '' , 10020 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search[/COLOR]' , '' , 10021 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 if 44 - 44: oOo0O0Ooo . ooOoO0O00 + i1IiIIIII
def iIiI1Iii1 ( ) :
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 OoO000O0Oo = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , iiOO0O0Ooo in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O + '  -  ' + ( iiOO0O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiIIIIIi , 10023 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 67 - 67: IIiIiII11i / I11i . i1IiIIIII . ii
  if 19 - 19: O00Oo000ooO0 . Ii1I / OOooOOo
  if 68 - 68: O0oOO0 / ii * Ii1i111I / O0O0O
def ooooO000 ( ) :
 if 61 - 61: O0oOO0 - i1IiIIIII + i1IiIIIII
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
 if 40 - 40: Ii . iI11I1II1I1I
def IiIIII1iiIIi ( url ) :
 I1I1I1IIi1III = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIiII = cloudflare . source ( I1I1I1IIi1III )
 o0O00oOoOO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 10022 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 17 - 17: Ii1i111I
  if 97 - 97: Ii1I * Ii1I / IIiI1I
  if 6 - 6: O0O0O
  if 72 - 72: Ii1i111I * Ii1I - OOooOOo / Ii1I + i1IiIIIII - IIiI1I
def IIii1III ( ) :
 if 94 - 94: Ii % ii / oOo0O0Ooo
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( O0oOOoooOO0O ) . replace ( ' ' , '+' )
 IIiII = cloudflare . source ( IiIIIIIi )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10022 , OOoOO0oo0ooO + 'dtv.png' )
   if 24 - 24: oOo0O0Ooo * O0O0O
   if 85 - 85: IIiIiII11i . O0oOO0 % i1IiIIIII % Ii1i111I
   if 80 - 80: O0O0O * Ii1i111I / iI11I1II1I1I % O0O0O / iI11I1II1I1I
def Iiii1 ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for i1I1IiiIi1i , i1iiIIiiiII , Ii1I1 , o0O0oo0OO0O in o0O00oOoOO :
  OO0ooO0 = ( Ii1I1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OoOooOO0oOOo0O = ( i1iiIIiiiII ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1IIiIIi1Ii1III = 'Season ' + OoOooOO0oOOo0O + 'Episode ' + OO0ooO0 + o0O0oo0OO0O
  Oooo00 ( I1IIiIIi1Ii1III , i1I1IiiIi1i )
  if 9 - 9: ii * o0o00Oo0O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: oO00Oo0o000 - O0O0O . i1IiIIIII % I11i
  if 30 - 30: Ii1I % Ii1i111I / oO00Oo0o000
def Oooo00 ( name , url ) :
 i1I1IiiIi1i = url
 i11IiI1I = name
 o0ooOooo000oOO = cloudflare . source ( i1I1IiiIi1i )
 iIIi1i1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o0ooOooo000oOO )
 for IIi , OOoooO00o0o in iIIi1i1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + i11IiI1I + OOoooO00o0o + '[/COLOR]' , IIi , 10012 , OOoOO0oo0ooO + 'dtv.png' )
  if 10 - 10: OoOO00O - Ii . Ii1I % ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - i1IiIIIII . iI11I1II1I1I
 if 30 - 30: O0oOO0 + O0oOO0 % O00Oo000ooO0 - I11i - Ii1I
def i111IiiI1Ii ( ) :
 if 72 - 72: o0o00Oo0O . OOooOOo * I1ii11iIi11i + Ii1I - I11i
 if 40 - 40: oO0o + oO0o
 if 94 - 94: IIiI1I * iI11I1II1I1I . Ii1i111I
 if 13 - 13: iI11I1II1I1I * OOooOOo / oO00Oo0o000 % O0oOO0 + O0O0O
 if 41 - 41: Ii1I
 if 5 - 5: I1ii11iIi11i
 if 100 - 100: OoOO00O + iI11I1II1I1I
 if 59 - 59: O00Oo000ooO0
 if 89 - 89: OOooOOo % iI11I1II1I1I
 if 35 - 35: Ii1I + oO00Oo0o000 - OOooOOo % O0O0O % I11i % OOooOOo
 if 45 - 45: oOo0O0Ooo * i1IiIIIII % oO0o
 if 24 - 24: O0oOO0 - Ii1i111I * O0O0O
 if 87 - 87: OoOO00O - Ii1I % Ii1I . O0O0O / Ii1I
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Program[/COLOR]' , '' , 10043 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
 if 79 - 79: O00Oo000ooO0 % oO0o
def Oo0oOO ( url ) :
 IIiII = Iiii ( url )
 oOoO0 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 o0O00oOoOO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oOoO0 ) )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 86 - 86: iI11I1II1I1I / o0o00Oo0O
def iiiIioo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
def o0OO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 76 - 76: o0o00Oo0O . oO0o + OOooOOo
  if 41 - 41: IIiIiII11i * O0oOO0
def o0oOoOo0 ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III1IiI1i1i = 'http://www.watchseries.ac/search/' + O0oOOoooOO0O . replace ( ' ' , '%20' )
 IIiII = Iiii ( III1IiI1i1i )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'watch online' in o0O0oo0OO0O :
   pass
  else :
   print IiIIIIIi
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.watchseries.ac' + IiIIIIIi , 10044 , i11ii1ii11i , '' , '' )
   if 94 - 94: IIiI1I - I1ii11iIi11i + O0O0O
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 59 - 59: Ii1i111I . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
def oO0o0Oo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , url , o0O0oo0OO0O , Ii1I1 , O00OoOO0oo0 in o0O00oOoOO :
  o0OOoOoO00O000 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( Ii1I1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0OOoOoO00O000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , i11ii1ii11i , '' , O00OoOO0oo0 )
  if 54 - 54: o0o00Oo0O - IIiI1I . i1IiIIIII % IIiI1I + IIiI1I
def i1iI1Iiii1I ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  o0OOoOoO00O000 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0OOoOoO00O000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 9 - 9: Ii1i111I / OOooOOo / IIiIiII11i + oO00Oo0o000
def o0O0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , i11ii1ii11i , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 57 - 57: i1IiIIIII - i1IiIIIII - Ii1I
def iio0o000Oo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIiII )
 oOoO0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 for i1iiIIiiiII , OOOooO0OO0o in oOoO0 :
  o0O00oOoOO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OOOooO0OO0o ) )
  for url , o0O0oo0OO0O in o0O00oOoOO :
   o0OOoOoO00O000 = ( i1iiIIiiiII ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0OOoOoO00O000 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 57 - 57: O0O0O * o0o00Oo0O * oO00Oo0o000
class I1II1oOOoo ( ) :
 if 9 - 9: Ii1i111I . oO0o * ooOoO0O00 . ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 32 - 32: OOooOOo . Ii1I % oOo0O0Ooo - IIiIiII11i
  o0OOoOoO00O000 = name
  self . Get_Sources ( IiIIIIIi , o0OOoOoO00O000 )
  if 11 - 11: o0o00Oo0O + oOo0O0Ooo
  if 80 - 80: O0O0O % O0O0O % o0o00Oo0O - Ii . IIiI1I / o0o00Oo0O
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  IIiII = Iiii ( URL )
  o0O00oOoOO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIiII )
  for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
   URL = 'http://www.watchseries.ac/link/' + IiIIIIIi
   self . Get_site_link ( URL , season_name )
   if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / OoOO00O . ooOoO0O00
 def Get_site_link ( self , url , season_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( IIiII )
  iIIi1i1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( IIiII )
  oOo00OooO0oO = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( IIiII )
  for url in o0O00oOoOO :
   self . main ( url , season_name )
  for url in iIIi1i1 :
   self . main ( url , season_name )
  for url in oOo00OooO0oO :
   self . main ( url , season_name )
   if 60 - 60: I1ii11iIi11i . O00Oo000ooO0 % oOo0O0Ooo - oO00Oo0o000
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oooOo = 'DACLIPS'
   if oooOo in I1II1oOOoo . source_list :
    pass
   else :
    self . daclips ( url , season_name , oooOo )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    oooOo = 'FILEHOOT'
    if oooOo in I1II1oOOoo . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , oooOo )
   else :
    if 'thevideo.me' in url :
     oooOo = 'THEVIDEO'
     if oooOo in I1II1oOOoo . source_list :
      pass
     else :
      self . thevideo ( url , season_name , oooOo )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      oooOo = 'ALLMYVIDEOS'
      if oooOo in I1II1oOOoo . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , oooOo )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       oooOo = 'VIDSPOT'
       if oooOo in I1II1oOOoo . source_list :
        pass
       else :
        self . vidspot ( url , season_name , oooOo )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        oooOo = 'VODLOCKER'
        if oooOo in I1II1oOOoo . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , oooOo )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 79 - 79: O0O0O - IIiIiII11i
         if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / OoOO00O * oOo0O0Ooo
 def allmyvid ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIiII )
  for OoOi1iI11Iii , o0O0oo0OO0O in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 91 - 91: i1IiIIIII + O0oOO0 % oOo0O0Ooo - O0oOO0 - O0O0O
 def vidspot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( IIiII )
  for OoOi1iI11Iii , o0O0oo0OO0O in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 42 - 42: OOooOOo
 def thevideo ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIiII )
  for OoOi1iI11Iii in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 79 - 79: ooOoO0O00
 def vodlocker ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for OoOi1iI11Iii in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 1 - 1: O0O0O / ooOoO0O00
 def daclips ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( IIiII )
  for OoOi1iI11Iii in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 74 - 74: Ii1i111I / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
 def filehoot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for OoOi1iI11Iii in o0O00oOoOO :
   self . Printer ( OoOi1iI11Iii , season_name , source_name )
   if 59 - 59: Ii . ii / Ii1i111I * Ii1I + ii
 def Printer ( self , Link , season_name , source_name ) :
  if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * IIiI1I / i1IiIIIII
  if Link in I1II1oOOoo . List :
   pass
  elif source_name in I1II1oOOoo . source_list :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + source_name + '[/COLOR]' , Link , 10012 , OOoOO0oo0ooO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   I1II1oOOoo . List . append ( Link )
   I1II1oOOoo . source_list . append ( source_name )
   if 95 - 95: O00Oo000ooO0 * o0o00Oo0O * oO00Oo0o000 . ii % I1ii11iIi11i + Ii1I
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 98 - 98: O0O0O . ii
   if 54 - 54: o0o00Oo0O / O00Oo000ooO0 % O0oOO0 * ooOoO0O00 * o0o00Oo0O
   if 48 - 48: I11i . O0O0O % OOooOOo - OOooOOo
   if 33 - 33: Ii1i111I % IIiIiII11i + oO0o
   if 93 - 93: ooOoO0O00 . O00Oo000ooO0 / oOo0O0Ooo + O00Oo000ooO0
def OOooOO ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Highlights[/COLOR]' , '' , 10008 , OOoOO0oo0ooO + 'Highlights.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Fixtures[/COLOR]' , '' , 10009 , OOoOO0oo0ooO + 'Fixtures.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Today On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , OOoOO0oo0ooO + 'PremiereLeague.png' , i1iIIi1 , '' )
 if 59 - 59: oO0o - oO0o + IIiI1I
def iiII ( url ) :
 o0OOOO00O0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for II11iiii , url , i11i1 , O00oo00OOOO , i1iIiiiiii1II , ooO0oO00O0o , IiIi1II111I , OOO , o0O0Oo00 , o00o , IIi1i1 in o0O00oOoOO :
  i11i1 = i11i1
  if 'Arsenal' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'arsenal-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                                  ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Bournemouth' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'afc-bournemouth.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                       ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Burnley' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'KEGnQWW.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                                   ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Chelsea' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'chelsea.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                                  ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Crystal' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'CrystalPalace.0.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                       ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Everton' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'Everton.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                                   ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Hull' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'hull-city-afc.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                                 ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Leicester' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'leicester-city-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                       ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Liverpool' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'liverpool-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                               ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Manchester City' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'city-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '               ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Manchester United' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + '91.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '          ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Middlesbrough' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'middlesbrough-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                 ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Southampton' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'southampton-fc-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                   ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Stoke City' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'stoke-city.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                          ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Sunderland' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'sunderland-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                        ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Swansea' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'swansea-city-afc.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                    ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Tottenham' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'tottenham-hotspur_zps4e3ed7c1.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '        ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Watford' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'watford-fc-hd-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '                              ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'Bromwich' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'west-bromwich-albion-logo.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '   ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  elif 'West Ham' in i11i1 :
   I111i1i1111 = OOoOO0oo0ooO + 'west-ham.png'
   o0O0oo0OO0O = '[COLOR' + oO0o0o0ooO0oO + ']' + II11iiii + ' - ' + i11i1 + '             ' + O00oo00OOOO + '        ' + i1iIiiiiii1II + '        ' + ooO0oO00O0o + '        ' + IiIi1II111I + '        ' + OOO + '        ' + o0O0Oo00 + '        ' + o00o + '[/COLOR]'
  o0OOOO00O0Oo ( str ( o0O0oo0OO0O ) , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I111i1i1111 , I111i1i1111 , i11i1 )
  if 84 - 84: i1IiIIIII + OoOO00O + I11i
def i1i1iIII11i ( description ) :
 i11i1 = description
 IiIIIIIi = ( 'http://www.fullmatchesandshows.com/?s=' + i11i1 ) . replace ( ' ' , '%20' )
 IiIIoOo ( IiIIIIIi )
 if 69 - 69: o0o00Oo0O / IIiIiII11i * ooOoO0O00
def oOIiiIIi ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o0O00oOoOO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + IiIIIIIi , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + i11ii1ii11i , i1iIIi1 , '' )
  if 96 - 96: ooOoO0O00 . Ii1i111I + O0O0O + Ii1I * i1IiIIIII - IIiIiII11i
def iIO0OO0o0O00oO ( url ) :
 IIiII = Iiii ( url )
 oOoO0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIiII )
 for oOoO0 in oOoO0 :
  o00OoO0o0oOo = re . compile ( '(.*?)</h2>' ) . findall ( str ( oOoO0 ) )
  for OoO0O0oo0o in o00OoO0o0oOo :
   OoO0O0oo0o = OoO0O0oo0o
  iIi11I11 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oOoO0 ) )
  for i1i , i11ii1ii11i , time , oOI11 in iIi11I11 :
   O0OoO0ooOO0o = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oOI11 )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + OoO0O0oo0o + ' - ' + i1i + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + i11ii1ii11i , i1iIIi1 , ( str ( O0OoO0ooOO0o ) ) )
   if 18 - 18: iI11I1II1I1I
 oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if 30 - 30: o0o00Oo0O + i1IiIIIII % I1ii11iIi11i . ooOoO0O00
def I111 ( ) :
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
 if 65 - 65: I1ii11iIi11i * o0o00Oo0O / OoOO00O . oO00Oo0o000 % I1ii11iIi11i
def i1Ii1i1 ( url ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , url , o0O0oo0OO0O in o0O00oOoOO :
  OoOoIiI1 = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   OoOoIiI1 = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + OoOoIiI1 + '[/COLOR]' , url , 10013 , i11ii1ii11i )
 for url , i11ii1ii11i , o0O0oo0OO0O in iIIi1i1 :
  OoOoIiI1 = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + OoOoIiI1 + '[/COLOR]' , url , 10013 , i11ii1ii11i )
def IiIIoOo ( url ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Live On G-Tv[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , OOoOO0oo0ooO + 'TodaysMacthes.png' , i1iIIi1 , '' )
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="(.+?)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( IIiII )
 if 13 - 13: ii + oO0o
 if 32 - 32: o0o00Oo0O + O0O0O % I1ii11iIi11i
 if 7 - 7: Ii1I / O0oOO0
 if 11 - 11: O00Oo000ooO0 * O0oOO0 / O0oOO0 - i1IiIIIII
 if 68 - 68: oOo0O0Ooo % O00Oo000ooO0 - O00Oo000ooO0 / oOo0O0Ooo + Ii1I - I1ii11iIi11i
 if 65 - 65: O0oOO0 - ooOoO0O00
 if 62 - 62: Ii1i111I / O0O0O % I1ii11iIi11i . ii / Ii / oO00Oo0o000
 for url , i11ii1ii11i , o0O0oo0OO0O in iIIi1i1 :
  OoOoIiI1 = o0O0oo0OO0O . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in o0O0oo0OO0O :
   pass
  else :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + OoOoIiI1 + '[/COLOR]' , url , 10013 , i11ii1ii11i )
   if 60 - 60: oOo0O0Ooo % O0O0O / I11i % O0O0O * Ii / IIiI1I
def i1Ii11IIi1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( IIiII )
 for IIi in o0O00oOoOO :
  iiiiI11ii = ( IIi ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  O00OO ( 'http:' + iiiiI11ii )
  if 73 - 73: ooOoO0O00 % ii
  if 25 - 25: O0O0O + IIiIiII11i
  if 79 - 79: O0oOO0
  if 40 - 40: I11i + Ii1i111I
def OoO000Oo0oO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 8046 , i11ii1ii11i )
 for url in iIIi1i1 :
  iiI11ii1I1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , OOoOO0oo0ooO + 'Next.png' )
def iiiIiiiI1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  O00OO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 50 - 50: O0oOO0 * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
def i11IIO00oo0O00 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 65 - 65: i1IiIIIII + IIiIiII11i
def Oo0O0OO0OoO0 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 26 - 26: i1IiIIIII * I1ii11iIi11i
 o0O00oOoOO = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 if 31 - 31: Ii1i111I * O0O0O . OoOO00O
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 8041 , OOoOO0oo0ooO + 'documentary.png' )
  if 35 - 35: Ii1i111I
  if 94 - 94: O0oOO0 / Ii % o0o00Oo0O
  if 70 - 70: Ii1i111I - I1ii11iIi11i / ii % ii
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooo0o0OOO0 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , i11ii1ii11i )
 for o0O0oo0OO0O , url , i11ii1ii11i in iIIi1i1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( 'NEXT PAGE' , url , 8041 , OOoOO0oo0ooO + 'Next.png' )
  if 17 - 17: IIiIiII11i + oOo0O0Ooo
  if 59 - 59: iI11I1II1I1I % OoOO00O . Ii
def OOo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , i11ii1ii11i , url , IIi1iI in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , i11ii1ii11i )
 for url in iIIi1i1 :
  O0OOOO0000O ( ( url ) . replace ( '//' , 'http://' ) )
  if 38 - 38: I1ii11iIi11i
def O0OOOO0000O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  Ooo0OOoOoO0 ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoOO0oo0ooO + 'documentary.png' )
  if 34 - 34: OOooOOo
def OoO0o00OOOOO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , i11ii1ii11i )
 for url in iIIi1i1 :
  iiI11ii1I1 ( 'NEXT' , url , 8048 , OOoOO0oo0ooO + 'Next.png' )
def I1iIi1iIIIIiI ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in iIIi1i1 :
  if 'rtd' in url :
   O000oooOO0Oo0 ( url )
   if 31 - 31: O00Oo000ooO0 - oO0o / i1IiIIIII . ooOoO0O00 / OoOO00O
def O000oooOO0Oo0 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for O00oO , file in o0O00oOoOO :
  url = ( 'https://rtd.rt.com' + O00oO + file )
  O00OO ( url )
  if 66 - 66: oO0o
  if 72 - 72: oO00Oo0o000
def OoO0 ( ) :
 IIiII = Oo0o0oooo0O0 ( 'http://www.stream2watch.co/live-tv' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , i1i1111I in o0O00oOoOO :
  iiI11ii1I1 ( ( o0O0oo0OO0O + '[COLOR' + oO0o0o0ooO0oO + ']' + i1i1111I + '[/COLOR]' ) , IiIIIIIi , 8086 , i11ii1ii11i )
  if 65 - 65: Ii1i111I % O0O0O + Ii1I
def Oooo ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 8087 , i11ii1ii11i )
  if 75 - 75: iI11I1II1I1I % O00Oo000ooO0 + Ii1I * o0o00Oo0O . IIiI1I - O0oOO0
def i1IIiIIIi1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  oOoO00O ( url , o0O0oo0OO0O )
  if 31 - 31: O0oOO0 . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * IIiI1I
def oOoO00O ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIiII )
 for url in o0O00oOoOO :
  print url
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 22 - 22: Ii1i111I % O00Oo000ooO0 . OOooOOo / O0oOO0 + i1IiIIIII
def OO000OOo ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + IiIIIIIi , 3002 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def oOo0O000Ooo0 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def i11i ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 O0o0O00o0o = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url , o0O0oo0OO0O in O0o0O00o0o :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'Next.png' )
 for url , i11ii1ii11i , o0O0oo0OO0O in iIIi1i1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + i11ii1ii11i )
def II1IIiiI1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O00O00 ( url )
def O00O00 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O00OO ( url )
  if 66 - 66: I1ii11iIi11i - iI11I1II1I1I
def iIiIIi11iI ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiIIIIIi , 8065 , OOoOO0oo0ooO + 'classicmovies.png' )
def ooo00o0o ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  iII1ii1 ( url )
  if 56 - 56: OOooOOo % Ii1I - OoOO00O % iI11I1II1I1I
def OoOoO0ooooO0 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , IiIIIIIi , 8065 , OOoOO0oo0ooO + 'classictv.png' )
def IIII1ii1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  if 'mp4' in url :
   O00OO ( url )
 for url in iIIi1i1 :
  yt . PlayVideo ( url )
  if 52 - 52: oO0o - i1IiIIIII - O0oOO0 - I11i + ooOoO0O00
def Iii1 ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + IiIIIIIi , 8071 , OOoOO0oo0ooO + 'streams.png' )
def OOoO ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  if '(Free Access)' in o0O0oo0OO0O :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , OOoOO0oo0ooO + 'streams.png' )
def i1IiiI ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , o0O0oo0OO0O , url in o0O00oOoOO :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , i11ii1ii11i , iIi11i1 , '' )
  if 70 - 70: Ii1i111I . i1IiIIIII * I1ii11iIi11i / i1IiIIIII
def Oo0OoOo ( ) :
 iIIIIiiIii ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 iIIIIiiIii ( 'Genres' , 'http://www.xvideos.com' , 10106 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 iIIIIiiIii ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 iIIIIiiIii ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 iIIIIiiIii ( 'Search' , '' , 10107 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' , )
 if 13 - 13: I11i
def IIi1ii ( url ) :
 IIiII = Iiii ( url )
 Ii1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in Ii1i1i :
  iIIIIiiIii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIiII )
 for url , o0O0oo0OO0O , OO0 in o0O00oOoOO :
  iIIIIiiIii ( ( o0O0oo0OO0O + ' - No of Videos : ' + ( OO0 ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 83 - 83: Ii1i111I - Ii1I * O0O0O
def oOO00OO0OooOo ( url ) :
 IIiII = Iiii ( url )
 Ii1i1i = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIiII )
 for url in Ii1i1i :
  iIIIIiiIii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , url , o0O0oo0OO0O , ii111iI1i1 in o0O00oOoOO :
  iIIIIiiIii ( o0O0oo0OO0O + '--' + ii111iI1i1 , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( i11ii1ii11i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 80 - 80: oO0o / O00Oo000ooO0 * oOo0O0Ooo % O00Oo000ooO0
  if 95 - 95: o0o00Oo0O / Ii1i111I . oO00Oo0o000
def iII11II1II ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , url , o0O0oo0OO0O , IiIi1iIIi1 , OOO00000o0 in o0O00oOoOO :
  iIIIIiiIii ( o0O0oo0OO0O + ' - Porn Quality : ' + OOO00000o0 + ' - ' + IiIi1iIIi1 , 'http://www.xvideos.com' + url , 10108 , i11ii1ii11i , i11ii1ii11i , OOO00000o0 + ' - ' + IiIi1iIIi1 )
 OOOO000Ooo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for url in OOOO000Ooo0O :
  iIIIIiiIii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 96 - 96: I1ii11iIi11i + oO00Oo0o000 . ooOoO0O00
def OooIii1I1iI ( url ) :
 IIiII = Iiii ( url )
 oOoO0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 Ii1i1i = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in Ii1i1i :
  iIIIIiiIii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( oOoO0 ) )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  iIIIIiiIii ( o0O0oo0OO0O , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 62 - 62: O0O0O + I1ii11iIi11i / Ii
  if 90 - 90: iI11I1II1I1I + OOooOOo
def IiI ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIiI = ( O0oOOoooOO0O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 Oo0o0O00 = IIiI . lower ( )
 II1iI1iiiI = 'http://www.xvideos.com/?k=' + Oo0o0O00
 print II1iI1iiiI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIiII = Iiii ( II1iI1iiiI )
 o0O00oOoOO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O , IiIi1iIIi1 , OOO00000o0 in o0O00oOoOO :
  iIIIIiiIii ( o0O0oo0OO0O + ' - Porn Quality : ' + OOO00000o0 + ' - ' + IiIi1iIIi1 , 'http://www.xvideos.com' + IiIIIIIi , 10108 , i11ii1ii11i , i11ii1ii11i , OOO00000o0 + ' - ' + IiIi1iIIi1 )
 OOOO000Ooo0O = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for IiIIIIIi in OOOO000Ooo0O :
  iIIIIiiIii ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + IiIIIIIi , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 75 - 75: ii . i1IiIIIII + oO0o / OoOO00O - oOo0O0Ooo % OoOO00O
def O0OooooO0o0O0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIiII )
 iIIi1i1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIiII )
 oOo00OooO0oO = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']LOW[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in iIIi1i1 :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HIGH[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in oOo00OooO0oO :
  if 'http' in url :
   Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']HLS[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
   if 74 - 74: OOooOOo / ooOoO0O00 % ii
def o00o0o000Oo ( url ) :
 IiIii1ii = xbmc . Player ( Oooo00OOo ( ) )
 import urlresolver
 try : IiIii1ii . play ( url )
 except : pass
 if 6 - 6: O0O0O / oOo0O0Ooo / OOooOOo
 if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 o0O00oOoOO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + IiIIIIIi ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , OOoOO0oo0ooO + 'gofish.png' )
def Ii1I1IIIiI1i ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( IIiII )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , OOoOO0oo0ooO + 'gofish.png' )
 for url , o0O0oo0OO0O , i11ii1ii11i in iIIi1i1 :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , OOoOO0oo0ooO + 'Next.png' )
def o0Oo00oOO ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 73 - 73: Ii1i111I / ii . IIiIiII11i - O00Oo000ooO0 * O0oOO0 * O00Oo000ooO0
  if 45 - 45: o0o00Oo0O * oO00Oo0o000 + Ii - i1IiIIIII - iI11I1II1I1I
  if 5 - 5: i1IiIIIII % I1ii11iIi11i % O00Oo000ooO0 % O0oOO0
I1Iiii = '{PQ},' ; I1I1Iii1Iiii = '{SC},' ; i1i1Ii1IiIII = '{XG},' ; I1IIii11 = '{JP},' ; I1I1 = '{HW},' ; O0OOO0ooO00o = '{RT},'
def I1iii1 ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 iIiiiIIiii = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OO0Oo00Oo = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 iIi = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O0OoOOoooo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0o = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + O0oOOoooOO0O
 Ii1iIiIi1I11 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 ii1I11OOO0 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 I1Ii1 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 O0oo0oOoO00 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 48 - 48: Ii1I
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIiII = i1I1iI ( IiIIIIIi )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0ooOooo000oOO = i1I1iI ( i1I1IiiIi1i )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Oo0oOOo = i1I1iI ( I1i1iiiI1 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( OO0Oo00Oo )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 o0o = i1I1iI ( iIi )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1I1I1I = i1I1iI ( O0o )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 iII1III = i1I1iI ( Ii1iIiIi1I11 )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0oo0oO00o = i1I1iI ( ii1I11OOO0 )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 I1ii111i1ii1 = i1I1iI ( I1Ii1 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0Ii11iIiiI = i1I1iI ( O0oo0oOoO00 )
 if 82 - 82: ii
 if 75 - 75: IIiIiII11i % oOo0O0Ooo + i1IiIIIII % ii / O00Oo000ooO0
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
  for Ii111I11 , o0O0oo0OO0O in o0O00oOoOO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiIIIIIi + Ii111I11 ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0ooOooo000oOO )
  for Ii111I11 , o0O0oo0OO0O in iIIi1i1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( i1I1IiiIi1i + Ii111I11 ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if Oo0oOOo != 'Failed' :
  oOo00OooO0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oOOo )
  for Ii111I11 , o0O0oo0OO0O in oOo00OooO0oO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1i1iiiI1 + Ii111I11 ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if Oo0OoO00oOO0o != 'Failed' :
  I1IIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for Ii111I11 , o0O0oo0OO0O in I1IIi :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , IiIIIIIi , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if o0o != 'Failed' :
  Oo0O0oo = [ ]
  o0O0oO0o0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in o0O0oO0o0 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    if o0O0oo0OO0O in Oo0O0oo :
     pass
    else :
     o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , IiIIIIIi , 1016 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
     Oo0O0oo . append ( o0O0oo0OO0O )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if i1I1I1I != 'Failed' :
  ooOoOoO0 = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1I1I1I )
  for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in ooOoOoO0 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + IiIIIIIi , 7067 , i11ii1ii11i )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 31 - 31: Ii - O0oOO0 / Ii1I - OoOO00O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iII1III != 'Failed' :
  iiIiIi1111iI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1III )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in iiIiIi1111iI1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Redemption[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 11 - 11: Ii1I . Ii1I + IIiIiII11i * OOooOOo . O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if O0oo0oO00o != 'Failed' :
  I1I1i1I1I1I1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oo0oO00o )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in I1I1i1I1I1I1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Reaper[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 34 - 34: oO0o * OoOO00O * I1ii11iIi11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if I1ii111i1ii1 != 'Failed' :
  Iioo0O00ooo0o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1ii111i1ii1 )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in Iioo0O00ooo0o :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Herovision[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 29 - 29: ii . IIiIiII11i % OOooOOo
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 26 - 26: iI11I1II1I1I - Ii1I . O00Oo000ooO0 . O00Oo000ooO0 + iI11I1II1I1I * I1ii11iIi11i
 if o0Ii11iIiiI != 'Failed' :
  O0Oo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( o0Ii11iIiiI )
  for IiIIIIIi , oOOO00o000o , o0O0oo0OO0O in O0Oo00 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Silent Hunter[/COLOR]' ) , IiIIIIIi , 222 , oOOO00o000o )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 63 - 63: ooOoO0O00 % Ii % IIiIiII11i * ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 ii11i11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 40 - 40: I1ii11iIi11i
 for oOOOo in ii11i11 :
  IIiIii = OOO00 + oOOOo + OooO0
  iI1Ii11 = i1I1iI ( IIiIii )
  if iI1Ii11 != 'Failed' :
   Ooo0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1Ii11 )
   for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in Ooo0 :
    if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
     OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source Pandoras[/COLOR]' , IiIIIIIi , 222 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 49 - 49: IIiIiII11i + ii . O0O0O + Ii / O0O0O
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 39 - 39: oO0o + o0o00Oo0O + O0oOO0 * IIiIiII11i % o0o00Oo0O - o0o00Oo0O
 ii11i11 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 41 - 41: O00Oo000ooO0 % I11i
 if 67 - 67: o0o00Oo0O % oO00Oo0o000
 for oOOOo in ii11i11 :
  IIiIii = iIiiiIIiii + oOOOo
  III = i1I1iI ( IIiIii )
  if III != 'Failed' :
   I1I = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( III )
   for Ii111I11 , o0O0oo0OO0O in I1I :
    if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
     Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iIiiiIIiii + oOOOo + Ii111I11 ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 70 - 70: OoOO00O . o0o00Oo0O - i1IiIIIII
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 62 - 62: oO00Oo0o000 * Ii1i111I
     if 74 - 74: OOooOOo . iI11I1II1I1I
def oOOoO0oO0oo0O ( ) :
 if 55 - 55: I1ii11iIi11i
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 if 35 - 35: Ii1I * IIiI1I . O00Oo000ooO0 . O00Oo000ooO0 - O0O0O % OOooOOo
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( O0oOOoooOO0O ) . replace ( ' ' , '%20' )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 OO0Oo00Oo = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 iIi = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Oo0o0O00 ) . replace ( ' ' , '+' )
 O0OoOOoooo = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 Ii1iIiIi1I11 = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 42 - 42: I11i - iI11I1II1I1I % ii
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 43 - 43: I11i - I1ii11iIi11i
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIiII = i1I1iI ( IiIIIIIi )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 o0ooOooo000oOO = i1I1iI ( i1I1IiiIi1i )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0oOOo = i1I1iI ( I1i1iiiI1 )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( OO0Oo00Oo )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0o = cloudflare . source ( iIi )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 III = i1I1iI ( O0OoOOoooo )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1I1I1I = i1I1iI ( O0o )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 iII1III = i1I1iI ( Ii1iIiIi1I11 )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 85 - 85: IIiIiII11i + oO00Oo0o000 - O0oOO0 * iI11I1II1I1I % O0O0O
 if iII1III != 'Failed' :
  iiIiIi1111iI1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1III )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in iiIiIi1111iI1 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source HeroVision[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 62 - 62: OoOO00O + o0o00Oo0O * oO0o
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: IIiIiII11i
 if i1I1I1I != 'Failed' :
  ooOoOoO0 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1I1I )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in ooOoOoO0 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- source Reaper[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 43 - 43: I1ii11iIi11i + ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 47 - 47: O0oOO0
    if 92 - 92: Ii1i111I % Ii % I1ii11iIi11i
    if 23 - 23: IIiIiII11i * IIiI1I
    if 80 - 80: oO00Oo0o000 / Ii + ii
    if 38 - 38: Ii1I % O0oOO0 + ooOoO0O00 * ii * O0O0O
    if 83 - 83: iI11I1II1I1I - O0oOO0 - oO00Oo0o000 / oO0o - o0o00Oo0O
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 81 - 81: OoOO00O - O0O0O * Ii1I / oO00Oo0o000
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
  for i11ii1ii11i , IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + IiIIIIIi , 10044 , i11ii1ii11i , '' , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 21 - 21: oO0o
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: Ii1i111I . o0o00Oo0O * Ii1i111I + iI11I1II1I1I
    if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - OoOO00O
    if 79 - 79: IIiIiII11i - O0O0O * Ii1I - OOooOOo . Ii1I
    if 11 - 11: o0o00Oo0O * OOooOOo
    if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % oO00Oo0o000 / IIiI1I
    if 18 - 18: ii
    if 57 - 57: O0oOO0 . OOooOOo * I11i - ii
    if 75 - 75: Ii / I11i . O00Oo000ooO0 . ooOoO0O00 . ooOoO0O00 / Ii1i111I
    if 94 - 94: O0oOO0 + oOo0O0Ooo
    if 56 - 56: OOooOOo % I11i
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOooo000oOO )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in iIIi1i1 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , IiIIIIIi , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 40 - 40: i1IiIIIII / O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  oOo00OooO0oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oOOo )
  for o0O0oo0OO0O in oOo00OooO0oO :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i1iiiI1 + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 29 - 29: OoOO00O - OoOO00O / O0oOO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0OoO00oOO0o != 'Failed' :
  I1IIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for o0O0oo0OO0O in I1IIi :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( OO0Oo00Oo + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 49 - 49: Ii1i111I + O0O0O % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  o0O0oO0o0 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( o0o )
  for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O0oO0o0 :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source - Dizi[/COLOR]' , IiIIIIIi , 8062 , i11ii1ii11i )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 4 - 4: IIiIiII11i - O0O0O % I1ii11iIi11i * Ii
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if III != 'Failed' :
  I1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( III )
  for IiIIIIIi , oOOO00o000o , O00OoOO0oo0 , iI1III1iIi11 , o0O0oo0OO0O in I1I :
   if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '- Source Scooby[/COLOR]' ) , IiIIIIIi , 1016 , oOOO00o000o , iI1III1iIi11 , O00OoOO0oo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 18 - 18: I1ii11iIi11i % o0o00Oo0O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 IIIIIiiI11i1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if III != 'Failed' :
  for oOOOo in IIIIIiiI11i1 :
   IIiIii = OOO00 + oOOOo + OooO0
   I1ii111i1ii1 = Iiii ( IIiIii )
   if I1ii111i1ii1 != 'Failed' :
    Iioo0O00ooo0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1ii111i1ii1 )
    for o0O0oo0OO0O , O00OoOO0oo0 , IiIIIIIi , i11ii1ii11i , iIi11i1 , IiI1II11iiI in Iioo0O00ooo0o :
     if Oo0o0O00 in o0O0oo0OO0O . lower ( ) :
      o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' - Source Pandoras[/COLOR]' , IiIIIIIi , IiI1II11iiI , i11ii1ii11i , iIi11i1 , O00OoOO0oo0 )
      Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
      if 43 - 43: oOo0O0Ooo / IIiI1I / O0oOO0 + iI11I1II1I1I + ii
      oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
      if 33 - 33: IIiIiII11i - O00Oo000ooO0 - O0oOO0
      if 92 - 92: oO0o * O00Oo000ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo00o0OO ( ) :
 if 32 - 32: i1IiIIIII + IIiI1I + iI11I1II1I1I * I1ii11iIi11i
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIiII = Iiii ( IiIIIIIi )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIiII )
 for o0O0oo0OO0O , i11ii1ii11i , ooiIii1I1111 in o0O00oOoOO :
  I1iIiiiIi1111I = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , I1iIiiiIi1111I )
   if 45 - 45: I11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
Oo0ooooO0O0oo = '{ZH},' ; ooooOOoOoO0oO00O = '{IX},' ; ooo0O = '{LM},'
if 15 - 15: ooOoO0O00 % ii * i1IiIIIII . IIiIiII11i + o0o00Oo0O * oO0o
def IiiiI1Ii ( url ) :
 III1I1ii = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( III1I1ii )
 for url , i1iiIIiiiII , iiOO0O0Ooo , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( ( i1iiIIiiiII ) . replace ( 'Sezon' , ' Season ' ) + ( iiOO0O0Ooo ) . replace ( 'Bölüm' , ' Episode ' ) + o0O0oo0OO0O , url , 8063 , '' )
  if 4 - 4: iI11I1II1I1I . ooOoO0O00
  if 63 - 63: iI11I1II1I1I + O00Oo000ooO0 % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
  if 60 - 60: I11i . OOooOOo % oO00Oo0o000 / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / i1IiIIIII . Ii1I * O0oOO0
def oo0O ( url ) :
 III1I1ii = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( III1I1ii )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , '' )
  if 100 - 100: ii - o0o00Oo0O . Ii1i111I / Ii1i111I + IIiIiII11i * OOooOOo
  if 37 - 37: I1ii11iIi11i
  if 72 - 72: O00Oo000ooO0 % Ii1I * i1IiIIIII . Ii % O00Oo000ooO0 * i1IiIIIII
  if 15 - 15: Ii1i111I / I1ii11iIi11i * Ii1i111I
def I1111I1Ii ( ) :
 if 68 - 68: oO0o + oOo0O0Ooo * I11i . O0O0O + OOooOOo + O0oOO0
 III1I1ii = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( III1I1ii )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O , iiOO0O0Ooo in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O + '  -  ' + ( iiOO0O0Ooo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , IiIIIIIi , 8063 , i11ii1ii11i )
  if 80 - 80: OOooOOo * i1IiIIIII
def iIIii1iiiIiiI ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 8002 , i11ii1ii11i )
def oOo0O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , time , url , o0O0oo0OO0O , IIi1iI in o0O00oOoOO :
  o0OOOO00O0Oo ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , time ) , url , 1015 , i11ii1ii11i , IIi1iI )
  if 77 - 77: o0o00Oo0O
def IIii ( ) :
 if 48 - 48: O0O0O % O0oOO0 + o0o00Oo0O
 iiI11ii1I1 ( 'Coronation Street' , '' , 8001 , '' )
 iiI11ii1I1 ( 'Eastenders' , '' , 8002 , '' )
 iiI11ii1I1 ( 'Emmerdale' , '' , 8003 , '' )
 iiI11ii1I1 ( 'Hollyoaks' , '' , 8004 , '' )
 iiI11ii1I1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 27 - 27: Ii1I / i1IiIIIII
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: O00Oo000ooO0 + iI11I1II1I1I + oOo0O0Ooo + oO00Oo0o000
 if 72 - 72: oO0o + Ii + Ii1I
def oOooOoOOo0O ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'Holly' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 41 - 41: IIiI1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 88 - 88: o0o00Oo0O . O0O0O % oOo0O0Ooo
def iii111i ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'East' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 21 - 21: Ii1i111I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: O00Oo000ooO0 % oOo0O0Ooo
def IIoO ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'Emmer' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 13 - 13: ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: o0o00Oo0O + oO0o . IIiI1I * I11i * IIiI1I
def OOOo0Oo0O ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'Coro' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 48 - 48: O0oOO0 % OOooOOo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: iI11I1II1I1I % oO0o + Ii
def IiOo00O0o0O ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'Celeb' in o0O0oo0OO0O :
   i11ii1ii11i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in IiIIIIIi :
    Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , IiIIIIIi . replace ( '\\/' , '/' ) , 8006 , i11ii1ii11i )
   else :
    pass
    if 86 - 86: Ii1i111I + o0o00Oo0O + I1ii11iIi11i - Ii1i111I
def Ii1iI1IIIII ( name , url ) :
 Ooo0OOOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ooo0OOOo :
  oo0I11i1i11IiIi1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  I11i1I1Ii = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  oo0I11i1i11IiIi1 = I11i1I1Ii . replace ( '\\/' , '/' )
 iiiIIiiii11 = xbmcgui . ListItem ( name , '' , '' )
 iiiIIiiii11 . setPath ( oo0I11i1i11IiIi1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiIIiiii11 )
 if 26 - 26: ooOoO0O00 / IIiI1I . IIiI1I
 if 20 - 20: i1IiIIIII - IIiI1I / I1ii11iIi11i * oO0o
def o00OIIIIIiiI ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o0O00oOoOO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , IiIIIIIi , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
 for IiIIIIIi , o0O0oo0OO0O in iIIi1i1 :
  iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , IiIIIIIi , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
  if 38 - 38: o0o00Oo0O
def ooOi1i1i11iI11II ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'Movies' in o0O0oo0OO0O :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( IiIIIIIi ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOoOO0oo0ooO + 'popcorn.png' )
def II1iiI1iI ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i11ii1ii11i )
 for url in iIIi1i1 :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOoOO0oo0ooO + 'Next.png' )
  if 74 - 74: O00Oo000ooO0 - o0o00Oo0O / oO00Oo0o000 * OoOO00O % O0oOO0 . oO00Oo0o000
  if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
def o00oo ( url ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url , i11ii1ii11i in o0O00oOoOO :
  if '{{' in o0O0oo0OO0O :
   pass
  else :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , i11ii1ii11i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
O000Oo00 = '{UJ},' ; iI1oOoo = '{WE},' ; o00O0o00oo = '{WP},' ; iIiiII = '{PP},'
def iII1I ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url , i11ii1ii11i in o0O00oOoOO :
  if '{{' in o0O0oo0OO0O :
   pass
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , i11ii1ii11i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00oOOo0Oo ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  Oooo0o0oO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oooo0o0oO ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: O0oOO0
 if 70 - 70: iI11I1II1I1I + Ii + I1ii11iIi11i / IIiI1I
 if 9 - 9: OOooOOo - O00Oo000ooO0
def iiIiIiI111 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if '(cooltvseries.com)' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
 for url , o0O0oo0OO0O in iIIi1i1 :
  if '(cooltvseries.com)' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
def OO0OO00ooO0 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O00OO ( ( url ) . replace ( ' ' , '%20' ) )
OOOOOoO00oo00 = '{XX},' ; iIIIII11 = '{UD},' ; ooooOOO0 = '{YT},' ; Ii1i = '{JS},' ; ooooOoOooo00Oo = '{PF},'
if 72 - 72: Ii1i111I
def i1I1IIiIIi ( ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  Ooo0OOoOoO0 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( IiIIIIIi ) ) , 222 , i11ii1ii11i )
  if 33 - 33: oO0o % O00Oo000ooO0 - iI11I1II1I1I
def IIII1I ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , url , o0O0oo0OO0O in o0O00oOoOO :
  if 'youtu' in url :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , OOoOO0oo0ooO + 'Next.png' )
  if 17 - 17: oO00Oo0o000
def o0O0OOOo0 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 4 - 4: O0oOO0 + o0o00Oo0O . ooOoO0O00 * Ii1I - I11i
def IIiIIIi1iii1 ( url ) :
 OoO000O0Oo = Iiii
 o0O00oOoOO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 222 , i11ii1ii11i )
  if 37 - 37: iI11I1II1I1I % Ii1i111I / O00Oo000ooO0
  if 37 - 37: oO00Oo0o000 - O0O0O - oO0o
  if 42 - 42: iI11I1II1I1I % OoOO00O - Ii1I + iI11I1II1I1I
  if 27 - 27: o0o00Oo0O / oO0o
  if 99 - 99: OoOO00O - O00Oo000ooO0 * iI11I1II1I1I . IIiIiII11i
def OooO00o000 ( ) :
 if 36 - 36: Ii1i111I - O00Oo000ooO0 . O00Oo000ooO0
 iiI11ii1I1 ( 'All Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Entertainment' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Movies' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Music' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'News' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Sports' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Documentary' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Kids' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Food' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Religious' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'USA Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 iiI11ii1I1 ( 'Other' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
 if 84 - 84: iI11I1II1I1I + ii
def Oo0OOOOOOO0oo ( Cat_Name ) :
 if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 I1iIIIiiii = False
 I1111 = '0'
 if Cat_Name == 'All Channels' : I1iIIIiiii = True
 if Cat_Name == 'Entertainment' : I1111 = '1'
 if Cat_Name == 'Movies' : I1111 = '2'
 if Cat_Name == 'Music' : I1111 = '3'
 if Cat_Name == 'News' : I1111 = '4'
 if Cat_Name == 'Sports' : I1111 = '5'
 if Cat_Name == 'Documentary' : I1111 = '6'
 if Cat_Name == 'Kids' : I1111 = '7'
 if Cat_Name == 'Food' : I1111 = '8'
 if Cat_Name == 'Religious' : I1111 = '9'
 if Cat_Name == 'USA Channels' : I1111 = '10'
 if Cat_Name == 'Other' : I1111 = '11'
 if 67 - 67: ooOoO0O00
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( o0O00oOoOO ) )
 for o0O0oo0OO0O , i11ii1ii11i , ooiIii1I1111 in o0O00oOoOO :
  I1iIiiiIi1111I = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  if ooiIii1I1111 == I1111 :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , I1iIiiiIi1111I )
  elif I1iIIIiiii == True :
   iiI11ii1I1 ( o0O0oo0OO0O , '' , 7022 , I1iIiiiIi1111I )
  else : pass
  if 84 - 84: oO00Oo0o000 . I11i * Ii % Ii % ooOoO0O00
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 95 - 95: I11i % IIiIiII11i % Ii1i111I . IIiI1I
def i111i ( Search_Name ) :
 OoO000O0Oo = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , IiIIIIIi , i1I1IiiIi1i , I1i1iiiI1 in o0O00oOoOO :
  I1iIiiiIi1111I = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( i11ii1ii11i ) . replace ( '\\' , '' )
  Ooo0OOoOoO0 ( Search_Name + ': Link 1' , ( IiIIIIIi ) . replace ( '\\' , '' ) , 222 , I1iIiiiIi1111I )
  Ooo0OOoOoO0 ( Search_Name + ': Link 2' , ( i1I1IiiIi1i ) . replace ( '\\' , '' ) , 222 , I1iIiiiIi1111I )
  Ooo0OOoOoO0 ( Search_Name + ': Link 3' , ( I1i1iiiI1 ) . replace ( '\\' , '' ) , 222 , I1iIiiiIi1111I )
  if 36 - 36: OoOO00O
def ooOO00o0 ( ) :
 OoO000O0Oo = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOoOO0oo0ooO + 'english.png' )
def Ii1I1iIiiI1 ( ) :
 OoO000O0Oo = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'xxx.png' )
def o00i111iiIiiIiI ( ) :
 OoO000O0Oo = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , IiIIIIIi in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , ( IiIIIIIi ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'vod(1).png' )
  if 59 - 59: i1IiIIIII + oOo0O0Ooo / IIiIiII11i / OOooOOo
def oOoo00 ( url ) :
 url
 oo0ooooo00o = xbmcgui . ListItem ( o0O0oo0OO0O , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo0ooooo00o )
 return
 if 29 - 29: i1IiIIIII / OOooOOo . iI11I1II1I1I / Ii1i111I % OOooOOo % IIiI1I
 if 49 - 49: IIiIiII11i / O00Oo000ooO0 - OoOO00O
def IiIII ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , O00OoOO0oo0 , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , ( O00OoOO0oo0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 for url in iIIi1i1 :
  iiI11ii1I1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , OOoOO0oo0ooO + 'Next.png' )
  if 92 - 92: oOo0O0Ooo % IIiI1I
def iiiI1IiI ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIiII )
 for url , O00OoOO0oo0 , i11ii1ii11i in o0O00oOoOO :
  OOooOoooOoOo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , O00OoOO0oo0 )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 OOOooO0OO0o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 for Ii111IIIIii in OOOooO0OO0o :
  O00o = ( Ii111IIIIii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o0OOOO00O0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + i11ii1ii11i , '' , O00o )
  if 22 - 22: Ii * oO00Oo0o000 . I1ii11iIi11i . ii + oOo0O0Ooo
def Iii1oooo00Oo0O ( INFO ) :
 o0iI11I1II ( 'info for workout' , INFO )
 if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
 if 27 - 27: IIiIiII11i + O0oOO0 . OOooOOo - oO00Oo0o000
 if 54 - 54: OOooOOo . I1ii11iIi11i
def Ii1 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 9031 , OOoOO0oo0ooO + 'icon.png' )
def iIIi11 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 9032 , OOoOO0oo0ooO + 'icon.png' )
def iIiiII1Ii1ii ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  if '://' in o0O0oo0OO0O :
   pass
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOoOO0oo0ooO + 'icon.png' )
def iIIi1 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , OOoOO0oo0ooO + 'icon.png' )
  if 76 - 76: oOo0O0Ooo - oOo0O0Ooo - I11i % O0oOO0 * o0o00Oo0O
  if 11 - 11: OoOO00O + Ii1i111I . oO0o . Ii * oO0o
  if 18 - 18: Ii1i111I + I1ii11iIi11i - oO0o / oO00Oo0o000 / i1IiIIIII
def OOoOoO ( ) :
 OoO000O0Oo = Iiii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  if 'category' in IiIIIIIi :
   iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.disclose.tv/' + IiIIIIIi , 7010 , OOoOO0oo0ooO + 'disclose.png' )
   if 72 - 72: OOooOOo / oO00Oo0o000 * O00Oo000ooO0 % iI11I1II1I1I
   if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * i1IiIIIII / I11i
def iiIIiI1 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , i11ii1ii11i in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://www.disclose.tv/' + url , 7011 , i11ii1ii11i )
 for url in next :
  iiI11ii1I1 ( 'NEXT' , url , 7010 , OOoOO0oo0ooO + 'Next.png' )
  if 28 - 28: Ii1I * O0O0O / IIiIiII11i + i1IiIIIII - o0o00Oo0O
  if 16 - 16: IIiIiII11i / OoOO00O . OoOO00O - OoOO00O / Ii1I
def I1Ii11i1ii1i ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 oOo00OooO0oO = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  if 'http' in url :
   Ooo0OOoOoO0 ( 'video/flv' , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url , o0O0oo0OO0O in iIIi1i1 :
  Ooo0OOoOoO0 ( o0O0oo0OO0O , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url in oOo00OooO0oO :
  Ooo0OOoOoO0 ( 'YT Link' , url , 8043 , OOoOO0oo0ooO + 'disclose.png' )
  if 90 - 90: I11i
  if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
def I1111111 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOoOO0oo0ooO + 'icon.png' )
  if 57 - 57: i1IiIIIII % oO0o - oOo0O0Ooo
def i11iI11 ( name , url , img ) :
 IIiII = Iiii ( url )
 iiIIiiiIi1 = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIiII )
 oOo0o = len ( iiIIiiiIi1 )
 if 63 - 63: O00Oo000ooO0 % O0oOO0 * OOooOOo - O00Oo000ooO0 + IIiI1I % Ii
 if 3 - 3: Ii1i111I . iI11I1II1I1I * IIiI1I + O0O0O . o0o00Oo0O . I11i
 if oOo0o == 1 :
  for oo00o00O0 in iiIIiiiIi1 :
   oo00o00O0 = oo00o00O0 . replace ( 'player' , 'watch' )
   O00o0OoooOo00 = oo00o00O0 + '&fv=&sou='
   iII1II = Iiii ( O00o0OoooOo00 )
   iiI111iIi1 = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( iII1II )
   for OoOi1iI11Iii in iiI111iIi1 :
    I1i1ii1ii = False
    Resolve ( OoOi1iI11Iii )
    if 32 - 32: O00Oo000ooO0 / ii
 elif oOo0o > 1 :
  if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - IIiI1I - Ii
  for oo00o00O0 in iiIIiiiIi1 :
   oo0O00o0 = Iiii ( oo00o00O0 )
   Oo0oOooOooO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oo0O00o0 )
   ii1I1iIII = Oo0oOooOooO
   ii1I1iIII = ( str ( ii1I1iIII ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ii1I1iIII
   Ooo0OOoOoO0 ( 'DOUBLE LINK' , ii1I1iIII , 424 , '' )
   if 11 - 11: OOooOOo / Ii / OOooOOo % oO0o - IIiI1I + IIiIiII11i
   for url in Oo0oOooOooO :
    iiI11ii1I1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i1I1IiiIi1i = Google . resolve ( url )
    except :
     pass
    try :
     ii1111II11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i1I1IiiIi1i ) )
     for i1111i11 , i1i11Iiii1iii in ii1111II11 :
      if 21 - 21: ooOoO0O00
      HD_URLS . append ( i1111i11 )
      SD_URLS . append ( i1i11Iiii1iii )
    except :
     pass
 else :
  pass
  if 69 - 69: OOooOOo + OOooOOo + i1IiIIIII % i1IiIIIII * Ii1i111I % OoOO00O
def ii1111IIiI1 ( ) :
 if 59 - 59: OoOO00O - I1ii11iIi11i
 if 34 - 34: OoOO00O - O0O0O * ii . oO0o / oOo0O0Ooo
 iiI11ii1I1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOoOO0oo0ooO + 'Movies.png' )
 if 66 - 66: I1ii11iIi11i / Ii % O0oOO0
 iiI11ii1I1 ( 'Search Movies' , '' , 7017 , OOoOO0oo0ooO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 43 - 43: i1IiIIIII
 if 84 - 84: i1IiIIIII . O00Oo000ooO0 . IIiI1I
def iIII1I1i ( ) :
 OoO000O0Oo = Iiii ( 'http://cnfstudio.com/' )
 o0O00oOoOO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , 'http://cnfstudio.com/genre/' + IiIIIIIi , 7003 , OOoOO0oo0ooO + 'icon.png' )
  if 26 - 26: IIiI1I - I1ii11iIi11i + oOo0O0Ooo + I11i
oooOOOOO = xbmcgui . Dialog ( )
if 37 - 37: I11i * i1IiIIIII + oOo0O0Ooo . Ii1I * ii
OoooOO0 = '{UN},' ; oo0OoO = '{IG},' ; iIIi1iii1 = '{PL},' ; o00o0 = '{LO},' ; OOoOo0O0 = '{LP},' ; I1o0 = '{HA},' ; I1IiiiiI1i1I = '{XD},' ; I11i1I1 = '{TA},' ; ooOooO = '{DP},' ; oooo = '{JT},' ; IIIiI1iIIII = '{JJ},' ; o0oo00OOOo = '{MM},' ; oo0oO = '{FQ},' ; i1i1IIi = '{HH},'
if 93 - 93: O0O0O
def o0Oo ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 III1IIiIi1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for i11ii1ii11i , url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , i11ii1ii11i )
 III1IIiIi1 = III1IIiIi1
 for url in III1IIiIi1 :
  iiI11ii1I1 ( 'Next Page' , url , 7003 , OOoOO0oo0ooO + 'Next.png' )
  if 97 - 97: I11i / O00Oo000ooO0 + OOooOOo + oO0o % oO00Oo0o000
def iIIi1II1 ( url ) :
 if 42 - 42: iI11I1II1I1I - O0oOO0 - Ii1i111I - oO00Oo0o000
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  O00oO = url + '&fv=&sou='
  O00oO = O00oO . replace ( 'player' , 'watch' )
  iIiI11II = OO0Iii1iIiI111Ii ( O00oO )
  ooO0oo0000oOo = OO0Iii1iIiI111Ii ( url )
  if 72 - 72: OoOO00O
  if 65 - 65: OOooOOo . IIiIiII11i % IIiI1I + OoOO00O
def OO0Iii1iIiI111Ii ( url ) :
 if 37 - 37: O0O0O - iI11I1II1I1I + IIiIiII11i . OoOO00O % iI11I1II1I1I
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  iII1ii1 ( url )
  if 17 - 17: oO00Oo0o000 + ooOoO0O00 % o0o00Oo0O
  if 65 - 65: O00Oo000ooO0
def iiI11 ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , OOoOO0oo0ooO + 'LocalM3U.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , OOoOO0oo0ooO + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  ooOoOOOoOo0oO0OoO = open ( oOo0oooo00o , 'r' )
  for oo0ooooo00o in ooOoOOOoOo0oO0OoO :
   I1ii11 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oo0ooooo00o )
   for o0O0oo0OO0O , IiIIIIIi in I1ii11 :
    Ooo0OOoOoO0 ( o0O0oo0OO0O , IiIIIIIi , 222 , OOoOO0oo0ooO + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 65 - 65: oO00Oo0o000 + IIiI1I * IIiI1I
def OoOO ( url ) :
 if os . path . exists ( Remote ) :
  IIiII = Oo0o0oooo0O0 ( url )
  o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
  for o0O0oo0OO0O , url in o0O00oOoOO :
   url = ( url ) . strip ( )
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 10 - 10: Ii1I . I11i
  if 75 - 75: o0o00Oo0O * ooOoO0O00 - Ii1i111I / i1IiIIIII % i1IiIIIII / OOooOOo
def i1iIi ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for IiIIIIIi in o0O00oOoOO :
  IiIIIIIi = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + IiIIIIIi
 o0O0oo0OO0O = 'plugin.video.GenieTv'
 if 5 - 5: o0o00Oo0O - IIiI1I / oO00Oo0o000 . I11i
 iIII1iIii ( IiIIIIIi , o0O0oo0OO0O )
 if 9 - 9: ooOoO0O00 - OOooOOo
def IIII ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for IiIIIIIi in o0O00oOoOO :
  IiIIIIIi = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + IiIIIIIi
 o0O0oo0OO0O = 'repository.GenieTv'
 if 57 - 57: iI11I1II1I1I * OoOO00O * IIiI1I / O0O0O
 iIII1iIii ( IiIIIIIi , o0O0oo0OO0O )
 if 46 - 46: OoOO00O
 if 61 - 61: I11i / O0oOO0 - IIiIiII11i
def oOoO0o0Ooo ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , OOoOO0oo0ooO + 'Catagories.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 44 - 44: oO0o * O0O0O
 if 54 - 54: OoOO00O % ooOoO0O00
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
oooOOoo0 = 'https://addons.tvaddons.ag/'
if 79 - 79: ii - O0oOO0 * OoOO00O - IIiIiII11i % OOooOOo * O00Oo000ooO0
def iI1III ( ) :
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 II1iI1iiiI = 'https://addons.tvaddons.ag/search/?keyword=' + Oo0o0O00
 IIiII = Iiii ( II1iI1iiiI )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for IiIIIIIi , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , IiIIIIIi , 10054 , 'https://addons.tvaddons.ag/' + I111i1i1111 , i1iIIi1 , '' )
  if 42 - 42: O0oOO0 + IIiI1I + OoOO00O * Ii1i111I . ooOoO0O00
  if 72 - 72: oOo0O0Ooo + OoOO00O
def IiI1 ( ) :
 IIiII = Iiii ( oooOOoo0 )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  if 'Repositories' in o0O0oo0OO0O :
   pass
  elif 'Services' in o0O0oo0OO0O :
   pass
  elif 'International' in o0O0oo0OO0O :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , IiIIIIIi , 10053 , 'https://addons.tvaddons.ag/' + i11ii1ii11i , i1iIIi1 , '' )
   if 11 - 11: OOooOOo / Ii1i111I
   if 47 - 47: i1IiIIIII . oO00Oo0o000 % IIiIiII11i + I1ii11iIi11i - O0O0O . IIiIiII11i
def Addon ( url ) :
 IIiII = Iiii ( url )
 Ii1Iiiiii = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIiII )
 for url in Ii1Iiiiii :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  if 'Please' in o0O0oo0OO0O :
   pass
  else :
   o0OOOO00O0Oo ( o0O0oo0OO0O , url , 10054 , 'https://addons.tvaddons.ag/' + i11ii1ii11i , i1iIIi1 , '' )
   if 25 - 25: IIiIiII11i % IIiIiII11i - OoOO00O . o0o00Oo0O
   if 79 - 79: O00Oo000ooO0 / oO0o * ii * OOooOOo + oOo0O0Ooo
def O0ooO ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , name + '.zip' )
   try :
    os . remove ( oo0OoOooo )
   except :
    pass
   downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
   O0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print O0ooOO
   print '======================================='
   extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
   oOOOoo00 ( )
   if 40 - 40: I11i . I11i * Ii
def iIII1iIii ( url , name ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 oo0OoOooo = os . path . join ( o0iiiI1I1iIIIi1 , name + '.zip' )
 try :
  os . remove ( oo0OoOooo )
 except :
  pass
 downloader . download ( url , oo0OoOooo , Oo0oO0ooo )
 O0ooOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print O0ooOO
 print '======================================='
 extract . all ( oo0OoOooo , O0ooOO , Oo0oO0ooo )
 oOOOoo00 ( )
 if 44 - 44: I11i
def oOOOoo00 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 80 - 80: Ii1I + Ii1i111I - O0oOO0 - I11i % OoOO00O
 if 85 - 85: oO00Oo0o000
def O0OoO00OoOO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 1007 , I111i1i1111 )
def OOoOo0ooOoo ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , I111i1i1111 )
  if 68 - 68: i1IiIIIII + OoOO00O
  if 58 - 58: O00Oo000ooO0 * OoOO00O . ooOoO0O00
def i11I1iiii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , O00OoOO0oo0 , iIi11i1 , name in o0O00oOoOO :
  if 'http' in url :
   if '.php' in url :
    i11I1I = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
    for oo0ooooo00o in i11I1I :
     if oo0ooooo00o == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iI1i1iIi1iiII ( name , url , 1016 , iconimage , iIi11i1 , O00OoOO0oo0 )
   else :
    if 'youtube' in url :
     i11I1I = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
     for oo0ooooo00o in i11I1I :
      if oo0ooooo00o == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0Oo0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iIi11i1 , O00OoOO0oo0 )
    else :
     i11I1I = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
     for oo0ooooo00o in i11I1I :
      if oo0ooooo00o == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0Oo0 ( name , url , 222 , iconimage , iIi11i1 , O00OoOO0oo0 )
     oO00OOoO00 ( 'movies' , 'INFO' )
  else :
   i1iIioOO00OOOoO0o ( url , iconimage , name )
   if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % O0O0O + oOo0O0Ooo % O0oOO0 / OoOO00O
 else :
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , I111i1i1111 , name in o0O00oOoOO :
   if 'http' in url :
    if '.php' in url :
     iiI11ii1I1 ( name , url , 1016 , I111i1i1111 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      Ooo0OOoOoO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111i1i1111 )
     else :
      i11I1I = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
      for oo0ooooo00o in i11I1I :
       if oo0ooooo00o == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      Ooo0OOoOoO0 ( name , url , 222 , I111i1i1111 )
      oO00OOoO00 ( 'movies' , 'INFO' )
   else :
    i1iIioOO00OOOoO0o ( url , I111i1i1111 , name )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 36 - 36: OOooOOo . Ii
def i1iIioOO00OOOoO0o ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oO00O0o0oOOO = ( url ) . replace ( ooooOOoOoO0oO00O , 'http' ) . replace ( iIIIII11 , '.com' ) ;
 ooooOoo00 = ( oO00O0o0oOOO ) . replace ( ooo0O , 'a' ) . replace ( i1i1Ii1IiIII , 'b' ) . replace ( I1IIii11 , 'c' ) . replace ( iI1oOoo , 'd' ) . replace ( iIIi1iii1 , 'e' ) . replace ( oooo , 'f' ) ;
 IIIIii1111i1 = ( ooooOoo00 ) . replace ( OOOOOoO00oo00 , 'g' ) . replace ( I1o0 , 'h' ) . replace ( ooooOOO0 , 'i' ) . replace ( ooooOoOooo00Oo , 'j' ) . replace ( I1I1 , 'k' ) . replace ( O0OOO0ooO00o , 'l' ) ;
 iiI1ii1 = ( IIIIii1111i1 ) . replace ( I1oOOoo0 , 'm' ) . replace ( II1OOO , 'n' ) . replace ( iiIII1I11iii , 'o' ) . replace ( ooIii , 'p' ) . replace ( o0OO00oOOO0o0 , 'q' ) . replace ( iiii , 'r' ) ;
 oOOOO = ( iiI1ii1 ) . replace ( OoOOoo0 , 's' ) . replace ( o00O0o00oo , 't' ) . replace ( oo0OOO0OOoOO , 'u' ) . replace ( oOoO , 'v' ) . replace ( II1i1 , 'w' ) . replace ( o0o0oo0OOo0O0 , 'x' ) ;
 iIIiiII11i1I1 = ( oOOOO ) . replace ( Ii111Ii1iiIi1 , 'y' ) . replace ( OOI11i1IIi1i1 , 'z' ) . replace ( OoooOO0 , '.' ) . replace ( oo0OoO , '(' ) . replace ( o00o0 , ')' ) . replace ( OOoOo0O0 , '/' ) ;
 I11i1iiiiIIIi = ( iIIiiII11i1I1 ) . replace ( Oo0ooooO0O0oo , '1' ) . replace ( iIiiII , '2' ) . replace ( Ii11Ii1 , '3' ) . replace ( I11i1I1 , '4' ) . replace ( ooOooO , '5' ) . replace ( Ii1i , '6' ) ;
 IIIO0oo0OOO0O0 = ( I11i1iiiiIIIi ) . replace ( IIIiI1iIIII , '7' ) . replace ( o0oo00OOOo , '8' ) . replace ( oo0oO , '9' ) . replace ( i1i1IIi , '0' ) . replace ( I1Iiii , ':' ) . replace ( I1I1Iii1Iiii , '%' ) ;
 url = ( IIIO0oo0OOO0O0 ) . replace ( O000Oo00 , '-' ) . replace ( I1IiiiiI1i1I , '_' ) ;
 Ooo0OOoOoO0 ( name , url , 222 , iconimage ) ;
 if 97 - 97: O00Oo000ooO0 - Ii1i111I / IIiIiII11i
 if 26 - 26: IIiI1I + o0o00Oo0O * IIiI1I . ooOoO0O00
def Ii11I1II1 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1007 , I111i1i1111 )
def I11Ii1I11 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , I111i1i1111 )
  if 43 - 43: oOo0O0Ooo % O00Oo000ooO0 % Ii1I
def OO00oOo0o00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0O0o = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0o )
 if 45 - 45: OOooOOo
 if 100 - 100: ooOoO0O00 % OoOO00O
def oO000O ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  if '-dir-' in o0O0oo0OO0O :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , i11ii1ii11i )
  else :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' , url , 1006 , i11ii1ii11i )
   if 62 - 62: ooOoO0O00 * iI11I1II1I1I % O0O0O % OOooOOo / ii
def iI1111iiI1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 OOO0ooO0Oo0 = ( 'http://afewbitsmore.com/' )
 o0O00oOoOO = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if '[To Parent Directory]' in o0O0oo0OO0O :
   o0O0oo0OO0O = 'HOME'
   pass
  elif 'HOME' in o0O0oo0OO0O :
   pass
  elif '.m3u' in o0O0oo0OO0O :
   iiI11ii1I1 ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , OOO0ooO0Oo0 + url , 2002 , OOoOO0oo0ooO + 'music.png' )
  elif '.mp3' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OOO0ooO0Oo0 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  elif '.m4a' in o0O0oo0OO0O :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OOO0ooO0Oo0 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) , OOO0ooO0Oo0 + url , 1012 , OOoOO0oo0ooO + 'music.png' )
def oo000oOo0OoO0 ( url ) :
 IIiII = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for i11ii1ii11i , o0O0oo0OO0O , url in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , OOoOO0oo0ooO + 'music.png' )
  if 28 - 28: O0oOO0 % ooOoO0O00 / O0O0O
def iiI1 ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 OOO0ooO0Oo0 = url
 o0O00oOoOO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  if '.mp3' in o0O0oo0OO0O :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   iiI11ii1I1 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '/' , '' ) , OOO0ooO0Oo0 + url , 1011 , OOoOO0oo0ooO + 'music.png' )
def II1II111 ( ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for IiIIIIIi , i11ii1ii11i , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , ( 'http://www.cyn.net/music/' + IiIIIIIi ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + i11ii1ii11i ) . replace ( ' ' , '%20' ) )
def OoO00oO0o00 ( url , img ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 i1I1IiiIi1i = url
 img = img
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i1I1IiiIi1i + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 25 - 25: O0oOO0 . I11i % oOo0O0Ooo + IIiI1I
def OOO0OOoOOO ( url ) :
 OoO000O0Oo = Oo0o0oooo0O0 ( url )
 i1I1IiiIi1i = url
 o0O00oOoOO = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , o0O0oo0OO0O in o0O00oOoOO :
  if '[VID]' in type :
   Ooo0OOoOoO0 ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i1I1IiiIi1i + url , 222 , OOoOO0oo0ooO + 'music.png' )
  if '[DIR]' in type :
   OOO0OOoOOO ( i1I1IiiIi1i + url )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: Ii1I - o0o00Oo0O
 if 35 - 35: i1IiIIIII . Ii1i111I . oO00Oo0o000 - Ii1i111I % Ii1i111I + oO00Oo0o000
def oO0oO00 ( ) :
 iIiiiIIiii = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 O0oOOoooOO0O = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo0o0O00 = O0oOOoooOO0O . lower ( )
 IiIIIIIi = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i1I1IiiIi1i = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 I1i1iiiI1 = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 15 - 15: oOo0O0Ooo % O0O0O . I1ii11iIi11i % iI11I1II1I1I
 IIiII = i1I1iI ( IiIIIIIi )
 o0ooOooo000oOO = i1I1iI ( i1I1IiiIi1i )
 Oo0oOOo = i1I1iI ( I1i1iiiI1 )
 if 98 - 98: Ii1i111I - ooOoO0O00 % OoOO00O - ii
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for o0O0oo0OO0O in o0O00oOoOO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIIIIIi + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 19 - 19: iI11I1II1I1I + oO00Oo0o000 . oO00Oo0o000 - I1ii11iIi11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for o0O0oo0OO0O in iIIi1i1 :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( i1I1IiiIi1i + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 41 - 41: oOo0O0Ooo . I1ii11iIi11i . O00Oo000ooO0 % ii + oO0o
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  oOo00OooO0oO = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oo0oOOo )
  for o0O0oo0OO0O in oOo00OooO0oO :
   if O0oOOoooOO0O in o0O0oo0OO0O . lower ( ) :
    iiI11ii1I1 ( ( o0O0oo0OO0O + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1i1iiiI1 + o0O0oo0OO0O ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 23 - 23: oOo0O0Ooo - I11i % O0O0O . o0o00Oo0O * ii + O0oOO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: I1ii11iIi11i
    if 3 - 3: O00Oo000ooO0 - ii * ii - oOo0O0Ooo / oO00Oo0o000 * Ii1I
    if 58 - 58: O00Oo000ooO0 % iI11I1II1I1I / Ii % I11i . oO00Oo0o000 * IIiI1I
    if 32 - 32: ii + I11i
    if 91 - 91: O0oOO0 - oO00Oo0o000 * oO00Oo0o000
    if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
I1oOOoo0 = '{SF},' ; II1OOO = '{IF},' ; iiIII1I11iii = '{PW},' ; Ii11Ii1 = '{AM},' ; ooIii = '{GF},' ; o0OO00oOOO0o0 = '{DD},' ; iiii = '{UO},' ; OoOOoo0 = '{LE},' ; oo0OOO0OOoOO = '{ZY},' ; oOoO = '{UE},' ; II1i1 = '{PE},' ; o0o0oo0OOo0O0 = '{JE},' ; Ii111Ii1iiIi1 = '{TH},' ; OOI11i1IIi1i1 = '{LK},'
if 24 - 24: oO0o / oO00Oo0o000 + IIiI1I * Ii1i111I * IIiI1I
if 10 - 10: oOo0O0Ooo - Ii1I - I1ii11iIi11i - I11i
def ii1IIii ( ) :
 OoO000O0Oo = Iiii ( 'http://www.iwatchseries.me/tv-list/' )
 o0O00oOoOO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 8021 , OOoOO0oo0ooO + 'iwatch.png' )
def Ii1111Ii1 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O , OoOo00o0OO in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O + OoOo00o0OO , url , 8022 , OOoOO0oo0ooO + 'iwatch.png' )
def III1Iiii1i11 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OO00 ( url )
def OO00 ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 iIIi1i1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 oOo00OooO0oO = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( 'VidSpot - ' + o0O0oo0OO0O , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for url in iIIi1i1 :
  Ooo0OOoOoO0 ( 'VodLocker' , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for o0O0oo0OO0O , url in oOo00OooO0oO :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   Ooo0OOoOoO0 ( 'TheVideo - ' + o0O0oo0OO0O , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
   if 10 - 10: Ii1i111I * ooOoO0O00 . O0O0O / oO00Oo0o000 . i1IiIIIII / oO00Oo0o000
def i1111I1iii1 ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o0O00oOoOO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1021 , OOoOO0oo0ooO + 'anime.png' )
  if 89 - 89: O00Oo000ooO0 - ooOoO0O00 - O00Oo000ooO0
  if 74 - 74: oO0o % oO0o
def IIIII1IIiIi ( ) :
 OoO000O0Oo = Iiii ( 'http://www.animetoon.org/cartoon' )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for IiIIIIIi , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , IiIIIIIi , 1002 , OOoOO0oo0ooO + 'anime.png' )
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * i1IiIIIII
  if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
  if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % OoOO00O
def oOoOo00oo ( url ) :
 OoO000O0Oo = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for i11ii1ii11i in iIIi1i1 :
  I111Ii = i11ii1ii11i
 oOo00OooO0oO = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in oOo00OooO0oO :
  iiI11ii1I1 ( 'NEXT PAGE' , url , 1002 , OOoOO0oo0ooO + 'Next.png' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , o0O0oo0OO0O in o0O00oOoOO :
  iiI11ii1I1 ( o0O0oo0OO0O , url , 1003 , I111Ii )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def II11IiIIiiiii ( url , IMAGE ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OoO000O0Oo )
 for o0O0oo0OO0O , url in o0O00oOoOO :
  print o0O0oo0OO0O + '     ' + url
  if 'easy' in url :
   oooOOo0o0OOO ( url )
  elif 'playpanda' in url :
   oooOOo0o0OOO ( url )
   if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + OoOO00O % ooOoO0O00 . O0O0O
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooOOo0o0OOO ( url ) :
 OoO000O0Oo = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in o0O00oOoOO :
  Ooo0OOoOoO0 ( 'STREAM' , url , 222 , OOoOO0oo0ooO + 'anime.png' )
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
def Oo0o0oooo0O0 ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 55 - 55: IIiI1I + I1ii11iIi11i
def o0OOOoO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iI111i11iI1 = ( '%s%s' % ( III1ii , url ) )
 O00oO = Oo0o0oooo0O0 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , I111i1i1111 , o0O0oo0OO0O in o0O00oOoOO :
  Ooo0OOoOoO0 ( '%s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + o0O0oo0OO0O + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I111i1i1111 )
  if 73 - 73: ii / ii
def iII1ii1 ( url ) :
 if 88 - 88: oO00Oo0o000 - OoOO00O - O0O0O + ooOoO0O00
 ii11IiiIi = open ( oOoOooOo0o0 , "a" )
 ii11IiiIi . write ( 'url="' + url + '"\n' )
 ii11IiiIi . close
 if 39 - 39: oO0o / I1ii11iIi11i % IIiIiII11i % Ii1i111I
 IiIii1ii = xbmc . Player ( Oooo00OOo ( ) )
 import urlresolver
 try : IiIii1ii . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( o0O0oo0OO0O ) )
 IiIii1ii = xbmc . Player ( Oooo00OOo ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IiIii1ii . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 57 - 57: oO0o
def oO0o0o ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % o0O0oo0OO0O )
 xbmc . sleep ( 1 )
 IiIii1ii = xbmc . Player ( Oooo00OOo ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % o0O0oo0OO0O )
 xbmc . sleep ( 1 )
 IiIii1ii . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 94 - 94: O00Oo000ooO0 % OoOO00O % Ii . O00Oo000ooO0
def O00OO ( url ) :
 IiIii1ii = xbmc . Player ( Oooo00OOo ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IiIii1ii . play ( url ) . strip ( )
 except : pass
 if 6 - 6: oO00Oo0o000 / ii / IIiI1I / oO00Oo0o000 + IIiI1I - OOooOOo
 if 71 - 71: Ii1I . oO00Oo0o000
def Oooo00OOo ( ) :
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
def iiI11ii1I1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiiIIiiii11 . addContextMenuItems ( O0oooOo0000o0 )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = True )
 return Ii1IIIII
 if 95 - 95: O0O0O
def iIIIIiiIii ( name , url , mode , iconimage , fanart , description ) :
 if 80 - 80: O00Oo000ooO0
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiIIiiii11 . setProperty ( "Fanart_Image" , fanart )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = True )
 return Ii1IIIII
 if 42 - 42: ii * IIiIiII11i
def Ooo0OOoOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiiIIiiii11 . addContextMenuItems ( O0oooOo0000o0 )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = False )
 return Ii1IIIII
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
   try : OOO = open ( announce ) ; IIIIIiII1 = OOO . read ( )
   except : IIIIIiII1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIIIIiII1 ) )
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
def oOOOoo00 ( ) :
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
def O00OIIIIIi1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0oIi1iiiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 88 - 88: OoOO00O / Ii % OOooOOo % i1IiIIIII
def OOI1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oooO00oOOooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IIIii111i ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + O000OoOO0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: oOo0O0Ooo / OOooOOo
def OO00OO0 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + Ooii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 28 - 28: oO0o
def OOOOoOooo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + i11iI1111ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 89 - 89: Ii / o0o00Oo0O - ooOoO0O00 % I1ii11iIi11i + Ii
def ii1IO0oo00o000 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + II1111iiI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - OoOO00O * iI11I1II1I1I
def OO0ooo0OOO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + O00oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 75 - 75: O0oOO0 - IIiI1I % IIiI1I + O0oOO0 * I11i - Ii1I
def I111Ii1I1I1iI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + IIIOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 11 - 11: o0o00Oo0O
def o0Oo0o ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + i1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 42 , oOOO00o000o , iIi11i1 , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
def iIIiIiii1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + oo0OO0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for o0O0oo0OO0O , url , oOOO00o000o , iIi11i1 , oOoO00oo0O in o0O00oOoOO :
  o0OOOO00O0Oo ( o0O0oo0OO0O , url , 5 , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , oOoO00oo0O )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 4 - 4: OOooOOo * o0o00Oo0O - Ii1i111I
 if 72 - 72: Ii1i111I + O0oOO0 / oOo0O0Ooo . O00Oo000ooO0 % oO0o / Ii
 if 13 - 13: oO00Oo0o000 % I11i + i1IiIIIII + oO00Oo0o000 + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: IIiI1I
 if 20 - 20: OoOO00O . oO00Oo0o000 % OoOO00O
 if 5 - 5: i1IiIIIII + IIiI1I
 if 23 - 23: oO00Oo0o000 % iI11I1II1I1I . Ii1i111I
 if 95 - 95: I1ii11iIi11i + Ii % i1IiIIIII - O0O0O
def iIIii ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ii1iI1II11ii , oO0 , i1iI in os . walk ( oOOoO0 ) :
     o000oo = 0
     o000oo += len ( i1iI )
     if o000oo > 0 :
      for OOO in i1iI :
       os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
  O0Ooo0o = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( O0Ooo0o )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 42 - 42: iI11I1II1I1I / Ii1i111I . o0o00Oo0O . OoOO00O
 if 12 - 12: Ii - iI11I1II1I1I * O00Oo000ooO0 * IIiI1I
 if 19 - 19: o0o00Oo0O + O0O0O + I11i
 if 81 - 81: iI11I1II1I1I
 if 51 - 51: I11i . Ii1I * OoOO00O / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % oO00Oo0o000 % O0O0O + Ii1i111I * O0O0O . OoOO00O
 if 89 - 89: ii % IIiIiII11i - oO0o % Ii
 if 7 - 7: O00Oo000ooO0
 if 15 - 15: I1ii11iIi11i + IIiI1I + oOo0O0Ooo * I11i
def iII1111IIIIiI ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 IiiiiIi11 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( IiiiiIi11 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( IiiiiIi11 ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 57 - 57: IIiI1I / oO0o - IIiIiII11i
   if 43 - 43: O00Oo000ooO0 % OoOO00O . i1IiIIIII / I1ii11iIi11i
   if o000oo > 0 :
    if 55 - 55: Ii1I % ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: ooOoO0O00 - IIiI1I % O0O0O / ooOoO0O00 + IIiIiII11i + Ii1I
     for OOO in i1iI :
      try :
       os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
      except :
       pass
     for ooO0oO00O0o in oO0 :
      try :
       shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      except :
       pass
       if 54 - 54: O0O0O
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  I1ii11I1IiI = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 20 - 20: oO0o
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( I1ii11I1IiI ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 99 - 99: I1ii11iIi11i + ii . IIiI1I + o0o00Oo0O
   if o000oo > 0 :
    if 85 - 85: IIiIiII11i - OoOO00O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( o000oo ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 93 - 93: O00Oo000ooO0 / Ii - O0O0O + oO0o / ooOoO0O00
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
   else :
    pass
  OO0oOOo0o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 46 - 46: ii
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( OO0oOOo0o ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 23 - 23: ooOoO0O00
   if o000oo > 0 :
    if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Ii1i111I . oO0o
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( o000oo ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 74 - 74: I1ii11iIi11i - IIiIiII11i - O00Oo000ooO0
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 50 - 50: oOo0O0Ooo - O0O0O + O0O0O * Ii1i111I + O0O0O
   else :
    pass
    if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
    if 30 - 30: OOooOOo - Ii
    if 94 - 94: OOooOOo % IIiI1I
    if 39 - 39: OOooOOo + oO00Oo0o000 % o0o00Oo0O
 i1Ii1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( i1Ii1I ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( i1Ii1I ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 60 - 60: O0oOO0 * OoOO00O + oO00Oo0o000 . i1IiIIIII . o0o00Oo0O
   if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
   if o000oo > 0 :
    if 66 - 66: oO00Oo0o000 * I11i / O00Oo000ooO0 * IIiI1I / ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 72 - 72: iI11I1II1I1I
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 82 - 82: OOooOOo . OoOO00O
   else :
    pass
    if 73 - 73: oO00Oo0o000
    if 25 - 25: O00Oo000ooO0
 OOii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( OOii ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( OOii ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 14 - 14: Ii1I * ooOoO0O00 / iI11I1II1I1I / O0O0O / o0o00Oo0O % I1ii11iIi11i
   if 1 - 1: i1IiIIIII % I11i + oO0o
   if o000oo > 0 :
    if 53 - 53: I1ii11iIi11i * Ii1i111I - OoOO00O % oO0o - OOooOOo - IIiI1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: IIiIiII11i + oO0o - I1ii11iIi11i + oOo0O0Ooo
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 20 - 20: oO0o
   else :
    pass
    if 64 - 64: O00Oo000ooO0
    if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
 oo000o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( oo000o ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( oo000o ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 6 - 6: i1IiIIIII + Ii1I + I1ii11iIi11i
   if 52 - 52: O00Oo000ooO0 * I1ii11iIi11i + ii
   if o000oo > 0 :
    if 93 - 93: O0oOO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: Ii / I11i / oO0o . OOooOOo % O0O0O
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 29 - 29: I11i
   else :
    pass
    if 13 - 13: OoOO00O + OoOO00O . Ii1i111I
    if 57 - 57: O0oOO0
    if 94 - 94: oO0o - IIiIiII11i % iI11I1II1I1I
 oOoo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( oOoo0o ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( oOoo0o ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 57 - 57: ii % IIiIiII11i - oO00Oo0o000
   if 1 - 1: O00Oo000ooO0
   if o000oo > 0 :
    if 27 - 27: OOooOOo . oO00Oo0o000 * OOooOOo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 8 - 8: O0O0O * O00Oo000ooO0 * O0oOO0
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 26 - 26: IIiI1I * i1IiIIIII / i1IiIIIII - IIiI1I
   else :
    pass
    if 59 - 59: OoOO00O % IIiI1I / IIiIiII11i + oOo0O0Ooo * O0oOO0
    if 100 - 100: Ii1I
 oO0o0OooOO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( oO0o0OooOO0 ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 42 - 42: ii . OOooOOo
   if 93 - 93: oOo0O0Ooo
   if o000oo > 0 :
    if 89 - 89: ii % Ii + oO00Oo0o000
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 12 - 12: OOooOOo * O0oOO0
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 59 - 59: IIiIiII11i * ii - ii
   else :
    pass
    if 33 - 33: o0o00Oo0O . Ii % I11i
    if 50 - 50: O0oOO0
 Oooo0O00OOo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( Oooo0O00OOo0o ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 4 - 4: O0O0O * ii % I1ii11iIi11i / O0oOO0
   if 11 - 11: I11i - IIiIiII11i % O0O0O . IIiIiII11i
   if o000oo > 0 :
    if 65 - 65: O0O0O . Ii % i1IiIIIII * IIiI1I % I1ii11iIi11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 51 - 51: oO0o % IIiI1I
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
   else :
    pass
    if 8 - 8: Ii1I % oO0o % O0O0O . Ii1I * Ii1I
    if 94 - 94: Ii + ii
 i1iII1iii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( i1iII1iii ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 97 - 97: oO00Oo0o000 / i1IiIIIII - Ii
   if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * O0oOO0 - Ii1i111I * oO0o
   if o000oo > 0 :
    if 78 - 78: IIiI1I % Ii + IIiI1I + I11i
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 22 - 22: Ii1i111I - I11i
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 54 - 54: O0O0O * oO0o - IIiI1I * Ii1i111I + I11i - OoOO00O
   else :
    pass
    if 5 - 5: O0O0O + OoOO00O
    if 48 - 48: oO00Oo0o000 * ooOoO0O00 - Ii1I / oOo0O0Ooo + Ii - ooOoO0O00
 oOo0Oi1i1III11IiIi = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( oOo0Oi1i1III11IiIi ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 99 - 99: IIiIiII11i - iI11I1II1I1I
   if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % oO00Oo0o000 - iI11I1II1I1I . Ii1i111I
   if o000oo > 0 :
    if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . oO00Oo0o000
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 31 - 31: o0o00Oo0O - O00Oo000ooO0 * Ii * ooOoO0O00
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 78 - 78: O0oOO0 * OOooOOo . OoOO00O . OOooOOo % iI11I1II1I1I
   else :
    pass
    if 67 - 67: OoOO00O . I1ii11iIi11i
    if 39 - 39: Ii1i111I * oO00Oo0o000
 O0oOO0o00OO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( O0oOO0o00OO ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 39 - 39: I11i . ooOoO0O00 % O0O0O / Ii1i111I % o0o00Oo0O
   if 100 - 100: oO00Oo0o000 - OOooOOo
   if o000oo > 0 :
    if 78 - 78: ii - OOooOOo . Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 36 - 36: O0O0O * IIiI1I + O00Oo000ooO0 * IIiI1I . Ii1I - iI11I1II1I1I
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 14 - 14: Ii1i111I * O0O0O + Ii
   else :
    pass
    if 84 - 84: IIiI1I / IIiIiII11i
    if 86 - 86: oOo0O0Ooo
 oOoOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( oOoOO ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 8 - 8: oOo0O0Ooo . Ii / oOo0O0Ooo * Ii1i111I
   if 87 - 87: O00Oo000ooO0 - o0o00Oo0O + oOo0O0Ooo / ii * IIiI1I / ooOoO0O00
   if o000oo > 0 :
    if 28 - 28: I11i - IIiI1I * Ii1I - IIiIiII11i % IIiIiII11i - O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 76 - 76: oO00Oo0o000
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 43 - 43: o0o00Oo0O / oO00Oo0o000 . iI11I1II1I1I - OOooOOo
   else :
    pass
    if 47 - 47: IIiIiII11i - Ii1I - OoOO00O
    if 9 - 9: Ii1I - O00Oo000ooO0
 o0o0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( oO0o0OooOO0 ) == True :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( o0o0 ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 87 - 87: Ii * IIiIiII11i - OoOO00O % ii
   if 55 - 55: ooOoO0O00
   if o000oo > 0 :
    if 67 - 67: oOo0O0Ooo - oO0o
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 60 - 60: ooOoO0O00 / iI11I1II1I1I * O0O0O + O0oOO0 + ii + IIiIiII11i
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
      if 13 - 13: iI11I1II1I1I - i1IiIIIII
   else :
    pass
    if 14 - 14: O0oOO0
    if 75 - 75: iI11I1II1I1I % O0oOO0 / i1IiIIIII - IIiI1I % Ii
    if 11 - 11: Ii1i111I . OoOO00O
 oO0OoO = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   i1II1IiIi111 = os . path . join ( oO0OoO , "cache.db" )
   os . unlink ( i1II1IiIi111 )
   if 53 - 53: IIiIiII11i . IIiIiII11i
 except :
  pass
  if 18 - 18: OoOO00O + OOooOOo . ooOoO0O00 / O00Oo000ooO0 / IIiI1I
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: O0oOO0 + O0O0O - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: O00Oo000ooO0
 if 52 - 52: o0o00Oo0O + O0oOO0
 if 11 - 11: ooOoO0O00 / oO00Oo0o000 * Ii1I * oO00Oo0o000 * O0oOO0 - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . OoOO00O
 if 26 - 26: O0O0O - O0oOO0 % I1ii11iIi11i - O0O0O + O00Oo000ooO0
 if 33 - 33: OoOO00O + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * O00Oo000ooO0
def ii11Ii1iii1I1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 Oo0OooO00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( Oo0OooO00oOo ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 17 - 17: oO00Oo0o000 % O0oOO0 + O00Oo000ooO0 % I11i . ooOoO0O00
   if 58 - 58: i1IiIIIII
   if o000oo > 0 :
    if 94 - 94: ii - O0oOO0 % i1IiIIIII - IIiI1I / ooOoO0O00
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: ii % IIiIiII11i
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
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
 if 7 - 7: Ii - Ii1i111I % I1ii11iIi11i
 if 76 - 76: oO0o * IIiI1I % I1ii11iIi11i . Ii / ii
 if 85 - 85: ii . oO0o . oO0o
 if 70 - 70: Ii1i111I
 if 72 - 72: oO00Oo0o000 - O0oOO0 - oOo0O0Ooo - IIiI1I + i1IiIIIII - ooOoO0O00
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: IIiI1I % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * O0O0O + IIiI1I % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % O00Oo000ooO0 . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
def Ii1iIi111i1i1 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 Oo0OooO00oOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1iI1II11ii , oO0 , i1iI in os . walk ( Oo0OooO00oOo ) :
   o000oo = 0
   o000oo += len ( i1iI )
   if 55 - 55: OOooOOo . iI11I1II1I1I * i1IiIIIII % iI11I1II1I1I . oO0o
   if 43 - 43: OoOO00O . i1IiIIIII + oOo0O0Ooo * Ii
   if o000oo > 0 :
    if 2 - 2: i1IiIIIII
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( o000oo ) + " files found" , "Do you want to delete them?" ) :
     if 3 - 3: oOo0O0Ooo . IIiI1I % o0o00Oo0O - O0oOO0 / o0o00Oo0O
     for OOO in i1iI :
      os . unlink ( os . path . join ( ii1iI1II11ii , OOO ) )
     for ooO0oO00O0o in oO0 :
      shutil . rmtree ( os . path . join ( ii1iI1II11ii , ooO0oO00O0o ) )
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
 iII1111IIIIiI ( url )
 return
 if 79 - 79: OoOO00O + O0O0O % O0oOO0 % oOo0O0Ooo
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: IIiI1I . O0O0O / I1ii11iIi11i . oO0o . Ii
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: IIiI1I + I1ii11iIi11i % Ii1i111I . O0O0O
 if 6 - 6: O00Oo000ooO0 + Ii1I
 if 62 - 62: O0O0O . oO00Oo0o000 - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
def oo0O0OO0Oooo ( url , name ) :
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 I1Iii1 = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml.bak' )
 if os . path . exists ( I1Iii1 ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml' )
   try :
    os . remove ( IiiI11Iii )
    print '=== GenieTv - REMOVING    ' + str ( IiiI11Iii ) + '    ==='
   except :
    pass
   O00oO = i1 . http_GET ( url ) . content
   o0O0Oo00 = open ( IiiI11Iii , "w" )
   o0O0Oo00 . write ( O00oO )
   o0O0Oo00 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IiiI11Iii ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml' )
  try :
   os . remove ( IiiI11Iii )
   print '=== GenieTv - REMOVING    ' + str ( IiiI11Iii ) + '    ==='
  except :
   pass
  O00oO = i1 . http_GET ( url ) . content
  o0O0Oo00 = open ( IiiI11Iii , "w" )
  o0O0Oo00 . write ( O00oO )
  o0O0Oo00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiiI11Iii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 9 - 9: IIiIiII11i % I1ii11iIi11i * OoOO00O + O00Oo000ooO0 % oO0o . ooOoO0O00
def oo00ooOOoo ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml' )
 try :
  o0O0Oo00 = open ( IiiI11Iii ) . read ( )
  if 'zero' in o0O0Oo00 :
   name = '0CACHE'
  elif 'tuxen' in o0O0Oo00 :
   name = 'TUXENS'
  elif 'muckys' in o0O0Oo00 :
   name = 'MUCKYS'
  elif 'p2p1' in o0O0Oo00 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in o0O0Oo00 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in o0O0Oo00 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 58 - 58: oO00Oo0o000 - Ii1i111I % Ii1I + ii - O0oOO0
def I1i1i1i ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'advancedsettings.xml' )
 try :
  os . remove ( IiiI11Iii )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IiiI11Iii ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 86 - 86: ooOoO0O00 * OoOO00O
 if 36 - 36: oOo0O0Ooo / I1ii11iIi11i % iI11I1II1I1I / o0o00Oo0O . Ii1I
 if 53 - 53: I11i % ii - O0O0O - ooOoO0O00 / oO0o
 if 33 - 33: O00Oo000ooO0 * Ii1i111I
 if 96 - 96: I11i - oOo0O0Ooo % OOooOOo + oO0o - O00Oo000ooO0 - O00Oo000ooO0
 if 2 - 2: O0oOO0 % Ii
 if 11 - 11: iI11I1II1I1I . oO00Oo0o000 - I1ii11iIi11i / Ii1i111I + IIiIiII11i
 if 29 - 29: Ii1i111I . Ii + ooOoO0O00 - OoOO00O + o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
def I1Ii11IIi ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o0O00oOoOO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for ii111iI , II1IIII1i1i , IiIiI1i1ii , iiii1I1IiI in o0O00oOoOO :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ii111iI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IiIiI1i1ii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iiii1I1IiI )
  inc = inc + 1
  if 49 - 49: Ii1I + O0O0O * IIiI1I * O0oOO0 / oOo0O0Ooo . Ii1I
  if 80 - 80: oOo0O0Ooo % O00Oo000ooO0 / Ii1i111I * oO0o - O0O0O / O0O0O
  if 13 - 13: I1ii11iIi11i
  if 70 - 70: IIiI1I
  if 51 - 51: o0o00Oo0O - Ii1I / Ii1i111I * IIiIiII11i + oO0o % Ii1I
  if 58 - 58: O0O0O + O00Oo000ooO0 % IIiI1I - OoOO00O - i1IiIIIII % OoOO00O
  if 86 - 86: I11i
  if 15 - 15: O0O0O - iI11I1II1I1I - IIiIiII11i - O00Oo000ooO0 % Ii1I
  if 80 - 80: O00Oo000ooO0 * IIiI1I . ooOoO0O00 % OoOO00O % Ii1I + O0oOO0
def IIII1IiiI ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'addons2.ini' )
  O00oO = i1 . http_GET ( url ) . content
  o0O0Oo00 = open ( IiiI11Iii , "w" )
  o0O0Oo00 . write ( O00oO )
  o0O0Oo00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiiI11Iii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 100 - 100: oOo0O0Ooo - i1IiIIIII
def OOOOo0ooOOO0 ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  o0iiiI1I1iIIIi1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IiiI11Iii = os . path . join ( o0iiiI1I1iIIIi1 , 'settings.xml' )
  O00oO = i1 . http_GET ( url ) . content
  o0O0Oo00 = open ( IiiI11Iii , "w" )
  o0O0Oo00 . write ( O00oO )
  o0O0Oo00 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiiI11Iii ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 91 - 91: Ii + OoOO00O % OoOO00O + I11i
 if 15 - 15: Ii1I . oOo0O0Ooo - oO00Oo0o000 - ooOoO0O00
def O00 ( ) :
 try :
  OO0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO0o0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    oO0o00o0o0OO0O0 = os . path . join ( OO0o0 , "source.db" )
    os . unlink ( oO0o00o0o0OO0O0 )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 12 - 12: ooOoO0O00 + ii . IIiI1I - Ii % I1ii11iIi11i * o0o00Oo0O
 if 65 - 65: O0O0O
 if 8 - 8: oO0o . O0O0O / Ii1I / oO0o + iI11I1II1I1I
 if 73 - 73: Ii / OOooOOo
 if 45 - 45: Ii1i111I . oO0o
def Iiii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 14 - 14: i1IiIIIII * oOo0O0Ooo - Ii1I
 if 10 - 10: IIiI1I % oO00Oo0o000 * Ii1I * o0o00Oo0O * Ii % oO00Oo0o000
 if 68 - 68: ii * OOooOOo
 if 9 - 9: oO00Oo0o000
 if 36 - 36: oO00Oo0o000 / OOooOOo + OOooOOo * O0oOO0 / i1IiIIIII * o0o00Oo0O
 if 17 - 17: oO0o / O0oOO0 % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def OOo0 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iIiiI11II11 = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iIiiI11II11 :
  o0o0O00O = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; o0o0O00O = xbmc . translatePath ( o0o0O00O ) ;
  oO0oO0OoO00 = os . path . join ( o0o0O00O , ".." , ".." ) ; oO0oO0OoO00 = os . path . abspath ( oO0oO0OoO00 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oO0oO0OoO00 ) ; Oo0ooo00o0O0 = False
  try :
   for ii1iI1II11ii , oO0 , i1iI in os . walk ( oO0oO0OoO00 , topdown = True ) :
    oO0 [ : ] = [ ooO0oO00O0o for ooO0oO00O0o in oO0 if ooO0oO00O0o not in iiIIIII1i1iI ]
    for o0O0oo0OO0O in i1iI :
     try : os . remove ( os . path . join ( ii1iI1II11ii , o0O0oo0OO0O ) )
     except :
      if o0O0oo0OO0O not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0ooo00o0O0 = True
      plugintools . log ( "Error removing " + ii1iI1II11ii + " " + o0O0oo0OO0O )
    for o0O0oo0OO0O in oO0 :
     try : os . rmdir ( os . path . join ( ii1iI1II11ii , o0O0oo0OO0O ) )
     except :
      if o0O0oo0OO0O not in [ "Database" , "userdata" ] : Oo0ooo00o0O0 = True
      plugintools . log ( "Error removing " + ii1iI1II11ii + " " + o0O0oo0OO0O )
   if not Oo0ooo00o0O0 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 IIOO0ooOo0OoOo0 ( )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * OoOO00O + iI11I1II1I1I
 if 80 - 80: I11i . IIiI1I . ii
 if 63 - 63: O0oOO0 . i1IiIIIII
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
  for ooo0oo00O00Oo in range ( len ( OOo0OOo ) ) :
   OOIiI1IIIiI1I1i = { }
   OOIiI1IIIiI1I1i = OOo0OOo [ ooo0oo00O00Oo ] . split ( '=' )
   if ( len ( OOIiI1IIIiI1I1i ) ) == 2 :
    IiIiIIIiI1iII [ OOIiI1IIIiI1I1i [ 0 ] ] = OOIiI1IIIiI1I1i [ 1 ]
    if 84 - 84: OOooOOo - Ii1i111I
 return IiIiIIIiI1iII
 if 80 - 80: Ii % i1IiIIIII - I1ii11iIi11i % i1IiIIIII
O0O0oOo0o0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i1IIII1iii11I = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oOOO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
Iii111111 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OooOO0o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1IiIi11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o0oIi1iiiii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1i1I1i1i1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
oooO00oOOooO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O000OoOO0oO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Ooii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i11iI1111ii1I = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
II1111iiI1II = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O00oOO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IIIOo0O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1ii = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IiiI11i1I = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii11i1IiII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o00O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oOooo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oooOO0OO0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
I11IIiIiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
oo0OO0Oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
III1ii = base64 . decodestring ( 'Q1VOVA==' )
def o0OOOO00O0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiIIiiii11 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0oooOo0000o0 = [ ]
  if showcontext == 'fav' :
   O0oooOo0000o0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   O0oooOo0000o0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiiIIiiii11 . addContextMenuItems ( O0oooOo0000o0 )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = True )
 return Ii1IIIII
 if 96 - 96: Ii - OOooOOo / IIiI1I % ii / iI11I1II1I1I - i1IiIIIII
def OOooOoooOoOo ( name , url , mode , iconimage , fanart , description ) :
 I11II1i11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii1IIIII = True
 iiiIIiiii11 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIIiiii11 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiiIIiiii11 . setProperty ( "Fanart_Image" , fanart )
 Ii1IIIII = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11II1i11 , listitem = iiiIIiiii11 , isFolder = False )
 return Ii1IIIII
 if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . Ii1i111I
 if 59 - 59: IIiI1I . ooOoO0O00
O0Ooo0O0O = o000Oo ( )
IiIIIIIi = None
o0O0oo0OO0O = None
IiI1II11iiI = None
oOOO00o000o = None
iIi11i1 = None
oOoO00oo0O = None
iiii1I1 = None
if 82 - 82: I11i * oO0o / O00Oo000ooO0
if 5 - 5: IIiI1I / O0O0O % O0oOO0 . Ii % OOooOOo + O0O0O
try :
 iiii1I1 = int ( O0Ooo0O0O [ "fav_mode" ] )
except :
 pass
 if 95 - 95: Ii1I
try :
 IiIIIIIi = urllib . unquote_plus ( O0Ooo0O0O [ "url" ] )
except :
 pass
try :
 o0O0oo0OO0O = urllib . unquote_plus ( O0Ooo0O0O [ "name" ] )
except :
 pass
try :
 oOOO00o000o = urllib . unquote_plus ( O0Ooo0O0O [ "iconimage" ] )
except :
 pass
try :
 IiI1II11iiI = int ( O0Ooo0O0O [ "mode" ] )
except :
 pass
try :
 iIi11i1 = urllib . unquote_plus ( O0Ooo0O0O [ "fanart" ] )
except :
 pass
try :
 oOoO00oo0O = urllib . unquote_plus ( O0Ooo0O0O [ "description" ] )
except :
 pass
 if 48 - 48: Ii1i111I
 if 14 - 14: iI11I1II1I1I / I11i * O00Oo000ooO0
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( IiI1II11iiI )
print "URL: " + str ( IiIIIIIi )
print "Name: " + str ( o0O0oo0OO0O )
print "IconImage: " + str ( oOOO00o000o )
if 35 - 35: iI11I1II1I1I
if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
def oO00OOoO00 ( content , viewType ) :
 if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 75 - 75: oOo0O0Ooo - O0oOO0 - oOo0O0Ooo % O0O0O % ii
if oOOO00o000o == None : oOOO00o000o = ii11iIi1I
if iIi11i1 == None : iIi11i1 = i1iIIi1
if IiI1II11iiI == None :
 iiIiI ( )
 if 13 - 13: O0oOO0 * oO0o % iI11I1II1I1I / O00Oo000ooO0 * IIiI1I . I1ii11iIi11i
elif IiI1II11iiI == 1 :
 IIi1I1 ( IiIIIIIi )
 if 23 - 23: O0oOO0 / O00Oo000ooO0 . IIiI1I * OoOO00O
elif IiI1II11iiI == 44 :
 I1i ( IiIIIIIi )
 if 87 - 87: Ii
elif IiI1II11iiI == 2 :
 o0OO000ooOo ( )
 if 34 - 34: ooOoO0O00
elif IiI1II11iiI == 3 :
 Ii1i1i1111 ( )
 if 64 - 64: iI11I1II1I1I / O00Oo000ooO0 / I1ii11iIi11i - Ii1I
elif IiI1II11iiI == 21 :
 iI1Ii11111iIi ( )
 if 100 - 100: O00Oo000ooO0 + ooOoO0O00 * oO0o
elif IiI1II11iiI == 4 :
 iIIIII1iiiiII ( )
 if 64 - 64: O0O0O * Ii . I1ii11iIi11i
elif IiI1II11iiI == 5 :
 ooOo ( IiIIIIIi )
 if 52 - 52: I1ii11iIi11i / O0oOO0 / IIiI1I - I11i / IIiI1I
elif IiI1II11iiI == 6 :
 ii11Ii1iii1I1 ( IiIIIIIi )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif IiI1II11iiI == 7 :
 oo0O0OO0Oooo ( IiIIIIIi , o0O0oo0OO0O )
 if 85 - 85: oOo0O0Ooo
elif IiI1II11iiI == 8 :
 oo00ooOOoo ( IiIIIIIi , o0O0oo0OO0O )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif IiI1II11iiI == 9 :
 FIXREPOSADDONS ( IiIIIIIi )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif IiI1II11iiI == 10 :
 oOOOoo00 ( )
 if 46 - 46: OOooOOo * Ii1i111I / O0O0O + I1ii11iIi11i + O00Oo000ooO0
elif IiI1II11iiI == 11 :
 I1i1i1i ( IiIIIIIi )
 if 95 - 95: I11i - OoOO00O
elif IiI1II11iiI == 12 :
 I1Ii11IIi ( )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif IiI1II11iiI == 13 :
 iIIii ( )
 if 19 - 19: OOooOOo . i1IiIIIII . ii
elif IiI1II11iiI == 14 :
 iII1111IIIIiI ( IiIIIIIi )
 if 79 - 79: i1IiIIIII * O0oOO0 * oOo0O0Ooo * Ii1I / Ii1I
elif IiI1II11iiI == 15 :
 II11i11II ( )
 if 62 - 62: O0oOO0 * OoOO00O % Ii1I - ooOoO0O00 - Ii1I
elif IiI1II11iiI == 16 :
 IIII1IiiI ( IiIIIIIi , o0O0oo0OO0O )
 if 24 - 24: i1IiIIIII
elif IiI1II11iiI == 17 :
 OOOOo0ooOOO0 ( IiIIIIIi , o0O0oo0OO0O )
 if 71 - 71: O00Oo000ooO0 - ooOoO0O00
elif IiI1II11iiI == 18 :
 O00 ( )
 if 56 - 56: OOooOOo + O0O0O
elif IiI1II11iiI == 19 :
 O0O00OOo ( IiIIIIIi )
 if 74 - 74: IIiI1I / oO00Oo0o000 / IIiIiII11i - IIiI1I / O0O0O % Ii1i111I
elif IiI1II11iiI == 40 :
 I1Ii11iiiI ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 19 - 19: O00Oo000ooO0 % ii + ii
elif IiI1II11iiI == 42 :
 o0Oii1111i ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 7 - 7: ooOoO0O00
elif IiI1II11iiI == 43 :
 iiiIi ( IiIIIIIi )
 if 91 - 91: OOooOOo - OOooOOo . O00Oo000ooO0
elif IiI1II11iiI == 20 :
 I1i1111I ( IiIIIIIi )
 if 33 - 33: oO00Oo0o000 - iI11I1II1I1I / OoOO00O % o0o00Oo0O
elif IiI1II11iiI == 22 :
 O00OIIIIIi1 ( IiIIIIIi )
 if 80 - 80: O00Oo000ooO0 % ii - O00Oo000ooO0
elif IiI1II11iiI == 23 :
 OOI1 ( IiIIIIIi )
 if 27 - 27: oO00Oo0o000 - I11i * Ii1I - oOo0O0Ooo
elif IiI1II11iiI == 24 :
 IIIii111i ( IiIIIIIi )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIiI1I . OoOO00O
elif IiI1II11iiI == 25 :
 OO00OO0 ( IiIIIIIi )
 if 100 - 100: IIiIiII11i / oO00Oo0o000 / IIiI1I - Ii1I * iI11I1II1I1I
elif IiI1II11iiI == 26 :
 OOOOoOooo ( IiIIIIIi )
 if 7 - 7: ooOoO0O00 . O00Oo000ooO0 % Ii * Ii1I . Ii1i111I % Ii1I
elif IiI1II11iiI == 27 :
 ii1IO0oo00o000 ( IiIIIIIi )
 if 35 - 35: oOo0O0Ooo
elif IiI1II11iiI == 28 :
 OO0ooo0OOO ( IiIIIIIi )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif IiI1II11iiI == 29 :
 I111Ii1I1I1iI ( IiIIIIIi )
 if 22 - 22: O0oOO0 . Ii . ii . ooOoO0O00
elif IiI1II11iiI == 30 :
 IIioo0OO ( IiIIIIIi )
 if 12 - 12: OOooOOo % i1IiIIIII + O0O0O . o0o00Oo0O % iI11I1II1I1I
elif IiI1II11iiI == 31 :
 o0Oo0o ( IiIIIIIi )
 if 41 - 41: ii
elif IiI1II11iiI == 32 :
 oooo0OO ( )
 if 13 - 13: Ii1i111I + oO00Oo0o000 - oO00Oo0o000 % O0O0O / Ii1i111I
elif IiI1II11iiI == 33 :
 o000 ( )
 if 4 - 4: oOo0O0Ooo + i1IiIIIII - O00Oo000ooO0 + IIiI1I
elif IiI1II11iiI == 35 :
 I1 ( IiIIIIIi )
 if 78 - 78: OoOO00O
elif IiI1II11iiI == 34 :
 IiiiIiiI ( IiIIIIIi )
 if 29 - 29: IIiIiII11i
elif IiI1II11iiI == 36 :
 OOOoO ( IiIIIIIi )
 if 79 - 79: iI11I1II1I1I - Ii + O0oOO0 - IIiIiII11i . iI11I1II1I1I
elif IiI1II11iiI == 37 :
 iiI11iIi ( IiIIIIIi )
 if 84 - 84: I1ii11iIi11i % Ii1i111I * o0o00Oo0O * Ii1i111I
elif IiI1II11iiI == 38 :
 oO00OoOO ( IiIIIIIi )
 if 66 - 66: i1IiIIIII / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0oOO0
elif IiI1II11iiI == 41 :
 OOo0 ( O0Ooo0O0O )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif IiI1II11iiI == 39 :
 iIIiIiii1 ( IiIIIIIi )
 if 37 - 37: ooOoO0O00 * Ii
elif IiI1II11iiI == 45 :
 TEXTS ( )
 if 95 - 95: Ii % oO00Oo0o000 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif IiI1II11iiI == 46 :
 oooooOOo0Oo ( )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / i1IiIIIII / oO00Oo0o000
elif IiI1II11iiI == 47 :
 GEVID ( )
 if 35 - 35: IIiI1I * i1IiIIIII
elif IiI1II11iiI == 48 :
 o00oo0000 ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif IiI1II11iiI == 49 :
 ii1I11 ( )
 if 13 - 13: oO0o * oO00Oo0o000 + I1ii11iIi11i - O00Oo000ooO0
elif IiI1II11iiI == 222 :
 iII1ii1 ( IiIIIIIi )
 if 31 - 31: oO0o
elif IiI1II11iiI == 333 :
 o0OOOoO ( IiIIIIIi )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - oO00Oo0o000 . Ii1I % I1ii11iIi11i . OoOO00O
elif IiI1II11iiI == 1020 :
 i1111I1iii1 ( )
 if 9 - 9: I11i
elif IiI1II11iiI == 1021 :
 ANIMEEP ( )
 if 55 - 55: i1IiIIIII % iI11I1II1I1I + Ii1i111I . O0oOO0
elif IiI1II11iiI == 1022 :
 ANIMEPLAY ( IiIIIIIi )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif IiI1II11iiI == 1001 :
 IIIII1IIiIi ( )
 if 23 - 23: Ii
elif IiI1II11iiI == 1005 :
 Ii11I1II1 ( )
 if 88 - 88: IIiIiII11i - IIiI1I / ii
elif IiI1II11iiI == 1007 :
 I11Ii1I11 ( IiIIIIIi )
 if 71 - 71: Ii1I
elif IiI1II11iiI == 1010 :
 oO000O ( IiIIIIIi )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif IiI1II11iiI == 1011 :
 iiI1 ( IiIIIIIi )
 if 1 - 1: O00Oo000ooO0 % ooOoO0O00
elif IiI1II11iiI == 1012 :
 iI1111iiI1 ( IiIIIIIi )
 if 41 - 41: oO0o * oO0o / IIiI1I + Ii1I . I11i
elif IiI1II11iiI == 1030 :
 II1II111 ( )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / OoOO00O
elif IiI1II11iiI == 1031 :
 OoO00oO0o00 ( IiIIIIIi , oOOO00o000o )
 if 80 - 80: Ii1I
elif IiI1II11iiI == 1032 :
 OOO0OOoOOO ( IiIIIIIi )
 if 67 - 67: IIiIiII11i
elif IiI1II11iiI == 1006 :
 Parse . ParseURL ( IiIIIIIi )
 if 2 - 2: I11i - o0o00Oo0O * OoOO00O % O00Oo000ooO0
elif IiI1II11iiI == 2030 :
 Parse . addonParseURL ( IiIIIIIi )
 if 64 - 64: ooOoO0O00 . O0oOO0
elif IiI1II11iiI == 2031 :
 Parse . apkParseURL ( IiIIIIIi )
 if 7 - 7: O0O0O . IIiI1I - IIiI1I / oO00Oo0o000 % I1ii11iIi11i
elif IiI1II11iiI == 1002 :
 oOoOo00oo ( IiIIIIIi )
 if 61 - 61: O0O0O - Ii1I / IIiI1I % Ii1I + oO0o / I1ii11iIi11i
elif IiI1II11iiI == 1003 :
 II11IiIIiiiii ( IiIIIIIi , oOOO00o000o )
 if 10 - 10: Ii / OOooOOo
elif IiI1II11iiI == 1004 :
 oooOOo0o0OOO ( IiIIIIIi )
 if 27 - 27: oOo0O0Ooo / ii
elif IiI1II11iiI == 1008 :
 i1I1IIiIIi ( )
 if 74 - 74: Ii1I % oO00Oo0o000 - oO0o * Ii1i111I . ii * oO0o
elif IiI1II11iiI == 1009 :
 OoOO ( IiIIIIIi )
 if 99 - 99: OOooOOo . IIiI1I - ii - o0o00Oo0O
elif IiI1II11iiI == 2001 :
 oOOo00ooO ( )
 if 6 - 6: i1IiIIIII
elif IiI1II11iiI == 2002 :
 oo000oOo0OoO0 ( IiIIIIIi )
 if 3 - 3: o0o00Oo0O - oO00Oo0o000 * OoOO00O * i1IiIIIII / OoOO00O
elif IiI1II11iiI == 1013 :
 i1I ( )
elif IiI1II11iiI == 10111113 :
 iiI1I1IIi11i1 ( IiIIIIIi )
 if 58 - 58: OoOO00O * iI11I1II1I1I + O0oOO0 . O0oOO0
elif IiI1II11iiI == 1014 :
 iIIii1iiiIiiI ( )
 if 74 - 74: O0oOO0 - I11i * O00Oo000ooO0 % O0oOO0
elif IiI1II11iiI == 1015 :
 oOo0O ( IiIIIIIi )
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * oO00Oo0o000 - oO0o - I11i
elif IiI1II11iiI == 1016 :
 i11I1iiii ( IiIIIIIi , oOOO00o000o , o0O0oo0OO0O )
 if 44 - 44: ii
elif IiI1II11iiI == 1017 :
 oOOoO0o0oO ( )
 if 82 - 82: OOooOOo . OOooOOo
elif IiI1II11iiI == 1018 :
 o0oO0O0o0O00O ( IiIIIIIi )
 if 10 - 10: I1ii11iIi11i * Ii1I . O0O0O . ii . i1IiIIIII * Ii1I
elif IiI1II11iiI == 1023 :
 OOo00 ( )
 if 80 - 80: oO00Oo0o000 + Ii1i111I . oO00Oo0o000 + i1IiIIIII
elif IiI1II11iiI == 1024 :
 O0OoO00OoOO ( IiIIIIIi )
 if 85 - 85: Ii . Ii1i111I + OoOO00O / OoOO00O
elif IiI1II11iiI == 1025 :
 OOoOo0ooOoo ( IiIIIIIi )
 if 43 - 43: O00Oo000ooO0 . ii - IIiIiII11i
elif IiI1II11iiI == 4001 :
 I11IiI ( )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * i1IiIIIII * O0O0O
elif IiI1II11iiI == 4002 :
 ooO0oOOooOo0 ( )
 if 19 - 19: oO00Oo0o000 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
elif IiI1II11iiI == 4003 :
 oO0o000OoOoO0 ( )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
elif IiI1II11iiI == 4004 :
 oOo00oOoO000 ( )
 if 15 - 15: OoOO00O + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
elif IiI1II11iiI == 4005 :
 Ii1iI1I1 ( )
 if 54 - 54: O00Oo000ooO0 - IIiIiII11i . O0oOO0 + OoOO00O
elif IiI1II11iiI == 4006 :
 oooOo0OOOoo0 ( )
 if 45 - 45: O0O0O + IIiIiII11i . IIiI1I / Ii1I
elif IiI1II11iiI == 4007 :
 IiII111i1i11 ( )
 if 76 - 76: OoOO00O + IIiI1I - O00Oo000ooO0 * iI11I1II1I1I % ooOoO0O00
elif IiI1II11iiI == 4008 :
 i111iIi1i1II1 ( )
 if 72 - 72: O0oOO0 + IIiIiII11i . o0o00Oo0O - IIiI1I / ii . oO00Oo0o000
elif IiI1II11iiI == 4009 : OOooo0oOO0O ( )
elif IiI1II11iiI == 4010 : iiI1ii11i1 ( )
elif IiI1II11iiI == 3000 :
 iiI11 ( )
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
elif IiI1II11iiI == 3001 :
 OO000OOo ( )
 if 32 - 32: ii
elif IiI1II11iiI == 3002 :
 oOo0O000Ooo0 ( IiIIIIIi )
 if 29 - 29: Ii1I
elif IiI1II11iiI == 3003 :
 i11i ( IiIIIIIi )
 if 41 - 41: OoOO00O
elif IiI1II11iiI == 3004 :
 II1IIiiI1 ( IiIIIIIi )
 if 49 - 49: OoOO00O % IIiIiII11i . OoOO00O - I11i - Ii1i111I * O00Oo000ooO0
elif IiI1II11iiI == 404 :
 OO00oOo0o00 ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o )
 if 47 - 47: o0o00Oo0O . I11i / OoOO00O * IIiI1I
elif IiI1II11iiI == 405 :
 oO0o0o ( IiIIIIIi )
 if 63 - 63: oO00Oo0o000 - O0O0O - IIiI1I - O0oOO0 / O0O0O + oO0o
elif IiI1II11iiI == 7030 :
 OooO00o000 ( )
 if 94 - 94: O00Oo000ooO0 / oOo0O0Ooo . IIiIiII11i
elif IiI1II11iiI == 7021 :
 Oo0OOOOOOO0oo ( o0O0oo0OO0O )
 if 32 - 32: O0O0O . i1IiIIIII % i1IiIIIII . OOooOOo
elif IiI1II11iiI == 7022 :
 i111i ( o0O0oo0OO0O )
 if 37 - 37: i1IiIIIII + o0o00Oo0O + i1IiIIIII . IIiI1I . I11i
elif IiI1II11iiI == 7000 :
 i11iI11 ( o0O0oo0OO0O , IiIIIIIi , img )
 if 78 - 78: oOo0O0Ooo / Ii1i111I + I11i . I1ii11iIi11i / o0o00Oo0O
elif IiI1II11iiI == 7050 :
 IIII1I ( IiIIIIIi )
 if 49 - 49: Ii1I
elif IiI1II11iiI == 7051 :
 o0O0OOOo0 ( IiIIIIIi )
 if 66 - 66: I11i . Ii1I
elif IiI1II11iiI == 7052 :
 iiIiIiI111 ( IiIIIIIi )
 if 18 - 18: I1ii11iIi11i + O00Oo000ooO0
elif IiI1II11iiI == 7053 :
 OO0OO00ooO0 ( IiIIIIIi )
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % OoOO00O . oOo0O0Ooo
elif IiI1II11iiI == 7054 :
 CoolPlay ( IiIIIIIi )
 if 43 - 43: oOo0O0Ooo % Ii1I * OoOO00O
elif IiI1II11iiI == 7060 :
 ooOi1i1i11iI11II ( )
 if 31 - 31: OoOO00O / IIiI1I
elif IiI1II11iiI == 7061 :
 o00oo ( IiIIIIIi )
 if 3 - 3: O00Oo000ooO0
elif IiI1II11iiI == 7063 :
 II1iiI1iI ( IiIIIIIi )
 if 37 - 37: OoOO00O * ii * Ii1i111I + I1ii11iIi11i . oOo0O0Ooo
elif IiI1II11iiI == 7062 :
 iII1I ( IiIIIIIi )
 if 61 - 61: i1IiIIIII . i1IiIIIII
elif IiI1II11iiI == 7064 :
 NATatozcat ( )
 if 17 - 17: IIiIiII11i / O0oOO0
elif IiI1II11iiI == 7067 :
 o00oOOo0Oo ( IiIIIIIi )
 if 80 - 80: i1IiIIIII * oO0o + OoOO00O
elif IiI1II11iiI == 7066 :
 NATatozA ( IiIIIIIi )
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
elif IiI1II11iiI == 7065 :
 Oooo0o0oO ( IiIIIIIi )
 if 98 - 98: I11i * I1ii11iIi11i - OoOO00O . O0oOO0
elif IiI1II11iiI == 7070 :
 o00OIIIIIiiI ( )
 if 2 - 2: I1ii11iIi11i - O0oOO0 % iI11I1II1I1I
elif IiI1II11iiI == 7071 :
 DIZIlist ( IiIIIIIi )
 if 88 - 88: oO00Oo0o000 - oO0o
elif IiI1II11iiI == 7072 :
 DIZIpull ( IiIIIIIi )
 if 79 - 79: IIiI1I
elif IiI1II11iiI == 7073 :
 WATCHDIZI ( IiIIIIIi )
 if 45 - 45: IIiIiII11i + IIiI1I . Ii1i111I . o0o00Oo0O * ooOoO0O00 - OoOO00O
elif IiI1II11iiI == 7002 :
 iIII1I1i ( )
 if 48 - 48: Ii1I + I1ii11iIi11i
elif IiI1II11iiI == 7003 :
 o0Oo ( IiIIIIIi )
 if 76 - 76: Ii1I
elif IiI1II11iiI == 7004 :
 iIIi1II1 ( IiIIIIIi )
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . OoOO00O
elif IiI1II11iiI == 7020 :
 OO0Iii1iIiI111Ii ( IiIIIIIi )
 if 51 - 51: OoOO00O + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
elif IiI1II11iiI == 7001 :
 OOoOoO ( )
 if 20 - 20: oO00Oo0o000 . Ii1i111I . OoOO00O + Ii1i111I - i1IiIIIII * O0O0O
elif IiI1II11iiI == 7010 :
 iiIIiI1 ( IiIIIIIi )
 if 82 - 82: oO0o
elif IiI1II11iiI == 7011 :
 I1Ii11i1ii1i ( IiIIIIIi )
 if 78 - 78: IIiIiII11i / Ii1i111I - Ii + Ii1I * I1ii11iIi11i
elif IiI1II11iiI == 7012 :
 I1111111 ( IiIIIIIi )
 if 17 - 17: OOooOOo
elif IiI1II11iiI == 7013 :
 cnfTVPlay2 ( IiIIIIIi )
elif IiI1II11iiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( IiIIIIIi )
elif IiI1II11iiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( IiIIIIIi )
elif IiI1II11iiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o )
elif IiI1II11iiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif IiI1II11iiI == 7018 :
 ii1111IIiI1 ( )
elif IiI1II11iiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( IiIIIIIi )
elif IiI1II11iiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( IiIIIIIi )
elif IiI1II11iiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( IiIIIIIi )
 if 72 - 72: IIiI1I . I1ii11iIi11i - Ii / oOo0O0Ooo
elif IiI1II11iiI == 8000 :
 IIii ( )
elif IiI1II11iiI == 8001 :
 OOOo0Oo0O ( )
elif IiI1II11iiI == 8002 :
 iii111i ( )
elif IiI1II11iiI == 8003 :
 IIoO ( )
elif IiI1II11iiI == 8004 :
 oOooOoOOo0O ( )
elif IiI1II11iiI == 8005 :
 IiOo00O0o0O ( )
elif IiI1II11iiI == 8006 :
 Ii1iI1IIIII ( o0O0oo0OO0O , IiIIIIIi )
elif IiI1II11iiI == 8030 :
 ii1I11iIiIII1 ( IiIIIIIi )
elif IiI1II11iiI == 8045 :
 OoO000Oo0oO ( IiIIIIIi )
elif IiI1II11iiI == 8046 :
 iiiIiiiI1 ( IiIIIIIi )
elif IiI1II11iiI == 8047 :
 i11IIO00oo0O00 ( IiIIIIIi )
elif IiI1II11iiI == 8048 :
 OoO0o00OOOOO ( IiIIIIIi )
elif IiI1II11iiI == 8049 :
 I1iIi1iIIIIiI ( IiIIIIIi )
elif IiI1II11iiI == 8020 :
 ii1IIii ( )
elif IiI1II11iiI == 8021 :
 Ii1111Ii1 ( IiIIIIIi )
elif IiI1II11iiI == 8022 :
 III1Iiii1i11 ( IiIIIIIi )
elif IiI1II11iiI == 8023 :
 OO00 ( IiIIIIIi )
elif IiI1II11iiI == 8040 :
 Oo0O0OO0OoO0 ( )
elif IiI1II11iiI == 8041 :
 oooo0o0OOO0 ( IiIIIIIi )
elif IiI1II11iiI == 8042 :
 OOo ( IiIIIIIi )
elif IiI1II11iiI == 8043 :
 yt . PlayVideo ( IiIIIIIi )
elif IiI1II11iiI == 8044 :
 O0OOOO0000O ( IiIIIIIi )
elif IiI1II11iiI == 8060 :
 iIiIIi11iI ( )
elif IiI1II11iiI == 8061 :
 ooo00o0o ( IiIIIIIi )
elif IiI1II11iiI == 8064 :
 OoOoO0ooooO0 ( )
elif IiI1II11iiI == 8065 :
 IIII1ii1 ( IiIIIIIi )
elif IiI1II11iiI == 8070 :
 Iii1 ( )
elif IiI1II11iiI == 8071 :
 OOoO ( IiIIIIIi )
elif IiI1II11iiI == 7080 :
 i1IiiI ( IiIIIIIi )
elif IiI1II11iiI == 8090 :
 iiI1ii1Iii ( )
elif IiI1II11iiI == 8091 :
 Ii1I1IIIiI1i ( IiIIIIIi )
elif IiI1II11iiI == 8092 :
 o0Oo00oOO ( IiIIIIIi )
elif IiI1II11iiI == 8081 :
 I1111I1Ii ( )
elif IiI1II11iiI == 8062 :
 IiiiI1Ii ( IiIIIIIi )
elif IiI1II11iiI == 8063 :
 oo0O ( IiIIIIIi )
elif IiI1II11iiI == 8050 :
 i1i1 ( )
elif IiI1II11iiI == 8051 :
 oO0ooOoO ( IiIIIIIi )
elif IiI1II11iiI == 8052 :
 ooO0000o00O ( IiIIIIIi )
elif IiI1II11iiI == 8085 :
 OoO0 ( )
elif IiI1II11iiI == 8086 :
 Oooo ( IiIIIIIi )
elif IiI1II11iiI == 8087 :
 i1IIiIIIi1 ( IiIIIIIi )
elif IiI1II11iiI == 8088 :
 oOoO00O ( IiIIIIIi , o0O0oo0OO0O )
elif IiI1II11iiI == 9000 :
 IiI1iii11iIi1 ( )
elif IiI1II11iiI == 1111 :
 oO0oO00 ( )
elif IiI1II11iiI == 9001 :
 I1iii1 ( )
elif IiI1II11iiI == 9002 :
 oOOoO0oO0oo0O ( )
elif IiI1II11iiI == 9003 :
 ooo00o0OO ( )
elif IiI1II11iiI == 50 :
 oOoooO0 ( IiIIIIIi )
elif IiI1II11iiI == 9020 :
 champlist ( )
elif IiI1II11iiI == 9021 :
 ooOO00o0 ( )
elif IiI1II11iiI == 9022 :
 Ii1I1iIiiI1 ( )
elif IiI1II11iiI == 9023 :
 o00i111iiIiiIiI ( )
elif IiI1II11iiI == 9024 :
 oOoo00 ( IiIIIIIi )
elif IiI1II11iiI == 9030 :
 Ii1 ( IiIIIIIi )
elif IiI1II11iiI == 9031 :
 iIIi11 ( IiIIIIIi )
elif IiI1II11iiI == 9032 :
 iIiiII1Ii1ii ( IiIIIIIi )
elif IiI1II11iiI == 9033 :
 iIIi1 ( IiIIIIIi )
elif IiI1II11iiI == 7085 :
 IiIII ( IiIIIIIi )
elif IiI1II11iiI == 7086 :
 iiiI1IiI ( IiIIIIIi )
elif IiI1II11iiI == 7087 :
 Iii1oooo00Oo0O ( oOoO00oo0O )
elif IiI1II11iiI == 9666 :
 Ii1iIi111i1i1 ( IiIIIIIi )
elif IiI1II11iiI == 10100 : Oo0OoOo ( )
elif IiI1II11iiI == 10105 : iII11II1II ( IiIIIIIi )
elif IiI1II11iiI == 10106 : OooIii1I1iI ( IiIIIIIi )
elif IiI1II11iiI == 10104 : oOO00OO0OooOo ( IiIIIIIi )
elif IiI1II11iiI == 10107 : IiI ( )
elif IiI1II11iiI == 10103 : IIi1ii ( IiIIIIIi )
elif IiI1II11iiI == 10108 : O0OooooO0o0O0 ( IiIIIIIi )
elif IiI1II11iiI == 10107 : IiI ( )
elif IiI1II11iiI == 10000 : Origin_Menu ( )
elif IiI1II11iiI == 10001 : oOoO0O00oo ( )
elif IiI1II11iiI == 10002 : OOooOO ( )
elif IiI1II11iiI == 10003 : OoOo ( )
elif IiI1II11iiI == 10004 : i11II ( IiIIIIIi )
elif IiI1II11iiI == 10005 : oo0 ( )
elif IiI1II11iiI == 10006 : Oo0O0O00Oo ( IiIIIIIi )
elif IiI1II11iiI == 10007 : o0O0oO0 ( IiIIIIIi , oOOO00o000o )
elif IiI1II11iiI == 10008 : I111 ( )
elif IiI1II11iiI == 10009 : oOIiiIIi ( )
elif IiI1II11iiI == 10010 : iIO0OO0o0O00oO ( IiIIIIIi )
elif IiI1II11iiI == 10011 : i1Ii1i1 ( IiIIIIIi )
elif IiI1II11iiI == 10012 : O00OO ( IiIIIIIi )
elif IiI1II11iiI == 10013 : i1Ii11IIi1 ( IiIIIIIi )
elif IiI1II11iiI == 10014 : Ii1Iii11 ( )
elif IiI1II11iiI == 10015 : ii1I111i1Ii ( )
elif IiI1II11iiI == 10016 : o00iI1i1II ( IiIIIIIi )
elif IiI1II11iiI == 10017 : o0i1I11iI1iiI ( )
elif IiI1II11iiI == 10018 : oo0OoOO0o0o ( )
elif IiI1II11iiI == 10019 : iIiI1Iii1 ( )
elif IiI1II11iiI == 10020 : ooooO000 ( )
elif IiI1II11iiI == 10021 : IIii1III ( )
elif IiI1II11iiI == 10022 : Iiii1 ( IiIIIIIi )
elif IiI1II11iiI == 10023 : Oooo00 ( o0O0oo0OO0O , IiIIIIIi )
elif IiI1II11iiI == 10024 : IiIIII1iiIIi ( IiIIIIIi )
elif IiI1II11iiI == 10025 : I11i11i1 ( )
elif IiI1II11iiI == 10026 : o0Ii1 ( )
elif IiI1II11iiI == 10027 : oOOOOoO00Ooo0 ( )
elif IiI1II11iiI == 10028 : ooOooO00Oo ( )
elif IiI1II11iiI == 10029 : OO0ooo0 ( )
elif IiI1II11iiI == 423 : ii1I ( IiIIIIIi )
elif IiI1II11iiI == 426 : ooooO ( IiIIIIIi )
elif IiI1II11iiI == 10030 : Izle_Films ( )
elif IiI1II11iiI == 10031 : Latest_Izle_Movies ( )
elif IiI1II11iiI == 10032 : Izle_Genres ( )
elif IiI1II11iiI == 10033 : Izle_Pop_Movies ( )
elif IiI1II11iiI == 10034 : Izle_Boxsets ( )
elif IiI1II11iiI == 10035 : Izle_Search ( )
elif IiI1II11iiI == 10036 : Izle_Genres_Movie ( IiIIIIIi )
elif IiI1II11iiI == 10037 : Izle_Boxset_single ( IiIIIIIi )
elif IiI1II11iiI == 10038 : Izle_IFRAME ( )
elif IiI1II11iiI == 10039 : Izle_Boxsets_Next ( IiIIIIIi )
elif IiI1II11iiI == 10040 : i111IiiI1Ii ( )
elif IiI1II11iiI == 10041 : o0O0 ( IiIIIIIi )
elif IiI1II11iiI == 10042 : oO0o0Oo ( IiIIIIIi )
elif IiI1II11iiI == 10043 : o0oOoOo0 ( )
elif IiI1II11iiI == 10044 : iio0o000Oo ( IiIIIIIi )
elif IiI1II11iiI == 10045 : I1II1oOOoo ( o0O0oo0OO0O )
elif IiI1II11iiI == 10046 : i1iI1Iiii1I ( IiIIIIIi )
elif IiI1II11iiI == 10047 : Oo0oOO ( IiIIIIIi )
elif IiI1II11iiI == 10048 : iiiIioo ( IiIIIIIi )
elif IiI1II11iiI == 10049 : o0OO ( IiIIIIIi )
elif IiI1II11iiI == 10050 : oOoO0o0Ooo ( )
elif IiI1II11iiI == 10051 : IiI1 ( )
elif IiI1II11iiI == 10052 : iI1III ( )
elif IiI1II11iiI == 10053 : Addon ( IiIIIIIi )
elif IiI1II11iiI == 10054 : O0ooO ( IiIIIIIi , o0O0oo0OO0O )
elif IiI1II11iiI == 10055 :
 oO0OIiii1I ( "addFavorite" )
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 O00O ( o0O0oo0OO0O , IiIIIIIi , oOOO00o000o , iIi11i1 , iiii1I1 )
elif IiI1II11iiI == 10056 :
 oO0OIiii1I ( "rmFavorite" )
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  o0O0oo0OO0O = o0O0oo0OO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 oO0o0o00oOo0O ( o0O0oo0OO0O )
elif IiI1II11iiI == 10057 :
 oO0OIiii1I ( "getFavorites" )
 o0oO00 ( )
elif IiI1II11iiI == 10058 : o00O0 ( )
elif IiI1II11iiI == 10059 : Donators_Guide ( )
elif IiI1II11iiI == 10060 : ooo000ooO0000 ( )
elif IiI1II11iiI == 10061 : i11i1iiI1i ( )
elif IiI1II11iiI == 10062 : I1II ( o0O0oo0OO0O , IiIIIIIi , oOoO00oo0O )
elif IiI1II11iiI == 10063 : i1iiIiI1Ii1i ( )
elif IiI1II11iiI == 10064 : Ooo0o00o0o ( )
elif IiI1II11iiI == 10065 : oO0o00ooO ( IiIIIIIi )
elif IiI1II11iiI == 10066 : iIIII1iIIii ( IiIIIIIi )
elif IiI1II11iiI == 10068 : iIi1Ii1i1iI ( IiIIIIIi )
elif IiI1II11iiI == 10069 : ii1ii111 ( IiIIIIIi )
elif IiI1II11iiI == 10070 : OOOOO0O00 ( IiIIIIIi )
elif IiI1II11iiI == 10071 : Genie_Watch ( )
elif IiI1II11iiI == 10072 : ooOoOo0 ( )
elif IiI1II11iiI == 10073 : I1i11 ( IiIIIIIi )
elif IiI1II11iiI == 10074 : ii1 ( IiIIIIIi )
elif IiI1II11iiI == 10075 : II1I1I1Ii ( oOOO00o000o , o0O0oo0OO0O , IiIIIIIi )
elif IiI1II11iiI == 10076 : i1i1ii ( IiIIIIIi )
elif IiI1II11iiI == 10077 : OooooOoooO ( IiIIIIIi )
elif IiI1II11iiI == 10078 : iII1i1 ( )
elif IiI1II11iiI == 10079 : Genie_Watch_Tv_Shows ( )
elif IiI1II11iiI == 10080 : Genie_Watch_Tv_Genre ( IiIIIIIi )
elif IiI1II11iiI == 10081 : Genie_Watch_TV_PlayRun ( IiIIIIIi )
elif IiI1II11iiI == 10082 : Genie_Watch_TV_Episodes ( IiIIIIIi , oOOO00o000o )
elif IiI1II11iiI == 10083 : Genie_Watch_Tv_Recent ( IiIIIIIi )
elif IiI1II11iiI == 10084 : O0Oo0oOOoooOOOOo ( )
elif IiI1II11iiI == 10085 : i1iIi ( )
elif IiI1II11iiI == 10086 : IIII ( )
elif IiI1II11iiI == 20000 : iI1I1I11IiII ( )
elif IiI1II11iiI == 20001 : IiI1IIIII1I ( )
elif IiI1II11iiI == 20002 : oOO0o0oo0 ( IiIIIIIi )
elif IiI1II11iiI == 20003 : Oo ( IiIIIIIi )
elif IiI1II11iiI == 20004 : i1iIIi1o0o0OoOOOOOo ( IiIIIIIi )
elif IiI1II11iiI == 21004 : i1iii11 ( )
elif IiI1II11iiI == 21005 : oOo0O0o0000o0O0 ( IiIIIIIi )
elif IiI1II11iiI == 21006 : iIiii ( IiIIIIIi )
elif IiI1II11iiI == 21007 : O000O ( IiIIIIIi )
elif IiI1II11iiI == 30000 : IiiIiI ( )
elif IiI1II11iiI == 30001 : ii1I1I111 ( )
elif IiI1II11iiI == 10012 : Resolve ( IiIIIIIi )
elif IiI1II11iiI == 30003 : Ii1iI ( )
elif IiI1II11iiI == 30004 : I11oOOooo ( IiIIIIIi )
elif IiI1II11iiI == 30005 : oOoooO000O ( IiIIIIIi )
elif IiI1II11iiI == 30006 : i1i1II11II1 ( )
elif IiI1II11iiI == 30007 : iiIi1I1i1 ( )
elif IiI1II11iiI == 30008 : oOo0OOoooO ( IiIIIIIi )
elif IiI1II11iiI == 30009 : i11i1Ii1 ( IiIIIIIi )
elif IiI1II11iiI == 30010 : iIiIii1I1II ( IiIIIIIi )
elif IiI1II11iiI == 30011 : IiiIIIiI1ii ( )
elif IiI1II11iiI == 30012 : iIii1Ooo0oO0 ( )
elif IiI1II11iiI == 30013 : ooOo0O0o0 ( )
elif IiI1II11iiI == 30014 : OooOo000o0o ( )
elif IiI1II11iiI == 30015 : IIII1ii ( IiIIIIIi , oOOO00o000o , iIi11i1 )
elif IiI1II11iiI == 30016 : iii1III1i ( IiIIIIIi )
elif IiI1II11iiI == 30019 : i1o0oooO ( IiIIIIIi )
elif IiI1II11iiI == 30017 : o0OoO00 ( IiIIIIIi )
elif IiI1II11iiI == 30018 : i1oO ( IiIIIIIi )
elif IiI1II11iiI == 30030 : o0oO0OO00oo0o ( )
elif IiI1II11iiI == 30031 : I1II1 ( )
elif IiI1II11iiI == 30032 : Oo000o ( )
elif IiI1II11iiI == 30033 : OO00oo ( )
elif IiI1II11iiI == 30034 : O0Oo0O0 ( )
elif IiI1II11iiI == 30035 : O0OOOo ( IiIIIIIi )
elif IiI1II11iiI == 30036 : i11I1I1iiI ( IiIIIIIi )
elif IiI1II11iiI == 30037 : I1i1iii1Ii ( IiIIIIIi )
elif IiI1II11iiI == 30038 : OoOOo ( )
elif IiI1II11iiI == 30039 : iIIiiIIi1IiI ( )
elif IiI1II11iiI == 50000 : IiI111111IIII ( )
elif IiI1II11iiI == 50001 : III1I1i1 ( )
elif IiI1II11iiI == 50002 : iiII ( IiIIIIIi )
elif IiI1II11iiI == 50003 : i1i1iIII11i ( oOoO00oo0O )
if 64 - 64: O0O0O
if 80 - 80: I11i % iI11I1II1I1I
if 63 - 63: O00Oo000ooO0 * Ii
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
