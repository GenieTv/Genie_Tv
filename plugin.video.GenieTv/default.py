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
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , OOoOO0oo0ooO + 'TvGuide.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']STREAM TEAM[/COLOR]' , str ( OOO00O ) , 4006 , OOoOO0oo0ooO + 'StreamTeam.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']24/7 STREAMS[/COLOR]' , '' , 30030 , OOoOO0oo0ooO + '247Streams.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MOVIES[/COLOR]' , str ( OOO00O ) , 4004 , OOoOO0oo0ooO + 'Movies.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']TV SHOWS[/COLOR]' , str ( OOO00O ) , 4005 , OOoOO0oo0ooO + 'TVShows.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KIDS[/COLOR]' , str ( OOO00O ) , 4007 , OOoOO0oo0ooO + 'Kids.png' , i1iIIi1 , '' )
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
  if 38 - 38: oO00Oo0o000
  if 84 - 84: iI11I1II1I1I % IIiI1I / iI11I1II1I1I % Ii1i111I
 if o0oO0 . getSetting ( 'Playlist Loader' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PLAYLIST LOADER[/COLOR]' , str ( OOO00O ) , 3000 , OOoOO0oo0ooO + 'PlaylistLoader.png' , i1iIIi1 , '' )
  if 45 - 45: o0o00Oo0O
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
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 100 - 100: oO00Oo0o000 * o0o00Oo0O
def o00oooO0Oo ( ) :
 if not os . path . exists ( II ) :
  o00oO0oo0OO ( 'Change Log 19/07/16 - v3.0.1' , 'Search fixed for series,  Watch series in tv shows tab fixed,   Watch Cartoons Online fixed in kids section.  Watched feature added but a work in progress' )
  os . makedirs ( II )
  if 57 - 57: oO00Oo0o000 % OoOO00O + I11i - I1ii11iIi11i
  if 65 - 65: Ii1i111I . OOooOOo
def IiI1i ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( OOO00O ) , 9001 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Popcorn Box' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']POPCORN BOX[/COLOR]' , str ( OOO00O ) , 7061 , OOoOO0oo0ooO + 'PopcornBox.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Film Trailers[/COLOR]' , i1111 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , OOoOO0oo0ooO + 'FilmTrailers.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , OOoOO0oo0ooO + 'ClassicMovies.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def o0Oo00 ( ) :
 I1ii11iI ( )
 if o0oO0 . getSetting ( 'G-tv' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']G-Tv PRIVATE LIST[/COLOR]' , '' , 10058 , OOoOO0oo0ooO + 'GTVIPTV.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']TV GUIDE[/COLOR]' , '' , 10063 , OOoOO0oo0ooO + 'GTVIPTV.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']Link GTV Donators Username and Password to Guide[/COLOR]' , '' , 4010 , OOoOO0oo0ooO + 'GTVIPTV.png' , i1iIIi1 , '' )
 if 32 - 32: I11i . O00Oo000ooO0 * Ii1i111I
 if 93 - 93: I11i % ooOoO0O00 . OoOO00O . Ii
def oOOoo00O00o ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( OOO00O ) , 9002 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 98 - 98: i1IiIIIII + O00Oo000ooO0 + O0O0O % ii
 if 97 - 97: o0o00Oo0O * ii . ii
 if o0oO0 . getSetting ( 'Watch Series' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH SERIES[/COLOR]' , '' , 10040 , OOoOO0oo0ooO + 'WatchSeries.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']iWATCH SERIES[/COLOR]' , '' , 8020 , OOoOO0oo0ooO + 'iWatchSeries.png' , i1iIIi1 , '' )
 if 33 - 33: oO00Oo0o000 + IIiI1I * O0O0O / iI11I1II1I1I - oOo0O0Ooo
 if 54 - 54: oO00Oo0o000 / i1IiIIIII . O0O0O % IIiI1I
 if o0oO0 . getSetting ( 'CLASSIC TV' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CLASSIC TV[/COLOR]' , str ( OOO00O ) , 8064 , OOoOO0oo0ooO + 'ClassicTV.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']TV Show Trailers[/COLOR]' , i1111 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , OOoOO0oo0ooO + 'TVShowTrailers.png' , i1iIIi1 , '' )
 if 57 - 57: Ii . Ii1I - OoOO00O - O0O0O + OOooOOo
 oO00OOoO00 ( 'movies' , 'MAIN' )
def oO00oooOOoOo0 ( ) :
 I1ii11iI ( )
 if o0oO0 . getSetting ( 'Silent Hunter' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 10084 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'The Reaper' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']THE REAPER[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'TheReaper.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Pandoras Box' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PANDORAS BOX[/COLOR]' , str ( OOO00O ) , 10025 , OOoOO0oo0ooO + 'PandorasBox.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Redemption Streams' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Redemption Streams[/COLOR]' , ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'RedemptionStreams.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']DoJo STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'DojoStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Scooby Streams' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , str ( OOO00O ) , 1023 , OOoOO0oo0ooO + 'ScoobyStreams.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'HeroVision' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , '' , 1017 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ITV[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'ITVStreams.png' , i1iIIi1 , '' )
 if 74 - 74: iI11I1II1I1I * Ii1I + OOooOOo / ooOoO0O00 / IIiIiII11i . I1ii11iIi11i
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 62 - 62: ii * oOo0O0Ooo
def oOOOoo0O0oO ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SILENT HUNTER SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , OOoOO0oo0ooO + 'SilentHunter.png' , i1iIIi1 , '' )
 if 6 - 6: i1IiIIIII * I11i + IIiI1I
def I1IIIiIiI1 ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HEROVISION SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , OOoOO0oo0ooO + 'Herovision.png' , i1iIIi1 , '' )
 if 28 - 28: iI11I1II1I1I % I1ii11iIi11i * oOo0O0Ooo % OoOO00O * I11i / I11i
def iIIII ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'SearchCartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'WCO' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( OOO00O ) , 21004 , OOoOO0oo0ooO + 'watchcartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Cartoons' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 10001 , OOoOO0oo0ooO + 'Cartoons.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'Anime' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']AnimeLand[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , OOoOO0oo0ooO + 'anime.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def I11iI1i1I11I11 ( ) :
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
 if 69 - 69: OOooOOo
 if 97 - 97: Ii1I % Ii1I % O0O0O / IIiI1I - iI11I1II1I1I
 if 69 - 69: oO00Oo0o000
def ooOOoooooo ( ) :
 IIiII = Iiii ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 o0O00oOoOO = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( IIiII )
 for IIi1i in o0O00oOoOO :
  IIi1i = ( str ( IIi1i ) )
  if os . path . exists ( xbmc . translatePath ( IIi1i ) ) :
   ii1I1 = ( IIi1i ) . replace ( 'special://home/addons/' , '' )
   o00oO0oo0OO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + ii1I1 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   OooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if OooooOOoo0 == 0 :
    I1I1iIiII1 ( IIi1i )
    i1I1IiiIi1i ( )
   elif OooooOOoo0 == 1 :
    iiI11ii1I1 ( IIi1i )
  else :
   pass
   if 82 - 82: IIiIiII11i % Ii1i111I / oO0o + OOooOOo / I11i / oO00Oo0o000
def iiI11ii1I1 ( addon ) :
 ii1I1 = ( addon ) . replace ( 'special://home/addons/' , '' )
 Oo0oO0ooo . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 Oo0oO0ooo . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 Oo0oO0ooo . close ( )
 if 70 - 70: O0O0O
def I1I1iIiII1 ( addon ) :
 oOOoo00O0O . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOOoO0o0oO = os . path . join ( iiI1IiI , 'default.py' )
 o0Oo0oO0oOO00 = open ( oOOoO0o0oO , "w+" )
 if 92 - 92: ii * oO00Oo0o000
 o0Oo0oO0oOO00 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o0Oo0oO0oOO00 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o0Oo0oO0oOO00 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 100 - 100: oO00Oo0o000 + oO00Oo0o000 * O00Oo000ooO0
 if 1 - 1: O0oOO0 . O0oOO0 / OOooOOo - oO00Oo0o000
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
 if 19 - 19: Ii1I % ii % O00Oo000ooO0 * I11i % o0o00Oo0O
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
 if 27 - 27: O0oOO0 % oOo0O0Ooo
 if 73 - 73: i1IiIIIII
 if 70 - 70: iI11I1II1I1I
 if 31 - 31: O00Oo000ooO0 - oOo0O0Ooo % iI11I1II1I1I
 if 92 - 92: ooOoO0O00 - iI11I1II1I1I
 if 16 - 16: oO0o - OOooOOo - i1IiIIIII - ooOoO0O00 / OoOO00O
 if 88 - 88: oO0o
 if 71 - 71: Ii1I
 if 7 - 7: Ii1I - oOo0O0Ooo . iI11I1II1I1I - ooOoO0O00
 if 59 - 59: I11i
 if 81 - 81: OOooOOo - OOooOOo . IIiI1I
 if 73 - 73: Ii1i111I % Ii - oOo0O0Ooo
 if 7 - 7: o0o00Oo0O * Ii * OoOO00O + O0oOO0 % oO0o - O0oOO0
 if 39 - 39: I1ii11iIi11i * i1IiIIIII % i1IiIIIII - ii + I11i - Ii1i111I
def iiO0oOo00o ( ) :
 o0OOOO00O0Oo ( 'Genre' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Most Viewed' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Box Office' , i1111 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( 'Search' , '' , 10078 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
 if 81 - 81: O00Oo000ooO0 % ooOoO0O00 . iI11I1II1I1I
def Ii1Iii1iIi ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1 = 'http://imoviemax.se/?s=' + ( OO0oo ) . replace ( ' ' , '+' )
 OOO0000oO = Iii1 . lower ( )
 iI1i111I1Ii ( OOO0000oO )
def i11i1ii1I ( url ) :
 o0OO0o0o00o = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="cat-item cat-item-.+? "><a href="(.+?)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( IIiII )
 for url , oOo0 , OOOoOO in o0O00oOoOO :
  if oOo0 in o0OO0o0o00o :
   pass
  else :
   o0OOOO00O0Oo ( oOo0 + ' - ' + OOOoOO + ' Films' , url , 10074 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
   o0OO0o0o00o . append ( oOo0 )
   if 10 - 10: IIiI1I + I1ii11iIi11i * Ii1I + iI11I1II1I1I / oO00Oo0o000 / Ii1I
def iI1II ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="(.+?)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 , o0OOo0o0O0O in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 + ' - Views:' + o0OOo0o0O0O , url , 10075 , OOoOO0oo0ooO + 'genievision.png' , i1iIIi1 , '' )
  if 65 - 65: Ii
  if 85 - 85: OoOO00O % IIiI1I + Ii1i111I / I11i . O0O0O + i1IiIIIII
def iI1i111I1Ii ( url ) :
 ooOoOo0 = [ ]
 IIiII = Iiii ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( IIiII )
 for next in next :
  o0OOOO00O0Oo ( 'NEXT PAGE' , next , 10074 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt="(.+?)" />.+?<a href="(.+?)"><span class="player"></span></a>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , oOo0 , url in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 10075 , I11iiiiI1i , I11iiiiI1i , '' )
  ooOoOo0 . append ( oOo0 )
  if 40 - 40: Ii1I + ooOoO0O00 * i1IiIIIII
def O0oOOoooOO0O ( img , name , url ) :
 img = img
 name = name
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="(.+?)" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</iframe></div>' ) . findall ( IIiII )
 for ooo00Ooo , url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Oo0o0O00 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Oo0o0O00
  ii1 = ( ooo00Ooo ) . replace ( 'play-' , 'Server ' )
  OOooOoooOoOo ( ii1 , Oo0o0O00 , 10076 , img , img , '' )
  if 39 - 39: OoOO00O / O0oOO0 . I11i % o0o00Oo0O * IIiI1I + oOo0O0Ooo
def O0oo0O ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( IIiII )
 for I1IiI11 in o0O00oOoOO :
  if '=m' in I1IiI11 :
   iI1iiiiIii ( I1IiI11 )
  elif 'php' in I1IiI11 :
   O0oo0O ( url )
  else :
   IIiII = Iiii ( I1IiI11 )
   o0O00oOoOO = re . compile ( 'content="(.+?)">' ) . findall ( IIiII )
   for iIiIiIiI in o0O00oOoOO :
    iI1iiiiIii ( I1IiI11 )
    if 30 - 30: oO00Oo0o000 . O0oOO0 * Ii1I
    if 17 - 17: oOo0O0Ooo . o0o00Oo0O + oO0o
    if 43 - 43: IIiIiII11i . O0O0O / Ii1I
def i1iI1 ( url ) :
 IIiII = Iiii ( url )
 i11ii1ii11i = re . compile ( '<td id=".+?" class="today">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for ooO0OoOO , O0O0Oo00 in i11ii1ii11i :
  print 'there ><><><><><><><><><><><><'
  ooO0OoOO = ooO0OoOO
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0O0Oo00 ) )
  for oOo0 , oOoO00o in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + ooO0OoOO + '[/COLOR] - ' + oOo0 + ' - [COLOR' + oO0o0o0ooO0oO + ']' + oOoO00o + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
 oO00O0 = re . compile ( '<td id=".+?" class="day">.+?title="(.+?)">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for ooO0OoOO , IIi1IIIi in oO00O0 :
  print 'there ><><><><><><><><><><><><'
  ooO0OoOO = ooO0OoOO
  o0O00oOoOO = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIi1IIIi ) )
  for oOo0 , oOoO00o in o0O00oOoOO :
   print 'here <><><><><><><><><><><><>'
   o0OOOO00O0Oo ( '[COLORred]' + ooO0OoOO + '[/COLOR] - ' + oOo0 + ' - [COLOR' + oO0o0o0ooO0oO + ']' + oOoO00o + '[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , OOoOO0oo0ooO + 'loader.png' , i1iIIi1 , '' )
   if 99 - 99: OoOO00O + oO0o * IIiIiII11i . I11i - Ii1I
   if 58 - 58: OoOO00O + I11i - oOo0O0Ooo
   if 3 - 3: oO0o
def oooOoOOO0oo0o ( url ) :
 IIiII = Iiii ( url )
 oO00O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
 for oO00O0 in oO00O0 :
  oOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oO00O0 ) )
  for oOo0 in oOo0 :
   oOo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oO00O0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  Oo0oooO0oO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oO00O0 ) )
  for Oo0oooO0oO in Oo0oooO0oO :
   Oo0oooO0oO = 'http:' + Oo0oooO0oO
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , '' , '' )
  if 19 - 19: Ii + ii - I1ii11iIi11i - Ii1i111I
  if 21 - 21: o0o00Oo0O % O00Oo000ooO0 . oOo0O0Ooo / IIiIiII11i + O00Oo000ooO0
  if 53 - 53: O0O0O - oOo0O0Ooo - O0O0O * IIiI1I
  if 71 - 71: o0o00Oo0O - iI11I1II1I1I
def i1II ( url ) :
 if 14 - 14: O0O0O / O0O0O % O0oOO0
 ooO = [ ]
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="(.+?)" class=".+?"><img src="(.+?)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( IIiII )
 for I1IiI11 , I11iiiiI1i , oOo0 , iiOO0O0Ooo in o0O00oOoOO :
  oOo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0ooOooo000oOO = Iiii ( I1IiI11 )
  iIIi1i1 = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0ooOooo000oOO )
  for oOoO0 , Oo0 in iIIi1i1 :
   oo0O0o00o0O = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( Oo0 ) )
   for I11i1II in oo0O0o00o0O :
    if oOo0 in ooO :
     pass
    else :
     OOooOoooOoOo ( oOo0 , oOoO0 , 8043 , I11iiiiI1i , I11iiiiI1i , I11i1II )
     oO00OOoO00 ( 'movies' , 'INFO' )
     ooO . append ( oOo0 )
     if 72 - 72: iI11I1II1I1I . ooOoO0O00 / I1ii11iIi11i . IIiIiII11i
     if 54 - 54: IIiIiII11i % IIiIiII11i
def Oo00000o0o ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , oOoOoOoo0 , I11i1II , III1ii1I , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 10065 , oOoOoOoo0 , III1ii1I , I11i1II )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 13 - 13: Ii + ooOoO0O00 * iI11I1II1I1I % ii - IIiIiII11i * i1IiIIIII
def iiIi1iI1iIii ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1 = 'https://www.youtube.com/results?search_query=' + ( OO0oo ) . replace ( ' ' , '+' )
 OOO0000oO = Iii1 . lower ( )
 IIiII = Iiii ( OOO0000oO )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for o00OooO0oo in next :
  o00OooO0oo = 'https://www.youtube.com' + o00OooO0oo
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , o00OooO0oo , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for I11iiiiI1i , o00OooO0oo , oOo0 , o0o0oOoOO0O , Oo0 in o0O00oOoOO :
  OO0o . append ( oOo0 )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  Oo0oooO0oO = 'http:' + ( I11iiiiI1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Oo0oooO0oO
  o00OooO0oo = 'http://www.youtube.com' + o00OooO0oo
  OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , Oo0oooO0oO , Oo0 )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for I11iiiiI1i , o00OooO0oo , oOo0 , o0o0oOoOO0O in o0O00oOoOO :
   print 'im doing it'
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   Oo0oooO0oO = 'http:' + ( I11iiiiI1i ) . replace ( 'https:' , '' )
   o00OooO0oo = 'http://www.youtube.com' + o00OooO0oo
   if '&' in o00OooO0oo :
    print ' i got here'
    IIiII = Iiii ( o00OooO0oo )
    oO00O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for oO00O0 in oO00O0 :
     oOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oO00O0 ) )
     for oOo0 in oOo0 :
      oOo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     o00OooO0oo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oO00O0 ) )
     for o00OooO0oo in o00OooO0oo :
      o00OooO0oo = 'https://www.youtube.com/w' + o00OooO0oo
     Oo0oooO0oO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oO00O0 ) )
     for Oo0oooO0oO in Oo0oooO0oO :
      Oo0oooO0oO = 'http:' + Oo0oooO0oO
     OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , i1iIIi1 , '' )
   elif oOo0 in OO0o :
    pass
   elif 'user' in o00OooO0oo or 'elete' in oOo0 :
    pass
   elif 'hannel' in o00OooO0oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + o00OooO0oo
    IIiII = Iiii ( o00OooO0oo )
    i1ii1II1ii = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for I11iiiiI1i , o00OooO0oo , oOo0 in i1ii1II1ii :
     if 'outube' in o00OooO0oo or 'list' in o00OooO0oo :
      pass
     elif 'atch' in o00OooO0oo :
      o00OooO0oo = ( o00OooO0oo ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I11iiiiI1i , 'http:' + I11iiiiI1i , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , Oo0oooO0oO , '' )
    if 28 - 28: Ii1I
def O00OoOO0oo0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( '<a href="(.+?)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( IIiII )
 for url in next :
  url = 'https://www.youtube.com' + url
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + '] NEXT [/COLOR]' , url , 10065 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 for I11iiiiI1i , url , oOo0 , o0o0oOoOO0O , Oo0 in o0O00oOoOO :
  OO0o . append ( oOo0 )
  oO00OOoO00 ( 'tvshows' , 'INFO' )
  Oo0oooO0oO = 'http:' + ( I11iiiiI1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + Oo0oooO0oO
  url = 'http://www.youtube.com' + url
  OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , Oo0oooO0oO , Oo0 )
 else :
  o0O00oOoOO = re . compile ( '<img src="(.+?)" alt=.+?yt-lockup-title "><a href="(.+?)".+?data-sessionlink=.+?" title="(.+?)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
  for I11iiiiI1i , url , oOo0 , o0o0oOoOO0O in o0O00oOoOO :
   oO00OOoO00 ( 'tvshows' , 'INFO' )
   Oo0oooO0oO = 'http:' + ( I11iiiiI1i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    IIiII = Iiii ( url )
    oO00O0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( IIiII )
    for oO00O0 in oO00O0 :
     oOo0 = re . compile ( 'data-video-title="(.+?)"' ) . findall ( str ( oO00O0 ) )
     for oOo0 in oOo0 :
      oOo0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( oO00O0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     Oo0oooO0oO = re . compile ( '<img.+?="(.+?)"' ) . findall ( str ( oO00O0 ) )
     for Oo0oooO0oO in Oo0oooO0oO :
      Oo0oooO0oO = 'http:' + Oo0oooO0oO
     OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , i1iIIi1 , '' )
   elif oOo0 in OO0o :
    pass
   elif 'user' in url or 'elete' in oOo0 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    IIiII = Iiii ( url )
    i1ii1II1ii = re . compile ( 'data-thumb="(.+?)".+?href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
    for I11iiiiI1i , url , oOo0 in i1ii1II1ii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + I11iiiiI1i , 'http:' + I11iiiiI1i , '' )
     else :
      pass
   else :
    OOooOoooOoOo ( '[COLORred]' + o0o0oOoOO0O + '[/COLOR]' + '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO , Oo0oooO0oO , '' )
    if 96 - 96: OOooOOo . I11i - O0oOO0
    if 99 - 99: O00Oo000ooO0 . I1ii11iIi11i - OoOO00O % OoOO00O * o0o00Oo0O . IIiIiII11i
def iIIII1iIIii ( ) :
 if oO == 'insert_password' :
  oOOoo00O0O . ok ( '[COLOR' + oO0o0o0ooO0oO + ']Donators Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided to donators to help with server and stream costs' , 'Donate @ [COLOR' + oO0o0o0ooO0oO + ']http://architects.x10host.com[/COLOR]' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
 else :
  oOOO00o000o = open ( o0 )
  o0O00oOoOO = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( oOOO00o000o ) )
  for iIi11i1 , oO00oo0o00o0o in o0O00oOoOO :
   if iIi11i1 == 'needs replacing' or oO00oo0o00o0o == 'needs replacing' :
    IiIIIIIi ( )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']DONATORS LIST[/COLOR]' , str ( OOO00O ) + '/thelistnew.m3u' , 7080 , OOoOO0oo0ooO + 'GTVIPTV.png' , i1iIIi1 , '' )
  if 11 - 11: ooOoO0O00 % Ii - ooOoO0O00 * OOooOOo
def i1I11IiI1iiII ( ) :
 oooOOOOO . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + Ooo + ")" )
 IiIIIIIi ( )
 oooOOOOO . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 91 - 91: O0oOO0 % O0oOO0
def i1iIiIIIII ( ) :
 try :
  o0ooOoO000oO = gui . TVGuide ( )
  o0ooOoO000oO . doModal ( )
  del o0ooOoO000oO
  if 85 - 85: I11i . OOooOOo / O0oOO0 . o0o00Oo0O % oO00Oo0o000
 except :
  import sys
  import traceback as tb
  ( OO0ooo0oOO , oo000ii , traceback ) = sys . exc_info ( )
  tb . print_exception ( OO0ooo0oOO , oo000ii , traceback )
  if 78 - 78: ii . oO0o + O0oOO0 - ooOoO0O00
def ii1O0 ( ) :
 o0OOOO00O0Oo ( 'Full Backup' , '' , 10061 , OOoOO0oo0ooO + 'FullBackUp.png' , i1iIIi1 , 'Back Up Your Full System' )
 if os . path . exists ( I11iii1Ii ) :
  o0OOOO00O0Oo ( 'Backup Genie Favourites' , o00OooO0oo , 10062 , OOoOO0oo0ooO + 'BackupGenieFavourites.png' , i1iIIi1 , 'Back Up Your favourites' )
 if os . path . exists ( iiiiiIIii ) :
  o0OOOO00O0Oo ( 'Backup Ivue Config' , iiiiiIIii , 10062 , OOoOO0oo0ooO + 'BackUpIvueConfig.png' , i1iIIi1 , 'Back Up Your master.db' )
 if os . path . exists ( O000OO0 ) :
  o0OOOO00O0Oo ( 'Backup Kodi Favourites' , O000OO0 , 10062 , OOoOO0oo0ooO + 'BackKodiFavourites.png' , i1iIIi1 , 'Back Up Your favourites.xml' )
  if 33 - 33: ooOoO0O00
  if 36 - 36: IIiIiII11i % Ii * OOooOOo + Ii1i111I
  if 25 - 25: iI11I1II1I1I % IIiI1I . O0oOO0
zip = o0oO0 . getSetting ( 'zip' )
IIIIi1 = xbmc . translatePath ( os . path . join ( zip ) )
def iIi11iiIiI1I ( ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  oooOOOOO . ok ( '[COLOR=white]Origin[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 89 - 89: IIiI1I - O0oOO0 % I1ii11iIi11i % I11i
  if 49 - 49: I1ii11iIi11i - oOo0O0Ooo / O00Oo000ooO0 / o0o00Oo0O % I11i * OoOO00O
  if 100 - 100: i1IiIIIII . IIiI1I / o0o00Oo0O * ooOoO0O00 * OoOO00O * I1ii11iIi11i
def OO00 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = I11iii1Ii
  elif 'Ivue' in name :
   url = iiiiiIIii
  elif 'Kodi' in name :
   url = O000OO0
  iIi11iiIiI1I ( )
  o0OOo00OoO = open ( url ) . read ( )
  iIi1 = os . path . join ( IIIIi1 , description . split ( 'Your ' ) [ 1 ] )
  OOO = open ( iIi1 , mode = 'w' )
  OOO . write ( o0OOo00OoO )
  OOO . close ( )
 else :
  if 'guisettings.xml' in description :
   i11iiI1111 = open ( os . path . join ( IIIIi1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOoooo000Oo00 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % skin
   o0O00oOoOO = re . compile ( oOoooo000Oo00 ) . findall ( i11iiI1111 )
   for type , OOoo , o00O00oO00 in o0O00oOoOO :
    o00O00oO00 = o00O00oO00 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OOoo , o00O00oO00 ) )
  else :
   iIi1 = os . path . join ( url )
   o0OOo00OoO = open ( os . path . join ( IIIIi1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOO = open ( iIi1 , mode = 'w' )
   OOO . write ( o0OOo00OoO )
   OOO . close ( )
 oooOOOOO . ok ( "[COLOR=white]Origin[/COLOR]" , "" , 'All Done !' , '' )
 if 23 - 23: iI11I1II1I1I * ooOoO0O00 % ii * O00Oo000ooO0
 if 9 - 9: O00Oo000ooO0 - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
 if 39 - 39: O00Oo000ooO0 * I1ii11iIi11i + iI11I1II1I1I - O00Oo000ooO0 + i1IiIIIII
 if 69 - 69: o0o00Oo0O
def o0ooO ( ) :
 OoOOOo0o0ooo = 1
 iIi11iiIiI1I ( )
 I1iiiiI1iI = xbmc . translatePath ( os . path . join ( IIIIi1 , 'Build Backup' , 'Full Backup' , '' ) )
 iIiiiii1i = xbmc . translatePath ( os . path . join ( IIIIi1 , 'Build Backup' , 'my_full_backup.zip' ) )
 iiIi1IIiI = xbmc . translatePath ( os . path . join ( IIIIi1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1iiiiI1iI ) :
  os . makedirs ( I1iiiiI1iI )
 i1oO0OO0 = oOOoo00O0O . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i1oO0OO0 ) : return False , 0
 o0O0Oo00 = i1oO0OO0
 O0Oo0o000oO = xbmc . translatePath ( os . path . join ( I1iiiiI1iI , o0O0Oo00 + '.zip' ) )
 oO0o00oOOooO0 = [ 'plugin.video.GenieTv' ]
 OOOoO000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oOOOO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IiIi1ii111i1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 i1i1i1I = "Creating full backup of existing build"
 oOoo000 = "Creating Community Build"
 OooOo00o = "Archiving..."
 IiI11i1IIiiI = ""
 oOOo000oOoO0 = "Please Wait"
 OoOo00o0OO ( i1iiIII111ii , O0Oo0o000oO , oOoo000 , OooOo00o , IiI11i1IIiiI , oOOo000oOoO0 , oOOOO , IiIi1ii111i1 )
 time . sleep ( 1 )
 ii1IIIIiI11 = xbmc . translatePath ( os . path . join ( I1iiiiI1iI , o0O0Oo00 + '_guisettings.zip' ) )
 iI1IIIii = zipfile . ZipFile ( ii1IIIIiI11 , mode = 'w' )
 try :
  iI1IIIii . write ( xbmc . translatePath ( os . path . join ( i1iiIII111ii , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iI1IIIii . close ( )
 if OoOOOo0o0ooo == 0 :
  oooOOOOO . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  oooOOOOO . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  oooOOOOO . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iIiiiii1i , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O0Oo0o000oO + '[/COLOR]' )
  if 7 - 7: O00Oo000ooO0 - Ii1i111I / IIiIiII11i * OoOO00O . IIiI1I * IIiI1I
def OoOo00o0OO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 O0O0oOOo0O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 II11 = len ( sourcefile )
 O00oooo00o0O = [ ]
 ii1iii1I1I = [ ]
 Oo0oO0ooo . create ( message_header , message1 , message2 , message3 )
 for oO0Ooo0ooOO0 , i1IIiIii1i , ooOOO0OooOo in os . walk ( sourcefile ) :
  for file in ooOOO0OooOo :
   ii1iii1I1I . append ( file )
 I1Ii = len ( ii1iii1I1I )
 for oO0Ooo0ooOO0 , i1IIiIii1i , ooOOO0OooOo in os . walk ( sourcefile ) :
  i1IIiIii1i [ : ] = [ oOO for oOO in i1IIiIii1i if oOO not in exclude_dirs ]
  ooOOO0OooOo [ : ] = [ OOO for OOO in ooOOO0OooOo if OOO not in exclude_files ]
  for file in ooOOO0OooOo :
   O00oooo00o0O . append ( file )
   Ii1II = len ( O00oooo00o0O ) / float ( I1Ii ) * 100
   Oo0oO0ooo . update ( int ( Ii1II ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O0Oo00 = os . path . join ( oO0Ooo0ooOO0 , file )
   if not 'temp' in i1IIiIii1i :
    if not 'plugin.program.originwizard' in i1IIiIii1i :
     import time
     ii1IiIIi1i = '01/01/1980'
     oOOo0OOOOo0Oo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O0Oo00 ) ) )
     if oOOo0OOOOo0Oo > ii1IiIIi1i :
      O0O0oOOo0O . write ( O0Oo00 , O0Oo00 [ II11 : ] )
 O0O0oOOo0O . close ( )
 Oo0oO0ooo . close ( )
 if 67 - 67: O0O0O / IIiI1I . Ii1i111I . iI11I1II1I1I
 if 12 - 12: ii
def ii1iiIi1 ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY STREAMS[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SCOOBY SCRAPES[/COLOR]' , ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , OOoOO0oo0ooO + 'scoob.png' , i1iIIi1 , '' )
 if 34 - 34: i1IiIIIII
 if 91 - 91: iI11I1II1I1I % I11i . iI11I1II1I1I % ooOoO0O00 / IIiIiII11i * OOooOOo
def iioo0o0OoOOO ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH MOVIES[/COLOR]' , str ( OOO00O ) , 9001 , OOoOO0oo0ooO + 'MOVIESv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH SERIES[/COLOR]' , str ( OOO00O ) , 9002 , OOoOO0oo0ooO + 'TVSHOWSv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON' , i1iIIi1 , '' )
 if 88 - 88: IIiI1I
 if 19 - 19: IIiIiII11i * O00Oo000ooO0 + OoOO00O
 if 65 - 65: i1IiIIIII . oO00Oo0o000 . oO0o . IIiI1I - i1IiIIIII
 if 19 - 19: Ii + IIiI1I % O0oOO0
def IIi ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']QuickSilver[/COLOR]' , ( i1111 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9xdWlja3NpbHZlcm11c2ljLw==' ) ) , 1006 , OOoOO0oo0ooO + 'Quicksilver.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC CHANNELS[/COLOR]' , str ( OOO00O ) , 30031 , OOoOO0oo0ooO + 'MusicChannels.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']UK RADIO[/COLOR]' , ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , OOoOO0oo0ooO + 'UKRadio.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']WORLD RADIO[/COLOR]' , str ( OOO00O ) , 1013 , OOoOO0oo0ooO + 'WorldRadio.png' , i1iIIi1 , '' )
 if o0oO0 . getSetting ( 'CONCERTS' ) == 'true' :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CONCERTS[/COLOR]' , ( i1111 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , OOoOO0oo0ooO + 'Concerts.png' , i1iIIi1 , '' )
  if 27 - 27: i1IiIIIII % OoOO00O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC VIDEOS[/COLOR]' , ( i1111 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , OOoOO0oo0ooO + 'MusicVideos.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC[/COLOR]' , str ( OOO00O ) + ( i1111 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , OOoOO0oo0ooO + 'Music.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']MUSIC SEARCH[/COLOR]' , str ( OOO00O ) , 1111 , OOoOO0oo0ooO + 'MusicSearch.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , i1iIIi1 , '' )
 if 58 - 58: i1IiIIIII * I11i + o0o00Oo0O % i1IiIIIII
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 25 - 25: I1ii11iIi11i % Ii1I * O0oOO0
def I11oo0ooOO ( ) :
 I1ii11iI ( )
 if 24 - 24: oO0o % oO0o * iI11I1II1I1I
 OOooOoooOoOo ( 'DELETE CACHE' , 'url' , 14 , OOoOO0oo0ooO + 'DeleteCache.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'DELETE PACKAGES' , 'url' , 6 , OOoOO0oo0ooO + 'DeletePackages.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FORCE REFRESH' , 'url' , 10 , OOoOO0oo0ooO + 'ForceRefresh.png' , i1iIIi1 , 'Force Refresh All Repos' )
 if 50 - 50: oO0o . Ii - O0O0O . O0O0O
 OOooOoooOoOo ( 'CHECK MY IP' , 'url' , 12 , OOoOO0oo0ooO + 'CheckMyIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , OOoOO0oo0ooO + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , i1iIIi1 , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ADVANCED SETTINGS XML[/COLOR]' , str ( OOO00O ) , 4 , OOoOO0oo0ooO + 'AdvancedSettingXML.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']URL FIXES[/COLOR]' , str ( OOO00O ) , 20 , OOoOO0oo0ooO + 'URLFixes.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: i1IiIIIII / I1ii11iIi11i * ooOoO0O00 . OOooOOo
 if 57 - 57: i1IiIIIII + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
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
 if 83 - 83: I11i / Ii % iI11I1II1I1I . Ii1i111I % O0O0O . ii
 if 94 - 94: OoOO00O + iI11I1II1I1I % oO0o
def O0OO0oOOo ( ) :
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
 if 94 - 94: I11i + ii * Ii1i111I - I1ii11iIi11i . O00Oo000ooO0 - I11i
def I1i11IiI11i1 ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Local Zip[/COLOR]' , I11 , 48 , OOoOO0oo0ooO + 'MyLocalZIP.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']My Online Zip[/COLOR]' , i11 , 43 , OOoOO0oo0ooO + 'MyOnlineZip.png' , i1iIIi1 , '' )
 if 87 - 87: O0O0O * O0O0O / oOo0O0Ooo / O0oOO0 % i1IiIIIII
def OooOOO0O00 ( ) :
 I1ii11iI ( )
 OOooOoooOoOo ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( OOO00O ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , OOoOO0oo0ooO + 'FTV4.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( OOO00O ) + '/wizard/customftv/settings.xml' , 17 , OOoOO0oo0ooO + 'FTV3.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , OOoOO0oo0ooO + 'FTV1.png' , i1iIIi1 , '' )
 OOooOoooOoOo ( 'RESET FTV DATABASE' , 'url' , 18 , OOoOO0oo0ooO + 'FTV2.png' , i1iIIi1 , '' )
 if 29 - 29: I11i % iI11I1II1I1I . ii % ii % IIiIiII11i / IIiI1I
 if 70 - 70: Ii % IIiI1I
 if 11 - 11: O00Oo000ooO0 % Ii1I % OoOO00O / IIiIiII11i % oO00Oo0o000 - I1ii11iIi11i
def OOooO ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SKINS[/COLOR]' , str ( OOO00O ) , 33 , OOoOO0oo0ooO + 'Skins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ARTWORK PACKS[/COLOR]' , str ( OOO00O ) , 34 , OOoOO0oo0ooO + 'ArtworkPacks.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CREATE UNIVERSAL PATHS[/COLOR]' , i1iiIII111ii , 35 , OOoOO0oo0ooO + 'CreateUniversalPath.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 79 - 79: oO00Oo0o000 % O0O0O % I11i % OoOO00O - IIiIiII11i * ii
def oOOO ( url ) :
 O00oO = Iiii ( ooo0oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 5 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 62 - 62: Ii1I + OoOO00O + ooOoO0O00 / ii
def IIiiii ( ) :
 I1ii11iI ( )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']GOTHAM SKINS[/COLOR]' , str ( OOO00O ) , 36 , OOoOO0oo0ooO + 'GothamSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']HELIX SKINS[/COLOR]' , str ( OOO00O ) , 37 , OOoOO0oo0ooO + 'HelixSkins.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']ISENGAARD SKINS[/COLOR]' , i1iiIII111ii , 38 , OOoOO0oo0ooO + 'IsengaardSkins.png' , i1iIIi1 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 37 - 37: I11i % O0oOO0
def O0II11i11II ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + II1Ii1iI1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 54 - 54: o0o00Oo0O
def OOoO000O00oO ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + i1OoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 44 - 44: i1IiIIIII
def O0O0o0o0o ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + IIIIIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 80 - 80: iI11I1II1I1I * oO00Oo0o000 % Ii1i111I % I1ii11iIi11i
def OooOO0o0 ( url ) :
 O00oO = Iiii ( i1111 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 91 - 91: O0O0O + ii - ooOoO0O00
def o000 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OOooo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 40 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 34 - 34: i1IiIIIII
def IiIIiIIIiIii ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + I1i11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 5 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 31 - 31: O0O0O / O00Oo000ooO0 * I11i . IIiIiII11i
def oooOO0OO0O ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK (Android only)[/COLOR]' , str ( OOO00O ) , 2 , OOoOO0oo0ooO + 'APKAndroidOnly.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']APK Search[/COLOR]' , str ( OOO00O ) , 30038 , OOoOO0oo0ooO + 'APKSearch.png' , i1iIIi1 , '' )
 if 78 - 78: OoOO00O / IIiIiII11i % OOooOOo
def oO00OoOO ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy5hcGtjcmFmdC5jb20v' ) )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Android Apps</a>' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'href="(.+?)">Android Games</a>' ) . findall ( O0OOoOOO0oO )
 I11IIiIiI = re . compile ( 'href="(.+?)">Wallpapers</a>' ) . findall ( O0OOoOOO0oO )
 iIIIi1i1I11i = re . compile ( 'href="(.+?)">Widgets</a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo in o0O00oOoOO :
  oOO0OO0OO ( 'Android Apps' , o00OooO0oo , 30035 , OOoOO0oo0ooO + 'apps.png' )
 for o00OooO0oo in iIIi1i1 :
  oOO0OO0OO ( 'Android Games' , o00OooO0oo , 30035 , OOoOO0oo0ooO + 'GAMES.png' )
 for o00OooO0oo in I11IIiIiI :
  oOO0OO0OO ( 'Wallpapers' , o00OooO0oo , 30036 , OOoOO0oo0ooO + 'wallpapers.png' )
 for o00OooO0oo in iIIIi1i1I11i :
  oOO0OO0OO ( 'Widgets' , o00OooO0oo , 30036 , OOoOO0oo0ooO + 'widgets.png' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
def oOOoooO ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  if 'cat' in url :
   oOO0OO0OO ( oOo0 , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def i1ii11 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'src="(.+?)".+?href="(.+?)" title ="(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'class="pagination_next"><a href="(.+?)">»</a></li>' ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i , url , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , url , 30037 , I11iiiiI1i )
 for url in iIIi1i1 :
  oOO0OO0OO ( 'NEXT PAGE' , url , 30036 , OOoOO0oo0ooO + 'APK.png' )
def ii1i ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '>Direct Download : <a  href="(.+?)">' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  IIioo0OO ( url )
def IIioo0OO ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">Download APK from APKCRAFT</a></p>' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  IiiI11i1I ( url )
def OOo0 ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1 = 'http://www.apkcraft.com/search/app/?search_text=' + ( OO0oo ) . replace ( ' ' , '+' ) + '&search_type=1'
 OOO0000oO = Iii1 . lower ( )
 i1ii11 ( OOO0000oO )
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
def IiiI11i1I ( url ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( OooOOo0 , 'Download' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 ooO000O = os . path . join ( IiiioooOOoooo , oOo0 + '.apk' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 53 - 53: I11i . IIiI1I / OoOO00O
def I11iiIi1i1 ( url ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 ooO000O = os . path . join ( IiiioooOOoooo , oOo0 + '.mp4' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 41 - 41: OoOO00O % Ii1I
 if 12 - 12: i1IiIIIII
def ooOo0O ( name , url , description ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://architects.x10host.com' )
 ooO000O = os . path . join ( IiiioooOOoooo , name )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 i1I1IIIiiI = xbmc . translatePath ( os . path . join ( oo00 ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print i1I1IIIiiI
 print '======================================='
 extract . all ( ooO000O , i1I1IIIiiI , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 71 - 71: i1IiIIIII * oO0o % ii % oO0o / oOo0O0Ooo
 if 56 - 56: ii % Ii * iI11I1II1I1I . oO0o * o0o00Oo0O
def iI ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 5 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 99 - 99: Ii1i111I - oO00Oo0o000 - O0O0O % oO0o
 if 21 - 21: IIiIiII11i % Ii1I . ooOoO0O00 - ii
def iiOOOO0o ( url ) :
 O00oO = Iiii ( OOO00O + ( i1111 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 30015 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 10 - 10: oO00Oo0o000 % oOo0O0Ooo
def oo0OoOooo ( url , iconimage , fanart ) :
 O00oO = Iiii ( url )
 Oo0o0O00 = url
 I11iiiiI1i = iconimage
 fanart = fanart
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for I1IiI11 , oOo0 in o0O00oOoOO :
  if '.mp4' in oOo0 :
   OOooOoooOoOo ( 'Watch VIDEO' , url + '/' + I1IiI11 , 222 , I11iiiiI1i , fanart , '' )
  if 'description' in oOo0 :
   OOooOoooOoOo ( 'Read Description' , url + '/' + I1IiI11 , 30017 , I11iiiiI1i , fanart , '' )
  if 'images' in oOo0 :
   o0OOOO00O0Oo ( 'View Images' , url + '/' + I1IiI11 , 30018 , I11iiiiI1i , fanart , '' )
  if 'url' in oOo0 :
   OOooOoooOoOo ( 'Install Build On Android' , url + '/' + I1IiI11 , 30016 , I11iiiiI1i , fanart , '' )
  if 'url' in oOo0 :
   OOooOoooOoOo ( 'Install Build On Pc' , url + '/' + I1IiI11 , 30019 , I11iiiiI1i , fanart , '' )
 oO00OOoO00 ( 'movies' , 'INFO' )
 if 95 - 95: O00Oo000ooO0 * Ii1I % O0oOO0 % OoOO00O - OoOO00O
def oOoooO0 ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  o0Oo0 ( url )
  if 25 - 25: i1IiIIIII
def oOO0o000Oo00o ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url="(.+?)"' ) . findall ( O00oO )
 for url in o0O00oOoOO :
  iii11II1I ( url )
  if 5 - 5: OOooOOo - O00Oo000ooO0 * O00Oo000ooO0
def IiiIi1IIII1i ( url ) :
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'desc="(.+?)"' ) . findall ( O00oO )
 for O0ooOoO in o0O00oOoOO :
  o00oO0oo0OO ( 'Description:' , O0ooOoO )
  if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + Ii1i111I
def IiiIi ( url ) :
 O00oO = Iiii ( url )
 url = url
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O00oO )
 for I1IiI11 , oOo0 in o0O00oOoOO :
  if 'png' in oOo0 :
   OOooOoooOoOo ( 'image' , '' , '' , url + '/' + I1IiI11 , url + '/' + I1IiI11 , '' )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 10 - 10: oO0o / I1ii11iIi11i
def I1i ( name , url , description ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ooO000O = os . path . join ( IiiioooOOoooo , name + '.zip' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II11iIII1i1I
 print '======================================='
 extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i1I1IiiIi1i ( )
 if 63 - 63: I1ii11iIi11i + oO00Oo0o000 - IIiIiII11i
 if 2 - 2: O00Oo000ooO0
def iii11II1I ( url ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooO000O = os . path . join ( IiiioooOOoooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II11iIII1i1I
 print '======================================='
 extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
 oOo0O0O0 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOoo0 ( )
 if 34 - 34: IIiI1I - ii . oOo0O0Ooo / IIiIiII11i
def o0Oo0 ( url ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooO000O = os . path . join ( IiiioooOOoooo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II11iIII1i1I
 print '======================================='
 extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
 oOo0O0O0 ( url )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 27 - 27: oO0o / I1ii11iIi11i * O0oOO0 - oO0o
 if 19 - 19: Ii1i111I
def Ooooo0OoO0 ( name , url , description ) :
 II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 ooO000O = os . path . join ( I11 )
 time . sleep ( 2 )
 Oo0oO0ooo . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print II11iIII1i1I
 print '======================================='
 extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 if 9 - 9: i1IiIIIII . O00Oo000ooO0
 if 31 - 31: O0O0O / iI11I1II1I1I
def oOoo0 ( ) :
 OooooOOoo0 = xbmcgui . Dialog ( ) . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if OooooOOoo0 == 0 :
  return
 elif OooooOOoo0 == 1 :
  pass
 o0oO0OoO0 = oOOOOOoOO ( )
 print "Platform: " + str ( o0oO0OoO0 )
 if o0oO0OoO0 == 'osx' :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  oooOOOOO . ok ( "[COLOR=red][B]WARNING  !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif o0oO0OoO0 == 'linux' :
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
 elif o0oO0OoO0 == 'android' :
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
 elif o0oO0OoO0 == 'windows' :
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
  if 81 - 81: IIiIiII11i + Ii / IIiI1I
def oOOOOOoOO ( ) :
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
  if 85 - 85: Ii + oO00Oo0o000 * OOooOOo
  if 1 - 1: ooOoO0O00 / I1ii11iIi11i . oO0o
  if 57 - 57: Ii1i111I . I1ii11iIi11i + IIiIiII11i
def i111i11I1ii ( url ) :
 Oo0oO0ooo . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( url ) :
  for file in ooOOO0OooOo :
   if file . endswith ( ".xml" ) :
    Oo0oO0ooo . update ( 0 , "Fixing" , file , 'Please Wait' )
    i11iiI1111 = open ( ( os . path . join ( OOooo , file ) ) ) . read ( )
    oo0 = i11iiI1111 . replace ( i1iiIII111ii , 'special://home/' )
    OOO = open ( ( os . path . join ( OOooo , file ) ) , mode = 'w' )
    OOO . write ( str ( oo0 ) )
    OOO . close ( )
 oOoo0 ( )
 if 73 - 73: OOooOOo . oOo0O0Ooo
def II1i11i1iIi11 ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a></td></tr>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , 'http://www.listenlive.eu/' + o00OooO0oo , 10111113 , OOoOO0oo0ooO + 'radio.png' )
def oo0O0oO0O0O ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , url in o0O00oOoOO :
  oOo0O ( oOo0 , url , 222 , OOoOO0oo0ooO + 'radio.png' )
  if 26 - 26: O00Oo000ooO0 / ooOoO0O00 * O0O0O . oOo0O0Ooo
def i1i ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" style="font-size:.8em;">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.toonjet.com/' + o00OooO0oo , 8051 , OOoOO0oo0ooO + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIiiiI ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"><img src="(.+?)"' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( '<a href="(.+?)">.+?</a></td></tr></table>' ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i in o0O00oOoOO :
  if 'ol.gif' in I11iiiiI1i :
   pass
  elif 'link_block_' in I11iiiiI1i :
   pass
  elif '.png' in I11iiiiI1i :
   pass
  else :
   oOO0OO0OO ( ( I11iiiiI1i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , OOoOO0oo0ooO + 'vod.png' )
 for url in iIIi1i1 :
  oOO0OO0OO ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , OOoOO0oo0ooO + 'Next.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO00oo00 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<iframe width="640" height="480" src="(.+?)" frameborder="0" allowfullscreen></iframe>' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , OOoOO0oo0ooO + 'classictoons.png' )
  if 76 - 76: ii + I1ii11iIi11i % O00Oo000ooO0 . oO0o + IIiIiII11i
  if 70 - 70: oOo0O0Ooo / Ii1i111I
def IIiiiiIiIIii ( ) :
 O0OO ( 'Audio Books' , '' , 30011 , OOoOO0oo0ooO + 'AudioBooks.png' , OOoOO0oo0ooO + 'AudioBooks.png' , '' )
 O0OO ( 'Kids Audio Books' , '' , 30006 , OOoOO0oo0ooO + 'KidsAudioBooks.png' , OOoOO0oo0ooO + 'KidsAudioBooks.png' , '' )
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
def I1ii1II1iII ( ) :
 O0OO ( 'All' , '' , 30001 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 O0OO ( 'Popular' , '' , 30012 , OOoOO0oo0ooO + 'POPULARv.png' , OOoOO0oo0ooO + 'POPULARv.png' , '' )
 O0OO ( 'Search' , '' , 30013 , OOoOO0oo0ooO + 'Search.png' , OOoOO0oo0ooO + 'Search.png' , '' )
 if 8 - 8: OOooOOo / o0o00Oo0O * o0o00Oo0O % oO00Oo0o000 - I1ii11iIi11i + Ii1i111I
def ooIi1IiIiIi1IiI ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for oOo0 , o00OooO0oo , i1iiIIi1I in o0O00oOoOO :
  if 'Parent' in oOo0 :
   pass
  elif '2' in i1iiIIi1I :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: oOo0O0Ooo * I1ii11iIi11i
def oOOo00o0OO ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for oOo0 , o00OooO0oo , i1iiIIi1I in o0O00oOoOO :
  if OO0oo in oOo0 . lower ( ) :
   if '1' in i1iiIIi1I :
    O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '2' in i1iiIIi1I :
    O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   elif '3' in i1iiIIi1I :
    O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * i1IiIIIII % IIiIiII11i
    if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
def II1 ( ) :
 IIiII = Iiii ( II11iiii1Ii + 'books' + OooO0 )
 o0O00oOoOO = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( IIiII )
 for oOo0 , o00OooO0oo , i1iiIIi1I in o0O00oOoOO :
  if '1' in i1iiIIi1I :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 3010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '2' in i1iiIIi1I :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '3' in i1iiIIi1I :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , o00OooO0oo , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 74 - 74: ii % i1IiIIIII % oO00Oo0o000 - oOo0O0Ooo - Ii1i111I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: o0o00Oo0O
def oO00oOOo0Oo ( url ) :
 I1IiI11 = url
 IIiII = Iiii ( url )
 iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
 for url , oOo0 in iIIi1i1 :
  if 'mp3' in oOo0 :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1IiI11 + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'wma' in oOo0 :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1IiI11 + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in oOo0 :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1IiI11 + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif '/' in oOo0 :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1IiI11 + url , 30009 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 5 - 5: I11i . o0o00Oo0O / I1ii11iIi11i % oO0o
   if 60 - 60: IIiIiII11i / iI11I1II1I1I + Ii1I . Ii
   if 40 - 40: I11i
def oOOo0oo0o0o0 ( url ) :
 IIiII = Iiii ( url )
 I1IiI11 = url
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  if 'Parent' in oOo0 :
   pass
  elif '.db' in oOo0 :
   pass
  elif '.jpg' in oOo0 :
   pass
  elif '.html' in oOo0 :
   pass
  elif '.doc' in oOo0 :
   pass
  elif 'mp3' in oOo0 :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1IiI11 + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in oOo0 :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1IiI11 + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1IiI11 + url , 30010 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 43 - 43: Ii1I / oOo0O0Ooo . O0oOO0
   if 62 - 62: iI11I1II1I1I + IIiI1I . I1ii11iIi11i / O00Oo000ooO0 % o0o00Oo0O . oO00Oo0o000
def Oo0oOooOoOo ( ) :
 O0OO ( 'A-Z' , '' , 30007 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 O0OO ( 'All' , '' , 30003 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 O0OO ( 'Search' , '' , 30014 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
 if 49 - 49: i1IiIIIII . Ii1I . Ii - IIiIiII11i / OoOO00O
def ooOo0O0o0 ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( IIiII )
 for o00OooO0oo , I11iiiiI1i in o0O00oOoOO :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + o00OooO0oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in I11iiiiI1i :
   pass
  else :
   O0OO ( I11iiiiI1i , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( o00OooO0oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + I11iiiiI1i + '.gif' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 65 - 65: O0oOO0 + o0o00Oo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: ii - OOooOOo - Ii * I11i / I1ii11iIi11i + ii
 if 35 - 35: ooOoO0O00 - I11i * IIiI1I
def O0oOoo0OoO0O ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  if '</a>' in oOo0 :
   pass
  elif '(' in oOo0 :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: ii / O0oOO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: ooOoO0O00 - iI11I1II1I1I
def Oo0Oo00o00oO ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if OO0oo in oOo0 . lower ( ) :
   if '</a>' in oOo0 :
    pass
   elif '(' in oOo0 :
    O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o00OooO0oo , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   else :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o00OooO0oo , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
    if 95 - 95: oOo0O0Ooo
    if 88 - 88: O00Oo000ooO0 % oO0o + oO00Oo0o000 + oO00Oo0o000 * IIiIiII11i
def o0Oo ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 o0O00oOoOO = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if '</a>' in oOo0 :
   pass
  elif '(' in oOo0 :
   O0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o00OooO0oo , 30005 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + o00OooO0oo , 30004 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: i1IiIIIII / I1ii11iIi11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: O0O0O - I1ii11iIi11i % O00Oo000ooO0
 if 50 - 50: ii
def IiI1i111IiIiIi1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">Download</a></b></td>' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  I1IiI11 = ( i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1IiI11 )
  if 39 - 39: Ii1i111I - Ii1I
def OOO0o0OO0OO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td width="247">(.*?)</td>.*?<a href="(.+?)">' , re . DOTALL ) . findall ( IIiII )
 for oOo0 , url in o0O00oOoOO :
  if '<p align' in oOo0 :
   pass
  elif '&nbsp;' in oOo0 :
   pass
  else :
   o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i1111 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , OOoOO0oo0ooO + 'KodibleAudioBooks.png' , '' )
   if 64 - 64: IIiIiII11i
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: OOooOOo % oO0o
 if 62 - 62: I11i
def I1i111i ( ) :
 IIiII = cloudflare . source ( i1111 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 o0O00oOoOO = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'ongoing' in o00OooO0oo :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 21005 , OOoOO0oo0ooO + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in o00OooO0oo :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 21005 , OOoOO0oo0ooO + 'CartoonShows.png' , '' , '' )
  if 'disney' in o00OooO0oo :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 21005 , OOoOO0oo0ooO + 'Disney.png' , '' , '' )
  if 'genre' in o00OooO0oo :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 21005 , OOoOO0oo0ooO + 'Genre.png' , '' , '' )
  if 'years' in o00OooO0oo :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 21005 , OOoOO0oo0ooO + 'Years.png' , '' , '' )
def iI1i ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 i111iiIIII = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( IIiII )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , I11iiiiI1i , I11iiiiI1i , oOo0 )
 for url , oOo0 in i111iiIIII :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in next :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
def OOO00OOo0o0Oo ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( IIiII )
 ooooOoO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 IIIIIIII = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( IIiII )
 oOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url in IIIIIIII :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY[/COLOR]' , 'http:' + url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 for url , oOo0 in ooooOoO0O :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
 else :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
def Oo0oOo0O0O0o ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'watchcartoons.png' , '' , '' )
  if 46 - 46: o0o00Oo0O * I1ii11iIi11i / o0o00Oo0O + oO0o
def o0o ( ) :
 oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']CARTOONS[/COLOR]' , '' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']ANIME[/COLOR]' , 'https://kissanime.to/AnimeList' , 20001 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 53 - 53: O0O0O % Ii1i111I . O0oOO0 - OOooOOo
def OoOoO0OoOOOOo ( ) :
 oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']BY NAME[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20002 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']BY GENRE[/COLOR]' , 'http://kisscartoon.me/CartoonList' , 20003 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
 if 61 - 61: Ii * O0O0O . IIiI1I . O0oOO0 % oO0o
def Iiii1iIii ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  if '?c=' in url :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 69 - 69: O0O0O % ii . oOo0O0Ooo
def I1III1II1I11 ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'href="(.+?)" title="(.+?)">/n(.+?)</a><br/>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi11 , oOo0 in o0O00oOoOO :
  if 'Genre' in url :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' )
   if 89 - 89: IIiIiII11i * O0oOO0 . O0O0O
def OO000o ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi11 , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi11 )
  if 4 - 4: ooOoO0O00 + O0oOO0 + ooOoO0O00
def i11IiIIi11I ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<img width="120" height="165" src="(.+?)" style=.+?<a class="bigChar" href="(.+?)">(.+?)</a>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( IIiII )
 for url , IIi11 , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://kisscartoon.me' + url , 20005 , img , '' , IIi11 )
  if 78 - 78: O00Oo000ooO0
  if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % oO00Oo0o000 . Ii1I % o0o00Oo0O
  if 47 - 47: I11i
  if 66 - 66: oOo0O0Ooo - O00Oo000ooO0
  if 33 - 33: oOo0O0Ooo / oO0o
def iiIIi ( ) :
 if 36 - 36: Ii1i111I . IIiIiII11i
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Cartoons[/COLOR]' , i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Cartoons[/COLOR]' , '' , 10005 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 if 25 - 25: O0O0O
def iI1 ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 11 - 11: oO0o
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( IIiII )
 if 18 - 18: IIiI1I - O0O0O % IIiI1I / Ii1i111I
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if OO0oo in oOo0 . lower ( ) :
   if 'Dad!' in oOo0 :
    pass
   elif 'Family Guy' in oOo0 :
    pass
   elif '2 Stupid' in oOo0 :
    pass
   elif 'The Zelfs' in oOo0 :
    pass
   elif 'A Clone' in oOo0 :
    pass
   elif 'A.T.O.M' in oOo0 :
    pass
   elif 'Almost Naked' in oOo0 :
    pass
   elif 'Angry Kid' in oOo0 :
    pass
   elif 'Annoying Orange' in oOo0 :
    pass
   elif 'Aqua Teen' in oOo0 :
    pass
   elif 'Assy Mcgee' in oOo0 :
    pass
   elif 'Astroblast' in oOo0 :
    pass
   elif 'Atomic Betty' in oOo0 :
    pass
   elif 'Axe Cop' in oOo0 :
    pass
   elif 'Baby Playpen' in oOo0 :
    pass
   elif 'Beavis and Butt' in oOo0 :
    pass
   elif 'Celebrity Deathmatch' in oOo0 :
    pass
   elif 'Clerks The' in oOo0 :
    pass
   elif 'Crapston Villas' in oOo0 :
    pass
   elif 'Duckman:' in oOo0 :
    pass
   elif 'Stripperella' in oOo0 :
    pass
   elif 'Vixen' in oOo0 :
    pass
   else :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
    if 68 - 68: OoOO00O * iI11I1II1I1I + oO00Oo0o000 % OOooOOo
    if 46 - 46: OOooOOo % ooOoO0O00 / O0O0O * I1ii11iIi11i * i1IiIIIII
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 67 - 67: OOooOOo * OOooOOo . OOooOOo + OoOO00O / O0O0O
def i1iI1IIIII1 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  if 'Dad!' in oOo0 :
   pass
  elif 'Family Guy' in oOo0 :
   pass
  elif '2 Stupid' in oOo0 :
   pass
  elif 'The Zelfs' in oOo0 :
   pass
  elif 'A Clone' in oOo0 :
   pass
  elif 'A.T.O.M' in oOo0 :
   pass
  elif 'Almost Naked' in oOo0 :
   pass
  elif 'Angry Kid' in oOo0 :
   pass
  elif 'Annoying Orange' in oOo0 :
   pass
  elif 'Aqua Teen' in oOo0 :
   pass
  elif 'Assy Mcgee' in oOo0 :
   pass
  elif 'Astroblast' in oOo0 :
   pass
  elif 'Atomic Betty' in oOo0 :
   pass
  elif 'Axe Cop' in oOo0 :
   pass
  elif 'Baby Playpen' in oOo0 :
   pass
  elif 'Beavis and Butt' in oOo0 :
   pass
  elif 'Celebrity Deathmatch' in oOo0 :
   pass
  elif 'Clerks The' in oOo0 :
   pass
  elif 'Crapston Villas' in oOo0 :
   pass
  elif 'Duckman:' in oOo0 :
   pass
  elif 'Stripperella' in oOo0 :
   pass
  elif 'Vixen' in oOo0 :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'ORIGINCARTOON.png' , i1iIIi1 , '' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: Ii1I % oO0o % OoOO00O
def oo0OOOOO0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i in iIIi1i1 :
  IiOOOo00 = I11iiiiI1i
 I11IIiIiI = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( O0OOoOOO0oO )
 for url in I11IIiIiI :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , url , 10006 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 10007 , IiOOOo00 )
  if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
  if 69 - 69: oO00Oo0o000 - oOo0O0Ooo
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: oOo0O0Ooo * Ii . O0oOO0
def iIIi1 ( url , IMAGE ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( O0OOoOOO0oO )
 for oOo0 , url in o0O00oOoOO :
  print oOo0 + '     ' + url
  if 'easy' in url :
   o0o0OoOOOOOo ( url )
   if 39 - 39: ii * i1IiIIIII * o0o00Oo0O . Ii1i111I . oO0o + O0oOO0
   if 9 - 9: OOooOOo + O0O0O % ii + I11i
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 56 - 56: ii + Ii1I - IIiI1I
def o0o0OoOOOOOo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  III1I1 ( url )
  if 12 - 12: iI11I1II1I1I % O0oOO0 % O0oOO0
  if 78 - 78: O00Oo000ooO0 . OOooOOo . Ii1i111I
  if 97 - 97: O0O0O
def oOoO0O00oo ( ) :
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / IIiI1I * O0O0O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Stand Up[/COLOR]' , '' , 10014 , OOoOO0oo0ooO + 'StandUp.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Comedian[/COLOR]' , '' , 10015 , OOoOO0oo0ooO + 'SearchComedian.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Others[/COLOR]' , '' , 10017 , OOoOO0oo0ooO + 'Others.png' , i1iIIi1 , '' )
 if 29 - 29: I11i
def oo0iIiI ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( IIiII )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  if 'elete' in oOo0 :
   pass
  else :
   oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 222 , I11iiiiI1i )
   if 81 - 81: OOooOOo % OoOO00O
def oo0i1iIIi1II1iiI ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 III1Ii1i1I1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , O0O00OooO , i1iII1IiiIiI1 in III1Ii1i1I1 :
  for OO0oo in O0O00OooO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I1IiI1iI11 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for o00OooO0oo , oOo0 in I1IiI1iI11 :
    if 'tube' in o00OooO0oo :
     pass
    elif 'stage' in o00OooO0oo :
     oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + O0O00OooO + '   -   ' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iiiiI1i , )
    elif 'vee' in o00OooO0oo :
     pass
     if 2 - 2: iI11I1II1I1I
def iiii1 ( ) :
 IIiII = Iiii ( ( i1111 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 III1Ii1i1I1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , O0O00OooO , i1iII1IiiIiI1 in III1Ii1i1I1 :
  I1IiI1iI11 = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for o00OooO0oo , oOo0 in I1IiI1iI11 :
   if 'tube' in o00OooO0oo :
    pass
   elif 'stage' in o00OooO0oo :
    oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + O0O00OooO + '   -   ' + oOo0 + '[/COLOR]' , ( o00OooO0oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + I11iiiiI1i )
   elif 'vee' in o00OooO0oo :
    pass
    if 66 - 66: O0O0O * iI11I1II1I1I % iI11I1II1I1I * O00Oo000ooO0 - O0oOO0 - O00Oo000ooO0
    if 70 - 70: oO00Oo0o000 + O0O0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: oO00Oo0o000 + OoOO00O
def i1i1 ( url ) :
 IIiII = Iiii ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOoO0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( IIiII )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOoO0 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOoO0 :
  III1I1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 27 - 27: oO00Oo0o000 + ii - OOooOOo
  if 15 - 15: O0O0O / Ii1i111I * o0o00Oo0O . IIiIiII11i - oO0o
  if 90 - 90: O0O0O
  if 94 - 94: Ii1i111I / Ii1I * oO00Oo0o000 - OOooOOo
  if 44 - 44: OoOO00O % Ii - IIiI1I * Ii1I + I1ii11iIi11i * i1IiIIIII
  if 41 - 41: o0o00Oo0O * O0oOO0 - OOooOOo . OoOO00O
  if 65 - 65: I1ii11iIi11i . ii
def OOoO0oo0O ( ) :
 if 49 - 49: I11i
 II1ii1ii11I1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , i1iIIi1 , '' )
 II1ii1ii11I1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 88 - 88: Ii1I
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 93 - 93: iI11I1II1I1I
def oo0oooo0OoO0o ( ) :
 II1ii1ii11I1 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 II1ii1ii11I1 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , i1iIIi1 , '' )
 if 50 - 50: IIiI1I / IIiI1I + i1IiIIIII * O0oOO0 / Ii1I
 oO00OOoO00 ( 'movies' , 'MAIN' )
def I1IIiiI1II1 ( ) :
 if 5 - 5: IIiI1I
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 OO = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 1 - 1: i1IiIIIII . O00Oo000ooO0
 for I1iIII1IiiI in OO :
  OOoooOoO0Oo = OOO00 + I1iIII1IiiI + OooO0
  IIiII = i1I1iI ( OOoooOoO0Oo )
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( IIiII )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , III1ii1I , oOo0 in o0O00oOoOO :
   if OO0oo in oOo0 . lower ( ) :
    Oo000 ( oOo0 , o00OooO0oo , 222 , oOoOoOoo0 , III1ii1I , I11i1II )
    if 48 - 48: Ii % O0O0O
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 29 - 29: IIiI1I + Ii % Ii1i111I
    if 93 - 93: OOooOOo % iI11I1II1I1I
def Ooo0o0oo0 ( ) :
 if 87 - 87: OOooOOo / O00Oo000ooO0 + iI11I1II1I1I
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 OO = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 93 - 93: iI11I1II1I1I + O0O0O % O0oOO0
 for I1iIII1IiiI in OO :
  iii1IiI1I1 = OOO00 + I1iIII1IiiI + OooO0
  IIiII = i1I1iI ( iii1IiI1I1 )
  o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( IIiII )
  for oOo0 , I11i1II , o00OooO0oo , I11iiiiI1i , III1ii1I , O00o in o0O00oOoOO :
   if OO0oo in oOo0 . lower ( ) :
    II1ii1ii11I1 ( oOo0 , o00OooO0oo , O00o , I11iiiiI1i , III1ii1I , I11i1II )
    if 86 - 86: Ii1I * IIiIiII11i * Ii1i111I
    oO00OOoO00 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 74 - 74: Ii1I / O00Oo000ooO0
    if 60 - 60: Ii1I
def IIoO00OoOo ( ) :
 if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + O00Oo000ooO0 % Ii % OOooOOo
 O0OOoOOO0oO = Iiii ( OOO00 + 'spongemain.php' )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , I11i1II , o00OooO0oo , I11iiiiI1i , III1ii1I , O00o in o0O00oOoOO :
  II1ii1ii11I1 ( oOo0 , o00OooO0oo , O00o , I11iiiiI1i , III1ii1I , I11i1II )
  oO00OOoO00 ( 'movies' , 'MAIN' )
def O0OOO0 ( url ) :
 if 8 - 8: Ii / IIiIiII11i + I11i * OoOO00O % O00Oo000ooO0 . Ii1i111I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1iIIIiIi1 = ( '%s%s' % ( IiI1 , url ) )
 O00oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , oOoOoOoo0 , I11i1II , O0oO , oOo0 in o0O00oOoOO :
  Oo000 ( oOo0 , url , 222 , oOoOoOoo0 , O0oO , I11i1II )
  if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - i1IiIIIII % I11i
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 30 - 30: oO00Oo0o000 % oO00Oo0o000 % O00Oo000ooO0 . OOooOOo
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: O0oOO0 / IIiIiII11i . OOooOOo % I11i * IIiIiII11i - O0oOO0
  if 55 - 55: oOo0O0Ooo
def Ii1i1 ( url ) :
 if 65 - 65: O0O0O + Ii1I / i1IiIIIII
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , I11i1II , url , I11iiiiI1i , III1ii1I , O00o in o0O00oOoOO :
  II1ii1ii11I1 ( oOo0 , url , O00o , I11iiiiI1i , III1ii1I , I11i1II )
  if 85 - 85: iI11I1II1I1I / ii % IIiIiII11i
  oO00OOoO00 ( 'movies' , 'MAIN' )
  if 49 - 49: Ii % OOooOOo + oO00Oo0o000 . IIiIiII11i % IIiI1I * i1IiIIIII
  if 67 - 67: ooOoO0O00
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: IIiIiII11i . ii
def Oo000 ( name , url , mode , iconimage , fanart , description ) :
 if 57 - 57: oOo0O0Ooo
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O000oOo . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = False )
 return i1i1Ii11Ii
 if 41 - 41: o0o00Oo0O + O0O0O . ooOoO0O00 - IIiIiII11i * I11i . oO0o
def II1ii1ii11I1 ( name , url , mode , iconimage , fanart , description ) :
 if 68 - 68: I11i
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O000oOo . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = True )
 return i1i1Ii11Ii
if 20 - 20: oO00Oo0o000 - oO00Oo0o000
if 37 - 37: O00Oo000ooO0
if 37 - 37: I1ii11iIi11i / O00Oo000ooO0 * o0o00Oo0O
if 73 - 73: IIiI1I * IIiI1I / O0oOO0
if 43 - 43: Ii1I . ooOoO0O00 . O00Oo000ooO0 + o0o00Oo0O * OoOO00O * o0o00Oo0O
if 41 - 41: Ii1I + OoOO00O % ii . Ii1I + IIiI1I . IIiI1I
if 31 - 31: Ii + IIiIiII11i . IIiI1I * OOooOOo
if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
if 87 - 87: i1IiIIIII + I11i . IIiI1I - ii
if 6 - 6: iI11I1II1I1I * ii
if 28 - 28: I1ii11iIi11i * I11i / oO00Oo0o000
if 52 - 52: o0o00Oo0O / I11i % IIiI1I * oOo0O0Ooo % i1IiIIIII
if 69 - 69: Ii1I
if 83 - 83: I11i
if 38 - 38: oO00Oo0o000 + ii . ooOoO0O00
def I1III1iIi ( string ) :
 if IIIii1II1II == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 82 - 82: oOo0O0Ooo + IIiI1I + Ii1I * oOo0O0Ooo % Ii % IIiI1I
def Iii ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1i11ii1Ii = [ ]
 try :
  if 12 - 12: i1IiIIIII . OoOO00O
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iIi1ii1I1 ) == False :
  I1III1iIi ( 'Making Favorites File' )
  i1i11ii1Ii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i11iiI1111 = open ( iIi1ii1I1 , "w" )
  i11iiI1111 . write ( json . dumps ( i1i11ii1Ii ) )
  i11iiI1111 . close ( )
 else :
  I1III1iIi ( 'Appending Favorites' )
  i11iiI1111 = open ( iIi1ii1I1 ) . read ( )
  O0oOI1IiI1iIiIiii = json . loads ( i11iiI1111 )
  O0oOI1IiI1iIiIiii . append ( ( name , url , iconimage , fanart , mode ) )
  oo0 = open ( iIi1ii1I1 , "w" )
  oo0 . write ( json . dumps ( O0oOI1IiI1iIiIiii ) )
  oo0 . close ( )
  if 29 - 29: O0oOO0 - ooOoO0O00 . Ii1i111I - Ii1I + O0oOO0 + ii
  if 36 - 36: ooOoO0O00 / O0oOO0 . iI11I1II1I1I
def i1IiiiiIi1I ( ) :
 if os . path . exists ( iIi1ii1I1 ) == False :
  i1i11ii1Ii = [ ]
  I1III1iIi ( 'Making Favorites File' )
  i1i11ii1Ii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  i11iiI1111 = open ( iIi1ii1I1 , "w" )
  i11iiI1111 . write ( json . dumps ( i1i11ii1Ii ) )
  i11iiI1111 . close ( )
 else :
  ooo0O0o0OoOO = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
  iIi11i = len ( ooo0O0o0OoOO )
  for o0o00o0Oo in ooo0O0o0OoOO :
   oOo0 = o0o00o0Oo [ 0 ]
   o00OooO0oo = o0o00o0Oo [ 1 ]
   oOoOoOoo0 = o0o00o0Oo [ 2 ]
   try :
    OOOOOo = o0o00o0Oo [ 3 ]
    if OOOOOo == None :
     raise
   except :
    if o0oO0 . getSetting ( 'use_thumb' ) == "true" :
     OOOOOo = oOoOoOoo0
    else :
     OOOOOo = III1ii1I
   try : oOOoo = o0o00o0Oo [ 5 ]
   except : oOOoo = None
   try : i1I1iIii11 = o0o00o0Oo [ 6 ]
   except : i1I1iIii11 = None
   if 80 - 80: OOooOOo - IIiIiII11i
   if o0o00o0Oo [ 4 ] == 0 :
    o0OOOO00O0Oo ( oOo0 , o00OooO0oo , '' , oOoOoOoo0 , III1ii1I , '' , 'fav' )
   else :
    o0OOOO00O0Oo ( oOo0 , o00OooO0oo , o0o00o0Oo [ 4 ] , oOoOoOoo0 , III1ii1I , '' , 'fav' )
    if 35 - 35: O0oOO0 - oO0o . I1ii11iIi11i * I1ii11iIi11i / Ii + Ii1I
def oOo0Oo0O0O ( name ) :
 O0oOI1IiI1iIiIiii = json . loads ( open ( iIi1ii1I1 ) . read ( ) )
 for III1II1i in range ( len ( O0oOI1IiI1iIiIiii ) ) :
  if O0oOI1IiI1iIiIiii [ III1II1i ] [ 0 ] == name :
   del O0oOI1IiI1iIiIiii [ III1II1i ]
   oo0 = open ( iIi1ii1I1 , "w" )
   oo0 . write ( json . dumps ( O0oOI1IiI1iIiIiii ) )
   oo0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 3 - 3: IIiI1I
 if 35 - 35: O00Oo000ooO0 . o0o00Oo0O + I1ii11iIi11i + i1IiIIIII + ooOoO0O00
def IiIIIIIi ( ) :
 OooOooO0O0o0 = os . path . join ( iIii1 , 'addons.ini' )
 OOO0o0 = open ( OooOooO0O0o0 , "w+" )
 if 34 - 34: oOo0O0Ooo % I1ii11iIi11i - OOooOOo + IIiI1I
 OOO0o0 . write ( r'# This file contains the "built-in" channels' + '\n' )
 OOO0o0 . write ( r'# It is parsed by Pythons ConfigParser' + '\n\n' )
 OOO0o0 . write ( r'[plugin.video.GenieTv]' + '\n' )
 OOO0o0 . write ( r'BBC One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F191.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+One%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BBC Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F190.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+Two%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BBC Four=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F188.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BBC+Four%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'ITV=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F208.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'ITV2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F207.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'ITV3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F206.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV3%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'ITV4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F205.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']ITV4%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Channel 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F183.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Channel+4%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Channel 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F185.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Channel+5%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'5STAR=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F187.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']5%2A%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'5 USA=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F186.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']5USA%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'RTE One=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F194.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']RTE+One%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'RTE Two=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F193.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']RTE+Two%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'TG4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F192.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']TG4%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F32.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F33.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Living=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F35.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Living%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Atlantic=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F34.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Atlantic%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Dave=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F325.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Dave%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Pick=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F324.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Pick%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'GOLD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F326.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Gold%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Watch HD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F518.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Watch%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'YESTERDAY=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F377.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Yesterday%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Comedy Central=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F181.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Comedy+Central%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'London Live=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F830.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']London+Live%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Disney Junior=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F230.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Disney+Jr.%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Disney Chnl=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F231.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Disney+Channel%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Animal Planet=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F198.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Animal+Planet%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Nat Geo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F197.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']National+Geographic+Channel%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Discovery=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F200.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Channel%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Discovery Science=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F199.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Science%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Disc.Turbo=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F168.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Discovery+Turbo%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Food Network=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F639.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Food+Network%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'MTV MUSIC=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F234.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']MTV+Music%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Film4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F182.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Film4%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'True Movies=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F853.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']True+Movies%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'True Movies 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F852.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']True+Movies+2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Action=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F732.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Action+%26+Adventure%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky ScFiHorror=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F511.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Sci-Fi+%26+Horror%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'SkyPremiereHD=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F516.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Premiere%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Greats=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F512.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Greats%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Family=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F509.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Family%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky DramaRom=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F510.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Drama+%26+Romance%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Thriller=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F514.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Crime+%26+Thriller%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Comedy=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F513.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Comedy%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Showcase=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F46.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Showcase%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Select=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F45.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Select%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Disney=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F195.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Movies+Disney%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F18.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F19.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports 3=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F20.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+3%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports 4=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F21.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+4%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports 5=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F22.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+5%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports F1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F24.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+F1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Sky Sports News=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F23.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Sky+Sports+News%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BT Sport 1=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F309.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BT Sport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F26.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BT Sport Europe=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F705.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+Europe%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'BT Sport ESPN=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F28.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']BT+Sport+ESPN%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Box Nation=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F173.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Box+Nation%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'WWENetwork=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F178.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']WWENetwork%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Eurosport=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F269.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Eurosport+1%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Eurosport 2=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F748.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Eurosport+2%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'At The Races=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F170.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']At+the+Races%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Racing UK=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F171.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Racing+UK%0D[%2FCOLOR]' + '\n' )
 OOO0o0 . write ( r'Poker central US=plugin://plugin.video.GenieTv/?url=http%3A%2F%2Fpiesustv.net%3A8000%2Flive%2F' + oo0o0O00 + '%2F' + oO + '%2F826.m3u8&mode=10012&name=[COLOR' + oO0o0o0ooO0oO + ']Poker+central+US%0D[%2FCOLOR]' + '\n' )
 if 79 - 79: IIiIiII11i - O0oOO0 . ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * oOo0O0Ooo
 if 7 - 7: ooOoO0O00 + i1IiIIIII % IIiI1I / I11i + ooOoO0O00
def I1ii11I ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  OOooOoooOoOo ( oOo0 , ( o00OooO0oo ) . strip ( ) , 222 , OOoOO0oo0ooO + '247.png' , OOoOO0oo0ooO + '247.png' , '' )
def II1II1IIII ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  OOooOoooOoOo ( oOo0 , ( o00OooO0oo ) . strip ( ) , 222 , OOoOO0oo0ooO + 'musicch.png' , OOoOO0oo0ooO + 'musicch.png' , '' )
def i1iiiiI1IiIIii ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  OOooOoooOoOo ( oOo0 , ( o00OooO0oo ) . strip ( ) , 222 , OOoOO0oo0ooO + 'NEWS.png' , OOoOO0oo0ooO + 'NEWS.png' , '' )
def IIIIiii ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  OOooOoooOoOo ( oOo0 , ( o00OooO0oo ) . strip ( ) , 222 , OOoOO0oo0ooO + 'adult.png' , OOoOO0oo0ooO + 'adult.png' , '' )
def Ii11Ii1iI ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 o0O00oOoOO = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  OOooOoooOoOo ( oOo0 , o00OooO0oo , 1016 , OOoOO0oo0ooO + 'TUTS.png' , OOoOO0oo0ooO + 'TUTS.png' , '' )
  if 87 - 87: I1ii11iIi11i + o0o00Oo0O - Ii1i111I * iI11I1II1I1I . oO00Oo0o000 % I11i
  if 83 - 83: IIiIiII11i * ooOoO0O00 * IIiI1I . Ii1I / Ii1i111I + ooOoO0O00
def i1Iio0oO00 ( ) :
 if 88 - 88: Ii1i111I + Ii % O0O0O * i1IiIIIII * i1IiIIIII * OoOO00O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Recent Episodes[/COLOR]' , '' , 10019 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , '' , 10020 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search[/COLOR]' , '' , 10021 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
 if 24 - 24: O0oOO0 / IIiI1I + O00Oo000ooO0 . O00Oo000ooO0
def I1ii1i ( ) :
 if 22 - 22: O0O0O * OoOO00O * Ii + IIiI1I * OOooOOo * oO0o
 O0OOoOOO0oO = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , I11iiiiI1i , oOo0 , oOoO00o in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 + '  -  ' + ( oOoO00o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o00OooO0oo , 10023 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 85 - 85: IIiI1I * i1IiIIIII % I1ii11iIi11i - IIiI1I - Ii1i111I
  if 46 - 46: o0o00Oo0O
  if 65 - 65: iI11I1II1I1I % O0O0O + o0o00Oo0O / ii
def O0000oO0o00 ( ) :
 if 80 - 80: ii + O00Oo000ooO0
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
 if 95 - 95: oO00Oo0o000 / O0O0O * oO00Oo0o000 - ii * ii % oO0o
def iI1I1I1i1i ( url ) :
 Oo0o0O00 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 IIiII = cloudflare . source ( Oo0o0O00 )
 o0O00oOoOO = re . compile ( '<div class="tv-series-single">.+?<a href="(.+?)" class="film-image">.+?<img src="(.+?)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 10022 , OOoOO0oo0ooO + 'dtv.png' , i1iIIi1 , '' )
  if 87 - 87: OOooOOo / O00Oo000ooO0 . O0oOO0 - i1IiIIIII / oO0o
  if 41 - 41: IIiIiII11i
  if 27 - 27: I1ii11iIi11i * OOooOOo % iI11I1II1I1I . oOo0O0Ooo
  if 70 - 70: Ii1i111I % IIiIiII11i % o0o00Oo0O . ooOoO0O00 / oO00Oo0o000
def OO0ooOoOO0OOo ( ) :
 if 51 - 51: iI11I1II1I1I * I11i / iI11I1II1I1I . iI11I1II1I1I . IIiI1I * Ii1i111I
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 o00OooO0oo = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OO0oo ) . replace ( ' ' , '+' )
 IIiII = cloudflare . source ( o00OooO0oo )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  if OO0oo in oOo0 . lower ( ) :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 10022 , OOoOO0oo0ooO + 'dtv.png' )
   if 93 - 93: O0O0O * OoOO00O
   if 27 - 27: oOo0O0Ooo * O0oOO0
   if 77 - 77: O00Oo000ooO0
def Oo ( url ) :
 IIiII = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for I1IiI11 , i1I11 , iII11ii1ii , oOo0 in o0O00oOoOO :
  oOO0OOOo000o = ( iII11ii1ii ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OO00oo = ( i1I11 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0Oo0O0 = 'Season ' + OO00oo + 'Episode ' + oOO0OOOo000o + oOo0
  I1IiiIiii1 ( O0Oo0O0 , I1IiI11 )
  if 39 - 39: O0oOO0 / o0o00Oo0O * O00Oo000ooO0
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: OoOO00O / iI11I1II1I1I - oO0o + oOo0O0Ooo % i1IiIIIII
  if 14 - 14: I11i % O00Oo000ooO0 + Ii1I + oO0o
def I1IiiIiii1 ( name , url ) :
 I1IiI11 = url
 OOOoOOo0o = name
 o0ooOooo000oOO = cloudflare . source ( I1IiI11 )
 iIIi1i1 = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( o0ooOooo000oOO )
 for oOoO0 , IiI1Iii1 in iIIi1i1 :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + OOOoOOo0o + IiI1Iii1 + '[/COLOR]' , oOoO0 , 10012 , OOoOO0oo0ooO + 'dtv.png' )
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: IIiIiII11i / I11i . i1IiIIIII . ii
 if 19 - 19: O00Oo000ooO0 . Ii1I / OOooOOo
def O00oo ( ) :
 if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
 if 70 - 70: O0O0O * O0O0O + I1ii11iIi11i * i1IiIIIII % oOo0O0Ooo + iI11I1II1I1I
 if 2 - 2: Ii
 if 98 - 98: O0O0O / oO0o - OoOO00O - oOo0O0Ooo / OOooOOo + Ii
 if 17 - 17: Ii1i111I
 if 97 - 97: Ii1I * Ii1I / IIiI1I
 if 6 - 6: O0O0O
 if 72 - 72: Ii1i111I * Ii1I - OOooOOo / Ii1I + i1IiIIIII - IIiI1I
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + oO00Oo0o000
 if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * O0O0O
 if 85 - 85: IIiIiII11i . O0oOO0 % i1IiIIIII % Ii1i111I
 if 80 - 80: O0O0O * Ii1i111I / iI11I1II1I1I % O0O0O / iI11I1II1I1I
 if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * IIiI1I . Ii * o0o00Oo0O
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseries.ac/latest' , 10046 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseries.ac/new' , 10042 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Genres[/COLOR]' , 'http://www.watchseries.ac/series' , 10048 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Series[/COLOR]' , 'http://www.watchseries.ac/series' , 10041 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Search Program[/COLOR]' , '' , 10043 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + O00Oo000ooO0
 if 27 - 27: i1IiIIIII
def O0OO0ooO00 ( url ) :
 IIiII = Iiii ( url )
 oO00O0 = re . compile ( '<ul class="pagination" style="line-height: 3;">(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 o0O00oOoOO = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( oO00O0 ) )
 for url , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.watchseries.ac/letters/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 83 - 83: iI11I1II1I1I
def OooOO0oOOo0O ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" class="sr-header">(.+?)</a>' ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.watchseries.ac/' + url , 10049 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
  if 42 - 42: IIiI1I / I11i + I1ii11iIi11i . I1ii11iIi11i % i1IiIIIII
def Ii1III1 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10049 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 80 - 80: iI11I1II1I1I . IIiI1I . oO00Oo0o000
  if 9 - 9: ii * o0o00Oo0O
def O0oO0OOoO ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00ooOOoO0O000O = 'http://www.watchseries.ac/search/' + OO0oo . replace ( ' ' , '%20' )
 IIiII = Iiii ( O00ooOOoO0O000O )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'watch online' in oOo0 :
   pass
  else :
   print o00OooO0oo
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.watchseries.ac' + o00OooO0oo , 10044 , I11iiiiI1i , '' , '' )
   if 20 - 20: oOo0O0Ooo . Ii1i111I
   xbmcplugin . setContent ( O00o0OO , 'movies' )
   if 75 - 75: O0oOO0
def iI1ii1Ii ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<div class="block-left-home-inside-text">.+?<a href="(.+?)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , url , oOo0 , iII11ii1ii , I11i1II in o0O00oOoOO :
  OooOOOoOoo0O0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iII11ii1ii ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + OooOOOoOoo0O0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , I11iiiiI1i , '' , I11i1II )
  if 81 - 81: O00Oo000ooO0 - I11i - I1ii11iIi11i - OoOO00O / i1IiIIIII % Ii1i111I
def oO0Oo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="(.+?)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  OooOOOoOoo0O0 = ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + OooOOOoOoo0O0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10046 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 72 - 72: o0o00Oo0O . OOooOOo * I1ii11iIi11i + Ii1I - I11i
def iII1I11 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="mask">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , I11iiiiI1i , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10041 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 15 - 15: Ii1i111I
def IiiI11I1IIiI ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( IIiII )
 oO00O0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( IIiII )
 for i1I11 , III1Ii1i1I1 in oO00O0 :
  o0O00oOoOO = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( III1Ii1i1I1 ) )
  for url , oOo0 in o0O00oOoOO :
   OooOOOoOoo0O0 = ( i1I11 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + OooOOOoOoo0O0 + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 iIIi1i1 = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="(.+?)">Next</a></li></ul>' , re . DOTALL ) . findall ( IIiII )
 for oOo0 , url in o0O00oOoOO :
  o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseries.ac' + url , 10045 , OOoOO0oo0ooO + 'WATCHSERIES.png' , '' , '' )
 for url in iIIi1i1 :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseries.ac' + url , 10044 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 5 - 5: I1ii11iIi11i
class o0oOo00 ( ) :
 if 22 - 22: iI11I1II1I1I + O00Oo000ooO0 + Ii1I + oO00Oo0o000 - OoOO00O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 48 - 48: OoOO00O - OOooOOo - oO0o + oOo0O0Ooo * OoOO00O
  OooOOOoOoo0O0 = name
  self . Get_Sources ( o00OooO0oo , OooOOOoOoo0O0 )
  if 67 - 67: I1ii11iIi11i / O0oOO0 - O00Oo000ooO0
  if 74 - 74: Ii1i111I * OoOO00O - Ii1I % iI11I1II1I1I
 def Get_Sources ( self , URL , season_name ) :
  Oo0oO0ooo = xbmcgui . DialogProgress ( )
  IIiII = Iiii ( URL )
  o0O00oOoOO = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( IIiII )
  for o00OooO0oo , oOo0 in o0O00oOoOO :
   URL = 'http://www.watchseries.ac/link/' + o00OooO0oo
   self . Get_site_link ( URL , season_name )
   if 56 - 56: Ii1I - o0o00Oo0O
 def Get_site_link ( self , url , season_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( IIiII )
  iIIi1i1 = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( IIiII )
  I11IIiIiI = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( IIiII )
  for url in o0O00oOoOO :
   self . main ( url , season_name )
  for url in iIIi1i1 :
   self . main ( url , season_name )
  for url in I11IIiIiI :
   self . main ( url , season_name )
   if 58 - 58: O00Oo000ooO0 + iI11I1II1I1I
 def main ( self , url , season_name ) :
  Oo0oO0ooo . create ( "[COLORwhite]Origin[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0II1IIi1iII1i = 'DACLIPS'
   if o0II1IIi1iII1i in o0oOo00 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0II1IIi1iII1i )
    Oo0oO0ooo . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    o0II1IIi1iII1i = 'FILEHOOT'
    if o0II1IIi1iII1i in o0oOo00 . source_list :
     pass
    else :
     Oo0oO0ooo . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , o0II1IIi1iII1i )
   else :
    if 'thevideo.me' in url :
     o0II1IIi1iII1i = 'THEVIDEO'
     if o0II1IIi1iII1i in o0oOo00 . source_list :
      pass
     else :
      self . thevideo ( url , season_name , o0II1IIi1iII1i )
      Oo0oO0ooo . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      o0II1IIi1iII1i = 'ALLMYVIDEOS'
      if o0II1IIi1iII1i in o0oOo00 . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , o0II1IIi1iII1i )
       Oo0oO0ooo . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       o0II1IIi1iII1i = 'VIDSPOT'
       if o0II1IIi1iII1i in o0oOo00 . source_list :
        pass
       else :
        self . vidspot ( url , season_name , o0II1IIi1iII1i )
        Oo0oO0ooo . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        o0II1IIi1iII1i = 'VODLOCKER'
        if o0II1IIi1iII1i in o0oOo00 . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , o0II1IIi1iII1i )
         Oo0oO0ooo . update ( 0 , "" , "Getting Vodlocker Links" )
         if 26 - 26: o0o00Oo0O
         if 17 - 17: IIiIiII11i
 def allmyvid ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( IIiII )
  for iiIiii , oOo0 in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
 def vidspot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( IIiII )
  for iiIiii , oOo0 in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 83 - 83: ooOoO0O00
 def thevideo ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( IIiII )
  for iiIiii in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 76 - 76: OoOO00O + iI11I1II1I1I + OOooOOo . oO0o
 def vodlocker ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for iiIiii in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 49 - 49: O00Oo000ooO0 / O0oOO0 / i1IiIIIII
 def daclips ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( IIiII )
  for iiIiii in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - O0oOO0
 def filehoot ( self , url , season_name , source_name ) :
  IIiII = Iiii ( url )
  o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( IIiII )
  for iiIiii in o0O00oOoOO :
   self . Printer ( iiIiii , season_name , source_name )
   if 38 - 38: I11i % oO00Oo0o000 + Ii + IIiI1I + O0oOO0 / Ii
 def Printer ( self , Link , season_name , source_name ) :
  if 94 - 94: IIiI1I - I1ii11iIi11i + O0O0O
  if Link in o0oOo00 . List :
   pass
  elif source_name in o0oOo00 . source_list :
   pass
  else :
   oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + source_name + '[/COLOR]' , Link , 10012 , OOoOO0oo0ooO + 'WATCHSERIES.png' )
   Oo0oO0ooo . update ( 100 , "" , "Got Source" )
   o0oOo00 . List . append ( Link )
   o0oOo00 . source_list . append ( source_name )
   if 59 - 59: Ii1i111I . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
   xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 56 - 56: O0O0O + O0oOO0
   if 32 - 32: IIiIiII11i + OOooOOo % O0oOO0 / OOooOOo + Ii1I
   if 2 - 2: Ii - oO00Oo0o000 + oO0o % Ii1i111I * OoOO00O
   if 54 - 54: o0o00Oo0O - IIiI1I . i1IiIIIII % IIiI1I + IIiI1I
   if 36 - 36: i1IiIIIII % Ii
def Iiii1Ii ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Highlights[/COLOR]' , '' , 10008 , OOoOO0oo0ooO + 'Highlights.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Fixtures[/COLOR]' , '' , 10009 , OOoOO0oo0ooO + 'Fixtures.png' , i1iIIi1 , '' )
 if 62 - 62: ooOoO0O00 % OOooOOo
def i1ii1I1IIIII ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 o0O00oOoOO = re . compile ( '<a target="_self" href="(.+?)".+?src="(.+?)" alt="(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00OooO0oo , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + I11iiiiI1i , i1iIIi1 , '' )
  if 69 - 69: iI11I1II1I1I . IIiIiII11i . ooOoO0O00 - I11i
def o00OoOO0O0 ( url ) :
 IIiII = Iiii ( url )
 oO00O0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( IIiII )
 for oO00O0 in oO00O0 :
  I1i1II1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( oO00O0 ) )
  for oOOooI1 in I1i1II1 :
   oOOooI1 = oOOooI1
  ooiiI1IIIii = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( oO00O0 ) )
  for iIOO0OOoooo0o , I11iiiiI1i , time , IiIi1Ii in ooiiI1IIIii :
   i1ii1II1ii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IiIi1Ii )
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOOooI1 + ' - ' + iIOO0OOoooo0o + ' - ' + time + '[/COLOR]' , '' , 10010 , i1111 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + I11iiiiI1i , i1iIIi1 , ( str ( i1ii1II1ii ) ) )
   if 39 - 39: OoOO00O
 oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if 24 - 24: Ii - OoOO00O + O0O0O * oOo0O0Ooo
def OoooOo0 ( ) :
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
 if 20 - 20: IIiIiII11i - Ii1i111I + ooOoO0O00 + OoOO00O
def i11i11i ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'class="entry-thumb" src="(.+?)" alt="".+?<h3 class="entry-title td-module-title"><a href="(.+?)" rel="bookmark" title=".+?">(.+?)</a></h3>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width="218" height="150" class="entry-thumb" src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , url , oOo0 in o0O00oOoOO :
  iiI1iI = oOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + iiI1iI + '[/COLOR]' , url , 10013 , I11iiiiI1i )
 for url , oOo0 , I11iiiiI1i in iIIi1i1 :
  iiI1iI = oOo0 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + iiI1iI + '[/COLOR]' , url , 10013 , I11iiiiI1i )
  if 84 - 84: ii + oO00Oo0o000 / oOo0O0Ooo % i1IiIIIII % Ii1I * oOo0O0Ooo
def OOoO0oooo ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<script data-config="(.+?)" data-height' ) . findall ( IIiII )
 for oOoO0 in o0O00oOoOO :
  I11io0Oo = ( oOoO0 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  III1I1 ( 'http:' + I11io0Oo )
  if 4 - 4: IIiIiII11i
  if 20 - 20: Ii % ii . O00Oo000ooO0 / Ii1i111I
def Ii11 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOo0O ( oOo0 , url , 8046 , I11iiiiI1i )
 for url in iIIi1i1 :
  oOO0OO0OO ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , OOoOO0oo0ooO + 'Next.png' )
def I1i1ii ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  III1I1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: O0oOO0 * O00Oo000ooO0 * o0o00Oo0O * iI11I1II1I1I
def OOOOoO ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 19 - 19: oOo0O0Ooo % OoOO00O . O00Oo000ooO0 * O0oOO0
def oOo0OOOOoO ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw==' ) )
 if 70 - 70: IIiIiII11i + oO00Oo0o000 + Ii - ooOoO0O00 / O00Oo000ooO0
 o0O00oOoOO = re . compile ( '<a href="(.+?)" >(.+?)</a></li>' ) . findall ( O0OOoOOO0oO )
 if 40 - 40: Ii1I * oO00Oo0o000
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , o00OooO0oo , 8041 , OOoOO0oo0ooO + 'documentary.png' )
  if 38 - 38: o0o00Oo0O . I1ii11iIi11i + OOooOOo - O0O0O
  if 43 - 43: IIiI1I + I1ii11iIi11i / ii
  if 24 - 24: o0o00Oo0O + I11i * OoOO00O - oO00Oo0o000
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iii11i1 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img width="95" height="125" src="([^"]*)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'title="([^"]*)" href="([^"]*)"><img src="([^"]*)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 next = re . compile ( 'class="inactive">.+?</a><a href="(.+?)">Next</a></div>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , I11iiiiI1i )
 for oOo0 , url , I11iiiiI1i in iIIi1i1 :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url , 8042 , I11iiiiI1i )
 for url in next :
  oOO0OO0OO ( 'NEXT PAGE' , url , 8041 , OOoOO0oo0ooO + 'Next.png' )
  if 100 - 100: Ii1i111I % Ii * IIiI1I / oO0o % Ii1I + i1IiIIIII
  if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
def OO0oo00oOO ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( '<div class="video new-video"><iframe width="766" height="431" src="(.+?)&iv_load_policy=3&showinfo=0&autohide=1"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , I11iiiiI1i , url , IIi11 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , url . replace ( 'https://www.youtube.com/embed/videoseries?list=' , '' ) . replace ( 'https://www.youtube.com/embed/' , '' ) , 8043 , I11iiiiI1i )
 for url in iIIi1i1 :
  I1iOO0O0O ( ( url ) . replace ( '//' , 'http://' ) )
  if 33 - 33: OoOO00O
def I1iOO0O0O ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<link rel="canonical" href="(.+?)">  <link rel="stylesheet"' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  oOo0O ( 'PLAY' , ( url ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , OOoOO0oo0ooO + 'documentary.png' )
  if 93 - 93: O0oOO0
def II11iIIii ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<h1><a href="([^"]*)">(.+?)</a>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , url , 8049 , I11iiiiI1i )
 for url in iIIi1i1 :
  oOO0OO0OO ( 'NEXT' , url , 8048 , OOoOO0oo0ooO + 'Next.png' )
def oooOo0Ooo0oo ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  if 'tube' in url :
   yt . PlayVideo ( ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) )
 for url in iIIi1i1 :
  if 'rtd' in url :
   oOIiiIIi ( url )
   if 96 - 96: ooOoO0O00 . Ii1i111I + O0O0O + Ii1I * i1IiIIIII - IIiIiII11i
def oOIiiIIi ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( O0OOoOOO0oO )
 for O00oO , file in o0O00oOoOO :
  url = ( 'https://rtd.rt.com' + O00oO + file )
  III1I1 ( url )
  if 1 - 1: o0o00Oo0O
  if 40 - 40: oO00Oo0o000 - OOooOOo * Ii1i111I - O00Oo000ooO0 / OOooOOo
def OO0ooO0oOO0o ( ) :
 IIiII = I1ii11 ( 'http://www.stream2watch.co/live-tv' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for o00OooO0oo , I11iiiiI1i , oOo0 , oo000oO0O in o0O00oOoOO :
  oOO0OO0OO ( ( oOo0 + '[COLOR' + oO0o0o0ooO0oO + ']' + oo000oO0O + '[/COLOR]' ) , o00OooO0oo , 8086 , I11iiiiI1i )
  if 100 - 100: iI11I1II1I1I
def ooOOo00 ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a class="front_channel_href" href="(.+?)" title=".+?">.+?<img class="front_channel_thumb" src="(.+?)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 8087 , I11iiiiI1i )
  if 39 - 39: I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * OOooOOo % o0o00Oo0O
def oo00ooooOOo00 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( 'a id="code_.+?data-f-href="(.+?)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  ii1iOO00Oooo000 ( url , oOo0 )
  if 38 - 38: oO0o . O0oOO0
def ii1iOO00Oooo000 ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( IIiII )
 for url in o0O00oOoOO :
  print url
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 34 - 34: ooOoO0O00 % O00Oo000ooO0
def OoOo ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + o00OooO0oo , 3002 , 'http://www.solie.org/alibrary/' + I11iiiiI1i )
def IiI1iiIiII ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I11iiiiI1i )
def IIiiiI1iI ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 O0O0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( '<td align="center" valign="top">.+?<a href="(.+?)">.+?<img src="(.+?)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url , oOo0 in O0O0 :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']Season- ' + oOo0 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'classicmovies.png' )
 for url in next :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , OOoOO0oo0ooO + 'Next.png' )
 for url , I11iiiiI1i , oOo0 in iIIi1i1 :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + I11iiiiI1i )
def O0oO0o0OOOOOO ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  IiI1i11IiIiii ( url )
def IiI1i11IiIiii ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  III1I1 ( url )
  if 4 - 4: oO00Oo0o000 - oOo0O0Ooo % O0O0O / I11i % O0O0O * IIiIiII11i
def IiI1I ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o00OooO0oo , 8065 , OOoOO0oo0ooO + 'classicmovies.png' )
def IIIiIi1iiI ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( "v.src = '([^']*)';" ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  iI1iiiiIii ( url )
  if 15 - 15: Ii1I . IIiI1I
def o0Iiii ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 o0O00oOoOO = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , o00OooO0oo , 8065 , OOoOO0oo0ooO + 'classictv.png' )
def I1i1I ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  if 'mp4' in url :
   III1I1 ( url )
 for url in iIIi1i1 :
  yt . PlayVideo ( url )
  if 17 - 17: Ii1i111I - IIiI1I % OoOO00O
def i11Ii1iIIIIi ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"> (.+?).m3u</a></li>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + o00OooO0oo , 8071 , OOoOO0oo0ooO + 'streams.png' )
def iii ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for oOo0 , url in o0O00oOoOO :
  if '(Free Access)' in oOo0 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , OOoOO0oo0ooO + 'streams.png' )
def O000OOO ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , oOo0 , url in o0O00oOoOO :
  url = ( ( i1111 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + oo0o0O00 + '/' + oO + url ) . strip ( )
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , I11iiiiI1i )
  if 59 - 59: oO00Oo0o000 . Ii1I + ii
def i1II11I11ii1 ( ) :
 O0OO ( 'Best Videos' , 'http://www.xvideos.com/best' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 O0OO ( 'Genres' , 'http://www.xvideos.com' , 10106 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 O0OO ( 'Recently Uploaded' , 'http://xvideos.com' , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 O0OO ( 'Tags' , 'http://www.xvideos.com/tags' , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 O0OO ( 'Search' , '' , 10107 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' , )
 if 64 - 64: O0O0O % OOooOOo / IIiIiII11i % O0oOO0 - IIiI1I
def I1II1IiI1 ( url ) :
 IIiII = Iiii ( url )
 iIIiI11iI1Ii1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in iIIiI11iI1Ii1 :
  O0OO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( IIiII )
 for url , oOo0 , OOOoOO in o0O00oOoOO :
  O0OO ( ( oOo0 + ' - No of Videos : ' + ( OOOoOO ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 94 - 94: O0oOO0 / Ii % o0o00Oo0O
def O0oO0oo0O ( url ) :
 IIiII = Iiii ( url )
 iIIiI11iI1Ii1 = re . compile ( 'href="([^"]*)">Next</a></li>' ) . findall ( IIiII )
 for url in iIIiI11iI1Ii1 :
  O0OO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , url , oOo0 , oooOOO0ooOoOOO in o0O00oOoOO :
  O0OO ( oOo0 + '--' + oooOOO0ooOoOOO , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( I11iiiiI1i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 68 - 68: o0o00Oo0O
  if 76 - 76: Ii1I
def ooO000OO ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="thumb"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , url , oOo0 , o0o0oOoOO0O , i111IIiIiiI1 in o0O00oOoOO :
  O0OO ( oOo0 + ' - Porn Quality : ' + i111IIiIiiI1 + ' - ' + o0o0oOoOO0O , 'http://www.xvideos.com' + url , 10108 , I11iiiiI1i , I11iiiiI1i , i111IIiIiiI1 + ' - ' + o0o0oOoOO0O )
 OO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for url in OO0 :
  O0OO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 28 - 28: I1ii11iIi11i % i1IiIIIII - oO0o + O0oOO0 / O0oOO0
def oo0oOO ( url ) :
 IIiII = Iiii ( url )
 oO00O0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 iIIiI11iI1Ii1 = re . compile ( '<li><a class=".+?".+?href="(.+?)">Next</a></li>' ) . findall ( IIiII )
 for url in iIIiI11iI1Ii1 :
  O0OO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( oO00O0 ) )
 for url , oOo0 in o0O00oOoOO :
  O0OO ( oOo0 , 'http://www.xvideos.com' + url , 10105 , OOoOO0oo0ooO + 'Jizbox.png' , '' , '' )
  if 41 - 41: oO0o . oO00Oo0o000 * O00Oo000ooO0 * oO00Oo0o000
  if 74 - 74: iI11I1II1I1I / I11i
def Oo0o0O0o ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iii1IiI1i = ( OO0oo ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OOO0000oO = iii1IiI1i . lower ( )
 OooO0ooO0o0 = 'http://www.xvideos.com/?k=' + OOO0000oO
 print OooO0ooO0o0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIiII = Iiii ( OooO0ooO0o0 )
 o0O00oOoOO = re . compile ( '<div class="thumb-inside"><script>.+?<img src="(.+?)".+?<a href="(.+?)" title=".+?">(.+?)</a></p>.+?uration">(.+?)</span>.+?Porn quality:(.+?)</span>' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , o00OooO0oo , oOo0 , o0o0oOoOO0O , i111IIiIiiI1 in o0O00oOoOO :
  O0OO ( oOo0 + ' - Porn Quality : ' + i111IIiIiiI1 + ' - ' + o0o0oOoOO0O , 'http://www.xvideos.com' + o00OooO0oo , 10108 , I11iiiiI1i , I11iiiiI1i , i111IIiIiiI1 + ' - ' + o0o0oOoOO0O )
 OO0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( IIiII )
 for o00OooO0oo in OO0 :
  O0OO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + o00OooO0oo , 10105 , OOoOO0oo0ooO + 'Next.png' , '' , '' )
  if 88 - 88: O0O0O % I1ii11iIi11i - Ii1i111I % O0O0O + O00Oo000ooO0 - IIiI1I
def ii1OO0 ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( IIiII )
 iIIi1i1 = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( IIiII )
 I11IIiIiI = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'http' in url :
   oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']LOW[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in iIIi1i1 :
  if 'http' in url :
   oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']HIGH[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
 for url in I11IIiIiI :
  if 'http' in url :
   oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']HLS[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'Jizbox.png' )
   if 96 - 96: o0o00Oo0O . IIiI1I - oOo0O0Ooo * I1ii11iIi11i
def OOoOOOo0 ( url ) :
 ooooOoO0O = xbmc . Player ( oOoO00O ( ) )
 import urlresolver
 try : ooooOoO0O . play ( url )
 except : pass
 if 31 - 31: O0oOO0 . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * IIiI1I
 if 22 - 22: Ii1i111I % O00Oo000ooO0 . OOooOOo / O0oOO0 + i1IiIIIII
def OO000OOo ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cDovL3d3dy5nb2Zpc2hpbmcuY28udWsvQW5nbGluZy1UaW1lcy9TZWN0aW9uL1ZpZGVvcy8=' ) )
 o0O00oOoOO = re . compile ( 'class="item.+?"><a href="(.+?)">(.+?)</a></li>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , ( 'http://www.gofishing.co.uk' + o00OooO0oo ) . replace ( 'http://www.gofishing.co.ukhttp://www.gofishing.co.uk' , 'http://www.gofishing.co.uk' ) , 8091 , OOoOO0oo0ooO + 'gofish.png' )
def oOo0O000Ooo0 ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<h2><a id=.+?href="([^"]*)">(.+?)</a></h2>' , re . DOTALL ) . findall ( IIiII )
 iIIi1i1 = re . compile ( '<h3><a href="([^"]*)" id=.+?>(.+?)</a> </h3>.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( IIiII )
 next = re . compile ( 'href="([^"]*)">next</a>&gt;</li>' , re . DOTALL ) . findall ( IIiII )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , OOoOO0oo0ooO + 'gofish.png' )
 for url , oOo0 , I11iiiiI1i in iIIi1i1 :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.gofishing.co.uk/' + url , 8092 , 'http://www.gofishing.co.uk/' + I11iiiiI1i )
 for url in next :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url . replace ( ' ' , '+' ) , 8091 , OOoOO0oo0ooO + 'Next.png' )
def i11i ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'src="https://www.youtube.com/embed/(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  yt . PlayVideo ( url )
  if 73 - 73: O0oOO0 % O0oOO0 . IIiI1I + oO00Oo0o000
  if 10 - 10: o0o00Oo0O / i1IiIIIII * O0oOO0 - oO0o - ooOoO0O00 . OOooOOo
  if 69 - 69: I1ii11iIi11i - OoOO00O % OoOO00O - i1IiIIIII * i1IiIIIII / I1ii11iIi11i
i1IiIIi = '{PQ},' ; OOOOo0 = '{SC},' ; ooOO0OOO00o = '{XG},' ; OoOoO0ooooO0 = '{JP},' ; IIII1ii1 = '{HW},' ; OOO0O0OOo = '{RT},'
def Iii1OOoO ( ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 i1IiiI = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 o00OooO0oo = ( i1111 ( 'aHR0cDovL2RsNC5tb3ZpZWZhcnNpLmNvbS9maWxtLzIwMTUtNy8=' ) )
 I1IiI11 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcyUyMChDcmFwJTIwQ29waWVzKS8=' ) )
 iIiIiIiI = ( i1111 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0OOO0o0O = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9OZXclMjBSZWxlYXNlcy8=' ) )
 IiIIi1iiI = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0ooOO00OO0o0O = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 III1IiiIiiI1i = ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OO0oo
 OoO0o00OoO = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL21vdmllcy9hbGxtb3ZpZS5waHA=' ) )
 Oo00Oooo00o = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbG1vdmllcy5waHA=' ) )
 II11II1I = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 O0OO00000o00 = ( i1111 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 83 - 83: O0O0O - O0oOO0 - O00Oo000ooO0 % ooOoO0O00 - IIiI1I . I11i
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 IIiII = i1I1iI ( o00OooO0oo )
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0ooOooo000oOO = i1I1iI ( I1IiI11 )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 Oo0oOOo = i1I1iI ( iIiIiIiI )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( O0OOO0o0O )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 oOo0oO = i1I1iI ( IiIIi1iiI )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 ooo0O = i1I1iI ( III1IiiIiiI1i )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 iI1iIIIIIiIi1 = i1I1iI ( OoO0o00OoO )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIi = i1I1iI ( Oo00Oooo00o )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOoooOo0o = i1I1iI ( II11II1I )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 III = i1I1iI ( O0OO00000o00 )
 if 36 - 36: ii / I1ii11iIi11i . oO00Oo0o000 % ii . i1IiIIIII + IIiIiII11i
 if 43 - 43: Ii1i111I % OoOO00O / I11i * oO00Oo0o000
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIiII )
  for ooo , oOo0 in o0O00oOoOO :
   if OO0oo in oOo0 . lower ( ) :
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( o00OooO0oo + ooo ) , 222 , '' )
    Oo0oO0ooo . update ( 0 , "" , "Getting Source 1 Links" )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o0ooOooo000oOO )
  for ooo , oOo0 in iIIi1i1 :
   if OO0oo in oOo0 . lower ( ) :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- Silent Hunter Cams[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , ( I1IiI11 + ooo ) , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 9 , "" , "Getting Silent Hunter Cams Links" )
 if Oo0oOOo != 'Failed' :
  I11IIiIiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0oOOo )
  for ooo , oOo0 in I11IIiIiI :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIiIiIiI + ooo ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 18 , "" , "Getting Source 3 Links" )
 if Oo0OoO00oOO0o != 'Failed' :
  iIIIi1i1I11i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for ooo , oOo0 in iIIIi1i1I11i :
   if OO0oo in oOo0 . lower ( ) :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- Silent Hunter[/COLOR]' ) . replace ( 'mkv' , '' ) . replace ( '.' , ' ' ) , o00OooO0oo , 222 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 27 , "" , "Getting Silent Hunter Links" )
 if oOo0oO != 'Failed' :
  Ii1I11IiI1i = [ ]
  I111 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo0oO )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in I111 :
   if OO0oo in oOo0 . lower ( ) :
    if oOo0 in Ii1I11IiI1i :
     pass
    else :
     o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , o00OooO0oo , 1016 , oOoOoOoo0 , O0oO , I11i1II )
     Ii1I11IiI1i . append ( oOo0 )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 36 , "" , "Getting Scooby Links" )
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if ooo0O != 'Failed' :
  I111oOOooo00OOooO = re . compile ( 'href="(.+?)".+?src="(.+?)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( ooo0O )
  for o00OooO0oo , I11iiiiI1i , oOo0 in I111oOOooo00OOooO :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + o00OooO0oo , 7067 , I11iiiiI1i )
    Oo0oO0ooo . update ( 45 , "" , "Getting Snag Links" )
    if 31 - 31: oOo0O0Ooo / I11i + oOo0O0Ooo - IIiIiII11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iI1iIIIIIiIi1 != 'Failed' :
  iiiii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIIIIIiIi1 )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in iiiii1i :
   if OO0oo in oOo0 . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Redemption[/COLOR]' ) , o00OooO0oo , 222 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 53 , "" , "Getting Redemption Links" )
    if 48 - 48: ii . I1ii11iIi11i * o0o00Oo0O / Ii1I . oOo0O0Ooo * Ii1i111I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iIi != 'Failed' :
  IIIiI1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iIi )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in IIIiI1i1 :
   if OO0oo in oOo0 . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Reaper[/COLOR]' ) , o00OooO0oo , 222 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 61 , "" , "Getting Reaper Links" )
    if 13 - 13: i1IiIIIII * Ii1i111I / o0o00Oo0O * I11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if oOoooOo0o != 'Failed' :
  Ii1iiIi11111I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoooOo0o )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in Ii1iiIi11111I :
   if OO0oo in oOo0 . lower ( ) :
    OOooOoooOoOo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Herovision[/COLOR]' ) , o00OooO0oo , 222 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Herovision Links" )
    if 72 - 72: oO0o . I11i * Ii1I . iI11I1II1I1I % Ii1I . OoOO00O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: i1IiIIIII + O0oOO0 * OoOO00O . OoOO00O + oO0o
 if III != 'Failed' :
  ii1O0Ooo0O = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( III )
  for o00OooO0oo , oOoOoOoo0 , oOo0 in ii1O0Ooo0O :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Silent Hunter[/COLOR]' ) , o00OooO0oo , 222 , oOoOoOoo0 )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 18 - 18: ooOoO0O00
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 OO = [ '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'films' ]
 if 4 - 4: O00Oo000ooO0
 for I1iIII1IiiI in OO :
  OOoooOoO0Oo = OOO00 + I1iIII1IiiI + OooO0
  oOo0OoOOOo0 = i1I1iI ( OOoooOoO0Oo )
  if oOo0OoOOOo0 != 'Failed' :
   OOoo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo0OoOOOo0 )
   for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in OOoo00 :
    if OO0oo in oOo0 . lower ( ) :
     OOooOoooOoOo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + ' - Source Pandoras[/COLOR]' , o00OooO0oo , 222 , oOoOoOoo0 , O0oO , I11i1II )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 89 , "" , "Getting Pandoras Links" )
     if 22 - 22: O0oOO0 / O0oOO0 - OoOO00O % Ii1i111I . i1IiIIIII + O00Oo000ooO0
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 64 - 64: ooOoO0O00 % Ii1I / OoOO00O % ii
 OO = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 24 - 24: oO00Oo0o000 + ii . O00Oo000ooO0 / OOooOOo / Ii1i111I
 if 65 - 65: ii
 for I1iIII1IiiI in OO :
  OOoooOoO0Oo = i1IiiI + I1iIII1IiiI
  iiii11iI1 = i1I1iI ( OOoooOoO0Oo )
  if oOo0oO != 'Failed' :
   Oo00Oo = re . compile ( '<li><a href="(.+?)"> (.+?)</a></li>' ) . findall ( iiii11iI1 )
   for ooo , oOo0 in Oo00Oo :
    if OO0oo in oOo0 . lower ( ) :
     oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1IiiI + I1iIII1IiiI + ooo ) , 222 , '' )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Source 5 Links" )
     if 25 - 25: iI11I1II1I1I
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: O0oOO0
     if 96 - 96: Ii1i111I
def IIIIii1 ( ) :
 if 63 - 63: IIiI1I
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 if 11 - 11: IIiI1I - iI11I1II1I1I
 o00OooO0oo = ( i1111 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYy9zZWFyY2gv' ) ) + ( OO0oo ) . replace ( ' ' , '%20' )
 I1IiI11 = ( i1111 ( 'aHR0cDovL3JlZGVtcHRpb25idWlsZC4xNm1iLmNvbS9SZWRlbXB0aW9uL3R2c2hvd3MvdHZtYWluLnBocA==' ) )
 iIiIiIiI = ( i1111 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 O0OOO0o0O = ( i1111 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9BbWVyaWNhbiUyMFNlcmlhbC8=' ) )
 IiIIi1iiI = ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OOO0000oO ) . replace ( ' ' , '+' )
 o0ooOO00OO0o0O = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 III1IiiIiiI1i = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9UaGVfUmVhcGVyL2FsbHR2LnBocA==' ) )
 OoO0o00OoO = ( i1111 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 92 - 92: oO0o
 Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 15 - 15: O00Oo000ooO0 / O00Oo000ooO0 + iI11I1II1I1I % ii
 Oo0oO0ooo . update ( 0 , "" , "Checking Source 1/9 Links" )
 IIiII = i1I1iI ( o00OooO0oo )
 Oo0oO0ooo . update ( 14 , "" , "Checking Source 2/9 Links" )
 o0ooOooo000oOO = i1I1iI ( I1IiI11 )
 Oo0oO0ooo . update ( 28 , "" , "Checking Source 3/9 Links" )
 Oo0oOOo = i1I1iI ( iIiIiIiI )
 Oo0oO0ooo . update ( 40 , "" , "Checking Source 4/9 Links" )
 Oo0OoO00oOO0o = i1I1iI ( O0OOO0o0O )
 Oo0oO0ooo . update ( 52 , "" , "Checking Source 5/9 Links" )
 oOo0oO = cloudflare . source ( IiIIi1iiI )
 Oo0oO0ooo . update ( 64 , "" , "Checking Source 6/9 Links" )
 iiii11iI1 = i1I1iI ( o0ooOO00OO0o0O )
 Oo0oO0ooo . update ( 76 , "" , "Checking Source 7/9 Links" )
 ooo0O = i1I1iI ( III1IiiIiiI1i )
 Oo0oO0ooo . update ( 88 , "" , "Checking Source 8/9 Links" )
 iI1iIIIIIiIi1 = i1I1iI ( OoO0o00OoO )
 Oo0oO0ooo . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 12 - 12: O0oOO0
 if iI1iIIIIIiIi1 != 'Failed' :
  iiiii1i = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1iIIIIIiIi1 )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in iiiii1i :
   if OOO0000oO in oOo0 . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source HeroVision[/COLOR]' ) , o00OooO0oo , 1016 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 10 , "" , "Getting Herovision Links" )
    if 36 - 36: oO00Oo0o000 . O00Oo000ooO0 * ii - I11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: i1IiIIIII . IIiI1I / iI11I1II1I1I + i1IiIIIII * oO00Oo0o000
 if ooo0O != 'Failed' :
  I111oOOooo00OOooO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( ooo0O )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in I111oOOooo00OOooO :
   if OOO0000oO in oOo0 . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- source Reaper[/COLOR]' ) , o00OooO0oo , 1016 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 20 , "" , "Getting Reaper Links" )
    if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - Ii1i111I + OoOO00O
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 48 - 48: Ii1I
    if 96 - 96: O0oOO0 . ii
    if 39 - 39: i1IiIIIII + oO0o
    if 80 - 80: i1IiIIIII % oO0o / OOooOOo
    if 54 - 54: I1ii11iIi11i % oO0o - i1IiIIIII - Ii1i111I
    if 71 - 71: O0oOO0 . Ii
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 30 , "" , "Getting CoolSeries Links" )
    if 56 - 56: o0o00Oo0O * IIiI1I + IIiI1I * iI11I1II1I1I / O0oOO0 * oO00Oo0o000
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<img src="(.+?)".+?<a href="(.+?)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( IIiII )
  for I11iiiiI1i , o00OooO0oo , oOo0 in o0O00oOoOO :
   if OOO0000oO in oOo0 . lower ( ) :
    o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + ' - WatchSeries[/COLOR]' , 'http://www.watchseries.ac' + o00OooO0oo , 10044 , I11iiiiI1i , '' , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 25 - 25: iI11I1II1I1I . Ii1i111I * Ii + I1ii11iIi11i * Ii1i111I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 67 - 67: IIiI1I
    if 88 - 88: I1ii11iIi11i
    if 8 - 8: Ii1I
    if 82 - 82: ii
    if 75 - 75: IIiIiII11i % oOo0O0Ooo + i1IiIIIII % ii / O00Oo000ooO0
    if 4 - 4: Ii - i1IiIIIII % Ii1I * oO00Oo0o000 % I11i
    if 71 - 71: O0oOO0 . O0oOO0 - iI11I1II1I1I
    if 22 - 22: ii / Ii1I % IIiI1I * OOooOOo
    if 32 - 32: ii % O0O0O % iI11I1II1I1I / o0o00Oo0O
    if 61 - 61: IIiIiII11i . o0o00Oo0O - OoOO00O - Ii1I / Ii - IIiIiII11i
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( o0ooOooo000oOO )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in iIIi1i1 :
   if OOO0000oO in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , o00OooO0oo , 1016 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 50 , "" , "Getting Redemption Links" )
    if 98 - 98: OoOO00O - oOo0O0Ooo . Ii * I1ii11iIi11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  I11IIiIiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0oOOo )
  for oOo0 in I11IIiIiI :
   if OOO0000oO in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIiIiI + oOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 60 , "" , "Getting Source 3 Links" )
    if 29 - 29: OoOO00O / O0oOO0 % Ii1i111I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0OoO00oOO0o != 'Failed' :
  iIIIi1i1I11i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Oo0OoO00oOO0o )
  for oOo0 in iIIIi1i1I11i :
   if OOO0000oO in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( O0OOO0o0O + oOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 70 , "" , "Getting Source 4 Links" )
    if 10 - 10: iI11I1II1I1I % ii % Ii1I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if oOo0oO != 'Failed' :
  I111 = re . compile ( '<a href="(.+?)" class="film-image">\n<img src="(.+?)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oOo0oO )
  for o00OooO0oo , I11iiiiI1i , oOo0 in I111 :
   if OOO0000oO in oOo0 . lower ( ) :
    oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + ' - Source - Dizi[/COLOR]' , o00OooO0oo , 8062 , I11iiiiI1i )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 80 , "" , "Getting Dizi Links" )
    if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * Ii1i111I
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if iiii11iI1 != 'Failed' :
  Oo00Oo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( iiii11iI1 )
  for o00OooO0oo , oOoOoOoo0 , I11i1II , O0oO , oOo0 in Oo00Oo :
   if OOO0000oO in oOo0 . lower ( ) :
    o0OOOO00O0Oo ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '- Source Scooby[/COLOR]' ) , o00OooO0oo , 1016 , oOoOoOoo0 , O0oO , I11i1II )
    Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    Oo0oO0ooo . update ( 90 , "" , "Getting Scooby Links" )
    if 89 - 89: OoOO00O - O0oOO0 . Ii1i111I - oO00Oo0o000 - oOo0O0Ooo
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 79 - 79: O00Oo000ooO0 + O00Oo000ooO0 + OoOO00O
 iiiII1i1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 97 - 97: o0o00Oo0O . oO00Oo0o000 / IIiIiII11i . o0o00Oo0O + ii
 for I1iIII1IiiI in iiiII1i1I :
  OOoooOoO0Oo = OOO00 + I1iIII1IiiI + OooO0
  oOoooOo0o = Iiii ( OOoooOoO0Oo )
  if oOoooOo0o != 'Failed' :
   Ii1iiIi11111I = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOoooOo0o )
   for oOo0 , I11i1II , o00OooO0oo , I11iiiiI1i , III1ii1I , O00o in Ii1iiIi11111I :
    if OOO0000oO in oOo0 . lower ( ) :
     o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + ' - Source Pandoras[/COLOR]' , o00OooO0oo , O00o , I11iiiiI1i , III1ii1I , I11i1II )
     Oo0oO0ooo . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     Oo0oO0ooo . update ( 100 , "" , "Getting Pandoras Links" )
     if 78 - 78: IIiIiII11i + O00Oo000ooO0
     oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: iI11I1II1I1I
     if 57 - 57: O00Oo000ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiI11I1Ii11II ( ) :
 if 75 - 75: Ii % O00Oo000ooO0
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 o00OooO0oo = ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIiII = Iiii ( o00OooO0oo )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( IIiII )
 for oOo0 , I11iiiiI1i , iiIIiI in o0O00oOoOO :
  Oo0000o = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iiiiI1i ) . replace ( '\\' , '' )
  if OO0oo in oOo0 . lower ( ) :
   oOO0OO0OO ( oOo0 , '' , 7022 , Oo0000o )
   if 33 - 33: OOooOOo * Ii1i111I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
iiIiII1 = '{ZH},' ; ii111iI = '{IX},' ; ii11I1 = '{LM},'
if 26 - 26: oO00Oo0o000 . OoOO00O + oOo0O0Ooo . OOooOOo + i1IiIIIII
def I1Ii1I ( url ) :
 Ii1111iiI = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( '<a class="season" href="(.+?)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Ii1111iiI )
 for url , i1I11 , oOoO00o , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( ( i1I11 ) . replace ( 'Sezon' , ' Season ' ) + ( oOoO00o ) . replace ( 'Bölüm' , ' Episode ' ) + oOo0 , url , 8063 , '' )
  if 15 - 15: O0oOO0 . I11i + OOooOOo . iI11I1II1I1I % O0oOO0 + o0o00Oo0O
  if 22 - 22: I11i + I1ii11iIi11i . O0oOO0 + Ii1I * IIiI1I . Ii
  if 90 - 90: i1IiIIIII * OOooOOo - I1ii11iIi11i + I11i
  if 53 - 53: ii . ii + I11i - IIiI1I + i1IiIIIII
def i1111iIII ( url ) :
 Ii1111iiI = cloudflare . source ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)",' , re . DOTALL ) . findall ( Ii1111iiI )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( oOo0 , url , 222 , '' )
  if 50 - 50: o0o00Oo0O * Ii1I + IIiIiII11i . ooOoO0O00 + OOooOOo
  if 39 - 39: iI11I1II1I1I + O0oOO0
  if 92 - 92: Ii1i111I % Ii % I1ii11iIi11i
  if 23 - 23: IIiIiII11i * IIiI1I
def o0Ooi1II11i1iI1 ( ) :
 if 81 - 81: O0O0O . ii * I11i * oO0o
 Ii1111iiI = cloudflare . source ( i1111 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 o0O00oOoOO = re . compile ( '<li id=".+?">.+?<a href="(.+?)">.+?<img width="40" height="40" src="(.+?)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Ii1111iiI )
 for o00OooO0oo , I11iiiiI1i , oOo0 , oOoO00o in o0O00oOoOO :
  oOO0OO0OO ( oOo0 + '  -  ' + ( oOoO00o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , o00OooO0oo , 8063 , I11iiiiI1i )
  if 10 - 10: O0O0O - IIiI1I % IIiIiII11i - oO00Oo0o000 - ooOoO0O00
def iIi11iI1i ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 8002 , I11iiiiI1i )
def Ii1iIi ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i , time , url , oOo0 , IIi11 in o0O00oOoOO :
  o0OOOO00O0Oo ( '%s %s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , time ) , url , 1015 , I11iiiiI1i , IIi11 )
  if 79 - 79: i1IiIIIII % oO00Oo0o000 / O0O0O - iI11I1II1I1I - OOooOOo
def o0oOO ( ) :
 if 84 - 84: Ii + O0oOO0 . o0o00Oo0O
 oOO0OO0OO ( 'Coronation Street' , '' , 8001 , '' )
 oOO0OO0OO ( 'Eastenders' , '' , 8002 , '' )
 oOO0OO0OO ( 'Emmerdale' , '' , 8003 , '' )
 oOO0OO0OO ( 'Hollyoaks' , '' , 8004 , '' )
 oOO0OO0OO ( 'Im a Celebrity' , '' , 8005 , '' )
 if 69 - 69: oO00Oo0o000 / ii % Ii
 if 18 - 18: Ii - O0oOO0 * O0O0O + I11i
 if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
 if 33 - 33: oO00Oo0o000 % IIiIiII11i
def IIi1II ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'Holly' in oOo0 :
   I11iiiiI1i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in o00OooO0oo :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o00OooO0oo . replace ( '\\/' , '/' ) , 8006 , I11iiiiI1i )
   else :
    pass
    if 40 - 40: i1IiIIIII / O00Oo000ooO0
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 29 - 29: OoOO00O - OoOO00O / O0oOO0
def I11IIII ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'East' in oOo0 :
   I11iiiiI1i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in o00OooO0oo :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o00OooO0oo . replace ( '\\/' , '/' ) , 8006 , I11iiiiI1i )
   else :
    pass
    if 38 - 38: ii . I11i . IIiIiII11i - IIiI1I
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: Ii + oOo0O0Ooo / I1ii11iIi11i % i1IiIIIII . OoOO00O + iI11I1II1I1I
def iI11I ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'Emmer' in oOo0 :
   I11iiiiI1i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in o00OooO0oo :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o00OooO0oo . replace ( '\\/' , '/' ) , 8006 , I11iiiiI1i )
   else :
    pass
    if 39 - 39: iI11I1II1I1I - O0O0O / O00Oo000ooO0 * o0o00Oo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: oOo0O0Ooo % ii / IIiI1I
def IiiiIIi ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)".+?target=_blank>(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'Coro' in oOo0 :
   I11iiiiI1i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in o00OooO0oo :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o00OooO0oo . replace ( '\\/' , '/' ) , 8006 , I11iiiiI1i )
   else :
    pass
    if 65 - 65: oO00Oo0o000 * IIiI1I / O00Oo000ooO0 + Ii * o0o00Oo0O - o0o00Oo0O
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: OoOO00O / Ii1I + O0O0O / i1IiIIIII + OOooOOo
def OOOii ( ) :
 IIiII = Iiii ( 'http://uksoapshare.blogspot.co.uk/' )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank">(.+?)</a>' ) . findall ( IIiII )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'Celeb' in oOo0 :
   I11iiiiI1i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in o00OooO0oo :
    oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , o00OooO0oo . replace ( '\\/' , '/' ) , 8006 , I11iiiiI1i )
   else :
    pass
    if 33 - 33: ii + oO00Oo0o000 / oO00Oo0o000 + oO00Oo0o000 * O00Oo000ooO0
def I1iIiiiIi1111I ( name , url ) :
 iII1i1ii = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iII1i1ii :
  i1I1ii1i = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  O0OOoOOO0oO = open_url ( url )
  url = re . compile ( 'src="(.+?)"></iframe>' ) . findall ( O0OOoOOO0oO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  O0OOoOOO0oO = open_url ( url )
  iiiiII11iIi = re . compile ( 'mp4","url":"(.+?)"' ) . findall ( O0OOoOOO0oO ) [ - 1 ]
  i1I1ii1i = iiiiII11iIi . replace ( '\\/' , '/' )
 O000oOo = xbmcgui . ListItem ( name , '' , '' )
 O000oOo . setPath ( i1I1ii1i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O000oOo )
 if 51 - 51: I1ii11iIi11i / O00Oo000ooO0 * OoOO00O - IIiIiII11i / oOo0O0Ooo . O00Oo000ooO0
 if 65 - 65: O00Oo000ooO0
def oooOOo0oOoOO ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 o0O00oOoOO = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="(.+?)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="(.+?)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , o00OooO0oo , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
 for o00OooO0oo , oOo0 in iIIi1i1 :
  oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , o00OooO0oo , 7071 , OOoOO0oo0ooO + 'popcorn.png' )
  if 6 - 6: O0O0O . Ii1i111I
def iIIII1 ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( '<a class="nav-item" href="(.+?)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'Movies' in oOo0 :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( o00OooO0oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , OOoOO0oo0ooO + 'popcorn.png' )
def Oooo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 o0O00oOoOO = re . compile ( '<a class="object-link size-poster".+?href="(.+?)" data-type="category">.+?src="(.+?)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iiiiI1i )
 for url in iIIi1i1 :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , OOoOO0oo0ooO + 'Next.png' )
  if 7 - 7: ooOoO0O00
  if 63 - 63: iI11I1II1I1I + O00Oo000ooO0 % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def OO0iiiii1iiIIii ( url ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , url , I11iiiiI1i in o0O00oOoOO :
  if '{{' in oOo0 :
   pass
  else :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , I11iiiiI1i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
II1IIii1I11I = '{UJ},' ; ii1IiIIiI11111Ii = '{WE},' ; O0OOo = '{WP},' ; O0o0O0 = '{PP},'
def OO0Oo00OO0oo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for oOo0 , url , I11iiiiI1i in o0O00oOoOO :
  if '{{' in oOo0 :
   pass
  else :
   oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , I11iiiiI1i )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOO00o0O0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="film-container">.+?<iframe src="(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  iIIii1iiiIiiI ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIIii1iiiIiiI ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'file: "(.+?)",.+?label: "(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 222 , OOoOO0oo0ooO + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: IIiIiII11i
 if 36 - 36: i1IiIIIII * OoOO00O
 if 16 - 16: IIiIiII11i
def oooOO0OO0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  if '(cooltvseries.com)' in oOo0 :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
 for url , oOo0 in iIIi1i1 :
  if '(cooltvseries.com)' in oOo0 :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , OOoOO0oo0ooO + 'CoolSeries.png' )
def iiI1i ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  III1I1 ( ( url ) . replace ( ' ' , '%20' ) )
OoOoIII1IiIi1 = '{XX},' ; oOOoO0O = '{UD},' ; OoOoO = '{YT},' ; oOOo00Ooo0O = '{JS},' ; iIii1Oo = '{PF},'
if 15 - 15: ooOoO0O00 + O00Oo000ooO0 % oOo0O0Ooo / Ii * OOooOOo
def oOiI1I ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="(.+?)" data-toggle="modal".+?data-target="#infoModal" name="(.+?)"> <img src="(.+?)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOo0O ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i1111 ( o00OooO0oo ) ) , 222 , I11iiiiI1i )
  if 6 - 6: oO0o
def OO000OOOo0Oo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i , url , oOo0 in o0O00oOoOO :
  if 'youtu' in url :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + I11iiiiI1i )
 for url in next :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT[/COLOR]' , url , 7050 , OOoOO0oo0ooO + 'Next.png' )
  if 75 - 75: IIiIiII11i + O0oOO0 % i1IiIIIII + I1ii11iIi11i
def oOoOOoo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 65 - 65: Ii - O0oOO0 * Ii1i111I + O0oOO0 / O00Oo000ooO0 + I11i
def IiII1I ( url ) :
 O0OOoOOO0oO = Iiii
 o0O00oOoOO = re . compile ( 'id:"(.+?)",url:"(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 222 , I11iiiiI1i )
  if 72 - 72: OoOO00O / I1ii11iIi11i / O0O0O * OOooOOo + i1IiIIIII
  if 58 - 58: I11i % oOo0O0Ooo . oOo0O0Ooo * oO0o - O00Oo000ooO0 . ii
  if 10 - 10: oO00Oo0o000
  if 48 - 48: IIiI1I * ooOoO0O00 % ii * OoOO00O * oO0o
  if 7 - 7: IIiI1I . OoOO00O . IIiI1I - oO00Oo0o000
def I1IiiI ( ) :
 if 29 - 29: IIiI1I . IIiI1I
 oOO0OO0OO ( 'All Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Entertainment' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Movies' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Music' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'News' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Sports' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Documentary' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Kids' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Food' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Religious' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'USA Channels' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 oOO0OO0OO ( 'Other' , '' , 7021 , OOoOO0oo0ooO + 'livetv.png' )
 if 20 - 20: i1IiIIIII - IIiI1I / I1ii11iIi11i * oO0o
 if 55 - 55: ii
def OO0OOOOOo ( Cat_Name ) :
 if 7 - 7: o0o00Oo0O + OoOO00O . IIiIiII11i
 iii11i1i1 = False
 o00OOo0o = '0'
 if Cat_Name == 'All Channels' : iii11i1i1 = True
 if Cat_Name == 'Entertainment' : o00OOo0o = '1'
 if Cat_Name == 'Movies' : o00OOo0o = '2'
 if Cat_Name == 'Music' : o00OOo0o = '3'
 if Cat_Name == 'News' : o00OOo0o = '4'
 if Cat_Name == 'Sports' : o00OOo0o = '5'
 if Cat_Name == 'Documentary' : o00OOo0o = '6'
 if Cat_Name == 'Kids' : o00OOo0o = '7'
 if Cat_Name == 'Food' : o00OOo0o = '8'
 if Cat_Name == 'Religious' : o00OOo0o = '9'
 if Cat_Name == 'USA Channels' : o00OOo0o = '10'
 if Cat_Name == 'Other' : o00OOo0o = '11'
 if 48 - 48: Ii / IIiIiII11i + OoOO00O + I11i . oO00Oo0o000 % i1IiIIIII
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 print 'Len Match: >>>' + str ( len ( o0O00oOoOO ) )
 for oOo0 , I11iiiiI1i , iiIIiI in o0O00oOoOO :
  Oo0000o = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iiiiI1i ) . replace ( '\\' , '' )
  if iiIIiI == o00OOo0o :
   oOO0OO0OO ( oOo0 , '' , 7022 , Oo0000o )
  elif iii11i1i1 == True :
   oOO0OO0OO ( oOo0 , '' , 7022 , Oo0000o )
  else : pass
  if 88 - 88: oO00Oo0o000 . oO00Oo0o000
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 71 - 71: O0oOO0 . Ii1I * o0o00Oo0O - oO00Oo0o000 - IIiIiII11i
def iIIi11ii ( Search_Name ) :
 O0OOoOOO0oO = Iiii ( i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 o0O00oOoOO = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i , o00OooO0oo , I1IiI11 , iIiIiIiI in o0O00oOoOO :
  Oo0000o = i1111 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( I11iiiiI1i ) . replace ( '\\' , '' )
  oOo0O ( Search_Name + ': Link 1' , ( o00OooO0oo ) . replace ( '\\' , '' ) , 222 , Oo0000o )
  oOo0O ( Search_Name + ': Link 2' , ( I1IiI11 ) . replace ( '\\' , '' ) , 222 , Oo0000o )
  oOo0O ( Search_Name + ': Link 3' , ( iIiIiIiI ) . replace ( '\\' , '' ) , 222 , Oo0000o )
  if 78 - 78: O00Oo000ooO0 - Ii1i111I % o0o00Oo0O - i1IiIIIII % oO0o
def i11IiIi ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  oOo0O ( oOo0 , ( o00OooO0oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , OOoOO0oo0ooO + 'english.png' )
def I111O0 ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  oOo0O ( oOo0 , ( o00OooO0oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'xxx.png' )
def oooIiII ( ) :
 O0OOoOOO0oO = Iiii ( i1111 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 o0O00oOoOO = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( O0OOoOOO0oO )
 for oOo0 , o00OooO0oo in o0O00oOoOO :
  oOo0O ( oOo0 , ( o00OooO0oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , OOoOO0oo0ooO + 'vod(1).png' )
  if 13 - 13: IIiIiII11i
def oO0o000oOO ( url ) :
 url
 Ii11Iiii = xbmcgui . ListItem ( oOo0 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii11Iiii )
 return
 if 98 - 98: ooOoO0O00 % I1ii11iIi11i
 if 82 - 82: O0oOO0
def OoOooO0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a class=.+?href="(.+?)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="(.+?)" class="videothumb" alt="(.+?)"></div>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( O0OOoOOO0oO )
 for url , I11i1II , I11iiiiI1i , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + I11iiiiI1i , '' , ( I11i1II ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 for url in iIIi1i1 :
  oOO0OO0OO ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , OOoOO0oo0ooO + 'Next.png' )
  if 9 - 9: OOooOOo - O00Oo000ooO0
def iiIi ( url ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( IIiII )
 for url , I11i1II , I11iiiiI1i in o0O00oOoOO :
  OOooOoooOoOo ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + I11iiiiI1i , '' , I11i1II )
  oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 III1Ii1i1I1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( IIiII )
 for IiI111 in III1Ii1i1I1 :
  OO0OO00ooO0 = ( IiI111 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  o0OOOO00O0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + I11iiiiI1i , '' , OO0OO00ooO0 )
  if 68 - 68: OOooOOo * Ii1I - ii - Ii1i111I + iI11I1II1I1I * Ii
def OoO ( INFO ) :
 o00oO0oo0OO ( 'info for workout' , INFO )
 if 34 - 34: I1ii11iIi11i - OoOO00O - IIiI1I
 if 61 - 61: Ii1I
 if 33 - 33: OOooOOo / oO0o
def I1ii1iI ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'cat-item-.+?"><a href="(.+?)" >(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , url , 9031 , OOoOO0oo0ooO + 'icon.png' )
def i1i1IIi ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" title=".+?" rel="bookmark"><time class="entry-date published updated" datetime=".+?">(.+?)</time></a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , url , 9032 , OOoOO0oo0ooO + 'icon.png' )
def i1Ii1i1ii1 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '#EXTINF:-.+?,(.+)\s*(.+)\s*' ) . findall ( O0OOoOOO0oO )
 for oOo0 , url in o0O00oOoOO :
  if '://' in oOo0 :
   pass
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '<br />' , '' ) , ( url ) . replace ( '<br />' , '' ) , 222 , OOoOO0oo0ooO + 'icon.png' )
def oOOoOOooO0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( O0OOoOOO0oO )
 for oOo0 , url in o0O00oOoOO :
  oOo0O ( oOo0 , url , 222 , OOoOO0oo0ooO + 'icon.png' )
  if 42 - 42: iI11I1II1I1I * OoOO00O / oO0o + i1IiIIIII
  if 48 - 48: ii - oO00Oo0o000 . Ii * IIiI1I - OoOO00O - I11i
  if 59 - 59: IIiI1I / Ii1i111I . I1ii11iIi11i
def o0III11IiI ( ) :
 O0OOoOOO0oO = Iiii ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 o0O00oOoOO = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  if 'category' in o00OooO0oo :
   oOO0OO0OO ( oOo0 , 'http://www.disclose.tv/' + o00OooO0oo , 7010 , OOoOO0oo0ooO + 'disclose.png' )
   if 53 - 53: IIiI1I / ooOoO0O00 / ooOoO0O00
   if 77 - 77: Ii1i111I + ooOoO0O00 . Ii1i111I
def oO0OOO ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 , I11iiiiI1i in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , 'http://www.disclose.tv/' + url , 7011 , I11iiiiI1i )
 for url in next :
  oOO0OO0OO ( 'NEXT' , url , 7010 , OOoOO0oo0ooO + 'Next.png' )
  if 42 - 42: iI11I1II1I1I % OoOO00O - Ii1I + iI11I1II1I1I
  if 27 - 27: o0o00Oo0O / oO0o
def O000oooO0 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( O0OOoOOO0oO )
 I11IIiIiI = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  if 'http' in url :
   oOo0O ( 'video/flv' , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url , oOo0 in iIIi1i1 :
  oOo0O ( oOo0 , url , 222 , OOoOO0oo0ooO + 'disclose.png' )
 for url in I11IIiIiI :
  oOo0O ( 'YT Link' , url , 8043 , OOoOO0oo0ooO + 'disclose.png' )
  if 75 - 75: Ii
  if 44 - 44: iI11I1II1I1I * oO00Oo0o000 * I1ii11iIi11i * Ii1I + Ii1i111I
def III1i1IIII1i ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , OOoOO0oo0ooO + 'icon.png' )
  if 48 - 48: ii
def Oo0OOOOOOO0oo ( name , url , img ) :
 IIiII = Iiii ( url )
 II1Iiiii111i = re . compile ( '<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( IIiII )
 OooooO0o0 = len ( II1Iiiii111i )
 if 99 - 99: i1IiIIIII * ooOoO0O00 . OoOO00O * oO00Oo0o000 . O0oOO0
 if 54 - 54: IIiI1I . ooOoO0O00 . Ii1I * I11i % IIiI1I
 if OooooO0o0 == 1 :
  for i1IIi111iI in II1Iiiii111i :
   i1IIi111iI = i1IIi111iI . replace ( 'player' , 'watch' )
   IiIiII11i1 = i1IIi111iI + '&fv=&sou='
   Ii1I1iIiiI1 = Iiii ( IiIiII11i1 )
   o00i111iiIiiIiI = re . compile ( '<source src="(.+?)" type=".+?">' , re . DOTALL ) . findall ( Ii1I1iIiiI1 )
   for iiIiii in o00i111iiIiiIiI :
    OOooooO = False
    Resolve ( iiIiii )
    if 80 - 80: OOooOOo + iI11I1II1I1I . O00Oo000ooO0
 elif OooooO0o0 > 1 :
  if 76 - 76: oOo0O0Ooo * i1IiIIIII
  for i1IIi111iI in II1Iiiii111i :
   ii111 = Iiii ( i1IIi111iI )
   IIiiI11 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( ii111 )
   IiIII = IIiiI11
   IiIII = ( str ( IiIII ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IiIII
   oOo0O ( 'DOUBLE LINK' , IiIII , 424 , '' )
   if 92 - 92: oOo0O0Ooo % IIiI1I
   for url in IIiiI11 :
    oOO0OO0OO ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1IiI11 = Google . resolve ( url )
    except :
     pass
    try :
     iiiI1IiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1IiI11 ) )
     for Ii111IIIIii , O00oIii1iIIiii1ii in iiiI1IiI :
      if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . OoOO00O % oO0o
      HD_URLS . append ( Ii111IIIIii )
      SD_URLS . append ( O00oIii1iIIiii1ii )
    except :
     pass
 else :
  pass
  if 2 - 2: ii - OoOO00O % O0O0O / oOo0O0Ooo / I11i
def iiII ( ) :
 if 30 - 30: O0oOO0
 if 57 - 57: I11i * Ii / OOooOOo
 oOO0OO0OO ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , OOoOO0oo0ooO + 'Movies.png' )
 if 40 - 40: iI11I1II1I1I - O0oOO0 / I1ii11iIi11i
 oOO0OO0OO ( 'Search Movies' , '' , 7017 , OOoOO0oo0ooO + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 24 - 24: O0O0O - IIiI1I / O0oOO0
 if 10 - 10: OOooOOo * ooOoO0O00
def I1Ii1ii ( ) :
 O0OOoOOO0oO = Iiii ( 'http://cnfstudio.com/' )
 o0O00oOoOO = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , 'http://cnfstudio.com/genre/' + o00OooO0oo , 7003 , OOoOO0oo0ooO + 'icon.png' )
  if 34 - 34: oOo0O0Ooo
oooOOOOO = xbmcgui . Dialog ( )
if 57 - 57: i1IiIIIII . OoOO00O % I11i
I1I11 = '{UN},' ; iI1i1iI1iI = '{IG},' ; I1IIiIi = '{PL},' ; OOOOoOoO = '{LO},' ; OO000 = '{LP},' ; o0oOoo0o = '{HA},' ; IiiIiIIi = '{XD},' ; O00Oo = '{TA},' ; oOOoooo0O0 = '{DP},' ; Ii111Ii11 = '{JT},' ; Ii1 = '{JJ},' ; IIIIiII = '{MM},' ; iII11 = '{FQ},' ; O00OO00OOOoO = '{HH},'
if 47 - 47: ooOoO0O00 % O0oOO0 - I1ii11iIi11i * Ii1i111I / Ii
def Iii1Iii ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iiI11111II = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i , url , oOo0 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , I11iiiiI1i )
 iiI11111II = iiI11111II
 for url in iiI11111II :
  oOO0OO0OO ( 'Next Page' , url , 7003 , OOoOO0oo0ooO + 'Next.png' )
  if 48 - 48: IIiI1I % Ii . ii * O00Oo000ooO0 % oO0o . IIiI1I
def IiOOo0 ( url ) :
 if 85 - 85: oO00Oo0o000 % Ii1I
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  O00oO = url + '&fv=&sou='
  O00oO = O00oO . replace ( 'player' , 'watch' )
  OO00o0O0oOooO = IiiIII1IIii1 ( O00oO )
  I11iIi1i1I1i1 = IiiIII1IIii1 ( url )
  if 14 - 14: Ii1i111I
  if 18 - 18: oOo0O0Ooo
def IiiIII1IIii1 ( url ) :
 if 23 - 23: ii * IIiIiII11i
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<video id=".+?<source src="(.+?)" type="video/mp4">' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  iI1iiiiIii ( url )
  if 70 - 70: Ii1I + oOo0O0Ooo
  if 65 - 65: IIiI1I - IIiI1I . I1ii11iIi11i
def oO00o0O00o ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Local M3u[/COLOR]' , oOo0oooo00o , 2001 , OOoOO0oo0ooO + 'LocalM3U.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']Remote M3u[/COLOR]' , Oo0o0000o0o0 , 7080 , OOoOO0oo0ooO + 'RemoteM3U.png' , i1iIIi1 , '' )
 if 78 - 78: Ii + iI11I1II1I1I
def oOOI1 ( ) :
 if os . path . exists ( oOo0oooo00o ) :
  OOI1i = open ( oOo0oooo00o , 'r' )
  for Ii11Iiii in OOI1i :
   i1II1iII1 = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( Ii11Iiii )
   for oOo0 , o00OooO0oo in i1II1iII1 :
    oOo0O ( oOo0 , o00OooO0oo , 222 , OOoOO0oo0ooO + 'streams.png' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 31 - 31: OoOO00O * I11i * OoOO00O + oO0o * I11i . oO00Oo0o000
def Oo00oo00o00Oo ( url ) :
 if os . path . exists ( Remote ) :
  IIiII = I1ii11 ( url )
  o0O00oOoOO = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
  for oOo0 , url in o0O00oOoOO :
   url = ( url ) . strip ( )
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  oOOoo00O0O . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  o0oO0 . openSettings ( sys . argv [ 0 ] )
  if 1 - 1: O00Oo000ooO0
  if 31 - 31: ooOoO0O00
def i1iIi ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for o00OooO0oo in o0O00oOoOO :
  o00OooO0oo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + o00OooO0oo
 oOo0 = 'plugin.video.GenieTv'
 if 21 - 21: ooOoO0O00
 OOOO00 ( o00OooO0oo , oOo0 )
 if 92 - 92: Ii1i111I % o0o00Oo0O % OoOO00O . OoOO00O . O00Oo000ooO0
def IIII ( ) :
 IIiII = Iiii ( i1111 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 o0O00oOoOO = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( IIiII )
 for o00OooO0oo in o0O00oOoOO :
  o00OooO0oo = i1111 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + o00OooO0oo
 oOo0 = 'repository.GenieTv'
 if 82 - 82: I1ii11iIi11i + OOooOOo . Ii1I % O0O0O / OoOO00O
 OOOO00 ( o00OooO0oo , oOo0 )
 if 37 - 37: O0O0O % oO00Oo0o000 % O0O0O
 if 14 - 14: oO0o / oOo0O0Ooo
def oO0o0 ( ) :
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']CATAGORIES[/COLOR]' , '' , 10051 , OOoOO0oo0ooO + 'Catagories.png' , i1iIIi1 , '' )
 o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']SEARCH[/COLOR]' , '' , 10052 , OOoOO0oo0ooO + 'Search.png' , i1iIIi1 , '' )
 if 43 - 43: i1IiIIIII
 if 84 - 84: i1IiIIIII . O00Oo000ooO0 . IIiI1I
o0oO0 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
oOOoo00O0O = xbmcgui . Dialog ( )
i1iiIII111ii = xbmc . translatePath ( 'special://home/' )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
iIII1I1i = 'https://addons.tvaddons.ag/'
if 26 - 26: IIiI1I - I1ii11iIi11i + oOo0O0Ooo + I11i
def III1iI1Ii11Ii ( ) :
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 OooO0ooO0o0 = 'https://addons.tvaddons.ag/search/?keyword=' + OOO0000oO
 IIiII = Iiii ( OooO0ooO0o0 )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for o00OooO0oo , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , o00OooO0oo , 10054 , 'https://addons.tvaddons.ag/' + Oo0oooO0oO , i1iIIi1 , '' )
  if 29 - 29: OOooOOo
  if 37 - 37: IIiIiII11i % IIiIiII11i + I11i % I1ii11iIi11i / oOo0O0Ooo . O0O0O
def o0i1I ( ) :
 IIiII = Iiii ( iIII1I1i )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  if 'Repositories' in oOo0 :
   pass
  elif 'Services' in oOo0 :
   pass
  elif 'International' in oOo0 :
   pass
  else :
   o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , o00OooO0oo , 10053 , 'https://addons.tvaddons.ag/' + I11iiiiI1i , i1iIIi1 , '' )
   if 44 - 44: i1IiIIIII * ooOoO0O00
   if 83 - 83: I11i % o0o00Oo0O + iI11I1II1I1I + O0O0O * I1ii11iIi11i * O0oOO0
def Addon ( url ) :
 IIiII = Iiii ( url )
 IIi1iI11Ii = re . compile ( '<li class="nextPage"><a class=".+?" href="(.+?)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( IIiII )
 for url in IIi1iI11Ii :
  o0OOOO00O0Oo ( '[COLOR' + oO0o0o0ooO0oO + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , OOoOO0oo0ooO + 'Next.png' , i1iIIi1 , '' )
 o0O00oOoOO = re . compile ( '<li><a href="(.+?)"><span class=".+?"><img src="(.+?)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( IIiII )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  if 'Please' in oOo0 :
   pass
  else :
   o0OOOO00O0Oo ( oOo0 , url , 10054 , 'https://addons.tvaddons.ag/' + I11iiiiI1i , i1iIIi1 , '' )
   if 20 - 20: I11i / O00Oo000ooO0
   if 25 - 25: OOooOOo + oO0o % OoOO00O % i1IiIIIII / O0O0O
def OOoOo ( url , name ) :
 IIiII = Iiii ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)"' ) . findall ( IIiII )
 for url in o0O00oOoOO :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   Oo0oO0ooo = xbmcgui . DialogProgress ( )
   Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
   ooO000O = os . path . join ( IiiioooOOoooo , name + '.zip' )
   try :
    os . remove ( ooO000O )
   except :
    pass
   downloader . download ( url , ooO000O , Oo0oO0ooo )
   II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print II11iIII1i1I
   print '======================================='
   extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
   i1I1IiiIi1i ( )
   if 27 - 27: oOo0O0Ooo * Ii / o0o00Oo0O / IIiIiII11i
def OOOO00 ( url , name ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( "Origin+Jaybox" , "Downloading Content" , '' , 'Please Wait' )
 ooO000O = os . path . join ( IiiioooOOoooo , name + '.zip' )
 try :
  os . remove ( ooO000O )
 except :
  pass
 downloader . download ( url , ooO000O , Oo0oO0ooo )
 II11iIII1i1I = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 Oo0oO0ooo . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print II11iIII1i1I
 print '======================================='
 extract . all ( ooO000O , II11iIII1i1I , Oo0oO0ooo )
 i1I1IiiIi1i ( )
 if 72 - 72: O0O0O - I1ii11iIi11i / Ii * oOo0O0Ooo + oO0o
def i1I1IiiIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 47 - 47: i1IiIIIII / IIiIiII11i % O00Oo000ooO0 . O0O0O * Ii1I
 if 35 - 35: I1ii11iIi11i * IIiIiII11i
def IIi1i1IIi ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , url , 1007 , Oo0oooO0oO )
def o0oo0Ooo0 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 1006 , Oo0oooO0oO )
  if 74 - 74: OoOO00O + Ii1I + oOo0O0Ooo
  if 37 - 37: O00Oo000ooO0
def OOO0O ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , iconimage , I11i1II , III1ii1I , name in o0O00oOoOO :
  if 'http' in url :
   if '.php' in url :
    II1ii1ii11I1 ( name , url , 1016 , iconimage , III1ii1I , I11i1II )
   else :
    if 'youtube' in url :
     Oo000 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , III1ii1I , I11i1II )
    else :
     I1iiIII = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
     for Ii11Iiii in I1iiIII :
      if Ii11Iiii == url :
       name = '[COLORred]Watched - [/COLOR]' + name
     Oo000 ( name , url , 222 , iconimage , III1ii1I , I11i1II )
     oO00OOoO00 ( 'movies' , 'INFO' )
  else :
   II1III ( url , iconimage , name )
   if 14 - 14: Ii1I * oO00Oo0o000 % ooOoO0O00 / Ii1I
 else :
  o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
  for url , Oo0oooO0oO , name in o0O00oOoOO :
   if 'http' in url :
    if '.php' in url :
     oOO0OO0OO ( name , url , 1016 , Oo0oooO0oO )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOo0O ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , Oo0oooO0oO )
     else :
      I1iiIII = re . compile ( 'url="(.+?)"\n' ) . findall ( str ( OOOO ) )
      for Ii11Iiii in I1iiIII :
       if Ii11Iiii == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOo0O ( name , url , 222 , Oo0oooO0oO )
      oO00OOoO00 ( 'movies' , 'INFO' )
   else :
    II1III ( url , Oo0oooO0oO , name )
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 48 - 48: I1ii11iIi11i
def II1III ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OO00oO0o0 = ( url ) . replace ( ii111iI , 'http' ) . replace ( oOOoO0O , '.com' ) ;
 o0oOo = ( OO00oO0o0 ) . replace ( ii11I1 , 'a' ) . replace ( ooOO0OOO00o , 'b' ) . replace ( OoOoO0ooooO0 , 'c' ) . replace ( ii1IiIIiI11111Ii , 'd' ) . replace ( I1IIiIi , 'e' ) . replace ( Ii111Ii11 , 'f' ) ;
 O0OoOo0oO0o = ( o0oOo ) . replace ( OoOoIII1IiIi1 , 'g' ) . replace ( o0oOoo0o , 'h' ) . replace ( OoOoO , 'i' ) . replace ( iIii1Oo , 'j' ) . replace ( IIII1ii1 , 'k' ) . replace ( OOO0O0OOo , 'l' ) ;
 I11iIi1i1IIi = ( O0OoOo0oO0o ) . replace ( II11I , 'm' ) . replace ( OOooo00oo , 'n' ) . replace ( i1iiIi1IiiiI , 'o' ) . replace ( OO0oooOO , 'p' ) . replace ( IIIi1iiIIiiiI , 'q' ) . replace ( I1IIiIi1iI , 'r' ) ;
 oOo0Iiii11 = ( I11iIi1i1IIi ) . replace ( o00000O , 's' ) . replace ( O0OOo , 't' ) . replace ( iIiiiII11 , 'u' ) . replace ( ooo00Oo0 , 'v' ) . replace ( iIii1i1Ii , 'w' ) . replace ( III1iIii , 'x' ) ;
 iiIII1i1 = ( oOo0Iiii11 ) . replace ( oOOo0OOoOO0 , 'y' ) . replace ( IiIi , 'z' ) . replace ( I1I11 , '.' ) . replace ( iI1i1iI1iI , '(' ) . replace ( OOOOoOoO , ')' ) . replace ( OO000 , '/' ) ;
 IIi1IiiIi1III = ( iiIII1i1 ) . replace ( iiIiII1 , '1' ) . replace ( O0o0O0 , '2' ) . replace ( IiIiIiiIIii , '3' ) . replace ( O00Oo , '4' ) . replace ( oOOoooo0O0 , '5' ) . replace ( oOOo00Ooo0O , '6' ) ;
 OOo00O00o0O0 = ( IIi1IiiIi1III ) . replace ( Ii1 , '7' ) . replace ( IIIIiII , '8' ) . replace ( iII11 , '9' ) . replace ( O00OO00OOOoO , '0' ) . replace ( i1IiIIi , ':' ) . replace ( OOOOo0 , '%' ) ;
 url = ( OOo00O00o0O0 ) . replace ( II1IIii1I11I , '-' ) . replace ( IiiIiIIi , '_' ) ;
 oOo0O ( name , url , 222 , iconimage ) ;
 if 31 - 31: oOo0O0Ooo
 if 36 - 36: oO0o + oO0o + oO0o % I1ii11iIi11i * IIiI1I
def O0IIi1i ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , o00OooO0oo , 1007 , Oo0oooO0oO )
def oO0oi1I1iI1 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 1006 , Oo0oooO0oO )
  if 91 - 91: O0O0O / iI11I1II1I1I + O0O0O
def iii1i1Iiiiiii ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOoo0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOoo0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoo0 )
 if 7 - 7: oOo0O0Ooo % oO00Oo0o000 * O00Oo000ooO0 + OOooOOo / OOooOOo
 if 34 - 34: IIiIiII11i % Ii % oO0o . OOooOOo + Ii
def OoOoO00O ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O0OOoOOO0oO )
 for url , I11iiiiI1i , oOo0 in o0O00oOoOO :
  if '-dir-' in oOo0 :
   oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , I11iiiiI1i )
  else :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' , url , 1006 , I11iiiiI1i )
   if 58 - 58: Ii1I % OoOO00O * OoOO00O - IIiI1I
def I111IiI11 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 oOO00OoOo = ( 'http://afewbitsmore.com/' )
 o0O00oOoOO = re . compile ( '<A HREF="(.+?)">(.+?)</A><br>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  if '[To Parent Directory]' in oOo0 :
   oOo0 = 'HOME'
   pass
  elif 'HOME' in oOo0 :
   pass
  elif '.m3u' in oOo0 :
   oOO0OO0OO ( '[COLOR' + oO0o0o0ooO0oO + ']PLAY ALL[/COLOR]' , oOO00OoOo + url , 2002 , OOoOO0oo0ooO + 'music.png' )
  elif '.mp3' in oOo0 :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , oOO00OoOo + url , 222 , OOoOO0oo0ooO + 'music.png' )
  elif '.m4a' in oOo0 :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , oOO00OoOo + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) , oOO00OoOo + url , 1012 , OOoOO0oo0ooO + 'music.png' )
def oOoo ( url ) :
 IIiII = I1ii11 ( url )
 o0O00oOoOO = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( IIiII )
 for I11iiiiI1i , oOo0 , url in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , OOoOO0oo0ooO + 'music.png' )
  if 68 - 68: i1IiIIIII + OoOO00O
def o0o0oooO00O0 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 oOO00OoOo = url
 o0O00oOoOO = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  if '.mp3' in oOo0 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , OOoOO0oo0ooO + 'music.png' )
  else :
   oOO0OO0OO ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '/' , '' ) , oOO00OoOo + url , 1011 , OOoOO0oo0ooO + 'music.png' )
def iiiI ( ) :
 O0OOoOOO0oO = I1ii11 ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)"><img src="(.+?)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , I11iiiiI1i , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , ( 'http://www.cyn.net/music/' + o00OooO0oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + I11iiiiI1i ) . replace ( ' ' , '%20' ) )
def IIi1 ( url , img ) :
 O0OOoOOO0oO = I1ii11 ( url )
 I1IiI11 = url
 img = img
 o0O00oOoOO = re . compile ( '<a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I1IiI11 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 44 - 44: oO0o + Ii1i111I % oO0o + ooOoO0O00 + IIiI1I + o0o00Oo0O
def Ii1iII1ii1 ( url ) :
 O0OOoOOO0oO = I1ii11 ( url )
 I1IiI11 = url
 o0O00oOoOO = re . compile ( 'alt="(.+?)"></td><td><a href="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 for type , url , oOo0 in o0O00oOoOO :
  if '[VID]' in type :
   oOo0O ( ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I1IiI11 + url , 222 , OOoOO0oo0ooO + 'music.png' )
  if '[DIR]' in type :
   Ii1iII1ii1 ( I1IiI11 + url )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: iI11I1II1I1I / Ii + IIiI1I
 if 41 - 41: oO00Oo0o000 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def ooooOoo00 ( ) :
 i1IiiI = ( i1111 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 OO0oo = oOOoo00O0O . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOO0000oO = OO0oo . lower ( )
 o00OooO0oo = ( i1111 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1IiI11 = ( i1111 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iIiIiIiI = ( i1111 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 7 - 7: i1IiIIIII * oO0o + ii . O0oOO0 * Ii1i111I
 IIiII = i1I1iI ( o00OooO0oo )
 o0ooOooo000oOO = i1I1iI ( I1IiI11 )
 Oo0oOOo = i1I1iI ( iIiIiIiI )
 if 82 - 82: iI11I1II1I1I * ii
 if IIiII != 'Failed' :
  o0O00oOoOO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for oOo0 in o0O00oOoOO :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o00OooO0oo + oOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 50 - 50: oO00Oo0o000 - IIiIiII11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if o0ooOooo000oOO != 'Failed' :
  iIIi1i1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( IIiII )
  for oOo0 in iIIi1i1 :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( I1IiI11 + oOo0 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 33 - 33: O00Oo000ooO0 / O00Oo000ooO0 . Ii * Ii1I + I11i
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
 if Oo0oOOo != 'Failed' :
  I11IIiIiI = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Oo0oOOo )
  for oOo0 in I11IIiIiI :
   if OO0oo in oOo0 . lower ( ) :
    oOO0OO0OO ( ( oOo0 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIiIiIiI + oOo0 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 16 - 16: O00Oo000ooO0
    oO00OOoO00 ( 'tvshows' , 'Media Info 3' )
    if 10 - 10: OOooOOo . O00Oo000ooO0 * iI11I1II1I1I - O0O0O - OOooOOo / oO00Oo0o000
    if 13 - 13: O0O0O + OOooOOo % O00Oo000ooO0 % ii
    if 22 - 22: oO00Oo0o000
    if 23 - 23: o0o00Oo0O
    if 41 - 41: ooOoO0O00 . i1IiIIIII / O0oOO0 / I11i % O00Oo000ooO0 - OoOO00O
    if 14 - 14: Ii1I - Ii * oO00Oo0o000
II11I = '{SF},' ; OOooo00oo = '{IF},' ; i1iiIi1IiiiI = '{PW},' ; IiIiIiiIIii = '{AM},' ; OO0oooOO = '{GF},' ; IIIi1iiIIiiiI = '{DD},' ; I1IIiIi1iI = '{UO},' ; o00000O = '{LE},' ; iIiiiII11 = '{ZY},' ; ooo00Oo0 = '{UE},' ; iIii1i1Ii = '{PE},' ; III1iIii = '{JE},' ; oOOo0OOoOO0 = '{TH},' ; IiIi = '{LK},'
if 39 - 39: ii
if 19 - 19: Ii
def oOOOOOoOOoo0 ( ) :
 O0OOoOOO0oO = Iiii ( 'http://www.iwatchseries.me/tv-list/' )
 o0O00oOoOO = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , o00OooO0oo , 8021 , OOoOO0oo0ooO + 'iwatch.png' )
def oo0OOO0OOoOO ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 , o0O0Oo00 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 + o0O0Oo00 , url , 8022 , OOoOO0oo0ooO + 'iwatch.png' )
def oOoO ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  II1i1 ( url )
def II1i1 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '{.+?"file" : "(.+?)",.+?"default" : true.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 iIIi1i1 = re . compile ( 'setup\(\{.+?file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( O0OOoOOO0oO )
 I11IIiIiI = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOo0O ( 'VidSpot - ' + oOo0 , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for url in iIIi1i1 :
  oOo0O ( 'VodLocker' , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
 for oOo0 , url in I11IIiIiI :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOo0O ( 'TheVideo - ' + oOo0 , url , 222 , OOoOO0oo0ooO + 'iwatch.png' )
   if 51 - 51: O0oOO0 * IIiI1I / ooOoO0O00
def IIi1I1 ( ) :
 O0OOoOOO0oO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 o0O00oOoOO = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , o00OooO0oo , 1021 , OOoOO0oo0ooO + 'anime.png' )
  if 37 - 37: I11i * I1ii11iIi11i
  if 11 - 11: O0O0O
def Oo0O0o00o00 ( ) :
 O0OOoOOO0oO = Iiii ( 'http://www.animetoon.org/cartoon' )
 o0O00oOoOO = re . compile ( '<td><a href="(.+?)">(.+)</a></td>' ) . findall ( O0OOoOOO0oO )
 for o00OooO0oo , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , o00OooO0oo , 1002 , OOoOO0oo0ooO + 'anime.png' )
  if 90 - 90: oO00Oo0o000 . IIiIiII11i . Ii1I
  if 32 - 32: O0oOO0 - oO0o . IIiI1I . IIiI1I % ooOoO0O00 * OoOO00O
  if 65 - 65: IIiI1I / O0oOO0 . IIiIiII11i
def o0oO00oooo ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 iIIi1i1 = re . compile ( '<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( O0OOoOOO0oO )
 for I11iiiiI1i in iIIi1i1 :
  IiOOOo00 = I11iiiiI1i
 I11IIiIiI = re . compile ( '<li><a href="(.+?)">Next</a></li>' ) . findall ( O0OOoOOO0oO )
 for url in I11IIiIiI :
  oOO0OO0OO ( 'NEXT PAGE' , url , 1002 , OOoOO0oo0ooO + 'Next.png' )
 o0O00oOoOO = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0OOoOOO0oO )
 for url , oOo0 in o0O00oOoOO :
  oOO0OO0OO ( oOo0 , url , 1003 , IiOOOo00 )
 xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0Oo00O ( url , IMAGE ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( O0OOoOOO0oO )
 for oOo0 , url in o0O00oOoOO :
  print oOo0 + '     ' + url
  if 'easy' in url :
   I1iII1 ( url )
  elif 'playpanda' in url :
   I1iII1 ( url )
   if 70 - 70: ooOoO0O00 % O0oOO0 . Ii1I - O00Oo000ooO0 + i1IiIIIII
  xbmcplugin . addSortMethod ( O00o0OO , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iII1 ( url ) :
 O0OOoOOO0oO = Iiii ( url )
 o0O00oOoOO = re . compile ( "url: '(.+?)'," ) . findall ( O0OOoOOO0oO )
 for url in o0O00oOoOO :
  oOo0O ( 'STREAM' , url , 222 , OOoOO0oo0ooO + 'anime.png' )
  if 84 - 84: O0O0O + IIiIiII11i * IIiIiII11i % I11i / IIiI1I + O0oOO0
  if 9 - 9: IIiI1I
def iIi11I1II ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 oo0OooOOo0 . add_header ( 'referer' , url )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 93 - 93: Ii1I - O0oOO0 % Ii1I
def I1ii11 ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 12 - 12: i1IiIIIII + oO0o * Ii1i111I + OoOO00O + O00Oo000ooO0
def O0O00oOo0o000 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1iIIIiIi1 = ( '%s%s' % ( IiI1 , url ) )
 O00oO = I1ii11 ( url )
 o0O00oOoOO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( O00oO )
 for url , Oo0oooO0oO , oOo0 in o0O00oOoOO :
  oOo0O ( '%s' % ( '[COLOR' + oO0o0o0ooO0oO + ']' + oOo0 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , Oo0oooO0oO )
  if 85 - 85: oOo0O0Ooo % O0oOO0
def iI1iiiiIii ( url ) :
 if 25 - 25: OOooOOo . IIiIiII11i * OoOO00O
 IiII111I = open ( oOoOooOo0o0 , "a" )
 IiII111I . write ( 'url="' + url + '"\n' )
 IiII111I . close
 if 62 - 62: ooOoO0O00 * iI11I1II1I1I % O0O0O % OOooOOo / ii
 ooooOoO0O = xbmc . Player ( oOoO00O ( ) )
 import urlresolver
 try : ooooOoO0O . play ( url )
 except : pass
 from urlresolver import common
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'LOADING' , 'Opening %s Now' % ( oOo0 ) )
 ooooOoO0O = xbmc . Player ( oOoO00O ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if Oo0oO0ooo . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  oooOOOOO = xbmcgui . Dialog ( )
  if oooOOOOO . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   oooOOOOO . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : ooooOoO0O . play ( url )
  except : pass
  try : o0oO0 . resolve_url ( url )
  except : pass
  Oo0oO0ooo . close ( )
  if 39 - 39: I1ii11iIi11i % IIiI1I
def OooO00O0OO0oo ( url ) :
 Oo0oO0ooo = xbmcgui . DialogProgress ( )
 Oo0oO0ooo . create ( 'Featching Your Video' , 'Featching Your Video' )
 Oo0oO0ooo . update ( 0 , '%s' % oOo0 )
 xbmc . sleep ( 1 )
 ooooOoO0O = xbmc . Player ( oOoO00O ( ) )
 Oo0oO0ooo . update ( 100 , '%s' % oOo0 )
 xbmc . sleep ( 1 )
 ooooOoO0O . play ( url ) . strip ( )
 Oo0oO0ooo . close ( )
 if 60 - 60: IIiIiII11i + I11i % oO00Oo0o000 + O0oOO0 . O00Oo000ooO0 % IIiIiII11i
def III1I1 ( url ) :
 ooooOoO0O = xbmc . Player ( oOoO00O ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : ooooOoO0O . play ( url ) . strip ( )
 except : pass
 if 58 - 58: O0oOO0
 if 45 - 45: I11i
def oOoO00O ( ) :
 try :
  o00ooOo = getSet ( "core-player" )
  if ( o00ooOo == 'DVDPLAYER' ) : iIoOO0OO00 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o00ooOo == 'MPLAYER' ) : iIoOO0OO00 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o00ooOo == 'PAPLAYER' ) : iIoOO0OO00 = xbmc . PLAYER_CORE_PAPLAYER
  else : iIoOO0OO00 = xbmc . PLAYER_CORE_AUTO
 except : iIoOO0OO00 = xbmc . PLAYER_CORE_AUTO
 return iIoOO0OO00
 return True
 if 75 - 75: IIiI1I * I1ii11iIi11i / oO00Oo0o000 * I1ii11iIi11i / O0oOO0
def oOO0OO0OO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiIi11IIi1I11 = [ ]
  if showcontext == 'fav' :
   IiIi11IIi1I11 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   IiIi11IIi1I11 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O000oOo . addContextMenuItems ( IiIi11IIi1I11 )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = True )
 return i1i1Ii11Ii
 if 65 - 65: OOooOOo * o0o00Oo0O - OOooOOo - oO0o
def O0OO ( name , url , mode , iconimage , fanart , description ) :
 if 96 - 96: Ii1I - o0o00Oo0O
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O000oOo . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = True )
 return i1i1Ii11Ii
 if 35 - 35: i1IiIIIII . Ii1i111I . oO00Oo0o000 - Ii1i111I % Ii1i111I + oO00Oo0o000
def oOo0O ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IiIi11IIi1I11 = [ ]
  if showcontext == 'fav' :
   IiIi11IIi1I11 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   IiIi11IIi1I11 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  O000oOo . addContextMenuItems ( IiIi11IIi1I11 )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = False )
 return i1i1Ii11Ii
 if 99 - 99: I11i + i1IiIIIII
 if 34 - 34: oO00Oo0o000 * I11i . oOo0O0Ooo % Ii
 if 61 - 61: iI11I1II1I1I + O0O0O * Ii1i111I - ooOoO0O00 % O0O0O
 if 76 - 76: O0O0O / OOooOOo
 if 12 - 12: oO00Oo0o000
 if 58 - 58: oO0o + iI11I1II1I1I % o0o00Oo0O + Ii1i111I + OOooOOo * ii
def o00oO0oo0OO ( heading , announce ) :
 class iII1IiI1iIi1I ( ) :
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
   try : OOO = open ( announce ) ; O0ooOoO = OOO . read ( )
   except : O0ooOoO = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O0ooOoO ) )
   return
 iII1IiI1iIi1I ( )
 iII1IiI1iIi1I ( )
 if 1 - 1: oO00Oo0o000 . O00Oo000ooO0 - O0oOO0
def IiI1O000oo0o ( ) :
 o00oO0oo0OO ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 4 - 4: oO00Oo0o000 * oOo0O0Ooo % oOo0O0Ooo / ii
 if 52 - 52: O0O0O + oO00Oo0o000 * oO00Oo0o000 * I1ii11iIi11i - iI11I1II1I1I + Ii1I
 if 34 - 34: IIiI1I / oO0o / I1ii11iIi11i
 if 92 - 92: oO00Oo0o000 % IIiI1I % I11i . oOo0O0Ooo - Ii1I - I11i
 if 40 - 40: oOo0O0Ooo / ii + oO0o * oO0o
def i1I1IiiIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 9 - 9: iI11I1II1I1I
 if 57 - 57: O0oOO0 / OoOO00O % I11i % Ii
 if 95 - 95: oO00Oo0o000 - I11i
 if 65 - 65: Ii - ii / o0o00Oo0O * O00Oo000ooO0 % Ii1i111I
 if 53 - 53: i1IiIIIII + oO00Oo0o000
 if 10 - 10: Ii1i111I * ooOoO0O00 . O0O0O / oO00Oo0o000 . i1IiIIIII / oO00Oo0o000
 if 1 - 1: IIiI1I % O0oOO0
 if 99 - 99: IIiI1I + iI11I1II1I1I . i1IiIIIII / oO0o * Ii1I
 if 87 - 87: O00Oo000ooO0 / IIiIiII11i % oO0o % oO0o
 if 28 - 28: OOooOOo % O0O0O - i1IiIIIII + i1IiIIIII + O0O0O / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * i1IiIIIII
 if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % OoOO00O
 if 81 - 81: oO0o - iI11I1II1I1I
 if 60 - 60: oO00Oo0o000
 if 77 - 77: oOo0O0Ooo / Ii1I
 if 95 - 95: oO00Oo0o000 * ooOoO0O00 + O0O0O
 if 40 - 40: IIiIiII11i
 if 7 - 7: i1IiIIIII / oO0o
 if 88 - 88: ooOoO0O00
 if 53 - 53: O0oOO0 . i1IiIIIII . I11i + O0O0O
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + OoOO00O % ooOoO0O00 . O0O0O
 if 57 - 57: O0O0O
 if 92 - 92: IIiIiII11i - oO0o - i1IiIIIII % oOo0O0Ooo - OOooOOo * oO00Oo0o000
def IiIi11 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0iIiI1I1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 45 - 45: oOo0O0Ooo + Ii1i111I + ooOoO0O00
def i1IIOOOoooOo00O ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + iiIIiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 67 - 67: Ii1I % ii
def III1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + I1I11Oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 6 - 6: oO00Oo0o000 / ii / IIiI1I / oO00Oo0o000 + IIiI1I - OOooOOo
def oO0 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + iIiII111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + iIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 67 - 67: Ii1i111I / o0o00Oo0O * OoOO00O - O00Oo000ooO0 . ii + O00Oo000ooO0
def i1I1iiiI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + i1IiIi1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 39 - 39: Ii + i1IiIIIII % IIiI1I + OoOO00O * oOo0O0Ooo + oO00Oo0o000
def Oo00oOo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0ooOo000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 81 - 81: ii - O00Oo000ooO0 - O00Oo000ooO0 + iI11I1II1I1I % Ii1i111I . ii
def o0ooo ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + Ii1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 87 - 87: ii
def iiI1 ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + OoIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 42 , oOoOoOoo0 , III1ii1I , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 61 - 61: oO0o / Ii1i111I % i1IiIIIII - O0oOO0
def IiI1i11i1iI ( url ) :
 O00oO = Iiii ( str ( OOO00O ) + o0oo0O0OO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O00oOoOO = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( O00oO )
 for oOo0 , url , oOoOoOoo0 , III1ii1I , Oo0 in o0O00oOoOO :
  o0OOOO00O0Oo ( oOo0 , url , 5 , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , OOoOO0oo0ooO + 'GenieTVRSSFeed.png' , Oo0 )
 oO00OOoO00 ( 'movies' , 'MAIN' )
 if 32 - 32: Ii1I / I1ii11iIi11i . OOooOOo + IIiI1I * OOooOOo * O00Oo000ooO0
 if 46 - 46: OoOO00O
 if 42 - 42: iI11I1II1I1I
 if 32 - 32: I1ii11iIi11i - OoOO00O . ii - ii - I1ii11iIi11i . iI11I1II1I1I
 if 34 - 34: I1ii11iIi11i
 if 31 - 31: ooOoO0O00 - Ii1i111I + oO00Oo0o000 + O0oOO0 . O0oOO0 . o0o00Oo0O
 if 33 - 33: ooOoO0O00 / IIiI1I * oO0o
 if 2 - 2: O0O0O . i1IiIIIII
 if 43 - 43: iI11I1II1I1I
def I1I1iIIiii1 ( ) :
 try :
  if os . path . exists ( oOOoO0 ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( oOOoO0 ) :
     I1IIiiiiI1iIi = 0
     I1IIiiiiI1iIi += len ( ooOOO0OooOo )
     if I1IIiiiiI1iIi > 0 :
      for OOO in ooOOO0OooOo :
       os . unlink ( os . path . join ( OOooo , OOO ) )
  ooOo0Oo = os . path . join ( OOooO0OOoo , "Textures13.db" )
  os . unlink ( ooOo0Oo )
  oooOOOOO . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 50 - 50: O0oOO0 * oO0o / OoOO00O % IIiIiII11i
 if 15 - 15: ooOoO0O00 . oOo0O0Ooo - OOooOOo % IIiIiII11i . O0oOO0 / O0O0O
 if 54 - 54: O0oOO0 - iI11I1II1I1I - Ii1i111I % OoOO00O / IIiIiII11i
 if 80 - 80: Ii % iI11I1II1I1I / Ii
 if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - OoOO00O - iI11I1II1I1I
 if 28 - 28: OOooOOo % ii
 if 13 - 13: O00Oo000ooO0 . I1ii11iIi11i - Ii1i111I / O0O0O - I1ii11iIi11i - oOo0O0Ooo
 if 84 - 84: IIiIiII11i
 if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
def O00O ( url ) :
 print '############################################################       DELETING STANDARD CACHE             ###############################################################'
 IIIIIi1 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( IIIIIi1 ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( IIIIIi1 ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 82 - 82: oO00Oo0o000 . ooOoO0O00 / O0O0O
   if 56 - 56: IIiI1I
   if I1IIiiiiI1iIi > 0 :
    if 23 - 23: ooOoO0O00
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete KODI Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 24 - 24: O00Oo000ooO0
     for OOO in ooOOO0OooOo :
      try :
       os . unlink ( os . path . join ( OOooo , OOO ) )
      except :
       pass
     for oOO in i1IIiIii1i :
      try :
       shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      except :
       pass
       if 51 - 51: i1IiIIIII % Ii
   else :
    pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  o0OoOoOo0O = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  if 37 - 37: ooOoO0O00 . oO00Oo0o000 - IIiIiII11i % I11i - ooOoO0O00 . O0O0O
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( o0OoOoOo0O ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 34 - 34: iI11I1II1I1I / IIiIiII11i
   if I1IIiiiiI1iIi > 0 :
    if 3 - 3: I11i - ii + IIiI1I . Ii1i111I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( I1IIiiiiI1iIi ) + " files found in 'Other'" , "Do you want to delete them?" ) :
     if 88 - 88: Ii1i111I - IIiI1I
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 68 - 68: I1ii11iIi11i % O0O0O . O00Oo000ooO0 - I11i / ooOoO0O00 / ii
   else :
    pass
  i1II11II11 = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  if 94 - 94: iI11I1II1I1I
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( i1II11II11 ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 1 - 1: o0o00Oo0O
   if I1IIiiiiI1iIi > 0 :
    if 2 - 2: oO0o . Ii1i111I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ATV2 Cache Files" , str ( I1IIiiiiI1iIi ) + " files found in 'LocalAndRental'" , "Do you want to delete them?" ) :
     if 97 - 97: I1ii11iIi11i
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 65 - 65: I1ii11iIi11i % i1IiIIIII / Ii / iI11I1II1I1I . oO00Oo0o000 + O0oOO0
   else :
    pass
    if 92 - 92: O0O0O
    if 96 - 96: oO00Oo0o000 * iI11I1II1I1I / OOooOOo % i1IiIIIII * IIiIiII11i
    if 3 - 3: i1IiIIIII . I1ii11iIi11i / Ii + oO0o
    if 47 - 47: O00Oo000ooO0 . i1IiIIIII
 O0oo00o000 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( O0oo00o000 ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( O0oo00o000 ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 5 - 5: Ii1I * OoOO00O % Ii1i111I % IIiIiII11i
   if 9 - 9: I11i % oO00Oo0o000 + Ii1i111I
   if I1IIiiiiI1iIi > 0 :
    if 55 - 55: oO0o - Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete WTF Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 38 - 38: iI11I1II1I1I % O00Oo000ooO0 % oO0o % o0o00Oo0O * iI11I1II1I1I / oO00Oo0o000
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 65 - 65: i1IiIIIII - oOo0O0Ooo * oO00Oo0o000
   else :
    pass
    if 99 - 99: oOo0O0Ooo
    if 64 - 64: Ii1I * OoOO00O * I1ii11iIi11i % O00Oo000ooO0 % O0oOO0
 OoO0000O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.4od/cache' ) , '' )
 if os . path . exists ( OoO0000O ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( OoO0000O ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 33 - 33: oO00Oo0o000 + IIiI1I - I1ii11iIi11i / OoOO00O + O0O0O . OOooOOo
   if 84 - 84: Ii / I11i % iI11I1II1I1I . O0oOO0 . oO0o / IIiI1I
   if I1IIiiiiI1iIi > 0 :
    if 55 - 55: IIiI1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete 4oD Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 3 - 3: iI11I1II1I1I
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 19 - 19: IIiIiII11i . oO0o * oO0o + oOo0O0Ooo % I1ii11iIi11i
   else :
    pass
    if 21 - 21: OOooOOo - Ii - OOooOOo
    if 4 - 4: Ii1i111I . O00Oo000ooO0
 I1I = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( I1I ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( I1I ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 36 - 36: Ii + OOooOOo . OOooOOo * o0o00Oo0O - Ii1i111I % oO00Oo0o000
   if 46 - 46: O0oOO0 / oOo0O0Ooo . O00Oo000ooO0 % oO0o / Ii
   if I1IIiiiiI1iIi > 0 :
    if 13 - 13: oO00Oo0o000 % I11i + i1IiIIIII + oO00Oo0o000 + Ii - Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete BBC iPlayer Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 11 - 11: IIiI1I
   else :
    pass
    if 20 - 20: OoOO00O . oO00Oo0o000 % OoOO00O
    if 5 - 5: i1IiIIIII + IIiI1I
    if 23 - 23: oO00Oo0o000 % iI11I1II1I1I . Ii1i111I
 OO0oO0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( OO0oO0O ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( OO0oO0O ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
   if 95 - 95: oO00Oo0o000 + O00Oo000ooO0 * iI11I1II1I1I
   if I1IIiiiiI1iIi > 0 :
    if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / OoOO00O
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Simple Downloader Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Ii1i111I
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 2 - 2: OoOO00O
   else :
    pass
    if 12 - 12: Ii - iI11I1II1I1I * O00Oo000ooO0 * IIiI1I
    if 19 - 19: o0o00Oo0O + O0O0O + I11i
 oO0IIi11IiiiI11i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( oO0IIi11IiiiI11i ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 68 - 68: O0O0O + Ii1i111I * O0O0O . O00Oo000ooO0 % OoOO00O - ii
   if 60 - 60: oO0o % Ii
   if I1IIiiiiI1iIi > 0 :
    if 7 - 7: O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete ITV Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 15 - 15: I1ii11iIi11i + IIiI1I + oOo0O0Ooo * I11i
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 33 - 33: I11i * I1ii11iIi11i
   else :
    pass
    if 88 - 88: oO00Oo0o000 % i1IiIIIII - OOooOOo - OOooOOo . oOo0O0Ooo
    if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - oO00Oo0o000
 Oo0OOo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.movies4me/cache' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( Oo0OOo ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 43 - 43: O00Oo000ooO0 % OoOO00O . i1IiIIIII / I1ii11iIi11i
   if 55 - 55: Ii1I % ii
   if I1IIiiiiI1iIi > 0 :
    if 73 - 73: ooOoO0O00 - IIiI1I % O0O0O / ooOoO0O00 + IIiIiII11i + Ii1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Movies4me Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 54 - 54: O0O0O
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 26 - 26: O0oOO0 % ii . oO00Oo0o000 * O0oOO0 + IIiIiII11i - Ii1I
   else :
    pass
    if 20 - 20: oO0o
    if 99 - 99: I1ii11iIi11i + ii . IIiI1I + o0o00Oo0O
 oo000o0O = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( oo000o0O ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 1 - 1: IIiIiII11i - ooOoO0O00 + O0O0O
   if 58 - 58: IIiI1I - ii
   if I1IIiiiiI1iIi > 0 :
    if 56 - 56: IIiI1I / IIiI1I
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Phoenix Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 21 - 21: o0o00Oo0O * O0oOO0 % OOooOOo / o0o00Oo0O
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 85 - 85: ii + ii
   else :
    pass
    if 23 - 23: ooOoO0O00
    if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Ii1i111I . oO0o
 oOOo0O0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.spotitube/cache' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( oOOo0O0Oo ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 50 - 50: O0O0O * Ii1i111I + i1IiIIIII - I1ii11iIi11i
   if 79 - 79: oO0o / ooOoO0O00
   if I1IIiiiiI1iIi > 0 :
    if 30 - 30: OOooOOo - Ii
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Music Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 94 - 94: OOooOOo % IIiI1I
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 39 - 39: OOooOOo + oO00Oo0o000 % o0o00Oo0O
   else :
    pass
    if 26 - 26: O0oOO0 + OOooOOo
    if 17 - 17: Ii1I - IIiI1I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * i1IiIIIII
 iIi1i1iiIiiiI = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.supercartoons/cache' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( iIi1i1iiIiiiI ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 79 - 79: ii * oO00Oo0o000 - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
   if 82 - 82: OOooOOo . OoOO00O
   if I1IIiiiiI1iIi > 0 :
    if 73 - 73: oO00Oo0o000
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete SuperCartoons Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 25 - 25: O00Oo000ooO0
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
   else :
    pass
    if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . OoOO00O - I1ii11iIi11i . Ii
    if 47 - 47: I1ii11iIi11i % oO0o - O0oOO0 - I1ii11iIi11i * O0O0O
 OOOOO0oOOoO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.tvonline.cc/cache' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( OOOOO0oOOoO ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 42 - 42: oOo0O0Ooo + Ii / oO0o
   if 64 - 64: O00Oo000ooO0
   if I1IIiiiiI1iIi > 0 :
    if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete TVonline Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 89 - 89: o0o00Oo0O + O00Oo000ooO0 * oO00Oo0o000
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 30 - 30: OOooOOo
   else :
    pass
    if 39 - 39: Ii1I + I11i + oO00Oo0o000 + O00Oo000ooO0
    if 48 - 48: oO00Oo0o000 / O0oOO0 . iI11I1II1I1I
 ooo0OOoo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.youtube/kodion' ) , '' )
 if os . path . exists ( oO0IIi11IiiiI11i ) == True :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( ooo0OOoo ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 52 - 52: oO0o
   if 49 - 49: OoOO00O . Ii1I % O0oOO0 . I1ii11iIi11i * i1IiIIIII
   if I1IIiiiiI1iIi > 0 :
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . O0oOO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete YouTube Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 20 - 20: IIiI1I + I11i . oO00Oo0o000 / Ii
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
      if 7 - 7: OOooOOo / OOooOOo . oO00Oo0o000 * o0o00Oo0O + O00Oo000ooO0 + O0O0O
   else :
    pass
    if 98 - 98: IIiIiII11i * O00Oo000ooO0 - oOo0O0Ooo % I11i - IIiI1I % Ii1I
    if 69 - 69: ooOoO0O00 % oO0o % oO00Oo0o000 / O0oOO0 / O0oOO0
    if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * O0oOO0
 iII = xbmc . translatePath ( 'special://masterprofile/addon_data/plugin.video.genesis' )
 oooOOOOO = xbmcgui . Dialog ( )
 try :
  if oooOOOOO . yesno ( "Delete Genesis Cache Files" , "Do you want to delete cache" ) :
   oooO0 = os . path . join ( iII , "cache.db" )
   os . unlink ( oooO0 )
   if 7 - 7: oO0o * IIiI1I
 except :
  pass
  if 16 - 16: oO00Oo0o000 . ooOoO0O00 . O00Oo000ooO0
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( "GenieTv" , "                               Finished Deleting Cache " , "                          [COLOR gold]Brought To You By GenieTv[/COLOR]" )
 if 50 - 50: oO0o - IIiIiII11i * ii - oOo0O0Ooo . o0o00Oo0O + o0o00Oo0O
 if 80 - 80: I11i
 if 50 - 50: O0oOO0
 if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * i1IiIIIII
 if 83 - 83: Ii - oOo0O0Ooo * Ii
 if 59 - 59: IIiI1I - ii / O0oOO0 + Ii1I . I11i - IIiI1I
 if 29 - 29: O0O0O
 if 26 - 26: o0o00Oo0O % i1IiIIIII - O00Oo000ooO0 . i1IiIIIII
 if 70 - 70: I11i + Ii1i111I / IIiI1I + O0oOO0 / oOo0O0Ooo
def iiioOo ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 II1IiI1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( II1IiI1II1 ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 21 - 21: ii . o0o00Oo0O / Ii
   if 86 - 86: OOooOOo / i1IiIIIII
   if I1IIiiiiI1iIi > 0 :
    if 40 - 40: iI11I1II1I1I / O0oOO0 / oOo0O0Ooo + Ii1I * i1IiIIIII
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: oO0o * O0oOO0 + O00Oo000ooO0 . O0O0O / O0oOO0
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
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
 if 91 - 91: OoOO00O + Ii1i111I - I1ii11iIi11i % OOooOOo . IIiI1I
 if 51 - 51: i1IiIIIII / Ii1i111I
 if 51 - 51: O0oOO0 * O0O0O - oO00Oo0o000 + IIiI1I
 if 46 - 46: I11i - Ii % oO0o / OoOO00O - OOooOOo
 if 88 - 88: O0O0O * oOo0O0Ooo / oO0o - i1IiIIIII / ooOoO0O00 . oO00Oo0o000
 if 26 - 26: Ii - O0oOO0
 if 45 - 45: O0oOO0 + IIiIiII11i % IIiI1I
 if 55 - 55: O0oOO0 - O0O0O % oOo0O0Ooo
 if 61 - 61: O0oOO0
def oOo0O0O0 ( url ) :
 print '###' + o0oOoO00o + ' - DELETING PACKAGES###'
 II1IiI1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( II1IiI1II1 ) :
   I1IIiiiiI1iIi = 0
   I1IIiiiiI1iIi += len ( ooOOO0OooOo )
   if 22 - 22: iI11I1II1I1I / O0oOO0 / oOo0O0Ooo - I11i
   if 21 - 21: O0O0O . Ii * Ii1i111I . i1IiIIIII / i1IiIIIII
   if I1IIiiiiI1iIi > 0 :
    if 42 - 42: ii / oO00Oo0o000 . I11i / o0o00Oo0O - O00Oo000ooO0 * O00Oo000ooO0
    oooOOOOO = xbmcgui . Dialog ( )
    if oooOOOOO . yesno ( "Delete Package Cache Files" , str ( I1IIiiiiI1iIi ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: OoOO00O % oO00Oo0o000
     for OOO in ooOOO0OooOo :
      os . unlink ( os . path . join ( OOooo , OOO ) )
     for oOO in i1IIiIii1i :
      shutil . rmtree ( os . path . join ( OOooo , oOO ) )
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
 O00O ( url )
 return
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % i1IiIIIII . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: oO00Oo0o000 % O0oOO0 - O0oOO0 % oOo0O0Ooo . i1IiIIIII - ii
 if 100 - 100: oOo0O0Ooo + OoOO00O + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * oO00Oo0o000 - OoOO00O + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
 if 36 - 36: O0O0O * IIiI1I + O00Oo000ooO0 * IIiI1I . Ii1I - iI11I1II1I1I
 if 14 - 14: Ii1i111I * O0O0O + Ii
 if 84 - 84: IIiI1I / IIiIiII11i
 if 86 - 86: oOo0O0Ooo
def oOoOO ( url , name ) :
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml' )
 oooOOOOO = xbmcgui . Dialog ( )
 Ii1IOOO0oOo00o0 = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml.bak' )
 if os . path . exists ( Ii1IOOO0oOo00o0 ) == False :
  if oooOOOOO . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + o0oOoO00o + ' - ADVANCED XML###'
   IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml' )
   try :
    os . remove ( Iiii111I1IiiI1i )
    print '=== GenieTv - REMOVING    ' + str ( Iiii111I1IiiI1i ) + '    ==='
   except :
    pass
   O00oO = i1 . http_GET ( url ) . content
   i11iiI1111 = open ( Iiii111I1IiiI1i , "w" )
   i11iiI1111 . write ( O00oO )
   i11iiI1111 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( Iiii111I1IiiI1i ) + '    ==='
   oooOOOOO = xbmcgui . Dialog ( )
   oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 else :
  print '###' + o0oOoO00o + ' - ADVANCED XML###'
  IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml' )
  try :
   os . remove ( Iiii111I1IiiI1i )
   print '=== GenieTv - REMOVING    ' + str ( Iiii111I1IiiI1i ) + '    ==='
  except :
   pass
  O00oO = i1 . http_GET ( url ) . content
  i11iiI1111 = open ( Iiii111I1IiiI1i , "w" )
  i11iiI1111 . write ( O00oO )
  i11iiI1111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiii111I1IiiI1i ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       Done Adding new Advanced XML" )
 return
 if 43 - 43: o0o00Oo0O / oO00Oo0o000 . iI11I1II1I1I - OOooOOo
def iiII1iiI ( url , name ) :
 print '###' + o0oOoO00o + ' - CHECK ADVANCE XML###'
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml' )
 try :
  i11iiI1111 = open ( Iiii111I1IiiI1i ) . read ( )
  if 'zero' in i11iiI1111 :
   name = '0CACHE'
  elif 'tuxen' in i11iiI1111 :
   name = 'TUXENS'
  elif 'muckys' in i11iiI1111 :
   name = 'MUCKYS'
  elif 'p2p1' in i11iiI1111 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i11iiI1111 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i11iiI1111 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 oooOOOOO = xbmcgui . Dialog ( )
 oooOOOOO . ok ( o0oOoO00o , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 57 - 57: Ii - Ii1i111I / O0oOO0 / I11i * Ii * I11i
def IiIii1iIIII ( url ) :
 print '###' + o0oOoO00o + ' - DELETING ADVANCE XML###'
 IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'advancedsettings.xml' )
 try :
  os . remove ( Iiii111I1IiiI1i )
  oooOOOOO = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( Iiii111I1IiiI1i ) + '    ==='
  oooOOOOO . ok ( o0oOoO00o , "       Remove Advanced Settings Sucessfull" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "       No Advanced Settings To Remove" )
 return
 if 92 - 92: O00Oo000ooO0 / iI11I1II1I1I
 if 43 - 43: O0oOO0 + ii + iI11I1II1I1I / ii
 if 65 - 65: i1IiIIIII
 if 14 - 14: O0oOO0
 if 75 - 75: iI11I1II1I1I % O0oOO0 / i1IiIIIII - IIiI1I % Ii
 if 11 - 11: Ii1i111I . OoOO00O
 if 87 - 87: i1IiIIIII + i1IiIIIII
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / OoOO00O . Ii1i111I * I11i
 if 21 - 21: IIiIiII11i
def iI1iIiii111 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 o0O00oOoOO = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( i1 . http_GET ( url ) . content )
 for ii1II1I , oOoo0oo0o0o , I1I11I1i1i1II , ii1II11IIII1 in o0O00oOoOO :
  if inc < 2 : oooOOOOO = xbmcgui . Dialog ( ) ; oooOOOOO . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ii1II1I , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1I11I1i1i1II , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ii1II11IIII1 )
  inc = inc + 1
  if 33 - 33: OoOO00O + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * O00Oo000ooO0
  if 21 - 21: o0o00Oo0O * O0oOO0 % oO0o
  if 14 - 14: o0o00Oo0O / oO00Oo0o000 / O0oOO0 + O00Oo000ooO0 - O00Oo000ooO0
  if 10 - 10: o0o00Oo0O - Ii1I / oO00Oo0o000 % OOooOOo / ii / OoOO00O
  if 73 - 73: O0oOO0 + O00Oo000ooO0 % I11i . Ii1I / i1IiIIIII . oO00Oo0o000
  if 76 - 76: Ii1i111I . Ii1I * ii % IIiI1I
  if 24 - 24: ii
  if 83 - 83: o0o00Oo0O / oO0o
  if 62 - 62: Ii1i111I
def o00O00oOooo ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV INI###'
  IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'addons2.ini' )
  O00oO = i1 . http_GET ( url ) . content
  i11iiI1111 = open ( Iiii111I1IiiI1i , "w" )
  i11iiI1111 . write ( O00oO )
  i11iiI1111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiii111I1IiiI1i ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New .ini File" )
 return
 if 85 - 85: ii . oO0o . oO0o
def o00O0O0OoO ( url , name ) :
 oooOOOOO = xbmcgui . Dialog ( )
 if oooOOOOO . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + o0oOoO00o + ' - CUSTOM FTV SETTINGS###'
  IiiioooOOoooo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  Iiii111I1IiiI1i = os . path . join ( IiiioooOOoooo , 'settings.xml' )
  O00oO = i1 . http_GET ( url ) . content
  i11iiI1111 = open ( Iiii111I1IiiI1i , "w" )
  i11iiI1111 . write ( O00oO )
  i11iiI1111 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( Iiii111I1IiiI1i ) + '    ==='
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "                               Done Adding New Settings" )
 return
 if 83 - 83: ooOoO0O00 - ii + oO0o * oOo0O0Ooo
 if 61 - 61: IIiI1I % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
def OOOO00oo00oo ( ) :
 try :
  OOIiI = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OOIiI ) == True :
   oooOOOOO = xbmcgui . Dialog ( )
   if oooOOOOO . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o0o00oo = os . path . join ( OOIiI , "source.db" )
    os . unlink ( o0o00oo )
  oooOOOOO . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  oooOOOOO = xbmcgui . Dialog ( )
  oooOOOOO . ok ( o0oOoO00o , "               Error Deleting Database No Database To Delete" )
 return
 if 45 - 45: o0o00Oo0O - OOooOOo % i1IiIIIII
 if 100 - 100: Ii . i1IiIIIII . Ii
 if 81 - 81: oOo0O0Ooo
 if 76 - 76: o0o00Oo0O - O0oOO0 / OoOO00O . I1ii11iIi11i - OoOO00O
 if 75 - 75: O0oOO0 % i1IiIIIII / I11i % IIiIiII11i
def Iiii ( url ) :
 oo0OooOOo0 = urllib2 . Request ( url )
 oo0OooOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 o0O = urllib2 . urlopen ( oo0OooOOo0 )
 O00oO = o0O . read ( )
 o0O . close ( )
 return O00oO
 if 30 - 30: I11i
 if 15 - 15: IIiIiII11i - OoOO00O - IIiI1I . O0O0O / Ii
 if 38 - 38: oO0o
 if 3 - 3: IIiIiII11i . oOo0O0Ooo / I1ii11iIi11i + I11i
 if 54 - 54: ooOoO0O00 - IIiIiII11i . ooOoO0O00
 if 33 - 33: IIiI1I + I1ii11iIi11i % Ii1i111I . O0O0O
 if 6 - 6: O00Oo000ooO0 + Ii1I
def OOOoooooO0oOOoO ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; I1I1 = plugintools . message_yes_no ( o0oOoO00o , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if I1I1 :
  oOoooo0OooO = xbmcaddon . Addon ( id = o00 ) . getAddonInfo ( 'path' ) ; oOoooo0OooO = xbmc . translatePath ( oOoooo0OooO ) ;
  OooO0O = os . path . join ( oOoooo0OooO , ".." , ".." ) ; OooO0O = os . path . abspath ( OooO0O ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OooO0O ) ; Oo0o = False
  try :
   for OOooo , i1IIiIii1i , ooOOO0OooOo in os . walk ( OooO0O , topdown = True ) :
    i1IIiIii1i [ : ] = [ oOO for oOO in i1IIiIii1i if oOO not in iiIIIII1i1iI ]
    for oOo0 in ooOOO0OooOo :
     try : os . remove ( os . path . join ( OOooo , oOo0 ) )
     except :
      if oOo0 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0o = True
      plugintools . log ( "Error removing " + OOooo + " " + oOo0 )
    for oOo0 in i1IIiIii1i :
     try : os . rmdir ( os . path . join ( OOooo , oOo0 ) )
     except :
      if oOo0 not in [ "Database" , "userdata" ] : Oo0o = True
      plugintools . log ( "Error removing " + OOooo + " " + oOo0 )
   if not Oo0o : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( o0oOoO00o , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( o0oOoO00o , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( o0oOoO00o , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oOoo0 ( )
 if 88 - 88: O0oOO0 / I1ii11iIi11i + OoOO00O % Ii * oO0o
 if 23 - 23: i1IiIIIII + O0oOO0 / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: IIiI1I - I11i
def OOOOo0o0O0 ( ) :
 I1 = [ ]
 I1i1 = sys . argv [ 2 ]
 if len ( I1i1 ) >= 2 :
  Ii1Ii = sys . argv [ 2 ]
  iIIOOoOOooO = Ii1Ii . replace ( '?' , '' )
  if ( Ii1Ii [ len ( Ii1Ii ) - 1 ] == '/' ) :
   Ii1Ii = Ii1Ii [ 0 : len ( Ii1Ii ) - 2 ]
  i1111II1iIII = iIIOOoOOooO . split ( '&' )
  I1 = { }
  for o0o00o0Oo in range ( len ( i1111II1iIII ) ) :
   I1ii11ii1iiI = { }
   I1ii11ii1iiI = i1111II1iIII [ o0o00o0Oo ] . split ( '=' )
   if ( len ( I1ii11ii1iiI ) ) == 2 :
    I1 [ I1ii11ii1iiI [ 0 ] ] = I1ii11ii1iiI [ 1 ]
    if 93 - 93: OOooOOo + Ii1i111I
 return I1
 if 27 - 27: iI11I1II1I1I * Ii1i111I
iiI1iiiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OooOOo0 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOoOO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOo00OOoOOO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
ooo0oooo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1iII11I1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
o0iIiI1I1II1 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i1i1ii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iiIIiI1I = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I1I11Oo0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIiII111 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iIi11 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
i1IiIi1I1i = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0ooOo000oo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Ii1Iii1 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoIII = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
I1i11II = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i1IiI1i = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOooo0O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
II1Ii1iI1i1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1OoOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IIIIIiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0oo0O0OO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IiI1 = base64 . decodestring ( 'Q1VOVA==' )
def o0OOOO00O0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O000oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IiIi11IIi1I11 = [ ]
  if showcontext == 'fav' :
   IiIi11IIi1I11 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOOOi11i1 :
   IiIi11IIi1I11 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  O000oOo . addContextMenuItems ( IiIi11IIi1I11 )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = True )
 return i1i1Ii11Ii
 if 16 - 16: Ii1i111I / ii . ooOoO0O00
def OOooOoooOoOo ( name , url , mode , iconimage , fanart , description ) :
 iii1IIiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i1i1Ii11Ii = True
 O000oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O000oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 O000oOo . setProperty ( "Fanart_Image" , fanart )
 i1i1Ii11Ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1IIiI , listitem = O000oOo , isFolder = False )
 return i1i1Ii11Ii
 if 90 - 90: I11i % Ii1I / OOooOOo
 if 85 - 85: oO00Oo0o000 - O0oOO0 - IIiI1I
Ii1Ii = OOOOo0o0O0 ( )
o00OooO0oo = None
oOo0 = None
O00o = None
oOoOoOoo0 = None
III1ii1I = None
Oo0 = None
IiI = None
if 80 - 80: oOo0O0Ooo % O00Oo000ooO0 / Ii1i111I * oO0o - O0O0O / O0O0O
if 13 - 13: I1ii11iIi11i
try :
 IiI = int ( Ii1Ii [ "fav_mode" ] )
except :
 pass
 if 70 - 70: IIiI1I
try :
 o00OooO0oo = urllib . unquote_plus ( Ii1Ii [ "url" ] )
except :
 pass
try :
 oOo0 = urllib . unquote_plus ( Ii1Ii [ "name" ] )
except :
 pass
try :
 oOoOoOoo0 = urllib . unquote_plus ( Ii1Ii [ "iconimage" ] )
except :
 pass
try :
 O00o = int ( Ii1Ii [ "mode" ] )
except :
 pass
try :
 III1ii1I = urllib . unquote_plus ( Ii1Ii [ "fanart" ] )
except :
 pass
try :
 Oo0 = urllib . unquote_plus ( Ii1Ii [ "description" ] )
except :
 pass
 if 51 - 51: o0o00Oo0O - Ii1I / Ii1i111I * IIiIiII11i + oO0o % Ii1I
 if 58 - 58: O0O0O + O00Oo000ooO0 % IIiI1I - OoOO00O - i1IiIIIII % OoOO00O
print str ( O0OoO000O0OO ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O00o )
print "URL: " + str ( o00OooO0oo )
print "Name: " + str ( oOo0 )
print "IconImage: " + str ( oOoOoOoo0 )
if 86 - 86: I11i
if 15 - 15: O0O0O - iI11I1II1I1I - IIiIiII11i - O00Oo000ooO0 % Ii1I
def oO00OOoO00 ( content , viewType ) :
 if 80 - 80: O00Oo000ooO0 * IIiI1I . ooOoO0O00 % OoOO00O % Ii1I + O0oOO0
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if o0oO0 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % o0oO0 . getSetting ( viewType ) )
  if 6 - 6: Ii1I . O0O0O . oO0o + O00Oo000ooO0
if oOoOoOoo0 == None : oOoOoOoo0 = ii11iIi1I
if III1ii1I == None : III1ii1I = i1iIIi1
if O00o == None :
 iiIiI ( )
 if 65 - 65: Ii1I / O0oOO0
elif O00o == 1 :
 iI ( o00OooO0oo )
 if 23 - 23: i1IiIIIII / i1IiIIIII * I11i * i1IiIIIII
elif O00o == 44 :
 iiOOOO0o ( o00OooO0oo )
 if 57 - 57: IIiI1I
elif O00o == 2 :
 oO00OoOO ( )
 if 29 - 29: oOo0O0Ooo
elif O00o == 3 :
 I11oo0ooOO ( )
 if 41 - 41: oO00Oo0o000 * oO0o - IIiI1I . OoOO00O
elif O00o == 21 :
 iI1Ii11111iIi ( )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - O0O0O + oO00Oo0o000
elif O00o == 4 :
 O0OO0oOOo ( )
 if 22 - 22: o0o00Oo0O % O00Oo000ooO0 % IIiI1I % oOo0O0Ooo
elif O00o == 5 :
 iii11II1I ( o00OooO0oo )
 if 34 - 34: IIiI1I . I1ii11iIi11i % Ii1I . IIiI1I % O00Oo000ooO0 / O00Oo000ooO0
elif O00o == 6 :
 iiioOo ( o00OooO0oo )
 if 84 - 84: OoOO00O
elif O00o == 7 :
 oOoOO ( o00OooO0oo , oOo0 )
 if 1 - 1: O0O0O - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
elif O00o == 8 :
 iiII1iiI ( o00OooO0oo , oOo0 )
 if 9 - 9: IIiI1I - IIiI1I
elif O00o == 9 :
 FIXREPOSADDONS ( o00OooO0oo )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + O0O0O
elif O00o == 10 :
 i1I1IiiIi1i ( )
 if 20 - 20: oO0o + Ii1i111I . IIiIiII11i / Ii
elif O00o == 11 :
 IiIii1iIIII ( o00OooO0oo )
 if 50 - 50: ii / oO0o % iI11I1II1I1I
elif O00o == 12 :
 iI1iIiii111 ( )
 if 41 - 41: Ii1I % Ii1I + O00Oo000ooO0 . IIiI1I % oO00Oo0o000 * O0oOO0
elif O00o == 13 :
 I1I1iIIiii1 ( )
 if 57 - 57: OoOO00O . oO00Oo0o000 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
elif O00o == 14 :
 O00O ( o00OooO0oo )
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
elif O00o == 15 :
 OooOOO0O00 ( )
 if 93 - 93: O0oOO0 / i1IiIIIII * o0o00Oo0O
elif O00o == 16 :
 o00O00oOooo ( o00OooO0oo , oOo0 )
 if 17 - 17: oO0o / O0oOO0 % oOo0O0Ooo
elif O00o == 17 :
 o00O0O0OoO ( o00OooO0oo , oOo0 )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
elif O00o == 18 :
 OOOO00oo00oo ( )
 if 60 - 60: Ii1I / O00Oo000ooO0 . Ii / oO0o % IIiIiII11i
elif O00o == 19 :
 IiiI11i1I ( o00OooO0oo )
 if 6 - 6: IIiI1I % I11i + oO00Oo0o000
elif O00o == 40 :
 ooOo0O ( oOo0 , o00OooO0oo , Oo0 )
 if 91 - 91: I11i + o0o00Oo0O * O0O0O * O00Oo000ooO0 * Ii1I
elif O00o == 42 :
 I1i ( oOo0 , o00OooO0oo , Oo0 )
 if 83 - 83: ii
elif O00o == 43 :
 o0Oo0 ( o00OooO0oo )
 if 52 - 52: I11i / OOooOOo % O0O0O % oO0o / O00Oo000ooO0 % I11i
elif O00o == 20 :
 oOOO ( o00OooO0oo )
 if 88 - 88: i1IiIIIII / Ii / OoOO00O / Ii * Ii1I % Ii1i111I
elif O00o == 22 :
 IiIi11 ( o00OooO0oo )
 if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * OoOO00O + iI11I1II1I1I
elif O00o == 23 :
 i1IIOOOoooOo00O ( o00OooO0oo )
 if 80 - 80: I11i . IIiI1I . ii
elif O00o == 24 :
 III1 ( o00OooO0oo )
 if 63 - 63: O0oOO0 . i1IiIIIII
elif O00o == 25 :
 oO0 ( o00OooO0oo )
 if 66 - 66: oOo0O0Ooo
elif O00o == 26 :
 I1Ii111I111 ( o00OooO0oo )
 if 99 - 99: oO0o % o0o00Oo0O . oO00Oo0o000 - Ii1I . I1ii11iIi11i / OOooOOo
elif O00o == 27 :
 i1I1iiiI ( o00OooO0oo )
 if 60 - 60: Ii1I
elif O00o == 28 :
 Oo00oOo ( o00OooO0oo )
 if 78 - 78: O0O0O + IIiIiII11i
elif O00o == 29 :
 o0ooo ( o00OooO0oo )
 if 55 - 55: ii
elif O00o == 30 :
 IiIIiIIIiIii ( o00OooO0oo )
 if 90 - 90: oOo0O0Ooo
elif O00o == 31 :
 iiI1 ( o00OooO0oo )
 if 4 - 4: i1IiIIIII % O0oOO0 - i1IiIIIII - I11i
elif O00o == 32 :
 OOooO ( )
 if 30 - 30: O00Oo000ooO0
elif O00o == 33 :
 IIiiii ( )
 if 34 - 34: O0O0O - IIiIiII11i - I11i + IIiI1I + oO00Oo0o000
elif O00o == 35 :
 i111i11I1ii ( o00OooO0oo )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
elif O00o == 34 :
 o000 ( o00OooO0oo )
 if 20 - 20: Ii - IIiIiII11i - O0oOO0 % O0O0O . O0oOO0
elif O00o == 36 :
 O0II11i11II ( o00OooO0oo )
 if 50 - 50: iI11I1II1I1I + oO00Oo0o000 - Ii1i111I - ii
elif O00o == 37 :
 OOoO000O00oO ( o00OooO0oo )
 if 84 - 84: OOooOOo - Ii1i111I
elif O00o == 38 :
 O0O0o0o0o ( o00OooO0oo )
 if 80 - 80: Ii % i1IiIIIII - I1ii11iIi11i % i1IiIIIII
elif O00o == 41 :
 OOOoooooO0oOOoO ( Ii1Ii )
 if 89 - 89: OoOO00O * Ii1i111I + OOooOOo / Ii
elif O00o == 39 :
 IiI1i11i1iI ( o00OooO0oo )
 if 68 - 68: ii * Ii1i111I
elif O00o == 45 :
 TEXTS ( )
 if 86 - 86: I11i / OOooOOo
elif O00o == 46 :
 IiI1O000oo0o ( )
 if 40 - 40: IIiI1I
elif O00o == 47 :
 GEVID ( )
 if 62 - 62: O0oOO0 / i1IiIIIII
elif O00o == 48 :
 Ooooo0OoO0 ( oOo0 , o00OooO0oo , Oo0 )
 if 74 - 74: IIiI1I % oO00Oo0o000 / oO00Oo0o000 - iI11I1II1I1I - IIiIiII11i + i1IiIIIII
elif O00o == 49 :
 I1i11IiI11i1 ( )
 if 92 - 92: Ii1i111I % oO00Oo0o000
elif O00o == 222 :
 iI1iiiiIii ( o00OooO0oo )
 if 18 - 18: O0oOO0 + oO00Oo0o000 / i1IiIIIII / O0O0O + iI11I1II1I1I % O00Oo000ooO0
elif O00o == 333 :
 O0O00oOo0o000 ( o00OooO0oo )
 if 94 - 94: Ii1i111I
 if 37 - 37: O0O0O
elif O00o == 1020 :
 IIi1I1 ( )
 if 52 - 52: Ii1I * oOo0O0Ooo . i1IiIIIII + ooOoO0O00 % O0O0O / iI11I1II1I1I
elif O00o == 1021 :
 ANIMEEP ( )
 if 68 - 68: oO00Oo0o000 - OOooOOo . Ii + I11i
elif O00o == 1022 :
 ANIMEPLAY ( o00OooO0oo )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
elif O00o == 1001 :
 Oo0O0o00o00 ( )
 if 33 - 33: Ii1i111I . I1ii11iIi11i
elif O00o == 1005 :
 O0IIi1i ( )
 if 89 - 89: IIiI1I + ooOoO0O00 - O00Oo000ooO0 + O0oOO0 . IIiIiII11i
elif O00o == 1007 :
 oO0oi1I1iI1 ( o00OooO0oo )
 if 85 - 85: iI11I1II1I1I - OoOO00O * I1ii11iIi11i . O0O0O + oO00Oo0o000
elif O00o == 1010 :
 OoOoO00O ( o00OooO0oo )
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
elif O00o == 1011 :
 o0o0oooO00O0 ( o00OooO0oo )
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . IIiI1I / IIiI1I
elif O00o == 1012 :
 I111IiI11 ( o00OooO0oo )
 if 43 - 43: oOo0O0Ooo
elif O00o == 1030 :
 iiiI ( )
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
elif O00o == 1031 :
 IIi1 ( o00OooO0oo , oOoOoOoo0 )
 if 34 - 34: I11i % Ii1I + OoOO00O * Ii1i111I / O0O0O
elif O00o == 1032 :
 Ii1iII1ii1 ( o00OooO0oo )
 if 18 - 18: O0oOO0
elif O00o == 1006 :
 Parse . ParseURL ( o00OooO0oo )
 if 92 - 92: oO0o % iI11I1II1I1I / O00Oo000ooO0 * IIiI1I . ooOoO0O00 + O0O0O
elif O00o == 2030 :
 Parse . addonParseURL ( o00OooO0oo )
 if 24 - 24: O00Oo000ooO0 . IIiI1I * O00Oo000ooO0 % Ii . Ii + ooOoO0O00
elif O00o == 2031 :
 Parse . apkParseURL ( o00OooO0oo )
 if 64 - 64: iI11I1II1I1I / O00Oo000ooO0 / I1ii11iIi11i - Ii1I
elif O00o == 1002 :
 o0oO00oooo ( o00OooO0oo )
 if 100 - 100: O00Oo000ooO0 + ooOoO0O00 * oO0o
elif O00o == 1003 :
 ooo0Oo00O ( o00OooO0oo , oOoOoOoo0 )
 if 64 - 64: O0O0O * Ii . I1ii11iIi11i
elif O00o == 1004 :
 I1iII1 ( o00OooO0oo )
 if 52 - 52: I1ii11iIi11i / O0oOO0 / IIiI1I - I11i / IIiI1I
elif O00o == 1008 :
 oOiI1I ( )
 if 74 - 74: ooOoO0O00 . iI11I1II1I1I
elif O00o == 1009 :
 Oo00oo00o00Oo ( o00OooO0oo )
 if 85 - 85: oOo0O0Ooo
elif O00o == 2001 :
 oOOI1 ( )
 if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
elif O00o == 2002 :
 oOoo ( o00OooO0oo )
 if 72 - 72: ii . I11i + o0o00Oo0O
elif O00o == 1013 :
 II1i11i1iIi11 ( )
elif O00o == 10111113 :
 oo0O0oO0O0O ( o00OooO0oo )
 if 46 - 46: OOooOOo * Ii1i111I / O0O0O + I1ii11iIi11i + O00Oo000ooO0
elif O00o == 1014 :
 iIi11iI1i ( )
 if 95 - 95: I11i - OoOO00O
elif O00o == 1015 :
 Ii1iIi ( o00OooO0oo )
 if 67 - 67: Ii1I * I1ii11iIi11i % I11i
elif O00o == 1016 :
 OOO0O ( o00OooO0oo , oOoOoOoo0 , oOo0 )
 if 19 - 19: OOooOOo . i1IiIIIII . ii
elif O00o == 1017 :
 I1IIIiIiI1 ( )
 if 79 - 79: i1IiIIIII * O0oOO0 * oOo0O0Ooo * Ii1I / Ii1I
elif O00o == 1023 :
 ii1iiIi1 ( )
 if 62 - 62: O0oOO0 * OoOO00O % Ii1I - ooOoO0O00 - Ii1I
elif O00o == 1024 :
 IIi1i1IIi ( o00OooO0oo )
 if 24 - 24: i1IiIIIII
elif O00o == 1025 :
 o0oo0Ooo0 ( o00OooO0oo )
 if 71 - 71: O00Oo000ooO0 - ooOoO0O00
elif O00o == 4001 :
 I11IiI ( )
 if 56 - 56: OOooOOo + O0O0O
elif O00o == 4002 :
 ooO0oOOooOo0 ( )
 if 74 - 74: IIiI1I / oO00Oo0o000 / IIiIiII11i - IIiI1I / O0O0O % Ii1i111I
elif O00o == 4003 :
 IIi ( )
 if 19 - 19: O00Oo000ooO0 % ii + ii
elif O00o == 4004 :
 IiI1i ( )
 if 7 - 7: ooOoO0O00
elif O00o == 4005 :
 oOOoo00O00o ( )
 if 91 - 91: OOooOOo - OOooOOo . O00Oo000ooO0
elif O00o == 4006 :
 oO00oooOOoOo0 ( )
 if 33 - 33: oO00Oo0o000 - iI11I1II1I1I / OoOO00O % o0o00Oo0O
elif O00o == 4007 :
 iIIII ( )
 if 80 - 80: O00Oo000ooO0 % ii - O00Oo000ooO0
elif O00o == 4008 :
 I11iI1i1I11I11 ( )
 if 27 - 27: oO00Oo0o000 - I11i * Ii1I - oOo0O0Ooo
elif O00o == 4009 : o0Oo00 ( )
elif O00o == 4010 : i1I11IiI1iiII ( )
elif O00o == 3000 :
 oO00o0O00o ( )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - IIiI1I . OoOO00O
elif O00o == 3001 :
 OoOo ( )
 if 100 - 100: IIiIiII11i / oO00Oo0o000 / IIiI1I - Ii1I * iI11I1II1I1I
elif O00o == 3002 :
 IiI1iiIiII ( o00OooO0oo )
 if 7 - 7: ooOoO0O00 . O00Oo000ooO0 % Ii * Ii1I . Ii1i111I % Ii1I
elif O00o == 3003 :
 IIiiiI1iI ( o00OooO0oo )
 if 35 - 35: oOo0O0Ooo
elif O00o == 3004 :
 O0oO0o0OOOOOO ( o00OooO0oo )
 if 48 - 48: ii % ii - oO0o . OOooOOo
elif O00o == 404 :
 iii1i1Iiiiiii ( oOo0 , o00OooO0oo , oOoOoOoo0 )
 if 22 - 22: O0oOO0 . Ii . ii . ooOoO0O00
elif O00o == 405 :
 OooO00O0OO0oo ( o00OooO0oo )
 if 12 - 12: OOooOOo % i1IiIIIII + O0O0O . o0o00Oo0O % iI11I1II1I1I
elif O00o == 7030 :
 I1IiiI ( )
 if 41 - 41: ii
elif O00o == 7021 :
 OO0OOOOOo ( oOo0 )
 if 13 - 13: Ii1i111I + oO00Oo0o000 - oO00Oo0o000 % O0O0O / Ii1i111I
elif O00o == 7022 :
 iIIi11ii ( oOo0 )
 if 4 - 4: oOo0O0Ooo + i1IiIIIII - O00Oo000ooO0 + IIiI1I
elif O00o == 7000 :
 Oo0OOOOOOO0oo ( oOo0 , o00OooO0oo , img )
 if 78 - 78: OoOO00O
elif O00o == 7050 :
 OO000OOOo0Oo ( o00OooO0oo )
 if 29 - 29: IIiIiII11i
elif O00o == 7051 :
 oOoOOoo ( o00OooO0oo )
 if 79 - 79: iI11I1II1I1I - Ii + O0oOO0 - IIiIiII11i . iI11I1II1I1I
elif O00o == 7052 :
 oooOO0OO0 ( o00OooO0oo )
 if 84 - 84: I1ii11iIi11i % Ii1i111I * o0o00Oo0O * Ii1i111I
elif O00o == 7053 :
 iiI1i ( o00OooO0oo )
 if 66 - 66: i1IiIIIII / iI11I1II1I1I - OOooOOo % o0o00Oo0O . O0oOO0
elif O00o == 7054 :
 CoolPlay ( o00OooO0oo )
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
elif O00o == 7060 :
 iIIII1 ( )
 if 37 - 37: ooOoO0O00 * Ii
elif O00o == 7061 :
 OO0iiiii1iiIIii ( o00OooO0oo )
 if 95 - 95: Ii % oO00Oo0o000 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
elif O00o == 7063 :
 Oooo ( o00OooO0oo )
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / i1IiIIIII / oO00Oo0o000
elif O00o == 7062 :
 OO0Oo00OO0oo ( o00OooO0oo )
 if 35 - 35: IIiI1I * i1IiIIIII
elif O00o == 7064 :
 NATatozcat ( )
 if 65 - 65: IIiIiII11i % ooOoO0O00
elif O00o == 7067 :
 oOO00o0O0 ( o00OooO0oo )
 if 13 - 13: oO0o * oO00Oo0o000 + I1ii11iIi11i - O00Oo000ooO0
elif O00o == 7066 :
 NATatozA ( o00OooO0oo )
 if 31 - 31: oO0o
elif O00o == 7065 :
 iIIii1iiiIiiI ( o00OooO0oo )
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
elif O00o == 7070 :
 oooOOo0oOoOO ( )
 if 77 - 77: Ii - oO00Oo0o000 . Ii1I % I1ii11iIi11i . OoOO00O
elif O00o == 7071 :
 DIZIlist ( o00OooO0oo )
 if 9 - 9: I11i
elif O00o == 7072 :
 DIZIpull ( o00OooO0oo )
 if 55 - 55: i1IiIIIII % iI11I1II1I1I + Ii1i111I . O0oOO0
elif O00o == 7073 :
 WATCHDIZI ( o00OooO0oo )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
elif O00o == 7002 :
 I1Ii1ii ( )
 if 23 - 23: Ii
elif O00o == 7003 :
 Iii1Iii ( o00OooO0oo )
 if 88 - 88: IIiIiII11i - IIiI1I / ii
elif O00o == 7004 :
 IiOOo0 ( o00OooO0oo )
 if 71 - 71: Ii1I
elif O00o == 7020 :
 IiiIII1IIii1 ( o00OooO0oo )
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
elif O00o == 7001 :
 o0III11IiI ( )
 if 1 - 1: O00Oo000ooO0 % ooOoO0O00
elif O00o == 7010 :
 oO0OOO ( o00OooO0oo )
 if 41 - 41: oO0o * oO0o / IIiI1I + Ii1I . I11i
elif O00o == 7011 :
 O000oooO0 ( o00OooO0oo )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / OoOO00O
elif O00o == 7012 :
 III1i1IIII1i ( o00OooO0oo )
 if 80 - 80: Ii1I
elif O00o == 7013 :
 cnfTVPlay2 ( o00OooO0oo )
elif O00o == 7014 :
 CNF_Studio_Indexer . MV_Movies ( o00OooO0oo )
elif O00o == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( o00OooO0oo )
elif O00o == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( oOo0 , o00OooO0oo , oOoOoOoo0 )
elif O00o == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O00o == 7018 :
 iiII ( )
elif O00o == 7019 :
 CNF_Studio_Indexer . List_Movies ( o00OooO0oo )
elif O00o == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( o00OooO0oo )
elif O00o == 7024 :
 CNF_Studio_Indexer . Box_Office ( o00OooO0oo )
 if 67 - 67: IIiIiII11i
elif O00o == 8000 :
 o0oOO ( )
elif O00o == 8001 :
 IiiiIIi ( )
elif O00o == 8002 :
 I11IIII ( )
elif O00o == 8003 :
 iI11I ( )
elif O00o == 8004 :
 IIi1II ( )
elif O00o == 8005 :
 OOOii ( )
elif O00o == 8006 :
 I1iIiiiIi1111I ( oOo0 , o00OooO0oo )
elif O00o == 8030 :
 OooOO0o0 ( o00OooO0oo )
elif O00o == 8045 :
 Ii11 ( o00OooO0oo )
elif O00o == 8046 :
 I1i1ii ( o00OooO0oo )
elif O00o == 8047 :
 OOOOoO ( o00OooO0oo )
elif O00o == 8048 :
 II11iIIii ( o00OooO0oo )
elif O00o == 8049 :
 oooOo0Ooo0oo ( o00OooO0oo )
elif O00o == 8020 :
 oOOOOOoOOoo0 ( )
elif O00o == 8021 :
 oo0OOO0OOoOO ( o00OooO0oo )
elif O00o == 8022 :
 oOoO ( o00OooO0oo )
elif O00o == 8023 :
 II1i1 ( o00OooO0oo )
elif O00o == 8040 :
 oOo0OOOOoO ( )
elif O00o == 8041 :
 iii11i1 ( o00OooO0oo )
elif O00o == 8042 :
 OO0oo00oOO ( o00OooO0oo )
elif O00o == 8043 :
 yt . PlayVideo ( o00OooO0oo )
elif O00o == 8044 :
 I1iOO0O0O ( o00OooO0oo )
elif O00o == 8060 :
 IiI1I ( )
elif O00o == 8061 :
 IIIiIi1iiI ( o00OooO0oo )
elif O00o == 8064 :
 o0Iiii ( )
elif O00o == 8065 :
 I1i1I ( o00OooO0oo )
elif O00o == 8070 :
 i11Ii1iIIIIi ( )
elif O00o == 8071 :
 iii ( o00OooO0oo )
elif O00o == 7080 :
 O000OOO ( o00OooO0oo )
elif O00o == 8090 :
 OO000OOo ( )
elif O00o == 8091 :
 oOo0O000Ooo0 ( o00OooO0oo )
elif O00o == 8092 :
 i11i ( o00OooO0oo )
elif O00o == 8081 :
 o0Ooi1II11i1iI1 ( )
elif O00o == 8062 :
 I1Ii1I ( o00OooO0oo )
elif O00o == 8063 :
 i1111iIII ( o00OooO0oo )
elif O00o == 8050 :
 i1i ( )
elif O00o == 8051 :
 IIIiiiI ( o00OooO0oo )
elif O00o == 8052 :
 OoO00oo00 ( o00OooO0oo )
elif O00o == 8085 :
 OO0ooO0oOO0o ( )
elif O00o == 8086 :
 ooOOo00 ( o00OooO0oo )
elif O00o == 8087 :
 oo00ooooOOo00 ( o00OooO0oo )
elif O00o == 8088 :
 ii1iOO00Oooo000 ( o00OooO0oo , oOo0 )
elif O00o == 9000 :
 iioo0o0OoOOO ( )
elif O00o == 1111 :
 ooooOoo00 ( )
elif O00o == 9001 :
 Iii1OOoO ( )
elif O00o == 9002 :
 IIIIii1 ( )
elif O00o == 9003 :
 IiI11I1Ii11II ( )
elif O00o == 50 :
 I11iiIi1i1 ( o00OooO0oo )
elif O00o == 9020 :
 champlist ( )
elif O00o == 9021 :
 i11IiIi ( )
elif O00o == 9022 :
 I111O0 ( )
elif O00o == 9023 :
 oooIiII ( )
elif O00o == 9024 :
 oO0o000oOO ( o00OooO0oo )
elif O00o == 9030 :
 I1ii1iI ( o00OooO0oo )
elif O00o == 9031 :
 i1i1IIi ( o00OooO0oo )
elif O00o == 9032 :
 i1Ii1i1ii1 ( o00OooO0oo )
elif O00o == 9033 :
 oOOoOOooO0 ( o00OooO0oo )
elif O00o == 7085 :
 OoOooO0 ( o00OooO0oo )
elif O00o == 7086 :
 iiIi ( o00OooO0oo )
elif O00o == 7087 :
 OoO ( Oo0 )
elif O00o == 9666 :
 oOo0O0O0 ( o00OooO0oo )
elif O00o == 10100 : i1II11I11ii1 ( )
elif O00o == 10105 : ooO000OO ( o00OooO0oo )
elif O00o == 10106 : oo0oOO ( o00OooO0oo )
elif O00o == 10104 : O0oO0oo0O ( o00OooO0oo )
elif O00o == 10107 : Oo0o0O0o ( )
elif O00o == 10103 : I1II1IiI1 ( o00OooO0oo )
elif O00o == 10108 : ii1OO0 ( o00OooO0oo )
elif O00o == 10107 : Oo0o0O0o ( )
elif O00o == 10000 : Origin_Menu ( )
elif O00o == 10001 : iiIIi ( )
elif O00o == 10002 : Iiii1Ii ( )
elif O00o == 10003 : oOoO0O00oo ( )
elif O00o == 10004 : i1iI1IIIII1 ( o00OooO0oo )
elif O00o == 10005 : iI1 ( )
elif O00o == 10006 : oo0OOOOO0 ( o00OooO0oo )
elif O00o == 10007 : iIIi1 ( o00OooO0oo , oOoOoOoo0 )
elif O00o == 10008 : OoooOo0 ( )
elif O00o == 10009 : i1ii1I1IIIII ( )
elif O00o == 10010 : o00OoOO0O0 ( o00OooO0oo )
elif O00o == 10011 : i11i11i ( o00OooO0oo )
elif O00o == 10012 : III1I1 ( o00OooO0oo )
elif O00o == 10013 : OOoO0oooo ( o00OooO0oo )
elif O00o == 10014 : iiii1 ( )
elif O00o == 10015 : oo0i1iIIi1II1iiI ( )
elif O00o == 10016 : i1i1 ( o00OooO0oo )
elif O00o == 10017 : oo0iIiI ( )
elif O00o == 10018 : i1Iio0oO00 ( )
elif O00o == 10019 : I1ii1i ( )
elif O00o == 10020 : O0000oO0o00 ( )
elif O00o == 10021 : OO0ooOoOO0OOo ( )
elif O00o == 10022 : Oo ( o00OooO0oo )
elif O00o == 10023 : I1IiiIiii1 ( oOo0 , o00OooO0oo )
elif O00o == 10024 : iI1I1I1i1i ( o00OooO0oo )
elif O00o == 10025 : OOoO0oo0O ( )
elif O00o == 10026 : oo0oooo0OoO0o ( )
elif O00o == 10027 : I1IIiiI1II1 ( )
elif O00o == 10028 : Ooo0o0oo0 ( )
elif O00o == 10029 : IIoO00OoOo ( )
elif O00o == 423 : Ii1i1 ( o00OooO0oo )
elif O00o == 426 : O0OOO0 ( o00OooO0oo )
elif O00o == 10030 : Izle_Films ( )
elif O00o == 10031 : Latest_Izle_Movies ( )
elif O00o == 10032 : Izle_Genres ( )
elif O00o == 10033 : Izle_Pop_Movies ( )
elif O00o == 10034 : Izle_Boxsets ( )
elif O00o == 10035 : Izle_Search ( )
elif O00o == 10036 : Izle_Genres_Movie ( o00OooO0oo )
elif O00o == 10037 : Izle_Boxset_single ( o00OooO0oo )
elif O00o == 10038 : Izle_IFRAME ( )
elif O00o == 10039 : Izle_Boxsets_Next ( o00OooO0oo )
elif O00o == 10040 : O00oo ( )
elif O00o == 10041 : iII1I11 ( o00OooO0oo )
elif O00o == 10042 : iI1ii1Ii ( o00OooO0oo )
elif O00o == 10043 : O0oO0OOoO ( )
elif O00o == 10044 : IiiI11I1IIiI ( o00OooO0oo )
elif O00o == 10045 : o0oOo00 ( oOo0 )
elif O00o == 10046 : oO0Oo ( o00OooO0oo )
elif O00o == 10047 : O0OO0ooO00 ( o00OooO0oo )
elif O00o == 10048 : OooOO0oOOo0O ( o00OooO0oo )
elif O00o == 10049 : Ii1III1 ( o00OooO0oo )
elif O00o == 10050 : oO0o0 ( )
elif O00o == 10051 : o0i1I ( )
elif O00o == 10052 : III1iI1Ii11Ii ( )
elif O00o == 10053 : Addon ( o00OooO0oo )
elif O00o == 10054 : OOoOo ( o00OooO0oo , oOo0 )
elif O00o == 10055 :
 I1III1iIi ( "addFavorite" )
 try :
  oOo0 = oOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOo0 = oOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 Iii ( oOo0 , o00OooO0oo , oOoOoOoo0 , III1ii1I , IiI )
elif O00o == 10056 :
 I1III1iIi ( "rmFavorite" )
 try :
  oOo0 = oOo0 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  oOo0 = oOo0 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOo0Oo0O0O ( oOo0 )
elif O00o == 10057 :
 I1III1iIi ( "getFavorites" )
 i1IiiiiIi1I ( )
elif O00o == 10058 : iIIII1iIIii ( )
elif O00o == 10059 : Donators_Guide ( )
elif O00o == 10060 : ii1O0 ( )
elif O00o == 10061 : o0ooO ( )
elif O00o == 10062 : OO00 ( oOo0 , o00OooO0oo , Oo0 )
elif O00o == 10063 : i1iIiIIIII ( )
elif O00o == 10064 : iiIi1iI1iIii ( )
elif O00o == 10065 : O00OoOO0oo0 ( o00OooO0oo )
elif O00o == 10066 : Oo00000o0o ( o00OooO0oo )
elif O00o == 10068 : i1II ( o00OooO0oo )
elif O00o == 10069 : oooOoOOO0oo0o ( o00OooO0oo )
elif O00o == 10070 : i1iI1 ( o00OooO0oo )
elif O00o == 10071 : Genie_Watch ( )
elif O00o == 10072 : iiO0oOo00o ( )
elif O00o == 10073 : i11i1ii1I ( o00OooO0oo )
elif O00o == 10074 : iI1i111I1Ii ( o00OooO0oo )
elif O00o == 10075 : O0oOOoooOO0O ( oOoOoOoo0 , oOo0 , o00OooO0oo )
elif O00o == 10076 : O0oo0O ( o00OooO0oo )
elif O00o == 10077 : iI1II ( o00OooO0oo )
elif O00o == 10078 : Ii1Iii1iIi ( )
elif O00o == 10079 : Genie_Watch_Tv_Shows ( )
elif O00o == 10080 : Genie_Watch_Tv_Genre ( o00OooO0oo )
elif O00o == 10081 : Genie_Watch_TV_PlayRun ( o00OooO0oo )
elif O00o == 10082 : Genie_Watch_TV_Episodes ( o00OooO0oo , oOoOoOoo0 )
elif O00o == 10083 : Genie_Watch_Tv_Recent ( o00OooO0oo )
elif O00o == 10084 : oOOOoo0O0oO ( )
elif O00o == 10085 : i1iIi ( )
elif O00o == 10086 : IIII ( )
elif O00o == 20000 : o0o ( )
elif O00o == 20001 : OoOoO0OoOOOOo ( )
elif O00o == 20002 : Iiii1iIii ( o00OooO0oo )
elif O00o == 20003 : I1III1II1I11 ( o00OooO0oo )
elif O00o == 20004 : OO000o ( o00OooO0oo )
elif O00o == 21004 : I1i111i ( )
elif O00o == 21005 : iI1i ( o00OooO0oo )
elif O00o == 21006 : OOO00OOo0o0Oo ( o00OooO0oo )
elif O00o == 21007 : Oo0oOo0O0O0o ( o00OooO0oo )
elif O00o == 30000 : IIiiiiIiIIii ( )
elif O00o == 30001 : II1 ( )
elif O00o == 10012 : Resolve ( o00OooO0oo )
elif O00o == 30003 : o0Oo ( )
elif O00o == 30004 : IiI1i111IiIiIi1 ( o00OooO0oo )
elif O00o == 30005 : OOO0o0OO0OO ( o00OooO0oo )
elif O00o == 30006 : Oo0oOooOoOo ( )
elif O00o == 30007 : ooOo0O0o0 ( )
elif O00o == 30008 : O0oOoo0OoO0O ( o00OooO0oo )
elif O00o == 30009 : oO00oOOo0Oo ( o00OooO0oo )
elif O00o == 30010 : oOOo0oo0o0o0 ( o00OooO0oo )
elif O00o == 30011 : I1ii1II1iII ( )
elif O00o == 30012 : ooIi1IiIiIi1IiI ( )
elif O00o == 30013 : oOOo00o0OO ( )
elif O00o == 30014 : Oo0Oo00o00oO ( )
elif O00o == 30015 : oo0OoOooo ( o00OooO0oo , oOoOoOoo0 , III1ii1I )
elif O00o == 30016 : oOoooO0 ( o00OooO0oo )
elif O00o == 30019 : oOO0o000Oo00o ( o00OooO0oo )
elif O00o == 30017 : IiiIi1IIII1i ( o00OooO0oo )
elif O00o == 30018 : IiiIi ( o00OooO0oo )
elif O00o == 30030 : I1ii11I ( )
elif O00o == 30031 : II1II1IIII ( )
elif O00o == 30032 : i1iiiiI1IiIIii ( )
elif O00o == 30033 : IIIIiii ( )
elif O00o == 30034 : Ii11Ii1iI ( )
elif O00o == 30035 : oOOoooO ( o00OooO0oo )
elif O00o == 30036 : i1ii11 ( o00OooO0oo )
elif O00o == 30037 : ii1i ( o00OooO0oo )
elif O00o == 30038 : OOo0 ( )
elif O00o == 30039 : oooOO0OO0O ( )
elif O00o == 50000 : IiI111111IIII ( )
if 2 - 2: I11i - o0o00Oo0O * OoOO00O % O00Oo000ooO0
if 64 - 64: ooOoO0O00 . O0oOO0
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
